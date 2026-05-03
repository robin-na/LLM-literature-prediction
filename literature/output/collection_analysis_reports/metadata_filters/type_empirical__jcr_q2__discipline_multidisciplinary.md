# 1) Evidence Base

The paper set consists of three experimental (lab-based) empirical studies. One (Liao et al., 2021) directly examines punishment mechanisms in a threshold public goods game (PGG). A second (Sadowski et al., 2015) studies a common-pool resource (CPR) dilemma but without any punishment or reward mechanisms, focusing instead on communication and leadership. The third (Schroeder et al., 2014) examines third-party punishment (3PP) and norm violation in a behavioral game structurally adjacent to a PGG, emphasizing non-payoff behavioral outcomes and the effects of local norms and trust. The set is relatively narrow for predicting efficiency changes due to punishment in canonical PGGs: only one paper (Liao et al.) provides direct evidence on the core intervention (punishment enablement) in a close public-goods structure. Others offer context about baseline efficiency (Sadowski et al.) or about factors that might moderate punishment effects (Schroeder et al.) but lack direct payoff-outcome data under PGG-punishment treatment.

# 2) Task Relevance

- **pgg_or_variant:**
  - **Liao et al. (2021):** *Close* – Uses a threshold public goods game, which is a known PGG variant.
  - **Sadowski et al. (2015):** *Close* – Examines a CPR dilemma with strategic overlap to PGGs.
  - **Schroeder et al. (2014):** *Adjacent* – Studies a third-party punishment paradigm with norm emphasis, not exactly a PGG.

- **punishment_or_sanctions:**
  - **Liao et al. (2021):** *Exact* – Direct manipulation of punishment (enabled vs. disabled).
  - **Sadowski et al. (2015):** *Weak* – No punishment or sanctions implemented.
  - **Schroeder et al. (2014):** *Exact* – Directly manipulates and measures third-party punishment.

- **efficiency_or_related_payoff_outcome:**
  - **Liao et al. (2021):** *Adjacent* – Focuses on cooperation success rates and investment rates (behavior); no explicit group efficiency or total earnings reported, but success rate is closely related.
  - **Sadowski et al. (2015):** *Exact* – Efficiency and total earnings explicitly measured.
  - **Schroeder et al. (2014):** *Adjacent* – Behavioral norms and punishment willingness are central; payoffs only contextually referenced.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:**
  - **Liao et al. (2021):** Reports success rates (group reaches threshold), arguably a proxy for group payoff and efficiency but does not specify total payoffs or efficiency ratio.
  - **Sadowski et al. (2015):** Explicitly reports efficiency, group payoff, and earnings.
  - **Schroeder et al. (2014):** Mentions mean payoffs but the primary analysis is on behavioral (norm violation, punishment, trust) outcomes.

- **Non-payoff behavioral outcomes:**
  - **Liao et al. (2021):** Individual/group investment rates, resource investment amount.
  - **Sadowski et al. (2015):** Cooperation, communications, emergence of leadership.
  - **Schroeder et al. (2014):** Frequency and expectation of punishment, norm violations, trust.

# 4) Main Findings Relevant To Prediction

- **Punishment’s effect:**
  - **Direct empirical evidence (Liao et al., 2021):** Introducing third-party punishment in a threshold PGG raises investment rates and increases the probability of achieving the cooperative outcome (success rate from ~56% to ~77%). This strongly implies higher efficiency in these games when punishment is enabled.
  - **Indirect evidence (Schroeder et al., 2014):** Willingness to punish and expectation of punishment is context-dependent—lower in low-trust environments with norm violations—and the subjective cost of punishment moderates actual punishment behavior. However, efficiency impacts are only implied, not measured.
  - **No direct evidence (Sadowski et al., 2015):** Demonstrates that moderate efficiency can be achieved without punishment if communication and leadership are present.

