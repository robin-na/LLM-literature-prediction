# 1) Evidence Base

The paper set consists of seven papers spanning both empirical (five) and theoretical (two) work. Among the empirical studies, four report laboratory experiments relevant to public goods games (PGG), and one is a scenario-based survey on attitudes. Two theory papers address strategic or psychological mechanisms underpinning cooperation and punishment. The empirical base is relatively narrow, with only one study directly reporting efficiency or group payoff outcomes in a repeated PGG with punishment options (Engelmann & Nikiforakis, 2015). Other empirical and theoretical papers focus on related behavioral mechanisms, social preferences, or conceptual moderators of punishment’s effectiveness but generally do **not** provide direct quantitative data on efficiency or welfare under punishment. In summary, for the downstream prediction task (treatment efficiency), the evidence base is narrow and anchored by a single, highly relevant experiment, with other studies providing context, baseline controls, or adjacent mechanistic insight.

# 2) Task Relevance

### pgg_or_variant
- `exact` relevance: Five of the seven papers study or model exact public goods games or clear variants (Engelmann & Nikiforakis, 2015; Thöni, 2014; Drouvelis et al., 2015; Martinsson et al., 2015). The others use adjacent paradigms (Prisoner’s Dilemma, collective aggression scenarios).
- `close/adjacent`: Two address games that are structurally similar but not canonical linear PGGs (Blonski & Spagnolo, 2015; Lopez, 2017; Gordon & Lea, 2016).

### punishment_or_sanctions
- `exact`: Four papers directly study or model peer punishment mechanisms (Engelmann & Nikiforakis, 2015; Thöni, 2014; Blonski & Spagnolo, 2015; Lopez, 2017; Gordon & Lea, 2016).
- `none`: Two empirical studies do not include any form of punishment or sanction (Drouvelis et al., 2015; Martinsson et al., 2015).

### efficiency_or_related_payoff_outcome
- `exact`: Only Engelmann & Nikiforakis (2015) report and analyze efficiency or directly related payoff outcomes in PGG with punishment.
- `adjacent`: Other papers typically focus on cooperation rates, contribution behaviors, norm compliance, or psychological outcomes (e.g., willingness to punish, reputational expectations) rather than group payoff or welfare.
- `none`: Some papers do not report any payoff-related data, focusing exclusively on non-payoff behavioral or attitudinal outcomes (e.g., Gordon & Lea, 2016).

**Conclusion:** The literature as a whole is highly relevant for understanding public goods games and the behavioral, motivational, or structural role of punishment. However, it is only sparsely relevant to the prediction of treatment efficiency, as only one study provides direct evidence on efficiency effects of enabling punishment in PGGs.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:**  
  - *Directly measured efficiency or group payoff:* Only Engelmann & Nikiforakis (2015) directly report on group earnings (efficiency) in PGGs with/without various punishment mechanisms.
  - *Baseline group earnings (adjacent/partial):* Some studies (e.g., Martinsson et al., 2015; Drouvelis et al., 2015) report average earnings as secondary outcomes, mostly as context for behavioral analyses, not as primary endpoints.

- **Non-payoff behavioral outcomes:**  
  - *Contribution rate/cooperation rate:* Common in nearly all papers except Gordon & Lea (2016), who focus on reputational and status-related outcomes.
  - *Punishment assigned, frequency of sanctions, antisocial punishment, motives for punishing:* Addressed primarily by Thöni (2014) and Engelmann & Nikiforakis (2015).
  - *Norm compliance, willingness to punish, reputational benefit, psychological attitudes toward sanctioning:* Explored in Thöni (2014), Gordon & Lea (2016), and Lopez (2017).

**Distinction:** Only Engelmann & Nikiforakis (2015) provide primary outcome data directly addressing group efficiency. The majority of behavioral outcomes in other papers inform about mechanisms or moderators but not net payoffs or efficiency.

# 4) Main Findings Relevant To Prediction

## Empirical Findings

- In linear repeated PGGs (4 players, 30 rounds), enabling peer punishment can increase group efficiency **if** the punishment environment is structured to limit retaliation and escalation (Engelmann & Nikiforakis, 2015). In a *single-stage, anonymous punishment* mechanism (SP), efficiency increases relative to the no-punishment control (NP), eventually surpassing it. When punishment is unconstrained—multiple stages, fixed IDs, and full information about punishers (RP)—retaliation and feuding emerge, raising costs and eroding efficiency gains. Some groups achieve high cooperation but at high punishment costs, leading to no net efficiency improvement.
- Baseline (control) efficiency appears similar across treatment arms—with punishment disabled. The *design of the punishment mechanism* itself determines the realized efficiency gain when punishment is enabled, rather than underlying control efficiency alone (Engelmann & Nikiforakis, 2015).

## Mechanisms and Moderators (Behavioral/Theoretical Findings)

