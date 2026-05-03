# 1) Evidence Base

The evidence base consists of 108 papers, with a mix of **empirical laboratory experiments** and **explicit theoretical (mechanism or simulation) papers**. There is strong representation of *exact* public goods games (PGGs), including high-quality experiments and classic theoretical work, as well as studies using adjacent paradigms (commons dilemmas, dictator/ultimatum games, repeated games, spatial games) and mechanisms (ostracism, exclusion, third-party punishment, rewards, or reputation).

- **Empirical Evidence**: Rich, especially for standard PGGs with and without peer punishment. Classic and recent experiments provide outcome data (sometimes exact efficiency, more often contribution rates).
- **Theory/Mechanism Arguments**: Prominent. Several papers provide analytical and simulation models linking punishment design to efficiency impacts, with attention to moderators such as group size, observability, and cost structures.
- **Coverage**: Relative to the prediction task (predicting efficiency outcomes in PGGs with/without punishment as a function of design dimensions plus control efficiency), the evidence base is **broad and deep** for exact PGG/punishment settings in the lab, but narrows when considering field settings, unusual design features, or variants involving rewards, third-party punishment, or dynamic partnerships.
- **Direct empirical efficiency outcomes** are substantially available, but many studies (especially meta-analyses, behavioral mechanism works, and field data) focus on contribution/cooperation rates or punishment behavior, rather than efficiency per se.

# 2) Task Relevance

**a) PGG_or_variant**:  
- *Exact relevance*: Many studies are **exact** on public goods games (PGG), using canonical multi-round, multi-player PGGs (e.g., Fehr & Gächter, Gintis et al.).
- *Close/adjacent*: Important supporting evidence from adjacent paradigms (repeated PD, CPR games, spatial games, and dictator/ultimatum games with punishment).
- *Weak/none*: Some papers focus on field or ethnographic settings, one-shot games, or behavioral paradigms that are only contextually related.

**b) Punishment_or_sanctions**:  
- *Exact relevance*: Substantial coverage of standard peer punishment (costly punishment as a direct, peer-administered deduction from payoffs).
- *Close*: Exclusion/ostracism, centralized or institutional punishment, reward mechanisms, and symbolic sanctions are discussed widely.
- *Adjacent/weak*: Reputation, social norms, and observational studies of punitive sentiment without implemented punishment.
- *Missing*: Some papers lack direct manipulation or measurement of punishment despite discussing related behavioral phenomena.

**c) Efficiency_or_related_payoff_outcome**:  
- *Exact*: Multiple high-quality studies report group efficiency or total earnings directly.
- *Close*: Many studies link contribution rates to theoretical or inferred payoffs, sometimes supported by simulations (e.g., Balliet et al., theoretical works).
- *Adjacent/weak*: A large proportion measure only non-payoff behavioral outcomes (contribution, cooperation, intention to punish, reported trust), inferring efficiency indirectly.
- *None*: Several ethnographic, psychological, or mechanism-based papers provide no direct or indirect estimates of efficiency.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes**:  
  - *Direct Measures*: Efficiency (as fraction of max possible group payoff), total earnings/welfare, surplus, coins generated (e.g., Gintis et al., Fehr & Gintis, Masclet, Barclay 2004, Semmann 2004).
  - *Indirect Measures/Inferences*: Outcomes inferred through cooperation rates or efficiency-rated simulations, often requiring assumptions (e.g., Balliet et al., Krup et al.).
- **Non-payoff behavioral outcomes**:  
  - *Dominant Measures in Many Papers*: Individual and average contribution rates, cooperation/defection rates, punishment/reward rates, norm compliance, trust, intentions, attitudes, moral emotions.
- **Notable distinctions**:  
  - Increased contribution rates or cooperation do not unambiguously mean higher efficiency, as punishment can destroy resources, and efficiency must account for both increased public good output *and* costs of punishment.
  - Symbolic representation (e.g., social judgment, hypothetical willingness to punish), not always indicative of real payoff impact.

# 4) Main Findings Relevant To Prediction

**Synthesis across the literature—Key findings:**

