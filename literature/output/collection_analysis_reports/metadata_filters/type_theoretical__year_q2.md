# Evidence Base

The evidence base consists almost exclusively of theoretical and simulation/modeling papers, with minimal direct empirical or laboratory experimental data. Nearly all papers are theory-driven, focusing on evolutionary and mathematical models of public goods games (PGGs), social dilemmas, and related environments. The scope is broad in terms of the types of cooperation dilemmas and punitive mechanisms considered but is narrow with respect to real-world measured efficiency changes, as experimental (lab-based) evidence is rare or absent in this set.

Key features of the evidence base:

- **Type of evidence:** Theoretical/analytical models, agent-based simulations, evolutionary game theory, and reviews of existing theory dominate.
- **Breadth versus depth:** The papers cover a wide variety of variants ("PGG or adjacent") and hypothesized mechanisms, but most do not provide direct, quantitative predictions of group efficiency in standard PGG experiments.
- **Focus:** The majority of the research is targeted at understanding the underlying mechanisms—how punishment, network structure, and incentive design affect cooperation and, by extension, group payoff.
- **Empirical gap:** Direct empirical measurement of efficiency before and after enabling punishment in lab or field PGGs is lacking; thus, transfer to real-world or experimental predictions requires caution.

# Task Relevance

## pgg_or_variant

