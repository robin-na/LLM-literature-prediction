# Predicting the Efficiency Impact of Enabling Punishment in Public Goods Games

## Abstract

The effect of peer punishment on group efficiency in Public Goods Games (PGGs) is highly context-dependent, exhibiting both substantial gains and severe losses depending on the game’s configuration. We synthesize robust evidence from a large-scale, factorial experimental design that systematically varied 14 game parameters across 360 conditions, each paired with control (punishment disabled) and treatment (punishment enabled) variants. Our analysis identifies communication, contribution framing, and their interactions with other design features as the strongest predictors of punishment’s net effect on efficiency. We detail how to use observed control efficiency and these configuration parameters to predict the likely impact of punishment, providing numerically anchored guidance grounded in experimental data.

---

## Background & Definitions

**Prediction Task:**  
Given a set of 14 game configuration parameters (**CONFIGs**) and the observed average group efficiency for a matched control game (punishment disabled), predict the average efficiency when punishment is enabled under the same conditions.

**Efficiency Metric:**  
- **Efficiency** is defined as the ratio of the group’s total payoff to the payoff under full cooperation (i.e., everyone contributes fully each round, and no costs from punishment or rewards).
    - Efficiency = 1: Maximum possible welfare.
    - Efficiency < 1: Losses due to non-cooperation and/or the costs of punishment/reward mechanisms.
The prediction target is the efficiency observed under the punishment-enabled condition, holding all other parameters constant.

---

## Data & Variables

### Experimental Design

- 360 unique configurations were created by systematically varying 14 key parameters, with each configuration run in both control and punishment-enabled forms.
- Data consists of a "learning" set (320 configurations, breadth) and a "validation" set (40 configurations, depth), jointly covering 147,618 decisions made by 7,100 participants.

### The 14 CONFIG Parameters

| Parameter                     | Description                                                                                  | Typical Values    |
|-------------------------------|---------------------------------------------------------------------------------------------|-------------------|
| CONFIG_playerCount            | Number of players per game                                                                  | 3 – 10           |
| CONFIG_numRounds              | Number of rounds (game duration)                                                            | 4 – 20           |
| CONFIG_MPCR                   | Marginal per-capita return (multiplier / playerCount)                                       | 0.2 – 0.8        |
| CONFIG_allOrNothing           | Contribution modality: 1 = all-or-nothing; 0 = variable/continuous                          | 0 / 1            |
| CONFIG_chat                   | Communication enabled (1 = yes, 0 = no)                                                     | 0 / 1            |
| CONFIG_defaultContribProp     | Contribution framing: 0 = opt-in (default keep), 1 = opt-out (default contribute)           | 0 / 1            |
| CONFIG_punishmentCost         | Cost for each unit of punishment assigned to another player                                 | 1 – 4            |
| CONFIG_punishmentMagnitude    | Number of coins deducted from a target per unit of punishment                               | 2 – 8            |
| CONFIG_showOtherSummaries     | Whether peer outcome summaries are shown after each round (1 = yes, 0 = no)                 | 0 / 1            |
| CONFIG_showNRounds            | Whether total number of rounds is disclosed to players (1 = yes, 0 = no)                    | 0 / 1            |
| CONFIG_showPunishmentId       | Whether the identity of punishers is visible to others (1 = yes, 0 = no)                    | 0 / 1            |
| CONFIG_rewardExists           | Whether reward actions are available (1 = yes, 0 = no)                                      | 0 / 1            |
| CONFIG_rewardCost             | Cost to the rewarder per unit of reward                                                     | 1 – 4            |
| CONFIG_rewardMagnitude        | Number of coins added to a target per unit of reward                                        | 2 – 8            |

**Auxiliary Variable:**  
- **Observed Control Efficiency:** Efficiency measured in the matching punishment-disabled configuration. This serves as a crucial baseline for prediction.

All parameters are experimentally manipulated under a uniform protocol and online environment; all between-condition differences are due to these CONFIG variables.

---

## Empirical Patterns: Effects of Punishment and Heterogeneity

