# 1) Evidence Base

The paper set comprises primarily **empirical, experimental laboratory studies**—with the overwhelming majority directly manipulating institutional and peer punishment in public-goods-game (PGG) or PGG-variant settings. A substantial subset of papers measures efficiency- or payoff-based outcomes, often reporting both behavioral (contribution) and efficiency (group payoff as a fraction of the social optimum) metrics. Some papers provide close variants (e.g., threshold PGGs, common-pool resource (CPR) games, centralized sanctioning, hierarchical structures, quasi-naturalistic field experiments), which augment the evidence base and support contextualization of results.

A smaller portion of the set addresses adjacent designs (e.g., dictator/ultimatum games, third-party punishment, exit/ostracism, non-monetary sanctions) or focuses on behavioral/psychological moderators rather than efficiency. Observational and theory contributions are rare and generally used for context, not primary evidence.

In terms of **breadth**, the literature is reasonably comprehensive for the specific prediction task (PGG with and without punishment), covering multiple dimensions (e.g., cost/impact structure, information, group size, heterogeneity, feedback), but **some game design dimensions (e.g., chat, show_n_rounds, show_other_summaries, default_contrib)** are only sometimes directly manipulated or discussed.

# 2) Task Relevance

**pgg_or_variant:**  
- **Exact relevance:** The majority of direct-evidence papers use standard linear PGGs or canonical step-level variants; several others use close variants (threshold games, CPR, hierarchical production).
- **Close/adjacent relevance:** Some experimental work is adjacent (e.g., dictator/ultimatum games, peer reporting, resource-extraction games), contributing context on punishment/cooperation but not directly estimating efficiency.

**punishment_or_sanctions:**  
- **Exact relevance:** A large proportion of studies directly manipulate punishment (peer, centralized, exogenous, endogenous, probabilistic, severity/cost, selection mechanisms), often as the main treatment variable.
- **Close/adjacent relevance:** Several papers examine reward, exit/exclusion, non-monetary/social sanctions, or combinations with punishment.
- **None/weak relevance:** Few studies without punishment or focusing only on baseline (no-punishment) cooperation.

**efficiency_or_related_payoff_outcome:**  
- **Exact relevance:** Approximately half the set provides exact measures of group payoff/welfare, efficiency ratios, or closely analogous surplus/welfare outcomes.
- **Close/adjacent relevance:** Many others report contribution rates, norm compliance, allocation fairness, or behavioral responses as proxies for efficiency, sometimes inferring efficiency shifts from contribution data (with or without adjustment for punishment costs).
- **None/weak relevance:** Some studies focus only on non-payoff behaviors or hypothetical scenarios, which inform psychological mechanisms but not quantitative efficiency predictions.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes:**
- **Reported directly:**  
  - Group payoff / earnings, total welfare, average individual/aggregate payoffs, surplus ratios, provision rates (step-level games), and efficiency (payoff/optimum).
- **Reported as close proxies:**  
  - Contribution data combined with knowledge of MPCR and cost structure (permits back-calculation of efficiency), group income/net surplus after punishment/reward costs, sometimes reported in figures or tables.
- **Less commonly or not reported:**  
  - Distributional consequences (inequality, variance in payoffs), downside risk (e.g., loss of all contributions in threshold games).

**Non-payoff behavioral outcomes:**  
- Contribution rates, frequency of cooperation/defection, norm compliance, frequency and severity of punishment/reward administered, antisocial punishment, beliefs about others, acceptance/rejection rates (ultimatum/dictator), psychological/affective responses, social evaluations/reputation effects, voting or selection for institutions, and norm salience.

**Key distinction:**  
Several studies note that increased contributions under punishment **do not always translate into increased efficiency**, as punishment costs or antisocial misuse can offset gains. Some designs report that efficiency can decline with punishment, or that reward mechanisms yield higher efficiency than punishment despite similar or even smaller contribution increases.

# 4) Main Findings Relevant To Prediction

