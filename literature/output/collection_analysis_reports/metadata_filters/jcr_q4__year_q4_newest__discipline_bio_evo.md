# 1) Evidence Base

The current paper set is **entirely theoretical**, with all three papers presenting formal models without new empirical or experimental results. The set is relatively **narrow** for the intervention of interest—peer punishment in conventional public goods games (PGGs)—because only one paper (Ishikawa & Fontanari, 2025) addresses punishment directly, and even then, only institutional punishment is modeled (not peer punishment). The other two papers (Kurokawa, 2022; Peña et al., 2024) concern adjacent game forms—repeated Prisoner's Dilemmas and binary-action threshold games—neither of which include explicit punishment or peer sanctions. Across the set, all papers focus on **payoff-related outcomes** at equilibrium. The largest gap is the absence of any empirical or experimental evidence, as well as the absence of direct modeling of peer punishment technologies.

# 2) Task Relevance

Assessing relevance on the three specified axes:

- **pgg_or_variant**:  
  - Ishikawa & Fontanari (2025): `exact` (models N-person Public Goods Game).
  - Kurokawa (2022), Peña et al. (2024): `adjacent` (model closely related social dilemma games—repeated PD and the shirker's dilemma/threshold collective action).

- **punishment_or_sanctions**:  
  - Ishikawa & Fontanari (2025): `exact` (models institutional punishment but *not* peer punishment).
  - Kurokawa (2022), Peña et al. (2024): `adjacent` (analyze partner switching or lack of mechanisms, not explicit punishment).

- **efficiency_or_related_payoff_outcome**:  
  - All three: `exact` (all directly study efficiency, welfare, or total payoff outcomes).

**Summary**: The literature base is moderately relevant: it is exact on efficiency or payoff, but less direct for the specific *peer* punishment mechanism and varied in the mapping to canonical PGGs. Its strongest evidential value is for how efficiency in collective action varies with punishment cost, institutional punishment availability, group size, and related payoff parameters.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes (exact relevance):**
- **Efficiency (group payoff relative to full cooperation):** All three papers focus on efficiency or expected group payoff.
- **Probability of Public Good Provision:** Peña et al. (2024) analyze the likelihood the collective action succeeds, which connects to welfare.
- **Equilibrium Welfare/Surplus:** All three papers analyze stationary payoff outcomes under equilibrium or evolutionary stability.

**Non-payoff behavioral outcomes:**
- **Frequency of Cooperators or Punishers:** Modeled as equilibrium strategies or population composition but always linked back to aggregate efficiency, not studied for their own sake.
- **Behavioral Dynamics (partner switching, threshold crossing):** In Kurokawa (2022), partner switching is an enforcement mechanism, not a direct measure of outcome.

**Distinction:** The outcome measures directly map to the efficiency concept relevant for prediction, rather than to contribution rates or norm compliance.

# 4) Main Findings Relevant To Prediction

**Punishment and efficiency:**
- **Ishikawa & Fontanari (2025):**  
  - Institutional punishment can enable a dramatic jump in efficiency (group payoff) if the cost-to-punishers is low enough relative to fines.  
  - Efficiency gains are not universal: zero-efficiency equilibria (all-defectors) remain stable; group dynamics, parameter values, and initial conditions are critical.
  - Cost-sharing among punishers expands the set of parameter values supporting high efficiency.  
  - Larger groups require more punishers to achieve institutional enforcement; the relationship to group size is complex.
  - Findings are **for institutional punishment, not peer punishment**; therefore, their transfer to the peer punishment setting is uncertain.

**Baseline effects without punishment:**
- **Peña et al. (2024):**  
  - In threshold PGG-like games with no punishment, efficiency generally declines with group size.
  - Increased volunteer proportions in larger groups do *not* translate to higher efficiency.
- **Kurokawa (2022):**  
  - In repeated interactions with partner choice (walk-away as a sanction), efficiency can be high if the game is not too "harsh" (i.e., moderate costs, low noise, stable relationships).
  - Absence of partner choice or adverse parameter values leads to low efficiency baselines.

**Sanctions other than punishment:**
- **Kurokawa (2022):**  
  - Partner switching, while not the same as costly punishment, serves an adjacent role—deterring defection and potentially raising efficiency.

**Parameter sensitivity:**
- Across the set, efficiency improvements from introducing sanctioning mechanisms (punishment, partner choice) depend on:
  - **Cost-to-benefit or cost-to-punisher ratios** (`mpcr`, `punishment_cost`)
  - **Group size** (`player_count`)
  - **Thresholds for enforcement action**
  - **Game stability and feedback (number of rounds, exogenous shocks)**

# 5) Prediction Guidance

**Implications for predicting efficiency with peer punishment:**
- The literature provides *theoretical* support for the possibility that enabling sanctions can considerably increase efficiency, mostly contingent on favorable parameters—especially the cost of punishment relative to its effect, and the ability to reach a critical mass of punishers.
- However, all direct evidence is for **institutional** (not peer) punishment, and adjacent models with voluntary assortment or partner switching; therefore, *quantitative* prediction—especially in typical peer-punishment PGGs—remains uncertain.
- When the control game (no punishment) is at low efficiency, enabling punishment or sanctions may push the game toward high efficiency in some parameter settings, but only if costs are not prohibitive and critical mass conditions are satisfied.
- Larger groups tend to face more difficulty in reaching high efficiency. Cost-sharing or threshold-based punishment may mitigate this.
- **Behavioral path dependence** (e.g., initial proportion of punishers or cooperators) is critical: otherwise stable low-efficiency outcomes can persist.
- No evidence in this set directly addresses effects of chat, reward mechanisms, information visibility, or peer punishment specifics; predictions for these dimensions remain speculative.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed:**
- `player_count` (group size): All papers analyze group size effects.
- `all_or_nothing`: Modeled as binary-action games in Ishikawa & Fontanari and Peña et al.
- `mpcr` (cost-benefit ratio): Central in all models.
- `punishment_cost`: Direct in Ishikawa & Fontanari (institutional). *Not addressed* for peer punishment.
- `punishment_tech` (institutional vs. peer): Only the institutional case modeled.

**Indirectly/contextually informed:**
- `num_rounds`: Kurokawa analyzes repeated interactions.
- `show_n_rounds`, `show_other_summaries`: In Kurokawa, summary/configuration elements impact information/stability.
- `default_contrib`: Not explicitly modeled, but all-or-nothing assumption in play.
- `reward_exists`, `reward_cost`, `reward_tech`: None of the papers include reward mechanisms.
- `show_punishment_id`, `chat`: Not addressed.

**Missing or only peripherally discussed:**
- Peer punishment implementation (`punishment_tech=peer`), communication, visibility of punishment identity, and reward system dimensions are effectively **absent**.

# 7) Important Limitations

- **Lack of peer punishment modeling:** There is *no* modeling of peer punishment, which is the key intervention for the prediction task. All results for punishment derive from institutional enforcement models, which differ in group coordination, information, and scale.
- **No empirical/experimental data:** All papers are theoretical; no observed treatment effects or parameter estimates for real-world settings are provided.
- **Parameter dependency:** Efficiency gains from introducing punishment or sanctions are highly sensitive to unmodeled or context-specific parameters—notably initial conditions, thresholds, and group heterogeneity.
- **Game variants:** Two papers focus on models that are only adjacent to canonical PGGs (repeated Prisoner's Dilemma, binary threshold). Their relevance is indirect, providing baseline expectations rather than direct comparators.
- **Sparse coverage of design dimensions:** Critical prediction features (chat, peer punishment tech, reward existence, payoff information visibility) are missing or only implicit.
- **No direct guidance on control-to-treatment mapping:** The papers do not provide a mapping from observed control efficiency to expected post-punishment efficiency in peer-punishment settings, except through abstract threshold logic.

**Summary:**  
This theory-heavy paper set provides *directional* guidance and mechanistic insight, especially highlighting parameter sensitivities and equilibrium structures in collective action under punishment. However, it cannot directly quantify or reliably estimate the average efficiency effect of enabling *peer* punishment in PGG-like environments for any arbitrary design configuration. Predictions will need to treat effects as contingent and highly uncertain in parameter regions not covered by institutional punishment theory.
