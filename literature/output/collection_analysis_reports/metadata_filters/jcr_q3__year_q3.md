# 1) Evidence Base

The evidence base is relatively **broad and strong for the core prediction task**, though the most directly useful evidence (exact-match) is provided by a **subset of empirical lab experiments and formal theoretical models**. Among the 92 papers:

- **Empirical studies** (especially lab experiments) offer clear, quantitative evidence on efficiency and payoff outcomes in canonical and variant public goods games (PGGs) with and without peer punishment (e.g., Pfattheicher et al., 2018; Kamei, 2019; Hou et al., 2019).
- **Theory papers** provide detailed formal models, often with explicit mappings from design parameters to expected payoff/efficiency outcomes (e.g., Dutta et al., 2021; Jiao et al., 2020; Wang & Lv, 2019).
- The wider set includes many **adjacent, indirect, or context-only studies** on cooperation, norm enforcement, social dilemmas, or trust games, often with behavioral but not payoff-based outcomes.
- The literature provides **rich variation in game design dimensions**, covering most of the 14 prediction variables, although direct, empirical efficiency data for all parameter combinations is limited.
- There is a **mix of settings**: canonical linear PGGs (with and without peer punishment), all-or-nothing and variant games, games with reward, third-party or centralized punishment settings, and some close analogues (CPR, trust game).
- The literature includes both **short-run and longer-term effects**, institutional variations, and moderator variables (e.g., monitoring regime, cost/effectiveness of punishment, social context).

**Summary:** The evidence base is strong for the core linear/repeated PGG with (peer) punishment and efficiency outcomes, but **thins out for complex variants**, large and very small groups, rich communication, and when multiple dimensions (e.g., reward + punishment + chat) interact.

---

# 2) Task Relevance

**pgg_or_variant:**  
- **Exact relevance**: Many papers focus on repeated, canonical PGGs or very close variants, directly manipulating punishment and measuring efficiency (e.g., Pfattheicher et al., 2018; Dutta et al., 2021).  
- **Close relevance**: Some studies use trust games, collective risk dilemmas, CPR games, or team production games with similar incentive structures and group dynamics.  
- **Adjacent/weak relevance**: Some explore only related social dilemmas, dictator/prisoner's dilemma games, or theoretical accounts not implemented as PGGs.

**punishment_or_sanctions:**  
- **Exact**: Many directly test the presence vs absence of **peer punishment** or institutional punishment, including cost structures and implementation (Pfattheicher et al., 2018; Hou et al., 2019; Kamei, 2019).  
- **Close**: A substantial number examine reputation, approval, social feedback, ostracism, or centralized (third-party) punishment as alternative or supplemental mechanisms.  
- **Adjacent/weak**: Many focus on reward, minimum provision rules, or other norm enforcement mechanisms only tangentially tied to punishment.

**efficiency_or_related_payoff_outcome:**  
- **Exact**: Several top papers **directly measure efficiency** (group payoff as share of cooperative optimum) or use very close proxies (mean group payoff, normalized utility, surplus; e.g., Pfattheicher et al., 2018; Dutta et al., 2021; Lippert & Tremewan, 2021).  
- **Close**: Many report group earnings, welfare, or aggregate payoffs, which are often convertible to efficiency ratios.  
- **Adjacent/weak**: A considerable share focus on **behavioral outcomes** (contribution rates, cooperation sustainability, punishment frequency)—relevant for mechanism but not equivalent to efficiency.

**Summary:** A strong subset of the literature is **highly relevant across all three dimensions**, but a significant portion provides only indirect or contextual evidence for regarding the efficiency effects of peer punishment in public goods games.

---

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes:**  
- **Efficiency** (primary): Ratio of total group payoff to maximum possible under full cooperation. Reported directly in several core studies and close theoretical models (e.g., Dutta et al., 2021; Wang & Lv, 2019; Hou et al., 2019; Lippert & Tremewan, 2021).
- **Group/average payoff, surplus, welfare**: Frequently measured and, when mapped to group maximum, convertible to efficiency.
- **Earnings, total coins/tokens**: Used in most experiments; sometimes only summary data is available.

**Non-payoff behavioral outcomes:**  
- **Contribution rates, cooperation levels, incidence of punishing/punishment assigned**: Very frequently reported as the main or only outcome (e.g., Greenwood et al., 2018; Chen et al., 2018).
- **Norm compliance, retaliatory punishment, trust, satisfaction**: Behavioral or attitudinal outcomes that are important for understanding mechanisms but not equivalent to efficiency.

