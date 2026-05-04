# figure3_paper_heterogeneity_agreement

## Purpose
Figure 3 for `main_text_260427`. The current canonical version focuses on the 2,011 individual papers only and shows heterogeneity in absolute augmented prediction performance on the raw correlation scale with paper rank made explicit on the x-axis. Cross-LLM agreement is not rendered in the current main-text figure and can be handled separately in text or a companion figure.

## Inheritance
- Semantic figure intent: paper-level augmentation heterogeneity
- Adapted from `main_text_260415` Figure 2 variants:
  - `plots/paper/main_text_260415/figure2_individual_collection_density.png`
  - `plots/paper/main_text_260415/figure2_heterogeneity_and_cross_model_agreement.png`
- Collections are intentionally removed from the `260427` main-text version and can be handled in the supplement.

## Output files
- Plot PNG: `plots/paper/main_text_260427/figure3_paper_heterogeneity_agreement.png`
- Paper-level rows: `results/paper/main_text_figures_260427/figure3_paper_heterogeneity_agreement_rows.csv`
- Summary table: `results/paper/main_text_figures_260427/figure3_paper_heterogeneity_agreement_summary.csv`
- Pairwise agreement table: `results/paper/main_text_figures_260427/figure3_paper_heterogeneity_agreement_pairwise.csv`
- Documentation: `results/paper/main_text_figures_260427/figure3_paper_heterogeneity_agreement_documentation.md`
- Script: `analysis/paper_figures/plot_figure3_main_text_260427.py`

## Input files
- Paper-level augmented performance rows: `results/paper/main_text_figures_260409/paper_repeat_correlation_metrics.csv`
- No-augmentation 30-run baseline summary: `results/paper/main_text_figures_260409/figure1_panel_b_baseline_vs_humans_correlation_cdf_llm_mean30_model_summary.csv`
- Noise ceiling benchmark table: `results/validation/no_augmentation_model_comparison/validation_no_augmentation_model_comparison_benchmarks.csv`

## Estimand
- Paper-level augmented performance: `corr(mean prediction across augmentation repeats, true outcome)` for each of the 2,011 papers.
- No-augmentation baseline marker: `corr(mean prediction across 30 baseline runs, true outcome)`.

## Construction
1. Restrict to the three main-text models: `Claude Sonnet 4.6`, `GPT-4.1`, and `Gemini 2.5 Pro`.
2. Take the paper-level `correlation` column from `paper_repeat_correlation_metrics.csv` for each model across all available papers.
3. Within each model, sort papers from worst to best augmented performance.
4. Plot paper percentile on the x-axis and raw augmented correlation on the y-axis in three side-by-side small multiples.
5. Divide each panel into four background regions using the no-augmentation baseline and the within-model crossover percentile, with darker shades for the realized underperformance and outperformance quadrants and lighter shades for the two counterfactual quadrants.
6. Plot sorted paper-level points in matching red and green based on whether each paper falls below or above the no-augmentation baseline.
7. Overlay the no-augmentation 30-run baseline as a solid black horizontal line and the estimated noise ceiling as a dotted black horizontal line, described by a compact figure-level legend.
8. Add one lower-left annotation reporting the share of papers that worsen prediction when given to the LLM.
9. Add a far-right summary gutter separated by a light vertical line, containing a small average point with a vertical 95% t interval across papers and a rotated `Average: ...` label.
10. Pairwise cross-LLM agreement is still computed into `figure3_paper_heterogeneity_agreement_pairwise.csv` as a companion table, but it is intentionally omitted from the current canonical main-text figure.

## Notes
- The figure stays on the raw-correlation scale so improvements are not overstated for lower-baseline models.
- `Paper percentile` is used rather than raw rank so the x-axis remains directly comparable across the three panels despite the one-paper difference for `GPT-4.1`.
- The displayed mean interval is a descriptive 95% interval for the average correlation across papers within a model, not a CI for a single paper-level correlation.
- Confidence intervals are intentionally omitted from the main panel. Raw-correlation CIs across only 20 validation experiments are large enough to visually swamp the paper-to-paper heterogeneity signal, while delta-based paired CIs would mismatch the raw-correlation y-axis.
- `GPT-4.1` has one fewer source paper in the corrected table, so its panel contains `2010` papers while the other two panels contain `2011`.

## Summary values
| model             |   n_items |   mean_correlation |   mean_correlation_ci_low |   mean_correlation_ci_high |   median_correlation |   p05_correlation |   p25_correlation |   p75_correlation |   p95_correlation |   min_correlation |   max_correlation |   baseline_correlation_mean30 |   n_above_baseline |   share_above_baseline |
|:------------------|----------:|-------------------:|--------------------------:|---------------------------:|---------------------:|------------------:|------------------:|------------------:|------------------:|------------------:|------------------:|------------------------------:|-------------------:|-----------------------:|
| Claude Sonnet 4.6 |      2011 |           0.656572 |                  0.655432 |                   0.657713 |             0.657171 |          0.616414 |          0.641111 |          0.673328 |          0.696953 |          0.403834 |          0.773322 |                      0.664486 |                768 |               0.3819   |
| GPT-4.1           |      2010 |           0.58596  |                  0.584029 |                   0.587891 |             0.586453 |          0.527332 |          0.562375 |          0.609922 |          0.651733 |          0.030176 |          0.782605 |                      0.614593 |                422 |               0.20995  |
| Gemini 2.5 Pro    |      2011 |           0.52802  |                  0.523917 |                   0.532123 |             0.549116 |          0.347421 |          0.494011 |          0.580896 |          0.644046 |          0.027303 |          0.834929 |                      0.399382 |               1824 |               0.907011 |

## Companion pairwise agreement values
| model_a           | model_b        |   n_shared_papers |   pearson_r |   pearson_p_two_sided |   spearman_rho |   spearman_p_two_sided |   kendall_tau |   kendall_p_two_sided |
|:------------------|:---------------|------------------:|------------:|----------------------:|---------------:|-----------------------:|--------------:|----------------------:|
| Claude Sonnet 4.6 | GPT-4.1        |              2010 |    0.297032 |                     0 |       0.195119 |                      0 |      0.132105 |                     0 |
| Claude Sonnet 4.6 | Gemini 2.5 Pro |              2011 |    0.304147 |                     0 |       0.22768  |                      0 |      0.155473 |                     0 |
| GPT-4.1           | Gemini 2.5 Pro |              2010 |    0.319347 |                     0 |       0.222671 |                      0 |      0.152724 |                     0 |
