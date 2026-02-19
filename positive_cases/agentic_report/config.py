from __future__ import annotations

import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_PATH = PROJECT_ROOT / "science-data_and_code" / "data" / "processed_data" / "df_analysis_learn.csv"
PAPER_PATH = PROJECT_ROOT / "PGG_papers" / "science-paper" / "PGG_paper_science.pdf"

BASE_OUTPUT_DIR = PROJECT_ROOT / "positive_cases" / "output"
CACHE_DIR = PROJECT_ROOT / "positive_cases" / ".cache"

DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1")
ANALYSIS_MODEL = os.getenv("OPENAI_ANALYSIS_MODEL", DEFAULT_MODEL)
SUMMARY_MODEL = os.getenv("OPENAI_SUMMARY_MODEL", DEFAULT_MODEL)
REPORT_MODEL = os.getenv("OPENAI_REPORT_MODEL", DEFAULT_MODEL)

FILE_PURPOSE = os.getenv("OPENAI_FILE_PURPOSE", "user_data")


def ensure_dirs(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
