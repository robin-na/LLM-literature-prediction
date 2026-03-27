# 1) Evidence Base

The paper set is **large (N=190)** and consists entirely of **theoretical and simulation studies**—there are **no primary empirical studies or field/experimental interventions**. All analyses focus on **public goods games (PGGs) or very close variants**, ensuring maximal formal relevance for public-goods-game-like environments. The evidence is wide-ranging in model architectures (well-mixed vs. spatial, voluntary vs. compulsory participation, peer vs. institutional punishment, exclusion/punishment/reward variants, and settings with communication, corruption, insurance, etc.), as well as in the **outcomes** and **design dimension focus**. The coverage is thus **broad and deep for theoretical mechanism and parameter mapping** relevant to predicting treatment efficiency, but **lacks direct empirical effect size calibration**.

The evidence base is **strongest on evolutionary and dynamic mechanisms, parameter thresholds, phase diagrams**, and the interactions among **game design dimensions**—ideal for mapping model architecture to expected treatment efficiency but requiring caution in generalizing to real-world effect sizes or heterogeneity.

# 2) Task Relevance

**pgg_or_variant:**  
- **Exact relevance:** Nearly all papers directly model PGGs or immediate close variants (threshold/CPR/dynamic resource, multi-species cycles, etc.).  
- **'Close' (not 'exact')**: A subset formally models CPRs or resource games with feedback or cyclical eco-dynamics, but the mapping to PGG structure and efficiency (relative to a cooperative optimum) is always made explicit.

**punishment_or_sanctions:**  
- **Exact relevance:** The vast majority analyze the introduction of punishment or closely related sanctions (peer, institutional, pool, exclusion, coordinated, probabilistic, etc.), including mechanistic variants such as anti-social and second-order punishment, bribery, and exclusion.  
- **Reward** and **hybrid** mechanisms are often covered as additional dimensions.  
- **Variants:** Some studies focus on exclusion/social ostracism or self-commitment as alternate forms of ‘sanction’, and these models are noted as close but not identical to canonical peer punishment.

**efficiency_or_related_payoff_outcome:**  
- **Exact/close relevance:** Efficiency is operationalized throughout as mean group payoff or welfare as a fraction of the fully cooperative optimum, or as closely analogous outcomes such as group achievement in climate dilemmas or sustainable resource levels. Many studies provide phase diagrams or explicit payoff mapping.  
- **Mixed relevance:** Some also report on institutional (not group) cost minimization, or report dynamic (not static) payoffs; a few use surrogate efficiency measures (e.g., frequency of cooperative equilibria, or eco-resource levels).  
- **Behavioral outcomes (e.g., cooperation rates) are distinguished from payoff-based efficiency**, and are only directly interpreted as efficiency when explicitly linked. Many studies emphasize the divergence between increased contributions and group efficiency (costly punishment can increase cooperation but reduce efficiency).

**Overall:**  
- The literature is **of maximal structural and mechanisms relevance** for the prediction task, offers direct mapping from design dimensions and control efficiency to treatment efficiency in theory and simulation, and extensively addresses **payoff-based outcomes**.  
- **Empirical transferability** and **calibration** to realized effect sizes in actual human groups are not addressed.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes (primary focus):**
- Treatments' effect on **group efficiency** (mean payoff relative to social optimum) is directly analyzed in nearly every study.
- Related/analogous outcomes: group welfare, total earnings, group achievement, resource sustainability, normalized utility/payoff, total number of resource units produced/retained.
- Many studies provide **phase diagrams or threshold conditions** for transitions from low to high efficiency.
- Some studies model **institutional cost efficiency** (cost per unit of achieved cooperation), which can be mapped to group efficiency.

**Non-payoff behavioral outcomes (explicitly distinguished):**
- **Contribution rates**, cooperation frequencies, prevalence of strategy types.
- Frequency or state of punishers/rewarders/excluders.
- Norm compliance, reputation, using communication or observation.
- The relationship between increased cooperation and increased efficiency is highlighted as **non-monotonic**: punishment may increase cooperation but reduce efficiency due to resource-burning **costs of sanctioning** (notably in lab-like or high-cost settings).
- Robustness and evolutionary stability of cooperation and punishment strategies are frequently a secondary focus.

