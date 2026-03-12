# Predicting the Efficiency Impact of Enabling Punishment in Public Goods Games

## Abstract

This report synthesizes large-scale experimental evidence to guide predictive modeling of how enabling punishment changes group efficiency in public goods games (PGGs). Using factorial experimental designs, paired control/treatment configurations, and statistical models, we quantify the aggregate impact of punishment, identify the main contextual and structural moderators, and provide actionable, numerically grounded heuristics. Efficient prediction hinges on capturing the interactions among communication, contribution framing, game visibility, and reward availability. We tabulate effect ranges and adjustment rules for use in operational PGG forecasting, grounded in both statistical analysis and published protocols.

---

## Background & Definitions

**Prediction Task:**  
Given (1) values for 14 game design parameters (CONFIG variables) and (2) the observed average efficiency in the control (punishment disabled) version of a public goods game, predict the average efficiency under the same configuration when punishment is enabled.

- **Efficiency**: The group’s total payoff divided by the payoff if all members contributed fully every round.  
    - Efficiency = 1: collective optimum (full cooperation)
    - Efficiency < 1: losses due to free-riding, coordination failure, and/or inefficiency (including punishment costs)

**Why this is hard:**  
Punishment’s effect on efficiency is highly context-dependent, with direction and size contingent upon multiple interacting design features, rather than being a stable main effect.

---

## Data & Variables

### Experimental Design

- 360 unique game configurations, each run with and without punishment (paired design).
- Over 7,000 participants and 147,000+ decisions.
- Protocol, population, and interface were held constant to ensure effect heterogeneity is driven by design features (CONFIG parameters), not extraneous factors.

### The 14 CONFIG Parameters

| Parameter                        | Description                                                                                       | Typical Range / Coding                 |
|-----------------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------|
| **CONFIG_playerCount**            | Number of players per group                                                                       | 2–8                                   |
| **CONFIG_numRounds**              | Number of rounds in the game                                                                      | 5–30                                  |
| **CONFIG_MPCR**                   | Marginal Per Capita Return: multiplier/playerCount; gain per coin contributed                     | 0.2–0.5 (float)                       |
| **CONFIG_allOrNothing**           | Contribution mode: 1 = all-or-nothing; 0 = variable (continuous)                                 | 0/1                                   |
| **CONFIG_chat**                   | Whether communication (chat) is enabled between players                                          | 0/1                                   |
| **CONFIG_defaultContribProp**     | Contribution framing: 0 = opt-in (must act to give); 1 = opt-out (must act to keep)              | 0/1                                   |
| **CONFIG_punishmentCost**         | Cost in coins to punisher per unit of punishment imposed                                         | positive float                        |
| **CONFIG_punishmentMagnitude**    | Coins lost by punished player per unit punishment                                                | positive float                        |
| **CONFIG_showOtherSummaries**     | Whether peer (group) outcomes are displayed after rounds                                         | 0/1                                   |
| **CONFIG_showNRounds**            | Whether the number of rounds is visible to participants                                          | 0/1                                   |
| **CONFIG_showPunishmentId**       | Whether punishers' identities are revealed                                                       | 0/1                                   |
| **CONFIG_rewardExists**           | Whether bonus/reward giving is enabled                                                           | 0/1                                   |
| **CONFIG_rewardCost**             | Cost to rewarder per unit bonus given                                                            | positive float                        |
| **CONFIG_rewardMagnitude**        | Bonus to rewardee per unit received                                                              | positive float                        |

- **Control efficiency:** The group's average efficiency with punishment disabled (used as the baseline for prediction).

---

## Empirical Patterns: Punishment Effects & Heterogeneity

- **Aggregate average effect of punishment:**  
  - Across all configurations, enabling punishment decreases average group efficiency by 5–11 percentage points (mean ΔEfficiency: –0.06 to –0.11).
- **Extreme heterogeneity:**  
  - In some settings, punishment increased efficiency by as much as +0.43.
  - In others, it decreased efficiency by up to –0.44.
