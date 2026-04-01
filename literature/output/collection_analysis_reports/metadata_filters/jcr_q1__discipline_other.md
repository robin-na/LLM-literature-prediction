# 1) Evidence Base

The supplied paper set is broad and multidisciplinary, with a mix of laboratory experimental studies and a substantial number of theoretical, modeling, and conceptual works. Roughly 12–15 of the 51 papers are empirical (mainly lab or field experiments); the rest are theory, simulation, or conceptual analysis rooted in evolutionary game theory, philosophy, or institutional economics. Most of the empirical papers focus on public goods games (PGG) or directly adjacent settings; the theory papers range from precise models of PGG and its variants to adjacent dilemmas (e.g., prisoner's dilemma, threshold games, trust games, coordination games) and conceptual discussions of punishment and cooperation in broader social or evolutionary contexts.

There is a reasonable spread of focus across the 14 game design dimensions, but the coverage is uneven (see section 6 below). The evidence base is strongest for standard linear/repeated PGGs with or without punishment and is complemented by meta-level syntheses and mechanism-focused theory. Several papers also link lab findings to field or policy contexts (e.g., fisheries, governance, climate agreements) or discuss the implications for real-world cooperation dilemmas.

# 2) Task Relevance

**pgg_or_variant:**  
- *Exact relevance*: Numerous empirical and theoretical papers focus directly on standard or repeated public goods games (Grechenig et al., 2010; Vasconcelos et al., 2022; Eisenberg & Engel, 2014; Kraak, 2011; Rosas, 2008, Frey & Rusch, 2012).
- *Close relevance*: Some papers examine PGG variants (spatial PGGs, threshold games, coordination games, trust games), which are structurally similar but not identical to the target environment.
- *Adjacent/Weak relevance*: Papers grounded in related social dilemmas (Prisoner's Dilemma, Ultimatum, networked games, principal-agent) offer indirect insights.
- *None*: A minority address only loosely related settings.

**punishment_or_sanctions:**  
- *Exact relevance*: Many papers examine peer or institutional punishment directly, often manipulating punishment availability, cost, or modality (Grechenig et al., 2010; Eisenberg & Engel, 2014; Vasconcelos et al., 2022).
- *Close/Adjacent*: Some focus on broader sanctions (exclusion, rewards, third-party, tax-based), or punishment mechanisms analogous but not identical to peer punishment in standard PGGs (Zhu et al., 2020; Brick & Visser, 2010; Liu et al., 2019).

**efficiency_or_related_payoff_outcome:**  
- *Exact relevance*: Several studies report efficiency as a primary outcome or in equivalent payoff terms (total group welfare/earnings, group payoff; Grechenig et al., 2010; Frey & Rusch, 2012; Eisenberg & Engel, 2014).
- *Close relevance*: Others report adjacent outcomes (group achievement in threshold games, compliance, average earnings, stabilization of group payoffs).
- *Adjacent/Weak*: Many discuss non-payoff outcomes—contribution rates, cooperation, norm compliance—though these are important behavioral correlates, they are not efficiency.
- *None*: Efficiency or group payoff is not measured or discussed at all in some conceptual or philosophical papers.

**Summary:** Overall, the evidence base is reasonably strong for standard PGGs with peer punishment and efficiency outcomes, but a significant portion of the literature is theoretical, or discusses adjacent settings and behavioral outcomes rather than the precise efficiency metric used for downstream prediction.

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes (Direct/Efficiency):**
- Efficiency (group payoff as share of maximum possible): Directly measured in multiple papers (Grechenig et al., 2010; Eisenberg & Engel, 2014; Frey & Rusch, 2012; Vasconcelos et al., 2022).
- Total earnings, welfare, surplus, average group payoff: Reported in empirical and theoretical work, often as proxies or directly equivalent to efficiency.
- Achievement of group targets (threshold games, emission targets): Treated as a close proxy for efficiency in some contexts (Brick & Visser, 2010; Vasconcelos et al., 2013).

**Non-Payoff Behavioral Outcomes:**
- Contribution rate/cooperation density: Most common outcome in simulation/theory papers (Quan et al., 2023; Zhu et al., 2020; Steimanis et al., 2020; Bell et al., 2016).
- Punishment (frequency, severity, type), reward rates, norm compliance: Frequently reported in both experiments and modeling studies.
- Reputation status, rate of norm violations, conditional cooperation: Used to track mechanisms rather than group payoffs.

**Distinction Noted:**  
Many papers explicitly measure and report only behavioral outcomes (e.g., cooperation rate), with efficiency inferred as a secondary or implied effect. Only a subset report group payoff/efficiency directly as per the strict prediction target.

# 4) Main Findings Relevant To Prediction

**Empirical findings:**
- **Punishment can increase efficiency, but only under some conditions.** When information about others’ behavior is accurate and punishment is well-calibrated, enabling peer punishment often increases group efficiency relative to control (Grechenig et al., 2010; Eisenberg & Engel, 2014).
- **Punishment can reduce efficiency when misapplied.** If information is noisy, punishment is persistent but misdirected, leading to efficiency loss below the no-punishment baseline (Grechenig et al., 2010). High transparency can reduce cooperation—and thus efficiency—contrary to standard deterrence logic (Engel, 2019).
- **Severity, likelihood, and nature of punishment are critical.** Sufficiently severe or certain punishment (e.g., treble/class-action damages, or automatic tax/fine sanctions) is more effective at sustaining high payoffs (Eisenberg & Engel, 2014; Brick & Visser, 2010). Actual experience of being punished, not just threat, drives behavior.
- **Longer repeated interaction increases the probability that punishment will pay off in efficiency.** Short games often see punishment remain inefficient, but in longer games efficiency with punishment can surpass baseline due to declining punishment over time as cooperation stabilizes (Frey & Rusch, 2012).
- **Group structure matters**: Stable, fixed groups favor efficient use of punishment; stranger-matching or highly dynamic populations reduce the benefit (Frey & Rusch, 2012; Vasconcelos et al., 2022).
- **Punishment mechanism type matters**: Exclusion-based or reputation-based punishment can be more efficient and stable than direct, costly peer punishment (Rosas, 2008; Liu et al., 2019).

**Theoretical/simulation findings:**
- **Punishment is most reliably efficient when well-aligned with group structure and the public good ‘scale’** (Vasconcelos et al., 2022).
- **Inefficient punishment (e.g., overpunishing, antisocial punishment, high cost per deduction) can erode group payoff despite high cooperation rates** (Rosas, 2008; Quan et al., 2023).
- **Institutional context and adoption matter**: Collective choice of punishment institutions, memory, and information structure (allowing learning) are key for positive efficiency effects (Vasconcelos et al., 2022).

**Behavioral findings (not efficiency outcomes but relevant mechanisms):**
- **Punishment generally increases cooperation/contribution rates**, especially when peer-driven, transparent, or context-sensitive, though this does not always map to increased efficiency due to punishment costs (Kraak, 2011; Brick & Visser, 2010; Bell et al., 2016).
- **Crowding out and polarization effects**: Punishment or sanctioning can crowd out extra voluntary contributions above a minimum, or polarize group behavior where contribution is all-or-nothing (Brick & Visser, 2010; Bell et al., 2016).

# 5) Prediction Guidance

- **Use control (no-punishment) efficiency as the baseline.** When predicting the effect of enabling punishment, adjust expectations depending on several key moderators:
    - **Information accuracy about contributions:** If players have accurate, round-by-round information about who contributed what, punishment is more likely to increase efficiency (Grechenig et al., 2010). If information is noisy or ambiguous, punishment can actually decrease efficiency.
    - **Game repetition (num_rounds), group stability, and time-horizon:** In longer games or with fixed groups, efficiency gains from punishment are more likely as groups settle into high cooperation and punishment costs decline (Frey & Rusch, 2012).
    - **Punishment cost and magnitude:** Lower cost and higher impact punishment (higher fine/cost ratio) correlates with greater efficiency, but only to the point that it does not promote antisocial or excessive punishment (Eisenberg & Engel, 2014; Rosas, 2008).
    - **Punishment mechanism and technology:** Exclusion-based or reputation-based punishment leads to more stable and higher efficiency compared to direct, costly peer punishment—when such mechanisms are available as options (Rosas, 2008; Liu et al., 2019).
    - **Communication and reputation features:** Allowing chat or reputation tracking alongside punishment typically boosts efficiency further (Kraak, 2011; Vasconcelos et al., 2022, adjacent evidence).
    - **Feedback/transparency:** The effect of showing others' contributions and punishment (show_other_summaries, show_punishment_id) is context-dependent and can backfire if precisely individualized (Engel, 2019).

- **Non-linear and conditional effects:** The effect size of punishment depends not just on its presence, but on its coherence and calibration with other design elements (severity, probability, alignment with group or public good structure, reputation mechanisms).

- **Beware reliance on non-payoff outcomes:** Many models and papers report increase in cooperation as a mechanism, but not all increases in cooperation rates translate to increased efficiency due to punishment transaction costs, antisocial punishment, or informational failures.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- **player_count:** Frequently manipulated or discussed; group size moderates punishment effectiveness, with smaller/mid-sized groups favoring peer punishment (Grechenig et al., 2010; Vasconcelos et al., 2022; Kraak, 2011).
- **num_rounds:** Time horizon is a critical moderator—longer repeated interactions allow punishment to pay off; this dimension is directly supported (Frey & Rusch, 2012; Bicchieri et al., 2004).
- **chat (communication):** Several papers empirically test or discuss communication (Kraak, 2011; Bell et al., 2016; Grechenig et al., 2010).
- **mpcr (marginal per capita return):** Directly manipulated; higher MPCR increases baseline cooperation and can moderate punishment effects (Eisenberg & Engel, 2014; Kraak, 2011).
- **punishment_cost, punishment_tech:** Heavily studied; costliness and method (direct, exclusion, reputation, peer vs. pool) are key design levers (Eisenberg & Engel, 2014; Rosas, 2008; Liu et al., 2019).
- **all_or_nothing:** Discussed in both threshold and linear contributions; implications for punishment effectiveness are addressed (Brick & Visser, 2010).
- **show_other_summaries, show_punishment_id:** Information feedback/transparency is an important moderator (Grechenig et al., 2010; Engel, 2019).
- **reward_exists/reward_cost/reward_tech:** Some adjacent papers discuss interplay of punishment and rewards but empirical support is limited (Raihani & Aitken, 2011; Kraak, 2011; Montoya et al., 2015).

**Indirectly Informed or Contextual Only:**
- **default_contrib:** Framing is mentioned obliquely but not empirically tested in the context of punishment.
- **show_n_rounds:** Not heavily featured except as a background variable, except in a few theory papers.

**Effectively Missing:**
- No evidence directly addresses the effect of 'default_contrib' (opt-in/opt-out framing) or systematically manipulates 'show_n_rounds' (though game length is manipulated, information about it is not foregrounded as a treatment).

# 7) Important Limitations

- **Sparse coverage of some key dimensions:** Some design aspects—framing, reward mechanisms, punishment/reward combinations, or default contribute/keep settings—are seldom empirically tested in conjunction with punishment and efficiency outcomes.
- **Limited studies measuring efficiency directly:** Many papers, especially theoretical or simulation work, measure only cooperation or contribution rates. Often, efficiency is inferred rather than explicitly measured.
- **Ambiguity and context sensitivity:** There is strong evidence that punishment *can* increase efficiency, but only under certain conditions—accurate information, calibrated punishment, long time horizons, etc. Under noisy information or misaligned incentives, punishment reduces efficiency. Some empirical and theoretical findings are in tension.
- **Extrapolation risks:** Many findings are based on simplified settings (theoretical, evolutionary, or small-N lab games) which may not generalize to larger groups, field settings, or high-complexity environments.
- **Gaps in real-world mapping:** Few studies test all dimensions together or in realistic, policy-relevant environments with both peer and institutional punishments, rewards, and varying communication, so multidimensional predictions may require extrapolation across partial results.
- **Behavioral/psychological nuance missing from efficiency models:** Some effects (e.g., emotional responses, antisocial punishment, reputation manipulation) introduce variance not easily captured by design parameters.

---

**Summary Judgment:**  
The literature is robust in mapping the main contours for how design features and baseline efficiency moderate the treatment effect of enabling peer punishment in PGG-like environments. However, predictions should account for the strong conditionality of these effects on information structure, punishment calibration, group stability, communication, and game length. Predictions for settings with unfamiliar combinations of features, or for rarely-manipulated dimensions, should be treated with caution. Non-payoff behavioral outcomes should not be substituted for efficiency unless efficiency is directly measured or robustly inferred.
