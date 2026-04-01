# 1) Evidence Base

The paper set is composed of 15 sources, with a balance between empirical laboratory experiments, observational/field studies, and theory or review papers. About half are directly experimental, with almost all experimental work focusing on non-payoff behavioral outcomes rather than efficiency or direct payoff. Theoretical and review papers dominate discussions about mechanism and contextual moderators, but empirical data directly linking punishment to efficiency or payoff in public-goods-game (PGG) contexts are sparse. The set uses a diversity of game types: some exact (PGG or very close variants), others adjacent (dictator, ultimatum, centipede, or real-world analogues). Measures of group payoff or efficiency are rare; most studies report on cooperation, punishment assignments, emotional responses, or context-dependent behavioral outcomes. As a result, while the evidence base is conceptually rich, it is narrow in directly supporting quantitative predictions of efficiency outcomes when punishment is enabled in PGGs.

# 2) Task Relevance

**pgg_or_variant:**  
- Most papers are either exact (classic PGGs) or adjacent (games structurally similar to PGGs, such as the centipede game or real-world collective action settings). About a third are entirely adjacent or use games that only overlap conceptually.  
- Relevance to PGG design and dynamics is highest in meta-analyses and some experimental/theoretical work (e.g., Spadaro et al., 2022; Capraro, 2024; Han et al., 2022), but weak or merely contextual in observational anthropology or real-world behavior papers.

**punishment_or_sanctions:**  
- Coverage is strong on the presence, type, and mechanisms of punishment or sanctions. Most sources directly address punishment, whether as experimental treatments or naturalistic behaviors, though a few focus more on mediation or reward systems.  
- Depth of analysis for punishment mechanics (cost, targeting, legitimacy) is variable, with theoretical treatments providing richer accounts than most experimental studies.

**efficiency_or_related_payoff_outcomes:**  
- Direct measurement of efficiency, group payoff, or welfare is rare (exact in Han et al., 2022; Nunney et al., 2022). Most outcome reporting is "adjacent" or "none": cooperation rate/change, punishment frequency, or qualitative impact. Only a minority report (adjacent-quality) payoff data, often as secondary outcomes, and typically not analyzed systematically to answer whether enabling punishment increases efficiency.

**Overall:**  
- The evidence set is highly relevant in terms of discussing punishment in PGG (or related) paradigms, but only weakly to moderately relevant in providing direct empirical efficiency outcomes needed for the downstream prediction task.

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes (Direct/Exact):**  
- Group efficiency, total payout, or social welfare: Only Han et al. (2022) (theory) and Nunney et al. (2022) (empirical, non-standard game) provide efficiency or closely related group payoff as primary outcomes.
- Some theoretical reviews summarize conditions under which payoffs or group welfare might rise or fall, but provide no empirical data (e.g., Wu et al., 2022; Frey & Burgess, 2023).

**Non-Payoff Behavioral Outcomes (Prevalent):**  
- Cooperation rate, punishment frequency/assignment, norm compliance, trust judgments, emotional responses, mediation/compensation practices, and expressions of guilt/shame are the main reported outcomes in experimental and field papers (e.g., Spadaro et al., 2022; Capraro, 2024; Guo et al., 2022; Gummerum et al., 2022).
- Many studies discuss the presence or mechanism of punishment/reward, or the behavioral strategies used, without relating these to group-level efficiency.

**Distinction:**  
- The literature overwhelmingly measures behavioral/psychological outcomes rather than the group payoff-based efficiency central to the prediction task.

# 4) Main Findings Relevant To Prediction

- **Enabling punishment generally increases cooperation rates** in PGGs and related games (Spadaro et al., 2022; Frey & Burgess, 2023). However, the translation of increased cooperation into higher efficiency is unclear, because most papers do not analyze payoff outcomes.  
- **Punishment can reduce efficiency** if it is misapplied, leads to retaliation, or is costly relative to its impact—especially in environments with noise or contested legitimacy (Wu et al., 2022; Han et al., 2022).  
- **Targeted and conditional punishment mechanisms (e.g., voluntary binding commitments)** maximize efficiency by avoiding the cost of over-punishment and only sanctioning true defectors (Han et al., 2022).
- **Reward mechanisms** may enhance or, in some settings, substitute for punishment, and can be more efficient in high-noise or low-legitimacy environments (Wu et al., 2022).
- **Communication/Chat and emotional signaling** (guilt/shame) can moderate the effect of punishment on subsequent cooperation and group payoff, in some cases substituting for punishment (Nunney et al., 2022).
- **Institutional trust and legitimacy** are critical: corrupt or unfair punishment reduces trust and can undermine the positive effects of punishment on group outcomes (Spadaro et al., 2023).
- **Cultural and social context** affects whether punishment is used at all and whether it targets group norm enforcement or dyadic restoration (Fitouchi & Singh, 2023; Singh & Garfield, 2022).

