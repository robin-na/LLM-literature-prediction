# 1) Evidence Base

This literature set comprises 159 papers, overwhelmingly theoretical, focusing on evolutionary game theory, agent-based modeling, analytical characterization, and computational simulations of public-goods-game (PGG) and related social dilemmas. There is a conspicuous scarcity of empirical laboratory experiments or field studies directly measuring payoff-based efficiency outcomes in PGGs with and without punishment; nearly all the relevant empirical studies are adjacent in design (e.g., ultimatum or principal-agent games). The set is broad and deep in terms of conceptual coverage across punishment mechanisms, population structures, learning rules, sanction types (peer, pool, institutional), norm evolution, and indirect reciprocity but less so in empirical parameterization or direct experimental effect sizes. Most results map to evolutionary or long-run equilibrium outcomes.

The evidence base directly addresses the central research question—predicting the efficiency effect of enabling punishment in PGG-like environments—from a wide variety of theoretical perspectives, with exact, close, or adjacent scope in almost every conceivable model variant. However, direct and quantitative synthesis for the full, empirically parameterized prediction task is limited by a lack of direct empirical outcome studies matching all 14 prediction design dimensions.

# 2) Task Relevance

The literature's relevance for the prediction task can be summarized on three main dimensions:

**a. pgg_or_variant:**  
- **exact:** The largest portion of the literature addresses standard or canonical PGGs, repeated PGGs, or minor variants, often with continuous or binary contribution choices, and with well-defined group structure and benefit-cost parameters.
- **close:** A substantial number of papers focus on adjacent games—public-goods-like dilemmas, threshold games, repeated Prisoner's Dilemma (IPD), common-pool resource games, and indirect reciprocity on networks—that share essential mechanisms and are analytically analogous to PGGs but differ in finer details.
- **adjacent/weak/none:** Some model settings are further from the canonical PGG structure (e.g., ultimatum game, Traveler’s Dilemma, principal-agent), offering only contextual insights.

**b. punishment_or_sanctions:**  
- **exact:** Many theory papers model peer, pool, or institutional punishment (with explicit cost/impact structures). Metanorms, anti-social punishment, and specifics of retaliation are often explicitly included.
- **close/adjacent:** Some papers discuss only reputation loss, indirect reciprocity, or partner selection as sanctioning, which are functionally similar but not technically the same as peer cost-imposing punishment.
- **weak/none:** Some studies do not include any sanctioning mechanism.

**c. efficiency_or_related_payoff_outcome:**  
- **exact:** There is a solid subset modeling aggregate group payoff, average efficiency, welfare, or surplus—i.e., direct payoff-based efficiency outcomes.
- **close/adjacent:** Many works focus on non-payoff behavioral outcomes (cooperation rates, strategy frequencies, norm prevalence) but provide a reasoned or implied mapping to payoff-based efficiency—often as “higher cooperation implies higher efficiency.”
- **none:** A portion of the set measures only behavioral strategies, perception, or evolution of norms without quantifying efficiency.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:**  
  - Explicit modeling or reporting of average group payoff, system efficiency, group welfare, surplus, or coins/resources generated under different game parameterizations.  
  - In many theoretical models, mean fitness or long-run payoff equilibrium is used as a proxy for efficiency.  
  - Simulation-based results often report average payoff for each strategy group or the total population, sometimes relative to the fully cooperative maximum.
- **Non-payoff behavioral outcomes:**  
  - Contribution frequency, cooperation rate, prevalence of punishment, evolution/stability of cooperative/punishing strategies, fraction of defectors/punishers, or norm compliance.
  - A large number of papers report only strategy frequencies based on evolutionary stability, not translate these directly to efficiency.

Crucially, while cooperation rate and efficiency are often correlated, they are not synonymous, as the cost of punishment, second-order free riding, anti-social punishment, and other strategic nuances can mean that higher cooperation does not always translate into higher group efficiency.

# 4) Main Findings Relevant To Prediction

