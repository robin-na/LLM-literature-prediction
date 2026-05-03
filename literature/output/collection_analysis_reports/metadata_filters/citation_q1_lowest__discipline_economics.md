# 1) Evidence Base

The paper set is large (229 items) and diverse, containing a rich mix of empirical (especially experimental lab and field studies) and theoretical work. The empirical studies dominate, especially experiments with repeated and one-shot public goods games (PGGs) and close variants, but there is also substantial coverage of related environments such as trust games, CPR (common-pool resource) extraction, and coordination/entry games. Theoretical papers often focus on mechanisms, institutional design, and equilibrium predictions about punishment’s efficacy.

Within this set, a significant number of studies directly implement and experimentally test peer or centralized punishment in PGG or PGG-like settings, with outcomes measured both in behavioral (e.g., contributions, compliance rates, punishment assigned) and, critically, payoff-based terms (e.g., group efficiency, group earnings, welfare, total coins). Both theory and experiments often contrast the punishment-enabled treatment to a standard control game with punishment disabled.

Contextually adjacent studies (e.g., bargaining, trust, coalition games, contests) extend the landscape but are less directly informative for the PGG-punishment-efficiency prediction task. Papers without explicit punishment, or with only weak connections to efficiency or payoffs, round out the periphery.

Overall, for the task of predicting the efficiency effect of enabling peer punishment in PGG-like environments, the evidence base is both broad and deep, with abundant directly relevant empirical data and theory, but significant heterogeneity and contextual detail.

---

# 2) Task Relevance

### a) PGG or Variant (`pgg_or_variant`)
- **Exact**: Many papers use canonical or slightly modified public goods games as their design, with full mapping to the forecast environment.
- **Close**: Others use directly analogous games (trust games, repeated PDs, CPRs, threshold public goods, etc.) where the logic, structure, and outcomes are similar but not identical.
- **Adjacent**: Additional studies address loosely related settings (ultimatum, bargaining, market games), offering mechanism or moderator evidence but not direct mappings.
- **Weak/None**: Many papers focus on mechanisms or behavioral outcomes relevant to PGGs without using a PGG structure, or provide only background evidence.

### b) Punishment or Sanctions (`punishment_or_sanctions`)
- **Exact**: The majority of core empirical and theoretical papers involve explicit, costly peer or centralized punishment mechanisms (often with detailed parameterizations: cost, target, severity, etc.).
- **Close/Adjacent**: Some studies focus on reward, exclusion, ostracism, or institutional variants (e.g., monitoring, coalition formation, network structure) that serve similar enforcement or sanctioning purposes.
- **Weak/None**: A large subset only considers the control (no-punishment) case or substitutes non-monetary or reputational sanctions.

### c) Efficiency or Related Payoff Outcomes (`efficiency_or_related_payoff_outcome`)
- **Exact**: There is robust measurement and analysis of efficiency (group payoff as a fraction of the social optimum) in many key papers.
- **Close**: Numerous others report earnings, welfare, or surplus, allowing for recalculation or proxying of efficiency.
- **Adjacent**: Many focus only on behavioral metrics (e.g., cooperation rate, contribution rate), which must not be conflated with efficiency.
- **Weak/None**: Some include no relevant payoff data.

**Summary:** The evidence base is strongest and most extensive where the task’s three dimensions (PGG, punishment, efficiency) align at the `exact` or `close` level, but coverage becomes increasingly indirect where outcomes are behavioral or the environment is more loosely analogous.

---

# 3) Outcomes Measured In The Literature

### Payoff-Related Outcomes (Direct Efficiency)
- **Efficiency** (group payoff vs. full cooperation) is directly measured in many PGG studies (lab and theory).
- **Group Payoff**, **total earnings**, **welfare**, and **surplus** are numerically reported and can generally be equated to efficiency, except where resource destruction or punishment costs intervene.
- Some papers use **comparative efficiency** (baseline vs. punishment-enabled) as the primary outcome.

### Non-Payoff Behavioral Outcomes
- **Contribution rate** or **cooperation rate** (share of endowment given, probability of contributing) is very frequently measured, and is often but not always positively associated with efficiency.
- **Punishment frequency** (how often punishment occurs), **amount assigned**, and **targeting** (prosocial vs. antisocial) are widely reported.
- **Norm compliance**, **compliance rates**, and **retaliation** behaviors are also commonly tracked.
- Studies sometimes report **willingness to pay to punish** or **preference for institutions**, which is informative for mechanism selection but not for efficiency per se.

**Critical Distinction**: Many papers (including some with ‘payoff’ outcomes) find that while punishment increases cooperation/contributions, the costliness of sanctioning can offset or reverse potential efficiency gains. This distinction between behavioral and efficiency outcomes is a recurring theme.

---

# 4) Main Findings Relevant To Prediction