# 5) Prediction Guidance

- **Punishment is likely to increase efficiency only when**:
    - The cost/benefit ratio for punishment is favorable (i.e., the marginal impact on defectors exceeds total cost to punishers).
    - Punishment is perceived as legitimate and targeted at actual defectors.
    - Noise is low: punishment misfires and retaliation are minimized.
    - There is no over-punishment or excessive escalation.
- **When control-game efficiency is already high** (suggesting near-universal cooperation), enabling punishment may produce little gain and could even reduce efficiency if punishment is costly and unnecessarily applied (Han et al., 2022).
- **Game design features** such as chat/communication, visibility of actions, and presence of rewards can interact with (and sometimes substitute for) punishment effects, modifying efficiency outcomes (Nunney et al., 2022; Wu et al., 2022).
- **Contextual moderators** (culture, group identity, emotion, legitimacy of institutions) can strengthen, reverse, or otherwise qualify the efficiency impact of punishment (Guo et al., 2022; Spadaro et al., 2023).
- **If only control-game efficiency and design dimensions are available**, predictions about the effect of enabling punishment should be made cautiously, referencing the boundary conditions above and recognizing that most literature evidence addresses behavior, not efficiency per se.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- `player_count`, `num_rounds`, `all_or_nothing`, `chat`, `mpcr`, `punishment_cost`, `punishment_tech`, `reward_exists`, `reward_cost`, `reward_tech`, `show_n_rounds`, `show_other_summaries`, `show_punishment_id` are at least contextually discussed or manipulated in several papers (empirical and theory), though almost always in relation to behavioral outcomes, not efficiency.
- `punishment_exists` (vs. disabled) is universally discussed as a treatment but direct evidence of impact on efficiency is limited.
- `chat` and `communication` are shown as important moderators of cooperation and potentially efficiency (Nunney et al., 2022; Spadaro et al., 2022).

**Indirectly Informed/Contextually Discussed:**
- `default_contrib`: Framing effects are present in some experiments but not tightly linked to efficiency outcomes (Capraro, 2024).
- `show_punishment_id` and related transparency/trust features are contextually described as affecting legitimacy and group behavior (Spadaro et al., 2023).
- `reward_exists`, `reward_tech` etc., are discussed in relation to how the availability of alternative incentives/penalties can promote or undermine efficiency (Wu et al., 2022).

**Missing or Sparsely Addressed:**
- Few papers systematically test or quantify how efficiency effects of punishment interact with more than two or three game design dimensions in the same study. Cross-study synthesis is needed but limited by differences in methodology and reporting.
- Crucially, **systematic, multi-factor experimental evidence on how the full set of 14 dimensions collectively shape efficiency outcomes when punishment is enabled is lacking**.

# 7) Important Limitations

- **Scarcity of direct efficiency outcomes:** Very few papers directly report or analyze group efficiency or total payoff; most focus on behavioral responses.
- **Lack of parameterized, multi-factorial experiments:** Explicit tests of how the 14 design dimensions jointly affect efficiency with and without punishment are not available; evidence is fragmented.
- **Predominance of behavioral (not payoff) outcomes:** Most of the literature provides evidence or mechanisms for increased cooperation or norm compliance, but their translation to group efficiency is not straightforward.
- **Noise, legitimacy, and cultural/contextual factors are recognized but not quantified:** Such factors are reported as important but usually only in qualitative or contextual terms.
- **Variation in game structure and outcome reporting:** Many studies use adjacent or non-standard games, making generalization to classic PGGs and the specific prediction task uncertain.
- **Limited ability to extrapolate effect sizes:** Theory papers and qualitative reviews provide mechanistic expectation but not empirical magnitude, limiting the quantitative usefulness for downstream prediction models.
- **Field and anthropological work may not generalize:** Punishment in small-scale societies is often dyadic or restorative rather than group-norm-enforcing, and may not be analogous to laboratory PGG punishment dynamics relevant to efficiency prediction.

---
In summary, while the literature base provides strong evidence that punishment increases cooperation and identifies many contextual and design moderators, direct evidence for predicting the change in efficiency (payoff) from enabling punishment is very limited. Most findings should be considered as qualitative guides or cautionary boundaries rather than concrete quantitative predictors. The effect of enabling punishment on efficiency is highly contingent on the wider game design, institutional context, and social environment—parameters sparsely and unevenly addressed across the studies available.
