"""
Repo entrypoint CLI.

Primary commands:
  evaluate        Auto-detect single vs multi annotator; build ground truth + matrix + mismatch report
  consensus       Build consensus UI and start the local server (Stage 1, multi-annotator)
  ui              Generate comparison UI and start the review server (Stage 2)
  refresh-eval    Same pipeline as evaluate (explicit refresh after input edits)
  feature-matrix  Print per-feature LLM vs human accuracy matrix

Utility commands:
  build           Generate outputs/comparison.html only
  ground-truth    Rebuild outputs/ground_truth.csv from inputs + consensus events
  finalize        Materialize the final reviewed dataset (raw + UI events)
  analyze         Run meta-analysis into data/
  mismatch-report Write combined mismatch report into outputs/mismatch.md
  clean           Remove generated artifacts (dry-run by default)
  test            Run the test suite
  build-dv-taxonomy  Build or refresh utils/dv_taxonomy.json via GPT-4.1

Advanced / debug commands:
  mismatch-summary   Per-field mismatch summary (subset of mismatch-report)
  mismatch-reasons   Mismatch examples with LLM reasons (subset of mismatch-report)
  error-analysis     Error taxonomy for prompt refinement (subset of mismatch-report)
"""

from __future__ import annotations

import argparse
from typing import Callable

from cli.parser import build_parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    ns = parser.parse_args(argv)
    func: Callable[[argparse.Namespace], int] = ns.func
    return func(ns)


if __name__ == "__main__":
    raise SystemExit(main())
