# 1) Evidence Base

The paper set consists entirely of theoretical and simulation works, with no direct empirical or experimental studies represented. The majority of the papers are formal modeling studies, agent-based simulations, or game-theoretic analyses focusing on public goods games (PGGs), close variants (e.g., collective risk dilemmas, commons games), and sometimes adjacent games (e.g., trust games, division of labor in networks, Prisoner’s Dilemmas). There is a strong concentration on the effects of punishment and related institutional interventions, though some papers discuss rewards, reputation, or norm enforcement as alternative or complementary mechanisms.

The coverage of the prediction task—estimating the effect of enabling peer punishment on efficiency outcomes in PGG-like environments from design dimensions and control efficiency—is broad in terms of mechanistic perspectives and payoff conditions. However, it is almost exclusively theoretical. While many papers report or model efficiency or closely related payoff outcomes, a substantial subset focus instead on behavioral outcomes such as cooperation rates, prevalence of strategies, or norm compliance, offering only indirect support for the prediction task. There is some depth in parameter exploration and design dimension mapping, but the lack of empirical data constrains calibration to real-world or lab PGGs.

# 2) Task Relevance

Below is a synthesis of the literature’s relevance to three target-relevance axes:

**pgg_or_variant**:  
- *exact*: Several papers model canonical public goods games or their direct extensions (e.g., Bühren et al., 2023; Zefferman, 2023; Botta et al., 2024; Kang et al., 2024; Shin et al., 2022; Okada et al., 2021; Battu, 2021), with explicit mapping to group size, MPCR, contribution structure, and punishment mechanisms.
- *close/adjacent*: Many studies analyze games structurally or functionally similar to PGGs, such as collective risk dilemmas (Garrido et al., 2025), resource harvesting, trust games, division of labor, and multi-player Prisoner's Dilemmas. In these cases, payoff externalities and strategic interdependence persist, even if formal details differ.
- *weak/none*: A minority of papers focus on environments where either the public goods structure or player interdependence is significantly different or missing (e.g., biological markets).

**punishment_or_sanctions**:  
- *exact*: Direct modeling or analysis of peer punishment or institutional punishment is common.
- *close/adjacent*: Some papers deal with reward mechanisms, reputation-based sanctions, or psychic/internalized costs, often as alternatives or complements to punishment.
- *none*: A small subset focus solely on baseline (no punishment) cases, useful mainly for control efficiency estimation.

**efficiency_or_related_payoff_outcome**:  
- *exact*: Efficiency (as defined—group payoff relative to the cooperative optimum) is a primary outcome in a significant subset (Bühren et al., 2023; Zefferman, 2023; Botta et al., 2024; Garrido et al., 2025; Chiba-Okabe & Plotkin, 2024; Itao & Kaneko, 2025; J. García & Traulsen, 2025; Mohlin et al., 2023; Berger & De Silva, 2021; Ezeigbo, 2017; Nirjhor & Nakamaru, 2023a/b).
- *close*: Other studies focus on total earnings, welfare, or surplus.
- *adjacent/weak*: Some report only on cooperation/contribution rates or frequencies of strategies, sometimes inferring payoff effects but not measuring them directly.
- *none*: A few do not measure payoff or efficiency at all.

**Summary**:  
Relevance to the prediction task is highest where the literature models PGGs with explicit efficiency/payoff outcomes and manipulates punishment, moderate in close structural variants, and low or missing in adjacent/non-payoff focused work.

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes (Directly Relevant):**
- Group efficiency (defined as payoff vs. cooperative optimum): Found in a notable portion of papers (e.g. Bühren et al., 2023; Zefferman, 2023; Botta et al., 2024; Garrido et al., 2025; Chiba-Okabe & Plotkin, 2024).
- Total group payoff, welfare, accumulated wealth, surplus, or related economic measures: Frequently modeled and often interchangeable with efficiency in the theory.
- Explicit measures of payoff differentiation between regimes (punishment enabled/disabled).

**Non-Payoff Behavioral Outcomes (Indirect/Not Directly Relevant):**
- Contribution rates, cooperation rates, or prevalence of various strategies: Most common outcomes in evolutionary or agent-based modeling papers (e.g., Kang et al., 2024; Shin et al., 2022; Okada et al., 2021; Battu, 2021).
- Punishment frequency, strategy abundance, or norm compliance: Tracked in many papers as proxies for ‘cooperative environment’, but these are not payoff/efficiency outcomes and can diverge (e.g., punishment may increase cooperation but reduce efficiency due to costs).
- Extinction/transition dynamics: Sometimes highlighted (e.g., Ibrahim, 2022), but not always convertible to payoff gains or losses.

