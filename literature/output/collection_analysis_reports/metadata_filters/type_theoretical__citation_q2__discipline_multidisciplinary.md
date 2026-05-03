# 1) Evidence Base

The literature base consists exclusively of **theoretical and simulation modeling papers**, with no direct experimental or empirical studies involving human subjects or field data. Out of 56 papers, a moderate subset (less than a third) model **standard public goods games (PGGs) with explicit punishment** and directly analyze **group efficiency or related payoff-based outcomes**—the central focus of the downstream prediction task. Most remaining papers either:
- Analyze adjacent games (e.g., Prisoner's Dilemma, common-pool resource, or auction/procurement environments),
- Examine only cooperation rates or other behavioral measures,
- Or discuss contextual factors and mechanism arguments without direct reference to efficiency effects of punishment in PGGs.

The literature thus provides a **foundational but not comprehensive** theoretical mapping of how punishment interacts with various PGG design dimensions to affect efficiency. The evidence is relatively **broad in terms of mechanisms and parameter sweeps covered** (group size, punishment cost, etc.), but **narrow in empirical grounding and lacking direct observation of actual efficiency effect sizes**.

# 2) Task Relevance

### a) pgg_or_variant
- **Exact:** About a quarter of papers model standard PGGs closely matching the prediction task (e.g., Hetzer & Sornette, 2013; Roberts, 2013; Bodnar & Salathé, 2012; Ye et al., 2016; Hintze et al., 2020).
- **Close/Adjacent:** Many address close variants (e.g., CPR, prisoner's dilemma, auctions with punishment), often preserving collective-action structure but varying key game-theoretic details (pool punishment, resource dynamics, etc.).
- **Weak/None:** Numerous papers do not model PGGs or analyze only indirect mechanisms/context.

### b) punishment_or_sanctions
- **Exact:** Papers modeling and manipulating explicit **punishment (peer, pool, or centralized)**, with detailed parameterization (e.g., cost, impact) are frequent in the exact and close PGG papers.
- **Adjacent:** Others conceptualize punishment through adjacent mechanisms (institutional fees, reputation loss, targeted exclusion) or discuss reward as a contrast class.
- **Weak/None:** Many papers only cite punishment as theoretical background or do not include it.

### c) efficiency_or_related_payoff_outcome
- **Exact/Close:** Some models compute or predict **group efficiency or average payoff** under control vs. punishment conditions; results are sometimes qualitative (phase diagrams, bifurcation points) rather than quantitative effect sizes.
- **Adjacent:** Many report only contribution rates, norm compliance, or other **behavioral outcomes** as proxies for efficiency.
- **Weak/None:** Several papers mention efficiency or payoff in passing but do not model or measure it.

**Summary:** The strongest, most directly relevant evidence comes from a minority of theory/simulation studies designed specifically to model PGGs with controllable punishment and output group efficiency/payoff statistics. Much of the paper set is adjacent, contextual, or focused on mechanistic arguments, limiting their use for direct prediction.

# 3) Outcomes Measured In The Literature

### a) Payoff-Based Outcomes
- **Direct Efficiency/Group Payoff:** A cluster of papers output average group payoff or efficiency as the main outcome, sometimes providing explicit thresholds or formulas for when punishment increases efficiency (e.g., Hetzer & Sornette, 2013; Roberts, 2013; Bodnar & Salathé, 2012; Ye et al., 2016; Hintze et al., 2020).
- **Theoretical Optima/Equilibria:** Several present phase diagrams or equilibrium analysis showing when maximal or suboptimal efficiency is theoretically attainable.

### b) Behavioral (Non-Payoff) Outcomes
- **Contribution/Cooperation Rates:** A larger set of papers report only average or equilibrium cooperation/contribution rates, norm following, or prevalence of strategy types, and do not model group efficiency as a function of these behaviors.
- **Punishment/Reward Frequency:** Some analyze punishment frequency, targeting, or procedural mechanisms divorced from efficiency measurement.
- **Strategy Prevalence/Norm Stability:** Studies of evolutionary/status models and network structure focus on the persistence of strategies and do not report efficiency.

**Importantly:** Several papers explicitly note that while increased cooperation is commonly observed with punishment, the net efficiency gain depends also on the cost and collateral effects of punishment—a distinction often lost in behavioral-only studies.

# 4) Main Findings Relevant To Prediction

Synthesizing across the most directly relevant theory/simulation studies:

- **Enabling punishment in standard PGGs often increases group efficiency,** especially when:
    - Punishment is cheap and/or effective (low cost to punisher, high fine to defector);
    - The punishment regime covers relevant interactions (high institutional reach, effective peer targeting);
    - Returns to cooperation have increasing returns to scale or sufficient synergy (Ye et al., 2016).
- **Threshold and non-linear effects are common:** There are typically sharp phase transitions; a small increase in punishment impact or reach can shift the group from low- to high-efficiency equilibria (Hetzer & Sornette, 2013; Bodnar & Salathé, 2012).
- **Punishment cost is a critical moderator:** Efficiency gains are offset or sometimes erased if punishment is too costly (Hintze et al., 2020).
- **Group size (player_count) and number of rounds (num_rounds):** Most models hold efficiency gains for small to moderate group sizes and in repeated games, but large groups or one-shot games present challenges for sustaining efficiency gains via punishment.
- **Alternative/adjunct mechanisms (e.g., inclusion, reward, joint liability):** Some papers argue these can supplement or even replace punishment, but do not systematically report on their efficiency impact relative to punishment.
- **Heterogeneity and social preferences:** In settings with highly competitive agents or conflicting incentives, punishment can backfire and decrease efficiency (Honjo & Kubo, 2020).
- **Population structure:** Networks with sufficient clustering and targeted punishment support higher efficiency; poorly structured networks (e.g., high average degree) can undermine norm stability and efficiency (Galan et al., 2011).
- **Continuous vs. discrete contribution:** Some theoretical results caution that in continuous-contribution environments, punishment alone may not create stable high-efficiency equilibria unless other forces (discreteness, strong moral motives) are present (Yan et al., 2023).

**Disagreements/Ambiguity:**
- Some models predict that in specific social preference environments or game structures (e.g., highly competitive SVOs), punishment does not raise and may even lower efficiency.
- Theory is strong and consistent; empirical validation is absent in this set.

# 5) Prediction Guidance

**Based on this literature, the following guidance is appropriate:**

- **When the control (no-punishment) game has low efficiency,** and punishment parameters (cost/impact) are favorable, **enabling punishment is likely to cause a large increase in efficiency**—potentially shifting the group into a high-efficiency equilibrium. This is supported quantitatively and qualitatively in canonical PGG models (Hetzer & Sornette, 2013; Roberts, 2013; Bodnar & Salathé, 2012).
- **The effect size depends critically on game design dimensions:**
    - **Punishment cost and magnitude:** Lower cost and/or higher magnitude improve efficiency gains, but excessive punishment costs can negate benefits or even reduce efficiency if punishment costs outweigh cooperation gains.
    - **Coverage and reach of punishment:** Incomplete punishment regimes or spatially limited institutions may fail to deliver efficiency gains until a critical threshold is reached.
    - **Group size and rounds:** Stable efficiency gains from punishment are more likely in small, repeated-game settings.
    - **Return structure (mpcr, IRS):** Nonlinear or increasing returns to scale can magnify the positive efficiency impact of punishment.
- **Caveats:** In environments with competitive social preferences or ambiguous punishment targets, punishment can lower efficiency (Honjo & Kubo, 2020). In continuous-choice games, punishment alone may not create stable high-efficiency outcomes (Yan et al., 2023).
- **Prediction from control efficiency:** If the control game already exhibits high efficiency, the marginal effect of enabling punishment may be diminished or even negative.

**Apply the literature using conditional logic:**
- *If* punishment is designed to be effective (cost < impact), coverage is high, and group design is standard (discrete PGG, repeated), *then* expect a substantial positive shift in efficiency when punishment is enabled.
- *If* control efficiency is already high, returns to scale are flat, or punishment is costly/ineffective, *then* anticipate little or no efficiency gain, or possibly a decline in efficiency, when punishment is introduced.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Design Dimensions:** 
- **player_count** (group size): Extensively modeled; efficiency effects of punishment are most robust in small groups; scaling effects discussed (Hetzer & Sornette, 2013; Roberts, 2013).
- **num_rounds:** Most models are of repeated games; efficiency gains from punishment are more pronounced in repeated vs. one-shot games.
- **mpcr:** Central in nearly all theory papers; threshold effects, phase transitions dependent on MPCR (Bodnar & Salathé, 2012; Ye et al., 2016).
- **punishment_cost, punishment_tech:** Critical drivers of whether punishment leads to higher efficiency (cost/impact ratio, institutional/peer/coverage).
- **all_or_nothing:** Most theory assumes binary contribution, but some discuss continuous (see caveats).
- **show_other_summaries:** Information on others can impact dynamics, but efficiency implications less directly shown.
- **reward_exists, reward_cost, reward_tech:** Some papers contrast reward and punishment mechanisms; usually show punishment is more effective for efficiency gains (Mondal et al., 2022).
- **show_n_rounds, show_punishment_id, chat, default_contrib:** Rarely modeled or only as context, not as manipulated dimensions.
- **default_contrib, chat:** Not systematically examined for their impact on efficiency with/without punishment in this set.

**Indirectly Informed/Contextually Discussed:**
- **show_other_summaries, show_n_rounds:** Referenced in relation to information structure and observability but without explicit efficiency results.
- **reward_exists, reward_cost, reward_tech:** Discussed mainly in relation to alternatives to punishment; effect on efficiency less reported.

**Effectively Missing:**
- Empirical variation in **chat**, **default_contrib**, and **show_punishment_id**—virtually absent as manipulated variables affecting efficiency in punishment-enabled PGGs.

# 7) Important Limitations

- **Lack of empirical data:** All evidence is based on theoretical models or simulations; no validation from experimental or field data in this set.
- **Behavioral vs. payoff outcomes:** Many findings conflate or substitute behavioral outcomes (e.g., cooperation rates) for true payoff/efficiency metrics, which can be misleading since punishment costs can offset cooperation gains.
- **Context specificity:** The degree to which model results (often stylized, assuming homogeneous, rational actors, or extreme punishment parameters) translate to real-world or laboratory PGGs is contested and untested herein.
- **Sparse data on several design dimensions:** Parameters such as **chat**, **default contribution framing**, and **information about punishers** are not systematically modeled; effect modifiers like player heterogeneity, communication, or the possibility of second-order punishment are largely overlooked or only mentioned.
- **Ambiguity and disagreement:** Some models predict negative or null efficiency effects of punishment under specific social preferences or game structures; evidence is not always convergent.
- **No effect size calibration:** While the direction of efficiency change is generally predicted, there are few or no empirical or simulation-based effect sizes quantifying the magnitude of efficiency gains for the full range of design dimension settings.

---

**Summary:** **Strong theory supports the conditional expectation that punishment enables large efficiency gains in PGGs—provided punishment is effective, group structure is favorable, and baseline efficiency is low.** The predicted effect is sensitive to cost/impact ratios, institutional reach, game structure (e.g., continuous vs. discrete), and underlying social preferences. However, several design dimensions are barely addressed, and there is considerable uncertainty—and no calibrated, empirically validated effect sizes—in this literature. Predictions beyond the core design variables should be made cautiously.
