# Prediction Rules for Estimating the Effect of Enabling Punishment on Efficiency in New Public Goods Games

## Abstract

This rule-based operational report provides guidance for predicting average efficiency in public goods games when punishment is enabled, given 14 configuration parameters and observed control efficiency. Drawing on large-scale experimental evidence (147,618 decisions; 360 configurations), these rules prioritize context interactions over single-parameter effects. Key predictors are ranked, and numerical heuristics define directions and ranges of predicted efficiency shifts. Communication, contribution framing, peer visibility, and game length dominate as moderators; punishment technical strength is weakly predictive. Tables and rules support accurate, context-aware efficiency prediction.

## Background & Definitions

**Prediction Task**:  
Given 14 design parameters (CONFIG) and the average efficiency of the *control* condition (no punishment), predict the average efficiency of the *treatment* condition (same game, punishment enabled).

- **Efficiency**: Total group payoff divided by payoff if all fully cooperate. Efficiency = 1 (full cooperation); lower values = less cooperation.
- All predictions are within-protocol and under a common online environment, with only CONFIG parameters varying.

## Data & Variables

**Key Variables (CONFIG Parameters):**

| Parameter Name              | Definition                                                                              |
|----------------------------|-----------------------------------------------------------------------------------------|
| CONFIG_playerCount          | Number of players in the game                                                          |
| CONFIG_numRounds           | Number of rounds in the game                                                           |
| CONFIG_MPCR                | Marginal per-capita return: multiplier / playerCount                                   |
| CONFIG_allOrNothing        | 1 = contributions are all-or-nothing; 0 = continuous                                   |
| CONFIG_chat                | 1 = chat enabled between players; 0 = not enabled                                      |
| CONFIG_defaultContribProp  | 0 = opt-in (default keep), 1 = opt-out (default contribute)                            |
| CONFIG_punishmentCost      | Cost to punisher per unit of punishment                                                |
| CONFIG_punishmentMagnitude | Coins deducted per unit punishment                                                      |
| CONFIG_showOtherSummaries  | 1 = peer outcomes visible each round, 0 = not visible                                  |
| CONFIG_showNRounds         | 1 = total number of rounds shown to players, 0 = not shown                             |
| CONFIG_showPunishmentId    | 1 = identity of punishers shown, 0 = not shown                                         |
| CONFIG_rewardExists        | 1 = rewards enabled in the game, 0 = not enabled                                       |
| CONFIG_rewardCost          | Cost per unit of reward to the rewarder                                                 |
| CONFIG_rewardMagnitude     | Coins added per unit of reward                                                         |

**Other Calculated Predictors (used in model and analysis):**

| Calculated Variable            | Definition                                                     |
|-------------------------------|----------------------------------------------------------------|
| CONFIG_punishmentTech         | Punishment effectiveness = punishmentMagnitude / punishmentCost |
| CONFIG_scaledPunishmentCost   | punishmentCost / endowment                                     |
| CONFIG_MPCR_adjusted          | multiplier / actual num players                                |
| CONFIG_rewardTech             | rewardMagnitude / rewardCost                                   |

**Control Efficiency:**  
Average efficiency in the exact same condition with punishment disabled, provided as input for prediction.

## Empirical Patterns (Punishment Effects & Heterogeneity)

**Main observations from experiment & analyses:**

- **Punishment effect on efficiency is highly heterogeneous**:
    - Overall effect ranges: Δefficiency from -44% to +43% depending on parameter context.
    - Mean learning effect: Efficiency drops from 0.71 → 0.63 with punishment enabled (Δ = -0.08, or ≈ -11%).
    - Mean validation effect: 0.72 → 0.68 (Δ = -0.04, or ≈ -6%).

