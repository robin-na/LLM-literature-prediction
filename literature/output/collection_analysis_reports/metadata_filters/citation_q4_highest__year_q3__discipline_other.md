# Evidence Base

The paper set consists of three papers, all theoretical in nature, with no experimental or empirical studies. Two of these use formal dynamical models of strategy evolution in public goods games (PGGs) or their variants (Zhu et al., 2020; Liu et al., 2019), providing mechanistic or modeling-based predictions. The third (Jagers et al., 2020) is a conceptual or framework paper focused on the preconditions and theoretical challenges for large-scale collective action. Across the three, the paper set is relatively narrow in terms of empirical support for the prediction task, but it is broad in the sense of covering both peer and pool (institutional) punishment/exclusion, and supplying context about scaling up collective action.

# Task Relevance

- **pgg_or_variant**: Two papers (Zhu et al., 2020; Liu et al., 2019) have *exact* relevance, modeling classic or closely related forms of public goods game. The third (Jagers et al., 2020) has *adjacent* relevance, discussing collective action at a broader scale with PGG analogies.
- **punishment_or_sanctions**: Zhu et al. (2020) is *exact*, comparing peer and pool punishment. Liu et al. (2019) is *adjacent*, focusing on pool *exclusion*, which is closely allied to punishment mechanics. Jagers et al. (2020) is *adjacent*, considering sanctions in a general sense but not modeling them quantitatively.
- **efficiency_or_related_payoff_outcome**: Liu et al. (2019) has *exact* relevance, directly modeling average payoff (i.e., efficiency). Zhu et al. (2020) is *adjacent*, analyzing behavioral strategy frequencies rather than efficiency or group payoff. Jagers et al. (2020) is *adjacent*; it discusses theoretical preconditions for sustaining collective action but provides no outcome data or quantitative predictions.

# Outcomes Measured In The Literature

- **Payoff-related outcomes**: Only Liu et al. (2019) directly analyzes efficiency or average group payoff outcomes linked to design changes (specifically, the introduction of pool exclusion).
- **Non-payoff behavioral outcomes**: Zhu et al. (2020) tracks frequencies of cooperators, defectors, and punishers, which are important for understanding behavioral change but distinct from efficiency. Jagers et al. (2020) does not report outcomes but discusses collective action preconditions.
- **Distinction**: Thus, while all discuss mechanisms or behavioral patterns relevant to efficiency, only one paper directly treats efficiency as an outcome measure. Behavioral measures (cooperation rates, prevalence of punishers, etc.) are more common in this set.

# Main Findings Relevant To Prediction

- **Peer vs. Pool Punishment**: Zhu et al. (2020) reports that peer punishment leads to higher cooperation rates than pool punishment within spatial PGGs, especially when transitions between punishment regimes are tuned toward more peer punishment. The findings are grounded in strategy frequencies, not payoffs, but imply likely efficiency gains where cooperation increases.
- **Exclusion Mechanisms**: Liu et al. (2019) finds that enabling prosocial pool exclusion raises average group payoffs and can stabilize or even maximize cooperation (and thus efficiency) compared to control PGGs (without exclusion/punishment) or to antisocial exclusion. The effect is robust to some antisocial behaviors and especially strong when second-order exclusion exists.
- **Scale and Mechanism**: Jagers et al. (2020) argues that as games get larger and more complex (in terms of group size, anonymity, heterogeneity, etc.), informal mechanisms including peer punishment lose effectiveness, making third-party or institutional sanctions necessary to achieve high cooperation, though this is presented as a theoretical claim rather than measured outcome.
- **Mechanism Focus**: All findings are mostly mechanistic or explanatory rather than offering direct quantitative predictions relating efficiency to the 14 game design dimensions.

# Prediction Guidance

- Where **prosocial pool exclusion** is implemented, prediction should allow for notable increases in average efficiency over a PGG control without such mechanisms (Liu et al., 2019). The improvement is strongest where exclusion can be institutionalized and includes second-order mechanisms.
- **Peer punishment**, as modeled, can increase cooperation frequency (Zhu et al., 2020), but direct links to efficiency require assumptions about payoff structure and the relationship between increased cooperation and net welfare, especially considering punishment costs.
- The effect of punishment, either peer or pool, may **decline with increasing player count and complexity**, unless transitioned to more centralized or institutional forms (Jagers et al., 2020).
- In **predictive models**, control efficiency is a relevant baseline, but the expected treatment increase from punishment will depend on whether the punishment is peer-based (less robust in larger groups), pool-based or exclusionary (potentially higher and more robust increases), and the implementation details (costs, second-order mechanisms, presence of antisocial strategies).
- However, the absence of direct empirical effect sizes or quantified payoff results means predictions must be conservative and uncertainty acknowledged.

# Design Dimensions Highlighted Across Papers

**Directly informed:**
- **player_count**: All three papers consider group size effects (either as explicit parameters or as conceptual drivers).
- **num_rounds**: Modeled in formal theory (Zhu et al., 2020; Liu et al., 2019), mainly as features influencing dynamics.
- **all_or_nothing**, **mpcr**: Modeled in both Zhu et al. (2020) and Liu et al. (2019).
- **punishment_cost**, **punishment_tech**: Explored in detail in Zhu et al. (2020); punishment cost is key to differentiating peer vs. pool punishment.
- **chat**, **show_other_summaries**, **show_punishment_id**: Only discussed contextually or as part of the scaling/complexity framework in Jagers et al. (2020).

**Indirectly/contextually discussed:**
- **default_contrib**: Not modeled directly, but relevant to initial conditions in evolutionary models.
- **reward_exists**, **reward_cost**, **reward_tech**: Only mentioned as possibilities in Jagers et al. (2020), not modeled or reported.
- **show_n_rounds**, **show_other_summaries**, **show_punishment_id**: Only contextually discussed as features affecting group dynamics or anonymity.

**Effectively missing:**
- **default_contrib**, **reward_cost**, **reward_tech**, **reward_exists**, **show_n_rounds**: Not empirically varied or modeled in a way that permits outcome mapping for prediction.

# Important Limitations

- **Empirical Gaps**: No experimental or empirical data; all findings are theoretical, so the predictive accuracy for real-world or laboratory PGGs is limited.
- **Payoff Outcomes Sparse**: Only one model (Liu et al., 2019) gives payoff (efficiency) as an explicit outcome. The others rely on behavioral proxies.
- **Limited Parameter Coverage**: Several design variables important for prediction (e.g., chat, reward mechanisms, visibility features) are either only contextually discussed or ignored.
- **External Validity**: Theoretical results may not generalize to finite, noisy, or heterogeneous human groups.
- **No Quantitative Effect Sizes**: The literature does not provide parameterized, quantitative mapping from control efficiency and design features to expected treatment efficiency.
- **Mechanism Mismatch**: The exclusion mechanism (Liu et al., 2019) is not identical to standard peer punishment, so findings may not transfer directly to all punishment-enabled designs.
- **Ambiguity in Scaling**: Jagers et al. (2020) warns of declining punishment effectiveness with scale but does not offer explicit guidance for prediction or parameter thresholds.

---

**Summary:**  
This paper set offers theoretical, mostly mechanistic expectations that punishment (especially when institutionalized as pool exclusion) can increase efficiency in public-goods settings, but the evidence is sparse and mostly indirect for predicting treatment efficiency from specific design dimensions. Most design dimensions are only partially addressed; efficiency-related results are limited and not aligned to the full set of design parameters used in downstream prediction tasks. Predictions must therefore be cautious and recognize substantial uncertainty.
