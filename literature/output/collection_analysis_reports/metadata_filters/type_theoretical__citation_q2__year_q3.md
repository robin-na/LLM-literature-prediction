# 1) Evidence Base

The paper set consists of 108 theory-focused works, nearly all being formal models or simulations, rather than empirical or laboratory/field experiments. The coverage of standard Public Goods Games (PGG) and direct variants is strong for theory and simulation, but the set contains little experimental data on observed efficiency outcomes. Most papers analyze deterministic or evolutionary models—varying game design parameters or introducing mechanisms such as punishment/reward, exclusion, centralized enforcement, or reputation. Many focus specifically on payoff-related outcomes (e.g., group payoff, efficiency, welfare), but a substantial portion only considers behavioral outcomes (e.g., cooperation rates, fractions of cooperators, or strategy distributions).

Crucially for the downstream prediction task (estimating efficiency under punishment from design + control efficiency), the evidence is skewed toward conditional/theoretical predictions across various parameter ranges, rather than empirical estimates or point predictions for common experimental designs.

# 2) Task Relevance

### a. **pgg_or_variant**
- **Relevance:** Nearly all highlighted papers are directly about the standard public goods game (PGG) or very close variants (e.g., linear or threshold PGG, spatial/networked PGGs, repeated n-person social dilemmas).
- **Label:** *exact* for the central cluster, though many move toward *close* (e.g., donation, snowdrift, or common-pool resource variants). Some adjacent works discuss indirect reciprocity, trust, or division-of-labor games.
- **Coverage:** Strong for theory, models, and computational simulation of core PGG dynamics.

### b. **punishment_or_sanctions**
- **Relevance:** Many papers focus explicitly on *punishment* or *sanctioning* mechanisms, including peer punishment, social exclusion, centralized/institutional punishment, and combinations with reward or reputation systems.
- **Label:** *exact* for standard punishment mechanisms, but coverage becomes *adjacent* or *weak* for systems relying solely on exclusion, costly precommitment, or reputation-based sanctions (without explicit punishment actions).
- **Coverage:** Good for a variety of punishment mechanisms (peer, leader-driven, institutional, endogenous), with some attention to the possibility of both pro-social and anti-social punishment, extortion/misuse, and cross-group enforcement.

### c. **efficiency_or_related_payoff_outcome**
- **Relevance:** A subset of papers report group efficiency, mean payoff, welfare, or profits as primary outcomes (*exact*, *close*). Many others report only behavioral outcomes like cooperation/contribution rates, which, while correlated, are *not* efficiency and can diverge in their implications due to costs of punishment, antisocial punishment, or norm compliance.
- **Label:** *exact* for a distinct subcluster (especially simulations that define efficiency or payoff ratio explicitly); *adjacent* or *weak* for papers focusing solely on cooperation rates or theoretical mechanisms.
- **Coverage:** Sufficient for qualitative inferences and parameter-sensitivity, but sparse for direct, quantitative predictions or empirical effect sizes.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes:** Some papers directly model or report group *efficiency*, total earnings, group payoff, surplus, welfare, or normalized utility. Examples: Powers (2018); Dutta et al. (2021); Kol'veková et al. (2021); Murase & Baek (2021); (Gámez et al., 2018).
- **Non-Payoff Behavioral Outcomes:** Widespread across the set. Most commonly, cooperation or contribution rates, prevalence of strategies, provision/licensing rates, or dynamics of cluster formation. Many treat these as proxies for efficiency, but several explicitly note their divergence (e.g., high cooperation sometimes yielding low efficiency under costly or antisocial punishment).
- **Combined Outcomes:** Some models report both payoff and behavioral outcomes, illustrating relationships (or lack thereof) between increased cooperation and group efficiency.
- **Indirect or Mechanism-Based Outcomes:** Norm compliance, reputation scores, or frequency of punishment/reward themselves.

# 4) Main Findings Relevant To Prediction

**Synthesis Across High-Relevance Papers:**

