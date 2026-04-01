# 1) Evidence Base

The paper set comprises five research articles, with four being empirical laboratory experiments and one a theoretical study. The empirical papers predominantly use repeated multi-player games analogous to, or directly based on, the public goods game (PGG), while the theoretical work explores evolutionary games on networks with endogenous self-regulation but without explicit punishment mechanisms. The evidence base spans (a) standard linear PGGs with and without punishment, (b) variants such as all-or-nothing designs, (c) common-pool resource games with social feedback or contracts, and (d) abstracted network-based game models. The scope is moderate: the set is somewhat broad around collective action games but much narrower for precisely predicting the efficiency effect of peer punishment in canonical PGGs, as only one paper (Castillo et al., 2021) fits that target exactly. Others provide partial or adjacent evidence, emphasizing behavior or alternative sanction mechanisms, not always reporting efficiency or payoff outcomes.

# 2) Task Relevance

Each key task-relevance dimension—pgg_or_variant, punishment_or_sanctions, and efficiency_or_related_payoff_outcome—is summarized below using the required labels:

| Paper | pgg_or_variant | punishment_or_sanctions | efficiency_or_related_payoff_outcome |
|-------|---------------|------------------------|--------------------------------------|
| Castillo et al., 2021 | exact | exact (centralized) | exact |
| Windmann et al., 2021 | exact | exact (peer) | adjacent (no efficiency outcome) |
| Becchetti et al., 2018 | close (all-or-nothing PGG) | adjacent (tax/subsidy, not punishment) | adjacent (no efficiency, only cooperation) |
| Przepiorka & Diekmann, 2020 | adjacent (CPR game) | adjacent (social feedback, not monetary) | exact |
| Madeo & Mocenni, 2021 | adjacent (theoretical, networked games) | weak (no explicit punishment) | exact |

**Synthesis:**  
- **pgg_or_variant**: Only two papers (Castillo et al., Windmann et al.) run the canonical linear PGG; others use close or adjacent designs (e.g., CPR games, all-or-nothing structures, network games).
- **punishment_or_sanctions**: Only Castillo et al. and Windmann et al. implement explicit punishment in the form of centralized (manager-administered) or peer punishment, respectively. Becchetti et al. study redistribution resembling tax/subsidy, which is adjacent but not punishment. Przepiorka & Diekmann analyze social (non-monetary) feedback as sanctions. Madeo & Mocenni only weakly relate, focusing on implicit self-regulation.
- **efficiency_or_related_payoff_outcome**: Efficiency or direct group payoff is an outcome in Castillo et al., Przepiorka & Diekmann, and Madeo & Mocenni. Windmann et al. and Becchetti et al. center on behavioral (contribution/punishment) outcomes and do not report efficiency.

**Overall**: Direct evidence on peer punishment effects on group efficiency in a canonical PGG is strongly limited: only one paper speaks to it exactly, and it is in a centralized, not peer, punishment implementation.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:**  
  - **Efficiency/Total Group Payoff**: Explicitly measured in Castillo et al. (net profit in PGG with/without centralized punishment), Przepiorka & Diekmann (average group profit in CPR game), and Madeo & Mocenni (theoretical average payoff/equilibrium efficiency).  
  - **Implied Efficiency**: Becchetti et al. discuss cooperation but not directly group efficiency. Increases in cooperation are taken to imply likely higher payoff but are not quantified.

- **Non-payoff behavioral outcomes:**  
  - **Contribution Rates/Cooperation**: Becchetti et al. explicitly focus on cooperation rate shifts.
  - **Punishment Frequency/Amount**: Windmann et al. measure individuals' punishment actions in PGGs, not group payoffs.
  - **Feedback Actions/Social Ratings**: Przepiorka & Diekmann analyze the effect of public/private social feedback.

**Distinction**: Where efficiency and group payoff are directly measured, these provide relevant empirical outcomes; papers focused on behavioral responses (punishment actions, contribution rate) are of limited predictive value for efficiency unless strong links to group payoff are demonstrated.

# 4) Main Findings Relevant To Prediction

**Centralized Punishment Increases Efficiency:**
- Castillo et al. (2021) is the only study providing an exact empirical test of enabling punishment (via a central authority/manager) in a standard linear PGG. Enabling centralized punishment leads to higher group efficiency relative to control (no punishment). This effect is robust to variations in punishment cost/effectiveness and indifferent to manager selection method (random vs. democratic).

**Peer Punishment Not Directly Linked to Efficiency:**
- Windmann et al. (2021) investigate peer punishment but only measure individual punitive behavior, not efficiency or group earnings. Thus, peer punishment's efficiency effect is unassessed.

**Alternative Mechanisms for Sustaining Cooperation:**
- Becchetti et al. (2018) demonstrate that ex post tax-subsidy redistribution can stabilize higher cooperation in an all-or-nothing repeated PGG with no chat, implying—but not measuring—higher group efficiency.
- Przepiorka & Diekmann (2020) show that, in a repeated CPR game, public visibility of social feedback (not punishment) increases efficiency relative to control, whereas private feedback does not.

