# figure2_main_text_results

## Purpose
This file documents the exact `260427` numerical values used to write the main-text Results prose for the canonical benchmark-versus-human figure.

## Relationship to the canonical figure
- Semantic figure ID: `benchmark_vs_human_crowds_bar`
- Canonical figure documentation: `results/paper/main_text_figures_260427/figure2_benchmark_vs_human_crowds_bar_documentation.md`
- Canonical figure rows: `results/paper/main_text_figures_260427/figure2_benchmark_vs_human_crowds_bar_rows.csv`
- Canonical figure pair significance: `results/paper/main_text_figures_260427/figure2_benchmark_vs_human_crowds_bar_pair_significance.csv`

## Output files
- Baseline LLM vs human WoC comparisons: `results/paper/main_text_figures_260427/figure2_baseline_llm_vs_human_woc_comparison.csv`
- All-condition LLM vs human WoC comparisons: `results/paper/main_text_figures_260427/figure2_llm_vs_human_woc_all_conditions_bootstrap.csv`
- Unaugmented LLM pairwise comparisons: `results/paper/main_text_figures_260427/figure2_unaugmented_llm_pairwise_bootstrap.csv`
- Human WoC vs no-treatment baseline comparisons: `results/paper/main_text_figures_260427/figure2_human_woc_vs_no_treatment_baseline_bootstrap.csv`
- Main-text key values: `results/paper/main_text_figures_260427/figure2_main_text_key_values.csv`
- This documentation file: `results/paper/main_text_figures_260427/figure2_main_text_results_documentation.md`
- Generating script: `analysis/paper_figures/summarize_figure2_main_text_results_260427.py`

## Input files
- LLM 30-run mean predictions: `results/validation/literature_incremental_pgg_science_repeat30/incremental_pgg_science_avg_predictions.csv`
- Human forecasts: `science-data_and_code/data/processed_data/prediction_survey.csv`
- Validation outcomes: `input/pgg_CONFIGmerged_validation.csv`
- Canonical figure pair-significance table: `results/paper/main_text_figures_260427/figure2_benchmark_vs_human_crowds_bar_pair_significance.csv`

## Estimands
- Human WoC correlation: `corr(mean human prediction across complete forecasters, true outcome)`
- LLM correlation: `corr(mean prediction across 30 runs, true outcome)`
- Pairwise comparison delta: `corr(vector_a, truth) - corr(vector_b, truth)`, bootstrapped over the 20 experiments with paired resampling

## Notes for manuscript use
- Use the baseline-vs-human table for claims that off-the-shelf LLMs do not differ significantly from laypeople or experts.
- Use the unaugmented pairwise table for claims about the best unaugmented model versus the worst.
- Use the canonical figure pair-significance table for within-model benchmark-paper gains.
- Use the all-condition table for claims that benchmark-augmented models significantly outperform human WoC references.
- Use the human-vs-no-treatment table for claims that laypeople and experts outperform the no-treatment baseline.

## Core plotted values
### Human wisdom-of-the-crowd
| label                         |    value |
|:------------------------------|---------:|
| Laypeople wisdom-of-the-crowd | 0.603834 |
| Experts wisdom-of-the-crowd   | 0.605577 |

### Displayed LLM bars
| label             | condition     |    value |
|:------------------|:--------------|---------:|
| Claude Sonnet 4.6 | baseline      | 0.664486 |
| Claude Sonnet 4.6 | science_gpt41 | 0.799038 |
| GPT-4.1           | baseline      | 0.614593 |
| GPT-4.1           | science_gpt41 | 0.758389 |
| Gemini 2.5 Pro    | baseline      | 0.399382 |
| Gemini 2.5 Pro    | science_gpt41 | 0.842593 |

