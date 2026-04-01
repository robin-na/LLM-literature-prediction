# 1) Evidence Base

The paper set is composed entirely of theoretical works, including analytic and simulation-based models. There are **no experimental** or **empirical** studies represented. The scope covers a **narrow range of direct public goods game (PGG) scenarios**, with most papers focusing on **variants of the PGG** or nearby social dilemma games (such as common-pool resource games and repeated prisoner’s dilemmas with spatial or network structure). A minority of papers attend exactly to the classic PGG with peer punishment and efficiency outcomes; others are “close” or “adjacent” in terms of the game structure, intervention, or outcome measures.

Overall, the evidence base is extensive in its theoretical modeling of mechanisms but limited in **(a) empirical realism/validation** and (b) direct coverage of the exact prediction task.

---

# 2) Task Relevance

We evaluate relevance for three target dimensions:

- **`pgg_or_variant`**:  
  - *Exact*: A subset of papers directly model the canonical or classic public goods game (e.g., Liu et al., 2019; Liu et al., 2018; Wang et al., 2021).
  - *Close*: Many papers study spatial PGGs or common-pool resource games, which share foundational features with PGGs (e.g., Chen & Szolnoki, 2018; Yan et al., 2021).  
  - *Adjacent/Weak*: Several focus on related social dilemmas (e.g., PDG, snowdrift games, or intellectual property contexts) and are less applicable for direct prediction.

- **`punishment_or_sanctions`**:  
  - *Exact/Close*: Most papers include explicit punishment or sanctioning mechanisms (either peer or institutional), often with varied implementation (peer, pool, exclusion, monitoring, bribery, etc.).
  - *Adjacent*: Some consider reputation systems or dynamic link weight adjustment primarily as indirect incentives.  
  - *None*: A few (e.g., Szolnoki & Chen, 2018; Wang, Chen & Szolnoki, 2019) do not include punishment or sanctions at all.

- **`efficiency_or_related_payoff_outcome`**:  
  - *Exact*: Only a small number explicitly report or analyze group efficiency or aggregate payoff (Liu et al., 2019; Liu et al., 2018; Chen & Szolnoki, 2018; Yan et al., 2021; Szolnoki & Chen, 2018).
  - *Adjacent*: The majority focus on cooperation rates, norm compliance, or population composition as primary outcomes, with efficiency referenced only occasionally or not at all.

In summary, **the set is most relevant for PGG and punishment mechanisms**, but **only a minority directly address efficiency/payoff outcomes** crucial to the downstream prediction task.

---

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes**:  
  - *Directly Measured*: Efficiency (group payoff as proportion of maximum possible), total group payoff, average payoff—most directly in Liu et al. (2019), Liu et al. (2018), Chen & Szolnoki (2018), Yan et al. (2021).
  - *Indirectly Assessed*: Some attention to costly incentives required to achieve cooperation (Wang et al., 2021).
  - *Not Measured*: Many papers do not compute average payoff, efficiency, or total welfare as defined above.

- **Non-Payoff Behavioral Outcomes** (most common):  
  - Contribution rate, cooperation rate, defector/cooperator/punisher population fractions.
  - Norm compliance, frequency of cooperation, and size of cooperative clusters.
  - Strategy evolution, presence of oscillatory dynamics, and regime thresholds (e.g., sudden jumps in cooperation, coexistence/bistability).

**Distinction**:  
Importantly, increased cooperation or norm compliance does not necessarily entail increased efficiency, especially when the costs of punishment or ecological/resource constraints are high. The literature demonstrates that positive effects on cooperation rates may not always align with gains in efficiency, particularly when sanctioning is costly or context limits the value of increased cooperation (Chen & Szolnoki, 2018; Yan et al., 2021).

---

# 4) Main Findings Relevant To Prediction

## Synthesis Across Papers

- **Punishment Often Promotes Cooperation, and Sometimes Efficiency**:  
  Enabling punishment mechanisms generally increases cooperation in PGG and spatial variants, but the effect on efficiency (payoff) is sensitive to **punishment costs, punishment effectiveness, and ecological/contextual constraints** (Liu et al., 2019; Liu et al., 2018).

- **Effect on Efficiency is Context-Dependent**:  
  - When punishment is effective (high penalty-to-cost ratio) and corruption/bribery is constrained, punishment increases both cooperation and efficiency (Liu et al., 2019).  
  - If punishment cost is high or the possibility for countermeasures (e.g., bribery/corruption, ecological depletion, excessive penalty strength) exists, efficiency gains from punishment can be neutralized or reversed (Liu et al., 2019; Chen & Szolnoki, 2018).  
  - Ecological or resource constraints can decouple cooperation from efficiency, such that even perfect cooperation enforced by punishment does not increase efficiency if resources cannot recover (Chen & Szolnoki, 2018; Yan et al., 2021).

- **Mechanisms Matter: Switching, Exclusion, Institutional Design**:  
  - Mechanisms allowing **switching between punishment and exclusion** as the number of defectors varies can yield higher efficiency than punishment alone (Liu et al., 2018).
  - Realized efficiency is maximized at intermediate switch thresholds and can suffer when the system is locked into either pure punishment or exclusion.
  - Institutional punishment (with probabilistic detection) can stabilize cooperation and group efficiency, but **effectiveness is determined by the combined probability and severity of punishment**, as well as the timing of feedback (Yan et al., 2021).

