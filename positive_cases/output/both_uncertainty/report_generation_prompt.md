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
        - Report style: uncertainty
        - Follow these additional style requirements exactly:
        - For every major predictive claim, include an explicit confidence label such as high, medium, or low.
- Distinguish stable effects from interaction-heavy or weakly supported effects.
- Include a section titled "High-Confidence Rules" and another titled "Low-Confidence / Unstable Regions".
- Preserve actionable guidance, but make uncertainty visible everywhere it matters.

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
                Let's proceed with the analysis step by step as requested.

## 1. Data Overview

First, I'll load the data, inspect key columns, and report basic structure and sample sizes relevant to the analysis. Then, I'll proceed to each of your analytic requests.

Let's get started by loading and previewing the data, then proceed to the analysis.

                ---

Paper memo:
                ---
                # Memo: Summary of PGG Manuscript for Efficiency Prediction Task

## 1) Design & Data

- The study used an “integrative” experiment structure: 14 design parameters were systematically and simultaneously varied across 360 unique experimental conditions (147,618 total decisions, 7,100 participants).
- Each experimental condition was a point in the 14-dimensional design space and defined a single PGG scenario. Each scenario was run as a pair of games: punishment disabled (“control”) and punishment enabled (“treatment”)—all other parameters matched.
- Data collection had two phases:
    - Wave 1 (learning): 320 conditions sampled via Sobol sequence (max coverage, 1 realization each).
    - Wave 2 (validation): 40 new conditions, each with 8-12 replicates (for higher precision), for out-of-sample prediction testing.
- All protocols, recruitment, and user interfaces were standardized to minimize hidden moderators.
- Each CONFIG parameter (see below) was systematically manipulated (see Table 1 for parameter list).

## 2) Efficiency Definition

- **Efficiency** is defined as the ratio of the group’s total net earnings to the total earnings under full cooperation (all contribute maximally every round):  
   Efficiency = (group’s net payoff) / (group’s payoff if all cooperate fully).
- Efficiency = 1: full cooperation; lower values mean less cooperation and/or welfare lost to inefficiency or costly punishment.
- In some analyses “normalized efficiency” is used, scaling observed earnings relative to the minimum (full defection) and maximum (full cooperation, no rewards) possible in each setting, enabling fairer comparison across parameter space.

## 3) Main Findings on Punishment

- On average, punishment **increased contributions** but did **not reliably increase efficiency** due to incurred punishment costs; in fact, welfare often decreased.
- Direction of punishment’s effect on efficiency was highly variable—ranging from +43% to -44% across experimental conditions.
    - In some setups, punishment dramatically reduced efficiency (e.g., 0.78 to 0.44); in others, it increased efficiency substantially (e.g., 0.56 to 0.80).
- Models (especially E-Net/Elastic Net) using the full CONFIG and observed control-game efficiency as inputs **outperformed human experts and laypeople** in prediction accuracy, with best model R² = 0.53 on out-of-sample tasks.
    - Human "wisdom of the crowd" and individual experts performed little better than guessing the grand mean efficiency under punishment.

## 4) Heterogeneity / Moderators

- Substantial, statistically robust heterogeneity in the effect of punishment on efficiency across conditions—attributed specifically to the varied CONFIG parameters (not random noise or external moderators).
- **Key moderators/predictors**:
    - **Communication:** By far the most important predictor; enabling communication increased the net effectiveness of punishment more than any other feature.
    - **Contribution Framing (opt-in vs. opt-out):** The effect of the default contribution condition interacts with other parameters, especially contribution type and peer outcome visibility.
    - **Game Length:** Only enhances punishment’s effectiveness if communication is available; effect is damped if other players' outcomes are visible.
    - **Reward Availability:** Consistently amplifies positive impact of punishment.
    - **Marginal Per Capita Return (MPCR):** Higher MPCR raises efficiency, but impact is generally smaller.
    - **Complex interactions** (e.g., opt-out increases effectiveness with variable contributions but can harm it in all-or-nothing settings; effects of outcome visibility and communication are similarly non-additive).
- **Punishment “technology”** (cost-magnitude ratio) is much less influential than context/interactional parameters.

## 5) Notes for Prediction

- **Best practice for prediction**: Use all 14 CONFIG parameters plus the control-game efficiency as features for modeling, as the context-rich approach captures interaction effects and heterogeneity.
- Control (no-punishment) efficiency is an *extremely useful summary feature*: it helps anchor predictions by summarizing baseline group behavior given the CONFIG.
- Consider key interaction effects in modeling; effects of some parameters depend critically on the values of others (e.g., communication × game length; contribution framing × contribution type × outcome visibility).
- Models trained on this structure generalize well to new CONFIGs, but the actual effect of punishment on efficiency can vary directionally and in magnitude—highlighting the need for highly contextual, parameter-based prediction rather than simple heuristics or rules-of-thumb.
- Caution: While the models work across the studied range, extrapolation beyond the sampled/design parameter space or to different populations may diminish accuracy.

---

**CONFIG parameter list (for each instance):** group size, game length, contribution type (variable/all-or-nothing), contribution framing (opt-in/opt-out), MPCR, communication, peer outcome visibility, actor anonymity, horizon knowledge, punishment enabled, peer incentive cost, punishment technology, reward enabled, reward technology.

                ---
```
