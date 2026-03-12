## 1) Design & Data

- The study systematically varied 14 design parameters (CONFIG features) across 360 experimental Public Goods Game (PGG) conditions, creating pairs of games with identical parameters except for punishment (enabled/disabled).
- Two data collection waves: a “learning” wave (320 conditions, one trial each, for breadth) and a “validation” wave (20 new conditions × 2, 8–12 trials each, for precision).
- 147,618 decisions were made by 7,100 participants across all conditions. All experiments used consistent protocols, interfaces, and recruitment to minimize hidden moderators.
- The dataset is well-suited for out-of-sample prediction: models are trained on learning wave and tested on held-out validation wave.

## 2) Efficiency Definition

- **Conventional Efficiency**: Ratio of a group’s total earnings to the earnings of a fully cooperative group (everyone contributes fully every round):  
  `Efficiency = (Group earnings) / (Earnings under full cooperation)`  
  This ranges from 0 (no cooperation) to 1 (full cooperation); 1 means the group achieves collectively optimal payoffs.
- Used for the human- and model-based prediction tasks, as it's simple and comparable across control/treatment games with identical configuration.
- **Normalized Efficiency**: For cross-configuration comparison, a more complex measure scales group earnings relative to both full cooperation and full defection scenarios. This is primarily for meta-analytic purposes, not single-instance predictions.

## 3) Main Findings on Punishment

- Punishment **increased average contributions**, but its effect on efficiency (welfare) was highly heterogeneous:
  - Average effect across all experiments: **punishment reduced efficiency** slightly (by 6–11%) but with large variation across settings.
  - In some configurations, punishment improved efficiency by up to 43%; in others, it reduced it by up to 44%.
- **Key determinants of positive/negative effects:**
  - **Communication**: Most important, enabling communication before/after rounds increased the positive effect of punishment (and was three times more predictive than any other feature).
  - **Contribution Framing**: Second most important. "Opt-out" (endowment starts in public fund) improved punishment effectiveness with variable contributions, but was harmful with all-or-nothing contributions—an effect modulated by whether others’ outcomes were visible.
  - **Game Length**: Longer games increased punishment effectiveness only if communication was enabled; this benefit weakened if outcome visibility was also enabled.
  - **Availability of Rewards**: Consistently enhanced the effect of punishment on efficiency, though it mattered less for variable prediction than communication or framing.
- Unexpectedly, **punishment’s mechanical details** (e.g., punishment cost/magnitude) were far less important for predicting welfare outcomes than contextual factors like communication or contribution framing.

## 4) Heterogeneity / Moderators

- Substantial, statistically significant heterogeneity in punishment’s effect size was observed, attributable mainly to experimentally-varying parameters, not population/sample idiosyncrasies.
- Interaction effects are critical: 
  - **Framing × Contribution Type × Outcome Visibility**
  - **Game Length × Communication × Outcome Visibility**
- Prediction accuracy improvements are greatest when factoring in moderator interactions—as opposed to assuming independent or main effects.
- Even within homogeneous populations, effects ranged broadly, suggesting real complexity and context-dependence in “punishment works” generalizations.
- These findings stress the need for integrative, high-dimensional predictive approaches rather than single-parameter investigations.

## 5) Notes for Prediction

- The best-performing predictive model used only: the 14 CONFIG/game parameters and the efficiency observed in the control condition (punishment off) to predict efficiency in the treatment (punishment on).
- Communication, contribution framing, reward availability, game length, outcome visibility, and MPCR are the most informative CONFIG variables for predicting when punishment will help or hurt welfare.
- Interactions among CONFIG variables are highly consequential; using only main effects will miss key boundary conditions.
- Human experts and collective lay predictors both underperformed the model: effective prediction requires integrating complex, interacting effects, not relying on intuition or single-variable reasoning.
- The observed patterns and model accuracy are likely optimistically high, as the population/sample was homogeneous.
- For single-instance prediction, **use the control efficiency and the specific 14 CONFIG parameters**. Cross-condition or meta-analytic extrapolation should consider population and protocol differences.

---

**Key takeaway**: To improve prediction accuracy, focus on the context-sensitivity and interactions among CONFIG parameters, with particular attention to communication, framing, and the availability of alternative incentives. Use both main effects and interaction terms in predictive models.
