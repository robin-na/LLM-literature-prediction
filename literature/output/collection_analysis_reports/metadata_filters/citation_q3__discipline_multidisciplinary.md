# 1) Evidence Base

The paper set is both **large** and **diverse** (121 papers), covering a broad range of empirical lab experiments, observational studies, and theoretical/simulation modeling. For the core domain of repeated public goods games (PGGs), the evidence includes:

- **Numerous high-quality empirical lab experiments** directly measuring both contribution/cooperation and payoff-based efficiency under punishment and control (e.g., Simpson et al., 2017; Chaudhuri & Paichayontvijit, 2017; Dong et al., 2016; Fehl et al., 2012).
- **Strong theoretical and modeling papers** tracking average payoff/welfare as a function of punishment parameters and game design (e.g., Salahshour, 2021; Wang et al., 2024; García & Traulsen, 2012, 2019; Ohdaira, 2022).
- **Close and adjacent variants** (threshold, snowdrift games, step-level, innovation races, prisoner's dilemma, exclusion/ostracism) with relevance to mechanisms and moderators for generalization.

Coverage is **narrowly focused and exact** for standard repeated PGGs with and without punishment, especially regarding core dimensions like player count, rounds, MPCR, punishment cost/tech. There is also **substantial adjacent and contextual coverage** regarding different types of punishment (peer, pool, third-party, ostracism/exclusion), mechanism design, and alternative intervention (reward, restorative justice, negotiation/commitment, reputation).

While most empirical work measures contributions or cooperation, a significant subset directly or indirectly measures efficiency, group payoff, or welfare outcomes. Thus, the base offers a **rich, multi-method triangulation** for the prediction task, with some dimensions (notably rare or complex game features) less explored.

---

# 2) Task Relevance

**a) `pgg_or_variant`**

- **Exact relevance**: Many papers directly examine (linear or threshold) repeated public goods games with real payoff structures (Simpson et al., 2017; Ozono et al., 2020; Chaudhuri & Paichayontvijit, 2017; Dong et al., 2016).
- **Close relevance**: Some theoretical work uses variants (step-level, snowdrift, voluntary participation, network/public goods integration) that maintain core PGG mechanisms and are justified for extrapolation (Jiang et al., 2013; Ozono et al., 2016).
- **Adjacent relevance**: A moderate number work with two-player PD or exclusion as sanctions or model the same underlying cooperation dilemma but not PGG per se.

**b) `punishment_or_sanctions`**

- **Exact relevance**: Many studies manipulate peer (and sometimes institutional) punishment as a switchable game feature, enabling direct estimation of punishment effect on outcomes (Simpson et al., 2017; Ozono et al., 2020; Chaudhuri & Paichayontvijit, 2017).
- **Close relevance**: Some model variants (ostracism, exclusion, moral judgment, leader punishment, probabilistic punishment, collective punishment) or analyze the effect of different forms of sanction (Ozono et al., 2016; Nakamaru & Yokoyama, 2014).
- **Adjacent/weak**: Others focus on alternate forms (restorative justice, third-party punishment in non-PGG games) or discuss punishment only as context.

**c) `efficiency_or_related_payoff_outcome`**

- **Exact relevance**: A notable portion directly reports group efficiency or mean payoff with and without punishment, as ratios to the social optimum (Simpson et al., 2017; Chaudhuri & Paichayontvijit, 2017; Dong et al., 2016).
- **Close relevance**: Many closely related studies measure group payoff, total earnings, or welfare—clear proxies for efficiency—even when not normalized to maximum possible (Hetzer & Sornette, 2013).
- **Adjacent**: The majority of theory papers report behavior, cooperation, or equilibrium frequencies but allow mapping to expected group payoffs. Some experiments focus exclusively on cooperation, punishment rate, or norm compliance, and not directly on efficiency.

---

# 3) Outcomes Measured In The Literature

- **Payoff-based outcomes (high relevance):**
    - **Group efficiency (ratio of actual to maximum payoff):** Explicitly reported in key papers (Simpson et al., 2017; Chaudhuri & Paichayontvijit, 2017; Ozono et al., 2020).
    - **Total group payoff/mean individual earnings/welfare/surplus:** Frequently measured, often compared across punishment and no-punishment treatments (Dong et al., 2016; Hetzer & Sornette, 2013).
