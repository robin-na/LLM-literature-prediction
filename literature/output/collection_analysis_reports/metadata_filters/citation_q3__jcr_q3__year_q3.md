# 1) Evidence Base

The paper set includes 23 studies with a mix of experimental (lab-based) and theoretical (modeling/simulation) papers. The evidence base is broad in terms of theoretical approaches (covering evolutionary game theory, decision science, norm psychology, and network models) but is narrower regarding direct empirical (experimental) results specifically linking peer punishment to efficiency in canonical public goods games (PGG). Direct efficiency measurement in experimental PGGs with and without peer punishment is comparatively rare in this set—most theoretical models and some experiments focus on cooperation rates or indirect markers of group success, with relatively few studies reporting (or even targeting) group efficiency as defined for the prediction task.

# 2) Task Relevance

**pgg_or_variant:**
- *exact*: A substantial subset of theory and experiment papers directly examine standard or continuous PGGs and their variants (e.g., Pfattheicher et al., 2018; Jiao et al., 2020; Huang et al., 2018; Flores et al., 2021; Murase & Baek, 2018).
- *close/adjacent*: Several papers study close but non-PGG social dilemmas (trust games, CPR, collective risk dilemmas) with relevant structural similarities (Fehr & Sutter, 2019; Perry et al., 2018; Couto et al., 2020).
- *none*: A few modeling/network studies are not relevant to PGG or any variant (Bianchi et al., 2020).

**punishment_or_sanctions:**
- *exact*: About half the set directly manipulates or models punishment or sanctioning as a design variable (Pfattheicher et al., 2018; Jiao et al., 2020; Huang et al., 2018; Flores et al., 2021).
- *close/adjacent*: Several discuss related incentive/sanction mechanisms (e.g., reward, gossip as social sanction, endogenous Nash reversion) but without explicit player-administered punishment (Fehr & Sutter, 2019; Fang & Chen, 2021).
- *none*: Some papers have no punishment or sanctioning mechanisms at all (Gianotti et al., 2019; Bianchi et al., 2020).

**efficiency_or_related_payoff_outcome:**
- *exact*: Relatively few papers report efficiency (total payoff / possible maximum) as the main outcome (Pfattheicher et al., 2018; Jiao et al., 2020; Huang et al., 2018; Fehr & Sutter, 2019).
- *close/adjacent*: More commonly, studies report behavioral outcomes (cooperation rates, norm compliance) or discuss welfare/achievement in ways related to efficiency, but specific group efficiency data are rare (Couto et al., 2020; Perry et al., 2018; Du et al., 2018).
- *weak/none*: Many empirical and theoretical papers lack payoff/efficiency outcomes altogether, focusing on behavior, norms, or cognitive mechanisms.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes (group payoff, efficiency, welfare, surplus):** The most directly relevant studies provide explicit measures of group efficiency or average total payoff under different punishment regimes (Pfattheicher et al., 2018; Jiao et al., 2020; Huang et al., 2018; Fehr & Sutter, 2019).
- **Non-Payoff Behavioral Outcomes (contribution rates, cooperation, punishment frequency, norm compliance):** These are far more common in both experimental and theory papers. In many cases, the main findings on the effect of punishment are based on changes in contributor types or persistence of prosocial behavior clusters (Flores et al., 2021; Du et al., 2018; Fang & Chen, 2021).
- **Other Outcomes:** Some studies examine psychological measures (e.g., trust, satisfaction, perceived fairness), neural correlates of prosociality (Gianotti et al., 2019), or emerging social norms, but these are not directly linked to group efficiency.

# 4) Main Findings Relevant To Prediction

