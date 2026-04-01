# 1) Evidence Base

**Nature of Evidence:**  
- The evidence base is comprised of 207 papers, nearly all of which are *theoretical*; there is a striking absence of empirical and experimental studies in this set.
- Theoretical papers offer detailed mechanism models, agent-based simulations, and analytic results often validated by simulation, but do not report lab or field experimental data.
- Most studies model public goods games (PGGs) or closely related social dilemmas using evolutionary game theory, replicator dynamics, or agent-based models on various network structures.
- The paper set is **broad and deep** for task-relevant theory in PGG and related social dilemmas, covering an extensive range of design features and mechanisms affecting efficiency. However, it is *narrow in empirical grounding*, lacking real-world or experimental outcome data for quantitative prediction.

# 2) Task Relevance

Evaluation is based on three axes:  
**a) pgg_or_variant**  
- The majority of papers are labeled *exact* or *close*: they explicitly model standard PGGs or direct variants (threshold PGGs, spatial PGGs, donation games with PGG structure, collective-risk dilemmas).
- A significant minority are *adjacent*: modeling repeated or networked Prisoner’s Dilemma games, Ultimatum games, resource competition, or indirect reciprocity—not all of which are direct PGGs.
- Some are *weak* or *none*, not modeling public goods contexts directly.

**b) punishment_or_sanctions**  
- Most topically relevant papers are *exact* (modeling peer or pool punishment, exclusion, or institutional sanctions).
- Several are *close* (modeling ‘punishment-like’ reputational mechanisms, social exclusion, or norm-based sanctions).
- Others are *adjacent*: covering reward, indirect sanctioning, or no explicit punishment mechanism.

**c) efficiency_or_related_payoff_outcome**  
- Many papers are *exact*: reporting group efficiency, total payoff, welfare, or surplus as primary outcomes.
- Some are *close* (group achievement, accumulated wealth, or cost-based proxy for efficiency).
- Many others are *adjacent* or *weak*: focusing on cooperation or contribution rates, strategy frequencies, norm-compliance, or equilibrium distributions, with no direct measurement of efficiency.

**Summary:**  
- The literature contains a *core* of highly relevant theory papers providing direct, mechanism-driven insights about punishment's effect on efficiency in PGGs, conditional on design dimensions and control-game efficiency.
- There is limited direct empirical validation or effect-size estimation in realistic game settings.

# 3) Outcomes Measured In The Literature

**Payoff/Efficiency-related Outcomes:**  
- *Efficiency/or payoff*: Defined as group total payoff relative to the maximum possible (full cooperation), is the direct outcome in most of the highly relevant theory work (e.g., Bühren et al., 2023; Duong & Han, 2021; Sasaki et al., 2015; Roberts, 2013).
- *Adjacent payoff proxies*: Some studies report group achievement, institutional cost to achieve cooperation, or stationarity of average payoffs (e.g., Góis et al., 2019; Perc, 2012).
- *Indirect measures*: Some model stationarity of cooperative states and infer efficiency via the abundance of punishers/cooperators/punished states.

**Non-payoff/Behavioral Outcomes:**  
- Many adjacent and weakly relevant papers primarily report *contribution rate*, *cooperation rate*, *punishment frequency*, *strategy prevalence*, or the evolutionary stability/frequency of behaviors.
- Papers based on indirect reciprocity, social norms, exclusion, and adaptation mechanisms often focus on the prevalence of cooperation or norm compliance, not efficiency.

**Distinction:**  
- **Crucially:** Not all increases in cooperation or punishment frequency translate to higher efficiency, as costly punishment may reduce group payoffs despite promoting compliance. Several papers explicitly highlight this distinction and analyze when punishment improves or harms efficiency.

# 4) Main Findings Relevant To Prediction

**Empirical Patterns from Theory (Payoff-Based):**
- **Punishment can increase efficiency…**
   - When punishment is *cost-effective*: low cost relative to its impact on defectors (Hetzer & Sornette, 2013; Zefferman, 2023; Roberts, 2013).
   - When the group or population is mostly non-cooperative in control; enabling punishment transforms the game from a social dilemma (defection trap) to a coordination game (Hetzer & Sornette, 2013; Eldakar & Wilson, 2008).
   - When combined with *voluntary participation* or *optional entry*, even small punishments can maximize group efficiency (Sasaki et al., 2012; Hauert et al., 2007).

