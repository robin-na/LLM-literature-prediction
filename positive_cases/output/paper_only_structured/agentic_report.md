# How Enabling Punishment Affects Efficiency in Public Goods Games: Prediction-Support Guidance

## Abstract

This report synthesizes evidence from a large integrative experiment (360 Public Goods Game configurations) to inform predictive modeling of efficiency when punishment is enabled. Using only data from the experimental paper, we summarize the observed heterogeneity in punishment effects and clarify key moderators. We provide variable definitions, outline empirical patterns, offer quantitative effect ranges, and translate findings into operational rules of thumb. Guidance is structured to support settings where 14 configurational parameters and control efficiency are known. Concrete recommendations are tailored to drive predictive accuracy in new configurations.

---

## Background & Definitions

**Prediction Task:**  
Given a full set of 14 CONFIG parameters and the average efficiency for a specific control configuration (punishment disabled), predict the average efficiency for the same configuration when punishment is enabled.

- **Efficiency:** Ratio of total group earnings (with current contributions and settings) to what the group would earn if all members fully cooperated every round (no punishment/reward costs). Efficiency = 1 signals perfect cooperation; lower values indicate losses from under-contribution or costly sanctioning.
- Each prediction instance involves paired experimental designs: only punishment availability changes between the control and treatment arms.

---

## Data & Variables

### Key CONFIG Parameters (Prediction Inputs)

| Parameter Name            | Description                                                                                |
|--------------------------|--------------------------------------------------------------------------------------------|
| CONFIG_playerCount        | Number of players per group/game                                                           |
| CONFIG_numRounds          | Number of rounds played                                                                    |
| CONFIG_MPCR               | Marginal per-capita return = (multiplier) / (playerCount)                                 |
| CONFIG_allOrNothing       | Contributions: 1 = all-or-nothing (binary); 0 = continuous/variable contributions allowed |
| CONFIG_chat               | 1 = in-game chat enabled between group members; 0 = chat disabled                         |
| CONFIG_defaultContribProp | Framing: 0 = opt-in (default keep), 1 = opt-out (default contribute)                      |
| CONFIG_punishmentCost     | Resource cost to punish per unit                                                          |
| CONFIG_punishmentMagnitude| Points/coins deducted from a target per unit punishment                                   |
| CONFIG_showOtherSummaries | Visibility: are peer results shown at the end of each round?                              |
| CONFIG_showNRounds        | Is the total number of game rounds revealed to players?                                   |
| CONFIG_showPunishmentId   | Is the identity of punishers shown?                                                       |
| CONFIG_rewardExists       | 1 = reward option enabled, 0 = reward disabled                                            |
| CONFIG_rewardCost         | Cost to reward per unit                                                                   |
| CONFIG_rewardMagnitude    | Points/coins granted per unit reward                                                      |

**Note:**  
The experiment holds protocol and online environment constant; only CONFIG parameters vary to generate heterogeneity.

---

## Empirical Patterns

### Numeric and Pattern Evidence

- Enabling punishment generates **heterogeneous efficiency effects**:
    - Efficiency impact varies from a **43% increase** to a **44% decrease** across configurations.
- **Average pattern:**
    - Punishment _increases contributions_ but, due to associated costs, _often reduces overall efficiency_.
    - In the learning phase: normalized efficiency fell from 0.71 (no punishment) to 0.63 (punishment); an 11% decrease.
    - In the validation phase: normalized efficiency fell from 0.72 to 0.68; a 6% decrease.
    - Individual games exhibited _much larger increases or decreases_; context is key.
- **Social/contextual parameters dominate:**
    - **Communication (chat enabled)** is consistently the most important moderator (impact of shuffling parameter leads to a 60% jump in prediction error).
    - **Contribution framing** (opt-out vs. opt-in) has secondary importance, especially when contributions are variable.
    - **Game length** and **peer outcome visibility** interact strongly with these social features.
    - Variations in **punishment cost/effectiveness** have relatively weak main effects compared to social context.
- **Key interaction:** Longer games only increase punishment effectiveness if communication is present; outcome visibility can weaken this synergy.

---

## Quantitative Summary

**Observed Numerical Ranges:**

| Statistic                                    | Value / Range        | Note                              |
|----------------------------------------------|---------------------|-----------------------------------|
| Max observed efficiency increase (punishment)| +43%                | Best-case configs                 |
| Max observed efficiency decrease (punishment)| -44%                | Worst-case configs                |
| Mean normalized efficiency drop (learning)   | -0.08 (11% decline) | From 0.71 → 0.63                  |
| Mean normalized efficiency drop (validation) | -0.04 (6% decline)  | From 0.72 → 0.68                  |
| Chat effect                                 | Strong positive      | See Moderator Matrix              |
| Framing effect                              | Conditional positive | Especially for variable contribs  |
| MPCR effect                                 | Weak, consistent     | Limited predictive value          |
| Technological parameters (punishment tech)   | Null/negligible      | Not strong main effects           |

### Moderator Matrix

