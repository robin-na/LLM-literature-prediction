# 1) Evidence Base

The paper set comprises a moderately broad mix of 25 papers, with a substantial empirical (mainly laboratory experimental) focus and a smaller but meaningful theory/modeling component. Most empirical studies utilize variations of repeated linear public goods games (PGG), though some extend to field settings or to adjacent social dilemma paradigms (e.g., weakest-link games, common pool resources, or dyadic trust/dictator games). Several theory papers address repeated social dilemmas broadly, including but not limited to PGG-like settings.

For the downstream prediction task—mapping game design dimensions plus control (no-punishment) efficiency to expected punishment-enabled efficiency—this set is much stronger for standard, linear, multi-player laboratory PGGs than for more complex, nonlinear, or naturally occurring environments. Empirical findings dominate, but several widely-cited theoretical arguments supplement and help interpret these results. Overall, direct measurement of efficiency or related group/payoff outcomes is moderately well-covered in the exact PGG domain but sparser or inferred in adjacent settings.

# 2) Task Relevance

**pgg_or_variant:**  
- *Exact*: The core of the set includes many standard PGG lab experiments (e.g., Kuwabara & Yu, Andrighetto et al., Fatas & Mateu, Dorrough et al., Fischer et al.), as well as some theory tailored to PGGs (Chen & Perc).
- *Close*: Several empirical and theoretical papers use close PGG variants (e.g., provider-beneficiary games, nonlinear CPRs in Cason & Gangadharan, or threshold/public-good dilemmas) where mechanisms are similar but outcomes may not fully generalize.
- *Adjacent/Weak*: Some studies analyze adjacent games (Prisoner’s Dilemma, trust and dictator games, or real-world/field norm violation contexts) or focus on general norm enforcement, which provides context but not direct prediction value.

**punishment_or_sanctions:**  
- *Exact*: Many studies directly manipulate and compare punishment-enabled and no-punishment conditions.
- *Close*: A subset includes reward alongside punishment, or examines counter-punishment.
- *Adjacent/Weak*: A few contextualize through indirect social exclusion, reputation, or information about violation, which may moderate behaviors analogous to punishment but are not institutional sanctions per se.

**efficiency_or_related_payoff_outcome:**  
- *Exact*: Several experiments measure group efficiency (as ratio of actual to maximal possible group earnings), total payoff, or surplus as a primary dependent variable.
- *Close*: Others provide detailed contribution/cooperation rates in linear PGGs, which map closely to efficiency in those cases.
- *Adjacent/Weak/None*: Some report only behavioral outcomes like punishment frequency, norm compliance, or propensity to cooperate, without reporting payoff-based outcomes.

**Summary:**  
The set is highly relevant for the target (punishment and efficiency in standard PGGs), but coverage is sparser or indirect for complex, nonlinear, or non-lab environments, or for nuanced institutional innovations (e.g., networked sanctions, complex information structures).

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes** (directly connected to "efficiency" as defined for prediction):  
  - **Group earnings**, **group efficiency** (earnings as proportion of full-cooperation optimum), **total surplus**, or **welfare** are directly reported in several key experiments (Kuwabara & Yu, Fischer et al., Andrighetto et al., Fatas & Mateu, Dorrough et al., Lierl, Cason & Gangadharan). Some theory papers explicitly model average group payoff or efficiency from behavioral strategy equilibria (Antoci & Zarri, Camera & Gioffré).
  - *Note*: In games with linear contribution-to-benefit mappings, average contribution rates can be taken as a close proxy for efficiency; this is less reliable in nonlinear or weak-link variants.

- **Non-payoff behavioral outcomes** (important for mechanism but *not* the same as efficiency):  
  - **Contribution rates**, **cooperation rates**, **punishment frequency**, **antisocial punishment**, **trust**, **norm compliance**, and **participation** are frequently measured (see e.g., Irwin et al., Nelissen & Mulder, Seip et al., Mieth et al., Berger & Hevenstone, Myers, Lyle, Eriksson et al.).
  - Studies using only these measures (especially without direct mapping to payoff) must be explicitly distinguished from those reporting efficiency.

- **Contextual or mechanism outcomes**:  
  - **Anger**, **legitimacy of punishment**, **social acceptability**, or **cognitive responses** form the focus in a few (Seip et al., Eriksson et al., Corgnet et al.)

# 4) Main Findings Relevant To Prediction

### On enabling punishment in PGGs:

