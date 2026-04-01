# 1) Evidence Base

This literature set consists entirely of **theory papers** (no empirical or direct experimental studies), representing a large and broad survey of recent and classic evolutionary game theory, simulation, and analytical work on public goods games (PGGs) and related environments. The review is thus shaped by models of repeated and networked social dilemmas, evolutionary dynamics, and institutional design. The set includes many exact-relevance PGG studies, as well as close and adjacent variants (e.g., repeated PD, threshold public goods, pool/peer punishment, exclusion, reputation systems, and meta-norm games). The coverage of **efficiency or payoff-based outcomes** is high—many papers provide explicit group payoff, welfare, or efficiency results, although a substantial fraction focus on behavioral or evolutionary equilibrium outcomes (e.g., cooperation rate, punisher abundance) without always calculating efficiency per se.

Quantitative predictions are largely based on *simulation and mathematical modeling*, resulting in explicit formulaic/parameterized or qualitative predictions for how various game design dimensions influence efficiency with and without punishment. Empirical grounding is typically provided via calibration to existing experiments or meta-analytic review of parameter ranges, but direct empirical effect sizes are rare. The set is **comparatively comprehensive for theoretical PGGs with punishment and efficiency**, but there are notable gaps in experimental, real-world, and field-evidence for out-of-sample generalization.

# 2) Task Relevance

**pgg_or_variant:**  
- **exact:** The majority of included studies model the standard PGG or very close variants (repeated linear PGG, voluntary/threshold PGG, structured/network PGG, or spatial PGG with punishment).  
- **close:** Many models extend to environments like repeated public goods with opt-out, peer/pool punishment, institution formation, or adjacent resource dilemmas (CPR games with sanctions).  
- **adjacent/weak:** Some studies focus only on the closely related Prisoner's Dilemma, snowdrift games, or donation games, or analyze mechanisms such as exclusion, partner selection, reputation, or social learning in dyadic or group settings.

**punishment_or_sanctions:**  
- **exact:** The bulk of the theory addresses peer or pool punishment, costly institutional enforcement, coordinated punishment technology, or related sanctioning mechanisms.
- **close/adjacent:** Several papers examine exclusion, social ostracism, metanorms, indirect punishment via reputation loss, or dynamic peer pressure, which often serve as analogs to explicit costly punishment.
- **weak/none:** Some work focuses on reward-only, social learning, group selection, or voluntary participation settings with no explicit sanctioning.

**efficiency_or_related_payoff_outcome:**  
- **exact:** Many papers report group efficiency (payoff relative to full cooperation), mean group payoff, welfare, or total resource abundance directly; several provide explicit conditions under which enabling punishment increases or decreases efficiency.
- **close:** Some studies use average payoff of cooperators/punishers, resource sustainability (CPR), or payoff-based equilibrium as a welfare proxy.
- **adjacent/weak:** A considerable subset focuses only on behavioral outcomes (cooperation rates, abundance of strategies) without mapping these to group payoff or efficiency, requiring inferential leaps.

# 3) Outcomes Measured In The Literature

- **Payoff-based outcomes (exact/close relevance):**
  - **Efficiency/group payoff:** Many theoretical models calculate group payoff, normalized utility, surplus, or efficiency (as defined by the ratio to full cooperation).
  - **Related: welfare, resource abundance, equilibrium mean earnings, or minimized efficiency loss.**
- **Non-payoff behavioral outcomes:**
  - **Cooperation rate/frequency, prevalence of strategies (cooperators, defectors, punishers, etc.), norm compliance, stability or abundance of cooperation, extinction/survival of types.**
  - These are often linked to efficiency only when punishment costs are explicitly considered—not all studies close this loop.
- **Hybrid:** Some studies report both, showing, for example, that cooperation rates can be high while efficiency is reduced (due to the cost of punishment or antisocial sanctioning).

# 4) Main Findings Relevant To Prediction

**Empirical themes and points of agreement:**

- **Enabling (well-designed) punishment almost always increases efficiency relative to no-punishment, when:**
    - Punishment cost is not too high, and punishment is sufficiently effective (i.e., high fine per unit cost) (Dutta et al., 2021; Hetzer & Sornette, 2013; Wang et al., 2025; Kranz, 2010).
    - The control game (no punishment) is inefficient (e.g., dominated by defectors).
    - The institutional or network structure allows punishment to be coordinated (Hwang, 2017; Powers, 2018; Bodnar & Salathé, 2012).
    - Meta-punishment, reputation, or coordination prevents the collapse into second-order free riding or antisocial punishment (Yamamoto & Okada, 2016; Galan et al., 2011).

