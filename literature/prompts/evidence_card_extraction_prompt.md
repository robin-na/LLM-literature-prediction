You are extracting a structured evidence card from a single academic paper for downstream synthesis about punishment effects in public-goods-game-like environments.

Read the full paper carefully. Use only the paper content. Do not invent details that are not supported by the text.

Return a JSON object only. No markdown fences. No prose before or after the JSON.

Use `N/A` for fields that do not apply by construction.
Use `N/R` for fields that the paper does not report, or that cannot be determined from the paper.

Key concepts:

- The downstream prediction task is: given the game design dimensions and the average efficiency of the control game with punishment disabled, predict the average efficiency of the same game when punishment is enabled.
- The game design dimensions used in prediction are: `player_count`, `num_rounds`, `chat`, `all_or_nothing`, `default_contrib`, `mpcr`, `punishment_cost`, `punishment_tech`, `reward_exists`, `reward_cost`, `reward_tech`, `show_n_rounds`, `show_other_summaries`, and `show_punishment_id`.
- `efficiency` means the ratio of the group’s total payoff to the total payoff of a fully cooperative group, where everyone contributes fully in every round.
- Closely related payoff-based outcomes include group payoff, total earnings, welfare, surplus, or total coins generated.
- Contribution rate, cooperation rate, punishment frequency, punishment assigned, norm compliance, and similar behavioral outcomes are not the same as efficiency or payoff. They may still be important, but they must be distinguished from payoff-based outcomes.

Classification rules:

1. Paper type hierarchy
- `paper_type_primary`: one of `theory`, `empirical`, `unclear`, `N/R`
- If `paper_type_primary != empirical`, set `paper_type_empirical` and `paper_type_experimental` to `N/A`.
- If `paper_type_primary == empirical`, set:
  - `paper_type_empirical`: one of `observational`, `experimental`, `unclear`, `N/R`
  - If `paper_type_empirical != experimental`, set `paper_type_experimental` to `N/A`.
  - If `paper_type_empirical == experimental`, set `paper_type_experimental`: one of `field_experiment`, `lab_experiment`, `other_experiment`, `unclear`, `N/R`

2. Target relevance
Assess these separately:
- `pgg_or_variant`: one of `exact`, `close`, `adjacent`, `weak`, `none`, `N/R`
- `punishment_or_sanctions`: one of `exact`, `close`, `adjacent`, `weak`, `none`, `N/R`
- `efficiency_or_related_payoff_outcome`: one of `exact`, `close`, `adjacent`, `weak`, `none`, `N/R`

Use these labels consistently:
- `exact`: directly studies the target concept
- `close`: not exact, but very similar and likely useful
- `adjacent`: related with partial transfer value
- `weak`: only loosely related
- `none`: not meaningfully related

For `efficiency_or_related_payoff_outcome`, use:
- `exact`: explicitly studies efficiency, welfare, group payoff, total earnings, surplus, or an equivalent payoff-based outcome
- `close`: studies a very similar payoff-based outcome
- `adjacent`: mainly studies contribution, cooperation, punishment, or norm compliance, with only limited payoff discussion
- `weak` or `none`: payoff-related outcomes are not meaningfully analyzed

3. Outcomes reported
- Distinguish payoff-related outcomes from non-payoff behavioral outcomes.
- If the paper’s dependent variables are things like contribution, cooperation, punishment behavior, or beliefs rather than payoff, state that explicitly.

4. Dimension evidence
- For each target dimension, provide:
  - `present`: one of `yes`, `no`, `N/R`
  - `evidence_tier`: one of `not_present`, `mention_only`, `contextual`, `informative_indirect`, `informative_direct`, `N/R`
  - `effect_direction`: one of `more_positive`, `less_positive`, `mixed`, `unclear`, `N/A`, `N/R`
  - `evidence_basis`: one of `manipulated`, `subgroup_analysis`, `correlational_pattern`, `discussion_only`, `N/A`, `N/R`
  - `notes`: string
  - `support_refs`: array of strings identifying where the support came from, such as section headings, page markers, table names, or figure names

Set `present = yes` when the paper lets you determine the value, setting, or state of the dimension, including cases where the feature is absent, disabled, continuous rather than all-or-nothing, or otherwise fixed at a known value.
Set `present = no` only when the paper does not provide enough information to determine the dimension in a meaningful way.

Interpret `effect_direction` as what the paper implies about punishment’s effect under that dimension. Use this field for dimension-level evidence. When possible, interpret it in terms of efficiency or payoff outcomes. If the paper only supports non-payoff outcomes, you may still use `effect_direction`, but say in `notes` that it is based on contribution, cooperation, punishment behavior, or another non-payoff outcome rather than payoff.

