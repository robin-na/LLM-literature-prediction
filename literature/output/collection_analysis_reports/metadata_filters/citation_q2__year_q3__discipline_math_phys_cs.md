# 1) Evidence Base

The paper set contains 80 papers, reflecting a wide range of empirical (notably a few lab/field experiments) and theoretical (mainly simulation- and analytic-model-based) research. There is a strong representation of computational/theoretical modeling, especially focusing on public goods games (PGG) and their close variants, as well as many adjacent social dilemma models (Prisoner's Dilemma, common-pool resource games, etc.). Empirical lab experiments directly addressing PGGs with punishment and reporting efficiency/welfare outcomes are present but in the minority (e.g., Castillo et al., 2021; Kol'veková et al., 2021).

The breadth is high regarding mechanisms and contextual settings, covering centralized/peer punishment, reward, reputation, information, and social structure, but when considering the exact downstream prediction task—quantitative prediction of efficiency in PGGs under peer punishment using specified design dimensions—the literature is narrower. A substantial portion of papers measure only behavioral outcomes (cooperation/contribution rates) rather than efficiency/welfare, or study adjacent games or mechanisms.

**Empirical vs. Theory:**  
- **Empirical (lab/field experiments):** Small but crucial subset, with high task relevance in a few cases (Castillo et al., 2021).
- **Theoretical/simulation models:** Majority; provide qualitative and sometimes parameterized predictions about efficiency and cooperation as a function of game settings.

# 2) Task Relevance

