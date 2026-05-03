# Figure Derivation Notes

Last updated: 2026-03-31

This note describes exactly how the current main-text figure set is derived, including the scripts, inputs, outputs, metrics, model subsets, and the most important caveats.

The active figure set is the raw-correlation version, not the adjusted-correlation sensitivity analysis.

## Regenerating The Figures

Current scripts:

- Figures 1-4:
  - `python analysis/literature_collection_analysis_reports/plot_paper_main_text_figures.py`
- Figure 5:
  - `python analysis/plot_figure5_rank_robustness.py`
- Figure 6:
  - `python analysis/plot_figure6_metadata_predictability_correlation.py`
- Figure 7:
  - `python analysis/plot_figure7_metadata_effect_robustness.py`
- Figure 8:
  - `python analysis/plot_figure8_collection_feature_importance_gpt41.py`

## Shared Conventions

- The main metric across Figures 1-4 is raw Pearson correlation between predicted and true treatment outcome across the 20 validation designs.
- All treatment outcomes are scaled to percentage points in the upstream figure scripts.
- The benchmark paper variant is `benchmark_pgg_ms`.
- The five-model set used in later figures is:
  - `GPT-4.1`
  - `GPT-4.1 Mini`
  - `GPT-5.1`
  - `GPT-5 Mini`
  - `GPT-5 Nano`

`GPT-4.1 Nano` is still included in Figure 2, but later figures focus on the five-model set above.

## Figure 1

**Files**

- Plot:
  - `plots/paper/main_text/figure1_panel_b_baseline_vs_humans_correlation_cdf.png`
  - `plots/paper/main_text/figure1_panel_b_baseline_vs_humans_correlation_cdf.pdf`
- Saved rows:
  - `results/paper/main_text_figures/figure1_panel_b_baseline_vs_humans_correlation_rows.csv`
  - `results/paper/main_text_figures/figure1_panel_b_baseline_vs_humans_correlation_reference_lines.csv`
  - `results/paper/main_text_figures/figure1_panel_b_baseline_vs_humans_correlation_cdf_percentiles.csv`

**Script**

- `analysis/literature_collection_analysis_reports/plot_paper_main_text_figures.py`

**Inputs**

- Human predictions:
  - `science-data_and_code/data/processed_data/prediction_survey.csv`
- Truth and no-treatment-effect reference:
  - `input/pgg_CONFIGmerged_validation.csv`
- Baseline LLM summary:
  - `results/validation/literature_collection_analysis_reports_repeat5/validation_literature_collection_analysis_report_repeat5_summary.csv`

**Construction**

- Keep only survey participants with:
  - valid predictions in the allowable range
  - `n_predictions_made == 20`
  - non-missing predictions on all 20 validation questions after pivoting to wide form
- Compute each human participant's correlation with the true treatment outcomes.
- Read one no-augmentation baseline correlation per model from the repeat-5 summary.
- Compute the "no treatment effect" reference as the correlation between control-group efficiency and the true treatment outcomes across the validation set.

**Display**

- Layperson and expert CDFs.
- Vertical lines for model-level no-augmentation baselines.
- Vertical line for the no-treatment-effect reference.

**Interpretation caveat**

This panel compares models to individual humans, not to human crowds.

## Figure 2

**Files**

- Plot:
  - `plots/paper/main_text/figure2_benchmark_report_vs_baseline_correlation.png`
  - `plots/paper/main_text/figure2_benchmark_report_vs_baseline_correlation.pdf`
- Saved rows:
  - `results/paper/main_text_figures/figure2_benchmark_report_vs_baseline_correlation_plot_rows.csv`
  - `results/paper/main_text_figures/figure2_benchmark_report_vs_baseline_correlation_summary.csv`

**Script**

- `analysis/literature_collection_analysis_reports/plot_paper_main_text_figures.py`

**Inputs**

- Benchmark-paper averaged predictions:
  - `results/validation/literature_collection_analysis_reports_repeat5/validation_literature_collection_analysis_report_repeat5_avg_predictions.csv`
