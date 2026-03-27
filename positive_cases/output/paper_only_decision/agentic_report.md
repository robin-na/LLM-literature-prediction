# Prediction-Support Report: Impact of Enabling Punishment on Efficiency in Public Goods Games

---

## 1. Title

**Estimating the Efficiency Impact of Enabling Punishment in Public Goods Games: Evidence-Based Guidance**

---

## 2. Abstract

This report synthesizes evidence from a large-scale integrative experiment systematically varying 14 public goods game (PGG) design parameters to support prediction of efficiency change when punishment is enabled. Highlighting strong empirical heterogeneity, the findings indicate that punishment can both increase or decrease group efficiency based on key contextual moderators. Predictive models using detailed game configuration and control efficiency outperform human experts. Guidance is provided only where directly supported by empirical evidence.

---

## 3. Background & Definitions

- **Prediction Task:**  
  For each new instance, given 14 CONFIG parameters and the average efficiency of the control condition (punishment disabled), predict the average efficiency of the same game when punishment is enabled.
- **Efficiency Definition:**  
  Efficiency = Group’s total payoff / Total payoff possible with full cooperation every round (efficiency = 1 is fully cooperative; lower values are less cooperative).
- **Goal:**  
  Predict direction and magnitude of the efficiency change due to enabling punishment, respecting only empirically validated relationships.

---

## 4. Data & Variables

**Design:**
- 360 unique game conditions, 147,618 decisions from 7,100 participants.
- Two phases: (1) Learning (broad, one-shot per config), (2) Validation (precise, multiple trials per config).

**Key Predictive Variables (CONFIG parameters):**
| Name                        | Description                                                                |
|-----------------------------|----------------------------------------------------------------------------|
| CONFIG_playerCount          | Number of players in the game                                             |
| CONFIG_numRounds            | Number of rounds per game                                                 |
| CONFIG_MPCR                 | Marginal per-capita return = multiplier / player count                    |
| CONFIG_allOrNothing         | If True, contributions are all-or-nothing (vs. continuous)                |
| CONFIG_chat                 | Chat enabled between players                                              |
| CONFIG_defaultContribProp   | 0 = opt-in (default keep), 1 = opt-out (default contribute)               |
| CONFIG_punishmentCost       | Cost to punisher per unit of punishment                                   |
| CONFIG_punishmentMagnitude  | Loss to punished per unit of punishment                                   |
| CONFIG_showOtherSummaries   | Are peer outcomes (earnings, punishments/rewards) shown?                  |
| CONFIG_showNRounds          | Is the total number of rounds shown?                                      |
| CONFIG_showPunishmentId     | Are punished/rewarded identities shown?                                   |
| CONFIG_rewardExists         | Is reward (positive sanctioning) enabled?                                 |
| CONFIG_rewardCost           | Cost to rewarder per unit of reward                                       |
| CONFIG_rewardMagnitude      | Gain to rewarded player per unit of reward                                |
| CONFIG_punishmentExists     | Is punishment enabled? (Distinguishes control/treatment)                  |

**Measured Outcome:**
- Efficiency in control (punishment disabled) and treatment (punishment enabled) games.

---

## 5. Empirical Patterns (Punishment Effects & Heterogeneity)

- **Overall:**
  - On average, enabling punishment *reduced* normalized efficiency by 11% in learning experiments and by 6% in validation experiments.
  - However, individual game conditions saw effects from −44% (decrease) to +43% (increase) in normalized efficiency.
  - Substantial statistically significant heterogeneity directly attributable to CONFIG parameters, not random or population noise.

- **Key Moderators (from model feature importance and SHAP analysis):**
  - **Communication (chat):** The most predictive and robust moderator; enabling chat makes positive punishment effects far more likely.
  - **Contribution Framing (defaultContribProp, opt-out vs. opt-in):** Enhances punishment effectiveness (increases efficiency) when contributions are variable, but *reduces* it in all-or-nothing settings; peer outcome visibility amplifies these effects.
  - **Contribution Type (allOrNothing):** Strongly interacts with framing.
  - **Game Length (numRounds):** Longer games only enhance punishment’s effect when chat is enabled; effect is weaker if peer outcome visibility is on.
  - **Peer Outcome Visibility (showOtherSummaries):** Can dampen positive punishment effects, especially for all-or-nothing contributions with opt-out defaults.
  - **Reward Exists:** Consistently enhances the efficiency impact of punishment.
  - **MPCR:** Higher values (less collective/individual conflict) slightly enhance positive impact of punishment but effect is small.
  - **Punishment ‘technologies’ (cost/magnitude):** Mild/no main effects observed; efficiency changes more contingent on context than on punishment mechanics themselves.