**Theoretical Insights on Alternatives to Punishment:**
- Madeo & Mocenni (2021) conceptually show partial cooperation can be stable and payoff-maximizing under self-regulation, but provide no insights on the effect of introducing explicit punishment.

**No Clear Evidence on Peer Punishment:**
- No direct evidence from this set on whether the typical, peer-administered punishment mechanism in repeated PGGs leads to higher efficiency, nor on possible negative effects (e.g., overspending on punishment reducing welfare).

# 5) Prediction Guidance

**Centralized (Manager) Punishment:**
- Enabling a centralized punishment institution in linear PGGs, per Castillo et al. (2021), can be expected to increase efficiency above control, regardless of tested punishment costs (within 1:1 and 3:1 fee-to-fine regimes) and manager selection mechanism. Predictors including presence/absence of centralized punishment, punishment cost/magnitude, and game baseline efficiency are informative for forecasting the treatment efficiency in these cases.

**Peer Punishment:**
- The literature set does not provide direct payoff-based evidence for peer punishment's effect on efficiency in standard multi-player PGGs. Windmann et al. suggests only that individual willingness to punish can be measured and predicted, not that it improves efficiency. Thus, predictions about efficiency gains (or losses) from enabling peer punishment cannot be grounded on this set.

**Other Sanction/Feedback Mechanisms:**
- If the game employs non-monetary sanctions (feedback, social ratings), Przepiorka & Diekmann's findings are relevant: public (visible) feedback can raise efficiency; private feedback does not.

**Alternative Mechanisms:**
- Tax/subsidy mechanisms or binding contracts (as in Becchetti et al., Przepiorka & Diekmann) can also increase efficiency but are not peer punishment per se.

**Summary**: For the downstream prediction task, only centralized punishment is directly evidenced to increase efficiency. Peer punishment effects on efficiency are not established in these papers; uncertainty must be reflected in any prediction using this set.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**
- **player_count:** Examined in all empirical setups (ranging from 4–10 players).
- **num_rounds:** All studies specify repeated games; impact on efficiency is observed in these contexts (especially decay vs. stability of cooperation).
- **mpcr:** Marginal per-capita return is consistently specified and influences baseline cooperation and effect size of interventions.
- **punishment_cost/magnitude:** Castillo et al. and Windmann et al. detail punishment cost/effectiveness; for centralized punishment, broad insensitivity to these values is found (within tested ranges).
- **all_or_nothing:** Studied in Becchetti et al. and Madeo & Mocenni; all-or-nothing versus continuous contributions can affect sanction effectiveness, but only non-payoff outcomes are reported.
- **chat:** Some studies manipulate presence/absence of communication.
- **reward_exists:** Examined in Becchetti et al. for redistribution (reward as subsidy).
- **show_n_rounds:** Przepiorka & Diekmann: players know number of rounds; some evidence this stabilizes cooperation.
- **show_other_summaries/show_punishment_id:** Public feedback about others’ choices/sanctions is studied (Przepiorka & Diekmann).

**Indirectly Informed or Contextually Discussed:**
- **default_contrib:** Not systematically varied or discussed.
- **punishment_tech:** Windmann et al. describe technical punishment parameters (e.g., 1:3 fine ratio).
- **reward_cost/magnitude/tech:** Reward mechanisms are largely absent or only appear in redistribution framing, not as peer reward.

**Effectively Missing:**
- Clarity on peer punishment versus centralized; most studies are not peer punishment.
- Systematic manipulation or reporting for **default_contrib**, **reward_cost**, **reward_magnitude**, **reward_tech**.

# 7) Important Limitations

- **Centralization of Punishment:** The only PGG efficiency finding with punishment (Castillo et al.) involves centralized, not peer, punishment. Generalizing to peer punishment is unsupported by this set.
- **Lack of Peer Punishment Efficiency Data:** No empirical paper directly tests or reports efficiency impact of peer punishment in repeated PGGs.
- **Behavioral Not Payoff Focus:** Several studies report on cooperation or punishment actions without measuring or reporting efficiency/welfare, which limits their relevance for payoff prediction.
- **Context Specificity:** Some findings (e.g., about contracts, social feedback, networked games) apply to adjacent but structurally distinct games (CPR, Stag-Hunt, Chicken), not canonical PGGs.
- **Design Gaps:** No studies manipulate or report on several prediction-relevant dimensions, such as default contributions or detailed reward implementations.
- **Ambiguity in Sanction Type:** Effects of public feedback versus monetary punishment are not easily transferable; findings on feedback/visibility (Przepiorka & Diekmann) should not be conflated with punishment effects.

**Bottom line:** This literature set provides robust guidance only for centralized punishment's positive effect on efficiency in repeated PGGs. It lacks direct evidence about peer punishment’s efficiency effect, and several design dimensions important for prediction are underexplored or missing. Caution and acknowledgment of these uncertainties are essential in downstream prediction based on this evidence.
