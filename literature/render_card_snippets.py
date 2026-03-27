#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path


RELEVANCE_POINTS = {
    "exact": 4.0,
    "close": 3.0,
    "adjacent": 2.0,
    "weak": 1.0,
    "mention_only": 0.5,
    "none": 0.0,
    "N/A": 0.0,
    "N/R": 0.0,
    "": 0.0,
}

OUTCOME_POINTS = {
    "efficiency_or_payoff": 1.0,
    "mixed": 0.8,
    "non_payoff_behavior": 0.2,
    "N/R": 0.0,
    "N/A": 0.0,
    "": 0.0,
}

TIER_PRIORITY = {
    "informative_direct": 4,
    "informative_indirect": 3,
    "contextual": 2,
    "mention_only": 1,
    "not_present": 0,
    "N/R": -1,
}

DIMENSION_LABELS = {
    "player_count": "player_count",
    "num_rounds": "num_rounds",
    "chat": "chat",
    "all_or_nothing": "all_or_nothing",
    "default_contrib": "default_contrib",
    "mpcr": "mpcr",
    "punishment_cost": "punishment_cost",
    "punishment_tech": "punishment_tech",
    "reward_exists": "reward_exists",
    "reward_cost": "reward_cost",
    "reward_tech": "reward_tech",
    "show_n_rounds": "show_n_rounds",
    "show_other_summaries": "show_other_summaries",
    "show_punishment_id": "show_punishment_id",
}


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def as_int(value: str) -> int:
    return int(value) if value else 0


def score_row(row: dict[str, str]) -> tuple[float, dict[str, float]]:
    components = {
        "pgg": RELEVANCE_POINTS.get(row["relevance_pgg_or_variant"], 0.0),
        "punishment": RELEVANCE_POINTS.get(row["relevance_punishment_or_sanctions"], 0.0),
        "efficiency": RELEVANCE_POINTS.get(row["relevance_efficiency_or_related_payoff_outcome"], 0.0),
        "paper_type": 1.0 if row["paper_type_primary"] == "empirical" else 0.5,
        "outcomes": OUTCOME_POINTS.get(row["outcomes_primary_outcome_type"], 0.0),
        "dimensions_contextual": min(as_int(row["dimension_contextual_or_better_count"]) / 14.0, 1.0),
        "dimensions_direct": min(as_int(row["dimension_informative_direct_count"]) / 14.0, 1.0),
    }
    score = round(
        3.0 * components["pgg"]
        + 3.0 * components["punishment"]
        + 2.0 * components["efficiency"]
        + 1.0 * components["paper_type"]
        + 1.0 * components["outcomes"]
        + 0.5 * components["dimensions_contextual"]
        + 0.5 * components["dimensions_direct"],
        3,
    )
    return score, components


def informative_dimension_line(dimension_row: dict[str, str]) -> str:
    effect = dimension_row["effect_direction"]
    basis = dimension_row["evidence_basis"]
    notes = dimension_row["notes"].strip()
    effect_part = f"; effect={effect}" if effect else ""
    basis_part = f"; basis={basis}" if basis else ""
    notes_part = f"; notes={notes}" if notes else ""
    return (
        f"- {DIMENSION_LABELS.get(dimension_row['dimension'], dimension_row['dimension'])}"
        f" [{dimension_row['evidence_tier']}{effect_part}{basis_part}]{notes_part}"
    )


