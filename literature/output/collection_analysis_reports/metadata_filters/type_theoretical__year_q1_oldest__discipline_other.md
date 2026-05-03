# 1) Evidence Base

The paper set consists entirely of theoretical and conceptual analyses; there are no empirical or experimental studies directly measuring outcomes in public-goods games (PGGs). Several papers synthesize results from laboratory PGGs or evolutionary simulations as part of their argumentation, but the evidence is mainly model-based rather than data-driven.

The coverage is moderate in scope. Most papers are concerned with cooperation, punishment, and related mechanisms in collective action or evolutionary contexts. There is a small but useful set of papers discussing efficiency or payoff outcomes, but much of the evidence concerns cooperation rates, behavioral persistence, or theoretical mechanisms underlying punishment. The set highlights various game design dimensions but rarely provides direct, parameterized guidance for prediction based on empirical data.

# 2) Task Relevance

### `pgg_or_variant`
- **exact**: 3 papers focus explicitly on PGGs or variants (e.g., Rosas, 2008; Frey & Rusch, 2012; Kraak, 2011).
- **close/adjacent**: Most other papers are adjacent, focusing on broader social dilemmas, trust games, or evolutionary analogues.
- **weak/none**: One paper (Clavien, 2012) references PGGs only to illustrate altruism, not as a core subject.

### `punishment_or_sanctions`
- **exact**: 7 papers directly discuss punishment as a mechanism in collective action (including different technologies: direct cost, exclusion, reputation, etc.).
- **adjacent/close**: Several papers discuss reward mechanisms as well or consider sanctions systems more generally.
- **weak/none**: One paper does not discuss punishment at all.

### `efficiency_or_related_payoff_outcome`
- **exact**: 3 papers focus on efficiency or payoff-based outcomes (Rosas, 2008; Frey & Rusch, 2012; Bicchieri et al., 2004).
- **close/adjacent**: 2 papers make indirect arguments about payoff improvements or welfare, but focus on cooperation or evolutionary persistence.
- **none**: The bulk of the set is concerned primarily with behavioral, moral, or evolutionary mechanisms rather than explicit efficiency metrics.

# 3) Outcomes Measured In The Literature

### Payoff-Related Outcomes
- **Group efficiency / total payoff / welfare**: Core outcome in Rosas (2008), Frey & Rusch (2012), Kraak (2011), and partially in Bicchieri et al. (2004).
- **Indirect or conceptual appeals**: Several papers posit that increasing cooperation through punishment will improve efficiency, but do not measure or model it explicitly.

### Non-Payoff Behavioral Outcomes
- **Cooperation/contribution rate**: Central focus in most papers (e.g., evolutionary persistence of altruism, norm compliance, moral order).
- **Punishment frequency/type**: Examined as to its effect on behavioral compliance or the maintenance of cooperation, not on total group payoff.

### Distinction
Most of the literature emphasizes mechanisms (how punishment affects cooperation or norm stability) rather than the net effect on group efficiency or payoff—though improved cooperation is often treated as a proxy for efficiency. Few papers quantify the relationship between design features, punishment, and payoff.

# 4) Main Findings Relevant To Prediction

- **Punishment can increase or decrease efficiency**, depending on design: When punishment is direct and costly, it may reduce efficiency due to resource waste, unless it successfully stabilizes cooperation over time (Rosas, 2008; Frey & Rusch, 2012).
- **Efficiency gains from punishment are contingent** on key design dimensions: Increases are likely with long time horizons, stable groups, and effective punishment (Frey & Rusch, 2012); in short/intermittent games, costly punishment may fail to improve or even lower efficiency due to ongoing punishment expenditures.
- **Punishment technology matters**: Exclusion-based or reputation-based punishment mechanisms tend to be more efficient and less wasteful than direct costly punishment when stabilizing cooperation (Rosas, 2008).
- **Communication and reputation amplify positive effects**: Peer-driven, transparent punishment, especially when combined with chat or reputation mechanisms, leads to more targeted punishment and higher increases in group efficiency (Kraak, 2011).
- **Rewards can supplement or sometimes outperform punishment**, particularly in settings with low baseline cooperation or at early stages (Raihani & Aitken, 2011), but the evidence here is from adjacent outcomes (cooperation rates) rather than payoff or efficiency explicitly.
- **Repeated interaction and time horizon** drive the development of conditional cooperation and, by extension, improvements to efficiency (Bicchieri et al., 2004)—even when explicit punishment is absent, but especially when it is present.
- **Magnitude and cost of punishment**: If punishment is too costly or ineffective (low punishment magnitude per unit cost), the efficiency gains are minimal and can be negative (Frey & Rusch, 2012).
- **Ambiguity** remains: Some theoretical arguments (Nakao & Machery, 2012) caution that punishment may not always improve efficiency, as it sometimes serves functions other than changing behavior for group benefit.

# 5) Prediction Guidance

