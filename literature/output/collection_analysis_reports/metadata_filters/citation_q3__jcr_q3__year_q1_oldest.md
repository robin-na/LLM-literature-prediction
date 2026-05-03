# 1) Evidence Base

The paper set comprises 34 theoretical and empirical studies, with a majority being theory papers and only a handful involving empirical experimental data (notably Bohnet & Baytelman, 2007; MOLM, 1994; Chen & Hauser, 2005). The set is broad in terms of the range of social dilemmas and mechanisms considered—including direct and indirect reciprocity, partner choice, spatial structure, reputation, and institution-building—but is narrower regarding direct, empirical, payoff-based studies of *public goods games* (PGG) with and without *peer punishment*. Most of the evidence on efficiency impacts is theoretical or based on adjacent paradigms (e.g., trust games, iterated prisoner’s dilemma). Some theory papers, however, adopt PGG-specific parameterization (Eldakar et al., 2007; Bednar, 2006; Powers et al., 2012; Okada & Bingham, 2008; de Jong & Tuyls, 2011), offering formal predictions tailored to PGGs. Direct empirical evidence on treatment efficiency in PGGs with and without punishment is limited. Much of the behavioral experimental literature focuses on cooperation rates or punishment assignment, which are not direct payoff-based outcomes.

# 2) Task Relevance

**pgg_or_variant:**  
- *Exact Relevance:* Several theory papers directly model public-goods games with standard or slightly modified design (Eldakar et al., 2007; Bednar, 2006; Powers et al., 2012; Milinski & Rockenbach, 2012; de Jong & Tuyls, 2011; de Weerd & Verbrugge, 2011; Rosas, 2010; Takezawa & Price, 2010).
- *Close/Adjacent Relevance:* Many papers operate with adjacent games (e.g., trust game, repeated n-person PD, CPR environments, inspection games), or address fundamental mechanisms that can generalize to but are not specific to PGGs (Bohnet & Baytelman, 2007; Okamoto & Matsumura, 2000; Leimar, 1997; Bravo & Tamburino, 2008).

**punishment_or_sanctions:**  
- *Exact Relevance:* At least half of the theory papers directly model peer punishment as in laboratory PGGs.
- *Close/Adjacent Relevance:* Some focus on indirect forms (e.g., withholding benefits, reputation mechanisms, policing, retaliation), or on punishment in other games (e.g., trust games, IPD, inspection games), or address cultural/group-level sanctioning rather than individual-level punishment.

**efficiency_or_related_payoff_outcome:**  
- *Exact/Close Relevance:* Only a subset directly analyze group efficiency, welfare, or total payoff as the primary outcome (Eldakar et al., 2007; Bednar, 2006; Powers et al., 2012; Okada & Bingham, 2008; Takezawa & Price, 2010; Weibull & Salomonsson, 2006; de Silva et al., 2010; Okamoto & Matsumura, 2000; Leimar, 1997; Bravo & Tamburino, 2008). 
- *Adjacent/Weak Relevance:* Many report only on behavioral outcomes (cooperation/contribution rates, norm compliance, frequency of punishment), often inferred but not directly tied to efficiency.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:** Group efficiency (total group payoff as a ratio of full-cooperation payoff), mean fitness, equilibrium welfare, average group payoff. These occur in a minority of the most relevant theoretical models and select adjacent empirical studies.
- **Non-payoff behavioral outcomes:** Contribution or cooperation rates, prevalence of punishment strategy, punishment frequency, compliance rates, trustworthiness, network structure evolution, retaliation, or affect toward punishers.
  - Many empirical lab studies focus primarily on these behavioral metrics rather than direct efficiency.
- **Linkage:** Behavioral outcomes are often implicitly (but not explicitly) tied to efficiency, with claims about payoff impact largely inferred rather than directly reported or quantified.

# 4) Main Findings Relevant To Prediction

**Direction and moderators of punishment’s effect:**
- **Punishment generally increases efficiency,** but this effect is *parameter-sensitive*. Under typical laboratory PGG conditions, enabling peer punishment raises group efficiency (Eldakar et al., 2007; Bednar, 2006; Milinski & Rockenbach, 2012). However, the boost is *incomplete*: groups do not reach full cooperation or peak efficiency due to the costs of punishment and incomplete deterrence of defection (Bednar, 2006; Powers et al., 2012).
- **Punishment cost and effectiveness critically moderate the effect.** Low-cost, high-impact punishment is most likely to transform low-efficiency groups to high-efficiency equilibria (Okada & Bingham, 2008). When punishment is too costly or weak, the efficiency gain is null or even negative (Powers et al., 2012; Weibull & Salomonsson, 2006; Leimar, 1997).
- **Group size and structure matter.** Positive effects of punishment on efficiency are generally stronger in small groups (Eldakar et al., 2007; Powers et al., 2012); in larger or well-mixed groups, anti-social punishment and weaker between-group variance can undermine the effect or even reverse it.
- **Repeated interaction (num_rounds):** The effect of punishment on efficiency is more positive in repeated games than in one-shot settings. Insufficient round length may prevent deterrence and cooperation from stabilizing (Eldakar et al., 2007; Leimar, 1997).
- **Imperfect monitoring/visibility:** Efficiency improvement is limited under noisy or partial monitoring; increased punishment severity can help but does not fully solve the compliance deficit (Bednar, 2006).
- **Interactions with other mechanisms:** The efficiency gains from punishment can be amplified by combining with reputation/indirect reciprocity mechanisms (Milinski & Rockenbach, 2012; Rosas, 2010).
- **Risks of anti-social punishment:** The possibility for defectors to punish cooperators can sometimes erase or reverse the positive effect of punishment (Powers et al., 2012).
- **Voluntary participation:** Enabling players to opt out can interact with punishment to increase equilibrium efficiency; in compulsory regimes, punishment may be less effective (de Silva et al., 2010).
- **Empirical studies** generally support the theoretical predictions, though often only via increased contributions rather than direct efficiency calculations (Bohnet & Baytelman, 2007; MOLM, 1994).

