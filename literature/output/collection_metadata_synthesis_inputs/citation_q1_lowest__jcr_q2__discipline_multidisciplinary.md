# Paper Set Evidence Digest

Number of papers in this paper set: 3

Each item below is a compact paper-level analysis digest. Use only this digest.

- source: Liao, Y. L., Zhang, L., Lei, S. Y., Song, M. Z., Deng, W. K., & Hu, D. F. (2021). RETRACTED: Third-Party Punishment Mechanism and Corporate Cooperation in Environmental Investment: Experiments on Public Goods Game (Retracted Article). *Discrete Dynamics in Nature and Society*.
  type: empirical | empirical=experimental | experimental=lab_experiment
  relevance: pgg=close | punishment=exact | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=more_positive
  dimensions: player_count, num_rounds, chat, all_or_nothing, mpcr, punishment_cost
  findings: This paper experimentally compares a threshold public goods game with and without third-party punishment (TPP), using groups of three participants (framed as enterprises) making resource investment decisions toward a group threshold. The TPP mechanism automatically punishes group members whose investment rate is below the group mean. The presence of TPP leads to higher mean resource investment amounts, higher individual and group investment rates, and a substantially higher success rate of cooperation (from 55.57% to 76.85%). Regression analysis confirms that TPP has a significant positive effect on investment behavior, even after controlling for individual characteristics and measured preferences for interaction and equity (IEP).
  prediction_guidance: This paper provides strong evidence that introducing a third-party punishment mechanism in a threshold public goods game increases group investment and the probability of achieving the public good. For prediction tasks, the presence of TPP (punishment enabled) should be expected to yield higher efficiency or group payoff than the control (punishment disabled), especially in small groups (n=3) with a threshold structure and automatic, impersonal punishment. The results are most directly applicable to threshold PGGs with automatic third-party punishment and no communication. The findings support a more positive effect of punishment on efficiency-related outcomes under these design conditions.

- source: Szilagyi, M. N., & Somogyi, I. (2010). Agent-Based Simulation of an N-Person Game with Parabolic Payoff Functions. *Complexity*.
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing
  findings: The study finds that the final proportion of cooperators depends strongly on the shape and relative position of the parabolic payoff functions, the agent update rule, and the definition of neighborhood (local vs. global). For some parameterizations, stable intermediate levels of cooperation emerge; in others, the system converges to all-cooperation or all-defection. The results are often unpredictable except in special cases (e.g., greedy or conformist agents with global neighborhoods). The paper does not report efficiency, group payoff, or welfare outcomes, nor does it include explicit punishment or reward mechanisms as in standard public goods games.
  prediction_guidance: This paper does not provide direct evidence for predicting the effect of enabling punishment on efficiency in public-goods-game-like environments. The game studied is adjacent to PGGs in that it is an N-person game with binary choices and payoff externalities, but it lacks explicit punishment/reward actions and does not report efficiency or group payoff. The findings may be useful for understanding how nonlinear payoff structures and local interactions affect cooperation rates, but they do not inform the prediction of efficiency changes due to punishment interventions.

- source: Johnson, T. (2023). Seeding the Spatial Prisoner's Dilemma with Ulam's Spiral. *Complexity*.
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=none | payoff=none
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing
  findings: The study finds that when cooperators are initially placed at the prime-numbered locations of Ulam's spiral on a spatial grid, they can grow to dominate the population under certain parameter conditions (specifically, when the temptation to defect b ≤ 1.33 and grid size n ≥ 23). The growth of cooperation is due to the formation of cooperative clusters in specific spatial configurations. The paper does not analyze or report on efficiency, group payoff, or any payoff-based outcomes, nor does it include any punishment or sanctioning mechanisms.
  prediction_guidance: This paper does not provide evidence relevant to predicting the effect of punishment on efficiency in public-goods-game-like environments. It does not include punishment, sanctions, or payoff-based outcomes, and the game is a spatial prisoner's dilemma rather than a public goods game. The findings are limited to the evolution of cooperation based on initial spatial seeding and do not inform the downstream prediction task regarding punishment or efficiency.

