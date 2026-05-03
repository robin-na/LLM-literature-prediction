# Exploratory Figure: Design-Space PCA Projection

Purpose:
- Explore whether a benchmark-fitted 2D projection shows broader coverage of the benchmark design space than the literature extraction set.

Inputs:
- `results/paper/lab_config_distributions_260427/combined_lab_extractions_broad_all_rows.csv`
- `input/pgg_CONFIGmerged_learn.csv`
- `input/pgg_CONFIGmerged_validation.csv`

Method:
- Use the same 12 design parameters as the current Figure 5.
- Convert all parameters into benchmark-supported bins or levels before encoding.
- Fit PCA on the benchmark one-hot design matrix only.
- Keep literature rows that report at least 8 of 12 design parameters (`n = 1005` rows from `293` papers).
- Fill the remaining missing literature values with benchmark modal bins only for projection into the benchmark PCA basis.

Explained variance: PC1 = `8.54%`, PC2 = `7.92%`.

Outputs:
- `results/paper/main_text_figures_260427/exploratory/figure5_design_space_pca_projection_rows.csv`
- `plots/paper/main_text_260427/exploratory/figure5_design_space_pca_projection.png`