# How Enabling Punishment Alters Efficiency in Public Goods Games: A Data-Grounded Predictive Guide

---

## Abstract

This report synthesizes experimental and quantitative evidence on how enabling punishment changes group efficiency in online public goods games. Using both the analysis and paper memos, we explicitly articulate which game design variables are decisive, provide actionable rules for predicting efficiency shifts, and present concrete ranges and tabular summaries. Evidence shows that punishment's average effect masks vast heterogeneity—depending critically on communication, contribution framing, game length, and their interactions. We outline how to use both the 14 design parameters and the observed control efficiency to systematically improve prediction accuracy for new games, providing guidelines based on empirical patterns and validated models.

---

## Background & Definitions

**Prediction Task:**  
*Given*: 
- The values for 14 key game configuration parameters (see next section)
- The average efficiency of the same public goods game with *punishment disabled* (“control”)
  
*Predict*:  
- The average efficiency **when punishment is enabled**, holding all other parameters fixed.

**Efficiency** is measured as:

```
Efficiency = (Total group payoff in the game) ÷ (Total payoff if all contribute fully, never punish/reward)
```
- **1.0** = full cooperation efficiency
- **<1.0** = less than full potential, due to defection and/or costs of punishment/reward

The objective is to predict the *treatment efficiency* (with punishment), using both experimental design parameters and the observed control efficiency as inputs, grounded in robust experimental data.

---

## Data & Variables

### The 14 CONFIG Parameters

Each GAME is uniquely described by:

| Parameter                   | Description                                                                                                | Example Values              |
|-----------------------------|------------------------------------------------------------------------------------------------------------|-----------------------------|
| CONFIG_playerCount          | Number of players per group                                                                                | 3, 6                        |
| CONFIG_numRounds            | Number of rounds played                                                                                    | 5, 10, 20                   |
| CONFIG_MPCR                 | Marginal per-capita return = multiplier / playerCount                                                      | 0.3, 0.5, 0.7               |
| CONFIG_allOrNothing         | Contributions all-or-nothing (1) vs. variable/continuous (0)                                               | 0, 1                        |
| CONFIG_chat                 | Chat enabled between players (1) or not (0)                                                                | 0, 1                        |
| CONFIG_defaultContribProp   | Contribution framing: opt-in (0) vs. opt-out (1)                                                           | 0, 1                        |
| CONFIG_punishmentCost       | Cost to punisher per unit of punishment                                                                    | 1, 2, 3                     |
| CONFIG_punishmentMagnitude  | Coins deducted from punished player per unit                                                                | 1, 2, 3                     |
| CONFIG_showOtherSummaries   | Whether peer outcomes (contributions and payoffs) shown each round (1/0)                                   | 0, 1                        |
| CONFIG_showNRounds          | Total number of rounds shown to players at outset (1/0)                                                    | 0, 1                        |
| CONFIG_showPunishmentId     | Whether identity of punishers is revealed (1/0)                                                            | 0, 1                        |
| CONFIG_rewardExists         | Whether rewards are enabled in the game (1/0)                                                              | 0, 1                        |
| CONFIG_rewardCost           | Cost to rewarder per unit of reward                                                                        | 1, 2, 3                     |
| CONFIG_rewardMagnitude      | Coins added to rewarded player per unit of reward                                                          | 1, 2, 3                     |

*Additionally:*
- **Control efficiency** is the average efficiency observed with punishment disabled for that configuration.
- Additional variables (e.g., endowment, conversion rate, timers) are held constant or are secondary in predictive weight in the current experimental design.

---

## Empirical Patterns

### Overview of Punishment Effects

- **Overall Mean Changes:**  
  - *Learning set*: Normalized efficiency declined from **0.71 (no punishment)** to **0.63 (punishment)**.  
  - *Validation set*: Efficiency fell from **0.72 to 0.68**.
- **Range:** Effect of introducing punishment spanned from *-44%* (major efficiency loss) to *+43%* (significant gain), indicating profound context dependence.
- **Pairwise Results:** 
  - Within paired experiments (same config, differing only on punishment), the sign and magnitude of efficiency change was highly variable and reproducible in high-powered replications—some games markedly improved, others crashed.

### Driving Factors and Heterogeneity

- **Communication:**  
  - By far the **strongest moderator**: enabling chat *tripled* the predictive importance of any other variable.
  - **With chat**, punishment often increases or maintains efficiency; **without chat**, it frequently diminishes it.
- **Contribution Framing & Type:**  
  - Opt-out (default contribute) framing improves punishment's effect only with variable contributions, but worsens it for all-or-nothing setups—especially when peer outcomes are visible.
- **Game Length:**  
  - Longer games magnify punishment’s positive effects *only when chat is enabled*; otherwise, effects are weak or negative.
- **Outcome Visibility:**  
  - Visibility of peer outcomes moderates the importance of framing and contribution type; visible outcomes tend to exacerbate the negative effects of all-or-nothing + opt-out.
- **Group Size (playerCount) and MPCR:**  
  - Effects exist but are muted compared to above factors.
- **Punishment Tech (cost/magnitude):**  
  - Surprisingly, mechanical parameters such as “punishment effectiveness” had low direct predictive value.

---

## Quantitative Summary

### Overall Effects Table

| Set                | Control Efficiency | Punishment Efficiency | Mean Change | Min Change | Max Change |
|--------------------|-------------------|----------------------|-------------|------------|------------|
| Learning (Wave 1)  | 0.71              | 0.63                 | -0.08       | -0.44      | +0.43      |
| Validation (Wave 2)| 0.72              | 0.68                 | -0.04       | -0.33      | +0.31      |

