# 1) Evidence Base

The paper set comprises 44 papers, predominantly laboratory experiments (empirical, experimental, lab-based), with several field experiments, and a few observational/theory-based studies. The set is skewed toward classic and close variants of the public goods game (PGG) and related social dilemmas targeting cooperation, often manipulating punishment and/or reward mechanisms. A minority of papers treat adjacent or broader cooperation dilemmas, or third-party punishment in non-PGG contexts.

A minority of the included studies report efficiency or directly related group payoff measures, which are the most relevant for the downstream prediction task. Many studies emphasize non-payoff behavioral outcomes, such as cooperation rates and punishment behavior, with less focus on direct effects on group efficiency or welfare. Overall, the evidence base is moderately broad, offering several high-quality empirical PGG-punishment studies with efficiency data, but with considerable reliance on behavioral proxies or adjacent paradigms, particularly for nuanced or less typical game design dimensions.

---

# 2) Task Relevance

**pgg_or_variant**  
- **exact:** A substantial fraction of papers employ the standard public goods game or a direct linear PGG variant, giving *exact* relevance for the core task (e.g., Kamijo et al., 2020; Eriksson & Strimling, 2012; Lo Iacono et al., 2023; Bravo & Squazzoni, 2013).
- **close:** Some papers employ close variants—e.g., threshold games, Prisoner's Dilemmas with group structure, ROSCA games, or common-pool resource dilemmas (e.g., van Miltenburg et al., 2017; Koike et al., 2018; Sadowski et al., 2015).
- **adjacent/weak/none:** A substantial tail of studies use adjacent setups (e.g., Dictator Games with punishment, third-party punishment, trust games), which are less relevant for efficiency prediction in PGG environments.

**punishment_or_sanctions**  
- **exact:** Many studies directly manipulate the presence/absence of punishment or sanctions (Kamijo et al., 2020; Lo Iacono et al., 2023; Bravo & Squazzoni, 2013).
- **adjacent:** Others look at rewards, exclusion, or reputational mechanisms, or focus on punishment in adjacent game types.
- **none:** Several key baseline/control studies lack any punishment or sanctioning (useful for control efficiency estimation, but not for treatment predictions).

**efficiency_or_related_payoff_outcome**  
- **exact/close:** Only a subset reports group efficiency or directly related payoff-based outcomes (group payoff, welfare, surplus) as primary results (Kamijo et al., 2020; Eriksson & Strimling, 2012; Lo Iacono et al., 2023; Bravo & Squazzoni, 2013; Salahshour et al., 2022; van Miltenburg et al., 2017).
- **adjacent:** Several others focus on contributions, cooperation rates, or punishment assignments, which are behavioral but not direct payoff measures. Some record earnings, but not in a form normalized for efficiency.
- **weak/none:** Many behavioral or psychological studies report neither efficiency nor payoffs.

**Summary:**  
- Evidence most strongly supports scenarios with classic or minor-variant linear PGGs, experimentally manipulated peer punishment, and measured group efficiency/payoff. For many game design features, evidence is less direct or missing.

---

# 3) Outcomes Measured In The Literature

**Payoff-Based Outcomes (highly target-relevant):**
- **Efficiency (group payoff / social optimum):** Explicitly reported in key studies (Kamijo et al., 2020; Eriksson & Strimling, 2012; Lo Iacono et al., 2023; Bravo & Squazzoni, 2013; van Miltenburg et al., 2017; Ozono et al., 2016; Koike et al., 2018; Salahshour et al., 2022).
- **Total earnings, group profit, joint welfare:** Sometimes reported in lieu of efficiency percentages.

**Non-Payoff Behavioral Outcomes (less target-relevant):**
- **Contribution rate, cooperation rate:** Common primary outcomes, especially in studies that do not report payoffs or efficiency (Lefebvre & Stenger, 2020; Kubena et al., 2014; Dickson et al., 2022).
- **Punishment behavior:** Frequency, targeting, antisocial punishment (Kubena et al., 2014; Paál & Bereczkei, 2015).
- **Norm compliance, moral emotions, fairness/punishment preference:** Reported mainly in adjacent literature.

**Notably, contribution/cooperation effects can diverge from efficiency if the cost of punishment outweighs gains from increased contributions, or if antisocial punishment is prevalent.**

---

# 4) Main Findings Relevant To Prediction

### Punishment’s Effect on Efficiency: Patterns Across Dimensions

