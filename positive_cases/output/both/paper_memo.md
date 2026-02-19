## 1) Design & Data

- The study used integrative experiments with 14 systematically varied design parameters, yielding 360 unique experimental conditions across two data collection waves: 320 for model training (Wave 1, maximizing coverage) and 40 for validation (Wave 2, maximizing precision with multiple replications per condition).
- Each experiment included a control game (punishment disabled) and a treatment game (punishment enabled), identical in all other parameters. Group size, game length, communication, outcome visibility, contribution type and framing, and peer incentive details (including punishment and reward settings) were among the manipulated variables.
- Data: 147,618 decisions from 7,100 participants. All experiments used uniform protocols to minimize hidden moderators. Breadth was prioritized in training, and depth/precision in validation.

## 2) Efficiency Definition

- Efficiency is the ratio of the group’s total payoff to the total payoff of a fully cooperative group (where all members contribute fully and never punish or reward):
  
    `Efficiency = Group Total Earnings / Full Cooperation Earnings`
  
  This was the primary measure in the forecasting and prediction tasks.
- For comparing across PGG variants, a normalized efficiency metric was also used, scaling group earnings between full defection (nobody ever contributes) and full cooperation. However, for the prediction context (single configuration), conventional efficiency suffices.

## 3) Main Findings on Punishment

- On average, punishment increased contributions but reduced efficiency: in learning experiments, normalized efficiency fell from 0.71 to 0.63 (11% decrease); in validation, from 0.72 to 0.68 (6% decrease). This average masked wide variation across parameterizations—punishment effects ranged from a 44% decrease to a 43% increase in efficiency depending on the game setup.
- The effect of punishment is highly heterogeneous and context-dependent: in some configurations, enabling punishment improved welfare, in others, it caused substantial declines. This heterogeneity was statistically significant and reproducible in high-powered replication.

## 4) Heterogeneity / Moderators

- Communication was by far the most important moderator, tripling the predictive importance of any other factor: having communication enabled robustly increased punishment’s effectiveness.
- Contribution framing (opt-in vs. opt-out) and its interaction with contribution type (variable vs. all-or-nothing) were crucial: opt-out framing improved effectiveness only with variable contributions and worsened it with all-or-nothing, especially when peer outcomes were visible.
- Game length mattered, but only in the presence of communication. Longer games benefited from punishment only with communication; peer outcome visibility attenuated this positive effect.
- Consistently weaker effects were observed for marginal per capita return (MPCR), group size, and surprisingly, the mechanical details of punishment technology (the cost-to-impact ratio of punishment did not robustly predict effectiveness).
- Substantial heterogeneity in punishment effects is attributed to these interacting design parameters rather than population variation, as experiments controlled for population and protocol differences.

## 5) Notes for Prediction

- Both the 14 configuration parameters and the observed efficiency in the control condition (punishment disabled) are strong predictors for the efficiency with punishment enabled. The best model (Elastic Net with interactions) had substantial out-of-sample explanatory power, outperforming both experts and crowds of laypeople, who tend to poorly incorporate the effects of cross-factor interactions.
- The importance of communication, contribution framing, contribution type, outcome visibility, and game length often depends on specific interactions—predictive models must capture this combinatorial structure.
- Single-parameter or linear reasoning generally fails: prediction accuracy depends on attending to high-order interactions among design features as learned in the experiments.
- When making predictions, leveraging the “status quo” efficiency (control, no punishment) as a baseline, then updating based on which interaction moderators are present, reflects best practice learned from the model.
