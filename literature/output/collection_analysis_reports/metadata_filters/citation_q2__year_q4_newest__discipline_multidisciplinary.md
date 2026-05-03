# 1) Evidence Base

The paper set includes 26 studies, with a mixture of **empirical lab experiments** (especially on public goods games and variants) and **theoretical models** (using replicator dynamics, evolutionary game theory, and simulations). The set is **broad in contextual and design dimension coverage** but is **narrower** in directly addressing the core prediction task: most papers are adjacent or indirect concerning the prediction of **efficiency outcomes from enabling peer punishment** in classic or modified PGGs given specific design parameters and control efficiency levels.

Within this set, only a **small subset of papers** provides **direct empirical or theoretical evidence** on the effect of enabling punishment on group efficiency or related payoff-based outcomes in exact PGG settings. Many papers are **theoretical or empirical studies on adjacent games**, focus on non-payoff outcomes (like cooperation rates or punishment frequency), or lack explicit manipulation of punishment mechanisms.

# 2) Task Relevance

**Summary of task-relevance of the literature set:**

- **pgg_or_variant**: The set includes several papers with **exact** PGG designs (e.g., Lo Iacono et al., 2023; Salahshour et al., 2022; Dickson et al., 2022), but many papers use **adjacent** or **close** models (nested games, resource dilemmas, contests, etc.), with much theoretical work examining mechanisms outside the canonical PGG.

- **punishment_or_sanctions**: A subset manipulates or models **peer punishment** or institutional sanctions (**exact**); several papers investigate only reward, reputation, or no explicit sanctioning (**adjacent/none**).

- **efficiency_or_related_payoff_outcome**: Only a handful (notably: Lo Iacono et al., 2023; Salahshour et al., 2022; Romano et al., 2024; Mondal et al., 2022) report **group efficiency or closely related payoff-based outcomes** as primary results (**exact/close**). Many others measure behavioral variables (contribution rates, cooperation, punishment frequency) (**weak/none** for the downstream task).

**Consistency in relevance labeling:**
- **Exact**: Lo Iacono et al. (2023), Salahshour et al. (2022) for all three dimensions.
- **Close/Adjacent**: Many theory and adjacently structured empirical papers address punishment (sometimes as reputation or third-party action) without directly measuring efficiency in standard PGGs.
- **Weak/None**: Papers focusing purely on cooperation dynamics or network outcomes, without either punishment or efficiency metrics.

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes:**
- *Group efficiency*, *average profit/welfare*, and *total earnings* are primary in a **small number of studies** (Lo Iacono et al., 2023; Salahshour et al., 2022; Romano et al., 2024; Mondal et al., 2022; Schnell & Muthukrishna, 2024; Murase & Hilbe, 2024).
    - Lo Iacono et al. (2023): Direct measurement of efficiency in exact PGGs.
    - Salahshour et al. (2022): Efficiency under noisy punishment.
    - Romano et al. (2024): Efficiency in nested social dilemmas with punishment/attack options.
    - Mondal et al. (2022): Efficiency as equilibrium total payoff in theory.
    - Several theories (Murase & Hilbe, Schnell & Muthukrishna) consider welfare/efficiency but often in more abstracted environments.

**Non-Payoff Behavioral Outcomes:**
- *Contribution/cooperation rates*, *punishment frequency*, *norm compliance*, *strategy prevalence*, or *punishment assignment* are far more **common** outcomes.
    - Many studies measure how design dimensions affect these behavioral variables.
    - Some discuss possible efficiency implications without providing direct payoff data.

# 4) Main Findings Relevant To Prediction

**Synthesis of cross-paper findings for predicting efficiency effects of peer punishment:**

- **Enabling Peer Punishment Increases or Sustains Efficiency (under standard conditions):**
    - In canonical PGGs (fixed group size, sufficient rounds, deterministic punishment, moderate cost), *enabling peer punishment reliably increases efficiency* relative to control (no-punishment) games, with effects robust across labs and sampling (Lo Iacono et al., 2023).
    - The effect is *not immediate*—it emerges over consecutive rounds as punishment supports norm compliance and discourages defection.
    - ***Empirical finding (exact, payoff):*** Peer punishment is a robust mechanism for increasing efficiency when well-implemented.

- **Moderators and Boundary Conditions:**
    - **Punishment Technology (Noise/Determinism):** When punishment is stochastic/noisy (uncertain impact), *efficiency gains disappear or reverse*. Noise increases antisocial punishment and lowers both contributions and average payoffs (Salahshour et al., 2022).
    - **Antisocial Punishment:** Punishment not aligned with norm enforcement (e.g., status-driven, attack-for-attack’s-sake) can *reduce efficiency*, sometimes making efficiency lower in punishment conditions than controls (Romano et al., 2024).
    - **Institutional Features:** The presence of legitimate, fair, or procedural aspects in centralized punishment regimes **increases contributions** (Dickson et al., 2022), but direct efficiency outcome is only inferred, not measured.
    - **Ecological and Game Structure Moderators:** In resource games, low resource growth can undermine the positive effect of punishment, while sufficient punishment and monitoring can shift whole-system dynamics toward high efficiency (Mondal et al., 2022; Sarkar, 2023, theory).
    - **Population/Nested Structure:** The scale of cooperation (local vs. global) affects the ability of reputational or indirect punishment to increase efficiency. In nested/grouped settings, punishment at one level can undermine efficiency at another (Schnell & Muthukrishna, 2024; Murase & Hilbe, 2024).
    - **Game Discreteness:** In continuous-action games, similarity-based social sanctions alone do *not* stabilize high cooperation/efficiency; additional mechanisms (moral preferences, discrete categories) may be needed (Yan et al., 2023, theory).

