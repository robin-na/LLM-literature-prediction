# 1) Evidence Base

This paper set is exceptionally broad (462 items), covering a dense and mature literature on cooperation, punishment, and efficiency in public goods and closely related games. The majority of studies are experimental lab or field papers focusing on public goods games (PGGs) with and without punishment, alongside a substantial body of theoretical and simulation work. There is a strong empirical base specifically examining efficiency or closely related group payoff outcomes in the presence and absence of punishment, making this set unusually well-suited for prediction tasks using PGG or VCM designs. Both canonical n-person linear PGGs and close variants (e.g., threshold games, repeated PDs, contests, CPRs, group formation, reputation systems, exclusion/ostracism) are extensively tested.

The set contains a substantial number of theory papers (including evolutionary models, agent-based simulations, analytical game theory) with explicit claims about the effect of punishment or sanctions on cooperation and efficiency. There are also numerous conceptual reviews and mechanism-centered discussions.

However, while empirical coverage is especially rich for standard repeated linear PGGs with 3–5 players, 6–30 rounds, continuous contributions, and standard punishment technologies (1:3 or similar cost-to-impact ratio), there is also significant heterogeneity in designs, contexts (e.g., cross-cultural, field vs. lab), and implementation details (e.g., endogenous vs. exogenous institution, visibility, communication, group composition).

Overall, compared to most domains, this evidence base is extensive, multi-method, and well-aligned with the prediction task, but certain design dimensions (see section 6) remain sparsely addressed.

---

# 2) Task Relevance

### PGG or Variant (`pgg_or_variant`)
**Relevance:** *exact*

The great majority of studies have `exact` relevance: the standard linear PGG/VCM, iterated with random or fixed matching, is the baseline for experimental analysis. Numerous close variants (threshold, all-or-nothing, CPRs) are also covered. Some studies use repeated PDs, trust games, weakest-link, or contests as adjacent, but the core mechanisms often translate well.

### Punishment or Sanctions (`punishment_or_sanctions`)
**Relevance:** *exact*

Most included evidence is *exactly* relevant: punishment or sanctioning (costly peer punishment, institutional punishment, exclusion/ostracism, reward/anti-reward, and hybrid forms) are manipulated as treatment variables, and their presence/absence is a key difference in experimental design. A smaller subset focuses on *adjacent* settings with partner choice, reputation, or other enforcement substitutes.

### Efficiency or Related Payoff Outcome (`efficiency_or_related_payoff_outcome`)
**Relevance:** *exact to close, with some adjacent/weak*

Direct payoff-based outcomes (group efficiency, group/average earnings, welfare, surplus) are measured in a large and diverse set of studies. Some focus primarily on contributions/cooperation, but most papers with *primary relevance* for prediction do report efficiency or sufficient data to infer it, aligning closely with the downstream task. Still, many studies provide only *behavioral* outcomes (not direct efficiency), and some analyze only adjacent outcomes (e.g., trust, reputation, beliefs, or willingness to punish).

---

# 3) Outcomes Measured In The Literature

### Payoff-Related Outcomes (aligned with "efficiency")
- **Group efficiency** (group total payoff as a proportion of the cooperative optimum): explicitly measured in many experimental PGGs (e.g., Fehr & Gächter, 2000; Gürerk et al., 2006; Masclet et al., 2003).
- **Group profit / average earnings**: often reported either directly or as "welfare" or "group payoff."
- **Surplus, coins generated, net earnings:** Variants on efficiency, especially in resource games and climate/crisis/contest PGGs.

### Closely Related Outcomes (interpretable for efficiency)
- *Achievement* in threshold games (fraction of successful groups).
- *Total group income* in trust, contest, or allocation games (where group output is measurable).
- *Payoff per player* in per-round or cumulative form.

### Non-Payoff Behavioral Outcomes
- **Contribution or cooperation rate:** Frequently measured, sometimes the main outcome (esp. in literature focused on social norms, psychology, network effects). These measures are *not* equivalent to efficiency, since higher contributions may be offset by costly punishment.
- **Punishment frequency / assigned points:** Inform mechanism, can index excessive or antisocial punishment.
- **Norm compliance, trust, reputation scores:** Important for mechanism studies; not a direct efficiency/payout proxy.

