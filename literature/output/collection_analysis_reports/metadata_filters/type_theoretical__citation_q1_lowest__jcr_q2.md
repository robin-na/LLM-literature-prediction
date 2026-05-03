# 1) Evidence Base

The paper set comprises **82 papers**, overwhelmingly theoretical and modeling in nature, focusing on evolutionary dynamics, agent-based simulations, and analytical solutions. The majority are not laboratory or field experiments but theory papers, typically exploring mechanisms, stability conditions, and parameter influences in public-goods-game (PGG) and related social dilemma environments. The set is **broad in mechanism coverage** (public goods, punishment, reward, peer and institutional enforcement, network and spatial structure, evolutionary dynamics, repeated games, heterogeneity, aspiration, and more), but only a **subset directly addresses the core prediction task**: estimating the effect of enabling peer punishment on group efficiency in PGG-like designs.

The **evidence directly informing the core prediction task**—impact of peer punishment on efficiency/payoff in standard or spatial PGGs—is concentrated in a modest number of theory papers (e.g., Wu et al., 2014; Sun et al., 2025; Huang et al., 2024; Yang & Yang, 2024; Cui et al., 2022; Zhang et al., 2019; Sun et al., 2024; Gao & Liang, 2020; some adjacent papers). Much of the remainder provides **adjacent or mechanistic context**, often examining behavioral outcomes (cooperation rate, punisher prevalence, norm compliance) or studying non-PGG games (dyadic PDs, resource sharing, trust games, market dilemmas, regulatory models).

**Empirical coverage is limited**; most claims rest on theoretical or simulated outcomes, sometimes validated against behavior in related lab experiments reported elsewhere. As a result, the literature is **strong in offering qualitative and sometimes quantitative modeling predictions, but less so in direct empirical effect estimation for specific experimental designs.**

# 2) Task Relevance

**a. pgg_or_variant:**  
- **Exact relevance:** Approximately a dozen key papers study standard or spatial/voluntary PGGs (e.g., Wu et al., 2014; Sun et al., 2025; Huang et al., 2024; Yang & Yang, 2024; Cui et al., 2022; Zhang et al., 2019), directly aligning with the downstream task.
- **Close/adjacent:** Large numbers of papers focus on repeated PDs, resource sharing, helping games, trust games, or PGG variants, providing mechanism insights applicable to PGGs but sometimes with caution needed in mapping findings.
- **Weak/none:** Many papers (especially those with only PD or non-payoff behavioral outcomes) are only tangentially relevant.

**b. punishment_or_sanctions:**  
- **Exact relevance:** Papers addressing peer, institutional, or self-organized punishment in PGGs or close variants are present (e.g., Wu et al., 2014; Sun et al., 2025; Huang et al., 2024; Sun et al., 2024; Gao & Liang, 2020, etc.).
- **Adjacent/close:** Many studies examine punishment-like mechanisms (exclusion, partner switching, reputation loss, regulatory penalties) in adjacent game types or discuss punishment in a conceptual review/theoretical sense.
- **Weak/none:** Some work focuses on non-punishment mechanisms (rewards, confidence, influence, structural interventions, etc.).

**c. efficiency_or_related_payoff_outcome:**  
- **Exact/close:** Several core PGG punishment studies—mostly theory or simulation—report efficiency, group average payoff, welfare, or directly related outcomes as primary analysis targets (Wu et al., 2014; Sun et al., 2025; Gao & Liang, 2020, etc.). Others provide explicit payoff calculations as output of equilibrium or simulation.
- **Adjacent:** Many studies primarily report on cooperation rate, norm compliance, or strategy frequencies, which only indirectly relate to efficiency.
- **Weak/none:** Many studies offer no payoff or efficiency analysis.

**Summary:**  
The **most relevant papers for prediction** are **theory papers on PGGs with explicit, parametric analysis of peer punishment and group efficiency**. Empirical and experimental direct evidence is limited. Many adjacent papers offer supporting mechanistic or moderator insights, but findings from non-PGG or purely behavioral studies must be extrapolated with caution.

