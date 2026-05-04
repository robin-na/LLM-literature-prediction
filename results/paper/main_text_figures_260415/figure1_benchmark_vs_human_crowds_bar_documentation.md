# figure1_benchmark_vs_human_crowds_bar

## Purpose
Figure 1 for `main_text_260415`. This plot compares human wisdom-of-the-crowd bars with LLM baseline and benchmark-paper-augmented bars on the same scale: Pearson correlation with the true treatment outcome across the 20 validation questions.

## Output files
- Plot PNG: `plots/paper/main_text_260415/figure1_benchmark_vs_human_crowds_bar.png`
- Plot rows: `results/paper/main_text_figures_260415/figure1_benchmark_vs_human_crowds_bar_rows.csv`
- Reference lines: `results/paper/main_text_figures_260415/figure1_benchmark_vs_human_crowds_bar_reference_lines.csv`
- Pair significance: `results/paper/main_text_figures_260415/figure1_benchmark_vs_human_crowds_bar_pair_significance.csv`
- Script: `analysis/paper_figures/plot_figure1_main_text_260415.py`

## Input files
- LLM 30-run mean predictions: `results/validation/literature_incremental_pgg_science_repeat30/incremental_pgg_science_avg_predictions.csv`
- LLM repeat-level predictions: `results/validation/literature_incremental_pgg_science_repeat30/incremental_pgg_science_repeat_rows.csv`
- Human forecasts: `science-data_and_code/data/processed_data/prediction_survey.csv`
- Validation outcomes: `input/pgg_CONFIGmerged_validation.csv`
- Noise ceiling benchmark table: `results/validation/no_augmentation_model_comparison/validation_no_augmentation_model_comparison_benchmarks.csv`

## Construction
1. Load the 20 validation outcomes from `efficiency_p` in `pgg_CONFIGmerged_validation.csv` and sort by `CONFIG_configId`.
2. Build the two human wisdom-of-the-crowd bars from `prediction_survey.csv`:
   - keep rows with `prediction` between `-0.2` and `1.2`
   - keep respondents with `n_predictions_made == 20`
   - split by source: `prolific` = laypeople, `sspp` = experts
   - pivot to `CONFIG_configId x playerID`
   - keep only complete participants with non-missing predictions for all 20 questions
   - average predictions across participants within source for each question
   - compute Pearson correlation between that mean prediction vector and the true outcome vector
3. Build the LLM bars from `incremental_pgg_science_avg_predictions.csv`:
   - use only `condition in ["baseline", "science_gpt41"]`
   - keep only the 8 displayed models: Claude Sonnet 4.6, GPT-5.1, GPT-4.1 Mini, GPT-4.1, GPT-5 Nano, GPT-5 Mini, GPT-4.1 Nano, Gemini 2.5 Pro
   - each row already contains the mean prediction vector across 30 runs for one model-condition pair
   - compute Pearson correlation between the 30-run mean prediction vector (`Q1`-`Q20`) and the true outcome vector
4. Add two horizontal reference lines:
   - `No-treatment outcome baseline` = Pearson correlation between `efficiency_np` and `efficiency_p` from `pgg_CONFIGmerged_validation.csv`
   - `Noise ceiling` = the `Noise ceiling` correlation from `validation_no_augmentation_model_comparison_benchmarks.csv`
5. Plot order:
   - first two bars: `Laypeople wisdom-of-the-crowd`, `Experts wisdom-of-the-crowd`
   - then the 8 LLMs in the fixed presentation order used in the figure
   - within each model, show `baseline` and `science_gpt41`
6. Error bars:
   - human wisdom-of-the-crowd bars: bootstrap the 20 experiments with replacement, then recompute the crowd-level correlation
   - LLM bars: bootstrap the 20 experiments with replacement, then recompute the model-level correlation
   - interval shown: percentile bootstrap 95% CI (`2.5%`, `97.5%`)
7. Pair significance:
   - only for LLM baseline vs benchmark-paper pairs
   - compute paired bootstrap resamples over the same 20 experiments for both bars
   - significance stars reflect whether the paired bootstrap CI for `corr_augmented - corr_baseline` excludes `0`
   - `*` = 95% CI excludes 0, `**` = 99% CI excludes 0, `***` = 99.9% CI excludes 0

## Notes
- LLM estimand: `corr(mean across 30 runs, truth)`. This is **not** the mean of per-run correlations.
- Human wisdom-of-the-crowd estimand: `corr(mean across complete human forecasters, truth)`.
- Error bars are percentile bootstrap 95% CIs on the plotted estimand itself.

