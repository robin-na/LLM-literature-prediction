# 1) Evidence Base

This literature set consists of 41 papers, all theoretical, encompassing game-theoretic modeling, evolutionary arguments, agent-based simulations, conceptual reviews, and comparisons to real-world analogues. There are no empirical or experimental laboratory studies, nor meta-analyses of such data. The set is relatively broad: most papers are not restricted to laboratory public goods games (PGGs), but consider related social dilemmas, repeated games, conflict or bargaining situations, or discuss collective action problems more generally. Some focus tightly on punishment mechanisms, while others discuss a broader ecology of control, reward, and communication mechanisms.

Outcomes in this set are mostly theoretical predictions, simulated behavioral equilibria, or qualitative generalizations drawn from existing literature. Efficiency or payoff-based outcomes are discussed in a subset of the papers, but most center behavioral outcomes such as contribution rate, cooperation frequency, or norm compliance. Direct empirical effect sizes or laboratory-validated predictions are mostly absent. The depth of discussion across the 14 design dimensions varies, with some dimensions (e.g., punishment cost, player count, marginal return) receiving more sustained attention.

# 2) Task Relevance

For the prediction task (effect of enabling peer punishment in a PGG-like environment, as a function of design dimensions and control efficiency), this literature set has partial but not complete relevance:

