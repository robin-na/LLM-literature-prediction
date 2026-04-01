from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from batch_inputs.paper_only_variants import (  # noqa: E402
    DEFAULT_MODELS,
    MODEL_TAGS,
    SYSTEM_PROMPT_SINGLE,
    SYSTEM_PROMPT_SINGLE_EXPLANATION,
    build_joint_prompt,
    build_joint_system_prompt,
    build_openai_request,
    build_single_prompt,
)

MODE_CHOICES = ["single", "reasoning", "joint", "joint_reasoning"]
DEFAULT_MODES = ["reasoning"]
DEFAULT_SET_PATH = Path(
    "literature/output/evidence_cards/literature_evidence_cards_cleaned/eligibility/sets/strict_predictive_empirical_payoff.csv"
)
DEFAULT_COMBINED_PATH = Path(
    "literature/output/evidence_cards/literature_evidence_cards_cleaned/combined.csv"
)
DEFAULT_METADATA_CSV = Path("paper_collection/WoS_251031_fileInfo.csv")
DEFAULT_MEMO_ROOT = Path("literature/output/paper_analysis_reports")

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

DIMENSION_LABELS = {
    "player_count": "player count",
    "num_rounds": "number of rounds",
    "chat": "chat",
    "all_or_nothing": "all-or-nothing contribution",
    "default_contrib": "default contribution framing",
    "mpcr": "mpcr",
    "punishment_cost": "punishment cost",
    "punishment_tech": "punishment technology",
    "reward_exists": "reward availability",
    "reward_cost": "reward cost",
    "reward_tech": "reward technology",
    "show_n_rounds": "knowing when the game ends",
    "show_other_summaries": "seeing peer outcomes",
    "show_punishment_id": "seeing punisher identity",
}

TIER_SENTENCE = {
    "informative_direct": "The paper directly informs this dimension.",
    "informative_indirect": "The paper gives an indirect but usable signal on this dimension.",
    "contextual": "The paper provides contextual guidance on this dimension.",
    "mention_only": "The paper mentions this dimension but gives limited predictive guidance.",
}

