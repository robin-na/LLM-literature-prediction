# 1) Evidence Base

The paper set consists exclusively of theoretical works (no empirical or experimental studies). Three papers provide mathematical or evolutionary modeling of collective action dilemmas, focusing on public goods games (PGG) or closely related scenarios; one is a conceptual review critiquing the theoretical assumptions in the field. The set is narrow in that it is dominated by formal theory rather than direct experimental or field evidence relevant for the prediction task. Most models deal with institutional or structural punishments, with limited direct discussion of peer punishment as implemented in experimental PGG variants. Overall, the literature represented provides conceptual and theoretical insight, with some models offering direct implications for efficiency and game design variables in PGG or adjacent games.

# 2) Task Relevance

- **`pgg_or_variant`:**
    - **exact**: One paper (Ishikawa & Fontanari, 2025) directly models a public goods game.
    - **adjacent/close**: Two (Kurokawa, 2022; Peña et al., 2024) cover repeated Prisoner's Dilemma with walk-away or the Shirker’s Dilemma/volunteer’s dilemma—adjacent but not identical to PGG, often lacking multi-player peer punishment or the exact payoffs.
    - **adjacent**: One (Hernández, 2021) is a theoretical review with mention of PGG, but does not directly model or measure such environments.

- **`punishment_or_sanctions`:**
    - **exact**: Only the Ishikawa & Fontanari (2025) paper analytically models punishment, but it is institutional rather than peer punishment (i.e., a centralized enforcement mechanism, not direct peer-to-peer sanctions).
    - **adjacent**: Kurokawa (2022) and Peña et al. (2024) do not model punishment directly but address mechanisms (partner switching/walk-away, group composition effects) functionally similar to sanctions; not explicit punishment.
    - **adjacent**: Hernández (2021) reviews the conceptual role of punishment in the evolution of cooperation but does not analyze payoff outcomes or the effect of sanctions in game-theoretic models.

- **`efficiency_or_related_payoff_outcome`:**
    - **exact/close**: Three of the four papers provide quantitative or theoretical results about efficiency or closely related group payoff outcomes.
    - **adjacent**: The conceptual review (Hernández, 2021) remains adjacent, discussing payoff consequences but not providing analyzable data or functional models.

Thus, only one paper provides **exact** triple relevance to the core prediction task, while the others offer varying degrees of adjacent or contextual relevance, usually lacking direct modeling of both peer punishment and PGG-specific settings.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes:**
    - **Efficiency, group payoff, expected welfare:** Directly modeled by Ishikawa & Fontanari (2025), Peña et al. (2024), and Kurokawa (2022), either as primary outcomes or as the focus of equilibrium analysis.
    - **Explicit predictions regarding total earnings, surplus, or collective welfare** are limited to theory; no experimental measurements are present.

- **Non-Payoff Behavioral Outcomes:**
    - **Contribution rates, cooperation rates, punishment behaviors:** Not directly measured; the focus of the three modeling papers is on how game structure influences equilibrium efficiency or frequencies of cooperation, not on behavioral trajectories or punishment frequencies.
    - Behavioral mechanisms such as walk-away (Kurokawa, 2022) are discussed as enforcement methods but without separating behavioral outcomes from payoffs.

The literature thus mostly measures or discusses **group-level payoff metrics** as modeled outcomes, not empirical behavioral measures.

# 4) Main Findings Relevant To Prediction

**Synthesis Across Papers:**

- **Institutional Punishment & Efficiency:** Institutional punishment (punishments administered by an institution rather than peers) can stabilize high-efficiency equilibria in PGGs, but only when punishment is not excessively costly for the enforcer and when punishers are sufficiently numerous (Ishikawa & Fontanari, 2025). Cost sharing among punishers and a favorable ratio of fines to costs increase the likelihood and stability of efficiency gains. However, if costs are high or too few punishers are present, the system remains at low efficiency (all-defectors). The effects are sharply sensitive to parameter values; the model does not include peer punishment, communication, or rewards.

- **Baseline Effects of Group Size:** In closely related threshold games (shirker’s dilemma), increasing group size tends to **decrease efficiency** at equilibrium, even if more people volunteer on average (Peña et al., 2024). The likelihood of reaching a cooperative equilibrium also falls with larger group size, due to shrinking basins of attraction for such equilibria. These are baseline results for no-punishment setups and do not include peer or institutional punishment.

- **Sanctions through Partner Switching (Walk-Away):** Mechanisms enabling players to break social ties with defectors (a functional analog to sanctioning) promote higher cooperation and efficiency under favorable conditions (Kurokawa, 2022). However, such “sanctions” are structurally different from the peer punishment typically implemented in PGG laboratory games.

- **Rewards and Communication:** No paper in the set directly analyzes the role of rewards, peer punishment technology or interface, or communication dimensions (e.g., chat, summary information, visibility), nor do they address how these features may moderate the effect of enabling punishment on efficiency.