**Ambiguity**:  
Outcomes are sometimes adjacent, e.g., when increased cooperation is presumed to translate to efficiency, but without reporting on the costs of punishment or institutional support, such implications are uncertain.

# 4) Main Findings Relevant To Prediction

- **Punishment can increase, decrease, or leave unchanged group efficiency, depending on design dimensions and baseline cooperativeness**.  
  - When punishment is *efficient* (i.e., the cost to punishers is low relative to its deterrent effect), enabling punishment can move efficiency close to the social optimum, especially if monitoring is effective and group size is manageable (Bühren et al., 2023; Zefferman, 2023; Botta et al., 2024; Nirjhor & Nakamaru, 2023a/b).
  - When punishment is *costly or ineffective*, it may reduce efficiency due to wasted punishment expenditures, even if cooperation/contribution rates rise (Bühren et al., 2023; Ezeigbo, 2017).

- **The effect of punishment is highly conditional on group composition and baseline conditions**.  
  - In low-cooperation groups, severe punishment can bring efficiency gains (Bühren et al., 2023), but in groups already near the cooperative optimum, punishment costs may outweigh marginal gains and reduce efficiency.
  - Heterogeneity in social preferences (e.g., mixture of conditional cooperators and selfish types) complicates predictions—mild punishment may help mid-cooperators but not extremes (Bühren et al., 2023).

- **Institutional design (flexibility, voting, monitoring structure) is critical**.
  - Mixed institutions (enabling both reward and punishment) or locally decided institutions outperform fixed punishment-only systems in threshold PGGs and related environments (Garrido et al., 2025; Chiba-Okabe & Plotkin, 2024).
  - Hierarchical or distributed monitoring changes how scalable punishment is, especially as group size increases (Zefferman, 2023).

- **Parameter thresholds often determine regime transitions**.  
  - There exist critical thresholds for punishment severity, scope, or monitoring efficiency, below which punishment is ineffective and wasteful, and above which cooperation and efficiency can be stabilized (Botta et al., 2024; Nirjhor & Nakamaru, 2023a/b).
  - The impact of group size, MPCR, and punishment cost interact with these thresholds (Zefferman, 2023).

- **Information and transparency can alter the effect of punishment**.
  - Rich and low-cost reputation information can undermine the deterrent effect of punishment, and may even reverse efficiency gains, especially in smaller or dyadic games (Berger & De Silva, 2021).

- **Reward mechanisms and internalized norms sometimes outperform or supplement punishment**.
  - Reward-only and mixed systems are sometimes more efficient, especially if punishment is costly or risks antisocial misuse (Garrido et al., 2025; Zhou et al., 2022).
  - Reputation-based enforcement and psychic costs can also sustain cooperation, but the absence of punishment may limit stability in more challenging environments (Lie-Panis et al., 2024).

- **Special cases and edge conditions**:  
  - In rare cases, enabling punishment can have negative effects on efficiency, especially if sophisticated defectors adaptively evade sanctions (Ibrahim, 2022), or if group size and institutional capacity are mismatched.

# 5) Prediction Guidance

- **The most robust evidence for predicting treatment efficiency from design dimensions and control efficiency comes from papers directly modeling PGGs with efficiency outcomes under several parameter regimes (Bühren et al., 2023; Zefferman, 2023; Botta et al., 2024)**. These models show that:
  - If the control game (punishment disabled) has low efficiency due to low cooperation, and the punishment regime is *efficiently parameterized* (low punishment cost, high effect), enabling punishment is likely to increase efficiency, potentially drastically.
  - If the control game already has high efficiency, enabling punishment may yield little or even negative net impact, due to introduction of new costs.
  - The direction and size of the payoff effect depend on specific design dimensions, especially punishment cost (`punishment_cost`), magnitude (`punishment_tech`), MPCR, group size, and monitoring/information structure.

- **Parametric or threshold-based predictions** are supported: One can expect large gains in efficiency from punishment only when system parameters cross analytic or simulation-identified thresholds (cost-benefit of punishment, monitoring range, etc.; Zefferman, 2023; Botta et al., 2024).

