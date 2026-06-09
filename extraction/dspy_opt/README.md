# DSPy-optimized PGG extraction prompt

Optimizes the main PGG extraction prompt (`SYSTEM_PROMPT` + `INSTRUCTION_TEXT` +
`OUTPUT_SCHEMA_DESCRIPTION` in `extraction/build_batch_input.py`) against the
human-labeled ground truth at `evaluator/inputs/human/human_generated.csv`.

Only papers whose markdown also exists in `PGG_papers/papers/` are used. At
write time that's **10 papers**, split deterministically (seed=7) into
**7 train / 3 test**.

The scoring metric reuses `align_rows` + `classify_match` + `COLUMN_MAP` from
the `evaluator/` package, so the optimized prompt is judged on the same
yardstick as `prediction/compare_vs_human_gt.py`.

## Install
```bash
pip install dspy-ai
```

## Run
```bash
export OPENAI_API_KEY=...

# Optimize against the 12 PGG CONFIG fields (default — the fields that matter
# for downstream efficiency prediction).
python -m extraction.dspy_opt.optimize

# Or optimize against all 22 fields:
python -m extraction.dspy_opt.optimize --metric all_fields

# MIPROv2 light (more thorough, ≈ 3–5× the cost):
python -m extraction.dspy_opt.optimize --optimizer mipro --mipro-auto light

# Score baseline vs optimized on the 3 held-out papers (reports both metrics):
python -m extraction.dspy_opt.evaluate
```

## Files
| File | Purpose |
|------|---------|
| `dataset.py` | Loads human GT, groups by paper, joins to markdowns, 7/3 split |
| `program.py` | DSPy `Signature` wrapping the existing system/instruction/schema text |
| `metric.py`  | Per-paper mean field accuracy via `align_rows` + `classify_match` |
| `optimize.py` | BootstrapFewShot (default) or MIPROv2; saves `outputs/optimized.json` |
| `evaluate.py` | Baseline vs optimized on the test split, both metrics |

## Cost notes

Papers are 20–40 KB each. A BootstrapFewShot run roughly:

- 7 train papers × a few bootstrap rounds ≈ 30–60 calls
- ~30 KB input × 8 K-token output ceiling per call
- gpt-4.1-mini (~$0.40/1M in, ~$1.60/1M out) → **~$1–3 per run**

`--max-demos 2` (default) keeps the prompt under control — at 3+ demos the
context balloons by ~90 KB. MIPROv2 light is a few × that.

## Caveats

- **N=3 test set.** Single-run Δ is noisy — re-run with a different `seed`
  in `dataset.py` for sanity, or use leave-one-out by iterating seeds.
- **10 usable papers total.** The human GT has 20 papers but 10 lack
  markdown files in `PGG_papers/papers/`. Adding them would let us widen
  the split.
- The optimizer only sees the *prompt's* output JSON, not the post-hoc
  XLSX flattening done by the real extraction pipeline — the metric
  parses JSON directly. That's tighter (avoids flattening bugs) but means
  XLSX-only normalisations aren't exercised.
- `missing_row` is scored as 0 (encourages right condition count);
  `both_empty` / `one_empty` are excluded from the denominator.