# 3) Outcomes Measured In The Literature

- **Payoff-based outcomes (directly relevant):**
  - *Efficiency/group efficiency*: The primary target—ratio of actual to maximum possible group payoff.
  - *Average/total group payoff*, *welfare*, *surplus*, *social utility*, or *earnings*—all closely related and often used interchangeably with “efficiency” in theory/simulation.
  - *Explicit equilibrium utilities*: Payoff formulas mapping design dimensions to outcomes in theoretical work.

- **Non-payoff behavioral outcomes (adjacent/indirect):**
  - *Contribution/cooperation rates*: Frequency of full or partial contribution, per-round or equilibrium.
  - *Punishment/reward frequency*: How often punishment or reward is assigned/distributed.
  - *Strategy distributions*: Prevalence of cooperators, defectors, punishers, justice strategists.
  - *Norm compliance*, *partner switching*, *retaliation dynamics*, *adaptive aspiration*.
  - *Structural outcomes*: Resource usage, network evolution, institutional emergence.

**Explicit distinction:**  
Only **a minority** of papers report **group efficiency or related payoffs as the main outcome**. Many focus on *cooperation rate or strategy frequency*, which may correlate with efficiency but are not equivalent and can mislead if interpreted as direct efficiency effects (e.g., punishment can raise cooperation but lower group efficiency due to high sanction costs, or vice versa).

# 4) Main Findings Relevant To Prediction

**Synthesis across literature with exact or close relevance:**

- **Enabling punishment (peer or institutional) in PGGs generally increases efficiency** compared to baseline (no-punishment) when:
  - **Punishment cost is low relative to its effectiveness** (Wu et al., 2014; Cui et al., 2022; Zhang et al., 2019; Heller & Sieberg, 2008; Gao & Liang, 2020).
  - **Synergy factor (MPCR/r) is low**, making the baseline efficiency poor; punishment can help move the group from low to high efficiency by deterring defectors (Wu et al., 2014; Sun et al., 2025).
  - **Punishment is targeted** (e.g., only the worst contributor is punished)—minimal yet effective punishment suffices to sustain full cooperation, maximizing efficiency with minimal cost (Huang et al., 2024).
  - **Network/spatial structure supports local clustering with shortcuts** (e.g., small-world structures), enabling punishment to efficiently suppress defectors and create stable high-cooperation configurations (Cui et al., 2022).
  - **Institutional design broadens coverage or uses tax funding** to finance punishment, further improving efficiency by removing second-order free-riding (Yang & Yang, 2024).

- **Key moderators of the efficiency effect of punishment:**  
  - **Punishment cost (CONFIG_punishmentCost):** Lower costs → greater efficiency gains; high costs can undo efficiency benefits (Wu et al., 2014; Zhang et al., 2019; Sun et al., 2024).
  - **Punishment effectiveness/tech (CONFIG_punishment_tech/Magnitude):** Higher impact per cost/effort increases efficiency benefit.
  - **MPCR/r (CONFIG_mpcr):** Lower values mean more potential for punishment to boost efficiency.
  - **Reward co-existence (CONFIG_rewardExists):** Combined reward & punishment or well-targeted reward can increase efficiency beyond punishment alone, and sometimes efficient reward can substitute for punishment (Sun et al., 2025; Yang & Yang, 2024; Gao & Liang, 2020; Huang et al., 2024).
  - **Player count (CONFIG_playerCount):** Cutoff thresholds for punishment effectiveness depend on group size and may require stronger punishment in larger groups (Huang et al., 2024).
  - **Cluster/network structure:** Spatial structure allows clusters of cooperators/punishers to resist invasion by defectors (Cui et al., 2022).
  - **Redistribution of fines:** Returning punishment fines to cooperators/punishers can help recoup efficiency losses caused by sanctioning costs, especially when punishment is expensive (Sun et al., 2024).

