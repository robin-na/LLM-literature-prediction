# 1) Evidence Base

This literature set comprises 33 papers, all theory-focused, including formal models, conceptual frameworks, reviews, and theory-driven literature syntheses. There are **no empirical or experimental studies** directly measuring efficiency effects of punishment across game designs. The theoretical scope is **broad with respect to mechanisms and environments** (repeated games, reputation, monitoring, cultural evolution, contracts), but **narrowly focused on payoff and efficiency in only a subset of the set**. While many papers discuss public goods games (PGGs) or variants, a significant fraction analyze Prisoner's Dilemma (PD), common pool resource (CPR), or partnership games, which are adjacent but not identical to the canonical PGG. Theoretical findings are often precise regarding mechanisms, equilibrium conditions, and comparative statics, and many offer **explicit predictions or parametric results relating efficiency to key design features**. However, evidence for numerical or real-world effect sizes, or direct generalization to all design dimensions in experimental PGGs, is **limited**.

# 2) Task Relevance

**a) `pgg_or_variant`:**
- **Exact**: Several core theory papers specifically model canonical PGGs and analyze peer punishment and efficiency (e.g., Wolitzky, 2013; Fehr & Schmidt, 1999; Carpenter et al., 2004).
- **Close/Adjacent**: Many papers focus on partnership, repeated PD, CPR, or networked PD games, which share strategic structure but differ in matching, group size, or contribution structure (e.g., Ali & Miller, 2016; Kandori, 1992; Ellison, 1994; Sethi & Somanathan, 2003).
- **None**: A minority do not address PGGs or any direct analog.

**b) `punishment_or_sanctions`:**
- **Exact**: Core PGG papers analyze peer punishment (both empirical-motivated and theoretical frameworks).
- **Close/Adjacent**: Some explore ostracism, third-party/community enforcement, monitoring, exclusion, or informal sanctions (e.g., MacLeod, 2007; Bowles & Gintis, 2004).
- **Weak/None**: A few only address social pressure or non-punitive mechanisms; some provide only background.

**c) `efficiency_or_related_payoff_outcome`:**
- **Exact**: Key theory papers provide explicit results relating peer punishment to group efficiency or total payoff (e.g., Wolitzky, 2013; Fehr & Schmidt, 1999).
- **Close/Adjacent**: Many discuss mechanisms supporting cooperation or norm compliance, with implications for efficiency but not always reporting payoff-based outcomes directly.
- **Weak/None**: Several papers limit findings to contribution rates, behavioral mechanisms, or non-payoff group efficacy.

**Summary:**  
The **most directly relevant evidence** is theoretical, from papers exactly addressing PGGs with peer punishment and quantifying group efficiency. A significant remainder make **close or adjacent arguments**, often in variants (repeated PD, CPRs, networks), adding mechanistic richness but complicating precise mapping to the PGG context or payoff measures.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes** (relevant for prediction):
    - *Efficiency* (ratio of actual to full-cooperation group payoff)
    - *Total group payoff/earnings/welfare* (often directly modeled)
    - *Surplus/coins generated* (only sometimes reported)
- **Behavioral or Non-Payoff Outcomes**:
    - Contribution or cooperation rates (frequently discussed)
    - Punishment or sanctioning frequency
    - Norm compliance, ostracism, and reputation dynamics
    - Social/psychological motivations for punishment (reciprocity, fairness, status)
    - Social network characteristics, population composition (e.g., proportion of reciprocators or punishers)
- **Distinction**:  
Most theory papers addressing efficiency also discuss cooperation rates. However, several (including reviews and psychological/evolutionary models) focus almost exclusively on *behavioral outcomes* or reasons for punishment and only infer implications for efficiency.

# 4) Main Findings Relevant To Prediction

