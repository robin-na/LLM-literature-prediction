# 1) Evidence Base

The current literature set is composed of both theoretical and empirical works, with an emphasis on theoretical and conceptual papers and a minority of empirical laboratory experiments or field observations. Of the nine papers, only two are empirical (one lab experiment in a classic public goods game and one observational study in a library commons), with the rest being theoretical or conceptual analyses. The majority of the theoretical works focus on mechanisms for generating cooperation—including various forms of punishment, exclusion, and norm-based solutions—rather than reporting experimental or simulated outcomes for the specific prediction task. As a result, while the set is moderately broad in its approach to sanctions and collective action problems, it is narrow and indirect with respect to predicting *efficiency outcomes specifically* from game design features and control-game efficiency baselines.

# 2) Task Relevance

**pgg_or_variant:**  
- **exact:** 3 papers (Engel, 2019; Zhu et al., 2020; Liu et al., 2019) use or analyze public goods games directly.
- **close/adjacent:** 4 papers (Pedroso, 2021; Steimanis et al., 2020; Jagers et al., 2020; Albergaria & Saes, 2018) study close variants or adjacent collective action problems (e.g., threshold PGG, spatial PD, commons).
- **weak/none:** 2 papers (Handfield & Thrasher, 2019; Heath & Rioux, 2018) are mainly theoretical and discuss cooperation more abstractly.

**punishment_or_sanctions:**  
- **exact:** 4 papers (Engel, 2019; Zhu et al., 2020; Steimanis et al., 2020; Albergaria & Saes, 2018) manipulate or analyze punishment or sanctioning directly within the game.
- **adjacent:** 3 papers (Liu et al., 2019; Pedroso, 2021; Jagers et al., 2020) touch on alternative mechanisms (exclusion, third-party enforcement) or do not directly operationalize punishment as in classic PGGs.
- **none/weak:** 2 papers provide only broad conceptual coverage.

**efficiency_or_related_payoff_outcome:**  
- **exact:** 1 paper (Liu et al., 2019) models payoff/efficiency explicitly.
- **adjacent:** 3 papers (Engel, 2019; Zhu et al., 2020; Steimanis et al., 2020) discuss payoffs but do not report efficiency as a main outcome (focus is on cooperation/contribution/frequency).
- **none/weak:** The remainder discuss payoff very little or not at all.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (efficiency, group payoff, welfare, surplus, total earnings):**  
  - *Directly measured/reported in detail:* Only Liu et al. (2019) (theory: efficiency/payoff in PGG with exclusion).
  - *Descriptively referenced or otherwise adjacent:* Engel (2019) reports total earnings descriptively but focuses on contribution behavior; other empirical/theoretical papers mainly discuss behavioral outcomes.
- **Non-payoff behavioral outcomes (contribution rate, cooperation rate, punishment frequency, norm compliance):**  
  - Most studies, including Engel (2019), Zhu et al. (2020), Steimanis et al. (2020), and Pedroso (2021), focus on cooperation and strategy frequencies (e.g., fraction cooperating, punishment assigned), rather than efficiency or group payoff.

# 4) Main Findings Relevant To Prediction

- **Peer vs pool punishment:**
  - *Peer punishment* is generally more effective at increasing cooperation than centralized/pool punishment in spatial or networked PGG variants (Zhu et al., 2020), but this is measured in behavioral terms, not direct efficiency (payoff) terms.
  - *Prosocial pool exclusion* (a form of institutional sanctioning) can robustly increase efficiency, even more than punishment, in theoretical infinite-population models (Liu et al., 2019).

- **Feedback and transparency:**
  - Full transparency (detailed individual-level feedback about contributions and punishment) can *reduce* cooperation in a standard lab PGG with centralized punishment, contradicting deterrence expectations (Engel, 2019). This suggests possible *negative or null effects on efficiency* of punishment when feedback is highly individualized, but evidence is on contribution, not direct efficiency.

