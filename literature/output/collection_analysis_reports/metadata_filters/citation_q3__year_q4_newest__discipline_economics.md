# 1) Evidence Base

The paper set consists of two empirical studies, both reporting findings from experimental designs—one a laboratory experiment (Zhou, X. Y., et al., 2023) and one a field experiment (Zhou, Y. X., et al., 2022). Both use variants of the standard Public Goods Game (PGG) with explicit punishment conditions, providing high contextual validity for the downstream prediction task (predicting the effect of enabling peer punishment in a PGG-like environment). The studies are methodologically robust, with well-documented design parameters.

However, the evidence base is narrow for the specific prediction task: both papers focus mainly on behavioral outcomes, especially contribution rates, and neither directly reports efficiency or payoff-based outcomes (such as group payoff or welfare). Their findings are therefore adjacent to, but not directly on, the efficiency outcomes central to the prediction task.

# 2) Task Relevance

**pgg_or_variant**:  
- **Relevance**: exact  
Both studies use the standard repeated or one-shot public goods game framework. This aligns perfectly with the prediction context, as the design dimensions match the PGG paradigm.

**punishment_or_sanctions**:
- **Relevance**: exact  
Both studies implement punishment mechanisms (either peer/“endogenous” or externally imposed/“exogenous”), either as an experimental treatment or comparative condition.

**efficiency_or_related_payoff_outcome**:
- **Relevance**: adjacent  
Neither paper provides direct empirical evidence for efficiency or group payoff (total earnings, welfare, etc.), the central variable for prediction. Instead, both report on contribution levels, which are theoretically linked but not equivalent to efficiency. Punishment’s effect on efficiency is not directly observable in the results, and must be inferred indirectly from behavioral changes.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes**:  
- **Absent**: Neither paper reports efficiency, group payoff, surplus, or any other aggregate payoff data specifically.

**Non-payoff (behavioral) outcomes**:  
- **Primary**: Both studies focus on contribution rates (how much is contributed to the group account) and punishment actions (how often, and to whom, punishment is assigned).

**Consequences**:  
- The measured outcomes provide strong evidence about how punishment changes contribution behavior, but do not conclusively indicate whether those behavioral changes result in net efficiency gains, due to the potentially substantial cost of punishment that could offset contribution increases.

# 4) Main Findings Relevant To Prediction

**Empirical findings**:
- **Punishment increases contributions**: Both studies robustly show that enabling punishment (peer- or third-party) increases contribution rates in the game, with the effect sometimes varying by cultural background (Zhou, X. Y., et al., 2023) or parental migration status (Zhou, Y. X., et al., 2022).
- **Moderating factors**:  
  - *Cultural background*: Rice-farming communities are more likely to punish and contribute, especially when punishment is allowed (Zhou, X. Y., et al., 2023).
  - *Developmental and social context*: Children’s cooperation increases with age; paternal migration reduces cooperation; exogenous punishment can offset social deficits in cooperation (Zhou, Y. X., et al., 2022).
- **Type of punishment**: Exogenous punishment is found to be more effective at raising contributions than endogenous punishment (Zhou, Y. X., et al., 2022), but evidence again speaks to contributions, not directly to efficiency.

**Theoretical/mechanism arguments**:
- The effect of punishment on contribution is presumed to translate into efficiency gains, but this is not demonstrated empirically due to lack of payoff reporting.

**Ambiguities**:
- Without payoff data, it is unclear if increased contributions after punishment intervention always result in higher group efficiency, especially given punishment costs.

# 5) Prediction Guidance

This literature set provides strong evidence that enabling punishment mechanisms increases contribution behavior in repeated or one-shot PGGs across both adult and child populations, and in both laboratory and field environments. This effect is robust to variations in social context, cultural background, and punishment implementation (peer vs. exogenous).

**For predicting efficiency (the downstream outcome):**
- Because efficiency is not directly measured, predictions must extrapolate from the robust finding that punishment reliably increases contributions.
- If contribution increases more than punishment costs (i.e., the cost of administering punishment is less than the value of extra contributions), efficiency likely rises; otherwise, it could remain flat or even decrease (a classic issue in PGG-with-punishment literature not documented here).
- The empirical evidence in this set does not permit a quantitative mapping from “contribution increase” to “efficiency increase,” but suggests that at minimum, punishment interventions are expected to move efficiency in a positive direction in environments where baseline cooperation is low.

**Caution**: Prediction must account for the missing data about the net payoff impact of punishment (i.e., cost-benefit tradeoff). It is reasonable (but unconfirmed) to expect that where punishment induces substantial increases in contribution (particularly when baseline is low), efficiency will also rise, but this remains an inference rather than a demonstrated outcome in the current evidence base.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed**:
- `player_count`, `num_rounds`, `chat`, `all_or_nothing`, `mpcr`, `punishment_cost`
  - Game structural parameters are explicitly reported and manipulated; evidence for their relevance in moderating punishment effects on contribution behavior is provided.

**Indirectly or contextually discussed**:
- `punishment_tech` (implementation is varied: endogenous/peer vs. exogenous/third-party; studied in Zhou, Y. X., et al., 2022)
- `default_contrib` (not specified—status is unknown, but typical PGG framing likely applies)
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id` (not specified; status unknown)
- `reward_exists`, `reward_cost`, `reward_tech` (not present/discussed)
- `all_or_nothing` (studied both with and without all-or-nothing framing; status varies)

**Effectively missing**:
- `default_contrib`, `reward_exists`, `reward_cost`, `reward_tech`, `reward_magnitude`, `show_n_rounds`, `show_other_summaries`, `show_punishment_id` are not directly discussed or varied, so there is no evidence about their direct influence on the payoff/effectiveness of punishment for efficiency.

# 7) Important Limitations

- **No efficiency or payoff data**: Both papers fail to report on group efficiency, earnings, or welfare, the primary outcomes for the prediction task. All inferences about efficiency must be made indirectly from contribution changes, without confirmation that these translate to net payoff gains after accounting for punishment costs.
- **Uncertainty about punishment costs**: Without explicit data on the scale of costs incurred by punishers, the overall impact on group surplus is speculative.
- **Limited design dimension coverage**: Several prediction-relevant design features (reward systems, information structures, and some framing variables) are unexamined in this evidence base.
- **Specific populations/contexts**: Findings are drawn from Chinese children (field, Zhou, Y. X., et al., 2022) and Chinese adults with different agricultural backgrounds (lab, Zhou, X. Y., et al., 2023), which may limit generalizability to other populations or settings.
- **Lack of heterogeneity analysis**: Although some moderators are examined (e.g., culture, age, social context), many plausible moderators (MPCR, punishment cost levels) are not systematically varied or analyzed for impact on efficiency.

**Summary judgment**:  
The literature base provides precise, high-quality evidence about the effect of punishment on contribution rates, but only adjacent and indirect insight for predicting changes in efficiency or overall group payoffs—the central variable for the downstream prediction task. This gap should be addressed with caution in practical predictive modeling.
