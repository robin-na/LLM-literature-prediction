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
from literature.build_prediction_batch_from_card_memos import build_apa_citation  # noqa: E402
from positive_cases.build_paper_only_new_variants_batch_input import (  # noqa: E402
    build_openai_request,
)


DEFAULT_MODEL = "gpt-4.1-2025-04-14"
DEFAULT_COLLECTION_SUMMARY_CSV = Path(
    "literature/output/evidence_cards/literature_evidence_cards_cleaned/collection_switch_sets/collection_switch_sets_summary.csv"
)
DEFAULT_COMBINED_CSV = Path(
    "literature/output/evidence_cards/literature_evidence_cards_cleaned/combined.csv"
)
DEFAULT_METADATA_CSV = Path("paper_collection/WoS_251031_fileInfo.csv")
DEFAULT_BUNDLE_DIR = Path("literature/output/collection_synthesis_inputs")

DIMENSION_ORDER = [
    "player_count",
    "num_rounds",
    "chat",
    "all_or_nothing",
    "default_contrib",
    "mpcr",
    "punishment_cost",
    "punishment_tech",
    "reward_exists",
    "reward_cost",
    "reward_tech",
    "show_n_rounds",
    "show_other_summaries",
    "show_punishment_id",
]

DIMENSION_LABELS = {dimension: dimension for dimension in DIMENSION_ORDER}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build hierarchical stage-1 batch JSONL for collection synthesis. "
            "This partitions the broad literature pool into the 8 disjoint A/B/C "
            "subsets and emits one literature analysis-report synthesis request for each."
        )
    )
    parser.add_argument(
        "--collection-summary-csv",
        type=Path,
        default=DEFAULT_COLLECTION_SUMMARY_CSV,
        help="Summary CSV emitted by build_collection_switch_sets.py",
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
        help="Model used to synthesize the stage-1 literature analysis reports.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("openAI_batch_input"),
        help="Directory for output JSONL files.",
    )
    parser.add_argument(
        "--output-prefix",
        default="synthesis_collection_switch_sets_stage1",
        help="Prefix for output batch files.",
    )
    parser.add_argument(
        "--bundle-dir",
        type=Path,
        default=DEFAULT_BUNDLE_DIR,
        help="Directory to write rendered paper-set digests and manifests.",
    )
    parser.add_argument(
        "--max-bundle-chars",
        type=int,
        default=100000000,
        help="Unused compatibility option retained for CLI compatibility. Stage 1 now builds one request per subset.",
    )
    return parser.parse_args()


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def normalize_custom_id(value: str) -> str:
    return Path(value).stem


def load_metadata_map(path: Path) -> dict[str, dict[str, str]]:
    metadata_map: dict[str, dict[str, str]] = {}
    for row in load_rows(path):
        custom_id = normalize_custom_id(row.get("custom_id", ""))
        if custom_id:
            metadata_map[custom_id] = row
    return metadata_map


def clean_text(text: str) -> str:
    return " ".join((text or "").split())


def relevance_rank(value: str) -> int:
    return {
        "exact": 4,
        "close": 3,
        "adjacent": 2,
        "weak": 1,
        "none": 0,
        "N/R": -1,
    }.get(str(value), -1)


def paper_sort_key(row: dict[str, str]) -> tuple[int, int, int, int, int, str]:
    return (
        relevance_rank(row.get("relevance_pgg_or_variant", "")),
        relevance_rank(row.get("relevance_punishment_or_sanctions", "")),
        relevance_rank(row.get("relevance_efficiency_or_related_payoff_outcome", "")),
        int(row.get("dimension_informative_direct_count", 0) or 0),
        int(row.get("dimension_contextual_or_better_count", 0) or 0),
        str(row.get("custom_id", "")),
    )


def dimension_lists(row: dict[str, str]) -> tuple[list[str], list[str]]:
    direct: list[str] = []
    contextual_or_better: list[str] = []
    for dimension in DIMENSION_ORDER:
        tier = str(row.get(f"dim_{dimension}_evidence_tier", "")).strip()
        if tier == "informative_direct":
            direct.append(DIMENSION_LABELS[dimension])
        if tier in {"informative_direct", "informative_indirect", "contextual"}:
            contextual_or_better.append(DIMENSION_LABELS[dimension])
    return direct, contextual_or_better


