# Evidence Base

This paper set (n = 90) comprises a predominantly theoretical and computational body of work, with a smaller but notable presence of empirical laboratory experiments and field studies. The literature is broad in coverage of cooperation in social dilemmas, but narrows significantly when focusing on the exact PGG (Public Goods Game) setting with peer punishment and explicit efficiency (payoff/welfare group outcomes). Within this subset, the dominant approach is evolutionary game theory and agent-based modeling; direct empirical (lab or field) studies of efficiency outcomes under punishment are sparser. Many papers report on behavioral outcomes (e.g., cooperation rates, punishment frequency) rather than direct payoff-based outcomes, and several related but non-PGG game paradigms (notably Prisoner’s Dilemma, collective-risk, and commons resource games) are included. Thus, the evidence base is moderately broad in PGGs with punishment but is select and mainly theoretical when strictly requiring direct efficiency or group payoff outcomes as the measure.

# Task Relevance

**pgg_or_variant:**
- **Exact Relevance:** Many topically central papers (e.g., Gao et al., 2020; Liu et al., 2019; Cui et al., 2019) model or analyze standard or direct variants of the public goods game.
- **Close/Adjacent Relevance:** A considerable portion extends to adjacent or related setups—such as collective-risk social dilemmas, common-pool resource games, or repeated donation/PD games with PGG-like mechanics—providing mechanistic insight but not always direct parameter mapping to standard PGGs.
- **Weak/None:** Some portion of the literature focuses on non-PGG dilemmas or high-level mechanism arguments not parameterized for prediction.

**punishment_or_sanctions:**
- **Exact:** Several core papers directly analyze peer or pool punishment mechanisms in PGGs, with explicit modeling of punishment cost, effectiveness, and technology.
- **Close/Adjacent:** Many others consider exclusion, reward, or hybrid (punishment/exclusion/reward) as adjacent, or invoke punishment-like mechanisms (e.g., reputation updates, exclusion, defensive strategies) but not strictly PGG punishment as implemented in empirical games.
- **Weak/None:** A minority lack sanctioning mechanisms altogether, reducing their relevance for the prediction task.

**efficiency_or_related_payoff_outcome:**
- **Exact:** Some central papers directly report group efficiency, total payoff, or average earnings (e.g., Gao et al., 2020; Liu et al., 2019; Murase & Baek, 2021; Gámez et al., 2018).
- **Close/Adjacent:** Many more report cooperation or contribution rates, sometimes with subsidiary payoff analysis or simulation-level average payoffs. A significant proportion, while theorizing on efficiency, only report on behavioral proxies (cooperation, punishment frequency).
- **Weak/None:** Some focus exclusively on non-payoff behavioral metrics or evolutionary dynamic attractors without quantifying efficiency.

# Outcomes Measured In The Literature

- **Payoff-Related Outcomes**: 
    - Efficiency (group payoff as a fraction of possible maximum)
    - Average group payoff/welfare, surplus, total coins/earnings
    - Explicit in several theoretical/modeling studies and a few experimental ones (e.g., Gao et al., 2020; Liu et al., 2019; Gámez et al., 2018; Murase & Baek, 2021)
    - Sometimes adjacent or only implied: e.g., higher cooperation interpreted as higher efficiency, without direct payoff quantification.
- **Non-Payoff Behavioral Outcomes**:
    - Cooperation/contribution rates, punishment frequency, prevalence of strategists (punishers, excluders, etc.)
    - Evolutionary/dynamical stable states or attractors (e.g., coexistence, dominance, cycling of strategies)
    - Strategy and norm compliance rates, sometimes connected to incentives or sanction prevalence
    - These are reported much more frequently, but must not be conflated with efficiency per instructions.

# Main Findings Relevant To Prediction

## Punishment Effects on Efficiency (Empirical and Theoretical)

- **Theoretical Consensus in PGGs:** 
    - **Enabling peer or pool punishment typically increases group efficiency** (payoff as defined) versus control, *when* cost and impact are favorably balanced and the threat of corruption or antisocial use of sanctions is low (Gao et al., 2020; Liu et al., 2019; Cui et al., 2019; Liu et al., 2018).
    - **Effect Size Is Moderated:** The increase in efficiency depends on the punishment cost, effectiveness (`punishment_cost`, `punishment_tech`), group size (`player_count`), synergy/MPCR (`mpcr`), consensus threshold (collective decision requirement for punishment in some models), and, in pool punishment, the risk of corruption/bribery (Liu et al., 2019).
    - **Pool vs Peer Punishment:** Models find both can raise efficiency, but context (networked vs. well-mixed; consensus mechanisms) determines which is more robust or more efficient. Autonomous (individual) punishment can be less effective in large groups unless costly; consensual punishment (voted) is preferred at low consensus thresholds.
    - **Switching/Hybrid Mechanisms:** Models incorporating exclusion or switching between punishment and exclusion (or reward/punishment) mechanisms can outperform pure punishment in promoting efficiency, especially as the number of defectors varies (Liu et al., 2018; Liu & Chen, 2020).
    - **Parameter Sensitivity:** Very high or low punishment cost or fine is suboptimal—moderate (intermediate) values can maximize efficiency (Zhang et al., 2020; Cui et al., 2019).

