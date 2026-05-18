from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from prediction_inputs.paper_only_variants import (  # noqa: E402
    MODEL_TAGS,
    build_joint_prompt,
    build_joint_system_prompt,
    build_openai_request,
)


DEFAULT_MODELS = ["gpt-5.1", "gpt-5-mini", "gpt-5-nano"]
DEFAULT_COLLECTION_INDEX = Path(
    "literature/output/collection_analysis_reports/switch_sets_stage1/report_index.csv"
)
DEFAULT_BENCHMARK_REPORT = Path(
    "literature/output/paper_analysis_reports/strict_predictive_empirical_payoff/PGG_MS_202502.md"
)

SINGLE_PAPER_WRAPPER = """Below is an analysis report distilled from one academic paper.
Use it as contextual evidence about how design features may change the efficiency impact of punishment.
Respect the report's stated limitations and do not infer beyond what the report supports."""

COLLECTION_REPORT_WRAPPER = """Below is an analysis report synthesized from multiple academic papers.
Use it as contextual evidence about how design features may change the efficiency impact of punishment.
Respect the report's stated limitations and do not infer beyond what the report supports."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build one joint-with-explanation literature suite batch JSONL per model, "
            "covering 5 repetitions each of: baseline, benchmark paper, and the 9 "
            "stage-1 collection reports."
        )
    )
    parser.add_argument(
        "--df-pgg",
        type=Path,
        default=Path("input/pgg_CONFIGmerged_validation.csv"),
        help="Validation configurations to predict.",
    )
    parser.add_argument(
        "--collection-index-csv",
        type=Path,
        default=DEFAULT_COLLECTION_INDEX,
        help="Report index CSV for the 9 stage-1 collection analysis reports.",
    )
    parser.add_argument(
        "--benchmark-report",
        type=Path,
        default=DEFAULT_BENCHMARK_REPORT,
        help="Rendered single-paper benchmark report for PGG_MS_202502.",
    )
    parser.add_argument(
        "--models",
        nargs="+",
        default=DEFAULT_MODELS,
        help="Model names to generate batch files for.",
    )
    parser.add_argument(
        "--n-repeats",
        type=int,
        default=5,
        help="Number of repeated calls per augmentation condition.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("openAI_batch_input"),
        help="Directory for output JSONL files.",
    )
    parser.add_argument(
        "--output-prefix",
        default="prediction_literature_joint_suite_reps1to5",
        help="Prefix for output JSONL filenames.",
    )
    return parser.parse_args()


def _model_tag(model: str) -> str:
    return MODEL_TAGS.get(model, "".join(ch for ch in model.lower() if ch.isalnum()))


def _load_collection_reports(index_csv: Path) -> list[dict[str, str]]:
    with index_csv.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    reports: list[dict[str, str]] = []
    for row in rows:
        variant_id = str(row.get("variant_id", "")).strip()
        report_path = Path(str(row.get("report_path", "")).strip())
        if not variant_id or not report_path:
            continue
        reports.append(
            {
                "variant_id": variant_id,
                "report_path": str(report_path),
                "variant_kind": str(row.get("variant_kind", "")).strip(),
            }
        )
    return sorted(reports, key=lambda item: item["variant_id"])


def _wrap_report(wrapper: str, report_text: str, prompt_text: str) -> str:
    return (
        f"{wrapper}\n"
        "----------Analysis Report Starts----------\n\n"
        f"{report_text.strip()}\n\n"
        "----------Analysis Report Ends----------\n"
        f"{prompt_text}"
    )


def _baseline_request(df: pd.DataFrame, model: str, rep_idx: int) -> dict:
    return build_openai_request(
        custom_id=f"baseline_joint_reasoning_rep{rep_idx}",
        model=model,
        system_prompt=build_joint_system_prompt(include_explanation=True),
        user_prompt=build_joint_prompt(df, include_explanation=True),
        include_logprobs=False,
        response_format_json=True,
        include_explanation=True,
    )


def _benchmark_request(df: pd.DataFrame, model: str, rep_idx: int, report_text: str) -> dict:
    return build_openai_request(
        custom_id=f"paper_analysis_report_joint_rep{rep_idx}/PGG_MS_202502",
        model=model,
        system_prompt=build_joint_system_prompt(include_explanation=True),
        user_prompt=_wrap_report(
            SINGLE_PAPER_WRAPPER,
            report_text,
            build_joint_prompt(df, include_explanation=True),
        ),
        include_logprobs=False,
        response_format_json=True,
        include_explanation=True,
    )


def _collection_request(
    df: pd.DataFrame,
    model: str,
    rep_idx: int,
    variant_id: str,
    report_text: str,
) -> dict:
    return build_openai_request(
        custom_id=f"collection_analysis_report_joint_rep{rep_idx}/{variant_id}",
        model=model,
        system_prompt=build_joint_system_prompt(include_explanation=True),
        user_prompt=_wrap_report(
            COLLECTION_REPORT_WRAPPER,
            report_text,
            build_joint_prompt(df, include_explanation=True),
        ),
        include_logprobs=False,
        response_format_json=True,
        include_explanation=True,
    )


def _build_requests(
    *,
    df: pd.DataFrame,
    model: str,
    n_repeats: int,
    benchmark_report_text: str,
    collection_reports: list[tuple[str, str]],
) -> list[dict]:
    requests: list[dict] = []
    for rep_idx in range(1, n_repeats + 1):
        requests.append(_baseline_request(df, model, rep_idx))
        requests.append(_benchmark_request(df, model, rep_idx, benchmark_report_text))
        for variant_id, report_text in collection_reports:
            requests.append(_collection_request(df, model, rep_idx, variant_id, report_text))
    return requests


def _write_jsonl(path: Path, records: list[dict]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    return len(records)


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.df_pgg).sort_values("CONFIG_configId").reset_index(drop=True)

    benchmark_report_text = args.benchmark_report.read_text(encoding="utf-8")
    collection_entries = _load_collection_reports(args.collection_index_csv)
    collection_reports = [
        (entry["variant_id"], Path(entry["report_path"]).read_text(encoding="utf-8"))
        for entry in collection_entries
    ]

    for model in args.models:
        requests = _build_requests(
            df=df,
            model=model,
            n_repeats=args.n_repeats,
            benchmark_report_text=benchmark_report_text,
            collection_reports=collection_reports,
        )
        output_path = args.output_dir / f"{args.output_prefix}_{_model_tag(model)}.jsonl"
        count = _write_jsonl(output_path, requests)
        print(f"Wrote {count} requests to {output_path}")


if __name__ == "__main__":
    main()
