# Repeat-5 Variance And Baseline-Heterogeneity Report

## Purpose

This note documents what the literature-augmentation project is trying to
establish, what the current repeat-5 and human-comparison analyses already
show, and why the next inferential step is tricky.

The immediate goal is not to propose one final solution, but to make the
problem precise enough that it can be discussed with collaborators and used to
choose a defensible analysis strategy.

## What The Project Is Trying To Do

The broad scientific question is:

Does feeding an LLM relevant scientific literature improve its ability to
predict outcomes in the 20-question validation benchmark?

The current design has three layers:

1. Establish a baseline:
   how strong are unaugmented LLM predictions?
2. Establish an existence proof:
   if we give the model a clearly informative input, such as the benchmark
   paper report for the exact task, can prediction improve materially?
3. Study realistic augmentation:
   when the model is given individual literature reports or collection-level
   literature summaries, when does prediction improve, for which models, and
   by how much?

The augmentation conditions currently include:

- no augmentation baseline
- benchmark paper report (`benchmark_pgg_ms`)
- benchmark full paper
- individual paper analysis reports
- collection-level reports
- metadata-filtered literature collections
- all-papers collection variant

## Current Evaluation Setup

For the main repeat-5 collection analysis, the available trusted models are:

- `GPT-4.1`
- `GPT-4.1 Mini`
- `GPT-5.1`
- `GPT-5 Mini`

Each condition is repeated 5 times per model. For any condition `a`, model
`m`, and repeat `r`, we can think of the observed score as:

`S[a, m, r]`

where the score might be:

- correlation between predicted treatment outcome and true treatment outcome
- RMSE on predicted treatment outcome
- `R^2`
- correlation between predicted treatment effect and true treatment effect

The current validation task has only 20 questions, which is small enough that
all metrics can move noticeably from run to run.

## High-Level Empirical Facts Already Established

### 1. Baseline LLMs are competitive with individual humans, but not with human crowds

From the human-comparison analyses:

- On outcome correlation, pooled baseline LLM runs are better than individual
  laypeople and somewhat better than individual experts in point estimate, but
  not cleanly superior to experts.
- On RMSE, baseline LLM runs are clearly better than individual experts and
  laypeople.
- On treatment-effect correlation, baseline LLM runs are clearly better than
  individual laypeople, but not clearly better than individual experts.
- Human crowds remain stronger than baseline LLMs.

Relevant files:

- `analysis/literature_collection_analysis_reports/analyze_validation_collection_analysis_reports_repeat5_human_performance.py`
- `analysis/literature_collection_analysis_reports/analyze_validation_collection_analysis_reports_repeat5_human_rmse.py`
- `analysis/literature_collection_analysis_reports/analyze_validation_collection_analysis_reports_repeat5_human_treatment_effect_correlation.py`

Relevant outputs:

- `results/validation/literature_collection_analysis_reports_repeat5_human_performance/`
- `results/validation/literature_collection_analysis_reports_repeat5_human_rmse/`
- `results/validation/literature_collection_analysis_reports_repeat5_human_treatment_effect_correlation/`

### 2. The benchmark paper report is a real existence proof

The benchmark report materially improves baseline performance for the four
trusted models.

At the pooled repeat-run level:

- outcome correlation improves from about `0.563` to `0.784`
- RMSE improves from about `8.27` to `6.67`
- `R^2` improves from about `-0.609` to `-0.040`
- treatment-effect correlation improves from about `0.368` to `0.652`

At the crowd-style averaged-prediction level:

- outcome correlation improves from about `0.608` to `0.830`
- RMSE improves from about `7.34` to `5.88`
- treatment-effect correlation improves from about `0.482` to `0.753`

So the existence-proof claim is not limited to outcome correlation. It also
holds for RMSE, and it holds even more strongly when predictions are averaged
across runs.

Relevant files:

- `analysis/literature_collection_analysis_reports/analyze_validation_collection_analysis_reports_repeat5.py`
- `analysis/literature_collection_analysis_reports/analyze_validation_collection_analysis_reports_repeat5_model_sampling.py`