### Empirical Findings:
- Empirical/lab evidence directly measuring efficiency (total payoff) with and without punishment in PGGs is very sparse. Theoretical/simulation work dominates.

### Theoretical and Simulation Findings:

- **Punishment generally increases efficiency over no-punishment when defectors dominate the baseline,** provided punishment is not excessively costly and retaliation or anti-social punishment are not too prevalent [(Gintis, 2000); (Henrich & Boyd, 2001); (Bowles & Gintis, 2004); (Gao et al., 2012); (Wang et al., 2010)].
- **The positive efficiency impact of punishment is highly contingent** on game parameters: punishment cost and magnitude, group size, number of rounds/continuation probability, the possibility of anti-social punishment, and the game’s spatial structure [(Rand et al., 2010); (Powers et al., 2012); (Eldakar et al., 2007); (Wolff, 2012); (Janssen & Bushman, 2008); (Nakamaru & Iwasa, 2006); (Sigmund et al., 2011)].
- **Punishment effect is largest when punishment is effective (high impact per unit cost) and not prohibitively costly [(Gintis, 2000); (Okada & Bingham, 2008)].**  
- **Pool/institutional punishment and the presence of metanorms (sanctioning non-punishers or rewarding punishers)** can enhance stability and efficiency, often more than peer punishment alone [(Sigmund et al., 2011); (Kendal et al., 2006)].
- **Presence of anti-social punishment or retaliation can neutralize or reverse efficiency gains.** If defectors also punish cooperators, or if punished individuals can retaliate, the efficiency effect may be null or negative [(Rand et al., 2010); (Powers et al., 2012); (Janssen & Bushman, 2008)].
- **Punishment can reduce efficiency when its cost outweighs the gains from increased cooperation,** particularly in games with high punishment cost, high retaliation potential, short horizon, or in the presence of persistent anti-social punishment [(Wolff, 2012); (Jaffe, 2004); (Abbink et al., 2004); (Isakov & Rand, 2012)].
- **Reward is occasionally found to outperform punishment on efficiency,** especially in spatial or heterogeneous settings, and when the cost of reward is relatively less than that of punishment [(Zhuang et al., 2012); (Kendal et al., 2006)].
- **The effect of enabling punishment saturates or reverses if the cost of punishment is too high,** if punishment is weak (low impact per cost), or if the game is too short (low repeated play) [(Eldakar et al., 2007); (Jones, 1999); (Weibull & Salomonsson, 2006)].
- **Spatial structure, voluntary participation, and reputation mechanisms generally enhance the positive effect of punishment on efficiency,** by supporting cluster formation, reducing second-order free riding, and allowing targeted punishment [(Perc & Szolnoki, 2012); (Sigmund et al., 2011); (De Silva & Sigmund, 2009); (Gintis et al., 2001)].
- **Absence or concealment of punisher identity can modulate retaliation and thus efficiency,** with anonymous punishment often more effective at sustaining cooperation [(Janssen & Bushman, 2008)].

# 5) Prediction Guidance

### General Guidance:

The preponderance of strong theoretical evidence supports a **default prediction that enabling peer punishment in a standard PGG increases average efficiency (group payoff) relative to a punishment-disabled control**, **when the following conditions are met**:
- The baseline game is characterized by substantial defection (low control efficiency).
- Punishment is not extremely costly; it is effective at deterring defection (i.e., fine:cost ratio is favorable).
- Anti-social punishment and retaliation are absent or limited.
- The number of rounds is sufficient (repeated interaction); efficiency increases with longer games or higher continuation probability.
- Group size (player_count) is not extremely large. Efficiency gains from punishment are less robust in larger groups due to the scaling of enforcement costs and free-riding opportunities [(Eldakar et al., 2007); (Bowles & Gintis, 2004)].
- There is some feedback via social learning, reputation, or voluntary participation, which can stabilize cooperative norms [(Henrich & Boyd, 2001); (Sigmund et al., 2011)].