**Explicit dichotomy:**  
- Many papers stress that **punishment** increases contributions/cooperation while **group efficiency may decrease** if punishment is wastefully costly, is anti-social, or induces retaliation. Efficiency gains are robust only under specific cost/impact and institutional arrangements.

# 4) Main Findings Relevant To Prediction

**Synthesis Across Papers:**
- **Enabling punishment typically increases efficiency** relative to control (no-punishment) in PGG-like environments, *provided* that certain design conditions are met.

- The **magnitude and even the sign** of the effect of punishment on efficiency is **conditional**—positive effects are found when:
    - Punishment cost is not excessive relative to impact (punishment_cost, punishment_tech).
    - Anti-social or retaliatory punishment is prevented or rare.
    - Second-order free-riding is addressed (e.g., via second-order punishment, reward to punishers, or exclusion).
    - There is sufficient monitoring, transparency, and identification to support effective punishment.
    - Group size and structure (player_count, network structure) support norm enforcement (smaller or networked groups, or hierarchies/institutions in large groups).
    - The baseline control efficiency is low (high baseline efficiency leaves less room for improvement).
    - Participation is voluntary, or punishment is institutionally coordinated rather than solely peer-driven (especially for tax-based, shared, or exclusionary regimes).
    - Parameter thresholds are surpassed (e.g., minimal fine/cost ratio, coverage of institution, critical mass of punishers).

- **Negative, null, or ambiguous effects** arise when:
    - Punishment is costly and/or inefficient (low fine-to-cost ratio).
    - Anti-social punishment or retaliation is prevalent.
    - Exclusion, bribery, or insurance allow defectors to evade sanction too cheaply.
    - Enforcement institutions are corrupt or unobservable.
    - Resource dynamics are limiting (e.g., in CPR games, efficiency cannot exceed sustainability constraints even with full cooperation).
    - Structural constraints: large groups without sufficient structure, weak monitoring, or with rival, expensive, or non-institutional enforcement.
    - The presence of multiple stable equilibria or strong path dependence: punishment may allow either high or low-efficiency states depending on initial conditions and stochastic events.
    - In some ecological or resource games, efficiency cannot improve if resource replenishment is too low, regardless of the cooperation rate.
 
- **Hybrid regimes** (adaptive/targeted punishment, reward for punishers, dynamic punishment/reward, probabilistic/fractional punishment) often perform best—yielding high efficiency at lower cost.

- **Exclusion mechanisms** can outperform standard punishment in supporting efficient cooperation, especially in well-designed peer/pool exclusion regimes.

- **Reward mechanisms**: Enabling reward (often in combination with punishment) can outperform or match punishment in efficiency under some conditions, but punishment is generally more robust at deterring defectors and sustaining cooperation.

- **Key moderators**: Control (no-punishment) efficiency, player_count, mpcr, punishment_cost, punishment_tech (fine/impact), number of rounds, chat and communication, institutional or peer punishment, optional/compulsory participation, possibility of anti-social punishment, reward_exists/reward_cost, possibility for exclusion or meta-norms.

# 5) Prediction Guidance

The literature provides **detailed, dimension-level guidance** for predicting treatment efficiency from game design and control (no-punishment) efficiency:

- **Baseline rule**: **If control efficiency is low (due to high defection), and punishment is enabled and not prohibitively costly, expect a significant increase in efficiency**—often approaching the fully cooperative benchmark in idealized models.

- **Magnitude and conditionals**:
    - **Positive effect**: When punishment cost is low-to-moderate, impact is high, group size is manageable, enforcement is transparent and anti-social punishment is rare/absent, and the institution is well-aligned with the social good (institutional, tax-based, or shared).
    - **Minimal or negative effect**: When punishment is costly, anti-social or retaliatory punishment occurs, enforcement is corrupt or ineffective, or baseline efficiency is already high.
    - **Null or context-dependent effect**: If resource replenishment is too slow (in CPR models), or if the payoff structure (e.g., meta-norm requirement, risk/threshold, non-linear benefit function) does not support efficiency gains from increased cooperation.

