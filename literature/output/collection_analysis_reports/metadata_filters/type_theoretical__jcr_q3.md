# 1) Evidence Base

The paper set provides a very broad and highly detailed theoretical literature base for understanding the efficiency effects of punishment in public-goods-game (PGG)-like environments. The overwhelming majority of papers are **theoretical models**; empirical or experimental findings are almost entirely absent from the set, with most references to empirical work found in the theoretical models' context-setting rather than as primary analyses. All the main findings, comparative statics, and predictions discussed are **based upon theoretical derivations, agent-based simulations, or formal model outcomes** rather than direct laboratory or field data on efficiency effects.

The literature is **broad** in contextual scope, incorporating a wide range of public goods settings (canonical PGGs, volunteer’s dilemmas, trust games, common pool resources, workplace teams, threshold games, institution building, etc.), population structures (well-mixed, spatial, networked, group structured), and enforcement mechanisms (peer punishment, institutional punishment, exclusion, reputation-based sanctioning, group-level sanctions, partner choice, etc.).

However, the set is **narrow** with respect to empirical calibration, as almost none of the studies provide laboratory or field experiment data specifically reporting treatment (punishment-enabled) and control (punishment-disabled) efficiency outcomes under systematically varied game design dimensions.

# 2) Task Relevance

### `pgg_or_variant`
- **exact:** The literature is dominated by papers that model the *canonical linear public goods game* and its close variants (e.g., well-mixed or spatial PGGs, voluntary PGGs, step-threshold PGGs, continuous or all-or-nothing contribution, institution-based sanctions, etc.).
- **close:** A substantial subset expands to adjacent games with analogous social dilemma structures (e.g., trust games, joint effort, team production, mutual aid games).
- **adjacent/weak:** Some papers focus on the repeated Prisoner's Dilemma, trust games, or pairwise games with only conceptual linkage to PGGs.
- **none:** Very few papers are entirely unrelated to public goods or cooperative dilemmas.

### `punishment_or_sanctions`
- **exact:** Nearly all papers with `pgg=exact` or `close` directly analyze costly punishment, exclusion, reward, or coordinated sanctions (either peer- or institutionally-administered).
- **adjacent:** A significant portion look at punishment-like mechanisms (reputation loss, withdrawal of future benefits, ostracism).
- **weak/none:** Only a small number mention punishment as background or focus only on alternative mechanisms (e.g., voluntary participation, partner choice).

### `efficiency_or_related_payoff_outcome`
- **exact/close:** A substantial number of papers analyze *efficiency* or *group payoff* as a primary outcome, giving explicit results on total group earnings, welfare, or normalized payoffs (relative to the full-cooperation benchmark).
- **adjacent:** Many models present only contribution rates, strategy frequencies, equilibrium types, or welfare as a secondary outcome; these require inference to efficiency.
- **weak/none:** Some only discuss behavioral outcomes, such as cooperation rates or punishment frequencies, tracking efficiency outcomes only contextually.
- **Empirical findings at the level of efficiency are sparse to non-existent in this set.** Any references to empirical outcomes are usually found in the theoretical context or model calibration.

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes (Directly Relevant):**
- **Efficiency or normalized group payoff:** Many papers report group earnings as a fraction of the social optimum (where all cooperate every round). Theory papers in particular anchor predictions on whether enabling punishment increases, decreases, or leaves unchanged this ratio.
- **Welfare/surplus/total coins or earnings:** Used as synonyms for group payoff by some models.

**Non-Payoff Behavioral Outcomes (Indirect/Adjacent):**
- **Contribution rate/cooperation rate:** Frequently reported as the frequency or proportion of cooperation in equilibrium but requires explicit mapping to group payoff for prediction tasks.
- **Punishment frequency or assigned punishment:** Some papers focus on how often punishment occurs, who punishes whom, and under what incentive schemes, but do not link this directly to payoffs.
- **Norm compliance or strategy frequency:** Often, equilibrium strategy prevalence is reported (e.g., prevalence of punishers, defectors, or conditional cooperators).

**Distinction:** The **most reliable and direct guidance** for efficiency prediction comes from those papers that explicitly report, analyze, or provide formulas for group efficiency/payoff as a result of enabling punishment, contingent on game design parameters.

# 4) Main Findings Relevant To Prediction

