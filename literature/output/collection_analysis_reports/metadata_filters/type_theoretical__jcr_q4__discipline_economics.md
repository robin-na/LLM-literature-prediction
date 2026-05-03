# 1) Evidence Base

This literature set consists entirely of theory papers with no direct empirical or experimental studies. All 23 papers are modeling or theoretical, spanning a mix of direct public goods games (PGGs), closely related social dilemma environments (such as repeated Prisoner’s Dilemma, volunteer’s dilemma, and donation/stag-hunt games), and broader theory on punishment, reward, and cooperation mechanisms. The set is relatively broad in the context of theoretical treatments of punishment and efficiency but contains only a handful of PGG-exact analyses directly modeling the switch from no-punishment to enabled-punishment treatments with explicit efficiency or payoff outcomes. Nevertheless, several papers offer highly structured guidance on game design dimension moderators. There is a heavy tilt toward analyzing under what structural or parametric conditions punishment can, in theory, induce higher group payoff (efficiency), with numerous boundary condition results, but little in terms of direct empirical magnitude estimates.

# 2) Task Relevance

**pgg_or_variant:**  
- *Exact relevance*: Seven papers model true PGGs or their closest variants with group production functions, including the effect of punishment (Alventosa & Olcina, 2021; Carpenter & Matthews, 2010; Botta et al., 2021; Thöni, 2014; Spitzer, 2016; Bolle, 2021; Friehe & Tabbach, 2018).  
- *Close/adjacent relevance*: Many use adjacent games—repeated Prisoner’s Dilemma, volunteer’s dilemma, donation or coordination games—that are not PGGs but share key features (e.g., collective action, dilemma structure).
- *Weak/none*: Some (esp. trust games, games without any sanctioning) are only contextually relevant.

**punishment_or_sanctions:**  
- *Exact relevance*: Most papers directly address punishment or sanctioning as a mechanism (either peer, centralized, or community/endogenous).  
- *Adjacent/weak*: Some address only reward, communication, or norm enforcement mechanisms without explicit punishment (e.g., reward-only or norm compliance).
- *None*: A small subset does not include punishment.

**efficiency_or_related_payoff_outcome:**  
- *Exact relevance*: About half explicitly model or discuss group efficiency, welfare, or total group payoff as primary outcomes of interest.
- *Adjacent*: Several only report on related behavioral outcomes (e.g., cooperation rate, norm adherence) and discuss efficiency only as an implication.
- *None*: A minority focus solely on norm compliance or signaling/psychological variables without any quantification of group payoff.

# 3) Outcomes Measured In The Literature

- **Payoff-based outcomes** (efficiency, welfare, group/average payoff): Addressed directly in about ten theoretical papers (e.g., Alventosa & Olcina, 2021; Carpenter & Matthews, 2010; Botta et al., 2021; Gioffré & Tampieri, 2025; Friehe & Tabbach, 2018).
- **Non-payoff behavioral outcomes** (contribution rate, cooperation frequency, norm compliance, punishment frequency, communication): Discussed in most papers, especially those focusing on mechanisms or psychological explanations rather than efficiency per se.
- **Reward and communication outcomes**: Some address coordination, emotional signaling, or endogenous reward mechanisms as alternatives or moderators.
- **Distinction**: Only the exact-efficiency papers allow direct inference about treatment efficiency; others require careful translation or cannot be used for quantitative downstream prediction.

# 4) Main Findings Relevant To Prediction

## Synthesis of Cross-Paper Findings

- **Peer/centralized punishment generally increases efficiency**, sometimes dramatically, by making cooperation or contribution incentive-compatible (Alventosa & Olcina, 2021; Carpenter & Matthews, 2010; Botta et al., 2021; Gioffré & Tampieri, 2025). High punishment effectiveness (i.e., the expected fine times detection probability) and low punishment cost to the group maximize efficiency gains.
    - *Boundary conditions*: If the punishment is too weak, too costly, or antisocial punishment is prevalent, the gains are muted or may even reverse (Thöni, 2014).
    - *Dependence on initial conditions*: If baseline cooperation is very low (e.g., high initial free-rider prevalence), punishment may fail to rescue group efficiency (Carpenter & Matthews, 2010).
- **Game parameters modulate the effect**:
    - Higher marginal per-capita return (MPCR) generally makes cooperation more easily sustainble; lower MPCR environments rely more on punishment to achieve efficiency (Alventosa & Olcina, 2021; Botta et al., 2021).
    - The effect of group size (player_count) is captured but less frequently analyzed as a moderator of the magnitude of efficiency gain from punishment.
    - In repeated games, the number of rounds and discount factor (patience) are critical: longer horizons/patience make punishment more effective in supporting cooperation equilibrium (Jones, 1999; Blonski & Spagnolo, 2015).
- **Centralized (institutional) punishment outperforms exclusively peer-to-peer (third-party) mechanisms** for sustaining high efficiency, but effectiveness is context-sensitive to institutional design and wealth distribution (Alventosa & Olcina, 2021; Carpenter & Matthews, 2010).
- **Fractional/random punishment coverage can yield large efficiency gains while lowering punishment costs**, provided the coverage fraction surpasses a critical threshold unique to the game’s parameters (Botta et al., 2021).
- **Psychological and social moderators (prospect theory, emotion, information structure, norm signaling, communication)** shift effectiveness:
    - Prospect-theoretic agents overweight small probabilities of being punished; thus, even mild/infrequent punishment can yield efficiency gains (Uchida et al., 2024).
    - Availability of communication or reward can substitute for or diminish the role of costly punishment (Golman, 2016; Spitzer, 2016).
