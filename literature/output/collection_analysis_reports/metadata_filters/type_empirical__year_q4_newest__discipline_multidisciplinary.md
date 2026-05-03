# 1) Evidence Base

The paper set comprises 51 studies, with the bulk being empirical lab experiments focused on economic games—primarily public goods games (PGGs) and their close variants. Most evidence is derived from highly controlled laboratory settings, frequently using standard PGG protocols or near relatives (e.g., variants of the Prisoner's Dilemma or Dictator Game with punishment/reward options). A minority of studies contribute theory or mechanism arguments, but these too are generally tested empirically.

A significant number of papers measure only behavioral outcomes (e.g., contributions, punishment decisions), while a substantial subset report payoff-based outcomes, including group efficiency, welfare, and total earnings. The paper set is relatively broad regarding PGG variants and sanctioning mechanisms, but direct high-quality evidence on treatment efficiency (the core downstream outcome) is more limited and often confined to canonical game parameterizations. Many papers address moderators or mechanisms—such as group structure, punishment design, or context effects—rather than providing comparable estimates across the full range of design dimensions relevant for prediction.

# 2) Task Relevance

**pgg_or_variant**  
- *Relevance*: Many papers are of **exact** relevance, centered on repeated PGGs where peer punishment is a main treatment; a smaller set are **close** variants (e.g., threshold PGGs, networked PGGs, or social dilemmas with similar cooperation dilemmas). Several others are **adjacent** (e.g., Prisoner's Dilemma, Dictator Game with punishment, or non-PGG social dilemmas), and a portion are **none**.
- *Synthesis*: The literature directly covers repeated PGGs with and without punishment, but for more atypical design configurations (e.g., nonstandard group sizes or novel punishment forms), evidence is sparser.

**punishment_or_sanctions**  
- *Relevance*: About half of the studies are of **exact** relevance, directly manipulating the presence or design of punishment or sanctioning mechanisms. Some are **adjacent**, focusing on related behaviors (reputation, exclusion, rejection) but without formal punishment options. Studies with only baseline PGGs (no punishment) are **none** for this dimension.
- *Synthesis*: The literature provides strong coverage for classic peer punishment, with supplemental insights into variations such as noisy punishment, third-party punishment, profit-motivated punishment, and alternative enforcement systems.

**efficiency_or_related_payoff_outcome**  
- *Relevance*: Robust **exact** coverage is limited; only a subset of papers directly measure and analyze group efficiency or payoff as a function of punishment (e.g., Lo Iacono et al., 2023; Salahshour et al., 2022; Molenmaker et al., 2023; DeCaro et al., 2024; Köster et al., 2022). Many otherwise-relevant studies report only **adjacent** outcomes (contribution rates, norm compliance) or provide payoff data only descriptively.
- *Synthesis*: Direct empirical findings on the key prediction outcome (payoff-based efficiency) under varying design dimensions are relatively rare, and evidence is often for a limited set of settings, with much inference requiring cautious extrapolation from non-payoff outcomes.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes**:
- **Efficiency**, group payoff, average/group earnings, welfare, or resource surplus—directly measured in a subset of PGG experiments (e.g., Lo Iacono et al., 2023; Salahshour et al., 2022; Molenmaker et al., 2023; Köster et al., 2022; DeCaro et al., 2024; Romano et al., 2024).
- Descriptive or summary statistics on total payoffs or net tokens (sometimes provided without formal analysis).

**Non-payoff (behavioral) outcomes**:
- **Contribution rate**, cooperation frequency, convergence (ICC), or change in collective behavior (most common outcome).
- **Punishment frequency/intensity**, norm compliance, emotional responses, or trust.
- Social or psychological constructs (e.g., legitimacy, trust, reputation, emotion expression).

**Distinction**: Many studies focus on behavioral outcomes, sometimes inferring likely effects on efficiency, but very few directly test the impact of punishment on realized efficiency or explicitly connect contribution increases to payoff increases under real cost structures.

# 4) Main Findings Relevant To Prediction

- **Peer punishment in standard repeated PGGs**: Enabling peer punishment typically increases group efficiency (payoff relative to full cooperation) over control in highly controlled, canonical settings, especially if the punishment regime is well-calibrated (e.g., cost-to-impact ratio of 1:3) (Lo Iacono et al., 2023).
- **Design-specificity**: Most robust efficiency gains from punishment are observed where group size, MPCR, and punishment parameters match classic setups. Extrapolation outside these settings (e.g., higher noise, different cost ratios, or group structure) is poorly constrained by direct data.
- **Punishment regime quality**: The effectiveness of punishment for efficiency depends heavily on its implementation:
    - **Deterministic vs. noisy punishment**: High noise in punishment effectiveness sharply reduces or negates gains in efficiency (Salahshour et al., 2022).
    - **Group homogeneity**: Punishment reliably increases efficiency only in homogenous groups; in pluriform groups, it can be discriminatory and reduce efficiency (Molenmaker et al., 2023).
    - **Punishment design**: Punishment that's not personally costly or is profit-driven can reduce efficiency; free-to-punisher or profitable third-party punishment destabilizes or harms group outcomes (Rodrigues et al., 2024; Alam & Rai, 2025).
    - **Legitimacy and coordination**: Well-facilitated or perceived legitimate punishment regimes (with communication, justice procedures, or coordinated enforcement) have larger, more persistent positive effects on efficiency than poorly-designed or corrupt regimes (DeCaro et al., 2024; Dickson et al., 2022).
    - **Antisocial/discriminatory or attack-based punishment options** strongly risk reducing efficiency, especially under conditions of group heterogeneity, resource scarcity, or status competition (Romano et al., 2024).
- **Behavioral vs. payoff outcomes**: Many studies confirm that punishment can increase contributions, but efficiency often rises less or not at all because of offsetting costs (Ozono & Nakama, 2022).
- **Boundary conditions**: The positive effect of punishment can be fragile—vanishing or reversing with slight changes to game design (e.g., increased punishment noise, allowance for profitable punishment, negative group structure effects).

# 5) Prediction Guidance

This literature provides the strongest support for positive effects of peer punishment on group efficiency in standard, tightly controlled PGGs featuring:
- Moderate to high group size,
- Many rounds,
- Continuous contributions,
- Non-trivial but not excessive punishment costs (e.g., 1:3 cost/impact ratio),
- Homogenously composed groups,
- Deterministic, transparent punishment mechanisms, and
- Facilitation, communication, and/or procedural legitimacy.

For the downstream prediction task:
- **If the control game shows high baseline efficiency and the punishment-enabled treatment closely matches canonical experimental designs, prediction of positive gains in efficiency is well-supported (Lo Iacono et al., 2023; Köster et al., 2022).**
- **Efficiency effects are likely to be much smaller, or even negative, whenever:**  
    - Punishment is noisy or stochastic (Salahshour et al., 2022)
    - The group is heterogeneous in salient social characteristics (Molenmaker et al., 2023)
    - Punishment is profitable or not personally costly (Alam & Rai, 2025; Rodrigues et al., 2024)
    - Antisocial punishment is substantial (not ruled out by design)
    - Coordination, communication, or legitimacy is undermined (DeCaro et al., 2024; Dickson et al., 2022)
    - Attack/contest options are present, especially under scarcity or status stress (Romano et al., 2024)
- **Behavioral increases in contribution do not always translate into efficiency gains**—especially when punishment imposes excessive costs or is misdirected.

Given the limited direct evidence on many prediction dimensions, when control efficiency is known:
- **Prediction should adjust for moderators captured in the design—especially punishment quality, group homogeneity, noise, and the presence of mechanisms supporting legitimate and coordinated punishment.**
- When little is known about these, or design dimensions differ substantially from the canonical, predictions should be regarded as weak or highly uncertain.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed by multiple papers**:
- `player_count`, `num_rounds`, `mpcr`, `all_or_nothing`, `punishment_cost`, `punishment_tech`: Directly addressed in multiple studies, especially in those comparing baseline and punishment-enabled settings (Lo Iacono et al., 2023; Salahshour et al., 2022; Molenmaker et al., 2023; DeCaro et al., 2024).
    - Variations in these are usually tightly controlled; direct evidence about their moderation of efficiency effects is rare (most papers fix parameters).
- `chat`, `show_other_summaries`, `show_punishment_id`: Examined as additional features in some papers, influencing coordination, legitimacy, or convergence (DeCaro et al., 2024; Nielsen & Pfattheicher, 2024).
- `punishment_exists`: Central to all studies meeting core relevance.

**Indirectly or contextually informed**:
- `default_contrib`: Occasionally manipulated (Ozono & Nakama, 2022) but rarely central.
- `show_n_rounds`, `group composition (not strictly analogous to dimensions above)`: Informative as moderating variables (Molenmaker et al., 2023).

**Sparse or missing**:
- `reward_exists`, `reward_cost`, `reward_tech`: Direct comparisons to rewards are rare; most focus on punishment alone (a few exceptions: Makovi et al., 2025).
- **Design interaction effects** (e.g., between chat and punishment, or between visibility and punishment) are discussed anecdotally but rarely directly tested for efficiency outcomes.
- **Novel punishment mechanisms or less common technical features** (e.g., virtual vs. face-to-face, endogenous institution choice, punishment profit-structures) are less thoroughly mapped; extrapolation is risky.

# 7) Important Limitations

- **Direct evidence for the key outcome—treatment efficiency conditional on control efficiency and precise design dimensions—is available from only a handful of studies**, mostly for canonical PGG designs.
- **Most studies do not experimentally vary multiple design dimensions**; generalization to novel or nonstandard settings is therefore weakly supported.
- Where **efficiency is not measured**, inferences must be cautious: high contributions do not guarantee higher efficiency if punishment is costly or misapplied.
- **Antisocial, discriminatory, or profit-motivated punishment can easily undermine or reverse punishment’s expected efficiency gains**—and many real-world or even experimental group structures may evoke these conditions.
- Moderator and mechanism evidence (e.g., legitimacy, coordination, group composition) is typically evaluated via non-payoff outcomes or qualitative description, not always by direct efficiency measures.
- The **impact of reward mechanisms, combined sanctioning/reward systems, or dynamic group entry/exit** on efficiency under punishment is rarely tested in tandem with punishment treatments.
- **Contextual factors** (culture, sample composition, online vs. lab) can moderate effects but are not systematically mapped onto efficiency outcomes.
- **Prediction for out-of-sample, high-dimensional, or multi-modal game designs remains speculative and should be labeled as such**.

---

**In summary**, the most robust evidence supports moderate positive efficiency effects of enabling well-designed, coordinated, and properly-calibrated peer punishment in canonical repeated PGGs among homogeneous groups. Effects are attenuated or even reversed under noisy, discriminatory, profitable, or poorly-coordinated punishment regimes, with many design dimensions only weakly or indirectly mapped. Extrapolations beyond standard settings should be made with explicit acknowledgment of large uncertainties.
