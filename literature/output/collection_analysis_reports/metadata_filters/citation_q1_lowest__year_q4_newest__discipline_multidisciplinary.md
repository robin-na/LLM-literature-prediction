# 1) Evidence Base

The paper set includes a substantial number (60) of empirical and theoretical studies, with a strong representation of both lab experiments and formal models. For the downstream prediction task—estimating the effect of enabling peer punishment on efficiency in repeated public goods games (PGGs) as a function of game design and control efficiency—the coverage is broad in terms of variant games and mechanisms. However, there is a sharp drop in direct relevance when it comes to papers that precisely analyze *efficiency* (total group payoff as a ratio to the full-cooperation optimum) as the main outcome. Many empirical papers focus on behavioral outcomes (contribution rates, punishment frequency), while multiple theory/modeling papers do directly analyze efficiency or closely related payoff metrics. Overall, the set is relatively strong for mechanism understanding and dimensions like punishment cost/tech, but sparse for direct, empirical, payoff-based efficiency outcomes in canonical PGGs with and without punishment.

# 2) Task Relevance

**a. `pgg_or_variant`**
- **Exact Relevance:** There is a solid core of papers with exact PGG relevance, both experimental and theoretical (e.g., Molenmaker et al., 2023; Bühren et al., 2023; Zefferman, 2023; Botta et al., 2024; Nakagawa et al., 2022).
- **Close/Adjacent/Weak:** Additional papers cover games adjacent to PGGs, such as trust games, threshold PGGs, division-of-labor games, and common-pool resource models, offering potentially transferable insights. Some are close but not canonical PGGs (e.g., Mohlin et al., 2023; Chiba-Okabe & Plotkin, 2024).

**b. `punishment_or_sanctions`**
- **Exact Relevance:** Many papers directly manipulate, introduce, or model peer punishment (e.g. Molenmaker et al., 2023; Zefferman, 2023; Bühren et al., 2023; Botta et al., 2024). Several studies also examine variations (third-party/institutional punishment, discriminatory or antisocial punishment, profit-motivated punishment).
- **Close/Adjacent/Weak:** Some works focus on sanction mechanisms outside peer punishment (e.g., rewards, recommendations, reputation), or discuss indirect sanctions (e.g. social exclusion, reputation-based enforcement).

**c. `efficiency_or_related_payoff_outcome`**
- **Exact/Close:** There is a core of theory and simulation papers analyzing efficiency (group payoff relative to the optimum) as a main outcome (e.g., Bühren et al., 2023; Botta et al., 2024; Zefferman, 2023; DeCaro et al., 2024; Mohlin et al., 2023; Chiba-Okabe & Plotkin, 2024; Nirjhor & Nakamaru, 2023). Some empirical studies also extract group earnings.
- **Adjacent/Weak:** Many empirical papers are contribution-focused, only adjacently addressing payoff/efficiency, with welfare/total payment sometimes mentioned in a secondary way.
- **None:** Several behaviorally focused papers give no efficiency or group payoff outcome.

# 3) Outcomes Measured In The Literature

**Payoff-Based Outcomes (Relevant to Efficiency):**
- *Efficiency* (group payoff as % of full cooperation): Directly analyzed in a subset of theory/simulation/modeling studies and a smaller number of lab experiments.
- *Group payoff/total earnings/welfare/surplus:* Occasionally reported, more frequently in theory papers and some experiments (e.g., DeCaro et al., 2024; Bühren et al., 2023; Garrido et al., 2025; Nirjhor & Nakamaru, 2023).
- *Market size, accumulated wealth, tokens harvested, resource level*: These are closely related, appearing especially in common-pool resource and risk dilemma models.

**Non-Payoff Behavioral Outcomes:**
- *Contribution or cooperation rate:* The most commonly reported outcome in empirical PGG research.
- *Punishment frequency/magnitude/strategy, convergence in cooperation, trust, social preference type, rejection, partner switching, norm compliance, etc.*: Multiple papers focus on these and discuss mechanisms, but these outcomes are not efficiency measures.

**Separation:** While behavioral outcomes often (but not uniformly) correlate with changes in group payoff, only studies reporting group-level payoff/efficiency, net of punishment costs, provide direct prediction evidence for the downstream efficiency task.

