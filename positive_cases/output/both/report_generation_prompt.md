# Built-in Report Prompt Record

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
                Great! I see the dataset. I'll proceed with the analysis and generate the requested memo.

### Plan:
1. **Load the data, inspect structure, and preprocess as needed.**
2. **Compute the overall mean efficiency with and without punishment.**
3. **Analyze paired configurations for within-pair treatment effects.**
4. **Assess heterogeneity of treatment effects across key features.**
5. **Fit two predictive models (linear regression & random forest) for treatment effects.**
6. **Extract and summarize practical heuristics and quantitative guidance.**
7. **Prepare Markdown memo with tables and results.**

Let's begin by loading the data and inspecting its structure.

                ---

Paper memo:
                ---
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

                ---
```
