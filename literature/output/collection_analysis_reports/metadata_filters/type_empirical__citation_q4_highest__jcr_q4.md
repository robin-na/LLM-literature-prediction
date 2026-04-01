# 1) Evidence Base

This paper set consists of three empirical studies, all based on laboratory experiments:

- **Breadth**: The set is narrow with respect to the prediction task, as only one paper (Carpenter et al., 2012) directly tests public goods games (PGGs) with punishment and efficiency measures. The other two papers (Manesi et al., 2016; Bourrat et al., 2011) use experiments not centered on economic games—focusing instead on the effects of surveillance cues on prosocial behavior or moral condemnation.
- **Empirical Focus**: All studies are empirical. There are no purely theoretical or simulation-based papers.
- **Outcome Coverage**: Of the three, only Carpenter et al. (2012) provides direct evidence for the prediction task, by experimentally varying network structure in PGGs with punishment and measuring group efficiency/payoff. The others contribute only contextually or adjacently through behavioral outcomes and do not report efficiency or payoff measures.

# 2) Task Relevance

Each paper’s relevance to the three core dimensions is as follows:

- **pgg_or_variant**:
    - *Exact*: Carpenter et al. (2012) employs true public goods games.
    - *Adjacent/None*: Manesi et al. (2016) uses helping tasks (adjacent, not economic games) and Bourrat et al. (2011) uses moral judgment vignettes (none).
- **punishment_or_sanctions**:
    - *Exact*: Carpenter et al. (2012) includes explicitly costly peer punishment.
    - *Weak/Adjacent*: Manesi et al. (2016) involves no punishment (weak), and Bourrat et al. (2011) looks at attitudinal condemnation, not actual sanctions (adjacent).
- **efficiency_or_related_payoff_outcome**:
    - *Exact*: Carpenter et al. (2012) directly reports efficiency and group payoff effects.
    - *Weak/None*: The other two only report non-payoff behavioral outcomes (helping or moral judgment).

Thus, only one paper is directly relevant across all three core dimensions, while the others are at best weakly or adjacently informative for behavioral context, not for payoff or efficiency outcomes.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes**:
    - *Directly measured only by Carpenter et al. (2012)*: This includes group efficiency (total group payoff relative to maximum possible payoff under full cooperation) in experimental PGGs with and without punishment, under varied network architectures.
- **Non-payoff behavioral outcomes**:
    - *Manesi et al. (2016)*: Measures prosocial effort (helping behavior) in response to gaze cues (“eyes”), but not in game or payoff contexts.
    - *Bourrat et al. (2011)*: Measures attitudinal condemnation of moral violations in the presence of surveillance cues, with no link to economic game behavior, sanctions, or payoffs.

The distinction is clear: only one paper directly informs the target efficiency outcome, while the other two deal exclusively with non-payoff behavioral or attitudinal measures.

# 4) Main Findings Relevant To Prediction

Synthesizing the set:

- **Network Effects on Punishment’s Efficiency Impact**:
    - **Carpenter et al. (2012)** is the critical source. It finds that the impact of enabling peer punishment on group efficiency is highly sensitive to network structure:
        - In *complete or well-connected* networks, punishment raises contributions and may improve efficiency if punishment use is modest.
        - In *directed or disconnected* networks, punishment is applied more, costs are higher, and efficiency often decreases—even when contributions increase—because punishment expenditures outweigh cooperation gains.
        - The marginal effect of increasing network connectedness is non-linear: sparse to moderately connected networks benefit most; beyond that, efficiency can decline due to over-punishment.
    - The study holds other key parameters constant (MPCR, punishment cost), thus isolating network architecture as a moderator of punishment’s effect on efficiency.
- **Other Papers**:
    - *Manesi et al. (2016)* and *Bourrat et al. (2011)* show that cues of observation or surveillance may increase prosocial sentiments or condemnation. However, as they lack group interaction, punishment dynamics, and payoff accounting, they do not inform the quantitative prediction of treatment efficiency in PGG-like environments.

