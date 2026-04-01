# 1) Evidence Base

The paper set comprises three empirical, experimental studies spanning artificial agent simulations and lab experiments. All papers study repeated social dilemma environments, primarily variants of the Prisoner’s Dilemma or dyadic cooperative exchanges, rather than canonical public goods games (PGGs). Only one paper (Dasgupta & Musolesi, 2025) directly measures efficiency or payoff outcomes, and does so in a multi-agent reinforcement learning (MARL) environment closely related to the Iterated Prisoner's Dilemma (IPD). The other papers focus on behavioral strategies (Chen & Hauser, 2005) and perceived reputational effects (Ashlock et al., 1996), not actual group efficiency or welfare payoffs. Overall, the evidence base is empirical but relatively narrow and only *adjacently* covers the exact prediction context (PGG efficiency under peer punishment).

# 2) Task Relevance

**PGG or variant:** All papers are `adjacent` to the prediction context, dealing primarily with repeated Prisoner's Dilemma or non-standard repeated cooperation games; none focus on PGGs per se.

**Punishment or sanctions:** All papers are relevant: Dasgupta & Musolesi (2025) and Ashlock et al. (1996) are `exact`, explicitly manipulating direct punishment; Chen & Hauser (2005) is `adjacent`, examining punishing cooperative strategies.

**Efficiency or related payoff outcome:** Only Dasgupta & Musolesi (2025) is `exact`, directly reporting group efficiency as a function of punishment. Ashlock et al. (1996) is `weak`, focusing on reputational and perceptual outcomes, not payoffs. Chen & Hauser (2005) is `adjacent`: it analyzes behavioral cooperation stabilized by punishment, but does not report payoff- or efficiency-based outcomes.

**Summary:** The set has limited direct relevance to the downstream prediction task: only one paper measures efficiency, and none do so in true PGG settings.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:** Only Dasgupta & Musolesi (2025) directly measure group efficiency (total group reward versus optimal possible reward), matching the prediction outcome.  
- **Behavioral outcomes:**  
    - Ashlock et al. (1996): Measures reputational perceptions and partner preferences related to punishment and withdrawal.  
    - Chen & Hauser (2005): Measures behavioral strategy prevalence and model fits for punishing versus forgiving reciprocity in primate games.
- **Distinction:** Only one study reports efficiency; the others focus entirely on non-payoff behavioral phenomena.

# 4) Main Findings Relevant To Prediction

The primary relevant empirical finding is from Dasgupta & Musolesi (2025):  
- **Direct, net-rewarding punishment increases efficiency:** When just punishment is net-rewarding (i.e., the cost of sanctioning is outweighed by its downstream cooperative benefits), enabling peer punishment leads to higher group efficiency compared to no-punishment controls.  
- **Mechanism for efficiency loss:** Third-party and combined punishment mechanisms can improve cooperation rates even further, but at the cost of increased punishment expenditures—reducing group efficiency relative to just direct punishment.  
- **Role of punishment cost:** If punishing is costly and not net-rewarding, neither cooperation nor punishment emerges, and efficiency collapses.  
- **Moderators:** Partner selection and reputation mechanisms further boost the efficiency-enhancing effect of direct punishment.
- **Robustness:** Effects are robust to changes in player population size.

The two other papers suggest, but do not demonstrate, that punishment can shape cooperation via behavioral and reputational mechanisms:
- **Ashlock et al. (1996):** Punishers are viewed less favorably than those who withdraw cooperation, especially if punishment leaves them with low payoffs, but no efficiency outcomes are reported.
- **Chen & Hauser (2005):** Punishing strategies stabilize cooperation behaviorally, but efficiency consequences are not evaluated.

# 5) Prediction Guidance

Based on the literature, the following guidance is appropriate for predicting the effect of enabling peer punishment on average group efficiency:
- **If direct punishment is net-rewarding** (punishment yields a positive return via increased cooperation), enabling such punishment can be expected to raise efficiency compared to a no-punishment baseline.  
- **The magnitude of efficiency gain** depends critically on the cost structure of punishment (punishment_cost), and potential for partner selection and reputational mechanisms to operate.
- **Third-party punishment or excessively costly mechanisms** may increase cooperation rates but are likely to decrease group efficiency relative to direct, low-cost punishment, due to wasteful expenditures on punishment itself.
- **Findings are more directly applicable to IPD-like environments** than PGGs; extrapolation to PGGs should be cautious, especially regarding group size robustness and structural specifics.
- **No paper compares treatment and control efficiency in canonical PGGs:** so predictions outside the studied MARL/IPD environments are indirect.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed:**
- `player_count`, `num_rounds`, `all_or_nothing`, `punishment_cost`, `punishment_tech`, `show_n_rounds`
    - These dimensions are manipulated or discussed empirically, with evidence of the main effect (Dasgupta & Musolesi, 2025) implying robustness to changes in group size and number of rounds, and the critical role of punishment cost/technique.

**Indirectly/contextually discussed:**
- `mpcr` (only mentioned in Chen & Hauser, 2005, but not directly linked to efficiency outcomes)
- `partner selection` and `reputation` mechanisms (important moderators in Dasgupta & Musolesi, 2025, but not explicit in the 14 dimensions list)
- `reward_exists`, `reward_cost`, `reward_tech`: Not directly studied; effects for efficiency are not explored.

**Sparse or missing:**
- `chat`, `default_contrib`, `show_other_summaries`, `show_punishment_id`, `reward_exists`, `reward_cost`, `reward_tech`, `show_other_summaries`, `show_punishment_id`

Many of the 14 prediction-relevant game design dimensions are not empirically explored in this set; conclusions are strongest regarding `punishment_cost` and the nature (direct/third-party) of punishment.

# 7) Important Limitations

- **No canonical PGGs studied:** All results are from IPD or adjacent repeated games, so generalization to PGGs is indirect and potentially limited.
- **Only one paper reports efficiency outcomes:** Most evidence is non-payoff behavioral, providing limited direct support for efficiency-based prediction.
- **Missing coverage for many prediction dimensions:** Key moderators like communication (chat), contribution framing, reward systems, and summary or information display conditions, are not empirically investigated here.
- **Population type:** Dasgupta & Musolesi (2025) uses MARL agents rather than human subjects, which may limit transferability of findings.
- **No variation or manipulation of control efficiency:** The typical prediction context—using control efficiency to predict treatment efficiency given punishment—is not directly tested.
- **Ambiguity in real-world interpretation:** Ashlock et al. (1996) and Chen & Hauser (2005) suggest reputational and behavioral pathways for punishment but do not track efficiency or group payoff, so their relevance is limited to theoretical or mechanistic insights.
- **No direct evidence on some punishment design nuances:** E.g., punishment identity visibility, reward existence, or communication/moderators.

**In sum:** This literature set provides some mechanistic and indirect empirical guidance, particularly regarding the efficiency advantage of net-rewarding, direct peer punishment in repeated cooperative dilemmas. However, it lacks both direct coverage of canonical PGG environments and systematic attention to most of the design dimensions critical for robust downstream efficiency prediction. Modelers should extrapolate with caution.