- **Moderator mapping**:
    - **Player count (player_count)**: Smaller groups—easier enforcement, larger groups require stronger institutions.
    - **Num rounds (num_rounds)**: Longer games allow initial costs to be amortized and for efficiency to increase over time as cooperation stabilizes.
    - **MPCR**: Higher mpcr increases both the base returns to cooperation and the effectiveness of punishment in shifting the equilibrium.
    - **Punishment cost and technology**: Lower punishment_cost and/or higher punishment_tech (cost-to-impact) strongly increase the likelihood and size of positive efficiency effects.
    - **Punishment type (punishment_tech)**: Peer vs. pool, social exclusion, tax-based, probabilistic/fractional, meta-norms.
    - **Optional participation, exclusion mechanisms, reward available, and visibility of enforcement** all act as substantial moderators.
    - **Control efficiency**: If the control efficiency is already near the cooperative optimum, the potential for punishment to raise efficiency is limited.

- **Empirical caution**: All the above statements rest on theoretical and simulation grounds; while mechanism mapping is robust, the **effect size magnitude** is not empirically calibrated and could differ in real-world or behaviorally heterogeneous populations.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions** (strong, parameterized evidence available in most papers):  
- player_count
- num_rounds
- all_or_nothing
- mpcr
- punishment_cost
- punishment_tech (fine/impact structures, risk of anti-social, exclusion vs. peer/pool/institutional, possibility of probabilistic/fractional punishment)
- reward_exists, reward_cost, reward_tech

**Frequently, but less precisely, informed**:  
- show_n_rounds (sometimes tracked as information/feedback)
- show_other_summaries (outcome or peer information; present in observability and reputation models)
- show_punishment_id (transparency/monitoring/corruptibility)
- chat (communication: highlighted for its capacity to moderate/replace punishment in elevating efficiency or for coordination, but not structurally modeled in most papers)
- default_contrib (framing opt-in/opt-out): Rarely modeled explicitly but may be inferred from initial condition and participation structures.

**Sparse/only contextually addressed or missing:**  
- Some game features such as **chat** (concurrent communication), or nuanced user interface details/feedback, are sparingly treated and lack robust simulation/theoretical results relating those to efficiency.
- **Information structure** and feedback (show_other_summaries, show_punishment_id) are discussed in information/reputation/corruption studies.
- **Control and transparency of institution (e.g., who designs/controls institutions, voting on enforcement levels)** are covered in certain institutional and 'endogenous-punishment' models.

**Summary:** The literature **most comprehensively informs** prediction for treatment efficiency as a function of **player_count, num_rounds, mpcr, all_or_nothing, punishment_cost, punishment_tech, and reward system variables**. Other dimensions such as chat, feedback, and transparency are discussed, but with less frequency or parametric clarity.

# 7) Important Limitations

- **No primary empirical effect sizes:** All results are theoretical or simulation-based; **quantitative predictions** for real human subjects or field interventions may not transfer directly.

- **Behavioral scope:** Theoretical models assume **rational, homogenous, or stylized agents** and may not capture **heterogeneity, learning, psychology, norms, or noise** as observed in lab/field studies.

- **Parameter sensitivity and bistability:** Many models feature **phase transitions, critical thresholds, and multiple equilibria**; small parameter changes or initial condition variation may cause large differences in efficiency outcomes (i.e., the effect of enabling punishment can be ‘all or nothing’ depending on thresholds being crossed).

- **Limited design dimension coverage:** **Some design features** (notably **chat**, framing, and most user-interface/experimental display parameters) are rarely if ever analyzed for their effect on efficiency.

- **Feature interactions:** The effect of punishment on efficiency is often **interdependent**, not additive, with other design features (reward, exclusion, monitoring tech, etc.). Pure main effects models may be misleading.

- **Negative and null results under-reported:** While positive effects are robustly supported when conditions are right, **many models stress costs, anti-social punishment, retaliation, corruption, insufficiently powerful incentives, or resource limitations** as reasons for neutral or negative effects on efficiency.

- **External validity/cultural context:** Some reviews caution against over-generalizing from theoretical models to real-world differences in communication, reputation, or culture that may alter punishment’s efficiency effects.

- **No robust treatment of dynamic/changing preferences or endogeneity** of player types, group composition, or long-term evolutionary change in social environment.

**In summary**: The literature provides **mechanistically rich, dimensionally detailed, and outcome-specific theoretical and simulation guidance** for predicting how enabling punishment changes efficiency in public-goods-game-like environments, but predictions must be **conditioned on design dimensions, control efficiency, and key moderators**. Empirical calibration and consideration of behavioral, cultural, and institutional context are essential for practical application.
