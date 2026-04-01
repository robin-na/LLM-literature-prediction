# 1) Evidence Base

The 13-paper evidence base combines empirical (mostly laboratory experiments, with some field and survey/hypothetical studies) and theoretical works. Only a minority of papers are directly focused on public-goods games (PGGs) with peer punishment and measure efficiency or related payoff outcomes. The set includes:

- **Empirical PGG-focused experiments**: A few papers (e.g., Castillo et al., 2021) use standard or close variants of linear public goods games and directly measure efficiency or group payoff changes due to punishment mechanisms.
- **Theory papers**: Several theory and review papers (e.g., Zhang & Pei, 2022; Forges et al., 2016; Madeo & Mocenni, 2021) discuss the mechanistic or predicted impacts of punishment in social dilemmas but do not provide new empirical data for PGG settings.
- **Papers reporting only on behavioral outcomes** (e.g., cooperation, willingness to punish) or focused on adjacent game types (ultimatum, principal-agent, CPR/resource games): These studies provide context but lack direct efficiency evidence.
- **Breadth vs. Narrowness**: The set is broad in covering a range of experimental, theoretical, and adjacent-game designs, but is narrow concerning the core downstream prediction task: Empirical, multi-player PGGs with direct comparison of group efficiency/payoff under peer punishment enabled vs. disabled.

# 2) Task Relevance

Evaluated across three target-relevance axes:

| Axis                  | Label   | Explanation                                                                                  |
|-----------------------|---------|----------------------------------------------------------------------------------------------|
| PGG or variant        | exact   | 3-4 papers use exact PGG settings (e.g., Castillo et al., Windmann et al.), several are close (e.g., field CPR, redistribution games), many are adjacent.                   |
| Punishment or sanctions | exact  | Peer or centralized punishment is manipulated or reviewed in several studies; a few study only adjacent social feedback or norm mechanisms.                               |
| Efficiency or related payoff | exact (minority), adjacent (majority) | Only a small subset reports direct efficiency or group payoff; most report non-payoff behavioral outcomes (cooperation, punishment frequency, slack).               |

Most available evidence is from **adjacent contexts** or focuses on **behavioral rather than payoff outcomes**. The literature is strongest for punishment mechanisms and behavioral cooperation relevance, but only a minority provide direct evidence for efficiency effects in true PGGs with peer punishment.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (Efficiency, Group Payoff/Earnings):**
    - **Directly measured** in a minority of papers (e.g., Castillo et al., 2021; Przepiorka & Diekmann, 2020; Abbink et al., 2004; Madeo & Mocenni, 2021 for theory).
    - **Proxy measures/Implied payoffs:** Several studies infer likely payoff changes from behavior (e.g., increased cooperation rates likely increase efficiency), but do not report payoff data (e.g., Becchetti et al., 2018; Noussair et al., 2015).
- **Non-payoff behavioral outcomes:**
    - **Contribution/cooperation rates, frequency of punishment use, willingness to punish, norm compliance, emotional reactions, slack/honesty in reporting.**
    - Most of the literature reports these outcomes rather than direct measures of average efficiency.

**Explicit statements:** Where outcomes are non-payoff, they are often interpreted as evidence for likely payoff movement, but this is sometimes speculative or indirect.

# 4) Main Findings Relevant To Prediction

- **Centralized (manager) punishment in linear PGGs robustly increases efficiency/payoff versus a no-punishment baseline.** The effect is seen across different punishment costs/effectiveness but for centralized, not peer, punishment (Castillo et al., 2021).
- **Peer punishment improves cooperation but may not always increase efficiency:** Theoretical reviews and some empirical evidence indicate that peer punishment can raise cooperation, but the efficiency effect is ambiguous because the costliness of punishment may offset welfare gains (Zhang & Pei, 2022; Abbink et al., 2004).
    - **Empirical (bargaining):** In two-player bargaining-like games, enabling punishment can lower efficiency due to destruction of value via costly punishment (Abbink et al., 2004).
    - **Field and non-lab evidence:** In applied/field environments or CPRs, peer punishment is sometimes ineffective at improving cooperation and may not translate into improved group outcomes (Noussair et al., 2015).
- **Reward mechanisms or social incentives (feedback, approval) sometimes substitute for punishment:** Public feedback (with visible identifiers) can increase efficiency; private feedback does not (Przepiorka & Diekmann, 2020). Reward-only mechanisms are less effective unless rewards are large or combined with punishment (Zhang & Pei, 2022; Chen, 2012).
- **The effect of enabling punishment is sensitive to:**
    - The **cost and effectiveness** of punishment, whether the setting is peer or centralized (more data for centralized), and whether punishment rates are very low, very high, or intermediate (Abbink et al., 2004).
    - The **context/framing**—effects in lab PGGs do not always generalize to field/real-world analogues (Noussair et al., 2015).
    - Whether **social vs. monetary sanction** is at play; motivation may differ and thus impact is not always aligned on payoffs (Leibbrandt & López-Pérez, 2014).

