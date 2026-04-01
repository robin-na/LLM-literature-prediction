# 1) Evidence Base

The paper set is comprised entirely of **theoretical studies** (no empirical or laboratory experiments) and centers overwhelmingly on **formal modeling and simulations** of public goods games (PGGs) and closely related social dilemma environments. There is a **narrow but deep focus** on the prediction task: most highly relevant papers directly model PGGs with/without punishment or sanctions and report outcomes—sometimes efficiency/payoff, sometimes behavioral variables such as cooperation rate. However, there remains a substantial subset of work addressing adjacent or weakly relevant paradigms (prisoner's dilemma, snowdrift games, resource sharing games, or organizational/biological analogs).

- **Empirical evidence**: None.
- **Experimental studies**: None.
- **Theory/simulations**: All.
- The theoretical analyses often derive explicit formulas or phase diagrams as functions of game parameters, directly informing prediction for standard PGGs, although generalizability to empirical settings can be uncertain.

**Conclusion:** This is a comprehensive theoretical base, strong for mechanistic insight and parametric prediction within modeled environments, but lacking empirical validation, field results, or laboratory calibration.

# 2) Task Relevance

**a. pgg_or_variant**  
- **exact:** The core of the paper set is highly relevant, modeling standard public goods games (PGGs) or direct extensions (e.g., spatial PGGs, optional participation, voluntary contributions), and providing results that map directly onto PGG payoff structure (e.g., Wu et al., 2014; Levine & Modica, 2016; Sasaki, 2014; Sui et al., 2017).
- **close:** Some work uses close variants (e.g., threshold public good games, multiplayer snowdrift games) (e.g., Xu et al., 2015; Zhang et al., 2015). These exhibit similar dynamics but are not strictly standard PGGs.
- **adjacent/weak:** A significant fraction analyzes repeated/iterated prisoner's dilemma, resource allocation, trust games, or broader social dilemmas (e.g., Camera & Gioffré, 2017; Han & Lenaerts, 2016). Results in this group are mainly used for analogy or indirect support.

**b. punishment_or_sanctions**  
- **exact:** The most relevant papers directly implement or manipulate peer or institutional punishment as an explicit design dimension (e.g., Wu et al., 2014; Levine & Modica, 2016; Cong et al., 2016).
- **close:** Some focus on reward, exclusion, or meta-punishment, or use punishment-adjacent mechanisms (e.g., reputation-based exclusion, environmental sanctions).
- **adjacent:** Others address punishment abstractly or contextually, without formal modeling (e.g., Boehm, 2014).

**c. efficiency_or_related_payoff_outcome**  
- **exact:** Several papers report efficiency (total group payoff relative to full cooperation) as a primary outcome (e.g., Wu et al., 2014; Levine & Modica, 2016; Cong et al., 2016; Sasaki, 2014; Sui et al., 2017).
- **close:** Some papers calculate average payoffs or group welfare but focus primarily on behavioral or strategic composition (e.g., Perc, 2016; Chen et al., 2014).
- **adjacent/weak:** Many report only cooperation/contribution rates, norm compliance, or punishment usage, not efficiency or payout statistics.

**Summary:** There is a **strong, direct theoretical literature** for PGGs, explicit punishment/sanction mechanisms, and efficiency-based outcomes. However, many papers offer only indirect guidance (behavioral proxies or adjacent games), and the coverage thins notably when mapping to empirical contexts.

# 3) Outcomes Measured In The Literature

**Payoff-Related (Efficiency/Group Payoff):**
- **Directly Modeled and Reported:** Several core papers (usually with PGG or variant as model) report *efficiency* as the primary outcome (e.g., Wu et al., 2014; Levine & Modica, 2016; Cong et al., 2016). These calculate group payoffs relative to the cooperative optimum or as surplus.
- **Average Payoff/Group Welfare/Surplus:** Many others present these, often providing analytic expressions as a function of game parameters.
- **Indirect or Theoretical Formulas:** Some report them not as explicit simulation outputs but as outcomes derivable from equilibrium analysis.

**Non-Payoff Behavioral Outcomes:**
- **Cooperation/Contribution Rate:** Widely reported; these indicate the prevalence of cooperation but do not always translate in a simple way to group efficiency (especially when punishment is costly or antisocial).
- **Punishment Frequency/Intensity:** Sometimes recorded as an outcome, especially to analyze trade-offs or second-order dynamics.
- **Strategy Prevalence:** Papers often present stationary distributions over strategies or typologies (cooperators, defectors, punishers, etc.).
  
**Explicit distinction:**  
While higher cooperation rates often imply potential increases in payoff, these must not be equated with efficiency unless payoff-cost structures and negative effects of punishment (e.g., inefficiency from costly antisocial punishment) are accounted for.

# 4) Main Findings Relevant To Prediction

**Empirical Findings vs. Theory:**  
All findings are theoretical or simulation-based; no empirical results are present.

**Synthesis of Cross-Paper Findings:**

- **Enabling punishment generally increases efficiency**, often dramatically so when:
    - Punishment cost is low (Wu et al., 2014; Sui et al., 2017; Eldakar et al., 2013).
    - Group size is large (Levine & Modica, 2016; Sui et al., 2017).
    - Marginal per-capita return (mpcr) is low (Wu et al., 2014), i.e., where cooperation is hard to sustain without punishment.
    - There are sufficient rounds (opportunity for punishment and learning) (Eldakar et al., 2013).
    - Punishment is effective (high fine-to-cost ratio) (Levine & Modica, 2016; Sui et al., 2017).
- **Rewards or hybrid punishment-reward regimes** sometimes yield higher efficiency than punishment alone, but the effect depends on their costs and the game’s structure (Cong et al., 2016; Yao & Chen, 2014).

- **The effect of punishment can be negative (reduce efficiency):**
    - If punishment cost is high, or punishment is poorly targeted (Levine & Modica, 2016; Yao & Chen, 2014).
    - In settings with high rates of antisocial punishment (Sylwester et al., 2013).
    - When punishment is too severe or not balanced with reward (Cong et al., 2016).

- **Institutional variants (tax-based, pool punishment):**
    - Institutional or tax-based punishment can overcome inefficiency caused by costliness or coordination problems with peer punishment (Yao & Chen, 2014; Sasaki, 2014).
    - The balance of participation, monitoring technology, audit rules, and the universality of punishment coverage critically moderates efficiency effects (Levine & Modica, 2016; Nasrallah & Cheaib, 2016).

- **Optional participation:** 
    - Institutional punishment with optional participation is particularly robust in creating high-efficiency outcomes (Sasaki, 2014).

- **Network/Population structure:** 
    - High connectivity and structured interaction (networks) can enhance the efficiency impact of punishment, particularly when punishment/exclusion can be directed correctly (Chung et al., 2013).
    - Reputation and group entry rules can function as alternatives to punishment for efficiency gain (Smaldino & Lubell, 2014).

- **Parameter Sensitivity and Thresholds:**
    - Nonlinearities and thresholds abound: efficiency gains occur only above critical values of punishment effectiveness and below certain cost ratios.
    - Some models find intermediate levels of punishment or mixed strategies (i.e., not always punishing) maximize efficiency (Chen et al., 2014).

- **Summary Table of Effects:**  
    | Situation                        | Efficiency w/Punishment      | Moderators                              |
    |-----------------------------------|-----------------------------|-----------------------------------------|
    | High punishment cost              | No gain or efficiency falls | Wu et al., 2014; Sui et al., 2017      |
    | Low punishment cost               | Efficiency rises            | Wu et al., 2014; Levine & Modica, 2016 |
    | High group size                   | Efficiency rises (if cost low) | Levine & Modica, 2016; Sui et al., 2017 |
    | Reward enabled (w/punishment)     | Reward may outperform punishment or both needed for max effect | Cong et al., 2016; Yao & Chen, 2014 |
    | Optional participation            | Efficiency gains robust     | Sasaki, 2014                             |

*Note: These findings rely on theoretical model validity and may not account for all real-world moderators such as antisocial punishment, implementation errors, or bounded rationality.*

# 5) Prediction Guidance

**How should this literature inform predictions of treatment efficiency (punishment enabled) from game design and control efficiency?**

- **Strong inference can be made** that, all else equal and within the modeled parameter regions:
    - Enabling peer or institutional punishment increases average efficiency above control (no-punishment) levels, *provided that* the punishment is not prohibitively costly, group size is not extremely small, and punishment is effective (high fine-to-cost ratio) (e.g., Levine & Modica, 2016; Sui et al., 2017; Wu et al., 2014).
    - The *increment* (treatment–control) is larger in harder cooperation environments (low mpcr), larger groups, and with efficient (well-targeted, low-cost, high-impact) punishment.

- **Design dimensions to pay particular attention to when predicting efficiency gain from punishment:**
    - **punishment_cost:** Lower cost increases the positive effect on efficiency.
    - **mpcr:** Lower mpcr environments gain more from punishment.
    - **player_count:** Larger groups benefit more from punishment (in terms of efficiency gains from baseline).
    - **punishment_tech:** Effective and well-administered punishment (or institutional forms) have larger positive effects.
    - **reward_exists / reward_cost / reward_tech:** Rewards and their interplay with punishment can moderate or amplify efficiency changes.

- **For any given control efficiency:** The predicted effect of enabling punishment can be estimated from theoretical model outputs, but model-derived increments need to be adjusted for:
    - Punishment cost and effectiveness.
    - Group size and number of rounds.
    - Optional participation and presence of reward mechanisms.
    - Potential for antisocial punishment, though this is noted primarily as a concern rather than formalized in efficiency terms.

- **Extrapolation caution:** 
    - Theoretical models often assume perfect knowledge, rational updating, and absence of implementation errors or complex psychological/cultural realities (e.g., antisocial punishment, bounded rationality).
    - If the real environment includes significant antisocial punishment, high uncertainty, or institutional weaknesses, efficiency gains may be reduced or reversal possible (Sylwester et al., 2013).

# 6) Design Dimensions Highlighted Across Papers

**Most Directly Informed:**
- **player_count** – Modeled and shown to strongly shape punishment efficacy (larger groups benefit more).
- **num_rounds** – Typically present; more rounds give more opportunity for punishment to reinforce cooperation.
- **mpcr** – Central parameter; lower mpcr → higher punishment impact.
- **punishment_cost** – Explicitly varied in almost every model.
- **punishment_tech** – Variations (peer vs. institutional, audit/monitoring, tax-based, etc.) and their effects are analyzed in multiple papers.
- **reward_exists / reward_cost / reward_tech** – Less common, but several models analyze simultaneous punishment/reward or compare them.

**Indirectly Informed:**
- **all_or_nothing** – Some debate on effect (continuous vs. discrete contributions).
- **chat / communication** – Occasionally modeled, often as a contextual moderator (Janssen, 2015), not always primary.
- **show_n_rounds, show_other_summaries, show_punishment_id** – Rarely formalized but sometimes discussed in relation to information structure or transparency.

**Contextually Discussed or Sparse:**
- **default_contrib** – Not systematically addressed; contribution framing not a key focus.
- **show_punishment_id** – Generally mentioned only as part of discussing antisocial punishment moderation/visibility.
- **show_other_summaries** – Occasionally discussed but not as a formal design variable.

**Effectively Missing:**
- Detailed empirical variation on framing, transparency, real-group communication, and norm salience.
- No empirical calibration for cognitive/psychological moderators.

# 7) Important Limitations

- **Lack of empirical data:** The entire evidence base is theoretical; findings may not generalize to real-world or even laboratory behavior due to unmodeled human factors (e.g., risk aversion, mistakes, learning, culture, and bounded rationality).
- **Behavioral outcomes ≠ efficiency:** Many results use cooperation rate or punishment frequency as proxies for efficiency, which can be misleading when punishment is costly or antisocial (costs can negate gains from cooperation).
- **Antisocial punishment and implementation errors** are rarely formalized in theoretical models, despite being a substantial empirical moderator.
- **Parameter and context sensitivity:** Model-based predictions often show threshold or nonlinear effects; extrapolating outside the simulated parameter regions may yield erroneous predictions.
- **Sparse coverage on some design dimensions:** Some prediction variables (e.g., framing, transparency, real-time information display) are under-theorized or missing in the models.
- **Treatment–control predictions are sensitive to model specifics:** For adjacent or non-standard variants (e.g., snowdrift game, trust game), mapping findings to standard PGG design dimensions can be nontrivial.
- **Institutional and social context:** Real-world settings often include norms, habits, legal or cultural constraints, and psychological biases absent from abstract models.
- **No calibration or benchmarking to real experimental data:** Even the most precise theoretical predictions cannot be validated or directly scaled for real-world or laboratory PGG environments.

---

**Summary:**  
The literature set provides a strong, theoretically rich foundation for predicting efficiency effects from punishment in public goods games as a function of core design dimensions (notably group size, rounds, mpcr, and punishment cost/technology). Predictions are likely valid within the boundaries of modeled environments but need to be interpreted cautiously when extrapolating to real or empirical settings, particularly when antisocial punishment or institutional failures may occur. Behavioral (non-payoff) outcomes are frequent and should not be confused with true efficiency unless costs of punishment are explicitly balanced. Several game design dimensions are very well-covered; others are barely addressed. The main gap is the lack of empirical data or testing of model predictions against observed human PGG behavior.