- **Enabling punishment generally increases efficiency—when punishment is effective and not too costly.** Numerous theoretical models and simulations find that introducing peer or institutional punishment mechanisms in PGG-like settings raises equilibrium efficiency and group payoff (Dutta et al., 2021; Cui et al., 2019; Wang & Lv, 2019; Kol'veková et al., 2021).
- **The effect is *conditional* on punishment parameters and game context:**
    - *Punishment cost and effectiveness*: If the punishment imposed on defectors is much greater than its cost to the punisher, the efficiency gain is robust. If costs are high or effectiveness is low, efficiency gains can be wiped out or reversed (Hintze et al., 2020; Fang et al., 2020; Sui et al., 2018; Quan et al., 2019).
    - *Antisocial/unequal punishment*: When punishment is used against cooperators or unequally applied, its benefits can vanish or negative welfare effects occur (Acemoglu & Wolitzky, 2021; Schunk & Wagner, 2021; Honjo & Kubo, 2020).
    - *Network and population structure*: Spatial/networked setups often enable punishment/reward mechanisms to stabilize clusters of cooperation and raise efficiency even when well-mixed models predict collapse. But effect sizes and thresholds vary (Wang & Lv, 2019; Cui et al., 2019).
    - *Norms and institutional context*: The distribution and control of punishment (peer vs. centralized, endogenous vs. exogenous, transparent vs. opaque) alters efficiency effects (Powers, 2018; Kol'veková et al., 2021; Barron & Guo, 2021; Brandt & Svendsen, 2019).
- **Punishment effect is non-monotonic:** Too strong or misapplied punishment can lower efficiency (via excessive cost or escalation/conflict); too weak fails to sustain cooperation (Honjo & Kubo, 2020; Barron & Guo, 2021; Ille, 2021).
- **Reward mechanisms and hybrid incentives** can, in some cases, outperform punishment for efficiency or make punishment unnecessary if inclusiveness (redistribution) is sufficient (Hintze et al., 2020; Chen et al., 2019).
- **Baseline efficiency moderates marginal impact:** In games with already high efficiency (high mpcr, strong pro-social norms, or reward), adding punishment may yield smaller or even negative marginal gains.

# 5) Prediction Guidance

- **General rule:** Introducing peer (or institutional) punishment *usually* increases average efficiency in public goods games, *provided* the punishment is effective (large fine per unit cost), not prone to misuse (antisocial punishment/extortion), and situated in a context where every player can both punish and be punished.
    - When the design ensures *low punishment cost* and *high punishment effectiveness*, the expected effect is a substantial efficiency increase (Dutta et al., 2021; Cui et al., 2019; Kol'veková et al., 2021).
    - *Baseline (control) efficiency* is an informative prior: if the control game (no punishment) is highly inefficient, enabling effective punishment typically leads to a sharp rise in efficiency. If the control is already efficient, the marginal benefit may be low or negative (Acemoglu & Wolitzky, 2021; Honjo & Kubo, 2020).
    - *Design dimensions* to emphasize in prediction: punishment cost and tech (effectiveness), player count, group structure, mpcr, and transparency (can punishers/rewarders be identified, is punishment equally available/applied?).
    - *When punishment is costly or ineffectively targeted,* efficiency can decline due to wasted resources or retaliation/counterpunishment (Hintze et al., 2020; Quan et al., 2019).
    - *Presence of reward and payoff redistribution* can interact with punishment and sometimes make it redundant (Hintze et al., 2020; Chen et al., 2019).
- **Ambiguities/disagreement:** Some models and scenarios forecast *neutral* or even *negative* effects on group efficiency from punishment, especially with:
    - Antisocial punishment/unequal sanctioning
    - Highly competitive, low-N, or one-shot games (Honjo & Kubo, 2020)
    - Opportunity for extortion/misuse of punishment (Barron & Guo, 2021)
- **Predictions must treat cooperation rate and efficiency separately:** Papers highlight that high cooperation does *not always* translate to high efficiency—punishment costs can dominate (Hintze et al., 2020; Quan et al., 2019).

# 6) Design Dimensions Highlighted Across Papers

- **Directly Informed Dimensions:** `player_count`, `num_rounds`, `all_or_nothing`, `mpcr`, `punishment_cost`, `punishment_tech` are robustly explored in relation to efficiency effects. Many models directly manipulate these variables and map parameter regions where punishment increases efficiency.
- **Indirectly Informed/Contextual Dimensions:** 
    - `show_punishment_id`, `show_other_summaries`, `chat`: Contextually discussed in relation to social learning, transparency, and norm monitoring, but not always systematically varied.
    - `reward_exists`, `reward_cost`, `reward_tech`: Sometimes explored alongside punishment (for mixed incentive environments or comparison), but less systematically.
    - `default_contrib`: Examined in a few papers as contribution framing or opt-in/opt-out, but typically not a primary focus.
- **Sparsely or Missing Dimensions:** 
    - `show_n_rounds`: Only rarely analyzed as to its impact on strategic planning and learning.
    - `chat`: Occasionally noted as a moderator (enabling coordinated punishment), but empirical links to efficiency are rare.
    - Some papers highlight the importance of institutional context and emergent properties not directly mapped to the 14 dimensions (e.g., endogenous rule choice, leadership structures, corruption/bribery risks), but these are not easily converted to prediction features.

# 7) Important Limitations

- **Empirical/experimental evidence is largely missing:** Quantitative predictions for real-world or laboratory outcomes are based on theory and simulation, not direct observation, raising external validity concerns.
- **Behavioral vs. payoff outcomes often conflated:** Many models use cooperation/contribution rates as proxies for efficiency, but this assumption is explicitly broken in cases where punishment is costly or misapplied.
- **Edge conditions and moderators:** Evidence for the efficiency impact of punishment is robust in well-mixed, n-person, repeated PGGs with standard parameters, but outcomes can diverge sharply in games with strong spatial structure, thresholds, stochastic or networked interactions, strong inequalities in punishment power, or opportunities for bribery/corruption.
- **Potential for misuse or antisocial punishment:** Several papers document scenarios where punishment increases conflict, reduces group welfare, or is used strategically rather than cooperatively.
- **Quantitative mapping is parameter-dependent:** The literature provides phase diagrams, boundaries, and qualitative regime mapping more than point estimates. Extrapolation outside analyzed parameter ranges is especially risky.
- **Sparse treatment of several design dimensions:** Chat, summary displays, and default contribution are rarely investigated as efficiency moderators under punishment.
- **Lack of repeated empirical validation:** Models often claim robustness within simulation, but few have been systematically validated against multiple empirical datasets.

---

**Summary:**  
The literature set provides strong theoretical and computational support for the expectation that peer punishment increases group efficiency in PGG-like games *when* it is effective, not too costly, and not subject to major misuse. The marginal benefit of punishment depends strongly on the cost/benefit ratio, baseline efficiency, group structure, and whether the punishment is applied prosocially and fairly. Game design dimensions most directly informing these predictions are group size, rounds, punishment cost and effectiveness, and benefit structure (mpcr). Several important dimensions remain sparse, and the lack of empirical data and frequent conflation of cooperation rate with efficiency are notable limitations. Ambiguity remains for contexts with antisocial punishment or opportunities for extortion. Thus, for prediction, reliance on the theory evidence should be qualified, especially for out-of-domain or structurally atypical games.
