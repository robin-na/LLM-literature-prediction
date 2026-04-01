# Evidence Base

The paper set consists of one empirical laboratory experimental paper focused on a linear public goods game with centralized punishment (Engel & Zhurakhovska, 2017), and one broad theoretical review of behavioral governance in common-resource games (Janssen, 2015). The Engel & Zhurakhovska study provides detailed empirical data on the intervention effect of introducing centrally-administered punishment into a PGG, while Janssen synthesizes findings from multiple experimental and field studies, focusing on how punishment and communication mechanisms affect resource governance. The evidence base is thus somewhat narrow for the specific prediction task, with only one direct empirical source and one theory/review source drawing from a wider literature. The overall emphasis is more on laboratory settings than on field or naturally occurring game environments.

# Task Relevance

- **pgg_or_variant**:  
  - Engel & Zhurakhovska (2017) is of exact relevance, as the design is a canonical repeated linear public goods game.
  - Janssen (2015) has close relevance, as it discusses common-pool resource and public goods dilemmas but incorporates a broader set of games.

- **punishment_or_sanctions**:  
  - Both papers are of exact relevance: all reported findings relate directly to enabling punishment or sanctioning institutions in collective-action games.
  - Engel & Zhurakhovska (2017) examines centralized (non-peer) punishment, while Janssen (2015) also discusses both peer and centralized punishment.

- **efficiency_or_related_payoff_outcome**:  
  - Both papers offer close relevance: while their primary outcomes include behavioral measures (e.g., contribution levels), they also report or synthesize findings about group payoffs, surplus, or earnings relative to baselines. Engel & Zhurakhovska (2017) references group profit, and Janssen (2015) discusses group efficiency/earnings.
  - However, neither provides efficiency strictly as a percent of maximum possible payoff; this has to be inferred.

# Outcomes Measured In The Literature

- **Payoff-Related Outcomes**:  
  - **Group profit**, **mean group earnings**, and **collective welfare** are explicitly reported or discussed as improved when punishment mechanisms are enabled (Engel & Zhurakhovska, 2017; Janssen, 2015).
  - Both papers maintain the distinction between increase in payoff (efficiency) and increase in contribution or cooperation rate.

- **Non-Payoff Behavioral Outcomes**:  
  - **Contribution rates**, **cooperation rates**, and details of **punishment assignments** or strategies are measured (especially in Engel & Zhurakhovska, 2017).
  - Janssen (2015) gives weight to context-specific behavioral patterns, such as communication and social norm compliance, and the behavioral mechanisms through which punishment affects outcomes.

- **Note:** While behavioral outcomes are well measured, efficiency per se is usually not reported as a simple ratio of observed to possible maximum.

# Main Findings Relevant To Prediction

- **Punishment Increases Payoff-Related Outcomes**:  
  - The addition of punishment, particularly centralized punishment by a non-participant authority, leads to higher group payoffs and efficiency than the Nash equilibrium or the no-punishment control condition (Engel & Zhurakhovska, 2017; Janssen, 2015).
  - This increase in efficiency is robust across several design variants: identity framing of the authority (public official or judge), whether punishment policy is announced, mode of authority selection, and player experience (Engel & Zhurakhovska, 2017).

- **Centralized vs. Peer Punishment**:  
  - Centralized (third-party) punishment appears to be at least as effective, if not more, than peer punishment in producing higher efficiency and more consistent payoff improvements (Janssen, 2015).

- **Context Moderation**:  
  - Both papers emphasize that contextual factors (e.g., group size/player count, the availability of communication/chat, and the structure of the punishment mechanism) can moderate the effectiveness of punishment on efficiency.
  - Janssen (2015) notes that the crowding out effect and cultural factors may sometimes diminish the positive effects of sanctioning.
  - Engel & Zhurakhovska (2017) reports that variations in authority selection and experience modulate the pattern, but not the direction, of the outcome.

- **Notable Gaps**:  
  - Quantitative estimates linking design dimensions to precise changes in efficiency are not provided. Most findings are qualitative or comparative.

# Prediction Guidance

- **General Direction**:  
  - The literature supports the prediction that enabling punishment in a repeated public goods or common resource game, especially via centralized sanctioning, typically increases group payoff and efficiency compared to the no-punishment condition.
  - This effect is robust in lab environments with clearly defined institutions and observable actions, and across moderate variation in design parameters like authority type and communication (Engel & Zhurakhovska, 2017; Janssen, 2015).

- **Design Sensitivities**:  
  - The size of the effect is likely to depend on details such as **group size**, **punishment cost and magnitude**, **MPCR**, and whether **chat** or communication is present, as suggested by both papers.
  - The presence of **centralized** rather than peer punishment may produce more stable improvements in efficiency.

- **Control Efficiency**:  
  - Since control (no-punishment) group efficiency is often well below the social optimum, the relative efficiency gain from punishment will be apparent, though not quantifiable with a specific coefficient from this literature.
  - Outcomes should be interpreted at least in terms of direction: enabling punishment is expected to increase efficiency, conditional on similar lab-like environments and institutional settings.

# Design Dimensions Highlighted Across Papers

- **Directly Informed**:  
  - `player_count`, `num_rounds`, `mpcr`, `punishment_cost`, and to a lesser extent `all_or_nothing` and `chat` are addressed by Engel & Zhurakhovska (2017). Laboratory details on these factors are specified and discussed.
  - The mechanism (`punishment_tech`) and institution (centralized authority) are also directly informed.

- **Indirectly Informed**:  
  - `show_other_summaries` and `show_punishment_id` are implied in Engel & Zhurakhovska (2017), but details are not the focus.
  - `reward_exists`, `reward_cost`, and `reward_tech` are not present in the main experimental designs but are discussed in the background in Janssen (2015).

- **Contextual or Missing**:  
  - `default_contrib` (contribution framing), `show_n_rounds`, and the specific manipulation of `reward_*` variables are not experimentally manipulated or central in these studies.

# Important Limitations

- **Narrow Empirical Base**:  
  - Only one experimental paper deals directly with efficiency effects of punishment in a classic PGG; other conclusions are qualitative syntheses from broader literature.

- **Centralized vs. Peer Punishment Gap**:  
  - Results about centralized punishment (Engel & Zhurakhovska, 2017) may not extend cleanly to peer punishment, which is more typical in PGG studies and the most common focus of prediction tasks about treatment efficiency.

- **Outcome Reporting**:  
  - Both papers focus primarily on group profit or earnings. Neither reports efficiency as a simple ratio to the full-cooperation maximum, requiring inference rather than direct measurement for the prediction variable.

- **Design Coverage Gaps**:  
  - Some key prediction dimensions (particularly continuous vs. all-or-nothing contribution technology, information display, reward presence and parameters, and framing) are sparsely addressed.

- **Quantitative Effect Sizes Lacking**:  
  - The literature does not provide concrete effect sizes or model parameters for predicting how much efficiency will increase under different game designs, only that a positive effect is generally observed.

- **Contextual Contingencies**:  
  - Theoretical review (Janssen, 2015) emphasizes context-sensitivity: group size, communication, cultural context, and trust moderate the punishment effect, but specific direction and magnitude are not given. Findings may not generalize beyond the stylized laboratory context.

- **Ambiguity in Cross-Study Comparisons**:  
  - Some mechanisms (e.g., crowding out from external rules, the difference between peer and centralized punishment) are noted as theoretically ambiguous or context-dependent, reducing certainty for out-of-sample prediction.
