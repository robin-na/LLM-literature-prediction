# 1) Evidence Base

This paper set includes two papers: one theoretical (Chowdhury et al., 2021) and one empirical/experimental (Fonseca & Peters, 2018). The theoretical paper models dynamic strategy adoption in a repeated Prisoner's Dilemma (PD) with policing (punishment), focusing on the eco-evolutionary dynamics of cooperation. The empirical paper experimentally studies the effect of enabling (potentially inaccurate) gossip in a repeated trust game, with group efficiency as a primary outcome. Neither paper tests the canonical public goods game (PGG) with monetary peer punishment, but both examine game-theoretic social dilemmas with intervention mechanisms analogous to punishment or sanctions. The evidence base is thus narrow in scope and somewhat indirect for the task of predicting efficiency effects of peer punishment in PGG-like environments.

# 2) Task Relevance

- **pgg_or_variant:**  
  *Relevance: adjacent*  
  Both papers study repeated social dilemma settings closely related to the PGG (PD in Chowdhury et al., trust game in Fonseca & Peters), but neither implements the canonical PGG. Most mechanisms and findings are applicable to the general logic of social dilemmas but may not fully translate to all PGG-specific institutional features.

- **punishment_or_sanctions:**  
  *Relevance: Chowdhury et al.: exact; Fonseca & Peters: adjacent*  
  Chowdhury et al. explicitly model costly (monetary) punishment ("policing"), matching the prediction task. Fonseca & Peters study non-monetary, reputation-based sanctions (gossip/reputation), which functionally substitute for formal punishment but do not involve direct costs.

- **efficiency_or_related_payoff_outcome:**  
  *Relevance: Chowdhury et al.: adjacent; Fonseca & Peters: exact*  
  Fonseca & Peters directly measure efficiency (joint payoff). Chowdhury et al. focus on behavioral outcomes (population shares of cooperators/defectors/punishers) and do not report efficiency, group payoff, or welfare, although their outcomes are related in the sense that more cooperation implies higher efficiency.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:**  
  - Fonseca & Peters (2018): *Group efficiency/joint payoffs* measured directly as the primary outcome.
  - Chowdhury et al. (2021): No direct measurement of payoff or efficiency. Focuses on proportions of strategies and stability/oscillation of cooperation levels.

- **Non-payoff behavioral outcomes:**  
  - Chowdhury et al. (2021): *Strategy frequencies, coexistence, and dominance cycles* in a repeated PD with policing.
  - Fonseca & Peters (2018): *Trust and trustworthiness* (behavioral), but interpreted through the lens of payoff outcomes.

# 4) Main Findings Relevant To Prediction

- **Punishment and social sanctions can promote cooperation** in social dilemmas, but the mechanism and effect strength depend on context and implementation.
  - *Chowdhury et al. (2021)* provide theoretical evidence for the potential of costly punishment to stabilize cooperation under certain parameters, especially with moderate punishment strength. However, high temptation to defect or other ecological parameters can undermine this effect or lead to population-level oscillations rather than stable efficiency gains.
  - *Fonseca & Peters (2018)* empirically demonstrate that enabling gossip (reputational channels) increases group efficiency in a repeated trust game. This effect holds even with informational inaccuracy, suggesting robustness of indirect sanctioning. The mechanism is reputational concern and discrimination, not direct monetary punishment.

- **Magnitude and type of sanction matter for efficiency:**
  - Fonseca & Peters show that even noisy (imperfect) gossip improves efficiency compared to no-sanction baselines, but the gain is largest with accurate information (i.e., effectiveness of sanctions matters).
  - In Chowdhury et al., the strength of punishment and temptation/k pays a key role in determining whether cooperation (and, by extension, efficiency) prevails.

- **Direct empirical evidence on peer punishment in PGG is missing:**  
  The literature set does not provide direct evidence on efficiency outcomes in PGG with enabled monetary peer punishment. Instead, it provides qualitative and adjacent support via related mechanisms.

# 5) Prediction Guidance

- **If a reputational or social sanctioning mechanism (e.g., gossip) is enabled in a PGG-like setting, efficiency is expected to increase relative to a non-sanction, control condition (Fonseca & Peters, 2018).** The gain is robust even if information is imperfect, but strongest when reputational signals are accurate.

- **The presence of formal costly punishment may promote cooperation, but the literature here provides only theoretical and qualitative support for efficiency improvement (Chowdhury et al., 2021).** The efficiency boost depends on the ecological and incentive structure: too weak or too strong punishment, or high temptation to defect, may lead to variable outcomes (cooperation, oscillation, or failure).

- **Prediction of average efficiency in the treatment is uncertain and context-dependent.** The degree of improvement over control efficiency with punishment enabled cannot be precisely estimated from this set and will depend on specific implementation details (punishment cost/magnitude, temptation level, reputation accuracy, etc.).

- **For parameter-based prediction models:** 
    - The introduction of a punishment or gossip dimension should be modeled as non-linearly increasing efficiency, with effect size modulated by the technical/institutional details of sanctioning and initial group performance in the control.
    - Effects may be larger for reputational (low/no-cost) sanctions than for costly monetary punishment, depending on the setting.

# 6) Design Dimensions Highlighted Across Papers

- **Directly informed dimensions:**
  - *player_count, num_rounds, chat, all_or_nothing, mpcr, show_n_rounds* (Fonseca & Peters, 2018): These dimensions are manipulated in the trust game but not in a PGG; their effects relate to efficiency gains from enabling gossip.
  - *punishment_cost, punishment_tech* (Chowdhury et al., 2021): Theoretical exploration of how changing punishment cost/efficacy alters cooperation dynamics.

- **Indirectly/contextually discussed:**
  - *show_other_summaries, show_punishment_id*: No direct manipulation, possible contextual relevance relating to information structure but not tested.
  - *default_contrib*: Not explicitly modeled or varied.
  - *reward_exists, reward_cost, reward_tech*: Not present; no evidence on reward treatments.

- **Effectively missing:**
  - *reward-related dimensions* (reward_exists, reward_cost, reward_tech), *default_contrib*, *show_punishment_id*: Not discussed or manipulated.
  - *Efficiency outcomes in PGG with monetary peer punishment*: Not directly measured.

# 7) Important Limitations

- **Applicability is limited by game type**: Neither paper uses the canonical PGG; findings are adjacent due to use of PD and trust games.
- **Outcomes rarely match the prediction task**: Only one paper measures efficiency as defined (Fonseca & Peters), and this is for reputational, not costly, punishment.
- **Generalization to direct monetary punishment in PGG is uncertain**: The positive efficiency effects from gossip/reputation may not map quantitatively to institutionalized peer punishment.
- **Limited dimension coverage**: Several game design parameters relevant to downstream prediction (e.g., reward systems, visibility of punishment, framing of contributions) are not examined.
- **No direct comparative baseline**: Absence of direct comparison between monetary punishment and reputational sanctions within the same experimental environment.
- **Chowdhury et al.**: Theory results lack direct mapping from behavioral/population dynamics to payoff-based efficiency, especially as measured in empirical literature.

> **In summary:**  
This literature set offers a narrow, contextually adjacent base for predicting efficiency effects of enabling punishment/sanctions in PGG-like games. There is strong evidence for efficiency gains via reputational sanctions, even when imperfect, but only theoretical and behavioral-level evidence for costly punishment. Many key game design dimensions are underexplored, and the papers do not provide direct quantitative effects for PGG with peer punishment, thus necessitating caution in transferring these findings to predictions about treatment efficiency in public goods games.
