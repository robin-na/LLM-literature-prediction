# Agentic PGG Prediction Support Report

This folder contains a small pipeline that calls the OpenAI Responses API to:
- Analyze `df_analysis_learn.csv` with Code Interpreter.
- Summarize the published PDF with File Search over a vector store.
- Synthesize a final prediction-support report in Markdown.

## How It Works (OpenAI API Calls)
The implementation lives under `positive_cases/agentic_report/` and uses the official Python SDK.

OpenAI functions used:
- `client.files.create(...)` to upload the CSV and PDF as files for the API to access.
- `client.vector_stores.create(...)` and `client.vector_stores.files.create_and_poll(...)` to build a vector store for the paper, enabling `file_search`.
- `client.responses.create(...)` with `tools=[{"type": "code_interpreter"}]` to run statistical analysis on the CSV inside the sandboxed tool.
- `client.responses.create(...)` with `tools=[{"type": "file_search", "vector_store_ids": [...]}]` to retrieve paper passages and summarize them.
- `client.responses.create(...)` (no tools) to synthesize the final report from the memos and base prompt.

## Run It
From the repo root:
```bash
python positive_cases/run_agentic_report.py
```

Outputs (by variant):
- `positive_cases/output/both/analysis_memo.md`
- `positive_cases/output/both/paper_memo.md`
- `positive_cases/output/both/agentic_report.md`

## Set Your API Key
macOS / Linux (zsh/bash):
```bash
export OPENAI_API_KEY="your_api_key_here"
```
OpenAI’s SDK automatically reads this environment variable.

Optional: make it persistent by adding it to your shell config (for zsh, `~/.zshrc`) and reloading:
```bash
echo 'export OPENAI_API_KEY="your_api_key_here"' >> ~/.zshrc
source ~/.zshrc
```

## Configuration
Variants:
```bash
# Use both data + paper (default)
python positive_cases/run_agentic_report.py --variant both

# Data only
python positive_cases/run_agentic_report.py --variant data_only

# Paper only
python positive_cases/run_agentic_report.py --variant paper_only
```

Environment variables supported by the pipeline:
- `OPENAI_MODEL` (default model for all steps)
- `OPENAI_ANALYSIS_MODEL`
- `OPENAI_SUMMARY_MODEL`
- `OPENAI_REPORT_MODEL`
- `OPENAI_FILE_PURPOSE` (default: `user_data`)

## Files
- `positive_cases/agentic_report/pipeline.py` main pipeline orchestrator.
- `positive_cases/agentic_report/prompts.py` prompt templates.
- `positive_cases/agentic_report/column_defs.py` CONFIG_ column descriptions.
- `positive_cases/agentic_report/config.py` file paths and defaults.
