# 1) Evidence Base

This literature set is composed primarily of theoretical studies using agent-based simulations and evolutionary game theory (the vast majority), with a minority of empirical studies (lab experiments) and some works touching on policy-oriented or empirical mechanism design. The set is quite broad in terms of the variety of mechanisms (peer and pool punishment, reward, exclusion, tolerance, commitment, mutual punishment, and reputation) and population structures (well-mixed, spatial/lattice, networked), but is *narrow* in that nearly all theoretical papers focus on highly stylized models, and empirical studies rarely report efficiency or group payoff as their main outcome. Most studies are aimed at abstract, model-based understanding rather than direct quantitative prediction at the design-dimension level relevant to practical experimental or policy settings. Nonetheless, several theory papers explicitly model the treatment/control difference with respect to the introduction of punishment and report efficiency-related outcomes.

# 2) Task Relevance

**pgg_or_variant:**

- **exact**: Most theory papers directly model public goods games (PGG) or threshold (all-or-nothing) PGGs (e.g., Perc et al., 2017; Szolnoki & Perc, 2013, 2017; Adami et al., 2016; Schoenmakers et al., 2014).
- **close/adjacent**: Some papers analyze related games such as trust games with feedback, commitment mechanisms, or reputation interventions (Li & Xiao, 2014; Han et al., 2017), or the prisoner's dilemma (Yang et al., 2015).
- **none**: Several works apply only to games without public goods structure (e.g., dictator games, standard PD, or market reputation systems).

**punishment_or_sanctions:**

- **exact**: Many models and some experimental studies specifically manipulate the availability, implementation, and parameters of peer or institutional punishment (e.g., Perc et al., 2017; Hauser et al., 2014; Schoenmakers et al., 2014).
- **close/adjacent**: Some consider reward, exclusion, tolerance, or commitment as alternatives or complements to classic punishment (Szolnoki & Chen, 2015; Han et al., 2017).
- **none**: Other studies include neither punishment nor any related sanction mechanism.

**efficiency_or_related_payoff_outcome:**

- **exact**: A subset of theory papers report effects directly on group efficiency, average payoff, welfare, or surplus (e.g., Perc et al., 2017; Szolnoki & Perc, 2013, 2017; Adami et al., 2016; Schoenmakers et al., 2014).
- **close/adjacent**: Many papers report only contribution rate, fraction of cooperators, or strategy composition; efficiency outcomes must be inferred (Chen et al., 2014; Szolnoki & Perc, 2016).
- **none**: Some empirical studies with behavioral focus (e.g., norm compliance, punishment frequency, strategy updating) do not report efficiency, payoff, or welfare.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:**  
    - Group efficiency (fraction of maximum possible payoff), total group payoff, average earnings: Directly reported in several theory papers (Perc et al., 2017; Szolnoki & Perc, 2013, 2017; Adami et al., 2016; Schoenmakers et al., 2014). Some empirical works (Li & Xiao, 2014) provide efficiency/earnings, but mainly in non-PGG contexts.
- **Non-payoff behavioral outcomes:**  
    - Prevalence of cooperation/defection, contribution rates, punishment frequencies, norm compliance, extinction probabilities, equilibrium strategy distribution, social instability. Most theory papers focus primarily on these, especially when exploring the effects of tolerance, exclusion, or commitment (e.g., Chen et al., 2014, Szolnoki & Chen, 2017).
- **Linkages:**  
    - Some works present derived formulas or phase diagrams linking strategy composition to expected efficiency, permitting indirect inference of payoff outcomes where they are not the primary outcome.

# 4) Main Findings Relevant To Prediction

## General Patterns

- **Peer or Pool Punishment Often Increases Efficiency, Conditionally:**  
  In theory-focused papers, enabling punishment increases efficiency/group payoff if (i) punishment is not prohibitively costly, (ii) punishment targets defectors (anti-social punishment is absent or rare), and (iii) the institutional or network structure allows punishers to cluster or coordinate. The effect is strongly moderated by design dimensions including punishment cost, effectiveness, group size, synergy factor (MPCR), and spatial/network structure (Perc et al., 2017; Szolnoki & Perc, 2013, 2017; Adami et al., 2016; Schoenmakers et al., 2014).

