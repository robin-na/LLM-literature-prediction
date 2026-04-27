from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

try:
    from batch_processing.agentic_workflow import (
        make_openai_client,
        run_agentic_field_extraction,
        run_agentic_field_extraction_v2,
        supported_fields,
    )
    from batch_processing.build_batch_input import SYSTEM_PROMPT, build_user_prompt as build_simple_user_prompt
    from batch_processing.extraction_cli_common import (
        DEFAULT_LOCAL_PAPER_DIR,
        DEFAULT_PAPER_IDS,
        RAW_PAPER_MARKDOWN_DIR_ENV_VAR,
        default_paper_dir,
        resolve_paper_dir,
    )
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
        call_simple_extraction,
        fill_paper_level_counts,
        make_simple_rows,
        run_hybrid_extraction_for_paper,
        simple_fields,
        write_hybrid_workbook,
    )
except ImportError:  # pragma: no cover - allows direct script execution
    from agentic_workflow import (  # type: ignore
        make_openai_client,
        run_agentic_field_extraction,
        run_agentic_field_extraction_v2,
        supported_fields,
    )
    from build_batch_input import SYSTEM_PROMPT, build_user_prompt as build_simple_user_prompt  # type: ignore
    from extraction_cli_common import (  # type: ignore
        DEFAULT_LOCAL_PAPER_DIR,
        DEFAULT_PAPER_IDS,
        RAW_PAPER_MARKDOWN_DIR_ENV_VAR,
        default_paper_dir,
        resolve_paper_dir,
    )
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
        call_simple_extraction,
        fill_paper_level_counts,
        make_simple_rows,
        run_hybrid_extraction_for_paper,
        simple_fields,
        write_hybrid_workbook,
    )


def _add_common_paper_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--paper-ids",
        nargs="+",
        default=DEFAULT_PAPER_IDS,
        help="Paper IDs / markdown basenames to process.",
    )
    parser.add_argument(
        "--paper-dir",
        default=default_paper_dir(),
        help=(
            "Directory containing raw paper markdown files. "
            f"Defaults to `{DEFAULT_LOCAL_PAPER_DIR}` or `{RAW_PAPER_MARKDOWN_DIR_ENV_VAR}` if set."
        ),
    )
    parser.add_argument(
        "--model",
        default="gpt-5.1",
        help="OpenAI model name.",
    )
    parser.add_argument(
        "--output-xlsx",
        required=True,
        help="Path to the output Excel workbook.",
    )


