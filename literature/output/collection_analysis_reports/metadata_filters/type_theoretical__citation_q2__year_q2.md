# 1) Evidence Base

This paper set comprises 100 papers, entirely theoretical, with no direct empirical or laboratory experiments. The coverage of the core prediction task—predicting treatment efficiency in public-goods-game (PGG) environments with and without peer punishment—ranges from exact (many PGG theory papers with explicit efficiency analysis) to close or adjacent (papers addressing efficiency, punishment, or public-goods-like environments but not all three together, and several focusing on behavioral or evolutionary dynamics without direct efficiency outcomes). Though broad in game-theoretic scope and rich in analyses of mechanism, structure, and parameter dependencies, the absence of direct empirical treatments or effect-size measurements from laboratory or field data does limit its direct applicability to real-world PGG predictions.

# 2) Task Relevance

### Relevance Labels:
- **exact**: Directly addresses PGGs/variants, punishment/sanctions, and efficiency/payoff.
- **close**: Encompasses core PGG elements or efficiency, but with partial or indirect coverage.
- **adjacent/weak/none**: Lacking one or more core aspects.

**a) pgg_or_variant**:
- Most papers (30+ entries) analyze the standard or slightly modified PGG (relevance=exact or close).
- A substantial portion are adjacent (e.g., repeated Prisoner's Dilemma, threshold games, snowdrift games, resource management, donor-recipient games).
- About a third focus on indirect or adjacent game structures (e.g., network sharing games, evolutionary or stratified PD games).

**b) punishment_or_sanctions**:
- Punishment is treated as a core mechanism in roughly half the set, with many analyzing parameterized forms of punishment (cost, impact, targeting, centralized vs. decentralized, institutional/pool vs. peer, probabilistic, graduated, with or without anti-social punishment). Some address reward as a counterpart.
- Several papers discuss only behavioral correlates (norm enforcement, social exclusion, reputation loss) or mechanisms such as insurance, exclusion, or donation, which are only analogous to punishment.
- Some only touch on punishment as a background mechanism.

**c) efficiency_or_related_payoff_outcome**:
- A number of papers (especially in the `exact` subset) directly model or report efficiency, group payoff, surplus, welfare, or average payoff as the main outcome.
- However, many others focus primarily on cooperation/contribution rates, stationary frequencies of strategies, or evolutionary stability (behavioral measures), which may only loosely infer efficiency.
- A substantial minority do not report efficiency or payoff at all.

# 3) Outcomes Measured In The Literature

### Payoff-based Outcomes (`exact` or `close` relevance)
- **Direct efficiency or total group payoff**: Several theory papers calculate, simulate, or derive explicit relationships for group efficiency as a function of punishment, group size, MPCR, and other game design parameters (e.g., Cong et al., 2016; Sasaki, 2014; Hetzer & Sornette, 2013; Roberts, 2013; Ye et al., 2016; Eldakar et al., 2013; Wang et al., 2015 (VPEF)).
- **Group welfare, surplus, total coins generated**: Used interchangeably with efficiency.
- **Stationary distribution of payoffs**: Calculated in evolutionary or replicator frameworks.

### Behavioral Outcomes (not efficiency; sometimes "adjacent" to payoff)
- **Cooperation/contribution rates**: Most common non-payoff outcome, often linked to predictions about potential efficiency but not directly measured as such.
- **Punishment/reward frequencies**: Frequently analyzed as outcome variables but distinct from efficiency unless explicitly mapped to costs/payoffs.
- **Strategy abundance or equilibrium frequencies**: Used predominately in evolutionary models.
- **Norm compliance, exclusion efficacy, or prevalence of honest strategies**: In some adjacent papers, these are measured but not mapped to group payoff.

**Explicitly, many papers do not quantify the translation of higher cooperation or punishment frequency into final group payoffs or efficiency. Several note that increased punishment can lower payoffs if the costs outweigh cooperation gains, or in the presence of anti-social punishment.**

# 4) Main Findings Relevant To Prediction

**Aggregated key findings, distinguishing scope, empirical (simulated/theoretical), and outcome type:**

- **Enabling Punishment Can Increase Efficiency**: Numerous theory and simulation papers predict that enabling (peer or institutional) punishment in a PGG increases group efficiency under typical parameterizations—provided the cost/benefit ratio of punishment is favorable (low punisher cost, high penalty for defectors), and strategic or evolutionary stability can be achieved (e.g., Roberts, 2013; Hetzer & Sornette, 2013; Cong et al., 2016; Wang et al., 2015 (VPEF); Sui et al., 2017). This applies especially when the mechanism avoids wasteful or anti-social punishment.

