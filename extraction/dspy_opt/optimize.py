from __future__ import annotations

import argparse
from pathlib import Path

import dspy

from .dataset import Example, load_examples
from .metric import dspy_metric, dspy_metric_pgg_only
from .program import PGGExtractor

OUTPUT_DIR = Path(__file__).parent / "outputs"


def _to_dspy(items: list[Example]) -> list[dspy.Example]:
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
    parser.add_argument("--model", default="openai/gpt-4.1-mini",
                        help="LiteLLM model id (e.g. 'openai/gpt-4.1-mini', 'anthropic/claude-haiku-4-5').")
    parser.add_argument("--optimizer", choices=["bootstrap", "mipro"], default="bootstrap")
    parser.add_argument("--metric", choices=["all_fields", "pgg_only"], default="pgg_only",
                        help="Optimization target: all 22 fields or just the 12 PGG CONFIG fields.")
    parser.add_argument("--max-demos", type=int, default=2,
                        help="BootstrapFewShot: max bootstrapped / labeled demos. Keep small — papers are 20–40 KB each.")
    parser.add_argument("--mipro-auto", choices=["light", "medium", "heavy"], default="light")
    parser.add_argument("--max-tokens", type=int, default=8000)
    parser.add_argument("--output-name", default="optimized.json")
    args = parser.parse_args()

    lm = dspy.LM(args.model, temperature=0, max_tokens=args.max_tokens, cache=True)
    dspy.configure(lm=lm)

    train_raw, _ = load_examples()
    train = _to_dspy(train_raw)
    print(f"Train: {len(train)} papers ({[ex.paper_id for ex in train_raw]})")

    metric_fn = dspy_metric_pgg_only if args.metric == "pgg_only" else dspy_metric
    student = PGGExtractor()

    if args.optimizer == "bootstrap":
        from dspy.teleprompt import BootstrapFewShot
        optimizer = BootstrapFewShot(
            metric=metric_fn,
            max_bootstrapped_demos=args.max_demos,
            max_labeled_demos=args.max_demos,
        )
        optimized = optimizer.compile(student, trainset=train)
    else:
        from dspy.teleprompt import MIPROv2
        optimizer = MIPROv2(metric=metric_fn, auto=args.mipro_auto)
        optimized = optimizer.compile(student, trainset=train,
                                      requires_permission_to_run=False)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / args.output_name
    optimized.save(str(out_path))
    print(f"\nSaved optimized program → {out_path}")
    print(f"Next: python -m extraction.dspy_opt.evaluate --model {args.model}")


if __name__ == "__main__":
    main()
