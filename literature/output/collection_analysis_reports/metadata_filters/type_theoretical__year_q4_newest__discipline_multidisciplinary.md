# 1) Evidence Base

This paper set consists exclusively of theoretical and simulation-based studies (no empirical or experimental primary data) with a primary focus on agent-based models, analytic equilibrium analysis, and evolutionary game theory. The majority directly address public goods games (PGGs) or close variants, with models varying from canonical PGGs with peer/pool punishment to institutional mechanisms, division-of-labor frameworks, dynamic resources, and trust/lending games. Very few empirical validations are present, though some agent-based simulations replicate or are calibrated against prior experimental findings (e.g., Bühren et al., 2023).

The evidence base is conceptually broad within the domain of game-theoretic and evolutionary modeling, offering a rich set of mechanistic insights covering a wide range of design dimensions. Importantly, many studies directly model or discuss efficiency or group payoff outcomes, providing direct relevance for prediction tasks focused on payoff-based efficiency. A smaller subset discusses only behavioral outcomes (e.g., cooperation rates, strategy frequencies) or indirect payoff proxies, which must be carefully separated in synthesis.

# 2) Task Relevance

- **pgg_or_variant:**  
  The set contains **many papers of exact relevance** (canonical PGG or close analytic equivalents) as well as several on threshold public goods, common-pool resource games, division-of-labor, structured trust or lending games, and dyadic dilemmas with institutional punishment. For forecasting efficiency under peer punishment specifically, the most relevant are those modeling standard or slightly adapted PGGs with peer or pool punishment (e.g., Bühren et al. 2023; Zefferman 2023; Wang et al. 2024; Botta et al. 2024).

  **Labels:**
  - PGG: majority "exact" or "close"
  - Some papers: "adjacent" or "weak" (when only behavioral or resource sustainability outcomes are reported)

- **punishment_or_sanctions:**  
  The **central theme** is the modeling of punishment and/or sanctions, mostly peer punishment, pool punishment, third-party or institutional punishment, and hybrid/complex institutions (with some reward comparison).  
  **Labels:**  
  - Punishment: nearly all "exact" or "close" (peer/pool/institutional mechanisms explicitly modeled), with a handful "adjacent" (e.g., only norm-based or indirect exclusion), and a few "none" for baselines without punishment.

- **efficiency_or_related_payoff_outcome:**  
  A significant subset of papers reports **efficiency** or payoff (group surplus, total earnings, welfare), directly supporting the prediction task. Some consider only behavioral outcomes (e.g., cooperation rates, frequencies), which are not equivalent and must be flagged.
  **Labels:**
  - Efficiency: many "exact" or "close" (explicit efficiency/payoff models)
  - Behavioral only: "adjacent" or "weak"

# 3) Outcomes Measured In The Literature

- **Payoff-Based Outcomes (relevant for efficiency prediction):**
    - *Efficiency*: Directly measured or calculated in many studies as group payoff relative to the full-cooperation maximum (e.g., Bühren et al., Zefferman, Wang et al., Botta et al.).
    - *Total group payoff, welfare, surplus, accumulated wealth, η_G*: Used interchangeably in 'payoff-exact' contexts.
    - *Resource abundance*: In common-pool resource games, as a proxy for group welfare/efficiency.

- **Non-Payoff Behavioral Outcomes:**
    - *Cooperation/contribution rate*: Proportion of group contributing.
    - *Strategy frequencies*: Fraction of cooperators, defectors, punishers, etc.
    - *Norm compliance, convergence to cooperation, stability of cooperators/punishers*: Often used in evolutionary settings.
    - *Oscillatory/chaotic dynamics*: When focus is on population or resource dynamics.

**Distinction:**  
Outcomes limited to cooperation rates or behavioral propensities do not map directly to efficiency, as high cooperation can sometimes entail high punishment costs that offset efficiency gains or even reduce payoffs (explicitly shown in, e.g., Han et al., 2024).

# 4) Main Findings Relevant To Prediction

Synthesizing across exact and close PGGs with modeled efficiency outcomes:

### General Effects of Enabling Punishment

- **Punishment can raise efficiency if**
    - Punishment is *cost-effective* (low cost to punisher, high impact on punished: Zefferman 2023; Wang et al. 2024; Botta et al. 2024).
    - Group’s *baseline cooperativeness* is low and coordination on full cooperation is otherwise difficult (Bühren et al. 2023).
    - Monitoring/detection is reliable and not excessively costly (Zefferman 2023; Botta et al. 2024).
    - Punishment parameters (severity, probability, scope) are tuned above critical thresholds (Wang et al. 2024; Ohdaira 2022; Nirjhor & Nakamaru 2023a/b).

