# 1) Evidence Base

The reviewed paper set is robust in coverage of public goods games (PGGs) and their variants, incorporating both **empirical (experimental lab studies)** and **theoretical papers**. Of the 37 papers, roughly one-third provide either direct experimental tests of punishment mechanisms in PGGs or models of efficiency with punishment, with the remainder focused on alternative mechanisms, adjacent games, or indirect outcomes. The empirical work includes both standard and variant PGG lab experiments, but many other included studies focus on contests, coalition games, team trust games, helping games, or mechanism design more broadly. Theoretically, papers address the sustainability of cooperation, efficiency, network effects, and dynamic punishment, but often in models that generalize or depart from standard PGGs.

The evidence base is **broad in game structure and mechanism coverage** but **heterogeneous in focus** on the core prediction task—namely, predicting efficiency change from adding punishment to a given PGG. Only a minority of studies directly compare group payoff or efficiency between control and punishment treatments in an exact PGG setting.

# 2) Task Relevance

| Dimension                     | Typical Relevance Label | Rationale                                                                                                    |
|-------------------------------|------------------------|--------------------------------------------------------------------------------------------------------------|
| **pgg_or_variant**            | exact/close/adjacent   | A substantial subset of papers are exact (e.g., Chen, 2022; Lippert & Tremewan, 2021), some are close or adjacent (e.g., Mitzkewitz & Neugebauer, 2020), while several address generalizations (e.g., networked or contest games). |
| **punishment_or_sanctions**   | exact/close/adjacent   | Several papers use exact (standard costly or monetary) punishment (e.g., Chen, 2022; Kingsley & Smith-Walter, 2024), while a number test or theorize adjacent forms—ostracism, peer approval, reputation, institution-based punishment, or coordinated punishment—with a few only referencing punishment but not manipulating it.              |
| **efficiency_or_related_payoff_outcome** | exact/close/adjacent/weak | Only a fraction of the papers directly report efficiency (group payoff ratio to the full-cooperation benchmark), while others focus on adjacent measures (earnings, total payoff, compliance rates) or entirely on non-payoff behavioral outcomes (e.g., contributions, cooperation frequency, honesty rates).                                        |

Overall, **direct experimental evidence on treatment-versus-control efficiency effects of peer punishment in exact PGGs is limited**, with richer coverage in theory or in variant or adjacent settings. Many studies measure only contribution or cooperation rates, not total or relative payoffs.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes (for Prediction Task):**
  - **Efficiency**: Most clearly aligned with prediction needs; measured as group earnings/payoff relative to the maximal full-cooperation benchmark. (E.g., Chen, 2022; Lippert & Tremewan, 2021; Faillo et al., 2020; Falvey et al., 2025; Mitzkewitz & Neugebauer, 2020; Zhosan & Gardner, 2013)
  - **Group Earnings/Payoff/Surplus**: Often reported when efficiency is not (sometimes as average tokens/period—cf. Chen, 2022; Hsu, 2013).
  - **Aggregate Welfare**: Includes studies using measures like welfare or surplus—functionally equivalent to efficiency for prediction.
- **Non-Payoff Behavioral Outcomes:**
  - **Contribution Rate/Level:** Commonly measured, but distinct from efficiency, as punishment costs or resource destruction can lead to higher contributions but lower efficiency (e.g., Kingsley & Smith-Walter, 2024).
  - **Compliance Rate**: Measured in tax games; increases may or may not translate to higher efficiency (e.g., Hsu, 2013).
  - **Punishment Frequency/Intensity or Sanction Assignment:** Often reported to analyze behavior, not efficiency impact.
  - **Other Behavioral Measures:** Norm adherence, strategy adoption, coalition membership, honesty rates.

In summary, few papers provide **direct payoff-based outcomes needed for prediction**; non-payoff behaviors can be informative for mechanism but are not directly predictive of group efficiency.

# 4) Main Findings Relevant To Prediction

