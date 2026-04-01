# 1) Evidence Base

The paper set comprises 55 sources encompassing both theory and empirical research, including laboratory experiments, field experiments, simulations, and theoretical/mathematical modeling. A substantial minority of papers focus directly on efficiency or related payoff outcomes in public goods games (PGG) or very close variants, while a larger share provide mechanism, behavioral, or contextual findings from adjacent or only loosely related domains (e.g., trust games, partner choice, animal cooperation, norm enforcement). There is significant diversity: some papers offer formal structure and direct mapping to PGG prediction tasks, but others are illustrative, conceptually driven, or offer only indirect evidence.

There is a moderate but not exhaustive empirical base targeting the direct comparison of control (no-punishment) and treatment (with-punishment) efficiency in classic PGG formats. Many studies report only behavioral (e.g., cooperation rate, frequency of punishment) or mechanism outcomes without payoff analysis. Some important game design dimensions are well-covered, but many are either contextually discussed or omitted entirely (e.g., chat, show_punishment_id, reward dimensions).

**In summary:**  
- **Breadth:** The set is broad in concepts/mechanisms but narrow in direct, empirical efficiency comparisons for PGGs with vs. without punishment.
- **Empirical/Theory mix:** There is a healthy admixture, with theory papers sometimes providing directly relevant predictions for design-based efficiency changes (but often conditional on strong assumptions).
- **Suitability for prediction:** The set offers partial but incomplete support for downstream efficiency prediction from PGG design variables.

# 2) Task Relevance

**pgg_or_variant:**  
- A minority of papers (e.g., Dong et al., Podder et al., Molleman et al., Schroeder et al.) are of **exact** relevance, using classic PGG or close optional PGG paradigms.
- Many others are **close** or **adjacent**, focusing on related games (e.g., common-pool resource dilemmas, trust games, PD games, dictator games, animal analogs), making results less directly applicable for classic PGG predictions.

**punishment_or_sanctions:**  
- About half of the set directly model or empirically test **punishment or sanctioning** (**exact** or **close**), but many do so as one of several mechanisms, or with variations (e.g., institutional vs. peer punishment, second/third-party punishment, informal social sanctions).
- Several studies are **adjacent**, discussing related norm enforcement, exclusion, or reward mechanisms (but not classic costly punishment).

**efficiency_or_related_payoff_outcome:**  
- Only a few studies report **efficiency, group payoff, or welfare** as a **primary outcome** (**exact/close**, e.g., Dong et al., Okada et al., Powers & Lehmann, Bhui et al.).
- A much larger share focus on non-payoff behavioral outcomes (contribution rate, cooperation frequency, norm compliance) or antecedents to payoff (reputation, anger, emotional drivers).

**Summary:**  
- The literature is a mosaic: directly relevant, efficiency-focused studies are a minority; most evidence is indirect or mechanism-focused, and many studies lack direct efficiency comparisons between no-punishment and punishment conditions.

# 3) Outcomes Measured In The Literature

## Payoff-related Outcomes:
- **Efficiency, group payoff, welfare, surplus, or total earnings**: Directly measured in a few theory papers (Dong et al. 2019, Okada et al. 2015; Powers & Lehmann 2013; Bhui et al. 2019; Hooper et al. 2021), some field/experimental studies (Vollan et al. 2013; Fonseca & Peters 2021), and less frequently in lab experiments.
- Some empirical studies mention theoretical efficiency (e.g., Gatiso et al.), but don't report empirical changes.
- Several papers only infer potential efficiency effects based on changes in cooperation or contributions, not in actual payoffs.

## Non-payoff (Behavioral) Outcomes:
- **Contribution/cooperation rates, norm compliance, punishment frequency, retaliation rates, emotional responses, reputation, and social bonding**: These are the most common outcomes measured.
- Many experiments report only changes in these behavioral outcomes, leaving efficiency/earnings effects ambiguous due to the costliness of punishment and the possibility that higher cooperation does not offset punishment costs.

**Distinction:**  
- Behavioral improvement in contribution/cooperation cannot be directly equated to improved efficiency; costly punishment or imperfect targeting can result in unchanged or even lower group payoffs.