### Note
Many papers explicitly distinguish between effects on cooperation and effects on efficiency/welfare, finding the two can diverge—often punishment increases cooperation but not always efficiency, due to punishment costs, antisocial punishment, or context (see below).

---

# 4) Main Findings Relevant To Prediction

**Empirical evidence** provides the following consistent, but nuanced, patterns relevant for predicting the effect of enabling punishment on efficiency in PGG-like games:

### **1. Standard Linear PGGs (4–5 players, repeated, moderate MPCR, continuous contrib):**

- **Enabling peer punishment almost always increases efficiency relative to control** (no punishment), especially when baseline (control) efficiency is low and punishment is not prohibitively costly/ineffective (Fehr & Gächter, 2000, 2002; Gintis et al., 2003; Masclet et al., 2003; Fudenberg & Pathak, 2010).
- **Magnitude:** Typical efficiency gains range from 10–40% over control, sometimes approaching the social optimum depending on group stability and matching (fixed > stranger), effectiveness of punishment (cost-to-impact ratio), and duration of repeated play.
- **Reward mechanisms (positive incentives) also increase efficiency,** and in several studies, reward outperforms punishment in efficiency terms because it lacks destructive costs (Rand et al., 2009; Sutter et al., 2010).

### **2. Moderators and Contextual Moderators:**

- **Accuracy of information about others' contributions** is *critical*: under *perfect monitoring*, punishment increases efficiency; under *noisy or uncertain monitoring*, punishment can reduce efficiency below baseline, due to misdirected/antisocial punishment and welfare loss (Ambrus & Greiner, 2012; Grechenig et al., 2010).
- **Social/cultural context** (degree of antisocial punishment, e.g., Russia/E. Europe, low-trust settings): where antisocial punishment is high, punishment reduces efficiency, sometimes sharply (Herrmann et al., 2008; Gächter & Herrmann, 2011; Fehr et al., 2008).
- **Game structure:** In one-shot PGGs or environments with high rates of misdirected punishment, efficiency benefits of punishment can be entirely absent or negative (Nikiforakis, 2008; Gächter & Herrmann, 2011; Guala, 2012).
- **Emotion or affect:** Excessive punishment is linked to anger and can destroy resources and lower efficiency unless controlled (Drouvelis & Grosskopf, 2016; Dickinson & Masclet, 2015).
- **Group composition (cultural/ethnic/motivational):** Efficiency benefits from punishment depend on group-specific norms (Barclay, 2004; Barclay & Raihani, 2016).

### **3. Variants and Specific Designs:**

- **Exclusion/ostracism (non-monetary peer punishment):** Frequently even more effective (higher efficiency) than monetary punishment, and less likely to provoke antisocial responses (Cinyabuguma et al., 2005; Feinberg et al., 2014; Masclet, 2003; Güth et al., 2007).
- **Voluntary institution choice/voting:** Endogenous selection of punishment/reward regimes reliably increases efficiency, as predicted by institutional choice theories (Sutter et al., 2010; Putterman et al., 2011; Markussen et al., 2014).
- **Centralized vs. peer punishment:** Delegated (centralized) punishment can increase efficiency more than peer punishment, if it is targeted and low-cost (Andreoni & Gee, 2012; Gross et al., 2016).
- **Second-order punishment, anti-social punishment, and counter-punishment:** Harm efficiency, often offsetting any gain from increased cooperation (Nikiforakis, 2008; Gächter & Herrmann, 2011).
- **Reward mechanisms:** Often increase efficiency at least as much as punishment, and sometimes more, because they avoid direct destruction—but combined mechanisms (punishment + reward) sometimes perform best (Rand et al., 2009; Chen et al., 2015; Szolnoki & Perc, 2013).
- **Intergroup competition:** Presence of between-group competition can strongly moderate the efficiency effects of punishment, sometimes amplifying benefits (Sääksvuori et al., 2011).