- **Peer punishment tends to increase efficiency in standard lab PGGs**:  
  - **Robustly Positive**: In canonical settings (4-8 players, repeated interactions, MPCR 0.3–0.4, standard punishment cost/impact), enabling peer punishment increases group efficiency, often dramatically: efficiency rises by 28–40% above control (e.g., Gintis et al., Masclet, Fehr & Gintis).
  - **Punishment effectiveness depends on context and design**:  
    - If punishment is too costly or lacks problems of *second-order free riding*, net efficiency gains may disappear or become negative (Ye et al., Guala, Ostrom et al.).
    - Punishment is more likely to boost efficiency when accompanied by mechanisms such as compensation for punishers ("sympathy"), communication, or endogenous institution-building (Ostrom et al., Ye et al.).
    - Efficiency gains accrue in the *long run* when punishment deters defection and actual punishment use drops as cooperation stabilizes (Balliet et al., MACY 1993).
- **Punishment sometimes fails to raise (or even reduces) efficiency**:  
  - When applied in "weak" or poorly coordinated form, punishment can destroy resources without sufficiently boosting cooperation, resulting in static or decreased efficiency (Guala, Ostrom et al., Tenbrunsel & Messick).
  - Punishment's net efficiency effect can be negative in the short term or in cultures with strong antisocial punishment norms, or where overpunishment is applied (Guala, Balliet et al., Barclay 2004 for cultural moderation).
  - The presence of alternative, more harmful defection options can neutralize or reverse the efficiency effect of punishment (Mulder et al., 2006).
  - Group size and composition (e.g., larger groups, absence of communication, or culturally specific norms) can weaken or reverse punishment’s effectiveness on efficiency (Barclay 2004, Tarui et al., Kerr et al., Balliet et al.).
- **Mechanism insights**:  
  - Efficiency is most improved when punishment is credible, not too costly, and deters defection such that actual use declines over time.
  - Punishment cost/benefit ratio, decision structure (binary vs. continuous contribution), information feedback (visibility of behavior and punishment), and institutional context (centralized vs. decentralized, voluntary vs. imposed) are critical moderators.
  - Information structure (imperfect monitoring), time horizon (number of rounds, patience), and institutional or social context (e.g., communication, leader legitimacy, reputation, or group selection) can tip the efficiency balance (Ostrom et al., ABREU et al., Tarui et al., Balliet et al.).
- **Alternative mechanisms**:  
  - In some designs, *reputation*, *reward*, *delegation of authority*, or *ostracism* can substitute for or outperform punishment in efficiency gains (Semmann 2004, Hamman 2011, Masclet 2003).
  - In field or ethnographic contexts, low- or no-cost, coordinated sanctions (gossip, ostracism) are seen as more efficient than costly, competitive punishment (Guala 2012, Masclet 2003).

# 5) Prediction Guidance

Given this literature, **predictions of treatment efficiency in PGG-like environments with enabled peer punishment** should be guided by:

1. **Control Efficiency as Baseline**:  
   - The known average efficiency of the punishment-disabled game is predictive: punishment rarely *reduces* efficiency below this value in standard lab PGGs unless costs are very high or punishment is uncoordinated and wasteful.
2. **Game Design Dimensions**:  
   - **Directly Informed** (see Section 6) — key moderators include:
     - player_count, num_rounds (especially longer games, moderate group sizes)
     - mpcr (the incentive to cooperate)
     - punishment_cost, punishment_tech (cost/impact ratio, decentralization)
     - presence/absence of communication (chat), information feedback (show_n_rounds, show_other_summaries)
   - **Qualitative Guidance**:
     - Expect substantial efficiency gains when:
       - Small/moderate group size (4–8), 10+ rounds, standard MPCR (0.3–0.4), peer punishment ratio not too costly, and clear information about actions and punishment.
       - There is no competing alternative defection option.
     - Efficiency gains may be minimal if:
       - Punishment is very costly, poorly coordinated, limited to "weak" forms, or the design allows anti-social/second-order punishment.
     - The effect size is *culturally and contextually dependent*: efficiency gains observed in some cultural groups or settings may not generalize.
   - **Highly moderate by**:
     - Existence of compensation/reward mechanisms, communication, endogenous punishment institution design, information timing/structure.
     - Lack of institutional support, high punishment cost, and presence of competing defection options can neutralize positive effects.
3. **Use Caution When**:
   - Making predictions for settings with large groups, complex or ambiguous info structures, unusual payoff functions (nonlinear, step-level), or under field/real-world conditions: efficiency improvements from punishment may not materialize.
   - Interpreting non-payoff behavioral results (increased contributions, cooperation) as direct proxies for efficiency.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions** (supported by empirical/theoretical outcome data):