### General Summary
- **Enabling costly punishment in standard PGGs (linear, well-mixed, with sufficient monitoring and sufficiently low cost/effective punishment) raises group efficiency—sometimes dramatically—relative to the control.** This result is highly robust for canonical lab settings (e.g., Fehr & Gächter), as supported by theory calibrated to those experiments (e.g., Dutta et al., Cressman et al., Gintis 2000/2003, Eldakar et al.).
- **The magnitude and even the sign of punishment effects are highly conditional** on specifics of the game design:
    - **Punishment effectiveness and cost:** Low-cost, high-impact punishment (whether peer or institutional) yields larger efficiency gains; if punishment is inefficient (i.e., high cost, low impact), efficiency gains evaporate or reverse (Eldakar et al., Gintis 2000, Wang & Lv 2019).
    - **Presence of antisocial/anti-cooperation punishment:** If defectors can punish cooperators ("antisocial punishment"), efficiency can *decrease or not improve* (Rand et al. 2010, Hauser et al. 2014, Powers et al. 2012, Oya & Ohtsuki 2017).
    - **Structure of punishment (peer vs institutional, pool punishment, exclusion, etc.):** Institutional punishment, exclusionary mechanisms, or well-structured institutional enforcement (with low corruption) are more robust mechanisms for efficiency gains than uncoordinated peer punishment, especially in larger or more complex groups (Prétôt et al. 2024, Lee et al. 2015, Fang et al. 2020, Huang et al. 2018).
    - **Retaliation and counter-punishment:** When retaliation against punishers is possible, efficiency gains are fragile or erased, especially in large groups or when punisher anonymity is not protected (Wolff 2012, Janssen & Bushman 2008).
    - **Population structure:** In spatial, networked, or group-structured populations, the effect of punishment is often contingent; in some settings, punishment only supports efficiency in structured populations, not in well-mixed ones (Oya & Ohtsuki 2017, Wang & Lv 2019, Nakamaru & Dieckmann 2009).
    - **Monitoring/observability:** Imperfect monitoring (e.g., noisy signals, anonymous groups, absence of outcome feedback) reduces or eliminates efficiency gains from enabling punishment because of mistaken or insufficient sanctioning (Bednar 2006, Mihm & Toth 2020, Laclau & Tomala 2017).
    - **Core game parameters (MPCR, player count, rounds, etc.):** Higher marginal per-capita return (MPCR) makes cooperation easier to sustain, so the incremental efficiency gain from punishment may be smaller at high MPCR and larger at low MPCR (Kranz 2010, Hwang 2017). The effect of group size is ambiguous: coordinated punishment can support high efficiency in large groups if appropriate mechanisms are in place, but uncoordinated punishment loses effectiveness as groups grow (Suzuki & Akiyama 2007, Hwang 2017).
    - **Voluntary participation and motivating norms:** Voluntary participation or norm-internalization amplifies the positive effect of punishment on efficiency (De Silva et al. 2010, Gintis 2003), while compulsory participation and norm disagreement reduce or eliminate these gains.
    - **Presence/absence of reward:** Punishment and reward can complement each other; some papers suggest the combination is more effective, or that reward alone is insufficient (Cressman et al. 2012, Milinski & Rockenbach 2012, Jiao et al. 2020).
    - **Monitoring technology:** Public or private visibility of sanctions and punishers changes the effect—if identities are known, efficiency is sometimes lower due to retaliation or norm conflict (Janssen & Bushman 2008, Lee et al. 2015).
    - **Random drift, mutation, and exploration:** High mutation, behavioral experimentation, or random exploration can undermine the stability of cooperation and the gains from punishment, especially if antisocial punishment is feasible (Hauser et al. 2014, Oya & Ohtsuki 2017, Wolff 2012).

**Empirical references** are used in theoretical model calibration, e.g., Dutta et al. (2021) and Gintis (2000, 2003) use Fehr & Gächter’s data, but the model predictions dominate.

**Contextual variation and exceptions** are explicitly noted: in some parameter regimes, enabling punishment can reduce efficiency (e.g., high costs, prevalent antisocial punishment, retaliation, bad enforcement structure, large groups, limited monitoring, or when defection is hard to detect or identify).

# 5) Prediction Guidance

## Mapping from Design Dimensions and Control Efficiency to Treatment Efficiency

Because almost all evidence is theoretical or simulation-based, the guidance for predicting the effect of enabling punishment in a PGG-like environment is **conditional and parameter-dependent**:

- **In standard, well-mixed PGGs without antisocial punishment, with moderate to high MPCR, effective and not-too-costly punishment, and sufficient monitoring, enabling punishment will increase average efficiency—sometimes substantially—relative to the control (no-punishment) baseline.** The expected treatment efficiency approaches or exceeds 80–90% of the optimum in the best-studied theoretical settings (Dutta et al., Gintis, Kranz, Cressman, Eldakar, Wang & Lv).
- **If the control efficiency is already high (e.g., due to high MPCR, reputation, or repeated interaction), the marginal gain from punishment may be small (Han et al., Archetti & Scheuring).**
- **If the punishment technology is weak (low punishment impact, high cost), or monitoring is imperfect, or games are very brief/one-shot**, the effect of punishment is limited or ambiguous (Eldakar et al., Bednar, Mihm & Toth, Nakamaru & Dieckmann).
- **If antisocial punishment is possible, retaliation is easy, or enforcers are corrupt or hard to identify, punishment can reduce efficiency below the control baseline** (Rand et al., Hauser et al., Lee et al. 2015, Oya & Ohtsuki 2017, Powers et al. 2012).
- **The design dimensions with strongest direct support for moderating prediction are:** punishment cost, punishment effectiveness (tech), player count, group size, number of rounds, MPCR, monitoring structure (show_other_summaries, show_n_rounds, show_punishment_id), reward options, and whether multiple enforcement mechanisms coexist (punishment and reward).