# 4) Main Findings Relevant To Prediction

**Empirical and Theory Papers Focused on Efficiency:**
- **Punishment increases efficiency**—but only under specific conditions:
    - *Uniform, homogenous groups*: Peer punishment increases group payoff and efficiency (Molenmaker et al., 2023).
    - *Group composition/heterogeneity matters*: In pluriform groups, punishment can be discriminatory and undermine efficiency—sometimes reducing it below the baseline (Molenmaker et al., 2023).
    - *Punishment must be efficient*: If punishment is low-cost and high-impact, efficiency increases; if punishment is costly, gains disappear or reverse (Zefferman, 2023; Bühren et al., 2023; Mohlin et al., 2023).
    - *Facilitation and learning matter*: Coordinated, facilitated groups with communication and structured punishment get the highest efficiency (DeCaro et al., 2024).
    - *Institution type and flexibility*: Institutions that can implement both punishment and rewards, or can adapt to local conditions, outperform fixed punishment-only or reward-only mechanisms (Garrido et al., 2025; Zhou et al., 2022).

- **Punishment can reduce efficiency:**
    - *Discriminatory punishment/pluriformity*: Out-group punishment, antisocial punishment, or profit-motivated punishment can reduce or even reverse gains (Molenmaker et al., 2023; Alam & Rai, 2025; García & Traulsen, 2025).
    - *Profitable punishment*: When punishers earn from punishing, this can destabilize cooperation and lower welfare (Alam & Rai, 2025).
    - *Costly, inefficient, or poorly targeted punishment*: If punishment costs are too high or effectiveness is too low, efficiency does not improve (Bühren et al., 2023; Zefferman, 2023; Mohlin et al., 2023).

- **Non-payoff findings supporting/moderating efficiency:**
    - *Most empirical studies document increases in contribution rates when punishment is enabled* (Nakagawa et al., 2022; Makovi et al., 2025), but the translation to efficiency is ambiguous, especially when costs of punishment are high or punishment is frequent but ineffective.
    - *Heterogeneity in effects*: Variation by social preference composition, institutional context, punishment/reward calibration, and group structure.

- **Control (baseline) efficiency matters**: As a rule, the higher the baseline efficiency without punishment, the smaller the potential gain from enabling punishment, and vice versa. In some models, enabling punishment can push very low baseline efficiency up toward the social optimum, but only when institutional parameters are favorable.

# 5) Prediction Guidance

**Key implications for predicting treatment efficiency:**
- **Punishment Effect Is Conditional:** Punishment is most likely to increase efficiency when:
    - Groups are homogenous/uniform
    - Punishment is cheap and highly effective (high punishment magnitude/low cost ratio)
    - Behavioral norms support targeting defectors and not out-group members
    - The baseline (control) efficiency is low
    - Institutions are able to flexibly coordinate, and communication/facilitation is present

- **Punishment Effect Can Be Neutral or Negative:**
    - In heterogeneous groups, with discriminatory, antisocial, or profit-motivated punishment, or when costs are high, punishment can diminish efficiency relative to control
    - If baseline efficiency is already high, adding punishment may not increase (and can even decrease) total payoffs due to the additional costs

- **Behavioral Outcomes Are Not Enough:** Increases in contribution rates do not guarantee efficiency gains—punishment costs must be included. High punishment frequencies with high costs can crowd out efficiency gains.

- **Dimension-Specific Moderation:**
    - *punishment_cost, punishment_tech (efficiency), player_count, group structure/composition*, and *information about others* (identity, full monitoring) show the largest and most direct effect on whether punishment raises, leaves unchanged, or lowers efficiency.
    - Contextual factors such as *facilitation, communication, prior experience with punishment, group learning*, and whether *punishment is from own endowment or a common pool* further moderate effects.