- **Comparative Reward Effects:** Reward can encourage cooperation, but (theory) is less effective than punishment at achieving maximum efficiency, since defectors may persist despite reward (Mondal et al., 2022).

# 5) Prediction Guidance

**How should this literature guide prediction of treatment efficiency, given control efficiency and game design?**

- Predict that **enabling peer punishment will increase average efficiency relative to control** when:
    - The PGG is *standard* in structure (as in Lo Iacono et al., 2023): moderate group size (e.g., ~12), 30+ rounds, linear MPCR, no exogenous shocks, deterministic punishment technology, moderate to low punishment cost (e.g., 1:3 cost-impact ratio).
    - The punishment **technology is deterministic** (no noise, clear mapping from punishment action to payoff deduction) and antisocial punishment is minimal.
    - There are no strong contest/status incentives misaligned with norm enforcement.
- Predict that **gains may be smaller or negative** when:
    - **Punishment implementation is noisy or ambiguous** (e.g., high variance of punishment impact) or when **antisocial punishment is prevalent**.
    - The game's social structure or institutions facilitate competition or attacks for non-normative reasons (Romano et al., 2024).
    - The environment has features undermining norm enforcement (low resource growth in resource dilemmas; high fragmentation in population structure).
- For **other design dimensions** not directly manipulated (chat, default contribution, visibility, etc.), evidence is **sparse** or only indirectly discussed.
- **Magnitude of effect:** Empirical results indicate that **efficiency gains can be large** (substantial in Lo Iacono et al., muted or reversed in Salahshour et al. with noise, negative in certain contest/attack contexts per Romano et al.). There is no strong evidence for non-linear scaling by group size, round count, or MPCR within the tight empirical parameter bands tested.
- When the **control game is already efficient**, the *incremental effect* of enabling punishment may be small.

**Where the literature is silent (dimension not tested, setting not studied), prediction should rely on baseline patterns and caution.**

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions:**
- `player_count` (Lo Iacono et al., Salahshour et al., Romano et al., theory papers)
- `num_rounds` (Lo Iacono et al., Salahshour et al., theory)
- `mpcr` (Lo Iacono et al., Salahshour et al., theory)
- `punishment_cost` (Lo Iacono et al., Salahshour et al., Romano et al., theory)
- `punishment_tech` (**determinism vs. noise** directly tested, Salahshour et al.)

**Indirectly or contextually informed:**
- `all_or_nothing` (frequent in model formulation, less in parameter variation)
- `reward_exists`, `reward_cost`, `reward_tech` (more in theory, little comparative empirical work on reward vs. punishment)
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id` (rarely manipulated or outcome-linked)
- `chat`, `default_contrib`, `show_n_rounds` (included in games as control variables, but not examined as moderators of efficiency effect for punishment)

**Missing or minimally addressed:**
- Effects of enabling **chat**, changing **default contribution framing**, showing **punishment/reward identities**, or *visibility/manipulation* of summaries. No papers manipulate or report on the predictive contribution of these dimensions for efficiency outcomes under punishment.

# 7) Important Limitations

- **Few exact empirical studies**: Strong payoff-based efficiency evidence comes mainly from *one experimental paradigm* (Lo Iacono et al., 2023), with design tightly fixed—generalizability to other parameterizations is limited.
- **Sparse empirical moderation**: Variation in key design dimensions outside a narrow band (e.g., effects of very high punishment cost, vastly different group size, different feedback visibility, or configurational differences in chat or social information) is essentially untested.
- **Over-reliance on theory for many design dimensions**: Some important moderators (joint liability, nested group structure, resource dynamics, continuous/discrete contribution) are supported by theoretical modeling, not direct experiment, making their predictive utility more speculative.
- **Ambiguity in real-world implementation**: Mechanisms like legitimacy, antisocial punishment, and contest motives are clearly important, but limited empirical work quantifies these as moderators of payoff outcomes in standard PGGs.
- **Common focus on behavioral, not payoff outcomes**: The bulk of the literature still assesses cooperation/contribution rates, *not* directly group efficiency (payoff relative to optimal), which is required for the task.
- **Contextual scope**: Several adjacent or weakly related studies provide only indirect insights, potentially muddying strong inference about classic PGGs with peer punishment.

---

**In summary:**  
Strong evidence supports prediction that, under standard deterministic peer punishment conditions, enabling punishment increases efficiency compared to no-punishment controls, especially in canonical PGG designs. The size and direction of the effect depend critically on punishment technology, antisocial punishment, and game incentives—few papers systematically vary additional design dimensions. Prediction outside the well-studied domain is possible only via cautious extrapolation informed by theory and adjacent findings, acknowledging major limitations in the scope and depth of current empirical evidence about multidimensional design parameter moderation.
