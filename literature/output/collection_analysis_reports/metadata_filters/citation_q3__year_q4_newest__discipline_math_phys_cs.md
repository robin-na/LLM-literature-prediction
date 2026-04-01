# 1) Evidence Base

The literature set consists almost entirely of theoretical and simulation-based model papers, with only one direct empirical (experimental) study (Sun, K. T. et al., 2022). Most papers employ evolutionary game theory, replicator dynamics, or agent-based simulations to investigate public goods games (PGGs) and closely related environments. The set is broad in its coverage of structural and institutional design variations within PGGs—such as network structure, reward vs. punishment mechanisms, corruption, and exclusion—but is narrow regarding direct, experimental quantification of **efficiency** outcomes in human groups or direct measurement of treatment effects under applied punishment.

Most models focus on structured (spatial or networked) and well-mixed infinite populations under various punishment/reward technologies. Outcome measurement varies, with group efficiency (i.e., normalized group payoff) explicitly examined in a minority of cases. Many studies emphasize cooperation or contribution rates rather than payoffs or efficiency per se.

**Summary:** The evidence base is theory-heavy and focuses on PGGs and variants analyzed through mathematical models and simulations. Direct laboratory or field experimental evidence involving efficiency under punishment is minimal. Direct measurement of payoff-based outcomes is limited; most findings are qualitative or conditional on model parameters.

# 2) Task Relevance

For each target dimension, the literature set's relevance is as follows:

