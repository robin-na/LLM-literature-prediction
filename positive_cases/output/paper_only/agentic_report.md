# How Enabling Punishment Changes Efficiency in Public Goods Games: Prediction-Support Guidelines Using Published Experimental Evidence

## Abstract

This report provides actionable predictive guidance on how enabling punishment changes the efficiency of public goods games, grounded strictly in the published experimental paper (“paper_only” evidence). The study systematically varied 14 design parameters across 360 experimental configurations, each tested with and without punishment. Key findings show punishment's effect on efficiency is highly context-dependent and often negative; increases in cooperation can be offset or outweighed by direct punishment costs. Moderators such as communication, contribution framing, and group visibility are more predictive than punishment mechanism details. Here, we restate the prediction task, define all key variables, present numeric summaries of observed effects, and offer empirically-backed decision rules for prediction, with explicit attention to parameter interactions and known knowledge gaps.

---

## Background & Definitions

**Prediction Task Restated:**  
Given values for 14 experimental CONFIG parameters and the measured efficiency of a control (no-punishment) public goods game, predict the average group efficiency if punishment is enabled under otherwise identical conditions.

**Efficiency** (primary outcome):  
- Defined as the ratio of observed group earnings to the earnings if all players fully cooperated every round.  
- **Efficiency = 1** implies perfect group cooperation. Lower values indicate inefficiency due to non-cooperation or costs associated with punishment.

**Primary Objective:**  
Forecast the efficiency in a punishment-enabled game *relative* to the same group’s no-punishment efficiency, using only variables and findings reported in the core paper.

---

## Data & Variables

**14 CONFIG Parameters Used as Predictors:**  
Below are the configuration variables experimentally manipulated and included in the prediction task.

| Parameter Name                | Description |
|-------------------------------|-------------|
| `CONFIG_playerCount`          | Number of players in each game. |
| `CONFIG_numRounds`            | Total number of rounds played. |
| `CONFIG_MPCR`                 | Marginal per-capita return: multiplier applied to contributions, divided by player count. |
| `CONFIG_allOrNothing`         | 1 if contributions are all-or-nothing; 0 if variable/continuous. |
| `CONFIG_chat`                 | 1 if players can communicate (“chat” enabled); 0 otherwise. |
| `CONFIG_defaultContribProp`   | 1 if contribution is opt-out (default contribute), 0 if opt-in (default keep). |
| `CONFIG_punishmentCost`       | Cost (in coins) to impose a single unit of punishment. |
| `CONFIG_punishmentMagnitude`  | Number of coins deducted from target per unit punishment. |
| `CONFIG_showOtherSummaries`   | 1 if peer outcomes are shown each round; 0 otherwise. |
| `CONFIG_showNRounds`          | 1 if total number of rounds is visible to players. |
| `CONFIG_showPunishmentId`     | 1 if identity of punishers/rewarders is revealed. |
| `CONFIG_rewardExists`         | 1 if a reward system is also enabled, 0 otherwise. |
| `CONFIG_rewardCost`           | Cost to give a reward (if enabled). |
| `CONFIG_rewardMagnitude`      | Magnitude added to recipient per unit reward (if enabled). |

In addition, **measured control efficiency** (from an otherwise identical no-punishment game) is available as an input to models.

---

## Empirical Patterns: Punishment Effects and Heterogeneity

### Average Effect of Punishment

- **On average, punishment *did not* increase efficiency.**
  - The paper reports an average *decrease* in normalized efficiency by approximately **6–11 percentage points** when punishment is enabled versus disabled.
- There is substantial heterogeneity:
  - Observed punishment effects range from a **43% improvement** to a **44% reduction** in efficiency across different configurations.

### Key Moderators (Ordered by Predictive Importance)

1. **Communication (`CONFIG_chat`):**
   - *Most influential*: Always increased the magnitude of punishment’s effect (i.e., punishment was more likely to be effective when chat was available). Removing/shuffling this variable increased predictive error by 60%.
2. **Contribution Framing (`CONFIG_defaultContribProp`):**
   - *Second most important*: "Opt-out" framing improved efficiency only when contributions were variable (not all-or-nothing); otherwise, it reduced efficiency.
3. **Contribution Type (`CONFIG_allOrNothing`):**
   - Interacted with framing and visibility; determined whether framing effects were beneficial or detrimental.
4. **Game Length (`CONFIG_numRounds`):**
   - Longer games enhanced punishment’s effect, but only if communication was allowed and peer outcomes were not visible.
5. **Peer Outcome Visibility (`CONFIG_showOtherSummaries`):**
   - Moderated effects of framing and game length.
6. **Reward System (`CONFIG_rewardExists`):**
   - The availability of rewards consistently helped efficiency but was less influential than communication, framing, or outcome visibility.
7. **Marginal Per Capita Return (`CONFIG_MPCR`):**
   - Higher values slightly increased punishment effectiveness, but effect size was small.
   
### Feature Interactions

