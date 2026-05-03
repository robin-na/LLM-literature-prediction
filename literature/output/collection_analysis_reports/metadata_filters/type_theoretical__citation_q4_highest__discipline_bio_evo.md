# 1) Evidence Base

The paper set consists entirely of theoretical analyses—mostly mathematical, simulation, and conceptual models—with no empirical or experimental studies measuring real or simulated participant behavior. The breadth of coverage is extensive concerning theoretical mechanisms, moderators, and parameter dependencies in public-goods-game (PGG) and related social dilemma environments, including standard, threshold, spatial, and indirect reciprocity variants. Direct attention to peer punishment and its effect on **group efficiency** (total payoff relative to full cooperation) is fairly common, but several papers address adjacent incentive mechanisms (rewards, exclusion, reputation) or focus primarily on cooperation/contribution rather than direct payoff-based efficiency. Many models are informed by, or interpret, classic empirical laboratory findings (e.g., Fehr & Gächter) as supporting evidence.

The evidence base is thus:
- **Theoretical** (all papers).
- **Simulation-supported** for most findings (especially replicator dynamics, agent-based models).
- **Mechanistically rich**—detailing the conditions, moderators, and evolutionary dynamics relevant to punishment, cooperation, and payoff outcomes.
- **Moderately broad** for the downstream prediction task, with some missing dimensions and sparse or indirect coverage of specific experimental game design features.

# 2) Task Relevance

**pgg_or_variant**:  
- *Exact*: The majority of papers focus on, or use as baseline, standard linear public goods games or close variants (e.g., threshold, spatial, networked PGGs). Several examine adjacent social dilemmas (e.g., repeated PD, indirect reciprocity), providing relevant analogies.
- *Relevance*: Mostly **exact**; some **close** or **adjacent**.

**punishment_or_sanctions**:  
- *Exact*: Most papers analyze peer or institutional punishment (costly peer punishment, exclusion, or institutional fines).
- *Partial*: Some focus on adjacent mechanisms (e.g., reputation loss, social norm enforcement, reward mechanisms) rather than explicit punishment.
- *Relevance*: Generally **exact**; some **close** or **adjacent** when only non-costly or reputational punishment is modeled.

**efficiency_or_related_payoff_outcome**:  
- *Exact*: Many models compute explicit group payoff or efficiency as the primary outcome.
- *Close/Adjacent*: Others use high cooperation rates as a proxy for efficiency without modeling the payoff cost of punishment, or focus on evolutionary fitness or success of strategies.
- *Relevance*: **Exact** in several key papers, but a considerable subset measure *behavioral* rather than *payoff* outcomes, reducing direct applicability.

**Summary**:  
The literature has high relevance to PGGs and punishment but only **moderate to high relevance to efficiency outcomes**, with some ambiguity where papers interpret increased cooperation as equivalent to increased efficiency without reporting payoff impacts (especially considering costly punishment).

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes** (directly corresponding to efficiency):
    - Group efficiency/total payoff relative to maximum possible (fully cooperative) levels (e.g., *Cressman et al., 2012*; *Gintis, 2000*; *Rand et al., 2010*).
    - Average group earnings, welfare, or fitness (e.g., *Henrich & Boyd, 2001*; *Adami et al., 2016*; *Sasaki & Uchida, 2013*).
    - Explicit treatment of surplus, total coins, or welfare in model output.

- **Behavioral Outcomes** (*non-payoff*):
    - Contribution rates, cooperation rates, fraction of punishers, norm compliance.
    - Frequency/evolution of cooperation or punishment strategies.
    - Stability or evolution of norms/strategies without reporting explicit group welfare.

The literature is **stronger on behavioral mechanisms** than on quantitative reporting of efficiency, with several models assuming that increased cooperation translates to increased efficiency, even when the cost of punishment is substantial.

# 4) Main Findings Relevant To Prediction

Synthesizing across the set, the literature supports several central points relevant to predicting the effect of peer punishment on efficiency in PGG-like games:

- **Enabling Punishment Generally Increases Efficiency—With Moderators**:  
    Most models (especially those tailored to PGGs) predict that enabling peer punishment increases group efficiency relative to baseline (punishment-disabled), but *only* if punishment is effective (high fine-to-cost ratio) and not too costly (*Gintis, 2000*; *Henrich & Boyd, 2001*; *Bowles & Gintis, 2004*). If punishment is too costly or ineffective, efficiency gains are attenuated or even reversed (*Guala, 2012*).

- **Critical Role of Anti-Social Punishment and Retaliation**:  
    If anti-social punishment (punishment of cooperators) or retaliation against punishers is possible and prevalent, enabling punishment can fail to increase, or may **decrease**, efficiency (*Rand et al., 2010*; *Hauser et al., 2014*; *Janssen & Bushman, 2008*). The absence of antisocial punishment is a necessary condition for realizing efficiency gains from punishment.

