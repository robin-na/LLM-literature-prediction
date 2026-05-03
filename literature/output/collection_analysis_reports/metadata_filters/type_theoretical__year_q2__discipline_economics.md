# 1) Evidence Base

The paper set consists of 42 items, all theoretical in nature—no empirical or experimental studies are included. The set is broad in its coverage of social dilemmas, repeated games, and public-goods-game-like environments, with a particular focus on formal models that analyze punishment (and sometimes reward) mechanisms and their impact on efficiency, cooperation, and norm enforcement. While many papers are exact fits to standard Public Goods Games (PGG), a substantial subset analyzes adjacent environments, including repeated Prisoner’s Dilemma, trust games, helping games, and mechanism design contexts. Coverage of design dimensions is broad, especially for key factors such as player count, marginal per-capita return (MPCR), punishment cost/technology, information structure, and sometimes chat or reward-related variables. However, consistent absence of empirical effect sizes and outcome data limits direct, quantitative prediction—findings are instead mechanism- and parameter-based, providing explicit boundaries and comparative statics within theoretical frameworks.

# 2) Task Relevance

**pgg_or_variant**:  
- *exact*: Several central papers present models for standard or linear PGGs, or direct variants (e.g., Levine & Modica, 2016; Wolitzky, 2013; Hwang, 2017).  
- *close*: Many analyze repeated games, trust games, and resource dilemmas with strong structural similarity to PGGs, but with different institutional details or heterogeneity (e.g., Camera & Gioffré, 2016; Chassang & Zehnder, 2016; Ali & Miller, 2016).  
- *adjacent*: Some focus on partner selection, group selection, or evolutionary models not fitting the canonical PGG setup.

**punishment_or_sanctions**:  
- *exact*: Most core papers focus specifically on peer (or community) punishment technologies, including cost structure, effectiveness, and coordination (e.g., Levine & Modica, 2016; Wolitzky, 2013; Olcina & Calabuig, 2015).  
- *close/adjacent*: Numerous models incorporate punishment as one of several enforcement tools (rewards, ostracism, exclusion) or discuss punishment adjacency (e.g., focusing on punishment-like strategies, endogenous exclusion, or norm enforcement).

**efficiency_or_related_payoff_outcome**:  
- *exact/close*: Many provide results directly on group efficiency, welfare, or total payoff under different enforcement regimes (e.g., Levine & Modica, 2016; Hwang, 2017; Buchholz et al., 2014; Chassang & Zehnder, 2016).  
- *adjacent*: Some focus on cooperation or norm compliance, inferring efficiency impacts but not quantifying them (e.g., Ogaki & Tanaka, 2017; Sylwester et al., 2013).  
- Notably, almost no paper offers direct empirical, quantitative evidence on efficiency deltas resulting from enabling punishment, nor do they systematically relate payoff findings to 'control efficiency' as in the stated prediction task.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes**:  
  - **Efficiency** (group payoff relative to social optimum) is frequently modeled, providing comparative statics and equilibrium boundaries (e.g., Levine & Modica, 2016; Wolitzky, 2013; Hwang, 2017).
  - **Total earnings/welfare/surplus** are outcome variables in many models (e.g., Buchholz et al., 2014; Richter et al., 2013; Laclau & Tomala, 2017).
- **Non-Payoff Behavioral Outcomes**:  
  - **Contribution/cooperation rates**, **punishment frequency**, and **norm compliance** are often endpoints, especially in models with social preferences or behavioral types (e.g., Ogaki & Tanaka, 2017; Thöni, 2014; Sylwester et al., 2013).
- **Mixed or Indirect Outcomes**:
  - Some studies infer efficiency from equilibrium cooperation, or discuss how certain strategies lead to efficiency improvements without explicit computation of group payoffs.
  - Papers that focus on evolutionary or group-level dynamics (e.g., Povey, 2014; Ognedal, 2016) consider both static and dynamic efficiency, sometimes finding trade-offs between immediate welfare gains and longer-run social composition.

