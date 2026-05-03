# 1) Evidence Base

The paper set is quite broad for the downstream prediction task, encompassing 159 sources with strong coverage of **public goods games (PGGs) and their close variants**, various **punishment and sanctioning mechanisms**, and **payoff/efficiency outcomes**. The majority are **empirical lab experiments** directly manipulating punishment in canonical or near-canonical PGGs, with a substantial supplement of theory/simulation papers, field experiments, and adjacent coordination/common-pool-resource (CPR) games. 

Empirical evidence dominates, with thorough reporting of group efficiency, earnings, welfare, or related payoff outcomes under treatment (punishment enabled) and control (punishment disabled) conditions in standard and modified PGG environments. Several theory papers provide explicit mechanistic predictions or equilibrium characterizations linking design parameters to efficiency.

There is especially **dense evidence** on standard dimensions such as **player count, number of rounds, MPCR, punishment cost/impact, centralization vs. decentralization, information structure, group heterogeneity, and network structure**. Some less conventional game designs (e.g., threshold/step-level, probabilistic punishment, exclusion, communication, endogenous/reward mechanisms) are also included.

However, **adjacent and weakly related papers** are present, especially those focusing on non-payoff behavioral measures, motivational or evolutionary theory, or real-world institutions, which do not always directly report efficiency or payoff outcomes compatible with the prediction target.

# 2) Task Relevance

**pgg_or_variant:**  
- **Exact relevance:** Dominant. The majority of studies are canonical or only minimally modified linear PGGs, with some step-level, threshold, and CPR games (labeled as "close").
- **Close/Adjacent relevance:** CPR games with similar payoff structure, trust games, and some collusion games are included, which are useful but require care in mapping findings to the PGG context.
- **None/Weak:** A small set of studies are outside the PGG domain altogether (e.g., dictator games, non-strategic helping), or focus exclusively on communication/reputation without any availability of punishment.

**punishment_or_sanctions:**  
- **Exact relevance:** Very strong. The majority of highlight papers directly manipulate or compare **punishment-enabled vs. punishment-disabled** PGGs, with detailed attention to the design and implementation of punishment mechanisms (costly, non-costly, centralized/peer, exclusion, probabilistic, legitimacy constraints, etc.).
- **Close/Adjacent:** Several studies focus on reward mechanisms, exclusion as punishment, communication, reputation, or partner selection, which provide indirect evidence about punishment’s effects.
- **Weak/None:** Some context-only or motivation-focused theory papers, and studies with only non-material sanctions.

**efficiency_or_related_payoff_outcome:**  
- **Exact/Close relevance:** Many studies explicitly measure and report **group efficiency, group earnings, total coins, welfare, or closely related payoff-based outcomes**. These are directly relevant for the prediction task.
- **Adjacent/Weak:** A significant number report **only contribution rates, punishment frequency, or cooperation**, often with claims that higher contribution likely implies higher efficiency in linear games—but they do not always provide group payoff or efficiency ratios.
- **None:** Non-strategic or hypothetical vignette studies, and psychological mechanism papers which do not discuss payoffs.

# 3) Outcomes Measured In The Literature

- **Payoff-based outcomes** (directly informed by the literature and critical for prediction):
    - *Efficiency* (group payoff as a proportion of the fully cooperative optimum)
    - Group earnings, total welfare, surplus, total coins generated
    - Average group income or profit (frequent proxy for efficiency)
- **Non-payoff behavioral outcomes** (measured very extensively, but not to be confused with efficiency):
    - Contribution rate, cooperation rate
    - Punishment frequency, anti-social punishment rates
    - Norm compliance, willingness to punish
    - Trust, reciprocity, in-group/out-group effects
    - Compliance with rules/obligations
- *Note:* In many cases, studies directly relate contribution rate and efficiency due to the linear structure of the game—i.e., in these cases, higher average contribution usually maps to higher efficiency, but this is not always guaranteed (e.g., where punishment costs offset gains).

# 4) Main Findings Relevant To Prediction

**General pattern:**  
- **Enabling peer punishment in standard, symmetric, linear repeated PGGs almost always increases efficiency compared to the no-punishment control**, provided that:  
    - Punishment technology is not extremely costly or weak  
    - Anti-social punishment rates are low  
    - The information environment is full and accurate  
    - The group is not highly heterogeneous or normatively conflicted

