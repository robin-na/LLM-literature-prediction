# Literature Workspace

This folder is for published-literature augmentation artifacts that are no longer part of the positive-case stage.

Layout:

- `run_reports.py`
  User-facing literature runner. By default it generates both the narrative and
  decision-support reports in one command.

- `run_agentic_report.py`
  Compatibility alias for the literature runner.

- `build_report_batch_input.py`
  User-facing builder for collection-level literature report batch JSONLs. By
  default it generates both narrative and decision-support synthesis files in one
  command.

- `build_prediction_batch_input.py`
  User-facing builder for prediction batch JSONLs derived from the literature
  report batch outputs.

- `build_prediction_batch_from_reports.py`
  User-facing builder for prediction batch JSONLs derived directly from the
  final narrative and decision report markdown files in `literature/output/`.

- `build_prediction_batch_from_card_memos.py`
  Builds per-paper prediction batch JSONLs from paper-level analysis reports
  rendered from the extracted evidence-card outputs. This is the entrypoint
  for one-paper-at-a-time augmentation experiments. It also supports
  continuation repeats via `--repeat-start-index`, so later runs can emit
  `rep2`, `rep3`, ... without regenerating `rep1`. The shared model registry
  now covers both the dated GPT-4.1 family and the GPT-5.1 family.

- `build_evidence_card_batch_input.py`
  User-facing builder for per-paper evidence-card extraction batch JSONLs from
  markdown papers, plus a small random smoke-test file and a token-estimate
  summary.

- `parse_evidence_card_batch_output.py`
  Parses evidence-card batch outputs into flat CSV tables, including a single
  denormalized `combined.csv` that downstream scripts use.

- `clean_markdown_corpus.py`
  Produces a cleaned markdown corpus for paper-level extraction, trimming
  stitched multi-article artifacts and trailing reference/commentary material
  while preserving the target paper content.

- `render_card_snippets.py`
  Renders compact card snippets from parsed evidence cards for inspection and
  lightweight augmentation experiments.

- `analyze_evidence_card_eligibility.py`
  Builds candidate literature subsets from the evidence-card metadata, such as
  the strict empirical payoff-like pool and broader support pools.

- `build_collection_switch_sets.py`
  Builds the agreed 8 switch-based collection-set CSVs, excluding
  `PGG_MS_202502`, and also writes the remaining broad set for individual-paper
  augmentation beyond the initial strict pool.

- `build_collection_synthesis_batch_input.py`
  Builds hierarchical stage-1 batch input for collection synthesis. It
  partitions the broad literature universe into the 8 A/B/C paper sets and
  asks the model to produce one literature analysis report for each. It also
  emits one extra direct full-corpus request over the full `broad_all` set
  (2011 papers, excluding `PGG_MS_202502`) for long-context comparison.
  The script also writes `leaf_manifest.csv` and `leaf_legend.csv`, which map
  ids like `leaf_a1_b0_c1` to the underlying switch meanings and paper counts.

- `build_collection_synthesis_final_batch_input.py`
  Builds hierarchical stage-2 batch input for collection synthesis. It takes
  the 8 stage-1 literature analysis reports and asks the model to produce one
  final narrative or decision-support report per collection.

- `build_prediction_batch_from_collection_reports.py`
  Extracts synthesized collection analysis reports from the stage-1 batch
  output, writes them to `literature/output/collection_analysis_reports/`,
  and builds joint-with-explanation prediction batch JSONLs for the supported
  GPT-4.1 family, `gpt-5.1`, `gpt-5-mini`, and `gpt-5-nano`. It also supports
  continuation repeats via `--repeat-start-index`.

- `build_joint_reasoning_suite_batch_input.py`
  Builds one merged joint-with-explanation literature suite batch JSONL per
  model. Each file contains 5 repetitions each of:
  - the unaugmented baseline
  - the `PGG_MS_202502` benchmark paper augmentation
  - the 9 stage-1 collection-report augmentations
  This produces `11 × 5 = 55` requests per model and is the cleanest entrypoint
  when running the literature suite as one batch.

