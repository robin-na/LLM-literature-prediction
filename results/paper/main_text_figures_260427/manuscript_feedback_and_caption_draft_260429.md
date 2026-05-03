# Manuscript Feedback And Figure Caption Drafts

This note reflects the manuscript in Google Doc tab `main` (`t.0`) as read on 2026-04-29, together with the current canonical local figure assets in `plots/paper/main_text_260427/` and their generating scripts.

## General Feedback

Overall, the paper now has a clear results arc:

1. off-the-shelf LLMs are already competitive with human crowds;
2. benchmark-aligned content can improve prediction substantially;
3. the broader literature has heterogeneous and often harmful effects;
4. simple metadata do not let us pre-filter helpful papers;
5. the empirical literature is rich but structurally misaligned with the prediction target.

That sequence reads well and feels much closer to a publishable main-text story than the earlier draft. The main issues left are mostly alignment and cleanup, not core argument.

### Highest-priority fixes

- The manuscript still points the off-the-shelf human/LLM comparison to `Fig. 1`, but the current local figure mapping places that result in `Fig. 2`. If `Fig. 1` remains the research-design schematic, those early Results references should move to `Fig. 2`.
- The current caption text in the manuscript for Figs. 2-5 is outdated relative to the canonical local figures.
  - Fig. 2 caption still says `8 LLMs`, but the current figure shows only `Claude Sonnet 4.6`, `GPT-4.1`, and `Gemini 2.5 Pro`.
  - Fig. 4 caption still describes `multivariable OLS regressions` and `717 collections`; the current figure is paper-only and uses elastic-net coefficients plus elastic-net permutation importance.
  - Fig. 5 still has only a placeholder caption.
- The Fig. 5 subsection contains duplicate material. There are currently two overlapping versions of the same paragraph block after the first two Fig. 5 paragraphs; one should be removed.
- The Fig. 5 benchmark-model placeholder should be filled with `elastic net: r = 0.773` against `noise ceiling: r = 0.777`.

### Style / flow notes

- The Results prose is now strongest when it explains why each next analysis is necessary. The Fig. 5 subsection in particular benefits from this; the current version is already moving in the right direction.
- The cross-LLM agreement result works well in the text and does not need a separate main-text figure right now. It is best used as a supporting sentence after the heterogeneity result, with an SI pointer if needed.
- In Fig. 4, the logic is good, but the caption should explicitly tell readers that Panel A and Panel B use the same elastic-net model family and answer different questions: association under the penalized fit versus reliance in out-of-sample prediction.
- In Fig. 5, it helps to keep the emphasis on `misalignment despite abundance`, not `absence of evidence`. That is already the strongest interpretive frame in the current draft.

## Figure Caption Drafts

### Figure 1

This caption is drafted against the current A-C schematic you shared, since the local `260427` figure manifest still marks Figure 1 as `lead_figure_tbd`.

**Fig. 1. Research design.** (A) Prediction benchmark from Alsobay et al. (2026): forecasters predict treatment-condition group efficiency for 20 public goods game experiments, each sampled across 14 design parameters, given the design description and the observed control-condition outcome. (B) Literature augmentation: 2,011 individual papers and 717 curated multi-paper collections were converted into prediction-focused reports. (C) Forecasting and evaluation: 8 LLMs generated predictions under no augmentation or with benchmark-paper, individual-paper, or collection-report augmentation, and performance was evaluated by the correlation between predicted and observed treatment outcomes. See Materials and Methods for prompting, report construction, and evaluation details.

### Figure 2

**Fig. 2. Benchmark-paper augmentation improves prediction beyond human crowds and off-the-shelf LLM baselines.** Bars show the Pearson correlation between predicted and observed treatment outcomes across the 20 benchmark experiments. The two upper bars are layperson and expert wisdom-of-the-crowd forecasts. For each displayed LLM, gray shows no augmentation and orange shows augmentation with the benchmark paper; LLM correlations are computed from mean predictions across 30 runs. Error bars are bootstrapped 95% confidence intervals. The dashed vertical line marks the no-treatment outcome baseline and the dotted vertical line marks the estimated noise ceiling. Asterisks compare each benchmark-augmented model with its own unaugmented baseline (`*` 95%, `**` 99%, `***` 99.9% confidence interval for the difference excludes 0). See Materials and Methods and SI Section X for details.

### Figure 3

**Fig. 3. Augmenting different papers produces highly heterogeneous effects on LLM prediction.** Panels A-C show paper-level augmented performance for `Claude Sonnet 4.6`, `GPT-4.1`, and `Gemini 2.5 Pro`. Each point is the correlation between true treatment outcomes and the model's mean prediction when augmented with one paper from the 2,011-paper corpus; papers are ordered by percentile from worst to best within model. The solid horizontal line marks unaugmented performance and the dotted horizontal line marks the estimated noise ceiling. Red points worsen prediction relative to the unaugmented model and green points improve it. The point at the far right shows the average augmented performance across papers with a 95% interval across papers. Collections and cross-LLM agreement are reported in the main text and SI.

### Figure 4

**Fig. 4. Simple paper metadata weakly predict augmented performance, although empirical papers are consistently associated with lower performance.** Panel A shows standardized coefficients from separate elastic-net models predicting paper-level augmented correlation from metadata. Points show fitted coefficients and horizontal bars show bootstrap 95% intervals. Panel B shows permutation importance from the same elastic-net models, measured as the percent increase in prediction error when each feature is shuffled; bars show standard errors across cross-validation folds. Both panels are based on individual-paper augmentation only. See Materials and Methods and SI Section X for model specification and robustness.

### Figure 5

**Fig. 5. The empirical literature provides incomplete and uneven coverage of the benchmark design space.** Panel A shows, across 3,630 extracted laboratory experiments, how many of the 12 benchmark-comparable design parameters were reported in each experiment. Panel B compares how often each parameter was varied across 756 laboratory papers with its predictive importance in the benchmark study. Panel C shows that reported parameter values are concentrated in a narrow subset of settings rather than being sampled evenly across the broader design space. See Materials and Methods and SI Section X for extraction, coding, and robustness checks.
