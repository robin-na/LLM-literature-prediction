from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from textwrap import dedent

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from agentic_report.column_defs import format_prediction_task_column_definitions  # noqa: E402
from agentic_report.prompts import (  # noqa: E402
    build_report_style_requirements,
    task_context_text,
)
from positive_cases.build_paper_only_new_variants_batch_input import (  # noqa: E402
    build_openai_request,
)
from positive_cases.literature_filter_utils import extract_openai_batch_output_text  # noqa: E402


DEFAULT_MODEL = "gpt-4.1-2025-04-14"
DEFAULT_VARIANTS = ["narrative", "decision"]
DEFAULT_COLLECTION_SUMMARY_CSV = Path(
    "literature/output/evidence_cards/literature_evidence_cards_cleaned/collection_switch_sets/collection_switch_sets_summary.csv"
)
DEFAULT_COLLECTION_LEAF_MAP_CSV = Path("literature/output/collection_synthesis_inputs/collection_leaf_map.csv")
DEFAULT_OUTPUT_BUNDLE_DIR = Path("literature/output/collection_synthesis_inputs/final_bundles")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build hierarchical stage-2 batch JSONLs that synthesize final collection "
            "reports from reusable subset summaries."
        )
    )
    parser.add_argument(
        "--leaf-output-jsonl",
        type=Path,
        required=True,
        help="OpenAI batch output JSONL from build_collection_synthesis_batch_input.py",
    )
    parser.add_argument(
        "--collection-leaf-map-csv",
        type=Path,
        default=DEFAULT_COLLECTION_LEAF_MAP_CSV,
        help="Collection-to-leaf map emitted by build_collection_synthesis_batch_input.py",
    )
    parser.add_argument(
        "--leaf-summary-manifest-csv",
        type=Path,
        default=Path("literature/output/collection_synthesis_inputs/leaf_manifest.csv"),
        help="Subset manifest emitted by build_collection_synthesis_batch_input.py",
    )
    parser.add_argument(
        "--collection-summary-csv",
        type=Path,
        default=DEFAULT_COLLECTION_SUMMARY_CSV,
        help="Summary CSV emitted by build_collection_switch_sets.py",
    )
    parser.add_argument(
        "--variants",
        nargs="+",
        default=DEFAULT_VARIANTS,
        choices=DEFAULT_VARIANTS,
        help="Final collection report styles to generate.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help="Model used to synthesize the final collection reports.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("openAI_batch_input"),
        help="Directory for output JSONL files.",
    )
    parser.add_argument(
        "--output-prefix",
        default="synthesis_collection_switch_sets",
        help="Prefix for final output batch files.",
    )
    parser.add_argument(
        "--bundle-dir",
        type=Path,
        default=DEFAULT_OUTPUT_BUNDLE_DIR,
        help="Directory to write grouped subset-synthesis bundles.",
    )
    return parser.parse_args()


def load_chunk_texts(path: Path) -> dict[str, str]:
    chunk_texts: dict[str, str] = {}
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
                chunk_texts[custom_id] = text.strip()
    return chunk_texts


def build_final_bundle(collection_id: str, n_papers: int, leaf_rows: list[dict[str, object]]) -> str:
    sections: list[str] = [
        f"# Literature Analysis Reports For Collection: {collection_id}",
        f"Total papers in collection: {n_papers}",
        f"Number of contributing literature analysis reports: {len(leaf_rows)}",
        "",
        "Each section below is a literature analysis report generated from one paper set drawn from the same literature universe.",
        "",
    ]
    for row in leaf_rows:
        sections.extend(
            [
                f"## {row['leaf_id']}",
                f"Papers in this paper set: {row['leaf_count']}",
                row["leaf_text"],
                "",
            ]
        )
    return "\n".join(str(part) for part in sections).strip() + "\n"


