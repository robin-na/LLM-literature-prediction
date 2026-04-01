# 1) Evidence Base

The evidence set consists exclusively of **theoretical papers** and reviews (n=79), without direct empirical or experimental data. These works span evolutionary game theory, replicator dynamics, agent-based models, and formal evolutionary analyses, with a strong emphasis on mechanism, conditions, and qualitative/parametric predictions. The paper set is **broad in its coverage of theoretical mechanisms** and moderately broad in its coverage of game design dimensions but is strictly **narrow regarding empirical calibration**—there are no laboratory or field experimental results included. The set covers a wide range of public-goods-game (PGG) models, institutional structures, punishment forms (peer, pool, exclusion, graduated), and adjacent game structures (e.g., common-pool resources, repeated games, networked populations).

# 2) Task Relevance

Assessment on the three key dimensions:

- **pgg_or_variant**:  
  - Label: **exact** for roughly half the papers, with the remainder being **close** or **adjacent** (resource games, repeated PD with public-good features).
  - Most models directly analyze standard PGGs or voluntary/threshold forms; a significant portion examine close conceptual relatives.

- **punishment_or_sanctions**:  
  - Label: **exact** for many (peer, pool, social exclusion), **close** for some (institutional, reward-based, reputation loss), and **adjacent** for works with softer or indirect enforcement.
  - Mechanisms include peer punishment, institutional/pool punishment, social exclusion, and hybrid mechanisms.

- **efficiency_or_related_payoff_outcome**:  
  - Label: **exact** for many theoretical works (explicit analysis of efficiency, group payoff, welfare, surplus), **close** for others relying on proxies (cooperation rate as predictor of efficiency), and **adjacent** or **weak** for purely behavioral outcome models.
  - A nontrivial portion directly analyze group efficiency or provide explicit mappings from cooperation to payoff.

**Summary**:  
The literature is **strongest for theoretical prediction of efficiency effects** given a specified PGG model and design features; less so for empirical effect sizes or patterns across different laboratory designs. Outcome mapping to efficiency is sometimes indirect, especially where only cooperation rates or evolutionary stability are analyzed.

# 3) Outcomes Measured In The Literature

**Payoff-Based Outcomes (Relevance: prediction task):**
- **Exact Payoff/Efficiency**: Many theoretical models provide group efficiency, average group payoff, welfare, total earnings, or explicit formulas mapping group strategies to payoffs (e.g., (Adami et al., 2016); (Dercole et al., 2013); (Sasaki & Uchida, 2013); (Lee et al., 2015)).
  - Some models express efficiency as a function of equilibrium cooperation rates, but clarify that costly punishment can create a gap between full cooperation rate and maximal payoff due to punishment costs.
- **Related Outcomes**: Some models present "group achievement" (Pacheco et al., 2014), mean fitness (Archetti & Scheuring, 2013), or sustainable yield/profit (Furuzono et al., 2013, Sasaki et al., 2016).

**Non-Payoff Behavioral Outcomes (Relevance: indirect/moderators):**
- **Cooperation/Contribution Rates/Frequencies**: Ubiquitously analyzed as the primary mechanism by which efficiency is potentially affected. Many models stop short of converting to payoffs.
- **Punishment/Reward Frequency**: Tracked to study mechanism sustainability (Szolnoki & Perc, 2013); but not directly mapped to efficiency.
- **Norm Compliance, Reputation, and Social Structure Effects**: Often used to explain or predict behavioral changes that may ultimately affect efficiency but not measured as payoffs.

**Distinctions:**
- Many papers **explicitly distinguish efficiency from cooperation** (e.g., Milinski, 2016; Rand & Nowak, 2013), noting, for example, that "punishment can sustain cooperation without always increasing efficiency if costs are high or punishment is misdirected."
- Some reviews ground policy implications in efficiency/welfare, but draw upon behavioral mechanisms as the causal processes.

# 4) Main Findings Relevant To Prediction

