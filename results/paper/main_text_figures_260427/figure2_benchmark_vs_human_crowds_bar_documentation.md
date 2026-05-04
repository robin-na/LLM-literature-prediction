# figure2_benchmark_vs_human_crowds_bar

## Purpose
Figure 2 for `main_text_260427`. This plot compares human wisdom-of-the-crowd performance with three LLM baselines and their benchmark-paper-augmented counterparts on the same Pearson-correlation scale across the 20 validation questions.

## Inheritance
- Semantic figure ID: `benchmark_vs_human_crowds_bar`
- Adapted from `main_text_260415` Figure 1 into the `main_text_260427` Figure 2 slot
- Parent assets:
  - Plot PNG: `plots/paper/main_text_260415/figure1_benchmark_vs_human_crowds_bar.png`
  - Rows CSV: `results/paper/main_text_figures_260415/figure1_benchmark_vs_human_crowds_bar_rows.csv`
  - Documentation: `results/paper/main_text_figures_260415/figure1_benchmark_vs_human_crowds_bar_documentation.md`

## Output files
- Plot PNG: `plots/paper/main_text_260427/figure2_benchmark_vs_human_crowds_bar.png`
- Plot rows: `results/paper/main_text_figures_260427/figure2_benchmark_vs_human_crowds_bar_rows.csv`
- Reference lines: `results/paper/main_text_figures_260427/figure2_benchmark_vs_human_crowds_bar_reference_lines.csv`
- Pair significance: `results/paper/main_text_figures_260427/figure2_benchmark_vs_human_crowds_bar_pair_significance.csv`
- Documentation: `results/paper/main_text_figures_260427/figure2_benchmark_vs_human_crowds_bar_documentation.md`
- Script: `analysis/paper_figures/plot_figure2_main_text_260427.py`

## Input files
- LLM 30-run mean predictions: `results/validation/literature_incremental_pgg_science_repeat30/incremental_pgg_science_avg_predictions.csv`
- Human forecasts: `science-data_and_code/data/processed_data/prediction_survey.csv`
- Validation outcomes: `input/pgg_CONFIGmerged_validation.csv`
- Noise ceiling benchmark table: `results/validation/no_augmentation_model_comparison/validation_no_augmentation_model_comparison_benchmarks.csv`

## Estimand
- Human wisdom-of-the-crowd bars: `corr(mean human prediction across complete forecasters, true outcome)`
- LLM bars: `corr(mean prediction across 30 runs, true outcome)`

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
   - keep only the three displayed models: `Claude Sonnet 4.6`, `GPT-4.1`, `Gemini 2.5 Pro`
   - each row already contains the mean prediction vector across 30 runs for one model-condition pair
   - compute Pearson correlation between the 30-run mean prediction vector (`Q1`-`Q20`) and the true outcome vector
4. Add two vertical reference lines:
   - `No-treatment outcome baseline` = Pearson correlation between `efficiency_np` and `efficiency_p` from `pgg_CONFIGmerged_validation.csv`
   - `Noise ceiling` = the `Noise ceiling` correlation from `validation_no_augmentation_model_comparison_benchmarks.csv`
5. Plot layout:
   - horizontal orientation relative to the `260415` parent
   - first two rows: `Laypeople wisdom-of-the-crowd`, `Experts wisdom-of-the-crowd`
   - next three rows: `Claude Sonnet 4.6`, `GPT-4.1`, `Gemini 2.5 Pro`
   - within each LLM row, show `baseline` and `science_gpt41`
6. Error bars:
   - bootstrap the 20 experiments with replacement
   - recompute the plotted correlation on each bootstrap sample
   - interval shown: percentile bootstrap 95% CI (`2.5%`, `97.5%`)
7. Pair significance:
   - only for LLM baseline vs benchmark-paper pairs
   - compute paired bootstrap resamples over the same 20 experiments for both bars
   - draw significance stars next to rows where the paired bootstrap CI for `corr_augmented - corr_baseline` excludes `0`
   - the explanatory threshold text is intentionally omitted from the figure and belongs in the manuscript caption

## Notes
- This figure intentionally drops the five omitted models from the `260415` parent to reduce visual density in the main text.
- The starred LLM comparisons are still computed from the full paired bootstrap distribution even though the threshold key is not printed in-panel.

## Values used in the plot
### Bars
| group       | label                         | condition                     |    value |    ci_low |   ci_high |
|:------------|:------------------------------|:------------------------------|---------:|----------:|----------:|
| human_crowd | Laypeople wisdom-of-the-crowd | Laypeople wisdom-of-the-crowd | 0.603834 |  0.235601 |  0.823304 |
| human_crowd | Experts wisdom-of-the-crowd   | Experts wisdom-of-the-crowd   | 0.605577 |  0.204898 |  0.833936 |
| llm         | Claude Sonnet 4.6             | baseline                      | 0.664486 |  0.294574 |  0.870821 |
| llm         | Claude Sonnet 4.6             | science_gpt41                 | 0.799038 |  0.591508 |  0.916997 |
| llm         | GPT-4.1                       | baseline                      | 0.614593 |  0.199031 |  0.865299 |
| llm         | GPT-4.1                       | science_gpt41                 | 0.758389 |  0.499204 |  0.906247 |
| llm         | Gemini 2.5 Pro                | baseline                      | 0.399382 | -0.098288 |  0.746307 |
| llm         | Gemini 2.5 Pro                | science_gpt41                 | 0.842593 |  0.674446 |  0.9413   |

### Reference lines
| label                         |    value |
|:------------------------------|---------:|
| No-treatment outcome baseline | 0.541475 |
| Noise ceiling                 | 0.776535 |

### Pair Significance
| model             |   baseline_corr |   benchmark_corr |   delta_corr |   delta_ci95_low |   delta_ci95_high |   delta_ci99_low |   delta_ci99_high |   delta_ci999_low |   delta_ci999_high |   p_bootstrap_two_sided | sig_label   |   n_boot |
|:------------------|----------------:|-----------------:|-------------:|-----------------:|------------------:|-----------------:|------------------:|------------------:|-------------------:|------------------------:|:------------|---------:|
| Claude Sonnet 4.6 |        0.664486 |         0.799038 |     0.134552 |         0.001652 |          0.356288 |        -0.036146 |          0.455523 |         -0.102179 |           0.58414  |                 0.04676 | *           |    50000 |
| GPT-4.1           |        0.614593 |         0.758389 |     0.143796 |         0.009078 |          0.326918 |        -0.017315 |          0.402559 |         -0.05416  |           0.499937 |                 0.03    | *           |    50000 |
| Gemini 2.5 Pro    |        0.399382 |         0.842593 |     0.443211 |         0.159903 |          0.829808 |         0.102524 |          1.00046  |          0.051201 |           1.21543  |                 0       | ***         |    50000 |
