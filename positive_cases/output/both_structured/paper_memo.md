## 1) Design & Data

- The study used an "integrative experiment" approach, exhaustively varying 14 design parameters (CONFIG) across 360 unique public goods game (PGG) conditions using both learning (320 conditions, single realization each) and validation (40 conditions, 8-12 replications each) samples. Across both waves, 7,100 participants made 147,618 decisions (contributions, punishments, rewards).
- Each experimental instance was run in paired conditions: control (punishment disabled) and treatment (punishment enabled), holding all other design parameters identical.
- The 14 parameters include group size, game length, contribution type (variable/all-or-nothing), contribution framing (opt-in/opt-out), MPCR (marginal per capita return), communication availability, peer outcome visibility, actor anonymity, horizon knowledge, and technology/cost settings for punishment/reward, among others.
- This systematic manipulation allows direct comparison of punishment effects, relative feature importance, and interactions among variables, with minimal hidden moderators (e.g., same recruitment/interface for all sessions). Data from the control condition serves as a key input for predicting the outcome in the punishment-enabled condition.

## 2) Efficiency Definition

- **Efficiency** is the primary outcome metric. It is defined as the ratio of the group’s actual total earnings to the total earnings achievable by a fully cooperative group (everyone always contributes fully, no punishment/reward costs incurred). Thus,
  ```
  Efficiency = (Group’s observed total payoff) / (Total payoff under full cooperation)
  ```
  Efficiency = 1 corresponds to maximum cooperation and no losses to punishment/reward; lower values indicate reduced welfare due to free-riding and/or the costs of sanctioning.
- For cross-condition comparisons, a normalized efficiency metric is also used (scaling relative to both full cooperation and full defection), but within the prediction task, regular efficiency is used since it is more intuitive and applicable to predicting single-configurations (i.e., treatment vs. control for the same parameter set).

## 3) Main Findings on Punishment

- Punishment generally increases contributions but does **not** always increase efficiency. On average, punishment led to reduced efficiency across all configurations (11% decline in learning phase, ~6% in validation), but this average masks **large heterogeneity**: in some settings, punishment improved efficiency dramatically (up to +43%), while in others, it was highly detrimental (as much as -44%).
- The effect of punishment is not determined by a single factor, but by complex, often contingent, interactions among multiple game parameters.
- Feature importance analyses revealed:
  - **Communication** (enabled/disabled) is by far the most important and consistent predictor of when punishment improves welfare, tripling prediction error when shuffled.
  - Availability of reward mechanisms and higher MPCR modestly and consistently improve punishment’s effect, but are much less predictive than communication.
  - Punishment technical parameters (cost, effectiveness) matter much less than expected: their influence on the welfare effect of punishment is minimal compared to contextual features (communication, framing, etc.).
- Predictive models (E-Net, OLS, RF, MLP, XGB) using the 14 parameters and control efficiency outperformed both expert and lay human forecasters. Human forecasters, including field experts, struggled to integrate the interacting effects and typically performed no better than baseline averaging.

## 4) Heterogeneity / Moderators

- There is **substantial, systematic heterogeneity** in punishment's effects, fully attributable to experimentally manipulated parameters (since all else was held constant).
- Key interactions:
  - **Contribution Framing**: Opt-out framing enhances punishment’s effectiveness when variable contributions are allowed, but *reduces* it when contributions are all-or-nothing; further modulated (amplified, attenuated) by peer outcome visibility.
  - **Game Length**: Extending the number of rounds boosts punishment effectiveness only when communication is allowed; this positive effect is dampened if outcomes are visible.
- Other tested factors included anonymity, group size, horizon knowledge, and more. The heterogeneity is not random noise but systematic, with I² heterogeneity statistic indicating real differences by condition.
- These findings point out that neither “punishment works” nor “punishment fails” is generally correct—the context (“when and for whom”) is decisive.

## 5) Notes for Prediction

- The best predictors for whether punishment will increase efficiency are: communication (most important), contribution framing, contribution type, game length, peer outcome visibility, and to a lesser degree, availability of reward.
- Many effects depend on **interactions** rather than main effects alone; e.g., framing effects depend on contribution type and visibility; game length only matters with communication, etc.
- Efficiency in the control games (no-punishment) is a key feature for prediction—it gives a baseline for likely group cooperation absent punishment.
- Do **not** over-rely on mechanical details of the punishment system—contextual and social parameters are far more important for success.
- High heterogeneity means out-of-sample predictive models trained on breadth of conditions are far superior to intuition-based human averaging, even from field experts.
