# LLM Literature Prediction

Research project studying whether augmenting LLM prompts with academic literature improves predictions of Public Goods Game (PGG) experiment outcomes. Specifically, we predict how enabling a punishment mechanism changes game **efficiency** — the ratio of actual group payoff to maximum cooperative payoff — across diverse experimental designs.

---

## Repository Structure

| Module | Purpose |
|--------|---------|
| [`extraction/`](extraction/extraction.md) | LLM pipeline for extracting structured data from 810 PGG papers using GPT-4.1 via the OpenAI Batch API |
| [`evaluator/`](evaluator/README.md) | Tool for comparing LLM extraction quality against human ground truth (field-level accuracy, mismatch reports, review UI) |
| [`prediction/`](prediction/) | Prediction pipeline: parse LLM outputs, compute metrics (RMSE, correlation, directional accuracy), generate figures |
| [`prediction_inputs/`](prediction_inputs/) | Shared literature filter utilities and paper-only prompt variants used by the literature batch builders |
| [`literature/`](literature/) | Batch input builders for literature-augmented prediction runs (abstracts, full texts, synthesis reports, RAG) |
| [`positive_cases/`](positive_cases/) | Agentic report generation and prompt variation analysis for individual prediction cases |
| [`extraction_app/`](extraction_app/) | Flask web UI for manually validating or correcting automated paper extractions |
| [`notebooks/`](notebooks/) | Jupyter notebooks for paper figures and exploratory prediction runs |
| [`science_data/`](science_data/README.md) | Experimental platform (Meteor/Node.js), raw game data, and reproduction code for the PGG experiments |
| [`input/`](input/) | PGG experiment configuration CSVs (validation and learning sets) |
| [`PGG_papers/`](PGG_papers/) | Paper metadata CSVs; actual `.md` files are downloaded separately from Google Drive |
| [`docs/`](docs/) | Academic supplementary materials (LaTeX SI for the extraction pipeline) |

---

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

For the evaluator, install its own dependencies:

```bash
pip install -r evaluator/requirements.txt
```

For the experimental platform and reproduction analysis, see [`science_data/README.md`](science_data/README.md).

### 2. Set API keys

```bash
cp .env.example .env
# Edit .env and fill in your OPENAI_API_KEY and ANTHROPIC_API_KEY
```

### 3. Download papers from Google Drive

Papers are stored as `.md` files in a shared Google Drive folder. See [`extraction/extraction.md`](extraction/extraction.md) for one-time setup.

```bash
python extraction/download_papers_md.py --pdf-list my_papers.txt
```

### 4. Run paper extraction

```bash
# Submit batch job (saves batch ID to console)
python extraction/extract_papers.py batch-submit \
  --paper-dir PGG_papers/papers \
  --paper-ids $(ls PGG_papers/papers/*.md | xargs -n1 basename | sed 's/\.md$//') \
  --save-jsonl extraction/inputs/batch_input.jsonl

# Check status
python extraction/extract_papers.py batch-status <batch_id>

# Collect results
python extraction/extract_papers.py batch-collect <batch_id> \
  --output-xlsx extraction/output_xlsx/extraction.xlsx
```

### 5. Compute prediction metrics

```bash
python prediction/prediction_metrics.py \
  --input-dir openAI_batch_output \
  --results-dir results \
  --ground-truth science_data/data/processed_data/df_paired_val.csv \
  --platform openai
```

---

## Data

### What is gitignored

Large files are not committed to the repo and must be obtained separately:

| Path | Description | How to obtain |
|------|-------------|---------------|
| `PGG_papers/papers/` | 810 PGG papers in Markdown format (70 MB) | Download via `extraction/download_papers_md.py` from Google Drive |
| `extraction/output_xlsx/` | Extraction results in XLSX format | Run the extraction pipeline |
| `openAI_batch_output/` | Raw LLM prediction JSONL outputs | Run prediction batch jobs |
| `results/` | Parsed prediction CSVs and metric summaries | Run `prediction/prediction_metrics.py` |

### Ground truth

`science_data/data/processed_data/df_paired_val.csv` — contains `CONFIG_configId`, `treatment_itt_efficiency`, and `control_itt_efficiency` for the 75 validation configurations. The baseline model uses control efficiency as its prediction.

---

## Evaluator

The `evaluator/` module compares LLM extractions against human-annotated ground truth. It supports:

- **Stage 1**: Browser UI for resolving multi-annotator disagreements (`python evaluator/main.py consensus --open`)
- **Stage 2**: Field-level accuracy matrix and mismatch report (`python evaluator/main.py evaluate`)

See [`evaluator/README.md`](evaluator/README.md) for full usage.

---

## Extraction

Structured experimental parameters were extracted from **810 PGG papers** using a fully automated LLM pipeline. The pipeline converts each paper's full text into condition-level rows capturing experimental design, independent/dependent variables, participant characteristics, and data provenance.

- **Model:** GPT-4.1 (OpenAI), temperature 0
- **API:** OpenAI Batch API (~50% cost reduction vs. real-time)
- **Output:** 808 papers extracted, 3,910 condition rows, 45 fields per condition

Full methodology: [`extraction/extraction.md`](extraction/extraction.md)  
Formal SI write-up: [`docs/extraction_SI.tex`](docs/extraction_SI.tex)

---

## Augmentation Strategies

Five literature augmentation strategies are compared in the prediction experiments:

| Strategy | Description |
|----------|-------------|
| Baseline | No literature augmentation |
| Abstract | Paper abstracts injected into prompt |
| Full text | Complete paper text injected |
| Synthesis | AI-generated literature synthesis report |
| RAG | Retrieval-augmented generation from a 757-paper vector store |

---

## Paper Figures

- Narrative overview: [`prediction/paper_figures/README.md`](prediction/paper_figures/README.md)
- Detailed derivations and data sources: [`prediction/paper_figures/figure_derivation_notes.md`](prediction/paper_figures/figure_derivation_notes.md)

---

## Citation

If you use this code or data, please cite the associated paper (see `docs/` for the supplementary information document).