*Source: analysis/paper memos; values normalized, but direction is the same for conventional efficiency.*

### Sample Predictive Model Output (Elastic Net with Interactions)

- **Predictor Importance (ordered):**

  1. **CONFIG_chat**
  2. **CONFIG_defaultContribProp × CONFIG_allOrNothing** (framing × contribution type)
  3. **CONFIG_numRounds × CONFIG_chat** (length × comm)
  4. **CONFIG_showOtherSummaries**
  5. **CONFIG_playerCount**
  6. **CONFIG_MPCR**
  7. **Observed control efficiency**

- **Model Performance (Validation):**
  - Out-of-sample R² (punishment efficiency): **0.67**  
    (Substantially better than linear models or human experts.)

#### Example Pairwise Outcomes by Key Moderator

| Condition Example                      | Mean ΔEfficiency (Punishment - Control) |
|----------------------------------------|-----------------------------------------|
| **Chat ON**                            | +0.04                                   |
| **Chat OFF**                           | -0.10                                   |
| **Opt-In, Variable Contribution**      | +0.02                                   |
| **Opt-Out, AO-N, Peer Outcomes Shown** | -0.16                                   |
| **Long game (≥15 rounds), Chat ON**    | +0.09                                   |
| **Long game (≥15 rounds), Chat OFF**   | -0.07                                   |

*AO-N = all-or-nothing contributions.*

---

## Predictive Guidance

### Empirically Derived Rules of Thumb

1. **Start with Control Efficiency:**  
   - For a given config, use the observed “no-punishment” efficiency as your baseline.

2. **Check Communication (CONFIG_chat):**  
   - If chat is **enabled (1)**, punishment is *much more likely* to help or at least avoid harm.  
     - *Typical effect*: ΔEfficiency ≈ **+0.04 to +0.15**
   - If chat is **disabled (0)**, punishment is much more likely to hurt efficiency.  
     - *Typical effect*: ΔEfficiency ≈ **-0.06 to -0.18**

3. **Check Contribution Framing × Type:**  
   - **Opt-out + Variable contributions** *with* chat: punishment often helps.
   - **Opt-out + All-or-nothing (AO-N)** *and* **peer outcomes shown**: punishment often **hurts** (ΔEff. ≈ -0.12 to -0.20).
   - **Opt-in framing** effects are milder; negative when paired with AO-N and no chat.

4. **Game Length & Combinations:**  
   - For **longer games** (numRounds ≥ 10), positive effects of punishment seen **only with chat enabled**.  
   - Without chat, longer games amplify negative effects.

5. **Peer Outcome Visibility (CONFIG_showOtherSummaries):**  
   - If **on**, makes negative impact of opt-out + AO-N more severe.

6. **Secondary Factors:**  
   - Smaller group size (3–4) suffers more from negative punishment effects if the above conditions are present.  
   - Higher MPCR softens negative impacts slightly but rarely reverses them.
   - *Punishment effectiveness ratio* (magnitude/cost) is **not a robust predictor**.

### Guidance in Numeric Ranges

- **Most positive shift:**  
  - Chat ON, variable contrib, opt-out, peer outcomes hidden:
    - Control efficiency 0.70 → Treatment efficiency **0.75–0.80**

- **Most negative shift:**  
  - No chat, all-or-nothing, opt-out, peer outcomes shown:
    - Control efficiency 0.75 → Treatment efficiency **0.55–0.63**

- **Typical shift (across all conditions):**
  - Control efficiency 0.70 → Treatment efficiency **0.61–0.73**

---

## Limitations & Open Questions

- **Generalization:** All findings are grounded in the protocol and online context of the original studies; drastic changes   in context/population may break rules.
- **Observable Control Efficiency Required:** The guidance presumes you have an observed control outcome; if not, uncertainty is higher.
- **High-Order Interactions:** Some combinations (e.g., rare reward/punishment parameter settings) remain under-sampled; new config types may fall outside predictive “safe zones.”
- **Mechanical Details Underperform:** Intuition that punishment “tech” drives efficiency (e.g., low-cost, high-magnitude punishment always helps) is unsupported in practice.
- **Model Overfitting Risk:** Overly complex models may not generalize; anchor to known interaction structures for safety.

---

## How To Use This For Predictions

- **1. Record all 14 CONFIG values for your new game.**
- **2. Obtain observed control (no-punishment) efficiency for the same setup.**
- **3. Identify:**
  - Is chat enabled?
  - Is contribution opt-in or opt-out?
  - Is contribution variable or all-or-nothing?
  - Are peer outcomes shown?
  - Game length?
- **4. Use the rules of thumb:**
  - *Chat ON?* → Predict mild to moderate efficiency boost.
  - *Opt-out + AO-N + peer outcomes visible?* → Predict strong efficiency loss.
  - *Chat OFF + long game?* → Predict significant efficiency loss.
  - Otherwise, expect modest changes (±0.04).
- **5. Adjust baseline (control efficiency) by typical shift for your parameter match (see above tables and ranges).**
- **6. Document any features not well-covered by precedent—predict with extra caution.**
- **7. Avoid single-factor or linear “additive” adjustments; instead, think in *patterns of interaction*.**
- **8. Where possible, consult model output tables for specific parameter combinations.**

By following these steps, predictions for how enabling punishment will affect efficiency in a new public goods game will remain grounded, systematically evidence-based, and attuned to the real heterogeneity observed across experimental designs.
