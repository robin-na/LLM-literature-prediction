# 1) Evidence Base

The paper set consists primarily of **empirical research**, mostly laboratory experiments, with a few field experiments and observational studies. There is a **notable emphasis on behavioral mechanisms**—such as punishment assignment, reaction to defection/norm violation, and social role dynamics—rather than direct measurement of group-level payoff or efficiency outcomes. Only a minority of papers report **efficiency or group payoff** as the central outcome, and even fewer do so in direct public goods game (PGG) contexts with controlled punishment treatments. The set is **broad in terms of species, settings, and behavioral focus**, but **narrow in directly supplying high-quality, quantitative evidence on the causal effect of punishment interventions on efficiency in PGGs with clear design mappings**. Where findings are most relevant, they often concern CPR (common-pool resource) games, trust games, or dyadic settings that are adjacent but not identical to standard multi-round PGGs.

# 2) Task Relevance

**pgg_or_variant**  
- **Exact relevance**: Only a handful of studies (e.g., Bone et al., 2014; Li et al., 2018; Frey, 2019) use canonical PGGs.
- **Close/Adjacent relevance**: Many studies use CPR games, trust games, ultimatum/dictator/minigame paradigms, or natural analogues (e.g., Gelcich et al., 2013; Javaid & Falk, 2015; Baum et al., 2012; Bshary & Grutter, 2005), providing informative context but not an exact structural match.
- **Coverage gaps**: Several papers are observational studies or use animal behavioral experiments without payoff/efficiency measurements, limiting direct relevance.

**punishment_or_sanctions**
- **Exact/Close relevance**: About half of the papers manipulate or measure punishment options directly, including both peer and third-party punishment, sometimes including external sanction regimes (e.g., Javaid & Falk, 2015; Gelcich et al., 2013).
- **Adjacent/Weak/None**: A number of studies mention punishment as a possible mechanism but do not implement or analyze it experimentally.

**efficiency_or_related_payoff_outcome**
- **Exact relevance**: Only a **small number of papers** (notably Javaid & Falk, 2015; Gelcich et al., 2013; dos Santos et al., 2014; dos Santos et al., 2013) report group efficiency or total payoff as a primary outcome.
- **Adjacent/Weak**: Many studies focus on contribution rates, fairness judgments, or neural markers, rather than the efficiency metric defined in the prediction task.

**Summary**: **Relevance for the precise prediction task is limited**: There are some exact matches, several close analogues (often with modified games or adjacent settings), and many that contribute more to mechanistic understanding or baseline context than direct prediction.

# 3) Outcomes Measured In The Literature

**Payoff-related Outcomes** (directly usable for the prediction task):
- **Efficiency / group payoff / surplus / total earnings**: Reported in only a few studies (Javaid & Falk, 2015; Gelcich et al., 2013; dos Santos et al., 2014, 2013; Perez et al., 2015—though not always as a treatment contrast).
- **Group-level change from control to punishment treatments**: Only a minority report this directly.

**Non-payoff Behavioral Outcomes** (informative but not directly substitutable for efficiency):
- **Contribution/cooperation rates**
- **Punishment/reward frequency or assignment**
- **Norm compliance and perceptions**
- **Partner choice, social preference, fairness judgments**
- **Neural or psychological correlates of punitive/cooperative behaviors**

**Distinction**: While **almost all studies capture behavioral and process-level data**, only a **few** provide explicit group efficiency outcomes differentiating control and punishment conditions.

# 4) Main Findings Relevant To Prediction

- **When control efficiency is low and punishment is enabled, efficiency can rise substantially** (Gelcich et al., 2013; dos Santos et al., 2013). The magnitude of gain varies with group social capital, exposure to enforcement, and baseline cooperativeness.
- **When baseline efficiency is already high and public social information is available**, enabling (costly, external) punishment can actually **reduce group efficiency** (Javaid & Falk, 2015). In this CPR setting, punishment created new coordination problems, ultimately lowering earnings.
- **The design of the punishment regime matters**: Effective sanctions (even probabilistic/weak) can improve efficiency in underperforming groups, but **costly, misaligned, or poorly targeted punishment may have little or negative effect**.
- **Punishment tends to be targeted at defectors rather than mere norm violators** (Bone et al., 2014), but the existence of antisocial or misdirected punishment can undermine gains (dos Santos et al., 2014).
- **Cognitive load or disturbance can nullify the anticipated efficiency benefits** of punishment/reputation mechanisms (dos Santos et al., 2014).
- **Reputation visibility** for punishment increases cooperation and can enhance group payoff (dos Santos et al., 2013).
- **Group composition** (e.g., social capital, unionization status, group identity) strongly moderates the treatment effect of punishment on efficiency (Gelcich et al., 2013; Baum et al., 2012).

# 5) Prediction Guidance

