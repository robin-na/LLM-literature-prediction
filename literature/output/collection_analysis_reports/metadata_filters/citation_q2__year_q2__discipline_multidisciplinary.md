# 1) Evidence Base

The paper set includes 32 papers with a broad mix of empirical (primarily lab experiments), theory, and simulation studies. The core of the evidence directly addresses public goods games (PGGs) or closely related repeated social dilemmas, particularly focusing on the introduction and effectiveness of peer punishment mechanisms. Several highly relevant papers provide both theoretical and simulation-based arguments regarding when and how punishment increases group efficiency (Hetzer & Sornette, 2013; Roberts, 2013; Ye et al., 2016), while a smaller subset offers direct empirical evidence on efficiency changes with punishment (Bravo & Squazzoni, 2013; van Miltenburg et al., 2017). There is also notable coverage of adjacent or related game forms (Prisoner’s Dilemma, trust games, networked games), with variable direct applicability to the PGG with punishment prediction task.

Overall, the evidence base for predicting the efficiency impact of enabling punishment in true PGG designs is solid in theory and moderately strong in empiricism, though certain design dimensions and empirical scenarios are underrepresented.

# 2) Task Relevance

**PGG or Variant (`pgg_or_variant`)**
- **exact:** Several theory and empirical papers are direct PGGs (Hetzer & Sornette, 2013; Roberts, 2013; Ye et al., 2016; Paál & Bereczkei, 2015; Kubena et al., 2014; Ozono et al., 2016; Fosgaard & Piovesan, 2015; Bravo & Squazzoni, 2013), providing highly task-relevant models and findings.
- **close/adjacent/weak:** A large number of papers address close variants (common-pool resource games, multi-player social dilemmas, modified PGGs, or multiplayer PDs), relevant for understanding edge cases and generalizations.

**Punishment or Sanctions (`punishment_or_sanctions`)**
- **exact:** Many papers directly manipulate or model punishment in PGGs or close analogs (Hetzer & Sornette, 2013; Roberts, 2013; Ye et al., 2016; Paál & Bereczkei, 2015; Kubena et al., 2014; Bravo & Squazzoni, 2013; van Miltenburg et al., 2017).
- **adjacent/weak:** Some explore adjacent concepts, such as collective/institutional sanctioning (Ozono et al., 2016), reward only (Gao et al., 2015), or mechanisms influencing punishment propensity (Konishi et al., 2017).

**Efficiency or Related Payoff Outcome (`efficiency_or_related_payoff_outcome`)**
- **exact:** Several theoretical and some empirical studies directly report efficiency or group payoff changes with punishment (Hetzer & Sornette, 2013; Roberts, 2013; Ye et al., 2016; Bravo & Squazzoni, 2013; van Miltenburg et al., 2017; Ozono et al., 2016).
- **adjacent/close:** Many report only behavioral outcomes (contributions, punishment frequency), or present payoff outcomes only in adjacent games.
- **none/weak:** A subset provides no relevant outcome for the prediction task.

# 3) Outcomes Measured In The Literature

- **Payoff-related (efficiency, group payoff, welfare, earnings, surplus):**
  - Direct efficiency or group payoff is measured in both theory (Hetzer & Sornette, 2013; Roberts, 2013; Ye et al., 2016; Ohdaira, 2017; Wang et al., 2014; Ito & Yoshimura, 2015) and a smaller subset of empirical papers (Bravo & Squazzoni, 2013; van Miltenburg et al., 2017; Ozono et al., 2016).
  - Some studies only suggest payoff effects via proxies or adjacent outcomes rather than direct measurement.
- **Non-payoff behavioral outcomes (contribution rate, cooperation, punishment assigned, norm compliance, motivation):**
  - Many laboratory papers—in particular, those focused on punishment dynamics (Kubena et al., 2014; Paál & Bereczkei, 2015)—provide only behavioral measures such as contributions or punishment assignment.
  - Studies with non-standard designs often focus exclusively on these behavioral outcomes.
  - Several theory papers model cooperation rates rather than group payoff.

# 4) Main Findings Relevant To Prediction

**Empirical and Theoretical Synthesis:**
- **When does punishment increase efficiency?**
  - Strong theoretical and simulation results predict that peer punishment increases efficiency in repeated PGGs, if punishment cost is sufficiently low, punishment impact is strong, and the marginal return to cooperation is high (Hetzer & Sornette, 2013; Roberts, 2013; Ye et al., 2016).
  - The efficiency effect is robust in standard, linear PGGs when above specified cost-effectiveness thresholds.
  - Empirical PGG studies corroborate these findings: compared to control (no punishment), enabling punishment increases efficiency, but is often less effective than rewards or institutional sanctions (Bravo & Squazzoni, 2013).
  - However, there are exceptions. In noisy monitoring environments, punishment can waste resources and reduce efficiency below control (van Miltenburg et al., 2017). In rank-based or highly competitive settings, punishment may be used strategically for rivalry, not to enforce cooperation, and thus does not improve (and may harm) efficiency (Paál & Bereczkei, 2015).

- **Mechanism and threshold arguments:**
  - Theory highlights specific threshold conditions for punishment to be efficiency-enhancing, often formalized as inequalities relating punishment cost (p), impact (q), and benefit/cost of cooperation (Roberts, 2013).
  - Evolutionary models point to a switch from defection to coordination regimes when punishment is both present and strong enough; below that threshold, efficiency gains are not realized (Hetzer & Sornette, 2013).

