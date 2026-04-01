# 1) Evidence Base

This evidence base is comprised of 104 papers, nearly all theoretical models (no direct empirical or experimental studies reported here). The set is **narrow and deep** with respect to evolutionary game theory models of public goods games (PGG) and closely related social dilemmas, with a focus on the dynamics of cooperation, punishment, and related mechanisms. For the prediction task—forecasting treatment group efficiency (payoff relative to maximum) with punishment enabled—**the core of the evidence base comes from a subset of highly relevant theory papers**, complemented by a large periphery focusing on adjacent mechanisms, behavioral outcomes, or variant game structures.

The **strengths** of the evidence base are:
- Several “exact” or “close” PGG models directly analyze efficiency or group payoff as a main outcome and explicitly manipulate game design dimensions.
- There are a small number of papers that include phase diagrams or explicit equations mapping design features to efficiency outcomes, offering relatively direct translation for prediction tasks.

The **gaps**:
- The vast majority of papers focus on cooperation rates or behavioral frequencies, not on payoff-based outcomes (efficiency/welfare/surplus).
- There is very limited direct empirical data. Most “confirmation” is theoretical or simulation-based (see Vasconcelos et al., 2022 for a notable exception via meta-review).
- Many models use spatial or structured populations, more complex sanction types (e.g., exclusion, reputation), or ecological/resource feedback, extending only “close” or “adjacent” relevance to standard linear PGGs.
- Almost all findings for efficiency rely on **model-specific structures and assumptions**, with context-specific moderators and boundaries.

# 2) Task Relevance

### a) `pgg_or_variant`
- **Exact Relevance:** About 20–25 papers model exact or near-exact PGGs, focusing on standard or voluntary participation, and frequently specifying “classic” design dimensions (e.g., MPCR, group size, punishment cost—see Wang et al., 2025; Vasconcelos et al., 2022).
- **Close/Adjacent Relevance:** Many papers (the bulk) study spatial, ecological, trust-based, or exclusion-augmented variants. Their structure is close to PGGs but may differ in critical details (e.g., trust/leadership/threshold resources).
- **None:** About 10–15% of reviewed papers are non-PGG or non-social dilemma settings (ultimatum games, bargaining, pure network structure).

### b) `punishment_or_sanctions`
- **Exact:** Core subset explicitly manipulates peer or institutional punishment and/or exclusion as a design variable—often in mathematical, agent-based, or replicator dynamic models.
- **Adjacent:** Broad periphery covers reward, combined reward/punishment, reputation systems, or indirect “punishment-like” mechanisms (e.g., removal, exclusion, environmental feedback).
- **None:** Many control/no-punishment baseline studies, or studies of only reputation/observation/update mechanisms.

### c) `efficiency_or_related_payoff_outcome`
- **Exact:** About 10–12 papers (e.g., Vasconcelos et al., 2022; Wang et al., 2025; Liu et al., 2024; Wang et al., 2024; Yaman et al., 2023) analyze efficiency/group payoff as a primary outcome.
- **Close/Adjacent:** Most others focus on cooperation rates, with only indirect arguments or qualitative expectation that efficiency will move in tandem (not always true).
- **None:** Substantial proportion of papers do not report group payoff, welfare, or efficiency metrics at all.

**Summary:** The literature is generally **highly relevant for PGG-like environments and punishment as a mechanism**, with “exact” evidence for efficiency limited to a minority of theoretical models. Most behavioral outcome studies provide only indirect or context-specific guidance for efficiency prediction.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (“efficiency”):** These include group efficiency (payoff relative to full cooperation), group payoff, welfare, surplus, or total earned coins. Only a small core of theory papers report these directly and systematically. When present, these outcomes are often parameterized by key game design variables.
- **Non-payoff behavioral outcomes:** The vast majority of papers report contribution rates, frequency of cooperators/defectors/punishers, norm compliance, punishment frequency, or related strategic frequencies. Many interpret these as proxies for efficiency, but the mapping is model-dependent and often non-monotonic due to punishment costs, exclusion effects, or second-order free riding.
- **Resource/community outcomes:** Some “close” models in ecological or resource PGGs report “achievement” (e.g., group reaches target), public good abundance, or sustainability—group success, but not strictly payoff/efficiency.

**Key distinction:** Only primary, explicit reporting of group payoff/efficiency can be used for direct quantitative prediction. Behavioral outcomes are **not equivalent** to efficiency because costly punishment can increase cooperation but reduce total group payoff (Zhang & Pei, 2022; Milinski, 2022).

# 4) Main Findings Relevant To Prediction