- **Indirect or context-specific modifiers**:
  - High transparency/monitoring or institutionally flexible systems (voting, responsive severity) further raise potential efficiency (Garrido et al., 2025).
  - If reward exists and can be mixed with punishment, often the best predicted outcomes require some balance (Chiba-Okabe & Plotkin, 2024; Zhou et al., 2022).
  - Structures that allow learning or endogenous institution formation (Bühren et al., 2023) can self-tune toward more efficient regimes.

- **Design dimensions not explicitly discussed** are best treated as moderators but require imputation or analogical reasoning rather than direct evidence.

- **Control efficiency is a critical anchor**: Most theoretical models predict the treatment effect of punishment *relative* to the control regime. Direct prediction should thus use observed/measured control efficiency for the given design as the baseline, then apply the dimension-informed expected gain or loss from enabling punishment.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Design Dimensions**:
- `player_count` (group size): Explicit in nearly all theory and simulation papers; its effect is generally monotonic—larger groups make effective cooperation via punishment harder to sustain unless punishment/monitoring scales efficiently (Zefferman, 2023; Botta et al., 2024).
- `num_rounds`: Models with repeated games report on long-run equilibria or learning dynamics (Bühren et al., 2023; Nirjhor & Nakamaru, 2023a/b).
- `all_or_nothing` (binary vs. continuous): Modeled in several papers and interacts with punishment efficacy, but not always systematically compared (Okada et al., 2021).
- `mpcr` (public goods multiplier): A key parameter widely analyzed (Bühren et al., 2023; Zefferman, 2023).
- `punishment_cost`, `punishment_tech` (punishment magnitude/severity): Central moderators across nearly all punishment-focused models (Bühren et al., 2023; Botta et al., 2024).
- `reward_exists`/`reward_cost`/`reward_tech`: Modeled in papers examining institutional design and mixed sanctioning (Garrido et al., 2025; Zhou et al., 2022).

**Indirectly or Contextually Discussed Dimensions**:
- `chat`: Rarely modeled, only contextually discussed as a potential modifier.
- `show_other_summaries`, `show_punishment_id`, `show_n_rounds`: Sometimes discussed as information/reputation mechanisms; evidence is indirect (Berger & De Silva, 2021).
- `default_contrib`: Contribution framing discussed in the context of norm evolution (Battu, 2023), but not directly matched to efficiency predictions.

**Effectively Missing or Sparsely Addressed**:
- Some dimensions (e.g., exact interface elements, real-world communication tools) are not systematically manipulated in the theory literature.
- Little evidence on direct effect of chat, punishment identity disclosure, or details of reward cost/tech beyond a few institutional papers.

# 7) Important Limitations

- **Entirely theoretical/simulation-based**: Absence of empirical or experimental data limits estimation of effect sizes and external validity outside model assumptions.
- **Parameter Calibration Uncertainty**: Model results are precise only for the parameter spaces explored; real-world or specific PGG settings may lie outside these calibrated regions or involve unmodeled nuances (human error, misapplied punishment, etc.).
- **Behavioral–Payoff Disconnect**: Many papers focus on cooperation rates or strategy prevalence, which can move independently of efficiency if punishment is costly.
- **Heterogeneity and Structure**: Most models assume homogeneous players or fixed structures. Real groups may have more diverse social preferences, incomplete information, or complex learning.
- **Mapping Limits**: Some prediction dimensions are only contextually or analogically addressed, not systematically analyzed across papers (especially chat, identity disclosure, and interface features).
- **Edge-case or Unmodeled Effects**: Several papers highlight cases where punishment fails to raise efficiency, such as when defectors adaptively evade sanctions, where institutional costs are excessive, or where information structure undermines deterrence—these circumstances may be underrepresented.
- **Institutional Specificity**: Results from voting-based, flexible, or third-party institutions may differ sharply from peer-only punishment environments.

**In summary:**  
The literature provides strong theoretical and simulation support for the conditions under which enabling punishment raises or lowers group efficiency in PGG-like environments. Prediction is most accurate where design dimensions (especially cost and scope of punishment, group size, MPCR) and baseline efficiency are known, and caution is warranted in high-cooperation or high-punishment-cost domains or where design features (chat, information) are not directly addressed in the models. The lack of empirical data and the frequent focus on behavioral—rather than payoff—outcomes are key limitations for downstream efficiency prediction.
