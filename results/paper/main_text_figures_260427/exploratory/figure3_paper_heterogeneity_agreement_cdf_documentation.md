# figure3_paper_heterogeneity_agreement_cdf

## Purpose
Exploratory CDF variant for `main_text_260427` Figure 3. This version keeps the raw correlation scale on the x-axis and shows the cumulative share of papers on the y-axis.

## Output files
- Plot PNG: `plots/paper/main_text_260427/exploratory/figure3_paper_heterogeneity_agreement_cdf.png`
- Paper-level rows: `results/paper/main_text_figures_260427/exploratory/figure3_paper_heterogeneity_agreement_cdf_rows.csv`
- Summary table: `results/paper/main_text_figures_260427/exploratory/figure3_paper_heterogeneity_agreement_cdf_summary.csv`
- Pairwise agreement table: `results/paper/main_text_figures_260427/exploratory/figure3_paper_heterogeneity_agreement_cdf_pairwise.csv`
- Documentation: `results/paper/main_text_figures_260427/exploratory/figure3_paper_heterogeneity_agreement_cdf_documentation.md`
- Script: `analysis/paper_figures/plot_figure3_paper_heterogeneity_agreement_cdf_260427.py`

## Notes
- Panel A is a raw-correlation CDF: x-axis = augmented paper performance, y-axis = share of papers at or below that performance.
- The no-augmentation baseline is shown as a vertical dashed line, so the share above baseline can be read directly as `1 - F(baseline)`.
- This variant is exploratory and is not the canonical Figure 3 unless promoted later.

## Summary values
| model             |   n_items |   mean_correlation |   median_correlation |   p05_correlation |   p25_correlation |   p75_correlation |   p95_correlation |   min_correlation |   max_correlation |   baseline_correlation_mean30 |   n_above_baseline |   share_above_baseline |
|:------------------|----------:|-------------------:|---------------------:|------------------:|------------------:|------------------:|------------------:|------------------:|------------------:|------------------------------:|-------------------:|-----------------------:|
| Claude Sonnet 4.6 |      2011 |           0.656572 |             0.657171 |          0.616414 |          0.641111 |          0.673328 |          0.696953 |          0.403834 |          0.773322 |                      0.664486 |                768 |               0.3819   |
| GPT-4.1           |      2010 |           0.58596  |             0.586453 |          0.527332 |          0.562375 |          0.609922 |          0.651733 |          0.030176 |          0.782605 |                      0.614593 |                422 |               0.20995  |
| Gemini 2.5 Pro    |      2011 |           0.52802  |             0.549116 |          0.347421 |          0.494011 |          0.580896 |          0.644046 |          0.027303 |          0.834929 |                      0.399382 |               1824 |               0.907011 |

## Pairwise agreement values
| model_a           | model_b        |   n_shared_papers |   pearson_r |   pearson_p_two_sided |
|:------------------|:---------------|------------------:|------------:|----------------------:|
| Claude Sonnet 4.6 | GPT-4.1        |              2010 |    0.297032 |                     0 |
| Claude Sonnet 4.6 | Gemini 2.5 Pro |              2011 |    0.304147 |                     0 |
| GPT-4.1           | Gemini 2.5 Pro |              2010 |    0.319347 |                     0 |