- **Costly or Misapplied Punishment Can Reduce Efficiency:**  
  High punishment cost, the presence of anti-social punishment, or parameters that permit excessive or poorly targeted punishment can offset or even reverse efficiency gains, sometimes producing outcomes worse than no-punishment baselines (Perc et al., 2017; Hauser et al., 2014).

- **Optimality and Diminishing Returns:**  
  The effects of enabling both punishment and reward are rarely greater than punishment alone, except under very stringent, low-cost or low-MPCR conditions (Szolnoki & Perc, 2013). There is often a nonmonotonic relationship between punishment severity and efficiency; intermediate levels maximize cooperation and efficiency, while excessive punishment imposes counterproductive costs.

- **Structural Features Matter:**  
  The effectiveness (and thus efficiency gain) from punishment is enhanced in structured populations (spatial/lattice/networked), where punishers can form clusters, and where institution visibility is high (Schoenmakers et al., 2014). In well-mixed or high-mutation settings, effects are weaker or absent.

- **Variant Mechanisms (Tolerance, Exclusion, Commitment):**  
  Mechanisms such as tolerance (conditional cooperation/withdrawal), social exclusion, and precommitment/compensation can often increase efficiency as much as or more than standard punishment, particularly when they are well-matched to key parameters (Szolnoki & Chen, 2015; Han et al., 2017; Li et al., 2015). However, these mechanisms represent adjacent, not exact, punishment scenarios.

- **Control Efficiency as a Baseline:**  
  Papers support the notion that efficiency in no-punishment control is a strong moderator:

   - When baseline efficiency is already high (e.g., high MPCR, small group size), adding punishment yields small or no additional efficiency.
   - When control efficiency is low (hard dilemma), enabling moderate-cost, effective punishment produces large efficiency gains—but only up to the point where the extra cost of punishment does not outweigh cooperative gains.

# 5) Prediction Guidance

- **Where Theory Applies Directly:**  
  For PGGs with design parameters matching the theory models (e.g., peer punishment, no anti-social punishment, moderate cost, moderate group size, and spatial/local interactions), enabling punishment is highly likely to increase average group efficiency relative to control—with the effect size dependent on punishment cost, MPCR, and group size (Perc et al., 2017; Adami et al., 2016; Schoenmakers et al., 2014).

- **Key Parameter Moderators:**
  - **Punishment Cost and Effectiveness:** Efficiency increases if the punishment is not overly costly and is targeted at defectors. Non-targeted or anti-social punishment may reduce or eliminate gains (Hauser et al., 2014).
  - **Group Size:** The positive effect of punishment is strongest in small-to-moderate group sizes; large groups dampen both cooperation and the impact of punishment unless additional mechanisms (e.g., institution visibility, pool punishment) are implemented.
  - **Synergy Factor (MPCR):** Games with low MPCR (hard dilemma) benefit most from punishment. For high MPCR or naturally cooperative settings, incremental efficiency from punishment is minimal or negative (Adami et al., 2016).
  - **Institutional/Network Structure:** Structured populations or visible institutions make punishment substantially more effective at increasing efficiency (Schoenmakers et al., 2014; Szolnoki & Perc, 2017).
  - **Reward Existence:** Adding reward to punishment yields little further increase in efficiency, except under very narrow parameter conditions.

- **Ambiguity and Model Boundaries:**
  - **If the design allows anti-social punishment** or non-discriminatory punishment, and the population is well-mixed or turnover/mutation is high, predictions about efficiency gain from enabling punishment are weak or negative (Hauser et al., 2014).
  - **If punishment costs are near or above the cost of cooperation/defection,** expect minimal improvement to efficiency, or even losses.

