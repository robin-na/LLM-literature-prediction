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
                The dataset has loaded successfully with 366 rows and 63 columns. Key columns present for the analysis are as described, including configuration parameters and efficiency outcomes. Next, I'll begin the analysis and prepare the memo as specified.

---

#### Analysis plan:
1. Data Overview — summary, treatment split.
2. Global Effect of Punishment (mean efficiency with/without).
3. Paired Treatment Effects (paired configurations, config-level diff).
4. Heterogeneity Analysis (by key features, grouped aggregations).
5. Predictive Modeling (linear regression, random forest).
6. Practical Heuristics.
7. Quantitative Summary/tables.
8. Caveats.

---

Let's start with **Data Overview** and stepwise calculations.

---

### 1) Data Overview

- How many games, how many are punishment/no-punishment.
- Efficiency distributions.

Let's compute these and show a small table to set the stage.

                ---

Paper memo:
                ---
                ## 1) Design & Data

- The study used an "integrative experiment" approach, exhaustively varying 14 design parameters (CONFIG) across 360 unique public goods game (PGG) conditions using both learning (320 conditions, single realization each) and validation (40 conditions, 8-12 replications each) samples. Across both waves, 7,100 participants made 147,618 decisions (contributions, punishments, rewards).
- Each experimental instance was run in paired conditions: control (punishment disabled) and treatment (punishment enabled), holding all other design parameters identical.
- The 14 parameters include group size, game length, contribution type (variable/all-or-nothing), contribution framing (opt-in/opt-out), MPCR (marginal per capita return), communication availability, peer outcome visibility, actor anonymity, horizon knowledge, and technology/cost settings for punishment/reward, among others.
- This systematic manipulation allows direct comparison of punishment effects, relative feature importance, and interactions among variables, with minimal hidden moderators (e.g., same recruitment/interface for all sessions). Data from the control condition serves as a key input for predicting the outcome in the punishment-enabled condition.

## 2) Efficiency Definition

- **Efficiency** is the primary outcome metric. It is defined as the ratio of the group’s actual total earnings to the total earnings achievable by a fully cooperative group (everyone always contributes fully, no punishment/reward costs incurred). Thus,
  ```
  Efficiency = (Group’s observed total payoff) / (Total payoff under full cooperation)
  ```
  Efficiency = 1 corresponds to maximum cooperation and no losses to punishment/reward; lower values indicate reduced welfare due to free-riding and/or the costs of sanctioning.
- For cross-condition comparisons, a normalized efficiency metric is also used (scaling relative to both full cooperation and full defection), but within the prediction task, regular efficiency is used since it is more intuitive and applicable to predicting single-configurations (i.e., treatment vs. control for the same parameter set).

## 3) Main Findings on Punishment

- Punishment generally increases contributions but does **not** always increase efficiency. On average, punishment led to reduced efficiency across all configurations (11% decline in learning phase, ~6% in validation), but this average masks **large heterogeneity**: in some settings, punishment improved efficiency dramatically (up to +43%), while in others, it was highly detrimental (as much as -44%).
- The effect of punishment is not determined by a single factor, but by complex, often contingent, interactions among multiple game parameters.
- Feature importance analyses revealed:
  - **Communication** (enabled/disabled) is by far the most important and consistent predictor of when punishment improves welfare, tripling prediction error when shuffled.
  - Availability of reward mechanisms and higher MPCR modestly and consistently improve punishment’s effect, but are much less predictive than communication.
  - Punishment technical parameters (cost, effectiveness) matter much less than expected: their influence on the welfare effect of punishment is minimal compared to contextual features (communication, framing, etc.).
- Predictive models (E-Net, OLS, RF, MLP, XGB) using the 14 parameters and control efficiency outperformed both expert and lay human forecasters. Human forecasters, including field experts, struggled to integrate the interacting effects and typically performed no better than baseline averaging.

## 4) Heterogeneity / Moderators

- There is **substantial, systematic heterogeneity** in punishment's effects, fully attributable to experimentally manipulated parameters (since all else was held constant).
- Key interactions:
  - **Contribution Framing**: Opt-out framing enhances punishment’s effectiveness when variable contributions are allowed, but *reduces* it when contributions are all-or-nothing; further modulated (amplified, attenuated) by peer outcome visibility.
  - **Game Length**: Extending the number of rounds boosts punishment effectiveness only when communication is allowed; this positive effect is dampened if outcomes are visible.
- Other tested factors included anonymity, group size, horizon knowledge, and more. The heterogeneity is not random noise but systematic, with I² heterogeneity statistic indicating real differences by condition.
- These findings point out that neither “punishment works” nor “punishment fails” is generally correct—the context (“when and for whom”) is decisive.

## 5) Notes for Prediction

- The best predictors for whether punishment will increase efficiency are: communication (most important), contribution framing, contribution type, game length, peer outcome visibility, and to a lesser degree, availability of reward.
- Many effects depend on **interactions** rather than main effects alone; e.g., framing effects depend on contribution type and visibility; game length only matters with communication, etc.
- Efficiency in the control games (no-punishment) is a key feature for prediction—it gives a baseline for likely group cooperation absent punishment.
- Do **not** over-rely on mechanical details of the punishment system—contextual and social parameters are far more important for success.
- High heterogeneity means out-of-sample predictive models trained on breadth of conditions are far superior to intuition-based human averaging, even from field experts.

                ---
```
