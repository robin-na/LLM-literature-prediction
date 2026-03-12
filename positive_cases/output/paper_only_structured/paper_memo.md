## 1) Design & Data

- The study employs an “integrative experiment” varying **14 design parameters** across 360 unique Public Goods Game (PGG) configurations, resulting in 147,618 decisions from 7,100 participants.
- Each experimental configuration is defined by a 14-dimensional vector specifying parameters such as group size, game length, contribution structure, communication, punishment availability, reward mechanisms, marginal per capita return (MPCR), peer outcome visibility, and more.
- For each configuration, there are two parallel games: a control (punishment disabled) and a treatment (punishment enabled), keeping all other parameters identical.
- Data collection occurred in two phases:
  - **Wave 1**: 320 conditions (single realization each, maximizing breadth).
  - **Wave 2**: 40 new conditions (8-12 realizations each, maximizing precision; preregistered, used for validation and human-machine prediction comparison).

## 2) Efficiency Definition

- **Efficiency** in each game is the ratio:
  - `Efficiency = (Group total earnings) / (Earnings if all members fully cooperate every round; no punishment/reward)`
  - Efficiency = 1 means full cooperation; less than 1 means some resources are lost (either to under-contribution or punishment/reward costs).
- **Normalized efficiency** is also reported (main text often focuses on it for cross-configuration comparison), but the human prediction task directly uses standard efficiency as above.

## 3) Main Findings on Punishment

- The impact of enabling punishment is **highly heterogeneous**:
  - Across configurations, punishment effects on efficiency range from a **43% increase** to a **44% decrease** (i.e., punishment can be highly beneficial or highly detrimental depending on context).
  - On average, punishment increased contributions but *often reduced efficiency* (due to the cost of punishment actions).
  - In the learning phase, punishment decreased normalized efficiency (0.71 to 0.63; 11% drop). In validation, the decrease was smaller (0.72 to 0.68; 6% drop), but both phases included individual cases with large gains or losses.
- **Key drivers** of positive punishment effects:
  1. **Communication** (chat enabled) is the most important factor—when allowed, it consistently enhances the effectiveness of punishment and prediction accuracy (shuffling this parameter increases prediction error by 60%).
  2. **Contribution framing** (opt-in vs. opt-out) is the second most important; opt-out framing increases punishment’s effect only if participants can make variable (not all-or-nothing) contributions.
  3. **Interaction effects**: For instance, longer games enhance punishment only if communication is available; with outcome visibility, this effect weakens.
- Surprising null: Technical details of the punishment rule (e.g., ratio of penalty to cost) mattered *less* than social/contextual features.

## 4) Heterogeneity / Moderators

- Substantial, reliable heterogeneity in punishment effects is observed, even with tightly controlled protocols and homogeneous subject pools.
- *Measured moderators* that predict the sign/magnitude of punishment’s impact:
  - Communication (dominant)
  - Contribution framing (opt-in/opt-out)
  - Contribution type (variable vs. all-or-nothing)
  - Game length (number of rounds)
  - Peer outcome visibility
  - MPCR (marginal per capita return; effect is consistent but relatively weak)
- **Strong interactions**: Effects of framing, game length, and peer visibility depend on each other (see above).
- Null or weak moderators: Structural features of the punishment mechanism itself are less predictive than social context and interaction structure.
- **Models trained on these moderators outperformed both expert and lay forecasts** for new (held-out) cases.

## 5) Notes for Prediction

- **Prediction inputs**: 14 CONFIG parameters + efficiency of control (no punishment) condition.
- **Prediction target**: average efficiency of same config with punishment enabled (as defined above).
- For improved prediction:
  - Weight *social context* (communication, visibility, framing, contribution type) heavily.
  - Be alert to strong cross-level interactions (e.g., game length matters only if communication is present).
  - Do not overemphasize punishment technology (cost:impact ratio) relative to social/contextual features, as these structural details are surprisingly weak predictors.
- The observed heterogeneity is genuine and arises from parameter combinations, not random error or researcher variation.
- For new/uncertain cases, models trained on past experiment data outperform both experts and crowds.
