# Built-in Report Prompt Record

This built-in variant used a multi-stage ensemble generation flow.

## Stage 1 Structured Draft Prompt

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
        - Report style: structured
        - Follow these additional style requirements exactly:
        - Prefer compact sections, bullets, and tables over long narrative paragraphs.
- Explicitly include a "Moderator Matrix" table with each key variable, likely effect direction, confidence, and interaction notes.
- Explicitly include a "Rules of Thumb" section formatted as if-then statements.
- Keep prose concise and operational.

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
                Great! I'll proceed with the statistical analysis, using the provided `df_analysis_learn.csv` dataset, and prepare the requested memo. Here’s a step-by-step plan:

1. **Load and inspect the dataset**.
2. **Compute overall mean efficiencies with and without punishment**.
3. **Analyze treatment effects within paired configurations**.
4. **Assess heterogeneity of treatment effects by key features**.
5. **Fit two predictive models (linear regression, random forest)**.
6. **Extract practical heuristics for when punishment increases/doesn't increase efficiency**.
7. **Quantify expected changes in efficiency for key parameters**.
8. **Summarize findings in a structured Markdown memo**.

Let's begin with loading and inspecting the data.

                ---

Paper memo:
                ---
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

                ---
```

## Stage 1 Quantitative Draft Prompt

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

        Analysis memo:
                ---
                Great! I'll proceed with the statistical analysis, using the provided `df_analysis_learn.csv` dataset, and prepare the requested memo. Here’s a step-by-step plan:

1. **Load and inspect the dataset**.
2. **Compute overall mean efficiencies with and without punishment**.
3. **Analyze treatment effects within paired configurations**.
4. **Assess heterogeneity of treatment effects by key features**.
5. **Fit two predictive models (linear regression, random forest)**.
6. **Extract practical heuristics for when punishment increases/doesn't increase efficiency**.
7. **Quantify expected changes in efficiency for key parameters**.
8. **Summarize findings in a structured Markdown memo**.

Let's begin with loading and inspecting the data.

                ---

Paper memo:
                ---
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

                ---
```

## Stage 2 Synthesis Prompt Template

The exact original stage-2 prompt depended on the intermediate drafts. The template below shows the synthesis prompt structure with placeholders.

```text
You are synthesizing a final prediction-support report from two candidate drafts.

        Your job:
        - Merge the strongest parts of both drafts into one final report.
        - Prefer claims that are numerically grounded, operational for prediction, and consistent with the supplied memos.
        - Remove redundancy, unsupported claims, and stylistic clutter.
        - Output only the final report in Markdown.

        Structured draft:
        ---
        <STRUCTURED_DRAFT>
        ---

        Quantitative draft:
        ---
        <QUANTITATIVE_DRAFT>
        ---

        Final report requirements:
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
        - Report style: ensemble
        - Follow these additional style requirements exactly:
        - Produce a final integrated report that combines strengths of multiple drafting styles.
- The final result should be compact, operational, quantitatively grounded, and internally consistent.
- Favor content that survives across multiple candidate draft forms over content that appears only once.

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
                Great! I'll proceed with the statistical analysis, using the provided `df_analysis_learn.csv` dataset, and prepare the requested memo. Here’s a step-by-step plan:

1. **Load and inspect the dataset**.
2. **Compute overall mean efficiencies with and without punishment**.
3. **Analyze treatment effects within paired configurations**.
4. **Assess heterogeneity of treatment effects by key features**.
5. **Fit two predictive models (linear regression, random forest)**.
6. **Extract practical heuristics for when punishment increases/doesn't increase efficiency**.
7. **Quantify expected changes in efficiency for key parameters**.
8. **Summarize findings in a structured Markdown memo**.

Let's begin with loading and inspecting the data.

                ---

Paper memo:
                ---
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
