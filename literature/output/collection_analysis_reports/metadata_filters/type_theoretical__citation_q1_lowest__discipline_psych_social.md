## 1) Evidence Base

The paper set analyzed here consists exclusively of theoretical works—no empirical or experimental papers are included. The coverage is relatively broad both in terms of the exactness of the public goods game (PGG) environments, the diversity of punishment and sanctioning structures, and the degree to which efficiency or related payoff-based outcomes are directly analyzed. However, the range of game structures extends from exact PGGs to closely adjacent and more distant social dilemma or collective action games, including variants of Prisoner's Dilemma, volunteer's dilemma, common-pool resource games, and coordination games. The set features in-depth formal modeling, simulation, and qualitative mechanism argumentation, but lacks real-world or experimental effect size estimates.

## 2) Task Relevance

**pgg_or_variant:**  
- Relevance is high: Many papers are exact to close variants of PGGs (Tanimoto, 2018; Botta et al., 2021; Kroupa, 2014; Eldakar et al., 2018; Odouard et al., 2023), while others use adjacent game structures (Prisoner's Dilemma, threshold public goods, volunteer's dilemma), allowing for informed inferences.

**punishment_or_sanctions:**  
- Relevance is also high: All papers model punishment (peer or institutional), sanctions, or enforcement mechanisms in a directly relevant way, though the type, scope (peer/institutional/third-party), and targeting of punishment differ by study.

**efficiency_or_related_payoff_outcome:**  
- Mixed relevance: Some papers analyze efficiency or group payoff directly and explicitly (Tanimoto, 2018; Botta et al., 2021; Kroupa, 2014; Asgharpourmasouleh et al., 2017; Heller & Sieberg, 2008), some focus on adjacent outcomes (cooperation rate, norm compliance, behavioral transitions), and others analyze payoff only indirectly or contextually.

This set is well-suited for developing qualitative and theoretical prediction guidance but does not offer empirical effect sizes or model estimates suitable for direct plug-in prediction.

## 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (exact or close):**  
  - Efficiency (group payoff as proportion of maximum possible, group welfare, average surplus) is reported or explicitly modeled in several papers (e.g., Tanimoto, 2018; Botta et al., 2021; Asgharpourmasouleh et al., 2017; Heller & Sieberg, 2008; Gioffré & Tampieri, 2025).  
  - Total earnings, group-level welfare, or surplus are sometimes used as functional equivalents to efficiency.

- **Non-payoff behavioral outcomes:**  
  - The large remainder of the literature uses contribution rate, cooperation rate, norm compliance, punishment or enforcement rate, and norm stability as primary outcomes (Odouard et al., 2023; Ogaki & Tanaka, 2017; Zachník, 2023; Kido & Takezawa, 2024). These are closely linked to payoffs but are not identical to efficiency and must be interpreted cautiously.
  - Many mechanism papers focus on how punishment, communication, power asymmetries, or reputation alter cooperation rates, with less direct attention to net payoffs after accounting for punishment costs.

- **Ambiguity/Indirection:**  
  - Several papers (especially those with adjacent relevance) primarily discuss efficiency-related outcomes through implied or indirect reasoning about cooperation rates, norm internalization, or enforcement dynamics.

## 4) Main Findings Relevant To Prediction

### General Pattern
- **Mixed effect of punishment:**  
  - The effect of enabling punishment on efficiency (relative to the no-punishment control) is highly context-dependent.
  - **Punishment reliably increases cooperation or compliance rates** in a wide range of models (Tanimoto, 2018; Botta et al., 2021; Ogaki & Tanaka, 2017), but only increases group efficiency when punishment costs are low or punishment is well-targeted and not misapplied (Tanimoto, 2018; Kroupa, 2014; Heller & Sieberg, 2008).
  - **Costly punishment can reduce group efficiency** even as it increases cooperation, especially in short, anonymous, or highly costly environments (Tanimoto, 2018; Kroupa, 2014; Antoci & Zarri, 2015).

