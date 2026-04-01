# 1) Evidence Base

The paper set is large (60 papers) and spans a mixture of **empirical laboratory experiments** and **theoretical (analytical and computational) modeling**. A substantial minority of the set comprises direct experimental PGGs with punishment and payoff-based outcomes, but there is also considerable conceptual, simulation, and adjacent-game-theoretic literature. The empirical coverage is broad on behavioral dimensions but narrower on **efficiency** (payoff) outcomes in the precise context of concern: efficiency effects of enabling peer punishment in repeated PGGs. Theoretical contributions include sophisticated treatments of institutional design, evolutionary mechanisms, and threshold effects, but vary in how many design dimensions they explicitly cover.

**Strengths:** Several recent and classic empirical studies provide exact or close evidence on efficiency outcomes with punishment in PGGs. Key design dimension manipulations (player count, rounds, MPCR, punishment cost/tech) are well-covered. The coverage is bolstered by theoretical contributions providing mechanistic insight and explicit quantitative predictions under varying design parameters.

**Weaknesses:** There is substantial reliance on adjacent paradigms (CPR games, prisoner's dilemma, threshold public goods, networked games). Many empirical studies do not report efficiency or total earnings as an outcome, focusing instead on behavioral or neural outcomes. Some theoretical work lacks empirical validation or omits dimension-level manipulation relevant to downstream prediction. Reward mechanisms, communication, and the visibility of summary information are rarely systematically manipulated.

# 2) Task Relevance

### a) **pgg_or_variant**
- **Exact:** Numerous papers provide exact or nearly exact PGG environments with comparable design features (e.g., Sparks et al., 2024; Nhim et al., 2023; Ishikawa & Fontanari, 2025; Powers et al., 2023).
- **Close/Adjacent:** Many more examine closely related games (CPR, threshold collective-risk, n-player PD), with direct transfer possible only for mechanistically similar payoff structures (e.g., Grimalda et al., 2022; Xu et al., 2022; Del Ponte et al., 2025).
- **Weak/None:** Some large-scale or neural studies are only loosely connected or use different game forms altogether.

### b) **punishment_or_sanctions**
- **Exact:** Many studies implement peer or institutional punishment as an explicit game treatment (e.g., Sparks et al., 2024; Ishikawa & Fontanari, 2025).
- **Close:** Others use related mechanisms (exclusion, group-level extinction, ‘walk-away’ strategies, partner choice, public revelation) as functional analogues but not formal punishment.
- **Adjacent/Weak:** A fair fraction mention punishment or sanctions only conceptually or as context.

### c) **efficiency_or_related_payoff_outcome**
- **Exact:** Several high-quality studies provide direct efficiency or group payoff data (Sparks et al., 2024; Nhim et al., 2023; Xu et al., 2022; Powers et al., 2023; Murase, 2025).
- **Close:** Others report group welfare, aggregate extraction, or probability of success (loss avoidance) that closely map to efficiency.
- **Adjacent/Weak:** Many studies focus on behavioral metrics (contribution rates, punishment frequency) without translating these into payoff/efficiency. Some do not address group-level monetary or resource outcomes at all.

# 3) Outcomes Measured In The Literature

- **Payoff-Based Outcomes (Main focus for prediction):**
    - **Efficiency** (group payoff / maximum possible),
    - **Group earnings/profit**, **welfare**, **probability of group success/loss avoidance**, and
    - **Resource sustainability** (for closely related dynamic resource games).
    - These are directly reported or can be inferred in some key studies (e.g., Sparks et al., 2024; Nhim et al., 2023; Duong et al., 2024; Wang et al., 2023 [resource management]).

- **Non-Payoff Behavioral Outcomes (Frequently reported and sometimes conflated):**
    - **Contribution or cooperation rates**
    - **Punishment frequencies (prosocial/antisocial/distinctions)**
    - **Norm compliance/following, trust, reputation, emotional response**
    - **Neural and psychological correlates**
    - These are the focus of much of the adjacent and some direct literature, but are not equivalent to efficiency.

# 4) Main Findings Relevant To Prediction

## Synthesis from Exact/Close PGGs with Direct Efficiency Outcomes

- **Enabling Peer or Institutional Punishment in Standard PGGs:**  
    - In repeated lab PGGs, **costly punishment increases and sustains contributions and, after initial net costs, can lead to equal or higher group efficiency** vs. control, particularly in long-run play (Sparks et al., 2024). The positive effect builds up over time; start-of-treatment efficiency may be lower due to punishment costs but overtakes control as cooperation is sustained.
    - The efficacy and efficiency benefit are **strongest when punishment is neither too costly nor too weak**, and when defection detectability is imperfect—here, punishment can be a strictly positive force for efficiency (Murase, 2025).
    - **Costless or purely expressive disapproval is not sufficient** to sustain efficiency—incentives must be material (Sparks et al., 2024).

- **Institutional Punishment vs. Peer Punishment:**  
    - **Institutional punishment** (centralized, cost-sharing among punishers) theoretically enables high-efficiency equilibria, provided costs are not excessive and a critical mass of punishment-supporters is reached (Ishikawa & Fontanari, 2025; Powers et al., 2023). If setup costs are high or cost-benefit ratios poor, punishment may not improve—sometimes may reduce—efficiency.
    - **Group size is an important moderator**: as player count increases, sustaining efficient punishment outcomes requires careful parameterization of costs, fines, and institutional consensus (Powers et al., 2023).

- **Cost Structure and Magnitude Matter:**  
    - When punishment is **sufficiently cheap and effective**, it can **substantially increase efficiency**; when costly, the loss from enforcement can offset the gains from higher cooperation, sometimes leading to lower net efficiency in punishment-enabled treatments (Nhim et al., 2023; Grimalda et al., 2022).
    - **Empirical findings are mixed** in close variants: some studies find that even with cooperation boosts, net earnings in punishment treatments fall short of those in control due to high enforcement costs (e.g., Grimalda et al., 2022; Cooney, 2025).

- **Contextual and Design Moderators:**  
    - In **voluntary, pledge-based public bads games**, punishment (financial penalties) can fail to raise efficiency if participants evade ambitious pledging or opt out (Del Ponte et al., 2025).
    - The **structure of punishment**—peer vs. institutional, opt-in vs. opt-out, public vs. private—has major effects on outcomes.
    - **Communication (chat), reward mechanisms, and summary visibility** are less frequently studied but may moderate or amplify punishment's effect.

- **Baselines Matter:**
    - If **control efficiency is already high** (due to high MPCR, strong social norms, or other cooperation-supporting features), the incremental effect of punishment may be smaller or even negative (due to added costs).
    - If **control efficiency is low** (typical in standard low-MPCR PGGs), the **scope for punishment to improve efficiency is greater**, if costs are not prohibitive (Sparks et al., 2024; Ishikawa & Fontanari, 2025).
    - **Bistability and path dependence:** Some models show that both high and low efficiency states are possible depending on initial conditions (Wang et al., 2023; Ishikawa & Fontanari, 2025).

## Indirect and Mechanism-Level Findings

- **Punishment as a Deterrent:** Theoretical accounts emphasize that the **threat** of punishment can be more efficiency-promoting than its frequent execution; efficient societies are often characterized by rare, but highly credible and deterrent, punishment (Murase, 2025).
- **Antisocial Punishment:** Low in many contexts, but when present or if costs are low, can undermine efficiency benefits.
- **Group Structure/Selection:** Mechanisms enabling fluid partner choice or group selection (e.g., ‘walk-away’ strategies, demographic extinction) can boost efficiency even without explicit punishment (Cooney, 2025; Kroumi, 2025).
- **Network/Hierarchy/Institutional Complexity:** Large or hierarchical groups benefit more from institutional punishment; consensus costs can curtail potential efficiency gains (Powers et al., 2023).

# 5) Prediction Guidance

The literature gives the following **guidance for efficiency prediction in repeated PGGs when peer punishment is enabled**:

- **Hold game design dimensions and control efficiency constant:**  
    - Enabling peer (or institutional) punishment will often—but not always—increase group efficiency, especially when the **punishment is neither too costly nor too weak**, and the **control efficiency is low**.
    - If the **control (no-punishment) efficiency is high** (due to high MPCR, strong social norms, or other features), the incremental efficiency gain attributable to punishment may be smaller or negative (punishment costs not recouped).
- **Include and attend to specific game design features:**
    - **Player count (group size):** Larger groups can make effective punishment more costly or administratively difficult; there may be a non-linear relationship (Powers et al., 2023; Ishikawa & Fontanari, 2025).
    - **MPCR:** Strongly modulates the incentive to cooperate; interacts with punishment effectiveness.
    - **Punishment cost and tech (fine-to-cost ratio):** The efficiency benefit of punishment is greatest when the punishment is **cost-effective**—cheap relative to its deterrent effect. High costs can easily lead to net efficiency losses (Nhim et al., 2023).
    - **Number of rounds:** Longer games make it **more likely that punishment achieves its efficiency-sustaining effect** (Sparks et al., 2024).
- **Caveats:**  
    - **Antisocial or misapplied punishment** (punishing cooperators or random punishment) undermines efficiency gains.  
    - **Voluntary/pledge-based games** may permit evasion that blunts the efficiency impact of punishment (Del Ponte et al., 2025).
    - **Institutional consensus/complexity:** If rules for punishment are costly or hard to coordinate, efficiency gains may not materialize (Powers et al., 2023).
- **Empirical/theoretical convergence:** Most laboratory and theory studies agree in trend but differ in effect size and parametric sensitivity. Where quantitative data are available, expect that the efficiency in punishment-enabled PGGs can reach or sometimes slightly exceed control over sufficient rounds if parameters are favorable.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- **player_count:** Extensively modeled and manipulated. Effects on punishment efficacy and efficiency well-documented.
- **num_rounds:** Important moderator in repeated games. Longer duration enhances potential efficiency gains from punishment.
- **mpcr:** Systematically varied; shown to interact with punishment effectiveness.
- **punishment_cost, punishment_tech:** Central to both empirical and theoretical studies—effects on efficiency well established.
- **all_or_nothing:** Studied in both continuous and all-or-nothing contribution frameworks.
- **reward_exists, reward_cost (less so):** Occasionally examined, mostly in resource management and division of labor models.
- **show_n_rounds, show_other_summaries:** Sometimes manipulated (e.g., in kin selection or norm studies), but much less systematically.
- **default_contrib:** Direct empirical study is rare; some studies use opt-in/opt-out frames.
- **chat:** Empirically manipulated in some studies (e.g., Sparks et al., 2024).

**Indirectly Informed/Contextually Discussed:**
- **punishment_tech:** Sometimes analyzed as ‘institutional’ vs. ‘peer’ or ‘direct’ vs. ‘indirect’, but operationalization varies.
- **show_punishment_id:** Rarely directly manipulated; mentioned in some reputation and signaling studies.
- **reward_tech, reward_cost:** Investigated in a subset of theoretical work, mostly central in hybrid or resource management models.

**Effectively Missing or Sparse:**
- **Visibility of summary information (show_other_summaries, show_punishment_id):** Rarely separated as a treatment.
- **Complex communication (combinations of chat and summary info), specific framing (default_contrib), and explicit coupling of peer punishment with reward:** Little systematic evidence as to their interaction effects on efficiency.

# 7) Important Limitations

- **Empirical Payoff Data Gaps:** Many studies do not report efficiency or group payoff, focusing on behavioral outcomes. Behavior-payoff mapping is often assumed but rarely quantified.
- **Punishment Structure Variability:** Differences in how punishment is implemented—peer vs. institutional, central vs. decentralized, voluntary vs. mandatory—limit transferability.
- **Reward Mechanisms and Combined Designs:** Sparse direct comparison of punishment vs. reward, or combined mechanisms, on efficiency outcomes.
- **Design Space Coverage:** Some prediction dimensions (showing IDs, detailed summary information, opt-in framing) are poorly covered.
- **Population Structure and Culture:** Most experiments use anonymous, one-shot or repeated, small-group lab contexts; generalization to field, networked, or culturally diverse groups is limited.
- **Treatment vs. Baseline Ambiguity:** Where control efficiency is very high or very low for other reasons (e.g., social norms, communication, kin structure), effects of punishment may be masked or nonlinear.
- **Non-monotonicities and Parameter Thresholds:** Several theoretical models show bistability or non-monotonic effects (e.g., intermediate cost/fine ratios are necessary for efficiency, too high or too low both fail).
- **Transfer from Adjacent Paradigms:** Results from CPR, threshold, and donation games are informative but cannot be mapped quantitatively without caution; details of public-good linearity, risk, and group context matter.

---

**In summary:**  
The literature base provides high-certainty directional evidence that enabling peer punishment in standard PGGs with appropriate parameterization **can increase efficiency**, particularly when control efficiency is low, and punishment is neither too weak nor too costly. Design dimensions—especially punishment cost/efficacy, group size, and game length—are central moderators, and their effects are supported by both theory and experiment. However, caution is warranted when transferring predictions across variants; behavioral data do not always transform cleanly to efficiency, and a subset of relevant prediction dimensions is underexplored in the current literature.
