# Collection Report Analysis

- `analyze_validation_collection_analysis_reports_stage1.py`
  Evaluates the 9 synthesized collection-level literature analysis reports
  against the matched no-augmentation baseline for `GPT-4.1`,
  `GPT-4.1 Mini`, and `GPT-4.1 Nano` in joint-with-explanation mode.
  It writes:
  - per-variant raw metrics and paired-bootstrap deltas
  - ranked tables within each model
  - model-level summaries of the best and worst collection variants
  - top/bottom tables for quick inspection

- `plot_validation_collection_analysis_reports_stage1.py`
  Plots the 9 collection variants with readable row labels and explicit A/B/C
  definitions. Each panel shows raw metric values for the three models, with
  model-specific no-augmentation baselines shown as dashed vertical lines and
  paired-bootstrap significance marked on the points. It also writes a
  correlation-only figure with one subplot per model.

- `analyze_validation_collection_analysis_reports_repeat5.py`
  Re-evaluates the stage-1 collection reports after averaging predictions over
  five runs. It combines:
  - the no-augmentation baseline `initial + rep1..rep4`
  - each collection report `rep1 + rep2..rep5`
  - the `PGG_MS` benchmark paper analysis report `rep1 + rep2..rep5`
  - the direct full-paper `PGG_MS` benchmark `rep1..rep5`
  It writes averaged prediction tables plus per-variant raw metrics,
  paired-bootstrap deltas versus the averaged baseline, ranked tables, and
  top/bottom summaries. `R^2` is computed against the learning-wave treatment
  mean baseline. Missing models are skipped automatically, so the script can be
  rerun as additional repeat outputs arrive. It also supports the newer one-file
  `gpt-5.1` literature suite, where baseline, benchmark, and collection runs
  all live in the same `55`-request batch output.

- `plot_validation_collection_analysis_reports_repeat5.py`
  Plots the repeat-5 validation results for correlation, `R^2`, and RMSE, one
  subplot per model slot in a fixed 2×3 layout (top row GPT-4.1 family, bottom
  row GPT-5 family). Pending models are shown as empty placeholder panels. Each
  figure includes:
  - the `E-Net` benchmark pinned at the far left
  - the `PGG_MS` benchmark paper analysis-report augmentation
  - the direct full-paper `PGG_MS` augmentation
  - the 9 collection variants sorted best-to-worst within each model
  - a dashed horizontal line for the matched five-run no-augmentation baseline
  - paired-bootstrap 95% CIs for augmentation-minus-baseline, translated onto
    the raw metric scale and drawn as vertical point-range intervals

- `check_benchmark_repeat_stability.py`
  Diagnoses how stable the five-run no-augmentation baseline and the five-run
  `PGG_MS` benchmark paper are for the repeat-5 collection analysis. It writes:
  - run-level metrics for each of the five baseline and benchmark runs
  - metrics after averaging predictions across the five runs
  - summary tables of run-to-run dispersion
  - question-level prediction standard deviations across runs
  - leave-one-run-out summaries showing how much each run moves the averaged
  benchmark or baseline result

- `plot_validation_collection_analysis_report_convergence.py`
  Examines whether the 9 collection-report variants make trusted models'
  predicted outcomes more similar to one another. It uses the same trusted
  five-model subset as the single-paper convergence analysis (`GPT-4.1`,
  `GPT-4.1 Mini`, `GPT-5.1`, `GPT-5 Mini`, `GPT-5 Nano`), matches against the
  five-run averaged no-augmentation baseline, and writes:
  - a per-variant convergence dataset
  - a one-row summary CSV
  - pairwise model-correlation matrices for the baseline and the
    most-convergent collection report
  - a 2x2 PNG figure with agreement-gain lollipops, agreement-vs-accuracy
    scatter, and baseline-versus-best-collection heatmaps

- `repeat5_variance_and_baseline_issue_report.md`
  Discussion note describing the current interpretability problem in the
  repeat-5 augmentation analysis: repeat noise is sometimes comparable to
  between-model variation, and models begin from different baselines, so naive
  pooling and raw counts of "helpful" augmentations can be misleading. The note
  summarizes what is already established, the exact failure modes, and the main
  design decisions still to be made.