def build_snippet(row: dict[str, str], dim_rows: list[dict[str, str]]) -> str:
    informative_rows = [
        d
        for d in dim_rows
        if d["evidence_tier"] in {"informative_direct", "informative_indirect", "contextual", "mention_only"}
    ]
    informative_rows.sort(
        key=lambda d: (
            -TIER_PRIORITY.get(d["evidence_tier"], -1),
            d["dimension"],
        )
    )
    dimension_lines = "\n".join(informative_dimension_line(d) for d in informative_rows)
    if not dimension_lines:
        dimension_lines = "- None"

    limitations = row["important_limitations_joined"].strip() or "None recorded."
    key_claims = row["key_claims_joined"].strip() or "None recorded."

    return "\n".join(
        [
            f"[Paper] {row['custom_id']}",
            f"Type: {row['paper_type_primary']} | empirical={row['paper_type_empirical']} | experimental={row['paper_type_experimental']}",
            (
                "Relevance: "
                f"pgg_or_variant={row['relevance_pgg_or_variant']}; "
                f"punishment_or_sanctions={row['relevance_punishment_or_sanctions']}; "
                f"efficiency_or_related_payoff_outcome={row['relevance_efficiency_or_related_payoff_outcome']}"
            ),
            (
                "Outcomes: "
                f"primary={row['outcomes_primary_outcome_type']}; "
                f"overall_effect_on_efficiency_or_payoff={row['overall_effect_direction_on_efficiency_or_related_payoff']}"
            ),
            "Informative dimensions:",
            dimension_lines,
            "Overall summary:",
            row["overall_summary"].strip(),
            "Paper findings:",
            row["paper_findings"].strip(),
            "Decision support:",
            row["decision_support"].strip(),
            "Key claims:",
            key_claims,
            "Important limitations:",
            limitations,
        ]
    )


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description="Render paper evidence cards into augmentation-ready text snippets.")
    parser.add_argument(
        "--papers",
        type=Path,
        default=Path("literature/output/evidence_cards/literature_evidence_cards_cleaned/combined.csv"),
        help="Combined evidence-card CSV from parse_evidence_card_batch_output.py",
    )
    parser.add_argument(
        "--dimensions",
        type=Path,
        default=Path("literature/output/evidence_cards/literature_evidence_cards_cleaned/dimensions.csv"),
        help="Dimensions CSV from parse_evidence_card_batch_output.py",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("literature/output/evidence_cards/literature_evidence_cards_cleaned/card_snippets"),
        help="Directory for rendered snippet outputs",
    )
    parser.add_argument(
        "--example-count",
        type=int,
        default=5,
        help="Number of top and bottom ranked examples to include in the sample markdown",
    )
    args = parser.parse_args()

    papers = load_csv(args.papers)
    dimensions = load_csv(args.dimensions)
    dims_by_paper: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in dimensions:
        dims_by_paper[row["custom_id"]].append(row)

    rendered_rows: list[dict[str, object]] = []
    for row in papers:
        score, components = score_row(row)
        snippet = build_snippet(row, dims_by_paper[row["custom_id"]])
        rendered_rows.append(
            {
                "custom_id": row["custom_id"],
                "relevance_score": score,
                "score_pgg": components["pgg"],
                "score_punishment": components["punishment"],
                "score_efficiency": components["efficiency"],
                "score_paper_type": components["paper_type"],
                "score_outcomes": components["outcomes"],
                "score_dimensions_contextual": round(components["dimensions_contextual"], 3),
                "score_dimensions_direct": round(components["dimensions_direct"], 3),
                "paper_type_primary": row["paper_type_primary"],
                "paper_type_empirical": row["paper_type_empirical"],
                "paper_type_experimental": row["paper_type_experimental"],
                "relevance_pgg_or_variant": row["relevance_pgg_or_variant"],
                "relevance_punishment_or_sanctions": row["relevance_punishment_or_sanctions"],
                "relevance_efficiency_or_related_payoff_outcome": row[
                    "relevance_efficiency_or_related_payoff_outcome"
                ],
                "outcomes_primary_outcome_type": row["outcomes_primary_outcome_type"],
                "overall_effect_direction_on_efficiency_or_related_payoff": row[
                    "overall_effect_direction_on_efficiency_or_related_payoff"
                ],
                "dimension_contextual_or_better_count": row["dimension_contextual_or_better_count"],
                "dimension_informative_direct_count": row["dimension_informative_direct_count"],
                "snippet": snippet,
            }
        )

    rendered_rows.sort(
        key=lambda r: (
            -float(r["relevance_score"]),
            r["custom_id"],
        )
    )

    output_dir = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = output_dir / "card_snippets.csv"
    jsonl_path = output_dir / "card_snippets.jsonl"
    examples_path = output_dir / "card_snippet_examples.md"
    summary_path = output_dir / "card_snippet_summary.json"

    write_csv(
        csv_path,
        rendered_rows,
        [
            "custom_id",
            "relevance_score",
            "score_pgg",
            "score_punishment",
            "score_efficiency",
            "score_paper_type",
            "score_outcomes",
            "score_dimensions_contextual",
            "score_dimensions_direct",
            "paper_type_primary",
            "paper_type_empirical",
            "paper_type_experimental",
            "relevance_pgg_or_variant",
            "relevance_punishment_or_sanctions",
            "relevance_efficiency_or_related_payoff_outcome",
            "outcomes_primary_outcome_type",
            "overall_effect_direction_on_efficiency_or_related_payoff",
            "dimension_contextual_or_better_count",
            "dimension_informative_direct_count",
            "snippet",
        ],
    )

    with jsonl_path.open("w") as f:
        for row in rendered_rows:
            f.write(json.dumps(row) + "\n")

    example_count = min(args.example_count, len(rendered_rows))
    top_examples = rendered_rows[:example_count]
    bottom_examples = rendered_rows[-example_count:]

    example_lines = ["# Card Snippet Examples", "", "## Most Relevant (heuristic ranking)", ""]
    for row in top_examples:
        example_lines.extend(
            [
                f"### {row['custom_id']} (score={row['relevance_score']})",
                "",
                "```text",
                row["snippet"],
                "```",
                "",
            ]
        )
    example_lines.extend(["## Least Relevant (heuristic ranking)", ""])
    for row in bottom_examples:
        example_lines.extend(
            [
                f"### {row['custom_id']} (score={row['relevance_score']})",
                "",
                "```text",
                row["snippet"],
                "```",
                "",
            ]
        )
    examples_path.write_text("\n".join(example_lines))

    with summary_path.open("w") as f:
        json.dump(
            {
                "n_snippets": len(rendered_rows),
                "example_count": example_count,
                "csv": str(csv_path),
                "jsonl": str(jsonl_path),
                "examples_markdown": str(examples_path),
                "top_example_ids": [row["custom_id"] for row in top_examples],
                "bottom_example_ids": [row["custom_id"] for row in bottom_examples],
            },
            f,
            indent=2,
        )

    print(csv_path)
    print(jsonl_path)
    print(examples_path)
    print(summary_path)


if __name__ == "__main__":
    main()
