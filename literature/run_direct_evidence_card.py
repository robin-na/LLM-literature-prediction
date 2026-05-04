from __future__ import annotations

import argparse
import csv
import json
import os
import subprocess
import sys
import time
import uuid
from pathlib import Path
from typing import Any

from openai import OpenAI


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from literature.build_evidence_card_batch_input import (  # noqa: E402
    build_messages,
    load_prompt,
)
from literature.parse_evidence_card_batch_output import parse_json_content  # noqa: E402


DEFAULT_MODELS = ["gpt-4.1-2025-04-14", "gpt-5.1"]
DEFAULT_PAPER_PATH = Path("paper_collection/papers_markdown_cleaned/PGG_Science.md")
DEFAULT_PROMPT_PATH = Path("literature/prompts/evidence_card_extraction_prompt.md")
DEFAULT_RAW_OUTPUT_DIR = Path("openAI_batch_output")
DEFAULT_PARSED_OUTPUT_ROOT = Path("literature/output/evidence_cards")
DEFAULT_BASE_CORPUS_DIR = Path("literature/output/evidence_cards/literature_evidence_cards_cleaned")
DEFAULT_OUTPUT_PREFIX = "literature_evidence_card"
DEFAULT_API_KEY_ENV_VAR = "OPENAI_API_KEY"

MODEL_TAGS = {
    "gpt-4.1-2025-04-14": "41",
    "gpt-5.1": "gpt51",
}

TABLE_FILES = [
    "papers.csv",
    "combined.csv",
    "dimensions.csv",
    "key_claims.csv",
    "important_limitations.csv",
    "errors.csv",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Call the OpenAI API directly to extract a single-paper literature evidence "
            "card, parse it into the standard evidence-card tables, and optionally "
            "produce a merged copy of the existing cleaned evidence-card corpus with the "
            "new paper appended."
        )
    )
    parser.add_argument(
        "--paper-path",
        type=Path,
        default=DEFAULT_PAPER_PATH,
        help="Path to the cleaned markdown paper to process.",
    )
    parser.add_argument(
        "--paper-id",
        default=None,
        help="Optional explicit paper id. Defaults to the markdown filename stem.",
    )
    parser.add_argument(
        "--prompt-path",
        type=Path,
        default=DEFAULT_PROMPT_PATH,
        help="Path to the shared evidence-card extraction prompt.",
    )
    parser.add_argument(
        "--models",
        nargs="+",
        default=DEFAULT_MODELS,
        help="One or more OpenAI model names to run.",
    )
    parser.add_argument(
        "--raw-output-dir",
        type=Path,
        default=DEFAULT_RAW_OUTPUT_DIR,
        help="Directory for raw batch-like JSONL outputs.",
    )
    parser.add_argument(
        "--parsed-output-root",
        type=Path,
        default=DEFAULT_PARSED_OUTPUT_ROOT,
        help="Root directory for parsed evidence-card outputs.",
    )
    parser.add_argument(
        "--base-corpus-dir",
        type=Path,
        default=DEFAULT_BASE_CORPUS_DIR,
        help="Existing parsed evidence-card corpus to merge into.",
    )
    parser.add_argument(
        "--output-prefix",
        default=DEFAULT_OUTPUT_PREFIX,
        help="Prefix used for raw and parsed output names.",
    )
    parser.add_argument(
        "--api-key-env-var",
        default=DEFAULT_API_KEY_ENV_VAR,
        help="Environment variable that holds the OpenAI API key.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Optional deterministic seed for Chat Completions. Use a negative value to omit it.",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.0,
        help="Sampling temperature to request when supported.",
    )
    parser.add_argument(
        "--max-attempts",
        type=int,
        default=2,
        help="Maximum attempts per model if the response is invalid JSON or a transient API error occurs.",
    )
    parser.add_argument(
        "--retry-sleep-seconds",
        type=float,
        default=1.0,
        help="Sleep between retry attempts.",
    )
    parser.add_argument(
        "--no-merge-with-base",
        action="store_true",
        help="Skip creation of merged corpus directories.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned outputs without making API calls.",
    )
    return parser.parse_args()


def model_tag(model: str) -> str:
    if model in MODEL_TAGS:
        return MODEL_TAGS[model]
    return (
        model.lower()
        .replace(".", "")
        .replace("-", "")
        .replace("/", "_")
    )


def output_stem(prefix: str, paper_id: str, model: str) -> str:
    return f"{prefix}_{paper_id.lower()}_{model_tag(model)}"


def build_request_body(
    *,
    paper_id: str,
    paper_text: str,
    system_prompt: str,
    model: str,
    seed: int | None,
    temperature: float | None,
) -> dict[str, Any]:
    body: dict[str, Any] = {
        "model": model,
        "messages": build_messages(
            paper_id=paper_id,
            paper_text=paper_text,
            system_prompt=system_prompt,
        ),
        "response_format": {"type": "json_object"},
    }
    if seed is not None:
        body["seed"] = seed
    if temperature is not None:
        body["temperature"] = temperature
    return body


