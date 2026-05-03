# 1) Evidence Base

The paper set consists primarily of theoretical and simulation studies complemented by a smaller number of empirical and experimental papers, including both laboratory and real-world field experiments. The majority of papers focus on public goods games (PGGs) and closely related multiplayer social dilemmas, with a strong emphasis on evolutionary models, agent-based simulations, and analytical approaches. Many studies explore variants: structured and unstructured populations, network effects, feedback mechanisms, and diverse punishment or reward technologies. The literature is relatively broad with respect to the variety of mechanisms (punishment, reward, exclusion, voluntary participation, feedback, etc.) and outcome variables assessed, but it is narrower with respect to exact matches to the target prediction task—namely, predicting quantitative efficiency changes from specified game design dimensions when peer punishment is enabled.

The bulk of the evidence relevant for efficiency effects comes from theoretical models (e.g., replicator dynamics, network simulations) with a smaller but critical set of experimental and field evidence. Several papers provide phase diagrams, analytical boundaries, or direct efficiency measures, but a large cluster of the literature measures only cooperation rates, strategy frequencies, or qualitative behavioral outcomes, requiring caution in translating their findings to efficiency predictions.

# 2) Task Relevance

**pgg_or_variant:**  
- *Exact relevance:* Most papers explicitly model public goods games or mathematical structures equivalent to repeated PGGs (e.g., Bahbouhi et al., 2024; Cui et al., 2019; Wang et al., 2011, 2025; Liu et al., 2024; Lv et al., 2023).
- *Close relevance:* Some studies examine collective-risk games, threshold PGGs, or donation/leader models structurally adjacent to PGGs but with significant differences in payoff structure (e.g., Jiang et al., 2023; Murase & Baek, 2021).
- *Adjacent/weak relevance:* Many papers model the prisoner's dilemma, voluntary dilemmas, or group bargaining, which offer relevant insights into social dilemmas and sanctioning but are structurally distinct from PGGs.
- *None:* A subset of reviewed studies deals with environments unrelated to PGGs.

**punishment_or_sanctions:**  
- *Exact relevance:* There is substantial coverage of peer punishment, institutional/imposed punishment, exclusion, and related sanctioning mechanisms in the PGG context (e.g., Bahbouhi et al., 2024; Wang et al., 2011; Cui et al., 2019; Wang et al., 2025; Lv et al., 2023).
- *Close/adjacent relevance:* Some papers focus on reward, exclusion, coalitions, or non-punitive mechanisms with brief or indirect discussion of punishment, or model punishment in adjacent games (PDG).
- *None:* Many papers focus on reward-only or other interventions, with no discussion of punishment.

**efficiency_or_related_payoff_outcome:**  
- *Exact/close relevance:* A critical subset measures efficiency directly as group payoff relative to the full-cooperation benchmark (e.g., Bahbouhi et al., 2024; Wang et al., 2011; Cui et al., 2019; Wang et al., 2025; Liu et al., 2024; Lv et al., 2023; Murase & Baek, 2021; Liu et al., 2023; Wang et al., 2015).
- *Adjacent relevance:* A large portion report only on cooperation/contribution rates or strategy prevalence, inferring likely efficiency improvements but not measuring efficiency explicitly.
- *Weak/none:* Several studies report only on behavioral/strategy outcomes or analyze mechanisms rather than aggregate payoff.

**Summary:**  
Overall, the evidence base is *strongest for core PGGs with explicit punishment and at least some efficiency outcomes*. However, much of the punishment literature relies on theoretical or simulation results, with fewer experimental demonstrations of efficiency effects. Many studies report on non-payoff behavioral outcomes, providing only inferential support for downstream efficiency predictions.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (direct):**  
  - Efficiency (ratio of actual group payoff to full cooperation): e.g., Bahbouhi et al., 2024; Wang et al., 2011, 2015, 2025; Cui et al., 2019; Liu et al., 2024; Lv et al., 2023; Murase & Baek, 2021.
  - Average payoff, group profit/welfare, total surplus: similar set as above.
  - Probability of reaching collective targets (proxy for efficiency): Jiang et al., 2023.
- **Payoff-related outcomes (adjacent):**  
  - Average contribution, total earnings per strategy, public good abundance, collective revenue (e.g., Fabbri et al., 2019; Kang et al., 2024).
- **Non-payoff behavioral outcomes:**  
  - Contribution rate, cooperation frequency, prevalence/strategy mix (most common outcome).
  - Norm compliance, altruistic punishment frequency, strategy dynamics, phase transitions.
  - Punishment frequency per se, types or targets of punishment.
- **Mechanism/process outcomes:**  
  - Evolutionary stability, updating rule effects, norm emergence.
  - Effects of feedback mechanisms, exclusion, exit, or insurance.

