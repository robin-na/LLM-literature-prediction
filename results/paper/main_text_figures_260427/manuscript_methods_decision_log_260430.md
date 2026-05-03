# Manuscript methods decision log, 2026-04-30

Working document: Google Doc `LLM PGG Literature`, main tab `t.0`.

## Operating rules for manuscript editing

- Do not directly edit the Google Doc unless the user explicitly asks for direct edits in the current turn.
- Treat user cuts and rewrites as intentional. Do not silently restore older wording or previous assistant drafts; if a removed point seems important, raise it outside the document and ask before reintroducing it.
- For manuscript prose passes, read from the top before diagnosing a section so that Methods, Results, and pointers do not become redundant or fragmented.
- Avoid database-oriented terms such as `row` in main-text prose unless discussing a data file directly; prefer reader-facing terms such as `experimental condition`, `treatment arm`, `extracted condition`, or `paper-condition observation` depending on context.

## Materials and Methods scope

- Keep the PNAS main-text Materials and Methods under 1,000 words.
- Avoid repeating the Study Overview. The benchmark setup and evaluation logic are already described there, so the Methods should focus on implementation details not already stated in the main text.
- Remove the standalone `Prediction benchmark` paragraph from Methods.
- Remove the standalone `Evaluation` paragraph from Methods. Keep repeat averaging and temperature details in the LLM prediction-procedure paragraph; route bootstrap details and alternative metrics to SI.

## Current model set

- Use 8 models total: GPT-4.1, GPT-4.1 Mini, GPT-4.1 Nano, GPT-5.1, GPT-5 Mini, GPT-5 Nano, Claude Sonnet 4.6, and Gemini 2.5 Pro.
- Main text reports 3 models: Claude Sonnet 4.6, GPT-4.1, and Gemini 2.5 Pro.
- Do not describe older Opus, Haiku, or Gemini Flash runs as part of the current model set.

## Repeat and temperature details

- Fig. 2 benchmark/no-augmentation conditions use 30 repeated calls per model-condition pair, averaged before evaluation.
- Individual-paper and collection-report augmentation use 5 repeated calls per model-input pair, averaged before evaluation.
- OpenAI prediction requests leave temperature unspecified and therefore use the API default of 1; Gemini and Anthropic batch requests explicitly set temperature to 1.
- Structured report generation from full texts uses GPT-4.1 with temperature 0.
- Main-text Methods now states that prediction calls used temperature 1.0 and keeps replicate variability details routed to the SI.
- Main-text Methods now explicitly states that predictions were averaged across repeated calls before computing predictive performance.

## Fig. 4 metadata-model details

- Main-text Methods now clarifies that citation counts and journal impact factors are log(1 + x)-transformed.
- Missing values in citation count, journal impact factor, and publication year are median-imputed within the modeling pipeline.
- The statistical-model list now uses `multilayer perceptron (MLP)` instead of the generic wording `neural network`.
- The main-text Methods paragraph no longer describes collection-level metadata averaging, because Fig. 4 is individual-paper only; collection details should stay in the SI.
- Main-text Methods now states that the Fig. 4 elastic-net coefficient intervals are bootstrapped over papers and that feature importance is computed by held-out-fold permutation as percent RMSE increase.

## Corpus accounting checked locally

- Current October 2025 WoS metadata file: `PGG_papers/WoS_251031_fileInfo.csv`.
- This file has 2,960 English records.
- Of these, 2,756 have `file_path` and `custom_id`, indicating full-text PDFs/markdown available for processing.
- The parsed structured-report table is `literature/output/evidence_cards/literature_evidence_cards_cleaned/papers.csv`.
- It contains 2,851 successfully parsed records.
- All 2,756 full-text records from the October 2025 WoS metadata file are present in the structured-report table.
- The structured-report table contains 95 additional records not in the October 2025 WoS metadata file; these come from previously collected markdown files in the project corpus, including `PGG_MS_202502`.
- Broad relevance screening yields 2,012 records in `literature/output/evidence_cards/literature_evidence_cards_cleaned/eligibility/sets/broad_support_all_types.csv`.
- The final individual-paper main-analysis corpus has 2,011 papers after excluding `PGG_MS_202502`.

