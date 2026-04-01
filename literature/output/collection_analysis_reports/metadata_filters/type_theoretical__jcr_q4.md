# 1) Evidence Base

**Breadth and Focus:**  
The paper set consists of 41 theoretical papers; there are no empirical or experimental studies. The collection is *narrow* in the sense that every paper is based in formal models or conceptual reviews—there are no data-based observations. However, it is *broad* in the diversity of social dilemma forms considered: while many models align exactly with public goods games (PGGs), others are based on repeated prisoner’s dilemmas, volunteer’s dilemmas, or related settings. Most studies focus on conceptual mechanisms, possible equilibria, and boundary conditions for cooperation and efficiency, rather than precise quantitative predictions.

**Types of Evidence:**  
- The evidence is almost entirely **theoretical**, making use of evolutionary game theory, agent-based models, analytical derivations, or simulation.
- There is considerable **variation in the closeness** of the modeled environments to real PGGs with peer punishment and to the target prediction environment.

**Coverage of Design Dimensions:**  
- Many game design parameters are investigated (e.g., `player_count`, `mpcr`, `punishment_cost`, `punishment_tech`), especially those central to the sanctioning mechanism.
- Some dimensions (e.g., `chat`, `show_other_summaries`, `show_punishment_id`, `default_contrib`, and reward-related variables) are poorly covered or absent.
- Findings are broadly robust to changes in some parameters but highly sensitive to others (notably punishment cost and mechanism).

**Conclusion:**  
This literature set provides a strong theoretical base, offering robust, qualified statements about **directional effects** of enabling punishment on efficiency in PGG-like games. However, the absence of *empirical calibration*, and limited direct analysis of all design dimensions, mean that prediction using only these sources should be cautious and context-sensitive.

# 2) Task Relevance

- **pgg_or_variant:**
  - **exact**: ~11 papers directly model standard or optional public goods games with canonical features (e.g., (Alventosa & Olcina, 2021); (Carpenter & Matthews, 2010); (Botta et al., 2021); etc.).
  - **close/adjacent**: Many others are based on repeated prisoner’s dilemmas, volunteer’s dilemmas, or other closely related models; these provide **close** or **adjacent** relevance (e.g., (Jones, 1999); (Andersson, 2020)).
  - **weak/none**: Few papers fall below *adjacent* on this dimension.

- **punishment_or_sanctions:**
  - **exact**: Most theoretical models do directly incorporate punishment—either peer, third-party/institutional, or concerted punishment. Some distinguish between altruistic and selfish punishment, and several include both punishment and reward mechanisms.
  - **adjacent/weak**: A minority of models involve mechanisms functionally similar to punishment (e.g., partner switching, walk-away) but not explicit costs/fines; these are *adjacent*.

- **efficiency_or_related_payoff_outcome:**
  - **exact**: About half of the papers analyze group efficiency or total welfare/payoff directly.
  - **close/adjacent/weak/none**: The other half analyze behavioral proxies (e.g., cooperation rates, norm compliance), evolutionary stability, or take efficiency as a background concept without explicit calculation.

**Overall:**  
The **strongest task relevance** occurs where models: (a) are exact or close variants of the PGG, (b) implement explicit, configurable punishment, and (c) track group payoff or efficiency as a primary outcome.

# 3) Outcomes Measured In The Literature

**Payoff/Efficiency Outcomes:**
- Many papers report **group efficiency**, **total welfare**, or **average payoff** as a principal model output (e.g., (Bowles & Gintis, 2004); (Voelkl, 2015); (Ishikawa & Fontanari, 2025)).
- Some models compare outcomes to a full-cooperation benchmark (as in the definition of efficiency for this prediction task).
- Others give **qualitative guidance**—such as whether the equilibrium “approaches the cooperative optimum” or is “higher than the control” (e.g., (Carpenter & Matthews, 2010); (Kendal et al., 2006)).
- A subset only report payoff-adjacent outcomes, such as the feasibility of cooperation, the size of the basin of efficient equilibria, or the impact of mechanism costs.

**Non-payoff Behavioral Outcomes:**
- Many models use **cooperation rate**, **punishment frequency**, or **norm compliance** as outcomes, either because efficiency outcomes are not easily defined within the setup, or for conceptual reasons (e.g., (Zhang & Pei, 2022); (Thöni, 2014)).
- Antisocial punishment, emotional dynamics, and trust are sometimes analyzed for their effect on group dynamics and behavior, without explicit calculation of efficiency.

