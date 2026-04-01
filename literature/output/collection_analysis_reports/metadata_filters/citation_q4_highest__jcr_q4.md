# 1) Evidence Base

The paper set consists of a mix of empirical laboratory experiments (2 papers) and theoretical modeling or review articles (5 papers). Of the seven papers, two are directly empirical and focus on laboratory settings: one manipulates punishment in public goods games (Carpenter et al., 2012), and the other investigates surveillance cues but not PGGs or efficiency (Manesi et al., 2016). The remainder are theoretical or review-based, addressing the evolution of cooperation and punishment (Bowles & Gintis, 2004; Okada, 2020; KRAINES & KRAINES, 1993; Hagen & Hammerstein, 2006; Bourrat et al., 2011). 

For the downstream prediction task—predicting efficiency in public goods games under alternative punishment conditions—the evidence base is **narrow**, with only one experimental study providing direct empirical findings relevant to the efficiency impact of punishment in PGGs (Carpenter et al., 2012). Theoretical papers, especially Bowles & Gintis (2004), supply robust modeling evidence relevant to efficiency, but empirical generalizability is less certain. Several other papers are only contextually or adjacently related and do not involve payoff or efficiency measurements.

# 2) Task Relevance

**pgg_or_variant**  
- **exact**: Carpenter et al. (2012) and Bowles & Gintis (2004) (theory) directly address PGGs or canonical variants.
- **close/adjacent/weak**: Okada (2020) and KRAINES & KRAINES (1993) focus on indirect reciprocity or dyadic dilemmas (IPD), not multi-party PGGs.
- **none**: Bourrat et al. (2011) does not address PGGs or economic games at all.

**punishment_or_sanctions**  
- **exact**: Carpenter et al. (2012), Bowles & Gintis (2004) explicitly study costly peer punishment as a game mechanism.
- **close/adjacent**: Okada (2020) and KRAINES & KRAINES (1993) discuss punishment in the context of indirect reciprocity and adaptive strategy, not explicit peer sanctioning in groups.
- **weak/none**: Manesi et al. (2016), Hagen & Hammerstein (2006), Bourrat et al. (2011) only touch weakly or not at all on punishment.

**efficiency_or_related_payoff_outcome**  
- **exact**: Carpenter et al. (2012) and Bowles & Gintis (2004) discuss efficiency, payoffs, or welfare as central outcomes.
- **close/adjacent**: KRAINES & KRAINES (1993) report efficiency/payoff but not in group games or PGGs.
- **weak/none**: Okada (2020), Manesi et al. (2016), Hagen & Hammerstein (2006), Bourrat et al. (2011) focus on behavior, norm compliance, or reputation rather than group payoff or efficiency.

The **task-relevant evidence** is thus concentrated in two papers, with the rest providing only contextual or mechanism-level insight.

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes:**  
- **Efficiency/group payoff/total earnings**: Directly measured in Carpenter et al. (2012; empirical PGG with/without punishment); theoretically modeled in Bowles & Gintis (2004; evolutionary modeling), and in KRAINES & KRAINES (1993; dyadic payoffs in iterated games).
- **Not Measured**: Five other papers do not measure or model group-level efficiency/payoff as a primary outcome.

**Non-Payoff Behavioral Outcomes:**  
- **Contribution, cooperation, norm compliance, moral condemnation, or prosocial behavior**: These outcomes feature in other papers (e.g., Okada, 2020; Manesi et al., 2016; Bourrat et al., 2011) but are not synonymous with efficiency. Reputation cues and surveillance effects are measured in terms of willingness to comply, rate tasks, or help others rather than group payoffs.

**Distinctions:**  
- Only Carpenter et al. (2012) provides experimental data linking punishment to group efficiency in PGGs.
- Most other findings concern cooperation rates, norm stability, or perception—not efficiency.

# 4) Main Findings Relevant To Prediction

- **Punishment Does Not Uniformly Increase Efficiency:** Carpenter et al. (2012) provide clear experimental evidence that the efficiency impact of adding peer punishment to a PGG strongly depends on the network structure—that is, "who can punish whom." In complete and some well-connected networks, punishment can raise contributions with *relatively low punishment expenditures*, boosting efficiency. In less connected or directed networks, despite increased contributions, *punishment costs outweigh gains*, sometimes reducing efficiency below the control condition.
    - The effect is thus moderated by network design, specifically the monitoring/punishment architecture, with *non-monotonic* returns from increasing edge density.

- **Theoretical Support for Positive Effect:** Bowles & Gintis (2004) supply theoretical support: when strong reciprocators (willing to incur costs to punish) exist, costly punishment supports high efficiency and group payoffs. This effect is robust across a variety of parameterizations including group size and punishment cost.

- **Payoff Effects Conditional on Game Structure:** Network structure and punishment cost are critical; enabling punishment *does not guarantee* efficiency gains (Carpenter et al., 2012). Theory suggests the presence of some punishment is generally efficiency-enhancing, but empirical evidence shows the implementation (network/punishment technology) is decisive.