- **Empirical and Adjacently Empirical Evidence:**
    - Where measured, **punishment in repeated/lab experiments tends to increase group payoff/efficiency relative to no-punishment controls**, particularly in low baseline cooperation environments (Zhao et al., 2018; Gámez et al., 2018). However, efficiency gains can be diminished or reversed if punishment is applied inefficiently (e.g., antisocial or envy-based punishment, high cost to punishers, or insufficient returns).
    - **Contextual and Conditional Results:** Punishment does not always improve efficiency—when it is rarely used, poorly targeted, or where ecological dynamics (in collective-risk or resource settings) limit the benefit of higher cooperation, efficiency gains may be small or even negative (Chen & Szolnoki, 2018; Wang et al., 2020 [resource games]).
    - **Non-PGG Evidence:** Several adjacent studies (e.g., on PD games, team production, bargaining/coercion models) reinforce the point that the **cost–benefit structure of punishment and the organization of group power** (e.g., symmetry vs. leader-based) are decisive for whether punishment increases efficiency, but their structural differences limit direct parameter mapping.

- **Negative and Mixed Evidence:**
    - If **punishment options are bilateral/mutual** (allowing for retaliation or “feuding”) in a two-sided game, enabling punishment can reduce efficiency (Bolton et al., 2018).
    - If **punishment is subject to corruption/bribery or manipulation**, the efficiency effect can be neutral or negative (Liu et al., 2019).
    - In hybrid sanction and reward environments, too generous rewards or excessive punishment can also reduce efficiency by imposing higher costs (Zhang et al., 2020; Chen, Q. et al., 2019).

- **Network and Behavioral Moderators:**
    - **Network Structure:** Spatial and networked PGGs show that punishment is more effective at increasing efficiency when network features or leader positioning reinforce the efficacy or focus of punishment (Wang & Guo, 2019; Liu & Chen, 2020).
    - **Communication and Information:** The ability to chat, observe others' actions, or publicize outcomes can strengthen the effect of punishment on efficiency by lowering monitoring costs and reinforcing norms (Song et al., 2020).
    - **Social Norms, Reputation, and Leader Effects:** Public reputation and strong norms (favoring cooperation and norm-enforcing punishment) increase both cooperation and efficiency, but private/fragmented reputation can blunt effect (Quan et al., 2021).

# Prediction Guidance

Drawing on the strongest and most relevant evidence:

- **Baseline Expectation:** If group efficiency under control (no punishment) is known, enabling peer punishment will generally (but not universally) increase group efficiency. The expected increment is moderated by:
    - **Punishment design:** Lower punishment cost and higher punishment effectiveness (fine per unit cost) increase the efficiency benefit. Extremely high costs or low impact can erase the benefit or reverse it.
    - **Group Size and Structure:** Efficiency gains are generally maintained as player count increases, but very large groups can dilute the impact of punishment unless the technology scales (Gao et al., 2020; Cui et al., 2019). Network topology, reputation, and presence of leaders can magnify punishment effectiveness.
    - **Synergy/MPCR:** Low baseline MPCR often has low cooperation and efficiency, so the marginal effect of punishment is higher (and sometimes necessary for meaningful efficiency). High MPCR may diminish the added effect, especially if baseline efficiency is already high.
    - **Consensus Mechanisms:** For models with collective punishment, low consensus thresholds and high willingness to punish amplify positive effects on efficiency.
    - **Sanctioning Context:** The mechanism of punishment matters—autonomous, consensual, pool-based, or exclusion-based sanctions differ in how they moderate efficiency.
    - **Information/Communication:** If the environment allows chat, summary displays, or reputation tracking, the deterrent effect of punishment is increased and efficiency benefit is likely greater.
    - **Ecological/Resource Settings:** In public goods variants with resource dynamics (commons), punishment only boosts efficiency if the resource can recover; if renewable capacity is too low, even perfect cooperation enforced by punishment won’t improve efficiency.
    - **Corruption/Bribery and Bilateral Punishment:** If sanctioning can be subverted (corruption) or is equally available to all (enabling feuds), punishment does not reliably improve—and can reduce—efficiency.
    - **Design Interactions:** Addition of reward options, identification mechanisms, and the relative magnitude of costs/fines to contributions can impact the efficacy of punishment on efficiency.

