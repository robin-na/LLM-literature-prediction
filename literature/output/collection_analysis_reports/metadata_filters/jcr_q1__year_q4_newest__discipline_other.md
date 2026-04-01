# 1) Evidence Base

The paper set is predominantly theoretical, with most papers using evolutionary and game-theoretic models, frequently supported by simulation, and only a handful providing empirical or laboratory experimental data. Of the 12 papers, nearly all are theory or simulation-based, with only one clear experimental study (Wei et al., 2025). The evidence base covers a mix of classic public goods games (PGG), spatial/networked social dilemmas, and adjacent coordination or principal-agent environments, with varying attention to punishment, sanctions, and efficiency. Overall, this is a narrow to moderately broad set with regard to the prediction task: only a few papers are directly about PGGs with punishment and efficiency, but several address closely related mechanisms and design choices. Empirical and laboratory data are underrepresented compared to simulation and theoretical arguments.

# 2) Task Relevance

**PGG or Variant:**  
- **Exact:** Two papers directly address PGGs (Vasconcelos et al., 2022; Quan et al., 2023), both with high relevance.  
- **Close/Adjacent:** Several others use related multi-agent, networked, or principal-agent coordination games, sometimes with continuous or all-or-nothing actions (e.g., Wei et al., 2025; Li & Jiang, 2023). Some are spatial or dyadic variants (Jia et al., 2023; Goodman, 2023).
- **Weak/None:** A subset are set in the Prisoner’s Dilemma or mutualism settings not directly modeled as PGGs (e.g., Wang et al., 2022; Lean & Jones, 2023).

**Punishment or Sanctions:**  
- **Exact/Close:** Several theory and modeling papers address punishment or sanctioning mechanisms directly (Vasconcelos et al., 2022; Quan et al., 2023; Li & Jiang, 2023; Wei et al., 2025; Jia et al., 2023).
- **Adjacent/Weak:** Some discuss sanction-like effects (e.g., job rotation as implicit punishment in Wei et al., 2025), but some papers entirely lack punishment or sanctioning features (Wang et al., 2022; Li et al., 2022; Zhu et al., 2023).
- **None:** Four papers do not include punishment/sanctioning at all.

**Efficiency or Related Payoff Outcome:**  
- **Exact:** Two theory papers (Vasconcelos et al., 2022; Li & Jiang, 2023) and one empirical paper (Wei et al., 2025) report efficiency or close group payoff measures directly.
- **Close/Adjacent:** Some use non-payoff behavioral outcomes to infer likely changes in efficiency, but do not report efficiency or group payoff directly (Quan et al., 2023; Jia et al., 2023).
- **Weak/None:** The majority report only cooperation or contribution rates, not efficiency per se.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes:**  
  - *Efficiency/Group Payoff:* Only a minority of papers directly report efficiency (group payoff relative to full cooperation) as their primary outcome (Vasconcelos et al., 2022; Li & Jiang, 2023; Wei et al., 2025).
  - *Related Measures:* Some report "group earnings," "welfare," or "surplus," generally interpreted as comparable to efficiency within the context.

- **Non-Payoff Behavioral Outcomes:**  
  - *Cooperation/Contribution Rates:* Most modeling work focuses on stead-state cooperation densities, contribution frequencies, or similar, but these are not payoff measures.
  - *Punishment Frequency/Norm Compliance:* Some studies report how often punishment is used, but do not link this mechanistically to efficiency or payoffs.
  - *Mechanistic or Theoretical Constructs:* Several papers focus on how learning, network structure, or institutional scale affect the prevalence or stability of cooperation, without quantitative payoff reporting.

# 4) Main Findings Relevant To Prediction

1. **Punishment Typically Increases Efficiency—With Key Moderators:**  
   - When punishment institutions are well-matched to the scale of the public good and adopted collectively, they reliably increase cooperation and group efficiency, substantiated by both theory and meta-analysis (Vasconcelos et al., 2022). Individual-level punishment works best only in "local" PG scenarios.
   - Poor alignment between institution and public good (e.g., individual sanctions for global goods) or poor learning/information environments may undermine or reverse efficiency gains (Vasconcelos et al., 2022).

2. **Punishment Mechanism Details Matter:**  
    - Graded punishment (cost/fine structures that escalate with repeated defection) is more effective than fixed punishment for sustaining high cooperation, especially when punishment cost is low relative to the fine (Quan et al., 2023), though the main outcome is cooperation, not efficiency.
    - The costliness of punishment to the punisher is consistently a key moderator—high punishment costs can erase efficiency benefits or reverse them (Quan et al., 2023; Li & Jiang, 2023).

3. **Punishment Alone May Not Be Sufficient:**  
    - Complex environments (e.g., multi-level governance or principal-agent settings) show that combining punishment with reward or monitoring institutions may be necessary for large efficiency gains; single tools have limited effect alone (Li & Jiang, 2023).

4. **Behavior-Outcome Gap and Detection Limitations:**  
    - High measured cooperation/contribution rates in punishment treatments do not guarantee correspondingly high efficiency; undetected or covert free-riding may persist and limit real payoff gains (Goodman, 2023).

5. **Empirical Confirmation in Adjacent Settings:**  
    - Laboratory evidence (Wei et al., 2025) from a principal-agent experiment supports the broader claim: introducing a costly punishment option (even if not always exercised) can substantially increase efficiency, especially when punishment is credibly external/imposed.