- **Critical Parameter Dependence/Threshold Effects**: The positive effect of punishment on efficiency is not universal; it depends on design dimensions such as:
  - **Punishment Cost and Effectiveness:** Punishment must be sufficiently cheap and impactful to deter defection without wasting resources (Roberts, 2013; Farjam et al., 2015; Eldakar et al., 2013; Sui et al., 2017).
  - **MPCR (Enhancement factor):** Punishment's efficiency benefit is strongest in low-MPCR or "harsh" environments, but in high-MPCR settings, punishment may not increase, or could even reduce, efficiency (Farjam et al., 2015; Ye et al., 2016).
  - **Group Size/Player Count:** While classic logic predicts diminishing returns to punishment in large groups, several theory papers counter that, under coordinated or institutional punishment, larger groups can see greater efficiency increases (Sasaki, 2014; Hwang, 2017; Boyd et al., 2014), provided coordination/monitoring is achieved and second-order free-riding is controlled.
  - **Game Iteration/Num Rounds:** Repeated games strengthen the efficiency gains from punishment compared to single-shot; longer association times make punishment more effective (Roberts, 2013; Eldakar et al., 2013).
  - **Technology and Structure of Punishment:** Centralized or tax-based, graduated, and well-targeted punishment (as opposed to decentralized or anti-social) robustly promote efficiency (Cong et al., 2016; Yao & Chen, 2014; Lee & Iwasa, 2014; Farjam et al., 2015; Chassang & Zehnder, 2016).
  - **Reward Exist/Compensation Mechanisms:** Balanced reward and punishment institutions outperform pure punishment or pure reward for efficiency (Cong et al., 2016; Yao & Chen, 2014). Pool punishment (institutional, publicly funded) can be more effective than peer (individual) punishment, which is vulnerable to second-order free-riding and anti-social punishment.
  - **Network/Information Structure:** Network connectivity and monitoring tech moderate whether punishment improves efficiency; with poor information (limited monitoring or incomplete networks), peer punishment's effect on efficiency is muted or negative (Chung et al., 2013; Balmaceda & Escobar, 2017; Larson, 2017).
  - **Optional Participation:** Punishment combined with optional participation can promote full cooperation and higher efficiency even when it fails under compulsory participation (Sasaki, 2014; Wang et al., 2015 (VPEF)).

- **Negative or Non-monotonic Effects**: Under certain conditions, punishment fails to improve or even lowers efficiency:
  - **High Cost or Anti-social Punishment:** When punisher costs are high, when antisocial punishment is present, or when punishment is poorly targeted, group efficiency can decrease (Handfield et al., 2016; Farjam et al., 2015; Gao et al., 2015).
  - **Retaliation and Counter-punishment:** Environments that allow for retaliation can nullify (or even reverse) the group-level efficiency gains from punishment (Noussair & van Soest, 2014).
  - **'Too Much' Punishment:** Some models find that excessive punishment leads to resource depletion, breakdown of institutions, or population collapse; efficiency gains are maximized at intermediate levels of punishment combined with reward (Cong et al., 2016; Yao & Chen, 2014).

- **Non-PGG or Behavioral Outcome Papers**: Many adjacent papers confirm that punishment increases cooperation rates, but either do not report, or caution about, the mapping to efficiency: frequent or indiscriminate punishment may raise cooperation but still lower or fail to improve efficiency if net resource cost is too high (Johnson, 2015; Yamamoto & Okada, 2016; Handfield et al., 2016).

# 5) Prediction Guidance

**Implications for predicting the efficiency of punishment-enabled PGGs from game dimensions and baseline (control) efficiency:**

- **Strong Theoretical Support for a Positive Effect**, *When Parameters are Favorable* (punisher cost < marginal benefit of cooperation enforced by punishment): If, in a control game, efficiency is low and design parameters support effective, low-cost punishment (sufficient monitoring, low punishment cost, high punishment impact, high network connectivity or institutional enforcement), then enabling punishment is likely to substantially increase efficiency, sometimes close to the full cooperation maximum.

- **Conditional and Non-monotonic Effects**:
  - **Low or Negative Impact Possible**: If the punishment cost is high relative to punishment impact, or if antisocial/retaliatory punishment is possible, or if MPCR is already high (i.e., cooperation is not a severe dilemma), enabling punishment may have little or even negative impact on efficiency (Farjam et al., 2015; Handfield et al., 2016; Noussair & van Soest, 2014).
  - **Network and Monitoring**: If monitoring/observation is limited, or the network is incomplete/peripheral, the efficiency gain from punishment may be negligible or negative.
  - **Pool (Institutional/Tax-based) vs Peer (Decentralized) Punishment**: Institutional (pool) punishment schemes or ones with a pool-funded system are more robustly positive in efficiency impact than peer punishment, which is more vulnerable to inefficiency from retaliation/antisocial punishment and targeting failure.

