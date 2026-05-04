# Figure 3: Metadata Coefficient Plot

Output:
- Figure: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/plots/paper/main_text_260415/figure3_metadata_coefficients.png`
- Rows: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/results/paper/main_text_figures_260415/figure3_metadata_coefficients_rows.csv`
- OLS predictive performance: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/results/paper/main_text_figures_260415/figure3_ols_predictive_performance.csv`

Purpose:
- Shows which paper or collection characteristics are positively or negatively associated with augmented prediction performance.
- The target is raw augmented performance, `Corr(y_true, y_pred)`, not correlation gain.

Construction:
- LLMs: `Claude Sonnet 4.6`, `GPT-4.1`, and `Gemini 2.5 Pro` (displayed as `Gemini Pro 2.5`).
- Panels: individual papers (n = 2,011) and collections (n = 717).
- Model: separate multivariable OLS for each LLM and panel.
- Predictors: log journal impact factor, log citation count, empirical-paper indicator/share, publication year, journal-discipline indicators, and log number of papers for collections.
- Predictors are grouped visually as study type, prestige/visibility proxies, publication timing, journal discipline, and collection scale.
- Continuous and binary predictors are median-imputed and standardized before fitting, so coefficients are comparable within a panel.
- Intervals are 95% HC3 robust confidence intervals from the OLS model.
- The x-axis is labeled as the standardized regression coefficient for prediction accuracy; the plotted intervals are 95% HC3 confidence intervals.
- Predictive performance is evaluated separately with grouped 5-fold cross-validation using the same features, median imputation, standardization, and an unregularized linear regression estimator.
- A positive coefficient means higher `Corr(y_true, y_pred)` after augmentation, conditional on the other displayed metadata variables.

Data sources:
- Individual-paper correlations: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/results/paper/main_text_figures_260409/paper_repeat_correlation_metrics.csv`
- Individual-paper metadata: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/literature/output/evidence_cards/literature_evidence_cards_cleaned/collection_metadata_sets/collection_metadata_catalog.csv`
- Collection correlations and metadata features: `build_collection_df()` from `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/analysis/paper_figures/plot_collection_linear_metadata_effect_260409.py`

Notes:
- OLS is used here instead of ridge because this figure is about interpretable conditional associations and sign, not out-of-sample prediction.
- The discipline coefficients are relative to the omitted discipline category captured by the intercept and other covariates.
- `Number of Papers` is not applicable for individual papers and is annotated as such in the individual-paper panel.
