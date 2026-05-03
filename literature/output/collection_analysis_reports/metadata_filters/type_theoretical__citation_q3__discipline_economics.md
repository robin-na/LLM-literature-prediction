# 1) Evidence Base

The paper set is composed entirely of theoretical (game theory, mechanism design, simulation/modeling) works; there are no (reported) empirical or experimental studies in the digest. The scope is broad with respect to social dilemmas, norm enforcement, and cooperation mechanisms, but only a subset of papers focus narrowly on standard public goods games (PGG) with clear payoff outcomes. Many papers examine closely related settings (common-pool resource games, collective reputation, trust, and coalition games) or address psychological, evolutionary, or organizational mechanisms.  

A proportion of the evidence base provides explicit analytical or simulation modeling of efficiency effects, with some offering comparative statics and parameterized predictions. Others provide only behavioral predictions, mechanism arguments, or broader conceptual context without quantifying payoff outcomes.

# 2) Task Relevance

**a) `pgg_or_variant`**  
- **Exact**: Several papers directly model standard PGGs (e.g., Levine & Modica, 2016; Hwang & Bowles, 2012; van der Weele, 2012).  
- **Close**: Many papers model close variants (spatial PGGs/CPRs, joint effort games, coalition/trust games; e.g., Acemoglu & Wolitzky, 2020; De Silva et al., 2010; Noailly et al., 2009).
- **Adjacent/Weak**: Some discuss public-goods-like organizational or social structures (e.g., Cordes et al., 2010) or only touch on PGGs contextually.

**b) `punishment_or_sanctions`**  
- **Exact**: A tier of papers centrally model or analyze peer punishment/sanctions (e.g., Levine & Modica, 2016; van der Weele, 2012; Hwang & Bowles, 2012).
- **Close/Adjacent**: Many model related mechanisms (expulsion, social sanctions, exclusion, monitoring/ostracism, reward systems, or indirect sanctioning).
- **Weak/None**: A few focus on internal motivation, reputation, or social norms in absence of explicit punishment.

**c) `efficiency_or_related_payoff_outcome`**  
- **Exact/Close**: About half of the most relevant papers report or model efficiency, surplus, group payoff, or welfare as explicit outcomes.
- **Adjacent**: Some discuss efficiency tangentially or as an implication of behavioral results.
- **Weak/None**: Numerous works focus on cooperation/defection rates, compliance, or punishment behavior, not payoff-based outcomes.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes**:  
  * Efficiency (payoff relative to social optimum): Directly modeled in several PGG-theoretic and CPR-variant papers (e.g., Levine & Modica, 2016; Acemoglu & Wolitzky, 2020; van der Weele, 2012; Noailly et al., 2007/2009; De Silva et al., 2010; Tarui et al., 2008; Saak, 2012).
  * Welfare, surplus, total group earnings, aggregate payoff: Also modeled directly in a range of theoretical works.

- **Non-payoff behavioral outcomes**:  
  * Contribution, cooperation rates, norm compliance, punishment/expulsion/reward assignment frequencies: Frequently emphasized across much of the literature (e.g., Reuben & Tyran, 2010; Orr, 2001; Thöni, 2014), but cannot be directly mapped onto efficiency outcomes without additional assumptions.

- **Contextual/Indirect outcomes**:  
  * Motive-driven behavior (altruistic/antisocial punishment, fairness, revenge); social norm internalization; trust and reciprocity profiles.

# 4) Main Findings Relevant To Prediction

- **Punishment typically increases efficiency, but conditionally**: Multiple theory papers (Levine & Modica, 2016; Acemoglu & Wolitzky, 2020; van der Weele, 2012; Noailly et al., 2007/2009; Saak, 2012) converge on the result that enabling peer or group punishment, if not prohibitively costly and sufficiently effective, can sustain higher efficiency by deterring defection/free-riding, often pushing outcomes close to the social optimum.

- **Cost/effectiveness of punishment matter critically**:  
  * When punishment is cheap and impactful, its introduction increases efficiency substantially (Levine & Modica, 2016; Acemoglu & Wolitzky, 2020).  
  * High punishment costs or weak implementation limit or even reverse efficiency gains.

- **Group size (player count) has nuanced effects**:  
  * Larger groups often benefit more from enabling punishment (Levine & Modica, 2016), but if groups are too large, or if monitoring is imperfect, maintaining efficiency becomes harder (Tarui et al., 2008; Noailly et al., 2009; Saak, 2012).

- **Social preference structure moderates punishment's effect**:  
  * High baseline social preferences (altruism or reciprocity) can reduce the incremental efficiency benefit of punishment, and in certain regimes can even reverse it due to reduced willingness to punish (Hwang & Bowles, 2012; van der Weele, 2012).

- **Information and monitoring design are key moderators**:  
  * Efficiency gains from punishment depend on information about other players' actions and the ability to credibly punish (Haag & Lagunoff, 2006; Bhaskar & Thomas, 2019; Saak, 2012).

- **Behavioral phenomena (e.g., antisocial punishment, crowding out of intrinsic motivation) can offset positive effects**:  
  * Antisocial punishment and moral crowding effects can undermine the net benefit of enabled punishment (Thöni, 2014; Orr, 2001).