### Moderators Identified Across Papers
- **Punishment cost and effectiveness:**  
  - When punishment has a high cost-to-impact ratio, group payoff (efficiency) may decline even as cooperation rises (Tanimoto, 2018; Antoci & Zarri, 2015; Heller & Sieberg, 2008).
  - Efficient punishment (low cost, high impact) more reliably raises both cooperation and efficiency (Tanimoto, 2018; Botta et al., 2021).
  - The threshold for punishment effectiveness (e.g., minimum fraction of defectors punished) is critical for stabilizing cooperative, efficient equilibria (Botta et al., 2021; Gioffré & Tampieri, 2025).

- **Game design dimensions:**
  - **Player count & group structure:** Larger groups can enhance the potency of institutional punishment or community enforcement, provided credible reporting and monitoring are possible (Annen, 2011; Gioffré & Tampieri, 2025).
  - **Number of rounds / iteration:** Longer repeated games or those with uncertain or infinite horizon make punishment more effective at sustaining high-efficiency equilibria (Kroupa, 2014; Corriveau, 2012; Evans & Thomas, 2001; Jones, 1999).
  - **Communication, reputation, and transparency:** The presence of communication or reputation mechanisms synergizes with punishment to support higher efficiency (Kroupa, 2014; Vincent, 2017). Anonymous or non-communicative games see lower efficiency when punishment is enabled.
  - **Institutional structure (peer vs. central punishment):** Centrally organized or institutionally enforced punishment mechanisms are more effective at producing stable high-efficiency equilibria, especially in large groups; peer punishment is more vulnerable to second-order free riding, power asymmetries, or retaliation (Prétôt et al., 2024; Eldakar et al., 2018).
  - **Network/structural features:** Heterogeneous networks or opportunities for targeted punishment/coalition formation further moderate the effect (Tanimoto, 2018; Skarzhinskaya & Tsurikov, 2021).
  - **Presence of rewards:** Models allowing selective rewards in addition to punishment can have more stable efficient equilibria, though improperly structured rewards can undermine punishment or efficiency (Antoci & Zarri, 2015; Skarzhinskaya & Tsurikov, 2021).

- **Behavioral/cognitive moderators:**  
  - Norm internalization, psychological biases (e.g., overweighting probability of punishment), and the distribution of social power modulate the effectiveness of punishment (Odouard et al., 2023; Uchida et al., 2024; Eldakar et al., 2018).

### Limits, Counterexamples, and Caveats
- **Punishment can decrease efficiency in the presence of:**  
  - High punishment costs (Kroupa, 2014).
  - Short or finite games where retaliation is possible (Rumble & Thomas, 2022).
  - Misapplied, antisocial, or parochial punishment (dos Santos & Knoch, 2021; Hernandez et al., 2022).
  - Lack of second-order punishment (if only defectors are punished and not those who fail to punish defectors) (Antoci & Zarri, 2015).

## 5) Prediction Guidance

- **Efficiency with punishment (relative to control) should be predicted as a positive function of:**
  - Low punishment cost per unit impact (`punishment_cost`, `punishment_tech`).
  - Sufficiently long or repeated game structure (`num_rounds`).
  - The possibility for communication or signaling (`chat`, `show_other_summaries`).
  - The presence of centralized or collectively funded punishment, especially with mechanisms to prevent second-order free riding.
  - Control efficiency: if baseline (no-punishment) efficiency is low, the marginal effect of punishment is often higher, provided costs are not prohibitive (Asgharpourmasouleh et al., 2017).

- **Efficiency gains are attenuated or negative when:**
  - Punishment is costly, misapplied, or prone to antisocial/perverse use.
  - The environment is short, anonymous, or structurally facilitates retaliation (Kroupa, 2014; Rumble & Thomas, 2022).
  - Power is highly asymmetric, enabling selfish punishers (Eldakar et al., 2018).
  - Only peer/individual punishment is available and monitoring is not collective (Prétôt et al., 2024).
  - Antisocial punishment or lack of second-order enforcement (failing to punish non-punishers) undermines the incentive for cooperation (Antoci & Zarri, 2015).

- **Dimension-level mapping:**  
  - Where control efficiency is high (already near maximum), the possible positive marginal effect of punishment is smaller and could even be negative if punishment costs are substantial.
  - Theoretical phase diagrams and thresholds (Botta et al., 2021; Gioffré & Tampieri, 2025) can guide identification of parameter regimes where punishment has large effects versus where it is inefficient or unnecessary.

