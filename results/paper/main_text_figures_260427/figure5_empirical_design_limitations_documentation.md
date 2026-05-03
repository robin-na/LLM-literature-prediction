# Figure 5: Empirical Design Limitations

Inputs:
- `results/paper/lab_config_distributions_260427/combined_lab_extractions_broad_all_rows.csv`
- `plots/lab_config_distributions_260427/parameter_analysis_mentions_variation_vs_predictive_importance.csv`
- `input/pgg_CONFIGmerged_learn.csv`
- `input/pgg_CONFIGmerged_validation.csv`

Panel A uses `3630` filtered lab-experiment rows and the 12-parameter design set to count how many design parameters are reported in each extracted experiment.
Panel B uses `756` lab papers and 12 design parameters that have benchmark permutation-importance values. Pearson correlation between predictive importance and cross-paper variation is `r = -0.127`, `p = 0.693`.
Panel C shows literature-only value concentration across the same 12 design parameters. Each mini-heatmap uses the share of reported experiments in each observed value or benchmark-defined bin, on a 0-100% color scale.

Outputs:
- `results/paper/main_text_figures_260427/figure5_reported_parameter_count_rows.csv`
- `results/paper/main_text_figures_260427/figure5_variation_vs_importance_rows.csv`
- `results/paper/main_text_figures_260427/figure5_value_distribution_rows.csv`

Notes:
- ID-visibility merges punishment-ID and reward-ID visibility into one design parameter.
- Punishment-existence, reward cost, reward technology, and endowment are excluded from the 12-parameter set.
- For Panel C, continuous parameters use benchmark-defined quartile bins to keep the value ranges readable and comparable.
- Parameters are ordered by modal share, so the most concentrated distributions appear first.