# 1) Evidence Base

The evidence base for this report comprises **46 papers**, overwhelmingly theoretical (game theory, evolutionary modeling) with a minority of empirical work (observational or laboratory experiment). The majority focus on **public goods games (PGGs) or close variants**, with some extending to related social dilemmas (e.g., Prisoner's Dilemma, mutualism, resource games, ultimatum games). The literature provides a **broad theoretical sweep over punishment mechanisms, cooperation strategies, and efficiency impacts** in social dilemma environments.

Empirical evidence is *extremely limited*: almost all efficiency or payoff outcomes are theoretical, with few experimental or field data points. Most models are parameterized in ways that map closely onto standard PGG dimensions, supporting external validity but bringing the usual caveats of theory-driven inference. The literature is broad in its conceptual and mechanistic exploration but is **narrow for empirical, direct, or quantitative prediction of efficiency effects** in real-world or experimental-lab PGGs with varying design dimensions.

# 2) Task Relevance

## a) Public Goods Game (pgg_or_variant)
- **exact**: Many papers model the canonical n-player linear public goods game or close derivations, e.g., (Eldakar et al., 2007; Deng et al., 2012; Wang et al., 2010; Sigmund et al., 2011; Milinski & Rockenbach, 2012; Dejong et al., 2008).
- **close**: A substantial portion extends to spatial PGGs, common pool resource (CPR) games, repeated n-person PD, or group-structured/partner-choice settings.
- **adjacent/weak/none**: Several papers examine Prisoner's Dilemma or other two-player strategic dilemmas, or focus on mechanisms like network rewiring, resource games, or ultimatum games.

## b) Punishment or Sanctions (punishment_or_sanctions)
- **exact**: Core theoretical models implement peer punishment, pool punishment, or both, with analyses of cost-structure and technological parameters.
- **close/adjacent**: Papers addressing indirect, endogenous, or reputation-based sanctions, or those studying partnership selection or conditional cooperation (without explicit costly punishment) populate the adjacent range.
- **weak/none**: Some studies only mention punishment in passing, focusing instead on dynamics without direct sanctioning.

## c) Efficiency or Related Payoff Outcome (efficiency_or_related_payoff_outcome)
- **exact**: A subset directly models and reports efficiency (group payoff relative to full cooperation) as the primary outcome, including explicit comparisons between punishment-enabled and control conditions (Eldakar et al., 2007; Deng et al., 2012; Wang et al., 2010).
- **close**: Others use high-level welfare, mean fitness, aggregate wealth, or mean final payoff.
- **adjacent/weak**: Most focus primarily on **behavioral outcomes** (contribution rate, cooperation frequency, strategy prevalence) and **infer** rather than measure efficiency gains.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:**  
    - **Efficiency (relative to full cooperation):** Directly modeled and reported in a minority of theory papers (Eldakar et al., 2007; Wang et al., 2010), and sometimes as average group payoff, total earnings, or welfare (Deng et al., 2012; Noailly et al., 2009; Sigmund et al., 2011).
    - **Total group payoff, mean fitness, aggregate wealth:** Used interchangeably in some evolutionary models and CPR games.

- **Non-payoff behavioral outcomes:**  
    - **Contribution/cooperation rate, strategy frequencies, norm compliance:** Much of the literature uses these as proxies for efficiency; results must be interpreted with caution when mapping to payoff-based prediction (Gao et al., 2012; de Weerd & Verbrugge, 2011; Vukov et al., 2012).
    - **Punishment frequency and assignment, stability of cooperation, network measures:** Frequently reported but not equivalent to group efficiency.

# 4) Main Findings Relevant To Prediction

**Synthesis across papers yields the following cross-cutting findings for predicting efficiency change due to enabling punishment in PGG-like environments:**

- **Punishment reliably increases efficiency under classic PGG design, provided punishment is not too costly and the game is sufficiently long/repeated** (Eldakar et al., 2007; Dejong et al., 2008; Wang et al., 2010; Sigmund et al., 2011; Milinski & Rockenbach, 2012). The effect holds for both peer and (especially) pool punishment, and is **most robust** when punishment is effective, costs are moderate, and the baseline (no-punishment) efficiency is low.
- **Group size / player_count:** Efficiency gains from punishment are generally **larger in small groups** and **diminish as group size increases** unless punishment is severe or shared (Deng et al., 2012; Eldakar et al., 2007; Noailly et al., 2009). Severe, concerted punishment can restore efficiency in larger groups (Deng et al., 2012).
- **Cost and effectiveness of punishment:** High punishment cost reliably reduces both the prevalence of punishment and its efficiency benefits (Eldakar et al., 2007; Okada & Bingham, 2008; Sigmund et al., 2011). High-impact/low-cost punishment is efficiency-promoting, while high-cost/low-impact or anti-social punishment may negate efficiency gains (Weibull & Salomonsson, 2006; Powers et al., 2012).
- **Punishment structure/technology:** Peer punishment is less robust to second-order free-riding; pool punishment with second-order punishment is more stable and brings higher efficiency, when present (Sigmund et al., 2011; Dejong et al., 2008).
- **Effects of anti-social punishment:** If defectors can punish cooperators (anti-social punishment), the efficiency gains from enabling punishment are greatly reduced or even reversed, especially in larger or less dispersive groups (Powers et al., 2012).
- **Spatial and network structure:** Local/clustered enforcement in spatial PGGs can sustain higher efficiency with punishment than well-mixed populations (Noailly et al., 2009; Nakamaru & Dieckmann, 2009).
- **Temporal structure/num_rounds:** The positive efficiency effect of punishment is stronger in games with multiple rounds or high continuation probability; in very short or one-shot games, punishment’s efficiency benefits are negligible or negative, especially if costly (Leimar, 1997; Eldakar et al., 2007).
- **Punishment is not always efficiency-enhancing:** Some models find that punishment increases norm compliance or cooperation but reduces overall efficiency, especially when punishment is costly and does not trigger synergistic group benefits (Jaffe, 2004; Isakov & Rand, 2012).
- **Synergistic mechanisms:** The **combination of punishment with reward, indirect reciprocity (reputation), or metanorms** (rewarding punishers or punishing non-punishers) further enhances efficiency, reduces the cost of maintaining cooperation, and can expand the parameter space where punishment increases efficiency (Milinski & Rockenbach, 2012; Sigmund et al., 2011; Kendal et al., 2006).

# 5) Prediction Guidance

- **Overall, the literature gives strong theoretical support for the expectation that enabling peer punishment in a PGG will increase average efficiency, especially in repeated games, small groups, and when the punishment cost is moderate and effectiveness is high.**
- The **efficiency boost** from punishment is **modulated by:**  
    - *player_count*: Larger groups generally reduce the positive impact, unless punishment is severe/concerted.
    - *num_rounds*: More repeated rounds support efficiency gains; short games limit them.
    - *punishment_cost*: Lower cost is more favorable; high cost can suppress efficiency or even make it worse than control.
    - *punishment_tech*: Effective punishment (high fine per unit cost) is more effective at increasing efficiency.
    - *mpcr*: Low-mpcr games see greater marginal benefit from punishment (since control efficiency is lower).
    - *anti-social punishment enabled*: If present, efficiency gains may disappear, especially in large groups.
    - *spatial structure*: Local enforcement in networks or spatial games supports efficiency, especially with clustering.
    - *reward_exists*, *reward_tech*, *reputation/indirect reciprocity*: The presence of these features (although less directly modeled) generally amplifies efficiency improvements from punishment (where studied).

- **Ambiguity remains** for parameter regimes with:  
    - Very high punishment cost or low effectiveness,
    - High group size without concerted/shared punishment,
    - Possibility of anti-social punishment,
    - Highly competitive (rather than welfare-dividing) payoff structures,
    - Short games or one-shot interactions.

- **Empirical anchor:** Minimal. Most evidence is theoretical. For designs closely emulating laboratory PGGs, the strongest and most specific guidance will be found in the parameterized theory models (Eldakar et al., 2007; Wang et al., 2010). Evidence from adjacent or unrelated domains should be used only for qualitative context.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- *player_count*: Frequently and directly modeled; essential moderator in almost all exact-relevance models.
- *num_rounds*: Modeled via repeated interactions, continuation probability, or game length; robust modulator of observed effects.
- *mpcr*: Directly parameterized in almost all PGG models.
- *punishment_cost*, *punishment_tech*: Consistently central; direct parameter sweeps and sensitivity analyses exist (e.g., cost-to-impact ratio, concerted vs. peer punishment).
- *punishment_exists*: Core manipulation in all relevant papers.
- *all_or_nothing*: Modeled in some theory papers (discrete vs. continuous contributions), but less central.

**Indirectly Informed / Contextually Discussed:**
- *reward_exists*, *reward_cost*, *reward_tech*: Occasionally included or discussed, primarily as extensions or in metanorm models (e.g., reward punishers).
- *show_other_summaries*, *show_n_rounds*: Sometimes included as info structure; usually peripheral but occasionally shown to moderate reputation, memory, or learning effects.
- *spatial structure*: Modeled in terms of local enforcement, clustering, and network effects.

**Effectively Missing or Minimal Evidence:**
- *chat*: Almost entirely missing; most models assume no communication.
- *default_contrib*: Not modeled; framing and default effects absent from theory literature.
- *showPunishmentId*: Rarely discussed; anonymity often assumed.
- *empirical evidence/realized experimental variation*: Scarce for all design dimensions beyond theory parameterizations.

# 7) Important Limitations

- **Empirical data is almost absent**: Most conclusions rest on theoretical models or simulations. There are virtually no experimental studies reporting efficiency outcomes with variations across all key design dimensions.
- **Behavioral outcomes dominate over efficiency:** Many papers report on cooperation rates, norm compliance, or strategy prevalence, not efficiency. Translating behavioral effects to payoff impacts requires caution and introduces uncertainty.
- **Parameter regime extrapolation:** Theory models often examine broad parameter sweeps (e.g., arbitrary group sizes, costs, rounds) and may not capture the specifics or psychological dynamics of laboratory or field PGGs.
- **Institutional and context features underexplored:** Important design dimensions like communication (chat), default contribution framing, explicit identification of punishers, and real-world social context are underrepresented.
- **Ambiguity in marginal cases:** The literature cautions that punishment can sometimes reduce efficiency (e.g., when anti-social punishment is possible, or costs are high) and this is not always predictable from standard PGG parameters alone.
- **Transfer from adjacent paradigms is uncertain:** Findings from adjacent games (Prisoner's Dilemma, Traveler's Dilemma, ultimatum, resource games) may not always map onto n-person PGGs with peer punishment.
- **Heterogeneity and second-order dynamics:** The evolution and stability of punishment itself, issues of second-order punishment/reward, and heterogeneity (in cost, behavior, connectivity) are complex and not fully resolved, potentially affecting efficiency outcomes.

---

**In summary:**  
The theoretical literature provides a robust foundation for predicting **increased efficiency in public goods games when peer punishment is enabled**, especially given unfavorable baseline conditions. However, the precise magnitude and universality of this effect across all design dimensions are subject to important caveats—particularly in cases with high punishment cost, large group size, or anti-social punishment. Many dimensions central to game design and laboratory implementation are underexplored, and virtually no empirical evidence directly supports or quantifies these patterns. Predictions drawn from this literature should therefore be robust in direction (qualitative effect), nuanced in magnitude (conditioned by core design parameters), and cautious about out-of-sample and empirical extrapolation.
