# 1) Evidence Base

The paper set comprises **258 papers** with a broad mix of empirical experiments, theory, simulation, and a few observational datasets. It includes a large number of direct experimental lab studies and an even greater number of theoretical and simulation-based models on public goods games (PGG), their close variants, and other social dilemma contexts.

- **Empirical base**: Multiple high-quality lab experiments and field experiments on PGGs (e.g., Bahbouhi et al., 2024; Pi et al., 2022; Cobo-Reyes et al., 2022; Wang & Huang, 2022; Pancotto et al., 2023; Lec et al., 2023), sometimes with efficiency or group payoff as direct outcomes.
- **Theoretical/simulation studies**: Dominant in quantity. Many provide explicit efficiency- or payoff-based results for variants of PGGs with various punishment and reward mechanisms, covering a broad parameter space (e.g., Sun et al., 2025; Li et al., 2022; Cui et al., 2022; Wang et al., 2025; Gao et al., 2023).
- **Coverage**: The set is broad for the general construct of social dilemmas and interventions (reward, exclusion, institutional/peer punishment), but relatively narrow for **exact lab PGGs** with all 14 prediction dimensions experimentally varied and both control and treatment efficiency measured.
- **Payoff/efficiency reporting**: Exact efficiency measures (i.e., group payoff relative to the full-cooperation optimum) are included in a moderate number of both empirical and theoretical papers; the majority of studies focus on cooperation rates, norm compliance, or behavioral measures instead.

In sum, the set is **sufficiently rich** in both empirical and theoretical evidence to support robust qualitative and some quantitative prediction guidance for the effect of enabling punishment on efficiency in PGG-like environments. However, some design dimensions and context combinations (e.g., chat, opt-in/opt-out framing, visibility of punishment) are less systematically covered.

# 2) Task Relevance

**Target-relevance assessment (pgg_or_variant | punishment_or_sanctions | efficiency_or_related_payoff_outcome):**

- **pgg_or_variant**
    - The vast majority of papers are `exact` or `close` for PGG or its direct variants, including threshold games, voluntary PGG (with loners), and collective-risk dilemmas.
    - Many theory/simulation works and several lab experiments address classic linear PGGs (e.g., Bahbouhi et al., 2024; Pi et al., 2022; Li et al., 2022).
    - A substantial number are `adjacent`, modeling social dilemmas (e.g., Prisoner’s Dilemma, donation game) where the mechanisms translate to PGG settings with some care.

- **punishment_or_sanctions**
    - Punishment or sanctioning is manipulated, modeled, or empirically measured in a large set (`exact`), including both peer and institutional punishment; some papers treat exclusion, reward, or hybrid mechanisms.
    - Some papers focus on adjacent mechanisms (partner choice, reputation exclusion) or only discuss punishment conceptually (`adjacent`).

- **efficiency_or_related_payoff_outcome**
    - A **substantial subset** of papers report efficiency, group payoff, or related welfare outcomes (`exact` or `close`), often as normalized ratios or group earnings.
    - However, many papers report only **non-payoff behavioral outcomes** (e.g., cooperation rate, norm compliance, frequency of punishment) and discuss efficiency only indirectly (`adjacent` or `weak`).

**Summary:** For the **core prediction task**—predicting treatment (punishment-enabled) efficiency from design features and control (no-punishment) efficiency—the literature is largely `exact` or `close` on structure and mechanisms, and reasonably strong on efficiency/related outcomes, with some gaps.

# 3) Outcomes Measured In The Literature

- **Payoff-based outcomes (directly relevant):**
    - Efficiency (group payoff as a fraction of the cooperative optimum), total earnings, net profit, group welfare, surplus, total coins/resources, and resource sustainability are frequently measured in both empirical and theoretical works (e.g., Bahbouhi et al., 2024; Pi et al., 2022; Sun et al., 2025; Wang & Huang, 2022; Wang et al., 2025).
    - Some studies use group achievement rate (reaching a collective target), which closely tracks efficiency in threshold dilemmas (`close` relevance).
    - Many theoretical papers provide **explicit formulas or phase diagrams** linking design parameters to equilibrium group payoff/efficiency.

- **Behavioral outcomes (not efficiency, but sometimes correlated):**
    - Contribution rate, cooperation rate, frequency of punishment or antisocial punishment, norm compliance, proportion of cooperators, and social welfare proxies (e.g., public good provision) are **much more common** in both experiment and simulation.
    - While these are sometimes positively correlated with efficiency, they are not the outcome to be predicted for this task.

- **Mixture and ambiguous cases:**
    - Several empirical studies and most simulation/theory papers report both types, but many focus only on behavior, referencing efficiency only in discussion or via implicit mapping.

# 4) Main Findings Relevant To Prediction

**Synthesis of cross-paper findings for predicting the effect of enabling punishment on efficiency in PGG(-like) environments:**

## General Patterns

