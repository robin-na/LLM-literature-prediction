# 1) Evidence Base

The evidence base consists of 17 papers, featuring a balance of experimental/empirical (lab experiment) and theoretical works. The empirical contributions primarily employ laboratory public goods, trust, or coordination games with variant institutional features, while theoretical papers span models of cooperation, punishment, social contract, and related dilemmas. The collection is broad in conceptual scope, encompassing both direct public goods games (PGG) and adjacent settings (trust games, minimum effort, donation, and shirker’s dilemmas). For the downstream prediction task—inferring treatment efficiency when peer punishment is enabled—coverage is variable. Several papers provide *exact* or *close* empirical evidence in public goods game contexts, including direct measurements of efficiency or closely related group payoffs. Others address adjacent designs or focus on behavioral outcomes (cooperation, contribution rates) with only indirect bearing on group efficiency. A subset of papers focus solely on theory or mechanism without new data. Overall, the set is broad in design, but direct empirical evidence for payoff-based efficiency outcomes in PGGs with peer punishment is limited relative to the overall number of papers.

---

# 2) Task Relevance

**pgg_or_variant:**  
- *Exact relevance:* Around one third of the papers provide *exact* evidence on classic public goods games (e.g., Cobo-Reyes et al., 2022; Pancotto et al., 2023; Peng, 2022).  
- *Close relevance:* Several papers employ variants such as minimum effort, team investment, or repeated Prisoner’s Dilemma (e.g., Lec et al., 2023; Gioffré & Tampieri, 2025) or review findings from PGGs (Zhang & Pei, 2022).
- *Adjacent/weak relevance:* Some papers address trust, delegation, or coordination games—relevant for general mechanisms but not structurally equivalent to PGGs (e.g., Herne et al., 2022; Calabuig et al., 2024).

**punishment_or_sanctions:**  
- *Exact relevance:* Many papers center on punishment or sanctioning, including both endogenous (peer) and institutional forms (Cobo-Reyes et al., 2022; Ishikawa & Fontanari, 2025).  
- *Close relevance:* Some study adjacent or hybrid punishment, like third-party sanctions or walk-away partner choice.
- *Adjacent/none:* A few focus exclusively on rewards (Peng, 2022) or address sanctions only as a baseline comparison.

**efficiency_or_related_payoff_outcome:**  
- *Exact relevance:* Direct measurement or reporting of efficiency or group payoff are present in about half of the papers, including empirical and theoretical studies (Cobo-Reyes et al., 2022; Lec et al., 2023; Gioffré & Tampieri, 2025).
- *Close/adjacent relevance:* Some papers infer efficiency from contribution data (Pancotto et al., 2023) or analyze conditions promoting cooperation, assuming a link to efficiency.
- *Weak/none:* Several focus on behavioral measures (contributions, cooperation rates) without payoff accounting (Zhang & Pei, 2022; Dato & Friehe, 2025), or only discuss efficiency contextually.

---

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes:**  
- *Direct reporting of efficiency or total group payoffs* appears in empirical studies such as Cobo-Reyes et al. (2022), Lec et al. (2023), Herne et al. (2022), and Calabuig et al. (2024), as well as theoretically in Ishikawa & Fontanari (2025), Gioffré & Tampieri (2025), and Uchida et al. (2024). Efficiency is sometimes defined as mean individual or group payoff, occasionally normalized to the cooperative optimum.
- *Indirectly inferred efficiency/payoff* is present in studies where only contributions or investments are reported (Pancotto et al., 2023), with inferences made based on the structure of payoffs.
- *Related payoff variables* such as welfare, surplus, or aggregate coins generated are sometimes used interchangeably with efficiency.

**Non-payoff behavioral outcomes:**  
- *Contribution rate, cooperation frequency, and punishment/reward assignment* are common, especially in studies synthesizing theoretical mechanisms (Zhang & Pei, 2022) or measuring behavioral reactions (Dato & Friehe, 2025; Bellucci, 2022).
- *Norm compliance, trust dynamics, or intentions* are often measured but are not payoff-based and must be distinguished (e.g., Li et al., 2023; Dato & Friehe, 2025).

Overall, about half the relevant studies provide outcome measures suitable for the prediction task (treatment efficiency with punishment), while the remainder focus on behavioral or adjacent outcomes.

