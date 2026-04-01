# 1) Evidence Base

This paper set is relatively broad in conceptual coverage but heterogeneous in relevance and in the types of methods and outcomes reported. It includes both **empirical lab experiments** (mainly on public goods games and close variants) and **theoretical/modeling papers** (mainly evolutionary game theory and related mechanisms). There are several papers offering **direct experimental estimates** of punishment effects on group efficiency, as well as theory papers and empirical studies focused on behavioral outcomes (cooperation rates, punishment assignment, communication, etc.). Some papers also address broader CPR, social dilemma, or adjacent contexts, such as common pool resource games, threshold or exclusion games, or one-shot and observational studies.

Overall, the set is **mixed in terms of empirical versus theoretical evidence**: There is a solid but limited core of experimental studies directly measuring efficiency in PGGs with and without punishment, surrounded by a larger body of papers focusing on contributions, punishment behavior, conditional cooperation, sanction reputation, communication, and theoretical mechanisms.

# 2) Task Relevance

For each of the three focal dimensions:
- **pgg_or_variant**: Most papers are either **exact** (explicitly public goods games or direct variants), but some are **close** (CPR/threshold/exclusion games), while a substantial minority are only **adjacent** (other social dilemmas, dictator games, or real-world scenarios).
- **punishment_or_sanctions**: About half the set is **exact** (directly manipulate or model punishment/sanctions), with the remainder being **adjacent** (rewards, exclusion, monitoring, or informal judgment) or **none**.
- **efficiency_or_related_payoff_outcome**: Direct reporting of **efficiency or group payoff** is notably **less common**. Many experiments measure behavioral responses (contributions, cooperation, etc.), with efficiency inferred but not always explicitly reported. Only a minority are **exact** on efficiency; several are **close** (group payoff, total earnings), while others are **adjacent** or **weak** (behavioral/proxy outcomes).

The **most relevant papers** for the downstream prediction task are empirically focused PGG experiments with both punishment manipulations and direct efficiency or group payoff measurement (e.g., Kölle, 2015; Choi & Ahn, 2013; Joffily et al., 2014). Several theory papers are close on mechanism but report payoff indirectly or focus mainly on cooperation rates.

# 3) Outcomes Measured In The Literature

- **Payoff-based/efficiency outcomes (most relevant):**
  - **Direct measurement:** Group efficiency as a percent of social optimum, total group payoff, welfare, or earnings (e.g., Kölle, 2015; Charness & Yang, 2014; Gelcich et al., 2013).
  - **Indirect/inferred:** Higher average group contribution rates as a proxy for higher efficiency (e.g., Choi & Ahn, 2013; Joffily et al., 2014).
  - **Theoretical payoff expressions:** Derived in models, sometimes used to comment on conditions for optimality but rarely matched to experimental data (e.g., Chen et al., 2014).
- **Non-payoff behavioral outcomes (less relevant):**
  - **Contribution and cooperation rates:** Reported in nearly every experimental PGG or variant paper.
  - **Punishment frequency/assignment:** Common metric, sometimes linked to group outcomes.
  - **Norm compliance, intentions, communication patterns, emotional/psychological/physiological responses:** Used in several studies (e.g., Joffily et al., 2014; Declerck et al., 2013).
  - **Reputation for punishment:** Focus of some adjacent studies, sometimes linked to future cooperation (dos Santos et al., 2013).

Importantly, **efficiency** is not always the primary metric and must not be conflated with behavioral outcomes.

# 4) Main Findings Relevant To Prediction

- **Punishment can, but does not always, increase efficiency** in public goods games:
  - In **homogeneous groups or groups with capability heterogeneity**, punishment often raises efficiency (Kölle, 2015).
  - With **valuation heterogeneity**, punishment may not increase efficiency and can even increase inequality (Kölle, 2015).
  - **Probabilistic or reputation-based punishment mechanisms** (when properly structured) can support higher payoffs, but optimality depends on the balance of cost and severity (Chen et al., 2014; dos Santos et al., 2013).
  - **Antisocial punishment** can undermine efficiency and even reduce group welfare in some contexts (Sylwester et al., 2013).

- **Most empirical PGG studies (with standard group sizes, moderate punishment costs, and no additional interventions) find that enabling punishment increases contributions and, by inference, efficiency** (Choi & Ahn, 2013; Joffily et al., 2014; Gelcich et al., 2013). However, direct measurement is rare.

- **Control (baseline) efficiency is predictive:** The change in efficiency from enabling punishment is generally larger when baseline efficiency is intermediate or low, and the effect is strongly moderated by group norms or social capital (Gelcich et al., 2013).

- **Communication and social structure can mediate the impact of punishment:**
  - Rich, open-ended chat and communication about sanctions increase the impact of punishment on cooperation and payoff (Cooper & Kühn, 2014).
  - The presence of reputation systems or visibility of punitive acts boosts their effectiveness for group payoff (dos Santos et al., 2013).

- **Alternative sanction mechanisms (e.g., exclusion, group formation, reward):**
  - Exclusion and voluntary group formation can increase efficiency, sometimes more so than standard costly punishment (Charness & Yang, 2014).
  - Reward mechanisms can also boost efficiency, especially in threshold or coordination environments, and sometimes are modeled as more effective than punishment in theory (Sasaki & Uchida, 2014).
  - Informal sanctions, such as social judgment, mainly affect behavior in specific cultural or context-dependent ways (Salmon & Serra, 2017).

- **Theoretical and simulation results (phase transitions, parameter thresholds):**
  - The impact of punishment on efficiency (or, more commonly, on cooperation rates) can be highly non-linear, with phase transitions based on group size, MPCR, punishment fines/cost, and other parameters (Perc, 2016; Chen et al., 2014).

