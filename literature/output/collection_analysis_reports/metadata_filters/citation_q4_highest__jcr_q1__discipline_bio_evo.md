# 1) Evidence Base

The paper set comprises **92 papers**, providing a broad sweep of empirical and theoretical literature, with a heavy emphasis on **laboratory experiments, game-theoretic models, and field/observational studies**. Roughly half of the set are empirical lab experiments manipulating **public goods games (PGGs)** or closely related environments, with others providing field data, and the remainder comprising **theoretical or modeling work**.

This corpus includes numerous high-relevance empirical studies directly comparing efficiency in control (no punishment) versus peer-punishment-enabled PGGs, alongside a large body of theoretical modeling—some with explicit efficiency/earnings outcomes, others focusing on mechanisms, equilibria, or evolutionary stability. **Contextual and adjacent works** address effects in CPR (common-pool resource games), third-party punishment, and ecological/animal models, but most theoretical and some field studies are indirect for the core efficiency prediction task.

# 2) Task Relevance

Task relevance is assessed using the labeled axes:

- **pgg_or_variant**:
  - **Exact**: Majority of empirical and several theory/model papers use precise PGG designs or direct linear/nonlinear variants (e.g., Sääksvuori et al., 2011; Gächter et al., 2017; Egas & Riedl, 2008).
  - **Close/Adjacent**: Several studies use CPR or asymmetric games, third-party punishment, or institution-based sanctions—informative for mechanism but not always aligned with prediction task's design dimensions.
  - **Weak/None**: Many animal behavior, neuro, or broad evolutionary models do not operationalize PGGs.

- **punishment_or_sanctions**:
  - **Exact**: Extensive direct evidence from classic peer-punishment and pool-punishment PGG experiments, as well as institutional punishment or exclusion models.
  - **Close**: Some examine reward, social exclusion, group-imposed sanctions, or reputation instead of direct monetary punishment.
  - **Adjacent**: Norm enforcement, group exit, and policing sometimes discussed as analogues.

