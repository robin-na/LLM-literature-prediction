# 1) Evidence Base

This paper set is comprised primarily of theoretical and simulation studies (6 papers), with a minority of empirical studies—either observational (2 papers) or experimental/lab-based (1 paper). The majority of the studies employ agent-based models, evolutionary game theory, or conceptual simulations rather than data collected from standard public goods game (PGG) laboratory experiments. The empirical coverage of actual payoff outcomes in controlled, PGG-like designs is sparse. Papers sometimes address adjacent domains (e.g., environmental governance, intentional community rule enforcement, cooperative water management) without directly modeling standard PGGs or reporting quantitative efficiency effects from punishment treatments. Most outcomes are behavioral (e.g., cooperation rates, compliance, or normative adherence), with only a few papers addressing group payoff or efficiency—and those nearly always without enabling punishment. The literature set is thus relatively broad regarding contexts and mechanisms, but narrow and indirect with respect to the exact prediction task: estimating efficiency change when punishment is enabled in a PGG.

# 2) Task Relevance

Task relevance is assessed separately for three key elements:

- **PGG or variant**: Only Park (2022) uses the exact Public Good Game paradigm, though it omits punishment. Other papers use adjacent or loosely analogous designs (e.g., regulatory games, networked social dilemmas, institutional emergence, resource extraction, and community cooperatives), labeling their paradigms as `adjacent` or, at best, `close`.
- **Punishment or sanctions**: Most papers discuss punishment mechanisms of some kind (`exact` or `close`), but only in adjacent paradigms. Only Qirko (2020), Jiang & Zheng (2024), Li et al. (2023), Huo & Liu (2024), Armstrong et al. (2024), and Wang & Mao (2024) feature explicit punishment, but none do so in an exact PGG. Park (2022) and Chang et al. (2021) have no punishment at all.
- **Efficiency or related payoff outcome**: Only Park (2022) measures efficiency directly, but does so solely with punishment disabled. Chang et al. (2021) reports close (final payoffs) but without punishment. All other studies focus on non-payoff behavioral outcomes; if they discuss compliance or cooperation, these are not strictly efficiency, and such relevance is labeled as `adjacent` or `weak`.

In summary, this literature set is characterized by:
- **Exact**: Only for component mechanisms (e.g., punishment), not in a fully matched PGG with efficiency outcomes.
- **Close/Adjacent**: In contexts, mechanisms, and sometimes the general structure of social dilemmas, especially regarding multi-stakeholder environmental governance or community enforcement norms.
- **None/Weak**: Direct evidence on efficiency effects of enabling punishment in PGGs is missing.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes**:
- Only Park (2022) reports efficiency/group payoff, but with *no punishment mechanism* modeled, thus providing no direct evidence on punishment effects.
- Chang et al. (2021) collects experimental payoff data (final coins extracted), but again, *without punishment*.
- Several papers report on the logical potential for improved welfare or lower costs (e.g., reduced government regulation effort with effective punishment in Jiang & Zheng, 2024), but without quantifying group payoff or efficiency.

**Non-payoff behavioral outcomes**:
- The majority of papers (Li et al., 2023; Jiang & Zheng, 2024; Huo & Liu, 2024; Qirko, 2020; Armstrong et al., 2024; Wang & Mao, 2024; Gao et al., 2024) assess outcomes such as cooperation rate, compliance with regulations, stability of norm enforcement, sanction frequency, and other indicators of behavioral compliance.
- These outcomes sometimes discuss payoffs as possible implications, but do not provide measured or simulated efficiency ratios.

# 4) Main Findings Relevant To Prediction

Synthesizing across the papers:

- **Punishment Mechanisms Promote Compliance and Cooperation (Behavioral):**
    - Theory and simulation studies consistently suggest that enabling punishment (especially when paired with dynamic or responsive features) promotes the stability of cooperation or compliance in multi-agent dilemmas (Jiang & Zheng, 2024; Li et al., 2023; Armstrong et al., 2024; Huo & Liu, 2024; Wang & Mao, 2024).
    - Punishment effectiveness can depend on the cost of applying it, the upper limit (tech), and network context, but *use* and *impact* are often context-dependent and may not generalize across all parameter settings (Qirko, 2020).

- **Efficiency Data Are Largely Absent:**
    - No study provides empirical or simulation-based estimates for group efficiency when punishment is enabled versus disabled in a standard PGG.
    - Park (2022) quantifies efficiency in PGGs but does not include any punishment mechanism.

- **Indirect Support for Efficiency Effects:**
    - Behavioral increases in cooperation or compliance are presumed (by some models) to enhance collective payoff, but this link is neither measured nor reliably quantified.
    - Some papers suggest trade-offs where the *cost* of punishment, or overuse of reward, may offset any gains in cooperation (Wang & Mao, 2024; Qirko, 2020).

