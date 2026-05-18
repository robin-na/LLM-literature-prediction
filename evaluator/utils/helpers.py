from __future__ import annotations

from pathlib import Path

from utils.csvio import Row
from utils.paths import STATE_DIR


def normalize_paper_id(value: str) -> str:
    return (value or "").replace(".md", "").strip()


def group_by_paper(
    rows: list[Row],
    key_col: str,
    *,
    strip_md: bool = False,
) -> dict[str, list[Row]]:
    groups: dict[str, list[Row]] = {}
    for row in rows:
        paper_id = (row.get(key_col) or "").strip()
        if strip_md:
            paper_id = normalize_paper_id(paper_id)
        if not paper_id:
            continue
        groups.setdefault(paper_id, []).append(row)
    return groups


def ordered_union(a: list[str], b: list[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for value in a + b:
        if value in seen:
            continue
        seen.add(value)
        out.append(value)
    return out


def is_empty_like(value: str) -> bool:
    normalized = (value or "").strip().lower()
    return (
        normalized in {"", "n/a", "na", "n/r", "nr", "none", "null"}
        or normalized.startswith("n/a")
        or normalized.startswith("n/r")
    )


def guess_reviewer_id(review_session_id: str) -> str:
    pattern = f"final_review_dataset__{review_session_id}__*.csv"
    candidates = [path for path in STATE_DIR.glob(pattern) if path.is_file()]
    if not candidates:
        return "anonymous"
    latest = max(candidates, key=lambda path: path.stat().st_mtime)
    prefix = f"final_review_dataset__{review_session_id}__"
    return latest.stem[len(prefix):] if latest.stem.startswith(prefix) else "anonymous"


def md_cell(value: object) -> str:
    text = str(value or "").replace("|", "\\|").replace("\n", "<br>")
    return text if text else ""
