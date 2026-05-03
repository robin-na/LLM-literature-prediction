# 1) Evidence Base

The paper set consists of 189 papers, all theoretical in nature, including analytic, simulation, or agent-based modeling studies. There are no empirical or experimental studies. This constitutes an extremely broad, comprehensive theoretical base for the prediction task but leaves a gap in empirical calibration.

Coverage of public goods games (PGGs) is extensive, with the majority of papers either exactly matching the PGG context or modeling close variants or adjacent games (e.g., trust games, repeated prisoner’s dilemma, resource management dilemmas, or networked settings). Sanctioning mechanisms (punishment and to a lesser degree, reward) are a primary focus across the set, with numerous papers modeling a wide range of punishment systems: peer- and pool-based, central and decentralized, symmetric and asymmetric, probabilistic and deterministic, as well as exclusion, reputation, institutionalized, and voluntary/compulsory forms.

A substantial portion of studies directly address payoff-based outcomes (efficiency, group welfare, total earnings), while many focus solely on behavioral outcomes (contribution or cooperation rates, punishment frequency). Some closest-adjacent papers report on payoff outcomes (sometimes labeled as "adjacent" in relevance), but a non-trivial share reports only indirectly relevant outcomes.

Overall, this literature base is best described as broad, rich, and highly mechanistic, with an emphasis on theoretical boundary-setting, sensitivity analysis, and multi-dimensional modeling—but with a notable gap in direct experimental or field validation.

---

# 2) Task Relevance

This section assesses three dimensions for literature-task mapping:  
**a. pgg_or_variant**  
- **Exact**: The majority of papers model standard PGGs or their close formal variants (e.g., threshold PGGs, voluntary PGGs, networked PGGs).  
- **Close/Adjacent**: Many adjacent models (repeated PD, trust games, resource dilemmas, and games with environmental feedback or reward/exclusion) often share the critical structure of social dilemma and sanctioning, with parameter mappings to PGGs.  
- **Weak/None**: A subset deals only conceptually or in settings where group provision is not central (e.g., coordination games).

**b. punishment_or_sanctions**  
- **Exact**: Many papers simulate explicit, costly punishment as a treatment—peer, pool, coordinated, exclusion-based, or institutional.  
- **Close/Adjacent**: Others focus on reward, reputation, exclusion, or informal sanctions, or combine punishment with these (carrot-and-stick). Some consider indirect mechanisms or punishment analogs.  
- **Weak/None**: Several only provide context or discuss design issues without modeling punishment per se.

**c. efficiency_or_related_payoff_outcome**  
- **Exact**: A minority of the theoretical papers report group efficiency or payoff outcomes as a primary or explicit dependent variable.  
- **Close/Adjacent**: Many report average payoffs, welfare, resource levels, or "expected profit," which are closely associated with efficiency but sometimes not normalized to full cooperation.  
- **Weak/None**: A substantial share reports only cooperation/contribution frequency, norm compliance, or strategy fractions, which are not equivalent to efficiency; these must be treated as only indirect evidence.

---

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes:**  
- *Efficiency* (group payoff/maximum possible), group welfare/surplus, total group earnings, public good or resource level, average payoff.
- Sometimes system-level metrics such as resource sustainability, expected profit, or average income.
- A subset report formulaic or asymptotic efficiency outcomes and explicit threshold conditions for full cooperation.

**Non-Payoff Behavioral Outcomes:**  
- Contribution/cooperation rate, fraction of cooperators/defectors/punishers, norm compliance, punishment frequency or intensity.
- Frequencies of strategy types (e.g., punishers, loners, cooperators, defectors, second-order free riders).
- Success or stability of cooperation, fairness, strategy evolution, equilibrium phase structure, cluster formation.

Crucially, only those studies measuring group payoff, efficiency relative to full cooperation, or similar welfare outcomes provide exact support for the downstream task; studies limited to behavioral outcomes can only be used as mechanism support, not quantitative payoff prediction.

---

# 4) Main Findings Relevant To Prediction

