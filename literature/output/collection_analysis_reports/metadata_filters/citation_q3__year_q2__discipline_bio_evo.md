# 1) Evidence Base

The paper set comprises a mix of **empirical (both field and laboratory experiments)** and **theoretical (game-theoretic, agent-based, and evolutionary modeling)** studies, with an emphasis on theory papers that provide explicit predictions about **punishment effects in public-goods games (PGGs) and close variants**. The set is broad in its consideration of **social dilemmas**, **enforcement mechanisms**, and various **game design dimensions**.

However, the **direct empirical evidence on the target outcome—group efficiency (total payoff relative to full cooperation) under punishment versus control—is limited**. Many empirical papers focus on **behavioral outcomes** (contribution, cooperation, norm compliance) rather than direct payoff-based measures. The **theory papers** fill several gaps by exploring **punishment effects on efficiency** across diverse settings, but often within stylized models.

Overall, the evidence base is **strong for mechanism insight and parameter sensitivity** (especially in theory), **adequate** for efficiency outcomes in PGGs with punishment, but **limited in direct empirical payoff outcomes for all combinations of game design dimensions** relevant for the prediction task.

---

# 2) Task Relevance

Task-relevance is assessed along three axes:

| Dimension                       | Relevance | Comments |
|----------------------------------|-----------|----------|
| `pgg_or_variant`                 | exact     | Most theory and several empirical papers use PGGs or structurally identical games (e.g., Oya & Ohtsuki, 2017; Dercole et al., 2013). Some extend to close variants (e.g., common-pool resources, repeated n-player PD), and a subset are only adjacent. |
| `punishment_or_sanctions`        | exact     | A large subset directly manipulates or models peer or institutional punishment (e.g., Oya & Ohtsuki, 2017), but some only discuss sanctions more broadly, or punishment is not enabled (`none` in some control/baseline papers). |
| `efficiency_or_related_payoff_outcome` | exact/close | Several theory papers report group efficiency/payoff (e.g., Archetti & Scheuring, 2013; Zhang et al., 2013); some empirical and review papers focus on behavioral proxies but not efficiency (e.g., Skatova & Ferguson, 2013). Many adjacent papers report behavioral rather than payoff outcomes, requiring extrapolation. |

- **Overall**: Task relevance is **highest in theory papers focused on linear PGGs with explicit punishment and efficiency outcomes** (e.g., Oya & Ohtsuki, 2017; Dercole et al., 2013; Archetti & Scheuring, 2013). Empirical coverage is often **adjacent** due to outcome focus mismatch.

---

# 3) Outcomes Measured In The Literature

- **Payoff-based outcomes (primary for prediction):**
  - *Efficiency (group payoff relative to full cooperation)* is analyzed directly in several theory papers (Oya & Ohtsuki, 2017; Archetti & Scheuring, 2013; Zhang et al., 2013; Dercole et al., 2013), and in select empirical/field lab work (Vollan et al., 2013).
  - *Related payoff metrics* (group welfare, surplus, total earnings) appear in both theory (Lee et al., 2015; Okada et al., 2015; Powers & Lehmann, 2013) and field experiments (Vollan et al., 2013), though sometimes as theoretical constructs rather than measured outcomes.
  - Some studies (e.g., Kurokawa & Ihara, 2017) provide analytic derivations of expected payoffs/efficiency thresholds, but not observed values.

- **Behavioral outcomes (distinct from payoff):**
  - *Contribution rates, cooperation frequency*, norm compliance, and punishment frequency are the focus in much of the empirical and behavioral literature (Skatova & Ferguson, 2013; Schroeder et al., 2015; Gatiso et al., 2015).
  - These outcomes are important but not direct measures of efficiency, and efficiency must often be inferred, with recognition of the distinction.

- **Ambiguity:** There is some conflation in review/discussion papers (Strang & Park, 2017) between cooperation rates and efficiency, but the best papers for prediction clearly distinguish these.

---

# 4) Main Findings Relevant To Prediction

Synthesizing the best-supported and most relevant findings:

- **Enabling Peer Punishment in PGGs:**
  - **Theory consensus:** In standard, linear PGGs, introducing peer punishment tends to increase group efficiency (i.e., group payoffs approach the cooperative maximum), often substantially, *if punishment is not too costly and design does not enable antisocial punishment* (Dercole et al., 2013; Oya & Ohtsuki, 2017; Archetti & Scheuring, 2013).
  - **Context dependence:** The effect is *highly sensitive* to:
    - **Population structure:** Punishment is more effective in spatially structured populations or those with repeat interactions/limited mobility (Oya & Ohtsuki, 2017; Roos et al., 2014).
    - **Cost-effectiveness of punishment:** Punishment increases efficiency only when cost-to-impact ratio is sufficiently favorable; high punishment costs or weak impact can make punishment ineffective or even reduce efficiency (Vukov et al., 2013; Dercole et al., 2013; Zhang et al., 2017).
    - **Institutional design:** Centralized or shared-cost punishment, or pre-assessment/institutionalized schemes, are more robust and can maintain efficiency even in large groups (Okada et al., 2015; Lee et al., 2015; Sasaki et al., 2016).
    - **Absence/presence of corruption or antisocial punishment:** If antisocial punishment or corrupt enforcement is possible, punishment can fail to improve or may reduce efficiency (Lee et al., 2015, 2017).
    - **Production function nonlinearity:** In nonlinear PGGs (e.g., threshold or sigmoidal production functions), high efficiency can be achieved without punishment; enabling punishment adds benefit mainly in linear settings (Archetti & Scheuring, 2013).
    - **Group size (player_count):** Punishment's effectiveness can decline in very large groups unless institutional mechanisms coordinate sanctioning (Powers & Lehmann, 2017).

