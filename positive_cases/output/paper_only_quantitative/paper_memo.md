## 1) Design & Data

- The study systematically varied 14 key design parameters across 360 experimental PGG conditions using two data collection waves:
  - Wave 1 (learning): 320 unique conditions, single realization each (maximizing breadth), selected via Sobol sequence.
  - Wave 2 (validation): 40 new conditions (20 pairs of treatment/control), each with 8–12 replications (providing precision for model validation).
- Each condition was represented as a 14-dimensional configuration vector, with treatment (punishment enabled) and control (punishment disabled) differing only in the punishment parameter.
- Data consists of 147,618 decisions (contributions, punishments, rewards) from 7,100 participants, all run under standardized protocols to minimize procedural heterogeneity.
- The two-phase design allows for pattern discovery (breadth) and robust model evaluation (precision) on held-out, pre-registered conditions.
- The prediction task is to use the 14 parameters + control efficiency to predict the efficiency outcome with punishment enabled.

## 2) Efficiency Definition

- **Efficiency** is the ratio of the group’s total payoff to what the group would earn with full cooperation every round (the “full cooperation” baseline).
- Efficiency = 1 means full cooperation; lower values indicate less group welfare.
- In this study, regular efficiency (not normalized across parameter differences) is used for model training and prediction as it is more actionable for decision-makers comparing single game configurations.
- (For normalization/cross-design comparisons, "normalized efficiency" scales outcomes between full defection and full cooperation, but prediction is based on regular efficiency.).

## 3) Main Findings on Punishment

- Punishment's effect on efficiency is **highly heterogeneous**: in some parameter settings, it increases efficiency by up to 43%, while in others it reduces efficiency by up to 44%.
- On average, punishment caused a slight reduction in efficiency, but the mean obscures large, regular, and significant moderation by game parameters.
- Models (particularly the elastic net with interactions "E-Net") substantially outperformed human experts and laypeople at predicting when punishment will help or hurt efficiency. The best model achieved out-of-sample R² = 0.53 in validation trials, while crowd averages for both experts and laypeople were near zero.
- Punishment parameters (e.g., the specific cost/technology of punishment) had *surprisingly low* overall predictive value compared to contextual/game design factors.

## 4) Heterogeneity / Moderators

- **Communication** is the single most important moderator: when enabled, it robustly and strongly amplifies punishment’s effectiveness. Shuffling the communication feature raised model prediction error by 60%, more than 3x any other feature.
- **Contribution framing** (opt-in vs. opt-out) is next most important, with effects contingent on other features (notably, contribution type: opt-out boosts punishment effectiveness with variable contributions but *reduces* it when contributions are all-or-nothing; peer outcome visibility further modulates this).
- **Game length**: Longer repeated games only make punishment more effective when communication is allowed; effect attenuated by peer outcome visibility.
- Other meaningful but less dominant factors include *reward availability* (with rewards consistently magnifying punishment effectiveness) and *higher MPCR* (milder dilemma increases punishment’s effectiveness).
- Substantial unexplained heterogeneity remains, even after considering these moderators, underscoring the complexity of prediction.

## 5) Notes for Prediction

- Prediction should always condition on the efficiency observed in the control (punishment-disabled) scenario, in addition to the 14 configuration parameters.
- The integrative approach—jointly varying many parameters—allows both discovery of general patterns and identification of boundary conditions for effects.
- Contextual factors matter substantially more than the mechanical details of punishment itself; models need to represent and interact features such as communication, framing, contribution type, game length, and visibility.
- Feature contributions can be non-linear and involve interactions (e.g., framing × contribution type × outcome visibility).
- Current models outperform intuitive/expert judgment, but complex interactions limit direct interpretability—statistical and machine learning approaches should be preferred for forecasting.
- External/generalization cautions: results are clearest for within-sample parameter variation (homogeneous population, digital PGG environment)—applicability to other populations or naturalistic settings is less certain.
