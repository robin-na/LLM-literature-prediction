# 1) Evidence Base

The paper set consists exclusively of theoretical papers and simulations (36 in total, none empirical or experimental), almost all from mathematical biology, evolutionary game theory, or computational social science.  
A significant fraction of the set addresses public goods games (PGGs) or their direct variants, focusing on the impact of punishment and other incentives on cooperation. Outcomes are typically strategy frequencies (cooperation rates), with a smaller number of papers modeling efficiency or total group payoff directly. Most theoretical models are well-mixed or spatial/evolutionary, with some incorporating resource dynamics, reputation, or ecological feedback.  
The evidence base is thus broad in its coverage of potential moderator mechanisms and game design parameters, but generally narrow on empirical calibration and direct measurement of the treatment effect (punishment on group efficiency) in human experimental PGGs.

# 2) Task Relevance

**pgg_or_variant:**  
- *exact*: Many papers model PGGs directly with parameters mapping closely to PGG implementation (e.g., player count, group size, mpcr, rounds, all-or-nothing).  
- *close*: Several papers analyze collective-risk dilemmas, donation games, or common-pool resource games with PGG-like structure.  
- *adjacent/weak*: Some models are of PDGs or snowdrift/stag-hunt games, or focus on reputation dynamics without public goods structure.

**punishment_or_sanctions:**  
- *exact*: Most studies formally model the enabling of peer or institutional punishment (sometimes also reward/exclusion), including cost, effectiveness, and frequency.  
- *adjacent*: A few deal with exclusion, reporting, policing, or reputation as indirect sanctions.  
- *none*: Several do not model punishment.

**efficiency_or_related_payoff_outcome:**  
- *exact/close*: ~1/3 of papers model or report efficiency, total payoff, welfare, or group-level earnings/achievement.  
- *adjacent/weak*: A majority use cooperation/contribution rates or strategy frequencies as the main outcome, offering only indirect inference about efficiency.  
- *none*: Some do not report any payoff-based outcome.

**Summary:**  
The most relevant papers are highly aligned with the prediction task, providing direct (theory-based) estimates of how specific punishment implementations affect efficiency in PGGs. However, a substantial portion of the literature relies on non-payoff behavioral outcomes or models adjacent games, reducing their predictive specificity for treatment efficiency in PGGs.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes:**
  - *Directly Measured/Modeled*: Efficiency (ratio of actual group payoff to full cooperation payoff), average group payoff, total earnings, welfare, surplus, aggregate coins generated, and group achievement.  
  - *Indirect/Proxy*: Cumulative institutional costs to reach cooperation; group achievement as reaching a behavioral threshold (not always the same as payoffs).
  - *Nuance*: Some models allow mapping from incentive cost/cooperation rates to efficiency, but rarely report both.

- **Non-Payoff (Behavioral) Outcomes:**
  - Contribution rate/cooperation rate (stationary or time-varying frequency of cooperators, punishers, defectors).  
  - Frequency/distribution of punishment or exclusion.  
  - Norm compliance, strategy dynamics, oscillatory regimes, cluster formation.  
  - Reputation scores, reporting rates, network topology effects.

**Note:** Many papers infer likely efficiency improvements from higher cooperation rates, but this inference is constrained or complicated by punishment/reward costs, antisocial punishment, resource dynamics, or nonlinearity in payoff structure.

# 4) Main Findings Relevant To Prediction

**1. Punishment Increases Cooperation, But Not Always Efficiency.**  
- The most consistent (theoretical) finding is that enabling (peer or institutional) punishment in PGGs robustly increases cooperation rates (e.g., Liu et al., 2018; Zhu et al., 2020; Fehr & Schurtenberger, 2018).
- However, efficiency gains are not guaranteed; when punishment is costly or when antisocial punishment is prevalent, net group payoff may not increase and may even decrease (Fehr & Schurtenberger, 2018).

