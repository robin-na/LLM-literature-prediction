# Figure 2: Individual Papers and Collections

Output:
- Figure: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/plots/paper/main_text_260415/figure2_individual_collection_density.png`
- Density rows: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/results/paper/main_text_figures_260415/figure2_individual_collection_density_rows.csv`
- Summary table: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/results/paper/main_text_figures_260415/figure2_individual_collection_density_summary.csv`

How the figure is constructed:
- Rows are the three main-text models, in this order: `Claude Sonnet 4.6`, `GPT-4.1`, `Gemini 2.5 Pro`.
- Left column shows the distribution of augmented correlation across the `2,011` individual-paper reports.
- Right column shows the distribution of augmented correlation across the collection reports, with the panel titled `717 collections`.
- The density itself comes from the corrected metadata-filter collection table, and a separate vertical reference line marks the `Collection of all papers` entry (`broad_all_2011`), which contains all `2,011` papers.
- The x-axis is the performance scale, `Corr(y_true, y_pred)`.
- Each panel includes:
  - a solid vertical line for the mean augmented correlation within that panel
  - a dashed vertical line for the model's unaugmented baseline
  - on the collection side only, a heavier dash-dot vertical line for the `Collection of all papers`

Primary data sources:
- Individual-paper density values: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/results/paper/main_text_figures_260409/paper_repeat_correlation_metrics.csv`
- Collection density values: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/results/paper/main_text_figures_260409/collection_repeat_correlation_metrics.csv`
- Unaugmented baseline lines (`corr(mean across 30 runs, truth)`): `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/results/paper/main_text_figures_260409/figure1_panel_b_baseline_vs_humans_correlation_cdf_llm_mean30_model_summary.csv`
- `Everything` collection:
  - GPT-4.1: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/results/validation/literature_collection_analysis_reports_metadata_filters/validation_literature_collection_analysis_report_metadata_filters_avg_predictions.csv`
  - Claude Sonnet 4.6: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/claude_batch_output/prediction_outputs_2026/prediction_outputs_2026_long.csv`
  - Gemini 2.5 Pro: `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/gemini_batch_output/prediction_outputs_2026/prediction_outputs_2026_long.csv`

Metric definition:
- All augmented density values come from the corrected `260409` pipeline and use `corr(mean prediction across repeats, truth)`, not mean of repeat-level correlations.
- The baseline line uses the same estimand, but with the mean prediction across `30` baseline runs.

Collection count note:
- `Claude Sonnet 4.6`: 716 metadata-filter collections in the corrected density table
- `GPT-4.1`: 715 metadata-filter collections in the corrected density table
- `Gemini 2.5 Pro`: 716 metadata-filter collections in the corrected density table
- The old metadata-filter design space contains `716` report-indexed collections plus the separate `Everything` collection. In the corrected `260409` repeat-intersection table, GPT-4.1 is missing one metadata-filter collection, so its right-panel density uses `715` values.