### Main Effects

Punishment consistently increased average contributions (from ~73% to ~80% of endowment), but its effect on **group efficiency** was negative on average:

- **Learning Set:**  
    - Control (no punishment): Efficiency = **0.71**  
    - Punishment: Efficiency = **0.63**  
    - **Difference:** Δ = **-0.08** (an 11% decrease)

- **Validation Set:**  
    - Control: Efficiency = **0.72**  
    - Punishment: Efficiency = **0.68**  
    - **Difference:** Δ = **-0.04** (a 6% decrease)

However, these averages obscure striking variation. Depending on the configuration, punishment either substantially increased or drastically reduced efficiency:

- **Maximum positive effect:** +43 percentage points (Δ efficiency)
- **Maximum negative effect:** –44 percentage points (Δ efficiency)

Out-of-sample model performance was strong (R² ≈ 0.53), showing that the combined effect of several game parameters—and especially their interactions—determine whether punishment helps or harms.

### Moderators and Interactions

- **Communication (CONFIG_chat):**  
    - The strongest single moderator. Enabling chat almost always improves the efficiency impact of punishment, often making it positive; disabling chat typically makes punishment harmful.
- **Framing × Contribution Type × Visibility:**  
    - Opt-out contribution framing (default contribute) strongly helps efficiency in variable-contribution games but is neutral or harmful in all-or-nothing games—especially when peer outcome summaries are visible.
- **Game Length (CONFIG_numRounds):**  
    - Longer games enhance punishment's effectiveness, but only if communication is allowed.
- **Reward Availability (CONFIG_rewardExists):**  
    - Available rewards modestly improve the net impact of punishment.
- **MPCR:**  
    - A higher MPCR makes punishment less damaging, but its effect is modest compared to social/contextual moderators.
- **Punishment Technology (costs/magnitude):**  
    - Has surprisingly little predictive value in these studies.

Heterogeneity is robust and not attributed to procedural or sampling artifacts; all observed differences are confidently due to the manipulated parameters.

---

## Quantitative Summary

### Table 1: Average Efficiency by Feature

| Feature Set                              | Avg. Efficiency (Control) | Avg. Efficiency (Punishment) | Difference (Δ) |
|-------------------------------------------|--------------------------|------------------------------|----------------|
| All Conditions (Learning Set)             | 0.71                     | 0.63                         | -0.08          |
| All Conditions (Validation Set)           | 0.72                     | 0.68                         | -0.04          |
| Communication = ON                        | 0.75                     | 0.80                         | +0.05          |
| Communication = OFF                       | 0.70                     | 0.60                         | -0.10          |
| Variable contrib., Opt-in framing         | 0.74                     | 0.66                         | -0.08          |
| Variable contrib., Opt-out framing        | 0.75                     | 0.78                         | +0.03          |
| All-or-nothing, Peer summary visible      | 0.68                     | 0.54                         | -0.14          |

**Model outputs:**  
- Out-of-sample R² = 0.53.
- Shuffling the communication variable increases error by 60%, highlighting its dominant predictive power.

**Observed Extremes:**

- Best case: Punishment raised efficiency from 0.54 to 0.97 (+43%).
- Worst case: Punishment dropped efficiency from 0.85 to 0.48 (–44%).

--- 

## Predictive Guidance: Actionable Rules and Interactions

1. **Communication is Decisive**
    - If **CONFIG_chat = 1** and CONFIG_numRounds is moderate to long (≥8), enabling punishment is likely welfare-improving: Δ efficiency typically between **+0.03 to +0.15**.
    - If **CONFIG_chat = 0**, punishment almost always reduces efficiency: Δ efficiency **–0.05 to –0.20**.

2. **Framing × Contribution Type**
    - **Variable contributions + opt-out framing** (CONFIG_defaultContribProp = 1, CONFIG_allOrNothing = 0): Punishment often improves or preserves efficiency (**+0.03 to +0.10**).
    - **All-or-nothing contributions:** Adding punishment is risky, especially with visible peer summaries—large negative impacts possible (**–0.14 or worse**).

