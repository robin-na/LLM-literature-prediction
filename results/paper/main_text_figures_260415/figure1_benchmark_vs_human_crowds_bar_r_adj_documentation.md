# figure1_benchmark_vs_human_crowds_bar_r_adj

## Purpose
Adjusted-correlation Figure 1 variant for `main_text_260415`. This version replaces raw correlation with `r_adj`, following the disattenuated-correlation logic described in Section 2.3 of the supplement at `/Users/robinna/Downloads/supplement.pdf`.

## Output files
- Plot PNG: `plots/paper/main_text_260415/figure1_benchmark_vs_human_crowds_bar_r_adj.png`
- Plot rows: `results/paper/main_text_figures_260415/figure1_benchmark_vs_human_crowds_bar_r_adj_rows.csv`
- Reference lines: `results/paper/main_text_figures_260415/figure1_benchmark_vs_human_crowds_bar_r_adj_reference_lines.csv`
- Script: `analysis/paper_figures/plot_figure1_main_text_260415_r_adj.py`

## Input files
- LLM 30-run mean predictions: `results/validation/literature_incremental_pgg_science_repeat30/incremental_pgg_science_avg_predictions.csv`
- Human forecasts: `science-data_and_code/data/processed_data/prediction_survey.csv`
- Paired validation outcomes: `science-data_and_code/data/processed_data/df_paired_val.csv`
- Supplementary methods reference: `/Users/robinna/Downloads/supplement.pdf`

## Construction
1. Load the 20 paired validation outcomes and treatment-effect uncertainty from `df_paired_val.csv` and `adjusted_correlation.load_truth_and_sem()`.
2. For each human WoC bar:
   - keep complete forecasters only (`n_predictions_made == 20`)
   - average predictions within source (`prolific` or `sspp`) across participants
   - fit the latent-correlation model `profile_likelihood_ci_adjusted_corr(mean_prediction, truth, sem_y)`
3. For each LLM bar:
   - use the 30-run mean prediction vector from `incremental_pgg_science_avg_predictions.csv`
   - fit the same latent-correlation model against the 20 true outcomes with `sem_y`
4. Reference lines:
   - `No-treatment outcome baseline` = adjusted correlation between observed untreated outcome and observed treated outcome
   - `Adjusted ceiling` = `1.0`, because once outcome uncertainty is disattenuated, the raw attenuation ceiling at `0.7765` is no longer the right reference scale
5. Error bars:
   - `95%` profile-likelihood confidence intervals for the latent correlation parameter `rho`
   - this is closer to the supplement than bootstrap-over-experiments, because the interval comes from the same measurement-error model as the point estimate

## Notes
- This figure uses `r_adj`, not raw `Corr(y_true, y_pred)`.
- The point estimate is the latent correlation after adjusting for sampling uncertainty in the true treatment outcomes.
- Because this metric already corrects the outcome-side attenuation, the old raw noise ceiling line at `0.7765` should not be carried over.

## Values used in the plot
### Bars
| group       | label             | condition     |    value |   ci_low |   ci_high |
|:------------|:------------------|:--------------|---------:|---------:|----------:|
| human_crowd | Laypeople WoC     | Laypeople WoC | 0.8182   | 0.443192 |  0.98219  |
| human_crowd | Experts WoC       | Experts WoC   | 0.844282 | 0.484558 |  0.995831 |
| llm         | Claude Sonnet 4.6 | baseline      | 0.911999 | 0.619926 |  0.999    |
| llm         | Claude Sonnet 4.6 | science_gpt41 | 0.992301 | 0.797217 |  0.999    |
| llm         | GPT-5.1           | baseline      | 0.905626 | 0.609679 |  0.999    |
| llm         | GPT-5.1           | science_gpt41 | 0.977768 | 0.755619 |  0.999    |
| llm         | GPT-4.1 Mini      | baseline      | 0.890648 | 0.566868 |  0.999    |
| llm         | GPT-4.1 Mini      | science_gpt41 | 0.940732 | 0.679647 |  0.999    |
| llm         | GPT-4.1           | baseline      | 0.886562 | 0.54409  |  0.999    |
| llm         | GPT-4.1           | science_gpt41 | 0.985237 | 0.769824 |  0.999    |
| llm         | GPT-5 Nano        | baseline      | 0.863543 | 0.504443 |  0.999    |
| llm         | GPT-5 Nano        | science_gpt41 | 0.94367  | 0.68671  |  0.999    |
| llm         | GPT-5 Mini        | baseline      | 0.890816 | 0.54917  |  0.999    |
| llm         | GPT-5 Mini        | science_gpt41 | 1        | 0.88278  |  1        |
| llm         | GPT-4.1 Nano      | baseline      | 0.741544 | 0.313397 |  0.947275 |
| llm         | GPT-4.1 Nano      | science_gpt41 | 0.878226 | 0.53962  |  0.999    |
| llm         | Gemini 2.5 Pro    | baseline      | 0.623243 | 0.131549 |  0.882575 |
| llm         | Gemini 2.5 Pro    | science_gpt41 | 1        | 0.88208  |  1        |

### Reference lines
| label                         |    value |
|:------------------------------|---------:|
| No-treatment outcome baseline | 0.752978 |
| Adjusted ceiling              | 1        |
