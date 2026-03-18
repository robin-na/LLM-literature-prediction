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
        - Report style: rules
        - Follow these additional style requirements exactly:
        - Make the report operational and rule-first rather than essay-first.
- Include a ranked predictor list, then a rules section built from if-then statements.
- Each rule should include direction of effect and an approximate numeric range when available.
- Keep narrative explanation minimal and subordinate to actionable guidance.

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
                Let's proceed step-by-step:

1. Load and inspect the data.
2. Compute overall mean efficiencies (punishment vs no-punishment).
3. Analyze treatment effects within paired configurations.
4. Examine heterogeneity of treatment effects by key features.
5. Fit two simple predictive models and extract key signals.
6. Summarize practical heuristics and quantitative guidance.
7. Compile caveats.

Let's begin by loading and reviewing the dataset.

                ---

Paper memo:
                ---
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

                ---
```
