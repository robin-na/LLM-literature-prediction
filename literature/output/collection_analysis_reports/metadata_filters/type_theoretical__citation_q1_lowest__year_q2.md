# 1) Evidence Base

The literature set is broad, consisting almost entirely of theory and simulation/modeling papers rather than empirical or lab experiments. Of the 52 papers, most present formal models, simulations, or theoretical analyses; there are virtually no new empirical or experimental findings reported. The set draws widely from adjacent domains—including the repeated Prisoner's Dilemma, trust games, resource sharing, and institutional economics—as well as from exact and close variants of the Public Goods Game (PGG). Within this broad theoretical landscape, only a modest proportion of papers study "efficiency" or directly related payoff outcomes; most focus on cooperation rates or the behavioral dynamics underlying cooperation.

# 2) Task Relevance

## PGG or Variant
- **Relevance:** The collection contains a core of papers with *exact* or *close* relevance to the PGG (especially for theory), but a sizable fraction (about half) are only *adjacent*, modeling games like spatial PDs or trust games. True empirical PGG studies are missing.

## Punishment or Sanctions
- **Relevance:** Most papers are *exact* or *close* for punishment or sanction mechanisms, often focusing on peer punishment or analogous social sanctions. Some, however, discuss only exclusion, reputation, or internalized costs (emotions or social pressure), which are labeled *adjacent*.

## Efficiency or Related Payoff Outcome
- **Relevance:** Fewer papers are *exact* for efficiency or group payoff; many discuss only cooperation rates, population compositions, or norm compliance—labeled *adjacent* or *weak*. A subset offers explicit efficiency measures (e.g., average payoff or surplus), but most do not.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes:** Some papers report or model group efficiency, welfare, average payoff, surplus, or maximum sustainable yield (e.g., Wu et al., 2014; Olcina & Calabuig, 2015; Asgharpourmasouleh et al., 2017). These outcomes are relatively rare, and even when used, often arise from theoretical models rather than empirical data.
- **Non-Payoff Behavioral Outcomes:** Most prevalent are measures such as cooperation rate, contribution rate, frequency of strategy types (e.g., punisher/defector), norm compliance, population structures, or the success of certain roles or strategies (see Ogaki & Tanaka, 2017; Teraji, 2016). Many studies use these as proxies for efficiency but do not analyze payoff dynamics.
- **Distinction:** The literature's main strength is in unpacking mechanisms and the behavioral preconditions for efficient outcomes, not in providing direct quantitative predictions of efficiency changes due to punishment.

# 4) Main Findings Relevant To Prediction

## Empirical Conclusions
- *Efficiency Effect is Conditional*: Enabling punishment in PGGs or close variants can dramatically increase efficiency—especially where baseline cooperation is low and punishment is cheap/effective (Wu et al., 2014; Olcina & Calabuig, 2015; Asgharpourmasouleh et al., 2017).
- *Costly Punishment Caveat*: Where punishment is expensive and not well-coordinated, it often fails to increase efficiency and may reduce group payoff despite higher cooperation (Kroupa, 2014; Ezeigbo, 2017; Antoci & Zarri, 2015).
- *Game Structure Moderators*: Effects are positively moderated by design features like longer time horizons, communication abilities, reputation, endogenous group formation, and lower MPCR (Kroupa, 2014). Spatial structure, information precision, and status hierarchies also matter.
- *Heterogeneity of Sanction Rules*: Subtle changes in who punishes whom, or in the possibility of rewarding, can yield sharply different efficiency outcomes—severe or misdirected punishment, second-order free riding, and antisocial punishment can all reduce efficiency (Antoci & Zarri, 2015).
- *Network and Information Effects*: Limited network knowledge (imprecise information about others) makes punishment more effective at sustaining high efficiency (Larson, 2016). Precise knowledge can reduce the deterrence effect of punishment.
- *Evolutionary/Dynamic Considerations*: Punishment's short-term efficiency gains may undermine intrinsic cooperation over the long run (Povey, 2014), making dynamic welfare effects ambiguous.

