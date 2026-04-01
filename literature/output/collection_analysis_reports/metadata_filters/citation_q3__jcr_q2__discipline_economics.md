# 1) Evidence Base

The reviewed literature set is quite broad, encompassing **87 papers** with a strong empirical core, primarily laboratory experiments, and a substantial minority of theory and computational papers. The majority of highly relevant papers are recent and experimental, with direct manipulations of punishment institutions in public goods game (PGG) or close-variant designs (see, e.g., Gürerk et al., 2018; Leibbrandt et al., 2015; Boosey & Isaac, 2016). Several theory papers provide formal mechanisms and comparative statics (Levine & Modica, 2016; Hwang & Bowles, 2012). The evidence base extensively covers the canonical linear PGG with and without punishment, variations in punishment technology, network structure, and contextual moderators such as endowment heterogeneity, group size, and subject pool. There is notable cross-context discussion (field vs. lab, student vs. general population, centralized vs. decentralized punishment).

The breadth is somewhat lessened by limitations in cross-society or large-scale field studies, though some studies address cultural and subject pool moderators. Most papers reporting on efficiency (or closely related payoff outcomes) use small groups (n=3-5), repeated game paradigms, and standard experimental controls. There is excellent coverage of design dimension variation for the effect of enabling punishment, though coverage is sparse or contextual for some dimensions like `chat`, `default_contrib`, and `show_punishment_id`.

# 2) Task Relevance

**Target relevance is as follows:**

- **pgg_or_variant:**  
  - The majority of the evidence is `exact`—i.e., focused on standard linear or step-level PGGs (e.g., Gürerk et al., 2018; Engl et al., 2021; Kingsley, 2016).  
  - Additional `close` evidence comes from CPR games, threshold-PGGs, or repeated PDs designed as public-goods-like environments.
- **punishment_or_sanctions:**  
  - Many studies are `exact`, directly enabling/disable costly peer or centralized punishment (e.g., Leibbrandt et al., 2015).  
  - Some are `close` (exclusion, reputation, weak or nonmonetary punishment) or `adjacent` (reward, shaming, legal framing).
- **efficiency_or_related_payoff_outcome:**  
  - Direct (i.e., `exact/close`) measurement of efficiency or group payoffs is frequent but **not universal**. Some studies only report related outcomes (earnings, surplus), while others focus solely on cooperation or punishment frequencies (`adjacent` or `weak`).

Overall, the **task relevance is high** with clear, frequent cases of `exact` or `close` relevance for all three keys, though some design/behavioral moderators are inferred from mechanisms or behavioral outcomes.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (core to prediction):**
  - Group efficiency (total payoff as a share of the fully cooperative benchmark) is reported directly in many PGG punishment papers (e.g., Gürerk et al., 2018; Kingsley, 2016; Leibbrandt et al., 2015).
  - Closely related: group earnings, welfare, aggregate surplus, probability of provision (in step-level games).
- **Non-payoff behavioral outcomes:**
  - Contribution (cooperation) rate, norm compliance, individual punishment frequency/type, prosocial vs. antisocial punishment, emotional drivers, belief changes.
  - Some studies only report behavioral outcomes, requiring inference regarding efficiency (e.g., Visser & Burns, 2015; Cheung, 2014).

The **payoff vs. behavioral distinction is clear in most evidence summaries**. Some studies, especially those using non-costly or non-monetary punishment (e.g., Dugar, 2013; Dugar, 2010), demonstrate efficiency gains explicitly, while others caution that increased cooperation does not always translate into higher efficiency if punishment costs offset gains.

# 4) Main Findings Relevant To Prediction

