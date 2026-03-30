from __future__ import annotations

"""Compatibility entrypoint for the hybrid extraction CLI.

The maintained implementation now lives in `batch_processing/hybrid_extract_app.py`
and the shared orchestration lives in `batch_processing/extraction_pipeline.py`.
"""

try:
    from batch_processing.hybrid_extract_app import main as delegated_main
except ImportError:  # pragma: no cover - allows direct script execution
    from hybrid_extract_app import main as delegated_main  # type: ignore

if __name__ == "__main__":
    delegated_main()
    raise SystemExit

import argparse
import json
import os
from pathlib import Path
from typing import Any

import pandas as pd

try:
    import tiktoken
except ImportError:  # pragma: no cover - optional dependency
    tiktoken = None

try:
    from batch_processing.agentic_workflow import make_openai_client, run_agentic_field_extraction
    from batch_processing.batch_output_to_csv import BASE_FIELDS
    from batch_processing.build_batch_input import (
        INSTRUCTION_TEXT,
        OUTPUT_SCHEMA_DESCRIPTION,
        SYSTEM_PROMPT,
    )
except ImportError:  # pragma: no cover - allows direct script execution
    from agentic_workflow import make_openai_client, run_agentic_field_extraction  # type: ignore
    from batch_output_to_csv import BASE_FIELDS  # type: ignore
    from build_batch_input import INSTRUCTION_TEXT, OUTPUT_SCHEMA_DESCRIPTION, SYSTEM_PROMPT  # type: ignore


AGENTIC_FIELDS = (
    "CONFIG_playerCount",
    "CONFIG_MPCR",
    "DV_contributionRate",
    "DV_efficiency",
    "CONFIG_allOrNothing",
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

DEFAULT_PRICE_INPUT_PER_1M = 2.0
DEFAULT_PRICE_OUTPUT_PER_1M = 8.0
SIMPLE_FIELDS = tuple(field for field in BASE_FIELDS if field not in AGENTIC_FIELDS)


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
        default="literature/output/paper_analysis_reports/broad_all",
        help="Directory containing source markdown files.",
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
        default=3500,
        help="Estimated output tokens for the simple extraction call.",
    )
    parser.add_argument(
        "--agent-output-tokens",
        type=int,
        default=1200,
        help="Estimated output tokens for extractor/revision/repair agent steps.",
    )
    parser.add_argument(
        "--critic-output-tokens",
        type=int,
        default=900,
        help="Estimated output tokens for critic steps.",
    )
    return parser.parse_args()


