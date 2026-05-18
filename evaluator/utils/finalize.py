from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

from utils.columns import COLUMN_MAP
from utils.csvio import Row, read_csv, write_csv
from utils.helpers import group_by_paper, ordered_union
from utils.matching import classify_match
from utils.review_state import build_classification_overrides, build_paper_notes
from utils.row_alignment import align_rows


@dataclass(frozen=True)
class FinalizePaths:
    """Filesystem inputs/outputs for final dataset materialization."""

    human_csv: Path
    llm_csv: Path
    review_events_csv: Path
    out_csv: Path


def read_review_events(review_events_csv: Path, review_session_id: str) -> list[dict[str, str]]:
    """Read review events for a single session from the event log CSV."""
    if not review_events_csv.exists():
        return []

    review_session_id = (review_session_id or "").strip()
    out: list[dict[str, str]] = []
    with review_events_csv.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if (row.get("review_session_id") or "").strip() != review_session_id:
                continue
            out.append({k: (v or "") for k, v in row.items()})
    return out


def materialize_final_dataset(
    paths: FinalizePaths, *, review_session_id: str, reviewer_id: str
) -> list[Row]:
    """Build a field-level 'final dataset' enriched with review annotations."""
    events = read_review_events(paths.review_events_csv, review_session_id)
    overrides_ui = build_classification_overrides(events)
    notes = build_paper_notes(events, reviewer_id=reviewer_id)
    return build_final_rows(
        human_rows=list(read_csv(paths.human_csv)),
        llm_rows=list(read_csv(paths.llm_csv)),
        overrides_ui=overrides_ui,
        notes=notes,
        review_session_id=review_session_id,
        reviewer_id=reviewer_id,
    )


def write_final_dataset(rows: list[Row], out_csv: Path) -> None:
    """Write the final dataset rows as a CSV file."""
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    write_csv(out_csv, rows)


def build_final_rows(
    *,
    human_rows: list[Row],
    llm_rows: list[Row],
    overrides_ui: dict[str, str],
    notes: dict[str, str],
    review_session_id: str,
    reviewer_id: str,
) -> list[Row]:
    """Build final dataset rows from already-loaded CSV rows and materialized state."""
    human_by_paper = group_by_paper(human_rows, "Filename")
    llm_by_paper = group_by_paper(llm_rows, "custom_id", strip_md=True)

    paper_ids = ordered_union(list(human_by_paper.keys()), list(llm_by_paper.keys()))
    out: list[Row] = []
    for paper_id in paper_ids:
        out.extend(
            _build_final_rows_for_paper(
                paper_id=paper_id,
                human_rows=human_by_paper.get(paper_id, []),
                llm_rows=llm_by_paper.get(paper_id, []),
                overrides_ui=overrides_ui,
                note=notes.get(paper_id, ""),
                review_session_id=review_session_id,
                reviewer_id=reviewer_id,
            )
        )
    return out


def _build_final_rows_for_paper(
    *,
    paper_id: str,
    human_rows: list[Row],
    llm_rows: list[Row],
    overrides_ui: dict[str, str],
    note: str,
    review_session_id: str,
    reviewer_id: str,
) -> list[Row]:
    out: list[Row] = []
    note_emitted = False
    for row_index, pair in enumerate(_pair_rows(human_rows, llm_rows)):
        for field_label, cols in COLUMN_MAP.items():
            emit_note = note if (not note_emitted) else ""
            note_emitted = True
            out.append(
                _build_cell_row(
                    paper_id=paper_id,
                    row_index=row_index,
                    field_label=field_label,
                    human_col=cols[0],
                    llm_col=cols[1],
                    pair=pair,
                    overrides_ui=overrides_ui,
                    note=emit_note,
                    review_session_id=review_session_id,
                    reviewer_id=reviewer_id,
                )
            )
    return out


def _build_cell_row(
    *,
    paper_id: str,
    row_index: int,
    field_label: str,
    human_col: str,
    llm_col: str,
    pair: tuple[Row | None, Row | None, bool, bool],
    overrides_ui: dict[str, str],
    note: str,
    review_session_id: str,
    reviewer_id: str,
) -> Row:
    h_row, l_row, human_exists, llm_exists = pair
    key = _make_key(paper_id, row_index, field_label)
    h_val, l_val = _get_cell_values(h_row, l_row, human_col=human_col, llm_col=llm_col)
    compare_label = "Lab / Experiment" if field_label == "Lab_Or_Field" else field_label
    auto_cls = classify_match(
        field_label=compare_label,
        human_value=h_val,
        llm_value=l_val,
        human_exists=human_exists,
        llm_exists=llm_exists,
    )
    auto_cls = _canon_stage2_classification(auto_cls)
    final_cls = _final_classification(auto_cls, overrides_ui.get(key, ""))
    return {
        "review_session_id": review_session_id,
        "reviewer_id": reviewer_id,
        "key": key,
        "paper_id": paper_id,
        "row_index": str(row_index),
        "field": field_label,
        "human_col": human_col,
        "llm_col": llm_col,
        "human_value": h_val,
        "llm_value": l_val,
        "auto_classification": auto_cls,
        "final_classification": final_cls,
        "paper_note": note,
    }


def _get_cell_values(h_row: Row | None, l_row: Row | None, *, human_col: str, llm_col: str) -> tuple[str, str]:
    h_val = (h_row.get(human_col, "") if h_row else "") or ""
    l_val = (l_row.get(llm_col, "") if l_row else "") or ""
    return str(h_val), str(l_val)


def _final_classification(auto_cls: str, override_ui: str) -> str:
    override_ui = (override_ui or "").strip()
    return _canon_classification(override_ui) if override_ui else auto_cls


def _canon_classification(value: str) -> str:
    return _canon_stage2_classification(value)


def _canon_stage2_classification(value: str) -> str:
    value = (value or "").strip().replace("-", "_")
    if value in {"match", "close", "both_empty"}:
        return "match"
    if value in {"mismatch", "one_empty", "missing_row"}:
        return "mismatch"
    return value


def _pair_rows(human_rows: list[Row], llm_rows: list[Row]) -> list[tuple[Row | None, Row | None, bool, bool]]:
    return [(h, l, h is not None, l is not None) for h, l in align_rows(human_rows, llm_rows, column_map=COLUMN_MAP)]


def _make_key(paper_id: str, row_index: int, field_label: str) -> str:
    return f"{paper_id}|{row_index}|{field_label}"



