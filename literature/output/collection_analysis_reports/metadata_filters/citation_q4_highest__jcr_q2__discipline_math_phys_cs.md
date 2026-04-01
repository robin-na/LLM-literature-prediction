# 1) Evidence Base

The literature set is **narrow** in methodological modality, being composed entirely of *theoretical* (analytical and/or simulation-based) studies; there are no empirical or laboratory experiments or real-world data. All papers use models (usually of evolutionary game dynamics) to analyze public goods games (PGGs), closely related multiplayer dilemmas, or sometimes more distantly related settings (e.g., spatial PDGs, common-pool resource games). Nearly all outcomes are reported as stationary or equilibrium *strategy fractions* or *dynamical phases*; only a subset of papers directly measure or report payoff-based efficiency outcomes.

The literature is **broad** in terms of model variants, considering a variety of population structures (well-mixed, spatial/lattice, networked, multi-level/community structure), sanctioning regimes (peer, institutional, adaptive, probabilistic, and sometimes reward as well as punishment), and game design manipulations. The focus is predominantly on *mechanisms* and their consequences for cooperation and, less frequently, efficiency.

# 2) Task Relevance

**pgg_or_variant**

- *Exact relevance*: A substantial majority of papers directly model the classic public goods game or spatial/networked variants (e.g., Perc, 2016; Chen et al., 2014; Helbing et al., 2010; Perc & Szolnoki, 2012; Wang et al., 2021; Szolnoki & Perc, 2016; Szolnoki & Chen, 2018).
- *Close to adjacent relevance*: A minority model adjacent settings (N-person snowdrift, spatial PDG, common-pool resource with feedback), which are structurally similar but not canonical PGGs (Yan et al., 2021; Wardil & da Silva, 2009; Sui et al., 2015).
- *None*: No studies in this set are entirely irrelevant structurally; all model social dilemmas.

**punishment_or_sanctions**

- *Exact relevance*: Multiple papers explicitly implement peer or institutional punishment and systematically vary punishment cost/severity (Perc, 2016; Chen et al., 2014; Helbing et al., 2010; Wang et al., 2021; Perc & Szolnoki, 2012; Wang et al., 2011; Szolnoki & Perc, 2012; Yan et al., 2021; Henrich & Henrich, 2006).
- *Close to adjacent relevance*: Several model reward, tolerance/abstention, or reputation as alternative or indirect forms of sanction (Szolnoki & Perc, 2016; Gao et al., 2010; Dong et al., 2019).
- *None*: Some omit sanctions entirely, focusing on structure or learning (Rong & Wu, 2009; Sui et al., 2015; Szolnoki & Chen, 2018).

**efficiency_or_related_payoff_outcome**

- *Exact relevance*: Only a handful directly analyze efficiency, welfare, or group payoff as a primary outcome (Szolnoki & Perc, 2016; Szolnoki & Chen, 2018; Yan et al., 2021), or report results that can be interpreted straightforwardly as group efficiency (Szolnoki & Perc, 2012).
- *Close relevance*: Many provide equilibrium payoff formulas or analyze cumulative costs, but focus on behavioral outcomes (cooperation rates or phase transitions) as proxies (Perc, 2016; Chen et al., 2014; Wang et al., 2021; Helbing et al., 2010).
- *Adjacent to weak relevance*: Several mention payoff but do not report efficiency, or only provide individual- or node-level payoff distributions.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes (efficiency, welfare, total payoff):**
- *Directly reported/measured*: 
    - Efficiency interpreted as defector-free, fully cooperative states (Szolnoki & Perc, 2016; Szolnoki & Chen, 2018).
    - Group payoff/resource level as explicit model variables (Yan et al., 2021).
    - Cumulative cost of incentives, with links to net group payoff (Wang et al., 2021).
- *Theoretical payoff expressions, but not primary outcome*: 
    - Some papers provide payoff calculations or formulas as part of their phase analysis, but only report on strategy prevalence (Chen et al., 2014; Perc, 2016).
