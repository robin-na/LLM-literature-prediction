# 1) Evidence Base

Across a set of 1445 theory papers (no direct empirical or experimental studies), the literature base is **broad and deep** for theoretical/evolutionary modeling of cooperation, punishment, and efficiency in repeated and spatially structured social dilemmas. There is **very high relevance** for public goods games (PGGs) and close variants, but empirical/lab experimental data are missing. The paper set is rich in models that explicitly define payoffs, equilibrium efficiency, and group outcomes as a function of game parameters, often providing closed-form predictions, phase diagrams, and explicit conditions under which punishment mechanisms do or do not increase efficiency.

**Importantly:**  
- The evidence is almost entirely theory and simulated outcomes, not empirical lab/field findings.
- Many models are parameterized with PGGs or adjacent games (e.g., networked trust games, threshold public goods, CPR dilemmas, iterated PD).
- Some papers study only cooperation rates rather than explicit efficiency or group payoff—these are used for mechanism context but marked accordingly.

# 2) Task Relevance

**Key dimensions:**

**pgg_or_variant:**  
- Nearly all theory papers are `exact` or `close` to PGGs or explicit public-goods-like group cooperation games (repeated/one-shot, continuous/all-or-nothing, threshold or linear payoffs, etc.).  
- Some use iterative PD, trust, or threshold games (`close`/`adjacent`/`weak`); only a minority are not public goods related.

**punishment_or_sanctions:**  
- Most analyze punishment or sanctioning directly (`exact`), but a significant subset study reward only, exclusion/ostracism (adjacent), or indirect mechanisms like reputation or exit (marked as `close` or `adjacent`).  
- About one-third focus on unconditional punishment, the effect of anti-social punishment, or weakly related punishments (e.g., jealousy-based, self-punishment, punishment via tie breaking).

**efficiency_or_related_payoff_outcome:**  
- About half report on efficiency or group payoff (`exact`).  
- Many report average payoff, welfare, surplus, or closely analogous measures (`close`).  
- A significant number focus on prevalence/fraction of cooperation rates or behavioral dynamics and NOT efficiency/payoff—these are only mechanism context, not used for main claims.

# 3) Outcomes Measured In The Literature

**Explicit payoff-based outcomes (`exact` or `close`):**  
- **Efficiency** ("ratio of group payoff to the full-cooperation benchmark") and average total payoff/welfare are standard in most game-theoretic models (e.g., Cressman et al. 2012; Levine & Modica 2016; Bühren et al. 2023).
- Group earnings, normalized utility, group surplus, or coins generated—reported directly in many mechanism-calibrated models.
- In resource/CPR/collective-risk models: sustainable resource level, group achievement proxy for efficiency (e.g., Vasconcelos et al. 2015, Góis et al. 2019).
- Cost to the institution to achieve cooperation in incentive design models, which can be mapped to efficiency (Duong & Han 2021).

**Non-payoff outcomes (NOT efficiency):**  
- **Cooperation rates/frequencies, prevalence of strategies, punishment frequency, norm compliance.**  
- Network/cluster structure, stability, social learning, average level of emotion, prevalence of altruism, etc.
- These are often used to infer likely efficiency direction/mechanism but DO NOT quantify efficiency without explicit payoff reporting.

# 4) Main Findings Relevant To Prediction

**Synthesis:**

### 1. **Punishment usually increases group efficiency relative to the no-punishment baseline, but only under key moderating conditions:**
   - **Punishment must be sufficiently effective (high fine-to-cost ratio, sufficient severity)** and not too costly for punishers (e.g., Cressman et al. 2012; Levine & Modica 2016; Fehr & Gintis 2007; Gintis 2000; Bowles & Gintis 2004; Powers et al. 2018; Gao et al. 2020).
   - **Suboptimal/inadequate, costly, or misdirected punishment is at best neutral on or reduces efficiency**: high-cost, poorly targeted, or anti-social punishment can destroy group surplus even as it deters some defection (Perc et al. 2017; Han et al. 2024; Rand & Nowak 2011; Vukov et al. 2013; Duong et al. 2021; Ezeigbo et al. 2017).
   - **Reward mechanisms are generally less robust than punishment for achieving full efficiency**, except sometimes when punishment is too costly or populations are error-prone (Dong et al. 2019; Sasaki & Uchida 2013; Wang et al. 2021).

