# 1) Evidence Base

The paper set is broad in scope (87 papers), with a substantial empirical emphasis, primarily reporting laboratory and field experiments in public-goods-game (PGG) or closely related environments. Several high-relevance meta-analyses, theory papers, and empirical studies provide a rich mix of direct observations, model-based predictions, and contextual or mechanism insights. The literature covers both peer and centralized punishment, institutional variants, and a wide range of design and contextual moderators.

While the majority of included papers directly manipulate or measure punishment in PGGs, a significant minority are theory papers, studies in adjacent game structures (CPR, PD, dictator games, real-world field contexts), or address non-payoff outcomes such as cooperation rates, norm compliance, and punishment frequency. Only a subset of empirical studies and reviews directly report payoff- or efficiency-based outcomes suitable for the intended downstream prediction task, although reporting of game design dimensions is often detailed and clear where relevant.

The base is thus deep for behavioral, mechanism, and context arguments, but thinner—and more selective—regarding direct, quantitative links between punishment (as manipulated treatment) and group efficiency as defined by total payoff relative to fully cooperative optimum.

# 2) Task Relevance

**Relevance:**

- **pgg_or_variant:** Most core empirical and some theoretical papers have `exact` or `close` relevance, studying either classic PGGs or structurally similar social dilemmas (CPR games, repeated PDs). Some contextual or conceptual papers are only `adjacent` or `weak`.
- **punishment_or_sanctions:** Many papers are `exact` (punishment manipulated/enabled), with others as `close` (e.g., gossip, ostracism, reward, institutional choice) or `adjacent` (e.g., dyadic sanctioning, third-party punishment, informal norm enforcement).
- **efficiency_or_related_payoff_outcome:** Fewer papers have `exact` or `close` relevance; many focus on **behavioral outcomes** (contributions/cooperation) without reporting or analyzing group efficiency or payoff. Only a minority directly report **efficiency** or related welfare/surplus outcomes.

**Summary:**  
- Direct, high-quality evidence exists for core prediction tasks (e.g., Lo Iacono et al., 2023; Krügel & Maaser, 2025; Duell et al., 2024; Eichenseer, 2023), but much of the broader literature is only indirectly relevant for **efficiency** prediction. The base is robust for behavioral and contextual insights but thinner for direct, calibrated efficiency outcomes.

# 3) Outcomes Measured In The Literature

- **Payoff-related Outcomes (Relevant for Task):**
    - **Efficiency (normalized group payoff):** Explicitly reported in key lab experiments and some meta-analyses (e.g., Lo Iacono et al., 2023; Eichenseer, 2023), but not in most studies.
    - **Total/group payoff, welfare, surplus:** Some studies report aggregate group earnings (Krügel & Maaser, 2025; Gross et al., 2022; Duell et al., 2024; Milinski & Marotzke, 2022).
    - **Treatment-control differences:** When present, typically compare average payoffs/efficiency between punishment and no-punishment conditions.

- **Non-payoff Behavioral Outcomes (Common but Distinct):**
    - **Contribution/cooperation rates:** Frequently reported and often increased by punishment (e.g., Spadaro et al., 2022; Jin et al., 2025), but do not necessarily reflect efficiency due to punishment costs.
    - **Punishment frequency, norm compliance, pro-social behavior:** Widely measured; implications for efficiency must be inferred and are often ambiguous.
    - **Emotional and psychological states:** Trust, anger, perception of legitimacy/support, norm perceptions.

- **Other Reporting:**
    - Many large field studies, agent-based models, and context-related papers use outcomes such as participation, compliance, reputation, or perceived trustworthiness, but not group payoff or efficiency.

# 4) Main Findings Relevant To Prediction

**Synthesized Findings on Punishment's Impact:**

- **Enabling peer punishment in standard PGGs generally increases group efficiency/payoff,** especially over time, *when the punishment system is credible, well-targeted, and institutionally supported* (Lo Iacono et al., 2023; Krügel & Maaser, 2025; Duell et al., 2024; Eichenseer, 2023).
    - **The efficiency effect is stronger** with higher information transparency (Chen et al., 2025), credible enforcement (Alt et al., 2023), individual-level monitoring (Eisenkopf & Walter, 2022), or collective/commitment-based punishment systems (Duell et al., 2024).
- **Punishment is often not efficiency-enhancing if:**
    - **Punishment is too weak, misapplied, or antisocial.** Ineffective punishment raises costs without improving cooperation, or even reduces earnings (Gross et al., 2022; Chen et al., 2025; Goto & Matsui, 2025; Angelsen & Naime, 2024; Milinski & Marotzke, 2022).
    - **Social context undermines punishment targeting or legitimacy.** Effects can be negative or null when pre-existing norms are strong, roles are ambiguous, or punishment is perceived as illegitimate or corrupt (Gross et al., 2022; Macleod et al., 2025; Milinski & Marotzke, 2022; Spadaro et al., 2023).
    - **Severe/harsh punishment crowds out voluntary cooperation,** lowering welfare (Hernandez et al., 2022).
    - **Enforcement is not credible,** monitoring is noisy, or information is partial—then, punishment often fails to increase efficiency (Alt et al., 2023; Eisenkopf & Walter, 2022).

- **Institutional design matters:** Well-designed collective punishment (commitment-based, opt-in) or competitive higher-order institutions outperform baseline peer punishment for efficiency (Duell et al., 2024; Krügel & Maaser, 2025).

