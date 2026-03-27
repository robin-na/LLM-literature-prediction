# Prediction-Support Report: How Enabling Punishment Changes Efficiency in New Public Goods Games

## 1. Title

**Empirical Forecasting: Effects of Enabling Punishment on Efficiency in Public Goods Games**

---

## 2. Abstract

This report provides evidence-backed guidance for predicting the impact of enabling punishment on efficiency in public goods games, given a CONFIG parameterization and control efficiency. Drawing only on published empirical findings, it summarizes key moderators, defines all relevant variables, discusses observed patterns in punishment's effects, and offers clear decision rules and operational guidance. Numeric and qualitative effects are reported strictly where supported by the cited literature.

---

## 3. Background & Definitions

**Prediction Task Restated:**  
Given a set of public goods game parameters (CONFIGs) and observed control game efficiency (with punishment disabled), predict the expected average efficiency when punishment is enabled. Efficiency is defined as the ratio of observed group payoff to the hypothetical maximum (full cooperation, every round). A value of 1 signals full cooperation; lower values indicate less cooperation.

---

## 4. Data & Variables

### CONFIG Parameter Definitions
- **CONFIG_playerCount:** Number of participants in the group.
- **CONFIG_numRounds:** Total number of rounds played.
- **CONFIG_MPCR:** Marginal per-capita return (public good multiplier divided by group size).
- **CONFIG_allOrNothing:** Binary; if true, contributions are all-or-nothing.
- **CONFIG_chat:** Whether in-game chat is enabled.
- **CONFIG_defaultContribProp:** 0 = "opt-in" framing, 1 = "opt-out".
- **CONFIG_punishmentCost:** Cost to the punisher per unit punishment applied.
- **CONFIG_punishmentMagnitude:** Coins lost by punished player per unit of punishment.
- **CONFIG_showOtherSummaries:** Whether peer outcomes are shown.
- **CONFIG_showNRounds:** Whether players can see round count.
- **CONFIG_showPunishmentId:** Whether punisher/rewarder identities are revealed.
- **CONFIG_rewardExists:** Whether rewards are enabled.
- **CONFIG_rewardCost:** Cost to the rewarder per unit reward applied.
- **CONFIG_rewardMagnitude:** Coins gained by rewarded player per unit of reward.
- **CONFIG_punishmentExists:** Whether punishment is enabled (the key difference between control and treatment).

---

## 5. Empirical Patterns

### Main Effects
- **Punishment, on average, increases cooperation and thus efficiency, but only when the punishment is sufficiently impactful compared to its cost. Otherwise, gains in contribution may be offset by the resource-wasting costs of punishment itself, or can even reduce efficiency.**  
- **Efficiency gains from punishment often emerge after several rounds, as players learn and adapt behavior. Early rounds may show little or negative effect**.
- In some cases, particularly where punishment is not well-targeted or is used "antisocially," efficiency may not improve, or may be worse than control.  
- Larger groups with endogenous authority or centralized punishment may see stronger efficiency gains.
- High effectiveness (punishmentMagnitude >> punishmentCost) is needed for efficiency gains.
- Information accuracy about contributions is critical; noisy or ambiguous signals reduce punishment’s positive effect on efficiency.
- The marginal per-capita return (MPCR), framing, and additional features such as reward opportunities moderate effects, but many are not universally established.

---

## 6. Predictive Guidance

### Moderator Matrix

| Variable/CONFIG        | Likely Direction | Confidence | Evidence Note                                  |
|------------------------|------------------|------------|------------------------------------------------|
| punishmentMagnitude    | ++ (if high)     | High       | Efficiency gains only with effective punishment  |
| punishmentCost         | -- (if high)     | High       | High cost relative to magnitude kills gains     |
| playerCount            | +                | Moderate   | Larger groups endorse bigger efficiency gains if authority is endogenous/centralized  |
| info accuracy          | ++ (if perfect)  | High       | Noisy info sharply reduces efficiency           |
| antisocial punishment  | --               | High       | Can negate or reverse efficiency improvements   |
| duration/numRounds     | + (over time)    | High       | Gains occur over repeated play                  |
| rewards present        | Ambiguous        | Low        | Weak/mixed evidence                            |
| communication (chat)   | Possible +       | Low        | Not universally tested                          |
| framing                | Unclear          | Low        | Not consistently reported                       |
| showOtherSummaries     | Unclear          | Low        | Not consistently reported                       |
| showNRounds            | Unclear          | Low        | Not consistently reported                       |
| allOrNothing contrib   | Unclear          | Low        | Not consistently reported                       |
| showPunishmentId       | Unclear          | Low        | Not consistently reported                       |
| average control efficiency | Baseline for comparison | High | Needed for relative estimates |

---

### Decision Rules

- **If** punishmentMagnitude is at least 3–4× punishmentCost, and contribution info is accurate, **then** enabling punishment is likely to increase efficiency relative to the control game, often achieving 80–90% of full cooperation in later rounds.
- **If** punishment cost is high relative to impact, **then** no significant efficiency gain is likely, even if group cooperation increases.
- **If** punishment is antisocial, poorly targeted, or information about free-riding is noisy, **then** efficiency may remain unchanged or decrease compared to control.
- **If** the game uses centralized enforcement via endogenous authority, and group size is large, **then** efficiency improvements are stronger.
- **If** punishment is enabled but used rarely after early rounds, **then** sustained cooperation and efficiency gains are likely, as punishment acts mostly as a threat.
- **If** rewards are present with punishment, or chat/framing is changed, **then** the evidence is mixed or missing; no strong prediction can be made beyond the specific empirical settings studied.

---

## 7. Limitations & Missing Evidence

- There is **no universal quantitative prediction** for how all 14 CONFIG parameters interact to shift efficiency. Most evidence centers on a few key variables (punishment cost/magnitude, group size, information quality, game length).
- **No clear findings** on the effects of: all-or-nothing contributions, chat, framing (opt-in/opt-out), reward settings, displaying peer outcomes, round counter, or punishment/reward identity display.
- Many studies highlight that **antisocial punishment and targeting errors** erode gains; design specifics and subject pools matter.
- Most studies analyze homogeneous groups; **diversity/moderators are rarely systematically varied**.
- **Numeric thresholds** (e.g., magnitude/cost ratios, minimum duration for effects) should only be applied when clearly matching the structure and measurements of the cited evidence.

---

## 8. How To Use This For Predictions

- **Always establish whether CONFIG_punishmentMagnitude is much greater than CONFIG_punishmentCost.** Efficiency gains require high punishment effectiveness.
- **If information about contributions is accurate and the setup matches typical experiments (small groups, continuous contributions, repeated play), expect increasing efficiency with punishment, especially after early rounds.**
- **If efficiency in the control game is already high (near 1), marginal gains when adding punishment may be small.**
- **Do not assume gains from punishment if: punishment is weak or costly, info is noisy, or design features differ from well-evidenced setups.**
- **If predicting in novel parameter spaces (e.g., with both rewards and punishment, or with changing group size/framing), be exceptionally cautious and default to reporting weak or missing evidence.**
- **Use the “Moderator Matrix” and “Decision Rules” to structure mechanistic/qualitative forecasts, rather than numeric point predictions, unless an empirical analog matches your instance closely.**

---

**References To Empirical Evidence Used:**  
- Nikiforakis & Normann (2008), Egas & Riedl (2008), Fehr & Gächter (2000/2002), Grechenig et al. (2010), Lim & Zhang (2020), and others as annotated above.