# 5) Prediction Guidance

- **Punishment, when enabled in PGG-like games, generally increases efficiency relative to control, particularly when (a) the punishment mechanism is sufficiently collective to match the scale of the public good, (b) the punishment cost is not too high, and (c) there is enough information or memory ("learning opportunities") for institution adoption and effectiveness (Vasconcelos et al., 2022; Li & Jiang, 2023).**
- **Magnitude of gain depends on:**
  - **Punishment Cost relative to Fine/Magnitude:** Lower cost and/or higher penalty yield greater efficiency gains, but excessive punishment (high costs) can reduce or reverse benefits (Quan et al., 2023; Li & Jiang, 2023).
  - **Mechanism Details:** Graded or contingent punishment mechanisms outperform static/fixed approaches (Quan et al., 2023), which suggests that `punishment_tech` and related parameters matter.
  - **Combining Tools:** Combining punishment with rewards, compensation, or additional institutional support maximizes efficiency (Li & Jiang, 2023).
  - **Potential Behavior-Payoff Disconnect:** In some designs, observed increases in cooperation may overstate efficiency gains (Goodman, 2023).
- **If the control efficiency (with punishment disabled) is already high, absolute efficiency gains from punishment will be smaller. When control efficiency is low, especially due to strong free-riding, the potential for punishment-enabled increases is larger (Vasconcelos et al., 2022; Li & Jiang, 2023).**

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**  
- `player_count`: Explicit in all core theory/empirical PGG and network models—affects both institution scale and cooperation stability (Vasconcelos et al., 2022; Quan et al., 2023).
- `num_rounds`: Salient in dynamic models and meta-analyses examining sustainability and learning (Vasconcelos et al., 2022).
- `mpcr`: Directly analyzed as "enhancement factor" or equivalent; higher MPCRs typically support higher baseline efficiency (Vasconcelos et al., 2022; Quan et al., 2023).
- `punishment_cost`: Central in theory and simulation—lower cost to punisher correlates with higher likely efficiency gains (Quan et al., 2023; Li & Jiang, 2023).
- `punishment_tech`: Graded/contingent vs. fixed punishment structures are explicitly compared in models (Quan et al., 2023; Vasconcelos et al., 2022).
- `show_other_summaries`, `show_n_rounds`: Information transparency and learning/memory opportunities are key moderators in theory (Vasconcelos et al., 2022).

**Indirectly Informed:**  
- `all_or_nothing`, `chat`, and `default_contrib`: Mentioned in some models as game structure or framing, but not systematically studied as moderators of efficiency effects of punishment.
- `reward_exists`, `reward_cost`, `reward_tech`: Reward tools are discussed as complementary interventions (Li & Jiang, 2023) but are less frequently the primary focus.

**Only Contextually Discussed or Sparse:**  
- `show_punishment_id`: Little systematic treatment, though models sometimes assume information about punishment assignment.
- `default_contrib`: Some mention of initial propensities or statuses in agent-based models, but not tied to efficiency-outcome prediction.
- `chat`: Examined as behavioral context (Wei et al., 2025), but not as a central variable affecting efficiency impact of punishment.

**Effectively Missing:**  
- Several dimensions (detailed reward mechanisms, punishment identity visibility, default contribution) are either absent, only touched upon incidentally, or not linked to efficiency outcomes.

# 7) Important Limitations

- **Empirical Evidence is Scarce:** Most results are theoretical or simulation-based; a dearth of laboratory evidence limits empirical generalizability.
- **Few Papers Directly Measure Efficiency:** Most studies focus on cooperation/contribution rates as their outcome; only a minority report or model efficiency/group payoff directly, which constrains the evidence base for payoff-based prediction.
- **PGG-Specific Mechanisms Sometimes Inferred from Adjacent Settings:** Several influential findings come from PD, networked, or principal-agent games, requiring interpretive inference to standard PGG environments.
- **Game Design Parameterization is Incomplete:** While some core dimensions are well studied (player count, punishment cost, mechanism type), others central to the prediction task (e.g., explicit information and reward structures, identity visibility, communication) are rarely examined directly.
- **Behavioral-Outcome Disconnect Cautions:** Theory highlights that improved cooperation rates via punishment do not always translate to higher group efficiency, especially if undetected or covert defection remains possible (Goodman, 2023).
- **Context and Learning Effects are Under-specified:** The impact of information flow, historical memory, and institutional adoption rules are flagged as important moderators, but laboratory and cross-study evidence remain limited here.
- **Divergences in Model Assumptions:** Some findings derive from stylized models (e.g., spatial structure, job rotation as punishment) and may not transfer simply to standard laboratory PGGs.

---

**References (key for findings, APA format):**

- Vasconcelos, V. V., Dannenberg, A., & Levin, S. A. (2022)
- Quan, J., Chen, X. Y., Yang, W. J., & Wang, X. J. (2023)
- Li, J. M., & Jiang, S. S. (2023)
- Wei, J., Zhong, Z. W., Chen, H. R., Arango-Aramburo, S., & Zhao, X. L. (2025)
- Goodman, J. R. (2023)
- Jia, C., Zhang, R. X., & Wang, D. (2023)
