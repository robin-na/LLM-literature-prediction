# 1) Evidence Base

**Composition and Scope**  
This paper set is rich and diverse, comprising 121 papers, roughly half empirical (predominantly laboratory experiments) and the remainder theoretical or agent-based modeling studies.  
- **Empirical base**: The bulk of high-relevance evidence comes from lab experiments studying standard linear public goods games (PGG) and close variants with detailed manipulation of punishment, reward, and institutional design.  
- **Theoretical base**: A substantial number of theory and simulation papers provide mechanistic accounts and comparative statics for punishment effects, often in extended or spatially structured PGGs.

**Task Suitability**  
For the core downstream prediction task—predicting the effect of enabling peer punishment on efficiency in PGG-like designs—this evidence base is unusually rich. There are numerous directly informative empirical and theoretical studies that vary game design parameters similar to the 14 prediction dimensions.  
- The set is **broad** in covering not only classic PGGs but also threshold PGGs, spatial/networked PGGs, CPR games (adjacent), and environments with different institutional arrangements, communication protocols, and punishment technologies.

**Strength of Outcome Evidence**  
Direct measurement of **group efficiency** (aggregate payoff relative to social optimum, controlling for design and baseline) is standard in a subset of experimental studies, while others focus on behavioral outcomes such as contribution rates and punishment frequency. The set includes meta-analyses, multi-country comparisons, and comparative studies distinguishing peer, institutional, and third-party punishment.

# 2) Task Relevance

**a) pgg_or_variant**  
- **Exact relevance**: There is a critical mass of papers directly manipulating classic linear public goods games with n-way contribution and payoff aggregation (e.g., Zhang et al., 2024; JARUNGRATTANAPONG, 2022; Kamei, 2024), including repeated, one-shot, and structural variants.
- **Close/adjacent relevance**: The set also contains studies on CPR games, threshold PGGs, and collective-risk dilemmas—adjacent but not strictly canonical PGGs.

**b) punishment_or_sanctions**  
- **Exact relevance**: Many studies implement direct peer punishment (costly or costless), formal/institutional punishment, or targeted sanctions with detailed description of cost-tech ratios and network structure.
- **Close/adjacent relevance**: Additional coverage includes third-party and higher-order punishment, ostracism, exclusion, and institutional design variations.

**c) efficiency_or_related_payoff_outcome**  
- **Exact and close relevance**: Multiple studies report **efficiency** or closely related outcomes (e.g., group payoff, welfare, surplus, total earnings) as primary dependent variables.
- **Adjacent/weak**: Several studies focus only on behavioral outcomes (contribution, norm compliance), with efficiency occasionally inferred but not measured directly.

**Summary**  
- **High proportion of 'exact' and 'close' studies** on all three dimensions.  
- **Behavioral outcome bias**: Some relevant studies report only non-payoff behavioral measures (e.g., cooperation rates, norm compliance).

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes**  
- **Directly measured**: Group efficiency, total group payoff/earnings (e.g., Zhang et al., 2024; Kamei, 2024; Joseph et al., 2025; Jarungrattanapong, 2022; Casari & Tavoni, 2024; Botelho et al., 2022).
- **Indirectly reported**: Some simulation/modeling papers directly output average payoff as efficiency or group welfare.

**Non-Payoff Behavioral Outcomes**  
- **Frequently tracked**: Contribution rate, cooperation rate, punishment assigned/frequency, norm compliance, retaliation/antisocial punishment.
- **Other measures**: Norm perceptions, fairness preferences, propensity to punish or reward, compliance frequency, emotional drivers.

**Distinction Clarity**  
Many primary findings in high-relevance papers explicitly distinguish between the effect of punishment on contributions/cooperation and its effect on **efficiency** (aggregate payoff, net of sanction costs). Some behavioral studies, especially those using non-standard designs or adjacent paradigms (ultimatum, trust, CPR), only report behavioral or attitudinal outcomes, not group efficiency.

# 4) Main Findings Relevant To Prediction

### Empirical Regularities

