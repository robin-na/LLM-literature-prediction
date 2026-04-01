# 1) Evidence Base

This paper set is **large (114 papers)**, but consists almost entirely of theoretical, game-theoretic, and simulation papers, with no new empirical or experimental studies. The majority are formal mathematical models or literature syntheses regarding cooperation, punishment, and efficiency/welfare in public-goods-game (PGG) or closely related environments. The evidence base is heavily weighted toward **theoretical predictions and mechanism arguments**. Multiple papers address formal efficiency or group payoff outcomes, but many focus only on **behavioral measures (e.g., cooperation rate, norm compliance, punishment frequency)** or provide only indirect, contextual, or high-level guidance without calibrated quantitative effect sizes.

# 2) Task Relevance

**pgg_or_variant**:  
- The set is **highly relevant** for PGGs and direct variants: at least a dozen papers analyze linear or nonlinear public goods games or threshold/optional variants exactly matching the target environment.
- Many additional papers are **close or adjacent variants**, including common-pool resource (CPR) models, indirect reciprocity, repeated or spatial PD games, division-of-labor games, and resource-sharing analogs.

**punishment_or_sanctions**:  
- Approximately half the papers are **exactly relevant** for punishment or sanctioning—explicitly modeling costly punishment, exclusion, rewards, or institutional sanctions as experimental/game design variables.
- Many others are **adjacent**, discussing partner choice, exit, reputation, social exclusion, or indirect/implicit sanctioning (which may or may not map cleanly onto the prediction variable `punishmentExists`).

**efficiency_or_related_payoff_outcome**:  
- Most directly relevant papers define and analyze **group efficiency** (payoff relative to fully cooperative maximum), welfare, surplus, or equivalent group earnings.
- However, a substantial fraction discuss only **non-payoff behavioral outcomes** (contribution/cooperation rates, norm compliance) and **do not report quantitative efficiency effects**.
- Some adjacent/weak papers discuss only mechanisms or suggest qualitative claims regarding payoff/economic efficiency.

# 3) Outcomes Measured In The Literature

- **Direct payoff-based outcomes** (efficiency, group payoff, total earnings):  
  Present and directly modeled in a subset of papers (e.g., Dong et al., 2019; Powers et al., 2023; Adami et al., 2016; Murase & Baek, 2021; Wang et al., 2024; Okada et al., 2015).
- **Behavioral/non-payoff outcomes** (contribution rates, cooperation frequency, punishment frequency, norm compliance):  
  Prevalent in many papers, especially in literature centered on evolutionary mechanisms or cognitive/psychological underpinnings (e.g., Fehr & Fischbacher, 2004; Gintis, 2011; Singer & Steinbeis, 2009).  
  Often **used as a proxy for efficiency** without direct payoff reporting—a notable limitation for the prediction task.
- Multiple papers combine **payoff analysis and behavioral outcomes**, while others provide only **mechanism-level or contextual insights** (e.g., on reputation, partner choice, or the ecological context).

# 4) Main Findings Relevant To Prediction

**Synthesis Across Papers:**

