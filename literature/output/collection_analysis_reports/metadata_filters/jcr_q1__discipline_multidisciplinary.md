# 1) Evidence Base

The paper set is broad (449 sources), with a large and representative coverage of both empirical (lab and field experiments) and theoretical/modeling papers directly focused on public goods games (PGGs), punishment/sanctioning mechanisms, and related payoff-based outcomes such as efficiency, group payoff, and welfare. The majority of directly relevant studies are controlled, laboratory-based experiments, supplemented by an extensive body of formal theory and simulation. There is a substantial fraction of adjacent or peripheral studies (e.g., Ultimatum and Prisoner's Dilemma games, real-world field contexts, prosocial behavior without direct payoff analysis), but the evidence base for PGGs with explicit punishment and efficiency outcomes is extensive and robust for the prediction task.

Empirical papers dominate the core evidence for efficiency in actual PGGs, while theory/simulation papers provide detailed mechanism insight and allow systematic exploration across design dimensions. Some empirical studies include nuanced manipulations of design parameters (e.g., punishment cost, group size, MPCR, institution choice, central vs. peer punishment, presence of reward, chat, visibility, etc.), allowing for strong inferences about causal effects on efficiency.

# 2) Task Relevance

**pgg_or_variant:**  
- The literature contains a large proportion of studies with `exact` relevance—standard PGGs and close variants (e.g., linear, binary/all-or-nothing, threshold/collective risk, networked PGGs). There is also a significant number of studies with `close` or `adjacent` relevance (e.g., prisoner’s dilemma, threshold games, trust games, field analogues).
- For task purposes, the evidence is sufficiently rich and directly relevant for most design dimension–outcome combinations needed in PGG-like settings.

**punishment_or_sanctions:**  
- Coverage is extensive and of `exact` relevance: all key punishment technologies (peer, centralized, pool, institutional, probabilistic, reputation-based, exclusion/ostracism, anti-social punishment, etc.) are examined. Both enabling and disabling punishment (as experimental treatments) and their consequences are focal.
- Studies also cover reward mechanisms and their comparison to punishment, as well as environment/contextual moderators such as reputation, corruption, communication, and cultural norms.

**efficiency_or_related_payoff_outcome:**  
- Many studies report `exact` efficiency outcomes: group earnings as a fraction of the social optimum (fully cooperative outcome), average payoffs, welfare, or surplus. Sometimes group payoff is reported directly, sometimes in comparison to a maximum or Nash baseline, or as “public goods provision.”
- A substantial subset reports only `close` or `adjacent` outcomes (e.g., mean contribution rates, maximally achieved group payoffs, proportion of rounds achieving success), which are not identical to efficiency as defined by the downstream task, but are closely correlated.

Thus, task relevance is `high` for the trio of outcome, setting, and mechanism required for prediction.

# 3) Outcomes Measured In The Literature

**Payoff-based outcomes:**  
- Group efficiency (total payoff as a fraction of the maximum possible), surplus generated, group profit, welfare, and average individual payoff are frequently and explicitly reported in both empirical and theoretical studies.
- Some models provide exact analytic expressions or simulation outcomes for efficiency under varied game parameters, including direct comparison of control (no punishment) and treatment (with punishment) conditions.

**Non-payoff behavioral outcomes:**  
- There is extensive reporting of behavioral measures such as contribution rates, cooperation frequencies, frequency and targeting of punishment, anti-social punishment prevalence, and emotion/norm-based mechanisms.
- Several papers highlight the distinction: increased cooperation rates do not always translate into increased efficiency, especially when punishment costs are substantial.

The literature makes an explicit effort to distinguish and (when possible) formally connect changes in contribution behavior to resulting efficiency outcomes.

# 4) Main Findings Relevant To Prediction

**General effect of punishment on efficiency:**  
- Adding (peer/institutional) punishment to standard PGGs usually increases group efficiency *when* punishment is effective, not prohibitively costly, and is not dominated by antisocial punishment or corruption (Fehr & Gächter 2002; Gürerk et al. 2006; Lo Iacono et al. 2023; Hilbe et al. 2014).
-However: High punishment costs, prevalence of antisocial punishment, ineffective targeting, noise, and risk of vendetta or retaliation often offset or reverse the efficiency gain (Simpson et al. 2017; Herrmann et al. 2008; Fehl et al. 2012; van Miltenburg et al. 2017; Salahshour et al. 2022; Wu et al. 2016; Bond et al. 2019).
- Empirically, efficiency is most improved by punishment when the baseline (control) efficiency is low due to widespread free riding; the effect is weaker/diminished or can even be negative when the baseline is already high or when punishment is misused (Jiang et al. 2013; Kamijo et al. 2020; Ozono et al. 2020).

**Moderators and mechanisms:**  
- **Punishment cost/effectiveness (“tech”):** Lower-cost/higher-impact punishment increases efficiency; too costly punishment can reduce it by direct resource loss (Simpson et al. 2017; Hintze et al. 2020; Zefferman 2023).
- **Noise/antisocial punishment:** Noise in the punishment mechanism, or high levels of antisocial punishment, substantially reduce—or even reverse—the efficiency gains from punishment (Salahshour et al. 2022; Wu et al. 2016; Herrmann et al. 2008).
- **Peer vs. institutional punishment:** Institutional/centralized (e.g., leader) punishment often produces higher efficiency than peer punishment, mostly due to less redundant/wasteful punishment (Harrell 2019; Gross et al. 2016).
- **Second-order punishment and self-governance:** The presence of second-order punishment (punishing non-punishers) or externally imposed enforcement increases efficiency beyond peer punishment alone (Hilbe et al. 2014; Perc 2012).
- **Reward vs. punishment:** Reward mechanisms (alone or in combination) can match or outperform punishment in raising efficiency, as they sustain cooperation without the resource cost associated with punishment (Rand et al. 2009; Kamijo et al. 2020; Góis et al. 2019).
- **Game difficulty (MPCR, local inefficiency):** Punishment is only effective when cooperation is not structurally inefficient (Ozono et al. 2020; Kamijo et al. 2020); in “harder” (lower MPCR) games or when local and global incentives are misaligned, the effect of punishment can be null or negative.
- **Institutional design (voluntary participation, observability, coordination):** Voluntary participation, group voting, norm-signaling, communication, and reputation/observability all moderate (usually increase) the efficiency benefit of punishment (Hauert et al. 2007; Rockenbach & Milinski 2006; Andrighetto et al. 2013).
- **Demographic context (group composition/heterogeneity):** Group structure and composition (uniform vs. pluriform) and cultural/social context are strong moderators of punishment’s effect on efficiency (Molenmaker et al. 2023; Alexander & Christia 2011).

**Edge cases and failures:**  
- In repeated dyadic games, punishment rarely increases efficiency and can even lower it, as the resource costs of punishment outweigh the gain in cooperation (Dreber et al. 2008; Wu et al. 2009; Wang et al. 2017).
- Institutional or leader punishment that can be corrupted (e.g., via bribery) leads to dramatic efficiency loss (Muthukrishna et al. 2017; Lee et al. 2019).
- When punishment is used competitively (rather than to enforce cooperation), or as a means of rivalry/status, it often undermines efficiency (Gross & De Dreu 2019; Paál & Bereczkei 2015; Romano et al. 2024).

# 5) Prediction Guidance

**For the downstream task (predicting efficiency with punishment enabled from control game design and control efficiency):**
- **Baseline:** Most standard lab PGGs with moderate/low initial (control) efficiency see a substantial increase in efficiency when peer or centralized punishment is enabled, provided it is effective and not too costly (evidence from multiple directly relevant studies: Fehr & Gächter 2002; Lo Iacono et al. 2023; Chaudhuri & Paichayontvijit 2017; Rockenbach & Milinski 2006; Gächter et al. 2017).
- **Magnitude:** The increase can be large (e.g., from 10–40% to 70–95% of the social optimum) but strongly depends on punishment cost/tech, group size, antisocial punishment prevalence, presence of communication, presence of reward, and game difficulty (MPCR).
- **Moderators:**  
    - **Punishment Cost/Tech:** Higher cost or lower effectiveness reduces efficiency gain. Optimal effect occurs at moderate cost/effectiveness; too high or too low can promote antisocial punishment or retaliation cycles.
    - **Noise and Anti-social punishment:** High noise or anti-social punishment prevalence strongly predicts negligible or negative efficiency effects of enabling punishment; control efficiency is not a sufficient predictor in these cases.
    - **Game framing/alignment:** When cooperation is inefficient or benefits only the global but not local group, punishment has little or no positive effect on efficiency.
    - **Alternative mechanisms:** In settings where reward or reputation mechanisms are present and salient, these can achieve similar or higher efficiency than punishment at lower resource cost.

- **Generalizable Patterns:**  
    - **If control efficiency is low**, and the design permits targeted, effective, not-too-costly punishment, with low antisocial punishment/noise and without alternative individual solutions, enabling punishment is highly likely to raise efficiency substantially.
    - **If control efficiency is already high**, or punishment is costly, non-targeted, or subject to corruption, the marginal effect on efficiency may be minimal or even negative (especially if costly punishment is used wastefully).
    - **If antisocial punishment is common or likely (e.g., high group heterogeneity, perceived unfairness, cultural context), punishment may reduce or fail to increase efficiency—explicitly reported in cross-cultural studies.

- **Treatment efficiency is never reliably predictable from control efficiency alone:** Key game design moderators must be included to avoid overestimating punishment effects.

- **Edge/exception cases:** When punishment is implemented as exclusion or via institutionally guided/collective mechanisms, or when combined with norm-signaling or communication, the efficiency effect can be maximized.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions:**
- `player_count`: Substantial experimental and theoretical manipulation; group size frequently shown to moderate punishment effectiveness and efficiency.
- `num_rounds`: Variation in rounds shows the effect of horizon on the sustainability and magnitude of efficiency gains from punishment.
- `mpcr`: Extensively discussed; strong moderator of baseline cooperation and the effect of punishment.
- `punishment_cost`, `punishment_tech`: Heavily analyzed; cost-to-impact ratio is a key moderator of efficiency effects from punishment.
- `all_or_nothing`: Both continuous and binary models are studied; dimension is directly relevant to specific effects (e.g., coordination vs. social dilemma).
- `reward_exists`, `reward_cost`, `reward_tech`: Many studies compare reward and punishment, revealing important interactions and tradeoffs.
- `show_other_summaries`, `show_n_rounds`, `show_punishment_id`: Some studies explore observability, information structure, and transparency as moderators of efficiency and punishment.

**Indirectly or contextually discussed dimensions:**
- `default_contrib`: Few studies manipulate default framing, but some discuss the effect of opt-in/opt-out on baseline cooperation.
- `chat`: Communication is tested in a moderate number of studies; its presence often boosts efficiency and can substitute for punishment.
- `show_punishment_id`: Some studies examine anonymity vs. identifiable punishment, showing effects on antisocial punishment and retaliation.
- `show_other_summaries`: Not always directly manipulated, but feedback structure is discussed in the context of monitoring and norm enforcement.

**Effectively missing or sparsely covered:**
- `default_contrib`, and more nuanced forms of framing are less frequently manipulated.

**Well established moderators:**  
- punishment cost/effectiveness, group size, horizon, MPCR, structure of interaction (network/local/global), social/ethnic homogeneity, information about others’ actions, observability of punishment, existence and structure of reward mechanisms.

# 7) Important Limitations

**Prediction for non-standard PGGs:**  
- Many adjacent papers (Prisoner's Dilemma, Dictator, Trust Games, field contexts) do not generalize quantitatively to standard multi-person PGGs, especially on the effect size/magnitude of punishment on efficiency.

**Cultural/contextual variation:**  
- The effect of punishment on efficiency can vary widely with cultural norms, prevalence of antisocial punishment, and structural features not captured in lab designs (Herrmann et al. 2008; Alexander & Christia 2011).

**Edge-case effects and structural dependence:**
- Efficiency gains from punishment are conditional on a suite of moderating factors (punishment cost/tech, strength of correlation with antisocial punishment, existence of alternative solutions like reward or partner choice, etc.); simple averages from experimental treatments may mislead if applied to games with differing design dimensions.

**Payoff vs. behavior measures:**  
- Many studies measure only contribution rates or behavioral outcomes rather than true efficiency as required for the prediction task. Where these are used as proxies, caution is warranted as they may overestimate efficiency gains in the presence of costly punishment.

**Complex environments and mechanism interaction:**  
- Effects found in lab studies with canonical parameters may not generalize to more complex, dynamic, or ecologically realistic settings (e.g., with opportunity for corruption, bribery, strategic competition, selective exclusion, or partner choice).

**Institutional detail missing:**  
- Some dimensions, such as the structure and visibility of punishment/reward, rules for norm communication, or real institutional context, are underexplored despite being potentially important moderators in real-world cases.

**Empirical generalizability versus model-driven effect sizes:**  
- Theoretical models often identify precise thresholds and phase transitions not always mapped directly to empirical parameter ranges. For high-stakes predictions, empirical calibration is recommended.

---

In sum:  
- The available literature provides detailed, directly relevant, and multidimensional evidence for predicting PGG efficiency under varying punishment regimes, group structures, and game design dimensions—especially in standard lab and canonical theoretical settings.
- Prediction must be contingent on core moderators: punishment cost/tech, group size, MPCR, presence of noise and antisocial punishment, and the structure and observability of the punishment mechanism.
- Control efficiency alone is rarely sufficient; design dimension moderators and context are essential for reliable prediction.
- Reward mechanisms, communication, institution choice, and exclusion/ostracism can offer equal or greater efficiency improvements, sometimes making punishment unnecessary or suboptimal.
- When predicting for out-of-sample designs (or environments with high societal heterogeneity, corruption opportunities, or non-canonical institutions), available evidence should be interpreted cautiously and, where possible, ground-truthed with empirical or high-fidelity simulation results.
