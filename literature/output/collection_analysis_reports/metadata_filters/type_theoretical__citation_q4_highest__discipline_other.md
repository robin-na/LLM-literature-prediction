# 1) Evidence Base

The paper set consists entirely of theory or review/theoretical synthesis work, with no new empirical or laboratory experimental studies. The coverage is broad in its engagement with cooperation, punishment, and public-goods-game (PGG)-like environments—including direct treatment of PGGs, as well as broader and adjacent collective action or cooperation models (including trust games, threshold PGGs, climate dilemmas, evolutionary animal behavior, and institutional context). However, only a minority of the papers report findings directly on payoff-related outcomes (i.e., group efficiency or total payoff), and much of the evidence is based on theoretical models, mechanistic arguments, or qualitative synthesis. Overall, the evidence base is moderately broad on the conceptual landscape but fairly limited and indirect in empirical predictive support for the specific downstream task.

# 2) Task Relevance

**pgg_or_variant:**  
- Relevance ranges from `exact` (papers explicitly modeling standard or spatial public goods games) to `adjacent` (papers discussing trust games, threshold games, or environmental collective action).
- About one-third of the papers are `exact` (Kraak, 2011; Zhu et al., 2020; Liu et al., 2019), another set is `close`, and the rest are `adjacent` or `none`.

**punishment_or_sanctions:**  
- Several papers are `exact` on punishment, addressing peer, pool, or institutional punishment (Kraak, 2011; Zhu et al., 2020; Vasconcelos et al., 2013; Cushman, 2015), while others discuss only exclusion (‘punishment=adjacent’) or lack direct focus.
- A subset primarily treat sanctions, while others treat broader institutional or psychological mechanisms without detailed modeling of punishment costs or types.

**efficiency_or_related_payoff_outcome:**  
- Direct evidence (`exact`) on efficiency or group payoff is rare—found in only two papers (Liu et al., 2019; Bicchieri et al., 2004). Several others present only behavioral proxies (cooperation rate, group achievement) or non-payoff outcomes.
- Most findings about payoff efficiency are indirect, mechanistic, or inferred rather than empirically measured.

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes:**
- Efficiency, group payoff, and average payoff are directly reported or modeled in a small subset (Liu et al., 2019; Bicchieri et al., 2004).
- Some papers cite improvements in ‘group achievement’ or ‘collective outcomes’ (Vasconcelos et al., 2013; Kraak, 2011), which are close but not always identical to efficiency as defined in the prediction task.

**Non-Payoff Behavioral Outcomes:**
- The majority of studies focus on cooperation rates, strategy frequencies, norm compliance, or the prevalence of punishment (e.g., Zhu et al., 2020; Dugatkin, 2002; Raihani & Aitken, 2011), which are important but not interchangeable with payoff-based efficiency.
- Several papers acknowledge the distinction, cautioning not to conflate increased cooperation with improved efficiency, especially where punishment incurs costs or retaliation (Kraak, 2011; Cushman, 2015).

# 4) Main Findings Relevant To Prediction

**Effects of Punishment on Efficiency:**
- **Direct Effects:**  
   - Theory and review work (Kraak, 2011; Liu et al., 2019) consistently argues that enabling peer punishment (or exclusion) in PGGs increases cooperation, and, by extension, can increase group efficiency—though the magnitude and durability depend on cost structures, payoff rates, and institutional context.
   - Prosocial pool exclusion can lead to higher or more robust efficiency than punishment, particularly in models with second-order exclusion (Liu et al., 2019).

- **Mechanisms and Moderators:**  
   - Communication (chat), reputation, and transparency further enhance the efficiency gains from punishment by reducing destructive retaliation, focusing sanctions, and stabilizing cooperation (Kraak, 2011; Raihani & Aitken, 2011).
   - Local and group-level punishment is more effective than global, population-level punishment—notably in smaller groups or settings where the risk of failure is salient (Vasconcelos et al., 2013).
   - Efficiency gains are most likely when punishment is peer-driven and institutional legitimacy is high; externally imposed or misunderstood sanctions can backfire (Kraak, 2011; Cushman, 2015).

- **Caveats:**  
   - Retaliatory cycles can erode net payoff despite higher cooperation rates (Cushman, 2015).
   - In threshold and trust games, repetition (longer games) or incremental probability of punishment can substitute for explicit sanctions to some extent (Bicchieri et al., 2004).
   - The effectiveness and efficiency impact of punishment mechanisms may decline as scale, anonymity, and complexity increase, unless sanctions are institutionalized (Jagers et al., 2020).

