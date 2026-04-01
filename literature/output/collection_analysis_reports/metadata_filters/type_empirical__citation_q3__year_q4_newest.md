# 1) Evidence Base

This paper set consists of 16 studies, almost all of which are empirical and experimental, with a mix of lab, field, and observational studies. The majority of experiments are with human participants and focus on cooperation, punishment, and enforcement in social dilemma and public-goods-game-like (PGG) environments. A few papers are meta-analyses or use artificial agents. Direct measurement of efficiency or group payoff (as opposed to behavioral outcomes like cooperation rate or punishment behavior) is rare; most studies focus on non-payoff behavioral measures. Only one paper (Köster et al., 2022) reports efficiency as a primary outcome in a multiagent environment. The breadth of the paper set covers various designs, cultures, and mechanisms relevant to punishment, but is relatively narrow for direct efficiency prediction in standard PGGs with punishment. Many papers use adjacent designs (e.g., trust games, dictator games, real-world societies) or focus on mechanisms (emotions, cognitive load, group identity) rather than downstream efficiency effects.

# 2) Task Relevance

**PGG or Variant:**  
- **exact:** Several papers use PGG or repeated PGG experimental designs (Zhou et al., 2023; Zhou et al., 2022; Spadaro et al., 2022; Capraro, 2024).
- **close/adjacent:** Many others use adjacent designs (e.g., third-party punishment games, trust games, centipede/intergroup dilemmas, evolutionary norm enforcement in artificial agents).
- **weak/none:** A minority use real-world village data or non-game settings.

**Punishment or Sanctions:**  
- **exact:** Many studies include punishment as a formal mechanism or treatment (Zhou et al., 2023; Zhou et al., 2022; Spadaro et al., 2022; Köster et al., 2022; Capraro, 2024).
- **close/adjacent:** Some focus on aspects of sanctioning, like third-party or exogenous punishment, without a canonical PGG structure.
- **none:** Several studies lack any punishment or sanctioning mechanism (Wang et al., 2023; Otten et al., 2022).

**Efficiency or Related Payoff Outcome:**  
- **exact:** Only Köster et al. (2022) and Nunney et al. (2022) report efficiency/group payoff as a primary outcome.
- **adjacent/weak:** Most studies measure contribution rates, trust, norm compliance, or punishment assigned, not group earnings, welfare, or surplus.
- **none:** Some are solely focused on norm perception, emotion, or mechanism, without any payoff measures.

**Summary:**  
The literature is strongest in exact/close relevance to PGG structures and the implementation of punishment/sanctions. It is much weaker in reporting or analyzing efficiency or group payoff outcomes, which are key for the downstream prediction task. Most evidence for the effect of punishment applies to behavioral cooperation, not directly to efficiency or welfare.

# 3) Outcomes Measured In The Literature

**Payoff-related Outcomes:**  
- **Direct (efficiency, group payoff, welfare):**  
  - Köster et al. (2022) (artificial agents, group efficiency effect of punishment)
  - Nunney et al. (2022) (intergroup game, effect of emotion on group payoff—mixed, not always standard PGG)
- **Indirect/adjacent (related to payoff):**  
  - Several others discuss behavioral proxies (cooperation rate, contribution rate) without reporting payoffs or efficiency calculation.

**Non-Payoff Behavioral Outcomes:**  
- Contribution or cooperation rates (Zhou et al., 2023; Zhou et al., 2022; Spadaro et al., 2022; Capraro, 2024)
- Punishment frequency/severity (Guo et al., 2022; Dimant & Gesche, 2023)
- Trust and trustworthiness (Sun et al., 2022; Makovi et al., 2023)
- Norm compliance and perceptions (Dimant & Gesche, 2023; Makovi et al., 2023)
- Emotional responses/effects (Gummerum et al., 2022; Nunney et al., 2022)
- Observational reports on real-world sanctions and mediation (Fitouchi & Singh, 2023; Singh & Garfield, 2022)

**Distinction:**  
Most of the literature provides rich data on how punishment affects *behavior* (such as increased cooperation or willingness to punish), but rarely measures the resulting impact on *group efficiency* or *total payoff*.

# 4) Main Findings Relevant To Prediction

- **Enabling punishment (peer or exogenous) robustly increases contribution or cooperation rates in repeated and one-shot PGGs and close variants** (Zhou et al., 2023; Zhou et al., 2022; Spadaro et al., 2022).
  - This is robust across different cultures, ages, and (to a degree) settings.
  - However, this effect is most directly observed in *behavioral* outcomes, not always in *efficiency*.

- **Link between increased cooperation and increased efficiency is implied, but rarely measured.**
  - Only Köster et al. (2022), in an adjacent artificial agent setting, shows that adding punishment increases efficiency (collective return), particularly when enforcement opportunities are more frequent.
  - In other studies, the mapping from higher contribution rates to higher efficiency is suggested but not directly tested.

- **Moderators of punishment's effect include:**
  - Cultural background and social norms (Zhou et al., 2023; Guo et al., 2022; Spadaro et al., 2023)
  - Trust in sanctioning institutions—if punishment is administered by corrupt/untrusted third parties, it may *reduce* cooperation/trust (Spadaro et al., 2023)
  - Communication and emotional cues (Nunney et al., 2022) can enhance or substitute for formal punishment, and emotional states (anger, shame, pride) can increase or decrease punishment rates (Gummerum et al., 2022).
  - Cognitive processing pathway (intuitive vs reflective) alters punishment rates (Capraro, 2024).

- **Punishment details (decentralized/peer vs exogenous/third-party), cost, and "technology" matter:**
  - Punishment is more effective at increasing contributions when exogenous (Zhou et al., 2022), but this is shown only for contributions, not for efficiency.
  - When punishment cost is too low or too high, effectiveness may change (reported in predictions, not as a central measured outcome).