# 4) Main Findings Relevant To Prediction

**(A) Empirical-quantitative (direct/closely related):**

- **Institutional Reward vs. Punishment:**  
  Theoretical models repeatedly show that institutional (especially centralized or externally enforced) **reward** tends to be more robust for increasing group efficiency than punishment, particularly under bounded rationality/decision errors. Institutional punishment can even reduce group welfare if error rates or costs are non-trivial, especially outside finely tuned parameters (Dong et al., 2019).

- **Synergy with Reputation Mechanisms:**  
  Punishment alone in optional PGGs (and OPGG variants) typically **does not increase efficiency** and sometimes reduces it (especially if anti-social punishment is possible). Only when paired with effective **reputation mechanisms** (that distinguish defectors from loners) does a combination of punishment and reputation lead to reliably higher efficiency and population fitness (Podder et al., 2021).

- **Effect of Group Structure and Demography:**  
  Institutionalized punishment can increase group efficiency in structured populations, particularly when population structure supports repeated interaction (Powers & Lehmann, 2013; Roos et al., 2014). Efficacy is reduced by high migration or low benefit multipliers.

- **Effect of Punishment Cost & Technology:**  
  Both empirical and theoretical work highlight the central importance of the **cost-to-impact ratio**: punishment increases efficiency only when its behavioral effect per unit cost is high; otherwise, it backfires (Okada et al., 2015; Vukov et al., 2013).

- **Group Size:**  
  The effectiveness of punishment in sustaining cooperation/efficiency **declines with increasing group size** unless mechanisms for centralized or coordinated monitoring/punishment are present (Powers & Lehmann 2017).

- **Democratic vs. Imposed Sanctions:**  
  Sanctioning rules that are democratically chosen tend to outperform imposed rules in increasing cooperation (and likely efficiency), especially when resources are abundant; the effect is more muted under scarcity (Gatiso et al., 2015).

**(B) Mechanism & Contextual Findings (indirect):**

- **Nonlinear or Context-dependent Effects:**  
  The efficiency outcome of enabling punishment is strongly **moderated by power asymmetry**, group norm alignment, presence of counter-punishment or corruption, and baseline norm compliance (Phillips, 2018; Vollan et al., 2013).

- **Reward/Second-order Incentives:**  
  Efficiency gains are not achieved in the long run by first-order punishment alone; robust improvement requires second-order incentives for rewarding contributions (Okada et al., 2015).

- **Communication, Chat, and Reputation:**  
  Communication can substitute for punishment in sustaining cooperation/efficiency, but the two are not always additive. Gossip, honest signaling, and observability can each increase efficiency in the absence of costly punishment (Jolly & Chang, 2021; Roberts, 2020).

- **Behavioral versus Efficiency Effects:**  
  Repeated findings that increased cooperation does not universally translate into improved efficiency; heavy or misapplied punishment can reduce total payoffs, particularly in well-mixed, large, or error-prone settings.

# 5) Prediction Guidance

**Core guidance:**  
- **Enabling punishment in classic PGG-like environments increases efficiency only under specific conditions:**  
  - **Low punishment cost, high impact**: Cost-effective peer or institutional punishment is a prerequisite for net efficiency gain; high punishment cost can erase cooperation gains through reduced group payoff (Okada et al., 2015; Vukov et al., 2013).
  - **Small or structured groups**: Punishment is more effective at increasing efficiency in small or structured groups with repeated interactions; effectiveness declines with group size or with mixing/randomization (Powers & Lehmann, 2017; Roos et al., 2014).
  - **Presence of reputation or coordination mechanisms**: Efficiency gains are greatest where punishment combines with effective reputation mechanisms, peer information, or coordination (Podder et al., 2021).
  - **Norm alignment and democratic legitimacy**: Rule/sanction alignment with group norms (and democratic selection) moderates positive efficiency effects; imposed or norm-misaligned sanctions may crowd out cooperation and harm efficiency (Gatiso et al., 2015; Vollan et al., 2013).
  - **Decision errors and anti-social punishment**: If players are error-prone or anti-social punishment exists, enabling punishment can lower efficiency (Dong et al., 2019).
  - **Baseline efficiency**: If the no-punishment control already exhibits high efficiency, there is little room for improvement by enabling punishment; with low control efficiency, punishment's marginal effect is highly variable and context-sensitive.

