# 1) Evidence Base

The paper set consists of 23 papers, comprising a mix of empirical (primarily experimental lab studies) and theoretical (mathematical or computational modeling) work. Of these, only a small subset includes direct empirical evidence on payoff-related outcomes in public-goods-game (PGG) or PGG-like environments with and without peer punishment. Most theoretical papers offer relevant conceptual models or simulated results but are often not set in standard linear PGGs. There is also substantial coverage of adjacent game types (e.g., trust games, dictator games, common pool resource games) and psychological or neurobiological mechanisms of punishment, but many do not directly address efficiency as defined for the prediction task.

Overall, the evidence base is **broad in theoretical and contextual scope** but **narrow in direct, parametric evidence** for predicting the quantitative effect of peer punishment on efficiency in well-defined PGGs. Few papers report the efficiency (group payoff relative to the full cooperation optimum) both with and without punishment in a format directly useful for prediction.

# 2) Task Relevance

**Dimension 1: PGG or Variant**
- **exact:** 3 papers (e.g., Espín et al., 2022; Li et al., 2024; Wang et al., 2024) are set in PGGs or very close variants.
- **close:** Around 5-6 additional papers employ close variants (e.g., CPR games, collective risk games).
- **adjacent/weak/none:** The remainder are theoretical, use adjacent game types, or are purely context- or mechanism-focused.

**Dimension 2: Punishment or Sanctions**
- **exact:** About half the papers include explicit peer punishment or sanctions (e.g., Espín et al., 2022; Xu et al., 2022; Grimalda et al., 2022).
- **close:** Theoretical works often model sanctions, exclusion, or penalty mechanisms in close analogs (e.g., Wang et al., 2024; Li et al., 2024).
- **adjacent/none:** Several papers only cover indirect or endogenous punishment (e.g., through exclusion, reputation) or focus solely on reward or coordination games.

**Dimension 3: Efficiency or Payoff-Related Outcome**
- **exact:** Only a few papers (notably, Wang et al., 2024; Yaman et al., 2023; Xu et al., 2022) focus on efficiency/group payoff as a primary outcome.
- **close:** Additional papers measure outcomes like group welfare, resource conservation (in CPR contexts), or related metrics mapped to payoff (e.g., Xu et al., 2022).
- **adjacent/none:** Many papers report only behavioral outcomes (contributions, cooperation rates, punishment frequency), reputational impacts, or psychological/neural responses.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes** (efficiency, group payoff/earnings, welfare, surplus): Directly reported or modeled in only a few papers (notably Wang et al., 2024; Yaman et al., 2023; Murase & Baek, 2023; Xu et al., 2022; Grimalda et al., 2022).
    - Some report actual monetary or resource outcomes (Xu et al., 2022; Grimalda et al., 2022).
    - Some theoretical papers provide efficiency in the context of modeled parameter sweeps (Wang et al., 2024; Yaman et al., 2023).
- **Non-payoff behavioral outcomes:** The most common outcome type, including cooperation/contribution rates, punishment frequency, norm compliance, and neural/psychological measures (e.g., Espín et al., 2022; Li et al., 2022; Xie et al., 2022).
    - Many of these outcomes are relevant to the process by which efficiency arises, but are not proxies or direct measures of group efficiency.

# 4) Main Findings Relevant To Prediction

**Empirical Findings:**
- In close variants of PGGs and CPR games, **enabling punishment (especially monetary fines of sufficient magnitude)** tends to increase cooperation rates and group welfare, but the impact on efficiency can be positive or negative depending on the cost of punishment (Xu et al., 2022; Grimalda et al., 2022).
    - E.g., in Grimalda et al. (2022), sanctions increased cooperation (measured by probability of avoiding losses) but **reduced overall group efficiency** (payoffs were higher without punishment due to the cost of sanctions).
    - Xu et al. (2022) demonstrates that high fines for over-extraction ("punishment") robustly increase welfare by reducing extraction in CPR, closely mapping to efficiency gains in PGGs, especially when fines are substantial.

**Theoretical Findings:**
- Direct, parameterized theoretical models (Wang et al., 2024) show that **punishment can improve efficiency strongly, weakly, or not at all depending on game context**, especially the resource growth rate/benefit structure and strength/cost of sanctions.
    - If the resource pool/gains from cooperation are high, punishment (and/or reward) can stabilize near-full efficiency.
    - Bistability is possible: group could end up at full cooperation (high efficiency) or at defection (low efficiency) depending on initial conditions and parameters.

- Models of decentralized social sanctioning (Yaman et al., 2023) indicate that **punishment/reward structures can drive close-to-optimal efficiency**, especially where role specialization or division of labor is needed.

- Some empirical and theoretical work underscores that **the cost of punishment is a key moderator**: high costs can erase or reverse the efficiency gains brought by increased cooperation (Grimalda et al., 2022; Wang et al., 2024).

**Non-payoff findings:** Many papers identify moderators and mechanisms for punishment (e.g., group composition, gender roles, network position, culture, communication), but these tend to influence behavioral outcomes and are less directly linked to efficiency measures.

