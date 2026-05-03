# 1) Evidence Base

This literature set includes 9 papers, all empirical, with a heavy emphasis on laboratory experimental work, plus one observational field study. Most experiments use non-PGG environments closely related to social dilemmas—namely, ultimatum games, prisoner's dilemmas (PD), dictator games, principal-agent settings, and market exchange games rather than canonical public goods games (PGG). The set is broad in covering a variety of social dilemmas and punishment/reward mechanisms but is narrow with respect to direct evidence on efficiency changes in actual public goods games with peer punishment enabled or disabled. The focus is more on mechanisms, behavioral responses, and indirect evidence rather than on direct measurement of efficiency in the PGG with punishment context required by the prediction task.

# 2) Task Relevance

**pgg_or_variant:**  
- *Relevance: adjacent (none exact)*  
  None of the included studies are direct empirical tests of repeated PGGs with peer punishment. All investigate adjacent designs such as repeated ultimatum, market exchange, PD, principal-agent, or dyadic repeated games. The behavioral, mechanism, and outcome findings are contextually relevant but not direct substitutes for canonical PGG evidence.

**punishment_or_sanctions:**  
- *Relevance: exact to adjacent*  
  Punishment or sanctioning mechanisms are a primary focus, with most papers enabling some form of punitive action (peer punishment, rejection, firing, etc.). At least one paper each describes punishment as its sole treatment of interest.

**efficiency_or_related_payoff_outcome:**  
- *Relevance: sparse, mostly adjacent or weak, two papers exact*  
  Most papers report behavioral outcomes (e.g., contribution/cooperation rate, honesty/slack reduction, punishment frequency), not group payoff or efficiency. Only two papers directly report efficiency/welfare (Abbink et al., 2004; Brown et al., 2004); others provide adjacent or speculative links between behavioral outcomes and payoff, but do not quantify group efficiency.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes (efficiency, group payoff, total earnings):**
- *Directly measured:*  
  - Efficiency: Abbink et al. (2004); Brown et al. (2004)  
  - Group surplus/payoff: Brown et al. (2004); Oberholzer-Gee et al. (2010)—latter in non-punishment context

**Non-payoff behavioral outcomes (NOT efficiency):**
- Contribution/cooperation rates (Davis & Holt, 1999; Falk et al., 2005; Goette et al., 2012; Chen & Hauser, 2005)
- Punishment frequency and targeting (Falk et al., 2005; Goette et al., 2012)
- Honesty/slack behavior (Chen, 2012)
- Partner choice/reputation effects (Ashlock et al., 1996)
- Conditional cooperation based on observed traits (Oberholzer-Gee et al., 2010)
- Model fits to behavioral strategies (Chen & Hauser, 2005)

A few papers make inference links from behavioral change (e.g., higher cooperation) to anticipated efficiency, but these are not empirically validated within those studies.

# 4) Main Findings Relevant To Prediction

- **Punishment often reduces efficiency when costly and when deterrence is partial.**  
  *Abbink et al. (2004)* show in a repeated ultimatum context that enabling visible peer punishment increases fairness and punishment frequency, but decreases overall efficiency because the costs of punishment outweigh gains from behavioral changes. Only at extreme levels (very high or low punishment) does efficiency approach maximum.

- **Informal and endogenous punishment (e.g., firing/termination) can enhance efficiency, especially with reputation or repeated relationships.**  
  *Brown et al. (2004)*—in repeated market exchange—find that the ability to sanction through contract termination substantially increases effort, wages, surplus, and efficiency. The positive effect is contingent on the repeated-interaction structure (relationship formation), and is less about direct costly punishment and more about future contingencies.

- **Punishment increases cooperation rates, but efficiency outcomes are unmeasured.**  
  *Davis & Holt (1999)* and others find that enabling punishment often increases behavioral cooperation, but do not report on efficiency, leaving the link from cooperation to payoff/efficiency unsubstantiated in these settings.

- **Punishment can become antisocial and destructive under intergroup competition.**  
  *Goette et al. (2012)* find a shift from prosocial to antisocial punishment with the introduction of competition between groups, theorizing this may reduce efficiency, though not measured.

- **Adjustments to partner choice, reputational strategies, and punishment styles can have substantial effects on group interactions, but payoff/efficiency impact is often only hypothesized.**
  
