# Collection Switch Sets

This folder stores the paper-set CSVs used for collection-level literature
augmentation experiments.

How the sets were built:

- Source universe:
  - `eligibility/sets/broad_support_all_types.csv`
  - interpreted through `papers.csv`
- Builder:
  - `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/literature/build_collection_switch_sets.py`
- Hard exclusion:
  - `PGG_MS_202502` is excluded from all collection sets in this folder

The three binary switches are:

- `A`
  - require both:
    - `relevance_pgg_or_variant in {exact, close}`
    - `relevance_punishment_or_sanctions in {exact, close}`
- `B`
  - require the paper to report a payoff-like primary outcome:
    - `outcomes_primary_outcome_type in {efficiency_or_payoff, mixed}`
- `C`
  - require `paper_type_primary == empirical`

Current agreed collection sets:

- `broad_all`
- `broad_empirical`
- `broad_payoff_like`
- `broad_empirical_payoff_like`
- `exactclose_pggpun`
- `exactclose_pggpun_empirical`
- `exactclose_pggpun_payoff_like`
- `exactclose_empirical_payoff`

Main files:

- `collection_switch_sets_summary.csv`
  - one row per agreed collection set, including switch settings, count, and
    set CSV path
- `collection_switch_sets_summary.json`
  - metadata summary including:
    - excluded ids
    - broad-universe count
    - remaining-broad count
- `sets/*.csv`
  - one-column `custom_id` CSV for each collection set
- `sets/broad_all_remaining_after_exactclose_empirical_payoff.csv`
  - the remaining broad individual-paper set used to extend the original
    strict single-paper augmentation run

Current counts:

- `broad_all`: `2011`
- `broad_empirical`: `947`
- `broad_payoff_like`: `874`
- `broad_empirical_payoff_like`: `409`
- `exactclose_pggpun`: `866`
- `exactclose_pggpun_empirical`: `440`
- `exactclose_pggpun_payoff_like`: `432`
- `exactclose_empirical_payoff`: `242`

These are the collection-set manifests used downstream by the collection
synthesis scripts.