# 5) Prediction Guidance

1. **Direct prediction of efficiency gains from punishment is only well-supported in a limited subset of the literature.** When using these papers, prediction should be conditioned on:
    - **The cost and magnitude of punishment:** High punishment costs can negate efficiency gains even if cooperation rates increase (Grimalda et al., 2022; Wang et al., 2024).
    - **Structural features:** Efficiency gains from punishment are more robust when the system benefits from sustained cooperation (high resource growth, high MPCR, or equivalent benefit parameter), and when punishment magnitude is sufficient (Xu et al., 2022; Wang et al., 2024).
    - **Initial efficiency level:** If baseline (control) efficiency is already high, added punishment may produce marginal or even negative returns (Grimalda et al., 2022). If baseline efficiency is low due to weak cooperation, and punishment is affordable and expected, efficiency can increase substantially (Xu et al., 2022; Yaman et al., 2023).

2. **Indirect predictors can be used when only behavioral or theoretical outcomes are available:**
    - High observed cooperation/contribution rates due to punishment can be interpreted as supporting potential efficiency gains, but only if punishment costs do not erase the benefit (Wang et al., 2024; Xu et al., 2022).
    - Contextual moderators (culture, group composition, network structure)—despite being discussed—are not robustly parameterized for prediction and are often only indirectly tested for effects on efficiency (Espín et al., 2022; Li et al., 2022).

3. **Prediction should not rely heavily on papers reporting only behavioral or neural outcomes** with no explicit mapping to group payoff or efficiency.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- `player_count`, `num_rounds`, `all_or_nothing`, `mpcr` or equivalent payoff-benefit parameter: Multiple papers (empirical and theoretical) analyze these.
- `punishment_cost`, `punishment_tech`: Widely modeled as critical moderators—high cost dampens effect, form of punishment (peer, centralized, exclusion) conditions outcomes.
- `reward_exists`: Some models and experiments include both reward and punishment arms, showing that both can increase efficiency under favorable conditions (Wang et al., 2024; Yaman et al., 2023).
- `chat`: Sometimes present in experiments; role as a moderator is noted (e.g., increased cooperation with communication, but rarely linked directly to efficiency plus punishment).

**Indirectly or Sparsely Informed:**
- `default_contrib`: Framing is occasionally manipulated, but not systematically linked to efficiency effects of punishment.
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Generally present for context/experimental control but not systematically studied for their direct moderation of efficiency.
- `reward_cost`, `reward_tech`, `reward_magnitude`: Considered in a handful of theory papers, less so in empirical ones.
- `punishment_magnitude`: Sometimes varied together with punishment cost, but often not separately parameterized.

**Effectively Missing or Weakly Discussed:**
- Detailed findings by game framing, visibility of punishment identity, or granularity of reward/punishment implementation are scarce.
- No consistent cross-paper analysis of `default_contrib`, `show_n_rounds`, `show_other_summaries`, or `show_punishment_id` as direct moderators of the efficiency effect from punishment.

# 7) Important Limitations

- **Sparse direct empirical evidence on efficiency effects:** Few experimental studies report or compare efficiency in PGGs with and without punishment, or systematically vary design dimensions of punishment for payoff effects.
- **Most papers use non-payoff outcomes:** Majority report only behavioral measures (e.g., cooperation rates, punishment assigned, norm compliance), not group earnings or efficiency ratios.
- **Complex interaction of moderators:** Where efficiency data are available, costs of punishment, group composition, and baseline efficiency all interact in ways that are only partly parameterized.
- **Many papers study adjacent or non-PGG designs:** The applicability of findings from trust games, dictator games, or CPR games depends on how structurally similar they are to the target PGG environment.
- **Payoff externalities often ignored:** Antisocial punishment, variation in implementation cost, endogeneity of sanctioning—while noted in some theory and review papers—are rarely connected to efficiency in a way actionable for prediction.
- **Contextual moderators (e.g., culture, gender, network structure) are discussed but rarely quantified for prediction.**
- **Potential for bistability and history effects:** Some theory notes that efficiency improvements with punishment can depend on initial conditions, especially in dynamic resource or tax-punishment models (Wang et al., 2024).
- **Ambiguity in effect direction:** In at least one empirical study (Grimalda et al., 2022), punishment increases cooperation but reduces efficiency—emphasizing the need not to assume automatic efficiency gains from increased cooperation.

---

**In summary:**  
While there is strong theoretical basis and some empirical support for the idea that enabling peer punishment often increases group efficiency in PGG-like environments—especially when punishment is not overly costly and baseline cooperation is low—the literature base leaves important prediction gaps. Many game design dimensions are addressed only indirectly, and few studies report all the needed outcomes (efficiency, parametric variation, PGGs with and without punishment) for confident, calibrated prediction. Caution is advised whenever extrapolating from behavioral outcomes or adjacent game types to predicted efficiency gains in true PGGs.