### **4. Theoretical Work:**

- **Phase diagrams and models (e.g., Perc et al., 2017; Fehr & Schmidt, 1999):** Show that the effect of punishment on efficiency is U-shaped or non-monotonic as a function of cost/effectiveness, group size, information, spatial structure, and other design dimensions.
- **Spatial and networked games:** Clustering and partner choice can support efficiency, with or without explicit punishment (Wang et al., 2017; Brandt et al., 2003).
- **Reputation and information mechanisms:** Reputation tracking or observability can substitute for punishment or amplify its efficiency impact when present (Rockenbach & Milinski, 2006, Fehr & Rockenbach, 2004).

---

# 5) Prediction Guidance

Based strictly on the supplied literature, prediction of treatment efficiency in PGG-like environments with punishment enabled—given the control efficiency and game design dimensions—should weigh the following principles:

- **In canonical repeated linear PGGs (3–5 players, moderate MPCR, no communication, continuous contribution, anonymous punishment), enabling peer punishment should be predicted to increase group efficiency, typically by 10–40% over control, provided baseline efficiency is declining or low.**
- **Magnitude of efficiency gain** declines as the cost of punishment increases (cost-to-impact ratio worsens), group size grows, or as rounds are shortened. Extremely high or low MPCR reduces gain. Small groups (4–5) are most robust; in very large groups, or when punishment is weak or cost is prohibitive, efficiency gains can disappear.
- **When control efficiency is already high (due to communication, endogenous sorting, high baseline prosociality, or reputation/reward mechanisms), enabling punishment has little or no further effect, and may even reduce efficiency by introducing costly, unnecessary sanctions.**
- **If the design allows communication, norm-signaling or explicit reputation, or enables targeted and well-constrained punishment (e.g., only low contributors can be punished), efficiency gains from punishment are maximized, and actual punishment frequency drops over time.**
- **If the design introduces significant monitoring/information noise, antisocial punishment, or counter-punishment, the effect of punishment on efficiency can be neutral or negative, even if cooperation rates rise.**
- **Ostracism/exclusion mechanisms often outperform monetary punishment for efficiency, with similar effects on cooperation but lower destroyable cost, especially in small groups.**
- **Reward (positive sanctioning) often increases efficiency at least as much as punishment, and the marginal benefit of adding punishment to a reward-only environment is low unless defectors persist.**
- **Institutional structure (endogenous vs. imposed, centralized vs. peer) strongly moderates the effect: efficiency gains are highest when institutions are chosen by subjects and punishment is directly targeted to non-cooperators.**
- **In adjacent or field-like designs (contests, CPR, trust games), effects are more variable: punishment can increase, decrease, or have negligible effect on efficiency, depending on context and group norms.**

Therefore, prediction models should:
- Use control efficiency as a base,
- Positive effect of enabling punishment, scaled by punishment parameters (cost, leverage), group size, rounds, and the accuracy/visibility of monitoring,
- Incorporate negative corrections for settings with high anticipated antisocial punishment, noisy information, counter-punishment, or contexts where baseline efficiency is already high due to reputational, communicative, or reward mechanisms,
- Expect weaker or even negative efficiency effects of punishment in difficult-to-monitor, high antisocial punishment, unequal, or heterogeneous returns environments,
- Treat exclusion/ostracism mechanisms as at least as effective (if not more so) than monetary punishment in boosting efficiency.

---

# 6) Design Dimensions Highlighted Across Papers

**Directly and well informed:**
- `player_count`: Extensive—group size effects reported often, with smaller groups predicted to benefit more from punishment.
- `num_rounds`: Well covered, with longer repeated games supporting greater efficiency gains from punishment.
- `mpcr`: Frequently manipulated, with non-monotonic effects on the efficiency gain from punishment; both low and high values can moderate the effect.
- `punishment_cost` / `punishment_tech`: Core dimensions, frequently reported and varied; cost-to-impact ratios central to quantitative predictions.
- `all_or_nothing`: Covered, especially in variants (step-level, threshold games), though often in continuous form.
- `show_n_rounds`: Sometimes discussed; known horizon affects strategies and can moderate end-game effects.
- `chat`, `show_other_summaries`: Directly manipulated in many studies; chat (communication) is a strong moderator, often crowding out the need for punishment.
- `reward_exists`, `reward_cost`, `reward_tech`: Extensively tested as positive control or variant to punishment treatments.

