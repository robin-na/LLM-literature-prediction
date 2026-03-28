# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a research project evaluating whether augmenting LLM prompts with academic literature improves predictions of Public Goods Game (PGG) experiment outcomes. Specifically, the task is predicting how enabling a punishment mechanism changes a game's **efficiency** (ratio of actual group payoff to maximum cooperative payoff, expressed as a percentage integer).

Augmentation strategies tested: baseline (no literature), paper abstracts, full texts, AI-generated synthesis reports, and RAG (OpenAI vector store retrieval).

## Commands

### Build batch input JSONL for paper extraction
```bash
python batch_processing/build_batch_input.py \
  --csv-path PGG_papers/WoS_251031_eligible.csv \
  --markdown-dir papers_markdown/ \
  --output batch_processing/inputs/batch_input.jsonl
```
Optional flags: `--model gpt-5.1`, `--temperature 0`, `--custom-ids <id1> <id2>`

### Convert batch output JSONL to structured CSV
```bash
python batch_processing/batch_output_to_csv.py --input-jsonl <output.jsonl>
# outputs to batch_processing/output_csv/<stem>.csv by default
```

### Compute prediction metrics (RMSE, correlation, directional accuracy with bootstrap CIs)
```bash
python analysis/prediction_metrics.py \
  --input-dir openAI_batch_output \
  --results-dir results \
  --ground-truth science-data_and_code/data/processed_data/df_paired_val.csv \
  --platform openai   # or: claude
```
Writes `<stem>.csv`, `<stem>_metrics.csv`, and `<stem>_metrics_delta.csv` for each `prediction*.jsonl` found in `--input-dir`.

## Architecture

### Core data flow
1. **Paper collection** (`paper_collection/`): Web of Science CSVs of eligible PGG papers, with metadata and `file_path`/`file_id` columns.
2. **Input configs** (`input/`): PGG experiment configurations as CSVs. Key files:
   - `pgg_validation_basePrompt.csv` — validation set used for prediction
   - `pgg_CONFIGmerged_validation.csv` / `pgg_CONFIGmerged_learn.csv` — extended sets
3. **Batch input construction**: Two routes:
   - Jupyter notebooks (`predict_individual.ipynb`, `predict_RAG.ipynb`) — exploratory; build `OpenAI_batch_input/*.jsonl`
   - `batch_processing/build_batch_input.py` — CLI script for paper-extraction prompts
4. **OpenAI Batch API**: JSONL requests submitted via the API; outputs land in `openAI_batch_output/` (or `claude_batch_output/`)
5. **Parsing & metrics** (`analysis/`):
   - `jsonl_parser.py` — `jsonl_to_dataframe()` extracts numeric predictions from LLM output; handles logprobs-based mean, JSON structured output, and plain numeric fallback; supports both `openai` and `claude` platform formats
   - `prediction_metrics.py` — orchestrates loading, metric computation, and CSV writing
6. **Results** (`results/`): Named `prediction_YYMMDD_<type>_<model>.csv` + `_metrics.csv` + `_metrics_delta.csv`
7. **Analysis scripts** (`analysis/`): Standalone Python scripts for cross-wave analysis, elastic net comparisons, positive-case studies, and figure generation
8. **Plot notebooks** (`plots/`): Jupyter notebooks for final paper figures

### Custom ID convention
Prediction batch requests use `custom_id` format `<variation>/<augmentation_key>/Q<n>` (OpenAI slash separator) or `<variation>_Q<n>` (Claude underscore). `jsonl_parser.py` handles both.

### Key prompt structure
- **System prompt**: Defines the efficiency prediction task
- **User prompt**: `make_predict_prompt(make_config(row), augmented_text=...)` — config block prepended with optional augmentation text
- **Augmentation instructions** (`prompt_summary`, `prompt_abstract_individual`, `prompt_fulltext`, etc.): Wrap the injected literature text with appropriate framing

### Environment / API keys
Required env vars: `OPENAI_API_KEY` (and optionally `OPENAI_ORG_ID`). No requirements.txt — packages used: `openai`, `pandas`, `numpy`, `matplotlib`, `tiktoken`, `scikit-learn`.

### Ground truth
`science-data_and_code/data/processed_data/df_paired_val.csv` — contains `CONFIG_configId`, `treatment_itt_efficiency`, `control_itt_efficiency`. The "baseline" model uses control efficiency as the prediction.

### RAG setup
OpenAI Vector Store `vs_68e867cb856881919afaf916060dcea8` (`pgg_elig`) holds ~757 paper PDFs uploaded via `predict_RAG.ipynb`. Filtered RAG uses `collection_mapping_251110.json` to restrict retrieval to relevant subsets of papers per prediction query.