- **Punishment increases contributions consistently** (Zhang et al., 2024; Kamei, 2024; JARUNGRATTANAPONG, 2022; Kim et al., 2025), but the impact on efficiency is **not uniformly positive**.
- **Efficiency effects depend strongly on punishment cost relative to effectiveness**  
  - **High punishment cost**: Even when cooperation increases, efficiency may decrease or remain flat due to sanctioning costs outweighing gains (Botelho et al., 2022; Casari & Tavoni, 2024; Deng et al., 2025).
  - **Costless or low-cost punishment**: When punishment is nearly costless or strongly effective, group efficiency often rises sharply, sometimes approaching the social optimum (Kamei, 2024; Sun et al., 2025; Bühren et al., 2025).
- **Network structure/coverage and institutional details matter**  
  - **Complete punishment networks** (everyone can punish everyone): Do not automatically yield higher efficiency—may suffer from ‘bystander effect’/diffusion of responsibility and lower actual punishment, leading to worse outcomes than more selective or incomplete networks (Peng & Fan, 2023; Bühren et al., 2025).
  - **Targeted punishment** (e.g., lowest contributor): Theoretically optimal (Huang et al., 2024), achieving maximal efficiency with minimal necessary sanctions.
- **Formal/institutional punishment** (administered centrally, with potential for endogenous selection) often sustains higher efficiency than peer/voluntary punishment, but only if sufficiently deterrent and without undermining incentives.
- **Magnitude of punishment**: Small or weak punishment can sometimes **reduce efficiency** by introducing costs without deterring free-riding (Ye et al., 2023; Sun et al., 2024); large or effective punishment is necessary for robust efficiency gains.
- **Antisocial punishment/retaliation**: Reduces efficiency, especially in settings where low contributors retaliate (JARUNGRATTANAPONG, 2022; Kim et al., 2025).
- **Chat/communication**: Generally increases efficiency (Zhang et al., 2024 indirectly; Bazart et al., 2022), but, when combined with punishment, can moderate both positive and negative effects depending on communication structure.
- **Heterogeneity & culture**: Effects vary with group composition (e.g., MPCR heterogeneity, group norms, country effects: Kamei et al., 2025; Peng & Fan, 2023).
- **Control efficiency as a predictor**: High control efficiency (without punishment) predicts little marginal gain from adding punishment and increases risk of net efficiency loss (Botelho et al., 2022; Casari & Tavoni, 2024). Low control efficiency predicts larger efficiency improvements from punishment (Kamei, 2024; Joseph et al., 2025).

### Mechanistic/Theoretical Insights

- **Thresholds**: There exists a minimum level of punishment required to sustain full cooperation/maximal efficiency (Huang et al., 2024). Above this threshold, additional punitive capacity offers diminishing return and may even reduce efficiency if overused.
- **Combined reward/punishment**: Theoretical work shows combining minimal punishment with maximal reward yields highest efficiency (Huang et al., 2024; Yang & Yang, 2024).
- **Network structure**: Small-world and spatial structure can boost the efficiency impact of punishment, especially when network clustering balances reach and reciprocity (Cui et al., 2022).

# 5) Prediction Guidance

- **Enabling peer punishment in classic linear PGGs** **usually increases efficiency** versus control when the control game has low efficiency, especially:
  - When punishment is low-cost and effective (high ratio of impact to cost).
  - When punishment is targeted efficiently (not distributed diffusely).
  - When antisocial/retaliatory punishment is minimal.
- **The efficiency gain from punishment is highly **moderated** by the following dimensions**:
  - **Punishment cost and effectiveness** (punishment_cost, punishment_tech): High cost relative to impact can lead to lower or unchanged efficiency, even if cooperation increases (Botelho et al., 2022; Casari & Tavoni, 2024).
  - **Player count**: Larger groups can suffer coordination problems or bystander effects, weakening punishment’s impact (Peng & Fan, 2023; Jarungrattanapong, 2022).
  - **Network/institutional structure**: Incomplete or poorly coordinated punishment institutions can fail to achieve efficiency gains or may have unpredictable effects (Peng & Fan, 2023; Bühren et al., 2025).
  - **Presence of reward (reward_exists)**: Joint reward and punishment can achieve higher efficiency, with minimal necessary sanctioning (Yang & Yang, 2024; Huang et al., 2024).
  - **Communication (chat)**: Enables higher cooperation and may interact with punishment (Kim et al., 2025; Bazart et al., 2022).
  - **Punisher/reward identity (show_punishment_id)**: Transparency can affect antisocial punishment or effectiveness, though results are design-specific.
