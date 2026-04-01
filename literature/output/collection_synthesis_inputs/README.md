# Collection Synthesis Inputs

This folder stores the rendered inputs and manifests for collection-level
literature synthesis.

Current workflow:

1. Build the agreed collection-set CSVs:
   - `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/literature/build_collection_switch_sets.py`
2. Build stage-1 synthesis requests:
   - `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/literature/build_collection_synthesis_batch_input.py`
3. Submit:
   - `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/openAI_batch_input/synthesis_collection_switch_sets_stage1.jsonl`
4. Parse the stage-1 outputs into markdown reports and build prediction inputs:
   - `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/literature/build_prediction_batch_from_collection_reports.py`

Important clarification:

- The current collection prediction experiments use the **9 stage-1 reports
  directly**:
  - 8 A/B/C subset reports
  - 1 direct `broad_all_2011` report
- The stage-2 builder exists, but the current reported collection-prediction
  results were **not** based on stage-2 recombined collection reports.

The 8 disjoint subset ids come from the agreed binary switches:

- `A`
  - exact/close on both PGG relevance and punishment relevance
- `B`
  - payoff-like primary outcome
- `C`
  - empirical only

So, for example:

- `leaf_a1_b0_c1`
  - `A=on`, `B=off`, `C=on`
  - exact/close PGG + punishment relevance
  - no payoff-like-outcome requirement
  - empirical only

Main files to use now:

- `leaf_manifest.csv`
  - one row per disjoint A/B/C subset, with count, digest path, and custom id
- `leaf_legend.csv`
  - concise mapping from `leaf_a*_b*_c*` ids to the switch meanings
- `collection_leaf_map.csv`
  - maps each named collection to the subset ids that compose it
- `direct_request_manifest.csv`
  - metadata for the extra direct long-context `broad_all_2011` request
- `prompt_previews/stage1_subset_prompt_preview.md`
  - rendered stage-1 prompt preview
- `leaf_a*.md`
  - the rendered paper-set digests used in the current 8 subset requests
- `broad_all_2011_direct.md`
  - the rendered direct full-corpus digest used in the 9th request

Current stage-1 requests:

- 8 subset reports:
  - `subset_summary/leaf_a0_b0_c0`
  - `subset_summary/leaf_a0_b0_c1`
  - `subset_summary/leaf_a0_b1_c0`
  - `subset_summary/leaf_a0_b1_c1`
  - `subset_summary/leaf_a1_b0_c0`
  - `subset_summary/leaf_a1_b0_c1`
  - `subset_summary/leaf_a1_b1_c0`
  - `subset_summary/leaf_a1_b1_c1`
- 1 direct report:
  - `collection_direct/broad_all_2011`

Legacy / superseded exploratory artifacts still present here:

- `chunk_manifest.csv`
- `chunks/`
- `leaf_chunk_manifest.csv`
- `leaf_chunks/`
- `broad_all.md`
- `broad_empirical.md`
- `broad_payoff_like.md`
- `broad_empirical_payoff_like.md`
- `exactclose_*.md`

Those files come from earlier chunked synthesis attempts. They are not the
current source of truth for the stage-1 collection experiments unless you
explicitly want to revisit hierarchical chunking.