- **Enabling punishment (especially peer or institutional) usually increases efficiency** relative to control, **if**:
    - Punishment is not prohibitively costly to assigners or the group (Bahbouhi et al., 2024; Pi et al., 2022; Sun et al., 2025; Wang & Huang, 2022; Sun et al., 2025; Liu et al., 2024).
    - The punishment technology and network structure avoid excessive or inefficient punishment (Pi et al., 2022; Bahbouhi et al., 2024; Cui et al., 2022; Gao et al., 2023).
    - Control efficiency is low due to free riding.

- **Efficiency gains from punishment are not universal:** Under some design conditions, **punishment can reduce efficiency**:
    - If punishment is excessively costly or over-applied (Calabuig et al., 2024; Zhang & Pei, 2022; Herne et al., 2022).
    - If antisocial punishment is prevalent (Pi et al., 2022; Bahbouhi et al., 2024), or coordination on normatively appropriate punishment is absent (Macleod et al., 2025).
    - In games with very high baseline cooperation, added punishment can sometimes crowd out efficiency benefits (Ishikawa & Fontanari, 2025; Gao et al., 2023).

- **The effect size of enabling punishment on efficiency is strongly **moderated** by:
    - **Game structure:** e.g., classic linear PGG, threshold/collective-risk PGG, snowdrift, minimum effort.
    - **Punishment type/technology:** Peer vs. institutional, pool vs. targeted, exclusion vs. deduction (Cobo-Reyes et al., 2022; Sun et al., 2025; Cui et al., 2022; Wang et al., 2025).
    - **Punishment parameters:** Cost and impact per unit, fine-to-cost ratios (Pi et al., 2022; Lee et al., 2022; Gao et al., 2023).
    - **Network structure:** Spatial, small-world, well-mixed, size of punishment network (Pi et al., 2022; Cui et al., 2022; Wang et al., 2025).
    - **Feedback/adaptivity:** State-dependent or dynamic punishment is sometimes more efficient (Wang et al., 2025; Sun et al., 2023; Gao et al., 2023).

- **Other moderators:**
    - **Group size (player_count):** Larger groups can attenuate efficiency gains, requiring stronger or better-coordinated punishment (Jiang et al., 2023; Kurokawa, 2023).
    - **Repetition (num_rounds):** In repeated games, punishment is more effective at raising and sustaining efficiency.
    - **Synergy (mpcr):** Higher MPCR makes cooperation easier; low MPCR requires stronger punishment for positive efficiency gains (multiple theory papers).
    - **Antisocial punishment:** The presence and level of antisocial punishment can neutralize or reverse positive effects (Bahbouhi et al., 2024; Pi et al., 2022).
    - **Team decision-making / consensus rules:** Unanimity or collective decision-making (as opposed to individual) can suppress antisocial punishment and increase net efficiency gains (Bahbouhi et al., 2024; Gao et al., 2023).
    - **Open vs. closed groups / migration:** Punishment especially improves efficiency where groups are open to migration (Cobo-Reyes et al., 2022).

- **Empirical divergence and conditions where punishment does not improve efficiency:**
    - In adjacent designs (e.g., trust games, asymmetric roles), punishment can sometimes reduce efficiency due to sanction costs exceeding cooperation gains (Herne et al., 2022; Calabuig et al., 2024).
    - Some lab experiments show that costly punishment is applied inefficiently or for non-prosocial reasons, resulting in net efficiency loss (Zhang & Pei, 2022).
    - Institutional conditions (e.g., clear norm coordination, formal grievance mechanisms) are necessary to ensure that punishment increases efficiency (Macleod et al., 2025).

## Quantitative Patterns

- Where explicit efficiency ratios are available, the effect of enabling punishment is often large and positive when:
    - Baseline cooperation is moderate or low.
    - Punishment is well-calibrated (not too costly; technology is precise).
    - Antisocial punishment is suppressed or filtered through collective mechanisms (Bahbouhi et al., 2024; Pi et al., 2022).
    - Institutional (tax-based or formal) punishment is especially effective (Li et al., 2022; Sun et al., 2025; Wang et al., 2025).

- **Threshold/stepwise effects:** Many simulation models show sharp transitions to high efficiency as punishment parameters cross a critical threshold, with feedback or adaptivity increasing the chance of positive outcomes (Liu et al., 2024; Wang et al., 2025).

# 5) Prediction Guidance

Based on this literature, the following **guidance is robustly supported** for forecasting efficiency effects of enabling punishment in public-goods-game-like environments:

- **If the empirical setting is a standard or close-variant repeated PGG, with standard linear returns and moderate to large groups, then:**
    - **Enabling punishment will generally increase efficiency**, with the magnitude of increase a function of:
        - Baseline (control) efficiency: Larger effect if control efficiency is low.
        - Punishment cost and efficacy: Higher efficiency gains with low-cost, high-impact punishment.
        - Absence of widespread antisocial punishment: If antisocial punishment is common (especially with peer punishment and weak norm coordination), net efficiency gains may be negligible or negative.
        - Structure of punishment network/tech: Universal access to punishment is not always better; limited, well-targeted punishment can be more efficient.
        - Institutional support: Institutional or tax-based punishment is generally more efficient than decentralized peer punishment, especially in large or open groups.
        - Team decision-making: Unanimity or majority-based team punishment decisions suppress inefficient punishment and raise efficiency.
        - Reward/exclusion hybrid mechanisms: Adding reward to punishment can, in some cases, further increase efficiency, but reward alone is usually less effective than punishment alone.

