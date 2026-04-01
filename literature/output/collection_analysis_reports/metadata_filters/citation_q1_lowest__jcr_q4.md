# 1) Evidence Base

This literature set is broad in descriptive scope but contains a mix of highly relevant empirical lab experiments and formal theoretical analyses directly targeting public-goods games (PGGs) with punishment, as well as many papers offering only adjacent or indirect evidence. Of the 49 sources, a significant subset (approx. 10–15) provides empirical or theoretical results on PGGs or their close variants with explicit manipulation of punishment and control (no-punishment) conditions, reporting on efficiency or group payoff outcomes. Another substantial subgroup deals with coordination, bargaining, or trust games, or with variants of social dilemmas (e.g., minimum effort, threshold, volunteer’s dilemmas), many with explicit punishment/reward mechanisms, but not exact PGGs. Purely theoretical/commentary papers further contextualize or critique mechanism effects but without new payoff data. Some ethnographic or observational works are included but contribute little direct or quantitative evidence to the prediction task.

Overall, the set is best described as moderately broad for the downstream prediction task: it offers strong, direct evidence for classic stylized lab PGGs with and without punishment, supplemented by a variety of adjacent models and experimental manipulations that highlight nuances and key moderators. However, there are also blind spots in experimental coverage for some game design dimensions and under certain institutional variants.

# 2) Task Relevance

**pgg_or_variant:**
- **Exact relevance:** About 10–12 papers provide direct evidence on PGGs (lab or theory) (e.g., Suleiman & Samid, 2021; Cobo-Reyes et al., 2022; Botta et al., 2021).
- **Close/Adjacent:** Many more focus on closely related social dilemmas (volunteer’s dilemma, minimum effort, threshold games, trust/ultimatum games), varying from 'close' (coordination, surplus-sharing, exclusion as sanction) to 'adjacent' (dyadic trust, real-effort games).
- **Weak/None:** Several papers only offer theoretical or ethnographic context, with no game or only distant analogies.

**punishment_or_sanctions:**
- **Exact relevance:** Many papers (both empirical and theoretical) manipulate the presence/absence and features of punishment (e.g., Suleiman & Samid, 2021; Kanitsar, 2021; Alventosa & Olcina, 2021).
- **Close/Adjacent:** Others discuss rewards, exclusion, replacement, or partner choice as adjacent sanctions. Some discuss punishment only theoretically without implementation or outcome measurement.
- **Weak/None:** A subset (e.g., focused on monitoring, democratic process, or informal norms without punishment) has little to no direct focus.

**efficiency_or_related_payoff_outcome:**
- **Exact relevance:** About 10–15 papers explicitly report efficiency, group payoff, welfare, or total earnings/welfare effects as primary outcomes.
- **Close/Adjacent:** Many others infer efficiency via contributing variables (e.g., increased contributions assumed to raise efficiency, but not measured directly).
- **Weak/None:** Several focus purely on behavioral/psychological/preference measures, norm compliance, or qualitative observation, with little or no reference to payoff data.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes (direct relevance):**
- Efficiency (group earnings as proportion of social optimum)
- Group/individual total payoff, welfare, surplus
- Earnings net of punishment/reward costs

**Non-payoff behavioral outcomes (indirect relevance):**
- Contribution/cooperation rates (common, but not identical to efficiency)
- Punishment/reward assignment frequency or magnitude
- Norm violation, antisocial vs. prosocial punishment
- Voting, group switching, partner exclusion, behavioral “success” (binary group outcome)
- Communication patterns and self-reported perceptions
- Trust, preference or psychological measures

It is crucial to note that, while a majority of empirical works measure both contribution rates and payoffs, a smaller number directly analyze and report efficiency as defined for prediction (ratio of achieved group payoff to full cooperation benchmark).

# 4) Main Findings Relevant To Prediction

**Synthesis of payoff-based findings from exact and close PGGs:**
- **Punishment usually increases efficiency:** Most lab and theoretical papers (e.g., Suleiman & Samid, 2021; Cobo-Reyes et al., 2022; Alventosa & Olcina, 2021; Kanitsar, 2021, for costless punishment; Botta et al., 2021) find that enabling punishment (relative to no-punishment control) increases group efficiency, but the magnitude of the effect is sensitive to (i) punishment cost and effectiveness, (ii) group composition (e.g., 'norm-keepers' vs. strong reciprocators), and (iii) institutional/contextual moderators (e.g., presence of migration, wealth inequality, or group openness).

- **Cost of punishment crucially moderates net efficiency effects:** Where punishment is costly (especially with high cost-to-impact ratios), efficiency gains may be neutralized or reversed—the cost can cancel out the benefit from increased contributions (e.g., Kanitsar, 2021; Calabuig et al., 2024; Herne et al., 2022).

- **Type of punishment (peer vs. institutional):** Centralized (institutional) punishment tends to generate larger efficiency gains than informal/peer punishment, especially in open or migratory groups; formal punishment is more robust (Cobo-Reyes et al., 2022; Alventosa & Olcina, 2021; Ishikawa & Fontanari, 2025).

- **Design feature moderators:** Key design dimensions—such as player count, number of rounds, MPCR, punishment cost and tech, and the possibility of communication or reward—affect the size and direction of the punishment effect.

**Findings from adjacent games or settings:**
- **Coordination/threshold games:** Enabling punishment increases likelihood of reaching payoff-dominant equilibria, especially when punishment is action-based and credible (e.g., Lec et al., 2023; Friehe & Tabbach, 2018; Gueth & Otsubo, 2023).
- **Partner choice/exclusion (adjacent sanctions):** Allowing exclusion can promote cooperation/efficiency, but effects are usually smaller or more transient than with explicit costly punishment.
- **Reward mechanisms:** Rewards can sometimes substitute for or outperform punishment (Peng, 2022), but mixed mechanisms are context-dependent.
- **Psychological/cultural context:** Efficiency gains from punishment depend on group composition (strong reciprocators, antisocial punishers), power symmetry, and cultural context (Suleiman & Samid, 2021; Eldakar et al., 2018).

