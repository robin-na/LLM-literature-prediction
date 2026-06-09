# Test-set extraction evaluation

Benchmarks Claude Sonnet 4.6 on a held-out test set of PGG papers, comparing its extraction against human annotations.

## What it does

1. **`extract_claude.py`** — reads every paper Markdown listed in `evaluator/inputs/human/human_out_of_sample.csv`, sends it to Claude with the same 34-field schema the human used, and writes structured outputs to `evaluator/inputs/llm/claude_out_of_sample.csv`. Async with concurrency cap (default 5) and graceful retry for `APIConnectionError`.
2. **`compare.py`** — aligns conditions per paper (greedy best-Jaccard on `Experiment Name` + `Topic` + `Misc`), then computes per-field agreement (exact match for categorical, ±5% tolerance for numeric). Writes three CSVs to `results/extraction_model_comparison/`.

## Run

```bash
# 1. Make sure ANTHROPIC_API_KEY is in .env
echo "ANTHROPIC_API_KEY=sk-ant-..." >> .env

# 2. Make sure the human ground truth + papers are in place (delivered via Drive)
ls evaluator/inputs/human/human_out_of_sample.csv  # required
ls PGG_papers/papers/*.md | head                    # required

# 3. Extract (~$5, ~2 min for 25 papers at concurrency=5)
python3 benchmarks/test_set_eval/extract_claude.py

# 4. Compare
python3 benchmarks/test_set_eval/compare.py
```

## Outputs

| Path | Content |
|---|---|
| `evaluator/inputs/llm/claude_out_of_sample.csv` | Claude's structured extraction (80 rows × 34 cols from 25 papers) |
| `benchmarks/test_set_eval/raw_claude_responses.json` | Per-paper raw JSON responses (for debugging) |
| `results/extraction_model_comparison/test_set_field_accuracy.csv` | Per-field accuracy table (24 fields) |
| `results/extraction_model_comparison/test_set_per_paper.csv` | Per-paper accuracy + granularity diff |
| `results/extraction_model_comparison/test_set_disagreements.csv` | All field-level disagreements, side-by-side |

The CSVs in `evaluator/inputs/llm/` are gitignored — outputs go to Google Drive.

## Tuning knobs

| Constant in `extract_claude.py` | Default | Notes |
|---|---|---|
| `MODEL` | `claude-sonnet-4-6` | Swap for opus 4.7 or haiku 4.5 |
| `MAX_CONCURRENT` | 5 | Tier-1 rate limits |
| `MAX_TOKENS` | 4096 | bjso.12450 (8 conditions) hits this — script auto-retries with 16K |

## Caveats

The `Simulation`/`Analytical`/`Review` columns in the schema are always N/A in the human data (the extraction app doesn't track them) but the LLM dutifully outputs 0 or 1. These show as 0% accuracy in the per-field table but are schema mismatches, not Claude failures. Excluding them lifts overall accuracy from ~86.5% to ~91–92% on the remaining 21 evaluable fields.
