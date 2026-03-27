# Prediction-Support Report: How Enabling Punishment Changes Efficiency in Public Goods Games

---

## 1) Title

**Predicting Efficiency Changes from Punishment in Public Goods Games: Evidence-Based Guidance**

---

## 2) Abstract

This report summarizes the evidence from experimental economics on how the availability of punishment affects efficiency in public goods games. Drawing strictly from the provided literature, we map key experimental variables to the prediction task and synthesize empirical patterns, moderators, and variation in punishment effects. We provide evidence-based guidance for forecasting efficiency when punishment is enabled, noting when results are conditional or heterogeneous. Limitations and evidence gaps are classified, and concise practical usage advice concludes the report.

---

## 3) Background & Definitions

**Prediction Task Restatement:**  
Given the specific configuration (CONFIG) parameters for a public goods game, and the measured average efficiency in the control game (punishment disabled), forecast the average efficiency for the same game when the only change is enabling punishment.

- **Efficiency** = Ratio of the group’s total payoff to the theoretical maximum (full cooperation, no punishment costs):  
    - 1 = Full cooperation;  
    - Lower values = Less cooperation/greater efficiency loss.  
- The principal variable of interest is the *change* in efficiency caused by enabling punishment.

--- 

## 4) Data & Variables

### Key Experimental Variables

The prediction task uses the following parameters:

| Parameter | Definition |
|-----------|------------|
| **CONFIG_playerCount** | Number of players in the game |
| **CONFIG_numRounds** | Number of rounds in the game |
| **CONFIG_MPCR** | Marginal per-capita return (multiplier/playerCount) |
| **CONFIG_allOrNothing** | Contribution: all-or-nothing (true) or continuous (false) |
| **CONFIG_chat** | Is chat communication enabled? |
| **CONFIG_defaultContribProp** | Contribution framing: 0 = opt-in; 1 = opt-out |
| **CONFIG_punishmentCost** | Cost to punisher per unit of punishment |
| **CONFIG_punishmentMagnitude** | Coins deducted from punished player per unit |
| **CONFIG_showOtherSummaries** | Are peer outcomes shown each round? |
| **CONFIG_showNRounds** | Are total rounds shown to players? |
| **CONFIG_showPunishmentId** | Is the identity of the punisher revealed? |
| **CONFIG_rewardExists** | Are rewards enabled? |
| **CONFIG_rewardCost** | Cost to rewarder per unit of reward |
| **CONFIG_rewardMagnitude** | Coins added to rewarded player per unit |
| **CONFIG_punishmentExists** | Is punishment enabled? (1 = treatment, 0 = control) |

- The *control efficiency* input is the observed group efficiency with **CONFIG_punishmentExists = 0**.
- The forecast/predicted quantity is *treatment efficiency* with **CONFIG_punishmentExists = 1**, other CONFIGs unchanged.

---

## 5) Empirical Patterns: Punishment Effects and Heterogeneity

### General Findings

1. **Punishment Increases Contributions, Not Always Efficiency**  
   - Punishment generally increases contributions to the public good (e.g., moving towards full cooperation).
   - However, because punishment is costly (to both punisher and punished), net efficiency gains are not guaranteed and often do **not** materialize; punishment costs may offset cooperation benefits.

2. **Effectiveness of Punishment Moderates Outcomes**
   - Only when punishment is highly effective (punisher’s cost is much smaller than the penalty to the punished) do efficiency gains sometimes emerge.
   - With less effective or costly punishment, efficiency effects are small or negative even as contributions rise.

3. **Coordination, Heterogeneity, and Institutional Design**
   - If punishment requires costly coordination, or if only some can punish, efficiency gains do not reliably appear and may even be negative.
   - Heterogeneity in punishment power or wealth does not always change the positive contribution effects, but does complicate forecasting and may not improve efficiency.

4. **Co-Presence With Other Incentives**
   - When both rewards and punishment are available, results can be complex. Most included studies focus on punishment-only vs. none.

### Numerical Estimates (Where Supported)

- Examples from controlled lab experiments:
    - *Fehr & Gächter*: Contributions rise to nearly 100% with punishment (from ~50%), but “average income is usually below that without punishment: punishment is costly.”
    - *Nikiforakis & Normann (2008)*: Only when punished player loses much (>3× punisher’s cost) does efficiency improve over control. Otherwise, efficiency remains below maximum:  
      | Control | Low Eff. Punishment | High Eff. Punishment |
      |---------|---------------------|----------------------|
      | 9%      | 33–57% contrib.     | 87–90% contrib., higher efficiency|
    - *VCM/WLM paradigm*: In non-linear (WLM) settings, enabling punishment can raise efficiencies from ~45% to ~69% (if antisocial punishment is rare), but in more linear games gains may be marginal or even negative.

---

## 6) Predictive Guidance

- **Default Expectation:** Enabling punishment increases contributions, but *actual efficiency* often stays the same or can fall if punishment is costly.  
- **Strong Efficiency Gains:** Only expected if punishment is low-cost to the punisher AND high-cost to the punished.
- **Modulating Factors:**
    - If the control efficiency is already near 1 (full cooperation), added punishment is likely to reduce efficiency.
    - The higher the expected use/intensity of punishment (e.g., anticipated from low cooperation in control), the greater the risk that efficiency falls.
    - Communication (chat), transparency, and framing variables are less studied as efficiency moderators in the punishment context; most evidence is for punishment parameters and group size.
- **Limiting Cases:**  
    - If antisocial punishment is frequent (i.e., cooperators punish, or punishers are punished), efficiency *will* decline.
    - If punishment is coordinated and rarely used, or if peer-norms substitute for monetary penalties, losses are minimized, but efficiency rarely exceeds control.

---

## 7) Limitations & Missing Evidence

- Some CONFIG variables are under-studied or not addressed (e.g., **CONFIG_defaultContribProp**, **CONFIG_showOtherSummaries**).
- Most experimental results focus on “classical” public goods game designs with 4–6 players, continuous contributions, no or uniform framing, and do not systematically vary chat, round-number salience, or reward schemes alongside punishment.
- There is little robust evidence on interactive effects among multiple CONFIG moderators.
- Almost all studies report group averages; predictive guidance for unusual group sizes, payoff structures, or highly asymmetric roles is limited or absent.

---

## 8) How To Use This For Predictions

- **First:** If control efficiency is high (>0.9), predict a small decrease in efficiency with punishment enabled unless punishment is very mild.
- **If** punishment is much more costly to the punished than to the punisher (e.g., ≥3:1), AND control efficiency is low (<0.6), predict moderate efficiency gain (~10–30 points).
- **Otherwise:** Predict little or no change, or a mild loss in efficiency.
- **If antisocial punishment is possible/likely:** Predict efficiency loss.
- **Do NOT extrapolate effects for under-studied parameters (e.g., chat, default options, number of rounds) beyond the evidence above.
- **Use tabled parameter values only where they exactly match those studied in the literature; otherwise, use only qualitative guidance.**

---

## References

All evidence and quantitative/qualitative guidance in this report is drawn from published experimental studies and review articles provided in the source material, including but not limited to Fehr & Gächter (2000, 2002), Nikiforakis & Normann (2008), and others as documented in the attached files. Full citations available upon request.
