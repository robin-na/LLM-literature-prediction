# 1) Evidence Base

The paper set consists of 307 papers, overwhelmingly composed of **theoretical models and simulations**. There is minimal to no empirical or experimental laboratory data directly measuring efficiency effects of punishment in PGGs, but an exceptionally extensive and diverse theoretical literature covers a vast range of PGG variants, punishment systems, and related social dilemmas (including resource games, trust games, collective-risk games, and adjacent frameworks).

The coverage of **public goods game (PGG)** and its close variants is **broad and deep**, spanning classic PGGs, spatial/networked variants, threshold PGGs, resource feedback games, and dynamic participation models. The treatment of **punishment and sanctioning** is likewise expansive, encompassing peer punishment, pool/institutional punishment, exclusion, reward systems, hybrid and adaptive protocols, and many edge-case and mechanism-focused punishment designs.

**Payoff-related outcomes**—especially group efficiency, welfare, and total payoff—are **less frequently the primary focus** compared to behavioral outcomes like cooperation or contribution rates, but a substantial subset of theory and simulation papers report average/group payoff or efficiency directly, and many offer analytical or computational mappings from strategy frequencies to expected payoffs.

# 2) Task Relevance

### (a) `pgg_or_variant`
- **Exact**: The majority of the core papers directly address classic or spatial PGGs, often with exact mapping to the downstream setting (continuous or all-or-nothing contributions, defined group size, repeated rounds).
- **Close**: A substantial number of highly relevant papers report on common-pool resource games, collective-risk dilemmas, iterated trust/donation games, or other multi-player social dilemmas that preserve the underlying structure and dilemma of the PGG.
- **Adjacent/Weak/None**: There is a long tail of papers on dyadic games (e.g., Prisoner’s Dilemma), ultimatum games, or other adjacent models, which are only partially informative for the specific PGG prediction task.

### (b) `punishment_or_sanctions`
- **Exact**: Many core theory papers manipulate punishment (peer or institutional), its cost, magnitude, and related mechanisms.
- **Close**: Exclusion mechanisms, risk-insurance analogs, access restrictions, or reward systems are analyzed as complements/substitutes for punishment.
- **Adjacent**: Adaptive strategies, tag-based ostracism, partner choice, and endogenous feedback are discussed as punishment-like or discipline mechanisms.
- **Weak/None**: Some works focus on non-punitive mechanisms for promoting cooperation and are contextually relevant primarily for baseline or comparative insights.

### (c) `efficiency_or_related_payoff_outcome`
- **Exact**: Numerous theoretical works analyze average group payoff, efficiency (as a fraction of the fully cooperative optimum), welfare, or surplus explicitly.
- **Close/Adjacent**: Some focus on group achievement, resource levels, or proxy metrics for welfare.
- **Weak/None**: The bulk of the literature uses behavioral measures (contribution rate, frequency of cooperation) and is less directly informative for efficiency prediction.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (Relevant for Prediction):**
  - **Efficiency:** Defined as group payoff/maximum possible (full cooperation in all rounds), directly reported or analytically derived in a significant subset.
  - **Group/average payoff / total wealth / welfare / resource levels**: Frequently given in common-pool and resource game variants, often as explicit functions of design parameters and strategy frequencies.
  - **Surplus/profit/social welfare**: Addressed in economic extensions (e.g., marketing cooperatives, team production, fisheries, public resource settings).
- **Non-payoff behavioral outcomes (Less relevant for direct predictive modeling):**
  - **Contribution/cooperation rate:** Ubiquitously reported, often used to infer (but not directly measure) group efficiency.
  - **Prevalence/frequency of strategy types (defectors, punishers, excluders):** Used as markers of dynamical phase/state.
  - **Stability, cyclic dominance, coexistence, norm prevalence:** Mechanism-focused or evolutionary outcome variables.

# 4) Main Findings Relevant To Prediction

### Empirical findings vs. theoretical arguments
- **Almost all findings are theoretical/simulation-based.** Generalizability beyond the model assumptions requires judicious interpretation, especially for laboratory or field settings.