- **But punishment can reduce efficiency…**
   - When punishment is very costly or ineffective, or both, the direct cost to punishers and/or collateral costs borne by others lower total group payoffs (Sigmund et al., 2010; Barrett, 2016).
   - If antisocial punishment is possible (i.e., defectors punish cooperators), efficiency can fall below control (Rand & Nowak, 2011).
   - With the possibility of corruption or ineffective institutions (Lee et al., 2019), institutional punishment may be exploited, resulting in lower efficiency.

- **Design Moderators and Interactions:**
   - *Spatial structure*: Structured/population-based punishment or local monitoring can have threshold effects—punishment reach or coverage beyond a critical value causes a sudden jump to high efficiency (Bodnar & Salathé, 2012; Wang et al., 2024).
   - *Reward vs. Punishment*: Rewards tend to be more efficient for increasing cooperation at low baseline rates; punishment is more efficient when high cooperation is already likely or required (Chen et al., 2015; Góis et al., 2019).
   - *Presence of Norms, Reputation or Observability*: Punishment is more efficient when reputation tracking is possible/observable; in anonymous or non-reputation settings, punishment has little or negative effect on efficiency (Sigmund et al., 2001; García & Traulsen, 2019).
   - *Second-order free riders*: Efficiency gains from punishment often require sanctioning non-punishers (second-order free-riders); if left unchecked, these undermine the sustainability and efficiency of punishment institutions (Perc, 2012).
   - *Hybrid or adaptive policies*: The most cost-efficient incentive schemes dynamically combine reward and punishment (Chen et al., 2015).

- **Payoff-Behavior divergence:**  
   - Many models find that punishment robustly increases cooperation rates, but only sometimes increases efficiency—if the costs of monitoring and punishment are high, overall payoffs can be reduced despite more cooperation (Sigmund et al., 2010; Fehr & Schurtenberger, 2018).

# 5) Prediction Guidance

**General Principles:**  
- **Effect of Punishment on Efficiency Depends on Control Efficiency & Design Dimensions**:
    - Where baseline control efficiency is low (widespread defection or moderate cooperation), introducing cost-effective punishment typically increases efficiency substantially (Bühren et al., 2023; Hetzer & Sornette, 2013; Eldakar & Wilson, 2008).
    - Where baseline efficiency is already high (near-maximum cooperation), additional punishment may be wasteful or counterproductive, reducing net payoffs (Bühren et al., 2023; Zefferman, 2023).

