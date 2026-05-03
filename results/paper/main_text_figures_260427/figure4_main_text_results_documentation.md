# figure4_main_text_results

## Purpose
Main-text numerical summary for the Figure 4 results section in `main_text_260427`.

## Source files
- Predictive-model benchmark: `results/paper/main_text_figures_260427/figure4_predictive_model_best.csv`
- Elastic-net coefficients: `results/paper/main_text_figures_260427/figure4_metadata_coefficients_elastic_net_rows.csv`
- Elastic-net permutation importance: `results/paper/main_text_figures_260427/figure4_metadata_coefficients_elastic_net_permutation_rows.csv`

## Key manuscript values

### Best predictive model and out-of-sample R^2
- Claude Sonnet 4.6: elastic net, `R^2 = 0.007`
- GPT-4.1: elastic net, `R^2 = 0.011`
- Gemini 2.5 Pro: elastic net, `R^2 = 0.031`

### Empirical-paper coefficient (Elastic net, standardized)
- Claude Sonnet 4.6: `-0.0021` with bootstrap interval `[-0.0036, -0.0008]`
- GPT-4.1: `-0.0032` with bootstrap interval `[-0.0060, -0.0015]`
- Gemini 2.5 Pro: `-0.0127` with bootstrap interval `[-0.0173, -0.0082]`

### Empirical-paper permutation importance
- Claude Sonnet 4.6: `0.683%` increase in prediction error when permuted; rank `#3` of 9 features
- GPT-4.1: `0.779%` increase in prediction error when permuted; rank `#1` of 9 features
- Gemini 2.5 Pro: `2.069%` increase in prediction error when permuted; rank `#1` of 9 features

## Interpretation notes
- The best metadata-only predictive model is elastic net for all three displayed LLMs, but out-of-sample fit remains weak and never exceeds `R^2 = 0.031`.
- The empirical-paper indicator is directionally negative for all three displayed LLMs.
- Empirical status is the highest-importance metadata feature for GPT-4.1 and Gemini 2.5 Pro, and the third-highest for Claude Sonnet 4.6.
