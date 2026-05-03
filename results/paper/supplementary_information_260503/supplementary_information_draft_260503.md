Supplementary Information

Scientific Literature Does Not Reliably Improve Large Language Model Predictions of Behavioral Experiments

Robin Na, Duncan J. Watts, and Abdullah Almaatouq

Draft status, May 3, 2026. This draft is source-backed where possible and uses CHECK markers where the current code, historical code, or manuscript language may still need confirmation. The main manuscript tab was not edited. This SI tab should eventually be cleaned of CHECK markers before submission.

S1. Prediction benchmark, evaluation metrics, and uncertainty estimates

S1.1 Benchmark prediction task

The prediction task comes from the public-goods-game punishment benchmark reported in Alsobay et al. (2026). We defer participant recruitment, experimental implementation, payment details, and the full integrative-experiment design procedure to that paper, because those details define the benchmark rather than the literature-augmentation procedure introduced here. We summarize only the information needed to reproduce the evaluation in the present paper.

The validation set contained 20 paired public goods game experiments. In each pair, the control condition disabled peer punishment and the treatment condition enabled peer punishment while keeping the remaining game design parameters fixed. The forecaster input was the 14-parameter game description and the observed mean efficiency in the control condition. The target was mean efficiency in the matched treatment condition. Efficiency was defined as the ratio of the group's realized payoff to the payoff that would have been obtained under full cooperation.

CHECK: Confirm whether the SI should say "20 paired experiments" or "20 validation configurations," and whether the trial count should be repeated here as 8 to 12 trials per condition or left entirely to Alsobay et al. (2026).

S1.2 Primary performance metric

The primary performance metric was the Pearson correlation between the vector of predicted treatment efficiencies and the vector of observed treatment efficiencies across the 20 validation experiments. We used correlation as the primary metric because the paper asks whether a source of information helps models rank and distinguish experimental outcomes across the design space, rather than whether it is calibrated on the absolute efficiency scale.

For robustness, we also computed root mean squared error (RMSE), R2 relative to the training-mean baseline, and directional accuracy, where directional accuracy measures whether the prediction correctly classified the treatment as increasing or decreasing efficiency relative to the observed control condition. These additional metrics are reported in the supplementary result tables and figures.

S1.3 Bootstrap confidence intervals and paired comparisons

All uncertainty intervals reported for correlation-based performance used a nonparametric bootstrap over the 20 validation experiments. For each bootstrap replicate, we sampled 20 experiments with replacement and recomputed the metric on that resampled set. For confidence intervals around a single model or benchmark, the interval is the 2.5th to 97.5th percentile of the bootstrap distribution.

For paired comparisons, including augmentation versus no augmentation for the same LLM, each bootstrap replicate sampled the same set of experiments for both prediction vectors. The reported difference was the augmented metric minus the comparison metric. A paired comparison was marked significant at the 95%, 99%, or 99.9% level when the corresponding percentile interval for the paired difference excluded zero.

S1.4 Baselines and reference lines

The no-treatment outcome baseline predicts that treatment-condition efficiency equals the observed control-condition efficiency for the same experimental configuration. In the validation set, the correlation between control efficiency and treatment efficiency was r = 0.541. This value appears as the no-treatment reference line in Fig. 2.

The estimated noise ceiling accounts for finite experimental sampling error in the observed treatment outcomes. The analysis estimated condition-level standard errors from trial-level outcomes in the benchmark validation data, separated sampling noise from observed between-condition variation, and computed the maximum correlation expected when predicting noisy observed treatment means. The resulting correlation ceiling was r = 0.777. The corresponding benchmark table also reports RMSE = 4.273 and R2 = 0.582 for the noise ceiling.

CHECK: The code also estimates a control-to-treatment ceiling and a target-only ceiling. The main figures use the target-only correlation ceiling from `validation_no_augmentation_model_comparison_benchmarks.csv`. Confirm this is the exact ceiling definition we want to name in prose.

S1.5 Human crowd benchmarks