| Variable                     | Likely Effect Direction        | Confidence | Interaction Notes                                                             |
|------------------------------|-------------------------------|------------|------------------------------------------------------------------------------|
| CONFIG_chat                  | Strongly positive (if enabled)| High       | Magnifies all other positive effects.                                         |
| CONFIG_defaultContribProp    | Positive (opt-out > opt-in)   | High       | Only for variable contributions—not all-or-nothing.                           |
| CONFIG_allOrNothing          | Negative moderating effect     | High       | If true, framing benefit disappears.                                          |
| CONFIG_numRounds             | Positive (longer games)       | Medium     | Only if chat is enabled; effect weakens with high peer outcome visibility.    |
| CONFIG_showOtherSummaries    | Weakly negative               | Medium     | Mitigates gains from long games/communication.                                |
| CONFIG_MPCR                  | Weakly positive               | Low        | Small, consistent effect; not a strong moderator.                             |
| CONFIG_punishmentCost        | Minimal                       | Low        | Structural; weak/no main effect in models.                                    |
| CONFIG_punishmentMagnitude   | Minimal                       | Low        | Structural; weak/no main effect in models.                                    |
| CONFIG_showPunishmentId      | Unclear/weak                  | Low        | Not highlighted as important.                                                 |
| CONFIG_rewardExists          | Weak/unclear                  | Low        | Moderates less than punishment; not central.                                  |
| CONFIG_rewardCost/Magnitude  | Minimal                       | Low        | Weak effect; only relevant if reward is enabled.                              |
| CONFIG_playerCount           | Unreported effect             | Low        | Not directly discussed in paper memo.                                         |
| CONFIG_showNRounds           | Unclear                       | Low        | Only interacts for long games with communication.                             |

---

## Predictive Guidance

### Rules of Thumb

- **If** `CONFIG_chat = 1` (communication enabled), **then** expect punishment to have a positive or less negative effect on efficiency, especially for longer games.
- **If** `CONFIG_chat = 0` (no communication), **then** enabling punishment is likely to decrease efficiency, except in unusual parameter combinations.
- **If** `CONFIG_defaultContribProp = 1` (opt-out framing) **and** `CONFIG_allOrNothing = 0` (variable contributions), **then** expect a moderate boost to punishment’s efficiency effect.
- **If** `CONFIG_allOrNothing = 1`, **then** the benefit of opt-out framing is neutralized; do not expect increased efficiency from this framing.
- **If** `CONFIG_numRounds` is high **and** chat is enabled, **then** punishment is more effective; **but** if peer outcomes are highly visible (`CONFIG_showOtherSummaries = 1`), this benefit is weakened.
- **If** punishment cost/magnitude parameters vary, **then** do **not** expect these alone to reliably shift efficiency; social/contextual parameters are stronger predictors.
- **If** MPCR is very low, **then** only expect small changes from punishment unless altered alongside enabling chat or reframing contributions.

### Feature Interactions

- **Chat × NumRounds**: Significant—positive punishment effects in longer games only when chat is present.
- **Framing × AllOrNothing**: Framing increases efficiency only for variable contributions. No additive benefit under all-or-nothing structure.
- **Visibility × Social Features**: Peer outcome visibility can dampen or reverse the benefit of otherwise positive configurations.
- **Punishment Tech × Social Context**: Technical details matter much less than who can coordinate or communicate.

---

## Limitations & Open Questions

- **Lack of direct coefficients:** The paper reports qualitative and directionally quantified effects without publishing full regression weights or model formulas for numeric prediction.
- **Unreported parameters:** Some variables (e.g., playerCount, certain visibility settings) lack detailed effect size reporting in the paper, potentially important for edge cases.
- **Context sensitivity:** Model performance depends on interaction combinations; guidance above is based on observed patterns, not closed-form marginal effects.
- **Reward mechanisms:** Effects of rewarding are not fully detailed and are not central to the main patterns described.
- **Extreme values:** Outlier configurations can see -44% to +43% efficiency swings, but the paper does not specify which config vectors map to these boundaries.

---

## How To Use This For Predictions

- **Start with the control efficiency value.** All guidance predicts the *increment* or decrement to that baseline.
- **Check if chat is enabled** (`CONFIG_chat = 1`). This is the most important predictor of a positive punishment effect.
- **Identify contribution structure:**
    - Variable contributions? If yes, check framing; opt-out helps.
    - All-or-nothing? Ignore framing for prediction impact.
- **Assess game length and peer visibility:**
    - Long games only help with punishment if chat is also enabled.
    - High outcome visibility may lessen punishment’s effectiveness, even with otherwise positive settings.
- **Treat technical punishment parameters as minor unless in edge cases.**
- **In ambiguous configurations (few social/contextual moderators), predict a mild reduction in efficiency when enabling punishment.**
- **Document any parameter gap (where the control variable is unreported or ambiguous) and be cautious about extrapolating beyond reported ranges.**

---

**Table: Decision Checklist for New Prediction Instances**

| Step  | Action                                                                    |
|-------|---------------------------------------------------------------------------|
| 1     | Record control (no punishment) efficiency.                                |
| 2     | Note chat status; prioritize this cue.                                    |
| 3     | Check contribution and framing; apply interaction rules.                  |
| 4     | Examine game length and peer visibility; adjust prediction accordingly.   |
| 5     | Make only minor adjustments for changes in punishment cost/magnitude.     |
| 6     | Use rules of thumb for direction; select change magnitude within -44% to +43%, referencing main patterns (mean ≈ 6–11% decrease). |
| 7     | Aggregate adjustments; never override control efficiency beyond the empirically observed range. |

This guidance translates directly from published evidence and is operationalized for consistent application to new instances within the integrative experiment domain.