---

# 4) Main Findings Relevant To Prediction

Synthesizing across papers:

- **Punishment increases efficiency when properly designed:**  
  Several *exact* and *close* studies show that enabling punishment (especially institutional/centralized) can significantly increase group efficiency, especially if punishment costs are low and the punishment is salient, credible, and well targeted (Cobo-Reyes et al., 2022; Ishikawa & Fontanari, 2025; Lec et al., 2023; Uchida et al., 2024; Gioffré & Tampieri, 2025). Cost-sharing among punishers or strong deterrence (either by high fines or high perceived risk) expands the parameter space for efficient equilibria.

- **Punishment can reduce efficiency if costs are high or use is excessive:**  
  Peer punishment with significant cost—especially when not restrained or subject to second-order free-riding or anti-social use—can lead to net efficiency losses, even if cooperation rates increase, due to the destruction of value via costly sanctions (Zhang & Pei, 2022; Herne et al., 2022; Calabuig et al., 2024). In some settings, efficiency is maximized in the *no-punishment* baseline.

- **Effect depends on context and moderators:**  
  Key moderators include:
  - **Group openness/migration:** Punishment is more effective in open groups (with migration/exit) (Cobo-Reyes et al., 2022).
  - **Type of punishment (peer vs institutional):** Institutional punishment is more robust/effective than peer punishment (Cobo-Reyes et al., 2022; Ishikawa & Fontanari, 2025).
  - **Cost-to-benefit ratio (MPCR in PGGs):** Higher returns to cooperation (high MPCR) and lower punishment cost increase the likelihood that efficiency improves with punishment (Gioffré & Tampieri, 2025; Ishikawa & Fontanari, 2025; Uchida et al., 2024).
  - **Game repetition:** Multi-round/repeated interactions favor efficiency gains with punishment, as deterrence or coordination emerges over time (Lec et al., 2023; Gioffré & Tampieri, 2025).
  - **Observability and precommitment:** Observable and pre-announced punishment schedules enhance efficiency by guiding expectations (Gueth & Otsubo, 2023; Li et al., 2023).
  - **Reward mechanisms:** When examined, majority-vote rewards can increase efficiency (Peng, 2022), but the literature does not robustly address how rewards interact with co-present punishment.

- **Ambiguities/disagreement:**  
  Some papers suggest peer punishment can *lower* efficiency even as it raises cooperation, due to costs and possible misuse (Zhang & Pei, 2022; Calabuig et al., 2024; Herne et al., 2022). Others indicate long-run net efficiency gains, especially in repeated games or when punishment is applied judiciously (Lec et al., 2023; Uchida et al., 2024).

- **Payoff vs behavior:**  
  Efficiency gains are not always aligned with cooperation gains; some settings show more frequent punishment raises contributions, but net earnings may not improve or may worsen (Herne et al., 2022; Zhang & Pei, 2022; Calabuig et al., 2024). Some positive results for efficiency depend on long-run coordination, not initial rounds (Lec et al., 2023).

---

# 5) Prediction Guidance

**How to use findings for prediction:**

- **Prioritize punishment details:** Predictions of treatment efficiency must account for the cost, efficacy, and institutional structure of punishment; low-cost, high-effectiveness, well-coordinated punishment is more likely to raise efficiency above control (Ishikawa & Fontanari, 2025; Cobo-Reyes et al., 2022).
- **Control game efficiency as a baseline:** If control (no-punishment) efficiency is high, introducing punishment can reduce efficiency through costs if little increase in cooperation is possible. If control efficiency is low, enabling punishment is more likely to increase both cooperation and efficiency, with the effect size shaped by cost/benefit ratios and behavioral response (Gioffré & Tampieri, 2025; Lec et al., 2023).
- **Contextual moderators:** Consider group openness (migration/exit), game repetition, and observability of punishment as positive moderators for efficiency gains (Cobo-Reyes et al., 2022; Gueth & Otsubo, 2023). Peer punishment in small, short games with high cost is less likely to improve efficiency (Herne et al., 2022; Calabuig et al., 2024).
- **Behavioral outcomes as indirect signals:** Where efficiency is missing but contribution/cooperation effects are strong, cautiously infer directionality for efficiency, but downweight the prediction, as payoff destruction via punishment can offset cooperation gains (Zhang & Pei, 2022; Pancotto et al., 2023).
- **Ambiguity and disagreement:** Be alert to settings (e.g., high-cost, indiscriminate, or antisocial punishment; binary-action, asymmetric games) where efficiency gains do not track increases in cooperation or contributions.

