# 1) Evidence Base

The evidence base for predicting the efficiency impact of enabling peer punishment in public-goods-game-like environments is strong but somewhat narrow. All papers are theoretical (no new empirical or experimental studies), but the set contains a large number of models tailored to exact or closely related public goods games (PGGs), covering a range of group structures, punishment/reward mechanisms, and implementation details. About half the papers address standard PGGs or direct variants, while many others examine adjacent games (e.g., threshold PGGs, trust games, networked dilemmas, or sequential interaction settings). The outcomes most commonly analyzed are contributions/cooperation rates (behavioral), but a substantial minority of papers do model and report group efficiency or related payoff-based outcomes. Notably, several models are calibrated to baseline experimental findings (e.g., Fehr & Gächter), and a few provide explicit formulas or phase diagrams linking game design dimensions to efficiency outcomes.

# 2) Task Relevance

**pgg_or_variant:**  
- *Relevance*: Many papers have `exact` relevance, modeling standard or canonical PGGs directly (e.g., Jiao et al., 2020; Dutta et al., 2021; Fang et al., 2020; Wang & Lv, 2019; Huang et al., 2018; Greenwood et al., 2018).
- *Adjacent* or *close*: A substantial portion of the literature considers adjacent games, such as collective-risk, trust, or threshold games where core incentive and punishment mechanisms are similar to those in PGGs but differ structurally.

**punishment_or_sanctions:**  
- *Relevance*: Most models manipulate, implement, or focus on costly peer or institutional punishment (`exact`), discussing peer punishment effectiveness, cost, and incentives directly. A smaller set focuses on reward, policing, exclusion, or more diffuse sanctioning (sometimes as contextual discussion).
- Papers on pure reward, reputation, or other cooperation-promoting mechanisms without explicit punishment are only contextually relevant.

**efficiency_or_related_payoff_outcome:**  
- *Relevance*: About half of the theory papers address group efficiency, welfare, average payoff, or explicit group surplus as a primary or explicit outcome (`exact` or `close`). Others use sum of contributions, prevalence of cooperation, or survival of strategies as behavioral proxies (`adjacent` or `close`). Some papers focus solely on behavioral dynamics (`weak` or `none`).

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes (directly relevant):**
- Group efficiency: ratio of total group payoff to the fully cooperative benchmark (e.g., Jiao et al., 2020; Dutta et al., 2021; Wang & Lv, 2019; Fang et al., 2020; Huang et al., 2018; Mihm & Toth, 2020; Jindani, 2020; Nakamaru et al., 2018).
- Group payoff / mean payoff / average fitness: sometimes normalized for direct efficiency interpretation.

**Non-payoff behavioral outcomes (proxy or indirect):**
- Contribution rate / cooperation fraction: frequently used as the main success metric but not identical to efficiency since costly interventions or inefficient institution designs may elevate cooperation at a net loss.
- Punishment frequency, norm compliance, or the persistence of cooperative clusters are common in spatial, networked, or evolutionary models.

**Ambiguous or contextual:**
- Some models use aggregate group behavior or stability of cooperation as a loose proxy for efficiency, but this is not reliably equivalent unless punishment costs are low and all excess costs are rebated.

# 4) Main Findings Relevant To Prediction

**Synthesis Across Papers:**

- **Enabling punishment generally increases efficiency relative to control, provided punishment is sufficiently effective and not excessively costly.** Multiple theory papers show that, in standard PGGs with plausible lab parameters (player count, rounds, MPCR, punishment cost), enabling peer punishment causes a substantial jump in group efficiency and welfare (Dutta et al., 2021; Wang & Lv, 2019; Huang et al., 2018).
- **The effect is highly sensitive to the punishment technology:** If the penalty for defectors is much higher than the cost imposed on punishers, efficiency gains are robust; otherwise, punishment can be neutral or even decrease efficiency due to second-order free-riding or spiraling costs (Fang et al., 2020; Perry et al., 2018; Greenwood et al., 2018).
- **Cost structure matters:** Models in which punishment cost is shared or probabilistically executed (rather than always-on or fixed per punisher) can support high efficiency even with high per-punishment costs (Jiao et al., 2020).
- **Corruption and counter-punishment can undermine efficiency:** In the presence of corruption or the possibility of bribery and antisocial punishment, enabling punishment does not guarantee improved efficiency and may lower it (Fang et al., 2020; Huang et al., 2018; Raihani & Power, 2021).
- **Network and monitoring structure moderate effectiveness:** Efficiency gains from punishment are robust when actions are visible or when monitoring is rich, but less so when information is local and punishment is delayed or ambiguous (Mihm & Toth, 2020; Jindani, 2020; Perry et al., 2018).
- **Design is critical:** Graduated or institutional punishment (where cost and fines scale with severity/frequency) can outperform strict/constant punishment schemes, especially in threshold or collective-risk games (Couto et al., 2020).
- **Parameter thresholds and non-monotonicity:** There are threshold effects—punishment is only effective (and improves efficiency) above critical levels of frequency and magnitude, and can be detrimental if too weak, too costly, or overapplied (Fang et al., 2020; Greenwood et al., 2018; Chang & Zhang, 2021).
- **Role of internalization, commitment, and institution design:** Where norm internalization or institutional incentives align individual and group interests, punishment raises efficiency; otherwise, it may create new free-rider or conflict problems (Dutta et al., 2021; Smith, 2020).

# 5) Prediction Guidance

