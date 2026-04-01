# 1) Evidence Base

The paper set consists entirely of **theoretical papers** (no empirical or experimental papers), focusing on evolutionary game theory models applied to public goods games (PGGs) and closely related environments (e.g., multi-player snowdrift, prisoner's dilemma variants, resource and innovation games). The set is **narrow** in directly modeling PGGs with punishment and efficiency as the outcome, but is **broad** in the diversity of mechanisms—covering peer vs. institutional punishment, conditional and probabilistic schemes, exclusion, mobility, corruption, reward systems, and various population structures.

Many papers report on **strategy dynamics, cooperation rates, evolutionary stable states, or prevalence of behavioral strategies**, with a smaller subset explicitly reporting **payoff-based outcomes (group payoff, welfare, efficiency)**. Notably, evidence for directly predicting the quantitative change in efficiency from enabling punishment in PGGs, conditional on design dimensions, is mostly **theoretical and mechanistic rather than data-driven or empirical**.

# 2) Task Relevance

- **pgg_or_variant**: The majority of the set is **exactly relevant** to PGGs or direct variants, but a substantial proportion examines adjacent games (Prisoner's Dilemma, threshold goods, innovation races).
    - Label: **exact/close** across critical mass.
- **punishment_or_sanctions**: Most studies are **exactly relevant**—explicitly modeling the introduction, parameterization, and impact of punishment or sanctioning mechanisms.
    - Label: **exact/close**, with some studies addressing exclusion (close/adjacent) or reward (adjacent).
- **efficiency_or_related_payoff_outcome**: Roughly one-third report **efficiency/group payoff** directly; others report **closely related** (e.g., welfare) or **adjacent** (e.g., cooperation rate) outcomes; several only present non-payoff behavioral dynamics.
    - Label: **exact** for a core, **close/adjacent/weak** for a significant remainder.

### Summary Table

| Relevance Dimension        | Label        | Comments                                                    |
|---------------------------|-------------|-------------------------------------------------------------|
| pgg_or_variant            | exact/close | Most models are PGGs, some are variants or adjacent games   |
| punishment_or_sanctions   | exact/close | Directly model punishment/sanctions; some exclusion/reward   |
| efficiency_or_payoff      | exact/close | Many model payoff/efficiency, but some only behavior         |

# 3) Outcomes Measured In The Literature

- **Payoff-based outcomes** (efficiency, group payoff, welfare, surplus):
    - Directly reported in a significant but minority subset (e.g., Salahshour, 2021; García & Traulsen, 2012, 2019; Wang et al., 2024; Hetzer & Sornette, 2013; Ohdaira, 2022; Han, 2022; Han et al., 2024).
    - Some models treat efficiency as the **stationary mean payoff or the evolutionary stable group payoff**.
    - Others provide only **qualitative** or **relative** payoff outcomes (e.g., higher/lower than control), not exact efficiency ratios.

- **Non-payoff behavioral outcomes**:
    - Predominate outside the above: cooperation/contribution rates, prevalence of punishment strategies, probability of reaching cooperative equilibrium, and frequency of defectors or punishers.
    - Exclusion, norm conformity, prevalence of fairness, and social learning outcomes also frequently reported.

- **Key distinction**: In many "mixed" or "adjacent" papers, **cooperation rates are assumed (not shown) to map onto payoff/efficiency outcomes**; however, effects on efficiency can differ due to the costs of punishment (Han et al., 2024).

# 4) Main Findings Relevant To Prediction

### General Pattern
- **Enabling punishment** in PGG(-like) environments often, but not always, **raises efficiency**, especially when:
    - Punishment is **effective** (i.e., deters defection for a low cost),
    - The marginal per-capita return (MPCR) is **high**,
    - The punishment cost is **neither too high nor too low** (optimal intermediate values),
    - There is **no or limited antisocial punishment/corruption** (Salahshour, 2021; Wang et al., 2024; García & Traulsen, 2019; Hetzer & Sornette, 2013).

- **Negative or neutral effects** can occur when:
    - **Punishment cost is too high:** Not enough incentive to punish, defectors persist, lower efficiency.
    - **Punishment cost is too low or poorly targeted:** Antisocial punishment, norm confusion, or cycles of hostility can lower mean group payoff (Salahshour, 2021; Han et al., 2024; Lee et al., 2019).
    - **Corruption** or the **ability to buy one's way out of punishment** renders the system exploitable, reducing efficiency (Lee et al., 2019; Abdallah et al., 2014).
    - **Conditionality/thresholds** for punishment are set too high, making coordinated punishment rare and defectors dominant (Huang et al., 2018).
    - **Population structure** prevents peer punishment from gaining traction (Wang et al., 2024; Shimao & Nakamaru, 2013).

- **Mechanism design nuances** (e.g., probabilistic punishment, punishment tied to payoff differences) can yield **higher efficiency than standard fixed-cost schemes** (Ohdaira, 2022, 2016).

- **Institutional and observability design**: Efficiency gains from punishment are strongest when **institutions are observable** and conditional strategies are available (García & Traulsen, 2019).

- **Nontrivial mapping from behavior to efficiency**: In several papers, *increased cooperation via punishment does not always translate to higher efficiency* due to costs incurred by punishers and possibility of antisocial/second-order punishment (Han et al., 2024; Stewart et al., 2016; Helbing et al., 2014).

### Key Empirical Claims (Theory-based)
- **Efficiency effects are parameter-sensitive** and can be mapped to specific critical thresholds (Wang et al., 2024).
- **Reward mechanisms** often outperform punishment on efficiency, even if both increase cooperation (Han et al., 2024; Han, 2022; Pal & Hilbe, 2022).
- **Hybrid and adaptive mechanisms** (peer punishment combined with centralized or probabilistic schemes) can mitigate negative side-effects (Abdallah et al., 2014; Ohdaira, 2022).
- **Context of game structure** (optional participation, exclusion, commitment stages) qualitatively changes punishment's effectiveness and the efficiency outcome.

# 5) Prediction Guidance

- **Prediction of efficiency change** from control (no punishment) to treatment (punishment enabled) should be **conditional** on:
    - **MPCR (mpcr):** Higher MPCR increases the likelihood that punishment boosts efficiency. If MPCR is too low, punishment may have minimal or negative effects.
    - **Punishment cost (punishment_cost):** Predict a positive efficiency effect only at moderate punishment costs; too high deters use, too low may induce antisocial punishment or instability.
    - **Punishment effectiveness (punishment_tech/punishment_magnitude):** High deterrence via impactful punishment is necessary for large efficiency gains.
    - **Player count (player_count):** Smaller groups show stronger positive effects of punishment on efficiency (Gao et al., 2015); very large groups may dilute the effect unless institutionally reinforced.
    - **Population/game structure:** Structured populations (regular graphs, spatial lattices) with local interaction and information support more favorable efficiency effects from punishment than well-mixed or random groups.
    - **Observability (show_punishment_id, show_other_summaries):** If institutions and punishers are visible/identifiable, efficiency gains are more likely (García & Traulsen, 2019).
    - **Exclusion/corruption possibilities:** If institutional corruption or antisocial punishment is feasible, or exclusion is delayed/expensive, *efficiency gains from punishment may be attenuated or reversed* (Lee et al., 2019; Abdallah et al., 2014).
    - **Adaptive/conditional punishment designs** (probabilistic, contingent, threshold-based): These often outperform standard punishment in both deterring defection and minimizing cost (Ohdaira, 2022; Huang et al., 2018).

- **Control game efficiency** is a strong baseline: Where baseline efficiency is already high (i.e., high cooperation without punishment), the room for improvement is limited; where baseline efficiency is low, the potential for efficiency increase from enabling punishment is greater, but only if critical thresholds in the above dimensions are met.

- **Do **not** infer large positive efficiency changes from punishment-enabled designs where punishment is expensive, poorly targeted, the payoff structure is unfavorable (low MPCR), or institutional corruption is possible.**

- **Qualitative and mechanistic guidance** is strong; quantitative effect size predictions are not directly provided by these papers.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed (widely modeled, critical for prediction):**
- `player_count`
- `num_rounds`
- `mpcr`
- `all_or_nothing`
- `punishment_cost`
- `punishment_tech` (effectiveness/magnitude)
- `reward_exists`, `reward_cost`, `reward_tech` (in reward-focused or hybrid papers)

**Indirectly Informed:**
- `default_contrib` (contribution framing occasionally discussed)
- `chat` (rarely discussed, typically absent in theoretical models)
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id` (only some models address observability or information; these moderators are highlighted mainly in institutional punishment models)

**Contextually Discussed or Sparse:**
- `reward_exists`, `reward_cost`, `reward_tech` (only in subset focusing on reward/competition between positive/negative incentives)
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id` (information structure effects underexplored)

**Effectively Missing:**
- **Few to none** of the theoretical models address chat/communication, real-time human interaction, or endogenously evolving game rules. Most ignore practicalities of experimental implementation (no discussion of software, identity protection, etc.).

# 7) Important Limitations

- **Lack of empirical calibration**: All findings are theoretical; no direct experimental effect sizes or variance estimates. Application to real-world or experimental settings requires caution and may require empirical correction.
- **Payoff outcomes often inferred, not calculated**: Many models use behavior as a proxy for efficiency, assuming monotonic mapping that may not always hold (due to cost of punishment, antisocial actions, or structural features).
- **Limited coverage of experimental design dimensions**: Information dimensions (summaries, revealed identities), communication, and framing are infrequently modeled.
- **Sensitivity to mechanisms and parameters**: The efficiency effect of punishment is highly conditional on parameter regime (MPCR, cost, effectiveness) and social-environmental context (structure, observability, corruption possibility).
- **Scope/transfer issues**: Some highly relevant structural findings (thresholds for punishment impact, effect of population structure) do not readily map to all possible prediction scenarios.
- **Special cases and exceptions**: Reward mechanisms often outperform punishment for efficiency; hybrid or adaptive mechanisms are under-explored in their generalizability; the dynamics of antisocial punishment, corruption, or over-regulation can sharply reduce or reverse predicted efficiency gains.
- **No quantitative estimates**: Guidance for how much efficiency will increase (i.e., numerical prediction) is not supplied; only qualitative direction (likely to increase/decrease) and mechanism-based thresholds.

---

**In summary**: This theory-heavy literature set provides strong mechanistic and qualitative guidance for when enabling punishment in a PGG-like game is likely to increase efficiency, highlighting critical dependence on key design dimensions such as punishment cost/effectiveness, MPCR, group size, and institutional structure. However, quantitative predictions require caution, as the models prioritize behaviors and mechanisms over empirical effect sizes and often leave key implementation dimensions underexplored.
