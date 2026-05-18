from __future__ import annotations

import argparse
import copy
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
ANALYSIS_ROOT = Path(__file__).resolve().parent
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

from batch_inputs.paper_only_variants import (  # noqa: E402
    MODEL_TAGS,
    build_joint_prompt,
    build_joint_system_prompt,
    build_openai_request,
)
from jsonl_parser import jsonl_to_dataframe  # noqa: E402


SEED_BASE = 20260329
SINGLE_PAPER_WRAPPER = """Below is an analysis report distilled from one academic paper.
Use it as contextual evidence about how design features may change the efficiency impact of punishment.
Respect the report's stated limitations and do not infer beyond what the report supports."""

COLLECTION_REPORT_WRAPPER = """Below is an analysis report synthesized from multiple academic papers.
Use it as contextual evidence about how design features may change the efficiency impact of punishment.
Respect the report's stated limitations and do not infer beyond what the report supports."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Audit validation prediction coverage across baseline, benchmark, "
            "single-paper, and collection augmentations, then write one per-model "
            "backfill batch JSONL for the missing requests."
        )
    )
    parser.add_argument(
        "--df-pgg",
        type=Path,
        default=Path("input/pgg_CONFIGmerged_validation.csv"),
        help="Validation configurations to predict.",
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=Path("openAI_batch_input"),
        help="Directory containing original batch input JSONLs.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("openAI_batch_output"),
        help="Directory containing completed batch output JSONLs.",
    )
    parser.add_argument(
        "--backfill-dir",
        type=Path,
        default=Path("openAI_batch_input") / "backfill_repeat5_missing",
        help="Directory for the generated per-model backfill JSONLs and summary CSVs.",
    )
    return parser.parse_args()


MODEL_SPECS = [
    {
        "label": "GPT-4.1",
        "api_model": "gpt-4.1-2025-04-14",
        "tag": "41",
        "baseline_initial_custom_id": "baseline_joint_reasoning",
        "baseline_repeat_ids": [f"baseline_joint_reasoning_rep{i}" for i in range(1, 5)],
        "output_files": [
            "prediction_positive_case_variations_41.jsonl",
            "prediction_positive_case_reasoning_repeats_41.jsonl",
            "prediction_literature_analysis_report_strict243_joint_41.jsonl",
            "prediction_literature_collection_analysis_report_stage1_9variants_joint_41.jsonl",
            "prediction_literature_collection_plus_pggms_joint_reps2to5_41.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_41.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_reps2to3_41.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_reps4to5_41.jsonl",
            "prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_41.jsonl",
        ],
        "input_files": [
            "prediction_positive_case_variations_41.jsonl",
            "prediction_positive_case_reasoning_repeats_41.jsonl",
            "prediction_literature_analysis_report_strict243_joint_41.jsonl",
            "prediction_literature_collection_analysis_report_stage1_9variants_joint_41.jsonl",
            "prediction_literature_collection_plus_pggms_joint_reps2to5_41.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_reps2to3_41.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_reps4to5_41.jsonl",
            "prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_41.jsonl",
        ],
        "category_filenames": {
            "baseline": "prediction_positive_case_variations_41.jsonl",
            "benchmark_report": "prediction_literature_analysis_report_strict243_joint_41.jsonl",
            "collection_stage1": "prediction_literature_collection_analysis_report_stage1_9variants_joint_41.jsonl",
            "individual_report": "prediction_literature_analysis_report_extended2011_joint_41.jsonl",
            "metadata_collection": "prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_41.jsonl",
        },
    },
    {
        "label": "GPT-4.1 Mini",
        "api_model": "gpt-4.1-mini-2025-04-14",
        "tag": "41mini",
        "baseline_initial_custom_id": "validation/baseline_joint_reasoning",
        "baseline_repeat_ids": [f"baseline_joint_reasoning_rep{i}" for i in range(1, 5)],
        "output_files": [
            "prediction_crosswave_variations_41mini.jsonl",
            "prediction_positive_case_reasoning_repeats_41mini.jsonl",
            "prediction_literature_analysis_report_strict243_joint_41mini.jsonl",
            "prediction_literature_collection_analysis_report_stage1_9variants_joint_41mini.jsonl",
            "prediction_literature_collection_plus_pggms_joint_reps2to5_41mini.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_41mini.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_reps2to3_41mini.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_reps4to5_41mini.jsonl",
            "prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_41mini.jsonl",
        ],
        "input_files": [
            "prediction_crosswave_variations_41mini.jsonl",
            "prediction_positive_case_reasoning_repeats_41mini.jsonl",
            "prediction_literature_analysis_report_strict243_joint_41mini.jsonl",
            "prediction_literature_collection_analysis_report_stage1_9variants_joint_41mini.jsonl",
            "prediction_literature_collection_plus_pggms_joint_reps2to5_41mini.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_reps2to3_41mini.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_reps4to5_41mini.jsonl",
            "prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_41mini.jsonl",
        ],
        "category_filenames": {
            "baseline": "prediction_crosswave_variations_41mini.jsonl",
            "benchmark_report": "prediction_literature_analysis_report_strict243_joint_41mini.jsonl",
            "collection_stage1": "prediction_literature_collection_analysis_report_stage1_9variants_joint_41mini.jsonl",
            "individual_report": "prediction_literature_analysis_report_extended2011_joint_41mini.jsonl",
            "metadata_collection": "prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_41mini.jsonl",
        },
    },
    {
        "label": "GPT-4.1 Nano",
        "api_model": "gpt-4.1-nano-2025-04-14",
        "tag": "41nano",
        "baseline_initial_custom_id": "validation/baseline_joint_reasoning",
        "baseline_repeat_ids": [f"baseline_joint_reasoning_rep{i}" for i in range(1, 5)],
        "output_files": [
            "prediction_crosswave_variations_41nano.jsonl",
            "prediction_positive_case_reasoning_repeats_41nano.jsonl",
            "prediction_literature_analysis_report_strict243_joint_41nano.jsonl",
            "prediction_literature_collection_analysis_report_stage1_9variants_joint_41nano.jsonl",
            "prediction_literature_collection_plus_pggms_joint_reps2to5_41nano.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_41nano.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_reps2to3_41nano.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_reps4to5_41nano.jsonl",
            "prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_41nano.jsonl",
        ],
        "input_files": [
            "prediction_crosswave_variations_41nano.jsonl",
            "prediction_positive_case_reasoning_repeats_41nano.jsonl",
            "prediction_literature_analysis_report_strict243_joint_41nano.jsonl",
            "prediction_literature_collection_analysis_report_stage1_9variants_joint_41nano.jsonl",
            "prediction_literature_collection_plus_pggms_joint_reps2to5_41nano.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_reps2to3_41nano.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_reps4to5_41nano.jsonl",
            "prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_41nano.jsonl",
        ],
        "category_filenames": {
            "baseline": "prediction_crosswave_variations_41nano.jsonl",
            "benchmark_report": "prediction_literature_analysis_report_strict243_joint_41nano.jsonl",
            "collection_stage1": "prediction_literature_collection_analysis_report_stage1_9variants_joint_41nano.jsonl",
            "individual_report": "prediction_literature_analysis_report_extended2011_joint_41nano.jsonl",
            "metadata_collection": "prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_41nano.jsonl",
        },
    },
    {
        "label": "GPT-5.1",
        "api_model": "gpt-5.1",
        "tag": "gpt51",
        "baseline_initial_custom_id": None,
        "baseline_repeat_ids": [f"baseline_joint_reasoning_rep{i}" for i in range(1, 6)],
        "output_files": [
            "prediction_literature_joint_suite_reps1to5_gpt51.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_gpt51.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_reps2to3_gpt51.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_reps4to5_gpt51.jsonl",
            "prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_gpt51.jsonl",
        ],
        "input_files": [
            "prediction_literature_joint_suite_reps1to5_gpt51.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_gpt51.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_reps2to3_gpt51.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_reps4to5_gpt51.jsonl",
            "prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_gpt51.jsonl",
        ],
        "category_filenames": {
            "baseline": "prediction_literature_joint_suite_reps1to5_gpt51.jsonl",
            "benchmark_report": "prediction_literature_joint_suite_reps1to5_gpt51.jsonl",
            "collection_stage1": "prediction_literature_joint_suite_reps1to5_gpt51.jsonl",
            "individual_report": "prediction_literature_analysis_report_extended2011_joint_gpt51.jsonl",
            "metadata_collection": "prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_gpt51.jsonl",
        },
    },
    {
        "label": "GPT-5 Mini",
        "api_model": "gpt-5-mini",
        "tag": "gpt5mini",
        "baseline_initial_custom_id": None,
        "baseline_repeat_ids": [f"baseline_joint_reasoning_rep{i}" for i in range(1, 6)],
        "output_files": [
            "prediction_literature_joint_suite_reps1to5_gpt5mini.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_gpt5mini.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_reps2to3_gpt5mini.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_reps4to5_gpt5mini.jsonl",
            "prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_gpt5mini.jsonl",
        ],
        "input_files": [
            "prediction_literature_joint_suite_reps1to5_gpt5mini.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_gpt5mini.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_reps2to3_gpt5mini.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_reps4to5_gpt5mini.jsonl",
            "prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_gpt5mini.jsonl",
        ],
        "category_filenames": {
            "baseline": "prediction_literature_joint_suite_reps1to5_gpt5mini.jsonl",
            "benchmark_report": "prediction_literature_joint_suite_reps1to5_gpt5mini.jsonl",
            "collection_stage1": "prediction_literature_joint_suite_reps1to5_gpt5mini.jsonl",
            "individual_report": "prediction_literature_analysis_report_extended2011_joint_gpt5mini.jsonl",
            "metadata_collection": "prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_gpt5mini.jsonl",
        },
    },
    {
        "label": "GPT-5 Nano",
        "api_model": "gpt-5-nano",
        "tag": "gpt5nano",
        "baseline_initial_custom_id": None,
        "baseline_repeat_ids": [f"baseline_joint_reasoning_rep{i}" for i in range(1, 6)],
        "output_files": [
            "prediction_literature_joint_suite_reps1to5_gpt5nano.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_gpt5nano.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_reps2to3_gpt5nano.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_reps4to5_gpt5nano.jsonl",
            "prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_gpt5nano.jsonl",
        ],
        "input_files": [
            "prediction_literature_joint_suite_reps1to5_gpt5nano.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_gpt5nano.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_reps2to3_gpt5nano.jsonl",
            "prediction_literature_analysis_report_extended2011_joint_reps4to5_gpt5nano.jsonl",
            "prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_gpt5nano.jsonl",
        ],
        "category_filenames": {
            "baseline": "prediction_literature_joint_suite_reps1to5_gpt5nano.jsonl",
            "benchmark_report": "prediction_literature_joint_suite_reps1to5_gpt5nano.jsonl",
            "collection_stage1": "prediction_literature_joint_suite_reps1to5_gpt5nano.jsonl",
            "individual_report": "prediction_literature_analysis_report_extended2011_joint_gpt5nano.jsonl",
            "metadata_collection": "prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_gpt5nano.jsonl",
        },
    },
]


def read_jsonl_records(path: Path) -> list[dict]:
    records: list[dict] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return records


def normalize_output_row_id(custom_id: str) -> str:
    match = re.match(r"^(?:validation|learning)/(.*)$", custom_id)
    if match:
        return match.group(1)
    return custom_id


def load_output_row_ids(output_dir: Path, filenames: list[str]) -> set[str]:
    row_ids: set[str] = set()
    for filename in filenames:
        path = output_dir / filename
        if not path.exists():
            continue
        df = jsonl_to_dataframe(path)
        row_ids.update(str(idx) for idx in df.index)
    return row_ids


def load_input_record_map(input_dir: Path, filenames: list[str]) -> dict[str, dict]:
    records: dict[str, dict] = {}
    for filename in filenames:
        path = input_dir / filename
        if not path.exists():
            continue
        for record in read_jsonl_records(path):
            custom_id = str(record.get("custom_id", "")).strip()
            if custom_id and custom_id not in records:
                records[custom_id] = record
    return records


def load_report_map(index_csv: Path, id_col: str) -> dict[str, Path]:
    with index_csv.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    out: dict[str, Path] = {}
    for row in rows:
        key = str(row[id_col]).strip()
        report_path = Path(str(row["report_path"]).strip())
        if key and report_path:
            out[key] = report_path
    return out


def expected_baseline_ids(spec: dict[str, object]) -> list[str]:
    ids: list[str] = []
    if spec["baseline_initial_custom_id"]:
        ids.append(str(spec["baseline_initial_custom_id"]))
    ids.extend(str(value) for value in spec["baseline_repeat_ids"])
    return ids


def expected_benchmark_ids(spec: dict[str, object]) -> list[str]:
    if spec["baseline_initial_custom_id"] is None:
        return [f"paper_analysis_report_joint_rep{i}/PGG_MS_202502" for i in range(1, 6)]
    return [
        "paper_analysis_report_joint/PGG_MS_202502",
        *[f"paper_analysis_report_joint_rep{i}/PGG_MS_202502" for i in range(2, 6)],
    ]


def expected_collection_stage1_ids(spec: dict[str, object], variant_ids: list[str]) -> list[str]:
    ids: list[str] = []
    if spec["baseline_initial_custom_id"] is None:
        for rep_idx in range(1, 6):
            ids.extend([f"collection_analysis_report_joint_rep{rep_idx}/{variant_id}" for variant_id in variant_ids])
        return ids

    ids.extend([f"collection_analysis_report_joint/{variant_id}" for variant_id in variant_ids])
    for rep_idx in range(2, 6):
        ids.extend([f"collection_analysis_report_joint_rep{rep_idx}/{variant_id}" for variant_id in variant_ids])
    return ids


def expected_individual_ids(source_ids: list[str]) -> list[str]:
    ids = [f"paper_analysis_report_joint/{source_id}" for source_id in source_ids]
    for rep_idx in range(2, 6):
        ids.extend([f"paper_analysis_report_joint_rep{rep_idx}/{source_id}" for source_id in source_ids])
    return ids


def expected_metadata_ids(variant_ids: list[str]) -> list[str]:
    ids: list[str] = []
    for rep_idx in range(1, 6):
        ids.extend([f"collection_analysis_report_joint_rep{rep_idx}/{variant_id}" for variant_id in variant_ids])
    return ids


def seed_for_custom_id(custom_id: str) -> int:
    match = re.search(r"_rep(\d+)(?:/|$)", custom_id)
    if match:
        rep_idx = int(match.group(1))
        return SEED_BASE + rep_idx - 1
    return SEED_BASE


def with_row_ids(custom_ids: list[str]) -> list[dict[str, str]]:
    return [
        {
            "custom_id": custom_id,
            "row_id": normalize_output_row_id(custom_id),
        }
        for custom_id in custom_ids
    ]


def wrap_report(wrapper: str, report_text: str, prompt_text: str) -> str:
    return (
        f"{wrapper}\n"
        "----------Analysis Report Starts----------\n\n"
        f"{report_text.strip()}\n\n"
        "----------Analysis Report Ends----------\n"
        f"{prompt_text}"
    )


def build_missing_record(
    *,
    custom_id: str,
    category: str,
    api_model: str,
    joint_prompt: str,
    benchmark_report_text: str,
    individual_reports: dict[str, Path],
    stage1_reports: dict[str, Path],
    metadata_reports: dict[str, Path],
) -> dict:
    seed = seed_for_custom_id(custom_id)
    system_prompt = build_joint_system_prompt(include_explanation=True)

    if category == "baseline":
        user_prompt = joint_prompt
    elif category == "benchmark_report":
        user_prompt = wrap_report(SINGLE_PAPER_WRAPPER, benchmark_report_text, joint_prompt)
    elif category == "individual_report":
        source_id = custom_id.rsplit("/", 1)[1]
        report_text = individual_reports[source_id].read_text(encoding="utf-8")
        user_prompt = wrap_report(SINGLE_PAPER_WRAPPER, report_text, joint_prompt)
    elif category == "collection_stage1":
        variant_id = custom_id.rsplit("/", 1)[1]
        report_text = stage1_reports[variant_id].read_text(encoding="utf-8")
        user_prompt = wrap_report(COLLECTION_REPORT_WRAPPER, report_text, joint_prompt)
    elif category == "metadata_collection":
        variant_id = custom_id.rsplit("/", 1)[1]
        report_text = metadata_reports[variant_id].read_text(encoding="utf-8")
        user_prompt = wrap_report(COLLECTION_REPORT_WRAPPER, report_text, joint_prompt)
    else:
        raise KeyError(f"Unsupported category: {category}")

    return build_openai_request(
        custom_id=custom_id,
        model=api_model,
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        include_logprobs=False,
        response_format_json=True,
        include_explanation=True,
        seed=seed,
    )


def main() -> None:
    args = parse_args()
    args.backfill_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(args.df_pgg).sort_values("CONFIG_configId").reset_index(drop=True)
    joint_prompt = build_joint_prompt(df, include_explanation=True)

    benchmark_report_text = (
        PROJECT_ROOT
        / "literature"
        / "output"
        / "paper_analysis_reports"
        / "strict_predictive_empirical_payoff"
        / "PGG_MS_202502.md"
    ).read_text(encoding="utf-8")
    individual_reports = load_report_map(
        PROJECT_ROOT / "literature" / "output" / "paper_analysis_reports" / "broad_all" / "report_index.csv",
        "custom_id",
    )
    stage1_reports = load_report_map(
        PROJECT_ROOT / "literature" / "output" / "collection_analysis_reports" / "switch_sets_stage1" / "report_index.csv",
        "variant_id",
    )
    metadata_reports = load_report_map(
        PROJECT_ROOT / "literature" / "output" / "collection_analysis_reports" / "metadata_filters" / "report_index.csv",
        "variant_id",
    )

    stage1_variant_ids = sorted(stage1_reports)
    metadata_variant_ids = sorted(metadata_reports)
    individual_source_ids = sorted(individual_reports)

    summary_rows: list[dict[str, object]] = []
    detail_rows: list[dict[str, object]] = []

    for spec in MODEL_SPECS:
        output_row_ids = load_output_row_ids(args.output_dir, list(spec["output_files"]))
        input_record_map = load_input_record_map(args.input_dir, list(spec["input_files"]))

        expected_by_category = {
            "baseline": with_row_ids(expected_baseline_ids(spec)),
            "benchmark_report": with_row_ids(expected_benchmark_ids(spec)),
            "collection_stage1": with_row_ids(expected_collection_stage1_ids(spec, stage1_variant_ids)),
            "individual_report": with_row_ids(expected_individual_ids(individual_source_ids)),
            "metadata_collection": with_row_ids(expected_metadata_ids(metadata_variant_ids)),
        }

        model_records: list[dict] = []
        category_counts: Counter[str] = Counter()

        for category, expected_entries in expected_by_category.items():
            missing_entries = [entry for entry in expected_entries if entry["row_id"] not in output_row_ids]
            if not missing_entries:
                continue

            category_counts[category] += len(missing_entries)
            source_filename = str(spec["category_filenames"][category])

            for entry in missing_entries:
                custom_id = entry["custom_id"]
                if custom_id in input_record_map:
                    record = copy.deepcopy(input_record_map[custom_id])
                    record.setdefault("body", {})
                    record["body"]["seed"] = seed_for_custom_id(custom_id)
                    build_source = "copied_from_input"
                else:
                    record = build_missing_record(
                        custom_id=custom_id,
                        category=category,
                        api_model=str(spec["api_model"]),
                        joint_prompt=joint_prompt,
                        benchmark_report_text=benchmark_report_text,
                        individual_reports=individual_reports,
                        stage1_reports=stage1_reports,
                        metadata_reports=metadata_reports,
                    )
                    build_source = "rebuilt_from_reports"

                model_records.append(record)
                detail_rows.append(
                    {
                        "model": spec["label"],
                        "api_model": spec["api_model"],
                        "category": category,
                        "custom_id": custom_id,
                        "seed": seed_for_custom_id(custom_id),
                        "build_source": build_source,
                        "source_filename": source_filename,
                    }
                )

        model_records.sort(key=lambda record: (record["custom_id"]))
        output_path = args.backfill_dir / f"prediction_repeat5_backfill_missing_{spec['tag']}.jsonl"
        if model_records:
            with output_path.open("w", encoding="utf-8") as handle:
                for record in model_records:
                    handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        summary_rows.append(
            {
                "model": spec["label"],
                "api_model": spec["api_model"],
                "output_path": str(output_path),
                "n_missing_total": int(len(model_records)),
                "n_missing_baseline": int(category_counts["baseline"]),
                "n_missing_benchmark_report": int(category_counts["benchmark_report"]),
                "n_missing_collection_stage1": int(category_counts["collection_stage1"]),
                "n_missing_individual_report": int(category_counts["individual_report"]),
                "n_missing_metadata_collection": int(category_counts["metadata_collection"]),
            }
        )

    summary_df = pd.DataFrame(summary_rows).sort_values("model").reset_index(drop=True)
    detail_df = pd.DataFrame(detail_rows).sort_values(["model", "category", "custom_id"]).reset_index(drop=True)

    summary_path = args.backfill_dir / "prediction_repeat5_backfill_missing_summary.csv"
    detail_path = args.backfill_dir / "prediction_repeat5_backfill_missing_rows.csv"
    summary_df.to_csv(summary_path, index=False)
    detail_df.to_csv(detail_path, index=False)

    print(summary_path)
    print(detail_path)
    for row in summary_df.itertuples(index=False):
        if getattr(row, "n_missing_total") > 0:
            print(getattr(row, "output_path"))


if __name__ == "__main__":
    main()