- **pgg_or_variant:**  
  - `exact`: A subset of papers model standard or spatial PGGs, threshold public goods, or repeated n-player social dilemmas (e.g., Baker & Rachlin, 2002; Noailly et al., 2009; Kol'veková et al., 2021).
  - `close`: Many papers focus on related games, such as the iterated Prisoner’s Dilemma, club goods, CPR, or contest models, with structures adjacent to PGGs (e.g., POLLOCK, 1988; Melkonyan et al., 2022; Amegashie & Runkel, 2012).
  - `adjacent/weak`: Several papers discuss behavioral experiments, natural settings, or theoretical constructs not specific to PGGs.
  - `none`: One paper is entirely off-topic.

- **punishment_or_sanctions:**  
  - `exact`: Most papers theorize, model, or discuss punishment (peer-based, centralized, endogenous, or through metanorms).
  - `adjacent`: A small number focus on alternative norm enforcement (e.g., reward-only, commitment, partner switching).
  - `none`: Several have no treatment manipulation.

- **efficiency_or_related_payoff_outcome:**
  - `exact`: A core of papers report efficiency (payoff relative to possible maximum) as their primary outcome (e.g., Kol'veková et al., 2021; Noailly et al., 2009).
  - `close`: Some papers report “group payoff”, “average welfare”, or comparative surplus, but not always as a ratio.
  - `adjacent/weak`: Most discuss non-payoff outcomes (contribution, norm compliance), behavioral dynamics, or neural/psychological motivations, with efficiency only implied.

# 3) Outcomes Measured In The Literature

- **Payoff/Efficiency Outcomes:**  
   A minority of theory/simulation papers directly model or report group efficiency, mean payoff, or welfare as central outcomes (e.g., Kol'veková et al., 2021; POLLOCK, 1988; Noailly et al., 2009). In these, efficiency is typically calculated as total group payoff relative to a cooperative benchmark.

- **Non-Payoff Behavioral Outcomes:**  
   The dominant class of outcomes is behavioral: cooperation or contribution rate, norm adherence, frequency of punishing, fairness of offers, strategy transitions, or agent-level decisions. These are often argued to correlate with efficiency, but the link is not always explicit and may be moderated by punishment cost and other factors.

- **Psychological/Motivational Outcomes:**  
   Some papers discuss the psychological drivers of punishment and cooperation (e.g., loss aversion, status signaling, evolutionary heuristics), or neural correlates, but do not report efficiency or payoff outcomes.

# 4) Main Findings Relevant To Prediction

- **General Effect of Punishment:**
  - Theoretical models and simulations consistently predict that enabling punishment (especially when not excessively costly and when punishment is effective) increases average group efficiency or payoff relative to control (no-punishment) PGGs or variants, as higher contributions are sustained (Baker & Rachlin, 2002; Kol'veková et al., 2021; Noailly et al., 2009; POLLOCK, 1988; Heller & Sieberg, 2008; Nasrallah & Cheaib, 2016).
  - However, the effect is not automatic or uniform: effectiveness depends critically on several design features and context.

- **Moderators and Dimension Dependencies:**
  - **Punishment Cost and Effectiveness:** Lower punisher cost, higher punishment impact, and declining punishment need (as cooperation stabilizes) all facilitate positive efficiency effects (Kol'veková et al., 2021; Heller & Sieberg, 2008).
  - **Group Size (player_count):** Positive effects of punishment on efficiency are more robust in moderate-to-large groups or where there is sufficient population structure. Very small groups or dyads may not see net efficiency gains (Rumble et al., 2022; Kritikos & Bolle, 2004).
  - **Spatial/Population Structure:** The presence of multiple groups, spatial clusters, or local enforcement strongly moderates whether punishment translates into efficiency gains (Noailly et al., 2009; POLLOCK, 1988). In well-mixed or unstructured groups, effectiveness may collapse.
  - **Cycle and Catastrophe Risks:** Non-monotonic, bifurcated, and path-dependent outcomes are highlighted: some parameter ranges (e.g., intermediate monitoring, high retaliation risk) can yield “catastrophes” with sharply reduced compliance and efficiency (Whitmeyer, 2004; Sylwester et al., 2013).
  - **Antisocial Punishment:** In some settings, punishment may be used against cooperators, reducing or reversing gains, especially where costs are low, institutions are weak, or social competition is high (Sylwester et al., 2013).
  - **Institutional and Social Context:** Institutional design (endogenous/collective punishment, transparency, support for punishers) strengthens the efficiency effects (Kol'veková et al., 2021; Brandt & Svendsen, 2019; Frey & Burgess, 2023).
  - **Punishment Timing & Communication:** Immediate punishment, communication, and informed targeting of defectors promote positive efficiency effects, whereas delayed or misdirected punishment can undermine them (Allgaier et al., 2020; Lazarus, 2023).

- **Negative or Weak Effects:**
  - Models of dyadic repeated games highlight that costly punishment can reduce overall efficiency, particularly when retaliation or cycles of escalating punishment occur, or where more socially positive strategies (generosity/forgiveness) are available (Rumble et al., 2022).
  - In environments with strong antisocial punishment, or population structures favoring group dominance, enabling punishment may not raise efficiency or may even lower it (Sylwester et al., 2013; Prietula & Conway, 2009).

# 5) Prediction Guidance

- **General Prediction:**  
  The literature provides robust theoretical support that enabling peer punishment in PGG-like environments generally increases efficiency (relative to a no-punishment control), particularly when design dimensions ensure punishment is effective, not excessively costly, targets defectors (not cooperators), and the population is sufficiently large or structured.

- **Parameter Sensitivity:**  
  Predictions should be conditioned on:
  - **Punishment Cost / Effectiveness:** Lower cost and higher impact are associated with higher efficiency gains, as long as costs do not overwhelm cooperative gains (Kol'veková et al., 2021; Heller & Sieberg, 2008).
  - **Group Structure:** Structured, multi-group, or spatial settings amplify efficiency benefits; in well-mixed, one-group designs, punishment may be less effective or even fail (Noailly et al., 2009; POLLOCK, 1988).
  - **Baseline (Control) Efficiency:** If baseline efficiency is already high without punishment, incremental gains from punishment may be smaller.
  - **Antisocial or Retaliatory Punishment:** Predictions should be tempered in settings with high risk of antisocial punishment or retaliation spirals, which can reduce or negate efficiency gains (Sylwester et al., 2013; Rumble et al., 2022).
  - **Stability and Timing:** Frequent parameter oscillation or delay in punishment weakens positive effects (Allgaier et al., 2020).

- **Indirectly Informed Dimensions:**  
  For some design dimensions (e.g., chat, show_n_rounds, reward_exists), the literature only provides contextual or mechanism-based arguments, rather than direct efficiency implications.

- **Ambiguity Caveat:**  
  The absence of empirical effect sizes, and the reliance on theoretical predictions with differing outcome measures or modeling assumptions, necessitate caution in making quantitative forecasts.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed (i.e., efficiency effects are explicitly modeled or discussed as a function of this variable):**
- **player_count:** Frequently discussed—positive effects of punishment are stronger in moderate-to-large groups and with spatial structure (Noailly et al., 2009; POLLOCK, 1988; Kol'veková et al., 2021).
- **num_rounds:** Present in repeated game models, which show that more rounds typically increase the scope for punishment effects and sustained cooperation.
- **mpcr (marginal per-capita return):** Models explicitly track the relationship between mpcr and both behavioral and efficiency outcomes (Kol'veková et al., 2021; Baker & Rachlin, 2002).
- **punishment_cost:** Central to nearly all relevant models; low to moderate cost is generally required for positive efficiency effects.
- **punishment_tech (technique, e.g., peer/centralized/shared):** Models compare peer vs. supervisor, pool vs. peer, and endogenous vs. exogenous punishment (Kol'veková et al., 2021; Moreno & Gutierrez-Garcia, 2018).
- **all_or_nothing:** Addressed in binary / discrete models (Kol'veková et al., 2021; POLLOCK, 1988).

**Indirectly informed (mechanistically discussed, but not modeled for efficiency):**
- **chat:** Mentioned as an enhancer of cooperation but not modeled for efficiency or payoff (Lazarus, 2023).
- **default_contrib:** Only contextually referenced.
- **show_n_rounds, show_other_summaries, show_punishment_id:** Sometimes discussed as affecting observability or monitoring, but not directly mapped to efficiency outcomes.

**Contextual or missing:**
- **reward_exists, reward_cost, reward_tech:** Reward mechanisms discussed as complements or alternatives to punishment, but their effect on efficiency (versus punishment) is less directly modeled, with a few exceptions (Baker & Rachlin, 2002).
- **show_n_rounds, show_other_summaries, show_punishment_id:** Rarely, if ever, directly quantified for payoff impacts.

**Not represented:**
- No papers directly model the effect of default contribution property, detailed reward parameters, or full combinations of “show” variables on efficiency.

# 7) Important Limitations

- **Empirical Gaps:**  
  All evidence is theoretical or computational. There are no direct empirical, laboratory, or field estimates of efficiency changes due to enabling punishment across PGG designs, nor any meta-analytic data.

- **Payoff vs. Behavior:**  
  In many papers, efficiency is not the central outcome—contribution rate or norm compliance often stand in as proxies for efficiency, but punishment costs or bystander impacts may reduce net payoffs even as cooperation rises.

- **Context Dependency and Ambiguity:**  
  The net efficiency effect of punishment is shown to depend nonlinearly on multiple factors (cost, group structure, antisocial uses, etc.), and in some parameter regions or social contexts, punishment may have no effect or even reduce efficiency.

- **Partial Dimension Coverage:**  
  Only a subset of the 14 design dimensions are robustly addressed with respect to efficiency; several (e.g., information displays, default setting, detailed reward mechanisms) are either absent or only discussed in a mechanistic fashion.

- **No Quantitative Effect Sizes:**  
  The literature can support directional qualitative predictions (e.g., “efficiency likely to increase with effective, not excessively costly punishment in group-structured games”) but does not provide quantitative mappings or effect sizes to use in parametric prediction.

- **External Validity and Specificity:**  
  Many papers model adjacent environments (CPR, bargaining games, contests, real-world political or organizational systems) that may only approximate PGG-specific dynamics.

---

**In summary:**  
This literature set supports qualitative prediction that enabling peer punishment in a public goods game will, under many design regimes, increase efficiency relative to control. This effect is conditional on design dimensions such as punishment cost, group structure, and risk of antisocial punishment, and is less likely in small or dyadic games or in unstructured, high-retaliation contexts. However, the absence of laboratory empirical findings and the limited direct mapping between payoff ratios and specific design variables means that predictions should be made with caution, preserving the contingencies and nonlinearities present in the theoretical models (Kol'veková et al., 2021; Noailly et al., 2009; POLLOCK, 1988; Sylwester et al., 2013; Whitmeyer, 2004).