### 2. **Critical game design moderators:**
   - **Player count (group size):** The positive effect of punishment on efficiency generally persists as group size increases, unless the monitoring/punishment cost grows too fast or antisocial/retaliatory punishment undermines deterrence (Levine & Modica 2016; Hwang, 2017; Sethi & Somanathan 2003; Powers et al. 2023).
   - **Marginal per-capita return (mpcr):** Low mpcr environments benefit most from punishment—punishment enables efficient outcomes where cooperation is otherwise hard, but for high-mpcr games, punishment may not add much to already high baseline efficiency (Wu et al. 2014; Perc et al. 2017; Wang et al. 2011).
   - **Punishment cost and effectiveness:** High fine-to-cost ratios are necessary for positive efficiency effects (Cressman et al. 2012; Gintis 2000; Okada & Bingham 2008); if punishment is effective but costly, or if second-order punishment is required, efficiency gains are smaller or negative.
   - **Population structure and information:** Spatial/game topology (lattice, small-world, group structure) enables localized punishment, forming cooperator/punisher clusters that support higher efficiency (Szolnoki & Perc 2013; Vasconcelos et al. 2022; Bodnar & Salathé 2012). Well-mixed populations without reputation or information transmission may fail to benefit from punishment (Ohtsuki et al. 2007, Laclau & Tomala 2017, Cressman et al. 2012).
   - **Anti-social or retaliatory punishment:** The possibility of punishment being used against high contributors or punishers themselves can nullify or reverse efficiency gains (Rand & Nowak 2011; Hauser et al. 2014; Rand et al. 2010; Lee et al. 2019).
   - **Second-order free-riding:** In evolutionary and institutional models, failure to punish non-punishers allows decay of punishment and collapse of cooperation/efficiency unless precommitted or prearranged sanctions are available (Sasaki et al. 2015; Perc 2012; Yao & Chen 2014).

### 3. **Intermediate/balanced incentive schemes or graduated punishment can maximize efficiency.**
   - Pure reward or pure punishment is rarely optimal for efficiency; mixed or adaptive strategies with punishment only above thresholds, or graduated to the degree of violation, can achieve higher efficiency at lower cost (Sun et al. 2023; Iwasa & Lee 2013; Sasaki et al. 2015; Cong et al. 2016; Jiao et al. 2020).

### 4. **There are well-understood exceptions:**
   - If punishment is allowed to be anti-social, if there is corruption/bribe-based avoidance of sanctions, or if monitoring is highly imperfect, punishment can reduce or fail to increase efficiency (Lee et al. 2019; Powers et al. 2012; Liu et al. 2019; Nakamaru et al. 2009).
   - Voluntary or partner-choice mechanisms (exit, ostracism, rewiring, link-breaking) can sometimes substitute for punishment, achieving high efficiency even without costly sanctions (Zimmermann & Eguíluz 2005; Graser et al. 2025; Hauser et al. 2009).
   - In indirect reciprocity frameworks, costly punishment often does not increase efficiency (Ohtsuki et al. 2009); non-costly exclusion or reputation mechanisms are more robust.

### 5. **Efficiency gains from punishment are typically larger when baseline (control) efficiency is low.**
   - For control games with high efficiency (e.g., high baseline cooperation, easy-to-monitor or high-mpcr), enabling punishment may not increase and can decrease efficiency due to surplus-destroying punishment costs.

# 5) Prediction Guidance

**For the downstream prediction task:**