# 5) Prediction Guidance

- **Direct Guidance**:
    - **Network architecture is decisive**: When predicting how enabling peer punishment will shift efficiency, *controlling for the network of monitoring and punishment is crucial*. In fully connected or well-connected networks, punishment is likely to enhance or sustain high efficiency, but only if punishment costs remain low through norm adherence. In sparsely connected, directed, or fragmented networks, enabling punishment can decrease efficiency due to overuse and high expenditures.
    - **Control efficiency alone is insufficient**: Even if the baseline (control) game is efficient, enabling punishment can *reduce* efficiency if the network structure fosters excessive punishment.
    - **Other parameters held constant in experiments**: The direct evidence does not cover variation in MPCR, punishment cost, or player count as those were fixed in Carpenter et al. (2012).
- **Indirect Guidance (from surveillance cue studies)**:
    - Behavioral mechanisms like increased reputational concerns might boost prosocial behaviors, but these effects are only weakly relevant, as they are not linked to actual payoffs or intra-group sanctions in the prediction context.

# 6) Design Dimensions Highlighted Across Papers

Of the 14 design dimensions:

- **Directly Informed**:
    - *player_count, num_rounds, chat, all_or_nothing, mpcr, punishment_cost*: All systematically manipulated or fixed in Carpenter et al. (2012).
    - *punishment_tech*: The paper focuses on network structure, the “who can punish whom” architecture, which is a critical aspect but not always captured in canonical dimension lists.
- **Indirectly or Contextually Informed**:
    - *show_n_rounds*: Mentioned in Manesi et al. (2016), but not in a PGG or payoff context.
    - *chat*: Included as a dimension but not uniquely analyzed for its influence on efficiency change under punishment.
- **Missing or Uninformed**:
    - *default_contrib, reward_exists, reward_cost, reward_tech, show_other_summaries, show_punishment_id*: Not manipulated or analyzed in any of the papers.
    - The effect of *reward mechanisms* (as opposed to punishment) is entirely missing.
    - *ShowPunishmentId* and parameters linked to information visibility or identity are missing.
    - *ShowOtherSummaries* (visibility of peers’ outcomes) discussed only as fixed background or context, not as treatment variables.

# 7) Important Limitations

- **Narrow Empirical Scope**: Only one paper (Carpenter et al., 2012) directly tests PGGs with punishment and efficiency outcomes, and only in four-player, 15-round games with fixed MPCR and punishment cost.
- **Network-centric evidence**: The findings’ generalizability may be limited, as other major game design dimensions (e.g., varying MPCR, different group sizes, presence of rewards, effects of chat or information visibility) are not systematically varied or tested for moderation of punishment’s efficiency impact.
- **Surveillance cue studies lack PGG context**: The other two studies are restricted to individual helping or moral evaluation tasks, so their results are not valid for predicting payoff changes in PGGs or mechanism settings with peer punishment.
- **Partial dimension coverage**: Several candidate predictors for treatment efficiency (e.g., reward systems, default contribution framing, information or identity visibility) are missing or discussed only peripherally.
- **Mixed effects of punishment**: The “efficiency gain” from enabling punishment is not uniform—even when punishment improves cooperation, overall payoffs may decline if punishment is applied heavily and inefficiently.
- **No direct comparison on some dimensions**: Dimensions such as default contribution mechanism, or information about rounds and other player actions, are not independently tested for their effect on punishment’s efficiency impact.
- **No evidence for scaling up**: The effect of increasing player count or rounds is not addressed for punishment’s efficiency effect; these are held constant in Carpenter et al. (2012).

**In summary**, the literature provides strong evidence for the critical importance of network architecture in moderating punishment’s effect on efficiency in PGGs, with other game design dimensions (besides network structure) largely uninformed or missing from the empirical base. Most other dimensions relevant to prediction are not covered, and the generalizability beyond the tested parameterizations is unclear. Direct prediction of treatment efficiency from control efficiency and game design features is thus well-supported only as far as network structure is directly comparable to those empirically tested in this paper set.