MEMO_WRAPPER = """Below is an analysis report distilled from one academic paper.
Use it as contextual evidence about how design features may change the efficiency impact of punishment.
Respect the report's stated limitations and do not infer beyond what the report supports."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build model-specific OpenAI batch JSONLs using one paper-card memo at a time "
            "as the augmentation source."
        )
    )
    parser.add_argument(
        "--df-pgg",
        type=Path,
        default=Path("input/pgg_CONFIGmerged_validation.csv"),
        help="Target validation configurations to predict.",
    )
    parser.add_argument(
        "--combined-csv",
        type=Path,
        default=DEFAULT_COMBINED_PATH,
        help="Combined evidence-card CSV from parse_evidence_card_batch_output.py",
    )
    parser.add_argument(
        "--paper-set-csv",
        type=Path,
        default=DEFAULT_SET_PATH,
        help="CSV listing the selected paper ids to use as augmentation sources.",
    )
    parser.add_argument(
        "--models",
        nargs="+",
        default=DEFAULT_MODELS,
        choices=DEFAULT_MODELS,
        help="Prediction models to generate batch files for.",
    )
    parser.add_argument(
        "--modes",
        nargs="+",
        default=DEFAULT_MODES,
        choices=MODE_CHOICES,
        help="Prediction elicitation modes to include.",
    )
    parser.add_argument(
        "--n-explanation-repeats",
        type=int,
        default=1,
        help="Number of repeated runs for explanation-included modes.",
    )
    parser.add_argument(
        "--repeat-start-index",
        type=int,
        default=1,
        help="Starting repeat index to use in custom_id suffixes for repeated runs.",
    )
    parser.add_argument(
        "--seed-base",
        type=int,
        default=None,
        help=(
            "Optional deterministic seed base for repeated explanation runs. "
            "When set, repeat k uses seed (seed_base + k - 1) across all requests."
        ),
    )
    parser.add_argument(
        "--max-papers",
        type=int,
        default=None,
        help="Optional cap on the number of selected papers.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("openAI_batch_input"),
        help="Directory for output JSONL files.",
    )
    parser.add_argument(
        "--output-prefix",
        default="prediction_literature_analysis_report_strict243",
        help="Prefix for output JSONL filenames.",
    )
    parser.add_argument(
        "--memo-root",
        type=Path,
        default=DEFAULT_MEMO_ROOT,
        help="Directory to write rendered analysis reports.",
    )
    parser.add_argument(
        "--metadata-csv",
        type=Path,
        default=DEFAULT_METADATA_CSV,
        help="Metadata CSV that maps markdown custom_id values to citation fields.",
    )
    return parser.parse_args()


def _model_tag(model: str) -> str:
    return MODEL_TAGS[model]


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def normalize_custom_id(value: str) -> str:
    return Path(value).stem


def normalize_title_case(text: str) -> str:
    text = (text or "").strip()
    if not text:
        return ""
    if text == text.upper():
        parts = text.lower().split()
        small = {"a", "an", "and", "as", "at", "by", "for", "from", "in", "of", "on", "or", "the", "to", "with"}
        out: list[str] = []
        for i, part in enumerate(parts):
            if i != 0 and i != len(parts) - 1 and part in small:
                out.append(part)
            else:
                out.append(part.capitalize())
        return " ".join(out)
    return text


def format_initials(text: str) -> str:
    compact = re.sub(r"[^A-Za-z-]", "", text or "")
    if not compact:
        return ""
    parts: list[str] = []
    i = 0
    while i < len(compact):
        ch = compact[i]
        if ch.isalpha():
            if i + 2 < len(compact) and compact[i + 1] == "-" and compact[i + 2].isalpha():
                parts.append(f"{ch}.-{compact[i + 2]}.")
                i += 3
                continue
            parts.append(f"{ch}.")
        i += 1
    return " ".join(parts)


def format_author_token(token: str) -> str:
    token = (token or "").strip()
    if not token:
        return ""
    if "," not in token:
        return token
    last, initials = [part.strip() for part in token.split(",", 1)]
    formatted_initials = format_initials(initials)
    return f"{last}, {formatted_initials}" if formatted_initials else last


def format_author_list(text: str) -> str:
    authors = [format_author_token(part) for part in (text or "").split(";") if part.strip()]
    authors = [author for author in authors if author]
    if not authors:
        return ""
    if len(authors) == 1:
        return authors[0]
    if len(authors) == 2:
        return f"{authors[0]}, & {authors[1]}"
    return ", ".join(authors[:-1]) + f", & {authors[-1]}"


def build_apa_citation(meta: dict[str, str]) -> str:
    authors = format_author_list(meta.get("Authors") or meta.get("Author Full Names") or "")
    year = (meta.get("Publication Year") or "").strip()
    title = (meta.get("Article Title") or "").strip()
    source = normalize_title_case(meta.get("Source Title") or "")
    pieces = []
    if authors:
        pieces.append(authors)
    if year:
        pieces.append(f"({year}).")
    if title:
        pieces.append(f"{title}.")
    if source:
        pieces.append(f"*{source}*.")
    return " ".join(pieces).strip()


def extract_source_fields(meta: dict[str, str]) -> dict[str, str]:
    return {
        "title": (meta.get("Article Title") or "").strip(),
        "authors": format_author_list(meta.get("Authors") or meta.get("Author Full Names") or ""),
        "journal": normalize_title_case(meta.get("Source Title") or ""),
        "year": (meta.get("Publication Year") or "").strip(),
    }


def load_metadata_map(path: Path) -> dict[str, dict[str, str]]:
    metadata_map: dict[str, dict[str, str]] = {}
    for row in load_rows(path):
        custom_id = normalize_custom_id(row.get("custom_id", ""))
        if custom_id:
            metadata_map[custom_id] = row
        doi = normalize_custom_id((row.get("DOI") or "").replace("/", "_"))
        if doi and doi not in metadata_map:
            metadata_map[doi] = row
    metadata_map["PGG_MS_202502"] = {
        "Authors": "Alsobaya, M; Rand, DG; Watts, DJ; Almaatouq, A",
        "Publication Year": "2025",
        "Article Title": "Integrative Experiments Identify How Punishment Impacts Welfare in Public Goods Games",
        "Source Title": "",
    }
    return metadata_map


def split_pipe_list(text: str) -> list[str]:
    text = (text or "").strip()
    if not text:
        return []
    return [part.strip() for part in text.split(" | ") if part.strip()]


def split_limitations(text: str) -> list[str]:
    text = (text or "").strip()
    if not text:
        return []
    return [part.strip() for part in text.split(" | ") if part.strip()]


def build_dimension_bullet(row: dict[str, str], dimension: str) -> str | None:
    tier = row.get(f"dim_{dimension}_evidence_tier", "")
    if tier not in TIER_SENTENCE:
        return None
    notes = row.get(f"dim_{dimension}_notes", "").strip()
    effect = row.get(f"dim_{dimension}_effect_direction", "").strip()
    parts = [f"- {DIMENSION_LABELS[dimension]}: {TIER_SENTENCE[tier]}"]
    if effect not in {"", "N/A", "N/R"}:
        parts.append(f"It suggests punishment is `{effect}` under this dimension.")
    if notes:
        parts.append(notes)
    return " ".join(parts)


def render_memo(row: dict[str, str], metadata: dict[str, str] | None) -> str:
    study_type = (
        f"{row['paper_type_primary']}; "
        f"empirical subtype={row['paper_type_empirical']}; "
        f"experimental subtype={row['paper_type_experimental']}"
    )
    relevance_text = (
        f"PGG or variant={row['relevance_pgg_or_variant']}; "
        f"punishment or sanctions={row['relevance_punishment_or_sanctions']}; "
        f"efficiency or payoff outcome={row['relevance_efficiency_or_related_payoff_outcome']}"
    )
    payoff_outcomes = split_pipe_list(row.get("outcomes_payoff_related_outcomes", ""))
    non_payoff_outcomes = split_pipe_list(row.get("outcomes_non_payoff_outcomes", ""))
    dimension_bullets = [
        bullet
        for dimension in DIMENSION_ORDER
        if (bullet := build_dimension_bullet(row, dimension)) is not None
    ]
    if not dimension_bullets:
        dimension_bullets = ["- None highlighted."]

    limitations = split_limitations(row.get("important_limitations_joined", ""))
    if not limitations:
        limitations = ["None recorded."]

    source_fields = extract_source_fields(metadata or {})

    lines = [
        "# Analysis Report",
        "",
        "## Source",
        f"Title: {source_fields['title']}",
        f"Authors: {source_fields['authors']}",
        f"Journal: {source_fields['journal']}",
        f"Year: {source_fields['year']}",
        "",
        "## Study Type",
        study_type,
        "",
        "## Task Relevance",
        relevance_text,
        "",
        "## Outcomes Measured",
        f"Primary outcome type: {row['outcomes_primary_outcome_type']}",
    ]
    if payoff_outcomes:
        lines.extend(["Payoff-related outcomes:", *[f"- {item}" for item in payoff_outcomes]])
    if non_payoff_outcomes:
        lines.extend(["Non-payoff outcomes:", *[f"- {item}" for item in non_payoff_outcomes]])
    notes = row.get("outcomes_notes", "").strip()
    if notes:
        lines.extend(["Outcome notes:", notes])

    lines.extend(
        [
            "",
            "## Main Findings Relevant To Prediction",
            row["paper_findings"].strip(),
            "",
            "## Prediction Guidance",
            row["decision_support"].strip(),
            "",
            "## Design Dimensions Highlighted In This Paper",
            *dimension_bullets,
            "",
            "## Important Limitations",
            *[f"- {item}" for item in limitations],
        ]
    )
    return "\n".join(lines).strip() + "\n"


def wrap_with_memo(memo_text: str, prompt_text: str) -> str:
    return f"""{MEMO_WRAPPER}
