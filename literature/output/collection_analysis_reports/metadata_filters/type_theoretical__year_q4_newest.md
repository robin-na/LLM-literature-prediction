# 1) Evidence Base

The paper set contains **only theoretical work** (no papers report empirical or experimental data) but is exceptionally broad and deep with respect to modeling approaches, mechanisms, and parameter exploration in **public goods games (PGGs) and closely related settings**. It covers an array of **payoff-based outcomes**, with a substantial subset focusing **directly and explicitly on efficiency or group payoff**—the central outcome of the prediction task. The evidence base includes exact PGG models, close PGG variants (common-pool resource games, threshold public goods, trust games, repeated PDs, etc.), and many adjacent or weakly related social dilemmas, with a mixture of standard and novel punishment mechanisms, institutional incentives, and hybrid reward-punishment structures. While the lack of direct empirical experiments is a limitation for real-world generalizability, the diversity, mechanistic detail, and explicit formulas in the theory papers make this evidence base unusually rich for prediction in design space.

# 2) Task Relevance

- **pgg_or_variant:**  
  - **Exact:** A significant portion of the papers directly analyze classic public goods games (PGGs), with explicit modeling of group contributions, MPCR, round structure, etc.
  - **Close:** A large set cover close variants, such as common-pool resource (CPR) games, threshold public goods, trust/reciprocity games, or repeated PDs with group structure, which share critical mechanisms but may differ in action space, outcome mapping, or cost-benefit structure.
  - **Adjacent/Weak:** Many others are in adjacent domains (PDs, networked social dilemmas, signaling, norm enforcement) and do not map with high fidelity to PGGs but still model mechanisms like costly punishment, exclusion, or reward.
  - **None:** Only a handful have no real relation to PGGs.

- **punishment_or_sanctions:**  
  - **Exact:** Many papers model “punishment enabled vs. disabled” manipulations or institutional/peer punishment rules matching the prediction variable.
  - **Close:** Others study variants, such as exclusion, indirect reciprocity as stand-in punishment, dynamic taxation, or anti-social punishment.
  - **Adjacent/Weak:** Several use mechanisms like partner choice or reputation as “soft” punishment, which do not fully capture the cost/impact of classic punishment.
  - **None:** Some papers entirely focus on non-punitive mechanisms (reward-only, social norms, or group selection).

- **efficiency_or_related_payoff_outcome:**  
  - **Exact:** A significant number of theory papers present **explicit efficiency outcomes** (payoff as a fraction of maximum, group welfare, average payoff, surplus, etc.) with clear mapping to the prediction target.
  - **Close:** Others report “group payoff,” “resources remaining,” or “probability of group success” in settings analogous to efficiency but requiring mapping.
  - **Adjacent/Weak:** Many papers focus on cooperation rates, prevalence of strategies, or stability/bistability of cooperation versus defection (non-payoff behavioral outcomes).
  - **None:** Papers about norm internalization, structural alignment, or reputation metrics without mapping to payoff or efficiency.

**Overall:**  
The set offers **high coverage of exact or close PGGs with punishment manipulations and efficiency outcomes**; adjacent papers provide context for game design factors, mechanisms, and possible boundary violations or exceptions.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (direct relevance for prediction):**
  - **Efficiency (ratio to optimum):** _Explicitly reported in many theory and simulation papers._ E.g., “group efficiency,” “average payoff as a fraction of cooperative optimum,” “group welfare,” “mean payoff,” “resource sustainability.”
  - **Group payoff / total earnings / surplus:** Often directly analyzed for both control (no punishment) and treatment (punishment enabled) scenarios.
  - **Welfare, social welfare:** Used as direct analogs for efficiency.

- **Non-payoff behavioral outcomes (must be distinguished):**
  - **Cooperation/contribution rates:** _Very frequently reported_, but recognized in the digest as not equivalent to efficiency. Should not be used as direct predictors except where mapping to payoff is verified.
  - **Strategy frequencies/dynamics:** Prevalence of cooperators, defectors, punishers, rewards, excluders.
  - **Phase diagrams, equilibrium characterization:** Game regions classified by dominant strategy but not by payoff.
  - **Norm compliance, trust prevalence:** Relevant for mechanisms but not payoff outcomes on their own.
  - **Resource status/abundance separated from payoff:** Sometimes used as a proxy, but only if explicitly linked to group payoff.

