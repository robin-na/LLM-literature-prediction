# Built-in Report Prompt Record

This built-in variant used a two-stage generation flow.

## Stage 1 Draft Prompt

```text
You are writing a prediction-support paper to help a model estimate how enabling punishment changes efficiency in new public goods games.

        Requirements:
        - Use the available memos as primary evidence (depending on the selected source mode).
        - Source mode: both. Use both the analysis memo and the paper memo.
        - Explain the key variables and how they map to experimental design.
        - Provide actionable predictive guidance, not just a summary.
        - Keep the report grounded in the data and the published paper.
        - Output in Markdown with clear section headers.
        - Target length: 800 to 1400 words.
        - Do NOT include any final-answer formatting or "Final Answer" template.
        - Assume the protocol and online environment are consistent across studies; differences are driven by the CONFIG parameters.
        - Include concrete numerical estimates and tables drawn from the available evidence.
        - Report style: freeform
        - Follow these additional style requirements exactly:
        - Write a balanced narrative synthesis with clear headings, concrete numbers, and actionable guidance.
- Use prose as the default form, with tables where helpful.

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

        Analysis memo:
                ---
                Understood—I'll begin by loading the data, inspecting key variables, and running the requested analyses step by step before assembling the final memo. 

Let's start by loading the dataset and summarizing relevant variables.

                ---

Paper memo:
                ---
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

                ---
```

## Stage 2 Refinement Prompt Template

The exact original stage-2 prompt depended on the stage-1 draft. The template below shows the prompt structure with a placeholder.

```text
You are revising a draft prediction-support report.

        Your job:
        - Audit the draft for unsupported claims, leakage across source constraints, vague statements, and weak quantitative grounding.
        - Rewrite the report so it is tighter, better supported, and more useful for prediction.
        - Preserve useful content from the draft only when it is supported by the memos.
        - Output only the improved final report in Markdown.

        Draft report:
        ---
        <STAGE_1_DRAFT_REPORT>
        ---

        Use these report requirements for the rewrite:
        You are writing a prediction-support paper to help a model estimate how enabling punishment changes efficiency in new public goods games.

        Requirements:
        - Use the available memos as primary evidence (depending on the selected source mode).
        - Source mode: both. Use both the analysis memo and the paper memo.
        - Explain the key variables and how they map to experimental design.
        - Provide actionable predictive guidance, not just a summary.
        - Keep the report grounded in the data and the published paper.
        - Output in Markdown with clear section headers.
        - Target length: 800 to 1400 words.
        - Do NOT include any final-answer formatting or "Final Answer" template.
        - Assume the protocol and online environment are consistent across studies; differences are driven by the CONFIG parameters.
        - Include concrete numerical estimates and tables drawn from the available evidence.
        - Report style: refined
        - Follow these additional style requirements exactly:
        - Produce a clean final report only.
- The report should read like a corrected and tightened version of an earlier draft.
- Eliminate unsupported claims, vague wording, and claims that are not grounded in the supplied memos.
- Be explicit about uncertainty when evidence is mixed or weak.

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

        Analysis memo:
                ---
                Understood—I'll begin by loading the data, inspecting key variables, and running the requested analyses step by step before assembling the final memo. 

Let's start by loading the dataset and summarizing relevant variables.

                ---

Paper memo:
                ---
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

                ---

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
```