### A. General Direction
- **Punishment often increases efficiency relative to no-punishment when:**
    - Punishment is not too costly relative to its effectiveness.
    - The baseline control efficiency is low (i.e., high defection).
    - The sanctioning system is well-targeted (prosocial) and collective choice is possible, especially for global or large-scale goods (Vasconcelos et al., 2022; Wang et al., 2025; Liu et al., 2024; Dughera, 2022; Libois, 2022; Yaman et al., 2023).
- **Punishment may fail to increase—and can sometimes reduce—efficiency when:**
    - Punishment is expensive or misapplied (second-order free riding, antisocial punishment, excessive exclusion).
    - Baseline (control) cooperation/efficiency is already high (further costly punishment is wasteful).
    - Ecological/resource feedbacks or institutional design constrain the positive effect (e.g., insufficient resource growth cannot be compensated by cooperation—Wang et al., 2024; Sarkar, 2023).
    - In continuous-contribution PGGs, punishment alone may not stabilize high-efficiency equilibria without additional stabilizing forces (Yan et al., 2023).

### B. Moderators From Design Dimensions
- **Player count/group size:** Larger groups generally require stronger, more efficient punishment to achieve the same efficiency gain; synergy effects possible with network structure (Libois, 2022; Lim & Capraro, 2022).
- **Rounds/memory/information:** Long repeated interactions, longer player memory, and the visibility of history/institution outcomes increase the effectiveness and sustainability of punishment (Vasconcelos et al., 2022).
- **MPCR (synergy factor):** Higher MPCR (stronger returns to cooperation) make punishment more effective; low MPCR settings may require strong, cheap punishment or may not achieve efficiency improvements at all (Wang et al., 2025; Lv et al., 2023; Liu et al., 2024).
- **Punishment cost and effectiveness:** Lower punishment cost/higher fine ratio increases efficiency gains; non-linear or synergistic punishments may be more effective in structured populations (Lv et al., 2022; Kang et al., 2024). High-cost punishment can suppress participation, crowd out cooperation, or lower efficiency.
- **Institutional form:** Collective or centralized (institutional) punishment tends to be less vulnerable to second-order free rider problems and is more efficient than pure peer punishment in large or global groups. Decentralized/peer punishment can be effective in local/small groups (Vasconcelos et al., 2022; Dughera, 2022; Yaman et al., 2023).
- **Resource/ecological context:** In resource-based PGGs, natural growth rate, ecological feedbacks, and thresholds interact with punishment to determine maximum achievable efficiency; under some conditions, even with strong punishment, the system cannot reach full efficiency (Wang et al., 2024; Libois, 2022).
- **Voluntary vs. compulsory participation:** With voluntary participation and well-designed institutional punishment/exclusion, higher efficiency is possible, but high costs to punishment/exclusion can induce exit or nonparticipation equilibria (Lv et al., 2023; Shen et al., 2025).

### C. Patterns of Nonlinear/Dynamic Effects
- **Bistability/multistability:** In many models with feedback or threshold mechanisms, the effect of punishment is not monotonic; initial conditions (e.g., initial cooperation rate) and design parameters interact, producing multiple stable equilibria (Liu et al., 2024; Wang et al., 2024; Murase & Hilbe, 2024).
- **Threshold/cost boundaries:** There are often critical thresholds for punishment intensity: below, punishment is ineffective; above, full cooperation and efficiency are stable (Liu et al., 2024; Wang et al., 2025; Yaman et al., 2023; Dughera, 2022; Lim & Capraro, 2022).

# 5) Prediction Guidance

Based on the literature:

- **Direct prediction of treatment efficiency** (with punishment enabled) should weigh:
    - **Control efficiency:** If efficiency is already high, marginal gains from enabling punishment may be small or even negative due to punishment costs.
    - **MPCR (synergy factor):** Punishment is most effective at increasing efficiency when MPCR is not too low. At low MPCR, only strong/effective/cheap punishment yields efficiency gains, and sometimes not even then.
    - **Punishment cost and effectiveness:** Lower cost per unit and higher fine ratios are associated with higher efficiency gains. There is generally a minimum (threshold) effectiveness required before efficiency increases; above this, moving toward maximal efficiency if other parameters allow.
    - **Institutional form and group structure:** In smaller, local, or well-structured groups, peer punishment can be efficient. For larger/global goods, collective (institutional) punishment is needed for efficiency gains.
    - **Repeated interactions/information/memory:** Longer memory and more information about past actions/history support both the adoption and effectiveness of punishment institutions/equilibria.
    - **Voluntary participation/exit options:** If participation is voluntary, high punishment costs/excessive severity can push groups to nonparticipation equilibria and lower efficiency.
    - **Ecological/resource feedback:** In dynamic resource environments, punishment can only improve efficiency if the resource pool/growth enables it; otherwise, even full cooperation does not prevent inefficiency.

