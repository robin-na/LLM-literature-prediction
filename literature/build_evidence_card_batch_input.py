from __future__ import annotations

import argparse
import json
import random
import statistics
from pathlib import Path


DEFAULT_MODEL = "gpt-4.1"
DEFAULT_TOKENIZER_MODEL = "gpt-4o"
DEFAULT_SMOKE_COUNT = 5
DEFAULT_SEED = 42
DEFAULT_OUTPUT_PREFIX = "literature_evidence_cards"
PROMPT_PATH = Path("literature/prompts/evidence_card_extraction_prompt.md")
PAPERS_DIR = Path("paper_collection/papers_markdown")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build OpenAI batch JSONLs for per-paper literature evidence-card extraction "
            "from markdown papers, plus a small random smoke-test file."
        )
    )
    parser.add_argument(
        "--papers-dir",
        type=Path,
        default=PAPERS_DIR,
        help="Directory containing paper markdown files.",
    )
    parser.add_argument(
        "--prompt-path",
        type=Path,
        default=PROMPT_PATH,
        help="Path to the common extraction prompt.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help="Model name to place in the batch request body.",
    )
    parser.add_argument(
        "--tokenizer-model",
        default=DEFAULT_TOKENIZER_MODEL,
        help="Tokenizer model name used for rough input-token estimation.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("openAI_batch_input"),
        help="Directory for output batch JSONLs.",
    )
    parser.add_argument(
        "--output-prefix",
        default=DEFAULT_OUTPUT_PREFIX,
        help="Filename prefix for generated batch inputs.",
    )
    parser.add_argument(
        "--smoke-count",
        type=int,
        default=DEFAULT_SMOKE_COUNT,
        help="Number of random papers to include in the smoke-test JSONL.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=DEFAULT_SEED,
        help="Random seed for smoke-test sampling.",
    )
    parser.add_argument(
        "--max-papers",
        type=int,
        default=None,
        help="Optional cap on the number of markdown papers to include in the full batch.",
    )
    return parser.parse_args()


def load_prompt(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def load_paper_paths(papers_dir: Path, max_papers: int | None) -> list[Path]:
    papers = sorted(papers_dir.glob("*.md"))
    if max_papers is not None:
        papers = papers[: max(0, max_papers)]
    if not papers:
        raise FileNotFoundError(f"No markdown papers found in {papers_dir}")
    return papers


def paper_id_from_path(path: Path) -> str:
    return path.stem


def build_messages(*, paper_id: str, paper_text: str, system_prompt: str) -> list[dict]:
    user_prompt = "\n\n".join(
        [
            f"paper_id: {paper_id}",
            "paper_markdown:",
            paper_text,
        ]
    )
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]


def build_record(*, paper_id: str, paper_text: str, system_prompt: str, model: str) -> dict:
    return {
        "custom_id": paper_id,
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": model,
            "messages": build_messages(
                paper_id=paper_id,
                paper_text=paper_text,
                system_prompt=system_prompt,
            ),
            "temperature": 0.0,
            "response_format": {"type": "json_object"},
        },
    }


