from __future__ import annotations

from pathlib import Path

from utils.csvio import Row, read_csv
from utils.eval_scope import EVAL_SCOPE_ALL, resolve_evaluation_scope
from utils.finalize import FinalizePaths, materialize_final_dataset
from utils.helpers import group_by_paper, ordered_union
from utils.paths import (
    GROUND_TRUTH_CSV,
    LLM_DATASET_CSV,
    OUTPUTS_DIR,
    REVIEW_EVENTS_CSV,
    STATE_DIR,
)

GRANULARITY_FIELD = "granularity"
DEFAULT_MISMATCH_SUMMARY_PATH = OUTPUTS_DIR / "mismatch_summary.md"


def mismatched_papers(
    field_name: str | None = None,
    *,
    review_session_id: str = "default",
    reviewer_id: str = "anonymous",
    ground_truth_csv: str | Path | None = None,
    paper_ids: list[str] | None = None,
    eval_scope: str = EVAL_SCOPE_ALL,
) -> list[str] | dict[str, list[str]]:
    """Return papers with mismatches for one field, or a full match summary.

    When `field_name` is provided, the function returns a list of paper ids with
    at least one mistake for that field. The special field name `granularity`
    means a paper-level row-count mismatch between human and LLM datasets.

    When `field_name` is omitted, the function returns:
    - `mismatched_papers`: papers with any mismatch in any field or granularity
    - `matched_papers`: papers with no mismatches at all
    """

    ground_truth_path = (
        Path(ground_truth_csv).expanduser().resolve() if ground_truth_csv else GROUND_TRUTH_CSV
    )
    human_rows = read_csv(ground_truth_path)
    llm_rows = read_csv(LLM_DATASET_CSV)
    final_rows = materialize_final_dataset(
        FinalizePaths(
            human_csv=ground_truth_path,
            llm_csv=LLM_DATASET_CSV,
            review_events_csv=REVIEW_EVENTS_CSV,
            out_csv=STATE_DIR / "__paper_mismatches_unused__.csv",
        ),
        review_session_id=review_session_id,
        reviewer_id=reviewer_id or "anonymous",
    )
    return mismatched_papers_from_rows(
        human_rows=human_rows,
        llm_rows=llm_rows,
        final_rows=final_rows,
        field_name=field_name,
        paper_ids=paper_ids,
        eval_scope=eval_scope,
    )


def mismatch_summary(
    *,
    review_session_id: str = "default",
    reviewer_id: str = "anonymous",
    ground_truth_csv: str | Path | None = None,
    paper_ids: list[str] | None = None,
    eval_scope: str = EVAL_SCOPE_ALL,
) -> dict[str, object]:
    """Return mismatch summary data for granularity and all comparable fields."""

    ground_truth_path = (
        Path(ground_truth_csv).expanduser().resolve() if ground_truth_csv else GROUND_TRUTH_CSV
    )
    human_rows = read_csv(ground_truth_path)
    llm_rows = read_csv(LLM_DATASET_CSV)
    final_rows = materialize_final_dataset(
        FinalizePaths(
            human_csv=ground_truth_path,
            llm_csv=LLM_DATASET_CSV,
            review_events_csv=REVIEW_EVENTS_CSV,
            out_csv=STATE_DIR / "__paper_mismatches_unused__.csv",
        ),
        review_session_id=review_session_id,
        reviewer_id=reviewer_id or "anonymous",
    )
    return mismatch_summary_from_rows(
        human_rows=human_rows,
        llm_rows=llm_rows,
        final_rows=final_rows,
        review_session_id=review_session_id,
        reviewer_id=reviewer_id or "anonymous",
        ground_truth_path=ground_truth_path,
        paper_ids=paper_ids,
        eval_scope=eval_scope,
    )


