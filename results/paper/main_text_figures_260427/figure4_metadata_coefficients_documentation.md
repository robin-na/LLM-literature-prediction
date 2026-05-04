# figure4_metadata_coefficients

## Purpose
Figure 4 for `main_text_260427`. This is a paper-only metadata figure that pairs elastic-net coefficients with elastic-net predictive feature importance for augmented performance.

## Inheritance
- Semantic figure ID: `metadata_coefficients`
- Adapted from `main_text_260415` Figure 3 into the `main_text_260427` Figure 4 slot
- Parent coefficient figure: `plots/paper/main_text_260415/figure3_metadata_coefficients.png`
- Parent permutation companion: `plots/paper/main_text_260415/figure3_individual_permutation_importance_ridge.png`

## Output files
- Plot PNG: `plots/paper/main_text_260427/figure4_metadata_coefficients.png`
- Canonical combined rows: `results/paper/main_text_figures_260427/figure4_metadata_coefficients_rows.csv`
- Elastic-net coefficient rows: `results/paper/main_text_figures_260427/figure4_metadata_coefficients_elastic_net_rows.csv`
- Elastic-net permutation rows: `results/paper/main_text_figures_260427/figure4_metadata_coefficients_elastic_net_permutation_rows.csv`
- Documentation: `results/paper/main_text_figures_260427/figure4_metadata_coefficients_documentation.md`
- Script: `analysis/paper_figures/plot_figure4_metadata_coefficients_260427.py`

## Input files
- Individual-paper correlations: `results/paper/main_text_figures_260409/paper_repeat_correlation_metrics.csv`
- Individual-paper metadata catalog: `literature/output/evidence_cards/literature_evidence_cards_cleaned/collection_metadata_sets/collection_metadata_catalog.csv`

## Construction
1. Restrict to the three displayed models: `Claude Sonnet 4.6`, `GPT-4.1`, and `Gemini 2.5 Pro`.
2. Build the individual-paper dataset by merging raw augmented correlation performance with paper metadata features.
3. Left panel:
   - fit a separate multivariable elastic-net model for each LLM
   - target = raw augmented performance, `Corr(y_true, y_pred)`
   - predictors = empirical-paper indicator, log citation count, log journal impact factor, publication year, and journal-discipline indicators
   - median-impute and standardize predictors before fitting
   - estimator = elastic net with `ElasticNetCV`
   - plot standardized coefficients with percentile bootstrap 95% intervals across paper rows
4. Right panel:
   - use the same individual-paper features and target
   - estimator = elastic net with `ElasticNetCV`
   - grouped 5-fold cross-validation by paper ID
   - within each held-out fold, permute one feature at a time `100` times
   - importance = percent increase in held-out prediction error (RMSE) relative to the unpermuted held-out prediction
   - plot mean importance with standard error across folds

## Interpretation
- Left panel: a positive coefficient means higher augmented correlation under the penalized elastic-net fit; coefficients may shrink to exactly zero.
- Right panel: a larger positive value means held-out prediction error rises more when that feature is broken, so the predictive model relies more on it.
- Both panels use the same elastic-net model family, so the coefficient and importance views are aligned to the same predictive estimator.

## Notes
- This `260427` figure intentionally drops the collection panel from the `260415` parent.
- The coefficient and permutation panels answer different questions and should not be numerically compared on the same x-scale.
- Individual-paper sample sizes are `2,010, 2,011` depending on model availability.
- The coefficient intervals are bootstrap intervals, not HC3 regression confidence intervals.

