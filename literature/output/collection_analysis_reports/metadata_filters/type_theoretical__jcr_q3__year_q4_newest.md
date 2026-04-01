# 1) Evidence Base

This paper set is comprised exclusively of theoretical papers (no empirical or experimental results), totaling 31 items. The theoretical analyses span mathematical models, agent-based simulations, and conceptual frameworks. The coverage is moderately broad in that it includes multiple approaches to public-goods games (PGG), but there is a noticeable emphasis on classic PGGs, structured and spatial variants, and neighboring social dilemmas (e.g., volunteer’s dilemmas, collective risk, indirect reciprocity). Most papers directly address punishment or sanctioning mechanisms, though sometimes the focus is on institutional rather than peer punishment. There is a strong representation of payoff-based outcomes, and several papers derive explicit or semi-explicit formulas linking design parameters to group efficiency or payoff, but many others focus on cooperation or contribution behaviors. Empirical validation of these results is absent—this constitutes a limitation for predictive calibration.

# 2) Task Relevance

### PGG or Variant (`pgg_or_variant`)
- **exact**: A substantial subset of the papers model classic linear or threshold public goods games (e.g., Prétôt et al., 2024; Wu & Sun, 2022; Wang et al., 2023; Guo et al., 2023; Du et al., 2023; Kristensen et al., 2025; Duong et al., 2024).
- **close**: Several model structurally similar games: workplace/team production (Dughera, 2022), farmer's crop burning (Vinayak, 2025), n-player dilemmas, and structured population models (Cooney, 2025; Kurokawa, 2023; Fontanari & Santos, 2024).
- **adjacent/weak**: A considerable proportion examine related games—indirect reciprocity, volunteer's dilemma, prisoner's dilemma, or resource allocation games—but with payout structures or player interaction rules different from canonical PGGs.

### Punishment or Sanctions (`punishment_or_sanctions`)
- **exact**: Many papers directly manipulate peer or institutional punishment as a primary mechanism (Prétôt et al., 2024; Wu & Sun, 2022; Wang et al., 2023; Guo et al., 2023; Du et al., 2023; Liu et al., 2024; Dughera, 2022; Vinayak, 2025; Cooney, 2025).
- **close/adjacent**: Others look at exclusion/ostracism, reward, or group-level sanctions (e.g., Kroumi, 2025), and some only mention punishment at the conceptual level or treat “punishment-like” mechanisms (e.g., selective extinction, conformity-based norms, or informal social sanctions).

### Efficiency or Related Payoff Outcomes (`efficiency_or_related_payoff_outcome`)
- **exact/close**: Around half the set reports efficiency, group payoff, or welfare outcomes directly (Prétôt et al., 2024; Duong et al., 2024; Dughera, 2022; Vinayak, 2025; Cooney, 2025; Kurokawa, 2023; Kristensen et al., 2025; Fontanari & Santos, 2024; Murase, 2025; Kroumi, 2025; Gros, 2022).
- **adjacent/weak**: Others present only behavioral outcomes (contributions, cooperation rate, norm compliance), arguing that these may be correlated with efficiency but not mapping them explicitly (Wu & Sun, 2022; Guo et al., 2023; Du et al., 2023).
- **none**: Some focus exclusively on conceptual or social mechanisms without addressing efficiency or payoff.

**Conclusion**: The relevance for the prediction task is highest in the subset that targets (i) classic or variant PGGs, (ii) experimentally manipulable punishment conditions, and (iii) efficiency or related payoff outcomes. A significant portion of the set is contextually or mechanistically relevant but lacks either direct correspondence to all three focal dimensions or empirical grounding.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes**: Efficiency, group payoff/earnings, welfare, surplus, fixation probability of cooperation (as a proxy for long-term average group welfare). These are measured or calculated in roughly half of the papers (e.g., Prétôt et al., 2024; Duong et al., 2024; Dughera, 2022; Vinayak, 2025; Cooney, 2025; Kurokawa, 2023; Kristensen et al., 2025; Fontanari & Santos, 2024; Kroumi, 2025).
- **Non-Payoff Behavioral Outcomes**: Contribution rates, cooperation rates, norm compliance rates, punishment/reward frequencies, and similar. Many papers report only these (e.g., Wu & Sun, 2022; Guo et al., 2023; Du et al., 2023; Kido & Takezawa, 2024), articulating that these are distinct from efficiency/payoff.
- **Conceptual/Mechanism Outcomes**: Papers focusing on credibility, reputation, enforcement, or group stability mechanisms, seldom providing quantitative outcome measures.
- **Ambivalence**: Some papers mix these, discussing mechanisms relating norm compliance to potential group payoffs but stopping short of quantifying this relationship.

