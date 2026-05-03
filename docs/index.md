# Documentation Index

All project documentation lives here. Sub-folders group docs by topic; formal publication materials are in `formal/`.

---

## Extraction

How PGG experimental parameters are extracted from papers into a structured dataset.

| Document | Description |
|----------|-------------|
| [extraction/pipeline.md](extraction/pipeline.md) | Automated extraction pipeline: schema, prompt design, CLI reference, post-processing |
| [extraction/agentic.md](extraction/agentic.md) | Hybrid agentic extraction: V2 pipeline, tools, field profiles, merge rules |
| [extraction/app.md](extraction/app.md) | Manual extraction web app: setup, interface, keyboard shortcuts, field definitions, export |

---

## Literature Augmentation

How the PGG literature is organised into collections and used to augment predictions.

| Document | Description |
|----------|-------------|
| [literature/augmentation_pipeline.md](literature/augmentation_pipeline.md) | Literature workspace: all scripts, commands, evidence cards, synthesis, prediction batch building |
| [literature/metadata_collections.md](literature/metadata_collections.md) | Metadata collection specification: filter dimensions, quartile cut points, naming, retention counts |

---

## Prediction & Reporting

How augmented predictions are generated, evaluated, and reported.

| Document | Description |
|----------|-------------|
| [prediction/agentic_reports.md](prediction/agentic_reports.md) | Agentic prediction support reports: OpenAI Responses API, report methods, batch building, notebook workflow |
| [prediction/results_layout.md](prediction/results_layout.md) | Results directory layout: validation subfolders, positive-case analyses |

---

## Analysis

Scripts and notes for evaluating augmentation performance and producing paper figures.

| Document | Description |
|----------|-------------|
| [analysis/figures.md](analysis/figures.md) | Paper figure narrative: what each figure shows, intended messages, caveats |
| [analysis/figure_derivations.md](analysis/figure_derivations.md) | Figure derivation notes: scripts, inputs, outputs, construction details for all 8 figures |
| [analysis/single_paper_analysis.md](analysis/single_paper_analysis.md) | Single-paper augmentation analysis scripts: validation, significance, features, ranking |
| [analysis/collection_analysis.md](analysis/collection_analysis.md) | Collection report analysis scripts: stage-1 evaluation, repeat-5 averaging, convergence |
| [analysis/repeat5_variance_note.md](analysis/repeat5_variance_note.md) | Technical note: repeat-5 variance, baseline heterogeneity, candidate analysis strategies |

---

## Formal Publication Materials

| Document | Description |
|----------|-------------|
| [formal/extraction_SI.tex](formal/extraction_SI.tex) | LaTeX source for the extraction supplementary information |
| [formal/SI_extraction.docx](formal/SI_extraction.docx) | Built Word version of the extraction SI |
| [formal/build_si_docx.py](formal/build_si_docx.py) | Script that builds `SI_extraction.docx` from the schema and narrative |