**Empirical vs. Theoretical:**
- All results are based on **theoretical modeling** or conceptual synthesis. No new empirical data or experimental results are reported.

# 5) Prediction Guidance

- **When is Efficiency Increased by Adding Punishment?**
    - **Institutional punishment** (as opposed to peer punishment) can dramatically increase efficiency, but only when the cost of punishers is low compared to the fines/decrements imposed on defectors, and when enough players are willing to pay for punishment up front (Ishikawa & Fontanari, 2025). Thus, knowing the control efficiency alone is insufficient for prediction without also knowing the punishment cost, group size, and enforcement mechanism details.
    - The specific prediction for peer punishment (where each individual can punish another at a personal cost) is not directly modeled and thus requires caution in extrapolation.

- **Effect of Control (No-Punishment) Efficiency:**
    - High baseline efficiency (in the control) may leave little room for improvement via added punishment (Peña et al., 2024), while low baseline efficiency can present an opportunity for substantial gains—if the punishment dynamics and initial conditions are favorable for coordinating on all-cooperator equilibria (Ishikawa & Fontanari, 2025).

- **Group Size and Structure:**
    - Larger groups generally present more difficulty for achieving high efficiency, both with and without punishment, and threshold parameters (costs, number of punishers required for institution) become more critical as group size increases (Peña et al., 2024; Ishikawa & Fontanari, 2025).

- **Indirect Relevance of Alternative Enforcement Mechanisms:**
    - Walk-away and partner switching mechanisms (Kurokawa, 2022) can also induce efficiency gains under favorable parameterizations, suggesting that sanctions need not be limited to direct punishment to achieve efficiency. However, outcomes should not be projected directly from walk-away models to punishment-enabled PGGs.

- **Predictive Cautions:**
    - None of the models directly combine all of the design features used in prediction (e.g., peer punishment, chat, rewards, explicit visibility or feedback), so extrapolation is limited.

# 6) Design Dimensions Highlighted Across Papers

- **Directly Informed:**
    - **player_count:** All three theoretical models incorporate group size and discuss its effect on efficiency.
    - **mpcr (cost-to-benefit ratio):** Explicitly analyzed in all models as a central determinant of sustainability of cooperation and efficiency.
    - **all_or_nothing:** Binary versus continuous contributions are modeled in at least two papers.
    - **punishment_cost, punishment_tech (institutional):** Only Ishikawa & Fontanari (2025) explicitly models punishment cost and the technological (institutional) implementation of punishment.

- **Indirectly Informed:**
    - **num_rounds, show_n_rounds, show_other_summaries:** Kurokawa (2022) models repeated interactions (number of rounds/group stability), and the effects of information, but only in the context of the repeated Prisoner’s Dilemma.
    - **default_contrib:** Not directly included, but framing or defaults could arguably influence initial conditions, which are important in models where equilibria depend on starting states.
    - **reward_exists, reward_cost, reward_tech:** Not addressed at all in modeling.
    - **show_punishment_id:** Not discussed.

- **Only Contextual/Missing:**
    - **chat (communication):** Absent from modeling and theory.
    - **peer punishment (as opposed to institutional):** Not directly modeled; most evidence is for institutional punishment or analogs.
    - **reward-related dimensions:** Not covered in the set.

# 7) Important Limitations

- **No Peer Punishment:** None of the papers model or empirically analyze the type of **peer punishment** (person-to-person costly sanctions) commonly used in laboratory PGGs. Predictions about enabling peer punishment must therefore be made cautiously, drawing on models of institutional punishment or adjacent mechanisms.

- **Theoretical/No Empirical Validation:** All results are **theoretical**; there is no direct empirical or field evidence in the set. Claims about real-world efficiency or predictability are therefore bounded by modeling assumptions and parameterizations.

- **Sparse Coverage of Design Space:** The full range of 14 design dimensions is covered incompletely. Only group size, contribution type, cost/benefit ratio, and punishment cost/structure are addressed directly. Crucial factors including communication (`chat`), peer punishment technology, reward mechanisms, and visibility of actions are not analyzed.

- **Ambiguity and Sensitivity to Parameters:** The models exhibit sharp **parameter sensitivity**—small changes in punishment cost or initial conditions can greatly alter the outcome (Ishikawa & Fontanari, 2025). There is also persistent ambiguity about which equilibrium will be selected in finite or mixed populations.

- **No Explicit Control-to-Treatment Mapping:** There is no direct mapping or formula for predicting the **treatment efficiency** from **control efficiency** plus design parameters, due to a lack of models tracking both states across treatments.

- **Conceptual Paper Lacks Actionable Evidence:** The conceptual critique by Hernández (2021) is broad and theoretical, offering context but not dimensions or quantitative results for prediction.

In summary, the literature set is strong on theoretical insight into how fundamental game parameters affect efficiency—under specific institutional or collective action models—but is limited for quantitative downstream prediction in peer-punishment-enabled PGGs with varied experimental design features.
