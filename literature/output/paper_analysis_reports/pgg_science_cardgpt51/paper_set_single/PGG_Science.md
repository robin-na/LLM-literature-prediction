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
- normalized efficiency (group earnings scaled between full defection and full cooperation benchmarks)
- conventional efficiency (group total earnings divided by earnings under full cooperation)
- group total earnings (implied via efficiency definitions)
Non-payoff outcomes:
- individual contribution decisions (percentage of endowment contributed)
- punishment decisions (number of punishments assigned)
- reward decisions (number of rewards assigned)
Outcome notes:
The central dependent variable for the main heterogeneity analysis is normalized efficiency, a payoff-based welfare measure. Conventional efficiency is used for the prediction task and human forecasting comparison. Contributions and punishment/reward actions are analyzed as behavioral mechanisms but are not the primary welfare outcome.

## Main Findings Relevant To Prediction
The study runs 360 distinct public goods game configurations (7100 participants, 147,618 decisions) defined by a 14-dimensional design space: group size, game length, contribution type (variable vs all-or-nothing), contribution framing (opt in vs opt out), MPCR, communication, peer outcome visibility, actor anonymity, horizon knowledge, punishment availability, peer incentive cost, punishment technology, reward availability, and reward technology. Each configuration is implemented as a pair of games: a control without punishment and a treatment with punishment, holding all other parameters fixed.

Punishment reliably increases contributions (e.g., from 73% to 80% of endowment in wave 1; 74% to 82% in wave 2), but its effect on welfare, measured as normalized efficiency (group earnings scaled between full defection and full cooperation), is heterogeneous. On average, punishment reduces normalized efficiency from 0.71 to 0.63 (11% decrease) in the learning experiments and from 0.72 to 0.68 (6% decrease, marginally significant) in the validation experiments. However, across conditions, punishment’s effect on normalized efficiency ranges from about −44% to +43% in wave 1 (clustered estimates) and from −44% to +29% in wave 2, indicating substantial context dependence.

Using the learning data, the authors train several models to predict treatment (punishment-enabled) efficiency from the 14 design parameters and the observed control efficiency. An elastic net model with interactions performs best, achieving out-of-sample R^2 ≈ 0.53 and RMSE ≈ 4.52 on the validation conditions, accounting for about 91% of the explainable variance given sampling noise. Human forecasters (53 experts and 500 laypeople) perform near the baseline of always predicting the mean treatment efficiency (R^2 ≈ 0.02–0.05), and no individual human outperforms the model.

Feature importance analyses (permutation importance and SHAP values) show that communication is the single most important and consistently positive moderator of punishment’s welfare effect: shuffling the communication feature increases prediction error by about 60%, and enabling communication systematically increases predicted efficiency under punishment. Reward availability and higher MPCR also consistently enhance punishment effectiveness, though MPCR’s effect is small in predictive terms.

Other parameters have important but interaction-dependent effects. Opt-out contribution framing (endowment initially in the public fund) improves punishment effectiveness when contributions are variable but harms it when contributions are all-or-nothing; peer outcome visibility amplifies the negative effect in all-or-nothing settings and attenuates the positive effect in variable settings. Game length improves punishment effectiveness only when communication is available, and this positive interaction is weaker when peer outcomes are visible. Peer outcome visibility itself tends to reduce punishment effectiveness in many contexts. Surprisingly, punishment technology (impact per coin spent) and peer incentive cost have relatively low predictive importance compared to these contextual and framing variables.

Overall, the paper demonstrates that punishment’s welfare impact is not uniformly positive or negative but depends systematically on game design features, especially communication, framing, contribution discreteness, game length, and information visibility.

## Prediction Guidance
This paper is directly aligned with the downstream prediction task: it uses the same structure—predicting treatment (punishment-enabled) efficiency from game design parameters and observed control efficiency—and evaluates multiple models out-of-sample. Its main value is to identify which design dimensions most strongly moderate punishment’s welfare effect and how.