- **Behavioral outcomes (contribution/cooperation rates) typically increase more than efficiency,** especially in studies not considering punishment costs; thus, increases in efficiency should not be presumed from cooperation alone (Eichenseer, 2023; Jin et al., 2025).

- **Non-standard settings (e.g., polycentric or subgroup punishment) may see negative or null effects,** with costs outweighing any cooperation increase or even reducing group welfare (Milinski & Marotzke, 2022; Goto & Matsui, 2025).

- **Transparency, monitoring, and information display strongly moderate effectiveness:** Punishment works better with public endowments or detailed summaries (Chen et al., 2025; Nielsen & Pfattheicher, 2024).

# 5) Prediction Guidance

- **Prediction of Treatment Efficiency from Control Efficiency and Design Dimensions:**
    - Where empirical evidence is strongest (e.g., standard linear PGGs with moderate group size, sufficient rounds, moderate to high MPCR, and costly yet effective punishment), enabling punishment increases group efficiency, often by 20–50 percentage points (relative to max, per meta-analytic estimates, e.g., Eichenseer, 2023).
    - **The size and direction of the effect depend on key moderators:**  
        - **Punishment cost:** Too low → more antisocial punishment (net negative); too high → deterrence is weak (little gain).
        - **Monitoring/punishment tech:** Detailed, individual-level monitoring enables efficiency gains; noisy/aggregate info disables the effect.
        - **Institutional support:** Commitment-based or institutionally supported punishment is more productive than baseline peer punishment.
        - **Contextual factors:** Endowment transparency, group size, social history (e.g., prior conflict), and community structure can convert positive effects into null or even negative ones.
    - **Control efficiency is an informative base** but must be adjusted for these design dimensions—punishment does not guarantee higher treatment efficiency across all environments.
    - **Do not rely on increased cooperation rates alone** to infer gains in efficiency—incorporate information on punishment frequency, cost, and targeting.

# 6) Design Dimensions Highlighted Across Papers

### **Directly Informed Dimensions:**
- **player_count, num_rounds:** Commonly specified and varied; efficiency effects are robust at small/moderate sizes, but larger groups may require more institutional design.
- **all_or_nothing, mpcr:** Frequently manipulated; classic effects of higher MPCR and continuous choices on higher base efficiency and larger punishment effects.
- **punishment_cost, punishment_tech:** Explicitly manipulated in many experiments; cost/impact ratio is a key determinant of punishment's efficiency effect. Tech varies from peer to third-party and higher-order institutions.
- **show_other_summaries, show_punishment_id:** Feedback/monitoring features are shown to be critical; transparent, detailed summaries improve punishment effectiveness and efficiency.
- **reward_exists, reward_cost, reward_tech:** Some studies compare or combine with punishment; reward alone can also increase efficiency and is often as or more efficient (Wu et al., 2022; Eichenseer, 2023).

### **Indirectly Informed/Contextually Addressed:**
- **chat, default_contrib:** Communication is often controlled; when present, is a known boost for efficiency—its interaction with punishment is noted but not systematically varied. Default contribution framing is investigated in a few cases (Capraro, 2024).
- **show_n_rounds:** Some studies specify or manipulate this, often as a platform artifact.
- **show_punishment_id:** Occasionally highlighted as influencing legitimacy or psychological responses.

### **Effectively Missing or Sparse:**
- **Details of all 14 dimensions combined:** No study systematically varies all dimensions; batchwise cross-dimension evidence is limited. Many contextual, field, and theory papers do not specify key dimensions, and some do not include direct PGGs or payoff outcomes.

# 7) Important Limitations

- **Efficiency outcomes are underreported:** Many studies infer efficiency gains from increased cooperation without accounting for punishment costs, leading to overstatement of positive effects.
- **Generality across design dimensions is limited:** Strong evidence comes from canonical lab designs (fixed group size, rounds, punishment system), but predictive utility weakens outside these settings; studies rarely cross major dimensions in factorial ways.
- **Contexts lacking transparency, strong pre-existing norms, or effective enforcement may not show positive efficiency effects** (Gross et al., 2022; Goto & Matsui, 2025; Milinski & Marotzke, 2022; Hernandez et al., 2022).
- **Boundary conditions are critical:** When punishment risks being misapplied, antisocial, or uncoordinated, efficiency can stay unchanged or even decline versus control.
- **Behavioral versus payoff outcome conflation:** Many influential papers emphasize cooperation and norm compliance, which are not always translated into higher group payoffs due to the costliness or inefficiency of punishment.
- **Sparse direct calibration for extreme or joint-moderator scenarios:** Prediction for very large groups, noisy environments, high asymmetry, or new institutional forms must extrapolate beyond the evidence base.
- **Heterogeneity in punishment effect reporting:** Some cultures/contexts support antisocial punishment or malicious enforcement, with divergent efficiency impacts (Chen et al., 2025; Angelsen & Naime, 2024).
- **Limited reporting on interaction with rewards, chat, entry/exit, identity, and framing:** The robustness of payoff gains under such combinations is underexplored.

---

### **Summary**
**The literature provides high-quality, direct evidence that enabling peer punishment in PGGs can increase group efficiency when punishment is well-designed, credible, and contextually appropriate. However, positive efficiency impacts are contingent on information, targeting, punishment cost, and institutional design—efficiency gains are not universal. Many design dimensions and social context variables act as moderators, and outcomes should not be inferred from cooperation rates alone. Predictive models should incorporate these caveats, and use direct efficiency evidence for calibration whenever possible.**
