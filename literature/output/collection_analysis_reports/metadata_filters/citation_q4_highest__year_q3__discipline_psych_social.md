# 1) Evidence Base

This paper set covers 14 sources, with a strong emphasis on theory and laboratory-based empirical work in behavioral economics, social psychology, and related disciplines. The majority of papers are theoretical reviews or qualitative syntheses (Fehr & Schurtenberger, 2018; Henrich & Muthukrishna, 2021; van Dijk & De Dreu, 2021; Horne & Mollborn, 2020; Okada, 2020), while about a third are experimental studies using public goods games (PGGs) or adjacent social dilemma paradigms (e.g., Pleasant & Barclay, 2018; Lindström et al., 2018; Barclay & Barker, 2020).

The set is relatively narrow for the downstream prediction task: almost all papers discuss cooperation, social norms, and punishment or reward, but few report direct empirical outcomes on group efficiency (the prediction target). Only one paper (Alvarez-Rodriguez et al., 2021) directly reports efficiency or related payoffs, and this paper does not include punishment. Other empirical studies focus on behavioral or reputational outcomes, not payoffs. Theoretically, the set is rich for mechanism discussions and identification of moderators.

# 2) Task Relevance

**pgg_or_variant:** The majority of papers are of `exact` or `close` relevance. Most central theoretical works explicitly address PGGs or repeated public goods social dilemmas. Several empirical studies use strict PGG designs, but a few pivot to adjacent paradigms (e.g., Prisoner’s Dilemma or real-world sharing; Barclay & Barker, 2020; Ember et al., 2018).

**punishment_or_sanctions:** The theoretical papers are largely `exact` or `close`, centering on punishment, sanctions, and their enabling design dimensions. Empirical coverage is sparser: a few key lab studies implement punishment as part of the PGG (Pleasant & Barclay, 2018; Lindström et al., 2018), while others discuss only punishment attitudes or related constructs (`adjacent`, `weak`, or `none` in some behavioral studies).

**efficiency_or_related_payoff_outcome:** Most papers are only `adjacent` or `weak`: they discuss cooperation rates, willingness to punish, or reputational outcomes rather than directly measuring group efficiency, surplus, or total payoff. Only Alvarez-Rodriguez et al. (2021) offers an `exact` relevance to efficiency, but does not study punishment. Empirical studies focusing on behavior rather than payoffs dominate.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes:**  
- Only one paper (Alvarez-Rodriguez et al., 2021) directly analyzes efficiency, payoff, or group-level surplus—but crucially, this is in the absence of punishment.
- Most theoretical reviews discuss conditions for efficiency, but do not report quantitative payoff results.
- Payoff-based outcomes reported are more often inferred than directly measured—papers often rely on proxies like increased cooperation or reduced norm violations to suggest effects on welfare or group payoff.

**Non-payoff behavioral outcomes:**  
- The modal outcome is behavioral: contribution rates, cooperation rates, norm compliance, punishment frequency, partner choice, reputational assessments, and moral or psychological judgments.
- Several empirical studies rely on vignettes, hypothetical decisions, or third-party ratings rather than experimental observation of game earnings.
- Third-party and antisocial punishment rates (Pleasant & Barclay, 2018; Pedersen et al., 2018; Lindström et al., 2018) are frequently reported, but with little link to aggregate efficiency.

# 4) Main Findings Relevant To Prediction

- **Punishment can increase cooperation, but not always efficiency:**  
  The literature consistently finds that enabling punishment in PGGs increases cooperation rates (Fehr & Schurtenberger, 2018; van Dijk & De Dreu, 2021). However, the associated improvement in efficiency or group payoff is inconsistent—punishment is often costly, and antisocial punishment or overuse can negate efficiency gains.

- **Antisocial punishment and contextual moderators suppress efficiency gains:**  
  Antisocial punishment (punishing high contributors) can erode or reverse the efficiency benefit of punishment, especially in contexts characterized by partner competition or weak normative controls (Pleasant & Barclay, 2018; Fehr & Schurtenberger, 2018).

- **Normative and institutional context is crucial:**  
  Punishment promotes efficiency only when normatively constrained (reducing antisocial punishment and collateral damage) and when embedded in a context supportive of prosocial outcomes (Fehr & Schurtenberger, 2018; Henrich & Muthukrishna, 2021; van Dijk & De Dreu, 2021).

- **Group size and benefit structure matter for baseline efficiency (control):**  
  Group size, MPCR, and network structure are central determinants of baseline (control) efficiency, but their interaction with punishment effects is not empirically quantified in this set (Alvarez-Rodriguez et al., 2021).

- **Third-party punishment is less robust outside narrow lab settings:**  
  Several papers suggest that willingness to punish is highly context-dependent—strong for personally relevant or group-norm violations, but attenuated in anonymous, third-party settings, implying that actual efficiency gains from punishment opportunities may be overestimated in some lab paradigms (Pedersen et al., 2018).

# 5) Prediction Guidance