**Empirical Findings (Efficiency or Payoff Focus):**
- **Standard peer punishment often increases cooperation but can decrease group efficiency due to punishment's direct costs:** Lab experiments and theoretical models consistently show that enabling standard (non-democratic) peer punishment substantially increases contribution rates, but the efficiency effect is negative or neutral unless punishment costs are low or punishment structures reduce antisocial punishment (Pfattheicher et al., 2018; Jiao et al., 2020).
- **Mechanism design is crucial—modifying punishment structure can change efficiency effects:** Variations like *democratic peer punishment* (punishment executed only with group consensus) or *probabilistic punishment* (Jiao et al., 2020) reduce wasteful or antisocial punishment and can allow punishment to improve both cooperation and efficiency, particularly as games are repeated or punishment is rare but credible.
- **High cost of punishment can eliminate efficiency gains:** Both theory and experiment highlight that when punishment is expensive relative to its effect, efficiency may fall below control (no-punishment) baselines despite higher cooperation (Huang et al., 2018; Perry et al., 2018).
- **Corruption and misuse of punishment can undermine efficiency unless checked:** The presence of corrupt punishment (punishers extracting bribes or punishing cooperators) generally decreases mean payoff unless additional mechanisms (corruption control, asymmetrical punishment targeted at corrupt punishers) are enabled (Huang et al., 2018).
- **Non-material social sanctions (e.g., gossip) can increase efficiency without direct costs:** Enabling third-party gossip results in increased trust and higher efficiency—potentially more cost-effective than direct punishment (Fehr & Sutter, 2019).

**Theory and Indirect/Behavioral Findings:**
- **Punishment expands the parameter space for cooperation, but efficiency effects are highly context-dependent:** In spatial or structured populations, punishment is particularly effective when costs are low and clustering is possible; at intermediate costs, it can be destructive instead (Flores et al., 2021).
- **Additional mechanisms (rewards, communication, probabilistic execution) can further moderate efficiency:** Rewards can be more effective than punishment in some settings (Fang & Chen, 2021); enabling chat can substitute for punishment as a means of increasing cooperation (Bigoni et al., 2019).

**Divergent or Cautionary Points:**
- **Antisocial punishment and reputation risks muddle predictions:** There is a risk that punishment may be maladaptive if it becomes antisocial (targeting cooperators), or when cultural/psychological context leads to social costs for prosocial individuals, sometimes decreasing efficiency (Raihani & Power, 2021).
- **Heterogeneity in agents and group structures (hierarchies, network effects) can create variable outcomes:** Models incorporating foresight, status, and adaptive strategies show that punishment is more likely to increase efficiency when it aligns individual and collective interests, and when dominant individuals are incentivized to punish (Perry et al., 2018; Smith, 2020).

# 5) Prediction Guidance

**Direct Guidance for Downstream Prediction:**
- *Punishment typically increases cooperation, but its efficiency effect is conditional*: For games with high punishment costs relative to impact, enabling standard peer punishment may reduce efficiency vs. the control; efficiency improvements are more likely when punishment is low-cost, rare, or implemented via democratic or probabilistic mechanisms (Pfattheicher et al., 2018; Jiao et al., 2020).
- *Design dimensions critically moderate efficiency impacts*: Efficiency gains are most likely with small/medium groups, moderate marginal per-capita return (mpcr), low punishment cost, and mechanisms that reduce the risk/cost of antisocial or excessive punishment (democratic/punishment, probabilistic punishment, corruption controls).
- *Use control efficiency as a baseline, reason about incremental gains or losses*: For environments already near full cooperation without punishment, adding punishment (especially costly forms) may reduce efficiency; for low-control-efficiency settings, well-designed punishment can potentially raise efficiency, but only if punishment costs do not dominate the efficiency calculation.
- *Beware generalizing from behavioral to efficiency outcomes*: Many studies report higher cooperation with punishment, but do not measure group payoff; efficiency gains cannot be assumed from behavioral improvements alone.

