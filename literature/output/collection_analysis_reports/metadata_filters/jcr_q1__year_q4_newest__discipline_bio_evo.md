# 1) Evidence Base

The paper set comprises 35 papers with a balanced mix of empirical (mainly laboratory experiments in economics or psychology) and theoretical studies (formal models, computational simulations, agent-based models). It is moderately broad in scope, including works on public goods games (PGGs) and a wide range of adjacent or structurally similar games (e.g., common-pool-resource (CPR) games, networked trust games, collective-risk dilemmas, repeated dyadic games). Some papers are only contextually related, offering conceptual frameworks or cross-societal context but lacking direct experimental or payoff data.

About a quarter of the papers provide *direct and exact* evidence for the core prediction task: the impact of enabling punishment on group efficiency in PGG-like environments. Another set provide *close* evidence through variants of PGGs, especially CPR games and collective-risk dilemmas. Many also discuss non-payoff behavioral outcomes or address only the motivational, psychological, or sociocultural context of sanctions, with little empirical link to efficiency.

In summary, while the set includes some highly relevant empirical and theoretical works, it is not exhaustive for every conceivable game design dimension and is less informative for games that diverge from standard PGG or CPR paradigms.

# 2) Task Relevance

**pgg_or_variant:**  
- **Exact:** Several papers directly study standard PGGs with punishment (e.g., Powers et al., 2023; Nhim et al., 2023).
- **Close:** Many focus on CPR games, collective-risk dilemmas, threshold or resource-based PGGs, repeated dyadic games with similar social dilemmas structure (e.g., Xu et al., 2022; Wang et al., 2024; Grimalda et al., 2022).
- **Adjacent:** Others address structurally similar or evolutionary models, networked trust games, or theoretical accounts of sanctioning (e.g., Yaman et al., 2023; Batistoni et al., 2022).
- **Weak/None:** Some papers only mention PGGs or public goods in passing or as high-level context.

**punishment_or_sanctions:**  
- **Exact:** Papers with implemented peer or institutional punishment mechanisms, especially as a treatment variable against a control condition (e.g., Powers et al., 2023; Nhim et al., 2023; Grimalda et al., 2022).
- **Close:** Works using fines, taxation, or rewards in analogous resource management or cooperation games.
- **Adjacent:** Studies addressing indirect punishment (partner choice, social exclusion) or punitive-like behaviors (e.g., retaliation, destruction, emotion-driven responses).
- **Weak/None:** Papers focused on related cooperation mechanisms without any punishment or sanctioning.

**efficiency_or_related_payoff_outcome:**  
- **Exact:** Studies explicitly measuring group efficiency, welfare, or total payoff relative to a social optimum (e.g., Nhim et al., 2023; Powers et al., 2023; Wang et al., 2024).
- **Close:** Outcomes such as group welfare (in resource games) or disaster avoidance (collective-risk dilemmas) that strongly correlate with efficiency but may not be strictly equivalent.
- **Adjacent:** Behavioral outcomes (cooperation/contribution rates, punishment frequency) with only inferred or unquantified links to efficiency.
- **Weak/None:** Papers limited to attitudinal, neural, or reputational outcomes with no direct mapping to efficiency.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes:**
- *Efficiency* (as group payoff divided by possible maximum): Directly measured in only a handful of experimental and theoretical papers (Powers et al., 2023; Nhim et al., 2023; Wang et al., 2024).
- *Group payoff, welfare, surplus, or disaster avoidance* (e.g., in collective-risk or CPR games): Reported in several studies but with varying fidelity in mapping to efficiency.
- *Dynamic payoff metrics* (e.g., bistability, payoff trajectories): Present in some theory papers with resource feedbacks or evolutionary game settings.

**Non-payoff behavioral outcomes:**
- *Contribution or cooperation rates:* Ubiquitous across the literature, often the primary metric for sanctioning impact (e.g., Xu et al., 2022).
- *Punishment frequency, mode, or target selection; norm compliance; partner choice; trust/reputation signals:* Examined especially in adjacent and theoretical/psychological works.
- *Neural or emotional correlates* (e.g., inter-brain synchronization, mood impacts): Present in some experimental papers, but not related to efficiency.

**Distinction:**  
Most studies in the set distinguish behavioral mechanisms (cooperation rate, compliance, punishment behavior) from group efficiency or overall monetary welfare. Very few studies bridge this with direct data on both, highlighting a key gap.

# 4) Main Findings Relevant To Prediction

