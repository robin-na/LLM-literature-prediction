from __future__ import annotations

import argparse
from pathlib import Path

from agentic_report.column_defs import (
    format_column_definitions,
    format_prediction_task_column_definitions,
)
from agentic_report.pipeline import REPORT_METHOD_SPECS, parse_report_method
from agentic_report.prompts import (
    build_final_report_prompt,
    build_paper_retrieval_report_prompt,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PREVIEW_DIR = PROJECT_ROOT / "positive_cases" / "prompt_previews"


def _preview_path(method: str) -> Path:
    return PREVIEW_DIR / f"{method}.md"


def build_prompt_preview(report_method: str) -> str:
    spec = parse_report_method(report_method)
    generation_mode = spec.get("generation_mode", "memo_then_report")

    if generation_mode == "paper_search_direct":
        prompt = build_paper_retrieval_report_prompt(
            column_defs=format_prediction_task_column_definitions(),
            report_style=spec["report_style"],
        )
    else:
        prompt = build_final_report_prompt(
            column_defs=format_column_definitions(),
            analysis_memo="(analysis memo placeholder for prompt preview)",
            paper_memo="(paper memo placeholder for prompt preview)",
            source_mode=spec["source_mode"],
            report_style=spec["report_style"],
        )

    return "# Prompt Preview\n\n```text\n" + prompt.strip() + "\n```\n"


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export prompt preview markdown files for report methods."
    )
    parser.add_argument(
        "--methods",
        nargs="+",
        default=["paper_only_narrative", "paper_only_decision"],
        choices=sorted(REPORT_METHOD_SPECS),
        help="Report methods to preview.",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    for method in args.methods:
        preview_path = _preview_path(method)
        preview_path.write_text(build_prompt_preview(method), encoding="utf-8")
        print(preview_path)


if __name__ == "__main__":
    main()
