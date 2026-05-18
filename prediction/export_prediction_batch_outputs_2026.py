from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path

import pandas as pd

from jsonl_parser import jsonl_to_dataframe


ROOT = Path(__file__).resolve().parents[1]
INPUT_DIR = ROOT / "openAI_batch_output"
OUTPUT_DIR = INPUT_DIR / "prediction_outputs_2026"


def _question_sort_key(label: str) -> tuple[str, int | str]:
    match = re.fullmatch(r"([A-Z]+)(\d+)", str(label))
    if not match:
        return (str(label), str(label))
    return (match.group(1), int(match.group(2)))


def _model_label(model_id: str | None) -> str:
    if not model_id:
        return ""
    label_map = {
        "gpt-4.1-2025-04-14": "GPT-4.1",
        "gpt-4.1-mini-2025-04-14": "GPT-4.1 Mini",
        "gpt-4.1-nano-2025-04-14": "GPT-4.1 Nano",
        "gpt-4o-2024-08-06": "GPT-4o",
        "gpt-4o-mini": "GPT-4o Mini",
        "gpt-5.1": "GPT-5.1",
        "gpt-5.1-2025-11-13": "GPT-5.1",
        "gpt-5-mini": "GPT-5 Mini",
        "gpt-5-nano": "GPT-5 Nano",
        "o3": "o3",
        "o4-mini": "o4-mini",
        "gpt-3.5-turbo": "GPT-3.5 Turbo",
    }
    for prefix, label in label_map.items():
        if model_id.startswith(prefix):
            return label
    return model_id


def _read_first_body(path: Path) -> dict:
    with path.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            return obj.get("response", {}).get("body", {}) or {}
    return {}


def _parse_row_id(row_id: str) -> dict[str, object]:
    source_item_id = ""
    if "/" in row_id:
        left, source_item_id = row_id.split("/", 1)
    else:
        left = row_id

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
    elif condition_stem.startswith("paper_only_"):
        augmentation_family = "paper_only_prompt"
    elif condition_stem.startswith("data_only_"):
        augmentation_family = "data_only_prompt"
    elif condition_stem.startswith("both_"):
        augmentation_family = "both_prompt"
    elif condition_stem.startswith("science-paper_"):
        augmentation_family = "positive_case_merged"
    elif condition_stem.startswith("pgg_CONFIGmerged_"):
        augmentation_family = "dataset_prediction"
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

    if repeat_label == "temp0":
        repeat_group = "temp0"
    else:
        repeat_group = "temp1"

    condition_id = f"{condition_stem}/{source_item_id}" if source_item_id else condition_stem

    return {
        "row_id": row_id,
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
        body = _read_first_body(path)
        response_model = str(body.get("model", "") or "")
        response_object = str(body.get("object", "") or "")

        try:
            df = jsonl_to_dataframe(path)
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

        for row_id, row in df[question_cols].iterrows():
            row_meta = _parse_row_id(str(row_id))
            base_record: dict[str, object] = {
                "source_file": path.name,
                "source_stem": path.stem,
                "mtime": mtime.isoformat(timespec="seconds"),
                "mtime_year": mtime.year,
                "response_model": response_model,
                "model_label": _model_label(response_model),
                "response_object": response_object,
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
        ["source_file", "condition_id", "repeat_group", "repeat_index", "row_id"]
    ).reset_index(drop=True)
    long = pd.DataFrame(long_rows).sort_values(
        ["source_file", "condition_id", "repeat_group", "repeat_index", "question_set", "question_index"]
    ).reset_index(drop=True)
    return manifest, wide, long


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest, wide, long = build_exports()

    manifest_path = OUTPUT_DIR / "prediction_output_manifest_2026.csv"
    wide_path = OUTPUT_DIR / "prediction_outputs_2026_wide.csv"
    long_path = OUTPUT_DIR / "prediction_outputs_2026_long.csv"

    manifest.to_csv(manifest_path, index=False)
    wide.to_csv(wide_path, index=False)
    long.to_csv(long_path, index=False)

    print(manifest_path)
    print(wide_path)
    print(long_path)


if __name__ == "__main__":
    main()