def render_digest_entry(
    row: dict[str, str],
    metadata: dict[str, str] | None,
) -> str:
    citation = build_apa_citation(metadata or {})
    direct_dims, context_dims = dimension_lists(row)
    if not direct_dims:
        direct_dims = context_dims
    direct_text = ", ".join(direct_dims[:6]) if direct_dims else "none"
    findings = clean_text(row.get("paper_findings", ""))
    decision = clean_text(row.get("decision_support", ""))
    return dedent(
        f"""
        - source: {citation}
          type: {row['paper_type_primary']} | empirical={row['paper_type_empirical']} | experimental={row['paper_type_experimental']}
          relevance: pgg={row['relevance_pgg_or_variant']} | punishment={row['relevance_punishment_or_sanctions']} | payoff={row['relevance_efficiency_or_related_payoff_outcome']}
          outcomes: primary={row['outcomes_primary_outcome_type']} | overall_effect={row['overall_effect_direction_on_efficiency_or_related_payoff']}
          dimensions: {direct_text}
          findings: {findings}
          prediction_guidance: {decision}
        """
    ).strip()


def build_entries(
    *,
    collection_rows: list[dict[str, str]],
    metadata_map: dict[str, dict[str, str]],
) -> list[str]:
    sorted_rows = sorted(collection_rows, key=paper_sort_key, reverse=True)
    return [
        render_digest_entry(
            row,
            metadata_map.get(row["custom_id"]),
        )
        for row in sorted_rows
    ]


def bool_label(value: bool) -> str:
    return "on" if value else "off"


def as_bool(value: object) -> bool:
    if isinstance(value, bool):
        return value
    text = str(value).strip().lower()
    return text in {"true", "1", "yes", "y"}


def paper_switch_values(row: dict[str, str]) -> tuple[bool, bool, bool]:
    a_on = (
        str(row.get("relevance_pgg_or_variant", "")).strip() in {"exact", "close"}
        and str(row.get("relevance_punishment_or_sanctions", "")).strip() in {"exact", "close"}
    )
    b_on = str(row.get("outcomes_primary_outcome_type", "")).strip() in {
        "efficiency_or_payoff",
        "mixed",
    }
    c_on = str(row.get("paper_type_primary", "")).strip() == "empirical"
    return a_on, b_on, c_on


def leaf_id(a_on: bool, b_on: bool, c_on: bool) -> str:
    return f"leaf_a{int(a_on)}_b{int(b_on)}_c{int(c_on)}"


def leaf_description(a_on: bool, b_on: bool, c_on: bool) -> str:
    return (
        f"A={bool_label(a_on)} (exact/close PGG+punishment), "
        f"B={bool_label(b_on)} (payoff-like outcomes), "
        f"C={bool_label(c_on)} (empirical)"
    )


def build_subset_bundle(
    *,
    subset_id: str,
    a_on: bool,
    b_on: bool,
    c_on: bool,
    n_total_papers: int,
    entries_text: list[str],
) -> str:
    return "\n\n".join(
        [
            "# Paper Set Evidence Digest",
            "Each item below is a compact paper-level analysis digest. Use only this digest.",
            *entries_text,
            "",
        ]
    )


