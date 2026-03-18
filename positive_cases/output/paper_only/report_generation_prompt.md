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

        Paper memo:
                ---
                ## 1) Design & Data

- The study used an integrative experiment varying 14 design parameters across 360 experimental conditions (147,618 decisions from 7,100 participants): 320 “learning” conditions (one trial each for maximum breadth), and 40 “validation” conditions (8–12 replications for precision) in two data collection waves. Each condition had a punishment-enabled (“treatment”) game and a punishment-disabled (“control”) game, identical except for the punishment feature.
- Parameters included group size, game length, contribution type (variable or all-or-nothing), framing (opt-in/out), marginal per capita return (MPCR), communication, peer outcome visibility, actor anonymity, horizon knowledge, punishment/reward availability, costs/technology for punishment/reward, etc.
- Experiments were run with consistent protocols, interfaces, and recruitment to minimize hidden confounds.
- Prediction models were trained on the learning data using PGG parameters and the control condition efficiency to predict treatment (punishment-enabled) efficiency, then tested on validation conditions; comparison was made to the performance of human forecasters (experts and laypeople).

## 2) Efficiency Definition

- **Efficiency** is defined as the ratio of the group’s total payoff to the total payoff under full cooperation (every player contributes their entire endowment every round).  
- Efficiency = 1 implies full cooperation/welfare; lower values reflect inefficiency, either due to non-cooperation or costs of punishment.
- The prediction task uses *regular* efficiency (net earnings scaled by the full cooperation baseline), not normalized efficiency (which is used for some cross-configuration comparisons in the paper).

## 3) Main Findings on Punishment

- **Punishment did not universally improve efficiency:** On average, punishment increased contributions, but did *not* consistently increase overall group efficiency. The average effect of punishment was slightly negative: a decrease in normalized efficiency by 6–11% on average, but with significant variability depending on the parameters—effects ranged from a 43% improvement to a 44% reduction in efficiency across different conditions.
- Notably, punishment technology (the magnitude/cost ratio) mattered less than expected for prediction accuracy; context (communication, framing, interactions) was far more important.
- Predictive models (especially elastic net with interactions) outperformed all human forecasters, with model R² = 0.53 on held-out data compared to near-zero for experts/laypeople.

## 4) Heterogeneity / Moderators

- Strong and systematic heterogeneity in punishment effects was observed. Some configurations saw large efficiency gains, others saw large losses.
- **Most influential moderators (by importance for prediction):**
  - Communication (most important; increased prediction error by 60% when shuffled; always increased punishment’s effectiveness).
  - Contribution framing (opt-in vs. opt-out; 2nd most important; opt-out improved efficiency only with *variable* contribution, but *reduced* it with all-or-nothing).
  - Game length (long games enhanced punishment’s effectiveness only if communication was allowed, especially when peer outcomes were not visible).
  - Peer outcome visibility (moderated framing and game length effects).
  - Availability of rewards (always helped, but less influential than the above).
  - MPCR (higher values slightly increased effectiveness, but effect was small).
- Many parameter effects were contingent on the settings of others—e.g., effect of framing depended on contribution type and outcome visibility.

## 5) Notes for Prediction

- Accurate prediction requires accounting for interactions among parameters, especially the context in which punishment operates rather than mechanistic punishment details.
- Including the efficiency of the control (no-punishment) game as an input boosts predictive accuracy.
- Communication, contribution framing, contribution type, game length, and outcome visibility are especially critical moderators; their interactions should be carefully modeled for highest prediction gain.
- Single-factor generalizations (e.g., “punishment works” or “fails”) are not reliable—the effects are highly context-dependent.
- Human predictions fail to capture the complexity of these interactions—mechanistic models trained on broad parameter sweeps generalize better to new scenarios.

                ---
```
