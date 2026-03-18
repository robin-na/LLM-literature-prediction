# Built-in Report Prompt Record

```text
You are writing a prediction-support paper to help a model estimate how enabling punishment changes efficiency in new public goods games.

        Requirements:
        - Use the available memos as primary evidence (depending on the selected source mode).
        - Source mode: paper_only. Use ONLY the paper memo. Do not introduce evidence or claims from the data analysis. If the paper lacks needed numbers, state the gaps explicitly.
        - Explain the key variables and how they map to experimental design.
        - Provide actionable predictive guidance, not just a summary.
        - Keep the report grounded in the data and the published paper.
        - Output in Markdown with clear section headers.
        - Target length: 800 to 1400 words.
        - Do NOT include any final-answer formatting or "Final Answer" template.
        - Assume the protocol and online environment are consistent across studies; differences are driven by the CONFIG parameters.
        - Include concrete numerical estimates and tables drawn from the available evidence.
        - Report style: quantitative
        - Follow these additional style requirements exactly:
        - Prioritize numeric evidence over narrative explanation.
- Put tables first whenever possible.
- Include at least three quantitative tables: overall effects, moderator effects, and prediction guidance ranges.
- Minimize qualitative wording unless it clarifies how to use the numbers.

        Prediction task context:
- Each prediction instance provides values for 14 CONFIG parameters plus the average efficiency of the control game (punishment disabled).
- The goal is to predict the average efficiency of the same game when punishment is enabled.
- Efficiency is the ratio of the group’s total payoff to the total payoff of a fully cooperative group (everyone contributes fully every round).
- Thus, efficiency = 1 means full cooperation; lower values indicate less cooperation.

        Include these sections:
        1) Title
        2) Abstract
        3) Background & Definitions (explicitly restate the prediction task: given 14 CONFIGs plus control efficiency, predict treatment efficiency)
        4) Data & Variables (explicitly list and define these 14 CONFIG parameters: CONFIG_playerCount, CONFIG_numRounds, CONFIG_MPCR, CONFIG_allOrNothing, CONFIG_chat, CONFIG_defaultContribProp with 0/1 coding, CONFIG_punishmentCost, CONFIG_punishmentMagnitude, CONFIG_showOtherSummaries, CONFIG_showNRounds, CONFIG_showPunishmentId, CONFIG_rewardExists, CONFIG_rewardCost, CONFIG_rewardMagnitude)
        5) Empirical Patterns (punishment effects and heterogeneity)
        6) Quantitative Summary (tables with numeric effects and model outputs)
        7) Predictive Guidance (rules of thumb and feature interactions with numeric ranges)
        8) Limitations & Open Questions
        9) How To Use This For Predictions (concise bullet list)

        Column definitions:
        - CONFIG_configId: Unique configuration identifier; paired punishment/no-punishment conditions share the same configId.
- CONFIG_playerCount: Number of players in the game.
- CONFIG_numRounds: Number of rounds in the game.
- CONFIG_showNRounds: Whether the total number of rounds is shown to players.
- CONFIG_endowment: Endowment (coins) given to each player per round.
- CONFIG_multiplier: Public-good multiplier applied to total contributions.
- CONFIG_allOrNothing: If true, contributions are all-or-nothing rather than continuous amounts.
- CONFIG_chat: Whether chat is enabled between players.
- CONFIG_defaultContribProp: Contribution framing: 0 = opt-in (default keep; must actively give), 1 = opt-out (default contribute; must actively keep).
- CONFIG_punishmentExists: Whether punishment is enabled in the game.
- CONFIG_punishmentCost: Cost to the punisher per unit of punishment.
- CONFIG_punishmentMagnitude: Coins deducted from a punished player per unit of punishment.
- CONFIG_rewardExists: Whether rewards are enabled in the game.
- CONFIG_rewardCost: Cost to the rewarder per unit of reward.
- CONFIG_rewardMagnitude: Coins added to a rewarded player per unit of reward.
- CONFIG_showOtherSummaries: Whether peer outcomes are shown each round.
- CONFIG_showPunishmentId: Whether the identity of punishers or rewarders is shown.
- CONFIG_showRewardId: Whether the identity of rewarders is shown.
- CONFIG_contributionDuration: Time window (seconds) to contribute.
- CONFIG_outcomeDuration: Time window (seconds) to view outcomes.
- CONFIG_summaryDuration: Time window (seconds) to view summary.
- CONFIG_basePay: Fixed base payment (currency units) to participants.
- CONFIG_conversionRate: Conversion rate from coins to payout.
- CONFIG_treatmentName: Human-readable treatment label.
- CONFIG_punishmentTech: Punishment effectiveness = punishmentMagnitude / punishmentCost.
- CONFIG_MPCR: Marginal per-capita return = multiplier / playerCount.
- CONFIG_scaledPunishmentCost: Scaled punishment cost = punishmentCost / endowment.
- CONFIG_MPCR_adjusted: Adjusted MPCR = multiplier / num_actual_players.
- CONFIG_rewardTech: Reward effectiveness = rewardMagnitude / rewardCost.
- num_completed_first_round: Number of players completing the first round.
- num_failed_readycheck: Count of players failing the ready check.
- num_started_game: Number of players who started the game.
- num_started_and_readycheck: Number of players who both started and passed ready check.
- num_actual_players: Number of players who actually participated.
- first_round_with_removed_player: First round in which a player was removed (if any).
- total_coin_gen: Total coins generated by the group across all rounds.
- total_costs: Total punishment/reward costs paid by participants.
- total_penalties: Total penalties assigned to punished players.
- total_rewards: Total rewards assigned to rewarded players.
- round_total_coin_gen: Sum of all players' round payoffs aggregated across rounds.
- round_defecting_coin_gen: Coins generated if everyone fully defects (keeps endowment).
- round_max_coin_gen: Coins generated if everyone fully cooperates.
- itt_efficiency: Efficiency = total coins generated / max possible coins (full cooperation).
- itt_relative_efficiency: Efficiency normalized between full defection and full cooperation (with smoothing).
- valid_number_of_starting_players: True if actual starting players are within the allowed deviation from planned playerCount.
- paired_config: True if this config has both punishment and no-punishment variants in the data.

        Paper memo:
                ---
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

                ---
```
