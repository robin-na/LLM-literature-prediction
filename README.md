# LLM Literature Prediction

Evaluating whether augmenting LLM prompts with academic literature improves predictions of Public Goods Game (PGG) experiment outcomes. The task is predicting how enabling a punishment mechanism changes a game's **efficiency** — the ratio of actual group payoff to the maximum cooperative payoff, expressed as a percentage.

## Project Structure

| Directory | Contents |
|-----------|----------|
| `batch_processing/` | Extraction pipeline: scripts, prompts, schema, CLI |
| `PGG_papers/papers/` | Paper Markdown files (downloaded from Google Drive) |
| `input/` | PGG experiment configurations (validation and learning sets) |
| `analysis/` | Prediction metrics, parsing, figure scripts |
| `results/` | Prediction output CSVs and metric summaries |
| `plots/` | Jupyter notebooks for paper figures |
| `docs/` | Academic documentation (SI LaTeX) |

## Paper Figures

- Narrative overview: [analysis/paper_figures/README.md](analysis/paper_figures/README.md)
- Detailed derivations and data sources: [analysis/paper_figures/figure_derivation_notes.md](analysis/paper_figures/figure_derivation_notes.md)

## Data Extraction

Structured experimental parameters were extracted from **810 PGG papers** using a fully automated LLM pipeline. The pipeline converts each paper's full text into condition-level rows, capturing experimental design, independent and dependent variables, participant characteristics, and data provenance.

- **Model:** GPT-4.1 (OpenAI), temperature 0
- **API:** OpenAI Batch API (~50% cost reduction vs. real-time)
- **Output:** 808 papers with extractable conditions, 3,910 condition rows, 45 fields per condition
- **Schema:** Condition-level (one row per treatment arm) with paper-level aggregations for `number_IVs`, `number_DVs`, `DV_efficiencyReported`, and `source_data`

Full methodology: [`batch_processing/extraction.md`](batch_processing/extraction.md)  
Formal SI write-up for publication: [`docs/extraction_SI.tex`](docs/extraction_SI.tex)

## Prediction Task

Given a PGG experimental configuration (group size, endowment, MPCR, punishment parameters, etc.), predict the efficiency change when a punishment mechanism is introduced. Augmentation strategies compared:

- **Baseline** — no literature augmentation
- **Abstracts** — paper abstracts injected into prompt
- **Full text** — full paper text injected
- **Synthesis reports** — AI-generated synthesis of relevant literature
- **RAG** — retrieval-augmented generation from a vector store of 757 papers

## Environment

```bash
# Required
export OPENAI_API_KEY=...

# Run extraction (see batch_processing/extraction.md for full workflow)
set -a && source .env && set +a
python batch_processing/extract_papers.py batch-submit --help

# Compute prediction metrics
python analysis/prediction_metrics.py \
  --input-dir openAI_batch_output \
  --results-dir results \
  --ground-truth science-data_and_code/data/processed_data/df_paired_val.csv \
  --platform openai
```

## Ground Truth

`science-data_and_code/data/processed_data/df_paired_val.csv` — contains `CONFIG_configId`, `treatment_itt_efficiency`, `control_itt_efficiency`. The baseline model uses control efficiency as the prediction.
