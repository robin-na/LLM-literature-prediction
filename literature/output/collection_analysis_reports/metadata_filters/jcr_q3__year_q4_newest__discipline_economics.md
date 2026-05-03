# 1) Evidence Base

This literature set comprises 21 papers, with a moderate mix of empirical (laboratory experiments dominate) and theoretical work. The focus is largely on public goods or closely related team/cooperative dilemmas. Of these, only a subset offer direct empirical evidence on efficiency or closely related payoff outcomes in public-goods-game (PGG) settings with and without peer punishment enabled. Several papers study adjacent mechanisms (e.g., coalition formation, allocation, automatic penalties, or institutional punishment) or concentrate on behavioral outcomes (e.g., contributions, norm compliance, punishment frequency) rather than efficiency per se.

Overall, the evidence base is moderately broad in its exploration of group contribution environments but is limited in its direct, quantitative, and systematic treatment of the marginal effect of peer/punishment-enabling interventions on group efficiency across diverse PGG designs. Empirical support for prediction of efficiency outcomes with punishment is found, but the set is narrower and more fragmented for the specific prediction task.

# 2) Task Relevance

### a) `pgg_or_variant`
- **Relevance:** The majority of the studies explicitly use the PGG or its close variants (`exact` or `close`). A minority use adjacent designs (e.g., networked PD, collective-risk dilemmas).
- **Label spread:** Most: `exact` or `close`; Some: `adjacent`.

### b) `punishment_or_sanctions`
- **Relevance:** Only a subset of papers feature treatment arms where peer punishment or similar sanctioning mechanisms are enabled (`exact` or `close`). Several others use adjacent mechanisms, such as endogenous allocation, coalition exclusion, or automatic penalties. Many studies do not include any form of punishment or sanction (`none`).
- **Label spread:** Some: `exact`; Several: `adjacent`; Many: `none`.

### c) `efficiency_or_related_payoff_outcome`
- **Relevance:** A handful report efficiency, group payoff, or welfare as primary outcomes (`exact`). Several others report only non-payoff behavioral outcomes (e.g., contribution rates, norm compliance), while others are theory papers with payoff-relevant mechanisms, but not payoff measures per se.
- **Label spread:** Some: `exact`; Several: `adjacent` or `close`; Many: `none`.

**Summary:** While there is a core of papers with strong task relevance—i.e., empirical PGGs with explicit efficiency and punishment outcome reporting—much of the paper set provides only indirect or contextual evidence for the downstream prediction task.

# 3) Outcomes Measured In The Literature

## a) **Payoff-related outcomes (efficiency, group payoff, surplus, welfare)**
- **Direct reporting:** Only a subset of experimental papers (e.g., Chen, 2022; Karakostas et al., 2023; Falvey et al., 2025) and theory work (Dughera, 2022; Sugaya & Wolitzky, 2023) directly study group efficiency or comparable payoffs.
- **Treatment inclusion:** Only a limited number report these outcomes for both punishment-enabled and control conditions.
- **Measurement style:** Typically, efficiency is operationalized as the group’s actual earnings divided by the maximum possible (full cooperation) in each treatment.

## b) **Non-payoff behavioral outcomes**
- **Very common:** Most experiments report contribution rates, cooperation frequencies, norm compliance, or related behavioral measures.
- **Punishment focus:** Some papers analyze punishment frequency, monitoring, type of norm violation, or use of sanctioning, but do not report the downstream impact on group payoff.
- **Important distinction:** Many papers find increased contributions with punishment but do not analyze or report whether these translate into efficiency gains, especially after accounting for punishment costs.

# 4) Main Findings Relevant To Prediction