## Indirect/Behavioral Outcomes

- If the only data available are behavioral (e.g., contribution rates, strategy frequencies), infer efficiency changes with caution: many models show that increased contribution rates under punishment correlate with higher average payoff, but this is not universal (increased punishment costs or retaliation can offset contribution gains).
- Empirical effect sizes and quantitative mappings are largely unavailable; all predictions must be interpreted as qualitative, with direction and magnitude determined by model fit to relevant design dimensions.

## Application Boundaries

- **Prediction is best for canonical experimental PGGs:** continuous contributions, well-mixed groups, peer punishment enabled as an extra stage, with known punishment cost and effect parameters, and no antisocial punishment or retaliation.
- **Prediction is less reliable or requires major caution** for:
    - Large group sizes (>8–12) unless coordinated/institutional punishment is present.
    - Settings with peer sanctions but possible antisocial punishment or retaliation.
    - Field or group-structured populations with strong migration, heterogeneity, or network complexity, unless supported by models explicitly including those features.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed** (i.e., explicit comparative statics, formulas, or quantitative predictions available):
- `player_count`: group size effects are deeply analyzed and sometimes show non-monotonic effect on efficiency.
- `num_rounds`: longer games, higher continuation probability promote punishment’s effectiveness, but only up to the point that punishment remains credible and impactful.
- `mpcr`: marginal per-capita return is a critical moderator for both baseline efficiency and the marginal effect of punishment.
- `punishment_cost`: universally analyzed; lower cost leads to more effective punishment and higher efficiency.
- `punishment_tech`: effectiveness (fine per cost) is a key determinant.
- `all_or_nothing`: discrete vs. continuous strategies are sometimes modeled (Eldakar et al., Cressman et al., Wang & Lv).
- `reward_exists`, `reward_cost`, `reward_tech`: included in many models showing additive or competitive effects with punishment.
- `punishment_tech`: covers punishment magnitude or efficacy per unit of cost.

**Indirectly informed** (i.e., contextual discussion, but not always with explicit model results):
- `show_other_summaries`, `show_n_rounds`: imperfect or absent monitoring reduces impact of punishment.
- `show_punishment_id`: identifiability of punishers affects retaliation and efficiency, but often not specifically parameterized.
- `chat`: communication is sometimes discussed as a moderator (can substitute for or complement punishment).
- `default_contrib`: discussed as framing (opt-in/opt-out), but rarely as a model parameter.
- `punishment_exists`: presence/absence of punishment is the treatment in question.

**Contextually or minimally discussed or missing:**
- Effects of specific framing choices, such as `default_contrib` (opt-in vs. opt-out), are only mentioned in passing (i.e., contextual).
- `chat` and information feedback dimensions are occasionally contextualized but not deeply parameterized outside information/monitoring structure.
- Few models explicitly analyze variations in `num_rounds`/game length as a standalone moderator apart from continuation probability.
- **Empirical correspondence for these dimensions is especially sparse.**

# 7) Important Limitations

- **No empirical treatment vs. control efficiency data**: Theorized predictions dominate; actual observed efficiency changes upon enabling/disabling punishment are nearly absent outside theoretical calibration.
- **Heavy reliance on theory**: All parameter sweeps and comparative statics come from formal models or agent-based simulation—models assume rational or evolutionary behavior, sometimes omitting learning, bounded rationality, or cultural inertia.
- **Behavioral outcomes vs. efficiency**: Many models use cooperation or punishment rates as proxies for efficiency, requiring careful interpretation of when higher cooperation actually raises payoff net of punishment costs.
- **Strong dependency on parameter regimes**: Most results only hold for moderate punishment cost, high punishment effectiveness, honest enforcement, and low retaliation/antisocial punishment; small parameter changes flip predicted outcomes in some models.
- **Population and network structure effects are complex**: There is ambiguity and sometimes direct contradiction among papers regarding the effects of group size, spatial/network structure, and voluntary participation.
- **Scope of generalization**: Predictions are less certain for field, institutionally complex, or non-canonical PGGs. The literature does not address many ecological or real-world design dimensions with empirical measurement.
- **Scarce guidance on newer or alternative mechanisms**: Innovations such as dynamic linking, flexible opt-out, and multi-level incentives are contextually discussed, but their payoff impact is less well-characterized in comparative predictions.

**In sum**, the literature provides **strong theoretical and mechanistic support** for the direction and conditionality of punishment’s effect on efficiency in PGG-like settings, with explicit dependency on core design dimensions, but **empirical quantitative evidence for prediction is limited**, and predictive confidence attenuates rapidly as game designs depart from canonical well-mixed lab PGGs. Behavioral outcomes must not be conflated with efficiency, and prediction requires careful mapping from design dimensions to the relevant theoretical regime.
