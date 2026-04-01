# 1) Evidence Base

The paper set consists exclusively of theory papers (19), with no experimental or direct empirical studies. Theoretical modeling dominates, ranging from classic public goods games (PGG) with formal equilibrium analysis to adjacent contexts (common-pool resource, bargaining, investment, reputation, stag-hunt, donation, and environmental collective-risk games). A substantial proportion of the papers are closely aligned with public goods or similar social-dilemma structures, while several are more peripheral, applying similar concepts to related but technically distinct settings.

For the core prediction task—mapping game parameters and control efficiency to efficiency under peer punishment in PGG-like settings—only a minority of papers provide exact coverage with explicit, quantitative guidance. Most adjacent literature contributes conceptual or mechanism-level insights rather than precise, plug-in prediction tools. There is broad theoretical scope (multiple mechanisms, cognitive and institutional moderators, population structure, and network effects are all considered), but a lack of granular empirical calibration and application to robustly parameterized prediction tasks.

# 2) Task Relevance

**pgg_or_variant:**  
- **exact:** Multiple papers directly analyze standard or closely parameterized PGGs (e.g., Huang et al., 2024; Dong et al., 2024; Wang et al., 2023; Chessa & Loiseau, 2024).
- **close:** Several apply to public-goods-like scenarios with minor structural differences (e.g., CPR games, workplace/team production, donation games, repeated PDs).
- **adjacent–weak:** Some focus on bargaining, trust, or social contract games with only thematic overlap.

**punishment_or_sanctions:**  
- **exact:** Several papers give focused analyses of explicit peer/institutional punishment in PGG or nearly identical games (e.g., Huang et al., 2024; Dughera, 2022; Wang et al., 2023).
- **close/adjacent:** A significant subset discuss indirect punishment, sanctioning via reputations, social pressure, or mechanisms analogous to punishment (e.g., grim trigger, community enforcement, fines, leadership).
- **weak/none:** A handful provide context or discuss behavioral mechanisms (norm enforcement, trust), but do not model or quantify punishment/sanctions.

**efficiency_or_related_payoff_outcome:**  
- **exact:** Most papers of direct PGG focus report on group efficiency, welfare, or surplus outcomes—sometimes giving explicit formulas or comparative statics.
- **close/adjacent:** Many adjacent papers measure efficiency in terms of welfare, payoff, or related quantities, but in structurally different games (PRD, CPR, bargaining, reputation).
- **weak/none:** Some focus on cooperation or compliance rates, trust, or norm adherence—acknowledging efficiency but only as a conceptual anchor.

# 3) Outcomes Measured In The Literature

- **Payoff-based outcomes (efficiency, total payoff, welfare):**  
  These are primary in about half of the most relevant papers, with explicit models relating group efficiency to game design (e.g., Huang et al., 2024; Dughera, 2022; Sugaya & Wolitzky, 2023; Libois, 2022; Dong et al., 2024; Gioffré & Tampieri, 2025; Chessa & Loiseau, 2024).  
  - Often reported as the condition under which full cooperation (and thus maximum efficiency) can be sustained, or the explicit equilibrium efficiency under different institutional arrangements.

- **Non-payoff behavioral outcomes (contribution rate, cooperation, norm compliance):**  
  Some papers focus primarily on frequency/dynamics of cooperation or behaviors leading to efficiency but do not report welfare/payoff ratios (e.g., Wang et al., 2023; Marco & Goetz, 2024).  
  - Several highlight how trust, expectation, or social norms modulate actions, with payoff as a backdrop rather than a quantified endpoint.

- **Other/mixed:**  
  Some papers discuss mechanisms without reporting either outcome quantitatively (e.g., Vromen, 2022; Bao et al., 2022; Liuzzi & Vié, 2022).

# 4) Main Findings Relevant To Prediction

Synthesizing across the literature, the following themes emerge:

- **Punishment can dramatically increase efficiency, but only under certain conditions.**  
  Targeted, credible punishment (especially against the lowest contributors) supports the full cooperative equilibrium and maximizes welfare, particularly when designed to be just sufficient to deter defection (Huang et al., 2024; Sugaya & Wolitzky, 2023; Dong et al., 2024; Gioffré & Tampieri, 2025; Libois, 2022). The theoretically optimal policy is to punish only as much as needed to reach and sustain full cooperation, as over-punishment can reduce morale or lead to inefficient equilibria (Dughera, 2022).

- **Thresholds and parameter regions are critical.**  
  Multiple papers provide explicit conditions where enabling punishment shifts the equilibrium from low to high efficiency. These thresholds depend on player count, MPCR, punishment cost, and the effectiveness or targeting of the punishment technology (Huang et al., 2024; Sugaya & Wolitzky, 2023; Libois, 2022).

- **Heterogeneity, population structure, and institutional design moderate punishment effects.**  
  Non-monotonic effects can arise: intermediate levels of kinship or coordination can undermine punishment and reduce efficiency compared to both low and high extremes (Dong et al., 2024). Network structure, cognitive biases (e.g., prospect theory effects), and reputation/memory windows can all shape whether punishment successfully increases efficiency (Marco & Goetz, 2024; Uchida et al., 2024; Pei, 2024).

- **Punishment is not always the most efficient incentive.**  
  In some parameter regimes (e.g., high skill/charisma in team production, or when effective motivation/reward is available), rewards or positive motivational mechanisms can yield higher efficiency than punishment (Dughera, 2022; Huang et al., 2024; Wang et al., 2023). Combined or calibrated use of reward and punishment can maximize welfare.

