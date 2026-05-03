# 1) Evidence Base

The evidence base in this literature set is broad in the sense that it covers a large diversity of theoretical models of public goods games (PGG) and adjacent collective action environments; however, it is dominated by theory papers and simulation studies, with no direct empirical or experimental studies focused on efficiency outcomes from enabling punishment. Most papers are mathematical or agent-based models that systematically vary game parameters, such as player count, number of rounds, marginal per-capita return (MPCR), and punishment cost, to analyze cooperation and payoff dynamics.

Empirical and experimental evidence is missing from this set, and while several papers report or compute efficiency (as group payoff or welfare), many report only indirect or adjacent outcomes (e.g., cooperation rate). The literature addresses a mix of PGGs, social dilemmas, Prisoner's Dilemma (PD), trust games, and applied multi-agent governance settings. There is some attention to both institutional (pool) and peer punishment, and several models incorporate reward mechanisms, exclusion, reputation, and network structures. A significant portion of the literature focuses on mechanism arguments, providing formulas, threshold conditions, and phase diagrams for efficiency and cooperation outcomes, but the generalization to real-world settings may be constrained by the lack of experimental validation.

# 2) Task Relevance

### a) PGG or Variant (`pgg_or_variant`)
- **Relevance:** Mostly `exact`; the core of the literature models canonical public goods games. Some papers are `adjacent`—trust games, governance dilemmas, or PDs with PGG-like features are also included.
- **Strength:** High, especially for theoretical prediction in canonical PGG or spatial/networked PGG formats.
- **Caveats:** Applicability may be reduced for designs featuring unusual structures or real-world contextual variables not captured in standard models.

### b) Punishment or Sanctions (`punishment_or_sanctions`)
- **Relevance:** Largely `exact` in modeling punishment (peer, pool, tax-based, probabilistic, institutional). Some papers are `close` or `adjacent` (focusing on exclusion, warning, or indirect punishment).
- **Strength:** Strong focus on the design, cost, strength, and adaptivity of punishment, with many studies contrasting punishment and reward.
- **Caveats:** A minority of papers discuss only alternative prosocial mechanisms (e.g., reputation) without considering punishment.

### c) Efficiency or Related Payoff Outcome (`efficiency_or_related_payoff_outcome`)
- **Relevance:** Mixed. A moderate number of papers report or compute group efficiency, welfare, or normalized payoff (`exact` or `close`). Many others focus on cooperation rate, norm compliance, or behavioral strategy frequencies (`adjacent` or `weak`).
- **Strength:** Where present, efficiency findings are closely linked to payoff-based definitions (group payoff, mean/average payoff, social welfare).
- **Caveats:** Predictions extrapolated from non-payoff outcomes (cooperation rate) should be treated with caution, as increased cooperation does not always translate into higher efficiency, especially when punishment is costly.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes (Efficiency):**
  - Explicit group efficiency or normalized group payoff is directly reported/calculated in several theory papers (e.g., Li et al. 2022; Sun et al. 2023; Shen et al. 2022; Ohdaira 2022; Wang & Perc 2022; Han 2022, 2024).
  - Related constructs such as average group payoff, welfare, surplus, or cumulative cost are calculated as primary or secondary outcomes in a subset of models.
- **Non-Payoff Behavioral Outcomes:**
  - Many papers report cooperation rate, defect rate, norm compliance, prevalence of punishment, or strategy frequencies as primary outcomes.
  - Some simulations and models discuss payoff only as a mechanism (e.g., for updating rules or evolutionary stability), not as an outcome of interest.
  - Reviews and conceptual papers focus on behavioral and institutional mechanisms rather than direct efficiency measures.

# 4) Main Findings Relevant To Prediction

**Synthesized Across Papers:**

- **Enabling punishment in standard PGGs generally increases efficiency (group payoff) relative to control, if**:
    - Punishment is not disproportionately costly relative to its impact (punishment cost and fine are moderate) (Li et al., 2022; Wang, C. Q. et al., 2024; Ohdaira, 2022).
    - The synergy factor (MPCR) is high enough and game parameters surpass theoretical thresholds for stable cooperation (Li et al., 2022; Wang & Perc, 2022).
    - Punishment is implemented in a way that minimizes second-order free-riding or antisocial effects (Shen et al., 2022).
    - Adaptive or probabilistic punishment—sensitive to reputation, local payoffs, or defection history—is particularly effective in maintaining higher efficiency in networked or spatial games (Wang, X. J. et al., 2024; Quan et al., 2023; Ohdaira, 2022).

- **Punishment does not always increase efficiency, and can reduce it when:**
    - The punishment cost exceeds its deterrent value, especially in peer punishment not supported by tax or institutional structures (Shen et al., 2022; Han et al., 2024).
    - Punishment leads to retaliation, is applied under noise, or targets cooperators by mistake (Wu et al., 2022).
    - Peer punishment, even if increasing cooperation, may result in lower total welfare due to costly enforcement, compared to reward mechanisms (Han et al., 2024; Wu et al., 2022).
    - Social exclusion or commitment-based punishment is not properly targeted or combined with other incentives, resulting in efficiency loss or over-regulation (Han et al., 2022, 2024; Han et al., 2022 Technology in Society).

- **Reward mechanisms can also promote efficiency, sometimes outperforming punishment, particularly where:**
    - Reward is more cost-effective, especially under noisy monitoring or where legitimacy is important (Sun et al., 2023; Wu et al., 2022; Han, 2022).

