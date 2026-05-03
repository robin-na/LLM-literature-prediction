# Paper Set Evidence Digest

Number of papers in this paper set: 3

Each item below is a compact paper-level analysis digest. Use only this digest.

- source: Wang, S. X., Chen, X. J., Xiao, Z. L., Szolnoki, A., & Vasconcelos, V. V. (2023). Optimization of institutional incentives for cooperation in structured populations. *Journal of the Royal Society Interface*.
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=close
  outcomes: primary=efficiency_or_payoff | overall_effect=more_positive
  dimensions: player_count, all_or_nothing, punishment_cost, punishment_tech, reward_exists, reward_cost
  findings: The paper finds that both institutional punishment and reward can be tuned to achieve near-full cooperation in structured populations, with the optimal protocol being time-invariant and identical for both types of incentives under a given update rule. The minimal cumulative cost to the institution depends on the initial fraction of cooperators: punishment is more cost-effective when initial cooperation is high, while reward is more cost-effective when initial cooperation is low. The results are supported by analytical derivations and simulations across regular, random, small-world, and scale-free networks. The main outcome is the cumulative cost to the institution, which is a proxy for efficiency from the perspective of implementing cooperation-promoting interventions.
  prediction_guidance: This paper provides strong theoretical guidance on how the cost-effectiveness of punishment (and reward) depends on game parameters such as network structure, update rule, and initial cooperation level. While it does not report group efficiency in the standard sense, its focus on the cumulative cost to achieve high cooperation is closely related and can inform predictions about the efficiency impact of enabling punishment in similar structured games. The results suggest that, with optimally tuned punishment, high cooperation (and thus high group efficiency) can be achieved at lower institutional cost when initial cooperation is already substantial. The findings are most directly applicable to structured Prisoner's Dilemma settings with institutional (not peer) punishment or reward, and may be less directly transferable to standard public goods games.

- source: Gou, Z. Q., & Li, Y. (2023). Prisoner's dilemma game model Based on historical strategy information. *Scientific Reports*.
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing
  findings: The study finds that increasing the length of historical memory (M) and the weight of memory information (β) in a spatial prisoner's dilemma model leads to higher cooperation rates and more stable cooperative clusters. The effect saturates at high memory lengths, and excessive memory does not further promote cooperation. The model does not include explicit punishment or reward mechanisms, and all outcomes are reported in terms of cooperation rate and strategy stability, not efficiency or group payoff.
  prediction_guidance: This paper does not provide direct evidence for predicting the effect of punishment on efficiency in public goods games or their close variants. It models a spatial prisoner's dilemma with memory-based strategy updating, focusing on how memory and its weight affect cooperation rates. There is no manipulation or analysis of punishment, reward, or efficiency outcomes. Thus, its relevance to the downstream prediction task is limited to providing indirect, adjacent evidence that memory and historical information can promote cooperation, but it does not inform the effect of punishment on efficiency.

- source: Andrighetto, G., & Vriens, E. (2022). A research agenda for the study of social norm change. *Philosophical Transactions of the Royal Society A-mathematical Physical and Engineering Sciences*.
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: none
  findings: The paper argues that social norms, especially when enforced by mechanisms like punishment, can facilitate cooperation in collective action problems. It reviews advances in measuring the causal effect of norms, the use of agent-based models to study norm change and tipping points, and the importance of contextual and individual heterogeneity (e.g., tightness-looseness theory). The authors emphasize that while social norms can promote large-scale behavioral change, they can also reinforce undesirable or inefficient behaviors, and that their strength can be both a solution and a barrier to change. The paper calls for future research integrating empirical and computational methods to better predict and intervene in norm change processes.
  prediction_guidance: This paper does not provide direct empirical evidence or quantitative findings that can be used to predict the effect of punishment on efficiency in public goods games or similar environments. However, it offers theoretical and conceptual insights: (1) punishment is discussed as a key enforcement mechanism for social norms that can support cooperation; (2) the effectiveness of punishment and norm enforcement is context-dependent, influenced by factors like group heterogeneity and cultural tightness; (3) strong norms (and by extension, strong punishment) can sometimes lead to inefficiency or undesirable outcomes. For prediction tasks, this paper suggests that the impact of punishment on efficiency is likely to be moderated by norm strength, group context, and the presence of tipping points, but does not provide direct parameter-level evidence.