- **exact:** Most highly relevant papers are theory models of PGGs—linear, threshold, spatial, repeated, and networked forms. However, there are also many adjacent studies (e.g., Prisoner's Dilemma, Snowdrift games), which, while closely related, do not map directly onto PGG payoffs or institutional structures.

## punishment_or_sanctions

- **exact:** The core focus is on punishment and sanctions. The majority of theoretical papers model costly punishment, exclusion, or coordinated sanction institutions as mechanisms for controlling defection.
- **close/adjacent:** Some papers focus primarily on alternative mechanisms (reward, tolerance, conditional cooperation, reputation), sometimes discussing punishment for reference or as a comparison. Others focus on punishment in related dilemmas but not with the structure of PGGs.

## efficiency_or_related_payoff_outcome

- **exact:** Several papers explicitly model and report on group efficiency (i.e., total group payoff relative to maximum possible under full cooperation) or analogous metrics (welfare, average payoff, surplus).
- **close:** Many studies use cooperation rates, prevalence of strategies, or achievement of group thresholds as proxies for efficiency but do not compute payoff-based efficiency directly.
- **adjacent/weak:** Some reports focus exclusively on behavioral outcomes (e.g., contribution rates, punishment frequency), with only indirect implications for efficiency.

# Outcomes Measured In The Literature

- **Payoff-based outcomes (efficiency, group payoff, welfare):** Some modeling papers (e.g., Wu et al. 2014; Levine & Modica 2016; Hetzer & Sornette 2013; Wang et al. 2015; among others) provide explicit group efficiency measures.
- **Non-payoff behavioral outcomes:** The majority of studies, especially those modeling evolutionary dynamics, report on frequencies of strategies (cooperators, defectors, punishers, etc.), cooperation rates, stability of cooperative equilibria, or the fraction of groups achieving a threshold.
- **Linkage:** While behavioral outcomes are used to infer potential efficiency changes (assuming higher cooperation generally raises group payoff), this is not always valid, especially where costly punishment reduces total payoff despite higher cooperation.

# Main Findings Relevant To Prediction

Synthesizing across high-relevance sources, the literature yields the following main findings for predicting the average efficiency of PGGs when peer punishment is enabled:

- **Punishment often increases efficiency compared to no-punishment baseline, especially when punishment is not too costly and sufficiently effective** (Wu et al., 2014; Levine & Modica, 2016; Szolnoki & Perc, 2013, 2017; Roberts, 2013; Hetzer & Sornette, 2013; Sui et al., 2017). In both spatial and well-mixed environments, if punishment cost is reasonable, enabling punishment can move the group from low to high efficiency, sometimes producing full cooperation.

- **The effectiveness of punishment depends critically on game parameters:**
    - **Punishment cost:** Lower cost to the punisher increases the parameter range where efficiency gains are observed (Wu et al., 2014; Levine & Modica, 2016; Hetzer & Sornette, 2013).
    - **Marginal per-capita return (mpcr):** Low mpcr games (where cooperation is otherwise hard to sustain) gain the most from enabling punishment (Wu et al., 2014; Perc et al., 2017; Cong et al., 2016).
    - **Group size (player_count):** Punishment can sustain efficiency even in large groups if design allows for coordination or local clustering (Levine & Modica, 2016; Perc et al., 2017; Hwang, 2017; Sui et al., 2017).
    - **Punishment technology:** The structure of punishment (peer vs. institutional, exclusion vs. point-deduction, centralized vs. decentralized) moderates its effect (Wolitzky, 2013; Szolnoki & Perc, 2013, 2017; Liu et al., 2017).

- **Potential negative/moderated effects:**
    - **Costly or misapplied punishment can decrease efficiency:** If punishment is too expensive or prompts cycles of retaliation, it may reduce group payoff despite higher cooperation (Barrett, 2016; Kurzban et al., 2015; Kroupa, 2014; Ezeigbo, 2017; Handfield et al., 2016).
    - **Antisocial punishment, corruption, or inefficient mechanisms can neutralize or reverse efficiency gains** (Hauser et al., 2014; Lee et al., 2015, 2017; Farjam et al., 2015). Design that permits antisocial or "perverse" punishment or makes enforcement vulnerable to corruption will often show little or negative efficiency improvement when enabling punishment.
    - **Reward as an alternative or complement:** Some models find reward (including tax-based funding for reward) can be more efficient than punishment, depending on parameters and implementation (Yao & Chen, 2014; Chen et al., 2015; Cong et al., 2016).

- **Interplay with other dimensions:**
    - **Spatial/network structure:** Structured populations (lattices, restricted neighborhoods) allow clustering of cooperators/punishers and extend the efficiency impact of punishment to harsher conditions (Perc et al., 2017; Hetzer & Sornette, 2013; Oya & Ohtsuki, 2017).
    - **Transparency, monitoring, and information:** Effectiveness of punishment increases with better monitoring and public information about contributions and/or punishment (Wolitzky, 2013; Schoenmakers et al., 2014; Wolitzky, 2013).
    - **Co-occurrence with exclusion or social pressure:** Exclusion mechanisms (ostracism, peer or pool exclusion) and social pressure are often found to outperform or complement costly punishment, especially for maintaining high long-term efficiency (Sasaki & Uchida, 2013; Liu et al., 2017).

- **Balance with reward and second-order sanctions:** Some models (Cong et al., 2016; Okada et al., 2015) point to the need for a balance between punishment and reward, and for mechanisms to resolve second-order free-riding (e.g., punishing non-punishers) to maintain efficiency in the long run.

# Prediction Guidance

Given the above, the literature supports the following guidance for downstream prediction of average efficiency in PGGs with peer punishment enabled, conditioning on design dimensions and control efficiency:

- **Punishment is predicted to increase average efficiency over control (no-punishment), particularly when:**
    - **Punishment cost is not prohibitively high,**
    - **Punishment effectiveness (impact per cost) is sufficient to deter defectors,**
    - **MPCR is low to moderate,**
    - **Group size is not so large as to make monitoring/neighborhood effects ineffective unless institutional or coordinated punishment is present,**
    - **Game structure allows identification/monitoring/coordination of punishers,**
    - **Antisocial punishment or high rates of corruption are not present or can be suppressed.**

- **The effect size may be muted, zero, or negative if:**
    - **Punishment cost is high (pay cost > expected benefit),**
    - **Punishment is easily misapplied (antisocial punishment or counter-punishment is high),**
    - **Enforcement mechanisms are vulnerable to corruption, or monitoring is weak,**
    - **Group size is large and design does not support coordination or clustering,**
    - **Reward, exclusion, or alternative mechanisms are more efficient given the parameterization.**

- **Predictions should be tempered by the control (no-punishment) efficiency:** Where baseline efficiency is already high, enabling punishment may yield only marginal improvements and, due to punishment costs, could even reduce efficiency. Where baseline efficiency (cooperation) is low, and the above favorable conditions are met, the introduction of punishment can produce large gains (even transforming low- to high-efficiency regimes).

- **Use design dimensions to adjust expectations:** For each major design parameter (player_count, num_rounds, mpcr, punishment_cost, punishment_tech, spatial/network structure, information/monitoring, presence of reward, etc.), the findings provide qualitative or, in some cases, analytic guidance for predicting the direction and (when possible) relative magnitude of the efficiency change.

# Design Dimensions Highlighted Across Papers

## Directly Informed Dimensions

Well-covered by the theory papers and central to the mechanisms analyzed:

- **player_count (group size):** Strongly addressed; affects the stability of cooperation and how easily punishment enforces efficiency.
- **num_rounds (repetition):** Extensively modeled; longer games support more effective punishment.
- **mpcr (marginal per-capita return):** Central parameter; lower mpcr increases the need for punishment/reward to sustain efficiency.
- **punishment_cost:** Core dimension in nearly every model studying punishment; the cost/efficiency tradeoff is frequently characterized.
- **punishment_tech (technology):** Type and structure of punishment (peer/institutional, exclusion/point deduction, centralized/decentralized) are key moderators.
- **reward_exists/reward_cost/reward_tech:** Many models compare punishment and reward or analyze their joint or comparative impact.
- **all_or_nothing, default_contrib, spatial/network structure:** Addressed in studies modeling continuous vs. binary contribution, network/clustering effects.

## Indirectly Informed/Contextually Discussed Dimensions

- **chat, show_n_rounds, show_other_summaries, show_punishment_id:** Discussed less directly. Some papers mention effects of transparency/communication and information structure (monitoring, identification of punishers/rewarders) as moderators of punishment's effectiveness, but rarely as direct parameters of comparison.

## Missing or Sparse Dimensions

- **default_contrib:** Not generally manipulated directly as a design parameter; framing effects (opt-in/opt-out) are not primary focus.
- **chat:** While communication is often noted as beneficial for cooperation, its interaction with punishment's effect on efficiency is not deeply modeled.
- **show_other_summaries, show_n_rounds, show_punishment_id:** These are only occasionally addressed as they impact information available for coordination, but very few papers systematically study their effect on efficiency with punishment.
- **Complex combinations:** Most models study a subset of dimensions, and combinatorial interactions (e.g., chat × group size × punishment type) are usually not exhaustively mapped.

# Important Limitations

- **Predominantly theoretical/simulation-based:** Findings are not based on direct experimental manipulations or real-world data; empirical validation is weak.
- **Key moderators underrepresented:** There is less systematic analysis of how certain design dimensions (e.g., chat, summary visibility, punishment identity) affect efficiency changes due to punishment.
- **Efficiency outcomes sometimes inferred, not reported:** Many studies use non-payoff outcomes (e.g., cooperation rates) as proxies for efficiency, which can be misleading when punishment costs are high.
- **Absence of payoff-based experimental controls:** Very few studies report efficiency ratios from actual experiments with and without punishment under controlled conditions.
- **Potential for oversimplified mapping:** Real-world institutional, psychological, or cultural moderators (e.g., retaliatory norms, reputation, cultural variance in antisocial punishment) may not be captured by the models.
- **Ambiguity where studies disagree:** Some models predict negative or zero efficiency impacts of punishment (especially when antisocial punishment, high cost, or corruption is present), meaning predictions should maintain uncertainty where these risk factors are non-negligible.
- **Absence of quantitative effect sizes:** While qualitative direction of effect is often clear, quantitative predictions of the magnitude of efficiency gains or losses with punishment are generally unavailable.

---

**Summary:**  
The literature set robustly supports theoretical predictions about the conditions under which enabling peer punishment in PGG-like environments increases group efficiency, relative to the no-punishment baseline. The effect is highly sensitive to design dimensions such as punishment cost, mpcr, group size, type of punishment mechanism, and features supporting coordination, monitoring, and exclusion. However, the almost-complete absence of empirical efficiency measurements and the reliance on behavioral proxies or simulation outputs mean that predictions of treatment efficiency should be made cautiously and critical moderators must be explicitly considered. The design dimension coverage aligns well with the main parameter set for prediction, with the exception of certain information and communication features, which are less well developed in the theoretical literature. Ambiguity should be preserved, especially for parameter regimes where models predict divergent outcomes (e.g., high cost or antisocial punishment, very large groups without coordination mechanisms, ambiguous monitoring).
