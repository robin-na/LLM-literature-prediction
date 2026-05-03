from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


DEFAULT_SOURCE_JSONL = Path("openAI_batch_input/prediction_literature_joint_suite_reps1to5_gpt51.jsonl")
DEFAULT_OUTPUT_DIR = Path("claude_batch_input")
DEFAULT_MODELS = [
    "claude-opus-4-6",
    "claude-sonnet-4-6",
    "claude-haiku-4-5",
]
DEFAULT_OUTPUT_PREFIX = "prediction_literature_baseline-benchmark_reasoning_anthropic_merged"
DEFAULT_COMBINED_SUFFIX = "allmodels"
DEFAULT_MAX_TOKENS = 32768
DEFAULT_TEMPERATURE = 1.0

MODEL_TAGS = {
    "claude-opus-4-6": "opus46",
    "claude-sonnet-4-6": "sonnet46",
    "claude-haiku-4-5": "haiku45",
}

BASELINE_PREFIX = "baseline_joint_reasoning_rep"
BENCHMARK_PREFIX = "paper_analysis_report_joint_rep"
BENCHMARK_SUFFIX = "/PGG_MS_202502"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build Anthropic Message Batches payloads for the literature suite's "
            "unaugmented baseline and PGG_MS_202502 benchmark-report augmentation, "
            "using the exact OpenAI prompts already used in the joint suite."
        )
    )
    parser.add_argument(
        "--source-jsonl",
        type=Path,
        default=DEFAULT_SOURCE_JSONL,
        help="Existing OpenAI literature-suite JSONL to use as the canonical prompt source.",
    )
    parser.add_argument(
        "--models",
        nargs="+",
        default=DEFAULT_MODELS,
        choices=DEFAULT_MODELS,
        help="Anthropic model names to generate batch payloads for.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory for output Anthropic batch JSON payloads.",
    )
    parser.add_argument(
        "--output-prefix",
        default=DEFAULT_OUTPUT_PREFIX,
        help="Prefix for output batch filenames.",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=DEFAULT_MAX_TOKENS,
        help="Anthropic max_tokens per request.",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=DEFAULT_TEMPERATURE,
        help="Sampling temperature to set on each request.",
    )
    return parser.parse_args()


def _model_tag(model: str) -> str:
    return MODEL_TAGS[model]


def _is_target_request(custom_id: str) -> bool:
    return custom_id.startswith(BASELINE_PREFIX) or (
        custom_id.startswith(BENCHMARK_PREFIX) and custom_id.endswith(BENCHMARK_SUFFIX)
    )


def _extract_rep_idx(custom_id: str) -> int:
    match = re.search(r"_rep(\d+)(?:/|$)", custom_id)
    if not match:
        raise ValueError(f"Could not extract repeat index from custom_id: {custom_id}")
    return int(match.group(1))


def _sort_key(item: dict) -> tuple[int, int]:
    custom_id = str(item["custom_id"])
    group = 0 if custom_id.startswith(BASELINE_PREFIX) else 1
    return group, _extract_rep_idx(custom_id)


def _load_openai_requests(path: Path) -> list[dict]:
    if not path.exists():
        raise FileNotFoundError(f"OpenAI suite JSONL not found: {path}")

    selected: list[dict] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            item = json.loads(line)
            custom_id = str(item.get("custom_id", "")).strip()
            if _is_target_request(custom_id):
                selected.append(item)

    if len(selected) != 10:
        raise ValueError(
            f"Expected 10 baseline+benchmark requests in {path}, found {len(selected)}"
        )

    baseline_count = sum(
        1 for item in selected if str(item.get("custom_id", "")).startswith(BASELINE_PREFIX)
    )
    benchmark_count = len(selected) - baseline_count
    if baseline_count != 5 or benchmark_count != 5:
        raise ValueError(
            "Expected 5 baseline requests and 5 benchmark requests, found "
            f"{baseline_count} baseline and {benchmark_count} benchmark"
        )

    return sorted(selected, key=_sort_key)


def _extract_message_texts(openai_item: dict) -> tuple[str, str]:
    body = openai_item.get("body", {})
    messages = body.get("messages", [])
    if len(messages) < 2:
        raise ValueError(f"Expected at least 2 messages in request {openai_item.get('custom_id')}")

    system_text = None
    user_text = None
    for message in messages:
        role = message.get("role")
        content = message.get("content")
        if role == "system":
            system_text = content
        elif role == "user":
            user_text = content

    if not isinstance(system_text, str) or not isinstance(user_text, str):
        raise ValueError(f"Missing system/user prompt text in request {openai_item.get('custom_id')}")

    return system_text, user_text


def _sanitize_custom_id(custom_id: str) -> str:
    safe = re.sub(r"[^a-zA-Z0-9_-]", "_", custom_id)
    if len(safe) <= 64:
        return safe
    head, _, tail = safe.rpartition("_")
    if not tail:
        return safe[:64]
    max_head_len = max(1, 64 - len(tail) - 1)
    return f"{head[:max_head_len]}_{tail}"


def _merged_custom_id(custom_id: str, model: str) -> str:
    return _sanitize_custom_id(f"{custom_id}__{_model_tag(model)}")


def _build_anthropic_request(
    openai_item: dict,
    *,
    model: str,
    max_tokens: int,
    temperature: float,
    merged: bool = False,
) -> dict:
    system_text, user_text = _extract_message_texts(openai_item)
    base_custom_id = str(openai_item["custom_id"])

    return {
        "custom_id": _merged_custom_id(base_custom_id, model) if merged else _sanitize_custom_id(base_custom_id),
        "params": {
            "model": model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "system": [
                {
                    "type": "text",
                    "text": system_text,
                }
            ],
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": user_text,
                        }
                    ],
                }
            ],
        },
    }


def _write_json(path: Path, payload: dict) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return len(payload.get("requests", []))


def main() -> None:
    args = parse_args()
    source_requests = _load_openai_requests(args.source_jsonl)
    merged_requests: list[dict] = []

    for model in args.models:
        requests = [
            _build_anthropic_request(
                openai_item,
                model=model,
                max_tokens=args.max_tokens,
                temperature=args.temperature,
            )
            for openai_item in source_requests
        ]
        payload = {"requests": requests}
        output_path = args.output_dir / f"{args.output_prefix}_{_model_tag(model)}.json"
        count = _write_json(output_path, payload)
        print(f"Wrote Anthropic batch payload with {count} requests to {output_path}")
        merged_requests.extend(
            _build_anthropic_request(
                openai_item,
                model=model,
                max_tokens=args.max_tokens,
                temperature=args.temperature,
                merged=True,
            )
            for openai_item in source_requests
        )

    merged_ids = [request["custom_id"] for request in merged_requests]
    if len(merged_ids) != len(set(merged_ids)):
        raise ValueError("Merged Anthropic batch would contain duplicate custom_id values.")

    merged_payload = {"requests": merged_requests}
    merged_output_path = args.output_dir / f"{args.output_prefix}_{DEFAULT_COMBINED_SUFFIX}.json"
    merged_count = _write_json(merged_output_path, merged_payload)
    print(f"Wrote merged Anthropic batch payload with {merged_count} requests to {merged_output_path}")


if __name__ == "__main__":
    main()
