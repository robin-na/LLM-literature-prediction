# 1) Evidence Base

**Paper Set Composition:**  
- All papers are theoretical; there are no empirical or experimental studies.
- The set is extensive (165 papers), with most theoretical models centered on Public Goods Games (PGGs) or close variants, and a secondary emphasis on adjacent dilemmas (e.g., Prisoner's Dilemma, common-pool resources, trust games).
- A subset of papers provide direct, quantitative, or simulation-based predictions for efficiency (ratio of group payoff to the cooperative optimum) as affected by punishment. Many others report only on cooperation rates, strategy prevalence, or other behavioral metrics.
- The evidence is broad and granular for the theoretical effect of punishment on efficiency in PGGs, but there is a lack of direct empirical outcome measurements and significant heterogeneity in models, mechanisms, and key assumptions.

---

# 2) Task Relevance

**pgg_or_variant:**  
- **Exact:** Major coverage; numerous models are calibrated to canonical or spatial PGGs, including repeated, all-or-nothing, and continuous contribution variants.
- **Close:** Many papers treat common-pool resource games, collective-risk dilemmas, or group-oriented resource allocation games with mechanics nearly identical to PGGs.
- **Adjacent:** Other papers focus on Prisoner's Dilemma, trust games, or resource-sharing models; useful for mechanism insight but lacking direct translation to n-player PGGs.

**punishment_or_sanctions:**  
- **Exact:** Many papers explicitly model peer or institutional punishment as costly, targeted reductions of others' payoffs, or exclusion mechanisms. Both peer and pool punishment receive detailed treatment.
- **Close:** Coverage includes related sanctions: exclusion, central power, institutional rules, third-party enforcement, deterrence, and practical variants (e.g., bribery, metanorms, hybrid reward–punishment, probabilistic or graded sanctions).
- **Adjacent/Weak:** Some models treat only reputation systems, social exclusion, gossip/ostracism, or "punitive" mechanisms that are functionally similar but not formal costly peer punishment.

**efficiency_or_related_payoff_outcome:**  
- **Exact or Close:** ~40% of the most relevant papers report or mathematically analyze group efficiency, welfare, or average payoff as a main outcome.
- **Adjacent/Weak:** The remainder focus on contribution or cooperation rates, norm compliance, or evolutionary stability. Many such models infer efficiency only indirectly via higher cooperation fractions, but this translation is not always warranted, especially when punishment carries explicit costs.

---

# 3) Outcomes Measured In The Literature

**Payoff-based (Efficiency) Outcomes:**  
- *Directly measured in a substantial but minority fraction* (e.g., Bühren et al. 2023; Jia & Wang 2024; Lu et al. 2024; Ohdaira 2025): Total group payoff, efficiency relative to optimum, welfare, surplus, coins generated, social welfare, total earnings.
- *Adjacently measured* in resource games, trust games, or variants: "Resource sustainability," "accumulated wealth," or "market size" serve as proxy efficiency metrics.

**Non-payoff Behavioral Outcomes (not efficiency):**  
- *Much of the literature* uses: cooperation rate, prevalence of strategies (cooperator/defector/punisher), norm adherence, frequency of punishment, or stability of behavior clusters.
- Many models conflate increased cooperation with higher efficiency without explicit consideration of punishment cost or resource waste.
- Some discuss institutional prevalence (e.g., adoption of enforcement mechanisms), norm internalization, or group achievement as behavioral proxies for efficiency.

---

# 4) Main Findings Relevant To Prediction

**A. Direction and Contingency of Punishment’s Effect on Efficiency:**  
- **Punishment can increase group efficiency** when: baseline (control) cooperation is low, punishment is sufficiently strong but not excessively costly, group size is moderate, and monitoring is efficient (Bühren et al., 2023; Zefferman, 2023; Lu et al., 2024; Ohdaira, 2025; Asgharpourmasouleh et al., 2017).
- **Punishment may decrease efficiency** if: it is costly and the marginal gain in cooperation does not offset these costs, particularly in very cooperative groups (Bühren et al., 2023; Ezeigbo, 2017; Kroupa, 2014; Matsuzawa & Tanimoto, 2018).
- **Institutional/third-party punishment** is generally more effective than uncoordinated peer punishment when institutional effectiveness is high and enforcement costs are moderate (Zefferman, 2023; Mohlin et al., 2023; Garrido et al., 2025; Lie-Panis et al., 2024).
- **Heterogeneity in group social preferences, consensus thresholds, and preference instability**: The efficiency boost from punishment is highly sensitive to the group’s composition, ability to reach consensus on punishment, and the stability of willingness to punish (Bühren et al., 2023; Gao & Li, 2023).
- **Punishment design (cost, magnitude, technology)**: Severe and well-targeted punishment deters free riding and can support full efficiency; mild or misdirected punishment is often wasteful (Botta et al., 2024; Zefferman, 2023; Nirjhor & Nakamaru, 2023).
- **Unintended consequences**: Antisocial punishment, bribery, or misdirected punishment can erode or even reverse efficiency gains, particularly when punishment is not well-targeted or social structure allows for evasion (Gao et al., 2023; Ding et al., 2025; Ezeigbo, 2017; Dos Santos & Knoch, 2021).
- **Interaction with group size and rounds**: Larger groups with hierarchical or institutional monitoring better sustain efficiency gains; too large groups or very short games usually diminish punishment’s effectiveness (Powers et al., 2023; Zefferman, 2023).
- **Interaction with rewards and alternatives**: When reward is available, combinations (hybrid or threshold-based schemes) may achieve equal or higher efficiency than punishment alone, but pure reward is usually inferior in hard dilemmas (Lu et al., 2024; Wang et al., 2024; Garrido et al., 2025).

**B. Baseline Efficiency as a Moderator:**  
- **Marginal effect**: If the control (no-punishment) efficiency is already high (e.g., due to network reciprocity, reputation, or communication), enabling punishment may yield little or negative net efficiency change (Kroupa, 2014; Gao et al., 2025).
- **Most positive effects** are observed when baseline efficiency is low and social or institutional conditions otherwise preclude stable cooperation (Botta et al., 2024; Asgharpourmasouleh et al., 2017).

**C. Non-payoff models:**  
- Cooperation rates almost always increase with well-designed punishment, but “efficiency,” defined as net group gain relative to the theoretical maximum, increases *only* if the cost and targeting of punishment are favorable.

---

# 5) Prediction Guidance

**For the Task:** Given game design dimensions and control game efficiency, predict treatment efficiency when peer punishment is enabled.

**Guidance from the Literature:**
- *Use control efficiency as a baseline*: The effect of enabling punishment is conditional; expect greater efficiency gains when control efficiency is low.
- *Map design dimensions* to expected outcomes:
    - **player_count (group size):** Efficiency gains from punishment are maximized in small to moderate groups or where hierarchical/institutional mechanisms function well; too large groups may dilute punishment effectiveness unless centrally coordinated (Zefferman, 2023; Powers et al., 2023).
    - **num_rounds:** Longer games enhance the efficiency benefit of punishment by allowing deterrence and learning (Kroupa, 2014).
    - **punishment_cost & punishment_tech:** High-cost or inefficient punishment often reduces total efficiency unless punishment effectiveness (the ratio of impact to cost) is high (Zefferman, 2023; Botta et al., 2024).
    - **punishment_magnitude:** Severe punishment is generally needed to move low-control-efficiency groups to high efficiency, but excessive severity can crowd out voluntary cooperation and reduce welfare (Hernandez et al., 2022).
    - **mpcr (marginal per-capita return):** Higher MPCR makes cooperation more achievable in control, so marginal benefit from punishment may be reduced.
    - **reward_exists:** If rewards are present, efficient punishment–reward hybrids can be superior to either alone (Lu et al., 2024; Garrido et al., 2025).
    - **chat, show_other_summaries, show_n_rounds:** Social information and communication can substitute for or interact with punishment, sometimes reducing its added value (Kroupa, 2014).
- *Expect non-monotonic effects*:
    - If punishment cost is too high or the group is highly cooperative in baseline, punishment may not increase efficiency and can reduce it.
    - If punishment is poorly targeted, allows antisocial use, or enables costly retaliation/bribery, efficiency gains may be weak, null, or negative (Gao & Li, 2023; Ezeigbo, 2017; Hernandez et al., 2022).
    - Institutional/third-party punishment is often more efficient than decentralized peer punishment, as long as collective action/consensus costs do not overwhelm the benefit (Powers et al., 2023; Garrido et al., 2025).
- *Default prediction*: Punishment increases efficiency relative to control when baseline is low, punishment is not too costly, and the technology enables targeted, sufficient, but not excessive sanctions; otherwise, the effect is small or negative.

---

# 6) Design Dimensions Highlighted Across Papers

- **Directly informed:**  
    - `player_count, num_rounds, all_or_nothing, mpcr, punishment_cost, punishment_tech, reward_exists` (frequency and cost of punishment, institution type, group size, rounds, structure of contributions, marginal return, and presence of rewards are specifically analyzed in many models).
- **Indirectly informed:**  
    - `chat, default_contrib, reward_cost, reward_tech, show_n_rounds, show_other_summaries, show_punishment_id` (outcomes or mechanisms are discussed in relation to group communication, social information, or visibility of punishment, but less commonly as main variables).
- **Contextually discussed/missing:**  
    - `default_contrib, show_punishment_id` (rarely a model focal point; mostly discussed as qualitative moderators or not included at all).
    - `show_other_summaries, show_n_rounds` are often not core variables but are occasionally referenced as part of treatment or information structure manipulations.
    - `chat` is sometimes present in model extensions but not always parameterized.
- **Reward mechanisms** receive some direct attention, but are less commonly modeled in tandem with punishment except in hybrid/threshold models.

---

# 7) Important Limitations

- **Lack of Empirical Research:** All evidence is theoretical; there are no empirical or experimental efficiency measures to validate predictions.
- **Behavioral Outcome/Efficiency Disconnect:** Many models use cooperation rate as a proxy for efficiency, but the translation to net group payoff depends critically on the specific costs and inefficiencies of punishment—often neglected or modeled abstractly.
- **Model Heterogeneity & High Conditionality:**  
    - Model structure (peer vs. pool punishment, spatial vs. well-mixed populations, network structure, punishment targeting, social information, preference instability) moderately to strongly alters predicted effects.
    - Parameter regimes (punishment cost, severity, group size, frequency, baseline efficiency) highly moderate both the direction and magnitude of efficiency changes.
    - Some models assume away important real-world features (second-order free riders, antisocial punishment, imperfect monitoring), which empirical studies show can have substantial effects.
- **Sparse Coverage of Some Dimensions:** Game features like chat, information visibility, and default contributions are rarely included in sufficient detail to make them strong predictors.  
- **Nonlinear/Non-monotonic Effects:** Predictions cannot assume additive impacts; in many models, punishment efficacy or efficiency effects change qualitatively above or below parameter thresholds.
- **No Direct Guidance for Mixed/Complex Interventions:** While many models analyze punishment or reward, complex, real-world settings with both (or with endogenous institution adoption) are less often fully characterized; mapping multi-dimensional interventions to predicted efficiency remains a challenge.
- **Policy/Mechanism Assumptions:** Some models assume perfect rationality, reputation, or enforcement capability, which may not be realistic; real systems often experience anti-social punishment, bribery, incomplete observation, or preference instability that can undermine theoretical efficiency gains.

---

**In summary:**  
The literature provides strong, multi-model theoretical support that enabling punishment increases efficiency relative to control *when* baseline cooperation is low, punishment is effective and not overly costly, and the game design supports effective deterrence and minimal waste. The moderating effects of game design dimensions—including group size, rounds, punishment cost and targeting, consensus/prior coordination, and information availability—are supported by detailed models and phase diagrams. However, theoretical predictions sometimes overestimate real efficiency gains due to neglected costs, behavioral noise, or unmodeled social dynamics, and the absence of empirical/experimental studies is an important caveat for applied prediction.
