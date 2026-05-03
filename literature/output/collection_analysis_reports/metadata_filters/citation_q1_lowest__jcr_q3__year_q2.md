# 1) Evidence Base

The paper set comprises a mixture of experimental (emphatically fewer in number) and primarily theoretical papers. Empirical studies (notably Zhosan & Gardner, 2013; Hsu, 2013; Myers, 2016) use controlled laboratory experiments with public-goods or group-dilemma frameworks, reporting both behavioral and payoff-related outcomes. Theoretical contributions constitute the majority, employing models adjacent or close to the public goods game (PGG) paradigm—with varying degrees of abstraction—to provide mechanistic insights into the effects of punishment/sanctioning and related institutions. This theoretical work is broad in mechanisms discussed (including coordinated punishment, exclusion, social pressure, network knowledge, etc.) but often less specific in mapping findings to standard PGGs or their exact parameterizations. The evidence base is thus moderate-to-broad in its coverage of mechanisms but thin in direct experimental evidence narrowly focused on PGG efficiency effects of punishment.

# 2) Task Relevance

### a) `pgg_or_variant`
- **exact**: Few papers (Zhosan & Gardner, 2013; Hsu, 2013) use laboratory experiments with PGG-like or close variant designs.
- **close**: Some theory papers (e.g., Antoci & Zarri, 2015; Olcina & Calabuig, 2015) model environments structurally close to PGGs (team trust games, repeated contribution dilemmas), while many others use adjacent frameworks (repeated prisoner's dilemma, resource-sharing, networked games).
- **adjacent/weak/none**: Most papers offer only analogical or mechanistic transferability to PGGs rather than direct implementation.

### b) `punishment_or_sanctions`
- **exact/close**: Most papers directly address peer punishment, coordinated sanctions, exclusion, or social/psychological punishment (e.g., Antoci & Zarri, 2015; Olcina & Calabuig, 2015; Furuzono et al., 2013; Povey, 2014).
- **adjacent**: Several papers discuss related mechanisms (institutional tagging, linkage, reciprocity rules) that facilitate punishment or norm enforcement.
- **none**: Few papers omit punishment altogether (e.g., Sthel et al., 2013).

### c) `efficiency_or_related_payoff_outcome`
- **exact**: Direct empirical measures of efficiency (group payoff vs. social optimum) are rare but present (Zhosan & Gardner, 2013; some theoretical papers).
- **close/adjacent/weak**: Many papers focus on related outcomes (average earnings, sustainability, welfare, maximum yield, system convergence) or discuss efficiency in terms of theoretical conditions without reporting numerical group payoff.
- **none**: A subset of the literature confines itself to behavioral outcomes (cooperation rates, compliance, participation) without efficiency reporting or theorizes without a defined group payoff concept.

# 3) Outcomes Measured In The Literature

- **Payoff-related Outcomes**: 
    - *Efficiency* (group payoff relative to social optimum) is directly measured in some empirical (Zhosan & Gardner, 2013) and theoretical work (Olcina & Calabuig, 2015; Antoci & Zarri, 2015).
    - *Earnings, welfare, surplus, or system profitability* are reported or theorized in some studies (Hsu, 2013; Povey, 2014; Laclau & Tomala, 2017).
- **Non-payoff Behavioral Outcomes**:
    - *Contribution rates, cooperation/compliance*, *frequency of cheating/participation*, and *network behavioral adaptation* are the focus in most theory work and some experiments (Myers, 2016; Christoforou et al., 2013).
    - Psychological/social mechanisms (social pressure, group selection, tagging, linkage strategies) are frequently analyzed as mediators of cooperation rather than as direct determinants of efficiency.
- **Explicit Distinction**: Only a fraction of the literature tracks both efficiency/payoff and cooperation, and often the link between the two is mediated by game structure or institutional context.

# 4) Main Findings Relevant To Prediction

- **Punishment Generally Increases Efficiency, But Not In All Circumstances**  
    - Experimental evidence (Zhosan & Gardner, 2013) indicates communication dramatically increases efficiency, with sanctioning mechanisms (warnings/monetary penalties) providing further, though usually smaller, incremental efficiency gains.
    - Theoretical models agree punishment *can* sustain high efficiency if institutional parameters align (low enough punishment cost, high enough effectiveness, strong peer pressure) (Olcina & Calabuig, 2015).
    - However, the effect is highly contingent: theory papers emphasize that punishment's efficiency impact is fragile if punishers are few, punishment targets are ambiguous, monitoring is weak, or second-order free-riding is neglected (Antoci & Zarri, 2015; Laclau & Tomala, 2017).
    - Some models warn that punishment may undermine long-term efficiency by crowding out intrinsic cooperation or shifting behaviors in unexpected equilibrium directions (Povey, 2014; Pin & Rogers, 2015).
- **Behavioral Outcomes Do Not Guarantee Payoff Gains**  
    - Laboratory findings show punishment reliably increases compliance, participation, or contribution, but these do not always translate into efficiency gains (Hsu, 2013; Myers, 2016).
    - Where punishment is costly or increases inefficient behavior (e.g., costly over-participation), group payoff may not improve and may even decrease (Myers, 2016).
- **Contextual Moderators are Critical**  
    - The presence of communication, the observability of actions, the network/information structure, and the effectiveness of monitoring all moderate how much, or even whether, punishment increases efficiency (Zhosan & Gardner, 2013; Larson, 2016; Inaba et al., 2016).
    - Models show that peer pressure, coordinated punishment, low punishment cost, or highly effective sanction mechanisms are often prerequisites for robust efficiency gains.

# 5) Prediction Guidance

- **Direct Empirical Basis Exists, But is Sparse**  
  Only limited direct empirical work allows mapping from control efficiency to expected post-punishment efficiency conditional on design parameters, notably Zhosan & Gardner (2013).  
- **Institutional Features Matter:**
    - Enabling *communication* and/or *punishment* is expected to increase efficiency, but communication's effect is larger and more robust.
    - Adding punishment to a setting that already allows communication leads to further, but smaller, efficiency improvements (Zhosan & Gardner, 2013).
- **Design Dimensions Must Be Considered:**  
  Model-based findings suggest that, for reliable efficiency gains:
    - *Punishment cost* should be low relative to its effectiveness.
    - *Monitoring* and observability must be strong for punishment to have sustained positive effects (Laclau & Tomala, 2017; Inaba et al., 2016).
    - *Peer pressure* and the potential for *coordinated punishment* (as opposed to purely individual sanctions) substantially increase the likelihood that punishment will have a strong positive efficiency effect (Olcina & Calabuig, 2015).
    - *Information structure* (network knowledge, visibility of others' actions) is an important moderator (Larson, 2016).
- **Pitfalls and Negative Effects:**
    - Where punishment costs outweigh cooperative benefits, or when punishment is misdirected (e.g., at non-punishing cooperators), efficiency can decline (Antoci & Zarri, 2015).
    - In settings with costly participation that doesn't contribute to value creation, punishment may increase group costs relative to benefits (Myers, 2016).
- **Ambiguity and Caution:**
    - When only non-payoff behavioral outcomes are reported, one cannot confidently infer efficiency gains.
    - Evidence supports a positive average effect of introducing punishment on efficiency, but only when key conditions (cost, efficacy, observability, peer support) are satisfied.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- `player_count`, `num_rounds`, `all_or_nothing`, `mpcr`, `punishment_cost`, `punishment_tech`: Frequently specified in both theory and experiment, directly linked to group structure, returns to cooperation, and sanction effectiveness (Zhosan & Gardner, 2013; Olcina & Calabuig, 2015; Antoci & Zarri, 2015).
- `chat`: Studied explicitly (Zhosan & Gardner, 2013; Larson, 2016), with communication robustly increasing efficiency even before punishment.
- `show_n_rounds`, `show_other_summaries`: Some treatments manipulate these features, primarily in theory papers addressing monitoring/observability (Laclau & Tomala, 2017; Inaba et al., 2016).

**Indirectly Informed or Contextually Discussed:**
- `default_contrib`: Framing is rarely specified; most models assume voluntary contribution.
- `reward_exists`, `reward_cost`, `reward_tech`: Sometimes included in extension models (Antoci & Zarri, 2015; Christoforou et al., 2013; Garay et al., 2014), though less consistently linked to efficiency predictions.
- `show_punishment_id`: Occasionally considered in modeling peer/psychological effects or retaliation (Povey, 2014).

**Effectively Missing:**
- Detailed operationalizations or empirical analyses of `reward_exists`, `reward_cost`, `reward_tech` are rare.
- Specifics on how the display of information about others’ actions and punishment identities moderate impact are typically only theorized or contextually discussed, not tested directly.

# 7) Important Limitations

- **Sparse Direct Empirical Data:**  
  Direct observation of efficiency changes due to enabling peer punishment in well-specified PGG environments is limited. Most evidence is theoretical or based on variants/adjacent designs, not standard PGGs.
- **Payoff vs. Behavioral Outcomes:**  
  Many studies report only behavioral outcomes (e.g., cooperation, compliance), not group payoffs or efficiency, limiting their value for predicting efficiency effects.
- **Contextual Dependence & Fragility:**  
  Theory uniformly stresses that the positive effect of punishment on efficiency is highly context-dependent—dependent on cost structures, monitoring, group size, and more. Results may not generalize to all parameter regimes, especially with high punishment cost, poor monitoring, or weak peer support.
- **Missing or Underexplored Dimensions:**  
  Several design dimensions relevant to prediction (e.g., detailed info provision, framing, reward mechanisms) are insufficiently addressed empirically across this literature.
- **Ambiguity Where Designs Depart from Standard PGGs:**  
  Results drawn from prisoner's dilemma, resource management, exclusion/linkage, or psychological/social-pressure models may not transfer quantitatively to PGG settings with continuous contribution and defined marginal per-capita return.
- **Longitudinal and Equilibrium Effects Less Understood:**  
  Some models highlight potentially negative long-term effects of punishment on intrinsic cooperation, but empirical evidence on this dynamic is lacking.

---

**References use only paper summaries:**  
- Zhosan & Gardner, 2013  
- Hsu, 2013  
- Antoci & Zarri, 2015  
- Laclau & Tomala, 2017  
- Olcina & Calabuig, 2015  
- Povey, 2014  
- Larson, 2016  
- Myers, 2016  
- Christoforou et al., 2013  
- Andrews & Davidson, 2013  
- Syi, 2014  
- Furuzono et al., 2013  
- Pin & Rogers, 2015  
- Inaba et al., 2016  
- Ghachem, 2016  
- Garay et al., 2014  
- Sthel et al., 2013