**Critical moderators of the efficiency effect of punishment:**
- **Cost and effectiveness of punishment:** High-cost or weak punishment mechanisms can yield small or even negative effects on efficiency due to deadweight loss exceeding the gains from increased contribution (Nicklisch et al., 2016; Leibbrandt et al., 2015).
- **Institutional structure:** Centralized and decentralized punishment can both be effective; legitimacy constraints (punishment only by high contributors; full feedback) increase efficiency (Faillo et al., 2013).
- **Anti-social punishment:** Where anti-social punishment (punishing high contributors) is common, efficiency gains are reduced or reversed—this is influenced by the subject pool, social norms, and network structure (Bruhin et al., 2020; Bortolotti et al., 2015).
- **Group heterogeneity:** Efficiency gains from punishment are muted or absent in groups with **heterogeneous endowments or returns**, unless the institutional design accommodates that heterogeneity (Kingsley, 2016; Kube et al., 2015).
- **Punishment network structure:** Asymmetric or incomplete punishment networks reduce the effectiveness of punishment and may decrease efficiency compared to symmetric networks (Boosey & Isaac, 2016; Leibbrandt et al., 2015).
- **Information and monitoring:** Noise, imperfect monitoring, and high judicial error rates reduce or eliminate the efficiency gains from punishment, especially when errors punish cooperators (Markussen et al., 2016; Nicklisch et al., 2016).
- **Cultural and social background:** Cultural context, group composition, and framing can strongly moderate the efficiency effect of punishment; some populations exhibit strong anti-social punishment or resistance to norm enforcement (Bruhin et al., 2020; Kocher et al., 2012).
- **Type of sanction:** Exclusion/ostracism, if costless, can be more effective than costly monetary punishment; costly exclusion does not increase net efficiency (Dannenberg et al., 2020).
- **Reward mechanisms:** In some institutional structures, rewards can increase efficiency even more than punishment, especially if the reward mechanism is designed to be net payoff positive (Gürerk et al., 2009).
- **Communication (chat):** Communication alone can sometimes substitute for punishment as a mechanism for supporting high efficiency; the effect of punishment is weaker when effective communication is possible (Leibbrandt & Sääksvuori, 2012; Engelmann & Nikiforakis, 2015).
- **Design features (e.g., higher-order punishment, social learning, voluntary participation):** Legitimacy, institutional endogeneity, and spillovers from social learning can enhance punishment’s positive impact on efficiency (Gürerk, 2013; Marcin et al., 2019; Engl et al., 2021; Deffains et al., 2019).

**Areas of ambiguity/conflict:**  
- In some environments (especially with strong anti-social punishment, endowment inequalities, or partial monitoring), enabling punishment can **reduce efficiency relative to control**, either by wasted punishment costs or retaliation spirals (Bruhin et al., 2020; Kingsley, 2016; Leibbrandt et al., 2015).
- Centralized/third-party punishment is more effective and less susceptible to anti-social misuse in some contexts, but can fail under high error or lack of legitimacy (Marcin et al., 2019; Markussen et al., 2016).
- Theory and some experiments suggest that **punishment can crowd out intrinsic motivation** and, in high-cooperation contexts, may not increase and can even decrease efficiency if baseline (control) efficiency is already high (van der Weele, 2012).

# 5) Prediction Guidance

**General rule:**  
- In repeated, linear PGGs with **homogeneous players, symmetric actionable punishment, full information, and moderate-to-low punishment cost**, enabling peer punishment can reliably be expected to **increase average efficiency compared to the same game with punishment disabled**, conditional on the control condition’s efficiency.

**Prediction should be moderated by:**
- **Punishment cost and effectiveness**: Prediction of treatment efficiency should incorporate the punishment cost/impact ratio. Net gains require punishment to be effective enough to increase or sustain cooperation at a moderate cost (Gürerk et al., 2018; Nicklisch et al., 2016).
- **Network/punishment structure**: Efficiency gains are highest with complete and symmetric punishment networks; gains are typically absent in asymmetric/incomplete networks (Boosey & Isaac, 2016; Leibbrandt et al., 2015).
- **Heterogeneity**: In groups with unequal endowments/returns, enabling punishment does **not necessarily increase efficiency** and may reduce it (Kingsley, 2016; Kube et al., 2015).
- **Anti-social punishment prevalence**: In contexts or samples with significant anti-social punishment, predicted efficiency gain from enabling punishment should be reduced or possibly set to zero (Bruhin et al., 2020; Bortolotti et al., 2015).
- **Information structure and monitoring**: Under noisy or imperfect monitoring (or high judicial error), effect of punishment on efficiency can be zero or negative (Nicklisch et al., 2016; Markussen et al., 2016).
- **Baseline (control) efficiency**: If control efficiency is already high (close to social optimum, e.g., due to strong social preference or communication), additional efficiency from punishment will be small or negative (van der Weele, 2012; Kocher et al., 2012).
- **Design dimensions**: Features such as chat/communication, higher-order punishment, selective feedback, visibility of punishment, and institutional endogeneity all moderate the direction and size of punishment effects and should be considered.

