# 1) Evidence Base

The paper set consists entirely of theoretical and model-based work, with no empirical or laboratory experiments directly reported. The literature is relatively broad conceptually, drawing on evolutionary theory, game theory, agent-based models, epistemic discussions, and reviews across various contexts (e.g., climate, networked cooperation, cultural evolution, online reputation, food storage). However, the empirical grounding is largely limited to references to prior experimental literature rather than novel data. Most models and arguments are adjacent to, but not always directly instantiated as, standard linear public goods games (PGGs). There is a high level of abstraction, and outcome measures vary widely, with a mixture of payoff-based and behavioral outcomes.

# 2) Task Relevance

**pgg_or_variant:**  
- **Label:** Predominantly "adjacent" or "close" (few "exact").  
- Direct modeling of standard PGGs is rare. Many papers use PGG-like settings (e.g., threshold games, stag hunt, network cooperation, common-pool resources) or refer to experimental economics PGGs as supporting context. This means that although structural analogies are strong, few results are strictly parameterized as linear PGGs relevant to the prediction task.

**punishment_or_sanctions:**  
- **Label:** Generally "exact" (when discussed), though coverage varies.  
- Punishment is a central focus throughout; most papers model or theorize about punishment or sanctions. However, the form varies (peer, centralized, reputation-based, meta-punishment, access exclusion), and few studies provide detailed breakdowns along all relevant technological or institutional dimensions (e.g., punishment_id, peer vs. centralized).

**efficiency_or_related_payoff_outcome:**  
- **Label:** Mixture of "exact", "close", and many "adjacent"/"weak".  
- A subset of papers report or directly model group payoff, welfare, or efficiency; many more focus primarily on behavioral outcomes (cooperation rate, norm compliance, honesty), with only indirect reference to efficiency.

**Summary:**  
The literature is highly relevant in terms of mechanisms and theoretical predictions, but not well anchored in direct, parameterized, empirical prediction of average efficiency in standard PGGs as a function of the full set of design dimensions.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes (efficiency, total group payoff, welfare):**  
- A minority of papers report these precisely, largely via theoretical models (e.g., Vlerick, 2016; Vanderschraaf, 2016; Zhang & van der Schaar, 2013; Xu et al., 2014; O’Connor, 2016).  
- In several cases, group achievement or success in threshold games is used as a proxy for group payoff (Vasconcelos et al., 2013).  
- Review papers summarize evidence that earnings or welfare improve with the introduction of punishment or communication (Janssen, 2015).

**Non-payoff behavioral outcomes:**  
- The majority of papers focus on behavioral proxies: cooperation rate, norm compliance, honesty prevalence, willingness to cooperate, frequency of enforcement, or evolutionary stability of strategies (Bruner, 2013; Forber & Smead, 2016; Mameli, 2013; Cushman, 2015).  
- Outcomes such as successful norm enforcement, group honesty, prevalence of cooperators, and reduction of defection are frequent.

**Key distinction:**  
Payoff-related measurement is less prevalent than behavioral, and often only implied through models showing behavioral shifts toward cooperation.

# 4) Main Findings Relevant To Prediction

- **Consistent theoretical support:** The literature robustly theorizes that enabling punishment in PGG-like environments increases cooperation and, by extension, average efficiency or group payoff, moving the system from inefficient equilibria toward efficient, cooperative equilibria (Vlerick, 2016; Vanderschraaf, 2016; Zhang & van der Schaar, 2013; Xu et al., 2014; Janssen, 2015).
- **Role of punishment structure:** The effectiveness of punishment depends critically on the incentive structure—punishment must be strong enough to deter defection, but not so costly or aggressive as to reduce overall group payoff (Bruner, 2013; Li, 2017; Angourakis et al., 2015).
- **Mechanism specifics:**  
    - Reputation-based and rating-sanction protocols are highlighted as especially efficient when compared to direct, ad-hoc peer punishment (Zhang & van der Schaar, 2013; Xu et al., 2014).
    - Local, group-level punishment is more effective than global or highly centralized forms in some settings (Vasconcelos et al., 2013).
    - Proper tuning of punishment strength, cost, and technological implementation is necessary; overly harsh punishment or excessively high costs can be counterproductive (Angourakis et al., 2015).
- **Key moderators:** Efficacy of punishment is context dependent: group size, communication, cultural background, risk perception, repeated interaction, cost structure, and transparency all moderate the impact (Janssen, 2015; Vasconcelos et al., 2013; Mameli, 2013; Sterelny, 2016).
- **Rationale for effect:** The mechanism is primarily through deterring free-riding and stabilizing cooperation; however, high levels of anti-social punishment or retaliation may reduce payoffs under some conditions (Cushman, 2015).

# 5) Prediction Guidance

