# 1) Evidence Base

The provided evidence base is **theoretical** and simulation-driven: all 169 reviewed papers employ formal modeling, computational simulation, or conceptual synthesis rather than laboratory or field experiments. Despite the absence of direct empirical studies, the theoretical scope is broad, encompassing a variety of public-goods games (PGGs), close variants, and adjacent settings including common-pool resource games, threshold dilemmas, and leader-follower structures. The literature is dense and specialized on evolutionary and game-theoretic mechanisms, with substantial attention to how punishment (and sometimes reward or exclusion) affect the evolution of cooperation and, crucially, efficiency or payoff outcomes.

There is rich coverage of payoff-based variables (efficiency, group payoff, welfare) in direct PGG models and extensions, though a significant minority of papers focus on behavioral outcomes (contribution rate, cooperation frequency) without reporting efficiency per se. The set includes precise analytical models mapping design dimensions to efficiency effects, as well as more mechanism-focused work highlighting key moderators such as institutional integrity, corruption, exclusion, resource growth, social norms, and information structure.

# 2) Task Relevance

**pgg_or_variant:**  
- **Exact relevance:** The literature includes numerous exact PGG models, usually with continuous or all-or-nothing contribution, explicit group formation, and standard efficiency measurement.  
- **Close relevance:** Many papers expand to variants like threshold PGGs, common-pool resource games, collective-risk dilemmas, and trust/lending games, retaining core strategic structure but introducing ecological or social parameters.  
- **Adjacent/weak relevance:** Papers on the prisoner's dilemma or donation games, or those with only indirect mapping to PGGs, are classified as adjacent; their contribution is mostly mechanistic rather than directly predictive for the target setting.

**punishment_or_sanctions:**  
- **Exact relevance:** Punishment is a central manipulator in many models, with explicit cost, magnitude, and technological variants (peer, pool, institutional, exclusion).  
- **Close/adjacent/weak relevance:** Related mechanisms such as exclusion, reputation, ostracism, indirect sanctions, and leader-enforced punishment are present and often yield similar functional roles, but may not map exactly to peer punishment as implemented in typical PGGs.

**efficiency_or_related_payoff_outcome:**  
- **Exact/close relevance:** Many papers assess group efficiency as total payoff relative to the full cooperation benchmark, aligning directly with the prediction target. Some report closely related outcomes (total coins, welfare, average group payoff, group achievement in threshold/risk games).  
- **Adjacent/weak relevance:** A notable portion reports primarily on contribution rates or cooperation frequency, with only qualitative or speculative links to final payoffs or efficiency, or restricts attention to strategy dynamics.

# 3) Outcomes Measured In The Literature

- **Payoff-related (task-aligned):**  
  - Group efficiency (as explicitly defined): ratio of realized to possible group payoff under full cooperation.  
  - Total group payoff, welfare, surplus.
  - Related: sum of individual payoffs, maximal group profit, resource sustainability, group achievement in threshold games.

- **Non-payoff behavioral (not directly aligned but informative):**  
  - Average contribution/cooperation rate.
  - Frequency of cooperative/punitive/exclusionary strategies.
  - Reputation or social norm compliance.
  - Emergence or stability of cooperation under various evolutionary dynamics.
  - Prevalence of antisocial punishment or second-order free-riding.
  - Inequality or distributional outcomes.

# 4) Main Findings Relevant To Prediction

- **Punishment tends to increase efficiency when:**
  - It is effective (high impact on defectors), not prohibitively costly, and structured to avoid antisocial or misguided targeting (Salahshour, 2021; Gao et al., 2020; Cui et al., 2019; Liu et al., 2018; Hintze et al., 2020; Murase & Baek, 2021).
  - Applied equally and transparently, without institutional corruption, and when accompanied by sufficient observability and conditional strategies (Acemoglu & Wolitzky, 2021; Garcia & Traulsen, 2019).
  - Used in settings with high marginal per-capita return (mpcr), moderate group size, and proportionate cost/fine parameters (Gao et al., 2020; Duong & Han, 2021; Chen & Szolnoki, 2018).
  - Prosocial exclusion mechanisms, when available, may outperform traditional costly punishment on efficiency (Liu & Chen, 2020; Liu et al., 2019).

- **Punishment can reduce or fail to increase efficiency when:**
  - Antisocial punishment (punishing cooperators) is prevalent or not normatively constrained (Fehr & Schurtenberger, 2018; Lee et al., 2019).
  - Institutional punishment can be corrupted or subject to rent-extracting leaders/extortion (Dong et al., 2019; Garcia & Traulsen, 2019; Barron & Guo, 2021).
  - Punishment is misaligned with group incentives (e.g., competitive environments, excessive severity/cost, or power-asymmetric relationships; Honjo & Kubo, 2020; Phillips, 2018; Ille, 2021).
  - Environmental or ecological context (e.g., insufficient resource growth, or in threshold games with low baseline cooperation) counteracts the positive effects of raised cooperation (Chen & Szolnoki, 2018; Wang et al., 2021).

- **Moderator mechanisms and game design effects:**
  - The efficiency effect of punishment is typically monotonic with punishment effectiveness (fine), non-monotonic with punishment cost (optimal at intermediate cost), and positively moderated by mpcr.
  - Reward mechanisms are often comparably or more effective at increasing efficiency, especially when decision errors or corruption undermine punishment (Dong et al., 2019; Sun et al., 2021; Chen, Q. et al., 2020).
  - The effect of punishment is highly contingent on the consensus threshold, information structure, observability (e.g., show_punishment_id, show_other_summaries), and the presence of communication/chat for norm establishment (Gao et al., 2020; van Dijk & De Dreu, 2021).