- **Baseline: Enabling punishing peers (peer punishment) in standard PGGs generally increases group efficiency over no-punishment controls, especially when punishment is sufficiently strong, focused, and the underlying PGG is efficient (MPCR >0.5) (Eriksson & Strimling, 2012; Lo Iacono et al., 2023; Bravo & Squazzoni, 2013).**
- **Exceptions:**
    - **Inefficient PGGs (MPCR <1):** Punishment alone does **not** significantly increase efficiency or payoffs, but reward does (Kamijo et al., 2020).
    - **Noisy Punishment:** Introducing stochasticity to punishment impact (punishment noise) sharply reduces or reverses efficiency gains (Salahshour et al., 2022; van Miltenburg et al., 2017). Efficient (deterministic) punishment is necessary for positive effects; noisy implementation leads to more errors, antisocial punishment, and lower payoffs.
    - **Antisocial/Competitive Punishment:** Environments with rank-based/tournament incentive structures, or where punishment is used for rivalry/status rather than norm enforcement, see little or even negative impact on efficiency (Paál & Bereczkei, 2015; Romano et al., 2024). The presence of punishment can lower group payoffs if misused.
    - **Collective/Weak Sanctions:** Collective or consensus-based punishment mechanisms are less effective (or negative) if monitoring is noisy or if the sanction regime is not credible and direct (Chapkovski, 2021; Koike et al., 2018).
    - **Institution Choice:** When players are allowed to voluntarily join sanctioning institutions, those who enter punishment regimes gain higher efficiency, but the effect is tightly linked to being able to opt in and the absence of communication or endogenous weakening (Lo Iacono et al., 2023).

- **Magnitude of Effect:**  
    - *Efficiency Gain Size*: When peer punishment works (strong, deterministic, external, or institutionally imposed), efficiency rises from near Nash equilibrium levels to near social optimum (Eriksson & Strimling, 2012).
    - *Relative to Reward*: Reward can often outperform punishment in inefficient PGGs (Kamijo et al., 2020; Bravo & Squazzoni, 2013).

- **Moderator Effects:**  
    - **Punishment Technology:** High-impact, low-cost, and deterministic punishment is most effective; costly, weak, or noisy punishment impairs or reverses efficiency gains (Salahshour et al., 2022; Bond, 2019).
    - **Group Composition (Cooperative propensities):** Externally imposed strong punishment lifts non-cooperative groups to the efficiency of cooperative ones (Eriksson & Strimling, 2012).
    - **Communication/Chat:** Often held constant/no chat in main studies. Evidence on chat as moderator is limited.
    - **Feedback/Transparency:** Full feedback enhances effect; punishment is more effective when actions are observable.
    - **Gender/Identity:** Some interaction with collective sanctions (Chapkovski, 2021) and social context, but not systematically examined.
    - **Control Efficiency:** Larger efficiency effects of punishment seen where baseline/control efficiency is low and punishment technology is strong (Eriksson & Strimling, 2012; Lo Iacono et al., 2023).

---

# 5) Prediction Guidance

The literature supports the following structured guidance for predicting the **average efficiency of the same game when peer punishment is enabled**:

- **When the control (no punishment) game has moderate or low efficiency, and peer punishment is enabled with a strong, deterministic, low-cost/high-impact technology in a standard linear PGG, the literature consistently finds a substantial increase in efficiency—often approaching the social optimum (Lo Iacono et al., 2023; Eriksson & Strimling, 2012).**
- **In contrast, if punishment is:**
    - *Noisy or stochastic*: Expect substantially reduced or even negative effects, relative to control (Salahshour et al., 2022; van Miltenburg et al., 2017).
    - *Implemented as a weak, non-credible, or costly mechanism*: Effect size is much smaller or absent (Paál & Bereczkei, 2015; Koike et al., 2018).
    - *Contextually competitive/tournament-based*: Punishment may be used non-cooperatively, yielding no efficiency gains or even losses (Paál & Bereczkei, 2015; Romano et al., 2024).
    - *In an inefficient PGG (MPCR <1)*: Punishment alone does *not* increase efficiency (Kamijo et al., 2020).

- **Enabling reward (with or without punishment) can increase efficiency more strongly, especially in inefficient PGGs.**
- **If the control game already achieves near social optimum efficiency, enabling punishment adds little or may reduce efficiency if punishment is misapplied or antisocial.**
- **If key design dimensions (punishment cost, impact, group size, round count, information structure) differ from classic experiments, or are not known, predictive confidence is reduced: extrapolation should assume weaker/uncertain effects.**

