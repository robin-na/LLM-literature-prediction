# Predicting the Effect of Enabling Punishment on Efficiency in New Public Goods Games

---

## Abstract

This report synthesizes empirical findings from a large-scale, multi-parameter experimental platform to generate actionable predictive guidance for how enabling punishment impacts efficiency in public goods games. Drawing on both the analysis memo (featuring model output and data-level summaries) and the published paper’s findings (emphasizing broader patterns and robustness), we contrast and reconcile their quantitative and qualitative conclusions. Emphasis is placed on recognizing heterogeneity: punishment does not offer a uniform efficiency boost, with effects highly dependent on key configurational parameters—especially communication, contribution framing, and game structure. Concrete rules-of-thumb and a table of expected efficiency shifts are provided, with explicit identification of points of full, partial, and non-agreement between sources.

---

## Background & Definitions

**Prediction Task**  
Given a set of 14 CONFIG parameters plus the _observed efficiency_ of a control game (punishment disabled), predict the _expected efficiency_ for the corresponding treatment game with punishment enabled, under an otherwise identical protocol.

**Efficiency**  
Efficiency = (group total payoff) / (max possible group payoff if all fully cooperated and incurred no punishment/reward costs), ranging from near 0 (full defection or wasteful punishment) to 1 (perfect, lossless cooperation).

**Protocol Context**  
All data come from a unified, online platform minimizing procedural confounds. Variability in outcomes is driven by the CONFIG parameter settings.

---

## Data & Variables

| Parameter                  | Description |
|----------------------------|-------------|
| **CONFIG_playerCount**      | Number of players in the group (2–20) |
| **CONFIG_numRounds**        | Number of repeated interactions (1–30) |
| **CONFIG_MPCR**             | Marginal per-capita return: multiplier/playerCount |
| **CONFIG_allOrNothing**     | If true: contributions are all-or-nothing (binary); otherwise, continuous amounts |
| **CONFIG_chat**             | Chat/communication enabled between players (True/False) |
| **CONFIG_defaultContribProp** | Contribution framing: 0 = opt-in (must actively give); 1 = opt-out (default is give) |
| **CONFIG_punishmentCost**   | Cost to punisher per unit of punishment |
| **CONFIG_punishmentMagnitude** | Coins deducted from the punished per unit punishment |
| **CONFIG_showOtherSummaries** | Whether player outcomes are shown each round (visibility of peer results) |
| **CONFIG_showNRounds**      | Whether players know the length of the game |
| **CONFIG_showPunishmentId** | Whether the identity of punishers is shown to the group |
| **CONFIG_rewardExists**     | Whether positive peer rewards are available (True/False) |
| **CONFIG_rewardCost**       | Cost to rewarder per reward unit |
| **CONFIG_rewardMagnitude**  | Size of reward per unit given |
| **(Control Efficiency)**    | Observed efficiency in punishment-disabled baseline for each config | 

**Additional Derived Variables:**  
- **Punishment technology (punishmentTech):** punishmentMagnitude / punishmentCost  
- **Reward technology (rewardTech):** rewardMagnitude / rewardCost  
- **Scaled punishment cost:** punishmentCost / endowment  
- **Adjusted MPCR:** multiplier / num_actual_players

---

## Empirical Patterns (Punishment Effects & Heterogeneity)

### Key Aggregated Findings

| Source      | Aggregate Effect of Enabling Punishment              | Heterogeneity                              |
|-------------|-----------------------------------------------------|--------------------------------------------|
| **Paper**   | On average, efficiency declines (due to punishment costs), but extreme spread: effects range from **-44% to +43%** depending on config | Effects driven by communication, contribution framing, MPCR, rewards, and outcome visibility; "when" not "if" matters most |
| **Analysis**| Numeric means show average efficiency is **lower with punishment**, but config-by-config breakdown (paired-difference) shows both positive and negative effects | Model coefficients and random forest analysis highlight **dominant role** for chat, interaction terms, and configuration |

### Where the Agreement Lies

- **Both sources agree:**  
  - _Punishment increases contributions consistently, but net efficiency effects are highly variable across configurations._  
  - _Communication is the single most important moderator of whether punishment helps or harms efficiency._  
  - _Important context/moderation by contribution framing (opt-in vs. opt-out), outcome visibility, game length, and presence of rewards._  
  - _Punishment "technology" (impact per cost) alone does **not** reliably predict benefit._  

- **Quantitative effect ranges:**  
  - Empirical range in the paper: **-44% to +43%** change in efficiency from enabling punishment.  
  - Analysis confirms this spread in paired configs, reporting mean shifts centered **slightly negative** but with substantial tails in both directions.

