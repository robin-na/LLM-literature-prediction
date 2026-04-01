# 1) Evidence Base

The paper set consists predominantly of **empirical laboratory experimental studies** focused on repeated linear public goods games (PGGs), with some high-quality **field experiments**, as well as a substantial number of **theoretical and modeling papers**. The empirical papers are generally **narrow in focus** on the voluntary contribution mechanism (VCM) and explicit peer punishment—sometimes with variations on institutional features or mechanisms like ostracism, voting, or social disapproval. There is also **coverage of related environments** (common-pool resource (CPR) experiments, principal-agent games, trust/investment games, spatial/network PGGs), and papers exploring the **evolutionary, cultural, and psychological foundations** of punishment and cooperation.

The **breadth for the prediction task** (predicting efficiency effects of enabling peer punishment in PGG-like environments) is good for standard lab PGGs, covering the majority of core design dimensions, but considerable heterogeneity and some gaps appear for less standard designs (e.g., spatial/networked games, CPRs, non-lab contexts, social/indirect punishment).

# 2) Task Relevance

Assessed by the three target-relevance dimensions:

#### a. pgg_or_variant

- **exact**: Many studies are classic repeated linear PGGs (Sefton et al., 2007; Noussair & Tucker, 2005; Casari & Luini, 2009; Nikiforakis et al., 2010; Reuben & Riedl, 2009, etc.).
- **close**: Some papers address close variants (common-pool resource games, trust/investment games with punishment, or CPRs with PGG structure).
- **adjacent/weak/none**: Several address only related mechanisms (ultimatum games, dictator games, spatial PDGs) or are theoretical without direct PGG implementation.

#### b. punishment_or_sanctions

- **exact**: Majority of high-relevance empirical and model papers directly manipulate peer punishment (costly, individual, or collective).
- **close**: Some study ostracism, social disapproval, or monitor/exclusion mechanisms as functionally similar sanctions.
- **adjacent**: A few rely on reward only or discuss punishment as a concept without explicit implementation.
- **weak/none**: Some omit sanctions or deal with social cues/communication without punitive content.

#### c. efficiency_or_related_payoff_outcome

- **exact/close**: Core lab PGG studies report **efficiency** or group earnings/payoff as primary outcomes. Some field/CPR studies also report these.
- **adjacent/weak/none**: Many studies report **contribution rates**, norm compliance, or punishment frequency (behavioral outcomes) instead. Several theoretical works focus on prevalence of strategies or evolutionary stability, without direct efficiency/payoff reporting.

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes (Direct/Close):**

- **Efficiency:** Defined as group total payoff as a fraction of maximum possible (full cooperation), frequently reported (e.g., Sefton et al., 2007; Kroll et al., 2007; Maier-Rigaud et al., 2010).
- **Group Earnings/Payoff:** Often equivalent to efficiency, sometimes stated in monetary units (Noussair & Tucker, 2005; Casari & Plott, 2003).
- **Welfare / Surplus / Total Coins Generated:** Sometimes used interchangeably with efficiency; consistently captured in the best studies.

**Non-Payoff Behavioral Outcomes (Indirect/Adjacent):**

- **Contribution/Cooperation Rate:** Universal in the literature but not equivalent to efficiency, as increased contributions can be offset by sanction costs.
- **Punishment Frequency/Amount/Targeting:** Often detailed, important for understanding mechanisms.
- **Norm Compliance / Social Approval / Perceived Fairness:** Studied to explain underlying motives or spillovers, not as efficiency measures.

**Theoretical Proxies:**

- **Stationary State Composition, Phase Diagrams:** Used in spatial/theoretical models (e.g., Szolnoki & Perc, 2012), sometimes interpreted as efficiency if defector-free.
- **Evolutionary Stability / Fitness:** Proxy for group outcomes in evolutionary theory, but not directly commensurate with experimental efficiency.

# 4) Main Findings Relevant To Prediction

