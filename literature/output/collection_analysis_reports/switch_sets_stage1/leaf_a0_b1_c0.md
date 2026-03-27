# 1) Evidence Base

This paper set consists entirely of theoretical (modeling, simulation, formal analysis) work, with no empirical or laboratory experimental studies included. The literature reviewed is very broad in terms of coverage of social dilemma environments, spanning standard public goods games (PGG), variants (threshold, networked, spatial, asymmetric, indirect reciprocity, trust, common pool resource, mutualisms), and many adjacent games (repeated Prisoner's Dilemma, coordination games, donation/helping games, auctions, and others). The analysis nearly always focuses on evolutionary, repeated, or structured-population models.

Virtually all studies focus on payoff-based group outcomes—such as group payoff, welfare, efficiency, surplus, social welfare, group productivity, or average group earnings—rather than on behavioral outcomes alone. However, these payoff-based outcomes are always derived from theoretical analysis, simulation, or formal equilibrium conditions, not from observed experimental data.

Most papers directly or indirectly address the role of incentive mechanisms, including punishment, reward, exclusion, sanctioning, partner selection, reputation, and institutional interventions. However, exact modeling of standard peer punishment as in canonical lab PGGs is rare; mechanisms analyzed are often analogous (e.g., exclusion, reputation-based, third-party, institutional, community-wide, indirect) rather than literal peer punishment with explicit cost/impact ratios.

In summary, this set delivers a comprehensive, highly diverse body of theoretical predictions and mechanistic analysis, with sparse direct modeling of all 14 PGG game design dimensions as found in contemporary experimental work, and with no direct experimental outcome data.

# 2) Task Relevance

## pgg_or_variant
- **Relevance**: Theoretical coverage of standard PGGs and close variants is high; many papers analyze exact PGGs, especially those with continuous or all-or-nothing contributions, repeated interaction, and networked or structured populations. However, a large share of studies focus on adjacent games (repeated PD, donation games, resource games, trust games, auctions, mutualisms, coordination games), making the overall relevance a mix of `exact`, `close`, and `adjacent`.

## punishment_or_sanctions
- **Relevance**: Theoretical modeling of punishment and sanctions is abundant, but the definition of "punishment" is broad—ranging from explicit peer or institutional punishment, to exclusion, reputation loss, ostracism, partner refusal, fine/fee mechanisms, or even efficiency-reducing threats. Few models match the canonical experimental peer punishment institution exactly; many others use adjacent incentive forms. Thus, coverage is best described as a mix of `exact` and `adjacent`, with the bulk of "punishment" being adjacent or indirect.

## efficiency_or_related_payoff_outcome
- **Relevance**: Nearly universal. All included papers—whether on PGGs or adjacent games, and regardless of mechanism—report on group payoff, efficiency (as defined by gains relative to the cooperative optimum), group welfare, total surplus, or similar outcomes, as primary theoretical results. Thus, this dimension is consistently `exact` or `close`.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes** (primary): All analyzed papers report efficiency—defined as group payoff relative to the fully cooperative benchmark—or closely analogous outcomes (group payoff, social welfare, surplus, or net earnings). Some papers provide explicit equilibrium payoffs under different mechanisms; others provide comparative statics or phase diagrams mapping payoff/efficiency across parameter ranges (e.g., as a function of group size, cost/benefit ratio, punishment cost, monitoring structure, network topology, reputation rules, etc.).
- **Non-payoff behavioral outcomes**: While often reported or modeled (e.g., cooperation rate, contribution rate, prevalence of defectors/punishers/cooperators, adoption of norms, partner selection), these are consistently distinguished from efficiency or group payoff in the theoretical models.

# 4) Main Findings Relevant To Prediction

## General Direction of Punishment’s Effect
- **Punishment often raises efficiency**: Across exact and adjacent models, the introduction of *well-designed* punishment mechanisms—peer, institutional, reputation-based, third-party, or exclusion—can move equilibrium group payoff from low (defection) toward the efficient cooperative optimum, especially in repeated, well-monitored, small to moderate-size groups, or networked populations with sufficient observability or reputation flow (e.g., [KANDORI, 1992]; [Camera & Gioffré, 2014]; [Jindani, 2020]; [Kitts, 2006]).
- **Critical dependence on punishment parameters**: Efficiency gains from punishment depend crucially on punishment cost to effect ratio, monitoring/observability structure (i.e., design dimensions like `punishment_cost`, `punishment_tech`, `show_other_summaries`, `show_punishment_id`), group size (`player_count`), the number of rounds (`num_rounds`), and MPCR.
- **Threshold or non-monotonic effects**: Many models show that punishment is only effective (i.e., increases group efficiency) if its strength or effectiveness exceeds key thresholds. Weak, costly, or poorly targeted punishment can decrease efficiency due to costs outweighing benefits ([Jia & Wang, 2025]; [Han et al., 2024]; [Quan et al., 2021]; [Nakao, 2009]).
- **Reward vs. punishment**: The literature frequently finds that reward mechanisms—especially when reputation-based and/or cost-effective—are as good as or superior to punishment, especially for promoting welfare rather than simply maximizing cooperation ([Han, 2022]; [Mondal et al., 2022]; [Hilbe & Sigmund, 2010]; [Han et al., 2024]).

## Negative or Mixed Punishment Effects
- **Punishment can harm efficiency**: If punishment is frequently misapplied (e.g., antisocial punishment, misidentification), too costly, or leads to retaliation/maladaptive punishment cycles, then group efficiency can be reduced relative to control ([Handfield et al., 2016]; [Ezeigbo, 2017]; [Ohtsuki et al., 2009]; [Jaffe, 2004]; [Han et al., 2024]).
- **Population structure matters**: In large, well-mixed, or highly heterogeneous populations, or where punishment is not reputationally visible or information is limited, punishment is often less effective or even counterproductive ([Suzuki & Akiyama, 2007]; [Sugaya & Wolitzky, 2023]; [Kurokawa, 2023]).

## Alternative Mechanisms
- **Exclusion and reputation**: Mechanisms such as peer exclusion, partner choice, dynamic network adaptation, and reputation-based access control can substitute for or outperform explicit costly punishment in raising efficiency ([Liu et al., 2019]; [Kang et al., 2024]; [Zschache, 2012]).
- **Conditional or context-dependent punishment**: Adaptive, targeted, or probabilistic punishment (e.g., proportional to payoff difference, conditional on reputation, or memory-based) tends to maximize efficiency ([Ohdaira, 2017]; [Luo & Zhao, 2013]; [Yan et al., 2021]).
- **Institutional and third-party punishment**: Specialized institutional or third-party punishment, if disciplined and not too costly, can enable large efficiency improvements especially when peer punishment falters ([Mohlin et al., 2023]; [Lippert & Spagnolo, 2011]).

## Dependence on Game and Population Design
- **Group size/number of players**: Efficiency gains from punishment are best sustained in small to moderate-size groups; with increasing group size, punishment's effectiveness can decline, become more costly, or be undermined by second-order free-riding or information constraints ([Suzuki & Akiyama, 2007]; [Gavrilets, 2015]).
- **Number of rounds**: Infinite or sufficiently long repeated interaction is a robust positive moderator; in finitely repeated games, especially with known endpoints, the threat of punishment is less credible, and efficiency may fall ([Matsushima, 2012]; [Lipman & Wang, 2000]).
- **Observability and monitoring**: When actions, histories, or identities are observable (`show_other_summaries`, `show_punishment_id`, reputation systems), punishment is more often efficiency-enhancing; with only local or no monitoring, positive effects are attenuated or lost ([KANDORI, 1992]; [Levine & Pesendorfer, 2007]).

## Baseline (Control) Efficiency as Moderator
- Where control efficiency (no-punishment) is already high due to repeated interaction, reputation, partner selection, or other pro-social mechanisms, the marginal gain from adding punishment is often small or negative (wasteful), as enforcement costs can exceed marginal gains ([Lie-Panis et al., 2024]; [Brandt & Sigmund, 2004]; [Kitts, 2006]).

# 5) Prediction Guidance

Given the evidence, the following principles should guide predictions of treatment (punishment-enabled) efficiency from design dimensions and control efficiency:

- **Baseline (control) efficiency is a powerful moderator**: If control efficiency is near the cooperative optimum, adding punishment may not increase and can decrease efficiency due to enforcement costs.
- **Critical thresholds for punishment**: Punishment increases efficiency only if effectiveness (punishment impact per unit cost, `punishment_cost` and `punishment_tech`) exceeds a game- and context-specific threshold (often tied to temptation payoff, discount factor, observability); otherwise, punishment may be wasteful.
- **Group size and rounds**: Smaller groups and longer interaction (higher `player_count` and `num_rounds`) favor larger efficiency gains from punishment; as groups grow, punishment efficacy declines unless backed by strong institutional, reputational, or exclusion mechanisms.
- **Observability and monitoring**: Enabling richer information feedbacks (`show_other_summaries`, `show_punishment_id`) sharply strengthens the positive effect of punishment on efficiency; poorly monitored or anonymous settings blunt the impact.
- **Type of punishment mechanism**: Institutional, third-party, or exclusion/information-based sanctions are typically more robust in promoting efficiency than simple peer punishment, particularly in large groups or with high heterogeneity.
- **Calibration matters**: Both underuse (weak, infrequent, or unconditional punishment) and overuse (frequent, high-cost, or erroneous punishment) can reduce efficiency.
- **Design features affecting second-order free-riding**: If punishment itself can be free-ridden (i.e., not enough punishers, or punishment of non-punishers is not enabled), efficiency gains are less likely to be realized.

**When evidence comes from non-payoff outcomes** (e.g., cooperation rate/contribution rate only), the literature warns that efficiency (payoff) may not covary; high punishment often raises cooperation but at net payoff loss due to punishment costs.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions:**
- `player_count` (group size): Frequently discussed, often parameterized; strong moderator of punishment impact, with effects declining as group size grows.
- `num_rounds`: Commonly considered; the effect of punishment is much stronger with longer or indefinite repetitions.
- `mpcr`: Central parameter affecting the cost/benefit of cooperation and the threshold for punishment effectiveness.
- `punishment_cost` and `punishment_tech`: Nearly all punishment modeling focuses on cost to punisher, effectiveness/strength, and the structure (peer, institutional, exclusion, etc.).
- `show_other_summaries`, `show_punishment_id`: Information and monitoring structure routinely highlighted as critical moderators.
- `reward_exists`, `reward_cost`, `reward_tech`: Many adjacent studies contrast reward and punishment; cost and technology of reward are analyzed.
  
**Indirectly informed/contextually discussed:**
- `all_or_nothing`: Explicitly varied in some models (discrete vs. continuous contribution).
- `show_n_rounds`: Sometimes manipulated or analyzed, especially regarding horizon effects.
- `show_punishment_id`: Considered primarily in reputation-based models and models with mixed public/private monitoring.
- `default_contrib`: Rarely modeled directly, but framing effects may be discussed.
- `chat`: Mentioned in some network/coordination models as a communication channel.
- `dynamic networks`/`partner selection`/`ostracism`/`exclusion`: Core to several adjacent models, but not formalized as prediction dimensions.

**Effectively missing:**
- No empirical direct modeling of `default_contrib` and `chat` as in laboratory treatments.
- Explicit design dimensions for dynamically changing group composition or real-time communication are rare.
- Multi-mechanism or factorial variations (i.e., crossing reward and punishment or combining with chat, etc.) are analyzed in a few synthetic models, but not comprehensively.

# 7) Important Limitations

- **No empirical laboratory data**: Entire analysis is theoretical/simulation, with no experimental effect sizes, confidence intervals, or real-world data on punishment-enabled vs. disabled efficiency.
- **Heterogeneity of mechanisms**: "Punishment" in the literature ranges from literal peer deduction to exclusion, reputation loss, partner switching, institutional fines, and more; not all match the standard peer punishment in control/treatment labs.
- **Transferability of quantitative predictions**: Explicit payoff predictions are model-specific; thresholds and effect sizes for one parameter constellation may not generalize, especially to complex, multi-dimensional experimental designs.
- **Sparse or missing direct evidence for some design dimensions**: Few studies model effects of default contribution framing, chat, or specific interface design elements; network, monitoring, and incentive structure are emphasized, but some dimensions (e.g., dynamic group size, communication) are under-modeled.
- **Ambiguity and disagreement remain**: Some models predict positive, others negative, or threshold/conditional effects of punishment on efficiency depending on cost/impact, error rates, network structure, and information availability.
- **Behavioral mechanisms and cognitive factors**: Important factors such as probability weighting (prospect theory), strong social preferences, or mistaken/antisocial punishment are handled in only a fraction of models.
- **Outcome mismatch risk**: Many findings are about cooperation rates rather than efficiency; some models highlight that high cooperation can co-occur with lower group payoff due to excessive punishment costs.

**In summary:** This literature base is broad and rich in theoretical mechanisms mapping design dimensions to group payoff/efficiency changes under punishment. However, it lacks the direct, empirical, game-by-game counterfactuals most valuable for parametric prediction of peer punishment treatment efficiency as a function of lab-design features and control efficiency. The direction and size of efficiency changes are often conditional, context-sensitive, and non-monotonic, requiring careful mapping from modeled mechanisms to the empirical settings of interest.