### Moderators/Mediators:

**Key game design dimensions that directly moderate the effect of punishment on efficiency (and for which evidence is exact or close):**
- **player_count:** Smaller groups typically see a higher positive impact of punishment. Large group size increases the free-rider problem and can dilute punishment effectiveness [(Eldakar et al., 2007); (Bowles & Gintis, 2004)].
- **num_rounds:** More rounds/longer repetition amplify the ability of punishment to sustain cooperation [(Jones, 1999); (Leimar, 1997)].
- **punishment_cost / punishment_tech:** Higher cost or lower efficacy of punishment weakens or negates its efficiency benefit. Adaptive, severe, and not-too-costly punishment improves outcomes [(Okada & Bingham, 2008); (Deng et al., 2012); (Gintis, 2000)].
- **mpcr (marginal per-capita return):** Efficiency gains from punishment are larger when mpcr is low to medium; if mpcr is already high, cooperation may be stable even without punishment.
- **Presence of anti-social punishment:** (whether defectors can punish cooperators): If present, the efficiency effect may be reduced to zero or negative [(Rand et al., 2010); (Powers et al., 2012)].
- **Retaliation possibility:** Easy retaliation against punishers (especially if punishers are identifiable) can suppress the efficiency benefit [(Wolff, 2012); (Janssen & Bushman, 2008)].
- **Reward_exists:** Literature suggests that reward can sometimes be as effective or more effective than punishment, depending on cost structure [(Zhuang et al., 2012); (Kendal et al., 2006)].
- **show_punishment_id, show_other_summaries:** Transparency and information structure affect retaliation, social learning, and thus efficiency.

**Variables with only indirect or contextual evidence:**
- **chat:** Most models lack communication; its effect is positive for cooperation in empirical studies but less addressed for efficiency when combined with punishment.
- **default_contrib:** Framing (opt-in/out) effects are rarely discussed explicitly.
- **all_or_nothing, show_n_rounds, reward_cost, reward_tech, show_other_summaries:** Sometimes addressed, but not systematically manipulated for efficiency impact.

### Quantitative Prediction:

The literature provides strong qualitative directionality (punishment increases efficiency relative to control in most, but not all, standard PGGs), but does **not** offer robust quantitative formulas or effect sizes that relate design dimensions and control efficiency to predicted treatment efficiency except in the context of specific parameter sweeps in simulation/theory papers.

**Mapping from control to treatment efficiency is most strongly inferred when:**
- Control efficiency is very low (defection dominates); enabling punishment generally yields substantial gains.
- Control efficiency is already high (cooperation stable without punishment); enabling punishment can at best maintain efficiency, and in some cases may slightly reduce it due to punishment costs.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed (frequently, with exact or close evidence):**
- `player_count`
- `num_rounds`
- `mpcr`
- `punishment_cost`
- `punishment_tech`
- `reward_exists` (in literature comparing reward and punishment)
- (To a lesser extent) `all_or_nothing`, `reward_cost`, `show_punishment_id`, `show_other_summaries` (some simulation models, but often not primary focus)

**Indirectly/Contextually Discussed:**
- `chat` (discussed as promoting trust/cooperation but rarely in synergy with punishment/efficiency)
- `default_contrib` (very little direct analysis)
- `show_n_rounds` (analytically analogous to continuation probability/discounting; impacts the effect of threat of punishment)
- `show_other_summaries` (serves as reputation/information; indirectly addressed)
- `reward_tech`, `reward_cost` (in papers comparing reward to punishment)

**Effectively Missing for Prediction Purposes:**
- No systematic empirical parameterization or cross-study meta-analysis links multiple design dimensions simultaneously to efficiency outcomes with high precision.  
- Explicit analysis of interaction effects between lesser-studied dimensions (chat × punishment, opt-in framing × punishment, etc.) is almost absent.

# 7) Important Limitations