- **If the game variant is a threshold/collective-risk PGG or similar coordination game:**
    - The presence of punishment raises the likelihood of achieving the coordinating target (group success), and thus increases efficiency, *but only if* punishment is sufficiently strong/probable (Jiang et al., 2023), and is especially important in larger groups or with higher risk of group failure.

- **If enabling punishment in a design where baseline efficiency (control) is already high or punishment cost is excessive:**
    - The predicted gain in efficiency is small, zero, or potentially negative.
    - If punishment cost is above a threshold where the resource lost to punishment exceeds gains from increased cooperation, efficiency may fall.

- **Where efficiency evidence is only indirect (i.e., only cooperation rates reported):**
    - Efficiency is likely to follow the direction of large changes in cooperation rates, but scaling may be sublinear if punishment is costly.
    - *Explicit caution*: Do not equate increased cooperation rate with higher efficiency unless the cost of punishment is known to be small or moderate.

- **Where evidence is conflicting or ambiguous:**
    - In highly asymmetric, binary, or team investment games, or where punishment can be misapplied or uncoordinated, efficiency may be benefited, unchanged, or harmed.
    - Use control efficiency and punishment cost as joint moderators; clarify the context.

# 6) Design Dimensions Highlighted Across Papers

**Of the 14 prediction dimensions:**

- **Directly informed:**
    - `player_count` (group size): Well studied, especially impact of size on punishment effectiveness and efficiency.
    - `num_rounds`: Repeated vs. single-shot effects are a common focus.
    - `mpcr`: Marginal per-capita return is a central parameter in almost all PGG studies.
    - `punishment_cost`, `punishment_tech`: Core design variables, thoroughly analyzed.
    - `all_or_nothing`: Both all-or-nothing and continuous variants are seen in empirical and theory papers.
    - `show_n_rounds`, `show_other_summaries`: Some experimental papers vary these (Wang & Huang, 2022), though less commonly in theory.
    - `reward_exists`/`reward_cost`/`reward_tech`: Common in hybrid mechanism studies.

- **Indirectly addressed:**
    - `default_contrib`: Explored in a few experimental papers (opt-in vs. opt-out framing), often as a context variable.
    - `chat`: Manipulated in some lab experiments (e.g., Wang & Huang, 2022), but rarely systematically as a moderator with punishment.

- **Contextually discussed/mentioned:**
    - `show_punishment_id`: Identity of the punisher is considered as a moderator in some lab experiments and simulation studies, but not systematically mapped.

- **Essentially missing or not systematically studied:**
    - No substantial evidence on the effects of `chat`, `show_punishment_id`, or complex feedback/visibility designs on efficiency when enabling punishment relative to control.
    - Interaction effects among more than 2-3 dimensions are rarely mapped explicitly with payoff outcomes.

# 7) Important Limitations

- **Efficiency outcomes are unavailable or only inferred for a large portion of the literature:** When studies report only cooperation rates, punishment frequency, or strategy distributions, the mapping to efficiency is ambiguous, especially when punishment is costly.
- **Empirical vs. theory gap:** Many findings are simulation/theory-based. Human participants sometimes misuse punishment or apply antisocial punishment more than is predicted by theory, which can undermine efficiency gains (Zhang & Pei, 2022).
- **Sparse evidence for some design dimensions:** Chat, contribution framing, feedback visibility, and identity of punishers are rarely studied as interacting moderators of efficiency under punishment.
- **Potential for non-monotonic or negative effects:** Punishment can reduce efficiency when costs are high or if punishment is misapplied. Over-confidence in positive efficiency effects can lead to predictive error.
- **Heterogeneous baseline conditions:** Variation in baseline (no-punishment) efficiency, group dynamics, and participant population can moderate effects and make prediction from design dimensions alone less accurate.
- **Complex variants and mapping limitations:** Many theoretical studies involve idealized infinite populations, deterministic dynamics, or complex hybrid/adjacent models, whereas lab experiments operate in finite, noisy, more variable settings.
- **Publication bias toward positive results:** Negative or null findings may be underrepresented.

---
**In conclusion**, the literature robustly supports the general prediction that enabling punishment (especially effective, not overly costly, and institutionally/collectively coordinated punishment) will increase efficiency in standard or moderately challenging PGG-like environments with low baseline efficiency. However, several important qualifiers apply, especially regarding the potential for costly, misapplied, or antisocial punishment to negate efficiency gains in particular game designs or populations. Many design dimensions are directly supported, but several—including communication, sanction visibility, and contribution framing—are weakly addressed. Predictions should incorporate uncertainty and contextual moderators accordingly.