**Empirical Findings (Efficiency or Related Payoff Outcomes):**

- **Punishment Often Increases Efficiency, But Not Universally:**
  - **Standard lab PGGs:** Enabling peer punishment generally increases group efficiency relative to the control (no-punishment), especially over repeated rounds as cooperation is sustained and punishment use declines (Sefton et al., 2007; Kroll et al., 2007; Fehr et al., 2002; Maier-Rigaud et al., 2010).
  - **Cost Structure Matters:** High cost/weak punishment can offset efficiency gains, while sufficiently strong punishment can yield high net gains (Casari & Luini, 2009; Casari & Plott, 2003; Ostrom, 2006).
  - **Institutional Features Moderate Outcomes:**
    - Punishment that filters out anti-social forms (e.g., consensual mechanisms or ostracism) yields far better efficiency than unfiltered individual punishment (Casari & Luini, 2009; Maier-Rigaud et al., 2010).
    - The possibility of feuds/counter-punishment can sharply reduce or negate efficiency gains (Nikiforakis & Engelmann, 2011).
  - **Heterogeneity Effects:** Punishment's efficiency benefit is reduced in groups with heterogeneous marginal returns or productivity differences (Reuben & Riedl, 2009; Tan, 2008).
  - **Role of Communication:** Communication itself has strong positive effects on efficiency; punishment adds little beyond communication (Bochet et al., 2006).

- **When Punishment Does Not Improve—Or May Reduce—Efficiency:**
  - **High costs, anti-social punishment, or retaliatory cycles** can erase the efficiency gains from sustaining high contributions, especially in games prone to "perverse" punishment or feud escalation (Decker et al., 2003; Bochet et al., 2006; Nikiforakis & Engelmann, 2011).
  - **Contextual Social Sanctions** (social disapproval, shame) may outperform monetary punishment in maintaining high efficiency (Lopez et al., 2012; Carpenter & Seki, 2011).

**Theoretical and Mechanism Arguments:**

- Theory generally supports the **potential** for punishment to increase efficiency, provided the cost to the punisher is not too high relative to impact and the population has mechanisms to stabilize cooperation (Sethi & Somanathan, 2003; Gardner & West, 2004; Henrich & Henrich, 2006).
- **Adaptive and consensual mechanisms** outperform fixed or unfiltered punishment, especially in spatial or networked games (Perc & Szolnoki, 2012; Szolnoki & Perc, 2012).
- **Collective action and cultural transmission** models highlight the role of punishment in sustaining high cooperation rates, but **do not always guarantee efficiency gains** unless specific structural preconditions are met (e.g., adequate monitoring, sufficient reciprocators, or group-level selection).

# 5) Prediction Guidance

- **Direct Use of Control Efficiency:** For standard repeated linear PGGs with peer punishment enabled (with specified punishment cost/impact, and absent communication or reward), the expected efficiency should be **higher** than the control, conditional on:
    - **Punishment is not prohibitively costly** (cost-impact ratio ≤ 1:2 or better).
    - **Institutional features prevent anti-social punishment** and minimize feuding.
    - **Group is homogeneous or has moderate heterogeneity.**
    - **No overriding features (e.g., intermediation, ambiguous punishment targeting) dampen the mechanism.**
- **Strong Moderators:**
    - **Punishment Cost and Effectiveness (`punishment_cost`, `punishment_tech`)**: Net efficiency gain is positive and increases with higher impact per unit cost.
    - **Feud/Countersanctioning (`punishment_tech`, `show_punishment_id`)**: Punishment that can be retaliated (via identity revelation or repeated pairings) undermines positive efficiency effect.
    - **Institutional Design (`punishment_tech`)**: Consensual, filtered, and ostracism rules consistently improve efficiency over standard individual punishment.
    - **Communication (`chat`)**: If strong chat/communication is present, enabling punishment often has little incremental effect on efficiency.