- **Non-payoff behavioral outcomes (supporting, not substitutive):**
    - **Contribution or cooperation rate, frequency of punishment/reward, punishment targeting, behavioral motifs (retaliation, second-order punishment):** Almost universally reported. These are informative for mechanism understanding but not equivalent to efficiency.
    - **Norm compliance, strategy frequencies, retaliation/vendettas:** Widely covered, especially in lab and simulation studies.
- **Other/group-structural outcomes:**
    - **Inequality (Gini), group composition stability, learning dynamics:** Adjacent to efficiency, reported in some network or mechanism studies (Tsvetkova et al., 2018; Dong et al., 2016).

---

# 4) Main Findings Relevant To Prediction

## General Effects:
- **Enabling peer punishment in standard repeated PGGs usually increases cooperation/contribution, but this does not translate into higher efficiency unless punishment is cost-effective.** Costs of administering punishment frequently offset or even outweigh the gains from higher cooperation, especially if punishment is used retaliatorily or excessively (Simpson et al., 2017; Fehl et al., 2012; Ozono et al., 2017).
- **Costless sanctions (moral judgment, approval, or ostracism) tend to achieve both higher cooperation and higher efficiency than costly material punishment:** When explicit monetary costs are minimized, group payoffs increase above control (Simpson et al., 2017; Nakamaru & Yokoyama, 2014).

## Moderators and Design Factors:
- **Alignment of incentives:** Punishment increases efficiency mainly when local and global welfare incentives are aligned. When cooperation benefits the broader group but not local individuals, punishment is less effective or even harmful (Ozono et al., 2020).
- **Cost and effectiveness of punishment:** High-cost, low-impact punishment often reduces efficiency. Conversely, optimal cost/impact regimes (theoretical models often specify thresholds) can allow punishment to increase efficiency if antisocial punishment is kept low (Salahshour, 2021; Wang et al., 2024).
- **Game parameters and structure:**
    - **Number of rounds:** Efficiency gains from punishment tend to be delayed; short games may see net loss due to initial high punishment costs, while long games allow learning and efficiency to recover (Chaudhuri & Paichayontvijit, 2017).
    - **Group size (player_count):** In small groups, targeted peer punishment can sometimes increase efficiency; in larger or less structured groups, collective action problems for punishing (diffusion of responsibility) can arise.
    - **MPCR (marginal per-capita return):** Higher MPCR favors the evolution of efficient punishment-cooperation equilibria (Salahshour, 2021; Wang et al., 2024).
    - **Observation, information, and population structure:** Efficiency gains depend on the observability of punishment institutions, ability to coordinate, and presence of anti-social punishment (García & Traulsen, 2019; Wang et al., 2024).
- **Dynamics and learning:** Retaliation cycles (vendettas) are a major risk where identities or prior punishment are known (Fehl et al., 2012). In environments with "credit assignment" problems (delay between defection and consequences), punishment accelerates learning and increases efficiency (Köster et al., 2022).

## Comparative Interventions:
- **Reward mechanisms generally outperform punishment for efficiency:** Both theoretically and empirically, reward produces equal or higher group payoffs/social welfare for the same resource expenditure, unless very specific environmental risks make strong punishment optimal (Han et al., 2024; Dong et al., 2016).
- **Combined punishment and reward or contextual interventions (moral appeals, negotiation/commitment, restorative justice) can produce higher efficiency than punishment alone.**

---

# 5) Prediction Guidance

- **The literature robustly supports that the effect of enabling punishment on group efficiency depends critically on game design and baseline efficiency without punishment. Prediction is highly context-sensitive, not monotonic.**
    - If **control efficiency is already high**, adding punishment (especially with material cost) does *not* increase and may reduce group efficiency due to wasted resources (Simpson et al., 2017; Jiang et al., 2013). Mild or costless sanctions may help, but severe or costly punishment may actually suppress efficiency.
    - If **control efficiency is low** (cooperation rare/defection prevalent), properly designed and moderate-cost punishment can increase group efficiency, provided retaliation cycles and antisocial punishment are managed (Dong et al., 2016; Wang et al., 2024; Salahshour, 2021).
