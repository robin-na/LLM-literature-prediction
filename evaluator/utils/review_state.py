from __future__ import annotations


def _canon_stage2_classification(value: str) -> str:
    value = (value or "").strip().replace("-", "_")
    if value in {"match", "close", "both_empty"}:
        return "match"
    if value in {"mismatch", "one_empty", "missing_row"}:
        return "mismatch"
    return value


def build_classification_overrides(events: list[dict[str, str]]) -> dict[str, str]:
    """Materialize the latest classification override per cell key.

    Expects events where:
    - action == 'set_classification'
    - key identifies the cell (e.g. 'paper|row|field')
    - new_classification is the chosen class, or '__auto'/empty to clear
    """
    overrides: dict[str, str] = {}
    for ev in events:
        if ev.get("action") != "set_classification":
            continue
        key = (ev.get("key") or "").strip()
        new_cls = (ev.get("new_classification") or "").strip()
        if not key:
            continue
        if not new_cls or new_cls == "__auto":
            overrides.pop(key, None)
        else:
            overrides[key] = _canon_stage2_classification(new_cls)
    return overrides


def build_paper_notes(events: list[dict[str, str]], reviewer_id: str) -> dict[str, str]:
    """Materialize the latest per-paper note for a reviewer.

    Expects events where:
    - action == 'set_paper_note'
    - key is the paper_id
    - new_value is the note text (empty clears)
    - reviewer_id is the reviewer who wrote the note
    """
    notes: dict[str, str] = {}
    reviewer_id = (reviewer_id or "").strip()
    for ev in events:
        if ev.get("action") != "set_paper_note":
            continue
        if (ev.get("reviewer_id") or "").strip() != reviewer_id:
            continue
        paper_id = (ev.get("key") or "").strip()
        note = (ev.get("new_value") or "").strip()
        if not paper_id:
            continue
        if not note:
            notes.pop(paper_id, None)
        else:
            notes[paper_id] = note
    return notes

