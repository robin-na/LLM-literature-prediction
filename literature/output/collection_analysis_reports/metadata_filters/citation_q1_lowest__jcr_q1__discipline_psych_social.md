# 1) Evidence Base

This literature set is both **empirically rich and well-aligned** with the prediction task: it includes a mix of experimental lab studies, field experiments, agent-based/evolutionary models, and theory papers. Of the 73 papers, a substantial subset directly evaluates public goods games (PGGs) or structurally close variants and empirically measures *payoff-derived efficiency* outcomes. The evidence spans **multiple types of punishment (peer, centralized, collective, third-party), monitoring technologies, transparency, group structure, and institutional context**. The set is strongest on standard repeated linear PGGs and closely related designs, with some papers making explicit efficiency comparisons between no-punishment and punishment conditions. Several meta-analyses and reviews synthesize evidence across multiple studies. Theory papers and modeling studies complement the experimental evidence, offering mechanistic insights and highlighting moderators. Some papers focus only on contributions or norm compliance (not efficiency), and a substantial number are only contextually relevant, not directly speaking to efficiency or punishment.

# 2) Task Relevance

**pgg_or_variant:**  
- *Exact*: Numerous studies use standard repeated PGGs or close analogs, including those manipulating player count, rounds, MPCR, and punishment/monitoring mechanisms (e.g., Castillo & Hamman, 2021; Krügel & Maaser, 2025; Duell et al., 2024; Chen et al., 2025; Kanitsar, 2019; Kroupa, 2014; Jin, Spadaro et al., 2025).
- *Close*: Some use generalized exchange, CPR games, or repeated PDs with analogous punishment structures (e.g., Milinski & Marotzke, 2022; Asgharpourmasouleh et al., 2017).
- *Adjacent–Weak*: A minority study adjacent contexts (ultimatum, dictator, leadership, or partner-choice games).
- *None*: Several, especially conceptual and field observation papers, do not use PGGs.

**punishment_or_sanctions:**  
- *Exact*: Many papers experimentally manipulate the **presence, cost, type, and credibility** of punishment (peer, centralized, collective, third-party, etc.), often using toggles analogous to `punishmentExists` (e.g., Castillo & Hamman, 2021; Duell et al., 2024; Krügel & Maaser, 2025).
- *Close–Adjacent*: Some explore reward, reputation, norm enforcement, or indirect/antisocial punishment, less common in standard PGGs.
- *None*: Some focus on non-sanctioning mechanisms only.

**efficiency_or_related_payoff_outcome:**  
- *Exact*: Several studies directly report **group efficiency**, **total payoff**, or **welfare** between punishment-enabled and baseline (e.g., Castillo & Hamman, 2021; Krügel & Maaser, 2025; Chen et al., 2025; Duell et al., 2024; Asgharpourmasouleh et al., 2017).
- *Close–Adjacent*: Many report group earnings or average payoff, sometimes indirectly, or require inference from contribution rates and punishment costs.
- *Weak/None*: Others report only individual behavior, norm compliance, or attitudinal outcomes.

# 3) Outcomes Measured in the Literature

- **Payoff-Related Outcomes:**
    - **Group efficiency:** Directly as the ratio of total earnings to fully cooperative maximum (Castillo & Hamman, 2021; Krügel & Maaser, 2025; Duell et al., 2024; Chen et al., 2025; Asgharpourmasouleh et al., 2017).
    - **Total group payoff/earnings:** Frequently reported or can be reconstructed from experiment details.
    - **Surplus/welfare:** Sometimes calculated, sometimes inferred.

- **Non-Payoff Behavioral Outcomes:**
    - **Contribution rates, cooperation rates, norm compliance:** Treated as proxies but distinct from efficacy; commonly measured.
    - **Punishment rates, antisocial vs. prosocial punishment, norm enforcement, voter preferences.**
    - **Solidarity, norm perceptions, beliefs, attitudes:** Sometimes related, but not payoff-based.

It is essential to recognize when literature provides only contribution-level results rather than efficiency—**increases in cooperation do not necessarily translate to improved efficiency** if punishment is too costly or misapplied.

# 4) Main Findings Relevant to Prediction

