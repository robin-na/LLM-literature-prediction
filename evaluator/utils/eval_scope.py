from __future__ import annotations

from dataclasses import dataclass

from utils.csvio import Row
from utils.helpers import ordered_union as _ordered_union

EVAL_SCOPE_ALL = "all"
EVAL_SCOPE_LAB_ONLY = "lab-only"
VALID_EVAL_SCOPES: tuple[str, ...] = (EVAL_SCOPE_ALL, EVAL_SCOPE_LAB_ONLY)

DEFAULT_TARGET_PAPERS: list[str] = [
    "10.1007_s10645-008-9094-1",
    "10.1177_0146167216684134",
    "10.1016_j.jpubeco.2015.12.012",
    "10.1007_s10640-025-00970-6",
    "10.3390_g14050065",
    "10.1111_apce.12343",
    "10.1016_j.evolhumbehav.2006.06.001",
    "10.1016_j.chieco.2022.101826",
    "10.1111_j.1468-0351.2005.00228.x",
]


@dataclass(frozen=True)
class EvaluationScope:
    mode: str
    base_paper_ids: list[str]
    paper_ids: list[str]
    excluded_non_lab_papers: list[str]


def default_target_papers() -> list[str]:
    return list(DEFAULT_TARGET_PAPERS)


def resolve_evaluation_scope(
    *,
    human_rows: list[Row],
    requested_paper_ids: list[str] | None = None,
    fallback_paper_ids: list[str] | None = None,
    eval_scope: str = EVAL_SCOPE_ALL,
) -> EvaluationScope:
    normalized_scope = normalize_eval_scope(eval_scope)
    if requested_paper_ids is not None:
        base_paper_ids = _ordered_union(list(requested_paper_ids), [])
    else:
        base_paper_ids = default_target_papers() or _ordered_union(list(fallback_paper_ids or []), [])

    if normalized_scope == EVAL_SCOPE_ALL:
        return EvaluationScope(
            mode=normalized_scope,
            base_paper_ids=base_paper_ids,
            paper_ids=base_paper_ids,
            excluded_non_lab_papers=[],
        )

    lab_paper_ids = set(lab_experiment_papers(human_rows))
    paper_ids = [paper_id for paper_id in base_paper_ids if paper_id in lab_paper_ids]
    excluded_non_lab_papers = [paper_id for paper_id in base_paper_ids if paper_id not in lab_paper_ids]
    return EvaluationScope(
        mode=normalized_scope,
        base_paper_ids=base_paper_ids,
        paper_ids=paper_ids,
        excluded_non_lab_papers=excluded_non_lab_papers,
    )


def normalize_eval_scope(eval_scope: str) -> str:
    normalized = (eval_scope or "").strip().lower()
    if normalized in VALID_EVAL_SCOPES:
        return normalized
    raise ValueError(
        f"Unknown eval scope '{eval_scope}'. Expected one of: {', '.join(VALID_EVAL_SCOPES)}"
    )


def lab_experiment_papers(human_rows: list[Row]) -> list[str]:
    grouped: dict[str, list[Row]] = {}
    for row in human_rows:
        paper_id = (row.get("Filename") or "").strip()
        if paper_id:
            grouped.setdefault(paper_id, []).append(row)
    return [paper_id for paper_id, rows in grouped.items() if _paper_has_lab_row(rows)]


def _paper_has_lab_row(rows: list[Row]) -> bool:
    return any(_is_lab_experiment_value((row.get("Lab_Or_Field") or "").strip()) for row in rows)


def _is_lab_experiment_value(value: str) -> bool:
    normalized = (value or "").strip().lower()
    if normalized in {"0", "false", "lab", "laboratory"}:
        return True
    try:
        return float(normalized) == 0.0
    except ValueError:
        return False


