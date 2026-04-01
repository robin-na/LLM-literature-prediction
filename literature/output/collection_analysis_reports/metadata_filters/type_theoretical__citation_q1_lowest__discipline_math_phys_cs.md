# 1) Evidence Base

The evidence base for the downstream prediction task—forecasting average group efficiency in public-goods-game-like environments with punishment enabled versus control—is *narrow but deep* on theory, with the corpus consisting entirely of **theoretical and computational studies**. There are no empirical or laboratory experimental data. Nearly all papers use mathematical modeling, simulation, and analytic arguments.

The paper set is:
- **Rich in modeling direct PGGs and close variants**: Many papers examine classic or spatial public goods games, often with sophisticated population structures, incentive schemes, and evolutionary update rules.
- **Highly focused on mechanisms of punishment and its alternatives**: Theoretical explorations include both peer and institutional punishment, resource reallocation (fines, compensation), hybrid reward-punishment schemes, and effects of costs, thresholds, and network topology.
- **Skewed toward simulation and equilibrium analysis**: Outcomes are almost always reported via equilibrium cooperation rates, average payoffs (efficiency), and, at times, conditions for the stability of efficient equilibria.
- **Sparse in empirical calibration**: There is **no direct experimental calibration** of “control efficiency” versus “treatment efficiency”—i.e., predicted efficiency with punishment enabled, conditional on the observed (or simulated) efficiency in the absence of punishment.

## Types of outcomes and coverage:
- **Payoff-based outcomes (efficiency, total welfare, average payoff)** are primary in a substantial subset (especially the most relevant PGG/punishment studies).
- **Behavioral outcomes** (contribution/cooperation rates, prevalence of punishers, strategic type frequencies) are reported in many papers, especially as indirect or leading indicators of efficiency.
- **Some ambiguity exists** in mapping cooperation rates to efficiency, especially in models with costly punishment, resource depletion, or second-order free-riding.

## Dimensional coverage:
The literature directly manipulates or theorizes about a subset of the **14 design dimensions** (see Section 6), most consistently **player count, number of rounds, all-or-nothing contributions, MPCR, punishment cost/tech, and network structure**. Others, such as chat, default contribution, and identity visibility, are rarely present.

# 2) Task Relevance

Relevance is assessed separately for:
- `pgg_or_variant`
- `punishment_or_sanctions`
- `efficiency_or_related_payoff_outcome`

### a. PGG or Variant

- **Exact relevance:** The bulk of high-signal findings comes from *exact* PGG models (classical, spatial, threshold, and variants with loners or pool punishment).
- **Close/adjacent relevance:** A nontrivial portion of the theoretical support is from *close* variants—common-pool resource games, voluntary contribution games, and (to a lesser degree) repeated Prisoner’s Dilemma. These are adjacent in structure and occasionally differ in incentive mechanisms or outcome mapping.
- **Weak/none:** Some adjacent models (trust games, crowd computing, network routing) contribute general insights, but are less directly informative.

### b. Punishment or Sanctions

- **Exact relevance:** Many papers manipulate *explicit punishment mechanisms*, ranging from peer to institutional, and various technological implementations (pool, peer, proportional, dynamic).
- **Close/adjacent:** Some examine functionally equivalent group exclusion, fines, incentive-based sanctions, and stochastic sanctions; others address indirect mechanisms (partner choice, ostracism) that serve as adjacent forms of sanction.
- **Weak/none:** A subset discusses only reward, communication, or non-punitive interventions; these do not inform the punishment effect directly.

### c. Efficiency or Related Payoff Outcome

- **Exact relevance:** A critical subset of papers isolates and models **average group payoff, efficiency (payoff as a fraction of the cooperative optimum), or total welfare**.
- **Close:** A number of works report average payoffs but focus interpretation on behavioral outcomes, or assume (rather than rigorously show) that higher cooperation rates translate automatically to higher efficiency.
- **Adjacent/weak:** Many papers report only behavioral outcomes, with efficiency inferred or not addressed at all.

**Summary:** The core of the literature is *exactly relevant* for PGG, punishment, and efficiency—but not every paper is strong on all three dimensions. Many highly cited or mechanistically rich studies focus on behavioral rather than efficiency outcomes, providing only indirect evidence.

# 3) Outcomes Measured in the Literature

- **Efficiency and payoff-based outcomes:** Explicitly calculated and compared in many theoretical and simulation models (e.g., Wu et al., 2014; Sun et al., 2025; Yang & Yang, 2024; Cui et al., 2022; Ishikawa & Fontanari, 2025; Gao & Li, 2023). Efficiency is unambiguously the central outcome in these cases.
    - This is usually expressed as average group payoff as a fraction of the fully cooperative maximum, or as average social welfare/surplus.
- **Behavioral outcomes:** Most papers also (or only) report:
    - Contribution/cooperation rates
    - Strategy frequencies (punishers, cooperators, defectors, loners, etc.)
    - Prevalence of institutional/governance types
    - Punishment or sanction rates
