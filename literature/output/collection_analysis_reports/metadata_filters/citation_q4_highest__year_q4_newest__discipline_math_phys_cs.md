# 1) Evidence Base

The paper set consists entirely of theory papers; there are no empirical or laboratory experimental studies included. The focus is somewhat narrow, addressing spatial and structured variants of the public goods game (PGG), but with notable differences in the mechanisms studied—one paper examines punishment (Lee et al., 2022), a second explores reward structures (Hua & Liu, 2024), and the third investigates the combined effect of punishment and learning heuristics (Lv & Song, 2022). The set provides phase diagram analyses, payoff modeling, and mechanistic explorations, but lacks real-world or experimental validation. Only the Lee et al. (2022) and Hua & Liu (2024) papers report on game efficiency or total welfare, with the former focused on punishment and the latter on reward; the remaining study tracks solely non-payoff behavioral outcomes (cooperation/investment levels).

# 2) Task Relevance

**pgg_or_variant**:  
- All three studies directly model public goods games or their close spatial equivalents; relevance is **exact**.

**punishment_or_sanctions**:  
- Only two papers involve punishment. Lee et al. (2022) is **exact** (punishment), while Lv & Song (2022) is **exact** for punishment mechanisms (though only adjacent to payoff outcomes). Hua & Liu (2024) is **none** (no punishment, only reward mechanisms).

**efficiency_or_related_payoff_outcome**:  
- Lee et al. (2022): **exact** (efficiency is primary outcome).
- Hua & Liu (2024): **exact** (efficiency/welfare as group payoff outcome).
- Lv & Song (2022): **adjacent** (does not measure efficiency/payoff directly; cooperation/investment rates are tracked).

Collectively, only one paper (Lee et al., 2022) is **exactly** relevant across all three target criteria (PGG, punishment, payoff/efficiency), while the others are either adjacent or off-target for punishment or efficiency, limiting the breadth of decisive evidence for the targeted prediction task.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes (efficiency, group payoff, welfare, surplus, coins generated):**
- **Lee et al. (2022):** Models and reports on group efficiency and total payoff under varying punishment costs and fines in spatial PGGs.
- **Hua & Liu (2024):** Reports group welfare outcomes in relation to reward schemes (no punishment angle).
- **Lv & Song (2022):** Does **not** report payoff or efficiency—only rates of cooperation and allocation to cooperation/punishment.

**Non-payoff behavioral outcomes (contribution/cooperation rate, punishment frequency, etc.):**
- **Lv & Song (2022):** Focuses exclusively on cooperation rates and investment allocation.
- **Lee et al. (2022):** Also discusses strategy abundances (proportion of cooperators, defectors, punishers) and spatial patterns, though these are secondary to payoff outcomes.
- **Hua & Liu (2024):** Behavioral outcomes are implicit in dynamics but not directly the focus.

**Distinction:** Across the set, only one study (Lee et al., 2022) supplies direct evidence on efficiency change due to punishment; others offer support only for mechanisms (cooperation) or alternative interventions (reward).

# 4) Main Findings Relevant To Prediction

- **Punishment Effects (Lee et al., 2022):**  
  Introducing peer punishment in a spatial PGG environment can increase group efficiency (measured as proportion of maximum possible group payoff), but this is contingent on the *cost* of punishment not being too high and the *fine* (punishment intensity) being substantial. There is a non-linear relationship—efficiency peaks at an optimal punishment cost, with both very low and very high costs leading to lower efficiency. If an additional "tax" is used to support punishers, the regime of high efficiency can be extended, but only when punishment is costly and fines are large; for low fines, the tax may worsen outcomes for cooperators.

- **Mechanism and Sensitivity (Lv & Song, 2022):**  
  The effect of punishment on cooperation rates (not efficiency) is highly sensitive to punishment intensity and social learning parameters. Higher punishment intensity doesn't always maximize cooperation, suggesting complex, parameter-dependent effects on both strategy adoption and resource allocation to punishment versus cooperation—these may translate into ambiguous efficiency effects, but the paper does **not** measure efficiency or group payoff directly.

