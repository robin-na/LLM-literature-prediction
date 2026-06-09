from __future__ import annotations

from pathlib import Path

from scripts import llm_error_analysis_report, mismatch_reason_report
from utils.eval_scope import EVAL_SCOPE_ALL
from utils.helpers import md_cell
from utils.paper_mismatches import mismatch_summary
from utils.paths import OUTPUTS_DIR

DEFAULT_MISMATCH_REPORT_MARKDOWN_PATH = OUTPUTS_DIR / "mismatch.md"
DEFAULT_MAX_EXAMPLES_PER_PATTERN = 5


def build_mismatch_report(
    *,
    review_session_id: str = "default",
    reviewer_id: str = "",
    ground_truth_csv: str | Path | None = None,
    paper_ids: list[str] | None = None,
    eval_scope: str = EVAL_SCOPE_ALL,
    max_examples_per_pattern: int = DEFAULT_MAX_EXAMPLES_PER_PATTERN,
) -> dict[str, object]:
    summary = mismatch_summary(
        review_session_id=review_session_id,
        reviewer_id=reviewer_id or "anonymous",
        ground_truth_csv=ground_truth_csv,
        paper_ids=paper_ids,
        eval_scope=eval_scope,
    )
    reasons = mismatch_reason_report.build_mismatch_reason_report(
        review_session_id=review_session_id,
        reviewer_id=reviewer_id,
        ground_truth_csv=ground_truth_csv,
        paper_ids=paper_ids,
        eval_scope=eval_scope,
    )
    analysis = llm_error_analysis_report.build_error_analysis_report_from_mismatch_report(
        reasons,
        max_examples_per_pattern=max_examples_per_pattern,
    )
    return {
        "review_session_id": review_session_id,
        "reviewer_id": reviewer_id or summary.get("reviewer_id", ""),
        "eval_scope": eval_scope,
        "summary": summary,
        "reasons": reasons,
        "analysis": analysis,
        "max_examples_per_pattern": max_examples_per_pattern,
    }


