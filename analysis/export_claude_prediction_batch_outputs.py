from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path

import pandas as pd

from jsonl_parser import jsonl_to_dataframe


ROOT = Path(__file__).resolve().parents[1]
INPUT_DIR = ROOT / "claude_batch_output"
OUTPUT_DIR = INPUT_DIR / "prediction_outputs_2026"
KNOWN_MODEL_TAGS = {"opus46", "sonnet46", "haiku45"}


def _question_sort_key(label: str) -> tuple[str, int | str]:
    match = re.fullmatch(r"([A-Z]+)(\d+)", str(label))
    if not match:
        return (str(label), str(label))
    return (match.group(1), int(match.group(2)))


def _model_label(model_id: str | None) -> str:
    if not model_id:
        return ""
    label_map = {
        "claude-opus-4-6": "Claude Opus 4.6",
        "claude-sonnet-4-6": "Claude Sonnet 4.6",
        "claude-haiku-4-5": "Claude Haiku 4.5",
    }
    for prefix, label in label_map.items():
        if model_id.startswith(prefix):
            return label
    return model_id


def _split_model_tag(row_id: str) -> tuple[str, str]:
    if "__" not in row_id:
        return row_id, ""
    base_id, tag = row_id.rsplit("__", 1)
    if tag in KNOWN_MODEL_TAGS:
        return base_id, tag
    return row_id, ""


def _strip_hash_suffix(row_id: str) -> str:
    return re.sub(r"___h[0-9a-f]{8}$", "", row_id)


def _restore_source_separator(row_id: str) -> str:
    patterns = [
        "paper_analysis_report",
        "paper_full_text",
        "collection_analysis_report",
    ]
    for stem in patterns:
        match = re.match(
            rf"^({stem}(?:_joint_reasoning|_reasoning|_joint)?(?:_rep\d+|_temp0)?)_(.+)$",
            row_id,
        )
        if match:
            return f"{match.group(1)}/{match.group(2)}"
    return row_id


def _parse_row_id(row_id: str) -> dict[str, object]:
    raw_row_id = str(row_id)
    base_row_id, model_tag = _split_model_tag(raw_row_id)
    normalized_row_id = _restore_source_separator(_strip_hash_suffix(base_row_id))

    source_item_id = ""
    if "/" in normalized_row_id:
        left, source_item_id = normalized_row_id.split("/", 1)
    else:
        left = normalized_row_id

    repeat_label = "initial"
    repeat_index = 0
    match = re.match(r"^(.*)_(rep\d+|temp0)$", left)
    if match:
        left = match.group(1)
        repeat_label = match.group(2)
        if repeat_label.startswith("rep"):
            repeat_index = int(repeat_label[3:])

    prompt_elicitation = "plain"
    condition_stem = left
    for suffix, label in [
        ("_joint_reasoning", "joint_reasoning"),
        ("_reasoning", "reasoning"),
        ("_joint", "joint"),
    ]:
        if left.endswith(suffix):
            condition_stem = left[: -len(suffix)]
            prompt_elicitation = label
            break

    if condition_stem == "baseline":
        augmentation_family = "baseline"
    elif condition_stem == "paper_analysis_report":
        augmentation_family = "single_paper_analysis_report"
    elif condition_stem == "paper_full_text":
        augmentation_family = "single_paper_full_text"
    elif condition_stem == "collection_analysis_report":
        augmentation_family = "collection_analysis_report"
    else:
        augmentation_family = "other"

    if source_item_id:
        if condition_stem == "paper_analysis_report":
            augmented_input_kind = "paper_analysis_report"
        elif condition_stem == "paper_full_text":
            augmented_input_kind = "paper_full_text"
        elif condition_stem == "collection_analysis_report":
            augmented_input_kind = "collection_analysis_report"
        else:
            augmented_input_kind = "attached_source"
    else:
        augmented_input_kind = "none"

    repeat_group = "temp0" if repeat_label == "temp0" else "temp1"
    condition_id = f"{condition_stem}/{source_item_id}" if source_item_id else condition_stem

    return {
        "raw_row_id": raw_row_id,
        "row_id": normalized_row_id,
        "model_tag": model_tag,
        "condition_id": condition_id,
        "condition_stem": condition_stem,
        "prompt_elicitation": prompt_elicitation,
        "augmentation_family": augmentation_family,
        "augmented_input_kind": augmented_input_kind,
        "augmented_input_id": source_item_id,
        "repeat_label": repeat_label,
        "repeat_index": repeat_index,
        "repeat_group": repeat_group,
    }


def _read_response_meta(path: Path) -> tuple[str, str, dict[str, dict[str, str]]]:
    row_meta: dict[str, dict[str, str]] = {}
    models: list[str] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            raw_row_id = str(obj.get("custom_id", "") or "")
            model_id = str(obj.get("result", {}).get("message", {}).get("model", "") or "")
            row_meta[raw_row_id] = {
                "response_model": model_id,
                "response_object": "claude.message_batch_results",
            }
            if model_id:
                models.append(model_id)

    unique_models = sorted(set(models))
    if len(unique_models) == 1:
        response_model = unique_models[0]
        response_object = "claude.message_batch_results"
    elif unique_models:
        response_model = "mixed"
        response_object = "claude.message_batch_results"
    else:
        response_model = ""
        response_object = "claude.message_batch_results"
    return response_model, response_object, row_meta