**Synthesis Across the Most Relevant Literature:**

- **Punishment increases contributions but often harms efficiency in standard, short, peer-punishment PGGs**, due to resource-destroying costs, unless punishment is well-targeted and/or infrequently used (Fehr et al., 2010; Botelho et al., 2022; Chen, 2022; Casari & Tavoni, 2024; Robbett, 2019; Del Ponte et al., 2025).
    - *Empirics show* that punishment can raise group payoff above control only if direct costs are low, the network structure channels punishment effectively, or higher-order (meta) punishment aligns incentives (Glöckner et al., 2018; Peng & Fan, 2023; Kanitsar, 2021; Krügel & Maaser, 2025).
- **Centralized, formal, or institutional punishment often increases efficiency more reliably**, especially when punishment is deterrent and costs can be amortized or are lower per infraction (Kamei, 2024; Kamei et al., 2023; Lim & Zhang, 2020; Huang et al., 2024).
- **Enabling punishment tends to have larger, more positive efficiency effects in repeated, longer-horizon, or endogenous-choice (institution selection) settings** (Fehr et al., 2010; Gürdal et al., 2021; Kamei et al., 2023), and when social interaction or feedback is possible.
- **Heterogeneity in group returns (MPCRs), group size, punishment network structure, and framing moderates the effect:** In heterogeneous PGGs, punishment can be ineffective or even harmful due to antisocial punishment and coordination problems (Chen, 2022; Peng & Fan, 2023). Larger groups sometimes see more efficient use of authority (Lim & Zhang, 2020).
- **Punishment technology (severity, targeting, coordination threshold), cost-to-impact ratio, and information/monitoring structure** sharply moderate efficiency effects (Huang et al., 2024; Glöckner et al., 2018; Nicklisch et al., 2021; Hugh-Jones & Perroni, 2017; Mihm & Toth, 2020).
    - *Efficient, targeted, or network-constrained punishment* tends to enable higher efficiency gains.
- **Reward mechanisms or combinations of carrot and stick (especially majority-vote reward)** sometimes outperform punishment in terms of efficiency, especially in heterogeneous groups (Chen, 2022; Peng, 2022).
- **Punishment increases group efficiency most strongly when baseline (control) efficiency is low due to free-riding:** Ceiling effects (i.e., when control is already efficient), additional gains from punishment are negligible or counterproductive (Lim & Zhang, 2020; Kamei et al., 2023).
- **Social context and cultural/normative background affect not only the efficiency of punishment but also its targeting and acceptance** (Gürdal et al., 2021; Kamei et al., 2025; Suleiman & Samid, 2021; Kamei et al., 2023; Kamei, 2024).

---

# 5) Prediction Guidance

**How This Literature Should Inform Prediction of Treatment Efficiency:**

**Direct Prediction Components:**
- **Baseline (Control) Efficiency**: Use empirical no-punishment efficiency as the reference point for estimating the effect of enabling punishment.
- **Game Design Moderators**:
    - **Player Count / Group Size**: Small (e.g., 3-5) groups often support more efficient, targeted enforcement; larger groups may require centralized punishment or authority.
    - **Number of Rounds / Time Horizon**: More rounds (≥ 20–50) favor efficiency gains from punishment; short games (≤ 10 rounds) often see efficiency losses.
    - **MPCR**: Lower MPCR exacerbates free-riding; the effectiveness of punishment is often lower when returns are heterogeneous or low.
    - **Punishment Cost and Effectiveness**: High cost-to-impact ratios (e.g., 1:1) usually erode efficiency gains. Lower-cost, higher-impact punishment, or institutionalized/centralized mechanisms, yield net positive effects.
    - **Punishment Technology**: Mechanisms targeting the lowest contributors, using coordinated or observable punishment, or both observed and unobserved channels, are most likely to raise efficiency.
    - **Monitoring and Information Structure**: Cheap, accurate monitoring is necessary for punishment to improve efficiency (Nicklisch et al., 2021); absence or costly monitoring makes gains unlikely.
    - **Chat and Communication**: Chat alone increases contributions and can substitute for punishment; punishment effects on efficiency are often larger when communication is absent.
    - **Reward/Reward Cost**: The presence of reward may interact, sometimes improving the efficiency impact compared to punishment alone.
    - **Show_n_rounds/Show_other_summaries/Show_punishment_id**: Full transparency can aid or hinder (depending on context) but is less central than other dimensions.
    - **Selection and Framing**: Institutions selected democratically or by voting, or framed with responsibility (vs. authority/power), typically yield stronger gains, especially with gender-based effects (Jiang & Wang, 2024).