- When **punishment is enabled**, cooperation rates typically increase (robust effect). However, the implications for **group efficiency** are more nuanced:
  - **Costly peer punishment** often raises cooperation but can **reduce efficiency** due to destruction of resources (punishment costs and fines) unless the game is long/repeated and punishment frequency drops over time (Guala, 2012; Dong et al., 2019).
  - **Institutional punishment** (centralized or coordinated) tends to be more efficient and robust, especially at **larger group sizes** and when the cost per effective sanction is low (Powers et al., 2023; Adami et al., 2016).
  - **Exclusion mechanisms** (social exclusion from benefits) are found to be **more efficient** than costly punishment, as they deter free riding without expending resources on punitive acts (Sasaki & Uchida, 2013).
  - **Reward (positive incentives)** is at least as effective or more so than punishment at increasing efficiency, particularly in boundedly rational or error-prone environments (Dong et al., 2019; Rand & Nowak, 2013).
  - The **marginal effect of punishment** on efficiency is greatest when the control (no-punishment) efficiency is low and/or the system is near the cooperation/defection critical point (Adami et al., 2016; Brandt et al., 2003).
  - **Optional participation** and the presence of **loners** can moderate the impact of punishment: If game parameters do not support the invasion of punishment (relative payoffs of loners/defectors/cooperators and returns-to-scale), then punishment provides little to no efficiency gain (Mathew & Boyd, 2009).
  - **Population structure, group size, and hierarchy**:  
    - In large or well-mixed groups, individual punishment is less effective unless institutionally coordinated (Powers et al., 2023; Powers & Lehmann, 2013).
    - Spatial or network structure (local repeated interactions) increases the efficacy of punishment and makes cooperative norms with punishment more likely to dominate (Brandt et al., 2003; Helbing et al., 2010; Pacheco et al., 2014).
  - **Cost-effectiveness of punishment** is a major moderator: High-cost, low-impact punishment can reduce efficiency; low-cost, high-impact (or more targeted, reputation-based) punishment increases it (Vukov et al., 2013; Guala, 2012).
  - **Presence of reputation, communication, and information flow (e.g., chat, visibility of punishment, summaries)** moderate both the behavioral and efficiency outcomes—punishment is more effective at increasing efficiency when reputation is salient and information is transparent (dos Santos et al., 2011; Milinski, 2016).
  - **Antisocial punishment** (punishment targeted at cooperators or high contributors) or misapplied punishment reduces or even reverses efficiency gains (Fehr & Schurtenberger, 2018; Dong et al., 2019).
  - **Ecological context and dynamic resource models** (common-pool resource environments): In resource-limited or slow-growth contexts, punishment may not raise efficiency even if cooperation is enforced (Wang et al., 2024; Chen & Szolnoki, 2018).
  - **Second-order dilemmas**: If only first-order punishment is possible (punishing defectors but not those who don't punish), efficiency gains from punishment are fragile; systems with meta-incentives (for rewarding punishers/rewarders) are more robust (Okada et al., 2015).

**Empirical estimates of effect size are generally not provided**; most findings are qualitative or parametric ("increases group efficiency under these conditions"). Some models provide explicit equations for efficiency as a function of design parameters, but these are not derived from laboratory or field data.

# 5) Prediction Guidance

- **Do not assume that enabling punishment will always increase efficiency**: The direction and magnitude of the effect depend strongly on game design dimensions (especially punishment cost and tech, group size, information structure, and the control efficiency).
- **Exact mapping from control to treatment efficiency requires attention to**:
  - **Punishment cost (cost per unit, relative to impact)**: Low cost/high fine is conducive to greater efficiency gains.
  - **Punishment technology/design**: Peer punishment (individual/informal) is less efficient for large groups and prone to second-order dilemmas; centralized/institutional punishment or exclusion is more robust.
  - **Player count and group structure**: Increases in player count generally reduce the efficacy of peer punishment unless supported by institutions or group structure.
  - **MPCR (marginal returns)**: Lower MPCR makes cooperation/efficiency harder to achieve; punishment is most effective when baseline efficiency is low to moderate.
  - **Reputation, communication, and transparency features (chat, summaries, punishment_id)**: These strongly moderate the effectiveness and efficiency gain of punishment.
  - **Repeated interaction (num_rounds, show_n_rounds), visibility of rules/outcomes**: Repetition and transparency amplify positive effects.
  - **Presence of anti-social punishment or weak norms**: Allowing anti-social punishment (punishing cooperators) generally reduces or negates efficiency gains.
  - **Ecological/resource dynamics (especially in CPR extensions)**: If resources cannot recover, punishment does not increase net efficiency.
- **If the control (no-punishment) efficiency is already high (near fully cooperative)**, enabling punishment may provide little or no additional gain, or could reduce efficiency by introducing unnecessary cost/friction (Adami et al., 2016; Guala, 2012).
- **If the control efficiency is low or on the cusp of cooperation/defection transition** (near threshold), punishment is likelier to induce large efficiency gains—conditional on punishment's cost-effectiveness and moderating features.
- **If reward exists (reward_exists, reward_cost, reward_tech)**: Expect its presence to compete with or even overshadow punishment in increasing efficiency; reward is often more cost-effective (Dong et al., 2019).
- **Context-dependent caveats**:  
  - Presence of meta-incentives (for punishing cooperators or second-order punishment) or exclusion mechanisms can flip the effect from negative to positive (Okada et al., 2015; Sasaki & Uchida, 2013).
  - The presence of optional participation or loners introduces additional critical conditions for punishment to affect efficiency (Mathew & Boyd, 2009).

**Prediction should always be conditional on:**
- The game design's fit with the core PGG models analyzed, especially with respect to the precise implementation of punishment, group size/structure, cost-benefit parameters, and reputational or communication mechanisms.
- The behavioral outcome (cooperation rate) **is not always a reliable proxy** for efficiency if punishment is costly or used indiscriminately.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**
- `player_count`: Heavily analyzed, especially as a moderator (Powers et al., 2023; Adami et al., 2016). Larger groups decrease efficacy of peer punishment; institutional features can mitigate.
- `num_rounds`: Discussed as crucial for stabilization of cooperation and efficiency gains over time (Murase & Baek, 2021; Murase & Baek, 2023).
- `mpcr`: Almost universally modeled in PGG and adjacent papers (Dong et al., 2019; Brandt et al., 2003).
- `punishment_cost`, `punishment_tech`: Core focus in nearly all direct punishment models; cost-effectiveness is identified as the single most important moderator of efficiency effects (Guala, 2012; Vukov et al., 2013).
- `reward_exists`, `reward_cost`, `reward_tech`: Multiple papers analyze interactions of reward and punishment (Dong et al., 2019; Rand & Nowak, 2013). Reward is usually found more efficiency-promoting than punishment.
- `all_or_nothing`: Directly manipulated in several PGG theory models (Archetti et al., 2011; Brandt et al., 2003).
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Addressed in reputation/norm-enforcement literature (Milinski, 2016; Raihani et al., 2015; dos Santos et al., 2011).

**Indirectly Informed / Contextual:**
- `chat`: Discussed mostly as a moderator for communication and information; shown to improve cooperation/efficiency but not often manipulated alongside punishment (Anderies et al., 2011; Milinski, 2016).
- `default_contrib`: Occasionally addressed in framing or behavioral outcome studies.
- `punishment_magnitude`: Less frequently specified than punishment cost, but effects are inferred from cost:impact ratio studies (Vukov et al., 2013).
- `punishmentExists`: All direct analyses include on/off comparisons; many adjacent papers address analogous toggling of punishment mechanisms.

**Effectively Missing or Only Contextual:**
- *Few or none* address framing features (e.g., `default_contrib`) in a way that links to efficiency under punishment.
- In most papers, **chat**, `show_n_rounds`, `show_other_summaries`, and `show_punishment_id` are discussed as information or transparency mechanisms, not systematically varied in formal models.
- Features like **player-level heterogeneity, explicit identity revelation, or continuous vs. binary contributions** (beyond all-or-nothing) are seldom analyzed in direct relation to efficiency effects of punishment.

# 7) Important Limitations

- The evidence base is **almost exclusively theoretical**; **empirical/experimental calibration is absent** in this set, precluding strong quantitative prediction or external validity checks.
- **Direct analysis of control (no-punishment) efficiency as a predictor** for treatment (punishment-enabled) efficiency is rare; most theory papers do not express relationships in these terms, focusing on marginal parameter shifts, thresholds, or bifurcations instead.
- **Game design dimensions are often considered singly, not in combinatorial interactions**—for example, the critical role of communication or reward mechanisms is discussed separately from changes in punishment cost or group structure in most models.
- **Antisocial punishment, retaliation, norm enforcement errors, and second-order free rider problems** are widely acknowledged but not always systematically modeled or mapped to prediction dimensions.
- **Outcomes are often behavioral**, especially in foundational or cognitive-theory literature, making direct translation to efficiency outcomes cautionary.
- **Edge cases, such as antisocial environments, optional participation, or dynamic/ecological resource constraints**, reveal that transformative efficiency effects from punishment are not universal, but these distinctions are often context-specific and thus hard to generalize.
- **Some key moderators such as meta-incentives, exclusion power, or real-world norms** (vs. abstract game rules) are only infrequently mapped to the design dimensions used in predictive modeling.

---

**In summary:**  
The literature provides **strong theoretical guidance** that effectiveness and efficiency gains from enabling punishment in PGG-like environments **are highly contingent on game design dimensions**, especially group size, punishment cost, type of punishment (peer vs. institutional/exclusion), and informational structures. While most models predict at least some efficiency gain in enabling punishment under "favorable" parameterizations, there is **substantial and explicit caution** that mis-specified punishment (high cost, low impact, high antisocial use, absence of supporting norms/communication/institutions) may yield little to no improvement—and sometimes even reduce efficiency. **Empirical calibration and direct mapping from control to treatment efficiency via these dimensions is absent**, so downstream predictions should be constructed as **moderated, mechanism-based extrapolations** rather than uncalibrated, effect-size estimates.
