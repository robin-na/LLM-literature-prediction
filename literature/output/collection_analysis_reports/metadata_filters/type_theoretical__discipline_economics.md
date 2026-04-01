# 1) Evidence Base

The paper set is a **large, theory-dominated corpus** (168 papers, almost all theoretical) that directly targets public goods game (PGG) environments and their close variants. Nearly all papers use formal models, with some using simulations, and very few reporting new experimental data and none with new empirical effect size estimates for efficiency. The evidence is **highly granular regarding mechanism and design parameterization**, but mostly concerns theoretical predictions, equilibrium characterizations, and comparative statics rather than empirical regularities or meta-analytic effect sizes.

The set is **narrow in terms of experimental evidence but extremely broad with respect to theoretical modeling** of PGGs and their punishment-enabled/disabled variants. There is a substantial and deep exploration of the moderators, mechanisms, and boundary conditions under which punishment increases, decreases, or leaves unchanged the efficiency of group outcomes.

# 2) Task Relevance

The relevance of the literature to the core prediction task—**predicting treatment efficiency (with peer punishment enabled) from design parameters and control efficiency (without punishment)**—is as follows:

- **pgg_or_variant:** **Exact** relevance is high. The majority of sources model or analyze standard PGGs or exact close variants (threshold, CPR, repeated, networked, or partnership games) and explicitly map to or generalize PGG design dimensions.
- **punishment_or_sanctions:** **Exact** relevance is very high in the core set: punishment technologies, peer and institutional punishment, and their parameterizations are central. A subset models reward, exclusion, or ostracism.
- **efficiency_or_related_payoff_outcome:** Most core papers have **exact** or **close** relevance: they report, derive, or discuss efficiency, group welfare, total payoff, or surplus as the primary or explicit outcome. Some include only adjacent outcomes (contribution rate, norm compliance, cooperation frequency), but the key theoretical models usually connect these to efficiency via equilibrium calculations.

**Empirical coverage of payoff outcomes is weak**: though many theoretical models give explicit relationships between game parameters and efficiency, few studies provide lab data or field estimates.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes (directly relevant for prediction):**

- **Efficiency (group payoff relative to maximum possible):** The central theoretical and simulation metric.
- **Welfare, total earnings, surplus, group payoff:** Used interchangeably with efficiency, typically as the sum or average of individual payoffs in the group.