**Explicit Distinction:**  
Several papers that track non-payoff behavioral outcomes caution that *increases in cooperation or norm compliance do not guarantee increased efficiency*, especially if punishment is costly or misaligned (e.g., (Zhang & Pei, 2022); (Jaffe, 2004)).

# 4) Main Findings Relevant To Prediction

**Consensus and Qualitative Direction:**
- **Most theoretical papers agree:** Enabling *costly punishment* in PGGs or their close variants can, under favorable parameter conditions, **increase group efficiency** by suppressing free-riding and stabilizing cooperation (e.g., (Alventosa & Olcina, 2021); (Carpenter & Matthews, 2010); (Bowles & Gintis, 2004); (Voelkl, 2015)).
- These efficiency gains are **conditional**: They are often largest when (i) the punishment is institutionally supported or concerted, (ii) cost of punishment is not too high relative to the fine or social benefit, and (iii) there are not too many baseline free-riders (initial condition matters).
- For **peer punishment** specifically, several models and reviews warn that costly punishment can incur enough *second-order* or antisocial punishment to **reduce or even reverse efficiency gains** (e.g., (Zhang & Pei, 2022); (Jaffe, 2004); (Thöni, 2014)).

**Important Moderators by Design Dimension:**
- **Player Count/Group Size:** Larger groups can *raise the threshold* needed for punishment to be effective, or reduce the magnitude of efficiency gains if cooperation is hard to coordinate (e.g., (Deng et al., 2012); (Ishikawa & Fontanari, 2025); (Gioffré & Tampieri, 2025)).
- **MPCR (Marginal Per Capita Return):** Higher MPCR generally makes cooperation easier and punishment more likely to stabilize high efficiency (e.g., (Botta et al., 2021); (Gioffré & Tampieri, 2025)).
- **Punishment Cost and Tech:** Lower punishment costs and higher punishment effectiveness (fines, detection probability, severity) increase the positive effect of enabling punishment (e.g., (Deng et al., 2012); (Voelkl, 2015); (Ishikawa & Fontanari, 2025)).
- **Punishment Structure:** *Institutional/centralized* and *concerted* punishments are more likely to yield net-positive efficiency gains than decentralized or peer punishment due to lower costs and less risk of antisocial punishment (e.g., (Alventosa & Olcina, 2021); (Deng et al., 2012); (Kendal et al., 2006)).
- **Reward Exists:** Inclusion of rewards as a complement to punishment can expand the basin of efficient equilibria (e.g., (Kendal et al., 2006)), but rewards alone are rarely as effective unless very large.

**Behavioral Mechanisms and Limitations:**
- *Antisocial punishment*, *selfish punishment*, and power asymmetries can undermine efficiency and, in some models, lower group payoffs below the punishment-disabled baseline (e.g., (Zhang & Pei, 2022); (Eldakar et al., 2018)).
- *Framing and context* (not always explicitly modeled in design dimensions) can substantially affect both cooperation and the efficacy of punishment (e.g., (Hagen & Hammerstein, 2006); (Thöni, 2014)).
- *Voluntary participation* (e.g., “loner” strategy) and *partner choice* can provide alternative paths to high efficiency, sometimes reducing or replacing the need for punishment (e.g., (Botta et al., 2021); (Castro & Toro, 2008)).

# 5) Prediction Guidance

**Best-Supported Prediction:**
- *Enabling (effective) punishment in a PGG or close variant, when compared to a no-punishment control, will generally increase average group efficiency—*especially* if the baseline efficiency is not already high, the punishment is not excessively costly, and if the design avoids conditions promoting antisocial or second-order punishment.*

**Key Moderators (from most to least supported):**
- **Punishment Cost/Effectiveness (`punishment_cost`, `punishment_tech`):** Strong informance; lower-cost, higher-effectiveness punishment predicts larger efficiency gains.
- **MPCR (`mpcr`):** Strong; higher returns to contribution amplify the efficacy of punishment.
- **Group Size (`player_count`) and Institutional Form:** Medium-strong; larger groups and centralized/institutional punishments tend to produce more robust efficiency gains if implementation is feasible.
- **Initial Efficiency Level (control):** Strong; the lower the baseline, the greater the scope for improvement, but if the system is deeply in the all-defection equilibrium, even added punishment may not rescue efficiency (Carpenter & Matthews, 2010).
- **Other Dimensions (less direct):** Evidence on `chat`, `show_punishment_id`, `default_contrib`, etc., is sparse or missing.