## Values used in the plot
### Bars
| group       | label                         | condition                     |    value |    ci_low |   ci_high |
|:------------|:------------------------------|:------------------------------|---------:|----------:|----------:|
| human_crowd | Laypeople wisdom-of-the-crowd | Laypeople wisdom-of-the-crowd | 0.603834 |  0.234114 |  0.825193 |
| human_crowd | Experts wisdom-of-the-crowd   | Experts wisdom-of-the-crowd   | 0.605577 |  0.232564 |  0.841887 |
| llm         | Claude Sonnet 4.6             | baseline                      | 0.664486 |  0.289051 |  0.873042 |
| llm         | Claude Sonnet 4.6             | science_gpt41                 | 0.799038 |  0.59405  |  0.918023 |
| llm         | GPT-5.1                       | baseline                      | 0.652617 |  0.238087 |  0.888363 |
| llm         | GPT-5.1                       | science_gpt41                 | 0.756194 |  0.48565  |  0.909145 |
| llm         | GPT-4.1 Mini                  | baseline                      | 0.615444 |  0.174308 |  0.861211 |
| llm         | GPT-4.1 Mini                  | science_gpt41                 | 0.717928 |  0.408338 |  0.889655 |
| llm         | GPT-4.1                       | baseline                      | 0.614593 |  0.213479 |  0.868899 |
| llm         | GPT-4.1                       | science_gpt41                 | 0.758389 |  0.495601 |  0.908449 |
| llm         | GPT-5 Nano                    | baseline                      | 0.598458 |  0.196823 |  0.84545  |
| llm         | GPT-5 Nano                    | science_gpt41                 | 0.715294 |  0.393534 |  0.891181 |
| llm         | GPT-5 Mini                    | baseline                      | 0.561647 |  0.059918 |  0.860111 |
| llm         | GPT-5 Mini                    | science_gpt41                 | 0.790183 |  0.537423 |  0.930009 |
| llm         | GPT-4.1 Nano                  | baseline                      | 0.521217 |  0.098642 |  0.795827 |
| llm         | GPT-4.1 Nano                  | science_gpt41                 | 0.620234 |  0.173659 |  0.863054 |
| llm         | Gemini 2.5 Pro                | baseline                      | 0.399382 | -0.111996 |  0.746995 |
| llm         | Gemini 2.5 Pro                | science_gpt41                 | 0.842593 |  0.679292 |  0.939523 |

### Reference lines
| label                         |    value |
|:------------------------------|---------:|
| No-treatment outcome baseline | 0.541475 |
| Noise ceiling                 | 0.776535 |

### Pair Significance
| model             |   baseline_corr |   benchmark_corr |   delta_corr |   delta_ci95_low |   delta_ci95_high |   delta_ci99_low |   delta_ci99_high |   delta_ci999_low |   delta_ci999_high |   p_bootstrap_two_sided | sig_label   |   n_boot |
|:------------------|----------------:|-----------------:|-------------:|-----------------:|------------------:|-----------------:|------------------:|------------------:|-------------------:|------------------------:|:------------|---------:|
| Claude Sonnet 4.6 |        0.664486 |         0.799038 |     0.134552 |         0.001735 |          0.356037 |        -0.03267  |          0.465    |         -0.092254 |           0.6124   |                 0.0458  | *           |    50000 |
| GPT-5.1           |        0.652617 |         0.756194 |     0.103577 |        -0.031187 |          0.288974 |        -0.072555 |          0.374354 |         -0.140583 |           0.528814 |                 0.14908 | n.s.        |    50000 |
| GPT-4.1 Mini      |        0.615444 |         0.717928 |     0.102485 |         0.009741 |          0.255165 |        -0.008063 |          0.315043 |         -0.036563 |           0.384054 |                 0.02104 | *           |    50000 |
| GPT-4.1           |        0.614593 |         0.758389 |     0.143796 |         0.00944  |          0.328957 |        -0.01844  |          0.406175 |         -0.049353 |           0.505641 |                 0.03112 | *           |    50000 |
| GPT-5 Nano        |        0.598458 |         0.715294 |     0.116837 |         0.01917  |          0.256052 |        -0.003793 |          0.308175 |         -0.029644 |           0.380135 |                 0.01332 | *           |    50000 |
| GPT-5 Mini        |        0.561647 |         0.790183 |     0.228536 |         0.036516 |          0.51202  |         0.003229 |          0.624724 |         -0.050015 |           0.747781 |                 0.00868 | **          |    50000 |
| GPT-4.1 Nano      |        0.521217 |         0.620234 |     0.099017 |        -0.038868 |          0.214439 |        -0.113151 |          0.259995 |         -0.207303 |           0.333867 |                 0.14156 | n.s.        |    50000 |
| Gemini 2.5 Pro    |        0.399382 |         0.842593 |     0.443211 |         0.161265 |          0.831754 |         0.100562 |          0.998675 |          0.050208 |           1.2047   |                 0.00024 | ***         |    50000 |
