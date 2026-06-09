# Data Index

Map of every data file in this repo: what it is, where it lives, what schema it uses, and which code reads it. Read this before touching anything in `input/`, `results/`, `evaluator/`, or `extraction_app/`.

If you can't find a file here, check `git log --diff-filter=A -- <path>` for the commit that introduced it.

---

## 0. Quick top-level map

| Directory | Purpose |
|---|---|
| `PGG_papers/` | The paper corpus (Markdown, PDFs, Web-of-Science catalog) |
| `input/` | PGG experiment **configs** to predict — the prediction targets |
| `science_data/` | The empirical ground-truth efficiency data those predictions are scored against |
| `extraction_app/` | Flask app for humans to extract PGG params from papers |
| `evaluator/` | Comparison app: human extractions vs LLM extractions |
| `extraction/` | Batch-API pipeline for LLM-driven paper extraction |
| `benchmarks/coda/` | CoDa LLM extraction benchmark (Claude vs GPT) |
| `literature/` | Pipeline that turns papers into prompt-augmentation artifacts |
| `prediction/` | Code + outputs for predicting efficiency from configs |
| `prediction_inputs/` | Inputs feeding the prediction pipeline |
| `openAI_batch_output/` / `claude_batch_output/` | Raw Batch-API JSONL responses |
| `results/` | All quantitative outputs: prediction CSVs, metric tables, paper figures |
| `positive_cases/` | Positive-case study outputs |
| `notebooks/` | Exploratory Jupyter notebooks |

---

## 1. The paper corpus

| Path | What | Schema / columns |
|---|---|---|
| `PGG_papers/papers/*.md` | Paper Markdown — ~759 files, one per paper, named by DOI (e.g. `10.1111_ecin.12713.md`) | plain Markdown |
| `extraction_app/pdfs/*.pdf` | Paper PDFs shown in the extraction-app viewer | binary |
| `PGG_papers/WoS_251031_eligible.csv` | Web-of-Science metadata for every eligible paper (~136K rows). **Authoritative source for titles/authors/year**, keyed by `custom_id`. | 70+ cols incl. `Publication Type`, `Authors`, `Article Title`, `Source Title`, `Publication Year`, `custom_id` |
| `PGG_papers/WoS_251031_fileInfo.csv` | File-level metadata for the same papers | smaller helper |
| `PGG_papers/7_papers/`, `PGG_papers/science-paper/` | Subsets used in specific exploratory studies | varies |

---

## 2. Prediction targets: PGG experiment configs

These are the *experiments* the LLM is asked to predict outcomes for.

| Path | What | Rows | Schema |
|---|---|---|---|
| `input/pgg_validation_basePrompt.csv` | **The validation set** used in the main prediction pipeline | 1024 | `CONFIG_configId`, all `CONFIG_*` fields (playerCount, numRounds, endowment, multiplier, allOrNothing, chat, defaultContribProp, punishment*, reward*, etc.) |
| `input/pgg_CONFIGmerged_validation.csv` | Smaller validation set with merged config variants | 20 | same schema |
| `input/pgg_CONFIGmerged_learn.csv` | Learning-set counterpart | varies | same schema |
| `input/pgg_validation_with19ValidationSet.csv` | Validation set + 19 additional cases | varies | same schema |
| `input/pgg_validation_basePrompt_OLD.csv` | Deprecated previous version. Don't use. | varies | same schema |
| `input/df_paired_learn.csv` | Paired control/treatment rows for the learning split | varies | paired schema |

---

## 3. Ground truth (efficiency outcomes)

These are the real-world outcomes from the empirical PGG studies — what predictions are scored against.

| Path | What | Schema |
|---|---|---|
| `science_data/data/processed_data/df_paired_val.csv` | **The canonical ground truth**: per-config `treatment_itt_efficiency` and `control_itt_efficiency`. Loaded as the "y" in `prediction_metrics.py`. | `CONFIG_configId`, `CONFIG_*`, `treatment_itt_efficiency`, `control_itt_efficiency` |
| `science_data/data/processed_data/*` | Other processed empirical datasets | various |
| `science_data/data/raw_data/*` | Raw versions of the above | various |
| `science_data/code/*` | Code that processes raw → processed | Python |

---

## 4. Extraction data (Project A: extract PGG params from papers)

### 4a. Human extractions

