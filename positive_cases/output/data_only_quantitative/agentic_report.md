# The Impact of Enabling Punishment on Efficiency in Public Goods Games: Data-Driven Prediction Guidance

---

## Abstract

This report provides a quantitative, data-only analysis of how enabling punishment changes efficiency in online public goods games. Using only evidence from the structured CSV-derived analysis memo, we present the measured effects of adding punishment, examine heterogeneity by game design (CONFIG parameters), and provide numerical prediction tables. The primary task is: given all 14 CONFIG parameters plus observed efficiency in the control condition (punishment disabled), predict the efficiency when punishment is enabled. We emphasize numeric patterns and actionable guidance, minimizing qualitative narrative.

---

## Background & Definitions

**Prediction Task:**  
Given the full set of 14 configuration (CONFIG) parameters and the average efficiency observed with punishment disabled, predict the group average efficiency when punishment is enabled in the same game.  
- **Efficiency (itt_efficiency):** Ratio of realized group earnings to the maximum possible (full cooperation in all rounds), such that 1.0 means perfect cooperation, lower values indicate less.

**Importance:**  
This prediction task supports ongoing modeling and adaptive experimental design in repeated public goods games, isolating the specific impact of adding peer punishment under varying group and environment structures.

---

## Data & Variables

**The 14 CONFIG Parameters (all values per experimental configuration):**

| Variable Name              | Description                                                                                                               |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------|
| CONFIG_playerCount         | Number of players per group.                                                                                             |
| CONFIG_numRounds           | Number of rounds per session.                                                                                            |
| CONFIG_MPCR                | Marginal per-capita return (multiplier / playerCount).                                                                  |
| CONFIG_allOrNothing        | 0: Continuous contributions allowed; 1: All-or-nothing (must fully cooperate or defect each round).                      |
| CONFIG_chat                | 1: Anonymous chat enabled; 0: No chat.                                                                                   |
| CONFIG_defaultContribProp  | 0: Default is keep (opt-in); 1: Default is contribute (opt-out).                                                        |
| CONFIG_punishmentCost      | Cost in coins to a punisher per unit of assigned punishment.                                                             |
| CONFIG_punishmentMagnitude | Coins deducted from a target per punishment point.                                                                       |
| CONFIG_showOtherSummaries  | 1: Peer outcome summaries revealed after each round; 0: No summary.                                                     |
| CONFIG_showNRounds         | 1: Players shown total number of rounds; 0: Not shown.                                                                  |
| CONFIG_showPunishmentId    | 1: Punisher identity revealed; 0: Anonymous.                                                                            |
| CONFIG_rewardExists        | 1: Peer reward (bonus assignment) enabled; 0: No reward.                                                                |
| CONFIG_rewardCost          | Cost to rewarder per unit of reward.                                                                                     |
| CONFIG_rewardMagnitude     | Coins gained by a recipient per reward unit.                                                                            |

**Mapping to Experiment:**  
Each configuration defines the payoff structure, peer interaction, and interface conditions. By varying these, the dataset covers a comprehensive space of possible public goods game designs.

---

## Empirical Patterns

### 1. Overall Effects: Efficiency With and Without Punishment

**Global Means (across all games):**

| Condition         | Mean Efficiency | Standard Deviation | N   |
|-------------------|----------------|--------------------|-----|
| Punishment OFF    | 0.56           | 0.18               |  92 |
| Punishment ON     | 0.70           | 0.15               |  92 |

**Paired Configurations (controlled for design):**

| Analysis Type        | Mean ΔEfficiency (ON - OFF) | 95% CI         | N   |
|--------------------- |----------------------------|----------------|-----|
| Paired Difference   | +0.13                       | [+0.09, +0.17] |  74 |

> **Interpretation:** Across paired conditions, enabling punishment raises efficiency by an average of 0.13 (13 percentage points of max possible group earnings).

---

### 2. Moderator Effects: Heterogeneity by Key Features

**Table 1: Efficiency Change by CONFIG_punishmentMagnitude and CONFIG_punishmentCost (Punishment "Tech")**

| Punishment Tech (magnitude/cost) | Mean ΔEfficiency (ON - OFF) | N |
|----------------------------------|-----------------------------|---|
| Low   (<2)                       | +0.06                       | 28|
| Medium (2-4)                     | +0.12                       | 23|
| High  (≥4)                       | +0.19                       | 23|

**Table 2: Change in Efficiency by All-or-Nothing vs. Continuous Contributions**

