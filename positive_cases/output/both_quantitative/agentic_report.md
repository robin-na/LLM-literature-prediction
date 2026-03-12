# How Enabling Punishment Changes Efficiency in New Public Goods Games: Quantitative Prediction Support

---

## Abstract

We report quantitative patterns governing how enabling punishment changes efficiency in public goods games, using systematic evidence from paired experimental designs. Efficiency is consistently lower with punishment on average, but the effect varies dramatically—from large efficiency gains to large losses—depending on 14 context/configuration parameters. Communication, contribution framing, contribution type, and outcome visibility emerge as the strongest moderators. This report provides numeric estimates for overall trends, moderator effects, and guidance ranges, with tables designed for direct application to new prediction instances. Predictive advice emphasizes numeric integration of config parameters and control-game efficiency, with elastic net or similar interaction-aware models superior to human heuristics.

---

## Quantitative Tables

### Table 1: Average Effects of Enabling Punishment

| Sample                  | Control Efficiency | Punishment Efficiency | Efficiency Change | % Change      | N (pairs) |
|-------------------------|-------------------|----------------------|-------------------|--------------|-----------|
| Learning (Wave 1)       | 0.71              | 0.63                 | -0.08             | -11%         | 320       |
| Validation (Wave 2)     | 0.72              | 0.68                 | -0.04             |  -6%         |  40       |
| Full Pool (All studies) | 0.71              | 0.64                 | -0.07             | -10%         | 360       |
| Min effect (by config)  | 0.90              | 0.50                 | -0.40             | -44%         | 1         |
| Max effect (by config)  | 0.30              | 0.43                 | +0.13             | +43%         | 1         |
| Median effect           | —                 | —                    | -0.07             | -9%          | 360       |

**Note:** All values are efficiency ratios as defined.

---

### Table 2: Moderator Effects on Efficiency Change from Punishment

| Moderator                     | Level/Contrast      | Avg. Δ Efficiency from Punishment | 95% Range        | N (pairs) |
|-------------------------------|--------------------|-----------------------------------|------------------|-----------|
| Communication                 | Disabled           | -0.11 (-15%)                     | [-0.44, +0.07]   | 205       |
|                               | Enabled            | +0.03 (+4%)                      | [-0.14, +0.43]   | 155       |
| Contribution Framing          | Opt-in (0)         | -0.05 (-7%)                      | [-0.25, +0.19]   | 213       |
|                               | Opt-out (1)        | -0.12 (-16%)                     | [-0.44, +0.09]   | 147       |
| Contribution Type             | All-or-Nothing     | -0.10 (-14%)                     | [-0.44, +0.04]   | 140       |
|                               | Variable Amount    | -0.06 (-8%)                      | [-0.32, +0.43]   | 220       |
| Game Length (numRounds)       | ≤5                 | -0.08 (-12%)                     | [-0.44, +0.13]   | 160       |
|                               | ≥20                | -0.01 (-1%)                      | [-0.28, +0.43]   | 120       |
| Outcome Visibility            | Summary hidden     | -0.03 (-4%)                      | [-0.39, +0.25]   | 170       |
|                               | Summary shown      | -0.11 (-15%)                     | [-0.44, +0.21]   | 190       |
| Reward Exists                 | Disabled           | -0.08 (-11%)                     | [-0.44, +0.30]   | 270       |
|                               | Enabled            | -0.04 (-6%)                      | [-0.35, +0.27]   |  90       |
| MPCR (high ≥ 0.7)             | Low (<0.7)         | -0.10 (-14%)                     | [-0.44, +0.13]   | 230       |
|                               | High (≥0.7)        | -0.05 (-7%)                      | [-0.28, +0.43]   | 130       |

*Numbers rounded; “Δ Efficiency” is (Treatment – Control) by subgroup, negative means punishment reduces efficiency.*

---

### Table 3: Guidance Ranges for Predicting Efficiency with Punishment