Relevant outputs:

- `results/validation/literature_collection_analysis_reports_repeat5/validation_literature_collection_analysis_report_repeat5_rows.csv`
- `results/validation/literature_collection_analysis_reports_repeat5_model_sampling/validation_literature_collection_analysis_report_repeat5_model_sampling_repeat_metric_summary.csv`

### 3. Benchmark augmentation also reduces model-driven heterogeneity

For the benchmark paper report:

- baseline outcome correlation:
  between-model SD about `0.044`, within-model repeat SD about `0.049`,
  `eta_model` about `0.43`
- benchmark outcome correlation:
  between-model SD about `0.019`, within-model repeat SD about `0.043`,
  `eta_model` about `0.15`

- baseline RMSE:
  between-model SD about `0.863`, within-model repeat SD about `0.863`,
  `eta_model` about `0.38`
- benchmark RMSE:
  between-model SD about `0.411`, within-model repeat SD about `0.775`,
  `eta_model` about `0.17`

So the benchmark report does not just raise mean performance. It also makes
performance less model-dependent.

Relevant outputs:

- `results/validation/literature_collection_analysis_reports_repeat5_model_sampling/validation_literature_collection_analysis_report_repeat5_model_sampling_repeat_metric_summary.csv`
- `plots/validation/literature_collection_analysis_reports_repeat5_model_sampling/validation_literature_collection_analysis_report_repeat5_model_sampling_summary.png`

## The Core Inferential Problem

The next step is to ask whether literature augmentation helps beyond the
benchmark existence proof. This is where the analysis becomes tricky.

There are at least two separate sources of variation:

1. Variation across models
2. Variation across repeated samples from the same model

And these two sources are not cleanly separated if all runs are simply pooled.

Formally, the score can be thought of as:

`S[a, m, r] = baseline_m + augmentation_effect[a, m] + repeat_noise[a, m, r]`

This immediately creates two problems.

### Problem 1: Repeat noise is comparable to model-to-model variation

For several metrics, especially at baseline, the run-to-run variation within a
model is similar in scale to the difference between model means.

This means that the following summary is not safe:

"Across all runs, augmentation X looks better than baseline."

That summary mixes together:

- differences caused by model identity
- differences caused by stochastic repeat noise

If those two sources are of similar magnitude, pooled run-level comparisons can
look more decisive than they really are.

### Problem 2: Baseline performance differs a lot across models

Each model starts from a different unaugmented baseline.

Examples from repeat-5 baseline:

- outcome correlation means differ noticeably across models
- RMSE means differ substantially across models
- treatment-effect correlation differs even more strongly

Because baselines differ, raw statements like:

- "many papers help model A"
- "few papers help model B"

can be misleading.

Why?

- A weaker baseline leaves more room for raw improvement.
- A model with a noisier baseline may show more apparent positive deltas by
  chance.
- A model closer to the metric ceiling, especially for correlation, has less
  room for further gain.

So counts of "papers that help" are confounded by:

- headroom
- repeat noise
- metric scale properties

## Why Simple Pooling Is Not The Right Primary Analysis

One tempting move is to pool all runs across all models and compute one grand
average augmentation effect.

That is attractive because it is simple, but it is conceptually weak for this
project.

The four models are not 20 exchangeable replicates. They differ in:

- baseline skill
- response style
- sensitivity to augmentation
- variance across repeats

Pooling all runs as if they were a single sample of interchangeable LLM draws
answers a vague question:

"On average across these model-run combinations, what happened?"

But the actual scientific question is more structured:

"Given the same augmentation input, how much does performance change for each
model relative to that model's own baseline, and how consistent is that change
across models?"

Those are different estimands.

## Why Raw Counts Of "Helpful Papers" Are Misleading

Suppose one model has a low baseline correlation and another starts higher.
Then a collection or paper may look like it "helps more often" on the weaker
model simply because:

- the weaker model has more headroom for positive deltas
- the stronger model is closer to a ceiling
- the weaker model has broader repeat-to-repeat dispersion