- No-augmentation averaged predictions:
  - `results/validation/literature_collection_analysis_reports_repeat5/validation_literature_collection_analysis_report_repeat5_baseline_avg_predictions.csv`
- Validation truth:
  - `input/pgg_CONFIGmerged_validation.csv`
- Noise ceiling reference:
  - `results/validation/no_augmentation_model_comparison/validation_no_augmentation_model_comparison_benchmarks.csv`

**Construction**

- For each model, use the 5-repeat averaged prediction vector across the 20 questions for:
  - no augmentation
  - benchmark paper augmentation
- For each condition, compute the raw correlation with truth.
- For each bar, compute a question-bootstrap 95% CI by resampling the 20 designs with replacement.
- For the benchmark-minus-baseline difference, compute a paired question bootstrap over the same 20 designs.

**Bracket labels**

- `*` if the paired 95% CI excludes zero
- `**` if the paired 99% CI excludes zero
- `***` if the paired 99.9% CI excludes zero
- `n.s.` otherwise

**Important note**

This figure intentionally does **not** mix repeat-level run correlations with the correlation of the 5-repeat averaged predictor. Earlier exploratory versions did, and those were misleading.

## Figure 3

**Files**

- Plot:
  - `plots/paper/main_text/figure3_individual_paper_augmentation_density_correlation.png`
  - `plots/paper/main_text/figure3_individual_paper_augmentation_density_correlation.pdf`
- Saved rows:
  - `results/paper/main_text_figures/figure3_individual_paper_augmentation_cdf_rows.csv`
  - `results/paper/main_text_figures/figure3_individual_paper_augmentation_cdf_baselines.csv`

**Script**

- `analysis/literature_collection_analysis_reports/plot_paper_main_text_figures.py`

**Inputs**

- Single-paper repeat-5 performance table:
  - `results/validation/literature_analysis_report_sources_repeat5/validation_literature_analysis_report_source_significance.csv`
- Benchmark-paper repeat-5 rows:
  - `results/validation/literature_collection_analysis_reports_repeat5/validation_literature_collection_analysis_report_repeat5_rows.csv`
- Noise ceiling reference:
  - `results/validation/no_augmentation_model_comparison/validation_no_augmentation_model_comparison_benchmarks.csv`

**Construction**

- Restrict to the five-model set used for the later paper analyses.
- For each model, take the single-paper augmented raw correlation for every one of the 2011 papers.
- Compute:
  - the no-augmentation correlation
  - the mean augmented-paper correlation
  - the benchmark-paper correlation
- Plot a kernel density over the 2011 paper-level correlations for each model.

**Display elements**

- Filled density: distribution over paper-augmented performance.
- Solid vertical line: average augmented-paper correlation.
- Dashed vertical line: no augmentation.
- Dotted vertical line: benchmark paper augmented.
- Dash-dot vertical line: noise ceiling.
- Horizontal arrow: shift from no augmentation to average augmented-paper performance.

**Important note**

The paper has a CDF variant saved from earlier exploration, but the density version is the current active main-text figure.

## Figure 4

**Files**

- Plot:
  - `plots/paper/main_text/figure4_collection_augmentation_density_correlation.png`
  - `plots/paper/main_text/figure4_collection_augmentation_density_correlation.pdf`
- Saved rows:
  - `results/paper/main_text_figures/figure4_collection_augmentation_density_rows.csv`
  - `results/paper/main_text_figures/figure4_collection_augmentation_density_summary.csv`

**Script**

- `analysis/literature_collection_analysis_reports/plot_paper_main_text_figures.py`

**Inputs**

- Metadata-filter collection performance rows:
  - `results/validation/literature_collection_analysis_reports_metadata_filters/validation_literature_collection_analysis_report_metadata_filters_rows.csv`
- Benchmark-paper repeat-5 rows:
  - `results/validation/literature_collection_analysis_reports_repeat5/validation_literature_collection_analysis_report_repeat5_rows.csv`
- Noise ceiling reference:
  - `results/validation/no_augmentation_model_comparison/validation_no_augmentation_model_comparison_benchmarks.csv`

