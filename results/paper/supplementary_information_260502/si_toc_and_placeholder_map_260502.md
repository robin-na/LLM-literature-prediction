# SI table of contents and placeholder map, 2026-05-02

Google Doc editing status: not inserted into the manuscript.

Working document: Google Doc `LLM PGG Literature`, main tab `t.0`.

## Proposed SI table of contents

### S1. Prediction benchmark, evaluation metrics, and uncertainty estimates

Purpose: give the reproducible details behind the benchmark target, the correlation metric, bootstrapped intervals, paired comparisons, no-treatment baseline, noise ceiling, and alternative performance metrics.

Likely contents:
- S1.1 Benchmark experiments and target outcome
- S1.2 Correlation metric and rationale
- S1.3 Bootstrap procedure for confidence intervals and paired differences
- S1.4 No-treatment baseline
- S1.5 Noise ceiling calculation
- S1.6 Alternative metrics and robustness checks

### S2. Article corpus construction and full-text processing

Purpose: document the Web of Science searches, corpus accounting, full-text availability, Mathpix/PDF-to-markdown conversion, and final count reconciliation.

Likely contents:
- S2.1 Web of Science search criteria and citation-topic filter
- S2.2 Combined search accounting across the earlier and October 2025 searches
- S2.3 Full-text availability and conversion to markdown
- S2.4 Exclusion of the benchmark manuscript from the augmentation corpus
- S2.5 Corpus count summary: 3,087 records, 2,851 full-text documents, 2,011 analysis papers

### S3. Structured reports and relevance screening

Purpose: document the GPT-4.1 structured report generation and how those reports were used to retain the 2,011-paper broad augmentation corpus.

Likely contents:
- S3.1 Structured-report prompt and output schema
- S3.2 Report fields: study type, PGG relevance, outcomes, benchmark design dimensions, findings, and limitations
- S3.3 Broad relevance-screening rule
- S3.4 Internal screen labels and examples, kept out of the main text
- S3.5 Screening count summary

### S4. Literature augmentation inputs and collection construction

Purpose: document exactly what was given to LLM predictors under individual-paper and multi-paper augmentation.

Likely contents:
- S4.1 Individual-paper augmentation inputs
- S4.2 Consolidated collection reports
- S4.3 All-paper report
- S4.4 Metadata domains used for collection construction: study type, citation level, journal-impact quartile, publication period, and journal discipline
- S4.5 Count and construction of the 717 multi-paper collections

### S5. LLM prediction prompts, model versions, API parameters, and repeat averaging

Purpose: document LLM model identities, prompt text, API details, temperature, repetitions, parsing, and robustness to stochastic output variability.

Likely contents:
- S5.1 Models and provider APIs
- S5.2 Prediction prompt templates
- S5.3 Generation parameters, including temperature 1.0
- S5.4 Repeated calls: 30 for unaugmented and benchmark-paper conditions, 5 for individual-paper and collection-report augmentation
- S5.5 Prediction parsing and averaging across repeated calls
- S5.6 Robustness to API-call variability

### S6. LLM prediction results across all models and augmentation sets

Purpose: collect the supplementary LLM performance results that are too detailed for the main text.

Likely contents:
- S6.1 Results for all 8 LLMs
- S6.2 Baseline and benchmark-paper augmentation results
- S6.3 Individual-paper augmentation results for all models
- S6.4 Multi-paper collection augmentation results
- S6.5 All-paper report results
- S6.6 Cross-LLM agreement/convergence results
- S6.7 Model-size or model-family comparisons, if retained in Discussion

### S7. Metadata models for predicting augmented performance

Purpose: document the Fig. 4 modeling pipeline and robustness results.

Likely contents:
- S7.1 Paper metadata variables and transformations
- S7.2 Missing-data handling and grouped cross-validation
- S7.3 Statistical models: ordinary least squares, ridge, elastic net, random forest, extra trees, gradient boosting, and multilayer perceptron
- S7.4 Predictive performance across statistical models
- S7.5 Elastic-net coefficients and coefficient intervals
- S7.6 Permutation importance
- S7.7 Robustness across all 8 LLMs and 717 collections

### S8. LLM-assisted empirical-design extraction and human validation

Purpose: document GPT-5.1 extraction of empirical/laboratory status and experimental design parameters.

Likely contents:
- S8.1 Extraction sample and paper inclusion
- S8.2 Extraction prompt and schema
- S8.3 Condition-level extraction and non-inference rule
- S8.4 Coding rules for reported, not reported, and not applicable fields
- S8.5 Human validation sample and agreement results

