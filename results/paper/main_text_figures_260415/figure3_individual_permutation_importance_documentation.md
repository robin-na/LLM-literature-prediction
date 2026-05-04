# Figure 3 Individual-Paper Permutation Importance

Outputs:
- OLS plot: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/plots/paper/main_text_260415/figure3_individual_permutation_importance_ols.png`
- Ridge plot: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/plots/paper/main_text_260415/figure3_individual_permutation_importance_ridge.png`
- OLS rows: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/results/paper/main_text_figures_260415/figure3_individual_permutation_importance_ols_rows.csv`
- Ridge rows: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/results/paper/main_text_figures_260415/figure3_individual_permutation_importance_ridge_rows.csv`

Purpose:
- Exploratory companion to Figure 3 showing which individual-paper metadata variables matter most for predicting augmented performance.
- Target is raw augmented performance, `Corr(y_true, y_pred)`, matching Figure 3.

Construction:
- LLMs: `Claude Sonnet 4.6`, `GPT-4.1`, and `Gemini 2.5 Pro`.
- Rows: individual papers only (`n = 2,010, 2,011` depending on model availability).
- Features: same individual-paper metadata as Figure 3: empirical-paper indicator, log citation count, log journal impact factor, publication year, and journal-discipline indicators.
- Preprocessing: median imputation and standardization inside each training fold.
- Estimators:
  - OLS / linear regression: same unregularized linear estimator used for Figure 3 predictive-performance documentation.
  - Ridge regression: `RidgeCV` over `np.logspace(-3, 3, 13)`, included because ridge was the best predictive model for individual papers in the Figure 3 benchmark table.
- Importance: 5-fold grouped cross-validation by paper ID. Within each held-out fold, each feature is permuted 100 times and importance is the percent increase in held-out RMSE relative to the unpermuted held-out prediction.
- Error bars: standard error across the 5 held-out folds.

Interpretation:
- Larger positive values mean predictions get worse when that feature is broken, so the model relies more on that feature for held-out prediction.
- Values near zero mean little held-out predictive contribution.
- Negative values can occur when a feature adds noise in held-out data.
- Because predictors are correlated, permutation importance is a predictive-utility measure, not a causal or uniquely attributable effect size.