- **Strongest Prediction Basis**: If the control game **already achieves high efficiency (e.g., >70% of optimum) and there is strong social information or publicity of actions**, the literature indicates that enabling punishment may have **no effect or could decrease efficiency** by introducing risk, waste, or conflict (Javaid & Falk, 2015).
- **When the baseline (control) efficiency is low and opportunities for misbehavior/defection are high**, **enabling punishment mechanisms—especially those with some element of visibility or probabilistic threat—tends to increase group efficiency** (Gelcich et al., 2013; dos Santos et al., 2013).
- **Group characteristics such as prior cooperative norms, social capital, and unionization** can amplify or dampen the positive effect of punishment on efficiency. Predicting the size of efficiency change should take these moderators into account when possible.
- **The negative effect of punishment on efficiency** tends to occur when punishment is costly, poorly targeted, or unaccompanied by gains for punished parties (Javaid & Falk, 2015; dos Santos et al., 2014).
- **Punishment design features** (cost, technology, magnitude, visibility, linkage to cooperation) are key: fixed/low cost and clear linkage of punishment to defection are more likely to improve efficiency, while ambiguous, high-cost, or reputationally obscure punishment may not.
- **Control condition baseline** is critical: **The effect size and direction of change are tightly conditional on starting efficiency**. The literature does not support a model where punishment always increases efficiency; rather, the effect depends on context and design.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed by Paper Set**:
- **player_count, num_rounds, mpcr, all_or_nothing**: Frequently reported, especially in empirical PGG/CPR experiments.
- **punishment_cost, punishment_tech**: Key in nearly all papers implementing explicit punishment. There is recurring attention on who can punish (peer/third/external party), cost structure (fixed/unitary/costless), and mechanism (e.g., fine, deduction).
- **chat**: Present in some designs (esp. Perez et al., 2015), with mixed indications regarding its effect on efficiency.
- **show_other_summaries, show_n_rounds**: Less systematically analyzed, though public feedback is noted as a moderator of baseline efficiency (Javaid & Falk, 2015) and as a control condition.
- **reward_exists, reward_cost, reward_tech**: Rarely manipulated; some mention reward as a comparator (Konishi & Ohtsubo, 2015), but systematic data are sparse.
- **default_contrib**: Framing is sometimes described but not manipulated independently.
- **show_punishment_id**: Reputation or visibility of punishment is highlighted as an amplifier (dos Santos et al., 2013), but direct experimental manipulation is limited.

**Indirectly Informed or Contextually Discussed**:
- **Group composition, social capital, identity (union vs. non-union, ethnic ingroup/outgroup)**: Strong contextual moderators, though not directly manipulable as prediction features.
- **Nature of sanctioning (second/third-party, external vs. peer)** and **linkage of punishment to cooperation** are identified as crucial but not always parameterized.

**Little or No Data**:
- **reward magnitude (reward_cost, reward_tech, reward_exists)** in combination with punishment is not systematically addressed.
- **Interaction terms** (e.g., chat x punishment, show_other_summaries x punishment) are generally untested.
- **default_contrib** and **all-or-nothing** are often reported but not analyzed as moderators with respect to punishment effects on efficiency.

# 7) Important Limitations

- **Sparse direct outcome data**: Very few studies report treatment-control changes in efficiency (as defined for prediction) across a variety of game designs.
- **Few “exact” matches**: The majority of evidence comes from adjacent or loosely analogous games, limiting external validity for core PGGs.
- **Limited range of design manipulations**: Most studies vary only a subset of the possible 14 dimensions, leaving complex interactions and main effects under-explored.
- **Empirical ambiguity**: Where data exist, findings are **strongly context-dependent**: sometimes punishment increases efficiency, sometimes it lowers it, and sometimes it is neutral.
- **Non-payoff behavioral outcomes dominate**: Most evidence concerns behaviors (e.g., cooperation, punishment frequency) or mechanisms rather than actual group-level payoff, complicating direct quantitative prediction.
- **Intervention/reporting heterogeneity**: Punishment is variously defined (peer/third/external, costly/free, visible/anonymous), making cross-study aggregation difficult.
- **Lack of high-powered, multi-condition experiments**: There are few if any studies simultaneously varying several key design dimensions (e.g., cost, MPCR, chat) and reporting efficiency change.
- **Conflict and negative side-effects**: Some studies suggest that introducing punishment can increase antisocial punishment, waste, or conflict, but these effects are not measured or explained in most of the literature.

---

**Summary:**  
The literature base offers **conditional and context-dependent predictions** for the effect of enabling punishment on efficiency in PGG-like games. Where **control efficiency is low and design allows for well-targeted, visible, and not excessively costly punishment, efficiency reliably increases**. **Where baseline efficiency is high or punishment is costly and diffuse, efficiency may stagnate or decline**. The current paper set provides only **patchy coverage** across the full range of prediction dimensions, and few direct efficiency outcomes, so downstream predictors should prioritize closely matched, direct, and contextually relevant studies for calibration and treat all findings as **strongly design- and context-dependent**.