- **Dependence on Game Design Dimensions:**
    - *Group Size*: Larger groups make cooperation harder to sustain, diminishing the effectiveness of punishment, though punishment extends the range of group sizes in which cooperation (and efficiency) is possible (*BOYD & RICHERSON, 1992*).
    - *Punishment Cost and Effectiveness*: Lower punisher cost and high impact on defectors consistently predict higher efficiency gains from punishment (*Gintis, 2000*; *Gardner & West, 2004*).
    - *Information Structure*: Public visibility of punishment (reputation, institutional transparency) amplifies the efficiency effect (*Schoenmakers et al., 2014*; *dos Santos et al., 2011*).
    - *Spatial/Network Structure*: Spatial or networked play generally enhances the positive effect of punishment on efficiency, as clusters of moralists (punishing cooperators) can eliminate defectors (*Brandt et al., 2003*; *Helbing et al., 2010*).

- **Institutional and Social Context Matters**:  
    Institutional punishment or exclusion (rather than peer punishment) can sometimes produce more stable high-efficiency outcomes, particularly when combined with rewards or cost-sharing mechanisms (*Cressman et al., 2012*; *Sasaki & Uchida, 2013*).

- **Potential Negative Side-Effects**:  
    Costly punishment can reduce efficiency by destroying resources, especially if cooperation is already high or costly punishment is used frequently (*Guala, 2012*; *Sigmund, 2007*).

- **Role of Norms and Learning Mechanisms**:  
    Social learning, conformist transmission, and reputation systems can stabilize punishment and cooperation, magnifying efficiency gains (*Henrich & Boyd, 2001*; *dos Santos et al., 2011*).

- **Reward Mechanisms as Comparators**:  
    Reward can also increase efficiency, and in some models, is more efficient than punishment; models comparing both typically find punishment more effective at stabilizing cooperation but more costly (*Rand & Nowak, 2013*).

# 5) Prediction Guidance

Based on this literature, prediction of average efficiency with peer punishment enabled (controlling for design dimensions and control efficiency) should:

- **Expect Increased Efficiency from Adding Punishment in Baseline Defector-Dominated or Mixed Games**, provided:
    - Punishment is effective (high punishment magnitude per unit cost),
    - Anti-social punishment and easy retaliation are absent or rare,
    - The cost of punishment to group members is not too high,
    - The group is not extremely large,
    - The game design provides sufficient information for effective punishment targeting (e.g., public summary displays, reputational or round-tracking features).

- **Quantitative Effect Size**:  
    The predicted magnitude of efficiency improvement is likely to be substantial when baseline (control) efficiency is low-to-moderate, punishment is efficient, and design structure supports norm enforcement. For settings where baseline efficiency is already high (near full cooperation), enabling punishment can sometimes reduce efficiency due to unnecessary punishment costs.

- **Critical Moderators**:
    - If anti-social punishment (punishing cooperators or arbitrary punishment) is allowed, or if punished defectors can easily retaliate, predicted efficiency gains are greatly reduced or can even reverse (punishment-enabled games perform similarly or worse than control; *Rand et al., 2010*; *Hauser et al., 2014*; *Janssen & Bushman, 2008*).
    - If punisher anonymity is protected, retaliation is less likely and efficiency gains are more robust.
    - If communication or chat is enabled, the need for actual punishment decreases as norms are stabilized more quickly, sometimes allowing punishment to serve as a threat rather than a frequent costly action.

- **Control Efficiency Moderation**:  
    Where the control (punishment-disabled) game already has moderate to high efficiency due to other mechanisms (reputation, network structure, reward), the incremental gain from enabling punishment is smaller and can be offset by punishment costs (*Archetti et al., 2011*).

- **Reward and Exclusion Mechanisms**:  
    Including reward or social exclusion with punishment can further increase (or sometimes replace) the positive efficiency effect, particularly when both are institutionalized (*Cressman et al., 2012*; *Sasaki & Uchida, 2013*).

- **Limitations of Generalization**:  
    Models recommend tailoring prediction to game-specific parameter values; for games at or near the critical point for cooperation (MPCR threshold), punishment has the largest marginal effect (*Adami et al., 2016*).

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions** (modeled explicitly in efficiency-focused PGG/punishment models):
- `player_count` (group size): Modeled and found to moderate punishment’s effect (especially in *BOYD & RICHERSON, 1992*; *Gintis, 2000*).
- `num_rounds`: Modeled widely; repeated interaction allows punishment to have a sustained effect (across most models).
- `mpcr`: Central in all efficiency analyses—critical moderator of the cooperation threshold and marginal effect of punishment.
- `punishment_cost`, `punishment_magnitude`, `punishment_tech`: Modeled in detail; the fine-to-fee ratio is a key parameter in nearly all theoretical PGG+punishment studies.
- `show_n_rounds`/visibility of the time horizon: Modeled occasionally, relevant for backward induction effects.
- `reward_exists`, `reward_cost`, `reward_tech`: Included in some models, which compare combined incentive schemes versus punishment alone.
- `all_or_nothing`: Modeled in some, but most focus on continuous PGGs.

