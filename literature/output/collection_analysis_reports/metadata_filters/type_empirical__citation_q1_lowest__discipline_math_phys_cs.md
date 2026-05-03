# 1) Evidence Base

The supplied paper set consists predominantly of *empirical, laboratory experimental* studies (the vast majority), with a few observational and simulation (MARL or agent-based) experiments. The scope is broad in terms of game structure: it covers canonical public goods games (PGGs), PGG variants (e.g., threshold PGGs, minimum effort/weakest-link, common-pool, team investment), and adjacent environments (Prisoner’s Dilemma (PD), trust/ultimatum games, principal-agent, delegation, and dynamic networked dilemmas). Several studies manipulate or discuss game dimensions crucial for the prediction task, such as group size, rounds, punishment/reward structures, and information conditions.

However, the evidence is distributed unequally across the exact dimensions and outcomes of interest. A subset directly addresses the effect of **enabling peer punishment in PGGs on group efficiency** as defined for the prediction task. Others provide only adjacent, indirect, or behavioral-outcome-based evidence (e.g., changes in contribution rate or norm compliance). There is a strong predominance of *experimental* over *theoretical* or *mechanism-only* papers; explicit theory papers are absent, but several studies include mechanism discussions or micro-theoretical interpretation.

**For the main task (predicting efficiency changes with peer punishment from design/control data in PGGs), the base is moderately broad but uneven:** strong for some design/punishment features in standard PGGs; thinner or more indirect for others and for adjacent domains.

# 2) Task Relevance

## `pgg_or_variant` relevance:
- **Exact relevance:** Many studies use canonical linear PGGs (e.g., Suleiman & Samid 2021; Cobo-Reyes et al. 2022; Peng 2022; Nax et al. 2018; Pancotto et al. 2023).
- **Close/Adjacent relevance:** Substantial number of studies use adjacent dilemmas (PD, weakest-link, threshold PGG, team investment, trust/ultimatum, principal-agent, delegation). These offer mechanism or outcome analogies (e.g., Kanitsar 2021; Lec et al. 2023; Gueth & Otsubo 2023).
- **Weak/None:** Some networked/cooperation studies lack explicit PGG or sanction context.

## `punishment_or_sanctions` relevance:
- **Exact relevance:** A major portion directly manipulates or compares presence/absence, type, or cost/technology of punishment (Suleiman & Samid 2021; Cobo-Reyes et al. 2022; Kanitsar 2021; Yang et al. 2020; Shuvo & Kabir 2024).
- **Adjacent/Weak:** A few only include exclusion/refusal (weak sanctions), norm compliance (survey), or focus on monitoring/information rather than sanctions per se (Becchetti et al. 2015).
- **None:** Studies focused on reward, monitoring, or selection mechanisms without any punishment condition.

## `efficiency_or_related_payoff_outcome` relevance:
- **Exact:** Several studies measure group efficiency as total payoff relative to maximum possible, or directly analyze surplus/welfare (Suleiman & Samid 2021; Cobo-Reyes et al. 2022; Peng 2022; Kanitsar 2021).
- **Close/Adjacent:** Several report on net benefits, total earnings, or final wealth as proxies (Shuvo & Kabir 2024; Zhao et al. 2018).
- **Weak:** Some focus mainly on behavioral or contribution outcomes, mentioning payoffs only in passing.
- **None:** Papers limited to cooperation rates, punishment frequencies, or attitudinal data.

**Summary:**  
The literature is *strong* for direct experimental evidence on punishment effects in PGGs, but weaker for settings with highly non-standard designs, for adjacent game classes, and where efficiency is not the primary/explicit outcome.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes (`efficiency` as defined, group payoff, total earnings, welfare, etc.):**  
  Explicitly measured in a subset of studies, especially those focusing on payoffs from PGGs with and without punishment or reward mechanisms (Suleiman & Samid 2021; Cobo-Reyes et al. 2022; Peng 2022; Kanitsar 2021; Lec et al. 2023; Gueth & Otsubo 2023).
- **Proxy Payoff Outcomes:**  
  Total welfare, surplus, or final wealth in some adjacent experiments (e.g., Shuvo & Kabir 2024; Di Guida et al. 2021).
- **Non-Payoff Behavioral Outcomes:**  
  Most studies (even many that mention payoffs) place primary weight on cooperation/contribution rate, punishment frequency, norm compliance, or governance preferences. In such cases, payoff or efficiency is, at best, discussed as a secondary consequence or inferred (Yang et al. 2020; Pancotto et al. 2023).
