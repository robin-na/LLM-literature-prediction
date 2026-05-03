# Paper Figure Narrative

Last updated: 2026-03-31

This folder documents the current main-text figure set for the paper draft. It is meant to answer two questions:

1. What is each figure trying to say?
2. What is the intended paper-ready interpretation, including the main caveats?

For exact derivations, inputs, scripts, and output paths, see [figure_derivations.md](./figure_derivations.md).

## Current Figure Story

The current figure sequence supports the following narrative:

- Off-the-shelf LLMs, even without literature augmentation, are competitive with individual human forecasters.
- A highly informative, target-matched benchmark report can materially improve prediction performance.
- Ordinary literature augmentation is heterogeneous: some papers and collections help, others hurt, and most of the action is not captured by a single global "literature helps" or "literature does not help" claim.
- Which papers or collections help is only partly aligned across models, with collections more robust than individual papers.
- Metadata is only weakly informative for individual papers, but more informative for collections.
- The collection story is structured enough that a small number of metadata dimensions explain a nontrivial part of the variation.

## Figure 1

**Question**

How good are baseline LLMs, before any literature is added, relative to human forecasters?

**What the panel shows**

- A CDF of individual layperson and expert outcome-correlation scores.
- One vertical line for each no-augmentation LLM.
- One vertical line for the "no treatment effect" reference predictor.

**Intended message**

- Baseline LLMs are competitive with individual human forecasters.
- Stronger models such as `GPT-4.1 Mini` and `GPT-5.1` outperform most individual humans.
- Some weaker models are only modestly better than the "no treatment effect" reference.

**Important caveat**

This figure compares LLMs to individual humans, not to human crowds. Human crowds still perform better than baseline LLMs.

## Figure 2

**Question**

Can a clearly informative, target-matched external input improve prediction?

**What the panel shows**

- For each model, no augmentation and benchmark-paper augmentation are shown side by side.
- Error bars show uncertainty in the raw correlation across the 20 validation designs.
- Brackets summarize whether the paired benchmark-minus-baseline correlation difference excludes zero at increasingly strict paired-CI thresholds.

**Intended message**

- The benchmark paper report is an existence proof that informative augmentation can help.
- The improvement is visible in five of the six models.
- This motivates the later question: if one highly informative source helps, what happens when we feed in many ordinary papers or filtered collections from the literature?

**Important caveat**

`GPT-4.1 Nano` is the exception, and later figures focus on the five-model set excluding it. That exclusion should be presented as a follow-on analytic focus, not as if the nano result did not exist.

## Figure 3

**Question**

What happens when we augment the model with one individual paper at a time?

**What the panel shows**

- For each of five models, a density over the correlations obtained by augmenting with each of the 2011 individual papers.
- A dashed line for no augmentation.
- A dotted line for the benchmark paper.
- A solid line for the average augmented-paper performance.

**Intended message**

- Individual-paper augmentation is highly heterogeneous.
- Some papers help, some hurt, and many are close to no augmentation.
- The benchmark paper is unusual relative to the broad single-paper literature distribution.

**Important caveat**

This figure is about the distribution of augmented performance over papers, not a claim that most papers help.

## Figure 4

**Question**

What happens when we augment the model with filtered collections of papers?

**What the panel shows**

- The same density-style summary as Figure 3, but over metadata-filtered literature collections instead of single papers.

**Intended message**

- Collections are also heterogeneous.
- The collection distribution is more structured than the single-paper distribution.
- This is the first hint that collection composition may be meaningfully predictable from metadata.

## Figure 5

**Question**

Are the same papers or collections helpful across models?

**What the panel shows**

- Pairwise model-by-model heatmaps of raw Spearman rank correlation in paper usefulness and collection usefulness.
- Matching heatmaps of a normalized rank correlation that divides the observed Spearman correlation by a repeat-based within-model reliability ceiling.

**Intended message**

- Cross-model agreement is not negligible, but it is far from perfect.
- Agreement is weaker for individual papers and stronger for collections.
- Some of the disagreement is attributable to repeat-level noise, but not all of it.

**How to phrase it**

- Individual papers: weak-to-moderate cross-model alignment.
- Collections: moderate cross-model alignment.

## Figure 6

**Question**

Can metadata alone predict how well an augmented paper or collection will perform?

**What the panel shows**

- Grouped-CV `R^2` and grouped-CV Spearman for metadata-only supervised prediction.
- Separate bars for individual papers and collections.
- Within-model results for the five-model set.

**Intended message**

- Metadata has weak predictive signal for individual papers.
- Metadata has a noticeably stronger, though still imperfect, predictive signal for collections.

**Important caveat**

This figure currently uses raw augmented `correlation`, not `delta_correlation`. So the safest wording is that metadata somewhat predicts augmented performance, not strictly that metadata predicts improvement over no augmentation.

## Figure 7

**Question**

Which metadata dimensions are associated with paper-level usefulness?

**What the panel shows**

- Standardized ridge coefficients on `correlation gain` for individual papers.
- One point estimate and interval per model for the same set of metadata features.

**Intended message**

- The individual-paper metadata signal is weak and fairly brittle.
- The clearest repeated negative association is that empirical papers tend to reduce correlation gain.
- Journal impact factor is mildly positive in some models, but the paper-level story is much noisier than the collection-level story.

**Important caveat**

These are predictive associations from a ridge model, not causal effects.

## Figure 8

**Question**

Which collection metadata dimensions matter most, and in what direction?

**What the panel shows**

- A permutation-importance bar chart for collection metadata.
- A SHAP beeswarm summary in the same feature order.
- The main-text panel currently uses `GPT-4.1`, where the best-performing collection predictor is `Extra Trees`.

**Intended message**

- The collection story is more structured and more predictable than the individual-paper story.
- The most important collection features are the number of papers, empirical share, citation, and discipline mix, with journal impact factor also contributing.
- The SHAP panel shows directionality and heterogeneity of those effects rather than only their rank order.

**Important caveat**

The main-text panel is a single-model illustration chosen because it is the clearest and strongest predictive case. Matching panels for the other models belong in the supplement.

## Narrative Guardrails

These are the claims the figure set supports well:

- Baseline LLMs are competitive with individual humans.
- Informative augmentation can help.
- Ordinary literature augmentation is heterogeneous.
- Collections are more structured and more cross-model robust than individual papers.
- Metadata is somewhat useful for predicting performance, especially for collections.

These are claims the current figure set does **not** support cleanly:

- "Most papers help."
- "Most papers hurt."
- "Metadata fully explains what helps."
- "The same papers help every model."
- "Figure 6 proves which papers improve relative to baseline."

## Parked / Exploratory Variants

These exist in the repo but are not the current primary figure versions:

- Figure 3 CDF variant. The density version is the active one.
- Adjusted-correlation figure set in `plots/paper/main_text_adjusted_correlation/`. This was kept separate because the adjusted metric distorted the human comparison in Figure 1.
