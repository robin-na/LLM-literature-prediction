# Stage-1 Collection Analysis Reports

This folder stores the 9 synthesized markdown reports that came back from:

- `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/openAI_batch_output/synthesis_collection_switch_sets_stage1.jsonl`

These reports were written to disk by:

- `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/literature/build_prediction_batch_from_collection_reports.py`

What is here:

- 8 subset reports:
  - `leaf_a0_b0_c0.md`
  - `leaf_a0_b0_c1.md`
  - `leaf_a0_b1_c0.md`
  - `leaf_a0_b1_c1.md`
  - `leaf_a1_b0_c0.md`
  - `leaf_a1_b0_c1.md`
  - `leaf_a1_b1_c0.md`
  - `leaf_a1_b1_c1.md`
- 1 direct full-corpus report:
  - `broad_all_2011.md`
- `report_index.csv`
  - maps `variant_id` to:
    - originating batch `custom_id`
    - variant kind
    - paper count
    - short description
    - markdown report path

Current experimental use:

- The collection-prediction batches and repeat-5 collection analyses in this
  repo use these **stage-1 reports directly**.
- They are the source for the 9 collection-report augmentation variants:
  - 8 subset reports
  - 1 direct `broad_all_2011` report

This is different from the optional stage-2 recombination workflow:

- `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/literature/build_collection_synthesis_final_batch_input.py`

That stage-2 path was prepared, but the current collection-level prediction
results in this repo were not built from stage-2 final collection reports.

Subset id reminder:

- `A`
  - exact/close on PGG relevance and punishment relevance
- `B`
  - payoff-like primary outcome
- `C`
  - empirical only

Examples:

- `leaf_a1_b0_c1`
  - exact/close PGG + punishment relevance
  - not restricted to payoff-like outcomes
  - empirical only
- `leaf_a1_b1_c0`
  - exact/close PGG + punishment relevance
  - payoff-like outcomes
  - not empirical-only

If you continue collection-level analysis in another thread, start with:

- `report_index.csv`
- `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/literature/output/collection_synthesis_inputs/leaf_legend.csv`
- `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/literature/output/collection_synthesis_inputs/collection_leaf_map.csv`