def _add_cost_args(parser: argparse.ArgumentParser, *, include_simple: bool) -> None:
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
    if include_simple:
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Primary entrypoint for paper data extraction. "
            "Use 'simple' for one-shot extraction, 'hybrid' for simple + agentic overrides, "
            "'agentic-field' to debug one field on one paper, "
            "or 'batch-submit' / 'batch-status' / 'batch-collect' for the OpenAI Batch API "
            "(same as simple but ~50%% cheaper, results within 24h)."
        )
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    simple_parser = subparsers.add_parser(
        "simple",
        help="Run one-shot extraction for all fields and write an Excel workbook.",
    )
    _add_common_paper_args(simple_parser)
    _add_cost_args(simple_parser, include_simple=True)

    hybrid_parser = subparsers.add_parser(
        "hybrid",
        help="Run simple extraction plus agentic overrides for selected fields.",
    )
    _add_common_paper_args(hybrid_parser)
    hybrid_parser.add_argument(
        "--max-critic-rounds",
        type=int,
        default=1,
        help="Maximum critic rounds for agentic fields.",
    )
    hybrid_parser.add_argument(
        "--max-tool-rounds",
        type=int,
        default=8,
        help="Maximum tool-call rounds per agent step before aborting that field.",
    )
    hybrid_parser.add_argument(
        "--fail-on-agentic-error",
        action="store_true",
        help="Abort the whole run if any agentic field fails instead of falling back to simple extraction.",
    )
    hybrid_parser.add_argument(
        "--agentic-version",
        choices=("v1", "v2"),
        default="v2",
        help="v2 is the recommended default. v1 keeps the legacy always-critic workflow.",
    )
    hybrid_parser.add_argument(
        "--min-review-confidence",
        type=float,
        default=0.85,
        help="v2 only: confidences below this threshold yield needs_review and prevent merge.",
    )
    _add_cost_args(hybrid_parser, include_simple=True)

    field_parser = subparsers.add_parser(
        "agentic-field",
        help="Run agentic extraction for one field on one paper.",
    )
    field_parser.add_argument(
        "--field",
        required=True,
        choices=supported_fields(),
        help="Field to extract.",
    )
    paper_group = field_parser.add_mutually_exclusive_group(required=True)
    paper_group.add_argument(
        "--paper-id",
        help="Paper ID / markdown basename to load from --paper-dir.",
    )
    paper_group.add_argument(
        "--paper-path",
        help="Direct path to a paper markdown file.",
    )
    field_parser.add_argument(
        "--paper-dir",
        default=default_paper_dir(),
        help=(
            "Directory containing raw paper markdown files when using --paper-id. "
            f"Defaults to `{DEFAULT_LOCAL_PAPER_DIR}` or `{RAW_PAPER_MARKDOWN_DIR_ENV_VAR}` if set."
        ),
    )
    field_parser.add_argument(
        "--model",
        default="gpt-5.1",
        help="OpenAI model name.",
    )
    field_parser.add_argument(
        "--agentic-version",
        choices=("v1", "v2"),
        default="v2",
        help="v2 is the recommended default. v1 keeps the legacy always-critic workflow.",
    )
    field_parser.add_argument(
        "--max-critic-rounds",
        type=int,
        default=1,
        help="Maximum number of skeptical review rounds.",
    )
    field_parser.add_argument(
        "--max-tool-rounds",
        type=int,
        default=8,
        help="Maximum number of tool-calling turns per agent step.",
    )
    field_parser.add_argument(
        "--min-review-confidence",
        type=float,
        default=0.85,
        help="v2 only: gate threshold on per-experiment confidence scores.",
    )
    field_parser.add_argument(
        "--temperature",
        type=float,
        default=0.0,
        help="Sampling temperature.",
    )
    field_parser.add_argument(
        "--output",
        help="Optional path to write the workflow JSON payload.",
    )
    field_parser.add_argument(
        "--final-only",
        action="store_true",
        help="Print only the final extraction JSON instead of the full workflow payload.",
    )
    field_parser.add_argument(
        "--show-cost-estimate",
        action="store_true",
        help="Print estimated token usage and cost before each API call.",
    )
    _add_cost_args(field_parser, include_simple=False)

    # ── Batch API subcommands ─────────────────────────────────────────────────
    batch_submit_parser = subparsers.add_parser(
        "batch-submit",
        help=(
            "Build a JSONL of simple-extraction requests, upload it, and submit an OpenAI "
            "Batch API job (~50%% cheaper than real-time, results within 24h). "
            "Prints the batch ID — save it to run 'batch-collect' later."
        ),
    )
    batch_submit_parser.add_argument(
        "--paper-ids",
        nargs="+",
        default=DEFAULT_PAPER_IDS,
        help="Paper IDs / markdown basenames to include. Defaults to the 7 dev papers.",
    )
    batch_submit_parser.add_argument(
        "--paper-dir",
        default=default_paper_dir(),
        help=(
            "Directory containing raw paper markdown files. "
            f"Defaults to `{DEFAULT_LOCAL_PAPER_DIR}` or `{RAW_PAPER_MARKDOWN_DIR_ENV_VAR}` if set."
        ),
    )
    batch_submit_parser.add_argument(
        "--model",
        default="gpt-5.1",
        help="OpenAI model name.",
    )
    batch_submit_parser.add_argument(
        "--save-jsonl",
        default=None,
        help="Optional path to save the submitted JSONL locally for reference.",
    )

    batch_status_parser = subparsers.add_parser(
        "batch-status",
        help="Check the status of a submitted Batch API job.",
    )
    batch_status_parser.add_argument("batch_id", help="Batch ID returned by batch-submit.")

    batch_collect_parser = subparsers.add_parser(
        "batch-collect",
        help=(
            "Download results of a completed Batch API job and write an Excel workbook. "
            "Equivalent output to 'simple', but sourced from the batch results file."
        ),
    )
    batch_collect_parser.add_argument("batch_id", help="Batch ID returned by batch-submit.")
    batch_collect_parser.add_argument(
        "--output-xlsx",
        required=True,
        help="Path to the output Excel workbook.",
    )
    batch_collect_parser.add_argument(
        "--save-jsonl",
        default=None,
        help="Optional path to save the raw output JSONL for debugging.",
    )

    return parser.parse_args()