## a) **Empirical papers with direct efficiency outcomes in PGG + punishment**
- **Chen (2022):** In heterogeneous MPCR PGGs, enabling punishment does **not** increase efficiency or average earnings; punishment often destroys resources, and efficiency can be flat or decrease relative to control. Reward opportunities prove much more effective.
- **Karakostas et al. (2023):** Mechanisms that allow for redistribution/sanctions (team allocator) can increase efficiency in linear PGGs, but may reduce efficiency in 'best-shot' and are neutral in 'weakest-link' games. Efficiency improvement depends heavily on underlying production technology and the ability to sanction/reward via allocation rather than costly punishment.
- **Falvey et al. (2025):** Mechanisms that link allocations to contributions (Galbraith Mechanism) substantially boost efficiency. However, this increase results from endogenous positive/negative incentives at zero explicit cost, which isn't identical to classic costly peer punishment.

## b) **Theoretical guidance**
- **Dughera (2022):** In teams, punishment can increase efficiency when monitoring is efficient and skill is low but is less efficient than reward/motivation regimes; outcomes are highly conditional on design parameters (monitoring, skills, charisma).
- **Sugaya & Wolitzky (2023):** High efficiency in large repeated games with bad-apple types requires targeted, involuntary punishment. Reward or voluntary mechanisms do not prevent efficiency collapse when group size is large with some defectors.
- **Wang et al. (2023):** Tax-based (institutional) punishment/reward mechanisms are needed for sustained cooperation; peer punishment alone is insufficient in well-mixed populations.

## c) **Papers with only adjacent, indirect, or negative findings**
- **Kingsley & Smith-Walter (2024):** Punishment increases *contributions* (not group efficiency); efficiency/payoff not reported.
- **Gallo et al. (2022):** In uncertain, dynamic network settings, punishment via link removal is less effective and group efficiency declines under noise; effects are sensitive to reputational accuracy.
- **Büyükboyaci et al. (2025):** Distributive punishment (reduced giving to non-cooperators) does not feed back to increased productive effort or efficiency.

## d) **Common mechanism findings**
- Resource-destroying punishment can lower (not raise) efficiency.
- Efficiency effects of punishment are highly context-dependent: depends on group heterogeneity, monitoring accuracy, presence of bad-apple types, and the cost/technology of punishment.
- Mechanisms that *reward* contributions or allow positive allocation are often more effective than those that rely on costly punishment.

# 5) Prediction Guidance

Based on this literature, the following points should inform prediction of efficiency in punishment-enabled PGGs, conditional on game design and control efficiency:

- **Do not expect a universal efficiency boost from punishment:** Several papers, especially with heterogeneous groups or high punishment costs, show **no improvement or even a decrease** in efficiency when enabling punishment versus control. This is often due to resource destruction from punishment, misuse (e.g., anti-social punishment), or the absence of strategic motivation for low-benefit members (Chen, 2022).
  
- **Mechanisms matter:** If the "punishment" is not costly resource destruction but instead is implemented through endogenous allocation or costless sanctions, efficiency can improve (Karakostas et al., 2023; Falvey et al., 2025), but such mechanisms are not equivalent to standard peer punishment (punisher's coins spent to destroy a target's payoff).
  
- **Production technology is key:** In standard, linear PGGs with targeted, efficient punishment and symmetric groups, theory predicts that punishment can sustain high efficiency (Sugaya & Wolitzky, 2023), but only when defectors can be reliably targeted and the problem of anti-social punishment or group heterogeneity is controlled.
  
- **High monitoring noise or weak targeting:** In environments with reputational uncertainty or inability to distinguish defectors, punishment is much less effective or can backfire by reducing efficiency (Gallo et al., 2022).

- **Rewards are often superior:** Where tested, reward mechanisms frequently outperform punishment in generating efficiency (Chen, 2022; Wang et al., 2023).

- **Group size and bad-apple risk:** In large groups, lack of targeted, involuntary punishment leads to efficiency collapse in the presence of even a few defectors (Sugaya & Wolitzky, 2023).