def build_subset_prompt(
    *,
    subset_id: str,
    a_on: bool,
    b_on: bool,
    c_on: bool,
    n_total_papers: int,
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

        Paper-set metadata:
        - Number of papers in this paper set: {n_total_papers}

        Paper-set evidence digest:
        ----------
        {bundle_text}
        ----------
        """
    ).strip()


def write_jsonl(path: Path, records: list[dict]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    return len(records)


def build_leaf_rows(
    *,
    combined_rows: dict[str, dict[str, str]],
    broad_set_path: Path,
) -> tuple[list[dict[str, object]], dict[str, list[dict[str, str]]]]:
    broad_ids = [row["custom_id"] for row in load_rows(broad_set_path)]
    grouped: dict[str, list[dict[str, str]]] = {}

    for custom_id in broad_ids:
        row = combined_rows[custom_id]
        a_on, b_on, c_on = paper_switch_values(row)
        grouped.setdefault(leaf_id(a_on, b_on, c_on), []).append(row)

    leaf_rows: list[dict[str, object]] = []
    for a_on in [False, True]:
        for b_on in [False, True]:
            for c_on in [False, True]:
                key = leaf_id(a_on, b_on, c_on)
                rows = grouped.get(key, [])
                leaf_rows.append(
                    {
                        "leaf_id": key,
                        "a_pgg_pun_exactclose": a_on,
                        "b_payoff_like_outcome": b_on,
                        "c_empirical_only": c_on,
                        "description": leaf_description(a_on, b_on, c_on),
                        "count": len(rows),
                    }
                )
    return leaf_rows, grouped


def build_collection_leaf_rows(
    *,
    collection_summary_rows: list[dict[str, str]],
    leaf_rows: list[dict[str, object]],
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for collection_row in collection_summary_rows:
        require_a = as_bool(collection_row["a_pgg_pun_exactclose"])
        require_b = as_bool(collection_row["b_payoff_like_outcome"])
        require_c = as_bool(collection_row["c_empirical_only"])
        for leaf_row in leaf_rows:
            include_leaf = True
            if require_a and not bool(leaf_row["a_pgg_pun_exactclose"]):
                include_leaf = False
            if require_b and not bool(leaf_row["b_payoff_like_outcome"]):
                include_leaf = False
            if require_c and not bool(leaf_row["c_empirical_only"]):
                include_leaf = False
            if include_leaf and int(leaf_row["count"]) > 0:
                rows.append(
                    {
                        "collection_id": collection_row["collection_id"],
                        "collection_count": int(collection_row["count"]),
                        "leaf_id": leaf_row["leaf_id"],
                        "leaf_count": int(leaf_row["count"]),
                        "a_pgg_pun_exactclose": bool(leaf_row["a_pgg_pun_exactclose"]),
                        "b_payoff_like_outcome": bool(leaf_row["b_payoff_like_outcome"]),
                        "c_empirical_only": bool(leaf_row["c_empirical_only"]),
                        "leaf_description": leaf_row["description"],
                    }
                )
    return rows


def main() -> None:
    args = parse_args()
    args.bundle_dir.mkdir(parents=True, exist_ok=True)
    leaf_sets_dir = args.bundle_dir / "leaf_sets"
    leaf_sets_dir.mkdir(parents=True, exist_ok=True)

    collection_summary_df = pd.read_csv(args.collection_summary_csv)
    collection_summary_rows = collection_summary_df.to_dict("records")
    combined_rows = {row["custom_id"]: row for row in load_rows(args.combined_csv)}
    metadata_map = load_metadata_map(args.metadata_csv)
    column_defs = format_prediction_task_column_definitions()

    broad_row = collection_summary_df.loc[
        collection_summary_df["collection_id"] == "broad_all"
    ]
    if broad_row.empty:
        raise KeyError("Could not find broad_all row in collection summary CSV.")
    broad_set_path = Path(str(broad_row.iloc[0]["set_path"]))

    leaf_rows, grouped_rows = build_leaf_rows(
        combined_rows=combined_rows,
        broad_set_path=broad_set_path,
    )
    collection_leaf_rows = build_collection_leaf_rows(
        collection_summary_rows=collection_summary_rows,
        leaf_rows=leaf_rows,
    )

    records: list[dict] = []
    preview_written = False

    for leaf_row in leaf_rows:
        leaf_id_value = str(leaf_row["leaf_id"])
        rows = grouped_rows.get(leaf_id_value, [])
        set_path = leaf_sets_dir / f"{leaf_id_value}.csv"
        pd.DataFrame({"custom_id": [row["custom_id"] for row in rows]}).to_csv(set_path, index=False)
        leaf_row["set_path"] = str(set_path)

        if not rows:
            continue

        entries = build_entries(
            collection_rows=rows,
            metadata_map=metadata_map,
        )
        custom_id = f"subset_summary/{leaf_id_value}"
        bundle_text = build_subset_bundle(
            subset_id=leaf_id_value,
            a_on=bool(leaf_row["a_pgg_pun_exactclose"]),
            b_on=bool(leaf_row["b_payoff_like_outcome"]),
            c_on=bool(leaf_row["c_empirical_only"]),
            n_total_papers=len(rows),
            entries_text=entries,
        )
        bundle_path = args.bundle_dir / f"{leaf_id_value}.md"
        bundle_path.write_text(bundle_text, encoding="utf-8")
        leaf_row["bundle_chars"] = len(bundle_text)
        leaf_row["custom_id"] = custom_id
        leaf_row["bundle_path"] = str(bundle_path)

        prompt_text = build_subset_prompt(
            subset_id=leaf_id_value,
            a_on=bool(leaf_row["a_pgg_pun_exactclose"]),
            b_on=bool(leaf_row["b_payoff_like_outcome"]),
            c_on=bool(leaf_row["c_empirical_only"]),
            n_total_papers=int(leaf_row["count"]),
            bundle_text=bundle_text,
            column_defs=column_defs,
        )
        if not preview_written:
            preview_dir = args.bundle_dir / "prompt_previews"
            preview_dir.mkdir(parents=True, exist_ok=True)
            (preview_dir / "stage1_subset_prompt_preview.md").write_text(
                prompt_text,
                encoding="utf-8",
            )
            preview_written = True
        records.append(
            build_openai_request(
                custom_id=custom_id,
                model=args.model,
                system_prompt="You are a careful research analyst writing literature analysis reports for prediction support.",
                user_prompt=prompt_text,
                include_logprobs=False,
                response_format_json=False,
                include_explanation=False,
            )
        )

    leaf_manifest_path = args.bundle_dir / "leaf_manifest.csv"
    pd.DataFrame(leaf_rows).sort_values("leaf_id").to_csv(leaf_manifest_path, index=False)
    print(leaf_manifest_path)

    leaf_legend_path = args.bundle_dir / "leaf_legend.csv"
    pd.DataFrame(
        [
            {
                "leaf_id": row["leaf_id"],
                "count": int(row["count"]),
                "a_switch": "exact/close on both PGG relevance and punishment relevance",
                "a_value": "on" if bool(row["a_pgg_pun_exactclose"]) else "off",
                "b_switch": "reports payoff-like outcomes",
                "b_value": "on" if bool(row["b_payoff_like_outcome"]) else "off",
                "c_switch": "empirical paper",
                "c_value": "on" if bool(row["c_empirical_only"]) else "off",
                "summary": row["description"],
            }
            for row in leaf_rows
        ]
    ).sort_values("leaf_id").to_csv(leaf_legend_path, index=False)
    print(leaf_legend_path)

    collection_leaf_map_path = args.bundle_dir / "collection_leaf_map.csv"
    pd.DataFrame(collection_leaf_rows).sort_values(["collection_id", "leaf_id"]).to_csv(
        collection_leaf_map_path, index=False
    )
    print(collection_leaf_map_path)

    broad_ids = [row["custom_id"] for row in load_rows(broad_set_path)]
    if "PGG_MS_202502" in broad_ids:
        raise ValueError("PGG_MS_202502 unexpectedly present in broad_all set.")
    broad_rows = [combined_rows[custom_id] for custom_id in broad_ids]
    broad_entries = build_entries(
        collection_rows=broad_rows,
        metadata_map=metadata_map,
    )
    broad_bundle_text = build_subset_bundle(
        subset_id="broad_all_2011_direct",
        a_on=False,
        b_on=False,
        c_on=False,
        n_total_papers=len(broad_rows),
        entries_text=broad_entries,
    )
    broad_bundle_path = args.bundle_dir / "broad_all_2011_direct.md"
    broad_bundle_path.write_text(broad_bundle_text, encoding="utf-8")
    broad_prompt_text = build_subset_prompt(
        subset_id="broad_all_2011_direct",
        a_on=False,
        b_on=False,
        c_on=False,
        n_total_papers=len(broad_rows),
        bundle_text=broad_bundle_text,
        column_defs=column_defs,
    )
    records.append(
        build_openai_request(
            custom_id="collection_direct/broad_all_2011",
            model=args.model,
            system_prompt="You are a careful research analyst writing literature analysis reports for prediction support.",
            user_prompt=broad_prompt_text,
            include_logprobs=False,
            response_format_json=False,
            include_explanation=False,
        )
    )
    direct_manifest_path = args.bundle_dir / "direct_request_manifest.csv"
    pd.DataFrame(
        [
            {
                "custom_id": "collection_direct/broad_all_2011",
                "collection_id": "broad_all",
                "count": len(broad_rows),
                "bundle_chars": len(broad_bundle_text),
                "bundle_path": str(broad_bundle_path),
                "contains_pgg_ms": False,
            }
        ]
    ).to_csv(direct_manifest_path, index=False)
    print(direct_manifest_path)

    output_path = args.output_dir / f"{args.output_prefix}.jsonl"
    count = write_jsonl(output_path, records)
    print(f"Wrote {count} requests to {output_path}")

if __name__ == "__main__":
    main()
