from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd

try:
    from batch_processing.agentic_workflow import (
        run_agentic_field_extraction,
        run_agentic_field_extraction_v2,
    )
    from batch_processing.build_batch_input import (
        SYSTEM_PROMPT,
        build_user_prompt as build_simple_user_prompt,
    )
    from batch_processing.extraction_schema import BASE_FIELDS, coerce_row
except ImportError:  # pragma: no cover - allows direct script execution
    from agentic_workflow import (  # type: ignore
        run_agentic_field_extraction,
        run_agentic_field_extraction_v2,
    )
    from build_batch_input import SYSTEM_PROMPT, build_user_prompt as build_simple_user_prompt  # type: ignore
    from extraction_schema import BASE_FIELDS, coerce_row  # type: ignore


DEFAULT_HYBRID_AGENTIC_FIELDS = (
    "CONFIG_playerCount",
    "CONFIG_MPCR",
    "CONFIG_allOrNothing",
    # DVs, DVs_Definitions, DV_efficiencyReported, CONFIG_showNRounds, CONFIG_showOtherSummaries
    # were evaluated with agentic extraction (hybrid_7papers_agentic5_v1.xlsx) and showed
    # no improvement vs simple extraction: DVs +3%, DVs_Definitions -12%, DV_efficiencyReported
    # 0%, CONFIG_showNRounds -27%, CONFIG_showOtherSummaries 0%. Kept out of default.
    # CONFIG_punishmentCost, CONFIG_punishmentTech, CONFIG_showPunishmentId,
    # CONFIG_defaultContribProp, CONFIG_chat were evaluated with agentic extraction
    # (hybrid_7papers_agentic5_v2.xlsx) and showed no improvement vs simple extraction:
    # all 0% delta. Kept out of default.
)


@dataclass
class HybridPaperExtractionResult:
    paper_id: str
    source_markdown: str
    rows: list[dict[str, Any]]
    metadata_rows: list[dict[str, Any]]
    simple_output: dict[str, Any]
    agentic_results: dict[str, dict[str, Any]]


@dataclass
class SimplePaperExtractionResult:
    paper_id: str
    source_markdown: str
    rows: list[dict[str, Any]]
    simple_output: dict[str, Any]


def simple_fields(agentic_fields: tuple[str, ...] = DEFAULT_HYBRID_AGENTIC_FIELDS) -> tuple[str, ...]:
    return tuple(field for field in BASE_FIELDS if field not in agentic_fields)


def resolve_paper_text(*, paper_path: str | None, paper_text: str | None) -> str:
    if bool(paper_path) == bool(paper_text):
        raise ValueError("Provide exactly one of paper_path or paper_text.")
    if paper_text is not None:
        return paper_text
    return Path(paper_path).read_text(encoding="utf-8")


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


def _agentic_merge_allowed(result: dict[str, Any]) -> bool:
    if result.get("error"):
        return False
    if result.get("agentic_version") == "v2":
        return result.get("pipeline_decision") == "accept"
    return True


def run_agentic_overrides(
    *,
    client: Any,
    model: str,
    paper_text: str,
    agentic_fields: tuple[str, ...] = DEFAULT_HYBRID_AGENTIC_FIELDS,
    max_critic_rounds: int = 1,
    max_tool_rounds: int = 8,
    continue_on_error: bool = True,
    agentic_version: str = "v2",
    min_review_confidence: float = 0.85,
    progress_callback: Any | None = None,
) -> dict[str, dict[str, Any]]:
    results: dict[str, dict[str, Any]] = {}
    for field in agentic_fields:
        try:
            if agentic_version == "v2":
                results[field] = run_agentic_field_extraction_v2(
                    client=client,
                    field=field,
                    paper_text=paper_text,
                    model=model,
                    max_critic_rounds=max_critic_rounds,
                    temperature=0.0,
                    max_tool_rounds=max_tool_rounds,
                    min_confidence=min_review_confidence,
                    progress_callback=progress_callback,
                )
            else:
                results[field] = run_agentic_field_extraction(
                    client=client,
                    field=field,
                    paper_text=paper_text,
                    model=model,
                    max_critic_rounds=max_critic_rounds,
                    temperature=0.0,
                    max_tool_rounds=max_tool_rounds,
                    progress_callback=progress_callback,
                )
        except Exception as exc:
            if not continue_on_error:
                raise
            results[field] = {
                "agentic_version": agentic_version,
                "pipeline_decision": "abstain",
                "final_output": {"experiments": []},
                "validation": {
                    "ok": False,
                    "errors": [f"agentic_error: {exc}"],
                    "warnings": [],
                },
                "critic_rounds": [],
                "error": str(exc),
            }
    return results