In summary, literature-supported prediction requires mapping the control-game efficiency, institutional features, and costs of punishment to the empirically supported parameter regions in the literature. In some cases, enabling punishment will improve efficiency; in others, particularly with uncoordinated, costly, or high-frequency peer punishment, efficiency may decline or remain unchanged.

---

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions:**
- `player_count`: Frequently varied and explicitly analyzed for its effects (Cobo-Reyes et al., 2022; Ishikawa & Fontanari, 2025; Pena et al., 2024).
- `num_rounds`: Experimentally manipulated and shown to moderate punishment effectiveness and coordination (Lec et al., 2023; Cobo-Reyes et al., 2022).
- `mpcr` (cost-to-benefit ratio): Central to theoretical and empirical models (Cobo-Reyes et al., 2022; Zhang & Pei, 2022; Gioffré & Tampieri, 2025).
- `all_or_nothing`: Some studies use binary-action games (Calabuig et al., 2024; Ishikawa & Fontanari, 2025).
- `punishment_cost` and `punishment_tech`: Detailed and varied; critical for moderating efficiency effects (Ishikawa & Fontanari, 2025; Lec et al., 2023).
- `reward_exists`, `reward_tech`, `reward_cost`: Addressed in some studies, mainly by contrast to punishment (Peng, 2022).

**Indirectly informed/contextually discussed:**
- `chat`: Generally absent, sometimes considered as a communication/coordination device (Lec et al., 2023; Pancotto et al., 2023).
- `show_n_rounds`, `show_other_summaries`: Occasionally discussed as information structures affecting strategic behavior (Kurokawa, 2022).
- `show_punishment_id`, observability details: Highlighted as critical in some adjacent games (Gueth & Otsubo, 2023; Li et al., 2023).

**Effectively missing or very sparsely addressed:**
- `default_contrib`: Rarely explicitly manipulated or reported.
- Details such as the specifics of how punishment or reward identities are displayed, or the exact framing of contributions (`defaultContribProp`), are mostly missing.

---

# 7) Important Limitations

- **Partial coverage of direct PGGs with peer punishment:** While several papers have *exact* or *close* relevance, many key findings come from adjacent games or theory, so transfer to generic PGGs with peer punishment must be cautious.
- **Limited empirical payoff data for peer punishment:** Some robust efficiency results derive from institutional punishment, or from coordination/adjacent games; settings with peer-only punishment show more mixed or weak evidence, especially empirically.
- **Potential overestimation from behavioral proxies:** Many studies infer likely efficiency changes from behavior (contributions, cooperation) rather than measuring net payoffs, risking misestimation if punishment costs are under- or over-utilized.
- **Design dimension sparsity:** Not all prediction dimensions are comprehensively covered; notably, specifics of contribution framing (`default_contrib`), information structure, and combined presence of punishment and reward are often missing.
- **Varied game structures and institutional features:** Effect sizes and even directions depend importantly on game type (peer vs institutional punishment, symmetric vs asymmetric games, optional vs compulsory participation), making broad generalization risky.
- **Complexity of moderators and interactions:** Interactions among design dimensions—such as group size, repetition, observability, and cost structure—mean that simple rules for predicting efficiency changes may not perform well out of sample.
- **Ambiguity and conflict in literature:** Some papers show punishment reliably improves efficiency; others find it reduces or has no effect, especially in short, costly, uncoordinated, or binary-action games.

---

**In conclusion:**  
The literature provides substantial, but heterogeneous, evidence for predicting efficiency effects of enabling punishment in PGG-like settings. Empirical and theoretical results reinforce that the effect of peer punishment is context-dependent, with efficiency gains most likely when costs are low, deterrence is credible, and group/punishment structure is favorable. However, damaging effects are possible—especially with peer costly punishment used excessively or inappropriately. Entries for several prediction dimensions are richly supported, but others remain sparse or indirect, and care is needed in mapping from literature to specific game designs.
