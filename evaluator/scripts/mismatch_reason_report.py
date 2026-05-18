from __future__ import annotations

from collections import OrderedDict
from pathlib import Path

from utils.columns import COLUMN_MAP
from utils.csvio import Row, read_csv, write_csv
from utils.eval_scope import EVAL_SCOPE_ALL, resolve_evaluation_scope
from utils.finalize import FinalizePaths, materialize_final_dataset
from utils.helpers import group_by_paper, guess_reviewer_id, md_cell, ordered_union
from utils.matching import classify_match
from utils.paths import GROUND_TRUTH_CSV, LLM_DATASET_CSV, OUTPUTS_DIR, REVIEW_EVENTS_CSV, STATE_DIR
from utils.row_alignment import align_rows, human_alignment_label, llm_alignment_label

DEFAULT_MISMATCH_REASON_MARKDOWN_PATH = OUTPUTS_DIR / "mismatch_reason_report.md"
DEFAULT_MISMATCH_REASON_CSV_PATH = OUTPUTS_DIR / "mismatch_reason_examples.csv"
GRANULARITY_FIELD = "granularity"


def build_mismatch_reason_report(
    *,
    review_session_id: str = "default",
    reviewer_id: str = "",
    ground_truth_csv: str | Path | None = None,
    paper_ids: list[str] | None = None,
    eval_scope: str = EVAL_SCOPE_ALL,
) -> dict[str, object]:
    reviewer = (reviewer_id or "").strip() or guess_reviewer_id(review_session_id)
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
            out_csv=STATE_DIR / "__mismatch_reason_report_unused__.csv",
        ),
        review_session_id=review_session_id,
        reviewer_id=reviewer,
    )
    return build_mismatch_reason_report_from_rows(
        human_rows=human_rows,
        llm_rows=llm_rows,
        final_rows=final_rows,
        review_session_id=review_session_id,
        reviewer_id=reviewer,
        ground_truth_path=ground_truth_path,
        llm_path=LLM_DATASET_CSV,
        paper_ids=paper_ids,
        eval_scope=eval_scope,
    )


def build_mismatch_reason_report_from_rows(
    *,
    human_rows: list[Row],
    llm_rows: list[Row],
    final_rows: list[Row],
    review_session_id: str = "default",
    reviewer_id: str = "anonymous",
    ground_truth_path: Path | None = None,
    llm_path: Path | None = None,
    paper_ids: list[str] | None = None,
    eval_scope: str = EVAL_SCOPE_ALL,
) -> dict[str, object]:
    human_by_paper = group_by_paper(human_rows, "Filename")
    llm_by_paper = group_by_paper(llm_rows, "custom_id", strip_md=True)
    scope = resolve_evaluation_scope(
        human_rows=human_rows,
        requested_paper_ids=paper_ids,
        fallback_paper_ids=ordered_union(list(human_by_paper.keys()), list(llm_by_paper.keys())),
        eval_scope=eval_scope,
    )
    target_papers = list(scope.paper_ids)
    granularity_mismatch_papers = [
        paper_id
        for paper_id in target_papers
        if len(human_by_paper.get(paper_id, [])) != len(llm_by_paper.get(paper_id, []))
    ]
    feature_scoring_papers = [paper_id for paper_id in target_papers if paper_id not in set(granularity_mismatch_papers)]

    aligned_context: dict[tuple[str, str], dict[str, object]] = {}
    for paper_id in feature_scoring_papers:
        pairs = align_rows(
            human_by_paper.get(paper_id, []),
            llm_by_paper.get(paper_id, []),
            column_map=COLUMN_MAP,
        )
        for row_index, (human_row, llm_row) in enumerate(pairs):
            aligned_context[(paper_id, str(row_index))] = {
                "human_exists": human_row is not None,
                "llm_exists": llm_row is not None,
                "human_label": human_alignment_label(human_row),
                "llm_label": llm_alignment_label(llm_row),
                "llm_row": llm_row,
            }

    report_rows: list[Row] = []
    for paper_id in granularity_mismatch_papers:
        report_rows.append(
            {
                "paper_id": paper_id,
                "row_index": "",
                "field": GRANULARITY_FIELD,
                "human_label": "",
                "llm_label": "",
                "human_col": "row_count",
                "llm_col": "row_count",
                "human_value": str(len(human_by_paper.get(paper_id, []))),
                "llm_value": str(len(llm_by_paper.get(paper_id, []))),
                "auto_classification": "mismatch",
                "final_classification": "mismatch",
                "mismatch_kind": "row_count_mismatch",
                "llm_reason": "",
                "llm_confidence": "",
                "paper_note": "",
            }
        )

    for row in final_rows:
        paper_id = (row.get("paper_id") or "").strip()
        row_index = (row.get("row_index") or "").strip()
        field = (row.get("field") or "").strip()
        final_classification = (row.get("final_classification") or "").strip()
        if paper_id not in feature_scoring_papers or final_classification != "mismatch":
            continue

        context = aligned_context.get((paper_id, row_index), {})
        human_exists = bool(context.get("human_exists"))
        llm_exists = bool(context.get("llm_exists"))
        llm_row = context.get("llm_row")
        llm_col = (row.get("llm_col") or "").strip()
        human_value = (row.get("human_value") or "").strip()
        llm_value = (row.get("llm_value") or "").strip()
        compare_label = "Lab / Experiment" if field == "Lab_Or_Field" else field
        detailed_auto = classify_match(
            field_label=compare_label,
            human_value=human_value,
            llm_value=llm_value,
            human_exists=human_exists,
            llm_exists=llm_exists,
        )
        mismatch_kind = (
            "review_override"
            if (row.get("auto_classification") or "").strip() != "mismatch"
            else detailed_auto
        )
        report_rows.append(
            {
                "paper_id": paper_id,
                "row_index": row_index,
                "field": field,
                "human_label": str(context.get("human_label") or ""),
                "llm_label": str(context.get("llm_label") or ""),
                "human_col": (row.get("human_col") or "").strip(),
                "llm_col": llm_col,
                "human_value": human_value,
                "llm_value": llm_value,
                "auto_classification": (row.get("auto_classification") or "").strip(),
                "final_classification": final_classification,
                "mismatch_kind": mismatch_kind,
                "llm_reason": _llm_reason(llm_row, llm_col),
                "llm_confidence": _llm_confidence(llm_row, llm_col),
                "paper_note": (row.get("paper_note") or "").strip(),
            }
        )

    field_order = [GRANULARITY_FIELD] + [field for field in COLUMN_MAP.keys() if any(r["field"] == field for r in report_rows)]
    grouped_rows: "OrderedDict[str, list[Row]]" = OrderedDict()
    for field in field_order:
        field_rows = [row for row in report_rows if row["field"] == field]
        if field_rows:
            grouped_rows[field] = field_rows

    return {
        "review_session_id": review_session_id,
        "reviewer_id": reviewer_id,
        "eval_scope": scope.mode,
        "ground_truth_path": str(ground_truth_path or ""),
        "llm_path": str(llm_path or ""),
        "base_target_papers": scope.base_paper_ids,
        "target_papers": target_papers,
        "feature_scoring_papers": feature_scoring_papers,
        "granularity_mismatch_papers": granularity_mismatch_papers,
        "excluded_non_lab_papers": scope.excluded_non_lab_papers,
        "rows": report_rows,
        "rows_by_field": grouped_rows,
    }


