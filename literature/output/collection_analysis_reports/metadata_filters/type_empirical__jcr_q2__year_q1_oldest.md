# 1) Evidence Base

The paper set contains **76 papers**, predominantly **empirical laboratory experiments**, with some field experiments and a smaller number of observational or naturalistic studies. The evidence base is **broad and deep in its coverage of public goods games (PGGs) and punishment mechanisms**, with a rich variety of game designs (varying player count, punishment cost/tech, reward options, communication, etc.) and a strong focus on **payoff outcomes**—especially group earnings and efficiency. The majority of high-relevance evidence comes from controlled laboratory or incentivized economic experiments with explicit reporting of efficiency or overall group payoff, supplemented by field studies and related mechanisms (e.g., ostracism, centralized punishment, social sanctions, reward, communication). The literature is **empirically robust and highly focused on PGG-like environments**, yielding a strong foundation for supporting predictive inference about efficiency impacts of introducing punishment.

# 2) Task Relevance

## Public Goods Game or Variant (`pgg_or_variant`)
- **exact**: The core of the evidence base consists of laboratory and field **public goods games (VCMs, linear PGGs, step-level, or close continuous-action analogs)**. Many experimental studies have direct mappings to the prediction task.
- **close**: Several studies use **common-pool resource (CPR) games** or other multi-person social dilemmas structurally close to PGGs.
- **adjacent/weak**: Some studies (especially those focused on trust games, investment games, prisoner’s dilemmas, or social preference games) provide **adjacent context or theoretical/motive-based insights**, but do not directly inform group efficiency in PGGs.
- **none**: A minority of psychological studies lack direct game-theoretic structure or only offer context.

## Punishment or Sanctions (`punishment_or_sanctions`)
- **exact**: The majority of relevant studies **explicitly manipulate the presence of peer punishment, centralized punishment, or social/monetary sanctioning mechanisms**.
- **close**: Some consider ostracism, reputation systems, or feedback incentives as functionally similar to punishment.
- **adjacent/weak/none**: Other work examines informal disapproval, the anticipation of punishment, or uses only non-monetary signals.

## Efficiency or Related Payoff Outcome (`efficiency_or_related_payoff_outcome`)
- **exact**: Many top papers **report group efficiency, mean payoff, or surplus directly** and analyze the effect of punishment on this outcome.
- **close**: Some papers focus on contribution rates and only imply efficiency by positioning results in terms of group earnings, welfare, or public good provision success.
- **adjacent**: Other studies primarily analyze **behavioral or motivational outcomes (e.g., cooperation rates, punishment assignment, norm adherence) without direct efficiency measures**.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes:**
- *Directly reported:* Group efficiency (as fraction of the cooperative optimum), aggregate group earnings/welfare, mean surplus, successful public good provision rates (for step-level games).
- *Closely related:* Group profit after costs, average per-game earnings, surplus net of punishment/reward costs.

**Non-payoff (behavioral) outcomes:**
- Contribution rates, cooperation rates, individual punishment frequency, norm compliance, choices under different institutions, distribution of contributions and punishment, inequality, motivational factors, attitude surveys, and group composition analyses.

**Distinction:**  
Several studies note that **punishment often increases contributions (behavior)** but does not always increase group efficiency or aggregate payoff, due to enforcement costs, antisocial punishment, or institutional detail. Explicit distinctions are often drawn between behavioral (contributions/punishment) and payoff outcomes.

# 4) Main Findings Relevant To Prediction

### a. **Punishment Increases Contributions, but Efficiency Gains Depend on Cost/Efficacy and Design**
- Most experiments show **punishment opportunities lead to sustained higher contributions** compared to control (no-punishment), both in standard linear PGGs and CPR games [(Sefton et al., 2007; Fehr et al., 2002; Nikiforakis & Engelmann, 2011)].
- **Efficiency gains are conditional**: If the costs of assigning and receiving punishment are high relative to their cooperative benefit, **net group efficiency may not increase or may decrease**. Some institutions see *higher contributions but lower efficiency*, especially early in adaptation or in the presence of antisocial or emotional punishment [(Decker et al., 2003; Bochet et al., 2006; Tan, 2008)].