- **Threshold and non-monotonic effects:**
  - There may be **critical thresholds** for punishment cost, implementation strength, or group structure, below which punishment is ineffective and above which efficiency jumps sharply (phase transitions, bifurcations; Wu et al., 2014; Whitmeyer, 2004; Huang et al., 2024).
  - **Excessive punishment cost, poorly targeted punishment, or over-intervention can lower efficiency—non-monotonic or U-shaped effects** (Yang & Yang, 2024; Sun et al., 2024; Whitmeyer, 2004).
  - **Redistribution and targeting mitigate this risk**, allowing punishment to operate with minimal efficiency loss.

- **Special or limiting cases:**
  - **Dyadic/PD findings (adjacent):** In two-player settings or finite repeated games, punishment’s efficiency effect may be weaker or even negative if retaliation and cost feedback are high, especially in noisy environments (Rumble et al., 2022).
  - **Institutional punishment with path-dependency:** Effectiveness of punishment in increasing efficiency is sensitive to the initial number of cooperators and equilibria selection; punishment might stabilize either cooperation or defection (Whitmeyer, 2004; Dong et al., 2024).

- **Empirical limitations:**  
  - **Direct experimental/lab evidence is sparse**; the great majority of claims about efficiency effects are theoretical or simulated, not empirically measured in anonymous lab groups with strict payoff reporting.

# 5) Prediction Guidance

**How to use this literature for predicting the efficiency impact of enabling punishment:**

- **Direction of effect:** In standard and spatial PGGs with typical parameters, **enabling peer punishment is expected to increase group efficiency** relative to control (no-punishment), **conditional on punishment not being overly costly** and being at least sufficiently targeted/effective to meaningfully deter defection.
- **Effect moderators to prioritize in prediction:**
  - **CONFIG_punishmentCost:** Lower cost, greater efficiency gain. If cost is high, positive effects can vanish or reverse.
  - **CONFIG_mpcr/synergy_factor:** Lower control efficiency (due to low MPCR) implies greater potential for punishment to increase efficiency.
  - **CONFIG_punishment_tech/Magnitude:** Higher effectiveness per cost is beneficial; low impact limits the benefit.
  - **CONFIG_playerCount:** Larger groups require more stringent punishment to achieve the same efficiency gains.
  - **CONFIG_rewardExists and reward parameters:** Presence/effectiveness of reward can amplify or substitute for punishment effects.
  - **Network structure (contextually tied to player_count and group assignment):** Small-world or locally clustered networks enhance punishment efficacy relative to random mixing.
- **Thresholds/phase transitions:** There are **parameter thresholds** below which punishment is ineffective (no substantial efficiency gain) and above which efficient cooperation is stable and near-maximal (Wu et al., 2014; Huang et al., 2024).
- **Fine targeting:** Targeting only the worst contributor (rather than blanket punishment) increases efficiency for a given cost (Huang et al., 2024).
- **Redistribution of fines:** Returning fines to the group/other cooperators can salvage lost efficiency due to sanction costs (Sun et al., 2024).
- **Initial condition sensitivity:** Some models suggest strong **path dependence** or multiple possible equilibria—prediction should favor average-case outcomes based on typical random initializations unless initial group composition is known (Whitmeyer, 2004; Dong et al., 2024).
- **Cautions for adjacent evidence:** Where findings are from repeated PDs or adjacent games, efficiency effects may be smaller, less stable, or negative in dyads, especially when punishment cost is high or retaliation cycles are possible (Rumble et al., 2022).

**Summary formula:** “All else equal, introducing peer punishment with low enough cost and sufficient impact will increase group efficiency—especially in low-MPCR, low baseline-efficiency environments, and when group size is modest. The efficiency gain is suppressed or eliminated if punishment is too costly, poorly targeted, or benefits are not returned to the group. Structural factors (network, spatial mixing, institutional context) further moderate this effect.”

# 6) Design Dimensions Highlighted Across Papers

The **best-informed dimensions** (directly and repeatedly addressed, with modeled or explicit outcome implications):

