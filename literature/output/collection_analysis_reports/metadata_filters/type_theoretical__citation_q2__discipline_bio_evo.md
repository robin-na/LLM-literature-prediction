# 1) Evidence Base

The literature set is exclusively theoretical—there are no empirical or experimental studies present. The scope is relatively narrow for the prediction task, as all 49 sources are theory papers, and most focus on standard or close variants of the public goods game (PGG) or related social dilemmas rather than empirical evaluation of punishment effects on efficiency. Several papers directly analyze efficiency, group payoff, or welfare outcomes in PGGs with punishment, but a substantial portion examine only behavioral outcomes (e.g., cooperation rates, strategy frequencies) or discuss theoretical mechanisms without reporting payoff-based results. Empirical relevance is thus limited to theoretical inference, simulations, or modeled predictions.

# 2) Task Relevance

**pgg_or_variant**:
- Relevance is **exact** for core papers modeling standard multi-player PGGs with design dimensions like player count, rounds, MPCR, and explicit punishment/reward stages. About a third of the papers fall in this category.
- Several others are **close** (e.g., public resource management or repeated donation/PD games), capturing essential features of the PGG but including additional dynamics (taxation, renewable resources, division of labor, reputation systems, etc.).
- Roughly half the papers are **adjacent** or **weak** (covering indirect reciprocity, evolutionary dynamics, group selection, trust games, and other related models), providing mechanism insight or context, but not directly modeling PGG payoff structures.

**punishment_or_sanctions**:
- Relevance is **exact** for about half the literature, where explicit peer or institutional punishment is modeled, and punished players incur costs/deductions.
- Some papers treat **close** mechanisms (e.g., exclusion, tax-funded punishment, indirect punishment via reputation or precommitment costs).
- Others are **adjacent** or **weak**, focusing on reputation damage, exclusion, social sanctioning, or avoidance, but not with explicit costly punishment as in canonical PGG experiments.
- A minority of sources discuss punishment only **contextually**.

**efficiency_or_related_payoff_outcome**:
- About a third provide **exact** relevance by explicitly reporting efficiency, group payoff, welfare, or surplus, aligned with the prediction task.
- Many report only **adjacent** or **weak** outcomes (e.g., cooperation/contribution rates), requiring indirect inference about efficiency.
- A number report **none** or only mention efficiency contextually, focusing instead on mechanisms, frequencies, or evolutionary stability.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes**: The most relevant papers analyze efficiency (group payoff relative to the full-cooperation maximum), total earnings, or welfare either directly (via payoff equations, Nash equilibria, simulation averages) or as a central modeled outcome. Some extend to surplus or sustainability (in dynamic resource contexts).
- **Non-Payoff Behavioral Outcomes**: Many papers primarily report cooperation rates, contribution proportions, evolutionary frequencies of strategies, or success rates of moral/enforcement norms. These are not equivalent to efficiency but may indirectly signal changes in group payoff, especially when moving from all-defection to high-cooperation equilibria.
- **Mechanism Arguments**: Some papers focus on the theoretical stability or emergence of cooperation under punishment but do not quantify efficiency outcomes, and may only refer to payoffs implication contextually.

# 4) Main Findings Relevant To Prediction

**Empirical (i.e., modeled or simulated) findings:**
- **Punishment often increases efficiency** relative to control (no-punishment) games, but only when certain parameter thresholds are met (e.g., sufficient punishment effectiveness / low cost, scarcity of retaliation or antisocial punishment, moderate game length) (Wolff, 2012; Wang & Lv, 2019; Eldakar et al., 2013; Murase & Baek, 2021; Fang et al., 2020; Lee & Iwasa, 2014).
- **Punishment effects are parameter-dependent and can be negative**: If punishment is too costly, easily retaliated, or undermined by corruption/bribery or anti-social punishment, efficiency gains disappear or may even turn negative (Fang et al., 2020; Wolff, 2012; Gao et al., 2015).
- **Punishment magnitude and cost are critical moderators**: Group efficiency improvement from punishment is strongest when punishment is cheap for punishers relative to the magnitude of fines/costs for defectors (Wang & Lv, 2019; Lee & Iwasa, 2014; Voelkl, 2015; Eldakar et al., 2013).
- **Group size and rounds interact with punishment effect**: Smaller player counts and larger numbers of rounds often amplify the effectiveness of punishment in boosting efficiency (Eldakar et al., 2013; Murase & Baek, 2021).
- **Effectiveness is higher for centralized or pool punishment** systems, especially in the presence of anti-social punishment or when free-rider problems at the enforcement stage are salient (Gao et al., 2015; Fang et al., 2020).
- **Population structure, spatial structure, migration and group competition** can amplify the positive effect of punishment (Kaiping et al., 2016; Voelkl, 2015; Vincent, 2007; Li et al., 2024), though concrete efficiency data is less prevalent.
- **Extensions involving reward, exclusion or reputation** as sanctioning alternatives often find similar or even higher efficiency effects if designed correctly (Fang et al., 2020; Wang et al., 2024).
- **Certain design features (e.g., possibility of chat, default contribution framing, information salience)** are rarely manipulated or explicitly linked to efficiency outcomes.

**Mechanism/theory arguments**:
- The efficacy of punishment for efficiency relies on its ability to deter defection without excessive cost. Retaliatory punishment, anti-social punishment, and corruption can undermine this efficacy.
- Commitment to punishment and recognizability of commitment may be critical in real-world and evolutionary contexts (Akdeniz & van Veelen, 2021; Cofnas, 2018), but these effects are not quantified in terms of payoff.