**Distinction:**  
- The literature **often conflates behavioral and payoff outcomes**, but careful analysis reveals that **increased cooperation via punishment may not always increase efficiency** due to direct costs of punishment (especially when antisocial punishment or excessive use occurs).
- Some studies report only behavioral outcomes, making them **less directly informative for quantitative efficiency prediction** (e.g., Molenmaker et al., 2019; Fraser & Nettle, 2020).

---

# 4) Main Findings Relevant To Prediction

### Effects of Punishment on Efficiency

- **Peer punishment usually increases efficiency** relative to no-punishment controls when:  
  - Punishment is **not excessively costly** relative to the harm it inflicts (i.e., high punishment effectiveness or "tech"; Dutta et al., 2021; Wang & Lv, 2019; Hou et al., 2019).
  - The opportunity for **antisocial or counter-punishment** is limited (Pfattheicher et al., 2018; Barrett, 2020).
  - There are **mechanisms to control punishment spiral** (e.g., democratic or probabilistic punishment; Pfattheicher et al., 2018; Jiao et al., 2020).

- **Efficiency may decline** (i.e., group pays more in punishment costs than is gained by increased cooperation) when:
  - Punishment is applied **excessively, inefficiently, or antisocially**, especially in early rounds or with uncoordinated punishers (Pfattheicher et al., 2018; Shreedhar et al., 2020).
  - **Punishment is costly** and fines are low (Greenwood et al., 2018; Fang et al., 2020).
  - **Corrupt or poorly targeted punishment** is present (Abbink et al., 2020).

- **Institutional design moderates effects**:
  - **Democratic, group, or probabilistic punishment** mechanisms improve efficiency over standard (individual) peer punishment, as they restrain wasteful punishment and antisocial punishment (Pfattheicher et al., 2018; Jiao et al., 2020).
  - **Endogenous monitoring and imperfect punishment networks** may yield higher efficiency than complete/centralized structures, as lower monitoring/punishment reduces costly overuse (DeAngelo & Gee, 2020; Shreedhar et al., 2020).

- **Strong empirical and theoretical convergence**: For canonical settings, punishment increases efficiency when designed well (moderate cost, effective, not open to abuse), but **the mapping to specific parameter spaces can be nonlinear and context-dependent** (Dutta et al., 2021; Fang et al., 2020; Perry et al., 2020).

**Payoff vs Behavioral Findings:**  
- Papers focusing on **contribution/cooperation rates** almost universally find that punishment increases cooperation, but in some cases, at such high cost that total efficiency does not improve or can even decline (Pfattheicher et al., 2018; Perry et al., 2020; Shreedhar et al., 2020).

---

# 5) Prediction Guidance

- **Control efficiency is a strong baseline predictor:** If efficiency without punishment is already high (near full cooperation), adding punishment may not improve, or may even reduce, efficiency due to the direct cost of punishment with little behavior left to change.
- **Punishment increases efficiency most when:**
  - The control efficiency is **intermediate or low** (room for improvement).
  - **Punishment cost is low to moderate** and has a **high effect-to-cost ratio** (punishment_tech).
  - **Punishment is well-targeted** at defectors (low antisocial/counter punishment).
  - **Game is sufficiently long for learning and norm stabilization** (democratic or group-run punishment can outperform control in extended runs; Pfattheicher et al., 2018).
- **Increased punishment effectiveness** (punishment_tech) enhances the efficiency gain, but only if costs (punishment_cost) are not so high as to offset gains (Wang & Lv, 2019; Hou et al., 2019; Dutta et al., 2021).
- **Communication (chat)**, **joint decision-making**, or **rating/reputation mechanisms** may yield similar or greater efficiency gains at lower cost (Lippert & Tremewan, 2021; Faillo et al., 2020).
- **Corruption, bribery, and antisocial punishment** are strong negative moderators; if present, efficiency gains from punishment are much less likely or may be negative (Abbink et al., 2020; Fang et al., 2020; Huang et al., 2018).

**Prediction under different game design dimensions should be grounded in:**
- Parameter-specific findings (e.g., efficiency gain for 4 players, 10 rounds, continuous, no chat, with punishment: Dutta et al., 2021; Pfattheicher et al., 2018).
- Structural moderators (monitoring regime, communication, matching, probabilistic vs certain punishment).

---

# 6) Design Dimensions Highlighted Across Papers

