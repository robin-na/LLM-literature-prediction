from __future__ import annotations

import random
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "evaluator"))

from utils.csvio import read_csv  # noqa: E402

HUMAN_CSV = REPO_ROOT / "evaluator" / "inputs" / "human" / "human_generated.csv"
PAPER_DIR = REPO_ROOT / "PGG_papers" / "papers"


@dataclass
class Example:
    paper_id: str
    paper_text: str
    human_rows: list[dict]   # one dict per condition, keyed by human column names


def load_examples(
    human_csv: Path = HUMAN_CSV,
    paper_dir: Path = PAPER_DIR,
    seed: int = 7,
    splits: tuple[int, int] = (7, 3),
) -> tuple[list[Example], list[Example]]:
    rows = read_csv(human_csv)
    by_paper: dict[str, list[dict]] = {}
    for r in rows:
        pid = r.get("Filename", "").strip()
        if pid:
            by_paper.setdefault(pid, []).append(r)

    examples: list[Example] = []
    for pid, h_rows in by_paper.items():
        md = paper_dir / f"{pid}.md"
        if not md.exists():
            continue
        examples.append(Example(
            paper_id=pid,
            paper_text=md.read_text(encoding="utf-8"),
            human_rows=h_rows,
        ))

    rng = random.Random(seed)
    rng.shuffle(examples)

    n_train, n_test = splits
    if n_train + n_test > len(examples):
        raise RuntimeError(
            f"Only {len(examples)} usable papers (need {n_train + n_test}). "
            f"Missing markdowns in {paper_dir}."
        )
    return examples[:n_train], examples[n_train:n_train + n_test]
