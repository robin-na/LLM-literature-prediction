# 1) Evidence Base

This paper set is relatively broad, with 210 papers spanning a diverse array of models, experimental lab and field studies, and theory (simulation, analytical models), mainly centered on public goods games (PGGs) and close variants. The majority of the most relevant evidence for the prediction task—efficiency outcomes under enabled vs. disabled punishment—comes from theoretical modeling and simulation, though there is substantial empirical support, particularly from lab experiments focusing on standard linear PGGs, centralized punishment, exclusion, and related designs. Notably, the set also covers variants such as collective-risk dilemmas, threshold public goods games (TPGGs), and numerous adjacent games (prisoner's dilemma, trust games, etc.), many of which provide only indirect support. Empirical evidence is strongest for standard linear and threshold PGGs with peer or centralized punishment; variants relying on social exclusion, reputation, or adaptive networks are prevalent but sometimes less directly mapped to the classic PGG structure.

Importantly, among the most directly relevant papers, there is a healthy mix of experiments and analytical models reporting on efficiency or closely related group payoff outcomes when comparing punishment-enabled and punishment-disabled conditions. However, a considerable number of papers—especially in adjacent or highly-structured variants—only report on cooperation rates or other behavioral metrics, which are not direct efficiency outcomes.

# 2) Task Relevance

**pgg_or_variant:**  
- **Exact relevance:** A substantial portion of the set focuses on standard linear PGGs or directly specified variants (e.g., Suleiman & Samid, Castillo et al., Jiao et al., Wang & Lv, Gao et al., Zhang et al., Botta et al., etc.), with empirical and simulation studies mapping onto the prediction task structure.  
- **Close or adjacent relevance:** Many studies extend to threshold PGGs, collective-risk resource dilemmas, exclusion games, and related n-player social dilemmas, which are structurally similar but sometimes involve additional dynamics (resource renewal, exclusion, insurance, etc.).  
- **Weak/none:** Adjacent models include prisoner's dilemma, trust games, and networked communication games, which are only weakly generalizable to the core PGG punishment/efficiency question.

**punishment_or_sanctions:**  
- **Exact relevance:** A core block of papers manipulate the presence, cost, and effectiveness of (peer/centralized/pool) punishment or sanctioning, and/or compare baseline (no-punishment) to punishment-enabled environments.  
- **Close relevance:** Some examine exclusion mechanisms as a form of sanction, or punishment-like mechanisms (e.g., loss of communication, social ostracism).  
- **Adjacent/weak:** Numerous studies use related incentive structures (rewards, redistribution) or focus on phenomena like network rewiring, reputation, or social feedback as indirect sanctions rather than direct punishment.

**efficiency_or_related_payoff_outcome:**  
- **Exact relevance:** There is strong representation of papers reporting average group payoff, net earnings, welfare, surplus, or group efficiency relative to the cooperative optimum (e.g., Suleiman & Samid, Castillo et al., Botta et al., Wang & Lv, Fang et al., Kol'veková et al., etc.).  
- **Close/adjacent relevance:** Many studies only report on cooperation rates, contribution sums, or strategy frequencies—behavioral outcomes that are not direct payoffs. Others discuss efficiency only as background or in a stylized fashion (e.g., in indirect reciprocity, trust games, or repeated PD).
- **None:** Some send only conceptual discussion or model mechanisms without reference to group-level payoff outcomes.

**Summary:**  
For the downstream task—predicting average efficiency under punishment from control efficiency and game dimensions—about 20–30 papers provide direct, robust, and relevant evidence. A much larger set provides indirect or mechanistic support, mainly on cooperation rates, while a significant fraction is not relevant for efficiency-based prediction of punishment effects in PGG contexts.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (central to prediction task):**  
  - **Efficiency** (defined as group payoff relative to the full-cooperation optimum): Directly reported or calculable in several key papers (e.g., Suleiman & Samid, Castillo et al., Kol'veková et al., Wang & Lv, Murase & Baek, Powers, Botta et al., etc.).
  - **Total group payoff / mean payoff / surplus:** Frequently reported. Sometimes mapped to efficiency, sometimes described as welfare/surplus.
  - **Probability/frequency of achieving a group threshold (e.g., in TPGGs), probability of full provision:** Sometimes reported as a proxy for welfare/surplus but only directly equivalent if the structure matches full cooperation payoff.
  - **Net profit / average earnings / average welfare:** Used in both empirical and theoretical papers as outcomes similar to efficiency but sometimes not directly normalized to the full-cooperation benchmark.

- **Non-payoff behavioral outcomes (should be interpreted separately):**  
  - **Contribution rate, cooperation rate, frequency of cooperators (or punishers/rewarders/etc.):** Ubiquitous, but distinct from efficiency. May be correlated but not identical due to the cost of punishment, incomplete participation, or second-order free-riding.
  - **Punishment frequency/intensity, antisocial punishment:** Occasionally measured, important as mechanisms but not efficiency per se.
  - **Norm compliance, reputation score, prevalence of excluders, alliance membership, etc.:** Too indirect for efficiency prediction.

**Distinction and caveat:** Payoff-based and contribution-based outcomes are often (but not always) positively correlated. Several papers demonstrate that high cooperation does **not** always map to high efficiency (especially when punishment is extremely costly, misdirected, or when second-order free-riding emerges).

# 4) Main Findings Relevant To Prediction

**Empirical and theoretical convergence:**  
- **Punishment increases efficiency in most standard PGGs:** The core empirical and theoretical evidence is that enabling (costly) punishment in a standard linear public goods game generally increases group efficiency/payoff relative to the un-punished (control) baseline, especially when the cost-to-effectiveness ratio of punishment is favorable and antisocial punishment is rare (Suleiman & Samid, Castillo et al., Wang & Lv, etc.).
- **Magnitude and robustness of gains:** The size of the efficiency gain is variable, and several studies note high variation or context dependence (Suleiman & Samid, Fang et al., Wang, Liu & Chen). Some note only moderate efficiency improvements, especially when cooperative norms are already strong or when sanctioning costs offset the gains from increased cooperation.
- **Institutional and structural moderators:**  
  - **Centralized vs. peer punishment:** Centralized (managerial) punishment is generally more robust to issues like retaliation and antisocial use but may not offer large added efficiency relative to peer punishment unless punishment is costless or highly efficient (Castillo et al.).
  - **Exclusion as punishment:** Exclusionary measures can be more effective than direct punishment in promoting both high cooperation and high efficiency under certain conditions (Liu & Chen, Fang, Perc & Xu).
  - **Graduated, probabilistic, or endogenous punishment:** Mechanisms that temper punishment frequency or scale it with offense magnitude (graduated, probabilistic) can achieve high cooperation and efficiency at lower cost (Couto et al., Kol'veková et al., Jiao et al.).
  - **Corruption, bribery, and disguise:** Ability for defectors to evade or corrupt punishment mechanisms can nullify or reverse efficiency gains (Liu, Chen & Szolnoki; Wang, Liu & Chen).
  - **Cultural/heterogeneity factors:** The presence of strong reciprocators vs. norm-keepers, or societal differences in punishment norms, modifies expected gains (Suleiman & Samid).

**Costs and design-moderated effects:**  
- **High punishment cost, low effectiveness:** If the punishment is too costly (relative to its effect on defectors), it can reduce net payoffs and even cause efficiency to drop below control levels, despite possibly higher cooperation rates (Kanitsar; Sui, Wu & Wang; Greenwood et al.).
- **Second-order free rider, antisocial punishment, and network effects:** Inefficiency can arise if punishment is misapplied (norm-keeper/antisocial) or if second-order free-riding is rampant. High network density may enable punishment to deter defection, but sparse networks or cyclical exchange structures may prevent efficiency gains (Kanitsar).

**Boundary and exception cases:**  
- **Weak, automatic, or imposed punishment (non-peer):** If punishment is automatic, applies only weakly (low impact per cost), or is distributed perverse (e.g., lowest contributor is always punished), efficiency gains are typically absent or negative (Yang et al.).
- **Resource/environmental limitations:** In resource-renewal (common-pool) games, even strong punishment does not guarantee efficiency if the underlying environment (growth rate, initial stock) cannot support sustainable cooperation—punishment may enforce cooperation but at the expense of overexploiting the resource (Chen & Szolnoki; Wang et al., 2021).
- **Threshold (all-or-nothing) PGGs:** Endogenous, low-cost, shared punishment mechanisms can result in large efficiency gains even if provision is not maximized, but the baseline level of cooperation, threshold size, and effectiveness all moderate the outcome (Kol'veková et al.).

**Comparison with rewards or other mechanisms:**  
- Some studies show that well-designed reward schemes, exclusion, or insurance mechanisms can substitute for punishment and—in certain settings—are more cost-effective, especially when baseline cooperation is high or the cost of maintaining the mechanism is low (Jiao et al., Chen & Chen, Kol'veková et al.).
- Others find that, where strong punishment is available and effectively targeted, punishment often outperforms reward alone (Zhang, An & Dong).

# 5) Prediction Guidance

**What the literature supports for downstream prediction:**  

- **Baseline (control) efficiency:** The efficiency of the control game (punishment disabled) is a reliable baseline from which to predict treatment efficiency, but the literature strongly demonstrates that the effect size of enabling punishment is highly variable and non-additive.
- **Key modifiers (use where dimension data are available):**
  - **Punishment cost and effectiveness:** Higher punishment effectiveness (impact per unit cost) predicts larger efficiency gains; low effectiveness or high cost can nullify or reverse the gain.
  - **Type of punishment (peer, centralized, exclusion, graduated):** Peer punishment generally increases efficiency, but centralized or exclusion-based punishment may yield additional benefits in specific structural contexts (e.g., when managing retaliation, second-order free-riding).
  - **Population structure/network topology:** Efficiency gains are strongest in well-mixed and dense sanctioning networks; sparse or cyclical structures (generalized exchange) may see little or no benefit.
  - **Group size and rounds:** Larger groups and more rounds generally support greater impact of punishment by providing more opportunities for norm enforcement (but with diminishing marginal returns and more room for antisocial punishment in some cases).
  - **MPCR, synergy, and threshold:** Higher marginal per capita return (mpcr) and appropriately calibrated thresholds can promote higher efficiency, especially when coupled with effective punishment; very low mpcr may require higher punishment for the same efficiency gains.
  - **Communication and summary/feedback structure:** The presence of communication channels or public feedback/signaling mechanisms can amplify the effect of punishment on efficiency.
- **Conditionality and moderation by population and culture:** The presence of strong reciprocators, willingness to punish, and social norms in the group (if known or proxied via population data) should be factored in as moderators.

**Quantitative mapping:**
- In the most well-specified cases, enabling medium- or high-effectiveness punishment raises efficiency by 5–30% relative to control efficiency (Suleiman & Samid, Kol'veková et al., Botta et al.), with diminishing returns as the control efficiency approaches the cooperative optimum.
- Very high cost or ineffective punishment can deliver zero or even negative net efficiency gains, sometimes despite high observed cooperation (Kanitsar, Sui et al.).
- Where corruption/bribery/disguise is possible and cost/effectiveness ratios are unfavorable, do not expect net efficiency gain (Liu, Chen & Szolnoki; Wang, Liu & Chen).
- In threshold variants, efficiency can rise dramatically if endogenous, shared, low-cost punishment is enabled (Kol'veková et al.), even with only moderate increases in provision rates.

**Where evidence is nonpayoff or only behavioral:**
- Use nonpayoff outcomes (contribution rate, cooperation frequency) as mechanistic or qualitative indicators of the likely direction of efficiency change, but do not assume proportional translation. Note that payoff-based outcomes may deviate when punishment is costly or misapplied.

# 6) Design Dimensions Highlighted Across Papers

**Dimensions directly and robustly informed:**  
- `player_count`: Widely studied, both in lab and theory. Larger N generally allows for stronger punishment effects, but also presents more scope for antisocial punishment and norm variation.
- `num_rounds`: Frequently specified; more rounds permit the buildup of norms and stable punishment-protected cooperation.
- `mpcr` (marginal per-capita return): Core parameter in almost all relevant models; higher mpcr supports greater efficiency gains from punishment.
- `punishment_cost`, `punishment_tech` (cost and effectiveness of punishment): Nearly all direct studies include these, with clear mapping to efficiency outcomes.
- `all_or_nothing`: Explored, particularly in TPGGs and exclusion variants; the structure affects the degree to which punishment promotes full provision.
- `reward_exists`, `reward_cost`, `reward_tech`: Often included; some analysis of reward vs. punishment or their synergy.
- `show_n_rounds`, `show_other_summaries`: Sometimes varied or noted, especially in experimental designs reporting on the impact of feedback or information.
- `chat`: Examined in several empirical studies, shown to amplify the effect of punishment in some (but not all) cases.

**Dimensions indirectly or contextually discussed:**  
- `default_contrib`: Framing effects are alluded to in a few experiments but rarely systematically manipulated.
- `punishment_tech` (impact per unit cost): Sometimes implicit (when cost and effectiveness are both reported).
- `show_punishment_id`: Sometimes implicit in lab studies, rarely varied as a core treatment variable.
- `punishment_tech`/`reward_tech`: Sometimes only the aggregate punishment/reward effect is reported, not split per unit.
- `chat`: Clearly manipulated in some experiments, absent in most lab studies.
- `all_or_nothing`: Distinction between binary (participation) vs. continuous contribution is sometimes made, but often standardized within a study.

**Dimensions sparsely or not informed:**  
- `default_contrib`: Rarely the focus of attention.
- `show_punishment_id`: Few studies analyze anonymity of punishers as a moderator.
- Details on user interface feedback (beyond general summary/information variables) are usually not reported systematically.

# 7) Important Limitations

- **Sparse direct empirical evidence for all design dimension combinations:** Most pay-off reporting studies focus on canonical parameterizations (e.g., 4- or 5-player, 10+ rounds, medium MPCR, peer punishment). Generalizing to rare combinations (e.g., large groups with very high punishment cost and low visibility) is under-informed.
- **Underreporting of net efficiency when punishment costs are high:** Many papers report only on behavioral outcomes (cooperation rates, contribution), which can mask situations where punishment costs offset or overwhelm the gain from increased contributions.
- **Adjacency of many models:** Numerous papers use adjacent games (PD, trust games, TPGGs with unique structures, or resource dilemmas) as mechanisms or comparative cases; findings may not transfer precisely to standard PGGs.
- **Insufficient attention to heterogeneity and cultural moderators:** Reporting on variation by cultural context, norm prevalence, and population-level willingness to punish is limited; predictions for multi-cultural or unfamiliar groups are less secure.
- **Breakdown at extremes:** Environments with very high rates of antisocial punishment, extreme corruption/bribery/disguise, or unusual incentive structures may not be well predicted by the literature.
- **Few field studies:** Real-world institutional variation, long time scales, and non-lab behaviors are underrepresented.
- **Reward vs. punishment tradeoffs:** While there is some theoretical and empirical comparison, direct comparisons of efficiency between punishment, reward, hybrid schemes, and other interventions are not always present, making it harder to benchmark punishment's efficiency impact relative to alternatives.

---

**In summary**, the literature very strongly supports that, *in standard PGGs and close variants*, enabling peer or appropriately designed centralized punishment generally increases group efficiency, especially when the cost-to-effectiveness ratio is favorable and when norms and population composition are supportive. The predicted increment to efficiency should be moderated by punishment cost, effectiveness, possible corruption or evasion, baseline efficiency, and the structure of interaction. The evidence base is robust for canonical cases, but prediction is weaker for extreme or uncommon design parameterizations, for social/cultural outlier populations, and for complex environmental or networked variants where efficiency may not translate directly from increased cooperation. Predictors should weight direct, efficiency-relevant evidence highest, treating cooperation rate and related non-payoff outcomes as supplementary moderators only when payoff-relevant data are lacking.