- **Structural Features:**
    - **Increasing Group Size (`player_count`)**: Weakens the effectiveness of peer punishment and reduces the magnitude of efficiency gains (Carpenter et al., 2009; Gardner & West, 2004).
    - **Marginal Per Capita Return (`mpcr`)**: Higher MPCR increases the return to cooperation and punishment's impact.
- **Time Dynamics:** Efficiency gains arise more in later rounds; in early rounds, sanction costs may temporarily reduce efficiency even with higher contributions.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- `player_count`: Almost all high-relevance experiments vary this.
- `num_rounds`: Well-explored, especially repeated 10–20 round sessions.
- `mpcr`: Explicitly manipulated and reported in most lab studies.
- `punishment_cost`, `punishment_tech`: Central to all punishment-focused empirical papers; cost-to-impact ratios frequently specified.
- `chat`: Several papers manipulate presence/absence of communication.
- `show_n_rounds`: Usually rounds are known; some variation present.
- `all_or_nothing`: Most use continuous contributions, though threshold/nonlinear cases occasionally discussed.
- `reward_exists`, `reward_cost`, `reward_tech`: Some papers feature reward-only or combined sanction/reward schemes (Sefton et al., 2007; Noussair & Tucker, 2005; Szolnoki & Perc, 2012).
- `show_other_summaries`: Typically peer outcomes shown; occasionally manipulated.
- `show_punishment_id`: Varies; anonymity of punishment frequently manipulated with substantial effect on outcomes.

**Indirectly Informed or Contextually Discussed:**
- `default_contrib` (framing): Not systematically varied, occasionally mentioned but rarely as a main treatment.
- Details of feedback timing, summary stats delivery, or interface specifics.

**Effectively Missing / Rarely Informed:**
- Fine-grained manipulations of interface, round uncertainty, or more complex group structures (e.g., networks, dynamic grouping) are less commonly reported in direct-relevance studies.

# 7) Important Limitations

- **Generalizability Beyond Standard PGGs:** Much strongest for 4–6 player, continuous, repeated linear PGGs in the lab; less clear for threshold/nonlinear, spatial, or highly heterogeneous groups.
- **Gaps on Certain Dimensions:** Little evidence about the effect of **default contribution framing**, **ambiguity in punishment/reward identity beyond anonymity**, or more complex information structures.
- **Efficiency Not Always Directly Measured:** Many behavioral studies report cooperation/contribution rather than efficiency; mapping from contribution rate to efficiency is nontrivial when sanction costs are high.
- **Anti-Social Punishment and Feuds:** Studies show that positive effects depend critically on *who* is punished and whether punishment becomes retaliatory—a direction sometimes missing or heterogeneous across studies.
- **Time Dynamics:** Efficiency benefits accrue mostly in the later rounds; short-term experiments or those with high end-period uncertainty may show muted or reversed effects.
- **Field vs. Lab Transferability:** Most direct evidence comes from highly controlled lab settings; translation to field or naturalistic settings with more complex social structures (e.g., real-world or evolutionary contexts) warrants caution.
- **Sparse Evidence on Some Design Interactions:** Effects of multiple interacting features (e.g., punishment **and** communication, or punishment with non-anonymous identity) are less systematically explored.
- **Theory–Empirical Gaps:** Some modelling papers make strong claims about feasibility of efficient punishment under specific evolutionary assumptions that are not always matched by empirical validation.

**Conclusion:**  
For **standard repeated linear public goods games**, enabling well-designed peer punishment usually increases efficiency compared to a control without punishment, with the size and reliability of the effect sensitive to punishment cost/effectiveness, institutional design (particularly anti-social punishment filters and consensus mechanisms), group size, payoff structure, and communication. The **most useful evidence** is available when all key design dimensions are matched and efficiency is directly measured. Caution is required when extrapolating to less-tested dimensions, non-standard designs, or field environments.
