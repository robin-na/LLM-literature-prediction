# 1) Evidence Base

The paper set consists predominantly of theoretical papers, with a smaller number of empirical laboratory or observational studies. Theory papers use evolutionary game theory, agent-based modeling, and analytic methods to characterize the effects of punishment and reward on cooperation and efficiency in environments related to public goods games (PGGs). A minority utilize lab, field, or ethnographic methods. Most models are multi-player, often with explicit group size and parameterized incentive schemes; empirical work includes both human and artificial agent studies, though several are adjacent to PGGs rather than exact implementations. In sum, the evidence base is moderately broad in coverage of social dilemma environments but is relatively narrow with respect to direct, controlled tests of the impact of peer punishment on **efficiency** in canonical PGGs. There are strong contributions for theory and mechanism, with only a handful of empirical studies directly measuring payoff-based efficiency outcomes.

# 2) Task Relevance

Task relevance is assessed along three axes—PGG or variant, punishment or sanctions, and efficiency or related payoff outcomes—using the prescribed coding:

- **pgg_or_variant:**
  - `exact`: Several key theory papers model exact PGGs or multiplayer public goods with or without additional strategic structure (e.g., Ohdaira, 2022; Wang et al., 2024; Liu et al., 2022, 2022).
  - `close` or `adjacent`: Many other papers use adjacent multiplayer social dilemmas (e.g., commitment games, or PD with group context—Han, 2022, 2024; Köster et al., 2022; Pal & Hilbe, 2022), or hybrid PGGs/trust/dictator games (Makovi et al., 2023; Spadaro et al., 2023).
  - `none`: A few have no PGG structure (e.g., Wang et al., 2023).

- **punishment_or_sanctions:**
  - `exact`: Several works manipulate or theorize peer punishment or related sanctions (Ohdaira, 2022; Wang et al., 2024; Han, 2022, 2024; Köster et al., 2022).
  - `adjacent`/`weak`: Some study exclusion, reward, or non-costly sanctions (Liu et al., 2022, 2022; Pal & Hilbe, 2022).
  - `none`: A subset lack any sanctioning institution (Otten et al., 2022; Wang et al., 2023).

- **efficiency_or_related_payoff_outcome:**
  - `exact`: A limited number of theory/agent-based studies explicitly analyze efficiency, group payoff, or welfare (Ohdaira, 2022; Wang et al., 2024; Han, 2022, 2024; Köster et al., 2022; Pal & Hilbe, 2022).
  - `adjacent`: Many report on cooperation rates, norm compliance, or trust, not efficiency (Liu et al., 2022, 2022; Makovi et al., 2023; Spadaro et al., 2023; Roy et al., 2023; Dimant & Gesche, 2023).
  - `none`: Some measure only non-payoff behavior (Otten et al., 2022; Singh & Garfield, 2022).

In summary: the most **direct** and relevant evidence for predicting the efficiency effect of enabling peer punishment in PGGs comes from a small number of theoretical works. Empirical validation is notably sparse for group-level efficiency.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (direct relevance):**
  - *Efficiency, group payoff, welfare, surplus, total earnings*: Explicitly analyzed in Ohdaira (2022), Wang et al. (2024), Köster et al. (2022), Pal & Hilbe (2022, for rewards), Han (2022, 2024).
    - Example: Wang et al. (2024) supply analytic formulas for mean payoff and show efficiency changes.
    - Example: Ohdaira (2022) evaluates average group payoff under variants of pool and peer punishment.

- **Non-payoff (behavioral) outcomes (adjacent/weak):**
  - *Cooperation/contribution rates, norm compliance, exclusion frequency, trust, punishment frequency*: Frequently reported.
    - Liu et al. (2022, 2022) emphasize cooperation rates and composition cycles.
    - Spadaro et al. (2023), Makovi et al. (2023), Dimant & Gesche (2023) focus on trust, perceptions, and punishment decisions.
    - Otten et al. (2022), Wang et al. (2023), Singh & Garfield (2022) report on contribution dynamics or institutional norms, not payoffs.