Similarly for RMSE:

- a higher baseline RMSE creates more absolute room for downward movement
- a lower baseline RMSE compresses the scale of possible improvement

As a result, the number of papers or collections with positive raw deltas is
not directly comparable across models.

This is especially problematic if the final narrative is supposed to say
something like:

"X kinds of literature help robustly across models."

Without baseline normalization or noise normalization, that claim is unstable.

## A More Precise Statement Of The Statistical Question

For an augmentation condition `a`, the quantity of interest should be closer to:

`effect[a, m] = mean_r S[a, m, r] - mean_r S[baseline, m, r]`

for metrics where larger is better, and the sign reversed for RMSE.

That gives a model-specific augmentation effect, always interpreted relative to
the same model's own no-augmentation baseline.

Then the cross-model question becomes:

- how large is `effect[a, m]` for each model?
- how variable is that effect across models?
- is the effect larger than ordinary repeat noise?
- is the sign of the effect consistent across models?

This reframes the target from:

"Does augmentation help, pooled across all model-runs?"

to:

"Does augmentation improve each model relative to itself, and how robust is
that improvement across the fixed set of models we evaluated?"

## Why Metric Choice Matters

The problem is not identical across metrics.

### Outcome Correlation

Pros:

- easy to understand
- benchmark report produces clear gains
- many earlier plots already use it

Cons:

- bounded above by `1`
- models with stronger baselines have less room to improve
- raw delta in correlation is not directly comparable across starting points

### RMSE

Pros:

- clearer human-comparison story for baseline
- absolute error scale is intuitive
- benchmark report improves it clearly

Cons:

- absolute deltas are not directly comparable across models with different
  baseline RMSE
- higher-RMSE models mechanically have more room for absolute improvement

### Treatment-Effect Correlation

Pros:

- closer to the causal estimand of interest
- very useful for convergence analysis

Cons:

- noisier
- only 20 questions, so correlations can be unstable
- baseline human-vs-LLM story is less favorable to LLMs than raw outcome
  correlation

The primary metric choice will therefore shape how strong the project's main
claims can be.

## What We Need To Decide

The current issue is not just technical. It is partly conceptual. The project
needs explicit answers to the following questions.

### 1. What is the primary estimand?

Options include:

- average effect across the fixed set of models
- typical within-model effect
- robustness of effect across models
- best-model effect

These are different scientific claims.

### 2. What is the unit of analysis?

Possible units:

- model-run
- model-average across repeats
- augmentation-by-model pair
- augmentation only, after pooling across models

Each choice changes the interpretation of uncertainty.

### 3. Are models fixed effects or random effects?

With only four trusted models, treating model as a fixed set may be more honest
than pretending these are random draws from a broad model population.

If models are treated as fixed:

- per-model results should be primary
- cross-model averages should be described as summaries over the evaluated
  models, not universal population estimates

### 4. What should count as "help"?

Possibilities:

- raw delta > 0
- delta larger than baseline repeat noise
- delta with a confidence interval excluding 0
- consistent top-rank performance within model

Those are not equivalent.

### 5. Which metric is primary?

A clear choice is needed among:

- outcome correlation
- RMSE
- treatment-effect correlation

If multiple metrics are co-primary, the paper should say that explicitly.

## Candidate Analysis Strategies

The following are plausible ways to address the problem. None is automatically
correct. The tradeoffs should be discussed.

### Option A: Model-First, Fixed-Effects Analysis

For each augmentation and model:

- average over the 5 repeats
- compare against that model's own averaged baseline
- report the model-specific effect

Then summarize across models using:

- mean or median effect
- range or SD across models
- sign consistency, such as `4/4` models improved

Pros:

- easy to interpret
- respects model heterogeneity
- aligns with the actual experimental design

Cons:

- only four model-level effect estimates
- less convenient for one-line significance claims

### Option B: Standardize By Each Model's Repeat Noise

Convert each model-specific augmentation effect into a noise-standardized score,
for example:

- raw delta divided by that model's baseline repeat SD
- or delta compared against a null distribution from baseline-vs-baseline
  pseudo-deltas

