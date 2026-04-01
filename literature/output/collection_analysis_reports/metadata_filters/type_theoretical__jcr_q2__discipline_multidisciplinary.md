# 1) Evidence Base

This literature set comprises six papers, all of which are theoretical or modeling studies, with none reporting experimental or empirical data. The breadth of the set is broad in the sense that it explores a variety of social dilemma games—including PGG-adjacent, N-person games, and spatial/repeated Prisoner’s Dilemma models—but is narrow with respect to the target prediction task: predicting efficiency changes due to peer punishment in public goods game (PGG) or highly similar settings. Of the six, only one paper (Jaffe, 2008) addresses social punishment as an explicit mechanism, and only two others (Zhang et al., 2020; Szilagyi & Somogyi, 2010, agent-based simulation) include parameters directly analogous to PGG design dimensions. Critically, efficiency or payoff-based outcomes—the primary target for the downstream prediction—are not a central measured outcome in any of the studies.

# 2) Task Relevance

For the three target-relevance axes:

**1. pgg_or_variant:**  
- **Labels:** All papers are at best "adjacent" to PGG (not exact). None are standard economic or experimental public goods games; several study N-person dilemma games or repeated/spatial PD.
- **Detail:** Four papers model games with similar social dilemma structures but not true PGGs. Two are based on the Prisoner's Dilemma; none implement a continuous contributions mechanism with marginal per capita returns (MPCR), the PGG hallmark.

**2. punishment_or_sanctions:**  
- **Labels:** Only Jaffe (2008) is "exact" in its treatment of punishment as a central mechanism; Zhang et al. (2020) is "adjacent" with a form of punishment/negative returns; the rest are "none."
- **Detail:** Most papers lack explicit punishment, sanctions, or reward mechanisms as in PGGs. Only Jaffe (2008) directly models and discusses social punishment; Zhang et al. (2020) models negative returns akin to punishment but not operationalized as post-hoc peer punishment.

**3. efficiency_or_related_payoff_outcome:**  
- **Labels:** No paper is "exact;" two are "close" (N-person chicken game, but not with punishment), the rest "adjacent" or "none."
- **Detail:** Most measure non-payoff behavioral outcomes (cooperation rates, generosity, trait dynamics). None report empirical or simulated group efficiency, total payoff, or welfare as a tracked or main outcome.

# 3) Outcomes Measured In The Literature

Across the set, the measured outcomes are almost exclusively non-payoff behavioral variables:
- **Primary:** Proportion of cooperators, cooperation rates, generosity frequency, trait/strategy frequencies, evolution or stability of cooperation or pro-social behavior.
- **Secondary:** In Zhang et al. (2020), willingness to cooperate given structural parameters; in Jaffe (2008), evolutionary stability of behavioral traits in response to shame and punishment.

**Payoff-based outcomes**—such as group efficiency, surplus, group payoff, total earnings, or welfare—are not directly analyzed, reported, or plotted in any paper. When mentioned, they are inferred only contextually (e.g., higher cooperation *could* yield higher payoff), but the studies do not compute or validate this for their models.

# 4) Main Findings Relevant To Prediction

- **Punishment effects:** Only Jaffe (2008) shows that the presence of punishment (especially costless) or evolved shame can stabilize higher levels of pro-social behavior (i.e., generosity) over time. However, fluctuations between high and low cooperation are noted, and no efficiency or group payoff measures are reported. The evolutionary lens means findings pertain to stability of cooperation rather than outcome magnitude.
    - *Interpretation for payoff context:* If higher cooperation translates to higher efficiency in similar game structures, punishment might be expected to increase efficiency—*but this is not directly demonstrated.* 

- **Moderate sanctions plus incentives:** Zhang et al. (2020) finds that moderate punishment for noncooperation, together with reward, increases willingness to cooperate among agent classes (local governments, organizations, poverty groups). However, the effect on efficiency or payoff is not quantified; main data is about cooperation or intent, not monetary outcomes.
    - *Interpretation for payoff context:* Increased cooperation generally correlates with higher efficiency in standard PGGs, but because the model is more complex and not a standard PGG, this remains qualitative and indirect.

- **Payoff structure sensitivity:** The N-person game studies (Szilagyi & Somogyi, 2010, both) show that small parameter shifts in payoff function can cause drastic, non-monotonic changes in the prevalence of cooperation. No group payoff or efficiency data are included; no punishment mechanisms are modeled.

