# 1) Evidence Base

The provided literature base is extensive (180 papers), drawing heavily from **empirical laboratory experiments** on public goods games (PGGs) and their close variants, as well as a subset of rigorous **theory and simulation** papers that model punishment effects in collective dilemmas. A majority of sources are **experimental studies with tightly controlled PGG parameters**—these form the backbone for analysis of punishment’s impact on efficiency. The remainder includes **close variants** (e.g., CPR, trust games), and a modest number of **theory/simulation papers** that generalize or contextualize findings from empirical work.

The evidence set is **rich and diverse** with respect to standard PGGs, covering a broad swathe of **game design dimensions** (group size, rounds, MPCR, information structures, punishment cost/impact, centralization, etc.), institutional mechanisms (peer vs. centralized, endogenous vs. exogenous, communication, exclusion), and context factors (cultural, emotional, informational, network, heterogeneity, etc.). However, there is **less direct coverage of rare or edge-case design combinations** (e.g., very large groups, highly asymmetric reward/punishment, exotic information settings).

There is a **strong empirical slant**; most results are **data-driven**, with theory papers often seeking to rationalize or interpret empirical regularities. Direct investigation of **group efficiency/welfare** as a function of punishment is the focal outcome in many empirical studies and several theory papers, though in some the central focus is contributions or cooperation rates rather than payoffs.

# 2) Task Relevance

**pgg_or_variant:**  
- **Exact relevance:** Most of the core analyzed evidence comes from **standard PGGs** or exact variants (canonical linear VCMs, threshold PGGs, punishment-enabled PGGs), with clear design mapping to the 14 prediction dimensions (`player_count`, `mpcr`, etc.).
- **Close relevance:** Several studies work with **CPR games, trust games, threshold or binary-contribution PGGs, and dynamic or networked PGG variants**. These offer close but not always exact mapping to the canonical PGG prediction environment.
- **Adjacent/weak relevance:** A minority of papers address more **distal variants** (e.g., two-player PDs, market-based dilemmas, third-party punishment in trust games) or focus on mechanisms parallel to punishment (e.g., reward-only, gossip/reputation without explicit payoff sanctions).

**punishment_or_sanctions:**  
- **Exact relevance:** A substantial core of papers experimentally manipulate **peer or centralized punishment**, exclusion, ostracism, enforcement institutions, or the option to implement punishment (endogenously/exogenously).
- **Close relevance:** Some evidence comes from **reward mechanisms, reputation/gossip, exclusion, or taxation**, which are not always directly analogous to costly punishment but serve similar enforcement roles.
- **Adjacent/weak relevance:** Some papers analyze punishment as voluntary exclusion, reporting, or indirect norm enforcement (e.g., via information sharing or emotion), with only weak direct implications for the formal punishment dimensions in the prediction task.

**efficiency_or_related_payoff_outcome:**  
- **Exact relevance:** Many empirical papers **explicitly report efficiency**, group payoff, welfare, total surplus, or directly comparable normalized payoff measures (e.g., as a ratio to full cooperation).
- **Close relevance:** Several report **earnings, mean payoffs, or surplus** without full normalization; some focus on group outcomes implied to be efficiency-related (e.g., reductions in destruction/overuse, increases in resource stock), with explicit calculations possible from reported results.
- **Adjacent/weak relevance:** Studies emphasizing **contributions, cooperation rates, or punishment frequency** as primary outcomes, or those measuring behavioral but not payoff-based outcomes.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes (central to efficiency):**
- **Efficiency (normalized group payoff relative to social optimum):** Core in most punishment-enabled PGG studies (e.g., Gürerk et al., 2018; Arechar et al., 2018; Dutta et al., 2021).
- **Group/mean payoffs, welfare, surplus, total coins/earnings:** Common and either directly reported or easily mapped to efficiency (e.g., Engl et al., 2021; Lim & Zhang, 2020).
- **Net profits, losses, or resource conservation:** In CPR/threshold settings, measured as group profit or resource retention vs. over-extraction losses (e.g., Wegmann & Musshoff, 2019).

**Non-payoff behavioral outcomes:**
- **Contribution rate, cooperation rate, compliance, conditional cooperation, norm enforcement, anti-/prosocial punishment rates.**
- **Punishment/reward frequency, targeting, antisocial/prosocial use, norm attributions, emotional responses.**
- **Partner selection, replacement, reputation, information sharing, group selection dynamics.**