Human comparison values use the benchmark-paper forecaster data. The layperson and expert crowd benchmarks were computed by retaining forecasters who completed all 20 validation predictions, averaging predictions within each group for each experiment, and correlating the resulting crowd mean vector with observed treatment outcomes. This produced similar crowd-level correlations for laypeople (r = 0.604) and experts (r = 0.606). Details of forecaster recruitment and survey administration are reported in Alsobay et al. (2026).

S1.6 Planned supplementary outputs

This section should include a table of all evaluation metrics for human crowds, no-treatment baseline, statistical benchmarks from Alsobay et al. (2026), unaugmented LLMs, benchmark-paper augmentation, individual-paper augmentation, collection-report augmentation, and all-paper report augmentation. It should also include the bootstrap settings, random seeds, and the exact row sources used to generate the main-text figures.

S2. Article corpus construction and full-text processing

S2.1 Web of Science searches

We constructed the article corpus from Web of Science Core Collection searches designed to capture research on punishment, sanctions, and cooperation in public-goods-game-like or adjacent social-dilemma settings. The project used two search rounds: an earlier search in 2024 and a later search collected in October 2025. Deduplicating these search exports by Web of Science accession number, DOI, and then normalized title/source/year produced 3,087 unique records. The October 2025 export contained 2,960 records; the earlier export contained 2,765 records. The combined corpus was used because some records present in the earlier export no longer appeared in the October 2025 export under what was intended to be the same search logic.

CHECK: Insert the exact Web of Science topic query, document-type/language filters, and citation-topic filters here. Also confirm whether we should explicitly state that the older-only records likely reflect WoS-side category or label changes rather than an intentional substantive change in inclusion criteria.

S2.2 Full-text retrieval and conversion

Full texts were obtained through institutional library access and retained project markdown files. The October 2025 file-info table contained 2,756 rows with both a file path and a custom identifier, and all 2,756 were present in the parsed structured-report table. The structured-report corpus contained 2,851 successfully parsed full-text documents. Of these, 2,848 matched a record in the combined Web of Science search universe and 3 were retained markdown-only files. The benchmark manuscript was one of the retained markdown-only files and was excluded from the published-literature augmentation corpus.

The current corpus accounting is therefore: two Web of Science search rounds returned 3,087 unique records; full texts were obtained or retained for 2,851 documents and converted into structured reports; the broad relevance screen retained 2,012 records; excluding the benchmark manuscript left 2,011 papers for the main individual-paper augmentation analyses.

S2.3 Treatment of older-search-only records

The final 2,011-paper augmentation inventory is not a strict subset of the October 2025 2,960-record export. Reconciliation against the combined records showed that 1,955 papers matched October 2025 full-text rows, 30 additional papers matched October 2025 metadata but lacked a full-text path in the October 2025 file-info table, and 26 papers traced only to older Web of Science or project corpus records. The older-only records that entered the final corpus were English journal articles in the older metadata and were enriched for broader adjacent cooperation/punishment literatures.

CHECK: Decide whether to keep this reconciliation in the main SI or move it to a supplementary table. It is important for auditability, but may distract readers unless presented as a compact count table.

S2.4 Exclusion of the benchmark manuscript

The benchmark manuscript, internally identified as `PGG_MS_202502`, was processed during some extraction and report-generation steps to allow benchmark-paper augmentation. It was excluded from the 2,011-paper broader-literature inventory so that the broader-literature analysis did not include the target benchmark paper. Benchmark-paper augmentation is reported separately as a best-case aligned input.

S3. Structured reports and relevance screening

S3.1 Structured report generation

Each full-text document was converted into a structured, prediction-focused report using GPT-4.1. The prompt instructed the model to use only the paper content, distinguish payoff-related outcomes from non-payoff behavioral outcomes, assess relevance to the target PGG punishment prediction task, and code which benchmark design dimensions were discussed. Structured report generation used temperature 0. The full prompt and output schema are provided in S10.

The report included study type, target relevance, outcome type, overall effect direction for efficiency or related payoff outcomes, key findings, prediction guidance, dimension-level evidence, and important limitations. These structured reports are the same objects described in the Study Overview of the main text.

