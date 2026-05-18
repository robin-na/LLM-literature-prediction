from __future__ import annotations

import os
from pathlib import Path

DEFAULT_PAPER_IDS = [
    "10.1007_s10645-008-9094-1",
    "10.1177_0146167216684134",
    "10.1016_j.jpubeco.2015.12.012",
    "10.1007_s10640-025-00970-6",
    "10.3390_g14050065",
    "10.1111_apce.12343",
    "10.1016_j.evolhumbehav.2006.06.001",
]

RAW_PAPER_MARKDOWN_DIR_ENV_VAR = "RAW_PAPER_MARKDOWN_DIR"
DEFAULT_LOCAL_PAPER_DIR = "PGG_papers/papers"
DERIVED_MARKDOWN_DIR_NAMES = frozenset({"paper_analysis_reports", "paper_card_memos"})


def default_paper_dir() -> str:
    return os.getenv(RAW_PAPER_MARKDOWN_DIR_ENV_VAR, DEFAULT_LOCAL_PAPER_DIR)


def is_derived_markdown_dir(path: Path) -> bool:
    return any(part.lower() in DERIVED_MARKDOWN_DIR_NAMES for part in path.parts)


def resolve_paper_dir(paper_dir_arg: str | None) -> Path:
    if not paper_dir_arg:
        raise ValueError(
            "Raw paper markdown directory is required. Pass --paper-dir or set "
            f"{RAW_PAPER_MARKDOWN_DIR_ENV_VAR}. Default expected path: {DEFAULT_LOCAL_PAPER_DIR}."
        )

    paper_dir = Path(paper_dir_arg)
    if not paper_dir.exists():
        raise FileNotFoundError(f"Paper markdown directory not found: {paper_dir}")
    if not paper_dir.is_dir():
        raise NotADirectoryError(f"Paper markdown path is not a directory: {paper_dir}")
    if is_derived_markdown_dir(paper_dir):
        raise ValueError(
            "Refusing to run extraction on derived markdown. Point --paper-dir "
            "at raw paper markdown, not `paper_analysis_reports` or `paper_card_memos`."
        )
    return paper_dir
