# 1) Evidence Base

The literature set is composed entirely of theoretical and simulation-based papers (no empirical or experimental papers), almost all published in the domains of evolutionary game theory, social physics, and computational economics. The set is broad in terms of modeling approaches (evolutionary dynamics, agent-based simulation, game-theoretical analysis) and spans a variety of public goods game (PGG) structures as well as adjacent settings (prisoner’s dilemma, common-pool resource, trust games, and organizational dilemmas). About a dozen papers are **directly relevant**—providing exact or close modeling of PGGs **with variable punishment** and reporting outcomes interpretable as efficiency or related group payoff. Many others are **indirectly informative or adjacent**, reporting on behavioral outcomes (e.g., cooperation rate) or focusing on alternative cooperation-promoting mechanisms (e.g., reward, social learning, reputation, network adaptation) without explicit or standardized implementation of punishment or direct measurement of efficiency.

The **mix is heavily theoretical and simulation-based**, with most papers reporting analytical equilibria, numerical simulation results, or comparative statics with respect to game parameters. Direct empirical, experimental, or field evidence is missing.

# 2) Task Relevance

## pgg_or_variant
- **Exact**: Several papers model classic or well-matched variants of the public goods game (Powers, 2018; Zhang & Cao, 2020; Sui et al., 2018; Zhang, Cui & Yue, 2019; Wang, Liu & Chen, 2020; Wang et al., 2021; Quan et al., 2018 [two papers]; etc.).
- **Close**: Others model nonlinear or threshold PGGs, exclusion as punishment, or common-pool resource settings that maintain close structural similarity (Gao & Liang, 2020; Kol'veková et al., 2021; Brandt & Svendsen, 2019; Yan et al., 2021).
- **Adjacent**: Many further papers study related social dilemmas (prisoner’s dilemma, trust game) or organizational analogs with somewhat different payoff structures or mechanisms.

## punishment_or_sanctions
- **Exact**: About 15-20 papers model explicit peer punishment or institutionally-coordinated punishment as a controlled, standardized mechanism.
- **Close/Adjacent**: Others examine exclusion, centralized (pool) punishment, tax-funded incentives, third-party sanctions, or non-human/automated enforcement, which share aspects of the target mechanism but may include features absent from standard peer punishment structures.
- **None/Weak**: Several focus exclusively on reward, reputation, partner selection, or mechanisms not involving punishment.

## efficiency_or_related_payoff_outcome
- **Exact**: A subset reports **efficiency** (mean group payoff relative to full cooperation) or **mean total payoff/welfare** (Powers, 2018; Zhang & Cao, 2020; Sui et al., 2018; Zhang, Cui & Yue, 2019; Wang, Liu & Chen, 2020; Quan et al., 2018; Yan et al., 2021; Gao & Liang, 2020; Kol'veková et al., 2021; Brandt & Svendsen, 2019; Podobnik et al., 2019; Baker & Choi, 2018; etc.).
- **Close/Adjacent**: Others report only **cooperation rates**, provision or contribution rates, or frequencies of strategies, using these as proxies for efficiency but not reporting payoff directly. Some report costs of incentives or cumulative cost to achieve cooperation.
- **None**: Several papers do **not report any payoff-based outcome** and focus solely on behavioral dynamics.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes**:
  - **Group efficiency** (ratio of actual group payoff to payoff under universal cooperation): directly reported or available through explicit examples within several papers.
  - **Total group payoff/utility/welfare/surplus/mean payoffs**: commonly used as a proxy or direct substitute for efficiency.
  - **Costs of punishment/reward mechanisms**: sometimes reported as cumulative cost subtracted from group payoff to compute net efficiency.

- **Non-payoff behavioral outcomes**:
  - **Contribution rate/cooperation frequency**: most frequently reported outcome; often used as an indirect indicator of efficiency but not equivalent.
  - **Punishment frequency or assignment, norm compliance, exclusion rates**: sometimes tracked as additional behavioral indicators.
  - **Provision rates or resource levels**: for threshold or resource-replenishing games (e.g., CPRs).
  - **Mechanism/process level outcomes**: e.g., stability of cooperation, phase transitions, or dynamics.

Across the set, **behavioral outcomes substantially outnumber direct payoff-based outcomes**, and even when payoff is reported, efficiency as defined for prediction—relative to full cooperation—is less commonly calculated.

# 4) Main Findings Relevant To Prediction

**Synthesizing across the most directly relevant papers:**

- **General pattern**: Enabling peer or institutional punishment in public goods games, all else equal, **tends to increase efficiency (group payoff) compared to a no-punishment control**, but only under the condition that:
    - Punishment is strong enough (high fine/low cost to punisher)
    - Sufficient resources or willingness to punish are present in the group
    - Institutional context ensures the mechanism is actually used and not underutilized due to individual incentives

- **Moderators and boundary conditions**:
    - **Punishment cost**: Lower cost to punisher and higher cost to punished favor higher efficiency gains (Zhang, Cui & Yue, 2019; Sui et al., 2018; Wang, Liu & Chen, 2020; Kol'veková et al., 2021)
    - **MPCR (Marginal Per Capita Return/synergy factor)**: Higher MPCR strengthens the positive effect of punishment; at low MPCR, effect may vanish or reverse (Zhang & Cao, 2020; Quan et al., 2018)
    - **Group size**: Smaller groups may achieve full cooperation/efficiency more readily with punishment, whereas large groups may underinvest in punishment/incentives, reducing the effect (Powers, 2018; Zhang & Cao, 2020)
    - **Alternative mechanisms**: When disguise or insurance mechanisms allow defectors to avoid punishment, the effect of punishment on efficiency can be undermined (Wang, Liu & Chen, 2020)
    - **Institutional vs. peer punishment**: Institutional mechanisms, especially when properly funded (tax or central pool), can achieve similar or sometimes greater efficiency gains, but weak or excessive punishment/intervention can be counterproductive (Yang & Fu, 2020; Kol'veková et al., 2021)
    - **Risk, inequality, or resource scarcity**: Under high resource or payoff variance, the efficacy of punishment is diminished; punishment may fail to prevent collapse if external conditions are harsh (Nhim et al., 2019)
    - **Antisocial punishment or misguided punishment**: In environments where punishment is not reliably targeted at defectors (e.g., antisocial punishment or overuse), efficiency can be reduced despite higher cooperation rates (Quan et al., 2019; Schunk & Wagner, 2021)
    - **Joint effects of punishment and reward**: In games where both are available, reward can sometimes be more efficient, especially when initial cooperation levels are low; hybrid protocols can outperform pure punishment (Wang et al., 2021; Kol'veková et al., 2021)

- **Exceptions and caveats**:
    - In some models, punishment increases cooperation rate but reduces efficiency because the cumulative cost of punishment outweighs payoff gains (Quan et al., 2019).
    - If punishment is set excessively high or overused, system collapse or negative payoffs may result (Podobnik et al., 2019).
    - Control efficiency is not always a reliable predictor: in some regimes, introducing punishment moves a low-efficiency system to high efficiency, but in others, the change is minimal or negative if punishment is poorly calibrated or mis-targeted.

# 5) Prediction Guidance

The literature supports **conditional prediction rules** for the efficiency effect of enabling peer punishment in public-goods-game-like environments, summarized as:

- **Baseline Guidance**:
    - If the control (no-punishment) game has low efficiency due to defection, and design parameters allow for effective, not-too-costly punishment, **enabling peer punishment is likely to produce a substantial increase in efficiency**.
    - The magnitude of gain is highest when **punishment cost is low, fines are high, MPCR is high, and group size is moderate/small**.

- **Moderating/Conditional Guidance**:
    - If **punishment cost is high**, or if punishing is unattractive to participants (insufficient willingness/resources for enforcement), the **effect of peer punishment on efficiency can be modest, null, or even negative**.
    - If **detected defectors can easily evade/avoid punishment** (e.g., disguise or insurance), efficiency gains are unlikely (Wang, Liu & Chen, 2020).
    - If **antisocial punishment**, mis-targeting, or high punishment frequency occurs, **efficiency may decrease despite higher cooperation rates** (Quan et al., 2019).
    - **Institutional/centralized punishment mechanisms** can produce similar effects to peer punishment but are sensitive to intervention strength and population structure (Yang & Fu, 2020; Kol'veková et al., 2021).
    - **Reward mechanisms** may be preferable or more efficient under certain initial conditions (low cooperation baseline) (Wang et al., 2021).
    - **Large groups** and/or **resource-scarce, unequal, or volatile environments** dampen the effect of punishment; in these, prediction is more uncertain or negative for efficiency improvement.
    - The **majority of models assume well-mixed populations**; spatial, network, or structured populations may show reduced or delayed efficiency gains due to local interaction, boundary effects, or coordination failures.

- **Dimension Use in Prediction**:
    - **Directly informed dimensions**: Player count, num_rounds, mpcr, all_or_nothing, punishment_cost, punishment_tech, and to some extent reward_exists and reward_cost.
    - **Indirectly or contextually informed dimensions**: default_contrib (as initial condition framing), show_other_summaries, show_n_rounds, show_punishment_id, chat.
    - **Missing or poorly informed dimensions**: Several display/communication dimensions (chat, show_other_summaries, show_punishment_id), as these are rarely explicitly manipulated in the theoretical literature.

- **Key Interpretative Note**: Where literature reports only contribution/cooperation rates, use caution: these do **not** always map directly to efficiency, as the cost of punishment may outweigh cooperation gains.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed by theory/simulation regarding efficiency:**
- `player_count`: Small groups favor higher efficiency gains from punishment; inverse or neutral effect in large groups (Powers, 2018; Zhang & Cao, 2020; Kol'veková et al., 2021).
- `num_rounds`: Repeated games generally facilitate learning and coordination, but diminishing returns or endgame effects can play a role; specifics less often varied independently.
- `all_or_nothing`: Both continuous and all-or-nothing PGGs modeled; generally, the results apply to both, though contribution granularity can modulate coordination/punishment effectiveness.
- `mpcr`: High marginal per capita return (synergy) consistently increases the positive effect of punishment on efficiency (multiple sources).
- `punishment_cost` and `punishment_tech`: Central to all main models; effect of punishment on efficiency strongly depends on these.
- `reward_exists`, `reward_cost`: When included, direct trade-offs between reward and punishment for efficiency are mapped (Wang et al., 2021; Kol'veková et al., 2021).

**Indirectly or contextually discussed:**
- `default_contrib`: Only occasionally discussed as a framing/inertia effect.
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id`, `chat`: Rarely explicitly modeled—infrequent in theoretical models; empirical effects on efficiency under punishment remain unclear.

**Essentially missing:**
- Display and communication dimensions (`chat`, identity transparency, round display, peer summaries) are almost entirely ignored in modeling, so their effect on the efficiency impact of punishment is unknown from this literature.

# 7) Important Limitations

- **No direct empirical or experimental evidence**: The entire set is theoretical/simulation-based; empirical generalizability and real human behavioral variation are unknown.
- **Efficiency and payoff often inferred, not directly measured**: Many papers report cooperation rates or related behavioral outcomes but do not present efficiency as a ratio to full cooperation, requiring caution in inference.
- **Sparse evidence on some design dimensions**: Display/communication features (chat, transparency, ID show) and framing effects (default_contrib) are underexplored in current models.
- **Limited direct mapping to complex or hybrid mechanisms**: Most results pertain to standard PGGs or their closest variants; applicability to games with combined or innovative punishment/reward technologies is less certain.
- **Parameter ranges and boundary cases**: Many positive findings hinge on parameter regimes (e.g., punishment cost, group size, MPCR) being within certain bounds; outside these, effects can reverse or vanish.
- **Behavioral realism**: No discussion or modeling of non-rational, emotional, or boundedly rational punishment (e.g., antisocial punishment prevalence, error in punishment, learning/forgetting effects, social preference heterogeneity beyond basic selection intensity).
- **Temporal/distributional effects**: Long-run versus short-run efficiency, and distribution of payoffs within the group, are rarely distinguished.
- **Ambiguity where findings conflict**: Some models suggest over-punishment reduces efficiency, others report only positive or neutral effects, and theoretical assumptions may differ; predictions should retain this ambiguity.

---

**In summary**: The theoretical/simulation literature provides moderately strong, but **conditional and parameter-dependent**, support for the assertion that enabling peer punishment in well-designed public goods games generally increases efficiency. The size and direction of the effect depend critically on punishment effectiveness/cost, MPCR, group size, willingness to enforce, and institutional or behavioral moderators. Communication and display variables are underexplored. Where only cooperation rates are reported, predictions about efficiency should be treated with caution. Real-world behavioral and empirical validation remains an open need.