**Empirical Evidence:**
- **Enabling punishment generally increases group efficiency compared to baseline,** but the size and even the *direction* of the effect are *strongly contingent* on game design dimensions (Castillo & Hamman, 2021; Krügel & Maaser, 2025; Chen et al., 2025; Asgharpourmasouleh et al., 2017).
    - **Centralized and collective punishment**—especially when pre-committed and participatory—show robust efficiency gains (Duell et al., 2024; Castillo & Hamman, 2021).
    - **Peer-to-peer punishment** increases cooperation but not always efficiency—when monitoring is imperfect (noisy), or when antisocial punishment is present, costly punishment can offset gains or worse (Kroupa, 2014; Duell et al., 2024; Milinski & Marotzke, 2022).
    - **Antisocial punishment** and punishment misapplied to cooperators or high contributors *undermines* efficiency (Duell et al., 2024; Angelsen & Naime, 2024).
    - **Monitoring quality is pivotal:** If individual actions are observable, punishment has stronger positive effects on efficiency (Eisenkopf & Walter, 2022; Kroupa, 2014; Arai et al., 2023).
    - **Transparency (e.g., endowment visibility)** interacts with punishment: efficiency gains are only realized when relevant information is public (Chen et al., 2025).
    - **Institutional context** (participatory design, credibility/enforcement) often trumps other dimensions: effects of punishment on efficiency are strongest when credibility and institutional support are high (Alt et al., 2023; Duell et al., 2024; Macleod et al., 2025).
    - **Punishment cost and impact:** Lower cost can lead to more antisocial or excessive punishment, eroding efficiency gains (Chen, Nave & Wang, 2025).
    - **Longer time horizons and communication:** Longer games or those permitting communication/reputation mechanisms amplify efficiency gains from punishment (Kroupa, 2014; Chen et al., 2025), while short, anonymous games suppress them.

**Theory and Models:**
- Efficiency is maximized only when sufficiently **severe punishment** is available and credible (Evans & Thomas, 2001), but *overly harsh punishment or high standards* can provoke perverse effects (Hernandez et al., 2022).
- Effectiveness of punishment is non-monotonic—**too severe or too frequently misapplied punishment can reduce efficiency** by crowding out voluntary cooperation (Kroupa, 2014; Hernandez et al., 2022).
- **Structural conditions** (e.g., group size, matching protocol, punishment targeting, ability to coordinate) shape whether punishment delivers efficiency gains.
- Observability and *group composition* (homogeneity, status, trust, culture) moderate the efficiency impact—heterogeneity and strong pre-existing norms can nullify or reverse the efficiency effect (Goto & Matsui, 2025; Grayson et al., 2025; Jin et al., 2024).

# 5) Prediction Guidance

## General Principle
- **The presence of a credible, well-designed punishment mechanism typically yields an increase in group efficiency over no-punishment baseline, especially when cooperation is otherwise fragile.**

## Conditional Effects
- **Do *not* assume that increased cooperation maps directly to increased efficiency**—account for punishment cost, antisocial punishment, and mis-targeting.
- **Positive efficiency effects are most likely** in:
  - Longer games (`num_rounds` high),
  - With communication (`chat` true) or transparency (`show_other_summaries`/endowment visibility),
  - With centralized/collective punishment, particularly if participation in enforcement is endogenous,
  - When individual-level monitoring is possible (`punishment_tech` supports).
- **Efficiency gains are weaker, null, or even negative** when:
  - Games are short or anonymous (few rounds, no communication),
  - The cost of punishment is high and/or impact is low,
  - There is significant antisocial punishment,
  - Punishment is enabled but not credible (low enforcement probability),
  - Community structure is highly cohesive and norms are already strong,
  - Monitoring is noisy or doesn't pinpoint individual contributors,
  - Institutional context does not support norm coordination or punishment targeting.

## Use of Control Efficiency
- **Control efficiency is a useful anchor:** If the control is already close to cooperative maximum, marginal gains from adding punishment are likely small or may be negative due to punishment costs.
- **If baseline (control) efficiency is low**, enabling punishment under favorable conditions can yield substantial efficiency gains, sometimes transforming a low-efficiency equilibrium into a high-efficiency one.

## Interactions with Design Dimensions
- **Punishment cost (`punishment_cost`)**: Lower cost increases usage but may backfire by encouraging antisocial punishment unless other mechanisms steer application.
- **Monitoring (`punishment_tech`/individual observability):** Strongly moderates effect size; when only group-level outcomes are visible, punishment is less effective and less efficient (Eisenkopf & Walter, 2022).
- **Transparency (`show_other_summaries`, `show_n_rounds`):** Increases effectiveness of punishment for efficiency gains (Chen et al., 2025).
- **Centralization vs. peer punishment:** Centralized (or institutionally anchored) punishment generally achieves higher efficiency, especially with proper design and participation (Duell et al., 2024; Krügel & Maaser, 2025).
- **Chat/communication:** Always increases efficiency, and interacts positively with punishment (Kroupa, 2014).
- **Time horizon (`num_rounds`)**: Efficiency of punishment increases the longer the game, as learning/coordination effects compound (Kroupa, 2014; Duell et al., 2024).
- **All-or-nothing decisions:** Binary contributions may moderate punishment's effect, especially when minimum contribution rules are manipulated (Gërxhani et al., 2021).
- **Player count:** Smaller groups more easily realize efficiency gains; effects may dissipate or invert with large, anonymous groups (Patrzyk & Takác, 2017).

