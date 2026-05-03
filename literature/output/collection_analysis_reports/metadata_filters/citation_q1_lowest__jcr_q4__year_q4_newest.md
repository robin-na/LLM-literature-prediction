# 1) Evidence Base

The paper set includes 25 sources, spanning empirical experimental work, theory, and observational/ethnographic studies. There is a moderate concentration of experimental lab studies employing controlled manipulations of punishment, reward, and institutional design in economic games, including classic public goods games (PGGs), coordination games, bargaining games, trust games, and variants/adjacents (e.g., institutional or team investment games). Several theory papers formalize collective action problems and social dilemmas with and without punishment. A minority of papers are observational, ethnographic, or contextual, not using experimental games.

For the downstream prediction task—forecasting efficiency changes in a PGG when peer punishment is enabled—only a subset of these papers provide direct empirical or theoretical evidence. The evidence base captures both direct and adjacent forms of punishment (peer, institutional, third-party, coordinated), and a range of payoff-based outcomes. Some papers have high transferability for the prediction task, while others provide only adjacent or contextually relevant insights.

# 2) Task Relevance

**a. PGG or Variant:**  
- *Exact relevance*: Several experimental and theory papers study classic PGGs or institutional variants (e.g., Cobo-Reyes et al., 2022; Pancotto et al., 2023; Ishikawa & Fontanari, 2025; Peng, 2022).
- *Close/adjacent relevance*: A large segment focuses on related social dilemmas—trust games, coordination games, threshold games, bargaining, or investment games—which share structural features but may not match PGGs in all design dimensions (e.g., Lec et al., 2023; Gueth & Otsubo, 2023; Calabuig et al., 2024).
- *Weak or none*: Some papers offer only conceptual or contextual relevance, not using PGG mechanics.

**b. Punishment or Sanctions:**  
- *Exact relevance*: Strong coverage of punishment manipulations, especially in experimental work with peer or institutional punishment (e.g., Cobo-Reyes et al., 2022; Ishikawa & Fontanari, 2025; Pancotto et al., 2023).
- *Close/adjacent relevance*: Several focus on adjacent forms (third-party or coordinated punishment, or walk-away/partner choice) or discuss reward instead (e.g., Lütz et al., 2023; Kurokawa, 2022).
- *None*: Some studies mention sanctions contextually but do not manipulate or study punishment.

**c. Efficiency or Related Payoff Outcomes:**  
- *Exact relevance*: A solid subset directly measures efficiency, group payoff, or closely related outcomes (e.g., Cobo-Reyes et al., 2022; Peng, 2022; Li et al., 2023; Gueth & Otsubo, 2023; Lec et al., 2023).
- *Close/adjacent*: Some use behavioral proxies (contribution rates, norm compliance) that are correlated, but not identical, to efficiency (e.g., Pancotto et al., 2023; Buso et al., 2025).
- *None*: Several report only behavioral or qualitative outcomes, or do not report payoff/efficiency at all.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (relevant for efficiency prediction):**
  - Average individual or group payoff.
  - Efficiency (group payoff as a proportion of the maximum).
  - Welfare/surplus/coins generated (e.g., Cobo-Reyes et al., 2022; Peng, 2022; Ishikawa & Fontanari, 2025).
  - Productivity per time unit (Kamei & Tabero, 2025).
- **Non-payoff behavioral outcomes:**
  - Contribution/cooperation rate (how much is given).
  - Frequency, targeting, and motives of punishment.
  - Acceptance/rejection rates in bargaining.
  - Partner choice frequencies.
  - Observed norm compliance.
  - Qualitative reports on conflict resolution strategies (e.g., Sequeira, 2023).
- *Explicitly*: Some papers only infer likely payoff effects from observed contribution changes, not reporting payoffs directly (e.g., Pancotto et al., 2023; Buso et al., 2025).

# 4) Main Findings Relevant To Prediction

Synthesizing across the papers most relevant for the prediction task:

- **Punishment can increase efficiency in PGGs, but only conditionally** (on cost and design parameters). Enabling formal or peer punishment boosts payoffs relative to informal sanctions or no-punishment baselines, especially when migration or group openness allows non-cooperators to leave/join (Cobo-Reyes et al., 2022; Ishikawa & Fontanari, 2025).
- **The cost-effectiveness of punishment is crucial**: High punishment costs or low punishment effectiveness can erode or negate efficiency gains, sometimes resulting in lower final efficiency than controls (Herne et al., 2022; Calabuig et al., 2024).
- **Institutional punishment (formal, cost-sharing) sustains high efficiency more reliably** than peer punishment, but only if a critical mass of punishers is reached and costs remain low (Ishikawa & Fontanari, 2025).
- **Reward mechanisms can also boost efficiency**, sometimes more reliably than punishment, particularly in heterogeneous groups and when deployed as majority-vote reward (Peng, 2022).
- **The impact of punishment on efficiency is design-sensitive**:
  - *Group size:* Thresholds for efficient outcomes with punishment can change non-monotonically with N (Ishikawa & Fontanari, 2025).
  - *Contribution type*: Binary (all-or-nothing) vs. continuous settings can moderate the impact.
  - *Mpcr/cost-to-benefit ratio*: Low MPCR (high cost/benefit) makes punishment less likely to substantially improve efficiency (Gioffré & Tampieri, 2025; Peña et al., 2024).
  - *Visibility and observability*: If punishment is visible and deterrent, efficiency can increase more (Li et al., 2023; Gueth & Otsubo, 2023).
  - *Repeated interactions*: In longer games, initial efficiency losses from punishment (due to cost) can be offset by later gains if coordination or cooperation stabilizes (Lec et al., 2023).
