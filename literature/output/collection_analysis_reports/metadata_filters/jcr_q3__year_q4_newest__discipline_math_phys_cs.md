# 1) Evidence Base

The paper set consists almost entirely of theoretical, simulation, or agent-based modeling papers (n=21), with only one paper based on empirical multi-agent experimentation. Most papers use mathematical analysis, numerical simulation, or agent-based modeling to analyze evolutionary or strategic outcomes in social dilemmas similar to, but not always exactly matching, the standard public goods game (PGG). The set includes both narrow and broad coverage regarding structure—some papers model standard PGGs or close variants, while others focus on adjacent games such as the n-person Prisoner's Dilemma, indirect reciprocity, volunteer dilemmas, or related resource allocation games.

Empirical data from laboratory or field experiments is notably absent, with substantive analysis overwhelmingly theoretical or computational. The outcome measures reported vary, but there is substantial emphasis on cooperation rates (a non-payoff behavioral outcome), with fewer studies reporting direct efficiency or group payoff metrics. Mechanistic or parameterized predictions are common.

Overall, the paper set provides a rich theoretical context for the effect of punishment and related mechanisms in PGG-like environments, but empirical generalizability is limited. The breadth in modeling approaches provides a range of scenarios, but direct studies of experimental PGGs with measured efficiency as the outcome are scarce.

# 2) Task Relevance

## PGG or Variant

**Relevance**: The set provides a **mix of exact, close, and adjacent coverage**.
- Several papers model exact PGGs or standard variants, including group size, marginal per-capita return (MPCR), and continuous or all-or-nothing contributions (e.g., Guo et al., 2023; Du et al., 2023; Vinayak, 2025).
- Some cover **close variants** such as n-person Prisoner's Dilemmas, volunteer dilemmas, or games with group-structured population but not strict PGG payoff functions (Kurokawa, 2023; Fontanari & Santos, 2024; Cooney, 2025).
- **Adjacency** also includes spatial, agent-based, or multi-game environments with PGG-like strategic structure but differing technically from the canonical PGG setup (Lu & Wang, 2024; Murase, 2025).

## Punishment or Sanctions

**Relevance**: Nearly all papers **address punishment or sanctions directly or in close analogy**.
- Many papers model explicit punishment cost, magnitude, or mechanism—including both peer and institutional punishment, exclusion, or group-level sanctions (Guo et al., 2023; Du et al., 2023; Li et al., 2024; Vinayak, 2025; Cooney, 2025; Kurokawa, 2023).
- Some address adjacent institutional arrangements or analogs of punishment, like group extinction (Kroumi, 2025) or partner selection/ostracism (Lu & Wang, 2024).
- A minority focus on adjacent outcomes such as tag-based harming (Bruner & Smead, 2022) or environmental 'space' which can act as indirect punishment (Cheng & Meng, 2023).

## Efficiency or Related Payoff Outcome

**Relevance**: Evidence is more **limited for direct efficiency outcomes**.
- Only a subset of papers report **group efficiency or related payoff outcomes** (Duong et al., 2024; Vinayak, 2025; Cooney, 2025; Kurokawa, 2023; Murase, 2025; Dasgupta & Musolesi, 2025).
- Many papers report **cooperation rate, norm compliance, or strategy frequencies**, but not efficiency ratios or total group payoff (Guo et al., 2023; Du et al., 2023; Esmaeili et al., 2022; Li et al., 2024).
- A few papers connect increased cooperation rates to likely efficiency improvements, but without explicit mapping or outcome reporting.

In sum, the literature most directly speaks to the PGG or its close variants and the implementation of punishment/sanctions, while **direct coverage of group efficiency or payoff** is present but less common.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes (Primary for Prediction):**  
  - Group efficiency (total payoff as a fraction of the fully cooperative benchmark): reported in a minority of papers (Duong et al., 2024; Vinayak, 2025; Cooney, 2025; Kurokawa, 2023; Murase, 2025; Dasgupta & Musolesi, 2025; Kristensen et al., 2025 [for baseline]).
  - Total group payoff, welfare, surplus, or total earnings.
  - Phase diagrams or analytical formulas for long-run payoff/efficiency as a function of design parameters.

- **Non-Payoff Behavioral Outcomes:**  
  - Cooperation/contribution rates (majority outcome, e.g., Guo et al., 2023; Du et al., 2023; Li et al., 2024; Esmaeili et al., 2022).
  - Strategy frequencies (proportions of cooperators, punishers, defectors).
  - Norm compliance.
  - Psychological constructs like envy or perceived payoff (Gros, 2022; Hu & Du, 2023).

