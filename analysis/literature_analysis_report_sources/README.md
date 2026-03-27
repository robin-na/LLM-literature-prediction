# Literature Analysis Report Source Analysis

This folder contains analysis code for one-paper-at-a-time literature
augmentation, where each augmentation source is a paper-level analysis report
derived from the evidence-card extraction pipeline.

Files:

- `analyze_validation_analysis_report_sources.py`
  Runs the matched-baseline validation analysis for the original strict-paper
  source pool. It computes raw metrics and deltas versus no augmentation,
  writes summary CSVs, and generates PNG figures for distributions,
  baseline-context dumbbells, and mean-delta summaries.

- `analyze_validation_analysis_report_sources_extended2011.py`
  Merges the strict-paper and remaining-broad-paper outputs into one extended
  source pool, drops `PGG_MS_202502` for that merged run, and reruns the same
  validation analysis into a separate results folder.

- `analyze_validation_analysis_report_sources_significance.py`
  Computes paired-bootstrap significance for the extended `2011` single-paper
  `joint_reasoning` source run. It writes one row per paper and model with raw
  metrics, deltas, delta confidence intervals, and boolean flags for
  significant improvement or worsening versus the matched no-augmentation
  baseline. The current run includes the GPT-4.1 family plus any available
  GPT-5-family merged individual-paper outputs that have a matched baseline.

- `analyze_validation_analysis_report_source_features.py`
  Merges the extended single-paper source deltas with evidence-card metadata
  and WoS bibliographic metadata, then fits pooled clustered OLS models,
  model-specific OLS models, and simple random-intercept mixed models to test
  whether paper-level features explain augmentation gains. It writes the merged
  analysis dataset plus coefficient, fit-summary, and cross-model sign
  consistency CSVs.

- `plot_validation_analysis_report_source_ranked_levels.py`
  Builds ranked raw-performance plots for the extended literature source pool.
  The current default figure is correlation under `joint_reasoning`, shown side
  by side for GPT-4.1, GPT-4.1 Mini, and GPT-4.1 Nano, with raw baseline lines,
  paired-bootstrap confidence intervals, and a marked benchmark-paper rank.

- `plot_validation_analysis_report_source_overview.py`
  Generates higher-level overview figures for the extended single-paper source
  analysis: raw correlation and RMSE distributions versus model baselines,
  pairwise rank-robustness scatterplots across models, within-model
  correlation-vs-RMSE tradeoff plots, and grouped cross-validated brittleness
  plots for predicting augmentation gains from paper-level features. It also
  writes normalized "gap closed toward E-Net" datasets and summary CSVs plus a
  comparison plot, so weaker-baseline models can be compared on a common
  scale. The single-paper metric-distribution plots use a fixed 2x3 model grid
  so pending GPT-5-family model panels can remain visibly empty until outputs
  are ready.

- `plot_validation_analysis_report_source_convergence.py`
  Analyzes whether augmenting the same paper report makes different models'
  predictions move closer together. It focuses on a trusted five-model subset
  (`GPT-4.1`, `GPT-4.1 Mini`, `GPT-5.1`, `GPT-5 Mini`, `GPT-5 Nano`), rewrites
  predictions in treatment-effect space by subtracting the observed
  no-punishment efficiency, and writes per-paper convergence datasets plus a
  composite PNG figure. The figure shows the distribution of agreement gains
  over baseline, how those gains relate to changes in mean outcome accuracy,
  and pairwise outcome-agreement heatmaps for the unaugmented baseline and the
  benchmark `PGG_MS` report.