- **Contextual evidence from adjacent designs and societies:**
  - In real-world, small-scale societies, punishment is usually dyadic and restorative, rather than group-norm enforcing. Group-level efficiency motives for punishment are rare (Fitouchi & Singh, 2023; Singh & Garfield, 2022).
  - In agent-based and evolutionary games, richer "enforcement opportunities" (even for arbitrary rules) can accelerate efficient norm learning and improve group payoff (Köster et al., 2022).

- **Cases where enabling punishment does *not* increase group payoff:**
  - Not directly observed in these papers due to lack of efficiency measurement; however, Spadaro et al. (2023) shows that if punishment institutions are perceived as corrupt, this can undermine trust and reduce cooperation.

# 5) Prediction Guidance

- **Prediction models can generally assume that enabling peer punishment in repeated or one-shot PGGs increases contribution rates, but should not automatically expect a proportional increase in group efficiency.** The mapping from higher cooperation to higher efficiency is context-dependent and can be undermined by punishment costs, antisocial punishment, or the specific implementation of the punishment technology.

- **Where baseline efficiency is low (e.g., due to low initial cooperation), enabling punishment is likely to produce a *relative* increase in efficiency,** provided punishment is not costly enough to offset group gains. This is indirectly supported by findings on contributions (Zhou et al., 2022), and is corroborated by artificial agent results showing efficiency gains (Köster et al., 2022).

- **Details matter:**
  - The prediction should be sensitive to **punishment cost** and **punishment magnitude**; too costly punishment can erode efficiency even as contributions increase.
  - **Cultural and social context** may affect the size of the effect, but there is no strong evidence of qualitative reversals in standard PGGs.
  - **Institutional integrity** is crucial: if punishment is administered by a third party and is perceived as unfair or corrupt, the expected efficiency gain may be reduced or even reversed.
  - **Communication** and **emotional expression** are important moderators; their presence can diminish or amplify the need/mechanism for punishment.

- **Dimension-level evidence should be interpreted with caution:** Because actual group efficiency or payoff is usually not measured, inferences often rely on the assumption that higher contributions mean higher efficiency, but this is not always true, especially when punishment is costly.

- **Any extrapolation beyond standard PGGs (e.g., adjacency to centipede or trust games, agent societies, or real societies) should be qualified by recognizing the lack of direct efficiency outcome measurement.**

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- `player_count`, `num_rounds`, `mpcr`: Frequently varied or specified; form the basis for almost all lab-based designs and comparisons.
- `punishment_cost`, `punishment_tech`: Often manipulated or discussed; effects on punishment behavior are explored.
- `chat`/`communication`: Sometimes included; shown to modulate cooperation but rarely directly linked to efficiency.

**Indirectly Informed Dimensions:**
- `all_or_nothing`, `default_contrib`: Sometimes present in experimental treatments, without direct comparison effects on efficiency.
- `show_other_summaries`, `show_n_rounds`, `show_punishment_id`: Occasionally described, mainly as context; rarely tested for direct effect on efficiency or even cooperation.
- `reward_exists`, `reward_cost`, `reward_tech`: Sometimes included, especially in comparative studies, but reward and punishment are not always tested in reciprocal designs.

**Only Contextually Discussed or Effectively Missing:**
- Details of `reward_magnitude`, or interaction effects between rewards and punishments, are only occasionally present (Wang et al., 2023).
- The interplay between visibility of punishment (identities) and efficiency is mentioned but not a focus.
- Real-world studies mention restorative vs. punitive approaches but do not manipulate game design dimensions experimentally.

**Summary:**  
The design dimensions that are most reliably informed are those related to basic game structure (player count, rounds, MPCR), punishment mechanisms (cost, technology), and to a lesser extent, communication. Most other dimensions are insufficiently studied for specific prediction about their effect on efficiency after enabling punishment.

# 7) Important Limitations

- **Scant direct measurement of efficiency:** Most papers use cooperation, contribution, or trust as a proxy for efficiency. Only one (Köster et al., 2022, artificial agents) measures true group efficiency after enabling punishment in a PGG-like environment.

- **Mapping from behavioral outcomes to efficiency is indirect and potentially misleading:** Increased contributions may not always increase efficiency, especially if punishment is expensive or misapplied (e.g., antisocial punishment, corrupt institutions).

- **Limited examination of design dimension interactions:** Very few studies systematically manipulate more than 2–3 dimensions relevant to prediction.

- **Cultural and ecological context may moderate but is not fully resolved:** While cultural background is often included as a moderator, direct cross-cultural comparisons of efficiency effects are lacking.

- **Observational and adjacent-context studies are less transferable:** Evidence from small-scale societies or non-PGG games may not generalize to lab PGGs with formal punishment and quantified payoffs.

- **Peer punishment vs third-party punishment distinctions blurred:** Some studies combine or do not distinguish between decentralized/peer and institutional punishment, affecting applicability to pure peer-punishment PGGs.

- **Reward mechanisms underexplored relative to punishment:** Occasionally present, but rarely in full factorial design with punishment for efficiency comparison.

- **Artificial agent studies (Köster et al., 2022) may not fully generalize to human groups.**

**Conclusion:**  
This body of literature establishes that enabling punishment reliably increases *behavioral cooperation* and likely *increases efficiency* in many PGG-like environments—conditional on the costs not outweighing the benefit, the punishment institution not being corrupt, and in the absence of strong social or cultural moderators that can reverse the effect. However, the limited direct evidence on efficiency constrains precise or mechanistic prediction of treatment efficiency from design dimensions and control efficiency alone. Further research with direct measurement of group payoffs and systematic manipulation of design features is needed to support robust downstream predictions.