----------Analysis Report Starts----------

{memo_text}

----------Analysis Report Ends----------
{prompt_text}"""


def load_selected_rows(combined_csv: Path, paper_set_csv: Path, max_papers: int | None) -> list[dict[str, str]]:
    selected_ids = [row["custom_id"] for row in load_rows(paper_set_csv)]
    if max_papers is not None:
        selected_ids = selected_ids[:max_papers]
    combined_rows = {row["custom_id"]: row for row in load_rows(combined_csv)}

    missing = [paper_id for paper_id in selected_ids if paper_id not in combined_rows]
    if missing:
        raise KeyError(f"Missing {len(missing)} paper ids in combined CSV, e.g. {missing[:5]}")

    return [combined_rows[paper_id] for paper_id in selected_ids]


def write_memos(
    memo_root: Path,
    set_name: str,
    rows: list[dict[str, str]],
    metadata_map: dict[str, dict[str, str]],
) -> dict[str, str]:
    memo_dir = memo_root / set_name
    memo_dir.mkdir(parents=True, exist_ok=True)
    memo_texts: dict[str, str] = {}
    index_rows: list[dict[str, str]] = []
    for row in rows:
        metadata = metadata_map.get(row["custom_id"])
        memo_text = render_memo(row, metadata)
        memo_path = memo_dir / f"{row['custom_id']}.md"
        memo_path.write_text(memo_text, encoding="utf-8")
        memo_texts[row["custom_id"]] = memo_text
        index_rows.append(
            {
                "custom_id": row["custom_id"],
                "report_path": str(memo_path),
                "paper_type_primary": row["paper_type_primary"],
                "paper_type_empirical": row["paper_type_empirical"],
                "paper_type_experimental": row["paper_type_experimental"],
                "relevance_pgg_or_variant": row["relevance_pgg_or_variant"],
                "relevance_punishment_or_sanctions": row["relevance_punishment_or_sanctions"],
                "relevance_efficiency_or_related_payoff_outcome": row[
                    "relevance_efficiency_or_related_payoff_outcome"
                ],
                "outcomes_primary_outcome_type": row["outcomes_primary_outcome_type"],
            }
        )
    index_path = memo_dir / "report_index.csv"
    with index_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(index_rows[0].keys()))
        writer.writeheader()
        writer.writerows(index_rows)
    return memo_texts


def build_requests(
    *,
    df: pd.DataFrame,
    memo_texts: dict[str, str],
    model: str,
    modes: list[str],
    n_explanation_repeats: int,
    repeat_start_index: int,
    seed_base: int | None,
) -> list[dict]:
    requests: list[dict] = []
    include_single = "single" in modes
    include_reasoning = "reasoning" in modes
    include_joint = "joint" in modes
    include_joint_reasoning = "joint_reasoning" in modes

    for paper_id, memo_text in memo_texts.items():
        if include_single:
            for i, (_, row) in enumerate(df.iterrows(), start=1):
                requests.append(
                    build_openai_request(
                        custom_id=f"paper_analysis_report/{paper_id}/Q{i}",
                        model=model,
                        system_prompt=SYSTEM_PROMPT_SINGLE,
                        user_prompt=wrap_with_memo(
                            memo_text,
                            build_single_prompt(row, include_explanation=False),
                        ),
                        include_logprobs=True,
                        response_format_json=False,
                        include_explanation=False,
                    )
                )

        if include_reasoning:
            for i, (_, row) in enumerate(df.iterrows(), start=1):
                for rep_idx in range(repeat_start_index, repeat_start_index + n_explanation_repeats):
                    suffix = "" if n_explanation_repeats == 1 else f"_rep{rep_idx}"
                    seed = None if seed_base is None else seed_base + rep_idx - 1
                    requests.append(
                        build_openai_request(
                            custom_id=f"paper_analysis_report{suffix}/{paper_id}/Q{i}",
                            model=model,
                            system_prompt=SYSTEM_PROMPT_SINGLE_EXPLANATION,
                            user_prompt=wrap_with_memo(
                                memo_text,
                                build_single_prompt(row, include_explanation=True),
                            ),
                            include_logprobs=False,
                            response_format_json=True,
                            include_explanation=True,
                            seed=seed,
                        )
                    )

        if include_joint:
            requests.append(
                build_openai_request(
                    custom_id=f"paper_analysis_report_joint/{paper_id}",
                    model=model,
                    system_prompt=build_joint_system_prompt(include_explanation=False),
                    user_prompt=wrap_with_memo(
                        memo_text,
                        build_joint_prompt(df, include_explanation=False),
                    ),
                    include_logprobs=False,
                    response_format_json=True,
                    include_explanation=False,
                )
            )

        if include_joint_reasoning:
            for rep_idx in range(repeat_start_index, repeat_start_index + n_explanation_repeats):
                suffix = "" if n_explanation_repeats == 1 else f"_rep{rep_idx}"
                seed = None if seed_base is None else seed_base + rep_idx - 1
                requests.append(
                    build_openai_request(
                        custom_id=f"paper_analysis_report_joint{suffix}/{paper_id}",
                        model=model,
                        system_prompt=build_joint_system_prompt(include_explanation=True),
                        user_prompt=wrap_with_memo(
                            memo_text,
                            build_joint_prompt(df, include_explanation=True),
                        ),
                        include_logprobs=False,
                        response_format_json=True,
                        include_explanation=True,
                        seed=seed,
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
    set_name = args.paper_set_csv.stem
    selected_rows = load_selected_rows(args.combined_csv, args.paper_set_csv, args.max_papers)
    metadata_map = load_metadata_map(args.metadata_csv)
    memo_texts = write_memos(args.memo_root, set_name, selected_rows, metadata_map)

    for model in args.models:
        requests = build_requests(
            df=df,
            memo_texts=memo_texts,
            model=model,
            modes=args.modes,
            n_explanation_repeats=args.n_explanation_repeats,
            repeat_start_index=args.repeat_start_index,
            seed_base=args.seed_base,
        )
        output_path = args.output_dir / f"{args.output_prefix}_{_model_tag(model)}.jsonl"
        count = write_jsonl(output_path, requests)
        print(f"Wrote {count} requests to {output_path}")


if __name__ == "__main__":
    main()