- `build_prediction_batch_from_full_pggms_paper.py`
  Builds benchmark-only joint-with-explanation prediction batch JSONLs that
  attach the full cleaned `PGG_MS_202502` manuscript text directly, instead of
  the LLM-generated single-paper analysis report. This is the direct A/B
  comparison against the benchmark-report augmentation path.

- `prompts/evidence_card_extraction_prompt.md`
  Common extraction instruction prompt shared across all paper evidence-card
  requests.

- `output/`
  Generated literature reports such as `paper_only_narrative/agentic_report.md`
  and `paper_only_decision/agentic_report.md`, plus parsed evidence-card tables,
  per-paper analysis reports, collection-level analysis reports, and
  collection-synthesis input bundles.

- `.cache/`
  Cached OpenAI file and vector-store ids used by the literature report pipeline.

Shared code:

- `agentic_report/` at the repo root is the neutral import surface for the shared
  report-generation engine.
- `positive_cases/` still contains experiment-specific scripts and legacy wrappers,
  but the literature workflow no longer needs to be launched from there.

Commands:

- Run both literature reports:
  `python literature/run_reports.py`
  `python literature/run_agentic_report.py`

- Run only one style:
  `python literature/run_reports.py --report-method paper_only_narrative`
  `python literature/run_reports.py --report-method paper_only_decision`

- Build both collection-level literature report batch files:
  `python literature/build_report_batch_input.py`

- Build literature prediction batch files from the two report outputs:
  `python literature/build_prediction_batch_input.py --narrative-reports <path> --decision-reports <path>`

- Build literature prediction batch files directly from the final report markdowns:
  `python literature/build_prediction_batch_from_reports.py`

- Build full and smoke-test evidence-card extraction batch files from markdown papers:
  `python literature/build_evidence_card_batch_input.py`

- Parse evidence-card outputs into CSVs:
  `python literature/parse_evidence_card_batch_output.py --input <batch-output.jsonl>`

- Build the agreed collection set manifests:
  `python literature/build_collection_switch_sets.py`

- Build stage-1 paper-set synthesis requests:
  `python literature/build_collection_synthesis_batch_input.py`
  This writes 9 requests total: 8 A/B/C paper-set reports plus 1 direct
  `broad_all` full-corpus report.

- Build stage-2 final collection synthesis requests after stage-1 outputs return:
  `python literature/build_collection_synthesis_final_batch_input.py --leaf-output-jsonl <stage1-output.jsonl>`

- Build prediction batch files directly from the 9 synthesized stage-1
  collection analysis reports:
  `python literature/build_prediction_batch_from_collection_reports.py`

- Build only repeat continuations (`rep2`-`rep5`) for the 9 collection reports:
  `python literature/build_prediction_batch_from_collection_reports.py --n-explanation-repeats 4 --repeat-start-index 2 --output-prefix prediction_literature_collection_analysis_report_stage1_9variants_joint_reps2to5`

- Build repeat continuations (`rep2`-`rep3`) for the merged `2011`-paper
  individual-paper augmentation set across the current 6 GPT-4.1 / GPT-5
  family models:
  `python literature/build_prediction_batch_from_card_memos.py --paper-set-csv literature/output/evidence_cards/literature_evidence_cards_cleaned/collection_switch_sets/sets/broad_all.csv --models gpt-4.1-2025-04-14 gpt-4.1-mini-2025-04-14 gpt-4.1-nano-2025-04-14 gpt-5.1 gpt-5-mini gpt-5-nano --modes joint_reasoning --n-explanation-repeats 2 --repeat-start-index 2 --output-prefix prediction_literature_analysis_report_extended2011_joint_reps2to3`

- Build 5-repeat full-paper benchmark augmentation files for the 6 current
  GPT-4.1 / GPT-5 family models:
  `python literature/build_prediction_batch_from_full_pggms_paper.py`
