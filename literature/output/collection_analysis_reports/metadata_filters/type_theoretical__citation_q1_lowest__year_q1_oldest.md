# 1) Evidence Base

The paper set consists entirely of theoretical papers (29/29), including some with simulation evidence, but none reports original empirical or experimental data. Most papers develop formal models or simulation results exploring the interplay between cooperation, punishment/reward, and group outcomes in repeated social dilemma games, N-person interactions, or public-goods-like settings. While a minority focus directly on public goods games (PGGs), many address closely related paradigms such as repeated Prisoner’s Dilemma, resource pooling, or networked cooperation. The set is broad conceptually but relatively narrow for the downstream prediction task in terms of direct, parameterized, and empirical evidence on payoff efficiency in PGGs with/without punishment. Only a handful discuss specific design dimensions of games (e.g., punishment cost, multiplier, information settings) in detail relevant to prediction.

# 2) Task Relevance

**pgg_or_variant:**
- **exact:** Only a few papers model standard public goods games directly, and mainly from a theoretical standpoint (e.g., Liu & Guo, 2010; Zhao et al., 2010).
- **close:** Several use repeated or networked social dilemmas, with structures that are highly analogous (e.g., Janus & Lim, 2009; Evans & Thomas, 2001; Corriveau, 2012; Tao et al., 2011). These frequently generalize to or encompass public goods environments.
- **adjacent–weak:** Many papers treat N-person games, repeated Prisoner’s Dilemma, or other environments sharing the key challenges of public goods but not with the same payoff and action structure (e.g., Ishida, 2009; Aramendia, 2006).

**punishment_or_sanctions:**
- **exact:** A substantial portion of the set analyzes punishment or sanctioning mechanisms as a central variable, including peer punishment, community enforcement, and formal/contractual punishment (e.g., Matsushima, 2012; Aramendia, 2006).
- **adjacent/mention only:** Several other papers discuss punishment mechanisms only conceptually, focus on adjacent mechanisms (e.g., exclusion, blackmail), or as one among several forces influencing cooperation.

**efficiency_or_related_payoff_outcome:**
- **exact:** Several papers analyze efficiency, group payoff, total welfare, or system utility as key outcomes (e.g., Janus & Lim, 2009; Tao et al., 2011; Evans & Thomas, 2001). Measures are either explicitly efficiency (payoff relative to optimum) or group-level total payoff.
- **adjacent/close:** Others highlight outcomes such as the abundance of cooperators or norm compliance, using these as partial proxies for welfare (Liu & Guo, 2010), but do not always provide direct efficiency results.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes** are explicitly modeled or theorized in about half the set, especially as:
    - Group efficiency (aggregate payoff / optimal payoff), welfare, total earnings, surplus, coins generated (Janus & Lim, 2009; Evans & Thomas, 2001; Matsushima, 2012; Tao et al., 2011; Robert et al., 2012; Corriveau, 2012; Heller & Sieberg, 2008).
    - Average fitness or system utility in evolutionary settings (Liu & Guo, 2010; Watve et al., 2011; Castro et al., 1998).

- **Non-payoff behavioral outcomes** (not directly efficiency/payoff) dominate in several papers:
    - Cooperation rate, prevalence of cooperators/non-cooperators, norm compliance.
    - Dynamics of strategy prevalence, cycles of cooperation or free-riding, or the effect of social/moral norms (Ma et al., 2009; Whitmeyer, 2004; Ziegler, 1997).
    - These measures are sometimes interpreted as proxies for welfare when they lead to higher payoffs, but they cannot be equated with efficiency and may be confounded by the cost of interventions (see Billard, 1996).

# 4) Main Findings Relevant To Prediction

**Synthesized empirical and theoretical findings:**