**Distinction is consistently made** between efficiency/payoff outcomes and non-payoff behavioral outcomes in theoretical presentation, though empirical mapping is often absent.

# 4) Main Findings Relevant To Prediction

### (A) When is Punishment Efficiency-Enhancing?

- **Institutional (collective) punishment** robustly increases efficiency if sufficiently resourced, with explicit boundaries for when this holds (Prétôt et al., 2024; Duong et al., 2024; Sugaya & Wolitzky, 2023).
- **Peer punishment** (unilateral) frequently fails due to the second-order free-rider problem and may not achieve efficiency, unless some agents “seed” initial monitoring or punishment costs are sufficiently low (Prétôt et al., 2024; Cooney, 2025).
- **Cost and Technology of Punishment**: Lower punishment costs and higher punishment effectiveness (punishment_tech) expand the parameter space where punishment increases efficiency (Guo et al., 2023; Cooney, 2025; Dughera, 2022).
- **Group Size**: As player_count increases, sustainment of efficiency relies more on targeting and involuntary sanctions. Purely voluntary punishment or reward systems lose potency, especially in the presence of “bad apples”—types who always defect (Sugaya & Wolitzky, 2023; Kurokawa, 2023).
- **Reward Regimes**: Efficient motivation/charisma (a kind of reward) is, in some models, even more effective and always at least as efficient as punishment, particularly with high-skill agents (Dughera, 2022; Vinayak, 2025; Wang et al., 2023).
- **Hybrid Mechanisms** and thresholds (Duong et al., 2024) are sometimes optimal—punishment alone may not suffice, but added reward narrows the zone of low efficiency.

### (B) Situations Where Punishment Does Not Increase, or Even Reduces, Efficiency

- If the cost of punishment is large relative to gains from cooperation, punishment may raise cooperation but reduce net group payoff (Cooney, 2025; Kurokawa, 2023).
- In very large groups where defectors cannot be reliably identified, or in the presence of high error rates in detection, punishment may be wasteful or counterproductive unless specialized mechanisms are present (Murase, 2025; Sugaya & Wolitzky, 2023).
- Psychological and social comparison effects (envy, reputation traps) can undermine the efficiency benefits of both punishment and reward (Gros, 2022; Wittek, 2022).

### (C) When is the Efficiency Impact Non-Monotonic or Conditional?

- The relationship between increasing punishment cost/magnitude and efficiency is often non-monotonic, with optimal zones for maximal group payoff (Cooney, 2025; Duong et al., 2024).
- Effectiveness of punishment is often contingent on other dimensions—group structure, monitoring technology, the detectability of defection, and the presence of hybrid incentive mechanisms (Murase, 2025; Prétôt et al., 2024; Duong et al., 2024).

# 5) Prediction Guidance

**Direct prediction guidance** is strongest when:

- The game is a classic or close variant PGG, with explicit efficiency outcomes, and punishment parameters (cost, magnitude, tech) and group size (player_count) are specified (Prétôt et al., 2024; Cooney, 2025; Dughera, 2022; Vinayak, 2025; Sugaya & Wolitzky, 2023).
- **Control game efficiency** (without punishment) is low: If punishment is implemented with low enough cost and sufficient severity, the model predicts a large (sometimes dramatic) efficiency increase. Enabling punishment in these cases frequently raises efficiency, sometimes to near-full cooperation (Vinayak, 2025; Prétôt et al., 2024).
- **Punishment is peer-based, high cost, and group size is large**: Expected efficiency gain disappears or becomes negative (Cooney, 2025; Kurokawa, 2023). There may even be a net loss due to wasted resources on punishment.
- **Institutional or collective punishment (tax-based, group-funded) mechanisms**: These arrangements, when properly parameterized, can lead to high efficiency, and are superior to peer punishment under most models (Prétôt et al., 2024; Wang et al., 2023; Duong et al., 2024).
- **Non-payoff behavioral findings** (increased cooperation rates): These are only weakly predictive of efficiency improvements—unless accompanied by analysis of punishment cost, they risk overestimating efficiency gains (Wu & Sun, 2022; Guo et al., 2023; Du et al., 2023).