def render_mismatch_report_markdown(report: dict[str, object]) -> str:
    summary = dict(report.get("summary") or {})
    reasons = dict(report.get("reasons") or {})
    analysis = dict(report.get("analysis") or {})
    overall = dict(summary.get("overall") or {})
    summary_rows = list(summary.get("rows") or [])
    pattern_summaries = list(analysis.get("pattern_summaries") or [])
    rows_by_field = dict(reasons.get("rows_by_field") or {})

    lines = [
        "# Mismatch Report",
        "",
        f"- Review session: {report.get('review_session_id', '')}",
        f"- Reviewer: {report.get('reviewer_id', '')}",
        f"- Evaluation scope: {summary.get('eval_scope', '')}",
        f"- Ground truth source: {summary.get('ground_truth_path', '')}",
        f"- LLM source: {summary.get('llm_path', '')}",
        f"- Target papers for eval matrix: {summary.get('total_papers', 0)}",
        f"- Papers used for feature scoring: {summary.get('feature_scoring_papers_count', 0)}",
        f"- Papers with any mismatch: {len(list(overall.get('mismatched_papers') or []))}",
        f"- Papers with no mismatches: {len(list(overall.get('matched_papers') or []))}",
        "",
        "## Summary",
        "",
        "| Field | Base Papers | Mismatch Count | Match Count | Mismatched Papers |",
        "|---|---:|---:|---:|---|",
    ]
    for row in summary_rows:
        lines.append(
            f"| {row.get('field', '')} | {row.get('denominator_count', 0)} | {row.get('mismatch_count', 0)} | {row.get('match_count', 0)} | {', '.join(list(row.get('mismatched_papers') or [])) or 'None'} |"
        )

    lines.extend(
        [
            "",
            "## Error Taxonomy",
            "",
            f"- Most affected fields: {', '.join(_format_top_items(list(analysis.get('top_fields') or []))) or 'None'}",
            "",
            "| Error Pattern | Count | Top Fields | Prompt Implication |",
            "|---|---:|---|---|",
        ]
    )
    for pattern_summary in pattern_summaries:
        lines.append(
            "| "
            + " | ".join(
                [
                    md_cell(_humanize_pattern(str(pattern_summary.get("pattern") or ""))),
                    md_cell(pattern_summary.get("count", 0)),
                    md_cell(", ".join(_format_top_items(list(pattern_summary.get("top_fields") or []))) or "None"),
                    md_cell(pattern_summary.get("prompt_implication", "")),
                ]
            )
            + " |"
        )

    for pattern_summary in pattern_summaries:
        lines.extend(
            [
                "",
                f"### {_humanize_pattern(str(pattern_summary.get('pattern') or ''))}",
                "",
                f"- Count: {pattern_summary.get('count', 0)}",
                f"- Top fields: {', '.join(_format_top_items(list(pattern_summary.get('top_fields') or []))) or 'None'}",
                f"- Top papers: {', '.join(_format_top_items(list(pattern_summary.get('top_papers') or []))) or 'None'}",
                f"- Why this is wrong: {pattern_summary.get('description', '')}",
                f"- Assessment of the LLM reasoning: {pattern_summary.get('reasoning_assessment', '')}",
                f"- Prompt implication: {pattern_summary.get('prompt_implication', '')}",
                "",
                "| Field | Paper | Human Value | LLM Value | LLM Reason | Human-Grounded Correction |",
                "|---|---|---|---|---|---|",
            ]
        )
        for example in list(pattern_summary.get("examples") or []):
            lines.append(
                "| "
                + " | ".join(
                    [
                        md_cell(example.get("field", "")),
                        md_cell(example.get("paper_id", "")),
                        md_cell(example.get("human_value", "")),
                        md_cell(example.get("llm_value", "")),
                        md_cell(example.get("llm_reason", "")),
                        md_cell(example.get("human_grounded_explanation", "")),
                    ]
                )
                + " |"
            )

    lines.extend(
        [
            "",
            "## Field Examples",
            "",
            f"- Granularity-mismatch papers excluded from field examples: {', '.join(list(reasons.get('granularity_mismatch_papers') or [])) or 'None'}",
            f"- Total mismatch examples: {len(list(reasons.get('rows') or []))}",
        ]
    )

    for field, field_rows in rows_by_field.items():
        lines.extend(
            [
                "",
                f"### {field}",
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

    lines.extend(
        [
            "",
            "## Overall Paper Lists",
            "",
            f"- Papers with any mismatch: {', '.join(list(overall.get('mismatched_papers') or [])) or 'None'}",
            f"- Papers with no mismatches: {', '.join(list(overall.get('matched_papers') or [])) or 'None'}",
        ]
    )
    return "\n".join(lines)


def write_mismatch_report_markdown(
    report: dict[str, object],
    *,
    markdown_out: str | Path = DEFAULT_MISMATCH_REPORT_MARKDOWN_PATH,
) -> Path:
    markdown_path = Path(markdown_out).expanduser().resolve()
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.write_text(render_mismatch_report_markdown(report), encoding="utf-8")
    return markdown_path


def main(
    *,
    review_session_id: str = "default",
    reviewer_id: str = "",
    ground_truth_csv: str | None = None,
    markdown_out: str = "",
    eval_scope: str = EVAL_SCOPE_ALL,
    max_examples_per_pattern: int = DEFAULT_MAX_EXAMPLES_PER_PATTERN,
) -> Path:
    report = build_mismatch_report(
        review_session_id=review_session_id,
        reviewer_id=reviewer_id,
        ground_truth_csv=ground_truth_csv,
        eval_scope=eval_scope,
        max_examples_per_pattern=max_examples_per_pattern,
    )
    return write_mismatch_report_markdown(
        report,
        markdown_out=markdown_out or DEFAULT_MISMATCH_REPORT_MARKDOWN_PATH,
    )


def _humanize_pattern(value: str) -> str:
    return value.replace("_", " ")


def _format_top_items(items: list[tuple[str, int]]) -> list[str]:
    return [f"{name} ({count})" for name, count in items if name]



if __name__ == "__main__":
    markdown_path = main()
    print(f"Saved mismatch report: {markdown_path}")
