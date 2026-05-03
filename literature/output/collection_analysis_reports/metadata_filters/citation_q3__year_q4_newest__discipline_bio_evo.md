# 1) Evidence Base

This paper set is composed of three empirical papers (two laboratory experimental studies and one observational ethnography) and one theoretical paper. The empirical studies range from experimental investigations of coordination and trust in collective settings to ethnographic documentation of justice in small-scale societies. The theoretical paper explores the psychological underpinnings of norm adherence and group dynamics. Overall, the set is broad in disciplinary scope (spanning economics, psychology, anthropology, and philosophy), but is narrow in directly addressing the specific prediction target: the efficiency effects of enabling peer punishment in public-goods-game (PGG) or closely related environments. Empirical coverage of efficiency or group-payoff outcomes in the presence versus absence of peer punishment is notably limited.

# 2) Task Relevance

**pgg_or_variant:**  
- *exact:* None of the papers study a canonical PGG with peer punishment enabled versus disabled.
- *close:* Wang et al. (2023) studies threshold public goods games, but without punishment or reward mechanisms.
- *adjacent:* Spadaro et al. (2023) employs economic games with sanctioning institutions (third-party punishment) but not strict PGGs; Singh & Garfield (2022) analyzes social penalties in real-world collective dilemmas, not PGGs.
- *none:* Bar-On & Lamm (2023) does not discuss PGGs.

**punishment_or_sanctions:**  
- *exact:* Spadaro et al. (2023) precisely isolates the presence of third-party punishment, though not peer punishment.
- *adjacent:* Singh & Garfield (2022) and Bar-On & Lamm (2023) discuss broader or indirect forms of sanctions or norm enforcement.
- *none:* Wang et al. (2023) does not include any punishment or sanction mechanism.

**efficiency_or_related_payoff_outcome:**  
- *close:* Wang et al. (2023) mainly studies coordination and threshold success rates, which relate to group payoff, but not with punishment enabled.
- *adjacent/weak:* Spadaro et al. (2023) does not measure or report efficiency outcomes, focusing on trust and cooperation rates; Singh & Garfield (2022) describes case patterns of cooperation restoration but without operationalized group efficiency measures.
- *none:* Bar-On & Lamm (2023) does not address payoff-based outcomes.

**Summary:**  
Across the three dimensions, no study directly addresses the efficiency impact of enabling peer punishment in a PGG context; the literature is mostly adjacent or only contextually relevant.

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes:**  
- Wang et al. (2023): Reports group success (whether the threshold is reached) in threshold PGGs, which is tightly linked to group payoff, but only in the absence of punishment/reward.
- Spadaro et al. (2023): Does *not* report group payoff or efficiency; focus is on behavioral responses.
- Singh & Garfield (2022): Provides qualitative data on restoration of cooperation and penalties, with no quantitative group payoff or efficiency metric.
- Bar-On & Lamm (2023): Does *not* measure any outcome; presents only theoretical narrative.

**Non-Payoff Behavioral Outcomes:**  
- Wang et al. (2023): Contribution patterns, coordination strategies, fairness heuristics.
- Spadaro et al. (2023): Trust, cooperation rate, perceived corruption, willingness to cooperate under institutional conditions.
- Singh & Garfield (2022): Descriptive patterns of penalty assignments, mediation behaviors, kin-based negotiation.
- Bar-On & Lamm (2023): Discussion of norm psychology and group identity without operationalized outcomes.

**Distinction:**  
With the exception of general group success in Wang et al. (2023), the evidence is dominated by non-payoff behavioral metrics rather than direct group efficiency or payout outcomes.

# 4) Main Findings Relevant To Prediction

**Empirical Findings:**
- **Coordination in Heterogeneous PGGs (Wang et al., 2023):** Endowment inequality hampers coordination and group success, reducing the proportion of groups achieving the collective threshold (a proxy for efficient outcomes). Productivity inequality does not have the same negative effect. No evidence is provided about the impact of punishment, as sanctioning is absent.
- **Role of Punishment Integrity (Spadaro et al., 2023):** The presence of corrupt third-party punishers undermines trust and reduces cooperation in various economic games. However, group payoff or efficiency metrics are not reported, nor is peer punishment examined—only centralized (third-party) punishment is varied, always present in the design.
- **Social Sanctions in Small-Scale Societies (Singh & Garfield, 2022):** In real-world, kin-based contexts, third-party punishment is rare, and penalties are used primarily for relationship repair. There is no evidence for group-level norm enforcement or for sanctions increasing group efficiency. Outcomes are qualitative and behavioral (restoration of cooperation), with no direct analog to PGG efficiency.
- **Theoretical Synthesis (Bar-On & Lamm, 2023):** Discusses how norm enforcement (including punishment) is entwined with group identity and norm psychology, but without empirical or quantitative findings related to efficiency or game design.