# 5) Prediction Guidance

- **General rule:** Enabling peer punishment is expected to raise average group efficiency (total group payoff as a fraction of optimal payoff), but not to the full-cooperation benchmark, and with diminishing returns as punishment becomes costlier, group size increases, or rounds decrease.
- **Baseline (control) efficiency is informative:** The efficiency observed with punishment disabled provides a lower bound; the predicted efficiency with punishment enabled should be higher, except under specific adverse conditions (high punishment costs, large group size with anti-social punishment risk, very short or noisy games).
- **Key design dimension effects:**
  - **Punishment cost, magnitude, and technological implementation** are primary: higher cost and lower effectiveness weaken the efficiency gain.
  - **Player count (group size):** Efficiency gains from punishment shrink with increasing group size.
  - **Game length (num_rounds):** More rounds enable punishment’s deterrent effect and allow efficiency gains to accumulate.
- **Contextual features:** The absence of communication, rewards, and reputation mechanisms means that predictions should not assume further efficiency boosts from these sources unless explicitly enabled (Eldakar et al., 2007; Milinski & Rockenbach, 2012).
- **Inability to reach full efficiency:** Even with punishment, equilibrium efficiency will fall short of 100% due to residual free-riding and the costs expended in punishing.
- **Cross-paper uncertainty:** In rare cases, punishment may reduce efficiency if anti-social use is prevalent, or costs are excessive.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions:**
- `player_count` (group size): directly manipulated and theoretically analyzed in most relevant theory papers.
- `num_rounds`: repeatedly analyzed for its effect on stability and efficiency.
- `mpcr`: key in predicting baseline cooperation and the ease of sustaining reciprocity.
- `punishment_cost` and `punishment_tech` (cost and effectiveness): primary focus of efficiency predictions.
- `all_or_nothing`: less commonly analyzed, but continuous-vs-discrete action space considered (Bednar, 2006; Takezawa & Price, 2010).
- `punishment_exists`: explicit in all theory models.
- To a lesser degree, `show_n_rounds` and `show_other_summaries` link to information and monitoring.

**Indirectly/contextually discussed:**
- `chat` (communication): mostly omitted; a small number mention its effects or its absence as an assumption (Eldakar et al., 2007; Ehmke & Shogren, 2009).
- `default_contrib`: rarely parameterized but occasionally mentioned in framing effects.
- `reward_exists`, `reward_cost`, `reward_tech`: discussed in context of stick–carrot comparisons but rarely parameterized.
- `show_punishment_id`: rarely manipulated as a variable.
- `show_other_summaries`: linked to monitoring and information structure rather than payoff per se.

**Effectively missing:**
- Effects of explicit framing (opt-in/opt-out), default contribution (`default_contrib`), and full combinations of feedback visibility (`show_punishment_id`, `show_other_summaries`) are not well covered in direct efficiency terms.

# 7) Important Limitations

- **Predominance of theory:** Most findings are from formal models, with little direct empirical quantification of efficiency impact from enabling punishment in actual laboratory PGGs. Thus, uncertainty about effect sizes is high.
- **Behavioral vs. payoff outcomes:** Many studies infer efficiency from cooperation rates or strategy adoption, but do not directly report group efficiency or payoff ratios.
- **Sparse direct evidence on several design dimensions:** Effects of communication, framing, reward mechanisms, visibility of rounds, and identification are only contextually discussed, if at all.
- **Limited accounting for anti-social punishment:** While highlighted as a major risk (Powers et al., 2012), empirical evidence on its prevalence and impact on efficiency in PGGs is scant in this set.
- **Adjacency and generalizability:** A minority of studies report on games that are not standard PGGs (trust game, inspection game, PD); caution is needed in generalizing to PGG scenarios.
- **Little conflict, but much conditionality/parameter dependence:** There is relatively consistent directionality for a positive effect of punishment—where model features are suitable (moderate cost, repeated rounds, small to moderate group size, no strong anti-social punishment)—but predictive confidence declines when applying outside these bounds.
- **Insufficiency for high-fidelity prediction:** While the literature broadly supports efficiency increases from enabling peer punishment under many PGG designs, it provides limited direct guidance for the size of the increase or the specific joint effects of all 14 design dimensions. Control efficiency remains the best baseline reference. 

---

**Summary:**  
The literature strongly and consistently supports a positive but incomplete effect of peer punishment on group efficiency in public-goods-game-like environments, conditional on moderate punishment cost, effectiveness, group size, and number of rounds. However, the available evidence is largely theoretical, with limited direct empirical documentation, and some potentially relevant design dimensions remain underexplored in payoff terms. Caution and parameter sensitivity should guide quantitative prediction.
