# 1) Evidence Base

This paper set consists primarily of theoretical contributions, with no dedicated empirical or experimental studies. The scope is moderately broad in disciplinary background—spanning evolutionary theory, agent-based modeling, social and ecological modeling, and network/game theory—but most papers are only **adjacent** to classic public goods games (PGGs) and often focus on general mechanisms of cooperation and punishment. Only one paper (Wu & Sun, 2022) directly models a PGG-like structure and mechanisms for peer punishment; the remainder are conceptual or explore related settings (e.g., common-pool resources, collaborative innovation networks, and social-ecological systems). Across the set, the primary focus is on behavioral and structural mechanisms—such as cooperation, norm enforcement, and sanction systems—rather than direct group efficiency or payoff-based outcomes.

# 2) Task Relevance

**pgg_or_variant**
- **Exact**: Wu & Sun (2022) is the only paper with direct (exact) relevance, modeling a true public goods game.
- **Close/Adjacent**: Several papers model or theorize about settings with strong structural parallels (Angourakis et al., 2015; Liu & Yang, 2018), such as common-pool resource dilemmas or multi-agent innovation networks, but do not implement true PGGs. Others are further removed, focusing on broader cooperative dilemmas or cultural evolution (CAMPBELL, 1991; Andrews & Davidson, 2013; Suratin et al., 2023).
- **None/Weak**: Sthel et al. (2013) is distant from PGGs, discussing cooperative architectures without a game-theoretic or incentive-based frame.

**punishment_or_sanctions**
- **Exact**: Three papers (Wu & Sun, 2022; Liu & Yang, 2018; Andrews & Davidson, 2013) explicitly analyze the effects of punishment or sanctions (peer or institutional).
- **Adjacent**: Other papers cover related topics like exclusion or access control (Angourakis et al., 2015), social or supernatural sanctions (Suratin et al., 2023; CAMPBELL, 1991), or discuss incentives generally.
- **None**: Sthel et al. (2013) does not address punishment or sanction mechanisms.

**efficiency_or_related_payoff_outcome**
- **Exact**: No paper reports efficiency or group payoff as defined in the prediction task.
- **Close/Adjacent**: Wu & Sun (2022) and Angourakis et al. (2015) report on total contributions, cooperation rates, surplus, and system performance, which are adjacent but not strict efficiency measures. Multiple papers focus only on behavioral outcomes such as strategy frequency, cooperation, or norm compliance.
- **None**: Several papers provide only conceptual or historical analysis without quantitative outcome data (Sthel et al., 2013; CAMPBELL, 1991).

**Summary:**  
The literature set is **limited in direct relevance** to the task: only one paper offers a model with both PGG structure and explicit peer punishment, and none provide empirical or experimental efficiency results needed for predictive modeling. Evidence on payoff-based outcomes is mostly indirect or adjacent.

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes:**  
- The only outcomes even adjacent to efficiency or group payoff are:
  - **Total contributions** or **cooperation rates** (Wu & Sun, 2022; Angourakis et al., 2015): These are **not** strictly efficiency but can be seen as upper bounds or correlates.
  - **Surplus/shortage avoidance** (Angourakis et al., 2015): Distantly related to group payoff.
  - **System performance** (aggregate behavioral or social outcomes), but not monetized payoffs.

**Non-Payoff Behavioral Outcomes:**  
- **Cooperation frequency** or **strategy adoption** (Liu & Yang, 2018)
- **Behavioral compliance**, **norm stability**, or **trust/reciprocity** (Suratin et al., 2023; Andrews & Davidson, 2013; CAMPBELL, 1991)
- **Gossip propagation** and **false-positive punishment exposure** (Wu & Sun, 2022)
- **Emergence/persistence of cooperation** (generalized evolutionary arguments)

**No Payoff Data:**  
- Most papers do **not** report payoffs, surplus, or efficiency metrics in the terms required for prediction; they instead discuss mechanisms, conditions, or strategies for cooperation.

# 4) Main Findings Relevant To Prediction

Synthesizing across papers, several theoretically and model-based insights are relevant for predicting the effect of enabling peer punishment on efficiency:

- **Punishment tends to increase cooperation**: Multiple models and theoretical syntheses argue that the presence of punishment (particularly when well-calibrated) stabilizes or increases group-level cooperation (Wu & Sun, 2022; Liu & Yang, 2018; Andrews & Davidson, 2013; Suratin et al., 2023; CAMPBELL, 1991).

- **Optimal degree and type of punishment is important**:  
    - Setting punishment too harshly can deter recovery and exclude contributors (Angourakis et al., 2015).
    - Social or reputational punishments can sometimes be more effective than monetary ones, particularly in contexts with high trust or non-utilitarian values (Suratin et al., 2023).
    - Punishment combined with compensation for those wrongly accused (monetary or reputational restoration) boosts cooperation most strongly in model settings (Wu & Sun, 2022).

- **Magnitude and cost matter, but are not directly quantified**:  
    - Models generally include punishment (and reward) costs as strategic parameters, showing that their adequacy relative to defecting incentives is crucial for stable cooperation (Liu & Yang, 2018; Wu & Sun, 2022), but do not specify effects in terms of efficiency.

