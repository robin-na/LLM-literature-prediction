from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import pandas as pd


DEFAULT_PAPERS_CSV = Path(
    "literature/output/evidence_cards/literature_evidence_cards_cleaned/papers.csv"
)
DEFAULT_BROAD_SET_CSV = Path(
    "literature/output/evidence_cards/literature_evidence_cards_cleaned/eligibility/sets/broad_support_all_types.csv"
)
DEFAULT_CURRENT_INDIVIDUAL_SET_CSV = Path(
    "literature/output/evidence_cards/literature_evidence_cards_cleaned/eligibility/sets/strict_predictive_empirical_payoff.csv"
)
DEFAULT_OUTPUT_DIR = Path(
    "literature/output/evidence_cards/literature_evidence_cards_cleaned/collection_switch_sets"
)
EXCLUDED_IDS = {"PGG_MS_202502"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build the agreed 8 collection-set CSVs from the broad literature pool, "
            "excluding PGG_MS_202502, plus the remaining broad individual-paper set."
        )
    )
    parser.add_argument(
        "--papers-csv",
        type=Path,
        default=DEFAULT_PAPERS_CSV,
        help="Paper-level parsed evidence-card CSV.",
    )
    parser.add_argument(
        "--broad-set-csv",
        type=Path,
        default=DEFAULT_BROAD_SET_CSV,
        help="CSV containing the broad all-types eligible paper ids.",
    )
    parser.add_argument(
        "--current-individual-set-csv",
        type=Path,
        default=DEFAULT_CURRENT_INDIVIDUAL_SET_CSV,
        help="Existing individual-paper set to subtract when building the remaining broad set.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory for collection-set CSVs and summary files.",
    )
    return parser.parse_args()


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def collection_specs() -> list[dict[str, object]]:
    return [
        {
            "collection_id": "broad_all",
            "a_pgg_pun_exactclose": False,
            "b_payoff_like_outcome": False,
            "c_empirical_only": False,
            "description": "Broad all-types pool with no additional A/B/C switches turned on.",
        },
        {
            "collection_id": "broad_empirical",
            "a_pgg_pun_exactclose": False,
            "b_payoff_like_outcome": False,
            "c_empirical_only": True,
            "description": "Broad pool restricted to empirical papers only.",
        },
        {
            "collection_id": "broad_payoff_like",
            "a_pgg_pun_exactclose": False,
            "b_payoff_like_outcome": True,
            "c_empirical_only": False,
            "description": "Broad pool restricted to papers that report payoff-like outcomes.",
        },
        {
            "collection_id": "broad_empirical_payoff_like",
            "a_pgg_pun_exactclose": False,
            "b_payoff_like_outcome": True,
            "c_empirical_only": True,
            "description": "Broad pool restricted to empirical papers with payoff-like outcomes.",
        },
        {
            "collection_id": "exactclose_pggpun",
            "a_pgg_pun_exactclose": True,
            "b_payoff_like_outcome": False,
            "c_empirical_only": False,
            "description": "Broad pool restricted to exact/close PGG relevance and exact/close punishment relevance.",
        },
        {
            "collection_id": "exactclose_pggpun_empirical",
            "a_pgg_pun_exactclose": True,
            "b_payoff_like_outcome": False,
            "c_empirical_only": True,
            "description": "Exact/close PGG and punishment relevance, empirical only.",
        },
        {
            "collection_id": "exactclose_pggpun_payoff_like",
            "a_pgg_pun_exactclose": True,
            "b_payoff_like_outcome": True,
            "c_empirical_only": False,
            "description": "Exact/close PGG and punishment relevance, plus payoff-like outcomes.",
        },
        {
            "collection_id": "exactclose_empirical_payoff",
            "a_pgg_pun_exactclose": True,
            "b_payoff_like_outcome": True,
            "c_empirical_only": True,
            "description": "Exact/close PGG and punishment relevance, payoff-like outcomes, empirical only.",
        },
    ]


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    sets_dir = args.output_dir / "sets"
    sets_dir.mkdir(parents=True, exist_ok=True)

    broad_ids = {
        row["custom_id"]
        for row in load_rows(args.broad_set_csv)
        if row.get("custom_id") and row["custom_id"] not in EXCLUDED_IDS
    }
    current_individual_ids = {
        row["custom_id"]
        for row in load_rows(args.current_individual_set_csv)
        if row.get("custom_id") and row["custom_id"] not in EXCLUDED_IDS
    }

    papers = pd.read_csv(args.papers_csv).rename(
        columns={
            "paper_type_primary": "paper_type",
            "relevance_pgg_or_variant": "pgg_rel",
            "relevance_punishment_or_sanctions": "pun_rel",
            "relevance_efficiency_or_related_payoff_outcome": "pay_rel",
            "outcomes_primary_outcome_type": "primary_outcome_type",
        }
    )
    papers = papers[papers["custom_id"].isin(broad_ids)].copy()
    papers = papers[~papers["custom_id"].isin(EXCLUDED_IDS)].copy()
    papers["payoff_like_outcome"] = papers["primary_outcome_type"].isin(
        ["efficiency_or_payoff", "mixed"]
    )

    summary_rows: list[dict[str, object]] = []

    for spec in collection_specs():
        subset = papers.copy()
        if spec["a_pgg_pun_exactclose"]:
            subset = subset[
                subset["pgg_rel"].isin(["exact", "close"])
                & subset["pun_rel"].isin(["exact", "close"])
            ]
        if spec["b_payoff_like_outcome"]:
            subset = subset[subset["payoff_like_outcome"]]
        if spec["c_empirical_only"]:
            subset = subset[subset["paper_type"] == "empirical"]

        subset = subset.sort_values(
            [
                "pgg_rel",
                "pun_rel",
                "pay_rel",
                "dimension_informative_direct_count",
                "dimension_contextual_or_better_count",
                "custom_id",
            ],
            ascending=[True, True, True, False, False, True],
            kind="mergesort",
        )

        output_path = sets_dir / f"{spec['collection_id']}.csv"
        subset[["custom_id"]].to_csv(output_path, index=False)

        summary_rows.append(
            {
                **spec,
                "count": int(len(subset)),
                "set_path": str(output_path),
            }
        )

    remaining = papers[~papers["custom_id"].isin(current_individual_ids)].copy()
    remaining_path = sets_dir / "broad_all_remaining_after_exactclose_empirical_payoff.csv"
    remaining[["custom_id"]].sort_values("custom_id").to_csv(remaining_path, index=False)

    summary_df = pd.DataFrame(summary_rows).sort_values("collection_id").reset_index(drop=True)
    summary_path = args.output_dir / "collection_switch_sets_summary.csv"
    summary_df.to_csv(summary_path, index=False)

    meta = {
        "excluded_ids": sorted(EXCLUDED_IDS),
        "broad_universe_count": int(len(papers)),
        "current_individual_set_count_excluding_excluded_ids": int(len(current_individual_ids)),
        "remaining_broad_count": int(len(remaining)),
        "remaining_broad_set_path": str(remaining_path),
        "n_collections": int(len(summary_df)),
    }
    summary_json_path = args.output_dir / "collection_switch_sets_summary.json"
    summary_json_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")

    print(summary_path)
    print(summary_json_path)
    print(remaining_path)


if __name__ == "__main__":
    main()
