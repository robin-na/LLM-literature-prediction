# Evidence Base

The literature base consists of both empirical (mostly laboratory experiments) and theoretical (including agent-based simulation and analytical modeling) studies, with a primary focus on standard and variant public goods games (PGGs), as well as adjacent social dilemma, resource, and contest environments. Out of 85 papers, a substantial fraction deliver direct empirical or theoretical findings about the efficiency consequences of implementing punishment in PGGs, while many others provide indirect or adjacent evidence, especially in structurally related games.

The set is broad in its coverage of contexts, institutional structures (peer punishment, leader punishment, third-party punishment, punishment versus reward, etc.), and population features (group size, composition, heterogeneity). However, there is a notable mixture in the type of outcomes measured: while several key papers focus explicitly on group efficiency or total earnings (i.e., true payoff-based outcomes), many report primarily on cooperation rates, contribution rates, or behavioral responses to punishment, which must not be conflated with efficiency.

Additionally, evidence on specific game design dimensions is uneven: classic parameters such as player count, round number, punishment cost, and MPCR are frequently discussed, but others (e.g., chat, show_n_rounds, show_other_summaries, show_punishment_id) are rarely addressed in direct connection to efficiency. The literature also displays a strong emphasis on laboratory studies with undergraduate samples, though theory papers often explore a broader set of hypothetical or stylized conditions.

# Task Relevance

### `pgg_or_variant`
- **Exact**: Many papers (e.g., Harrell, 2019; Molenmaker et al., 2023; Bühren et al., 2023; Zefferman, 2023; Botta et al., 2024) use standard linear or threshold PGGs.
- **Close/Adjacent**: Several apply close variants (e.g., team contest, common-pool resource, trust or division-of-labor games) where the core mechanisms are highly comparable (e.g., Heine & Strobel, 2020; Garrido et al., 2025; Nirjhor & Nakamaru, 2023).
- **Weak/None**: Some focus on dyadic social dilemmas or unrelated market/trust games, providing only context (e.g., Loch-Temzelides, 2021).

### `punishment_or_sanctions`
- **Exact**: Many primary studies manipulate punishment (enabled or disabled), varying its form (peer, leader, third-party).
- **Close**: Some address reward mechanisms, exclusion, or norm-based enforcement as substitutes or complements (e.g., reward existence, exclusion as punishment).
- **Adjacent/Weak**: Indirect or weak link to punishment (guilt induction, trust-based mechanisms, social exclusion without explicit cost).
- **None**: Several provide only a behavioral sanctioning context without manipulating punishment.

### `efficiency_or_related_payoff_outcome`
- **Exact**: A subset directly measure and report efficiency, group earnings, total payoff, or welfare (e.g., Harrell, 2019; Bühren et al., 2023; Zefferman, 2023; Botta et al., 2024; Heine & Strobel, 2020; DeCaro et al., 2024; Ezeigbo, 2017).
- **Close/Adjacent/Weak**: Many report cooperation/contribution rates or sanction frequency without translating these into actual group efficiency (e.g., Clarke & Dickinson, 2020).
- **None**: Some have no relevance for payoff-based outcomes.

**Synthesis:**  
The strongest, most relevant evidence for the prediction task comes from papers that are exact on all three dimensions—using PGGs or direct variants, manipulating real punishment/sanctions, and reporting efficiency or explicit total group payoff outcomes.

# Outcomes Measured In The Literature

- **Payoff-related outcomes** (group efficiency, total group earnings, surplus, welfare) are central in a subset of the literature, including both laboratory experiments and agent-based or game-theoretic models that are parameterized sufficiently to yield treatment/control efficiency comparisons.
    - *Example:* Harrell (2019), Bühren et al. (2023), Zefferman (2023), Botta et al. (2024), DeCaro et al. (2024), Heine & Strobel (2020).
- **Behavioral outcomes** (contribution rate, cooperation rate, frequency of punishment, norm compliance, etc.) are reported in most empirical experiments; however, these do not always correspond to efficiency. Some studies infer likely efficiency effects based on behavioral proxies but do not directly report payoff-based changes.
    - *Example:* Nakagawa et al. (2022), Clark & Dickinson (2020), Okada et al. (2021).
- Some **hybrid outcomes**—such as investment or threshold achievement rates—can serve as close proxies for efficiency in threshold PGGs but do not constitute direct efficiency measures unless total payoffs are compared to the social optimum.

Critically, numerous studies do not report efficiency or group payoff at all, focusing instead on mechanisms, beliefs, or psychological processes (e.g., norm beliefs, negative reciprocity, emotional context).

# Main Findings Relevant To Prediction

## General Effects of Punishment on Efficiency in PGGs