- **Use of Non-Payoff Outcome Evidence:** Strong findings that punishment increases cooperation rates can be tentatively taken as supporting higher efficiency, but only when the cost of punishment is not excessive relative to its benefit and when net group payoff is prioritized in the design.

- **Predictive Gaps:** Where the exact outcome is not efficiency or group payoff (but rather behavioral rates), prediction must default to cautiously positive expectation (efficiency likely to increase), unless costs are unmodeled or context suggests net cost may outweigh benefits.

# Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- `player_count`: Core parameter in almost all theoretical models; evidence shows group size affects punishment effectiveness.
- `num_rounds`: Infinite or fixed round numbers modeled; repeated games enhance punishment utility (Murase & Baek, 2021).
- `mpcr`: The marginal per capita return is central in nearly all models and modulates both the baseline and the effectiveness of punishment.
- `all_or_nothing`: Discrete vs. continuous contribution structures are modeled, with effects on strategy space.
- `punishment_cost` and `punishment_tech`: Key in most punishment mechanism studies and often directly parameterized.
- `reward_exists`, `reward_cost`, `reward_tech`: Many studies contrast or combine reward and punishment; presence of rewards moderates punishment efficacy.
- `show_other_summaries`, `show_n_rounds`: Sometimes directly modeled (especially information feedback studies); evidence supports importance of transparency.
- `chat`: Less commonly modeled, but evidence (adjacent) suggests communication dramatically increases the effect of punishment (Song et al., 2020).

**Indirectly Informed/Contextual:**
- `default_contrib`: Some framing models (default contribute/keep) touch on this indirectly, but not always a primary parameter.
- `show_punishment_id`: Occasionally modeled as reputation or group feedback mechanism (public vs. private punishers).
- `punishment_tech` and `punishment_cost` are often collapsed into a single effective parameter (fine per cost), which may obscure interaction effects.

**Missing/Underexplored:**
- Effects of `chat` are rarely parameterized directly in payoff modeling; often inferred from qualitative or experimental studies.
- `default_contrib`, `show_punishment_id`, and the interplay between visibility/identification and efficiency are not deeply explored.
- Simultaneous manipulation of all or multiple dimensions is rare; most models hold all but a few parameters constant.

# Important Limitations

- **Dominance of Theoretical Over Empirical Evidence:** Most high-relevance findings are theoretical; real-world/lab data with direct efficiency outcomes under peer punishment are rare, limiting external validity.
- **Behavioral vs. Payoff Outcomes:** The overwhelming frequency of cooperation/contribution rates as outcomes requires careful inference to efficiency, especially when punishment is costly or inefficient.
- **Adjacency and Structural Non-Equivalence:** Many “close” or “adjacent” papers concern games with different strategic structures (e.g., PD, collective-risk, resource games), which may not map linearly to PGGs.
- **Parameter Coverage Gaps:** Not all prediction dimensions are equally well represented—e.g., chat, visibility of punishment, contribution framing are underexplored.
- **Corruption, Antisocial Punishment, and Collusion Uncertainty:** Several papers highlight that under certain structural or institutional conditions (availability of retaliation, potential for corruption, or asymmetric power), punishment can fail to increase—and may decrease—efficiency.
- **Ecological Context and Resource Dynamics:** In public goods games with resource dynamics, punishment may not safeguard efficiency if resources are depleted regardless of behavior.
- **Sample/Population Differences:** Many models use infinite populations, synchronous updating, or idealized rational/learning agents, in contrast to finite and mixed-motive human lab settings.
- **Limited Quantitative Effect Sizes:** Few papers provide empirical or simulation-derived numerical mappings of efficiency gain across parameter space, complicating precise prediction.

---

**In summary:**  
The literature provides robust theoretical support for the expectation that enabling peer punishment in public goods games will increase group efficiency, relative to control, *if* the cost–benefit structure (technology, cost, impact, network structure, information) is favorable. The predicted magnitude and certainty of efficiency gain are conditional on group size, punishment detail, baseline cooperation, and moderator variables like communication and corruption. Caution is due when inferring from non-payoff outcomes, mapping findings from adjacent or non-standard games, or applying results to under-explored design dimensions such as chat availability and contribution framing.