- `player_count` (group size): Explicit in threshold formulas for sustainability of cooperation under punishment (Huang et al., 2024; Wu et al., 2014).
- `num_rounds`: Length of interaction moderates the sustainability and credibility of punishment (grim triggers, penance contracts, lasting effects; Wu et al., 2014; Matsushima, 2012; Camera & Gioffré, 2025).
- `mpcr` (synergy/multiplier): Strongly and consistently mapped to the payoff-enhancing effect of punishment; central in nearly all core theory papers.
- `all_or_nothing`: Many models use both binary and continuous contribution structures, with generally similar qualitative findings.
- `punishment_cost` and (`punishment_tech`/`punishmentMagnitude`): The **most critical moderators** of the efficiency effect of punishment.
- `reward_exists`/`reward_cost`/`reward_tech`: Addressed in several theory papers, either as co-treatments or comparative mechanisms.
- `show_n_rounds`: Sometimes included in repeated game models to affect equilibrium selection and timing-triggered punishments.

**Indirectly or contextually discussed:**

- `chat`: Rarely or only contextually examined; communication is assumed absent or local in most simulation/theory models but could affect coordination on punishment.
- `show_other_summaries`, `show_punishment_id`: Contextual, especially in repeated/partner-changing games—identification moderates effectiveness in sustaining cooperation, but not universally modeled or quantified.
- `default_contrib`: Occasionally discussed in framing and opt-in/opt-out behavior, often not separately parameterized.
- `reward_exists`, `reward_cost`, `reward_tech`: When addressed, usually as secondary parameters, with core results for pure punishment or combined systems.
- `show_n_rounds` and `num_rounds`: Underlie repeated/finite game models but are often treated as exogenous or infinite horizon for theory.

**Dimensions effectively missing or only lightly touched:**

- `chat`, `default_contrib`, `show_other_summaries`, `show_punishment_id`: Seldom the focus of theoretical results.
- Realistic implementation details (NUDGE, interface design, group assignment protocols) are rarely specified.

# 7) Important Limitations

- **Empirical data sparse:** Most direct claims are from theory/simulation—meaning actual effect sizes or precise quantitative predictions should be interpreted as model-based, not measured.
- **Parameter regime caveats:** Many theoretical claims rely on being “above threshold” for punishment cost/effectiveness or “below threshold” for group size, temptation, or heterogeneity; **results may not generalize to all parameter combinations**.
- **Mapping from cooperation rate to efficiency is not always monotonic:** High cooperation does not guarantee high efficiency if punishment is too costly.
- **Equilibrium multiplicity and path dependence:** Some environments are sensitive to initial group composition or stochastic shocks; average-case predictions may not hold in small samples or highly unstable environments.
- **Adjacent evidence extrapolation:** The payoff-benefit of punishment in adjacent games (PDs, trust games) may not translate directly to standard PGGs—care is needed when applying adjacent results.
- **Missing design dimensions:** Some game configuration variables (chat, identification, summary provision, default contributions) are under-explored, limiting ability to finely predict their influence on efficiency.
- **Punishment design granularity:** Many studies model abstract “punishment” or general cost/fine, whereas practical implementations may vary (public vs. private, fixed vs. variable fine, immediate vs. delayed, targeted vs. blanket).
- **Network structure over-/under-emphasized:** Spatial and small-world network results may not generalize to well-mixed or randomly assigned PGGs without spatial structure.
- **Lack of experimental variability:** Most theory papers assume homogeneous, rational (or evolutionary) agents; real human groups may diverge due to cognitive constraints, error, or social preference heterogeneity.

---

**In summary:**  
The theoretical literature provides **strong, explicit support** for the expectation that enabling peer punishment will increase efficiency in most PGGs compared to no-punishment baselines, **especially when punishment cost is low and MPCR is not too high**. The effect is **parametrically sensitive to punishment cost/effectiveness, group size, synergy factor, and targeting**. Results are **robust across a range of models and game structures**, but **empirical calibration of effect magnitude is missing**, and the influence of several practical design dimensions is **understudied**. **Ambiguity exists in adjacent/PD literature, especially about retaliation, cost, and the risk of efficiency loss when punishment is misapplied.**