S3.2 Relevance screen for the 2,011-paper inventory

The broad main-analysis inventory was built from the structured reports. The screen retained papers with potential relevance to at least one of the benchmark concepts: a public-goods-game-like or adjacent social-dilemma setting, punishment or sanctioning, payoff/efficiency or a closely related outcome, and at least one benchmark design dimension that could inform prediction. This screen was intentionally broader than a strict filter for lab PGG efficiency studies, because the literature-augmentation analysis asked whether LLMs benefit from the wider body of potentially relevant literature.

The broad screen retained 2,012 records. After excluding the benchmark manuscript, the final inventory contained 2,011 papers. This inventory includes empirical, theoretical, review, and adjacent-domain papers. It should not be interpreted as 2,011 papers that all directly report benchmark-like laboratory PGG efficiency outcomes.

CHECK: The internal labels `exact`, `close`, `adjacent`, `weak`, and `none` should be described in the full prompt appendix. In prose, avoid making these labels do too much work for readers.

S3.3 Relation to the empirical-design subset

The 2,011-paper inventory is broader than the empirical-design subset used for Fig. 5. Fig. 5 begins from the same broad inventory but then uses a separate condition-level extraction pipeline to identify empirical papers, laboratory experiments, and reported design parameters. The Fig. 5 denominator is therefore not the same as the 2,011-paper augmentation denominator.

S4. Literature augmentation inputs and collection construction

S4.1 Individual-paper augmentation

For individual-paper augmentation, each LLM received the same prediction prompt used in the unaugmented baseline plus one structured analysis report derived from one paper. The report was wrapped with instructions telling the LLM to treat it as contextual evidence about how design features may change the efficiency impact of punishment and to respect the report's limitations. The prediction output contained one prediction for each of the 20 validation experiments.

S4.2 Benchmark-paper augmentation

Benchmark-paper augmentation used the same prediction structure but provided a structured report generated from the benchmark paper itself. The benchmark-paper report did not include the exact target treatment outcomes for the 20 validation experiments used for evaluation; it summarized the aligned benchmark study and the broader experimental program from which the benchmark came. This condition was analyzed separately from broader-literature augmentation because it represents a highly aligned input rather than an ordinary article from the prior literature.

S4.3 Multi-paper collection reports

Multi-paper augmentation used consolidated literature reports synthesized from sets of individual structured reports. The current metadata-based workflow grouped papers by up to three filters over five metadata dimensions: study type, citation quartile, journal-impact quartile, publication-period quartile, and coarse journal discipline. Collections with fewer than two papers were dropped. The metadata-collection builder retained 716 metadata-filtered collections. Together with the all-paper report for the 2,011-paper inventory, this gives 717 multi-paper literature inputs described in the main text.

CHECK: Downstream summary files show 716 metadata-filtered collections, plus the all-paper report. Some model-specific summaries count additional variants when benchmark-paper augmentation is included. Confirm that the main text's "717 multi-paper collections" should be interpreted as 716 metadata-filtered collection reports plus the all-paper report.

S4.4 Collection metadata definitions

Study type was derived from the structured report's primary paper type. Citation quartiles were computed from Times Cited, All Databases in the Web of Science metadata. Journal-impact quartiles were derived from the 2024-2025 Journal Citation Reports match by ISSN or eISSN. Publication-year quartiles were computed from observed publication years in the catalog. Coarse discipline was derived from Web of Science category labels using deterministic keyword rules for economics, psychology/social science, biology/evolution, mathematics/physics/computer science, multidisciplinary science, and other fields. A paper could belong to more than one discipline category when Web of Science supplied multiple categories.

S5. LLM prediction prompts, model versions, API parameters, and repeat averaging

S5.1 Models

