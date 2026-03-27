from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from agentic_report.config import (  # noqa: E402
    ANALYSIS_MODEL,
    DEFAULT_LITERATURE_VECTOR_STORE_ID,
    LITERATURE_CACHE_DIR,
    LITERATURE_OUTPUT_DIR,
    REPORT_MODEL,
    SUMMARY_MODEL,
)
from agentic_report.pipeline import (  # noqa: E402
    canonical_output_dir_name,
    parse_report_method,
    run_pipeline,
)

LITERATURE_METHODS = [
    "paper_only_narrative",
    "paper_only_decision",
]


def _report_output_path(report_method: str, output_root: Path) -> Path:
    spec = parse_report_method(report_method)
    dir_name = canonical_output_dir_name(
        source_mode=spec["source_mode"],
        report_style=spec["report_style"],
    )
    return output_root / dir_name / "agentic_report.md"


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Generate literature reports. By default this runs both the narrative "
            "and decision-support report styles in one command."
        )
    )
    parser.add_argument(
        "--methods",
        nargs="+",
        default=LITERATURE_METHODS,
        choices=LITERATURE_METHODS,
        help="Literature report methods to generate.",
    )
    parser.add_argument(
        "--report-method",
        default=None,
        choices=LITERATURE_METHODS,
        help="Optional single-method shortcut. Overrides --methods.",
    )
    parser.add_argument(
        "--report-model",
        default=REPORT_MODEL,
        help="Model used for final report synthesis.",
    )
    parser.add_argument(
        "--analysis-model",
        default=ANALYSIS_MODEL,
        help="Included for interface consistency; unused by the direct literature methods.",
    )
    parser.add_argument(
        "--summary-model",
        default=SUMMARY_MODEL,
        help="Included for interface consistency; unused by the direct literature methods.",
    )
    parser.add_argument(
        "--vector-store-id",
        default=DEFAULT_LITERATURE_VECTOR_STORE_ID,
        help="Existing vector store id containing the literature PDFs.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=LITERATURE_OUTPUT_DIR,
        help="Root directory for literature outputs.",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=LITERATURE_CACHE_DIR,
        help="Directory for cached OpenAI file/vector-store ids.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Regenerate reports even if the target report file already exists.",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    methods = [args.report_method] if args.report_method else list(args.methods)

    for report_method in methods:
        report_path = _report_output_path(report_method, args.output_root)
        if report_path.exists() and not args.force:
            print(f"Skipping existing report: {report_path}")
            continue

        outputs = run_pipeline(
            analysis_model=args.analysis_model,
            summary_model=args.summary_model,
            report_model=args.report_model,
            reuse_memos=True,
            report_method=report_method,
            vector_store_id=args.vector_store_id,
            output_root=args.output_root,
            cache_dir=args.cache_dir,
        )
        print(f"Generated {report_method}: {outputs['report']}")


if __name__ == "__main__":
    main()
