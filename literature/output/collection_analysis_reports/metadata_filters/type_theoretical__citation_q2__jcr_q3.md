# 1) Evidence Base

This literature set is comprised exclusively of theoretical (modeling) papers, with no direct experimental or empirically-derived data. Most papers use formal models and simulations, ranging from standard public goods games (PGG) with or without punishment, to close variants and more distant social dilemmas or trust-game analogues. The set is narrow in focus on punishment and theoretical mechanisms, but broad in terms of model structures (classic PGGs, spatial/networked games, games with leadership, partner selection, indirect reciprocity, commitment, etc.). Payoff-based outcomes (efficiency, welfare, group payoff) are a primary focus in many, but a nontrivial number report only behavioral outcomes (contribution rates, cooperation frequencies, strategy equilibria). A notable strength is the wide range of game design dimensions analyzed across the models. However, the absence of direct empirical findings limits the ability to derive precise effect sizes or calibrate quantitative predictions.

# 2) Task Relevance

Relevance (using the labels `exact`, `close`, `adjacent`, `weak`, `none`):

- **pgg_or_variant**: The majority of the papers are either `exact` (standard PGG models) or `close` (team production, division-of-labor games, trust-like repeated games). Some are `adjacent` (Prisoner’s Dilemma, Snowdrift, donation games, spatial variants), and a few are `none/weak` (resource allocation, Stackelberg security games).
- **punishment_or_sanctions**: Many papers are `exact`—they explicitly manipulate or model punishment in PGGs; others are `close` (modeling analogous sanctions, exclusion, or reward mechanisms closely tied to punishment); some are `adjacent` (focusing on network formation, reputation, or indirect reciprocity as substitutes).
- **efficiency_or_related_payoff_outcome**: Several papers are `exact`, reporting on group efficiency, welfare, or payoff. Others are only `adjacent` or `close`, reporting on behavioral proxies (e.g., sum of contributions, frequency of cooperation) or providing only qualitative statements about welfare.

Overall, the literature set is strongly relevant for theoretical guidance on the efficiency effects of punishment in public-goods-game-like settings, but lacks empirical outcome data and is not always directly aligned with the structure or measures required for prediction in the exact downstream task.

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes:**
- *Efficiency (group payoff/maximum possible)* is explicitly analyzed in several papers (e.g., Wolff, 2012; Dutta et al., 2021; Fang et al., 2020; Hwang, 2017; Wang & Lv, 2019; Kranz, 2010; Dughera, 2022; Chassang & Zehnder, 2016; Nakao, 2009; Buchholz et al., 2014).
- *Group payoff/earnings, welfare, surplus*: Used interchangeably with efficiency in several sources, providing a directly relevant outcome for prediction.
- *Related (but not identical) outcomes*, such as average payoff per cooperator or payoff thresholds, are sometimes reported.

**Non-Payoff Behavioral Outcomes:**
- *Contribution or cooperation rates* are frequently measured (e.g., Chen et al., 2018; Kaiping et al., 2016), often used as proxies or theorized to strongly correlate with efficiency, but not equivalent.
- *Punishment rates, frequencies, strategy abundances, norm compliance*: Detailed in evolutionary and spatial models, providing insights into underlying mechanisms but not direct efficiency outcomes.

It is critical to distinguish that only some papers provide direct evidence on the efficiency effects of punishment—the rest offer indirect inferences via increased cooperation or hypothesized payoff improvements.

# 4) Main Findings Relevant To Prediction

**Empirical findings:** Absent in this set—all evidence is theoretical or simulation-based.