## Reader-facing terminology

- Use `structured, prediction-focused report` or `structured report`, not `evidence card`, in the manuscript.
- Explain that the structured reports are the same report objects introduced in Study Overview: they summarize study type, task relevance, outcomes, punishment-related findings, design-dimension coverage, and limitations for prediction.
- Keep internal screen labels such as `exact`, `close`, and `adjacent` in the SI.
- In the main text, describe the relevance screen in plain terms: retained papers had potential relevance to a PGG or related social-dilemma setting, punishment or sanctioning, and efficiency/welfare/payoff or a closely related outcome, and discussed at least one benchmark design dimension in a way that could inform prediction.

## Corpus-screen clarification after Fig. 5 check

- The 2,011-paper set is the broad main-analysis prediction-augmentation inventory, not the narrower empirical-design subset used in Fig. 5.
- The broad inventory comes from `broad_support_all_types` after excluding `PGG_MS_202502`; this screen permits adjacent relevance to the benchmark concepts and includes both empirical and theoretical papers.
- The stricter structured-report screens are much smaller: `strict_predictive_all_types` has 490 records; `strict_predictive_empirical_payoff` has 243 records before excluding the benchmark manuscript.
- Fig. 5 starts from the 2,011-paper broad inventory but then uses extraction workbooks filtered to papers in that inventory. The workbook merge covers 943 of the 2,011 papers; 940 are empirical under the inclusive workbook rule (`METHOD_empirical` or `METHOD_lab`), 756 have at least one lab row, and these 756 lab papers / 3,630 lab-condition rows drive the displayed design-parameter analyses.
- Main-text Methods should therefore describe the broad screen conservatively and then separately describe the Fig. 5 empirical-design subset. Avoid implying that all 2,011 papers directly report benchmark-like lab PGG efficiency evidence.

## Methods revision reset after rereading from top

- The Study Overview already explains the benchmark, PGG setup, structured-report idea, correlation metric, bootstrap intuition, noise ceiling, and figure flow. The Materials and Methods should not restate these motivations except where a reproducible implementation detail is needed.
- The current Methods has duplicated corpus prose: a broad 2,851/2,011 structured-report paragraph followed by an older `n=1,398` binary-screen paragraph. The `n=1,398` paragraph appears inconsistent with the current 2,011-paper main-analysis inventory and should be removed or moved to SI only if it describes a superseded/auxiliary screen.
- The 2,011 inventory should be described as derived from the 2,851 full-text structured-report set. A concise chain is: 2,960 English WoS metadata records; 2,756 full texts accessible and converted; plus 95 previously collected project full texts; 2,851 structured reports; broad relevance screen gives 2,012 records; excluding `PGG_MS_202502` leaves 2,011.
- Main-text Methods should emphasize reproducibility knobs: WoS source and full-text conversion, structured-report model/prompt/temperature, eligibility screen at a high level, construction of single-paper and collection augmentations, model set and repetition scheme, prediction format/parsing, metadata-model implementation, and empirical-design extraction sample.
- Anything already argued in Results should not be repeated: why benchmark-paper augmentation is a best-case diagnostic, why empirical papers are surprising, why Fig. 5 motivates misalignment. Methods can name the samples and variables, but the interpretation belongs in Results/Discussion.

## Source of the 95 additional structured-report full texts

