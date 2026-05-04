from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


DEFAULT_SOURCE_JSONL = Path("openAI_batch_input/prediction_literature_joint_suite_reps1to5_gpt51.jsonl")
DEFAULT_OUTPUT_DIR = Path("gemini_batch_input")
DEFAULT_MODELS = ["gemini-2.5-flash", "gemini-2.5-pro"]
DEFAULT_OUTPUT_PREFIX = "prediction_literature_baseline-benchmark_joint_reps1to5"
DEFAULT_SEED_BASE = 20260329

MODEL_TAGS = {
    "gemini-2.5-flash": "gemini25flash",
    "gemini-2.5-pro": "gemini25pro",
}

BASELINE_PREFIX = "baseline_joint_reasoning_rep"
BENCHMARK_PREFIX = "paper_analysis_report_joint_rep"
BENCHMARK_SUFFIX = "/PGG_MS_202502"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build Gemini Batch API JSONLs for the literature suite's unaugmented "
            "baseline and PGG_MS_202502 benchmark-report augmentation, using the "
            "exact OpenAI prompts already used in the joint suite."
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
        help="Gemini models to generate JSONLs for.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory for output Gemini batch JSONLs.",
    )
    parser.add_argument(
        "--output-prefix",
        default=DEFAULT_OUTPUT_PREFIX,
        help="Prefix for output JSONL filenames.",
    )
    parser.add_argument(
        "--seed-base",
        type=int,
        default=DEFAULT_SEED_BASE,
        help=(
            "Deterministic seed base for repeated runs. Repeat k uses "
            "seed (seed_base + k - 1). Use a negative value to omit seeds."
        ),
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=1.0,
        help="Sampling temperature to set in Gemini generation_config.",
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

    return selected


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


def _build_gemini_line(
    openai_item: dict,
    *,
    temperature: float,
    seed_base: int | None,
) -> dict:
    custom_id = str(openai_item["custom_id"])
    rep_idx = _extract_rep_idx(custom_id)
    system_text, user_text = _extract_message_texts(openai_item)

    generation_config: dict[str, object] = {
        "response_mime_type": "application/json",
        "temperature": temperature,
    }
    if seed_base is not None:
        generation_config["seed"] = seed_base + rep_idx - 1

    return {
        "key": custom_id,
        "request": {
            "system_instruction": {
                "parts": [{"text": system_text}],
            },
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": user_text}],
                }
            ],
            "generation_config": generation_config,
        },
    }


def _write_jsonl(path: Path, records: list[dict]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    return len(records)


def main() -> None:
    args = parse_args()
    seed_base = None if args.seed_base < 0 else args.seed_base
    openai_requests = _load_openai_requests(args.source_jsonl)

    gemini_records = [
        _build_gemini_line(
            openai_item,
            temperature=args.temperature,
            seed_base=seed_base,
        )
        for openai_item in openai_requests
    ]

    for model in args.models:
        model_records = [
            {
                "key": record["key"],
                "request": {
                    **record["request"],
                    "model": model,
                },
            }
            for record in gemini_records
        ]

        output_path = args.output_dir / f"{args.output_prefix}_{_model_tag(model)}.jsonl"
        count = _write_jsonl(output_path, model_records)
        print(f"Wrote {count} requests to {output_path}")


if __name__ == "__main__":
    main()
