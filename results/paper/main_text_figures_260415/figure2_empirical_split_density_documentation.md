# Exploratory empirical split density

Output:
- Figure: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/plots/paper/main_text_260415/figure2_empirical_split_density.png`
- Rows: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/results/paper/main_text_figures_260415/figure2_empirical_split_density_rows.csv`
- Summary: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/results/paper/main_text_figures_260415/figure2_empirical_split_density_summary.csv`

Construction:
- Same three models as the main-text Figure 2: `Claude Sonnet 4.6`, `GPT-4.1`, `Gemini 2.5 Pro`.
- Left column: augmented individual-paper correlations split by paper-level empirical label.
- Right column: augmented collection correlations split only across the subset of collection reports with an explicit type filter:
  - `type_value = empirical`
  - `type_value = theoretical`
- Collections with `type_value = ANY` are excluded from the split overlay, because they are not cleanly classifiable as empirical or non-empirical.

Data sources:
- Individual-paper correlations: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/results/paper/main_text_figures_260409/paper_repeat_correlation_metrics.csv`
- Individual-paper empirical labels: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/results/validation/literature_analysis_report_sources_repeat5/paper_feature_analysis_dataset_repeat5.csv`
- Collection correlations and type labels: constructed through `build_collection_df()` in `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/analysis/paper_figures/plot_collection_linear_metadata_effect_260409.py`
- No-augmentation baseline line: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/results/paper/main_text_figures_260409/figure1_panel_b_baseline_vs_humans_correlation_cdf_llm_mean30_model_summary.csv`
- Estimated ceiling: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/results/validation/no_augmentation_model_comparison/validation_no_augmentation_model_comparison_benchmarks.csv`

Counts:
- `Claude Sonnet 4.6` / `individual_papers`: 908 empirical and 1047 non-empirical papers
- `Claude Sonnet 4.6` / `type_filtered_collections`: 133 empirical and 137 non-empirical collections
- `GPT-4.1` / `individual_papers`: 908 empirical and 1047 non-empirical papers
- `GPT-4.1` / `type_filtered_collections`: 133 empirical and 137 non-empirical collections
- `Gemini 2.5 Pro` / `individual_papers`: 908 empirical and 1047 non-empirical papers
- `Gemini 2.5 Pro` / `type_filtered_collections`: 133 empirical and 137 non-empirical collections