- **Critical Moderators (best evidenced dimensions):**
    - *punishment_cost* and *punishment_tech*: Lower costs and higher punishment effectiveness increase the likelihood that enabling punishment increases efficiency (Hetzer & Sornette, 2013; Zefferman, 2023; Roberts, 2013).
    - *player_count* (group size): Larger groups require more efficient punishment (per-punisher cost decreases with more punishers; Boyd et al., 2010), but also face greater coordination and monitoring challenges (Perc, 2012; Zefferman, 2023).
    - *mpcr*: Higher marginal per-capita return (MPCR) increases the potential for punishment to be beneficial; at low MPCR, efficiency gains are harder to achieve (Salahshour, 2021).
    - *reward_exists*: When reward mechanisms are also enabled, efficiency is maximized by adaptive use—reward to build cooperation, punishment to maintain it (Chen et al., 2015; Góis et al., 2019).
    - *show_punishment_id*/*show_other_summaries*: Observability/reputation is key for punishment to be effective and efficient (Sigmund et al., 2001; García & Traulsen, 2019).
    - *network structure* and *monitoring*: High reach and efficient monitoring produce threshold-like jumps in efficiency when punishment is enabled (Bodnar & Salathé, 2012).

- **Use of Control-Game Efficiency**:  
   - Given validated theoretical models calibrated to experimental data, treatment efficiency with punishment can often be predicted as a nonlinear function of control efficiency and design parameters, with threshold and regime-shift effects.

**Cautions:**  
- Do not presume that higher cooperation rate always yields higher efficiency—costly punishment can still lower net payoffs if not effective or if misapplied.
- If antisocial punishment, corruption, or poorly designed sanction systems are possible, punishment may harm efficiency (Rand & Nowak, 2011; Lee et al., 2019).
- Institutional context (pool vs. peer punishment, voluntary participation, possibility for exclusion) is often more important than parameter values.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions (Frequent & Mechanistically Modeled):**
- *player_count*: Modeled as group size; explicit in most major theories and phase diagrams.
- *num_rounds*: Modeled in repeated games; sometimes as rounds per game, sometimes via evolutionary time.
- *all_or_nothing*: Both binary (all-or-nothing) and continuous contribution models are analyzed, with key differences in dynamics and efficiency.
- *mpcr*: Central parameter in nearly all models—effects always modulated by the marginal return of contributions.
- *punishment_cost* and *punishment_tech* (punishment magnitude/effectiveness): Core to all models of sanctioning—efficiency effects are highly sensitive to these.
- *reward_exists*, *reward_cost*, *reward_tech*: Explicitly explored in several models comparing reward, punishment, and combinations.
- *show_other_summaries*, *show_punishment_id*: Observability and information/reputation are often explicitly modeled and shown to be necessary for punishment to improve efficiency.

**Indirectly Informed or Contextually Discussed:**
- *chat*: Rarely modeled or discussed directly; assumed absent in most theory.
- *default_contrib*: Framing effect is rarely a focus; if present, its moderation of baseline rates is discussed but seldom linked to efficiency prediction.
- *show_n_rounds*: Discussed in some iterated/finite-horizon models as influencing end-game effects.
- *show_punishment_id*: Mapped to reputational observability in several (e.g., Sigmund et al., 2001).

**Effectively Missing (Little/No Evidence):**
- *chat*, *default_contrib* (in its framing sense).
- *fine-grained design of reward vs. punishment coexistence/choice* (i.e., hybrid conditions are studied, but the result of overlaid, competing, or optional peer reward and peer punishment is less directly explored).
- Empirical mapping from lab parameter values (e.g., specific costs and multipliers) to real observed efficiency changes is sparse.

# 7) Important Limitations

**1. Lack of Empirical Data:**  
- The literature is robust in mechanistic theory and simulation but *almost entirely lacks direct experimental or empirical* findings for quantitative estimation of efficiency treatment effects.

**2. Behavioral vs. Payoff Outcomes:**  
- While theory is clear about moderating factors, many papers measure only cooperation rate, norm adherence, or behavior—not efficiency—requiring careful translation.

**3. Context Specificity and Mechanism Detail:**  
- Many key results are *contingent on context*: e.g., punishment is only beneficial if second-order free-riders are sanctioned, if antisocial punishment is suppressed, or if monitoring is efficient.
- Institutional design features such as peer vs. pool punishment, observability, voluntary participation, and exclusion are often assumed cleanly, but real-world games may not match these stylized contexts.

**4. Non-Linearity and Threshold Effects:**  
- The effects of enabling punishment are often *nonlinear* and *subject to regime shifts*—small changes in cost-effectiveness, monitoring, or network structure can cause large changes in efficiency.

**5. Sparse Coverage of Certain Dimensions:**  
- Some dimensions with potential major effects (e.g., chat, default contribution framing) are unmodeled or missing.
- Reward mechanisms are less thoroughly compared to punishment across all game designs.

**6. Unknown Transferability of Mechanistic Results:**  
- Even where theory provides explicit formulas (e.g., for phase transitions in efficiency), the mapping from stylized, infinite-aggregation models to finite human groups may limit quantitative precision.
- The models' mapping to practical experimental setups (with finite rounds, turnover, learning, and implementation errors) is developed but not calibrated empirically.

---

**In summary**: The literature provides strong theoretical direction for predicting treatment efficiency with punishment, dependent on nuanced game design settings and the efficiency of the control game. Models richly explore how design dimensions moderate the magnitude and even the sign of punishment's effect on efficiency, but the absence of experimental effect sizes and real-world calibration is a critical caveat for quantitative prediction. Specific prediction for any novel game setting will require careful mapping of the proposed design to the nearest modeled domain, with attention to context, design regime, and the mechanisms identified as critical moderators.
