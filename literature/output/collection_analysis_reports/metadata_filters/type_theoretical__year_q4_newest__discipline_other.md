# 1) Evidence Base

The paper set is composed entirely of **theoretical and modeling papers**; there are no empirical or experimental papers. The vast majority use evolutionary game theory, agent-based modeling, or analytical game-theoretic approaches—in some cases supplemented with embedded meta-analyses or comparative reviews (see Vasconcelos et al., 2022). The domains represented are diverse, ranging from canonical public goods games (PGGs) to adjacent or structurally similar settings such as regulatory dilemmas, innovation governance, environmental and resource management, and multi-actor cooperation games (e.g., trust, signaling, or principal-agent scenarios).

On the **prediction task of treatment efficiency (group payoff as a ratio to full cooperation) in PGG-like games with peer punishment**, the evidence base is **narrow**:
- Only one paper (Vasconcelos et al., 2022) provides an exact match (theoretical and meta-study synthesis) on all dimensions.
- A handful of papers provide a **close** match, reporting efficiency, group payoff, or closely related outcomes in adjacent designs or theoretical variants (e.g., Lim & Capraro, 2022; Li & Jiang, 2023).
- Most papers focus on **behavioral outcomes** (cooperation rates, strategy frequencies) in adjacent designs without reporting efficiency or group payoff as outcomes.
- Few papers report **parameter sweeps or dimension-specific effects** in forms directly translatable to prediction along the provided design dimensions.
- **Experimental manipulation** of punishment parameters (cost, tech, existence, reward interaction) is often present, but payoff/efficiency observables are rarely the primary focus.

Thus, prediction guidance must rely largely on theoretical findings and mechanism arguments, supported by a narrow empirical meta-review and simulation evidence.

# 2) Task Relevance

The three key areas of relevance are summarized below, with consistent use of the relevance labels (`exact`, `close`, `adjacent`, `weak`, `none`):

| Target-Relevance Dimension           | Evidence Coverage                     |
|--------------------------------------|---------------------------------------|
| `pgg_or_variant`                     | Several papers are `exact` (Vasconcelos et al., 2022; Quan et al., 2023; Wu & Sun, 2022; Park, 2022), but the majority are `adjacent` (regulatory, multi-actor social dilemmas, or PD/trust game variants). |
| `punishment_or_sanctions`            | Many papers are `exact` (Vasconcelos et al., 2022; Quan et al., 2023; Lim & Capraro, 2022; Rubin, 2022), with some discussing only `adjacent` forms (legal or social sanctions, government intervention). |
| `efficiency_or_related_payoff_outcome`| Direct `exact` reporting is rare (Vasconcelos et al., 2022; Lim & Capraro, 2022; Li & Jiang, 2023), with most presenting `adjacent` or `close` coverage (total contribution, stability, welfare proxies, or payoff-based mechanism arguments). A majority focus on non-payoff behavioral measures (`adjacent` or `weak`). |

**Summary:** The set is **rich in theory and mechanism coverage** on PGGs and punishment, but only a minority directly address the efficiency outcome of interest with payoff-related measurements or simulations.

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes:**
- **Efficiency/Group Payoff**: Only a minority report this directly (Vasconcelos et al., 2022; Lim & Capraro, 2022; Li & Jiang, 2023).
- **Proxies**: Some address aggregate earnings, welfare, or surplus as proxies (Rubin, 2022—sometimes only `close` relevance).

**Non-Payoff Behavioral Outcomes:**
- Far more common: **cooperation rate**, contribution rate, **compliance rate**, **stability of cooperation**, or related strategy frequencies (Quan et al., 2023; Wu & Sun, 2022; Wang & Cui, 2022; etc.).
- Outcomes such as norm compliance, punishment/reward frequency, or honesty rates (e.g., Rubin, 2022).

**Important Distinction:** Outcome variables in most papers are **not** efficiency as defined for prediction (total realized vs. maximum possible group payoff); they measure **intermediate behavioral dynamics** rather than final welfare.

# 4) Main Findings Relevant To Prediction

**Synthesized empirical/theoretical findings:**

- **Punishment institutions generally increase efficiency in canonical PGGs when well-designed and appropriately implemented,** but the effect depends on institutional scale, adoption mechanisms, and learning/information conditions. Group-level (collective) punishment institutions are especially effective for global goods; poor alignment or information quality can limit effectiveness (Vasconcelos et al., 2022).
- **The cost and structure of punishment (graded vs. fixed, dynamic vs. static, cost/fine ratio) are key moderators:** Lower punishment cost, graded/dynamic intensity, and effective detection all predict stronger positive effects on cooperation and (by inference or direct evidence) efficiency (Quan et al., 2023; Wang & Cui, 2022; Jiang & Zheng, 2024).
- **Network structure matters:** Structured populations (networks) lower the threshold for punishment effectiveness and allow high efficiency to be reached at lower punishment levels (Lim & Capraro, 2022; Li et al., 2023).
- **Combination with rewards or complementary mechanisms is often necessary for maximal efficiency:** Punishment alone may be insufficient; combining with rewards and institutional incentives achieves more robust high-payoff equilibria, especially in multi-actor settings (Li & Jiang, 2023; Zhao & Zou, 2025).
- **Punishment that targets non-cooperation (defection) increases efficiency; punishment targeting other behaviors (e.g., lying) may harm overall efficiency:** The target of punishment is a critical design feature (Rubin, 2022).
- **Adoption and effectiveness of punishment institutions are sensitive to perceived efficacy, learning opportunities, and information sharing:** Poorly informed or poorly designed institutions may be rejected or have no/mixed effect (Vasconcelos et al., 2022).
- **High cooperation rates do not always imply high efficiency:** If punishment is mis-targeted or undetectable defection is possible, observed cooperation can be decoupled from true payoff outcomes (Goodman, 2023).
- **Most findings on increased cooperation, system stability, or compliance are indirect evidence for efficiency:** These should only supplement, not substitute, direct efficiency measurement unless mechanism arguments are exceptionally well specified.

