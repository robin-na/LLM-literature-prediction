# 1) Evidence Base

This paper set is relatively broad for the prediction task, comprising 94 papers with a mix of empirical (notable: several lab experiments) and predominantly theoretical and simulation-based studies. Papers cover a range of environments, including standard and threshold public goods games (PGGs), variants like the snowdrift game and common pool resource dilemmas, as well as adjacent game-theoretic environments such as the repeated prisoner’s dilemma and division-of-labor games. A subset of papers report empirical lab data with direct efficiency measures or related payoffs, while many provide theoretical models exploring parameter sweeps, evolutionary dynamics, and mechanism design.

Most payoff-related findings relevant to treatment-control efficiency changes come from theory or simulation; empirical studies measuring actual group payoffs or efficiency under both punishment-enabled and disabled conditions are fewer but do exist (e.g., Pi et al., 2022; Wang & Huang, 2022). A significant portion of the literature tracks only behavioral outcomes (e.g., contribution rates, cooperation rates, prevalence of cooperation strategies) or focuses on mechanisms and moderators (network structure, heterogeneity, reward presence) without direct efficiency/total payoff measures.

# 2) Task Relevance

**pgg_or_variant:**  
- *Exact relevance* is met by numerous studies implementing standard PGGs or direct variants in both empirical and theoretical frameworks (e.g., Pi et al., 2022; Wang & Huang, 2022; Cong et al., 2016; Sui et al., 2017).  
- *Close relevance* extends to threshold public goods games, snowdrift, and common-pool-resource models (e.g., Kol'veková et al., 2021; Yamamoto & Okada, 2016; Hua & Liu, 2023).
- *Adjacent* or *weak* relevance covers models of partner selection, indirect reciprocity, or other social dilemmas (PDG, division-of-labor) with some shared mechanism but lacking the core PGG payoff structure.

**punishment_or_sanctions:**  
- *Exact relevance* is achieved in studies with peer or institutional punishment as a core intervention, often as a switchable game dimension or with parameterized cost/magnitude (e.g., Pi et al., 2022; Sui et al., 2018; Kol'veková et al., 2021).
- *Close* to *adjacent relevance* includes works on ostracism, social exclusion, or "punishment-like" mechanisms (e.g., reputation exclusion, network rewiring as punishment, meta-norms).
- A nontrivial share are *none* or *weak* on punishment when focusing on reward-only, reputation-based cooperation, or other solution concepts.

**efficiency_or_related_payoff_outcome:**  
- A strong subset of papers provide *exact* efficiency or total group payoff data (often theoretical/simulated), either as primary or secondary outcome (e.g., Kol'veková et al., 2021; Pi et al., 2022).  
- Others provide *close* proxies (group welfare, average payoff, resource levels).
- Many theoretical and simulation works are *adjacent*, using behavioral metrics (cooperation/contribution rates), reporting on “group achievement,” or focusing on conditions for evolutionary abundance but not total payoffs.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes:**  
- *Efficiency*, *total group payoff*, *mean individual payoff*, *group welfare*, and *surplus* directly relate to the prediction task.  
- Several empirical and simulation studies report these measures, allowing direct inferences about changes in efficiency with and without punishment (e.g., Kol'veková et al., 2021; Pi et al., 2022; Zhuang et al., 2012).

**Non-payoff behavioral outcomes:**  
- *Contribution rate*, *cooperation rate*, *frequency of punishing/rewarding actions*, *prevalence of strategies*, and *fraction of successful provisions* are prevalent, especially in evolutionary and agent-based models.
- While increases in cooperation or contribution generally suggest potential for higher efficiency, this mapping is frequently non-monotonic (i.e., high cooperation does not always equal optimal efficiency, especially if punishment is costly or antisocial).

Many papers focus exclusively on behavioral change, not group payoff, so evidence must be carefully filtered for payoff relevance.

# 4) Main Findings Relevant To Prediction

## Synthesis Across Papers

**General pattern:**  
- Enabling peer or institutional punishment in PGG(-like) environments increases efficiency/group payoff relative to control (no punishment) in the majority of reviewed cases (Pi et al., 2022; Wang & Huang, 2022; Sui et al., 2017; Sasaki, 2014; Kol'veková et al., 2021; Zhuang et al., 2012; Powers, 2018).
- The *size* of the efficiency increase, and even its *direction*, are context-dependent, with exceptions arising especially where punishment is costly, poorly targeted, excessive, or produces second-order dilemmas (Quan et al., 2019; Sui et al., 2018; Cong et al., 2016).

**Key moderators and mechanisms:**
- **Punishment cost:** Lower punishment cost generally increases efficiency gains of punishment interventions (Kol'veková et al., 2021; Sui et al., 2017; Kang et al., 2024). If costs are high, efficiency can decrease despite higher cooperation.
- **Punishment network/technology:** Complete versus incomplete or structured punishment networks generate markedly different efficiency outcomes; more potential punishers can dilute effectiveness and reduce efficiency due to bystander effect (Pi et al., 2022).
- **Effectiveness and intensity:** Punishment (and reward) must meet critical thresholds of effectiveness-to-cost ratio to yield efficiency gains (Sui et al., 2017; Sui et al., 2018; Yao & Chen, 2014; Zhuang et al., 2012).
- **Reward presence:** Combined reward and punishment (if both are possible) can outperform either alone in promoting efficiency, but too much of either can reduce gains or destabilize the intervention institution (Cong et al., 2016; Zhuang et al., 2012).
- **Voluntary/optional participation:** Optional participation in conjunction with institutional punishment greatly lowers the threshold for full cooperation and maximum efficiency (Sasaki, 2014; Xia et al., 2011).
- **Group size and MPCR:** Efficiency impact of punishment is moderated by group size and the marginal per capita return—larger groups and higher MPCRs tend to make punishment more favorable (Sui et al., 2017; Kol'veková et al., 2021; Zhuang et al., 2012).
- **Timing and observability:** Punishment impact does not require real-time observability, as long as its possibility is credible (Wang & Huang, 2022).

**Contradictory/conditional evidence:**  
- When punishment is excessive or punishment costs exceed the gains from cooperation, efficiency can decrease relative to control (Quan et al., 2019; Sui et al., 2018; Powers, 2018).
- Theoretical accounts show that reward mechanisms can sometimes outperform punishment for the same cost (Zhuang et al., 2012; Yao & Chen, 2014).

# 5) Prediction Guidance

Based on the reviewed literature:
- **Direction of effect:** In standard and threshold PGGs, the default prediction is that enabling peer punishment—if designed with moderate cost and sufficient effectiveness—will increase group efficiency relative to an otherwise identical control game (Pi et al., 2022; Wang & Huang, 2022; Sui et al., 2017; Kol'veková et al., 2021).
- **Magnitude of effect:** The efficiency gain is variable, typically positive but potentially modest if punishment costs are nontrivial, or, in some configurations, negative (Quan et al., 2019; Sui et al., 2018). Relative gains are more likely (and larger) when the control baseline efficiency is low.
- **Key design dimensions:** For precise prediction, the effects of punishment cost (`punishment_cost`), network technology (`punishment_tech`), group size (`player_count`), number of rounds (`num_rounds`), and marginal per capita return (`mpcr`) must be modeled, as these interact multiplicatively with the efficiency benefit (Pi et al., 2022; Kol'veková et al., 2021; Sui et al., 2017).
- **Punishment structure:** More is not always better—overly permissive or dense punishment networks (everyone can punish everyone) can create bystander dilution and reduce the efficacy and efficiency benefit (Pi et al., 2022).
- **Reward existence:** If rewards are also enabled (`reward_exists`), mixed incentive regimes often outperform pure punishment, but the combined cost of both interventions must be considered (Cong et al., 2016; Zhuang et al., 2012).
- **Indirect evidence:** When using outcomes based on cooperation rates or behavioral change, explicitly acknowledge that such measures often correlate with, but do not guarantee, efficiency improvements, particularly if the cost of punishment is significant.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed (in multiple papers):**
- `player_count` (frequently parameterized; impacts punishment effectiveness and threshold dynamics)
- `num_rounds` (lab experiments and simulations with varying round lengths)
- `mpcr` (key moderator; examined across a spectrum of values)
- `punishment_cost` (centerpiece in nearly all explanatory models)
- `punishment_tech` (network structure, restrictiveness, endogenous/exogenous allocation)
- `reward_exists` (a recurrent moderating factor with several mixed-incentive studies)
- `reward_cost` (included in some models comparing reward and punishment)
- `all_or_nothing` (distinction between threshold and linear PGGs, and within snowdrift variants)

**Indirectly informed or contextually discussed:**
- `chat` (some lab studies include communication and analyze its interaction with punishment, but limited direct comparison)
- `default_contrib` (framing and default effect addressed in select simulation studies)
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id` (occasionally varied; effects on reputation and observability impact, but not systematically linked to efficiency outcomes)

**Effectively missing or only peripherally considered:**
- Some experimental and theoretical works do not provide enough detail on `reward_tech`, exact `punishment_tech`, or observability-related dimensions to allow parameterized prediction.
- The mapping from control efficiency to treatment efficiency (prediction task core) is often available only implicitly, or requires estimation from parameter sweeps and relative outcome reports rather than directly paired experimental outcomes.

# 7) Important Limitations

- **Empirical scarcity:** Direct lab-experimental evidence reporting both control and punishment-enabled efficiency under matched designs is limited, making quantitative predictions less robust than qualitative ones.
- **Payoff outcome reporting:** Many otherwise-rich models report only behavioral outcomes (contribution/cooperation rates), which can diverge substantially from efficiency, especially in costly punishment regimes.
- **Mechanism specificity:** High variety exists in punishment mechanisms (peer vs. institutional, endogenous vs. exogenous, shared vs. individualized, availability of exclusion/ostracism), limiting the transferability of findings across settings (Pi et al., 2022 vs. Kol'veková et al., 2021).
- **Parameter interaction complexity:** Most models reveal nonlinear and sometimes non-monotonic interactions between group size, MPCR, punishment cost, and intervention network; simple linear predictions may underperform.
- **Edge cases:** Under high punishment cost or excessive punishment, efficiency can decrease even as behavioral cooperation increases (Quan et al., 2019; Sui et al., 2018).
- **Control condition variability:** The baseline efficiency (without punishment) is itself highly sensitive to MPCR, group size, and other framing effects, adding uncertainty to the mapping from control to treatment efficiency.
- **Generalizability limits:** Simulations are often based on large or infinite populations, evolutionary updating, or stylized rationality assumptions, which may not match empirical settings or finite-group lab experiments.
- **Sparse evidence:** Some dimensions relevant to the downstream prediction task (e.g., various forms of observability, chat, or fine-grained technological details) are sparsely addressed and often context-specific.

---

**References (selected):**
- Pi, J. X. et al. (2022)
- Kol'veková, G. et al. (2021)
- Wang, C. Q. & Huang, C. C. (2022)
- Sui, X. K. et al. (2017, 2018)
- Cong, R. et al. (2016)
- Powers, S. T. (2018)
- Zhuang, Q. et al. (2012)
- Sasaki, T. (2014)
- Quan, J. et al. (2019)
- Yamamoto, H. & Okada, I. (2016)
- Kang, H. W. et al. (2024)