def extract_content_from_record(record: dict[str, Any]) -> str | None:
    response = record.get("response") or {}
    body = response.get("body") or {}
    if response.get("status_code") != 200:
        return None
    choices = body.get("choices") or []
    if not choices:
        return None
    message = choices[0].get("message") or {}
    content = message.get("content")
    return content if isinstance(content, str) else None


def success_record(*, custom_id: str, response: Any) -> dict[str, Any]:
    return {
        "id": f"direct_req_{uuid.uuid4().hex}",
        "custom_id": custom_id,
        "response": {
            "status_code": 200,
            "request_id": getattr(response, "_request_id", ""),
            "body": response.model_dump(mode="json"),
        },
    }


def error_record(*, custom_id: str, exc: Exception) -> dict[str, Any]:
    status_code = getattr(exc, "status_code", None)
    request_id = getattr(exc, "request_id", "")
    return {
        "id": f"direct_req_{uuid.uuid4().hex}",
        "custom_id": custom_id,
        "response": {
            "status_code": int(status_code) if isinstance(status_code, int) else 0,
            "request_id": request_id,
            "body": {
                "error": {
                    "message": str(exc),
                }
            },
        },
    }


def should_retry_api_error(record: dict[str, Any]) -> bool:
    response = record.get("response") or {}
    status_code = response.get("status_code")
    return status_code in {0, 408, 409, 429, 500, 502, 503, 504}


def maybe_retry_without_temperature(body: dict[str, Any], exc: Exception) -> dict[str, Any] | None:
    error_text = str(exc).lower()
    if "temperature" not in error_text:
        return None
    if "unsupported" not in error_text and "unknown parameter" not in error_text and "invalid" not in error_text:
        return None
    retry_body = dict(body)
    retry_body.pop("temperature", None)
    return retry_body


def request_card_record(
    *,
    client: OpenAI,
    paper_id: str,
    paper_text: str,
    system_prompt: str,
    model: str,
    seed: int | None,
    temperature: float | None,
    max_attempts: int,
    retry_sleep_seconds: float,
) -> tuple[dict[str, Any], int, str]:
    body = build_request_body(
        paper_id=paper_id,
        paper_text=paper_text,
        system_prompt=system_prompt,
        model=model,
        seed=seed,
        temperature=temperature,
    )
    last_record: dict[str, Any] | None = None
    last_parse_error = ""

    for attempt in range(1, max_attempts + 1):
        try:
            response = client.chat.completions.create(**body)
            record = success_record(custom_id=paper_id, response=response)
        except Exception as exc:
            retry_body = maybe_retry_without_temperature(body, exc)
            if retry_body is not None:
                body = retry_body
                try:
                    response = client.chat.completions.create(**body)
                    record = success_record(custom_id=paper_id, response=response)
                except Exception as retry_exc:
                    record = error_record(custom_id=paper_id, exc=retry_exc)
            else:
                record = error_record(custom_id=paper_id, exc=exc)

        last_record = record
        content = extract_content_from_record(record)
        if content is None:
            if attempt < max_attempts and should_retry_api_error(record):
                time.sleep(retry_sleep_seconds)
                continue
            return record, attempt, last_parse_error

        try:
            parse_json_content(content)
            return record, attempt, ""
        except Exception as exc:
            last_parse_error = repr(exc)
            if attempt < max_attempts:
                time.sleep(retry_sleep_seconds)
                continue
            return record, attempt, last_parse_error

    if last_record is None:
        raise RuntimeError("No request record was produced.")
    return last_record, max_attempts, last_parse_error


def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def run_parser(input_path: Path, output_dir: Path) -> None:
    subprocess.run(
        [
            sys.executable,
            str(PROJECT_ROOT / "literature/parse_evidence_card_batch_output.py"),
            "--input",
            str(input_path),
            "--output-dir",
            str(output_dir),
        ],
        check=True,
        cwd=PROJECT_ROOT,
    )