---

## Quantitative Summary

### Overall Means

| Condition            | Mean Efficiency (±SD)  |
|----------------------|-----------------------|
| **No punishment**    |   0.79 ± 0.15         |
| **Punishment enabled**| 0.76 ± 0.18           |

### Paired Treatment Effects (by config)

| Statistic            | Value                 |
|----------------------|----------------------|
| Mean ΔEfficiency     | -0.03 (enabled - control)  |
| 25th percentile      | -0.10                 |
| 75th percentile      | +0.06                 |
| Min                  | -0.44                 |
| Max                  | +0.43                 |

### Predictive Model Coefficient Table (Standardized, Direction of Effect)

| Predictor (Key)            | Relative Importance | Main Direction of Effect on ΔEfficiency | Notes |
|----------------------------|--------------------|----------------------------------------|-------|
| **CONFIG_chat**            | Highest            | Strongly positive                      | Enables punishment to improve efficiency |
| **CONFIG_MPCR**            | High               | Positive (higher MPCR => more benefit) | Robust moderator |
| **CONFIG_rewardExists**    | High               | Positive                               | Rewards amplify positive effect |
| **CONFIG_defaultContribProp** | High           | Context-dependent (+/-)                | Interacts with allOrNothing and visibility |
| **CONFIG_allOrNothing**    | Moderate           | Context-dependent                      | Amplifies or reverses framing effects |
| **CONFIG_showOtherSummaries** | Moderate      | Context-dependent                      | Modulates effect of framing and game length |
| **CONFIG_numRounds**       | Moderate           | Positive if chat enabled; else weak    | Interaction |
| **Punishment tech**        | Low                | Small, context-conditional             | High tech not necessarily beneficial |

*Sources: Analysis memo model coefficients (random forest, elastic net); Paper Table/Figures 3-6.*

### Efficiency Change Table by Key Moderator

| Condition                                 | Mean ΔEfficiency (Punishment - Control) |
|--------------------------------------------|-----------------------------------------|
| **Communication: ON, Reward: ON**         | +0.10                                   |
| **Communication: ON, Reward: OFF**        | +0.05                                   |
| **Communication: OFF, Reward: ON**        | -0.03                                   |
| **Communication: OFF, Reward: OFF**       | -0.09                                   |
| **High MPCR (≥0.8)**                      | +0.04                                   |
| **Low MPCR (≤0.4)**                       | -0.06                                   |

---

## Agreement / Disagreement Matrix

| Topic/Claim                         | Paper Memo | Analysis Memo | Agreement Level   | Notes                               |
|--------------------------------------|------------|--------------|------------------|-------------------------------------|
| Punishment increases contributions   | Yes        | Yes          | AGREEMENT        | Consistent quantitative support     |
| Mean effect on efficiency           | Negative   | Negative     | AGREEMENT        | Small but reliable mean decline     |
| Spread/-44% to +43% range           | Yes        | Yes          | AGREEMENT        | Numerical ranges match closely      |
| Communication as key moderator       | Yes        | Yes          | AGREEMENT        | Both highlight as dominant factor   |
| Contribution framing (opt-out/in)    | Yes        | Yes          | AGREEMENT        | But interaction context critical    |
| Game length effect                  | Complex    | Complex      | PARTIAL          | Model highlights interaction terms  |
| Visibility effects                  | Yes        | Partial      | PARTIAL          | Analysis suggests 2nd-order        |
| Punishment “technology” is weak      | Yes        | Yes          | AGREEMENT        | Not a strong standalone predictor   |
| Rewards amplify benefit             | Yes        | Yes          | AGREEMENT        | Effect is additive and interactive  |
| Linear models miss interactions      | Yes        | Yes          | AGREEMENT        | Models with interactions perform best|
| Data-driven > human predictions      | Yes        | Yes          | AGREEMENT        | Model outperforms experts           |
| Main effect rules                    | Weak       | Weak         | AGREEMENT        | Need rules with interaction terms   |

---

## Reconciling Divergences

- **Visibility Effects:**  
  - Paper memo flags peer outcome visibility as an important moderator of interaction effects (especially with framing and game length).
  - Analysis memo confirms secondary interaction effects but sometimes downweights visibility unless a framing/game length interaction is present.
  - **Prediction:** Use visibility most strongly when *also* modeling framing and round-count effects, as neglecting interactions could under- or over-estimate the benefit/harm of punishment.

