from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from agentic_report.column_defs import format_prediction_task_column_definitions  # noqa: E402
from agentic_report.config import DEFAULT_LITERATURE_VECTOR_STORE_ID  # noqa: E402
from agentic_report.prompts import build_paper_retrieval_report_prompt  # noqa: E402
from prediction_inputs.literature_filters import (  # noqa: E402
    build_collection_file_id_map,
    chunk_items,
    load_collection_map,
    write_jsonl,
)

DEFAULT_VARIANTS = ["paper_only_narrative", "paper_only_decision"]
VARIANT_TO_STYLE = {
    "paper_only_narrative": "narrative",
    "paper_only_decision": "decision",
}
DEFAULT_MODEL = "gpt-4.1-2025-04-14"
DEFAULT_COLLECTIONS_PER_FILE = 0
DEFAULT_MAX_NUM_RESULTS = 50


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build batch JSONLs that generate collection-level literature reports via "
            "Responses API file_search against one or more literature vector stores."
        )
    )
    parser.add_argument(
        "--eligible-csv",
        type=Path,
        default=Path("paper_collection/WoS_251031_eligible_design.csv"),
        help="CSV with literature rows and file ids.",
    )
    parser.add_argument(
        "--collection-map",
        type=Path,
        default=Path("paper_collection/collection_mapping_251110.json"),
        help="JSON mapping collection labels to literature row indices.",
    )
    parser.add_argument(
        "--file-id-column",
        default="file_id",
        help="Column in --eligible-csv that contains uploaded OpenAI file ids.",
    )
    parser.add_argument(
        "--vector-store-ids",
        nargs="*",
        default=None,
        help=(
            "One or more literature vector store ids. If omitted, reads "
            "OPENAI_LITERATURE_VECTOR_STORE_IDS as a comma-separated env var."
        ),
    )
    parser.add_argument(
        "--variants",
        nargs="+",
        default=DEFAULT_VARIANTS,
        choices=DEFAULT_VARIANTS,
        help="Report styles to build.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help="Responses API model used to synthesize the collection reports.",
    )
    parser.add_argument(
        "--filter-key",
        default="fileId",
        help="Vector-store attribute key used in file_search filters.",
    )
    parser.add_argument(
        "--max-num-results",
        type=int,
        default=DEFAULT_MAX_NUM_RESULTS,
        help="Max retrieved chunks per report request.",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.0,
        help="Temperature for report synthesis requests.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("openAI_batch_input"),
        help="Directory for output JSONL files.",
    )
    parser.add_argument(
        "--output-prefix",
        default="synthesis_literature_filtered",
        help="Prefix for output JSONL filenames.",
    )
    parser.add_argument(
        "--max-collections",
        type=int,
        default=None,
        help="Optional cap on the number of collection filters to include.",
    )
    parser.add_argument(
        "--collections-per-file",
        type=int,
        default=DEFAULT_COLLECTIONS_PER_FILE,
        help=(
            "If > 0, split each variant into multiple files, each covering at most this "
            "many collection filters."
        ),
    )
    return parser.parse_args()


def resolve_vector_store_ids(explicit_ids: list[str] | None) -> list[str]:
    if explicit_ids:
        return [value for value in explicit_ids if value]

    env_value = os.getenv("OPENAI_LITERATURE_VECTOR_STORE_IDS", "").strip()
    if env_value:
        return [value.strip() for value in env_value.split(",") if value.strip()]
    return [DEFAULT_LITERATURE_VECTOR_STORE_ID]


def build_report_request(
    *,
    collection_label: str,
    model: str,
    prompt_text: str,
    vector_store_ids: list[str],
    file_ids: list[str],
    filter_key: str,
    max_num_results: int,
    temperature: float,
) -> dict:
    return {
        "custom_id": collection_label,
        "method": "POST",
        "url": "/v1/responses",
        "body": {
            "model": model,
            "input": [
                {
                    "role": "user",
                    "content": [{"type": "input_text", "text": prompt_text}],
                }
            ],
            "tools": [
                {
                    "type": "file_search",
                    "vector_store_ids": vector_store_ids,
                    "filters": {
                        "type": "in",
                        "key": filter_key,
                        "value": file_ids,
                    },
                    "max_num_results": max_num_results,
                }
            ],
            "include": ["file_search_call.results"],
            "temperature": temperature,
        },
    }


def output_path_for_variant(
    *,
    output_dir: Path,
    output_prefix: str,
    variant_name: str,
    part_idx: int,
    n_parts: int,
) -> Path:
    stem = f"{output_prefix}_{variant_name}"
    if n_parts > 1:
        stem = f"{stem}_part{part_idx:02d}"
    return output_dir / f"{stem}.jsonl"


def main() -> None:
    args = parse_args()
    vector_store_ids = resolve_vector_store_ids(args.vector_store_ids)
    collection_items = load_collection_map(
        args.collection_map,
        max_collections=args.max_collections,
    )
    file_id_map = build_collection_file_id_map(
        args.eligible_csv,
        collection_items,
        file_id_column=args.file_id_column,
    )
    column_defs = format_prediction_task_column_definitions()

    labels = [label for label, _ in collection_items]
    label_batches = chunk_items(labels, args.collections_per_file)

    for variant_name in args.variants:
        style = VARIANT_TO_STYLE[variant_name]
        prompt_text = build_paper_retrieval_report_prompt(
            column_defs=column_defs,
            report_style=style,
        )
        for part_idx, label_batch in enumerate(label_batches, start=1):
            records = [
                build_report_request(
                    collection_label=label,
                    model=args.model,
                    prompt_text=prompt_text,
                    vector_store_ids=vector_store_ids,
                    file_ids=file_id_map[label],
                    filter_key=args.filter_key,
                    max_num_results=args.max_num_results,
                    temperature=args.temperature,
                )
                for label in label_batch
            ]
            output_path = output_path_for_variant(
                output_dir=args.output_dir,
                output_prefix=args.output_prefix,
                variant_name=variant_name,
                part_idx=part_idx,
                n_parts=len(label_batches),
            )
            count = write_jsonl(output_path, records)
            print(f"Wrote {count} requests to {output_path}")


if __name__ == "__main__":
    main()