- **Other:**  
  - Some papers provide only qualitative or analytical results (equilibrium frequencies, evolutionary stability).
  - A small number consider phase transitions or thresholds (e.g., abrupt cooperation shifts; Esmaeili et al., 2022).

**Distinction:**  
Although high cooperation rates are often seen as preconditions for efficiency, these are not identical, especially when punishment cost is substantial or when cooperation is achieved at the expense of costly sanctions. The mapping from behavioral outcomes to efficiency is not always reported or transparent.

# 4) Main Findings Relevant To Prediction

## General Patterns

- **Punishment Mechanisms:**  
  - Punishment (including both peer and institutional forms) **can increase cooperation rates** robustly across a wide range of model variants, especially when combined with structural features like kin selection, spatial structure, or partner selection (Guo et al., 2023; Du et al., 2023; Li et al., 2024; Cooney, 2025; Dasgupta & Musolesi, 2025).
  - However, **increases in cooperation do not always translate to improved efficiency**: if punishment is costly and used frequently, the net group payoff can decrease, even as cooperation increases (Cooney, 2025; Kurokawa, 2023; Murase, 2025).
  - **Threshold effects**: Sufficiently strong punishment (relative to the incentive to defect) can create phase transitions from inefficient to efficient equilibria (Vinayak, 2025; Esmaeili et al., 2022; Hu & Du, 2023).

- **Moderating Role of Design Dimensions:**
  - **Punishment cost and magnitude**: Lower cost-to-impact ratios make punishment more likely to enhance efficiency; high cost undermines efficiency (Kurokawa, 2023; Cooney, 2025; Hu & Du, 2023).
  - **Population and group structure**: Small groups, kin structure, and group-level selection can increase the likelihood of efficient outcomes with punishment; as group size increases, efficiency gains from punishment diminish or reverse unless punishment is cheap or group-level effects are strong (Kristensen et al., 2025; Kurokawa, 2023; Kroumi, 2025).
  - **Detectability of defection:** When defection is hard to detect, punishment can be efficient by deterring rare but severe abuses (Murase, 2025).
  - **Type of punishment**: Direct, net-rewarding punishment is most efficient in some settings; third-party or combined punishment can reduce efficiency due to costly overuse, even if cooperation rates are higher (Dasgupta & Musolesi, 2025).
  - **Reward mechanisms**: Often modeled in tandem with punishment—mixed incentive schemes can be more efficient under certain cost structures (Duong et al., 2024; Vinayak, 2025).

- **Interaction with Control Efficiency:**  
  - Where **control efficiency is already high** (i.e., high baseline cooperation), enabling punishment often yields **little to no efficiency improvement** and may reduce group payoff if sanctions are overused (Murase, 2025; Kurokawa, 2023; Cooney, 2025).
  - When **control efficiency is low**, **enabling punishment can produce substantial efficiency gains, up to the fully cooperative benchmark** if parameters are favorable (Vinayak, 2025; Murase, 2025).
  - **Indirect or phase change mechanisms**: Some models indicate that punishment only produces a step improvement in efficiency if its parameters cross a threshold; otherwise, the effect is minimal (Vinayak, 2025; Esmaeili et al., 2022).

## Areas of Ambiguity/Disagreement

- Some models highlight **non-monotonicity**: beyond a certain point, increasing punishment magnitude or frequency harms efficiency due to escalating costs (Cooney, 2025; Kurokawa, 2023).
- **Empirical absence:** The lack of experimental studies in this set means these predictions have uncertain magnitude or real-world robustness.

# 5) Prediction Guidance

Based on the literature set, the following principles should inform prediction of average treatment efficiency in PGG-like environments with punishment enabled:

- **Effect size and direction depend on control efficiency:**  
  - If the baseline game (control, with punishment disabled) already achieves high efficiency, adding punishment is unlikely to further improve efficiency and may reduce it (punishment costs can outweigh gains).
  - If baseline efficiency is low (widespread defection), enabling punishment **can increase efficiency sharply**, especially if punishment is effective (low cost, high deterrence).

