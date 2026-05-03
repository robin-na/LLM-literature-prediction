## 1) Evidence Base

**Nature of the Evidence Base:**  
This literature set is **broad and substantial**, drawn from 109 theory papers (no empirical or laboratory experimental work in this set). The papers are predominantly theoretical and/or based on agent-based or evolutionary simulations. No paper in this set supplies direct laboratory or field experiment data on public goods games (PGGs) with and without punishment, but many provide mathematical models and simulated results highly relevant to the downstream prediction task.

**Focus of Evidence:**  
The body of work ranges from standard PGGs to close variants (e.g., threshold PGGs, common-pool resource games), and includes in-depth treatment of punishment, reward, exclusion, and related sanction systems. Outcomes studied include both group efficiency/payoff and related behavioral variables (mainly cooperation/contribution rates). The set offers both general theoretical mechanisms and systematic mappings of design parameters to outcomes, especially for efficiency, within the constraints of model assumptions.

---

## 2) Task Relevance

### a) **pgg_or_variant**
- **Relevance:** `exact` for a large subset; some `close`; substantial minority are `adjacent`.
- **Synthesis:** The majority of the most relevant work directly models standard PGGs or slight variants (e.g., spatial/networked PGGs, threshold PGGs, collective-risk dilemmas). More distant yet sometimes informative are repeated Prisoner's Dilemma, indirect reciprocity, and common-pool resource games.

### b) **punishment_or_sanctions**
- **Relevance:** `exact` for central papers; `close` and `adjacent` for mechanism discussions (e.g., reputation loss, exclusion, indirect sanctions).
- **Synthesis:** The bulk of the evidence base is **highly relevant to punishment**, encompassing peer punishment, pool/institutional punishment, adaptive punishment, and exclusion. Some adjacent papers focus on related mechanisms like indirect reciprocity or partner choice, which are only analogically or contextually relevant.

### c) **efficiency_or_related_payoff_outcome**
- **Relevance:** About half of the central PGG + punishment papers report **`exact`** efficiency or closely related payoff outcomes. The remainder infer efficiency indirectly from cooperation rates, evolutionary stability, or strategy frequencies (`close` or `adjacent`).
- **Synthesis:** Direct modeling or reporting of group efficiency (as defined for the prediction task) is common in the most central theory/modeling papers, with other papers using behavioral proxies or evolutionary success.

---

## 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes:**  
  - **Efficiency**, average group payoff (relative to maximum possible), welfare, and surplus are the primary focus in the key papers (e.g., Cressman et al., 2012; Perc et al., 2017; Gintis, 2000; Szolnoki & Perc, 2013; Bowles & Gintis, 2004).
  - Payoff is sometimes directly calculated (analytic or simulation results), sometimes inferred from the dominance of cooperators in models where contribution directly determines group payoff.
  - Some papers, especially those modeling environmental feedback or resource renewal, use sustainability as a close proxy for efficiency (e.g., Yan et al., 2021).

- **Non-Payoff Behavioral Outcomes:**  
  - **Contribution/cooperation rates**, strategy frequency (e.g., cooperators, defectors, punishers), phase diagrams, and evolutionary stability are widely reported.
  - Papers focusing only on these rates often do so in contexts where the mapping to group efficiency is indirect.
  - Other behavioral outcomes include punishment frequency, retaliation, reputation scores, and partnership structure.

- **Overlap and Distinction:**  
  - It is crucial to disentangle increases in contribution rate (behavioral outcome) from increases in efficiency (payoff outcome), as some models show that more punishment does not always lead to higher efficiency due to punishment costs.

---

## 4) Main Findings Relevant To Prediction

### **General Effect of Punishment on Efficiency**  
- **Enabling (peer or institutional) punishment in PGG-like environments generally increases group efficiency relative to no-punishment controls**, provided the punishment is not too costly and has sufficient impact (Cressman et al., 2012; Perc et al., 2017; Gintis, 2000; Szolnoki & Perc, 2013; Bowles & Gintis, 2004).
    - The effect size and likelihood depend heavily on design parameters (player count, MPCR, cost/fine of punishment, punishment type, spatial structure).

### **Moderating Factors & Exceptions**
- **High punishment cost**: If punishment is costly or inefficient, efficiency gains disappear and can become negative (Perc et al., 2017; Lee et al., 2022).
- **Anti-social punishment**: Allowing punishment of cooperators ("anti-social punishment") can destabilize cooperation and nullify or reverse efficiency gains (Rand et al., 2010; Hauser et al., 2014); however, in some spatially structured environments, mechanisms like second-order free-riding can help restore prosocial punishment's effectiveness (Szolnoki & Perc, 2017).
- **Retaliation risk**: The possibility of retaliation against punishers undermines punishment's positive effects on both cooperation and efficiency, especially if punishers are easily identified (Janssen & Bushman, 2008).
- **Information/monitoring**: Efficiency gains from punishment require sufficiently informative and timely monitoring—imperfect information or short action cycles can reduce efficiency despite sanctioning options (Abreu et al., 1991).
- **Structural features**: Population structure (spatial networks, repeated groupings, migration, partner choice) can magnify or moderate punishment's effectiveness (Perc et al., 2017; Helbing et al., 2010; Bowles & Gintis, 2004).
- **Alternative Mechanisms**: Other mechanisms (e.g., exclusion, reputation, commitment, adaptive reward, or mobility) may substitute for or interact with punishment, sometimes achieving similar or even greater efficiency (Szolnoki & Chen, 2015; Han et al., 2017; Szolnoki & Perc, 2016).

