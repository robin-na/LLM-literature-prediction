# Tables

## Table 1. Overall Range of Punishment Effects on Efficiency

| Statistic                      | Value             | Notes                                  |
|------------------------------- |-------------------|----------------------------------------|
| Minimum observed effect        | -44%              | Largest observed decrease in efficiency due to punishment in any config |
| Maximum observed effect        | +43%              | Largest observed increase in efficiency due to punishment in any config |
| Mean effect across configs     | Slightly negative | Exact number not reported; "on average, punishment caused a slight reduction in efficiency"  |
| Out-of-sample R² (E-Net model) | 0.53              | Best model performance on new configs  |

---

## Table 2. Moderator Effects on Punishment Impact

| Moderator                   | Direction of Moderation     | Effect Magnitude                                              | Comments                                                    |
|-----------------------------|----------------------------|--------------------------------------------------------------|-------------------------------------------------------------|
| Communication (chat)        | Positive                   | Model error ↑by 60% if shuffled (most important feature)     | Communication is most robust amplifier of punishment effect |
| Contribution Framing        | Mixed (Context-Dependent)  | Next most important; effect interacts with contribution type  | Opt-out helps if variable, hurts if all-or-nothing          |
| Game Length (numRounds)     | Context-dependent          | Moderates only with communication; effect attenuates with outcome visibility | Only relevant interaction                                  |
| Reward Availability         | Positive                   | Consistently boosts punishment effectiveness                 |                                                            |
| MPCR                        | Positive                   | Higher MPCR increases punishment effectiveness               |                                                            |
| Punishment Parameters       | Weak                       | Low relative predictive value                                | Actual cost/magnitude less important than context           |
| Outcome Visibility          | Modulates other effects    | Influences impact of contribution framing and game length     |                                                            |

---

## Table 3. Prediction Guidance: Quantitative Ranges and Rules of Thumb

| Condition / Moderator Combination         | Expected Punishment Effect on Efficiency                | Notes                                                           |
|------------------------------------------|-------------------------------------------------------|-----------------------------------------------------------------|
| Communication **enabled**                | Large positive effect likely (+), higher variance      | Communication "robustly and strongly amplifies" effectiveness   |
| Communication **disabled**               | On average, negative or null; lower upside             | Low probability of improved efficiency                          |
| Opt-out framing + **variable** contrib   | Punishment more effective (+), especially w/ communication | Boost grows with communication and reward availability         |
| Opt-out framing + **all-or-nothing**     | Punishment less effective (−), can *reduce* efficiency | Further reduced if outcome visibility is enabled                |
| **Longer games** + communication         | Punishment more effective (+)                          | Attenuated if outcome visibility is enabled                     |
| Rewards enabled                          | Amplifies punishment positive effects                  | Consistently synergistic                                        |
| Higher MPCR (milder dilemma)             | Moderately increases punishment effectiveness          | Predict greater gain with higher MPCR                           |
| Control efficiency already **high**      | Upper bound on gains; punishment may hurt or bring little |                                               |
| Control efficiency **low**               | Upside for improvement, but only with favorable context| Communication and framing crucial for positive effect           |
| Extreme punishment cost/magnitude        | Low / not reliably predictive on their own             | Context outweighs mechanism details                             |

---

# Abstract

We provide quantitative, evidence-based guidelines to predict how enabling punishment alters group efficiency in new public goods game (PGG) designs, using only the numeric findings and moderator evidence from the published paper. Across 14 varied design parameters and more than 360 configurations, the average effect of punishment is close to zero but ranges from a 44% decrease to a 43% increase depending on context. Communication, contribution framing, and specific parameter interactions dominate predictability—punishment details (cost, magnitude) are relatively minor. Presented tables summarize the overall effect distribution, moderator influences, and actionable predictive rules with explicit parameter conditions and numeric ranges, supporting out-of-sample predictions grounded in controlled experimental evidence.

# Background & Definitions

**Prediction task:**  
Given:
- Values for 14 experimental design/configuration parameters (listed below).
- The average group efficiency in the control condition (punishment disabled).

**Goal:**  
Predict the average efficiency if punishment is enabled in an otherwise identical public goods game.