- **Punishment can reduce or fail to improve efficiency if**
    - Punishment cost is high relative to its deterrent effect, leading to wasted resources on punishment or retaliatory cycles (Bühren et al. 2023; Han et al., 2024).
    - Social preference structure already supports high cooperation; then, punishment cost outweighs marginal cooperative gains (Bühren et al. 2023).
    - Group/monitoring structure makes universal or well-targeted punishment infeasible (e.g., large groups, costly monitoring: Zefferman 2023).
    - Conditional defectors evade punishment or punishment is easily sidestepped (Ibrahim 2022).

- **Form and governance of punishment matters:**
    - Institutional or third-party mechanisms can outperform or fill gaps where peer punishment is weak (Mohlin et al. 2023; Lie-Panis et al. 2024).
    - Institutions which can choose between punishment and reward (or optimally mix them) obtain superior efficiency (Garrido et al. 2025; Zhou & Li 2022; Han 2022).
    - Flexible, context-dependent punishment (rather than fixed bare-cost peer punishment) yields more robust and higher efficiency (Ohdaira 2022; Botta et al. 2024).

- **Reward mechanisms generally outperform punishment:**
    - When compared, reward is more likely to increase efficiency; punishment often raises cooperation but at greater cost (Han et al., 2024; Chiba-Okabe & Plotkin 2024).

- **Role of game structure, population and network:**
    - Structured (not well-mixed) populations facilitate larger efficiency gains from punishment if coordination and monitoring are possible (Wang et al. 2024; Botta et al. 2024).
    - Larger groups require more efficient punishment/monitoring to achieve the same effect, scaling with cost and structure (Zefferman 2023).
    - Full monitoring/compulsion is rarely realistic; partial monitoring with moderate punishment can achieve similar effects if well-calibrated (Botta et al. 2024).

- **Moderation, nonlinearities and context-dependence:**
    - Effects are *non-monotonic*; too little punishment is costly and ineffective, too much is wasteful or counterproductive (Bühren et al. 2023; Jia & Wang 2025).
    - Population heterogeneity (social preferences, patience), interaction structure, and strategic sophistication moderate the efficiency gains from punishment (Bühren et al. 2023; Lie-Panis et al. 2024).
    - Environment/context: Ecological feedbacks, resource growth rates, or the presence of institutional objectives (selfish vs. prosocial) can invert efficacy (Sarkar 2023; Chiba-Okabe & Plotkin 2024).

# 5) Prediction Guidance

## How This Literature Should Inform Efficiency Prediction

### When Payoff/Efficiency is Directly Modeled

1. **In PGGs with baseline low efficiency and low-cost, highly effective punishment enabled:**
    - Predict a substantial increase in efficiency (potentially toward social optimum), *if punishment cost/effect ratio is high* (Zefferman 2023; Wang et al. 2024; Botta et al. 2024; Nirjhor & Nakamaru 2023a/b; Mohlin et al. 2023).
    - Use critical threshold formulas (as in Wang et al. 2024; Nirjhor & Nakamaru 2023a/b) relating punishment cost/magnitude, player count, and MPCR to detect whether group is above/below threshold for efficiency gain.

2. **In PGGs with high baseline efficiency or high-cooperative/strong-norm groups:**
    - Expect marginal or *negative efficiency gain* from punishment: cost of punishment outweighs small increases in cooperation (Bühren et al. 2023).

3. **If punishment is not cost-effective, monitoring is weak, or group size is large:**
    - Expect *no improvement or even reduced efficiency* compared to control, due to cost drag and ineffectiveness (Han et al., 2024; Zefferman 2023).

4. **If institutions allow both punishment and reward or adaptive institutional choice:**
    - Predict efficiency at or above the maximum of single-mechanism regimes, especially in bottom-up or locally adaptive systems (Garrido et al. 2025; Zhou & Li 2022).

5. **Continuous-choice PGGs:**  
    - Punishment is often not sufficient to stabilize high cooperation, unless augmented by additional mechanisms (Yan et al. 2023).

### When Only Behavioral Outcomes are Reported

- Increased cooperation rates imply—but do not guarantee—increased efficiency; gains can be offset fully (or more) by the cost of widespread punishment (Han et al., 2024; Bühren et al. 2023).
- Use effect direction (increase/no change/decrease in cooperation) as a *non-binding prior* on efficiency, but do not impute quantitative payoffs unless payoff impact of punishment is assessed.

### Broader Context and Limits

- The effect of enabling punishment is not universally positive; cost-effectiveness, institutional design, and baseline efficiency must be considered.
- When the control (no-punishment) efficiency is already high, added punishment is likely wasteful, reducing efficiency.
- Contextual moderators, such as group structure, monitoring ability, and institution objectives, can reverse or strongly moderate the efficiency effect.

