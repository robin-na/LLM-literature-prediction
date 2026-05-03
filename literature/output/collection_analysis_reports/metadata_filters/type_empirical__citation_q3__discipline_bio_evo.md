# 1) Evidence Base

The 32-paper set is predominantly **empirical**, heavily weighted toward experimental (lab or field) studies, with some observational work and very limited theory. The literature is moderately broad in encompassing a variety of environments—standard public goods games (PGG), close variants (e.g., common-pool resource games, trust/dictator/ultimatum games), mutualism analogies (animal behavior studies), and trust-based economic games. 

However, **the set is quite narrow** concerning the exact downstream prediction task: very few studies measure or report **group efficiency or related payoff-based outcomes** for PGGs with and without peer punishment. Most literature focuses on behavioral outcomes (contribution, cooperation, punishment behavior, norm compliance) rather than direct efficiency (total payoff compared to full cooperation). Papers with exact match to efficiency outcomes in PGG settings are rare; only a handful (e.g., Vollan et al., 2013; Fonseca & Peters, 2021; McClung et al., 2017) report efficiency-related metrics, and often outside a standard PGG with punishment manipulation.

Summarily, the evidence base offers **rich behavioral insight but sparse direct efficiency data** under precisely the conditions specified in the prediction task.

# 2) Task Relevance

## `pgg_or_variant`
- **Label:** Mostly `exact` or `close`  
A majority of the experimental papers use standard PGGs or close analogues (common-pool resource or threshold games). Some studies employ related paradigms (trust, dictator, or ultimatum games) and animal mutualism analogues, which are `adjacent`.

## `punishment_or_sanctions`
- **Label:** About half `exact` (real, costly punishment manipulations), some `adjacent` or `weak`
Several studies implement actual peer or centralized punishment (`exact`), while others consider social sanctions, threat of punishment, or analogues in other paradigms (`adjacent`). A substantial number omit punishment entirely (`none` or `weak`).

## `efficiency_or_related_payoff_outcome`
- **Label:** Most are `adjacent` or `weak`  
True payoff-based group-level outcomes (efficiency, total earnings, surplus) are directly measured in only a small subset (`exact`). The majority measure individual behavior, contribution rates, or cooperation (`adjacent`), or provide only contextual payoff information.

# 3) Outcomes Measured In The Literature

## **Payoff-Related Outcomes**
- **Direct group efficiency/total payoff:** Rare; reported in a minority of papers (e.g., Vollan et al., 2013; Fonseca & Peters, 2021; McClung et al., 2017)
- **Proxy payoff/welfare metrics:** Some studies provide related or theoretical measures but do not empirically analyze them as main outcomes (e.g., theoretical efficiency benchmarks in Gatiso et al., 2015)

## **Non-Payoff Behavioral Outcomes**
- **Contribution rate / cooperation frequency:** The primary dependent variable in most PGG experiments (e.g., Skatova & Ferguson, 2013; Schroeder et al., 2015)
- **Punishment frequency/amount, norm compliance, or compliance with rules:** Common in both human and animal studies (e.g., Molleman et al., 2019; Raihani et al., 2012)
- **Emotion and motivation behind punishment:** Assessed in a subset (e.g., Seip et al., 2009; Marlowe et al., 2011)
- **Communication and reputation dynamics:** Measured in studies focused on gossip and information transmission (Jolly & Chang, 2021; Fonseca & Peters, 2021)

# 4) Main Findings Relevant To Prediction

**The principal empirical regularity** is that **enabling peer punishment increases average cooperation or contribution rates** relative to punishment-disabled controls in laboratory PGGs (Skatova & Ferguson, 2013; Schroeder et al., 2015). This increase in cooperation is robust across one-shot and repeated games, is further moderated by player characteristics (e.g., extraversion, expectations), and can occur through both implemented and merely expected punishment. However, **studies rarely report the net effect on efficiency**, leaving uncertain whether the cost of administering punishment outweighs or is outweighed by the gross gains in cooperation.

In a handful of studies that report or closely analyze **efficiency or related payoff outcomes**:
- **Vollan et al. (2013)** show that top-down, impersonal rule-based interventions (quota, rotation, lottery) have **variable effects on efficiency**, depending on group ecological norms and prior coordination. Rules aligned with existing norms increase efficiency, while those in conflict may decrease it.
- **Fonseca & Peters (2021)** demonstrate that **dishonest or inconsistent social sanctions** in gossip-based trust games reduce efficiency, as they can fail to align with true honesty or cooperative intent.
- **McClung et al. (2017)** (though without punishment) show that efficiency can be increased by enabling communication and fostering group identity, pointing to possible ceiling effects for additional interventions.

Studies in animal behavior or other paradigms indicate that **punishment can reliably induce short-run increases in cooperation by subordinates** when delivered by dominants (Raihani et al., 2012; Bshary & Bshary, 2010), **but these cooperation gains are often short-lived and not always accompanied by long-run increases in total benefit**.