Key implications for prediction:
- Communication (chat) is the dominant moderator: when chat is enabled, punishment is much more likely to increase efficiency; when disabled, punishment often reduces efficiency. Any predictive model should assign substantial weight to the chat dimension.
- Contribution framing (default_contrib) and contribution type (all_or_nothing) interact strongly. Opt-out framing (default in public fund) tends to make punishment more beneficial when contributions are continuous/variable, but more harmful when contributions are all-or-nothing, especially when peer outcomes are visible. Predictive models should include interaction terms between default_contrib, all_or_nothing, and show_other_summaries.
- Game length (num_rounds) improves punishment’s effect on efficiency primarily when communication is available; without communication, longer games do not reliably help and can even exacerbate inefficiencies. Thus, num_rounds should be modeled with an interaction with chat and possibly show_other_summaries.
- Peer outcome visibility (show_other_summaries) often dampens the positive effects of communication and opt-out framing on punishment effectiveness and can make punishment less welfare-improving, likely via discouraging enforcement or encouraging retaliation. Predictive models should treat visibility as a potentially negative moderator.
- Reward mechanisms (reward_exists) consistently enhance punishment’s welfare effect, so conditions with both punishment and reward should be predicted to have higher treatment efficiency than punishment-only conditions, holding other factors and control efficiency constant.
- MPCR has a small but consistent positive effect: higher MPCR (weaker social dilemma) makes punishment more likely to improve efficiency.
- Punishment technology and cost (punishment_tech, punishment_cost/peer incentive cost) are less predictive than expected; models should include them but not rely on them as primary drivers of welfare effects.

Because the authors’ best-performing model already uses the same feature set (14 design parameters plus control efficiency) and achieves high out-of-sample R^2, their qualitative findings about which dimensions matter and how they interact provide strong guidance for structuring and regularizing new predictive models in similar PGG-like environments.

