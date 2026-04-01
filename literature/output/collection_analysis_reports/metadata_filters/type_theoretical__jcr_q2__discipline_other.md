# 1) Evidence Base

The paper set consists exclusively of theoretical works (no empirical or laboratory experiments) modeling a range of public goods games (PGG), related social dilemmas, and adjacent regional governance, trust, and regulatory settings. The coverage is broad in terms of institutional forms, network structures, and design dimensions. However, for the specific downstream prediction task—predicting efficiency outcomes in PGGs with or without punishment—empirical evidence is absent. Only a subset of papers (e.g., Zhang & Cao, 2020; Park, 2022; Janssen, 2015) directly model or synthesize public goods games (PGGs) with all payoff-relevant design features, while others engage with trust games, principal-agent models, or regulatory/CPR dilemmas with overlapping but not identical structures. Several papers review or simulate comparative regimes (punishment, reward, communication), and a minority provide analytic boundaries for when punishment improves group efficiency. The literature set is thus methodologically homogenous (theory/modeling/simulation only), but contextually and topically broad with varying proximity to the target prediction environment.

# 2) Task Relevance

**pgg_or_variant:**  
- *Exact:* Zhang & Cao (2020); Park (2022); Janssen (2015) focus on PGGs or standard social dilemmas nearly identical to PGGs, and sometimes distinguish PGGs from closely related types.
- *Close/Adjacent:* Most other papers (e.g., Lim & Capraro, 2022; Baker & Choi, 2018; Wang & Cui, 2022) consider trust games, principal-agent problems, or regional resource dilemmas which share features with PGGs but differ in strategic structure, player roles, payoff externalities, or update mechanisms.

**punishment_or_sanctions:**  
- *Exact:* A majority of papers model or analyze punishment or sanction mechanisms in detail, sometimes also considering dynamic vs. static sanctioning, institutional vs. peer punishment, or the combination with reward (Janssen, 2015; Lim & Capraro, 2022; Zhang & Cao, 2020).
- *Close/Adjacent:* A few address related regulatory interventions or the emergence of institutional sanctions, but not the direct peer-punishment as in standard PGGs (Armstrong et al., 2024).

**efficiency_or_related_payoff_outcome:**  
- *Exact:* Only a small subset directly analyze efficiency or aggregate group payoff (Zhang & Cao, 2020; Lim & Capraro, 2022 [for trust games]); Park (2022) evaluates efficiency, but only for PGGs *without* punishment.
- *Adjacent/Weak:* Many papers focus on compliance, cooperation probability, or the stability of behavior, not total payoff or efficiency per se.
- *Weak:* Several relevant findings thus rest on behavioral proxies, not direct measurement or calculation of efficiency (e.g., legal emission probability, compliance, cooperative strategy preponderance).

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes:**  
  - *Efficiency (group payoff relative to full cooperation):* Addressed directly only in a few papers (Zhang & Cao, 2020; Lim & Capraro, 2022 [trust game]).
  - *Total earnings / mean payoff / surplus:* Modeled or implicitly analyzed in papers focusing on PGGs or trust games with explicit payoff matrices (Zhang & Cao, 2020; Lim & Capraro, 2022; Park, 2022 for the control condition).
  - Many other papers *do not* report direct payoff/efficiency outcomes, even when discussing incentive/penalty mechanisms.

- **Non-Payoff Behavioral Outcomes:**  
  - *Contribution or cooperation rates, compliance/stability of cooperation strategies, probability of legal emissions, norm adherence, likelihood of regulation or monitoring, supervision probability.*  
    These are dominant in the majority of the literature set (e.g., Li et al., 2023; Wang & Mao, 2024; Huo & Liu, 2024).
  - These measures are argued to *predict* or support higher efficiency, but translation to total payoffs is often assumed, not demonstrated.

# 4) Main Findings Relevant To Prediction

Synthesizing across relevant papers:

- **Punishment tends to increase efficiency in PGGs—under certain parameter regimes.**  
  - When punishment is *strong enough* relative to the public goods multiplier and not too costly, models predict a transition to full cooperation, achieving maximal efficiency (Zhang & Cao, 2020; Lim & Capraro, 2022).
  - If punishment is *weak, costly, or can be circumvented* (e.g., low fine, high cost, or available insurance), defection or speculative strategies persist, and efficiency gains are marginal or absent (Zhang & Cao, 2020; Baker & Choi, 2018).
  - The threshold for effective punishment is analytically characterized in some models (Zhang & Cao, 2020; Lim & Capraro, 2022 [networked trust game]).

- **Contextual and design factors moderate the impact of punishment:**  
  - *Group size and network structure:* Efficiency benefits from punishment are more robust in smaller or more connected groups, as effectiveness of monitoring and sanctioning scale differently with group size (Janssen, 2015; Lim & Capraro, 2022).
  - *Institutional design:* Centralized or legal sanctions may outperform peer punishment when enforcement is more accurate and observable (Baker & Choi, 2018; Janssen, 2015).
  - *Communication and reward mechanisms can synergize with punishment* to boost efficiency, but “crowding out” effects from external regulation are possible if poorly designed (Janssen, 2015).

