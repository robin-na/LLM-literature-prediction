# Paper Set Evidence Digest

Number of papers in this paper set: 4

Each item below is a compact paper-level analysis digest. Use only this digest.

- source: Okada, I. (2020). A Review of Theoretical Studies on Indirect Reciprocity. *Games*.
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=close | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr, punishment_cost, punishment_tech
  findings: The paper synthesizes theoretical advances in indirect reciprocity, showing that cooperation can be maintained in social dilemma settings when reputation mechanisms and justified punishment are present. It details how the refinement of assessment functions (e.g., leading eight norms) resolves issues like the scoring and punishment dilemmas, enabling stable cooperation under certain conditions. However, it notes that these models are not directly applicable to public goods games, as selective cooperation (the core of indirect reciprocity) is not possible in standard PGGs. The review also highlights the importance of the benefit-cost ratio, error rates, and the distinction between public and private reputation systems in determining the stability of cooperation. While punishment and reward mechanisms are discussed, the focus is on their role in norm stability and cooperation, not on efficiency or group payoff.
  prediction_guidance: This paper provides theoretical context for how punishment and reputation mechanisms can stabilize cooperation in social dilemmas, but it does not offer direct evidence for predicting efficiency outcomes in public goods games with or without punishment. Its models are adjacent to PGGs but differ in key structural ways (e.g., selective cooperation vs. public goods provision). The review is useful for understanding the mechanisms by which punishment and norm refinement can support cooperation, but it does not provide quantitative or comparative data on efficiency or group payoff. For the downstream prediction task, this paper suggests that the effectiveness of punishment depends on norm structure, reputation information, and error rates, but it does not allow for direct mapping from game design dimensions to efficiency outcomes in PGGs.

- source: KRAINES, D., & KRAINES, V. (1993). LEARNING TO COOPERATE WITH PAVLOV - AN ADAPTIVE STRATEGY FOR THE ITERATED PRISONERS-DILEMMA WITH NOISE. *Theory and Decision*.
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=adjacent | payoff=exact
  outcomes: primary=efficiency_or_payoff | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr
  findings: The paper finds that Pavlovian strategies, which adapt their probability of cooperation based on positive and negative payoffs (interpreted as rewards and punishments), can achieve high average payoffs and are robust to noise in the iterated Prisoner's Dilemma. Pavlov can exploit overly cooperative opponents (like All-C), is not easily exploited except by always-defect strategies, and can recover mutual cooperation after errors more quickly than Tit-for-Tat (TFT). The optimal learning rate (parameter n) balances exploitability and speed of learning, with n=3 or 4 performing best in simulations. The paper provides detailed payoff tables and Markov chain analyses for various strategy matchups, but does not study group interactions, explicit peer punishment, or public goods games.
  prediction_guidance: This paper does not provide direct evidence for predicting the effect of enabling punishment in public goods games, as it does not study group games, peer punishment, or any of the relevant game design dimensions. However, it is informative about how strategies that adapt to positive and negative payoffs (interpreted as endogenous rewards and punishments) can lead to high efficiency and mutual cooperation in repeated dyadic dilemmas. The findings suggest that adaptive learning can be robust to noise and can outperform simple reciprocity (TFT) in some environments. For the downstream prediction task, this paper is only indirectly relevant, as it does not address the effect of enabling punishment mechanisms or any of the design dimensions in public goods games.

- source: Manesi, Z., Van Lange, P. A. M., & Pollet, T. V. (2016). Eyes Wide Open: Only Eyes That Pay Attention Promote Prosocial Behavior. *Evolutionary Psychology*.
  type: empirical | empirical=experimental | experimental=lab_experiment
  relevance: pgg=adjacent | punishment=weak | payoff=weak
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, chat, all_or_nothing, show_n_rounds
  findings: The paper finds that images of eyes with direct gaze (watching eyes) increase prosocial behavior in a helping task, compared to averted eyes, closed eyes, or control images. The effect is observed in the likelihood of completing the task for another participant and in the amount of work left for the partner. The effect is attributed to increased reputational concern when being 'watched.' However, the task is not a public goods game, does not involve group interaction, punishment, or explicit payoff structures, and does not report efficiency or group payoff outcomes.
  prediction_guidance: This paper does not provide direct evidence for predicting the effect of punishment on efficiency in public goods games or similar environments. The design is adjacent to dictator games and mixed-motive helping tasks, not PGGs. There is no punishment, sanctioning, or payoff-based outcome. The findings may be weakly informative for understanding how cues of observation or reputation can increase prosocial behavior, but they do not inform the quantitative prediction of efficiency changes due to punishment in PGG-like games. The paper is not directly useful for the downstream prediction task as specified.

- source: Bourrat, P., Baumard, N., & McKay, R. (2011). Surveillance Cues Enhance Moral Condemnation. *Evolutionary Psychology*.
  type: empirical | empirical=experimental | experimental=lab_experiment
  relevance: pgg=none | punishment=adjacent | payoff=none
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: none
  findings: Participants exposed to images of eyes (vs. flowers) rated moral violations as less acceptable, indicating greater condemnation. The effect is interpreted as evidence that subtle cues of being watched activate reputation-maintenance mechanisms, leading to stronger public endorsement of moral norms. However, the study does not involve economic games, punishment choices, or any payoff-based outcomes.
  prediction_guidance: This paper does not provide evidence relevant to predicting the effect of punishment on efficiency in public goods games or similar environments. It does not manipulate or measure any of the game design dimensions of interest (e.g., player count, MPCR, punishment cost), nor does it report on efficiency or payoff outcomes. Its findings are only adjacent to the prediction task, as they concern the effect of surveillance cues on moral condemnation, not on actual cooperative or punitive behavior or group outcomes.