## Design Dimensions Highlighted In This Paper
- player count: The paper provides contextual guidance on this dimension. It suggests punishment is `unclear` under this dimension. Group size (2–20 players) is one of the 14 manipulated design parameters, but the paper does not report a clear, consistent effect of group size on punishment’s impact on efficiency. It is included as a feature in the predictive models, but not highlighted as an important or consistent moderator.
- number of rounds: The paper gives an indirect but usable signal on this dimension. It suggests punishment is `more_positive` under this dimension. Game length (1–30 rounds) is manipulated and analyzed. Longer games enhance punishment effectiveness (higher efficiency under punishment) only when communication is available; without communication, longer games do not consistently help. Thus, the direction is conditionally more positive, based on interactions rather than a main effect.
- chat: The paper directly informs this dimension. It suggests punishment is `more_positive` under this dimension. Communication (chat) is a binary design parameter (enabled/disabled). It is the most important predictor of punishment effectiveness: enabling communication consistently increases efficiency in punishment-enabled games and strongly improves model predictions. It also interacts with game length and outcome visibility.
- all-or-nothing contribution: The paper directly informs this dimension. It suggests punishment is `mixed` under this dimension. Contribution type (variable vs all-or-nothing) is manipulated. Its effect on punishment’s welfare impact is strongly interaction-dependent: with opt-out framing, punishment is more effective when contributions are variable but less effective when contributions are all-or-nothing; peer outcome visibility further modulates this. Thus, the direction is mixed and contingent.
- default contribution framing: The paper directly informs this dimension. It suggests punishment is `mixed` under this dimension. Contribution framing (opt in vs opt out) is manipulated. Opt-out framing enhances punishment effectiveness when contributions are variable but reduces it when contributions are all-or-nothing, with peer outcome visibility amplifying or attenuating these effects. Therefore, its effect direction is mixed and highly interaction-dependent.
- mpcr: The paper gives an indirect but usable signal on this dimension. It suggests punishment is `more_positive` under this dimension. MPCR (0.06–0.7) is manipulated and included in the predictive model. The paper reports that higher MPCR, which weakens the social dilemma, enhances punishment effectiveness (more positive effect on efficiency), though its contribution to prediction accuracy is small compared to other features.
- punishment cost: The paper provides contextual guidance on this dimension. It suggests punishment is `unclear` under this dimension. Peer incentive cost (1–4 coins per unit of punishment or reward) is manipulated. The paper does not separately analyze punishment cost’s effect on welfare; it is folded into a general statement that punishment parameters matter less than expected. No clear direction is reported for how higher or lower cost changes punishment’s efficiency impact.
- punishment technology: The paper gives an indirect but usable signal on this dimension. It suggests punishment is `unclear` under this dimension. Punishment technology (1–4 coins deducted per coin spent) is manipulated. Feature importance analysis shows it has the smallest effect on predictive performance among all features, and the paper emphasizes that punishment technology is less important than expected. The direction of its effect on efficiency is not clearly specified; the main result is its low predictive importance.
- reward availability: The paper directly informs this dimension. It suggests punishment is `more_positive` under this dimension. Reward availability (enabled/disabled) is manipulated. The paper reports that the availability of reward mechanisms consistently enhances punishment’s effectiveness on efficiency and is important for prediction accuracy (4.6% increase in error when shuffled).
- reward cost: The paper provides contextual guidance on this dimension. It suggests punishment is `unclear` under this dimension. Peer incentive cost applies to both punishment and reward (1–4 coins per unit). The paper does not isolate the effect of reward cost on welfare or punishment effectiveness; it is only described as part of the general incentive structure.
- reward technology: The paper mentions this dimension but gives limited predictive guidance. It suggests punishment is `unclear` under this dimension. Reward technology (0.5–1.5 coins granted per coin spent) is defined and manipulated but explicitly excluded from the main E-Net feature importance analysis because it is only meaningful when rewards are enabled. The paper does not report a direct effect of reward technology on punishment’s welfare impact.
- knowing when the game ends: The paper provides contextual guidance on this dimension. It suggests punishment is `unclear` under this dimension. Horizon knowledge (known vs unknown total number of rounds) is manipulated and included as a design parameter, but the paper does not report specific results on how it moderates punishment’s effect on efficiency.
- seeing peer outcomes: The paper directly informs this dimension. It suggests punishment is `less_positive` under this dimension. Peer outcome visibility (visible vs hidden summaries of others’ earnings and punishments/rewards) is manipulated. Visibility tends to reduce punishment effectiveness: it amplifies the negative effect of opt-out framing with all-or-nothing contributions, attenuates the positive effect with variable contributions, and weakens the positive interaction between game length and communication. The paper suggests mechanisms like discouraging enforcement or enabling retaliation.
- seeing punisher identity: The paper provides contextual guidance on this dimension. It suggests punishment is `unclear` under this dimension. Actor anonymity (whether identities of punishers/rewarders are revealed) is manipulated. The paper notes that visibility of who punishes could affect retaliation and enforcement, but does not provide a clear, quantified effect of this parameter on punishment’s welfare impact.

## Important Limitations
- The experiments use stylized public goods games with specific parameter ranges and online participant pools (MTurk and Prolific), which limits external validity to other cooperation games and real-world settings.
- The study focuses on variation in game parameters within relatively homogeneous populations; interactions between population characteristics and game design are not explored but may be important.
- Some design parameters (e.g., group size, horizon knowledge, punishment cost, reward technology) are included in the models but receive little direct substantive analysis, so their causal roles remain unclear.
- Normalized efficiency and conventional efficiency are model-based welfare measures that assume specific benchmarks (full cooperation and full defection) and ignore potential utility heterogeneity across participants.
- Although the best-performing model explains most of the explainable variance given sampling noise, model multiplicity and potential overfitting to the learning data mean that alternative models could assign different importance to some parameters, especially punishment technology and costs.