**Empirical-theoretical consensus in the core PGG and close-variant theory:**
- **Peer punishment opportunities substantially increase efficiency** in repeated PGGs, often to near-optimal levels, provided certain conditions are met: (a) punishment is not excessively costly, (b) players can monitor/identify others' actions, and (c) a sufficient fraction of players are "enforcers" (Wolitzky, 2013; Fehr & Schmidt, 1999; Kandori, 1992; ABREU et al., 1991).
- **Quantitative predictions/formulas** are sometimes offered, giving the maximum sustainable efficiency as a function of group size (`player_count`), marginal per-capita return (`mpcr`), punishment cost, monitoring structure (`punishment_tech`), and information transmission (Wolitzky, 2013; Fehr & Schmidt, 1999).
- **Moderators and limits**:
    - **Imperfect monitoring/noise**: Lower efficiency unless patience is high (ABREU et al., 1991; Levine & Pesendorfer, 2007).
    - **Punishment cost**: Higher punishment cost reduces the impact and stability of efficient cooperation (Sethi & Somanathan, 2003; Fehr & Schmidt, 1999).
    - **Antisocial punishment**: In environments with high antisocial punishment (punishment of cooperators), group efficiency may even decrease when punishment is allowed (Sylwester et al., 2013).
    - **Forgiveness and temporary sanctioning**: Permanent exclusion can be less effective than temporary, forgiving punishment (Ali & Miller, 2016).
    - **Information structure**: Efficiency gains depend crucially on the ability of players to observe and identify defectors (`show_punishment_id`, `show_other_summaries`) (Kandori, 1992; Levine & Pesendorfer, 2007).
    - **Population composition/group size**: Larger group size can undermine cooperation unless there is assortative matching or sufficient monitoring/reputation (Wolitzky, 2013; Kandori, 1992).
- **Non-payoff findings** (contextual modifiers):  
    - Communication (`chat`) consistently increases cooperation and, by extension, efficiency in narratives (Ostrom, 2000), but few give explicit payoff estimates.
    - Social norms, reciprocity, psychological motivation, and reputation are *necessary for punishment to support efficiency* but are not sufficient if institutional design is unfavorable (Carpenter et al., 2004; Falk & Fischbacher, 2006; Ostrom, 2000).

**Points of ambiguity/contingency:**
- In some models, **punishment can lower efficiency** if too widespread, poorly targeted, or costly (Sethi & Somanathan, 2003; Anderies et al., 2011; Festré, 2010).
- Contexts with **antisocial punishment** or weak legal/trust institutions can see *reduced* efficiency from peer punishment (Sylwester et al., 2013).
- Efficiency gains may *depend on initial conditions, group norms, or the learning process* (Chassang, 2010).

# 5) Prediction Guidance

**For predicting treatment (with-punishment) efficiency from design dimensions and control efficiency:**
- The literature **strongly supports** the expectation that, in canonical PGGs, **enabling peer punishment will increase group efficiency compared to punishment-disabled controls**, holding other dimensions constant, provided at least moderate monitoring and norm enforcement are possible.
- **Key design moderators** (as most supported by theoretical literature):
    - Lower `punishment_cost` and higher `mpcr` → larger efficiency gain from punishment (Fehr & Schmidt, 1999).
    - High `player_count` and low `mpcr` → efficiency gain is smaller; monitoring and social structure become more crucial (Wolitzky, 2013).
    - Effective punishment requires *information transmission*; e.g., `show_other_summaries` and `show_punishment_id` features are strongly positive moderators (Kandori, 1992; Levine & Pesendorfer, 2007).
    - If *punishment is "antisocial", non-credible, or enables retaliation*, efficiency gains may be null or negative (Sylwester et al., 2013).
    - Temporary/forgiving sanctions outperform permanent ostracism for efficiency (Ali & Miller, 2016).
