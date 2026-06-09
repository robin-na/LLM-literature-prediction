from __future__ import annotations

from collections import Counter, OrderedDict
from pathlib import Path

from scripts import mismatch_reason_report
from utils.eval_scope import EVAL_SCOPE_ALL
from utils.helpers import is_empty_like, md_cell
from utils.paths import OUTPUTS_DIR

DEFAULT_ERROR_ANALYSIS_MARKDOWN_PATH = OUTPUTS_DIR / "llm_error_analysis_report.md"
DEFAULT_MAX_EXAMPLES_PER_PATTERN = 5

PATTERN_DESCRIPTIONS: "OrderedDict[str, tuple[str, str, str]]" = OrderedDict(
    [
        (
            "unit_of_analysis_confusion",
            (
                "The LLM identified a real quantity, but counted the wrong entity (for example people instead of strategic players/teams).",
                "State explicitly whether the schema wants strategic players, teams, individuals, or total human participants. Tell the extractor to prefer the unit used by the experimental interaction, not the headcount mentioned in prose.",
                "The reasoning points to real evidence, but it maps that evidence to the wrong unit of analysis.",
            ),
        ),
        (
            "normalization_or_scale_error",
            (
                "The LLM cited a relevant number but failed to convert it into the schema's required scale or normalization.",
                "For numeric outcomes, tell the extractor to transform raw values into the schema format before writing the answer. Add reminders about per-player vs per-group, 0-1 normalization, and MPCR/per-capita conventions.",
                "The reasoning often finds the right source quantity, but the final answer keeps the wrong scale.",
            ),
        ),
        (
            "schema_zero_vs_missingness",
            (
                "The LLM treated an explicit schema zero/false as if the field were missing or inapplicable.",
                "List the fields where `0` means a meaningful negative answer, not missing data. Tell the extractor to emit `0` when the paper implies absence rather than `N/A` or blank.",
                "The reasoning confuses negative evidence with missing evidence.",
            ),
        ),
        (
            "overconservative_abstention",
            (
                "The LLM abstained even though the human coding shows the value can be inferred from the paper.",
                "Encourage derivation when the paper gives enough ingredients to compute the schema value, and require a short derivation rather than defaulting to `N/R`.",
                "The reasoning is too cautious: it demands verbatim reporting where grounded inference is acceptable.",
            ),
        ),
        (
            "hallucinated_or_overinferred_value",
            (
                "The LLM supplied a value even though the ground truth treats the field as unreported or unsupported.",
                "Tell the extractor not to estimate or fill unsupported values. When evidence is incomplete, it should leave the field unreported instead of guessing.",
                "The reasoning overreaches beyond what the paper supports.",
            ),
        ),
        (
            "field_semantics_misread",
            (
                "The LLM misunderstood what the schema field is asking for.",
                "Add short field definitions and counterexamples to the prompt so similar-looking concepts are not conflated.",
                "The reasoning uses relevant text, but for the wrong schema definition.",
            ),
        ),
        (
            "speculative_inference",
            (
                "The LLM openly estimates, approximates, or visually infers a value that the ground truth does not accept.",
                "Ban approximate reconstruction unless the prompt explicitly allows it. Prefer `N/R` over visual estimation.",
                "The reasoning itself signals low-support inference.",
            ),
        ),
        (
            "granularity_mismatch",
            (
                "The LLM extracted the wrong number of rows/conditions for the paper.",
                "Add prompt steps that enumerate conditions before filling fields, and require the extractor to reconcile its row count with the experimental conditions described in the paper.",
                "This is a row-coverage failure rather than a single-field misunderstanding.",
            ),
        ),
        (
            "value_interpretation_error",
            (
                "The LLM found partially relevant evidence but still landed on the wrong schema value.",
                "Strengthen field-specific instructions and add more worked examples for ambiguous cases.",
                "The reasoning is directionally related, but not reliable enough to reach the gold value.",
            ),
        ),
    ]
)


