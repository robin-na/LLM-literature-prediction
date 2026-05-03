# 1) Evidence Base

The evidence base is broad, comprising 61 papers spanning empirical lab and field experiments, formal theoretical analyses, computational models, and conceptual discussions. Among these, there is a substantial subset of high-relevance, empirical and theoretical studies directly testing or modeling the effect of peer or institutional punishment in public goods games (PGGs) or close variants on efficiency or related payoff-based outcomes (e.g., Sparks et al., 2024; Nhim et al., 2023; Powers et al., 2023; Ishikawa & Fontanari, 2025; Cooney, 2025). However, a significant portion of the corpus is adjacent or weakly relevant: examining related dilemmas (e.g., Prisoner’s Dilemma, threshold public goods, common-pool resources), non-payoff outcomes (e.g., cooperation rates, punishment frequency), or focusing on mechanisms (e.g., reputation, social norms, neural processes) without reporting efficiency or group payoff data. Theory and simulation papers are well represented, providing formal models relating punishment parameters to efficiency under various assumptions. Empirical evidence is mainly from lab experiments with well-described game structures; field or naturalistic studies are less common.

# 2) Task Relevance

**pgg_or_variant:**
- **Exact:** Many papers study the standard PGG or very close institutional variants (e.g., Sparks et al., 2024; Nhim et al., 2023; Powers et al., 2023; Ishikawa & Fontanari, 2025), offering direct evidence.  
- **Close/Adjacent:** Several others analyze analogues (n-person Prisoner’s Dilemma, public bads, indirect reciprocity, resource dilemmas) with similar structure but sometimes crucial institutional or dynamic differences (e.g., Murase, 2025; Kurokawa, 2023).
- **Weak/None:** Some works focus on unrelated or less relevant games (dictator game, ultimatum, asocial rule compliance) and are not informative for PGG-based prediction.

**punishment_or_sanctions:**
- **Exact:** Numerous studies manipulate the presence, structure, or cost of peer/institutional punishment (e.g., Sparks et al., 2024; Ishikawa & Fontanari, 2025; Powers et al., 2023).
- **Close/Adjacent:** Others explore punishment-like or sanctioning mechanisms (exclusion, indirect/psychological punishment, partner choice, institutional tagging) or analyze cooperative mechanisms without actual punishment interventions.
- **Weak/None:** Several focus on environments with no punishment or where punishment is only discussed conceptually.

**efficiency_or_related_payoff_outcome:**
- **Exact:** A subset explicitly measures or models efficiency as the primary outcome (e.g., Sparks et al., 2024; Nhim et al., 2023; Cooney, 2025).  
- **Close/Adjacent:** Many others report group payoff, welfare, or surplus (as direct proxies for efficiency) or frame their theoretical results via fitness, expected payoff, or population abundance—suitable for efficiency-based prediction.
- **Weak/None:** A large segment focuses solely on behavioral outcomes (contribution or cooperation rates, punishment assignments), norm compliance, or attitudes, with no direct group payoff measurement.

# 3) Outcomes Measured In The Literature

**Payoff/Efficiency Outcomes:**
- Explicit efficiency (group earnings or payoff relative to full cooperation) is measured directly in prominent experimental designs (Sparks et al., 2024; Nhim et al., 2023), and modeled in detail in several theoretical works (Ishikawa & Fontanari, 2025; Cooney, 2025).
- Related outcomes such as group payoff, total earnings, surplus, and fitness/fixation probability are frequently reported in theory papers and some experiments, often used as valid proxies for efficiency.
- Several theoretical studies provide explicit analytical or numerical predictions for group payoff/efficiency as a function of game parameters (e.g., MPCR, punishment cost, group size).

**Non-Payoff Behavioral Outcomes:**
- Many papers report only cooperation/contribution rates, frequency or targeting of punishment, or compliance behaviors. These include studies on norm psychology, partner choice, reputation, neural or psychological underpinnings, and social learning.
- While these outcomes may indicate mechanisms by which efficiency could be affected, they are not directly mapping to group payoff without additional linking assumptions.

# 4) Main Findings Relevant To Prediction

Across the best-informed, high-relevance papers:

- **Enabling costly, material peer or institutional punishment in repeated PGGs almost always increases contribution rates and can, under favorable conditions, increase group efficiency/payoff compared to control (no-punishment) conditions, especially over the long term** (Sparks et al., 2024; Powers et al., 2023).
    - However, **the efficiency gain is not universal:** the net effect on payoff depends on whether the benefits of increased cooperation outweigh the direct and indirect costs of administering punishment (Nhim et al., 2023; Cooney, 2025).
    - **Punishment is more likely to improve efficiency when:**
        - The cost to punishers is low relative to the fine/impact on defectors.
        - Game is sufficiently long or repeated, allowing benefits to accrue (Sparks et al., 2024).
        - Critical mass of punishers is reached, or institutional cost-sharing is available (Ishikawa & Fontanari, 2025; Greenwood et al., 2018).
        - Defection is hard to detect (Murase, 2025), or when there is limited information about defectors' identities (Larson, 2016).
    - **Efficiency gains may not materialize, or efficiency can decrease if:**
        - The cost of punishment is high or inefficiently allocated (Nhim et al., 2023; Cooney, 2025).
        - Punishment is ineffectively targeted or excessive (Cooney, 2025; Murase, 2025).
        - The potential gains from increased cooperation are offset by wasted resources spent on sanctioning, or by antisocial/retaliatory punishment (Nhim et al., 2023; dos Santos et al., 2014).
        - Players can opt-out or undermine the institutional structure/pledges (Del Ponte et al., 2025).
    - **Form of punishment matters:**
        - Costly, material punishment is consistently more effective for long-run efficiency than non-costly forms (e.g., expressed disapproval) which yield only temporary gains (Sparks et al., 2024).
        - Institutional (shared-cost) punishment systems expand the range of parameters where efficiency gains are achieved (Powers et al., 2023; Ishikawa & Fontanari, 2025).
    - **Effect moderators:**
        - Player count (group size), punishment cost, punishment technology (peer vs. institutional), MPCR, game length, information structure about contributions/outcomes, and reward mechanisms all moderate the efficiency impact.
    - **Contextual moderators:**
        - Cognitive load, social norms, reputation systems, and possibility of retaliation can substantially alter the outcome, often by affecting the efficiency or targeting of punishment (dos Santos et al., 2014; Murase, 2025; Odouard et al., 2023).
        - The effect of punishment may be limited or null in voluntary or weakly enforced settings—punishment must be unavoidable to reliably increase efficiency (Del Ponte et al., 2025).

Importantly, some models and experiments highlight **boundary conditions or non-monotonic effects**: too costly or excessive punishment can lead to reduced group payoff even as cooperation rises (Nhim et al., 2023; Cooney, 2025; Greenwood et al., 2018), or can foster antisocial punishment that undermines net benefit.

Empirical findings are consistent with the best-supported theoretical predictions: efficiency improvement is conditional on cost, institutional structure, and player behavior. Not all environments show gains; imposed costs can in some cases reduce overall welfare.

# 5) Prediction Guidance

**For the prediction task—estimating average efficiency with punishment enabled, given game design and baseline (control) efficiency:**

- **If the control game efficiency is low** (due to frequent defection), enabling peer (or institutional) punishment is likely, but not certain, to raise efficiency under the following dimension settings:
    - **Low to moderate punishment cost** and high punishment efficacy/fines (Sparks et al., 2024; Ishikawa & Fontanari, 2025).
    - **Longer games** (higher num_rounds) allow efficiency gains from higher cooperation to outweigh initial punishment costs (Sparks et al., 2024).
    - **Group sizes typical for lab PGGs** (3–6 players) with standard MPCR (e.g., 0.4) are well-studied; effect in larger groups may depend more on cost-sharing and institutional structure (Powers et al., 2023; Ishikawa & Fontanari, 2025).
    - **Peer punishment must be unavoidable/unavoidable, well-targeted, and not so costly as to overwhelm cooperation gains** (Nhim et al., 2023; Cooney, 2025).
- **If the control game efficiency is already high**, the marginal benefit of enabling punishment is likely to be minimal or even negative, as punishment costs will not be offset by meaningful gains in contribution.
- **Game design dimensions must be jointly considered:** Very high punishment costs, very large groups with no cost-sharing, or weak MPCR can all reduce or reverse efficiency gains.
- **Institutional punishment or cost-sharing arrangements** broaden conditions for positive treatment effects, especially in larger groups.
- **Voluntary or opt-in punishment schemes (pledge-and-review, as in public bads games)** may not yield any efficiency gain unless mechanisms ensure ambitious targets and full participation (Del Ponte et al., 2025).
- **Cognitive constraints, antisocial punishment, or poorly designed punishment can attenuate or eliminate efficiency gains, even with punishment enabled** (dos Santos et al., 2014; Nhim et al., 2023).
- **Extrapolating from non-payoff outcomes (e.g., increased cooperation rates) to efficiency is generally supported in most lab studies but caution is needed, as intervention costs may outweigh cooperative gains in some parameter regions**.