**General Patterns**  
- **Punishment Dominates Defection in Many Parameter Regimes:** Across exact and close PGG variants, when punishment is sufficiently strong and/or well-designed, it reliably shifts the system from a defection regime (low payoff/efficiency) to a high-cooperation, high-efficiency regime (e.g., Hetzer & Sornette, 2013; Cui et al., 2019; Wang et al., 2011; Vasconcelos et al., 2022; Wang, Y. F. et al., 2015; Gámez et al., 2018; Yaman et al., 2023; Nuño et al., 2010; Farjam et al., 2015; Johnson, S., 2015).
- **Threshold Effects, Non-Linearity, and Bistability:** The efficiency benefit of punishment is rarely linear. There are often sharp threshold effects: below critical punishment intensity or effectiveness, little or no improvement; above, dramatic increase. Some models show bistability or path dependence—initial conditions (e.g., initial cooperation rate) can determine whether high or low efficiency outcomes are reached (Liu et al., 2024; Ye et al., 2016; Thorsten et al., 2012).
- **Punishment Cost-Effectiveness is Essential:** The gain from punishment is higher when punishment is inexpensive for punishers and highly detrimental to defectors (Roberts, 2013; Hintze et al., 2020; Hetzer & Sornette, 2013; Frey & Rusch, 2012). If the cost is too high or the effectiveness too low, punishment may *not* improve and can even reduce efficiency (Handfield et al., 2016; Honjo & Kubo, 2020; Farjam et al., 2015).
- **Network/Population Structure:** Structured populations (local interactions, network clustering, moderate group/cluster size) often amplify the positive effect of punishment (Bodnar & Salathé, 2012; Murase & Baek, 2021, 2024; Ohdaira, 2017; Vasconcelos et al., 2022), while well-mixed, anonymous, or large groups can dampen it or make defection more difficult to suppress (Boyd et al., 2014; Wang, Q. L. et al., 2020).
- **Institutional and Mechanism Design Matters:** The *type* of punishment (peer vs. pool, direct vs. exclusion, centralized vs. decentralized, possibility of extortion or misuse) is a major moderator of efficiency outcomes (Acemoglu & Wolitzky, 2021; Barron & Guo, 2021; Libois, 2022; Duéñez-Guzmán & Sadedin, 2012). Mechanisms allowing extortion, antisocial punishment, or abuse can eliminate the efficiency gain, even causing it to decrease relative to no punishment (Barron & Guo, 2021; Handfield et al., 2016; Honjo & Kubo, 2020).
- **Time Horizon and Repeated Play:** Punishment is more likely to improve efficiency in long-run, repeated, or partner-matching settings, allowing cooperation to stabilize and punishment costs to decline (Frey & Rusch, 2012; Roberts, 2013; Murase & Baek, 2021; Vasconcelos et al., 2022).
- **Role of Reward:** Reward systems can promote cooperation, but are generally less effective than punishment at eliminating defection and maximizing efficiency (Wang, Y. F. et al., 2011; Cui et al., 2019; Mondal et al., 2022; Chen et al., 2019). Misapplied or poorly designed rewards and combined mechanisms can be less effective or counterproductive.

**Critical Moderators and Design Dimensions**
- **player_count & group size:** Smaller groups make punishment more effective; large group size requires stronger or more centralized punishment (Boyd et al., 2014; Vasconcelos et al., 2022; Wang, Q. L. et al., 2020).
- **num_rounds:** Efficiency gains from punishment accumulate in longer and repeated interactions (Frey & Rusch, 2012; Roberts, 2013).
- **mpcr:** At low MPCR (scarce resources), well-designed punishment increases efficiency; at high MPCR, punishment may not be beneficial (Farjam et al., 2015; Ye et al., 2016).
- **punishment_cost, punishment_tech:** Lower cost and higher impact/fine are more likely to increase efficiency (Roberts, 2013; Hetzer & Sornette, 2013; Hintze et al., 2020; Liu et al., 2024).
- **reward_exists:** Reward can't fully substitute for punishment but can complement it (Cui et al., 2019; Mondal et al., 2022).
- **all_or_nothing, default_contrib, voluntary participation:** Discrete actions (all-or-nothing), opt-in framing, and voluntary participation change thresholds for punishment to be effective (Lv et al., 2023; Wang, Y. F. et al., 2015).
- **network/chat/structure, show_other_summaries:** More information and local interaction generally support greater effectiveness of punishment (Bodnar & Salathé, 2012; Vasconcelos et al., 2022; Ohdaira, 2017).
- **possibility of antisocial/retaliatory punishment:** If present, efficiency can decrease (Handfield et al., 2016; Honjo & Kubo, 2020).
- **exclusion/reputation/visibility:** Exclusion and reputation-based mechanisms can outperform costly punishment under some conditions (Rosas, 2008; Kang et al., 2024).

