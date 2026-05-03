# 1) Evidence Base

This literature set consists almost entirely of theoretical and simulation-based studies (no direct empirical or experimental measurement of payoffs or efficiency with punishment in public goods games is included, except for a few key adjacent experimental studies). The focus of the set is narrow, with a heavy emphasis on **public goods games (PGGs)** and close variants, and most papers directly engage with **punishment or sanctioning mechanisms** as a treatment dimension. The main outcomes of interest are **group efficiency**, **total payoff**, or other payoff-based metrics, though a significant number of studies instead report **cooperation rates**, **strategy abundances**, or norm compliance as primary outcomes. There are also adjacent studies investigating **exclusion, reputation, ostracism, and network adaptation**, and a limited set of empirical (experimental) papers that mostly address behavioral rather than efficiency outcomes. Overall, the evidence base is strong theoretically and is especially rich for spatial, networked, or agent-based PGG models with well-specified sanctions, but sparse for direct, empirical quantification of efficiency changes due to punishment in real or laboratory PGG environments.

# 2) Task Relevance

**PGG or Variant**: `exact`
- The bulk of the literature directly studies public goods games or mathematically equivalent structural variants (e.g., threshold games, common-pool resource games).
- Some adjacent or weakly relevant studies model Prisoner's Dilemmas, trust games, or market games.

**Punishment or Sanctions**: `exact`
- Most of the central papers directly model **peer or pool punishment**, as well as exclusion, with well-specified cost, effectiveness, and sometimes mechanisms for antisocial or conditional punishment.
- A few studies analyze reward-only mechanisms (`weak/none` relevance for punishment).

**Efficiency or Related Payoff Outcome**: `exact`, with moderate presence of `close` or `adjacent`
- A large proportion of studies directly model or report **efficiency, total payoff, or group welfare**, though a notable subset reports only on cooperation rate or related behavioral outcomes—marked as `adjacent`.
- The mapping from behavior to efficiency is sometimes explicit and sometimes inferred.

# 3) Outcomes Measured In The Literature

- **Payoff-related (efficiency, group payoff, welfare, surplus):**
  - Most theory papers specify or explicitly track average group payoff, evolutionary fitness, or efficiency ratio (e.g., Perc et al., 2017; Szolnoki & Perc, 2013; Adami et al., 2016; Liu et al., 2018).
  - Several studies provide phase diagrams of efficiency as a function of punishment cost, MPCR, and other dimensions.
  - Some papers report only on **achievement rate** (fraction of successful groups), which is a close proxy for efficiency in threshold PGGs (Pacheco et al., 2014).

- **Non-payoff behavioral (contribution/cooperation rate, norm compliance, punishment frequency):**
  - Many papers focus on steady-state fractions of cooperators, punishers, and defectors or on extinction probabilities (Yang & Rong, 2015; Liu et al., 2019; Quan et al., 2019).
  - Experimental papers often report **punishment assignment patterns** or **punishment motivations**, not efficiency (Falk et al., 2005; Goette et al., 2012).

**Key distinction:**  
Not all increases in cooperation rate translate straightforwardly into higher efficiency, due to the costliness of punishment and the possibility of antisocial or wasteful punishment.

# 4) Main Findings Relevant To Prediction

### Cross-Paper Synthesis

- **Punishment generally increases efficiency** in PGGs, especially in spatial/networked or agent-based models, provided that:
    - The **cost of punishment is not prohibitively high**,
    - **Punishment is sufficiently effective** (high fine/severity, high detection/impact),
    - The **MPCR/synergy parameter** is moderate or high,
    - **Antisocial punishment** or corruption is limited or compensated by population structure (Szolnoki & Perc, 2013, 2017; Lee et al., 2022; Perc et al., 2017; Adami et al., 2016; Liu et al., 2019).
- **Structure matters**:
    - **Spatial/networked (local interaction) games** can sustain efficiency boosts from punishment even when well-mixed games cannot, due to clustering of cooperators and punishers (Szolnoki & Perc, 2013; Helbing et al., 2010).
    - **Partner selection/ostracism** and **network adaptation** can have even stronger effects on efficiency than explicit costly punishment (Zimmermann & Eguíluz, 2005).
- **Cost of punishment and effectiveness are critical moderators:**  
   - There is often an **optimal punishment cost level** maximizing efficiency; too weak punishments are ineffective, too costly ones reduce efficiency by draining group resources (Lee et al., 2022; Adami et al., 2016; Liu et al., 2018).
   - **Antisocial punishment, corruption, or mis-targeted punishment** can negate or reverse efficiency gains (Goette et al., 2012; Liu et al., 2019).
- **Additional features:**
    - Adding rewards in addition to punishment does **not generally increase efficiency further**, except in low-cost, low-MPCR environments (Szolnoki & Perc, 2013).
    - Flexible sanctioning (switching between punishment and exclusion) can enhance efficiency, especially under intermediate conditions (Liu et al., 2018).
    - **Imperfect/infrequent monitoring or information** can sharply limit the ability of punishment to improve efficiency (Abreu et al., 1991; Ohtsuki et al., 2015).
    - **Ecological context/resource renewal** interacts with punishment—if resources cannot recover, efficiency may not improve even with perfect punishment (Chen & Szolnoki, 2018).