def build_error_analysis_report(
    *,
    review_session_id: str = "default",
    reviewer_id: str = "",
    ground_truth_csv: str | Path | None = None,
    paper_ids: list[str] | None = None,
    eval_scope: str = EVAL_SCOPE_ALL,
    max_examples_per_pattern: int = DEFAULT_MAX_EXAMPLES_PER_PATTERN,
) -> dict[str, object]:
    mismatch_report = mismatch_reason_report.build_mismatch_reason_report(
        review_session_id=review_session_id,
        reviewer_id=reviewer_id,
        ground_truth_csv=ground_truth_csv,
        paper_ids=paper_ids,
        eval_scope=eval_scope,
    )
    return build_error_analysis_report_from_mismatch_report(
        mismatch_report,
        max_examples_per_pattern=max_examples_per_pattern,
    )


def build_error_analysis_report_from_mismatch_report(
    mismatch_report: dict[str, object],
    *,
    max_examples_per_pattern: int = DEFAULT_MAX_EXAMPLES_PER_PATTERN,
) -> dict[str, object]:
    analyzed_rows = [_analyze_row(dict(row)) for row in list(mismatch_report.get("rows") or [])]
    rows_by_pattern: "OrderedDict[str, list[dict[str, object]]]" = OrderedDict()
    pattern_summaries: list[dict[str, object]] = []
    pattern_order = [
        pattern
        for pattern in PATTERN_DESCRIPTIONS.keys()
        if any(str(row.get("error_pattern") or "") == pattern for row in analyzed_rows)
    ]

    for pattern in pattern_order:
        pattern_rows = [row for row in analyzed_rows if row.get("error_pattern") == pattern]
        rows_by_pattern[pattern] = pattern_rows
        description, prompt_implication, reasoning_assessment = PATTERN_DESCRIPTIONS[pattern]
        field_counts = Counter(str(row.get("field") or "") for row in pattern_rows)
        paper_counts = Counter(str(row.get("paper_id") or "") for row in pattern_rows)
        pattern_summaries.append(
            {
                "pattern": pattern,
                "count": len(pattern_rows),
                "top_fields": _top_items(field_counts),
                "top_papers": _top_items(paper_counts),
                "description": description,
                "prompt_implication": prompt_implication,
                "reasoning_assessment": reasoning_assessment,
                "examples": pattern_rows[: max_examples_per_pattern],
            }
        )

    field_counts = Counter(str(row.get("field") or "") for row in analyzed_rows if row.get("field") != "granularity")
    return {
        "review_session_id": mismatch_report.get("review_session_id", ""),
        "reviewer_id": mismatch_report.get("reviewer_id", ""),
        "eval_scope": mismatch_report.get("eval_scope", ""),
        "ground_truth_path": mismatch_report.get("ground_truth_path", ""),
        "llm_path": mismatch_report.get("llm_path", ""),
        "target_papers": list(mismatch_report.get("target_papers") or []),
        "feature_scoring_papers": list(mismatch_report.get("feature_scoring_papers") or []),
        "granularity_mismatch_papers": list(mismatch_report.get("granularity_mismatch_papers") or []),
        "rows": analyzed_rows,
        "rows_by_pattern": rows_by_pattern,
        "pattern_summaries": pattern_summaries,
        "top_fields": _top_items(field_counts),
        "max_examples_per_pattern": max_examples_per_pattern,
    }