### **Empirical Findings**
- **Punishment Does Not Always Increase Efficiency in PGGs:** In the clearest PGG-with-payoff studies (e.g., Chen, 2022), **enabling punishment does not increase group efficiency** and sometimes reduces average group earnings relative to control, particularly due to antisocial or poorly targeted punishment and resource destruction.
- **Institutional Features Matter:** Mechanisms enabling coalition enforcement, community or coordinated punishment, or institutional structures (tax-based) can have much more pronounced and positive effects on efficiency than voluntary ad hoc punishment (McEvoy, 2012; Wang et al., 2023; Olcina & Calabuig, 2015).
- **Comparison to Rewards and Communication:** Several papers (Faillo et al., 2020; Chen, 2022) find that reward or social approval (even non-monetary, costless) can increase efficiency as much as or more than punishment, sometimes at lower cost. Communication is repeatedly shown (Zhosan & Gardner, 2013) to have a large, positive effect on efficiency, often outweighing or supplementing punishment effects.
- **Contextual Moderators:** Game design dimensions such as **MPCR, heterogeneity, player count, cost and magnitude of punishment, feedback structure, visibility (monitoring), and possibility of antisocial punishment** modulate whether punishment increases or decreases efficiency.

### **Theoretical Findings**
- **Targeted and Effective Punishment Needed:** Theory (Sugaya & Wolitzky, 2023; Jindani, 2020; Olcina & Calabuig, 2015) shows that **punishment that is targeted, effective, and coordinated can sustain or even ensure efficient cooperation**, but punishment that is untargeted, ineffective, or misapplied can fail or reduce efficiency.
- **Critical Role of Monitoring:** The ability for players to observe defections and attribute them to individuals (Mihm & Toth, 2020; Laclau & Tomala, 2017) is crucial—efficiency gains from punishment depend on sufficient information and monitoring structure (e.g., show_other_summaries, show_punishment_id).
- **Costs Matter:** In settings where the cost of punishment is high relative to its effectiveness, or where peer/reward mechanisms are weak, punishment may not sustain efficiency. Excessive punishment costs can even decrease efficiency below control levels.

### **Adjacency and Ambiguity**
- Some studies show that the **announcement or framing of punishment can crowd out intrinsic motivation** and reduce cooperation or efficiency, even when punishment is not enforced (Klempt & Pull, 2018; Hakimov & Kajackaite, 2024; Povey, 2014).
- **Heterogeneous effects:** Group composition (e.g., presence of 'bad apples' or antisocial punishers), visibility of identity, and the presence of network structure can create ambiguous or negative effects of punishment on efficiency.

**In summary:** The most directly relevant experimental studies produce mixed or negative evidence for punishment enhancing efficiency in PGGs, except in institutional forms or with careful design. Theory supports this, showing punishment *can* enable efficiency, but only under sufficient effectiveness, coordination, and information.

# 5) Prediction Guidance

