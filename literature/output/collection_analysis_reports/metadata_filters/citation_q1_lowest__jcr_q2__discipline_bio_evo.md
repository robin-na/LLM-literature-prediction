# 1) Evidence Base

The six-paper set spans both theory and empirical studies, with heavy emphasis on laboratory experiments (four papers), one observational field study, and one theoretical/review work. The evidence is generally broad in its treatment of punishment and cooperation mechanisms, but narrow in directly quantitative, payoff-based outcomes related to efficiency changes from enabling punishment in standard public-goods-game (PGG) settings. Only one paper—dos Santos et al. (2014)—directly reports on efficiency or group payoff as an outcome in a peer punishment context; most papers focus on behavioral, neural, or psychological mechanisms underlying punishment, cooperation, or norm compliance. Several studies utilize adjacent or variant game designs rather than canonical linear PGGs, and only a minority systematically manipulate game design dimensions relevant for predictive modeling.

# 2) Task Relevance

### pgg_or_variant

- **exact**: Two papers (Levy, 2022; Li et al., 2018) deal with canonical or linear PGGs.
- **close/adjacent**: Remaining papers use close variants (prisoner’s dilemma, Mini Ultimatum Game, reputation-based helping/punishment games, or naturalistic shoal-based dilemmas).
- **none**: None are wholly irrelevant, but for some the linkage to standard PGGs is loose.

### punishment_or_sanctions

- **exact**: Four papers explicitly study punishment or sanction mechanisms (Levy, 2022; Chen et al., 2019; dos Santos et al., 2014; Güney & Newell, 2013).
- **close**: One field study discusses punishment-like behavior (Cisarovsky et al., 2012), though not in formal games.
- **none**: One paper (Li et al., 2018) does not involve any punishment.

### efficiency_or_related_payoff_outcome

- **exact**: Only dos Santos et al. (2014) reports efficiency or direct payoff consequences in a punishment-enabled context.
- **adjacent**: Levy (2022) reviews payoff effects but without direct new evidence; the rest focus on non-payoff behaviors or contextual correlates.
- **none**: Several papers (Li et al., 2018; Chen et al., 2019; Güney & Newell, 2013; Cisarovsky et al., 2012) do not report efficiency/group payoff outcomes.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:**  
    - Group efficiency and mean payoff are *directly measured* only in dos Santos et al. (2014) (exact).
    - Levy (2022) reviews evidence for payoff effects but does not offer new empirical efficiency data.
- **Non-payoff behavioral outcomes:**  
    - Most studies measure norm beliefs (Li et al., 2018), punishment assigned (Chen et al., 2019; Güney & Newell, 2013), cooperation/contribution rates, antisocial/prosocial punishment, or spatial patterns of punishment (Cisarovsky et al., 2012).
    - No direct measurement of group payoff or efficiency in these studies—these outcomes may have implicit links to efficiency but are *not equivalent*.

# 4) Main Findings Relevant To Prediction

## Empirical evidence (payoff-based)
- **Punishment does not guarantee higher efficiency**: dos Santos et al. (2014) show that enabling punishment does not necessarily improve group efficiency; efficiency gains can be negated by cognitive load or misdirected punishment (e.g., antisocial punishment).
    - *Under cognitive disturbance*, both payoff and positive punishment effects are weakened or disappear.
    - **Interpretation:** The presence of punishment mechanisms may only increase efficiency if punishment is selectively prosocial and if cognition is not compromised.

## Theoretical and review arguments
- **Punishment can improve efficiency under certain conditions**: Levy (2022) summarizes literature indicating that punishment mechanisms often—but not always—increase average group profit and efficiency, particularly when punishment is not prohibitively costly and retaliation is minimized.
    - Notes *boundary conditions*: Costliness of punishment, risk of antisocial punishment or retaliation, and the institutional or cognitive setting may all set limits on positive efficiency effects.