- **Empirical data paucity:** There is a near-total absence of large-scale, parameter-matched experimental studies directly reporting efficiency or group payoff for peer-punishment-enabled vs control PGGs as a function of all 14 design dimensions.
- **Reliance on theoretical models:** The strong guidance is built on stylized evolutionary games, often with simplified assumptions about player rationality, population updating, and structure; generalizing to empirical settings or to all parameter regions is hazardous, particularly in cases involving human subjects.
- **Behavioral versus payoff outcome conflation:** Many papers infer payoff effects from cooperation rate, but second-order effects (punishment costs, antisocial punishment, retaliation, etc.) mean that higher cooperation does not always mean higher efficiency.
- **Sparse coverage of specific dimensions:** Some prediction variables are rarely modeled (e.g., chat, opt-in framing, default_contrib, information displays), reducing confidence in out-of-sample prediction for games manipulating these features.
- **Parameter sensitivity and non-monotonicities:** The direction and magnitude of punishment effects are sensitive to parameter regimes. For instance, anti-social punishment, high punishment cost, short time horizons, or easy retaliation can suppress or reverse efficiency gains.
- **Ambiguity in edge cases and in the presence of anti-social punishment:** Several credible models and some empirical examples show punishment can reduce efficiency compared to the baseline (especially when punishment is too frequent or used for norm enforcement rather than cooperation), creating warning cases for over-generalization [(Rand et al., 2010); (Abbink et al., 2004); (Jaffe, 2004)].

# Summary Table: Design Dimension Coverage

| Dimension                 | Coverage in Literature         | Key Finding/Implication for Prediction                                  |
|---------------------------|-------------------------------|-------------------------------------------------------------------------|
| player_count              | exact                         | Efficiency benefit of punishment declines in larger groups              |
| num_rounds                | exact                         | Longer games enhance positive effect of punishment                      |
| mpcr                      | exact                         | Lower mpcr: greater efficiency boost from punishment                    |
| punishment_cost           | exact                         | Lower cost: larger, more robust efficiency gains                        |
| punishment_tech           | exact                         | Higher impact per cost: stronger positive effect                        |
| reward_exists             | exact / close                 | Reward can enhance or substitute for punishment, sometimes more effective|
| reward_cost, reward_tech  | close                         | Less systematic, but optimal reward cost is generally lower than punishment|
| all_or_nothing            | close                         | Moderate impact; sometimes modeled                                      |
| chat                      | indirect                      | Promotes trust/cooperation, less clear with punishment on efficiency    |
| show_punishment_id        | indirect                      | Anonymity can reduce retaliation, increasing efficiency                 |
| show_other_summaries      | indirect                      | Information can support/preserve efficiency via reputation mechanisms   |
| show_n_rounds             | indirect (as time horizon)    | Short games weaken punishment effect; longer is better                  |
| default_contrib           | missing                       | Not analyzed in most studies                                            |

# Concluding Prediction Guidance

**When using this literature to predict treatment efficiency (punishment enabled) from design dimensions and control efficiency:**
- **Default expectation** is that enabling peer punishment substantially increases efficiency where baseline defection is high, punishment is effective and not too costly, and group size/time horizon is favorable.
- **Caveats**: In high-cost, retaliation-possible, antisocial punishment, or short-game contexts, the effect may be negligible or negative.
- **Effects are strongly moderated** by design dimensions including punishment cost/effectiveness, group size, number of rounds, presence of rewards, and information structure.
- **Quantitative predictions** should be made with caution and, where possible, parameterized using the formulas and threshold conditions given in the closest-matching theoretical papers.
- **Dimension interactions and less-studied design features** should prompt conservative or uncertainty-inclusive predictions, as empirical evidence is lacking.

If the specific game design falls into an area with limited direct evidence (e.g., features like chat, opt-in framing, complicated information/reward architectures), **predictions should focus on baseline expectations from the best-matched theoretical models, and highlight the resulting increased uncertainty**.
