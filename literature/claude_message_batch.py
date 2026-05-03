from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any

import anthropic

try:
    from api_key_env import DEFAULT_ENV_FILE, load_env_file
except ModuleNotFoundError:
    from literature.api_key_env import DEFAULT_ENV_FILE, load_env_file

DEFAULT_OUTPUT_DIR = Path("claude_batch_output")
DEFAULT_API_KEY_ENV = "ANTHROPIC_API_KEY"


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


def _write_jsonl(path: Path, rows: list[Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(_jsonable(row), ensure_ascii=False) + "\n")


def _resolve_api_key(api_key: str | None, api_key_env: str) -> str:
    key = api_key or os.environ.get(api_key_env)
    if not key:
        raise SystemExit(
            f"Missing Anthropic API key. Set ${api_key_env} or pass --api-key."
        )
    return key


def _client(api_key: str | None, api_key_env: str) -> anthropic.Anthropic:
    return anthropic.Anthropic(api_key=_resolve_api_key(api_key, api_key_env))


def _load_requests(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    requests = payload.get("requests")
    if not isinstance(requests, list) or not requests:
        raise SystemExit(f"Expected a JSON object with a non-empty 'requests' list: {path}")
    return requests


def _load_batch_id(batch_id: str | None, batch_meta: Path | None) -> str:
    if batch_id:
        return batch_id
    if batch_meta:
        payload = json.loads(batch_meta.read_text(encoding="utf-8"))
        value = payload.get("id")
        if isinstance(value, str) and value:
            return value
        raise SystemExit(f"Could not find batch id in {batch_meta}")
    raise SystemExit("Provide --batch-id or --batch-meta.")


def cmd_submit(args: argparse.Namespace) -> None:
    client = _client(args.api_key, args.api_key_env)
    requests = _load_requests(args.input)
    batch = client.messages.batches.create(requests=requests)
    batch_data = _jsonable(batch)

    meta_out = args.meta_out or (args.output_dir / f"{args.input.stem}.batch.json")
    _write_json(meta_out, batch_data)

    print(f"Submitted {len(requests)} requests from {args.input}")
    print(f"Batch id: {batch_data['id']}")
    print(f"Saved batch metadata to {meta_out}")


def cmd_status(args: argparse.Namespace) -> None:
    client = _client(args.api_key, args.api_key_env)
    batch_id = _load_batch_id(args.batch_id, args.batch_meta)
    batch = client.messages.batches.retrieve(batch_id)
    print(json.dumps(_jsonable(batch), ensure_ascii=False, indent=2))


def cmd_results(args: argparse.Namespace) -> None:
    client = _client(args.api_key, args.api_key_env)
    batch_id = _load_batch_id(args.batch_id, args.batch_meta)
    rows = list(client.messages.batches.results(batch_id))
    _write_jsonl(args.output, rows)
    print(f"Wrote {len(rows)} results to {args.output}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Submit, inspect, and download Anthropic Message Batches for Claude."
    )
    parser.add_argument(
        "--env-file",
        type=Path,
        default=DEFAULT_ENV_FILE,
        help=f"Optional local env file to preload API keys from. Default: {DEFAULT_ENV_FILE}",
    )
    parser.add_argument(
        "--api-key",
        help="Anthropic API key. Defaults to the environment variable set by --api-key-env.",
    )
    parser.add_argument(
        "--api-key-env",
        default=DEFAULT_API_KEY_ENV,
        help=f"Environment variable to read the API key from. Default: {DEFAULT_API_KEY_ENV}",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    submit = subparsers.add_parser("submit", help="Create a Claude Message Batch from a local JSON payload.")
    submit.add_argument("--input", type=Path, required=True, help="Path to the Anthropic batch JSON payload.")
    submit.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory for default metadata outputs.",
    )
    submit.add_argument(
        "--meta-out",
        type=Path,
        help="Optional path for the batch metadata JSON written after submit.",
    )
    submit.set_defaults(func=cmd_submit)

    status = subparsers.add_parser("status", help="Fetch current status for an existing batch.")
    status.add_argument("--batch-id", help="Anthropic batch id, e.g. msgbatch_...")
    status.add_argument("--batch-meta", type=Path, help="Metadata JSON created by the submit command.")
    status.set_defaults(func=cmd_status)

    results = subparsers.add_parser("results", help="Download JSONL results for a finished batch.")
    results.add_argument("--batch-id", help="Anthropic batch id, e.g. msgbatch_...")
    results.add_argument("--batch-meta", type=Path, help="Metadata JSON created by the submit command.")
    results.add_argument("--output", type=Path, required=True, help="Destination JSONL path.")
    results.set_defaults(func=cmd_results)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    load_env_file(args.env_file)
    args.func(args)


if __name__ == "__main__":
    main()