- **Predictions derived only from increased cooperation rates may be misleading**; costly punishment may raise cooperation but lower efficiency unless the cost is outweighed by the gain in public good provision.

- **Uncertainty and ambiguity**: Key transition boundaries (e.g., threshold MPCR, punishment intensity) are model- and context-specific; multiple equilibria may exist. In some models, punishment can reduce efficiency via over-sanctioning or antisocial punishment.

- **For design dimensions not directly manipulated (e.g., chat, identity visibility, default contribution framing), caution should be used and only indirect references drawn from relevant adjacent findings (e.g., information increases effectiveness in some settings).**

# 6) Design Dimensions Highlighted Across Papers

**Directly informed by multiple ‘exact’ or ‘close’ payoff-focused models:**
- `player_count`: Modeled in nearly all core efficiency studies (Vasconcelos et al., 2022; Libois, 2022; Lim & Capraro, 2022).
- `num_rounds`: Length of game and memory/information about prior rounds strongly moderated punishment effects in key models (Vasconcelos et al., 2022).
- `mpcr`: Almost universal key moderator; density and comparative statics in several models.
- `punishment_cost` & `punishment_tech`: Central to nearly every mechanistic efficiency model; explicit equations/phase diagrams provided in several sources.
- `all_or_nothing`: Modeled directly in some PGGs and PD-based variants, especially regarding punishment effects.
- `show_other_summaries`, `show_n_rounds`: Directly referenced as affecting learning/environment in some efficiency models.
- `reward_exists/reward_cost/reward_tech`: Sometimes included in joint or comparative models; less often as a main focus.

**Indirectly or contextually informed:**
- `chat`: Discussed as increasing cooperation, but not as a direct focus for efficiency in core payoff models.
- `default_contrib`: Framing rarely manipulated in payoff-relevant models; only contextually mentioned in meta-analyses or behavioral studies.
- `show_punishment_id`: Occasionally modeled (e.g., for antisocial punishment, meta-norms), but rarely in direct efficiency analyses.

**Effectively missing or extremely sparse:**
- Many papers do **not manipulate or report** outcomes for chat, default contribution framing, identity revelation, or display of round numbers or peer summaries—these are contextually discussed at most.
- Structured population effects and network topology (degree, local vs. global updating) receive substantial indirect treatment, especially in adjacent and close models.

# 7) Important Limitations

- **Empirical data are lacking**; findings are overwhelmingly theoretical or simulation-based. Real-world transferability and robustness to human noise or bounded rationality are untested here.
- **Efficiency outcomes are underreported**; most studies focus on cooperation rates, which may diverge from efficiency due to costly punishment or exclusion.
- **Complexity and specificity of models**: Several key efficiency-focused models have intricate structures (spatial, networked, ecological, institutional) that may not map precisely to the target prediction task.
- **Generalization limited by absence of key design dimensions** (e.g., communication, identity visibility, default contribution). For many prediction dimensions, only indirect or contextual evidence is available.
- **Ambiguity and multi-equilibria**: Several main models show bistability, multistability, or non-monotonic effects, making quantitative prediction highly contingent on initial conditions and parameter values.
- **Moderators may interact in nonlinear or threshold-dependent ways** (e.g., synergy factor and punishment cost), limiting the utility of additive or linear prediction models.
- **Resource/ecological models show that efficiency may be bounded by exogenous constraints** (e.g., resource growth), regardless of punishment.
- **Absence of human behavioral pathologies**: Human real-world behaviors—such as antisocial punishment, errors in punishment application, shifting norms—are rarely captured in these theoretical models.

**Conclusion:**  
Robust theoretical evidence supports the idea that, in public-goods-game-like environments, enabling effective, well-calibrated punishment usually increases group efficiency relative to controls without punishment, **especially in low-efficiency, low-MPCR, or large-group settings—provided that punishment costs are not prohibitive and the sanctioning system is well-designed**. However, the effect is **not universal** and is mediated by multiple game design dimensions, initial conditions, and potential for second-order or antisocial punishment. The evidence base is strong in theoretical mechanism but limited in direct empirical demonstration, and many dimensions central to the prediction task are underexplored. Use predictions from this evidence base with **due caution regarding contextual fit and parameter sensitivity**.