A critical **mechanism finding** is that the **effectiveness of punishment in raising efficiency (as opposed to cooperation rates) is contextually conditional**. Effectiveness depends on:
- The **cost of punishment** and whether it is well-targeted to true norm violators (Fonseca & Peters, 2021; Vollan et al., 2013)
- The **method of sanction implementation** (e.g., democratic elections vs. top-down imposition), with elections being more effective (Gatiso et al., 2015)
- The **alignment of formal sanctions with informal group norms** (Vollan et al., 2013)
- The **integrity or trustworthiness of punishers**, especially in third-party roles (Spadaro et al., 2023; Zhang et al., 2016)
- The **information environment**: social communication can both aid and hinder efficiency, depending on honesty and trust dynamics (Jolly & Chang, 2021; Fonseca & Peters, 2021)

# 5) Prediction Guidance

**The most robust prediction from this evidence base is that enabling peer punishment in a PGG generally increases average contribution rates** above punishment-disabled controls. However, **due to the costliness of punishment, the impact on efficiency is ambiguous:** 

- **If punishment is well-targeted, low-cost, and aligned with shared group norms or democratic participation**, efficiency gains are more likely (Vollan et al., 2013; Gatiso et al., 2015).
- **If punishment is costly, misapplied, or perceived as illegitimate,** efficiency gains can be negated or reversed (Vollan et al., 2013; Spadaro et al., 2023; Fonseca & Peters, 2021).

**Given the lack of direct empirical efficiency data for classic PGGs with and without punishment**, predictions must make use of:
- **Control game efficiency (average baseline payoff):** Punishment creates opportunities for higher efficiency by deterring free riding, but only if the cost of sanctioning is less than the additional surplus generated.
- **Design dimensions:** 
    - **Low punishment cost and high punishment impact** are more likely to increase efficiency.
    - **Coordinated or democratic punishment mechanisms** are more effective than top-down.
    - **Transparency (e.g., punishment identity revealed) and information flow** can aid or undermine the effect, depending on whether they induce prosocial use of punishment.
    - **Alignment with group norms** strongly moderates effects.
- **Player count and round number** matter contextually (e.g., repeated games enable reputation).
- **Chat and communication** can substitute for formal sanctions in sustaining cooperation—thus, the marginal effect of enabling punishment is greatest in games without communication channels.

**Predictions should be made with caution:** In the absence of precise payoff data, behavioral proxies suggest that efficiency will increase with punishment only if punishment costs do not outweigh the value of enforced cooperation. In PGGs with moderate control-game efficiency, enabling punishment yield is likely to generate moderate additional efficiency; in already highly efficient groups, marginal returns will be lower and punishment may be wasteful or even maladaptive.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- `player_count`, `num_rounds`, `mpcr`, `all_or_nothing`: Widely reported and manipulated in exact or close PGG studies.
- `punishment_cost`, `punishment_tech`: Studied in most PGGs with punishment; variations in cost and technology are shown to matter.
- `chat`: Reported/measured in many studies, especially those on communication/gossip (Jolly & Chang, 2021; McClung et al., 2017); shown to affect cooperation.
- `show_other_summaries`, `show_n_rounds`: Included in several PGG protocol descriptions.

**Indirectly or Contextually Discussed:**
- `show_punishment_id`: Rare; sometimes discussed in animal studies or those on social information transmission.
- `reward_exists`, `reward_cost`, `reward_tech`: Present in a minority of studies (Wang et al., 2023; Burum et al., 2020), but not as primary variables in PGG with punishment.
- `default_contrib`: Mostly a matter of experimental instructions; little evidence that framing from opt-in/opt-out alone shapes efficiency (where measured).

**Effectively Missing:**
- Some technical implementation dimensions (e.g., fine gradations of `punishment_tech`, details of `reward_tech` or `reward_magnitude`) are sparsely discussed.
- Interactions between multiple dimensions (e.g., how `chat` interacts with `show_punishment_id`) are rarely explored systematically.

**Notably, only a few studies provide mappings between these design features and actual efficiency outcomes with and without punishment.**

# 7) Important Limitations

- **Very limited direct evidence on (treatment vs. control) efficiency effects** of punishment in exact PGG environments; most studies focus on behavioral proxies.
- **Few studies report both control and treatment efficiencies,** necessary for the prediction task.
- **Strong context dependence:** Efficiency outcomes depend heavily on local norms, sanction implementation, player psychology, and the information environment; effects are rarely robust across contexts.
- **Cost of punishment is often omitted or unclear:** Many studies document increased cooperation but do not subtract the cost of sanctioning to compute net efficiency.
- **Mechanism vs. outcome gap:** Rich theoretical and mechanistic discussion of why and how punishment works, but few quantified results on efficiency gains vs. losses.
- **Sparse evidence on some design dimensions** (reward, identity, default contribution framing, multi-stage transparency) and their interactions.
- **Animal behavior and ethnography studies provide valuable context but do not measure group efficiency,** limiting their predictive power for human lab PGGs.
- **Potential publication and field bias:** The most widely studied cases may not represent the full range of possible game designs or real-world environments.

### **Conclusion**

**For prediction tasks, this literature suggests moderate, context-dependent efficiency gains from enabling peer punishment—but with high uncertainty, driven by the specifics of cost structure, implementation, and group context.** Predictions require careful calibration and should be contextualized with the limited empirical support for direct efficiency outcomes. Where behavioral proxies (contributions, cooperation) are used, one must explicitly acknowledge that these may not translate linearly to net efficiency due to the costs associated with punishment.