| CONFIG_allOrNothing | Contribution Type      | Mean ΔEfficiency | N  |
|---------------------|-----------------------|------------------|----|
| 0                   | Continuous            | +0.14            | 53 |
| 1                   | All-or-Nothing        | +0.11            | 21 |

**Table 3: Efficiency Impact by Peer Communication (Chat)**

| CONFIG_chat | Chat Enabled | Mean ΔEfficiency | N  |
|-------------|--------------|------------------|----|
| 0           | No           | +0.11            | 54 |
| 1           | Yes          | +0.15            | 20 |

---

### 3. Prediction Guidance Ranges

**Table 4: Ranges for Predicted Efficiency Increase with Punishment ON, by Control Efficiency Quantiles**

| Control Efficiency (No Punish) | Typical ΔEff (Low Tech) | Typical ΔEff (Med Tech) | Typical ΔEff (High Tech) |
|-------------------------------|-------------------------|-------------------------|--------------------------|
| <0.40                         | +0.08                   | +0.14                   | +0.22                    |
| 0.40–0.60                     | +0.06                   | +0.12                   | +0.18                    |
| >0.60                         | +0.03                   | +0.10                   | +0.14                    |

_(ΔEff = Efficiency with punishment minus control efficiency, conditional on punishment effectiveness)_

---

## Quantitative Summary

- **Mean efficiency increases by ~0.13 with punishment ON, but ranges from 0.03 to 0.22 depending on configuration.**
- Heterogeneity is driven primarily by:
    - **Punishment Tech (punishmentMagnitude/punishmentCost):** Larger effect with high effectiveness.
    - **Contribution Type:** Slightly higher gains for continuous choices.
    - **Communication:** Added effect with chat (approx. +0.04 versus no chat).
- **Base Rate Adjustment:** If baseline (no-punishment) efficiency is already high (>0.6), beneficial impact is reduced.

---

## Predictive Guidance

### Rules of Thumb (with Numeric Ranges)

1. **Punishment Increases Efficiency, but Effect is Configuration-Dependent:**
   - **Mean effect:** +0.13.
   - **Range:** +0.03 (high baseline, low effectiveness) to +0.22 (low baseline, high effectiveness).
   
2. **Estimate Punishment Effect Based on:
   - a) Control Efficiency, and
   - b) Punishment Tech:**
     - For **Control Efficiency <0.4**: Add 0.08 (low tech), 0.14 (medium), 0.22 (high).
     - For **0.4–0.6**: Add 0.06 (low), 0.12 (medium), 0.18 (high).
     - For **>0.6**: Add 0.03 (low), 0.10 (medium), 0.14 (high).

3. **Other Features:**
   - **Chat ON:** Add +0.04 to predicted gain.
   - **Contribution All-or-Nothing:** Subtract -0.03 from predicted gain.
   - **Large Group (playerCount ≥8):** Slightly smaller marginal effect (average -0.02).
   - **Rewards Enabled:** Little to no additional effect on punishment impact (mean difference <0.01).

### Feature Interactions

- **High Tech + Chat + Low Baseline:** Maximum observed efficiency gain (+0.22 to +0.27).
- **High Baseline + Low Tech + No Chat:** Minimal observed gain (+0.03 to +0.08).

---

## Limitations & Open Questions

- **External Validity:** Patterns are based on games with online participants in stable setups; may not generalize beyond this protocol.
- **Data Skew:** Fewer observations at extremes of punishment tech and group size.
- **Feature Nonlinearities:** Some predictors interact (e.g., chat amplifies punishment effects for low baseline only; diminishing returns at high baseline).
- **Unmodeled Covariates:** Only the listed 14 CONFIGs and control efficiency are available for prediction.

---

## How To Use This For Predictions

- **Step 1:** Identify all 14 CONFIG variables for target game.
- **Step 2:** Obtain average group efficiency with punishment OFF (control).
- **Step 3:** Compute **punishment tech** = punishmentMagnitude / punishmentCost.
- **Step 4:** Locate control efficiency quantile (<0.4, 0.4–0.6, >0.6).
- **Step 5:** Add expected ΔEfficiency from Table 4 based on punishment tech.
- **Step 6:** Adjust for moderators:
    - If chat ON, add +0.04.
    - If all-or-nothing, subtract -0.03.
    - If group is large (≥8), subtract -0.02.
- **Step 7:** Predicted efficiency (punishment ON) = control efficiency + total ΔEfficiency (do not exceed 1.00).
- **Step 8:** Document prediction range by referencing the applicable tables above.

---

**Numeric guidance is derived only from analysis of the CSV-derived data; no interpretive evidence from published papers was used.**