*Important note*: In many cases, increased cooperation or compliance **does not** equate to higher group efficiency given the cost of punishment—this distinction is underscored in several theory papers (Han et al., 2024).

# 4) Main Findings Relevant To Prediction

- **Punishment generally increases efficiency in structured PGGs—conditioned on sufficient punishment strength.** Theory papers (Ohdaira, 2022; Wang et al., 2024) indicate that, in structured populations or networks, enabling peer or pool punishment can lead to the (near-)elimination of defection, with mean payoffs and efficiency converging to those of the fully cooperative optimum—if the punishment fine exceeds a calculable threshold and the cost is not excessively high.

- **Mechanism design moderates efficiency effects.** For adaptive, probabilistic punishment mechanisms sensitive to actual payoffs or norm violations, efficiency gains can be larger and more robust (Ohdaira, 2022; Köster et al., 2022). Fixed, indiscriminate, or excessively costly punishment mechanisms can undermine or fail to improve efficiency.

- **Reward often outperforms punishment for efficiency.** Several modeling studies (Han, 2022; Han et al., 2024; Pal & Hilbe, 2022) show that, even when both punishment and reward increase cooperation, reward mechanisms typically produce higher group payoff/efficiency, as punishment imposes deadweight losses.

- **Punishment can increase cooperation without raising efficiency.** Han et al. (2024) demonstrate that peer punishment, though it suppresses defection, can reduce overall social welfare (efficiency) due to its cost, and that only appropriately moderate, cost-effective punishment yields any efficiency improvement. (This is a crucial caveat: more punishment is not always better for efficiency.)

- **Empirical and simulated agent-based evidence supports theory but is less comprehensive.** Köster et al. (2022), using artificial agents, show that enabling punishment (even for arbitrary rules) increases group efficiency during collective learning, but transfer to real-human PGGs with immediate feedback may be limited.

- **Non-payoff outcomes underscore context-sensitivity.** Many studies find that the effectiveness and targeting of punishment (and its effect on cooperation or trust) depend on information structure, salience of norms, cost-benefit parameters, timing, and group composition, but these do not directly translate into group efficiency without payoff analysis.

# 5) Prediction Guidance

**For a PGG-like environment, when predicting average efficiency after enabling peer punishment (relative to observed control efficiency as well as game design dimensions):**

- **Expect an efficiency increase** from enabling peer punishment, provided:
  - The punishment is not too costly (“punishment_cost” low relative to its impact).
  - Punishment can be effectively targeted (punishment_tech not overly noisy or capped).
  - The environment allows sufficient rounds and/or social structure for punishment to influence behavior.

- **Efficiency increase is not guaranteed**:
  - If the marginal cost of punishment is high relative to the marginal per-capita return (MPCR), net efficiency gains may be erased by punishment costs, even if cooperation rises (Han et al., 2024).
  - If the punishment regime is fixed, indiscriminate, or unrealistically strong, it may lead to sanctioning cycles or inefficiency (Wang et al., 2024).

- **Key prediction moderators** (with supporting citations):
  - **mpcr**: Higher MPCR makes cooperation and thus efficiency gains from punishment more likely (Wang et al., 2024).
  - **punishment_cost**: Lower costs are better for net payoff, ceteris paribus (Han, 2022).
  - **structure (player_count, regular graph, etc.)**: Structured populations support punishment-driven efficiency gains more than well-mixed populations (Wang et al., 2024).
  - **punishment_tech**: Adaptive/probabilistic (as opposed to deterministic, always-on) punishment mechanisms improve payoffs (Ohdaira, 2022).
  - **num_rounds**: More rounds amplify the efficiency effect of punishment by allowing time for learning and norm establishment (Ohdaira, 2022; Liu et al., 2022).
  - **control efficiency**: The *lift* due to punishment depends on baseline efficiency; if baseline is already near ceiling, incremental gains are small.
  - **reward_exists**: Games with both punishment and reward, or with only rewards, may achieve even higher efficiency (Han et al., 2022; Pal & Hilbe, 2022).
  - **chat, show_other_summaries, show_punishment_id**: Information and reputation structures can amplify or dampen efficiency effects, but direct evidence is sparse.