Some studies report only contributions or behavior and **explicitly do not analyze efficiency/payoff themselves** (e.g., Albrecht et al., 2018; Otten et al., 2021).

**Key distinction:**  
**Prediction for efficiency/payoff cannot be made from contribution or punishment frequency alone**, except in linear PGGs with zero or trivial punishment cost. **Studies relying on contributions or behavior without linking to payoff must be treated as indirect or limited evidence for the efficiency prediction task.**

# 4) Main Findings Relevant To Prediction

## a. **General Effect of Punishment on Efficiency**

- **Punishment generally increases group efficiency relative to no-punishment controls** in standard PGGs under typical laboratory parameters (4–5 players, 5–20 rounds, MPCR ≈ 0.4–0.6, moderate punishment cost/impact), **provided antisocial punishment is rare and information about contributions is sufficient** (Gürerk et al., 2018; Arechar et al., 2018; Dutta et al., 2021).
- **Efficiency gains are substantial** but seldom reach the full cooperation benchmark; due to punishment costs, group earnings typically rise to 70–95% of the optimum, depending on design (Engl et al., 2021; Lim & Zhang, 2020; Suleiman & Samid, 2021).
- **Peer punishment, third-party (centralized) punishment, and endogenous/exogenous institution choice** all generally result in higher efficiency than no punishment when norm violations are observable and punishers target defectors (Gürdal et al., 2021; Angelovski et al., 2018; Cobo-Reyes et al., 2019).

## b. **Design-Dependent Moderators and Boundary Cases**

- **Group composition and cultural context matter:** In groups with high prevalence of antisocial punishment or in which in-group favoritism deters enforcing punishment on certain members, the impact of punishment on efficiency is reduced or can even be negative (Mantilla et al., 2021; Bruhin et al., 2020; Bühren & Dannenberg, 2021).
- **Heterogeneity:** Endowment or payoff heterogeneity moderates punishment's effect; when contribution capacity/endowment is unobservable, punishment can misfire, reducing efficiency (De Geest & Kingsley, 2019; Waichman, 2020).
- **Information/framing:** Efficient punishment depends on visibility of contributions, transparency of punishment, and salience of norm violation (De Geest & Kingsley, 2021; Glöckner et al., 2018; Waichman & Stenzel, 2019; Ambrus & Greiner, 2019). Multiple punishment channels or stronger monitoring can augment efficiency, especially when individuals can cross-verify behavior.
- **Institutional format:** Democratic (voted) vs. exogenous punishment institution selection does **not strongly affect efficiency** conditional on punishment being implemented (Marcin et al., 2019; Castillo et al., 2021). Punishment severity and cost-to-impact ratio **moderate the efficiency impact**: more cost-effective punishment has stronger positive payoff effects (Tanimoto, 2018; Acemoglu & Wolitzky, 2021).
- **Network structure:** Dense, hierarchical (star/complete) networks favor efficiency via punishment. In sparse or fragmented networks, punishment can be less efficient or backfire (Fatas et al., 2020; Kanitsar, 2021; Shreedhar et al., 2020).
- **Feedback and monitoring:** Presence and cheapness of monitoring, and effective feedback linking punishment to prior action, are **critical for punishment to improve efficiency**. Without such measures, punishment may increase cooperation but not efficiency due to misapplication and excessive cost (Nicklisch et al., 2021; Waichman & Stenzel, 2019).
- **Costly or misapplied punishment:** When punishment is very costly (relative to contributed surplus), antisocial, or poorly targeted, **efficiency gains are eroded or reversed**; in some CPR/threshold games, actual group payoffs are lower when punishment is enabled (Vollan et al., 2019; Robbett, 2019; De Geest & Kingsley, 2019).

## c. **Interactions with Other Mechanisms**
- **Chat and communication:** Adding chat can **substantially boost efficiency**, sometimes more than punishment alone, or synergistically with punishment (Koch et al., 2021; Kamei, 2019).
- **Rewards/institutional competition:** When reward mechanisms are available, especially those with a net payoff bonus, they tend to yield higher or equivalent efficiency compared to punishment (Gürerk et al., 2018; Chugunova et al., 2020).
- **Exclusion/ostracism:** Exclusion as punishment increases efficiency only if it is costless; otherwise, costs can nullify or outweigh cooperation gains (Dannenberg et al., 2020).
- **Emotional context:** Emotional environment (e.g., induced happiness vs. anger) moderates whether punishment improves or harms efficiency (Lee & Min, 2021).

