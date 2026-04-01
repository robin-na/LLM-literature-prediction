# 1) Evidence Base

The literature set is **broad and predominantly theoretical**, with 206 papers, nearly all using **theoretical models and agent-based simulations**, and very few reporting on laboratory or field experiments. The coverage of public goods game (PGG) structures is deep, including classic linear PGGs, spatial/networked variants, threshold and resource-based dilemmas, and adjacent games such as iterated Prisoner's Dilemma (PD) and common-pool resource management tasks. Most papers focus on **mechanisms—especially forms of punishment, reward, and institutional design**—and supply detailed mechanism and parameter analyses, but **empirical/experimental confirmation is rare**. 

Outcomes are predominantly **behavioral (cooperation/contribution rates, strategy prevalence)**, but a substantial subset explicitly report or calculate **payoff-based efficiency** (group payoff vs. social optimum). Many models are constructed so that average payoff and efficiency can be interpreted analogously to experimental PGGs, but often require careful interpretation. The set is weighted toward **mechanistic and conditional findings**, with common reporting of the moderators, thresholds, and intervention parameter ranges that determine whether punishment helps or harms efficiency.

# 2) Task Relevance

**a) `pgg_or_variant`:**

- **exact**: ~40–50% of papers use standard PGGs (linear or threshold, with or without spatial structure).  
- **close**: Remainder use close variants—resource games, threshold/dilemma settings, common-pool resources, repeated PD, or donation games with public-good-like structure.
- **adjacent/weak**: Some analyze trust, division-of-labor, or signaling games with mechanisms adjacent to PGGs.  
- **none**: Very few.

**b) `punishment_or_sanctions`:**

- **exact**: Many papers implement explicit costly punishment, including peer, institutional, probabilistic, threshold-triggered, or third-party punishment.
- **close**: Substantial coverage of reward, mixed incentives, exclusion, partner choice (walk-away), and dynamic rules that function similarly to punishment.
- **adjacent**: Some focus on reputation, ostracism, or soft/behavioral punishment.
- **none**: About a third of the set, especially baseline/control condition papers.

**c) `efficiency_or_related_payoff_outcome`:**

- **exact**: A sizeable set directly report efficiency, group payoff relative to optimum, surplus, or total welfare.
- **close**: Many more interpret efficiency indirectly (e.g., as prevalence of cooperators when model structure makes cooperation ≈ social optimum).
- **adjacent/weak**: Large number focus on non-payoff outcomes (contribution rates, behavioral strategies, trust).
- **none**: A minority (theoretical/conceptual essays).

**Summary**: There is **strong coverage** of PGG and variant structures, **comprehensive coverage** of punishment/sanction mechanisms (peer, institutional, hybrid), and **moderate but sufficient direct coverage** of efficiency or direct payoff-based outcomes for modeling predictions, with the remainder providing highly relevant indirect behavioral/mechanistic evidence.

# 3) Outcomes Measured In The Literature

- **Payoff-based outcomes (efficiency, group payoff, welfare):**
  - Directly analyzed in a meaningful minority of papers—a core set provide **explicit efficiency or group payoff as primary outcome**.
  - Many others supply **analytical expressions, phase diagrams, or simulated payoffs** mapping design parameters (e.g., punishment cost, MPCR, player count) to efficiency.
  - Efficiency is usually defined as **actual group payoff over socially optimal payoff** (full cooperation).
  - Some models specify efficiency as "resource sustainability" or "market size and average accumulated wealth" in resource or economic variants.

- **Non-payoff behavioral outcomes:**
  - Widely reported—cooperation/contribution rates, strategy frequencies, norm compliance, prevalence of punishment/reward, evolutionary stability of strategies.
  - These are often indirectly interpreted as proxies for efficiency but may diverge sharply, especially when **punishment costs are high or when second-order free riding occurs**.

**Distinction is routinely made** (and should be retained in synthesis): models/papers that report only behavioral outcomes should be used as **supporting or cautionary evidence** rather than direct evidence on efficiency.

# 4) Main Findings Relevant To Prediction

**Synthesis of the efficiency impact of enabling peer punishment in PGG(-like) environments:**