**2. Efficiency Effects Depend on Game Design Dimensions.**  
- *Player count, group size, and synergy factor (MPCR)* directly affect baseline efficiency and the cost-benefit ratio of punishment (Duong & Han, 2021; Alvarez-Rodriguez et al., 2021).
- *Punishment cost and effectiveness*: Lower punishment costs and higher punishment magnitude/fine generally increase efficiency gains up to a threshold; excessive cost can undermine both cooperation and efficiency (Yang & Chen, 2018; Liu et al., 2019; Ågren et al., 2019).
- *Type of punishment*: Peer punishment often yields higher cooperation (and potentially efficiency) than pool punishment when the cost/fine ratio is favorable (Zhu et al., 2020; Liu et al., 2018).
- *Role of rewards*: Reward is more cost-efficient when baseline cooperation is low; punishment becomes more cost-efficient at high cooperation thresholds (Duong & Han, 2021; Wang et al., 2021; Góis et al., 2019).
- *Ecological/resource context*: If the resource renews too slowly or overexploitation is possible, even perfect cooperation (enforced by punishment) does not guarantee efficiency; the ecological constraint dominates (Chen & Szolnoki, 2018; Yan et al., 2021).

**3. Moderator Mechanisms:**
- *Corruption and bribery reduce or neutralize punishment's efficiency effects* (Liu, Chen, & Szolnoki, 2019).
- *Antisocial punishment* (punishing cooperators) reduces or even reverses efficiency gains (Fehr & Schurtenberger, 2018).
- *Normative/institutional context*: Institutional control of punishment channels its use into efficiency-enhancing directions (reducing antisocial use), but at the cost of additional resources (Duong & Han, 2021; Fehr & Schurtenberger, 2018; Sun et al., 2021).
- *Size and complexity*: As group size or social complexity increases, informal (peer) punishment is less effective for efficiency, and institutional/third-party solutions become more important (Jagers et al., 2020).

**4. Temporal/Network Structure:**
- Baseline efficiency and the parameter space for effective punishment differ by spatial/networked structure and history/memory of play (Alvarez-Rodriguez et al., 2021; Danku et al., 2019), though direct payoff effects of punishment are more often inferred than measured here.

# 5) Prediction Guidance

**When punishment is enabled in a PGG-like environment:**
- **Efficiency will likely increase** if:
  - The cost of punishment is lower than the marginal benefit to the group (low `punishment_cost`, high `punishment_magnitude`).
  - Antisocial punishment is rare or constrained by institutional/normative design (`punishment_tech` or `show_punishment_id`); credible punishment targets defectors, not cooperators.
  - Corruption/bribery is unavailable or unattractive (`punishment_tech` does not allow evasion/collusion; low bribe/payoff for corrupted enforcement).
  - The synergy factor (MPCR) and player count are in a range where cooperation is productive but not easily achieved in the control.
  - The ecological substrate supports increased cooperation translating into higher payoffs (resource is not overexploited).
  - Reward is not already present as an alternative incentive, unless a hybrid is implemented optimally (Duong & Han, 2021; Góis et al., 2019).

- **Efficiency gains are limited or negated** if:
  - Punishment costs are high relative to cooperative surplus.
  - Antisocial punishment (of cooperators) is frequent or unmitigated.
  - Institutional punishment adds substantial overhead or is subject to corruption.
  - Network/structural constraints undermine the targeting or efficacy of punishment.
  - The baseline (control) efficiency is already high, in which case additional punishment mainly adds costs.

- **Dimension-by-dimension guidance:**
  - *player_count, mpcr, punishment_cost, punishment_tech*: These parameters are the best supported for mechanistically predicting the direction and sometimes the size of the efficiency shift.
  - *reward_exists*: The presence and design of reward can fundamentally alter the efficiency outcome—reward is often optimal at low cooperation, punishment at higher cooperation.
  - *other dimensions* (chat, show_other_summaries, show_punishment_id, default_contrib): Discussed more as theoretical moderators than explicitly modeled, but likely relevant in practice through norm formation, information availability, and coordination.

