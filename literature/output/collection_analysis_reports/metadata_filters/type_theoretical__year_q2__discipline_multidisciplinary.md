# 1) Evidence Base

The evidence base consists of 66 papers, all theoretical and predominantly using models and agent-based simulations rather than empirical or experimental data. The coverage is broad in terms of mechanism variants, collective dilemmas, and contextual factors, but narrow in that it lacks direct lab/field experimental estimates of efficiency changes from enabling punishment. Most papers employ game-theoretic or evolutionary analysis of public goods games (PGGs), variants like snowdrift and trust games, and adjacent social dilemmas (e.g., prisoner's dilemma, Ultimatum Game). Outcomes vary from explicit efficiency/payoff calculations to non-payoff behavioral markers (e.g., cooperation rates). The set includes several major theoretical syntheses and many focused mechanism studies.

# 2) Task Relevance

### pgg_or_variant

- **exact relevance:** Many papers use PGG or very close institutional variants (e.g., spatial/networked PGGs, pool vs. peer punishment, hybrid incentive regimes).
- **close relevance:** Some papers model snowdrift or linear threshold games, which share key incentive features but differ in how public good returns accrue or in the presence of thresholds.
- **adjacent/weak:** A significant subset study closely related dilemmas (prisoner's dilemma, Ultimatum Game, bribery, resource allocation, trust games), which are not, by definition, PGGs but share social dilemma structure. These are mainly mechanism/insight pieces, not primary evidence for quantitative PGG efficiency shifts.

### punishment_or_sanctions

- **exact relevance:** A core group directly models peer, pool, or institutional punishment as a distinct, parameterized game feature.
- **close:** Some focus on exclusion/ostracism (akin to punishment) or interconnected hybrid mechanisms.
- **adjacent/weak:** Some analyze phenomena analogous to punishment (e.g., commitment compensation, retaliation, signaling via punishment), but not formal or parameterized as in standard PGGs.
- **missing:** A moderate number study environments explicitly without punishment, making them context only.

### efficiency_or_related_payoff_outcome

- **exact:** Several PGG papers directly measure or model efficiency (group payoff as a fraction of maximum).
- **close:** Others report group payoff, average earnings, total coins, or welfare—interpretable as efficiency under typical PGG definitions.
- **adjacent:** Many report only contribution rates, prevalence of cooperators/punishers, or related behavioral outcomes with implicit but not explicit efficiency analysis.
- **none:** Numerous adjacent papers report only strategy proportions, cluster stability, or oscillatory dynamics—non-payoff outcomes.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:**  
  - Group efficiency (relative to maximal cooperation)  
  - Group/mean payoff, earnings, welfare, surplus, total coins, fitness  
  - Explicit statements about total group welfare or efficiency before/after enabling punishment

- **Non-payoff behavioral outcomes:**  
  - Contribution/cooperation rates, prevalence of cooperators/punishers  
  - Frequencies of strategies (defector, cooperator, punisher, excluder)  
  - Punishment assigned, retaliation rates, norm compliance  
  - Evolutionary stability or persistence of behavioral types  
  - Emergent norm content or distribution of fairness offers

- **Distinction:**  
  Many theoretical studies measure behavioral markers (like increased cooperation from punishment) and infer likely efficiency changes, but only some explicitly account for the punishment costs deducted from total group payoffs.

# 4) Main Findings Relevant To Prediction

- **General effect of punishment on efficiency:**  
  - In standard PGGs, enabling an effective and not overly costly punishment mechanism generally increases group efficiency, especially if the control efficiency is low (Hetzer & Sornette, 2013; Roberts, 2013; Chen et al., 2015).  
  - The efficiency gain is conditional: if punishment is too costly, poorly targeted, or invites retaliation, efficiency can stagnate or even decline despite increased cooperation (Barrett, 2016; Ezeigbo, 2017; Helbing et al., 2014).
  - Hybrid systems combining reward and punishment often outperform pure punishment in both cooperation rates and net efficiency (Chen et al., 2015; Sasaki et al., 2015).

- **Key moderators (with theoretical or qualitative empirical support):**  
  - **Punishment cost and effectiveness:** Low-cost, high-impact punishment is more likely to convert contributions into net efficiency gains (Roberts, 2013; Barrett, 2016; Hetzer & Sornette, 2013).
  - **Group size and MPCR:** Efficiency gains from punishment can be diluted in large groups unless the mechanism can scale; at high MPCR, efficiency outcomes become less sensitive to punishment (Ye et al., 2016; Sasaki et al., 2015).
  - **Institutional context:** Pool punishment, exclusion mechanisms, and institutional/hybrid punishment alter the tradeoff between increased cooperation and net cost (Liu et al., 2017; Chen et al., 2015).
  - **Reward co-existence:** Rewards facilitate the emergence of punishment and help solve second-order free-rider problems, enabling stable, high-efficiency states (Sasaki et al., 2015).
  - **Population structure:** Spatial structure and coevolutionary rules moderate the effect of punishment (Perc et al., 2013); adaptive structures can magnify or dampen punishment’s benefit.
  - **Return to scale:** Increasing returns sharply boost the efficiency payoff to punishment (Ye et al., 2016); in linear PGGs, effects are more modest or contingent.
  - **Special context (corruption, contest, coordination):** In environments with significant corruption, intergroup contest, or complex coordination demands, punishment’s effect on efficiency may be negative or ambiguous (Gavrilets & Richerson, 2017; Abdallah et al., 2014; Barrett, 2016).

- **Empirical vs. theoretical:**  
  - Almost all evidence is theoretical/simulation-based; lack of experimental estimates or direct efficiency ratios (no direct quantitative effect sizes from lab treatment-control efficiency).

# 5) Prediction Guidance

- **Qualitative prediction:**  
  - When a control PGG design exhibits low efficiency, enabling an effective, not overly costly punishment mechanism is likely to boost efficiency substantially, provided punishment parameters fall in the “effective” region (punishment cost low relative to its impact, no major retaliation or corruption, and MPCR/group size not at extreme levels).
  - The effect is maximized if punishment is complemented by rewards or hybrid regimes, or is adaptively applied after cooperation is established.
  - If punishment is very costly or group size is large, gains in cooperation may be offset by the direct cost of sanctions, causing weak or even negative shifts in efficiency.
  - In certain institutional contexts (e.g., where exclusion or commitment mechanisms are feasible), efficiency may be increased even more than with traditional punishment.
  - Game design dimensions to pay special attention to for prediction: **punishment cost, punishment-to-impact ratio, MPCR, player count, reward existence, spatial/network structure.**
  - Use control efficiency as a baseline; the higher the pre-existing efficiency, the smaller the expected treatment effect from enabling punishment, unless group composition or structure dramatically change.

- **Limits of prediction (from this literature):**  
  - Most predictions must be directional or suggestive, not strictly quantitative—evidence primarily justifies whether efficiency is likely to rise or fall, not by how much.
  - Predictions are best for parameter regimes closely matching theoretical models (small–medium groups, clear pairwise punishment, evolutionary/iterated games).

# 6) Design Dimensions Highlighted Across Papers

**Directly informed:**
- `player_count` – discusses group size scaling, often in direct models (e.g., up to N=12–20).
- `num_rounds` – relevant in repeated/iterated models; longer games allow reputation buildup, stronger treatment effects.
- `mpcr` (Marginal Per Capita Return) – commonly manipulated; its value is often a key moderator.
- `all_or_nothing` – explored in discrete vs. continuous contribution models.
- `punishment_cost` and `punishment_tech` – punishment cost per point, punishment impact, implementation mechanism are central everywhere punishment is modeled.
- `reward_exists`, `reward_cost`, `reward_tech` – several models include reward as critical moderator (especially hybrid models).
- `show_other_summaries` and `show_n_rounds` – present in information/monitoring models.

**Indirectly/contextually informed:**
- `default_contrib` – indirectly relevant via studies of framing and engagement but rarely modeled explicitly.
- `chat` – communication is typically disabled in theoretical models; a few discuss its effects contextually.
- `show_punishment_id` – some adjacent models analyze indirect effects from punishment visibility (as a trust signal), but without direct analysis in PGGs.

**Effectively missing:**
- Most models do not analyze or vary `default_contrib`, `chat`, `show_punishment_id`, or fine-grained information display (beyond basic monitoring).
- Rarely experimental: real-world implementation and noise/error, often critical in practice, are generally not modeled.
- Very few papers discuss or model dynamic adjustment of design dimensions within an experiment or over time.

# 7) Important Limitations

- **Theoretical focus, no direct empirical estimates:** All findings are model-based (theory/simulation), with no human or real-world data providing experimental efficiency ratios for control vs. peer punishment.
- **Behavioral/efficiency distinction:** Many findings conflate increases in cooperation rates with increased efficiency, but in high-cost punishment regimes, efficiency gains may not materialize even when cooperation ascends.
- **Parameter regimes for “effectiveness”:** Precise thresholds where punishment switches from beneficial to harmful are model-specific; not all are mapped to the full range of design dimensions, especially for large groups or nonstandard MPCR.
- **Interactive/hybrid mechanisms:** Efficiency gains attributed to punishment in some models depend on concurrent reward, exclusion, or coordination mechanisms; results may not generalize to “punishment alone” scenarios.
- **Game structure generalizability:** Many papers use spatial, evolutionary, or adjacent game forms (prisoner’s dilemma, snowdrift, trust game) rather than iterated, well-mixed PGGs, constraining transferability.
- **Neglect of certain real-world institutional features:** Factors like communication (`chat`), punishment attribution (`show_punishment_id`), or default framing (`default_contrib`) are rarely feature-modeled.
- **Antisocial punishment and norm content:** The literature notes, but often does not quantify, risks from retaliation, corruption, norm misalignment, or antisocial enforcement, which can in practice reduce or even reverse efficiency gains.

---

**Summary**:  
The literature provides strong theoretical and qualitative simulation-based support for the prediction that (a) enabling an effective, not overly costly punishment mechanism will, in standard low-efficiency PGGs, typically increase efficiency; (b) the magnitude and even the sign of this effect are highly sensitive to punishment cost/effect ratio, group size, MPCR, and institutional modifiers (reward, exclusion, hybrid). Predictions should be directional, not absolute, and are best suited for use in qualitative or semi-quantitative causal models, with special caution where group size is large, punishment costs are high, or hybrid mechanisms are absent. Experimental validation is lacking, and attention to behavioral vs. true efficiency outcomes is necessary for downstream prediction.