**When Predicting Treatment Efficiency from Design + Control:**
- If *standard peer punishment with moderate cost* is enabled, expect possible efficiency loss or modest gain depending on cost, number of rounds, and likelihood of antisocial punishment.
- If *punishment structure includes democratic consensus or high selectivity/probabilistic execution*, expect higher potential for efficiency gains versus both control and standard punishment.
- *Corruption controls* and *alignment between individual and group interests* (as in institutional or graduated punishment) are likely to increase efficiency impact.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions** (strong, quantitative, or explicitly modeled evidence):
- **player_count**: Modeled in most relevant theory papers and varied in experiments (e.g., Pfattheicher et al., 2018; Jiao et al., 2020); group size effects are discussed.
- **num_rounds**: Repeated game structure and round effects are direct moderating variables (democratic punishment becomes more efficient over time).
- **mpcr**: Marginal per-capita return is a key parameter in theory and experiment (varied in Pfattheicher et al., 2018; Jiao et al., 2020), affecting both cooperation and the cost/benefit trade-off of punishment.
- **punishment_cost**: Central in most modeling papers (Jiao et al., 2020; Huang et al., 2018; Flores et al., 2021); directly moderates efficiency impact.
- **punishment_tech**: Mechanism details (democratic, probabilistic, graduated, institutional) are directly analyzed and shown to affect efficiency (Pfattheicher et al., 2018; Jiao et al., 2020; Couto et al., 2020).
- **reward_exists/reward_cost**: Modeled in several papers (Jiao et al., 2020; Fang & Chen, 2021).

**Indirectly Informed Dimensions** (contextual discussion or partial analysis):
- **all_or_nothing**: Some studies use continuous vs. all-or-nothing contribution designs, but effects on prediction are only sometimes addressed.
- **chat**: Effects of communication (chat) are shown to strongly boost cooperation; not always cross-analyzed with punishment efficiency (Bigoni et al., 2019).
- **show_other_summaries/show_n_rounds**: Partially present in models, rarely isolated experimentally.
- **show_punishment_id**: Not extensively discussed as a key moderator in this set.

**Missing or Sparsely Addressed Dimensions**:
- **default_contrib**: Framing effects (opt-in/opt-out default contributions) are not analyzed.
- **reward_tech, reward_magnitude, reward_cost**: Only modeled at a general level; comparative efficiency impact versus punishment is not a major focus.
- **show_punishment_id** and **reputational visibility**: Occasionally mentioned (e.g., in the context of antisocial punishment or gossip), but not systematically varied as a design feature.

# 7) Important Limitations

- **Sparse direct experimental evidence on efficiency effects of enabling (vs. not enabling) punishment in PGGs:** While several theory papers and a key experiment (Pfattheicher et al., 2018) address this, most studies report on contribution or cooperation rates, not total group efficiency.
- **Few papers enable systematic prediction across the full 14 design dimensions:** Most empirical studies vary just 2-3 game parameters, limiting extrapolation.
- **Limited empirical data on more complex punishment structures (e.g., probabilistic, graduated, democratic) and their real-world efficiency effects:** Theory is suggestive but generalizability is uncertain.
- **Ambiguity in mapping behavioral improvements to efficiency:** Many studies equate increased cooperation with increased welfare or efficiency, but direct measurement of total payoffs is uncommon, and efficiency gains can be offset by punishment costs.
- **Antisocial punishment and misuse are not always modeled or measured:** This can lead to overestimating positive effects of punishment on efficiency.
- **Limited attention to cross-dimensional interactions:** For instance, how chat, visibility, and network structure moderate punishment's efficiency impact.
- **Transference from adjacent or non-PGG games:** While structural analogies are suggestive, prediction from trust games or CPR dilemmas to canonical PGGs should be cautious.
- **Cultural/contextual relevance:** Some theoretical mechanisms or experimental settings may not generalize across societies or field environments.

---

**In summary:** The literature provides a useful (but incomplete) platform for predicting the efficiency impact of enabling punishment in public-goods-game-like designs. It supports nuanced, context-dependent predictions—especially with careful attention to mechanism details (punishment cost, structure, and corruption controls)—while highlighting the need to avoid overgeneralizing from behavioral to efficiency outcomes. Some prediction dimensions are well-supported, but important gaps remain, especially in empirical outcome measurement and cross-dimensional analysis.