# 5) Prediction Guidance

- **For linear PGGs with centralized punishment** (manager can punish; structure as in Castillo et al., 2021): Enabling punishment is strongly likely to increase efficiency, regardless of manager selection mechanism or moderate variations in punishment cost or scope.
- **For standard, peer punishment PGGs:** The evidence is more equivocal:
    - **Theory and prior reviews** (Zhang & Pei, 2022) suggest cooperation rises, but efficiency does not always. If punishment is costly and frequently used, net efficiency gains may be absent or even negative (costs of punishment can offset benefits of increased cooperation) (Abbink et al., 2004).
    - **Prediction from design dimensions:** Key moderators are the punishment cost/effectiveness, who can administer punishment, and the presence of complementary incentives (reward, public feedback, visible identities).
    - **Control efficiency is a useful baseline:** If control (no punishment) efficiency is already high, additional gains from punishment may be limited or negative (cost outweighs cooperation benefit). If control efficiency is low (very low baseline cooperation), punishment is more likely to yield net gains—unless the costs incurred from punishment are too high.
    - **Settings with social/identifiable feedback** (showing others’ actions/punishers): These can substitute for punishment and improve efficiency without the costs of direct sanctions (Przepiorka & Diekmann, 2020).
- **No quantitative prediction curves/coefficients** are present; all guidance is qualitative and contingent upon design details (dimension-level inference).

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions (empirical or theory, many with at least contextual detail):**
- `player_count`: A core parameter in most studies; group size considered in most experiments and theory.
- `num_rounds`: Frequent factor; repeated games, length/known endpoint matter for design and effect sustainability.
- `mpcr`: Often specified or held constant; high vs. low MPCR affects the temptation to free-ride and response to punishment.
- `all_or_nothing`: Manipulated in some, default in others; discussed in terms of discrete vs. continuous contributions.
- `chat`: Sometimes manipulated (presence/absence of communication).
- `punishment_cost` and `punishment_tech` (who can punish, what fee-to-fine ratios are used); important for both theory and empirical work.
- `reward_exists`, `reward_cost`, `reward_tech`: Some studies explore these alongside punishment.
- `show_other_summaries`, `show_punishment_id`: Explicitly studied in manipulations of public/private feedback (Przepiorka & Diekmann, 2020).
- `default_contrib`/`contribution framing`: Rarely varied, but occasionally present.
- `show_n_rounds`: Sometimes manipulated.
**Indirectly or sparsely informed dimensions:**
- `punishment_magnitude`: Only sometimes reported or manipulated.
- `reward_magnitude`: Seldom detailed.
- Some interaction effects between dimensions are hypothesized/theorized, but rarely directly tested.

# 7) Important Limitations

- **Coverage Gap for Peer Punishment Efficiency in Multi-player PGGs:** The literature provides only limited direct empirical evidence for the treatment effect of peer punishment on efficiency in the canonical, linear, multi-player PGGs—most evidence is for centralized punishment, adjacent games, or non-payoff outcomes.
- **Outcome Alignment:** Many studies focus on behavioral proxies (contribution/cooperation, frequency of punishment) rather than group payoff or efficiency, restricting their predictive power for payoff-based outcomes.
- **External Validity:** Positive punishment effects in lab PGGs do not consistently generalize to field settings or other game structures (Noussair et al., 2015; Abbink et al., 2004).
- **Qualitative not Quantitative Guidance:** No studies offer explicit quantitative prediction models or parameter estimates for mapping design dimensions plus control efficiency to treatment efficiency.
- **Dimension Gaps:** Some game design dimensions relevant for prediction (e.g., default contribution framing, magnitude settings, many interaction terms) have little or no direct empirical evidence.
- **Ambiguity and Contradictions:** Where evidence exists, findings are sometimes in tension:
    - Peer punishment increases cooperation but not always efficiency (Zhang & Pei, 2022).
    - In bargaining/minigames, punishment can decrease efficiency (Abbink et al., 2004).
- **Missing or under-specified for key prediction settings:** Many results are for adjacent contexts (dyadic games, principal-agent, CPR) rather than core PGG designs.
- **Reward and feedback mechanisms as moderators or substitutes**: While some papers address combined or alternate incentives, these are not systematically mapped onto prediction dimensions.

**Summary:**  
This paper set offers good qualitative, mechanism-level insight about when and why enabling punishment in public-goods environments may (or may not) increase efficiency. However, only one or two studies provide direct, empirically supported guidance for treatment efficiency in canonical PGGs, and support is much stronger for centralized than peer punishment. Behavioral proxies predominate, and generalizability is uncertain. Prediction efforts must thus rely on well-supported mechanisms but remain cautious and guarded due to substantial, well-documented evidentiary gaps.