| Path | What | Notes |
|---|---|---|
| `extraction_app/extractions.json` | **The live human-extraction store**. Backs the extraction app. 25 papers, ~56 conditions. Keys = paper DOI; values = `{conditions: [{label, Empirical, CONFIG_*, ...}]}` | Edited via the Flask app at `extraction_app/app.py`. Do **not** edit by hand while the app is running — it will overwrite via auto-save. |
| `extraction_app/Human_Extraction_Guide.docx` | Word doc rendered into the in-app guide at `/guide` | Editing this updates the guide in real time |
| `evaluator/inputs/human/human_in_sample.csv` | **Human extractions used for prompt development** (35 papers, 70 condition rows). Was `human_generated.csv`. | 34 cols incl. `Filename`, `Title of the Paper`, `Topic`, `Experiment Name`, `Controled_Or_Observational` (intentional single-`l` typo), `Empirical`, `Lab_Or_Field`, `Simulation`, `Analytical`, `Review`, all `CONFIG_*`, `DV_contributionRate`, `DV_efficiencyReported`, `DV_efficiency`, `Misc` |
| `evaluator/inputs/human/human_out_of_sample.csv` | **Held-out test set for final eval** (25 papers, 56 rows). Generated from `extraction_app/extractions.json`. | Same schema as in-sample |
| `evaluator/outputs/ground_truth.csv` | Reviewed consensus across annotators | `Filename`, `Alignment_Label`, `Granularity`, `Empirical`, `Controled_Or_Observational`, `Lab_Or_Field`, all `CONFIG_*` |
| `evaluator/data/review_events.csv` | Append-only log of reviewer actions | event log |
| `evaluator/data/consensus_events.csv` | Append-only log of consensus actions | event log |
| `evaluator/data/review_data.csv` | Persistent review state snapshot | snapshot |

### 4b. LLM extractions

| Path | What | Schema |
|---|---|---|
| `evaluator/inputs/llm/*` | LLM-produced extractions (CSV/XLSX). Loaded as separate "annotators" by `evaluator/utils/consensus.py`. | Same column schema as human CSVs |
| `extraction/inputs/*.jsonl` | OpenAI/Claude **Batch API request** JSONLs for paper extraction | one JSON-encoded request per line |
| `extraction/inputs/*custom_id_map.json` | Maps batch `custom_id` → human-readable paper id | `{custom_id: paper_id}` |
| `extraction/output_xlsx/*.xlsx` | Per-batch extraction results | spreadsheet |
| `extraction/outputs/*` | Other extraction outputs | various |

### 4c. CoDa benchmark (Claude vs GPT)

| Path | What |
|---|---|
| `benchmarks/coda/batch_inputs/{claude,gpt}_batch{,_v2}.jsonl` | Batch-API requests for the CoDa fields extraction (4 files: 2 models × 2 schema versions) |
| `benchmarks/coda/batch_outputs/*` | Raw model responses |
| `benchmarks/coda/data/` | CoDa schema definitions and paper selections |
| `benchmarks/coda/results/` | Benchmark output tables |
| `benchmarks/coda/coda_schema.py`, `coda_schema_v2.py` | Pydantic schemas defining the CoDa fields |
| `benchmarks/coda/01_select_papers*.py` → `04_evaluate*.py` | Pipeline steps |

### 4d. Extraction comparison reports

| Path | What | Schema |
|---|---|---|
| `results/extraction_model_comparison/agreement.csv` | Per-field agreement rate between GPT-4.1 and Sonnet-4.6 across 37 fields | `field`, `type`, `n_condition_pairs`, `n_agree`, `n_disagree`, `agreement_rate`, `n_both_missing`, `n_one_missing`, `n_both_present`, `n_agree_present` |
| `results/extraction_model_comparison/disagreements.csv` | Every individual disagreement (~17K rows) | `custom_id`, `condition_idx`, `field`, `type`, `gpt41`, `sonnet46` |
| `results/extraction_model_comparison/disagreement_papers_by_field.md` | Per-field summary of which papers disagree | Markdown |
| `results/extraction_model_comparison/human_comparison_table.csv` | Per-field accuracy of Claude vs GPT against the human ground truth | `field`, `category`, `claude_accuracy`, `gpt_accuracy`, `winner`, `claude_mae`, `gpt_mae`, `n_scored_claude`, `n_scored_gpt` |
| `results/extraction_model_comparison/{disagreement,coda_benchmark,human_benchmark,unified_benchmark,alignment_methodology}_report.{tex,pdf}` | Compiled reports | LaTeX + PDFs |
| `results/extraction_model_comparison/agreement.png`, `agreement_optimal_alignment.png` | Figures |

