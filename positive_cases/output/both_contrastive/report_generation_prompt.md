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
        - Report style: contrastive
        - Follow these additional style requirements exactly:
        - Explicitly separate where the paper memo and analysis memo agree, partially agree, or disagree.
- Include an "Agreement / Disagreement Matrix" table.
- Reconcile conflicts and explain which evidence should dominate prediction when they diverge.
- The final predictive guidance should clearly indicate whether it is supported by paper, data, or both.

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
                Great, I'll perform the requested analysis on the uploaded dataset. Here's the plan:

1. **Load the Data** and conduct a brief review.
2. **Compute Overall Means** for efficiency with and without punishment.
3. **Estimate Treatment Effects** in paired configs by config-level aggregation.
4. **Analyze Heterogeneity** by the key parameters.
5. **Fit Predictive Models** (linear regression and random forest) to predict the outcome, and extract key feature signals.
6. **Practical Heuristics**: distill insights about when punishment boosts efficiency.
7. **Quantitative Guidance**: numerical estimates of effect sizes and efficiency ranges.
8. **Caveats** section.

I’ll then assemble a concise memo in Markdown with tables and statistical outputs.

Let's get started by loading and inspecting the data.

                ---

Paper memo:
                ---
                ## 1) Design & Data

- The study utilizes an integrative, high-throughput experimental approach. It systematically varied 14 design parameters across 360 unique conditions in public goods games (PGGs), yielding over 147,000 decisions from 7,100 participants. Parameters included group size (2-20), game length (1-30 rounds), contribution type (variable vs. all-or-nothing), contribution framing (opt-in vs. opt-out), MPCR, communication, peer outcome visibility, anonymity, knowledge of horizon, punishment and reward mechanisms (on/off), peer incentive cost, punishment/reward technology, and more.
- Each experiment consisted of a matched pair: one control (punishment disabled) and one treatment (punishment enabled), sharing all other configuration values.
- The design consisted of two data waves: Wave 1 (learning/space-filling, single trial per 320 conditions) and Wave 2 (validation/higher precision, 8-12 trials across 40 conditions).
- All experiments were run on a unified platform with identical protocols to minimize confounds.
- Predictive models (elastic net, random forest, XGBoost, MLP, OLS) were evaluated using out-of-sample performance (R², RMSE) on held-out validation settings, with comparison to human forecasters (experts and laypeople).

## 2) Efficiency Definition

- **Efficiency** is defined as the ratio of the group’s total payoff to the maximum possible payoff (i.e., if everyone contributed fully every round and no coins were lost to punishment/reward costs). 
- Mathematically:  
  \[
  \text{Efficiency} = \frac{\text{Total group earnings}}{\text{Earnings under full cooperation}}
  \]
  Values near 1 indicate full cooperation; lower values reflect less cooperation or higher punishment/reward losses.
- For comparison across games with different structure, a "normalized efficiency" metric is sometimes used, which adjusts for differences in minimum and maximum possible outcomes for each setup.

## 3) Main Findings on Punishment

- **Punishment consistently increased contributions** (e.g., from 73% to 80% average endowment contributed), but did not reliably increase efficiency: average efficiency actually **declined when punishment was enabled** due to the costs associated with punishing, though effects are highly heterogeneous.
- The effect of punishment on efficiency ranged from **+43% to -44%** depending on other game parameters.
- Prediction models (especially elastic net with interaction terms) **outperformed human experts at predicting when punishment would be beneficial vs. detrimental**.
- The **most important factor for benefit from punishment was the availability of communication**, which had a much larger impact than any other feature. When communication was enabled, punishment was much more likely to improve efficiency.
- Other consistently positive moderators: reward availability and higher MPCR (marginal per capita return).
- **Complex interactions:** for example, opt-out contribution framing increases punishment’s effectiveness only for variable contributions, but can decrease it for all-or-nothing contributions, particularly when peer outcomes are visible. Game length increases effectiveness of punishment primarily when communication is allowed.

## 4) Heterogeneity / Moderators

- Heterogeneity was substantial and robust: punishment effects on efficiency were sometimes dramatically positive or negative within the same participant pool and protocol, depending only on configuration.
- **Key moderators and interactions:**
  - **Communication:** Dominant predictor, amplifies punishment’s effectiveness.
  - **Contribution Framing (opt-in/opt-out):** Second most important, with effects contingent on type of contribution (variable vs all-or-nothing) and outcome visibility.
  - **Game Length:** Important, but only increases punishment effectiveness with communication; effect dampened by peer outcome visibility.
  - **Outcome Visibility:** Modulates framing and game-length effects, and can either attenuate or amplify punishment’s impact depending on the situation.
  - **Reward mechanisms:** The presence of rewards boosts likelihood that punishment is welfare enhancing.
  - **Punishment technology (severity vs. cost):** Surprisingly little predictive power in aggregate models, implying context and interaction matter more than the raw punishment ratio.
- Between-game heterogeneity was largely attributable to configuration, not random noise.

## 5) Notes for Prediction

- Use the 14 CONFIG parameters and control game efficiency as model input.
- Prioritize communication, contribution framing, and interaction terms in feature engineering or model interpretation.
- Consider conditional effects: e.g., communication amplifies punishment effectiveness in long games; opt-out framing can help or harm depending on contribution type/outcome visibility.
- Simple main effects or averages mask substantial variation; interpretable interaction terms are key.
- Human intuition (even expert) is poor at integrating these factors; data-driven modeling is more reliable.
- Results and insights are strongest within the design space tested; external validity should be treated cautiously.

                ---
```
