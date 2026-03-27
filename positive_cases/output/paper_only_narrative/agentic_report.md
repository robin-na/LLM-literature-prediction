# Prediction Report: Estimating Punishment Effects on Efficiency in Public Goods Games

## 1) Title

**Estimating Efficiency Outcomes from Enabling Punishment in New Public Goods Games: Evidence-Based Predictive Support**

---

## 2) Abstract

This report synthesizes experimental evidence on how enabling punishment in public goods games (PGGs) influences group efficiency, utilizing direct findings from a large-scale, systematically varied experiment. Drawing on 360 unique experimental conditions and over 7,000 participants, we summarize the predictive performance of statistical models that use configurable game parameters (CONFIG), plus control (no punishment) efficiency, to forecast efficiency under punishment. We provide practical guidance for prediction, highlight key moderators of punishment effects, and specify the limits of evidence, ensuring all claims are strictly supported by the attached paper.

---

## 3) Background & Definitions

The prediction task is as follows: *Given all 14 configurable parameters of a public goods game (CONFIG), plus the observed average efficiency in the control condition (punishment disabled), estimate the average efficiency for the same game when peer punishment is enabled*. Efficiency is formally defined as the ratio of a group’s actual total payoff to that of a fully cooperative group. An efficiency of 1 signals perfect cooperation, lower values indicate less cooperation.

The primary aim is not to determine "if" punishment works, but "when" it increases or decreases efficiency, by leveraging empirical regularities reflected in experimental data and statistical models fit to these data.

---

## 4) Data & Variables

### Experimental Design and Prediction Inputs

Each game configuration is characterized by the following 14 parameters, plus the binary indicator for punishment:

| Parameter                   | Description                                                                                  |
|-----------------------------|----------------------------------------------------------------------------------------------|
| CONFIG_playerCount          | Number of players in the game                                                                |
| CONFIG_numRounds            | Number of rounds in the game                                                                 |
| CONFIG_MPCR                 | Marginal per-capita return = multiplier / playerCount                                        |
| CONFIG_allOrNothing         | True if contributions are all-or-nothing, otherwise continuous                               |
| CONFIG_chat                 | Whether chat is enabled between players                                                      |
| CONFIG_defaultContribProp   | 0 = opt-in (default keep, must actively give); 1 = opt-out (default contribute, must keep)   |
| CONFIG_punishmentCost       | Cost to punisher per unit punishment                                                         |
| CONFIG_punishmentMagnitude  | Coins deducted from punished player per unit punishment                                      |
| CONFIG_showOtherSummaries   | Whether peer outcomes are shown each round                                                   |
| CONFIG_showNRounds          | Whether total number of rounds is shown to players                                           |
| CONFIG_showPunishmentId     | Whether the identity of punishers/rewarders is shown                                         |
| CONFIG_rewardExists         | Whether rewards are enabled                                                                  |
| CONFIG_rewardCost           | Cost to rewarder per unit reward                                                             |
| CONFIG_rewardMagnitude      | Coins added to rewarded player per unit reward                                               |
| CONFIG_punishmentExists     | Whether punishment is enabled (distinguishes control from treatment)                         |

### Mapping to Experiment

Experimental games were run in matched pairs differing only by CONFIG_punishmentExists. Both regular and normalized efficiency were measured, but **regular efficiency (treatment efficiency)** is the target for prediction.

---

## 5) Empirical Patterns (Punishment Effects and Heterogeneity)

### Main Effects

- **On average, punishment does not always improve efficiency.** Across the learning experiments, punishment reduced normalized efficiency from 0.71 to 0.63 (an 11% decrease), and in validation experiments from 0.72 to 0.68 (6% decrease), though the latter effect was only marginally significant.
- **Punishment can either *increase* or *decrease* efficiency sharply depending on game parameters.** In some settings, punishment caused a 43% improvement, in others a 44% reduction.
- **The predictive statistical model (E-Net) achieved out-of-sample R² = 0.53**, outperforming both experts and laypeople on this prediction task.