- **General Finding**: **Enabling punishment in PGGs *usually* increases efficiency** compared to a no-punishment baseline, *but only* if punishment cost and effectiveness fall within favorable ranges, the game is not already highly cooperative, and side-effects (such as retaliation, antisocial punishment, or waste) are limited (e.g., Sun et al., 2025; Huang et al., 2024; Cui et al., 2022; Zefferman, 2023).
- **Conditionality and Moderators**:
  - **Baseline Efficiency (control condition)**: Punishment shows the greatest marginal efficiency gain when the control game is at *low to moderate efficiency* (many defectors, low cooperation).
  - **Punishment Cost and Effectiveness**: The *ratio* of punishment impact to punisher's cost (punishment efficiency) is critical (Bühren et al., 2023; Zefferman, 2023). Low-cost, high-effectiveness punishment robustly increases efficiency; high-cost or low-effectiveness may actually reduce payoff below the no-punishment baseline, especially due to wasted resources and retaliation cycles (Cooney, 2025; Bühren et al., 2023; Zefferman, 2023).
  - **Targeting/Technology**: Institutional, *targeted* punishment (especially at clear defectors or the lowest contributor) is more likely to induce full cooperation and maximize efficiency (Huang et al., 2024; Sun et al., 2025). Universal, untargeted, or misapplied punishment can waste resources or even backfire.
  - **Group Size (`player_count`)**: Larger groups require more efficient or institutionalized punishment—*peer punishment may not scale*, and the effectiveness of voluntary or peer punishment often declines with group size (Zefferman, 2023; Zefferman, 2023; Ishikawa & Fontanari, 2025).
  - **MPCR**: Lower marginal per capita return makes cooperation harder; here, punishment can be crucial to rescue efficiency (Cui et al., 2022; Sun et al., 2025; Zefferman, 2023).
  - **Network Structure**: Spatial and networked PGGs with small-world properties, clustering, and appropriate punishment spread amplify the efficiency benefits of punishment (Cui et al., 2022).
  - **Punishment Frequency and Social Preferences**: Punishment is most efficient when applied *rarely but strongly* to defectors; repeated, mild, or misapplied punishment can drain resources (Bühren et al., 2023; Gao & Li, 2023).
  - **Presence of Rewards**: When combined with rewards (i.e., both punishment and reward enabled), *efficiency is often higher* than with either alone, especially when control efficiency is low (Sun et al., 2025; Huang et al., 2024; Yang & Yang, 2024).
  - **Voluntary vs. Institutional Funding**: *Tax/institutional ("pool") punishment and reward* are often more effective than voluntary/peer mechanisms at achieving high efficiency, especially in large groups (Prétôt et al., 2024; Yang & Yang, 2024; Powers et al., 2023).

- **Critical thresholds and bi-stability**: Many models find **sharp transitions**: below a threshold in punishment severity or contributor willingness, punishment has little/no effect; above it, full cooperation and maximum efficiency are equilibrium (Huang et al., 2024; Gao et al., 2025). *Initial conditions* and the presence of already-cooperative groups can determine final outcome due to bi-stability.

- **Negative and Mixed Effects**: When **punishment cost is high, monitoring is inefficient, or group size is large without centralized punishment, enabling punishment can lower efficiency relative to control** (Bühren et al., 2023; Ishikawa & Fontanari, 2025; Cooney, 2025). *Antisocial punishment* or the possibility of undetectable defection can negate or even reverse the efficiency benefit (García & Traulsen, 2025; Goodman, 2023; Kurokawa, 2023).

- **Adjacent findings (PD and variants)**: Models of repeated/dyadic games, trust games, and related collective action problems **generally reinforce the main conclusion**: *punishment is conditionally efficiency-enhancing*, with effectiveness modulated by cost, group size, memory, strategy set, and punishment targeting (Murase, 2025; Gioffré & Tampieri, 2025; Nirjhor & Nakamaru, 2023; Zhou et al., 2022).

# 5) Prediction Guidance

- **When and How to Expect Efficiency Gains from Punishment**:
  - If the **control game has low to moderate efficiency** and peer (especially targeted or institutional) punishment is enabled with **cost and effectiveness in an optimal range**, predict a **substantial absolute and proportional increase in average efficiency** (often approaching the social optimum if punishment is strong and targeted) (Sun et al., 2025; Huang et al., 2024; Zefferman, 2023).
  - **For moderate-to-large groups** or when **peer punishment is inefficient**, expect efficiency gains only if **institutional or tax-based punishment is implemented** and at sufficient scale (Prétôt et al., 2024; Yang & Yang, 2024; Ishikawa & Fontanari, 2025; Powers et al., 2023).
  - **If control efficiency is already high** (cooperation nearly at optimum), punishment may yield little further benefit and could even **reduce efficiency by introducing unnecessary costs** (Bühren et al., 2023; Gao et al., 2025).
  - For **high punishment cost, weak effectiveness, or untargeted application**, **do not expect a positive efficiency effect**—punishment may waste resources or encourage cycles of retaliation, lowering overall group payoff (Bühren et al., 2023; Cooney, 2025; Goodman, 2023).
  - **Dimension-by-dimension mapping** (see next section) is essential; uncritical extrapolation or simple rule-of-thumb applications will fail to capture known non-linearities and boundary effects.