This literature supports **conditional predictions**:
- **Efficiency is likely to increase** in PGG-like environments when enabling peer punishment—if the control efficiency is low, groups are stable, the number of rounds is high, and punishment is effective and not prohibitively costly (Rosas, 2008; Frey & Rusch, 2012; Kraak, 2011).
- **Efficiency is likely to decrease or not improve** if the game is short, partner groups are not stable (stranger matching), the cost of punishment is high, or the punishment technology is direct and crude, leading to ongoing resource waste (Rosas, 2008; Frey & Rusch, 2012).
- **Design features such as communication and reputation systems** further moderate the effect: their presence typically boosts the positive impact of punishment on efficiency (Kraak, 2011).
- **If the baseline (control) efficiency is already high**, the marginal benefit of enabling punishment may be small, and the added cost could even reduce efficiency. Thus, baseline efficiency is an important predictor.
- **Dimension interactions** matter: e.g., high punishment cost may only depress efficiency if rounds are few or group structure is unstable; over long games, cooperation and thus efficiency may recover as the need for punishment declines.

However, most results are qualitative or model-based, and **few provide quantitative estimates** linking specific design parameters or control efficiency to post-punishment treatment efficiency.

# 6) Design Dimensions Highlighted Across Papers

### Directly Informed by Literature
- **player_count**: Discussed in relation to group effects (Rosas, 2008; Kraak, 2011; Sripada, 2005; Bicchieri et al., 2004).
- **num_rounds**: Strongly highlighted as key moderator (Frey & Rusch, 2012; Bicchieri et al., 2004; Kraak, 2011).
- **punishment_cost**: Directly analyzed (Rosas, 2008; Frey & Rusch, 2012; Kraak, 2011; Woodcock & Heath, 2002).
- **punishment_tech**: Varieties of punishment and their effects (Rosas, 2008; Woodcock & Heath, 2002; Sripada, 2005).
- **chat**: Communication shown to increase cooperation/efficiency when combined with punishment (Kraak, 2011).
- **mpcr**: Addressed as it moderates collective benefit (Kraak, 2011; Bicchieri et al., 2004).
- **reward_exists**: Contextually discussed as an alternative or supplement to punishment (Raihani & Aitken, 2011; Campbell, 1991).

### Indirectly Informed or Contextual
- **all_or_nothing**: Mentioned in modeling context (Kraak, 2011; Bicchieri et al., 2004), secondary to efficiency.
- **default_contrib**: Not directly analyzed, possible indirect relevance via framing (Raihani & Aitken, 2011).
- **show_other_summaries**, **show_punishment_id**: Very limited, contextually discussed as related to transparency/reputation (Kraak, 2011).
- **punishment_magnitude**: Rare explicit treatment, but implied via punishment efficacy.
- **reward_cost**/**reward_tech**: Little direct discussion; covered in terms of existence and conceptual role, not parameterized.

### Effectively Missing
- **Detailed analysis of show_n_rounds**: Only referenced once (Bicchieri et al., 2004).
- **Quantitative interaction of multiple dimensions**: The multidimensional detail present in most prediction tasks is lacking; evidence on interaction effects is qualitative.

# 7) Important Limitations

- **Empirical evidence is limited or absent**: All papers are theoretical or conceptual; none report new experimental data on post-punishment efficiency.
- **Efficiency outcomes are only rarely the primary focus**, with most studies emphasizing cooperation rates or theoretical mechanism stability.
- **Few quantitative, parameterized results**: The set lacks regression models or effect size estimates explicitly linking design dimensions and control efficiency to treatment efficiency.
- **Dimension coverage is uneven**: Player count, number of rounds, punishment cost/tech, and communication are reasonably well addressed, but several key predictors (reward details, framing, visibility features) are only briefly mentioned or not covered.
- **Interaction effects** are not explored empirically, and model-based findings may not map cleanly to real-world or experimental treatments.
- **Ambiguity in direction and magnitude**: While many papers argue that punishment can improve efficiency, several caution about possible efficiency losses under certain conditions, and the literature cautions against simplistic optimism.
- **Adverse selection and extrinsic cost arguments**: Multiple conceptual analyses highlight that adding punishment can sometimes have perverse effects or may not work if intrinsic motivations are undermined (Kraak, 2011; Nakao & Machery, 2012).
- **Contextual and ecological validity**: Some evidence comes from trust-game or animal studies and may not fully generalize to laboratory PGGs with the specific features required for downstream prediction.

---

**Summary:**  
The theoretical literature supports that enabling peer punishment in public-goods-game-like setups can increase efficiency—particularly with sufficient rounds, effective punishment, communication, and low initial cooperation—but the connection is primarily qualitative and indirect. Predictions must adjust for key design parameters, with particular caution on cost, technology, time horizon, and baseline efficiency. The absence of empirical, quantitative evidence and coverage gaps (especially for less-studied game features) means predictions require careful qualification.
