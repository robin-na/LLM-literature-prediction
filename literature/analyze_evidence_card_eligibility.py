#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path
from typing import Callable


STRICT = {"exact", "close"}
BROAD = {"exact", "close", "adjacent"}
PAYOFF_OUTCOMES = {"efficiency_or_payoff", "mixed"}


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def as_int(row: dict[str, str], key: str) -> int:
    value = row.get(key, "")
    return int(value) if value else 0


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def breakdown(counter: Counter[str]) -> str:
    if not counter:
        return ""
    return " | ".join(f"{key}:{value}" for key, value in counter.most_common())


def make_summary_row(name: str, description: str, rows: list[dict[str, str]]) -> dict[str, object]:
    return {
        "set_name": name,
        "description": description,
        "count": len(rows),
        "paper_type_primary": breakdown(Counter(r["paper_type_primary"] for r in rows)),
        "paper_type_empirical": breakdown(Counter(r["paper_type_empirical"] for r in rows)),
        "paper_type_experimental": breakdown(Counter(r["paper_type_experimental"] for r in rows)),
        "relevance_pgg_or_variant": breakdown(Counter(r["relevance_pgg_or_variant"] for r in rows)),
        "relevance_punishment_or_sanctions": breakdown(Counter(r["relevance_punishment_or_sanctions"] for r in rows)),
        "relevance_efficiency_or_related_payoff_outcome": breakdown(
            Counter(r["relevance_efficiency_or_related_payoff_outcome"] for r in rows)
        ),
        "outcomes_primary_outcome_type": breakdown(Counter(r["outcomes_primary_outcome_type"] for r in rows)),
        "mean_dimension_contextual_or_better_count": round(
            sum(as_int(r, "dimension_contextual_or_better_count") for r in rows) / len(rows), 2
        )
        if rows
        else 0.0,
        "mean_dimension_informative_direct_count": round(
            sum(as_int(r, "dimension_informative_direct_count") for r in rows) / len(rows), 2
        )
        if rows
        else 0.0,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Summarize augmentation-eligible literature sets from parsed evidence-card outputs."
    )
    parser.add_argument(
        "--papers",
        default="literature/output/evidence_cards/literature_evidence_cards_cleaned/papers.csv",
        help="Parsed paper-level CSV from parse_evidence_card_batch_output.py",
    )
    parser.add_argument(
        "--output-dir",
        default="literature/output/evidence_cards/literature_evidence_cards_cleaned/eligibility",
        help="Directory for summary tables and set membership files",
    )
    args = parser.parse_args()

    papers_path = Path(args.papers)
    output_dir = Path(args.output_dir)
    rows = load_rows(papers_path)

    def base_ok(r: dict[str, str]) -> bool:
        return r.get("parse_status") == "ok" and r.get("status_code") == "200"

    def contextual(r: dict[str, str]) -> bool:
        return as_int(r, "dimension_contextual_or_better_count") >= 1

    def direct(r: dict[str, str]) -> bool:
        return as_int(r, "dimension_informative_direct_count") >= 1

    set_defs: list[tuple[str, str, Callable[[dict[str, str]], bool]]] = [
        (
            "exact_predictive_empirical_payoff",
            "Empirical papers only, with exact relevance for PGG/variant, punishment, and efficiency/payoff, and directly reported payoff-like outcomes.",
            lambda r: base_ok(r)
            and contextual(r)
            and r["paper_type_primary"] == "empirical"
            and r["relevance_pgg_or_variant"] == "exact"
            and r["relevance_punishment_or_sanctions"] == "exact"
            and r["relevance_efficiency_or_related_payoff_outcome"] == "exact"
            and r["outcomes_primary_outcome_type"] in PAYOFF_OUTCOMES,
        ),
        (
            "strict_predictive_all_types",
            "PGG/variant exact-or-close, punishment exact-or-close, efficiency/payoff exact-or-close, any paper type.",
            lambda r: base_ok(r)
            and contextual(r)
            and r["relevance_pgg_or_variant"] in STRICT
            and r["relevance_punishment_or_sanctions"] in STRICT
            and r["relevance_efficiency_or_related_payoff_outcome"] in STRICT,
        ),
        (
            "strict_predictive_empirical",
            "Same as strict_predictive_all_types, restricted to empirical papers.",
            lambda r: base_ok(r)
            and contextual(r)
            and r["paper_type_primary"] == "empirical"
            and r["relevance_pgg_or_variant"] in STRICT
            and r["relevance_punishment_or_sanctions"] in STRICT
            and r["relevance_efficiency_or_related_payoff_outcome"] in STRICT,
        ),
        (
            "strict_predictive_empirical_payoff",
            "Same as strict_predictive_empirical, plus the paper directly reports payoff-like outcomes (efficiency_or_payoff or mixed).",
            lambda r: base_ok(r)
            and contextual(r)
            and r["paper_type_primary"] == "empirical"
            and r["relevance_pgg_or_variant"] in STRICT
            and r["relevance_punishment_or_sanctions"] in STRICT
            and r["relevance_efficiency_or_related_payoff_outcome"] in STRICT
            and r["outcomes_primary_outcome_type"] in PAYOFF_OUTCOMES,
        ),
        (
            "strict_predictive_all_types_direct_dimension",
            "Same as strict_predictive_all_types, but requiring at least one informative_direct dimension.",
            lambda r: base_ok(r)
            and direct(r)
            and r["relevance_pgg_or_variant"] in STRICT
            and r["relevance_punishment_or_sanctions"] in STRICT
            and r["relevance_efficiency_or_related_payoff_outcome"] in STRICT,
        ),
        (
            "pgg_punishment_empirical_any_outcome",
            "PGG/variant exact-or-close and punishment exact-or-close, empirical only, regardless of whether payoff outcomes are direct.",
            lambda r: base_ok(r)
            and contextual(r)
            and r["paper_type_primary"] == "empirical"
            and r["relevance_pgg_or_variant"] in STRICT
            and r["relevance_punishment_or_sanctions"] in STRICT,
        ),
        (
            "broad_support_all_types",
            "PGG/variant, punishment, and efficiency/payoff all exact-close-adjacent, any paper type.",
            lambda r: base_ok(r)
            and contextual(r)
            and r["relevance_pgg_or_variant"] in BROAD
            and r["relevance_punishment_or_sanctions"] in BROAD
            and r["relevance_efficiency_or_related_payoff_outcome"] in BROAD,
        ),
        (
            "broad_support_empirical",
            "Same as broad_support_all_types, restricted to empirical papers.",
            lambda r: base_ok(r)
            and contextual(r)
            and r["paper_type_primary"] == "empirical"
            and r["relevance_pgg_or_variant"] in BROAD
            and r["relevance_punishment_or_sanctions"] in BROAD
            and r["relevance_efficiency_or_related_payoff_outcome"] in BROAD,
        ),
    ]

    summary_rows: list[dict[str, object]] = []
    membership_rows: list[dict[str, object]] = []

    selected_by_set: dict[str, list[dict[str, str]]] = {}
    for set_name, description, predicate in set_defs:
        selected = [r for r in rows if predicate(r)]
        selected_by_set[set_name] = selected
        summary_rows.append(make_summary_row(set_name, description, selected))

    for row in rows:
        membership = {
            "custom_id": row["custom_id"],
            "paper_type_primary": row["paper_type_primary"],
            "paper_type_empirical": row["paper_type_empirical"],
            "paper_type_experimental": row["paper_type_experimental"],
            "relevance_pgg_or_variant": row["relevance_pgg_or_variant"],
            "relevance_punishment_or_sanctions": row["relevance_punishment_or_sanctions"],
            "relevance_efficiency_or_related_payoff_outcome": row[
                "relevance_efficiency_or_related_payoff_outcome"
            ],
            "outcomes_primary_outcome_type": row["outcomes_primary_outcome_type"],
            "dimension_contextual_or_better_count": row["dimension_contextual_or_better_count"],
            "dimension_informative_direct_count": row["dimension_informative_direct_count"],
        }
        for set_name, _, predicate in set_defs:
            membership[set_name] = "yes" if predicate(row) else "no"
        membership_rows.append(membership)

    output_dir.mkdir(parents=True, exist_ok=True)
    write_csv(
        output_dir / "eligibility_summary.csv",
        summary_rows,
        [
            "set_name",
            "description",
            "count",
            "paper_type_primary",
            "paper_type_empirical",
            "paper_type_experimental",
            "relevance_pgg_or_variant",
            "relevance_punishment_or_sanctions",
            "relevance_efficiency_or_related_payoff_outcome",
            "outcomes_primary_outcome_type",
            "mean_dimension_contextual_or_better_count",
            "mean_dimension_informative_direct_count",
        ],
    )
    write_csv(
        output_dir / "eligibility_membership.csv",
        membership_rows,
        [
            "custom_id",
            "paper_type_primary",
            "paper_type_empirical",
            "paper_type_experimental",
            "relevance_pgg_or_variant",
            "relevance_punishment_or_sanctions",
            "relevance_efficiency_or_related_payoff_outcome",
            "outcomes_primary_outcome_type",
            "dimension_contextual_or_better_count",
            "dimension_informative_direct_count",
        ]
        + [set_name for set_name, _, _ in set_defs],
    )

    set_dir = output_dir / "sets"
    set_dir.mkdir(parents=True, exist_ok=True)
    for set_name, description, _ in set_defs:
        selected = selected_by_set[set_name]
        write_csv(
            set_dir / f"{set_name}.csv",
            [
                {
                    "custom_id": r["custom_id"],
                    "paper_type_primary": r["paper_type_primary"],
                    "paper_type_empirical": r["paper_type_empirical"],
                    "paper_type_experimental": r["paper_type_experimental"],
                    "relevance_pgg_or_variant": r["relevance_pgg_or_variant"],
                    "relevance_punishment_or_sanctions": r["relevance_punishment_or_sanctions"],
                    "relevance_efficiency_or_related_payoff_outcome": r[
                        "relevance_efficiency_or_related_payoff_outcome"
                    ],
                    "outcomes_primary_outcome_type": r["outcomes_primary_outcome_type"],
                    "dimension_contextual_or_better_count": r["dimension_contextual_or_better_count"],
                    "dimension_informative_direct_count": r["dimension_informative_direct_count"],
                }
                for r in selected
            ],
            [
                "custom_id",
                "paper_type_primary",
                "paper_type_empirical",
                "paper_type_experimental",
                "relevance_pgg_or_variant",
                "relevance_punishment_or_sanctions",
                "relevance_efficiency_or_related_payoff_outcome",
                "outcomes_primary_outcome_type",
                "dimension_contextual_or_better_count",
                "dimension_informative_direct_count",
            ],
        )

    summary_json = {
        "papers_csv": str(papers_path),
        "n_rows": len(rows),
        "sets": summary_rows,
        "set_descriptions": {set_name: description for set_name, description, _ in set_defs},
    }
    with (output_dir / "eligibility_summary.json").open("w") as f:
        json.dump(summary_json, f, indent=2)

    print(f"Wrote {output_dir / 'eligibility_summary.csv'}")
    print(f"Wrote {output_dir / 'eligibility_membership.csv'}")
    print(f"Wrote {output_dir / 'eligibility_summary.json'}")
    print(f"Wrote {len(set_defs)} set files under {set_dir}")


if __name__ == "__main__":
    main()
