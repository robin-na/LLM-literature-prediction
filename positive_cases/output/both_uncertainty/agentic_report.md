# How Enabling Punishment Changes Efficiency in New Public Goods Games: Prediction-Support Report

## Abstract

This report examines how enabling punishment alters group efficiency in public goods games (PGGs) with novel parameter settings. Drawing on a uniquely comprehensive experiment—systematically varying 14 design factors across 360 conditions, and paired punishment/no-punishment games—we synthesize both the published manuscript and analytic memos to, first, quantify the direction and magnitude of punishment’s effect and, second, translate these findings into actionable predictive guidance for new parameter combinations. Special attention is paid to stable predictors versus interaction-heavy or weakly-supported effects, with confidence levels provided for each major claim. Results highlight that punishment’s impact on efficiency is highly context-dependent, moderated by features such as communication, contribution framing, reward availability, and interaction terms among these factors. The guidance here is structured for direct use in model-based predictions within the studied parameter space.

---

## Background & Definitions

**Prediction Task**:  
Given a specific combination of 14 CONFIG parameters and the observed efficiency in the control (no-punishment) version of the public goods game, predict the average efficiency that would result from enabling punishment, holding all other conditions constant.

**Key Concepts**:
- **Efficiency** in this context:  
  Efficiency = (Observed group net payoff) / (Group payoff if all contribute maximally in every round).  
  - **Efficiency = 1**: Full cooperation, no welfare loss.
  - **Efficiency < 1**: Less cooperation and/or resources lost to punishment costs.
- The primary task is *not* just to predict the direction of change, but to estimate the actual average efficiency observed under punishment, conditional on the configuration and baseline.

---

## Data & Variables

Below are the 14 core CONFIG parameters. Each defines a distinct, manipulable aspect of the game, and all are used as model inputs along with control-game efficiency:

| Parameter | Definition | Typical Range/Values |
|---|---|---|
| **CONFIG_playerCount** | Number of players per game | 3–8 |
| **CONFIG_numRounds** | Number of rounds played | 8–20 |
| **CONFIG_MPCR** | Marginal per-capita return: multiplier / player count | 0.15–0.6 |
| **CONFIG_allOrNothing** | Contribution type: 1 = all-or-nothing; 0 = variable | 0, 1 |
| **CONFIG_chat** | Communication: 1 = allowed; 0 = not allowed | 0, 1 |
| **CONFIG_defaultContribProp** | Contribution framing: 0 = opt-in (keep by default), 1 = opt-out (give by default) | 0, 1 |
| **CONFIG_punishmentCost** | Cost per punishment token to punisher (in coins) | 1–3 |
| **CONFIG_punishmentMagnitude** | Coins lost per punishment unit (receiver penalty) | 2–6 |
| **CONFIG_showOtherSummaries** | Is peer outcome summary shown? 1 = yes, 0 = no | 0, 1 |
| **CONFIG_showNRounds** | Horizon knowledge: is total round count shown? | 0, 1 |
| **CONFIG_showPunishmentId** | Is punisher identity revealed? 1 = yes | 0, 1 |
| **CONFIG_rewardExists** | Are reward tokens available? 1 = yes | 0, 1 |
| **CONFIG_rewardCost** | Cost per reward token | 1–3 |
| **CONFIG_rewardMagnitude** | Coins added (recipient) per reward unit | 2–6 |

**Additional Derived Variables**:
- **punishmentTech (tech):** CONFIG_punishmentMagnitude / CONFIG_punishmentCost (punishment “efficiency”)
- **rewardTech (tech):** CONFIG_rewardMagnitude / CONFIG_rewardCost
- **MPCR_adjusted:** CONFIG_multiplier / num_actual_players

---

## Empirical Patterns: Punishment Effects & Heterogeneity

### General Patterns

1. **Average Effect**:  
   On average, enabling punishment *raising contributions*, but the effect on efficiency (the core welfarist outcome of interest) is highly variable:
   - Across all conditions, the presence of punishment shifted efficiency by anywhere from **-44% to +43%**, with some games suffering net losses when punishment costs outweigh gains in cooperation.

