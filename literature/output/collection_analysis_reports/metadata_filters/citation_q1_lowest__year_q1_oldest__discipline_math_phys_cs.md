# 1) Evidence Base

This paper set (N=13) is composed entirely of theoretical or simulation-based papers; there are no empirical (lab or field) experimental studies. The set is fairly broad in terms of the types of social dilemma games and mechanisms addressed, spanning classic and spatial public goods games (PGG), prisoner's dilemma (PD), resource and flow allocation games, and adjacent cooperative environments involving reputation or reporting. Nearly all papers present qualitative or formal models, with several offering extensive simulation results; a few synthesize previous theoretical mechanisms. The breadth of topics means the set is not tightly focused on public goods games with peer punishment and measured efficiency, but it includes multiple direct treatments of punishment and payoff outcomes in repeated cooperation settings—albeit typically via theory.

# 2) Task Relevance

#### pgg_or_variant

- **exact:** ~4 papers focus on public goods games (PGG) or mechanisms functionally equivalent to PGG (Liu & Guo, 2010; Zhao et al., 2010; Xiao & Hua, 2012; Sigmund & Hilbe, 2011).
- **close/adjacent:** Most others address repeated resource dilemmas (PD, flow control, or reputation-based systems) structurally adjacent to or close analogs of PGG (Evans & Thomas, 2001; Tao et al., 2011; Castro et al., 1998; Robert et al., 2012).
- **weak/none:** Few directly examine one-shot or static PGGs, and several papers do not involve explicit group provision dilemmas.

#### punishment_or_sanctions

- **exact:** ~6 papers include explicit punishment/sanctioning mechanisms, often as peer punishment (Liu & Guo, 2010; Tao et al., 2011; Evans & Thomas, 2001; Annen, 2011; Castro et al., 1998).
- **close/adjacent:** A number consider punishment-equivalent mechanisms (e.g., reprobation, exclusion, reputation-based refusal, internalized costs; Robert et al., 2012; Billard, 1996), or discuss the effect of moral norms or rewards as functionally similar to punishment.
- **none:** Several studies are purely focused on network structure, spatial patterns, or behavioral rules without any explicit punishment.

#### efficiency_or_related_payoff_outcome

- **exact:** Few papers report efficiency or total group payoff as a primary output (Tao et al., 2011; Evans & Thomas, 2001; Castro et al., 1998; Robert et al., 2012; Annen, 2011).
- **adjacent/close:** Several use average payoff, system utility, “fitness,” or welfare as proxies (Liu & Guo, 2010), or qualitative outcomes about equilibrium efficiency (Jones, 1999), but focus more on conditions or comparative statics rather than reporting numeric efficiency shifts.
- **none:** Multiple papers measure only cooperation/contribution rates, frequencies of strategies, or network state variables (Xiao & Hua, 2012; Sigmund & Hilbe, 2011; Ma et al., 2009).

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:** Several papers explicitly address _efficiency_ (group payoff normalized by maximum possible payoff: e.g., Tao et al., 2011; Annen, 2011; Evans & Thomas, 2001; Castro et al., 1998; Robert et al., 2012). Others use strongly related metrics such as system utility, average payoff, welfare, or fitness (Liu & Guo, 2010).
- **Non-payoff behavioral outcomes:** A substantial proportion primarily report on _cooperation rate_, _contribution frequency_, _strategy dynamics_, or evolution of behaviors (e.g., fraction of cooperators; Xiao & Hua, 2012; Ma et al., 2009; Szilagyi & Somogyi, 2010; Billard, 1996; Sigmund & Hilbe, 2011). These outcomes are important but should not be conflated with efficiency.
- **Mixed/indirect:** Some model the stability or existence of cooperative equilibria, which implies (but does not quantify) efficiency (Jones, 1999; Evans & Thomas, 2001).

# 4) Main Findings Relevant To Prediction

Synthesizing across the most relevant papers:

- **Punishment generally increases efficiency—if not too costly:** Across direct and adjacent settings, enabling punishment typically moves groups from inefficient to more efficient equilibria or system states, provided the _cost of punishment is not too high_ relative to the benefit (Liu & Guo, 2010; Tao et al., 2011; Castro et al., 1998; Evans & Thomas, 2001; Robert et al., 2012; Annen, 2011).
- **Effect is context-dependent:** The _magnitude_ of efficiency gain depends strongly on the game’s structure—e.g., duration (number of rounds), probability of continuation, severity and cost of punishment, player count, observability, and reporting mechanisms (Evans & Thomas, 2001; Annen, 2011; Jones, 1999).
- **Punishment is more effective with larger groups, full observability, and coordination:** Efficiency gains are typically more robust in environments with larger groups and where punishment can be credibly and accurately targeted or reported (Annen, 2011; Castro et al., 1998).
- **Short games or weak punishment often yield little gain:** With few rounds, or when the ability to punish is limited—either by high punishment cost, low magnitude, or lack of observability—the increase in efficiency may be negligible or offset by punishment costs (Liu & Guo, 2010; Billard, 1996).
- **Threshold effects and parameter regimes:** Theoretical results stress _explicit thresholds_—for instance, minimum severity or minimum number of rounds—for punishment to yield efficiency (Evans & Thomas, 2001; Jones, 1999).
- **Behavioral (not payoff) outcomes commonly measured:** Many models find that punishment increases cooperation/contribution, but not all translate directly to net efficiency gains, because punishment itself consumes resources (Billard, 1996).

