# 1) Evidence Base

The paper set is exceptionally broad, with 69 papers encompassing lab and field experiments, theory, and meta-analyses on public goods games (PGG) and related social dilemmas. The set is predominantly empirical, with a heavy focus on experimental economics, combining both repeated and one-shot games, as well as adjacent environments like Common Pool Resource (CPR) games and market externality settings. Theoretical works provide formal guidance on mechanism design and welfare outcomes.

Crucially, the subset of papers with *direct empirical evidence* on the effect of *punishment* on *group efficiency or payoff outcomes* in canonical PGG and close variants is robust and multi-sourced (e.g., Jarungrattanapong, 2022; Ye et al., 2023; Kamei, 2024; Joseph et al., 2025; Botelho et al., 2022; Casari & Tavoni, 2024; Ntuli et al., 2023), spanning different institutional and participant contexts. Several theory papers directly address efficiency effects (e.g., Huang et al., 2024).

However, many papers in the set focus instead on cooperation rates, punishment behavior, norm compliance, or related non-payoff behavioral outcomes, and are of *adjacent* or *indirect* relevance for the prediction task, especially when efficiency outcomes are not reported or the treatment is not punishment (e.g., chat, reward, or minimum contribution treatments).

# 2) Task Relevance

**pgg_or_variant**: The literature is strongly relevant, with many studies using canonical PGG designs and others using close variants (CPR, market externality, PD, group lying), offering a rich evidence base for PGG-like environments. Several studies use adjacent or structurally similar games.

- **Relevance rating**: *exact* for most empirical lab studies and theory; *close* for CPR or market settings; *adjacent* for PD or games with different central mechanisms.

**punishment_or_sanctions**: Many papers study peer or institutional punishment, including ostracism, costly punishment, probabilistic sanctions, monitoring/fines, and centralized or third-party punishment. However, some focus only on communication, rewards, minimums, or alternative sanctioning, or on psychological factors affecting punishment use.

- **Relevance rating**: *exact* (majority, especially for peer or institutional punishment in PGGs), *close* (CRP, monitoring/fines, centralized sanctions), *adjacent* (partner choice, appeals), *weak/none* (papers with no punishment or only norms).

**efficiency_or_related_payoff_outcome**: Direct efficiency or group payoff is reported for a substantial subset of the literature, but many papers focus only on contribution rates, norm adherence, compliance, or similar behavioral outcomes.

- **Relevance rating**: *exact* (substantial empirical/theory subset), *close* (if efficiency can be inferred but not directly reported), *adjacent/weak/none* (if only contributions or non-payoff outcomes are measured).

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes**: Efficiency or group payoff (relative to the full-cooperation benchmark) is the primary measured outcome in a substantial number of core studies (e.g., Jarungrattanapong, 2022; Ye et al., 2023; Peng & Fan, 2023; Kamei, 2024; Joseph et al., 2025; Botelho et al., 2022; Casari & Tavoni, 2024; Ntuli et al., 2023; De Geest et al., 2022; Huang et al., 2024). Several others provide adjacent but not exact measures (average earnings, welfare, surplus); these are appropriately mapped for prediction.
- **Non-payoff behavioral outcomes**: Many studies, especially those in adjacent or less canonical variants, emphasize contribution/cooperation rates, punishment frequency, norm adherence, compliance, or related behaviors (e.g., Noussair et al., 2024; Coutts, 2024; Ramalingam & Stoddard, 2024; Gallo et al., 2023). Some focus on the psychological or group dynamic antecedents/moderators of punishment or cooperation rather than efficiency per se.

It is essential to note that *contribution increases do not always translate into efficiency gains*, due to the welfare costs of punishment.

# 4) Main Findings Relevant To Prediction

**Empirical findings from canonical or close PGGs:**

- **Punishment usually increases cooperation/contributions**, but the *effect on efficiency is conditional* on the following:
    - **Cost-effectiveness of punishment**: When punishment is costly to the punisher, its introduction can increase contributions but *reduce or fail to improve efficiency*, as the welfare cost of punishment (for both target and punisher) can offset or exceed the payoff gain from higher contributions (Botelho et al., 2022; Casari & Tavoni, 2024; Peng, 2022; Deng et al., 2025).
    - **Network/institutional structure**: Punishment's positive effect on efficiency is stronger in settings with incomplete networks (Peng & Fan, 2023), formal/institutionally set punishment, or costless deterrent punishment (Bühren et al., 2025; Kamei, 2024), compared to decentralized, voluntary, or anti-social-prone punishment.
    - **Magnitude and targeting**: Large, well-targeted punishment, especially when aimed at the lowest contributors or at pivotal thresholds, can *maximize efficiency* (Ye et al., 2023; Huang et al., 2024).
    - **Design features (player count, rounds, MPCR)**: Higher MPCRs, smaller groups, and complete information about others' actions tend to facilitate efficiency gains from punishment, but group composition (e.g., cognitive ability, culture) and the potential for anti-social punishment or retaliation can moderate or reverse this effect.
    - **Endogeneity and representation**: When individuals can vote or institutionalize punishment, they do so only if it improves payoffs for themselves (Botelho et al., 2022), and representation (rather than self-decision-making) can reduce punishment's effectiveness for efficiency (Kim et al., 2025).
    - **Adjacency effects**: In adjacent CPR, resource, or market externality games, punishment generally *increases efficiency* when it is well-targeted and cost-effective, but can fail or reduce efficiency if costs are too high, if punishment is collective/non-targeted, or if social context undermines coordinated enforcement (Ntuli et al., 2023; De Geest et al., 2022; Schaefer, 2023; Jiang & Villeval, 2024).

**Theoretical results:**

