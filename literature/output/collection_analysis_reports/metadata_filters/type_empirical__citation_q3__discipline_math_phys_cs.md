# 1) Evidence Base

This literature set is composed entirely of empirical laboratory and field experiments, with one observational study and no theoretical-only papers. The set is moderately broad in terms of the types of game environments studied, covering standard linear public goods games (PGGs), close variants (including binary trust games, feedback systems, and piracy-like games), and unrelated behavioral games (e.g., primate cooperation). Experimental manipulations include the presence/absence of punishment, variations in punishment structure (e.g., anonymous vs. identifiable, coordinated vs. uncoordinated), and related mechanisms (e.g., redistribution, priming, information about others).

Despite this breadth, only a minority of studies report payoff-based outcomes (efficiency or group earnings), and even fewer compare efficiency with and without peer punishment using standard PGGs. Most studies measure behavioral outcomes (contribution rates, trust, strategy updates, norm compliance), and several investigate punishment in games only adjacent to PGGs (e.g., trust games, market feedback systems). The depth of evidence for the exact prediction task—predicting group efficiency changes when enabling peer punishment in well-parameterized PGGs—is therefore moderate but somewhat limited by the scope and outcome measures of the included studies.

# 2) Task Relevance

**pgg_or_variant:**  
- Five papers have exact relevance, investigating standard PGGs or linear voluntary contribution mechanisms (VCMs).
- Four papers study close variants (e.g., digital piracy, optional PGGs, trust games with some PGG features).
- Three are adjacent, dealing with norm enforcement, moral hazard markets, or animal cooperation models.

**punishment_or_sanctions:**  
- Only two papers examine peer punishment in standard PGGs with close institutional similarity to the prediction task.
- Several others use adjacent concepts (exogenous punishment, third-party/collective punishment, feedback retaliation, leader punishment), or have no punishment at all (primarily focusing on control conditions or other interventions).

**efficiency_or_related_payoff_outcome:**  
- Only three studies report exact efficiency or welfare outcomes directly (ratio or group total relative to maximum possible).
- Three more use closely related outcomes (group profit, earnings), though sometimes in non-standard games or not as ratios.
- The majority focus on non-payoff behavioral outcomes (contributions, cooperation rates), do not analyze efficiency, or confound efficiency with other variables.

**Summary:**  
- Only a small subset of the literature provides *exact* evidence along all three dimensions required for the downstream prediction task. Most studies contribute *indirect* or *adjacent* evidence, especially regarding punishment mechanisms and efficiency outcomes.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes (efficiency, group payoff, welfare):**  
- ***Reported explicitly:***  
  - Engelmann & Nikiforakis (2015): Direct group efficiency measures under different punishment conditions in a repeated linear PGG.
  - Bolton et al. (2018): Efficiency (realized divided by maximum possible payoff) in feedback/moral hazard experiments.
  - Oberholzer-Gee et al. (2010): Share of stakes converted to winnings (as a proportion), a direct efficiency analog in a one-shot game.
  - Hashim et al. (2014): Group profit and purchasing rates (as absolute and relative levels), though in a piracy context.
  - Ren & Zheng (2021): Efficiency under redistribution, but only in PGGs without punishment.

- ***Reported but as secondary outcomes or not used for main inference:***  
  - Some studies present average or total earnings but focus analysis on behavior.

**Non-payoff behavioral outcomes:**  
- ***Primary focus:***  
  - Villatoro et al. (2014): Contribution rates as an outcome of punishment coordination.
  - Drouvelis et al. (2015), Martinsson et al. (2015): Contribution rates and conditional cooperation.
  - Xu et al. (2019): Strategy updating dynamics.
  - Sun et al. (2022), Sun & Luo (2020): Trust/trustworthiness (binary outcomes), punishment assignment behavior, voting; gender differences in punishment.
  - Chen & Hauser (2005): Pulling/cooperation frequency and fit to punishment-based behavioral models in primate dyads.

**Distinction:**  
- Only a small fraction of the evidence speaks directly to group efficiency. Most of the literature emphasizes social behavioral responses to incentives or the structure of punishment, which—while informative about potential efficiency channels—cannot simply be treated as efficiency outcomes.

# 4) Main Findings Relevant To Prediction

**Efficiency effects of enabling peer punishment in PGGs:**  
- **Punishment increases efficiency conditionally:**  
  - In standard, linear, repeated PGGs, enabling peer punishment increases group efficiency *relative to control (no-punishment)* when the punishment mechanism is *constrained*: a single, anonymous punishment stage per round, with round-randomized IDs. Efficiency gains accrue over time, surpassing control games in later rounds. The efficiency gain is attributed to increasing contributions with contained punishment costs (Engelmann & Nikiforakis, 2015).

- **Complex punishment undermines efficiency:**  
  - When punishment mechanisms are less constrained—multiple stages per round, fixed (identifiable) player identities, full information about who punished whom—efficiency does **not** increase compared to control. While punishment increases contributions, this is offset by higher punishment costs and the emergence of feuding and retaliation cycles. Not all groups are affected equally; some achieve high cooperation, but others experience costly conflicts (Engelmann & Nikiforakis, 2015).

- **Retaliation and bilateral punishment can reduce efficiency:**  
  - In adjacent environments (two-sided moral hazard with mutual feedback withdrawal), introducing bilateral punishment/retaliation options reduces efficiency by promoting strategic retaliation and reducing the informativeness of reputation mechanisms. This negative effect is absent in one-sided settings (Bolton et al., 2018).

- **No evidence for payoff benefit from norm-signaling or leader punishment interventions:**  
  - Studies of coordinated versus uncoordinated punishment structures (Villatoro et al., 2014) and gender differences in punishment intensity (Sun & Luo, 2020) find differences in behavioral outcomes (cooperation rates, punishment assignment), but do not report group efficiency, so cannot clarify the net payoff effect.

