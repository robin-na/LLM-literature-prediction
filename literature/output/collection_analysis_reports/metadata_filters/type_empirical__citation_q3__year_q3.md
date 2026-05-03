# 1) Evidence Base

This paper set is relatively **broad** in its coverage of public goods games (PGGs), with a strong empirical (lab experimental) focus. Of the 87 papers, the largest subset are experimental laboratory studies, with some observational and field experiments. The set contains numerous **exact-match PGG studies directly manipulating punishment**, as well as studies with close or adjacent designs (e.g., CPR games, trust games, or repeated Prisoner’s Dilemmas). Theories and mechanism arguments appear, but the bulk of evidence is **empirical**.

Regarding outcomes, several papers measure **efficiency or group payoffs** directly, which aligns closely with the downstream prediction task. Many others focus on behavioral outcomes (e.g., contribution rates, cooperation, norm compliance, punishment frequency), which, while informative about mechanisms, only indirectly speak to efficiency.

Relative to the 14 game design dimensions relevant for prediction, the literature is **strongest** on dimensions like player count, number of rounds, marginal per-capita return (mpcr), punishment existence/type, and punishment cost/technology. Dimensions like chat, default contributions, information visibility, and presence of rewards are also addressed but less comprehensively. Some variables (e.g., show_punishment_id, reward_cost, reward_tech) receive sparse or no direct empirical attention.

# 2) Task Relevance

**pgg_or_variant:**  
- **Exact relevance**: Many papers use standard linear public goods games (PGGs) or very close variants, directly matching the downstream prediction environment. A smaller set uses CPR games, repeated trust/PD games, or other social dilemmas: these are labeled ‘close’ or ‘adjacent’ depending on their similarity.
  
**punishment_or_sanctions:**  
- **Exact relevance**: A major portion of the set manipulates or compares the presence/absence or structure of **punishment institutions** (peer, central, leader, democratic, exclusion, etc.), perfectly matching the target intervention.
- **Close/adjacent**: Some studies substitute reward-only, monitoring, ostracism, gossip, or liability rules that functionally resemble punishment.
- **Weak/none**: Baseline or control studies without sanctions/punishments are present but not the majority.

**efficiency_or_related_payoff_outcome:**  
- **Exact**: Over a dozen papers report direct measures of **efficiency** (group payoff relative to full cooperation) or closely related outcomes (total group payoff, welfare, surplus).
- **Close**: Several more report average earnings or group allocation; these are taken as close proxies.
- **Adjacent/weak/none**: Many papers, even those manipulating punishment in PGGs, report only behavioral outcomes (contribution/cooperation) and not efficiency or payoff.

**Summary:**  
- The evidence base is **strong and directly relevant** for the prediction task on PGGs with punishment and efficiency. However, coverage is **uneven**—some critical design dimensions and contexts (especially large group sizes, complex institutions, or information conditions) are much less explored in direct efficiency terms.

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes** (closest to ‘efficiency’ as defined for prediction):
- **Group efficiency** (payoff relative to the cooperative optimum): Directly measured in a significant set of PGG/punishment studies (e.g., Ozono et al., 2020; Gürerk et al., 2018; Engl et al., 2021; Nockur et al., 2021; Marcin et al., 2019; Dannenberg et al., 2020; Kamei, 2020; Ahmad & Loch, 2020).
- **Group payoff / total earnings / welfare**: Used as primary or secondary outcomes in many studies (sometimes instead of the efficiency ratio; see above for close mapping).
- **Average individual payoff**: Sometimes reported, but often less relevant for group-level efficiency.

**Non-Payoff Behavioral Outcomes** (adjacent or indirect for efficiency prediction):
- **Contribution/cooperation rates**: Universally measured; inform about direction of punishment effect but not its net efficiency impact, since costly punishment can reduce payoffs even as cooperation increases.
- **Punishment frequency, intensity, assignment**: Used to analyze mechanisms but not final payoffs.
- **Norm compliance, satisfaction, trust, fairness perceptions**: Valuable for mechanism explanation, but not efficiency.

**Findings using behavioral rather than payoff outcomes are valuable for mechanistic interpretation, but must not be conflated with efficiency impacts.**

# 4) Main Findings Relevant To Prediction

**a) Enabling Punishment Usually Increases Efficiency, But Not Always:**
- In **standard linear PGGs**, enabling peer or central punishment raises contributions and frequently raises average payoffs/efficiency relative to no-punishment controls, especially where punishment is cost-effective and anti-social punishment is minimal (Gürerk et al., 2018; Engl et al., 2021; Marcin et al., 2019).
- **Reward mechanisms** (when present) can have similar or even stronger effects, but their net efficiency depends on their cost/effect ratio (Gürerk et al., 2018).
- However, enabling **peer punishment at moderate to high cost** can decrease efficiency—the increased contributions are offset by high punishment expenditures (Nockur et al., 2021; Pfattheicher et al., 2018).