- **In some adjacent designs, punishment fails to increase efficiency or even reduces it**, as the direct costs outweigh the cooperation gains or because frequent punishment destroys joint surplus (Herne et al., 2022; Calabuig et al., 2024).

# 5) Prediction Guidance

**For the downstream prediction task:**
- When moving from a control game (no punishment) to a game with punishment, you should expect:
  - **Efficiency gains if**:
    - Punishment is not prohibitively costly,
    - The fine-to-cost ratio is favorable (impact per unit of punishment is high),
    - The initial level of cooperation is not extremely low,
    - A critical mass of punishers can be reached,
    - The design features (player count, MPCR, contribution format) are not at extremes undermining coordination,
    - Punishment is visible and can serve as a deterrent (Li et al., 2023).
  - **Little or negative effect on efficiency if**:
    - Punishment is costly and often used (so costs outweigh gains from higher cooperation),
    - The group structure leads to fragmented or uncoordinated punishment,
    - Baseline cooperation is already high and there is little room for improvement,
    - The game is a variant where punishment mostly redistributes costs (Herne et al., 2022; Calabuig et al., 2024).
- **When only indirect, behavioral evidence is available:** Increases in contribution or cooperation rates can signal likely, but not guaranteed, increases in efficiency—costs of punishment must be subtracted to form payoff predictions (Pancotto et al., 2023).
- **Contextual moderators:** Group openness, possibility of migration, information presentation (e.g., showing round N, showing punishers' identity), and the option to combine rewards with punishment can substantially moderate the effect (Cobo-Reyes et al., 2022; Peng, 2022; Li et al., 2023).

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions (frequent explicit manipulation):**
- `player_count` (group size): Studied in both empirical and theory papers (e.g., effect of N on punishment efficacy).
- `num_rounds`: Many repeated games; round numbers specified.
- `mpcr`: Central in nearly all payoff-based experimental and theory works.
- `all_or_nothing` (binary vs. continuous contributions): Explicitly compared in multiple papers.
- `punishment_cost` and `punishment_tech` (cost, fine, punishment assignment): Often reported and manipulated in both peer and institutional punishment experiments.
- `reward_exists`, `reward_tech` (in studies including rewards): Particularly in Peng (2022), Pevnitskaya & Ryvkin (2022).
- `chat`: Explicitly varied in a subset (Cobo-Reyes et al., Pancotto et al.).

**Indirectly or contextually discussed:**
- `default_contrib` (opt-in/opt-out): Touched on in participation framing (Pancotto et al., 2023).
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Sometimes implicit in information conditions/manipulations (Li et al., 2023; Gueth & Otsubo, 2023).

**Sparse or effectively missing:**
- `reward_cost`, `reward_tech`: Few studies report the cost/impact ratio of rewards with precision.
- `show_punishment_id`: Seldom varied or clearly reported.
- Some dimensions are rarely the focus except as background features, reducing the ability of this literature to support granular prediction along these lines.

# 7) Important Limitations

- **Limited direct evidence for standard peer punishment in PGG:** While several papers have direct experiments with peer or institutional punishment in PGGs, many studies address adjacent games, alternative punishment forms (third-party, coordinated), or variants (binary vs. continuous, real-effort vs. tokens), possibly reducing the precision of prediction for standard PGGs.
- **Heterogeneity of punishment forms:** The literature mixes peer and institutional punishment, coordinated vs. uncoordinated, formal vs. informal, and sometimes walks away from the specific features of classic PGG peer punishment.
- **Efficiency measurement precision varies:** Not all experiments report explicit group efficiency or net payoff; some infer efficiency via contributions, which can be misleading if punishment costs are large.
- **Sparse direct evidence on several key design dimensions:** Dimensions such as visibility of punishment identity, default contribution framing, or detailed reward mechanisms are seldom systematically varied, weakening support for predictors involving these features.
- **Migration and group openness effects are only covered in select papers:** Generalizability across closed vs. open communities is thus limited (Cobo-Reyes et al., 2022 gives direct evidence, others do not).
- **Transferability from adjacent designs is uncertain:** Many findings from coordination, trust, or bargaining games may not quantitatively transfer to standard PGGs; mechanisms and relative importance of punishment costs may differ.
- **Psychological and cultural moderators are mostly contextual:** E.g., prospect-theory biases are discussed in theory (Uchida et al., 2024), but direct empirical evidence in PGGs is limited.
- **Lack of real-world field evidence:** The empirical base is predominantly lab experiments, which may not reproduce group dynamics in naturalistic settings.
- **Control game efficiency often underreported:** Some studies lack explicit reporting of baseline efficiency without punishment, complicating quantitative prediction of the delta from punishment.

In sum, this literature is moderately supportive of the downstream prediction task—especially for standard design dimensions and control conditions close to those reported in the more central PGG experiments and theory—but leaves gaps for some design features and when extrapolating to less-standard settings or population behaviors. Predictions should account for the wide context- and parameter-dependence of punishment's efficiency effects described in this evidence base.