- **Design features not strongly covered**: Chat, all_or_nothing, default_contrib, reward_cost/reward_tech specifics (except for reward as a comparison condition), and player observation of round count are generally under-explored.

# 6) Design Dimensions Highlighted Across Papers

- **Directly informed (matched in models/analyses and tested for effect):**
  - `player_count`, `num_rounds`, `mpcr`, `punishment_cost`, `punishment_tech` (Ohdaira, 2022; Wang et al., 2024; Han, 2022, 2024).
  - `all_or_nothing` and continuous: Some studies include both binary and continuous contributions (Pal & Hilbe, 2022).
  - `reward_exists`, `reward_cost`, `reward_tech` for comparison (Pal & Hilbe, 2022; Han, 2022, 2024).

- **Indirectly informed (parameter in passing, mechanism, or as context):**
  - `show_punishment_id` and `show_other_summaries` (Köster et al., 2022: agent-based; also appearing in analyses of norm learning dynamics).
  - `chat` (Makovi et al., 2023; Spadaro et al., 2023, but not with efficiency outcomes).

- **Contextually discussed or covered only in adjacent designs:**
  - `default_contrib` (Han, 2022: commitment/opt-in framing).
  - `reward_cost`, `reward_tech` (frequently modeled for reward vs. punishment contrast, but less so in purely punishment-enabled designs).
  - Information disclosure elements (`show_n_rounds`, `show_punishment_id`) affect norm formation and compliance (adjacent studies), but rarely linked directly to efficiency.

- **Effectively missing:** Dimensions like `chat` (as a direct efficiency moderator), `all_or_nothing` (except in reward models), and the fine granularity of information presentation are not empirically or theoretically varied in direct efficiency analyses.

# 7) Important Limitations

- **Sparse empirical evidence for actual efficiency effects in human PGGs.** Most direct statements about efficiency derive from theory or simulation, with empirical confirmation (especially for varied parameterizations or real-world social settings) limited.

- **Transferability to all prediction contexts may be limited.** Many studies use specific population structures (e.g., regular graphs, artificial agents), payoff schemes, or social environments (kin-based societies, agent learning), limiting the generalizability of formulas or directional effects.

- **Behavioral/structural moderators not systematically tested.** There is a lack of multifactorial experimental work examining how multiple game design dimensions interact to moderate the net efficiency effect of punishment.

- **Reward mechanisms often outperform punishment for efficiency, but most models do not test both together, nor with all prediction dimensions.** Insights from reward-focused or mixed-incentive environments must be applied to pure-punishment treatments with care.

- **Critical thresholds for efficiency improvement are context-dependent and model-specific.** The formulas for when punishment will increase group efficiency are generally not plug-and-play for new designs; careful parameter mapping is needed.

- **Most adjacent/empirical studies focus on behavioral rather than payoff outcomes** (e.g., trust, norm compliance, exclusion frequency), limiting their use in predicting efficiency as defined in efficiency ratio terms.

- **Under-exploration of several design dimensions.** Little direct evidence is available for several predictor dimensions in the downstream prediction task, especially information-related features and chat.

---

**Summary:**  
The current literature set provides strong theoretical, but only moderate empirical, support for predicting that enabling peer punishment increases efficiency in PGGs, mostly conditional on punishment being sufficiently effective and not excessively costly. The effect is robust in structured populations and under adaptive punishment regimes, but can fail or become negative if costs are high or if punishment is poorly targeted. Theories highlight the potential for reward mechanisms to achieve greater efficiency gains. For many design dimensions relevant to prediction, evidence is either indirect or lacking. Care should be taken not to overgeneralize from cooperation or contribution rate findings to efficiency, as these outcomes can diverge with costly punishment. Prediction of efficiency outcomes from game design plus baseline efficiency should draw primarily from the core theory papers, treating behavioral-only findings as contextual or suggestive moderators.