**b) The Effect of Punishment on Efficiency Is Highly Moderated:**
- **Punishment Institution Structure**: Democratic and central punishment systems often mitigate wasteful, anti-social, or retaliatory punishment, yielding higher (or less negative) effects on efficiency than standard peer punishment (Nockur et al., 2021; Pfattheicher et al., 2018; Kamei, 2020).
- **Cost Structure**: If punishment is costless or highly effective (e.g., low cost, high impact), efficiency gains are more likely. High-cost punishment often reduces net efficiency or only yields modest improvements (Dannenberg et al., 2020; Nockur et al., 2021).
- **Targeting and Norm Alignment**: When cooperation is locally inefficient or norm disagreement is present, punishment may fail to increase efficiency or even reduce it (Ozono et al., 2020).
- **Prevalence of Antisocial Punishment**: When there are many ‘antisocial punishers’ (those who punish high contributors or punish out of revenge), enabling punishment can reduce efficiency significantly (Bruhin et al., 2020). This effect also appears culturally.
- **Group Size**: As group size increases, the risk of over-punishment escalates unless punishment is coordinated (Kamei, 2020).
- **Baseline Incentives/Control Efficiency**: If the control game is already highly efficient, adding punishment sometimes reduces, rather than increases, efficiency (Ahmad & Loch, 2020; Nair et al., 2018).

**c) Effects in Non-Standard Environments:**
- **Exclusion/Ostracism as Punishment**: When exclusion is costless, it can robustly increase both cooperation and efficiency; if exclusion is costly, efficiency gains disappear (Dannenberg et al., 2020).
- **Endogeneity of Institutions**: Whether punishment is voted in or imposed (endogenous vs. exogenous) usually does **not** affect efficiency (Marcin et al., 2019; Dannenberg et al., 2020).
- **Visibility and Inequality**: Revealing income/endowment information shifts sanctioning (e.g., from punishing the poor to the rich) and can increase contributions and decrease payoff inequality; efficiency effects are inferred as positive but not always directly measured (Hauser et al., 2021).
- **Supply networks/adapted PGGs**: In adjacent games, enabling punishment can reduce efficiency if the environment is already cooperative, but can increase group allocations (though rarely net payoff) in highly uncooperative environments (Nair et al., 2018).

# 5) Prediction Guidance

**Synthesized Literature Implications:**

- **For games with moderate baseline cooperation (control efficiency < social optimum):**
  - Enabling peer or central punishment is likely to **increase efficiency**, provided punishment is cost-effective and antisocial punishment is minimal (Gürerk et al., 2018; Engl et al., 2021; Marcin et al., 2019).
  - The efficiency gain is moderated by punishment cost, impact, design (peer, leader, central, democratic), group size, and the prevalence of antisocial punishment (Bruhin et al., 2020; Nockur et al., 2021).

- **If the control game already achieves high efficiency (e.g., due to high MPCR or high baseline trust):**
  - Adding punishment may be **ineffectual or even reduce net efficiency** due to punishment costs and/or the emergence of retaliatory/antisocial punishment cycles (Ahmad & Loch, 2020; Nair et al., 2018).

- **When local and global incentives are misaligned, or localization restricts punishment targeting:**
  - Punishment/Reward mechanisms do **not improve efficiency** and may be largely ineffectual (Ozono et al., 2020).

- **For large group sizes (beyond 4–5):**
  - Uncoordinated peer punishment can generate **over-punishment and severe efficiency losses**; coordination mechanisms (e.g., voting, leader) can mitigate this (Kamei, 2020; Nockur et al., 2021).

- **When institutional endogeneity (voting) is present:**
  - It has **small or no additional effect** on efficiency beyond the effect of enabling punishment itself (Marcin et al., 2019).

- **If antisocial punishers are prevalent (whether due to population, culture, or group composition):**
  - The anticipated efficiency gain from punishment should be **discounted or reversed** (Bruhin et al., 2020).

**General prediction approach:**  
- Given game design dimensions and control efficiency, **predict an increase in efficiency when punishment is enabled** in standard PGGs, unless:
    - Punishment is high-cost or low-impact,
    - Peer punishment is unsupervised and group size is large,
    - Control efficiency is already high,
    - Population contains many antisocial punishers,
    - The environment is not locally incentive-aligned.