- **Punishment tends to increase efficiency relative to control (no-punishment) games,** provided certain conditions are met:
    - **Cost of punishment:** Effects are positive if punishment cost is moderate and not too high relative to the benefit of cooperation (Liu & Guo, 2010; Heller & Sieberg, 2008). If punishment is too costly, the burden overrides efficiency gains.
    - **Severity/effectiveness of punishment:** Efficient outcomes are only achievable if punishment is sufficiently severe or “draconian” to deter deviation (Evans & Thomas, 2001); mild or “nondraconian” punishment may not suffice.
    - **Repeated interaction and patience:** Punishment is effective at sustaining cooperation in repeated/intertemporal settings, especially when players are sufficiently patient (high discount factor) and can observe or credibly report each other's actions (Janus & Lim, 2009; Corriveau, 2012; Aramendia, 2006; Tao et al., 2011).
    - **Credibility and enforcement:** The design of the punishment phase (finite vs. infinite, contingent on observed defection, possibility of side payments/blackmail for stabilizing policing, etc.) shapes robustness (Watve et al., 2011; Aramendia, 2006).
    - **Group size and monitoring:** The effect of punishment can strengthen with group size, provided mechanisms for community enforcement, information sharing, or reputation exist (Annen, 2011). In very large or poorly observed groups, incentives for community punishment may weaken, requiring more institutional supports.
    - **Non-monotonic and multiple equilibria:** Some models (Whitmeyer, 2004) predict that punishment can produce sharply non-linear or even catastrophic effects, with the possibility that efficiency collapses at intermediate monitoring levels, depending on initial compliance or historical path dependence.

- **Design features that interact with punishment's efficacy:**
    - **Punishment cost/payout ratio** (direct evidence): Several models (Liu & Guo, 2010; Heller & Sieberg, 2008) provide explicit conditions under which the cost of punishment must be small enough relative to cooperation benefit for punishment to increase efficiency.
    - **Punishment mechanism/technology:** Models distinguish between direct, indirect, and mixed punishment, with mixed mechanisms being most robust (Corriveau, 2012); collective punishment (Nash reversion) can enforce efficiency under broader conditions (Janus & Lim, 2009).
    - **Information and observability:** Efficiency gains from punishment are far greater when actions and reputations are fully observable or can be credibly reported (Robert et al., 2012; Annen, 2011).

- **Theoretical consensus:** Given repeated interaction, credible and not-too-costly punishment, and reasonable monitoring/observability, enabling punishment will likely increase efficiency compared to control. Results are conditional and often not monotonic—there are threshold and regime effects.

# 5) Prediction Guidance

**How the literature should inform prediction of treatment efficiency from design dimensions plus control efficiency:**

- **Direction of Effect:** The strongest theoretical support points to an increase in efficiency relative to the control (no-punishment) game when peer punishment is enabled, as long as punishment is not prohibitively costly and is credibly enforceable and observed (Liu & Guo, 2010; Janus & Lim, 2009; Corriveau, 2012; Heller & Sieberg, 2008).
- **Context and Moderators:** The magnitude and even direction of effect depend on:
    - **Punishment cost:** Higher costs for punishers are likely to reduce or nullify efficiency gains; some models predict no gain or even negative effects at high cost.
    - **Group size and information:** Larger groups with observable actions or exogenous reporting support greater efficiency gains; if monitoring or reporting is endogenous or costly, the benefit is reduced (Annen, 2011).
    - **Game length:** Repetition, especially with an unknown or long horizon, enables threat of punishment to sustain cooperation and thus maximum efficiency (Matsushima, 2012; Tao et al., 2011).
    - **Punishment mechanism:** The efficacy and robustness of efficiency gains rise with the severity, credibility, and transparency of punishment strategies (Evans & Thomas, 2001; Aramendia, 2006).
    - **Initial conditions:** Some models highlight path dependence: with poor initial compliance or moderate monitoring, efficiency may collapse even with punishment (Whitmeyer, 2004).

- **Mapping from control to treatment efficiency** can be expected to be:
    - **Positive shift:** Treatment efficiency will generally be above control efficiency in the same game design, but not necessarily to full efficiency.
    - **Conditional:** The shift is greater for designs with moderate punishment cost, high monitoring, repeated interaction, and clear observability.
    - **No simple quantitative rule:** The theory is clear about directionality and conditions but does not yield precise quantitative effect sizes for most design dimension combinations.
