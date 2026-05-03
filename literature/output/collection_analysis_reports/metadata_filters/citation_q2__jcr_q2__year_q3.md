# 1) Evidence Base

The paper set is robust: it includes 90 sources with a strong empirical focus on standard linear public goods games (PGGs) and their close variants. Most core studies are laboratory experiments that directly manipulate punishment and measure group payoff or efficiency, well-aligned with the downstream prediction task. There is a substantial presence of theoretical/simulation work mapping design dimensions (e.g., punishment cost/effectiveness, information structure), which complements the empirical findings. The breadth of topics also means evidence exists for a range of moderators, including heterogeneity, information, network structure, peer vs. centralized punishment, and context (emotions, group composition, communication).

However, the set also contains many papers that are adjacent or weakly relevant: studies on trust, CPRs, network or spatial dilemmas, or papers focused solely on non-payoff behavioral outcomes (e.g., cooperation rate, punishment frequency). As a result, the overall base is broad but the highest-density evidence concerns classic PGGs with measured efficiency or group payoff changes when punishment is enabled.

# 2) Task Relevance

- **pgg_or_variant**:  
  - Label: **exact** (majority), with **close** and **adjacent** support.
  - Many papers use precisely the repeated linear PGG. Several more employ threshold PGGs or common-pool resource (CPR) games (close), or structurally similar social dilemmas (adjacent). Very few papers are unrelated.  
- **punishment_or_sanctions**:  
  - Label: **exact** (many), with a mixture of **close** (e.g., exclusion, centralized punishment, fines, whistleblowing) and **adjacent** (reputation, exit, reporting, partner choice) mechanisms.
  - The most relevant papers implement direct, costly peer or pool punishment; some add endogenous institutional choice or compare peer to centralized enforcement.