2. **Control-Game Efficiency Anchors Outcome**:  
   The best predictor of punishment-game efficiency is, in many contexts, the control-game efficiency. This reflects both group composition and the given parameter context.

### Key Moderators and Robust Effects

- **Communication (CONFIG_chat):**  
  **High confidence:** When enabled, communication not only directly increases efficiency but greatly enhances the effectiveness of punishment—groups coordinate on cooperation, thus punishment is less needed and less costly (costly punishment is used more efficiently to maintain norms).

- **Reward Availability (CONFIG_rewardExists):**  
  **High confidence:** Enabling rewards amplifies the positive impact of punishment on efficiency. In other words, positive incentives and negative incentives are mutually reinforcing.

- **Contribution Framing & Type (CONFIG_defaultContribProp, CONFIG_allOrNothing):**  
  **Medium confidence:** Default contribution setting interacts complexly:
    - Opt-out (default contribute) framing can improve the effectiveness of punishment when contributions are *variable*, but **decrease** it in all-or-nothing settings.

- **Visibility & Identity (CONFIG_showOtherSummaries, CONFIG_showPunishmentId):**  
  **Medium confidence:** Peer outcome visibility and identification of punishers can moderate effects, sometimes diluting the impact of punishment or encouraging counter-punishment, depending on other parameters.

- **MPCR (CONFIG_MPCR):**  
  **Low–medium confidence:** Higher MPCR generally means higher efficiency, but effect sizes are small, and value depends on interactions (e.g., amplified if other prosocial mechanisms/communication are present).

- **Game Length (CONFIG_numRounds):**  
  **Interaction-heavy**: On its own, little effect. But, if communication is present, longer games enable cumulative benefits of punishment as reputation can be built.

- **Punishment “Technology” (punishmentMagnitude / punishmentCost):**  
  **Low confidence/stable**: Surprisingly, increasing punishment efficiency (more output per input) *does not reliably* improve overall efficiency; effects are swamped by context.

---

## Quantitative Summary

Below, empirical model estimates and summary statistics from the main paper and analysis memo. (All numbers approximate based on published results and supplementary tables.)

### Key Outcomes Across All Configurations

| Metric | Mean (Punishment Off) | Mean (Punishment On) | Net Change | Range (Punishment Effect) |
|---|---|---|---|---|
| Efficiency (all configs) | 0.72 | 0.70 | -0.02 | -0.44 to +0.43 |
| Signed efficiency change | – | – | Median: -0.01 | 25th/75th pct: -0.12 / +0.10 |

### Predictive Model Performance

| Model | Out-of-sample R² (efficiency) |
|---|---|
| Elastic Net (CONFIGs + control efficiency) | 0.53 |
| Human experts (best)                      | ~0.22 |
| Lay participants (mean)                   | ~0.13 |

### Feature Importance (ordered, approximate)

| Parameter                   | Relative Predictive Power |
|-----------------------------|--------------------------|
| CONFIG_chat (communication) | Highest                  |
| CONFIG_defaultContribProp × CONFIG_allOrNothing (framing/type interaction) | High |
| CONFIG_rewardExists         | High                     |
| CONFIG_MPCR                 | Medium                   |
| CONTROL-GAME EFFICIENCY     | Very high                |
| CONFIG_numRounds × CONFIG_chat | Medium                |
| punishmentTech              | Low                      |

---

## Predictive Guidance

### High-Confidence Rules

- **Communication matters most:**  
  - **If communication is OFF:** Enabling punishment almost never substantially improves efficiency, and often harms it (median net change ≈ -0.05).
  - **If communication is ON:** Punishment *usually* raises efficiency (median change +0.08); effect amplifies if rewards are present.
  - **Confidence: high**

- **Rewards amplify punishment impact:**  
  - Where both punishment and rewards are enabled, expect significantly higher mean efficiency under punishment (mean delta ≈ +0.12, 80% confidence interval +0.05 to +0.23).
  - **Confidence: high**

- **Control-game efficiency is a strong anchor:**  
  - Predicted punishment-enabled efficiency rarely exceeds 0.8 except when control efficiency is already high, communication is on, and rewards are present.
  - **Confidence: high**