- **Key Moderators from Game Design:**
  - **Punishment cost and effectiveness:** Lower cost and higher effectiveness per unit increase the likelihood that punishment will boost efficiency.
  - **Group size (player_count):** Smaller groups or those with strong kin/group selection are more conducive to efficiency gains from punishment.
  - **Punishment technology/implementation** (punishment_tech): Peer, institutional, direct, or exclusion mechanisms have different impacts; peer punishment often relies on group structure or partner selection to be efficient.
  - **Reward mechanisms (reward_exists, reward_cost, reward_tech):** Mixed incentive regimes can enhance efficiency when punishment costs are nontrivial.

- **Dimensional Interactions:**
  - The combination of **mpcr**, **punishment_cost**, and **player_count** sets the incentive landscape; e.g., high synergy factors (mpcr), low punishment costs, and small group size predict more efficient punishment-enabled equilibria.
  - **Detectability of defection** and related technical dimensions (e.g., show_other_summaries, show_punishment_id) modulate the efficiency gains from punishment; hard-to-detect defection can make punishment essential for efficiency improvement.

- **Formulas and Frameworks:**  
  - Several papers (Cooney, 2025; Murase, 2025; Duong et al., 2024; Vinayak, 2025) provide analytic or numeric relationships linking efficiency outcomes to game parameters. These can be used as mechanistic priors or for model-based prediction.

- **Cautions:**  
  - High cooperation rates do not guarantee higher efficiency; large and/or frequent punishment can lower overall payoff.
  - There is no robust empirical estimate of typical effect size due to a lack of experimental data in this set.

# 6) Design Dimensions Highlighted Across Papers

## Directly Informed Dimensions

- **player_count**: Modeled or varied in most papers; critical for group dynamics and selection effects.
- **num_rounds**: Included in several papers as part of repeated or evolutionary games; affects stability and sustainability.
- **all_or_nothing**: Varied in both continuous and dichotomous contribution models.
- **mpcr**: Explicitly analyzed, especially as an 'enhancement factor' or synergy parameter; central to predictions of cooperation and efficiency.
- **punishment_cost**: Key moderator in most relevant models; often defined as cost per unit punishment.
- **punishment_tech**: Several papers distinguish between types of punishment (peer, third-party, institutional, exclusion, etc.).
- **reward_exists, reward_cost**: Sometimes included as co-moderators with punishment (Vinayak, 2025; Duong et al., 2024).

## Indirectly or Contextually Discussed Dimensions

- **default_contrib**: Rarely discussed; only indirectly via social or cognitive framing.
- **show_n_rounds, show_other_summaries, show_punishment_id**: Sometimes alluded to in terms of reputation visibility or information structure but not systematically manipulated.
- **chat**: Not discussed in this set; no direct evidence for or against.

## Effectively Missing Dimensions

- **default_contrib, chat**: Little to no discussion or modeling.
- **reward_tech**: Typically not differentiated beyond existence and cost.
- **show_n_rounds, show_other_summaries, show_punishment_id**: Used sparingly as variations in model parameters, but not comprehensively analyzed.

# 7) Important Limitations

- **Empirical generalizability is weak:** Nearly all findings are theoretical or simulated; real-world behavioral and contextual factors are untested in this literature set.
- **Efficiency is inconsistently reported:** Many studies focus on behavioral outcomes (cooperation rate) without mapping to group efficiency or payoff, complicating direct quantitative prediction.
- **Limited coverage of dimension interactions:** While several design dimensions are modeled, their combinatorial or interactive effects (e.g., group size × punishment cost) are rarely mapped out exhaustively or empirically calibrated.
- **Neglect of some prediction dimensions:** Key features such as communication (chat), framing (default_contrib), and real-time information displays (show_* settings) are largely missing from analysis.
- **Potential non-monotonic effects and thresholds:** The models suggest nonlinear and context-dependent effects of punishment on efficiency, leading to ambiguity for 'realistic' parameter settings and practical application.
- **No direct evidence for time-course or dynamic adaptation:** Most predictions are equilibrium-based or long-run averages rather than transient, round-by-round effects.
- **No systematic treatment of heterogeneity or demographic stochasticity:** Individual variation, learning, or adaptive behavior are under-explored, with most models assuming homogeneity or fixed parameter distributions.

**In conclusion**, while this literature set is theoretically strong and provides a detailed mechanistic understanding of the conditions under which punishment might increase, decrease, or have no effect on group efficiency in PGG-like games, it is limited by its lack of empirical data, incomplete coverage of all design dimensions, and its reliance on equilibrium or average-outcome metrics. Predictions made using this literature should be seen as mechanistic priors subject to significant empirical uncertainty.