def write_jsonl(path: Path, records: list[dict]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    return len(records)


def get_encoding(tokenizer_model: str):
    import tiktoken

    try:
        return tiktoken.encoding_for_model(tokenizer_model)
    except KeyError:
        return tiktoken.get_encoding("o200k_base")


def estimate_chat_tokens(messages: list[dict], encoding) -> int:
    # Approximate chat-completion token counting for modern chat models.
    tokens_per_message = 3
    tokens_per_name = 1
    total = 3
    for message in messages:
        total += tokens_per_message
        for key, value in message.items():
            total += len(encoding.encode(str(value)))
            if key == "name":
                total += tokens_per_name
    return total


def build_token_summary(
    *,
    paper_paths: list[Path],
    system_prompt: str,
    tokenizer_model: str,
    smoke_ids: set[str],
) -> dict:
    try:
        encoding = get_encoding(tokenizer_model)
    except Exception as exc:
        return {
            "tokenizer_model_requested": tokenizer_model,
            "tokenizer_note": (
                "Token estimate unavailable because tiktoken could not load the requested "
                "encoding in the current environment."
            ),
            "tokenizer_error": repr(exc),
            "n_papers": len(paper_paths),
        }
    per_paper: list[dict[str, object]] = []

    for path in paper_paths:
        paper_id = paper_id_from_path(path)
        paper_text = path.read_text(encoding="utf-8")
        messages = build_messages(
            paper_id=paper_id,
            paper_text=paper_text,
            system_prompt=system_prompt,
        )
        token_count = estimate_chat_tokens(messages, encoding)
        per_paper.append(
            {
                "paper_id": paper_id,
                "path": str(path),
                "estimated_input_tokens": token_count,
                "is_smoke_sample": paper_id in smoke_ids,
            }
        )

    token_values = [int(item["estimated_input_tokens"]) for item in per_paper]
    smoke_values = [
        int(item["estimated_input_tokens"]) for item in per_paper if item["is_smoke_sample"]
    ]

    def _quantile(values: list[int], q: float) -> int:
        if not values:
            return 0
        idx = min(len(values) - 1, max(0, int(round((len(values) - 1) * q))))
        return sorted(values)[idx]

    return {
        "tokenizer_model_requested": tokenizer_model,
        "tokenizer_note": (
            "Estimated with tiktoken chat-message counting and tokenizer-model fallback. "
            "This is approximate."
        ),
        "n_papers": len(per_paper),
        "total_estimated_input_tokens": int(sum(token_values)),
        "mean_estimated_input_tokens": float(statistics.mean(token_values)) if token_values else 0.0,
        "median_estimated_input_tokens": float(statistics.median(token_values)) if token_values else 0.0,
        "p95_estimated_input_tokens": _quantile(token_values, 0.95),
        "max_estimated_input_tokens": max(token_values) if token_values else 0,
        "n_over_32k": sum(1 for value in token_values if value > 32_000),
        "n_over_64k": sum(1 for value in token_values if value > 64_000),
        "n_over_128k": sum(1 for value in token_values if value > 128_000),
        "smoke_sample_total_estimated_input_tokens": int(sum(smoke_values)),
        "largest_papers": sorted(
            per_paper,
            key=lambda item: int(item["estimated_input_tokens"]),
            reverse=True,
        )[:10],
        "smoke_sample": [item for item in per_paper if item["is_smoke_sample"]],
    }


def main() -> None:
    args = parse_args()
    system_prompt = load_prompt(args.prompt_path)
    paper_paths = load_paper_paths(args.papers_dir, args.max_papers)

    full_records: list[dict] = []
    for path in paper_paths:
        paper_id = paper_id_from_path(path)
        paper_text = path.read_text(encoding="utf-8")
        full_records.append(
            build_record(
                paper_id=paper_id,
                paper_text=paper_text,
                system_prompt=system_prompt,
                model=args.model,
            )
        )

    smoke_count = min(max(args.smoke_count, 0), len(paper_paths))
    rng = random.Random(args.seed)
    smoke_paths = rng.sample(paper_paths, smoke_count) if smoke_count else []
    smoke_ids = {paper_id_from_path(path) for path in smoke_paths}
    smoke_records = [
        record for record in full_records if record["custom_id"] in smoke_ids
    ]

    full_output = args.output_dir / f"{args.output_prefix}.jsonl"
    smoke_output = args.output_dir / f"{args.output_prefix}_smoke{smoke_count}.jsonl"
    summary_output = args.output_dir / f"{args.output_prefix}_token_estimate.json"

    full_count = write_jsonl(full_output, full_records)
    smoke_count_written = write_jsonl(smoke_output, smoke_records)

    summary = build_token_summary(
        paper_paths=paper_paths,
        system_prompt=system_prompt,
        tokenizer_model=args.tokenizer_model,
        smoke_ids=smoke_ids,
    )
    summary_output.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Prompt: {args.prompt_path}")
    print(f"Wrote {full_count} requests to {full_output}")
    print(f"Wrote {smoke_count_written} requests to {smoke_output}")
    print(f"Wrote token estimate summary to {summary_output}")


if __name__ == "__main__":
    main()