# 4) Main Findings Relevant To Prediction

## Synthesis of Key Findings:

### (A) Enabling Peer Punishment Generally Increases Efficiency—But Not Universally
- **Empirical status**: Theoretical mechanisms only, with formulas and parameter boundaries; not empirically calibrated.
- **Core logic**: In standard or repeated public goods games, if punishment is available, not prohibitively costly, and sufficiently coordinated/effective, efficiency increases relative to a no-punishment baseline—even in large groups (Levine & Modica, 2016; Wolitzky, 2013; Hwang, 2017).
- **Supporting conditions**: Monitoring technology (perfect/imperfect), punishment cost and magnitude, and the existence of coordinated (grim trigger/contagious) strategies are central. Group size effects can be positive or negative depending on monitoring and punishment mechanisms.
- **Quantitative implications**: Many papers offer explicit boundaries and comparative statics (e.g., conditions on punishment cost, minimum effectiveness, or group patience required to sustain high efficiency).

### (B) Moderators and Limitations
- Incomplete or noisy monitoring, costly audits, or weakly coordinated punishment can prevent efficiency improvements (Wolitzky, 2013; Laclau & Tomala, 2017; Balmaceda & Escobar, 2017).
- The possibility of antisocial punishment, counter-punishment, or high rates of non-cooperative types can undermine or even reverse efficiency gains (Thöni, 2014; Sylwester et al., 2013; Noussair & van Soest, 2014).
- Game framing (all-or-nothing vs. continuous), communication (chat), and knowledge of game length or round structure (show_n_rounds) act as important moderators (Noussair & van Soest, 2014; Golman, 2016).

### (C) Reward, Exclusion, and Alternative Enforcement
- Reward-based or endogenous-exclusion mechanisms can achieve high efficiency in some social dilemma settings; sometimes as functionally effective as punishment if properly targeted (Greiff, 2013; Buchholz et al., 2014).
- In dynamic populations and evolutionary models, long-term efficiency may be reduced by punishment mechanisms that crowd out intrinsic motivation (Povey, 2014).

### (D) Parameter Sensitivities and Mechanism Arguments
- Efficacy of punishment rises with group patience (discount factor), monitoring reach, and punishment magnitude.
- Coordination among punishers is especially critical in larger groups (Hwang, 2017; Olcina & Calabuig, 2015).
- The structure of interaction (network, ranking, group identity) conditions whether punishment can sustain efficiency at all (Feinberg & Kets, 2014; Harbaugh & To, 2014).

### (E) Behavioral vs. Efficiency Outcomes
- Many studies highlight that higher cooperation/contribution rates via punishment do not always translate into higher efficiency, especially if punishment is costly or misdirected (e.g., antisocial punishment) (Thöni, 2014; Sylwester et al., 2013).

# 5) Prediction Guidance

Based on this literature, **enabling peer punishment in public-goods-game-like environments should be expected to increase efficiency relative to the control (punishment-disabled) game**, provided:
- **Punishment is not prohibitively costly** and can be delivered with sufficient effectiveness.
- **Monitoring/audit technology** enables detection of defections with reasonably high probability.
- **Coordination among punishers** is likely (e.g., sufficiently connected environments, or explicit trigger/threshold rules).
- **Antisocial punishment and retaliation are not dominant behavioral tendencies in the population or context.**