**Control outcomes matter:**  
The average efficiency of the control condition sets a "base rate"—if already near maximum, enabling punishment likely has minimal or negative marginal effect. If control efficiency is low, design dimensions (punishment cost, group size, etc.) plus contextual mechanisms (reputation, information) moderate the likely treatment effect's magnitude and direction.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**  
- **player_count**: Frequently manipulated or modeled; smaller/structured groups facilitate effective punishment (Powers & Lehmann, 2017; Okada et al., 2015).
- **num_rounds**: Explored in repeated game settings; more rounds enable threats of punishment to have cumulative effects.
- **mpcr (marginal per-capita return)**: Central to all formal PGG theory work (Dong et al., 2019; Powers & Lehmann, 2013).
- **all_or_nothing, punishment_cost, punishment_tech**: Directly varied in multiple papers (Dong et al., 2019; Okada et al., 2015; Vukov et al., 2013).
- **reward_exists, reward_cost, reward_tech**: Explored mainly in theoretical work as contrast/combination mechanisms (Dong et al., Okada et al.).
- **show_other_summaries, show_n_rounds, show_punishment_id (information/visibility)**: Sometimes included, often contextually discussed (Jolly & Chang, 2021; Roos et al., 2014).

**Indirectly Informed/Contextually Addressed:**  
- **chat (communication)**: Found to substitute for punishment in some cases; rarely manipulated alongside punishment interventions.
- **default_contrib**: Framing and default options discussed rarely and incompletely.
- **punishment_magnitude**: Sometimes folded in as part of cost-to-impact ratios, but not always isolated as an independent dimension.

**Missing/Sparse Dimensions:**  
- **reward_cost, reward_tech, reward_magnitude**: Infrequently manipulated or directly compared to punishment effects.
- The simultaneous influence of multiple dimensions is rarely tested empirically.

# 7) Important Limitations

- **Scarcity of Direct Efficiency Data:**  
  Few studies report direct, experimental efficiency comparisons (group payoff relative to full cooperation) with and without punishment in standard PGGs.
  
- **Overreliance on Behavioral Outcomes:**  
  Many papers focus on cooperation/contribution rates rather than on holistic group payoff, leading to ambiguity about net efficiency effects due to costs of punishment.

- **Context Sensitivity:**  
  Results are highly sensitive to the social, cultural, and institutional context (e.g., role of reputational mechanisms, group norms, third-party punishment legitimacy, anti-social punishment).

- **Partial Coverage of Dimensions:**  
  No single study or even cluster of studies systematically varies all 14 prediction-relevant design dimensions. Some (e.g., chat, default_contrib, information visibility) are often left untested.

- **Theoretical Assumptions:**  
  Many theory papers require strong, sometimes implausible, assumptions (e.g., error-free decision-making, exogenous norm stability, unlimited cognitive capacity) for positive punishment effects.

- **Adjacent Domains/Ecological Validity:**  
  Some adjacent or loosely related studies use animal behavior, trust games, or common-pool resource settings that do not match the PGG payoff structure, technology, or group dynamics.

- **Ambiguity and Mixed Findings:**  
  Several papers show that punishment can both increase or decrease efficiency depending on parameter regimes—high punishment cost, presence of anti-social punishment, or misaligned group norms can reverse positive effects.

---

**In sum:** The literature provides useful qualitative and some quantitative guidance about dimensions under which enabling peer punishment in PGG-like environments will increase, decrease, or leave unchanged group efficiency. The most robust positive effects occur with low-cost, high-impact punishment in small or structured groups, especially with supportive reputation and communication mechanisms. However, the range of outcomes is broad and context-sensitive. Many predictive dimensions remain underexplored; predictions based solely on this literature should be made with pronounced caution and explicit acknowledgment of limitations.