- **Enforcement mechanisms interact with baseline efficiency/drivers**:  
    - Where baseline (control) cooperation is efficient, excessive punishment is less beneficial and may suppress overall group benefit (Angourakis et al., 2015).
    - Features like dependency on the resource, tolerance for defectors, and the design of exclusion rules shape overall performance, mapping analogously to PGG payoff structures.

- **Reward mechanisms and combined sanction systems**:  
    - Some work notes that the presence of both rewards and punishments offers additional levers for cooperation (CAMPBELL, 1991; Liu & Yang, 2018), but does not specify payoff effects.

Collectively, these findings suggest that enabling punishment is likely to increase cooperation and potentially group efficiency under most conditions, but the actual efficiency gain is likely sensitive to punishment parameters, group composition, and context. These effects are theoretically supported but not empirically demonstrated in efficiency terms in this literature set.

# 5) Prediction Guidance

**What can be concluded for the downstream prediction task?**

- *Qualitative Prediction:*  
  The literature provides indirect and theoretical support for a **positive effect of peer punishment** (especially when well-designed) on group cooperation and, by extension, the efficiency of public-goods-game-like environments (Wu & Sun, 2022; Andrews & Davidson, 2013).

- *Limitations to Quantitative Prediction:*  
  There is **no empirical or direct modeling evidence** in this set that maps game design dimensions (e.g., player count, MPCR, punishment cost) and control efficiency values onto resultant treatment efficiency with punishment.  
  **Total contributions** and **cooperation rates** are reported instead of efficiency or group payoff; thus, any quantitative prediction about the magnitude of efficiency gains remains **unsupported**.

- *Design Implications:*  
  When making downstream efficiency predictions, modelers should:
    - Anticipate that **enabling peer punishment will typically not decrease** and may plausibly **increase efficiency**, particularly in groups where control (no-punishment) efficiency is moderate or low.
    - Recognize that **punishment that is too severe or too lenient** diminishes effectiveness or can even lower welfare/performance through over-punishment or unchecked free-riding (Angourakis et al., 2015).
    - Consider context: **Type of punishment** (social vs. monetary), **compensation mechanisms** for misapplied punishment (Wu & Sun, 2022), and **institutional trust** may all shape outcomes.
    - Treat any attempt to derive **numeric efficiency predictions or estimates** as **unsupported by this literature set**.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- **punishment_cost**: Explicitly modeled (Wu & Sun, 2022; Liu & Yang, 2018), including sensitivity to cost in strategic stability, but not tied quantitatively to efficiency outcomes.
- **player_count, num_rounds, all_or_nothing, mpcr, punishment_tech**: Variously included as structural variables in modeling studies (Wu & Sun, 2022; Angourakis et al., 2015), indicating importance but not quantifying their moderating effects on efficiency.
- **reward_exists**: Considered in several models and theory papers (Liu & Yang, 2018; CAMPBELL, 1991; Suratin et al., 2023).

**Indirectly or Contextually Discussed:**
- **show_other_summaries, show_punishment_id, show_n_rounds**: Only contextually addressed, mainly in terms of transparency/norm-building, not empirically modeled.
- **reward_cost, reward_tech**: Generally raised in discussion of incentive structures, but with little modeled detail.
- **default_contrib**: Framing and behavioral default effects are not directly discussed.
- **chat**: Communication/trust is mentioned as important (Suratin et al., 2023) but not modeled.

**Effectively Missing:**
- Most literature in this set does **not** model or measure the detailed effects of these dimensions on efficiency with punishment enabled. Effects are often hypothesized or justified theoretically without mechanism-specific quantification.

# 7) Important Limitations

- **Empirical data on efficiency is lacking**: The set features no experimental or field data reporting efficiency or group payoff effects of enabling punishment in PGG-like games.
- **Non-payoff outcomes dominate**: Nearly all modeling and theory papers focus on non-payoff behavioral outcomes (e.g., cooperation rates, norm adherence) rather than efficiency or earnings.
- **Game design parameter coverage is incomplete**: Many predictive dimensions (e.g., chat, default_contrib, show_punishment_id) are unaddressed or at best tangentially discussed without modeling their role in payoff outcomes.
- **Theoretical bias**: Heavy reliance on theoretical and normative arguments may distort the expected direction or magnitude of effects in real experimental or practical settings.
- **Generalizability is uncertain**: Insights from models of common-pool resources, legal-normative NRM, or evolutionary cultural theory may not transfer cleanly to canonical PGG experimental settings.
- **No quantitative guidance for downstream prediction**: The set cannot support calibration or credible estimation of the efficiency impact of enabling punishment, conditional on game design features or control efficiency.

**Overall**, the literature reviewed here provides theoretical and indirect modeling support for the expectation that peer punishment improves group cooperation and potentially efficiency, but cannot inform quantitative prediction of efficiency outcomes for specified public goods game designs. Modelers must look elsewhere for direct empirical or summed statistical guidance on treatment-level efficiency.