- **Behavioral and indirect evidence generally supports efficiency gains from punishment:**  
  - Even in models not directly reporting efficiency, stronger or dynamic punishment designs robustly increase compliance, cooperation, and norm adherence—theoretical prerequisites for higher group payoff (e.g., Jiang & Zheng, 2024; Huo & Liu, 2024), though exact efficiency translation remains unsupported.

- **Potential limits and reversals:**  
  - When punishment is error-prone, overly costly, or when external incentives crowd out intrinsic motivation, efficiency gains diminish or may reverse (Baker & Choi, 2018; Janssen, 2015).
  - Overly severe (static) punishment or poorly targeted sanctioning can destabilize cooperation or induce cycles (Jiang & Zheng, 2024).

# 5) Prediction Guidance

**For predicting average efficiency (treatment) from control efficiency plus game design:**

- If the game design dimension values (mpcr, punishment_cost, group size, etc.) imply that punishment is *salient, not too costly, and visible*, it is theoretically well-supported to predict a *substantial efficiency gain* when punishment is enabled—potentially to near-maximal efficiency if the initial (control) efficiency is moderate and parameter thresholds are exceeded (Zhang & Cao, 2020; Lim & Capraro, 2022; Baker & Choi, 2018).
- If punishment is *weak, error-prone, very costly, or group structure is highly adverse* (e.g., large, fragmented, or with insurance/avoidance options), *minimal or no efficiency gain* is predicted; cycles or partial cooperation may persist (Zhang & Cao, 2020; Armstrong et al., 2024).
- If *communication/reputation/trust mechanisms* are present, or group size is small/moderate, efficiency gains from enabling punishment remain positive and may be synergistic (Janssen, 2015; Lim & Capraro, 2022).
- When control (no punishment) efficiency is already high (e.g., due to strong norm compliance or other mechanisms), enabling punishment may yield only marginal gains, or even introduce costs that slightly *reduce* efficiency (crowding out, over-punishment).

All above points rest on *theoretical* evidence; empirical quantification is missing, and the “translation” from behavioral to payoff outcomes is sometimes implicit.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed (by theory or explicit modeling):**
- `player_count`, `num_rounds`, `all_or_nothing`, `mpcr`, `punishment_cost`, `punishment_tech`—regularly parameterized and discussed as determinants of equilibrium and efficiency (esp. Zhang & Cao, 2020; Lim & Capraro, 2022; Park, 2022).
- `reward_exists`—explicitly included in some adjacent models (Jiang & Zheng, 2024; Li et al., 2023).
- `show_n_rounds`—discussed in legal sanctioning set-ups (Baker & Choi, 2018).

**Indirectly informed / contextually discussed:**
- `chat`—discussed as a boost for group efficiency/moderation of punishment effects (Janssen, 2015).
- `default_contrib`—framing effects assumed but rarely explicitly modeled.
- `show_other_summaries`—visibility of outcomes noted as a moderator in some legal and trust models (Baker & Choi, 2018).
- `show_punishment_id`—partially considered under the “transparency” of sanctions.
- `reward_cost`, `reward_tech`—modeled in some papers with reward as a separate mechanism.

**Effectively missing / not modeled:**
- How efficiency outcomes depend on combinations/interactions of show_other_summaries, show_punishment_id, default_contrib, or chat, except in limited conceptual discussion.

# 7) Important Limitations

- **Lack of empirical/experimental findings:** All results are theoretical or from simulations; no measured efficiency outcomes from actual PGG experiments are in the evidence base.
- **Few exact matches to target outcome:** Only a minority of papers report or model “efficiency” as a ratio of group payoff to the full-cooperation benchmark in an exact PGG with/without punishment.
- **Heavily reliant on behavioral proxies:** Much of the support for predicting efficiency gain comes from changes in cooperation/compliance probabilities, not direct group payoffs.
- **Generalizability questions for adjacent models:** Many findings derive from games with important structural differences (e.g., trust games, principal-agent, multi-actor regulatory games), which may not fully generalize to experimental PGGs.
- **Sparse attention to some prediction dimensions:** Direct outcome mapping for dimensions like chat, visibility variables, or contribution framing is thin, limiting nuanced multi-dimensional prediction.
- **Ambiguity in parameter sensitivity:** Although thresholds for “effective” punishment are sometimes calculated, real-world mapping to empirical parameter values is unclear.
- **No coverage of dynamic or long-term trajectories:** Most models identify equilibrium or steady-state outcomes rather than transient efficiency trajectories or path dependence.

**In sum:**  
The theoretical literature robustly supports the *potential* for punishment to increase efficiency in public goods games, with clearly specified design moderators and parameter boundaries. However, quantitative prediction is limited by the lack of empirical payoff data, sparse treatment of some experimental dimensions, and extensive reliance on indirect or behavioral outcomes in adjacent problem domains. Prediction should carefully consider whether the modeled conditions match the design being forecast, and the translation of behavioral to payoff gains should remain explicit and cautious.