- **Non-Payoff Mechanisms:** Other studies (Okada, 2020; Manesi et al., 2016; Bourrat et al., 2011) discuss how punishment and/or observation can stabilize norm compliance or increase prosocial behavior, but *do not link these mechanisms to efficiency or group payoff*.

# 5) Prediction Guidance

This literature set should inform efficiency prediction as follows:

- **If the network architecture is complete or well-connected** (i.e., all players can punish all others), and punishment costs are moderate, expect **efficiency to increase relative to control**. Use control efficiency as a baseline, but **adjust upward** if group contribution is likely to increase *without excessive punishment expenditure* (Carpenter et al., 2012; Bowles & Gintis, 2004).

- **If the punishment network is sparse, directed, or disconnected**, prediction is more uncertain. Empirically, punishment expenditures can become so frequent or severe that **efficiency falls below control levels** (Carpenter et al., 2012). In these cases, use control efficiency as a ceiling; predicted treatment efficiency should be **adjusted downward or left unchanged** unless there is strong reason to expect low punishment expenditure.

- **Game-theoretic models** (Bowles & Gintis, 2004) suggest robustness across player_count, num_rounds, mpcr, and punishment_cost, but these findings are theoretical, not always empirically validated, and may presume full network connectivity and/or idealized learning/mixing.

- **Indirect or contextual factors** like framing, observation cues, or implicit norms can moderate punishment behavior (Hagen & Hammerstein, 2006), but are *not systematically modeled in prediction dimensions* and cannot be directly included in quantitative prediction.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**
- player_count (Carpenter et al., 2012; Bowles & Gintis, 2004)
- num_rounds (Carpenter et al., 2012; Bowles & Gintis, 2004)
- mpcr (Carpenter et al., 2012; Bowles & Gintis, 2004)
- punishment_cost (Carpenter et al., 2012; Bowles & Gintis, 2004)
- punishment_tech (network/monitoring structure in Carpenter et al., 2012; adjacent in Okada, 2020)

**Indirectly Informed or Contextually Discussed:**
- chat (Carpenter et al., 2012; Manesi et al., 2016; not explored in-depth)
- all_or_nothing (Carpenter et al., 2012; Okada, 2020)
- show_n_rounds (Manesi et al., 2016; peripheral)
- default_contrib (adjacent via framing discussion)
- show_other_summaries, show_punishment_id (not systematically manipulated but related to information/monitoring)

**Effectively Missing or Lacking Evidence:**
- reward_exists, reward_cost, reward_tech, reward_magnitude (not present in included PGGs; discussed in Okada, 2020 only as part of norm mechanism in indirect reciprocity, not efficiency)
- show_punishment_id (not studied directly as a design lever for efficiency)
- show_other_summaries (not systematically manipulated)
- Some aspects of chat, framing, and implicit observation cues may contextually moderate outcomes but lack controlled evaluation in PGG-punishment contexts with measured efficiency.

# 7) Important Limitations

- **Empirical Evidence is Largely Limited to Network Structure:** Only one experimental paper (Carpenter et al., 2012) systematically manipulates both punishment and measured efficiency in public goods games using different network structures. Generalizability to games varying other dimensions (e.g., punishment magnitude, reward, information features) is untested.

- **Most Papers Lack Direct Payoff/Efficiency Measures:** Several papers address norm compliance, behavior, or perception, not efficiency or group payoff, reducing their utility for quantitative efficiency prediction.

- **Reward Mechanisms and Combined Treatments Are Missing:** No experimental or theoretical studies in this set jointly manipulate or compare reward/cooperation, making prediction in settings with reward or combined incentives less informed.

- **Indirect Reciprocity and Framing Effects Remain Theoretical:** While the literature addresses indirect reciprocity, surveillance, and social framing, these mechanisms are not integrated into PGG prediction models nor tested with efficiency as outcome.

- **Theory May Overstate Generalizability:** Strong reciprocity models (Bowles & Gintis, 2004) suggest robust efficiency gains from punishment but may over-generalize from special cases or assume conditions (e.g., homogeneous mixing, ideal adaptation) that do not hold in practice.

- **Missing Dimensions:** Several key prediction variables (reward_*, show_*, punishment_magnitude) are not covered, and information is absent or sparse on how these moderate punishment effects on efficiency.

- **Heterogeneity and Boundary Conditions Are Unclear:** There is ambiguity regarding how findings scale to larger groups, different MPCRs, varying punishment costs, or other complex design elements.

**In summary:** The available literature provides robust evidence that punishment can increase efficiency in PGGs, but only under specific conditions (notably complete/well-connected networks and moderate punishment costs). The generalizability to other design dimensions is not established, and most papers in the set do not directly address efficiency or payoff outcomes. This significantly constrains the confidence and specificity of downstream efficiency predictions outside the best-evidenced settings.
