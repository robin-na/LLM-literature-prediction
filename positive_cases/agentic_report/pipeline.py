from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from typing import Any, Dict

from .column_defs import format_column_definitions
from .config import (
    ANALYSIS_MODEL,
    BASE_OUTPUT_DIR,
    CACHE_DIR,
    DATA_PATH,
    FILE_PURPOSE,
    PAPER_PATH,
    REPORT_MODEL,
    SUMMARY_MODEL,
    ensure_dirs,
)
from .prompts import (
    build_analysis_prompt,
    build_final_report_prompt,
    build_paper_summary_prompt,
)


CACHE_PATH = CACHE_DIR / "openai_artifacts.json"


def _load_cache() -> Dict[str, Any]:
    if not CACHE_PATH.exists():
        return {"files": {}, "vector_stores": {}}
    try:
        return json.loads(CACHE_PATH.read_text())
    except json.JSONDecodeError:
        return {"files": {}, "vector_stores": {}}


def _save_cache(cache: Dict[str, Any]) -> None:
    CACHE_PATH.write_text(json.dumps(cache, indent=2))


def _fingerprint(path: Path) -> Dict[str, Any]:
    stat = path.stat()
    return {"path": str(path), "mtime": stat.st_mtime, "size": stat.st_size}


def _get_or_upload_file(client, path: Path, purpose: str, cache: Dict[str, Any]) -> str:
    path = path.resolve()
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    fingerprint = _fingerprint(path)
    cache_key = str(path)
    cached = cache["files"].get(cache_key)
    if cached and cached.get("fingerprint") == fingerprint:
        return cached["file_id"]

    with path.open("rb") as f:
        file_obj = client.files.create(file=f, purpose=purpose)
    file_id = file_obj.id
    cache["files"][cache_key] = {"file_id": file_id, "fingerprint": fingerprint}
    _save_cache(cache)
    return file_id


def _get_or_create_vector_store(client, pdf_file_id: str, cache: Dict[str, Any]) -> str:
    if not hasattr(client, "vector_stores"):
        raise RuntimeError(
            "OpenAI SDK does not expose vector_stores. Please upgrade the openai package."
        )

    cache_key = str(PAPER_PATH.resolve())
    cached = cache["vector_stores"].get(cache_key)
    if cached and cached.get("file_id") == pdf_file_id:
        return cached["vector_store_id"]

    vector_store = client.vector_stores.create(name="PGG_science_paper")
    files_api = client.vector_stores.files
    create_and_poll = getattr(files_api, "create_and_poll", None)
    if callable(create_and_poll):
        create_and_poll(vector_store_id=vector_store.id, file_id=pdf_file_id)
    else:
        vs_file = files_api.create(vector_store_id=vector_store.id, file_id=pdf_file_id)
        retrieve = getattr(files_api, "retrieve", None)
        if callable(retrieve) and getattr(vs_file, "id", None):
            for _ in range(30):
                status = getattr(
                    retrieve(vector_store_id=vector_store.id, file_id=vs_file.id),
                    "status",
                    None,
                )
                if status in {"completed", "ready"}:
                    break
                time.sleep(2)

    cache["vector_stores"][cache_key] = {
        "vector_store_id": vector_store.id,
        "file_id": pdf_file_id,
    }
    _save_cache(cache)
    return vector_store.id


def _write_text(path: Path, text: str) -> None:
    path.write_text(text.strip() + "\n", encoding="utf-8")


def _extract_output_text(response) -> str:
    # OpenAI python SDK exposes output_text for convenient access.
    text = getattr(response, "output_text", None)
    if text:
        return text

    # Fallback: join text content from output items.
    parts = []
    for item in getattr(response, "output", []) or []:
        for content in getattr(item, "content", []) or []:
            if getattr(content, "type", None) == "output_text":
                parts.append(getattr(content, "text", ""))
    return "\n".join(parts).strip()