### Substantive synthesized findings
- **Punishment can increase group efficiency, but only within parameter regimes where its cost and effectiveness are properly calibrated** (e.g., low or moderate punishment cost, sufficiently high impact/fine, no excessive antisocial punishment). For PGGs with very high punishment cost or ineffective punishment, efficiency gains are attenuated or even reversed (Perc et al., 2017; Szolnoki & Perc, 2013).
- **Spatial/network structure strongly amplifies the effectiveness of punishment relative to well-mixed populations** (Szolnoki & Perc, 2017; Wang et al., 2015). Clustering effects allow cooperation and punishment to reinforce each other and overcome second-order free-riding.
- **Institutional/pool punishment and exclusion are generally more robust than peer punishment**, especially in the presence of antisocial punishment, corruption, or strategy-specific vulnerabilities (Liu & Chen, 2019; Li et al., 2015).
- **Control game efficiency (i.e., efficiency with punishment disabled) is a crucial baseline:** The marginal effect of punishment is greatest when control efficiency is low (cooperation is rare), and punishment can generate large efficiency gains. If the control system is already highly cooperative/efficient (e.g., due to other mechanisms or high MPCR), adding punishment yields limited or negligible efficiency improvements, and can sometimes reduce efficiency due to its direct cost (Gao et al., 2020; Szolnoki & Chen, 2018).
- **Thresholds and non-monotonicity:** There are critical thresholds for group size, MPCR (synergy factor), punishment cost, and punishment intensity above or below which punishment becomes effective or counterproductive (Li et al., 2022; Gao et al., 2020; Nuño et al., 2010).
- **Reward vs. punishment:** Reward (possibly combined with punishment) can sometimes match or outperform punishment for increasing efficiency, but in most models, punishment is more robust or cost-effective except when reward implementation is highly favorable and free-riding is suppressed (Sun et al., 2023; Okada et al., 2015; Wang et al., 2022).
- **Complex/adjacent factors (partner choice, reputation, voluntary participation, corruption):** These can independently increase cooperation and efficiency and often interact with punishment’s effectiveness, especially through mechanisms like reputation-based exclusion, monitoring, and conditional cooperation (Wang et al., 2015; Liu et al., 2022).

# 5) Prediction Guidance

### Direct implications for the downstream prediction task:

- **Baseline control efficiency is important**: In games where the control has high efficiency (many cooperators), the effect of enabling punishment may be small, neutral, or slightly negative (due to punishment costs). The largest efficiency boosts from punishment arise when the control is inefficient (cooperation is low).
- **Key design dimensions with strong direct evidence**:
  - **`player_count`**: Moderate group sizes tend to facilitate the effectiveness of punishment; very large groups may dilute punishment’s deterrence unless institutional mechanisms are used (Wang et al., 2015; Perc et al., 2017).
  - **`mpcr`**: There is a sharp increase in efficiency once the synergy factor passes a threshold that enables cluster formation and makes punishment viable (Li et al., 2022; Perc et al., 2017).
  - **`punishment_cost` and `punishment_tech/magnitude`**: The effectiveness of punishment is non-monotonic—punishment must be strong enough to deter defection, but not so costly as to undermine efficiency (Szolnoki & Perc, 2013; Nuño et al., 2010; Luo & Zhao, 2013).
  - **`punishment_tech` (type: peer vs. institutional, exclusion, adaptive protocols, probabilistic assignment, etc.)**: Institutional and exclusion mechanisms are more robust and less susceptible to antisocial punishment and corruption (Liu & Chen, 2019; Wang & Perc, 2022).
  - **`all_or_nothing`**: Effect sizes and model behavior often differ between continuous-contribution and binary (all-or-nothing) PGGs; most findings are valid for both but should be parameter-matched.
  - **`num_rounds`**: Infinite or long repeated games or evolutionary settings generally favor higher efficiency under punishment, especially with reputation and partner stability. For short/few rounds, punishment may have little time to act unless coordination and learning are rapid (ABREU et al., 1991).
  - **Secondary or contextually informed dimensions**: `reward_exists`, `reward_cost`, `reward_tech` (for hybrid or reward–only protocols), and visibility/information (`show_n_rounds`, `show_other_summaries`, `show_punishment_id`) are important moderators but only partially parameterized by current literature.

- **Other dimensions (chat, default_contrib, show_punishment_id)**: These have little direct coverage; communication is widely inferred to increase punishment effectiveness but is not systematically modeled for efficiency (Song et al., 2020).

- **Nonlinearities and boundary effects**: The effect of enabling punishment is often highly nonlinear—there exist regions of parameter space where even small increases in fine, reductions in cost, or small changes in group size can sharply transition the system from inefficient to highly efficient equilibrium (Li et al., 2022; Perc et al., 2017).