**Empirical results:**
- **Punishment often increases efficiency over control:** In repeated linear PGGs, the introduction of peer or centralized costly punishment regularly produces substantial increases in group efficiency, provided that punishment is effective and not overly costly (Fehr et al., 2002; Waichman & Stenzel, 2019; Wang & Qin, 2015; Qin & Wang, 2013; Joseph et al., 2025).
- **Efficiency gains not guaranteed:** Multiple papers demonstrate *no effect, small effect, or even negative effect* of punishment on efficiency. This occurs when:
  - Punishment is used extensively and costs are high (Botelho et al., 2022; Decker et al., 2003; Vollan et al., 2019).
  - Antisocial punishment is common (punishment of cooperators as well as defectors).
  - Punishment is not effectively targeted (random punishment, poor feedback, costly monitoring, inefficiency in design; Fatas et al., 2010; Goeschl & Jarke, 2016).
  - The group structure is privileged/heterogeneous, with poor norm targeting (Reuben & Riedl, 2009).
  - The effect of punishment depends on design features such as who assigns punishment and selection mechanism (Grieco et al., 2017; Benard & Barclay, 2020).
- **Magnitude and type of punishment matter:** Small penalties may not deter or may even reduce efficiency if used frequently, while larger/more effective punishment can improve efficiency but risk higher costs and retaliation if misapplied (Ye et al., 2023; Waichman & Stenzel, 2019).
- **Reward and hybrid mechanisms:** In direct comparisons, reward typically increases efficiency more than punishment, primarily because reward mechanisms add to group surplus rather than reducing it (Gürerk et al., 2009; Drouvelis et al., 2017).
- **Information and feedback critical:** The effect of punishment on efficiency is stronger when feedback is salient and norm violations are observable; delayed or anonymous punishment (or poor feedback) reduces the efficiency gain, sometimes completely (Waichman & Stenzel, 2019; Decker et al., 2003).
- **Institutional context / social learning:** Social history, transparency, and endogenous institution choice can amplify the positive effect of punishment on efficiency, particularly via lowering wasted punishment and coordinating expectations (Gürerk, 2013).
- **Group composition and structure:** Democratic leader selection (Benard & Barclay, 2020), top-contributor punishment assignment (Grieco et al., 2017), and privileged group heterogeneity (Reuben & Riedl, 2009) significantly moderate efficiency effects.

**Key takeaways:**
- **Punishment's effect on group efficiency is conditional**—not universally positive.
- **Control-game efficiency is informative,** but the marginal effect of punishment also depends heavily on game mechanics (cost, targeting, information, group structure, punishment severity, availability of reward, monitoring, enforcement scope).
- **Behavioral increases in cooperation/contribution are insufficient for positive efficiency impact**—punishment cost and misuse (e.g., antisocial punishment) often offset gains.

# 5) Prediction Guidance

**How should this literature inform prediction of treatment efficiency from design dimensions and control efficiency?**

- **Baseline (control) efficiency is an important predictor,** but **not sufficient**—the marginal effect of enabling punishment frequently depends on several key moderators.
- **Punishment increases efficiency when:**  
  - Punishment is low to moderate in cost and high in impact (cost/impact>1:3).
  - Information feedback is clear: players can reliably identify norm violators.
  - Antisocial/retaliatory punishment is rare or institutionally mitigated.
  - Group is relatively homogeneous (no large privileged/minority members with different returns).
  - The punishment institution is appropriately structured (not random, not unrestricted; potentially leader-based or with selection rules promoting targeted deterrence).
  - Players have access to social history, or feedback channels support learning/convergence to cooperation.
- **Punishment may fail to increase (or may reduce) efficiency when:**  
  - The mechanism induces high costs, excessive punishment, or is used antisocially.
  - Feedback is absent, punishment is anonymous or poorly targeted, or monitoring is costly.
  - The group is heterogeneous in benefits, with privileged members less responsive.
  - The design encourages emotional or retaliatory punishment (collective rules, high uncertainty, lack of institutional checks).
  - Reward or hybrid mechanisms are available and perform better in raising both contributions and efficiency.
- **Non-monotonic or inverse-U effects:**  
  - There is often a non-linear relation between punishment probability/severity and efficiency: some punishment is effective, but too severe or too probabilistic punishment may erode efficiency (Qin & Wang, 2013).
- **Interaction with other mechanisms:**  
  - Feedback, social learning, reputation, and reward are strong positive moderators of efficiency, sometimes outperforming or substituting for punishment.
- **Dimension-specific adjustments:**  
  - Short games (few rounds): punishment's effect may be minimal or dominated by first-round contributions.
  - One-shot or low baseline cooperation: punishment may make little difference, especially when used infrequently (Funk & Mischkowski, 2022).
  - Threshold/all-or-nothing games: effect of punishment on efficiency can be complex—raising contributions but increasing risk of collective failure or deadweight loss (Joseph et al., 2025).

