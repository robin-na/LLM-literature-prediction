# 1) Evidence Base

The paper set consists of 13 works, representing a mix of empirical (primarily experimental lab-based studies) and theoretical papers. Empirical papers (e.g., Engel & Zhurakhovska, 2017; Eisenberg & Engel, 2014; Bell et al., 2016) focus on variants of the public goods game (PGG) and provide direct experimental evidence about punishment mechanisms. Several theory and conceptual papers (e.g., Janssen, 2015; Bruner, 2013; Sterelny, 2016; Zhang & van der Schaar, 2013) offer modeling, review, or evolutionary arguments regarding cooperation, punishment, and underlying mechanisms. The literature broadly covers both standard and adjacent settings to the PGG, with some works investigating online, common-pool resource, or norm-governed environments. The bulk of evidence relevant to the prediction task (efficiency impact of enabling punishment in PGG-like settings) comes mainly from a subset of empirical experimental studies and a small number of closely related theoretical models.

# 2) Task Relevance

- **pgg_or_variant**:
  - **Exact**: Strong coverage from empirical lab studies (Engel & Zhurakhovska, 2017; Eisenberg & Engel, 2014; Bell et al., 2016).
  - **Close/Adjacent**: Several theory papers rely on environments structurally similar to the PGG (e.g., Zhang & van der Schaar, 2013's repeated gift-giving; Angourakis et al., 2015's food storage model).
  - **Weak/None**: Some papers (Brevers et al., 2013; Fagundes, 2017) consider dyadic or norm-based social dilemmas only contextually related.

- **punishment_or_sanctions**:
  - **Exact/Close**: Most empirical and theoretical works either manipulate or model peer or centralized punishment (Engel & Zhurakhovska, 2017; Eisenberg & Engel, 2014; Janssen, 2015; Bruner, 2013; Zhang & van der Schaar, 2013).
  - **Adjacent**: Some papers consider sanctions or exclusion as related mechanisms (Angourakis et al., 2015; Fagundes, 2017).
  - **Weak/None**: A minority either do not vary punishment or only mention it contextually (Brevers et al., 2013).

- **efficiency_or_related_payoff_outcome**:
  - **Close/Exact**: A few empirical studies report or allow inference about group payoff/welfare (Engel & Zhurakhovska, 2017; Eisenberg & Engel, 2014; Zhang & van der Schaar, 2013).
  - **Adjacent/Weak**: Most papers report on non-payoff behavioral outcomes (e.g., cooperation rate, norm compliance), not efficiency directly.
  - **None**: Some theory and empirical works do not measure or discuss aggregate payoff outcomes.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes**:
  - Direct measures (profit, group payoff, welfare, efficiency): Reported or inferable in a handful of empirical PGG studies (Engel & Zhurakhovska, 2017; Eisenberg & Engel, 2014), and modeled explicitly in Zhang & van der Schaar (2013), albeit in a non-standard repeated game.
  - Most works do **not** report the efficiency ratio (payoff as a proportion of full-cooperation maximum) directly.

- **Non-Payoff Behavioral Outcomes**:
  - **Most Common**: Contribution rates, cooperation rates, punishment frequency, norm compliance, or behavioral responses to punishment (e.g., Bell et al., 2016; Janssen, 2015; Bruner, 2013; Angourakis et al., 2015).
  - These outcomes inform understanding of underlying processes but do not map directly to efficiency or surplus.

- **Contextual and Conceptual Outcomes**:
  - Theory papers often discuss broader mechanism or outcome constructs, such as reputation, norm evolution, or general cooperation levels, with only indirect reference to payoff or welfare implications.

# 4) Main Findings Relevant To Prediction

- **Empirical studies of repeated PGGs (with and without punishment) consistently find that enabling punishment—especially when it is sufficiently costly to free riders and/or likely to be imposed—increases group payoff and thus efficiency compared to the no-punishment baseline.** Increases in contribution rates translate into higher and more stable group earnings (Engel & Zhurakhovska, 2017; Eisenberg & Engel, 2014).

- **Severity and actual implementation of punishment matter:** Stronger, more certain, or more group-aligned punishment regimes (e.g., treble or class action damages) are most effective in stabilizing cooperation and group welfare. The mere *possibility* of punishment has weaker effects than its actual realization (Eisenberg & Engel, 2014).

- **Punishment is context-sensitive:** Communication, group size, and implementation details (centralized vs. peer punishment, transparency) moderate effects (Janssen, 2015).

- **Non-payoff findings support efficiency improvements but add ambiguity:** Punishment often increases cooperation-related behaviors but may also have side effects, such as increased free-riding in certain conditions (Bell et al., 2016), or may crowd out voluntary agreement (Janssen, 2015).

- **Theoretical and simulation-based models show that well-calibrated punishment mechanisms (including reputation protocols) can raise efficiency to near-optimal levels in repeated interactions, provided cost-benefit ratios and implementation are optimal (Zhang & van der Schaar, 2013).** If punishment is too weak or too harsh, efficiency gains are limited or counterproductive.