# 5) Prediction Guidance

- **Directionality:**  
  Enabling peer punishment in public-goods-game-like environments generally increases average efficiency and group payoff compared to punishment-disabled controls, particularly when communication, transparency, and/or peer-driven mechanisms are present (Kraak, 2011; Liu et al., 2019).

- **Magnitude:**  
  The literature provides qualitative, not quantitative, estimates. Control efficiency is a necessary predictor, but adjustments for game structure (e.g., long versus short games, cost/benefit ratios, group size) and presence of communication or reputation features are necessary for more accurate prediction.

- **Dimension-Specific Adjustments:**  
   - High punishment cost, destructive retaliation, or high anonymity may limit or reverse efficiency gains.
   - Pool exclusion often outperforms punishment in maintaining high efficiency but is only directly modeled in one theoretical study (Liu et al., 2019).
   - The addition of chat or mechanisms revealing player actions (i.e., `show_other_summaries`, `show_punishment_id`) is supported as improving the efficacy—and efficiency effect—of punishment mechanisms (Kraak, 2011; Jagers et al., 2020).

- **Limitations of Literature for Quantitative Modeling:**  
  There is insufficient empirical data for parameterizing exact effect sizes or for modeling nuanced interactions among the 14 game design dimensions and baseline control efficiency. Predictions must thus be qualitative or mechanism-based rather than strictly statistical.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- `player_count`, `num_rounds`, `all_or_nothing`, and `mpcr` are common across the major theoretical studies (Kraak, 2011; Zhu et al., 2020; Liu et al., 2019; Bicchieri et al., 2004), with explicit discussion of their effects on the emergence and impact of cooperation, punishment, and efficiency. 
- `punishment_cost` and the specification of `punishment_tech` are considered in several papers, with guidance that lower punishment costs amplify effectiveness but may also increase wasteful or retaliatory punishment.

**Indirectly or Contextually Discussed Dimensions:**
- `chat` (as communication) and mechanisms related to player information (e.g., `show_punishment_id`, `show_other_summaries`) are emphasized as moderators of efficiency impact from punishment (Kraak, 2011; Jagers et al., 2020).
- `reward_exists` and its cost structure are discussed but only as secondary to punishment or in reviews on general cooperation mechanisms (Raihani & Aitken, 2011).

**Sparse or Missing Dimensions:**
- `default_contrib`, `reward_cost`, `reward_tech`, and explicit modeling of `show_n_rounds` are rarely discussed with direct reference to efficiency or only contextually noted.
- `all_or_nothing` is modeled in several theory papers but without direct linkage to empirical efficiency outcomes.
- Very few papers address the specific design or effects of `reward_tech` or `reward_cost` in conjunction with punishment.

# 7) Important Limitations

- **Empirical Thinness:**  
   - The literature set is dominated by theory and synthesis; there are no new or meta-analyzed laboratory datasets providing direct, quantitative estimates of efficiency change from enabling punishment under known baseline (control) conditions.
- **Outcome Ambiguity:**  
   - Many papers focus on cooperation rates or group achievement as proxies for efficiency, with limited discussion of net group payoff or efficiency when accounting for the costs of punishment.
- **Parameter Gaps:**  
   - Several key game design dimensions used for prediction (e.g., `default_contrib`, details of `reward_cost`/`reward_tech`, and player-level summary mechanisms) are largely unaddressed or are embedded within broader mechanism discussions without performance data.
- **Contextual and Scale Limits:**  
   - Papers note that findings from small-group laboratory studies (and their theoretical models) may not generalize to larger-scale, high-anonymity, or high-complexity settings characteristic of real-world commons (Jagers et al., 2020).
- **Retaliation, Legitimacy, and Institutional Context:**  
   - Theoretical work cautions that the positive effects of punishment on efficiency are contingent on legitimacy, the avoidance of costly retaliation cycles, and the institutional design of the sanctioning system (Kraak, 2011; Cushman, 2015).
- **No Direct Quantitative Transfer:**  
   - Due to reliance on theory, generalization, and lack of direct measurement of all design dimensions, predictions about the efficiency effect of punishment in novel game parameter spaces must be made cautiously and with substantial uncertainty.

---

**Summary:**  
The literature set strongly supports the general (theoretical) prediction that enabling peer punishment (especially in combination with chat/reputation mechanisms) improves group efficiency over punishment-disabled controls in PGG-like games, but quantitative, parameter-level guidance is weak. Most design dimensions are only partially or indirectly addressed. Efficiency predictions must therefore lean on mechanism-based reasoning rather than direct empirical effect estimation.