- **Contextual moderators include:**
    - **Network structure:** Punishment is more effective at increasing efficiency in structured populations than in well-mixed settings, due to cluster formation and spatial reciprocity (Wang, C. Q. et al., 2024; Quan et al., 2023).
    - **Timing and form of punishment:** Early, well-targeted, and institutionally supported punishment supports higher efficiency (Liu et al., 2022).
    - **Combination with rewards or other governance tools:** The best results (highest efficiency) are often achieved not with punishment alone but with a well-calibrated mix of punishment, reward, and supporting mechanisms such as reputation or exclusion (Li, J. M. et al., 2023; Sun et al., 2023; Shen et al., 2022).

# 5) Prediction Guidance

- **When efficiency is directly reported or mechanistically derivable (from model equations), treatment efficiency with punishment enabled should be predicted as higher than control efficiency if punishment parameters (cost, effectiveness) and other design features meet or exceed theoretical thresholds.** If control efficiency is already high (e.g., due to favorable MPCR or other cooperation-supporting features), the marginal gain from punishment may be less, and in some cases, net efficiency could even decrease if the costs of punishment outweigh deterrence gains (Han et al., 2024; Wu et al., 2022).

- **Design features most relevant for prediction include:** player count, MPCR, punishment cost and effectiveness, type (peer, pool, institutional), reward options, network/spatial structure, reputation mechanisms, and the possibility of antisocial punishment or exclusion.

- **Predictions based on models reporting only cooperation or behavioral rates should be made with caution, and preferably tempered by models or theory that relate those rates to actual payoffs.** Several studies warn that high cooperation under costly punishment may still yield lower group welfare than lower cooperation with reward or no punishment (Han et al., 2024).

- **Hybrid and adaptive punishment/reward mechanisms, especially those responsive to the observed behavior or reputation of players, consistently yield higher predicted efficiency than static, non-adaptive punishment.**

- **Contextual factors, such as corruption, institutional support, the possibility of bribes, and observability of contributions, can substantially moderate the efficiency impact of punishment, even overturning the expected sign (Liu & Chen, 2022; Wu et al., 2022).**

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions** (modeled extensively, with strong linkage to efficiency or payoff outcomes in the literature):
- **player_count**
- **num_rounds**
- **all_or_nothing**
- **mpcr**
- **punishment_cost**
- **punishment_tech** (type, structure, adaptivity, targeting of punishment)
- **reward_exists** (including interaction between punishment and reward)
- **reward_cost**
- **show_n_rounds** (less common, but present in some repeated game models)
- **show_other_summaries** (occasionally, as part of information structure)

**Indirectly Informed Dimensions** (modeled as context or for behavioral outcomes, but with limited direct efficiency data):
- **chat** (rarely modeled; mainly addressed in larger sociological or negotiation settings, e.g., Frey & Burgess, 2023)
- **default_contrib** (occasionally, via opt-in/opt-out or commitment models)
- **reward_tech** (precision of reward targeting, e.g., reputation-based allocation)
- **show_punishment_id** (specifically as reputation or observability mechanisms; generally, more indirect)

**Effectively Missing or Only Contextually Discussed:**
- **Detailed implementation of default contribution framing and chat function.**
- **Direct experimental study of the effect of information visibility (show_n_rounds, show_other_summaries, show_punishment_id) on efficiency.**
- **Logistical features such as ease of communication, clarity of rounds, or framing defaults have not been systematically studied for their impact on treatment efficiency.**

# 7) Important Limitations

- **Lack of Empirical and Experimental Evidence:** The literature is almost entirely theoretical or simulation-based, without direct empirical testing or real-world experimental validation on efficiency outcomes of enabling punishment.
- **Efficiency Often Indirect or Implied:** Many papers infer efficiency effects based on cooperation rates or behavioral dynamics, not on direct measurement or calculation of group payoff/efficiency. This is a significant limitation for payoff-focused prediction.
- **Overemphasis on Canonical Models:** Real-world idiosyncrasies, such as individual heterogeneity, institutional complexity, social identity, and legitimacy of punishment, are not well captured in most models.
- **Limited Discussion of Some Design Dimensions:** Chat, default contribution framing, and detailed implementation of information conditions are not systematically addressed.
- **Potential Misalignment Between Cooperation and Efficiency:** Some papers demonstrate that increased cooperation does not necessarily mean higher efficiency, especially when the cost of punishment is high or punishment is misapplied.
- **Ambiguity for Peer vs. Institutional Punishment:** Many findings are for institutional punishment; while peer punishment is analyzed, its impact appears more variable and sometimes less efficient.
- **Translational Challenges for Adjacent Settings:** Findings from adjacent domains (e.g., governance, environmental protection, trust games) may not transfer straightforwardly to canonical public goods games.

---

**Summary**:  
Theoretical models provide strong guidance that enabling well-designed punishment in PGGs usually increases efficiency relative to control, provided game parameters favor cooperation and the cost-effectiveness of punishment is high. However, the evidence is less clear, and sometimes negative, when punishment is costly, misapplied, or when indirect information makes targeting difficult. The literature is best at informing predictions involving player count, MPCR, punishment/reward structure and cost, and network structure, but is weaker on nuanced design features such as communication, framing, or detailed information structure. Real-world predictions should be tempered by the lack of empirical data and by the demonstrated cases where greater cooperation from punishment fails to translate to increased efficiency.