def run_pipeline(
    analysis_model: str = ANALYSIS_MODEL,
    summary_model: str = SUMMARY_MODEL,
    report_model: str = REPORT_MODEL,
    reuse_memos: bool = False,
    skip_analysis: bool = False,
    skip_paper: bool = False,
    variant: str = "both",
) -> Dict[str, Path]:
    source_mode = variant.lower().strip()
    if source_mode not in {"both", "data_only", "paper_only"}:
        source_mode = "both"

    if source_mode == "data_only":
        skip_paper = True
    elif source_mode == "paper_only":
        skip_analysis = True

    output_dir = BASE_OUTPUT_DIR / source_mode
    ensure_dirs(output_dir)

    try:
        from openai import OpenAI
    except ImportError as exc:
        raise RuntimeError(
            "openai package is not installed. Install it with `pip install openai`."
        ) from exc

    client = OpenAI()

    column_defs = format_column_definitions()
    cache = _load_cache()

    analysis_path = output_dir / "analysis_memo.md"
    paper_path = output_dir / "paper_memo.md"
    report_path = output_dir / "agentic_report.md"

    analysis_memo = ""
    paper_memo = ""

    if not skip_analysis:
        if reuse_memos and analysis_path.exists():
            analysis_memo = analysis_path.read_text(encoding="utf-8")
        else:
            data_file_id = _get_or_upload_file(client, DATA_PATH, FILE_PURPOSE, cache)
            analysis_prompt = build_analysis_prompt(column_defs)
            response = client.responses.create(
                model=analysis_model,
                input=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "input_text", "text": analysis_prompt},
                        ],
                    }
                ],
                tools=[
                    {
                        "type": "code_interpreter",
                        "container": {
                            "type": "auto",
                            "file_ids": [data_file_id],
                        },
                    }
                ],
            )
            analysis_memo = _extract_output_text(response)
            _write_text(analysis_path, analysis_memo)

    if not skip_paper:
        if reuse_memos and paper_path.exists():
            paper_memo = paper_path.read_text(encoding="utf-8")
        else:
            pdf_file_id = _get_or_upload_file(client, PAPER_PATH, FILE_PURPOSE, cache)
            vector_store_id = _get_or_create_vector_store(client, pdf_file_id, cache)
            paper_prompt = build_paper_summary_prompt()
            response = client.responses.create(
                model=summary_model,
                input=[
                    {
                        "role": "user",
                        "content": [{"type": "input_text", "text": paper_prompt}],
                    }
                ],
                tools=[
                    {
                        "type": "file_search",
                        "vector_store_ids": [vector_store_id],
                    }
                ],
            )
            paper_memo = _extract_output_text(response)
            _write_text(paper_path, paper_memo)

    if not analysis_memo:
        if source_mode != "paper_only" and analysis_path.exists():
            analysis_memo = analysis_path.read_text(encoding="utf-8")
        else:
            analysis_memo = "(analysis memo unavailable)"

    if not paper_memo:
        if source_mode != "data_only" and paper_path.exists():
            paper_memo = paper_path.read_text(encoding="utf-8")
        else:
            paper_memo = "(paper memo unavailable)"

    report_prompt = build_final_report_prompt(
        column_defs=column_defs,
        analysis_memo=analysis_memo,
        paper_memo=paper_memo,
        source_mode=source_mode,
    )

    response = client.responses.create(
        model=report_model,
        input=report_prompt,
    )
    report_text = _extract_output_text(response)
    _write_text(report_path, report_text)

    return {
        "analysis_memo": analysis_path,
        "paper_memo": paper_path,
        "report": report_path,
    }


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate an agentic prediction-support report.")
    parser.add_argument("--analysis-model", default=ANALYSIS_MODEL)
    parser.add_argument("--summary-model", default=SUMMARY_MODEL)
    parser.add_argument("--report-model", default=REPORT_MODEL)
    parser.add_argument("--reuse-memos", action="store_true", help="Reuse memo files if present.")
    parser.add_argument("--skip-analysis", action="store_true", help="Skip data analysis step.")
    parser.add_argument("--skip-paper", action="store_true", help="Skip paper summary step.")
    parser.add_argument(
        "--variant",
        default="both",
        choices=["both", "data_only", "paper_only"],
        help="Select evidence source: both, data_only, or paper_only.",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    outputs = run_pipeline(
        analysis_model=args.analysis_model,
        summary_model=args.summary_model,
        report_model=args.report_model,
        reuse_memos=args.reuse_memos,
        skip_analysis=args.skip_analysis,
        skip_paper=args.skip_paper,
        variant=args.variant,
    )
    print("Generated:")
    for name, path in outputs.items():
        print(f"- {name}: {path}")


if __name__ == "__main__":
    main()