## Baseline LLM vs human WoC
| model             | human_reference   |   model_corr |   human_corr |   delta_corr_model_minus_human |   delta_ci95_low |   delta_ci95_high |   delta_ci99_low |   delta_ci99_high |   delta_ci999_low |   delta_ci999_high |   p_bootstrap_two_sided | verdict   |   n_boot |
|:------------------|:------------------|-------------:|-------------:|-------------------------------:|-----------------:|------------------:|-----------------:|------------------:|------------------:|-------------------:|------------------------:|:----------|---------:|
| Claude Sonnet 4.6 | Laypeople WoC     |     0.664486 |     0.603834 |                       0.060652 |        -0.089852 |          0.247107 |        -0.145517 |          0.327246 |         -0.236791 |           0.462512 |                 0.47716 | n.s.      |    50000 |
| Claude Sonnet 4.6 | Experts WoC       |     0.664486 |     0.605577 |                       0.058909 |        -0.052132 |          0.210094 |        -0.086965 |          0.271728 |         -0.138196 |           0.362542 |                 0.36076 | n.s.      |    50000 |
| GPT-4.1           | Laypeople WoC     |     0.614593 |     0.603834 |                       0.010759 |        -0.07255  |          0.096126 |        -0.09974  |          0.12544  |         -0.130378 |           0.16319  |                 0.77104 | n.s.      |    50000 |
| GPT-4.1           | Experts WoC       |     0.614593 |     0.605577 |                       0.009016 |        -0.054831 |          0.077398 |        -0.076496 |          0.101667 |         -0.099982 |           0.138721 |                 0.71172 | n.s.      |    50000 |
| Gemini 2.5 Pro    | Laypeople WoC     |     0.399382 |     0.603834 |                      -0.204452 |        -0.52269  |          0.104482 |        -0.651387 |          0.204572 |         -0.832    |           0.330023 |                 0.19292 | n.s.      |    50000 |
| Gemini 2.5 Pro    | Experts WoC       |     0.399382 |     0.605577 |                      -0.206195 |        -0.503148 |          0.079711 |        -0.623146 |          0.175168 |         -0.798745 |           0.298329 |                 0.15768 | n.s.      |    50000 |

## All displayed LLM conditions vs human WoC
| model             | condition     | human_reference   |   model_corr |   human_corr |   delta_model_minus_human |   delta_ci95_low |   delta_ci95_high |   p_bootstrap_two_sided | significant_95   |   n_boot |
|:------------------|:--------------|:------------------|-------------:|-------------:|--------------------------:|-----------------:|------------------:|------------------------:|:-----------------|---------:|
| Claude Sonnet 4.6 | baseline      | Laypeople WoC     |     0.664486 |     0.603834 |                  0.060652 |        -0.089619 |          0.24498  |                 0.46916 | False            |    50000 |
| Claude Sonnet 4.6 | baseline      | Experts WoC       |     0.664486 |     0.605577 |                  0.058909 |        -0.05328  |          0.210234 |                 0.35528 | False            |    50000 |
| Claude Sonnet 4.6 | science_gpt41 | Laypeople WoC     |     0.799038 |     0.603834 |                  0.195205 |         0.036505 |          0.440012 |                 0.00936 | True             |    50000 |
| Claude Sonnet 4.6 | science_gpt41 | Experts WoC       |     0.799038 |     0.605577 |                  0.193461 |         0.027802 |          0.451752 |                 0.01716 | True             |    50000 |
| GPT-4.1           | baseline      | Laypeople WoC     |     0.614593 |     0.603834 |                  0.010759 |        -0.072314 |          0.096727 |                 0.76116 | False            |    50000 |
| GPT-4.1           | baseline      | Experts WoC       |     0.614593 |     0.605577 |                  0.009016 |        -0.054948 |          0.076677 |                 0.7176  | False            |    50000 |
| GPT-4.1           | science_gpt41 | Laypeople WoC     |     0.758389 |     0.603834 |                  0.154556 |         0.038933 |          0.328795 |                 0.00296 | True             |    50000 |
| GPT-4.1           | science_gpt41 | Experts WoC       |     0.758389 |     0.605577 |                  0.152812 |         0.037328 |          0.325079 |                 0.00464 | True             |    50000 |
| Gemini 2.5 Pro    | baseline      | Laypeople WoC     |     0.399382 |     0.603834 |                 -0.204452 |        -0.519965 |          0.106158 |                 0.19796 | False            |    50000 |
| Gemini 2.5 Pro    | baseline      | Experts WoC       |     0.399382 |     0.605577 |                 -0.206195 |        -0.50103  |          0.076012 |                 0.15124 | False            |    50000 |
| Gemini 2.5 Pro    | science_gpt41 | Laypeople WoC     |     0.842593 |     0.603834 |                  0.23876  |         0.05018  |          0.526101 |                 0.00872 | True             |    50000 |
| Gemini 2.5 Pro    | science_gpt41 | Experts WoC       |     0.842593 |     0.605577 |                  0.237016 |         0.03976  |          0.545309 |                 0.01424 | True             |    50000 |