### **Parameter Sensitivity and Phase Transitions**
- The efficiency benefit from enabling punishment is typically **nonlinear** (frequently displaying sharp transitions or regime shifts as cost, fine, or group structure passes thresholds; e.g., Szolnoki & Perc, 2013; Adami et al., 2016).
- **Group size:** Larger groups generally make cooperation and thus efficiency harder to sustain; the efficiency benefit from punishment may increase with group size if punishment is effective, but can vanish or become negative if punishment cost is high or sanctioning is ineffective (Suzuki & Akiyama, 2007; Hilbe et al., 2015).

---

## 5) Prediction Guidance

- **Baseline:** If control efficiency (no punishment) is very low (near all-defection), and design dimensions permit reasonably effective, not-too-costly punishment, expect a **substantial efficiency gain** when enabling punishment, with the magnitude depending on the fine-to-cost ratio and other parameters (Cressman et al., 2012; Gintis, 2000).
- **Parameter mapping:** Use mappings from key model papers (e.g., Perc et al., 2017; Szolnoki & Perc, 2013) to estimate whether the punishment parameters (cost, magnitude, type) fall within high-, low-, or intermediate-effectiveness regions. For most realistic PGGs, a moderate cost and sufficiently high fine produce efficiency gains; high costs or inefficient punishment negate these gains.
- **Structural issues:** Adjust predictions for spatial/networked games (clustering supports higher efficiency, especially at low MPCR), and be cautious in well-mixed or very large groups without additional supporting mechanisms.
- **Punishment type:** The literature finds **peer punishment, pool (institutional) punishment, and exclusion** can all improve efficiency, but with different sensitivities to cost, information, and the possibility of antisocial use.
- **Monitoring and information:** For repeated/long games, opaque or infrequent reporting reduces the efficacy of punishment for sustaining efficiency (Abreu et al., 1991).
- **Anti-social punishment/retaliation:** If the design allows for anti-social punishment or easy retaliation against punishers, the effect on efficiency should be set to neutral or negative.
- **Reward and alternatives:** Enabling reward (when available) can also increase efficiency, particularly when the initial cooperation level is high. However, in most models, punishment is more efficient than reward (Szolnoki & Perc, 2013; Cressman et al., 2012).

---

## 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- **player_count (group size):** Extensively modeled as a parameter; efficiency effects of punishment are often group-size dependent.
- **num_rounds:** Frequently incorporated in evolutionary and repeated games; the length of interaction moderates the effect of punishment on efficiency.
- **mpcr (Marginal per-capita return):** Central to nearly all PGG models; efficiency effects of punishment are strongly moderated by MPCR/synergy factor.
- **punishment_cost**, **punishment_tech** (fine/effectiveness): Key focus of nearly every punishment effectiveness discussion; direct mappings available from several papers.
- **reward_exists, reward_cost, reward_tech:** Modeled but less central; where present, reward parameters are often contrasted with those of punishment.
- **all_or_nothing (contribution structure):** Many models specify whether contribution is binary or continuous, with phase transitions depending on this structure.

**Indirectly Informed/Only Contextually Discussed:**
- **chat (communication):** Some mention (especially Ostrom, 2009), but not typically formalized; where absent, predictions for chat-enabled environments are less well informed.
- **default_contrib:** Framing (e.g., opt-in vs. opt-out) is almost entirely absent as a model parameter; possible contextual effects (see literature on framing, not in core models).
- **show_n_rounds, show_other_summaries, show_punishment_id:** Information and monitoring are critical moderators (Abreu et al., 1991; Janssen & Bushman, 2008), but direct modeling using these specific variables is rare; implications are inferential.

**Effectively Missing:**
- **default_contrib** (framing), **show_n_rounds**, **show_other_summaries**, **show_punishment_id** lack systematic study in these theoretical models; predictions for efficiency change with these parameters are not constrained by this literature.

---

## 7) Important Limitations

- **Lack of direct empirical data:** All results are theoretical or simulation-based; there are no empirical or experimental results on realized efficiency when punishment is enabled.
- **Parameter mapping:** While many models are parameterized (player count, MPCR, cost/fine of punishment), variation in model details (update rule, spatial structure, learning protocol) makes mapping directly to every practical design dimension non-trivial.
- **Non-payoff outcome prevalence:** Many findings rely on cooperation rate or strategy frequency rather than efficiency strictly defined as the ratio of actual to maximum possible payoff.
- **Missing dimensions:** Critical design features such as communication, visibility of punishment, round structure, and framing are seldom or only indirectly modeled. Results for these are suggestive at best.
- **Ambiguity in complex settings:** Papers diverge substantially in the presence of anti-social punishment, retaliation, and in non-standard game structures (e.g., resource feedback, environmental coupling), sometimes producing opposed results.
- **Assumptions of infinite populations/iterations:** Many models assume very large or infinite populations and rounds; finite size or time effects may be poorly captured.
- **Heterogeneous definitions:** Some models conflate enforcement mechanisms, making it difficult to separate predictions for peer vs. institutional punishment or for exclusion vs. deduction-based punishment.

**Conclusion:**  
**The literature provides strong theoretical (not direct empirical) support for the claim that enabling (peer or institutional) punishment increases efficiency in PGGs, especially at moderate cost and when control efficiency is low. However, this effect is not guaranteed and depends strongly on punishment cost, structure, information, and the possibility of anti-social punishment or retaliation. Furthermore, predictions for games with complex or atypical design dimensions should be viewed with caution, as direct evidence is sparse for those parameter regimes.**