**Distinction:**  
Papers reporting only behavioral outcomes (cooperation/punishment frequencies) seldom measure efficiency directly. Where only behavioral outcomes are available, efficiency predictions must be made cautiously and are only inferential.

# 4) Main Findings Relevant To Prediction

## Cross-paper synthesis on punishment’s effect on efficiency:

**General pattern:**  
- Enabling peer punishment in PGGs *usually increases efficiency* (group payoff relative to full cooperation), especially when the baseline (control) is inefficient due to low cooperation (e.g., Bahbouhi et al., 2024; Wang et al., 2011; Cui et al., 2019; Wang et al., 2025; Liu et al., 2024; Lv et al., 2023).
- The magnitude of the efficiency gain depends on game parameters: **group size, number of rounds, mpcr, punishment cost and magnitude, presence of entry fees, feedback mechanisms, and group structure.**

**Important dimensions and moderators:**
- **Synergy factor (mpcr):** Higher mpcr amplifies the effect—punishment is more likely to promote efficiency when mpcr is high (Cui et al., 2019; Liu et al., 2024; Lv et al., 2023).
- **Punishment cost and effectiveness:** Low punishment cost and high effectiveness promote high efficiency; high cost or weak punishment can reduce or negate efficiency gains. Excessive punishment cost can lead to inefficiency by over-penalizing, while insufficient punishment fails to suppress defection (Liu et al., 2024; Wang et al., 2011, 2025; Bahbouhi et al., 2024).
- **Design of punishment/updating mechanism:** Cooperator-driven or reputation-based punishment is generally more effective than indiscriminate punishment (Cui et al., 2019; Bahbouhi et al., 2024; Quan et al., 2022, 2023).
- **Group structure:** Structured (networked) populations can moderate the effectiveness—some network topologies (e.g., scale-free) are less responsive to punishment (Shutters, 2012).
- **Entry and voluntary participation:** Availability of exit/entry options and moderate entry fees can enhance the effect of punishment by sustaining cooperation at higher efficiency (Wang et al., 2011, 2015).
- **Feedback mechanisms:** Local or state-dependent feedback (mpcr increasing with contributors) can sharply enhance punishment's efficiency-boosting effect (Wang et al., 2025).
- **Institutional implementation:** Third-party/institutional punishment often sustains higher efficiency if credibly implemented, but design details are critical (team decision rules, reporting, anti-social punishment; Bahbouhi et al., 2024; Liu et al., 2023).

**Limitations and deviations:**
- **Threshold effects/bistability:** In several models, punishment must exceed a critical threshold (in probability or severity) to produce high efficiency; below this, it may have little or no effect (Liu et al., 2024; Jiang et al., 2023; Ding et al., 2025).
- **Non-monotonicity:** Excessive punishment spending or too high cost/fine ratio can *reduce* efficiency (Nuño et al., 2010; Liu et al., 2024).
- **Contextual moderators:** Memory, updating rules, team/unanimity rules, reputation/exclusion mechanisms, and initial conditions can all modulate the impact (Kaiping et al., 2014; Bahbouhi et al., 2024; Kang et al., 2024).
- **Ambiguity in adjacent settings:** In adjacent games (e.g., PDG, insurance/coalition models), effectiveness does not always transfer (Iwamura et al., 2020).

# 5) Prediction Guidance

- **Direct quantitative prediction of treatment efficiency is best grounded in studies measuring group efficiency/payoff in PGGs with controlled variations in punishment and relevant parameters** (Bahbouhi et al., 2024; Wang et al., 2011, 2015, 2025; Cui et al., 2019; Liu et al., 2024; Lv et al., 2023). Where such studies align with the target game design, their findings can support both the expected direction and magnitude of efficiency change.
- **If the control (no-punishment) game is inefficient (low baseline efficiency), enabling punishment is highly likely to produce a gain in efficiency—provided the punishment cost is moderate and the punishment technology is effective** (robustly observed in both lab and theoretical studies).
- **Game design dimensions (player count, mpcr, punishment cost, punishment magnitude, voluntary participation, structure of feedback, and decision rules) are all critical moderators:**
  - *High mpcr, low-to-moderate punishment cost, and high punishment effectiveness* predict larger efficiency gains.
  - *Larger groups* sometimes require higher punishment thresholds to sustain efficiency improvement (Jiang et al., 2023).
  - *Entry fees* and voluntary participation can both enable the system to sustain high efficiency with punishment; without them, the effect may vanish.
  - *Team-based/unanimity decision rules* filter out counterproductive punishment, enhancing efficiency gains.
  - *Institutional or third-party punishment* can generate stable high efficiency when credible and sufficiently severe.