- **Behavioral mechanisms and contextual moderators:**
  - The effectiveness of punishment can depend on cost, magnitude, visibility, and cultural context.
  - Punishment is potentially counterproductive if widely used in antisocial ways or if group heterogeneity is not conducive to cooperation (Sylwester et al., 2013).
  - Mechanisms like monitoring and reputational incentives play strong moderating roles (Wilson et al., 2013; dos Santos et al., 2013).

# 5) Prediction Guidance

**The literature supports several key principles for predicting average efficiency with punishment enabled as a function of design dimensions and baseline efficiency:**

- **Punishment Effect Is Not Universal**: The effect size depends greatly on baseline control efficiency, type of heterogeneity (capability/valuation/cultural), punishment cost/magnitude, and population/social structure.
- **High Control Efficiency → Limited or No Further Gains**: If control efficiency is already high, the incremental effect of punishment is usually small (Kölle, 2015).
- **Low to Medium Control Efficiency → Likely Efficiency Gains with Punishment**, but only if antisocial punishment is rare and group norms/social capital are strong (Gelcich et al., 2013).
- **Group Heterogeneity Moderates the Effect**: Capability heterogeneity often strengthens positive effects, while valuation heterogeneity or weak social capital can nullify or reverse them (Kölle, 2015; Gelcich et al., 2013).
- **Reward and Exclusion Can Substitute or Outperform Punishment**: In some designs, reward or exclusion-based sanctions yield equal or better efficiency gains, especially when ease of group formation or merging is present (Charness & Yang, 2014; Sasaki & Uchida, 2014).
- **Critical Game Parameters**: Prediction should weigh group size, number of rounds, MPCR, punishment cost/magnitude, communication channels, and feedback structure, as their variations are shown in the literature to moderate outcomes.
- **Dimensionally, the Most Direct Predictors**: The dimensions most directly associated with variation in treatment efficiency (punishment enabled) are: player_count, num_rounds, mpcr, punishment_cost, punishment_tech/visibility, baseline efficiency (as affected by default_contrib and context), and sometimes chat/communication.

**Key Caveat**: In most studies, outcomes are reported as contribution rates, not direct efficiency. When inferring treatment efficiency from increased contributions, the magnitude must be discounted for the cost of punishment incurred—otherwise, group earnings may not rise as much as contributions.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- `player_count`: Varied and explicitly manipulated (most papers).
- `num_rounds`: Varied; longer games typically facilitate larger punishment effects (Kölle, 2015).
- `mpcr`: Widely covered; lower MPCRs make efficiency gains via punishment harder (Perc, 2016; Choi & Ahn, 2013).
- `punishment_cost` and `punishment_tech`: Explicitly analyzed in theory and empirical papers; critical for predicting punishment's effectiveness and costliness.
- `all_or_nothing`: Studied in both all-or-nothing and continuous games.
- `reward_exists`, `reward_cost`: Analyzed in a few papers examining the substitution or complementarity of reward and punishment (Sasaki & Uchida, 2014).

**Indirectly or Contextually Informed Dimensions:**
- `chat`: Studied as a moderator (Oprea et al., 2014; Cooper & Kühn, 2014).
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Touched upon in feedback/visibility studies, but not always manipulated directly.
- `default_contrib`: Only rarely explicit (Gelcich et al., 2013).
- `punishment_magnitude`: Closely tied to `punishment_cost`; manipulated in some theory papers but not always reported separately.
- `reward_tech`, `reward_magnitude`: Less commonly manipulated.

**Dimensions Mostly Missing or Thinly Covered:**
- `show_punishment_id`: Reputation/visibility is present in some adjacent studies (dos Santos et al., 2013) but rarely manipulated systematically.
- Fine-grained aspects of `punishment_tech` and multiple types of reward/sanction simultaneously are not broadly covered in the empirical literature.

# 7) Important Limitations

- **Efficiency outcome reporting is inconsistent**: Many studies infer efficiency from contribution rates rather than reporting payoff-based efficiency directly, risking overstatement of punishment benefits if cost is not accounted for.
- **Heterogeneity in design and environment**: Not all studies match the canonical linear PGG; external validity for specific prediction dimensions (e.g., structured populations, field-lab CPRs) may be limited.
- **Scarcity of systematic multi-dimensional variation**: Few studies systematically vary more than a subset of the 14 prediction dimensions, and moderators such as cultural context or social capital are not typically jointly analyzed with core game parameters.
- **Context-sensitivity and cultural moderation**: Rates of antisocial punishment, compliance with sanctions, and baseline cooperativeness vary substantially across group types and cultures, complicating generalization.
- **Reward, exclusion, and communication treatments**: Adjacent mechanisms (aside from costly punishment) sometimes outperform punishment or interact with it in non-additive ways, which may not be directly captured by simple punishment-enabled vs. punishment-disabled comparisons.
- **Limited direct guidance for novel or edge-case parameter combinations**: Mechanistic and phase-transition models indicate potential for sharp non-linearities, but the empirical base is thin for unusual combinations (e.g., very high punishment cost with low MPCR, large groups with high heterogeneity).
- **Ambiguity in negative or null results**: Some theoretically plausible mechanisms (e.g., antisocial punishment) are not always empirically prominent but may appear under specific conditions.

**In sum**, the literature base provides a moderate-to-strong foundation for predicting qualitative effects of punishment on efficiency in PGG-like environments as a function of standard game dimensions and baseline efficiency, with important caution for contextual moderators, costs, and heterogeneity. Fine-grained, quantitative predictions—especially across the full 14-dimension design space—remain subject to notable uncertainty and extrapolation risk.