- **Empirical findings:** Empirical studies *consistently find increased contribution rates* when punishment is possible (Skatova & Ferguson, 2013; Schroeder et al., 2015); some field-lab studies show improved earnings/efficiency when rules are aligned with local norms and sanctions are participatory (Vollan et al., 2013; Gatiso et al., 2015). Direct measurement of efficiency, however, is less common than in theory.

- **Special cases:** In rare scenarios (e.g., introduction of cheap insurance against punishment, or high punishment cost), punishment fails to sustain cooperation and efficiency (Zhang et al., 2013). In well-mixed populations without mechanisms to maintain clusters of punishers, punishment alone does not improve efficiency (Oya & Ohtsuki, 2017; Roos et al., 2014).

- **Mechanisms for failure/backfire:** When punishment is costly and not well-targeted, or when punishers themselves are defectors (antisocial punishment), efficiency can *decline* relative to control (Oya & Ohtsuki, 2017; Vukov et al., 2013; Lee et al., 2015).

---

# 5) Prediction Guidance

**Strengths of prediction from this literature:**

- For **standard PGGs with linear benefit functions**, *enabling peer punishment predicts a robust increase in efficiency* relative to a no-punishment baseline, provided punishment is not too costly and is well-targeted (Dercole et al., 2013; Archetti & Scheuring, 2013).
- **Structured populations, repeated interactions, and institutionalized (centralized) punishment** settings are most likely to yield large efficiency improvements.
- *Control game efficiency* is relevant: when control efficiency is low, the marginal efficiency gain from enabling punishment is typically greater (Zhang et al., 2013; Archetti & Scheuring, 2013).

**Cautions and moderating factors:**

- **Design dimensions moderate the effect:**
  - *Player count:* Larger groups dilute the individual impact of punishment and, without coordination, can reduce its effectiveness (Powers & Lehmann, 2017).
  - *Punishment cost/tech:* High-cost, low-effectiveness punishment can reduce efficiency (Vukov et al., 2013).
  - *Antisocial punishment or corruption:* Can negate or reverse the efficiency gains (Lee et al., 2015, 2017).
  - *Production function nonlinearity:* In non-linear games, efficiency can be high even without punishment, so enabling punishment adds little (Archetti & Scheuring, 2013).

**Gaps:**

- **Quantitative predictions:** Exact values for the efficiency boost are less certain empirically and depend on unmeasured moderators in many settings; theoretical models (Dercole et al., 2013) provide formulas under specified assumptions.

- **Behavioral vs. payoff outcomes:** Many empirical results are about cooperation/contribution, not efficiency. Translating increased cooperation into efficiency requires adjustment for the cost of punishment, which can offset part of the gains from higher contributions if punishment is overused or misdirected.

---

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**
- `player_count`: Strongly examined—its effects on efficiency and punishment impact are modeled and discussed in both theory and empirical work. Larger groups reduce effectiveness unless institutionally managed (Dercole et al., 2013; Powers & Lehmann, 2017).
- `mpcr`: Explicit in theory; higher multipliers make cooperation more attractive and increase marginal efficiency gain of punishment (Dercole et al., 2013; Oya & Ohtsuki, 2017).
- `punishment_cost` and `punishment_tech`: Widely viewed as key moderators of punishment's effectiveness for efficiency (Vukov et al., 2013; Dercole et al., 2013; Lee et al., 2015).
- `all_or_nothing`: Modeled in most theory work, sometimes as only possible contribution structure (Oya & Ohtsuki, 2017).
- `num_rounds`: Considered, particularly in repeated game analyses, which impact the sustainability of cooperation and efficiency (Schroeder et al., 2015; Oya & Ohtsuki, 2017).
- `reward_exists/cost/tech`: Examined in work modeling both punishment and reward as alternative or co-occurring mechanisms (Okada et al., 2015), although direct evidence is sparser.
- `show_punishment_id`, `show_other_summaries`, `show_n_rounds`: Occasionally treated (e.g., Lee et al., 2015) in relation to transparency/information and the effectiveness/legitimacy of punishment.