def _require_api_key() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise EnvironmentError("OPENAI_API_KEY is not set.")


def _paper_path_from_id(paper_dir: Path, paper_id: str) -> Path:
    paper_path = paper_dir / f"{paper_id}.md"
    if not paper_path.exists():
        raise FileNotFoundError(f"Paper markdown not found: {paper_path}")
    return paper_path


def _run_simple_mode(args: argparse.Namespace) -> str:
    _require_api_key()
    client = make_openai_client()
    tracker = LiveCostTracker(
        model=args.model,
        price_input_per_1m=args.price_input_per_1m,
        price_output_per_1m=args.price_output_per_1m,
        simple_output_tokens=args.simple_output_tokens,
        agent_output_tokens=args.agent_output_tokens,
        critic_output_tokens=args.critic_output_tokens,
    )

    paper_dir = resolve_paper_dir(args.paper_dir)
    extraction_rows: list[dict[str, object]] = []

    for paper_id in args.paper_ids:
        paper_path = _paper_path_from_id(paper_dir, paper_id)
        paper_text = paper_path.read_text(encoding="utf-8")
        tracker.start_paper(paper_id, simple_fields=simple_fields(), agentic_fields=None)
        tracker.log_simple_request(
            paper_id=paper_id,
            system_prompt=SYSTEM_PROMPT,
            user_prompt=build_simple_user_prompt(paper_text),
        )
        simple_output = call_simple_extraction(client=client, model=args.model, paper_text=paper_text)
        experiments = simple_output.get("experiments", [])
        if not isinstance(experiments, list):
            raise ValueError(f"'experiments' was not a list for {paper_id}")
        rows = make_simple_rows(paper_id, experiments)
        for row in rows:
            row["source_markdown"] = str(paper_path)
        extraction_rows.extend(rows)

    fill_paper_level_counts(extraction_rows)
    output_path = write_hybrid_workbook(
        output_path=args.output_xlsx,
        extraction_rows=extraction_rows,
        metadata_rows=[],
    )
    tracker.write_cost_summary(
        "batch_processing/cost.md",
        run_label=f"simple / {args.model}",
        paper_ids=args.paper_ids,
        output_xlsx=output_path,
    )
    return output_path


def _run_hybrid_mode(args: argparse.Namespace) -> str:
    _require_api_key()
    client = make_openai_client()
    tracker = LiveCostTracker(
        model=args.model,
        price_input_per_1m=args.price_input_per_1m,
        price_output_per_1m=args.price_output_per_1m,
        simple_output_tokens=args.simple_output_tokens,
        agent_output_tokens=args.agent_output_tokens,
        critic_output_tokens=args.critic_output_tokens,
    )

    extraction_rows: list[dict[str, object]] = []
    metadata_rows: list[dict[str, object]] = []
    paper_dir = resolve_paper_dir(args.paper_dir)
    agentic_fields = DEFAULT_HYBRID_AGENTIC_FIELDS
    simple_field_set = simple_fields(agentic_fields)

    for paper_id in args.paper_ids:
        paper_path = _paper_path_from_id(paper_dir, paper_id)
        paper_text = paper_path.read_text(encoding="utf-8")
        tracker.start_paper(
            paper_id,
            simple_fields=simple_field_set,
            agentic_fields=agentic_fields,
        )
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
            max_tool_rounds=args.max_tool_rounds,
            continue_on_agentic_error=not args.fail_on_agentic_error,
            agentic_version=args.agentic_version,
            min_review_confidence=args.min_review_confidence,
            progress_callback=tracker.callback,
        )
        extraction_rows.extend(result.rows)
        metadata_rows.extend(result.metadata_rows)

    fill_paper_level_counts(extraction_rows)
    output_path = write_hybrid_workbook(
        output_path=args.output_xlsx,
        extraction_rows=extraction_rows,
        metadata_rows=metadata_rows,
    )
    tracker.write_cost_summary(
        "batch_processing/cost.md",
        run_label=f"hybrid / {args.model}",
        paper_ids=args.paper_ids,
        output_xlsx=output_path,
    )
    return output_path