---

## 6. Predictive Guidance

### Moderator Matrix

| Variable               | Likely Direction of Moderation         | Confidence | Evidence Note                                                                   |
|------------------------|----------------------------------------|------------|---------------------------------------------------------------------------------|
| Communication (chat)   | Strongly increases positive effect     | High       | Most important feature; always positive when enabled                             |
| Contribution Framing   | Mixed (↑ for variable, ↓ for all-or-n)| High       | Strong effect, but contingent on contrib type & visibility                       |
| Contribution Type      | Modulates framing effect               | High       | See above                                                                        |
| Game Length            | ↑ only if chat enabled                 | Moderate   | No effect if no chat; weaker if outcomes visible                                 |
| Outcome Visibility     | Can dampen positive effect             | Moderate   | Negative mainly in all-or-nothing + opt-out                                      |
| Reward Exists          | Increases positive effect              | Moderate   | Consistent across configs                                                        |
| MPCR                   | Mild increase                         | Low        | Statistically robust but weak                                                      |
| Punishment Cost/Magn.  | Little effect alone                   | Low        | No systematic effect outside of interactions                                      |
| Other variables        | Insufficient evidence for main effect  | Low        | -                                                                                 |

---

## 7. Decision Rules

**If-Then Statements (Strongly Supported):**

1. **If chat is enabled,** then punishment is much more likely to improve efficiency.  
   *Evidence: Dominant positive moderator*.

2. **If both opt-out framing and variable contributions,** then punishment tends to raise efficiency.  
   *Evidence: Robust conditional effect*.

3. **If both opt-out framing and all-or-nothing contributions,** or if peer outcomes are visible, then punishment tends to reduce efficiency.  
   *Evidence: Amplified negative effect in these contexts*.

4. **If the game is long and chat is enabled,** then the positive efficiency effect of punishment is stronger; if no chat, game length does not help.  
   *Evidence: Clear contingent effect*.

5. **If reward is enabled,** punishment’s efficiency effects are more positive.  
   *Evidence: Consistent across all models*.

**Where Evidence is Weak or Missing:**

- **If only punishment cost or magnitude is changed with all else held constant,** expect little/no change in efficiency direction or magnitude.
  *Evidence: Punishment “technology” is not a strong driver*.
- **If the configuration falls outside tested parameter ranges (see dataset in paper),** no reliable guidance is available.
- **No numeric threshold or deterministic rules for MPCR, player count, or horizon knowledge are supported.**

---

## 8. Limitations & Missing Evidence

- **No guidance outside the parametrized design space.**
- **No strong evidence on the main effects for punishment cost/magnitude, player count, or round knowledge.**
- **No predictive rules for sub-populations or real-world translation.**
- **Key effects are sometimes highly contingent on multi-way interactions; single-rule application may mislead.**
- **Predictions for efficiency must always reference underlying experimental or modeled estimates, not single-point heuristics.**

---

## 9. How To Use This For Predictions

- **Always enter the full set of 14 CONFIG parameters, plus control efficiency, as prediction inputs.**
- **Identify if chat is enabled; this is the most influential moderator.**
- **Always check the combination of contribution framing, type, and peer outcome visibility.**
- **Assume negligible main effect for punishment cost/magnitude.**
- **Apply only if-then rules that match the configuration; otherwise, defer to empirical or model-based prediction.**
- **Do not extrapolate these findings to drastically different populations or to games outside the 14-dimensional CONFIG space.**
- **If the setting is novel or highly ambiguous, report low confidence and consider further empirical estimation.**

---

**End of Report**

---

**[Supporting Citations:]**
- Main findings and moderator matrix: 
- Quantitative ranges and heterogeneity: 
- Definition of variables and outcome:
