# 1) Evidence Base

The paper set consists of three papers: one experimental study (Carpenter et al., 2012), and two theory papers (Okada, 2020; Kraines & Kraines, 1993). The Carpenter et al. paper provides direct empirical evidence from public goods games (PGGs) with punishment, targeting efficiency and related payoff outcomes under various controlled manipulations. The Okada paper is a broad theoretical review situated in the literature of indirect reciprocity but not focused on public goods per se, while the Kraines & Kraines paper presents simulation-based theory for iterated dyadic dilemmas, not groups or punishment-enabled PGGs. Taken together, the evidence base is relatively narrow for the specific task of forecasting efficiency effects of peer punishment in PGGs: only one paper offers direct, experimental results; the others provide mechanism-level context from adjacent domains.

# 2) Task Relevance

**pgg_or_variant**
- Carpenter et al. (2012): `exact` — Studies classic PGGs with lab manipulations.
- Okada (2020): `adjacent` — Focus is theoretical models of indirect reciprocity, structurally adjacent but not PGGs.
- Kraines & Kraines (1993): `adjacent` — Focuses on iterated Prisoner’s Dilemma, a two-player social dilemma, not multi-player or public goods.

**punishment_or_sanctions**
- Carpenter et al. (2012): `exact` — Explicit, experiment-level manipulations of costly peer punishment.
- Okada (2020): `close` — Discusses punishment in reputation and reciprocity contexts, but not operationalized in PGGs.
- Kraines & Kraines (1993): `adjacent` — Punishment conceptualized via negative payoffs in adaptive strategies, not explicit peer punishment.

**efficiency_or_related_payoff_outcome**
- Carpenter et al. (2012): `exact` — Directly measures group efficiency and related payoffs.
- Okada (2020): `adjacent` — Focuses on behavioral stability and cooperation, not group payoffs or efficiency.
- Kraines & Kraines (1993): `exact` — Simulated average payoffs, but in dyadic games, not group efficiency.

In summary, only Carpenter et al. (2012) achieves exact relevance across all dimensions. The remaining papers are at best adjacent or close, offering supporting mechanism arguments but not direct predictive evidence for PGGs with peer punishment and measurable efficiency.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes**
    - Carpenter et al. (2012): Measures group efficiency (payoff as a proportion of theoretical maximum), total group earnings, and how these change with punishment enabled versus disabled.
    - Kraines & Kraines (1993): Reports average payoffs achieved by dyadic strategies in iterated dilemmas, analogous to efficiency for two players, but not within a PGG or group setting.
    - Okada (2020): Does *not* report or analyze efficiency, payoff, or group welfare; focus is on theoretical stability of cooperation via norms.

- **Non-payoff behavioral outcomes**
    - Carpenter et al. (2012): Also measures contributions, frequency/intensity of punishment, network interactions; these are used as mechanisms but not confused with efficiency per se.
    - Okada (2020): Discusses cooperation rates, norm compliance, assessment functions, error tolerance, and stability of behavioral strategies.
    - Kraines & Kraines (1993): Concentrates on strategy adaptation, recovery from error, behavioral responsiveness.

Most relevant for downstream prediction are the objectively measured efficiency and group payoff outcomes in Carpenter et al. (2012). Theoretical or adjacent results elsewhere leverage non-payoff mechanisms or interpret efficiency only in analogous, not directly transferable, settings.

# 4) Main Findings Relevant To Prediction

Synthesizing across the three papers:
- **From empirical evidence (Carpenter et al., 2012):**
    - The net effect of enabling peer punishment on group efficiency is *contingent* on the underlying network structure. Punishment reliably increases contribution levels across settings, but whether this translates to improved efficiency depends on how punishment costs accumulate in the group.
    - Complete or highly connected networks allow for higher efficiency because punishment expenditures are minimized: only rare, targeted punishment is needed to deter free-riding, so group payoffs improve.
    - Disconnected or directed networks result in *more frequent and severe punishment*, with higher cumulative costs. Here, efficiency can fall below the no-punishment baseline, even if cooperation rates rise, due to costly sanctioning cycles.
    - The marginal benefit from increasing monitoring links is non-linear: moving from low to moderate connectivity boosts efficiency, but excess links in already dense networks can promote over-punishment and suppress efficiency.