- **Mutation and cooperation cycles:** The repeated PD and spatial models (Toupo et al., 2014; Johnson, 2023) demonstrate that cooperation can be maintained or even dominate via mutation or spatial configuration, but do not include punishment or report on efficiency.

# 5) Prediction Guidance

Given these findings:
- **Direct Prediction:** There is no direct evidence in this paper set on how enabling peer punishment in a PGG (with accompanying design parameters) shifts group efficiency, holding baseline efficiency constant.
- **Indirect Evidence:** Both Jaffe (2008) and Zhang et al. (2020) provide indirect, qualitative evidence that the introduction of punishment (especially at low or moderate cost) can stabilize or increase cooperative behavior. If one assumes that in PGG-like settings more cooperation increases efficiency, this suggests *a likely increase* in efficiency when peer punishment is enabled.
- **Caveats:** Without direct payoff data, the magnitude, functional form, or situational conditions are not illuminated. Behaviors may oscillate or be unstable due to evolutionary or agent dynamics (Jaffe, 2008).
- **Other Design Effects:** The adjacent studies emphasize that other design parameters (payoff structure, complexity, presence of reward, agent update rules) can produce abrupt or surprising shifts in outcome, suggesting that predictions based on punishment alone may be overly simplistic.

In sum: Evidence supports the expectation that enabling peer punishment in PGG-like environments generally increases cooperation, and by plausible extension, group efficiency—especially if the cost of punishment is low to moderate. However, the absence of direct, quantitative efficiency data or precise mappings from behavior to payoff means that only qualitative prediction is justified.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed:**  
- punishment_cost (Jaffe, 2008; Zhang et al., 2020)
- player_count (Szilagyi & Somogyi, 2010; Zhang et al., 2020)
- num_rounds (Szilagyi & Somogyi, 2010; Toupo et al., 2014)
- all_or_nothing (Szilagyi & Somogyi, 2010; Toupo et al., 2014)
- reward_exists (Zhang et al., 2020)

**Indirectly/contextually discussed:**  
- default_contrib / default_contrib_prop (implied in agent strategies and cooperation definitions, but not as manipulable design variables)
- mpcr (payoff function sensitivity discussed in N-person games, though not labelled as such)
- punishment_tech / punishment_magnitude (Jaffe, 2008 refers to costliness, but not implementation details)
- chat, show_n_rounds, show_other_summaries, show_punishment_id, reward_cost, reward_tech, reward_magnitude (not discussed or missing)

**Effectively missing:**  
- Most peer communication/social information mechanisms (chat, visibility)
- Technical implementation of punishment/reward (how punishment is delivered, identity revelation)
- Direct manipulation or reporting of default contribution, framing, round count visibility, and Marginal Per Capita Return (as an explicit parameter)
- No study tracks explicit group payoff, welfare, or surplus, nor do they tie contribution rates to measured efficiency.

# 7) Important Limitations

- **No empirical or experimental data:** All evidence is from theoretical or agent-based modeling, which limits validation of claims with actual human behavior or real payoff data.
- **No direct efficiency outcomes:** No paper reports group efficiency, total payoff, welfare, or surplus as a central measured outcome, severely limiting the predictive value for the target task.
- **Mostly adjacent games:** The studied games are social dilemmas but do not implement all core features of PGGs (e.g., continuous contributions with MPCR, real economic incentives, explicit post-hoc peer punishment).
- **Punishment mechanisms not detailed or missing:** Only two papers treat punishment in ways relevant to PGGs, and only one makes it a central mechanism.
- **Behavior-payoff translation is assumed:** The link between increased cooperation and increased efficiency is assumed but not tested, leaving outcome predictions speculative.
- **Sparse coverage of key design dimensions:** Several prediction-relevant game parameters (communication, reward cost/tech, visibility of information, and explicit implementation details) are unaddressed.
- **Generalizability:** The complex and context-specific models, especially with multiple agent types or spatial structures, may not translate cleanly to standard laboratory or field PGGs with peer punishment.

**Conclusion:**  
This paper set offers only indirect, qualitative support for the expected positive effect of enabling peer punishment on efficiency in PGG-like settings. Absence of actual efficiency data, minimal overlap with canonical PGG design, and lack of experimental replication mean that any quantitative or highly nuanced prediction from this literature should be made with great caution.
