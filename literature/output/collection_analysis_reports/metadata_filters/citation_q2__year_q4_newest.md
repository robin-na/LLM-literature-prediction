# 1) Evidence Base

The paper set is composed of a substantial and diverse mix (n = 172) of empirical laboratory experiments, field experiments, and theoretical/computational models. Many studies are directly focused on public goods games (PGG) and their close variants, while others examine adjacent social dilemmas (e.g., prisoner's dilemma, collective risk games, trust games, and common-pool resource settings). A notable proportion of studies present empirical evidence with direct measurement of group efficiency or related payoff outcomes, yet a large number focus on behavioral proxies (e.g., cooperation rate, punishment behavior) without reporting efficiency. Theoretical models expand coverage to dynamic, networked, and ecological variants but may lack direct measurement of efficiency. Overall, the evidence base is broad in game and mechanism coverage, but the subset with direct relevance to predicting the efficiency impact of punishment in canonical PGGs is narrower.

# 2) Task Relevance

### a) `pgg_or_variant`
- **Exact relevance**: Many high-quality lab experiments and theoretical models directly implement the PGG or canonical linear PGG (e.g., Lo Iacono et al., 2023; Bahbouhi et al., 2024; Salahshour et al., 2022).
- **Close relevance**: Some studies use close variants such as threshold/collective-risk PGGs or common-pool resource games (Ntuli et al., 2023; Wang et al., 2025; Jiang et al., 2023).
- **Adjacent or weak**: Numerous papers use adjacent games (e.g., prisoner's dilemma, trust game, spatially structured dilemmas), which provide context or mechanistic insight but do not always transfer directly to standard PGG predictions.

### b) `punishment_or_sanctions`
- **Exact relevance**: Many studies manipulate or model peer punishment, centralized punishment, or exclusion as a sanction (Lo Iacono et al., 2023; Peng, 2022; Salahshour et al., 2022), and several compare different punishment technologies and costs.
- **Close adjacent**: Studies with reward as a primary mechanism, or those examining punishment-like mechanisms (e.g., exclusion, social reputation) are common.
- **None/irrelevant**: Several studies do not include punishment or sanctions at all, and cannot inform on its impact.

### c) `efficiency_or_related_payoff_outcome`
- **Exact**: A notable subset of experimental and theoretical studies directly report group efficiency, total group earnings, or explicit payoff-based metrics (Lo Iacono et al., 2023; Bahbouhi et al., 2024; Peng, 2022; Harrell & Wolff, 2023; Eichenseer, 2023).
- **Close**: Many studies provide near-equivalent outcomes (e.g., group welfare, probability of target achievement in threshold games, resource sustainability).
- **Adjacent/None**: A large proportion focus on behavioral outcomes (contribution, cooperation, punishment frequency) without mapping these to group efficiency/payoff ratios.

# 3) Outcomes Measured In The Literature

- **Payoff-related (efficiency, group payoff, total earnings, welfare)**: Measured and reported in a substantial subset of lab experiments and theoretical models, particularly those with exact or close task relevance.
- **Non-payoff behavioral (contribution rate, cooperation rate, punishment frequencies, norm compliance, etc.)**: Extremely common, both in empirical and theoretical work—even in PGGs. Many studies measure only behavioral proxies, making it critical to distinguish these outcomes when drawing inference for efficiency prediction.
- **Ambiguity**: Some papers conflate group cooperation with efficiency or do not specify whether reported increases in cooperation actually translate to higher aggregate payoffs (e.g., when costly punishment counteracts cooperation gains).

# 4) Main Findings Relevant To Prediction

**Empirical findings (lab/field PGGs):**
- **Punishment usually increases efficiency**: In canonical repeated linear PGGs, enabling peer punishment typically increases group efficiency/payoff compared to control, though often only after initial rounds or if design parameters (punishment cost, MPCR, institution choice) are favorable (Lo Iacono et al., 2023; Bahbouhi et al., 2024; Harrell & Wolff, 2023).
- **Costly punishment can offset efficiency gains**: In small groups or where punishment is used anti-socially or inefficiently, gains in cooperation may be negated by the direct costs of punishment (Peng, 2022; Grimalda et al., 2022; Gross et al., 2022; Eichenseer, 2023); some experiments report no net efficiency gain from enabling punishment.
- **Punishment technology and context are critical moderators**:
    - **Punishment cost-to-impact ratio**: Lower costs and higher impact ratios favor efficiency increases; high costs can erode gains (Bahbouhi et al., 2024; Salahshour et al., 2022).
    - **Punishment noise**: Stochastic punishment effectiveness (noise) reduces efficiency, mainly via increased anti-social punishment and less precise deterrence (Salahshour et al., 2022).
    - **Network/punishment structure**: Complete punishment networks do not always maximize efficiency; selective or incomplete networks may yield better outcomes by reducing costs (Pi et al., 2022).
    - **Team decision rules**: Unanimity in team punishment decisions can reduce anti-social punishment and thereby increase efficiency more than individual-based punishment (Bahbouhi et al., 2024).
    - **Group size and structure**: Larger, denser groups can see greater efficiency gains from punishment, provided the sanctioning is effective and not excessively costly (Harrell & Wolff, 2023; Eichenseer, 2023).
- **Institutional and environmental moderators**: Endogenous institution choice, feedback on rounds/others' behavior, and social context (e.g., history of conflict) affect the realized efficiency impact of punishment.
- **In collective-risk and resource management settings**: The efficiency impact of punishment is often contingent on features such as the resource growth rate, threshold effect, and the nature of the sanction (Ntuli et al., 2023; Wang et al., 2024; Libois, 2022).

**Theoretical/mechanism findings**:
- **Synergy between punishment and network/group structure**: Punishment is more efficient in structured or local networks than in well-mixed populations, with lower necessary punishment intensities to achieve cooperation (Lim & Capraro, 2022; Wang et al., 2025).
- **Threshold and bistability effects**: Models commonly show that efficiency gains from punishment only arise above certain punishment intensity/cost-effectiveness thresholds; below these, enabling punishment does little (Liu et al., 2024; Lv et al., 2023; Mondal et al., 2022).
- **Absence of universal positive effect**: Several models and reviews emphasize that enabling punishment does not guarantee an efficiency increase; payoff gains require that the design dimensions cross key parameter boundaries (Peng, 2022; Zhang & Pei, 2022).
- **Punishment can reduce efficiency under certain designs**: When punishment is assigned for non-normative or competitive reasons (e.g., status, anti-social motives), efficiency may fall, especially when costly attack options exist (Romano et al., 2024).
- **State-based feedback and dynamic mechanisms**: Adding dynamic or feedback-driven punishment/return (as in local state feedback or variable synergies) increases the likelihood of reaching the efficient equilibrium, especially in otherwise hard-to-coordinate environments (Wang et al., 2025; Liu et al., 2024).

# 5) Prediction Guidance

- **Use control (no-punishment) efficiency as a strong predictor**. In most studies, the direction and sometimes magnitude of the efficiency gain from enabling punishment depends critically on the baseline/control efficiency.
- **Adjust for punishment cost, technology, and structure effects**. Direct evidence indicates that the punishment cost-to-impact ratio (`punishment_cost`, `punishment_tech`), the presence of noise in implementation, and the network/punishment assignment rules (`punishment_tech`) are major moderators of the effect.
- **Account for group size and heterogeneity**. Larger groups with effective, local or networked punishment show greater and more robust efficiency gains from introducing punishment, provided the system avoids high anti-social or wasteful punishment.
- **Beware of parameter regimes with no gain or loss of efficiency**. In small groups, or where anti-social and/or excessive punishment occurs, the cost of punishment can offset or overwhelm gains from higher cooperation (Peng, 2022; Grimalda et al., 2022).
- **Consider institution adoption and learning context**. Efficiency gains are more likely when participants can select effective sanctioning institutions or have sufficient informational/memory resources to learn the effectiveness of punishment (Vasconcelos et al., 2022).
- **The efficiency impact is highly sensitive to key design dimensions**. The literature supports strong, non-linear, and sometimes contextually contingent effects; for instance, beneficiary and public good scales, the form of feedback, and team/shared responsibility all matter.
- **For reward-enabled environments**, reward mechanisms generally produce smaller efficiency gains than punishment, but may sustain high cooperation where punishment is absent or poorly targeted (Eichenseer, 2023; Mondal et al., 2022).

# 6) Design Dimensions Highlighted Across Papers

**Well informed (direct empirical or theoretical evidence):**
- `player_count`: Frequently manipulated or modeled; effects on efficiency are well documented (Lo Iacono et al., 2023; Eichenseer, 2023).
- `num_rounds`: Standard in repeated PGGs; effects on punishment’s efficacy are observed (Lo Iacono et al., 2023; Wang et al., 2025).
- `mpcr`: Explicit in most primary studies; higher MPCR typically increases both baseline efficiency and the potential gains from punishment (Peng, 2022; Wang et al., 2025).
- `punishment_cost`, `punishment_tech`: Heavily discussed; the cost-to-impact ratio and the nature/structure of punishment are central moderators (Salahshour et al., 2022; Pi et al., 2022).
- `all_or_nothing`: Studied less directly; some papers examine binary vs. continuous contribution (Bahbouhi et al., 2024; Pi et al., 2022).
- `chat`: Included in some studies; presence of chat/communication generally increases cooperation and can interact with punishment effects (Harrell & Wolff, 2023).
- `show_n_rounds`, `show_other_summaries`: Sometimes manipulated to explore informational context's effect on behavior and punishment (Eichenseer, 2023; Adams et al., 2022).

**Indirect or only contextually addressed:**
- `default_contrib`: Rarely a primary focus but discussed in framing/conceptual contexts.
- `reward_exists`, `reward_cost`, `reward_tech`: Studied mainly in theoretical or reward-focused papers; generally less directly tested in PGGs with both punishment and reward.
- `show_punishment_id`: Occasionally addressed via anonymity/identifiability manipulations (Gross et al., 2022).
- **Dynamic and contextual moderators (history of conflict, culture, institution adoption rules)**: Explored qualitatively and in some comparative studies but less often as explicit manipulated dimensions.

**Effectively missing or underrepresented:**
- Some dimensions, like `default_contrib` or specific feedback/reporting rules (`show_punishment_id`, `show_other_summaries`), receive little direct experimental study regarding their impact on the efficiency effect of punishment.

# 7) Important Limitations

- **Behavioral outcomes ≠ efficiency**: Many studies report behavioral outcomes (contribution, cooperation rates) rather than efficiency or group payoff. While correlated, high contributions do not guarantee higher efficiency if punishment is inefficient or anti-social.
- **Sparse coverage on some design dimensions**: Direct empirical evidence is limited for dimensions such as `default_contrib`, nuanced feedback, or the interplay between reward and punishment mechanisms within the same environment.
- **Generality/scope of findings**: Many results are established under standard, tightly controlled designs (fixed player count, punishment cost/tech, homogeneous groups). The effect of punishment in environments with other institutional or feedback changes may not generalize without caution.
- **Ambiguity in direction/magnitude**: Disagreement remains about when punishment increases, has no effect, or reduces efficiency—especially where anti-social punishment, high costs, or status/competitive motives are present.
- **Cross-study variation and context dependence**: The magnitude and sometimes the direction of the efficiency impact depend strongly on initial conditions, specific implementation of sanctioning, network structure, and environmental feedback. Nonlinearities and threshold effects are common.
- **Adjacency of many models**: Theoretical or computational work often uses adjacent but non-PGG models (PD, trust game), requiring careful interpretation or transfer of insights.

---

**In summary:**  
There is robust, multi-modal evidence that enabling peer punishment increases group efficiency in standard repeated public goods games, but the magnitude and reliability of this effect are highly sensitive to cost structures, punishment implementation, network and feedback structures, and environment-specific moderators. The control efficiency provides a strong baseline for prediction, with design dimensions such as player count, rounds, MPCR, and punishment details further accounting for treatment effects. However, not all environments or mechanisms yield efficiency gains, and an overreliance on behavioral outcomes or on studies with adjacent settings should be avoided in quantitative prediction.
