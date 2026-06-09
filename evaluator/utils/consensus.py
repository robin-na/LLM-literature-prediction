from __future__ import annotations

import csv
from collections import OrderedDict
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from utils.columns import COLUMN_MAP as FIELD_MAP, GROUND_TRUTH_COLUMNS
from utils.csvio import Row, read_csv, write_csv
from utils.helpers import normalize_paper_id as _normalize_id
from utils.matching import classify_match
from utils.paths import (
    CONSENSUS_EVENTS_CSV,
    GROUND_TRUTH_CSV,
    HUMAN_DATASET_CSV,
    HUMAN_INPUT_DIR,
    SUPPORTED_INPUT_SUFFIXES,
)


@dataclass(frozen=True)
class AlignedPaperRow:
    paper_id: str
    row_index: int
    alignment_type: str
    rows_by_annotator: dict[str, Row | None]


@dataclass(frozen=True)
class ConsensusCell:
    key: str
    paper_id: str
    row_index: int
    field_label: str
    values_by_annotator: dict[str, str]
    auto_accepted: bool
    auto_value: str



def load_human_datasets(human_datasets_dir: Path) -> "OrderedDict[str, list[Row]]":
    csv_paths = _list_supported_dataset_files(human_datasets_dir)

    if not csv_paths and HUMAN_DATASET_CSV.exists():
        csv_paths = [HUMAN_DATASET_CSV]

    if not csv_paths:
        raise ValueError(
            "No human CSV/XLSX files found. Add one or more files under "
            f"{human_datasets_dir} (or ensure {HUMAN_DATASET_CSV} exists)."
        )
    if len(csv_paths) > 10:
        raise ValueError(f"Expected at most 10 human CSVs; found {len(csv_paths)}")

    out: "OrderedDict[str, list[Row]]" = OrderedDict()
    for path in csv_paths:
        out[path.stem] = read_csv(path)
    return out


def _list_supported_dataset_files(
    directory: Path,
    predicate: Callable[[Path], bool] | None = None,
) -> list[Path]:
    if not directory.exists():
        return []

    by_stem: dict[str, Path] = {}
    for suffix in SUPPORTED_INPUT_SUFFIXES:
        for path in directory.glob(f"*{suffix}"):
            if predicate and not predicate(path):
                continue
            existing = by_stem.get(path.stem)
            if existing is None or path.stat().st_mtime > existing.stat().st_mtime:
                by_stem[path.stem] = path
    return sorted(by_stem.values())


def group_rows_by_paper(rows: list[Row], key_col: str = "Filename") -> "OrderedDict[str, list[Row]]":
    groups: "OrderedDict[str, list[Row]]" = OrderedDict()
    for row in rows:
        paper_id = _normalize_id(row.get(key_col, ""))
        if not paper_id:
            continue
        groups.setdefault(paper_id, []).append(row)
    return groups


def align_rows_for_paper(rows_by_annotator: dict[str, list[Row]]) -> list[AlignedPaperRow]:
    # Phase 1: unique granularity matching (stable ordered union across annotators)
    granularity_unique_index: dict[str, dict[str, int]] = {}
    granularity_order: list[str] = []
    for annotator, rows in rows_by_annotator.items():
        by_granularity: dict[str, list[int]] = {}
        for idx, row in enumerate(rows):
            granularity = (row.get("Granularity") or "").strip()
            if not granularity:
                continue
            by_granularity.setdefault(granularity, []).append(idx)
        for granularity, indices in by_granularity.items():
            if len(indices) != 1:
                continue
            granularity_unique_index.setdefault(granularity, {})[annotator] = indices[0]
            if granularity not in granularity_order:
                granularity_order.append(granularity)

    consumed: dict[str, set[int]] = {annotator: set() for annotator in rows_by_annotator.keys()}
    aligned: list[AlignedPaperRow] = []
    row_index = 0
    paper_id = _infer_paper_id(rows_by_annotator)

    for granularity in granularity_order:
        entries = granularity_unique_index.get(granularity, {})
        if len(entries) < 2:
            continue
        row_map: dict[str, Row | None] = {}
        any_row = False
        for annotator, rows in rows_by_annotator.items():
            idx = entries.get(annotator)
            if idx is None or idx in consumed[annotator]:
                row_map[annotator] = None
                continue
            row_map[annotator] = rows[idx]
            consumed[annotator].add(idx)
            any_row = True
        if not any_row:
            continue
        aligned.append(
            AlignedPaperRow(
                paper_id=paper_id,
                row_index=row_index,
                alignment_type="granularity",
                rows_by_annotator=row_map,
            )
        )
        row_index += 1

    # Phase 2: fallback by row index over each annotator's remaining rows
    remaining_indices: dict[str, list[int]] = {}
    for annotator, rows in rows_by_annotator.items():
        remaining_indices[annotator] = [idx for idx in range(len(rows)) if idx not in consumed[annotator]]
    max_remaining = max((len(v) for v in remaining_indices.values()), default=0)

    for offset in range(max_remaining):
        row_map = {}
        any_row = False
        for annotator, rows in rows_by_annotator.items():
            rem = remaining_indices[annotator]
            if offset >= len(rem):
                row_map[annotator] = None
                continue
            idx = rem[offset]
            row_map[annotator] = rows[idx]
            any_row = True
        if not any_row:
            continue
        aligned.append(
            AlignedPaperRow(
                paper_id=paper_id,
                row_index=row_index,
                alignment_type="row_index",
                rows_by_annotator=row_map,
            )
        )
        row_index += 1

    return aligned