- **Direction of effect:** The literature strongly supports predicting that enabling peer punishment (under generic or well-calibrated conditions) will *increase* average efficiency in PGG-like environments.
- **Magnitude of effect:** There are no empirical quantitative estimates or precise parameters mapping control efficiency to treatment efficiency; prediction must be qualitative or based on direction and a presumption of improvement.
- **Parameter sensitivity:** The predicted efficiency gain is sensitive to design features, especially:
    - Punishment cost and magnitude (punishment must be credible and not excessively costly).
    - Group size and communication (effectiveness tends to decline in larger or less transparent groups; communication can act synergistically).
    - Form of punishment (peer vs. centralized, direct vs. rating/reputation-based).
- **Use of control efficiency:** If the control game already achieves high efficiency (e.g., via communication or strong social norms), the marginal effect of adding punishment may be reduced (crowding out—Janssen, 2015).
- **Contextual caveats:** If the punishment mechanism is weak, poorly specified, or if the game design allows for retaliation or anti-social punishment, the efficiency gains may not materialize—and group efficiency might even decline (Cushman, 2015; Angourakis et al., 2015).
- **Inference risk:** Given the evidence is mostly theoretical, predictions should be hedged: punishment generally raises efficiency, but with significant moderation by the above factors.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**  
- **player_count:** Regularly considered; effects on mechanism efficacy (Vasconcelos et al., 2013; Vanderschraaf, 2016; Xu et al., 2014; Mameli, 2013).
- **punishment_cost, punishment_tech:** Frequently discussed; central to model tuning and effectiveness (Vlerick, 2016; Bruner, 2013; Zhang & van der Schaar, 2013).
- **mpcr (Marginal per-capita return):** Modeled in some game-theoretic papers (Vasconcelos et al., 2013; Xu et al., 2014).
- **all_or_nothing, num_rounds:** Modeled in agent-based and evolutionary games (Xu et al., 2014; O’Connor, 2016; Angourakis et al., 2015).
- **chat (communication):** Recognized as co-factor or moderator (Janssen, 2015; Mameli, 2013).

**Indirectly/Contextually Discussed:**  
- **reward_exists, reward_cost, reward_tech:** Raised as strategic complements or alternatives to punishment (Bruner, 2013); less often central to analysis.
- **default_contrib:** Only contextually mentioned in model assumptions.
- **show_n_rounds, show_other_summaries, show_punishment_id:** Occasionally referenced as factors affecting transparency and coordination (O’Connor, 2016; Sterelny, 2016; Mameli, 2013).

**Effectively Missing or Not Well Informed:**  
- **Empirical calibration of all dimensions:** No papers supply direct empirical tests for the full parameter space or report efficiency outcomes as a function of all 14 design features.
- **Interaction effects:** Multi-way interaction effects between dimensions are not systematically analyzed—particularly for reward vs. punishment joint design, or the impact of summary/identity features.

# 7) Important Limitations

- **Lack of empirical data:** The set is devoid of new or direct empirical studies matching the prediction task; results are theoretical or model-based, and references to experimental work are used only as background.
- **Adjacency of models:** Very few studies model the *exact* linear PGG relevant to typical laboratory experiments. Analogous games may display different qualitative or quantitative effects under design manipulations (e.g., threshold games, networked reciprocity, two-player stag hunts).
- **Outcome ambiguity:** Payoff-related outcomes are not always directly reported; in many cases, only behavioral outcomes are analyzed, and efficiency is inferred or proxied.
- **Parameter mapping gap:** There's weak quantitative mapping from the control efficiency and design parameters to the anticipated magnitude of efficiency improvement under punishment.
- **Complex moderators:** The literature notes that efficiency effects are contingent on context (group size, communication, network structure, cultural norms), yet formal cross-paper synthesis on how each moderator impacts efficiency is incomplete.
- **Potential for negative or null effects:** Some theoretical contexts warn that punishment, if costly or subject to retaliation, might not increase (or might even decrease) group payoff, but the empirical calibration of these scenarios is lacking (Cushman, 2015; Angourakis et al., 2015).
- **Coverage of design space:** Certain prediction dimensions are missing or only referenced in passing, especially for technological features (e.g., show_punishment_id) or reward mechanisms.

---

**Summary for Prediction Tasks:**  
- Literature synthesizes strong qualitative support for the expectation that peer punishment increases efficiency in public-goods-game-like environments, relative to baselines without punishment, but empirical magnitude and parameterization are not directly available. Most evidence is theoretical, focused on mechanisms and contextual moderators; prediction should account for possible moderation by group size, cost structure, communication, and form of punishment. No direct mapping from all 14 design dimensions to effect size is available, and control efficiency is not formally linked to expected treatment efficiency except as a qualitative prior.
