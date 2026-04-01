# 1) Evidence Base

The paper set consists of approximately 300 theoretical papers, with a pronounced emphasis on formal modeling, evolutionary game theory, and simulation results. There is a near-total absence of laboratory, field, or empirical studies with real payoff data. The theoretical coverage of the classic linear Public Goods Game (PGG) and close variants (e.g., common pool resource dilemmas, threshold/step public goods, indirect reciprocity games) is exceptionally broad. Models span a wide range of assumptions and game forms, including both institutional and peer punishment, reward, social exclusion, norm-based sanctioning, and institution-building. 

Outcomes are predominantly analyzed in terms of Nash or evolutionary stability, stationary distributions of strategies, and often as equilibrium or long-run average payoffs (group welfare, mean fitness, group productivity, total earnings, etc.), which map directly to the efficiency outcome of interest. Some models provide phase diagrams or explicit analytic conditions, while others rely on simulation or qualitative stability analysis.

Despite the diversity of models, the evidence base is largely "narrow" from a prediction perspective: nearly all findings are theoretical (deductive or simulated), with relatively little variability in methodological approach, and no direct estimation or statistical generalization from empirical measurement. Nevertheless, the diversity of model structures, parameter sweeps, and contexts means that the theoretical parameter space explored is very wide, allowing for inferences about moderator effects and boundary conditions for punishment efficacy.

# 2) Task Relevance

