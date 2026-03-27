You are writing a prediction-support report to help estimate how enabling punishment changes efficiency in new public goods games.

        Use file search over the attached paper(s).

        Requirements:
        - Base the report strictly on what the paper(s) support.
        - Do not speculate beyond the retrieved evidence.
        - If a requested quantity, moderator, or rule is not clearly supported by the paper(s), say that explicitly.
        - Explain the key variables and how they map to experimental design.
        - Provide predictive guidance that is useful for forecasting, while remaining faithful to the paper evidence.
        - Output in Markdown with clear section headers.
        - Include numerical estimates and tables only when they are directly supported by the paper evidence.
        - Follow these additional style requirements exactly:
        - Keep the report narrative-driven and readable, with prose as the default form.
- Use tables only when they clarify the paper evidence.

        Prediction task context:
- Each prediction instance provides values for 14 CONFIG parameters plus the average efficiency of the control game (punishment disabled).
- The goal is to predict the average efficiency of the same game when punishment is enabled.
- Efficiency is the ratio of the group’s total payoff to the total payoff of a fully cooperative group (everyone contributes fully every round).
- Thus, efficiency = 1 means full cooperation; lower values indicate less cooperation.

        Include these sections:
        1) Title
        2) Abstract
        3) Background & Definitions (explicitly restate the prediction task: given CONFIGs plus control efficiency, predict treatment efficiency)
        4) Data & Variables (explicitly define the 14 CONFIG parameters used in prediction, plus CONFIG_punishmentExists because it distinguishes control from treatment)
        5) Empirical Patterns (punishment effects and heterogeneity)
        6) Predictive Guidance
        7) Limitations & Missing Evidence
        8) How To Use This For Predictions (concise bullet list)

        Column definitions:
        - CONFIG_playerCount: Number of players in the game.
- CONFIG_numRounds: Number of rounds in the game.
- CONFIG_MPCR: Marginal per-capita return = multiplier / playerCount.
- CONFIG_allOrNothing: If true, contributions are all-or-nothing rather than continuous amounts.
- CONFIG_chat: Whether chat is enabled between players.
- CONFIG_defaultContribProp: Contribution framing: 0 = opt-in (default keep; must actively give), 1 = opt-out (default contribute; must actively keep).
- CONFIG_punishmentCost: Cost to the punisher per unit of punishment.
- CONFIG_punishmentMagnitude: Coins deducted from a punished player per unit of punishment.
- CONFIG_showOtherSummaries: Whether peer outcomes are shown each round.
- CONFIG_showNRounds: Whether the total number of rounds is shown to players.
- CONFIG_showPunishmentId: Whether the identity of punishers or rewarders is shown.
- CONFIG_rewardExists: Whether rewards are enabled in the game.
- CONFIG_rewardCost: Cost to the rewarder per unit of reward.
- CONFIG_rewardMagnitude: Coins added to a rewarded player per unit of reward.
- CONFIG_punishmentExists: Whether punishment is enabled in the game.