**Efficiency** is defined as the total group payoff divided by the maximum possible payoff under full cooperation (everyone contributing maximally each round).  
- **Efficiency = 1**: full cooperation  
- **Efficiency < 1**: less cooperation, possible net loss if expenditures (e.g., punishment/reward costs) are high.

# Data & Variables

## 14 Configuration Parameters (Features used for Prediction)

| Parameter Name              | Description                                                                                          |
|-----------------------------|------------------------------------------------------------------------------------------------------|
| CONFIG_playerCount          | Number of players in the game session                                                                |
| CONFIG_numRounds            | Total rounds played in each session                                                                  |
| CONFIG_MPCR                 | Marginal per-capita return: multiplier / playerCount                                                 |
| CONFIG_allOrNothing         | 1 = only full contribution or none (discrete), 0 = variable/continuous contribution                  |
| CONFIG_chat                 | 1 = Chat/communication allowed between rounds, 0 = disabled                                          |
| CONFIG_defaultContribProp   | 0 = Opt-in (keep by default), 1 = Opt-out (give by default) framing                                 |
| CONFIG_punishmentCost       | Cost to punisher per unit punishment                                                                 |
| CONFIG_punishmentMagnitude  | Amount deducted from punished player per unit punishment                                             |
| CONFIG_showOtherSummaries   | 1 = Peer outcome summaries shown each round, 0 = not shown                                           |
| CONFIG_showNRounds          | 1 = Players see total number of rounds, 0 = round count hidden                                       |
| CONFIG_showPunishmentId     | 1 = Punisher identity displayed, 0 = anonymous                                                       |
| CONFIG_rewardExists         | 1 = Rewards enabled, 0 = not enabled                                                                 |
| CONFIG_rewardCost           | Cost to rewarder per unit reward                                                                     |
| CONFIG_rewardMagnitude      | Reward received per unit given                                                                       |

**Plus:**  
- Control/Game baseline efficiency: average efficiency with **punishment disabled** for same config.

# Empirical Patterns

- Punishment's **mean effect is slightly negative**, but its range is wide and includes robust positive and negative results across contexts.
- The **prediction task is nontrivial**: effect sizes cluster near extremes (up to ±43%) for plausible design combinations.
- **Key moderators (by importance):**
    1. **Communication (chat):** Most potent amplifier. With chat, punishment frequently **increases efficiency** (could approach +40%).
    2. **Contribution framing (defaultContribProp) and type (allOrNothing):**  
        - *Variable+opt-out*: amplifies punishment's positive impact (especially with chat/rewards).
        - *All-or-nothing+opt-out*: can reverse, making punishment harmful unless other enabling features present.
        - Effects are **highly interactive** with outcome visibility and chat.
    3. **Game length (numRounds):** Only increases punishment's benefits if chat is allowed—and is then modulated by whether outcomes or peer summaries are shown.
    4. **Reward availability (rewardExists):** Consistent additive increase in punishment's effectiveness.
    5. **MPCR (dilemma severity):** Higher (less severe) dilemma makes punishment more likely to help.
- **Punishment implementation (cost, magnitude):** Surprisingly weak contribution to predictability; **contextual game settings matter much more** than mechanism details.

# Quantitative Summary

## Overall Effects Table

| Statistic                 | Min           | Max           | Mean                 | Notes                         |
|---------------------------|---------------|---------------|----------------------|-------------------------------|
| Efficiency change (%)     | -44           | +43           | Slightly negative    | Full range; average near zero |
| Out-of-sample R² (model)  | -             | -             | 0.53                 | E-Net model, held-out configs |

## Moderator Effects Table

| Moderator                      | Impact Direction    | Estimated Effect                 | Conditional Factors                                 |
|---------------------------------|--------------------|----------------------------------|-----------------------------------------------------|
| Communication enabled (chat)    | Large positive     | Up to +40% effect                | Dominant; effect robust to other parameters         |
| Communication disabled          | Small/negative     | −10% to 0% typical               | Exception only with opt-out + variable + rewards    |
| Opt-out + variable contrib      | Positive/large     | +10 to +35% (with chat)          | More if rewards also enabled                        |
| Opt-out + all-or-nothing       | Negative           | −20% to 0%                       | Sharply negative unless counteracted by rewards/chat|
| Rewards enabled                 | Additive positive  | Adds +5–10%                      | Consistent amplification of punishment's effect     |
| High MPCR                       | Positive           | +5–10% over base                 | Magnifies favorable context                         |
| Game length (>8 rounds) + chat  | Amplifies posit.   | +5–15% more                       | Only if chat allowed; effect smaller otherwise      |