Interpretation of `evidence_tier`:
- `not_present`: the dimension is not meaningfully present in the paper
- `mention_only`: the dimension is mentioned, but not in a way that materially informs prediction
- `contextual`: the dimension provides contextual framing or mechanism discussion but weak direct predictive guidance
- `informative_indirect`: the paper provides a usable but indirect signal about the dimension
- `informative_direct`: the paper directly varies, analyzes, or strongly interprets the dimension in a way relevant to prediction

Target dimensions to assess:
- `player_count`: number of players in the game
- `num_rounds`: number of rounds
- `chat`: whether communication or chat between players is allowed
- `all_or_nothing`: whether contribution choices are all-or-nothing rather than continuous
- `default_contrib`: whether the contribution choice is framed with a default, such as opt-in vs opt-out or default keep vs default contribute
- `mpcr`: marginal per-capita return, usually multiplier divided by player count
- `punishment_cost`: cost to the punisher per unit of punishment
- `punishment_tech`: punishment impact per unit cost, or punishment effectiveness
- `reward_exists`: whether a reward mechanism is available
- `reward_cost`: cost to the rewarder per unit of reward
- `reward_tech`: reward impact per unit cost, or reward effectiveness
- `show_n_rounds`: whether players know the exact total number of rounds in advance, or otherwise know exactly when the game will end
- `show_other_summaries`: whether players are shown summary information about others’ contributions, payoffs, or related outcomes
- `show_punishment_id`: whether players can identify who punished or rewarded

Map the paper’s terminology to these dimensions when the substantive concept is equivalent, even if the exact variable name differs.

5. Key claims
- `key_claims` should contain the high-signal claims relevant to punishment, cooperation, efficiency, payoff, or moderators.
- Each claim object should include:
  - `claim`
  - `support_level`: one of `high`, `medium`, `low`, `N/R`
  - `support_refs`: array of evidence references

6. Prose fields tied to the prediction task
- `paper_findings` should describe the paper’s findings in a way that is useful for the downstream prediction task.
- `decision_support` should explain how this paper should inform prediction of treatment efficiency from the game design dimensions plus control efficiency.
- If the paper has limited relevance to the prediction task, say that and explain why in these fields.

Return exactly this top-level JSON structure:

{
  "paper_type_primary": "theory|empirical|unclear|N/R",
  "paper_type_empirical": "observational|experimental|unclear|N/A|N/R",
  "paper_type_experimental": "field_experiment|lab_experiment|other_experiment|unclear|N/A|N/R",
  "target_relevance": {
    "pgg_or_variant": "exact|close|adjacent|weak|none|N/R",
    "punishment_or_sanctions": "exact|close|adjacent|weak|none|N/R",
    "efficiency_or_related_payoff_outcome": "exact|close|adjacent|weak|none|N/R"
  },
  "outcomes_reported": {
    "primary_outcome_type": "efficiency_or_payoff|non_payoff_behavior|mixed|N/R",
    "payoff_related_outcomes": ["..."],
    "non_payoff_outcomes": ["..."],
    "notes": "..."
  },
  "overall_effect_direction_on_efficiency_or_related_payoff": "more_positive|less_positive|mixed|unclear|N/A|N/R",
  "overall_summary": "...",
  "paper_findings": "...",
  "decision_support": "...",
  "key_claims": [
    {
      "claim": "...",
      "support_level": "high|medium|low|N/R",
      "support_refs": ["..."]
    }
  ],
  "dimensions": {
    "player_count": {
      "present": "yes|no|N/R",
      "evidence_tier": "not_present|mention_only|contextual|informative_indirect|informative_direct|N/R",
      "effect_direction": "more_positive|less_positive|mixed|unclear|N/A|N/R",
      "evidence_basis": "manipulated|subgroup_analysis|correlational_pattern|discussion_only|N/A|N/R",
      "notes": "",
      "support_refs": []
    },
    "num_rounds": {},
    "chat": {},
    "all_or_nothing": {},
    "default_contrib": {},
    "mpcr": {},
    "punishment_cost": {},
    "punishment_tech": {},
    "reward_exists": {},
    "reward_cost": {},
    "reward_tech": {},
    "show_n_rounds": {},
    "show_other_summaries": {},
    "show_punishment_id": {}
  },
  "important_limitations": ["..."]
}

Consistency requirements:
- Every target dimension must be present in `dimensions`.
- If a dimension is absent, set:
  - `present = no`
  - `evidence_tier = not_present`
  - `effect_direction = N/A`
  - `evidence_basis = N/A`
  - `support_refs = []`
- If a field does not apply by construction, use `N/A`.
- If the paper does not report enough information to determine a field, use `N/R`.
- Set `overall_effect_direction_on_efficiency_or_related_payoff = N/A` when the paper does not directly analyze efficiency, payoff, welfare, surplus, or another closely related payoff-based outcome.
- Keep `overall_summary`, `paper_findings`, `decision_support`, `notes`, and `important_limitations` evidence-grounded.