Thus, **for prediction tasks**, direct mapping from control efficiency to treatment efficiency when enabling punishment depends crucially on:
- Whether punishment is peer-based and costly (expect flat or reduced efficiency unless group is symmetric, punishment is well-targeted, and antisocial punishment is limited);
- The production technology (linear PGGs allow positive effects under some conditions, while heterogeneous, best-shot, or weakest-link games may see no gain or a loss);
- The monitoring/punishment technology (precision, transparency, cost);
- Potential for anti-social punishment or strategic misuse.

# 6) Design Dimensions Highlighted Across Papers

### **Directly informed:**
- `player_count`: Frequently manipulated and analyzed as a moderator of efficiency/punishment effect (e.g., Sugaya & Wolitzky, 2023).
- `num_rounds`: Many papers use repeated games with various round numbers.
- `mpcr`: Explicitly explored as a key parameter in multiple studies (Chen, 2022; Falvey et al., 2025; Ball et al., 2025), with strong payoff and efficiency implications.
- `punishment_cost`: Directly manipulated in several empirical and theory papers.
- `punishment_tech`: Theoretical and experimental focus on precision, targeting, and punishment implementation.
- `all_or_nothing`: Explored in some (Ball et al., 2025; Camera et al., 2025).
- `chat`: Occasional moderator in studies on communication and punishment (Hajikhameneh & Iannaccone, 2023).
- `reward_exists`: Examined as an alternative/complementary mechanism to punishment (Chen, 2022; Wang et al., 2023).
- `show_n_rounds`: Sometimes manipulated.

### **Indirectly informed/contextually discussed:**
- `default_contrib`: Occasionally mentioned in framing/manipulation.
- `show_other_summaries`, `show_punishment_id`: Inferrable in some studies but not systematically examined as moderators of efficiency effects.
- `reward_cost`, `reward_tech`: Far less often manipulated; more often contextually described.

### **Effectively missing:**
- Several dimensions are not systematically varied or connected to efficiency effects of punishment in this literature: `show_punishment_id` (identity revelation is rarely the focus), `default_contrib` (framing often fixed). `reward_cost` and `reward_tech` are largely untested for their marginal interaction with punishment-enabled efficiency.

# 7) Important Limitations

- **Sparse direct evidence:** Very few papers present the head-to-head comparison of control (no punishment) versus peer punishment on efficiency, controlling for all game dimensions of interest. Most results are context-dependent, narrowly framed, or limited in sample.
- **Confounding mechanisms:** Some "punishment" treatments involve endogenous allocation, automatic penalties, or coalition exclusion instead of canonical costly peer punishment, reducing comparability.
- **Over-reliance on contribution as proxy:** Many studies solely report contribution rates or behavioral outcomes—these do not necessarily translate into efficiency improvements, especially once punishment costs are considered.
- **Limited dimensional coverage:** Not all 14 design dimensions are systematically or simultaneously tested.
- **Ambiguity in group heterogeneity:** When group benefit (e.g., MPCR) is heterogeneous, findings suggest punishment can be ineffective or even counterproductive, but this does not generalize to all settings.
- **Lack of field or naturally occurring group evidence:** Most evidence is from controlled lab experiments with short time horizons and induced incentives.
- **Boundary conditions underexplored:** Important moderators (e.g., anti-social punishment rates, monitoring accuracy, social context, norms) are often reported but not modeled for prediction.
- **Disagreement and ambiguity:** Even where efficiency data is reported, some papers report positive, some negative, and many mixed effects, indicating lack of consensus or strong contextual dependence.

---

**In summary:** The available literature provides partial but not comprehensive guidance on predicting the effect of enabling peer punishment on efficiency in PGG-like environments. Direct evidence is strongest for standard linear PGGs with symmetric groups and well-implemented, precise punishment. Key moderators are group size, punishment cost and technology, production function, and group heterogeneity. Predictions outside these settings should be made with caution and an expectation of no systematic efficiency gain, or even a decline, when enabling costly punishment mechanisms.