- **Behavioral and dynamic caveats.**  
  Repeated games, path dependency, and the possibility of stable inefficient regimes (punishment cycles, norm failures) can produce ambiguous or mixed efficiency outcomes even when punishment is available (Dughera, 2022; Gioffré & Tampieri, 2025). Policy interventions need careful tailoring to context.

# 5) Prediction Guidance

The literature provides a moderately strong (albeit theory-heavy) foundation for predicting the efficiency effect of enabling peer punishment in PGG-like environments:

- **When the control game's efficiency is low due to sustained defection, introducing sufficiently strong, targeted punishment is theoretically very likely to sharply increase efficiency, often up to or near the fully cooperative optimum.** The transition is generally threshold-bound: little or no effect occurs until the cost/magnitude/targeting of punishment crosses a key boundary, after which efficiency often increases discontinuously (Huang et al., 2024; Sugaya & Wolitzky, 2023; Libois, 2022).
- **The predicted efficiency gain is maximized when punishment is minimal but precisely targeted.** Overuse or indiscriminate application of punishment can depress welfare, create cycles of retaliation, or entrench inefficient equilibria (Dughera, 2022).
- **Design dimensions such as player count, MPCR, punishment cost and magnitude, and punishment targeting are critical.** Explicit comparative statics exist for some of these, and control efficiency can serve as a baseline for how 'close' the system is to efficient outcomes absent punishment.
- **Payoff-based predictions from theory may overstate the efficiency increase if behavioral or institutional moderators (heterogeneity, limited monitoring, memory, cognitive biases) are not favorable.**  
- **Reward mechanisms can substitute for or complement punishment, sometimes yielding higher efficiency, especially in settings conducive to positive motivation or when punishment is expensive or demotivating.**  
- **Predictions outside the parameter regimes directly analyzed in the more relevant theory papers (e.g., one-shot, highly dynamic, or highly heterogeneous games) should be made with caution, as non-monotonic or ambiguous effects can occur.**

# 6) Design Dimensions Highlighted Across Papers

**Directly informed:**  
- **player_count:** Frequently explicit in models; larger groups are generally harder to sustain cooperation in, unless effective punishment is present (Huang et al., 2024; Sugaya & Wolitzky, 2023; Libois, 2022; Dughera, 2022).
- **num_rounds:** Considered mostly in repeated or dynamic games; longer/infinitely repeated games are more favorable for punishment-supported cooperation (Camera & Gioffré, 2025).
- **all_or_nothing:** Explicit in several models (Huang et al., 2024; Chessa & Loiseau, 2024); can affect thresholds for cooperation and punishment effectiveness.
- **mpcr:** Central moderator (Huang et al., 2024; Libois, 2022; Dong et al., 2024).
- **punishment_cost / punishment_tech:** Core to most punishment models; effectiveness and threshold effects directly modeled (Huang et al., 2024; Sugaya & Wolitzky, 2023).
- **reward_exists / reward_cost / reward_tech:** Directly addressed in some (Huang et al., 2024; Wang et al., 2023; Dughera, 2022).
- **show_n_rounds:** Occasionally considered (Dong et al., 2024; Libois, 2022), mostly as a framing or repeated-game variable.

**Indirectly/contextually informed:**  
- **chat:** Only addressed peripherally, if at all.
- **default_contrib:** Not directly modeled; some papers analyze contribution set restrictions (Chessa & Loiseau, 2024).
- **show_other_summaries / show_punishment_id:** Reputation, monitoring, and information structures are often discussed (Pei, 2024), but mapping to these specific variables is indirect.

**Missing or only very loosely addressed:**  
- **reward_magnitude:** Rarely directly parameterized.
- **Some game features like chat, partner matching, or framing (e.g., default contribution) are not systematically analyzed across this literature set.**

# 7) Important Limitations

- **Lack of empirical calibration:** All papers are theoretical; real-world and laboratory complexities, such as bounded rationality, implementation errors, or social-psychological moderators, are generally not accounted for.
- **Sparse direct mapping to several design dimensions:** Some predictor variables (e.g., reward magnitude, chat, default contribution, identity display) are thinly or not at all covered. Fine-grained design interaction effects are not always theorized.
- **Transfer to non-PGG games is uncertain:** Many adjacent results (repeated PD, bargaining, resource management) require cautious extrapolation when applying predictions to literal PGG settings.
- **Behavioral outcomes and psychological mechanisms are sometimes conflated with efficiency in discussion:** Only a subset of the literature uses strict payoff-ratio (efficiency) as the main outcome.
- **Ambiguities remain for heterogeneous, unstable, or path-dependent games:** Several models show multiple equilibria, bi-stability, or non-monotonic parameter effects, implying that predictions are more certain only in well-characterized parameter regions.
- **Reward mechanisms and their interaction with punishment are not as richly parameterized or modeled as punishment alone.**

---

**In summary:**  
This literature set strongly supports the inference that, under standard PGG-like conditions with low baseline efficiency, enabling well-designed, credible, and sufficiently strong peer punishment is likely to substantially increase efficiency, often to full-cooperation, provided thresholds in key design dimensions are reached. Predictions are most reliable within the parameter space and incentive structure directly modeled; outside, effects can be muted or ambiguous. The absence of empirical data and incomplete coverage of some game dimensions mean that predictions should be qualified by theoretical and contextual limitations.