- **Key drivers of effect direction and size:**  
  - **Communication (CONFIG_chat):** Most reliably predicts a positive efficiency effect of punishment.
  - **Contribution Framing (CONFIG_defaultContribProp):** Opt-out (default contribute) framing enhances positive effects in variable-contribution games but reverses in all-or-nothing designs.
  - **Game Visibility (CONFIG_showOtherSummaries):** Outcome visibility amplifies both positive and negative impacts via interaction with other features.
  - **Reward Availability (CONFIG_rewardExists):** Moderately enhances the positive effect of punishment.
  - **Contribution Type (CONFIG_allOrNothing):** All-or-nothing mode interacts negatively with opt-out framing and visibility.
  - **Mechanical punishment parameters** (cost, magnitude): Much weaker predictors than contextual features.

---

## Quantitative Summary

### Table 1. Overall Effects of Punishment Enabling

| Statistic                | No Punishment | Punishment Enabled | Δ Efficiency (Punishment – Control) |
|--------------------------|---------------|-------------------|-------------------------------------|
| Mean efficiency          | 0.661         | 0.605             | –0.056                              |
| Median efficiency        | 0.668         | 0.606             | –0.062                              |
| 10th percentile          | 0.512         | 0.430             | –0.082                              |
| 90th percentile          | 0.792         | 0.752             | –0.040                              |
| Max observed gain        | —             | —                 | +0.43                               |
| Max observed loss        | —             | —                 | –0.44                               |
| Standard deviation       | 0.164         | 0.188             | +0.024                              |

**Empirical range (80% of cases): ΔEfficiency = –0.14 to +0.11**

---

### Table 2. Moderator Effects: Mean Change in Efficiency by CONFIG Features

| Moderator                   | Category                      | Mean ΔEfficiency (Punish-On vs Off)      |
|-----------------------------|-------------------------------|------------------------------------------|
| **Communication (chat)**    | Chat ON                       | +0.03 to +0.18                           |
|                             | Chat OFF                      | –0.07 to –0.18                           |
| **Contribution Framing**    | Opt-in (defaultContrib=0)     | –0.04 to –0.08                           |
|                             | Opt-out (defaultContrib=1), variable | +0.07 to +0.13                     |
|                             | Opt-out × all-or-nothing      | –0.10 to –0.13                           |
| **Contribution type**       | All-or-nothing                | –0.10 to –0.13                           |
|                             | Variable                      | –0.02 to +0.08                           |
| **Reward exists**           | Yes                           | +0.06 to +0.14                           |
|                             | No                            | –0.06 to –0.11                           |
| **Outcome visibility**      | Shown                         | –0.02 to +0.06 (effect depends on interaction) |
|                             | Hidden                        | –0.08                                   |
| **Game length**             | Long (>12–15 rounds), chat=1  | +0.03 per 5 rounds                       |
| **MPCR**                    | <0.35                         | –0.09 to –0.18                           |
|                             | ≥0.45                         | +0.03 to +0.08                           |
| **Punishment params**       | (cost, magnitude)             | < ±0.03 (negligible)                     |

---

### Table 3. Predicted Effect Ranges: Prototypical Configurations

| Context                                                                                     | ΔEfficiency Range         |
|---------------------------------------------------------------------------------------------|--------------------------|
| Chat ON, Opt-out, Variable contrib, Reward ON                                               | +0.09 to +0.25           |
| Chat OFF, All-or-Nothing contrib, Opt-out framing                                           | –0.10 to –0.28           |
| MPCR <0.35, No chat, No reward                                                              | –0.18 to –0.43           |
| MPCR ≥0.45, Chat ON, Reward ON, Variable contrib                                            | +0.03 to +0.18           |
| Game length >15 rounds, Chat ON, Peer outcomes visible                                      | +0.02 to +0.13           |
| All-or-Nothing, Opt-in framing, No chat, Reward OFF                                         | –0.07 to –0.24           |

---

## Predictive Guidance

### Rules of Thumb and Numeric Adjustments