def mismatched_papers_from_rows(
    *,
    human_rows: list[Row],
    llm_rows: list[Row],
    final_rows: list[Row],
    field_name: str | None = None,
    paper_ids: list[str] | None = None,
    eval_scope: str = EVAL_SCOPE_ALL,
) -> list[str] | dict[str, list[str]]:
    """Pure helper behind `mismatched_papers`, useful for tests and notebooks."""

    human_by_paper = group_by_paper(human_rows, "Filename")
    llm_by_paper = group_by_paper(llm_rows, "custom_id", strip_md=True)
    scope = resolve_evaluation_scope(
        human_rows=human_rows,
        requested_paper_ids=paper_ids,
        fallback_paper_ids=ordered_union(list(human_by_paper.keys()), list(llm_by_paper.keys())),
        eval_scope=eval_scope,
    )
    all_papers = scope.paper_ids

    granularity_mismatch_set = {
        paper_id
        for paper_id in all_papers
        if len(human_by_paper.get(paper_id, [])) != len(llm_by_paper.get(paper_id, []))
    }
    mismatch_fields = {str(row.get("field") or "").strip() for row in final_rows if row.get("field")}
    feature_scoring_papers = [paper_id for paper_id in all_papers if paper_id not in granularity_mismatch_set]

    normalized_field = _normalize_requested_field(field_name, mismatch_fields)
    if normalized_field == GRANULARITY_FIELD:
        return [paper_id for paper_id in all_papers if paper_id in granularity_mismatch_set]

    field_mismatch_set = {
        str(row.get("paper_id") or "").strip()
        for row in final_rows
        if str(row.get("field") or "").strip() == normalized_field
        and str(row.get("final_classification") or "").strip() == "mismatch"
    }

    if normalized_field:
        return [paper_id for paper_id in feature_scoring_papers if paper_id in field_mismatch_set]

    all_mismatch_set = granularity_mismatch_set | {
        str(row.get("paper_id") or "").strip()
        for row in final_rows
        if str(row.get("final_classification") or "").strip() == "mismatch"
    }
    return {
        "mismatched_papers": [paper_id for paper_id in all_papers if paper_id in all_mismatch_set],
        "matched_papers": [paper_id for paper_id in all_papers if paper_id not in all_mismatch_set],
    }


def mismatch_summary_from_rows(
    *,
    human_rows: list[Row],
    llm_rows: list[Row],
    final_rows: list[Row],
    review_session_id: str = "default",
    reviewer_id: str = "anonymous",
    ground_truth_path: Path | None = None,
    paper_ids: list[str] | None = None,
    eval_scope: str = EVAL_SCOPE_ALL,
) -> dict[str, object]:
    """Build per-field mismatch summary data from already-loaded rows."""

    human_by_paper = group_by_paper(human_rows, "Filename")
    llm_by_paper = group_by_paper(llm_rows, "custom_id", strip_md=True)
    scope = resolve_evaluation_scope(
        human_rows=human_rows,
        requested_paper_ids=paper_ids,
        fallback_paper_ids=ordered_union(list(human_by_paper.keys()), list(llm_by_paper.keys())),
        eval_scope=eval_scope,
    )
    all_papers = scope.paper_ids

    granularity_mismatch_set = {
        paper_id
        for paper_id in all_papers
        if len(human_by_paper.get(paper_id, [])) != len(llm_by_paper.get(paper_id, []))
    }
    feature_scoring_papers = [paper_id for paper_id in all_papers if paper_id not in granularity_mismatch_set]
    mismatch_fields = sorted(
        {str(row.get("field") or "").strip() for row in final_rows if str(row.get("field") or "").strip()}
    )
    overall = mismatched_papers_from_rows(
        human_rows=human_rows,
        llm_rows=llm_rows,
        final_rows=final_rows,
        field_name=None,
        paper_ids=all_papers,
        eval_scope=EVAL_SCOPE_ALL,
    )

    summary_rows: list[dict[str, object]] = []
    ordered_fields = [GRANULARITY_FIELD] + mismatch_fields
    for field_name in ordered_fields:
        mismatched = mismatched_papers_from_rows(
            human_rows=human_rows,
            llm_rows=llm_rows,
            final_rows=final_rows,
            field_name=field_name,
            paper_ids=all_papers,
            eval_scope=EVAL_SCOPE_ALL,
        )
        mismatched_list = list(mismatched)
        mismatched_set = set(mismatched_list)
        denominator_papers = all_papers if field_name == GRANULARITY_FIELD else feature_scoring_papers
        summary_rows.append(
            {
                "field": field_name,
                "mismatch_count": len(mismatched_list),
                "match_count": len(denominator_papers) - len(mismatched_list),
                "denominator_count": len(denominator_papers),
                "mismatched_papers": mismatched_list,
                "matched_papers": [paper_id for paper_id in denominator_papers if paper_id not in mismatched_set],
            }
        )

    return {
        "review_session_id": review_session_id,
        "reviewer_id": reviewer_id,
        "eval_scope": scope.mode,
        "ground_truth_path": str(ground_truth_path or ""),
        "llm_path": str(LLM_DATASET_CSV),
        "base_papers_count": len(scope.base_paper_ids),
        "total_papers": len(all_papers),
        "feature_scoring_papers_count": len(feature_scoring_papers),
        "all_papers": all_papers,
        "feature_scoring_papers": feature_scoring_papers,
        "excluded_non_lab_papers": scope.excluded_non_lab_papers,
        "overall": overall,
        "rows": summary_rows,
    }