## Elastic-net coefficient rows
| model             | model_display     | feature_key             | feature_label         | feature_group         |         coef |       ci_low |      ci_high |    n | panel_key                | panel_display            |
|:------------------|:------------------|:------------------------|:----------------------|:----------------------|-------------:|-------------:|-------------:|-----:|:-------------------------|:-------------------------|
| Claude Sonnet 4.6 | Claude Sonnet 4.6 | journal_impact          | Journal Impact Factor | Prestige / visibility |  0.000789651 | -0.000240823 |  0.00237192  | 2011 | elastic_net_coefficients | Elastic net coefficients |
| Claude Sonnet 4.6 | Claude Sonnet 4.6 | citation                | Citation              | Prestige / visibility | -0.00299985  | -0.00478004  | -0.00138575  | 2011 | elastic_net_coefficients | Elastic net coefficients |
| Claude Sonnet 4.6 | Claude Sonnet 4.6 | empirical_share         | Empirical             | Study type            | -0.00209353  | -0.00363175  | -0.000755203 | 2011 | elastic_net_coefficients | Elastic net coefficients |
| Claude Sonnet 4.6 | Claude Sonnet 4.6 | recent                  | Publication Year      | Publication timing    | -0.00234991  | -0.00376012  | -0.00103449  | 2011 | elastic_net_coefficients | Elastic net coefficients |
| Claude Sonnet 4.6 | Claude Sonnet 4.6 | biology_share           | Biology               | Journal discipline    |  0.000865072 |  0           |  0.00222191  | 2011 | elastic_net_coefficients | Elastic net coefficients |
| Claude Sonnet 4.6 | Claude Sonnet 4.6 | economics_share         | Economics             | Journal discipline    |  8.26252e-05 | -0.000801678 |  0.00206546  | 2011 | elastic_net_coefficients | Elastic net coefficients |
| Claude Sonnet 4.6 | Claude Sonnet 4.6 | psychology_share        | Psychology            | Journal discipline    |  0.000368865 | -0.000437136 |  0.00191783  | 2011 | elastic_net_coefficients | Elastic net coefficients |
| Claude Sonnet 4.6 | Claude Sonnet 4.6 | mathphysics_share       | Math/Physics          | Journal discipline    | -0.00110012  | -0.00233896  |  2.76671e-07 | 2011 | elastic_net_coefficients | Elastic net coefficients |
| Claude Sonnet 4.6 | Claude Sonnet 4.6 | multidisciplinary_share | Multidisciplinary     | Journal discipline    |  4.34667e-05 | -0.00102877  |  0.00152724  | 2011 | elastic_net_coefficients | Elastic net coefficients |
| GPT-4.1           | GPT-4.1           | journal_impact          | Journal Impact Factor | Prestige / visibility |  0           | -0.00112313  |  0.00281695  | 2010 | elastic_net_coefficients | Elastic net coefficients |
| GPT-4.1           | GPT-4.1           | citation                | Citation              | Prestige / visibility |  0           | -0.00178256  |  0.00192362  | 2010 | elastic_net_coefficients | Elastic net coefficients |
| GPT-4.1           | GPT-4.1           | empirical_share         | Empirical             | Study type            | -0.00318963  | -0.00601173  | -0.00154782  | 2010 | elastic_net_coefficients | Elastic net coefficients |
| GPT-4.1           | GPT-4.1           | recent                  | Publication Year      | Publication timing    |  0           | -0.00179539  |  0.00262936  | 2010 | elastic_net_coefficients | Elastic net coefficients |
| GPT-4.1           | GPT-4.1           | biology_share           | Biology               | Journal discipline    |  0           | -0.00234275  |  0.00114245  | 2010 | elastic_net_coefficients | Elastic net coefficients |
| GPT-4.1           | GPT-4.1           | economics_share         | Economics             | Journal discipline    | -0.00118759  | -0.00511188  |  0           | 2010 | elastic_net_coefficients | Elastic net coefficients |
| GPT-4.1           | GPT-4.1           | psychology_share        | Psychology            | Journal discipline    | -0           | -0.00304316  |  0           | 2010 | elastic_net_coefficients | Elastic net coefficients |
| GPT-4.1           | GPT-4.1           | mathphysics_share       | Math/Physics          | Journal discipline    |  0           | -0.00215992  |  0.00205597  | 2010 | elastic_net_coefficients | Elastic net coefficients |
| GPT-4.1           | GPT-4.1           | multidisciplinary_share | Multidisciplinary     | Journal discipline    | -0           | -0.00379359  |  0           | 2010 | elastic_net_coefficients | Elastic net coefficients |
| Gemini 2.5 Pro    | Gemini 2.5 Pro    | journal_impact          | Journal Impact Factor | Prestige / visibility |  0           | -0.00411022  |  0.00469544  | 2011 | elastic_net_coefficients | Elastic net coefficients |
| Gemini 2.5 Pro    | Gemini 2.5 Pro    | citation                | Citation              | Prestige / visibility | -0.0056529   | -0.0115901   |  0           | 2011 | elastic_net_coefficients | Elastic net coefficients |
| Gemini 2.5 Pro    | Gemini 2.5 Pro    | empirical_share         | Empirical             | Study type            | -0.0126756   | -0.0173175   | -0.00821698  | 2011 | elastic_net_coefficients | Elastic net coefficients |
| Gemini 2.5 Pro    | Gemini 2.5 Pro    | recent                  | Publication Year      | Publication timing    |  0           | -0.00382178  |  0.00383534  | 2011 | elastic_net_coefficients | Elastic net coefficients |
| Gemini 2.5 Pro    | Gemini 2.5 Pro    | biology_share           | Biology               | Journal discipline    |  0.00428736  |  0           |  0.00876476  | 2011 | elastic_net_coefficients | Elastic net coefficients |
| Gemini 2.5 Pro    | Gemini 2.5 Pro    | economics_share         | Economics             | Journal discipline    | -0.00327742  | -0.00821902  |  8.87832e-07 | 2011 | elastic_net_coefficients | Elastic net coefficients |
| Gemini 2.5 Pro    | Gemini 2.5 Pro    | psychology_share        | Psychology            | Journal discipline    |  0           | -0.00207891  |  0.00493084  | 2011 | elastic_net_coefficients | Elastic net coefficients |
| Gemini 2.5 Pro    | Gemini 2.5 Pro    | mathphysics_share       | Math/Physics          | Journal discipline    | -0           | -0.00397188  |  0.00350022  | 2011 | elastic_net_coefficients | Elastic net coefficients |
| Gemini 2.5 Pro    | Gemini 2.5 Pro    | multidisciplinary_share | Multidisciplinary     | Journal discipline    |  0.00150425  |  0           |  0.00622759  | 2011 | elastic_net_coefficients | Elastic net coefficients |