**Indirectly or Contextually Informed:**
- `chat`: Rarely manipulated; communication and its effect on cooperation/efficiency is discussed but not as a primary moderator of punishment effects.
- `default_contrib`: Framing effects and default options are minimally addressed; some behavioral studies note decision framing but not as a main dimension.
- `punishment_magnitude`: While always inherent to the modeling of punishment parameters, not always presented as a distinct design lever.
- `reward_magnitude`: Treated in studies that model both reward and punishment, but often as a composite incentive measure.
- `show_other_summaries`, `show_n_rounds`: Sometimes controlled as part of experimental setup but not usually as a focus for punishment effect prediction.

**Effectively Missing:**
- Precise **interaction effects** between many of the 14 dimensions (e.g., whether changing chat or default_contrib modifies the efficiency impact of punishment) are largely unexamined.
- Few papers **systematically vary multiple design dimensions** in combination when reporting efficiency outcomes.
- **Empirical measurement** of efficiency combining all dimension settings is lacking; most designs use standard parameter values.

---

# 7) Important Limitations

- **Empirical gaps:** There is a *shortage of direct, empirical measurements of group efficiency (total payoff)* under both control and punishment-enabled conditions across diverse game designs. Most empirical studies focus on cooperation rates, not efficiency.
- **Theory–empirical gap:** Many relevant results are from **theory and simulation**, which, while valuable for mechanisms and parameter sensitivity, may not always generalize to real-world or lab behavior due to unmodeled factors (heterogeneity, bounded rationality, real sanctioning errors, etc.).
- **Context sensitivity/contingency:** Multiple theory papers and field experiments show that the **effect of punishment on efficiency is highly context-dependent**, especially with respect to group structure, institutional design, and the possibility of antisocial punishment or enforcement corruption.
- **Limited coverage of certain dimensions:** Many game design features relevant for modern online or behavioral contexts (e.g., `chat`, payoff framing, punishment/reward interface design) are underexplored.
- **Intervention realism:** Most studies, particularly theory, assume idealized punishment implementation—real-world interventions often face *compliance, transparency, and norm-fit* challenges (Vollan et al., 2013).
- **Payoff–behavior translation:** Increased contribution does not always translate one-to-one into higher efficiency due to punishment costs, over-punishment, or inefficient sanctioning. This is often not accounted for in behavioral reports.
- **Scarcity of cross-dimension data:** Few studies allow mapping full interactions among all 14 design dimensions for prediction purposes.
- **Modest empirical field/lab estimation:** Some key parameters (e.g., impact of punishment cost in very large groups, or under varying knowledge of rounds/identity) lack sufficient direct empirical testing.

---

# Summary Table: Dimension–Evidence Mapping

| Dimension          | Coverage       | Prediction Insight Provided                |
|--------------------|:--------------|:------------------------------------------|
| player_count       | direct        | Efficiency gains from punishment diminish in larger groups unless coordinated/institutionalized. |
| num_rounds         | direct        | More rounds favor stable cooperation under punishment (esp. in theory); not often varied in empirical work. |
| chat               | minimal       | Communication increases cooperation, but its interaction with punishment for efficiency is underexplored. |
| all_or_nothing     | direct        | Most models assume this structure.         |
| default_contrib    | context only  | Rarely manipulated for prediction.         |
| mpcr               | direct        | Stronger public goods value amplifies efficiency gain from punishment. |
| punishment_cost    | direct        | Critical moderator: low cost enhances, high cost reduces/negates efficiency benefit. |
| punishment_tech    | direct        | Shared-cost and institutionalized punishment more effective for efficiency. |
| reward_exists/cost/tech | partial | Reward as alternative/supplement to punishment; key in meta-incentive models. |
| show_n_rounds      | context       | Some theory/empirical work includes, rarely focal for efficiency under punishment. |
| show_other_summaries| context      | Sometimes varied in field/lab studies.     |
| show_punishment_id | limited       | Transparency can reduce corruption, enhance effectiveness of punishment. |
| punishment_magnitude | indirect    | Embedded in models’ punishment effectiveness parameters.    |
| reward_magnitude   | indirect      | Embedded in theoretical studies with joint incentive frameworks. |

---

# References

References to specific findings and claims appear as APA-style citations above, according to supplied source lines. Key papers directly supporting efficiency predictions include: (Oya & Ohtsuki, 2017; Dercole et al., 2013; Archetti & Scheuring, 2013; Lee et al., 2015; Powers & Lehmann, 2013; Okada et al., 2015; Zhang et al., 2013; Vollan et al., 2013).

---

**In summary:**  
Punishment robustly increases efficiency in linear, well-specified PGGs unless costs are prohibitive, population is well-mixed without coordination, or the design suffers from enforcement corruption/antisocial punishment. Many moderating factors must be considered, with institutional context, group size, and parameter values especially important. The evidence base is rich in mechanisms and qualitative guidance, but less so in empirical payoff data across the full range of game design dimensions for direct quantitative prediction.