**Theory findings – Direct on Payoff/Efficiency:**
- **Punishment often increases efficiency**, provided its cost is not excessive and it is sufficiently effective relative to the loss imposed on defectors. This effect is robust in standard PGGs (Wolff, 2012; Dutta et al., 2021; Kranz, 2010; Hwang, 2017; Wang & Lv, 2019; Buchholz et al., 2014).
- **Parameter sensitivities are key**: The magnitude of the efficiency gain depends on punishment cost, effectiveness (`punishment_tech`), group size (`player_count`), marginal per capita return (`mpcr`), continuation probability (game duration), prevalence of coordinated punishment or retaliation, and existence of reward options (multiple sources).
- **Nonlinear and non-monotonic effects**: Efficiency benefits can disappear or even reverse at high punishment costs, high continuation probabilities, presence of retaliation/antisocial punishment, noisy monitoring, or under certain population structures (Wolff, 2012; Dughera, 2022; Fang et al., 2020; Nakao, 2009; Camera & Gioffré, 2014).
- **Group size (`player_count`) effects**: Contrary to classic free-rider logic, larger groups can sometimes experience *greater* efficiency gains from punishment if punishers can coordinate (Hwang, 2017; Buchholz et al., 2014). However, very large groups may dilute enforcement unless punishment is nonrival.
- **Role of monitoring and information**: The effectiveness of punishment for efficiency is conditioned on monitoring technology (`punishment_tech`), quality of information (Chassang & Zehnder, 2016), speed/network structure (Balmaceda & Escobar, 2017), and ability to identify defectors.
- **Structural moderators**: Presence of leaders, reward mechanisms, spatial structure, and migration/community effects all change the comparative statics of punishment effects (Fang et al., 2020; Kaiping et al., 2016).

**Findings based on non-payoff behavioral outcomes:**
- Many papers (e.g., Chen et al., 2018; Kaiping et al., 2016) show that punishment increases contributions or cooperation rates, especially in networked or structured populations and under favorable parameter choices. However, these do not always translate directly to increased efficiency, especially if punishment cost is high.

**Ambiguity or conflicting results:**
- Some models find that punishment can reduce efficiency (or be neutral) if costs are high, punishment is misapplied, or retaliation/antisocial punishment is common (Wolff, 2012; Dughera, 2022; Brandts & Fatas, 2012).

# 5) Prediction Guidance

- The dominant theoretical expectation is that, for standard PGGs (4+ players, ~10 rounds, continuous contributions, moderate-to-high `mpcr`, moderate-cost punishment), **enabling punishment will increase average efficiency** compared to control (no-punishment), barring unusually high costs or prevalence of maladaptive punishment (Dutta et al., 2021; Kranz, 2010).
- **Crucial moderators** for efficiency gain include:
    - **Punishment cost and tech:** Higher punishment effectiveness (greater impact per unit cost) leads to greater efficiency gains; high costs can negate or reverse the gain.
    - **Player count:** Gains can persist or rise with group size if punishment is coordinated or nonrival, but may shrink in rival enforcement systems.
    - **Game length/continuation:** Punishment is more effective in finite or moderately long games; too long a horizon can undermine effect (Wolff, 2012).
    - **Presence of reward or alternative enforcement:** Efficiency gains from punishment may be less than those from reward, leader charisma, or motivational regimes (Dughera, 2022).
    - **Network structure:** Structured or dynamic networks, spatial populations, or community competition can amplify or reduce punishment’s effect according to the model specifics.
- **Baseline (control) efficiency is a strong predictor** for treatment efficiency; predicted treatment efficiency should not be lower than control unless costs of punishment are particularly high or mechanisms such as retaliatory/antisocial punishment are active.
- **Ambiguity remains** around domains with high antisocial punishment, complex retaliation, or noisy monitoring; in such cases, the effect of enabling punishment is parameter-sensitive and may fail to increase efficiency.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions:**
- `player_count` – Modeled in almost all theory papers; group size is treated as a crucial moderator.
- `num_rounds` / continuation probability – Central for repeated games, as game duration shapes payoffs and enforcement.
- `all_or_nothing` – Used in many models for simplicity; some allow continuous contributions.
- `mpcr` – Explicitly a key parameter in almost all efficiency models; higher `mpcr` universally supports greater punishment effectiveness.
- `punishment_cost`, `punishment_tech` – Directly manipulated and central to predictions of efficiency change; optimal punishment is high-impact, low-cost.
- `reward_exists`, `reward_cost`, `reward_tech` – Modeled in several papers as alternatives or complements to punishment.
- `show_other_summaries`, `show_n_rounds` – Modeled in relation to information flow, monitoring, and transparency; affect punishment’s targeting and sustainability.
- `chat` – Modeled less often, but sometimes included as a form of communication impacting cooperation.