- **If a game design has low control efficiency (no punishment), and punishment is enabled with reasonable cost-effectiveness,** theoretical models predict a large, often sharp, increase in efficiency (group payoff relative to cooperative optimum)—sometimes up to or near the maximal level (Fehr & Gintis 2007; Levine & Modica 2016; Kranz 2010; Okada & Bingham 2008; Gintis 2000; Boyd & Richerson 1992).
- **The size of the efficiency gain from punishment is highly sensitive to:**
  - **Punishment effectiveness:** High fine-to-cost ratio needed. If cost is high or effectiveness is low, efficiency gains disappear or reverse.
  - **Presence of anti-social punishment, corruption, or retaliation:** Erodes or reverses positive effects.
  - **Population structure/topology:** Clustered/localized punishment is more efficient; well-mixed environments need monitoring or reputation transmission.
  - **Group size and mpcr:** Gains are most reliable in small-to-moderate groups and low-mpcr games; in very large groups or with high mpcr, punishment becomes less critical.
  - **Information/reputation:** If punishment acts via reputation and is observable, efficiency gains are larger; if behavior is anonymous or information is too coarse, effects weaken.
  - **Initial state/baseline:** If control efficiency is already high, the marginal efficiency effect of punishment is smaller—may be negative if costs dominate (Levine & Modica 2016; Kroupa 2014; Han et al. 2024; Ohtsuki et al. 2009).
- **Account for dynamic/long-run effects:** Many models show that efficiency with punishment is highest in the long run, as costly punishment is used less frequently once cooperation is established (Dejong et al. 2008; Gintis 2003; Fehr & Gintis 2007).
- **Graduated or threshold-triggered punishment may yield higher efficiency at lower cost than constant or severe punishment (Ohtsuki & Iwasa 2013; Jiao et al. 2020; Wang et al. 2021).**
- **Reward or institutionally supported hybrid (reward+punishment) schemes can be more efficient than punishment or reward alone for some parameter ranges (Sun et al. 2023; Sasaki et al. 2015; Jiao et al. 2020; Cong et al. 2016; Han et al. 2022).**
- **Negative/ambiguous cases arise when punishment is highly costly, anti-social, or easily circumvented:** In such cases, efficiency may decrease or be unchanged.

**Practical modeling recommendation:**  
Use parameter regimes from the literature that match the intended prediction context (e.g., group size, rounds, punishment cost/tech, network structure, available information) to select the most aligned phase diagram or theoretical result—do NOT extrapolate from behavioral (non-payoff) findings or from control games with high baseline efficiency.

# 6) Design Dimensions Highlighted Across Papers

### **Directly Informed Dimensions (explicit in payoff/equilibrium equations, direct comparative statics):**
- **player_count:** Many models provide explicit dependence of equilibrium efficiency on group size (Levine & Modica 2016; Cressman et al. 2012; MacLeod 2007; Hwang 2017; Okada & Bingham 2008; Wang et al. 2011; Sethi & Somanathan 2003).
- **num_rounds:** Repeatedness/patience is critical; long games or high discount factor sustain higher efficiency with punishment (Levine & Modica 2016; Jones 1999; Laclau & Tomala 2017).
- **mpcr:** Universally parameterized; explicit thresholds for when punishment increases efficiency (Wu et al. 2014; Perc et al. 2017; Kranz 2010).
- **punishment_cost / punishment_tech:** Always parameterized in payoff equations (Cressman et al. 2012; Gintis 2000; Ohtsuki et al. 2009).
- **population structure (network, spatial, group/assortment):** Explicitly modeled and compared (Szolnoki & Perc 2013; Vasconcelos et al. 2015; Bodnar & Salathé 2012).
- **reward_exists / reward_cost / reward_tech:** Directly compared in many hybrid incentive models (Sun et al. 2023; Jiao et al. 2020).

