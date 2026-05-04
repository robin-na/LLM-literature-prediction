# Analysis Report

## Source
Title: Integrative experiments identify how punishment affects welfare in public goods games
Authors: Alsobay, M., Rand, D. G., Watts, D. J., & Almaatouq, A.
Journal: Science
Year: 2026

## Study Type
empirical; empirical subtype=experimental; experimental subtype=lab_experiment

## Task Relevance
PGG or variant=exact; punishment or sanctions=exact; efficiency or payoff outcome=exact

## Outcomes Measured
Primary outcome type: efficiency_or_payoff
Payoff-related outcomes:
- normalized efficiency
- efficiency (group earnings relative to full cooperation)
- group earnings
Non-payoff outcomes:
- contribution rate
- punishment frequency
- reward frequency
Outcome notes:
The primary dependent variable is efficiency (group earnings relative to full cooperation), with normalized efficiency used for cross-condition comparability. Contribution rates and punishment/reward behaviors are also reported but are not the main focus.

## Main Findings Relevant To Prediction
Punishment's effect on group efficiency in PGGs is not uniform: it can either increase or decrease welfare depending on the specific combination of game design parameters. Communication is the single most important moderator, consistently making punishment more effective at improving efficiency. Contribution framing (opt-in vs opt-out), contribution type (variable vs all-or-nothing), game length, and peer outcome visibility also play major roles, often interacting in complex ways. The availability of rewards and higher MPCRs also enhance punishment's positive effect, though to a lesser extent. Punishment cost and punishment technology (effectiveness per unit cost) are surprisingly less important predictors. Predictive models trained on these dimensions and control efficiency outperform human experts and laypeople in forecasting the effect of punishment on efficiency.

## Prediction Guidance
This paper provides direct, high-quality evidence for predicting the effect of enabling punishment on efficiency in PGG-like environments, conditional on game design dimensions and control efficiency. The findings show that the effect of punishment is highly context-dependent and can be reliably predicted using the 14 design parameters plus control efficiency. Communication, contribution framing, contribution type, game length, and outcome visibility are especially critical to consider. The paper's models and empirical results should be used as a primary reference for forecasting efficiency outcomes when punishment is introduced in new PGG designs.

## Design Dimensions Highlighted In This Paper
- player count: The paper directly informs this dimension. It suggests punishment is `mixed` under this dimension. Group size (player count) was systematically varied from 2 to 20 players as one of the 14 design parameters. Its effect on punishment effectiveness is not highlighted as especially strong or consistent, but it is included in all predictive models.
- number of rounds: The paper directly informs this dimension. It suggests punishment is `mixed` under this dimension. Game length (number of rounds) was systematically varied from 1 to 30. Its effect on punishment effectiveness is important but contingent: longer games enhance punishment effectiveness only when communication is available, and this effect is weaker when peer outcomes are visible.
- chat: The paper directly informs this dimension. It suggests punishment is `more_positive` under this dimension. Communication (chat) was systematically manipulated (enabled/disabled). It is the single most important moderator, with communication consistently making punishment more effective at improving efficiency.
- all-or-nothing contribution: The paper directly informs this dimension. It suggests punishment is `mixed` under this dimension. Contribution type (variable vs all-or-nothing) was systematically manipulated. Its effect on punishment effectiveness is important and interacts with contribution framing and outcome visibility.
- default contribution framing: The paper directly informs this dimension. It suggests punishment is `mixed` under this dimension. Contribution framing (opt-in vs opt-out) was systematically manipulated. It is the second most important predictor, with its effect contingent on contribution type and outcome visibility.
- mpcr: The paper directly informs this dimension. It suggests punishment is `more_positive` under this dimension. MPCR (marginal per capita return) was systematically varied from 0.06 to 0.7. Higher MPCRs consistently enhance punishment's positive effect on efficiency, though the effect is smaller than other features.
- punishment cost: The paper directly informs this dimension. It suggests punishment is `mixed` under this dimension. Punishment cost (peer incentive cost) was systematically varied (1 to 4 coins per unit). Its effect on efficiency is present but found to be less important than other parameters.
- punishment technology: The paper directly informs this dimension. It suggests punishment is `mixed` under this dimension. Punishment technology (impact per unit cost) was systematically varied (1 to 4 coins deducted per coin spent). Surprisingly, it had the smallest effect on predictive performance among all features.
- reward availability: The paper directly informs this dimension. It suggests punishment is `more_positive` under this dimension. Reward mechanism availability was systematically manipulated (enabled/disabled). The presence of rewards consistently enhances punishment's positive effect on efficiency.
- reward cost: The paper directly informs this dimension. It suggests punishment is `mixed` under this dimension. Reward cost (peer incentive cost for reward) was systematically varied (1 to 4 coins per unit). Its effect is not highlighted as especially strong or consistent.
- reward technology: The paper directly informs this dimension. It suggests punishment is `mixed` under this dimension. Reward technology (impact per unit cost) was systematically varied (0.5 to 1.5 coins per coin spent). Its effect is not highlighted as especially strong or consistent.
- knowing when the game ends: The paper directly informs this dimension. It suggests punishment is `mixed` under this dimension. Horizon knowledge (whether players know the total number of rounds) was systematically manipulated. Its effect is not highlighted as especially strong or consistent.
- seeing peer outcomes: The paper directly informs this dimension. It suggests punishment is `mixed` under this dimension. Peer outcome visibility (showing summaries of others' earnings and punishments/rewards) was systematically manipulated. Its effect is important and interacts with other features, such as contribution framing and game length.
- seeing punisher identity: The paper directly informs this dimension. It suggests punishment is `mixed` under this dimension. Actor anonymity (whether the identity of punishers/rewarders is revealed) was systematically manipulated. Its effect is not highlighted as especially strong or consistent.

## Important Limitations
- PGGs are stylized laboratory games; external validity to real-world cooperation problems is limited.
- The study isolates variation in game parameters within a relatively homogeneous participant population; effects may differ across populations.
- The design space, while broad, is not exhaustive; other potentially relevant parameters or real-world complexities are not captured.
- Some parameter combinations were sampled only once (in wave 1), limiting precision for those conditions.
- Interpretability of complex model interactions is limited; some findings may be specific to the modeling approach used.