- **Indirect or adjacent literature (focusing on cooperation rates) consistently finds that punishment increases cooperation, which usually but not always translates into higher efficiency—but the translation is context-dependent and influenced by punishment cost.**
- **Predictions should be cautious in scenarios with high punishment cost, anti-social punishment, poorly targeted sanctions, or institutional/legal/psychological features that weaken punishment credibility or effectiveness.** Efficiency gains are not universal and can reverse or disappear under such conditions.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed from evidence (studied with efficiency outcomes):**
- `player_count` (group size): Studied in both theory and experiment—larger groups require higher punishment risk (Jiang et al., 2023; Cui et al., 2019).
- `num_rounds`: Present in nearly all repeated game/lab experiment models.
- `mpcr`: Explicitly manipulated in most efficiency studies (Cui et al., 2019; Liu et al., 2024; Wang et al., 2011, 2025; Lv et al., 2023).
- `punishment_cost`, `punishment_tech` (magnitude/severity): Heavily stressed as determinants of efficiency, with phase transitions, non-monotonicity, or threshold effects (Liu et al., 2024; Nuño et al., 2010).
- `reward_exists` (less often with efficiency as main outcome): Some studies include combined or alternative reward mechanisms for comparison (Wang et al., 2011, 2015; Cui et al., 2019).

**Indirectly or inconsistently informed:**
- `all_or_nothing`, `default_contrib`: Sometimes specified; findings suggest qualitative impacts but typically not varied to isolate effects on efficiency.
- `chat`, `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Infrequently manipulated in the efficiency-focused literature; inclusion mainly in lab experiments or specific mechanism studies—effects mostly contextual.
- `reward_cost`, `reward_tech`: Explored where reward is compared to punishment (Wang et al., 2011; Mondal et al., 2022), but often peripheral to the central efficiency findings regarding punishment.

**Contextually discussed/ rarely isolated:**
- `chat`, `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Included in descriptions or as experimenter controls, but seldom as focal variables in efficiency outcome comparisons.

**Effectively missing for direct efficiency prediction:**
- Specific manipulations of visual feedback (`show_n_rounds`, `show_other_summaries`, `show_punishment_id`), contribution framing (`default_contrib`), chat, and detailed reward technology are generally underexplored in efficiency-focused punishment studies.

# 7) Important Limitations

- **Prevalence of theory and simulation over empirical evidence:** Most efficiency findings derive from theoretical analyses and simulations; strong, well-powered experimental tests are less numerous (notably Bahbouhi et al., 2024; Jiang et al., 2023).
- **Translation from cooperation rate to efficiency is not always valid:** Many studies report only behavioral outcomes; high cooperation does not guarantee high efficiency, especially if punishment costs are excessive or anti-social punishment is significant.
- **Limited coverage of some design dimensions:** Many prediction-dimension variables (especially those relating to information provision, chat, contributor anonymity, and framing effects) have received little attention in the efficiency literature.
- **Ambiguity in adjacent models:** For studies using variants (e.g., collective-risk games, donation/leader models, insurance/coalition mechanisms), mapping results to standard PGGs with peer punishment may misstate effects.
- **Second-order free rider and anti-social punishment:** Several models show that if these problems are not addressed by game design or team decision rules, the expected increase in efficiency can be greatly reduced or even reversed.
- **Threshold/non-monotonic effects:** The efficiency impact of punishment is often non-linear; gains may require a minimum punishment intensity or fine, and excessive cost can erode or negate improvements (Liu et al., 2024; Nuño et al., 2010).
- **Contextual and dynamic influences:** Evolutionary assumptions, updating rules, memory, initial conditions, and endogenous behavioral heterogeneity can all modify predicted efficiency, leading to model sensitivity and challenges in generalization (Kaiping et al., 2014; Bahbouhi et al., 2024).
- **Incomplete empirical calibration:** While mechanisms and moderators are well-mapped, the literature provides limited systematic mapping of parameter ranges to observed effect sizes in efficiency, restricting the precision of downstream predictions.
- **Sparse focus on combined or competing reward and punishment regimes:** While many studies compare punishment to reward, few systematically analyze the joint impact or optimal balance on efficiency as a function of game design.

---

**In summary:**  
The literature strongly supports that punishment generally increases efficiency in PGG-like environments, particularly when designed with effective cost/fine ratios, moderate group size, and sufficient severity to deter defection. Predictions should account for threshold and non-monotonic effects, sensitivity to structural design dimensions, and the fact that efficiency gains are not guaranteed if punishment is weak, too costly, or poorly targeted. Dimension-level data are robust for group size, rounds, mpcr, and punishment parameters; other variables are less well-covered, limiting comprehensive prediction across the full space of design dimensions. Where only cooperation rates are available, efficiency predictions must be made inferentially and with acknowledged uncertainty.
