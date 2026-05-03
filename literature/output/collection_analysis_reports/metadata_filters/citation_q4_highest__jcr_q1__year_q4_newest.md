# 1) Evidence Base

The paper set comprises 11 sources, predominantly theoretical in nature, with no direct empirical or experimental studies reporting observed efficiency or payoff outcomes under manipulation in the lab or field. The set is moderately broad, covering various aspects of public goods games (PGGs), punishment and reward mechanisms, social norm enforcement, strategy updating, and cooperation dynamics—mostly through simulations, agent-based models, and conceptual reviews. Several papers are highly specific to spatial games or structured populations (e.g., Lee et al., 2022; Lv & Song, 2022), while others address evolutionary, psychological, and cultural contexts in broader collective action or dilemma settings. Notably, only a few papers model payoff-related outcomes (e.g., efficiency, total group payoff) as primary endpoints, and fewer still do so under manipulation of punishment in actual PGG-like environments. Coverage of the downstream prediction task is thus partial: robust on mechanism and parameter analysis in simulated or hypothetical systems, but lacking on large-sample empirical effect sizes or direct experimental validation.

# 2) Task Relevance

### pgg_or_variant
- **exact:** Several papers directly address classical or spatial public goods games (Lee et al., 2022; Lv & Song, 2022; Hua & Liu, 2024).
- **close/adjacent:** Others model the Prisoner’s Dilemma (Gou & Li, 2023; Wang et al., 2022) or discuss public goods problems in anthropological or applied settings (Boyd & Richerson, 2022) or related theoretical contexts.

### punishment_or_sanctions
- **exact:** A subset directly models punishment as a mechanism affecting outcomes in the PGG (Lee et al., 2022; Wang et al., 2023).
- **adjacent/close:** Several papers review punishment as one of several norm enforcement or cooperation-sustaining mechanisms (Van Lange & Rand, 2022; Boyd & Richerson, 2022; Andrighetto & Vriens, 2022; Gross & Vostroknutov, 2022), often in general conceptual, rather than game-theoretic, terms.
- **none:** Some papers focus on reward/incentives (Hua & Liu, 2024) or neglect punishment as a factor (Wang et al., 2022; Gou & Li, 2023; Wang et al., 2022).

### efficiency_or_related_payoff_outcome
- **exact/close:** Only a few sources use efficiency (ratio of achieved to optimal group payoff) or total/social payoff as their primary outcome (Lee et al., 2022; Hua & Liu, 2024; Wang et al., 2023). Many others—while modeling cooperation, sanctions, or norms—focus on behavioral measures (e.g., cooperation or compliance rates) rather than efficiency or aggregate payoff.
- **adjacent/weak:** Most other sources provide only indirect information relevant to efficiency, relying on mechanistic, behavioral, or institutional cost outcomes (Wang et al., 2023; Van Lange & Rand, 2022).

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:** 
    - Efficiency (group payoff as a proportion of maximal possible; Lee et al., 2022; Hua & Liu, 2024).
    - Cumulative cost to an institution implementing incentive mechanisms, often treated as a proxy for social welfare or system-level efficiency (Wang et al., 2023).
- **Non-payoff behavioral outcomes:**
    - Cooperation rate, contribution rate, norm compliance, and cluster stability are common endpoints (Lv & Song, 2022; Gou & Li, 2023; Van Lange & Rand, 2022; Boyd & Richerson, 2022; Andrighetto & Vriens, 2022).
    - Mechanism and strategy-behavioral dynamics (e.g., proliferation, cyclic dominance, role of gossip or memory) are frequently highlighted.
- **Notably missing:**
    - Few studies report direct empirical data on realized group earnings or social surplus under experimental manipulation of punishment in actual PGGs.
    - No studies explicitly report average "efficiency with punishment" as a predicted or observed value given control condition efficiency.

# 4) Main Findings Relevant To Prediction

### Synthesized Empirical/Theoretical Findings

- **Punishment Increases Efficiency Under Specific Conditions:** 
    - Spatially structured models consistently show that introducing punishment can increase group efficiency relative to no-punishment controls, but only when punishment cost is moderate and fines are sufficiently large (Lee et al., 2022).
    - Too-high punishment costs or too-low fines either reduce or fail to boost efficiency.
    - There is evidence for an **optimal punishment cost** (neither too high nor too low) maximizing collective payoff (Lee et al., 2022).
    - The addition of supporting institutional taxes can further increase efficiency, especially when punishment is costly, but may backfire with weak punishment (Lee et al., 2022).

- **Dependency on Behavioral and Learning Rules:** 
    - Effects of punishment on cooperation (but not directly on efficiency) depend on learning rules: certain updating dynamics (e.g., weighted neighbor influence) interact with punishment intensity to affect cooperation levels (Lv & Song, 2022).
    - Although higher cooperation may imply higher efficiency, this is only indirectly supported since efficiency itself is not reported.

- **Institutional Versus Peer Punishment:** 
    - Institutional punishment achieves high cooperation (and by extension, likely better efficiency) more cost-effectively when the pre-existing cooperation rate is already high, whereas rewards are better for low baseline cooperation (Wang et al., 2023).