**General Patterns:**
- **Punishment Can Increase Efficiency—But Context Matters:**  
  - In standard or voluntary PGGs, enabling effective, pro-social punishment commonly shifts equilibria or evolutionary dynamics toward higher group efficiency (Sasaki & Uchida, 2013; Dercole et al., 2013; Adami et al., 2016; Schoenmakers et al., 2014).
  - The effect of punishment is **highly contingent** on parameters:
    - **Cost and Effectiveness of Punishment**: If punishment is costly relative to its deterrence, efficiency gains can evaporate or punishment can even reduce efficiency (Hauser et al., 2014; Vukov et al., 2013). Optimality often requires punishment to be both effective (high fine-to-cost ratio) and targeted, or for second-order punishment/reward mechanisms to be present (Okada et al., 2015; Iwasa & Lee, 2013).
    - **Population/Interaction Structure**: Punishment is ineffective in well-mixed populations but may be highly effective in structured or spatial contexts (Oya & Ohtsuki, 2017; Roos et al., 2014; Kaiping et al., 2016; Adami et al., 2016).
    - **Antisocial Punishment**: The presence of antisocial punishment neutralizes or reverses efficiency gains from punishment (Hauser et al., 2014; Rand & Nowak, 2013; Gao et al., 2015).
    - **Institutional/Information Design**: Centralized, visible punishment creates more robust efficiency gains than decentralized (peer) punishment, especially when anti-social punishment is possible (Schoenmakers et al., 2014; Gao et al., 2015; Lee et al., 2015). Information about enforcer honesty (and corruptibility) is critical (Lee et al., 2017).
    - **Graduated/Context-Dependent Punishment**: Punishment tailored to harm or context, rather than being severe-for-all, maximizes efficiency especially in heterogeneous populations and where errors in monitoring are present (Iwasa & Lee, 2013; Lee & Iwasa, 2014).
    - **Social Exclusion as Punishment**: Exclusion mechanisms (removal of benefits) generally outperform costly deduction-based punishment for long-run efficiency (Sasaki & Uchida, 2013; Sasaki et al., 2016).
    - **Baseline Efficiency Matters**: In highly efficient control games, enabling punishment adds little or is even detrimental. In low-efficiency baselines, potential for positive effect is greater (Archetti & Scheuring, 2013; Adami et al., 2016).
    - **Group Size and Rounds**: Smaller group sizes and more repeated interaction (num_rounds) generally amplify the positive effect of punishment (Eldakar et al., 2013; Adami et al., 2016).

**Mechanistic/Welfare Arguments:**
- Efficiency improvements via punishment are not inevitable—**mechanism design, parameterization, population structure, and anti-social dynamics critically mediate the outcome.** The literature directly supports strong context-dependency and non-monotonicity rather than simple generalized claims.

# 5) Prediction Guidance

- **Baseline-Adjusted Expectation**:  
  - **If the control game is inefficient**, enabling effective, pro-social punishment is likely to increase efficiency **if and only if** (a) punishment is not too costly, (b) antisocial punishment is prevented or rare, (c) some form of population structure, repeated interaction, or reputation/tracking is present, and (d) the punishment mechanism is robust (institutionalized or with cost-sharing/visibility).
  - **If the control game is already efficient**, efficiency improvements from enabling punishment will be minimal, and punishment costs can reduce net efficiency.
- **Parameter Moderation**:
  - **Punishment Cost/Effectiveness**: Lower cost and higher effectiveness (high fine per unit cost) increase the effect. If punishment is inefficient, the efficiency effect is weak or negative.
  - **Antisocial Punishment**: If anti-social (punishing cooperators) is possible/unprevented, **do not expect efficiency gains** (Hauser et al., 2014).
  - **Population Structure**: Expect more positive effects in spatial, clustered, or repeated-group settings; weak or null effects in well-mixed/anonymous setups.
  - **Punishment Technology**: Social exclusion or graduated, context-sensitive sanctions (rather than pure peer-deduction) are more efficiency-promoting, especially when second-order free-riding is addressed.
  - **Institutional Features/Information**: Public visibility of who can/will punish, and transparency of enforcement, increase the likelihood of efficiency gains.
  - **Group Size and Iteration**: Smaller groups and longer duration games (high num_rounds) enhance the effectiveness of punishment; large groups may require institutional solutions.
- **Nonlinear/Threshold Effects**: Expect that punishment may create a "critical mass" effect—if most defect, punishment will not help, but if a threshold of cooperators/punishers is present, efficiency can sharply increase (Adami et al., 2016; Dercole et al., 2013).

