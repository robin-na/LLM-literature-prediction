# Evidence Base

The paper set comprises a mix of theoretical and empirical sources, including experimental lab and field studies, computational models, conceptual/theoretical reviews, and agent-based simulations. The evidence base is broad in scope for the topic of cooperation, punishment, and efficiency in social dilemmas, but the subset providing directly relevant, empirical, and quantitative results for public-goods-game (PGG)-like environments with manipulation of punishment is not exhaustive. Many of the most informative papers for the prediction task (predicting average efficiency with peer punishment from design dimensions and control efficiency) are theoretical models or simulations parameterized for PGGs or their close analogues. There is inconsistent reporting of efficiency as a ratio to the group optimum; many studies focus on contribution rates or cooperation frequency, but not directly on payoff-based efficiency.

# Task Relevance

**1. pgg_or_variant:**  
The literature has a high density of exact-relevance papers—studies using standard or closely-matching PGGs (often with control and punishment treatments), as well as a large body of theory/simulation work mapping onto PGG design dimensions. Theoretical papers often use formal analogues of the PGG with parameters corresponding closely to experimental conditions. However, a significant minority of sources are adjacent or weakly relevant, using repeated Prisoner’s Dilemma, trust, or mutualism games.  
**Relevance label:** exact to close for a majority; substantial adjacent content.

**2. punishment_or_sanctions:**  
Many papers manipulate punishment as a condition or model costly sanctioning in theoretical work. Both institutional (external) and peer (decentralized) punishment are covered. However, some studies model only indirect punishment (reputation, withholding cooperation), and not all specify peer punishment exactly as in the classic PGG treatment. There is close attention to the cost and effectiveness of punishment, and many studies explicitly discuss anti-social punishment (punishment of cooperators) and its effect on outcomes.  
**Relevance label:** exact for ~half, close to adjacent for many.

**3. efficiency_or_related_payoff_outcome:**  
While there are numerous studies reporting group payoff, efficiency, or welfare, many key experiments focus mainly on contributions or cooperation rate, with efficiency inferred but not always reported quantitatively. Theoretical papers often use group payoff as a central outcome. Explicit reporting of the ratio of observed to optimal payoff (efficiency) is less common in empirical studies, but direct findings for welfare/earnings are available in several core sources.  
**Relevance label:** efficiency: exact for a minority, close/adjacent for many, with some studies supplying only behavioral or mechanistic evidence.

# Outcomes Measured In The Literature

