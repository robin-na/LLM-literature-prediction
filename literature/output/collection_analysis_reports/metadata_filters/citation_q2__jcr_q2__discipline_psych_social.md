# 1) Evidence Base

The paper set consists predominantly of empirical laboratory experiments (especially standard or variant public goods games (PGGs) with controlled manipulations) alongside a smaller number of theory and agent-based modeling papers. Methodological coverage is broad in terms of subject populations, institutional settings, and mechanisms studied, but direct, quantitative evidence mapping game design dimensions (and control efficiency) to treatment efficiency with punishment is confined to a subset of highly relevant lab-based PGG experiments. The theoretical papers offer valuable mechanism insights but are limited in providing empirical calibrations. Many included papers are only adjacent to PGGs or the efficiency outcome, often focusing instead on cooperation rates, norm compliance, or psychological/behavioral drivers of punishment. Thus, the evidence base is moderately broad in addressing mechanisms and moderators, but only a sub-block provides strong, highly applicable data for the exact prediction task.

# 2) Task Relevance

- **pgg_or_variant**:  
  - Relevance is `exact` for roughly half the paper set, which use standard linear or threshold PGGs. Others are `close` (e.g., threshold PG, resource extraction, tax evasion, cross-group or organizational structure), `adjacent` (ultimatum, dictator, trust, bargaining games), or `weak/none` for studies with different core dilemmas or outcome structures.
- **punishment_or_sanctions**:  
  - The coverage of punishment is strong, with many studies directly manipulating or modeling peer or exogenous punishment, covering peer punishment (`exact`), endogenous/centralized punishment (`close`), and non-monetary/reputational sanctions (`adjacent`). Some studies only reference punishment mechanisms as context or background (`weak/none`).
- **efficiency_or_related_payoff_outcome**:  
  - There is a pronounced drop in direct relevance: only a limited subset measure **efficiency** or payoff as a central or primary outcome (`exact`). Many report only on contribution rates, compliance, behavioral responses, or norm adherence (`adjacent`/`close`). Several influential PGG punishment papers infer efficiency from increased contribution but do not always explicitly report group earnings net of punishment costs.

# 3) Outcomes Measured In The Literature

