# 1) Evidence Base

The paper set comprises 32 studies with a mixture of theoretical models, simulations, laboratory experiments, field experiments, and conceptual or review-style theoretical work. The base is moderately broad in scope but, concerning the specific prediction task—how enabling peer punishment affects group efficiency in public-goods-game (PGG) settings, conditional on control efficiency—the majority of evidence is **theoretical** or **mechanistic**, with relatively few robust **empirical** studies reporting direct efficiency outcomes under controlled manipulation of punishment. A subset of papers report on adjacent or structurally similar games (trust, principal-agent, regulatory dilemmas), often with payoff-related outcomes. A significant portion is focused on behavioral/mechanism-level outcomes (e.g., cooperation rates) rather than group payoffs or efficiency. Very few studies directly manipulate or systematically report on all key **game design dimensions**, leading to patchy coverage for parameter-level prediction.

# 2) Task Relevance

### pgg_or_variant
- **Exact relevance**: Several papers (e.g., Vasconcelos et al., 2022; Quan et al., 2023; Wu & Sun, 2022; Park, 2022) use public goods games or very close variants.
- **Close/adjacent**: Many others use adjacent games (e.g., trust games, regulatory dilemmas, principal-agent settings) that share free-riding or social dilemma structure but differ from standard PGGs in important strategic or institutional details.
- **Weak/none**: A minority analyze broader or only conceptually related settings (e.g., multispecies mutualism or business cooperation).

### punishment_or_sanctions
- **Exact/close relevance**: The majority of the theory and model papers consider explicit punishment or sanctions as key mechanisms; some experiments also feature implemented punishment treatments.
- **Adjacent**: A subset broaden definition to include government fines, carbon taxes, institutional sanctions, or social/psychological punishment.
- **None**: Some papers include no punishment at all and serve only as context or control.

### efficiency_or_related_payoff_outcome
- **Exact**: Only a limited subset report group efficiency (payoff relative to full cooperation) or total group payoff as primary or secondary outcomes (e.g., Vasconcelos et al., 2022; Lim & Capraro, 2022; Suzuki & Ishiwata, 2022; Wei et al., 2025).
- **Close/adjacent**: Many report on total contributions, investment, or similar proxies that are closely related but not identical to efficiency.
- **Weak/none**: The bulk focus on behavioral measures (contribution rates, cooperation frequency, compliance, stability of cooperation) with no explicit link to payoffs or efficiency.

# 3) Outcomes Measured In The Literature

- **Payoff-based outcomes** (directly relevant): 
    - Group efficiency (ratio to max possible payoff): Reported in select papers (e.g., Vasconcelos et al., 2022; Lim & Capraro, 2022; Suzuki & Ishiwata, 2022; Wei et al., 2025).
    - Group/total payoff, total profit, welfare, collective surplus.
- **Behavioral/non-payoff outcomes** (distinct from payoffs):
    - Cooperation or contribution rates, norm compliance, investment behavior.
    - Stability of strategy equilibria.
    - Punishment frequency, fairness, honesty, or trust.
- **Proxy outcomes**: Collective investment, transition rates to cooperation, total contributions (behavioral proxies for efficiency, but not equivalent).

It is critical to note that much of the evidence, even if supportive of cooperation, is grounded in non-payoff behavioral outcomes rather than efficiency per se.

# 4) Main Findings Relevant To Prediction

- **Punishment is often, but not always, associated with higher efficiency in PGGs and very close variants**, especially when the punishment institution is appropriately structured, not too costly, and aligned with the collective action problem at hand (Vasconcelos et al., 2022; Lim & Capraro, 2022; Suzuki & Ishiwata, 2022).
- **Institutional and contextual moderators are central:** The scale and method of institution adoption (collective vs. individual choice), alignment between institutional scope and public good, and information/memory conditions crucially affect whether punishment increases efficiency (Vasconcelos et al., 2022). In trust games/adjacent games, network structure also moderates the effectiveness of punishment at increasing efficiency (Lim & Capraro, 2022).
- **Punishment can backfire or crowd out cooperation:** In some real-world field settings, enabling punishment reduced collective investment and group outcomes (Amirova et al., 2022), highlighting that punishment can sometimes decrease efficiency, particularly when it undermines intrinsic motivation.
- **Behavioral gains ≠ efficiency gains:** Many papers show that punishment increases cooperation rates or compliance, but, as some theory papers caution, this does not always yield higher efficiency. If costs of punishment or errors in targeting are high, punishment can reduce group payoffs despite increases in observed cooperative behavior (Rubin, 2022; Goodman, 2022).
- **Punishment effectiveness depends on design details:** Graded or dynamic punishment rules are generally more effective at stabilizing cooperation (Quan et al., 2023; Wang & Cui, 2022; Jiang & Zheng, 2024), but payoff impacts are typically inferred and not directly reported.
- **Complementarity with rewards and other tools:** Punishment is more effective, or only effective, at increasing efficiency when combined with rewards, performance appraisals, or compensation systems in some organizational or governance settings (Li & Jiang, 2023; Zhao & Zou, 2025).
- **Parametric dependences:** Cost and magnitude of punishment, as well as network characteristics, public good size, and game repetition, are frequently modeled but rarely tested in multi-factorial empirical designs.
- **Information and learning conditions:** Greater transparency, longer memory, and access to history enhance the ability of groups to realize efficiency gains from punishment institutions (Vasconcelos et al., 2022).

