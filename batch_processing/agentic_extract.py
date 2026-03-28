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
except ImportError:  # pragma: no cover - allows direct script execution
    from agentic_workflow import make_openai_client, run_agentic_field_extraction, supported_fields  # type: ignore


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
    return parser.parse_args()


def load_paper_text(args: argparse.Namespace) -> str:
    if bool(args.paper_path) == bool(args.paper_text):
        raise ValueError("Provide exactly one of --paper-path or --paper-text.")
    if args.paper_text is not None:
        return args.paper_text
    return Path(args.paper_path).read_text(encoding="utf-8")


def main() -> None:
    args = parse_args()
    try:
        paper_text = load_paper_text(args)
    except Exception as exc:
        print(f"Error loading paper text: {exc}", file=sys.stderr)
        sys.exit(1)

    client = make_openai_client()
    try:
        result = run_agentic_field_extraction(
            client=client,
            field=args.field,
            paper_text=paper_text,
            model=args.model,
            max_critic_rounds=args.max_critic_rounds,
            temperature=args.temperature,
            max_tool_rounds=args.max_tool_rounds,
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


if __name__ == "__main__":
    main()