**a. pgg_or_variant**
- **exact**: The majority of papers (15+) directly study the classic public goods game or immediate variants (e.g., spatial PGG, pool punishment in PGGs).
- **close/adjacent**: Several papers examine adjacent social dilemmas (prisoner's dilemma, trust games, or generalized environments with similar choice structures).

**b. punishment_or_sanctions**
- **exact**: Most papers focus precisely on punishment or sanctioning, including tax-based punishment, probabilistic punishment, exclusion mechanisms, and feedback/intensity adaptation for punishment.
- **close/adjacent**: A few deal with exposure-based sanctioning or punishment analogs that depart from classic PGG punishment design.
- **none**: Only two papers focus on reputation or cooperation in the absence of any explicit punishment mechanism.

**c. efficiency_or_related_payoff_outcome**
- **exact**: A limited subset of papers report group efficiency or average group payoff as a primary outcome (Li et al., 2022; Sun et al., 2023; Wang & Perc, 2022).
- **close/adjacent**: More papers report average payoff, cost minimization, cost to institution, or payoff gap between strategies (Sun, Z. B. et al., 2023; Wang S.X. et al., 2022; Xie & Liu, 2024).
- **weak**: The majority only report behavior (contribution/cooperation rates, strategy frequencies). The mapping to efficiency or group payoff is discussed but not measured directly.

**Summary:** Relevance is **high** for PGGs and punishment, but **mixed to limited** for direct efficiency outcomes, with most evidence indirect or adjacent at best for the specific prediction task concerning efficiency shifts under peer punishment.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes (Efficiency, Group Payoff, Welfare, Surplus, Total Coins)**
    - *Directly measured* in a small number of theory/model papers (e.g., Li et al., 2022; Sun, Z. B. et al., 2023; Wang & Perc, 2022; Wang S.X. et al., 2022). These typically report efficiency ratios, average payoffs, cumulative costs, or explicitly construct payoff functions under different game design dimensions.
    - *Indirectly addressed* via average payoffs of cooperators/defectors, cost minimization (institutional cost), or by implication from the dominance of cooperation.

- **Non-Payoff Behavioral Outcomes (Contribution/Cooperation Rate, Punishment Frequency, Norm Compliance, Trust, Strategy Proportions)**
    - The *majority* of papers prioritize these: showing how design features affect cooperation frequency, prevalence of punishing/defecting strategies, trustworthiness, or compliance.
    - Payoff is often inferred from behavior, but the precise relationship (especially considering the costliness of punishment) is rarely specified or calculated.

**Distinction:** The direct prediction target—group efficiency with punishment enabled—has limited direct representation; behavioral proxies are common but have ambiguous mappings to efficiency due to cost structures and possible non-linearities.

# 4) Main Findings Relevant To Prediction

**Synthesis of Core Findings:**

- **Punishment Mechanisms Can Increase Efficiency, But Only In Certain Parameter Regimes**
    - Tax-based and institutional punishment can *dramatically* increase group efficiency—sometimes surpassing reward mechanisms—if punishment fines and costs are well-calibrated, and MPCR/synergy factor is high (Li et al., 2022; Wang & Perc, 2022).
    - When punishment is too costly, too weak, or ineffectively implemented, gains in cooperation may not translate into efficiency improvement, or efficiency may even decrease (Shen et al., 2022; Lee et al., 2024).

- **The Structure and Delivery of Punishment/Reward Matters**
    - Efficiency effects are highly sensitive to *how* punishment and reward are implemented:
        - Rewarding cooperators is more efficient than rewarding punishers.
        - Excessive support of punishers by rewards can *decrease* overall efficiency compared to control, even if cooperation remains high (Shen et al., 2022).
        - Hybrid incentive schemes (reward + punishment) can be optimal or suboptimal depending on the efficiency ratio of reward/punishment and network structure (Sun, Z. B. et al., 2023).

- **Dimension Effects and Critical Thresholds**
    - There are pronounced threshold effects on efficiency: e.g., critical values for punishment cost/fine, MPCR/synergy factor, and group size. Exceeding thresholds can lead to full cooperation and efficiency, while falling short can yield no gains or even losses (Li et al., 2022; Sun, Z. B. et al., 2023).
    - Reputation-based and probabilistic mechanisms can sustain both cooperation and payoff improvements when tuned properly—but may collapse if inclusive/exclusive thresholds are poorly chosen (Wang, X.J. et al., 2024; Quan et al., 2023).

- **Corruption and Institutional Weakness Can Erode Efficiency Gains from Punishment**
    - Corruption (bribery) can undermine the positive effect of punishment on cooperation, thereby reducing potential efficiency gains (Liu & Chen, 2022). When punishment can be bypassed, or when the economic 'richness' of the game changes, effects can reverse or become complex.

- **Most Evidence Is Theoretical/Simulated, Not Empirical**
    - No empirical study directly measures efficiency shifts under peer punishment in a classic PGG. The sole experiment (Sun, K.T. et al., 2022) addresses a trust game with collective punishment and reports behavioral changes, not efficiency.

**Disagreements/Ambiguities:**
- Some models predict that increasing punishment intensity always boosts efficiency, while others demonstrate negative or non-monotonic effects at high costs or with maladapted institutional support. Reward and punishment are not always additive; their interaction can produce counterproductive effects.

# 5) Prediction Guidance

**Usefulness of the Literature for Prediction:**
- **Direct mappings:** Where payoff/efficiency is explicitly modeled as a function of game parameters (Li et al., 2022; Wang & Perc, 2022), _theoretical_ formulas permit direct prediction of group efficiency given design features such as player_count, num_rounds (or simplifications for infinite populations), all_or_nothing, mpcr, punishment_cost, and punishment_tech.
    - These models can help estimate the *magnitude* and *sign* of expected efficiency changes from enabling punishment—conditional on design dimensions.
    - However, these are typically for well-mixed, infinite, or idealized populations, often with institutional rather than peer punishment.

- **Indirect/adjacent evidence:** Many papers show that proper design and moderate punishment can improve average payoffs or cost-effectiveness, _particularly_ when institutional and technological parameters are optimized, but the extrapolation to peer punishment effects in finite experimental or real-world groups is less justified.

- **Insufficient behavioral mapping:** Since most papers report cooperation/strategy frequencies, and the translation to efficiency depends on unmeasured punishment costs and differing game frames, prediction based solely on cooperation is unreliable.

**Therefore, for the downstream prediction task:**
- When theoretical models supply payoff/efficiency as a function of the game design, use those formulas directly—mindful of their assumptions (e.g., population size, type of punishment).
- Where only cooperation increases are reported, calibrate predictions conservatively, recognizing the risk that efficiency might remain flat or decline if punishment is costly or maladapted.
- Absence of empirical parameterization or experimental measurement of peer punishment's real-world effect on efficiency remains a crucial knowledge gap.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- **player_count**: Used explicitly in payoff/efficiency models.
- **num_rounds**: Modeled in infinite form (replicator dynamics) or as background in phase diagrams.
- **all_or_nothing**: Several models distinguish between all-or-nothing and continuous contributions.
- **mpcr**: Critical in almost all models; synergy/multiplier is often a bifurcation parameter.
- **punishment_cost & punishment_tech**: Central—both in models reporting efficiency and in those addressing behavioral outcomes.
- **reward_exists, reward_cost, reward_tech**: Frequently examined, especially in hybrid design models.

**Indirectly Informed Dimensions:**
- **show_n_rounds, show_other_summaries, show_punishment_id**: Rarely, if ever, manipulated in the theory models (exception: some models examine information effects via strategy composition, but not as explicit game dimensions).
- **chat**: Only the empirical trust game study includes any communication, which is not central to the core prediction task.

**Only Contextually Discussed/Missing:**
- **default_contrib**: Not examined as an independent manipulation.
- **reward_magnitude, punishment_magnitude**: Sometimes covered via generic 'cost' and 'fine' parameters but not always distinct.
- **show_other_summaries, show_punishment_id**: Largely absent or only relevant in stylized form.

**Peer Punishment vs. Institutional Punishment:**  
Most theoretical models address institutional or tax-based punishment; few focus on peer punishment _per se_, which limits direct prediction relevance for peer-based designs.

# 7) Important Limitations

- **Scarcity of Empirical and Experimental Efficiency Data**: Direct, quantitative experimental evidence for the effect of *peer* punishment on *efficiency* in PGG environments is absent; almost all findings are from theoretical or simulation models under idealized assumptions.
- **Efficiency Measurement Often Based on Model Assumptions**: Direct relevance for finite, experimental, or real-world PGGs is limited by untested behavioral assumptions (e.g., replicator dynamics, best-response adaptation, infinite population).
- **Punishment Framing Tends Toward Institutional/Tax-Based**: The translation of findings for institutional or tax-supported punishment to classic *peer punishment* in small groups is uncertain.
- **Behavioral Outcomes May Not Map Directly to Efficiency**: High cooperation or punishment frequency does not guarantee high efficiency if punishment is costly; only a minority of models examine the full payoff accounting.
- **Dimension Coverage Uneven**: Some design features relevant for downstream prediction—such as chat, default contribution framing, reward/punishment visibility—are missing or underexamined.
- **Heterogeneity and Network Structure**: Network or spatial effects are central in many models, which may complicate transfer to well-mixed or small group laboratory settings.
- **Nonlinearity and Threshold Effects**: Many models reveal sharp threshold or non-monotonic responses; predictions may be highly sensitive to parameter misestimation.

**Summary Limitation:** While the literature robustly indicates that *well-designed* punishment mechanisms _can_ enhance group efficiency or payoff under the right conditions, the absence of systematic, empirical evidence on peer punishment's effect on efficiency—and uneven coverage of all prediction-relevant game dimensions—demands cautious, model-based rather than data-driven prediction.
