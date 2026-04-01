# 1) Evidence Base

The paper set consists of 14 papers, with a mix of empirical (laboratory experiments) and theoretical (evolutionary/game-theoretic, conceptual) work. Only a few papers report direct experimental findings from public goods games (PGGs) with and without punishment, while most of the set provides theoretical arguments, mechanism discussions, or evidence from adjacent game types and environments. Thematically, the literature is broad, spanning classic PGGs, governance scenarios, networked dilemmas, evolutionary and moral philosophy perspectives, reputation systems, and analogues (e.g., queueing, Ultimatum Game). In aggregate, direct empirical evidence for the specific downstream prediction task—especially for efficiency effects of enabling peer punishment in PGG-like environments—is limited, but conceptual and mechanism-based coverage is rich.

# 2) Task Relevance

**pgg_or_variant**  
- **exact:** A minority of papers deliver direct relevance by focusing on standard public goods games or their close variants (Eisenberg & Engel, 2014; Quan et al., 2023; Bell et al., 2016).  
- **close:** Some theoretical papers (e.g., Zhang & van der Schaar, 2013; Li & Jiang, 2023) involve PGG-like repeated multiplayer games with similar strategic properties.  
- **adjacent / weak:** Many papers analyze only adjacent dilemmas (e.g., networked prisoners’ dilemma, Ultimatum Game, collective-risk games) or discuss norm enforcement in analogous real-world situations (queues, environmental management, group hunting).  
- **none:** One paper (Fagundes, 2017) uses PGG experiments only for mechanism context without formal modeling or new data.

**punishment_or_sanctions**  
- **exact:** Several papers directly manipulate or model peer punishment or formal sanctioning in the context of group contributions (Eisenberg & Engel, 2014; Quan et al., 2023; Bell et al., 2016).  
- **close/adjacent:** Many discuss punishment mechanisms more generally or outside the exact PGG lab, including reputation-based and evolutionary forms, or penalties/rewards in governance settings (Li & Jiang, 2023; Sripada, 2005; Sterelny, 2016; Nakao & Machery, 2012).  
- **none:** Some papers provide only context or motivation without systematic analysis of punishment.

**efficiency_or_related_payoff_outcome**  
- **exact:** Only a few papers (Zhang & van der Schaar, 2013; Li & Jiang, 2023; Eisenberg & Engel, 2014) explicitly measure or model group efficiency or total welfare as their key outcome.
- **close:** Some analyze group payoffs, surplus, or welfare as part of mechanism design simulations.
- **adjacent/weak:** Most report behavioral proxies (contribution rate, cooperation) and infer potential efficiency effects, but do not quantify them.
- **none:** Several papers focus strictly on changes in cooperation or norm compliance without analyzing payoffs.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes:**  
- Group efficiency, total payoff, surplus, or welfare are the primary outcome in only a subset of the literature (Eisenberg & Engel, 2014; Zhang & van der Schaar, 2013; Li & Jiang, 2023), often via simulation or formulaic calculation.
- Many studies reference payoffs as mechanism context but do not report efficiency statistics.
- Some experimental studies mention decay or stability of group payoff qualitatively, without direct efficiency measures.

**Non-payoff behavioral outcomes:**  
- Most theory and experimental papers focus on contribution rates, cooperation densities, norm compliance, punishment frequency, and emotional responses.
- Findings about increased cooperation, deterrence of free-riding, and norm observance dominate the set (Quan et al., 2023; Bell et al., 2016; Sripada, 2005).
- Some studies dwell on punishment occurrence or its psychological motivations (e.g., fairness, norm robustness).

**Distinction:**  
- The corpus is much stronger on behavioral (non-payoff) outcomes than quantitative efficiency or total payoff effects. Payoff-based outcome data is sparse.

# 4) Main Findings Relevant To Prediction

Synthesizing across the most relevant empirical and theoretical papers:

- **Enabling punishment typically increases cooperation and can substantially boost group efficiency compared to no-punishment control, but only when the punishment regime is well-calibrated in terms of severity, likelihood, and cost-to-effect ratio.** Severe or group-harm-based penalties were more effective than mild or self-interested punishments (Eisenberg & Engel, 2014).

- **Behavioral mechanisms:** The deterrent effect is a product of actual punishment experienced, not just the threat or option of punishment (Eisenberg & Engel, 2014). Graded or reputation-based punishment schemes are often more robust in sustaining high cooperation, particularly in repeated or networked interactions (Quan et al., 2023; Zhang & van der Schaar, 2013).

- **Boundary conditions:** Punishment increases cooperation (and, sometimes, efficiency) only when the cost to punishers is not prohibitively high or the initial punishment probability is not too low (Quan et al., 2023; Sripada, 2005). Overly severe or costly punishment regimes may have perverse effects or discourage contribution.

- **Limits to efficiency increase:** Some evidence (Li & Jiang, 2023) indicates that punishment alone may be insufficient—combinations of sanctions and rewards or supporting governance mechanisms yield the highest efficiency gains, especially in complex, real-world applications.
  
