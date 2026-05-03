# 1) Evidence Base

The reviewed paper set consists predominantly of theoretical papers deploying analytical modeling or agent-based simulation rather than empirical or experimental studies. Most papers are adjacent to the public goods game (PGG) paradigm, focusing on related multi-actor social dilemmas or evolutionary game scenarios, and frequently examining the role of punishment and sanctions. Only one paper (Gao et al., 2024) reports empirical/observational data, and this is limited to a bibliometric overview without quantitative payoff outcome synthesis. Overall, the set is broad regarding mechanisms and contexts (including regulatory games, networked and agent-based models, and environmental governance), but narrow in direct, empirical coverage of efficiency changes in canonical PGGs due to punishment interventions.

# 2) Task Relevance

**PGG or Variant (`pgg_or_variant`)**:  
- **Exact relevance**: Only one paper—Park (2022)—directly models a PGG, but it does not include punishment or rewards.  
- **Adjacent relevance**: Most other papers examine PGG-like or closely related social dilemmas (e.g., trust games, common-pool resource dilemmas, principal-agent models, public health regulation, water pollution governance, construction innovation, etc.), sometimes with formal structural similarities to the PGG but with context-specific modifications.

**Punishment or Sanctions (`punishment_or_sanctions`)**:  
- **Exact/close relevance**: Most papers analyze punishment as a mechanism explicitly, though the form, implementation, and nature of punishment (peer, institutional, dynamic/static, etc.) frequently vary from standard PGG experiments.
- **None**: The sole direct PGG paper (Park, 2022) does not consider punishment at all.

**Efficiency or Related Payoff Outcome (`efficiency_or_related_payoff_outcome`)**:  
- **Exact**: Only Lim & Capraro (2022) (theoretical, on trust games) and Park (2022) (PGG, but no punishment) model mean payoff or efficiency as primary outcomes.
- **Adjacent/weak**: Nearly all other papers focus chiefly on non-payoff behavioral outcomes—strategy profiles, compliance rates, cooperation likelihood, or the stability of cooperative equilibria—with efficiency, group payoff, or surplus not directly calculated or reported.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes**: Only two papers (Park, 2022; Lim & Capraro, 2022) report or model mean payoff or efficiency, and of these, only Lim & Capraro (2022) considers punishment. The remaining works do not provide efficiency or payoff as measurable outputs.
- **Non-Payoff Behavioral Outcomes**: Nearly all other papers focus on compliance rates, cooperation probabilities, equilibrium strategy profiles, the probability of legal versus illegal action, or the frequency of sanctioning—i.e., outcomes linked to behavior and norm adherence, not group payoff or efficiency per se.
- **Outcome distinction**: In almost all cases where increased punishment is said to promote cooperation, this evidence is behavioral (norm compliance, self-discipline, reduced defection) rather than payoff-based.

# 4) Main Findings Relevant To Prediction

- **Theoretical models support that punishment can promote cooperation** (Li et al., 2023; Lim & Capraro, 2022; Huo & Liu, 2024; Wang & Mao, 2024), which by standard mechanisms should, in principle, increase average group payoff and thus efficiency. However, except for Lim & Capraro (2022), this implication is not measured or quantified.
- **Punishment effects are moderated by mechanism specifics**:  
    - **Dynamic vs. static punishment**: Dynamic (behavior-dependent) punishment is found to be more effective at stabilizing cooperation than static punishment (Wang & Cui, 2022; Jiang & Zheng, 2024).
    - **Institutional structure**: Punishment implemented institutionally and in conjunction with network structure can create synergy, achieving full efficiency at lower cost in trust games (Lim & Capraro, 2022).
    - **Cost and efficacy of punishment**: Results suggest efficiency benefits only accrue up to the point where punishment costs begin to reduce net payoffs (Lim & Capraro, 2022).
    - **Network structure and heterogeneity**: Networked environments and the presence of key nodes (high centrality) can amplify the effect of punishment on behavioral outcomes (Li et al., 2023).
- **Reward mechanisms and interplay with punishment**: Several models include both punishment and reward, generally finding that punishment is a more reliable promoter of prosocial behavior than reward—though the two can interact, with excessive rewards sometimes undermining compliance (Wang & Cui, 2022; Jiang & Zheng, 2024; Li et al., 2023; Huo & Liu, 2024).
- **Empirical payoff evidence is sparse**: Only Lim & Capraro (2022) provides explicit analytical payoff/efficiency results linking punishment to improved efficiency in PGG-adjacent trust games; theory suggests maximal efficiency at the threshold punishment level that induces full cooperation.

