from __future__ import annotations

import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_PATH = PROJECT_ROOT / "science-data_and_code" / "data" / "processed_data" / "df_analysis_learn.csv"
PAPER_PATH = PROJECT_ROOT / "PGG_papers" / "science-paper" / "PGG_paper_science.pdf"

BASE_OUTPUT_DIR = PROJECT_ROOT / "positive_cases" / "output"
CACHE_DIR = PROJECT_ROOT / "positive_cases" / ".cache"
LITERATURE_DIR = PROJECT_ROOT / "literature"
LITERATURE_OUTPUT_DIR = LITERATURE_DIR / "output"
LITERATURE_CACHE_DIR = LITERATURE_DIR / ".cache"

DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1")
ANALYSIS_MODEL = os.getenv("OPENAI_ANALYSIS_MODEL", DEFAULT_MODEL)
SUMMARY_MODEL = os.getenv("OPENAI_SUMMARY_MODEL", DEFAULT_MODEL)
REPORT_MODEL = os.getenv("OPENAI_REPORT_MODEL", DEFAULT_MODEL)

FILE_PURPOSE = os.getenv("OPENAI_FILE_PURPOSE", "user_data")
DEFAULT_LITERATURE_VECTOR_STORE_ID = os.getenv(
    "OPENAI_LITERATURE_VECTOR_STORE_ID",
    "vs_68e867cb856881919afaf916060dcea8",
)


def ensure_dirs(output_dir: Path, cache_dir: Path = CACHE_DIR) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    cache_dir.mkdir(parents=True, exist_ok=True)


def resolve_paper_paths() -> list[Path]:
    path = PAPER_PATH.resolve()
    if path.is_file():
        return [path]
    if path.is_dir():
        pdfs = sorted(path.rglob("*.pdf"))
        if pdfs:
            return pdfs
    raise FileNotFoundError(f"No paper PDF files found at: {path}")
