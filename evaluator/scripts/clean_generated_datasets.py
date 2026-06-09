from __future__ import annotations

from pathlib import Path

from utils.paths import GROUND_TRUTH_CSV, STATE_DIR


def _append_if_exists(paths: list[Path], path: Path) -> None:
    if path.exists() and path.is_file():
        paths.append(path)


def _append_glob_matches(paths: list[Path], root: Path, pattern: str) -> None:
    if not root.exists():
        return
    for p in root.glob(pattern):
        if p.is_file():
            paths.append(p)


def _collect_generated_files() -> list[Path]:
    files: list[Path] = []

    _append_if_exists(files, GROUND_TRUTH_CSV)
    _append_if_exists(files, STATE_DIR / "consensus_events.csv")

    _append_if_exists(files, STATE_DIR / "review_events.csv")
    _append_if_exists(files, STATE_DIR / "review_data.csv")
    _append_glob_matches(files, STATE_DIR, "review_overrides__*.csv")
    _append_glob_matches(files, STATE_DIR, "final_review_dataset__*.csv")
    _append_glob_matches(files, STATE_DIR, "meta_*.csv")

    unique = sorted(set(files), key=lambda p: str(p))
    return unique


def clean_generated_datasets(*, dry_run: bool) -> list[Path]:
    """Delete generated analysis-dataset artifacts and return affected paths."""
    targets = _collect_generated_files()
    if dry_run:
        return targets

    deleted: list[Path] = []
    for path in targets:
        if not path.exists() or not path.is_file():
            continue
        path.unlink()
        deleted.append(path)
    return deleted