### Control Efficiency as a Moderator

- If the control game has high efficiency (i.e., baseline cooperation is already strong), the marginal benefit of enabling punishment is typically low or negative (Bühren et al. 2023; Lie-Panis et al. 2024).
- If the control game is inefficient, and design parameters favor cost-effective punishment, the efficiency lift due to punishment can be large (Botta et al. 2024; Wang et al. 2024).

# 6) Design Dimensions Highlighted Across Papers

## Directly Informed Dimensions

- **player_count**: Extensively modeled; larger groups reduce punishment effectiveness unless punishment/monitoring scale efficiently (Zefferman 2023; Wang et al. 2024; Botta et al. 2024; Nirjhor & Nakamaru 2023a/b).
- **num_rounds**: Modeled as infinite/long-run in most theory; finite effects in agent-based simulation; more rounds typically facilitate institutional/altruistic evolution.
- **all_or_nothing**: Both continuous and binary (all-or-nothing) PGGs are represented; evidence for both.
- **mpcr**: Central moderator; higher MPCR typically facilitates cooperation and reduces need for extreme punishment (Zefferman 2023; Wang et al. 2024).
- **punishment_cost**, **punishment_tech (magnitude, probability, institution type)**: Core focus in nearly all punishment-oriented papers; cost-effectiveness threshold is a central prediction ingredient (Bühren et al. 2023; Wang et al. 2024; Ohdaira 2022; Botta et al. 2024).
- **reward_exists**, **reward_cost/tech**: Well-represented in papers contrasting punishment and reward or hybrid institutions (Garrido et al. 2025; Zhou & Li 2022; Han 2022).

## Indirectly/Occasionally Informed or Contextually Discussed

- **chat**: Rarely modeled; most studies do not consider communication.
- **default_contrib**: Rarely discussed; some mention framing/initial cooperation as a moderator.
- **show_n_rounds**/**show_other_summaries**/**show_punishment_id**: Indirectly referenced in papers on transparency, monitoring structure, or reputation (Pal & Hilbe 2022; Lie-Panis et al. 2024).
- **reward_exists**: Discussed in mixed-institution and comparison studies.

## Effectively Missing or Very Limited

- **chat**, **default_contrib**: Most theories omit direct modeling of communication or default framing.
- **show_punishment_id**, **show_n_rounds**, **show_other_summaries**: These information/framing variables are often absent or only contextually mentioned as part of reputation/monitoring design.

# 7) Important Limitations

- **Absence of empirical/experimental studies**: Nearly all findings are theoretical or simulation-based; real-world behavioral variation, bounded rationality, and implementation frictions may not be captured (exceptions: Bühren et al. 2023 simulation is calibrated to experimental data).

- **Overemphasis on idealized monitoring and implementation**: Many models assume perfect or stylized monitoring, instantaneous and accurate punishment, or infinite rounds, limiting generalizability to real-world or lab settings.

- **Simplified or restricted strategy spaces**: Several models restrict punishers, antisocial punishment, or role assignment, which may overestimate the positive effect of punishment (García & Traulsen 2025).

- **Bias toward strong parametric effects**: Most results focus on regimes where punishment reliably enforces cooperation or not, possibly underplaying moderate, non-equilibrium, or noisy real-world settings.

- **Sparse evidence for nuanced design dimensions**: Variables such as chat, information display, default framing, and dynamic institution choice are rarely modeled, limiting dimension-specific prediction.

- **Ambiguity in outcome mapping**: Many studies report behavioral increases in cooperation or norm compliance, which *may not* translate directly to payoff gains, especially when punishment is costly or when cooperation is already high.

- **Adjacent-context results**: Several included studies model division-of-labor, resource feedback, trust/lending, or dyadic dilemmas, which are close but not canonically PGG, thus requiring caution in transfer to strict PGG prediction.

- **No direct variance/uncertainty quantification**: The theory models provide sharp thresholds or directional predictions but rarely address the variance in outcomes expected under real-world parameter uncertainty or heterogeneity.

---

**In summary:**  
This literature provides strong theoretical and simulation-based guidance for predicting the effect of punishment on efficiency in PGG-like environments when design dimensions and control efficiency are known. Prediction should carefully weight the cost-effectiveness of punishment, the baseline efficiency, and key game design features (player count, MPCR, punishment parameters), while avoiding over-reliance on behavioral outcomes not mapped to payoffs. Design dimensions such as chat, information framing, and default contributions are underrepresented, limiting granularity in predictions along these axes. The task is further limited by the lack of empirical validation and simplified modeling assumptions.
