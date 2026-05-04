# Figure 2: Heterogeneity and Cross-LLM Agreement

Output:
- Figure: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/plots/paper/main_text_260415/figure2_heterogeneity_and_cross_model_agreement.png`
- Rows: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/results/paper/main_text_figures_260415/figure2_heterogeneity_and_cross_model_agreement_rows.csv`
- Summary: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/results/paper/main_text_figures_260415/figure2_heterogeneity_and_cross_model_agreement_summary.csv`
- Pairwise agreement: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/results/paper/main_text_figures_260415/figure2_heterogeneity_and_cross_model_agreement_pairwise.csv`

Purpose:
- Panel A shows that augmented performance varies substantially depending on which paper or collection is supplied.
- Panel B shows whether the three main-text LLMs agree on which augmented papers or collections perform better or worse using Pearson r.

Construction:
- LLMs: `Claude Sonnet 4.6`, `GPT-4.1`, and `Gemini 2.5 Pro` (displayed as `Gemini Pro 2.5` in the figure).
- Input types:
  - Individual papers: n = 2,011.
  - Collections: n = 717, operationalized as the corrected metadata-filter collection rows in `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/results/paper/main_text_figures_260409/collection_repeat_correlation_metrics.csv` plus the separate `Collection of all papers` row.
- Metric: `Corr(y_true, y_pred)`.
- Panel A boxplots use item-level augmented correlations from the corrected `260409` tables.
- Panel A boxes show median and interquartile range; whiskers span the 5th to 95th percentiles; outliers are plotted as faint points.
- Panel A diamond markers show each LLM's no-augmentation 30-run performance and are labeled as `No augmentation`.
- Panel A vertical dotted black line marks the noise ceiling from `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/results/validation/no_augmentation_model_comparison/validation_no_augmentation_model_comparison_benchmarks.csv`.
- Panel B heatmaps use pairwise complete items for the three displayed LLMs.
- Panel B masks the upper triangle because each agreement matrix is symmetric.
- Panel B uses one shared vertical colorbar centered between the individual-paper and collection heatmaps.
- Pearson r is computed across item-level augmented correlations.
- Pairwise table includes a standard one-sided parametric Pearson test of `r > 0`.

Data sources:
- Individual-paper correlations: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/results/paper/main_text_figures_260409/paper_repeat_correlation_metrics.csv`
- Collection correlations: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/results/paper/main_text_figures_260409/collection_repeat_correlation_metrics.csv`, with `Collection of all papers` reconstructed from the same source path used in `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/plots/paper/main_text_260415/figure2_individual_collection_density.png`.
- Unaugmented baseline table: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/results/paper/main_text_figures_260409/figure1_panel_b_baseline_vs_humans_correlation_cdf_llm_mean30_model_summary.csv`
- Noise ceiling table: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/results/validation/no_augmentation_model_comparison/validation_no_augmentation_model_comparison_benchmarks.csv`

Notes:
- All augmented values use `corr(mean prediction across repeats, truth)`, not mean of repeat-level correlations.
- Pairwise paper agreement uses 2010 shared papers.
- Pairwise collection agreement uses 716 shared collections.
- The parametric Pearson p-values are descriptive. They assume independent item rows, which is not strictly true for overlapping metadata-filter collections.
