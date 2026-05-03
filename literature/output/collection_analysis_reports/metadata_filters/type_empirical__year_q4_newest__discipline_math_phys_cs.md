# 1) Evidence Base

The paper set comprises 26 papers, with the majority being **empirical, lab experimental studies** on social dilemmas, public goods games (PGGs), close variants (like trust games, minimum effort games, and team investment games), as well as several **adjacent contexts** (e.g., mart-reinforcement learning agents, real-world norm enforcement, bibliometric analyses). Most experiments involve standard game-theoretic manipulations of group size, rounds, punishment/reward options, and information feedback.

**Strengths:**
- Several papers (**~8**) provide **exact and direct empirical evidence** on the effect of peer punishment on efficiency in standard PGGs or direct variants.  
- Some studies **systematically manipulate design dimensions** (e.g., punishment network structure, team vs. individual decision-making, type of sanctioning institution, migration openness).
- Empirical focus is strong, with very few theoretical-only or meta-analytic papers.

**Limitations:**
- The set is **broad in coverage of social dilemmas**, but for the **precise prediction task**—treatment efficiency in PGGs when enabling punishment—coverage is **less comprehensive** for certain dimensions (e.g., chat, framing, reward mechanisms).
- Many studies with **adjacent or weak relevance** address trust games, coordination games, or PDG variants, rather than standard multi-player PGGs.
- Some studies only report **behavioral outcomes** (e.g., contribution rate), not group payoff or efficiency.

---

# 2) Task Relevance

Relevance is assessed on three target dimensions:

### A. `pgg_or_variant`  
- **Exact**: About 7–8 papers use standard repeated or single-shot PGGs.
- **Close**: Several papers employ true variants (minimum effort, collective-risk, delegation games).
- **Adjacent/Weak/None**: Trust games, dyadic PDG, volunteering games, multi-agent MARL, or network games make up the remainder.

### B. `punishment_or_sanctions`  
- **Exact/Close**: Over half the set manipulates peer punishment or institutional sanctions directly.
- **Adjacent**: Some focused on reward-only, or on other cooperation mechanisms without direct punishment.
- **None/Weak**: A handful do not involve any sanction mechanism and are context-only.

### C. `efficiency_or_related_payoff_outcome`  
- **Exact**: Only a subset directly reports **efficiency** (ratio of earnings or group payoff to maximum cooperative payoff).
- **Close/Adjacent**: Others report total/group payoff or welfare, which can be mapped but not always cleanly; some only report contribution rates or behavioral proxies.
- **Weak/None**: Several papers provide no payoff or efficiency data.

**Summary:**  
There is **direct, high-quality evidence** for the prediction task in standard PGGs with peer punishment (e.g., Bahbouhi et al., 2024; Pi et al., 2022; Cobo-Reyes et al., 2022; Wang & Huang, 2022). Adjacent evidence from coordination, trust, delegation, and principal-agent games provides additional—but less direct—support or qualification.

---

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes:**
- **Group Efficiency** (i.e., group payoff as a fraction of the maximum): explicitly measured in most exact-relevant PGG studies.
- **Total Group Payoff/Welfare**: sometimes reported instead of normalized efficiency.
- **Average Individual Payoff**: often used as a proxy for group efficiency, especially when group sizes are homogeneous.

**Behavioral Outcomes (Non-Payoff):**
- **Contribution/Cooperation Rates**: universally reported.
- **Punishment Frequency/Assignment**: frequency or targeting of punishment, with some studies detailing anti-social vs. pro-social uses.
- **Norm Compliance**: adherence to specified contribution or behavioral norms.
- **Partner Selection**: changes in network structures or partner choice (in dynamic and networked games).
- **Voting/Preference for Sanctioning Institutions**.

**Distinguishing Note:**  
Several papers report *only* behavioral outcomes, requiring inference about efficiency gains from contribution increases (e.g., Pancotto et al., 2023; Shuvo & Kabir, 2024).