## (a) Papers Directly Measuring Efficiency Effects
- **Punishment often increases behavioral cooperation but does NOT universally increase efficiency.** The costs of monitoring, enforcement, and sanctioning can outweigh the benefits of increased contributions, especially with high punishment costs or strict enforcement (Nhim et al., 2023; Grimalda et al., 2022).
- **Tax or minimum-contribution regimes may boost both contributions and efficiency,** while costly direct punishment may only boost contributions but reduce or leave efficiency unchanged—due to punishment’s resource drain (Nhim et al., 2023; Wang et al., 2024).
- **Efficiency effects of punishment are strongly context-dependent:** Group size, the institutional mode of punishment (peer vs. centralized), the cost structure, and the baseline level of cooperation (control efficiency) are powerful moderators (Powers et al., 2023; Nhim et al., 2023; Wang et al., 2024).

## (b) Theory and Close-variant Empirical Findings
- **Evolutionary and agent-based models suggest optimal punishment 'levels':** Over-punishment is wasteful, under-punishment fails to deter defectors. Effective institutional design is key to maximizing efficiency (Powers et al., 2023).
- **Resource dynamics can dominate punishment effects:** In games where group welfare depends on resource growth or threshold effects (e.g., CPRs, collective-risk games), punishment only increases efficiency when the resource or risk structure allows it (Wang et al., 2024; Grimalda et al., 2022).
- **In voluntary or opt-in games, punishment may have little efficiency effect:** If avoidance of punishment is possible, efficiency does not reliably rise with punishment-enabled treatments (Del Ponte et al., 2025).

## (c) Indirect and Behavioral Outcome Findings
- **Increases in cooperation rates typically—but not always—imply increased efficiency.** Mapping is not always direct; the cost of punishment, reward, or other institutions may erode net group benefit (Xu et al., 2022; Odouard et al., 2023).
- **Norms, institutional design, and group structure are key:** Sanctioning works best with proper norm internalization and enforcement, while institutional trustworthiness and group hierarchy can mediate or even reverse effects (Odouard et al., 2023; Spadaro et al., 2023).

# 5) Prediction Guidance

- **Use direct effect estimates (when available) from game designs most similar to the prediction query.** If the paper reports the change in group efficiency when punishment is enabled—net of punishment costs—this is the most reliable evidence.
- **Control efficiency (of the punishment-disabled game) is a strong predictor of treatment efficiency—*the higher the baseline, the smaller the absolute efficiency effect of punishment*.** When baseline cooperation (and thus efficiency) is high, introducing punishment has weaker or even negative efficiency effects (especially if punishment is costly) (Grimalda et al., 2022; Nhim et al., 2023).
- **Examine punishment cost and implementation details:** High punishment costs, decentralized/voluntary enforcement, or structures allowing avoidance of sanctions generally decrease or negate the efficiency gains of punishment (Del Ponte et al., 2025; Nhim et al., 2023).
- **Specific game design dimensions interact:** Group size (player_count), marginal per-capita return (mpcr), punishment cost, and institutional centralization all directly moderate the effect size—e.g., larger groups or higher mpcr often make efficient cooperation harder, increasing the potential value of punishment (Wang et al., 2024; Powers et al., 2023).
- **Indirect evidence can guide qualitative expectations when direct data are missing:** For instance, in resource management games or repeated interactions where punishment is possible but not institutionally enforced, efficiency may only rise if defection is truly deterred and costs are not prohibitive (Xu et al., 2022; Wang et al., 2024).
- **Beware the cost-compensation trap:** If punishment significantly boosts cooperation but is resource-consuming, efficiency may be flat or even decline—direct measurement is necessary (Nhim et al., 2023; Grimalda et al., 2022).

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- **player_count**: Group size effects on cooperation and efficiency are addressed in both empirical and theory papers (Powers et al., 2023; Nhim et al., 2023; Wang et al., 2024; Xu et al., 2022).
- **num_rounds**: Game length is varied in several experiments and models, especially regarding the evolution of cooperation or persistence of effects (Xu et al., 2022; Odouard et al., 2023).
- **mpcr**: Core in experimental and theoretical work, especially regarding benefit-to-cost ratios and their interaction with punishment effectiveness (Powers et al., 2023; Xu et al., 2022).
- **punishment_cost & punishment_tech**: Multiple papers directly vary or model the cost and technological implementation of punishment (Nhim et al., 2023; Powers et al., 2023; Grimalda et al., 2022; Wang et al., 2024; Yaman et al., 2023).
- **reward_exists**: Some studies include reward stages/mechanisms as alternatives or complements to punishment (Wang et al., 2024; Yaman et al., 2023).
- **all_or_nothing, default_contrib**: Included in several experimental designs and models (Nhim et al., 2023; Odouard et al., 2023; Del Ponte et al., 2025).
- **chat**: Examined in relation to communication effects on cooperation, though less often tied to efficiency outcomes (Nhim et al., 2023; Xu et al., 2022).
- **show_other_summaries, show_n_rounds**: Manipulated in some experimental protocols, with possible (but typically indirect) effects on contributions and norms (Odouard et al., 2023; Morsky et al., 2024).