- **Indirection in behavior-payoff translation:** Several papers caution that increased cooperation does not always translate straightforwardly into efficiency gains, due to possible over-punishment, excessive cost of sanctions, or side effects such as meta-punishment or increased free-riding (Bell et al., 2016; Nakao & Machery, 2012).

- **Empirical ambiguity:** Some experimental results show punishment boosts cooperation but also increases free riding among certain subgroups, leading to ambiguous predictions for net efficiency (Bell et al., 2016).

# 5) Prediction Guidance

**Supported Guidance:**  
- Where baseline efficiency (control, no-punishment) is low due to decay or free-riding, *enabling well-calibrated peer punishment is highly likely to increase efficiency*, with the increase mediated by punishment severity, likelihood, and cost-benefit balance (Eisenberg & Engel, 2014; Quan et al., 2023).
- For games with repeated interaction, feedback about group outcomes, and endogenous (peer) punishment, observable improvements in efficiency are specifically tied to the experience of real, enforceable sanctions, and are *not* solely the result of the theoretical option to punish.

**Cautions:**  
- If punishment is costlier than the harm it deters, or is rarely applied, efficiency gains are limited or can even be negative (Quan et al., 2023).
- Improved behavioral compliance (cooperation rates) often, but not always, translates into higher efficiency; the translation can be undermined by increased sanctioning costs or misuse of punishment (Bell et al., 2016).
- In some networked or complex governance settings, *punishment must be paired with other incentives* (e.g., rewards, public performance appraisal) to be fully effective in improving group efficiency (Li & Jiang, 2023).

**Uncertainties:**  
- Most empirical and theoretical results are context-specific and parameter-dependent; quantitative predictions for treatment efficiency require close attention to punishment cost, severity, mode of administration, and other incentive features.
- The evidence base is thin for many variants of the 14 design dimensions, especially those involving communication, identity visibility, and reward mechanisms.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**  
- `player_count`, `num_rounds`, `all_or_nothing`, `mpcr`, `punishment_cost`, `punishment_tech`: Frequently included as experimental or model parameters, with direct discussion of their moderating effects on punishment success and efficiency (Eisenberg & Engel, 2014; Quan et al., 2023; Zhang & van der Schaar, 2013).
- `chat` (communication): Directly present in a few studies, especially in connection with increased cooperation under risk or negotiation scenarios (Bell et al., 2016; Hurlstone et al., 2017), but seldom mapped onto efficiency directly.

**Indirectly Informed or Contextual:**  
- `reward_exists`, `reward_cost`, `reward_tech`: Only contextually discussed; Li & Jiang (2023) note importance of reward mechanisms alongside punishment, but with little quantitative resolution.
- `show_other_summaries`, `show_n_rounds`, `default_contrib`, `show_punishment_id`: Occasionally referenced in mechanism discussions, but experimental data are minimal or absent.

**Effectively Missing:**  
- Quantitative evidence is especially sparse or absent for `default_contrib`, `reward_cost`, `reward_tech`, `show_other_summaries`, `show_n_rounds`, and `show_punishment_id`.
- Few papers systematically manipulate multiple dimensions simultaneously; most focus on punishment variables and group structure.

# 7) Important Limitations

- **Limited direct efficiency evidence:** Only a handful of papers measure or model group efficiency as a function of peer punishment; the rest infer effects from cooperation rates or behavioral indicators, which may diverge from actual payoff changes.
- **Parameter and regime specificity:** Findings on punishment effectiveness are highly contingent on the calibration of punishment cost, frequency, and severity. There is a lack of broad parameter sweep studies covering the full space of design dimensions relevant for prediction.
- **Scarce multi-factorial analyses:** Very few studies systematically test interactions among multiple design variables (e.g., communication × punishment × identity visibility), limiting the generalizability of effect estimates.
- **Contextual and external validity issues:** Many papers draw their conclusions from adjacent or loosely related environments (e.g., networked dilemmas, governance games, Ultimatum Game), raising concerns about direct applicability to standard PGGs.
- **Predominance of mechanism over outcome:** Much of the literature focuses on theoretical justification or mechanism description, rather than outcome data suitable for quantitative prediction.
- **Ambiguity in behavior-payoff linkage:** The translation from behavioral effects (increased cooperation) to actual efficiency outcomes is not always clear and may be contingent, especially when punishment is costly or misapplied.
- **Sparse attention to some design dimensions:** Many configuration variables relevant to the prediction task (particularly those relating to reward, default framing, and information) are rarely manipulated or analyzed in this literature set.

---

**In summary:**  
Direct experimental and model-based evidence from PGGs indicates a general efficiency boost under well-calibrated peer punishment, but the magnitude and reliability of the effect are sensitive to punishment regime details, incentive structure, and contextual moderators. While behavioral compliance increases are robustly linked to punishment mechanisms, their translation into efficiency gains is less systematically documented. Many key design dimensions affecting treatment efficiency remain under-explored in this literature set, and care is warranted when extrapolating findings to novel or multi-faceted environments.