- **From adjacent theory:**
    - Okada (2020) shows that punishment, especially when structured through norms and reputation, stabilizes cooperation in repeated-dilemma models, but public goods settings (where all benefit from one’s action) cannot directly apply selective reciprocity mechanisms.
    - Kraines & Kraines (1993) finds that adaptive “Pavlov” learning strategies achieve high dyadic payoffs and resilience to noise, but environments, strategies, and payoff structures differ from group-based PGG dynamics. No direct inference to group efficiency with punishment is supported.

Thus, the **single most robust prediction** is that efficiency impacts of punishment in PGGs are *not uniform*: in some game architectures, enabling punishment “works” (efficiency↑), in others, it does not or can even backfire (efficiency↓), depending almost entirely on the punishment network’s structure, not simply the existence or cost parameters of punishment.

# 5) Prediction Guidance

The empirical record (Carpenter et al., 2012) implies that using only average efficiency in the control game (punishment disabled) and game design dimensions is insufficient to determine the efficiency effect of enabling peer punishment. Instead:

- Consider **network architecture** (who punishes whom): Complete or highly connected networks predict positive gains from enabling punishment, notably when punishment costs, all other parameters, and MPCR are held constant.
- In sparse, directed, or disconnected networks, enabling punishment increases costly sanctioning cycles, suppressing efficiency relative to the control.
- Other dimensions (e.g., player count, MPCR, punishment cost) were held fixed, so their independent or interactive effects remain undetermined in this set.
- No paper indicates that enabling punishment is uniformly beneficial for efficiency; context and structure are decisive.
- Adjacent theory supports that norm-based and learning-based dynamics are important, but cannot be directly mapped to efficiency outcomes in group PGGs.

Thus, **predictions should be moderated by the network context**: Do not overestimate, or assume universal, efficiency improvement from enabling punishment.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed (manipulated or analyzed empirically, affecting efficiency with punishment):**
- `player_count` (all: 4; constant in empirical, discussed in theory)
- `num_rounds` (all: 15; constant in empirical, parameter in theory)
- `mpcr` (constant in empirical, parameter in theory)
- `punishment_cost` (explicitly manipulated in empirical; considered in theory)
- **Additional, critical dimension in empirical:** *network architecture* (not listed among the 14 preset prediction dimensions but crucial in Carpenter et al., 2012)

**Indirectly informed (contextually or theoretically discussed but not empirically varied for payoff):**
- `all_or_nothing` (discussed as a framing or structure in theory)
- `chat` (present in empirical design, but not emphasized for payoff outcomes)
- `punishment_tech` (considered in theory, i.e., targeting, norms, but not empirically manipulated for efficiency)
- `show_other_summaries`, `show_n_rounds`, `show_punishment_id` (sometimes noted in protocol/theory, effect on efficiency not analyzed)

**Essentially missing (not discussed or analyzed for their effect on efficiency):**
- `default_contrib` (not discussed)
- `reward_exists`, `reward_cost`, `reward_tech` (not present in the empirical or theoretical designs; some reference to reward mechanisms in the context of norms, but not as experimental levers)
- `show_n_rounds` (only as context, not for efficiency)
  
Thus, the strongest and most direct evidence pertains to network structure (a dimension external to the enumerated 14), and to some extent to player count, rounds, MPCR, and punishment cost (all held constant empirically).

# 7) Important Limitations

- Only one paper (Carpenter et al., 2012) provides directly relevant empirical data; the rest speak only to related mechanisms or adjacent payoff concepts.
- The main experimental findings are limited to a single parameter set for most game dimensions (player count, rounds, MPCR, punishment cost), so generalizability across a broader design space is not empirically established.
- Network architecture, found to be a decisive moderator for treatment efficiency, is not captured within the standard 14 listed game design dimensions—translation from these dimensions to network structure may be ambiguous or missing.
- Adjacent theoretical accounts support and explain the mechanisms by which punishment *could* yield higher efficiency, but do not deliver quantitative or context-sensitive predictions for multi-player PGGs.
- Payoff outcomes in adjacent theory (Kraines & Kraines, 1993) arise from dyadic interactions, not group context, and their direct transfer to PGGs is not justified.
- Several prediction dimensions (reward mechanisms, contribution framing, real-time feedback features) are absent from both manipulation and analysis, leaving major gaps in dimension-level prediction coverage.
- The overall literature base is narrow for prediction: a single, high-relevance empirical study, with two supporting but structurally distinct theoretical papers, limits robustness and coverage for design-driven efficiency forecasting in PGGs with punishment.