**Ambiguities and Disagreements**  
- In some parameter regimes (e.g., high punishment cost, short games, possibility of misuse), enabling punishment reduces efficiency or has no effect (Handfield et al., 2016; Honjo & Kubo, 2020; Barron & Guo, 2021).
- Effect of punishment is not universal: Moderated by social value orientation, structure, history of play, and possibility of mutation/noise (Honjo & Kubo, 2020; Thomadsen & Bhardwaj, 2011).
- Some models show bistable or path-dependent outcomes—efficiency is subject to coordination and initial strategy distributions (Liu et al., 2024; Ye et al., 2016).
- The mapping from behavior (e.g., cooperation rate) to efficiency is sometimes ambiguous: high cooperation rates with costly, misdirected, or inefficient punishment may not translate to high payoff.

---

# 5) Prediction Guidance

**What the Literature Strongly Supports:**
- When the control (no-punishment) efficiency is low and the introduced punishment mechanism has low cost and high effectiveness, enabling punishment *usually* substantially increases efficiency—often driving it near the full-cooperation/maximum–payoff regime, conditional on proper design (Cui et al., 2019; Hetzer & Sornette, 2013; Wang, Y. F. et al., 2011, 2015; Gámez et al., 2018; Nuño et al., 2010).
- The magnitude of the efficiency increase is highly sensitive to the *details* of the punishment design: cost, impact, institutional arrangement (peer vs. pool), mechanism for avoiding antisocial punishment, and alignment of punishment with defecting behavior (Acemoglu & Wolitzky, 2021; Frey & Rusch, 2012; Barron & Guo, 2021).
- MPCR and group size moderate the effect: low MPCR (hard social dilemmas) benefit more from punishment than high MPCR (less temptation to free ride); large groups require stronger, more centralized, or more efficiently coordinated punishment to maintain efficiency gains (Farjam et al., 2015; Bodnar & Salathé, 2012; Vasconcelos et al., 2022).
- Longer repeated interactions always strengthen the positive effect of punishment on efficiency because long-term stabilization allows punishment to decline and net payoffs to rise (Frey & Rusch, 2012; Roberts, 2013).
- Interventions that allow extortion, exploitation, or retaliation can *reduce* or even reverse the expected efficiency gain from enabling punishment (Barron & Guo, 2021; Handfield et al., 2016; Honjo & Kubo, 2020).
- If punishment is enabled but is too costly, misapplied, or limited in scope (e.g., applied only to non-elites), efficiency gains are not realized and can even be offset (Acemoglu & Wolitzky, 2021; Handfield et al., 2016; Honjo & Kubo, 2020).

**How to Map to Design Dimensions and Control Efficiency:**
- Given *all* design dimensions and the observed control game efficiency, the *size* and *sign* of the expected efficiency gain when enabling punishment should be predicted as a function of:
  - **Cost-Effectiveness of Punishment:** Lower *punishment_cost* and higher *punishment_tech* (fine/magnitude) predict greater efficiency gain (Roberts, 2013; Farjam et al., 2015; Hetzer & Sornette, 2013).
  - **Game Hardness (MPCR):** Lower *mpcr* predicts bigger marginal benefit of punishment (Farjam et al., 2015; Ye et al., 2016).
  - **Time Horizon (*num_rounds*):** More rounds mean greater net benefit, as cooperation stabilizes and punishment costs decrease (Frey & Rusch, 2012).
  - **Group Size (*player_count*):** Smaller groups find it easier to coordinate punishment, but institutional or pool punishment can restore efficiency in large groups if sufficiently strong (Bodnar & Salathé, 2012; Vasconcelos et al., 2022).
  - **Voluntary Participation, Entry Fee, Default Contribution:** Voluntary participation and entry fees interact with punishment to discourage defectors and support high efficiency (Wang, Y. F. et al., 2011, 2015).
  - **Network/Chat/Information (*show_other_summaries, chat*):** Local information, partner choice, network clustering can amplify effects, especially by making punishment more targeted and less costly (Bodnar & Salathé, 2012; Vasconcelos et al., 2022; Barron & Guo, 2021).
- If the control efficiency is already high (near full cooperation), adding punishment may add little or even reduce efficiency, particularly if punishment is costly or misapplied (Handfield et al., 2016; Farjam et al., 2015; Honjo & Kubo, 2020).
- *Conversely*, where control efficiency is low (free-riding dominates), activating an effective punishment mechanism (well-aligned, moderate cost, high impact, low risk of abuse/anti-social misuse) is predicted to yield a large positive effect, often sharply increasing efficiency towards the cooperative maximum.

