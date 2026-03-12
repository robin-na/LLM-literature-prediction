## 1) Design & Data

- The study systematically varied 14 design parameters across 360 experimental conditions (147,618 decisions from 7,100 participants). Each experimental condition consisted of a pair: a treatment (punishment enabled) and a control (punishment disabled) game, identical except for the punishment manipulation.
- Data were collected in two waves. Wave 1 (learning) used 320 unique, quasi-randomly sampled conditions (one observation each) to maximize coverage. Wave 2 (validation) included 40 new conditions (with 8-12 replications each) to increase statistical power and test out-of-sample predictions.
- Each scenario is described by a 14-dimensional vector, including group size, game length, communication, reward options, contribution type, framing, MPCR, and more. This wide coverage enables examination of interactions and robust prediction of punishment effects.

## 2) Efficiency Definition

- "Efficiency" is defined as the group's total earnings divided by the earnings the group would obtain if everyone contributed fully in every round and no punishment or rewards occurred. Thus:  
  `Efficiency = (Group’s total payoff) / (Total payoff of a fully cooperative group)`  
  Efficiency of 1 means fully cooperative, lower values indicate less cooperation.
- "Normalized efficiency" scales group earnings between full defection (nobody contributes) and full cooperation, to compare across different designs. For prediction tasks, however, the unnormalized efficiency (relative to full cooperation) is used since it is more intuitive for single-configuration predictions.

## 3) Main Findings on Punishment

- On average, introducing punishment increased contributions but often *decreased overall efficiency* due to the costs of punishment; the direction and size of the effect were highly heterogeneous:

  - In learning experiments: normalized efficiency dropped on average from 0.71 to 0.63 with punishment (11% decrease).
  - In validation experiments: decreased from 0.72 to 0.68 (6% decrease), but with large between-condition variability.

- The effect size of punishment ranged from +43% to -44% efficiency change depending on parameter combinations.
- Communication was found to be the *dominant factor* determining whether punishment improves or harms efficiency, followed by contribution framing (opt-in vs. opt-out), contribution type (all-or-nothing vs. variable), game length, and outcome visibility.
- Models (e.g., elastic net with interaction terms) trained on the learning data outperformed both human experts and non-experts at predicting the impact of punishment in new scenarios (out-of-sample R² up to 0.53).

## 4) Heterogeneity / Moderators

- There is *substantial, systematic heterogeneity* in the effect of punishment across experiments, which is attributable to differences in game parameters rather than sampling noise or procedural variance.
- Main moderators and their patterns:
  - **Communication:** When enabled, punishment much more likely to increase efficiency (most important predictor).
  - **Contribution framing:** Opt-out defaults (starting with all resources in the public fund) increased punishment's effectiveness with variable contributions, but reduced it with all-or-nothing contributions. The effect of framing also depends on outcome visibility.
  - **Game length:** Longer games amplified the positive effect of punishment—but only when communication was allowed; this benefit is dampened if peer outcome visibility is high.
  - **Outcome visibility:** Can modulate framing and game length effects, sometimes reducing the positive impact of other moderators.
  - **Reward availability and MPCR:** Both had consistent but weaker positive effects on punishment's impact. Surprisingly, the mechanical parameters of punishment (cost, magnitude) mattered much less for efficiency than context and structural factors.

## 5) Notes for Prediction

- **Inputs:** For each prediction, use the 14 PGG design parameters (see Table 1: group size, game length, MPCR, communication, framing, contribution type, outcome visibility, etc.) plus the observed efficiency of the *control* game (no punishment).
- **Outputs:** Predict the average efficiency when punishment is enabled, using the same group/configuration.
- **Key moderators to watch for:** Communication, contribution framing and type (and their interaction), game length (especially with communication), and outcome visibility.
- Including the control efficiency as a predictor is crucial, as it integrates unmodeled aspects of the baseline group behavior.
- The dominant prediction approach uses models capable of learning interactions (e.g., elastic net with 2-way interactions).
- Human and even expert forecasters tend to underperform statistical models for this task due to difficulty in mentally integrating multi-factor effects.