## Unaugmented LLM pairwise comparisons
| model_a           | model_b        |   corr_a |   corr_b |   delta_a_minus_b |   delta_ci95_low |   delta_ci95_high |   p_bootstrap_two_sided | significant_95   |   n_boot |
|:------------------|:---------------|---------:|---------:|------------------:|-----------------:|------------------:|------------------------:|:-----------------|---------:|
| Claude Sonnet 4.6 | GPT-4.1        | 0.664486 | 0.614593 |          0.049893 |        -0.069815 |          0.218394 |                 0.65416 | False            |    50000 |
| Claude Sonnet 4.6 | Gemini 2.5 Pro | 0.664486 | 0.399382 |          0.265104 |         0.057277 |          0.512265 |                 0.00948 | True             |    50000 |
| GPT-4.1           | Gemini 2.5 Pro | 0.614593 | 0.399382 |          0.215211 |        -0.088552 |          0.521086 |                 0.15968 | False            |    50000 |

## Human WoC vs no-treatment baseline
| human_reference   |   human_corr |   no_treatment_corr |   delta_human_minus_no_treatment |   delta_ci95_low |   delta_ci95_high |   delta_ci99_low |   delta_ci99_high |   delta_ci999_low |   delta_ci999_high |   p_bootstrap_two_sided | significant_95   |   n_boot |
|:------------------|-------------:|--------------------:|---------------------------------:|-----------------:|------------------:|-----------------:|------------------:|------------------:|-------------------:|------------------------:|:-----------------|---------:|
| Laypeople WoC     |     0.603834 |            0.541475 |                         0.062359 |         0.006363 |          0.132243 |        -0.006585 |          0.164805 |         -0.023389 |           0.215463 |                 0.02352 | True             |    50000 |
| Experts WoC       |     0.605577 |            0.541475 |                         0.064102 |        -0.015503 |          0.161924 |        -0.03997  |          0.202431 |         -0.074909 |           0.275071 |                 0.1324  | False            |    50000 |

