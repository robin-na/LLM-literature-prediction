# 1) Evidence Base

The paper set consists entirely of empirical studies, with seven laboratory or field experiments and one observational field intervention. Of the eight papers, only one (Amirova et al., 2022) is a field experiment directly featuring peer punishment in a repeated public-good-like context. The others range from classic and step-level public goods game (PGG) laboratory studies, competitive multi-player resource games, third-party punishment lab games, to organizational surveys and field interventions on norm adoption. No theoretical or purely mechanism-oriented papers are included. The set is relatively broad in including a variety of social dilemma and resource management contexts, but narrow and sparse concerning direct empirical evidence on peer punishment effects on efficiency in standard or near-standard PGGs, especially with explicit efficiency or payoff outcomes.

# 2) Task Relevance

### pgg_or_variant
- **Relevance:** Ranges from `close` (e.g., lab experiments with repeated PGGs or binary social dilemmas: Amirova et al., 2022; Zhang et al., 2019; Gomez-Ruiz & Sánchez-Expósito, 2020; Herne et al., 2023) to `adjacent` (games modeling related social dilemmas with competitive, investment, or market components: Suzuki & Ishiwata, 2022; Ferguson, 2021; Berger, 2021).
- **Summary:** Several papers use games structurally close to the PGG; fewer represent classic PGG structures directly.

### punishment_or_sanctions
- **Relevance:** Only two papers (`Amirova et al., 2022; Suzuki & Ishiwata, 2022`) implement a direct punishment or sanction mechanism. Others are `adjacent` (e.g., third-party punishment, informal norm enforcement) or lack any punitive component, focusing instead on communication, role models, or feedback.
- **Summary:** Only a minority provide direct evidence on the effect of punishment; most discuss no such mechanism or only informal analogues.

### efficiency_or_related_payoff_outcome
- **Relevance:** Only three papers (`Amirova et al., 2022; Suzuki & Ishiwata, 2022; Zhang et al., 2019`) have outcomes close or exactly matching efficiency or group payoff. Others measure behavioral outcomes or provide only weakly related economic value/organizational performance indicators.
- **Summary:** Explicit efficiency or group payoff outcomes are underrepresented compared to behavioral indicators (contribution rates, norm adoption).

# 3) Outcomes Measured In The Literature

- **Payoff-related Outcomes:**  
  - *Close/Exact:*  
    - Explicit group payoff or efficiency (Suzuki & Ishiwata, 2022; Zhang et al., 2019; Herne et al., 2023—except no punishment treatment).
    - Collective investment as a behavioral proxy for group efficiency (Amirova et al., 2022; not reported as explicit payoff ratios).
  - *Weak/Adjacent:*  
    - Economic value or competitiveness (Holubcik et al., 2023), but not in a game-theoretic or PGG sense.
    - Distributional effects, but not group efficiency (Ferguson, 2021).
- **Non-payoff Behavioral Outcomes:**  
    - Contribution or cooperation rates, free-riding responses, norm adoption (Berger, 2021; Gomez-Ruiz & Sánchez-Expósito, 2020).
    - Choices between compensation vs. punishment (Ferguson, 2021).
    - Behavioral indicators of synergy and collaboration (Holubcik et al., 2023).

# 4) Main Findings Relevant To Prediction

**Direct Evidence on Punishment and Efficiency:**
- **Amirova et al. (2022):** In a repeated field-social dilemma (close to PGG), *enabling punishment lowered collective investment* and thus reduced efficiency, counter to standard theory. Communication (chat) robustly increased investment, but did not always prevent sub-optimal (low-efficiency) equilibria. The main measurement is collective investment, which tracks efficiency closely but is not the same as explicit group payoff.
- **Suzuki & Ishiwata (2022):** In a competitive, repeated market game (adjacent to PGG) with a "punishment" (carbon tax), *group profit (efficiency)* increased following the introduction of the tax, but not significantly. The effect was only realized after implementation—announcement alone had no effect.

**Indirect or Adjacent Evidence:**
- **Role Models and Communication:**  
  - Communication and structured dialogue consistently raise cooperation and *efficiency* (Herne et al., 2023; Zhang et al., 2019) but in the absence of punishment.  
  - Adding a consistent contributor (role model) increased both cooperation and group earnings (Zhang et al., 2019).
- **Informal Mechanisms:**  
  - Team identity reduces free-riding among men (Gomez-Ruiz & Sánchez-Expósito, 2020), but not women; only behavioral effects measured.
  - Normative feedback (Berger, 2021) can induce tipping or boomerang in sustainable behavior; outcomes purely behavioral, not efficiency/payoff.
- **Compensation vs. Punishment Preferences:**  
  - Players prefer compensation to punishment in one-shot games with third-party options (Ferguson, 2021), with behavioral (not payoff) outcome emphasis.