**The literature takes care to distinguish between behavioral and payoff-level results; only explicit payoff/efficiency measures should be directly used in prediction.**

# 4) Main Findings Relevant To Prediction

## Cross-paper Synthesis

- **Punishment (peer, institutional, or exclusion) almost always increases efficiency** versus a low-efficiency control _when_:
  - **Punishment is sufficiently strong and not too costly** (there are explicit cost/impact thresholds in many models).
  - The control game (punishment disabled) yields low efficiency (i.e., cooperation does not self-sustain).

- **The size and sign of the efficiency gain (vs. control) is highly moderated by**:
  - **Punishment cost and effectiveness** (fine-to-cost ratio, magnitude, impact per unit cost).
  - **Marginal per-capita return (MPCR)**: Higher returns make it easier for punishment to achieve full efficiency.
  - **Player count (group size):** Larger groups often require more effective/cheaper punishment; otherwise, efficiency gains fade and can even reverse.
  - **Network or population structure:** Structured populations (e.g., lattices, small-world, regular graphs) expand the parameter regime where punishment increases efficiency. Some models (e.g., well-mixed infinite populations) require stricter conditions.
  - **Type of punishment:** Institutional/tax-based punishment is often more effective (and less prone to second-order free rider problems) than peer punishment. Social exclusion and hybrid punishment/reward are sometimes superior.
  - **Presence of reward:** Combined reward and punishment can yield higher efficiency, but reward alone rarely eliminates defectors in PGG-like settings.
  - **Punishment targeting and selectivity:** Targeted punishment (e.g., “punish the lowest contributor”) is often optimal for efficiency, minimizing unnecessary costs.

- **Boundary effects and exceptions:**
  - **Very costly, inefficient, or mis-targeted punishment can reduce efficiency below control** (particularly in peer punishment or antisocial punishment regimes).
  - **High initial cooperation** in control (or when network reciprocity is strong) can mean the addition of punishment is neutral or even negative for efficiency.
  - **Bistability and initial conditions:** In some models, both defective and efficient equilibria are possible—with punishment shifting the attraction basins, but not guaranteeing high efficiency from all starting points.
  - **Special structures (e.g., commitment stages, voluntary participation):** The effect of punishment on efficiency can be reversed or limited; reward or opt-out options may sometimes work better.

- **Quantitative guidance:**
  - Many models **provide explicit threshold conditions or analytic formulas** for efficiency change as a function of punishment cost, fine, group size, MPCR, etc.—these can be directly used for mapping game design to treatment efficiency.

## Payoff vs. Behavioral Outcomes

- Some **papers only report increased cooperation/contribution rates** (not payoffs): these should not be mapped onto efficiency unless the cost/benefit structure is confirmed to support it.

- **Proofs that increasing cooperation does not necessarily increase efficiency** (due to punishment imposition costs) are common, especially in peer punishment models.

# 5) Prediction Guidance

- **For prediction of average efficiency in PGG-like games with peer punishment enabled:**
  - **If the control (no-punishment) efficiency is low and the design dimensions imply that punishment cost is not excessive and effectiveness is high**, expect a substantial increase in efficiency, often approaching cooperative optimum.
  - **The effect size (treatment-control efficiency difference) can be estimated from explicit formulas** in theory papers mapping from player count, MPCR, punishment cost, punishment magnitude, and network structure.
  - **Efficiency improvements will be smaller or may be negative** if:
    - **Punishment is peer-based and costly** (often resulting in welfare loss even if cooperation rises),
    - **Punishment is mistargeted (e.g., antisocial or nonselective punishment),**
    - **Reward or exclusion mechanisms are absent in settings where they are the efficient enforcement technology,**
    - **Control efficiency is already high due to baseline reciprocity or network structure.**
  - **Adjunct mechanisms (e.g., information, communication, reputation):**
    - Typically **augment** the effectiveness of punishment and can lower the necessary punishment cost/magnitude threshold to achieve high efficiency.
  - **In resource management or threshold games:** The **baseline resource growth rate and group risk structure** are additional crucial moderators—is there a renewable resource, and does cooperation actually prevent collapse?
  - **If design dimensions correspond to very large group size or low punishment effectiveness,** expect little or no improvement in efficiency; the effect is often strictly parameter-bounded.