- **Punishment design details (cost, tech, identity visibility, scope, process)** sharply moderate efficacy, as small structural differences yield large outcome differences (Spitzer, 2016; Friehe & Tabbach, 2018).
- **Partial group or class-targeted punishment can generate efficiency, but government type or implementation incentives can cause over- or underapplication, affecting efficiency** (Alventosa & Olcina, 2021).
- **Antisocial punishment (punishment of cooperators) is detrimental to efficiency** (Thöni, 2014); environments prone to this can see reduced or negative efficiency gains.

# 5) Prediction Guidance

- **Directly supported prediction**: *Enabling peer or centralized punishment in a PGG environment is expected, under most theoretically typical parameterizations, to increase group efficiency relative to the no-punishment control*, especially if the baseline efficiency is low due to free-riding, and the punishment mechanism is strong, not too costly, and not prone to antisocial punishment.
    - The gain is most robust where MPCR is moderate to high, punishment effectiveness > threshold, and group/subject pool factors do not trigger antisocial punishment.
    - If control efficiency is already high, incremental gains are likely smaller, and in some cases adding punishment may be unnecessary or counterproductive (e.g., potential for norm overenforcement or crowd-out of intrinsic motivation).
- **Quantitative calibration is limited:** The set provides strong qualitative directionality/moderator guidance but no empirical quantification of expected efficiency increases. The impact of each design dimension is well-stylelized theoretically but not empirically mapped for real-world prediction tasks.
- **Design feature sensitivity is high:** Small changes to punishment cost or process, contribution mechanism (all-or-nothing vs. continuous), group size, MPCR, or information structure (visibility, chat, reward availability) can produce nonlinear changes in the effect of punishment on efficiency.
- **Control efficiency as a predictor:** If the baseline (no-punishment) game already produces high efficiency, the marginal gain from punishment is likely to be minimal or even negative (due to punishment costs and possible norm crowd-out). If baseline efficiency is low, large positive shifts are theoretically possible, contingent on strong enough and well-designed punishment intervention.

# 6) Design Dimensions Highlighted Across Papers

The 14 prediction task design dimensions are covered unevenly:

- **Directly informed (explicitly modeled in efficiency prediction):**
    - `player_count`: Discussed in most core theory (affecting threshold, equilibrium stability).
    - `num_rounds`: Repeated games are analyzed in detail for equilibrium predictions.
    - `all_or_nothing`: Several models use binary (contribute/defect) formats.
    - `mpcr`: Universally treated as a key moderator of incentive structure and efficiency outcome.
    - `punishment_cost`, `punishment_tech` (effectiveness, coverage, targeting): Central to nearly all relevant theoretical models.
- **Indirectly informed (parameters affect outcomes but not always parameterized precisely):**
    - `show_other_summaries`, `show_n_rounds`: Some consideration, especially for repeated games with information structure (important for supporting enforcement/punishment credibility).
    - `reward_exists`, `reward_cost`, `reward_tech`: Addressed, but mainly as moderators or in studies where alternative incentives (rewards) act as substitutes or complements to punishment.
    - `default_contrib`: Rarely treated except where framing effects matter.
    - `chat`: Explored as a communication channel that interacts with or substitutes for costly punishment, but not always parameterized.
    - `show_punishment_id`: Occasionally considered as group observability or anonymity; generally identified as important but not modeled in payoff function.
- **Contextually discussed / sparse:**
    - `default_contrib`, `show_punishment_id`, and detailed implementation features (subject pool, cultural context) are sometimes noted as important in predicting deviations or antisocial punishment but lack formal parametric mapping.
- **Effectively missing in this set:**
    - No direct empirical data on *how much* efficiency changes with parameter variation or real-world noise/heterogeneity.
    - No direct treatment of hybrid/complex institutional structures (combinations of rewards, punishments, communication, endogenous institutional choice).

# 7) Important Limitations

- **All results are theoretical:** Predictions are based on equilibrium, boundary condition, or dynamic stability arguments—not on empirical observation of actual efficiency changes.
- **Parameter sensitivity may limit generalizability:** The realized effect of punishment on group efficiency is highly sensitive to specific game and punishment design features. Many theory models treat only a subset of dimensions at a time.
- **Payoff outcomes often assumed, not measured:** Where models do not output explicit efficiency numbers but only equilibrium existence/structure, there is ambiguity about practical effect sizes.
- **Behavioral and informational nuances (antisocial punishment, crowd-out, prospect theory effects, misimplementation, subject pool, and psychological context) are flagged as critical moderators, but there is little quantification for integrating such effects into a numerical prediction or automated forecast.
- **Empirical calibration is unavailable:** There are no direct experimental estimates or parameter-bound interaction effects to guide how to weigh control efficiency when predicting the efficiency of the treatment (punishment) condition—only theoretical directionality.
- **Some mechanisms are only adjacent/analogous:** Results from repeated PD, volunteer’s dilemma, and other social dilemmas may not perfectly transfer to multi-agent, continuous-contribution PGGs, especially regarding group-level structural phenomena.

---

**In summary:**  
The literature supports a strong theoretical expectation that enabling appropriately designed punishment increases the efficiency of public-goods-like games, contingent on design details and context; however, quantitative, empirical, and dimension-specific mapping is unavailable. Predictions must therefore be based on structural theoretical understanding and moderator identification, not on empirically grounded effect sizes.