### b. **Institutional Detail is Critical**
- **Consensus-based or anti-antisocial punishment institutions** (e.g., requiring multiple group members to approve a sanction, or filtering antisocial punishment) yield **higher efficiency gains** than simple peer-based punishment ([Casari & Luini, 2009]).
- **The impact/cost ratio of punishment ("punishment_tech")** is a strong moderator: More efficient punishment (higher impact per unit cost) results in greater efficiency gains ([Sefton et al., 2007; Rigdon, 2009]).

### c. **Contextual Features Moderate Punishment’s Impact**
- **Communication** highly enhances cooperation and efficiency; punishment adds little marginal benefit when chat or face-to-face communication is allowed ([Bochet et al., 2006]).
- **Group size** and **heterogeneity** matter: In large groups, or groups with heterogeneous returns (privileged groups), the efficiency effect of punishment is smaller or mixed.\* Punishment may *increase inequality* sometimes ([Reuben & Riedl, 2009; Tan, 2008]).
- **Possibility of Counter-punishment (Feuds)**: Where punishment can be avenged or escalate, efficiency effects can reverse—feuds can lower both cooperation and payoff ([Nikiforakis & Engelmann, 2011]).

### d. **Centralized or Combined Sanctioning Systems Can Outperform Peer-only Punishment**
- Adding a centralized punishment mechanism ("leader", "third-party enforcement") or combining formal (monetary) and informal (social/shame) sanctions often yields higher efficiency than peer-only punishment ([Gürerk et al., 2009; Noussair & Tucker, 2005; Maier-Rigaud et al., 2010; Guillen et al., 2010]).

### e. **Punishment vs. Rewards**
- **Rewards alone** are less effective than punishment for sustaining high contributions or efficiency (\*often fading quickly\*), except when their impact ratio is net-positive ([Vyrastekova & van Soest, 2008; Sefton et al., 2007]).

### f. **Persistence and Time Dynamics**
- Punishment often shows **initial efficiency losses (due to heavy enforcement costs)**, which can shift to net gains as cooperation stabilizes and punishment becomes less frequent ([Sefton et al., 2007; Fehr et al., 2002]).
- **End-game effects** can erode efficiency improvements, unless institutional design insulates against unraveling.

### g. **Behavioral Mechanisms**
- Punishment is generally **targeted at defectors**, but levels and targeting are sensitive to group context and institutional detail. **Perverse punishment** (punishing cooperators) can erode or eliminate efficiency gains ([Bochet et al., 2006; Ones & Putterman, 2007]).

# 5) Prediction Guidance

- **Prediction should be based on matching game designs in the literature—especially on player_count, num_rounds, MPCR, punishment_cost/tech, and information structure.** Direct mappings (“exact” matches) should be weighted most heavily.
- **Enabling punishment generally increases efficiency compared to control** when:  
  - The cost/impact ratio is moderate or better (punishment_tech is not too low).
  - Punishment is targeted at defectors, *not* perverse, and feuds/antisocial punishment are rare.
  - The institution filters antisocial punishment and/or allows for consensus/cross-checking.
  - The group is homogeneous or baseline contributions are low.

- **Efficiency gains are often delayed** due to front-loaded punishment costs but may become substantial by the final rounds.
- **If the control (no-punishment) efficiency is already high**, punishment may have little effect or could even reduce net efficiency (due to unnecessary sanction costs).
- **Punishment effectiveness is markedly reduced or reversed** in:  
  - Highly heterogeneous groups (privileged players, variable MPCRs).
  - Designs permitting retaliation or counter-punishment (escalating feuds).
  - Large groups where punishment costs are too diffused.
  - Environments rife with anti-social punishment or if punishment cannot be properly targeted.
  - Designs with high “anonymity” and no feedback about punishers or recipients.
  - When chat or open communication is present, the added value of punishment for efficiency diminishes dramatically.

- For **adjacent and close variants** (CPR, trust games, minimum effort, real-world field studies), the basic *direction* of the punishment effect is similar: efficiency gains depend on cost/impact, institutional structure, and group features, but effect sizes and exact mappings must be treated cautiously.