**Where direct efficiency evidence is absent** (i.e., only behavioral outcomes are provided), only infer efficiency effects with caution, considering punishment costs.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Design Dimensions:**
- **player_count**: Most studies specify and systematically vary group size (especially 4–5 players), with some direct evidence on size effects and over-punishment at large N.
- **num_rounds**: Number of rounds is usually standardized and reported; evidence for the effect of round count on sustainability of efficiency is available.
- **mpcr**: Systematic variation and reporting; higher mpcr generally boosts baseline cooperation and can interact with punishment effectiveness.
- **punishment_cost/punishment_magnitude (punishment_tech)**: Critical dimension—cost/effect ratio is linked tightly to efficiency outcomes.
- **all_or_nothing/continuous_contribution**: Both types present; evidence that these affect how punishment translates into higher efficiency.
- **punishment_exists/institution type**: Covered comprehensively; evidence on peer/central/democratic variants.
- **chat**: Examined in some studies, generally increases baseline cooperation (possibly substituting for punishment).
- **show_other_summaries/show_n_rounds**: Present but less systematically varied in relation to efficiency with punishment.

**Indirectly Informed or Contextually Discussed:**
- **default_contrib**: Rarely manipulated as a standalone variable.
- **reward_exists/reward_cost/reward_tech**: Some studies examine reward and compare its efficiency effects to punishment; less common and sometimes confounded by reward design.
- **show_punishment_id**: Very sparsely addressed; identity revelation is mentioned but rarely as a primary manipulation.

**Effectively Missing Dimensions:**
- **Specific manipulation of detailed information structures, especially show_punishment_id, reward_cost, reward_tech.**
- **Systematic, large-scale variation of communication modes (chat, gossip) in connection to punishment and efficiency.**
- **Fine-grained manipulation of default contributions or opt-in/opt-out framing.**

# 7) Important Limitations

- **Behavioral vs. Payoff Outcomes:** Many studies report only contribution/cooperation rates; effects on group efficiency are often inferred rather than measured. Behavioral gains can be offset or even reversed by the costs of punishment (Nockur et al., 2021; Pfattheicher et al., 2018). Predictions based on behavioral outcomes must be tempered.

- **Narrow Group Sizes and Settings:** Most direct efficiency evidence comes from **small groups** (3–5 players). Large group and complex networked environments are under-studied, and generalization should be cautious.

- **Cultural and Population Heterogeneity:** The efficiency effect of punishment is **not universal**—it depends on the prevalence of antisocial punishers, which varies by context (Bruhin et al., 2020).

- **Limited Treatment of Information, Framing, and Default Conditions:** While some studies examine the impact of chat, income visibility, or norm framing, the set is sparse on manipulations of more nuanced information and institutional design variables.

- **Rare Controls for High Baseline Efficiency:** Where control efficiency is already high (e.g., high mpcr), the net efficiency impact of punishment may be zero or negative, but only a minority of studies feature such controls.

- **Endogeneity and Institutional Choice Effects Often Modest:** Institution endogeneity (participant voting) rarely affects efficiency beyond the core presence/absence of punishment (Marcin et al., 2019; Dannenberg et al., 2020).

- **Real-World Generalizability:** The tendency for punishment to be less frequent and less effective outside the lab (Pedersen et al., 2020) means lab results may overestimate efficiency gains from punishment in naturalistic settings.

- **Sparse Data on Some Design Dimensions:** Variables such as reward/technology/cost, or the public/private nature of sanctions, are not systematically mapped.

---

# Summary Table: Dimension-to-Evidence Mapping

| Dimension                | Direct    | Indirect          | Contextual     | Missing/Sparse     |
|--------------------------|-----------|-------------------|----------------|--------------------|
| player_count             | Yes       |                   |                |                |
| num_rounds               | Yes       |                   |                |                |
| chat                     | Some      | Indirect on payoff|                | Sparse         |
| all_or_nothing           | Yes       |                   |                |                |
| default_contrib          |           | Contextual        |                | Sparse         |
| mpcr                     | Yes       | Indirect          |                |                |
| punishment_cost          | Yes       |                   |                |                |
| punishment_tech/magnitude| Yes       |                   |                | Sparse detail  |
| reward_exists            | Some      |                   |                | Sparse         |
| reward_cost, reward_tech |           |                   | Contextual     | Sparse         |
| show_n_rounds            | Some      | Contextual        |                | Sparse         |
| show_other_summaries     | Some      | Contextual        |                | Sparse         |
| show_punishment_id       |           | Contextual        |                | Missing        |

---

## **In conclusion**, the literature base provides robust, but contextually contingent, guidance for predicting the efficiency effect of enabling punishment in PGG-like environments. However, predictions must integrate both game design and contextual moderators (especially punishment costs, institution structure, group size, and population composition), and must carefully distinguish between Group efficiency and behavioral outcome metrics. Some design dimensions required for fine-tuned prediction remain underexplored.