The current analysis includes 8 proprietary LLMs: GPT-4.1, GPT-4.1 Mini, GPT-4.1 Nano, GPT-5.1, GPT-5 Mini, GPT-5 Nano, Claude Sonnet 4.6, and Gemini 2.5 Pro. The main text reports three of these models: Claude Sonnet 4.6, GPT-4.1, and Gemini 2.5 Pro. Historical project outputs also contain older or omitted models, including Claude Opus, Claude Haiku, and Gemini 2.5 Flash; those are not part of the current 8-model analysis unless explicitly labeled as historical or exploratory.

CHECK: Confirm exact provider-side model IDs for Claude Sonnet 4.6 and Gemini 2.5 Pro as submitted in final batches.

S5.2 Prediction prompt format

Prediction prompts used a common task preamble explaining the PGG punishment prediction task and the definition of efficiency. For joint prediction requests, the prompt presented all 20 validation experiments in one table. Each row included the control efficiency percentage, player count, number of rounds, chat availability, all-or-nothing contribution indicator, default-contribution framing, MPCR, punishment cost, punishment technology, reward availability, reward cost, reward technology, whether total rounds were shown, whether peer outcomes were shown, and whether punishers or rewarders were identified. The model was instructed to return a JSON object keyed by question IDs, with each value containing an explanation and an integer efficiency prediction.

The unaugmented baseline contained only the task preamble and the validation experiment table. Augmented prompts inserted either a single-paper report, a benchmark-paper report, a collection report, or the all-paper report before the same validation experiment table.

S5.3 Generation parameters and repeated calls

Prediction calls used temperature 1.0. For OpenAI chat-completion prediction requests, temperature was left unspecified, corresponding to the API default of 1. For Gemini and Anthropic batch requests, temperature was set explicitly to 1. Benchmark-paper and no-augmentation conditions were repeated 30 times for each model-condition pair. Individual-paper and collection-report augmentation were repeated 5 times for each model-input pair. Predictions were averaged across repeated calls before computing performance metrics.

The repeated-call design was used because stochastic decoding can change individual predictions even under the same prompt. Averaging repeated calls reduces this run-level variation and makes the evaluation focus on the information condition rather than a single random draw. Supplementary robustness analyses should report the magnitude of run-to-run variation and show that the main conclusions are not driven by temperature-induced noise.

S5.4 Prediction parsing

For JSON prediction outputs, predictions were parsed from the question-keyed response object. Each prediction was expected to be an integer efficiency percentage with no percent sign. Parsed predictions were aligned to the 20 validation experiments by question ID before averaging across repeats and computing metrics. Responses that failed parsing or omitted required predictions should be documented in a model-by-condition parsing table.

CHECK: Add the final parse-failure counts after verifying the current batch output parser. If parse failures were zero or negligible, say so explicitly.

S6. LLM prediction results across all models and augmentation sets

S6.1 Unaugmented and benchmark-paper results

Fig. 2 reports the three main-text models. The SI should report the same no-augmentation and benchmark-paper comparison for all 8 current models, using the 30-run averaged predictions. The canonical main-text values for the three displayed models are: Claude Sonnet 4.6 baseline r = 0.664 and benchmark-paper r = 0.799; GPT-4.1 baseline r = 0.615 and benchmark-paper r = 0.758; Gemini 2.5 Pro baseline r = 0.399 and benchmark-paper r = 0.843. The benchmark-paper gain was positive for all three displayed models under paired bootstrap over the 20 validation experiments.

CHECK: The current `incremental_pgg_science_avg_prediction_metrics.csv` also contains historical models not in the current 8-model set. The all-8 SI figure should filter to the current set before reporting values.

S6.2 Individual-paper heterogeneity

Individual-paper augmentation produced substantial heterogeneity across the 2,011 papers. For Claude Sonnet 4.6, the average paper-augmented correlation was 0.657, slightly below its 30-run unaugmented baseline of 0.664, and 768 of 2,011 papers improved prediction relative to baseline. For GPT-4.1, the average was 0.586, below its baseline of 0.615, and 422 of 2,010 papers improved prediction. For Gemini 2.5 Pro, the average was 0.528, above its weak baseline of 0.399, and 1,824 of 2,011 papers improved prediction. The SI should provide the corresponding distributions for all 8 models and additional metrics beyond correlation.