**Mechanism Arguments:**  
- Trust and perceived legitimacy of punishment institutions (even when not explicitly measured in payoff terms) are suggested as potential moderators of cooperation.
- Social context—particularly the structure of relationships (e.g., kin-based versus anonymous)—may affect the presence and nature of sanctions, and thus their potential impact on efficiency.

**Ambiguity/Disagreement:**  
- The findings suggest possible negative consequences when punishment is perceived as unfair or corrupt (Spadaro et al., 2023), but lack efficiency outcome data.
- In small-scale societies, group-level punishment/efficiency logic does not map directly to observed sanctioning behaviors (Singh & Garfield, 2022).

# 5) Prediction Guidance

Given the notable lack of direct empirical data on the efficiency impact of enabling peer punishment in PGG environments, this literature set provides only indirect or contextual guidance for the downstream prediction task:

- **Baseline Efficiency Context:** There is moderate empirical support (Wang et al., 2023) for the influence of group composition (e.g., endowment inequality) on control-group (no punishment) efficiency, implying that control efficiency is a meaningful baseline for prediction, especially in asymmetric designs. However, no evidence connects this baseline to changes due to punishment.
- **Moderating Effects:** The integrity or trustworthiness of sanctioning institutions is highlighted as a moderator for cooperation, with implications that punishment may not always boost cooperation or efficiency (Spadaro et al., 2023), but these results are in contexts distinct from peer punishment in PGGs.
- **Non-Generalizability to Peer Punishment:** Ethnographic and theoretical papers emphasize that punishment mechanisms, and their effects, may vary substantially by social context and may not reliably increase efficiency (Singh & Garfield, 2022; Bar-On & Lamm, 2023).
- **Lack of Payoff Data:** Since most outcomes are non-payoff behavioral measures, translation to predicted efficiency outcomes for the downstream task is speculative; there is no basis for quantitative calibration.

**In summary:** The literature supports using control efficiency, game design heterogeneity, and the perceived legitimacy of punishment as relevant contextual signals, but provides no empirical regularity or parameterization for predicting efficiency with punishment enabled.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**
- **player_count, num_rounds, all_or_nothing, reward_exists, reward_cost, reward_tech** (Wang et al., 2023; covers these in threshold PGGs, but without punishment or payoff outcomes when sanctions are present)
- **player_count, num_rounds, chat, all_or_nothing, mpcr, punishment_cost** (Spadaro et al., 2023; peer punishment not included, but third-party punishment and some dimensions addressed)
- **chat, punishment_cost, show_other_summaries, show_punishment_id** (Singh & Garfield, 2022; through qualitative observation)

**Indirectly Informed or Contextually Discussed:**
- **legitimacy/integrity of the punishment institution** (Spadaro et al., 2023), relevant though not one of the 14 explicit dimensions.
- **social/kin structure and mediation norms** (Singh & Garfield, 2022)

**Effectively Missing:**
- **default_contrib, punishment_tech, reward_tech, reward_exists, reward_cost, reward_tech, show_n_rounds, show_other_summaries, show_punishment_id** are rarely or never discussed in efficiency or punishment contexts relevant to the prediction target.
- No paper explicitly measures or manipulates the effect of any single design dimension on the change in efficiency with punishment enabled.

# 7) Important Limitations

- **Lack of Direct Evidence:** No studies manipulate or measure the introduction of peer punishment in PGGs and measure efficiency outcomes, meaning the core prediction target is unsupported by direct empirical data. Most evidence is at best adjacent.
- **Outcomes Focused on Behavior, Not Payoff:** Almost all measured outcomes concern trust, cooperation, penalty assignment, or group decision patterns, not explicit payoff or efficiency results.
- **Institutional/Contextual Mismatch:** The closest punishment study uses third-party punishers, not peer punishment. Real-world evidence is primarily from kin-based small societies, which differ fundamentally from typical experimental PGG environments.
- **Ambiguity in Generalization:** Theory papers emphasize context-dependent mechanisms; empirical findings regarding punishment (especially negative or null effects) may not generalize to peer punishment in economic games.
- **Sparse Coverage of Design Parameters:** While some design dimensions are described, few are manipulated in ways relevant for causal inference regarding efficiency impacts of punishment.
- **No Quantitative Calibration:** There is no empirical basis in this set for specifying the magnitude or even the direction of the shift in efficiency due to enabling peer punishment.

**Conclusion:**  
While the literature provides context on how some game design features and institutional factors can affect baseline efficiency or the potential moderation of punishment effects, it offers almost no direct, empirical, or quantitative support for predicting changes in efficiency due to enabling peer punishment in PGG-like settings. Any predictions made on this basis would be extrapolative and highly uncertain.