- **Baseline (control) efficiency is a core moderator**:  
  * If the no-punishment baseline is already highly efficient (due to social preference, trust, or voluntary mechanisms), enabling punishment may have limited or even negative efficiency effects (van der Weele, 2012; Hwang & Bowles, 2012).

# 5) Prediction Guidance

- **Directionality**: Enabling peer punishment in PGG and close variants usually increases efficiency, unless:
    - The cost of punishment is too high,
    - The punishment technology is ineffective,
    - Social preferences already sustain high control efficiency,
    - Antisocial punishment or moral crowding effects dominate,
    - Monitoring and information are inadequate.

- **Dimension-driven adjustment**: The expected size of the efficiency gain is larger when:
    - Groups are larger (up to a point) and punishment is effective,
    - Punishment cost is low,
    - Baseline contribution rates (in controls) are low,
    - Monitoring/audit information is strong,
    - Social preference for cooperation is moderate (not extremely high or low).

- **Parameterization**: Several models provide explicit or semi-explicit formulas for equilibrium efficiency as a function of game parameters (see Levine & Modica, 2016; Acemoglu & Wolitzky, 2020; van der Weele, 2012; Saak, 2012; Noailly et al., 2009). These can be used to inform statistical or structural prediction models using design dimensions as inputs.

- **Heuristics when data is missing**:  
    - If control (no-punishment) efficiency is low, predicated efficiency with punishment is likely to be substantially higher, especially with low punishment cost and high effectiveness.
    - If control efficiency is already high, expect little or no efficiency gain from enabling punishment; may even see a decrease if trust/norms crowd out punishment.

- **Cautions**:  
    - When only behavioral (contribution/cooperation) outcomes are reported, infer efficiency changes only if group earnings/payoffs are also described.
    - Efficiency effects are not always monotonic or universal; moderators (player composition, group size, structure of monitoring, intrinsic motivation, antisocial punishment prevalence) can flip or mask the average effect.

# 6) Design Dimensions Highlighted Across Papers

Below is a summary of the 14 prediction dimensions:

**Directly Informed** (parameterized in models or directly analyzed as moderators of efficiency):  
- `player_count`  
- `num_rounds`  
- `all_or_nothing`  
- `mpcr`  
- `punishment_cost`  
- `punishment_tech`  
- `show_other_summaries` (in select models with monitoring/feedback)  
- `show_n_rounds` (in some repeated/finite-horizon models)

**Indirectly Informed** (discussed for relevance/context but not tightly parameterized):  
- `chat` (conceptually addressed as communication/coordination, Ehmke & Shogren, 2009)  
- `reward_exists`, `reward_cost`, `reward_tech` (occasionally considered in models where reward and punishment coexist, e.g., Sutter & Untertrifaller, 2020; Mulder, 2018; Shibayama, 2015)

**Contextually Discussed** (acknowledged but insufficient detail for modeling prediction):  
- `default_contrib` (framing rarely explicitly studied)  
- `show_punishment_id` (traceability/identity occasionally discussed as a feature influencing reputation, e.g., Saak, 2012)

**Effectively Missing**:  
- No direct modeling of `chat` as a binary dimension, nor explicit treatment of `default_contrib`.  
- Little/no direct attention to `show_punishment_id` outside a few adjacent models.  
- Sparse evidence on `reward_cost`, `reward_tech`, and their interaction with punishment in main efficiency models.

# 7) Important Limitations

- **Empirical evidence is lacking**: All digest papers are theoretical or simulation-based. There are no direct experimental or field data on realized efficiency changes from punishment treatments, limiting external validity and calibration.
  
- **Payoff-based outcomes not always measured**: Many papers report only behavioral changes (cooperation rates, punishment frequency), which do not always translate directly to efficiency improvements, particularly when punishment is costly or antisocial.

- **Design dimension coverage is uneven**: Key prediction moderators (e.g., chat, identity visibility, reward structure, default contribution framing) are under-studied or modeled only qualitatively. Not all possible game dimension combinations are systematically explored.

- **Ambiguity in real-world applicability**: The models often assume rational, homogeneous agents or stylized preference distributions. Real participant heterogeneity and bounded rationality may undermine model predictions.

- **Contextual and non-linear moderators**: Group composition, cultural context, antisocial punishment prevalence, trust, and intrinsic motivation can strongly moderate or reverse the average effect of punishment, creating substantial uncertainty for out-of-sample predictions.

- **Potential for disagreement/contradiction**: Some models (e.g., Hwang & Bowles, 2012; van der Weele, 2012; Orr, 2001) suggest conditions where punishment reduces efficiency, in contrast to standard models predicting universally positive effects.

- **Limited treatment of dynamic/learning behavior**: Most models analyze equilibrium outcomes, not real experimental trajectories (e.g., contribution decay or learning across rounds), leaving dynamic predictions less well-supported.

---

**Summary**:  
The literature set offers a rich, theory-driven foundation for predicting the efficiency effect of introducing peer punishment in PGG-like environments as a function of baseline efficiency and design parameters, particularly `player_count`, `mpcr`, `punishment_cost`, and `punishment_tech`. However, important design dimensions are understudied, real-world calibration is lacking, and contextual moderators can produce non-monotonic or even negative effects. Predictions based on this literature should be framed probabilistically and with explicit recognition of scope conditions and uncertainty.