# 6) Design Dimensions Highlighted Across Papers

## Directly Informed Dimensions:
- `player_count`: Varied across exact and close studies; small to moderate group sizes studied most (3–5 common), with some larger. Smaller groups often see stronger effects (Kanitsar, 2019).
- `num_rounds`: Systematically manipulated; **longer games** consistently yield larger, sustained efficiency gains from punishment (Kroupa, 2014).
- `chat`: Strong evidence that communication synergizes with punishment for higher efficiency (Kroupa, 2014; Chen et al., 2025).
- `all_or_nothing`: Both binary and continuous PGGs well represented; some studies directly manipulate minimum contribution rules (Gërxhani et al., 2021).
- `mpcr`: Studied as a moderator of cooperation and efficiency; lower MPCRs (higher conflict) reduce baseline efficiency, and absolute efficiency gains from punishment may be smaller in easy games than hard ones (Jin et al., 2024).
- `punishment_cost` and `punishment_tech`: Central; major determinant of antisocial punishment/effectiveness (Chen, Nave, & Wang, 2025; Eisenkopf & Walter, 2022).
- `show_other_summaries`, `show_n_rounds`: Transparency is shown to moderate the effect (Chen et al., 2025).
- `reward_exists`: Some meta-analyses and experimental evidence on interaction with rewards/no rewards (Jin, Spadaro et al., 2025).

## Indirectly Informed or Contextual Only:
- `default_contrib`: Rarely manipulated directly; some evidence from opt-in/opt-out framing in adjacent or close variants.
- `show_punishment_id`: Only contextually discussed or implicit (few papers explicitly compare anonymity vs. transparency in punishment identity).
- `reward_cost`, `reward_tech`: Limited direct data; most studies focus on punishment in isolation.
- `punishment_magnitude`: Sometimes varied (Chen, Nave & Wang, 2025), but less often as a targeted manipulation.

## Effectively Missing or Sparse:
- **Simultaneous manipulation** of all design dimensions; comprehensive factorial is generally lacking.
- **Explicit mapping** from the precise PGG configuration over all 14 dimensions to efficiency delta is *rare*.
- Dimensions about *rewards* and *rewarding technology* are insufficiently addressed for specific quantitative predictions.

# 7) Important Limitations

- **Efficiency Not Always Reported Directly:** Many studies use contribution rates, norm compliance, or voting for institutions as proxies; direct efficiency ratios (actual vs. maximum possible group payoff) are less often provided.
- **Interaction Effects Not Fully Explored:** Most studies manipulate a handful of dimensions, rarely the full set relevant for out-of-sample prediction.
- **Punishment Implementation Varies:** Results can differ for peer, centralized, collective, third-party, and indirect punishment, limiting generalizability.
- **Cultural and Institutional Context Matters:** Effects found in lab settings may not generalize to field, especially when norms/pre-existing sanctions vary.
- **Antisocial Punishment and Mis-Targeting:** These can erase or reverse efficiency gains, but are not consistently measured or modeled.
- **Ceiling Effects:** Where baseline cooperation is high, the marginal efficiency gain from enabling punishment is often minimal or negative due to the direct cost of punishment use.
- **Extent of Cost Accounting:** Some studies fail to fully subtract punishment costs when reporting group payoff.
- **Reward Mechanisms Understudied:** The joint or separate impact of positive incentives is not systematically examined alongside punishment.
- **Design Dimension Gaps:** Sparse or missing data on the effects of default contribution, punishment/reward magnitude, and show_punishment_id.
- **Theoretical Models Make Strong Assumptions:** Infinite time, perfect reputation, severe punishment strategies, or agent rationality may not match practical settings.

---

**Summary**:  
The available literature provides **strong support** for the claim that enabling punishment in PGG-like environments *typically* increases group efficiency over no-punishment baseline, **conditional on game design features**, monitoring quality, and institutional context. *Specific design dimensions*—especially punishment cost, type, monitoring technology, transparency, group size, and opportunity for communication—**critically moderate the efficiency effect**. Control efficiency is informative but *alone insufficient*, as the marginal efficiency gain is context-dependent and sensitive to underlying design/implementation details. **Prediction accuracy is best where study designs and outcomes align closely with the target task and dimensions.** Ambiguities remain, and the potential for negative or null effects under some conditions requires cautious, dimension-aware application of these findings.