**In summary:** The literature supports a *conditional* prediction: enabling peer punishment increases efficiency when the cost/benefit ratio is favorable and the punishment mechanism is well-structured, but can decrease efficiency if costs are high or punishment is misapplied. Design dimensions related to player count, punishment cost, technological implementation, and game duration are especially critical.

# 6) Design Dimensions Highlighted Across Papers

The following **prediction-relevant game design dimensions** are:

**Directly informed (multiple papers with both empirical/theoretical support & efficiency outcomes):**
- `player_count` (group size): strongly informs threshold effects, institutional stability, and cost-sharing (Sparks et al., 2024; Ishikawa & Fontanari, 2025; Powers et al., 2023; Cooney, 2025).
- `num_rounds`: repeated interaction length, supports accruing efficiency gains from punishment-enabled cooperation (Sparks et al., 2024).
- `mpcr` (Marginal Per Capita Return): central in determining incentives and feasibility of cooperation/punishment (multiple theoretical models).
- `punishment_cost` and, less explicitly, `punishment_tech` (peer vs. institutional): cost moderates the efficiency impact; mechanism type shapes the effect and threshold (Sparks et al., 2024; Ishikawa & Fontanari, 2025; Powers et al., 2023).
- `all_or_nothing`: modeled and manipulated in several theory papers affecting threshold effects (Greenwood et al., 2018; Kristensen et al., 2025).
- `show_other_summaries` and related information dimensions: less commonly, information about others’ payoffs/contributions shown to impact learning and social comparison (Burton-Chellew & D’Amico, 2021).

**Indirectly informed/contextually discussed (outcomes mainly behavioral, or efficiency as a secondary/derived result):**
- `chat` (communication): some mention, but empirical efficiency effects with and without chat are sparse; one empirical (Nhim et al., 2023) includes chat but does not isolate its effect.
- `default_contrib`: indirectly addressed in pledge-type games (Del Ponte et al., 2025).
- `show_n_rounds`: included as a dimension in experimental designs but rarely assessed as a moderator of treatment effects.
- `show_punishment_id`: some theory work discusses punishment anonymity but little empirical data on efficiency impact.

**Sparse or mostly missing:**
- `reward_exists`, `reward_cost`, `reward_tech`: Rarely directly tested as moderators of the punishment-efficiency relationship; some models include simultaneous reward, but evidence is weaker and less explicit regarding their interaction with punishment.
- Some dimensions such as public knowledge of identities or summaries are addressed only in adjacent work, with primarily behavioral outcomes.

For the dimensions above, the combination of `player_count`, `mpcr`, `punishment_cost`, and the exact punishment implementation (`punishment_tech`, e.g., peer vs. institutional) are **best supported by direct, payoff-relevant evidence**.

# 7) Important Limitations

- **Limited data on certain design dimensions:** Effects of `chat`, `reward` (and their cost/tech parameters), `show_punishment_id`, and default contribution framing on efficiency are rarely isolated or tested.
- **Mapping from non-payoff outcomes (e.g., cooperation rates) to efficiency is not always linear or consistent—intervention costs may swamp contribution gains, especially when punishment is costly or misdirected** (Nhim et al., 2023; Cooney, 2025).
- **Effects are often conditional and non-monotonic:** The benefit of punishment can be reversed if the cost is too high, if antisocial punishment is frequent, or if cognitive/informational constraints impair effective punishment targeting (dos Santos et al., 2014).
- **Some key moderators (e.g., player motivation, social context, externalities, institutional uptake, initial conditions) are identified in theory but not always tested or measured empirically.**
- **Empirical evidence is mostly lab-based with small groups**; field and large-scale institutional contexts are less well covered.
- **Voluntary punishment regimes in which participation or ambition can be avoided typically do not improve efficiency; findings from mandatory/enforced games may not generalize to voluntary-institution contexts** (Del Ponte et al., 2025).
- **Construct generalizability:** Several adjacent theoretical papers model variants of the PGG or related dilemmas with structural differences that may preclude direct transferability.
- **No single study covers the full span of the 14 prediction-relevant dimensions; synthesis is needed across studies with different designs.**
- **Potential for publication bias:** The absence of reported efficiency losses in some studies may reflect selective reporting.

**In summary**, the literature base provides a well-developed, nuanced picture of when and how punishment increases efficiency in PGG-like environments, with strong support for certain game design and parameter effects on treatment efficiency versus control. However, evidence is incomplete for several dimensions, effects are conditional, and mapping from behavioral outcomes to payoff requires caution. Careful attention to cost structures, group size, game length, punishment technology, and baseline efficiency is necessary for accurate prediction.
