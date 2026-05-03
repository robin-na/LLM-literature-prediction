# 1) Evidence Base

The paper set consists of four papers: one empirical observational study (Berger, 2021) and three theoretical contributions (Liu & Yang, 2018; Angourakis et al., 2015; Campbell, 1991). None of the papers present experimental public goods game (PGG) data, and only one (Berger, 2021) addresses field evidence (not a PGG variant). The set is quite broad and interdisciplinary, touching on agent-based modeling, evolutionary theory, historical analysis, and field interventions. For the downstream prediction task—forecasting average efficiency in PGG-like environments when peer punishment is enabled—this set provides only indirect and partial guidance, with little directly empirical or quantitative evidence on the efficiency effects of peer punishment.

# 2) Task Relevance

The papers vary in relevance across the three core dimensions:

- **pgg_or_variant:**
  - *adjacent* – All papers model or theorize about cooperation and free-riding, but in contexts that are adjacent (innovation networks, food storage, cultural moral orders) rather than direct PGG or its close variants.
- **punishment_or_sanctions:**
  - *exact* to *adjacent* – Liu & Yang (2018) directly model punishment/incentive mechanisms; Angourakis et al. (2015) and Campbell (1991) discuss sanctions but in broader or non-institutional forms; Berger (2021) primarily examines normative feedback, not punishment.
- **efficiency_or_related_payoff_outcome:**
  - *adjacent* to *weak* – Only Angourakis et al. (2015) approaches "payoff" concepts via surplus/shortage avoidance, but not efficiency as defined for PGG. Liu & Yang (2018) and Campbell (1991) theorize about group effectiveness or positive cooperation but do not quantify efficiency or group payoff. Berger (2021) is *weak* on this dimension, focusing on behavioral norm change.

**Summary:** The set is of *moderate to low* direct relevance; it supports mechanism and context interpretation but does not provide direct empirical or quantitative payoff-based results for PGGs with punishment.

# 3) Outcomes Measured In The Literature

**Payoff-related Outcomes:**
- *Only contextually discussed.* Angourakis et al. (2015) discusses surplus and avoidance of shortages in an agent-based common-pool resource model, which bears some relationship to group payoff but does not measure efficiency as defined in PGGs.
- Liu & Yang (2018) assess the stability of cooperation but do not report group payoff or efficiency.
- Campbell (1991) theorizes about group effectiveness/cohesion and does not report quantitative payoff outcomes.
- Berger (2021) does not report any payoff, earnings, or efficiency outcomes.

**Non-Payoff Behavioral Outcomes:**
- *Dominant in all papers.* All papers report outcomes like frequency of cooperation (Liu & Yang, 2018), norm adoption or behavioral change (Berger, 2021), or access to collective resources conditional on cooperation (Angourakis et al., 2015). Campbell (1991) is entirely theoretical on group-level effects of sanction belief systems.

**Conclusion:** The literature almost exclusively addresses behavioral rather than payoff-based outcomes, providing only very indirect proxies for efficiency.

# 4) Main Findings Relevant To Prediction

Synthesizing across the set:

- **Punishment and Cooperation:** There is broad theoretical support that sanction systems (punishment/reward mechanisms or their analogues) can stabilize or increase cooperative behavior in group contexts (Liu & Yang, 2018; Campbell, 1991; Angourakis et al., 2015).
- **Threshold Effects:** Liu & Yang (2018) finds that only when the sum of incentives and punishments crosses a particular threshold, stable cooperation emerges; below that, defection/negative cooperation dominates.
- **Sanction Severity:** Angourakis et al. (2015) highlight the non-monotonic effect of sanctions: too tight enforcement (high reciprocity demand) can decrease system performance, while too lax enforcement allows free-riding. Middle-ground (moderate sanctioning) optimizes sustained cooperation.
- **Indirect Suggestion for Efficiency:** While none measure efficiency directly, system performance, group stability, and surplus are commonly referenced proxies. The implication is that appropriately calibrated punishment can, ceteris paribus, improve system payoff/efficiency, but inappropriate settings (overly harsh or weak sanctions) can be detrimental—even compared to no punishment.
- **Norm Change Dynamics:** Berger (2021) illustrates that behavior can rapidly shift (in either direction) in response to feedback, with initial conditions (existing norm prevalence) being critical—suggesting path dependence and potential instability in normative interventions.

