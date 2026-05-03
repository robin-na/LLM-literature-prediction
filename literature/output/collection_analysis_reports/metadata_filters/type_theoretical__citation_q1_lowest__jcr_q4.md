# 1) Evidence Base

The paper set is exclusively **theoretical**—all 23 sources propose formal models or conceptual arguments, with no empirical or experimental work represented. The set is **broad in conceptual coverage**, encompassing exact public goods games (PGG), adjacent games (e.g., repeated Prisoner’s Dilemma, threshold games, team production), and broader evolutionary accounts, but it is **narrow** in that it lacks empirical calibration and contains no direct experimental measurements. Regarding sanctions, the scope includes both peer and institutional punishment, as well as related mechanisms (rewards, contract incentives, walk-away/partner choice, and communication). The outcomes span efficiency or related payoffs for many theories, though some focus on behavioral markers alone.

# 2) Task Relevance

**pgg_or_variant:**  
- **exact:** Several papers present models exactly of PGGs or optional PGGs, including analyses of punishment mechanisms and efficiency (e.g., Alventosa & Olcina, 2021; Botta et al., 2021; Ishikawa & Fontanari, 2025; Eldakar et al., 2018; Spitzer, 2016).
- **close/adjacent:** Many use adjacent paradigms with strong mapping to PGGs, such as the repeated Prisoner’s Dilemma (e.g., Gioffré & Tampieri, 2025; Annen, 2011; Kurokawa, 2022), volunteer’s dilemmas, and shirker’s dilemmas.
- **weak/none:** Several are about trust/investment games or social norm models lacking group settings or punishment.

**punishment_or_sanctions:**  
- **exact:** Core subset directly analyze punishment mechanisms in PGGs or direct analogs (centralized or peer; action- vs outcome-based).
- **adjacent:** Some analyze reward, partner choice, contracts, norm enforcement, or communication in lieu of punishment.
- **none:** A fraction lack any model or analysis of punishment/sanctions.

**efficiency_or_related_payoff_outcome:**  
- **exact:** About half analyze efficiency, group welfare, surplus, or total payoff effects as primary outcomes.
- **close/adjacent:** Some focus on equilibrium existence, stability, or likelihood of cooperation, implying payoff-based consequences but without explicit efficiency measures.
- **weak/none:** Several measure or discuss only non-payoff markers (e.g., contribution rates, norm compliance, strategy frequencies).

# 3) Outcomes Measured In The Literature

- **Payoff/Efficiency outcomes** (group payoff, efficiency, welfare, surplus):
    - *Primary focus*: Most “exact” and “close” theory models, especially those on institutional/peer punishment in PGG or analogous environments, use group payoff or efficiency as core criteria (e.g., Alventosa & Olcina, 2021; Botta et al., 2021; Ishikawa & Fontanari, 2025; Friehe & Tabbach, 2018; Gioffré & Tampieri, 2025; Annen, 2011; Uchida et al., 2024; Skarzhinskaya & Tsurikov, 2021).
- **Non-payoff behavioral outcomes** (cooperation rate, punishment frequency, norm compliance, strategy stability):
    - *Secondary focus*: Several models ground conclusions in the stability or equilibrium rate of cooperative strategies, or in the effect of punishment on maintaining cooperation, sometimes inferring efficiency implications, but not always measuring total payoff explicitly (e.g., Zhao & Zou, 2025; Eldakar et al., 2018; Jones, 1999).  
    - Some purely discuss motives, mechanisms, or conditions for behavior, not outcomes (e.g., Golman, 2016; Spitzer, 2016).

# 4) Main Findings Relevant To Prediction

**Empirical claims are absent** (no measured treatment–control efficiency deltas); claims are mechanistic/theoretical:

- **Punishment generally improves efficiency, conditional on cost/effectiveness:**  
    - *Peer and Institutional*: Models show that adding punishment can shift equilibrium from low to high efficiency, particularly if punishment is strong and/or aligned with group interests (Alventosa & Olcina, 2021; Botta et al., 2021; Gioffré & Tampieri, 2025; Friehe & Tabbach, 2018; Uchida et al., 2024).
    - *Thresholds are common*: High punishment cost, ineffective technology, or unfavorable cost/benefit ratios may prevent efficiency gains (Ishikawa & Fontanari, 2025; Gioffré & Tampieri, 2025; Uchida et al., 2024).
- **Structural moderators:**  
    - *Player count/group size*: Larger groups may require stronger or more effective punishment to achieve gains (Annen, 2011; Peña et al., 2024). In threshold games, larger groups can decrease efficiency in the absence of punishment.
    - *Punishment technology/cost*: Efficiency improvements are larger when punishment is more effective (high fine/low cost) (Alventosa & Olcina, 2021; Botta et al., 2021; Ishikawa & Fontanari, 2025).
    - *Power and institutional alignment*: Efficiency gains are maximized when the sanctioning institution reflects the interests of the general group, not a selfish minority (Alventosa & Olcina, 2021; Eldakar et al., 2018).
    - *Equilibrium multiplicity and initial conditions*: Multiple stable states exist—punishment **can** raise efficiency but may not unless system starts in a favorable state or all actors coordinate (Ishikawa & Fontanari, 2025; Uchida et al., 2024).
    - *Behavioral moderators*: Prospect-theoretic biases can make weak or infrequent punishment more effective (Uchida et al., 2024).
