# figure4_predictive_model_benchmark

## Purpose
Expanded predictive-model benchmark for the `260427` paper-only metadata task used alongside Figure 4.

## Task
- Dataset: individual papers only
- Models scored: `Claude Sonnet 4.6`, `GPT-4.1`, `Gemini 2.5 Pro`
- Target: raw augmented performance, `Corr(y_true, y_pred)`
- Features: same paper-level metadata features used in Figure 4

## Construction
1. Build the same individual-paper metadata dataset used by the Figure 4 coefficient and permutation panels.
2. Evaluate each estimator separately within each LLM.
3. Use grouped 5-fold cross-validation by paper ID.
4. Record overall cross-validated `R^2`, Pearson `r`, and Spearman `rho`, plus fold means and standard deviations.

## Estimators
- `ols`: unregularized linear regression
- `ridge`: `RidgeCV(alphas=np.logspace(-3, 3, 13))`
- `elastic_net`: `ElasticNetCV` with `l1_ratio` grid `[0.05, 0.2, 0.5, 0.8, 0.95, 1.0]`
- `random_forest`
- `extra_trees`
- `gradient_boosting`
- `mlp`: one hidden-layer neural-network baseline with early stopping

## Output files
- Full benchmark table: `results/paper/main_text_figures_260427/figure4_predictive_model_benchmark.csv`
- Best-by-model summary: `results/paper/main_text_figures_260427/figure4_predictive_model_best.csv`
- Documentation: `results/paper/main_text_figures_260427/figure4_predictive_model_benchmark_documentation.md`
- Script: `analysis/paper_figures/benchmark_figure4_predictive_models_260427.py`