- **Punishment can fail to increase efficiency or even reduce it when:**
    - Punishment cost is high or effectiveness is low (Roberts, 2013; Sui et al., 2018).
    - There is antisocial punishment or counter-punishment (Zhang & Pei, 2022; Brandts & Fatas, 2012; Handfield et al., 2016).
    - Retaliation (punished agents punish back) or corruption is possible (Wolff, 2012; Fang et al., 2020; Shi et al., 2022).
    - Game is short, group composition is unstable, or information on others' behavior is poor (Frey & Rusch, 2012; Powers, 2018).
    - Societal or group context is competitive or norm disagreement is high (Honjo & Kubo, 2020; Barrett, 2020).

- **Punishment/reward balance:**  
    - Several models find an optimal mix of punishment and reward maximizes efficiency, with too much of either reducing group welfare (Cong et al., 2016; Wang et al., 2011; Yao & Chen, 2014).

- **Many models identify explicit parameter thresholds:**  
    - Above a critical value for punishment effectiveness, efficiency transforms from low (defection) to high (cooperation) (Hetzer & Sornette, 2013; Cui et al., 2019).
    - Bistability and regime shift are common: with certain initial conditions or parameter ranges, both high and low efficiency states can be stable (Liu et al., 2024; Liu et al., 2019).
    - In settings with increasing returns to scale (IRS), punishment increases efficiency more dramatically (Ye et al., 2016).

- **Dimension-level effects:**
    - **player_count:** Efficiency effects of punishment can increase in larger groups when punishment is coordinated (Hwang, 2017), but diminish without coordination or in rival enforcement regimes (Buchholz et al., 2014).
    - **num_rounds:** Longer games allow learning and accumulation of efficiency gains from punishment (Frey & Rusch, 2012; Dutta et al., 2021).
    - **mpcr:** The effect of punishment is larger when MPCR is moderate/low; at high MPCR, cooperation may already be stable (Farjam et al., 2015; Zhuang et al., 2012).
    - **punishment_cost/punishment_tech:** Lower cost, higher effectiveness shifts efficiency gains upward; there can be non-monotonicities—punishment that is too harsh or costly can lower efficiency (Kranz, 2010; Nuño et al., 2010).
    - **all_or_nothing, chat, reward_exists, reward_cost/tech:** Evidence for these is sparse or indirect (discussed below in section 6).

**Points of disagreement or ambiguity:**

- Some adjacent models (especially in highly competitive or misaligned social preference settings) find that punishment can decrease efficiency (Honjo & Kubo, 2020; Handfield et al., 2016).
- In the presence of antisocial punishment or uncoordinated sanctioning, punishment may reduce both cooperation and efficiency (Brandts & Fatas, 2012; Galan et al., 2011; Handfield et al., 2016).
- Empirical laboratory effect sizes and real-world generalizability are not assessed; all predictions are theoretically derived.
- Some models show that non-punitive mechanisms (voluntary participation, exclusion, partner selection, or reward) can substitute for punishment, making its marginal effect on efficiency context-dependent or zero (Ding et al., 2023; Kurokawa, 2019).

# 5) Prediction Guidance

- **Enabling peer punishment in a PGG-like environment is predicted to increase group efficiency relative to the same design with punishment disabled, under the following conditions:**
    - Punishment cost is moderate or low, punishment impact per cost is sufficiently high, and the baseline (control) efficiency is low (i.e., widespread defection).
    - The game enables coordinated, targeted, or collective punishment, preventing second-order free riding and antisocial punishment.
    - The punishment institution matches the scale of the public good (local punishment for local goods, collective for global) (Vasconcelos et al., 2022).
    - Sufficient rounds or repeated interactions to allow behavioral adaptation and learning (Frey & Rusch, 2012; Dutta et al., 2021).
    - No or limited retaliation, corruption, or norm disagreement; punishment is perceived as legitimate/fair (Wolff, 2012; Barrett, 2020).

- **Key moderators and their integration into prediction:**
    - Control (no-punishment) efficiency serves as a baseline, but the efficiency *jump* due to punishment will be larger when baseline efficiency is low.
    - The *direction* and *magnitude* of the effect are mainly set by: punishment cost, punishment effectiveness (fine per cost), group size, MPCR, length of the game, institutional structure (peer, pool), and coordination capacity.
    - Reward existence or a mixed system can further shape efficiency—optimal efficiency is often achieved at intermediate punishment/reward mixtures.
    - Pool/institutional punishment and reputation-based exclusion can, in specific contexts, outperform simple peer punishment in sustaining efficiency.

- **Cautions and boundary conditions:**
    - Effect is *not* universally positive: high punishment costs, antisocial punishment, uncoordinated or poorly targeted punishment, or competitive social preference structures can reduce efficiency, sometimes below the control (Handfield et al., 2016; Honjo & Kubo, 2020).
    - The presence of voluntary participation, exclusion, partner choice, or sufficiently high MPCR (i.e., baseline efficiency already high) can render the incremental efficiency effect of punishment null or negative.
    - Theories are sensitive to parameters: threshold-type effects are common; models often specify a critical punishment cost/impact above which efficiency improves, or below which punishment is ineffective or counterproductive.