**pgg_or_variant**:  
- The relevance of the literature to the classic Public Goods Game or its direct variants is `exact` for a large proportion of the set, including most of the main theoretical models (e.g., Cressman et al. 2012; Eldakar et al. 2007; Gintis 2000; Oya & Ohtsuki 2017; Deng et al. 2012; Powers et al. 2023, and many others).  
- A substantial minority of papers use adjacent games (e.g., repeated Prisoner's Dilemma, indirect reciprocity, mutualism models), for which the mapping to PGGs is close or adjacent depending on details.
  
**punishment_or_sanctions**:  
- The majority of models include `exact` representations of costly punishment or sanctions as a treatment variable, often directly distinguishing between peer punishment, institutional punishment, social exclusion, and reward as alternative or co-occurring interventions.
- Some papers analyze adjacent mechanisms (e.g., partner choice, reputation-based withholding), which functionally overlap with sanctions but may not be coded as explicit punishment interventions.  
- A notable subset explicitly explores anti-social punishment, retaliation, corruption, and institutional failures as moderators.
  
**efficiency_or_related_payoff_outcome**:  
- Many papers show `exact` relevance by tracking collective group payoff, welfare, fitness, or efficiency (i.e., mean group payoff relative to the maximum possible, or the efficiency ratio as defined in the prediction task).
- Several others are close, focusing on outcomes like group achievement, population mean fitness, or long-run average payoffs that are directly interpretable as efficiency measures.  
- A substantial number only report behavioral outcomes (contribution rates, strategy frequencies), for which effects on efficiency are inferred but not always directly quantified, meriting `adjacent` or `weak` relevance for the prediction outcome.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes**:  
- _Efficiency_ (ratio of actual group payoff to payoff under full cooperation) is a primary or explicit outcome in numerous papers.
- Related measures: group total payoff, mean fitness, group welfare, aggregate earnings, and outcome ratios expressed directly relative to equilibrium or theoretical optimum are prevalent.
- Some models use group achievement (e.g., attainment of collective thresholds) as a direct surrogate for efficiency.
- Several papers provide explicit quantitative predictions or parameterized formulas linking game design dimensions, control efficiency, and treatment efficiency.

**Non-payoff (behavioral) outcomes**:  
- Many papers measure and analyze:  
    - Cooperation/contribution rates  
    - Prevalence/frequency of strategy types (cooperator, defector, punisher, rewarder)
    - Norm compliance rates
    - Evolutionary stability/basin of attraction for various strategies  
- Some models report only stationary distributions or transition probabilities, which must be translated cautiously into efficiency implications.
- Behavioral outcomes do not always correspond to efficiency outcomes: higher cooperation does not necessarily imply higher efficiency if, for example, punishment is costly or is misapplied.

# 4) Main Findings Relevant To Prediction

**Synthesis across main axes:**

- **Effect of Enabling Punishment:**  
  - The dominant theoretical result is that enabling punishment—under favorable conditions—*can* increase group efficiency relative to the no-punishment baseline by sustaining higher levels of cooperation, thereby increasing collective payoffs (Gintis 2000; Boyd & Richerson 1992; Eldakar et al. 2007; Powers et al. 2023).  
  - The efficiency effect is almost never universal. It is highly contingent on multiple design dimensions—including punishment effectiveness (impact per cost), group size, punishment cost, population structure, presence of anti-social punishment/retaliation, error rates, institutional integrity, and others.

- **Boundary Conditions & Moderators:**  
  - _Punishment Cost and Effectiveness_: The positive effect of punishment on efficiency is strongest when punishment is inexpensive to apply and highly effective (i.e., imposes a large cost on defectors per unit cost to punishers). If punishment is too costly, or has little deterrence value, it often reduces efficiency by destroying resources (Gintis 2000; Eldakar et al. 2007; Okada & Bingham 2008; Wang & Lv 2019).
  - _Group Size_: Efficiency gains from punishment are diluted or may reverse as group size increases, unless punishment is institutionally coordinated or costs are shared (Powers & Lehmann 2013; Eldakar et al. 2013; Wang & Lv 2019).  
  - _Population Structure_: Spatial structure and group-level selection generally increase the efficacy and efficiency effect of punishment (Helbing et al. 2010; Oya & Ohtsuki 2017; POLLOCK 1988; Cooney 2025), but effects may be neutral or negative in well-mixed populations unless initial punisher prevalence is high.
  - _Retaliation and Anti-social Punishment_: The effect of punishment on efficiency is frequently negative or null if anti-social punishment (punishing cooperators) or retaliation is possible (Rand et al. 2010; Powers et al. 2013; Wolff 2012; Hauser et al. 2014; Janssen & Bushman 2008).

- **Institutional vs. Peer Punishment:**  
  - Institutionalized punishment (especially with cost-sharing and transparency) is generally more robust in sustaining efficiency compared to peer punishment, which is more vulnerable to second-order free-riding, anti-social use, and excessive cost (Schoenmakers et al. 2014; Ishikawa & Fontanari 2025; Dercole et al. 2013).
  - Social exclusion and ostracism mechanisms (as an alternative to costly punishment) can achieve similar or higher efficiency, often more robustly (Sasaki & Uchida 2013; Deng et al. 2012).

- **Role of Rewards and Reputation:**  
  - Reward-only mechanisms are sometimes found to increase efficiency as much or more than punishment, especially in settings with high error rates or weak punishment (Dong et al. 2019; Sasaki & Uchida 2014).
  - Reputation systems and communication mechanisms can substitute for or amplify the effects of punishment, often leading to higher efficiency by reducing the need for costly sanctions (dos Santos et al. 2011; Milinski 2016).

- **Control Game Efficiency as Moderator:**  
  - The baseline (control) efficiency is a strong predictor of treatment (punishment-enabled) efficiency. When baseline efficiency is high (due, e.g., to high MPCR or strong reputational mechanisms), adding punishment yields little incremental gain or can even harm efficiency due to unnecessary costs. When baseline efficiency is low, effective punishment is more likely to yield large efficiency gains (Cressman et al. 2012; Adami et al. 2016; Wang & Lv 2019).

- **Contextual and System-level Constraints:**  
  - Ecological and resource dynamics can override the potential for efficiency gains: if resources cannot renew or population dynamics are unfavorable, even perfect cooperation achieved via punishment may not improve efficiency (Chen & Perc 2014; Lee et al. 2017; Wang et al. 2024).
  - Corruption, bribery, and institutional dysfunction can negate or reverse the positive effects of punishment on efficiency (Fang et al. 2020; Lee et al. 2015, 2017).
  - The presence of mechanisms for anti-social rewarding can also foil the efficacy of punishment/reward in improving efficiency (dos Santos 2015).

**Empirical Alignment:**  
  - Laboratory experimental findings (as interpreted by theory papers) often show increases in cooperation, but efficiency gains are limited and observed mainly in long-run or repeated settings with stable groups and low punishment costs (Guala 2012; Milinski & Rockenbach 2012).
  - In field-like and institutionally rich environments, real-world sanctions tend to be less costly (gossip, ostracism) and more effective at sustaining efficiency than classic costly peer punishment (Guala 2012; Fehr & Schurtenberger 2018).

# 5) Prediction Guidance

- **Use of Game Design Dimensions:**  
  - Theoretical models provide direct mappings or functional relationships between key design dimensions (player_count, num_rounds, mpcr, punishment_cost, punishment_tech, population structure) and the expected efficiency gain from enabling punishment.  
  - For a given baseline (control) efficiency, expect higher treatment (punishment-enabled) efficiency when:  
      - Punishment is highly effective per unit cost  
      - Punishment cost is moderate or low  
      - Group size is small to moderate (or if institutional mechanisms coordinate sanctioning/cost-sharing in larger groups)  
      - Population structure supports clustering or limited dispersal  
      - Anti-social punishment and retaliation are ruled out or normatively constrained  
      - There is no institutional corruption or instability; honesty and transparency can be maintained  
      - The baseline efficiency is low or moderate (leaving room for improvement)
  - Expect limited or negative efficiency effects when:  
      - Punishment cost is high  
      - Punishment efficacy is low  
      - Group size is large without coordination or cost sharing  
      - Anti-social punishment or easy retaliation is possible  
      - Baseline efficiency is already high  
      - Resource/ecological constraints limit the benefit of increased cooperation

- **Predictive Mapping:**  
  - For standard PGGs with typical parameters (and absent strong moderators like anti-social punishment, corruption, or high resource scarcity), enabling punishment is predicted to increase average efficiency, often substantially if control efficiency is low. The exact magnitude depends on the specific parameterization—some models provide explicit phase boundaries or formulas for this mapping (e.g., Deng et al. 2012; Wang & Lv 2019; Jiao et al. 2020).
  - Where outcomes are derived from non-payoff behavioral measures, translate with caution: increased cooperation typically, but not invariably, implies higher efficiency.

- **Quantitative Predictions:**  
  - Caution is warranted in making exact quantitative predictions—while explicit models exist, parameterization to real environments or specific experimental designs may not be direct. Use functional relationships and relative effect predictions rather than absolute values unless the model precisely matches the target design. 

- **Absence of Evidence:**  
  - For prediction of efficiency under manipulation of dimensions such as chat, show_punishment_id, default_contrib, or reward_enabled (without reward data), the literature is sparse or missing.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed (widely manipulated/central in models):**  
- `player_count` (group size): Frequent—many models analyze effect of group size on punishment efficacy and efficiency (e.g., Bowles & Gintis 2004; Eldakar et al. 2007).
- `num_rounds`: Often varied; typically, more rounds/repetition enhances punishment efficacy, per classic reciprocity logic.  
- `mpcr` (marginal per capita return): Key parameter modulating baseline efficiency and the potential room for punishment to improve outcomes.  
- `punishment_cost`, `punishment_tech` (punishment magnitude): Central focus—almost all models analyze cost/effect balance as main moderator.
- `all_or_nothing`: Present in step/threshold models; influences ability to support cooperation.  
- `reward_exists`, `reward_cost`, `reward_tech`: Addressed in many models contrasting or combining reward with punishment.
- `population_structure`: Frequently analyzed as spatial structure, networks, migration/group selection, etc. (maps to player_count & beyond).

**Indirectly informed or occasionally analyzed:**  
- `chat`/communication: Considered occasionally; generally shown to boost cooperation and sometimes efficiency, though not always modeled in combination with punishment.
- `show_punishment_id` (punisher identity): Important in models of retaliation, anti-social punishment, and reputation; visibility moderates retaliation risk and punishment uptake.
- `show_other_summaries`, `show_n_rounds` (information/feedback): Sometimes modeled as transparency or information structure; crucial for reputation and institutional punishment efficacy.
- `default_contrib`: Rarely manipulated directly; discussed occasionally in terms of framing effects or social default.

**Contextually discussed or effectively missing:**  
- `default_contrib`, `chat`, and `reward` dimensions often only discussed as background or are not systematically manipulated.
- Multi-dimensional interaction (e.g., interplay of chat and punishment, or default-contribute and punishment) is almost always absent; models typically manipulate one to three variables at a time.

# 7) Important Limitations

- **Theoretical Generalization:**  
  - Nearly all findings are derived from theory or simulation. There is very limited empirical constraint or real-world calibration, so generalizability to laboratory or natural settings may be limited, especially under behavioral heterogeneity or unforeseen contexts.

- **Absence of Empirical Effect Sizes:**  
  - The set lacks directly measured or meta-analyzed empirical effect sizes needed to calibrate quantitative predictions with high confidence.

- **Exclusion of Certain Design Dimensions:**  
  - Dimensions such as `chat`, `show_punishment_id`, `default_contrib` are rarely or never manipulated in combination with punishment in the theoretical literature.
  - Multi-dimensional effects (e.g., interaction between chat and punishment, or chat and group size) remain under-explored.

- **Ambiguity in Nonlinear/Structured Games:**  
  - For threshold, step, or nonlinear public goods games, and in structurally complex models (spatial, hierarchical, institutional), the effect of punishment can be highly parameter-dependent and sometimes ambiguous.
  - Population structure and ecological/resource constraints can dominate punishment effects, sometimes making efficiency gains impossible even with perfect cooperation.

- **Dependence on Behavioral Assumptions:**  
  - Many models assume infinite populations, evolutionary dynamics, full rationality, or certain forms of social learning; these may not mirror short-run or finite-population laboratory/game contexts.
  - The treatment of anti-social punishment, retaliation, and second-order free riding is inconsistent across models, leading to divergent predictions when these are possible.

- **Sparse Coverage of Some Moderators:**  
  - The impact of dynamic features like bonus/penalty randomness, noisy monitoring, learning rate heterogeneity, or network updating rules is only explored in a small subset of models.

**In summary:** The literature provides strong, direct, and nuanced theoretical grounding for predicting the effect of punishment on efficiency in PGG-like environments as a function of control efficiency and core design dimensions (group size, rounds, punishment cost/tech, structure). However, many details must be interpreted contextually, non-payoff outcomes must be distinguished, and limitations of theoretical generalization and missing empirical calibration must be recognized. Some dimensions remain under-explored, and payoff-based efficiency effects are highly contingent on game design, institutional, and population parameters.