def iter_prediction_files_2026() -> list[Path]:
    out: list[Path] = []
    for path in sorted(INPUT_DIR.glob("prediction*.jsonl")):
        mtime = datetime.fromtimestamp(path.stat().st_mtime)
        if mtime.year != 2026:
            continue
        out.append(path)
    return out


def build_exports() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    manifest_rows: list[dict[str, object]] = []
    wide_rows: list[dict[str, object]] = []
    long_rows: list[dict[str, object]] = []

    for path in iter_prediction_files_2026():
        mtime = datetime.fromtimestamp(path.stat().st_mtime)
        response_model, response_object, row_level_meta = _read_response_meta(path)

        try:
            df = jsonl_to_dataframe(path, platform="claude")
        except Exception as exc:
            manifest_rows.append(
                {
                    "source_file": path.name,
                    "source_stem": path.stem,
                    "mtime": mtime.isoformat(timespec="seconds"),
                    "mtime_year": mtime.year,
                    "response_model": response_model,
                    "model_label": _model_label(response_model),
                    "response_object": response_object,
                    "n_rows": 0,
                    "n_question_cols": 0,
                    "parsed_ok": False,
                    "parse_error": str(exc),
                }
            )
            continue

        question_cols = sorted(
            [str(col) for col in df.columns if re.fullmatch(r"[QL]\d+", str(col))],
            key=_question_sort_key,
        )
        if not question_cols:
            manifest_rows.append(
                {
                    "source_file": path.name,
                    "source_stem": path.stem,
                    "mtime": mtime.isoformat(timespec="seconds"),
                    "mtime_year": mtime.year,
                    "response_model": response_model,
                    "model_label": _model_label(response_model),
                    "response_object": response_object,
                    "n_rows": int(df.shape[0]),
                    "n_question_cols": 0,
                    "parsed_ok": False,
                    "parse_error": "No Q/L prediction columns found",
                }
            )
            continue

        manifest_rows.append(
            {
                "source_file": path.name,
                "source_stem": path.stem,
                "mtime": mtime.isoformat(timespec="seconds"),
                "mtime_year": mtime.year,
                "response_model": response_model,
                "model_label": _model_label(response_model),
                "response_object": response_object,
                "n_rows": int(df.shape[0]),
                "n_question_cols": len(question_cols),
                "parsed_ok": True,
                "parse_error": "",
            }
        )

        for raw_row_id, row in df[question_cols].iterrows():
            raw_row_id_str = str(raw_row_id)
            row_meta = _parse_row_id(raw_row_id_str)
            row_response_meta = row_level_meta.get(
                raw_row_id_str,
                {"response_model": response_model, "response_object": response_object},
            )
            base_record: dict[str, object] = {
                "source_file": path.name,
                "source_stem": path.stem,
                "mtime": mtime.isoformat(timespec="seconds"),
                "mtime_year": mtime.year,
                "response_model": row_response_meta["response_model"],
                "model_label": _model_label(row_response_meta["response_model"]),
                "response_object": row_response_meta["response_object"],
                **row_meta,
            }

            wide_record = base_record.copy()
            n_predictions = 0
            for question in question_cols:
                value = pd.to_numeric(pd.Series([row[question]]), errors="coerce").iloc[0]
                wide_record[question] = value
                if pd.notna(value):
                    n_predictions += 1
                    question_match = re.fullmatch(r"([QL])(\d+)", question)
                    long_rows.append(
                        {
                            **base_record,
                            "question": question,
                            "question_set": question_match.group(1) if question_match else "",
                            "question_index": int(question_match.group(2)) if question_match else pd.NA,
                            "prediction": float(value),
                        }
                    )
            wide_record["n_predictions"] = n_predictions
            wide_rows.append(wide_record)

    manifest = pd.DataFrame(manifest_rows).sort_values(["mtime", "source_file"]).reset_index(drop=True)
    wide = pd.DataFrame(wide_rows).sort_values(
        ["source_file", "model_label", "condition_id", "repeat_group", "repeat_index", "row_id"]
    ).reset_index(drop=True)
    long = pd.DataFrame(long_rows).sort_values(
        [
            "source_file",
            "model_label",
            "condition_id",
            "repeat_group",
            "repeat_index",
            "question_set",
            "question_index",
        ]
    ).reset_index(drop=True)
    return manifest, wide, long


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest, wide, long = build_exports()
    manifest.to_csv(OUTPUT_DIR / "prediction_output_manifest_2026.csv", index=False)
    wide.to_csv(OUTPUT_DIR / "prediction_outputs_2026_wide.csv", index=False)
    long.to_csv(OUTPUT_DIR / "prediction_outputs_2026_long.csv", index=False)


if __name__ == "__main__":
    main()
