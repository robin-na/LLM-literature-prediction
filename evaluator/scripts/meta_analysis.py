from __future__ import annotations

from collections import Counter, OrderedDict
from pathlib import Path

from utils.columns import COLUMN_MAP
from utils.csvio import Row, read_csv, write_csv
from utils.finalize import read_review_events
from utils.helpers import group_by_paper, is_empty_like
from utils.matching import classify_match
from utils.paths import GROUND_TRUTH_CSV, LLM_DATASET_CSV, REVIEW_DATA_CSV, REVIEW_EVENTS_CSV, STATE_DIR
from utils.review_state import build_classification_overrides
from utils.row_alignment import align_rows

OverrideKey = tuple[str, str, str]


def matching_label(field_label: str) -> str:
    return "Lab / Experiment" if field_label == "Lab_Or_Field" else field_label


def canon_stage2_classification(value: str) -> str:
    value = (value or "").strip().replace("-", "_")
    if value in {"match", "close", "both_empty"}:
        return "match"
    if value in {"mismatch", "one_empty", "missing_row"}:
        return "mismatch"
    return value


def _parse_ui_key(key: str) -> OverrideKey | None:
    parts = (key or "").split("|")
    if len(parts) < 3:
        return None
    paper_id = parts[0]
    row_index = parts[1]
    field_label = "|".join(parts[2:])
    if not (paper_id or row_index or field_label):
        return None
    return (paper_id, row_index, field_label)


def load_overrides_from_events(review_session_id: str) -> dict[OverrideKey, str]:
    events = read_review_events(REVIEW_EVENTS_CSV, review_session_id)
    overrides_ui = build_classification_overrides(events)
    overrides: dict[OverrideKey, str] = {}
    for key, cls in overrides_ui.items():
        parsed = _parse_ui_key(key)
        if parsed:
            overrides[parsed] = cls
    return overrides


def load_overrides_from_review_data(path: Path) -> dict[OverrideKey, str]:
    if not path.exists():
        return {}
    overrides: dict[OverrideKey, str] = {}
    for row in read_csv(path):
        key: OverrideKey = (row.get("paper_id", ""), row.get("row_index", ""), row.get("field", ""))
        if key == ("", "", ""):
            continue
        if row.get("manually_reviewed") == "yes":
            overrides[key] = row.get("final_classification", "")
    return overrides


def iter_row_pairs(human_rows: list[Row], llm_rows: list[Row]) -> list[tuple[int, Row | None, Row | None]]:
    return [(i, h, l) for i, (h, l) in enumerate(align_rows(human_rows, llm_rows, column_map=COLUMN_MAP))]


def build_field_level_rows(human_rows: list[Row], llm_rows: list[Row], overrides: dict[OverrideKey, str]) -> list[Row]:
    human_groups = group_by_paper(human_rows, "Filename")
    llm_groups = group_by_paper(llm_rows, "custom_id", strip_md=True)
    all_papers = list(OrderedDict.fromkeys(list(human_groups.keys()) + list(llm_groups.keys())))
    out: list[Row] = []
    for paper_id in all_papers:
        h_rows = human_groups.get(paper_id, [])
        l_rows = llm_groups.get(paper_id, [])
        for row_index, h, l in iter_row_pairs(h_rows, l_rows):
            for field_label, (h_col, l_col) in COLUMN_MAP.items():
                h_val = ((h.get(h_col) if h else "") or "").strip()
                l_val = ((l.get(l_col) if l else "") or "").strip()
                auto_cls = classify_match(matching_label(field_label), h_val, l_val, h is not None, l is not None)
                auto_cls = canon_stage2_classification(auto_cls)
                ov_key: OverrideKey = (paper_id, str(row_index), field_label)
                final_cls = canon_stage2_classification(overrides.get(ov_key) or auto_cls)
                tp, tn, fp, fn = confusion_bucket(h_val, l_val, final_cls)
                out.append(
                    {
                        "paper_id": paper_id,
                        "row_index": str(row_index),
                        "field": field_label,
                        "ground_truth_value": h_val,
                        "llm_value": l_val,
                        "auto_classification": auto_cls,
                        "final_classification": final_cls,
                        "manually_reviewed": "yes" if ov_key in overrides else "no",
                        "TP": str(tp),
                        "TN": str(tn),
                        "FP": str(fp),
                        "FN": str(fn),
                    }
                )
    return out


