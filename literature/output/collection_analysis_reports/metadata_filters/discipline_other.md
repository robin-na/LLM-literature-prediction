# Evidence Base

The paper set comprises a substantial mix of empirical (mainly lab experiments, some field/observational) and theoretical/modeling studies, with a strong focus on public goods games (PGGs), PGG-like variants, and adjacent social dilemmas. Among the 193 summaries, the evidence base is **broad but uneven**: for direct (canonical lab) PGGs with peer punishment and measured efficiency or group payoff, there is a robust empirical core. Surrounding this are many theoretical papers and studies of adjacent games or real-world analogues that inform mechanisms, moderators, and behavioral underpinnings of punishment, but do not always measure efficiency directly or use standard PGGs.

Empirical findings are richly represented, especially for standard linear PGGs with and without punishment, as well as core design dimensions (player count, rounds, MPCR, punishment cost/tech, etc.). However, the empirical base is thinner for more complex institutional arrangements (e.g., second-order punishment, voting on punishment rules, variable group sizes, group formation, endowment inequality) and for large-scale field or observational settings.

# Task Relevance

### 1. pgg_or_variant
- **exact:** The literature contains a high volume of studies with *exact* relevance—standard lab PGGs (e.g., linear or VCM), sometimes with continuous or binary contributions and peer punishment, and several with measured group efficiency or payoff as a primary outcome.
- **close:** Many papers examine PGG variants (e.g., threshold games, CPR games, step-level or nonlinear PGGs, networked/partner matching, or games with exclusion/sanctioning institutions), lending 'close' relevance but sometimes with altered strategic structure.
- **adjacent:** A large number of studies model or empirically analyze adjacent dilemmas (e.g., trust games, prisoner's dilemma, dictator games, principal-agent/moral hazard games), field interventions, evolutionary models, or real-world resource governance.

### 2. punishment_or_sanctions
- **exact:** Many papers directly enable/disable punishment or compare punishment to other sanction/reward systems within classic PGGs—here, the task relevance is exact.
- **close/adjacent:** Other papers model or measure institutional punishment, exclusion, taxation, fines, regulatory interventions, gossip, or reputation-based sanctions as analogues or complements to costly peer punishment.
- **weak/none:** Some influential papers discuss only reward mechanisms, communication, or institution building, or focus solely on settings without the possibility of formal or informal punishment.

### 3. efficiency_or_related_payoff_outcome
- **exact:** Robust empirical and theoretical evidence exists reporting group efficiency (payoff relative to cooperative optimum), total earnings, surplus, or welfare, especially in lab settings.
- **close:** Several papers report on group payoff/earnings without normalizing by the social optimum, or use proxies (resource survival, successful thresholds, market profit).
- **adjacent/weak:** Many papers focus primarily on contribution/cooperation rates, punishment frequency, norm compliance, or qualitative descriptions of group success, with efficiency as a background concept rather than a measured outcome.

# Outcomes Measured In The Literature

- **Payoff-related outcomes:** These include group efficiency (group payoff as share of the fully cooperative maximum), total earnings, welfare, mean group profit, or group surplus. These are commonly reported in the canonical PGG literature with and without punishment, as well as in some theoretical models.
- **Non-payoff behavioral outcomes:** These include cooperation/contribution rates, frequency and targeting of punishment (including anti-social punishment), norm compliance, ostracism/exclusion rates, voting choices, psychological/emotional responses, group formation and exit, and responses to communication or reputation mechanisms. Many papers rely primarily or solely on these outcomes.
- **Mixed or proxy outcomes:** Some studies report behavioral proxies (e.g., conditional cooperation, group investment in infrastructure, threshold achievements, resource survival). These can be close correlates of efficiency but require caution.

**Explicit separation between these outcome types is critical**—payoff-based efficiency increases may not coincide with increases in contribution or punishment behavior, particularly when punishment is costly or anti-social punishment is common.

# Main Findings Relevant To Prediction

Synthesis across the core literature reveals several converging themes and some divergences:

- **Punishment increases cooperation/contributions but does not universally increase efficiency.** Empirical lab PGGs show that enabling peer punishment generally raises cooperation but, due to the direct costs of punishment, group efficiency often stays the same or even declines unless punishment is highly effective/cost-efficient and/or the game is sufficiently long to allow punishment use to decay as cooperation stabilizes (e.g., Grechenig et al., 2010; Engel & Zhurakhovska, 2017; related lab studies).
- **Design dimensions that moderate the punishment–efficiency relationship:**  
    - *Punishment effectiveness* (cost/fine ratio): Efficiency gains appear only if punishment is sufficiently severe relative to its cost; otherwise, costs outweigh benefits (Yamagishi, 1986; relevant empirical findings).
    - *Number of rounds (time horizon):* Short games often see efficiency losses from punishment because costs are incurred before stable high cooperation emerges. In longer games, efficiency can surpass controls as punishment use falls (Frey & Rusch, 2012).
    - *Information structure/accuracy:* Accurate monitoring is necessary for punishment to be well-targeted and effective; under noisy information, anti-social or misdirected punishment erodes efficiency (Grechenig et al., 2010).
    - *Institutional form:* Democratic or endogenously chosen punishment systems, or centralized punishment (by elected/judicial authorities), can maintain or even raise efficiency, often by reducing anti-social punishment and coordinating enforcement (multiple sources).
    - *Punishment technology (peer, pool, exclusion, dynamic/static):* Variants like exclusion often increase efficiency compared to costly peer punishment, especially when properly targeted and anti-social punishment is rare (Liu et al., 2019; comparative studies).
    - *Group structure/endowment heterogeneity:* In some CPR variants, punishment's efficiency effect is positive only when inequality creates a focal norm and coordination point; otherwise, it may degrade earnings (De Geest & Kingsley, 2021).
    - *Matching structure:* Random rematching tends to make punishment more effective and less retaliatory; fixed matching/partnering often allows retaliation to undermine efficiency (empirical studies).
    - *Communication and feedback mechanisms:* The presence of chat or tailored feedback can increase baseline efficiency and can substitute for or interact with the effect of punishment.
- **Control game efficiency as a predictor:** Control (no-punishment) efficiency is a strong baseline predictor. Where control efficiency is already high, enabling punishment often has little or even a negative effect; with low baseline efficiency, punishment is more likely to catalyze large increases (Vasconcelos et al., 2022; multiple empirical papers).
- **Contextual constraints:** Field experiments in real-world commons sometimes show that punishment (especially externally imposed) can crowd out intrinsic motivation and *reduce* efficiency or cooperative investment (Amirova et al., 2022).
- **Qualitative mechanism insights:** Punishment is more likely to increase efficiency if it is (a) accurately applied to defectors, (b) not offset by anti-social/counter-punishment, (c) less costly or more impactful, (d) seen as legitimate (democratically chosen, institutionalized), and (e) embedded in repeated, stable group contexts.

# Prediction Guidance

- **General rule:** Do **not** assume that enabling peer punishment will increase efficiency across all PGG variants. Predict an efficiency gain *only* when supporting design features (e.g., high punishment effectiveness, long horizon, accurate information, low baseline efficiency, well-coordinated/institutionalized punishment) are present. Otherwise, expect a neutral or negative effect on efficiency, even with increased cooperation.
- **When control efficiency is known:** If control (no-punishment) efficiency is low and the design allows targeted, effective, not-too-costly punishment in a repeated game, predict a strong efficiency boost from adding punishment. If control efficiency is moderate to high, and/or if punishment is individually costly, short-run, or vulnerable to anti-social use, predict little change or a slight reduction in efficiency relative to control.
- **Moderators to incorporate:**
    - *Punishment cost/tech (cost/impact ratio):* High cost-to-impact ratios predict negative or no effect; low ratios predict positive effect.
    - *Game length (num_rounds):* Short games predict negative/neutral effect; longer games predict increasingly positive effect as punishment costs subside.
    - *Group composition and structure (player_count, matching):* Larger, stranger-matched groups with no communication reduce the efficiency impact; stable groups and/or chat allow positive effects to emerge.
    - *Information structure (show_other_summaries, accuracy):* Noisy or limited information about contributions reduces the efficiency impact or can reverse it.
    - *Institutional design (punishment_tech, voting, exclusion vs. peer):* Centralized, voted, or exclusion-based punishment predicts higher efficiency impact, especially with collective/group choice; peer punishment may reduce efficiency due to mis-targeting and cost.
    - *Reward presence (reward_exists):* Where reward is available, its effect on efficiency may substitute or interact with punishment's effect (can reduce the use and need for punishment, at times supporting higher efficiency).
- **Complex/adjacent settings:** For settings using non-standard payoffs, CPR, or threshold games, use caution and default to "effect is likely positive if design enables accurate, low-cost, well-targeted sanctions; otherwise, expect weak or negative effects."
- **Behavioral outcomes vs. efficiency:** Never substitute increased cooperation/contribution rate or punishment frequency for actual efficiency increases unless a direct group payoff or surplus is reported.

# Design Dimensions Highlighted Across Papers

**Best-informed (direct or strong indirect evidence):**
- `player_count`
- `num_rounds`
- `punishment_cost` and `punishment_tech` (especially cost/fine ratio)
- `mpcr`
- `all_or_nothing` (continuous vs. binary contributions)
- `chat` (communication effect on baseline and interaction with punishment)
- `show_other_summaries` (information/feedback)
- `reward_exists` (and reward/punishment interaction in some studies)

**Indirectly informed or contextually discussed:**
- `default_contrib` (framing: opt-in/out) — rarely directly varied but occasionally mentioned as a moderator
- `show_n_rounds` (salience of game length) — included as manipulation; influences learning/punishment decay
- `show_punishment_id` (anonymity vs. transparency of punishment) — affects antisocial/counter-punishment in some studies

**Sparse or missing:**
- `reward_cost`, `reward_tech` — less commonly varied; more attention in adjacent or reward-centric studies
- `show_other_summaries`/`show_punishment_id` — sometimes specified but seldom the main manipulation relevant to efficiency
- Combined or cross-dimension treatments (e.g., reward + punishment, complex institutional overlays, endogenous group formation) are less empirically developed

# Important Limitations

- **Efficiency outcome measurement is not universal:** Many studies report only behavioral or cooperation outcomes, making translation to payoff-based efficiency predictions problematic in those cases.
- **Parameter scope:** Direct, high-powered lab evidence is abundant for moderate group sizes (3–5), repeated games (often 10–20 rounds), and standard linear PGGs, but thinner for large groups, field games, nonlinear/threshold environments, or complex institutional variables (dynamic punishment, exclusion, reward/punishment mixes, endogenous rules).
- **Anti-social punishment and counter-punishment:** Several studies highlight that anti-social punishment or counter-punishment can fully or partially offset efficiency gains, especially when punishment is not coordinated or is individually initiated.
- **External validity and field context:** Field experiments and real-world case studies sometimes diverge sharply from lab findings—punishment can crowd out motivation, be infeasible, or lose legitimacy, neutralizing or reversing lab-based predictions.
- **Complexity of mechanism interplay:** Many papers discuss interaction effects (communication + punishment, endogenous institution selection, group formation rules) that are incompletely explored in empirical work.
- **Aggressive generalization:** The literature strongly cautions against assuming a positive punishment–efficiency link without reference to cost/technology, error/accuracy, group structure, and baseline efficiency. Predictive models that do not interact design dimensions may be unreliable.
- **Missing or sparse dimensions:** Some important design features, especially those that interact with punishment (reward mechanisms, dynamic institution choice, role of transparency, real-world group composition), remain under-explored relative to core dimensions.

---

**Summary:**  
Laboratory and theoretical research provides strong, nuanced evidence that the effect of enabling punishment on group efficiency in public-goods-game-like environments is *not* uniformly positive: it is highly design-dependent. Predicting treatment efficiency from control efficiency and design dimensions requires incorporating the cost-efficiency of punishment, information structure, institutional design, and time horizon as critical moderators. Outcomes must be explicitly payoff-based, and the limitations of extrapolating behavioral proxies or results from adjacent settings should be respected. While many design dimensions are well studied, combinatorial and institutional complexities are less often empirically addressed. External validity into field settings remains a significant caveat.