- The structured-report batch used the cleaned markdown inventory in `paper_collection/papers_markdown_cleaned/`, not only rows with nonempty `file_path` in `PGG_papers/WoS_251031_fileInfo.csv`.
- After normalizing away the `.md` suffix in WoS `custom_id`, the current October 2025 WoS file contains 2,756 full-text rows with `file_path` and `custom_id`; the structured-report table contains those 2,756 plus 95 additional cleaned markdown files.
- A DOI-only reconciliation was too conservative. Using WoS UT identifiers where available plus exact normalized title matching against all 2,960 October 2025 WoS metadata records, 40 of the 95 additional files match the October 2025 metadata but lack a full-text `file_path`/`custom_id` in `PGG_papers/WoS_251031_fileInfo.csv`.
- Of those 40 October-metadata matches, 35 match by stronger metadata identifiers/composites (UT, DOI, or title+source+year) and 5 match only by exact normalized title.
- The remaining 55 additional files do not match the October 2025 2,960 metadata records under this multi-identifier check. Most trace to older WoS/corpus files, especially `paper_collection/WoS_241106_fileInfo.xlsx`, `paper_collection/WoS_coop_punishment_241009_1500_updated_241101.xlsx`, and/or `paper_collection/WoS_eligible_241106.csv`.
- After backtracking `10.1109_access.2020.3029458`, only 3 of the 95 are currently traceable in the repo only to pre-existing markdown files and the cleaned markdown summary: `10.1080_2153599x.2022.2065345`, `10.1177_147470491000800105`, and `PGG_MS_202502`.
- Of the 95 additional files, 56 survive the broad relevance screen and are included in the 2,011-paper prediction-augmentation inventory.

## Origin check for the 55 not matched to October 2025 metadata

- A follow-up reconciliation file was written to `results/paper/main_text_figures_260427/extra_55_not_in_oct2025_metadata_origin_reconciliation.csv`.
- Of the 55 additional files that do not match the October 2025 2,960 metadata records, 52 exist in older WoS/corpus records and 3 are only traceable to pre-existing markdown files in this repo.
- Source pattern among the 52 older-record files:
  - 25 appear in both `paper_collection/WoS_241106_fileInfo.xlsx` and `paper_collection/WoS_coop_punishment_241009_1500_updated_241101.xlsx`.
  - 19 appear in those two older files plus `paper_collection/WoS_eligible_241106.csv`.
  - 4 appear only in `paper_collection/WoS_241106_fileInfo.xlsx`.
  - 2 appear only in `paper_collection/WoS_eligible_241106.csv`.
  - 2 appear in `paper_collection/WoS_241106_fileInfo.xlsx` and `paper_collection/WoS_eligible_241106.csv`.
- Of these 55 files, 26 enter the final 2,011-paper `broad_all` inventory, and all 26 have older WoS/corpus records after backtracking `10.1109_access.2020.3029458`.
- The 3 markdown-only files among the 55 are `10.1080_2153599x.2022.2065345`, `10.1177_147470491000800105`, and `PGG_MS_202502`; none are in `broad_all`.
- `10.1109_access.2020.3029458` is not markdown-only. It appears in `paper_collection/WoS_241106_fileInfo.xlsx`, `paper_collection/WoS_coop_punishment_241009_1500_updated_241101.xlsx`, and `paper_collection/WoS_241106.enl` with DOI `10.1109/ACCESS.2020.3029458`, WoS accession `WOS:000583568700001`, and PDF path `paper_collection/WoS_241106.Data/PDF/1154073370/10.1109_access.2020.3029458.pdf`.

## Metadata diagnostic for older-only records

- Diagnostic files were written to `results/paper/main_text_figures_260427/extra_55_old_record_metadata_diagnostics.csv` and `results/paper/main_text_figures_260427/extra_26_broad_all_old_record_metadata_diagnostics.csv`.
- The older-only records do not appear to be a simple language/document-type error. Among the 26 older-only records that enter the final 2,011-paper `broad_all` inventory, all 26 are English journal articles in the older WoS/corpus metadata.
- The 26 older-only `broad_all` records also have no obvious visible document-type/language exclusion flag in the old record spreadsheets. Fourteen were in `paper_collection/WoS_eligible_241106.csv`, and all 14 had `cooperation=True` and `punishment=True`.
- Relative to the October 2025 2,960-record metadata set, the older-only records are enriched for broader adjacent literatures rather than clean benchmark-like PGG studies: religion/moralizing gods, evolutionary cooperation, game-theory or simulation, legal/social exchange, and non-PGG punishment/cooperation tasks.
- Full old metadata text fields show that the 26 older-only `broad_all` records mostly still match a broad cooperation-plus-punishment/sanction topic query: 26/26 mention cooperation in title/abstract/keywords, 25/26 mention punishment or sanctions, and 25/26 mention both. But only 5/26 mention public goods and 5/26 mention social dilemma.
- The most plausible explanation is therefore not an obvious spreadsheet filtering mistake, but a difference in WoS record/query behavior between the older and October 2025 collections, possibly because citation-topic/category/index labels or other WoS-side filters changed. A secondary issue is that the structured-report screen was broad enough to retain some adjacent older records.