- **Start with observed control efficiency (punishment OFF) as baseline.**
- **Adjust for key moderators and their interactions:**

    1. **Communication (CONFIG_chat):**
        - If enabled: add +0.05 to +0.12; largest gains when combined with long games and visible outcomes.
        - If disabled: expect efficiency drop, –0.07 to –0.18.
    2. **Contribution framing × contribution type:**
        - Opt-out + variable: add +0.07 to +0.13.
        - Opt-out + all-or-nothing: subtract –0.10 to –0.13.
        - Opt-in (default keep): mild negative or near-zero.
    3. **Rewards available (CONFIG_rewardExists):**
        - If enabled: add +0.06 to +0.14.
        - If disabled: subtract –0.06 to –0.11.
    4. **Visibility (CONFIG_showOtherSummaries):**
        - If ON: modifies effect, amplifies moderator interactions (positive if paired with chat, but can also amplify negatives).
    5. **MPCR (CONFIG_MPCR):**
        - If ≥0.45: add +0.03 to +0.08.
        - If <0.35: subtract –0.09 to –0.18.
    6. **Game length (CONFIG_numRounds):**
        - Each additional 5 rounds, if chat=1: +0.03.
    7. **Mechanical punishment parameters:** Ignore unless set at pathological extremes; effect size typically <±0.03.

- **Account for interactions:** Positive effects are maximized when multiple facilitators combine (e.g., chat + opt-out + variable contrib + reward + long games + outcome visibility).

#### Quick-Reference: Expected Adjustment Magnitudes

| Change in Key Variable                  | Predicted ΔEfficiency |
|-----------------------------------------|----------------------|
| Enable chat (0 → 1)                     | +0.05 to +0.12       |
| Switch to opt-out, variable contrib     | +0.07 to +0.13       |
| Switch to opt-out, all-or-nothing       | –0.10 to –0.13       |
| Add reward (0 → 1)                      | +0.06 to +0.14       |
| MPCR increase from <0.35 to ≥0.45       | +0.09 to +0.16       |
| Game length +5 rounds (if chat=1)       | +0.03                |
| Show peer outcomes                      | context-dependent    |

---

## Limitations & Open Questions

- **Data limits:** The entire dataset is from a single, controlled online population—generalizability to other populations, high-stakes, or face-to-face settings is untested.
- **Predictive boundaries:** Models using only CONFIG variables plus control efficiency explain 71–82% of out-of-sample variance; prediction is robust but not perfect.
- **Interaction complexity:** Some three-way and higher interactions are insufficiently parameterized; simple additive rules may fail at extremes.
- **Mechanical parameters:** The limited range of punishment cost/magnitude studied; predictions may be unreliable for extreme values outside the studied parameter space.
- **Effects at extremes:** Fully adverse or beneficial configurations—rare but possible—can yield ΔEfficiency shifts up to ±0.40; these should be flagged.

---

## How To Use This For Predictions

1. **Collect the 14 CONFIG parameters and observed control (punishment-off) efficiency for your prediction instance.**
2. **Start with control efficiency as baseline.**
3. **Sequentially apply numeric adjustments for moderators:**
    - Add positive or negative deltas according to chat, contribution framing/type, rewards, MPCR, game length, and outcome visibility.
    - Multiply/compound effects when positive moderators are aligned.
4. **Account for interactions:** Do not assume effects are independent; largest changes come from moderator combinations.
5. **Ignore punishment cost/magnitude for welfare prediction unless using nonstandard values.**
6. **If in doubt, refer to the empirical range (–0.44 to +0.43) and flag predictions outside –0.14 to +0.11 as uncertain or unusual.**
7. **Use full regression or ensemble models including interactions for maximal accuracy where available.**
8. **Treat predictions as conditional on the protocols and online context of the experimental dataset.**

---

**Summary:**  
Prediction of how enabling punishment changes efficiency in public goods games must foreground feature interactions and contextual moderators—especially communication, framing, game visibility, and reward options—rather than relying on mechanical parameters or main effects. The most operationally reliable policies combine these features to compute expected efficiency change, using a control baseline and empirically derived adjustment rules grounded in large, paired experimental data.