**Indirectly or sparsely informed dimensions:**
- **reward_cost, reward_tech, reward_magnitude**: Present but less systematically varied or analyzed across the set; focus falls on punishment mechanisms.
- **show_punishment_id (identity of punishers shown)**: Rarely directly manipulated; disciplinary transparency or anonymity is contextually discussed (e.g., Spadaro et al., 2023).
- **default_contrib**: Examined in some experimental frames but with less focus on efficiency effects (Del Ponte et al., 2025).
- **punishment_magnitude**: Sometimes conflated with cost or bundled in ‘cost/benefit’ ratios; explicit systematic studies are fewer.

**Missing or only contextually discussed:**
- Many dimensions (especially those relating to interface features or participant feedback) are not directly studied in most papers, meaning their role in efficiency change with punishment is uncertain from this set.

# 7) Important Limitations

- **Sparse direct empirical evidence on efficiency increases:** Though contributions and cooperation rise under punishment in many designs, few studies explicitly report net group efficiency after accounting for punishment costs.
- **Baseline (control) efficiency effects are underexplored:** Most studies do not systematically test how the initial efficiency level moderates the effect of introducing punishment.
- **Generalizability is limited:** Many results arise from lab experiments with narrow parameter ranges (e.g., small groups, short games), making transfer to other group sizes or institutional settings uncertain.
- **Heterogeneity of ‘punishment’ mechanisms:** Ranges from centralized taxes to peer-sanctioning and even indirect mechanisms; these differences crucially affect efficiency outcomes and are not always comparable.
- **Theory-practice and outcome gaps:** Several prominent theory papers provide detailed predictions for specific mechanisms, but are not always matched by empirical measurement of efficiency or realization in actual games.
- **Non-payoff outcome measurement predominates:** Many works use behavioral proxies that may not map straightforwardly to efficiency, especially if the cost of enforcement is high.
- **Game design dimension gaps:** Some key prediction variables (e.g., identity transparency, reward cost/magnitude, show_punishment_id) are seldom directly manipulated or reported, limiting precision for those comparing across full design spaces.
- **Ambiguity in mapping behavioral outcomes to efficiency:** When only contributions or cooperation rates are reported, the conversion to efficiency is context-dependent and can be misleading if punishment is costly or coordination fails.

---

## **Summary Table: Prediction Guidance on Efficiency Effects from Paper Set**

| Design Dimension             | Direct Evidence | Implication for Efficiency Change When Punishment Enabled        |
|------------------------------|----------------|----------------------------------------------------------------|
| player_count                 | Yes            | Larger groups amplify the need and effect of institutionalized punishment; risk of inefficiency without hierarchy (Powers et al., 2023). |
| num_rounds                   | Moderate       | More rounds can increase the payoff of punishing (deterrence); effect is context-dependent. |
| mpcr                         | Yes            | Intermediate mpcr has the greatest variance in punishment effectiveness (Odouard et al., 2023; Powers et al., 2023). |
| all_or_nothing               | Moderate       | All-or-nothing rules can interact with punishment by making norms and deviations clearer (Nhim et al., 2023). |
| chat                         | Indirect       | Communication can increase baseline efficiency, thus diminishing punishment’s marginal effect. |
| default_contrib              | Weak           | Framing effects may impact initial contributions but efficiency effect is unclear.           |
| punishment_cost              | Yes            | High punishment cost reduces or reverses efficiency gains from increased cooperation (Nhim et al., 2023; Grimalda et al., 2022). |
| punishment_tech              | Moderate       | Centralized (tax/fine) settings may allow gains in efficiency if well-designed (Wang et al., 2024). |
| show_n_rounds                | Weak           | Relevance to efficiency is indirect.                                                         |
| show_other_summaries         | Indirect       | Peer comparisons can interact with norm enforcement but efficiency linkage is not always direct. |
| show_punishment_id           | Weak           | Transparency may affect norm enforcement but empirical tie to efficiency is limited.         |
| reward_exists (and reward variables) | Moderate       | Rewards can substitute for or complement punishment; can increase efficiency but sometimes at equal or higher cost (Wang et al., 2024). |
| punishment_magnitude         | Moderate       | Needs to be high enough to deter but not so high as to waste resources; many studies confound cost with magnitude. |

## **Conclusion**
The literature set supports the cautious prediction that *enabling punishment in PGG-like environments often increases cooperation but does not reliably increase average efficiency*. The efficiency gain depends crucially on baseline efficiency, the cost and structure of punishment, group size, and whether the institutional arrangement minimizes punishment costs relative to created cooperation benefits. Absence of direct payoff results, variable mapping from behavioral to efficiency outcomes, and limited coverage of some design dimensions mean predictions remain approximate, especially for combinations not directly tested in the papers. Careful consideration of context, cost structures, and baseline rates is essential when projecting efficiency changes from punishment-enabled treatments.