- **Key moderators (with largest interactions):**
    - **Communication (`CONFIG_chat`)**: When enabled, punishment is likely to *improve* efficiency. When disabled, impact is often negative.
    - **Contribution framing (`CONFIG_defaultContribProp`) & type (`CONFIG_allOrNothing`)**: Opt-out benefits punishment effect in variable contributions but can *reduce* effectiveness in all-or-nothing conditions.
    - **Peer outcome visibility (`CONFIG_showOtherSummaries`)**: Seeing peer outcomes can dampen positive effect of punishment; interacts with contribution framing.
    - **Game length (`CONFIG_numRounds`)**: Longer games amplify positive punishment effects but only when chat is enabled.

- **Reward system** (if present) and higher **MPCR** are positive but have smaller impact than the above factors.

- **Punishment parameters** (cost, magnitude): Little direct effect; their predictive power mainly comes from interactions with game context, not main effects.

- **Control efficiency**: Higher observed efficiency in control predicts higher efficiency with punishment enabled (effect is less than 1:1 but strong).

## Quantitative Summary

**Table 1: Global Means (from analysis and paper)**

| Condition             | Mean Efficiency | SD    |
|-----------------------|----------------|-------|
| No Punishment (Ctrl)  | 0.71           | 0.17  |
| Punishment Enabled    | 0.63           | 0.18  |
| Validation Ctrl       | 0.72           | 0.16  |
| Validation Punish     | 0.68           | 0.18  |

**Table 2: Summary of Key Moderators and Ranges**

| Parameter/Interaction         | Punishment Effect on Efficiency                            | Numeric Range / Effect                        |
|------------------------------|------------------------------------------------------------|-----------------------------------------------|
| Chat enabled                 | Tends to increase efficiency when punishment is enabled     | Δ +0.07 to +0.20                              |
| Chat disabled                | Tends to decrease efficiency                               | Δ -0.05 to -0.16                              |
| Opt-in (default keep)        | Punishment more effective                                  | Δ +0.04 to +0.18                              |
| Opt-out (default contribute) | Effect context dependent (see rules)                       | Range: -0.08 to +0.10                         |
| Long games + chat            | Amplifies positive effect                                  | Δ +0.15 to +0.25                              |
| Peer outcome visibility      | Dampens positive effect, especially for all-or-nothing     | Up to -0.10                                   |
| Punishment cost/multiplier   | Weak direct effect                                         | Most Δ <±0.03                                 |
| Control efficiency           | Strong positive predictor; adjusted slope < 1              | Slope ≈ 0.7–0.9                               |

**Model signal:**  
- Top models (e.g., Elastic Net) outperform human prediction, relying more on context and interaction effects than single-parameter main effects.

## Predictive Guidance

### Ranked Predictor List

1. **CONFIG_chat** (chat enabled/disabled)
2. **CONFIG_defaultContribProp** and **CONFIG_allOrNothing** (framing × contribution type)
3. **CONFIG_numRounds** (game length, especially with chat)
4. **CONFIG_showOtherSummaries** (peer outcome visibility)
5. **CONFIG_MPCR** (marginal per-capita return)
6. **CONFIG_rewardExists** (reward enabled)
7. **Control efficiency** (from paired no-punishment condition)
8. **Punishment/reward technical parameters** _only via interaction_ (e.g., punishmentTech)
9. **CONFIG_playerCount** (mild moderator)
10. **CONFIG_showNRounds**, **CONFIG_showPunishmentId** (minor)

### Rules (If-Then Statements With Numeric Effects)

#### Core Rule:  
- **If all else equal & no other strong moderating features, enabling punishment decreases efficiency by 5–12%.**  
  - Numeric effect: Δefficiency ≈ -0.05 to -0.12 relative to control.

#### Key Moderators and Interactions

1. **If `CONFIG_chat` = 1 (chat enabled):**
    - *Then* enabling punishment increases efficiency by **+0.07 to +0.20** vs. control;
    - *If* game is also long (`CONFIG_numRounds` ≥ median, e.g., ≥ 15), *then* increase can reach **+0.15 to +0.25**.

2. **If `CONFIG_chat` = 0 (chat disabled):**
    - *Then* enabling punishment reduces efficiency by **-0.05 to -0.16**.