- **Payoff-based guidance (not just behavioral rates):** Predictions should focus on group payoff or efficiency solely, and avoid inferring welfare from cooperation rates absent explicit cost calculations.

# 6) Design Dimensions Highlighted Across Papers

- **Directly informed dimensions:**  
    - **player_count:** Several models address the moderating effects of group size, both for the possibility and magnitude of efficiency gains (e.g., Annen, 2011; Corriveau, 2012).
    - **num_rounds:** Game repetition is foundational and underlies nearly all positive predictions for punishment-induced efficiency (e.g., Tao et al., 2011; Aramendia, 2006).
    - **mpcr:** Appears in several models as a key parameter for cooperation benefit (Liu & Guo, 2010; Zhao et al., 2010).
    - **punishment_cost:** Explicitly modeled as critical for efficiency (Liu & Guo, 2010; Heller & Sieberg, 2008).
    - **punishment_tech:** Various forms/theories of punishment mechanism and strategy analyzed (Janus & Lim, 2009; Corriveau, 2012; Evans & Thomas, 2001).

- **Indirectly/contextually informed dimensions:**
    - **reward_exists, reward_cost, reward_tech:** A few papers compare the impact of sanctions (punishment) and incentives (reward) (Billard, 1996; Ishida, 2009).
    - **show_other_summaries, show_punishment_id:** Discussed in theoretical form as information or observability; not always directly mapped to experimental implementation (Annen, 2011; Robert et al., 2012).
    - **all_or_nothing/continuous:** Variously present as binary or continuous choices but less central to efficiency predictions in the theoretical literature reviewed.

- **Dimensions essentially missing/weakly addressed:**
    - **chat:** Only Billard (1996) and a few others mention communication, generally as a contextual factor, not a parameter with direct modeled effects.
    - **default_contrib:** Not systematically modeled; framing effects, opt-in/opt-out defaults, or endowment framing are missing as explicit prediction moderators.
    - **show_n_rounds:** Occasionally appears (Matsushima, 2012; Corriveau, 2012) but as a contextual rule, not a flexible design dimension.

# 7) Important Limitations

- **Empirical gaps:** The entire set is theoretical and/or simulation-based. There is no empirical quantification of effect sizes for enabling punishment under varying design conditions, nor direct calibration to real-world or laboratory data.
- **Parameterization and mapping:** While many dimensions are discussed, few models provide explicit parameterized mappings from the full set of design dimensions (e.g., group size, punishment details, information conditions) to predicted efficiency shifts.
- **Scope of generalization:** Many results are adjacent or close but not exact to standard public goods games (e.g., they analyze repeated Prisoner’s Dilemma, not PGG), so translation to a canonical PGG may introduce error.
- **Payoff proxies and confusion:** Some papers infer efficiency changes from behavioral measures (cooperation/norm compliance), which may not align with actual group payoffs if intervention costs are substantial.
- **Boundary cases and ambiguity:** Several models stress strong conditions on patience, observability, and punishment cost, with ambiguous or even negative predicted effects outside these domains (e.g., Whitmeyer, 2004). Multiple equilibria or nonlinear regime shifts (catastrophes) highlight unpredictability in some cases.
- **Limited coverage of some design dimensions:** Key experimental manipulations like chat, framing (default_contrib), identity revelation, or reward mechanisms are sparsely or only contextually covered.

**In sum:**  
This theoretical literature provides robust qualitative and conditional guidance: when peer punishment is enabled in public-goods-game-like repeated environments, group efficiency is likely to rise, especially when punishment is not overly costly, is transparent, and is credibly enforceable. The strength and even direction of the effect critically depend on the detailed structure of punishment, group size, monitoring, and patience. There is no empirical quantification or precise functional form available for linking the full set of predictor dimensions to treatment efficiency, so prediction must proceed with caution, nuance, and explicit attention to the conditional logic revealed in this literature.
