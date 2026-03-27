from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from batch_inputs.literature_filters import (  # noqa: E402
    chunk_items,
    extract_openai_batch_output_text,
    write_jsonl,
)
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
DEFAULT_COLLECTIONS_PER_FILE = 50


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build chunked OpenAI prediction batch JSONLs from collection-level "
            "literature reports, carrying forward the selected paper-only narrative/"
            "decision report styles and elicitation modes."
        )
    )
    parser.add_argument(
        "--df-pgg",
        type=Path,
        default=Path("input/pgg_CONFIGmerged_validation.csv"),
        help="Target validation configurations to predict.",
    )
    parser.add_argument(
        "--narrative-reports",
        type=Path,
        required=True,
        help="Batch output JSONL containing collection-level narrative reports.",
    )
    parser.add_argument(
        "--decision-reports",
        type=Path,
        required=True,
        help="Batch output JSONL containing collection-level decision-support reports.",
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
    parser.add_argument(
        "--collections-per-file",
        type=int,
        default=DEFAULT_COLLECTIONS_PER_FILE,
        help="Maximum number of collection filters to include per output JSONL.",
    )
    parser.add_argument(
        "--max-collections",
        type=int,
        default=None,
        help="Optional cap on the number of report collections to include.",
    )
    parser.add_argument(
        "--allow-missing-reports",
        action="store_true",
        help="Skip collections missing from any requested report file instead of failing.",
    )
    return parser.parse_args()


def _model_tag(model: str) -> str:
    return MODEL_TAGS[model]


def _variant_collection_id(variant_name: str, collection_label: str) -> str:
    return f"{variant_name}::{collection_label}"


def load_report_map(path: Path) -> dict[str, str]:
    report_map: dict[str, str] = {}
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            item = json.loads(line)
            custom_id = str(item.get("custom_id", "")).strip()
            if not custom_id:
                continue
            text = extract_openai_batch_output_text(item)
            if not text:
                continue
            report_map[custom_id] = text
    if not report_map:
        raise ValueError(f"No report texts were recovered from {path}")
    return report_map


def ordered_collection_labels(report_map: dict[str, str]) -> list[str]:
    return list(report_map.keys())


def resolve_collection_labels(
    *,
    variants: list[str],
    report_maps: dict[str, dict[str, str]],
    max_collections: int | None,
    allow_missing_reports: bool,
) -> list[str]:
    ordered = ordered_collection_labels(report_maps[variants[0]])
    resolved: list[str] = []
    for label in ordered:
        if all(label in report_maps[variant] for variant in variants):
            resolved.append(label)
            continue
        if not allow_missing_reports:
            missing = [variant for variant in variants if label not in report_maps[variant]]
            raise KeyError(f"Missing report(s) for collection '{label}': {missing}")
    if max_collections is not None:
        resolved = resolved[: max(0, max_collections)]
    return resolved


def build_requests_for_labels(
    *,
    df: pd.DataFrame,
    collection_labels: list[str],
    report_maps: dict[str, dict[str, str]],
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

    for collection_label in collection_labels:
        for variant_name in variants:
            report_text = report_maps[variant_name][collection_label]
            variant_collection_id = _variant_collection_id(variant_name, collection_label)

            if include_single:
                for i, (_, row) in enumerate(df.iterrows(), start=1):
                    requests.append(
                        build_openai_request(
                            custom_id=f"{variant_collection_id}/Q{i}",
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
                                custom_id=f"{variant_collection_id}_explanation_rep{rep_idx}/Q{i}",
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
                        custom_id=f"{variant_collection_id}_joint",
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
                            custom_id=f"{variant_collection_id}_joint_explanation_rep{rep_idx}",
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


def output_path_for_model(
    *,
    output_dir: Path,
    output_prefix: str,
    model: str,
    part_idx: int,
    n_parts: int,
) -> Path:
    stem = f"{output_prefix}_{_model_tag(model)}"
    if n_parts > 1:
        stem = f"{stem}_part{part_idx:02d}"
    return output_dir / f"{stem}.jsonl"


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.df_pgg).sort_values("CONFIG_configId").reset_index(drop=True)
    report_maps = {
        "paper_only_narrative": load_report_map(args.narrative_reports),
        "paper_only_decision": load_report_map(args.decision_reports),
    }
    collection_labels = resolve_collection_labels(
        variants=args.variants,
        report_maps=report_maps,
        max_collections=args.max_collections,
        allow_missing_reports=args.allow_missing_reports,
    )
    label_batches = chunk_items(collection_labels, args.collections_per_file)

    for model in args.models:
        for part_idx, label_batch in enumerate(label_batches, start=1):
            requests = build_requests_for_labels(
                df=df,
                collection_labels=label_batch,
                report_maps=report_maps,
                model=model,
                variants=args.variants,
                modes=args.modes,
                n_explanation_repeats=args.n_explanation_repeats,
            )
            output_path = output_path_for_model(
                output_dir=args.output_dir,
                output_prefix=args.output_prefix,
                model=model,
                part_idx=part_idx,
                n_parts=len(label_batches),
            )
            count = write_jsonl(output_path, requests)
            print(f"Wrote {count} requests to {output_path}")


if __name__ == "__main__":
    main()

