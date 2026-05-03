# Evidence Base

This paper set includes a diverse mix of theoretical and empirical work, but is weighted toward theory papers with only one clear empirical experimental study (Engel & Zhurakhovska, 2017). The other four are primarily theoretical, with two focusing on evolutionary game models in standard PGG or multi-agent frameworks (Zhang & Cao, 2020; Wang et al., 2022), one a review of behavioral and institutional interventions with reference to lab findings (Janssen, 2015), and one addressing punishment versus reputational sanctions in a moral hazard context (Baker & Choi, 2018). The breadth is moderate: the set covers standard public goods games (PGG), empirical and theoretical arguments about sanctions, and both payoff and behavioral outcomes, but only a subset present direct, quantitative evidence about efficiency in lab PGGs with and without punishment.

# Task Relevance

### pgg_or_variant
- **exact**: Two of the papers (Zhang & Cao, 2020; Engel & Zhurakhovska, 2017) study standard linear or extended PGGs directly.
- **close**: Janssen (2015) discusses PGGs and closely related common pool resource dilemmas.
- **adjacent**: Baker & Choi (2018) and Wang et al. (2022) are structurally related but tailored to other domains (litigation/moral hazard, enterprise innovation with spillover), using repeated game or cooperation frameworks.

### punishment_or_sanctions
- **exact**: All five papers treat punishment or legal sanctions centrally, with explicit model or manipulation.
- **exact**: Both peer and centralized punishment mechanisms are considered. Engel & Zhurakhovska (2017) specifically investigate centralized punishment.

### efficiency_or_related_payoff_outcome
- **exact**: Zhang & Cao (2020), Baker & Choi (2018) (theoretical) explicitly model efficiency as a central outcome.
- **close**: Engel & Zhurakhovska (2017) and Janssen (2015) report group payoff, mean earnings, or “profit,” but these are not always normalized as efficiency.
- **adjacent**: Wang et al. (2022) emphasize the probability and stability of cooperation, not direct payoff or efficiency; the link must be inferred.

# Outcomes Measured In The Literature

- **Payoff-related outcomes**: Efficiency (as ratio to maximum), total/group payoff, profit, earnings, and (in theory) welfare and surplus are the focus in Zhang & Cao (2020), Engel & Zhurakhovska (2017), Baker & Choi (2018), and are referenced in Janssen (2015).
    - However, direct experimental measurement of efficiency is rare; group earnings/profits are more common empirically (Engel & Zhurakhovska, 2017; Janssen, 2015).
    - Some theory (Baker & Choi, 2018; Zhang & Cao, 2020) focuses on modeled efficiency but without empirical quantification.
- **Non-payoff behavioral outcomes**: These include contribution rates, norm compliance, enforcement frequency, and strategy stability (primary in Wang et al., 2022, and also Engel & Zhurakhovska, 2017). These outcomes generally support the mechanism for payoff improvement but are not direct measures of efficiency.
- **Other outcomes**: Centralized vs. peer punishment mechanisms, the role of communication, and information structure are also highlighted.

# Main Findings Relevant To Prediction

- **Enabling punishment increases efficiency when punishment is strong enough relative to the public goods multiplier, group size, and when escape options are not too attractive** (Zhang & Cao, 2020). The theoretical model provides threshold conditions for when punishment transforms low-efficiency (defection/cycles) to high-efficiency (full cooperation) equilibria.
- **Experimental evidence shows that centralized punishment by a non-beneficiary authority reliably raises both contributions and group payoffs above the no-punishment baseline in repeated PGGs** (Engel & Zhurakhovska, 2017). Although not reported as a ratio to the optimum, group profit/earnings increase with punishment.
- **Review evidence confirms that both communication and punishment increase average group earnings and reduce resource overuse in common-pool/PGG settings** (Janssen, 2015), but stresses that the effect size and sustainability depend on group size, communication, the fairness of sanctioning, and cultural/institutional context.
- **Theory suggests that legal sanctions (formal punishment) can dominate reputational sanctions for deterring bad behavior and boosting efficiency, especially when punishment is accurate, public, and not too expensive** (Baker & Choi, 2018).
- **Effectiveness of punishment on behavioral outcomes is robust—higher penalty or greater threat increases cooperation rates and reduces opportunism—but direct efficiency gains must be inferred** (Wang et al., 2022).

# Prediction Guidance

