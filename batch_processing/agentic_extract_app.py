from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    from batch_processing.agentic_workflow import (
        make_openai_client,
        run_agentic_field_extraction,
        supported_fields,
    )
    from batch_processing.extraction_logging import (
        DEFAULT_AGENT_OUTPUT_TOKENS,
        DEFAULT_CRITIC_OUTPUT_TOKENS,
        DEFAULT_PRICE_INPUT_PER_1M,
        DEFAULT_PRICE_OUTPUT_PER_1M,
        LiveCostTracker,
    )
    from batch_processing.extraction_pipeline import resolve_paper_text
except ImportError:  # pragma: no cover - allows direct script execution
    from agentic_workflow import make_openai_client, run_agentic_field_extraction, supported_fields  # type: ignore
    from extraction_logging import (  # type: ignore
        DEFAULT_AGENT_OUTPUT_TOKENS,
        DEFAULT_CRITIC_OUTPUT_TOKENS,
        DEFAULT_PRICE_INPUT_PER_1M,
        DEFAULT_PRICE_OUTPUT_PER_1M,
        LiveCostTracker,
    )
    from extraction_pipeline import resolve_paper_text  # type: ignore


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run agentic field extraction for a single paper and field."
    )
    parser.add_argument(
        "--field",
        required=True,
        choices=supported_fields(),
        help="Field to extract.",
    )
    parser.add_argument(
        "--paper-path",
        help="Path to a paper text or markdown file.",
    )
    parser.add_argument(
        "--paper-text",
        help="Paper text inline. Use this or --paper-path.",
    )
    parser.add_argument(
        "--model",
        default="gpt-4.1",
        help="OpenAI chat model name.",
    )
    parser.add_argument(
        "--max-critic-rounds",
        type=int,
        default=1,
        help="Maximum number of skeptical review rounds.",
    )
    parser.add_argument(
        "--max-tool-rounds",
        type=int,
        default=8,
        help="Maximum number of tool-calling turns per agent step.",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.0,
        help="Sampling temperature.",
    )
    parser.add_argument(
        "--output",
        help="Optional path to write the full workflow JSON payload.",
    )
    parser.add_argument(
        "--final-only",
        action="store_true",
        help="Print only the final extraction JSON instead of the full workflow payload.",
    )
    parser.add_argument(
        "--show-cost-estimate",
        action="store_true",
        help="Print estimated token usage and cost before each API call.",
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
        "--agent-output-tokens",
        type=int,
        default=DEFAULT_AGENT_OUTPUT_TOKENS,
        help="Estimated output tokens for extractor/revision/repair steps.",
    )
    parser.add_argument(
        "--critic-output-tokens",
        type=int,
        default=DEFAULT_CRITIC_OUTPUT_TOKENS,
        help="Estimated output tokens for critic steps.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    try:
        paper_text = resolve_paper_text(
            paper_path=args.paper_path,
            paper_text=args.paper_text,
        )
    except Exception as exc:
        print(f"Error loading paper text: {exc}", file=sys.stderr)
        sys.exit(1)

    client = make_openai_client()
    progress_callback = None
    if args.show_cost_estimate:
        tracker = LiveCostTracker(
            model=args.model,
            price_input_per_1m=args.price_input_per_1m,
            price_output_per_1m=args.price_output_per_1m,
            agent_output_tokens=args.agent_output_tokens,
            critic_output_tokens=args.critic_output_tokens,
        )
        tracker.start_paper(args.field, simple_fields=None, agentic_fields=(args.field,))
        progress_callback = tracker.callback

    try:
        result = run_agentic_field_extraction(
            client=client,
            field=args.field,
            paper_text=paper_text,
            model=args.model,
            max_critic_rounds=args.max_critic_rounds,
            temperature=args.temperature,
            max_tool_rounds=args.max_tool_rounds,
            progress_callback=progress_callback,
        )
    except Exception as exc:
        print(f"Extraction failed: {exc}", file=sys.stderr)
        sys.exit(1)

    output_payload = result["final_output"] if args.final_only else result
    output_text = json.dumps(output_payload, ensure_ascii=False, indent=2)
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(output_text + "\n", encoding="utf-8")
    print(output_text)