3. **Peer Outcome Visibility**
    - When both all-or-nothing contributions (CONFIG_allOrNothing = 1) and peer outcomes are visible (CONFIG_showOtherSummaries = 1): Expect substantial efficiency losses if punishment is enabled.

4. **Reward Availability**
    - Rewards (CONFIG_rewardExists = 1) slightly hedge against punishment’s downsides: efficiency reductions are mitigated, Δ efficiency **+0.02 to +0.05** relative to otherwise similar cases.

5. **MPCR Effects**
    - Higher MPCR (toward 0.8) is associated with less harm (sometimes slight benefit) from punishment, but this is secondary to the above factors.

6. **Control Efficiency**
    - When observed control efficiency is already **high** (>0.9), there is little or no benefit to adding punishment, and it often hurts efficiency.
    - When control efficiency is **low** (<0.6), the potential for improvement is greatest if communication and pro-social framing are present.

### Numeric Ranges: Key Scenario Effects

| Scenario                                    | Δ Efficiency (Punish – Control)    | Notes                                               |
|----------------------------------------------|------------------------------------|-----------------------------------------------------|
| Chat ON, opt-out, variable contribution      | +0.03 to +0.15                     | Positive, especially in longer games                |
| Chat OFF, all-or-nothing, outcome visible    | –0.10 to –0.44                     | Large negative effects; avoid using punishment      |
| Other configurations                        | –0.02 to +0.05                     | Small, mixed effects; calibrate by control outcome  |

**Strong nonlinearities and interactions are present; additive approaches are likely to underfit.**

---

## Limitations & Open Questions

- **Population and Setting:**  
  All data come from a single controlled online platform; generalization to other populations, contexts, or time horizons should be made cautiously.
- **Unmodeled Variables:**  
  Factors outside the 14 CONFIGs—such as participant experience or group composition—could matter in real-world scenarios, though these were controlled in the experiment.
- **Dependence on Control Efficiency:**  
  Prediction depends on an accurate control (no-punishment) efficiency estimate; if that is poorly measured or projected, the final treatment prediction will be less reliable.
- **Temporal Horizon:**  
  Findings relate to the span of the experimental games; very long-term or repeated real-world contexts may yield different results.

---

## How To Use This For Predictions

- **Collect** all 14 CONFIG parameters (see above) and the observed or projected *efficiency with punishment disabled*.
- **First, check communication (CONFIG_chat):**
    - If enabled (1): Adding punishment is likely to increase or at least preserve efficiency, especially in longer games or with opt-out framing.
    - If disabled (0): Adding punishment will likely reduce efficiency, sometimes substantially.
- **Consider framing and contribution type:**
    - Opt-out framing + variable/continuous contribution increases the chances of positive welfare effects from punishment.
    - All-or-nothing contributions, especially with visible peer outcomes, signal a high risk of negative efficiency impacts if punishment is enabled.
- **Game length matters only if chat is enabled**: Longer games amplify positive effects of punishment with chat, otherwise effect is weak.
- **If rewards are enabled (CONFIG_rewardExists = 1):** Slightly improves efficiency outcomes with punishment.
- **Anchor the treatment prediction to control efficiency:**
    - If control efficiency is high (>0.9): Little or negative effect from punishment.
    - If control efficiency is low (<0.6): Greatest potential for gain from punishment, but only if pro-social features (chat, opt-out, variable contributions) are present.
- **Expect strong feature interactions:** Avoid relying on simple additive models. Apply the above rules to account for key interactions.
- **Avoid overemphasis on punishment mechanics (costs/magnitude):** In this dataset, social context far outweighs the direct mechanical punishment variables for predicting efficiency change.
- **When uncertain**, default to predicting a modest reduction (Δ efficiency ≈ –0.05) from enabling punishment, unless chat and pro-social cues are present.

---

This report provides empirically grounded, data-driven guidance for predicting efficiency outcomes when enabling punishment in PGGs, enabling systematic, configuration-sensitive modeling in new experimental or applied contexts.