- **efficiency_or_related_payoff_outcome**:  
  - Label: **exact** (several core studies), but many only report **close** or **adjacent** outcomes.
  - A substantial chunk of the literature reports contribution or cooperation rates, punishment frequency, or norm compliance—behaviors not strictly equivalent to efficiency, though often correlated.  
  - However, a sufficient number of empirical studies report group payoff, welfare, or normalized efficiency outcomes, directly matching the prediction target.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (directly relevant):**
  - **Efficiency/group payoff/welfare/surplus:** Explicitly measured in many empirical and some theoretical works (e.g., Lee & Min, 2021; Angelovski et al., 2018; Mantilla et al., 2021; Cobo-Reyes et al., 2019; Fatas et al., 2020; Waichman, 2020; Koch et al., 2021; De Geest & Kingsley, 2021; Kol'veková et al., 2021).
  - **Total earnings, profit, surplus:** Used interchangeably with efficiency in several studies, though occasionally calculated slightly differently.
  - Some theory/simulation papers directly predict average payoff or system growth rates.

- **Non-payoff behavioral outcomes (contextually relevant, not substitutes):**
  - **Contribution/cooperation rate:** Nearly universal as a primary or secondary variable; many papers use this as a proxy for efficiency, but it's not always proportional due to punishment costs.
  - **Punishment frequency/assignment, norm compliance, conditional cooperation:** Foundational for understanding mechanisms, but not equivalent to efficiency.
  - **Retaliation, antisocial punishment, norm enforcement dynamics:** Inform why efficiency does/does not change, but not measures of payoff.
  - **Some studies examine effects on trust, social norms, reputation, but without payoff analysis.**

# 4) Main Findings Relevant To Prediction

**General Patterns (Synthesized Across Papers):**
- **Enabling punishment often increases efficiency, but...**  
  - Only if punishment is well-targeted at defectors, antisocial punishment and retaliation are low, and punishment costs do not exceed the efficiency gain from increased cooperation (e.g., Angelovski et al., 2018; Waichman, 2020; Schlösser et al., 2018).
- **Substantial exceptions:**  
  - Where antisocial punishment, costly peer feud cycles, or mis-targeted sanctions prevail, punishment can reduce or fail to increase efficiency relative to control (e.g., Mantilla et al., 2021; Vollan et al., 2019; Drouvelis et al., 2021; Fatas et al., 2020 [circle/line networks]; De Geest & Kingsley, 2019).
- **Critical moderators include:**  
  - **Group composition/diversity:** In-group favoritism or out-group aversion reduces punishment's effect (Mantilla et al., 2021; Drouvelis et al., 2021).
  - **Heterogeneity in endowment/capacity:** Efficiency gains from punishment require observable and targetable heterogeneity (Waichman, 2020; De Geest & Kingsley, 2021).
  - **Information structure:** Effective punishment requires both contribution and capacity (endowment) to be visible (De Geest & Kingsley, 2019, 2021; Waichman & Stenzel, 2019).
  - **Punishment mechanism/technology:** Peer punishment (self-governed) is more vulnerable to inefficiency than centralized or shared/pooled mechanisms (Angelovski et al., 2018; Kol'veková et al., 2021).
  - **Punishment cost and severity:** High punishment costs or low impact ratios can moderate the efficiency effect; too high costs can make punishment destructive (Sui et al., 2018; Powers, 2018; Podobnik et al., 2019).
  - **Network structure:** Complete/star networks favor efficiency gains from punishment; incomplete (circle/line) structures favor antisocial cycles and inefficiency (Fatas et al., 2020).
  - **Chat/communication:** Joint presence of chat and punishment can improve efficiency more than either alone; early communication is especially powerful (Koch et al., 2021).
  - **Emotional context:** Incidental happiness or anger can flip the effect of punishment on efficiency (Lee & Min, 2021).
  - **Institutional choice/endogeneity:** If players can vote in punishment mechanisms, both efficiency and fairness increase relative to imposed institutions (Cobo-Reyes et al., 2019; Kol'veková et al., 2021).

- **Control group efficiency is a good, but NOT sufficient, baseline.**  
  The effect of enabling punishment on efficiency is highly conditional; control efficiency must be interpreted in the context of punishment's cost/benefit and design moderators.

- **Other design features that impact the punishment effect:**  
  - Visibility of punishment (to others or to recipients) increases targeting and thus efficiency (Kamei, 2018; Waichman & Stenzel, 2019).
  - Presence of rewards as an alternative or complement to punishment is a separate moderator (less studied in this set for efficiency).
  - Sanctioner incentives matter: if punishers benefit extrinsically or appear self-interested, efficiency can paradoxically fall (Angelovski et al., 2018).

# 5) Prediction Guidance

The literature indicates that **the average efficiency of the punishment-enabled game cannot be predicted from control efficiency alone**; prediction accuracy depends on detailed alignment of game design dimensions with the known evidence base.

**Core prediction rules backed by evidence:**
- **Punishment increases efficiency IF:**
  - Peer or centralized punishment is cheap/targeted,
  - Antisocial punishment is limited,
  - Group is homogeneous or diversity does not disrupt norm enforcement,
  - Endowments/capacity are visible, so punishment can be accurately targeted,
  - Network is complete or star-like,
  - Mechanism allows for endogenously calibrated, low-cost or pooled punishment,
  - Optionally, chat/communication is enabled and precedes punishment,
  - The emotional environment is neutral/angry (not incidentially happy).

- **Punishment has no effect or reduces efficiency IF:**
  - Antisocial punishment/retaliation is high (due to group norms, diversity, status dynamics, or incomplete/wrong targeting),
  - Punishment costs are high or impact is low,
  - Group structure limits visibility, communication, or coordination,
  - The environment elicits happiness or in-group favoritism/intergroup tension dominates,
  - Institutional design (e.g., sanctioner paid by pool) is perceived as unfair or as second-order free riding.

- **Reward mechanisms alone can also increase efficiency, but the prediction task is focused on punishment. Some mechanisms blending punishments and rewards (or allowing choice) require separate consideration.**

- **Theory consistently demonstrates threshold/bifurcation effects:** If punishment support falls below a minimum or is too delayed, efficiency collapses; moderate, timely punishment sustains high efficiency (Brandt & Svendsen, 2019; Powers, 2018).

- **Sensitivity to design dimensions:**  
  Predictions must explicitly incorporate the measured or modeled parameters: player_count, num_rounds, MPCR, all_or_nothing, punishment_cost/effectiveness, information availability (show_other_summaries, show_punishment_id), communication, and group composition. Sparse or missing evidence for some dimensions requires conservative extrapolation, with uncertainty reported.

# 6) Design Dimensions Highlighted Across Papers

| Dimension                   | Literature Coverage                                                                         | Guidance for Prediction                      |
|-----------------------------|--------------------------------------------------------------------------------------------|----------------------------------------------|
| `player_count`              | Direct in nearly all studies                                                               | Strongly informed                            |
| `num_rounds`                | Direct in all repeated game studies                                                        | Strongly informed                            |
| `chat`                      | Included in a moderate subset; shown to moderate the effect of punishment                  | Moderately informed (predict synergy)        |
| `all_or_nothing`            | Most studies specify (continuous or discrete)                                              | Well covered                                 |
| `default_contrib`           | Rarely varied/explicit; sometimes present as opt-in/out framing                           | Sparse                                       |
| `mpcr`                      | Always specified; central to effects                                                       | Strongly informed                            |
| `punishment_cost`           | Almost always reported and manipulated                                                     | Strongly informed                            |
| `punishment_tech`           | Peer, centralized, shared, whistleblowing; varied in several key papers                    | Moderately to strongly informed              |
| `reward_exists`             | Sometimes included, but often held constant when examining punishment                      | Moderately informed; less relevant for pure punishment predictions |
| `reward_cost`               | Seldom varied independently                                                                | Sparse                                       |
| `reward_tech`               | Rarely a key focus                                                                         | Sparse                                       |
| `show_n_rounds`             | Often specified (known/unknown horizon)                                                    | Moderately informed; effects smaller         |
| `show_other_summaries`      | Key for information structure; directly relevant where targeting is examined               | Directly supported in relevant studies       |
| `show_punishment_id`        | Sometimes varied; visibility/salience shown to increase effect of punishment               | Some evidence, but weaker and context-dependent  |

**Indirectly, other contextual dimensions also have robust support:**  
- Group composition (homogeneity, status, ethnicity)
- Heterogeneity of endowments/capacities
- Emotional context (explicit manipulation)
- Network or organizational structure (complete, star, line, pyramid)

**Missing or contextually discussed:**  
- Contribution framing (default_contrib): only rare explicit manipulations.
- Reward cost/tech: generally not the focus when predicting punishment-driven efficiency.

# 7) Important Limitations

- **Ambiguity and heterogeneity:** In some parameter regions, and in settings with high antisocial punishment or poorly targeted sanctions, the efficiency effect is ambiguous or negative; empirical studies sometimes directly conflict.
- **Sparse causal evidence on reward**: While reward and communication matter, well-powered, direct evidence on their combined effect with punishment and on their contingent effects is less common.
- **Non-payoff outcomes overemphasized:** Many studies only report contribution rates or norm compliance but not realized efficiency; these are not substitutes and may create overestimates of efficiency benefits.
- **External validity**: Most evidence is from lab experiments with student populations; generalization to field or naturalistic settings, especially with larger groups, more rounds, or "real" stakes, is uncertain.
- **Parameter gaps**: Some design dimensions (e.g., reward tech/cost, contribution framing) are under-explored. Indirect inference required for prediction under such settings.
- **Peer vs. centralized vs. shared punishment**: While strongly evidenced in some cases, the efficiency tradeoff between forms (peer, pool, centralized) may not generalize.
- **Emotion and context**: Papers manipulating emotional context or group composition show large, occasionally non-intuitive moderation effects but few studies systematically cross these with other parameters.

---

**Summary:** The contemporary literature provides strong, nuanced evidence for predicting the efficiency effect of enabling peer punishment in public goods games, conditional on key design dimensions. Some dimensions are richly evidenced (group size, MPCR, punishment cost/tech, information structure), but others—especially reward mechanisms and contribution framing—are sparse. The main guidance is to expect treatment efficiency to increase relative to control when punishment is well-targeted, low-cost, and group/context supports effective sanctioning; otherwise, efficiency gains are null or negative—especially when punishment is antisocial, mistargeted, costly, or group norms/intergroup dynamics interfere. Carefully align game parameters with evidence and preserve uncertainty where evidence is ambiguous or missing.