- **Reward-Only Comparison (Hua & Liu, 2024):**  
  Adaptive institutional reward mechanisms can stabilize cooperation and high welfare under threshold conditions, but the paper contains **no evidence** on punishment's effect.

# 5) Prediction Guidance

The primary guidance available for predicting efficiency with peer punishment enabled—given control efficiency—is theoretical and parameter-dependent. **Lee et al. (2022)** suggests:
- Enabling peer punishment will tend to improve group efficiency compared to no-punishment control **if** punishment is not too expensive for punishers and the magnitude of punishment per unit (fine) is sufficient.
- There is an **optimal region** where punishment cost balances deterrence versus punisher burdens; both low and excessively high costs can fail to maximize efficiency.
- If the punishment cost is high, an institutional subsidy ("tax" supporting punishers) can expand the region of high efficiency—but this may backfire if fines are not sufficient.
- If punishment is weak or costly, or if strategic interactions generate cyclic dominance (between contributors, defectors, and punishers), efficiency gains may not materialize and may even reverse.

**No guidance emerges for games with chat, identity exposure, reward presence in combination with punishment, or real versus continuous contribution protocols, as these are not empirically nor theoretically targeted.**

**Control efficiency is a useful baseline**: the *marginal effect* of adding punishment relates to how much room there is for improvement in the no-punishment baseline, and how the punishment parameters interact.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed:**
- `player_count` (group size): Theoretical models in both punishment and reward studies vary the group size, influencing efficiency and threshold effects (Lee et al., 2022; Hua & Liu, 2024).
- `num_rounds`: Modeled in spatial dynamics (Lee et al., 2022; Lv & Song, 2022).
- `all_or_nothing`: Both all-or-nothing and continuous versions considered (Lee et al., 2022; Lv & Song, 2022).
- `mpcr`: Marginal per-capita return is a key structural parameter in all three studies.
- `punishment_cost` and `punishment_tech`: Critical in Lee et al. (2022) and modeled in Lv & Song (2022).
- `reward_exists`, `reward_cost`, `reward_tech`: Covered in Hua & Liu (2024) only (reward, not punishment).

**Indirectly or sparsely informed:**
- `default_contrib` (framing): Not mentioned in any study.
- `chat`: Not discussed.
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Not modeled.
- `reward_exists` and related dimensions: Only addressed in the reward context, not in combination with punishment.

**Effectively missing:** Social communication (`chat`), framing/defaults, and information exposure (summary/identity) are not covered, and thus their impacts remain unknown in this literature.

# 7) Important Limitations

- **Theoretical Only:** All findings are derived from mathematical models—no laboratory or field data are present. This restricts confidence in external validity, especially regarding human behavior or parameter non-idealities.
- **Spatial Assumptions:** Results are for spatially structured populations, which may not generalize to well-mixed groups or other PGG implementations.
- **Limited Dimensional Coverage:** Critical design features relevant for field or lab settings (e.g., chat, exposure, framing, reward-punishment combinations) are not represented.
- **Mechanism vs. Outcome:** Except for Lee et al. (2022), most findings pertain to cooperation rates, not directly to efficiency or group payoff. Even Lee et al.'s results rest on model assumptions about strategic updates and payoffs.
- **Parameter Sensitivity:** The predicted benefit of punishment is highly sensitive to the precise cost, fine, and (if implemented) tax/subsidy rates, with non-monotonicity possible. No "one size fits all" guidance is supported.
- **No Cross-validation:** The absence of empirical validation means that model-predicted optimal regions may not occur in practice, especially under unmodeled behavioral or institutional factors.

**In summary:**
The available literature offers strong theoretical (but not empirical) support that enabling punishment can increase group efficiency relative to no-punishment baselines, but only in a specific region of design space (moderate costs and adequate fines). For most design dimensions, either no evidence or only context-specific, indirect insights are available. Predictions about the effect of peer punishment on efficiency should be made cautiously, with explicit attention to the parameter regime, and with the understanding that key design and behavioral factors are absent from this corpus.
