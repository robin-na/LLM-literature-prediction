# 1) Evidence Base

The paper set is **broad and diverse**, comprising 104 papers including empirical lab experiments, observational studies, theory/simulation work, and hybrid mechanism/behavioral studies. Around **one-quarter** of the set provides *exact* or *close* coverage of standard public goods games (PGG) with explicit peer or institutional punishment and efficiency/payoff outcomes, giving solid, but not exhaustive, empirical and theoretical foundations for prediction. The remainder include adjacent dilemmas (e.g., trust game, prisoner's dilemma, collective risk dilemmas), focus on non-payoff behavioral outcomes (e.g., cooperation rate, punishment frequency), or address only proximal mechanisms or context.

Notably, the paper set includes:
- **Empirical lab experiments** with standard PGGs and systematic punishment manipulations (e.g., Lo Iacono et al., 2023; Salahshour et al., 2022; Molenmaker et al., 2023).
- **Agent-based and analytical theory** addressing institutional design and mechanistic moderators (e.g., Zefferman, 2023; Wang et al., 2024; Botta et al., 2024).
- **Simulation papers** that validate theory against known empirical patterns (e.g., Bühren et al., 2023).
- **Contextual or adjacent work** that either lacks standard PGG structure or does not directly report group efficiency outcomes.

This mix ensures strong, but parameter-specific, evidence for classic PGGs with peer punishment, while coverage is **sparser or more indirect** for some design feature combinations and non-standard environments.

# 2) Task Relevance

**pgg_or_variant**:  
- *Exact relevance*: A substantial subset of papers directly manipulates PGG design dimensions, especially repeated, multi-player linear PGGs.  
- *Close relevance*: A secondary stream covers threshold PGGs, common-pool resource dilemmas, or structured PGG variants (e.g., networked or spatial games).  
- *Adjacent/weak relevance*: Many papers involve Prisoner’s Dilemma, trust games, or other social dilemmas, often with analogical but not identical structure.  
- *None*: About 20-25% of the set (e.g., studies of dictator games, rule-following, etc.).

**punishment_or_sanctions**:  
- *Exact relevance*: Many studies test the effect of adding/removing *peer* or *institutional* punishment mechanisms, typically costly and with specified cost-to-impact ratios.  
- *Close/adjacent*: Others include alternative sanctions (e.g., exclusion, partner choice, reward, or third-party enforcement), or focus on psychological/informal mechanisms.  
- *Weak or none*: Some studies lack sanctions entirely or analyze only the correlates of punishment behavior.

**efficiency_or_related_payoff_outcome**:  
- *Exact relevance*: Less than half of the studies directly measure group efficiency (total payoff relative to the fully cooperative benchmark).  
- *Close*: Many report group earnings, total or average payoffs, or welfare, enabling loose mapping to efficiency.  
- *Adjacent/weak relevance*: A significant fraction only report contributions, cooperation rates, or punishment frequency—important moderators, but **not** efficiency outcomes.  
- *None*: Some papers focus exclusively on attitudinal, reputational, or emotional outcomes.

**Summary**:  
**Strongest direct relevance** for standard PGGs with peer punishment and explicit efficiency or group payoff outcomes, but **many papers provide only indirect or contextual evidence** due to lack of payoff measurement or deviation from canonical PGG structures.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes (efficiency, total group payoff, welfare):**  
- *Directly measured* in a limited subset, where experimental or theoretical work reports average profits in control and punishment-enabled conditions (e.g., Lo Iacono et al., 2023; Salahshour et al., 2022; Wang et al., 2024; Botta et al., 2024; Zefferman, 2023; Bühren et al., 2023).
- *Closely related*: Some report group earnings, tokens generated, net welfare, or surrogate efficiency metrics (e.g., DeCaro et al., 2024; Garrido et al., 2025; Chiba-Okabe & Plotkin, 2024).
- *Indirectly inferred*: Some simulations/theories allow back-calculation from reported strategy abundances or equilibria.

**Non-payoff behavioral outcomes (not efficiency):**  
- The majority measure *contribution rate*, *cooperation rate*, *punishment frequency/intensity*, *norm compliance*, or *punishment assignment*.
- Some explore *convergence*, *variance in cooperation*, or *dynamics of strategies*.
- Several focus on *mechanisms*: effects of communication, group heterogeneity, group structure, reputation, or facilitation.

It is **crucial** to distinguish:  
- *Payoff/efficiency* = what is directly relevant to the prediction task;  
- *Behavioral outcomes* = key moderators/explanatory factors, but **not** sufficient alone for efficiency-based predictions.

# 4) Main Findings Relevant To Prediction

**SYNTHESIS ACROSS EVIDENCE**

### a) Enabling punishment generally increases efficiency, but with major qualifications:
- **In canonical linear repeated PGGs**, enabling peer punishment robustly increases group efficiency (profits) relative to no-punishment baseline, though gains often emerge after initial rounds (Lo Iacono et al., 2023; Wang et al., 2024; Botta et al., 2024).
- **The positive effect is heavily parameter-dependent**:
  - **Punishment efficiency/cost**: High punishment cost, weak impact, or antisocial punishment (punishing cooperators) can reverse or nullify efficiency gains (Salahshour et al., 2022; Ozono & Nakama, 2022; Bühren et al., 2023).
  - **Group structure**: In uniform or homogenous groups, punishment is effective; in pluriform or heterogeneous groups, punishment may target dissimilar others, undermining efficiency (Molenmaker et al., 2023).
  - **Design and implementation**: Adaptive or probabilistic punishment may outperform fixed schemes (Ohdaira, 2022).
  - **Punishment *can* reduce efficiency if misapplied** (e.g., profitable punishment, antisocial punishment, or competitive/attack options): in such cases, efficiency may fall below control (Alam & Rai, 2025; Romano et al., 2024; Han et al., 2024).

### b) **Effect size is variable and moderated by control efficiency**
- If control efficiency is already high (due to social preferences, communication, or baseline cooperation), **marginal efficiency gains from punishment are smaller** or potentially negative (Zefferman, 2023; Lie-Panis et al., 2024).
- If control efficiency is low, well-calibrated punishment offers a larger gain but only if key design parameters (cost/benefit ratio, monitoring, group size) are favorable.

### c) **Institutional design, monitoring, and coordination are key modifiers**
- Facilitation of norm discussion or mediated institution choice can greatly magnify efficiency gains from punishment; uncoordinated or arbitrary punishment often fails (DeCaro et al., 2024; Botta et al., 2024).
- Monitoring and observability are essential: perfect monitoring amplifies benefits; noisy or incomplete monitoring can enable antisocial punishment or reduce efficiency (Salahshour et al., 2022; Zefferman, 2023).

### d) **Comparison to reward and other mechanisms**
- Reward can increase cooperation, but is often less efficient or more costly than well-designed punishment, though sometimes more effective at increasing social welfare depending on cost structures (Han, 2022; Han et al., 2024).
- Mixed or flexible institutions (punish/reward chosen by group) can outpace either punishment-only or reward-only designs (Garrido et al., 2025).

### e) **Findings are robust across empirical/theoretical studies when design dimensions are matched, but generalization is limited by lack of dimension-level variation in many papers.**
- Much theory provides *explicit conditions* (thresholds depending on player count, MPCR, punishment ratios, monitoring costs) for when efficiency gains are expected (Wang et al., 2024; Zefferman, 2023; Nirjhor & Nakamaru, 2023).

# 5) Prediction Guidance

**When predicting treatment efficiency (punishment enabled) given game design dimensions and control efficiency:**

- **Positive shifts in efficiency are most likely** when punishment is:
  - *Sufficiently cost-effective* (low cost, high impact per unit);
  - *Accurately and fairly targeted* (low antisocial/discriminatory use);
  - *Backed by perfect or high-quality monitoring*;
  - *Applied in relatively homogenous or coordinated groups*.

- **Marginal efficiency gains diminish** or even become negative when:
  - *Punishment cost is high* (relative to impact);
  - *Antisocial or discriminatory punishment is prevalent* (noise, heterogeneity, or ambiguous norms);
  - *Group size exceeds monitoring/coordination capacity* (Zefferman, 2023);
  - *Baseline control efficiency is already high*, making additional enforcement costly and unnecessary.

- **Control efficiency is a critical predictor/moderator**, but incomplete:  
  Models and empirical results stress that even with identical control efficiency, *variation in cost-to-impact ratio, group structure, monitoring, and information provision* can drastically alter the punishment effect.

- **Beware simple mappings from contribution to efficiency**:  
  Many papers report increased contributions as a result of punishment, but **payoff gains can be offset by punishment costs**—only studies that explicitly report efficiency or group payoff provide direct decision support.

- **Explicit threshold formulas and parameter dependence**:  
  Predictive use of theory should employ the reported thresholds/formulas for punishment effectiveness, cost, and group size under the game’s design parameters (Wang et al., 2024; Zefferman, 2023; Nirjhor & Nakamaru, 2023).

- **Mechanism/Context matters:**  
  Punishment via third-party, endogenous institution choice, or as part of a mixed punishment/reward institution demonstrates substantial moderating effects, sometimes enabling larger efficiency gains.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed by empirical/theory evidence:**
- **player_count**: Most studies fix group size (e.g., 4 or 12), a few vary it and model scaling effects explicitly (Lo Iacono et al., 2023; Zefferman, 2023; Wang et al., 2024).
- **num_rounds**: Standard, though often held constant; some theory considers effect of persistence/finite repetition.
- **mpcr**: Commonly reported and shown to interact with punishment effectiveness.
- **punishment_cost/punishment_tech**: Central to almost all mechanism-focused papers; cost-to-impact ratio repeatedly highlighted as a key moderator.
- **all_or_nothing**: Some studies and theories directly compare continuous vs. dichotomous choice impacts on outcomes.
- **show_other_summaries/show_punishment_id**: Feedback/transparency is highlighted as important for convergence and targeting (Nielsen & Pfattheicher, 2024).

**Indirectly or contextually discussed:**
- **chat**: Empirically measured in some (Lo Iacono et al., 2023; Nakagawa et al., 2022), indicated to increase baseline efficiency and sometimes moderate the effect of punishment.
- **group composition/heterogeneity** (not in base 14) is a strong moderator (Molenmaker et al., 2023) but only measured in select studies.
- **default_contrib**: Rarely manipulated.
- **show_n_rounds, show_other_summaries**: Sometimes included, with some evidence that feedback/summary presentation can affect targeting and norm enforcement.
- **reward_exists, reward_cost, reward_tech**: Some studies (esp. mixed-incentive or reward-vs-punishment comparisons) explore their interaction with punishment.

**Effectively missing or only referenced contextually:**
- **Dimension combinations**: Few studies systematically vary multiple design dimensions, limiting generalizability.
- **Other contextual features**: Ecological risk, real-world setting, and culture usually held constant or only discussed in adjacent frameworks.

# 7) Important Limitations

- **Limited multi-dimensional coverage**: Few papers systematically vary or test the *joint effect* of multiple prediction-relevant dimensions (apart from simulation studies assuming/exploring parameter sensitivity).
- **Design parameter lock-in**: Most high-quality papers hold core parameters constant (group size, MPCR, punishment cost), restricting predictive range to similar settings.
- **Behavioral outcome dominance**: Many studies report only contribution or punishment behavior—not group efficiency—making them only indirect sources for efficiency prediction.
- **Empirical-theoretical transfer gap**: Theoretical models are sometimes more generalizable (due to explicit formulas) but may abstract away psychological and group process intricacies (e.g., discrimination, antisocial punishment, institutional learning).
- **Population/sample and context specificity**: Several empirical studies are restricted to narrow samples (e.g., European university students, Japanese online workers), and effects may not generalize across cultures or field versus lab settings.
- **Adjacency and variant outcome focus**: While adjacent games (PD, trust, threshold dilemmas) offer context, transfer of findings on efficiency is not always direct.
- **Scarce direct evidence for many dimensions**: Some design features (e.g., chat, default contribution framing, reward-present designs, visibility of punishment identity) are rarely experimentally manipulated in conjunction with others, constraining dimension-level predictions.
- **Ambiguity and disagreement** remain: Not all studies agree on the sign or size of efficiency effects (e.g., under noise, group heterogeneity, profit motive for punishment, presence of attack/competitive options).
- **Mechanisms versus outcome divergence**: Mechanism-focused findings (e.g., effective monitoring, trust communication, institution-building) cannot always be mapped directly onto efficiency predictions without more granular outcome data.

---

### **In summary:**  
The literature provides robust, parameter-specific evidence that **enabling punishment in canonical PGGs increases efficiency when punishment is cost-effective, well-targeted, and institutional context is favorable**, but *major and quantifiable exceptions exist* depending on group composition, punishment structure, monitoring quality, and baseline efficiency. When making out-of-sample predictions, only those design dimensions and settings directly supported by payoff-based outcome studies should guide predictions, with the remainder offering qualitative or mechanistic caution rather than direct evidence. 

*Key papers for parameter-matched predictions include*: Lo Iacono et al. (2023), Salahshour et al. (2022), Molenmaker et al. (2023), Zefferman (2023), Wang et al. (2024), Botta et al. (2024), Bühren et al. (2023), and adjacent simulation/theory sources that provide explicit parameter thresholds for efficiency outcomes.