def build_final_prompt(
    *,
    collection_id: str,
    n_papers: int,
    report_style: str,
    column_defs: str,
    leaf_bundle_text: str,
) -> str:
    style_requirements = build_report_style_requirements(report_style)
    return dedent(
        f"""
        You are writing a prediction-support literature synthesis report to help estimate how enabling peer punishment changes efficiency in new public goods games.

        Use only the literature analysis reports below. Each report was generated from a different paper set drawn from the same literature universe.

        Requirements:
        - Synthesize across the full collection rather than repeating the supplied reports.
        - Preserve uncertainty and conflict when the reports disagree.
        - Weigh exact evidence more heavily than non-exact evidence.
        - Weigh payoff-like outcomes more heavily than papers that discuss only non-payoff behavioral outcomes.
        - Distinguish empirical findings from theory or mechanism arguments when both are present.
        - Make it clear when evidence is concentrated on some design dimensions and sparse on others.
        - Support substantive claims with APA-style citations to the source papers based on the citations already contained in the supplied reports.
        - Base the report strictly on the supplied reports and do not add outside claims.
        - Output Markdown with clear section headers.
        - Follow these additional style requirements exactly:
        {style_requirements}

        {task_context_text()}

        Include these sections:
        1) Title
        2) Abstract
        3) Background & Definitions
        4) Evidence Base
        5) Cross-Paper Empirical Patterns
        6) Predictive Guidance
        7) Limitations & Missing Evidence
        8) How To Use This For Predictions

        Column definitions:
        {column_defs}

        Collection metadata:
        - Collection id: {collection_id}
        - Number of papers: {n_papers}

        Literature analysis reports:
        ----------
        {leaf_bundle_text}
        ----------
        """
    ).strip()


def write_jsonl(path: Path, records: list[dict]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    return len(records)


def main() -> None:
    args = parse_args()
    args.bundle_dir.mkdir(parents=True, exist_ok=True)

    leaf_texts = load_chunk_texts(args.leaf_output_jsonl)
    collection_leaf_map = pd.read_csv(args.collection_leaf_map_csv)
    leaf_summary_manifest = pd.read_csv(args.leaf_summary_manifest_csv)
    collection_summary = pd.read_csv(args.collection_summary_csv)
    column_defs = format_prediction_task_column_definitions()

    leaf_summary_manifest["leaf_text"] = leaf_summary_manifest["custom_id"].map(leaf_texts)
    missing_mask = leaf_summary_manifest["leaf_text"].isna() | (
        leaf_summary_manifest["leaf_text"].str.strip() == ""
    )
    if missing_mask.any():
        missing_ids = leaf_summary_manifest.loc[missing_mask, "custom_id"].tolist()
        raise KeyError(
            f"Missing subset-summary outputs for {len(missing_ids)} manifest rows, e.g. {missing_ids[:5]}"
        )

    merged = collection_leaf_map.merge(
        leaf_summary_manifest[
            [
                "leaf_id",
                "custom_id",
                "a_pgg_pun_exactclose",
                "b_payoff_like_outcome",
                "c_empirical_only",
                "leaf_text",
            ]
        ],
        on="leaf_id",
        how="left",
        suffixes=("", "_manifest"),
    )

    prompt_preview_dir = args.bundle_dir / "prompt_previews"
    prompt_preview_dir.mkdir(parents=True, exist_ok=True)
    preview_written: dict[str, bool] = {variant: False for variant in args.variants}

    for variant in args.variants:
        records: list[dict] = []
        for summary_row in collection_summary.to_dict("records"):
            collection_id = str(summary_row["collection_id"])
            leaf_rows = (
                merged[merged["collection_id"] == collection_id]
                .sort_values(["a_pgg_pun_exactclose", "b_payoff_like_outcome", "c_empirical_only", "leaf_id"])
                .to_dict("records")
            )
            bundle_text = build_final_bundle(
                collection_id=collection_id,
                n_papers=int(summary_row["count"]),
                leaf_rows=leaf_rows,
            )
            bundle_path = args.bundle_dir / f"{collection_id}.md"
            bundle_path.write_text(bundle_text, encoding="utf-8")
            prompt_text = build_final_prompt(
                collection_id=collection_id,
                n_papers=int(summary_row["count"]),
                report_style=variant,
                column_defs=column_defs,
                leaf_bundle_text=bundle_text,
            )
            if not preview_written[variant]:
                (prompt_preview_dir / f"{variant}_prompt_preview.md").write_text(
                    prompt_text,
                    encoding="utf-8",
                )
                preview_written[variant] = True
            records.append(
                build_openai_request(
                    custom_id=collection_id,
                    model=args.model,
                    system_prompt="You are a careful research analyst synthesizing literature into a prediction-support report.",
                    user_prompt=prompt_text,
                    include_logprobs=False,
                    response_format_json=False,
                    include_explanation=False,
                )
            )

        output_path = args.output_dir / f"{args.output_prefix}_{variant}.jsonl"
        count = write_jsonl(output_path, records)
        print(f"Wrote {count} requests to {output_path}")


if __name__ == "__main__":
    main()