- **For the 14 prediction dimensions**, use direct evidence for: player count, rounds, MPCR, punishment cost/magnitude/tech, all-or-nothing vs. continuous contributions, chat (communication allowed), observability (identity display, visibility of outcomes), reward existence, and information display.**
    - Design regimes with *low-cost, effective*, and *prosocially targeted* punishment have the best chance of raising efficiency.
    - Designs enabling **easy retaliation, costly punishment, high anti-social punishment, or severe misalignment of incentives** are likely to see little or negative efficiency effects.
- **Baselines matter:** The *difference* between control and treatment matters as much as absolute values. Where control is highly inefficient, punishment effects on efficiency tend to be larger.
- **Empirical findings from exact PGGs are preferred for direct prediction; other designs/theory are best for mechanism or extrapolation to rarely-studied parameter ranges.**
- **Caveat:** Many results about punishment increasing cooperation do **not translate directly** into efficiency gains. Predictors tuned only on contribution data are likely to overstate efficiency in punishment-enabled treatments.

---

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**
- `player_count`, `num_rounds`, `mpcr`, `punishment_cost`, `punishment_tech`, `all_or_nothing` (and by extension, continuous-contribution framing): Routinely manipulated and analyzed for their moderating effects.
- `reward_exists`, `reward_cost`, `reward_tech`: Examined in papers comparing reward and punishment; strong evidence on their distinct or additive effects.
- `chat`: Covered in empirical experiments examining the effect of communication.
- `show_punishment_id`: Some studies explicitly manipulate the anonymity/visibility of punishment (important for retaliation and vendetta risk).

**Indirectly Informed:**
- `show_other_summaries`, `show_n_rounds`: Sometimes varied; information structure generally recognized as a moderator, but direct evidence is less common.
- `default_contrib`: Framing studies occasionally address this (opt-in vs. opt-out), but direct efficiency effects of default are less frequently reported.

**Only Contextually Discussed:**
- `all_or_nothing`: Terminology overlaps with continuous contributions; not all papers explicitly separate the two.
- `reward_exists`, `reward_cost`, `reward_tech`: When not the main focus, these may only be described as background, but not systematically varied.

**Missing or Sparse:**
- Some rare or combined features (e.g., complex reward schemes, asynchronous exclusion, third-party vs. peer punishment, networked PGGs, very large groups) are underrepresented or only modeled theoretically.
- Rich-metadata (e.g., precise information displays, complex identity conditions, high default contributions) are less commonly the focus of direct efficiency measurement.

---

# 7) Important Limitations

- **Efficiency is not always reported, or is inferred from behavioral proxies:** Many studies default to measuring contributions/cooperation; the translation from contributions to efficiency requires careful attention to punishment/reward costs, which are sometimes substantial.
- **Retaliation cycles and anti-social punishment are under-addressed in forecasting efficiency:** Evidence shows that under some conditions, vendettas or anti-social punishment (punishing cooperators) can lead to efficiency loss, but not all studies provide data on the prevalence or size of these effects.
- **Theory and simulation results depend strongly on modeling choices:** Evolutionary models, assumptions about mutation structure, observability, and learning can lead to opposite predictions about whether punishment increases or decreases efficiency (García & Traulsen, 2012, 2019).
- **Empirical coverage is broad but not exhaustive across the full range of game design dimensions:** Novel features, high dimension interactions, very large or very small groups, and rare/realistic informational environments are less represented.
- **Population and context matters:** Results from small-N, highly controlled lab settings may not fully capture group heterogeneity, dynamics, or endogeneity present in field or larger-scale environments (network effects, endogenous leadership, group fluidity).
- **Non-PGG and adjacent game forms are informative but not strictly generalizable:** Care must be taken when drawing on models or results from threshold games, innovation races, exclusion/ostracism, or PD/UG settings.

---

**In summary:**  
The literature provides a strong and nuanced base for predicting the effect of enabling punishment on group efficiency in PGG-like games, especially for standard laboratory PGGs with typical parameter regimes. Predictive accuracy is highest when control efficiency, punishment cost/effectiveness parameters, and group structure match those of well-studied conditions. Efficiency effects of punishment are: (1) dependent on cost-benefit balance, (2) not reliably positive, and (3) subject to important moderators such as incentive alignment, possibility of retaliation, institution integrity, and population structure. Modelers and forecasters should not conflate increases in cooperation or punishment frequency with gains in efficiency. Context- and design-specific adjustment is mandatory.