- **Control (punishment-off) efficiency is often low and stable:**  
  - Across studies, in the absence of punishment, group efficiency remains low (often below 50% of maximum relative to full cooperation), and is resistant to increases through redistribution (Ren & Zheng, 2021) or priming (Drouvelis et al., 2015), though unpredictable context effects exist.

**Moderators and contextual variables:**  
- The structure and *costliness* of punishment, the number of possible punishment stages per round, anonymity, information about punishers, and the potential for retaliation are repeatedly shown or argued to moderate the efficiency effect.
- The *presence* of social cues or coordination in punishment increases cooperation rates, but these effects cannot be directly translated to efficiency improvements in the absence of cost accounting.
- Player demographics and history can affect baseline efficiency (Oberholzer-Gee et al., 2010) but not the effect of punishment per se.

# 5) Prediction Guidance

- **Quantitative prediction of treatment efficiency (punishment-on) from control efficiency is only directly supported for standard linear PGGs when punishment is implemented as a single, anonymous, uncoordinated stage per round (Engelmann & Nikiforakis, 2015):**
  - If *control efficiency is low* and *punishment is simple and anonymous*, enabling punishment is likely to increase efficiency, especially in later rounds. Magnitude of improvement is design-dependent, but can cross control-outcome lines by end of the experiment.
  - If *punishment allows for multiple stages, fixed identities, and full information*, enabling punishment does **not** reliably increase efficiency despite higher contributions; efficiency gains are absorbed by punishment costs and feuds.
  - Thus, *prediction should weight punishment mechanism design heavily*, not simply the presence of punishment.

- **When using design dimensions for prediction:**
  - *player_count, num_rounds, mpcr, punishment_cost, punishment_tech*—especially the anonymity/identifiability of punishers and the number of punishment stages—are directly evidenced as strong moderators.
  - *chat, all_or_nothing, default_contrib, reward*, and information display dimensions (*show_n_rounds, show_other_summaries, show_punishment_id*) are largely untested or contextually discussed; prediction using those is weakly informed here.

- **When literature offers only behavioral outcomes:**
  - High cooperation/contribution rates due to punishment may *not* translate into higher group efficiency unless punishment costs are small and retaliation mechanisms are absent.

- **Control (punishment-off) efficiency does not predict treatment efficiency unless the punishment institution is specified in detail.** Mechanism details can reverse the direction of the effect.

- **Where no directly relevant evidence is provided (e.g., leader punishment, third-party punishment, trust games), predictions about efficiency effects in standard PGGs are speculative and should be treated as such.**

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**
- *player_count:* Almost all empirical PGGs and variants specify group size, sometimes manipulating it.
- *num_rounds:* Varies across studies; repeated interaction is frequently studied.
- *mpcr:* Explicitly stated and sometimes varied in standard PGG experiments.
- *punishment_cost/punishment_tech:* Deeply analyzed in Engelmann & Nikiforakis (2015), Bolton et al. (2018), Sun & Luo (2020), and other studies.
- *all_or_nothing:* Sometimes specified; effects not systematically analyzed for punishment effects.
- *show_punishment_id (anonymity/fixed IDs):* Major focus in Engelmann & Nikiforakis (2015); shown as critical moderator.
  
**Indirect/Partially Informed:**
- *chat, show_n_rounds, show_other_summaries:* Mentioned as experimental features; little direct evidence of their effect on efficiency or punishment impact.
- *default_contrib:* Discussed as framing in some control settings, not manipulated in punishment studies.
- *reward_exists, reward_cost, reward_tech:* Not the focus of any study; only relevant as absent or in setting baselines.
  
**Contextually Discussed or Missing:**
- Most information-based and interface features (*show_n_rounds*, *show_other_summaries*, *show_punishment_id*) are contextually discussed rather than analyzed as treatments.
- *reward dimensions* are omitted or set to zero in all included punishment experiments.

# 7) Important Limitations

- **Few studies allow direct, parameterized prediction of efficiency changes due to enabling peer punishment, even within standard PGGs.** The essential design nuances of the punishment stage—number of stages, anonymity, and information structure—are critical, and only a subset of literature explores these in depth.
- **Most studies substitute behavioral outcomes for payoff-based efficiency,** limiting inference about the true welfare effects of punishment.
- **No systematic investigation across the full range of 14 design dimensions**—many are untested or only noted as controlled aspects.
- **Evidence from adjacent or close-variant games (trust games, moral hazard, piracy games) must be generalized with caution**, as their mechanisms and group interaction structures often differ from standard PGGs. They can inform prediction in contextually similar but not standard-rich environments.
- **No theory papers are included to formalize mechanisms or clarify which results may generalize across parameter space.**
- **Retaliation, feuding, and complex punishment environments are shown to undermine or reverse efficiency gains,** yet precise thresholds for these effects are unquantified and context-dependent.
- **Magnitude, rather than mere direction, of efficiency change is generally underreported**, making quantitative prediction uncertain.
- **Potential for publication or experimental design bias:** Laboratory studies often focus on environments expected to show positive treatment effects, limiting the external validity to field or more complex real-world scenarios.

---

**In summary:**  
This literature set provides direct and reliable guidance for predicting treatment efficiency (with peer punishment enabled) in standard linear PGGs *only* when key punishment design features are known and well-specified, particularly anonymity, punishment cost, and the number of punishment stages. When these features are absent or the design allows retaliation and complex punishment responses, efficiency gains are not observed. Most other dimensions are under-informed. For all other design contexts or when relying on behavioral outcomes, predictions about efficiency gains from punishment must be made cautiously and with explicit acknowledgment of these limitations.
