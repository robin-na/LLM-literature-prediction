# 1) Evidence Base

This literature set consists entirely of theoretical papers (11/11), with no empirical or experimental studies. Most papers use formal models (evolutionary game theory, agent-based simulation, or analytical methods) rather than reporting data from lab or field experiments. The coverage is broad in terms of topics—spanning public goods games, prisoner’s dilemma, norm change, cooperation scaling, and enforcement mechanisms—but only a minority of papers are directly focused on payoff-based outcomes in the canonical or near-canonical public goods game (PGG) with peer punishment. There is substantial attention to general mechanisms (norms, punishment, rewards, reputation), but primarily in adjacent settings or at a conceptual level. Only a few provide direct or close quantitative analysis of efficiency (group payoff normalized to theoretical maximum) in PGG with punishment (notably, Lee et al., 2022).

**Empirical versus Theoretical Balance:** All papers are theoretical or review-based; none bring new data.

**Narrowness versus Breadth:** The set is thematically broad regarding “cooperation and punishment,” but narrow in directly informing predictions about efficiency effects of punishment in PGG as specified in the downstream task.

# 2) Task Relevance

Relevance is evaluated on three dimensions:

### a) `pgg_or_variant`  
- **Exact:** Lee et al. (2022), Lv & Song (2022), Hua & Liu (2024)
- **Close/Adjacent:** Wang et al. (2023); Van Lange & Rand (2022)—review repeated social dilemmas including PGG.
- **Adjacent/Weak:** Gou & Li (2023), Wang et al. (2022); other papers (Boyd & Richerson, Traulsen & Glynatsi, Andrighetto & Vriens, Gross & Vostroknutov) discuss cooperation or collective action problems, often using Prisoner’s Dilemma or conceptual models.

### b) `punishment_or_sanctions`  
- **Exact:** Lee et al. (2022), Lv & Song (2022), Wang et al. (2023)
- **Adjacent:** Some review or discuss direct sanctions, punishment, or social norm enforcement in more general forms (Boyd & Richerson, Van Lange & Rand, Andrighetto & Vriens, Gross & Vostroknutov).
- **None:** Papers focusing solely on rewards or noise (Hua & Liu, 2024; Wang et al., 2022).

### c) `efficiency_or_related_payoff_outcome`  
- **Exact:** Lee et al. (2022), Hua & Liu (2024; for reward)
- **Close:** Wang et al. (2023; cumulative institutional cost as a welfare proxy)
- **Adjacent:** Most others measure cooperation rate/behavior or discuss efficiency conceptually.
- **None:** Several focus only on cooperation or norm-following without any group payoff metrics.

**Summary:** Only a small subset (Lee et al., 2022) provides exact, payoff-based, and PGG-relevant theory about the effects of punishment on efficiency. Most others are either focused on adjacent questions/mechanisms or on non-payoff outcomes.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes (directly relevant to prediction):**
- **Group efficiency/average payoff:** Lee et al. (2022) (for punishment in structured PGG); Hua & Liu (2024) (for rewards, not punishment); Wang et al. (2023) (institutional cost to reach cooperation).
- **Cumulative institutional cost (as welfare proxy):** Wang et al. (2023).

**Non-payoff behavioral outcomes (not directly usable for efficiency prediction):**
- **Cooperation/contribution rates or cooperation stability:** Lv & Song (2022), Gou & Li (2023), Wang et al. (2022), Van Lange & Rand (2022), Boyd & Richerson (2022), Andrighetto & Vriens (2022), Gross & Vostroknutov (2022).
- **Norm compliance/tipping points in social behavior:** Andrighetto & Vriens (2022); often mechanistic, lacking explicit payoff data.
- **Punishment frequency/assigned punishment:** Sometimes discussed, but not translated into welfare or group efficiency metrics.
- **No outcome data reported:** Traulsen & Glynatsi (2023), as a field review.

**Explicit separation:** The majority of the literature set focuses on behavioral outcomes rather than payoffs; these cannot be treated as efficiency except where explicitly modeled.

# 4) Main Findings Relevant To Prediction

**Direct Findings:**
- **Enabling punishment in structured PGGs can increase group efficiency, but only if punishment costs are moderate and the fines (punishment effectiveness) are high** (Lee et al., 2022). There exists an optimal punishment cost: too low or too high can both be inefficient. The efficiency gain is modulated by the presence of support (such as a tax) for punishers.
- **If punishment costs are too high or the fine is too low, enabling punishment can decrease efficiency**—in some cases causing cyclic dominance among strategies that may destabilize high payoff regimes (Lee et al., 2022).

**Indirect/Mechanistic Findings:**
- **Cooperation rates increase with punishment under certain learning rules and parameter regimes, but**—importantly—the allocation of resources toward punishing can reduce total investment in cooperation, which may not always translate to efficiency gains (Lv & Song, 2022; non-payoff evidence).
- **Punishment is more effective at sustaining cooperation when contributions are observable or when social reputation mechanisms are in place** (Van Lange & Rand, 2022; non-payoff, contextual).
- **Institutional (rather than peer) punishment can achieve high cooperation efficiently if properly optimized** (Wang et al., 2023), but these results pertain mostly to institutional cost, not peer punishment or group payoff per se.
- **Scale and structure matter:** Efficacy of punishment may decrease as group size increases, requiring additional supporting mechanisms (Boyd & Richerson, 2022; contextual, not payoff or design-specific).
- **Adaptive rewards can also achieve efficient cooperation** (Hua & Liu, 2024), but this informs efficiency prediction only for reward-based interventions, not punishment.