**Critical Caveats:**
- **If punishment is likely to be anti-social, mis-targeted, or overused, expect zero or negative efficiency impact even if cooperation rates rise (Botelho et al., 2022; Chen, 2022; Casari & Tavoni, 2024).**
- **In environments with high baseline efficiency, the marginal gain from adding punishment may be small or negative.**
- **Cultural, social, and group-norm factors can dominate or moderate the expected effect, especially in field or cross-cultural settings (Gürdal et al., 2021; Kamei et al., 2025).**
- **Control efficiency is only a reliable predictor when the game design and social context match those in the experimental evidence.**

**In sum:** The downstream prediction should map from control efficiency and the 14 game design dimensions, using moderation logic as detailed above, rather than assuming a universally positive (or negative) efficiency effect from punishment.

---

# 6) Design Dimensions Highlighted Across Papers

### Directly Informed Dimensions:
- **player_count**: Extensively reported and analyzed; group size is central to both mechanism function and efficiency outcomes.
- **num_rounds**: Clear evidence that longer horizons favor positive efficiency effects from punishment.
- **mpcr**: Directly measured and manipulated; its role as a moderator is evident in experimental and theoretical work.
- **punishment_cost**: One of the strongest predictors; the cost-to-impact ratio frequently determines whether efficiency gains are realized or lost.
- **punishment_tech**: Variations (peer vs. centralized, targeted vs. untargeted, requirement for coordination, network structure) are frequent experimental treatments.
- **chat**: Presence/absence and type (free vs. structured) are well studied and shown to affect both baseline and treatment efficiency.
- **show_other_summaries, show_n_rounds**: To some extent, these are manipulated and shown to affect monitoring and strategic play.

### Indirectly or Weakly Informed Dimensions:
- **all_or_nothing**: Some evidence from binary (all-or-nothing) games, but much less than from continuous-contribution games.
- **default_contrib**: Few studies address opt-in vs. opt-out contributing.
- **reward_exists, reward_cost, reward_tech**: Fewer papers directly address reward (vs punishment), though some show that majority-vote rewards can outperform punishment for efficiency.
- **show_punishment_id**: Generally, anonymity prevails; few studies directly compare anonymous vs. identified punishment.
- **network-specific punishment structure**: Some studies provide evidence on network forms (e.g., incomplete networks, circle, decentralized vs. centralized).

### Contextually Discussed or Missing:
- **Interaction of multiple dimensions**: Some important qualitative findings (e.g., authority with female, responsibility framing) highlight the importance of contextual design features (Jiang & Wang, 2024).
- **Repeated institution selection, endogenous adoption, and higher-order punishment**: Sparse but highly informative evidence exists.

---

# 7) Important Limitations

1. **Context-Specificity**: Findings on punishment’s efficiency effect are highly sensitive to experimental design, population (culture, age, profession), and institutional detail. Direct transfer requires close design matching.

2. **Payoff vs. Behavioral Outcomes**: Many studies measure only contributions or compliance, not payoffs/efficiency. In such cases, any inference about efficiency must be carefully qualified.

3. **Short vs. Long Horizon**: Most lab PGGs are relatively short (≤10 periods), while real-world relevance may require consideration of longer-term or repeated interactions.

4. **Absence of Multi-Dimensional Designs**: Few studies systematically cross all 14 design dimensions, leaving gaps for rare or combined stylings (e.g., large groups with chat, rewards, all-or-nothing, and networked punishment).

5. **Reporting Gaps**: Not all empirical papers report both control and treatment efficiency, or do so in a manner that allows for direct calculation of effect size.

6. **Heterogeneity and Antisocial Punishment**: Particularly in culturally or demographically heterogeneous populations, anti-social punishment or poor targeting frequently leads to efficiency losses (even as cooperation rises).

7. **Induced vs. Endogenous Motivations**: Some efficiency gains from punishment may be due to induced compliance (“anticipation of punishment”), rather than actual punishment action or costs—a limitation where compliance, not cost, is measured.

8. **Generalizability**: Results from controlled lab settings may under- or overstate punishment effects compared to naturalistic or field environments.

9. **Uncertainty About Interaction Effects**: Existing literature often varies one or two dimensions at a time; little evidence is available on complex interactions (e.g., punishment × chat × default_contrib × reward_exists).

10. **Limited Adjacent Evidence**: Papers in adjacent domains provide useful mechanism insights but are not always translatable to quantitative prediction in standard PGG contexts.

---

**In summary:**  
The literature provides a rich foundation for predicting how enabling peer punishment will likely affect efficiency in PGG-like environments, conditional on the detailed game design and control efficiency. The effect of punishment is not universally positive; it is strongly moderated (and sometimes reversed) by specific design parameters—especially punishment cost-effectiveness, targeting, monitoring, and the institutional or social context. There is strong evidence for a conditional prediction model, rather than a one-size-fits-all effect. Researchers should be explicit about when their predictions are based on direct payoff outcomes versus behavioral proxies, and recognize the non-trivial risk of efficiency losses due to malfunctioning or costly punishment institutions.
