# 1) Evidence Base

The literature base for this analysis comprises 103 academic papers, spanning a mix of **empirical experimental studies** (both laboratory and field) and **theoretical modeling papers**. The paper set is **broad and rich** regarding core public goods games (PGG) and the effects of punishment and sanctions, with direct empirical evidence available for standard PGGs as well as a substantial body of adjacent work (e.g., repeated Prisoner's Dilemma, trust games, field studies in commons management, and theory of cooperation evolution).

- **Empirical Papers:** Numerous lab experiments directly test the effect of enabling versus disabling punishment in standard PGGs (e.g., Fehr & Gächter, 2002; Rand et al., 2009; Eriksson & Strimling, 2012). Field experiments and observational studies extend results to real-world commons and diverse populations.
- **Theoretical Papers:** Many theoretical and modeling papers explore mechanisms, parameter sensitivity, and evolutionary stability of punishment and cooperation (e.g., Hauert et al., 2007; Sigmund et al., 2010). These models often map out when and why punishment may or may not increase group welfare or efficiency.

**Narrowness/Broadness for the Prediction Task:**  
For the specific task of *predicting efficiency* with punishment enabled (given design features and control-game efficiency), the paper set is quite strong—multiple high-quality sources directly measure efficiency or related payoff outcomes in PGGs with experimental control over game dimensions. However, there is notable coverage of adjacent or indirect settings (dyadic games, field common-pool resources, indirect punishment), and not all dimensions of experimental design are equally or directly addressed.

---

# 2) Task Relevance

**pgg_or_variant:**
- **Exact relevance**: Many papers deploy canonical PGG lab designs or minimal variants (e.g., player count 4-6, repeated rounds, voluntary or compulsory contribution, continuous or discrete choices).
- **Close relevance**: A subset use adjacent settings—repeated PD, trust games, or evolutionary simulations with PGG structure.

**punishment_or_sanctions:**
- **Exact relevance**: Core studies focus on peer punishment or institutional sanctions, manipulating their presence/absence and severity.
- **Close or adjacent relevance**: Some model reputation, exclusion, reward, or ostracism as substitutes/adjuncts for direct punishment; others examine antisocial punishment or coordination in collective monitoring.
- **Weak/none**: A considerable portion of the broader set does not include punishment, useful primarily for baseline (control) efficiency estimation.

**efficiency_or_related_payoff_outcome:**
- **Exact relevance**: Key PGG experiments and models (e.g., Fehr & Gächter, 2002; Gürerk et al., 2006) directly measure efficiency—as total group payoff relative to the cooperative maximum.
- **Close/adjacent relevance**: Several report earnings, surplus, or group welfare, or infer efficiency from contribution/payoff proxies.
- **Weak/none**: Many behavioral, neurological, or psychological studies only measure cooperation or punishment assignment, not efficiency.

**Summary:**  
The set contains a robust core of **exactly relevant** sources on PGGs, punishment, and efficiency-based outcomes, supplemented by a large pool of *contextually adjacent* literature.

---

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes:**
- **Efficiency:** Defined as group payoff relative to the cooperative optimum; measured directly in a subset of PGG experiments and theory papers (e.g., Fehr & Gächter, 2002; Gürerk et al., 2006; Rockenbach & Milinski, 2006).
- **Related:**
  - Total earnings, average payoff, welfare, or surplus (e.g., Eriksson & Strimling, 2012; Dreber et al., 2008; Rand & Nowak, 2011).
  - Sometimes aggregate or per capita group earnings in control vs. punishment settings.

**Non-Payoff Behavioral Outcomes:**  
(Explicitly distinct from efficiency; often more commonly reported)
- **Contribution/Cooperation rates** (e.g., fraction of tokens contributed in a round)
- **Frequency and targeting of punishment events**
- **Retaliation, vendetta cycles, or antisocial punishment**
- **Punishment assignment and emotional mechanisms (e.g., anger, perception of fairness)**
- **Norm compliance or partner choice behavior**

**Caveat:**  
While increased contribution is often correlated with higher efficiency, studies are careful to warn that increased punishment use can impose direct costs that may offset gains from increased cooperation, meaning **high cooperation does not always equal high efficiency** (see, e.g., Rand et al., 2009; Herrmann et al., 2008).

---

# 4) Main Findings Relevant To Prediction

**General Patterns:**
- **Punishment often increases efficiency—but not always**: Most standard PGG lab experiments find that enabling peer punishment *increases group efficiency* relative to no-punishment controls (Fehr & Gächter, 2002; Gürerk et al., 2006). The effect is robust across variations in group sizes and rounds, but...
- **Efficiency gains are sensitive to design details and context:**  
    - **High punishment costs** or frequent **retaliation** can offset or entirely erase efficiency gains (Rand et al., 2009; Fehl et al., 2012).
    - **Antisocial punishment** (punishing cooperators) or vendetta cycles can vastly reduce or nullify welfare gains, particularly in some cultures or populations (Herrmann et al., 2008).
    - **Communication, reputation, or centralized monitoring** often *amplify* or *replace* the efficiency gains from punishment (Janssen et al., 2010; Rockenbach & Milinski, 2006).
    - **Weak vs. strong** punishment: Only *strong and externally imposed* punishment institutions reliably solve the ‘hard problem’ of cooperation for low-cooperation groups (Eriksson & Strimling, 2012).

**Modifiers and Conditionalities:**
- **Group Size (player_count):** Effects of punishment are generally positive in small/medium groups; larger sizes increase challenges for coordination and can reduce punishment’s efficacy unless mechanisms (e.g., reputation, centralization) address second-order free-riding (Perc, 2012; Boyd et al., 2010).
- **Number of Rounds (num_rounds):** More rounds allow for sustained cooperation; endgame effects may still erode cooperation unless punishment is present (Fehr & Gächter, 2002; Fowler, 2005).
- **Marginal per capita return (mpcr):** Higher mpcr (i.e., greater benefits from cooperation) usually magnifies the efficiency effect of punishment (Rockenbach & Milinski, 2006; Rand & Nowak, 2011).
- **Punishment cost and magnitude:** High cost or low impact punishment can reduce efficiency gains, or even make intervention negative for group payoffs (Rand et al., 2009; Sigmund et al., 2010).
- **Institutional/technological design:** Centralized or coordinated punishment often achieves higher efficiency than purely peer-based sanctioning—especially when legitimacy is high (Baldassarri & Grossman, 2011).
- **Communication and reputation:** Communication can substitute for or amplify the effects of punishment; reputation mechanisms often raise efficiency even more than direct punishment (Milinski et al., 2002; Sigmund et al., 2010).

**Cases Where Punishment Fails to Raise Efficiency:**
- **Punishment is used antisocially/retaliation dominates** (Herrmann et al., 2008; Fehl et al., 2012)
- **Punishment is present but cannot be effectively coordinated (second-order free-rider problem)** (Perc, 2012; Sigmund et al., 2010).
- **High cost/low impact ratios or pool punishment with insufficient reach** (Sigmund et al., 2010; Bodnar & Salathé, 2012).
- **Absence of supporting context (no reputation, high group size, anonymity, no communication)** (Janssen et al., 2010; Hilbe & Traulsen, 2012).

---

# 5) Prediction Guidance

**Direct Guidance from Literature:**
- **For standard PGGs** (moderate group size, repeated rounds, peer punishment enabled at standard cost/impact):
  - **Expect a substantial efficiency increase** when punishment is enabled, particularly if control (no-punishment) efficiency is low. Effect size is largest if efficiency in control is low and punishment is strong, coordinated, and not overused for retaliation (Fehr & Gächter, 2002; Gürerk et al., 2006; Eriksson & Strimling, 2012).
- **If control efficiency is already high** (many are contributing), the absolute gain from adding punishment may be modest, and costs of unnecessary punishment may lower *net* efficiency (Rand et al., 2009).
- **If antisocial punishment, vendetta cycles, or unchecked retaliation are prevalent** (e.g., due to culture or group composition), efficiency gains may be minimal or negative (Herrmann et al., 2008; Fehl et al., 2012).
- **If punishment is centralized, coordinated, or strongly enforced**, the efficiency boost is greatest and more robust, provided punishers are not excessively burdened (Boyd et al., 2010; Baldassarri & Grossman, 2011).
- **Critical moderators** for accurate prediction include punishment cost/effectiveness, type (peer vs. institutional), presence of reputation/communication, group size, possibility of antisocial punishment, and culture/norm context.

**Indirect Guidance/Caveats:**
- High mpcr, communication, or visibility of actions (reputation) can partially or wholly substitute for punishment in boosting efficiency (Rockenbach & Milinski, 2006; Milinski et al., 2002).
- Presence of rewards can be as or more effective than punishment and more efficient, as punishment is costly (Rand et al., 2009).
- Design dimensions alone do not fully determine outcomes: social context and baseline group composition (cooperative types, antisocial types) matter (Herrmann et al., 2008; Kurzban & Houser, 2005).

---

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**  
(`= explicit manipulation or analysis of dimension’s moderation of punishment effect on efficiency`)
- `player_count` — extensively manipulated in both empirical and theoretical studies.
- `num_rounds` — varied for examining sustainability/endgame effects.
- `mpcr` — key moderator, with parameter sweeps in both lab and theory papers.
- `punishment_cost` and `punishment_tech` (cost, magnitude, centralization, effectiveness) — frequently varied and analyzed.
- `all_or_nothing` (binary vs. continuous choice) — covered in both experiments and models.

**Indirectly Informed/Contextually Discussed:**  
- `chat`, `show_n_rounds`, `show_other_summaries` — communication and visibility mechanisms are discussed extensively, shown to act as amplifiers or substitutes for punishment.
- `reward_exists`, `reward_cost`, `reward_tech` — some direct cross-manipulation with punishment, though less frequently as a primary focus.
- `show_punishment_id` — identification or anonymity of punishers as a moderator for retaliation and antisocial punishment.
- `default_contrib` — framing of contributions as opt-in/opt-out is less commonly varied, but is sometimes noted to affect baseline cooperation.
- `show_punishment_id` — linked to retribution/vendetta risks, especially in field and cross-cultural studies.

**Effectively Missing or Sparse:**
- Systematic coverage of `default_contrib`, detailed variations in reward parameters (especially cost/tech), and fine-grained manipulation of visibility features or endogenously varying the game’s communication structure.

---

# 7) Important Limitations

- **Underrepresentation of Some Moderators:**  
  Not all 14 game design dimensions are fully covered as moderators of punishment’s efficiency effects. Especially sparse are analyses on the framing (`default_contrib`), several reward-related dimensions, and specific roles of summary displays.
- **Context Sensitivity and External Validity:**  
  The positive effect of punishment on efficiency is highly **context-dependent**. Culture, existing norms, prior group composition, and the possibility of antisocial punishment (punishing cooperators) can reverse predicted effects—yet these are often not immediately observable or codified game design parameters.
- **Outcome Ambiguity in Adjacent Literature:**  
  Many behavioral studies report changes in contributions, punishment assignment, or emotional responses without mapping to efficiency or group payoff, leading to potential overestimation of the link between punishment and efficiency if taken at face value.
- **Parameter Sensitivity:**  
  The effect size and even the direction of the punishment effect on efficiency are not monotonic and can change sharply with modest variation in **punishment cost**, **fine**, **group size**, **mpcr**, or the presence/absence of antisocial punishment.
- **Assumptions Hidden in Theory Papers:**  
  Theoretical models sometimes yield optimistic conclusions about punishment effects under assumptions (e.g., perfect coordination, restricted strategy sets, no antisocial punishment) that are not always realized in experiments or real settings.
- **Limited Subpopulation/Cross-Society Testing:**  
  Direct measurement of efficiency impact in non-Western or field contexts is less prevalent, and most cross-society findings suggest more variability (Herrmann et al., 2008; Wu et al., 2009).
- **Absence of Long-Term and Dynamic Designs:**  
  Most laboratory evidence is for short-run or mid-length repeated games. Effects may differ in very long-term, open-ended, or dynamically structured environments.

---

**Conclusion:**  
The synthesized literature strongly supports the **expectation that enabling peer punishment in classic public goods games increases group efficiency, especially when baseline (control) efficiency is low**, group size is moderate, punishment is effective but not excessive, and antisocial retaliation is minimized. However, **the size and even the sign of the efficiency effect can flip** under different cost structures, social contexts, or if punishment escalates or is misdirected. Accurate prediction should therefore incorporate not only the experimental design dimensions but also proxies for group composition, baseline efficiency, and local cultural or institutional context wherever possible.
