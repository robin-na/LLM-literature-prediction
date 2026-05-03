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
from literature.build_collection_synthesis_batch_input import (  # noqa: E402
    build_entries,
    load_metadata_map,
)
from positive_cases.build_paper_only_new_variants_batch_input import (  # noqa: E402
    build_openai_request,
)


DEFAULT_MODEL = "gpt-4.1-2025-04-14"
DEFAULT_COLLECTION_SUMMARY_CSV = Path(
    "literature/output/evidence_cards/literature_evidence_cards_cleaned/collection_metadata_sets/collection_metadata_summary.csv"
)
DEFAULT_COMBINED_CSV = Path(
    "literature/output/evidence_cards/literature_evidence_cards_cleaned/combined.csv"
)
DEFAULT_METADATA_CSV = Path("paper_collection/WoS_251031_fileInfo.csv")
DEFAULT_BUNDLE_DIR = Path("literature/output/collection_metadata_synthesis_inputs")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build batch JSONL requests for metadata-based collection synthesis. "
            "Each request summarizes one metadata-filtered literature collection using the "
            "evidence-card digests."
        )
    )
    parser.add_argument(
        "--collection-summary-csv",
        type=Path,
        default=DEFAULT_COLLECTION_SUMMARY_CSV,
        help="Collection summary CSV emitted by build_collection_metadata_sets.py",
    )
    parser.add_argument(
        "--combined-csv",
        type=Path,
        default=DEFAULT_COMBINED_CSV,
        help="Combined evidence-card CSV from parse_evidence_card_batch_output.py",
    )
    parser.add_argument(
        "--metadata-csv",
        type=Path,
        default=DEFAULT_METADATA_CSV,
        help="Metadata CSV mapping custom ids to source fields.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help="Model used to synthesize the collection analysis reports.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("openAI_batch_input"),
        help="Directory for output JSONL files.",
    )
    parser.add_argument(
        "--output-prefix",
        default="synthesis_collection_metadata_filters",
        help="Prefix for output batch file names.",
    )
    parser.add_argument(
        "--bundle-dir",
        type=Path,
        default=DEFAULT_BUNDLE_DIR,
        help="Directory to write rendered collection digests and manifests.",
    )
    parser.add_argument(
        "--max-collections",
        type=int,
        default=None,
        help="Optional cap on the number of collections to render.",
    )
    parser.add_argument(
        "--collections-per-file",
        type=int,
        default=0,
        help="If > 0, split the batch requests across multiple JSONL files.",
    )
    return parser.parse_args()


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_jsonl(path: Path, records: list[dict]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    return len(records)


def chunk_rows(rows: list[dict[str, str]], chunk_size: int) -> list[list[dict[str, str]]]:
    if chunk_size <= 0:
        return [rows]
    return [rows[i : i + chunk_size] for i in range(0, len(rows), chunk_size)]


def build_collection_bundle(
    *,
    n_total_papers: int,
    entries_text: list[str],
) -> str:
    return "\n\n".join(
        [
            "# Paper Set Evidence Digest",
            f"Number of papers in this paper set: {n_total_papers}",
            (
                "Each item below is a compact paper-level analysis digest. "
                "Use only this digest."
            ),
            *entries_text,
            "",
        ]
    )


def build_collection_prompt(
    *,
    bundle_text: str,
    column_defs: str,
) -> str:
    return dedent(
        f"""
        You are writing a literature analysis report synthesized across multiple academic papers for downstream prediction about punishment effects in public-goods-game-like environments.

        Use only the paper-set evidence digest below. Do not invent details that are not supported by the supplied paper summaries.

        Key concepts:
        - The downstream prediction task is: given the game design dimensions and the average efficiency of the control game with punishment disabled, predict the average efficiency of the same game when peer punishment is enabled.
        - The game design dimensions used in prediction are: `player_count`, `num_rounds`, `chat`, `all_or_nothing`, `default_contrib`, `mpcr`, `punishment_cost`, `punishment_tech`, `reward_exists`, `reward_cost`, `reward_tech`, `show_n_rounds`, `show_other_summaries`, and `show_punishment_id`.
        - `efficiency` means the ratio of the group's total payoff to the total payoff of a fully cooperative group, where everyone contributes fully in every round.
        - Closely related payoff-based outcomes include group payoff, total earnings, welfare, surplus, or total coins generated.
        - Contribution rate, cooperation rate, punishment frequency, punishment assigned, norm compliance, and similar behavioral outcomes are not the same as efficiency or payoff. They may still be important, but they must be distinguished from payoff-based outcomes.

        What to do:
        - Synthesize across the papers instead of summarizing them one by one.
        - Assess the literature separately on three target-relevance dimensions: `pgg_or_variant`, `punishment_or_sanctions`, and `efficiency_or_related_payoff_outcome`.
        - Use the relevance labels consistently: `exact`, `close`, `adjacent`, `weak`, and `none`.
        - Distinguish empirical findings from theory or mechanism arguments.
        - Distinguish payoff-related outcomes from non-payoff behavioral outcomes.
        - Identify which of the 14 prediction dimensions are directly informed, indirectly informed, only contextually discussed, or effectively missing in this paper set.
        - When discussing dimension-level evidence, interpret it in terms of what the literature implies about punishment's effect under that dimension. When the evidence is based on non-payoff outcomes rather than payoff, say so explicitly.
        - Preserve ambiguity and disagreement when the papers conflict.
        - Support substantive claims with APA-style citations to the source papers based on the supplied source lines, for example `(Dorrough et al., 2017)`.
        - If the paper set has limited relevance to the prediction task, say that clearly and explain why.
        - Do not add outside claims.

        Output Markdown with these sections:
        1) Evidence Base
        2) Task Relevance
        3) Outcomes Measured In The Literature
        4) Main Findings Relevant To Prediction
        5) Prediction Guidance
        6) Design Dimensions Highlighted Across Papers
        7) Important Limitations

        Expectations for the sections:
        - `Evidence Base`: describe the mix of empirical versus theory papers, and whether the paper set is narrow or broad for the prediction task.
        - `Task Relevance`: summarize how directly the literature speaks to PGG or variants, punishment or sanctions, and efficiency or related payoff outcomes.
        - `Outcomes Measured In The Literature`: distinguish payoff-related outcomes from non-payoff behavioral outcomes.
        - `Main Findings Relevant To Prediction`: synthesize the cross-paper findings most useful for predicting treatment efficiency.
        - `Prediction Guidance`: explain how this literature should inform prediction of treatment efficiency from design dimensions plus control efficiency.
        - `Design Dimensions Highlighted Across Papers`: summarize which dimensions are best informed and which are sparse.
        - `Important Limitations`: identify limitations of this literature set for the downstream prediction task.

        Column definitions:
        {column_defs}

        {bundle_text}
        """
    ).strip()


def output_path_for_part(
    *,
    output_dir: Path,
    output_prefix: str,
    part_idx: int,
    n_parts: int,
) -> Path:
    stem = output_prefix
    if n_parts > 1:
        stem = f"{stem}_part{part_idx:02d}"
    return output_dir / f"{stem}.jsonl"


def main() -> None:
    args = parse_args()
    args.bundle_dir.mkdir(parents=True, exist_ok=True)

    summary_rows = load_rows(args.collection_summary_csv)
    if args.max_collections is not None:
        summary_rows = summary_rows[: max(0, args.max_collections)]

    combined_rows = {
        row["custom_id"]: row for row in load_rows(args.combined_csv) if row.get("custom_id")
    }
    metadata_map = load_metadata_map(args.metadata_csv)
    column_defs = format_prediction_task_column_definitions()

    records: list[dict] = []
    manifest_rows: list[dict[str, object]] = []
    prompt_preview_written = False

    for row in summary_rows:
        collection_id = str(row["collection_id"])
        n_filters = int(row.get("n_filters", 0) or 0)
        filter_label = str(row.get("filter_label", "")).strip()
        set_path = Path(str(row["set_path"]))
        member_ids = [member_row["custom_id"] for member_row in load_rows(set_path)]
        collection_rows = [combined_rows[custom_id] for custom_id in member_ids]

        entries = build_entries(
            collection_rows=collection_rows,
            metadata_map=metadata_map,
        )
        bundle_text = build_collection_bundle(
            n_total_papers=len(collection_rows),
            entries_text=entries,
        )
        bundle_path = args.bundle_dir / f"{collection_id}.md"
        bundle_path.write_text(bundle_text, encoding="utf-8")

        prompt_text = build_collection_prompt(
            bundle_text=bundle_text,
            column_defs=column_defs,
        )
        if not prompt_preview_written:
            preview_dir = args.bundle_dir / "prompt_previews"
            preview_dir.mkdir(parents=True, exist_ok=True)
            (preview_dir / "metadata_collection_prompt_preview.md").write_text(
                prompt_text,
                encoding="utf-8",
            )
            prompt_preview_written = True

        custom_id = f"collection_metadata/{collection_id}"
        records.append(
            build_openai_request(
                custom_id=custom_id,
                model=args.model,
                system_prompt=(
                    "You are a careful research analyst writing literature analysis "
                    "reports for prediction support."
                ),
                user_prompt=prompt_text,
                include_logprobs=False,
                response_format_json=False,
                include_explanation=False,
            )
        )
        manifest_rows.append(
            {
                "collection_id": collection_id,
                "custom_id": custom_id,
                "n_filters": n_filters,
                "filter_label": filter_label,
                "count": len(collection_rows),
                "bundle_chars": len(bundle_text),
                "bundle_path": str(bundle_path),
            }
        )

    manifest_path = args.bundle_dir / "request_manifest.csv"
    pd.DataFrame(manifest_rows).to_csv(manifest_path, index=False)
    print(manifest_path)

    record_batches = chunk_rows(records, args.collections_per_file)
    for part_idx, record_batch in enumerate(record_batches, start=1):
        output_path = output_path_for_part(
            output_dir=args.output_dir,
            output_prefix=args.output_prefix,
            part_idx=part_idx,
            n_parts=len(record_batches),
        )
        count = write_jsonl(output_path, record_batch)
        print(f"Wrote {count} requests to {output_path}")


if __name__ == "__main__":
    main()