- **Efficiency boost from punishment is not guaranteed:**  
  Enabling peer punishment may increase observed cooperation, but the net effect on efficiency depends critically on the rate of antisocial punishment and the cost structure. In empirical settings where antisocial punishment is prevalent (e.g., partner selection or biological markets), the usual efficiency gain can be negated or reversed (Pleasant & Barclay, 2018; Fehr & Schurtenberger, 2018).

- **Key moderators for prediction:**  
  Theoretical reviews emphasize the importance of group size, MPCR (benefit structure), punishment cost (and magnitude), and chat/communication in shaping both the normative context and the capacity for mutual monitoring (Fehr & Schurtenberger, 2018; van Dijk & De Dreu, 2021; Henrich & Muthukrishna, 2021). However, direct empirical relationships between these and efficiency under punishment are sparse.

- **Use control efficiency as a baseline, but adjust conservatively:**  
  Given the limited direct empirical evidence, the most supported approach is to use the (measured or predicted) control efficiency as the starting point and apply adjustments for treatment efficiency changes only when:
  - The game context strongly supports normatively prosocial punishment (e.g., limited antisocial punishment, strong prosocial norms, effective communication).
  - The punishment cost and magnitude are balanced to reward cooperation but not trigger excessive retaliation or collateral cost.
  - Be wary of contexts with elevated antisocial punishment, which can eliminate or reverse efficiency gains even when punishment is available.

- **Caveat absence of direct empirical effect sizes:**  
  No paper in the set provides quantitative estimates of the typical efficiency change resulting from enabling punishment, nor is variation across game dimensions (other than via review or mechanism argument) empirically established.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions:**
- `player_count`, `num_rounds`, `mpcr`, `all_or_nothing`, `chat`, `punishment_cost`, `punishment_tech`  
  (Mentioned in numerous lab studies and reviews as core levers for game dynamics and punishment/cooperation mechanisms.)

**Indirectly informed/contextually discussed:**
- `show_other_summaries`, `show_n_rounds`, `show_punishment_id`  
  (Discussed as moderators of observability, transparency, and strategic play, but with little empirical payoff data.)

- `reward_exists`, `reward_cost`, `reward_tech`  
  (Addressed in sociological and indirect reciprocity theories, not tied to empirical efficiency outcomes.)

- `default_contrib`  
  (Framing and default effects mostly absent; only implicit in some experimental studies.)

**Missing/sparse dimensions:**
- No evidence on the interaction of most presentation/framing variables (`default_contrib`, `show_punishment_id`, etc.) with payoff outcomes.
- No direct coverage of reward magnitude/cost in conjunction with punishment in empirical PGGs.

# 7) Important Limitations

- **Scarce direct evidence on efficiency outcomes:**  
  Nearly all the central findings are based on cooperation rates, norm-compliance behavior, or punishment frequency—not measured group efficiency or payoffs. The lone efficiency-focused paper studies group structure but not punishment.

- **Empirical studies do not systematically vary or report all relevant game design dimensions:**  
  The mapping from design features (especially nuanced ones like `show_punishment_id`, `reward_tech`, or `default_contrib`) to efficiency outcomes via punishment is unsupported by direct evidence.

- **Cultural and institutional moderators often discussed, rarely experimentally manipulated:**  
  While theoretical work underscores the moderating roles of culture, group size, and institutional context, the literature set lacks cross-cultural or institutional-variation studies tying these to efficiency effects of punishment.

- **Ambiguity and disagreement are unresolved:**  
  The effect of punishment on efficiency is subject to nontrivial ambiguity—findings about the benefit of punishment are frequently bounded or reversed by counterproductive punishment behaviors (antisocial punishment) or context effects (partner competition).

- **No quantitative mapping or parameter estimates for prediction:**  
  The gap between theory (rich discussion of mechanisms) and data (sparse efficiency outcomes) means that this set supports only cautious, qualitative guidance, not model-based or numerical prediction.

---

**References:**  
- Pleasant, A., & Barclay, P. (2018)  
- Lindström, B., Jangard, S., Selbing, I., & Olsson, A. (2018)  
- van Dijk, E., & De Dreu, C. K. W. (2021)  
- Fehr, E., & Schurtenberger, I. (2018)  
- Henrich, J., & Muthukrishna, M. (2021)  
- Alvarez-Rodriguez, U., et al. (2021)  
- Barclay, P., & Barker, J. L. (2020)  
- Horne, C., & Mollborn, S. (2020)  
- Dhaliwal, N. A., Patil, I., & Cushman, F. (2021)  
- Pedersen, E. J., McAuliffe, W. H. B., & McCullough, M. E. (2018)  
- Okada, I. (2020)  
- Vonasch, A. J., Reynolds, T., Winegard, B. M., & Baumeister, R. F. (2018)  
- Jin, S. X., Balliet, D., Romano, A., Spadaro, G., van Lissa, C. J., Agostini, M., Bélanger, J. J., Gützkow, B., Kreienkamp, J., & Leander, N. P. (2021)  
- Ember, C. R., Skoggard, I., Ringen, E. J., & Farrer, M. (2018)