**Indirectly Informed or Sparsely Modeled Dimensions**:
- `chat` (communication): Discussed as a moderator (e.g., *Anderies et al., 2011*), but rarely modeled explicitly in payoff outcome models.
- `default_contrib` (opt-in/opt-out framing): Only peripherally addressed.
- `show_other_summaries`/feedback: Modeled in some papers on reputation and information, important for effectiveness of punishment, but details are sometimes abstracted.
- `show_punishment_id`: Discussed as a key moderator (punisher anonymity/retaliation) in several, but not always parameterized.

**Dimensions Largely Missing or Contextual Only**:
- `reward_exists`, `reward_cost`, `reward_tech`: Present in some comparative studies but absent from many core PGG punishment models.
- `default_contrib`, `chat`, `show_other_summaries`: Generally only contextually discussed, at best.

# 7) Important Limitations

- **Empirical Data is Absent**:  
    All evidence is theoretical or simulation-based. Models assume evolutionary dynamics or rational behavior not directly validated against human or animal behavior in controlled laboratory or field experiments.

- **Parameter Calibration Uncertain**:  
    Prediction of effect sizes for a specific game requires appropriately mapping real-world or experimental game parameters (e.g., MPCR, punishment cost, visibility) onto model parameters. Many papers give only qualitative or relative predictions.

- **Overreliance on Behavioral Proxies**:  
    Several findings infer efficiency changes based on increased cooperation rates without adjusting for the cost of punishment itself, which can lead to overestimation of efficiency gains if punishment remains frequent and costly.

- **Sparse Attention to Certain Design Features**:  
    Some design dimensions critical for lab and field experiments (chat, framing, summary feedback, punisher/rewarder identity, default contributions, etc.) are rarely modeled with explicit payoff effects, limiting the ability to account for their moderation in predictions.

- **Anti-Social Punishment and Retaliation Insufficiently Quantified**:  
    While highlighted as key failure modes for punishment's effectiveness, the structural and parametric dependence of anti-social punishment and retaliation on design features is not always formalized.

- **Adjacency of Some Models**:  
    A fraction of the evidence is adjacent—relying on repeated PD, indirect reciprocity, partner choice, or group-structured interaction—so care must be taken not to overgeneralize beyond their context.

- **Lack of Heterogeneity and Human Diversity Modeling**:  
    Most models assume homogeneous populations; findings regarding individual differences, cultural norms, and variation in outcome due to framing or demographic diversity cannot be incorporated.

- **Assumption of Peer vs. Institutional Punishment**:  
    Some high-efficiency predictions depend on institutional (not peer) punishment or social exclusion, which are not always directly mapped to standard peer-punishment experimental designs.

---

## **Summary Table** (extracted from above for quick reference)

| Dimension                  | Directly informed?          | Level of evidence         |
|----------------------------|-----------------------------|--------------------------|
| player_count               | Yes                         | Strong (quantitative)    |
| num_rounds                 | Yes                         | Strong (quantitative)    |
| chat                       | Contextually discussed      | Weak/Indirect            |
| all_or_nothing             | Yes (in some)               | Moderate                 |
| default_contrib            | Context only                | Sparse                   |
| mpcr                       | Yes                         | Strong                   |
| punishment_cost            | Yes                         | Strong                   |
| punishment_tech/magnitude  | Yes                         | Strong                   |
| reward_exists              | Yes (some studies)          | Moderate                 |
| reward_cost/reward_tech    | Yes (some studies)          | Moderate                 |
| show_n_rounds              | Modeled occasionally        | Moderate                 |
| show_other_summaries       | Context only                | Weak                     |
| show_punishment_id         | Moderately modeled          | Moderate                 |

---

# **Bottom Line**
The literature provides strong **mechanistic** support and general conditions for when punishment is expected to increase average group efficiency in PGG-like environments, but the **effect size and even direction** depend strongly on game design parameters, the possibility of anti-social punishment/retaliation, and the cost-effectiveness of punishment. **Prediction must account for these moderators** and cannot assume a universally positive effect. Most relevant game design dimensions are addressed in at least some models, but empirical calibration and direct mapping to all experimental designs are limited.