- **Ambiguity and Disagreement:**  
  - No universally positive effect: Several models find both positive and negative efficiency changes depending on parameterization.
  - Non-monotonic effects: More severe punishment may backfire and reduce efficiency by crowding out voluntary cooperation (Hernandez et al., 2022; Antoci & Zarri, 2015).
  - Some models highlight path dependency and multiple equilibria—efficiency can be low or high depending on initial group state and parameterization (Whitmeyer, 2004; Jones, 1999).

## 6) Design Dimensions Highlighted Across Papers

**Most directly informed dimensions:**
- `player_count` (group size): Frequently modeled, directly moderating punishment efficacy and equilibrium structure.
- `num_rounds`: Key for sustaining cooperation and efficiency improvements via punishment; longer repeated games yield better outcomes.
- `punishment_cost`, `punishment_tech`: Core drivers of whether punishment is effective or efficient (cost-to-impact ratio, efficiency of punishment).
- `mpcr` (marginal per capita return): Often included, moderating the inherent social dilemma strength.
- `all_or_nothing`: Many models explicitly address binary (all-or-nothing) versus continuous choices.
- `show_other_summaries`, `show_n_rounds`: Shown to influence monitoring and information transmission in some models.
- `chat`: Communication's presence is highlighted as a critical moderator.
- `reward_exists`, `reward_cost`, `reward_tech`: Models including rewards or hybrid incentive mechanisms are present, but less frequently than punishment.

**Indirectly or contextually discussed:**
- `default_contrib`: Few direct findings, but influence is implied via baseline norms or frames.
- `show_punishment_id`: Less commonly modeled, but relevant for social enforcement structure.
- Peer vs. institutional enforcement is a pervasive contextual theme.

**Effectively missing or only peripherally addressed:**
- No explicit findings on `default_contrib` (opt-in/opt-out framing), nor granular manipulation of summary displays or other subtle framing effects.
- Sparse discussion on non-punishment idiosyncratic summary or information arrangements.

## 7) Important Limitations

- **Absence of empirical data:** The set is entirely theoretical; findings are not directly validated on laboratory or field data and do not offer real-world effect size estimates.
- **Payoff vs. behavioral outcome conflation:** Many papers infer about efficiency from cooperation rates or norm compliance but lack direct payoff aggregation, making the translation to efficiency somewhat inferential.
- **Parameter regime ambiguity:** Some models show strong positive or negative effects of punishment on efficiency under different (sometimes unobservable) parameterizations (punishment cost, group power asymmetry, degree of institutionalization, etc.).
- **Generalizability:** High model specificity; even exact PGG formalizations abstract away real-world noise, learning dynamics, or context. Some results (Grim Trigger, draconian punishment equilibria) may be unrealistic in finite-horizon/lab games.
- **Missing dimensions:** Not all 14 game design variables are fully represented, and interdependencies are incompletely mapped.
- **Mechanism overestimation:** Theoretical models sometimes show greater efficiency gains for idealized punishment mechanisms than seen in empirical or experimental studies.
- **No treatment effect baselines:** Theories often assume a zero-efficiency baseline. Predictive application requires mapping to observed control efficiency, which may attenuate the marginal effect of punishment.
- **Disagreement:** Substantial cross-paper ambiguity (e.g., cost of punishment, antisocial punishment, role of communication).

---

**In summary:**  
This theoretical paper set robustly supports the general mechanism whereby enabling (peer or institutional) punishment in PGG-like environments can increase cooperation rates and, contingent on low punishment cost and enabling institutional features, increase efficiency. However, the efficiency impact is not universally positive; high-cost, misapplied, or purely peer-based punishment can reduce efficiency. The most relevant game design dimensions for prediction are group size, repetition, punishment cost/tech, communication, and enforcement structure. The lack of empirical data, diversity of model structures, and gaps in dimensional coverage require cautious and context-dependent extrapolation for downstream prediction tasks (e.g., predicting average group efficiency under punishment, given control efficiency and game parameters). The literature soundly cautions against assuming monotonic or universal positive effects from enabling punishment.
