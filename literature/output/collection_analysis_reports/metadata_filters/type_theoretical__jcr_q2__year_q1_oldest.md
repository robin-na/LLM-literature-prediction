# 1) Evidence Base

The evidence base consists of **theory-focused** papers, with a strong emphasis on mathematical modeling, agent-based simulations, and conceptual analyses. There is very limited direct experimental or empirical data in the set. However, the theory papers comprehensively address both standard and variant forms of public goods games (PGGs), as well as adjacent social dilemmas (e.g., repeated prisoner’s dilemma, common pool resource (CPR) games, and others). The breadth for the specific **prediction task of treatment efficiency in peer punishment-enabled PGGs** is moderate: many papers directly model classic or spatial PGGs with costly punishment, but a substantial subset deals with adjacent mechanisms or settings (prisoner's dilemma, exclusion, monitoring, peer rewards, group selection), providing contextually relevant but less direct evidence. Most outcome measures are theoretical group payoff, welfare, or related efficiency statistics—though notably, many studies report on behavioral outcomes (e.g., cooperation rates, strategy frequencies) instead of payoff or efficiency.

# 2) Task Relevance

- **pgg_or_variant**: The relevance is **high**, with a large subset of the literature modeling classic or spatial PGGs directly (`exact`). Many remaining studies are in adjacent repeated games or other social dilemmas (`close` or `adjacent`), with a few focused on related but non-identical settings (family, market, organizational, partner-control, etc.).

- **punishment_or_sanctions**: Coverage is also **high**. Most theory papers model costly punishment or sanctioning explicitly (`exact`), including variants (peer, pool, adaptive, targeted, institutional). Some examine reward mechanisms as a comparison, or contextual sanctions (social control, exclusion, boycotts).

- **efficiency_or_related_payoff_outcome**: This dimension is **well-covered but less cleanly**. A significant number of papers report payoff- or efficiency-based outcomes (`exact` or `close`), including average group payoff, surplus, or welfare. However, many studies substitute behavioral outcomes (contribution rate, cooperation rate, punishment frequency), which are not identical to efficiency (this is called out explicitly below).

**Summary:** There is a rich theoretical treatment of PGGs with punishment and payoff outcomes, but many key results on efficiency are inferred from cooperation or norm compliance outcomes. The coverage for *predicting treatment efficiency* is as strong as possible with a mostly theory-based literature.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes** (group payoff, average earnings, efficiency, welfare): About half of the directly relevant PGG+punishment studies report these explicitly (e.g., *Zhuang et al., 2012*; *Wang et al., 2010*; *Dejong et al., 2008*; *Congleton & Vanberg, 2001*).
- **Behavioral outcomes** (contribution rate, cooperation prevalence, defection frequency, strategy adoption): Many papers, especially on spatial or structured games, report primarily behavioral outcomes rather than payoffs (e.g., *Perc & Szolnoki, 2012*; *Helbing et al., 2010*; *Gao et al., 2012*).
- **Indirect or contextual outcomes**: Some models focus on evolutionary stability, frequency of norm compliance, or trait prevalence, rarely translating these directly into group payoff or efficiency terms.

**Distinction:** The distinction is generally clear. Prediction tasks requiring actual efficiency outcomes must rely mainly on studies reporting direct payoff or explicit efficiency measures (not solely on increased cooperation or reduced defection).

# 4) Main Findings Relevant To Prediction

**Synthesis of Core Empirical and Theoretical Patterns:**

- **Punishment in PGGs increases efficiency when control efficiency is low.** Strong theoretical consensus exists that enabling (effective) peer punishment in classic PGGs raises average group payoff and efficiency relative to the no-punishment baseline—especially where control efficiency is low due to prevalent defection (*Wang et al., 2010*; *Dejong et al., 2008*; *Sigmund et al., 2011*; *Congleton & Vanberg, 2001*; *Noailly et al., 2009, 2007*).

- **Strength and cost of punishment matter.** Efficiency gains are largest when the punishment is both impactful on defectors and not prohibitively costly to punishers (*Gardner & West, 2004*; *Dejong et al., 2008*; *Hwang & Bowles, 2012*). Overly costly or weak punishment can reduce or even reverse efficiency gains (*Sethi & Somanathan, 2003*; *Helbing et al., 2010*).

- **Population structure and group size moderate effects.** Structured populations, spatial settings, or smaller groups generally show larger efficiency gains from punishment compared to well-mixed or large populations where execution and targeting of punishment is harder (*POLLOCK, 1988*; *Noailly et al., 2009*; *Zhuang et al., 2012*).

- **Punishment can be less efficient than reward.** In models that compare both interventions directly, reward mechanisms may, for a given cost, lead to higher efficiency than punishment—especially at low MPCR (*Zhuang et al., 2012*). However, punishment is often more robust at stabilizing high-contribution equilibria.

- **Punishment efficacy is not monotonic and can backfire or show threshold effects.** Some studies highlight non-linear or path-dependent effects; e.g., punishment can collapse efficiency if too severe, too lenient, or poorly targeted (the "control catastrophe": *Whitmeyer, 2004*; non-monotonicity: *Helbing et al., 2010*; *Orr, 2001*).

- **Social preference, composition, and voluntary participation moderate effects.** In highly altruistic groups, the effect of punishment may diminish or even reduce efficiency because altruistic individuals forgo punishment, weakening deterrence (*Hwang & Bowles, 2012*). Voluntary participation increases the positive impact of punishment on efficiency (*Sigmund et al., 2011*; *Xia et al., 2011*).

- **Adjacent and institutional punishments:** In coercive, asymmetric, or institutional designs, punishment may reduce overall efficiency due to costs imposed on subjects without compensating group gains (*Isakov & Rand, 2012*).

- **Exit, monitoring, and network features:** The availability of exit, monitoring structure, and repeated interactions can all moderate the efficiency impact, sometimes crucially (*Congleton & Vanberg, 2001*; *Haag & Lagunoff, 2006*).

# 5) Prediction Guidance

Based on the reviewed literature, **the introduction of (effective, not overly costly) peer punishment into a PGG is predicted to increase efficiency compared to a control with punishment disabled, with the following caveats:**

- The **magnitude** of efficiency improvement depends on the control’s baseline (lower control efficiency → larger gains from punishment; if control efficiency is already high, punishment may not raise it further and may reduce average payoffs if cost is high).
- **Game design dimensions** that are directly supported in the theory (see next section) should be weighted: strong, low-cost, well-targeted, and salient punishment in small, repeated groups, with possible information sharing, is especially effective.
- **Effect moderators** identified in the literature (and thus, prediction features to focus on): player count/group size, number of rounds, MPCR, punishment cost and magnitude, punishment targeting structure (peer, pool, second-order), network or spatial structure, voluntary participation/exclusion, and possibly default contribution framing.
- **Warning:** If punishment is enabled in settings with high altruism and weak reciprocity, or where group composition or monitoring is poor (e.g., large, anonymous, non-structured groups), efficiency gains may be minimal, zero, or negative (*Hwang & Bowles, 2012*; *Orr, 2001*; *Isakov & Rand, 2012*).
- **Quantitative calibration:** Where payoff effects are reported, models often provide explicit equilibrium outcomes or closed-form predictions that can be used for model calibration (e.g., *Wang et al., 2010*, *Hwang & Bowles, 2012*, *Sigmund et al., 2011*).

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions** (i.e., modeled explicitly in efficiency predictions):

- `player_count` (frequent, often explicitly modeled)
- `num_rounds` (repeatedness discussed, especially in repeated/finite games)
- `all_or_nothing` (binary vs. continuous contribution structures, often varied)
- `mpcr` (Marginal per-capita return, a primary moderator)
- `punishment_cost` (cost to punishers, a critical variable)
- `punishment_tech` (targeting: peer, pool, adaptive, second-order, etc.)
- `show_other_summaries` and `show_n_rounds` (sometimes modeled as information structure)
- (To a lesser but meaningful extent) `default_contrib` (sometimes varied, e.g., opt-in vs. opt-out framing)
- Contextual evidence for: `reward_exists`, `reward_cost`, `reward_tech`, in cases comparing reward and punishment.

**Indirectly informed / Contextually discussed:**

- `chat` (discussed in some models as communication or voluntary participation affecting efficiency, but usually not operationalized in formal models)
- `show_punishment_id` (discussed in terms of anonymity or identity effects, but rarely a model parameter)

**Effectively missing / absent:**

- Simultaneous manipulation of all dimensions is rare; most models alter only a subset.
- Dimensions like `reward_magnitude`, `show_punishment_id`, and detailed chat modalities are sparsely or never explicitly parameterized in models of efficiency outcomes.

# 7) Important Limitations

- **Empirical vacuum:** Most results are from theory and simulation; there is a near-total absence of experimental or observational empirical estimates of treatment efficiency with/without punishment. Model realism and external validity are uncertain.
- **Payoff–behavior mapping:** Many findings infer efficiency gains from increased cooperation/contribution or reduced defections, but the actual net payoff can be ambiguous if punishment is expensive—behavioral improvements do not guarantee higher efficiency.
- **Unmodeled moderators:** Real-world features—complex social preferences, communication (chat), reputation, identity, and long/unknown time horizons—are often absent from models but could critically influence actual efficiency.
- **Boundary conditions and negative effects underexplored:** Several papers explicitly warn that punishment can reduce efficiency in high-altruism or high-cost settings (*Hwang & Bowles, 2012*; *Orr, 2001*; *Isakov & Rand, 2012*)—real-world prediction requires close attention to these moderators, but empirical quantification is lacking.
- **Limited coverage of reward and alternative interventions:** Direct comparative evidence between reward and punishment is relatively rare, and other mechanisms (exit, monitoring, exclusion, network adaptation) are sometimes confounded.
- **Design dimension gaps:** Chat, reward magnitude, identity revelation, and some information structure variables are under- or un-modeled for efficiency outcomes.
- **Lack of group composition data:** The effect of player preferences, type composition (e.g., proportion of reciprocators/altruists), and cultural factors is theorized but not empirically grounded.

---

**Conclusion:**  
The literature delivers a strong theoretical endorsement that adding peer punishment to standard PGGs generally increases efficiency—conditional on details of cost, targeting, group structure, and baseline efficiency. Predictions should focus greatest weight on metrics and dimensions directly modeled: player count, round number, MPCR, punishment cost/tech—while treating evidence inferred from behavioral outcomes with caution and maintaining skepticism about generalization in settings where key moderators (group composition, altruism levels, communication) are unknown or unmodeled. The largest substantive limitation is reliance on theoretical rather than empirical effect validation.