**Use of Behavioral Outcomes:**
- Contribution and cooperation rates are only indirect evidence for efficiency; unless accompanied by payoff analysis, these should be used cautiously, and pay particular attention to possible negative efficiency impact through wasteful or misdirected punishment.

---

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**  
- *player_count*: Extensively modeled; group size is a key moderator (positive for smaller groups or with sufficient institutional enforcement for large groups).
- *num_rounds*: Long time horizon positively moderates efficiency impact.
- *mpcr*: A central parameter; efficiency benefit of punishment greatest when MPCR is low.
- *punishment_cost* and *punishment_tech*: Core; trade-off between cost and impact crucial for predicting effect size.
- *reward_exists*: Included in many models; can moderate (but not substitute for) punishment effects.
- *all_or_nothing*: Models include both binary and continuous contribution; interaction with discretization is analyzed in several studies.
- *show_other_summaries*, *chat*: Information features are acknowledged as important and explicitly modeled in several networked/game-theoretic papers.

**Indirectly Informed:**  
- *default_contrib* (framing), *show_n_rounds*, *show_punishment_id*: Sometimes treated as framing or context variables; occasional reference to identity/repeatedness. *default_contrib* is rarely a modeling focus but related through opt-in/opt-out discussions.
- *punishment magnitude* (if differentiated from cost): Often modeled jointly with *punishment_cost* as fine/cost ratio.

**Contextually Discussed / Sparse:**  
- *punishment_tech* (who can punish whom, institution vs. peer): Addressed in mechanism-comparison papers, but many models idealize this as either peer punishment or centralized; fine-grained technology mapping is rare.
- *reward_cost*, *reward_tech*: Modeled occasionally, mainly as a counterpoint to punishment, or to study carrot and stick together.
- *show_other_summaries*, *show_n_rounds*: Sometimes discussed in connection with information and transparency, not always isolated as distinct design variables.

**Effectively Missing:**  
- None: All 14 prediction dimensions are at least *contextually* present across the literature base, although some are only marginally addressed or with limited sensitivity analysis. Framing variables and presentation details (not core to the mechanics) receive the least direct modeling.

---

# 7) Important Limitations

- **Lack of Empirical Calibration:** All available evidence is theoretical/simulation-based; while diverse, it does not quantify real-world or laboratory effect sizes. Empirical variability and ecological validity cannot be assessed from the present set.
- **Payoff-Behavior Disconnect:** Many studies use behavioral outcomes as proxies for efficiency (e.g., showing increased cooperation rate), but these do not always translate to higher group payoff, especially when punishment is costly or misapplied. Care must be taken not to conflate contribution frequency with efficiency.
- **Potential for Negative or Null Effects:** Some papers (e.g., Handfield et al., 2016; Honjo & Kubo, 2020; Barron & Guo, 2021; Farjam et al., 2015) explicitly show that punishment can reduce efficiency under plausible parameterizations. Not all models agree on downstream effects; context and design details are critical.
- **Complexity and Thresholds:** Efficiency gains are often subject to thresholds or nonlinearities—small parameter or initial state changes can flip the expected effect of punishment from positive to negative due to bistability, coordination issues, or saturation (Liu et al., 2024; Ye et al., 2016).
- **Generalizability Concerns:** Many models rely on stylized PGGs or adjacent games. Results sometimes depend on specific parameterizations (e.g., homogeneous groups, strong selection, absence of noise or antisocial behavior), which may not generalize to all settings.
- **Unmodeled Features:** Practical design dimensions, such as the psychological impact of default framing, round number salience, or identity visibility, are underexplored. The external context (culture, real-world institutions) may alter predictions but is not captured in the modeling base.
- **Reward Mechanisms Less Well Explored:** Although punishment is thoroughly studied, reward mechanisms and their interaction with punishment are less systematically analyzed; thus predictions for systems with both may be less reliable.

---

**Summary:**  
The available theoretical literature robustly supports that enabling effective, well-calibrated punishment substantially increases efficiency in public-goods-game-like environments—*if* the relevant design dimensions (e.g., low punishment cost, high punishment impact, sufficient rounds, appropriate group size, correct institutional arrangement) are favorable and abuse is prevented. The gain is largest when the no-punishment control efficiency is low. However, moderation by cost, institutional context, group structure, and potential for misuse is essential, and in unfavorable or misuse-prone treatments, the efficiency benefit can disappear or reverse.

For prediction, the most direct inferences can be drawn when game designs are closely matched, efficiency is precisely defined and normalized, and the relevant design dimensions are specified. When using outcomes or dimensions only indirectly addressed in the literature, caution and mechanism-based reasoning are required.