- **In adjacent domains, exclusion or access-control mechanisms and informal social sanctions are also theorized to stabilize cooperation, but excessive harshness can reduce overall performance by inhibiting recovery from shocks or discouraging engagement (Angourakis et al., 2015; Bruner, 2013).**

# 5) Prediction Guidance

Based on the available literature:

- **Enabling punishment in repeated public goods games is predicted to raise average efficiency relative to the no-punishment control, especially when the punishment regime is sufficiently strong but not excessively harsh.** The magnitude of improvement depends on design dimensions: group size, number of rounds, punishment cost/severity, transparency, and presence of communication.

- **Control group efficiency serves as a baseline, and the expected gain from adding punishment is greater when control efficiency is low (i.e., when free-riding is prevalent).** Gains may plateau or even decline if the punishment regime is so severe as to discourage participation or if implementation leads to retaliation or over-punishment.

- **When translating findings to new designs, models should adjust for punishment magnitude, cost, authority structure, and presence/absence of group feedback.** Actual efficiency increases are best predicted for designs matching those of Engel & Zhurakhovska (2017) or Eisenberg & Engel (2014): repeated, multi-player, linear PGGs with explicit, endogenous punishment options.

- **Settings with one-shot games, high baseline cooperation, or weak/absent punishment are less likely to experience large efficiency increases.** Adjacent settings with exclusion or reputation-based sanctioning suggest similar, though contextually mediated, effects.

- **Where only non-payoff (behavioral) outcomes are available, predictions about efficiency should be qualified due to the risk that increased punishment raises cooperation but also increases costly punitive actions, potentially offsetting group-level gains.**

# 6) Design Dimensions Highlighted Across Papers

- **Directly Informed Dimensions**:
    - **player_count**, **num_rounds**, **mpcr**, **punishment_cost**: Frequently manipulated and explicitly described in core empirical PGG studies (Engel & Zhurakhovska, 2017; Eisenberg & Engel, 2014).
    - **all_or_nothing**: Some studies distinguish all-or-nothing from continuous contribution games (Bell et al., 2016; Zhang & van der Schaar, 2013).
    - **punishment_tech**: Mode of punishment (centralized/judge vs. peer; authority structure) considered in empirical and theory studies.
    - **reward_exists**: Reward options are noted as absent in most PGG settings discussed, but analyzed in adjunct to punishment (Bruner, 2013).
    - **chat**: Role of communication is highlighted as a moderator but not always manipulated.
    - **show_other_summaries**, **show_n_rounds**, **show_punishment_id**: Occasionally specified in design but rarely manipulated; transparency/feedback sometimes discussed as influencing cooperation.

- **Indirectly or Contextually Discussed**:
    - **default_contrib**: Framing as opt-in/opt-out is occasionally mentioned but not central to main findings.
    - **reward_cost**, **reward_tech**: Reward mechanisms are referenced but less systematically studied.

- **Missing or Sparsely Informed**:
    - Several secondary interface and information structure dimensions (e.g., detailed feedback mechanisms, fine variants of transparency, nuances of framing) are not deeply covered. Some design details, such as exact punishment targeting rules, are often implicit or unreported outside core empirical papers.

# 7) Important Limitations

- **Narrowest evidence is for repeated, linear PGGs with explicit, endogenous punishment:** Most payoff-related findings are concentrated in lab experimental manipulations of standard PGGs. Other papers supply only indirect or contextual support for efficiency predictions.

- **Efficiency as a specific quantitative measure (ratio to social optimum) is rarely reported directly; most studies report earnings or surplus, requiring inference or estimation.**

- **Many studies focus primarily on non-payoff behavioral outcomes, which may not translate directly into group efficiency or welfare. Higher cooperation rates may be offset by costly or misdirected punishment actions, dampening realized efficiency gains.**

- **Several design dimensions relevant to prediction are only sparsely or incompletely addressed (especially feedback/transparency parameters, reward co-existence, punishment identity).**

- **Contextual moderators—such as communication, authority structure, group heterogeneity, and real-world institutional analogs—are highlighted as important, but parameter-dependent guidance for these is limited.**

- **Most theory papers and adjacent empirical studies operate in structurally different or only loosely analogous environments, limiting their predictive utility for standard PGG dimensions.**

- **Meta-punishment, reciprocity, and reputation are widely discussed as mechanisms but are not systematically analyzed for their quantitative efficiency impact in this paper set.**

- **Heterogeneity of experimental and modeling assumptions means findings do not always generalize across settings; outcome variability and implementation details matter.** Where evidence conflicts (e.g., excessive punishment backfiring), ambiguity should be explicitly acknowledged.

---

**In summary:**  
The literature provides strong support for positive punishment effects on group efficiency in standard repeated public goods games, with the clearest predictions available when empirical designs closely match the downstream prediction context. The prediction task is best informed by leveraging direct findings from experimental PGG studies employing explicit, parameterized punishment, supplemented by theory where structural similarity is high. Where evidence shifts to behavioral proxies or adjacent domains, efficiency predictions become more speculative and design-sensitive, warranting caution and explicit qualification.