- **Enabling punishment often increases cooperation/contributions, but its effect on efficiency (total group payoffs) is less straightforward and highly contingent on game and institution design.**
    - In classic PGGs, punishment can increase efficiency—*especially when baseline (control) efficiency is low due to free-riding*—but punishment costs may offset or outweigh the gains from higher cooperation if punishment is widely used or poorly targeted (Bühren et al., 2023; Harrell, 2019; Zefferman, 2023).
    - **Peer punishment tends to be less efficient than leader or centralized punishment**, primarily due to higher punishment costs and coordination failure (Harrell, 2019; Zefferman, 2023; Botta et al., 2024).
    - In some parameter regimes—**e.g., costly or inefficient punishment, high antisocial punishment, or group heterogeneity—enabling punishment can decrease efficiency** (Heine & Strobel, 2020; Ezeigbo, 2017; Molenmaker et al., 2023).
    - *Discriminatory punishment* due to group heterogeneity or identity differences can undermine the benefits of punishment, resulting in no efficiency gains or even losses (Molenmaker et al., 2023).
    - **Severe, well-targeted, and low-cost punishment is much more likely to deliver efficiency gains** (Botta et al., 2024; Zefferman, 2023; Mohlin et al., 2023; Nirjhor & Nakamaru, 2023).

- **Threshold effects:** Mild punishment may reduce payoffs (costs > gains in cooperation); severe punishment can enable full cooperation and maximal efficiency, especially among low cooperators (Bühren et al., 2023; Botta et al., 2024).

- **Punishment design is critical:** Who can punish, punishment cost/efficacy, visibility (show_punishment_id), information about others’ actions (show_other_summaries), and the institutional structure (peer, leader, third-party, or centralized) strongly mediate punishment's net effect on efficiency (Harrell, 2019; Zefferman, 2023; DeCaro et al., 2024; Mohlin et al., 2023; Berger & De Silva, 2021).

- ***Contextual moderators and interactions:***
    - **Group structure**: Uniformity vs. heterogeneity (homogenous vs. pluriform) can flip the sign of punishment’s effect on efficiency (Molenmaker et al., 2023; Nielsen & Pfattheicher, 2024).
    - **Baseline cooperativeness:** If the control (no punishment) game already achieves high cooperation/efficiency, enabling punishment may yield little further gain or even negative returns due to punishment costs (Harrell, 2019; Botta et al., 2024; Lie-Panis et al., 2024).
    - **Facilitation, communication, and learning:** Facilitated discussion, communication, or restorative justice-style interventions can magnify the efficiency gains of punishment (DeCaro et al., 2024; Posten et al., 2025).

- **Negative and counterproductive effects:**
    - Misdesigned punishment institutions (profitable for punishers, or vulnerable to antisocial/discriminatory punishment) can actively reduce efficiency (Heine & Strobel, 2020; Alam & Rai, 2025; Molenmaker et al., 2023; Ezeigbo, 2017; Ibrahim, 2022).
    - When punishment is primarily used for norm signaling, not cooperation enforcement, costs may accumulate without increasing efficiency.

## Theoretical Mechanisms and Empirical Concordance

- Models and empirical results both point to **parametric thresholds**: effectiveness of punishment (magnitude vs. cost), monitoring scope, and group size interact nonlinearly to determine when punishment yields efficiency gains (Zefferman, 2023; Botta et al., 2024; Bühren et al., 2023; Nirjhor & Nakamaru, 2023).
- **Self-organized, context-aware or reputation-driven punishment institutions outperform indiscriminate, static, or uncoordinated sanctioning** in maximizing group payoffs (Lie-Panis et al., 2024; Garrido et al., 2025; Mohlin et al., 2023).
- Reward and punishment often have asymmetric or non-additive effects; in some environments, **rewards increase efficiency more effectively or with fewer costs than punishment** (Heine & Strobel, 2020; Garrido et al., 2025).

# Prediction Guidance

- **Direct prediction of treatment efficiency from control efficiency and design dimensions requires attention to individual and interactive effects of the following:**
    - **Punishment cost and impact (punishment_cost, punishment_tech):** Lower-cost, higher-impact punishment is consistently associated with larger (sometimes near-maximal) efficiency gains (Botta et al., 2024; Zefferman, 2023; Mohlin et al., 2023).
    - **Structure of punishment authority:** Peer punishment often results in higher costs (lower efficiency gain) due to redundancy, counter-punishment, and lack of coordination; centralized/leader/third-party punishment, if well-placed, yields higher efficiency (Harrell, 2019; Zefferman, 2023). However, undisciplined or profitable third-party punishment may be detrimental (Alam & Rai, 2025).
    - **Baseline (control) efficiency:** Efficiency gains from enabling punishment are highest when starting from low baseline efficiency due to uncontrolled free-riding; when control efficiency is already high, the marginal efficiency gain from punishment is attenuated or negative (Harrell, 2019; Lie-Panis et al., 2024).
    - **Group size and composition (player_count):** Larger groups and greater heterogeneity can exacerbate the costs and reduce the positive effect of punishment without centralized monitoring or high punishment efficiency (Molenmaker et al., 2023; Zefferman, 2023).
    - **Feedback and information (show_other_summaries, show_punishment_id):** Detailed, public feedback and transparency modulate both the effectiveness and targeting of punishment; information structure (costly, minimal vs. rich) can flip the efficiency effect of punishment (Berger & De Silva, 2021; Nielsen & Pfattheicher, 2024).
    - **Communication (chat):** Opportunities for discussion, especially when guided or facilitated, can improve coordination and maximize the efficiency gains from punishment (DeCaro et al., 2024).
    - **Punishment/reward synergy:** Combinations of punishment and reward, or flexible institutional design, can sometimes outperform either alone (Garrido et al., 2025), but in some contest or high-competition settings, this can backfire (Heine & Strobel, 2020).

