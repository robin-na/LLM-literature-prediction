# Memo: Summary of PGG Manuscript for Efficiency Prediction Task

## 1) Design & Data

- The study used an “integrative” experiment structure: 14 design parameters were systematically and simultaneously varied across 360 unique experimental conditions (147,618 total decisions, 7,100 participants).
- Each experimental condition was a point in the 14-dimensional design space and defined a single PGG scenario. Each scenario was run as a pair of games: punishment disabled (“control”) and punishment enabled (“treatment”)—all other parameters matched.
- Data collection had two phases:
    - Wave 1 (learning): 320 conditions sampled via Sobol sequence (max coverage, 1 realization each).
    - Wave 2 (validation): 40 new conditions, each with 8-12 replicates (for higher precision), for out-of-sample prediction testing.
- All protocols, recruitment, and user interfaces were standardized to minimize hidden moderators.
- Each CONFIG parameter (see below) was systematically manipulated (see Table 1 for parameter list).

## 2) Efficiency Definition

- **Efficiency** is defined as the ratio of the group’s total net earnings to the total earnings under full cooperation (all contribute maximally every round):  
   Efficiency = (group’s net payoff) / (group’s payoff if all cooperate fully).
- Efficiency = 1: full cooperation; lower values mean less cooperation and/or welfare lost to inefficiency or costly punishment.
- In some analyses “normalized efficiency” is used, scaling observed earnings relative to the minimum (full defection) and maximum (full cooperation, no rewards) possible in each setting, enabling fairer comparison across parameter space.

## 3) Main Findings on Punishment

- On average, punishment **increased contributions** but did **not reliably increase efficiency** due to incurred punishment costs; in fact, welfare often decreased.
- Direction of punishment’s effect on efficiency was highly variable—ranging from +43% to -44% across experimental conditions.
    - In some setups, punishment dramatically reduced efficiency (e.g., 0.78 to 0.44); in others, it increased efficiency substantially (e.g., 0.56 to 0.80).
- Models (especially E-Net/Elastic Net) using the full CONFIG and observed control-game efficiency as inputs **outperformed human experts and laypeople** in prediction accuracy, with best model R² = 0.53 on out-of-sample tasks.
    - Human "wisdom of the crowd" and individual experts performed little better than guessing the grand mean efficiency under punishment.

## 4) Heterogeneity / Moderators

- Substantial, statistically robust heterogeneity in the effect of punishment on efficiency across conditions—attributed specifically to the varied CONFIG parameters (not random noise or external moderators).
- **Key moderators/predictors**:
    - **Communication:** By far the most important predictor; enabling communication increased the net effectiveness of punishment more than any other feature.
    - **Contribution Framing (opt-in vs. opt-out):** The effect of the default contribution condition interacts with other parameters, especially contribution type and peer outcome visibility.
    - **Game Length:** Only enhances punishment’s effectiveness if communication is available; effect is damped if other players' outcomes are visible.
    - **Reward Availability:** Consistently amplifies positive impact of punishment.
    - **Marginal Per Capita Return (MPCR):** Higher MPCR raises efficiency, but impact is generally smaller.
    - **Complex interactions** (e.g., opt-out increases effectiveness with variable contributions but can harm it in all-or-nothing settings; effects of outcome visibility and communication are similarly non-additive).
- **Punishment “technology”** (cost-magnitude ratio) is much less influential than context/interactional parameters.

## 5) Notes for Prediction

- **Best practice for prediction**: Use all 14 CONFIG parameters plus the control-game efficiency as features for modeling, as the context-rich approach captures interaction effects and heterogeneity.
- Control (no-punishment) efficiency is an *extremely useful summary feature*: it helps anchor predictions by summarizing baseline group behavior given the CONFIG.
- Consider key interaction effects in modeling; effects of some parameters depend critically on the values of others (e.g., communication × game length; contribution framing × contribution type × outcome visibility).
- Models trained on this structure generalize well to new CONFIGs, but the actual effect of punishment on efficiency can vary directionally and in magnitude—highlighting the need for highly contextual, parameter-based prediction rather than simple heuristics or rules-of-thumb.
- Caution: While the models work across the studied range, extrapolation beyond the sampled/design parameter space or to different populations may diminish accuracy.

---

**CONFIG parameter list (for each instance):** group size, game length, contribution type (variable/all-or-nothing), contribution framing (opt-in/opt-out), MPCR, communication, peer outcome visibility, actor anonymity, horizon knowledge, punishment enabled, peer incentive cost, punishment technology, reward enabled, reward technology.