### Key Moderators

#### Consistently Important:
- **Communication (CONFIG_chat):** Enabling chat has the single largest positive effect on punishment efficiency. Shuffling this variable increased model error by 60%, three times that of any other factor. Communication supports explicit coordination and norm-setting, greatly amplifying punishment’s positive potential.

#### Consistently Positive (but smaller impact):
- **Availability of rewards (CONFIG_rewardExists)**
- **Marginal per-capita return (CONFIG_MPCR)**

#### Contingent/Interaction Effects:
- **Contribution Framing (CONFIG_defaultContribProp) × Contribution Type (CONFIG_allOrNothing):** Opt-out framing helps when contributions are variable, but actually hurts efficiency with all-or-nothing contributions. This negative effect is amplified when peer outcomes are visible.
- **Game Length (CONFIG_numRounds) × Communication × Peer Outcome Visibility (CONFIG_showOtherSummaries):** Longer games only increase punishment efficiency if communication is allowed, and this effect is weaker when peer outcomes are visible.

#### Punishment Parameters (CONFIG_punishmentCost, CONFIG_punishmentMagnitude)
- Surprisingly, these had *minimal effects* on efficiency outcomes compared to context variables above.

### Table: Variables Most Important for Out-of-Sample Prediction

| Rank | Parameter            | Relative Impact (on model prediction error)      |
|------|----------------------|-------------------------------------------------|
| 1    | Communication        | 60% increase when shuffled                      |
| 2    | Contribution framing | 18% increase when shuffled (interaction effect) |
| 3    | Game length          | 11.5% increase when shuffled (interaction effect)|
| 4    | Rewards exist        | 4.6% increase when shuffled                     |
| —    | Punishment cost / size | Smallest overall effect                      |



---

## 6) Predictive Guidance

- **Strong context effects:** The outcome of enabling punishment depends heavily on *multiple interacting factors*, primarily communication, contribution framing, and contribution type.
- **Model forecasts are superior to expert/lay intuition:** Simple heuristics (e.g., “punishment always helps” or “it’s mostly about the cost or magnitude of punishment”) perform poorly.
- **Expect heterogeneity:** Effects ranged from -44% to +43% change in efficiency depending on the configuration. Predict using the full set of CONFIG parameters plus the observed control efficiency.
- **Rule of thumb for communication:** If chat is enabled, punishment is *much* more likely to improve efficiency.
- **If using opt-out framing:** Avoid all-or-nothing contribution rules if the goal is to facilitate positive punishment effects.

---

## 7) Limitations & Missing Evidence

- **All predictive guidance is limited to the design space covered in the experiments (see the parameter ranges above).** Results should not be extrapolated outside this space.
- **Effects of punishment cost and magnitude are not robustly identified as important by the paper; thus, no specific guidance can be given on their role beyond noting their surprising lack of impact in this dataset.**
- **External generalizability:** The findings are specific to stylized public goods games and not certain to hold for other forms of cooperation or in real-world settings.
- **Population effects:** The experiments held population constant; thus, how generalizable the results are across different populations is untested.

---

## 8) How To Use This For Predictions

- Always input all 14 CONFIG parameters *plus control efficiency* to the predictive model.
- Pay close attention to whether communication (chat) is enabled; this is the single most influential moderator.
- Note contribution framing and type: opt-out + variable is usually favorable for punishment; opt-out + all-or-nothing is likely to reduce efficiency, especially with visible outcomes.
- Game length matters mainly when chat is enabled.
- Do **not** rely on punishment cost or magnitude to drive predictions; these are not major effectors per the evidence.
- Expect a wide range of possible outcomes: both efficiency increases and decreases of similar magnitude are possible.
- If in doubt, model-based predictions (E-Net or similar statistical models) are empirically superior to expert judgment.

---

**All claims and guidance above are strictly drawn from the attached experimental evidence; no extrapolation or unsupported speculation is included.**
