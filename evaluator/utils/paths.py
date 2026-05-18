from __future__ import annotations

from pathlib import Path

# Repository layout:
#   inputs/human/  — drop human annotator CSV/XLSX files (one or many)
#   inputs/llm/    — drop LLM extraction CSV/XLSX
#   outputs/       — generated ground truth, matrix, HTML, mismatch report (often gitignored)
#   data/          — persistent review/consensus state (event logs, exports)

REPO_ROOT: Path = Path(__file__).resolve().parents[1]
SUPPORTED_INPUT_SUFFIXES: tuple[str, ...] = (".xlsx", ".csv")

DATA_DIR: Path = REPO_ROOT / "data"
STATE_DIR: Path = DATA_DIR

INPUTS_DIR: Path = REPO_ROOT / "inputs"
HUMAN_INPUT_DIR: Path = INPUTS_DIR / "human"
LLM_INPUT_DIR: Path = INPUTS_DIR / "llm"

OUTPUTS_DIR: Path = REPO_ROOT / "outputs"


def resolve_input_dataset_path(directory: Path, basename: str) -> Path:
    candidates = [directory / f"{basename}{suffix}" for suffix in SUPPORTED_INPUT_SUFFIXES]
    existing = [path for path in candidates if path.exists()]
    if existing:
        return max(existing, key=lambda path: path.stat().st_mtime)
    return directory / f"{basename}{SUPPORTED_INPUT_SUFFIXES[0]}"


HUMAN_DATASET_CSV: Path = resolve_input_dataset_path(HUMAN_INPUT_DIR, "human_generated")
LLM_DATASET_CSV: Path = resolve_input_dataset_path(LLM_INPUT_DIR, "LLM_generated")

REVIEW_EVENTS_CSV: Path = STATE_DIR / "review_events.csv"
CONSENSUS_EVENTS_CSV: Path = STATE_DIR / "consensus_events.csv"
GROUND_TRUTH_CSV: Path = OUTPUTS_DIR / "ground_truth.csv"
REVIEW_DATA_CSV: Path = STATE_DIR / "review_data.csv"

FEATURE_MATRIX_SVG: Path = OUTPUTS_DIR / "feature_accuracy_matrix.svg"

COMPARISON_HTML: Path = OUTPUTS_DIR / "comparison.html"
CONSENSUS_HTML: Path = OUTPUTS_DIR / "consensus.html"

# Back-compat: consensus UI and older code refer to "human datasets directory"
HUMAN_DATASETS_DIR: Path = HUMAN_INPUT_DIR