- **Contextual Moderators and Boundary Conditions:**
    - Several papers highlight that features like network structure, monitoring, innovation rate, cost of sanctioning, and the presence/absence of rewards can strongly moderate the impact of punishment (Li et al., 2023; Armstrong et al., 2024; Wang & Mao, 2024).
    - Real-world settings show that punishment is often rarely used or only deployed under particular conditions (Qirko, 2020).

# 5) Prediction Guidance

Given the absence of direct, quantitative evidence relating *control efficiency* and *treatment efficiency* (under punishment) in PGGs, guidance must be inferred cautiously and qualitatively:

- **General Expectation:** When punishment is enabled in PGG-like environments, theory and simulation studies suggest an increased likelihood of cooperative or compliant behavior, particularly when punishment is well-targeted (low cost, dynamic/responsive, or supported institutionally).
- **Magnitude and Direction:** Owing to the lack of payoff or efficiency data, it is not possible to specify the size or even consistent sign (positive or negative) of the efficiency change from enabling punishment. Theory suggests efficiency *could* increase if cooperation gains outweigh direct punishment costs, but this balance is unmeasured.
- **Design Dimension Moderation:** The effects of punishment are likely to be mediated by dimensions such as player_count, punishment_cost, and network structure, but this literature set lacks direct, empirical parametrization for these moderators in relation to efficiency.
- **Weaknesses:** Without payoff data, predictions must fall back on behavioral patterns; in real-world or complex environments, the actual use and resulting impact of punishment is variable and contextually limited (Qirko, 2020).

*Thus, for the prediction task—estimating treatment efficiency in PGGs with punishment—this literature set supports the generic expectation that punishment may increase compliance but does not provide calibration for the efficiency effect based on measurable outcomes or design dimensions.*

# 6) Design Dimensions Highlighted Across Papers

Across this literature set, the following prediction dimensions are informed at various levels:

- **Directly Informed** (i.e., modeled or manipulated, though not always in PGGs):  
    - `player_count` (most theory and simulation papers)  
    - `num_rounds` (Park, 2022; Armstrong et al., 2024; Jiang & Zheng, 2024)  
    - `all_or_nothing` (frequent, but effects on efficiency not isolated)  
    - `punishment_cost` (multiple papers emphasize its importance)  
    - `punishment_tech` or limits (Jiang & Zheng, 2024; Li et al., 2023; Qirko, 2020)  
    - `reward_exists`, `reward_cost` (several models include reward/bonus options as design dimensions)

- **Indirectly/Contextually Discussed**:  
    - `chat` (Qirko, 2020, in community contexts)  
    - `show_other_summaries`, `show_punishment_id` (Qirko, 2020, as context for norm enforcement)

- **Occasionally Mentioned**:  
    - `mpcr` (Park, 2022, but only without punishment)  
    - `show_n_rounds` (Chang et al., 2021, but not tied to punishment or efficiency)

- **Effectively Missing**:  
    - `default_contrib` (rarely specified or manipulated in any model)  
    - `punishment_magnitude`, `reward_magnitude` (not specified or manipulated distinctly)
    - No papers manipulate the full range of 14 prediction dimensions in the context of efficiency change when punishment is enabled.

# 7) Important Limitations

- **Lack of Direct Efficiency Data:** None of the papers measure or simulate group efficiency as a function of punishment activation in standard PGGs; most model only non-payoff behavioral outcomes.
- **Contextual and Domain Differences:** Many studies operate in social, institutional, or resource-extraction settings that are only analogously related to PGGs. Results may not generalize cleanly to laboratory public goods experiments.
- **Design Dimension Sparsity:** Key prediction moderators (e.g., chat, default_contrib, punishment/reward magnitude, visibility features) are only rarely incorporated or analyzed systematically.
- **Over-reliance on Theory/Simulation:** The preponderance of agent-based modeling and evolutionary game theory produces rich hypotheses about mechanisms but provides little empirical anchoring for actual effect sizes or parameter calibration.
- **Behavioral versus Payoff Outcomes:** Most papers substitute compliance, cooperation rates, or norm adherence for group payoff or efficiency, complicating inference about the net welfare impact of punishment.
- **Potential Publication and Selection Bias:** The focus on punishment mechanisms in governance or community settings may over-represent the scenarios where punishment has meaningful effects, limiting out-of-sample validity.
- **No Quantitative Mapping:** There is no basis in this set for a quantitative mapping from control efficiency and design variables to expected treatment efficiency after enabling punishment.

---

**Summary Statement:**  
This literature set provides broad conceptual and theoretical support for the role of punishment in promoting cooperation and compliance in multi-agent social dilemmas, but lacks direct, quantitative evidence for predicting efficiency changes in public-goods-game-like environments from design dimensions and control efficiency. Payoff-based outcomes are almost entirely absent where punishment is enabled, necessitating a cautious and primarily qualitative approach to prediction.