**Directly informed:**
- **player_count**: Effects on efficiency are observed for 2-, 3-, and 4-player games. Group size interacts with punishment effectiveness; small groups are better studied (Dutta et al., 2021; Lippert & Tremewan, 2021; Kamei, 2019).
- **num_rounds**: Most evidence from 6–20 rounds; longer games allow punishment effects to accumulate (Pfattheicher et al., 2018; Lippert & Tremewan, 2021; Kamei, 2019).
- **mpcr**: Reported in almost all direct studies; efficiency effects of punishment tend to increase at moderate/high MPCR (Dutta et al., 2021; Wang & Lv, 2019).
- **punishment_cost**, **punishment_tech**: Central to almost every PGG-with-punishment study. Low cost or high tech gives stronger efficiency gains.
- **all_or_nothing**: Both continuous and all-or-nothing designs covered; most core findings generalize but with some nuance (Pfattheicher et al., 2018).

**Indirectly informed/contextually discussed:**
- **chat**: Communication increases efficiency and can act as a substitute for punishment; rarely both present and measured (Kamei, 2019; Lippert & Tremewan, 2021).
- **reward_exists / reward_cost / reward_tech**: Less studied, but evidence suggests reward alone is less effective than punishment or the combination (Hou et al., 2019; Fang & Chen, 2021).
- **show_n_rounds, show_other_summaries, show_punishment_id**: Some theoretical coverage (Jindani, 2020; Mihm & Toth, 2020), experimental studies less common.

**Effectively missing/sparse:**
- **default_contrib**: Rarely varied directly; only a few studies mention framing effects of defaults.
- **show_punishment_id**: Very rarely manipulated except in community enforcement theory and a few adjacent studies.
- **complex combinations (reward plus punishment plus chat)**: Rarely all varied in factorial designs.

---

# 7) Important Limitations

- **Coverage bias**: Most studies are with **small groups, short horizons, and laboratory conditions**. Effects may differ in larger or real-world groups, in field or online environments.
- **Behavioral vs payoff conflation**: Many studies report **cooperation rates**, not efficiency/payoff. **Actual efficiency can be lower with punishment despite higher cooperation** because of punishment costs.
- **Delivery method edge cases**: The impact of punishment is sensitive to **implementation details** (e.g., standard vs democratic punishment, centralization, chance of corruption/antisocial use), but evidence for these variations is still sparse.
- **Design space gaps**: Several game design dimensions (**default contribution, persistent identity, mixed monitoring regimes, reward configurations, feedback visibility**) are **not systematically studied** in combination with punishment and efficiency outcomes.
- **External validity**: Results are strongest for laboratory linear PGGs; **generalization to field settings, larger/heterogeneous groups, or highly variant games requires caution**.
- **Dynamic and cultural moderators**: Some findings highlight parameter thresholds and cultural/psychological moderators (Pfattheicher et al., 2018; Dutta et al., 2021; Barrett, 2020), but these are often discussed in theory or as post hoc explanations, lacking systematic experimental variation.

---

## **Summary Table: Prediction Relevance of Dimensions**

| Dimension             | Evidence Coverage                | Prediction Implications                                               |
|-----------------------|----------------------------------|-----------------------------------------------------------------------|
| player_count          | Direct, broad                    | Small groups: clearer positive effect; larger: less clear             |
| num_rounds            | Direct, moderate                 | Longer games: effects compound, democratic/group punishment improves  |
| mpcr                  | Direct, strong                   | Higher MPCR → larger efficiency gains from punishment                 |
| punishment_cost       | Direct, strong                   | Lower cost → stronger efficiency gain                                 |
| punishment_tech       | Direct, strong                   | Higher tech (impact per unit cost) → stronger efficiency gain         |
| all_or_nothing        | Direct, moderate                 | Effects similar but context-dependent; most with continuous           |
| chat                  | Indirect, moderate               | Strongly increases efficiency; can substitute for punishment          |
| reward_exists, etc.   | Indirect, sparse                 | Reward alone less effective; combo can increase efficiency            |
| show_n_rounds, etc.   | Indirect/theory                  | Feedback increases effectiveness/contextualizes punishment            |
| default_contrib       | Sparse                           | Little direct evidence                                                |
| show_punishment_id    | Sparse/theory                    | Possible moderating effect; insufficient data                         |

---

**Bottom line:**  
- **When directly studied** (canonical repeated PGGs with peer punishment), **enabling punishment often increases efficiency, but only when punishment is well-targeted, not overly costly, and not vulnerable to antisocial use or corruption**.  
- **Key moderators** are punishment cost/effectiveness, monitoring regime, group size, and the baseline level of cooperation absent punishment.  
- **Predictions for complex or less-studied parameter combinations should be made with caution** given evidence gaps.  
- **Do not infer efficiency changes from cooperation rate changes without considering punishment costs**—increases in cooperation with very costly punishment may not yield net efficiency increases.  
- **Decisions should use only design dimensions with strong evidence coverage** for extrapolation, and maintain uncertainty for unexplored aspect combinations.
