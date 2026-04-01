# 1) Evidence Base

The paper set is both large and rich, containing **238 papers** with a diversity of theoretical, simulation-based, and empirical (mostly lab experimental) studies. There is a strong predominance of theoretical/simulation work; empirical lab experiment papers are much less common. The majority of studies focus on **public goods games (PGGs)** and close variants, with a smaller but significant minority addressing adjacent dilemma games (e.g., snowdrift, prisoner's dilemma). Most included studies examine the **effects of punishment or sanctioning mechanisms** on cooperation, and approximately a third directly report or analyze **payoff-based efficiency outcomes**; many others focus predominantly on behavioral metrics (contribution rates, strategy frequencies). Particularly for **punishment-enabled vs. punishment-disabled efficiency prediction**, the evidence base is robust but with notable empirical and design variation, and some papers provide directly quantitative outcome data, while others provide only qualitative or indirect evidence.

---

# 2) Task Relevance

### a. pgg_or_variant
- **Exact**: The majority of studies focus precisely on PGGs or threshold public goods games (TPGGs), including both standard and spatial/networked variants.
- **Close**: Some papers use adjacent social dilemmas (N-person snowdrift games, CRDs, prisoner's dilemma with group/leader punishment), which share the key incentive structure but differ in payoff aggregation or participation rules.
- **Adjacent/Weak**: A large tail of papers examine closely related games (iterated PD, trust games, resource games) or agent-based models inspired by, but not identical to, PGGs.

### b. punishment_or_sanctions
- **Exact**: Many studies manipulate standard costly **peer or institutional punishment**—either endogenous (peer), exogenous (institutional/pool), or variants (exclusion, ostracism, fine redistribution).
- **Close**: Some model punishment analogs (e.g., automatic/third-party punishment, reward mechanisms with punitive aspects, or exclusion as the main sanction).
- **Adjacent/Weak**: Others focus on **reward**, **partner switching**, or mechanisms that function as indirect punishment (e.g., link breaking, reputation-based exclusion), not always mapping cleanly onto real PGG punishment options.

### c. efficiency_or_related_payoff_outcome
- **Exact**: About one third of the studies provide efficiency or closely related **welfare, group payoff, total earnings, or surplus** measures as explicit outcomes, comparing treatment (punishment-enabled) to control (punishment-disabled) games.
- **Close**: Many report only **behavioral outcomes** but discuss efficiency in interpretation, provide formulas or theoretical equilibrium payoffs, or report payoff changes in simulation.
- **Adjacent/Weak**: A considerable subset measure only cooperation/contribution rates, punishment/reward frequencies, or norm compliance; these are not payoff-based but correlate with efficiency under ideal conditions. Some papers offer only mechanistic arguments or qualitative predictions about efficiency.

---

# 3) Outcomes Measured In The Literature

## Payoff-Related Outcomes
- **Efficiency**: Explicitly measured as total group payoff / maximum possible payoff (full cooperation) in a substantial fraction of papers (e.g., Pi et al., 2022; Wu et al., 2014; Sun et al., 2025).
- **Group Payoff, Welfare, Surplus, Earnings**: Many report average group payoff, sometimes mapped to efficiency ratios; occasionally total earnings or surplus (e.g., Kol'veková et al., 2021).
- **Related Outcomes**: Some use group "achievement" (fraction achieving a threshold), welfare, or resource sustainable yield as proxies.

## Non-Payoff Behavioral Outcomes
- **Contribution/Cooperation Rate**: Most frequently reported; measures the fraction of rounds or players contributing/cooperating.
- **Strategy Frequencies**: Evolutionary studies report fractions of cooperators, punishers, defectors, loners, etc.
- **Punishment/Reward Frequency**: Incidence and distribution of punishment or reward actions.
- **Norm Compliance, Trust, Reputation**: Some papers focus on norm-following behavior, reputation updates, or trust outcomes.

**Distinction:** Only **payoff-related outcomes**—not behavioral metrics—are valid for directly addressing the efficiency prediction task. Many studies rely on behavioral outputs and infer efficiency relationships, requiring careful qualification when used.

---

# 4) Main Findings Relevant To Prediction

## Synthesis Across Evidence

- **Punishment Typically Raises Efficiency, But Context Matters**: Enabling peer or institutional punishment in PGGs usually (though not universally) increases group efficiency, sometimes dramatically—particularly when the control (punishment-disabled) setting has low efficiency due to widespread defection (e.g., Wang et al., 2010; Wu et al., 2014; Sun et al., 2025).

- **Cost and Effectiveness of Punishment Are Key Moderators**: Lower **punishment cost**, higher **punishment magnitude/effectiveness**, and higher **marginal per-capita return (MPCR)** amplify the positive effect of punishment on efficiency (Wu et al., 2014; Zhuang et al., 2012; Gao & Liang, 2020). High punishment cost or weak punishment can nullify or reverse the efficiency gain, sometimes making punishment inefficient, especially if antisocial punishment or overuse is prevalent (Quan et al., 2018; Wang et al., 2020).

- **Network Structure/Population Heterogeneity Strongly Shapes Outcomes**: Spatial structures (e.g., lattices, small-world, scale-free networks) allow punishment to be more effective and less costly due to localized clustering and reciprocity (Cui et al., 2022; Noailly et al., 2009). Well-mixed settings often require stronger or more costly punishment to achieve comparable efficiency improvements (Kol'veková et al., 2021).

- **Peer vs. Institutional Punishment**: Both forms increase efficiency under the right conditions, but institutional (pool) punishment, especially when funded by taxes (not voluntary contributions), achieves higher, more stable efficiency and can solve second-order punishment problems (Yang & Yang, 2024; Yao & Chen, 2014; Sasaki, 2014). However, ineffective or too costly institutional punishment can decrease efficiency, particularly if the punishment is not well matched to the social dilemma (Isakov & Rand, 2012).

- **Complementary and Competing Mechanisms**: The effect of punishment is stronger when combined with reward mechanisms, especially when both intervention types are neither excessive nor too weak. Pure reward alone is often less efficient than pure punishment for stabilizing cooperation, though a balanced combination can yield optimal results (Cong et al., 2016; Zhuang et al., 2012). Excessive punishment, or its application in conjunction with contradictory reward structures, can undermine efficiency (Shen et al., 2022).

- **Design Features—Player Count, Rounds, Communication, Visibility**:
    - **Player Count**: Larger groups generally make punishment harder to coordinate and more costly, reducing effectiveness unless institutional mechanisms address second-order problems (Sigmund et al., 2011).
    - **Num Rounds**: Repeated interactions allow for reputation and sustained punishment to operate more efficiently (Kol'veková et al., 2021).
    - **Communication (chat)**: Not systematically manipulated across studies focused on payoff; effect on efficiency often not directly measured.
    - **Visibility (show_n_rounds, show_other_summaries, show_punishment_id)**: Some studies demonstrate that increased observation and visibility of behavior or punishment can facilitate higher efficiency via norm activation even when direct punishment rates are low (Wang et al., 2020).

- **Special Cases Where Punishment Can Lower Efficiency**: In some settings, especially with **cheap antisocial punishment**, **high punishment costs**, or uncoordinated application (e.g., everyone can punish but redundancy dilutes effect), punishment may fail to increase or can even reduce efficiency relative to the no-punishment baseline (Pi et al., 2022; Wang et al., 2020; Quan et al., 2018; Isakov & Rand, 2012; Quan et al., 2019).

- **Threshold and Nonlinear Effects**: In threshold public goods games and collective-risk dilemmas, punishment is often most effective for intermediate parameter values (risk, resource levels); too strong or too weak punishment (or too high or too low resource abundance) can reduce the efficiency gains (Gao & Liang, 2020; Hua & Liu, 2023; Sun et al., 2024).

## Empirical vs. Theoretical Patterns

- **Empirical Studies**: Robustly support punishment-enabled efficiency gains in small-to-moderate group PGGs (Wang et al., 2020; Pi et al., 2022; Liao et al., 2021*retracted*), though with exceptions when punishment is weak or automatic.
- **Theoretical/Simulation Studies**: Provide a detailed mapping of when, how, and under what moderators punishment increases efficiency, often deriving threshold conditions; but real-world applicability may be limited by assumptions (infinite populations, perfect rationality, evolutionary updating).

---

# 5) Prediction Guidance

**For predicting average efficiency in a punishment-enabled treatment given game design and control efficiency:**

- **Directionality**: In most standard linear PGGs, **enabling peer or institutional punishment will increase average efficiency** over the control game, especially when control efficiency is low (defection-dominated) and design parameters are in the typical PGG range.

- **Magnitude and Moderators**:
    - **Low punishment cost and high effectiveness** (punishment_impact/cost ratio) yield **large efficiency gains** (Wu et al., 2014; Zhuang et al., 2012).
    - **Spatial/networked settings** amplify punishment's effectiveness; well-mixed or random-matching settings require stronger institutional backing (Noailly et al., 2009; Cui et al., 2022).
    - **Network structure of punishment**: More potential punishers (complete network) can dilute impact and lower efficiency ("bystander effect"); less redundant, more targeted punishment (e.g., circle or pairwise networks) achieve higher efficiency (Pi et al., 2022).
    - **MPCR**: Lower MPCRs (lower marginal return to cooperation) gain most in efficiency when punishment is enabled; as MPCR rises, baseline efficiency is higher and punishment's marginal impact lessens (Wu et al., 2014; Sui et al., 2017).
    - **Institutional mechanisms and funding**: Tax-funded punishment institutions outperform voluntary enforcement by preventing second-order free-rider problems, further raising group efficiency (Yang & Yang, 2024; Yao & Chen, 2014).
    - **Reward**: Presence of reward alongside punishment may further increase efficiency, but pure reward is often less effective and can be suboptimal compared to a balanced punishment-reward regime (Cong et al., 2016).

- **Key Exceptions**: Weak, automatic, or non-salient punishment tends not to increase efficiency (Yang et al., 2020); excessive punishment cost or antisocial application can neutralize gains or decrease efficiency (Quan et al., 2018; Wang et al., 2020; Prietula & Conway, 2009).

- **Cautions**: The mapping from contribution rate increase to efficiency gain is nontrivial—if punishment costs are high relative to susceptibility of defectors and do not generate a sufficient shift to cooperation, efficiency can plateau or drop.

---

# 6) Design Dimensions Highlighted Across Papers

### Strong/DIRECT EVIDENCE:
- **player_count**: Widely manipulated; many theoretical and some empirical studies explore group size effects on punishment impact (Sui et al., 2017; Sigmund et al., 2011; Kol'veková et al., 2021).
- **num_rounds**: Common dimension in evolutionary simulations and experiments; longer games facilitate norm stabilization (Kol'veková et al., 2021).
- **mpcr**: Universally recognized as critical; most theoretical papers model or sweep over MPCR/return parameters (Wu et al., 2014; Wang et al., 2010; Sun et al., 2025).
- **punishment_cost & punishment_tech**: Central variables—hundreds of papers examine effects of changing cost and mode/effectiveness of punishment.
- **all_or_nothing**: Addressed in both threshold and discrete/continuous-contribution versions of the PGG; some studies report differences (Kol'veková et al., 2021).
- **reward_exists**: Several models include the option for reward and examine interaction with punishment (Cong et al., 2016; Zhuang et al., 2012; Sun et al., 2024).

### Moderate/INDIRECT EVIDENCE:
- **chat**: Rarely manipulated in payoff-focused studies, but present in some lab experiments; effect on efficiency not always isolated or quantified.
- **default_contrib**: Framing effects, such as opt-in versus opt-out contribution, are discussed in some laboratory contexts but not widely modeled for efficiency.
- **show_other_summaries, show_n_rounds, show_punishment_id**: Sometimes manipulated experimentally; more often discussed in terms of feedback and observation necessary for norm maintenance and enforcement salience.
- **reward_cost, reward_tech**: Explored less frequently than punishment parameters; discussed mainly in relation to their interaction with punishment mechanisms.

### Sparse/MISSING:
- **Network features of punishment (who can punish whom)**: Directly modeled in a subset of studies (Pi et al., 2022; Cui et al., 2022), but not always explicitly parameterized as a design dimension in experiments or for prediction.
- **Contextual variables (e.g., cultural background, real-world group):** Only rarely reported or controlled for.

---

# 7) Important Limitations

- **Empirical Generalizability**: The proportion of empirical (especially large-scale or field) experiments is small compared to theoretical and simulation work. Many predictions about punishment effects on efficiency are based on model outcomes rather than observed human behavior.

- **Outcome Measurement Gaps**: Only a subset of the literature **directly measures efficiency or payoff-based outcomes**; reliance on behavioral proxies (contribution/cooperation rates) is common. These proxies **do not always map cleanly** to efficiency, especially when punishment is costly or antisocial punishment is present.

- **Parameter Range and Specification**: Many theoretical results depend on idealized parameter regimes (infinite populations, very large/few rounds, perfect discrimination, etc.), which may not reflect typical lab experiments or practical settings.

- **Design Coverage**: Some design dimensions relevant for prediction—such as **chat, default contribution, feedback/visibility, and identity salience**—are infrequently isolated and systematically varied in studies focusing on efficiency.

- **Mechanism Interactions**: Studies sometimes confound **punishment/reward** with other design changes (e.g., changing both punishment and communication), complicating attribution of efficiency changes to punishment alone.

- **Heterogeneity in Game Structure**: Results for **standard linear PGGs** are often generalized to threshold, spatial, or institutionally administered games; care is needed when mapping findings across variants.

- **Ambiguity in Negative/Null Effects**: While the aggregate trend is that punishment increases efficiency, **contexts exist where efficiency does not improve or even decreases** with punishment (e.g., when punishment is too costly, antisocial, or redundant), and these results are not always harmonized or quantitatively compared.

- **Limited Multi-dimensional Interactions**: Interactions between multiple game design variables (e.g., simultaneous changes in group size, punishment, and reward) are underexplored in terms of their joint impact on efficiency.

---

**In summary**: The literature robustly supports the expectation that enabling peer or institutional punishment increases efficiency in public goods games under most standard experimental and model conditions, with numerous moderators (cost, effectiveness, structure, MPCR, group size, and institutional versus peer enforcement) well characterized. However, quantitative prediction accuracy is reduced by incomplete empirical mapping, reliance on behavioral rather than payoff outcomes, and less systematic variation of all potentially relevant design dimensions. Prediction models should account for these limitations and be especially cautious in settings with high punishment cost, antisocial punishment, small groups with ambiguous network structure, or when using behavioral proxies for efficiency.
