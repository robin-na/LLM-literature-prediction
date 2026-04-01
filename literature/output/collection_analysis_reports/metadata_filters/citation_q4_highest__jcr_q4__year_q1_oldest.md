# 1) Evidence Base

This paper set consists of a mix of three theoretical papers and two empirical/experimental papers. Of the five, only two are direct lab experiments measuring outcomes in actual economic game settings; the remainder are theoretical or focus on adjacent mechanisms. The empirical papers (Carpenter et al., 2012; Bourrat et al., 2011) differ in their degree of relevance, with only one directly investigating public goods games with punishment and efficiency as outcomes. Theoretically, Bowles & Gintis (2004) directly examine PGG-like environments with punishment, whereas the other theory papers focus on broader or adjacent issues (learning in dyadic games—KRAINES & KRAINES, 1993—and the role of framing, cues, and interpretation—Hagen & Hammerstein, 2006).

Overall, this set is relatively narrow in direct empirical coverage of public goods games with enabled punishment and measured efficiency; most of the directly relevant findings rest on one empirical and one theory paper.

# 2) Task Relevance

**pgg_or_variant**
- *exact*: Carpenter et al. (2012) (empirical), Bowles & Gintis (2004) (theory)
- *close*: Bowles & Gintis (2004) (theory; covers PGG-like environments), KRAINES & KRAINES (1993) (iterated Prisoner's Dilemma—but not group settings)
- *adjacent or weaker*: Hagen & Hammerstein (2006), Bourrat et al. (2011)

**punishment_or_sanctions**
- *exact*: Carpenter et al. (2012), Bowles & Gintis (2004)
- *adjacent*: KRAINES & KRAINES (1993) (learning from payoff changes, not explicit peer punishment), Hagen & Hammerstein (2006), Bourrat et al. (2011)

**efficiency_or_related_payoff_outcome**
- *exact*: Carpenter et al. (2012), Bowles & Gintis (2004), KRAINES & KRAINES (1993) (but only in dyadic, not group settings)
- *adjacent*: Hagen & Hammerstein (2006) (discusses behavioral/normative outcomes, not payoff), Bourrat et al. (2011) (no payoff measured)

The direct task relevance is strongest for Carpenter et al. (2012) and Bowles & Gintis (2004); both address all three prediction-relevant dimensions at least at the "close" or "exact" level. The rest provide only peripheral or mechanism-level commentary and do not directly address efficiency in PGGs with punishment.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes (Efficiency, Group Payoff, Welfare, Surplus)**
    - *Directly measured*: Carpenter et al. (2012) (experimental); Bowles & Gintis (2004) (model outputs)
    - *Indirectly informed or only in adjacent domains*: KRAINES & KRAINES (1993) (efficiency and average payoff in dyadic games, not group PGG)
    - *Absent*: Bourrat et al. (2011); Hagen & Hammerstein (2006)
- **Non-Payoff Behavioral Outcomes (Contribution rates, norm compliance, condemnation)**
    - *Measured and primary*: Bourrat et al. (2011) (moral condemnation)
    - *Discussions of behavioral mechanisms*: Hagen & Hammerstein (2006), KRAINES & KRAINES (1993)
    - *Also present as secondary outcomes in*: Carpenter et al. (2012) (contributions, punishment frequency), Bowles & Gintis (2004) (frequency of cooperation)

Where efficiency or group payoff is directly measured, it is usually clearly distinguished from mere behavior or attitudes.

# 4) Main Findings Relevant To Prediction

Synthesizing across the set, the key findings for prediction about efficiency when enabling peer punishment are:

- **Punishment’s Impact on Efficiency Is Moderated by Network Structure:** In lab experiments by Carpenter et al. (2012), the effect of enabling punishment is strongly contingent on the architecture of the punishment network. Complete and well-connected networks see increased contributions and (often) increased efficiency, as the punishment deters free-riding with relatively low punishment expenditures. In more fragmented (directed/disconnected) networks, punishment occurs more frequently and severely, often reducing net efficiency below the control, due to high punishment costs eating into total group payoffs. Thus, punishment's efficiency effect is *not uniformly positive*; network connectivity alters the outcome dramatically (Carpenter et al., 2012).

- **Theory Predicts Generally Positive Effects with Costly Punishment:** Bowles & Gintis (2004) model populations with a fraction of strong reciprocators (willing to incur cost to punish defectors) and consistently find that costly punishment allows cooperation and high efficiency to be stabilized, across broad parameter ranges. Without punishment, selfish behavior dominates and efficiency collapses. The positive effect is robust to group size, punishment cost, and other features in the models, provided some mechanism for enforcement exists (Bowles & Gintis, 2004).

- **Adaptive Strategies in Dyads Achieve High Efficiency, but are Not Directly Generalizable:** KRAINES & KRAINES (1993) show how learning strategies based on recent payoffs (“Pavlovian” learning) can achieve high efficiency in noisy dyadic games, suggesting robustness of reciprocity-like mechanisms. However, this is only adjacent, as adaptation is endogenous and not tied to institutionalized peer punishment, nor group interaction.

- **Contextual/Framing Factors May Moderate Effects:** Hagen & Hammerstein (2006) point out that behavior in experimental punishment games is sensitive to framing, implicit context, and cues, cautioning against overgeneralization from experimental results in the absence of these details.

- **Surveillance Cues Can Influence Normative Judgments, Not Payoff:** Bourrat et al. (2011) finds that subtle cues (e.g., images of eyes) shift moral condemnation, but give no evidence on group payoffs or economic efficiency.

# 5) Prediction Guidance

Based on this literature, the following is suggested for predicting the efficiency of a PGG-like game when moving from a no-punishment ("control") to a peer-punishment ("treatment") condition:

- **Network Architecture Is Decisive:** The effectiveness of punishment in raising efficiency depends critically on who can punish whom. In settings with complete or nearly-complete punishment networks, enabling punishment tends to increase or at least sustain high efficiency, provided punishment is not over-used (Carpenter et al., 2012). In sparse or directed networks, punishment may occur often but be too costly, reducing total group efficiency.

- **Baseline Group Efficiency Must Be Contextualized:** Control efficiency prior to enabling punishment is important, but must be interpreted in light of the network structure and cost parameters; punishment may only help when initial cooperation is not already high. High punishment expenditures may even lower efficiency below control.

- **Parameter Robustness in Theory, But Less So in Experiments:** Theory (Bowles & Gintis, 2004) suggests the efficiency benefits of punishment are robust to group size and punishment cost. However, empirical findings (Carpenter et al., 2012) show critical dependence on network architecture rather than just cost/MPCR.

- **Limited Empirical Guidance for Many Prediction Dimensions:** Almost all direct empirical data concern fixed player count (four players), fixed MPCR and punishment cost, and fixed/few network structures. There is little direct experimental evidence in this set for the effects of other design features (e.g., chat, framing, default contribution, reward options, information settings).

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed by Empirical or Theoretical Results:**
- `player_count`: Varies in theory (Bowles & Gintis, 2004); fixed in empirical (Carpenter et al., 2012, but only 4-player games).
- `num_rounds`: Considered as repeated rounds in both empirical and theory papers.
- `mpcr`: Examined in both, but with little variation in the empirical study.
- `punishment_cost`: Held constant in empirical; varied in theory.
- `punishment_tech` (punishment network structure): *Strongly analyzed* in Carpenter et al. (2012); found to be a critical moderator.
- `all_or_nothing`, `chat`: Covered in Carpenter et al. (2012) (but not as focal manipulated variables).
  
**Indirectly Informed or Contextually Discussed:**
- `default_contrib`: Not directly manipulated or reported.
- `reward_exists`, `reward_cost`, `reward_tech`: Not empirically or theoretically examined.
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Only contextually mentioned (Hagen & Hammerstein, 2006), with no direct data.

**Effectively Missing Across Papers:**
- No direct evidence on chat effects, default contribution framing, reward mechanics, exposure of round count, summary displays, or punisher identification.
- No evidence mapping specific parameter ranges to treatment-control efficiency changes except for network structure.

# 7) Important Limitations

- **Strong Evidence for Only a Subset of Design Dimensions:** Only network structure, player count, round repetitions, MPCR, and punishment cost are covered meaningfully. Many other potentially important design features are untested.
- **Most Empirical Results Are Under Narrow Conditions:** The primary empirical study (Carpenter et al., 2012) uses a single player count, MPCR, and punishment cost; results may not generalize across the parameter space.
- **No Empirical Data on Reward-Enabled Games, Chat, or Information Controls:** Reward mechanisms, chat between players, and UI features are outside the evidence base.
- **Potential for Context or Framing Effects:** As underlined by Hagen & Hammerstein (2006), behavioral and efficiency outcomes may be context-dependent in ways not reflected in standard game design dimensions.
- **Theoretical Results May Overstate Generalizability:** Bowles & Gintis (2004) see robust positive effects of punishment in simulation, but real-world or empirical results (Carpenter et al., 2012) show sensitivity to network/punishment structure.
- **No Evidence for Heterogeneity across Groups or Cultures:** Despite theory predicting stability of cooperation in heterogeneous populations (Bowles & Gintis, 2004), the empirical set does not provide cross-population or cross-cultural results.

**In summary**, the core substantive prediction for efficiency change with enabled punishment is well-supported *only* for certain network architectures and cost structures. For other design variations or more granular predictions, the evidence is limited or absent in this paper set.