## a) `pgg_or_variant`
- **Exact relevance:** Substantial core cluster directly model or test PGGs or explicit variants—most theory and a few experiments (e.g., Castillo et al., 2021; Kol'veková et al., 2021; Cui et al., 2019; Sui et al., 2018).
- **Close relevance:** Common-pool resource games, threshold PGGs, donation games with group outcomes.
- **Adjacent/Weak:** Many works on Prisoner's Dilemma, river or division of labor games—structurally similar but not PGGs.
- **None:** Minority (e.g., Stackelberg security game).

## b) `punishment_or_sanctions`
- **Exact relevance:** Several directly examine punishment mechanisms in PGGs (peer, centralized, exclusionary, etc.—see Castillo et al., 2021; Sui et al., 2018).
- **Close/Adjacent:** Some focus solely on reward, ostracism, exit/partner switching, or broader incentive frameworks rather than strict costly punishment.
- **Weak/None:** Many do not include punishment or sanctions.

## c) `efficiency_or_related_payoff_outcome`
- **Exact relevance:** Fewer papers report efficiency, group payoff, welfare, or surplus explicitly; several do (e.g., Castillo et al., 2021; Kol'veková et al., 2021; Wang & Lv, 2019; Cui et al., 2019).
- **Close:** Some report average payoff per strategy or group, which is generally close but not always mapped to the definition of efficiency used in the task.
- **Adjacent:** Large fraction report only cooperation, contribution, or strategy proportions.
- **None:** A minority; some focus on evolutionary stability, frequency of behaviors, or structural outcomes without explicit payoff analysis.

**Summary:**  
The most relevant evidence is concentrated in a subset of theory/simulation and a handful of experimental papers that examine both punishment and payoff-based efficiency in PGGs or their close variants. Much of the literature diverges on at least one dimension (punishment, exact game structure, or payoff outcome).

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes:**
- **Efficiency (defined as group actual/optimal payoff):** Directly measured in a number of studies (e.g., Castillo et al., 2021; Kol'veková et al., 2021; Cui et al., 2019; Wang & Lv, 2019; Sui et al., 2018; Murase & Baek, 2021).
- **Group payoff, surplus, welfare, or total earnings:** Often reported as proxies for efficiency (e.g., Fang et al., 2020; Gámez et al., 2018; Nakamaru et al., 2018).
- **Strategy-specific average payoff:** Sometimes reported but not always mapped to group-level efficiency (e.g., Wei et al., 2021; Wang & Lv, 2019).
- **Indirect or adjacent payoff proxies:** Some papers imply payoff effects but only report changes in cooperation/contribution.

**Non-Payoff Behavioral Outcomes:**
- **Contribution or cooperation rates:** Most commonly reported; important for interpreting mechanism but not sufficient for efficiency prediction (e.g., Chen et al., 2018; Moreno & Gutierrez-Garcia, 2018).
- **Punishment or reward frequency, norm compliance, strategy prevalence:** Useful for mechanism discussion, but not direct evidence for efficiency.

**Distinction:**  
Multiple papers explicitly note that increased cooperation/contribution rates do not guarantee increased efficiency due to the cost of punishment (e.g., Quan et al., 2019; Kol'veková et al., 2021).

# 4) Main Findings Relevant To Prediction

**Empirical and Theory Papers—Consistent Patterns:**
- **Enabling punishment in PGGs usually increases efficiency, but the effect is conditional.**
    - The effect is clearly positive in most linear/threshold PGGs when punishment is sufficiently cheap/effective (Castillo et al., 2021; Kol'veková et al., 2021; Cui et al., 2019; Wang & Lv, 2019; Gámez et al., 2018; Podobnik et al., 2019).
    - Endogenous or dynamic punishment mechanisms can achieve high efficiency at low cost once cooperation stabilizes (Kol'veková et al., 2021).
    - Centralized (manager-based or institutional) punishment works—mechanism of selection (vote vs. random) is less important than the presence of punishment and the cost/impact ratio (Castillo et al., 2021).

- **Efficiency gains depend strongly on punishment cost, effectiveness, and context.**
    - If punishment is too costly relative to its impact, efficiency can be reduced due to wasted resources (Quan et al., 2019; Fang et al., 2020; Sui et al., 2018).
    - Theoretical models highlight non-monotonic effects: too harsh or frequent punishment may suppress efficiency (Podobnik et al., 2019; Ille, 2021; Chang & Zhang, 2021).
    - Performance-based or shared-cost punishment, low prevalence of corruption/bribery, and efficient targeting all facilitate positive efficiency effects (Fang et al., 2020; Kol'veková et al., 2021).

- **Other design moderators:**
    - **MPCR (marginal per-capita return):** Efficiency increases with synergy factor—punishment is more effective at higher MPCR but can also be needed at lower MPCRs to preclude collapse (Cui et al., 2019; Wang & Lv, 2019).
    - **Player count, group size:** Group size moderates the punishment effectiveness threshold (Wang & Lv, 2019; Sui et al., 2018). In theory, larger groups make sustaining cooperation harder, increasing the importance of punishment's design.
    - **Information/reputation structure:** Peer monitoring/publicity facilitates punishment's effectiveness (Kol'veková et al., 2021; Wei et al., 2021).
    - **Punishment type (peer vs. centralized):** Both can increase efficiency; relative effectiveness depends on structure and costs (Castillo et al., 2021; Moreno & Gutierrez-Garcia, 2018).

- **Contrary or nuanced findings:**
    - **Costly or overused punishment can be welfare-reducing:** Punishment that is frequent and costly can increase cooperation but lower net payoff, especially under certain parameterizations or social norms (Quan et al., 2019).
    - **Non-costly (ostracism, exit) or reward mechanisms may provide efficiency gains without the cost burden of punishment, but direct comparisons are sparse.**

**Link to Prediction Dimensions:**
Notably, only a subset of PGG punishment studies report both:
  - Control (no-punishment) efficiency **and**
  - Treatment (with-punishment) efficiency **as a function of design dimensions** (see next section).

# 5) Prediction Guidance

For the downstream task—predicting the treatment efficiency of a PGG-like game with peer punishment from design dimensions and control efficiency—the following guidance emerges:

- **Enabling (peer or centralized) punishment almost always increases efficiency relative to no-punishment controls, provided:**  
    - **Punishment is not too costly relative to its deterrent effect.**
    - **Mechanisms for reputational targeting or shared cost are present to minimize excessive punishment.**
    - **Bribery, corruption, or second-order free-riding do not overwhelm the punishment system.**

- **Magnitude and robustness of the efficiency gain are a function of the following dimensions:**
    - **Punishment cost and magnitude (punisher cost, punished loss):** Lower costs and higher impact per unit cost yield greater efficiency gains (Kol'veková et al., 2021; Sui et al., 2018; Cui et al., 2019; Fang et al., 2020).
    - **MPCR:** Higher MPCR amplifies the positive effect of punishment (Cui et al., 2019; Wang & Lv, 2019; Murase & Baek, 2021).
    - **Player count (group size):** Larger groups may require more effective or institutionalized forms of punishment for the same efficiency gain (Wang & Lv, 2019; Sui et al., 2018).
    - **Institutional design (peer vs. centralized, endogenous vs. exogenous):** Centralized punishment can work regardless of selector legitimacy (Castillo et al., 2021), but peer and shared models are also viable with proper coordination (Kol'veková et al., 2021).

- **Behavioral Outcomes ≠ Efficiency:** High contribution or cooperation rates generally—but not always—translate to higher efficiency due to the cost factor.

- **Uninformed dimensions:** Many design aspects (e.g., chat, default contribution, information display, opt-in framing, identity of punishers, reward mechanisms where not layered with punishment) are less often directly linked to efficiency changes in these models.

- **Quantitative mapping:** While directionality is robust given the above conditions, the literature only intermittently provides quantitative mappings (i.e., effect size estimates depending on the control efficiency and dimension values).

- **Control efficiency is a necessary baseline:** Settings with already-high cooperation in control may see lower incremental gains; in low-efficiency controls, punishment is more likely to produce pronounced improvements.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions (evidence for how punishment effect on efficiency varies):**
- **player_count (group size):** Direct and detailed in many models and some experimental studies.
- **mpcr (synergy factor):** Consistently modeled, linked to both baseline efficiency and the effectiveness of punishment.
- **num_rounds:** Addressed in iterated/repeated game models and in experiments; effects are usually on stability rather than immediate efficiency.
- **punishment_cost, punishment_tech (impact/per coin):** Central in all exact-relevance punishment models; effect is often mapped explicitly to efficiency difference (see Kol'veková et al., 2021; Sui et al., 2018; Fang et al., 2020).
- **all_or_nothing (vs. continuous):** Some explicit comparisons (Kol'veková et al., 2021).
- **reward_exists, reward_cost, reward_tech:** Addressed primarily in studies including both reward and punishment; generally, rewards can substitute for or augment the effect of punishment, but cost structures/coverage matter greatly.
- **chat, show_other_summaries, show_punishment_id:** Occasionally included (Castillo et al., 2021; Kol'veková et al., 2021; Przepiorka & Diekmann, 2020), but often only contextually discussed.

**Indirect or Contextual Evidence:**
- **default_contrib:** Rarely analyzed or explicitly manipulated.
- **show_n_rounds:** Occasionally varied, but less often focal.
- **punishment_tech (mechanism/targeting):** Broader in theory work; level of targeting or structure of punishment can modulate the efficiency impact.

**Effectively Missing or Weakly Informed Dimensions:**
- **Reward-related dimensions** beyond their presence or absence (quantitative interactions with punishment are rarely modeled empirically).
- **Communication and identity display dimensions** (e.g., chat, show_punishment_id) typically have only indirect, contextual coverage—with one experiment on feedback visibility in a related CPR game (Przepiorka & Diekmann, 2020).

**Summary:**  
Strongest evidence links the effect of punishment on efficiency to group size, number of rounds, MPCR, punishment cost/magnitude, and to a lesser degree, the form of punishment. Other prediction dimensions are much less thoroughly addressed.

# 7) Important Limitations

- **Lack of comprehensive empirical studies:** The overwhelming majority are theory/simulation papers; direct experimental evidence mapping design dimensions to efficiency effects is sparse (notably Castillo et al., 2021 and Kol'veková et al., 2021).
- **Limited direct evidence on peer punishment:** Many models focus on institutional/centralized punishment or broader incentive regimes.
- **Behavioral vs. payoff conflation:** Many findings about increased cooperation rates do **not** correspond to increases in efficiency, especially where punishment is costly or overused (explicitly flagged in Quan et al., 2019; Kol'veková et al., 2021).
- **Sparse evidence for interaction effects:** Detailed cross-dimensional effects (e.g., how punishment cost interacts with player count and MPCR in empirical settings) are rarely validated.
- **Relatively few studies provide both control and treatment efficiency as functions of all prediction dimensions.**
- **Transferability from adjacent games:** Caution warranted when applying findings from prisoner's dilemma, threshold games, or other adjacent games—mechanism and effect size may not directly map to standard PGGs.
- **Some dimensions are only contextually discussed or entirely missing:** Notably, chat, information presentation, identity disclosure, and default contribution framing.
- **Quantitative prediction is difficult:** While directionality (positive/negative/no effect) of punishment is generally well supported, magnitude and boundary conditions are less precisely mapped, especially in peer punishment with varying efficiency baselines.

---

**In conclusion:**  
This literature base offers robust support that punishment typically increases efficiency in PGG and close variants, primarily when punishment is sufficiently effective and not overly costly. The moderators most directly predictive are group size, MPCR, and the punishment cost/impact ratio. However, the evidence base is far richer for qualitative mechanistic prediction than for fine-grained quantitative estimation across the full vector of design dimensions, and is far stronger for theory/simulation than for empirical, parameterized mapping to experimental data. Non-payoff outcomes should not be treated as direct proxies for efficiency. Extrapolation should be especially cautious in settings where multiple unstudied design features (e.g., chat, visibility, reward layering) or very high baseline efficiency are present.