def render_mismatch_reason_markdown(report: dict[str, object]) -> str:
    rows = list(report.get("rows") or [])
    rows_by_field = OrderedDict(report.get("rows_by_field") or {})
    lines = [
        "# Mismatch Reason Report",
        "",
        f"- Review session: {report.get('review_session_id', '')}",
        f"- Reviewer: {report.get('reviewer_id', '')}",
        f"- Evaluation scope: {report.get('eval_scope', '')}",
        f"- Ground truth source: {report.get('ground_truth_path', '')}",
        f"- LLM source: {report.get('llm_path', '')}",
        f"- Target papers for eval matrix: {len(list(report.get('target_papers') or []))}",
        f"- Papers used for feature scoring: {len(list(report.get('feature_scoring_papers') or []))}",
        f"- Granularity-mismatch papers excluded from field examples: {', '.join(list(report.get('granularity_mismatch_papers') or [])) or 'None'}",
        f"- Total mismatch examples: {len(rows)}",
        "",
    ]
    for field, field_rows in rows_by_field.items():
        lines.extend(
            [
                f"## {field}",
                "",
                f"- Mismatch examples: {len(field_rows)}",
                "",
                "| Paper | Row | Human Label | LLM Label | Human Value | LLM Value | Mismatch Kind | LLM Reason | Confidence |",
                "|---|---:|---|---|---|---|---|---|---|",
            ]
        )
        for row in field_rows:
            lines.append(
                "| "
                + " | ".join(
                    [
                        md_cell(row.get("paper_id", "")),
                        md_cell(row.get("row_index", "")),
                        md_cell(row.get("human_label", "")),
                        md_cell(row.get("llm_label", "")),
                        md_cell(row.get("human_value", "")),
                        md_cell(row.get("llm_value", "")),
                        md_cell(row.get("mismatch_kind", "")),
                        md_cell(row.get("llm_reason", "")),
                        md_cell(row.get("llm_confidence", "")),
                    ]
                )
                + " |"
            )
        lines.append("")
    return "\n".join(lines)


def write_mismatch_reason_outputs(
    report: dict[str, object],
    *,
    markdown_out: str | Path = DEFAULT_MISMATCH_REASON_MARKDOWN_PATH,
    csv_out: str | Path = DEFAULT_MISMATCH_REASON_CSV_PATH,
) -> tuple[Path, Path]:
    markdown_path = Path(markdown_out).expanduser().resolve()
    csv_path = Path(csv_out).expanduser().resolve()
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.write_text(render_mismatch_reason_markdown(report), encoding="utf-8")
    write_csv(csv_path, list(report.get("rows") or []))
    return markdown_path, csv_path


def main(
    *,
    review_session_id: str = "default",
    reviewer_id: str = "",
    ground_truth_csv: str | None = None,
    markdown_out: str = "",
    csv_out: str = "",
    eval_scope: str = EVAL_SCOPE_ALL,
) -> tuple[Path, Path]:
    report = build_mismatch_reason_report(
        review_session_id=review_session_id,
        reviewer_id=reviewer_id,
        ground_truth_csv=ground_truth_csv,
        eval_scope=eval_scope,
    )
    return write_mismatch_reason_outputs(
        report,
        markdown_out=markdown_out or DEFAULT_MISMATCH_REASON_MARKDOWN_PATH,
        csv_out=csv_out or DEFAULT_MISMATCH_REASON_CSV_PATH,
    )



def _llm_reason(llm_row: object, llm_col: str) -> str:
    if not isinstance(llm_row, dict) or not llm_col:
        return ""
    return str((llm_row.get(f"{llm_col}_reason") or "")).strip()


def _llm_confidence(llm_row: object, llm_col: str) -> str:
    if not isinstance(llm_row, dict) or not llm_col:
        return ""
    return str((llm_row.get(f"{llm_col}_confidence") or "")).strip()



if __name__ == "__main__":
    markdown_path, csv_path = main()
    print(f"Saved mismatch reason report: {markdown_path}")
    print(f"Saved mismatch reason CSV: {csv_path}")
