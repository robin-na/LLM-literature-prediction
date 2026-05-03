# 1) Evidence Base

The provided literature set is dominated by *theoretical and simulation studies*, with a modest minority of *empirical laboratory experiments*, and a small number of bibliometric or survey-style syntheses. The set is broad in terms of social dilemma contexts (public goods games, networked games, trust games, resource allocation, and adjacent settings like the prisoner's dilemma), but *narrow or concentrated* with respect to *empirical payoff-based efficiency outcomes* in classical, controlled PGG contexts. 

Crucially, the strongest, most directly applicable evidence for the prediction task comes from a core subset of *theoretical and simulation-based papers* specifically on standard or spatial PGGs with explicit, parameterized punishment mechanisms affecting group efficiency. Laboratory experimental evidence is rare but present in a few closely matched cases—mostly pertaining to variants (e.g., threshold PGGs with third-party punishment).

# 2) Task Relevance

### By Dimension

- **pgg_or_variant**:  
  - *exact*: About 15–20 papers model standard or variant public goods games (PGGs) directly.  
  - *close*: Several more focus on 'nearby' N-player dilemmas (threshold games, resource sharing, collective-risk games).  
  - *adjacent/weak*: Many use prisoner's dilemma, snowdrift, or trust games, which are structurally related but differ crucially in payoff structure and cooperation dynamics.

- **punishment_or_sanctions**:  
  - *exact*: ~10–12 papers provide explicit, parameterized comparisons with and without punishment mechanisms in PGGs or very close variants.  
  - *close*: More papers introduce institutional, third-party, or hybrid punishment mechanisms, or discuss analogous sanctioning elements.  
  - *adjacent/weak*: Many rely on non-payoff sanctions (e.g. partner-switching, reputation-based exclusion) or focus on settings where punishment is a behavioral moderator but not a direct payoff deduction.

- **efficiency_or_related_payoff_outcome**:  
  - *exact*: ~7–10 papers report explicit efficiency, group payoff, or welfare comparisons with and without punishment in PGG-like settings.  
  - *close*: Some report closely related outcomes (e.g., probability of achieving the group goal, welfare proxies) in collective-risk or threshold games.  
  - *adjacent/weak*: The majority report *behavioral outcomes* (cooperation rate, contribution frequency, prevalence of cooperators vs. defectors) rather than direct payoff-based group efficiency measures.

**Summary:**  
The subset of papers with *exact* or *close* relevance across all three axes—PGG structure, explicit punishment, and group efficiency/payoff outcomes—is limited. Most of the literature provides only indirect, adjacent, or mechanistic support for efficiency prediction.

# 3) Outcomes Measured In The Literature

- **Payoff-based outcomes** (central to prediction):  
  - *Directly measured:* Efficiency (group payoff as % of full cooperation), total welfare, and success rates in meeting group targets (in threshold games).
  - *Indirect proxies:* Frequency of successful outcomes, equilibrium group payoff, total coins generated.

- **Non-payoff behavioral outcomes** (secondary for prediction):  
  - Prevalence of cooperation, contribution rates, fractions of cooperators and defectors, norm enforcement behavior, punishment/reward frequency, partner choice dynamics, strategy adoption rates.

*Important distinction*: Many studies show that punishment increases *cooperation rates*, but do not assess or report the *net efficiency*, which can be lower if punishment is costly or misapplied.

# 4) Main Findings Relevant To Prediction

### Empirical and Theoretical Evidence (Payoff-focused and Directly Relevant)

- **Enabling punishment (when costs are not prohibitively high and the marginal per-capita return (MPCR) is low or moderate) in a standard or spatial PGG robustly increases group efficiency — often moving equilibria from low to high efficiency (Wu et al., 2014; Sun et al., 2025; Cui et al., 2022; Zhang et al., 2019; Gao & Liang, 2020).**
  - This effect is strongest when punishment cost is low, the punishment mechanism is sufficiently effective, and defector suppression leads to stable clusters or all-cooperator states.

- **The magnitude of the efficiency gain from punishment is highly sensitive to:**
  - Punishment cost and effectiveness (Wu et al., 2014; Sun et al., 2025; Zhang et al., 2019).
  - Game structure (network topology: small-world > regular lattice > random; fairness mechanism present; local vs. global information, etc.) (Cui et al., 2022; Zhang et al., 2019).
  - Parameterization: strong collective punishment (tax-funded) is more effective, and, in some cases, *reward* may work even better (Yang & Yang, 2024).

- **When punishment is 'cheap and effective', efficiency gains are large even in adverse settings (low MPCR); as punishment cost rises, or if punishment is ineffective, these gains are diminished or can reverse — especially if resource wastage from punishment surpasses the benefit of increased cooperation (Sun et al., 2024).**
  - Redistribution of punishment fines to cooperators can partially or fully offset punishment costs in high-cost settings (Sun et al., 2024).

- **Variants with weak, automatic, and strictly efficiency-reducing punishment (not peer punishment; e.g., central, low-magnitude, non-deterrent fines) may fail to increase efficiency (Yang et al., 2020).**
  - In such cases, punishment neither raises contributions nor increases group payoff.

- **Third-party or institutional punishment (TPP):** When well calibrated, automatic TPP systems can increase contribution and the probability of group success in threshold PGGs — translating to likely increases in group payoff, at least in small groups (Liao et al., 2021 [Retracted]; Morison et al., 2025; Yang et al., 2018).

### Adjacent/Mechanistic Evidence

- Many studies model cooperation rates and show that *punishment (even when rare or only moderately effective) can strongly boost cooperation and prevalence of pro-social strategies* (Nakamura, 2019; Li et al., 2023; Qian et al., 2022).
  - Important caveat: These outcomes do *not account for the cost of punishment* or the net group payoff.

- Institutional structure matters: Peer punishment and central punishment interact in threshold games, and their net efficiency depends on risk, wastage, and implementation (Qian et al., 2022).

# 5) Prediction Guidance

Given the evidence base:

- **In PGGs and close variants, prediction of treatment (punishment-enabled) efficiency from design dimensions and control efficiency should be most strongly anchored in the following principles:**
  - **Punishment will generally increase efficiency, especially when:**
    - *Punishment cost is low* relative to its effectiveness.
    - *MPCR* is low (i.e., when cooperation is hard to sustain in control).
    - *Network structure* supports clustering/reciprocity (spatial or small-world).
  - **Efficiency gains are *modulated* by:**
    - Cost and redistributive mechanism of punishment.
    - Player count and group size (thresholds for effectiveness and stability).
    - Additional mechanisms (fairness, memory, learning dynamics).
    - Implementation as *peer* vs. *central* (or third-party) punishment.
    - The presence of *reward* (punishment + reward can be more effective than either alone in some models).

- **Quantitative prediction of treatment efficiency should *not* be based on behavioral outcomes (e.g., cooperation rate) alone, unless the cost of punishment is negligible or explicitly factored in.**

- **For games with weak, non-peer, or non-deterrent punishment (or where the punishment is explicitly efficiency-reducing), expect little or no efficiency gain—and possibly losses compared to control (Yang et al., 2020).**

- **In threshold or collective-risk variants, enabling punishment can increase the probability of achieving group goals, supporting higher expected efficiency (Liao et al., 2021; Yan et al., 2024), but details of implementation, group size, and cost all matter.**

- **In adjacent settings (trust games, resource allocation games), punishment mechanisms increase efficiency mostly when they are universally applied and deterrent; partial, selective, or expensive punishment can reduce or reverse these benefits (Nasrallah & Cheaib, 2016; Mariano & Correia, 2015; Dubey et al., 2021; Rauwolf & Bryson, 2018).**

- **Control efficiency is highly predictive of treatment efficiency when punishment is not effective or punishing is costly (i.e., treatment adds little); when punishment is cost-effective and cooperation is low in control, expect dramatic efficiency gains.**

# 6) Design Dimensions Highlighted Across Papers

- **Directly informed (with payoff/efficiency outcomes):**
  - `player_count`: Strongly featured across models/studies as a moderator of punishment’s effectiveness and equilibrium states.
  - `mpcr`: Central across PGG papers; high signal for predicting when punishment shifts efficiency.
  - `punishment_cost`, `punishment_tech`: Parameterized and manipulated in most direct-relevance models; critical for prediction.
  - `all_or_nothing`: Most models are either all-or-nothing or continuous PGG; explicitly manipulated in several papers.
  - `num_rounds`: Moderately addressed (usually as infinite or fixed length); some attention given to memory effects and game length.
  - `reward_exists`: Modeled in combination with punishment in multiple theory papers (Sun et al., 2025; Yang & Yang, 2024; Gao & Liang, 2020).

- **Indirectly informed:**
  - `show_other_summaries`, `show_n_rounds`, `show_punishment_id`: Indirectly mentioned as moderators (network information, transparency), but rarely manipulated as main variables in payoff-outcome studies.
  - `chat`: Only occasional mention; little direct evidence for its effect on efficiency with punishment.
  - `default_contrib`: Framing is rarely the focus.
  - `punishment_exists`/`reward_cost`/`reward_tech`: Where modeled, usually included as part of the main mechanism, not as a separate dimension; rarely parameterized across studies.

- **Only contextually or sparsely discussed:**
  - `show_punishment_id`, `chat`, and `default_contrib` are discussed only peripherally, not as focal design elements in most payoff-based studies.
  - `reward_cost`, `reward_tech`, and explicit manipulation or reporting of these dimensions are minimal.

- **Effectively missing:**
  - Several dimensions (especially related to display, interface, or behavioral transparency—e.g., `show_n_rounds`, `chat`, `show_punishment_id`) are not systematically examined with respect to *efficiency* effects in the punishment context in this literature set.

# 7) Important Limitations

- **Empirical limitation:** Direct laboratory (real participant) studies of *efficiency effects of peer punishment in PGGs* are sparse. Most findings derive from simulation or theory; external validity or quantitative effect sizes are lacking for many parameter regimes.

- **Outcome limitation:** Many papers report *behavioral* cooperation increases but lack payoff/efficiency analysis; costs of punishment (welfare impacts) are often ignored or only qualitatively discussed.

- **Design dimension coverage:** Network topologies, punishment cost/tech, player count, and synergy (MPCR) are most deeply analyzed; other dimensions crucial for prediction (information display, chat, reward parameters, framing) are largely unaddressed.

- **Contextual specificity:** Results often depend on stylized or idealized conditions (spatial structure, infinite/large populations, evolutionary selection) that may not map perfectly to controlled laboratory or real-world PGGs.

- **Conflict and ambiguity:** Some models predict that punishment can reduce efficiency if cost is high, if punishment is not properly targeted, or if system-level wastage (from over-punishment) offsets cooperation gains (Sun et al., 2024; Qian et al., 2022; Yang et al., 2020).

- **Generality caveat:** Adjacent and mechanistic models (prisoner’s dilemma, trust, or resource sharing games) may not transfer effect quantitatively to standard PGG efficiency, due to structural differences.

---

# Summary Table

| Dimension               | Coverage          | Evidence for Effect on Efficiency from Punishment    |
|-------------------------|-------------------|------------------------------------------------------|
| player_count            | Direct            | Moderates effectiveness, thresholds for cooperation (Wu et al., 2014; Zhang et al., 2019)                  |
| num_rounds              | Direct/Moderate   | Game length/memory can matter but not systematically varied                                |
| chat                    | Sparse/Contextual | Rarely analyzed with efficiency outcome                                                  |
| all_or_nothing          | Direct            | Mechanisms operate in both types; effect size context-specific                           |
| default_contrib         | Sparse            | Not a primary focus                                                                     |
| mpcr                    | Direct            | Central moderator: low MPCR, punishment more valuable (Wu et al., 2014; Cui et al., 2022)                   |
| punishment_cost         | Direct            | Strong moderator: lower cost, higher gain; high cost can reverse benefit                   |
| punishment_tech         | Direct            | Punishment magnitude/effectiveness; design specifics critical                             |
| reward_exists           | Moderate/Direct   | Reward amplifies effect; sometimes more effective (Yang & Yang, 2024)                     |
| reward_cost/tech        | Sparse            | Some modeling, little efficiency evidence                                                |
| show_n_rounds           | Sparse            | Contextual moderator, not directly studied                                               |
| show_other_summaries    | Indirect          | Sometimes implicit (e.g., network information); effects on efficiency unclear             |
| show_punishment_id      | Sparse            | Practically unstudied for efficiency outcomes                                            |

# References

- Wu, Z. W., Xu, Z. J., & Zhang, L. Z. (2014)
- Sun, X. P., Liu, X. Z., Kang, H. W., Shen, Y., & Chen, Q. Y. (2025)
- Yang, Z. H., & Yang, Y. L. (2024)
- Cui, P. B., Wu, Z. X., & Zhou, T. (2022)
- Zhang, B. J., Cui, Z. G., & Yue, X. H. (2019)
- Sun, X. P., Bi, Y. Z., Kang, H. W., Shen, Y., & Chen, Q. Y. (2024)
- Yang, X. Q., Zhang, F., Wang, W. X., Zhang, D., Shi, Z. H., & Zhou, S. W. (2020)
- Gao, S. P., & Liang, J. L. (2020)
- Liao, Y. L., Zhang, L., Lei, S. Y., Song, M. Z., Deng, W. K., & Hu, D. F. (2021) [Retracted]
- Nasrallah, W. F., & Cheaib, K. A. (2016)
- Mariano, P., & Correia, L. (2015)
- Dubey, S. P., Kedar, G. D., & Ghate, S. H. (2021)
- Rauwolf, P., & Bryson, J. J. (2018)
- Qian, J., Sun, X., Zhang, T. D., & Chai, Y. T. (2022)