**Cautions**  
- Applying findings directly requires alignment of the target’s design dimensions with the model's assumptions—many theoretical results assume idealized rationality, evolutionary timescales, or perfect implementation of mechanisms.
- **No direct calibration for laboratory effect sizes**—predictions should be treated as "likely direction and moderators" rather than precise quantitative estimates.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions** (clear, mechanistic analysis):
- **player_count**: Extensively analyzed; smaller groups more conducive to punishment improving efficiency; large groups require institutions or information (Eldakar et al., 2013; Powers & Lehmann, 2013; Adami et al., 2016).
- **num_rounds**: Repetition/iteration generally increases effect of punishment (Eldakar et al., 2013; Adami et al., 2016).
- **punishment_cost**: Universally modeled; often interacts with punishment_tech.
- **punishment_tech**: Substantial focus; peer vs. pool, exclusion, graduated, centralized/vs decentralized (Sasaki & Uchida, 2013; Schoenmakers et al., 2014; Iwasa & Lee, 2013).
- **mpcr**: Central to most public goods models; frequently studied as a continuous moderator.
- **all_or_nothing**: Less attention, but some models distinguish between continuous and binary contributions.
- **reward_exists, reward_cost, reward_tech**: Several papers model joint reward/punishment settings, but more focus is on punishment.

**Indirectly Informed/Contextually Discussed:**
- **default_contrib**: Rarely an explicit focus; sometimes assumed as part of framing.
- **chat**: Occasionally discussed re: communication and reputation (Milinski, 2016; Declerck et al., 2013).
- **show_other_summaries, show_n_rounds, show_punishment_id**: Implicitly relevant in models emphasizing information/reputation/tracking (Schoenmakers et al., 2014; Lee et al., 2015) but not always operationalized as distinct variables.
- **punishment_magnitude**: Nearly always parameterized jointly with cost, but not always discussed as a design dimension; effectiveness (fine per cost) is the operative moderator.

**Effectively Missing or Sparse:**
- **default_contrib, chat, show_other_summaries, show_n_rounds, show_punishment_id**: Often missing as explicit variables or only discussed in narrative/mechanism interpretation, not as systematically analyzed moderators.

# 7) Important Limitations

- **Empirical Calibration Is Lacking:**  
  - The literature here is theoretical. There are **no direct experimental effect sizes**. Quantitative predictions about likely efficiency levels and effect sizes are not empirically grounded; findings set out qualitative, parametric, and mechanistic contingencies instead.

- **Mechanism Assumptions May Not Translate:**  
  - Many models assume evolutionary dynamics, infinite repetition, or perfectly rational agents, which may not match real-world or laboratory PGG implementations.
  - Some assume away anti-social punishment, second-order free-riding, or restrict strategy space (e.g., pro-social punishment only), which is often not the case in experiments.

- **Outcome Mapping Ambiguity:**  
  - For works that focus on behavioral outcomes (cooperation rates, strategies), the translation to efficiency/payoff can be context-dependent, particularly when punishment is costly or misdirected.

- **Moderators and Dimension Interactions:**  
  - While many key prediction dimensions are addressed, others are underexamined or only superficially discussed (e.g., chat, feedback, framing, information cues). Interaction effects between dimensions (e.g., punishment cost × group size × network structure) are sometimes theorized but not fully mapped.

- **Institutional and Real-World Complexity:**  
  - Models with highly stylized or idealized institutions may miss practical implementation challenges (corruption, transparency, error-prone monitoring, self-selection, etc.).

- **Uncertainties and Disagreement:**  
  - Where anti-social punishment or high punishment costs are possible, there is clear **disagreement and model-dependent ambiguity**: some predict positive efficiency effects, others neutral or negative. The prediction must therefore be **sensitive to model match to the target environment**.

---

**Summary Statement:**  
This theoretical literature base provides a rich, mechanistic foundation for understanding and **qualitatively predicting when and why enabling punishment might increase efficiency in PGG-like environments**. The predicted direction and magnitude are **highly dependent on design parameters** (especially punishment cost/effectiveness, group structure, possibility of anti-social punishment, and baseline efficiency), and **no direct quantitative calibration is available** in this set. Several prediction dimensions are well-theorized (player count, punishment cost/tech, mpcr); others are underexplored. Use these findings as parameter-sensitive moderators for qualitative predictions about efficiency outcomes, but not as a source of empirical effect size estimates or guarantees.
