# 1) Evidence Base

The evidence base consists exclusively of theoretical and simulation-based papers (no empirical or lab/field experimental studies) addressing public goods games (PGGs), their variants, and closely related multi-player social dilemma environments. Out of 327 papers surveyed, there is a dense, detailed cluster of papers providing exact or close theoretical analyses of PGGs with and without peer or institutional punishment, often reporting on group efficiency or payoff-based outcomes. The literature is broad in its exploration of mechanisms (peer, pool, institutional, networked, and adaptive punishment), inclusion of both punishment and reward, and consideration of various game design dimensions (group size, number of rounds, cost/effectiveness of punishment, network structure, etc.). However, all studies are model-based or simulation-driven, and the coverage of empirical parameterizations is absent. No primary data is available, and all findings are rooted in mathematical or agent-based models.

# 2) Task Relevance

**PGG or Variant:**  
- Relevance is **exact** for the dense core of theoretical/simulation models focused directly on PGGs or voluntary/optional PGGs (e.g., Powers, 2018; Wu et al., 2014; Sun et al., 2025; Levine & Modica, 2016).
- **Close** relevance appears for some CPR (common-pool resource), N-person snowdrift, and trust games where group payoff is the key outcome, and the strategic structure closely parallels PGGs.
- **Adjacent** or **weak** for dyadic (PD) studies, bargaining games, and certain evolutionary/organizational models.

**Punishment or Sanctions:**  
- **Exact** relevance when costly, peer, pool, institutional, or adaptive punishment is systematically manipulated as a game design dimension (majority of theoretical PGG models).
- **Close/adjacent** for studies using alternative sanctioning mechanisms (ostracism, social exclusion) or where punishment is not always the main or only intervention (e.g., reward and punishment combined), but whose mechanisms map to efficiency impacts analogous to punishment.

**Efficiency or Related Payoff Outcome:**  
- **Exact** in many models, with group efficiency, total group payoff, or explicit welfare/surplus as reported main outcomes.
- **Close/adjacent** where reported outcomes are average payoff, prevalence of full cooperation (proxy for maximum efficiency), or stochastic stability of cooperative equilibria.
- **Explicit distinction** is made in the corpus between payoff (efficiency) outcomes and behavioral outcomes (contribution rate, punishment frequency, cooperation rate). Many papers report both, but not always with equal weight.

# 3) Outcomes Measured In The Literature

**Payoff-related Outcomes (Relevant):**
- Group efficiency: Ratio of total realized group payoff to the full-cooperation benchmark.
- Aggregate/group/mean payoff: Direct measurement of welfare, coins, or collective earnings.
- Surplus, welfare, or maximum group fitness in evolutionary models.

**Non-payoff Behavioral Outcomes (Important but Distinct):**
- Contribution/cooperation rates: Share of cooperators, average contribution per round.
- Frequency of punishment/reward: Rate at which punishment is meted out.
- Prevalence or abundance of punishment/cooperation types.
- Norm compliance, ostracism occurrence, or dynamics of strategy clusters.

**Notably, some papers only indirectly inform on efficiency by discussing equilibrium selection, or by mapping parameter regimes to the likelihood of being in an 'efficient' (all-cooperate) versus 'defection' (low-efficiency) state. A subset of the literature (especially adjacent or weakly-relevant papers) reports only on behavioral outcomes, not on any payoff-based measure.**

# 4) Main Findings Relevant To Prediction