### **Indirectly or Contextually Informed:**
- **all_or_nothing / default_contrib:** Covered in both continuous and binary choice models, but less often shown to moderate efficiency effects directly.
- **chat, show_other_summaries, show_n_rounds, show_punishment_id:** These are indicators for information structure; some models include or discuss these dimensions explicitly in reputation and monitoring technologies but not always parameterized for efficiency prediction. Information/reputation is a key moderator for punishment's efficiency effect.
- **punishment_tech (parameterization of "who can punish whom", centralized vs peer, anonymity):** Directly relevant; institutional vs peer punishment and the possibility of anti-social punishment are core topics (Szolnoki & Perc 2017; Perc et al. 2017).
- **reward_exists / reward_cost / reward_tech / reward_magnitude:** Well-studied in hybrid incentive schemes.
- **other display/framing dimensions:** Very rarely parameterized, usually only as lab environment context.

### **Effectively Missing or Only Discussed in Passing:**
- **default_contrib (opt-in vs opt-out), show_other_summaries, show_n_rounds (round horizon transparency):** Sometimes addressed in the context of framing or experimental manipulation, but rarely parameterized in efficiency equations.
- **punishment_magnitude, punishment allocation rules (minority/majority, targeted, probabilistic):** Sometimes included in advanced models (e.g., graded/graduated punishment), but often fixed.

# 7) Important Limitations

**1. Theoretical—Not Empirical:**  
All findings are theoretical model results, not lab or field experimental effect sizes. The results are robust and mechanistically clear, but empirical generalization must be cautious.

**2. Parameter Sensitivity:**  
Many models show sharp phase transitions, thresholds, or bistability: the effect of enabling punishment can be highly nonlinear and parameter-dependent (critical thresholds for group size, punishment cost, punishment effectiveness, information structure, or initial state).

**3. Exclusion of Behavioral-Only Outcomes:**  
Cooperation rates, norm compliance, or prevalence of strategies are NOT usable proxies for efficiency except where payoff mapping is explicitly provided. Many cited papers whose main outcomes are cooperation/strategy fractions can only be used for qualitative mechanism context.

**4. Adjacent Outcomes:**  
A substantial proportion of papers are on adjacent games (PDG, trust, etc.) or mechanisms (exclusion, reputation, exit/rewiring, voluntary participation). These can guide mechanism reasoning but may not match PGG structures or payoff mapping exactly.

**5. Mapping to Prediction Dimensions:**  
Some design dimensions (information feedback, identity transparency, opt-in/opt-out framing, etc.) are not always explicitly parameterized; where so, they must be regarded as only weakly or contextually informed.

**6. Critical Moderators Not Always Measured:**  
Key moderators that can reverse or qualitatively alter the effect of punishment include:
- Cost and effectiveness of punishment,
- Type/presence of anti-social punishment,
- Corruption or bribery,
- Group structure and monitoring technology,
- Initial composition (e.g., presence of punishers, balance of strategies).
In cases where these are unmeasured or not specified, predictions must be more conservative.

**7. Absence of Laboratory or Real-World Data:**  
While evolutionary and game-theoretic models are rich, predictions about magnitude of efficiency change (how much efficiency rises with punishment enabled) cannot be calibrated to real-world effect size or mapped directly without empirical effect size estimates.

---

**Summary:**  
The theoretical literature provides strong support for predicting that enabling peer punishment in PGGs generally increases efficiency **relative to the no-punishment baseline**—especially in small/moderate groups, low-mpcr environments, with effective and well-targeted punishment, no anti-social punishment, sufficient information, and not-excessive costs. Key design dimensions (group size, rounds, mpcr, punishment cost/tech, network structure, information structure) are well-theorized as moderators, but initial baseline efficiency (control game) must always be considered—as the marginal benefit from punishment is highest when baseline efficiency is low. Caution is needed in high-mpcr, already-high-efficiency, or anti-social/corruptible settings, and for direct quantitative prediction absent field/lab effect sizes.