- **No payoff/efficiency reporting:**  
  A minority of studies focus strictly on behavioral attitudes, sanctioning propensity, or dynamics of selection/cooperation, with no efficiency/payoff data at all.

*Important distinction:* Many studies reporting increased cooperation or contribution with punishment do not always show increased efficiency – the net effect depends on the costliness and application of punishment.

# 4) Main Findings Relevant To Prediction

- **Peer punishment in canonical PGGs generally increases average efficiency relative to control (no-punishment),** but the magnitude varies by game design and social context. The largest and most reliable efficiency gains are observed with strong reciprocators and low 'norm-keeper' prevalence (Suleiman & Samid 2021).
- **Formal/centralized punishment outperforms informal/peer punishment in open societies** with migration or membership turnover; in closed groups, informal sanctions can be equally efficient if initial cooperation is high (Cobo-Reyes et al. 2022).
- **Cost and effectiveness of punishment (punishment cost, tech/multiplier):**  
  - **Low-cost or costless punishment yields more substantial efficiency gains; costly punishment often erodes or eliminates net benefits.** In some cases, enabling punishment can even lower efficiency relative to control (Kanitsar 2021; Herne et al. 2022; Calabuig et al. 2024).
  - **Punishment size relative to cost (the fine-to-cost ratio) is crucial.**
- **Network structure and population context are key moderators.**  
  - *Dense public good sanction networks:* punishment increases efficiency.  
  - *Sparse/generalized exchange networks:* punishment has little or no positive effect (Kanitsar 2021).
- **Non-peer (e.g., automatic, centralized, low-magnitude) punishment can sometimes be ineffective or strictly efficiency-reducing,** especially if its impact is not deterrent (Yang et al. 2020).
- **In adjacent games:**  
  - Punishment may increase cooperation, but the cost of punishment can offset or even outweigh welfare gains.  
  - Coordination/weakest-link games sometimes yield greater efficiency gains from punishment as a coordination device, provided the cost is not prohibitive.
- **Social information and observability:**  
  - The presence, visibility, and identification of punishment signals can enhance the deterrent effect and promote efficiency (Li et al. 2023; Gueth & Otsubo 2023).  
  - Conversely, monitoring alone (without sanctions) may decrease efficiency in low social capital settings (Becchetti et al. 2015).
- **Variance and heterogeneity:**  
  Efficiency effects can be highly variable across groups/societies, depending on both player type composition and punishment norms (Suleiman & Samid 2021). Allowing for endogenous matchings or repeated interactions tends to increase variance without reliably increasing average efficiency (Di Guida et al. 2021).
- **Reward mechanisms (in absence of punishment):** Majority-vote reward increases efficiency robustly, especially in heterogeneous groups; peer reward may help only in homogeneous ones (Peng 2022).

# 5) Prediction Guidance

- **If the control efficiency is known for a standard PGG, enabling peer punishment is reliably expected to increase average efficiency, but this is moderated by punishment cost, punishment effectiveness, group structure, and social context** (Suleiman & Samid 2021; Kanitsar 2021).
    - *Direct experimental evidence* supports positive efficiency effects for peer punishment under standard parameterizations (n=3-5, 1:3 cost-effect ratios, MPCR .3-.5).
    - *If punishment is costly and/or applied inefficiently (e.g., norm-keepers punish both high and low contributors, or punishment is common but not well-targeted),* efficiency gains may be negligible or even negative.
- **Design dimensions that substantially moderate the effect:**
    - **Punishment cost and fine-to-cost ratio:** Lower cost-to-fine ratios yield larger, more reliable gains.
    - **Player count and group openness:** Larger or open groups (migration, endogenous formation) tend to benefit more from formal punishment, but informal peer punishment may be fragile under these conditions (Cobo-Reyes et al. 2022).
    - **Number of rounds:** Sufficiently repeated interaction is crucial, but the effect can attenuate if groups do not successfully learn or if antisocial punishment emerges.
    - **Chat/communication:** Rarely directly manipulated alongside punishment; evidence is sparse.
    - **Information structure (punishment id, other outcomes shown):** Observability and visibility of punishment actions can enhance positive effects.
    - **Other moderators:** Institutional context for norm coordination (e.g., grievance procedures) can shift the effect from negative to positive (Macleod et al. 2025).
- **Adjacent-game evidence (minimum effort, coordination, team investment) highlights that punishment can facilitate efficient coordination,** but only if costs do not overwhelm the benefits, and only for some structures.
- **Behavioral outcome increases (cooperation rate, contributions) are necessary but not sufficient for gains in efficiency:** The net resource destroyed in punishment must not offset the gains from increased contributions.
- **Control-game efficiency is a partial predictor:** The marginal effect of enabling punishment depends critically on design features (especially cost/benefit of punishment) and social structure. It cannot be assumed to be additive (Kanitsar 2021; Macleod et al. 2025).

