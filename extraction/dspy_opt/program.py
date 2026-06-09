from __future__ import annotations

import sys
from pathlib import Path

import dspy

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "extraction"))

from build_batch_input import (  # noqa: E402
    INSTRUCTION_TEXT,
    OUTPUT_SCHEMA_DESCRIPTION,
    SYSTEM_PROMPT,
)

_BASE_INSTRUCTIONS = (
    f"{SYSTEM_PROMPT}\n\n{OUTPUT_SCHEMA_DESCRIPTION}\n\n{INSTRUCTION_TEXT}"
)

ExtractPGG = dspy.Signature(
    "paper_text -> extraction_json",
    instructions=_BASE_INSTRUCTIONS,
)


class PGGExtractor(dspy.Module):
    def __init__(self):
        super().__init__()
        self.predict = dspy.Predict(ExtractPGG)

    def forward(self, paper_text: str):
        return self.predict(paper_text=paper_text)
