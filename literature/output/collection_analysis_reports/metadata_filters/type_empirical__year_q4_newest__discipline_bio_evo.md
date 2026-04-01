# 1) Evidence Base

The paper set consists predominantly of empirical, experimental lab studies (most using human subjects) with a strong emphasis on behavioral economics and social dilemmas. About a third of the papers study standard or close-variant repeated public goods games (PGGs) with or without punishment; however, the remainder involve adjacent or only partially related paradigms, such as dictator games, common-pool resource (CPR) games, trust/ultimatum games, or real-world ethnographic/observational studies. The majority of studies focus on behavioral outcomes (e.g., cooperation, norm enforcement, punishment/reward choices), with a more limited subset reporting direct payoff-based outcomes (i.e., group efficiency, total earnings, or group welfare). Theoretical or purely mechanistic (e.g., neural, social signaling) explanations are represented but only as context; the bulk of the base is empirical. The set is therefore moderately broad, providing a strong anchor for some (but not all) game design dimensions and showing varied coverage for the specific prediction task—namely, predicting PGG efficiency as a function of punishment and other design features.

# 2) Task Relevance

**pgg_or_variant**  
- **Exact**: Several studies directly employ standard repeated public goods games (e.g., Sparks et al., 2024; Espín et al., 2022; Nhim et al., 2023).
- **Close/Adjacent**: Others use close variants (e.g., CPR games, threshold collective-risk dilemmas, public bads; e.g., Xu et al., 2022; Grimalda et al., 2022; Del Ponte et al., 2025), or adjacent economic games as models for group behavior.
- **Weak/None**: A number of papers use one-shot or dyadic games lacking group structure, repeated interaction, or explicit public goods focus.

**punishment_or_sanctions**  
- **Exact**: Some papers manipulate the presence of peer or institutionalized costly punishment (e.g., Sparks et al., 2024; Nhim et al., 2023; Espín et al., 2022).
- **Close/Adjacent**: Several examine non-standard punishment (e.g., financial penalties with voluntary opt-in, indirect punishment, third-party punishment, destruction stages), or punishment-like consequences not mapped onto PGG payoff structure (e.g., Grimalda et al., 2022; Del Ponte et al., 2025; Li et al., 2022).
- **Weak/None**: Some studies examine settings without punishment (often focusing on non-payoff mechanisms or dictatorial/prosocial allocations), or report only on the correlates of punishment in society generally.

**efficiency_or_related_payoff_outcome**  
- **Exact**: A few high-quality studies report group efficiency or total earnings as primary outcomes (e.g., Sparks et al., 2024; Nhim et al., 2023; Del Ponte et al., 2025).
- **Close/Adjacent**: Some provide outcomes closely related to efficiency (group welfare, resource extraction mapped to social optimum, probability of loss avoidance) and permit direct inferences (e.g., Xu et al., 2022; Grimalda et al., 2022).
- **Weak/None**: Many focus primarily on behavioral outcomes (cooperation, punishment/reward actions, norm compliance, trust) or on neural/psychological mechanisms without reporting group payoff or efficiency measures.

# 3) Outcomes Measured In The Literature

**Payoff-related Outcomes (Efficiency, Group Payoff, Welfare):**
- *Directly measured*: Group efficiency, average group earnings relative to the social optimum (Sparks et al., 2024; Nhim et al., 2023; Del Ponte et al., 2025)
- *Mapped or interpreted as efficiency*: Extracted resource levels in CPR games (Xu et al., 2022), probability of group success/loss avoidance (Grimalda et al., 2022)
- *Indirect/infrequent*: Some studies mention group payoff or welfare incidentally, but analytic focus remains behavioral.

**Non-payoff Behavioral Outcomes:**
- Contribution/cooperation rates
- Punishment/reward choices and frequencies
- Trust, norm enforcement, emotions, neural measures
- Partner selection, signaling, and reputation dynamics
- Rule compliance or prosocial tendencies absent group payoff context

**Distinction Maintained:**  
Findings regarding increased contributions/cooperation do not always correspond to increased efficiency, as the cost of punishment (or the mechanism for punishment reward) can offset or even outweigh the gains from higher cooperation, sometimes resulting in unchanged or *lower* final group payoff (see e.g., Nhim et al., 2023; Grimalda et al., 2022).

# 4) Main Findings Relevant To Prediction

Synthesizing across the most relevant studies:

- **Costly punishment can (but does not always) increase efficiency:**  
  - Costly punishment leads to sustained higher contributions and, over long repeated interactions, increases or maintains group efficiency relative to control, provided punishment costs are not so high as to offset all cooperation gains (Sparks et al., 2024).
  - However, if the cost of punishing is large relative to the cooperation gain or if punishment is poorly targeted or too frequent, efficiency improvements are neutralized or reversed: higher contributions do not guarantee higher group payoff (Nhim et al., 2023; Grimalda et al., 2022).

- **Institutional design and punishment structure matter:**  
  - Comparing minimum contribution/tax regimes (which enforce baseline cooperation without direct punishment) to strict costly enforcement reveals taxes improve both contributions and efficiency, while costly enforcement increases contributions but decreases efficiency due to high punishment costs (Nhim et al., 2023).
  - Voluntary or "opt-in" punishment regimes (where penalties can be easily avoided, or pledges are unambitious) do not yield efficiency gains—punishment only works when credible and encompassing (Del Ponte et al., 2025).