# 5) Prediction Guidance

**How this literature should inform prediction of treatment efficiency from design dimensions plus control efficiency:**

- **Presence/Absence of Punishment**: Enabling peer punishment in canonical PGGs generally increases efficiency compared to the no-punishment condition, but only within certain institutional and informational contexts.
- **Magnitude of Effect**: The efficiency lift is greatest when:
    - Punishment cost is low relative to the fine/impact (Quan et al., 2023).
    - The game environment supports learning and transparent information (Vasconcelos et al., 2022).
    - The punishment institution matches the scale/nature of the resource dilemma (Vasconcelos et al., 2022).
    - The network structure is not too sparse, allowing punishment to be effective at lower cost (Lim & Capraro, 2022).
- **Institutional and Mechanism Design**: Graded/dynamic punishment and institutionally collective adoption are more effective for efficiency; static or individualized regimes are less robust. The design of the punishment technology and adoption mechanism are key model variables.
- **Control Efficiency as Predictor**: In some models (Rubin, 2022), the pre-punishment (control) efficiency may not predict the post-treatment (with punishment) efficiency if punishment targets behaviors other than defection (e.g., lying), if defection detection is imperfect, or if the costs of punishment are high relative to its benefits.
- **Interaction with Rewards and Other Tools**: The presence and specification of rewards can moderate punishment effects. Combined regimes usually outperform punishment-only or reward-only regimes.
- **Limitations of Non-Payoff Proxies**: If literature provides only behavioral proxies (e.g., cooperation rates), predictions should be qualified, as increased cooperation does not always translate proportionally to group efficiency/payoff (Goodman, 2023; Rubin, 2022).
- **Ambiguity and Contingency**: Effectiveness is reduced or even reversed when punishment is misaligned, costly, poorly targeted, or used in social environments that enable covert defection or retaliation.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions:**
- `player_count`, `num_rounds`, `mpcr`, `all_or_nothing`, `punishment_cost`, `punishment_tech`: Often explicitly modeled; several papers sweep or manipulate these dimensions (e.g., Vasconcelos et al., 2022; Quan et al., 2023; Lim & Capraro, 2022).
- `reward_exists`, `reward_cost`, `reward_tech`: Sometimes manipulated in multi-tool regimes (Li & Jiang, 2023; Zhao & Zou, 2025).

**Indirectly informed or contextually discussed:**
- `show_other_summaries`, `show_n_rounds`, `show_punishment_id`: Occasionally discussed as aspects of information sharing or learning environment but rarely directly tested for efficiency consequences. Vasconcelos et al. (2022) highlight information environment as key in institution adoption and effectiveness.
- `chat`, `default_contrib`: Mentioned only peripherally if at all; some papers discuss communication as a generic cooperation facilitator but do not model it directly.
- `punishment_magnitude`: Sometimes embedded in the definition of cost/impact, but not always separately varied.

**Effectively missing or unaddressed:**
- Effects of default contribution framing, identity transparency, total round transparency, and explicit communication are largely absent or only alluded to contextually without quantitative analysis.
- Many dimensions (especially those tied to user interface or presentation) are **not directly modeled**, making extrapolation across those parameters highly uncertain.

# 7) Important Limitations

- **Scarcity of payoff/efficiency data in PGGs**: Direct, empirical, or even simulated evidence for the effect of enabling punishment on efficiency is limited and concentrated in a few theory/meta-review sources (notably Vasconcelos et al., 2022).
- **Heavy reliance on theoretical models**: Almost all findings are based on simulation, analytic derivation, or conceptual argument. Predicted magnitude, variability, and external validity thus remain uncertain.
- **Behavioral proxies dominate**: Most adjacent literature uses cooperation or compliance rates as the main outcome, and may overstate the predictability of payoff outcomes.
- **Diversity of game structures**: Many "adjacent" papers involve more complex or institutionally rich settings (e.g., multi-level governance, trust signaling, regulatory dilemmas) which may not cleanly map to canonical PGG design dimensions.
- **Parameter coverage is patchy**: Not all relevant design dimensions are explored systematically; especially sparse are dimensions related to communication, information transparency, default choices, and interface details.
- **Potential for mechanism mismatches**: Some models assume perfect detection of defection or perfect enforcement, which can overstate punishment efficacy compared to laboratory or field experiments.
- **Negative or ambiguous effects**: Some models (Rubin, 2022; Goodman, 2023) highlight scenarios where punishment does not improve—or may even decrease—group efficiency, especially if mis-targeted, costly, or if undetected defection is possible.
- **Multi-tool and interaction effects**: Many findings suggest that predictors are interdependent (e.g., punishment alone vs. punishment + reward), but such interactions are seldom explicitly modeled across all dimensions.
- **Absence of experimental parameter sweeps**: Without systematic empirical or broad simulation parameter sweeps, generalizing to new combinations of design dimensions is uncertain.

---

**In conclusion:** The literature provides solid mechanistic and theoretical support for the claim that enabling peer punishment in PGGs *can* increase group efficiency, but the magnitude, robustness, and boundaries of this effect remain only partially characterized across the full range of design features relevant for fine-grained prediction. Where efficiency is not directly measured, proxy outcomes and simulated mechanisms should be used with clear caveats. The most robust predictions will be for canonical PGGs with well-aligned institutions, low punishment cost, adequate information and monitoring, and collective adoption mechanisms.
