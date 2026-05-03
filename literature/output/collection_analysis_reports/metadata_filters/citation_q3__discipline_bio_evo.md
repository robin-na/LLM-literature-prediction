# 1) Evidence Base

The paper set is broad and diverse but highly theory-oriented, with sparse direct empirical evidence on payoff-based outcomes in experimental settings. The largest fraction of papers come from theoretical modeling—especially evolutionary game theory and agent-based simulations—focused on public goods games (PGGs), their close variants (e.g., common-pool resource dilemmas), and adjacent social dilemma frameworks (e.g., iterated Prisoner's Dilemma, threshold games, mutualisms). Some field and laboratory experiments are included, but these typically report behavioral rather than direct efficiency outcomes.  
Exact-experimental papers testing efficiency or total payoff effects of enabling punishment in PGGs are relatively rare. However, several theoretical and modeling studies offer explicit predictions on efficiency under varying game design dimensions and with/without punishment.

# 2) Task Relevance

### a) pgg_or_variant  
- **Exact Relevance**: Many theory papers (e.g., Eldakar et al., 2007; Oya & Ohtsuki, 2017; Milinski & Rockenbach, 2012) directly model standard or continuous PGGs, including variations with institutional/peer punishment and reward.
- **Close/Adjacent**: A substantial proportion address common-pool resource dilemmas, n-person Prisoner's Dilemma, trust games, threshold goods, or mutualisms—these are structurally similar but do not always perfectly map onto classic PGG designs.
- **Weak/None**: Some works only discuss punishment in non-PGG contexts, or address norm enforcement without mapping to a formal public goods structure.

### b) punishment_or_sanctions  
- **Exact Relevance**: Most included models and reviews manipulate peer or institutional punishment as a core independent variable and analyze design features (e.g., cost, effectiveness, identification).
- **Close/Adjacent**: Other studies focus on related enforcement mechanisms, e.g., exclusion, shunning, partner choice, or indirect punishment (gossip), or discuss the psychological/neural basis of punitive behavior without implementing it as a group-level intervention.
- **Weak/None**: A small subset only reference punishment tangentially or focus solely on reward mechanisms.

### c) efficiency_or_related_payoff_outcome  
- **Exact**: Several theoretical studies model group efficiency (mean payoff compared to the optimal fully cooperative benchmark) and provide explicit outcome metrics (e.g., Dong et al., 2019; Jiao et al., 2020; Eldakar et al., 2007).
- **Close**: A larger set link their behavioral or evolutionary analyses to aggregate payoffs or group welfare in a way that is mappable to efficiency (e.g., Oya & Ohtsuki, 2017; Powers et al., 2012).
- **Adjacent/Weak**: Many empirical and behavioral studies, including most experiments, report only non-payoff outcomes (e.g., contribution/cooperation rates, punishment frequency, attitude changes), requiring inference to relate to efficiency.

**Summary:**  
- The literature is highly relevant for PGGs and punishment, but only moderately so for direct efficiency or group-payoff outcomes—the core outcome for the downstream prediction task.

# 3) Outcomes Measured In The Literature

- **Payoff-based Outcomes (Efficiency):**  
  - *Directly reported* (rare): Mean group payoff, welfare, aggregate earnings relative to maximum possible (e.g., efficiency ratios in theory models, some simulation studies).
  - *Indirectly inferred*: Some papers provide explicit payoff formulas, equilibrium calculations, or model efficiency as a derived outcome.
- **Non-Payoff Behavioral Outcomes:**  
  - *Much more common*: Contribution/cooperation rates, free riding, prevalence/frequency of punishment, norm compliance, retaliation, switching rates, attitudes, and neural/psychological measurements.
  - *Important distinction*: These outcomes are often positively correlated with efficiency but do not account for the costs imposed by punishment (e.g., punishment costs may increase cooperation but reduce group welfare/efficiency—a point made explicitly in several reviews and models).

# 4) Main Findings Relevant To Prediction

### General Pattern

- **Punishment tends to increase cooperation** (behavioral outcome) in laboratory and theory models across a wide range of standard PGGs, but the effect on efficiency (payoff) is consistently shown to be strongly moderated by the details of the game design, especially the **cost-effectiveness of punishment**, the presence of **institutional/peer reward**, and possible **corruption or anti-social punishment**.
- **Efficiency effects can be positive, neutral, or negative** depending on:
    - **Punishment cost**: High-cost punishment often improves norm compliance but can reduce or invert efficiency gains (Dong et al., 2019; Powers et al., 2012; Jaffe, 2004; Vukov et al., 2013).
    - **Punishment effectiveness/tech**: Punishment that is highly effective per unit cost is more likely to deliver efficiency gains (Okada & Bingham, 2008; Zach, J.L. et al., 2013).
    - **Group/population structure**: Punishment works best to improve efficiency in small groups, repeated interactions, or spatially structured populations; in large or unstructured groups, effects are weaker or negative (Oya & Ohtsuki, 2017; POLLOCK, G.B., 1988; Powers & Lehmann, 2017).
    - **Anti-social or corrupt punishment**: If anti-social punishment (punishing cooperators) or corrupt punishment (defectors escaping or manipulating punishment) is possible, efficiency effects can reverse or vanish (Powers et al., 2012; Lee et al., 2015, 2017; Spadaro et al., 2023).
    - **Institutional design**: Institutional rewards often outperform punishment for efficiency (Dong et al., 2019; Kendal et al., 2006), and the presence of reputation systems or second-order incentives (meta-punishments) further stabilizes efficiency gains (Okada et al., 2015; Kendal et al., 2006; Rosas, 2010; Milinski & Rockenbach, 2012).

### Empirical Results
- *Lab experiments on efficiency outcomes in PGGs are rare* (see above).
- Most empirical lab and field data show increased contributions when peer punishment is enabled, but do not report payoff-based efficiency outcomes. Inferences about efficiency usually rely on theory.

### Mechanism and Modulation
- Efficiency benefits of punishment are largest when **punishment is rare, targeted, shared**, or **graduated** (Dercole et al., 2013; Deng et al., 2012; Couto et al., 2020; Iwasa & Lee, 2013).
- **Probabilistic punishment** or **concerted/severe but rare punishment** achieves high efficiency at lower cost, especially in large groups (Jiao et al., 2020; Deng et al., 2012).
- **Coordination mechanisms, participatory rule-making, trustworthy and transparent enforcement, and institutional meta-norms** further strengthen positive efficiency effects (Gatiso et al., 2015; Lee et al., 2015, 2017; Kendal et al., 2006; Milinski & Rockenbach, 2012).
- **Punishment can reduce efficiency** or prove counterproductive if costs are high, enforcement is corrupt/anti-social, or social contexts do not support legitimacy/compliance (Dong et al., 2019; Jaffe, 2004; Powers et al., 2012; Vollan et al., 2013; Spadaro et al., 2023).

# 5) Prediction Guidance

### Direct Implications
- If **control efficiency is known** and game design includes standard PGG elements, the **enabling of peer punishment** is most likely to **increase average efficiency** when:
    - **Punishment cost is moderate or low, and impact/effectiveness is high** (`punishment_cost`, `punishment_tech`)
    - **Group size (player_count)** is small to moderate, or population is structured (spatial/local interactions)
    - **Number of rounds (num_rounds)** is >1 (punishment loses effect in one-shot games)
    - **Anti-social or corrupt punishment is not possible or minimal** (`punishment_tech`, `show_punishment_id`)
    - **Punishment is probabilistic or concerted rather than always-on**
    - **Institutional features support reputational meta-mechanisms, coordinated punishment, or participatory establishment of sanctions**
- If **punishment is costly, anti-social or corrupt, group size is large with no structure, or no reputation/meta-enforcement is present**, enabling punishment may **not increase—and could decrease—efficiency** relative to control (see, e.g., Dong et al., 2019; Powers et al., 2012; Jaffe, 2004).

### Indirect Guidance & Cautions
- **Behavioral increases** in contribution/cooperation **do not guarantee efficiency gains**: the cost of punishment must be considered (many empirical studies neglect this, only reporting behavioral effects).
- **Empirical lab experiments rarely report efficiency**, so reliance on theory and modeling is necessary.
- **Institutional rewards, reputation systems, and second-order incentives** (e.g., rewarding punishers) are often **more robust for efficiency** than punishment alone.
- **Context, social norms, and implementation details**, including participatory governance and transparency (elections, identification of punishers, summary information shown), can mediate the effectiveness of punishment on efficiency.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- `player_count`: Modeled in most theory papers and key for scaling effects.
- `num_rounds`: Critical in theoretical and experimental models (punishment more effective in repeated games).
- `mpcr`: Extensive theoretical analysis; higher mpcr makes cooperation/efficiency easier to sustain.
- `punishment_cost`, `punishment_tech`: Multiple papers show explicit parameter sweeps and direct effects.
- `reward_exists`/`reward_cost`/`reward_tech`: Several studies provide contrasts between reward and punishment mechanisms.
- `all_or_nothing`: Modeled in both binary and continuous PGGs with differing consequences.
- `show_punishment_id`: Discussed in corruption/honesty models (identifiability moderates the effect).
- `show_other_summaries`, `show_n_rounds`: Sometimes included, especially in studies on information effects.

**Indirectly Informed Dimensions:**
- `chat`: Communication/coordination effects noted, but not always incorporated in formal analyses.
- `default_contrib`: Framing effects and default contribution settings are mentioned in a few behavioral studies.
- `punishment_exists`: Core manipulated variable throughout.
- `show_punishment_id`: Effects of identification on anti-social punishment/corruption are commented on.

**Sparse or Contextual Discussion:**
- `reward_cost`, `reward_tech` (relative to punishment): Addressed when examining reward versus punishment, but not always in parameterized form.
- `show_n_rounds`: Mostly discussed in terms of repeated versus single-shot.
- `default_contrib`: Framing less frequently examined.
- `show_other_summaries`, `show_punishment_id`, `chat`: Contextually referenced but rarely isolated as experimental treatments.

**Missing or Not Systematically Analyzed:**
- **Interaction effects** between dimensions (e.g., between `chat` and `punishment_cost`)
- Details on framing, behavioral heterogeneity, and default settings are not consistently explored.

# 7) Important Limitations

- **Empirical evidence on efficiency outcomes is sparse**: Most behavioral or experimental studies report only contribution rates or related outcomes, not direct group efficiency.
- **Heavy reliance on theory**: The majority of directly relevant evidence (for efficiency effects under varying design dimensions) comes from mathematical models and simulations, which may not capture laboratory or field idiosyncrasies, such as emotions, comprehension, or hidden costs.
- **Synchronicity and uniformity**: Real-world and even lab PGGs may include noise, understanding errors, and diversity not easily captured in models assuming homogeneous rationality or error rates.
- **Context-dependence not fully mapped**: The literature repeatedly notes that efficiency effects of punishment depend on institutional trust, social context, the prevalence of anti-social punishment, and the overlap with local norms, but these effects are not systematically parameterized across the 14 prediction dimensions.
- **Parameter regions with negative or null effects**: There is strong evidence that punishment can reduce efficiency under certain parameterizations, especially when costs are high, anti-social punishment is allowed, or enforcement is corrupt or illegitimate.
- **Translation from adjacent games**: Many supporting findings are from games adjacent to standard PGGs (e.g., common-pool resources, threshold games, iterated dilemmas), requiring caution in direct transfer to PGG design contexts.

---

**In conclusion:**  
- The literature base directly informs the predicted efficiency effect of enabling punishment in public-goods-game-like environments under many (but not all) parameterizations.
- Predictions should be adjusted in light of punishment cost, group size/structure, punishment effectiveness, enforcement integrity, and presence of supporting institutional or social mechanisms.
- Reliance on cooperation/contribution rates alone is insufficient; prediction should be rooted in payoff-based analysis.
- There are significant gaps—both empirical (lab/field efficiency data) and in contextual interactions between design dimensions—so predictions must retain caveats about the mapping from theory to practice.
