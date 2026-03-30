from __future__ import annotations

import argparse
import os
from pathlib import Path

try:
    from batch_processing.agentic_workflow import make_openai_client
    from batch_processing.build_batch_input import SYSTEM_PROMPT, build_user_prompt as build_simple_user_prompt
    from batch_processing.extraction_logging import (
        DEFAULT_AGENT_OUTPUT_TOKENS,
        DEFAULT_CRITIC_OUTPUT_TOKENS,
        DEFAULT_PRICE_INPUT_PER_1M,
        DEFAULT_PRICE_OUTPUT_PER_1M,
        DEFAULT_SIMPLE_OUTPUT_TOKENS,
        LiveCostTracker,
    )
    from batch_processing.extraction_pipeline import (
        DEFAULT_HYBRID_AGENTIC_FIELDS,
        run_hybrid_extraction_for_paper,
        simple_fields,
        write_hybrid_workbook,
    )
except ImportError:  # pragma: no cover - allows direct script execution
    from agentic_workflow import make_openai_client  # type: ignore
    from build_batch_input import SYSTEM_PROMPT, build_user_prompt as build_simple_user_prompt  # type: ignore
    from extraction_logging import (  # type: ignore
        DEFAULT_AGENT_OUTPUT_TOKENS,
        DEFAULT_CRITIC_OUTPUT_TOKENS,
        DEFAULT_PRICE_INPUT_PER_1M,
        DEFAULT_PRICE_OUTPUT_PER_1M,
        DEFAULT_SIMPLE_OUTPUT_TOKENS,
        LiveCostTracker,
    )
    from extraction_pipeline import (  # type: ignore
        DEFAULT_HYBRID_AGENTIC_FIELDS,
        run_hybrid_extraction_for_paper,
        simple_fields,
        write_hybrid_workbook,
    )


DEFAULT_PAPER_IDS = [
    "10.1007_s10645-008-9094-1",
    "10.1177_0146167216684134",
    "10.1016_j.jpubeco.2015.12.012",
    "10.1007_s10640-025-00970-6",
    "10.3390_g14050065",
    "10.1111_apce.12343",
    "10.1016_j.evolhumbehav.2006.06.001",
]

RAW_PAPER_MARKDOWN_DIR_ENV_VAR = "RAW_PAPER_MARKDOWN_DIR"
DERIVED_MARKDOWN_DIR_NAMES = frozenset({"paper_analysis_reports", "paper_card_memos"})


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run hybrid paper extraction with agentic overrides for selected fields."
    )
    parser.add_argument(
        "--paper-ids",
        nargs="+",
        default=DEFAULT_PAPER_IDS,
        help="Paper IDs / markdown basenames to process.",
    )
    parser.add_argument(
        "--paper-dir",
        default=os.getenv(RAW_PAPER_MARKDOWN_DIR_ENV_VAR),
        help=(
            "Directory containing raw paper markdown files. "
            f"Required unless `{RAW_PAPER_MARKDOWN_DIR_ENV_VAR}` is set. "
            "Derived summary directories are rejected."
        ),
    )
    parser.add_argument(
        "--model",
        default="gpt-4.1",
        help="Model name for both simple and agentic extraction.",
    )
    parser.add_argument(
        "--output-xlsx",
        default="batch_processing/output_xlsx/agentic_extraction_7papers.xlsx",
        help="Path to the output workbook.",
    )
    parser.add_argument(
        "--max-critic-rounds",
        type=int,
        default=1,
        help="Maximum critic rounds for agentic fields.",
    )
    parser.add_argument(
        "--price-input-per-1m",
        type=float,
        default=DEFAULT_PRICE_INPUT_PER_1M,
        help="Estimated input token price in USD per 1M tokens.",
    )
    parser.add_argument(
        "--price-output-per-1m",
        type=float,
        default=DEFAULT_PRICE_OUTPUT_PER_1M,
        help="Estimated output token price in USD per 1M tokens.",
    )
    parser.add_argument(
        "--simple-output-tokens",
        type=int,
        default=DEFAULT_SIMPLE_OUTPUT_TOKENS,
        help="Estimated output tokens for the simple extraction call.",
    )
    parser.add_argument(
        "--agent-output-tokens",
        type=int,
        default=DEFAULT_AGENT_OUTPUT_TOKENS,
        help="Estimated output tokens for extractor/revision/repair agent steps.",
    )
    parser.add_argument(
        "--critic-output-tokens",
        type=int,
        default=DEFAULT_CRITIC_OUTPUT_TOKENS,
        help="Estimated output tokens for critic steps.",
    )
    return parser.parse_args()


def is_derived_markdown_dir(path: Path) -> bool:
    return any(part.lower() in DERIVED_MARKDOWN_DIR_NAMES for part in path.parts)


def resolve_paper_dir(paper_dir_arg: str | None) -> Path:
    if not paper_dir_arg:
        raise ValueError(
            "Raw paper markdown directory is required. Pass --paper-dir or set "
            f"{RAW_PAPER_MARKDOWN_DIR_ENV_VAR}."
        )

    paper_dir = Path(paper_dir_arg)
    if not paper_dir.exists():
        raise FileNotFoundError(f"Paper markdown directory not found: {paper_dir}")
    if not paper_dir.is_dir():
        raise NotADirectoryError(f"Paper markdown path is not a directory: {paper_dir}")
    if is_derived_markdown_dir(paper_dir):
        raise ValueError(
            "Refusing to run hybrid extraction on derived markdown. Point --paper-dir "
            "at raw paper markdown, not `paper_analysis_reports` or `paper_card_memos`."
        )
    return paper_dir


def main() -> None:
    args = parse_args()
    if not os.getenv("OPENAI_API_KEY"):
        raise EnvironmentError("OPENAI_API_KEY is not set.")

    client = make_openai_client()
    agentic_fields = DEFAULT_HYBRID_AGENTIC_FIELDS
    tracker = LiveCostTracker(
        model=args.model,
        price_input_per_1m=args.price_input_per_1m,
        price_output_per_1m=args.price_output_per_1m,
        simple_output_tokens=args.simple_output_tokens,
        agent_output_tokens=args.agent_output_tokens,
        critic_output_tokens=args.critic_output_tokens,
    )

    extraction_rows = []
    metadata_rows = []
    paper_dir = resolve_paper_dir(args.paper_dir)
    simple_field_set = simple_fields(agentic_fields)

    for paper_id in args.paper_ids:
        paper_path = paper_dir / f"{paper_id}.md"
        if not paper_path.exists():
            raise FileNotFoundError(f"Paper markdown not found: {paper_path}")

        tracker.start_paper(
            paper_id,
            simple_fields=simple_field_set,
            agentic_fields=agentic_fields,
        )
        paper_text = paper_path.read_text(encoding="utf-8")
        tracker.log_simple_request(
            paper_id=paper_id,
            system_prompt=SYSTEM_PROMPT,
            user_prompt=build_simple_user_prompt(paper_text),
        )
        result = run_hybrid_extraction_for_paper(
            client=client,
            model=args.model,
            paper_id=paper_id,
            paper_path=str(paper_path),
            agentic_fields=agentic_fields,
            max_critic_rounds=args.max_critic_rounds,
            progress_callback=tracker.callback,
        )
        extraction_rows.extend(result.rows)
        metadata_rows.extend(result.metadata_rows)

    output_path = write_hybrid_workbook(
        output_path=args.output_xlsx,
        extraction_rows=extraction_rows,
        metadata_rows=metadata_rows,
    )
    print(output_path)