# 5) Prediction Guidance

- **Strong prediction basis:**  
  - If the control game efficiency is low and the game enables effective, non-corruptible, well-calibrated punishment (suitable punishment cost to fine ratio, no antisocial or extortive dynamics), **efficiency is likely to increase when peer punishment is enabled**—especially when peer punishment is transparent and well-targeted at defectors.

- **Magnitude and boundary cases:**  
  - The efficiency gain is largest when (1) group size is moderate, (2) mpcr is above the cooperation threshold but not so high that cooperation arises spontaneously, (3) punishment is neither too cheap (risking antisocial punishment) nor too costly (no one willing to sanction).  
  - If the control efficiency is already high (i.e., spontaneous cooperation is common), the marginal benefit of punishment may be negligible or negative due to the cost offset.  
  - At low punishment cost and low threshold for action, but with weak or absent norm constraints, antisocial punishment may flourish, potentially **reducing efficiency**.

- **Indirect or context-specific patterns:**  
  - Where exclusion or leader-based institutional punishment is available and used to target defectors, efficiency gains may be larger than for decentralized costly punishment.  
  - In settings allowing for corruption, extortion, or ambiguous targeting, enabling punishment can backfire, yielding lower average payoffs than the no-punishment baseline.  
  - Ecological/resource constraints or extreme group heterogeneity can modulate or even reverse the benefit from punishment.

- **Uncertainty:**  
  - Most evidence is theoretical or from simulation, and parameter specificity for empirical settings is often lacking.
  - Behavioral outcomes may not always translate to efficiency improvements; high cooperation rates achieved via costly punishment may leave net payoffs unchanged or lower.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed:**  
- `player_count` (group size): Most models specify this and analyze its impact explicitly (Duong & Han, 2021; Gao et al., 2020).
- `mpcr`: Central to nearly all payoff-based modeling as the driving parameter for cooperation/defection tradeoffs.
- `punishment_cost` & `punishment_tech`/ `punishmentMagnitude`: Nearly all directly modeled, with comparative statics on cost, effectiveness, and targeting (peer, pool, institutional).
- `all_or_nothing`: Many works study both binary and continuous contribution settings.
- `reward_exists`, `reward_cost`, `reward_tech`: Explicitly compared in several models assessing efficiency tradeoffs.
- `num_rounds`: Infinite, repeated, and finite games all considered (though infinite/index limit is most common).

**Indirectly informed:**  
- `show_punishment_id`, `show_other_summaries`: Modeled as observability/conditional strategies, with importance for sustaining cooperation.
- `chat`: Discussed as communication/norm formation; not always manipulated directly.
- `default_contrib`: Framing and default choice indirectly shown to affect behavior and norm compliance.

**Only contextually discussed or sparse:**  
- `show_n_rounds`: Sometimes included to address shadow-of-the-future effects.
- `show_other_summaries`: Related to information structure, sometimes addressed as "public signals" or observability.
- `reward_exists`, `reward_cost`, `reward_tech`: Directly modeled where rewards are the focus but less so in pure punishment studies.

**Effectively missing:**  
- Explicit individual-level or empirical variations in behavioral type prevalence (`conditional cooperators`, etc.) are often assumed or exogenously set.

# 7) Important Limitations

- **Absence of empirical (lab/field) data:** All results are theoretical/simulation-based. Generalizability to real human behavior, especially outside well-specified payoff structures, is uncertain.
- **Imprecision regarding effect size:** While directional predictions (punishment increases/decreases efficiency) are robust, precise quantitative estimates for specific parameter regimes are generally lacking.
- **Insufficient outcome reporting:** Many studies use behavioral outcomes (cooperation rate) as proxies for efficiency. Where the link between cooperation and group payoff is not explicated, it introduces potential bias or overestimation of punishment's positive impact.
- **Context sensitivity and cross-model disagreement:** Contradictory predictions emerge when considering antisocial punishment, institutional corruption, leader opportunism, or ecological/resource constraints—highlighting that enabling punishment is not uniformly beneficial.
- **Limited mapping for certain design dimensions:** Dimensions like `chat`, `default_contrib`, `show_punishment_id`, and complex information structure are often included only as conceptual moderators, not formal model parameters.
- **Reward and exclusion mechanisms:** Literature shows that exclusion or reward can sometimes outperform punishment in increasing efficiency, especially under error or corruption, complicating predictions where these mechanisms coexist.
- **Potential cultural and power-structure bias:** Mechanisms may not transfer directly to settings with pronounced power asymmetries, social value orientation effects, or where external validity (e.g., real-world norm enforcement) is weak.

---

**Summary:**
The literature robustly supports the expectation that **enabling peer (or well-structured institutional) punishment typically increases efficiency relative to a no-punishment control in public goods games**, but with significant qualifications: this is **contingent on punishment being cost-effective, well-targeted, normatively constrained, and not vulnerable to corruption or misuse**. The magnitude and even direction of the effect can reverse in the presence of antisocial punishment, leader extortion, ecological constraints, or poor institutional design. Design dimensions such as `mpcr`, `punishment_cost`/`punishment_tech`, group size, and observability of actions are the most strongly evidenced moderators for prediction.

For **downstream prediction**, these models enable both qualitative and, in some cases, formula-based efficiency forecasting, but careful attention is required to the risk of mapping behavioral (non-payoff) outcomes onto efficiency, and to the unmodeled context variables that may strongly moderate real-world effects.
