# Figure 4: Empirical Design Limitations

Inputs:
- `batch_processing/output_csv/simple_batch_197papers.xlsx`
- `batch_processing/output_csv/simple_batch_810papers.xlsx`
- filtered to the `broad_all` main-analysis inventory in `literature/output/paper_analysis_reports/broad_all/report_index.csv` (`2,011` papers); dropped `61` out-of-scope papers and `294` rows.

Rows included after filtering: `3630` lab-condition rows grouped by `custom_id` (`756` papers).

Design parameter definition: 14 design parameters. Punishment-ID and reward-ID visibility are merged into one ID-visibility parameter. Punishment-existence and endowment variables are excluded.

Panel A: Percent of lab papers where each design parameter is reported at least once, and percent where it varies within paper.

Panel B: Paper-level distribution. Reported means every lab-condition row in that paper reports the parameter. Varied means the parameter takes more than one value across lab-condition rows in that paper.

Panel C: Percent of experiments by group-size and number-of-rounds bins. The heatmap uses `3362` rows with numeric group size >= 2 and number of rounds >= 1.