- *Not measured*: 
    - Most papers focus on the behavioral or strategic equilibrium, not explicit efficiency.

**Behavioral (non-payoff) outcomes:**
- Frequency of cooperation, prevalence of strategies, phases of strategy mix.
- Emergence/persistence of punishment, reward, or norm adherence.
- Effects of network structure or updating rules on cooperation rate.

**Explicit distinction maintained:** Only a small subset directly measure or report efficiency as defined by group payoff relative to the full-cooperation benchmark. Most leverage cooperation rate as a *proxy*, but guide that this is not always equivalent to efficiency due to sanction costs.

# 4) Main Findings Relevant To Prediction

- **Punishment generally promotes cooperation and, potentially, higher efficiency:**
    - Several models show that introducing punishment can transform parameter regions dominated by defection into ones of high or even full cooperation (Perc & Szolnoki, 2012; Szolnoki & Perc, 2012; Chen et al., 2014; Perc, 2016; Helbing et al., 2010).

- **Cost and mode of punishment critically moderate efficiency effects:**
    - Punishment only increases efficiency if its *cost* does not outweigh the gains from increased cooperation (Szolnoki & Perc, 2012; Wang et al., 2021). **Adaptive or probabilistic punishment** can reduce total sanctioning costs while maintaining high cooperation, thus maximizing net efficiency (Perc & Szolnoki, 2012; Chen et al., 2014).
    - Overly severe or expensive punishment can lead to lower cooperation or to cycles that reduce payoff (Helbing et al., 2010; Chen et al., 2014).

- **Game/environmental structure modulates punishment's effect:**
    - *Spatially structured* or *networked* populations allow targeted, context-sensitive punishment to efficiently eliminate defectors, reducing sanction costs and improving group efficiency compared to well-mixed populations (Perc, 2016; Szolnoki & Perc, 2012).
    - In *common-pool resource games*, institutional punishment promotes both cooperation and sustainability, but only if the probability × severity is high enough—otherwise, efficiency gains are not achieved (Yan et al., 2021).

- **Initial conditions and parameter sensitivity:**
    - The baseline level of cooperation when punishment is off (i.e., control efficiency) determines whether punishment or reward is more cost-effective (Wang et al., 2021).
    - Synergy factor (MPCR), group size, and cost/penalty ratios appear in phase boundaries for high-efficiency regimes (Perc, 2016; Szolnoki & Perc, 2012).

- **Alternative mechanisms:**
    - Conditional tolerance, adaptive rewarding, reputation-based incentives, or structure/learning diversity can, in some cases, achieve similar efficiency gains to explicit punishment (Szolnoki & Perc, 2016; Szolnoki & Chen, 2018; Dong et al., 2019).
    - Reward alone is less efficient than punishment in achieving high-efficiency equilibria (Szolnoki & Perc, 2012; Szolnoki & Perc, 2010).

# 5) Prediction Guidance

Given this literature base, **efficiency under punishment is likely to exceed efficiency in punishment-disabled controls when:**
- Sanction costs are not too high relative to the benefit of increased cooperation (Szolnoki & Perc, 2012; Wang et al., 2021).
- The punishment regime is adaptive, targeted, or probabilistically shared to minimize wasted costs (Perc & Szolnoki, 2012; Chen et al., 2014).
- The underlying environment (MPCR, group size, population structure) supports the feasibility of cooperation once defectors are suppressed (Perc, 2016).

