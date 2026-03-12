## 1) Design & Data

- The study used an integrative, factorial experimental design, systematically varying 14 key game parameters across 360 unique Public Goods Game (PGG) conditions. These included group size, game length, marginal per capita return (MPCR), communication, contribution type/framing, peer outcome visibility, actor anonymity, horizon knowledge, and the availability and details of punishment/reward mechanisms, among others.
- Each experiment comprised two games—a control (punishment disabled) and a treatment (punishment enabled)—with identical parameters except for the punishment mechanism.
- Data were collected in two waves:
  - Wave 1 (learning): 320 conditions sampled once each using a Sobol sequence for maximum design space coverage (single realization per condition for breadth).
  - Wave 2 (validation): 40 new conditions drawn randomly, executed with 8-12 trials each for precision and robust estimation, also enabling human forecast comparisons.
- In total: 147,618 decisions from 7,100 participants, yielding both breadth and depth for out-of-sample prediction and generalization.

## 2) Efficiency Definition

- The main outcome for the prediction task is *efficiency*, defined as the ratio of the group’s total payoff to the payoff a fully cooperative group would achieve (i.e., if all members contribute fully every round and incur no punishment/reward costs):
  
  > Efficiency = (group total earnings) / (earnings under full cooperation in the same configuration)
  
- An efficiency of 1 means full cooperation with no losses to punishment/reward; lower values indicate less cooperation, more costly punishment, or both.
- For cross-game comparison, an additional *normalized efficiency* metric is used, but for prediction tasks—since configuration is held constant—regular efficiency is the relevant quantity.

## 3) Main Findings on Punishment

- **Punishment increases contributions** (average contributions rose from ~73% to ~80% of endowment), but the impact on efficiency (welfare, after accounting for punishment costs) is highly heterogeneous.
- On average, *punishment reduced efficiency*: from 0.71 to 0.63 (11% decrease) in the learning set, and from 0.72 to 0.68 (6% decrease, marginally significant) in the validation set.
- Crucially, in some configurations, punishment *dramatically increases* efficiency (up to +43%), while in others it *strongly decreases* it (down to -44%).
- The best-performing model (Elastic Net with two-way interactions) predicted these effects better than both expert and lay human forecasters (out-of-sample R² = 0.53 for the model; humans ~0.02-0.05).
- Key factors:
  - **Communication** is by far the most important factor: Model error increases by 60% if communication is shuffled. Allowing communication (even basic chat) robustly increases the effectiveness of punishment for group welfare.
  - **Contribution framing** (opt-in vs. opt-out) is the next most important; the effect of framing depends on whether contributions are variable (can choose amounts) or all-or-nothing, with further modulation by peer outcome visibility.
  - **Game length** enhances punishment effectiveness, but only with communication, and less so if outcomes are visible.
  - **Availability of rewards** and higher MPCR also generally enhance punishment’s positive effects, but MPCR’s effect is relatively modest for predictive purposes.
  - Surprisingly, *mechanical* aspects of punishment (e.g., punishment cost/technology) had minimal impact on prediction accuracy compared to social/contextual factors.

## 4) Heterogeneity / Moderators

- There is substantial and significant heterogeneity in punishment’s impact across configurations, as confirmed by formal statistical tests (Cochran’s Q, permutation tests).
- Sources of heterogeneity and key interactions:
  - **Communication**: The dominant moderator; absence can make punishment harmful, presence often makes it beneficial.
  - **Contribution Framing × Contribution Type**: Opt-out framing helps when contributions are variable, harms when they are all-or-nothing; effect is amplified by visible peer outcomes for all-or-nothing, attenuated for variable.
  - **Game Length × Communication × Outcome Visibility**: Long games help only with communication; visible outcomes dampen this benefit.
  - **Reward availability** and **MPCR** are positive but less interactive with other features.
  - *Heterogeneity is not due to population differences or procedural artifacts,* as all experiments shared identical protocols; thus, differences are confidently attributed to game parameters.

## 5) Notes for Prediction

- Use all 14 configuration parameters plus control (no-punishment) efficiency as features.
- Model structure should allow for *strong non-additive interactions* (e.g., communication × game length, framing × contribution type × visibility).
- Control efficiency provides considerable predictive power, likely capturing unmodeled aspects and baseline group dynamics.
- Model performance demonstrates that aggregating multiple weak contextual clues is crucial—human forecasters failed in this integration, especially non-linearities and higher-order interactions.
- Factors like “punishment technology” (the mechanical details of cost/magnitude) are less useful for prediction than context-sensitive features, especially communication and framing.
- Regular (not normalized) efficiency is the target for prediction, as only one configuration is considered per instance.
- Takeaway: The question is not “does punishment work?” but “when does it work for group welfare, and for whom?”—requiring context-aware, interaction-sensitive modeling.