- **Summary guidance:**  
  *For making predictions from game design and control efficiency: If the core game structure is a standard or repeated PGG, and if punishment is moderate/low-cost, high-effectiveness, well-coordinated, and applied in an environment with moderate to low MPCR or control efficiency, then enabling punishment should be expected to produce a substantial jump in efficiency, approaching the fully cooperative benchmark in some parameter regimes. The predicted magnitude of this jump is largest in inefficient controls, smaller in moderate-efficiency controls, and could be zero or negative if the above conditions are not met.*

# 6) Design Dimensions Highlighted Across Papers

**Best informed dimensions (direct support):**
- **player_count**: Most models analyze group size effects on punishment efficacy, especially its role in thresholds, coordination, and the risk of free riding (Hwang, 2017; Sui et al., 2017).
- **num_rounds**: Theoretical and computational papers analyze repeated interactions and their effect on learning and the long-run efficiency of punishment regimes (Frey & Rusch, 2012; Dutta et al., 2021).
- **mpcr**: Marginal per-capita return is a key variable in determining both baseline and post-punishment efficiency (Farjam et al., 2015; Zhuang et al., 2012).
- **punishment_cost, punishment_tech**: Directly modeled and shown to be major moderators of efficiency change (Roberts, 2013; Van Cleve, 2016; Nuño et al., 2010).
- **reward_exists, reward_cost, reward_tech**: Several studies analyze reward in combination with punishment and as an alternative, noting differential effects on efficiency depending on mix and context (Cong et al., 2016; Yao & Chen, 2014).

**Indirectly informed or contextually discussed:**
- **all_or_nothing (contribution granularity)**: Modeled in some studies, particularly threshold games and models with discrete vs. continuous action, but typically secondary to primary findings.
- **chat**: Few models include direct communication; some reviews or simulation studies reference communication as a moderator (Noussair & van Soest, 2014) but do not provide quantitative mapping to efficiency outcomes.
- **default_contrib**: Not typically varied or explicitly analyzed, though some models mention framing or initial conditions as affecting equilibrium selection.
- **show_n_rounds, show_other_summaries, show_punishment_id**: Information dimensions are sometimes modeled (reputation, observability, summary feedback), but most theoretical work assumes full or perfect information, making translation to these variables indirect.

**Sparse/missing dimensions:**
- **default_contrib**, **chat**, **show_partial_summaries**: Only occasionally mentioned, with little direct analysis of their effect on payoff-based outcomes or efficiency.
- **Network structure and identity features:** While network structure is analyzed (spatial, small world, scale-free, etc.), mapping to peer identification or punishment identity is not always explicit.

# 7) Important Limitations

- **Lack of empirical effect sizes and variability:** All findings are derived from theory or simulation; predictions on efficiency jumps must be interpreted as potential rather than average or guaranteed effects.
- **Non-monotonicity and threshold effects:** Many models emphasize critical parameter values (for cost, impact, etc.); small changes near thresholds can flip predicted outcomes, making fine-grained prediction error-prone.
- **Behavioral outcomes versus efficiency outcomes:** A sizeable minority of models report only cooperation rates, strategy frequencies, or equilibrium abundance, not actual efficiency or group payoff; in those cases, extrapolation to efficiency requires caution.
- **Generalizability and context dependence:** Many models assume infinite or well-mixed populations, perfect information, and stylized assumptions about updating and learning; real-world and experimental generalizability is not tested.
- **Limited analysis of complex design features:** Certain design dimensions (chat, detailed information structure, default contribution, identity of punishers/rewarders) are under-theorized; presence or absence in real-world or experimental settings may moderate effects in unknown ways.
- **Uncertainty about the marginal effect size with additional mechanisms:** In environments already rich in reward, exclusion, or partner choice, the added efficiency benefit of enabling punishment is ambiguous.
- **Possibility of antisocial punishment and retaliation:** Some theoretical and simulation models point to strong negative effects from uncoordinated, misaligned, or anti-social punishment, which can reduce efficiency (Brandts & Fatas, 2012; Handfield et al., 2016), but the formulas for these effects are rarely specified.
- **Dependence on initial conditions and evolutionary path:** Several studies show hysteresis, bistability, and path dependence: identical designs can result in different long-term efficiency depending on initial strategy abundances or random drift.

---

**In summary:**  
The literature provides strong theoretical, simulation, and formulaic support for the prediction that enabling peer punishment in standard or close-variant PGGs increases efficiency, but the effect is highly parameter-dependent and can be negative if punishment is costly, antisocial, or poorly coordinated. Efficiency gains are most reliably predicted when punishment is moderate/low cost, highly effective, coordinated, and when the baseline efficiency is low, but context effects (reward, exclusion, communication) and certain game design features (information, group structure) must be considered. Many parameter-specific analytical conditions are available for integrating game design variables into predictions, but empirical validation and out-of-sample effect calibration are lacking.