def load_csv_with_fieldnames(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        return list(reader.fieldnames or []), rows


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build_single_paper_set(path: Path, paper_id: str) -> None:
    write_csv(path, ["custom_id"], [{"custom_id": paper_id}])


def merge_table(base_path: Path, single_path: Path, merged_path: Path, paper_id: str) -> int:
    base_fieldnames, base_rows = load_csv_with_fieldnames(base_path)
    single_fieldnames, single_rows = load_csv_with_fieldnames(single_path)
    merged_rows = [row for row in base_rows if row.get("custom_id") != paper_id] + single_rows
    fieldnames = base_fieldnames or single_fieldnames
    write_csv(merged_path, fieldnames, merged_rows)
    return len(merged_rows)


def build_merged_summary(
    *,
    base_corpus_dir: Path,
    single_output_dir: Path,
    merged_output_dir: Path,
    raw_jsonl: Path,
    paper_id: str,
    model: str,
    table_counts: dict[str, int],
) -> None:
    summary = {
        "input_path": str(raw_jsonl),
        "output_dir": str(merged_output_dir),
        "base_corpus_dir": str(base_corpus_dir),
        "single_output_dir": str(single_output_dir),
        "added_custom_ids": [paper_id],
        "model": model,
        "papers_csv": str(merged_output_dir / "papers.csv"),
        "combined_csv": str(merged_output_dir / "combined.csv"),
        "dimensions_csv": str(merged_output_dir / "dimensions.csv"),
        "key_claims_csv": str(merged_output_dir / "key_claims.csv"),
        "important_limitations_csv": str(merged_output_dir / "important_limitations.csv"),
        "errors_csv": str(merged_output_dir / "errors.csv"),
        "paper_set_csv": str(merged_output_dir / "paper_set_single.csv"),
        "table_row_counts": table_counts,
    }
    (merged_output_dir / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def merge_with_base_corpus(
    *,
    base_corpus_dir: Path,
    single_output_dir: Path,
    merged_output_dir: Path,
    raw_jsonl: Path,
    paper_id: str,
    model: str,
) -> None:
    merged_output_dir.mkdir(parents=True, exist_ok=True)
    table_counts: dict[str, int] = {}
    for table_name in TABLE_FILES:
        base_path = base_corpus_dir / table_name
        single_path = single_output_dir / table_name
        merged_path = merged_output_dir / table_name
        table_counts[table_name] = merge_table(base_path, single_path, merged_path, paper_id)

    build_single_paper_set(merged_output_dir / "paper_set_single.csv", paper_id)
    build_merged_summary(
        base_corpus_dir=base_corpus_dir,
        single_output_dir=single_output_dir,
        merged_output_dir=merged_output_dir,
        raw_jsonl=raw_jsonl,
        paper_id=paper_id,
        model=model,
        table_counts=table_counts,
    )


def main() -> None:
    args = parse_args()
    paper_path = args.paper_path
    if not paper_path.exists():
        raise FileNotFoundError(f"Paper markdown not found: {paper_path}")
    if not args.prompt_path.exists():
        raise FileNotFoundError(f"Prompt not found: {args.prompt_path}")
    if not args.no_merge_with_base and not args.base_corpus_dir.exists():
        raise FileNotFoundError(f"Base evidence-card corpus not found: {args.base_corpus_dir}")

    paper_id = args.paper_id or paper_path.stem
    system_prompt = load_prompt(args.prompt_path)
    paper_text = paper_path.read_text(encoding="utf-8")
    seed = None if args.seed < 0 else int(args.seed)

    planned: list[tuple[str, Path, Path, Path | None]] = []
    for model in args.models:
        stem = output_stem(args.output_prefix, paper_id, model)
        raw_jsonl = args.raw_output_dir / f"{stem}.jsonl"
        single_output_dir = args.parsed_output_root / stem
        merged_output_dir = None
        if not args.no_merge_with_base:
            merged_output_dir = (
                args.parsed_output_root
                / f"{args.base_corpus_dir.name}_plus_{paper_id.lower()}_{model_tag(model)}"
            )
        planned.append((model, raw_jsonl, single_output_dir, merged_output_dir))

    if args.dry_run:
        print(f"Paper id: {paper_id}")
        print(f"Paper path: {paper_path}")
        print(f"Prompt path: {args.prompt_path}")
        for model, raw_jsonl, single_output_dir, merged_output_dir in planned:
            print(f"Model: {model}")
            print(f"  Raw JSONL: {raw_jsonl}")
            print(f"  Parsed output: {single_output_dir}")
            if merged_output_dir is not None:
                print(f"  Merged corpus: {merged_output_dir}")
        return

    api_key = os.environ.get(args.api_key_env_var, "").strip()
    if not api_key:
        raise EnvironmentError(
            f"{args.api_key_env_var} is not set. Export an OpenAI API key before running this script."
        )

    client = OpenAI(api_key=api_key)

    for model, raw_jsonl, single_output_dir, merged_output_dir in planned:
        record, attempts_used, parse_retry_error = request_card_record(
            client=client,
            paper_id=paper_id,
            paper_text=paper_text,
            system_prompt=system_prompt,
            model=model,
            seed=seed,
            temperature=args.temperature,
            max_attempts=max(1, args.max_attempts),
            retry_sleep_seconds=max(0.0, args.retry_sleep_seconds),
        )
        write_jsonl(raw_jsonl, [record])
        run_parser(raw_jsonl, single_output_dir)
        build_single_paper_set(single_output_dir / "paper_set_single.csv", paper_id)

        if merged_output_dir is not None:
            merge_with_base_corpus(
                base_corpus_dir=args.base_corpus_dir,
                single_output_dir=single_output_dir,
                merged_output_dir=merged_output_dir,
                raw_jsonl=raw_jsonl,
                paper_id=paper_id,
                model=model,
            )

        print(f"Model: {model}")
        print(f"  Attempts used: {attempts_used}")
        if parse_retry_error:
            print(f"  Final JSON validation note: {parse_retry_error}")
        print(f"  Raw JSONL: {raw_jsonl}")
        print(f"  Parsed output: {single_output_dir}")
        print(f"  Paper set CSV: {single_output_dir / 'paper_set_single.csv'}")
        if merged_output_dir is not None:
            print(f"  Merged corpus: {merged_output_dir}")
            print(f"  Merged paper set CSV: {merged_output_dir / 'paper_set_single.csv'}")


if __name__ == "__main__":
    main()
