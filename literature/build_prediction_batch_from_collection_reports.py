from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from prediction_inputs.paper_only_variants import (  # noqa: E402
    DEFAULT_MODELS,
    MODEL_TAGS,
    build_joint_prompt,
    build_joint_system_prompt,
    build_openai_request,
)
from positive_cases.literature_filter_utils import extract_openai_batch_output_text  # noqa: E402


DEFAULT_OUTPUT_JSONL = Path("openAI_batch_output/synthesis_collection_switch_sets_stage1.jsonl")
DEFAULT_LEAF_LEGEND = Path("literature/output/collection_synthesis_inputs/leaf_legend.csv")
DEFAULT_DIRECT_MANIFEST = Path("literature/output/collection_synthesis_inputs/direct_request_manifest.csv")
DEFAULT_REPORT_ROOT = Path("literature/output/collection_analysis_reports/switch_sets_stage1")

COLLECTION_REPORT_WRAPPER = """Below is an analysis report synthesized from multiple academic papers.
Use it as contextual evidence about how design features may change the efficiency impact of punishment.
Respect the report's stated limitations and do not infer beyond what the report supports."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build joint-with-explanation prediction batch JSONLs from synthesized "
            "collection analysis reports."
        )
    )
    parser.add_argument(
        "--report-output-jsonl",
        type=Path,
        default=DEFAULT_OUTPUT_JSONL,
        help="OpenAI batch output JSONL containing synthesized collection analysis reports.",
    )
    parser.add_argument(
        "--df-pgg",
        type=Path,
        default=Path("input/pgg_CONFIGmerged_validation.csv"),
        help="Target validation configurations to predict.",
    )
    parser.add_argument(
        "--models",
        nargs="+",
        default=DEFAULT_MODELS,
        choices=sorted(MODEL_TAGS),
        help="Prediction models to generate batch files for.",
    )
    parser.add_argument(
        "--n-explanation-repeats",
        type=int,
        default=1,
        help="Number of repeated runs for the joint explanation mode.",
    )
    parser.add_argument(
        "--repeat-start-index",
        type=int,
        default=1,
        help="Starting repeat index to use in custom_id suffixes for repeated runs.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("openAI_batch_input"),
        help="Directory for output JSONL files.",
    )
    parser.add_argument(
        "--output-prefix",
        default="prediction_literature_collection_analysis_report_stage1_9variants_joint",
        help="Prefix for output JSONL filenames.",
    )
    parser.add_argument(
        "--report-root",
        type=Path,
        default=DEFAULT_REPORT_ROOT,
        help="Directory to write rendered collection analysis reports.",
    )
    parser.add_argument(
        "--leaf-legend-csv",
        type=Path,
        default=DEFAULT_LEAF_LEGEND,
        help="Legend CSV describing the leaf ids used in the stage-1 synthesis run.",
    )
    parser.add_argument(
        "--direct-manifest-csv",
        type=Path,
        default=DEFAULT_DIRECT_MANIFEST,
        help="Manifest CSV for direct collection synthesis requests.",
    )
    return parser.parse_args()


def _model_tag(model: str) -> str:
    return MODEL_TAGS[model]


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def normalize_variant_id(custom_id: str) -> str:
    parts = [part for part in str(custom_id).split("/") if part]
    return parts[-1] if parts else str(custom_id)


def load_variant_metadata(
    leaf_legend_csv: Path,
    direct_manifest_csv: Path,
) -> dict[str, dict[str, str]]:
    metadata: dict[str, dict[str, str]] = {}

    if leaf_legend_csv.exists():
        for row in load_rows(leaf_legend_csv):
            variant_id = row["leaf_id"]
            metadata[variant_id] = {
                "variant_id": variant_id,
                "custom_id": f"subset_summary/{variant_id}",
                "variant_kind": "subset_summary",
                "count": row.get("count", ""),
                "description": row.get("summary", ""),
            }

    if direct_manifest_csv.exists():
        for row in load_rows(direct_manifest_csv):
            variant_id = normalize_variant_id(row["custom_id"])
            metadata[variant_id] = {
                "variant_id": variant_id,
                "custom_id": row["custom_id"],
                "variant_kind": "collection_direct",
                "count": row.get("count", ""),
                "description": f"Direct synthesized report for collection `{row.get('collection_id', '')}`.",
            }

    return metadata


def load_report_texts(path: Path) -> dict[str, dict[str, str]]:
    report_texts: dict[str, dict[str, str]] = {}
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            item = json.loads(line)
            custom_id = str(item.get("custom_id", "")).strip()
            if not custom_id:
                continue
            text = extract_openai_batch_output_text(item)
            if isinstance(text, str) and text.strip():
                variant_id = normalize_variant_id(custom_id)
                report_texts[variant_id] = {
                    "custom_id": custom_id,
                    "variant_id": variant_id,
                    "report_text": text.strip(),
                }
    return report_texts


def write_reports(
    report_root: Path,
    report_texts: dict[str, dict[str, str]],
    metadata_map: dict[str, dict[str, str]],
) -> dict[str, str]:
    report_root.mkdir(parents=True, exist_ok=True)
    index_rows: list[dict[str, str]] = []
    rendered: dict[str, str] = {}

    for variant_id in sorted(report_texts):
        entry = report_texts[variant_id]
        report_text = entry["report_text"]
        report_path = report_root / f"{variant_id}.md"
        report_path.write_text(report_text + "\n", encoding="utf-8")
        rendered[variant_id] = report_text

        meta = metadata_map.get(variant_id, {})
        index_rows.append(
            {
                "variant_id": variant_id,
                "custom_id": entry["custom_id"],
                "variant_kind": meta.get("variant_kind", ""),
                "count": meta.get("count", ""),
                "description": meta.get("description", ""),
                "report_path": str(report_path),
            }
        )

    index_path = report_root / "report_index.csv"
    with index_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "variant_id",
                "custom_id",
                "variant_kind",
                "count",
                "description",
                "report_path",
            ],
        )
        writer.writeheader()
        writer.writerows(index_rows)

    return rendered


def build_requests(
    *,
    df: pd.DataFrame,
    report_texts: dict[str, str],
    model: str,
    n_explanation_repeats: int,
    repeat_start_index: int,
) -> list[dict]:
    requests: list[dict] = []
    for variant_id in sorted(report_texts):
        report_text = report_texts[variant_id]
        for rep_idx in range(repeat_start_index, repeat_start_index + n_explanation_repeats):
            suffix = "" if n_explanation_repeats == 1 else f"_rep{rep_idx}"
            requests.append(
                    build_openai_request(
                        custom_id=f"collection_analysis_report_joint{suffix}/{variant_id}",
                        model=model,
                        system_prompt=build_joint_system_prompt(include_explanation=True),
                        user_prompt=(
                            f"{COLLECTION_REPORT_WRAPPER}\n"
                            "----------Analysis Report Starts----------\n\n"
                            f"{report_text}\n\n"
                            "----------Analysis Report Ends----------\n"
                            f"{build_joint_prompt(df, include_explanation=True)}"
                        ),
                        include_logprobs=False,
                        response_format_json=True,
                        include_explanation=True,
                    )
            )
    return requests


def write_jsonl(path: Path, records: list[dict]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    return len(records)


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.df_pgg).sort_values("CONFIG_configId").reset_index(drop=True)
    metadata_map = load_variant_metadata(args.leaf_legend_csv, args.direct_manifest_csv)
    report_entries = load_report_texts(args.report_output_jsonl)
    report_texts = write_reports(args.report_root, report_entries, metadata_map)

    for model in args.models:
        requests = build_requests(
            df=df,
            report_texts=report_texts,
            model=model,
            n_explanation_repeats=args.n_explanation_repeats,
            repeat_start_index=args.repeat_start_index,
        )
        output_path = args.output_dir / f"{args.output_prefix}_{_model_tag(model)}.jsonl"
        count = write_jsonl(output_path, requests)
        print(f"Wrote {count} requests to {output_path}")


if __name__ == "__main__":
    main()
