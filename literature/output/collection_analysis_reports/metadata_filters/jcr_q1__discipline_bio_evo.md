# 1) Evidence Base

The paper set is large (200 papers) and features a rich blend of **empirical laboratory and field experiments** (including many lab-based public goods games (PGG) with and without punishment), as well as **theoretical and simulation studies**. The literature is **broad and diverse**, encompassing classic, linear PGGs; threshold and common-pool resource (CPR) games; variants involving institutional and peer punishment, reward, exclusion, and combinations with reputation or communication. Numerous papers explicitly measure **payoff-based efficiency outcomes**, while others focus on behavioral outcomes (cooperation, punishment rates, norm compliance) or discuss mechanisms, evolutionary dynamics, or sociocultural moderators.

**A subset of papers (both empirical and theoretical) provide exact or close matches** to the downstream prediction task: estimating average efficiency in PGG-like games with peer punishment, given game design and control efficiency. Many others address adjacent outcomes or game types (e.g., third-party punishment, CPRs, reward systems, indirect reciprocity, or observational/ethnographic data) and thus provide useful but less direct insight.

# 2) Task Relevance

**Relevance by Dimension:**

- **pgg_or_variant:**  
  - *Exact:* A significant number of empirical and theoretical studies exactly match the standard PGG or close symmetric n-player public goods game. Many others use clear close variants (CPR games, threshold games, repeated Prisoner's Dilemmas, etc). A minority address only adjacent games (dictator, trust, ultimatum, etc.).
- **punishment_or_sanctions:**  
  - *Exact or close:* Many papers provide direct empirical evidence on peer or institutional punishment, often matching or closely approximating the prediction task's design (costly, decentralized, peer, or institutional punishment implemented as a treatment vs. control). Others focus on social exclusion, reward, third-party punishment, indirect sanctions, or observational/ethnographic evidence, which are “close” or “adjacent” but not always structurally identical. A minority only discuss punishment conceptually, or not at all.
- **efficiency_or_related_payoff_outcome:**  
  - *Exact or close:* Several high-value empirical and theoretical papers directly report group efficiency (total payoff relative to full cooperation), group earnings, welfare, or directly analogous measures. Many others, while not reporting efficiency per se, address group payoff, surplus, resource stock, or disaster avoidance—providing *close* proxies. Many papers, however, report only indirect or behavioral outcomes (contribution rate, norm compliance, punishment assigned), which are not exact but often allow cautious inference about efficiency. Some notable papers explicitly show that higher cooperation does not always imply higher efficiency.

**In summary:**  
The set is **highly relevant overall**, containing many *exact* and *close* matches, but key theoretical and contextual papers address *adjacent* questions or rely on non-payoff outcomes, which must be carefully distinguished. There is ample data for synthesis on the core prediction task—but context and moderators often matter critically.

# 3) Outcomes Measured In The Literature

- **Payoff-based Outcomes (directly relevant):**
  - *Efficiency* (payoff divide by social optimum)
  - Group total payoff, earnings, welfare, surplus
  - Resource sustainability (CPR games)
  - Disaster avoidance rates (threshold/collective risk PGGs)
  - Achievement of public good/provision level/success probability

- **Non-payoff Behavioral Outcomes (indirectly relevant):**
  - Contribution/cooperation rates
  - Rates and magnitude of punishment given/received
  - Norm compliance, antisocial punishment
  - Inequality, variance in contributions/earnings
  - Evolutionary stability, strategy frequencies

- **Key distinctions:**
  - Many studies **explicitly demonstrate** that increases in cooperation/contribution do *not always* translate to increases in efficiency, due to the direct costliness or misapplication of punishment (e.g., Egas & Riedl, 2008; Nhim et al., 2023; Grimalda et al., 2022).
  - Studies with mixed or partial outcome reporting require cautious interpretation: when efficiency is not reported but contribution or cooperation is, conclusions must not be overreached.

# 4) Main Findings Relevant To Prediction

## Empirical and Simulation Evidence

- **Punishment as a Double-Edged Sword:**
  - In standard linear PGGs with moderate MPCR and typical punishment cost/tech, *allowing costly peer punishment increases cooperation but does not reliably increase efficiency*: the costs of administering punishment often outweigh the gains from increased contributions (Egas & Riedl, 2008; Sääksvuori et al., 2011; Burton-Chellew & Guérin, 2021). In several cases, group efficiency with punishment is observed to be *lower* than control (no-punishment), especially as anti-social punishment or redundant punishment is common.
  - When **punishment is cheap and highly effective**, efficiency gains are possible, especially when punishment is rarely needed (O'Gorman et al., 2009; Gächter et al., 2017). The efficiency boost is greatest when cooperation is otherwise fragile and punishment is used mainly as a threat.

- **Contextual Factors Moderating Punishment’s Efficiency Effect:**
  - **Intergroup competition**: Key for unlocking efficiency gains from punishment. In the absence of group competition, punishment rarely improves efficiency; with competition, it can have large positive effects (Sääksvuori et al., 2011; Puurtinen & Mappes, 2009).
  - **Institutional punishment**: Centralized or coordinated punishment regimes (e.g., institutionally managed, “pool punishment,” minimum contributions/tax with enforcement) have mixed effects—sometimes strongly increasing efficiency if designed well, but sometimes reducing it if punishment costs are high or if crowding-out occurs (Nhim et al., 2023; Dong et al., 2019; Vollan, 2008).
  - **Punishment technology and design**: One designated punisher avoids redundancy and is more efficient than allowing all players to punish (O’Gorman et al., 2009). Second-order punishment (punishing non-punishers) can stabilize cooperation but often at high cost to efficiency (Traulsen et al., 2012).
  - **Cultural, normative, and trust context**: Efficiency effects depend on the prevalence of anti-social punishment, social trust, cultural background, and whether punishment is self-determined or externally imposed (Gächter et al., 2010; Vollan, 2008; Guala, 2012; Castillo et al., 2011).
  - **Synergy/MPCR**: Higher marginal per capita returns (MPCR), and the ability of punishment to bring systems near critical cooperation thresholds, are strong predictors of potential efficiency gains (Adami et al., 2016; Brandt et al., 2003). In non-linear or threshold PGGs, context and parameterization matter even more.
  - **Reward versus punishment**: Reward generally produces greater efficiency gains than punishment for comparable investments, especially when players are error-prone (Dong et al., 2019; Rand & Nowak, 2013).
  - **Complementarity with reputation/communication**: Combining punishment with reputation, communication, or coordination mechanisms can increase efficiency, both by reducing the need for costly punishment and by making enforcement more effective (Milinski, 2016; Sigmund, 2007; Dos Santos et al., 2011).

- **Variants and Special Cases:**
  - **Social exclusion (ostracism)**: Acts as a low-cost, high-effectiveness punishment; shows robust efficiency gains in laboratory PGGs with group formation (Sasaki & Uchida, 2013; Sääksvuori, 2014).
  - **CPR and field settings**: External, monitored punishment can reliably raise efficiency in resource games with real-world users (Wegmann & Musshoff, 2019); but effects are context-dependent—crowding-out occurs if trust is high and punishment is externally imposed (Vollan, 2008).
  - **Threshold/collective risk games**: Punishment often raises cooperation (probability of group success) but may still lower efficiency due to cost (Grimalda et al., 2022).
  - **Partner choice and network structure**: Reduces need for punishment; can increase efficiency to levels equal to or greater than environments with punishment (Graser et al., 2025; Helbing et al., 2010).

## Theoretical and Evolutionary Mechanism Arguments

- **Meta-incentives and higher-order sanctions**: Stable high efficiency typically requires not just first-order punishment, but also second-order sanctions (punishing non-punishers; Okada et al., 2015).
- **Group size and scalability**: Punishment effectiveness and the efficiency benefit both tend to decrease with larger group size unless institutional/centralized mechanisms, hierarchy, or group structuring supplement peer sanctions (Powers et al., 2023; Powers & Lehmann, 2017). Small groups are more responsive to peer punishment.
- **Reputation and observability**: If punishment is visible and can be incorporated into reputational updating, it is more likely to deliver efficiency gains (Dos Santos et al., 2011; Hilbe & Sigmund, 2010).
- **Ecological and resource dynamics**: In CPR/renewable resource games, the effect of punishment is capped by ecological constraints; if the growth rate is too low or resource feedback negative, punishment cannot restore efficiency (Wang et al., 2024; Chen & Szolnoki, 2018).

## Key Consistencies and Disagreements

- **General Patterns:** 
  - Punishment increases cooperation more reliably than efficiency.
  - The potential for efficiency gains from punishment is highest when (a) baseline (control) efficiency is low, (b) punishment is cheap and effective, and (c) game structure, social, or institutional context support coordination.
  - The cost structure and type of punishment (peer, pool, exclusion), alongside cultural/trust context, decisively moderate efficiency outcomes.

- **Contradictions:** 
  - Disagreement on whether, in standard lab PGGs, costly punishment is on net efficiency-destroying (Egas & Riedl, 2008; Burton-Chellew & Guérin, 2021) or (sometimes) efficiency-improving (Gächter et al., 2017; O'Gorman et al., 2009). The divergence is explained by differences in punishment technology, MPCR, presence/absence of reputation, group competition, and cultural context.

# 5) Prediction Guidance

**For the downstream task—predicting efficiency in a PGG/variant when peer punishment is enabled, given game design and control efficiency—the literature supports the following structured guidance:**

- **Baseline efficiency (control condition) is a crucial predictor:** If control efficiency is already high (close to the social optimum), enabling punishment is less likely to improve and may reduce efficiency (due to punishment costs).
- **Game design dimensions most strongly moderating the punishment effect:**
  - *punishment_cost (and cost-to-impact ratio):* Lower cost/more effective punishment = greater chance of efficiency gain.
  - *player_count and group size:* Smaller groups → stronger/clearer positive effects; larger groups → weaker effects unless institutional mechanisms are present.
  - *mpcr (synergy):* Efficiency gains from punishment are concentrated near the critical threshold(s) for cooperation; in high-MPCR environments, gains are limited if efficiency is already high.
  - *institutional features:* Centralized/institutional punishment, especially when group-selected or coordinated, tends to be more efficient than uncoordinated, redundant peer punishment.
  - *frequency and transparency of information (show_other_summaries, show_punishment_id):* Visible outcomes and punishment/reward actions favor efficient targeting and may reduce unnecessary punishment.
  - *intergroup competition:* Presence of between-group competition or ecological risk scenarios (e.g., competitive resource depletion) is a strong positive moderator.
  - *reward_exists and reward_cost/tech:* Enabling well-designed rewards may be more effective than punishment for raising efficiency, particularly when decision errors are likely.

- **Negative and cautionary cases:**
  - High rates of anti-social punishment, redundancy (multiple punishers), or non-aligned institutional rules (lack of buy-in, high-trust/crowding-out effects) may erase or reverse efficiency gains from punishment.
  - Punishment tends to be efficiency-reducing when either (a) the behavioral boost is small or limited to a minority of defectors, or (b) the punishment cost is substantial relative to group gains from increased cooperation.

- **When prediction is ambiguous:**
  - If the literature only reports behavioral outcomes (not efficiency), or efficiency results vary widely with context, the prediction should preserve this ambiguity.
  - Empirical cases frequently report that design dimensions alone are not always sufficient—sociocultural context and group-level variables (norms, trust, history, cultural baseline rates of antisocial punishment) can significantly alter outcomes (Gächter et al., 2010; Vollan, 2008).
  - The mapping from control efficiency to treatment efficiency is not always linear; sometimes efficiency is even lower with punishment, despite higher cooperation.

**Summary Statement:**  
**Enabling peer punishment in PGG-like environments typically raises group efficiency only if (i) the control efficiency is low, (ii) punishment is cheap and effective, (iii) design supports coordination or institutionalization, and (iv) antisocial or redundant punishment is limited. Otherwise, punishment may raise cooperation but not efficiency, or could even reduce efficiency via wasteful expenditure or norm backlash.**

# 6) Design Dimensions Highlighted Across Papers

**Well-Informed Dimensions:**
- **player_count**: Group size is universally reported, with strong evidence for its moderating role.
- **num_rounds**: Repetition and time horizon are core to both empirical and theoretical studies, modulating punishment effectiveness and efficiency gains.
- **all_or_nothing**: Most studies specify whether contributions are continuous or binary—binary/all-or-nothing games often show more dramatic treatment effects and sharper efficiency declines with punishment cost.
- **mpcr**: Marginal per capita return (synergy) is one of the most thoroughly analyzed moderators.
- **punishment_cost and punishment_tech**: Almost always clearly specified; the cost-to-impact ratio is repeatedly shown to be pivotal in efficiency outcomes.
- **reward_exists and reward_cost/tech**: Less universally manipulated, but several direct theoretical and empirical studies provide comparative evidence to punishment.
- **chat (communication)**: Many studies manipulate communication and show its positive (and sometimes substitutive) effect on both cooperation and efficiency.
- **show_n_rounds, show_other_summaries, show_punishment_id**: Some studies specify and manipulate these, particularly in contexts involving reputation and visibility.

**Sparsely or Indirectly Addressed Dimensions:**
- **default_contrib**: Opt-in vs. opt-out framing is generally not a primary design variable in the literature.
- **show_punishment_id**: Not commonly a main treatment—its impact is mainly inferred from studies on reputation/observability.
- **contextual moderators not formalized in prediction variables**: Group voting/self-determination, cultural context, local norm compatibility, or history of prior cooperation/trust.

# 7) Important Limitations

- **Control efficiency is highly predictive, but not always sufficient alone:** Identical design dimensions can yield divergent outcomes depending on unmeasured sociocultural or psychological moderators (culture, trust, history, antisocial punishment, buy-in).
- **Many studies report contribution/behavioral outcomes but not efficiency:** Care must be taken not to equate increased cooperation with increased efficiency; overgeneralization from behavioral to payoff outcomes is unsupported by the literature.
- **Static design dimensions can miss critical context:** Important moderators such as legitimacy/self-determination of institutional rules, communication quality, and antisocial punishment are not always captured by the standard 14 design dimensions.
- **Heterogeneity in punishment implementation:** "Punishment" varies (peer vs. institutional, monetary vs. exclusion, first- vs. second-order, visibility, etc.), and results are not always directly comparable. Peer punishment and pool punishment may yield different efficiency effects depending on context.
- **Limited generalizability across game types:** Inferences from field CPR studies, threshold games, third-party punishment, or evolutionary simulations often require caution when transferring to canonical PGGs.
- **Winner’s curse in well-performing control games:** When control (no-punishment) efficiency is already close to maximum, setting-based or parameter-based predictions may overstate the benefit of enabling punishment.
- **Publishing and reporting bias toward significance:** Null or negative results for punishment on efficiency may be underreported in the literature relative to positive behavioral effects.
- **Not all design dimensions are orthogonally varied or jointly manipulated:** Many studies report fixed values or confound treatments, limiting direct estimation of interaction effects among dimensions.

---

**In summary, this literature base is broad, deep, and contains many exact and close matches for the prediction task, but prediction of efficiency gains from enabling punishment in PGG-like games must always be contextual, attentive to design details, and cautious about over-reliance on behavioral proxies or unmeasured moderators.**