The collected literature provides the following core guidance for predicting the efficiency effect of enabling peer (or centralized) punishment in PGG-like settings:
- **Punishment tends to increase efficiency, but only when strong enough relative to group size and the returns to cooperation** (Zhang & Cao, 2020; Engel & Zhurakhovska, 2017). Weak or costly punishment, easy escape routes, or attractive non-cooperative options (like lonership or speculation) can diminish or nullify this effect.
- **Improvements in efficiency are supported both by behavioral mechanisms (higher cooperation rates) and, in most models/experiments, by observed or predicted gains in group payoff.** However, payoffs do not always reach the social optimum; the predicted effect on efficiency is often an increase, but not necessarily full efficiency.
- **Game design factors such as group size, punishment cost/magnitude, communication, and potential for centralization all moderate the effect.** Higher player count can dilute punishment effectiveness unless punishment scales adequately; high punishment cost reduces effectiveness; communication generally amplifies the benefit; centralized punishment can be especially effective (Engel & Zhurakhovska, 2017; Janssen, 2015).
- **Where only behavioral outcomes are reported, positive movement in cooperation rates suggests, but does not guarantee, increased efficiency** (Wang et al., 2022).

Thus, for the prediction task: If the control game with no punishment is inefficient, and punishment is added with significant penalty-to-cost ratio and no strong compensating escape avenues, a material efficiency increase can be predicted. The specific magnitude will depend on parameter thresholds as given in theory (Zhang & Cao, 2020), with empirical confirmation in lab experiments (Engel & Zhurakhovska, 2017).

# Design Dimensions Highlighted Across Papers

- **Directly informed**:
    - `player_count`: Explicitly treated in theoretical (Zhang & Cao, 2020; Baker & Choi, 2018; Wang et al., 2022) and empirical (Engel & Zhurakhovska, 2017) work.
    - `num_rounds`: Modeled in theory (Zhang & Cao, 2020; Baker & Choi, 2018), important in repeated games; set in experiments.
    - `all_or_nothing`: Discussed in theoretical models (Zhang & Cao, 2020; Baker & Choi, 2018; Wang et al., 2022), also in lab protocols.
    - `mpcr`: Public goods multiplier is central in models and experiments.
    - `punishment_cost`, `punishment_tech`: Both mechanism of punishment, and the cost per unit, are explicitly analyzed across four papers.
    - `chat`: Role of communication is discussed (Janssen, 2015; Engel & Zhurakhovska, 2017).

- **Indirectly or contextually discussed**:
    - `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Mostly referenced in lab details (Engel & Zhurakhovska, 2017).
    - `punishment_magnitude`: Present as fine (alpha) in models.
    - `default_contrib`: Not discussed; none of the papers vary contribution framing.

- **Sparse or missing**:
    - `reward_exists`, `reward_cost`, `reward_tech`: None of the papers analyze reward mechanisms alongside punishment in prediction of group efficiency.
    - `default_contrib`, `show_punishment_id`: Not referenced explicitly as manipulations or tested factors.

# Important Limitations

- **Empirical evidence on efficiency is limited to a single laboratory experiment** (Engel & Zhurakhovska, 2017), and even there, outcomes are reported as group profit/earnings, not normalized efficiency.
- **Most payoff effects are theoretical predictions or indirect inferences from cooperation rates or earnings**, limiting the precision of predicted efficiency changes.
- **Some papers model or review institutional/field settings only adjacent to PGGs (e.g., punishment in legal or enterprise contexts), so their comparative statics support, but do not quantify, efficiency effects in lab public goods settings** (Baker & Choi, 2018; Wang et al., 2022).
- **Key design dimensions such as reward options, punishment identity visibility, and contribution framing are not systematically varied or tested.**
- **Effects are context-dependent:** Cultural, institutional, and group-specific variables (communication, centralization, heterogeneity) can modulate observed efficiency changes in ways not fully predicted by abstract models.
- **Theoretical models may assume large, well-mixed populations without repeated encounters or fine-grained strategic learning, limiting direct extrapolation to small lab groups or real-world settings.**
- **Crowding out and sustainability of efficiency gains are noted as issues but not analytically resolved in the set** (Janssen, 2015).
- **Ambiguity remains in threshold effects:** Under which parameter ranges does punishment deliver material gains in efficiency? Quantitative boundaries are provided only in abstract terms (Zhang & Cao, 2020), and empirical calibration is sparse.

---

**Summary:**  
The literature set provides theoretical and some empirical support that enabling punishment in public-goods-game-like environments will, under the right conditions (punishment strong/effective, costs reasonable, few loopholes), increase efficiency relative to the control. Most relevant evidence applies when prediction input dimensions (punishment design, group size, MPCR) fall within analyzed regimes. However, quantitative evidence is sparse; the role of less-studied design features and context dependency should be acknowledged in any prediction.
