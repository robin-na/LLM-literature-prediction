# 1) Evidence Base

The literature base is extensive (470 papers) and covers experimental, observational, and theoretical research. For the prediction task—forecasting treatment efficiency in PGG-like environments as a function of design and control efficiency—much of the highest-relevance evidence comes from empirical lab experiments and formal models focused directly on public goods games (PGGs) with and without peer punishment. The core papers supply rich payoff/efficiency outcomes in canonical PGGs and major variants, often explicitly reporting group earnings, efficiency ratios, or comparative outcomes for control (no punishment) vs. treatment (punishment enabled) conditions.

A smaller but important set of papers addresses common variants (e.g., threshold public goods, collective-risk dilemmas, contests, leader/centralized punishment, optional participation, reward co-enabled). There is significant work on the mechanistic and context-specific moderators of punishment's effectiveness (cost-effectiveness, antisocial/corruptible punishment, population structure, group identity, and more).

Some papers are strictly theoretical, focusing on evolutionary models, phase diagrams, or mechanism arguments; many of these are validated by simulation or by reference to experimental findings.

A large remainder of the literature is adjacent: it explores related games (e.g., PD, dictator, trust, ultimatum), non-payoff behavioral outcomes, or institutional/psychological context without reporting efficiency or group payoff. These provide important context and moderator insights but less direct guidance for quantitative efficiency prediction.

**Strengths:**  
- Multiple high-quality, high-relevance experimental and modeling papers mapping punishment effects on efficiency/earnings from standard/control to treatment conditions.
- Well-specified manipulation of key game design dimensions such as player count, rounds, MPCR, punishment cost/tech, group structure, and information features.
- Rich reporting of settings where punishment backfires, is neutral, or positive for efficiency.

**Limitations:**  
- Despite breadth, many papers report solely behavioral outcomes (contribution, norm compliance, punishment rates) rather than efficiency/payoff.
- Certain design dimensions (chat, default contribution, feedback visibility, identification of punishers/rewarders) are only sporadically addressed.
- Some results hinge on context (cultural, social, or psychological moderators) not included in the prediction model.
- Adjacent or weakly related evidence is abundant but doesn't directly support the downstream prediction task.

---

# 2) Task Relevance

## pgg_or_variant

- **Relevance:** Most direct evidence comes from studies labeled as `pgg=exact`, involving classic linear or threshold PGGs. There is also substantial coverage of close variants (CRD, stag-hunt, contests, repeated dyadic games, resource dilemmas).
- **Coverage:** exact (for core experiments); close/adjacent (for extensions, ecological or institutional variants); weak/none (many psychological/field/sociological studies).
  
## punishment_or_sanctions

- **Relevance:** Many papers manipulate or model `punishment=exact` (peer punishment, leader/central, third-party, implicit/explicit sanctions) with clear documentation of sanctioning regime, cost, impact, and rules of engagement. Adjacent coverage: exclusion, reward, indirect punishment, or social-network sanctions.
- **Coverage:** exact (canonical peer punishment and variants); close (institutional, indirect, or exclusionary mechanisms); adjacent/weak (moral judgments, costless sanctions, reputational effects, etc.).
  
## efficiency_or_related_payoff_outcome

- **Relevance:** The high-relevance subset reports `payoff=exact` (earnings, group payoff, group efficiency relative to optimum, surplus). Many only report non-payoff behavioral measures (contributions, punishment frequencies).
- **Coverage:** exact (papers with efficiency/group payoff as a primary outcome); close/adjacent (papers with related group welfare, surplus); weak/none (behavioral or norm-only outcomes).
  
**Summary:** There is broad and deep direct relevance for most core game parameterizations (standard repeated PGGs with/without peer punishment) and their efficiency outcomes, but less for variants with complex additional treatments or for dimensions rarely manipulated in experimental designs.

---

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes:**
- Group efficiency (group payoff as a fraction of maximum possible/cooperative group payoff)
- Mean/aggregate earnings
- Welfare/surplus created
- Success rates (in threshold/collective-risk games)
- Total resources remaining or generated

**Non-Payoff Behavioral Outcomes (not strictly efficiency):**
- Contribution rates (individual or group)
- Punishment/reward frequencies, targeting, and intensity
- Norm compliance, conformity
- Trust, trustworthiness, cooperation rate
- Emotional responses (anger, guilt), norm perceptions, reputation dynamics
- Ostracism or exclusion rates
- Inequality, distributional outcomes

**Distinction:**  
Many papers only report behavioral or psychological outcomes; payoff/efficiency effects must not be inferred from these alone unless data supporting the link are shown (e.g., if a study finds increased contributions but also substantial punishment costs, net efficiency may not rise).

---

# 4) Main Findings Relevant To Prediction