- **Punishment generally increases efficiency over control (no-punishment) baselines:** The overwhelming signal across theoretical and simulation models is that enabling peer or institutional punishment, when it is not excessively costly and is sufficiently effective, raises efficiency/payoff, especially in environments where control games see low efficiency due to widespread defection (e.g., Powers, 2018; Wu et al., 2014; Sun et al., 2025; Levine & Modica, 2016; Wang et al., 2010; Dejong et al., 2008).
- **Magnitude of efficiency gain depends on key design parameters:**
    - **Punishment cost and effectiveness:** Lower cost and higher punishment impact per unit cost increase efficiency gain; if cost is too high or punishment is ineffective, improvement can be small or negative (Wu et al., 2014; Zhuang et al., 2012; Sun et al., 2025; Wang, Z. et al., 2010). Theoretical models often express explicit thresholds.
    - **Marginal per-capita return (mpcr):** Punishment effects are largest at low mpcr, where defection would otherwise dominate, and strongest where achieving cooperation is hardest by incentives alone (Wu et al., 2014; Zhuang et al., 2012; Zhuang et al., 2012; Sigmund et al., 2011).
    - **Player count/group size:** Larger groups can sustain higher efficiency with punishment, but only if the punishment regime scales (Levine & Modica, 2016; Sui et al., 2018). Some models note diminishing returns or the need for institutional solutions as group size increases.
    - **Number of rounds:** More rounds (repeated play) increase the opportunity for punishment to work via deterrence and thus improve efficiency (Eldakar et al., 2013; Congleton & Vanberg, 2001).
    - **Punishment technology/identification:** Effective monitoring, detection, and assignment of punishment (show_punishment_id) increase positive efficiency effects, especially for institutional punishment.
    - **Institutional versus peer punishment:** Institutional (tax-based or centralized) punishment mechanisms can achieve higher and more stable efficiency and may even outperform peer punishment, especially when second-order free riding is addressed (Sigmund et al., 2011; Yao & Chen, 2014; Yang & Yang, 2024).
    - **Network and spatial structure:** Small-world and regular lattice structures that enable local clustering or adaptive punishment can increase the average group efficiency from punishment relative to well-mixed settings (Cui et al., 2022; Yao & Chen, 2014).
    - **Presence of reward mechanisms:** When both punishment and reward are present, efficiency is typically highest with an optimal mix. Excessive punishment without reward or vice versa is suboptimal (Cong et al., 2016; Yang & Yang, 2024). Simultaneous availability of both can be robust, but reward often outperforms punishment for equivalent cost (Zhuang et al., 2012).
    - **Balance between conditional altruism/reciprocity and punishment:** Social preferences moderate the impact: high unconditional altruism may dampen both the need for and the willingness to punish, thereby lowering the efficiency gain (Hwang & Bowles, 2012).
    - **Existence of anti-social punishment, second-order free-riding, cost of monitoring, delays, and disguise:** These can undermine the efficiency benefit of punishment either by reducing its use or by allowing defectors to escape consequences (Wang, Q. et al., 2020; Shen et al., 2022).
- **Threshold and non-monotonic effects:** There is often a threshold punishment cost or punishment effectiveness below which punishment has little or no effect, and above which full cooperation (maximum efficiency) is stable; increasing punishment beyond this point may reduce efficiency due to costs (Sun et al., 2025; Sigmund et al., 2011).
- **Pool (institutional) versus peer punishment:** Pool punishment with second-order punishment (punishing non-punishers) is reliably more stable and effective in raising efficiency, but may require mechanisms to avoid anti-social punishment or excessive costs (Sigmund et al., 2011; Sasaki, 2014).
- **Parameter-specific and context-dependent exceptions:** Some models document cases where enabling punishment does not increase, or even reduces, efficiency—e.g., if altruism is high (Hwang & Bowles, 2012), anti-social punishment is prevalent (see discussion in Sylwester et al., 2013, review), defectors can disguise cheaply, or when punishment/intervention is too weak/too strong (Sun et al., 2024; Sui et al., 2018; Whitmeyer, 2004).

# 5) Prediction Guidance

## How this literature should inform prediction of treatment efficiency from game design dimensions plus control efficiency:

- **Base expectation:**  
  For most well-parameterized PGGs with controlled punishment design, *enabling peer or institutional punishment will increase efficiency above the control (no-punishment) baseline,* with the effect being strongest when the control efficiency is low (i.e., widespread defection).

- **Key points for prediction:**
    - **Punishment cost (punishment_cost):** Strong negative interaction. Lower costs → higher efficiency gains; high costs can negate benefits or even reduce efficiency.
    - **Punishment effectiveness (punishment_tech):** Only when punishment sufficiently outstrips its cost does efficiency increase; explicit analytic thresholds are often provided.
    - **Group size (player_count) and number of rounds (num_rounds):** Larger groups/longer games may require institutional punishment for full efficiency gains or are otherwise more vulnerable to collapse without structured punishment.
    - **MPCR (mpcr):** Effect size of efficiency gain from punishment is greatest at low mpcr values.
    - **All-or-nothing contributions (all_or_nothing):** Effects are preserved in all-or-nothing setups, but thresholds for stability may be tighter (Archetti & Scheuring, 2011).
    - **Reward mechanisms (reward_exists, reward_cost, reward_tech):** The presence and effectiveness of rewards can increase efficiency further and sometimes outperform punishment; the optimal is a balanced mix (Cong et al., 2016; Yang & Yang, 2024).
    - **Network structure/dynamics:** Small-world and regular networks facilitate higher efficiency with punishment; in random or highly connected networks, punishment is less effective, and efficiency gains diminish (Cui et al., 2022).
    - **Punishment administration (show_punishment_id, institutional vs. peer):** Institutional punishment with identification/monitoring is more stable and effective for group efficiency; peer punishment is effective but more vulnerable to undermining by second-order free-riders or anti-social punishment.
    - **Social preference context (default_contrib, chat, show_other_summaries):** High altruism may reduce efficiency gains from punishment; communication and visibility can increase or substitute for punishment’s effect.
    - **Control efficiency:** Because efficiency frequently rises to the cooperative maximum when conditions for effective punishment are met, *the magnitude of the treatment effect is inversely related to the control efficiency*: the lower the baseline, the greater the potential gain.

