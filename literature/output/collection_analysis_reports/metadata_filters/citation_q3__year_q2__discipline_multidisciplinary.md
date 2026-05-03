# 1) Evidence Base

The paper set comprises 57 sources, including both empirical (primarily laboratory experiments) and theoretical (mathematical and simulation modeling) studies. The selection is relatively broad in the context of general economic game research but narrows appropriately for the prediction task, with a substantial subset addressing either Public Goods Games (PGG) directly or closely related multiplayer social dilemmas (e.g., Snowdrift, Prisoner's Dilemma with punishment). Empirical findings typically report on behavioral, payoff, or efficiency outcomes in controlled lab or simulation environments. Theoretical papers provide mechanism arguments, evolutionarily stable strategy analyses, and parameter sweeps to predict or explain observed patterns. There are relatively few field or naturalistic studies.

Importantly for the prediction task, a core set of papers (e.g., Simpson et al., 2017; Chaudhuri & Paichayontvijit, 2017; Ozono et al., 2017; Dong et al., 2016) provide experimental data on efficiency in PGGs with and without punishment, while others extend these findings to nuanced contexts (e.g., punishment technology, leader punishment, resource abundance, or population structure). Some adjacent studies focus primarily on behavioral change, strategy evolution, or the motivational psychology of punishment, emphasizing the need to distinguish these outcomes from direct measures of efficiency.

# 2) Task Relevance

**pgg_or_variant**:
- *Exact relevance*: Many papers are on standard PGGs or direct close variants (Ozono et al., Dong et al., Simpson et al., Hetzer & Sornette, Chaudhuri & Paichayontvijit, etc.).
- *Close/adjacent*: Some papers use Snowdrift games or iterated PDs with punishment, or PGGs with structural modifications.
- *Weak/none*: Several papers focus solely on adjacent game structures or different types of economic games.

**punishment_or_sanctions**:
- *Exact relevance*: Core papers manipulate the punishment dimension explicitly—enabling/disabling peer punishment (Simpson et al., Ozono et al., Chaudhuri & Paichayontvijit).
- *Close*: Variants include institutional punishment, ostracism, or probabilistic/adaptive mechanisms (Hetzer & Sornette; Nakamaru & Yokoyama).
- *Adjacent/weak*: Some only tangentially address punishment, e.g., via social image or indirect norm enforcement.

**efficiency_or_related_payoff_outcome**:
- *Exact*: Several central studies measure efficiency/group payoff directly (Simpson et al., Ozono et al., Chaudhuri & Paichayontvijit, Dong et al., Grimalda et al., Ozono et al. (2016), Hetzer & Sornette (theoretical)). 
- *Close/adjacent*: Many others report on contribution rates/behavioral outcomes, with efficiency inferred but not measured.
- *Weak/none*: Some papers exclusively assess non-payoff behavioral or process outcomes.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (directly relevant):**  
  - *Efficiency*: Explicitly defined as group total payoff relative to the fully cooperative benchmark (Simpson et al., Ozono et al., Chaudhuri & Paichayontvijit, Dong et al.).
  - *Group profit/earnings/welfare*: As reported in experiments and simulations (Dong et al., Hetzer & Sornette, Ozono et al. (2016), Grimalda et al.).
  - *Surplus, total public good produced*: Proxy for efficiency in some studies.

- **Non-payoff behavioral outcomes (adjacent or indirect):**
  - *Contribution rates, cooperation rates*
  - *Punishment frequency/amount assigned, norm compliance*
  - *Strategy adoption, equilibrium selection*
  - *Retaliation, trust, motivational shifts*

Several studies blur the line by reporting both: efficiency alongside behavioral responses (e.g., Simpson et al., Chaudhuri & Paichayontvijit). However, many only infer potential efficiency improvement/loss from indirect effects (behavioral change), which must be distinguished from actual measured efficiency.

# 4) Main Findings Relevant To Prediction

**Empirical findings on PGGs:**
- Costly peer punishment increases contribution/cooperation rates over control but often does *not* increase average efficiency; the economic cost of imposing or receiving punishment can cancel out the gains from higher cooperation. This is robust in typical lab PGGs: Simpson et al. (2017) found that material punishment raised contributions but failed to improve group earnings relative to control—a result echoed in Ozono et al. (2017), where increased cooperation from complex punishment systems came at a high (efficiency-reducing) cost.
- Non-material (costless) sanctions, such as approval/disapproval, often outperform material punishment by increasing both cooperation and efficiency, as their deterrent effect comes with no cost (Simpson et al., 2017).
- Punishment’s impact on efficiency is sensitive to its *cost-to-effectiveness ratio (punishment tech)*. If punishment is cheap and effective enough, or group structure supports efficient use (e.g., leader-based or coordinated punishment), efficiency gains are possible (Chaudhuri & Paichayontvijit, 2017; Ozono et al. (2016)).
- *Time horizon (num_rounds)* and *matching protocol* matter: The efficiency effect of punishment tends to improve over repeated games and with fixed (partner) matching, as learning establishes cooperation and punishment is less wastefully applied (Chaudhuri & Paichayontvijit, 2017).
- Where the baseline (control) game already produces high efficiency, strong punishment can decrease efficiency due to unnecessary costs and retaliation cycles (Jiang et al., 2013; Grimalda et al., 2016).
- Institutional details—such as punishment resource abundance, prioritization of second-order punishment, leader support systems—moderate the net efficiency effects (Ozono et al. (2017, 2016)).

**Theoretical/mechanism arguments:**
- Evolutionary models agree that, under certain preference structures (e.g., disadvantageous inequity aversion), punishment can stabilize high-cooperation equilibria and enhance group fitness (Hetzer & Sornette, 2013).
- Models that allow for flexible, context-sensitive punishment (e.g., probablistic, payoff-difference-based) can yield higher efficiency than rigid, always-on punishment (Ohdaira, 2016).
- The possibility of retaliatory cycles, norm path-dependence, and anti-social punishment may sometimes render punishment inefficient (Simpson et al., 2017; Helbing et al., 2014).

**Efficiency increases are likelier:**
- When punishment is *non-costly* or *cost-effective* and deters defection without excessive waste.
- When game structure (e.g., long num_rounds, fixed groups) supports stable cooperation with reduced punishment use over time.
- When initial efficiency is very low (cooperation is rare), making the gains from inducing contributions larger than the costs (Jiang et al., 2013; Dong et al., 2016).

**Efficiency decreases are likelier:**
- When punishment is *costly* and overtakes gains from improved cooperation (Simpson et al., 2017; Grimalda et al., 2016).
- In short games or settings with random re-matching, where the threat of punishment is continually re-imposed (Chaudhuri & Paichayontvijit, 2017).
- When anti-social or retaliatory punishment is prevalent.

# 5) Prediction Guidance

Given a PGG-like design and observed control efficiency, the literature suggests:

- **Costly peer punishment** should generally *not* be expected to increase average efficiency above control in standard PGGs unless the punishment is highly cost-effective, the game is long, and/or group structure supports efficient signaling and learning. Prediction models should, therefore, adjust the treatment efficiency estimate upwards mainly when these favorable conditions are present (Simpson et al., 2017; Ozono et al., 2017; Chaudhuri & Paichayontvijit, 2017).

- The **effect of punishment is strongly moderated** by the control efficiency:  
  - **Low control efficiency/rare cooperation**: Punishment (especially if strong and well-designed) can raise efficiency, as the room for cooperative gains outweighs punishment costs (Jiang et al., 2013; Dong et al., 2016).
  - **High control efficiency/likely cooperation**: Adding strong punishment may reduce efficiency due to unnecessary sanctioning and potential retaliation (Jiang et al., 2013; Grimalda et al., 2016).

- **Punishment technology and cost (punishment_cost, punishment_tech)** are critical: Punishment must be effective enough to deter free-riding, but not so costly that any net gains are swamped. Prediction models should weigh these parameters heavily.

- **Game duration (num_rounds)** and **matching protocol** affect punishment's impact: Longer, fixed-group games allow sanctioning to serve as a credible threat with lower waste, supporting higher long-run efficiency (Chaudhuri & Paichayontvijit, 2017).

- Features such as **costless, non-material punishment** (approval/disapproval) or **well-designed institutional punishment** (leader, pool, or hybrid systems) can sometimes deliver both higher cooperation and efficiency (Simpson et al., 2017; Ozono et al., 2016), whereas peer punishment may not.

- **Retaliation potential, anti-social punishment, and group composition** (e.g., trust, propensity to punish) also act as moderators: high anti-social punishment or low trust can diminish or reverse any efficiency gains.

Overall:  
- For most standard lab PGGs, **enabling costly peer punishment produces null or slightly negative effects on efficiency, unless control efficiency is low, punishment is cost-effective, and the game structure supports learning**.
- **Non-material or institutional punishment mechanisms may outperform costly peer punishment** in both cooperation and efficiency.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed design dimensions:**  
- `player_count`: Most core studies report group size, typically n=4 or n=5 (Simpson et al., 2017; Ozono et al., Chaudhuri & Paichayontvijit).
- `num_rounds`: Varies across studies, with evidence on the effect of repeated interaction.
- `mpcr`: Directly manipulated in most experiments.
- `all_or_nothing`: Both continuous and binary contributions covered.
- `punishment_cost` & `punishment_tech`: Central in the majority of empirical and theoretical papers; manipulated in cost-to-effectiveness ratio and intensity.
- `chat`: Explicitly absent in most controlled experiments.  
- `punishmentExists/punishment_enabled` (treatment): The main manipulation in several key studies.

**Indirectly informed or contextually discussed:**  
- `default_contrib`, `show_n_rounds`, `show_other_summaries`, `show_punishment_id` (e.g., whether players know identities or overall game structure) are mentioned in a few studies, generally as controls or background conditions (Simpson et al., Stewart et al.).
- `reward_exists`, `reward_cost`, `reward_tech`: Some studies include reward-only or combined reward/punishment arms (Dong et al., Gao et al.), offering indirect evidence.
- `punishment_magnitude`: Sometimes reported as part of punishment technology.

**Effectively missing/sparse coverage:**  
- Dimensions related to **surface UI/feedback structure** (`show_punishment_id`, `show_other_summaries`), **chat**, and **default contribution framing** are only rarely manipulated explicitly, and evidence is indirect or context-dependent.

# 7) Important Limitations

- **Scope of punishment mechanisms**: Most empirical evidence is on *costly peer punishment*. Other forms (e.g., costless social sanction, institutional/leader punishment, ostracism) are less frequently investigated, and their effects may differ substantially.
- **Parameter coverage and external validity**: Many experiments rely on small groups, laboratory settings, short game durations, and simple designs; generalizability to larger, real-world groups, networks, or field conditions is limited.
- **Relative sparsity on some dimensions**: Little systematic evidence for the effects of chat, information feedback features, or finer points of reward systems, which may moderate the effect of punishment.
- **Behavioral (not payoff) emphasis in some theoretical work**: A significant share of the theoretical evidence is about cooperation/contribution rates, which often—but not always—tracks efficiency, but can diverge where punishment costs are high.
- **Ambiguity and mixed findings**: There are clear cases (e.g., Simpson et al., 2017; Grimalda et al., 2016) where punishment increases cooperation but *reduces* or does not improve efficiency, and others where gains depend on design or control condition. This heterogeneity should inform prediction uncertainty.
- **Missing contexts**: Dynamic, networked, or heterogeneous populations, and naturalistic/field contexts, are not well covered. Also, there is little evidence on long-term effects after the game ends.
- **Potential publication bias**: More dramatic punishment effects (positive or negative) may be overrepresented.

---

**In sum:**  
This paper set provides a strong empirical and theoretical foundation for predicting the effect of enabling costly peer punishment on efficiency in standard lab PGGs, with nuanced findings about conditions for gains and losses. However, caution is warranted when generalizing to other forms of punishment, complex environments, or under-explored design dimensions. For most typical lab PGGs, the expectation should be that enabling costly peer punishment does not increase efficiency unless specific design conditions are met (favorable punishment technology, low baseline efficiency, long time horizons, efficient implementation). Non-material sanctioning or cost-effective institutional mechanisms offer more promise for boosting both cooperation and efficiency.