- **Punishment's effect is highly context-dependent:**
    - **Centralization and cost matter:** Centralized, costly punishment (e.g., designated punishers) tends to increase efficiency and prosocial punishment, while costless or decentralized (peer-to-peer) punishment often leads to excessive, wasteful "punishment wars" and lower efficiency (Kuwabara & Yu; Fischer et al.).
    - **Production technology is crucial:** Linear PGGs may see little or no efficiency gain from punishment where antisocial punishment is common. In weakest-link (complementary output) games, punishment can sharply increase efficiency by moving groups to high-output equilibria (Fatas & Mateu).
    - **Information environment influences effect:** Poor or noisy information can reduce the positive effects of punishment on efficiency. Centralization helps mainly under moderate noise; with perfect information, decentralized punishment does not outperform control (Fischer et al.).
    - **Power structure stability:** Instability/inequality in punishment power (i.e., dynamic assignments, strong/weak punishers) can undermine efficiency, even compared to no-punishment or stable/equal-punishment systems, by encouraging wasteful contests for power (Dorrough et al.).
    - **Communication as moderator:** Allowing communication (chat or normative messaging) alongside punishment increases efficiency substantially, both by raising cooperation and by neutralizing the negative feedback from counter-punishment; absence of communication allows counter-punishment to erode or negate efficiency gains (Andrighetto et al.).
    - **Network structure and roles:** Who can punish whom dramatically changes efficiency impacts. Beneficiary-only sanctioning improves efficiency; when providers or other parties can also participate in punishment, this benefit disappears or reverses (Lierl).
    - **Game payoff structure (nonlinearity) matters:** In nonlinear common pool games, peer punishment does *not* improve efficiency, in contrast to its effect in linear games. Communication has a massive positive effect, making punishment redundant (Cason & Gangadharan).
    - **Heterogeneity and cross-cultural variation:** Cultural norms and behavioral heterogeneity (antisocial punishers, trust, reciprocity expectation) can limit or reverse the efficiency benefit of punishment (Fatas & Mateu; Antoci & Zarri; Eriksson et al.).

- **Theory/modeling insights:**  
    - Punishment generally supports efficiency if cooperators/punishers are numerous enough (Antoci & Zarri; Camera & Gioffré).
    - The benefit disappears or reverses when there is significant antisocial punishment, when reciprocal or symmetric strong reciprocity removes incentive to cooperate, or when reward undermines punishers’ credibility (Antoci & Zarri).
    - Equilibria sustaining high efficiency require sufficient "breadth of monitoring," moderate punishment costs, and patient players (Camera & Gioffré).

- **Empirical findings in non-standard or adjacent settings** (included for completeness):  
    - Prosocial motivation, external context (e.g., media exposure), and reputation can affect baseline cooperation rates, but do not directly change efficiency in punishment-enabled contexts (Cardador et al., Lyle, Pfattheicher, etc.).
    - Antisocial punishment (punishing cooperators or excessive mutual punishment) is a robust threat to efficiency gains.

# 5) Prediction Guidance

- **Direct predictions should strongly weight which PGG design is used:**
    - *Linear, repeated PGG, with peer punishment*: Expect variable to small or even negative changes in efficiency, especially if antisocial punishment is prevalent (Fatas & Mateu, Dorrough et al., Fischer et al.).
    - *Linear, repeated PGG, with costly, designated punishment*: Expect positive efficiency gains, especially if punishment is legitimized by cost and centralization (Kuwabara & Yu).
    - *Complementary/weakest-link public good*: Punishment reliably produces strong efficiency increases (Fatas & Mateu).
    - *Nonlinear CPR (common pool resource)*: Do not expect efficiency gains from peer punishment; prediction should lean toward no change or possible waste (Cason & Gangadharan).
    - *Communication enabled*: Predict positive synergy—communication amplifies or restores the efficiency gains from punishment, especially in the presence of counter-punishment risk (Andrighetto et al., Cason & Gangadharan).
    - *Instability/inequality in punishment power*: If punishment assignment is unstable/unequal, expect lower or even negative effects on efficiency (Dorrough et al.).
    - *Networked/role-based sanctioning*: Pay careful attention to sanctioning architecture—efficiency gains are highest when only some roles (e.g., beneficiaries) can punish (Lierl).

- **Control (baseline, no-punishment) efficiency is a weak but necessary anchor:**  
    - When control efficiency is already high, punishment is less likely to add significant gains and more likely to provoke wasteful or antisocial punishment.
    - When control efficiency is low (e.g., in weakest-link games or with very low MPCR), the design details of punishment (cost, centralization, and communication) become the main determinants of whether efficiency can be rescued.

- **Dimension-by-dimension effects (see below) must be carefully considered.**