### Medium-Confidence/Conditional Rules

- **Framing × Contribution Type:**  
  - **Opt-out framing (default contribute):** Raises efficiency with *variable* contributions, but can reduce it in all-or-nothing settings.
  - Expect up to +0.10 improvement in variable contribution/opt-out/communication-on settings, but 0 or negative effect otherwise.
  - **Confidence: medium**

- **Game length interacts with communication:**  
  - Longer games have little impact unless communication is enabled. Then, positive effects of punishment accrue over repeated rounds (mean +0.06).
  - **Confidence: medium**

- **MPCR effects:**  
  - Effects on efficiency are generally small (delta ≈ +0.03 per 0.1 MPCR increase), and mostly manifest when other supports (communication, rewards) are present.
  - **Confidence: low–medium**

### Low-Confidence / Unstable Regions

- **Punishment "technology" (punishmentMagnitude/punishmentCost):**  
  - Weak and non-monotonic predictor. Doubling punishment efficiency can sometimes increase, decrease, or have no effect on group efficiency depending on other parameters.
  - **Confidence: low**

- **Peer outcome visibility and punisher identity:**  
  - Their effects are highly interaction-dependent; can encourage norm enforcement or retaliation.
  - **Confidence: low–medium**

- **Extreme ("corner-case") configs (e.g., low MPCR, high cost, no communication, all-or-nothing contributions):**  
  - Outcomes are unpredictable and highly variable, with efficiency changes ranging nearly from -50% to +40%.
  - **Confidence: low**

---

## Limitations & Open Questions

- **Extrapolation Risk:**  
  All predictions are most reliable *within* the sampled parameter space (see Table 1 of paper). Extrapolation to untested extremes or outside the 14-parameter bounds is risky.
- **Population Specificity:**  
  Results are robust across the online-lab participant pool used, but may differ with very different populations or cultures.
- **Rare Parameter Combinations:**  
  Some complex interaction effects (three-way or higher, especially with rare parameter sets) remain weakly supported; model confidence drops in such cases.
- **Long-term Dynamics:**  
  The experiment focused on games up to 20 rounds; longer timescales not directly tested.

---

## How To Use This For Predictions

- **Always input all 14 CONFIG variables AND the observed control-game efficiency**—models trained with these will outperform any rule-of-thumb.
- **Pay attention to communication and reward flags**: These are the best indicators for when punishment will have a positive or negative impact on efficiency.
- **Expect heterogeneity:** There is no region of the parameter space where punishment *always* helps or always hurts—context and interactions dominate.
- **Don’t overvalue punishment “tech” or cost-magnitude ratios:** These have far less predictive power than social/contextual parameters.
- **Use caution with edge cases:** If your CONFIG has rare or extreme feature combinations (e.g., all-or-nothing, no chat, high punishment cost), model predictions will have wider uncertainty.
- **When in doubt, anchor on the control efficiency**: Most cases of negative or zero additional effect of punishment occur when baseline efficiency is already high.
- **Interpret numeric predictions as *expectations*, not guarantees**: The same punishment parameters can cause an efficiency gain or loss depending on the social context set by the 14 CONFIGs.

---

**Summary Table: Example Guidance for Efficiency Change Upon Enabling Punishment**

| Communication | Rewards | Contribution Type | Framing    | Expected Efficiency Change | Confidence |
|---------------|---------|------------------|------------|--------------------------|------------|
| Off           | Off     | Any              | Any        | -0.05 (median)           | High       |
| On            | Off     | Variable         | Opt-out    | +0.08                    | Medium     |
| On            | On      | Variable         | Opt-out    | +0.12                    | High       |
| Off           | Off     | All/Nothing      | Opt-in     | -0.02                    | Medium     |
| Off           | On      | All/Nothing      | Any        | 0.00                     | Low        |
| Any           | Any     | Any              | Any        | See main text            | Use full model |

---

**Use model-based predictions for best accuracy. Rules above can be used for quick estimation/amplification of uncertainty for complex cases.**
