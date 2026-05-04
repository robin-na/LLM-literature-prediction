from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any

from openai import OpenAI

try:
    from api_key_env import DEFAULT_ENV_FILE, load_env_file
except ModuleNotFoundError:
    from literature.api_key_env import DEFAULT_ENV_FILE, load_env_file


DEFAULT_OUTPUT_DIR = Path("openAI_batch_output")
DEFAULT_API_KEY_ENV = "OPENAI_API_KEY"
VALID_BATCH_ENDPOINTS = {
    "/v1/responses",
    "/v1/chat/completions",
    "/v1/embeddings",
    "/v1/completions",
}


def _jsonable(value: Any) -> Any:
    if hasattr(value, "model_dump"):
        return value.model_dump(mode="json")
    if hasattr(value, "to_dict"):
        return value.to_dict()
    if isinstance(value, dict):
        return {k: _jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_jsonable(v) for v in value]
    return value


def _write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(_jsonable(payload), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _resolve_api_key(api_key: str | None, api_key_env: str) -> str:
    key = api_key or os.environ.get(api_key_env)
    if not key:
        raise SystemExit(f"Missing OpenAI API key. Set ${api_key_env} or pass --api-key.")
    return key


def _client(api_key: str | None, api_key_env: str) -> OpenAI:
    return OpenAI(api_key=_resolve_api_key(api_key, api_key_env))


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise SystemExit(f"Input file not found: {path}")
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise SystemExit(f"Invalid JSON on line {line_number} of {path}: {exc}") from exc
            if not isinstance(row, dict):
                raise SystemExit(f"Expected JSON object on line {line_number} of {path}")
            rows.append(row)
    if not rows:
        raise SystemExit(f"No JSONL rows found in {path}")
    return rows


def _infer_endpoint(rows: list[dict[str, Any]]) -> str:
    endpoints = {str(row.get("url", "")).strip() for row in rows}
    endpoints.discard("")
    if len(endpoints) != 1:
        raise SystemExit(f"Expected exactly one batch endpoint in the JSONL, found: {sorted(endpoints)}")
    endpoint = next(iter(endpoints))
    if endpoint not in VALID_BATCH_ENDPOINTS:
        raise SystemExit(
            f"Unsupported batch endpoint {endpoint!r}. Expected one of: {sorted(VALID_BATCH_ENDPOINTS)}"
        )
    return endpoint


def _load_batch_id(batch_id: str | None, batch_meta: Path | None) -> str:
    if batch_id:
        return batch_id
    if not batch_meta:
        raise SystemExit("Provide --batch-id or --batch-meta.")
    payload = json.loads(batch_meta.read_text(encoding="utf-8"))
    value = payload.get("batch_id")
    if isinstance(value, str) and value:
        return value
    batch = payload.get("batch")
    if isinstance(batch, dict):
        batch_id_value = batch.get("id")
        if isinstance(batch_id_value, str) and batch_id_value:
            return batch_id_value
    raise SystemExit(f"Could not find batch id in {batch_meta}")


def cmd_submit(args: argparse.Namespace) -> None:
    client = _client(args.api_key, args.api_key_env)
    rows = _load_jsonl(args.input)
    endpoint = args.endpoint or _infer_endpoint(rows)

    with args.input.open("rb") as handle:
        input_file = client.files.create(file=handle, purpose="batch")

    batch = client.batches.create(
        input_file_id=input_file.id,
        endpoint=endpoint,
        completion_window="24h",
    )

    meta_payload = {
        "input_path": str(args.input),
        "endpoint": endpoint,
        "request_count": len(rows),
        "input_file": _jsonable(input_file),
        "input_file_id": input_file.id,
        "batch": _jsonable(batch),
        "batch_id": batch.id,
    }
    meta_out = args.meta_out or (args.output_dir / f"{args.input.stem}.batch.json")
    _write_json(meta_out, meta_payload)

    print(f"Uploaded {len(rows)} requests from {args.input}")
    print(f"Endpoint: {endpoint}")
    print(f"Input file id: {input_file.id}")
    print(f"Batch id: {batch.id}")
    print(f"Saved batch metadata to {meta_out}")


def cmd_status(args: argparse.Namespace) -> None:
    client = _client(args.api_key, args.api_key_env)
    batch_id = _load_batch_id(args.batch_id, args.batch_meta)
    batch = client.batches.retrieve(batch_id)
    print(json.dumps(_jsonable(batch), ensure_ascii=False, indent=2))


def _write_binary_response(path: Path, response: Any) -> None:
    data = response.read() if hasattr(response, "read") else bytes(response)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def cmd_results(args: argparse.Namespace) -> None:
    client = _client(args.api_key, args.api_key_env)
    batch_id = _load_batch_id(args.batch_id, args.batch_meta)
    batch = client.batches.retrieve(batch_id)

    output_file_id = getattr(batch, "output_file_id", None)
    if not output_file_id:
        raise SystemExit(
            f"Batch {batch_id} has no output_file_id yet. Current status: {getattr(batch, 'status', 'unknown')}"
        )

    output_content = client.files.content(output_file_id)
    _write_binary_response(args.output, output_content)
    print(f"Downloaded output file {output_file_id}")
    print(f"Wrote {args.output}")

    error_file_id = getattr(batch, "error_file_id", None)
    if args.error_output and error_file_id:
        error_content = client.files.content(error_file_id)
        _write_binary_response(args.error_output, error_content)
        print(f"Downloaded error file {error_file_id}")
        print(f"Wrote {args.error_output}")
    elif args.error_output and not error_file_id:
        print(f"No error_file_id is available for batch {batch_id}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Submit, inspect, and download OpenAI Batch API jobs from local JSONL input files."
    )
    parser.add_argument(
        "--env-file",
        type=Path,
        default=DEFAULT_ENV_FILE,
        help=f"Optional local env file to preload API keys from. Default: {DEFAULT_ENV_FILE}",
    )
    parser.add_argument(
        "--api-key",
        help="OpenAI API key. Defaults to the environment variable set by --api-key-env.",
    )
    parser.add_argument(
        "--api-key-env",
        default=DEFAULT_API_KEY_ENV,
        help=f"Environment variable to read the API key from. Default: {DEFAULT_API_KEY_ENV}",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    submit = subparsers.add_parser("submit", help="Upload a local JSONL and create an OpenAI batch.")
    submit.add_argument("--input", type=Path, required=True, help="Path to the OpenAI batch input JSONL.")
    submit.add_argument(
        "--endpoint",
        choices=sorted(VALID_BATCH_ENDPOINTS),
        help="Optional batch endpoint. If omitted, infer it from the JSONL's url field.",
    )
    submit.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory for default metadata outputs.",
    )
    submit.add_argument(
        "--meta-out",
        type=Path,
        help="Optional path for the metadata JSON written after submit.",
    )
    submit.set_defaults(func=cmd_submit)

    status = subparsers.add_parser("status", help="Fetch current status for an existing OpenAI batch.")
    status.add_argument("--batch-id", help="OpenAI batch id, e.g. batch_abc123")
    status.add_argument("--batch-meta", type=Path, help="Metadata JSON created by the submit command.")
    status.set_defaults(func=cmd_status)

    results = subparsers.add_parser("results", help="Download JSONL results for an existing OpenAI batch.")
    results.add_argument("--batch-id", help="OpenAI batch id, e.g. batch_abc123")
    results.add_argument("--batch-meta", type=Path, help="Metadata JSON created by the submit command.")
    results.add_argument("--output", type=Path, required=True, help="Destination output JSONL path.")
    results.add_argument(
        "--error-output",
        type=Path,
        help="Optional destination for the batch error JSONL if OpenAI produced one.",
    )
    results.set_defaults(func=cmd_results)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    load_env_file(args.env_file)
    args.func(args)


if __name__ == "__main__":
    main()