The literature gives structured, though primarily theoretical, tools for predicting efficiency in treatment (punishment-enabled) conditions from control efficiency and game design:

- **Expect a substantial (but not guaranteed) increase in efficiency when peer punishment is enabled, particularly in games structurally similar to canonical lab PGGs:**
    - This increase is most reliable at moderate group size, standard MPCR, moderate costs, and when monitoring is straightforward and punishment is effective (Dutta et al., 2021; Wang & Lv, 2019).
    - Quantitative models and calibrated examples (e.g., to Fehr & Gächter) exist for standard 4-player, 10-round games.
- **The magnitude of the effect is heavily moderated by design dimensions:**
    - *Punishment_cost* and *punishment_tech*: High cost and low effectiveness reduce or reverse gains.
    - *Player_count* and *num_rounds*: Effects may attenuate or strengthen depending on group size and repetition; some models find larger group size weakens effectiveness (due to coordination and second-order free riders) while others find stability can be maintained with good monitoring/observation structures.
    - *Reward_exists*: Presence of reward can substitute or augment punishment effects; some models find reward is more efficient than punishment under certain circumstances (Fang & Chen, 2021).
- **Negative or mixed effects are possible:**
    - If punishment is costly, misapplied (e.g., antisocial punishment), undermined by corruption, or information is poor, enabling punishment can fail to improve or even harm efficiency (Fang et al., 2020; Raihani & Power, 2021; Perry et al., 2018).
- **Probabilistic or graduated punishment can optimize cost/benefit:** Instead of always-on, deterministic punishment, moderate probability or scalable punishment often yields higher net efficiency, especially when costs are high (Jiao et al., 2020; Couto et al., 2020).
- **Prediction for non-standard games or with missing design information is more uncertain:** While adjacent models suggest generalizability of the mechanisms, precise quantitative predictions should only be made when key dimensions (cost, effectiveness, group size, monitoring) are specified.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions (explicitly modeled, with effect on efficiency):**
- `player_count`
- `num_rounds`
- `mpcr`
- `punishment_cost`
- `punishment_tech` (sometimes operationalized as punishment/fine magnitude or inflicted cost per unit of cost to punisher)
- `reward_exists` (where reward and punishment co-exist)
- `all_or_nothing` (discrete/continuous contributions)
- `reward_cost` / `reward_tech` (in reward-focused or combined models)

**Indirectly or contextually discussed dimensions:**
- `show_other_summaries` and `show_punishment_id`: Equated with monitoring, observation structure, or information flow (e.g., Mihm & Toth, 2020; Jindani, 2020).
- `chat`: Occasionally mentioned as a means for norm communication, but rarely operationalized in efficiency analyses.

**Sparsely covered or missing dimensions:**
- `default_contrib` (framing): Rarely specified; controls for opt-in/opt-out default may matter for behavior but are not structurally present in models focusing on efficiency with/without punishment.
- `show_n_rounds`: Sometimes manipulated to affect strategic planning, but not systematically tied to efficiency outcomes.
- `show_punishment_id`: Only occasionally modeled; relevant to retaliation or counter-punishment dynamics.
- Network dimensions (local/global): Sometimes represented by structure of interactions but not always mapped to specific prediction columns.

**Summary mapping:**
- Key prediction-relevant parameters (player_count, punishment_cost, punishment_tech, mpcr) are well-covered.
- Several visual or procedural features (information display, identity revelation, chat) may be discussed as moderators, but evidence is indirect.

# 7) Important Limitations

- **Absence of empirical studies:** All evidence is theoretical or simulation-based. While some models are calibrated to classic experiments, generalizability to new, especially field, settings or complex human dynamics is uncertain.
- **Outcome ambiguity:** Many papers focus on contribution rates, strategy prevalence, or behavioral dynamics rather than explicit group efficiency or payoff. Use caution interpreting behavioral improvements as efficiency gains—costly or misapplied punishment can increase cooperation but *reduce* group surplus.
- **Parameter sensitivity and threshold effects:** Model-based predictions are often highly sensitive to particular parameter values (punishment effectiveness, cost, monitoring structure), and efficiency effects may be non-monotonic or discontinuous across these parameters.
- **Context dependency:** Effects may be positive, neutral, or negative depending on group size, population structure, presence of corruption, and information. Important moderators such as antisocial punishment or counter-punishment are discussed in some papers, but general theory is inconsistent regarding their practical significance.
- **Limited coverage of some design dimensions:** Some game design features relevant to experimental or field implementations (e.g., chat, identity display, default options) are only contextually discussed or missing as independent variables.
- **No new quantitative benchmarks:** No new empirical effect sizes or benchmarks for predicted efficiency are provided; findings are theoretical or demonstrated with simulated/analytical models.
- **Transferability to heterogeneous or highly realistic environments:** Most findings are derived from simplified or parameterized game-theoretic models and may not fully account for real human heterogeneity, norm dynamics, or institution-building.

---

**In summary:**  
The literature provides strong theoretical evidence that peer punishment generally increases efficiency in standard PGGs, provided design dimensions (notably punishment cost/effectiveness and information flow) support credible, effective, and low-cost sanctioning. Effects are context- and parameter-dependent, and caution is warranted when extending predictions to environments with corruption, antisocial punishment, high punishment costs, ambiguous monitoring, or complex interactions. The best-informed dimensions for prediction are player count, rounds, MPCR, punishment cost, and punishment effectiveness, with moderate evidence for the importance of monitoring structure and network details. Empirical confirmation and effect size benchmarks from new data remain a gap.