def render_error_analysis_markdown(report: dict[str, object]) -> str:
    rows = list(report.get("rows") or [])
    pattern_summaries = list(report.get("pattern_summaries") or [])
    lines = [
        "# LLM Error Analysis Report",
        "",
        f"- Review session: {report.get('review_session_id', '')}",
        f"- Reviewer: {report.get('reviewer_id', '')}",
        f"- Evaluation scope: {report.get('eval_scope', '')}",
        f"- Ground truth source: {report.get('ground_truth_path', '')}",
        f"- LLM source: {report.get('llm_path', '')}",
        f"- Target papers for analysis: {len(list(report.get('target_papers') or []))}",
        f"- Papers used for field-level analysis: {len(list(report.get('feature_scoring_papers') or []))}",
        f"- Total reviewed mismatch rows: {len(rows)}",
        "",
        "## Executive Summary",
        "",
        f"- Most affected fields: {', '.join(_format_top_items(list(report.get('top_fields') or []))) or 'None'}",
        "",
        "| Error Pattern | Count | Top Fields | Prompt Implication |",
        "|---|---:|---|---|",
    ]
    for summary in pattern_summaries:
        lines.append(
            "| "
            + " | ".join(
                [
                    md_cell(_humanize_pattern(str(summary.get("pattern") or ""))),
                    md_cell(summary.get("count", 0)),
                    md_cell(", ".join(_format_top_items(list(summary.get("top_fields") or []))) or "None"),
                    md_cell(summary.get("prompt_implication", "")),
                ]
            )
            + " |"
        )

    for summary in pattern_summaries:
        lines.extend(
            [
                "",
                f"## {_humanize_pattern(str(summary.get('pattern') or ''))}",
                "",
                f"- Count: {summary.get('count', 0)}",
                f"- Top fields: {', '.join(_format_top_items(list(summary.get('top_fields') or []))) or 'None'}",
                f"- Top papers: {', '.join(_format_top_items(list(summary.get('top_papers') or []))) or 'None'}",
                f"- Why this is wrong: {summary.get('description', '')}",
                f"- Assessment of the LLM reasoning: {summary.get('reasoning_assessment', '')}",
                f"- Prompt implication: {summary.get('prompt_implication', '')}",
                "",
                "| Field | Paper | Human Value | LLM Value | LLM Reason | Human-Grounded Correction |",
                "|---|---|---|---|---|---|",
            ]
        )
        for example in list(summary.get("examples") or []):
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

    return "\n".join(lines)


def write_error_analysis_markdown(
    report: dict[str, object],
    *,
    markdown_out: str | Path = DEFAULT_ERROR_ANALYSIS_MARKDOWN_PATH,
) -> Path:
    markdown_path = Path(markdown_out).expanduser().resolve()
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.write_text(render_error_analysis_markdown(report), encoding="utf-8")
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
    report = build_error_analysis_report(
        review_session_id=review_session_id,
        reviewer_id=reviewer_id,
        ground_truth_csv=ground_truth_csv,
        eval_scope=eval_scope,
        max_examples_per_pattern=max_examples_per_pattern,
    )
    return write_error_analysis_markdown(
        report,
        markdown_out=markdown_out or DEFAULT_ERROR_ANALYSIS_MARKDOWN_PATH,
    )


def _analyze_row(row: dict[str, object]) -> dict[str, object]:
    error_pattern = _infer_error_pattern(row)
    row["error_pattern"] = error_pattern
    row["human_grounded_explanation"] = _infer_human_grounded_explanation(row, error_pattern)
    row["prompt_implication"] = PATTERN_DESCRIPTIONS[error_pattern][1]
    row["llm_reason_assessment"] = PATTERN_DESCRIPTIONS[error_pattern][2]
    return row


def _infer_error_pattern(row: dict[str, object]) -> str:
    field = str(row.get("field") or "")
    human_value = str(row.get("human_value") or "").strip()
    llm_value = str(row.get("llm_value") or "").strip()
    llm_reason = str(row.get("llm_reason") or "").lower()

    if field == "granularity":
        return "granularity_mismatch"
    if _looks_speculative(llm_reason):
        return "speculative_inference"
    if is_empty_like(human_value) and not is_empty_like(llm_value):
        return "hallucinated_or_overinferred_value"
    if not is_empty_like(human_value) and is_empty_like(llm_value):
        if human_value.strip() == "0":
            return "schema_zero_vs_missingness"
        return "overconservative_abstention"
    if field == "CONFIG_playerCount" and _is_unit_of_analysis_confusion(human_value, llm_value, llm_reason):
        return "unit_of_analysis_confusion"
    if _is_normalization_or_scale_error(field, human_value, llm_value, llm_reason):
        return "normalization_or_scale_error"
    if _is_boolean_semantics_error(human_value, llm_value):
        return "field_semantics_misread"
    return "value_interpretation_error"