- **Expert prediction**: Use empirical PGG studies with exact/close mapping for quantitative priors. Adjust prediction up for designs with consensus punishment, high punishment_tech, or combined sanctions; adjust downward for high-cost, low-impact punishment, opportunity for feuding, group heterogeneity, or evidence of anti-social punishment.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed for prediction:**
- `player_count`, `num_rounds`, `mpcr`, `punishment_cost`, `punishment_tech` —*Heavily reported and analyzed* (nearly all high-quality PGG studies).
- `chat` (communication) —*Directly manipulated and critical moderator for efficiency effects in several core papers*.
- `all_or_nothing` (binary vs. continuous contributions) —*Directly specified and occasionally analyzed across studies*.
- `reward_exists`, `reward_cost`, `reward_tech` —*Well represented as both moderating and alternative incentive structures*.
- `show_n_rounds`, `show_other_summaries` (information on rounds/others' payoffs) —*Often reported, but less systematically varied*.

**Indirectly or contextually informed:**
- `default_contrib` (framing/default) —*Occasionally discussed as opt-in/opt-out but not systematically varied across most studies*.
- `show_punishment_id` (punishment/reward identity) —*Often noted as "anonymous" or not shown, but design rarely varied*
- `show_other_summaries` —*Contextually important for targeting but not always systematically manipulated*.

**Effectively missing/infrequently addressed:**
- Some nuanced combinations (e.g., detailed interaction between showing punishment identity and chat; default contribution rarely a central design variable).
- Detailed cross-variation in `reward_tech` together with `punishment_tech` and full reward-punishment matrix experiments are rare.

# 7) Important Limitations

- **Efficiency effect is heterogeneous:** There is marked *variation across studies* in whether punishment improves, does not affect, or even lowers group efficiency—most often due to enforcement costs, institutional details (consensus vs. peer, centralized vs. decentralized), group heterogeneity, and anti-social punishment.
- **Not all design dimensions are independently or jointly varied:** Some dimensions (e.g., default_contrib, or simultaneous variation of communication + punishment + info) are not separably identified in most studies.
- **Payoff effects often timedependent:** Early rounds may see efficiency losses due to heavy punishment; only later rounds recoup gains. End-game and learning dynamics are only partially understood.
- **Behavioral results do not always map to payoff gains:** Many studies focus on increased contributions, which are often (but not always) associated with higher efficiency. The literature is explicit about cases when higher cooperation does NOT translate to higher payoff due to punishment cost.
- **Social/contextual moderators under-explored:** Variables such as pre-existing trust, culture, real-world group experience, or rare group types (very large or small, field environments) are not well represented in the core payoff literature.
- **Adjacency of centralized/CPR/trust games:** The clearest evidence comes from standard PGGs; many institutionally adjacent games (CPR, investment/trust, real-world resource dilemmas) demonstrate similar qualitative mechanisms but may not provide precise quantitative guidance for standard PGG predictions.
- **Dynamic institutional feedbacks:** Longer-term or post-game persistence of punishment effects (e.g., the "educational" effect of prior sanctions) is documented in some studies but is not systematically analyzed for predictive modeling.
- **Selective reporting:** Some studies report either behavioral or payoff outcomes but not both, limiting fully causal inference about the linkage between punishment, behavior, and efficiency.

---

**References (representative, not exhaustive):**  
Sefton et al., 2007; Gürerk et al., 2009; Noussair & Tucker, 2005; Casari & Luini, 2009; Nikiforakis & Engelmann, 2011; Bochet et al., 2006; Reuben & Riedl, 2009; Decker et al., 2003; Tan, 2008; Kroll et al., 2007; Fehr et al., 2002; Maier-Rigaud et al., 2010; Rigdon, 2009; Vyrastekova & van Soest, 2008; Ones & Putterman, 2007; Casari & Plott, 2003; Ostrom, 2006.

---

## In summary:
- **The evidence base is strong and directly relevant** for predicting punishment effects on efficiency in PGG-like environments, with clear evidence that *design dimension details and context matter critically*.
- **Punishment generally increases efficiency over control under favorable design and context**, but not universally.
- Predictive modeling **must condition on institutional details and baseline (no-punishment) efficiency**.
- **Key moderating design dimensions**—such as punishment_tech, punishment_cost, communication, institutional structure—are well covered; others less so.
- **Ambiguity and heterogeneity** in findings remain, especially around anti-social punishment, group size, heterogeneity, and end-game dynamics.