- **efficiency_or_related_payoff_outcome**:
  - **Exact/Close**: Several empirical and theory papers report **efficiency** (ratio of obtained vs. maximum payoff), group payoff/earnings, or closely related surplus/welfare (e.g., Gächter et al., 2017; Sääksvuori et al., 2011; O'Gorman et al., 2009). Others report mean earnings, group provisioning, or resource-level as close proxies.
  - **Adjacent/Weak**: A large subset only report **behavioral outcomes** (contribution/cooperation rates, punishment events), with inferences about efficiency made only indirectly or via theoretical payoff logic.
  - **None**: A few focus only on neural, motivational, or evolutionary mechanism.

**Overall:** There is substantial **direct and close evidence** on how peer punishment affects efficiency in public-goods-game-like environments, with nuanced theoretical and empirical coverage. The relevance is **highest** for studies explicitly reporting efficiency or total group payoff under PGG rules with varying punishment regimes.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (efficiency, group payoff, earnings, welfare, coins, surplus):**
  - Directly measured and reported in multiple key lab experiments (e.g., Gächter et al., 2017; Sääksvuori et al., 2011; O'Gorman et al., 2009; Egas & Riedl, 2008; Traulsen et al., 2012).
  - Also captured as **resource sustainability** or **mean provision** in CPR experiments (e.g., Vollan, 2008; Castillo et al., 2011).
  - Theoretical works often derive group efficiency results analytically or from simulation (e.g., Adami et al., 2016; Sasaki & Uchida, 2013).

- **Non-payoff behavioral outcomes (contribution rate, cooperation, norm compliance, punishment assigned, patient/impatient punishment, antisocial punishment):**
  - Ubiquitous, often the primary reported outcome (notably in theory, neuro/social cognition, and evolutionary studies).
  - Laboratory studies frequently use these behaviors to infer *probable* impacts on group payoff, but distinctions are sometimes blurred.
  - Some empirical studies explicitly note behavioral improvement (e.g., more cooperation) without payoff gains, due to punishment costs.

**Key distinction:** Several high-relevance sources demonstrate that **increased cooperation does not always yield higher efficiency**—punishment costs can cancel out gains from higher contributions, or even reduce overall group earnings.

# 4) Main Findings Relevant To Prediction

**Synthesis of cross-paper findings:**

- **Punishment usually increases cooperation, but efficiency gains are conditional.**
  - Most lab experiments show enabling (peer) punishment typically **arrests the decline in cooperation**, raising contributions closer to the social optimum.
  - **Efficiency (group payoff relative to social optimum) increases** only when punishment costs are *not excessive*, or when punishment is used sparingly after initial stabilization (Gächter et al., 2017; O'Gorman et al., 2009).
  - In many studies, the **group profit in punishment conditions remains below the social optimum** because punishment costs subtract from the gains (Egas & Riedl, 2008; Guala, 2012; Traulsen et al., 2012).

- **Critical moderators:**
  - **Punishment cost-to-impact ratio:** Low-cost, high-impact punishment is most effective at improving both cooperation and efficiency (Egas & Riedl, 2008; Traulsen et al., 2012). If punishment is too costly or ineffective, net efficiency does not improve—or even declines.
  - **Structure of punishment regime:** Centralized/designed punishment (single punisher), *coordinated* or *pool* punishment often yields higher efficiency than uncoordinated, diffuse peer-punishment due to reduced redundant punishment (O'Gorman et al., 2009).
  - **Group competition:** Intergroup competition can unlock large efficiency gains from punishment that are absent in isolated groups (Sääksvuori et al., 2011).
  - **Cultural and social context:** The same punishment mechanism can raise, have no effect, or reduce efficiency depending on **cultural background**, prevalence of antisocial punishment, or group self-determination (Gächter & Herrmann, 2009; Vollan, 2008).
  - **Reputation and information:** Availability of reputation signaling or observability can make punishment more efficient, allowing threat rather than frequent costly use (Milinski, 2016; dos Santos et al., 2011).
  - **Environmental and institutional context:** In CPRs or field experiments, externally imposed or low-legitimacy punishment institutions can **crowd out** cooperation, reducing efficiency; locally chosen or well-trusted rules tend to perform better (Vollan, 2008; Castillo et al., 2011).

- **Variants:**
  - **Pool (institutional) vs. Peer punishment:** Pool punishment, especially with second-order punishment, often **reduces efficiency more than peer punishment** due to higher, sustained costs, even while stabilizing cooperation (Traulsen et al., 2012).
  - **Social exclusion:** Models show social exclusion (punishment via exclusion from benefits) can vastly outperform costly punishment at raising efficiency—if exclusion is cheap and effective (Sasaki & Uchida, 2013).

- **Specific scenarios where punishment fails to improve efficiency:**
  - When **punishment is costly and coordination is lacking** (Guala, 2012).
  - When **antisocial punishment** (punishing cooperators) is prevalent due to group/cultural norms (Gächter & Herrmann, 2009).
  - In **field/CPR settings**, when external punishment is imposed without group buy-in or when group trust is high (Vollan, 2008; Castillo et al., 2011).
  - Where **resource ecological dynamics** preclude sustainable efficiency gains even with perfect cooperation (Chen & Szolnoki, 2018).
  - In presence of **bribery/corruption opportunities**, which can fully reverse the effect of punitive institutions (Muthukrishna et al., 2017).

# 5) Prediction Guidance

Given a set of design dimensions and control game efficiency:

- **Baseline expectation:** Enabling peer punishment in a PGG with "reasonable" parameters (moderate group size, repeated rounds, not extreme punishment cost) will generally **increase average efficiency** over control, **especially if baseline (control) efficiency is low due to free-riding** (Gächter et al., 2017; O'Gorman et al., 2009; Adami et al., 2016).

- **Magnitude and even direction of the effect are strongly conditional**:
  - **If control efficiency is already high** (due to, e.g., high MPCR, pre-existing trust, or other pro-social incentives), the marginal gain from adding punishment may be muted or negative (Egas & Riedl, 2008; Vollan, 2008).
  - **If punishment cost is high relative to its impact, or if there are multiple redundant punishers, efficiency can decrease** (Guala, 2012; Traulsen et al., 2012).
  - Efficiency **gains are maximized with low-cost/high-impact punishment**, group-legitimized sanction schemes, strong group competition, or pairing with reputation mechanisms.

- **Control efficiency is a strong, but not sufficient predictor** of treatment (punishment-enabled) efficiency. The effect size on efficiency depends on **key design moderators**, especially:
  - `punishment_cost`, `punishment_tech` (cost-to-impact ratio),
  - `player_count`, `num_rounds` (group size, repeated interaction),
  - presence of **group competition** or institutional features,
  - information (`show_other_summaries`, `show_punishment_id`),
  - cultural/group context (not always explicitly measured).

- **Prediction caution:** If game design includes institutional complexity (pool punishment, leader roles, bribery opportunity, external enforcement), or local conditions suggesting norm misalignment or low legitimacy, **don't assume positive efficiency gains** from enabling punishment. In such cases, punishment can leave efficiency unchanged or reduced versus control.

- **Efficiency gains from punishment are especially likely when:**
  - Control games have declining or low efficiency due to unchecked free-riding.
  - Punishment is **cheap and effective**, or is coordinated/centralized.
  - Group competition or **reputation systems** are also enabled.
  - Social/cultural context supports punishment as enforcement, not as antisocial sabotage.

- **Efficiency losses or null effects are more likely when:**
  - Punishment is **expensive, redundant, or imposed externally with no group support**.
  - Antisocial punishment is common, or cultural norms undermine cooperative punishment.
  - Ecological/resource constraints cap sustainable collective benefit.
  - Bribery, rent-seeking, or antisocial reward is possible.

# 6) Design Dimensions Highlighted Across Papers

- **Directly informed (with robust evidence):**
  - `player_count`, `num_rounds`: Multiple studies vary group size (3–8 common) and length (6–30 rounds), with both efficiency and behavioral outcomes reported.
  - `mpcr`: Key parameter; high/low MPCR affects baseline efficiency and the effect of punishment.
  - `punishment_cost`, `punishment_tech`: Core moderators in almost all high-relevance lab and theory papers.
  - `all_or_nothing`: Most studies report on binary (all-or-nothing) or continuous contributions; some model both cases.
  - `show_other_summaries`: Manipulated in various reputation/observability experiments.
  - `chat`: Less commonly manipulated, but evidence suggests communication (when present) raises efficiency, sometimes reducing need for punishment.
  - `reward_exists`, `reward_cost`, `reward_tech`: Smaller empirical base; most reward studies suggest rewards can substitute for or augment punishment, sometimes providing *greater* efficiency.

- **Indirectly informed:**
  - `default_contrib` (opt-in vs opt-out framing),
  - `show_n_rounds` (total rounds revealed or not),
  - `show_punishment_id` (punisher identity),
  - `punishment_magnitude`: Sometimes implies by cost-to-effect ratio.

- **Only contextually discussed / Sparse:**
  - **Institutional features**: Leader enforcement, group voting, bribery, external regulation, self-determination—discussed in field and theory papers with variable mapping to design dimensions.
  - **Cultural context/legitimacy/trust**: Known to critically moderate effects, but not standardized as a design dimension.

- **Missing or rarely addressed:**
  - Detailed exploration of secondary design interaction effects (e.g., explicit chat + punishment + reward interplay).
  - Comprehensive exploration of framing/manipulation effects beyond those outlined (e.g., specifics of punishment/reward *implementation* outside cost/benefit ratio).

# 7) Important Limitations

- **Generalizability Issues:**
  - Many lab studies use *student subjects*, artificial endowments, and repeated anonymous interaction—field and cross-cultural studies often show quite different effects.
  - **Cultural/contextual effects** (e.g., antisocial punishment, group trust, legitimacy) are powerful moderators **rarely captured by standard game design dimensions**.
  - **Institutional variations** (e.g., pool vs. peer punishment, exclusion rather than deduction, optional participation) can flip efficiency effects, yet are not always cleanly coded in standard dimensions.

- **Outcome specification:**
  - Many studies report only behavioral indicators (contributions, punishment rates) rather than explicit efficiency.
  - Inferences from behavior to payoff may be valid only under equilibrium, not in transition or with frequent costly punishment.

- **Ecological/Economic constraints:**
  - In CPR and real-world resource contexts, **resource growth rates, ecological dynamics, and legal environment** can limit the value of laboratory findings for real setting predictions.

- **Dimension Coverage:**
  - Some design dimensions, especially those involving information structure (`show_n_rounds`, `show_punishment_id`), are *underexplored* in terms of their interaction with punishment effects on efficiency.

- **Ambiguity and Disagreement:**
  - Direct conflicts exist: e.g., some lab and theory papers find punishment always reduces efficiency unless conditions are ideal; others report near-optimal efficiency with punishment under standard PGG parameters.
  - Null and negative results—where punishment fails or reduces efficiency—are context-specific but not rare.

- **Missing quantitative effect sizes:**
  - Most papers do not provide directly transferable quantitative estimates for the marginal effect of enabling punishment on efficiency as a function of all 14 design dimensions.
  - **Downstream predictions must rely on conditional/qualitative patterns** and proxies (e.g., impact of cost-to-effect ratio, baseline efficiency, group context), not formulaic transformation from control to punishment-enabled outcomes.

---

**In summary:**  
The literature—especially empirical lab PGGs—supports a nuanced, **conditional optimism** about the effect of peer punishment on efficiency: **punishment often improves efficiency over control in settings with low baseline cooperation, if punishment is not prohibitively costly, and if social/institutional context is supportive.** However, this effect is frequently **reversed or nullified by high punishment costs, lack of coordination, cultural disagreement on norms, or field-specific ecological constraints.** Design dimensions most tightly linked to predicting efficiency changes are group size, rounds, MPCR, punishment cost/tech, reputation/information, and the presence of competition. **Control efficiency provides context—but only in combination with these moderators can one predict efficiency under punishment with confidence.** Recognizing the limits of laboratory generalizability, contextual factors (trust, legitimacy, norm consensus) are also essential but not captured in standard dimensions.