## d. **Theoretical Results and Boundary Mechanisms**
- **Theory confirms empirical trends** but stipulates that punishment's effect on efficiency is **not automatic**: effectiveness, cost, information, and group structure all condition outcomes (Dutta et al., 2021; Acemoglu & Wolitzky, 2021; Alventosa & Olcina, 2021).
- **Punishment can backfire:** Inefficient, misapplied, or too costly punishment can reduce group welfare (Tanimoto, 2018; Cordes et al., 2021; Robbett, 2019; Vollan et al., 2019).
- **Endogenous punishment and institution survival:** Only when punishment remains cost-effective, appropriately targeted, and norm-consistent does efficiency rise and institutional self-selection persist (Brandt & Svendsen, 2019).

# 5) Prediction Guidance

- **Strong baseline:** In standard laboratory PGGs with moderate group size (3–5), 10–30 rounds, moderate MPCR (0.4–0.6), explicit information about contribution/norm violations, and peer or centralized punishment with **moderate cost/impact ratios (e.g., 1:3)**, enabling punishment reliably yields a **substantial efficiency gain** over the control (no-punishment) condition (Arechar et al., 2018; Dutta et al., 2021; Gürdal et al., 2021; Cobo-Reyes et al., 2019).
- **Prediction should be cautiously upward from control efficiency, but not to full optimum**: Typical observed efficiency with punishment enabled rises **by 10%–30% of the social optimum** over the control, often stabilizing at **75–95% efficiency** depending on particulars.
- **Key positive moderators:**  
    - **Low prevalence of antisocial punishment**  
    - **High accuracy and low cost of monitoring/feedback**  
    - **Centralized or democratic punishment mechanisms** (if implemented)
    - **Low-to-moderate punishment cost relative to impact**
    - **Symmetric or observable heterogeneity**
    - **Complete or star/hierarchical network structures**
    - **Availability of communication or early institution choice**
- **Key negative moderators:**  
    - **High prevalence of antisocial punishment** (Bruhin et al., 2020)
    - **Endowment or payoff heterogeneity with unobservable contributions**
    - **Group or population with high in-group/out-group boundaries or status disparities**
    - **Punishment is very costly, global (collective), or poorly targeted**  
    - **Punishment network is sparse, generalized exchange rather than public-goods structure** (Kanitsar, 2021)
    - **CPR/threshold or extraction games** with punishment often fail to improve efficiency due to resource destruction or mis-targeting (Vollan et al., 2019; De Geest & Kingsley, 2019)
    - **Negative emotional context or lack of clear norm salience**  
    - **Punishment institution is absent, misapplied, or subject to system gaming/extortion**  

- **Crucial: Control (no-punishment) efficiency is a strong, but not sufficient, predictor of possible efficiency gains.** Extreme baseline inefficiency (e.g., near-zero contribution) can be improved dramatically, but only if punishment is well targeted and not subverted. If control efficiency is already high (e.g., due to reputation, partner choice, or chat), adding punishment can **reduce or have no effect on efficiency** due to the cost of unnecessary sanctions (Bühren & Dannenberg, 2021; Brunner & Ostermaier, 2018).

- **Interactions:** When both chat/communication and punishment are present, the efficiency effect is larger than either mechanism alone (Koch et al., 2021). When multiple punishment channels (e.g., observed and unobserved) are combined, efficiency gains can be realized via reduced punishment expenditure and enhanced norm salience (Glöckner et al., 2018).

- **Quantitative mapping:** Typical parameterizations (from e.g., Arechar et al., 2018; Gürdal et al., 2021):  
    - **Control efficiency:** ~50–65% social optimum  
    - **Punishment-enabled efficiency:** ~70–90% social optimum  
    - **Reward-enabled (where reward is net-positive):** Occasionally higher than with punishment, but less common in PGG punishment-design studies