- **Reward, Communication, and Balanced Incentive Structures**: Models suggest that inclusion of rewards alongside punishment and enabled communication can have greater/robust positive effects on efficiency—pure punishment is less robust than balanced institutional incentives (Cong et al., 2016; Yao & Chen, 2014).

- **Parameter Thresholds Are Critical**: For moderation by design, predictions should be tuned based on explicit cost/benefit thresholds and model-derived formulas (e.g., p < q*b/c in Roberts, 2013; analytical thresholds for punishment/reward parameters in Cong et al., 2016 and Sui et al., 2017).

- **Heterogeneity and Structure Required**: The effect of punishment is stronger in homogeneous, well-mixed or well-coordinated environments; in the presence of strong heterogeneity or dynamic partner choice, substitute mechanisms (preferential interaction, network rewiring) can replace the need for punishment to maintain efficiency.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed** (empirically or analytically integrated into efficiency predictions with punishment):
- **player_count**: Explicit comparative statics and threshold analyses (most exact and close papers).
- **num_rounds**: Often directly analyzed for impact on reputation, evolutionary stability, and punishment efficacy.
- **mpcr**: Central to nearly all analytic and simulation models of PGG efficiency and punishment thresholds.
- **punishment_cost & punishment_tech**: Core focus of many models—differentiating peer, institutional, graduated, centralized, and networked enforcement.
- **reward_exists, reward_cost, reward_tech**: Covered in most institutional-incentives models.
- **all_or_nothing**: Many models use binary (all or nothing) choice; several analyze continuous/differentiated contribution levels.
- **show_other_summaries, show_punishment_id**: Some network and monitoring papers touch on these dimensions, especially regarding how visibility/observability affects punishment efficacy.
- **show_n_rounds**: Discussed as a factor in repeated game/patience models.
- **chat**: Rarely directly analyzed, but communication is recognized as a robust efficiency booster (Noussair & van Soest, 2014).
- **default_contrib**: Only very rarely specified; typical models assume no default framing.
- **punishment_tech**: Institutional reward/punishment, peer punishment, and tax-based schemes well represented.

**Indirectly informed/incomplete**:
- **chat, default_contrib, show_n_rounds**: Occasionally discussed for communication effects or transparency but not formally modeled.
- **reward_cost, reward_tech**: Present in fewer papers, some only as comparisons to punishment.

**Missing/Insufficiently covered**:
- **default_contrib**, **chat**, and **some display/information conditions** (e.g., show_n_rounds, show_other_summaries) receive little direct attention in relation to efficiency.

# 7) Important Limitations

- **No Empirical Effect Sizes**: All evidence is theoretical or simulation-based; there are no direct empirical or experimental measurements of efficiency gains from enabling punishment in real groups or laboratory settings.
- **Treatment of Anti-Social and Retaliatory Punishment**: While some models account for anti-social punishment, most assume or require its absence for positive efficiency effects; empirical settings may differ.
- **Translatability from Behavioral to Efficiency Outcomes**: Many models infer efficiency from cooperation rates or frequencies; the precise mapping can differ, especially when punishment is costly.
- **Breadth and Diversity of Paradigms**: Not all models fit the standard continuous-contribution multi-round PGG with peer punishment; many are in adjacent or structurally related games (e.g., network sharing, PD, trust games, resource management).
- **Parameter Sensitivity and Lack of Universality**: The literature is cautious—punishment does not always increase efficiency, and strong dependence on cost/benefit thresholds, monitoring structure, heterogeneity, and institutional design is repeatedly emphasized.
- **Sparse Coverage of Some Design Features**: Dimensions like chat, default contribution framing, and summary display are infrequently analyzed in relation to efficiency.
- **Uncertainty in Mixed or Ambiguous Cases**: Several papers find mixed, non-monotonic, or U-shaped effects (e.g., too much punishment, high MPCR, group size extremes).
- **No Human Subject Generalizability**: Without empirical corroboration, the mapping from theoretical/simulation results to actual human groups remains uncertain.

---

In summary, the literature provides strong and nuanced *theoretical* guidance: enabling punishment in PGG-like environments is likely to increase efficiency, but only under favorable combinations of key design parameters. Predicted efficiency gains are highly contingent on punishment cost-effectiveness, game structure, and participant coordination, and may disappear or reverse under adverse conditions (high cost, antisocial punishment, retaliation, limited monitoring, or structural constraints). The absence of empirical evidence limits quantification and external validity of these predictions.
