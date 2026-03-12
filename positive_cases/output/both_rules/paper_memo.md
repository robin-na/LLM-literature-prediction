## 1) Design & Data

- The study uses an integrative experiment across 360 different PGG conditions, varying 14 design parameters and collecting 147,618 decisions from 7,100 participants. Data collection occurred in two waves: Wave 1 (learning experiments) sampled 320 conditions (1 trial each), and Wave 2 (validation experiments) sampled 40 new conditions (multiple trials per condition for higher precision).
- Each prediction instance provides: 14 configuration parameters and the average efficiency of the control condition (punishment disabled), aiming to predict efficiency when punishment is enabled.
- Design parameters include: group size, game length, contribution type, framing, MPCR, communication, peer outcome visibility, actor anonymity, horizon knowledge, punishment/reward parameters, and peer incentive costs (see Table 1 in the paper for full list).
- The experimental setup ensures all other conditions are held constant between each paired control/treatment game except for punishment, maximizing interpretability of the punishment effect.

## 2) Efficiency Definition

- Efficiency (the main outcome to predict) is defined as the ratio of the group's total earnings to the total earnings of a fully cooperative group (everyone contributes fully every round, with no punishment or rewarding).
- Formula:  
  `efficiency = (group’s total payoff) / (full cooperation payoff)`  
  Efficiency = 1 means full cooperation; lower values indicate less cooperation.
- For cross-configuration comparison, "normalized efficiency" is sometimes used, but for prediction tasks and model training, regular (unnormalized) efficiency is used as it matches human intuitions and task requirements.

## 3) Main Findings on Punishment

- Punishment’s effect on efficiency is highly heterogeneous: it ranges from +43% to -44% depending on design parameters.
- On average, punishment increased contributions but had a nuanced effect on efficiency:  
  - In learning experiments: Average normalized efficiency decreased from 0.71 to 0.63 (11% decrease).
  - In validation, decrease from 0.72 to 0.68 (6%)—but with many conditions showing positive or strongly negative effects, indicating high heterogeneity.
- Key determinant: the effect size of punishment on efficiency varies strongly by context. There is no universal positive or negative effect.
- Predictive models (E-Net best) using config parameters and control efficiency outperform both human experts and laypeople in forecasting punishment-enabled efficiency. Human forecasters (including domain experts) did not outperform naive baselines or models.

## 4) Heterogeneity / Moderators

- Communication is the single most important moderator: enabling communication increases the effectiveness of punishment in promoting efficiency but interacts with other features, e.g., game length.
- Contribution framing (opt-in vs. opt-out) is also critical:
  - Opt-out enhances punishment’s effectiveness for variable contribution types but reduces it for all-or-nothing contributions, especially when peer outcomes are visible.
- Game length boosts punishment effectiveness only when communication is available; the effect is dampened if peer outcome visibility is enabled.
- Reward options and higher MPCR are positive—but effect sizes are smaller than the above.
- Surprisingly, the specific parameters of punishment (e.g., technology, cost/multiplier) matter much less than expected—context and interactions among the other parameters are far more predictive.

## 5) Notes for Prediction

- Integrate config parameters and control efficiency: Both direct game design variables (the 14 config parameters) and the efficiency in the no-punishment condition provide strong predictive signal for punishment-enabled efficiency.
- Focus on key moderators: Communication, contribution framing/type, peer outcome visibility, and game length drive the largest effects and often interact complexly.
- Ignore direct effect of punishment "technology" except in interaction: Direct parameterization of punishment strength and cost was much less predictive than expected.
- Expect context sensitivity—not universal trends: Model predictions should account for contingent effects and interactions—single-factor “main effect” explanations will not generalize.
- Use regular efficiency for out-of-sample prediction tasks where the goal is to predict the effect of punishment enabling on the identical configuration, as was done in validation and forecasting tasks in the study.
- Consider limitations: External validity may be restricted (mechanical MTurk population, stylized PGGs), and the model may somewhat overestimate generalizability due to the experiment’s homogeneous population and tightly controlled protocols.