- **Baseline (control) efficiency** is a valuable input: If the control game is already highly efficient, adding punishment can introduce unnecessary costs and actually reduce efficiency.
- **In special/adjacent cases** (e.g., CPR games with intergroup conflict or collective punishment rather than targeted punishment), punishment may be less effective or, if poorly structured, detrimental to efficiency (Schaefer, 2023; Deng et al., 2025; Jiang & Villeval, 2024).
- **Antisocial punishment** and **retaliation loops** should be considered risk factors for net efficiency loss.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions**  
- **player_count**: Well-covered, with direct evidence for effects in 2–6 players and higher.
- **num_rounds**: Many studies, both one-shot and repeated (typical: 1, 6, 10, 15, 30, 32 rounds).
- **mpcr**: Explicitly reported and manipulated in most experimental and theory papers.
- **punishment_cost, punishment_tech**: Central to nearly every punishment-enabled study; several studies systematically vary these parameters.
- **chat**: While not always manipulated as a treatment, its presence or absence is clearly specified; several studies test its effects.
- **all_or_nothing**: Binary (all-or-nothing) and continuous PGGs are both represented.
- **reward_exists, reward_cost, reward_tech**: Investigated in a subset of papers, with findings on the combined effect of reward and punishment.

**Indirectly or Contextually Discussed Dimensions**  
- **show_other_summaries, show_n_rounds**: Occasionally manipulated, more often described as part of the design (e.g., feedback visibility).
- **show_punishment_id**: Sometimes manipulated in centralized punishment or transparency studies, but not consistently varied.
- **default_contrib**: Rarely manipulated; most studies use default ‘keep’ (opt-in) framing.

**Missing or Sparsely Covered Dimensions**  
- **Treatment precedence/sequencing**: While some papers randomize or sequence treatments, dimensions specific to temporal info display (e.g., round-number visibility) are usually only contextually described.
- **Complex reward and punishment institutions** (e.g., endogenous institution formation, higher-order punishment) are addressed in a subset (e.g., Kamei et al., 2025), but not systematically connected to all 14 dimensions.

# 7) Important Limitations

- **Context generalizability**: Most experimental studies use student participants in standard lab conditions. Results may differ with real-world stakes, heterogeneous populations, or field settings.
- **Non-uniform efficiency reporting**: Not all papers report efficiency (group payoff relative to social optimum) in a way directly compatible with the prediction task; inference sometimes relies on proxy outcomes (contribution rate, cooperation, retaliation rates).
- **Limited data on less common dimensions**: Certain design features (e.g., punishment transparency, default contribution framing, round-number display) are rarely manipulated systematically, limiting evidence for their specific predictive value.
- **Ambiguity in adjacent and mixed-design games**: Results from CPR, collective-risk, and adjacent paradigms may not transfer directly to canonical PGGs, especially when mechanisms or outcomes differ (e.g., non-targeted group punishment, group-specific externalities).
- **Antisocial and erroneous punishment**: Several studies note that the presence of antisocial punishment (punishing cooperators) and retaliation can undermine efficiency gains, but the conditions under which this occurs are not always specified or predictable.
- **Interaction effects**: Design dimension interactions (e.g., player count × punishment network, chat × punishment) are not always explored systematically, so multidimensional prediction is subject to additional uncertainty.
- **Up-scaling and external validity**: Most findings apply to small-n laboratory groups; scaling up to real-world or larger online environments may add new moderating dynamics (diffusion, social identity, network effects).

---

**Summary**:  
The literature base synthesized here is unusually strong for making principled, evidence-based predictions about punishment's effect on efficiency in public-goods-game-like environments, conditional on game design and control efficiency. The core conclusion is that the efficiency effect of introducing punishment is highly conditional on the cost-effectiveness of the sanctioning mechanism, the baseline (control) efficiency, and key structural moderators such as network/institutional design, presence of rewards, and group composition. Prediction efforts should rely most heavily on those studies that directly manipulate and report efficiency outcomes across explicitly documented design dimensions, while treating behavioral-only or adjacent-outcome studies as supportive but not determinative.