- **Prediction Inputs Mapped to Literature**:
  - **Game design dimensions** (player count, rounds, all_or_nothing, mpcr, punishment_cost, punishment_tech) are **well studied**—allow parameterized, conditional quantitative or qualitative prediction of efficiency change (see Huang et al., 2024; Zefferman, 2023; Bühren et al., 2023).
  - **Other dimensions** (chat, default_contrib, reward_exists/cost/tech, show_n_rounds, show_other_summaries, show_punishment_id) are **less directly studied**, but evidence suggests **chat/reputation mechanisms can be strong substitutes**, and **reward can supplement or, in high baseline-cooperation settings, substitute for punishment** (Janssen et al., 2022; Prétôt et al., 2024; Chan et al., 2024).
  - **Moderators such as network structure, population heterogeneity (social preferences), monitoring/implementation technology, corruption, and strategy set** are **critical according to the literature**.

- **When using indirect evidence (from behavioral outcomes):**
  - Increase prediction uncertainty and avoid quantifying efficiency changes unless behavioral-to-payoff mapping is clear (e.g., settings where "all cooperation" guarantees optimal efficiency).

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**

- `player_count` (group size): Heavily studied as a moderator of punishment's efficiency effect (Sun et al., 2025; Zefferman, 2023; Powers et al., 2023).
- `num_rounds`: Many models are repeated games; predictions are sensitive to round number and discounting (Gioffré & Tampieri, 2025).
- `mpcr` (marginal per-capita return): Core parameter in all main PGG findings; low MPCR strengthens the need for punishment.
- `all_or_nothing`: Studied, especially in binary-contribution PGGs or threshold games.
- `punishment_cost`, `punishment_tech` (effectiveness): Universally covered—key moderators in every model with punishment.
- `reward_exists`, `reward_cost`, `reward_tech`: Often included as joint mechanisms (especially for hybrid or threshold-triggered interventions); strong synergy/interaction effects reported.
- `punishment_exists`: Always manipulated (the core treatment dimension).

**Indirectly Informed or Contextually Discussed:**

- `show_n_rounds`, `show_other_summaries`, `show_punishment_id` (information/observability): Some models explore observability (monitoring technology, transparency), but empirical mapping is sparse.
- `chat`: Included in a minority of models/experiments, but *shown to strongly boost efficiency* (Janssen et al., 2022).
- `default_contrib`: Framing effects lightly studied, usually not as central moderators.

**Effectively Missing or Addressed Only in Precautionary Warnings:**

- Heterogeneity in **social preferences** and **population composition**: Heavily discussed as moderators (Bühren et al., 2023; Zefferman, 2023), but not always mapped directly to dimensions above.
- **Corruption and antisocial punishment**: Not systematically parameterized.
- **Realistic behavioral noise, error, or misimplementation**: Discussed as negative moderators.
- **Empirical laboratory data, especially in multi-round or large-N settings with all dimensions manipulated**, is rare.

# 7) Important Limitations

- **Empirical Sparsity**: Much of the actionable evidence is theoretical or simulation-based. There is a shortage of experimental/lab studies reporting both control and punishment-enabled efficiency under systematically varied design parameters.
- **Mapping from behavior to efficiency**: Many models report cooperation rates but not efficiency or total payoff; assuming a direct translation is often unwarranted, especially when punishment is costly or when antisocial punishment exists.
- **Parameter boundary effects, bi-stability, and non-monotonicities**: Literature consistently shows that punishment can be highly non-linear (diminishing or even negative marginal returns at high cost, retaliation, or poorly targeted application), so simple main-effects models will mispredict outside well-studied regions.
- **Heterogeneity and strategy set**: The impact of punishment depends heavily on population composition (e.g., social preference structure, susceptibility to norm enforcement, possibility for antisocial punishment or evasion).
- **Institutional realism**: Many findings relating to institutional or pool-based punishment assume perfect or costless monitoring, flawless implementation, or homogeneous populations—these assumptions rarely hold outside stylized models.
- **Sparse direct coverage of some design dimensions** (e.g., chat, some information revelation variables, default contribution, identification display), which may be important in field or lab settings.
- **Generalizability to field or empirical/experimental settings**: Real-world noise, error, implementation barriers, and unexpected strategic responses (e.g., corruption, retaliation, preference adaptation) can undermine model-based predictions.
- **Adjacent evidence**: Many adjacent papers do not include punishment, study only dyadic/different structures, or do not report efficiency, limiting the strength of their transferability.

---

**In summary:** For the downstream task—predicting efficiency under peer punishment from game structure and control efficiency—the literature provides **strong, mechanistically detailed guidance but with significant caveats**. Core design parameters (group size, MPCR, punishment cost/technology, targeting, and baseline efficiency) are **well evidenced** as moderators, and the **effect of enabling punishment is highly conditional**—usually positive when baseline efficiency is low and punishment is efficiently targeted, but sometimes null or negative if punishment is costly or misapplied. **Heterogeneity, information design, and adjacent mechanisms (reward, institutional features) are important moderators found throughout the literature**. **Prediction should be conditional and cautious** if full empirical or dimension-level mapping is not available.