## Main-text key values
| key                                       |      value | description                                                          | source_table                      |
|:------------------------------------------|-----------:|:---------------------------------------------------------------------|:----------------------------------|
| laypeople_woc_corr                        |   0.603834 | Laypeople wisdom-of-the-crowd correlation                            | figure2 rows                      |
| experts_woc_corr                          |   0.605577 | Experts wisdom-of-the-crowd correlation                              | figure2 rows                      |
| laypeople_complete_n                      | 468        | Number of laypeople with complete 20-question forecasts              | human prediction survey           |
| experts_complete_n                        |  38        | Number of experts with complete 20-question forecasts                | human prediction survey           |
| claude_sonnet_46_baseline_corr            |   0.664486 | Claude Sonnet 4.6 baseline correlation                               | figure2 rows                      |
| claude_sonnet_46_benchmark_corr           |   0.799038 | Claude Sonnet 4.6 benchmark-augmented correlation                    | figure2 rows                      |
| gpt_41_baseline_corr                      |   0.614593 | GPT-4.1 baseline correlation                                         | figure2 rows                      |
| gpt_41_benchmark_corr                     |   0.758389 | GPT-4.1 benchmark-augmented correlation                              | figure2 rows                      |
| gemini_25_pro_baseline_corr               |   0.399382 | Gemini 2.5 Pro baseline correlation                                  | figure2 rows                      |
| gemini_25_pro_benchmark_corr              |   0.842593 | Gemini 2.5 Pro benchmark-augmented correlation                       | figure2 rows                      |
| no_treatment_baseline_corr                |   0.541475 | No-treatment outcome baseline correlation                            | figure2 reference line            |
| noise_ceiling_corr                        |   0.776535 | Noise ceiling correlation                                            | figure2 reference line            |
| laypeople_minus_no_treatment_delta        |   0.062359 | Laypeople WoC minus no-treatment baseline correlation                | human vs no-treatment bootstrap   |
| laypeople_minus_no_treatment_ci95_low     |   0.006363 | Lower 95% CI for laypeople WoC minus no-treatment baseline           | human vs no-treatment bootstrap   |
| laypeople_minus_no_treatment_ci95_high    |   0.132243 | Upper 95% CI for laypeople WoC minus no-treatment baseline           | human vs no-treatment bootstrap   |
| experts_minus_no_treatment_delta          |   0.064102 | Experts WoC minus no-treatment baseline correlation                  | human vs no-treatment bootstrap   |
| experts_minus_no_treatment_ci95_low       |  -0.015503 | Lower 95% CI for experts WoC minus no-treatment baseline             | human vs no-treatment bootstrap   |
| experts_minus_no_treatment_ci95_high      |   0.161924 | Upper 95% CI for experts WoC minus no-treatment baseline             | human vs no-treatment bootstrap   |
| claude_baseline_minus_laypeople_delta     |   0.060652 | Claude Sonnet 4.6 baseline minus laypeople WoC correlation           | baseline vs human bootstrap       |
| claude_baseline_minus_laypeople_ci95_low  |  -0.089852 | Lower 95% CI for Claude baseline minus laypeople WoC                 | baseline vs human bootstrap       |
| claude_baseline_minus_laypeople_ci95_high |   0.247107 | Upper 95% CI for Claude baseline minus laypeople WoC                 | baseline vs human bootstrap       |
| claude_baseline_minus_experts_delta       |   0.058909 | Claude Sonnet 4.6 baseline minus experts WoC correlation             | baseline vs human bootstrap       |
| claude_baseline_minus_experts_ci95_low    |  -0.052132 | Lower 95% CI for Claude baseline minus experts WoC                   | baseline vs human bootstrap       |
| claude_baseline_minus_experts_ci95_high   |   0.210094 | Upper 95% CI for Claude baseline minus experts WoC                   | baseline vs human bootstrap       |
| claude_minus_gemini_baseline_delta        |   0.265104 | Claude Sonnet 4.6 baseline minus Gemini 2.5 Pro baseline correlation | unaugmented pairwise bootstrap    |
| claude_minus_gemini_baseline_ci95_low     |   0.057277 | Lower 95% CI for Claude minus Gemini baseline delta                  | unaugmented pairwise bootstrap    |
| claude_minus_gemini_baseline_ci95_high    |   0.512265 | Upper 95% CI for Claude minus Gemini baseline delta                  | unaugmented pairwise bootstrap    |
| gemini_25_pro_benchmark_gain_delta        |   0.443211 | Gemini 2.5 Pro benchmark minus baseline delta                        | figure2 pair significance         |
| gemini_25_pro_benchmark_gain_ci95_low     |   0.159903 | Lower 95% CI for Gemini 2.5 Pro benchmark gain                       | figure2 pair significance         |
| gemini_25_pro_benchmark_gain_ci95_high    |   0.829808 | Upper 95% CI for Gemini 2.5 Pro benchmark gain                       | figure2 pair significance         |
| gpt_41_benchmark_gain_delta               |   0.143796 | GPT-4.1 benchmark minus baseline delta                               | figure2 pair significance         |
| gpt_41_benchmark_gain_ci95_low            |   0.009078 | Lower 95% CI for GPT-4.1 benchmark gain                              | figure2 pair significance         |
| gpt_41_benchmark_gain_ci95_high           |   0.326918 | Upper 95% CI for GPT-4.1 benchmark gain                              | figure2 pair significance         |
| claude_sonnet_46_benchmark_gain_delta     |   0.134552 | Claude Sonnet 4.6 benchmark minus baseline delta                     | figure2 pair significance         |
| claude_sonnet_46_benchmark_gain_ci95_low  |   0.001652 | Lower 95% CI for Claude Sonnet 4.6 benchmark gain                    | figure2 pair significance         |
| claude_sonnet_46_benchmark_gain_ci95_high |   0.356288 | Upper 95% CI for Claude Sonnet 4.6 benchmark gain                    | figure2 pair significance         |
| gpt41_benchmark_minus_laypeople_delta     |   0.154556 | GPT-4.1 benchmark minus laypeople WoC correlation                    | all conditions vs human bootstrap |
| gpt41_benchmark_minus_laypeople_ci95_low  |   0.038933 | Lower 95% CI for GPT-4.1 benchmark minus laypeople WoC               | all conditions vs human bootstrap |
| gpt41_benchmark_minus_laypeople_ci95_high |   0.328795 | Upper 95% CI for GPT-4.1 benchmark minus laypeople WoC               | all conditions vs human bootstrap |
| gpt41_benchmark_minus_experts_delta       |   0.152812 | GPT-4.1 benchmark minus experts WoC correlation                      | all conditions vs human bootstrap |
| gpt41_benchmark_minus_experts_ci95_low    |   0.037328 | Lower 95% CI for GPT-4.1 benchmark minus experts WoC                 | all conditions vs human bootstrap |
| gpt41_benchmark_minus_experts_ci95_high   |   0.325079 | Upper 95% CI for GPT-4.1 benchmark minus experts WoC                 | all conditions vs human bootstrap |