# 5) Prediction Guidance

- **Prediction anchor:** Where control (no-punishment) efficiency is known and key game design dimensions match (player count, MPCR, punishment cost/tech, reward enabled), the prevailing empirical and theoretical evidence supports predicting *higher* average efficiency in the punishment-enabled treatment, especially for classic lab PGGs.

- **Magnitude estimation:** The size of the improvement is highly variable—moderate on average, but much larger if punishment is cheap, institutionalized, and/or the group contains many strong reciprocators and few norm-keepers (Suleiman & Samid, 2021; Alventosa & Olcina, 2021). Gains are smaller (or can even disappear or reverse) if punishment is costly, ongoing, or leads to frequent antisocial punishment.

- **Group/institutional context:** Prediction is sensitive to group openness (greater gains in open/migratory societies), power symmetry (altruistic vs. selfish punishment), and information structures (transparency increases deterrence).

- **Reward and monitoring:** If reward exists (alone or with punishment), or if there is increased monitoring without sanctions, efficiency effects may differ substantially. Monitoring alone can *reduce* efficiency without formal sanctions (Becchetti et al., 2015). Peer reward may increase efficiency, but only in homogeneous groups or under specific rules.

- **Caveats:** For games with high punishment cost, weak punishment impact, or high antisocial punishment, predicted efficiency change should be small or even negative. Absence of direct payoff data in some studies means that efficiency improvements must sometimes be inferred from contributions, but these are not always reliable proxies.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions (with substantial empirical/theoretical basis):**
- `player_count` (group size): Multiple effects on threshold for high efficiency, stability of cooperation, and punishment effectiveness.
- `num_rounds`: Longer games support higher gains from deterrent punishment; short horizons dampen effect.
- `all_or_nothing` (binary vs. continuous contributions): Most predictions are for standard continuous, but many binary/threshold games are also analyzed.
- `mpcr` (marginal per-capita return): Directly manipulated in both theory and lab studies—critical for incentives and efficiency effect size.
- `punishment_cost`/`punishment_tech`: Extensively manipulated (cost-to-impact, centralized vs. peer).
- `reward_exists`, `reward_cost`, `reward_tech`: Several papers compare or supplement punishment with reward.
- `chat`/`show_n_rounds`/`show_other_summaries`: Some influence (transparency, communication), but less central to payoff outcomes.

**Indirectly informed/contextually discussed:**
- `default_contrib`: Framing defaults are occasionally varied (participation compulsory/optional), but effects are usually inferred rather than measured.
- `show_punishment_id`: Few explicit tests of visibility, but some evidence that punishment observability can moderate deterrence and efficiency (Li et al., 2023; Gueth & Otsubo, 2023).

**Effectively missing or sparsely addressed:**
- Detailed manipulation of `reward_tech` (e.g., number of reward tokens, anonymous assignment).
- Direct tests of the interaction between multiple dimensions (e.g., chat and punishment).
- Systematic exploration of framing (`default_contrib`) and its effect jointly with punishment.
- Explicit manipulation of information structures (`show_n_rounds`, `show_other_summaries`, etc.) to measure indirect effects on efficiency apart from those listed.

# 7) Important Limitations

- **Heterogeneity, context, and composition limitations:** The effect of punishment is highly variable across group compositions (e.g., frequency of strong reciprocators, cultural background) and social context. Without detailed group-level covariates, predictions may be noisy (Suleiman & Samid, 2021).
- **Underreporting of net efficiency:** Some empirical studies focus on contributions, not efficiency net of punishment costs; actual group payoff gains are sometimes overstated or not measured.
- **Adjacency of evidence:** Many studies are on coordination games, bargaining, or volunteer’s dilemmas—closely related but not exact PGGs—so quantitative transferability is limited.
- **Sparse evidence for complex or nonstandard design dimensions:** Some dimensions, such as the effects of punishment/reward identity visibility or contribution framing, are only weakly addressed.
- **Interaction effects less studied:** Effects of enabling multiple mechanisms (e.g., simultaneous reward and punishment, communication with punishment) are rarely analyzed together.
- **Lab context and generalizability:** Much of the directly relevant evidence comes from controlled lab PGGs with university students and stylized monetary stakes; field generalizability may be limited.
- **Insufficient evidence for extreme values:** Few studies systematically vary punishment to (very) high or very low cost/effectiveness, or examine extremely large or small groups.
- **Variability in measurement and reporting:** Inconsistent reporting of efficiency vs. earnings vs. contributions may obscure the true net payoff impact.
- **Lack of direct causal mediation:** Few studies empirically dissect whether efficiency gains arise only through increased contributions or also from changes in payoff structure/accounting.

---

**In summary:**  
The literature robustly supports the prediction that punishment in standard PGGs raises efficiency compared to control, especially when punishment is cheap, effective, and embedded in supportive social/institutional contexts. The prediction is less certain or reversed as punishment costs increase, antisocial punishment appears, or contextual factors intervene. Control (no-punishment) efficiency is a meaningful baseline, but the effect of enabling punishment is moderated by key, often manipulable, design dimensions—those regarding the cost/impact of sanctions, group composition, information structure, and sometimes reward mechanisms. Nevertheless, predictions for less standard parameterizations, for novel institutional hybrids, or for designs with missing experimental evidence, remain speculative or must be treated with caution.