**Non-payoff (behavioral) outcomes (reinforce but don't substitute for payoff outcomes):**

- **Contribution/cooperation rates:** Widely reported, theorized, and simulated; important as mechanisms for explaining changes in efficiency, but not themselves efficiency.
- **Punishment/reward frequency/severity:** Used to explain mechanism or as endogenous variables in equilibrium characterization.
- **Norm compliance, reputation, exclusion, partner selection:** Discussed for their role in sustaining cooperation, with linkages to efficiency, but not always mapped to payoff metrics.

The theoretical literature is careful to distinguish between **contribution rate increases (which only improve efficiency if punishment costs do not outweigh gains)** and true improvements in total group payoff/efficiency.

# 4) Main Findings Relevant To Prediction

## Empirical vs. Theory

- **Empirical evidence for payoff-based efficiency changes in response to enabling peer punishment in PGGs is very limited.**
- **Theoretical models overwhelmingly predict that enabling effective, not-too-costly punishment increases efficiency, sometimes dramatically**, relative to the control game, across a broad range of game parameters ((Levine & Modica, 2016); (Fehr & Schmidt, 1999); (Dutta et al., 2021); (Kranz, 2010); (Botta et al., 2021); (Huang et al., 2024)).
- **Efficiency gains are largest** when:
    - Punishment cost is low relative to the harm it inflicts (punishment_cost, punishment_tech).
    - Monitoring of actions is sufficiently informative (show_other_summaries, show_punishment_id).
    - Group size is moderate to large (player_count), but only if coordinated or credible punishment strategies are feasible ((Wolitzky, 2013); (Hwang, 2017)).
    - Baseline (control) efficiency is low (i.e., none of the other mechanisms—history, social preferences—currently sustain cooperation).
- **Efficiency gains are reduced, attenuated, or may even become negative** when:
    - Punishment is costly (punishment_cost is high relative to impact), or its application is inefficient (e.g., antisocial punishment is prevalent, or punishment is misapplied ((Tanimoto, 2018); (Thöni, 2014); (Sylwester et al., 2013))).
    - Social preferences (altruism, norm internalization) are strong enough to sustain cooperation without punishment, or when punishment crowds out intrinsic motivation ((Hwang & Bowles, 2012); (Ostrom, 2000)).
    - Punishment institutions are poorly designed (e.g., collective/pool punishment not targeted, only certain classes can be punished, extortion is possible ((Acemoglu & Wolitzky, 2021); (Barron & Guo, 2021); (Alventosa & Olcina, 2021))).
    - Monitoring is noisy, information is incomplete, or identification of defectors is hard ((ABREU et al., 1991); (Levine & Pesendorfer, 2007); (Mihm & Toth, 2020)).
    - Anti-social punishment, retaliation, or misuse of punishment mechanisms is common (documented especially in cross-cultural settings).
- **Cooperation rates often increase when punishment is introduced, but group efficiency can decrease if punishment costs are high.** Some models explicitly document that increased punishment can sustain high cooperation but reduce net payoffs, and the effect is sensitive to punishment parameters ((Tanimoto, 2018); See also reviews: (Noussair & van Soest, 2014)).
- **Network, monitoring, and information structures critically moderate the efficiency gains from punishment.** Richer monitoring enables more efficient deterrence and maximizes impact per unit punishment cost.
- **Heterogeneity and population structure matter:** If the group consists of a mix of types (e.g., altruists, reciprocators, and defectors), the composition will affect the equilibrium efficiency gain from punishment ((Hwang & Bowles, 2012); (Dong et al., 2024); (Sethi & Somanathan, 2003); (Sugaya & Wolitzky, 2023); (Kranz, 2010)).
- **Reward mechanisms can, in certain settings, match or exceed the efficiency gains from punishment, and the combination of minimal targeted punishment and broad-based reward leads to maximal efficiency ((Huang et al., 2024)).**
- **On rare occasions, adding punishment can worsen efficiency (even as cooperation rises), especially with inefficient punishment, misuse, high cost, or crowding-out of social preferences ((Tanimoto, 2018); (Sylwester et al., 2013); (Hwang & Bowles, 2012); (Ostrom, 2000)).**

# 5) Prediction Guidance

- **Theory is highly favorable to the use of analytical (mechanism-based) prediction of treatment efficiency as a function of game design parameters and control efficiency.** Theoretical models provide explicit formulas, thresholds, and comparative statics for efficiency as a function of design variables: player_count, num_rounds, mpcr, punishment_cost/punishment_tech, all_or_nothing, reward_exists/cost/tech, information structures, and baseline compliance rates.
- **If the control game has low efficiency (near Nash equilibrium), enabling peer punishment (with moderate cost and good monitoring) is predicted to *substantially* increase efficiency, often close to the social optimum ((Fehr & Schmidt, 1999); (Levine & Modica, 2016); (Dutta et al., 2021); (Kranz, 2010)).**
- **The size of the efficiency gain is sensitive to:**
    - **Punishment cost**: Lower punishment cost (or higher punishment effectiveness) yields larger efficiency gains.
    - **Monitoring quality**: More informative or publicly available outcome or identity signals yield higher efficiency.
    - **Group size**: Large groups can still achieve high efficiency with punishment, if punishment tech and monitoring scale (contrary to classic group size pessimism).
    - **Population composition/social preference**: If a large fraction of the group are unconditional altruists, or if anti-social punishers exist, the efficiency gain from enabling punishment may be reduced or even negative ((Hwang & Bowles, 2012); (Tanimoto, 2018); (Thöni, 2014)).
    - **Baseline (control) efficiency**: If control efficiency is already high (because of social norms, communication, strong default contributions), enabling punishment yields little or no efficiency gain and may crowd out intrinsic motives.
    - **Presence of anti-social punishment or retaliation**: Frequent anti-social punishment can undermine overall welfare, making efficiency gains from enabling punishment ambiguous or negative in some sub-populations or cultures.
- **Contextual features such as chat/communication and the presence of reward mechanisms interact with punishment to moderate efficiency gains.** Les robust evidence exists for chat, reward, or information disclosure mechanisms, but communication is generally found to be strongly positive for cooperation/efficiency; combined mechanisms (punishment + chat) nearly always outperform punishment alone ((Noussair & van Soest, 2014); (Ostrom, 2000)).
- **Predictions must not infer monotonic increases in efficiency with punishment; non-monotonic and context-dependent effects are well documented.**

# 6) Design Dimensions Highlighted Across Papers

**Directly informed by theory and (occasionally) simulation:**
- **player_count**: Quantitative/qualitative effects mapped, with explicit thresholds for group-size impact and coordination mechanisms ((Levine & Modica, 2016); (Wolitzky, 2013); (Buchholz et al., 2014)).
- **num_rounds**: Repeated play is central to most models; discounted vs. finitely repeated structures are addressed.
- **mpcr**: Central in all PGG models; threshold and linear returns mapped with comparative statics.
- **punishment_cost**, **punishment_tech**: Most models specify the cost to the punisher, the harm imposed on the punished, and their ratio; this is the most critical parameter in nearly all models.
- **all_or_nothing**: Binary vs. continuous contribution is addressed in many models (some findings are parameter-specific).
- **reward_exists/ reward_cost/ reward_tech**: Some models treat reward and punishment together and provide clear comparative statics (less coverage, but see (Huang et al., 2024)).
- **show_other_summaries/ show_punishment_id/ show_n_rounds**: Information and monitoring structures are addressed theoretically as key moderators of equilibrium support and magnitude of efficiency gain ((Mihm & Toth, 2020); (Levine & Pesendorfer, 2007); (ABREU et al., 1991)).
- **default_contrib**: Frame and initial conditions are less often discussed directly, though some theory notes the importance of risky or deviating equilibria (e.g., (Carpenter & Matthews, 2010)).
- **chat**: Conceptually linked to cooperation but less directly included in theoretical models.
- **punishment_magnitude**: Some models map the quantitative penalty imposed for each unit of punishment (see, e.g., (Carpenter & Matthews, 2010)), but often parameterized jointly with punishment_cost as "effectiveness."

**Indirectly informed/contextually discussed:**
- **Reward mechanisms**: When present, typically increase or complement efficiency gains from punishment, but less often modeled jointly.
- **Default contribution framing, pure 'chat,' and specific information feedback mechanisms are discussed as moderators but are less frequently parameterized directly.**
- **Anti-social punishment, exclusion, retaliatory punishment**: Identified as important moderators, but not as simple design dimensions.

**Missing/sparse:**
- **Empirical calibration for dimensions such as chat, default_contrib, show_other_summaries, show_n_rounds, and show_punishment_id** is almost absent—these are discussed conceptually but not with empirical estimates for efficiency gain due to manipulation.
- **Realistic cultural moderators or detailed behavioral calibration for anti-social punishment impact** is thin across the theoretical literature.

# 7) Important Limitations

- **Empirical evidence for actual effect sizes of peer punishment on efficiency across game designs is essentially absent.** All major claims rely on theoretical modelling or agent-based simulation; there is little to no meta-analytic synthesis of efficiency outcomes across PGG experiments with systematically varied peer punishment features.
- **Theoretical models often assume rational, forward-looking agents and perfect or controlled deviations.** Real-world (or even laboratory) behavioral regularities such as confusion, learning, anti-social punishment, and retaliation are recognized in mechanism discussions, but only a few models attempt to incorporate these (leading to uncertainty in real-world generalizability).
- **Crowding-out of intrinsic motivation, presence of anti-social punishment, and costly enforcement are recognized as threat points, but almost never parameterized empirically.** The frequency and magnitude of these undermining factors are not given with real-world prevalence data.
- **Non-payoff behavioral outcomes (e.g., contribution rate, norm compliance) are not substitutes for efficiency outcomes:** While there is ample evidence that punishment increases cooperation rates, the literature is careful to note that if punishment is inefficient (too costly or misapplied), group payoff and efficiency can stagnate or even decline.
- **Sparse attention to some prediction dimensions:** Empirical calibration for design features such as chat, information disclosure, reward interaction, and default contribution frame is absent or sparse.
- **Context-dependence:** Multiple models show that efficiency gains can be negative or null, especially in specific group compositions, cultures, or institutional setups (crowding-out, anti-social punishment). Predictive accuracy thus requires conservatism and attention to local context.
- **Absence of direct lab/field data on efficiency in diverse contexts:** Models span a large space of possible environments, but empirical generality is limited—applications to non-lab, large-scale, or natural environments must be made with caution.

---

**Summary:**  
The literature provides extremely strong theoretical and mechanistic support for the idea that enabling peer punishment (when effective and not too costly) dramatically increases efficiency in PGGs, *especially* when the baseline efficiency is low. The direction, magnitude, or even sign of the efficiency change is tightly moderated by punishment cost and effectiveness, monitoring quality, group size, baseline efficiency, group composition, and the possibility of anti-social or misapplied punishment. For prediction, theory offers explicit functional relationships as long as control efficiency and key design features are known. However, empirical calibration and effect size estimates for diverse contexts are essentially missing; all efficiency-directed prediction will hinge on mechanistic mapping from design parameters, with only indirect empirical anchoring, and must be qualified by attention to moderators not always observable in advance.