- **Punishment often increases efficiency, but the effect is highly context- and design-dependent.**
  - **Standard PGGs:** Enabling costly punishment generally increases group efficiency compared to control (no punishment), so long as antisocial punishment is rare, and the punishment technology has an effective cost/impact ratio (Gürerk et al., 2018; Fu et al., 2017; Engl et al., 2021).
  - **Punishment cost and impact are critical:** High cost and/or low-impact punishment can erode or eliminate efficiency gains. If punishment is too cheap and/or not well-targeted, antisocial punishment may arise, undermining efficiency (Bruhin et al., 2020; Kingsley, 2016).
  - **Antisocial punishment:** Prevalence varies by group composition and culture; in some settings, enabling punishment reduces efficiency due to antisocial (punishing cooperators) behavior (Bruhin et al., 2020; Bortolotti et al., 2015; Kocher et al., 2012).
  - **Network structure:** Efficiency gains from punishment require symmetric and well-connected punishment networks (Leibbrandt et al., 2015; Boosey & Isaac, 2016). Asymmetry (e.g., untouchables, incomplete networks) or partial monitoring can eliminate or reverse efficiency gains.
  - **Endowment heterogeneity:** When endowments are unequal and information is missing or ambiguous, punishment's effect on efficiency is muted or negative, due to normative conflict and increased punishment costs (Kingsley, 2016).
  - **Centralized vs. decentralized punishment:** Centralized approaches (leaders, third-party) may reduce antisocial punishment and improve targeting but are not always more efficient than peer punishment in the same design (Gürerk et al., 2018; Marcin et al., 2019).
  - **Costless/non-monetary punishment:** Costless social disapproval or approval can increase efficiency, but effects are generally weaker or more variable and often depend on combination with other mechanisms (Dugar, 2013).
  - **Reward mechanisms:** Positive incentives can raise contributions and efficiency, but often require a net-positive impact ratio to affect payoffs; transfer rewards may not help (Gürerk et al., 2018; Vyrastekova & van Soest, 2008).

- **Moderators and boundary conditions:**
  - **Information and identifiability (show_punishment_id):** Full disclosure of punishment sources strengthens efficiency gains via accountability and targeting (Kamei & Putterman, 2015).
  - **Communication/chat:** Not directly manipulated in most highly relevant studies; when present, can enhance cooperation independent of punishment, making efficiency attribution ambiguous.
  - **Group size:** Increases potential efficiency gains from punishment under effective technology (Levine & Modica, 2016), but can increase risk of over-punishment without coordination (Kamei, 2020).
  - **Baseline cooperation:** When control (no punishment) efficiency is already high, adding punishment may yield little or no additional efficiency and can even decrease it if punishment is misapplied (Kocher et al., 2012; Bortolotti et al., 2015).
  - **Conditional or role-based exit/exclusion:** Exclusion mechanisms can substitute for punishment and sometimes outperform it, but only if efficient and well-targeted (Croson et al., 2015; Dannenberg et al., 2020).

# 5) Prediction Guidance

- **Prediction of average efficiency with punishment enabled should**:
  - Expect **efficiency gains** over control in standard small-group, repeated PGGs with effective, well-calibrated peer punishment, and minimal antisocial punishment, especially with homogeneous endowments and symmetric monitoring (Gürerk et al., 2018; Fu et al., 2017; Gürerk, 2013; Marcin et al., 2019).
  - **Adjust for design features:**
    - **Punishment cost/impact (`punishment_cost`, `punishment_tech`)**: Efficiency gains are maximized with moderate cost and high impact; too high a cost or too low an impact can nullify or even reverse efficiency gains.
    - **Network structure (`player_count`, symmetry, monitoring)**: Asymmetric or incomplete networks reduce or eliminate gains (Boosey & Isaac, 2016; Leibbrandt et al., 2015).
    - **Group composition (culture, antisocial types, endowment heterogeneity):** High antisocial punishment, norm conflict, or cultural factors can undermine or reverse efficiency effects (Bruhin et al., 2020; Kingsley, 2016; Bortolotti et al., 2015).
    - **Information structure (`show_punishment_id`, `show_other_summaries`)**: Full, public information about punishers and outcomes facilitates pro-social punishment and efficiency (Kamei & Putterman, 2015; Engel & Kurschilgen, 2013).
    - **Baseline (control) efficiency:** If efficiency is already high, do **not** expect large or any efficiency gains from enabling punishment (Kocher et al., 2012).
    - **Punishment technology variance (exclusion, probabilistic, random, non-monetary):** These mechanisms can have positive, negative, or neutral efficiency effects depending on design specifics, especially cost structures and targeting precision (Leibbrandt et al., 2015; Dugar, 2013; Fatas et al., 2010).
    - **Centralized mechanisms and law:** Centralized (leader or third-party) punishment is no guarantee of higher efficiency over peer punishment; legal or normative framing can enhance pro-social effects (Gürerk et al., 2018; Engel & Kurschilgen, 2013).
  - **In complex or ambiguous designs (heterogeneity, incomplete networks, etc.), use caution and consider efficiency effects as indeterminate or moderated by group composition and behavioral patterns.**