- **Boundary cases:**  
    - In certain contexts (mixed composition, high antisocial punishment, unobservable heterogeneity), enabling punishment can **reduce efficiency relative to control** (Bruhin et al., 2020; Mantilla et al., 2021; Vollan et al., 2019).
    - In networked or dynamic settings, the appropriate network density, matching/routing rules, or timing of feedback must be considered to avoid efficiency loss (Fatas et al., 2020; Mihm & Toth, 2020).

**Summary for prediction tasks:**  
- Use **control (no-punishment) efficiency** as baseline.
- Adjust **upward** for standard PGGs with well-targeted, moderate-cost punishment and transparent information.
- Moderate or **dampen gains** where antisocial punishment, misapplied sanctions, unobservable heterogeneity, or network sparsity are present.
- **Expect smaller or no gains** (and possible losses) in complex CPR, threshold, or collective punishment games, or in fragmented/diverse populations without strong norm consensus.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed** (with multiple, robust sources for efficiency outcomes):  
- `player_count`, `num_rounds`, `mpcr`, `punishment_cost`, `punishment_tech`, `all_or_nothing`, `chat`, `show_other_summaries` (i.e., monitoring), `show_n_rounds`

**Indirectly informed**:  
- `default_contrib` (framing effects noted), `show_punishment_id` (some work on feedback/identity)
- `reward_exists`, `reward_cost`, `reward_tech` (reward often analyzed as a separate or competing mechanism, but less central than punishment across the set; more attention when both reward and punishment are present)

**Contextually discussed**:  
- Effects of communication (`chat`), emotional induction, group heterogeneity, endogenous/exogenous institution choice, partner matching, and network structure are discussed as moderators.

**Effectively missing or sparse**:  
- **Interaction effects among rarely combined features:** e.g., large group sizes combined with sophisticated punishment/reward tech, or rare feedback/identification structures.
- **Rare or extreme cost structures:** e.g., punitive costs near or above the full endowment, severe reward asymmetries.
- **Long-horizon or field settings:** While some field/lab-in-field studies exist, most evidence comes from lab contexts with group sizes ≤10 and rounds ≤30.

# 7) Important Limitations

- **Gaps in design coverage:** While most canonical PGG parameters are well covered, **some regions of the design space are thinly populated** (e.g., very large groups, rare forms of feedback, hybrid social/monetary punishment).
- **External validity:** The evidence base is **laboratory dominated**; field, large-scale, and “real-world” settings are less well represented, and these may feature different dynamics (e.g., scaling, legitimacy of punishment).
- **Cultural/normative moderation:** There is **substantial variance** across cultures, group types, and populations in both the use and impact of punishment (Bruhin et al., 2020; Mantilla et al., 2021).
- **Mechanistic ambiguity:** In complex or dynamic environments (CPRs, extraction, dynamic institution formation), the **effective impact of punishment on efficiency is less predictable**, and sometimes negative, due to informational noise, mis-targeting, or perverse incentives.
- **Behavioral vs. payoff outcomes:** A number of otherwise-relevant papers **report only cooperation or contribution rates, not efficiency**, and cannot substitute for direct efficiency findings.
- **Complex interplay of design moderators:** Many key moderators (e.g., information structures, group composition, punishment targeting) interact in **nonlinear ways**; simple additive models may fail to capture these effects.
- **Punishment cost impact:** As punishment cost rises, or if punishment is available in the absence of clear norm consensus or adequate information, **punishment can reduce efficiency** (Vollan et al., 2019; Tanimoto, 2018).
- **Model boundary:** The reviewed evidence is **most generalizable to repeated, small-group, laboratory PGGs**; caution is needed when extrapolating to complex, asymmetric, or field settings (Acemoglu & Wolitzky, 2021).

---

**In summary:**  
- The literature supports a robust, **directionally positive prediction for the effect of enabling punishment on group efficiency in standard PGGs**, but with **crucial qualifications** based on group composition, information, punishment cost/impact, and institutional detail.
- **Efficiency gains are conditional** and depend on avoiding antisocial punishment, ensuring transparent and accurate information, and structuring punishment to be cost-effective and norm-aligned.
- **Prediction from control efficiency and design parameters is well supported** in canonical settings, but **extrapolation beyond core PGG variants requires care** due to context-sensitive moderators and occasional reversal of the efficiency benefit.