**Recommendation for prediction:**  
- **Start from control efficiency;** incorporate adjustments based on: MPCR, punishment cost/impact, feedback/information structure, group composition, and evidence for available moderators (e.g., social learning, institution selection, reward availability).
- When specific design parameters are matched to high-relevance studies in the set, **use those quantitative shifts in efficiency** (treatment vs. control) as prior adjustment factors.
- For **missing or contextually discussed dimensions (e.g., chat, default_contrib, visibility, reward tech),** be cautious—literature is thin and findings should be incorporated with wide uncertainty.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions (regularly manipulated, measured, or reported):**
- `player_count`: Consistently reported; both small (2-5) and larger groups represented, but most findings drawn from groups of 3–5.
- `num_rounds`: Almost always specified; literature covers both one-shot and repeated settings, with strong evidence that round structure moderates punishment's effect.
- `mpcr`: Always reported; central to mapping contributions to efficiency.
- `punishment_cost`/`punishment_tech`: Directly specified in all punishment studies; often varied across treatments to probe efficiency effects; includes cost/impact ratio, probability, and severity.
- `all_or_nothing`: Manipulated in some studies; both continuous and binary contributions addressed.
- `reward_exists`/`reward_cost`/`reward_tech`: Present in several studies for comparison; direct evidence that reward mechanisms, when available, often yield higher efficiency than punishment.
- `chat`: Varied; rarely the central manipulation, but its presence/absence is always reported and sometimes shown to affect efficiency in conjunction with punishment.
- `show_other_summaries`, `show_n_rounds`: Occasionally reported as context, but not the main focus; evidence for their moderating effect is secondary.

**Indirectly informed or only contextually discussed:**
- `default_contrib`: Rarely manipulated or highlighted; framing as opt-in/out is infrequently addressed.
- `show_punishment_id`: Disclosure of punishment assigner’s identity is mentioned in some contexts, but few direct comparisons.
- `show_other_summaries`: Sometimes noted as part of the information/feedback environment but not systematically varied.

**Effectively missing:**
- No systematic experimental evidence directly manipulates `default_contrib` or `show_punishment_id` as central dimensions for efficiency.
- Few papers analyze the interaction of `chat` with punishment in regard to efficiency (most focus on cooperation or norm formation, not payoffs).
- Dimensions like `show_n_rounds`, unless paired with strategic uncertainty treatments, are underexplored.

# 7) Important Limitations

- **Efficiency reporting is incomplete:**  
  - Many otherwise relevant studies report only behavioral (contribution/cooperation) outcomes, precluding direct estimation of the effect of punishment on efficiency.
  - Some designs (e.g., threshold games, CPR) produce ambiguous efficiency implications, as success/failure and risk are confounded with cost effects.
- **Experimental generalizability:**  
  - Most direct-evidence studies use small groups, lab protocols, and university student pools; results may not generalize to large-group, field, or naturally occurring PGG-like environments.
- **Sparse coverage of some design dimensions:**  
  - Dimensions like messaging/chat, default contribution framing, punishment identity disclosure, or more complex information structures (e.g., show_other_summaries, show_n_rounds) are rarely the focus.
- **Heterogeneity in punishment design:**  
  - Direct comparability between studies is sometimes limited by variation in punishment implementation (peer vs. centralized, probabilistic vs. deterministic, leader/administered vs. decentralized).
- **Ambiguity from adjacent/close variants:**  
  - Close variants (e.g., third-party punishment, CPR/extraction games, step-level/threshold games, exit/exclusion as sanction) offer valuable context, but findings may not cleanly transfer to standard linear PGGs for quantitative prediction.
- **Nonlinear and context-dependent effects:**  
  - The effect of punishment is not uniform; factors such as group composition, baseline efficiency, information feedback, punishment/reward cost structure, and presence of alternative institutions strongly moderate the observed efficiency impact.
- **Scarcity of long-run or real-world studies:**  
  - Most evidence is from short- to medium-horizon experiments. Effects of punishment on efficiency in more real-world, longer-term, or high-stakes scenarios remain underexplored.
- **Potential publication bias:**  
  - There is some risk that null or negative results may be underrepresented, given the salience of positive punishment effects in the original literature. However, this digest includes multiple null/negative findings as well.

---

This evidence synthesis **strongly supports using game design dimensions and control efficiency as foundational predictors for treatment efficiency,** **provided modelers adjust for the presence or absence of key design features above.** Reliable prediction should account for punishment's cost/impact ratio, information feedback, group composition, and the possibility of alternative positive incentives (rewards), with full recognition that efficacy and efficiency gains are context-dependent—not universal.
