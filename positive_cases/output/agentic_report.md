# Predicting the Impact of Punishment on Efficiency in Public Goods Games

## Abstract

This report provides predictive guidance for estimating how enabling punishment changes efficiency in newly configured public goods games, drawing on comprehensive, paired experimental data and recent published findings. We synthesize evidence from a large-scale dataset (360 conditions; 147,000+ decisions) and outline actionable rules-of-thumb for model-based prediction. Key design parameters and their implications are mapped to the experimental protocol, highlighting the central relevance of context effects, namely communication, contribution framing/type, and peer transparency. While enabling punishment can alter group efficiency, its effect is highly variable—ranging from large gains to severe losses—depending primarily on contextual features rather than properties of the punishment system itself. The proposed approach leverages all 14 configuration parameters plus control game efficiency for accurate, config-sensitive prediction.

---

## Background & Definitions

Public goods games (PGGs) are canonical experimental paradigms in which participants make repeated decisions about how much of a private endowment to contribute to a group pool. Contributions are multiplied and redistributed, creating a social dilemma: individual rationality (free-riding) conflicts with collective welfare (full cooperation). To address persistent free-riding, many designs allow for “punishment” (costly sanctions) and/or rewards. 

**Efficiency** in this context is the primary welfare measure:  
> **Efficiency** = (Observed total group earnings) / (Total earnings if everyone contributed the maximum, every round, with no losses).

By construction, efficiency = 1 indicates full cooperation and zero wasted resources; lower values reflect cooperation shortfalls and/or additional welfare losses due to costly interventions (e.g., punishment/reward expenditures).

The key prediction task:  
> Given a set of design parameters (the CONFIG), and the average efficiency achieved in the “control” game (punishment disabled), what will the efficiency be in a matching “treatment” game (punishment enabled)?

---

## Data & Variables

The experimental dataset consists of 360 unique configurations, each defined by 14 systematically varied design parameters ("CONFIG"), plus a paired control/treatment structure for punishment. 

**CONFIG Parameters (14):**

1. **CONFIG_playerCount**: Number of players per group.
2. **CONFIG_numRounds**: Number of rounds played per game.
3. **CONFIG_MPCR**: Marginal per-capita return—how much each contributed coin returns to each player (multiplier divided by player count).
4. **CONFIG_allOrNothing**: Contribution mode (0: variable contribution; 1: all-or-nothing).
5. **CONFIG_chat**: Chat enabled? (0/1).
6. **CONFIG_defaultContribProp**: Contribution framing (0: opt-in, default is keep; 1: opt-out, default is contribute).
7. **CONFIG_punishmentCost**: Cost to punisher per unit of punishment.
8. **CONFIG_punishmentMagnitude**: Coins deducted from punished player per punishment unit.
9. **CONFIG_showOtherSummaries**: Other players’ outcomes shown? (0/1).
10. **CONFIG_showNRounds**: Is the total number of rounds shown to players? (0/1).
11. **CONFIG_showPunishmentId**: Is the identity of punishers revealed? (0/1).
12. **CONFIG_rewardExists**: Are rewards enabled? (0/1).
13. **CONFIG_rewardCost**: Cost per unit of reward.
14. **CONFIG_rewardMagnitude**: Benefit gained per unit of reward.

> **Additional Input**:  
> - **Control Efficiency**: Average efficiency in the punishment-off (control) variant of the game.

These variables encode the full design, allowing robust mapping from parameter space to observed behavior.

---

## Empirical Patterns (Punishment Effects & Heterogeneity)

### Average Punishment Effects

- **Punishment raises contributions**: On average, enabling punishment increases contribution rates from ~73–74% to ~80–82% of endowment.
- **But punishment often reduces efficiency**: Mean efficiency *drops* with punishment (normalized efficiency falls from 0.71 to 0.63 in the main data, and from 0.72 to 0.68 in validation).
    - This occurs because gains in cooperation are often offset (or exceeded) by the direct costs of punishment itself.

### Highly Context-Dependent Effects

- **Variance is extreme**: In some conditions, punishment intervention *raises* efficiency by up to 43%; in others, it *reduces* it by as much as 44%.
- **Distribution**: The effect is not bell-shaped. Rather, most configs cluster near no effect, with heavy tails in both positive and negative directions.
    - This means a model that predicts "small average effect" will fail badly in many plausible contexts.

### Dominant Moderators