- **Magnitude and implementation of punishment is critical:**  
  - High-magnitude fines have a stronger and more persistent positive effect on reducing inefficient extraction (improving welfare) than low-magnitude fines; punishment that is symbolic or reputational without material consequences generally does not sustain efficiency or cooperation (Xu et al., 2022; Sparks et al., 2024).

- **Baseline efficiency moderates the effect of punishment:**  
  - In samples with low default efficiency/cooperation, the marginal benefit of punishment is potentially larger, though high punishment costs can still negate this (Grimalda et al., 2022).
  - Where control (punishment-absent) efficiency is already high, the potential for punishment to further increase efficiency is reduced, while added costs may lower net payoff.

- **Non-payoff mechanisms (e.g., signaling, reputation, social information) shape punishment usage and might influence group dynamics, but do not directly translate into efficiency changes.**  

# 5) Prediction Guidance

- **Direct prediction of group efficiency when peer punishment is enabled should be grounded primarily in studies with exact or close measurement of payoff-based outcomes (e.g., Sparks et al., 2024; Nhim et al., 2023; Xu et al., 2022).**
  - If game design closely matches these studies (e.g., 4-5 players, 18-40 rounds, standard PGG with continuous contributions, known MPCR, no chat), and punishment is a costly, direct deduction mechanism, enabling punishment is likely to:
    - Increase efficiency over time *if* punishment is rationally targeted and costs are not excessive.
    - Lead to modest or even negative efficiency effects if punishment costs are high or if the punishment mechanism is easily avoidable and not coupled with other enforcement.
  - Prediction should consider: cost and magnitude of possible punishment, player count, number of rounds, and current (control) efficiency. The benefit of punishment is conditional on the design details—generic assumptions are risky.

- **For games with voluntary, opt-in, or weak enforcement ("public bads," opt-out pledges, easily avoided penalties), introducing punishment is unlikely to improve efficiency unless participation rates and ambition are high.** Harsh penalties do not improve efficiency in these designs if players can simply avoid sanctioning (Del Ponte et al., 2025).

- **Non-payoff behavioral findings (cooperation rates, trust, norm compliance) are informative for mechanism understanding, but should not be directly mapped to efficiency in prediction tasks.**

- **Baseline ("control") efficiency is a critical anchor for prediction: the marginal gain from punishment diminishes as control efficiency rises, and the risk of wasted resources due to excessive punishment increases.**

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions:**
- **player_count** (directly informed in all relevant experiment reports)
- **num_rounds** (routinely reported; long games allow cumulative efficiency results)
- **mpcr** (often specified in payoff formula; important moderator)
- **punishment_cost** (essential, highly informative for efficiency effects)
- **punishment_tech** (nature of peer or centralized punishment, deterministic or probabilistic)
- **all_or_nothing** (continuous vs. binary contributions; present in methods)

**Indirect/contextual dimensions:**
- **chat** (occasionally manipulated or discussed as impacting coordination/trust)
- **default_contrib** (opt-in vs. opt-out rarely central, sometimes mentioned re: framing)
- **reward_exists, reward_cost, reward_tech** (seldom present as main manipulation; evidence mostly missing or contextual)
- **show_n_rounds, show_other_summaries, show_punishment_id** (sometimes described in method details; not systematically tested)
  
**Design dimensions essentially missing or only minimally covered:**
- **default_contrib**
- **reward_exists, reward_cost, reward_tech**
- **show_n_rounds, show_other_summaries, show_punishment_id** (mostly descriptive or context-specific; not core focus)

# 7) Important Limitations

- **Incomplete coverage of design space:** Only a subset of the 14 key dimensions are systematically manipulated or tested in ways that inform prediction of efficiency effects; especially sparse are studies varying reward mechanisms, contribution framing, or information treatments.

- **Behavioral outcomes often substituted for efficiency:** Many studies focus on cooperation rates, punishment frequency, or trust proxies rather than direct payoff-based outcomes; mechanism findings must not be over-interpreted as predicting efficiency.

- **Variability in punishment design and context:** Differences in punishment cost, mode (peer vs. centralized), voluntariness, and enforceability create heterogeneity in outcomes. This complicates transferability of findings from one paradigm/deign to another.

- **Boundary conditions and moderators not always clear:** Baseline efficiency, player motivation, cultural context, or perceived legitimacy of punishment can moderate effects, but not all relevant moderators are tested for.

- **Ambiguity in ambiguous or marginal designs:** Some included games are only adjacent to PGGs, and the translation of findings from these settings to standard PGG efficiency may not hold.

- **Scarcity of large-N, high-powered, multi-condition studies reporting direct efficiency outcomes across a wide design parameter grid. Most "actionable" evidence comes from a handful of recent, well-controlled experiments.**

In summary, while several high-relevance studies provide solid base evidence that enabling costly peer punishment in standard PGGs can increase group efficiency compared to control—*but only when punishment is well-calibrated, not excessively costly, and not easily avoided*—the literature as a whole contains gaps in design coverage, a frequent mismatch between behavioral and payoff outcomes, and significant context dependency. Prediction should rely on close matching with these key design features and control outcomes, and avoid generalizing from non-payoff behavioral findings or marginally relevant settings.