def build_consensus_cells(
    aligned_rows: list[AlignedPaperRow],
    annotators: list[str],
) -> list[ConsensusCell]:
    cells: list[ConsensusCell] = []
    for aligned in aligned_rows:
        for field_label, (human_col, _) in FIELD_MAP.items():
            values: dict[str, str] = {}
            for annotator in annotators:
                row = aligned.rows_by_annotator.get(annotator)
                values[annotator] = ((row.get(human_col) if row else "") or "").strip()

            auto_accepted = _all_values_agree(field_label, list(values.values()))
            # Explicit rule: never auto-suggest this field when all inputs are blank.
            if field_label == "Controled_Or_Observational" and all((v or "").strip() == "" for v in values.values()):
                auto_accepted = False
            auto_value = _consensus_value(list(values.values())) if auto_accepted else ""
            key = f"{aligned.paper_id}|{aligned.row_index}|{field_label}"
            cells.append(
                ConsensusCell(
                    key=key,
                    paper_id=aligned.paper_id,
                    row_index=aligned.row_index,
                    field_label=field_label,
                    values_by_annotator=values,
                    auto_accepted=auto_accepted,
                    auto_value=auto_value,
                )
            )
    return cells


def build_alignment(
    datasets_by_annotator: "OrderedDict[str, list[Row]]",
) -> tuple[list[str], list[AlignedPaperRow], list[ConsensusCell]]:
    annotators = list(datasets_by_annotator.keys())
    grouped: dict[str, dict[str, list[Row]]] = {}
    for annotator, rows in datasets_by_annotator.items():
        for paper_id, prows in group_rows_by_paper(rows).items():
            grouped.setdefault(paper_id, {})[annotator] = prows

    all_aligned: list[AlignedPaperRow] = []
    all_cells: list[ConsensusCell] = []
    for paper_id in grouped.keys():
        per_paper = {annotator: grouped[paper_id].get(annotator, []) for annotator in annotators}
        aligned_rows = align_rows_for_paper(per_paper)
        all_aligned.extend(aligned_rows)
        all_cells.extend(build_consensus_cells(aligned_rows, annotators))
    return annotators, all_aligned, all_cells


def build_consensus_state(cells: list[ConsensusCell], events: list[dict[str, str]]) -> dict[str, str]:
    by_key = {cell.key: cell for cell in cells}
    state: dict[str, str] = {}
    for cell in cells:
        if cell.auto_accepted:
            state[cell.key] = cell.auto_value

    for event in events:
        key = (event.get("key") or "").strip()
        action = (event.get("action") or "").strip()
        if not key:
            continue
        if action == "clear_ground_truth":
            state.pop(key, None)
            continue
        if action != "set_ground_truth":
            continue
        cell = by_key.get(key)
        if (
            cell
            and cell.field_label == "Controled_Or_Observational"
            and all((v or "").strip() == "" for v in cell.values_by_annotator.values())
        ):
            # Keep truly blank source cells blank, regardless of stale past selections.
            state.pop(key, None)
            continue
        value = (event.get("new_value") or "").strip()
        if value:
            state[key] = value
        else:
            state.pop(key, None)
    return state