For **prediction from game dimensions:**
- **MPCR (synergy factor)**, **punishment cost**, **punishment severity/technology**, and **game structure** (spatial vs. well-mixed, network degree) are the dimensions most directly tied to the efficiency outcome under punishment.
- **If control efficiency is already high** (i.e., cooperation is prevalent without sanctions), the *incremental gain from enabling punishment* is likely marginal, and net efficiency may even *decline* due to sanctioning costs (Wang et al., 2021).
- **If control efficiency is low** (defection dominates), *enabling punishment* can substantially raise efficiency, but only if cost-effective punishment is feasible.
- **Punishment cost and adaptiveness of implementation** are critical: high sanction costs can negate the efficiency gains from increased cooperation.
- **Threshold effects**: Many models indicate non-linear or phase-transition-like effects of punishment parameters, suggesting that moderate increases in cost or decreases in punishment effectiveness can sharply reduce gains in efficiency (Helbing et al., 2010; Yan et al., 2021).

Because most studies **do not** report precise quantitative effects on efficiency, predictions must often be inferred *indirectly* from reported cooperation rates, the prevalence of defector-free states, and, when provided, net payoff formulas that account for sanctioning costs.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informative Dimensions:**
- `player_count`: Manipulated and theorized in nearly all models.
- `num_rounds`: Present as either explicit round counts or as implicit evolutionary timescales.
- `mpcr`: Specifically parameterized, especially as the synergy factor.
- `punishment_cost`: Explicitly examined in nearly all punishment models.
- `punishment_tech` (e.g., severity/effectiveness): Central in most, including discussion of fine magnitude, adaptiveness, and probability/targeting.
- `reward_exists`, `reward_cost`, `reward_tech`: Discussed in those that consider the reward alternative.
- `all_or_nothing`: Modeled as discrete or continuous play in many.
- `player_count`, `network structure`: Feature prominently in models varying spatial, networked, or community structure.

**Indirectly/Contextually Discussed:**
- `chat`, `default_contrib`, `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Rarely, if ever, manipulated. Some models incorporate feedback about others' actions (`show_other_summaries`), but this is not a focus.
- `default_contrib`: Only informally mapped as framing in a minority of papers.
- `show_n_rounds`: Information about game length is not typically varied.

**Missing or Only Contextual:**
- Dimensions related to explicit interface/framing (e.g., chat, opt-in vs. opt-out framing, visibility of punishers), which are common in behavioral experiments, are generally *absent* from this set of theory papers.

# 7) Important Limitations

- **Lack of direct efficiency measurement**: Most papers analyze cooperation rate, not group efficiency (payoff normalized to the cooperative optimum), and often do not subtract sanctioning costs—meaning net efficiency may be overstated if inferred solely from increased cooperation.
- **No empirical data**: All findings are theoretical or simulated; generalizability to lab or field settings is untested within this set.
- **Structural scope**: Papers focus mostly on spatial/networked populations or adaptive mechanisms, which may not generalize to standard lab PGGs (well-mixed, anonymous).
- **Parameter sparsity**: Some design dimensions relevant to applied prediction (e.g., communication, framing effects) are unaddressed or only contextually discussed.
- **Assumption sensitivity**: Many key results depend on evolutionary dynamics, update rules, or spatial locality—parameter sweeps in one modeling tradition may not map quantitatively to others.
- **Ambiguity in non-linear effects**: Several findings emphasize non-monotonic or threshold effects (e.g., too severe punishment, or highly clustered networks can backfire), but the critical parameters are not always consistently specified across models.
- **Mapping behavioral to payoff outcomes is indirect**: Most predictions about efficiency must be inferred from cooperation rates and theoretical cost accounting, not observed or directly reported efficiency data.

---

**Summary:**  
This literature set provides a robust theoretical basis for why and how enabling punishment can increase efficiency in PGG-like environments—primarily when punishment is cost-effective, adaptive, and when baseline efficiency is low. The predictions regarding the magnitude and conditions of efficiency improvement are indirect, inferred from models of cooperation dynamics, with direct efficiency outcomes reported only in a subset of papers. Many dimensions central to behavioral PGG experiments are under-addressed, making transfer to applied environments less precise. Quantitative prediction should be cautious, leveraging phase diagrams and documented threshold effects where available, but recognizing that direct efficiency data are sparse.
