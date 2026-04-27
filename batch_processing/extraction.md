# PGG Paper Extraction — Methodology & Usage

This document describes the automated data extraction pipeline used to extract structured experimental parameters from Public Goods Game (PGG) papers. It covers the extraction schema, pipeline design, prompt engineering, and CLI reference.

For the formal academic write-up see [`docs/extraction_SI.tex`](../docs/extraction_SI.tex).

---

## Overview

The pipeline reads full-text Markdown versions of academic papers and extracts structured data at the **condition level** — one row per experimental treatment or control arm. The output is an Excel workbook with one row per condition and up to 136 columns (45 fields × 3 columns each: value, reason, confidence).

### Pipeline

```
PDFs on Google Drive
        │
        ▼
[download_papers_md.py]
  OAuth2 authentication → search Drive folder "papers_markdown"
  → download .md files → PGG_papers/papers/<doi>.md
        │
        ▼
[extract_papers_app.py  batch-submit]
  For each paper: build prompt (schema + instructions + full text)
  → write JSONL → upload to OpenAI → submit Batch API job
  → print batch_id
        │
        ▼  (up to 24 hours, ~50% cheaper than real-time)
[OpenAI Batch API — gpt-4.1, temperature 0]
        │
        ▼
[extract_papers_app.py  batch-collect]
  Download JSONL results → parse experiments lists
  → coerce types → fill_paper_level_counts()
  → write Excel workbook
        │
        ▼
batch_processing/output_xlsx/<name>.xlsx
  Sheet "extractions" — one row per condition
```

---

## Extraction Schema

Each field produces three columns in the output: `{field}`, `{field}_reason`, `{field}_confidence`. Fields use `N/A` (not applicable to this condition) or `N/R` (applicable but not reported).

### Condition Identification

| Field | Type | Granularity | Description |
|-------|------|------------|-------------|
| `data_id` | string | condition | Label the paper uses for this condition (e.g. "Experiment 1 – Punishment Treatment") |
| `indep_var` | string | condition | Independent variable(s) and their value(s) for this row (e.g. "punishment_mechanism: yes, group_size: 4") |

### Method Classification

| Field | Type | Granularity | Description |
|-------|------|------------|-------------|
| `METHOD_empirical` | bool | condition | True if the study uses human participants |
| `METHOD_experiment` | bool | condition | True if controlled experiment; false if observational |
| `METHOD_lab` | bool | condition | True if lab-based; false if field experiment |
| `METHOD_simulation` | bool | condition | True if agent-based / computer simulation (no humans) |
| `METHOD_analytical` | bool | condition | True if formal mathematical model (no human subjects) |

### Experimental Configuration

| Field | Type | Granularity | Description |
|-------|------|------------|-------------|
| `CONFIG_playerCount` | int | condition | Number of strategic players per group. Teams count as one player each; do not report session headcount. |
| `CONFIG_numRounds` | int | condition | Number of game rounds or periods |
| `CONFIG_allOrNothing` | 0/1 | condition | **Counterintuitive name:** 1 = continuous contribution (any amount 0–endowment); 0 = binary all-or-nothing. N/A if not described. |
| `CONFIG_defaultContribProp` | 0–1 | condition | Fraction of endowment placed in public fund by default. 0 = standard VCM (private account default); 1 = opt-out game (public fund default). |
| `CONFIG_MPCR` | float | condition | Marginal per-capita return = group multiplier ÷ group size |
| `CONFIG_chat` | 0/1 | condition | 1 = unrestricted free-form communication allowed; 0 = explicitly prohibited; N/A if not mentioned |
| `CONFIG_showOtherSummaries` | 0/1 | condition | 1 = participants see others' contributions/earnings/punishments after each round; N/A if not mentioned |
| `CONFIG_showPunishmentId` | 0/1 | condition | 1 = punished player knows punisher identity; 0 = anonymous punishment; N/A if no punishment or not stated |
| `CONFIG_showRewardId` | 0/1 | condition | 1 = reward recipient can identify rewarder; N/A if no reward or not stated |
| `CONFIG_showNRounds` | 0/1 | condition | 1 only if paper explicitly states the round count or remaining rounds are displayed to participants. N/A if not stated — never 0 from silence. |
| `CONFIG_punishmentExists` | 0/1 | condition | 1 only if punishment mechanism explicitly described for this condition; N/A if not mentioned |
| `CONFIG_punishmentCost` | float | condition | Tokens the punisher spends per unit of punishment assigned. N/A if no punishment. |
| `CONFIG_punishmentTech` | float | condition | Reduction in target's payoff per unit of punishment received. N/A if no punishment. |
| `CONFIG_rewardExists` | 0/1 | condition | 1 only if reward mechanism explicitly described; N/A if not mentioned (never 0 from silence) |
| `CONFIG_rewardCost` | float | condition | Tokens the rewarder spends per unit of reward. N/A if no reward. |
| `CONFIG_rewardTech` | float | condition | Increase in recipient's payoff per unit of reward. N/A if no reward. |
| `CONFIG_endowment` | float | condition | Initial tokens per player per round |

### Independent and Dependent Variables

| Field | Type | Granularity | Description |
|-------|------|------------|-------------|
| `IVs` | JSON array | condition | Snake_case names of experimental factors varied across conditions in this paper and relevant to this condition. E.g. `["punishment_mechanism", "group_size"]`. Fixed parameters (e.g. endowment when never varied) are excluded. |
| `number_IVs` | int | **paper** | Count of unique IV names across all conditions in the paper. **Computed programmatically** (union of all IVs arrays, not asked to the LLM). Same value in every row for a given paper. |
| `DVs` | JSON array | condition | Snake_case names of outcome measures reported/analyzed for this specific condition. E.g. `["individual_contribution", "group_contribution", "punishment_assigned"]`. Conditions without punishment do not list punishment DVs. |
| `DVs_Definitions` | JSON object | condition | Maps each DV name in this row's DVs list to its paper-specific definition. Keys must exactly match DVs entries. |
| `number_DVs` | int | **paper** | Count of unique DV names across all conditions in the paper. **Computed programmatically** (union of all DVs arrays). Same value in every row for a given paper. |
| `DV_efficiencyReported` | 0/1 | **paper** | 1 if efficiency (actual group payoff / max cooperative payoff) is reported anywhere in the paper; 0 only if never appears. Same value in every row for a given paper. |