---

# 4) Main Findings Relevant To Prediction

## Synthesis Across Papers

### General Effect of Peer Punishment
**In standard repeated PGGs with peer punishment:**
- **Enabling peer punishment typically increases group efficiency compared to no-punishment baseline** (Bahbouhi et al., 2024; Pi et al., 2022; Wang & Huang, 2022). The effect is mediated through increased contributions and—when punishment is well-targeted—limited wasteful punishment expenditure.

### Moderators and Qualifiers

- **Decision Rule / Group Structure:**  
  Unanimity teams filter out destructive punishment, achieving higher efficiency than individuals or majority-rule teams (Bahbouhi et al., 2024).
- **Punishment Network Structure:**  
  Incomplete networks (e.g., circle, pairwise) can yield higher efficiency than allowing everyone to punish everyone due to reduced punishment abuse and bystander effects (Pi et al., 2022).
- **Sanctioning Institution (Formal vs. Informal):**  
  Formal (centralized) punishment mechanisms produce higher efficiency than informal peer punishment, particularly in open societies with member migration (Cobo-Reyes et al., 2022).
- **Observability:**  
  Punishment increases efficiency regardless of whether sanctions are observable during play (Wang & Huang, 2022).
- **MPCR Heterogeneity:**  
  Efficiency gains may be larger or more robust in homogeneous MPCR groups; heterogeneity introduces challenges (Peng, 2022; Pi et al., 2022).
- **Antisocial Punishment:**  
  Less prevalent or less costly antisocial punishment is associated with higher efficiency gains (Bahbouhi et al., 2024).
- **Game Variant:**  
  In collective-risk PGGs, strong punishment must be credible/frequent (high risk) to realize efficiency gains; otherwise, the effect is weak (Jiang et al., 2023).

### Contrasts/Limitations from Adjacent Games

- **Trust/Game Variants:**  
  In some trust or team investment games, enabling punishment does **not** improve, or may even reduce, efficiency due to direct punishment costs outweighing gains in behavior (Herne et al., 2022; Calabuig et al., 2024).
- **Coordination Games:**  
  In minimum effort (weakest-link) games, voluntary costly punishment increases coordination and ultimately, efficiency (Lec et al., 2023); but this may be context-specific.
- **Institutional Framing:**  
  In principal-agent (management) games, punishment raises efficiency only with strong institutional support and norm coordination (Macleod et al., 2025).

### Inference from Non-Payoff Outcomes:
- When only cooperation or contribution rates increase, **inference about efficiency gains is justified when (i) punishment is not too costly**, and **(ii) antisocial or misapplied punishment is rare** (Pancotto et al., 2023; Shuvo & Kabir, 2024).

---

# 5) Prediction Guidance

Based on the synthesized literature, **predictions of treatment efficiency (when enabling peer punishment in PGGs) from game design plus control efficiency should be guided by:**

- **Positive Efficiency Effect Typical:**  
  *Enabling peer punishment in standard repeated PGGs typically increases efficiency relative to control*, though the effect size is moderate and context-dependent (Bahbouhi et al., 2024; Wang & Huang, 2022).

### Design Dimensions That Modulate the Effect:

- **Group Structure/Decision Rule:**  
  If the group acts as a team with strong coordination requirements (e.g., unanimity rule), the efficiency gain from punishment is **greater** than among individuals—a feature not always present in standard PGGs.
- **Punishment Network / Technology:**  
  The ability for all to punish all is **not always optimal**; restricting punishment (e.g., to incomplete networks or requiring coordination) can increase efficiency by minimizing excessive and redundant punishment (Pi et al., 2022).
- **Sanction Type and Institution:**  
  Formal, centralized punishment often achieves **higher efficiency** than informal, decentralized peer punishment, especially in contexts with migration (Cobo-Reyes et al., 2022).
- **Control Efficiency as Baseline:**  
  The control (no-punishment) efficiency is often predictive of the likely gain; settings with already-high efficiency see smaller improvements.
