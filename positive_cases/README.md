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

Build prediction batch inputs from `input/pgg_CONFIGmerged_validation.csv`, augmented with
the generated reports in `positive_cases/output/{both,data_only,paper_only}/agentic_report.md`:
```bash
python positive_cases/build_positive_case_batch_input.py
```

This now writes merged output only:
- `openAI_batch_input/prediction_positive_cases_merged_52.jsonl`

Reasoning+JSON mode (no logprobs, temperature forced to 1.0, merged only):
```bash
python positive_cases/build_positive_case_batch_input.py --include-reasoning
```

This writes:
- `openAI_batch_input/prediction_positive_cases_reasoning_merged_52.jsonl`

Generate an Anthropic/Claude batch payload (single JSON object with `requests`):
```bash
python positive_cases/build_positive_case_batch_input.py --platform anthropic
```

This writes:
- `openAI_batch_input/prediction_positive_cases_anthropic_merged_sonnet46.json` (default model)

Anthropic Sonnet 4.6 (explicit):
```bash
python positive_cases/build_positive_case_batch_input.py \
  --platform anthropic \
  --model claude-sonnet-4-6
```

Anthropic Opus 4.6:
```bash
python positive_cases/build_positive_case_batch_input.py \
  --platform anthropic \
  --model claude-opus-4-6
```

Anthropic reasoning mode:
```bash
python positive_cases/build_positive_case_batch_input.py \
  --platform anthropic \
  --model claude-sonnet-4-6 \
  --include-reasoning
```

This writes:
- `openAI_batch_input/prediction_positive_cases_reasoning_anthropic_merged_sonnet46.json`

Submit Anthropic batch payload with curl:
```bash
curl https://api.anthropic.com/v1/messages/batches \
  --header "x-api-key: $ANTHROPIC_API_KEY" \
  --header "anthropic-version: 2023-06-01" \
  --header "content-type: application/json" \
  --data @openAI_batch_input/prediction_positive_cases_anthropic_merged_sonnet46.json
```

Custom IDs are formatted as:
- `science-paper_both/Q1 ... science-paper_both/Q20`
- `science-paper_data_only/Q1 ... science-paper_data_only/Q20`
- `science-paper_paper_only/Q1 ... science-paper_paper_only/Q20`

For Anthropic payloads (because `/` is not allowed), IDs are:
- `science-paper_both_Q1 ... science-paper_both_Q20`
- `science-paper_data_only_Q1 ... science-paper_data_only_Q20`
- `science-paper_paper_only_Q1 ... science-paper_paper_only_Q20`

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

For Anthropic API calls:
```bash
export ANTHROPIC_API_KEY="your_anthropic_key_here"
```

Optional: make it persistent by adding it to your shell config (for zsh, `~/.zshrc`) and reloading:
```bash
echo 'export OPENAI_API_KEY="your_api_key_here"' >> ~/.zshrc
echo 'export ANTHROPIC_API_KEY="your_anthropic_key_here"' >> ~/.zshrc
source ~/.zshrc
```

No additional package is needed to generate batch files/payloads with this script.
Optional: if you want to submit via Python SDK instead of curl, install Anthropic's SDK:
```bash
pip install anthropic
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
