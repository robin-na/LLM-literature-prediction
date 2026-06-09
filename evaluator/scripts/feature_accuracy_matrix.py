from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from utils.columns import COLUMN_MAP as FEATURE_MAP
from utils.csvio import Row, read_csv
from utils.eval_scope import EVAL_SCOPE_ALL, resolve_evaluation_scope
from utils.finalize import FinalizePaths, materialize_final_dataset
from utils.helpers import group_by_paper, guess_reviewer_id, is_empty_like
from utils.paths import FEATURE_MATRIX_SVG, GROUND_TRUTH_CSV, LLM_DATASET_CSV, REVIEW_EVENTS_CSV, STATE_DIR


@dataclass
class FeatureStat:
    total: int = 0
    llm_match: int = 0
    tp: int = 0
    tn: int = 0
    fp: int = 0
    fn: int = 0
    abs_error_sum: float = 0.0
    abs_error_n: int = 0


def _pct(numer: int, denom: int) -> str:
    if denom <= 0:
        return "n/a"
    return f"{(100.0 * numer / denom):.2f}%"


def _is_granularity_mismatch(h_rows: list[Row], l_rows: list[Row]) -> bool:
    # Stage 2 aligns rows by position. Different row counts imply a paper-level
    # granularity mismatch for this quick diagnostic view.
    return len(h_rows) != len(l_rows)


def _confusion_bucket(human_value: str, llm_value: str, final_classification: str) -> tuple[int, int, int, int]:
    # This function is used to convert the human and LLM values into a confusion matrix.
    gt_empty = is_empty_like(human_value)
    llm_empty = is_empty_like(llm_value)
    if gt_empty and llm_empty:
        return (0, 1, 0, 0)
    if final_classification == "match":
        return (1, 0, 0, 0)
    if (not gt_empty) and llm_empty:
        return (0, 0, 0, 1)
    if gt_empty and (not llm_empty):
        return (0, 0, 1, 0)
    if final_classification == "mismatch":
        return (0, 0, 1, 0)
    return (0, 0, 0, 0)


def _parse_float(value: str) -> float | None:
    try:
        return float((value or "").strip())
    except ValueError:
        return None


def _render_table(headers: list[str], rows: list[list[str]]) -> str:
    # This function is used to render the table as a string.
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(cell))

    def fmt_row(cells: list[str]) -> str:
        # This function is used to format a row of the table.
        return "| " + " | ".join(cells[i].ljust(widths[i]) for i in range(len(cells))) + " |"

    sep = "+-" + "-+-".join("-" * w for w in widths) + "-+"
    out: list[str] = [sep, fmt_row(headers), sep]
    for row in rows:
        out.append(fmt_row(row))
    out.append(sep)
    return "\n".join(out)


def _build_matrix_rows(stats: dict[str, FeatureStat]) -> list[list[str]]:
    # This function is used to build the rows of the table.
    table_rows: list[list[str]] = []
    for feature in FEATURE_MAP.keys():
        stat = stats[feature]
        llm_acc = _pct(stat.llm_match, stat.total)
        human_acc = "100.00%" if stat.total > 0 else "n/a"
        precision = _pct(stat.tp, stat.tp + stat.fp)
        recall = _pct(stat.tp, stat.tp + stat.fn)
        mean_abs_error = (
            f"{(stat.abs_error_sum / stat.abs_error_n):.4f}" if stat.abs_error_n > 0 else "n/a"
        )
        table_rows.append([feature, llm_acc, human_acc, precision, recall, mean_abs_error])
    return sorted(
        table_rows,
        key=lambda row: (float(row[1].rstrip("%")) if row[1] != "n/a" else 101.0, row[0]),
    )