- **Indirect or Qualitative Guidance:**
  - When only cooperation rates are reported, efficiency will only improve if increased cooperation outweighs total punishment expenditures. Phase diagrams or payoff expressions in these models enable estimation, but introduce inference error.
  - The presence of efficient commitment, exclusion, or tolerance mechanisms can substitute for (or outperform) punishment under certain parameterizations, but should not be assumed equivalent without direct design matching.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**
- **player_count, num_rounds:** Explicitly manipulated in many models and used in phase diagrams for efficiency effects.
- **mpcr (synergy factor):** Central to all theory papers; critical moderator for efficiency gain from punishment.
- **punishment_cost, punishment_tech:** Explicitly varied and shown to have non-linear (often nonmonotonic) effects on efficiency.
- **reward_exists:** Often manipulated or included for comparison (usually found to be less central than punishment).
- **all_or_nothing:** Addressed in threshold PGGs and models with discrete vs. continuous contributions.
- **punishment_exists (for treatment/control difference):** The core manipulation.

**Indirectly Informed/Contextually Discussed:**
- **chat:** Touched on in some empirical papers, but rarely modeled in theory.
- **show_other_summaries, show_n_rounds, show_punishment_id:** These feedback/information visibility variables map to notionally similar constructs (e.g., observability, institution visibility, monitoring), but are not manipulated directly in most papers.
- **reward_cost, reward_tech:** Addressed primarily in studies comparing reward and punishment or reward-based mechanisms.

**Effectively Missing or Sparse:**
- **default_contrib:** Only incidentally discussed, not manipulated.
- **show_other_summaries, show_n_rounds, show_punishment_id:** Rarely manipulated as explicit experimental variables.
- **chat:** Considered in a few empirical works, typically not in theory.
- **Some parameters (e.g., the difference between peer and pool punishment, or interaction with chat and norm salience) have limited or no direct quantitative evidence.**

# 7) Important Limitations

- **Empirical Gaps:**  
   - Most findings are theoretical or simulation-based; very few papers report real experimental or field data with efficiency as the outcome. Real-world human behaviors (limited rationality, fairness concerns, anti-social punishment) may deviate from theoretical predictions.

- **Payoff Outcomes Often Inferred Indirectly:**
   - Many studies focus on cooperation frequency or strategy prevalence, not efficiency or group payoff. Predictions often require inferring payoff using provided equations or by mapping phase diagrams onto efficiency outcomes.

- **Parameter Coverage Not Comprehensive:**
   - Only a subset of the 14 design dimensions is systematically varied and analyzed. Several contextual features—especially those linked to information, communication, or identity—are discussed only in passing, not tested.

- **Mechanism Interactions and Spillovers:**
   - Some adjacent or close-relatives of punishment (e.g., exclusion, commitment, reputation) are not generic stand-ins for peer punishment, so transferability of their efficiency effects is uncertain.

- **Ambiguity in Anti-social Punishment and High Mutation:**
   - Where anti-social punishment or high-exploration dynamics are possible, results diverge; some models predict strong negative or neutral efficiency effects for punishment (Hauser et al., 2014).

- **Limited Generalizability to Heterogeneous Populations and Institutions:**
   - Most models focus on symmetric, homogenous settings. Real environments may include varying propensities to punish, differences in information, or mixed sanction mechanisms.

- **Reward and Feedback Mechanisms:**  
   - The relationship of reward mechanisms, rebates, or market-style feedback to punishment-enabled PGGs is structurally close but not identical, so findings on rewards/rebates cannot be directly mapped.

---

In summary, theoretically grounded evidence strongly supports the generalization that enabling well-targeted, not-too-costly, and visible punishment can increase efficiency in public goods games—*conditional* on the absence of high anti-social punishment and appropriateness of core design parameters (group size, MPCR, institutional structure). However, due to sparse empirical confirmation, overinterpretation of quantitative effect sizes or transfer to untested parameter regimes is not advised. Predictions should leverage this literature as a set of mechanism-of-action constraints and qualitative patterns, with specific quantitative estimates grounded in model results only where all major parameter matches are secure.