*Importantly, do not infer efficiency increases from behavioral outcomes (higher contributions) unless costs and side-effects of punishment are accounted for explicitly.*

---

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**  
- **player_count:** Multiple studies vary group size; main findings are drawn from groups of 4 to 12. Effect of punishment is robust across this range if other design features are held constant (Kamijo et al., 2020; Lo Iacono et al., 2023).
- **num_rounds:** Most experiments report the number of rounds; longer games show more pronounced institution/treatment effects.
- **mpcr:** Several studies directly assess MPCR (Kamijo et al., 2020; Bravo & Squazzoni, 2013). Critical for interpreting when punishment is effective; punishment increases efficiency primarily where MPCR indicates an efficient PGG (MPCR ≥1 or close).
- **punishment_cost/punishment_tech:** Frequently manipulated; effect size of punishment on efficiency is highly sensitive to the cost-to-impact ratio and determinism of punishment (Eriksson & Strimling, 2012; Salahshour et al., 2022).
- **all_or_nothing:** Included in many studies; no clear moderator effect observed in the context of efficiency, unless combined with other features (van Miltenburg et al., 2017).
- **reward_exists/reward_cost/reward_tech:** Explicitly manipulated in some studies (Kamijo et al., 2020; Bravo & Squazzoni, 2013), showing reward can sometimes outperform punishment.
- **show_n_rounds, show_other_summaries, show_punishment_id:** Sometimes specified, but rarely manipulated systematically with respect to efficiency outcomes.
- **chat:** Usually not enabled; effect on efficiency under punishment not directly studied.

**Indirectly Informed/Contextually Discussed:**  
- **default_contrib:** Studied without punishment; not evaluated as moderator for punishment’s impact on efficiency.
- **show_punishment_id/identification:** Mentioned in passing; some studies employ identified sanctions, but effect of identifiability not isolated.

**Missing or Weakly Covered Dimensions:**  
- **default_contrib, show_punishment_id (as modulator), chat (as moderator for punishment efficacy):** Largely missing direct experimental manipulation in conjunction with efficiency outcomes.
- **Interaction/Moderation among design features (e.g., chat × punishment, feedback × punishment):** Very limited evidence.
- **Contextual moderators (such as culture, gender, competition/framing):** Examined in some adjacent or close studies, but not systematically measured for efficiency.

---

# 7) Important Limitations

- **Limited Direct Evidence on All Prediction Dimensions:** Most studies tightly control a subset of design features (player count, MPCR, punishment cost, rounds), so the moderating effects of less-standard dimensions (chat, default contribution framing, feedback structure) are unclear.
- **Sparse Reporting of Efficiency Outcomes:** Many studies measure only behavioral effects (e.g., contribution rates) or focus on mechanisms, making inferences about efficiency indirect. Results based on contributions or punishment frequency should not be overgeneralized to efficiency when punishment is costly or used antisocially.
- **Potential Publication Bias and Homogeneous Lab Conditions:** Most high-relevance studies use undergraduate samples in laboratory settings, possibly limiting generalizability to field or diverse demographic settings.
- **Ambiguity about Antisocial or Strategic Punishment:** Some designs (competitive/tournament setups, contexts of ambiguous norm violations) find no positive efficiency effect, or negative effects, but don’t always measure collective versus individual impacts robustly.
- **Limited Evidence on Complex/Endogenous Institutions:** Few studies allow for endogenous institution building, varying punishment/reward settings, or co-evolution of rules and behavior.
- **Adjacency of Some Key Evidence:** Several papers use close but non-identical environments (threshold games, contest games, ROSCA, or third-party punishment tasks), which may not fully generalize to standard PGG contexts.

**Conclusion:**  
The literature strongly supports that enabling strong, deterministic, well-targeted peer punishment in standard PGGs robustly increases efficiency when baseline efficiency is low (due to defection), with the effect size moderated (and sometimes reversed) by the design dimensions of punishment technology, group structure, and payoff framing. Where punishment is weak, noisy, expensive, or used strategically (rather than for norm enforcement), efficiency gains are absent or negative. Extrapolation to parameterizations not directly studied (e.g., rare or interacting dimensions) should be undertaken cautiously, and efficiency should not be inferred solely from increased contribution rates. Reward mechanisms can outperform punishment under inefficiency. The evidence base is strong for canonical, “classic” PGGs but sparser for novel, hybrid, or real-world institutional environments.