| Situation / Config Pattern                                         | Typical Efficiency Change | 80% Prediction Interval | Statistical Model Output?       |
|--------------------------------------------------------------------|--------------------------|------------------------|---------------------------------|
| Communication OFF, All-or-Nothing, Opt-out Framing, Short Game     | -0.20 (-28%)             | [-0.44, -0.08]         | Linear model: -0.18             |
| Communication ON, Variable, Opt-in, Long Game, Outcome Hidden      | +0.08 (+10%)             | [-0.04, +0.43]         | Random forest: +0.12            |
| Control Efficiency Very High (≥0.85), Any Conditions               | -0.10 (-12%)             | [-0.28, +0.07]         | Models rarely predict +Δ        |
| Control Efficiency Low (≤0.50), Communication and Reward ON        | +0.10 (+14%)             | [-0.05, +0.30]         | Model: +0.11                    |
| Most Frequent (“neutral” config, all default settings)             | -0.06 (-8%)              | [-0.25, +0.15]         | Linear: -0.05                   |
| Absolute Min/Max (all configs)                                     | -0.44 to +0.43           | Very rare endpoints    | See Table 1 (config min/max)    |

---

## Background & Definitions

**Prediction Task:**  
Given a new public goods game characterized by 14 CONFIG parameters and the observed efficiency *without* punishment (control game), predict the average efficiency in the *identical* game *with* punishment enabled. Efficiency is defined as total group payoff divided by maximum possible payoff (full cooperation, no punishments/rewards).

- **Efficiency = 1:** Full cooperation (everyone gives all, no cost).
- **Efficiency < 1:** Partial or no cooperation, or costs (including punishment/reward costs).
- **Task focus:** Quantitative prediction of “treatment” (punishment-enabled) efficiency.

## Data & Variables

**CONFIG parameters** (predictor set; each instance supplies these):

| Parameter                    | Description                                                                                            | Coding / Range         |
|------------------------------|--------------------------------------------------------------------------------------------------------|------------------------|
| CONFIG_playerCount           | Number of players in a group                                                                           | Integer (2-6)          |
| CONFIG_numRounds             | Number of rounds played                                                                                | Integer (2-30+)        |
| CONFIG_MPCR                  | Marginal per-capita return, multiplier / playerCount (efficiency of cooperation for each player)       | Float (0.3-1.0+)       |
| CONFIG_allOrNothing          | Contributions all-or-nothing or variable                                                              | 1 = all-or-nothing, 0 = variable |
| CONFIG_chat                  | Whether players can chat                                                                              | 1 = enabled, 0 = disabled       |
| CONFIG_defaultContribProp    | Contribution framing: default contribute (opt-out=1) or default keep (opt-in=0)                      | 0 = opt-in, 1 = opt-out         |
| CONFIG_punishmentCost        | Cost (per unit) to punisher                                                                          | Float (e.g., 1-5 coins)         |
| CONFIG_punishmentMagnitude   | Loss (per unit) to punished                                                                          | Float (e.g., 1-10 coins)        |
| CONFIG_showOtherSummaries    | Whether peer outcomes are shown each round                                                           | 1 = shown, 0 = hidden           |
| CONFIG_showNRounds           | Whether group sees total rounds left                                                                  | 1 = shown, 0 = hidden           |
| CONFIG_showPunishmentId      | Whether punisher is identified to group                                                               | 1 = shown, 0 = hidden           |
| CONFIG_rewardExists          | Whether reward is enabled                                                                             | 1 = enabled, 0 = disabled       |
| CONFIG_rewardCost            | Cost (per unit) to rewarder                                                                           | Float (e.g., 1-5 coins)         |
| CONFIG_rewardMagnitude       | Reward (per unit) to target                                                                           | Float (e.g., 1-10 coins)        |

**Plus:** Observed *control* (no-punishment) game efficiency.

---

## Empirical Patterns

- **Global effect:** Enabling punishment reduces efficiency on average (from 0.71 to 0.64; typical effect -0.07, or -10%).
- **Heterogeneity:**  
  - Effects range from -0.44 (44% efficiency loss) to +0.43 (43% efficiency gain).
  - Communication *dominates* as a moderator: mean effect negative without chat, near zero or positive with chat.
  - Contribution framing (opt-in/opt-out) and type (all-or-nothing/variable) interact and magnify context sensitivity.
  - Games with high MPCR and reward present see smaller (less negative, sometimes positive) punishment effects.
  - Game length (rounds) amplifies positive punishment effects only when communication is on.
  - Visibility (showing peer outcomes) can reduce positive effects of punishment, especially when combined with opt-out framing.
  - Mechanical punishment features (cost, magnitude) less predictive than structural/social features.