def read_consensus_events(
    consensus_session_id: str,
    *,
    consensus_events_csv: Path = CONSENSUS_EVENTS_CSV,
) -> list[dict[str, str]]:
    """Read all consensus events for a session from the append-only log."""
    if not consensus_events_csv.exists() or consensus_events_csv.stat().st_size == 0:
        return []
    with consensus_events_csv.open("r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [dict(row) for row in reader if row.get("consensus_session_id") == consensus_session_id]


def materialize_ground_truth_rows(
    *,
    consensus_session_id: str = "default",
    human_datasets_dir: Path = HUMAN_INPUT_DIR,
    consensus_events_csv: Path = CONSENSUS_EVENTS_CSV,
) -> list[Row]:
    """Build ground-truth rows from raw human datasets and saved consensus events."""
    datasets = load_human_datasets(human_datasets_dir)
    _, aligned_rows, cells = build_alignment(datasets)
    events = read_consensus_events(
        consensus_session_id,
        consensus_events_csv=consensus_events_csv,
    )
    selections = build_consensus_state(cells, events)
    return build_ground_truth_rows(aligned_rows, cells, selections)


def export_ground_truth_csv(
    *,
    consensus_session_id: str = "default",
    human_datasets_dir: Path = HUMAN_INPUT_DIR,
    consensus_events_csv: Path = CONSENSUS_EVENTS_CSV,
    out_csv: Path = GROUND_TRUTH_CSV,
) -> Path:
    """Write the materialized ground-truth CSV and return the resolved path."""
    rows = materialize_ground_truth_rows(
        consensus_session_id=consensus_session_id,
        human_datasets_dir=human_datasets_dir,
        consensus_events_csv=consensus_events_csv,
    )
    resolved_out = out_csv.expanduser().resolve()
    resolved_out.parent.mkdir(parents=True, exist_ok=True)
    write_csv(resolved_out, rows)
    return resolved_out


def build_ground_truth_rows(
    aligned_rows: list[AlignedPaperRow],
    cells: list[ConsensusCell],
    consensus_state: dict[str, str],
) -> list[Row]:
    by_key = {cell.key: cell for cell in cells}
    out: list[Row] = []
    for aligned in aligned_rows:
        row: Row = {
            "Filename": aligned.paper_id,
            "Alignment_Label": _alignment_label_for_row(aligned),
            "Granularity": _granularity_label_for_row(aligned),
        }
        for field_label, (human_col, _) in FIELD_MAP.items():
            key = f"{aligned.paper_id}|{aligned.row_index}|{field_label}"
            value = consensus_state.get(key, "")
            if not value:
                cell = by_key.get(key)
                if cell:
                    value = cell.auto_value if cell.auto_accepted else ""
            row[human_col] = value
        out.append(row)
    return out


def _infer_paper_id(rows_by_annotator: dict[str, list[Row]]) -> str:
    for rows in rows_by_annotator.values():
        for row in rows:
            paper_id = _normalize_id(row.get("Filename", ""))
            if paper_id:
                return paper_id
    return ""


def _consensus_value(values: list[str]) -> str:
    for value in values:
        if value.strip():
            return value.strip()
    return ""


def _alignment_label_for_row(aligned: AlignedPaperRow) -> str:
    for column in ("Experiment Name", "Granularity"):
        for row in aligned.rows_by_annotator.values():
            value = ((row.get(column) if row else "") or "").strip()
            if value:
                return value
    return ""


def _granularity_label_for_row(aligned: AlignedPaperRow) -> str:
    for row in aligned.rows_by_annotator.values():
        value = ((row.get("Granularity") if row else "") or "").strip()
        if value:
            return value
    return ""


def _is_empty_like(value: str) -> bool:
    return (value or "").strip() == ""


def _all_values_agree(field_label: str, values: list[str]) -> bool:
    if len(values) <= 1:
        return True
    compare_label = "Lab / Experiment" if field_label == "Lab_Or_Field" else field_label
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            left = "" if _is_empty_like(values[i]) else values[i]
            right = "" if _is_empty_like(values[j]) else values[j]
            cls = classify_match(
                field_label=compare_label,
                human_value=left,
                llm_value=right,
                human_exists=True,
                llm_exists=True,
                compare_human_to_llm=False,
            )
            if cls not in {"match", "close"}:
                return False
    return True