- **Direction and Magnitude Depend on Game Design:** Efficient, well-calibrated punishment in homogenous, small to medium groups is most likely to yield high efficiency improvements; costly, misdirected, or profit-driven punishment in heterogeneous or poorly coordinated groups is likely to yield small or even negative effects on efficiency.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**
- `player_count`: Group size is a robust moderator (Zefferman, 2023; Nirjhor & Nakamaru, 2023).
- `num_rounds`: Relevant in most repeated PGG models, affecting learning and decay.
- `chat`: Communication/facilitation increases efficacy of punishment (DeCaro et al., 2024; Nakagawa et al., 2022).
- `all_or_nothing`: Both binary and continuous PGGs covered—punishment effects persist but may differ in magnitude.
- `mpcr`: MPCR directly moderates the gains from cooperation and potential efficiency (Bühren et al., 2023).
- `punishment_cost`: Core driver of efficiency gains (Zefferman, 2023; Bühren et al., 2023; Mohlin et al., 2023).
- `punishment_tech`: Who, how, and with what effectiveness punishment is implemented is crucial (Botta et al., 2024; Mohlin et al., 2023).
- `reward_exists`: Models with both reward and punishment show that mixed institutions can yield higher efficiency than single-mechanism institutions (Garrido et al., 2025; Zhou et al., 2022).

**Indirectly Informed/Contextually Discussed:**
- `show_other_summaries`, `show_n_rounds`, `default_contrib`, `show_punishment_id`: Occasionally manipulated, influence monitoring and information structure, and thus the potential effectiveness of punishment (Molenmaker et al., 2023; Nielsen & Pfattheicher, 2024).
- `reward_cost`, `reward_tech`: Present in a subset of papers including mixed-incentive institution models.

**Effectively Missing:**
- Calibrated, systematic evidence on the interaction of *default_contrib* and punishment, specific effects of *show_punishment_id*, and nuanced breakdowns for multi-dimensional moderation (e.g., simultaneous effects of chat, identity transparency, and punishment cost) are sparse.
- Experimental evidence on the parametric effects of some dimensions (e.g., interaction effects between reward and punishment costs, or all nuanced variants of *chat* and *summary display*) is limited.

# 7) Important Limitations

- **Empirical Payoff-Based Data Scarce:** There is a paucity of high-powered lab experiments reporting *efficiency* as the main dependent variable. Many studies focus on contributions, with only indirect or incomplete inference about payoffs after punishment costs.
- **Behavioral vs. Payoff-Based Outcomes:** Many findings are about contribution/cooperation rates, not group earnings or efficiency. These are not equivalent; a design that increases contributions but generates costly or misdirected punishment (e.g., antisocial or profit-driven punishment) can lower efficiency.
- **Group Structure Under-Modeled:** Empirical work underrepresents the impact of group heterogeneity, identity salience, and demographic mixing, despite evidence that these strongly moderate punishment effects (Molenmaker et al., 2023).
- **Variants and Parameter Heterogeneity:** Many findings are model- or context-specific (e.g., third-party vs. peer punishment, binary vs. continuous contributions, risk-based or threshold PGGs), which may or may not transfer to the exact structure of the target game.
- **Sparse Evidence on Certain Dimensions:** Several prediction-relevant design dimensions (especially `default_contrib`, `show_punishment_id`, fine-tuned institution mixing, and dynamic adaptation in repeated play) lack systematic experimental analysis.
- **Non-Linearities and Thresholds:** Many models demonstrate sharp thresholds (e.g., minimum punishment efficiency, critical risk) without empirical mapping of where real-world group contexts lie relative to these thresholds.
- **Overrepresentation of Positive Results in Theory:** Theoretical analyses frequently show large gains from punishment under idealized conditions—real-world complexity, noise, discrimination, and learning subtleties can reduce these effects.
- **Missing Real-World Heterogeneities:** Limited evidence on the effects of cultural background, personality, or prior learning—in practice these may make punishment much less predictable in impact than the canonical models suggest.

---

**In summary**: The literature provides robust theoretical basis, moderate empirical support, and strong mechanism insight for predicting that, in canonical public goods games, enabling punishment can increase group efficiency *when punishment is cheap, fairly applied, and well-targeted*. The effect is dramatically moderated by group composition, punishment cost/technology, and institutional structure. Predictors based solely on control efficiency and standard design dimensions may misestimate treatment efficiency if they ignore key moderators such as group heterogeneity, discrimination, misaligned punishment incentives, or the capacity for coordination/facilitation. The evidence base is strongest for the role of punishment cost/efficiency, group size/composition, and the structure of sanctioning institutions; weaker for design details like default contribution framing and identity transparency. Predictions should be made cautiously, incorporating these moderators and avoiding over-reliance on behavioral proxies for efficiency.
