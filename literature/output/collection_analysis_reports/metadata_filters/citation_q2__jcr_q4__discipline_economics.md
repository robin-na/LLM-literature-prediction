# 1) Evidence Base

The paper set contains a mix of empirical laboratory and field experiments (majority), supported by a few theoretical papers. Empirical evidence focuses primarily on linear public goods games (PGG) or closely related social dilemmas, often with manipulations of institutional sanctions (punishment, reward, leader/centralized sanction), and sometimes includes contextually similar but structurally distinct games (e.g., bargaining, trust, or common-pool resource games). Theoretical work chiefly involves models of PGG or related games, emphasizing the role of punishment in supporting cooperation and efficiency.

Overall, the set is moderately broad in disciplinary coverage but somewhat narrow in its direct empirical focus on the exact prediction task (i.e., on payoff-based outcomes in classic PGG with peer punishment). Most empirical papers use standard lab game setups, enabling moderate generalizability to the prediction task, but field, network, bargaining, and CPR literatures are also represented. However, direct, high-relevance evidence (i.e., experimental PGG with explicit efficiency measured under both control and punishment-enabled treatments) is available in only a few papers; most studies either focus on non-payoff behavioral outcomes or on adjacent game structures.

# 2) Task Relevance

### pgg_or_variant
- **Exact:** Multiple papers (Kocher & Matzat, 2016; Castillo et al., 2021; Carpenter & Matthews, 2010) directly address standard or canonical variants of PGG.
- **Close/Adjacent:** Several empirical and theory studies use games with similar group structure and strategic dilemmas (all-or-nothing contribution, CPR, voting, bargaining), but depart from classic PGG structure (e.g., trust/minigame, split two-stage games).
- **Weak/None:** A few theoretical papers address network or Bayesian games, lacking central PGG features (Madeo & Mocenni, 2021; Forges et al., 2016).

### punishment_or_sanctions
- **Exact:** Most papers include explicit punishment mechanisms, focusing on peer or centralized punishment systems in social dilemmas.
- **Adjacent:** Some papers study reward or redistribution mechanisms only (Becchetti et al., 2018), or focus on non-monetary/indirect ("social feedback", Przepiorka & Diekmann, 2020).
- **Weak/None:** A minority (e.g., Madeo & Mocenni, 2021) discuss neither punishment nor sanctions.

### efficiency_or_related_payoff_outcome
- **Exact:** A minority of papers explicitly report **efficiency** or group payoff as a primary outcome (Kocher & Matzat, 2016; Castillo et al., 2021; Carpenter & Matthews, 2010; Przepiorka & Diekmann, 2020).
- **Close/Adjacent:** Some report surrogate or theoretically equivalent outcomes (e.g., welfare, surplus), or focus on behavioral proxies (catch, effort) closely related to group payoff.
- **Weak/None:** Most empirical studies focus on **non-payoff behavioral outcomes** (contributions, cooperation, punishment frequency), and/or operate in non-PGG environments (bargaining, trust games).

# 3) Outcomes Measured In The Literature

- **Payoff-related (directly measured):** 
    - Average group efficiency/profit relative to cooperative optimum (Kocher & Matzat, 2016; Castillo et al., 2021; Carpenter & Matthews, 2010; Przepiorka & Diekmann, 2020).
    - Group surplus/welfare, sometimes as modeled equilibrium outcomes.
- **Payoff-related (theoretical/surrogate):**
    - Nash equilibrium payoffs, joint plan efficiency (Forges et al., 2016).
    - Analytical/numerical comparison of average payoffs at equilibrium (Madeo & Mocenni, 2021).
- **Behavioral, non-payoff outcomes (most common):**
    - Contribution/cooperation rates, frequency and targets of punishment, cooperation decay, norm compliance, trustworthiness, revenge, offer fairness, use of sanctions or approval/disapproval mechanisms.

**Explicit distinction** is made in several digests between behavioral effects (e.g., increased contributions) and net payoff/efficiency (e.g., Kocher & Matzat, 2016; Abbink et al., 2004).

# 4) Main Findings Relevant To Prediction

- **Peer punishment tends to increase cooperation but often reduces efficiency in repeated linear PGG with standard peer-punishment design,** due to the direct costs of punishment outweighing the gains from increased contributions (Kocher & Matzat, 2016; Abbink et al., 2004). This effect is consistent in both experimental and some adjacent bargaining contexts.
- **Centralized punishment** (where a manager or leader has exclusive punishment rights) can **increase both contributions and efficiency,** sometimes substantially, especially when punishment is effective and counter-punishment is disabled or rare (Castillo et al., 2021; supported by theory in Carpenter & Matthews, 2010 for third-party punishment).
- **The cost and effectiveness of punishment** (punishment_cost, punishment_tech) matter: In peer sanction settings, higher costs or less effective punishment can exacerbate efficiency loss, while extremely effective punishment that deters free-riding might shift the net effect toward positive, though rarely achieved empirically (Kocher & Matzat, 2016; Carpenter & Matthews, 2010; Forges et al., 2016).
- **Reward institutions tend to be preferred and are more efficient** than punishment or standard VCM, even with lower leverage (Kocher & Matzat, 2016).
- **Field and CPR-type games provide mixed or negative evidence** on the generalizability of laboratory punishment effects: in some real-world social dilemmas, enabling peer punishment does not improve behavioral outcomes or efficiency proxies (Noussair et al., 2015).
- **Contextual moderators** (such as prior group corruption exposure, presence of counter-punishment, and social feedback mechanisms) can alter the effect of punishment, often diminishing its effectiveness for increasing either cooperation or efficiency (Campos-Vazquez & Mejia, 2016; Przepiorka & Diekmann, 2020).

# 5) Prediction Guidance