def _render_svg_table(
    *,
    headers: list[str],
    rows: list[list[str]],
    metadata_lines: list[str],
    output_path: Path,
) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    col_widths = [360, 160, 160, 140, 140, 170]
    row_h = 52
    header_h = 56
    meta_h = 26 * len(metadata_lines) + 34
    title_h = 52
    margin = 24
    table_w = sum(col_widths)
    width = table_w + margin * 2
    height = margin * 2 + title_h + meta_h + header_h + row_h * len(rows) + 16

    x0 = margin
    y = margin
    parts: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect x="0" y="0" width="100%" height="100%" fill="#ffffff"/>',
        f'<text x="{x0}" y="{y + 28}" font-size="28" font-family="Arial, Helvetica, sans-serif" fill="#111827" font-weight="700">Feature Accuracy Matrix</text>',
    ]
    y += title_h

    for line in metadata_lines:
        parts.append(
            f'<text x="{x0}" y="{y}" font-size="18" font-family="Arial, Helvetica, sans-serif" fill="#374151">{line}</text>'
        )
        y += 26
    y += 8

    parts.append(f'<rect x="{x0}" y="{y}" width="{table_w}" height="{header_h}" fill="#111827" rx="8" ry="8"/>')
    cx = x0
    for i, h in enumerate(headers):
        parts.append(
            f'<text x="{cx + 14}" y="{y + 36}" font-size="20" font-family="Arial, Helvetica, sans-serif" fill="#ffffff" font-weight="700">{h}</text>'
        )
        cx += col_widths[i]
    y += header_h

    for r_idx, row in enumerate(rows):
        fill = "#f8fafc" if (r_idx % 2 == 0) else "#ffffff"
        parts.append(
            f'<rect x="{x0}" y="{y}" width="{table_w}" height="{row_h}" fill="{fill}" rx="6" ry="6"/>'
        )
        cx = x0
        for c_idx, cell in enumerate(row):
            parts.append(
                f'<text x="{cx + 14}" y="{y + 34}" font-size="19" font-family="Arial, Helvetica, sans-serif" fill="#111827">{cell}</text>'
            )
            cx += col_widths[c_idx]
        y += row_h

    parts.append("</svg>")
    output_path.write_text("\n".join(parts), encoding="utf-8")
    return output_path