- **Optimal design principles**: Minimal, targeted punishment achieves maximal efficiency (Huang et al., 2024). Combined reward and minimal punishment is even more effective if both are available.
- **Population structure and patience** also play a role: repeated play, high patience, and the absence of uncoordinated altruists support efficient enforcement via punishment (Dong et al., 2024; Camera & Gioffré, 2025).

**Summary:**  
- Enabling punishment *can* increase efficiency, but only when the cost, structure, and implementation are favorable.  
- In standard lab PGGs with costly voluntary punishment, efficiency gains are possible but *far from guaranteed* and may be negative.  
- Well-designed, costless, or institutionally implemented punishment sustains high efficiency.  
- Incomplete, coordinated, or targeted punishment mechanisms typically perform better than decentralized or anti-social-prone peer punishment.  
- Antisocial punishment, retaliatory dynamics, and high punishment costs are consistent, empirically observed obstacles to efficiency gains.

# 5) Prediction Guidance

Given *game design dimensions* and *control efficiency*, predict efficiency with punishment enabled as follows:

- **Presence of peer or institutional punishment (punishment_exists, punishment_tech, punishment_cost):**
    - *If punishment is institutionally set, costless or nearly so, and well targeted*: Expect substantial, often maximal, efficiency gains relative to control in otherwise standard PGGs (Kamei, 2024; Bühren et al., 2025; Huang et al., 2024).
    - *If punishment is decentralized, peer-to-peer, and costly*: Do *not* assume efficiency gains; anticipate neutral or negative efficiency change unless the punishment is rarely used and anti-social punishment is limited (Botelho et al., 2022; Casari & Tavoni, 2024; Peng, 2022; Deng et al., 2025).
    - *Magnitude matters*: Sufficiently strong punishment (above a critical threshold), well targeted, is necessary for efficiency improvements (Ye et al., 2023; Huang et al., 2024).
- **Reference to control (no-punishment) efficiency:**
    - *Low control efficiency*: Introduction of effective punishment can produce large absolute efficiency gains, *if* the punishment design is favorable (e.g., Kamei, 2024).
    - *Already high control efficiency*: Less room for improvement, and punishment costs may simply reduce payoffs.
- **Moderator dimensions:**
    - *player_count*: Smaller groups generally achieve higher efficiency gains from punishment, while larger or more heterogeneous groups are at risk of coordination failures (Jiang & Villeval, 2024).
    - *mpcr*: Higher MPCRs make punishment mechanisms more likely to pay off in efficiency terms.
    - *network/institutional structure*: Complete punishment networks can backfire (Peng & Fan, 2023; Bühren et al., 2025) compared to incomplete or strategic networks.
    - *all_or_nothing, chat, show_other_summaries, show_punishment_id*: These may modulate behavioral responses and thus efficiency, but are less directly addressed in efficiency studies.
    - *Reward mechanisms*: If both punishment and reward (reward_exists) are present, theory predicts to use maximal reward and minimal punishment for maximal efficiency (Huang et al., 2024).
    - *Culture, representation, cognitive ability*: Cultural and cognitive heterogeneity, group decision structure, and representation can moderate not just the behavioral effects of punishment but also efficiency impacts (Kim et al., 2025; Kamei et al., 2025).

**Caveat:**  
Increasing contributions does *not* guarantee increased efficiency due to the direct cost of punishment. Consider whether the cost of punishment is likely to eat into efficiency gains from cooperation.

# 6) Design Dimensions Highlighted Across Papers

- **Directly informed:** player_count, num_rounds, mpcr, punishment_cost, punishment_tech, all_or_nothing (most empirical studies and theory papers).
- **Indirectly informed:** chat (a few studies note it as a moderator, but most PGGs have none), reward_exists, reward_cost, reward_tech (few studies with both reward and punishment).
- **Only contextually discussed:** show_n_rounds, show_other_summaries, show_punishment_id, default_contrib (often controlled or unreported; some exceptions in studies of information, feedback, or default settings).
- **Effectively missing:** There is little systematic experimental manipulation of default_contrib, show_n_rounds, show_punishment_id across studies reporting on efficiency outcomes with punishment.

# 7) Important Limitations

- **Heterogeneity in mechanisms:** The efficiency effect of punishment varies widely depending on punishment mechanics, cost, magnitude, and network structure, which are not always reported in standardized ways.
- **Overrepresentation of lab environments:** The majority of payoff-based evidence comes from controlled lab settings, which may not capture field complexity (though some field and framed experiments are included).
- **Cultural and group composition moderators underexplored:** While several papers highlight differences due to culture, cognitive ability, and group composition, most efficiency findings are drawn from homogeneous, student samples.
- **Sparse manipulation of certain dimensions:** Design features such as chat, feedback, default contribution, and the visibility of punishers are rarely experimentally varied among payoff-outcome studies.
- **Ambiguity and disagreement:** Empirical results conflict—some show large efficiency gains (when punishment is costless or well-targeted), others show losses or null effects (when punishment is costly, antisocial, or collective rather than individual).
- **Predominance of non-payoff (behavioral) outcomes in broader literature:** Many papers in the set only report on contribution rates or punishment behaviors; these cannot be mapped directly onto efficiency changes.
- **External validity:** The translation of laboratory results, especially for diverse institutional forms of punishment, to field prediction is limited.

---

**In conclusion:**  
The literature offers strong, multi-sourced, but design-sensitive evidence for predicting efficiency changes from enabling punishment in PGG-like games. Accurate prediction requires close reference to punishment cost/tech and control efficiency. Other dimensions are less systematically evaluated, but pose important moderators or sources of uncertainty. Prediction accuracy will be highest when the canonical design dimensions and institutional structure in the prediction input closely match the experimental conditions from high-relevance, efficiency-reporting studies.