- **Communication (Chat) is key**: Allowing players to communicate (CONFIG_chat=1) is the strongest positive moderator of punishment's beneficial effect; its presence changes the effect of punishment more than any system parameter.
- **Contribution framing & type**: Interactions between opt-in/opt-out framing, variable/all-or-nothing contributions, and outcome visibility produce sharply divergent effects.
    - For example, opt-out framing amplifies punishment's benefits with variable contributions, but *reduces* it under all-or-nothing, especially if peer outcomes are visible.
- **Reward system presence enhances punishment**: If rewards can also be given (CONFIG_rewardExists=1), punishment is more likely to be beneficial.
- **Punishment technology ("effectiveness") is surprisingly unimportant**: The ratio of magnitude to cost does *not* reliably predict the welfare effect of punishment.

---

## Predictive Guidance (Rules of Thumb & Feature Interactions)

Based on model and empirical results, we recommend the following predictive principles:

### 1. **Leverage Control Efficiency**
   - The observed efficiency in the no-punishment game is **the best single predictor** of efficiency with punishment enabled.
   - Most other features modulate *the difference* between control and treatment efficiency.

### 2. **Communication Effect Dominates**
   - If chat is enabled (**CONFIG_chat=1**), expect **much greater efficiency gains** from enabling punishment (or, at minimum, lower likelihood of catastrophic losses).
   - Without chat, predicted impact of punishment should be conservative or negative, unless other moderators are very favorable.

### 3. **Contribution Framing-Type Interactions**
   - **Variable contributions + opt-out framing (CONFIG_allOrNothing=0, CONFIG_defaultContribProp=1):**
      - Amplifies positive punishment effect, especially if peer summaries are hidden.
   - **All-or-nothing + opt-out + peer summaries visible (CONFIG_allOrNothing=1, CONFIG_defaultContribProp=1, CONFIG_showOtherSummaries=1):**
      - Punishment’s effectiveness is *harmed*, often producing net losses.
   - **Variable contribution + opt-in framing (CONFIG_allOrNothing=0, CONFIG_defaultContribProp=0):**
      - Moderately positive, but less so than opt-out.
   - **All-or-nothing + opt-in (CONFIG_allOrNothing=1, CONFIG_defaultContribProp=0):**
      - Neutral to mildly negative.

### 4. **Game Length Effect (if Chat Enabled)**
   - With chat enabled, increasing the number of rounds (CONFIG_numRounds) strengthens the positive effect of punishment.
   - Without chat, longer games do *not* improve punishment’s effect.

### 5. **Reward Mechanisms**
   - If rewards are available (CONFIG_rewardExists=1), punishment’s welfare impact is usually more likely to be positive, all else equal.

### 6. **Do Not Overweight 'Punishment Technology'**
   - Parameters like magnitude/cost (CONFIG_punishmentMagnitude, CONFIG_punishmentCost) are **not** strong predictors. Focus on social context mods.

### 7. **Peer Outcome Visibility**
   - If players can see each others’ outcomes (CONFIG_showOtherSummaries=1), it can either amplify or dampen punishment’s effect, contingent on contribution type and framing.

---

## Limitations & Open Questions

- **Model Generalization**: Though parameter space is broad, extrapolation outside tested ranges or protocols may not hold.
- **No Systematic Timing or Staging Analysis**: Time limits (contribution/outcome durations) were not tested as fundamental moderators in this dataset.
- **Reward System Interactions**: Fine-grained effects of complex reward+punishment combinations remain under-explored.
- **No "Moral" or Cultural Framing**: Results reflect incentives, not cultural or framing manipulations.
- **Inter-Individual/Group Variability**: The prediction task is for *average* group efficiency, not for outlier groups or individuals.

---

## How To Use This For Predictions

- **Always input all 14 CONFIG fields and the control (no-punishment) efficiency to your model.**
- **Expect the impact of enabling punishment to be highly context-sensitive; never assume uniform positive or negative effects.**
- **If chat is enabled, upweight your predicted gain in efficiency from punishment, especially for longer games.**
- **Check key interactions:**
    - Variable contribution + opt-out framing = higher benefit from punishment.
    - All-or-nothing + opt-out + peer visibility = likely net welfare *loss* with punishment.
- **Ignore punishment magnitude/cost as major outcome drivers, except in extreme outlier cases.**
- **Presence of reward mechanisms generally tips punishment’s effect toward positive.**
- **Default to E-Net or similar statistical models, but explicitly encode the above interaction logic for best predictive accuracy.**
- **Do not use global averages or naïve regression on punishment technology—context is king.**
- **If unsure, predict only minor adjustments from control efficiency (plus/minus 5–10%), unless chat or strong interaction effects are present.**
