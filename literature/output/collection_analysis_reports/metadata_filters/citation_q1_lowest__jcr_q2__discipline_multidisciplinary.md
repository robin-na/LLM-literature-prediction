# 1) Evidence Base

This paper set consists of three papers: one experimental/empirical study and two theoretical/simulation works. The empirical paper (Liao et al., 2021) uses a laboratory threshold public goods game (PGG) with an automatic third-party punishment mechanism. The other two are agent-based simulation or theoretical analyses (Szilagyi & Somogyi, 2010; Johnson, 2023) of N-person games and spatial prisoner's dilemma, respectively. The set is narrow in terms of directly addressing the prediction of efficiency in PGGs with versus without punishment, as only one paper (Liao et al., 2021) deals with both punishment and (adjacent) payoff outcomes in a PGG-variant setting. The remaining papers are adjacent or weak in relevance to the downstream prediction task, focusing on cooperation rates rather than efficiency and omitting punishment mechanisms.

# 2) Task Relevance

**pgg_or_variant**:
- **Exact:** Only Liao et al. (2021) uses a PGG-variant (threshold PGG).
- **Adjacent:** Szilagyi & Somogyi (2010) and Johnson (2023) study N-person games with externalities or spatial prisoner’s dilemma—both adjacent to but not the same as the standard PGG.

**punishment_or_sanctions**:
- **Exact:** Liao et al. (2021) experimentally manipulates punishment, specifically third-party (automatic) punishment.
- **Adjacent/None:** Szilagyi & Somogyi (2010) mentions no explicit punishment or reward; Johnson (2023) includes no punishment at all.

**efficiency_or_related_payoff_outcome**:
- **Adjacent:** Liao et al. (2021) focuses on non-payoff behavioral outcomes (investment rates, success rates of cooperation), but does relate these to group success and thus indirectly to efficiency.
- **None/Adjacent:** Szilagyi & Somogyi (2010) and Johnson (2023) do *not* report group payoff, efficiency, or closely related outcomes (total earnings, welfare, surplus).

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:**
  - Liao et al. (2021): Measures *success rate of cooperation* (fraction of groups reaching the investment threshold). While not labeled as "efficiency," this is adjacent, as higher success roughly aligns with higher group payoff in threshold PGGs.
  - Theoretical studies (Szilagyi & Somogyi, 2010; Johnson, 2023): Do *not* report group payoff, efficiency, total earnings, or other direct payoff-based outcomes.

- **Non-payoff behavioral outcomes:**
  - Liao et al. (2021): Primary outcomes are *individual and group investment rates* (i.e., contribution rates, a behavioral metric).
  - Szilagyi & Somogyi (2010) and Johnson (2023): Focus exclusively on the *proportion of cooperators*, spatial patterns of cooperation, and emergence or stabilization of cooperation/clusters.

Overall, only weak or adjacent evidence is provided for payoff-related outcomes relevant to predicting efficiency. The majority of measured outcomes are behavioral rather than direct payoff/efficiency metrics.

# 4) Main Findings Relevant To Prediction

- **Punishment Mechanisms:**
  - *Empirical evidence (Liao et al., 2021):* Introducing a third-party automatic punishment mechanism in a threshold PGG **substantially increases the rate at which groups achieve the public good threshold** (an increase from ~56% to ~77%). This effect is attributed to higher average resource investments per individual, as punishment deters free-riding and incentivizes higher contributions.
  - The mechanism is *automatic, impersonal*, and does not require player communication.

- **Behavioral vs. Efficiency Measures:**
  - The improved *success rate* in Liao et al. (2021) suggests (but does not directly quantify) higher group efficiency, as more groups attain the efficient outcome (public good provided).
  - The actual ratio of total group earnings to the fully cooperative maximum ("efficiency") is not explicitly reported, leaving some ambiguity about the size of payoff gains relative to the cost of punishment incurred.

- **Absence of Informative Comparisons:**
  - The theoretical/simulation studies (Szilagyi & Somogyi, 2010; Johnson, 2023) provide no information about the effects of punishment or sanctions on payoff-based group efficiency.

- **Ambiguity and Context:**
  - Liao et al. (2021) relates *only* to small groups (n=3) under a threshold structure with automatic punishment. It is unclear if findings generalize to other PGG forms, punishment types (peer-to-peer, voluntary), or group sizes.