- **Caveats:**
    - If punishment cost is high, or mechanisms for enforcement are weak or mis-targeted, enabling punishment can yield little or even negative efficiency change (Sun et al., 2024; Hwang & Bowles, 2012).
    - Reward (when available) may, for equal cost, be more effective than punishment or required for optimal efficiency (Zhuang et al., 2012; Cong et al., 2016; Yang & Yang, 2024).
    - Purely peer punishment can be unstable or subject to collapse, especially in large groups or when second-order free-riding is present (Sigmund et al., 2011).
    - Effects may be thresholded: below a minimum effective punishment, very little change; above, a sharp switch to high efficiency (Sun et al., 2025; Huang et al., 2024).
    - Social context, communication (chat), and visibility (show_other_summaries) can augment or, in some cases, substitute for punishment’s effect on efficiency.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**  
- **player_count** (all): The role of group size is central; most models vary or specify group size in their analysis.
- **num_rounds**: Repeated play and its impact on efficiency are extensively considered.
- **mpcr**: Almost universally analyzed; models often report effects at different marginal return values.
- **all_or_nothing**: Explicitly manipulated in several models (threshold PGGs, N-person snowdrift).
- **punishment_cost & punishment_tech**: Cost and technological parameters for punishment are a primary axis for theory and simulation, with explicit thresholds often reported.
- **reward_exists, reward_cost, reward_tech**: Many studies examine the interplay between punishment and reward, with design implications mapped to efficiency gains.
- **punishment_exists (prediction variable):** The presence/absence and form of punishment are universally central to the theory base.

**Indirectly Informed:**  
- **chat, default_contrib, show_other_summaries, show_n_rounds, show_punishment_id**: These are less consistently analyzed. Institutional models sometimes consider information flow, communication, and anonymity, but not always as independent moderators.
- **punishment_tech**: Broadly considered (peer vs. institutional, adaptivity, monitoring), but with less granularity for identity and visibility controls.

**Only Contextually Discussed or Sparse:**  
- Framing variables (default_contrib), optional participation, identity revelation, round counting, and chat are considered peripherally or in broad discussion, but not as systematic, parameter-swept variables.

**Effectively Missing:**  
- Empirical calibration for the exact magnitude of effects; no direct mapping to human-subject experimental parameterizations or observed treatment effects.
- Very sparse or absent discussion of behavioral details such as emotion, cognitive load, within-game learning, or the effect of defaults on efficiency (these are sometimes seen in adjacent or only contextually relevant papers).

# 7) Important Limitations

- **No empirical/laboratory studies:** All findings are from theory and simulation—no quantitative treatment effects as observed in lab or field PGGs.
- **Behavioral realism is limited:** Human behavior may deviate systematically from the single-parameter, equilibrium-based, or fully rational model assumptions, especially in the use and perception of punishment.
- **No direct effect size estimates:** While directionality is strong and thresholds are well characterized, the quantitative size of treatment-control efficiency changes in real-world or lab settings is uncalibrated.
- **Limited exploration of certain dimensions:** Chat, framing (default contributions), detailed information structure, and optional participation are under-explored as moderators.
- **Cultural and contextual moderators:** Some models discuss the potential for anti-social punishment or cultural variance but lack direct evidence.
- **Reward mechanisms:** While some theorize about or include reward, far fewer analyze its effect as systematically as punishment, especially in mixed or hybrid settings.
- **Static vs. dynamic environments:** Most models are equilibrium-focused; the dynamics (e.g., how quickly efficiency rises post-punishment) and robustness to path dependence or initial conditions receive less systematic attention.
- **Complexity and non-monotonicity:** Some models highlight that the effect of punishment is non-monotonic (can backfire or have threshold/catastrophic effects), complicating straightforward prediction.
- **Lack of explicit mapping to all prediction dimensions:** While player_count, mpcr, num_rounds, and punishment parameters are extensively covered, dimensions such as chat, default_contrib, or show_punishment_id are mostly neglected or only treated as contextual background.

---

**Summary:**  
The literature base provides strong, consistent, theoretical support for a positive effect of enabling peer or institutional punishment on efficiency in control-to-treatment PGG-like predictions, conditional on the design dimensions of punishment cost, effectiveness, group size, mpcr, and to some extent, institutional structure and network topology. However, no empirical effect sizes or human data are available; therefore, predictions about the magnitude, rather than the direction or critical thresholds, should be made with caution. Several design dimensions (notably chat, default framing, identity, and some information presentation) are underexplored, and real-world moderators such as anti-social punishment or cultural specificity are not fully addressed.