**Disagreements/Ambiguities**:
- Some models find that under high continuation probability, or when mutation/retaliation are frequent, punishment's positive effect on efficiency cannot be sustained (Wolff, 2012).
- The impact of population structuring and group-level selection remains theoretically supportive but quantitatively ambiguous for efficiency gains in PGGs with punishment.

# 5) Prediction Guidance

- **Direct (Payoff/efficiency-based) prediction**: The best-supported quantitative guidance is that enabling peer (or centralized) punishment will increase average efficiency (group payoff) over control when (a) punishment is effective (high deduction per cost), (b) its cost to punishers is moderate or low, (c) there is not widespread anti-social punishment or retaliation, and (d) the environment is not dominated by strong incentives or mechanisms for corruption/bribery or for undermining enforcement (Wolff, 2012; Wang & Lv, 2019; Fang et al., 2020; Lee & Iwasa, 2014; Voelkl, 2015; Yaman et al., 2023).
    - **Magnitude of effect** is not generally reported empirically—most guidance is qualitative or structurally parameterized.
- **Baseline (control) efficiency is a central moderator**: The higher the control efficiency, the smaller the potential effect of enabling punishment, as already-high cooperation leaves little room for improvement (implied across all direct and adjacent models).
- **Game design dimensions to weigh most strongly**:
    - **punishment_cost / punishment_tech**: Lower cost and higher effectiveness predict stronger positive effects of punishment.
    - **player_count, num_rounds, mpcr**: Smaller groups, longer interactions, and higher marginal per-capita return often synergize with punishment’s effect.
    - **all_or_nothing**: Both all-or-nothing and continuous budgets are represented; effects of this framing are less clearly distinguished but may interact with stepwise punishment magnitude.
    - **population structure/networking**: Structured populations or group competition generally enlarge parameter regions for effective punishment, but efficiency outcomes are modeled only indirectly.
    - **corruption/bribery**: Contexts where punishment is subvertible predict lower or negative efficiency effects (Fang et al., 2020; Gao et al., 2015).
- **Indirect dimensions**: Features like chat, information availability, default contribution framing, and the salience of the punishment/reward identity are rarely modeled for payoff outcomes; their effect on efficiency is unknown or only discussed contextually.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed:**
- `player_count`, `num_rounds`, `all_or_nothing`, `mpcr`, `punishment_cost`, `punishment_tech`—these are handled explicitly in model analysis and are the strongest quantitative moderators of predicted efficiency effect.
- `reward_exists` and `reward_cost` are analyzed in some models (e.g., Wang et al., 2024; Voelkl, 2015), especially as alternatives or complements to punishment.

**Indirectly informed:**
- `punishment_magnitude` (implied in models where punishment effectiveness is parameterized, though not always distinguished from cost).
- `show_n_rounds`, `show_other_summaries`—occasionally discussed in models with repeated rounds, reputation, or observability, but with only adjacent links to efficiency.

**Only contextually discussed:**
- `chat`, `default_contrib`, `reward_tech`, `show_punishment_id`—the impact of these features on efficiency is speculative or only briefly mentioned, not tested or parameterized.

**Effectively missing:**
- No papers explicitly provide data or parameter sweeps on `chat`, `default_contrib`, `show_punishment_id`, or contribution framing as moderators of efficiency under punishment.
- `reward_tech` (granularity or scaling of reward) and its detailed interaction with punishment are rare.
- The formats and visibility of information (beyond presence or absence, e.g., exact summary formats, chat content) are not modeled with respect to efficiency.

# 7) Important Limitations

- **No empirical (experimental/data-driven) effect sizes or real-world calibration**: All evidence is theoretical, usually analytic or based on simulation—no studies present observable, experimental efficiency differentials when punishment is enabled versus disabled.
- **Sparse variation on some design dimensions**: Several game features (chat, contribution framing, information structure, identity/salience of punishers/rewarders) commonly manipulated in experimental PGGs are not modeled or only discussed theoretically, limiting design-level generalization.
- **Indirect inference for many moderators**: Many mechanism papers focus on cooperation rates or frequencies, not direct payoff/efficiency outcomes—the mapping to group efficiency is plausible (more cooperation usually means higher payoff), but this is not always linear or guaranteed, and exceptions are acknowledged in some models (Wolff, 2012; Fishman, 2006).
- **Heterogeneity of enforcement/punishment models**: Ranges from peer to centralized (pool) punishment, from direct deduction to exclusion or reputation loss, and from static to dynamic/structured populations—findings may not transfer uniformly across all PGG implementations.
- **Sensitivity to model assumptions**: Presence of retaliation, bribery, mutation, anti-social punishment, or errors in punishment/reward implementation can sharply reverse or neutralize efficiency effects (Fang et al., 2020; Gao et al., 2015).
- **Quantitative lack of external validity**: While models are internally consistent, there is no empirical check on parameter values, prevalence of phenomena like corruption/retaliation, or real-world game dynamics, so predictions may over- or underestimate actual efficiency effects.
- **Ambiguity and disagreement**: Some models find neutral or even negative effects of punishment in certain parameter regimes (Wolff, 2012; Fishman, 2006), underscoring the lack of a universal positive effect.

---

**In summary:**  
The theoretical literature directly supports the prediction that, for most (but not all) parameter regimes, enabling peer or centralized punishment in public-goods-game-like environments will increase average efficiency compared to control, provided punishment is sufficiently effective, costs are not prohibitive, and enforcement is robust to retaliation and corruption. The most robust design-level evidence supports prioritizing group size, number of rounds, MPCR, and punishment cost/effectiveness as moderators. Many secondary PGG game features and behavioral outcomes are not directly linked to payoff, and the absence of empirical calibration is a key limitation for practical prediction tasks.