# 5) Prediction Guidance

- **Direct empirical guidance is limited**: Only a small number of studies provide directly comparable, parametric evidence on the efficiency effect of peer punishment in classic PGGs. Where this exists, punishment typically increases group efficiency if the institution is effective, punishment is not excessively costly, and design conditions (e.g., memory, information) are favorable.
    - For new game designs matching the scope of Vasconcelos et al. (2022) or Lim & Capraro (2022), use their moderator findings: efficiency effect is strongest with collective-choice punishment for collective goods, matched institutional scope, high-quality information, and moderate punishment costs.
    - In networked or structured populations, punishment is more effective at lower cost thresholds due to support from network structure (Lim & Capraro, 2022).
    - Real-world or field settings may not follow lab results: evidence from field experiments (Amirova et al., 2022) warns that punishment can reduce efficiency by crowding out intrinsic motivation.
- **When control efficiency is already high,** punishment may have limited or negative effects (Rubin, 2022; Amirova et al., 2022).
- **Efficiency prediction from behavioral proxies is risky:** Findings based solely on increased cooperation rates, norm compliance, or stability should not be mechanically mapped to increased efficiency without considering punishment costs and possible crowding effects.
- **Design dimensions are critical:** As explored below, moderator effects found in model and meta-study work can guide which dimensions should be prioritized in efficiency prediction when enabling punishment. However, dimensional coverage is incomplete.

# 6) Design Dimensions Highlighted Across Papers

**Dimensions directly informed by payoff outcome studies:**
- `player_count`, `num_rounds`, `mpcr`, `punishment_cost`, `punishment_tech`: Frequently modeled (Vasconcelos et al., 2022; Lim & Capraro, 2022; Suzuki & Ishiwata, 2022; Wei et al., 2025); some empirical or parametric sweep evidence, but mostly in theory/modeling work.
- `chat` (communication): Empirical support that communication increases efficiency, but its interaction with punishment is rarely explored jointly (Herne et al., 2023; Amirova et al., 2022).
- `all_or_nothing`, `default_contrib`: Occasionally manipulated; limited systematic evidence on their interaction with punishment’s effect on efficiency.
- `show_other_summaries`, `show_n_rounds`: Considered in a handful of studies (Vasconcelos et al., 2022).
- `reward_exists`, `reward_cost`, `reward_tech`: Some studies analyze joint or comparative effects of reward and punishment (Li & Jiang, 2023; Zhao & Zou, 2025), indicating that their presence can moderate or amplify effects on efficiency.

**Dimensions only contextually or sparsely discussed:**
- `show_punishment_id`: Rarely, if ever, examined in relation to efficiency.
- `punishment_magnitude`: Sometimes considered in combination with cost; more often in models than in experiments.
- `default_contrib`: Framing variation (opt-in/opt-out) is rarely isolated.

**Dimensions effectively missing or only theorized:**
- Many papers do not test, or only speculate about, dimensions such as the explicit framing (`default_contrib`), details of punishment targeting or identification (`show_punishment_id`), or information presentation (`show_other_summaries`). Direct, systematic evidence about how these factors moderate efficiency is sparse.

# 7) Important Limitations

- **Limited direct empirical evidence:** There are few experiments that directly report efficiency or total group payoff for both control and punishment-enabled conditions under systematic variation of multiple design dimensions.
- **Over-reliance on behavioral proxies:** Many claims about efficiency are inferred from increased cooperation or investment rates, but, as several theory papers warn, such proxies can be misleading, especially if punishment is costly or misapplied.
- **Field versus laboratory mismatch:** Lab experiments typically show more positive effects of punishment on efficiency, whereas some real-world/field studies reveal neutral or negative effects due to complex social and motivational interactions (Amirova et al., 2022).
- **Insufficient dimensional detail:** While important parameters (e.g., player count, punishment cost, network structure) are often modeled, comprehensive empirical tests of their moderator effect on efficiency are rare.
- **Ambiguity in definitions and measurement:** Not all papers clearly distinguish between efficiency (payoff-based) and behavioral outcomes, and some use proxies (e.g., collective investment, compliance) without explicit calculation of efficiency or group payoff.
- **Dependence on institutional and informational context:** The positive effect of punishment on efficiency is often contingent on appropriate institutional design and learning conditions, which may not be easily matched between studies or prediction targets.
- **Risk of publication/metastudy over-optimism:** Some meta-analytic summaries focus on positive cases ("when punishment works"), potentially underrepresenting cases or parameter regimes where punishment has no effect or reduces efficiency.
- **Sparse exploration of complex interactions:** Interaction effects between communication, reward, punishment identification, information conditions, and other dimensions are largely untested in combination.

---

In sum, the literature provides **conditional** and **context-dependent** support for the positive efficiency effects of punishment in PGGs, moderated by key design dimensions, but with important empirical, conceptual, and generalizability gaps for quantitative prediction in new or untested parameter regimes.
