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

        Paper memo:
                ---
                ## 1) Design & Data

- The study employs an “integrative experiment” varying **14 design parameters** across 360 unique Public Goods Game (PGG) configurations, resulting in 147,618 decisions from 7,100 participants.
- Each experimental configuration is defined by a 14-dimensional vector specifying parameters such as group size, game length, contribution structure, communication, punishment availability, reward mechanisms, marginal per capita return (MPCR), peer outcome visibility, and more.
- For each configuration, there are two parallel games: a control (punishment disabled) and a treatment (punishment enabled), keeping all other parameters identical.
- Data collection occurred in two phases:
  - **Wave 1**: 320 conditions (single realization each, maximizing breadth).
  - **Wave 2**: 40 new conditions (8-12 realizations each, maximizing precision; preregistered, used for validation and human-machine prediction comparison).

## 2) Efficiency Definition

- **Efficiency** in each game is the ratio:
  - `Efficiency = (Group total earnings) / (Earnings if all members fully cooperate every round; no punishment/reward)`
  - Efficiency = 1 means full cooperation; less than 1 means some resources are lost (either to under-contribution or punishment/reward costs).
- **Normalized efficiency** is also reported (main text often focuses on it for cross-configuration comparison), but the human prediction task directly uses standard efficiency as above.

## 3) Main Findings on Punishment

- The impact of enabling punishment is **highly heterogeneous**:
  - Across configurations, punishment effects on efficiency range from a **43% increase** to a **44% decrease** (i.e., punishment can be highly beneficial or highly detrimental depending on context).
  - On average, punishment increased contributions but *often reduced efficiency* (due to the cost of punishment actions).
  - In the learning phase, punishment decreased normalized efficiency (0.71 to 0.63; 11% drop). In validation, the decrease was smaller (0.72 to 0.68; 6% drop), but both phases included individual cases with large gains or losses.
- **Key drivers** of positive punishment effects:
  1. **Communication** (chat enabled) is the most important factor—when allowed, it consistently enhances the effectiveness of punishment and prediction accuracy (shuffling this parameter increases prediction error by 60%).
  2. **Contribution framing** (opt-in vs. opt-out) is the second most important; opt-out framing increases punishment’s effect only if participants can make variable (not all-or-nothing) contributions.
  3. **Interaction effects**: For instance, longer games enhance punishment only if communication is available; with outcome visibility, this effect weakens.
- Surprising null: Technical details of the punishment rule (e.g., ratio of penalty to cost) mattered *less* than social/contextual features.

## 4) Heterogeneity / Moderators

- Substantial, reliable heterogeneity in punishment effects is observed, even with tightly controlled protocols and homogeneous subject pools.
- *Measured moderators* that predict the sign/magnitude of punishment’s impact:
  - Communication (dominant)
  - Contribution framing (opt-in/opt-out)
  - Contribution type (variable vs. all-or-nothing)
  - Game length (number of rounds)
  - Peer outcome visibility
  - MPCR (marginal per capita return; effect is consistent but relatively weak)
- **Strong interactions**: Effects of framing, game length, and peer visibility depend on each other (see above).
- Null or weak moderators: Structural features of the punishment mechanism itself are less predictive than social context and interaction structure.
- **Models trained on these moderators outperformed both expert and lay forecasts** for new (held-out) cases.

## 5) Notes for Prediction

- **Prediction inputs**: 14 CONFIG parameters + efficiency of control (no punishment) condition.
- **Prediction target**: average efficiency of same config with punishment enabled (as defined above).
- For improved prediction:
  - Weight *social context* (communication, visibility, framing, contribution type) heavily.
  - Be alert to strong cross-level interactions (e.g., game length matters only if communication is present).
  - Do not overemphasize punishment technology (cost:impact ratio) relative to social/contextual features, as these structural details are surprisingly weak predictors.
- The observed heterogeneity is genuine and arises from parameter combinations, not random error or researcher variation.
- For new/uncertain cases, models trained on past experiment data outperform both experts and crowds.

                ---
```