# 6) Design Dimensions Highlighted Across Papers

- **Directly informed by empirical evidence (`player_count`, `num_rounds`, `mpcr`, `all_or_nothing`, `punishment_cost`, `punishment_tech`, `reward_exists`, `reward_cost`, `reward_tech`)**:
  - Variations in each demonstrate differential efficiency effects of punishment, with especially strong evidence for the core dimensions of group size, rounds, MPCR, and punishment cost/impact.
- **Indirectly or contextually informed (`chat`, `show_n_rounds`, `show_other_summaries`, `show_punishment_id`, `default_contrib`)**:
  - Chat (communication) is only manipulated in a minority of studies, but when present, both moderates and sometimes substitutes for punishment effects.
  - Information display dimensions are impactful but less frequently independently varied; identifiability and history can strengthen pro-social punishment.
  - Default contribution framing is only present in a few adjacent studies (Brekke et al., 2017); effects are ambiguous and rarely linked directly to efficiency.
- **Sparse or missing:**
  - Some context for exclusion (punishment as ostracism), legal framing, and reward exists, but less so for combinations or rare variants.

# 7) Important Limitations

- **Efficiency measures are sometimes inferred, not always directly reported.**  
  Many papers use contribution rates or cooperation as proxies, which can be misleading if punishment or exclusion costs offset gains.
- **Antisocial punishment is a critical but under-specified moderator.**  
  The prevalence and drivers of antisocial punishment can be highly variable, cultural, and context-specific, and are not predictable from structural game dimensions alone (Bruhin et al., 2020; Bortolotti et al., 2015).
- **Network structure is often hidden in standard designs.**  
  The default PGG design is typically fully connected, but actual punishment networks may vary (pairwise, partial, asymmetric), and this can dramatically affect efficiency gains (Leibbrandt et al., 2015; Boosey & Isaac, 2016).
- **Non-representative subject pools.**  
  Many findings are from student samples; general population or high-heterogeneity groups can exhibit different behaviors, including more antisocial punishment and less gain from punishment institutions (Bortolotti et al., 2015; Kocher et al., 2012).
- **Most evidence is for small groups, repeated games, and homogeneity.**  
  Effects in large groups, field settings, or with substantial real-world heterogeneity may depart from lab results.
- **Interaction effects are under-explored.**  
  Few studies systematically vary multiple dimensions (e.g., group size × punishment cost × information).
- **Reward mechanisms and combinations with punishment are less well investigated** as independent moderators of efficiency.
- **Some key dimensions are rarely manipulated independently**
  (e.g., chat, identity disclosure, default contribution, order/horizon information).
- **Results may not generalize outside the linear or threshold PGG paradigm**, especially to dynamic settings, common-pool resources with feedback, or highly asymmetric games.

----

**Summary:**  
The literature provides strong, design-aware empirical and theoretical support for the **conditional prediction** that enabling well-calibrated, targeted, peer punishment in a standard repeated PGG with homogeneous groups and symmetric networks will, on average, increase efficiency over the control. However, efficiency gains depend on cost/benefit calibration of punishment, the absence of antisocial punishment (itself not predictable from game design dimensions alone), and favorable information structure. Incomplete punishment networks, endowment heterogeneity without information, prevalence of antisocial types, and high punishment cost can nullify or reverse efficiency effects. Many studies document behavioral increases in cooperation that translate imperfectly (or sometimes not at all) into efficiency gains, especially when punishment or exclusion costs are high. Generalization to unfamiliar parameter regions or field settings is **risky** without deeper understanding of group composition, culture, and the social context surrounding punishment institutions.
