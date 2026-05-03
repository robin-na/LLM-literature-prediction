# 1) Evidence Base

The paper set consists of three works, all of which are theory-focused and none of which report new empirical or experimental data. The evidence base is quite narrow for the downstream prediction of efficiency effects of punishment in public-goods-game-like environments. Only one paper (Vasconcelos et al., 2013) presents a formal theoretical model directly related to threshold public goods games with punishment; the other two papers (Cushman, 2015; Clavien & Chapuisat, 2013) are conceptual and discuss general arguments about punishment, cooperation, and related behavioral concepts. There is no direct experimental or quantitative empirical literature in this set on payoff or efficiency outcomes.

# 2) Task Relevance

**pgg_or_variant**
- **Vasconcelos et al. (2013):** Relevance is **close**; the model examines a threshold public goods game (a specific variant).
- **Cushman (2015):** Relevance is **adjacent**; discusses PG games and experimental evidence but abstracts over many designs.
- **Clavien & Chapuisat (2013):** Relevance is **adjacent**; refers generally to public goods games in discussing definitional issues.

**punishment_or_sanctions**
- **Vasconcelos et al. (2013):** **Exact**; focuses on local sanctioning institutions, a direct analogue to peer punishment.
- **Cushman (2015):** **Exact**; conceptualizes punishment's role in human cooperation and experiments.
- **Clavien & Chapuisat (2013):** **Adjacent**; discusses punishment mostly to clarify terminological confusion.

**efficiency_or_related_payoff_outcome**
- **Vasconcelos et al. (2013):** **Adjacent**; does not report efficiency per se but models 'group achievement' (group success in meeting threshold), a close proxy.
- **Cushman (2015):** **Adjacent**; notes that punishment can increase or decrease group welfare but provides no empirical data.
- **Clavien & Chapuisat (2013):** **Weak**; mainly stresses distinctions between outcome and motivation, not results.

**Summary:** The literature is most relevant for conceptual and theoretical discussions of punishment and institutional design. Direct evidence on treatment efficiency, especially quantitative, is missing.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes**  
- **Vasconcelos et al. (2013):** Does *not* report group payoff or efficiency directly, but does model 'group achievement' (i.e., rate at which groups reach the public good threshold). This is closely related to efficiency in threshold settings but is not equivalent; any efficiency statements are inferred, not measured.
- **Cushman (2015):** Discusses group welfare and payoff implications theoretically, with references to cycles of retaliation, but provides no quantitative or even qualitative empirical findings on payoffs or efficiency.
- **Clavien & Chapuisat (2013):** Does not discuss payoffs or efficiency as primary outcomes; focuses on definitional clarity.

**Non-payoff behavioral outcomes**
- **Vasconcelos et al. (2013):** Primary reported outcome is non-payoff: group achievement or cooperative success.
- **Cushman (2015):** Cites non-payoff outcomes such as norm compliance, punishment frequency, and cooperation rate.
- **Clavien & Chapuisat (2013):** Focuses on motivational and definitional categories rather than outcomes.

**Distinction:** This literature set largely discusses behavioral and institutional outcomes, with only one paper (Vasconcelos et al., 2013) coming close to addressing a payoff-related group success measure.

# 4) Main Findings Relevant To Prediction

- **Punishment mechanisms, especially when local and at the group level, are theoretically predicted to increase the rate of successful collective action in threshold public goods games compared to no punishment or to global-level punishment (Vasconcelos et al., 2013).** While the primary outcome is group achievement (achieving the public good threshold), this is strongly related to, but does not directly measure, efficiency. The increase in 'group achievement' implies an increase in average group payoffs, especially in all-or-nothing or threshold environments.
- The effectiveness of punishment in Vasconcelos et al. (2013) is **greater for smaller groups** and **when the perceived risk of collective loss is low**, suggesting a stronger positive effect of enabling punishment on efficiency under these conditions.
- **Cushman (2015) provides a mechanism argument** that punishment can foster norm compliance and stabilize cooperation, potentially benefiting efficiency, but also warns that cycles of retaliation (e.g., counterpunishment) can reduce group payoff. No empirical efficiency data is given.
- **Clavien & Chapuisat (2013) caution** that much of the public goods and punishment literature measures cooperation rate or punishment frequency rather than payoff or efficiency, and that findings on behavioral or preference altruism should be clearly distinguished from outcome-based claims.

# 5) Prediction Guidance