---

## 5. Prediction data (Project B: predict efficiency from configs)

### 5a. Pipeline inputs

| Path | What |
|---|---|
| `prediction_inputs/*` | Inputs the prediction scripts consume (intermediate, often regenerated) |
| `input/pgg_validation_basePrompt.csv` | The main config set (see §2) |

### 5b. Raw Batch-API responses

| Path | What |
|---|---|
| `openAI_batch_output/*.jsonl` | OpenAI batch responses, one JSON per line. Parsed by `prediction/jsonl_parser.py`. |
| `claude_batch_output/*.jsonl` | Claude batch responses, same shape. |

### 5c. Prediction results

Naming pattern (per `CLAUDE.md`): **`prediction_YYMMDD_<type>_<model>.csv`** plus `_metrics.csv` and `_metrics_delta.csv`.

| Path pattern | What |
|---|---|
| `results/prediction_*.csv` | Per-config predicted efficiency, one column per question Q1-Q21 (~127 files) |
| `results/prediction_*_metrics.csv` | RMSE, correlation, directional-accuracy with bootstrap CIs. Columns: `variation`, `rmse`, `rmse_ci_low/high`, `correlation`, `correlation_ci_low/high`, `directional_accuracy`, `directional_accuracy_ci_low/high`, `n` |
| `results/prediction_*_metrics_delta.csv` | Same metrics expressed as a delta vs baseline | `delta_rmse`, `delta_correlation`, `delta_directional_accuracy`, `n` plus CI columns |

Key prefixes within `results/prediction_*`:

| Prefix | Meaning |
|---|---|
| `prediction_baseline_41` | Baseline prediction with GPT-4.1 (no literature) |
| `prediction_251110_RAG_41` | RAG augmentation, GPT-4.1, dated 2025-11-10 |
| `prediction_251110_abstracts_41` | Abstract-only augmentation |
| `prediction_251110_report_41` | Synthesis-report augmentation |
| `prediction_251105_individual_*` | Individual per-paper augmentation (full text vs abstract vs report) |
| `prediction_250722_synthesis_41` | Synthesis runs from July 2025 |
| `prediction_250722_report_all_41` | "All papers" report variant |
| `prediction_crosswave_variations_41[nano]_*` | Cross-wave robustness analysis |
| `prediction_learning_wave_elicitation_41_*` | Learning-wave elicitation analysis |
| `prediction_experiment_data_*` | Experiment-data augmentation |
| `prediction_positive_case*` | Positive-case study runs |

### 5d. Additional analyses

| Path | What |
|---|---|
| `results/elastic_net_*.csv` | Elastic-net baseline comparisons |
| `results/enet_feature_importance_and_shap_summary.csv` | Feature importance from elastic net |
| `results/cache_enet_validation_*.csv` | Cached SHAP and permutation importance |
| `results/crosswave_*.csv` | Cross-wave configuration tendency tables |
| `results/r2_*.csv` | R² benchmark tables |
| `results/learning_r2_benchmark_table.csv` | R² benchmarks for the learning split |
| `results/llm_shift_vs_enet_importance_table.csv` | LLM shift vs elastic-net importance |
| `results/granular_performance_delta_r2_table.csv` | Granular performance deltas |
| `results/feature_corr_shift_vs_matched_baseline_by_variant.csv` | Feature correlation shifts |
| `results/config_{binary,continuous}_feature_*.csv` | Per-config feature analyses |
| `results/punishment_regression_comparison/*` | Punishment regression analysis |

### 5e. Validation outputs

| Path | What |
|---|---|
| `results/validation/*` | ~198 files: per-variant prediction outputs and summaries |
| `results/validation_*.csv` | ~40 top-level validation summary CSVs (variant metadata, shift vs interpretability, monotonicity heterogeneity, reasoning features, etc.) |

---

## 6. Literature processing (prompt augmentation pipeline)