def validate_columns(human_rows: list[Row], llm_rows: list[Row]) -> None:
    human_cols = set(human_rows[0].keys()) if human_rows else set()
    llm_cols = set(llm_rows[0].keys()) if llm_rows else set()
    required_human = {"Filename"} | {h for h, _ in COLUMN_MAP.values()}
    required_llm = {"custom_id"} | {l for _, l in COLUMN_MAP.values()}
    missing_h = sorted(required_human - human_cols)
    missing_l = sorted(required_llm - llm_cols)
    if missing_h:
        raise ValueError(f"Ground truth CSV missing required columns: {', '.join(missing_h)}")
    if missing_l:
        raise ValueError(f"LLM CSV missing required columns: {', '.join(missing_l)}")


def confusion_bucket(human_value: str, llm_value: str, final_classification: str) -> tuple[int, int, int, int]:
    gt_empty = is_empty_like(human_value)
    llm_empty = is_empty_like(llm_value)
    if gt_empty and llm_empty:
        return (0, 1, 0, 0)
    if (not gt_empty) and llm_empty:
        return (0, 0, 0, 1)
    if gt_empty and (not llm_empty):
        return (0, 0, 1, 0)
    if final_classification == "match":
        return (1, 0, 0, 0)
    if final_classification == "mismatch":
        return (0, 0, 1, 0)
    return (0, 0, 0, 0)


def safe_div(num: int, den: int) -> str:
    if den == 0:
        return ""
    return f"{(num / den):.4f}"


def summarize(field_rows: list[Row]) -> list[Row]:
    agg: "OrderedDict[str, Counter]" = OrderedDict()
    for row in field_rows:
        field = row["field"]
        agg.setdefault(field, Counter())
        agg[field]["TP"] += int(row["TP"])
        agg[field]["TN"] += int(row["TN"])
        agg[field]["FP"] += int(row["FP"])
        agg[field]["FN"] += int(row["FN"])

    out: list[Row] = []
    grand = Counter()
    for field, counts in agg.items():
        out.append(summary_row(field, counts))
        grand.update(counts)
    out.append(summary_row("GRAND_TOTAL", grand))
    return out


def summarize_paper_level(field_rows: list[Row]) -> list[Row]:
    agg: "OrderedDict[str, Counter]" = OrderedDict()
    for row in field_rows:
        paper = row["paper_id"]
        agg.setdefault(paper, Counter())
        agg[paper]["TP"] += int(row["TP"])
        agg[paper]["TN"] += int(row["TN"])
        agg[paper]["FP"] += int(row["FP"])
        agg[paper]["FN"] += int(row["FN"])
    out: list[Row] = []
    for paper, counts in agg.items():
        tp = counts.get("TP", 0)
        tn = counts.get("TN", 0)
        fp = counts.get("FP", 0)
        fn = counts.get("FN", 0)
        total = tp + tn + fp + fn
        out.append(
            {
                "paper_id": paper,
                "TP": str(tp),
                "TN": str(tn),
                "FP": str(fp),
                "FN": str(fn),
                "total_observations": str(total),
                "accuracy": safe_div(tp + tn, total),
            }
        )
    return out


def summary_row(field: str, counts: Counter) -> Row:
    tp = counts.get("TP", 0)
    tn = counts.get("TN", 0)
    fp = counts.get("FP", 0)
    fn = counts.get("FN", 0)
    total = tp + tn + fp + fn
    return {
        "field": field,
        "TP": str(tp),
        "TN": str(tn),
        "FP": str(fp),
        "FN": str(fn),
        "total_observations": str(total),
        "accuracy": safe_div(tp + tn, total),
        "precision": safe_div(tp, tp + fp),
        "sensitivity": safe_div(tp, tp + fn),
        "specificity": safe_div(tn, tn + fp),
    }


def main() -> None:
    overrides = load_overrides_from_review_data(REVIEW_DATA_CSV)
    if not overrides:
        overrides = load_overrides_from_events("default")
    if not overrides and Path("review_data.csv").exists():
        overrides = load_overrides_from_review_data(Path("review_data.csv"))

    if not GROUND_TRUTH_CSV.exists():
        raise FileNotFoundError(
            f"Ground truth CSV not found at {GROUND_TRUTH_CSV}. Run `python3 main.py evaluate` or `python3 main.py ground-truth` first."
        )
    human_rows = read_csv(GROUND_TRUTH_CSV)
    llm_rows = read_csv(LLM_DATASET_CSV)
    validate_columns(human_rows, llm_rows)
    field_rows = build_field_level_rows(human_rows, llm_rows, overrides)
    paper_rows = summarize_paper_level(field_rows)
    summary = summarize(field_rows)

    STATE_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(STATE_DIR / "meta_paper_level.csv", paper_rows)
    write_csv(STATE_DIR / "meta_field_level.csv", field_rows)
    write_csv(STATE_DIR / "meta_summary.csv", summary)
    print(f"Wrote analysis outputs to {STATE_DIR}")


if __name__ == "__main__":
    main()