- For **standard linear PGGs**, **enabling peer punishment is likely to decrease group efficiency** relative to control (punishment disabled) **under most conditions**, because while punishments boost contributions, their costs more than offset these gains (Kocher & Matzat, 2016). Predict treatment efficiency as typically *lower* than control by a margin reflecting average punishment cost rates, especially when punishment is neither extremely rare nor fully deterrent.
- **Centralized (manager/third-party) punishment, when effective and not subject to counter-punishment, should be expected to increase efficiency** compared to control, largely independent of the manager selection mechanism, and robust to tested punishment costs and technologies (Castillo et al., 2021; Carpenter & Matthews, 2010). Predict efficiency as higher with such centralized punishment enabled, unless starting from a very low-efficiency baseline (Carpenter & Matthews, 2010).
- When **reward and punishment are both available**, reward-only institutions appear to yield higher efficiency than those allowing punishment or both (Kocher & Matzat, 2016). Predict reward-enabled treatments as highest in efficiency, punishment-enabled as lowest, control/VCM intermediate.
- **Behavioral outcomes** (contributions, cooperation rates) are unreliable proxies for efficiency: Many papers show contributions rise but efficiency falls with punishment, so direct efficiency outcomes should guide prediction, not behavioral surrogates.
- **In field/CPR settings or settings with counter-punishment or corruption exposure,** do not assume positive efficiency effects from punishment; may be zero or negative, especially when punishment is peer-based and not highly targeted (Noussair et al., 2015; Campos-Vazquez & Mejia, 2016).

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed (Multiple Papers):**
- `player_count`: Manipulated across studies, from 2–10.
- `num_rounds`: Standard in lab (5–20), tested for stability and decay effects.
- `mpcr`: Explicitly specified in high-relevance studies; theoretical implications from equilibrium analysis.
- `punishment_cost`: Directly manipulated in both lab and theory.
- `punishment_tech` (effectiveness/magnitude): Varied in lab and modeled in theory.
- `all_or_nothing`: Both continuous and all-or-nothing variants tested.
- `chat`: Typically disabled; communicative effects weakly addressed.
- `reward_exists`: Contrasted with punishment in several studies.

**Indirectly Discussed/Partial Coverage:**
- `show_other_summaries` and `show_n_rounds`: Feedback/readout conditions examined in social feedback and CPR studies.
- `show_punishment_id`: Addressed in some feedback/social sanction contexts.

**Sparse/Missing:**
- `default_contrib`: Rarely specified as explicit design manipulation.
- `reward_cost`, `reward_tech`: Partially addressed, mostly in reward-enabled treatments.
- **No studies directly manipulate or systematically analyze all 14 dimensions simultaneously.**
- Interactions across dimensions (e.g., combined effects of `chat` and `punishment_cost`) are rarely tested outside specific studies.

# 7) Important Limitations

- **Limited direct empirical evidence** on efficiency in peer-punishment-enabled linear PGGs: Only a subset of papers report direct efficiency measures; others focus on behavioral proxies or adjacent games.
- **External validity is mixed:** Field or contextually realistic social dilemma games often do not reproduce the efficiency or behavioral effects observed in laboratory PGGs; predictions based on lab data may not generalize (Noussair et al., 2015).
- **Dimensional sparseness:** Most design dimensions are not systematically or independently manipulated; thus, predictions about the combined or interactive effects of multiple design dimensions are uncertain.
- **No direct evidence for certain prediction dimensions:** Some dimensions relevant to the downstream task (e.g., `default_contrib`, full feedback conditions, nuances of rewards/punishments) are understudied.
- **Behavioral vs. efficiency outcomes:** Many findings about cooperation/contribution do not translate to efficiency outcomes, which can be misleading if used for direct payoff predictions.
- **Ambiguity and boundary conditions:** The effect of enabling punishment on efficiency can reverse (positive to negative) depending on whether the institutional design is centralized or peer-based, on the prevalence of free-riders in the control, and on the precise cost/effectiveness parameters; theoretical results depend on initial conditions and assumptions not always met empirically (Carpenter & Matthews, 2010).
- **Scarcity of robust cross-game extrapolation:** Most evidence is context- and design-dependent, making broad generalizations hazardous without matching the prediction setting closely to studied parameter ranges.

---

### **Summary Table: Relevance of Paper Set to Prediction Dimensions**

| Dimension                | Evidence Type     | Strength of Evidence                |
|--------------------------|------------------|-------------------------------------|
| player_count             | Empirical/Theory | Direct, moderate coverage           |
| num_rounds               | Empirical/Theory | Direct, moderate coverage           |
| chat                     | Empirical        | Direct/Indirect, weak coverage      |
| all_or_nothing           | Empirical/Theory | Direct, moderate coverage           |
| default_contrib          | Empirical        | Indirect/contextual, sparse         |
| mpcr                     | Empirical/Theory | Direct, moderate coverage           |
| punishment_cost          | Empirical/Theory | Direct, moderate coverage           |
| punishment_tech          | Empirical/Theory | Direct/indirect, moderate coverage  |
| reward_exists            | Empirical        | Direct, moderate in reward studies  |
| reward_cost/tech         | Empirical        | Indirect, sparse                    |
| show_n_rounds            | Empirical        | Indirect, limited coverage          |
| show_other_summaries     | Empirical        | Indirect, moderate in feedback      |
| show_punishment_id       | Empirical        | Indirect, limited                   |

**Overall:** The literature set provides moderate direct empirical and theoretical support for a subset of prediction dimensions relevant to efficiency effects of punishment in PGG-like environments, but is limited by incomplete dimensional coverage, predominance of behavioral outcomes, and context-dependent findings. Predictions based on this literature should foreground peer versus centralized punishment, the baseline (control) efficiency, and the costs and effectiveness of the punishment mechanism.