def make_simple_rows(custom_id: str, experiments: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [coerce_row(custom_id, experiment) for experiment in experiments if isinstance(experiment, dict)]


def run_simple_extraction_for_paper(
    *,
    client: Any,
    model: str,
    paper_id: str,
    paper_path: str,
) -> SimplePaperExtractionResult:
    source_path = Path(paper_path)
    paper_text = source_path.read_text(encoding="utf-8")
    simple_output = call_simple_extraction(client=client, model=model, paper_text=paper_text)
    experiments = simple_output.get("experiments", [])
    if not isinstance(experiments, list):
        raise ValueError(f"'experiments' was not a list for {paper_id}")

    rows = make_simple_rows(paper_id, experiments)
    for row in rows:
        row["source_markdown"] = str(source_path)

    return SimplePaperExtractionResult(
        paper_id=paper_id,
        source_markdown=str(source_path),
        rows=rows,
        simple_output=simple_output,
    )


def merge_agentic_fields_into_rows(
    *,
    simple_rows: list[dict[str, Any]],
    agentic_results: dict[str, dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    metadata_rows: list[dict[str, Any]] = []
    lookup: dict[str, list[dict[str, Any]]] = {}
    for row in simple_rows:
        lookup.setdefault(normalize_data_id(row.get("data_id")), []).append(row)

    for field, result in agentic_results.items():
        merge_field = _agentic_merge_allowed(result)
        experiments = result["final_output"].get("experiments", [])
        if merge_field:
            for experiment in experiments:
                normalized = normalize_data_id(experiment.get("data_id"))
                candidates = lookup.get(normalized, [])
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
        gate = result.get("gate_result") or {}
        metadata_rows.append(
            {
                "field": field,
                "agentic_version": result.get("agentic_version", "v1"),
                "pipeline_decision": result.get("pipeline_decision", ""),
                "merge_applied": merge_field,
                "gate_decision": gate.get("decision", ""),
                "skipped_critic": result.get("skipped_critic", False),
                "validation_ok": result["validation"]["ok"],
                "validation_errors": json.dumps(result["validation"]["errors"], ensure_ascii=False),
                "validation_warnings": json.dumps(
                    result["validation"]["warnings"], ensure_ascii=False
                ),
                "critic_round_count": len(result["critic_rounds"]),
                "agentic_error": result.get("error", ""),
            }
        )
    return simple_rows, metadata_rows


def run_hybrid_extraction_for_paper(
    *,
    client: Any,
    model: str,
    paper_id: str,
    paper_path: str,
    agentic_fields: tuple[str, ...] = DEFAULT_HYBRID_AGENTIC_FIELDS,
    max_critic_rounds: int = 1,
    max_tool_rounds: int = 8,
    continue_on_agentic_error: bool = True,
    agentic_version: str = "v2",
    min_review_confidence: float = 0.85,
    progress_callback: Any | None = None,
) -> HybridPaperExtractionResult:
    source_path = Path(paper_path)
    paper_text = source_path.read_text(encoding="utf-8")
    simple_output = call_simple_extraction(client=client, model=model, paper_text=paper_text)
    experiments = simple_output.get("experiments", [])
    if not isinstance(experiments, list):
        raise ValueError(f"'experiments' was not a list for {paper_id}")
    rows = make_simple_rows(paper_id, experiments)

    agentic_results = run_agentic_overrides(
        client=client,
        model=model,
        paper_text=paper_text,
        agentic_fields=agentic_fields,
        max_critic_rounds=max_critic_rounds,
        max_tool_rounds=max_tool_rounds,
        continue_on_error=continue_on_agentic_error,
        agentic_version=agentic_version,
        min_review_confidence=min_review_confidence,
        progress_callback=progress_callback,
    )
    merged_rows, metadata_rows = merge_agentic_fields_into_rows(
        simple_rows=rows,
        agentic_results=agentic_results,
    )
    for row in merged_rows:
        row["source_markdown"] = str(source_path)
    for item in metadata_rows:
        item["custom_id"] = paper_id
        item["source_markdown"] = str(source_path)

    return HybridPaperExtractionResult(
        paper_id=paper_id,
        source_markdown=str(source_path),
        rows=merged_rows,
        metadata_rows=metadata_rows,
        simple_output=simple_output,
        agentic_results=agentic_results,
    )


def write_hybrid_workbook(
    *,
    output_path: str,
    extraction_rows: list[dict[str, Any]],
    metadata_rows: list[dict[str, Any]],
) -> str:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(path) as writer:
        pd.DataFrame(extraction_rows).to_excel(writer, sheet_name="extractions", index=False)
        if metadata_rows:
            pd.DataFrame(metadata_rows).to_excel(writer, sheet_name="agentic_meta", index=False)
    return str(path)


def normalize_data_id(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    return " ".join(value.lower().split())