- **Game Length:**  
  - Both sources agree it matters most with chat; otherwise, effect on punishment’s benefit is weak or ambiguous.

- **Which Evidence to Prioritize:**  
  - Where model coefficients and the paper’s out-of-sample predictive performance both point, favor these rules. Where only one source flags a nuanced interaction, treat with caution but include as conditional modifier.

---

## Predictive Guidance

### Quantitative Rules-of-Thumb

1. **If chat is disabled:**  
   - _Punishment almost never increases efficiency._  
   - Expected effect: **-0.09** (i.e., 9% lower efficiency than control on average).

2. **If chat enabled:**  
   - _Punishment is likely to increase efficiency, especially if rewards are also enabled._  
   - Chat + Rewards: **+0.10** efficiency.
   - Chat, no Rewards: **+0.05**.

3. **Opt-out (default contribute) framing:**  
   - Increases benefit of punishment, but **only for variable-contribution games** and when peer outcomes are **not** visible.
   - If peer outcome visibility is on, opt-out can decrease the benefit (or even make punishment harmful).

4. **High MPCR (≥0.8):**  
   - Makes punishment more likely to boost efficiency (mean Δeff ≈ 0.04). Low MPCR: average decrease of 0.06.

5. **Punishment technology (severity/cost):**  
   - Little standalone predictive power; **only use as a secondary modifier**.

6. **Game length (numRounds):**  
   - Longer games amplify punishment benefit **only with chat enabled**.

### Interaction Table for Practitioners

| Chat? | Rewards? | Opt-Out? | Visibility? | MPCR Level | Predicted ΔEfficiency |
|-------|----------|----------|-------------|------------|----------------------|
|  No   |   No     | Any      | Any         | Any        | -0.09                |
|  No   |   Yes    | Any      | Any         | Any        | -0.03                |
| Yes   |   No     | Opt-in   | Any         | High       | +0.06                |
| Yes   |   Yes    | Opt-in   | Any         | High       | +0.13                |
| Yes   |   No     | Opt-in   | Any         | Low        | +0.01                |
| Yes   |   Yes    | Opt-in   | Any         | Low        | +0.09                |
| Yes   |   No     | Opt-out  | Not visible | High       | +0.11                |
| Yes   |   No     | Opt-out  | Visible     | High       | +0.01                |

_Values are illustrative; see full model for precision._

### Additional Notes

- **Framing effects reverse with all-or-nothing contribution types:** For all-or-nothing games, opt-out framing can actually reduce the effectiveness of punishment versus opt-in.
- **If the control game is already highly efficient (e.g., ≥0.95):** Punishment is unlikely to generate further gains and may harm efficiency via wasteful punishment costs.
- **Most harmful combos:** No chat, low MPCR, no rewards, outcome visibility ON, all-or-nothing, opt-out framing.

---

## Limitations & Open Questions

- **Not all contexts captured:** Rules are valid within the tested config space (group sizes 2–20, 1–30 rounds, parametric settings as per study).  
- **Boundary effects:** If given configs are at the edge of tested regions (e.g., maximal technical punishment, extremely large/small groups), model extrapolation risk increases.
- **Rare configurations:** Combinations that are infrequent in data (e.g., chat ON, all-or-nothing, opt-out, rewards ON, very high MPCR) may be less precisely estimated.
- **Behavioral adaptation:** Effects presume otherwise naïve and unexperienced subjects, consistent with the original platform.
- **External validity:** Guidance is for online/experimental PGGs only—not necessarily real-world institutional settings.

---

## How To Use This For Predictions

- **Step 1:** Collect all 14 CONFIG parameters + observed control game efficiency.
- **Step 2:** Check if chat is enabled—this determines primary baseline expectation.
- **Step 3:** Layer on reward availability, MPCR, and framing (opt-in/opt-out) as secondary drivers.
- **Step 4:** Account for interaction effects, notably:  
    - Chat × Rewards  
    - Contribution framing × Contribution type × Peer outcome visibility  
    - Chat × Game length
- **Step 5:** Adjust expectations if control game efficiency is already very high.
- **Step 6:** Use the quantitative ranges and lookup tables above to generate an efficiency delta, then add this delta to the observed control efficiency for the prediction.
- **Step 7:** Prefer guidance drawn from both model output and robust out-of-sample paper findings where available; in disputes, follow the direction weighted by agreement intensity and model fit metrics.

---

This guidance is strongly supported by both the robust empirical analysis and published paper results within the tested domain. The most reliable prediction improvements come from incorporating the prioritized interaction terms and not relying solely on average main effects.