- Effects of these factors are highly context-dependent: e.g., contribution framing is beneficial in variable-contribution games but detrimental in all-or-nothing games.
- No single-parameter rules can reliably predict the direction of punishment’s effect.

---

## Quantitative Summary

Below is a numeric summary, as reported in the paper:

| Statistic                                   | Value / Range            | Source/Comments               |
|----------------------------------------------|--------------------------|-------------------------------|
| Average effect of punishment on efficiency   | –6% to –11% (normalized) | Efficiency drops when punishment enabled, on average. |
| Range of observed punishment effects         | –44% to +43% (normalized) | Wide context-dependent variation; not symmetric. |
| Best-case configuration change              | +43% increase            | In rare, favorable contexts.  |
| Worst-case configuration change             | –44% decrease            | In unfavorable contexts.      |
| Predictive model (elastic net) R²           | 0.53 (held-out data)     | Substantially outperformed human forecasters. |
| Communication’s effect on prediction error  | +60% when shuffled       | Implies predictive necessity. |

**Table: Example Efficiency Outcomes by Configuration**  
(*Directly reported means or ranges from the paper; the paper does not provide a full config-by-config table.*)

| Condition                            | Typical Efficiency Change with Punishment  |
|---------------------------------------|--------------------------------------------|
| No communication & unfavorable framing| –20 to –44 percentage points               |
| Communication present, positive framing, long games | +10 to +43 percentage points          |
| Reward system enabled                 | Positive effect, often additive            |
| High MPCR (returns to cooperation)    | Slight positive moderation                 |
| “Typical” config (random)             | –6% to –11% on average                    |

**Note:** The paper lacks per-configuration numeric detail; only overall and range statistics are available.

---

## Predictive Guidance: Actionable Rules of Thumb

### When is Punishment Likely to **Decrease** Efficiency?
- **In the absence of communication** (`CONFIG_chat` = 0), punishment usually *reduces* efficiency, especially if:
  - Peer outcome visibility is ON (`CONFIG_showOtherSummaries` = 1)
  - Framing is *opt-out* in an all-or-nothing game (`CONFIG_defaultContribProp` = 1, `CONFIG_allOrNothing` = 1)
- **If control efficiency is already high** (close to 1), enabling punishment rarely increases efficiency further; the added cost usually outweighs potential gains.

### When Might Punishment **Increase** Efficiency?
- **With communication enabled** (`CONFIG_chat` = 1), especially in:
  - Variable-contribution games (`CONFIG_allOrNothing` = 0)
  - Opt-out framing (`CONFIG_defaultContribProp` = 1)
  - Longer games (`CONFIG_numRounds` > median)
  - Peer outcome visibility OFF (`CONFIG_showOtherSummaries` = 0)
- **If initial (control) efficiency is low:** Greater potential for punishment to raise cooperation and thus efficiency—but only in favorable social settings (see above).

### How Do Other Factors Influence Predictions?
- **Reward System Present:** Tends to further boost efficiency, potentially mitigating negative effects of punishment.
- **Punishment “Technology” (cost/magnitude):** Less predictive than context; only use as a tie-breaker or for marginal adjustment.
- **MPCR:** Higher MPCR slightly raises the probability that punishment will help, but effect is small relative to communication/framing.

---

## Limitations & Open Questions

- **Numerical gaps:** The published paper gives only aggregate statistics and qualitative moderator effects—not full config-by-config results. Some numeric estimates (e.g., exact efficiency changes for specific parameter combinations) are thus unavailable.
- **Punishment technology:** Contrary to conventional wisdom, mechanistic punishment details (cost/magnitude) add little to predictive accuracy once context is known; this may differ in unseen environments.
- **Generalizability:** All games used the same interface/protocol; predictions may be less reliable under fundamentally different settings or unmeasured behavioral incentives.
- **Control efficiency relevance:** The importance of control-game efficiency is borne out in modeling, but the paper does not detail interactions between control efficiency and specific configurations.

---

## How To Use This For Predictions

- **Always include**: The 14 CONFIG variables *plus* control (no-punishment) efficiency as model features.
- **Heavily weight context:** Model communication, contribution framing, contribution type, and peer visibility as dominant moderators.
- **Account for interactions**: Use statistical methods capable of modeling high-order interactions (e.g., elastic net with interactions).
- **If communication = 0, expect negative efficiency effects** unless all other parameters are highly favorable.
- **Punishment tech variables** (cost, magnitude) are *minor*—only adjust prediction slightly using these.
- **When in doubt**, default to the **average finding**: enabling punishment will **slightly decrease efficiency** (~6–11%) unless there is strong evidence from configuration/context to suggest otherwise.
- **Beware one-factor rules:** Effects are not reliably predictable from any single parameter alone.
- **Use model output, not intuition:** Human forecasters underperformed statistical models trained with these features.

---

*All evidence, data, and rules herein are drawn strictly from the published experimental paper. For implementation, match configuration inputs and rely on interaction-heavy prediction models as described above.*