- **Where empirical payoff-based evidence is lacking, behavioral outcomes are consistent with but not definitive for efficiency prediction.**
- **Institutional details, population structure, and sample characteristics can be strong moderators, and their absence or ambiguity in a specific prediction context should increase uncertainty in the forecast.**

# Design Dimensions Highlighted Across Papers

**Directly informed design dimensions:**
- `player_count` (group size): Frequently discussed; higher player count can dilute individual effects of punishment and create coordination challenges (Harrell, 2019; Molenmaker et al., 2023; Zefferman, 2023).
- `num_rounds`: Common, especially in repeated games; longer games can allow learning and adaptation, impacting both punishment and efficiency.
- `all_or_nothing`: Both continuous and binary contribution games represented.
- `mpcr`: Explicitly addressed in mechanism and efficiency analyses; higher MPCR generally facilitates both cooperation and the efficiency of punishment.
- `punishment_cost` and `punishment_tech`: Central to (and often manipulated in) many studies.
- `chat`: Empirically shown to moderate punishment effects, especially when structured (DeCaro et al., 2024).

**Indirectly or occasionally informed:**
- `show_other_summaries`, `show_punishment_id`, `show_n_rounds`: Sometimes manipulated or discussed in relation to information structure, but rarely tied directly to efficiency outcomes outside of theoretical or illustrative models (Berger & De Silva, 2021; Nielsen & Pfattheicher, 2024).
- `default_contrib`: Addressed in some framing/priming studies; rarely linked to efficiency via punishment.
- `reward_exists`, `reward_cost`, `reward_tech`: Present in a subset of studies; interactions with punishment and separate effects on efficiency discussed (Heine & Strobel, 2020; Garrido et al., 2025).

**Sparse or missing:**
- The exact impact of design dimensions such as `show_n_rounds`, `default_contrib`, and detailed feedback visibility has limited empirical or quantitative theoretical reporting in terms of efficiency change associated with enabling punishment.

# Important Limitations

- **Behavioral-proxy-only studies:** Many (especially empirical lab) studies report only contribution or cooperation rates, not group efficiency or payoff, requiring indirect inference and reducing transparency and precision in prediction.
- **Heterogeneity of settings:** Parameter values, institutional rules, sample populations, and measurement periods vary widely; this limits the portability of exact quantitative findings to new game designs or populations.
- **Sparse evidence on interactive effects:** While some theory papers model interactions among dimensions, few empirical studies systematically cross multiple design dimensions, making it difficult to estimate nonadditive or complex moderators.
- **External validity limitations:** Predominant use of undergraduate samples, artificial stakes, and laboratory settings.
- **Underexplored dimensions:** Limited direct evidence on the effect of institutional communication, identity transparency, information feedback, or various framing/visibility factors on efficiency when punishment is enabled.
- **Disagreement and contingency:** Empirical and theoretical findings differ about when punishment increases, does not affect, or reduces efficiency—e.g., in team contest games or when cost/benefit ratios are unfavorable (Heine & Strobel, 2020), in heterogeneous/pluriform groups (Molenmaker et al., 2023), or profitable punishment regimes (Alam & Rai, 2025).
- **Edge cases and exceptions:** Negative or null efficiency effects are plausible and empirically documented under certain punitive institution designs or population structures.

# Summary Table: Task Relevance and Evidence Sparsity by Design Dimension
| Dimension                | Direct Evidence | Indirect Evidence | Sparse/Missing |
|--------------------------|----------------|------------------|----------------|
| player_count             | Yes            | Yes              |                |
| num_rounds               | Yes            |                  |                |
| chat                     | Yes (context)  |                  |                |
| all_or_nothing           | Yes            |                  |                |
| default_contrib          |                | Yes              | Yes            |
| mpcr                     | Yes            |                  |                |
| punishment_cost          | Yes            |                  |                |
| punishment_tech          | Yes            |                  |                |
| reward_exists            | Yes            |                  |                |
| reward_cost              | Yes            |                  |                |
| reward_tech              | Yes            |                  |                |
| show_n_rounds            |                | Yes              | Yes            |
| show_other_summaries     | Indirect       | Yes              | Yes            |
| show_punishment_id       | Indirect       | Yes              | Yes            |

# Conclusion

The literature provides a robust but highly context-dependent basis for predicting the change in average efficiency when enabling peer punishment in public-goods-game-like environments, conditional on game design dimensions and baseline (control) efficiency. The effect can be strongly positive, negligible, or even negative, depending on punishment institution design, costs and efficacy, group structure, and baseline cooperation. For accurate prediction, careful mapping from the target game design to the closest-matching evidence base is needed, and predictions for poorly evidenced design dimensions or complex moderator interactions should be made with appropriate caution and uncertainty.
