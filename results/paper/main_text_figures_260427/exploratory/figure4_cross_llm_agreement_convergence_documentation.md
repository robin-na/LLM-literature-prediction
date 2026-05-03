# figure4_cross_llm_agreement_convergence

## Purpose
Exploratory two-panel candidate for a possible `main_text_260427` Figure 4 focused on cross-LLM agreement across individual papers. This variant does not replace the current canonical Figure 4 mapping in `figure_manifest.csv`.

## Output files
- Plot PNG: `plots/paper/main_text_260427/exploratory/figure4_cross_llm_agreement_convergence.png`
- Paper-level convergence rows: `results/paper/main_text_figures_260427/exploratory/figure4_cross_llm_agreement_convergence_paper_rows.csv`
- Pairwise agreement table: `results/paper/main_text_figures_260427/exploratory/figure4_cross_llm_agreement_convergence_pairwise.csv`
- Summary table: `results/paper/main_text_figures_260427/exploratory/figure4_cross_llm_agreement_convergence_summary.csv`
- Documentation: `results/paper/main_text_figures_260427/exploratory/figure4_cross_llm_agreement_convergence_documentation.md`
- Script: `analysis/paper_figures/plot_figure4_cross_llm_agreement_convergence_260427.py`

## Input files
- Canonical Figure 3 rows: `results/paper/main_text_figures_260427/figure3_paper_heterogeneity_agreement_rows.csv`

## Construction
1. Start from the canonical `260427` Figure 3 paper-level rows for the three main-text models.
2. Restrict to papers shared by all three models, yielding 2,010 papers.
3. Panel A computes pairwise Pearson correlations between the three model-specific paper-level augmented performance vectors.
4. Panel B computes, for each shared paper, the mean pairwise absolute gap in augmented correlation across the three models.
5. The Panel B reference line is the corresponding mean pairwise absolute gap across the three unaugmented model baselines.
6. Papers below that line are labeled as reducing cross-model performance gaps; papers above it are labeled as increasing them.

## Estimands
- Panel A: `corr(paper-level augmented correlation vector for model a, paper-level augmented correlation vector for model b)` across shared papers.
- Panel B: `mean(|r_a - r_b|, |r_a - r_c|, |r_b - r_c|)` across the three displayed LLMs for a given paper.

## Summary values
|   n_shared_papers |   baseline_mean_pairwise_abs_gap |   baseline_cross_model_sd |   baseline_cross_model_range |   n_reduce_gap |   share_reduce_gap |   n_increase_gap |   share_increase_gap |   mean_augmented_mean_pairwise_abs_gap |   median_augmented_mean_pairwise_abs_gap |   p05_augmented_mean_pairwise_abs_gap |   p95_augmented_mean_pairwise_abs_gap |
|------------------:|---------------------------------:|--------------------------:|-----------------------------:|---------------:|-------------------:|-----------------:|---------------------:|---------------------------------------:|-----------------------------------------:|--------------------------------------:|--------------------------------------:|
|              2010 |                         0.176736 |                  0.140881 |                     0.265104 |           1846 |           0.918408 |              164 |             0.081592 |                               0.092467 |                                 0.077861 |                              0.033531 |                              0.197839 |

## Pairwise agreement values
| model_a           | model_b        |   n_shared_papers |   pearson_r |   pearson_p_two_sided |
|:------------------|:---------------|------------------:|------------:|----------------------:|
| Claude Sonnet 4.6 | GPT-4.1        |              2010 |    0.297032 |                     0 |
| Claude Sonnet 4.6 | Gemini 2.5 Pro |              2010 |    0.305123 |                     0 |
| GPT-4.1           | Gemini 2.5 Pro |              2010 |    0.319347 |                     0 |