- **Outcomes based solely on contributions, cooperation rates, or punishment frequency should not be directly mapped to efficiency unless game linearity is confirmed (see section 6).**

# 6) Design Dimensions Highlighted Across Papers

**Directly informed:**  
- `player_count`: Covered in nearly all empirical papers; known to modulate ease of sustaining cooperation but no clear non-monotonic effect on efficiency gain from punishment.
- `num_rounds`: Extensively manipulated; longer games allow punishment-credibility effects and learning but can also allow negative effects from repeated mutual punishment in peer punishment conditions.
- `punishment_cost`: Explored deeply; higher costs can foster legitimacy (Kuwabara & Yu), reduce antisocial punishment, but, if too high, may deter beneficial punishment.
- `punishment_tech` (who can punish whom, centralized/peer): Strong, direct evidence on importance (Kuwabara & Yu, Fischer et al., Dorrough et al., Lierl).
- `mpcr`: Varies across studies; efficiency impact of punishment sometimes depends on whether MPCR is high enough to make cooperation sustainable.
- `chat`: Communication repeatedly shown to amplify efficiency impact of punishment (Andrighetto et al., Cason & Gangadharan).

**Indirectly informed:**  
- `all_or_nothing` (vs. continuous): Some studies use binary contribution games or threshold games (Fatas & Mateu, Park et al.), showing that effect of punishment can differ from continuous.
- `show_n_rounds` (information about time horizon): Some effect on backward induction and strategic behavior (Camera & Gioffré; Martin et al.).
- `show_other_summaries`: Some evidence on information effects (Martin et al., Fischer et al.), but less targeted analysis.
- `show_punishment_id`: Limited but relevant for reputation or social punishment (Eriksson et al., Nelissen & Mulder).

**Scarcely covered or missing:**  
- `default_contrib`: Not explicitly manipulated in this set.
- `reward_exists`, `reward_cost`, `reward_tech`: Covered in few theory and empirical papers (Antoci & Zarri, Nelissen & Mulder, Lierl), primarily as secondary mechanisms rather than predictors of treatment efficiency.
- `show_other_summaries`: Occasionally relevant for monitoring and retaliation (Camera & Gioffré, Andrighetto et al.); not a central focus.
- Many “behavioral economics” mechanism papers in this set do not systematically manipulate all 14 dimensions.

# 7) Important Limitations

- **Sparse direct evidence on efficiency in non-linear, naturalistic, or large-scale real-world settings:** Most findings are based on small, homogeneous lab groups with simple, linear payoffs.
- **Much evidence on behavioral, not payoff, outcomes:** A significant fraction of the literature measures cooperation, contribution rate, or norm compliance, not efficiency/welfare; mapping from cooperation to efficiency can be unreliable outside linear games.
- **Heterogeneity in punishment implementation:** Institutions (peer vs. centralized, stable vs. unstable roles) vary across studies, making direct comparison and generalization risky.
- **Cultural and demographic moderators are largely untreated in quantitative form:** Some indication that antisocial punishment varies by context (Fatas & Mateu; Eriksson et al.), but not systematically mapped to design dimensions.
- **Secondary dimensions (e.g., defaults, framing, observation of punishers, explicit reward tech) remain underexplored as efficiency moderators; hence, prediction in their presence requires extrapolation or caution.**
- **Use of theory is necessary in many cases to link behavioral/proxy outcomes to efficiency or to extend prediction to under-studied design combinations, but these extrapolations should be flagged as requiring additional empirical support.**
- **Ambiguity and disagreement:** There is clear evidence of mixed or even negative effects of punishment on efficiency under certain institutions (costless or decentralized punishment, unstable roles, high antisocial punishment cultures), so defaulting to "punishment raises efficiency" is unwarranted.

---

**In summary:**  
The literature base for the prediction of treatment efficiency from game design and control efficiency in PGG or similar environments is good but not comprehensive. Certain game design dimensions—particularly punishment institution, cost, and the presence of communication—are critical moderators, and their effects are well-documented in efficiency terms for standard laboratory PGGs. The effect becomes ambiguous, absent, or negative in nonlinear settings, under unstable punishment roles, or where antisocial punishment prevails. Design dimensions such as defaults, detailed feedback structures, or explicit reward mechanisms are only sparsely covered, so prediction in those areas must be cautious and qualified. Many studies report on behavioral outcomes rather than direct efficiency or group payoff, and these should be treated as indirect evidence except in linear games. Ambiguity remains in the cross-paper findings, which should be preserved and reflected in predictive applications.