def _infer_human_grounded_explanation(row: dict[str, object], pattern: str) -> str:
    field = str(row.get("field") or "")
    human_value = str(row.get("human_value") or "").strip()
    llm_value = str(row.get("llm_value") or "").strip()

    if pattern == "granularity_mismatch":
        return f"The ground truth expects {human_value} rows for this paper, but the LLM produced {llm_value}."
    if pattern == "unit_of_analysis_confusion":
        return (
            f"For `{field}`, the ground truth uses `{human_value}` as the interacting player/team count, "
            f"while the LLM answered `{llm_value}` using a different headcount."
        )
    if pattern == "normalization_or_scale_error":
        return (
            f"For `{field}`, the gold value is `{human_value}` in schema format, but the LLM wrote `{llm_value}` "
            "without converting to the required scale."
        )
    if pattern == "schema_zero_vs_missingness":
        return (
            f"For `{field}`, the ground truth encodes explicit absence as `{human_value}`, so the correct output is a schema zero/false, not `{llm_value or 'blank'}`."
        )
    if pattern == "overconservative_abstention":
        return (
            f"For `{field}`, the ground truth records `{human_value}`, so the extractor should derive the value rather than abstaining with `{llm_value or 'blank'}`."
        )
    if pattern == "hallucinated_or_overinferred_value":
        return (
            f"For `{field}`, the ground truth treats the field as unreported (`{human_value or 'blank'}`), so `{llm_value}` is unsupported over-inference."
        )
    if pattern == "field_semantics_misread":
        return (
            f"For `{field}`, the schema expects `{human_value}` but the LLM gave `{llm_value}`, indicating a misunderstanding of the field definition."
        )
    if pattern == "speculative_inference":
        return (
            f"For `{field}`, the ground truth does not accept the LLM's approximation; the supported target remains `{human_value}` rather than the estimated `{llm_value}`."
        )
    return (
        f"For `{field}`, the ground truth value is `{human_value}` while the LLM output is `{llm_value}`. "
        "The cited evidence is related, but it does not justify the schema value the LLM produced."
    )


def _is_normalization_or_scale_error(field: str, human_value: str, llm_value: str, llm_reason: str) -> bool:
    human_num = _parse_float(human_value)
    llm_num = _parse_float(llm_value)
    if human_num is None or llm_num is None:
        return False
    if field in {"DV_contributionRate", "DV_efficiency", "CONFIG_defaultContribProp", "CONFIG_MPCR"}:
        if 0.0 <= human_num <= 1.0 and llm_num > 1.0:
            return True
        if any(token in llm_reason for token in ("normalize", "normalized", "out of", "per capita", "divide", "fraction")):
            return True
    return False


def _is_unit_of_analysis_confusion(human_value: str, llm_value: str, llm_reason: str) -> bool:
    human_num = _parse_float(human_value)
    llm_num = _parse_float(llm_value)
    if human_num is None or llm_num is None or human_num == 0:
        return False
    ratio = max(human_num, llm_num) / min(human_num, llm_num)
    reason_has_unit_words = any(token in llm_reason for token in ("team", "teams", "participant", "participants", "members", "humans"))
    return reason_has_unit_words or abs(ratio - round(ratio)) < 0.05


def _is_boolean_semantics_error(human_value: str, llm_value: str) -> bool:
    if is_empty_like(human_value) or is_empty_like(llm_value):
        return False
    human_bool = _to_bool(human_value)
    llm_bool = _to_bool(llm_value)
    return human_bool is not None and llm_bool is not None and human_bool != llm_bool


def _looks_speculative(reason: str) -> bool:
    lowered = (reason or "").lower()
    return any(
        token in lowered
        for token in (
            "approx",
            "approximately",
            "visual inspection",
            "estimate",
            "estimated",
            "safer to use",
            "mapping uncertain",
            "treat as",
        )
    )



def _parse_float(value: str) -> float | None:
    try:
        return float((value or "").strip())
    except ValueError:
        return None


def _to_bool(value: str) -> bool | None:
    normalized = (value or "").strip().lower()
    if normalized in {"1", "true", "yes"}:
        return True
    if normalized in {"0", "false", "no"}:
        return False
    return None


def _top_items(counter: Counter[str], *, limit: int = 3) -> list[tuple[str, int]]:
    return [(name, count) for name, count in counter.most_common(limit) if name]


def _format_top_items(items: list[tuple[str, int]]) -> list[str]:
    return [f"{name} ({count})" for name, count in items if name]


def _humanize_pattern(value: str) -> str:
    return value.replace("_", " ")



if __name__ == "__main__":
    markdown_path = main()
    print(f"Saved error analysis report: {markdown_path}")