## Mechanism and Theory Content
- Evidence is robust that punishment can raise cooperation and, under the right conditions, efficiency, but multiple equilibrium and path dependence are central—punishment can also lock groups into low-efficiency states if misapplied or if social/institutional mechanisms are weak.
- Presence of “second-order free riders” (cooperators who don't punish) is a key challenge; mechanisms to punish them (or peer-pressure punishers) can be required for robust high efficiency (Antoci & Zarri, 2015; Olcina & Calabuig, 2015).
- Reward or reputation can substitute for or interact with punishment, affecting efficiency outcomes in sometimes non-intuitive ways (Kroupa, 2014; Antoci & Zarri, 2015).
- Information/monitoring structure (whether punishment is targeted, anonymous, or public) is a crucial moderator of possible efficiency.

# 5) Prediction Guidance

- **Directionality:** The literature collectively points toward **conditional positive effects** of punishment on efficiency in PGG-like environments. The effect is strongest when punishment is cheap, effective, and well-targeted, particularly at low baseline efficiency (i.e., when control efficiency is low).
- **Adjustment for Design Dimensions:** 
  - *Lowering punishment cost* and *increasing punishment effectiveness* should increase predicted efficiency with punishment enabled.
  - *Higher MPCR* generally reduces the marginal effect of enabling punishment, while low MPCR environments see the largest efficiency gain from punishment (Wu et al., 2014; Olcina & Calabuig, 2015).
  - *Enabling chat/communication* and *reputation* mechanisms, or increasing *num_rounds*, increases the likelihood that punishment is efficient (Kroupa, 2014).
  - If reward is present, the effect of punishment is complicated, with potential attenuation or even reversal due to interaction effects (Antoci & Zarri, 2015).
  - Poor monitoring/attribution, high player count, or structural anonymity reduce the payoff-benefit from punishment (Laclau & Tomala, 2017).
- **Initial Efficiency:** If the control (no-punishment) efficiency is already high, the incremental effect of punishment may be small or even negative if punishment incurs unnecessary costs.
- **Fragility and Multiple Equilibria:** The improvement in efficiency due to punishment is highly dependent on social and institutional context. There are parameter regions where enabling punishment can entrench inefficiency, especially with antisocial punishment, second-order free riders, or high costs.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**
- `player_count`: Frequently discussed; effects on cooperation stability, efficiency, network clustering, and the effectiveness of punishment are all sensitive to group size.
- `num_rounds`: Directly discussed in evolutionary/repeated game settings; longer games tend to support more efficient use of punishment.
- `all_or_nothing`: Commonly featured in adjacent PD models; influences the structure of available strategies.
- `mpcr`: Explicitly analyzed (Wu et al., 2014; Olcina & Calabuig, 2015); lower MPCR makes punishment more critical for efficiency.
- `punishment_cost`, `punishment_tech`: Central moderators across many papers; lower cost and higher efficacy increase efficiency through punishment.
- `reward_exists`/`reward_cost`/`reward_tech`: Discussed in some detail regarding potential substitution/complementarity with punishment.

**Indirectly Informed:**
- `chat`: Appears as communication or reputation; indirect but important moderator of efficiency via punishment use.
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Occasionally contextually discussed (monitoring, observability, and attribution).
- `default_contrib`: Mentioned in framing and behavioral terms, but not as a main moderator of efficiency.

**Only Contextually Discussed / Effectively Missing:**
- Most papers do not address `default_contrib`, `show_n_rounds`, or explicitly how information on rounds or contributions is framed, except in passing.
- Few papers model `chat` explicitly as a treatment variable.
- Details such as `show_punishment_id` (anonymity of sanctions), `show_other_summaries`, or round-by-round feedback are largely implicit or missing.
- Empirical mapping of dimension effects is missing—very few papers offer parameterized, empirical, or quantitative guidance linking design inputs to efficiency changes.

# 7) Important Limitations

- **Lack of Empirical Data:** The entire literature set is theoretical or simulation-based. This means quantitative prediction of efficiency changes from empirical game designs is highly uncertain.
- **Payoff/Outcome Mapping:** Few models provide explicit, operationalizable mappings from design dimensions to efficiency delta when enabling punishment. Many focus on theoretical mechanisms or equilibrium properties rather than effective, predictive relationships.
- **Non-PGG Studies as Basis:** Almost half the papers are only adjacent to PGGs, often modeling the repeated PD or dyadic games. Careful transfer of mechanisms is needed, and direct efficiency predictions should be made with caution.
- **Overemphasis on Behavioral Outcomes:** Many "efficiency" arguments are inferred from cooperation rates/norm compliance, not directly calculated group payoffs. The two can diverge, especially when punishment is costly.
- **Multiple Equilibria and Context Dependence:** Most papers demonstrate that both high and low efficiency are possible depending on initial conditions, coordination, or the structure of norms and monitoring; there is no single, universal outcome even for the same basic game design.
- **Missing Design Dimensions:** Some features that are likely to be important in real experimental or organizational settings—such as simultaneous reward and punishment, framing of default actions, or the details of information provision—are not systematically modeled.
- **Long-Run vs. Short-Run Effects:** Dynamic/long-run efficiency may differ from static/short-run outcomes, particularly where intrinsic motivation or group selection is important (Povey, 2014).
- **Ambiguity in Edge Cases:** In lab-like settings (short, anonymous, high punishment cost, no communication), several papers argue punishment can lower efficiency.

---

**In summary:**  
This literature set provides strong theoretical support that adding peer punishment to a PGG-like environment can, under appropriate design parameters (cheap and effective punishment, good monitoring, communication, moderate player count, and low baseline cooperation), substantially increase group efficiency. However, the effect is highly conditional: poorly designed punishment, high costs, absence of communication or reputation, or adverse game structure can make punishment ineffective or even counterproductive for efficiency. The absence of empirical or quantitative estimates for treatment effects is a significant limitation, and many relevant design features for prediction remain only weakly or contextually addressed.