**Construction**

- Restrict to metadata-filter collections and the same five-model set as Figure 3.
- For each model, use the collection-level raw correlation values across the full metadata-filter sweep.
- Compute:
  - no-augmentation correlation
  - mean augmented-collection correlation
  - benchmark-paper correlation
- Plot model-wise density summaries with the same conventions used in Figure 3.

## Figure 5

**Files**

- Plot:
  - `plots/paper/main_text/figure5_cross_model_rank_robustness.png`
  - `plots/paper/main_text/figure5_cross_model_rank_robustness.pdf`
- Saved tables:
  - `results/paper/main_text_figures/figure5_cross_model_rank_robustness_pairwise.csv`
  - `results/paper/main_text_figures/figure5_cross_model_rank_robustness_summary.csv`
  - `results/paper/main_text_figures/figure5_cross_model_rank_robustness_reliability.csv`

**Script**

- `analysis/plot_figure5_rank_robustness.py`

**Upstream inputs**

- Pairwise rank-agreement table:
  - `results/paper/robustness/cross_model_repeat_rank_ceiling_pairwise.csv`
- Repeat-based reliability table:
  - `results/paper/robustness/cross_model_repeat_rank_ceiling_reliability.csv`

**Construction**

- Compute pairwise cross-model Spearman rank correlation in item usefulness separately for:
  - individual papers
  - collections
- Use a repeat-based within-model rank-reliability ceiling to normalize the observed Spearman correlation.

**Normalized rho**

- `normalized rho = observed Spearman rho / repeat-based ceiling`

The repeat-based ceiling comes from within-model repeat-to-repeat ranking agreement, projected to the 5-repeat aggregate.

**Important note**

This is a repeat-noise normalization, not a question-bootstrap adjustment.

## Figure 6

**Files**

- Plot:
  - `plots/paper/main_text/figure6_metadata_predictability_correlation.png`
  - `plots/paper/main_text/figure6_metadata_predictability_correlation.pdf`
- Saved rows:
  - `results/paper/main_text_figures/figure6_metadata_predictability_correlation_rows.csv`

**Script**

- `analysis/plot_figure6_metadata_predictability_correlation.py`

**Upstream inputs**

- Metadata supervised benchmark summary:
  - `results/validation/literature_metadata_supervised_benchmarks/literature_metadata_supervised_model_best.csv`
- Benchmark generation script:
  - `analysis/analyze_literature_metadata_supervised_benchmarks.py`

**Construction**

- Target: raw augmented `correlation`
- Datasets:
  - individual papers
  - metadata-filter collections
- Scope:
  - within-model for the five-model set
- Best model is selected from the supervised benchmark for each row.
- The figure shows:
  - grouped-CV `R^2`
  - grouped-CV Spearman
- Error bars use fold standard error across the five grouped CV folds.

**Grouping**

- Papers are grouped by `source_id`.
- Collections are grouped by `variant_id`.

This prevents the same item from appearing in both train and test folds.

**Important note**

This figure is about predicting augmented performance from metadata, not necessarily improvement over no augmentation, because it uses raw `correlation` instead of `delta_correlation`.

## Figure 7

**Files**

- Plot:
  - `plots/paper/main_text/figure7_individual_metadata_effect_robustness.png`
  - `plots/paper/main_text/figure7_individual_metadata_effect_robustness.pdf`
- Saved rows:
  - `results/paper/main_text_figures/figure7_individual_metadata_effect_robustness_rows.csv`

**Script**

- `analysis/plot_figure7_metadata_effect_robustness.py`

**Inputs**

- Repeat-5 single-paper performance:
  - `results/validation/literature_analysis_report_sources_repeat5/validation_literature_analysis_report_source_significance.csv`
- Paper metadata catalog:
  - `literature/output/evidence_cards/literature_evidence_cards_cleaned/collection_metadata_sets/collection_metadata_catalog.csv`

**Target**

- `delta_correlation`

**Model**