- **Design details matter:**  
    - Action-based punishment is typically superior to outcome-based for driving efficiency (Friehe & Tabbach, 2018).
    - Communication, rewards, coalition contracts, and partner choice can serve as substitutes or complements to punishment (Skarzhinskaya & Tsurikov, 2021; Golman, 2016; Kurokawa, 2022; Lütz et al., 2023), but their payoff effects may differ.

**Disagreement/Ambiguity:**  
- Some models highlight scenarios where punishment can be ineffective, counterproductive, or lead to partial (not maximal) efficiency—especially with collective punishment, high cost, misaligned institutions, or severe power asymmetry (Bolle, 2021; Eldakar et al., 2018; Ishikawa & Fontanari, 2025).

# 5) Prediction Guidance

- **Predicted direction of effect:**  
    **When punishment is enabled (relative to control), group efficiency is predicted to increase**, often substantially, provided punishment cost is not too high, effectiveness is sufficient, and group/institutional alignment is present.
- **Dependence on design dimensions:**  
    - **Direct evidence:** The following prediction dimensions are **directly modeled and shown as important moderators**: `player_count`, `num_rounds` (repeated vs one-shot), `all_or_nothing`, `mpcr`, `punishment_cost`, `punishment_tech`. **High values of MPCR, strong/low-cost punishment, and repetition favor greater efficiency gains.**
    - **Indirect or sparse evidence:** Little to no theory on the effects of `chat`, `default_contrib`, `reward_exists/cost/tech`, or the details of summary and ID display (`show_n_rounds`, `show_other_summaries`, `show_punishment_id`). Some mechanisms (`reward_exists`, communication) are discussed contextually; their direct effect on efficiency with punishment is unquantified.
    - **Adjacent mechanisms (partner choice, contracts):** In systems enabling these, efficiency may rise even without punishment, setting a higher baseline; the marginal efficiency boost from adding punishment may thus be less dramatic in these contexts.
- **Control efficiency as a baseline:**  
    Where the no-punishment (control) game is close to zero efficiency, enabling effective punishment can—in theory—yield large efficiency increases, possibly up to the full-cooperation optimum. If control efficiency is already high due to other design elements, the gain from punishment may be smaller.
- **Conditionality:**  
    If punishment is weak, costly, collective (rather than peer-based), or misaligned, efficiency gains can be minor or even negative, depending on free-riding by punishers or institutional excess.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**
- `player_count`: Modeled as a moderator; larger groups can dilute punishment effect or raise coordination thresholds.
- `num_rounds`: Critical for models of repeated interaction; more rounds generally support punishment effectiveness.
- `all_or_nothing`: Distinction between binary and continuous contributions is theorized (many all-or-nothing models).
- `mpcr`: Universally modeled as the payoff multiplier; dictates cost/benefit of cooperation.
- `punishment_cost`, `punishment_tech`: Central moderators of punishment effectiveness and thus efficiency impact.

**Indirect or Partial Evidence:**
- `reward_exists`, `reward_cost`, `reward_tech`: Occasionally modeled (often as analogs or complements to punishment), but less is said about their interaction with punishment.
- `chat`: Considered theoretically as a potential substitute for punishment under signaling motives, but payoff effects not modeled.
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Little or no direct modeling. Some models allow for reporting/information differences (`show_other_summaries`) impacting punishment credibility or truthfulness.

**Contextually Mentioned or Missing:**
- `default_contrib`: Not directly theorized in any model.
- Details of feedback displays or identity salience have minimal or no direct theoretical attention.

# 7) Important Limitations

- **No empirical or experimental data**: The set contains theoretical work only—no parameterized effect sizes, real-world heterogeneity, or variance estimates.
- **Generalizability to peer punishment limited**: Several core models focus on **institutional punishment** (centralized, 'pool') rather than direct peer-to-peer sanctions; classic experimental PGGs use peer punishment.
- **Behavioral effects inferred, not measured**: For some adjacent models, inferences about efficiency are made via effects on cooperation or stability, not directly on group payoff.
- **Sparse coverage of certain design features**: Key real-world features (communication, feedback, framing, reward integration) are rarely detailed or are only contextually modeled, reducing direct prediction fidelity.
- **Equilibrium multiplicity and practical feasibility**: Many models show that both high- and low-efficiency equilibria can coexist; practical group trajectory may depend on initial conditions, learning, and bounded rationality, which are unmodeled.
- **Ambiguous or mixed effects in special cases**: Collective punishment, high cost, concentration of power, or certain forms of outcome-based policy may not yield efficiency gains and can, in special cases, reduce group welfare.
- **No direct modeling of all 14 dimensions in unison**: No paper systematically varies or cross-models all prediction dimensions relevant to real experimental designs.
- **Adjacent-case transferability issues**: Where models treat repeated PD, team production, or other adjacent games, mapping findings exactly to PGGs with peer punishment introduces uncertainty.
- **Ambiguity in non-payoff measures**: Some models conflate stable cooperation with efficiency, but total group payoff and efficiency may diverge under differential costs or incentives.

---

**In conclusion:** The literature base provides **robust theoretical support** for the conditional prediction that enabling punishment increases average efficiency in PGG-like environments—provided the punishment regime is effective and aligned. The size of the efficiency gain depends on structural parameters well-captured in several prediction dimensions, although important gaps in design features and the absence of empirical data limit the direct applicability and quantitative precision of predictions.