- **In sum:** The best prediction accuracy is achieved by applying **analytically derived thresholds and payoff formulas** from theory papers, using the control efficiency and 14 design dimensions to infer whether the punishment-enabled game will yield (a) a sharp transition to full or near-full efficiency, (b) moderate improvement from baseline, or (c) no or negative change if punishment is too costly or inefficient.

# 6) Design Dimensions Highlighted Across Papers

- **Directly informed dimensions (from exact and close theory papers):**
  - `player_count` (group size): Key in threshold conditions and in scaling of punishment effectiveness and cost.
  - `num_rounds`: Implicit in models with repeated interaction, stability of cooperation, and learning; affects the credibility of punishment threats.
  - `all_or_nothing`: Many models handle both continuous and binary action; critical for payoff mapping and optimal punishment targeting.
  - `mpcr` (synergy factor): Central moderator—the most commonly varied experimental parameter.
  - `punishment_cost`, `punishment_tech` (effectiveness of punishment per cost/fine): These are often parameterized directly in analytic threshold formulas.
  - `reward_exists`, `reward_cost`, `reward_tech`: Explored especially in hybrid reward/punishment models.
  - `show_other_summaries`, `show_n_rounds`: Information structure affects punishment institution formation and learning.
  - `show_punishment_id`: Sometimes analyzed in reputation/information models.

- **Indirectly informed or only contextually discussed dimensions:**
  - `chat`: Sometimes included in extended models (higher importance in adjacent papers), mostly via its effect on norm formation, but rarely parameterized for efficiency mapping.
  - `default_contrib`: Framing and default choices are contextually analyzed; limited direct evidence for their impact on efficiency change due to punishment.
  - `show_punishment_id`: Infrequently directly studied as a moderator of efficiency for punishment effects.

- **Effectively missing or weakly informed:**
  - Some dimensions, especially default framing variables (`default_contrib`), and visibility variables (`chat`, `show_punishment_id`) are undercharacterized in most exact theory papers, limiting the ability to make high-confidence predictions when these are the principal differences in design.

# 7) Important Limitations

- **Absence of empirical calibration:** All findings are from theoretical/simulation work; actual human or field subject behavior may deviate from model predictions, especially due to psychological or institutional complications not captured in models.
- **Mapping from behavioral to payoff outcomes:** In many adjacent or weaker papers, cooperation rates, strategy frequencies, or equilibrium structure are reported, not efficiency—mapping these to group payoff can only be done when cost structures are clear and comparable.
- **Boundary regime sensitivity:** Many theory papers report abrupt or non-monotonic threshold effects and bistability; outcomes may be highly sensitive to specific parameter values or initial conditions, requiring careful parameter mapping for precise prediction.
- **Design dimensions incompletely explored:** For several design features (e.g., communication, chat, punishment observability), the direct moderating effect on efficiency with punishment enabled vs. disabled is not parametrically established.
- **Peer punishment is often less efficient:** While enabling punishment generally improves efficiency when baseline efficiency is low, peer punishment is repeatedly shown to reduce efficiency if costs per act are high; institutional or well-tuned selective punishment is often a necessary condition for full efficiency improvements.
- **Empirical missing evidence:** There is limited or no direct laboratory or field validation of theoretical predictions for some complex hybrid models or for large group sizes/settings not practically tested.
- **Generalizability to experimental PGGs:** Some close or adjacent papers use resource, trust, or PD frameworks with similar but not identical incentive structures; direct mapping to canonical PGGs may not always be strictly valid.

---

**In conclusion:**  
This literature base provides **strong, mechanistically explicit theoretical support for predicting efficiency effects of punishment in public goods games, especially for core design dimensions** (group size, MPCR, punishment cost/effectiveness, network structure) and for settings where the control game is inefficient and the punishment mechanism crosses analytic thresholds for effectiveness. The prediction should be made using the explicit parameter formulas or outcome maps from these theory papers, being cautious to apply only models where design dimensions (including type of punishment, structure, and cost) match the scenario, and restricting behavioral-result-based inferences to situations where payoff mapping is justified and explicit. Limitations stem from the absence of empirical data, incomplete treatment of some dimensions, and known sensitivity/bistability in many theoretical models.