def _run_agentic_field_mode(args: argparse.Namespace) -> None:
    _require_api_key()
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

    if args.paper_path:
        paper_path = Path(args.paper_path)
    else:
        paper_dir = resolve_paper_dir(args.paper_dir)
        paper_path = _paper_path_from_id(paper_dir, str(args.paper_id))

    paper_text = paper_path.read_text(encoding="utf-8")
    if args.agentic_version == "v2":
        result = run_agentic_field_extraction_v2(
            client=client,
            field=args.field,
            paper_text=paper_text,
            model=args.model,
            max_critic_rounds=args.max_critic_rounds,
            temperature=args.temperature,
            max_tool_rounds=args.max_tool_rounds,
            min_confidence=args.min_review_confidence,
            progress_callback=progress_callback,
        )
    else:
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

    output_payload = result["final_output"] if args.final_only else result
    output_text = json.dumps(output_payload, ensure_ascii=False, indent=2)
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(output_text + "\n", encoding="utf-8")
    print(output_text)


def _build_batch_jsonl_lines(paper_ids: list[str], paper_dir: Path, model: str) -> list[str]:
    """Build one JSONL line per paper for the OpenAI Batch API /v1/responses endpoint."""
    lines = []
    for paper_id in paper_ids:
        paper_path = paper_dir / f"{paper_id}.md"
        if not paper_path.exists():
            print(f"Warning: {paper_path} not found, skipping.", file=sys.stderr)
            continue
        paper_text = paper_path.read_text(encoding="utf-8")
        record = {
            "custom_id": paper_id,
            "method": "POST",
            "url": "/v1/responses",
            "body": {
                "model": model,
                "input": [
                    {
                        "role": "system",
                        "content": [{"type": "input_text", "text": SYSTEM_PROMPT}],
                    },
                    {
                        "role": "user",
                        "content": [{"type": "input_text", "text": build_simple_user_prompt(paper_text)}],
                    },
                ],
                "text": {"format": {"type": "json_object"}},
                "temperature": 0,
            },
        }
        lines.append(json.dumps(record, ensure_ascii=False))
    return lines


def _extract_output_text(response_body: dict) -> str | None:
    """Extract the text output from a Batch API response body (Responses API format)."""
    # Direct key (if serialised)
    if response_body.get("output_text"):
        return response_body["output_text"]
    # Parse from output array: [{type: message, content: [{type: output_text, text: ...}]}]
    for item in response_body.get("output", []):
        if not isinstance(item, dict):
            continue
        for part in item.get("content", []):
            if isinstance(part, dict) and part.get("type") == "output_text":
                return part.get("text")
    return None


def _run_batch_submit_mode(args: argparse.Namespace) -> None:
    _require_api_key()
    client = make_openai_client()
    paper_dir = resolve_paper_dir(args.paper_dir)

    paper_ids = args.paper_ids
    if paper_ids == DEFAULT_PAPER_IDS:
        # No explicit list given — scan the directory for all .md files
        paper_ids = sorted(p.stem for p in paper_dir.glob("*.md"))
        print(f"No --paper-ids given; found {len(paper_ids)} papers in {paper_dir}")
    print(f"Building requests for {len(paper_ids)} papers...")
    lines = _build_batch_jsonl_lines(paper_ids, paper_dir, args.model)
    if not lines:
        print("No papers found — nothing to submit.", file=sys.stderr)
        sys.exit(1)
    print(f"  {len(lines)} requests built.")

    jsonl_bytes = ("\n".join(lines) + "\n").encode()

    if args.save_jsonl:
        Path(args.save_jsonl).parent.mkdir(parents=True, exist_ok=True)
        Path(args.save_jsonl).write_bytes(jsonl_bytes)
        print(f"  JSONL saved to {args.save_jsonl}")

    print("Uploading file to OpenAI...")
    file_obj = client.files.create(
        file=("batch_input.jsonl", jsonl_bytes, "application/jsonl"),
        purpose="batch",
    )
    print(f"  File uploaded: {file_obj.id}")

    print("Submitting batch job...")
    batch = client.batches.create(
        input_file_id=file_obj.id,
        endpoint="/v1/responses",
        completion_window="24h",
    )
    print(f"\nBatch submitted successfully.")
    print(f"  Batch ID : {batch.id}")
    print(f"  Status   : {batch.status}")
    print(f"  Requests : {len(lines)}")
    print(f"\nCheck progress:  python batch_processing/extract_papers.py batch-status {batch.id}")
    print(f"Collect results: python batch_processing/extract_papers.py batch-collect {batch.id} --output-xlsx <path>")


