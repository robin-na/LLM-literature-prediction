from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from typing import Any, Dict

from .column_defs import (
    format_column_definitions,
    format_prediction_task_column_definitions,
)
from .config import (
    ANALYSIS_MODEL,
    BASE_OUTPUT_DIR,
    CACHE_DIR,
    DATA_PATH,
    DEFAULT_LITERATURE_VECTOR_STORE_ID,
    FILE_PURPOSE,
    LITERATURE_CACHE_DIR,
    LITERATURE_OUTPUT_DIR,
    REPORT_MODEL,
    SUMMARY_MODEL,
    ensure_dirs,
    resolve_paper_paths,
)
from .prompts import (
    build_analysis_prompt,
    build_final_report_prompt,
    build_paper_retrieval_report_prompt,
    build_report_ensemble_prompt,
    build_paper_summary_prompt,
    build_report_refinement_prompt,
)

FILE_SEARCH_MAX_NUM_RESULTS = 50

REPORT_METHOD_SPECS = {
    "paper_only_freeform": {"source_mode": "paper_only", "report_style": "freeform"},
    "paper_only_narrative": {
        "source_mode": "paper_only",
        "report_style": "narrative",
        "generation_mode": "paper_search_direct",
    },
    "data_only_freeform": {"source_mode": "data_only", "report_style": "freeform"},
    "both_freeform": {"source_mode": "both", "report_style": "freeform"},
    "paper_only_structured": {"source_mode": "paper_only", "report_style": "structured"},
    "paper_only_decision": {
        "source_mode": "paper_only",
        "report_style": "decision",
        "generation_mode": "paper_search_direct",
    },
    "data_only_structured": {"source_mode": "data_only", "report_style": "structured"},
    "both_structured": {"source_mode": "both", "report_style": "structured"},
    "paper_only_quantitative": {"source_mode": "paper_only", "report_style": "quantitative"},
    "data_only_quantitative": {"source_mode": "data_only", "report_style": "quantitative"},
    "both_quantitative": {"source_mode": "both", "report_style": "quantitative"},
    "both_rules": {"source_mode": "both", "report_style": "rules"},
    "both_contrastive": {"source_mode": "both", "report_style": "contrastive"},
    "both_uncertainty": {"source_mode": "both", "report_style": "uncertainty"},
    "both_refined": {"source_mode": "both", "report_style": "refined"},
    "both_ensemble": {"source_mode": "both", "report_style": "ensemble"},
}


def parse_report_method(report_method: str) -> dict[str, str]:
    method = report_method.lower().strip()
    if method not in REPORT_METHOD_SPECS:
        raise ValueError(
            f"Unsupported report method '{report_method}'. "
            f"Expected one of: {', '.join(sorted(REPORT_METHOD_SPECS))}"
        )
    return REPORT_METHOD_SPECS[method]


def canonical_output_dir_name(source_mode: str, report_style: str) -> str:
    if report_style == "freeform" and source_mode in {"both", "data_only", "paper_only"}:
        return source_mode
    return f"{source_mode}_{report_style}"


def _load_cache(cache_path: Path) -> Dict[str, Any]:
    if not cache_path.exists():
        return {"files": {}, "vector_stores": {}}
    try:
        return json.loads(cache_path.read_text())
    except json.JSONDecodeError:
        return {"files": {}, "vector_stores": {}}


def _save_cache(cache: Dict[str, Any], cache_path: Path) -> None:
    cache_path.write_text(json.dumps(cache, indent=2))


def _fingerprint(path: Path) -> Dict[str, Any]:
    stat = path.stat()
    return {"path": str(path), "mtime": stat.st_mtime, "size": stat.st_size}


def _get_or_upload_file(
    client,
    path: Path,
    purpose: str,
    cache: Dict[str, Any],
    cache_path: Path,
) -> str:
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
    _save_cache(cache, cache_path)
    return file_id


def _get_or_create_vector_store(
    client,
    paper_paths: list[Path],
    pdf_file_ids: list[str],
    cache: Dict[str, Any],
    cache_path: Path,
) -> str:
    if not hasattr(client, "vector_stores"):
        raise RuntimeError(
            "OpenAI SDK does not expose vector_stores. Please upgrade the openai package."
        )

    cache_key = "||".join(str(path.resolve()) for path in paper_paths)
    cached = cache["vector_stores"].get(cache_key)
    if cached and cached.get("file_ids") == pdf_file_ids:
        return cached["vector_store_id"]

    vector_store = client.vector_stores.create(name="PGG_science_papers")
    files_api = client.vector_stores.files
    create_and_poll = getattr(files_api, "create_and_poll", None)
    for pdf_file_id in pdf_file_ids:
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
        "file_ids": pdf_file_ids,
    }
    _save_cache(cache, cache_path)
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


def _response_to_dict(response) -> Dict[str, Any]:
    model_dump = getattr(response, "model_dump", None)
    if callable(model_dump):
        return model_dump()
    to_dict = getattr(response, "to_dict", None)
    if callable(to_dict):
        return to_dict()
    if isinstance(response, dict):
        return response
    return {"id": getattr(response, "id", None), "output": getattr(response, "output", None)}