## Empirical-design extraction wording

- Main-text Methods now distinguishes paper-level empirical status from the later extraction task: empirical status is described as coming from the GPT-4.1 structured reports, while GPT-5.1 is described as extracting additional Fig. 5 information not directly available in WoS metadata.
- GPT-5.1 extraction is now described as experimental-condition-level extraction.
- The main text now states the non-inference rule: fields were coded as not reported when the paper did not state or unambiguously imply the value.
- Human validation wording was tightened to `judgments`; the live manuscript currently states `agreement ... was at least 0.80`.
- The LLM-extraction citation sentence was softened to say that recent evaluations suggest LLMs can support structured extraction from scientific texts, rather than claiming broad strong capability.

## Oct. 2025 spreadsheet subset check

- `paper_collection/WoS_251031.xls` was parsed directly and has 2,960 rows and 72 columns. It is the spreadsheet counterpart to the October 2025 record export, distinct from `WoS_251031_fileInfo.csv`.
- `10.1109_access.2020.3029458` does not appear in `paper_collection/WoS_251031.xls` by DOI fragment `3029458`, exact DOI `10.1109/ACCESS.2020.3029458`, WoS accession `WOS:000583568700001`, title, or `Online Car-Hailing` text.
- The final 2,011-paper `broad_all` set is therefore not strictly a subset of the 2,960 October 2025 spreadsheet. Current reconciliation: 1,955 records match October 2025 full-text rows with `custom_id`; 30 additional records match October 2025 metadata but lacked `file_path`/`custom_id` in `WoS_251031_fileInfo.csv`; and 26 records trace only to older WoS/corpus records.
- If the main-text Methods needs a clean one-line chain from the October 2025 search, use the subset count `1,985` for records in the 2,011 set that match the October 2025 metadata, or describe the analyzed full-text corpus as the October 2025 full-text set plus retained full texts from an earlier version of the same WoS search/corpus. Do not write that all 2,011 are simply "out of" the 2,960 October 2025 records unless the 26 older-only records are excluded or otherwise handled.

## Combined-search corpus accounting

- The earlier WoS search spreadsheet `paper_collection/WoS_241106.xls` has 2,765 rows. The October 2025 WoS search spreadsheet `paper_collection/WoS_251031.xls` has 2,960 rows.
- Deduplicating the two search exports by WoS accession, DOI, then title/source/year gives 3,087 unique records: 2,632 records are shared by the two searches, 131 are earlier-search-only, and 324 are October-2025-only.
- The older `paper_collection/WoS_coop_punishment_241009_1500_updated_241101.xlsx` spreadsheet is subsumed by the `WoS_241106.xls` search for this deduplicated union; adding it does not change the 3,087 unique-record count.
- Full-text availability by file-info tables: `paper_collection/WoS_241106_fileInfo.xlsx` has 1,259 rows with `file_path`; `paper_collection/WoS_251031_fileInfo.csv` has 2,756 rows with `file_path` and `custom_id`. The deduplicated full-text union across the old and current file-info sources contains 2,844 unique metadata records, plus retained markdown files that explain the processed-report count.
- The structured-report corpus has 2,851 parsed full-text documents. Of these, 2,848 match a record in the combined WoS search universe and 3 are retained markdown-only documents (`10.1080_2153599x.2022.2065345`, `10.1177_147470491000800105`, and `PGG_MS_202502`). None of the two non-benchmark markdown-only documents enter the final 2,011-paper `broad_all` set, and `PGG_MS_202502` is explicitly excluded.
- Suggested Methods chain: two WoS search rounds returned 3,087 unique records; full texts were obtained or retained for 2,851 documents and converted to structured reports; GPT-4.1 broad relevance screening retained 2,012 records; excluding the benchmark manuscript left 2,011 papers for the main literature-augmentation analyses.