- **Payoff-based outcomes**:  
  - *Efficiency* (group earnings as a fraction of the cooperative optimum) is directly measured in a small set of high-quality lab PGG studies (e.g., Wang & Qin, 2015; Waichman & Stenzel, 2019; Vollan et al., 2019; Kol'veková et al., 2021). Some provide clear evidence on group payoff, welfare, or surplus as primary outcomes. A few theory papers report efficiency as a simulated/model outcome.
- **Non-payoff behavioral outcomes**:  
  - The majority of studies focus on behavioral measures: contribution/cooperation rates, norm compliance, punishment (and antisocial punishment) frequency, rule adherence, and the social evaluation of punishers/rewarders. While these correlate with efficiency under some circumstances, they are not synonymous and can diverge—particularly when punishment costs are high or antisocial punishment prevails.

# 4) Main Findings Relevant To Prediction

- **Punishment generally increases efficiency in standard linear PGGs**:  
  - Enabling peer or exogenous punishment robustly increases efficiency/group earnings relative to control (no-punishment) when the punishment is appropriately designed and feedback is salient (Wang & Qin, 2015; Waichman & Stenzel, 2019; Grieco et al., 2017).  
  - Tangibility and immediacy of punishment (cash vs. token; delay and feedback) matter, especially in early rounds, but adaptation can attenuate these differences over time (Wang & Qin, 2015).
- **Design of punishment institution strongly moderates the effect**:  
  - Assigning punishment rights to high contributors (with turnover) can further increase efficiency beyond decentralized regimes; random assignment does not (Grieco et al., 2017).
- **Punishment cost and cost-effectiveness are critical**:  
  - If punishment is low-cost and shared or endogenous, efficiency can be substantially increased at minimal cost (Kol'veková et al., 2021).  
  - High punishment costs or poorly targeted punishment (due to lack of feedback or costly monitoring) can erode or eliminate efficiency gains (Waichman & Stenzel, 2019; Vollan et al., 2019).
- **Threshold and externality structure matters**:  
  - In threshold/TPGGs and extraction games, punishment may not increase efficiency, as the costs (including antisocial punishment) can outweigh cooperation gains (Vollan et al., 2019).
- **Antisocial punishment and group composition**:  
  - High levels of antisocial punishment (especially in peer/self-governed settings) can negate welfare gains and even make punishment net-detrimental (Vollan et al., 2019).
- **Feedback and punishment salience**:  
  - Salient, timely feedback between rule violation and punishment is needed for punishment to increase efficiency; otherwise, costs are high and net welfare is not improved (Waichman & Stenzel, 2019).
- **Other insights**:  
  - The main positive effects for efficiency are seen when reward is absent or not available (papers with reward mechanisms analyze different dynamics).  
  - Coordination through communication or leadership can sometimes substitute for punishment in raising efficiency, but when both are present, their interaction is less well quantified (Morgan et al., 2019).

# 5) Prediction Guidance

- **Core implication**:  
  - When predicting the group efficiency of a PGG-like game with peer punishment enabled (vs. control), draw on direct empirical evidence from standard linear PGGs: expect a substantial and statistically significant increase in efficiency, provided punishment design is effective (low-to-moderate cost, well-targeted, feedback is salient, and antisocial punishment is limited).
- **Control efficiency as a baseline**:  
  - The efficiency gain from punishment is much larger when the control (no-punishment) efficiency is low to moderate. Where control efficiency is near the cooperative optimum, marginal gains from punishment are smaller and can even be negative if punishment costs are not offset by increased cooperation.
- **Design dimensions as moderators**:  
  - **Player count**: Most strong-evidence studies focus on small groups (N=4-5); generalization to very large groups should be cautious (Kritikos & Bolle, 2004; Bshary & Bshary, 2010) as the incentive to punish weakens in large groups.
  - **MPCR**: Most direct studies use MPCR ~0.4–0.5; both higher marginal returns and threshold structures may alter the net impact of punishment (Kol'veková et al., 2021; Vollan et al., 2019).
  - **Punishment cost/tech**: Efficiency rises with lower punishment cost and more targeted or endogenous mechanisms. High cost or random/untargeted punishment risks net efficiency loss.
  - **Punishment/feedback linkage**: Delays or ambiguity in linking punishment to norm deviations degrade the efficiency effect.
  - **Presence of antisocial punishment**: Group heterogeneity and social conflict increase the risk of antisocial punishment and thus reduce efficiency gains or cause net losses.

- **When outcome measures are not efficiency**:
  - Be explicit: increases in contribution or cooperation rates under punishment usually, but not always, translate to higher efficiency—if punishment costs and mis-targeting are non-trivial, net efficiency gains may not follow.  
  - Absence of reported payoff/efficiency means efficiency impact must be treated as indeterminate despite reported increases in behavioral compliance or contributions.

# 6) Design Dimensions Highlighted Across Papers

- **Directly informed**:  
  - `player_count`, `num_rounds`, `mpcr`, `punishment_cost`, `punishment_tech`, `all_or_nothing`, `chat`  
    (These dimensions are commonly manipulated and precisely reported in payoff/mechanism-focused PGG experiments.)
- **Indirectly informed/contextually discussed**:  
  - `show_n_rounds`, `show_other_summaries`, `show_punishment_id`  
    (Occasionally specified, but with limited analysis of their direct impact on efficiency except for feedback salience.)
  - `reward_exists`, `reward_cost`, `reward_tech`  
    (Some studies explicitly exclude these, others study reward as an alternative/comparison, but not as a joint treatment.)
  - `default_contrib`  
    (Framing rarely directly analyzed in efficiency terms.)
- **Effectively missing**:  
  - Detailed analysis of `chat` (as opposed to simple communication phases), contextual variations in `default_contrib`, and explicit manipulation of display/information parameters beyond basic feedback mechanisms.

# 7) Important Limitations

- **Sparse direct evidence for efficiency in settings outside standard linear PGGs**:  
  - Most reliable findings are for small-group, repeated, linear public goods games; extrapolation to field settings, threshold/extraction games, tax evasion, or organizational contexts should be made with caution.
- **Insufficient attention to large groups and group heterogeneity**:  
  - Few studies analyze the effect of player count above 4-5, or systematically vary group diversity, status, or cross-group affiliations, which are known moderators of punishment behavior and antisocial punishment.
- **Prevalence of non-payoff outcomes**:  
  - Many papers report only behavioral outcomes, making inferences about efficiency indirect and uncertain, especially when punishment is frequent or antisocial.
- **Limited coverage of some design dimensions**:  
  - Few studies isolate the effect of communication (`chat`), default framing, or punishment visibility (`show_punishment_id`) on efficiency beyond basic feedback.
- **Ambiguity in the effect under threshold and extraction game structures**:  
  - Some papers (Vollan et al., 2019) provide evidence of net welfare loss with punishment in threshold/extraction settings, mainly due to costly/antisocial punishment.  
  - Others (Kol'veková et al., 2021) find efficiency gains with endogenous, low-cost punishment structures—heterogeneity in impact remains unresolved.
- **Unmeasured long-term and contextual effects**:  
  - Most results are short-to-medium term laboratory findings; effects may differ under longer horizons, repeated group formation, or after withdrawal of punishment mechanisms.

---

**References (examples):**  
- Wang & Qin, 2015; Waichman & Stenzel, 2019; Grieco et al., 2017; Vollan et al., 2019; Kol'veková et al., 2021; Kumakawa, 2013; Morgan et al., 2019; Kritikos & Bolle, 2004; Bshary & Bshary, 2010.  
(Full APA-style references are available per the source lines above.)