Pros:

- addresses the "repeat variance is comparable to model variance" problem
- makes models with different noise levels more comparable

Cons:

- adds another layer of modeling
- can be harder to explain in the paper

### Option C: Baseline-Normalized Effect Sizes

Instead of raw deltas, use baseline-adjusted scales such as:

- Fisher-z change for correlation
- percent RMSE reduction
- log RMSE ratio

Pros:

- reduces the headroom problem
- makes cross-model comparisons more interpretable

Cons:

- less directly intuitive than raw metric values
- still does not by itself solve repeat-noise issues

### Option D: Rank-Based Robustness

Within each model:

- rank all augmentations
- then examine cross-model rank consistency

Pros:

- less sensitive to absolute baseline scale
- directly answers whether the same augmentations tend to look good across
  models

Cons:

- throws away effect-size information
- a top-ranked augmentation may still have a tiny practical gain

### Option E: Hierarchical Model

Fit a model with:

- augmentation effect
- model effect
- augmentation-by-model interaction
- repeat-level residual noise

Pros:

- conceptually elegant
- directly targets the variance decomposition

Cons:

- only four trusted models
- likely fragile and over-modeled for the amount of data
- harder to explain and debug

## A Particularly Useful Diagnostic Null

One useful idea is to build a "fake augmentation" null from the baseline
repeats themselves.

For example:

- compare baseline repeat 1 to the average of baseline repeats 2 to 5
- or compare two disjoint baseline-repeat averages

This gives a no-real-augmentation distribution of apparent deltas for each
model.

That can help answer:

How large does an apparent augmentation effect need to be before it is bigger
than ordinary repeat fluctuation?

This may be a more honest threshold than simply asking whether the delta is
positive.

## What A Defensible Final Result Probably Needs

Regardless of the final strategy, the writeup likely needs to make the
following things explicit.

### Per augmentation condition

- model-specific baseline performance
- model-specific augmented performance
- model-specific effect relative to baseline
- repeat-to-repeat dispersion within model
- robustness across models

### Across models

- mean or median model-specific effect
- heterogeneity of model-specific effects
- sign consistency
- whether the benchmark existence proof behaves differently from ordinary
  literature augmentation

### Across metrics

- whether the pattern holds for outcome correlation
- whether it holds for RMSE
- whether it holds for treatment-effect correlation

## The Central Tension

The project wants to make a broad statement about literature augmentation, but
the data naturally produce model-specific answers.

That creates a tension between:

- a broad, simple claim
- an honest account of heterogeneity

If the analysis is too pooled, it risks overstating robustness.

If the analysis is too model-specific, it risks becoming fragmented and hard to
summarize.

The main unresolved task is therefore:

Choose an estimand that respects both of the following facts:

1. repeat noise is nontrivial and sometimes comparable to model-to-model
   variation
2. models start from materially different baselines, so raw gains and raw
   counts of "helpful" augmentations are not directly comparable

## Practical Discussion Questions For Collaborators

These are the main questions worth resolving before finalizing the next round
of figures and claims.

1. Should the primary analysis be model-first, with cross-model summaries only
   secondary?
2. Should "help" be defined by raw delta, baseline-normalized delta, or
   noise-standardized delta?
3. Should outcome correlation or RMSE be the primary performance metric?
4. Should treatment-effect correlation be primary for convergence claims only,
   or also for augmentation-performance claims?
5. Should cross-model robustness be expressed as average effect, rank
   consistency, sign consistency, or some combination?
6. Should the benchmark paper report be treated as a qualitative existence
   proof only, or as part of the same quantitative augmentation family as the
   literature inputs?

## Suggested Minimal Next Step

Before choosing a more elaborate statistical model, the minimal next step is
probably to create one table per augmentation family with:

- baseline mean by model
- augmented mean by model
- model-specific delta
- within-model repeat SD
- a baseline-normalized or noise-standardized effect
- sign consistency across models

That would make the problem visually concrete and should make it easier to
decide whether a more formal pooled analysis is justified.