- **Moderating design dimensions:**
  - Group size, punishment cost and technology, marginal per capita return (MPCR), and the structure of returns to cooperation (e.g., increasing returns to scale) are direct, theoretically grounded moderators.
  - Information structure (noisy versus perfect monitoring), type of punishment technology (peer vs. institutional), and presence of reward further moderate the payoff effect.
  - Chat/communication is sometimes mentioned as supporting baseline cooperation in the absence of punishment, but its direct interaction with punishment and efficiency is much less studied.

- **Payoff versus behavioral effects:**
  - Higher contributions through punishment do not always raise efficiency if resources are wasted on mutual or antisocial punishment (Kubena et al., 2014; Paál & Bereczkei, 2015), or if punishment is not well targeted.
  - Some studies find increased cooperation but ambiguous or unmeasured efficiency impact due to unreported group payoffs.

# 5) Prediction Guidance

**When predicting average efficiency with peer punishment enabled, conditional on game design and control efficiency:**
- Expect **large efficiency gains** when enabling punishment in standard, repeated, small-to-moderate group-size PGGs without noise, provided the punishment cost is not too high, the impact is substantial, and baseline efficiency is low (Hetzer & Sornette, 2013; Roberts, 2013; Bravo & Squazzoni, 2013).
- **Noisy monitoring** or environments where punishment is misallocated can **reduce or reverse** these gains (van Miltenburg et al., 2017), so models should downgrade the expected impact under such conditions.
- **Competitive settings** (e.g., rank-based payoffs) may produce **no efficiency gain or even harm**, since punishment is used against rivals, not defectors (Paál & Bereczkei, 2015).
- **High rates of antisocial punishment** (targeting high cooperators) can offset contribution gains and limit or nullify efficiency improvements, especially in large groups or certain cultural contexts (Kubena et al., 2014).
- Consider **design dimensions** such as player count, number of rounds, MPCR, punishment cost, and information structure as critical to the effect size and direction.
- The presence of **institutional punishment** or reward mechanisms can dominate or substitute for peer punishment in raising efficiency (Ozono et al., 2016; Bravo & Squazzoni, 2013).

# 6) Design Dimensions Highlighted Across Papers

**Directly (well) informed:**
- `player_count`, `num_rounds`, `all_or_nothing`, `mpcr`, `punishment_cost`, `punishment_tech`: Commonly varied or highlighted in both theory and empirical PGG studies, with explicit links to predicted or observed efficiency effects.
- `show_other_summaries`: Sometimes present (mostly in studies reporting feedback, not always experimentally varied).
- `reward_exists`, `reward_cost`, `reward_tech`: Discussed and/or manipulated in a subset of papers (Bravo & Squazzoni, 2013; Gao et al., 2015).

**Indirectly or contextually discussed:**
- `chat`: Discussed or present as a facilitator in some designs but rarely central to payoff-based findings regarding punishment effects.
- `show_n_rounds`: Sometimes included to prevent or allow end-game effects; theoretical importance noted, but empirical manipulation is less common.
- `default_contrib`: Rarely varied jointly with punishment; studied in isolation (Fosgaard & Piovesan, 2015).

**Sparse or missing:**
- `show_punishment_id`: Not systematically manipulated; anonymity versus identifiability of punishers/rewarders is only rarely addressed as a focus.
- Many papers do **not** vary or systematically analyze effects of summary feedback or explicit identification, limiting evidence for this dimension.

# 7) Important Limitations

- **Behavioral — not payoff — focus in many studies:** A sizable portion of the literature measures only contributions or punishment assignments, not efficiency, group payoff, or welfare. These findings cannot be safely extrapolated to predict efficiency effects of punishment.
- **Empirical data on efficiency gains is limited** to a handful of experimental studies; much of the predictive clarity comes from formal models and simulations.
- **No systematic coverage of all design dimensions:** Not all 14 dimensions are fully or directly studied; some, like default contributions or punishment visibility, are largely unaddressed in the context of efficiency.
- **Context-sensitivity and exceptions:** While standard theory predicts positive effects of punishment on efficiency, exceptions (e.g., under noise, in competitive environments, in presence of antisocial punishment) are well documented and must temper strong predictions.
- **Sparse evidence on large groups or heterogeneous populations:** Most detailed analyses address small to moderate group sizes with strangers; effects in large, stratified, or culturally diverse populations remain ambiguous.
- **Adjacent/indirect evidence dominates for complex or hybrid designs:** Designs with sophisticated social structures, real-world stakes, or alternative sanctioning institutions are either underrepresented or only weakly generalizable to standard PGGs.
- **Limited evidence on interaction effects:** How multiple design features (e.g., reward plus punishment, or chat with punishment) jointly shape efficiency is rarely empirically studied.

---

**In summary:**  
Predictions of efficiency gains with punishment enabled in PGGs should be grounded primarily in theory and supported by targeted empirical findings, being cautious to account for specific game design moderators and the limitations in empirical coverage of some design dimensions. Direct evidence for certain parameter regimes and for all design dimensions is lacking, while some contexts show neutral or negative efficiency effects, highlighting the importance of a conditional, design-aware predictive approach.