- **In cases where punishment is extremely costly or information is poor**, efficiency gains are attenuated or absent.
- **Where empirical guidance is lacking,** the best practice is to assume that enabling peer punishment will *raise efficiency close to the theoretical maximum sustainable with the given group size, mpcr, and punishment effectiveness*, unless there is a strong contextual reason (e.g., antisocial punishment, high cost, very large group, lack of observability) to moderate this expectation.
- When only non-payoff behavioral evidence is available for certain dimensions, map reported increases in cooperation or norm compliance to a **bounded, but potentially incomplete, increase in efficiency**; do not treat increased cooperation as isomorphic with maximized payoff.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed** (theoretical/empirical linkage to efficiency with punishment):
- `player_count`: Widely analyzed for its effect on sustainability of efficiency gains from punishment.
- `num_rounds`: Relevant in repeated-game analyses.
- `mpcr`: Critical parameter in all canonical PGG theory; effects on incentives and punishment returns are explicit.
- `all_or_nothing`: Modeled in some theory; relevant to the cooperation threshold and effect size.
- `punishment_cost`: Central to predictions about the magnitude and stability of efficiency gains.
- `punishment_tech`: Several papers explicitly model monitoring/technology for punishment or community enforcement.
- `show_other_summaries`, `show_punishment_id`: Key in models of monitoring, reputation, and identification; explicitly linked to efficiency effects.
- `reward_exists`: Occasionally modeled as an alternative/complement (Wolitzky, 2013; MacLeod, 2007).

**Indirectly informed/context-discussed**:
- `chat`: Communication is frequently mentioned as beneficial but usually linked to behavioral rather than payoff effects.
- `default_contrib`: Rarely addressed directly; effect on punishment's impact on efficiency usually inferred, not modeled.
- `reward_cost`, `reward_tech`: Discussed in the context of alternatives to punishment, but not as primary efficiency moderators.
- `show_n_rounds`: Occasionally included; effect on behavior and possibly patience, but rarely isolated in efficiency outcomes.

**Effectively missing**:
- Empirical data to parameterize predictions for any of the 14 dimensions.
- Interaction/moderator effects among design features (e.g., chat × punishment or reward × punishment) are not addressed with quantitative precision.
- `punishment_magnitude`, `reward_magnitude`: Not discussed explicitly; usually subsumed under cost/effectiveness parameters.

# 7) Important Limitations

- **No empirical or quantitative experimental evidence**: All findings are theoretical or conceptual. There are no parameterized, data-driven effect sizes for the efficiency impact of punishment in specific game designs.
- **Adjacency and context dependence**: Many results are derived for close variants (e.g., repeated PD, community enforcement models) and require careful mapping to PGGs. There is ambiguity about direct generalizability to large-group or one-shot contexts.
- **Limited attention to some prediction dimensions**: Several features (e.g., `default_contrib`, `punishment_magnitude`, or full communication protocols) are circumstantially discussed or omitted.
- **Ambiguity in edge cases**: Predicted efficiency gains may turn negative or ambiguous in presence of antisocial punishment, high punishment cost, weak monitoring, or large group size (as per Sylwester et al., 2013; Sethi & Somanathan, 2003).
- **Behavioral outcome dominance**: Many papers report on cooperation or norm adherence rates, without direct or quantitative mapping to total group efficiency.
- **Complex mechanisms not always operationalizable**: Theories involving evolution, learning, and social norms may specify necessary conditions for efficiency, but lack direct correspondences to experimental design features/formats.

---

**In summary:**  
The literature **strongly and directly supports the positive effect of enabling peer punishment on efficiency in standard repeated PGGs, contingent on reasonable punishment cost and monitoring capacity**, with explicit theoretical predictions for several key design dimensions. However, absence of empirical quantification, ambiguous mapping in adjacent models, and significant context dependence (especially regarding group size, monitoring, and the potential for antisocial punishment) limit the ability to make high-confidence, fine-grained parametric predictions across all game setups. The predictor should model efficiency increases as driven by punishment's presence, modulated by group size, MPCR, monitoring/information quality, and punishment cost, using theoretical upper bounds for efficiency unless there are strong contrary moderators in the design.