- **Moderators highlighted:**
  - **Trust and local norms:** Affect the use and expected effect of punishment (Schroeder et al.).
  - **Communication and leadership:** Can substitute for sanctions in enabling moderate efficiency, potentially limiting incremental benefit from punishment (Sadowski et al.).
  - **Automatic/detached punishment:** Liao et al. use third-party, automatic punishment, which may differ in effect from endogenous peer punishment.

# 5) Prediction Guidance

- **If a game is structurally similar to Liao et al. (2021) (threshold PGG, small group, impersonal automatic punishment, no chat):** Enablement of punishment is likely to produce a marked increase in group efficiency, as measured by success in achieving the public good.
- **If a game aligns more with Sadowski et al. (2015) (open communication, leadership, large group/community):** Baseline efficiency without punishment may already be moderate; it is unclear if adding punishment would further increase efficiency, given the lack of evidence.
- **If game context includes low trust, norm violation, or high punishment cost (Schroeder et al., 2014):** Effectiveness of punishment for boosting efficiency may be significantly attenuated.

- **Dimension-specific:** The literature best supports positive efficiency effects for punishment in designs with small groups, no communication, and impersonal third-party punishment. Caution is warranted in extrapolating to designs with endogenous punishment, high communication, or settings with varying trust and norm baselines.

# 6) Design Dimensions Highlighted Across Papers

- **Directly informed (empirical evidence on dimension and its interaction with punishment/efficiency):**
  - `player_count` (n=3 in Liao, referenced in Schroeder)
  - `num_rounds` (multi-round in all; interaction with punishment not isolated)
  - `all_or_nothing` (all papers)
  - `mpcr` (Liao, Sadowski)
  - `punishment_cost` (Liao, Schroeder; Liao manipulates, Schroeder focuses on subjective value)
  - `punishment_tech` (Schroeder only; third-party/automatic/impersonal vs. not)
  - `chat` (Sadowski: extensively used; Liao: chat absent, no deliberation)
  - `show_n_rounds`, `show_other_summaries` (Sadowski, Schroeder)

- **Indirectly or contextually discussed:**
  - `default_contrib` (framing not discussed explicitly)
  - `reward_exists`, `reward_cost`, `reward_tech` (not manipulated or analyzed)
  - `show_punishment_id` (identification not systematically manipulated)
  - Group size beyond n=3

- **Effectively missing:**
  - Most reward-related dimensions are not addressed.
  - `show_punishment_id`, detailed information/feedback mechanics, are not linked to efficiency.

# 7) Important Limitations

- **Structural scope:** Only one paper (Liao et al., 2021) investigates the main prediction dimension (punishment enablement) in a reasonably close PGG environment, and it uses an automatic, third-party mechanism rather than endogenous peer punishment.
- **Ambiguity in generalizability:** The highlighted efficiency gain is most credible only for small, no-chat, third-party punishment designs. It is unclear if similar effects hold with endogenous punishment or in environments rich in communication or social structure.
- **Limited payoff measurement:** Behavioral outcomes (contribution rate, norm violation, punishment assignments) are measured more frequently than efficiency; efficiency is directly measured only in Sadowski et al., where punishment does not exist.
- **Missing design dimension coverage:** Several prediction-relevant dimensions (especially regarding reward, identification feedback, or group size >3) are not empirically addressed.
- **Contextual moderators (trust, norms):** Evidence suggests that baseline trust and local norm adherence can substantially moderate the effectiveness of punishment, but efficiency impacts under these moderators remain ambiguous due to lack of direct measurement (Schroeder et al., 2014).
- **Retraction warning:** The main empirical result for punishment effect (Liao et al., 2021) comes from a retracted article, which raises concerns about result reliability.

**Overall, the literature set provides limited but suggestive guidance: evidence is strongest for efficiency improvement via third-party punishment in small, threshold PGGs without communication, but extrapolation to other settings is risky, and payoff-based outcome data are often only proxied or missing.**