- **Cost and Magnitude of Punishment:**  
  If punishment is *not* prohibitively costly relative to its deterrence benefit, efficiency gains from punishment are more likely; high punishment costs can neutralize or reverse efficiency gains (Herne et al., 2022; Calabuig et al., 2024).

### Caveats:

- **Payoff Gains Are Not Guaranteed in Adjacent Games:**  
  In binary-contribution, asymmetric, or certain trust/coordination games, punishment can fail to raise or even reduce efficiency, particularly if punishment is misapplied or overused.
- **Behavioral-only Studies:**  
  Where only contribution or cooperation rates are available, careful inference is required: improvements in these rates likely—but not always—translate to efficiency if punishment costs are low.

---

# 6) Design Dimensions Highlighted Across Papers

**Dimensions Directly Informed:**
- player_count: Manipulated/reported in nearly all PGG or variant experiments.
- num_rounds: Standard in repeated games.
- all_or_nothing: Many studies specify binary or continuous contributions.
- mpcr: Almost always reported as a central design/parameter variable.
- punishment_cost and punishment_tech: Thoroughly manipulated in several key studies (e.g., cost-to-fine ratios, network type, centralized vs. peer punishment).
- show_n_rounds, show_other_summaries: Information feedback is common, though not uniformly highlighted.
- reward_exists, reward_cost, reward_tech: Addressed primarily in studies on reward or combined mechanisms (Peng, 2022), but less frequent for cross-punishment comparisons.
- chat: Explicitly manipulated or held constant (more often no chat).
- default_contrib, show_punishment_id: Rarely manipulated; only contextually mentioned in a few papers.
- punishment_exists: Central to prediction task; always specified.

**Dimensions Only Contextually Discussed or Sparse:**
- chat: Typically absent, but effect of communication is sometimes addressed in adjacent or control conditions.
- default_contrib: Framing effect is rarely a treatment variable.
- show_punishment_id: Whether punishment is anonymous or not is inconsistently manipulated or reported.
- reward mechanism: Independent reward is less often studied in direct comparison to punishment.

---

# 7) Important Limitations

- **Coverage Gaps:**  
  Several design dimensions (e.g., chat, default contribution framing, reward parameters, anonymity of punishment/reward) are sparsely addressed; predictions for these require extrapolation or carry high uncertainty.
- **Heterogeneity in Outcome Reporting:**  
  Many studies report only behavioral or non-payoff outcomes (e.g., contribution rates), or use adjacent/variant game structures, making quantitative predictions of efficiency less reliable.
- **Lack of Meta-Analysis:**  
  No aggregate quantitative synthesis or effect-size distribution is provided across contexts; heterogeneity between study contexts and procedures remains high.
- **Context-Dependence:**  
  Efficiency effects of punishment **vary by team/individual decision, institution, network structure, and game variant**; generalization outside standard repeated PGGs must be cautious.
- **Ambiguity in Adjacent Games:**  
  In trust, investment, and certain coordination games (adjacent to PGGs), punishment sometimes fails to improve or even reduces efficiency, especially when punishment is costly, misapplied, or overused.
- **Baseline Control Data Sometimes Missing:**  
  Not all studies report control (no-punishment) efficiency for direct comparison.

---

**In sum:**  
The literature provides robust, directly relevant evidence that, in standard repeated PGGs, enabling peer punishment—when not prohibitively costly and not open to widespread misapplication—**usually increases group efficiency**, with the magnitude of improvement moderated by several game design features. However, substantial caution is warranted in extrapolating to adjacent game types, or when design features (punishment cost, coordination, reward/punishment structure, communication) depart from standard laboratory PGG paradigms. Design dimensions most critical to prediction are punishment technology (network and cost), team/individual structure, institutional context, and baseline efficiency. Several dimensions are poorly covered and predictions for those contexts are inherently more uncertain.
