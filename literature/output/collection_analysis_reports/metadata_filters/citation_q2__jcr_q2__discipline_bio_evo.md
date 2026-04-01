# 1) Evidence Base

The paper set is a mixed collection of empirical (lab and field), observational, and theoretical works, with significant heterogeneity in paradigm closeness to public goods games (PGG) and the kind of punishment or sanctioning studied. Only a minority of papers are both theoretically and empirically grounded in standard PGG designs with clear, measurable efficiency or group payoff outcomes (e.g., Eldakar et al., 2013; Javaid & Falk, 2015). Several papers explore behavioral outcomes, evolutionary arguments, neural mechanisms, or adjacent economic games (such as trust games, common-pool resource games, or animal analogs), which provide contextual or mechanistic insight but less direct evidence for the downstream prediction task. The evidence base is therefore somewhat broad, conceptually diverse, and relatively sparse in direct, empirical studies of efficiency effects of enabling punishment in public-goods-like environments.

# 2) Task Relevance

**PGG or Variant**:  
- *exact relevance*: A subset of papers use canonical PGG designs (Eldakar et al., 2013; Bone et al., 2014; Li et al., 2018; Frey, 2019).
- *close/adjacent relevance*: Others employ CPR games or trust games with related but not identical structure and payoff logic (Javaid & Falk, 2015; Perez et al., 2015; Baum et al., 2012).

**Punishment or Sanctions**:  
- *exact relevance*: Several studies feature explicit, manipulative punishment or sanctioning opportunities (Eldakar et al., 2013; Bone et al., 2014; Javaid & Falk, 2015; Konishi & Ohtsubo, 2015).
- *adjacent/weak relevance*: Some discuss punishment as a concept or observe endogenous/indirect forms (e.g., enforcement via communication in Perez et al., 2015; aggression as punishment in Bshary & Bshary, 2010; evolutionary discussions in Bateson, 2014).

**Efficiency or Related Payoff Outcome**:  
- *exact/close relevance*: Very few report group efficiency, payoff, or related welfare metrics as the main outcome (Eldakar et al., 2013; Javaid & Falk, 2015).
- *adjacent/none*: Most others focus on behavioral outcomes (contribution, punishment assignment, norm compliance) or evolutionary survival, rather than actual group efficiency or total earnings (Bone et al., 2014; Li et al., 2018).

**Summary**:  
The literature directly informs the prediction task only in a small subset of studies, while the rest provides adjacent evidence mainly about the mechanisms governing cooperation and punishment or context for interpreting observed effects.

# 3) Outcomes Measured In The Literature

- **Payoff-Based Outcomes** (*directly relevant*):  
  - *Group efficiency* (ratio of realized to optimal payoffs) and total group payoff are primary in Eldakar et al. (2013, theory) and Javaid & Falk (2015, empirical), and to a lesser extent in Perez et al. (2015, via group success).
  - Some studies measure related metrics (earnings, surplus) but stop short of reporting efficiency (Javaid & Falk, 2015).
- **Non-Payoff Behavioral Outcomes** (*not equivalent to efficiency*):  
  - Most frequently: contribution rates, cooperation rates, punishment/reward rates, norm compliance, partner choice, enforcer presence (Bone et al., 2014; Li et al., 2018; Perez et al., 2015; Baum et al., 2012; Konishi & Ohtsubo, 2015).
  - Neural and evolutionary markers (Miraghaie et al., 2022; Inglis et al., 2014; Bateson, 2014).
- **Absence of Key Outcomes**:  
  - Several studies report no payoff, efficiency, or group welfare data (Smith et al., 2022; Leighton, 2014).

# 4) Main Findings Relevant To Prediction

**(a) When direct efficiency or group payoff is measured:**
- *Punishment increases efficiency when design conditions are right.*  
  - Theoretical modeling (Eldakar et al., 2013) shows that punishment typically raises group efficiency in PGGs, especially when: (i) punishment costs are low, (ii) group size is small, (iii) interactions are repeated (more rounds). The transition from selfish to altruistic punishers further amplifies efficiency gains.
- *Punishment can decrease efficiency when baseline is high.*  
  - Field evidence in a CPR game (Javaid & Falk, 2015) shows that when baseline efficiency is already high (due to local norms and social information), costly, probabilistic punishment can lower group efficiency by causing resource wastage and new coordination problems.

**(b) When behavioral or mechanistic outcomes are measured:**
- *Punishment is predominantly targeted at defectors, not norm-violators per se* (Bone et al., 2014), but the efficiency effect is unknown.
- *Informal enforcement and leadership may correlate with group conflict, not group success* (Perez et al., 2015); the presence of enforcers does not guarantee efficiency gains.
- *Repeated interaction and smaller group size favor effective punishment* (Bshary & Bshary, 2010; Eldakar et al., 2013), but these are findings about the usage of punishment, not its efficiency effect.

**(c) Mechanistic and evolutionary insights:**
- *Effectiveness of punishment is contingent on linkage between punishment and cooperation* (Inglis et al., 2014); without such linkage, gains to group outcome are not guaranteed.
- *Inter-group, cross-identity, or evolutionary variation can alter the effects or necessity of punishment* (Baum et al., 2012).