- **Intermediate/adjacent outcomes:**
    - Resource sustainability, network resilience, “achievement” (e.g., in networked climate games), and "group accomplishment" are used in some adjacent models.

**Distinction:** The best evidence for predicting *treatment efficiency* comes from papers that calculate average group payoff as an equilibrium property. Where only cooperation rates or behavioral frequencies are reported, inference on efficiency is possible only under assumptions about punishment cost and how closely cooperation maps to efficiency.

# 4) Main Findings Relevant To Prediction

## General Main Effects
- **Punishment typically increases efficiency relative to control**: Under the majority of modeled parameter regimes, *enabling punishment* (peer or institutional, especially with moderate/low cost and sufficient impact) increases group efficiency in PGGs compared to control games without punishment (Wu et al., 2014; Sun et al., 2025; Yang & Yang, 2024; Ohdaira, 2025; Cui et al., 2022; Gao et al., 2020; Botta et al., 2021).
- **The effect size depends on parameterization:**
    - **Punishment cost/effectiveness:** Lower punishment cost and/or higher punishment effectiveness (punishment tech) greatly amplify the efficiency effect. High-cost or low-effectiveness punishment can diminish or even reverse efficiency gains (Wu et al., 2014; Sun et al., 2025; Zhang et al., 2019; Cooney, 2025).
    - **MPCR (synergy factor):** The positive effect of punishment on efficiency is *especially strong when MPCR is low* and control efficiency is low (Wu et al., 2014; Cui et al., 2022; Botta et al., 2021).
    - **Collective willingness and consensus:** Punishment is only efficiency-enhancing when the willingness to punish and consensus to do so are high; instability in preferences can undermine or even reverse gains (Gao & Li, 2023; Greenwood et al., 2018).
    - **Group size and structure:** Larger groups often require cost sharing, lower per-punisher cost, or institutional mechanisms for high efficiency to emerge (Ishikawa & Fontanari, 2025).
    - **Population/network structure:** Small-world/topologically clustered networks tend to strengthen the positive effect of punishment (Cui et al., 2022; Sun et al., 2025).
    - **Institutional vs. peer punishment:** Institutional (tax-funded, centralized) punishment can yield higher efficiency and broader stability than peer punishment, especially with cost sharing (Yang & Yang, 2024; Ishikawa & Fontanari, 2025).
    - **Reward and hybrid schemes:** When combined with reward or fine distribution mechanisms, punishment can achieve or approach maximal efficiency, particularly in difficult environments (Sun et al., 2025; Lu et al., 2024; Wang et al., 2024).
    - **Threshold effects and bi-stability:** In games with threshold or nonlinear structure, *strong* enough punishment can abruptly shift the group to maximal efficiency, but below threshold, efficiency gains are not realized (Botta et al., 2021; Wang et al., 2024; Wang & Shen, 2024).

## Mechanistic Nuance and Limitations
- **Punishment can fail or backfire:** When punishment costs are high, willingness to punish is unstable, consensus thresholds are high, or initial conditions are unfavorable (few punishers), punishment may have no effect or can decrease efficiency (Gao & Li, 2023; Greenwood et al., 2018; Sun et al., 2024).
- **Redistribution of fines matters:** Allocating fines back to cooperators and punishers can mitigate efficiency losses from high-cost punishment; without this, the net effect can be neutral or negative at high punishment cost (Sun, Bi et al., 2024).
- **Second-order free-riding and anti-social punishment:** The prevalence of nonpunishers, “fence sitters”, or anti-social punishers can limit or complicate efficiency gains, especially if peer punishment is not well targeted or institutional contexts incentivize anti-social variants (Qian et al., 2023; Ishikawa & Fontanari, 2025).
- **Weak/modest effects in high-efficiency control:** If the *control game already achieves high efficiency* (via network reciprocity or other mechanisms), adding punishment may yield little additional gain or may even lower efficiency by introducing costs (Gao et al., 2025; Greenwood et al., 2018).
- **Empirical mapping is missing:** Most findings are theoretical/mechanistic. Quantitative prediction of *treatment* efficiency as a function of *control* efficiency (plus design dimensions) is possible only through strong model-based extrapolation, not direct empirical calibration.

# 5) Prediction Guidance

**How to use this literature to predict treatment efficiency given design dimensions and control efficiency:**

