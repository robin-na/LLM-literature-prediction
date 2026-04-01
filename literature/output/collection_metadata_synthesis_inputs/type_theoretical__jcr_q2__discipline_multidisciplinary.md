# Paper Set Evidence Digest

Number of papers in this paper set: 6

Each item below is a compact paper-level analysis digest. Use only this digest.

- source: Jaffe, K. (2008). Evolution of Shame as an Adaptation to Social Punishment and its Contribution to Social Cohesiveness. *Complexity*.
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: punishment_cost
  findings: The paper finds that shame can evolve as an adaptation to social punishment, increasing pro-social behavior (generosity) after punishment. When punishment is present (especially if costless to the punisher) or when shame is present, populations maintain higher levels of generosity and a balance between punishers and non-punishers. However, the model does not directly report on group efficiency or total payoff, focusing instead on the evolutionary dynamics of behavioral traits. The results suggest that shame and punishment can stabilize cooperation for long periods, but with fluctuations between cooperative and selfish phases.
  prediction_guidance: This paper provides indirect support for the idea that punishment (and shame) can increase pro-social behavior in resource-sharing environments, which may translate to higher efficiency in public goods games. However, because the model is not a direct PGG and does not report efficiency or group payoff, its value for predicting efficiency outcomes is limited. The main relevance is in showing that punishment and shame can stabilize cooperation, especially when punishment is not costly to the punisher. The findings are more about evolutionary stability and trait frequencies than about efficiency per se.

- source: Zhang, N., Zhang, X. X., Lei, M., & Yang, Y. J. (2020). Multiagent Collaborative Governance for Targeted Poverty Alleviation from the Perspective of Stakeholders. *Complexity*.
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, all_or_nothing, punishment_cost, reward_exists
  findings: The paper finds that: (1) Increasing support from local governments and social organizations to poverty groups can promote the willingness of poverty groups to cooperate, but excessive support from higher-level government does not necessarily lead to more cooperation or better outcomes. (2) Moderate increases in punishment (negative returns) for noncooperation by social organizations and poverty groups can encourage cooperative behavior. (3) Increasing the basic economic benefits for social organizations and poverty groups significantly increases their willingness to cooperate. The model suggests that a combination of incentives and moderate sanctions is more effective than top-down subsidies alone. However, the main outcomes are the equilibrium rates of cooperation, not efficiency or group payoffs.
  prediction_guidance: This paper provides indirect, contextual evidence for the prediction task. It does not report efficiency or group payoff outcomes, but it does analyze how punishment (modeled as negative returns for noncooperation) and other design parameters affect the evolution of cooperation in a multi-agent setting. The findings suggest that moderate punishment can increase cooperation rates, which in standard public goods games is often associated with higher efficiency, but this is not directly demonstrated here. The model is more complex than standard PGGs, involving three types of agents and context-specific payoffs. Thus, the paper is best used for qualitative, indirect support: it reinforces that punishment and incentives can promote cooperation, but does not provide quantitative estimates of efficiency effects for PGG-like environments.

- source: Szilagyi, M. N., & Somogyi, I. (2010). Agent-Based Simulation of an N-Person Game with Parabolic Payoff Functions. *Complexity*.
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing
  findings: The study finds that the final proportion of cooperators depends strongly on the shape and relative position of the parabolic payoff functions, the agent update rule, and the definition of neighborhood (local vs. global). For some parameterizations, stable intermediate levels of cooperation emerge; in others, the system converges to all-cooperation or all-defection. The results are often unpredictable except in special cases (e.g., greedy or conformist agents with global neighborhoods). The paper does not report efficiency, group payoff, or welfare outcomes, nor does it include explicit punishment or reward mechanisms as in standard public goods games.
  prediction_guidance: This paper does not provide direct evidence for predicting the effect of enabling punishment on efficiency in public-goods-game-like environments. The game studied is adjacent to PGGs in that it is an N-person game with binary choices and payoff externalities, but it lacks explicit punishment/reward actions and does not report efficiency or group payoff. The findings may be useful for understanding how nonlinear payoff structures and local interactions affect cooperation rates, but they do not inform the prediction of efficiency changes due to punishment interventions.

- source: Szilagyi, M. N., & Somogyi, I. (2010). A Systematic Analysis of the N-person Chicken Game. *Complexity*.
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=none | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing
  findings: The study finds that in the N-person chicken game, the final proportion of cooperators depends sensitively and sometimes non-monotonically on the payoff function parameters (R and S). For certain parameter ranges, small changes can lead to drastic shifts in cooperation rates. The system stabilizes to a constant or oscillating cooperation rate, but the group efficiency or total payoff is not directly analyzed. No punishment, reward, or sanctioning mechanisms are included in the model.
  prediction_guidance: This paper does not provide direct evidence for predicting the effect of punishment on efficiency in public-goods-game-like environments, as it does not include any punishment or sanctioning mechanism. However, it does provide insight into how the structure of payoff functions (e.g., the relative rewards for cooperation and defection) can lead to abrupt changes in cooperation rates in N-person social dilemmas. For the downstream prediction task, this paper is only indirectly relevant, as it does not address punishment, efficiency, or payoff outcomes in the presence or absence of sanctions.

- source: Toupo, D. F. P., Rand, D. G., & Strogatz, S. H. (2014). Limit Cycles Sparked by Mutation in the Repeated Prisoner's Dilemma. *International Journal of Bifurcation and Chaos*.
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=none | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: num_rounds, all_or_nothing
  findings: The paper finds that introducing mutation into the evolutionary dynamics of the repeated Prisoner's Dilemma (with ALLC, ALLD, and costly TFT) can robustly generate stable limit cycles in the population, resulting in oscillations between cooperation and defection. These cycles occur for a wide range of mutation structures and parameter values, and can be sparked by arbitrarily small mutation rates and complexity costs. The presence of these cycles means that cooperation can persist at substantial levels, even though defection would otherwise dominate. However, the analysis is entirely theoretical and does not include punishment, reward, or explicit efficiency outcomes.
  prediction_guidance: This paper does not provide direct evidence for the effect of punishment on efficiency in public-goods-game-like environments. It is relevant as adjacent theory, showing that mutation and strategy diversity can sustain cooperation in repeated Prisoner's Dilemma settings, but it does not address punishment, sanctions, or payoff-based efficiency. Therefore, it should not be used as direct evidence for predicting efficiency changes due to punishment. Its main value is in highlighting the importance of mutation and strategy diversity for sustaining cooperation, which may be contextually informative for broader models of cooperation.

- source: Johnson, T. (2023). Seeding the Spatial Prisoner's Dilemma with Ulam's Spiral. *Complexity*.
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=none | payoff=none
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing
  findings: The study finds that when cooperators are initially placed at the prime-numbered locations of Ulam's spiral on a spatial grid, they can grow to dominate the population under certain parameter conditions (specifically, when the temptation to defect b ≤ 1.33 and grid size n ≥ 23). The growth of cooperation is due to the formation of cooperative clusters in specific spatial configurations. The paper does not analyze or report on efficiency, group payoff, or any payoff-based outcomes, nor does it include any punishment or sanctioning mechanisms.
  prediction_guidance: This paper does not provide evidence relevant to predicting the effect of punishment on efficiency in public-goods-game-like environments. It does not include punishment, sanctions, or payoff-based outcomes, and the game is a spatial prisoner's dilemma rather than a public goods game. The findings are limited to the evolution of cooperation based on initial spatial seeding and do not inform the downstream prediction task regarding punishment or efficiency.

