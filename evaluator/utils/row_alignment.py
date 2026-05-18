from __future__ import annotations

import re
from functools import lru_cache
from typing import Mapping

from utils.csvio import Row
from utils.matching import classify_match

Pair = tuple[Row | None, Row | None]

_GENERIC_LABEL_TOKENS = {
    "a",
    "an",
    "and",
    "baseline",
    "condition",
    "conditions",
    "control",
    "experiment",
    "experiments",
    "group",
    "groups",
    "part",
    "phase",
    "row",
    "scheme",
    "study",
    "treatment",
}

_CLASS_SCORE = {
    "match": 3.0,
    "close": 2.5,
    "mismatch": -1.5,
    "one_empty": -2.0,
    "both_empty": 0.05,
    "missing_row": -3.0,
}

_HUMAN_LABEL_COLUMNS = ("Alignment_Label", "Experiment Name", "Granularity")
_LLM_LABEL_COLUMNS = ("data_id", "v")


def align_rows(
    human_rows: list[Row],
    llm_rows: list[Row],
    *,
    column_map: Mapping[str, tuple[str, str]],
) -> list[Pair]:
    """Align Stage 2 rows by best semantic match while preserving human order."""

    if not human_rows and not llm_rows:
        return []
    if not human_rows:
        return [(None, row) for row in llm_rows]
    if not llm_rows:
        return [(row, None) for row in human_rows]

    scores = [
        [_pair_score(h_row, l_row, column_map=column_map) for l_row in llm_rows]
        for h_row in human_rows
    ]

    if len(human_rows) == len(llm_rows):
        return _align_rows_force_bijection(human_rows, llm_rows, scores)

    @lru_cache(maxsize=None)
    def best_score(h_idx: int, used_mask: int) -> float:
        if h_idx >= len(human_rows):
            return 0.0

        best = best_score(h_idx + 1, used_mask)
        for l_idx in range(len(llm_rows)):
            if used_mask & (1 << l_idx):
                continue
            candidate = scores[h_idx][l_idx] + best_score(h_idx + 1, used_mask | (1 << l_idx))
            if candidate > best:
                best = candidate
        return best

    pairs: list[Pair] = []
    used_mask = 0
    for h_idx, h_row in enumerate(human_rows):
        skip_score = best_score(h_idx + 1, used_mask)
        chosen_l_idx: int | None = None
        chosen_total = skip_score
        for l_idx in range(len(llm_rows)):
            if used_mask & (1 << l_idx):
                continue
            candidate = scores[h_idx][l_idx] + best_score(h_idx + 1, used_mask | (1 << l_idx))
            if candidate > chosen_total:
                chosen_total = candidate
                chosen_l_idx = l_idx
        if chosen_l_idx is None:
            pairs.append((h_row, None))
            continue
        used_mask |= 1 << chosen_l_idx
        pairs.append((h_row, llm_rows[chosen_l_idx]))

    for l_idx, l_row in enumerate(llm_rows):
        if used_mask & (1 << l_idx):
            continue
        pairs.append((None, l_row))
    return pairs


def _align_rows_force_bijection(
    human_rows: list[Row],
    llm_rows: list[Row],
    scores: list[list[float]],
) -> list[Pair]:
    @lru_cache(maxsize=None)
    def best_score(h_idx: int, used_mask: int) -> float:
        if h_idx >= len(human_rows):
            return 0.0

        best = float("-inf")
        for l_idx in range(len(llm_rows)):
            if used_mask & (1 << l_idx):
                continue
            candidate = scores[h_idx][l_idx] + best_score(h_idx + 1, used_mask | (1 << l_idx))
            if candidate > best:
                best = candidate
        return best

    pairs: list[Pair] = []
    used_mask = 0
    for h_idx, h_row in enumerate(human_rows):
        chosen_l_idx: int | None = None
        chosen_total = float("-inf")
        for l_idx in range(len(llm_rows)):
            if used_mask & (1 << l_idx):
                continue
            candidate = scores[h_idx][l_idx] + best_score(h_idx + 1, used_mask | (1 << l_idx))
            if candidate > chosen_total:
                chosen_total = candidate
                chosen_l_idx = l_idx
        if chosen_l_idx is None:
            pairs.append((h_row, None))
            continue
        used_mask |= 1 << chosen_l_idx
        pairs.append((h_row, llm_rows[chosen_l_idx]))
    return pairs


def human_alignment_label(row: Row | None) -> str:
    return _first_non_empty(row, _HUMAN_LABEL_COLUMNS)


def llm_alignment_label(row: Row | None) -> str:
    return _first_non_empty(row, _LLM_LABEL_COLUMNS)


def _pair_score(h_row: Row, l_row: Row, *, column_map: Mapping[str, tuple[str, str]]) -> float:
    score = 0.0
    for field_label, (human_col, llm_col) in column_map.items():
        h_val = str((h_row.get(human_col) or "")).strip()
        l_val = str((l_row.get(llm_col) or "")).strip()
        compare_label = "Lab / Experiment" if field_label == "Lab_Or_Field" else field_label
        cls = classify_match(
            field_label=compare_label,
            human_value=h_val,
            llm_value=l_val,
            human_exists=True,
            llm_exists=True,
        )
        score += _CLASS_SCORE.get(cls, 0.0)
    score += _label_bonus(h_row, l_row)
    return score


def _label_bonus(h_row: Row, l_row: Row) -> float:
    human_label = human_alignment_label(h_row)
    llm_label = llm_alignment_label(l_row)
    if not human_label or not llm_label:
        return 0.0

    human_norm = _normalize_label(human_label)
    llm_norm = _normalize_label(llm_label)
    if human_norm and llm_norm and human_norm == llm_norm:
        return 12.0

    human_tokens = _label_tokens(human_label)
    llm_tokens = _label_tokens(llm_label)
    if not human_tokens or not llm_tokens:
        return 0.0

    overlap = human_tokens & llm_tokens
    union = human_tokens | llm_tokens
    jaccard = len(overlap) / len(union) if union else 0.0
    bonus = jaccard * 6.0 + min(len(overlap), 3) * 0.75
    if human_norm and llm_norm and (human_norm in llm_norm or llm_norm in human_norm):
        bonus += 1.5
    return bonus


def _normalize_label(value: str) -> str:
    text = re.sub(r"[^a-z0-9]+", " ", (value or "").strip().lower())
    return " ".join(text.split())


def _label_tokens(value: str) -> set[str]:
    normalized = _normalize_label(value)
    return {
        token
        for token in normalized.split()
        if token and token not in _GENERIC_LABEL_TOKENS
    }


def _first_non_empty(row: Row | None, columns: tuple[str, ...]) -> str:
    if not row:
        return ""
    for column in columns:
        value = str((row.get(column) or "")).strip()
        if value:
            return value
    return ""
