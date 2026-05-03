# 1) Evidence Base

The evidence base is composed entirely of theoretical papers (n = 32) with no empirical or experimental studies. All findings are derived from formal models, simulations, or analytical/theoretical arguments, often supported by extensive parameter sweeps. The coverage is relatively broad in terms of the variants and mechanisms considered—public goods games (PGGs), closely related social dilemmas, models with spatial structure, and extensions involving indirect reciprocity, leadership, or anti-social punishment. However, for the core prediction task—estimating the effect of enabling peer punishment on efficiency in PGG-like environments—the directly applicable literature is mostly theoretical, with many papers reporting on behavioral outcomes rather than efficiency or total payoff.

The set features many studies addressing the mechanisms and conditions for the evolution or stability of cooperation (and, by extension, the use and effect of punishment/sanctions), sometimes in PGGs and sometimes in adjacent game families (e.g., Prisoner's Dilemma, Snowdrift Game). Overall, the evidence is primarily mechanistic and qualitative, with a few papers providing closed-form or parameter-dependent predictions for efficiency/payoff outcomes under varied punishment regimes.

# 2) Task Relevance

**pgg_or_variant**  
- *Exact*: Numerous papers use the standard linear or all-or-nothing public goods game as the main model, often with peer punishment mechanisms (e.g., Wolff, 2012; Fang et al., 2020; Wang & Lv, 2019).
- *Close*: Several expand to related repeated, spatial, or structured social dilemmas without departing far from PGG rules. Some focus on pairwise games, volunteer dilemmas, or division-of-labor games (e.g., Nakamaru et al., 2018; Camera & Gioffré, 2014).
- *Adjacent/Weak*: A substantial fraction deal with games outside the multi-player PGG context or where PGG is only a background motivation.

**punishment_or_sanctions**  
- *Exact*: Multiple papers focus directly on costly peer punishment, exclusion, or formal sanctioning mechanisms in PGGs (Wolff, 2012; Fang et al., 2020; Wang & Lv, 2019).
- *Close*: Many explore punishment analogues (e.g., reputation loss, payoff transfer, exclusion) in spatial or evolutionary contexts.
- *Adjacent*: Some treat reward only, or consider mechanisms like partner selection or peer exclusion only as contextual references.

**efficiency_or_related_payoff_outcome**  
- *Exact*: Fewer papers report efficiency or total group payoff as a primary outcome (e.g., Wolff, 2012; Wang & Lv, 2019; Camera & Gioffré, 2014).
- *Close/Adjacent*: Far more report cooperation or contribution rates, the abundance of strategy types, or frequencies of punishment assignment.
- *Weak/None*: Some do not report payoff-related outcomes, focusing instead on evolutionary stability, coexistence, or structural dynamics.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:**  
  - *Direct efficiency or group payoff* is explicitly modeled or calculated in a limited subset (e.g., Wolff, 2012; Wang & Lv, 2019; Camera & Gioffré, 2014). Quantitative predictions are typically parameter-sensitive and theoretical.
  - Other papers report average payoff per player, welfare, surplus, or Nash equilibrium payoffs.

- **Non-payoff behavioral outcomes:**  
  - Far more common are: cooperation/contribution rates, frequency of punishment assigned, norm compliance, strategy abundance, or network/structural metrics (e.g., Chen et al., 2018; Kaiping et al., 2016).
  - Some outcomes are frequencies of antisocial punishment, retaliation, or transitions/coexistence between strategy types.

- These distinctions are crucial: increases in cooperation rates or contribution frequency do not necessarily translate to increased efficiency, especially when punishment is costly.

# 4) Main Findings Relevant To Prediction

Synthesized across the most relevant papers:

- **Punishment can increase efficiency—conditionally:**  
  - When the cost per unit punishment is low relative to the impact on defectors, and when retaliation or anti-social punishment is absent or costly, enabling peer punishment enables more cooperation and increases efficiency (Wolff, 2012; Fang et al., 2020; Wang & Lv, 2019).
  - When punishment is effective (greater impact per cost), efficiency increases are more likely, with the risk of negative returns if costs are too high or non-cooperating defectors retaliate.

- **Limits of punishment for efficiency:**  
  - If punishment is too costly, or if anti-social punishment and retaliation are easy and unpunished, overall efficiency may plateau or even decline compared to the control, as group resources are wasted on mutual defections and punishment cycles (Wolff, 2012; Gao et al., 2015).
  - The presence of bribery, corruption, or low monitoring/incentive for enforcers undermines punishment’s effect on efficiency (Fang et al., 2020).

- **Game structure moderates punishment’s effect:**  
  - Group size, number of rounds, and spatial or network structure all influence the parameter region in which punishment promotes efficiency. Small groups and short games have fewer opportunities for strategic retaliation to undermine punishment, and spatial structure can foster clusters of cooperation that amplify the effect of punishment (Kaiping et al., 2016; Wang & Lv, 2019).
  - Structured populations often allow punishment and cooperation to emerge more readily, especially with group competition or migration (Kaiping et al., 2016; Wei et al., 2021).

- **Centralized vs decentralized punishment and antisocial punishment:**  
  - Centralized (pool) punishment is generally more robust than decentralized (peer) punishment when anti-social punishment (punishing cooperators) is possible (Gao et al., 2015).
  - Anti-social punishment can neutralize or even reverse the positive effect of decentralized peer punishment on efficiency.

- **Parameter sensitivity and non-monotonic effects:**  
  - The effect of punishment on efficiency is often non-monotonic: moderate punishment intensity is often optimal, as too high costs (from excessive or misdirected punishment) reduce efficiency (Chang & Zhang, 2021).

- **Retaliation and stability issues:**  
  - Retaliatory punishment and the shadow of the future have complex impacts: if the continuation probability (number of rounds, patience) is high, punishment may lose effectiveness due to the threat of retaliation (Wolff, 2012).

- **Role of leader/authority punishment:**  
  - Exclusion and punishment by a benevolent leader with performance-based incentives can sometimes overcome the second-order free rider problem, but are vulnerable to bribery and efficiency loss if leader incentives are weak (Fang et al., 2020).

# 5) Prediction Guidance

- **Efficiency prediction should be conditional:**  
  - Efficiency with punishment enabled (vs. control) increases primarily when *punishment is effective and not too costly*, *retaliatory mechanisms are limited or absent*, and other design dimensions (player count, game length, spatial structure) are favorable (Wolff, 2012; Wang & Lv, 2019).
  - The efficiency effect is *parameter-sensitive*: predictions should reference the magnitude of *punishment_cost*, *punishment_tech* (i.e., impact per unit cost), and *player_count*, as well as *num_rounds* (which proxies for the shadow of the future and opportunity for retaliation).
  - Structured populations (e.g., spatial, group-based) tend to enhance the positive effect of punishment on efficiency, especially when group competition or fitness-based migration is present (Kaiping et al., 2016).
  - Centralized punishment or strong performance incentives for enforcers are associated with higher expected efficiency compared to decentralized, retaliation-prone peer punishment (Fang et al., 2020; Gao et al., 2015).
  - Contexts with high *punishment_cost* or easy anti-social punishment predict low or negative efficiency effects of punishment.

- **Control game efficiency is a key baseline:**  
  - The higher the control efficiency, the smaller the potential for punishment to increase efficiency, unless punishment also suppresses occasional defection or enables stable full cooperation.

- **Behavioral outcomes are not substitutes for efficiency:**  
  - Many papers show increased cooperation/contribution rates with punishment, but do not account for payoff costs. For prediction of efficiency, focus only on findings where both benefits (higher contribution) and costs (of punishment) are included in the outcome measure.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- `player_count`: Most models; widely modeled as a key factor in group dynamics, with larger groups sometimes diluting the effect of punishment.
- `num_rounds`: Modeled through continuation probability or explicit round number; important for repeated-game effects, retaliation, and equilibrium analysis.
- `mpcr`: Always present in payoff calculations.
- `punishment_cost`, `punishment_tech` (aka fine per cost): Central to many findings—effectiveness and cost interact non-linearly to predict efficiency outcomes.
- `all_or_nothing`: Modeled in some settings; affects the strength and clarity of punishment signals.
  
**Indirectly or Occasionally Informed:**
- `show_n_rounds`, `show_other_summaries`: Discussed in papers dealing with information availability or monitoring.
- `reward_exists`, `reward_cost`, `reward_tech`: Only a few adjacent papers compare reward mechanisms to punishment; effects are sometimes modeled in hybrid settings.
- `show_punishment_id`: Touched upon in studies of antisocial punishment and retaliation.

**Contextually Discussed or Sparse:**
- `chat`, `default_contrib`: Rarely modeled explicitly; their effects can be inferred only contextually (e.g., via communication or framing studies).
- `show_punishment_id`: Only addressed where anonymity vs. identification modulates retaliation/antisocial punishment.

**Effectively Missing:**
- Empirical calibration of real effect sizes and heterogeneity for each dimension is largely absent, as all papers are theoretical.

# 7) Important Limitations

- **Absence of empirical data:**  
  The entire set is theoretical; no empirical or experimental papers test or estimate actual effect sizes or validate theoretical predictions in real groups.

- **Efficiency not always a primary outcome:**  
  Many papers focus on cooperation/contribution rates, evolutionary stability, or frequencies of behavioral types, not efficiency or total group payoff. Results based only on increased cooperation/contribution may overstate the impact on efficiency due to the costs of punishment.

- **Design dimension coverage is uneven:**  
  Not all 14 predictive dimensions are addressed in each paper, and some, such as communication (`chat`), default contribution framing, and the specific implementation of summary/monitoring information, are largely missing.

- **Quantitative predictions are parametric and context-dependent:**  
  The effectiveness of punishment for increasing efficiency is shown to depend non-monotonically and often non-linearly on parameters (e.g., punishment effectiveness per cost, group size, round number), making generalization difficult.

- **Punishment design matters critically:**  
  The literature shows that the form of punishment (centralized vs decentralized, peer vs leader, possibility of anti-social/retaliatory punishment) is a key determinant, but operationalizations in prediction tasks may not fully capture this nuance.

- **Limited scope for indirect or adjacent findings:**  
  Many adjacent papers provide useful mechanistic context but cannot substitute for direct evidence about efficiency impacts—for example, showing increases in cooperation do not guarantee improved efficiency once punishment costs are considered.

- **Ambiguity and disagreement:**  
  Some models show that punishment can *reduce* efficiency under certain conditions (high cost, easy retaliation, anti-social punishment). These negative effects may be underemphasized given the focus on the evolution or stability of cooperation.

---

**Bottom line:**  
The literature supports the general prediction that enabling peer punishment increases efficiency in PGG-like environments *when punishment is effective and not too costly, retaliation/antisocial punishment are hard or rare, and group structure is favorable*; but the effect is highly parameter-dependent, can be negative in adverse contexts, and is only robustly evidenced in theoretical models rather than empirical data. Most design dimensions are directly or indirectly informed, but there's a lack of payoff-based empirical outcome evidence to support fine-grained or quantitative prediction.