**Indirectly/contextually discussed:**
- `default_contrib` – Occasionally mentioned in framing models (opt-in/opt-out), but not a focal variable.
- `show_punishment_id` – Touched upon in models where anonymity or observability shapes retaliation/antisocial punishment.

**Effectively missing or weakly modeled:**
- In-depth treatment of `chat`, `default_contrib`, and `show_punishment_id` is relatively sparse; their effects are acknowledged but rarely parameterized.

# 7) Important Limitations

- **Absence of empirical data**: All findings are theoretical or simulation-based; no direct experimental or field data.
- **Known contexts dominate**: Core findings are best supported for standard, well-mixed PGGs with canonical lab parameters (e.g., Fehr & Gächter–like designs). Other contexts (field games, large-scale or highly networked systems, interventions in real organizations) are less directly validated.
- **Non-payoff outcomes**: Many results infer efficiency changes from cooperation or contribution rates, but these may not account for the costs or maladaptive targeting of punishment.
- **Parameter sensitivity**: Several models show that positive effects only hold within certain parameter ranges (e.g., low cost, rare retaliation, nonrival enforcement). Real games may feature antisocial punishment, noisy monitoring, or other undermining factors not fully captured.
- **Missing behavioral moderators**: Important moderators such as norms, population heterogeneity, commitment ability, and group selection are often incorporated only in specialized models.
- **Sparse coverage of some design features**: Effects of chat/communication, contribution framing, and punishment/reward visibility are underexplored.
- **Generalizability**: Much of the logic is transferable, but exact quantitative predictions may not map onto real-world or experimental settings without calibration.

---

## Summary Table – Design Dimension Coverage

| Design Dimension             | Direct Evidence | Indirect/Contextual | Sparse/Missing  |
|-----------------------------|----------------|---------------------|-----------------|
| player_count                 | X              |                     |                 |
| num_rounds                   | X              |                     |                 |
| chat                        |                | X                   |                 |
| all_or_nothing               | X              |                     |                 |
| default_contrib              |                | X                   |                 |
| mpcr                         | X              |                     |                 |
| punishment_cost              | X              |                     |                 |
| punishment_tech              | X              |                     |                 |
| reward_exists                | X              |                     |                 |
| reward_cost                  | X              |                     |                 |
| reward_tech                  | X              |                     |                 |
| show_n_rounds                |                | X                   |                 |
| show_other_summaries         | X              |                     |                 |
| show_punishment_id           |                | X                   |                 |


---

### Concluding Guidance
- Theoretical models robustly support a positive effect of enabling punishment on efficiency in standard public goods games, with the strength and even direction of the effect depending on game parameters—especially punishment cost, effectiveness, and group structure.
- Predictions for treatment efficiency should be conservative outside the empirically validated parameter space (e.g., very large groups, high-cost or anti-social punishment contexts), and must explicitly account for the parameter sensitivities elucidated above.
- When empirical payoff outcomes are needed and only theoretical models are available, select parameter settings and baseline efficiencies closest to the real target environment, and recognize that uncertainty remains large in untested or edge-case parameter regimes.
- Direct transfer of qualitative findings is appropriate for standard lab-analog PGGs; quantitative predictions must be interpreted as upper bounds or illustrative outcomes, not exact expectations.
- Overall, this literature offers a rich and nuanced theoretical basis, but prediction tasks would benefit from supplementation with empirical calibration in future work.