- **Diminishing Returns and Nonlinearities**:  
  - There are regimes where increasing punishment severity or probability has non-monotonic or threshold effects (He et al., 2019; Chen & Szolnoki, 2018).
  - **Too much or too expensive punishment can reduce efficiency** due to cost overload or by failing to prevent defector dominance (Yang et al., 2018).

- **Payoff Outcomes are Sparse**:  
  - Direct measurements of efficiency are present in only a small subset of studies; most findings extrapolate from cooperation rates or theoretical arguments about cost-benefit dynamics not always specific to payoff ratios.

- **Indirect Mechanistic Lessons**:  
  - Indirect incentives (reputation, adaptive feedback, link weighting) may promote cooperation, but the translation to efficiency depends on cost structures and is not established in these models.

---

# 5) Prediction Guidance

## Predicting Treatment Efficiency from Design and Control Efficiency

- **Direct Use of Efficiency Data**:  
  - Where available, results (e.g., Liu et al., 2019; Liu et al., 2018) indicate that the **increment to efficiency from enabling punishment is strongest when punishment is both effective and not overly costly**, and the game environment does not easily allow exploitation via corruption or resource depletion.

- **Conditional Modulation**:
  - **Control game efficiency** matters: If default cooperation is already high (e.g., due to high MPCR or small group size), enabling costly punishment may produce **diminishing or negligible increases in efficiency**; in some models, it could even reduce efficiency due to sanctioning costs (Wang et al., 2021).
  - Punishment that is too weak (low severity, low probability) can be ineffective in both cooperation and efficiency; **optimal ranges exist**, dependent on cost and context (Liu et al., 2018; Yan et al., 2021).

- **Design Parameters Mapping**:
  - Prediction should account for **punishment cost, punishment effectiveness (fine magnitude, detection probability), player count, MPCR**, and whether mechanisms allow for bribery/exclusion.
  - **Institutional versus peer punishment**: Peer punishment with shared cost or exclusion tends to be more efficient if it adapts to the frequency of defectors; institutional punishment's impact is dictated by probability-severity-product and feedback timing (Liu et al., 2018; Yan et al., 2021).

- **Absence of Structural Moderators**:
  - **Reward mechanisms** and **communication/chat** are not directly treated in most available evidence, so prediction under those features remains speculative.
  - **All-or-nothing settings** are addressed in some models, but with less clarity on efficiency impacts.

- **Extrapolation Risk**:
  - Where payoff data are not reported and only cooperation rates are available, **caution is warranted**, as efficiency can be decoupled from cooperation depending on the punishment cost structure or resource/ecological parameters.

---

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed**:
- `player_count`, `num_rounds`, `mpcr`: Most theory models specify or manipulate these.
- `punishment_cost`, `punishment_tech`: Explicitly modeled in nearly all PGG and close variant models.
- `all_or_nothing`: Included in several, though efficiency implications are less direct.
- `punishment_exists`: Central to all relevant models.

**Indirectly Informed**:
- `default_contrib`: Some models are sensitive to initial conditions (Wang et al., 2021), but this is not always made explicit as a design parameter.
- `reward_exists`, `reward_tech`, `reward_cost`: Occasionally discussed (Wang et al., 2021; Yang et al., 2018; some adjacent PDG/SDG models), usually as secondary or comparison mechanisms.
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Only very rarely and generically referenced (Yang et al., 2018 used `show_n_rounds`), otherwise almost completely missing.

**Contextually Discussed or Missing**:
- `chat`: Not addressed in efficiency-specific models.
- `show_punishment_id`: Not discussed; identity of punishers vs. anonymity is not explicitly modeled.

---

# 7) Important Limitations

- **Empirical Validation Lacking**:  
  All insights are derived from theory and simulations, not actual laboratory or field data. Generalizing to real human groups is risky.

- **Sparse Direct Efficiency Data**:  
  Only a handful of papers report or model efficiency as a primary outcome; most rely on cooperation rate or use payoff outcomes only to discuss population dynamics.

- **Ambiguity from Theoretical Breadth**:  
  Disagreement exists concerning when punishment increases efficiency—some findings are highly context-dependent, and model structure (e.g., presence of bribery or ecological feedback) can flip predictions.

- **Limited Coverage of Full Design Space**:  
  Critical prediction dimensions such as communication (`chat`), framing (`default_contrib`), reward settings, and summary/identity exposures are poorly represented or missing, constraining prediction for a wide range of game designs.

- **Reliance on Mechanism Arguments for Adjacent Games**:  
  Many lessons are extrapolated from PDG, snowdrift, or networked resource games—these may not transfer with fidelity to classic PGG payoff structures or sanctioning logic.

- **No Human Error, Learning, or Psychological Process**:  
  Theoretical agents follow explicit payoff-determined strategies; stochasticity, perception, bounded rationality, or social norms are not represented as in empirical studies.

---

**In summary:**  
The literature set provides substantial theoretical insight into how design parameters, especially *punishment cost* and *punishment effectiveness*, modulate the efficiency impact of punishment in PGG-like environments. Direct predictions of efficiency outcomes are, however, *rare and highly contextual*, with many design dimensions uncovered or only weakly addressed. Mechanistic and indirect evidence strongly supports that punishment raises cooperation, but efficiency improvements require careful balancing of incentives, costs, and ecological or contextual factors. Predictions made from this literature should account for substantial theoretical caveats and missing empirical grounding.
