# 1) Evidence Base

This paper set consists of a mix of empirical (2 laboratory experiments, 1 observational study) and predominantly theoretical or modeling papers (7), with a broad lens on social dilemmas, cooperation, and punishment mechanisms. Only one empirical study (Engel, 2019) uses a standard linear public goods game (PGG); most other papers examine related but distinct environments (e.g., Prisoner's Dilemma, principal-agent games, mutualisms, community resource settings). Similarly, only two studies (Engel, 2019; Wei et al., 2025) provide direct empirical data on efficiency or related payoff-based outcomes in the presence or absence of punishment. Several theoretical papers rigorously analyze the role and evolutionary logic of punishment, but often in settings not isomorphic to standard PGGs or without direct outcome measures. Overall, the evidence base is broad in conceptual and mechanistic scope but limited in direct empirical coverage of the downstream prediction task.

# 2) Task Relevance

The paper set’s relevance to the specific prediction task is mixed:

- **pgg_or_variant**: Only Engel (2019) is an experimental study of an exact PGG; several others are in adjacent paradigms such as spatial Prisoner's Dilemma (Steimanis et al., 2020; Li et al., 2022), principal-agent (Wei et al., 2025), or theoretical models of coordination games (Vanderschraaf, 2016; Pedroso, 2021). Most theory papers treat public goods dilemmas conceptually or use analogs. Task relevance: ranges from `exact` (Engel, 2019) to `adjacent` (most others).
- **punishment_or_sanctions**: Most papers analyze punishment or sanctioning (`exact`), though a few only discuss externalities, partner selection, or cooperation without explicit punishment (`adjacent` or `none`).
- **efficiency_or_related_payoff_outcome**: Only Wei et al. (2025) and Vanderschraaf (2016) (theory) address group efficiency or analogous payoffs directly; Engel (2019) and some others provide only descriptions or theoretical interpretation. Most papers focus on behavioral (cooperation) outcomes or conceptual arguments. Task relevance: generally `adjacent` or `weak` for efficiency, with very little `exact` relevance.

Overall, there is high to moderate relevance for punishment/sanctions, moderate to low for PGG structure, and low for direct efficiency outcome measurement.

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes:**
- **Efficiency, group payoff, welfare, or surplus**: Empirically, only Wei et al. (2025) directly measures efficiency as the total earnings relative to possible surplus. Engel (2019) only describes total earnings, without systematic analysis. Vanderschraaf (2016) provides theoretical evidence using efficient equilibrium selection probabilities in a coordination/punishment context.
- **No direct efficiency reporting**: Most theoretical and some empirical papers focus on cooperation rates, norm compliance, or strategic behavior changes, not payoff-based group outcomes.

**Non-Payoff Behavioral Outcomes:**
- **Contribution or cooperation rates**: Extensively used in Engel (2019), Steimanis et al. (2020), Li et al. (2022), Pedroso (2021), and theoretical accounts.
- **Punishment assigned/punishment frequency**: Several papers (Engel, 2019; Steimanis et al., 2020; Goodman, 2023) track frequency or targets of punishment rather than outcomes.
- **Norm compliance, moral responsibility, or signaling**: Theoretical papers (Fischborn, 2023; Pedroso, 2021; Goodman, 2023) emphasize evolution and justification of punishment, not payoffs.

**Observational/Field Outcomes:**  
- **Behavioral externalities**: Albergaria & Saes (2018) tracks borrowing behavior and its externalities, not efficiency or payoffs.

# 4) Main Findings Relevant To Prediction

- **Punishment Can Facilitate Efficiency, Under Specific Conditions**: The strongest theoretical support comes from Vanderschraaf (2016), who finds that adding a costly punishment option to a coordination game (Stag Hunt) dramatically increases the likelihood of efficient, cooperative outcomes, even when the punishment is weakly dominated. The effect is strongest when punishment inflicted is at least as large as the punisher's cost, and robust across parameters—but this is in a 2-player evolutionary framework, not a multi-player repeated PGG.
- **In Some Contexts, Punishment May Not Raise Efficiency**: Engel (2019) finds, experimentally, that in linear PGGs with centralized punishment, increased transparency (individual-level punishment/contribution feedback) reduces cooperation relative to less detailed feedback, running counter to deterrence theory. Importantly, efficiency is not directly analyzed, but the implication is that punishment, especially with high transparency, may not always bolster group outcomes—sometimes the opposite.
- **Positive Efficiency Effects in Principal-Agent Analogs**: Wei et al. (2025) shows empirically that introducing a costly, even non-credible, punishment-like mechanism (job rotation threat) can measurably increase group efficiency in principal-agent settings by reducing strategic shirking.
- **Cooperation vs. Efficiency Divergence**: Theoretical warnings (Goodman, 2023) stress that high observed cooperation rates due to punishment do not guarantee higher efficiency if undetected defection modes exist.
- **Cooperation Frequency Effects**: Several spatial or conditional punishment models (Steimanis et al., 2020; Li et al., 2022) support the idea that punishment mechanisms promote higher average cooperation rates in spatial games, but do not provide evidence on whether this raises efficiency net of costs.
- **Sanction Type & Community Effects**: Albergaria & Saes (2018) notes that different sanction types cause externalities, but does not inform on group efficiency or payoffs.

# 5) Prediction Guidance

- **Expected Direction**: Theoretical and some empirical evidence suggests that enabling punishment in social dilemma games often increases the probability of efficient outcomes or at least raises cooperation rates, supporting the prediction that treatment efficiency usually increases with punishment relative to control conditions—especially when punishment is sufficiently severe relative to its cost (Vanderschraaf, 2016; Wei et al., 2025).
- **Key Moderators**: However, effect strength and direction depend on variables such as the transparency of punishment (Engel, 2019), type of punishment mechanism (centralized vs. peer), risk of undetected defection (Goodman, 2023), and cost/efficacy balance in sanctioning (Steimanis et al., 2020).
- **Caveats**: Empirical findings (Engel, 2019) show that increased transparency about punishment can undermine cooperation, so prediction functions must account for possible null or negative effects in these conditions.
- **Control Efficiency as Baseline**: Since most studies lack direct mapping between control efficiency and treatment efficiency under varying game design, strong generalization is not supported. The effect of punishment may be weaker or negative if control efficiency is already high or if the punishment institution undermines trust or backfires due to second-order free riding.
- **Transferability Concerns**: Most evidence is for adjacent or conceptual settings. Results may not transfer directly to all parameter regimes or to large, multi-player, repeated linear PGGs with peer punishment.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**
- **player_count**: Frequently manipulated (Engel, 2019; Wei et al., 2025; theory papers).
- **num_rounds**: Discussed or used in experiment structures.
- **all_or_nothing**: Several models contrast all-or-nothing and continuous (Engel, 2019; theory).
- **mpcr (marginal per-capita return)**: A central variable in payoff structures and manipulable in some theoretical and experimental papers.
- **punishment_cost**/**punishment_tech**: Frequently discussed, often central to mechanism arguments and experimental treatments.
- **show_other_summaries**, **show_punishment_id**: Systematically manipulated in Engel (2019), directly informing prediction about feedback/transparency effects.
- **chat**: Included in Engel (2019) and Wei et al. (2025).
- **reward_exists**, **reward_cost**, **reward_tech**: Only contextually discussed; not manipulated in any study.

**Indirect or Contextually Discussed:**
- **default_contrib**: Only rarely described, not systematically manipulated.
- **show_n_rounds**: Present as a game parameter but not systematically analyzed for outcome effects.

**Effectively Missing:**
- **reward_cost**, **reward_tech**, **reward_exists** as primary manipulated variables.
- **default_contrib** in empirical testing.

# 7) Important Limitations

- **Scarcity of Direct Efficiency/Payoff Results**: Very few empirical studies (Wei et al., 2025; Engel, 2019—descriptive only) provide direct efficiency outcome analysis in PGGs with peer punishment.
- **Predominance of Theory & Non-PGG Studies**: Most evidence comes from theoretical or adjacent-game models (coordination games, Prisoner’s Dilemmas, field observations, mutualisms) rather than repeated multi-player PGGs, limiting external validity.
- **Contribution vs. Efficiency Ambiguity**: Many findings are about increased cooperation or norm compliance, which may not translate to higher group efficiency due to the costliness of punishment itself and possible misalignment between observed cooperation and actual welfare (Goodman, 2023).
- **Limited Dimensional Mapping**: Not all 14 specified design dimensions are systematically varied or analyzed; several (reward-related, contribution framing) have little or no empirical/theoretical support in this set.
- **Transparency and Institution Details Matter**: Empirical evidence (Engel, 2019) suggests that punishment can backfire under high transparency of feedback—a strong caveat for interpreting simple “punishment increases efficiency” heuristics.
- **Transferability and Scaling**: Effects observed in 2-player games, spatial lattices, or with non-peer (centralized or exogenous) punishment should not be generalized quantitatively to conventional repeated PGGs with peer punishment without caution.

---

**In sum:**  
The literature provides theoretical support and limited empirical evidence that introducing punishment can increase efficiency in social dilemmas, but effect direction and magnitude depend strongly on design details—such as feedback structure, cost/efficacy of punishment, and the baseline efficiency. Behavioral outcomes such as increased cooperation do not always equate to improved efficiency, especially if punishment costs or undetected defection are significant. Most design dimensions are only partially covered; direct empirical mappings from control to treatment efficiency in PGGs with peer punishment are sparse in this set.