# 5) Prediction Guidance

- **Supported Guidance:**
  - **Enabling an automatic third-party punishment mechanism in small-group, threshold PGG settings should lead to *higher* efficiency or group payoffs compared to a control without punishment** (Liao et al., 2021). This guidance is strongest when the control-game efficiency is substantially below maximum (i.e., many groups failing to achieve the threshold).

- **Interpretation Notes:**
  - The literature most directly supports a positive effect of punishment on efficiency when: group size is small (n=3), the PGG is threshold-based, punishment is automatic (not peer-assigned), and communication is *not* present.

- **Uncertainty:**
  - The precise *magnitude* of efficiency gain is not known, as only success rates and investment rates are reported (not total payoffs minus incurred punishment costs).
  - Predictions to other contexts (larger groups, voluntary/peer punishment, continuous contributions) are not supported by this literature.

- **Other design dimensions (chat, reward, visibility, contribution framing, etc.):** No evidence found to inform directional prediction across these, except that chat was *not* enabled in the only relevant experiment.

# 6) Design Dimensions Highlighted Across Papers

- **Directly informed:**
  - *player_count*: n=3 tested (Liao et al., 2021; also adopted in simulations).
  - *num_rounds*: Multiple rounds, but precise comparative findings limited.
  - *all_or_nothing*: Some degree of all-or-nothing or threshold structure in Liao et al. (2021).
  - *mpcr*: Included in Liao et al. (2021) threshold setup; simulation papers also consider marginal returns.
  - *punishment_cost*: Key manipulated treatment in Liao et al. (2021).

- **Indirectly informed:**
  - *chat*: Liao et al. (2021) confirms chat *not* present; implication is effect of punishment is tested in isolation.
  - *default_contrib*: Not addressed.
  - *punishment_tech*: Automatic, impersonal third-party punishment in Liao et al. (2021) only.
  - *reward_exists/cost/tech*: Not present or discussed.

- **Contextually discussed:**
  - Theoretical work explores variety of game structures (payoff shape, local/global interactions) (Szilagyi & Somogyi, 2010; Johnson, 2023), but *without* direct connection to punishment or efficiency outcomes.

- **Effectively missing:**
  - *show_n_rounds, show_other_summaries, show_punishment_id*: Not addressed.
  - *reward dimensions*: Not informed.
  - *peer vs. third-party punishment distinction*: Only third-party, automatic type is included.

# 7) Important Limitations

- **Scarcity of Efficiency Data:** No paper provides a direct measurement of "efficiency" as the ratio of actual to maximum possible group payoffs. Liao et al. (2021) offers only adjacent outcomes (success rates, investment rates) and does not net out the cost of punishment when estimating welfare.

- **Narrow Context:** The only empirical evidence is from a threshold PGG with small groups, automatic third-party punishment, and no communication. This is a narrow slice of possible design dimensions.

- **Lack of Punishment Variation:** No evidence on peer-assigned or voluntary punishment, combinations with reward, or the impact of other design elements such as chat, information visibility, or contribution framing.

- **Adjacency of Simulation Results:** The theoretical/simulation papers, while exploring relevant behavioral dynamics, do not analyze standard PGGs, efficiency, or punishment effects, and therefore cannot robustly inform the downstream prediction task.

- **Retraction Notice:** The main empirical paper (Liao et al., 2021) is marked as retracted, potentially limiting its reliability.

- **Ambiguity About Cost of Punishment:** Even where behavioral outcomes improve (cooperation rates, group investment), it is not clear if net payoff (group welfare after accounting for punishment costs) rises.

- **Limited Generalization:** Predictions cannot be extended with confidence to larger groups, regular linear PGGs, games with peer/voluntary sanctioning, or other manipulation of the design dimensions due to lack of coverage.

---

**In summary:**  
This literature set provides limited, mainly context-specific empirical support for predicting efficiency gains from enabling (automatic, third-party) punishment in small-group, threshold PGGs. Most design dimensions and other PGG contexts are missing or only weakly informed, and the efficiency metric itself is not directly reported. Given these constraints, predictions should be cautious and restricted to closely matching experimental circumstances.