# 5) Prediction Guidance

- **Strongest guidance** comes from Eldakar et al. (2013):  
  *Enabling peer punishment in a standard PGG is theoretically predicted to increase group efficiency, provided punishment costs are low, group size is small, and interactions are repeated. The benefit is weaker (or may reverse) as punishment cost increases, group size grows, or the game is one-shot or has few rounds.*
- **Empirical modifier** from Javaid & Falk (2015):  
  *If the efficiency in the no-punishment condition is already high (e.g., due to public feedback or strong local norms), adding costly punishment may not improve—and can sometimes reduce—efficiency, especially if the punishment system is costly, probabilistic, or poorly targeted.*
- **Behavioral/adjacent evidence:**  
  Suggests that punishment is often accurately targeted at defectors and that mere assignment of sanctioning roles or indirect forms of enforcement (e.g., via communication) does not guarantee efficiency improvement.

- **Design-dependent expectations:**  
  High baseline efficiency and well-functioning informal enforcement (i.e., with public information and strong social norms) reduce or reverse the efficiency gains from enabling punishment.

- **No empirical guidance** exists in this paper set for settings involving reward mechanisms (reward_exists, reward_cost, reward_tech), chat, identity revelation, or all-or-nothing contribution framing.
 
# 6) Design Dimensions Highlighted Across Papers

- **Directly Informed Dimensions:**
  - `player_count` (most studies, empirically and theoretically): Small group size more conducive to positive punishment effects.
  - `num_rounds` (several studies): More repeated rounds increase efficacy of punishment (Eldakar et al., 2013).
  - `mpcr` (public goods marginal return; several studies report but rarely manipulate effect).
  - `punishment_cost` (key variable in Eldakar et al., 2013; Javaid & Falk, 2015): Lower cost increases efficiency gains from punishment.
  
- **Indirectly Informed/Contextual Dimensions:**
  - `all_or_nothing` (some mention; impact not systematically evaluated).
  - `chat`, `show_n_rounds`, `show_other_summaries` (contextual; some papers note the presence of communication, but direct impact on efficiency returns from punishment is not quantified).
  - `punishment_tech` (occasionally discussed, as "mechanism"/"technology"—not systematically tested).
  - `default_contrib` (framing is reported but effects on efficiency modulated by punishment are not measured).

- **Sparse or Missing:**
  - `reward_exists`, `reward_cost`, `reward_tech`, `reward_magnitude` (rare or not manipulated alongside punishment).
  - `show_punishment_id` (identity revelation of punishers/rewarders rarely addressed).
 
- **Summary:**  
  Only the basic PGG structural elements—player count, number of rounds, MPCR, and punishment cost—are consistently analyzed for their effect on punishment's impact on group efficiency. All other design parameters are discussed as context or control variables, not as testable moderators of punishment effects on efficiency within this paper set.

# 7) Important Limitations

- **Empirical sparseness:**  
  Very few studies report both (a) efficiency metrics and (b) experimental manipulation of punishment in public goods contexts.
  
- **Variability in design and outcome reporting:**  
  Studies differ in the mapping to the PGG paradigm, the type of punishment (peer vs. third-party, probabilistic vs. deterministic, endogenous vs. exogenous), and the nature of measured outcomes (payoff vs. behavioral).
  
- **Generalizability concerns:**  
  The efficiency-increasing effect of punishment is best-supported by a theoretical model (Eldakar et al., 2013) and a limited number of field/lab studies. Contexts with strong local norms or high baseline efficiency weaken or even invert this effect (Javaid & Falk, 2015).
  
- **Payoff vs. behavioral outcome confusion:**  
  Most papers measure behavioral or psychological outcomes (e.g., rates of contribution, norm compliance) rather than efficiency or group payoff, which makes direct prediction of efficiency effects hazardous if one naively extrapolates from behavioral to payoff-level data.
  
- **Missing or weak treatment of key dimensions:**  
  Only four of fourteen design dimensions (player count, num rounds, MPCR, punishment cost) are robustly covered. Mechanisms involving reward, information structures around punishment, and communication are generally not assessed in terms of their interaction with efficiency returns from punishment.

- **Ambiguity and conflicting results:**  
  Evidence suggests the effect of enabling punishment is not always positive for group efficiency and may depend critically on the initial efficiency (control condition), cost structures, and the presence of other strong norm-enforcing mechanisms.

---

**In summary:**  
For the prediction of average efficiency in public goods games when enabling peer punishment, the literature most strongly supports a positive effect of punishment under design conditions of small groups, multiple rounds, low punishment costs, and low control efficiency. However, where baseline efficiency is high (perhaps due to public information or strong norms), introducing costly punishment can reduce efficiency. Most design dimensions relevant to PGGs are only sparsely or contextually addressed in this paper set. The literature is richer in behavioral results and mechanism discussions than in direct, quantitative efficiency outcomes. Predictions should take into account the limited direct empirical foundation and substantial contextual dependency.
