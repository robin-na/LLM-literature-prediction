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

Generate the report-variation set with the OpenAI Responses API:
```bash
python positive_cases/run_report_variations.py \
  --methods both_structured both_quantitative both_rules both_contrastive both_uncertainty both_refined both_ensemble
```

Generate all six named report methods and skip ones already on disk:
```bash
python positive_cases/run_report_variations.py
```

Interactive notebook for prompt iteration on the validation positive-case task:
- Notebook: `positive_cases/positive_case_prompt_lab.ipynb`
- Helper module: `positive_cases/notebook_utils.py`
- Variant registry: `positive_cases/output/report_variant_registry.json`

The notebook is set up for:
- `gpt-4.1`
- reasoning JSON output
- one-question-at-a-time prediction
- sequential prediction calls
- live evaluation with correlation, RMSE, and directional accuracy

It is intentionally opinionated:
- the editable part is the **report-generation prompt**
- prediction-time prompting is fixed
- report augmentation for prediction is selected by **variant name**

Workflow:
1. choose `SOURCE_MODE` and `BASE_REPORT_STYLE`
2. edit `REPORT_PROMPT_ADDENDUM`
3. generate a named report variant under `positive_cases/output/<variant_name>/`
4. evaluate it by adding that variant name to `PREDICTION_VARIANTS`

Built-in variants now also store:
- `report_generation_prompt.md`

Each generated custom variant stores:
- `agentic_report.md`
- `report_generation_prompt.md`
- copied source memo files
- `variant_metadata.json`

The resulting run bundle is saved under `results/notebook_positive_case_prompt_lab/`.

Named report methods currently supported:
- `paper_only_freeform`
- `data_only_freeform`
- `both_freeform`
- `paper_only_structured`
- `data_only_structured`
- `both_structured`
- `paper_only_quantitative`
- `data_only_quantitative`
- `both_quantitative`
- `both_rules`
- `both_contrastive`
- `both_uncertainty`
- `both_refined`
- `both_ensemble`

Build one merged OpenAI batch input across report methods and elicitation modes:
```bash
python positive_cases/build_positive_case_variation_batch_input.py
```

This writes:
- `openAI_batch_input/prediction_positive_case_variations_41.jsonl`

Included conditions:
- Baseline, single-question, answer-only
- Baseline, single-question, reasoning JSON
- Baseline, joint 20-question, answer-only JSON
- Baseline, joint 20-question, reasoning JSON
- The same four elicitation modes for each generated report method

Joint 20-question elicitation uses a compact column guide and a single structured table, rather than repeating the full game description 20 times.

Build the learning-wave elicitation-only batch file (no augmentation, sorted by `CONFIG_configId`):
```bash
python positive_cases/build_learning_wave_elicitation_batch_input.py
```

This writes:
- `openAI_batch_input/prediction_learning_wave_elicitation_41.jsonl`

Build one merged OpenAI batch input across both validation and learning targets, all
elicitation variants, all generated report methods, and the experiment-catalog input
variants:
```bash
python positive_cases/build_crosswave_variation_batch_input.py \
  --model gpt-4.1 \
  --skip-baseline \
  --skip-experiment-inputs
python positive_cases/build_crosswave_variation_batch_input.py \
  --model gpt-4.1-mini \
  --skip-experiment-inputs
python positive_cases/build_crosswave_variation_batch_input.py \
  --model gpt-4.1-nano \
  --skip-experiment-inputs
```

This writes:
- `openAI_batch_input/prediction_crosswave_variations_41.jsonl`
- `openAI_batch_input/prediction_crosswave_variations_41mini.jsonl`
- `openAI_batch_input/prediction_crosswave_variations_41nano.jsonl`

Included condition families:
- `baseline` for the `gpt-4.1-mini` file
- every report method currently on disk

Optional switches:
- `--skip-baseline`
- `--skip-experiment-inputs`

Included elicitation modes for each family:
- single-question answer-only (`top_logprobs=20`)
- single-question reasoning JSON
- joint prediction over the full target wave, answer-only JSON
- joint prediction over the full target wave, reasoning JSON

Per-question IDs remain:
- validation: `.../Q1 ... /Q20`
- learning: `.../L1 ... /L150`

Joint-request IDs are dataset-qualified to avoid collisions in the merged file:
- `validation/baseline_joint`
- `learning/baseline_joint`
- `validation/both_structured_joint_reasoning`
- `learning/pgg_CONFIGmerged_learn_joint`

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