## Benchmark rows
| dataset           | model             | model_display     | predictive_model   |   n_rows |   n_groups |       cv_r2 |   cv_pearson_r |   cv_spearman_rho |   mean_fold_r2 |   sd_fold_r2 |   mean_fold_pearson_r |   sd_fold_pearson_r |   mean_fold_spearman_rho |   sd_fold_spearman_rho |
|:------------------|:------------------|:------------------|:-------------------|---------:|-----------:|------------:|---------------:|------------------:|---------------:|-------------:|----------------------:|--------------------:|-------------------------:|-----------------------:|
| individual_papers | Claude Sonnet 4.6 | Claude Sonnet 4.6 | ols                |     2011 |       2011 |  0.00653938 |     0.093592   |         0.0935341 |     0.00600531 |   0.00558033 |            0.0956337  |           0.0224427 |                0.0948005 |              0.0230673 |
| individual_papers | Claude Sonnet 4.6 | Claude Sonnet 4.6 | ridge              |     2011 |       2011 |  0.0069888  |     0.0890332  |         0.0915059 |     0.00642078 |   0.00485998 |            0.0911654  |           0.0232848 |                0.0930005 |              0.0227118 |
| individual_papers | Claude Sonnet 4.6 | Claude Sonnet 4.6 | elastic_net        |     2011 |       2011 |  0.0070611  |     0.0886521  |         0.0920113 |     0.0064476  |   0.00468605 |            0.0922776  |           0.0226648 |                0.0935779 |              0.0213944 |
| individual_papers | Claude Sonnet 4.6 | Claude Sonnet 4.6 | random_forest      |     2011 |       2011 | -0.0551249  |     0.0364024  |         0.0328434 |    -0.0563212  |   0.0336974  |            0.0404858  |           0.0431871 |                0.0348994 |              0.0518714 |
| individual_papers | Claude Sonnet 4.6 | Claude Sonnet 4.6 | extra_trees        |     2011 |       2011 | -0.0759868  |     0.041323   |         0.0538459 |    -0.078143   |   0.0253597  |            0.0419157  |           0.0268129 |                0.0563145 |              0.0207721 |
| individual_papers | Claude Sonnet 4.6 | Claude Sonnet 4.6 | gradient_boosting  |     2011 |       2011 | -0.0509506  |     0.0480556  |         0.0390229 |    -0.0514944  |   0.0472215  |            0.0546701  |           0.0653067 |                0.0396262 |              0.059808  |
| individual_papers | Claude Sonnet 4.6 | Claude Sonnet 4.6 | mlp                |     2011 |       2011 | -0.347352   |     0.00103949 |         0.0212566 |    -0.355199   |   0.169064   |            0.00119025 |           0.0221682 |                0.0260282 |              0.016308  |
| individual_papers | GPT-4.1           | GPT-4.1           | ols                |     2010 |       2010 |  0.00588284 |     0.0970503  |         0.14189   |     0.00288722 |   0.0172015  |            0.112151   |           0.0395144 |                0.147753  |              0.0377481 |
| individual_papers | GPT-4.1           | GPT-4.1           | ridge              |     2010 |       2010 |  0.00865901 |     0.095176   |         0.138845  |     0.00572795 |   0.014314   |            0.114789   |           0.0394075 |                0.152384  |              0.0459889 |
| individual_papers | GPT-4.1           | GPT-4.1           | elastic_net        |     2010 |       2010 |  0.0109189  |     0.10552    |         0.142599  |     0.00773147 |   0.0118608  |            0.125459   |           0.0376228 |                0.151403  |              0.0330248 |
| individual_papers | GPT-4.1           | GPT-4.1           | random_forest      |     2010 |       2010 | -0.0427235  |     0.0839478  |         0.123833  |    -0.050655   |   0.0214502  |            0.0888841  |           0.0189351 |                0.125562  |              0.0271572 |
| individual_papers | GPT-4.1           | GPT-4.1           | extra_trees        |     2010 |       2010 | -0.0648696  |     0.0838378  |         0.125647  |    -0.0732463  |   0.0338958  |            0.0890694  |           0.0152348 |                0.127063  |              0.0335021 |
| individual_papers | GPT-4.1           | GPT-4.1           | gradient_boosting  |     2010 |       2010 | -0.145687   |     0.0397656  |         0.0961594 |    -0.163214   |   0.152036   |            0.0504839  |           0.0581505 |                0.103002  |              0.074021  |
| individual_papers | GPT-4.1           | GPT-4.1           | mlp                |     2010 |       2010 | -0.245284   |     0.0245134  |         0.0768268 |    -0.25174    |   0.081233   |            0.0332044  |           0.047545  |                0.076537  |              0.027526  |
| individual_papers | Gemini 2.5 Pro    | Gemini 2.5 Pro    | ols                |     2011 |       2011 |  0.0295678  |     0.173839   |         0.151561  |     0.030658   |   0.0346449  |            0.182561   |           0.0798543 |                0.158381  |              0.0754884 |
| individual_papers | Gemini 2.5 Pro    | Gemini 2.5 Pro    | ridge              |     2011 |       2011 |  0.0301882  |     0.173773   |         0.1501    |     0.0311228  |   0.0294439  |            0.182986   |           0.0809102 |                0.157823  |              0.0783015 |
| individual_papers | Gemini 2.5 Pro    | Gemini 2.5 Pro    | elastic_net        |     2011 |       2011 |  0.0308093  |     0.175536   |         0.150568  |     0.031795   |   0.0310513  |            0.185331   |           0.0822656 |                0.160354  |              0.0751906 |
| individual_papers | Gemini 2.5 Pro    | Gemini 2.5 Pro    | random_forest      |     2011 |       2011 | -0.0143665  |     0.147996   |         0.121458  |    -0.0140941  |   0.033621   |            0.149876   |           0.0500319 |                0.123588  |              0.0478514 |
| individual_papers | Gemini 2.5 Pro    | Gemini 2.5 Pro    | extra_trees        |     2011 |       2011 | -0.0420106  |     0.12367    |         0.118734  |    -0.0422038  |   0.0244771  |            0.125075   |           0.0283045 |                0.119864  |              0.0203777 |
| individual_papers | Gemini 2.5 Pro    | Gemini 2.5 Pro    | gradient_boosting  |     2011 |       2011 | -0.0164562  |     0.127817   |         0.112489  |    -0.0160596  |   0.0328082  |            0.1279     |           0.057679  |                0.115723  |              0.0519376 |
| individual_papers | Gemini 2.5 Pro    | Gemini 2.5 Pro    | mlp                |     2011 |       2011 | -0.0754476  |     0.100481   |         0.0938551 |    -0.0742507  |   0.0252778  |            0.103353   |           0.0303174 |                0.0956387 |              0.0449728 |

## Best estimator by model
| dataset           | model             | model_display     | predictive_model   |   n_rows |   n_groups |     cv_r2 |   cv_pearson_r |   cv_spearman_rho |   mean_fold_r2 |   sd_fold_r2 |   mean_fold_pearson_r |   sd_fold_pearson_r |   mean_fold_spearman_rho |   sd_fold_spearman_rho |
|:------------------|:------------------|:------------------|:-------------------|---------:|-----------:|----------:|---------------:|------------------:|---------------:|-------------:|----------------------:|--------------------:|-------------------------:|-----------------------:|
| individual_papers | Claude Sonnet 4.6 | Claude Sonnet 4.6 | elastic_net        |     2011 |       2011 | 0.0070611 |      0.0886521 |         0.0920113 |     0.0064476  |   0.00468605 |             0.0922776 |           0.0226648 |                0.0935779 |              0.0213944 |
| individual_papers | GPT-4.1           | GPT-4.1           | elastic_net        |     2010 |       2010 | 0.0109189 |      0.10552   |         0.142599  |     0.00773147 |   0.0118608  |             0.125459  |           0.0376228 |                0.151403  |              0.0330248 |
| individual_papers | Gemini 2.5 Pro    | Gemini 2.5 Pro    | elastic_net        |     2011 |       2011 | 0.0308093 |      0.175536  |         0.150568  |     0.031795   |   0.0310513  |             0.185331  |           0.0822656 |                0.160354  |              0.0751906 |