# 5) Prediction Guidance

Given the game design dimensions and the control efficiency, the consensus of this literature suggests:

- **Enabling peer punishment generally increases predicted efficiency _relative to control_, as long as punishment is not excessively costly and can be effectively targeted.**
    - The magnitude of gain is:
      - **Greater with more rounds (or higher continuation probability)**, because threat of future punishment is more credible.
      - **Stronger in larger groups, and when punishment cost is moderate but not negligible** (Liu & Guo, 2010; Annen, 2011).
      - **Reduced** or **possibly offset** if punishment costs outweigh the gains from increased cooperation (Billard, 1996; Liu & Guo, 2010).
    - The **mapping from control to treatment efficiency is not directly given** (no effect sizes or equations), but _direction and moderators are well-supported_.
- **Design features that support visibility and accuracy (e.g., show_other_summaries, show_punishment_id) increase the efficacy of punishment and thus efficiency gains**.
- **When control efficiency is already near-maximum, room for improvement is limited; when it is low, punishment enables a jump _if design features support credible, low-cost punishment_.**
- **Non-payoff behavior (cooperation rates) should not substitute for efficiency in prediction, but higher observed control cooperation suggests lower marginal benefit of punishment.**

# 6) Design Dimensions Highlighted Across Papers

#### Directly Informed Dimensions

- **player_count**: Frequently discussed, especially for moderating punishment effectiveness in large vs small groups (Annen, 2011; Tao et al., 2011).
- **num_rounds**: Central to most theory (Evans & Thomas, 2001; Jones, 1999; Tao et al., 2011), as longer/repeated interactions favor punishment’s impact.
- **mpcr**: Sometimes modeled (Liu & Guo, 2010; Castro et al., 1998), affects benefit-cost ratio.
- **punishment_cost/punishment_tech**: Core to multiple models (Liu & Guo, 2010; Billard, 1996; Castro et al., 1998), critical in determining if punishment increases efficiency.
- **show_other_summaries/show_punishment_id**: Implicated in observability, reporting, and peer enforcement (Annen, 2011; Castro et al., 1998; Robert et al., 2012).
- **all_or_nothing**: Sometimes explicitly modeled, though usually less central.

#### Indirectly Informed / Contextually Discussed

- **chat**: Discussed as a social facilitator (Billard, 1996), not analytically modeled.
- **reward_exists/reward_cost/reward_tech**: Mentioned (Sigmund & Hilbe, 2011; Billard, 1996), but not directly modeled in terms of efficiency shifts vis-à-vis punishment.
- **show_n_rounds**: Sometimes included in model structure, less emphasized for efficiency itself.

#### Effectively Missing

- **default_contrib**: Not discussed or modeled in this set.
- **reward-related dimensions as moderators of punishment**: Not systematically explored in relation to efficiency.

# 7) Important Limitations

- **No empirical calibration or effect sizes:** All results are theoretical or simulation-based, with _no direct empirical validation_. The literature supports qualitative direction (“punishment will increase efficiency if...”) but not quantitative predictions for real-world settings or effect magnitude.
- **Limited direct coverage of full PGGs with peer punishment and efficiency as the primary outcome:** Many models are adjacent (PD-like, flow control games, reputation), not canonical PGGs.
- **Behavioral outcomes often substituted for efficiency:** Multiple papers use cooperation rate or equilibrium structure, not true payoff-based efficiency, as their result variable. This can overstate the policy value if punishment is costly.
- **Conditional effectiveness:** Effectiveness depends on design—high punishment costs, short horizons, imperfect observability, or limitations in punishment action can sharply constrain or negate efficiency gains.
- **Neglect of certain dimensions:** Some design features relevant to prediction (e.g., default contribution, details of reward tech/cost) are not meaningfully addressed.
- **No evidence from laboratory or field experiments:** Limitations in external validity and robustness to unmodeled human behavior.
- **Potential for over-generalization:** The logical findings about punishment effectiveness often hinge on strong modeling assumptions (infinite repetition, rationality, discounting), which may not hold in practical settings.

---

**Summary:**  
The theoretical literature in this set robustly supports the qualitative prediction that enabling peer punishment can increase efficiency in public-goods-like games—especially when design parameters (duration, group size, cost/benefit ratio, observability) are favorable. However, quantitative estimates or the exact mapping from control to treatment efficiency are lacking, and many moderator dimensions are only partially addressed. Prediction should be sensitive to the actual game design parameters, with closer attention to those most strongly supported in theory (player count, number of rounds, punishment cost and implementation, observability), acknowledging key limitations and the absence of empirical effect sizes.