def _run_batch_status_mode(args: argparse.Namespace) -> None:
    _require_api_key()
    client = make_openai_client()
    batch = client.batches.retrieve(args.batch_id)
    counts = batch.request_counts
    print(f"Batch ID : {batch.id}")
    print(f"Status   : {batch.status}")
    print(f"Requests : {counts.completed} completed / {counts.failed} failed / {counts.total} total")
    if batch.status == "completed":
        print(f"\nReady to collect. Run:")
        print(f"  python batch_processing/extract_papers.py batch-collect {batch.id} --output-xlsx <path>")
    elif batch.status in ("failed", "expired", "cancelled"):
        print(f"\nBatch ended with status '{batch.status}'. Check the OpenAI dashboard for details.")
    else:
        print(f"\nNot ready yet — check again later.")


def _run_batch_collect_mode(args: argparse.Namespace) -> None:
    _require_api_key()
    client = make_openai_client()

    batch = client.batches.retrieve(args.batch_id)
    if batch.status != "completed":
        print(f"Batch is not completed yet (status: {batch.status}). Cannot collect.", file=sys.stderr)
        sys.exit(1)

    print(f"Downloading results (output file: {batch.output_file_id})...")
    raw_content = client.files.content(batch.output_file_id).text

    if args.save_jsonl:
        Path(args.save_jsonl).parent.mkdir(parents=True, exist_ok=True)
        Path(args.save_jsonl).write_text(raw_content, encoding="utf-8")
        print(f"  Raw JSONL saved to {args.save_jsonl}")

    extraction_rows: list[dict] = []
    errors: list[str] = []

    for line in raw_content.splitlines():
        if not line.strip():
            continue
        result = json.loads(line)
        custom_id = result.get("custom_id", "<unknown>")

        if result.get("error"):
            errors.append(f"{custom_id}: {result['error']}")
            continue

        response = result.get("response", {})
        if response.get("status_code") != 200:
            errors.append(f"{custom_id}: HTTP {response.get('status_code')}")
            continue

        output_text = _extract_output_text(response.get("body", {}))
        if not output_text:
            errors.append(f"{custom_id}: no output_text in response body")
            continue

        try:
            parsed = json.loads(output_text)
        except json.JSONDecodeError as exc:
            errors.append(f"{custom_id}: JSON parse error — {exc}")
            continue

        experiments = parsed.get("experiments", [])
        if not isinstance(experiments, list):
            errors.append(f"{custom_id}: 'experiments' was not a list")
            continue

        rows = make_simple_rows(custom_id, experiments)
        extraction_rows.extend(rows)

    fill_paper_level_counts(extraction_rows)
    output_path = write_hybrid_workbook(
        output_path=args.output_xlsx,
        extraction_rows=extraction_rows,
        metadata_rows=[],
    )

    papers_done = len({r.get("custom_id", "") for r in extraction_rows})
    print(f"\nResults written to: {output_path}")
    print(f"Papers collected  : {papers_done}")
    print(f"Rows extracted    : {len(extraction_rows)}")
    if errors:
        print(f"\nErrors ({len(errors)}):")
        for e in errors:
            print(f"  {e}")


def main() -> None:
    args = parse_args()
    try:
        if args.command == "simple":
            output_path = _run_simple_mode(args)
            print(output_path)
            return
        if args.command == "hybrid":
            output_path = _run_hybrid_mode(args)
            print(output_path)
            return
        if args.command == "agentic-field":
            _run_agentic_field_mode(args)
            return
        if args.command == "batch-submit":
            _run_batch_submit_mode(args)
            return
        if args.command == "batch-status":
            _run_batch_status_mode(args)
            return
        if args.command == "batch-collect":
            _run_batch_collect_mode(args)
            return
        raise ValueError(f"Unknown command: {args.command}")
    except Exception as exc:
        print(f"Extraction failed: {exc}", file=sys.stderr)
        sys.exit(1)
