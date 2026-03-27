from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from batch_inputs.paper_only_variants import (  # noqa: E402
    DEFAULT_MODELS,
    DEFAULT_VARIANTS,
    MODEL_TAGS,
    N_EXPLANATION_REPEATS,
    SYSTEM_PROMPT_SINGLE,
    SYSTEM_PROMPT_SINGLE_EXPLANATION,
    build_joint_prompt,
    build_joint_system_prompt,
    build_openai_request,
    build_single_prompt,
    wrap_with_report,
)

MODE_CHOICES = ["single", "reasoning", "joint", "joint_reasoning"]
DEFAULT_MODES = ["reasoning", "joint_reasoning"]
DEFAULT_REPORT_PATHS = {
    "paper_only_narrative": Path("literature/output/paper_only_narrative/agentic_report.md"),
    "paper_only_decision": Path("literature/output/paper_only_decision/agentic_report.md"),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build model-specific OpenAI batch JSONLs from the literature narrative "
            "and decision-support report markdown files."
        )
    )
    parser.add_argument(
        "--df-pgg",
        type=Path,
        default=Path("input/pgg_CONFIGmerged_validation.csv"),
        help="Target validation configurations to predict.",
    )
    parser.add_argument(
        "--narrative-report",
        type=Path,
        default=DEFAULT_REPORT_PATHS["paper_only_narrative"],
        help="Markdown report for the narrative literature synthesis.",
    )
    parser.add_argument(
        "--decision-report",
        type=Path,
        default=DEFAULT_REPORT_PATHS["paper_only_decision"],
        help="Markdown report for the decision-support literature synthesis.",
    )
    parser.add_argument(
        "--models",
        nargs="+",
        default=DEFAULT_MODELS,
        choices=DEFAULT_MODELS,
        help="Prediction models to generate batch files for.",
    )
    parser.add_argument(
        "--variants",
        nargs="+",
        default=DEFAULT_VARIANTS,
        choices=DEFAULT_VARIANTS,
        help="Report variants to include.",
    )
    parser.add_argument(
        "--modes",
        nargs="+",
        default=DEFAULT_MODES,
        choices=MODE_CHOICES,
        help="Elicitation modes to include.",
    )
    parser.add_argument(
        "--n-explanation-repeats",
        type=int,
        default=N_EXPLANATION_REPEATS,
        help="Number of repeated runs for explanation-included modes.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("openAI_batch_input"),
        help="Directory for output JSONL files.",
    )
    parser.add_argument(
        "--output-prefix",
        default="prediction_literature_narrative-decision",
        help="Prefix for output JSONL filenames.",
    )
    return parser.parse_args()


def _model_tag(model: str) -> str:
    return MODEL_TAGS[model]


def load_report_texts(args: argparse.Namespace) -> dict[str, str]:
    report_paths = {
        "paper_only_narrative": args.narrative_report,
        "paper_only_decision": args.decision_report,
    }
    report_texts: dict[str, str] = {}
    for variant_name, path in report_paths.items():
        if variant_name not in args.variants:
            continue
        if not path.exists():
            raise FileNotFoundError(f"Report not found for {variant_name}: {path}")
        report_texts[variant_name] = path.read_text(encoding="utf-8")
    return report_texts


def build_requests(
    *,
    df: pd.DataFrame,
    report_texts: dict[str, str],
    model: str,
    variants: list[str],
    modes: list[str],
    n_explanation_repeats: int,
) -> list[dict]:
    requests: list[dict] = []
    include_single = "single" in modes
    include_reasoning = "reasoning" in modes
    include_joint = "joint" in modes
    include_joint_reasoning = "joint_reasoning" in modes

    for variant_name in variants:
        report_text = report_texts[variant_name]

        if include_single:
            for i, (_, row) in enumerate(df.iterrows(), start=1):
                requests.append(
                    build_openai_request(
                        custom_id=f"{variant_name}/Q{i}",
                        model=model,
                        system_prompt=SYSTEM_PROMPT_SINGLE,
                        user_prompt=wrap_with_report(
                            report_text,
                            build_single_prompt(row, include_explanation=False),
                        ),
                        include_logprobs=True,
                        response_format_json=False,
                        include_explanation=False,
                    )
                )

        if include_reasoning:
            for i, (_, row) in enumerate(df.iterrows(), start=1):
                for rep_idx in range(1, n_explanation_repeats + 1):
                    requests.append(
                        build_openai_request(
                            custom_id=f"{variant_name}_explanation_rep{rep_idx}/Q{i}",
                            model=model,
                            system_prompt=SYSTEM_PROMPT_SINGLE_EXPLANATION,
                            user_prompt=wrap_with_report(
                                report_text,
                                build_single_prompt(row, include_explanation=True),
                            ),
                            include_logprobs=False,
                            response_format_json=True,
                            include_explanation=True,
                        )
                    )

        if include_joint:
            requests.append(
                build_openai_request(
                    custom_id=f"{variant_name}_joint",
                    model=model,
                    system_prompt=build_joint_system_prompt(include_explanation=False),
                    user_prompt=wrap_with_report(
                        report_text,
                        build_joint_prompt(df, include_explanation=False),
                    ),
                    include_logprobs=False,
                    response_format_json=True,
                    include_explanation=False,
                )
            )

        if include_joint_reasoning:
            for rep_idx in range(1, n_explanation_repeats + 1):
                requests.append(
                    build_openai_request(
                        custom_id=f"{variant_name}_joint_explanation_rep{rep_idx}",
                        model=model,
                        system_prompt=build_joint_system_prompt(include_explanation=True),
                        user_prompt=wrap_with_report(
                            report_text,
                            build_joint_prompt(df, include_explanation=True),
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
    report_texts = load_report_texts(args)

    for model in args.models:
        requests = build_requests(
            df=df,
            report_texts=report_texts,
            model=model,
            variants=args.variants,
            modes=args.modes,
            n_explanation_repeats=args.n_explanation_repeats,
        )
        output_path = args.output_dir / f"{args.output_prefix}_{_model_tag(model)}.jsonl"
        count = write_jsonl(output_path, requests)
        print(f"Wrote {count} requests to {output_path}")


if __name__ == "__main__":
    main()
