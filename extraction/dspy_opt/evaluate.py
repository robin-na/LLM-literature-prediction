from __future__ import annotations

import argparse
from pathlib import Path

import dspy
from dspy.evaluate import Evaluate

from .dataset import load_examples
from .metric import dspy_metric, dspy_metric_pgg_only
from .program import PGGExtractor

OUTPUT_DIR = Path(__file__).parent / "outputs"


def _to_dspy(items):
    return [
        dspy.Example(
            paper_text=ex.paper_text,
            human_rows=ex.human_rows,
            paper_id=ex.paper_id,
        ).with_inputs("paper_text")
        for ex in items
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="openai/gpt-4.1-mini")
    parser.add_argument("--optimized", default=str(OUTPUT_DIR / "optimized.json"))
    parser.add_argument("--max-tokens", type=int, default=8000)
    parser.add_argument("--num-threads", type=int, default=4)
    args = parser.parse_args()

    lm = dspy.LM(args.model, temperature=0, max_tokens=args.max_tokens, cache=True)
    dspy.configure(lm=lm)

    _, test_raw = load_examples()
    test = _to_dspy(test_raw)
    print(f"Test: {len(test)} held-out papers ({[ex.paper_id for ex in test_raw]})")

    for metric_name, metric_fn in [("PGG-only (12 fields)", dspy_metric_pgg_only),
                                    ("All 22 fields",        dspy_metric)]:
        print(f"\n=== {metric_name} ===")
        evaluator = Evaluate(devset=test, metric=metric_fn,
                             num_threads=args.num_threads,
                             display_progress=True, display_table=0)

        baseline = evaluator(PGGExtractor())
        print(f"Baseline mean = {baseline:.3f}")

        opt_path = Path(args.optimized)
        if not opt_path.exists():
            print(f"(no optimized program at {opt_path}, skipping)")
            continue
        optimized = PGGExtractor()
        optimized.load(str(opt_path))
        opt_score = evaluator(optimized)
        print(f"Optimized mean = {opt_score:.3f}")
        print(f"Δ = {opt_score - baseline:+.3f}")


if __name__ == "__main__":
    main()