**General Trends:**
- **Canonical, repeated, fixed-group PGGs:** Enabling peer punishment (with standard linear costs and impact) usually increases efficiency/earnings substantially, moving the group from low-baseline (control) levels toward the cooperative optimum—*if* punishment is pro-social and mechanisms prevent substantial antisocial punishment or escalation/counter-punishment (Fehr & Gächter 2002; Gächter et al., 2017; Gürerk et al., 2006; Lo Iacono et al., 2023; Eriksson & Strimling, 2012; Rockenbach & Milinski, 2006).
- **Punishment cost/impact ratio:** The relative efficiency boost is greatest when punishment is highly effective (high impact per unit cost) and declines or reverses if punishment is costly or ineffective (Wu et al., 2016; Zefferman, 2023; Barrett, 2016; Ezeigbo, 2017).
- **Antisocial/retaliatory punishment or corruption:** The efficiency effect is diminished or negative in environments prone to antisocial punishment, cycles of retaliation (vendettas), or institutional corruption (Herrmann et al., 2008; Salahshour et al., 2022; Muthukrishna et al., 2017; Lee et al., 2019).
- **Control efficiency as a moderator:** If the control (no punishment) game already achieves high efficiency (typically at MPCR ≳ 0.5 or with reputation/communication), adding punishment yields little or no additional efficiency increase (Rand et al., 2009; Jiang et al., 2013; Lohse & Waichman, 2020).
- **Alignment with social optimum:** When cooperation itself is inefficient (MPCR < 1/n), enabling punishment can enforce 'bad' norms, raising contributions but reducing efficiency (Abbink et al., 2017; Kamijo et al., 2020).
- **Reward vs. punishment:** Enabling reward (especially cost-effective, budget-balanced, or endogenous) usually increases efficiency as much or more than punishment, and combining both can yield the highest net payoff (Rand et al., 2009; Ozono et al., 2020; Chaudhuri & Paichayontvijit, 2017). Punishment is rarely superior for efficiency unless cooperation is otherwise hard to achieve.
- **Role of communication, norm-signaling:** Communication, explicit norm-signaling, or reputation-based interventions often substitute or complement punishment, achieving high efficiency with lower costs (Andrighetto et al., 2013; Rockenbach & Milinski, 2006).
- **Noisy punishment (stochastic impact):** Noise in punishment (unpredictability about punishment's effect) robustly reduces efficiency, often drastically, due to increased undeserved, antisocial, or misdirected punishment (Salahshour et al., 2022; van Miltenburg et al., 2017).
- **Centralized/leader punishment vs. peer:** Centralized or delegated punishment often yields higher efficiency than decentralized peer punishment, especially if the leader is prosocial and institution is robust (Gross et al., 2016; Harrell, 2019; Hilbe et al., 2014; Ozono et al., 2016).
- **Second-order free rider problem:** Institutional punishment schemes must address non-contributors to punishment (second-order free riders) to be sustainable and efficient (Perc, 2012; Hilbe et al., 2014).
- **Optional participation/exclusion:** Efficiency gains from punishment are highest in games with voluntary participation or exclusion options (Hauert et al., 2007; Sasaki et al., 2012; Nakamaru & Yokoyama, 2014). Costless exclusion often outperforms costly punishment for efficiency.
- **Group composition and structure:** Heterogeneous groups (mixed social types, cultural background) and larger groups increase the risk of discriminatory or antisocial punishment, reducing efficiency (Molenmaker et al., 2023; Alexander & Christia, 2011); homogeneous groups benefit more from punishment.
- **Structured/population/network effects:** The effectiveness and efficiency of punishment can depend on spatial/network structure, with some graph topologies supporting higher efficiency gains from punishment (Wang et al., 2024; Bodnar & Salathé, 2012; Galan et al., 2011).

---

# 5) Prediction Guidance

- **Directly mapped prediction:** When predicting efficiency in a repeated, small-group, continuous-contribution PGG with peer punishment, use baseline/control efficiency plus game parameters (player_count, num_rounds, MPCR, punishment_cost/tech). Expect substantial efficiency gains from enabling punishment if baseline efficiency is low and punishment is cost-effective, pro-social, and well-targeted.
- **Key positive moderators:** High MPCR, low punishment cost, high punishment impact, group homogeneity, absence of antisocial/corrupt motives, effective feedback/information, restricted opportunity for retaliation, norm-signaling or reputation support.
- **Neutral or negative moderators:** High baseline efficiency (e.g., due to high MPCR, communication, or reward already enabled), costly or noisy punishment, group heterogeneity (cultural, social), presence of antisocial or retaliatory punishment, institutional corruption, or the possibility of 'bad norm' punishment.
- **Threshold, collective-risk, or contest variants:** Efficiency effects depend on whether the game is locally or globally efficient, and whether the punishment increases net group success or only increases costly enforcement (Ozono et al., 2020; Bravo & Squazzoni, 2013).
- **Reward vs. punishment:** If reward is available and cost-effective, expect equal or higher efficiency than for punishment, except possibly when baseline cooperation is very low and only punishment can deter persistent free riding.
- **Control efficiency is not always a reliable predictor:** If the control game is already near-optimal, punishment yields little—except in cases of anti-social or misaligned norms, where punishment may decrease efficiency.
- **Out-of-sample variants:** For less-standard PGGs (e.g., with communication, endogenous institution choice, or spatial structure), adjust expectations based on applicable evidence of how these dimensions interact with punishment.
- **Absence or negative effect:** In some environments, adding punishment may decrease efficiency—when punishment is used for rivalry, antisocial motives, or when it triggers vendettas or cycles of counter-punishment (Herrmann et al., 2008; Janssen et al., 2010; Gross & De Dreu, 2019).

---

# 6) Design Dimensions Highlighted Across Papers

**Directly informed:**
- `player_count`: Frequently manipulated (groups of 2–12+); group size shown as a key moderator for punishment's efficiency effect.
- `num_rounds`: Numbers of rounds systematically varied; long- vs. short-horizon effects on both cooperation stability and punishment cost-benefit.
- `mpcr`: Extensively varied; central to the efficiency benefit of punishment—positive returns are necessary for punishment to be efficiency-enhancing.
- `punishment_cost` & `punishment_tech`: Cost-to-impact ratios and punishment structure (peer, pool, automatic, stochastic) are central moderators of efficiency effects.
- `all_or_nothing` (binary vs. continuous contributions): Standard linear and binary versions; impacts cooperation dynamics and punishment frequency.
- `reward_exists` (and reward_cost, reward_tech): Co-enabled reward/punishment conditions studied; reward often produces higher efficiency.
- `show_n_rounds`, `show_other_summaries`: Feedback and information about rounds and others' actions extensively tested as moderators.
  
**Indirectly/conceptually discussed:**
- `default_contrib`: Framing effects sometimes studied, but less central for efficiency than MPCR or punishment cost/tech.
- `show_punishment_id`: Identification of punishers tested in some studies; anonymity often reduces efficiency as antisocial punishment rises.
- `chat`: Communication tested as an alternative/enhancer to punishment; interaction with punishment is a significant moderator.
  
**Only contextually addressed or sparse:**
- `show_other_summaries`: Some evidence on detailed feedback and its impact.
- `show_punishment_id`: Limited but suggestive evidence; identification may decrease antisocial punishment.
- Interactions across multiple less-standardized dimensions often remain underexplored (e.g., the joint effect of chat and identity feedback).

**Effectively missing:**
- Systematic manipulation of all 14 prediction dimensions in a single design is rare.
- Effect of `default_contrib`, rare forms of feedback (e.g., reputation spillover, indirect peer exclusion vs. punishment), or highly complex feedback structures is infrequently studied with payoff outcomes.

---

# 7) Important Limitations

- **Behavioral outcome/efficiency mismatch:** A majority of studies focus on behavioral responses (e.g., increased contribution) without reporting net group payoff or efficiency, leaving open the possibility of cases where cooperation rises but net efficiency does not (due to punishment costs, antisocial punishment, or retaliation).
- **Limited full-dimensional coverage:** Very few studies simultaneously vary and report efficiency outcomes as a function of all 14 game design dimensions. Most cover a subset (most commonly player count, rounds, MPCR, and punishment cost/tech).
- **Context/moderator dependence:** Numerous studies identify context-specific moderators (culture, group composition, risk structure, possibility of corruption), but these are often not part of the prediction model; using general rules without accounting for context may lead to misprediction.
- **Control efficiency non-monotonicity:** High (optimal) control efficiency settings may see little or no gain—or even a decrease—from enabling punishment, making control efficiency alone an unreliable predictor in some designs.
- **Reward/alternate mechanism dominance:** In cases where reward, communication, or reputation is available, these mechanisms often outperform punishment for efficiency, and their interactions are incompletely characterized across all dimensions.
- **Ambiguity/unresolved cases:** Some studies conflict: punishment increases cooperation everywhere, but efficiency only under specific cost/impact and group structure regimes; evidence for the effect of punishment in large, dynamic, or field settings is sparse and sometimes contradictory.
- **Indirect evidence abound:** Many adjacent or weak-relevance papers offer context or mechanisms but cannot be used to support predictions about efficiency quantitatively.

---

**Summary:**  
While the literature provides strong, quantitative, and mechanistic support for predicting the effect of enabling punishment on efficiency in standard PGG-like laboratory settings—and identifies specific design dimensions and moderators that inform robust prediction—important limitations arise from incomplete coverage of all design dimensions, frequent reliance on non-payoff behavioral metrics, and numerous context-specific or adjacent findings that cannot be directly transferred to the precise efficiency prediction task. Care must be taken to restrict prediction to the empirical and theoretical boundaries established by the exact and close-relevance literature, and to preserve identified ambiguities and context dependencies.
