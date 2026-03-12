from __future__ import annotations

import argparse
from pathlib import Path

from agentic_report.config import ANALYSIS_MODEL, BASE_OUTPUT_DIR, REPORT_MODEL, SUMMARY_MODEL
from agentic_report.pipeline import (
    REPORT_METHOD_SPECS,
    canonical_output_dir_name,
    parse_report_method,
    run_pipeline,
)


def _report_output_path(report_method: str) -> Path:
    spec = parse_report_method(report_method)
    dir_name = canonical_output_dir_name(
        source_mode=spec["source_mode"],
        report_style=spec["report_style"],
    )
    return BASE_OUTPUT_DIR / dir_name / "agentic_report.md"


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate positive-case report variations with the OpenAI Responses API."
    )
    parser.add_argument(
        "--methods",
        nargs="+",
        default=list(REPORT_METHOD_SPECS.keys()),
        choices=sorted(REPORT_METHOD_SPECS),
        help="Report methods to generate.",
    )
    parser.add_argument(
        "--report-model",
        default=REPORT_MODEL,
        help="Model used for final report synthesis.",
    )
    parser.add_argument(
        "--analysis-model",
        default=None,
        help="Override analysis model; defaults to config.",
    )
    parser.add_argument(
        "--summary-model",
        default=None,
        help="Override summary model; defaults to config.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Regenerate reports even if the target report file already exists.",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()

    for report_method in args.methods:
        report_path = _report_output_path(report_method)
        if report_path.exists() and not args.force:
            print(f"Skipping existing report: {report_path}")
            continue

        outputs = run_pipeline(
            report_model=args.report_model,
            analysis_model=args.analysis_model or ANALYSIS_MODEL,
            summary_model=args.summary_model or SUMMARY_MODEL,
            reuse_memos=True,
            report_method=report_method,
        )
        print(f"Generated {report_method}: {outputs['report']}")


if __name__ == "__main__":
    main()