| Path | What | Size |
|---|---|---|
| `literature/prompts/` | Prompt templates that drive paper analysis | small |
| `literature/output/paper_analysis_reports/{broad_all,pgg_ms_only,strict_predictive_empirical_payoff,...}/*.md` | Per-paper analysis reports under different scoping variants | hundreds of files |
| `literature/output/paper_only_narrative/*` | Narrative-form paper-only outputs | varies |
| `literature/output/paper_only_decision/*` | Decision-form paper-only outputs | varies |
| `literature/output/paper_card_memos/*` | Per-paper card memos | varies |
| `literature/output/evidence_cards/*` | Evidence cards | varies |
| `literature/output/collection_synthesis_inputs/*` | Synthesis pipeline inputs at the collection level | varies |
| `literature/output/collection_metadata_synthesis_inputs/*` | Metadata-filtered synthesis inputs | varies |
| `literature/output/collection_analysis_reports/*` | Collection-level analysis reports | varies |
| `literature/output/*/file_search_log.json` | Per-variant search logs (debugging aid) | varies |
| `positive_cases/output/*` | Positive-case study literature outputs (`agentic_report.md`, `analysis_memo.md`, `both`, `both_contrastive`, `both_ensemble`, `both_quantitative`, `both_refined`, `both_rules`, ...) | varies |

The directory naming scheme reflects experimental variants — when a new augmentation experiment is run, a new sibling directory appears (e.g. `broad_all_remaining_after_exactclose_empirical_payoff`).

---

## 7. Paper figures and tables

| Path | What |
|---|---|
| `results/paper/main_text_figures/*.csv` | CSVs backing each main-text figure (~98 files) |
| `results/paper/main_text_figures_mean_repeat_correlation/*.csv` | Repeat-correlation variants of the figures |
| `results/paper/main_text_figures/figure1_panel_b_baseline_vs_humans_correlation_*.csv` | Figure 1, panel B: baseline-vs-humans correlation (cdf percentiles, reference lines, rows, crowds) |
| `experiment_figures/data/*.csv` | 9 supporting CSVs for experiment figures |
| `slides/*` | Slide deck assets |
| `docs/*` | Documentation |

---

## 8. Extraction pipeline runtime files

| Path | What |
|---|---|
| `extraction_app/static/index.html` | Single-page form for human extraction |
| `extraction_app/app.py` | Flask backend |
| `extraction_app/extractions.json` | Live human extractions (see §4a) |
| `extraction_app/templates/` | (Empty / placeholder) |
| `extraction/build_batch_input.py` | Builds Batch-API JSONLs for paper extraction |
| `extraction/extract_papers.py` | Wraps OpenAI Batch API for simple extraction |
| `extraction/download_papers_md.py` | Downloads paper Markdowns from Google Drive |
| `extraction/dspy_opt/*` | DSPy optimization experiments |

---

## 9. Notebooks

| Path | What |
|---|---|
| `notebooks/predict_individual.ipynb` | Exploratory: build per-paper individual prediction batches |
| `notebooks/predict_RAG.ipynb` | Exploratory: build RAG prediction batches |
| `notebooks/*.ipynb` | Other exploratory notebooks |
| `evaluator/notebooks/compare_datasets.ipynb` | Compare human vs LLM datasets |

---

## 10. Secrets (gitignored — do NOT commit)

| Path | Purpose |
|---|---|
| `extraction/gdrive_credentials.json` | OAuth client for Google Drive paper downloads |
| `extraction/gdrive_token.json` | Cached OAuth token |
| `.env` (if present) | API keys (`OPENAI_API_KEY`, `OPENAI_ORG_ID`) |

---

## 11. Caches and build artifacts (safe to delete)

| Path | What |
|---|---|
| `**/__pycache__/` | Python bytecode |
| `**/.ipynb_checkpoints/` | Jupyter autosave |
| `positive_cases/.cache/` | Positive-case pipeline cache |
| `.mplconfig/` | Matplotlib config cache |
| `.venv*/`, `venv/` | Virtual environments |

---

## Conventions

- **Paper IDs**: DOIs with `/` replaced by `_` (e.g. `10.1111/ecin.12713` → `10.1111_ecin.12713`).
- **Custom IDs in batch JSONLs**: `<variation>/<augmentation_key>/Q<n>` (OpenAI) or `<variation>_Q<n>` (Claude). Parsed by `prediction/jsonl_parser.py`.
- **Date prefixes** in `prediction_*.csv` files use `YYMMDD` (e.g. `250722` = 22 July 2025). Files without a date prefix are baselines or are dated by their content.
- **Model suffixes**: `_41` = GPT-4.1, `_41nano` = GPT-4.1-nano, `_opus46` = Claude Opus 4.6. Older runs may use different suffixes.
- **`_metrics.csv` vs `_metrics_delta.csv`**: the former is absolute metrics, the latter is the change relative to a matched baseline.
- **`Controled_Or_Observational`**: yes, it's a typo (single `l`). Matches the ground-truth column and is preserved everywhere downstream — do not "fix" it.