- `player_count`: Strongly covered; small groups (4–8) classic, larger groups less so (Barclay 2004; Tarui et al.).
- `num_rounds`: Most lab studies use 10+ rounds; longer time horizons generally favor efficiency gains from punishment.
- `mpcr`: MPG per capita return is typically manipulated and reported as a key efficiency moderator.
- `punishment_cost`: Ubiquitously varied; higher costs reduce or eliminate efficiency gains from punishment.
- `punishment_tech`: Peer (decentralized) punishment is standard; centralized/ostracism/exclusion designs covered (e.g., Masclet, Hamman, Balliet meta).
- `reward_exists`: Some studies directly compare punishment and reward or combinations (Balliet meta, Kiyonari & Barclay); presence of reward can independently improve efficiency.
- `chat` (communication): Communication shows a prominent, often synergistic interaction with punishment in enabling efficiency gains (Ostrom et al., Hamman, Masclet).
- `show_n_rounds`, `show_other_summaries`: Sometimes manipulated, but direct evidence for their moderation is less common.
- `all_or_nothing`, `default_contrib`: Some studies manipulate binary vs. continuous contributions and default framing; less consistently linked to efficiency results.
- `show_punishment_id`: Identity feedback affects behavior; more likely to increase punishment frequency or shift the nature (prosocial/antisocial), but efficiency effects less empirically defined.
- `reward_cost`, `reward_tech`: Reward-specific mechanisms are examined in direct comparison to punishment, particularly when both are available; efficiency gains are often highest in reward or reward+punishment settings.
- `punishment_magnitude`: Not always reported explicitly, but studies manipulating the punishment impact/cost ratio highlight its importance.

**Indirectly Informed/Contextual Dimensions**:

- Network structure, information asymmetry, institutional rules (election of monitors, constitutional choice), feedback, and legitimacy are identified as important, but evidence is sometimes limited to non-payoff outcomes or inferred via theoretical mechanism (ABREU et al., Guala).

**Sparse/Missing**:

- Detailed data on the *effect of revealing punishers' identities* (`show_punishment_id`) on group efficiency, rather than just punishment frequency or behavior.
- Effects of *default contribution framing* and *information about round number* on efficiency, outside of standard parameters.
- Step-level or nonlinear public good production functions (some theoretical coverage, but empirical evidence sparse).
- Extension to settings with both punishment and reward enabled, or field-like institutions (some indirect and adjacent, less empirical measurement of efficiency).

# 7) Important Limitations

- **Efficiency Outcomes vs. Behavioral Outcomes**: *Many* papers report only on contribution/cooperation behavior, not group efficiency or payoff. Extrapolations to efficiency must be made cautiously, as increased cooperation may be offset by costly punishment.
- **Context and Generalizability**: Most high-relevance findings are from lab studies with standard (small N, short horizon) PGG designs; findings may not translate to larger groups, longer time horizons, field settings, or games with alternative decision structures (adjacent papers often note divergence in efficiency implications).
- **Cultural, Social, and Institutional Moderators**: The efficacy and efficiency impact of punishment is moderated by culture, group composition, legitimacy, and institutional design (Barclay 2004, Guala, Ostrom et al.).
- **Specification of Key Dimensions**: Some design dimensions relevant to prediction (punishment identity, framing of defaults, detailed information disclosure) have little or no direct evidence linking them to measured efficiency.
- **Negative and Ambiguous Effects**: There is clear across-paper evidence that punishment can sometimes fail or backfire (reduce efficiency), particularly when poorly coordinated, costly, or in the presence of alternative defection or anti-social punishment. These conditions are not always made salient in primary results.
- **Short vs. Long-Run Effects**: Efficiency gains from punishment may require long repeated interaction; short-run costs can dominate in brief or one-shot games.
- **Indirect Evidence**: For many dimensions or mechanisms (rewards, reputational cues, institutional context), the efficiency impact must be inferred from behavioral change or adjacent outcome measures, often via theoretical models rather than outcome data.
- **Control Baseline Dependency**: Actual efficiency gains from punishment can be small or negative if the control (punishment-disabled) game already achieves high efficiency through other means (e.g., communication, reputation).

---

**Summary**:  
The supplied literature base supports a robust, but **context-sensitive and design-dependent, positive average effect of peer punishment on efficiency in standard laboratory PGGs**. Effect strengths vary with group size, punishment cost and technology, communication, and cultural and institutional factors; efficiency gains are not universal and can be reversed in adverse design contexts. The literature directly informs prediction for most standard game design dimensions, but some dimension-level moderators and real-world complexities remain less well evidenced, and must be applied with due caution.