S6.3 Cross-LLM agreement and convergence

Across shared individual papers, the three main-text models showed moderate agreement in paper-level augmented performance: Pearson r = 0.297 for Claude Sonnet 4.6 versus GPT-4.1, r = 0.304 for Claude Sonnet 4.6 versus Gemini 2.5 Pro, and r = 0.319 for GPT-4.1 versus Gemini 2.5 Pro. In the main text, convergence is also summarized by the reduction in absolute pairwise differences in performance after models receive the same paper. The SI should include the full pairwise agreement and convergence tables, including all current models and collection-report inputs.

CHECK: If a convergence panel is added to the main text, update this section to distinguish main-text convergence from supplementary robustness.

S6.4 Collection-report augmentation

The same qualitative pattern observed for individual papers should be reported for multi-paper reports: collection reports can move LLM predictions and sometimes improve performance, but broader aggregation does not guarantee improvement. The all-paper report is especially important because it tests whether giving the model a consolidated report over the entire broad corpus solves the paper-selection problem. In current results, the all-paper report did not consistently outperform unaugmented LLMs across models.

CHECK: Add model-specific all-paper and metadata-filter collection values from `validation_literature_collection_analysis_report_metadata_filters_summary.csv` after confirming the current 8-model filter and the 716-plus-all-paper count.

S7. Metadata models for predicting augmented performance

S7.1 Predictors and transformations

The metadata analysis predicted individual-paper augmented performance from observable paper characteristics. Predictors included empirical-paper status, publication year, journal discipline indicators, citation count, and journal impact factor. Citation counts and journal impact factors were transformed as log(1 + x). Missing citation count, journal impact factor, and publication year values were median-imputed within the modeling pipeline.

S7.2 Statistical models and cross-validation

We evaluated ordinary least squares, ridge regression, elastic net, random forest, extra trees, gradient boosting, and multilayer perceptron (MLP) models. Linear models and the MLP used standardized predictors. Model performance was evaluated with grouped 5-fold cross-validation by paper identifier so that repeated entries for the same paper did not appear in both training and held-out folds. For the main-text Fig. 4 analysis, elastic net had the strongest performance among the tested metadata models for the three displayed LLMs.

S7.3 Predictive performance

Even the best metadata model explained little held-out variation in paper-level augmented performance. For the three displayed LLMs, elastic-net cross-validated R2 was 0.007 for Claude Sonnet 4.6, 0.011 for GPT-4.1, and 0.031 for Gemini 2.5 Pro. This supports the main-text claim that coarse paper metadata provide limited guidance for identifying helpful papers before running the prediction task.

S7.4 Coefficients and feature importance

Elastic-net coefficients were estimated separately for each LLM. Coefficient intervals in Fig. 4 were obtained by bootstrapping over papers. Permutation feature importance was computed within held-out folds by permuting one feature at a time and measuring the percent increase in held-out RMSE relative to the unpermuted held-out prediction. The empirical-paper indicator was directionally negative for all three displayed LLMs and had high permutation importance for GPT-4.1 and Gemini 2.5 Pro, but the overall predictive fit remained weak.

S7.5 Supplementary robustness

The SI should report model performance across all seven statistical estimators, all 8 current LLMs, and the collection-report metadata analyses. It should also include a missing-data summary for citation counts, journal impact factor, and publication year, because median imputation only affects records with missing values.

S8. LLM-assisted empirical-design extraction and human validation

S8.1 Extraction sample

The empirical-design analysis began from the 2,011-paper broad inventory but used a separate condition-level extraction pipeline. The merged extraction workbooks covered 943 papers in the broad inventory. Under the inclusive paper-level rule used for Fig. 5, a paper counted as empirical if any workbook entry indicated `METHOD_empirical` or `METHOD_lab`. This yielded 940 empirical papers, of which 756 included at least one laboratory experiment. The laboratory-condition subset contained 3,630 condition-level records and was used for the displayed design-parameter analyses.

S8.2 Extraction model and coding rule

