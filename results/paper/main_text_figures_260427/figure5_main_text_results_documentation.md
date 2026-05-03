# figure5_main_text_results

## Purpose
Main-text numerical summary for the Figure 5 results section in `main_text_260427`.

## Source files
- Main-text corpus IDs: `results/validation/literature_analysis_report_sources_overview/single_paper_overview_dataset.csv`
- Extraction workbooks: `batch_processing/output_csv/simple_batch_197papers.xlsx`, `batch_processing/output_csv/simple_batch_810papers.xlsx`
- Panel A rows: `results/paper/main_text_figures_260427/figure5_reported_parameter_count_rows.csv`
- Panel B rows: `results/paper/main_text_figures_260427/figure5_variation_vs_importance_rows.csv`
- Panel C rows: `results/paper/main_text_figures_260427/figure5_value_distribution_rows.csv`
- Evenness comparison: `results/paper/main_text_figures_260427/figure5_value_evenness_vs_benchmark_rows.csv`
- This summary script treats those Figure 5 row tables as canonical for the displayed 12-parameter comparison. In manuscript prose, describe the `14 -> 12` reduction as excluding reward cost and reward technology because they are only defined when reward exists.

## Workbook methodology
- The main-text corpus contains `2,011` unique papers.
- `943` of those papers appear in the extraction workbooks; `1,068` corpus papers have no workbook row.
- A paper counts as empirical if **any** workbook row for that `custom_id` is marked `METHOD_empirical`.
- A paper counts as including lab experiments if **any** workbook row for that `custom_id` is marked `METHOD_lab`.
- Two papers are marked `METHOD_lab` without also being marked `METHOD_empirical`, so for the paper-level denominator we treat `METHOD_lab` as sufficient evidence of empirical status.
- Under that inclusive rule, the workbook-based empirical denominator is `940` papers, and `756` of them (`80.4%`) include at least one lab row.
- The lab-row subset used for the causal-density opener contains `3,630` rows marked `METHOD_lab` in the workbooks.

## Key manuscript values

### Corpus composition
- Strict workbook-based empirical papers (`METHOD_empirical`): `938`
- Inclusive workbook-based empirical papers (`METHOD_empirical` or `METHOD_lab`): `940`
- Workbook-based lab papers in that corpus: `756`
- Share of inclusive empirical papers that include at least one lab row: `80.4%`

### Causal density from the workbook
- Lab rows: `3,630`
- Mean `number_IVs`: `2.1` (median `2`; `2,983` rows with nonmissing IV counts)
- Mean `number_DVs`: `5.1` (median `5`; `2,987` rows with nonmissing DV counts)
- Unique IV labels across lab rows: `757`
- Unique DV labels across lab rows: `1,968`
- After conservative lexical harmonization, these counts are `756` IV labels and `1,968` DV labels.
- Under a broader exploratory family heuristic, they drop to `322` IV families and `512` DV families.
- Most common IV labels: punishment_mechanism (229), punishment (195), communication (120), treatment (107), group_size (99), game_type (94), punishment_opportunity (67), sanction_type (63), matching_protocol (55), phase (46)
- Most common DV labels: individual_contribution (1798), group_contribution (1576), punishment_assigned (741), punishment_received (569), net_earnings (375), efficiency (277), individual_earnings (126), earnings (123), cooperation_rate (107), individual_cooperation (103)

### Benchmark-parameter coverage in the aggregate
- Group size reported in `751` of `756` lab papers (`99.3%`)
- Contribution type reported in `728` papers (`96.3%`)
- Game length reported in `724` papers (`95.8%`)
- Contribution framing reported in `493` papers (`65.2%`)
- Punishment cost reported in `460` papers (`60.8%`)
- Punishment technology reported in `427` papers (`56.5%`)
- Communication reported in `230` papers (`30.4%`)
- Reward reported in `197` papers (`26.1%`)

### Outcome coverage in the aggregate
- Contribution-related outcomes appear in `396` of `756` lab papers (`52.4%`)
- Punishment-related outcomes appear in `428` papers (`56.6%`)
- Earnings/payoff outcomes appear in `308` papers (`40.7%`)
- Cooperation outcomes appear in `110` papers (`14.6%`)
- Efficiency/welfare outcomes appear in `78` papers (`10.3%`)

### Panel A: parameter reporting
- Lab-experiment rows: `3,630`
- Displayed benchmark-comparable parameters: `12`
- Mean parameters reported per experiment: `6.2`
- Median parameters reported per experiment: `6`
- Experiments reporting 7 or fewer parameters: `2,625` (`72.3%`)
- Experiments reporting all `12` parameters: `41` (`1.1%`)

### Panel B: variation versus benchmark importance
- Lab papers: `756`
- Pearson `r = -0.127`, `p = 0.693`
- Most frequently varied parameters: Game length (10.2%; n=77), Group size (9.9%; n=75), Punishment technology (6.3%; n=48)
- Most predictive benchmark parameters: Communication (60.0% error increase when shuffled; varied in 3.7% of papers), Contribution framing (17.9% error increase when shuffled; varied in 0.9% of papers), Contribution type (14.6% error increase when shuffled; varied in 1.6% of papers)
- The benchmark importance values are the canonical Figure 5 values: percent increase in prediction error when the parameter is shuffled in the benchmark model.

### Panel C: concentration in a narrow subset of settings
- Mean literature evenness across the 12 displayed parameters: `0.628`
- Mean benchmark evenness across the same parameters: `0.990`
- Most concentrated modal values: Default contribution=opt in (98.7%), Show other summaries=visible (95.3%), Group size=2-6 (91.1%), Chat=disabled (84.0%), All-or-nothing=all-or-nothing (74.0%), Show punishment/reward ID=hidden (70.5%)

## Interpretation notes
- The workbook-based method supports the claim that most empirical papers in the main-text corpus include lab experiments. Under the inclusive workbook rule (`METHOD_empirical` or `METHOD_lab`), the denominator is `940`, not the evidence-card count of `947`.
- The causal-density opener can be grounded in the workbook itself: typical lab rows already involve multiple independent variables and multiple dependent variables, and the label vocabulary is very large.
- The raw `757` / `1,968` counts are exact-label counts, not hand-harmonized concept counts. Conservative lexical harmonization changes almost nothing (`756` IVs, `1,968` DVs), while a broader exploratory family heuristic still leaves hundreds of families (`322` IV, `512` DV).
- Figure 5 is therefore not just about sparsity. The literature contains many experiments, many manipulated factors, and many outcomes, yet it remains misaligned with the benchmark because relevant parameters are underreported, the wrong parameters are varied most often, and observed values cluster in narrow regions of the design space.

## Output tables
- `figure5_main_text_key_values.csv`
- `figure5_workbook_iv_dv_label_counts.csv`
- `figure5_workbook_iv_dv_harmonization_rows.csv`
- `figure5_workbook_iv_dv_harmonization_summary.csv`
- `figure5_workbook_iv_dv_family_summary.csv`
- `figure5_workbook_concept_coverage.csv`