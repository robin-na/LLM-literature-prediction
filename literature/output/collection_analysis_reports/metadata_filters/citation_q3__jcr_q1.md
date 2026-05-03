# 1) Evidence Base

The paper set is both wide-ranging and deep: it contains 382 papers, including a substantial mix of empirical laboratory experiments, field experiments, and theoretical/simulation studies. There is a strong representation of public goods games (PGGs) and close variants, with many studies directly manipulating punishment/sanctioning mechanisms and measuring efficiency or closely related payoff outcomes. Many papers offer direct, high-relevance empirical comparisons between control (punishment off) and treatment (punishment on) conditions, while others provide theoretical models mapping design parameters to efficiency outcomes. A notable strength is the diversity of punishment mechanisms studied (peer, centralized, institutional, exclusion, graded, asymmetric power, etc.), and the inclusion of moderators (e.g., information structure, group size, heterogeneity, error, retaliation, reward mechanisms). Some papers focus strictly on behavioral measures (contribution rates, cooperation) or on mechanisms and context (norms, emotion, culture) and do not report efficiency, but this is clearly marked in their summaries.

# 2) Task Relevance

**a. PGG or Variant**:  
- The great majority of the core papers are labeled as `pgg=exact`, focusing on canonical public goods games or very close variants (threshold PGG, snowdrift game, common pool resource games).
- Relevant adjacent environments (e.g., repeated prisoner's dilemmas, trust and ultimatum games with punishment, resource management games, pairwise cooperation with punishment) are classified as `pgg=close` or `pgg=adjacent` and are generally used with caution in synthesis.
- A minority of papers (especially in theory/sociology/neuroscience) are `pgg=none` and do not inform the prediction task.

**b. Punishment or Sanctions**:  
- There are numerous studies with `punishment=exact` relevance, including detailed manipulations of costly peer punishment, centralized punishment, pool punishment, exclusion, and reputational or indirect punishment. Some directly compare types (peer vs. centralized, etc.).
- Many papers also investigate `punishment=close` (social exclusion as punishment, partner choice), or discuss adjacent mechanisms (reputation/gossip/ostracism, reward vs. punishment) where the main focus is not literal costly punishment but related social or behavioral enforcement.

**c. Efficiency or Related Payoff Outcomes**:
- Many of the most informative papers are labeled `payoff=exact` or `payoff=close`, reporting efficiency as defined for the prediction task (total group payoff as a proportion of the full-cooperation maximum) or closely related measures (group earnings, welfare, total coins, surplus).
- A significant fraction measure only behavioral outcomes (contribution/cooperation rates, punishment frequency), clearly marked as non-payoff-focused.
- Several theoretical and simulation papers provide phase diagrams, regime mappings, or explicit efficiency formulas, while others give only qualitative or directional guidance or focus on distribution (inequality) or stability of cooperation rather than overall efficiency.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes (directly relevant for prediction):**
- Average efficiency (group payoff / maximum possible)
- Group earnings, total coins/payoff, welfare, surplus generated.
- Explicit comparison of efficiency under control (no punishment) vs. treatment (punishment enabled).
- Some report phase transitions or critical thresholds for efficiency gains or losses.

**Non-payoff behavioral outcomes (only indirect evidence):**
- Contribution rates, cooperation rates, prevalence/frequency of cooperation/defection/punishment.
- Norm compliance, behavioral types, strategy distributions.
- Retaliation, anti-social punishment, cycles of vendetta.
- Punishment/reward frequency, preferences for action, emotional drivers (anger, fairness).

**Other outcomes:**
- Inequality (Gini coefficient, payoff dispersion), satisfaction, legitimacy, norm internalization.
- Institutional choice, voting for punishment mechanisms.
- Reputation, trust, leader selection, strategy observation.

**Distinctions**: Many papers note that an increase in cooperation or contribution rates does not guarantee an increase in efficiency, especially when punishment costs are high, antisocial punishment occurs, or retaliation cycles result.

# 4) Main Findings Relevant To Prediction

**General Patterns:**
- **Punishment increases cooperation/contributions** almost universally (when measured), but **does not always increase efficiency**: the cost of punishment can offset or even outweigh gains from increased cooperation.
- **Punishment is most likely to improve efficiency when**:
    - The baseline (control) efficiency is low (cooperation is rare).
    - Punishment is effective (high fine-to-cost ratio) and well-calibrated.
    - Retaliation is prevented, antisocial punishment is minimized.
    - There is sufficient deterrence without excessive use (punishment is rarely actually applied).
    - The information environment is rich (low noise, accurate target identification).
    - Institutional (centralized, leader-driven, or voted) punishment structures are in place, especially with prosocial leaders.
- **Punishment may not improve (or can reduce) efficiency when**:
    - Control (baseline) efficiency is already high; the extra cost of implementing punishment outweighs marginal gains in cooperation.
    - Punishment is expensive (high cost/low impact); cycles of retaliation or vendettas occur.
    - Judicial error, inaccuracy, or misapplication (punishing cooperators) is present.
    - Antisocial punishment (punishing high contributors or prosocials) is common.
    - Cultural or institutional context crowds out the positive effect (e.g., imposed strong punishment in presence of possibility of corruption or low trust).
    - Alternative defection options exist or social expectations are low; punishment fails to coordinate trust.
    - Group heterogeneity (especially in returns or harmed minorities) undermines effectiveness.
- **Reward mechanisms are often more efficient than punishment** in both theory and experiment, especially when punishment invites retaliation, is costly, or is prone to error or antisocial use.
- **Exclusion, reputation-based sanctions, or costless social/moral judgments** can sometimes achieve efficiency gains without the overhead of costly material punishment, and in some designs, out-perform punishment.
- **Structural moderators** (group size, number of rounds, matching protocol, availability of communication, summary/feedback, information visibility, network structure) are repeatedly found to shape whether punishment increases efficiency and by how much.
- **Leadership and authority structure** (central vs. peer punishment, legitimacy, leader's prosociality) play a major role, as do the presence of commitment/voting and endogenous institution formation stages.

# 5) Prediction Guidance

Based on the synthesized literature:

- **Prediction of treatment efficiency (punishment-enabled), given design dimensions and baseline efficiency**, must consider critical moderators identified in the literature:
    - **Baseline (control) efficiency**: If the game without punishment already sustains high efficiency (contributions near optimal), adding costly punishment may reduce efficiency via its cost. Conversely, if baseline efficiency is low, punishment—if effective—can provide a clear gain.
    - **Punishment cost and impact (punishment_cost, punishment_tech, punishment_magnitude)**: Higher efficiency gains are likely when the fine-to-cost ratio is high, and when punishment is rarely (but credibly) used to deter rather than frequently used, which incurs high cost.
    - **Type of punishment**: Peer punishment can often reduce efficiency by creating cycles of retaliation or wasteful vendettas, especially in small, repeated games; institutional/centralized punishment, or punishment by designated leaders, especially prosocial ones, tends to be less wasteful and more net efficient.
    - **Antisocial punishment and error**: The presence of antisocial punishment or judicial error (punishing cooperators) typically reduces or negates efficiency gains.
    - **Information environment**: When contribution and punishment histories are accurately known, efficiency gains from punishment are higher. With noisy feedback or ambiguity, efficiency gains are reduced or reversed.
    - **Group size (player_count) and structure**: Larger groups may see declining marginal efficiency gains from punishment unless institutional enforcement is present; centralized or coordinated punishment structures help sustain efficiency at larger scale.
    - **Matching structure and rounds (num_rounds)**: Longer games and stable group composition (partner vs. random) facilitate learning and norm establishment, generally increasing the long-run efficiency benefit of punishment.
    - **Other interventions (reward_exists, reward_cost, chat, show_other_summaries)**: The addition of communication, rewards, or moral judgment opportunities can, in some settings, achieve equal or greater efficiency gains at lower cost.
    - **Cultural/contextual factors (chat, leadership legitimacy, group heterogeneity)**: Cultural norms, legitimacy of authority or punishment, and heterogeneity in player returns or endowments can strongly moderate the effect.
- **Use control efficiency as an anchor**: Empirical papers frequently compare efficiencies with and without punishment, often showing little or no increase, or even a decrease in efficiency with the introduction of costly peer punishment in already cooperative contexts, but substantial improvements when baseline efficiency is low.
- **Beware non-payoff behavioral evidence**: High rates of increased cooperation or punishment are not in themselves evidence of increased efficiency; the net cost of enforcement and side effects must be considered.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions** (i.e., with substantial, quantitative, and/or comparative evidence in multiple papers):
- `player_count` (group size): Extensively analyzed; efficiency effect of punishment modulated by group size.
- `num_rounds`: Number of rounds and repeated interaction strongly affects long-run punishment impacts.
- `mpcr`: The per-capita return is a key moderator: lower baseline efficiency makes punishment more likely to increase efficiency.
- `punishment_cost`, `punishment_magnitude`, `punishment_tech`: Many studies explicitly vary these and report effects on efficiency.
- `punishment_exists`, `reward_exists`: Numerously and precisely manipulated; joint effects discussed.
- `all_or_nothing` (binary vs. continuous contribution): Some direct treatment, especially with step-level or threshold games.
- `chat` (communication): Frequently studied as a moderator of both baseline efficiency and the marginal effect of punishment.
- `show_other_summaries`, `show_n_rounds`: Feedback and transparency about contributions and group progress are common experimental treatments.
- `show_punishment_id`: Identity visibility of punishers and punishment assignment is covered in studies of retaliation, reputation, and coordination.

**Indirectly informed** (mentioned, or manipulated in a limited subset of studies, with partial or qualitative evidence):
- `default_contrib`: Framing (opt-in vs opt-out) is included in some studies of defaults and social context.
- `reward_cost`, `reward_tech`: Sometimes directly compared to punishment cost/tech, sometimes only contextually.
- `reward_magnitude`: Discussed mainly in reward vs. punishment comparison studies.

**Contextually discussed or weakly treated** (mentioned as relevant but not addressed with quantitative evidence for efficiency outcomes):
- Group heterogeneity (endowment asymmetry, marginal return differences).
- Identification and network structure nuances (beyond standard design dimensions).
- Enforcement legitimacy, cultural context, or norm congruence.

**Effectively missing or uncalibrated**:
- Some intersectional dimensions (e.g., chat combined with punishment, opt-out default combined with exclusion).
- Many studies in the adjacent game categories discuss mechanisms or behavioral outcomes but lack data linking specific design dimensions to efficiency in the presence/absence of punishment.

# 7) Important Limitations

- **Non-payoff outcomes**: A sizable proportion of papers measure only behavioral outcomes, making mapping to efficiency speculative in those cases.
- **Ambiguity/disagreement**: There is no consensus on the net effect of punishment on efficiency—empirical and theoretical findings conflict depending on the parameter regime (punishment cost, baseline efficiency, antisocial punishment, error/noise, group size, etc.).
- **Empirical data is strongly context-dependent**: Variation in specific game designs (player count, MPCR, matching, information, etc.) leads to different qualitative and quantitative effects of punishment. Generalizing across contexts is risky.
- **Underexplored/missing dimensions**: Some design variables are rarely manipulated in conjunction, and high-order interaction effects are understudied.
- **Exclusion/social sanctions vs. costly punishment**: Several strong efficiency effects are found for costless exclusion or moral judgment, which are not always comparable to material punishment in PGGs.
- **Field vs. lab and ecological validity**: There is a recurring warning that laboratory punishment rates and effects may overstate or misstate real-world impacts, especially in large groups or under informal social enforcement regimes.
- **Nonlinear and nonmonotonic effects**: Multiple papers note that increasing punishment strength or likelihood does not always monotonically increase efficiency and can reverse direction at moderate or high levels.
- **Sparse evidence in non-canonical and high-dimensional settings**: For game designs far from the standard PGG, evidence is sparse or only qualitative.

---

**In summary:**  
The literature provides robust, but highly context-sensitive, evidence that the efficiency effect of enabling punishment in public-goods-game-like environments is mediated by the interaction of baseline efficiency, punishment cost-effectiveness, institution type, error/noise, and group/context structure. In many canonical designs, especially with costly peer punishment and moderate-to-high baseline efficiency, enabling punishment does **not** increase, and may reduce, treatment efficiency. In settings with low baseline cooperation, effective and well-targeted punishment (especially in institutional or well-structured central forms) can yield substantial efficiency gains, but only when costs, error, and retaliation are limited. Reward mechanisms are frequently found to be more efficient under similar conditions. Prediction of treatment efficiency must use control efficiency, detailed design dimension knowledge, and awareness of these moderators, and should treat non-payoff behavioral outcomes with caution. The literature is strongest for canonical PGGs, and predictions for more complex or hybrid designs should be made with distinct uncertainty.