def main(
    *,
    image_out: str | None = None,
    review_session_id: str = "default",
    reviewer_id: str = "",
    ground_truth_csv: str | None = None,
    eval_scope: str = EVAL_SCOPE_ALL,
) -> None:
    reviewer = (reviewer_id or "").strip() or guess_reviewer_id(review_session_id)
    ground_truth_path = (
        Path(ground_truth_csv).expanduser().resolve() if ground_truth_csv else GROUND_TRUTH_CSV
    )

    human_rows = read_csv(ground_truth_path)
    llm_rows = read_csv(LLM_DATASET_CSV)
    scope = resolve_evaluation_scope(human_rows=human_rows, eval_scope=eval_scope)
    final_rows = materialize_final_dataset(
        FinalizePaths(
            human_csv=ground_truth_path,
            llm_csv=LLM_DATASET_CSV,
            review_events_csv=REVIEW_EVENTS_CSV,
            out_csv=STATE_DIR / "__feature_matrix_unused__.csv",
        ),
        review_session_id=review_session_id,
        reviewer_id=reviewer,
    )

    human_by_paper = group_by_paper(human_rows, "Filename")
    llm_by_paper = group_by_paper(llm_rows, "custom_id", strip_md=True)

    stats: dict[str, FeatureStat] = {feature: FeatureStat() for feature in FEATURE_MAP.keys()}
    granularity_mismatch_papers: list[str] = []
    used_papers: set[str] = set()

    for paper_id in scope.paper_ids:
        h_rows = human_by_paper.get(paper_id, [])
        l_rows = llm_by_paper.get(paper_id, [])
        if _is_granularity_mismatch(h_rows, l_rows):
            granularity_mismatch_papers.append(paper_id)
            continue
        used_papers.add(paper_id)

    for row in final_rows:
        paper_id = (row.get("paper_id") or "").strip()
        feature = (row.get("field") or "").strip()
        if paper_id not in used_papers or feature not in FEATURE_MAP:
            continue
        stat = stats[feature]
        human_value = (row.get("human_value") or "").strip()
        llm_value = (row.get("llm_value") or "").strip()
        final_classification = (row.get("final_classification") or "").strip()
        stat.total += 1
        if final_classification in {"match", "both_empty"}:
            stat.llm_match += 1
        tp, tn, fp, fn = _confusion_bucket(human_value, llm_value, final_classification)
        stat.tp += tp
        stat.tn += tn
        stat.fp += fp
        stat.fn += fn
        human_numeric = _parse_float(human_value)
        llm_numeric = _parse_float(llm_value)
        if human_numeric is not None and llm_numeric is not None:
            stat.abs_error_sum += abs(human_numeric - llm_numeric)
            stat.abs_error_n += 1

    table_rows = _build_matrix_rows(stats)

    total_target_papers = len(scope.paper_ids)
    used_for_feature_scoring = [paper_id for paper_id in scope.paper_ids if paper_id not in set(granularity_mismatch_papers)]
    granularity_mismatch_count = len(granularity_mismatch_papers)
    granularity_match_accuracy = _pct(
        total_target_papers - granularity_mismatch_count,
        total_target_papers,
    )

    print("Feature Accuracy Matrix (filtered paper subset)")
    print(f"- Evaluation scope: {scope.mode}")
    if scope.mode != EVAL_SCOPE_ALL:
        print(f"- Base target papers before scope filter: {len(scope.base_paper_ids)}")
        if scope.excluded_non_lab_papers:
            print("- Excluded non-lab papers:")
            for paper_id in scope.excluded_non_lab_papers:
                print(f"  - {paper_id}")
    print(f"- Target papers (unique): {total_target_papers}")
    print(f"- Papers used for feature scoring: {len(used_for_feature_scoring)}")
    print(
        "- Granularity mismatches (paper-level row-count mismatch): "
        f"{granularity_mismatch_count}/{total_target_papers} "
        f"({_pct(granularity_mismatch_count, total_target_papers)})"
    )
    if granularity_mismatch_papers:
        print("- Excluded papers due to granularity mismatch:")
        for paper_id in granularity_mismatch_papers:
            print(f"  - {paper_id}")
    print(f"- Granularity match accuracy: {granularity_match_accuracy}")
    print(f"- Review session: {review_session_id}")
    print(f"- Reviewer: {reviewer}")
    print(f"- Ground truth source: {ground_truth_path}")
    print(f"- LLM source: {LLM_DATASET_CSV}")
    print("")
    print(
        _render_table(
            ["Feature", "LLM Accuracy", "Human Accuracy", "Precision", "Recall", "Mean Abs Error"],
            table_rows,
        )
    )

    out_path = (
        Path(image_out).expanduser().resolve()
        if image_out
        else FEATURE_MATRIX_SVG.resolve()
    )
    metadata = [
        f"Evaluation scope: {scope.mode}",
        f"Target papers (unique): {total_target_papers}",
        f"Papers used for feature scoring: {len(used_for_feature_scoring)}",
        f"Review session: {review_session_id}",
        f"Reviewer: {reviewer}",
        (
            "Granularity mismatches: "
            f"{granularity_mismatch_count}/{total_target_papers} "
            f"({_pct(granularity_mismatch_count, total_target_papers)})"
        ),
        f"Granularity match accuracy: {granularity_match_accuracy}",
    ]
    written = _render_svg_table(
        headers=["Feature", "LLM Accuracy", "Human Accuracy", "Precision", "Recall", "Mean Abs Error"],
        rows=table_rows,
        metadata_lines=metadata,
        output_path=out_path,
    )
    print("")
    print(f"Saved matrix image: {written}")


if __name__ == "__main__":
    main()
