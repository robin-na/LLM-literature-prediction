from __future__ import annotations

import argparse
import json
import os
import tempfile
from pathlib import Path
from typing import Any

from google import genai
from google.genai import types

try:
    from api_key_env import DEFAULT_ENV_FILE, load_env_file
except ModuleNotFoundError:
    from literature.api_key_env import DEFAULT_ENV_FILE, load_env_file

DEFAULT_OUTPUT_DIR = Path("gemini_batch_output")
DEFAULT_API_KEY_ENV = "GEMINI_API_KEY"


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
        raise SystemExit(f"Missing Gemini API key. Set ${api_key_env} or pass --api-key.")
    return key


def _client(api_key: str | None, api_key_env: str) -> genai.Client:
    return genai.Client(api_key=_resolve_api_key(api_key, api_key_env))


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


def _infer_model(rows: list[dict[str, Any]]) -> str | None:
    models = {
        str(row.get("request", {}).get("model")).strip()
        for row in rows
        if isinstance(row.get("request"), dict) and row.get("request", {}).get("model")
    }
    models.discard("")
    if not models:
        return None
    if len(models) > 1:
        raise SystemExit(f"Expected exactly one model in input JSONL, found multiple: {sorted(models)}")
    return next(iter(models))


def _normalize_rows(rows: list[dict[str, Any]], *, model: str) -> list[dict[str, Any]]:
    normalized: list[dict[str, Any]] = []
    for idx, row in enumerate(rows, start=1):
        key = row.get("key")
        request = row.get("request")
        if not isinstance(request, dict):
            raise SystemExit(f"Row {idx} is missing an object-valued 'request' field.")
        row_model = request.get("model")
        if row_model is not None and str(row_model).strip() not in {"", model}:
            raise SystemExit(
                f"Row {idx} has request.model={row_model!r}, which conflicts with resolved model {model!r}."
            )
        clean_request = {k: v for k, v in request.items() if k != "model"}
        clean_row: dict[str, Any] = {"request": clean_request}
        if key is not None:
            clean_row["key"] = key
        normalized.append(clean_row)
    return normalized


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def _load_batch_name(batch_name: str | None, batch_meta: Path | None) -> str:
    if batch_name:
        return batch_name
    if not batch_meta:
        raise SystemExit("Provide --batch-name or --batch-meta.")
    payload = json.loads(batch_meta.read_text(encoding="utf-8"))
    value = payload.get("batch_name")
    if isinstance(value, str) and value:
        return value
    batch = payload.get("batch")
    if isinstance(batch, dict):
        batch_name_value = batch.get("name")
        if isinstance(batch_name_value, str) and batch_name_value:
            return batch_name_value
    raise SystemExit(f"Could not find batch name in {batch_meta}")


def _default_meta_out(input_path: Path, output_dir: Path) -> Path:
    return output_dir / f"{input_path.stem}.batch.json"


def cmd_submit(args: argparse.Namespace) -> None:
    client = _client(args.api_key, args.api_key_env)
    rows = _load_jsonl(args.input)
    inferred_model = _infer_model(rows)
    resolved_model = args.model or inferred_model
    if not resolved_model:
        raise SystemExit(
            "Could not infer a model from the input JSONL. Pass --model explicitly."
        )

    normalized_rows = _normalize_rows(rows, model=resolved_model)
    display_name = args.display_name or args.input.stem

    with tempfile.TemporaryDirectory(prefix="gemini-batch-") as tmp_dir:
        upload_path = Path(tmp_dir) / args.input.name
        _write_jsonl(upload_path, normalized_rows)
        uploaded_file = client.files.upload(
            file=upload_path,
            config=types.UploadFileConfig(
                display_name=display_name,
                mime_type="jsonl",
            ),
        )

    batch = client.batches.create(
        model=resolved_model,
        src=uploaded_file.name,
        config={"display_name": display_name},
    )

    meta_payload = {
        "input_path": str(args.input),
        "resolved_model": resolved_model,
        "request_count": len(normalized_rows),
        "uploaded_file": _jsonable(uploaded_file),
        "uploaded_file_name": uploaded_file.name,
        "batch": _jsonable(batch),
        "batch_name": batch.name,
    }
    meta_out = args.meta_out or _default_meta_out(args.input, args.output_dir)
    _write_json(meta_out, meta_payload)

    print(f"Uploaded {len(normalized_rows)} requests from {args.input}")
    print(f"Model: {resolved_model}")
    print(f"Input file resource: {uploaded_file.name}")
    print(f"Batch name: {batch.name}")
    print(f"Saved batch metadata to {meta_out}")


def cmd_status(args: argparse.Namespace) -> None:
    client = _client(args.api_key, args.api_key_env)
    batch_name = _load_batch_name(args.batch_name, args.batch_meta)
    batch = client.batches.get(name=batch_name)
    print(json.dumps(_jsonable(batch), ensure_ascii=False, indent=2))


def cmd_results(args: argparse.Namespace) -> None:
    client = _client(args.api_key, args.api_key_env)
    batch_name = _load_batch_name(args.batch_name, args.batch_meta)
    batch = client.batches.get(name=batch_name)

    state_name = getattr(getattr(batch, "state", None), "name", None) or str(getattr(batch, "state", ""))
    if state_name != "JOB_STATE_SUCCEEDED":
        raise SystemExit(
            f"Batch {batch_name} is not finished successfully. Current state: {state_name or 'unknown'}"
        )

    result_file_name = getattr(getattr(batch, "dest", None), "file_name", None)
    if not result_file_name:
        raise SystemExit(f"Batch {batch_name} has no downloadable result file.")

    content = client.files.download(file=result_file_name)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(content)
    print(f"Downloaded result file {result_file_name}")
    print(f"Wrote {args.output}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Submit, inspect, and download Gemini Batch API jobs from local JSONL input files."
    )
    parser.add_argument(
        "--env-file",
        type=Path,
        default=DEFAULT_ENV_FILE,
        help=f"Optional local env file to preload API keys from. Default: {DEFAULT_ENV_FILE}",
    )
    parser.add_argument(
        "--api-key",
        help="Gemini API key. Defaults to the environment variable set by --api-key-env.",
    )
    parser.add_argument(
        "--api-key-env",
        default=DEFAULT_API_KEY_ENV,
        help=f"Environment variable to read the API key from. Default: {DEFAULT_API_KEY_ENV}",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    submit = subparsers.add_parser("submit", help="Upload a local JSONL and create a Gemini batch job.")
    submit.add_argument("--input", type=Path, required=True, help="Path to the Gemini batch input JSONL.")
    submit.add_argument(
        "--model",
        help="Gemini model name. If omitted, infer it from request.model in the JSONL.",
    )
    submit.add_argument(
        "--display-name",
        help="Optional Gemini batch display name. Defaults to the input stem.",
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

    status = subparsers.add_parser("status", help="Fetch current status for an existing Gemini batch.")
    status.add_argument("--batch-name", help="Gemini batch resource name, e.g. batches/123...")
    status.add_argument("--batch-meta", type=Path, help="Metadata JSON created by the submit command.")
    status.set_defaults(func=cmd_status)

    results = subparsers.add_parser("results", help="Download JSONL results for a finished Gemini batch.")
    results.add_argument("--batch-name", help="Gemini batch resource name, e.g. batches/123...")
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