- The *presence of antisocial punishment* (punishing cooperators, revenge) is detrimental to efficiency and more likely when game design allows open retaliation (Thöni, 2014).
- The impact of punishment on sustaining cooperation in repeated games depends on strategic factors like the harshness and reputation structure of punishment strategies and the patience of players (Blonski & Spagnolo, 2015). However, these arguments do not quantify efficiency effects.
- Social context (e.g., status of the punisher, visibility of actions) may modulate willingness to punish but lacks direct evidence on efficiency or earnings (Gordon & Lea, 2016; Lopez, 2017).

## Consistency and Ambiguity

- There is consistency in the empirical finding that simple, anonymous, one-shot peer punishment mechanisms can improve efficiency by increasing and sustaining cooperation, but *only when designed to limit costly retaliation or cycles*.
- The main ambiguity is in more complex, information-rich, or multi-stage punishment environments, which, while increasing compliance or contribution, may dissipate group resources through punishment costs, nullifying or even reversing efficiency gains.

# 5) Prediction Guidance

Given the evidence, **predictions for treatment efficiency (with punishment enabled) should hinge not only on the control (no-punishment) efficiency but, critically, on the design specifics of the punishment mechanism**:

- **If punishment is implemented as a single, anonymous, per-round stage (no ID tracking, no information about punishers), enabling punishment is likely to *increase* average efficiency relative to the control (no-punishment) baseline, especially in repeated games with 4 players, 30 rounds, and typical MPCRs (Engelmann & Nikiforakis, 2015).**
- **If punishment allows retaliation—via multiple punishment stages, fixed IDs, and/or transparency about who punishes whom—the efficiency gain is at risk: high punishment costs and feuding offset the benefits of increased contributions (Engelmann & Nikiforakis, 2015; Thöni, 2014). Efficiency may not improve over baseline, and in some groups may fall below control.**
- **Control efficiency is a necessary baseline but is insufficient for predicting treatment efficiency without accounting for punishment technology and information structure.**
- **Mechanism arguments (Blonski & Spagnolo, 2015; Thöni, 2014) imply additional moderators—players' patience, risk attitudes, susceptibility to antisocial motives—but these dimensions are not systematically mapped to efficiency outcomes in public goods experiments and thus cannot support granular quantitative predictions here.**

# 6) Design Dimensions Highlighted Across Papers

**Directly informed design dimensions (with empirical data on payoff/efficiency):**
- `player_count`, `num_rounds`, `all_or_nothing`, `mpcr`, `punishment_cost`, `punishment_tech` (Engelmann & Nikiforakis, 2015).

**Indirectly informed (behavioral data, no efficiency):**
- `chat`, `show_n_rounds`, `show_other_summaries` (in studies without punishment, e.g., Drouvelis et al., 2015; Martinsson et al., 2015).

**Contextually discussed / moderator arguments:**
- `show_punishment_id` (linked to retaliation and punishment effectiveness, but no direct efficiency instantiation—Engelmann & Nikiforakis, 2015; Gordon & Lea, 2016).
- `reward_exists` (Lopez, 2017, via attitudes, not payoff).

**Effectively missing (not empirically instantiated with efficiency outcomes):**
- `default_contrib` (no direct test or report).
- `reward_cost`, `reward_tech` (only mentioned, not analyzed in payoff terms).
- `show_other_summaries`, `show_n_rounds` (no efficiency data under punishment).
- `chat` (not combined with punishment in efficiency analysis).

# 7) Important Limitations

- **Essential limitation:** Only one experimental paper (Engelmann & Nikiforakis, 2015) provides direct, quantitative evidence of peer punishment effects on group efficiency in a PGG. All other studies are either *adjacent* in mechanics, report only behavioral outcomes, or discuss theory—rendering cross-paper synthesis on efficiency shallow.
- **Design space coverage** is narrow—most dimensions used in the downstream prediction task are under-informed in terms of their empirical relation to efficiency under punishment. Especially under-represented: contextual cues (e.g., chat, show_n_rounds), reward mechanisms, default framing, and feedback structures.
- **No studies in this set experimentally manipulate or combine factors such as chat, group size, MPCR, or information provision in a systematic way alongside punishment treatment and report efficiency outcomes.**
- **Behavioral findings** on contribution rates, willingness to punish, or attitudes, while useful for understanding possible moderators or mechanisms, are not directly translatable into efficiency predictions.
- **Ambiguity persists** for environments enabling complex punishment strategies or retaliation, as efficiency outcomes become highly variable and group-specific.
- **No coverage** of large groups, different MPCR regimes, shorter or longer time horizons, or alternate forms of peer sanctioning (beyond those in Engelmann & Nikiforakis, 2015).

**In sum:** The literature provides strong guidance that efficiency outcomes when punishment is enabled are highly sensitive to punishment design parameters; however, coverage of other game dimensions is sparse or absent, so prediction beyond mechanisms closely matching Engelmann & Nikiforakis (2015) is speculative. Additional empirical evidence is needed for robust prediction across the full design space.