**Notably**, a prediction based **only on design parameters and control efficiency** is insufficient if information about the above moderators, especially group heterogeneity and anti-social punishment prevalence, is missing—these can swing the effect from positive to negative.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed by the literature:**
- `player_count`, `num_rounds`, `mpcr`: Extensively studied; almost all relevant papers vary or report on these.
- `punishment_cost`, `punishment_tech`: Cost-to-impact ratio, effectiveness, probability/severity, network structure are central to the efficiency effects and are well-documented.
- `all_or_nothing`: Both binary (all-or-nothing) and continuous PGGs are covered, with findings that results are broadly consistent across forms, though binary interactions can increase strategic sensitivity.
- `reward_exists`, `reward_cost`, `reward_tech`: Comparisons to reward and combinations of punish/reward are common.
- `chat`: Several papers examine the effect of chat/communication.
- `show_other_summaries`, `show_n_rounds`, `show_punishment_id`: Variations in feedback, information display, and anonymity are frequently studied and shown to moderate punishment effects.

**Indirectly informed:**
- `default_contrib`: Framing defaults (opt-in vs. opt-out) are less commonly manipulated but appear in some digests.
- `show_punishment_id`: The effect of visible vs. anonymous punishment is covered in select studies and shown to be relevant for anti-social punishment or retaliation.

**Only contextually discussed / sparse:**
- `chat`, `show_n_rounds`, some information feedback variables are often described but not always systematically manipulated.
- Endowment asymmetry, subject pool, and cultural background are mentioned as major moderators, but these are not always operationalized as prediction dimensions.

**Effectively missing:**
- Some dimensions (e.g., higher-order information about others' histories, behavioral type composition in a group, real-world group structure) are only incidentally addressed or not encoded as explicit dimensions, but are shown to matter substantially in explanatory studies.

# 7) Important Limitations

- **Population composition is often unobserved in prediction**: The efficiency impact of punishment is highly sensitive to unmeasured heterogeneity in anti-social punishers, pro-sociality, or cultural context. Many field and lab findings indicate large cross-population variance, which is not always captured by design dimensions (`player_count`, etc.).
- **Behavioral outcomes ≠ efficiency outcomes**: In many empirical studies, contribution rates are reported and discussed, but efficiency is only implied or not directly analyzed. Mechanisms that increase contributions do not always increase efficiency (e.g., when punishment is costly).
- **Contextual fit**: Some highly cited lab experiments use student subjects, artificial stakes, or exclusively Western samples, while field studies or diverse subject pools show systematically different punishment effects, especially due to anti-social punishment.
- **Game variants/generalizability**: The downstream task addresses canonical PGGs (“PGG-like”), but a significant portion of evidence comes from closely related, but not identical, games (e.g., CPR, step-level, trust, contest, collusion games). Care is required in extrapolating quantitative findings.
- **Dimension coverage gaps**: Some prediction-relevant design attributes (e.g., detailed information structures, framing, dynamic adjustments, partner matching) are only partially informed by the literature.
- **Limited guidance for extremal or non-standard parameter settings**: Most findings center on group sizes 3-5, MPCRs between 0.3 and 0.5, punishment cost/impact ratios between 1:2 and 1:4, and up to 20–30 rounds. Extrapolation beyond these (large groups, very costly punishment, very long/short games) is less empirically supported.
- **Potential publication and reporting bias**: As in all social science domains, positive effects of punishment may be overrepresented, and negative/null results underreported.
- **Aggregate predictions may hide subgroup divergence**: For example, average efficiency might rise while certain players or types (e.g., high contributors, minorities) are harmed or unattached.

**In sum**: The literature base for this prediction task is robust, with strong and nuanced support for the general finding that enabling punishment in PGG-like environments can increase efficiency—but only under conditions that avoid high anti-social punishment, costly or ineffective punishment, group heterogeneity, and limited information. Prediction accuracy is highest when the key design and contextual dimensions that moderate the effect of punishment are specified and matched to the evidence base. Ambiguity remains where these context variables are unmeasured or not encoded in the input to prediction.