3. **If `CONFIG_allOrNothing` = 0 (variable contribution) AND `CONFIG_defaultContribProp` = 1 (opt-out):**
    - *Then* punishment is substantially more effective; Δefficiency **+0.08 to +0.13**.

4. **If `CONFIG_allOrNothing` = 1 (all-or-nothing) AND `CONFIG_defaultContribProp` = 1 (opt-out) AND `CONFIG_showOtherSummaries` = 1:**
    - *Then* punishment *reduces* efficiency; Δefficiency **-0.08 to -0.15**.

5. **If `CONFIG_showOtherSummaries` = 1:**
    - *Then* positive punishment effects are dampened by up to **0.10**.

6. **If `CONFIG_rewardExists` = 1:**
    - *Then* (minor) increases in efficiency from punishment, Δefficiency **+0.02 to +0.06**.

7. **If higher `CONFIG_MPCR` (≥0.5):**
    - *Then* marginal increase in positive punishment effect, Δefficiency **+0.03 to +0.08**.

8. **If `CONFIG_numRounds` is large (≥75th percentile):**
    - *Then* only boosts punishment effect if chat is enabled.

9. **If control efficiency is high (≥0.8):**
    - *Then* punishment effect is muted; predicted treatment efficiency ≈ 0.7–0.95 × control.

10. **If control efficiency is low (≤0.5) AND chat is disabled OR all-or-nothing & opt-out:**
    - *Then* enabling punishment may *further* reduce efficiency (Δ up to -0.20).

#### Secondary/Minor Rules

- **Punishment tech/cost/magnitude:**  
  No main effect unless interacting with chat, framing, or MPCR; otherwise, ignore as predictive signal.
- **Other minor config parameters:**  
  Minimal main effect unless supporting a key moderator above.

### Range Table

| Primary Scenario                                 | Predicted Δefficiency (punishment - control)  |
|--------------------------------------------------|------------------------------------------------|
| Chat on, flexible contrib, opt-in                | +0.15 to +0.25                                 |
| Chat off, control efficiency high (≥0.8)         | -0.04 to -0.07                                 |
| Chat off, all-or-nothing, opt-out, peer visible  | -0.10 to -0.20                                 |
| Chat on, long game (>15 rounds), opt-in          | +0.15 to +0.30                                 |
| Rewards present, peer hidden, variable contrib   | +0.07 to +0.13                                 |
| Control efficiency low (<0.5), chat off          | -0.12 to -0.20                                 |

## Limitations & Open Questions

- Rules are empirically grounded but models may overfit to the specific population (MTurk, US/UK, online environment).
- External validity outside the study’s protocol is unknown.
- Some combinations of config parameters are under-represented in the data; rare edge cases may not follow these patterns.
- Reward and punishment systems not experimentally orthogonal in all cases; complex three-way interactions may be underestimated.
- The directionality and magnitude of punishment’s effect are not universal—context and configuration interactions matter most.

## How To Use This For Predictions

- For each new instance, record all 14 CONFIG parameters plus observed control efficiency.
- Apply the ranked predictor rules in order: check for chat, then framing/type, then outcome visibility and game length, and so forth.
- Adjust the predicted Δefficiency from control using numeric ranges in the rule table.
- For most accurate results, weight control efficiency heavily but adjust for configuration as above.
- Use multi-factor interaction rules: do not assume additive independent effects.
- Ignore direct punishment “technology” unless noted in interaction rules.
- Treat strong negative effects as more likely if chat is off, or all-or-nothing/opt-out/framing is adverse.
- Document edge cases and uncertainty if config combination is rare or unusual.
- Use regular (unnormalized) efficiency as primary outcome when predicting.

---

**Operationalizing these rules yields robust and context-aware predictions of punishment-enabled efficiency in new public goods games, making them suitable for model training, forecasting, or policy simulation under controlled online PGG protocols.**