- **Main Expectation:** The presence of an efficient, well-designed punishment mechanism almost always increases efficiency relative to control *when control efficiency is low* (i.e., in challenging environments), provided punishment cost is not excessively high, punishment is well targeted, and willingness to punish is sufficient (Wu et al., 2014; Sun et al., 2025; Cui et al., 2022).
- **Exceptional Cases:** When control efficiency is already high (e.g., via network structure, reward schemes, or intrinsic reciprocity), adding punishment produces marginal or even negative efficiency changes due to added costs (Gao et al., 2025; Greenwood et al., 2018).
- **Parametric Sensitivity:**
    - ***MPCR (“synergy factor”) and punishment cost are critical moderators*:** Low MPCR (benefit of public good) and low efficiency in control amplify the positive impact of punishment, while high punishment cost can negate or reverse efficiency gains.
    - **Institutional context, group size, and fine distribution** also moderate the effect; institutional (tax-based, cost-shared) punishment is generally more reliable than voluntary or peer punishment at generating efficiency gains in large or heterogeneous groups (Yang & Yang, 2024; Ishikawa & Fontanari, 2025).
    - **Dynamic adjustment, feedback mechanisms, and fine redistribution** can further optimize efficiency, especially in resource-limited or complex games (Ohdaira, 2025; Gao, Pan & He, 2024).
    - **Threshold and consensus models**: In collective-decision or bi-stable games, a critical mass/willingness to punish is required for efficiency to improve—the effect is not monotonic (Gao & Li, 2023; Botta et al., 2021).
- **Prediction caveats:**
    - *Quantitative mapping* from control to treatment efficiency is model-dependent; predictions should reference parameter sweeps or phase diagrams from the most structurally similar theoretical models in the corpus.
    - **Behavioral outcome papers should not be over-interpreted** as supporting efficiency increases unless punishment costs and mapping from contributions to payoffs are clearly accounted for.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed:**  
- `player_count`, `num_rounds`, `all_or_nothing`, `mpcr`, `punishment_cost`, `punishment_tech`, `reward_exists`  
  (Regularly parameterized and modeled; strong evidence for their moderating role.)

**Indirectly or partially informed:**  
- `chat` (almost never examined, sometimes contextually discussed as “communication” outside the formal game but almost absent in efficiency outcome models)
- `default_contrib` (rarely if ever manipulated or studied as a framing effect)
- `reward_cost`, `reward_tech` (occasionally covered in hybrid reward-punishment models)
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id` (very occasionally manipulated in reputation, communication, or information structure studies, but efficiency outcomes rarely tied directly to these variables)

**Contextually discussed, not modelled:**  
- Most design features related to **player information, feedback displays, default settings, and interface features** appear as contextual variables in a few conceptual or signaling theory papers, but are almost never linked explicitly to efficiency calculations.

**Effectively missing:**  
- `chat`, `default_contrib`, and `show_punishment_id` are almost entirely unaddressed as formal moderators of treatment effects on efficiency.

# 7) Important Limitations

**1. Absence of direct empirical data:**  
- All findings are theoretical or simulation-based. There is little to no empirical mapping from “control efficiency” to “treatment efficiency” in real-world experimental PGGs.

**2. Parameter regime dependence:**  
- Predictions are often *conditional* on parameter regimes (e.g., punishment cost, MPCR, consensus threshold). Extreme values outside these boundaries can drive null or negative effects.

**3. Overreliance on behavioral-outcome proxying:**  
- Many simulations report only cooperation rates; only a subset systematically accounts for the cost of punishment in efficiency calculations. Behavioral proxies may overstate efficiency gains if punishment is costly.

**4. Structural and model assumptions:**  
- Results can be highly sensitive to population structure (e.g., spatial vs. well-mixed), group size, deterministic vs. stochastic update rules, and learning mechanisms, undermining generalizability.

**5. Limited coverage of real-world institutional/psychological complexity:**  
- Most models do not incorporate rich communication, psychological motives, framing effects, or exogenous shocks beyond those explicitly encoded in the payoff matrices.

**6. Incomplete dimensional coverage:**  
- Several design features central to laboratory or field PGGs (e.g., chat, default framing, visibility of punishment identity) are rarely or never modeled as moderators of efficiency.

**7. Unaddressed second-order problems and anti-social punishment:**  
- Some models flag the instability of efficiency gains due to second-order free-riding, anti-social punishment, or unstable willingness to punish, often without offering robust solutions.

**8. Bi-stability and dependence on initial conditions:**  
- Some theoretical models predict both high- and low-efficiency equilibria (“bi-stability”) depending on initial composition or historical path, limiting predictability from design dimensions alone.

---

**In summary:**  
- Strong theoretical evidence supports that enabling well-designed punishment mechanisms in PGG-like environments generally increases efficiency versus no-punishment control, *especially when the control game is low-efficiency*, punishment costs are moderate/low, and the mechanism is well targeted/implemented.
- The marginal treatment effect is sensitive to design dimensions, most notably *player count, MPCR, punishment cost, enforcement structure (peer vs. institutional), and willingness to punish*.
- Prediction of absolute treatment efficiency should rely on explicit model-based sweeps for the parameter regime of interest; evidence is most robust for classical and spatial PGGs, less so for games with features not formally covered by the literature (chat, default framing, etc.).
- Use caution when inferring efficiency from behavioral outcomes, and recognize that generalizability may be limited by theoretical scope and the lack of empirical calibration.