## Elastic-net permutation-importance rows
| estimator   | estimator_label   | model             | model_display     | feature_key             | feature_label         | feature_group         |   mean_importance |   sd_importance |   n_folds |   n_total |   se_importance | panel_key                          | panel_display                      |
|:------------|:------------------|:------------------|:------------------|:------------------------|:----------------------|:----------------------|------------------:|----------------:|----------:|----------:|----------------:|:-----------------------------------|:-----------------------------------|
| elastic_net | Elastic net       | Claude Sonnet 4.6 | Claude Sonnet 4.6 | biology_share           | Biology               | Journal discipline    |        0.0613383  |      0.164242   |         5 |      2011 |      0.0734513  | elastic_net_permutation_importance | Elastic net permutation importance |
| elastic_net | Elastic net       | Claude Sonnet 4.6 | Claude Sonnet 4.6 | citation                | Citation              | Prestige / visibility |        1.25168    |      0.806383   |         5 |      2011 |      0.360626   | elastic_net_permutation_importance | Elastic net permutation importance |
| elastic_net | Elastic net       | Claude Sonnet 4.6 | Claude Sonnet 4.6 | economics_share         | Economics             | Journal discipline    |       -0.0110423  |      0.0595746  |         5 |      2011 |      0.0266426  | elastic_net_permutation_importance | Elastic net permutation importance |
| elastic_net | Elastic net       | Claude Sonnet 4.6 | Claude Sonnet 4.6 | empirical_share         | Empirical             | Study type            |        0.682917   |      0.155156   |         5 |      2011 |      0.0693877  | elastic_net_permutation_importance | Elastic net permutation importance |
| elastic_net | Elastic net       | Claude Sonnet 4.6 | Claude Sonnet 4.6 | journal_impact          | Journal Impact Factor | Prestige / visibility |        0.0255288  |      0.168618   |         5 |      2011 |      0.0754082  | elastic_net_permutation_importance | Elastic net permutation importance |
| elastic_net | Elastic net       | Claude Sonnet 4.6 | Claude Sonnet 4.6 | mathphysics_share       | Math/Physics          | Journal discipline    |        0.099446   |      0.0720304  |         5 |      2011 |      0.032213   | elastic_net_permutation_importance | Elastic net permutation importance |
| elastic_net | Elastic net       | Claude Sonnet 4.6 | Claude Sonnet 4.6 | multidisciplinary_share | Multidisciplinary     | Journal discipline    |       -0.045732   |      0.038479   |         5 |      2011 |      0.0172083  | elastic_net_permutation_importance | Elastic net permutation importance |
| elastic_net | Elastic net       | Claude Sonnet 4.6 | Claude Sonnet 4.6 | psychology_share        | Psychology            | Journal discipline    |       -0.0344649  |      0.130687   |         5 |      2011 |      0.0584451  | elastic_net_permutation_importance | Elastic net permutation importance |
| elastic_net | Elastic net       | Claude Sonnet 4.6 | Claude Sonnet 4.6 | recent                  | Publication Year      | Publication timing    |        0.737248   |      0.251383   |         5 |      2011 |      0.112422   | elastic_net_permutation_importance | Elastic net permutation importance |
| elastic_net | Elastic net       | GPT-4.1           | GPT-4.1           | biology_share           | Biology               | Journal discipline    |        0          |      0          |         5 |      2010 |      0          | elastic_net_permutation_importance | Elastic net permutation importance |
| elastic_net | Elastic net       | GPT-4.1           | GPT-4.1           | citation                | Citation              | Prestige / visibility |       -0.0133861  |      0.0299323  |         5 |      2010 |      0.0133861  | elastic_net_permutation_importance | Elastic net permutation importance |
| elastic_net | Elastic net       | GPT-4.1           | GPT-4.1           | economics_share         | Economics             | Journal discipline    |        0.197593   |      0.0968715  |         5 |      2010 |      0.0433222  | elastic_net_permutation_importance | Elastic net permutation importance |
| elastic_net | Elastic net       | GPT-4.1           | GPT-4.1           | empirical_share         | Empirical             | Study type            |        0.779484   |      0.245737   |         5 |      2010 |      0.109897   | elastic_net_permutation_importance | Elastic net permutation importance |
| elastic_net | Elastic net       | GPT-4.1           | GPT-4.1           | journal_impact          | Journal Impact Factor | Prestige / visibility |       -0.0012051  |      0.00269468 |         5 |      2010 |      0.0012051  | elastic_net_permutation_importance | Elastic net permutation importance |
| elastic_net | Elastic net       | GPT-4.1           | GPT-4.1           | mathphysics_share       | Math/Physics          | Journal discipline    |       -0.00612241 |      0.0136901  |         5 |      2010 |      0.00612241 | elastic_net_permutation_importance | Elastic net permutation importance |
| elastic_net | Elastic net       | GPT-4.1           | GPT-4.1           | multidisciplinary_share | Multidisciplinary     | Journal discipline    |        0          |      0          |         5 |      2010 |      0          | elastic_net_permutation_importance | Elastic net permutation importance |
| elastic_net | Elastic net       | GPT-4.1           | GPT-4.1           | psychology_share        | Psychology            | Journal discipline    |       -0.0271277  |      0.0606593  |         5 |      2010 |      0.0271277  | elastic_net_permutation_importance | Elastic net permutation importance |
| elastic_net | Elastic net       | GPT-4.1           | GPT-4.1           | recent                  | Publication Year      | Publication timing    |        0          |      0          |         5 |      2010 |      0          | elastic_net_permutation_importance | Elastic net permutation importance |
| elastic_net | Elastic net       | Gemini 2.5 Pro    | Gemini 2.5 Pro    | biology_share           | Biology               | Journal discipline    |        0.255562   |      0.201655   |         5 |      2011 |      0.090183   | elastic_net_permutation_importance | Elastic net permutation importance |
| elastic_net | Elastic net       | Gemini 2.5 Pro    | Gemini 2.5 Pro    | citation                | Citation              | Prestige / visibility |        0.455068   |      0.314928   |         5 |      2011 |      0.14084    | elastic_net_permutation_importance | Elastic net permutation importance |
| elastic_net | Elastic net       | Gemini 2.5 Pro    | Gemini 2.5 Pro    | economics_share         | Economics             | Journal discipline    |        0.130684   |      0.167063   |         5 |      2011 |      0.074713   | elastic_net_permutation_importance | Elastic net permutation importance |
| elastic_net | Elastic net       | Gemini 2.5 Pro    | Gemini 2.5 Pro    | empirical_share         | Empirical             | Study type            |        2.06876    |      1.25621    |         5 |      2011 |      0.561793   | elastic_net_permutation_importance | Elastic net permutation importance |
| elastic_net | Elastic net       | Gemini 2.5 Pro    | Gemini 2.5 Pro    | journal_impact          | Journal Impact Factor | Prestige / visibility |       -0.0123947  |      0.0277154  |         5 |      2011 |      0.0123947  | elastic_net_permutation_importance | Elastic net permutation importance |
| elastic_net | Elastic net       | Gemini 2.5 Pro    | Gemini 2.5 Pro    | mathphysics_share       | Math/Physics          | Journal discipline    |       -0.0508238  |      0.113646   |         5 |      2011 |      0.0508238  | elastic_net_permutation_importance | Elastic net permutation importance |
| elastic_net | Elastic net       | Gemini 2.5 Pro    | Gemini 2.5 Pro    | multidisciplinary_share | Multidisciplinary     | Journal discipline    |        0.0312354  |      0.0425334  |         5 |      2011 |      0.0190215  | elastic_net_permutation_importance | Elastic net permutation importance |
| elastic_net | Elastic net       | Gemini 2.5 Pro    | Gemini 2.5 Pro    | psychology_share        | Psychology            | Journal discipline    |       -0.0233918  |      0.0523056  |         5 |      2011 |      0.0233918  | elastic_net_permutation_importance | Elastic net permutation importance |
| elastic_net | Elastic net       | Gemini 2.5 Pro    | Gemini 2.5 Pro    | recent                  | Publication Year      | Publication timing    |        0          |      0          |         5 |      2011 |      0          | elastic_net_permutation_importance | Elastic net permutation importance |
