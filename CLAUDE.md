# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a research project evaluating whether augmenting LLM prompts with academic literature improves predictions of Public Goods Game (PGG) experiment outcomes. Specifically, the task is predicting how enabling a punishment mechanism changes a game's **efficiency** (ratio of actual group payoff to maximum cooperative payoff, expressed as a percentage integer).

Augmentation strategies tested: baseline (no literature), paper abstracts, full texts, AI-generated synthesis reports, and RAG (OpenAI vector store retrieval).

## Commands

### Download paper Markdown files from Google Drive
Papers are stored as `.md` files in a shared Google Drive folder (`Shared with me > PGG papers > papers_markdown`). Download them to `PGG_papers/papers/` before running extraction.

```bash
# Download using a hardcoded list (edit PDF_PATHS inside the script)
python extraction/download_papers_md.py

# Download from a text file (one PDF path per line)
python extraction/download_papers_md.py --pdf-list my_papers.txt

# Custom output dir or Drive folder name
python extraction/download_papers_md.py \
  --pdf-list my_papers.txt \
  --output-dir PGG_papers/papers \
  --drive-folder papers_markdown
```

**First-time setup** (one-time, per machine):
1. `pip install google-api-python-client google-auth-oauthlib google-auth-httplib2`
2. In [Google Cloud Console](https://console.cloud.google.com): enable Google Drive API → create OAuth 2.0 Desktop App credentials → download JSON → save as `extraction/gdrive_credentials.json`
3. In the OAuth consent screen (Audience tab): set User Type to **External**, add your Gmail as a test user
4. First run opens a browser for login; token cached in `extraction/gdrive_token.json` (both files are gitignored)

### Run simple paper extraction via OpenAI Batch API (~50% cheaper, ≤24h turnaround)
```bash
# Step 1: submit (saves batch ID to console)
python extraction/extract_papers.py batch-submit \
  --paper-dir PGG_papers/papers \
  --paper-ids $(ls PGG_papers/papers/*.md | xargs -n1 basename | sed 's/\.md$//') \
  --save-jsonl extraction/inputs/batch_input_simple.jsonl

# Step 2: check status
python extraction/extract_papers.py batch-status <batch_id>

# Step 3: collect results once completed
python extraction/extract_papers.py batch-collect <batch_id> \
  --output-xlsx extraction/output_xlsx/simple_batch.xlsx \
  --save-jsonl extraction/inputs/batch_output_simple.jsonl
```

### Run simple extraction (real-time, instant but full price)
```bash
python extraction/extract_papers.py simple \
  --paper-dir PGG_papers/papers \
  --paper-ids $(ls PGG_papers/papers/*.md | xargs -n1 basename | sed 's/\.md$//') \
  --output-xlsx extraction/output_xlsx/simple_extraction.xlsx
```

### Build batch input JSONL for paper extraction
```bash
python extraction/build_batch_input.py \
  --csv-path PGG_papers/WoS_251031_eligible.csv \
  --markdown-dir papers_markdown/ \
  --output extraction/inputs/batch_input.jsonl
```
Optional flags: `--model gpt-5.1`, `--temperature 0`, `--custom-ids <id1> <id2>`

### Compute prediction metrics (RMSE, correlation, directional accuracy with bootstrap CIs)
```bash
python prediction/prediction_metrics.py \
  --input-dir openAI_batch_output \
  --results-dir results \
  --ground-truth science_data/data/processed_data/df_paired_val.csv \
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
   - Jupyter notebooks (`notebooks/predict_individual.ipynb`, `notebooks/predict_RAG.ipynb`) — exploratory; build `OpenAI_batch_input/*.jsonl`
   - `extraction/build_batch_input.py` — CLI script for paper-extraction prompts
4. **OpenAI Batch API**: JSONL requests submitted via the API; outputs land in `openAI_batch_output/` (or `claude_batch_output/`)
5. **Parsing & metrics** (`prediction/`):
   - `jsonl_parser.py` — `jsonl_to_dataframe()` extracts numeric predictions from LLM output; handles logprobs-based mean, JSON structured output, and plain numeric fallback; supports both `openai` and `claude` platform formats
   - `prediction_metrics.py` — orchestrates loading, metric computation, and CSV writing
6. **Results** (`results/`): Named `prediction_YYMMDD_<type>_<model>.csv` + `_metrics.csv` + `_metrics_delta.csv`
7. **Analysis scripts** (`prediction/`): Standalone Python scripts for cross-wave analysis, elastic net comparisons, positive-case studies, and figure generation
8. **Plot notebooks** (`notebooks/`): Jupyter notebooks for final paper figures

### Custom ID convention
Prediction batch requests use `custom_id` format `<variation>/<augmentation_key>/Q<n>` (OpenAI slash separator) or `<variation>_Q<n>` (Claude underscore). `jsonl_parser.py` handles both.

### Key prompt structure
- **System prompt**: Defines the efficiency prediction task
- **User prompt**: `make_predict_prompt(make_config(row), augmented_text=...)` — config block prepended with optional augmentation text
- **Augmentation instructions** (`prompt_summary`, `prompt_abstract_individual`, `prompt_fulltext`, etc.): Wrap the injected literature text with appropriate framing

### Environment / API keys
Required env vars: `OPENAI_API_KEY` (and optionally `OPENAI_ORG_ID`). No requirements.txt — packages used: `openai`, `pandas`, `numpy`, `matplotlib`, `tiktoken`, `scikit-learn`.

### Ground truth
`science_data/data/processed_data/df_paired_val.csv` — contains `CONFIG_configId`, `treatment_itt_efficiency`, `control_itt_efficiency`. The "baseline" model uses control efficiency as the prediction.

### RAG setup
OpenAI Vector Store `vs_68e867cb856881919afaf916060dcea8` (`pgg_elig`) holds ~757 paper PDFs uploaded via `predict_RAG.ipynb`. Filtered RAG uses `collection_mapping_251110.json` to restrict retrieval to relevant subsets of papers per prediction query.