# 5) Prediction Guidance

Given the evidence:

- **Direction of Effect:** The literature provides moderate support for the expectation that enabling punishment in PGG-adjacent environments can increase cooperation, and—by extension—group efficiency, *if* punishment mechanisms are set at moderate, context-appropriate levels (Liu & Yang, 2018; Angourakis et al., 2015).
- **Limits and Dangers:** Too harsh or imbalanced punishment risks reducing efficiency, either by excluding contributors (Angourakis et al., 2015) or increasing costs that outweigh cooperative gains (implied by Liu & Yang, 2018).
- **Baseline/Control Efficiency Matters:** None of the papers empirically condition punishment effects on baseline efficiency, but Angourakis et al. (2015) and Berger (2021) both suggest that system characteristics and initial conditions crucially mediate the effects of interventions.
- **Quantitative Prediction is Unsupported:** The set provides no empirical function or magnitude estimation; all guidance is qualitative and mechanism-based.
- **Relevance to Prediction Dimensions:** Only some design variables are directly addressed (see below), so prediction will need to default to general mechanism theories rather than dimension-specific estimates.

# 6) Design Dimensions Highlighted Across Papers

- **Directly Informed:**
  - `punishment_cost` (Liu & Yang, 2018): Explicitly modeled as a threshold component; higher cost reduces willingness to punish.
  - `reward_exists` (Liu & Yang, 2018; Campbell, 1991): Co-discussed with punishment as complementary incentives.
  - `player_count`, `num_rounds` (Angourakis et al., 2015): Modeled in the agent-based simulation, but not directly parameterized for payoff outcomes.
  - `show_other_summaries` (Berger, 2021): Normative feedback operationalized as group summary info, affecting norm adoption.

- **Indirectly Informed:**
  - `mpcr`: Efficiency of food storage in Angourakis et al. (2015) maps onto this, but not in PGG form.
  - `punishment_tech`, `reward_tech`: Discussed as access control and supernatural sanctions conceptually, but not as operational game techs.
  - `all_or_nothing`, `default_contrib`, `show_n_rounds`, `show_punishment_id`, `reward_cost`, `reward_tech`: Only contextually or not at all addressed.

- **Effectively Missing:**
  - No empirical evidence on the impact of `chat`, `all_or_nothing`, `default_contrib`, or the reward and punishment magnitude fields on group efficiency.
  - No treatment of visibility of punishment/reward (`showPunishmentId`), number of rounds shown, or most reward/punishment technical variables in a directly predictive way.

# 7) Important Limitations

- **Lack of Direct PGG Evidence:** No paper in the set offers experimental or field data from standard public goods games with and without punishment.
- **Behavioral, Not Payoff Outcomes:** Nearly all results are in terms of cooperation frequency or norm change, not actual earnings, group payoff, or efficiency.
- **Absence of Quantitative Prediction:** No parameterized functions or effect sizes are available; all conclusions are qualitative, relying on theoretical inference or analogical model argument.
- **Sparse Coverage of Design Dimensions:** Only a few of the 14 prediction dimensions are addressed, mainly in broad terms and often without empirical backing.
- **Generalizability is Uncertain:** The models and theory may not generalize to lab PGGs or to other parameter ranges; context and mechanism ambiguity remains high.
- **Interaction Effects and Baselines:** There is little to no evidence on how punishment's effect depends on pre-existing efficiency or other design features.
- **Potential for Contradictory Effects:** Angourakis et al. (2015) notes that too strong or too weak sanctioning can reduce system performance, leaving ambiguous guidance for setting punishment parameters.

---

**In sum:** The paper set supports the general theoretical principle that properly calibrated punishment can improve cooperation and (likely) group outcomes in collective action settings. However, it leaves significant uncertainty about the magnitude, conditions, and parametric dependence of efficiency changes in actual PGG designs. Predictions should therefore be hedged, emphasizing mechanism-based reasoning, and interpreted cautiously given the lack of payoff-relevant empirical evidence and the limited direct coverage of design dimensions.