def _extract_file_search_log(response_payload: Dict[str, Any], prompt_text: str) -> Dict[str, Any]:
    output_items = response_payload.get("output") or []
    calls = []
    for item in output_items:
        if item.get("type") != "file_search_call":
            continue
        calls.append(
            {
                "id": item.get("id"),
                "status": item.get("status"),
                "queries": item.get("queries"),
                "results": item.get("results", item.get("search_results")),
            }
        )
    return {
        "response_id": response_payload.get("id"),
        "prompt_text": prompt_text,
        "file_search_calls": calls,
    }


def _write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def run_pipeline(
    analysis_model: str = ANALYSIS_MODEL,
    summary_model: str = SUMMARY_MODEL,
    report_model: str = REPORT_MODEL,
    reuse_memos: bool = False,
    skip_analysis: bool = False,
    skip_paper: bool = False,
    variant: str = "both",
    report_style: str = "freeform",
    report_method: str | None = None,
    vector_store_id: str | None = None,
    output_root: Path | None = None,
    cache_dir: Path | None = None,
) -> Dict[str, Path]:
    generation_mode = "memo_then_report"
    if report_method is not None:
        spec = parse_report_method(report_method)
        source_mode = spec["source_mode"]
        report_style = spec["report_style"]
        generation_mode = spec.get("generation_mode", generation_mode)
    else:
        source_mode = variant.lower().strip()
        report_style = report_style.lower().strip()

    if source_mode not in {"both", "data_only", "paper_only"}:
        source_mode = "both"
    if report_style not in {
        "freeform",
        "structured",
        "quantitative",
        "narrative",
        "decision",
        "rules",
        "contrastive",
        "uncertainty",
        "refined",
        "ensemble",
    }:
        report_style = "freeform"

    if source_mode == "data_only":
        skip_paper = True
    elif source_mode == "paper_only":
        skip_analysis = True

    if output_root is None:
        output_root = BASE_OUTPUT_DIR
        if report_method in {"paper_only_narrative", "paper_only_decision"}:
            output_root = LITERATURE_OUTPUT_DIR
    if cache_dir is None:
        cache_dir = CACHE_DIR
        if report_method in {"paper_only_narrative", "paper_only_decision"}:
            cache_dir = LITERATURE_CACHE_DIR

    output_dir = output_root / canonical_output_dir_name(source_mode, report_style)
    ensure_dirs(output_dir, cache_dir)
    cache_path = cache_dir / "openai_artifacts.json"

    try:
        from openai import OpenAI
    except ImportError as exc:
        raise RuntimeError(
            "openai package is not installed. Install it with `pip install openai`."
        ) from exc

    client = OpenAI()

    column_defs = format_column_definitions()
    cache = _load_cache(cache_path)

    analysis_path = output_dir / "analysis_memo.md"
    paper_path = output_dir / "paper_memo.md"
    report_path = output_dir / "agentic_report.md"
    prompt_path = output_dir / "report_generation_prompt.md"
    retrieval_log_path = output_dir / "file_search_log.json"

    analysis_memo = ""
    paper_memo = ""

    def resolve_vector_store_id() -> str:
        if vector_store_id:
            return vector_store_id
        paper_paths = resolve_paper_paths()
        pdf_file_ids = [
            _get_or_upload_file(client, paper_pdf_path, FILE_PURPOSE, cache, cache_path)
            for paper_pdf_path in paper_paths
        ]
        return _get_or_create_vector_store(client, paper_paths, pdf_file_ids, cache, cache_path)

    if generation_mode == "paper_search_direct":
        active_vector_store_id = resolve_vector_store_id()
        report_prompt = build_paper_retrieval_report_prompt(
            column_defs=format_prediction_task_column_definitions(),
            report_style=report_style,
        )
        _write_text(prompt_path, report_prompt)
        response = client.responses.create(
            model=report_model,
            input=[
                {
                    "role": "user",
                    "content": [{"type": "input_text", "text": report_prompt}],
                }
            ],
            tools=[
                {
                    "type": "file_search",
                    "vector_store_ids": [active_vector_store_id],
                    "max_num_results": FILE_SEARCH_MAX_NUM_RESULTS,
                }
            ],
            include=["file_search_call.results"],
        )
        _write_json(
            retrieval_log_path,
            _extract_file_search_log(_response_to_dict(response), report_prompt),
        )
        report_text = _extract_output_text(response)
        _write_text(report_path, report_text)
        return {
            "analysis_memo": analysis_path,
            "paper_memo": paper_path,
            "report_prompt": prompt_path,
            "file_search_log": retrieval_log_path,
            "report": report_path,
        }

    if not skip_analysis:
        if reuse_memos and analysis_path.exists():
            analysis_memo = analysis_path.read_text(encoding="utf-8")
        else:
            data_file_id = _get_or_upload_file(client, DATA_PATH, FILE_PURPOSE, cache, cache_path)
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
            active_vector_store_id = resolve_vector_store_id()
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
                        "vector_store_ids": [active_vector_store_id],
                        "max_num_results": FILE_SEARCH_MAX_NUM_RESULTS,
                    }
                ],
                include=["file_search_call.results"],
            )
            _write_json(
                retrieval_log_path,
                _extract_file_search_log(_response_to_dict(response), paper_prompt),
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

    if report_style == "refined":
        draft_prompt = build_final_report_prompt(
            column_defs=column_defs,
            analysis_memo=analysis_memo,
            paper_memo=paper_memo,
            source_mode=source_mode,
            report_style="freeform",
        )
        draft_response = client.responses.create(
            model=report_model,
            input=draft_prompt,
        )
        draft_report = _extract_output_text(draft_response)
        refinement_prompt = build_report_refinement_prompt(
            column_defs=column_defs,
            analysis_memo=analysis_memo,
            paper_memo=paper_memo,
            draft_report=draft_report,
            source_mode=source_mode,
        )
        response = client.responses.create(
            model=report_model,
            input=refinement_prompt,
        )
        report_text = _extract_output_text(response)
    elif report_style == "ensemble":
        structured_prompt = build_final_report_prompt(
            column_defs=column_defs,
            analysis_memo=analysis_memo,
            paper_memo=paper_memo,
            source_mode=source_mode,
            report_style="structured",
        )
        quantitative_prompt = build_final_report_prompt(
            column_defs=column_defs,
            analysis_memo=analysis_memo,
            paper_memo=paper_memo,
            source_mode=source_mode,
            report_style="quantitative",
        )
        structured_response = client.responses.create(
            model=report_model,
            input=structured_prompt,
        )
        quantitative_response = client.responses.create(
            model=report_model,
            input=quantitative_prompt,
        )
        structured_draft = _extract_output_text(structured_response)
        quantitative_draft = _extract_output_text(quantitative_response)
        ensemble_prompt = build_report_ensemble_prompt(
            column_defs=column_defs,
            analysis_memo=analysis_memo,
            paper_memo=paper_memo,
            structured_draft=structured_draft,
            quantitative_draft=quantitative_draft,
            source_mode=source_mode,
        )
        response = client.responses.create(
            model=report_model,
            input=ensemble_prompt,
        )
        report_text = _extract_output_text(response)
    else:
        report_prompt = build_final_report_prompt(
            column_defs=column_defs,
            analysis_memo=analysis_memo,
            paper_memo=paper_memo,
            source_mode=source_mode,
            report_style=report_style,
        )
        _write_text(prompt_path, report_prompt)
        response = client.responses.create(
            model=report_model,
            input=report_prompt,
        )
        report_text = _extract_output_text(response)
    _write_text(report_path, report_text)

    return {
        "analysis_memo": analysis_path,
        "paper_memo": paper_path,
        "report_prompt": prompt_path,
        "file_search_log": retrieval_log_path,
        "report": report_path,
    }


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate an agentic prediction-support report.")
    parser.add_argument("--analysis-model", default=ANALYSIS_MODEL)
    parser.add_argument("--summary-model", default=SUMMARY_MODEL)
    parser.add_argument("--report-model", default=REPORT_MODEL)
    parser.add_argument(
        "--output-root",
        type=Path,
        default=None,
        help=(
            "Root directory for generated outputs. Defaults to literature/output for "
            "the direct literature report methods, otherwise positive_cases/output."
        ),
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=None,
        help=(
            "Directory for cached OpenAI file/vector-store ids. Defaults to "
            "literature/.cache for the direct literature report methods, otherwise "
            "positive_cases/.cache."
        ),
    )
    parser.add_argument(
        "--vector-store-id",
        default=DEFAULT_LITERATURE_VECTOR_STORE_ID,
        help=(
            "Existing vector store id for paper retrieval. Defaults to the stored "
            "eligible-literature vector store."
        ),
    )
    parser.add_argument("--reuse-memos", action="store_true", help="Reuse memo files if present.")
    parser.add_argument("--skip-analysis", action="store_true", help="Skip data analysis step.")
    parser.add_argument("--skip-paper", action="store_true", help="Skip paper summary step.")
    parser.add_argument(
        "--variant",
        default="both",
        choices=["both", "data_only", "paper_only"],
        help="Select evidence source: both, data_only, or paper_only.",
    )
    parser.add_argument(
        "--report-style",
        default="freeform",
        choices=[
            "freeform",
            "structured",
            "quantitative",
            "rules",
            "contrastive",
            "uncertainty",
            "refined",
            "ensemble",
        ],
        help="Report synthesis style.",
    )
    parser.add_argument(
        "--report-method",
        default=None,
        choices=sorted(REPORT_METHOD_SPECS),
        help="Named report method shortcut.",
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
        report_style=args.report_style,
        report_method=args.report_method,
        vector_store_id=args.vector_store_id,
        output_root=args.output_root,
        cache_dir=args.cache_dir,
    )
    print("Generated:")
    for name, path in outputs.items():
        print(f"- {name}: {path}")


if __name__ == "__main__":
    main()