# 5) Prediction Guidance

- **Direct guidance for the downstream prediction task is limited** due to the paucity of empirical PGG studies measuring efficiency with punishment manipulations. The main theoretical result coming closest is Lim & Capraro (2022), who show that enabling punishment in trust games boosts efficiency up to a threshold, especially in the presence of structured networks, but that excessive punishment cost can erode efficiency gains.
- **For PGGs or similar social dilemmas, one can expect**:
    - Enabling peer or institutional punishment will usually increase efficiency when baseline (control) efficiency is below the full-cooperation benchmark, unless punishment is set prohibitively costly (so that costs outweigh gains from reduced free-riding).
    - The strength of this effect, and its dependence on experimental parameters, remains uncertain—almost all other theory and simulation work only report improved cooperation/compliance rates, not net payoff or efficiency.
    - Punishment is likely to be more efficient when implemented dynamically (as a function of observed behavior), less so if static, and more effective in network-structured populations when punishment is not too costly.
    - Reward systems and their costs should also be considered; excessive or poorly calibrated rewards may not enhance (and may even reduce) compliant behavior or efficiency.
- **Control efficiency remains a useful baseline**, but in the absence of more direct quantitative results, the size of efficiency increase due to punishment must be inferred cautiously, primarily from theoretical mechanisms rather than empirical evidence.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions**  
- `player_count`: Explicit parameter in nearly all theory models; affects the effectiveness of punishment (e.g., larger groups may dilute individual impact).
- `num_rounds`: Modeled in some agent-based or repeated games (Park, 2022; Armstrong et al., 2024), but not often discussed in terms of its impact on efficiency/punishment interaction.
- `all_or_nothing`: Modeled in most papers; may affect the severity of defection/cooperation and hence the role of punishment.
- `mpcr`: A critical parameter both in PGG (Park, 2022) and many adjacent models (Lim & Capraro, 2022); higher MPCR (returns to cooperation) tend to amplify the benefits of cooperation enforcement via punishment.
- `punishment_cost`: Central to all punishment-related models; higher cost often diminishes the net payoff effect of punishment.
- `punishment_tech` (i.e., punishment effectiveness): Sometimes explicit (e.g., upper limits, dynamics—Jiang & Zheng, 2024; Lim & Capraro, 2022).
- `reward_exists`: Explicit in most models, often as a comparator to punishment.

**Indirectly Informed/Contextually Discussed Dimensions**  
- `chat`, `default_contrib`, `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Rarely explicitly modeled; communication and information feedback (chat/summary) discussed at the field overview level (Gao et al., 2024) as relevant mechanisms but not parameterized.
- `reward_cost`, `reward_tech`: Discussed contextually where models include rewards; effect on compliance and interaction with punishment often explored, but impact on efficiency rarely measured.

**Effectively Missing**  
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id`, `default_contrib`: Not parameterized or analyzed in existing models; their influence on the efficiency impact of punishment remains undiscussed in the reviewed paper set.

# 7) Important Limitations

- **Lack of empirical data**: There is a major deficit of experimental or observational data directly linking punishment to efficiency gains in canonical PGGs within this literature set.
- **Outcomes are mostly behavioral, not payoff-based**: Most evidence regarding the benefits of punishment focuses on cooperation or compliance rates, not changes in group payoff or efficiency.
- **PGG specificity is limited**: Many papers use structurally similar but non-identical social dilemma games, introducing potential translation problems for direct PGG prediction.
- **Punishment mechanisms are often institutional, dynamic, or context-specific**, potentially diverging from standard peer punishment protocols in PGG labs.
- **Moderating effects (network structure, cost, dynamic rules) are not consistently quantified** for efficiency. Mechanistic findings often imply but do not demonstrate or fully parameterize their aggregate impact on payoffs.
- **Nearly all design dimensions except punishment and MPCR are underexplored** as moderators of the treatment effect on efficiency within this literature.
- **Ceiling effects are not considered**: Scenarios with near-maximal efficiency under control are not explored for potential null or negative punishment effects.
- **Reward mechanisms are inconsistently incorporated**, with the potential for unintended impacts on norm compliance, but rarely on efficiency directly.

**In summary:** While the reviewed literature is rich in theoretical and mechanistic insight regarding how punishment may promote cooperation in social dilemmas, direct quantitative evidence on its impact on group efficiency in public goods games, and on how this impact varies with experimental design dimensions, remains sparse. Predictors should therefore be cautious: benefit is likely, especially when punishment is modestly costly and designed dynamically, but the literature does not provide robust parameter-level guidance for predicting the magnitude of such efficiency gains.
