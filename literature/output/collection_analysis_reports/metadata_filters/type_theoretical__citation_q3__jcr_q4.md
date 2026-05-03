# 1) Evidence Base

The current paper set comprises **seven papers**, all of which are theoretical, with no direct empirical or experimental studies. Theoretical approaches include evolutionary modeling, agent-based simulation, and standard game-theoretic modeling in public goods game (PGG) or similar strategic environments. The set is **narrow** in empirical scope but **moderate to broad** in terms of theoretical paradigms explored, encompassing PGGs, repeated games, evolutionary norms, and institutional punishment mechanisms.

There is **strong direct theoretical representation** of classic and variant PGGs with punishment, but most conclusions are derived from models, not real-world data. Some papers focus specifically on public goods games, while others use variants such as repeated Prisoner's Dilemma or agent-based resource-sharing games with transferable logic. Coverage of design parameters is uneven, with certain prediction-relevant dimensions (like player_count, punishment_cost) addressed repeatedly and others (such as chat, default contribution framing, or identity transparency) missing.

---

# 2) Task Relevance

**pgg_or_variant:**  
- **exact:** Three papers are directly focused on PGGs: Deng et al. (2012), Thöni (2014), and Kurokawa et al. (2010).  
- **close/adjacent:** Several others (Kendal et al., 2006; Jaffe, 2004; Blonski & Spagnolo, 2015; Huang, 2007) model adjacent environments (e.g., repeated Prisoner's Dilemma or resource-sharing) that share structural analogies with PGGs.
- **weak/none:** No unrelated studies; all papers are at least adjacent.

**punishment_or_sanctions:**  
- **exact:** All studies are explicitly concerned with forms of punishment, sanctions, or policing, ranging from standard costly punishment to concerted, metanorm, or institutional punishments, plus analysis of antisocial punishment.
- **close:** Some address contingent cooperation or social investment, which act as functional punishment/sanction analogues.

**efficiency_or_related_payoff_outcome:**  
- **exact:** Deng et al. (2012), Kurokawa et al. (2010), Kendal et al. (2006), and Jaffe (2004) provide primary outcomes in terms of group efficiency, mean fitness, aggregate wealth, or related payoffs.
- **adjacent:** Thöni (2014), Blonski & Spagnolo (2015), and Huang (2007) focus on behavioral outcomes (e.g., punishment frequency, cooperation rate, norm compliance, trust) with efficiency/total payoff only discussed in passing or as an implication.

**Summary:**  
Overall, this is a **theoretically strong** set for examining the effects of punishment on (predicted) efficiency in public-goods-like games, but empirical verification is lacking. Payoff-relevant outcomes are present in roughly half the papers (with the rest focusing on mechanisms or behaviors), and direct match to PGGs is also about half, with the remainder structurally proximate but not identical.

---

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes (relevant to prediction):**
- **Group efficiency/total payoff:** Most directly: Deng et al. (2012; theoretical/simulations), Kurokawa et al. (2010; theoretical), Kendal et al. (2006; theoretical), and Jaffe (2004; agent-based simulation). 
- **Mean fitness/aggregate wealth:** Reported or modeled in Kendal et al. (2006), Jaffe (2004).
- **Welfare, surplus, average payoff:** Discussed in context (Deng et al., Kurokawa et al.) or as a byproduct of evolutionary success.

**Non-payoff behavioral outcomes:**
- **Cooperation/contribution rate, norm compliance:** Several studies (especially Huang, 2007; Thöni, 2014; Blonski & Spagnolo, 2015) center on these, i.e., how often players cooperate or punish, not how much is collectively earned.
- **Punishment assignment/frequency, antisocial punishment occurrences:** Mechanistic focus in Thöni (2014), Blonski & Spagnolo (2015), some discussion in Jaffe (2004), and Huang (2007).

**Explicit distinction:**  
- Some papers (especially Thöni, 2014; Huang, 2007) measure behavioral/psychological effects without linking them directly to efficiency or group payoff, while others (e.g., Jaffe, 2004) do link punishment to total welfare and thus group efficiency.

---

# 4) Main Findings Relevant To Prediction

**Consistency and Divergence:**
- **Efficiency-increasing effects of punishment:**  
  - **Deng et al. (2012):** Rare, severe, and concerted punishment greatly increases group efficiency, especially with large groups and severe punishment, and reduces the cost of sustaining cooperation.
  - **Kendal et al. (2006):** Metanorm-based punishment or reward (especially rewarding punishers) fosters high efficiency and stable norm compliance.
  - **Kurokawa et al. (2010):** Generous, contingent strategies (akin to tolerant punishment) outperform strict retaliation or defection, supporting efficient cooperation when replacing defectors; however, this does not address costly punishment directly.

- **Efficiency-limiting or reducing effects:**
  - **Jaffe (2004):** Costly punishment increases norm adherence but can reduce group efficiency or wealth unless synergistic social benefits result from the enforced behaviors.
  - **Thöni (2014):** Antisocial punishment undermines the efficiency of informal punishment institutions—efficiency effects depend negatively on prevalence of such punishment.
  - **Blonski & Spagnolo (2015), Huang (2007):** Main findings are behavioral (not efficiency), but suggest that effectiveness and structure of punishment affect how cooperation and thus possible efficiency are achieved; the riskiness and patience of the environment matter.

**Design Dimension Insights:**
- Effects of **player count, punishment severity, and cost** are directly modeled in several papers (Deng et al., Kurokawa et al., Kendal et al., Jaffe, Blonski & Spagnolo). Larger groups may yield more pronounced efficiency improvements if punishment is rare but severe and/or shared.
- **Reward mechanisms** (Kendal et al., 2006) may outperform pure punishment, enabling greater efficiency gains.
- **Antisocial punishment** (Thöni, 2014) can negate efficiency improvements, and its likelihood may depend on group inequality or psychological factors rather than payoff structure.

**Empirical Status:**  
All findings are theoretical or simulation based—no empirical corroboration is presented in this set.

---

# 5) Prediction Guidance

To predict **treatment efficiency** (with peer punishment enabled) in public-goods-game-like designs:
- **Punishment mechanisms (design features) matter extensively.** Theoretical models (Deng et al., 2012; Kendal et al., 2006) suggest that *rare, severe, concerted,* or *metanorm-supported* punishment can cause large increases in efficiency, particularly as group size and punishment severity increase and as costs are kept moderate.
- **Standard costly punishment** does NOT universally increase efficiency: If punishment is common, antisocial, or not complemented by reward mechanisms, group efficiency may stagnate or even decline (Jaffe, 2004; Thöni, 2014), relative to control games. This is especially true if the total cost of punishment outweighs gains from increased cooperation.
- **Game parameters can shift the effect size:**  
  - **Player count:** Larger groups (n > 4) are more likely to see positive efficiency change with appropriate punishment mechanisms (Deng et al., 2012; Kurokawa et al., 2010).
  - **Punishment cost/severity:** Severe, infrequent, or shared-cost punishment works better for efficiency than frequent, mild, or individually costly punishment (Deng et al., 2012).
  - **Presence of reward:** Adding metanorm reward (Kendal et al., 2006) can substantially increase the probability of reaching efficient states.
- **Behavioral mechanisms such as antisocial punishment or diminished intrinsic motivation** (Thöni, 2014; Huang, 2007) can attenuate or reverse efficiency improvements in some environments, but these effects are not directly linked to payoff in these models.

**Net guidance:**  
If the baseline (control) efficiency is known, enabling peer punishment can be expected to increase efficiency primarily *when punishment is well-designed* (rare, severe, concerted, or reward-supported) and *when the risk of antisocial punishment is low*. In other designs, efficiency may remain flat or decline due to increased costs. The diversity of theoretical mechanisms in the literature means that direct quantitative prediction remains difficult without empirical calibration.

---

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions:**
- **player_count:** Modeled in PGG and repeated games (Deng et al., Kurokawa et al., Kendal et al., Jaffe, Blonski & Spagnolo, Huang).
- **num_rounds:** Incorporated in repeated-game settings (Kurokawa et al., Blonski & Spagnolo, Jaffe, Kendal et al., Huang).
- **all_or_nothing:** Explicitly part of several model setups (Deng et al., Thöni, Kurokawa et al., Blonski & Spagnolo, Huang).
- **mpcr:** Central to payoff structure in the PGG-based models (Deng et al., Kurokawa et al., Thöni, Blonski & Spagnolo, Huang).
- **punishment_cost** and **punishment_tech:** Explicitly varied and modeled in nearly all studies except those focusing entirely on metanorms or adjacent games.
- **reward_exists, reward_cost:** Modeled in Kendal et al. (metanorms/rewards for punishers).
- **show_n_rounds, show_other_summaries:** Kurokawa et al. model group knowledge as part of reciprocation strategy triggers.

**Indirectly/contextually addressed:**
- **show_punishment_id:** Generally not modeled (identity revelation not explicit).
- **default_contrib:** Not present (framing effects not modeled).
- **chat:** Not addressed.
- **reward_tech:** Somewhat addressed in Kendal et al.

**Effectively missing:**
- **chat, default_contrib, show_punishment_id, show_other_summaries** (except for possible indirect handling of group-level summary info in some repeated-game models).

---

# 7) Important Limitations

- **Empirical evidence is absent:** All findings are theoretical or simulated; real-world or experimental confirmation is missing from this set.
- **Generalizability to empirical contexts is speculative:** Structural and psychological aspects crucial to real-world PGG behavior (e.g., communication, framing, subject pool idiosyncrasy) are not included.
- **Sparse coverage of some design parameters:** Identity transparency, chat, default contribution framing, and detailed information feedback on others’ actions—which are often critical in laboratory or online settings—are unaddressed.
- **Predictions are contingent on model assumptions:** The efficiency effects of punishment mechanisms depend on stylized rules (rarity, severity, metanorms, population structure) that may not correspond to real-world group dynamics.
- **Ambiguity and conflict in theoretical direction:** Some models (e.g., Deng et al., Kendal et al.) predict strong efficiency gains under specific conditions; others (Jaffe, Thöni) emphasize potential efficiency losses in the presence of costly or antisocial punishment.
- **Non-payoff behavioral outcomes are not equivalent to efficiency:** Several papers focus on cooperation rates, norm compliance, or punishment frequency; these are only indirectly relevant to payoff prediction and should not be equated with efficiency outcomes.
- **Parameter calibration is not provided:** No paper offers empirically estimated effect sizes or directly parametrizable predictions based on the 14 design variables plus control efficiency.

**In summary:**  
This literature set provides rich theoretical insight—especially into how punishment’s design and group structure can (or cannot) promote efficiency—but does not offer direct, quantified, or empirically calibrated models for predicting the treatment efficiency of arbitrary PGG-like environments based solely on design dimensions and control efficiency. Its predictive guidance therefore remains *conditional and qualitative* rather than *precise or quantitative*.