## Non-payoff, behavioral outcomes
- **Punishment behavior and its drivers**: Other studies (Chen et al., 2019; Güney & Newell, 2013) demonstrate that cooperation and punishment are variable and can be modulated by psychological or neural mechanisms, fairness perceptions, spatial structuring, or reputational cues—but without demonstrating how these translate to efficiency outcomes.

# 5) Prediction Guidance

The literature implies that *enabling punishment* in public-goods-game-like environments may—but does not always—improve group efficiency. In particular:
- **Control efficiency is not a reliable floor:** Even with high baseline (control) efficiency, adding punishment can lower efficiency if punishment is misdirected (antisocial) or if cognitive/informational disturbances are present.
- **Context and dimension effects matter:** Cognitive load and environmental detail (superfluous information) can disrupt the efficiency gains typically associated with punishment (dos Santos et al., 2014).
- **No simple, unconditional uplift:** There is little empirical support in this paper set for assuming a universally positive or reliably quantifiable efficiency boost when enabling punishment, even when controlling for game design dimensions. 
- **Predictive modeling should remain agnostic:** Given the limited direct evidence and pattern of context sensitivity, predictions should allow for null, positive, or even negative changes in efficiency when punishment is enabled, with strong dependence on contextual and dimension-level factors such as fairness framing, cognitive demands, and clarity of punishment targets.

# 6) Design Dimensions Highlighted Across Papers

- **Directly informed:**  
    - *player_count*, *num_rounds*, *chat*, *all_or_nothing*, *mpcr*, *punishment_cost*  
      (covered in various empirical and theoretical papers; all with non-payoff, and only dos Santos et al. (2014) reporting payoff outcomes).
    - *punishment_tech*, *show_punishment_id* (theory and review, Levy, 2022; behavioral, Güney & Newell, 2013).
- **Indirectly/contextually discussed:**  
    - *show_n_rounds*, *show_other_summaries* (mentioned in protocols or control variables, with little reported effect).
    - *spatial structure* (field context only, Cisarovsky et al., 2012).
- **Effectively missing or sparse:**  
    - *default_contrib*, *reward_exists*, *reward_cost*, *reward_tech*, *show_punishment_id* (beyond brief mention, not systematically studied for payoff effects in this set).
- **Summary:**  
   Most design dimensions are addressed at a behavioral or theoretical level, but only *punishment_cost*, *player_count*, *num_rounds*, and *mpcr* receive even partial payoff-based attention, and only in specific contexts.

# 7) Important Limitations

- **Sparse direct efficiency data:** Only one paper systematically reports changes in group efficiency with punishment enabled, and finds effects are context-sensitive and sometimes null or negative (dos Santos et al., 2014).
- **Dominance of non-payoff outcomes:** Most studies focus on mechanisms, norm beliefs, and punishment behaviors without mapping these to overall group payoffs or efficiency.
- **Generalizability concerns:** Several studies use non-standard or adjacent game designs (e.g., Mini Ultimatum Game, reputation-based games, natural field settings), which may limit transferability of findings to canonical PGGs.
- **Limited dimension-specific quantification:** Almost none of the key prediction dimensions (out of 14) have been systematically manipulated and linked to quantitative efficiency outcomes.
- **No quantitative effect sizes:** No studies provide direct, parameterized treatment/control efficiency uplift attributable to punishment under varying design features.
- **Context sensitivity:** Findings suggest strong dependence of efficiency effects on emotional, cognitive, or environmental context—none of which are fully captured by the supplied design dimensions.
- **Ambiguity in boundary conditions:** Both positive and negative (or null) effects of punishment on efficiency are reported or theorized, with few agreed-upon generalities.

---

**In summary**, the literature set’s primary value for the prediction task lies in highlighting the *conditional* and *context-sensitive* nature of punishment’s effects on efficiency in public goods games, with only sparse empirical payoff data to guide quantitative prediction. Most design dimensions are only weakly or indirectly linked to efficiency-based outcomes, and the effect of punishment should be treated as ambiguous and highly context-dependent in evidence-based forecasting.