def render_mismatch_summary_report(summary: dict[str, object]) -> str:
    """Render mismatch summary data into a markdown report."""

    overall = dict(summary.get("overall") or {})
    mismatched_overall = list(overall.get("mismatched_papers") or [])
    matched_overall = list(overall.get("matched_papers") or [])
    rows = list(summary.get("rows") or [])

    lines = [
        "# Mismatch Summary",
        "",
        f"- Review session: {summary.get('review_session_id', '')}",
        f"- Reviewer: {summary.get('reviewer_id', '')}",
        f"- Evaluation scope: {summary.get('eval_scope', '')}",
        f"- Ground truth source: {summary.get('ground_truth_path', '')}",
        f"- LLM source: {summary.get('llm_path', '')}",
        f"- Target papers for eval matrix: {summary.get('total_papers', 0)}",
        f"- Papers used for feature scoring: {summary.get('feature_scoring_papers_count', 0)}",
        f"- Papers with any mismatch: {len(mismatched_overall)}",
        f"- Papers with no mismatches: {len(matched_overall)}",
        "",
        "## Per-Field Summary",
        "",
        "| Field | Base Papers | Mismatch Count | Match Count | Mismatched Papers |",
        "|---|---:|---:|---:|---|",
    ]
    for row in rows:
        mismatched_papers = ", ".join(list(row.get("mismatched_papers") or [])) or "None"
        lines.append(
            f"| {row.get('field', '')} | {row.get('denominator_count', 0)} | {row.get('mismatch_count', 0)} | {row.get('match_count', 0)} | {mismatched_papers} |"
        )

    lines.extend(
        [
            "",
            "## Overall Paper Lists",
            "",
            f"- Papers with any mismatch: {', '.join(mismatched_overall) or 'None'}",
            f"- Papers with no mismatches: {', '.join(matched_overall) or 'None'}",
            "",
        ]
    )
    return "\n".join(lines)


def write_mismatch_summary_report(
    summary: dict[str, object],
    output_path: str | Path = DEFAULT_MISMATCH_SUMMARY_PATH,
) -> Path:
    """Write the markdown mismatch summary report and return the resolved path."""

    path = Path(output_path).expanduser().resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_mismatch_summary_report(summary), encoding="utf-8")
    return path


def _normalize_requested_field(field_name: str | None, available_fields: set[str]) -> str:
    requested = (field_name or "").strip()
    if not requested:
        return ""

    lower_map = {field.lower(): field for field in available_fields}
    lower_map[GRANULARITY_FIELD] = GRANULARITY_FIELD
    key = requested.lower()
    if key in lower_map:
        return lower_map[key]

    available = sorted(available_fields | {GRANULARITY_FIELD})
    raise ValueError(
        f"Unknown field '{field_name}'. Expected one of: {', '.join(available)}"
    )