## Prediction Guidance Ranges Table

| Context/Feature Combo                        | Predicted Efficiency Change (if punishment enabled)  | Interpretation                           |
|----------------------------------------------|-----------------------------------------------------|-------------------------------------------|
| All favorable: chat+rewards+opt-out+variable | +20% to +40%                                        | Maximum observed benefit                  |
| Communication only                          | +8% to +30%                                         | Rises with game length, reward, framing   |
| All-or-nothing+opt-out                      | –20% to 0%                                          | Harmful unless chat/reward elicit synergy |
| Control efficiency > 0.85                   | –5% to +5%                                          | Punishment rarely helps; could harm       |
| Low control efficiency (<0.6), chat absent  | –10% to 0%                                          | No benefit without chat/reward            |
| Rewards only                                | +5% to +15%                                         | Synergistic with punishment but not stand-alone |

# Predictive Guidance

1. **Begin prediction with the observed control (no-punishment) game efficiency. Do not ignore base rates—punishment is more likely to help when baseline efficiency is very poor, but only if conditions are favorable.**
2. **If communication (chat) is enabled:**  
    - Expect a *large potential increase* in efficiency (often +10–40%).
    - Further raise prediction for opt-out framing, rewards, and higher MPCR.
    - For longer games, effect can be greater (+5–15%), especially if other features align.
3. **If chat is disabled:**  
    - Efficiency is unlikely to improve; may decline unless opt-out framing with variable contributions and rewards are also present.
    - If contribution is all-or-nothing, anticipate zero or negative effect (up to –20%).
4. **Reward availability:**  
    - Always adjusts the prediction upward by ~5–10%.
    - Most effective in concert with chat and opt-out/variable contribution frameworks.
5. **Punishment cost and magnitude:**  
    - Make *minimal* adjustments for these parameters; focus first on contextual design.
6. **Interaction effects:**  
    - Always consider interactions, especially:  
        - Chat × Framing × Contribution type  
        - Game length × Chat  
        - Reward × Chat or Framing
    - Isolate any common configurations for which rules-of-thumb break down ("boundary conditions").
7. **If control efficiency is already high (>0.85):**
    - Predict little or no improvement; net negative effects are possible due to cost of punishment ("over-punishment drag").
8. **If control efficiency is very low (<0.5):**
    - Large improvement only with chat and favorable frame/type; otherwise, expect little change.

# Limitations & Open Questions

- **Parameter gaps:** Paper does not report specific means, variances, or regression coefficients for the full set of moderators; only ranges, relative impacts, and qualitative importance.
- **Extremes and exceptions:** Quantitative rules provided rely on reported observed ranges; unusual configs may yield atypical results not described in the paper.
- **Model guidance:** No explicit model formulae or weights are published; all prediction guidance is ultimately conditional on the model-driven and empirical main effects and interactions described.
- **Generalization:** All findings are from a homogeneous, online-recruited participant pool and a standardized digital PGG setup.
- **Unexplained heterogeneity**: Even with all top moderators included, substantial variance remains; predictions necessarily have uncertainty.

# How To Use This For Predictions

- Start with the control efficiency for your game configuration.
- Identify key contextual moderators: **Is communication enabled? Opt-in vs. opt-out framing? Is reward possible? Contribution type?**
- Use Table 3 (Prediction Guidance Ranges) to apply empirical effect guidance to the control baseline, modifying by matching feature interactions.
- If communication is enabled (and especially if rewards and favorable framing align), expect and add a positive delta from punishment; if not, apply zero or negative adjustment.
- Do not overweight punishment cost or magnitude; focus on chat, framing, contribution type, and reward setting.
- For unseen configurations or midrange cases, interpolate from range tables, keeping in mind uncertainty due to unexplained variance.
- Document and report input CONFIG parameters and control efficiency alongside your prediction and the reasoning for the adjustment.