- **Conditional cooperation based on observable characteristics can reduce efficiency in binary, high-stakes games.**  
  *Oberholzer-Gee et al. (2010)* document a drop in efficiency when players condition their choices on observed traits rather than employing direct punitive mechanisms.

# 5) Prediction Guidance

For the downstream prediction task—forecasting group efficiency with peer punishment enabled given control-game efficiency and game design parameters—this literature provides only **partial, indirect guidance**:

- Where punishment is **costly, used frequently, and fails to fully deter uncooperative behavior**, *efficiency may decrease* relative to control due to the costliness of sanctions outweighing gains from compliance (Abbink et al., 2004). This is especially salient when punishment rates are moderate and not fully effective.
- In environments with **relationship-based or endogenous future-contingent punishment** (not direct costly punishment in each round), *efficiency can improve*, approaching levels seen with external enforcement if agents can maintain repeated interactions and reputations (Brown et al., 2004).
- Merely observing **increased rates of cooperation or norm compliance does not guarantee higher efficiency**, as sanctioning costs can outweigh contributions gained (supported by absence of efficiency reporting in most behavior-oriented studies).
- If **social context changes** (e.g., group competition), punishment may become antisocial and destructive, *potentially reducing efficiency* (Goette et al., 2012).
- For most other design dimensions and behavioral mechanisms, evidence is indirect and should be used with substantial caution.

# 6) Design Dimensions Highlighted Across Papers

**Dimensions Directly Informed (measured in at least some studies with efficiency or direct payoff outcome):**
- `player_count` (multiple dyadic and triadic games)
- `num_rounds` (varying repetition; key in relational contracting findings)
- `punishment_cost` (manipulated in several studies)
- `punishment_tech` (visibility, coverage, magnitude)
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id` (used in relational/labor market context)

**Dimensions Indirectly Informed (discussed via behavioral, not payoff, outcomes):**
- `all_or_nothing`  
- `chat` (rarely or never present in these designs)
- `mpcr` (occasionally manipulated, mostly behavioral)
- `default_contrib` (basis for opt-in/opt-out not directly addressed)
- `reward_exists`, `reward_cost`, `reward_tech` (addressed in principal-agent context and via combined carrot-stick interventions)
- Social context features (competition, reputation, observable traits)

**Dimensions Only Contextually Discussed or Effectively Missing:**
- Most papers do not manipulate or systematically investigate chat, the default contribution framing, or reward parameters (with limited exception), and there is no direct evidence for PGG group size effects or multi-round/long-horizon compared to one-shot unless specifically designed for relational contract settings.

# 7) Important Limitations

- **No direct experimental evidence for repeated PGGs with and without peer punishment:** All findings are for adjacent or structurally similar games, not canonical PGGs.
- **Sparse reporting of efficiency or group payoff:** Most studies report only behavioral measures, making inferences about efficiency highly indirect except where specifically measured (Abbink et al., 2004; Brown et al., 2004; Oberholzer-Gee et al., 2010).
- **Behavioral outcomes may not translate into efficiency gains:** Increased cooperation or norm compliance is often accompanied by increased costly punishment, which can offset or even outweigh gains in public goods provisioning.
- **Key design dimensions for prediction are not systematically varied or cross-compared for efficiency outcomes** in this set.
- **Results from dyadic, market, or PD-like games may not extrapolate reliably to multi-player PGGs, especially for larger group sizes or complex interaction structures.**
- **Ambiguity around when punishment is efficiency-enhancing:** Even among adjacent games, the net efficiency effect hinges on context—relational structure, costliness, ability to build reputation—leading to potentially contradictory guidance.
- **Generality to real-world PGG environments is limited** by the highly controlled and simplified nature of laboratory experiments in these papers.

---

**In summary:**  
The literature base, while rich in experimental exploration of punishment and sanctions across social dilemma environments, provides only patchy and mostly indirect guidance for predicting efficiency effects of peer punishment in PGG-like games. Where direct efficiency is measured, punishment does not reliably increase efficiency and can decrease it if costs are high and deterrence imperfect (Abbink et al., 2004). Endogenous or repeated relationship-based punishment, however, can boost efficiency via improved discipline and cooperation (Brown et al., 2004). Most other studies report only behavioral outcomes or are too structurally dissimilar to inform efficiency prediction with confidence. Design parameters relevant to prediction are incompletely covered, with group size, cost, repetition, and punishment mechanism being the most substantiated. This evidence base should be treated with care and its limitations kept in mind for downstream prediction tasks.
