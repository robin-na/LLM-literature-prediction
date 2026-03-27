# Agentic PGG Prediction Support Report

This folder contains a small pipeline that calls the OpenAI Responses API to:
- Analyze `df_analysis_learn.csv` with Code Interpreter.
- Summarize the published PDF with File Search over a vector store.
- Synthesize a final prediction-support report in Markdown.
- For the newer paper-only variants, retrieve directly from the paper vector store and synthesize the final report in one Responses API call.

## How It Works (OpenAI API Calls)
The implementation lives under `positive_cases/agentic_report/` and uses the official Python SDK.

OpenAI functions used:
- `client.files.create(...)` to upload the CSV and PDF as files for the API to access.
- `client.vector_stores.create(...)` and `client.vector_stores.files.create_and_poll(...)` to build a vector store for the paper, enabling `file_search`.
- `client.responses.create(...)` with `tools=[{"type": "code_interpreter"}]` to run statistical analysis on the CSV inside the sandboxed tool.
- `client.responses.create(...)` with `tools=[{"type": "file_search", "vector_store_ids": [...], "max_num_results": 50}]` to retrieve paper passages and summarize them.
- `client.responses.create(...)` (no tools) to synthesize the final report from the memos and base prompt.
- `client.responses.create(...)` with `tools=[{"type": "file_search", "vector_store_ids": [...], "max_num_results": 50}]` to generate the new direct paper-only report variants without an intermediate `paper_memo.md`.

Retrieval configuration:
- vector store chunking strategy: OpenAI default `auto`
- current default chunking behavior from the Retrieval guide: `800` token chunks with `400` token overlap
- `max_num_results`: `50`
- `include=["file_search_call.results"]` is enabled on paper-retrieval calls, so the saved log includes tool queries and raw retrieved result payloads

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

Export prompt previews for the new direct paper-only variants before running them:
```bash
python positive_cases/export_prompt_previews.py \
  --methods paper_only_narrative paper_only_decision
```

This writes:
- `positive_cases/prompt_previews/paper_only_narrative.md`
- `positive_cases/prompt_previews/paper_only_decision.md`

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
- `file_search_log.json` for any variant that uses paper retrieval

Each generated custom variant stores:
- `agentic_report.md`
- `report_generation_prompt.md`
- `file_search_log.json` when paper retrieval is used
- copied source memo files
- `variant_metadata.json`

The resulting run bundle is saved under `results/notebook_positive_case_prompt_lab/`.

Main analysis outputs under `results/` now mirror the `plots/` layout, for example:
- `results/validation/no_augmentation_model_comparison/`
- `results/validation/augmentation_delta_by_model/`
- `results/validation/augmentation_convergence/`
- `results/validation/model_suite_comprehensive/`
- `results/validation/reasoning_repeat_summary/`

Named report methods currently supported:
- `paper_only_freeform`
- `paper_only_narrative`
- `data_only_freeform`
- `both_freeform`
- `paper_only_structured`
- `paper_only_decision`
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

Method notes:
- `paper_only_narrative`
  Uses the Responses API with `file_search` directly against the paper vector store in one call.
  It is narrative-driven and requires explicit acknowledgment of missing evidence.
- `paper_only_decision`
  Uses the same one-call `file_search` flow, but asks for a more decision-support-oriented output with a moderator matrix and decision rules.
- The older `paper_only_freeform`, `paper_only_structured`, and `paper_only_quantitative` methods are unchanged and still use the memo-then-report flow.
- All paper-retrieval paths now request up to `50` retrieved chunks and persist `file_search_log.json` with the prompt text, tool queries, and retrieved result payloads.

Build model-specific OpenAI batch files for the two new paper-only retrieval variants
(`paper_only_narrative` and `paper_only_decision`) across the 4.1 family only:
```bash
python positive_cases/build_paper_only_new_variants_batch_input.py
```

This writes:
- `openAI_batch_input/prediction_positive_case_paper_only_narrative-decision_41.jsonl`
- `openAI_batch_input/prediction_positive_case_paper_only_narrative-decision_41mini.jsonl`
- `openAI_batch_input/prediction_positive_case_paper_only_narrative-decision_41nano.jsonl`

Behavior:
- includes exactly two augmented variants:
  - `paper_only_narrative`
  - `paper_only_decision`
- includes four elicitation modes for each variant:
  - `single w/o explanation`
  - `single with explanation`
  - `joint w/o explanation`
  - `joint with explanation`
- explanation-included modes are repeated `5` times per condition for comparability with the repeated baseline runs
- direct single-question requests include `logprobs=true` and `top_logprobs=20`
- explanation requests use JSON with `explanation` and `prediction`
- example custom IDs:
  - `paper_only_narrative/Q1`
  - `paper_only_narrative_explanation_rep1/Q1`
  - `paper_only_narrative_joint`
  - `paper_only_narrative_joint_explanation_rep1`