### Disagreements and Ambiguity

- **Context-dependent negative effects**:  
  Some settings with high punishment cost, high levels of antisocial punishment, or strong intergroup competition see decreased or unchanged efficiency (Perc et al., 2017; Goette et al., 2012).
- **Empirical gaps**:  
  Theoretical predictions are not always matched with experimental confirmation on efficiency outcomes.

# 5) Prediction Guidance

- **Punishment should be expected to increase efficiency** relative to control (no-punishment) only if the game design features **moderate-to-low punishment cost, sufficient effectiveness**, and lacks institutionalized antisocial punishment or easy opportunities for corruption.
- **Phase diagrams and model formulas** from theory papers can be mapped to specific design parameters (player count, MPCR, punishment cost/severity) to estimate expected efficiency shifts. Use control efficiency as a baseline and adjust according to:
    - **If punishment parameters are in the 'favorable' region** (moderate cost, high impact), **predict a positive efficiency shift**.
    - **If punishment is too costly, ineffective, or mis-targeted (e.g., antisocial/competitively motivated)**, **predict minimal to negative effect**.
- **For networked or spatially-structured populations**, expect a stronger and more robust efficiency gain from punishment, particularly at intermediate MPCR and group sizes (Szolnoki & Perc, 2013; Helbing et al., 2010).
- **Flexible, context-sensitive sanctioning mechanisms** (e.g., switching between punishment and exclusion) may yield higher efficiency than pure punishment or exclusion across parameter spaces (Liu et al., 2018).
- **Information structure and observability** are critical: if monitoring or punishment targets are poorly specified, efficiency gains are sharply limited (Abreu et al., 1991).

# 6) Design Dimensions Highlighted Across Papers

- **Directly Informed:**
    - `player_count` (group size): most theory papers vary this and often hold at 5 (spatial/networked models).
    - `mpcr` (synergy/multiplier): varied and found to interact strongly with punishment effect.
    - `punishment_cost`, `punishment_tech` (cost/impact and mechanism): usually explicitly parameterized and analyzed (key moderators).
    - `all_or_nothing` (contribution framing): varies across models; generally considered.
    - `num_rounds` (repetition): sometimes modeled as infinite/ongoing, sometimes finite.
    - `reward_exists` (reward vs punishment): several papers model both, finding limited marginal benefit from reward when punishment is present.
- **Indirectly Informed/Contextual:**
    - `chat`, `show_other_summaries`, `show_punishment_id`: information and communication are rarely modeled directly, but the importance of information structure or monitoring is emphasized (Abreu et al., 1991; Ohtsuki et al., 2015).
    - `default_contrib`: (opt-in/opt-out framing) rarely addressed.
    - `punishment_tech`: sometimes mapped to pool vs peer punishment, exclusion, or ostracism.
    - `reward_cost`, `reward_tech`: discussed where reward mechanisms are compared to punishment.
    - `show_n_rounds`: seldom discussed, though related to end-game effects.
- **Effectively Missing:**
    - Empirical variation in `chat`, `show_other_summaries`, `show_punishment_id`, and technology/framing manipulations.
    - Direct experimental measurement of these dimensions in PGG with efficiency as outcome.

# 7) Important Limitations

- **Lack of empirical data**:  
  Nearly all direct evidence is theoretical or simulation-based. Most findings about efficiency are modeled rather than directly measured in real human groups or lab experiments with actual payoffs.

- **Behavioral outcomes ≠ payoff outcomes**:  
  Many papers conflate or substitute cooperation rate for efficiency, but high cooperation is not always efficient if punishment is costly, misapplied, or motivated by antisocial incentives.

- **Sparse evidence for nonstandard dimensions**:  
  Game features such as chat, contribution framing, real-time feedback, punishment/reward technology specification, and many nuanced information features are under-explored.

- **Ecological, social, and informational context**:  
  Effects of punishment on efficiency depend on environmental features (resource renewal, network adaptation, risk), but direct guidance is available only for some stylized model contexts.

- **Phase transitions and non-monotonicity**:  
  Several models predict efficiency effects that are highly sensitive to parameter thresholds—small changes in punishment cost or MPCR can flip the efficiency effect's sign.

- **Antisocial punishment, corruption, and competition**:  
  These factors can undermine or reverse the typical efficiency gains from punishment; such settings are not universally or systematically modeled.

- **Transferability**:  
  Complex models are often specified for idealized, infinite, well-mixed or locally structured populations, which may not generalize to finite, real-world, or laboratory environments.

---

**In summary:**  
The literature provides robust theoretical support for a **positive efficiency impact of enabling punishment in PGGs**, conditional on game design dimensions—most critically, **punishment cost, effectiveness, group structure, and information environment**. Empirical confirmation and direct evidence for other design manipulations are limited. Predictive accuracy will be highest where the game design matches model assumptions, and should be made cautiously when generalizing beyond those scenarios.
