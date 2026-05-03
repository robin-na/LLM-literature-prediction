# 1) Evidence Base

The literature set comprises 14 papers, spanning a mix of empirical experimental works (both lab and field), as well as several theoretical models. Theories are primarily focused on abstracted mechanisms of cooperation or punishment, while empirical studies often leverage laboratory public goods games (PGGs) or closely related social dilemmas. However, the breadth of direct relevance to the specific prediction task—predicting efficiency effects of enabling peer punishment in PGGs based on design dimensions plus control efficiency—is somewhat limited. Only a subset of papers covers all of: (1) a PGG or close variant, (2) explicit punishment or sanctions as a manipulable factor, and (3) efficiency or payoff-based outcomes as a primary endpoint. Many studies focus on behavioral outcomes (e.g., cooperation rates, punishment assigned) or on adjacent game forms and mechanisms (e.g., indirect reputation, neural modulation), rather than direct efficiency impacts of peer punishment in PGGs.

# 2) Task Relevance

**pgg_or_variant**:  
- **exact** relevance: Several papers explicitly use standard or linear PGGs (Greenwood et al., 2018; Micheli et al., 2021; Burton-Chellew & D'Amico, 2021; Morsky & Akçay, 2021; Liu et al., 2020; Chen et al., 2021; Li et al., 2018).
- **close/adjacent**: Field studies or models using CPR games, mutual-aid games, survivor’s dilemmas, or other n-player dilemmas offer context but are not design-identical (Gallier et al., 2018; Shimura & Nakamaru, 2018; Kayser & Lampert, 2021).

**punishment_or_sanctions**:  
- **exact**: Only few studies manipulate or systematically analyze explicit punishment as a treatment (Greenwood et al., 2018 [theory]; Chen et al., 2019 [PD with punishment]).
- **close/adjacent**: Other studies discuss punishment conceptually or analyze related incentive mechanisms (Micheli et al., 2021 with centralized punishments; Morsky & Akçay, 2021; Hernández, 2021), or focus on behavioral correlates (e.g., neural underpinnings of punishment tendencies).
- **none/weak**: Many empirical PGG studies in this set omit any punishment or reward condition.

**efficiency_or_related_payoff_outcome**:  
- **exact/close**: Efficiency or group payoff is a modeled primary outcome in a subset of theoretical works (Greenwood et al., 2018; Shimura & Nakamaru, 2018; Kayser & Lampert, 2021), but is largely unmeasured in empirical studies, which instead focus on cooperation/contribution rates.
- **adjacent/none**: Most lab experimental studies report only behavioral outcomes—not total or group efficiency.

**Summary**:  
Only a small subset of the literature base is fully *exactly* relevant across all three axes; most papers are weaker or only provide contextual or adjacent evidence for the specific prediction task.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes:**  
  - **Efficiency / Group Payoff / Welfare**: Theoretical works frequently model or discuss efficiency as the group payoff ratio compared to the maximum possible (Greenwood et al., 2018; Shimura & Nakamaru, 2018; Kayser & Lampert, 2021; Laird, 2018).
  - **Experimental Payoff Measurements**: Strikingly, empirical lab and field studies rarely report efficiency directly; their data generally focus on behavioral variables.

- **Non-Payoff Behavioral Outcomes:**  
  - **Contribution/Cooperation Rates**: What proportion or amount group members contribute is the most common outcome (Micheli et al., 2021; Burton-Chellew & D'Amico, 2021; Liu et al., 2020; Chen et al., 2021).
  - **Punishment Frequency/Assigned**: Some studies analyze how much or often punishment is used, or the effect of interventions (Chen et al., 2019).
  - **Normative Beliefs / Judgments**: Studies using tDCS or other neural manipulations assess shifts in perceived norms or expectations (Liu et al., 2020; Li et al., 2018).

**Distinction**: Most non-theoretical papers draw inferences about efficiency impacts only indirectly—through behavioral effects rather than measured payoffs.

# 4) Main Findings Relevant To Prediction

**Theoretical Insights:**
- **Conditional Effect of Punishment**: The effect of peer punishment on efficiency is strongly conditional—enabling punishment only increases group efficiency if enough punishers are present and certain cost/impact thresholds are met. Under sub-threshold conditions, punishment does not improve and may even reduce efficiency (Greenwood et al., 2018). Explicit formulas relate population composition and cost levels.
- **Centralized Incentives Parallel Peer Sanctions**: Centralized financial/sanction mechanisms robustly raise contribution rates, though efficiency effects are inferred but unmeasured (Micheli et al., 2021). There is no clear payoff distinction between reward and punishment treatments in this context.
- **Role of Social Information**: Exposing players to information about successful (i.e., high-earning) behaviors—without explicit punishment—can undermine cooperation, suggesting information regimes that highlight successful free-riding may lower efficiency (Burton-Chellew & D'Amico, 2021).
- **Game Structure Matters**: Larger groups and more rounds can support cooperation and higher efficiency in specific structures—notably mutual-aid and reputation-based games (Shimura & Nakamaru, 2018). However, these effects may not generalize to classic PGGs with peer punishment.

**Empirical Gaps:**
- Experimental studies overwhelmingly report non-payoff outcomes (mainly contribution rates), leaving open the translation to efficiency or net group payoff—especially after accounting for punishment costs, which may offset gains from higher cooperation.
- Very few empirical studies manipulate all relevant game dimensions or measure both control and treatment efficiency under enabled/disabled punishment.

# 5) Prediction Guidance

- **Condition Dependence**: Theory implies that simply enabling punishment is **not** a reliable way to increase efficiency; efficiency gains depend critically on punishment parameters (`punishment_cost`, `punishment_tech`, and implicitly, the social mix of punishers), as well as on game structure parameters such as `mpcr`, `all_or_nothing`, `player_count` (Greenwood et al., 2018).
- **Contribution-Behavior Inference**: Empirical studies provide indirect support that punishment or reward mechanisms increase cooperation rates, which is *generally* (but not infallibly) associated with higher efficiency—especially when punishment costs are low relative to defectors’ gains (Micheli et al., 2021).
- **Control Efficiency Anchor**: When the control game already achieves high efficiency (i.e., most players cooperate), the *marginal* benefit of enabling punishment may be small or even negative once direct and indirect costs are taken into account. Conversely, in low-efficiency controls, effective punishment regimes are more likely to generate net gains if a sufficient number of punishers exist and costs are not excessive.
- **Unmeasured Penalties**: The literature warns that punishment can, under some parameters, reduce net efficiency due to its direct costs, even if cooperation rates rise.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- `player_count`: Explicitly modeled in theory and reported in many experiments (Greenwood et al., 2018; Micheli et al., 2021; Shimura & Nakamaru, 2018).
- `num_rounds`: Addressed as a major determinant of repeated-game dynamics (Shimura & Nakamaru, 2018).
- `all_or_nothing`, `mpcr`: Key parameters controlling returns to cooperation; informed by both theory and experiment.
- `punishment_cost`, `punishment_tech`: Explored in theoretical works (mainly Greenwood et al., 2018), often missing or fixed in empirical studies.
- `chat`, `show_n_rounds`, `show_other_summaries`: Sometimes reported as background for context or moderating variables.
- `default_contrib`: Occasionally varied, but rarely analyzed as a primary determinant.

**Indirectly/Contextually Informed or Missing Dimensions:**
- `reward_exists`, `reward_cost`, `reward_tech`: Only addressed in studies that compare punishment and reward directly (Micheli et al., 2021), often absent otherwise.
- `show_punishment_id`: Not explicitly varied or analyzed as a primary factor in this literature set.
- **No paper in this set provides direct comparisons across the full multidimensional design space including all 14 predictors.**

# 7) Important Limitations

- **Gap Between Behavioral and Efficiency Outcomes**: The most consistent limitation is the lack of direct measurement or reporting of efficiency or group payoff in experimental studies. Most outcomes are behavioral proxies (cooperation, contributions), and the translation to net efficiency—after accounting for punishment costs—is assumed rather than established empirically.
- **Sparse Experimental Manipulation of Punishment Parameters**: While theory papers (e.g., Greenwood et al., 2018) model cost/impact tradeoffs for punishment, empirical studies typically use fixed or standard parameterizations, limiting the ability to empirically calibrate predictions across different punishment regimes.
- **Indirect Relevance**: Several studies use adjacent game structures, focus on neural/psychological mechanisms, or discuss punishment only at a theoretical or conceptual level. This limits their direct value for quantitative prediction.
- **Limited Coverage of Joint Dimension Effects**: No empirical study systematically varies multiple design dimensions in tandem (e.g., combining group size with punishment cost and visibility); most vary a single feature or context.
- **Ambiguity on Population Composition**: Theoretical work emphasizes that the outcome of enabling punishment is highly dependent on the prevalence of willing punishers in the population, a variable usually uncontrolled or unmeasured in experimental settings.
- **Limited Discussion of Practical Implementation**: Few papers consider issues of punishment implementation (`punishment_tech`), error, or information leakage that may substantially modify efficiency outcomes in real-world settings.

---

**Conclusion:**  
The paper set provides strong conceptual and theoretical insights on the *conditional* effect of punishment on efficiency in public-goods-game-like environments, with partial indirect empirical support from behavioral outcomes. Reliable quantitative prediction of average efficiency after enabling punishment, relative to control, requires careful modeling of key dimensions (especially punishment cost, impact, group composition, and existing efficiency levels)—but empirical data connecting these dimensions to actual efficiency outcomes in PGGs is sparse. This literature is best seen as generating hypotheses and interpretable constraints rather than as a source of direct empirical prediction estimates.