- these new files use `explanation` in prompts and custom IDs for the new variants only
- older historical generators and analysis code still use `reasoning` labels for backward compatibility

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

Build model-specific OpenAI positive-case batch files for single-question elicitation only
(no joint requests), across all registered report variants plus a baseline control:
```bash
python positive_cases/build_positive_case_model_batch_suite.py
```

This writes one combined file per model:
- `openAI_batch_input/prediction_positive_case_variants_single_o3.jsonl`
- `openAI_batch_input/prediction_positive_case_variants_single_o4mini.jsonl`
- `openAI_batch_input/prediction_positive_case_variants_single_35turbo.jsonl`
- `openAI_batch_input/prediction_positive_case_variants_single_4omini.jsonl`
- `openAI_batch_input/prediction_positive_case_variants_single_4o.jsonl`
- `openAI_batch_input/prediction_positive_case_variants_single_gpt51.jsonl`

Default models:
- `o3`
- `o4-mini`
- `gpt-3.5-turbo`
- `gpt-4o-mini`
- `gpt-4o`
- `gpt-5.1`

For `gpt-5.1`, use direct-only generation when you need logprobs, and the generator
will cap `top_logprobs` at `5`:
```bash
python positive_cases/build_positive_case_model_batch_suite.py --models gpt-5.1 --direct-only
```

Behavior:
- each file contains both direct-output and reasoning requests
- direct-output requests ask for integer-only answers and include `logprobs=true` with `top_logprobs=20`
- reasoning requests ask for JSON with `reasoning` and `prediction`
- o-series payloads use a `developer` instruction message and omit `temperature`
- non-o-series payloads use the existing `system` message pattern and keep `temperature`

Build model-specific OpenAI positive-case batch files for joint 20-question elicitation
only, across all registered report variants plus a baseline control:
```bash
python positive_cases/build_positive_case_model_joint_batch_suite.py
```

This writes one combined file per model:
- `openAI_batch_input/prediction_positive_case_variants_joint_o3.jsonl`
- `openAI_batch_input/prediction_positive_case_variants_joint_o4mini.jsonl`
- `openAI_batch_input/prediction_positive_case_variants_joint_35turbo.jsonl`
- `openAI_batch_input/prediction_positive_case_variants_joint_4omini.jsonl`
- `openAI_batch_input/prediction_positive_case_variants_joint_4o.jsonl`
- `openAI_batch_input/prediction_positive_case_variants_joint_gpt51.jsonl`

Behavior:
- GPT-family files contain both `joint` and `joint_reasoning` requests
- `o3` and `o4-mini` files contain `joint_reasoning` requests only
- joint direct requests return JSON objects mapping `Q1...Q20` to integer predictions
- joint reasoning requests return JSON objects mapping `Q1...Q20` to `{reasoning, prediction}`
- no logprobs are requested for joint modes
- o-series payloads use a `developer` instruction message and omit `temperature`
- non-o-series payloads use the existing `system` message pattern and keep `temperature`

Build repeated reasoning-only positive-case batch files, covering both one-at-a-time
reasoning and joint reasoning. This is useful for measuring decoding variance across
repeated stochastic calls and comparing it to a `temperature=0` anchor:
```bash
python positive_cases/build_positive_case_reasoning_repeat_batch_suite.py
```

This writes one file per model, for example:
- `openAI_batch_input/prediction_positive_case_reasoning_repeats_35turbo.jsonl`
- `openAI_batch_input/prediction_positive_case_reasoning_repeats_41.jsonl`
- `openAI_batch_input/prediction_positive_case_reasoning_repeats_41mini.jsonl`
- `openAI_batch_input/prediction_positive_case_reasoning_repeats_41nano.jsonl`
- `openAI_batch_input/prediction_positive_case_reasoning_repeats_4omini.jsonl`
- `openAI_batch_input/prediction_positive_case_reasoning_repeats_4o.jsonl`
- `openAI_batch_input/prediction_positive_case_reasoning_repeats_o3.jsonl`
- `openAI_batch_input/prediction_positive_case_reasoning_repeats_o4mini.jsonl`
- `openAI_batch_input/prediction_positive_case_reasoning_repeats_gpt51.jsonl`

Behavior:
- includes all built-in report variants plus the baseline condition
- includes both single-question reasoning and joint reasoning
- runs `n=4` repeated stochastic calls per condition by default
- non-o-series models also include a `temperature=0` anchor
- custom ids use suffixes like `rep1`, `rep2`, `rep3`, `rep4`, and `temp0`

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