From this paper set, the qualitative prediction is that **enabling peer or group-level punishment is likely to increase average efficiency (as measured by group payoff as a proportion of the social optimum) in threshold public goods games, especially with smaller groups and lower perceived risks of collective loss** (Vasconcelos et al., 2013). However, predictions should be tempered because the primary evidence is theoretical and the measured outcomes are proxies (group success, not payoff). The literature also highlights that **contextual factors**—such as institutional design, the possibility of retaliation, and group size—moderate the effect of punishment, and these nuances should be considered in prediction (Cushman, 2015).

This set **does not provide quantitative transfer functions or effect sizes** needed for regression-style predictions. **If the control (no-punishment) game efficiency is already high, the incremental effect of enabling punishment may be small, particularly if institutional risks (like retaliation) are present.**

Predictions should rely on **mechanism-based reasoning**:
- If the game is a threshold PGG (all-or-nothing, group success/failure), adding local/group-level punishment is likely to raise efficiency in the punishment-enabled condition, with the effect stronger for small groups and lower risk environments (Vasconcelos et al., 2013).
- In classic linear PGGs, or environments with high baseline efficiency, the benefit may be less or even negative if punishment leads to cycles of retaliation or inefficient sanctioning (Cushman, 2015).
- Outcomes that look like increased cooperation or compliance may not always translate into increased efficiency (Clavien & Chapuisat, 2013).

# 6) Design Dimensions Highlighted Across Papers

**Directly informed (via theoretical or model-based analysis):**
- `player_count` (group size): Strongly emphasized in Vasconcelos et al. (2013)—smaller groups show more benefit from punishment.
- `all_or_nothing` (threshold): Explicit in Vasconcelos et al. (2013)—outcomes are framed in all-or-nothing threshold terms.
- `mpcr` (marginal per-capita return): Modeled in Vasconcelos et al. (2013), affecting group achievement.
- `punishment_cost` and `punishment_tech`: Modeled in Vasconcelos et al. (2013)—structure and cost of sanctioning institution impact outcomes.

**Indirectly discussed or only contextually covered:**
- `punishment_exists` (enabling punishment): Central to Vasconcelos et al. (2013) and theoretical discussion in Cushman (2015).
- `punishment_tech` (how peers can punish): Explored in a mechanism sense by both Vasconcelos et al. (2013) and Cushman (2015).
- Institutional context (group-level vs. global): Discussed by Vasconcelos et al. (2013) and Cushman (2015).

**Effectively missing or only backgrounded:**
- `num_rounds`
- `chat`
- `default_contrib`
- `reward_exists`, `reward_cost`, `reward_tech`
- `show_n_rounds`
- `show_other_summaries`
- `show_punishment_id`

These design dimensions are not empirically or theoretically examined in the current set and thus present significant gaps for prediction.

# 7) Important Limitations

- **Lack of direct empirical and quantitative effect data:** All three papers are theory-focused; none report new data on efficiency or group payoff in punishment-enabled vs. control games. Predictions must rely on mechanistic analogy, not empirical estimations.
- **Outcome measures in most papers are non-payoff behavioral outcomes:** Only one paper (Vasconcelos et al., 2013) addresses an efficiency-adjacent outcome (group achievement), not efficiency per se.
- **Partial coverage of game design dimensions:** Only a subset of the 14 relevant dimensions are discussed; most are missing or only touched upon as generic context.
- **Applicability limited to threshold (all-or-nothing) PGGs:** The main explicit model is for all-or-nothing threshold games, not general continuous-contribution PGGs. Extrapolation to classic linear PGGs is not well supported.
- **Ambiguity in direction and size of efficiency effect:** Can depend on group size, risk, institutional details, and the risk of inefficient or retaliatory punishment. No consensus or estimate for effect direction in the broader range of designs.
- **Definition and measurement warnings:** Papers stress that measures such as contribution or cooperation rates, while useful, are distinct from efficiency or total payoff outcomes, and prediction must not conflate these (Clavien & Chapuisat, 2013).
- **No direct guidance for reward, heterogeneity, round structure, or information display:** These are important for prediction in broader environments but omitted here.

**Conclusion:** This theory-heavy, empirically-thin literature set provides qualitative mechanism reasoning that can inform directional prediction for certain threshold PGG settings, but is insufficient for calibrated or comprehensive prediction of the efficiency impact of enabling peer punishment across the full range of public-goods-game-like environments.