- Standardized ridge regression, fit separately within each model
- Median imputation for missing numeric values
- Standardization before ridge fitting
- `RidgeCV` over log-spaced alpha values

**Intervals**

- Bootstrap over items, `N_BOOT = 400`

**Features**

- `Journal Impact Factor` = `log1p(jif_value)`
- `Citation` = `log1p(citations)`
- `Publication Year` = numeric year
- `Empirical papers` = 1 for empirical, 0 for theory
- Discipline indicators are paper-level binary features:
  - Biology
  - Economics
  - Psychology
  - Math/Physics
  - Multidisciplinary

**Important note**

Figure 7 is a linearized summary of a weak predictive signal. It is best read as a directional association plot, not as a strong causal or structural model.

## Figure 8

**Files**

- Main-text plot:
  - `plots/paper/main_text/figure8_collection_feature_importance_gpt41.png`
  - `plots/paper/main_text/figure8_collection_feature_importance_gpt41.pdf`
- Main-text tables:
  - `results/paper/main_text_figures/figure8_collection_feature_importance_gpt41_permutation.csv`
  - `results/paper/main_text_figures/figure8_collection_feature_importance_gpt41_shap_points.csv`
  - `results/paper/main_text_figures/figure8_collection_feature_importance_gpt41_shap_summary.csv`
- SI plots:
  - `plots/paper/si/figure8_collection_feature_importance_gpt41mini.png`
  - `plots/paper/si/figure8_collection_feature_importance_gpt51.png`
  - `plots/paper/si/figure8_collection_feature_importance_gpt5mini.png`
  - `plots/paper/si/figure8_collection_feature_importance_gpt5nano.png`

**Script**

- `analysis/plot_figure8_collection_feature_importance_gpt41.py`

**Inputs**

- Collection-level relationship dataset:
  - `results/validation/literature_collection_analysis_reports_metadata_filters/validation_literature_collection_analysis_report_metadata_filters_relationship_dataset.csv`
- Paper metadata catalog:
  - `literature/output/evidence_cards/literature_evidence_cards_cleaned/collection_metadata_sets/collection_metadata_catalog.csv`
- Supervised benchmark table used to choose the best nonlinear model:
  - `results/validation/literature_metadata_supervised_benchmarks/literature_metadata_supervised_model_benchmark.csv`

**Target**

- `delta_correlation`

**Why GPT-4.1 in the main text**

The main-text panel currently uses `GPT-4.1`, where the best-performing collection predictor is `Extra Trees`, and where the predictive signal is especially clear. Other models are rendered to the supplement using the same plotting template.

**Collection features**

These are not metadata-filter labels or bins. They are actual within-collection composition summaries:

- `Journal Impact Factor` = mean `log1p(jif_value)` across member papers
- `Citation` = mean `log1p(citations)` across member papers
- `Publication Year` = mean publication year across member papers
- `Empirical Papers` = mean empirical share across member papers
- Discipline features = within-collection shares for:
  - Biology
  - Economics
  - Psychology
  - Math/Physics
  - Multidisciplinary
- `Number of Papers` = `log_count`

**Permutation importance**

- Grouped 5-fold CV with grouping by `variant_id`
- Metric: percent increase in prediction RMSE after permuting a feature in the held-out fold
- `N_PERM_REPEATS = 80` permutations per feature per fold

**SHAP panel**

- Fit the chosen tree model on the full collection dataset for that model
- Use `shap.TreeExplainer`
- Plot SHAP beeswarm points in the same feature order as the permutation-importance panel

**Important note**

Figure 8 is intentionally nonlinear because the collection supervised-learning benchmark showed that nonlinear models materially outperform ridge for this task.

## Adjusted-Correlation Sensitivity Version

A separate adjusted-correlation figure set exists in:

- `plots/paper/main_text_adjusted_correlation/`

Those were generated from:

- `analysis/literature_collection_analysis_reports/plot_paper_main_text_figures_adjusted.py`

This version is deliberately kept separate because the adjusted metric made the human-comparison panel behave pathologically, especially for layperson predictions in Figure 1.
