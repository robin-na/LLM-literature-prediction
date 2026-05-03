# 1) Evidence Base

The provided paper set is predominantly empirical, with a strong focus on laboratory experiments, supplemented by a few field experiments. The majority of the studies use experimental manipulations to analyze cooperation, punishment, and related outcomes in public-goods-game (PGG) environments or variants thereof. A subset addresses closely related games (ultimatum game, CPR games, prisoner's dilemma, etc.), sometimes modifying key mechanisms (e.g., network adaptation, redistribution, leader punishment).

Most papers report behavioral outcomes (contribution rate, compliance, cooperation), and several report payoff-based outcomes such as group payoff, efficiency, surplus, or net profit. A portion of the literature does not report efficiency-related measures, instead limiting findings to behavioral or mechanism evidence.

Overall, the evidence base is moderately broad in terms of game design dimensions and environmental features, with direct coverage of standard linear PGGs with punishment as well as related institutions (centralized punishment, partial punishment networks, threshold targets). However, direct, high-relevance evidence for all 14 prediction dimensions is patchy, and some dimensions are rarely or never systematically tested (e.g., chat, default contribution, reward mechanisms, information display). The theoretical arguments are limited; most inferences and guidance are empirical.

# 2) Task Relevance

The paper set's relevance to the prediction task—predicting treatment efficiency from design features and baseline (control) efficiency—varies by dimension:

| Dimension                 | Relevance Rating | Synthesis |
|---------------------------|-----------------|-----------|
| `pgg_or_variant`          | **exact/close** | The core experiments (Bahbouhi et al., Pi et al., Castillo et al., Wang & Huang, Jiang et al.) employ classic, repeated linear PGGs or highly analogous variants (e.g., snowdrift, CPR, collective risk, redistribution games). Several others use structurally adjacent designs (ultimatum game, prisoner's dilemma, CPR). Relevance is high for standard PGGs, with diminishing directness for neighboring paradigms. |
| `punishment_or_sanctions` | **exact**       | A substantial subset implements peer punishment or institutionalized (centralized) sanctioning, some with variations (network structure, cost, magnitude, centralization, probabilistic application). A second subset examines reward, feedback, or leader sanctions. Not all studies compare to true no-punishment baselines. |
| `efficiency_or_related_payoff_outcome` | **exact/close** | Several studies directly report efficiency, group payoff, or surplus, supporting direct comparison to the task outcome. However, some key studies report only behavioral proxies (cooperation rate, compliance) and discuss efficiency only implicitly or in discussion. Adjacent papers often omit payoff measures, limiting their direct predictive value. |

Thus, the evidence set offers **direct** and **highly relevant** empirical support for the prediction task for classic PGGs with peer punishment, especially on efficiency outcomes. Coverage is weaker for non-standard variants, alternative sanctioning forms, and some detailed design dimensions.

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes:**
- **Efficiency / Net Profit / Group Payoff**: Frequently measured directly (Bahbouhi et al., Pi et al., Castillo et al., Wang & Huang, Jiang et al., Przepiorka & Diekmann, Fabbri et al., partially Abbink et al.).
- **Welfare, Surplus, Total Coins**: Sometimes inferred from reported payoffs (e.g., group earnings).
- **Compliance/Revenue** (in policy or field contexts as proxies for efficiency, e.g., ticket sales in Fabbri et al.).

**Non-Payoff Behavioral Outcomes:**
- **Contribution/Cooperation Rate**: Ubiquitous. Used as the main measure in some papers not reporting payoffs (Pan et al., Becchetti et al., Weng et al.).
- **Punishment Frequency/Type, Norm Compliance, Slack Reduction**: Used to understand mechanisms or behavioral processes, sometimes without direct linkage to payoffs.
- **Volunteering/Participation, Information Preferences**: Behaviorally illustrative but not directly tied to efficiency.

**Distinction:**  
While high contribution rates usually support higher group payoff, efficiency measures account for the cost of sanctions; thus, punishment can increase contributions but still reduce efficiency if the sanction cost outweighs cooperation gains (e.g., Abbink et al.). Some mechanism-focused studies do not report efficiency outcomes.

# 4) Main Findings Relevant To Prediction

**Empirical Synthesis on Punishment and Efficiency:**
- *General Effect*: Introducing peer punishment in standard repeated PGGs **typically increases group efficiency (net profits/payoff)** relative to baseline, by increasing cooperation and deterring free riding, though the effect is contingent on key game parameters and punishment structure (Bahbouhi et al., Pi et al., Castillo et al., Wang & Huang, Jiang et al.).
- *Role of Costly Punishment*: Efficiency gains hinge on the **relative cost and deterrence value** of punishment. When punishment is too costly or too weak, efficiency does not improve (Abbink et al., Jiang et al.). If punishment is frequent but only partially deters free riding, costs can erode efficiency.
- *Moderators:*
    - **Decision Rule / Team Structure**: Team-based punishment (especially with unanimity) reduces anti-social, wasteful punishment and **boosts efficiency** (Bahbouhi et al.).
    - **Punishment Network Structure**: Incomplete punishment networks (e.g., circles, pairwise) can **increase efficiency** relative to complete networks by curbing bystander effects and minimizing redundant or anti-social punishment (Pi et al.).
    - **Centralized vs. Peer Punishment**: Centralized institutions with a single enforcer **increase efficiency robustly**, independent of manager selection method (Castillo et al.).
    - **Punishment Strength and Risk**: Punishment has a **threshold effect**—it raises efficiency only when **punishment is strong and credible** (Jiang et al.). Larger groups require stronger deterrence.
    - **Observability and Norms**: Informing players about potential for punishment affects behavior and can stabilize cooperation and payoff, even when sanctions are unobservable (Wang & Huang).
    - **Field Context and Realism**: In field or framed environments, peer punishment/reward does **not always increase efficiency or cooperation** (Noussair et al., Fabbri et al.), highlighting contextual limits.
    - **Reward Mechanisms**: When layered onto punishment regimes, **rewards can further raise compliance and efficiency** (Fabbri et al.), but cost and sustainability matter.

**Theoretical and Mechanism Arguments:**
- **Punishment as Deterrence**: Sanctioning deters free riding if costs are low relative to effect and norm adherence is strong.
- **Anti-social Punishment**: Wasteful or misdirected punishment can decrease group efficiency.
- **Feedback and Social Information**: Public feedback/ratings can substitute for formal sanctions in boosting efficiency in some variants (Przepiorka & Diekmann).
- **Endogenous Networks/Choices**: Adaptive partner selection (tie-breaking) functions like non-monetary sanctions but is structurally distinct from standard punishment (Sun et al., Pan et al.).

# 5) Prediction Guidance

**For Predicting Treatment Efficiency in PGG-like Environments:**

- When **peer punishment is enabled in a repeated linear PGG**, and punishment cost and magnitude are within empirically tested ranges, **treatment efficiency will generally rise** relative to a no-punishment control—*but* this is conditional on effective deterrence and the avoidance of excessive, wasteful punishment.
    - **Magnitude of efficiency increase** is mediated by design choices: network structure (`punishment_tech`), team decision rule (`player_count` and team composition), punishment cost (`punishment_cost`), and the structure of information/feedback.
- If **punishment is too costly, too weak, or misapplied (e.g., anti-social, not deterring free riding)**, efficiency gains may be negligible or negative. Beware false positives from rising cooperation rates that are offset by high sanction costs.
- **Team-based or unanimity decisions** in punishment **improve efficiency** through filtered, less anti-social sanctioning.
- **Centralized punishment** (one enforcer) produces **strong, robust efficiency improvements**, regardless of the enforcer’s selection.
- **Incomplete or networked punishment regimes** may outperform complete-peer punishment by reducing over-punishing or bystander effects.
- **Larger groups or riskier targets** may need **stronger, more credible punishment** to maintain efficiency gains.
- **Field environments** and some adjacent game structures (CPR, ultimatum, real-world compliance) display **less robust positive effects**—punishment may not improve or may even reduce efficiency.
- **Control (no-punishment) efficiency** remains a vital baseline for prediction, as some designs have high initial cooperation regardless of punishment.

**Practical Use:** For comparable settings (repeated linear PGGs with standard parameterizations), expect treatment efficiency > control efficiency (punishment disabled), especially when:
- Punishment cost is moderate/low, network structure is incomplete or centralized, and team decision making reduces antisocial punishment.  
However, always check for excessive sanction costs and group/game features that may reverse this effect.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- **player_count**: Regularly varied (2–30); group size moderates punishment effects, especially for centralized punishment and threshold games.
- **num_rounds**: Most experiments use repeated games (typically 10–20 rounds), showing robust effects over time, with decay in cooperation sometimes observed.
- **mpcr**: Explicitly manipulated; lower MPCR makes cooperation less attractive and increases the role of punishment.
- **punishment_cost / punishment_tech**: Central to many papers; cost, network topology (who can punish whom), and centralization structure are key moderators of treatment efficiency.
- **all_or_nothing**: Both continuous and all-or-nothing designs appear; relevant for generalization.
- **show_n_rounds / show_other_summaries**: Sometimes reported; public information/feedback is shown to enhance cooperation and efficiency.
- **reward_exists**: Explored in select studies, typically as an adjunct to punishment.

**Indirectly Informed or Contextually Discussed:**
- **chat**: Some mention absence/presence; generally found to increase cooperation but specifics for interaction with punishment are sparse.
- **default_contrib**: Framing (opt-in/out) is specified in a few, but its interaction with punishment is rarely the focus.
- **reward_cost / reward_tech**: Field and hybrid lab/field studies (e.g., Fabbri et al.) provide some evidence, but less systematic.
- **show_punishment_id**: Sometimes included in feedback treatments; public identification may increase deterrence without direct payoff loss.

**Effectively Missing/Under-addressed:**
- **Punishment magnitude** (distinct from cost)
- **Combined reward and punishment technologies** in the same PGG experiment
- **Complex feedback variants** (e.g., real-time detailed feedback, anonymity effects)

# 7) Important Limitations

- **Gaps in Dimensional Coverage**: Many design dimensions relevant to prediction (default contribution, chat, reward mechanisms, punishment identity) are inconsistently reported or analyzed; effects are extrapolated from a subset of studies.
- **Limited Generalizability**: Most evidence comes from controlled laboratory settings; field and more ecologically valid studies sometimes diverge, warning against direct transfer of findings.
- **Efficiency Often Inferred**: Some studies infer efficiency gains from behavioral outcomes rather than reporting direct payoff ratios, introducing ambiguity (increases in cooperation do not always translate to higher efficiency).
- **Variation in Punishment Application**: Moderator effects (team rules, network structure, manager selection) are substantial—punishment does not have uniform effects across game formats.
- **Scarcity of Negative Results**: Few studies demonstrate outright efficiency losses in standard PGGs with punishment, but there is strong evidence in related games (e.g., ultimatum) and field settings, highlighting context sensitivity.
- **Ambiguity on Extreme Parameter Values**: Limited evidence for large groups, high punishment costs, rare sanctions, or very long games.
- **Behavioral Mechanism Papers**: Several works report only behavioral changes, limiting their value for efficiency prediction.

**Summary:**  
The literature set provides valuable empirical guidance for predicting the efficiency impact of enabling peer punishment in public goods games as a function of key game design dimensions and control efficiency, especially for canonical lab PGGs. However, extrapolation to untested parameter spaces, complex or hybrid institutional settings, or real-world environments demands caution, considering the incomplete design coverage and conditional effects demonstrated across studies.