**Indirectly or contextually discussed:**
- `punishment_tech`: The form of punishment (peer vs. centralized, restriction/pool vs. targeted) is a strong moderator; many studies address it, but not always with direct comparisons.
- `default_contrib`: Some studies frame contribution as opt-in/opt-out, but most use explicit choices.
- `show_punishment_id`: Anonymity and observability are addressed as moderators, particularly in networked and cross-cultural settings.
- `show_other_summaries`: Peer outcome observability frequently included as a feedback/information structure, recognized as important.

**Sparse or effectively missing:**
- Some fine distinctions, such as the effect of `default_contrib` and `show_punishment_id` separately from other information structure variables, are less commonly isolated.
- Very large group sizes (>16), highly dynamic or flexible group formation, and some novel combinations of dimensions (e.g., chat plus high-cost punishment in very large groups) are less represented.
- There is limited evidence on very short (1–2 round) or extremely long (100+ round) games, or on settings with highly complex feedback structures or real-world field implementations with direct monetary punishments.

---

# 7) Important Limitations

**1. Parameter Sparsity in Some Dimensions:**  
Not all 14 prediction dimensions are fully crossed; some (e.g., high values of `player_count`, hybrid chat+punishment, or rare combinations of information feedback and multiple sanction systems) are underexplored. Predictions for novel or extreme values should, therefore, be made with caution.

**2. Contextual Modifiers and External Validity:**  
Cultural context, baseline social norms, and field vs. lab setting significantly moderate the efficiency effect of punishment; identical game mechanics can yield opposite results depending on these factors.

**3. Behavioral vs. Payoff Outcomes:**  
Many studies focus on contribution or cooperation rather than efficiency. Effects on cooperation do not always translate to increased efficiency due to punishment costs, retaliation, or antisocial punishment.

**4. Ambiguity and Heterogeneity:**  
Where monitoring is imperfect, punishment is often misdirected or antisocial, leading to efficiency losses; importance of institution design (targeted vs. untargeted punishment) is high, and outcomes can be ambiguous or even negative for efficiency.

**5. Exclusion of Field Population Diversity:**  
Findings from student or WEIRD populations may not generalize; rates of antisocial punishment, norm salience, and group composition collide with design variables in ways not always captured by experimental manipulation.

**6. Theoretical vs. Empirical Gaps:**  
Simulation and theory papers explore a wider parameter space than experiments. Some robust theoretical predictions (e.g., from spatial models, phase diagrams) may not align with experimental results in human settings due to psychological, cognitive, or motivational factors unmet in models.

**7. Treatment of Exclusion/Ostracism:**  
While evidence shows that exclusion often outperforms monetary punishment for efficiency, many experimental designs do not compare both directly. Where only exclusion or only punishment is present, cross-design prediction is less precise.

**8. Downstream Policy and Time-Scaling:**  
Laboratory timescales may not match those required for efficiency gains to emerge in real populations, especially where initial high punishment costs only pay off after many rounds.

**9. Limitations in Causality and Mechanism Attribution:**  
While institutional choice, communication, and reputation often moderate punishment effects, their interplay is complex, and causality is not always cleanly identified.

---
**In summary:**  
This literature base provides unusually rich, directly relevant evidence for predicting the efficiency impact of enabling punishment in PGG-like games, conditional on game design and control efficiency. Key task dimensions—especially group size, rounds, MPCR, punishment cost/technology, and communication—are directly supported, but heterogeneity due to social context, antisocial punishment, monitoring quality, and institution structure pose important caveats. The efficiency gain from enabling punishment is robust and sizable in canonical repeated linear public goods games with low or declining control efficiency, but can be absent or negative where punishment is mistargeted or the context is hostile. Assignment of prediction confidence should account for these domain-dependent moderators.