# 6) Design Dimensions Highlighted Across Papers

### **Directly informed by payoffs in punishment-enabled and control conditions:**
- **player_count:** Reported in nearly all studies; evidence for standard sizes (3-8).
- **num_rounds:** Commonly included and often linked to the decay/evolution of punishment's effect.
- **mpcr:** Explicitly stated in exact-relevance studies; robust findings for common values (e.g., 0.3-0.5).
- **punishment_cost/punishment_tech:** Most core studies report and manipulate these directly (critical for payoff outcomes).
- **all_or_nothing:** Both continuous and binary designs are present; evidence from threshold/all-or-nothing and from continuous PGGs.
- **chat:** Rare as a co-variate with punishment; impact only contextually discussed.
- **show_n_rounds, show_other_summaries, show_punishment_id:** Sometimes included, mainly as context. Observability of punishment or rewards is highlighted in some adjacent studies (Li et al. 2023; Gueth & Otsubo 2023).
- **reward_exists/reward_tech/reward_cost:** Directly tested only in a few studies (Peng 2022, where majority-vote reward is the focus).
- **default_contrib:** Framing (opt-in/opt-out) is specified in some, but its effect is sparsely tested.
- **punishment_magnitude:** Closely related to cost/tech; when specified, included under punishment technology.
- **punishment_exists:** Central in all relevant studies; the core treatment condition.

### **Dimensions missing, sparsely covered, or only discussed contextually:**
- **chat:** Only some evidence. Co-impact with punishment not experimentally tested.
- **default_contrib:** Very limited experimental variation.
- **show_other_summaries, show_n_rounds, show_punishment_id:** Often included for context, rarely manipulated.
- **reward dimensions:** Most studies do not include reward treatments alongside punishment.
- **Dynamic selection/social network structure:** In some adjacent/variant studies, but rarely specified within the canonical PGG context.

# 7) Important Limitations

- **Not all studies report efficiency/payoff outcomes directly;** many report only on behavioral outcomes (cooperation, contributions, punishment rates), requiring inference or caution when mapping to payoff consequences.
- **Ambiguous or inconsistent findings in adjacent or noncanonical game environments:** In some asymmetric, team, or dynamic network settings, enabling punishment does *not* increase (and may decrease) efficiency, especially when punishment is costly or misapplied (Kanitsar 2021; Herne et al. 2022; Calabuig et al. 2024).
- **Generalizability:** Most evidence comes from small, homogeneous lab groups; context (cultural, institutional, participant pool) can substantially moderate punishment effectiveness (Suleiman & Samid 2021; Cobo-Reyes et al. 2022).
- **Complex interaction effects between design dimensions:** Few studies systematically vary multiple dimensions (e.g., punishment cost, group size, MPCR) within a single experiment, limiting the ability to estimate their joint effects.
- **Sparse evidence for some design variables (chat, visibility of punishment/reward decisions, default contributions):** These dimensions are often present but not systematically manipulated.
- **Control efficiency is not always reported or is inferred from contribution data, reducing precision for the main prediction task.**
- **Rewards and punishment often not jointly manipulated:** Limited evidence on their interaction or relative/combined effects.
- **Antisocial or misdirected punishment can sometimes reduce efficiency, making group composition and norm structure important unexplained moderators.**
- **Adjacent and nonstandard games:** Substantial amount of adjacent literature (coordination, team, delegation, principal-agent) provides only partial guidance and may not cleanly generalize.
- **Variance across groups:** Even when average effects are found, within-treatment variance is large, especially relating to the composition and behavior of participant groups and societies.

---

### In summary

- **Best-supported design dimensions for prediction** include player_count, num_rounds, mpcr, punishment_cost, punishment_tech, all_or_nothing, and (to a lesser degree) information visibility and openness/closure of the group.
- **Most studies support the conclusion that enabling peer punishment in canonical PGGs raises efficiency over the control, but the magnitude and even sign depends on implementation details (especially cost-effectiveness of punishment), social context, and group composition.**
- **Predictive models should avoid extrapolating outside experimentally-supported regions; for designs with high punishment cost, non-peer/automatic punishment, strong norm-keeping behavior, or unusual social structures, positive efficiency effects cannot be assumed.**
- **Careful attention must be paid to distinguish behavioral cooperation from actual efficiency effects, as the latter depend on net resource flow after including the cost of punishment.**