### Study Context

| Field | Type | Granularity | Description |
|-------|------|------------|-------------|
| `source_data` | string | **paper** | `"Internal"` = authors collected the data themselves (lab, online, or field); `"External"` = data borrowed from another experiment or external dataset (reanalysis). Same value in every row. |
| `participant_country` | string | condition | Country where experiment was conducted. N/R if not stated. |
| `participant_age` | string | condition | Age descriptor (e.g. "student", "18–35 years"). N/R if not stated. |
| `participant_gender` | string | condition | Gender composition: "mixed", "male only", "female only", or N/R. |
| `participant_education` | string | condition | Education level (e.g. "undergraduate students", "general population"). N/R if not stated. |
| `experiment_environment` | categorical | condition | One of: `"Online"`, `"On site"`, `"Field experiment"`, `"Observational"`, `"No human"` |
| `other_game_info` | string | condition | Free-text field for additional design details not captured elsewhere |

---

## Prompt Design

### Non-Inference Rule
The system prompt instructs the model:
> *"Only report a value when the paper explicitly states it or when it is directly and unambiguously computable from reported numbers. Do NOT infer values from silence, convention, or reasonable assumption."*

This is enforced separately for CONFIG fields (`N/A` for silence) and DV fields (`N/R` for unreported values). The distinction prevents false zeros and false negatives.

### N/A vs N/R
- **N/A** — the field does not apply to this condition (e.g. `CONFIG_punishmentCost` when `CONFIG_punishmentExists = N/A`)
- **N/R** — the field is applicable but the paper does not report the value

### Condition-Level Extraction
Each paper is expected to produce one JSON object per experimental condition. The LLM is instructed to create separate objects for each treatment arm, not to merge conditions.

### Reason and Confidence
For every field the model returns a `{field}_reason` (brief justification quoting or paraphrasing the paper) and `{field}_confidence` (self-assessed 0–1 numeric confidence).

---

## Post-Processing: Programmatic Counts

`number_IVs` and `number_DVs` are **not** extracted by the LLM. After collection, `fill_paper_level_counts()` (in `extraction_pipeline.py`) computes them:

1. Group all rows by `custom_id` (paper)
2. For each paper, parse the `IVs` and `DVs` JSON arrays from every condition row
3. Take the union of all IV names; count → `number_IVs`
4. Take the union of all DV names; count → `number_DVs`
5. Write the same integer to every row for that paper

This is more reliable than asking the LLM to count, which is prone to level-counting errors (e.g. treating "punishment: yes/no" as 2 IVs instead of 1).

---

## Output

**File:** `batch_processing/output_xlsx/<name>.xlsx`

**Sheet "extractions":**
- Columns: `custom_id` + (for each of 45 fields: `{field}`, `{field}_reason`, `{field}_confidence`) = 136 columns total
- Rows: one per experimental condition
- Arrays stored as JSON strings (`IVs`, `DVs`, `DVs_Definitions`)

---

## CLI Reference

Set environment variables before running:
```bash
set -a && source .env && set +a
```

### Download papers from Google Drive
```bash
# Download a specific list of papers (one DOI-based PDF path per line)
python batch_processing/download_papers_md.py \
  --pdf-list batch_processing/inputs/pdf_paths_800.txt \
  --output-dir PGG_papers/papers \
  --drive-folder papers_markdown
```
Already-existing files are skipped. Re-runnable safely.

### Batch API extraction (recommended for large runs — ~50% cheaper)

```bash
# Step 1: submit
python batch_processing/extract_papers.py batch-submit \
  --paper-dir PGG_papers/papers \
  --paper-ids $(cat batch_processing/inputs/paper_ids_800.txt | tr '\n' ' ') \
  --model gpt-4.1 \
  --save-jsonl batch_processing/inputs/batch_input_810papers.jsonl
# → prints batch_id, save it

# Step 2: check status (poll until "completed")
python batch_processing/extract_papers.py batch-status <batch_id>

# Step 3: collect results
python batch_processing/extract_papers.py batch-collect <batch_id> \
  --output-xlsx batch_processing/output_xlsx/simple_batch_810papers.xlsx \
  --save-jsonl batch_processing/inputs/batch_output_810papers.jsonl
```

### Real-time extraction (small runs / testing)
```bash
python batch_processing/extract_papers.py simple \
  --paper-dir PGG_papers/papers \
  --paper-ids 10.1007_s10645-008-9094-1 \
  --model gpt-4.1 \
  --output-xlsx batch_processing/output_xlsx/test.xlsx
```

### Hybrid extraction (simple + agentic overrides for error-prone fields)
```bash
python batch_processing/extract_papers.py hybrid \
  --paper-dir PGG_papers/papers \
  --paper-ids 10.1007_s10645-008-9094-1 \
  --agentic-version v2 \
  --output-xlsx batch_processing/output_xlsx/hybrid.xlsx
```

### Debug one field on one paper
```bash
python batch_processing/extract_papers.py agentic-field \
  --field CONFIG_MPCR \
  --paper-id 10.1007_s10645-008-9094-1 \
  --paper-dir PGG_papers/papers \
  --agentic-version v2 \
  --final-only
```