class LiveCostTracker:
    def __init__(
        self,
        *,
        model: str,
        price_input_per_1m: float,
        price_output_per_1m: float,
        simple_output_tokens: int,
        agent_output_tokens: int,
        critic_output_tokens: int,
    ) -> None:
        self.model = model
        self.price_input_per_1m = price_input_per_1m
        self.price_output_per_1m = price_output_per_1m
        self.simple_output_tokens = simple_output_tokens
        self.agent_output_tokens = agent_output_tokens
        self.critic_output_tokens = critic_output_tokens
        self.total_input_tokens = 0
        self.total_estimated_output_tokens = 0
        self.request_count = 0

    def start_paper(self, paper_id: str) -> None:
        print("\n" + "=" * 80, flush=True)
        print(f"[paper] {paper_id}", flush=True)
        print("=" * 80, flush=True)
        print(
            "[mode] simple  -> "
            + ", ".join(SIMPLE_FIELDS),
            flush=True,
        )
        print(
            "[mode] agentic -> "
            + ", ".join(AGENTIC_FIELDS),
            flush=True,
        )
        print("-" * 80, flush=True)

    def estimate_text_tokens(self, text: str) -> int:
        if tiktoken is not None:
            try:
                encoding = tiktoken.encoding_for_model(self.model)
            except Exception:
                encoding = tiktoken.get_encoding("cl100k_base")
            return len(encoding.encode(text))
        return max(1, len(text) // 4)

    def estimate_messages_tokens(self, messages: list[dict[str, Any]]) -> int:
        total = 0
        for message in messages:
            total += 4
            total += self.estimate_text_tokens(str(message.get("role", "")))
            total += self.estimate_text_tokens(self._flatten_message_content(message.get("content", "")))
            for tool_call in message.get("tool_calls", []) or []:
                function = tool_call.get("function", {})
                total += self.estimate_text_tokens(str(function.get("name", "")))
                total += self.estimate_text_tokens(str(function.get("arguments", "")))
            tool_call_id = message.get("tool_call_id")
            if tool_call_id:
                total += self.estimate_text_tokens(str(tool_call_id))
        return total

    def log_simple_request(self, *, paper_id: str, system_prompt: str, user_prompt: str) -> None:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
        self._log_request(
            label=f"{paper_id}:simple:all_non_agentic_fields",
            messages=messages,
            estimated_output_tokens=self.simple_output_tokens,
        )

    def callback(self, payload: dict[str, Any]) -> None:
        label = str(payload.get("label", "agent_call"))
        messages = payload.get("messages", [])
        estimated_output_tokens = self.agent_output_tokens
        if "critic" in label:
            estimated_output_tokens = self.critic_output_tokens
        self._log_request(
            label=label,
            messages=messages if isinstance(messages, list) else [],
            estimated_output_tokens=estimated_output_tokens,
        )

    def _log_request(
        self,
        *,
        label: str,
        messages: list[dict[str, Any]],
        estimated_output_tokens: int,
    ) -> None:
        input_tokens = self.estimate_messages_tokens(messages)
        input_cost = (input_tokens / 1_000_000) * self.price_input_per_1m
        output_cost = (estimated_output_tokens / 1_000_000) * self.price_output_per_1m
        total_cost = input_cost + output_cost

        self.request_count += 1
        self.total_input_tokens += input_tokens
        self.total_estimated_output_tokens += estimated_output_tokens
        cumulative_cost = (
            (self.total_input_tokens / 1_000_000) * self.price_input_per_1m
            + (self.total_estimated_output_tokens / 1_000_000) * self.price_output_per_1m
        )
        print(f"[estimate {self.request_count:03d}] {self._pretty_label(label)}", flush=True)
        print(
            f"  input     ~ {input_tokens:>10,} tok   ~ ${input_cost:>8.4f}",
            flush=True,
        )
        print(
            f"  output    ~ {estimated_output_tokens:>10,} tok   ~ ${output_cost:>8.4f}",
            flush=True,
        )
        print(f"  call est. ~ ${total_cost:>8.4f}", flush=True)
        print(
            "  cumulative"
            f" ~ in {self.total_input_tokens:,} tok"
            f" | out {self.total_estimated_output_tokens:,} tok"
            f" | ${cumulative_cost:.4f}",
            flush=True,
        )

    def _flatten_message_content(self, content: Any) -> str:
        if isinstance(content, str):
            return content
        if isinstance(content, list):
            parts: list[str] = []
            for item in content:
                if isinstance(item, dict):
                    parts.append(str(item.get("text", "")))
                else:
                    parts.append(str(item))
            return "\n".join(parts)
        return str(content)

    def _pretty_label(self, label: str) -> str:
        parts = label.split(":")
        if len(parts) == 3 and parts[1] == "simple":
            return f"simple  | {parts[0]} | {parts[2].replace('_', ' ')}"
        if len(parts) >= 2:
            return f"agentic | {parts[0]} -> {':'.join(parts[1:]).replace('_', ' ')}"
        if ":" not in label:
            return label
        return label.replace("_", " ")


def build_simple_user_prompt(paper_text: str) -> str:
    return "\n\n".join(
        [
            OUTPUT_SCHEMA_DESCRIPTION,
            INSTRUCTION_TEXT,
            "Paper text:\n" + paper_text,
        ]
    )


def call_simple_extraction(*, client: Any, model: str, paper_text: str) -> dict[str, Any]:
    response = client.responses.create(
        model=model,
        input=[
            {
                "role": "system",
                "content": [{"type": "input_text", "text": SYSTEM_PROMPT}],
            },
            {
                "role": "user",
                "content": [{"type": "input_text", "text": build_simple_user_prompt(paper_text)}],
            },
        ],
        text={"format": {"type": "json_object"}},
        temperature=0,
    )
    output_text = getattr(response, "output_text", None)
    if not output_text:
        raise ValueError("Simple extraction response did not include output_text.")
    parsed = json.loads(output_text)
    if not isinstance(parsed, dict):
        raise ValueError("Simple extraction output was not a JSON object.")
    return parsed


def normalize_data_id(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    return " ".join(value.lower().split())


def make_base_row(custom_id: str, experiment: dict[str, Any]) -> dict[str, Any]:
    row = {"custom_id": custom_id}
    for field in BASE_FIELDS:
        row[field] = experiment.get(field, "N/R")
        row[f"{field}_reason"] = experiment.get(f"{field}_reason", "")
        row[f"{field}_confidence"] = experiment.get(f"{field}_confidence", 0)
    return row


def merge_agentic_fields(
    *,
    simple_rows: list[dict[str, Any]],
    agentic_results: dict[str, dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    metadata_rows: list[dict[str, Any]] = []
    simple_lookup: dict[str, list[dict[str, Any]]] = {}
    for row in simple_rows:
        simple_lookup.setdefault(normalize_data_id(row.get("data_id")), []).append(row)

    for field, result in agentic_results.items():
        experiments = result["final_output"].get("experiments", [])
        for experiment in experiments:
            normalized = normalize_data_id(experiment.get("data_id"))
            candidates = simple_lookup.get(normalized, [])
            target_row: dict[str, Any] | None = None
            if len(candidates) == 1:
                target_row = candidates[0]
            elif len(simple_rows) == 1 and len(experiments) == 1:
                target_row = simple_rows[0]
            if target_row is None:
                continue
            target_row[field] = experiment.get(field, target_row.get(field, "N/R"))
            target_row[f"{field}_reason"] = experiment.get(
                f"{field}_reason",
                target_row.get(f"{field}_reason", ""),
            )
            target_row[f"{field}_confidence"] = experiment.get(
                f"{field}_confidence",
                target_row.get(f"{field}_confidence", 0),
            )
        metadata_rows.append(
            {
                "field": field,
                "validation_ok": result["validation"]["ok"],
                "validation_errors": json.dumps(result["validation"]["errors"], ensure_ascii=False),
                "validation_warnings": json.dumps(
                    result["validation"]["warnings"], ensure_ascii=False
                ),
                "critic_round_count": len(result["critic_rounds"]),
            }
        )
    return simple_rows, metadata_rows


def main() -> None:
    args = parse_args()
    if not os.getenv("OPENAI_API_KEY"):
        raise EnvironmentError("OPENAI_API_KEY is not set.")
    paper_dir = Path(args.paper_dir)
    client = make_openai_client()
    cost_tracker = LiveCostTracker(
        model=args.model,
        price_input_per_1m=args.price_input_per_1m,
        price_output_per_1m=args.price_output_per_1m,
        simple_output_tokens=args.simple_output_tokens,
        agent_output_tokens=args.agent_output_tokens,
        critic_output_tokens=args.critic_output_tokens,
    )

    all_rows: list[dict[str, Any]] = []
    metadata_rows: list[dict[str, Any]] = []

    for paper_id in args.paper_ids:
        paper_path = paper_dir / f"{paper_id}.md"
        if not paper_path.exists():
            raise FileNotFoundError(f"Paper markdown not found: {paper_path}")

        cost_tracker.start_paper(paper_id)
        paper_text = paper_path.read_text(encoding="utf-8")
        simple_user_prompt = build_simple_user_prompt(paper_text)
        cost_tracker.log_simple_request(
            paper_id=paper_id,
            system_prompt=SYSTEM_PROMPT,
            user_prompt=simple_user_prompt,
        )
        simple_output = call_simple_extraction(
            client=client,
            model=args.model,
            paper_text=paper_text,
        )
        experiments = simple_output.get("experiments", [])
        if not isinstance(experiments, list):
            raise ValueError(f"'experiments' was not a list for {paper_id}")
        simple_rows = [make_base_row(paper_id, experiment) for experiment in experiments if isinstance(experiment, dict)]

        agentic_results: dict[str, dict[str, Any]] = {}
        for field in AGENTIC_FIELDS:
            agentic_results[field] = run_agentic_field_extraction(
                client=client,
                field=field,
                paper_text=paper_text,
                model=args.model,
                max_critic_rounds=args.max_critic_rounds,
                temperature=0.0,
                progress_callback=cost_tracker.callback,
            )

        merged_rows, paper_metadata = merge_agentic_fields(
            simple_rows=simple_rows,
            agentic_results=agentic_results,
        )
        for row in merged_rows:
            row["source_markdown"] = str(paper_path)
        for item in paper_metadata:
            item["custom_id"] = paper_id
            item["source_markdown"] = str(paper_path)

        all_rows.extend(merged_rows)
        metadata_rows.extend(paper_metadata)

    output_path = Path(args.output_xlsx)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(output_path) as writer:
        pd.DataFrame(all_rows).to_excel(writer, sheet_name="extractions", index=False)
        pd.DataFrame(metadata_rows).to_excel(writer, sheet_name="agentic_meta", index=False)

    print(output_path)


if __name__ == "__main__":
    main()