- **Adjacency and potential for reverse effects**: In certain variants (e.g., cyclic games, anti-social punishment, high corruption, excessive punishment severity), enabling punishment can backfire and reduce efficiency below the control game (Griffin & Belmonte, 2017; Vukov et al., 2013; McBride et al., 2016).

### Empirical use: For new game designs, **the best available approach is to map game parameters (especially group size, MPCR, punishment cost/effect, and the control efficiency) to the relevant theoretical model**, using the published equations or phase diagrams to forecast treatment efficiency. If the game is close to standard PGG or a well-analyzed variant, quantitative prediction of efficiency with enabled punishment is possible, but predictions are less certain for designs with novel dimensions or outside the covered parameter regions.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed (strong evidence and explicit mapping):**
- `player_count`
- `num_rounds`
- `all_or_nothing`
- `mpcr`
- `punishment_cost`
- `punishment_tech` (peer vs. institutional exclusion/punishment, probabilistic/deterministic, hybrid, etc.)
- `reward_exists`, `reward_cost`, `reward_tech` (for comparative/combined treatments)
  
**Indirectly informed or contextually mapped:**
- `show_n_rounds` (sometimes manipulated in repeated/confidential settings)
- `show_other_summaries` (`show_punishment_id`): often discussed in the context of monitoring, reputation, or social norm enforcement, but not as direct predictors in most models.
- `default_contrib` (framing): scant direct evidence, but some studies suggest minor framing/moderation effects.
- `chat` (communication/ coordination): frequently discussed as increasing punishment effectiveness but not directly modeled in group efficiency terms.

**Sparse, peripheral, or missing in the literature:**
- Effects of `chat`, contribution framing (`default_contrib`), and transparency (`show_punishment_id`) on payoff-based efficiency are not systematically modeled.
- Interaction of multiple visibility/manipulation features (e.g., how simultaneous changes to summaries, identities, and communication moderate punishment effects) is generally not analyzed with respect to efficiency.
- Complex cross-effects between these dimensions and exogenous features like environmental/resource feedback, dynamic participation, or multi-layered/grouped games are not comprehensively parameterized for efficiency.

# 7) Important Limitations

- **Empirical evidence is limited**: Most findings are based on mathematical modeling and simulations, not laboratory or field experiments. This limits the direct external validity for real-world prediction.
- **Efficiency outcomes are less frequently the primary outcome** than behavioral measures, especially in recent simulation literature (where cooperation rates dominate reporting).
- **Complex interactions and moderators** (such as the effect of communication, reputation, institutional structure, or corruption) are often considered in isolation or in simplified form, making it difficult to model all relevant 14 prediction dimensions jointly.
- **Non-monotonic and sometimes ambiguous directional effects** mean that enabling punishment can reduce efficiency in some designs—especially at high cost, in the presence of antisocial punishment, or when overused (Griffin & Belmonte, 2017; Perc et al., 2017; Vukov et al., 2013; Nuño et al., 2010).
- **Scarce direct evidence on less-standard dimensions** (`chat`, `default_contrib`, certain forms of visibility/transparency, and hybrid or dynamically adaptive punishment/reward technologies).
- **Exclusion, hybrid, and adjacent mechanisms** are sometimes more effective than standard punishment, but their effects are not always analytically mapped to efficiency outcomes in a way directly usable for prediction.
- **Reported payoffs often assume well-mixed infinite populations and/or specific updating rules**, which may not generalize to finite, experimental, or structured settings.

---

**In summary**, the literature provides robust theoretical evidence that punishment, when effectively and affordably deployed, generally increases efficiency relative to a no-punishment control in PGG-like environments—*but* the effect is highly sensitive to game design features (especially group size, punishment cost/intensity, MPCR, and underlying baseline efficiency). Non-payoff measures dominate reporting, so careful mapping to efficiency is necessary, especially as some settings produce negative or null treatment effects. Adjacent behavioral mechanisms (partner choice, exclusion, reputation, voluntary participation) are frequently shown to rival or exceed classic punishment in promoting efficiency, but their effects are less well parameterized for joint prediction with classic PGG punishment dimensions. The absence of robust empirical data and the prevalence of non-payoff outcome measures are key limitations for precise, quantitative efficiency forecasting in novel game designs.