- **Direct Experimental Evidence (Exact PGGs):** For standard lab PGGs matching games like Chen (2022), do not expect efficiency gains from enabling punishment; efficiency may be unchanged or even lower vs. control, due to cost of punishment and antisocial uses.
- **Control Efficiency is a Strong Predictor:** If the control (no punishment) efficiency is already relatively high, **adding peer punishment is less likely to provide additional gains**—and may even lower efficiency (Chen, 2022).
- **Institutional/Coordinated Punishment:** Where the punishment mechanism is institutional (tax-based, coalition-enforced) or coordinated, and punishment is sufficiently effective/low-cost, **enable substantial efficiency gains** (Jindani, 2020; Olcina & Calabuig, 2015; Mihm & Toth, 2020; Sugaya & Wolitzky, 2023).
- **Monitoring and Feedback:** Efficient outcomes are most likely when **punishment is both feasible and visible** (players can monitor others' actions and identities—show_other_summaries, show_punishment_id).
- **Design Dimensions are Critical:** For reliable prediction, consider player_count, MPCR, punishment_cost and magnitude, game heterogeneity, feedback structure, and communication.
- **Reward and Communication:** In some settings, enabling reward or communication may be more effective at boosting efficiency than punishment.
- **Predict Ambiguous or No Effect Where Evidence is Sparse or Behavioral-Only:** Where only contribution rate or behavioral outcomes are reported, do not infer efficiency gains without direct payoff data.

# 6) Design Dimensions Highlighted Across Papers

- **Directly Informed Dimensions:**
  - **player_count**: Frequent focus or variation (most experimental work).
  - **num_rounds**: Nearly universal in repeated game studies.
  - **chat**: Treated as a moderator (Zhosan & Gardner, 2013; Hajikhameneh & Iannaccone, 2023).
  - **mpcr (Marginal per capita return)**: Often highlighted as a moderator of both baseline efficiency and punishment effects.
  - **all_or_nothing**: Some studies distinguish continuous vs. binary contribution.
  - **punishment_cost/punishment_tech**: Directly manipulated in several studies; linked to likelihood and effect of punishment (Chen, 2022; Mitzkewitz & Neugebauer, 2020).
  - **show_other_summaries and show_punishment_id**: Addressed conceptually and via monitoring in theory (Mihm & Toth, 2020; Laclau & Tomala, 2017; Jindani, 2020).
  - **reward_exists/reward_cost/reward_tech**: Sometimes varied in multi-arm experiments.

- **Indirectly Informed:**
  - **default_contrib**: Occasionally contextually described, rarely a direct treatment.
  - **show_n_rounds**: Sometimes used as feedback/uncertainty manipulation.
  
- **Sparse or Missing:**
  - **show_punishment_id**: Only a few papers make identity or attribution explicit.
  - **punishment_magnitude**: Occasionally implied, but not always separately varied.
  - **reward_cost/reward_tech**: Less often manipulated or precisely reported.

**Notably**, papers are most informative where they detail and manipulate punishment mechanism parameters, and where efficiency is the primary outcome. Dimensions like chat, monitoring, group size, and MPCR are best-supported; other dimensions, such as default_contrib, are infrequently discussed.

# 7) Important Limitations

- **Few Exact PGG Experiments with Full Payoff Reporting:** Only a small set of studies directly test peer punishment in exact PGGs and report efficiency; many measure only contributions or adjacent games.
- **Generalizability Limits:** Many findings are for two-player games, specific mechanisms (e.g., pledge-and-review, coordinated punishment), or adjacent settings (network games, team trust games, tax games), limiting transferability to generic PGG prediction.
- **Ambiguous Effects and Moderators:** The effect of punishment depends critically on design details (mechanism, cost, visibility, group structure, coordination), and effects may be negative, null, or positive depending on these moderators.
- **Behavioral vs. Payoff Outcomes:** Many studies only report on cooperation, contribution, or compliance—not on efficiency or group welfare—limiting predictive power for payoff-based tasks.
- **Lack of Systematic Variation:** Most studies vary a subset of design dimensions, impeding a full multivariate understanding of how design drives efficiency with and without punishment.
- **Time Horizon Effects:** Some theory points to dynamic negative consequences of punishment on group welfare via erosion of intrinsic motivation, not usually captured in short-horizon experiments (Povey, 2014).
- **Sparse Data on Certain Dimensions:** Features like default_contrib, show_punishment_id, or nuances of punishment/reward magnitude are infrequently varied or reported.

**In conclusion**, the literature provides rich theoretical and some direct experimental perspective on when and why punishment can (or cannot) increase efficiency in PGGs, but actual prediction of treatment efficiency requires caution, close matching to studied mechanisms, and should not over-extrapolate from non-payoff or adjacent outcomes. Empirical findings directly support the expectation that standard peer punishment in PGGs often does not increase (and sometimes reduces) efficiency relative to control, unless specifically institutionalized or coordinated under favorable design conditions.