**Generalizable prediction rules supported by the literature:**
- Enabling punishment increases efficiency only if (a) the combined cost of punishment is less than or comparable to the efficiency gain, and (b) punishment is sufficiently effective at deterring defection.
- Magnitude of efficiency increase is modulated by group size, punishment cost, and punishment technology. There are strong threshold effects.
- Where available, hybrid or institutional sanctioning models provide the clearest quantitative mapping from design to expected efficiency (Prétôt et al., 2024; Duong et al., 2024).

# 6) Design Dimensions Highlighted Across Papers

- **Directly Informed**:
    - `player_count` (group size): Central in nearly all quantitative and mechanistic models. Increasing group size generally reduces the relative efficacy of peer punishment unless compensated by institutional design.
    - `mpcr` (marginal per-capita return/multiplier): A key moderator; higher MPCRs enable easier transitions to high-efficiency equilibria.
    - `punishment_cost` and `punishment_tech` (effectiveness/severity): Explicitly modeled and shown to critically affect both cooperation and efficiency.
    - `reward_exists`, `reward_cost`, `reward_tech`: Explored in several hybrid models; direct comparison with punishment outcomes.
    - `all_or_nothing`: Some models use binary/continuous contribution, affecting stability and equilibrium properties.
- **Indirectly Informed**:
    - `num_rounds`: Discussed in dynamic/iterated models (some phase diagrams), but less often a focal parameter.
    - `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Sometimes included (especially in structured/normative models) as factors influencing the visibility of behavior and sanctions, but not generally linked by explicit formula to efficiency.
    - `default_contrib`: Only tangentially addressed; not typically a main dimension in theory papers but relates to framing effects and initial conditions.
    - `chat`: Virtually absent except as a conceptual moderator (not parameterized).
- **Effectively Missing or Contextual**:
    - `chat`, `default_contrib`, `show_other_summaries`, `show_punishment_id`: Not parameterized in a way to inform efficiency predictions.
    - Most models do not address payoff framing, communication, or second-order information visibility as primary levers.
    - No paper quantitatively links outcome to `chat` or framing; their relevance for efficiency prediction is speculative in this literature.

# 7) Important Limitations

- **Lack of Empirical Validation**: All included work is theoretical or simulation-based; empirical magnitude, noise, and real-world feasibility are untested.
- **Behavioral–Payoff Disconnect**: Many studies focus on cooperation/contribution rates, which do not map perfectly onto group efficiency due to the non-negligible cost of (especially peer) punishment. Behavioral gains may be erased, or overcompensated, by punishment costs.
- **Peer vs. Institutional Punishment**: Peer punishment efficacy is consistently undermined by second-order free-riding in large groups, but the literature does not always specify when “punishment enabled” means peer, institutional, or hybrid—results may not generalize across implementation forms.
- **Sparse Coverage of Some Design Dimensions**: Communication (`chat`), framing (`default_contrib`), and second-order information (`show_punishment_id`) are largely under-explored in relation to efficiency outcomes.
- **Model Dependency and Threshold Effects**: Many findings depend critically on sharp thresholds or phase transitions (e.g., punishment cost, group size, MPCR), making out-of-sample prediction sensitive.
- **Contextual Mechanisms underexplored**: Social mechanisms such as reputation, group dissolution, and norm formation are occasionally modeled but their interplay with efficiency outcomes is not consistently parameterized or measured.
- **Control Efficiency Baseline**: Several models are most informative when control (no-punishment) efficiency is known to be low—if baseline cooperation is high, enabling punishment can sometimes reduce efficiency due to enforcement costs.
- **Absence of Empirical Noise**: Real-world idiosyncrasies (bounded rationality, error, communication, enforcement friction) are addressed sporadically if at all.

---

## Summary

**Overall, the literature provides solid mechanistic and quantitative guidance for predicting the effect of enabling punishment on group efficiency in public-goods-game-like settings—particularly when key design parameters (group size, MPCR, punishment cost/effectiveness) are specified and the distinction between peer and institutional punishment is clear. Efficiency increases are most reliably predicted for institutional punishment with moderate costs and high effectiveness, especially when baseline (control) efficiency is low. Peer punishment in large groups is generally ineffective or even harmful to efficiency due to second-order free-riding and enforcement cost. Behavioral measures (cooperation, contribution rates) should not be over-interpreted as efficiency gains unless costs are fully accounted for. Several relevant prediction dimensions—especially communication and information revelation—remain under-theorized, and all conclusions are moderated by the lack of empirical calibration.**