**Mechanisms Moderating Prediction:**
- The effect of punishment on efficiency is sensitive to design parameters (player count, punishment cost, magnitude, network topology), and to the structure of the population (well-mixed vs. spatial).
- Social norms and their strength can moderate the effect of punishment—with strong norms potentially leading both to desirable (high cooperation/efficiency) and undesirable (entrenched inefficiency or norm-based exclusion) equilibria (Andrighetto & Vriens, 2022).

# 5) Prediction Guidance

- **For cases matching Lee et al. (2022):** If peer punishment is enabled in a spatially structured PGG, and the punishment cost per unit is moderate and fines are relatively large, expect an increase in average group efficiency relative to control (no-punishment). The increase is largest when punishment costs are not excessive, fines are sufficiently large, and optional supports (like taxes for punishers) are available and properly calibrated. However, if the cost is too high or the fine too low, efficiency may not rise and can decrease versus no-punishment—a non-monotonic relationship.
- **Sensitivity:** Results are highly sensitive to the precise punishment cost and magnitude. There is not a simple rule that punishment always increases efficiency; rather, inefficient punishment regimes (e.g., high cost, low fine) can erode group payoff.
- **Parameter importance:** For tasks requiring prediction from design variables plus baseline/control efficiency, priority should be given to parameterizing punishment cost, punishment magnitude, and the underlying structure of the game (network vs. well-mixed, spatial). Related parameters such as player count and MPCR (marginal per-capita return) have moderate, model-dependent effects.
- **Sparse evidence for other design features:** For other design dimensions (e.g., chat, observability, identity disclosure), the literature highlights their role in promoting cooperation, but not in a way that supports quantitative efficiency prediction.
- **Behavioral outcomes ≠ efficiency:** In the absence of direct efficiency/earnings figures, increases in contribution or cooperation rates [as in Lv & Song (2022)] should not be translated directly into efficiency predictions, due to possible offsetting punishments costs and behavioral spillovers.
- **Extrapolation beyond spatial or structured settings:** For well-mixed or laboratory PGGs (without explicit spatial or network structure), the general principles from Lee et al. (2022) likely apply qualitatively, but there is insufficient theory in this set to specify quantitative effects. Caution should be taken not to overfit predictions outside of modeled regimes.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed (supported by at least one exact/close PGG with efficiency/punishment analysis):**
- `player_count` (Lee et al., 2022; Hua & Liu, 2024)
- `num_rounds` (Lee et al., 2022; Lv & Song, 2022; Gou & Li, 2023)
- `all_or_nothing` (Lee et al., 2022; Lv & Song, 2022; Hua & Liu, 2024)
- `mpcr` (Lee et al., 2022; Hua & Liu, 2024)
- `punishment_cost` (Lee et al., 2022; Lv & Song, 2022; Wang et al., 2023)
- `punishment_tech` (Lee et al., 2022; Lv & Song, 2022)
- `reward_exists`, `reward_cost`, `reward_tech` (Hua & Liu, 2024; Wang et al., 2023—for reward only, not punishment)

**Indirect/Contextual Only:**
- `show_other_summaries`, `show_n_rounds`, `chat`, `show_punishment_id` (mentioned as moderators of cooperation, e.g., Van Lange & Rand, 2022; Boyd & Richerson, 2022, but not tied to efficiency outcomes).

**Effectively Missing:**
- `default_contrib` (contribution framing not modeled or tested)
- `reward_cost`, `reward_tech`, `reward_exists` (addressed for rewards, not for punishment-based games)
- Any joint manipulation or analysis of id disclosure/observability in punishment-enabled PGG with efficiency data.
- Most papers do not discuss or manipulate the presence of chat, nor the behavioral implications of identity disclosure for peer punishment efficiency.

# 7) Important Limitations

- **Empirical gap:** All evidence is theoretical or review-based; no experimental or field data are included to validate the theoretical models or predictions.
- **Sparse coverage of design space:** Only a few design dimensions are systematically manipulated in ways that map to the full set of prediction inputs. Variables such as chat, default contribution, identity visibility, or information structure are rarely addressed in relation to efficiency.
- **Context specificity:** Main direct evidence pertains to structured or spatially organized PGGs, not to well-mixed groups or all lab PGG variants. Applicability to other environments (e.g., online, asynchronous, laboratory) is uncertain.
- **Payoff-behavior disconnect:** Most papers report behavioral outcomes (cooperation rate, norm adherence) rather than efficiency or group payoff, limiting the direct applicability to the prediction of treatment efficiency in the downstream task.
- **No unified theory for all dimensions:** Theoretical predictions are sensitive to parameter choices (especially punishment cost and fine), with non-monotonic effects and possible counterintuitive outcomes (e.g., inefficiency at high punishment costs). There is no simple rule or mapping for most design dimensions.
- **Limited evidence on combined interventions:** Papers addressing both punishment and reward (Wang et al., 2023; Hua & Liu, 2024) do so mainly for institutional punishment/reward, whereas the task concerns peer punishment.
- **No data-driven calibration:** The lack of empirical data prevents data-driven translation of qualitative or phase-diagram relationships into quantitative prediction models.
- **No direct exploration of sequential or duration effects:** While number of rounds is sometimes a parameter, its interaction with other design features for efficiency prediction is not systematically addressed.

**Summary Statement:**  
The present literature set delivers strong theoretical insight into how punishment can, but does not always, increase efficiency in structured public goods games—primarily under spatial/networked models and when punishment is neither too weak nor too costly. For other game designs, populations, and nuanced intervention details, the evidence is indirect, incomplete, or missing. This set is best suited to inform qualitative prediction and to highlight crucial game design moderators (chiefly punishment cost and fine), but lacks comprehensive, empirical, or design-complete quantitative guidance for downstream efficiency prediction.
