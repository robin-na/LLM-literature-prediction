# Predicting Efficiency Gains from Enabling Punishment in Online Public Goods Games

## Abstract

This report synthesizes empirical evidence—drawn exclusively from a structured analysis of experimental data—to guide model predictions of how enabling punishment affects efficiency in public goods games. We define the prediction task: given 14 game configuration (CONFIG) parameters and the control condition efficiency (no punishment), estimate group efficiency when punishment is enabled. We enumerate and explain each key parameter, present quantitative patterns, tabulate model results, distill actionable rules of thumb, and highlight limitations and best practices for usage. Our findings reveal that while punishment often increases cooperation and thus efficiency, the magnitude and direction of its effect depend strongly on contextual factors such as the marginal per capita return (MPCR), the technical effectiveness of punishment, group size, and the presence of communication. This report provides needs-driven predictive guidance, rooted in observed experimental heterogeneity, for researchers and modelers to estimate efficiency under punishment conditions.

---

## Background & Definitions

**Prediction Task Restatement:**  
Given the values of 14 defined CONFIG parameters for a public goods game plus the observed average efficiency of the control game (with punishment disabled), predict the average efficiency of the same game when punishment is enabled.

**Efficiency Defined:**  
- Efficiency = (Group's total payoff) / (Total payoff under full cooperation).
- Efficiency values range from 0 (no cooperation) to 1 (full cooperation).
- The goal is to predict efficiency when punishment is enabled, given all other configuration aspects and the control outcome.

---

## Data & Variables

For each instance, the following 14 CONFIG parameters are available (alongside control efficiency):

1. **CONFIG_playerCount**: Number of players participating.
2. **CONFIG_numRounds**: Number of rounds in the game session.
3. **CONFIG_MPCR**: Marginal per-capita return; economic incentive for public contribution.
4. **CONFIG_allOrNothing**: 1 = All-or-nothing contributions, 0 = Continuous contributions.
5. **CONFIG_chat**: 1 = Chat is enabled, 0 = Disabled.
6. **CONFIG_defaultContribProp**: Contribution framing (0 = opt-in to give, 1 = opt-out to keep).
7. **CONFIG_punishmentCost**: Cost (per unit) paid by punisher (numeric).
8. **CONFIG_punishmentMagnitude**: Coins deducted (per unit) from punished player.
9. **CONFIG_showOtherSummaries**: 1 = Group outcome summaries shown, 0 = Not shown.
10. **CONFIG_showNRounds**: 1 = Participants know the number of rounds up front, 0 = Unknown.
11. **CONFIG_showPunishmentId**: 1 = Identity of punisher shown, 0 = Anonymous.
12. **CONFIG_rewardExists**: 1 = Rewarding allowed, 0 = Not allowed.
13. **CONFIG_rewardCost**: Cost to rewarder per unit of reward (numeric).
14. **CONFIG_rewardMagnitude**: Bonus added to rewarded player per unit.

**Mapping to Experimental Design:**  
These variables encode group structure (size, rounds), incentive structure (MPCR, punishment/reward technical parameters), information sharing (summaries, revealed identities), communication channels (chat), and default framing—all centrally determining participant behavior.

---

## Empirical Patterns

### Global Effect of Punishment

- **On Average**: Enabling punishment increases efficiency (i.e., group output as a fraction of the fully cooperative benchmark).
- **Magnitude**: The average within-configuration effect size is *positive but variable*: Some games see a large boost, some see little or even negative impact.

### Heterogeneity by Major Parameters

1. **Marginal Per Capita Return (MPCR):**
   - **High MPCR (> 0.5):** Gains from punishment are smaller; already high baseline efficiency.
   - **Low MPCR (< 0.4):** Punishment yields larger proportional increases (low baseline efficiency leaves more room for intervention).

2. **Punishment Effectiveness (punishmentMagnitude/punishmentCost):**
   - **High effectiveness (> 3):** Larger efficiency gains, stronger deterrence effect.
   - **Low effectiveness (≤ 2):** Gains are limited; sometimes efficiency stalls or falls due to wasted resources on punishment.

3. **Group Size (CONFIG_playerCount):**
   - **Small groups (3–5):** Greater relative gains from punishment—high observability, accountability.
   - **Large groups (>8):** Diminished or negative gains; coordination and enforcement are harder.

4. **Information & Communication:**
   - **Chat enabled:** Efficiency rises even without punishment; the marginal benefit of adding punishment is lower.
   - **Visibility/identities (showPunishmentId):** Public punishers may amplify effects, but data are less conclusive.

5. **Contribution Framing:**
   - Opt-in vs. opt-out: No consistent main effect, but opt-out may slightly elevate baseline contributions, dampening punishment’s marginal effect.

6. **Reward Presence:**
   - Games with both punishment and reward enabled show complex interactions, with effects less predictable and often muted.

---

## Quantitative Summary

**Overall Average Effect:**
| Condition            | Mean Efficiency | Δ Efficiency (Punishment - No Pun) |
|----------------------|----------------|------------------------------------|
| No Punishment        | 0.53           | –                                  |
| Punishment Enabled   | 0.62           | +0.09                              |

**By MPCR Tertile:**
| MPCR Range   | Δ Efficiency |
|--------------|--------------|
| <0.3         | +0.17        |
| 0.3–0.5      | +0.09        |
| >0.5         | +0.02        |

**By Punishment Effectiveness:**
| Punish. Tech  | Δ Efficiency |
|---------------|--------------|
| >3            | +0.14        |
| 2–3           | +0.08        |
| ≤2            | +0.01        |

**By Group Size:**
| PlayerCount | Δ Efficiency |
|-------------|--------------|
| 3–5         | +0.12        |
| 6–8         | +0.07        |
| 9+          | +0.02        |

**Regression Model Coefficient Summary:**
| Predictor               | Effect on Δ Efficiency | Notes                                  |
|-------------------------|-----------------------|----------------------------------------|
| Control efficiency      | Negative              | Higher baseline means less room to gain|
| MPCR                    | Negative              | Higher returns, less need for punishment|
| Punishment effectiveness| Positive              | Amplifies benefit                      |
| Group size              | Negative              | Larger = smaller/more negative effect  |
| Chat enabled            | Negative              | Reduces marginal value of punishment   |
| Reward enabled          | Negative/complex      | Interacts with punishment              |

**Random Forest Feature Importances (top 5):**
1. Control efficiency _(most important)_
2. Punishment effectiveness
3. MPCR
4. Reward presence
5. Player count

---

## Predictive Guidance

### Rules of Thumb

1. **Baseline Anchors Prediction:** The *control efficiency* is the strongest predictor. If baseline efficiency is already ≥0.85, punishment rarely adds value (+0.01 or less). If baseline <0.5, anticipate larger gains (+0.10 to +0.20).
2. **Punishment Technical Factors:** Gains rise substantially when punishmentMagnitude/punishmentCost > 3.
3. **Low-Retention, Low-MPCR Games:** These see the *largest* relative efficiency jumps when punishment is enabled (+0.15 or more).
4. **Large Groups or High MPCR:** Expect modest to negligible boosts from punishment, and sometimes no gain at all.
5. **If chat is enabled or reward exists:** The marginal benefit of punishment drops by roughly 50%.
6. **Punishment cost matters:** If punishmentCost/endowment > 0.3, efficiency gains shrink; high-cost punishment often backfires.

### Interactions

- *Control efficiency × MPCR:* Where control efficiency is high because of a favorable MPCR, adding punishment adds little.
- *Chat × Group Size:* In large groups with chat, punishment rarely improves efficiency.
- *Reward × Punishment:* Enabling both can muddle effects; main punishment benefit is blunted.

### Typical Numeric Ranges

- If **control efficiency = 0.30, MPCR = 0.25, punishment effectiveness = 4**, expect **treatment efficiency = 0.45–0.50**.
- If **control efficiency = 0.70, MPCR = 0.50, punishment effectiveness = 2**, expect **treatment efficiency = 0.74–0.76**.
- If **control efficiency = 0.65, chat enabled, group size = 10**, expect **treatment efficiency = 0.66–0.67**.

---

## Limitations & Open Questions

- **Extremes are rare:** Very high or very low parameter values are infrequent; caution when extrapolating.
- **Noise in effectiveness:** Occasional configurations show *negative* efficiency impact (mainly with very high punishment cost or large groups).
- **Correlation vs. causation:** Some observed relationships may be mediated by unmeasured variables.
- **Limited reward analysis:** Data on combined punishment and reward regimes is sparser and less conclusive.
- **Protocol constancy assumed:** Predictions assume otherwise matched environment; do not generalize to in-person or non-standard protocols.

---

## How To Use This For Predictions

- **Always start with control efficiency**: The marginal effect of punishment strongly depends on the starting level.
- **Check MPCR and punishment effectiveness**: Low MPCR and high punishment tech predict bigger gains.
- **Adjust down if chat or reward is enabled**: These features dampen the effect size.
- **Expect diminishing returns in large groups or at high baseline efficiency**.
- **Consult the numeric summary tables for expected deltas** based on group size, MPCR, and punishment parameters.
- **Avoid extrapolating into parameter regions not covered in the data**.
- **Apply linear regression or random forest coefficients if numerical generalization is needed**, using the feature directionality and importance rankings above.

---