The main paper-level empirical status used in earlier analyses came from GPT-4.1 structured reports. The more detailed Fig. 5 design-parameter extraction used an LLM-assisted condition-level extraction procedure. The extraction prompt asked the model to identify every experiment, simulation, or observational condition described in a paper and to code design parameters, outcome measures, method type, participant information, and confidence/rationale fields. Fields were coded as not reported when the paper did not state or unambiguously imply the value; the extraction was not intended to infer missing design details from field norms.

CHECK: Confirm whether the final Fig. 5 condition-level extraction model should be stated as GPT-5.1 for all extraction workbooks, or whether one workbook was produced under an older GPT-4.1 procedure and should be documented as such.

S8.3 Condition-level extraction and post-processing

Each extracted object corresponded to a condition or treatment arm as described by the paper. For each field, the model returned a value, a short reason, and a confidence score. After extraction, project code computed paper-level counts of unique independent-variable names and dependent-variable names by taking the union across all extracted conditions for each paper. This was done programmatically rather than asking the LLM to count variables, because counts based directly on model text can confuse variable names with variable levels.

S8.4 Human validation

The extraction was validated on a random sample of 20 papers by comparing LLM judgments with three human raters. The main text currently states that agreement was at least 0.80. The SI should report the sampled-paper selection procedure, validation fields, agreement statistic, and field-specific agreement values.

CHECK: Insert the exact agreement statistic, denominator, and field list after locating the final validation file.

S9. Empirical design-space coverage analyses and robustness

S9.1 Parameter reporting

Fig. 5 Panel A used 3,630 laboratory-condition records and a 12-parameter benchmark-comparable design set. The displayed parameter set excludes reward cost and reward technology because they are defined only when reward exists. Across extracted lab conditions, the mean number of reported benchmark-comparable parameters was 6.2 and the median was 6. A total of 2,625 conditions, or 72.3%, reported 7 or fewer of the 12 displayed parameters, and 41 conditions, or 1.1%, reported all 12.

S9.2 Parameter variation versus benchmark importance

Fig. 5 Panel B compared how often each benchmark-comparable parameter varied across the empirical literature with how important the same parameter was in the benchmark prediction model. Across 756 lab papers and 12 parameters, the Pearson correlation between cross-paper variation frequency and benchmark-model predictive importance was r = -0.127 (p = 0.693). The most frequently varied parameters were game length, group size, and punishment technology. The most predictive benchmark parameters were communication, contribution framing, and contribution type.

S9.3 Parameter-value coverage

Fig. 5 Panel C compared the distribution of reported literature values with the benchmark design space. Several parameters were concentrated in narrow value ranges in the empirical literature. Examples include default contribution set to opt in, peer summaries visible, group size between 2 and 6, chat disabled, all-or-nothing contribution, and punisher or rewarder identity hidden. Mean literature evenness across the 12 displayed parameters was 0.628, compared with 0.990 in the benchmark design.

S9.4 Robustness and alternative coding

The SI should include robustness checks for alternative denominator choices, empirical-status definitions, lab-only filtering, and treatment of not-reported values. It should also include a table mapping the 14 benchmark design parameters to the 12 displayed Fig. 5 parameters, noting why reward cost and reward technology are conditionally defined and excluded from the 12-parameter comparison.

S10. Full prompts and schemas

S10.1 Structured report prompt

The structured-report prompt was stored in `literature/prompts/evidence_card_extraction_prompt.md`. It instructed GPT-4.1 to extract a JSON object from a single paper using only the paper content. The prompt defined the downstream prediction task, listed the 14 benchmark design dimensions, defined efficiency, separated payoff-based outcomes from non-payoff behavioral outcomes, and required the following top-level fields: paper type, target relevance, outcomes reported, overall effect direction on efficiency or related payoff, overall summary, paper findings, decision support, key claims, dimension-level evidence, and important limitations.

Full prompt text should be inserted here verbatim after confirming this is the final structured-report prompt used for the 2,851-paper report corpus.