- **Norms and Additional Mechanisms:** 
    - Norm enforcement, reputation, and alternative mechanisms such as gossip can supplement or substitute for punishment in increasing cooperation, sometimes with lower efficiency loss (Van Lange & Rand, 2022).
    - Strong norm enforcement (and by implication, strong punishment) can, under some conditions, sustain inefficient or undesirable equilibria as well as positive ones (Andrighetto & Vriens, 2022).

- **Contextual Moderators:** 
    - Group size, observability, network structure, and initial condition specifics are important moderators—although quantitative effects are not specified in the reviewed literature.
    - Transition from small to large groups may necessitate added punishment or other sanctions to maintain cooperation, though the direct efficiency effect remains ambiguous and context-dependent (Boyd & Richerson, 2022).

# 5) Prediction Guidance

Based on this literature set:
- **Direct Predictive Value:** The most specific guidance for predicting post-punishment efficiency comes from Lee et al. (2022): if a game's existing efficiency is moderate or low, enabling punishment will increase efficiency only when the cost to punishers is not too high and the fine is large enough to deter defection. The relationship is non-monotonic (there exists an optimal punishment cost/fine balance), and outcomes are highly sensitive to parameter value choices and spatial structure. The model strictly applies to spatial PGGs with three strategies (Cooperator, Defector, Punisher).
- **Institutional Cost Considerations:** If the game uses institutional punishment (rather than peer), overall gains in efficiency can depend on the baseline level of cooperation: for already-cooperative populations, punishment is more cost-effective than reward, but the reverse holds at low cooperation (Wang et al., 2023).
- **Mechanistic but Non-Payoff Evidence:** Other reviewed constructs (norm strengths, learning rules, use of gossip, network topology) influence the qualitative effect of punishment on cooperation but do not quantify its impact on efficiency. Thus, their relevance for forward prediction is primarily in identifying contexts where punishment is more/less likely to be efficiency-improving.
- **Where Insufficient:** For most of the 14 game design dimensions, there is either only theoretical coverage (not empirical) or only mechanistic discussion without explicit quantitative effect sizes. Crucially, there are no robust empirical links between control-game efficiency and subsequent efficiency under punishment across parameter ranges.

# 6) Design Dimensions Highlighted Across Papers

### Directly Informed Dimensions
- **player_count:** Explicit in multiple theory papers (Lee et al., 2022; Lv & Song, 2022; Hua & Liu, 2024).
- **num_rounds:** Modeled in several simulations and discussed as important for repeated dynamics (Lee et al., 2022; Lv & Song, 2022).
- **all_or_nothing:** Present in structural and evolutionary models (Lee et al., 2022; Hua & Liu, 2024).
- **mpcr (Marginal per-capita return):** Key parameter in payoff and phase analyses in PGG studies (Lee et al., 2022; Hua & Liu, 2024).
- **punishment_cost, punishment_tech (implementation details):** Central to theoretical models (Lee et al., 2022; Lv & Song, 2022; Wang et al., 2023).

### Indirectly or Partially Informed
- **reward_exists, reward_cost, reward_tech:** Covered in reward-focused papers and in dual-incentive models (Hua & Liu, 2024; Wang et al., 2023).
- **show_other_summaries:** Discussed in relation to observability and norm enforcement (Van Lange & Rand, 2022).
- **show_punishment_id:** Addressed in social and historical contexts (Boyd & Richerson, 2022).

### Contextually Mentioned/Broadly Discussed
- **chat, show_n_rounds, default_contrib:** Not systematically modeled, but referenced sporadically as structural or procedural variables.

### Effectively Missing/Not Covered
- **default_contrib:** Rarely specified as a manipulated dimension; only occasionally inherent in model framing.
- **chat, show_n_rounds:** Only minor or contextual mentions, not systematically explored for impact on efficiency or punishment effects.

# 7) Important Limitations

- **Empirical Gaps:** There are no empirical studies or meta-analyses in this set reporting observed efficiency outcomes under the addition of punishment, nor systematic mapping from control to treatment efficiency.
- **Parameter Sensitivity:** Even in theory, efficiency effects of punishment are highly sensitive to calibrated parameter values (punishment cost, fine, population structure), often unique to specific game forms (e.g., spatial, institutional).
- **Indirectness of Results:** The majority of behavioral results concern cooperation or norm compliance rates, not payoff-based efficiency, even though these may be correlated.
- **Generalizability Issues:** Results for spatial PGGs, institutional versus peer punishment, or structured network contexts may not generalize to standard experimental PGG designs with random matching or no spatial structure.
- **Design Dimensions Underexplored:** Several prediction dimensions (e.g., chat, default contribution, round information) are absent or only mentioned contextually, limiting model input coverage.
- **Absence of Quantitative Effect Sizes:** Where efficiency is discussed, the literature is theoretical/model-based, often yielding qualitative or phase-based statements rather than effect-size predictions.
- **No Direct Mapping from Control Game Efficiency:** There is no empirical or theoretical study in the set that provides a direct mapping or formula relating observed control-game efficiency (with punishment off) to expected treatment efficiency (with punishment on), conditional on the full 14-dimensional design vector.

---

In summary, the literature set provides several mechanistically detailed and theoretically justified pathways through which punishment can affect efficiency in structured PGG-like environments, identifying parameter conditions necessary for efficiency improvements. However, the evidence is predominantly theoretical and mechanism-focused, with only indirect support for the quantitative prediction task. Most game design dimensions are at best only partially addressed, and the lack of empirical, effect-size-based studies remains a major limitation for predictive model calibration.