- **Conditionality and environment:**
  - Conditional punishment (punishing others with opposite strategies *if one's own payoff is below average*) increases cooperation rates in spatial dilemmas (Steimanis et al., 2020), but efficiency/total payoff is not reported.
  - Lack of information or environmental harshness can promote "redundant" cooperation without punishment (Pedroso, 2021), indirectly suggesting the role of information in moderating cooperation (but not reporting efficiency).

- **Scale and institutionalization:**
  - Larger-scale collective action settings make informal (peer) punishment less effective; formalized sanctions may become necessary (Jagers et al., 2020).

- **Sanction types and externalities:**
  - Sanction type (monetary vs non-monetary) creates distinct externalities in commons resource use but payoff efficiency is not measured (Albergaria & Saes, 2018).

- **Mechanism-based critiques:**
  - Some philosophical theory undermines the plausibility of greenbeard-like mechanisms for large-scale cooperation via punishment (Heath & Rioux, 2018), introducing skepticism about generalizability.

# 5) Prediction Guidance

- **Best-informed guidance:**  
  - When *prosocial exclusion* (institutionalized enforcement, not peer punishment per se) is available, efficiency increases substantially and persistently in theory models, especially under well-mixed/infinite-population assumptions (Liu et al., 2019). This may not generalize to lab settings with finite groups, but it indicates that *replacing or augmenting peer punishment with exclusion or institutional punishment* may be optimal for efficiency.

- **Empirical evidence for punishment per se:**  
  - Enabling punishment does not guarantee efficiency gains: high transparency and individualized feedback about punishment can backfire and reduce cooperation, thus potentially reducing efficiency, especially when baseline (control) contributions/efficiency are moderate or high (Engel, 2019).

- **Peer punishment effectiveness:**  
  - Peer punishment increases cooperation more effectively than pool punishment in spatial PGGs (Zhu et al., 2020), though real efficiency effects are not reported. Predicting efficiency gains based solely on higher cooperation rates is uncertain due to the cost of punishment reducing net payoffs.

- **Conditional punishment:**  
  - Conditional forms of punishment (where agents only punish if their payoff is low) increase cooperation in spatial dilemmas, but there is no direct evidence for corresponding gains in efficiency (Steimanis et al., 2020).

- **Caveat for scaling up:**  
  - Increases in player count and complexity (scale) may decrease the effectiveness of informal (peer) punishment for sustaining efficiency (Jagers et al., 2020).

- **Indirect and high-level context:**  
  - Other works contribute only theoretical context or critique, and should not be weighted for numeric prediction.

**In sum:** For predicting treatment efficiency when enabling peer punishment, one should be cautious: empirical evidence suggests effects can be negative or null if transparency is high (Engel, 2019); theory suggests institutional exclusion (not peer punishment) is robustly positive for efficiency (Liu et al., 2019); and evidence for peer punishment increasing group efficiency rather than cooperation per se is mostly indirect. Predictive modeling should thus make use of control-game (no punishment) efficiency as a benchmark but should adjust expectations downwards if feedback is highly individualized or up only if exclusion (not peer punishment) is implemented.

# 6) Design Dimensions Highlighted Across Papers

- **Directly informed:**  
  - `player_count` (Engel, Zhu, Liu, Pedroso, Jagers)
  - `num_rounds` (Engel, Zhu, Liu)
  - `all_or_nothing` (Engel, Zhu, Liu, Pedroso, Steimanis)
  - `mpcr` (Engel, Zhu, Liu, Pedroso)
  - `punishment_cost` (Engel, Zhu, Steimanis, Albergaria)
  - `punishment_tech` (Zhu, Steimanis, Albergaria)
  - `chat` (Engel, Jagers)
  - `show_other_summaries` (Engel, Pedroso, Jagers)
  - `show_punishment_id` (Jagers)
- **Indirectly/contextually discussed:**  
  - `reward_exists`, `reward_cost`, `reward_tech` (rarely manipulated or mentioned; not focal)
  - `show_n_rounds` (rare mention)
  - `default_contrib` (discussed in framing/assurance but not manipulated)
- **Effectively missing:**  
  - Notably absent are systematic manipulations or empirical results for `reward_exists`, `reward_cost`, `reward_tech`, `reward_magnitude`, and rarely, `default_contrib` and `show_n_rounds`.
  - Nearly all empirical efficiency evidence is for “peer punishment enabled” versus “baseline,” not in parametric space spanning the above 14 dimensions.

# 7) Important Limitations

- **Scarcity of direct efficiency evidence:**  
  - Only one paper directly reports efficiency or group payoff as the primary outcome in a PGG variant (theory, with prosocial exclusion, not peer punishment) (Liu et al., 2019).
  - Most empirical results, including the key lab experiment (Engel, 2019), report behavioral outcomes (contributions, cooperation), making translation to efficiency ambiguous—especially since efficiency can decrease if punishment is overused.

- **Ambiguity in punishment effects:**  
  - In important setups (e.g., high transparency), enabling punishment can reduce cooperation (Engel, 2019), and thus may reduce or fail to increase efficiency.

- **Limited parameter coverage:**  
  - Many game design dimensions critical for prediction (e.g., reward mechanisms, default contribution, full punishment tech variation) are not systematically manipulated or are missing altogether.

- **Generality of theory:**  
  - The most optimistic efficiency results for punishment (actually for exclusion) rest on strong theoretical assumptions (infinite populations, deterministic replicator dynamics) and may not apply to small-N lab or field settings.

- **Lack of reward mechanism exploration:**  
  - No paper in the set systematically studies the interaction between punishment and reward, a potentially important moderator of efficiency effects.

- **Disagreement and context dependence:**  
  - The prediction task is complicated by context-dependent findings: punishment can increase, decrease, or have nil effect on efficiency depending on feedback and baseline cooperation.

- **Scarce multisource empirical confirmation:**  
  - Cross-paper empirical replication for any given dimension or result is lacking, so generalizability is uncertain.

**Overall, this paper set provides important theoretical caution and mechanism insights but is limited in its empirical, dimension-level coverage for predicting treatment efficiency in public goods game–like designs with punishment.**