When these conditions are met, the theoretical models often provide explicit quantitative relationships (though actual parameter values must be set based on the game's parameters and not empirical regularities). For a task mapping from design dimensions plus control efficiency to punishment-enabled efficiency, the literature supports modeling:
- **Improvement in efficiency as a (nonlinear) function of punishment cost, magnitude, monitoring, and group size**, with upper bounds imposed by the quality of monitoring and possibility of antisocial punishment.
- **Contextual moderators** including communication/chat (increases efficiency independently), framing, and network structure.
- **Control efficiency**: If the control game already achieves high efficiency (e.g., via communication or stable cooperation), the marginal effect of enabling punishment may be minimal.

**Caveats**: When punishment is too costly or misapplied (e.g., antisocial, retaliatory, or targeting the wrong individuals), efficiency can be unchanged or even reduced, relative to control. Qualitative predictions should respect this ambiguity (Noussair & van Soest, 2014; Thöni, 2014).

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions**:  
- *player_count*: Well-covered; predictions about group size effects are explicit in many models.  
- *num_rounds*: Appears in many models; longer games and repeated interaction with high patience allow more effective punishment and higher efficiency.  
- *mpcr*: Central; numerous papers model outcomes as explicit functions of marginal returns to cooperation.  
- *punishment_cost*, *punishment_tech*: Very well covered; cost and effectiveness of punishment are critical thresholds for efficiency gains.  
- *all_or_nothing*: Modeled in both forms; design affects feasibility of cooperation/punishment.  
- *show_n_rounds*, *show_other_summaries*, *show_punishment_id*: Sometimes discussed as aspects of monitoring and information structure, important for prediction in specific network configurations.  
- *reward_exists*, *reward_cost*, *reward_tech*: Theoretical coverage in fewer papers, mostly in comparison or as alternative enforcement mechanisms (e.g., Greiff, 2013; Chassang & Zehnder, 2016).

**Indirectly Informed/Contextual Dimensions**:  
- *chat*: Mentioned, mainly as a strong independent moderator of efficiency (Noussair & van Soest, 2014), but not always parameterized.
- *default_contrib*: Contribution framing sometimes discussed as influencing baseline cooperation, rarely as a modeled parameter in efficiency predictions.
- *show_n_rounds*, *show_other_summaries*, and *show_punishment_id*: Explicitly modeled where monitoring/information structure is critical, otherwise contextually discussed.

**Effectively Missing**:  
- No empirical studies directly calibrate all 14 dimensions jointly, nor do any provide effect sizes for each parameter in combination.
- No direct empirical evidence links baseline control efficiency to average efficiency with punishment for arbitrary parameter profiles.

# 7) Important Limitations

- **Lack of Empirical Quantification**: All findings are theoretically derived; there are no lab or field experiments in this set providing real-world effect sizes or empirical validation of parameter sensitivities.
- **Adjacent Game Structures**: Many models abstract from standard linear PGGs—findings may not generalize directly to the canonical lab PGG or experimental treatments with explicit punishment.
- **Unmodeled Design Dimensions**: Several prediction dimensions are discussed only contextually or not at all (e.g., default contribution frame, communication/chat, identifiability of punishers), and therefore cannot be directly incorporated into quantitative predictive models from this literature alone.
- **Assumption Sensitivity**: The predicted effect of punishment on efficiency depends strongly on model specifics—effectiveness and cost of punishment, monitoring quality, degree of coordination, presence of antisocial punishment, and heterogeneity all act as critical moderators. Even small changes in parameterization or assumptions can shift qualitative predictions.
- **Absence of Dynamic Evolutionary Effects**: Some models (e.g., Povey, 2014) warn that punishment may undermine the evolution of intrinsic motivation for cooperation, thus reducing dynamic efficiency even if static welfare is higher.
- **Ambiguity Where Real-World Contexts Vary**: Cultural and social factors (e.g., prevalence of antisocial punishment or counter-punishment) are recognized as critical, but the theory provides only possible outcomes, not predictive probabilities.

---
**In sum:** The theoretical literature robustly supports the expectation that enabling peer punishment in public-goods-like environments increases average efficiency—provided the punishment technology is effective, punishment costs are not too high, monitoring is adequate, and coordination among punishers is feasible. However, efficiency gains are not guaranteed: antisocial punishment, costliness, and poor monitoring can nullify or even reverse the effect. The mapping from design dimensions and control efficiency to treatment efficiency is best informed by parameters relating to group size, rounds, MPCR, punishment cost and technology, and monitoring structure, but is not empirically quantified in this set. Predictions derived from these models should be seen as qualitative and mechanistic, not quantitative or empirically validated.