**Important Caveats:**
- **Peer Punishment:** Efficiency gains are not guaranteed; costs of punishment, antisocial targeting, or second-order free-riding may make activation of peer punishment *neutral or negative* for efficiency in some environments (Zhang & Pei, 2022; Jaffe, 2004).
- **Path Dependence:** Initial composition (proportion of free-riders vs. punishers) and game history can lock the system in low-efficiency or high-efficiency equilibria (Ishikawa & Fontanari, 2025).
- **Behavioral Complexity:** Psychological factors, such as prospect-theoretic biases (Uchida et al., 2024), may amplify the deterrent impact of even mild punishment, making real-world outcomes more sensitive than static models predict.

**Quantitative Precision:**  
Because outcomes are modeled rather than measured, **quantitative predictions require parametrization** from the specific theory paper most matching the game design in question.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- `player_count`: Extensively modeled. Effects of group size on threshold for, and stability of, efficient cooperation/punishment addressed in many models.
- `num_rounds`: Modeled in repeated games—discount factors, continuation probability, and the effect of feedback over rounds are treated, though perfect mapping to finite rounds is sometimes missing.
- `mpcr`: Core parameter in most models—more cooperative returns make punishment more effective.
- `punishment_cost` & `punishment_tech`: Heavily explored; their ratio is central to predicting efficiency impacts.
- `all_or_nothing`: Modeled as binary participation or contribution in many models.
- `reward_exists`, `reward_cost`, `reward_tech`: Treated in a subset of models focusing specifically on reward vs. punishment trade-offs.
- `punishment_exists`: All models concerning punishment assume variation in its presence/absence.

**Indirectly or Contextually Informed Dimensions:**
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Sometimes mentioned or present in the environment structure, but *not* usually manipulated.
- `default_contrib`: Framing (opt-in/opt-out) is essentially absent from formal analysis.

**Missing or Weakly Covered Dimensions:**
- `chat`: Only a couple of papers mention communication.
- `show_punishment_id`: Not explicitly parameterized.
- `show_other_summaries`: Occurs in some repeated-matching games, but never manipulated systematically.

**Conclusion:**  
Prediction can be most confidently anchored on:  
`player_count`, `num_rounds`, `all_or_nothing`, `mpcr`, `punishment_cost`, `punishment_tech`, and (where applicable) `reward_exists`, `reward_cost`, and `reward_tech`.

# 7) Important Limitations

- **All Theoretical Modeling:** There are no empirical or laboratory studies in this set; as such, all quantitative guidance is subject to the realism of model assumptions and parameterizations.
- **Limited Empirical Calibration:** No data to indicate effect sizes, noise, participants’ actual expectations, or behavioral pathologies that can arise in real settings.
- **Parameter Range Sensitivity:** Some models show “knife-edge” conditions—small changes in cost/benefit, punishment effectiveness, or player composition can shift equilibrium from full efficiency to full defection or vice versa (e.g., (Carpenter & Matthews, 2010); (Ishikawa & Fontanari, 2025)).
- **Sparse Coverage of Social and Informational Context:** Communication (`chat`), punishment transparency (`show_punishment_id`), and summary visibility are barely treated; these are often important in experimental or field results.
- **Antisocial and Second-Order Effects:** A subset of models and reviews caution that efficiently calibrating prediction requires knowing whether peer punishment will be prosocial, antisocial, or lead to costly contestation (Zhang & Pei, 2022; Thöni, 2014).
- **No Direct Guidance for Some Design Dimensions:** Some parameters in the 14-dimension set are essentially unmapped by this evidence base; predictions should explicitly flag these as sources of model uncertainty.
- **No Nuanced Demographics or Behavioral Heterogeneity:** Real human players may react differently to punishment, depending on psychology, cultural background, or even perception of fairness—factors modeled only abstractly.

**Summary Limitation:**  
This literature supports *directional* and *mechanistic* prediction—enabling punishment will usually increase efficiency in theory-driven PGGs. But context, exact design, baseline efficiency, and the risk of unintended punishment dynamics must all be considered, and predictions should be treated as *qualitative hypotheses* unless a close theoretical analog exists. Quantitative, design-dimension-aware prediction requires empirical calibration not present in this paper set.