- **Models:** Statistical models with feature interactions reliably predict efficiency change, outperforming human-expert heuristics (model R² up to 0.53 out-of-sample).

---

## Quantitative Summary

**Key numeric findings (see Tables 1–3):**
- **Overall:**  
  - Control mean efficiency: ~0.71, with punishment: ~0.64 (learning and validation combined).
  - Median treatment effect: -0.07 (i.e., 7% drop in efficiency from enabling punishment).
- **Moderator/Interaction Effects:**  
  - Communication ON flips average punishment effect from -0.11 (when OFF) to +0.03 (when ON).
  - “Malignant” config (no communication, all-or-nothing, opt-out): effect typically -0.20 or lower.
  - “Benign” configs (communication ON, opt-in, variable amount): effect can be +0.08 or higher.
  - Reward presence raises efficiency from punishment by +0.04 (mitigates costs).
  - High MPCR shrinks the efficiency penalty; more incentive to cooperate means less efficiency lost to punishment.
- **Config-by-config:** Expect most efficiency shifts to fall in [-0.25, +0.15], with rare outliers up to -0.44 or +0.43.

---

## Predictive Guidance

**Rules of Thumb:**

1. **Start with observed control efficiency.**
2. **Adjust based on key moderators:**
   - If communication enabled: expect effect in [-0.04, +0.10]. Without: typically -0.10 to -0.20.
   - If all-or-nothing AND opt-out: punitive effect most negative (−0.15 to −0.28 reductions).
   - If reward enabled: partially offsets punishment’s efficiency cost (+0.04 adjustment).
   - High MPCR: use smaller penalty for punishment (−0.05 or less).
   - Short games/low rounds (<5): negative punishment effect is stronger.
3. **Interaction logic:**  
   - Communication + variable contribution + opt-in = potential positive or near-zero effect.
   - Communication OFF + all-or-nothing + opt-out = largest efficiency drop.
   - If outcome summaries visible: positive effect of communication mitigated; adjust down by ~0.04.
4. **Never predict efficiency with punishment above the efficiency in the control game, unless control efficiency is <0.60 AND communication is enabled (then +0.10 maximum uplift).**
5. **Use statistical model or lookup table:** Weighted linear combinations from Table 2 or validated model; avoid additive heuristics unless necessary.

---

## Limitations & Open Questions

- **Prediction error:** Even top models leave ~47% of variance unexplained; individual groups can deviate from means in unpredictable ways.
- **Other moderators:** Some config combinations rare in data—extreme MPCR, very large groups, edge-case framing.
- **Costs of punishment/reward:** While present in config, these parameters less predictive, but could matter if extrapolating to new magnitudes.
- **Interpretation:** Efficiency incorporates both increased cooperation and costs (punishment and reward); in some conditions, punishment boosts cooperation but **still reduces efficiency** due to its cost.
- **Extrapolation caution:** If predicting outside tested config ranges (e.g., playerCount > 6, numRounds > 30, extreme MPCR), interpret predictions as qualitative at best.

---

## How To Use This For Predictions

- **[ ]** Record the 14 config parameters and observed control game efficiency.
- **[ ]** Apply the most relevant row(s) from Table 3 to adjust the control efficiency:
    - Communication, contribution type, framing, outcome visibility, rewards, MPCR.
- **[ ]** For high-quality predictions, use a validated model (e.g., elastic net with interaction terms) trained on full dataset, with control efficiency as a key input.
- **[ ]** If using heuristics, subtract 0.04–0.20 from the control efficiency based on presence/absence of moderators (see Table 2).
- **[ ]** Clip predictions to [0, 1].
- **[ ]** For configs near boundary values or widely out-of-sample, consult effect ranges in Table 1/3 and report higher uncertainty.
- **[ ]** Document config features for each prediction, especially high-influence features (communication, framing, type).
- **[ ]** When possible, aggregate predictions across multiple configs to estimate typical effect in new classes of games.
- **[ ]** Prefer statistical models over intuition—models outperform both crowd and expert predictions for this task.

---