CHECK: I located the current prompt file, but because prompt provenance is central to reproducibility, confirm before we paste the long verbatim prompt into the submission SI.

S10.2 Prediction prompt template

The core prediction system preamble was:

We have conducted multiple public goods game experiments with varying experimental designs, to measure the effect of punishment in cooperative settings under various environments. Your task is to predict how enabling a peer punishment mechanism to a specific game changes the efficiency compared to the same game with punishment disabled. According to our experiments, whether punishment increases efficiency or not is highly dependent on many dimensions of experiment design, and it is your job to navigate this heterogeneity and make accurate predictions.

Efficiency is the ratio between the game players' behavior and that of a fully cooperative group, i.e. a group in which all members contribute their full endowment in every round. In other words, efficiency measures how close a group's total payoff is compared to that of a group that always contributed the entire endowment and benefited maximally from the multiplier. An efficiency value of 100 means that a group earned the same amount of coins as a hypothetical group that always cooperated.

For explanation-included joint prediction requests, models were instructed to respond with a JSON object where each key was a Q-id and each value contained an explanation and an integer prediction. The user prompt began with either no additional context or an inserted literature report, followed by a 20-row validation table. The table columns were Q, control efficiency percentage, players, rounds, chat, all-or-nothing contribution, default contribution, MPCR, punishment cost, punishment technology, reward availability, reward cost, reward technology, rounds known, peer outcomes, and punisher identity.

CHECK: Insert the exact validation-table template and wrapper strings from `positive_cases/build_paper_only_new_variants_batch_input.py`, `literature/build_prediction_batch_from_card_memos.py`, and `literature/build_prediction_batch_from_collection_reports.py`.

S10.3 Collection synthesis prompt template

The collection synthesis prompt asked GPT-4.1 to write a literature analysis report synthesized across multiple academic papers for downstream prediction about punishment effects in PGG-like environments. The prompt instructed the model to use only the supplied paper-set evidence digest; synthesize across papers rather than summarize them one by one; assess PGG relevance, punishment relevance, and payoff/efficiency relevance separately; distinguish empirical findings from theory; identify which prediction dimensions were directly, indirectly, contextually, or not at all informed; preserve ambiguity and disagreement; and output Markdown sections titled Evidence Base, Task Relevance, Outcomes Measured In The Literature, Main Findings Relevant To Prediction, Prediction Guidance, Design Dimensions Highlighted Across Papers, and Important Limitations.

CHECK: Insert the full static prompt from `literature/build_collection_metadata_synthesis_batch_input.py` and note that collection identifiers and filter labels were intentionally omitted from the prompt body.

S10.4 Empirical-design extraction prompt template

The empirical-design extraction prompt instructed the model to extract every experiment, simulation, or observational condition described in a paper and to return valid JSON matching a specified schema. The schema included method indicators, benchmark design parameters, dependent variables, participant characteristics, environment, and free-text game information, with corresponding reason and confidence fields for each extracted value. The prompt required "N/R" for not reported and "N/A" for not applicable, and instructed the model not to invent information that could not be inferred from the paper.

CHECK: Insert the full schema from `batch_processing/build_batch_input.py` or the final extraction script if different. Also confirm whether the submitted SI should include the attached `Extraction_LLM.pdf` wording or the current repo script as the source of truth.

S11. Reproducibility files and code paths

The following files are current source-of-truth references for the main-text figures and should be mirrored in the reproducibility appendix: `results/paper/main_text_figures_260427/README.md`, `results/paper/main_text_figures_260427/figure_manifest.csv`, the figure-specific documentation files for Figs. 1-5, and the plotting scripts under `analysis/paper_figures/`. The SI should also include the batch-generation scripts for structured reports, individual-paper predictions, benchmark-paper predictions, collection-report predictions, metadata modeling, and empirical-design extraction.

CHECK: Before final SI drafting, organize a compact "current pipeline" manifest that separates canonical scripts from historical exploratory scripts. The repo contains older Opus, Haiku, Gemini Flash, and earlier collection workflows; without a manifest, the SI risks citing outdated paths.
