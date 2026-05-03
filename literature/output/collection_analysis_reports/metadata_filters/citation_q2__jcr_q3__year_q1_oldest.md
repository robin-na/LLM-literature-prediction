# 1) Evidence Base

The paper set includes 24 papers providing a mix of empirical (primarily laboratory experiments) and theoretical works, spanning standard public goods games (PGGs), close variants (common pool resources, rotating goods, etc.), and more distantly related social dilemmas (Prisoner's Dilemmas, endogenous partner-choice games). The set is relatively broad, containing both direct and indirect evidence, as well as mechanism arguments about the effects of punishment in collective action settings. About a third of the papers are empirical lab studies focusing on PGGs or similar structures; the remainder are formal models or interpretive theory pieces.

Empirical coverage is strongest for standard, linear PGGs with 4 players, 10–40 rounds, no chat, and continuous contributions, with and without costly peer punishment. Theory papers extend findings to evolutionary settings, structured populations, and adjacent social dilemmas. Several papers do not directly report efficiency or payoff outcomes, focusing instead on cooperation rates or norm dynamics. Some theoretical works provide explicit predictions for efficiency as a function of design parameters, enriching the conceptual toolkit for prediction.

Overall, for the downstream task of forecasting the change in efficiency with the introduction of peer punishment (conditional on design features and control efficiency), the evidence base is moderate: there is some strong direct evidence, a substantial set of indirect results, but many contextual or only marginally relevant papers.

# 2) Task Relevance

### Relevance by Dimension

- **pgg_or_variant**  
  - Labeled: `exact` for core PGGs, `close` for CPR, adjacent for repeated PD and non-standard collective action games.
  - There are several core empirical and theory papers with `exact` relevance (e.g., Nicklisch & Wolff, 2011; Kranz, 2010; Brandts & Fatas, 2012; Colombier et al., 2011). Many others are close but not canonical PGGs.

- **punishment_or_sanctions**  
  - Labeled: `exact` in most empirical and theory PGG papers; `adjacent` or `close` when focusing on exclusion, reputation, or structure as sanction mechanisms.
  - Direct experimental data on peer punishment is present; some papers also analyze reward or ostracism.
  - Several theory papers model punishment at a general level or via mechanism arguments.

- **efficiency_or_related_payoff_outcome**  
  - Labeled: `exact`, `close`, or `adjacent` depending on outcome reported.
  - Empirical coverage of efficiency and group payoff is moderate but not universal; several key findings are based on normative or behavioral outcomes, not efficiency per se.
  - Several theory papers explicitly model efficiency or welfare as a function of game design and punishment features.

In summary: The strongest coverage is for `pgg_or_variant` with `exact` or `close` mapping, and for `punishment_or_sanctions` with at least `close` relevance. However, direct reporting of efficiency or group payoff (the target outcome) is somewhat less frequent, with several studies reporting only behavioral (contribution) outcomes.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes** (exact/close/adjacent):
  - **Efficiency/group payoff/welfare**: Directly measured in some lab experiments (Nicklisch & Wolff, 2011; Colombier et al., 2011) and modeled in detail in several theory papers (Kranz, 2010; Nakao, 2009; Wolff, 2012).
  - **Surplus, total earnings**, and **explicit efficiency ratios**: Less frequently reported, though implied in theory (Kranz, 2010; Chassang & Takahashi, 2011).
  - **Weak** or **adjacent** referencing in papers focusing on social welfare, resource stock, or “social benefit”, but without explicit efficiency ratios (Vincent, 2007; Rob & Yang, 2010).

- **Non-payoff behavioral outcomes**:
  - **Contribution/cooperation rate**: Most frequently measured outcome in experiments.
  - **Punishment frequency, norm compliance, exclusion, or ostracism activity**: Common foci in both empirical and theory literature.
  - **Attitudes, perceived fairness, or approval**: Studied in observational and attitudinal research (Ohnuma et al., 2005).
  - Most papers reporting behavioral outcomes (contribution, punishment action, norm monitoring) do not directly report on efficiency.

# 4) Main Findings Relevant To Prediction

- **Punishment usually increases cooperation/contributions** in both standard and close PGGs, as supported by both empirical lab work and theory (Nicklisch & Wolff, 2011; Kranz, 2010; Brandts & Fatas, 2012).
- **Effect on efficiency (payoff) is conditional:**
  - When punishment is **not too costly and is targeted at defectors**, **efficiency generally rises** compared to control (no punishment) (Kranz, 2010; Nicklisch & Wolff, 2011; Vincent, 2007).
  - **High punishment costs or presence of anti-social/counter-punishment** can **reduce or eliminate gains** in efficiency, sometimes even causing efficiency to fall below the control treatment (Colombier et al., 2011; Wolff, 2012; Nakao, 2009).
- **Punishment mechanism details matter**:
  - **Counter-punishment (retaliation against punishers)** does not necessarily lead to an efficiency collapse (Nicklisch & Wolff, 2011), but can under some evolutionary or high-mutation settings (Wolff, 2012).
  - The **effectiveness (impact/cost ratio) and precision of punishment** (punishment_tech) strongly moderate its effect (Kranz, 2010; Nakao, 2009).
  - **Procedural justice** (accuracy, transparency) and social identification can enhance the positive effect of punishment (De Cremer et al., 2012), but evidence on efficiency is indirect.
- **Comparison with reward and exclusion:**
  - In designs where both punishment and reward are possible, **reward tends to outperform punishment in efficiency** (Colombier et al., 2011).
  - **Ostracism/exclusion mechanisms** can robustly increase cooperation, with likely positive effects on efficiency (Akpalu & Martinsson, 2012; Rob & Yang, 2010).
- **Structural and social moderators**:
  - **Number of players, rounds, MPCR (marginal returns), group structure**: More rounds and higher MPCR generally strengthen the positive effect of punishment, but very high continuation probabilities with low punishment efficiency can increase the risk of efficiency erosion due to sustained retaliation or strategic exploitation (Wolff, 2012; Kranz, 2010).
  - **Observability, chat, information display**: Effects are mostly reported on behavioral (cooperation) rather than on efficiency outcomes.
- **Ambiguity and disagreement**:
  - Some models and data suggest **punishment may undermine group efficiency**, especially when antisocial punishment/counter-punishment or evasion is possible (Colombier et al., 2011; Mulder et al., 2009; Wolff, 2012).
  - Empirical and theoretical results are mostly aligned for standard linear PGGs, but less so for games with more complicated structure (common pool resources, exclusion games, etc.).

# 5) Prediction Guidance

- **When directly relevant efficiency data are available (e.g., Nicklisch & Wolff, 2011; Kranz, 2010):**
  - **Enabling peer punishment is likely to increase efficiency over control** if:
    - Punishment costs are not excessive,
    - Punishment is effective (high impact per cost),
    - Retaliation/antisocial punishment is low,
    - The MPCR is not too low,
    - The setting lacks complex evasion or circumvention opportunities.
  - The predicted increase is stronger in **simple, small-group, fixed-length PGGs** that match the lab standards.

- **Where direct evidence is missing (reliance on behavioral outcomes or theory):**
  - **Efficiency uplift is plausible** only insofar as increased cooperation outweighs direct costs of punishment.
  - **High punishment cost or prevalence of antisocial punishment/counter-punishment** may mean **efficiency stays flat or falls**, even if behavioral cooperation increases.
  - **Rewards or exclusion** (when available) may outperform punishment in boosting efficiency.

- **Design dimensions for prediction:**
  - Emphasis should be placed on **punishment_cost**, **punishment_tech**, **player_count**, **num_rounds**, and **mpcr** as direct predictors, supported by quantitative or semi-quantitative models (Kranz, 2010; Nakao, 2009).
  - **Control efficiency** is a strong baseline; predicted efficiency with punishment should not exceed the full cooperation benchmark, and uplift should be parameterized by the incremental cost-benefit calculus of the punishment regime.

- **Ambiguity:**  
  - For **adjacent or weakly relevant game types** (ostracism, common pool resources, endogenous group structuring games), results may not transfer cleanly. Predictions should accordingly be made with caution and clear statement of limitations.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions:**  
- `player_count`: Frequently varied and analyzed (Nicklisch & Wolff, 2011; Kranz, 2010).
- `num_rounds`: Studied as moderator of punishment effectiveness (Wolff, 2012; Davis & Holt, 1994; Kranz, 2010).
- `mpcr`: Explicit in theory and empirical studies for payoff calculus (Kranz, 2010; Nakao, 2009).
- `punishment_cost`, `punishment_tech`: Central in almost all theoretical and empirical studies of punishment efficiency (Nicklisch & Wolff, 2011; Kranz, 2010; Nakao, 2009).
- `all_or_nothing`: Occasionally varied, but mostly continuous contributions.
- `chat`, `show_n_rounds`, `show_other_summaries`: Sometimes included, primarily as context.
- `reward_exists`, `reward_cost`, `reward_tech`: Directly studied in some relevant comparison designs (Colombier et al., 2011).

**Indirectly or contextually discussed dimensions:**  
- `default_contrib`: Rare, only as framing in a few experiments.
- `show_punishment_id`: Infrequently manipulated; some lab studies vary anonymity or identifiability (Nicklisch & Wolff, 2011).
- `show_n_rounds` and `show_other_summaries`: Sometimes manipulated; impact is usually studied via contribution and cooperation, less so via efficiency.

**Effectively missing:**  
- No direct evidence reporting or modeling predictions by variation in `default_contrib`, or on the technical specification of `punishment_tech` and `reward_tech` beyond cost/impact per unit.
- Details on communication (`chat`) and information display are often omitted or treated as background.

# 7) Important Limitations

- **Incomplete coverage of all prediction dimensions:**
  - While core predictors (player count, num rounds, punishment parameters) are robustly studied, others (default_contrib, reward_tech, information display) are weakly or not at all covered.
- **Scarcity of direct efficiency outcome data:**
  - Many experimental and theoretical papers analyze only cooperation rates, not group payoff or efficiency.
- **Ambiguity in generalizing from adjacent or close variants:**
  - Several findings are from CPR, exclusion, or repeated PD games; efficiency effects may not translate directly to linear PGGs.
- **Sensitivity to context and mechanism detail:**
  - Some efficiency effects of punishment are highly model- or parameter-dependent (punishment cost, retaliation, opportunity for antisocial punishment, structural features), resulting in contradictory or context-dependent findings.
- **Potential publication bias and lab effect:**
  - Most experiments are laboratory-based with fixed group size, artificial stakes, and limited rounds, which may not generalize to field or large-scale environments.
- **Absence of experimental data on some dimensions:**
  - Features like communication (`chat`), explicit identity display (`show_punishment_id`), and advanced reputation or network structures are rarely experimentally varied in direct conjunction with efficiency outcomes.
- **Interpretation risk with non-payoff outcomes:**
  - Many findings cited as evidence for the efficacy of punishment are based on cooperation/contribution behavior; claims regarding efficiency must be bounded by the recognition of this distinction.

**In summary:**  
The literature provides a foundation for predicting the effect of enabling punishment on efficiency in standard PGGs as a function of key game design parameters and control efficiency. However, sparse direct evidence on some design dimensions and the variable effect of punishment across parameter spaces (especially re: cost/tech and retaliation/antisocial punishment) mean that predictions will carry substantial uncertainty outside well-studied, “canonical” parameter ranges. Caution should be exercised when extrapolating from adjacent games or from behavioral to payoff outcomes.