- **Payoff/Efficiency Outcomes:**  
  - Group efficiency (payoff relative to the fully cooperative outcome), total earnings, welfare, or surplus are reported in several empirical (Egas & Riedl, 2008; Sääksvuori et al., 2011; O'Gorman et al., 2009) and many theoretical studies (e.g., Gintis, 2000; Bowles & Gintis, 2004).
  - Numerous theoretical and simulation studies provide explicit analysis of how design dimensions affect group efficiency as a function of punishment parameters (e.g., cost/effectiveness, group size).

- **Non-payoff Behavioral Outcomes:**  
  - Contribution rate, cooperation rate, norm compliance, frequency and type of punishment, and other behavioral proxies for efficiency are more commonly measured, especially in experimental work.
  - Some studies focus exclusively on behavioral mechanisms without direct calculation of effects on net group payoff or efficiency (e.g., Anger as a driver of punishment—Seip et al., 2009).

- **Indirect/Contextual Outcomes:**  
  - Many papers examine evolutionary stability or the prevalence of strategies (e.g., prevalence of altruists vs defectors), with the implication that these affect efficiency, but without direct measurement.
  - Reputation, partner choice, and cultural context/moderators (e.g., antisocial punishment, intergroup competition, self-determination, and trust) are identified as critical influences.

# Main Findings Relevant To Prediction

**Empirical Findings:**
- **Punishment often raises cooperation rates but can reduce efficiency:**  
  - Egas & Riedl (2008), Traulsen et al. (2012), and Guala (2012) find that while punishment increases cooperation, it frequently reduces net group efficiency due to the direct resource costs of sanctions.
- **Punishment can raise efficiency but only under certain conditions:**  
  - O'Gorman et al. (2009) find higher efficiency with a single designated punisher compared to diffuse punishment.
  - Sääksvuori et al. (2011) show that the effect is contingent on intergroup competition: punishment increases efficiency only when group competition is present.
  - Vollan (2008) and Castillo et al. (2011) find that externally imposed punishment can crowd out cooperation and reduce efficiency, especially when participation or local support is low or when punishment is illegitimate.

**Theoretical Findings:**
- **Cost-effectiveness and structure of punishment are critical moderators:**  
  - Low-cost, high-impact (effective) punishment is necessary for efficiency gains (Egas & Riedl, 2008; Gintis, 2000; Bowles & Gintis, 2004).
  - Too costly punishment can undermine or even reverse efficiency gains; anti-social punishment and retaliation greatly reduce or negate the positive effect (Rand et al., 2010; Powers et al., 2012).
  - Spatial structure, repeated interactions, and the presence of metanorms (punition/rewarding of punishers) and reputation systems can support high efficiency (dos Santos et al., 2011; BOYD & RICHERSON, 1992; Nakamaru & Dieckmann, 2009).
- **Combination of reward and punishment, or institutionally coordinated sanctions, has more robust positive effects** (Cressman et al., 2012; Milinski & Rockenbach, 2012).
- **Cultural, institutional, and social context alters outcome drastically:**  
  - Cross-cultural variation in antisocial punishment means that design dimensions alone are insufficient to predict outcomes (Gächter et al., 2010; Gächter & Herrmann, 2009).
  - Voluntary, self-determined (voted-in) punishment works better than external, imposed punishment (Vollan, 2008; Castillo et al., 2011).

# Prediction Guidance

**For predicting the treatment (punishment-enabled) efficiency in PGGs given control efficiency and design dimensions:**

- **Expect positive treatment-control efficiency differences if:**
  - Baseline efficiency is low (control with decaying cooperation).
  - Punishment is low- to moderately-costly and highly effective (high punishment:impact ratio).
  - Peer punishment is coordinated or institutional, not predominantly anti-social, and not subject to frequent retaliation.
  - The context allows for reputation, metanorms, or secondary mechanisms reducing the cost of punishment (e.g., reward, communication, or coordination).
  - The punishment structure avoids redundancy and is not excessively diffuse (as in the single-punisher regime).

- **Expect little to no efficiency gain—or possible efficiency loss—if:**
  - Punishment is costly and frequently used, with no mechanisms to coordinate or limit redundant punishment (e.g., peer punishment by all).
  - Anti-social punishment is common or permitted.
  - Retaliation against punishers is easy or likely.
  - Cultural/social trust is high and punishment is externally imposed (leading to crowding-out).
  - The baseline efficiency is already high in control (little scope for improvement).
  - Game features promote punishment of cooperators or bystanders, or allow for significant norm ambiguity.

- **Design dimensions explicitly informed (see next section) should be used to map from observed control efficiency to expected treatment efficiency, with the effect size being a function of punishment cost/effectiveness, group size, availability of communication, duration (number of rounds), and competition context.**
- **Incorporate contextual and social moderators (e.g., group self-determination, trust, culture) if relevant information is available; these can override the expected directionality suggested by game structure alone.**

# Design Dimensions Highlighted Across Papers

**Directly Informed:**  
- `player_count`, `num_rounds`, `mpcr`, `punishment_cost`, `punishment_tech` (punishment impact/magnitude), and occasionally `all_or_nothing`.
- `chat` (communication) is regularly analyzed as a moderator.
- `show_punishment_id` (anonymity/identifiability) is occasionally included (e.g., retaliation is more likely when punishers are identifiable).
- `reward_exists` and `reward_cost/tech` are covered in papers analyzing the combined or comparative effect of reward and punishment.
- `show_n_rounds` and `show_other_summaries` are occasionally mentioned (information role).

**Indirectly Informed or Contextually Discussed:**  
- `default_contrib` (framing) is addressed in papers analyzing opt-in/opt-out or norm design.
- `show_other_summaries` (outcome visibility) and `show_punishment_id` link to reputation effects, retaliation, and the social context of punishment/reward.
- `all_or_nothing` and `mpcr` are sometimes discussed in theory or as game structure but not always manipulated experimentally.

**Rare/Sparse or Missing:**  
- `default_contrib` and non-standard framing receive little direct attention.
- Detailed breakdowns of `show_n_rounds`, `show_other_summaries`, or implementation nuances (e.g., precise timing, real-time chat vs. message boards) are rare.
- Cases where punishment and reward co-exist with full details manipulated are less common, though the theoretical literature covers combined incentives.
- The interaction effects of multiple features (three-way or higher interactions) are not systematically addressed in most studies.

# Important Limitations

- **Measurement Limitation:** Many experimental papers use cooperation/contribution rates, not efficiency, as their primary outcomes; efficiency must be inferred in some cases, which introduces uncertainty for quantitative prediction.
- **Contextual Gaps:** Cultural, social, and group-level moderators (e.g., trust, self-determination, legitimacy of rules, institutional context) are often crucial and yet are not always codified as game design dimensions available for prediction, limiting model transferability (Gächter et al., 2010; Vollan, 2008).
- **Heterogeneity in Implementation:** Peer vs. institutional punishment, anti-social vs. pro-social punishment, single vs. multiple punishers, anonymous vs. identifiable, and various cost structures are not always clearly categorized or comparable.
- **Boundary Conditions:** Findings often depend on moderate values of punishment cost/effectiveness and game length, with extreme parameter values (very high cost, very large group, very short/long games) yielding divergent outcomes; theory often overstates generality beyond tested boundaries.
- **Theoretical-empirical Gap:** Many strong claims about parameter effects come from theory models, not experimental tests; empirical studies sometimes find weaker, negative, or highly context-dependent effects.
- **Reporting Inconsistencies:** Quantitative effect sizes, especially for efficiency or payoff ratios, are sporadically reported and not always aligned across studies.
- **Conversion from Control to Treatment:** The scalability of experimental findings to arbitrary control baselines (or to games with very high/low baseline efficiency) can be uncertain—effects may be largest when baseline is low, and negligible when baseline is already high.
- **Indirect Mapping for Non-Payoff Outcomes:** Using changes in behavioral outcomes as proxies for efficiency may be misleading, especially if punishment is frequent and costly or if punishment behaviors are anti-social.

---

In summary, the paper set offers strong, broadly consistent theoretical guidance and qualified empirical support for the moderators of punishment’s efficiency effect in PGGs. The effect of enabling peer punishment is positive under favorable, coordinated, well-structured conditions but can be negative or negligible in the presence of costly, anti-social, or externally imposed punishment—especially in the absence of mechanisms for coordination, reputation, or trust. The evidence base identifies the most influential design dimensions for prediction (including punishment cost/tech, group size, rounds, information structure, competition context, and social legitimacy), but quantitative prediction of the efficiency delta remains challenging when baseline efficiency is high, when anti-social punishment is present, or when participant context is outside the tested empirical envelope.