- **Control efficiency is predictive of treatment efficiency**: When baseline cooperation is low, the marginal efficiency gain from punishment is higher (Duong & Han, 2021; Wang et al., 2021; Góis et al., 2019). When baseline efficiency is already high, punishment may yield little to no additional gain, or even a reduction.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed in this set:**
- `player_count`: Explicitly parameterized in most models, showing nonlinear effects on both baseline efficiency and the impact of punishment.
- `num_rounds`: Many models simulate evolutionary time or repeated rounds; effect is operationalized through time-to-equilibrium or stochastic turnover.
- `mpcr` (marginal per-capita return): Central in almost all exact/close-relevance papers; a key driver of cooperation stability and efficiency.
- `punishment_cost`, `punishment_tech` (type, severity, mechanism): Core in the best-supported papers. Many models allow direct tuning of cost/effectiveness.
- `reward_exists`, `reward_cost`, `reward_tech`: Several papers contrast reward and punishment, offering insight into relative efficiency.
- `all_or_nothing`: Presence or absence of binary/continuous contribution is parameterized in multiple models.

**Indirectly/contextually discussed:**
- `chat`, `default_contrib`, `show_other_summaries`, `show_n_rounds`, `show_punishment_id`: Sensible moderators, noted in theoretical reviews as potentially important for norm formation, monitoring, and antisocial punishment, but rarely parameterized or modeled directly.
- `reward_exists`, though mentioned, sometimes refers to simulations that are structurally adjacent but not directly mapped to standard PGGs.

**Effectively missing for direct prediction:**
- Precise mapping of behavioral design elements (chat, transparency, framing, specific information feedback) to efficiency under punishment—these are mostly theoretical or hypothetical, lacking in direct payoff-based modeling.
- Detailed effect of policy transparency (e.g., showing punishment/reward identity) on efficiency.

# 7) Important Limitations

- **Lack of empirical calibration:** All evidence is theoretical/simulated; no experimental/human data. Real-world payoff consequences of enabling punishment remain subject to unmodeled behavioral variability and institutional noise.
- **Payoff vs. behavior distinction:** Most papers infer efficiency impact from cooperation rates, potentially overstating efficiency gains when punishment is costly or misapplied (e.g., antisocial punishment, institutional overhead).
- **Heterogeneous context modeling:** Many real-world moderators (cultural context, individual heterogeneity, learning dynamics) are acknowledged but not included or parameterized in most models.
- **Limited modeling of information/context cues:** While chat, feedback, and transparency are theorized to be important for the normative context and antisocial punishment mitigation, they are rarely systematically varied in efficiency models.
- **Resource/ecological feedback:** PGG variants with resource dynamics show strong context sensitivity—punishment can backfire when the environment constrains achievable efficiency, but most classic PGG models do not include such constraints.
- **Complexity of optimal policy:** Several findings suggest that the most efficient scenario is a dynamic or hybrid combination of reward and punishment, and that their cost-efficiency depends on group composition and temporal dynamics. Most models assume static policy.
- **Generalization from models**: Many findings are drawn from infinite/homogeneous populations, spatial structures, or game-theoretic abstractions, not finite, noisy, or institutionally complex environments.
- **Sparse coverage of some dimensions:** Design variables like chat, default contribution framing, and visibility of others' choices/punishments—likely relevant moderators—are not parameterized with respect to efficiency in most models.

---

**In summary**, the literature provides robust theoretical guidance for predicting the direction and conditional magnitude of efficiency changes from enabling punishment in PGG-like games. The best predictions come from models that match the actual game on group size, MPCR, and punishment cost/technology. The prediction is most reliable when control efficiency is low, punishment is targeted and cost-effective, and when antisocial or corrupt punishment is absent. However, the translation from cooperation rates to efficiency must account for punishment costs, and several behavioral/contextual design dimensions and real-world moderators remain insufficiently quantified for high-confidence prediction.