### S9. Empirical design-space coverage analyses and robustness

Purpose: document the analyses behind Fig. 5 and related robustness checks.

Likely contents:
- S9.1 Construction of the 940 empirical-paper and 756 laboratory-paper samples
- S9.2 Reported-parameter count analysis
- S9.3 Parameter-variation analysis across papers
- S9.4 Comparison with benchmark-model parameter importance
- S9.5 Parameter-value coverage and concentration
- S9.6 Robustness checks and alternative coding choices

## Replacement map for live `SI Section X` placeholders

The live Google Doc main tab currently has 26 occurrences of `SI Section X`.

| Occurrence | Manuscript location / context | Replace with |
| ---: | --- | --- |
| 1 | Study Overview: `2,011 published articles... (see SI Section X for details)` | `SI Section S2` |
| 2 | Study Overview: consolidated literature reports for collections | `SI Section S4` |
| 3 | Study Overview: bootstrapping methods | `SI Section S1` |
| 4 | Study Overview: noise ceiling calculation | `SI Section S1` |
| 5 | Study Overview: results across other performance metrics | `SI Section S1` |
| 6 | Fig. 1 caption: prompting, report construction, and evaluation details | `SI Sections S1 and S3-S5` |
| 7 | Results opening: results for the other 5 LLMs | `SI Section S6` |
| 8 | Fig. 2 Results: benchmark-paper augmentation additional details | `SI Section S6` |
| 9 | Fig. 2 caption: details for bars, CIs, reference lines, and tests | `SI Sections S1, S5, and S6` |
| 10 | Fig. 3 Results: 717 multi-paper collections and all-paper report | `SI Section S6` |
| 11 | Fig. 3 caption: other LLMs and 717 collections | `SI Section S6` |
| 12 | Fig. 4 Results: metadata-model evaluation methods and performance across statistical models | `SI Section S7` |
| 13 | Fig. 4 Results: empirical-paper robustness across other LLMs and collections | `SI Section S7` |
| 14 | Fig. 4 caption: model specification and evaluation methods | `SI Section S7` |
| 15 | Fig. 4 caption: results across other LLMs and 717 collections | `SI Section S7` |
| 16 | Fig. 5 caption: extraction, coding, and robustness checks | `SI Sections S8 and S9` |
| 17 | Discussion draft: no significant signal from higher-performing/larger/newer models | `SI Section S6` |
| 18 | Materials and Methods, Article corpus: exact search criteria | `SI Section S2` |
| 19 | Materials and Methods, Article corpus: structured report details | `SI Section S3` |
| 20 | Materials and Methods, Article corpus: screening criteria based on structured reports | `SI Section S3` |
| 21 | Materials and Methods, Article corpus: exact grouping criteria for collections | `SI Section S4` |
| 22 | Materials and Methods, Prediction prompts: robustness across API-call variability | `SI Section S5` |
| 23 | Materials and Methods, Prediction prompts: exact LLM prompts and parameters | `SI Section S5` |
| 24 | Materials and Methods, Prediction prompts: evaluation procedure and other metrics | `SI Section S1` |
| 25 | Materials and Methods, Metadata models: performance across statistical models | `SI Section S7` |
| 26 | Materials and Methods, LLM extraction: extraction prompt, validation procedure, and results | `SI Section S8` |

## Suggested wording cleanup while replacing placeholders

- In places where a sentence currently has multiple `SI Section X` references in a row, combine them rather than replacing mechanically.
- Example:
  - Current: `See SI Section X for details on bootstrapping methods, SI Section X for the noise ceiling calculation, and SI Section X for results across other performance metrics.`
  - Suggested: `See SI Section S1 for bootstrapping methods, the noise-ceiling calculation, and results across other performance metrics.`
- Example:
  - Current: `See SI Section X for details on the structured report and SI Section X for the screening criteria based on it.`
  - Suggested: `See SI Section S3 for structured-report generation and relevance-screening criteria.`
- Example:
  - Current: `See Materials and Methods and SI Section X for model specification, evaluation methods, and SI Section X for results across other LLMs and 717 multi-paper collections.`
  - Suggested: `See Materials and Methods and SI Section S7 for model specification, evaluation methods, and robustness across other LLMs and multi-paper collections.`

## Open decisions

- If the convergence plot becomes part of the revised Fig. 3, keep its supporting methods/results in `SI Section S6`.
- If the Discussion placeholder about model size/generation is removed, occurrence 17 will no longer need replacement.
- If the SI becomes long, S8 and S9 could be merged into one section, but keeping them separate makes Fig. 5 easier to navigate.