**Areas of (Dis)Agreement and Ambiguity:**
- **Field vs. Lab:**  
  - Field evidence (Amirova et al., 2022) indicates that punishment *may lower* efficiency under conditions of high intrinsic motivation, contrary to many lab findings and classic theory.
  - Lab and market simulation evidence (Suzuki & Ishiwata, 2022) finds that appropriately targeted punishment (tax) can support social optimum with limited impact on uncertainty.

# 5) Prediction Guidance

The literature provides only modest direct support for predicting the impact of enabling peer punishment on efficiency in public-goods environments:
- **Punishment can lower efficiency (Amirova et al., 2022):** Particularly in real-world, repeated field social dilemmas where intrinsic motivation is strong, the introduction of punishment may crowd out voluntary cooperation, reducing overall efficiency-related outcomes—even when communication is possible.
- **Punishment can increase or not affect efficiency (Suzuki & Ishiwata, 2022):** In structured, competitive environments where the punishment mechanism directly targets negative externalities (carbon tax), efficiency (group profit) may increase or remain unchanged, especially if the mechanism is salient and actually implemented.
- **Communication reliably increases efficiency:** Multiple studies show communication improves efficiency, but this effect is independent from punishment and cannot be used to extrapolate punishment effects.
- **Behavioral improvements ≠ Payoff improvements:** Many papers document positive behavioral effects—higher cooperation or norm adherence—but do not demonstrate (or directly measure) efficiency gains.
- **Predicting treatment efficiency:** Given the mix of findings, one should not assume that adding punishment will always improve efficiency above the control (no punishment) baseline. The presence of strong intrinsic motivation, communication, and field context may invert the expected positive effect of punishment. When making predictions, consider the closeness of the empirical context and whether the outcome measured is truly efficiency/payoff.

# 6) Design Dimensions Highlighted Across Papers

- **Directly Informed Dimensions:**  
  - `player_count` (several studies: Amirova, Herne, Suzuki, Ferguson, Zhang, Gomez-Ruiz)
  - `num_rounds` (most experimental studies)
  - `chat` (Amirova, Herne, Gomez-Ruiz, Zhang)
  - `all_or_nothing` (Herne, Gomez-Ruiz, Zhang, Suzuki, Ferguson)
  - `mpcr` (Herne, Gomez-Ruiz, Zhang, Ferguson)
  - `punishment_cost`, `punishment_tech` (Suzuki, Ferguson, Amirova)
  - `show_n_rounds` (Herne, Suzuki, Gomez-Ruiz, Zhang)
  - `show_other_summaries` (Berger)
- **Indirectly Informed/Only Contextual:**  
  - `default_contrib` (not directly manipulated in any paper; possible in some step-level games)
  - `show_punishment_id` (not reported as a variable)
  - `reward_exists`, `reward_cost`, `reward_tech` (compensation option in Ferguson, but not in a PGG)
- **Effectively Missing:**  
  - Most reward-related dimensions are absent or only notionally addressed.
  - Explicit manipulation of `show_punishment_id` (punisher/rewarder identification) missing.
  - Most studies do not give fine-grained reporting of outcomes subdivided by these variables.

# 7) Important Limitations

- **Scarcity of payoff-focused PGG studies with punishment:** Only Amirova et al. (2022) directly examines punishment's effect on efficiency in a PGG-like context, and does not report explicit efficiency ratios.
- **Reliance on behavioral proxies:** Most studies rely on contribution, cooperation, or investment as proxies, rather than directly measuring group payoff or efficiency.
- **Limited generalizability:** Key studies (e.g., Amirova et al., 2022; Suzuki & Ishiwata, 2022) occur in specific contexts (field irrigation cooperation; simulated energy market). Findings may not generalize to all types of PGGs or lab experiments.
- **Lack of reward mechanism studies:** Reward options are largely unaddressed or only present as adjacent (compensation) mechanisms.
- **Ambiguous or inconsistent effects:** Punishment's effect on efficiency is mixed—one field study shows crowding out, one market simulation shows (non-significant) improvement. Context sensitivity appears high.
- **Missing variance in design dimensions:** Some dimensions (such as identification, reward, default contribution) are absent or barely tested, constraining the scope of predictive modeling.
- **No theoretical synthesis:** All evidence is empirical, so mechanism-based generalizations must be interpreted with caution.

---

**Summary:**  
This literature base suggests that the impact of peer punishment on efficiency in public-goods-like games is highly context-dependent. While classic economic models and lab studies may predict efficiency gains from punishment, this is not consistently borne out in field experiments, where crowding out of intrinsic motivation is a substantial risk. Communication robustly increases efficiency independently. Key design dimensions—such as player count, number of rounds, chat, and (less so) punishment cost/technology—are replicated across studies, but many other dimensions are thinly addressed or missing. Predictions should be cautious: punishment may lower, not raise, efficiency relative to control, especially when intrinsic cooperative motivation is present. Explicit attention to context, outcome measurement, and intervention design details is essential.
