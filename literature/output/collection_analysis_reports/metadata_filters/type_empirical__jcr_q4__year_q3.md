# 1) Evidence Base

This literature set consists of 10 laboratory experimental papers, with a strong empirical character—no theory or simulation papers are included. The papers primarily study variations on public goods games (PGGs), collective action dilemmas, and related games involving punishment, sanctioning, or feedback mechanisms. The set is broad in that it covers several institutional mechanisms (peer punishment, centralized punishment, social feedback, exclusion, endogenous grouping, redistribution, etc.) and a range of public goods and closely related games, but is narrower in its exclusive reliance on lab-based human subject experiments.

## Breadth and Empirical Focus
- The majority directly study standard PGGs or close variants, but some include generalized exchange, common-pool resource (CPR) games, and asymmetric surplus allocation.
- Most provide direct empirical outcome data, especially on group earnings, efficiency, or closely related payoffs, but several focus only on behavioral outcomes (e.g., punishment frequency, cooperation rates).
- Several papers describe the tested game design dimensions in detail (e.g., group size, number of rounds, MPCR, punishment parameters), while others offer only minimal contextual detail.

# 2) Task Relevance

The prediction task requires literature that is:
- (A) On PGG or closely analogous multiplayer social dilemmas (`pgg_or_variant`)
- (B) Explicitly manipulates peer punishment or sanctions (`punishment_or_sanctions`)
- (C) Empirically measures efficiency or group payoff outcomes (`efficiency_or_related_payoff_outcome`)

### Dimension-by-Dimension Relevance

| Paper set focus          | `pgg_or_variant` | `punishment_or_sanctions` | `efficiency_or_related_payoff_outcome` |
|-------------------------|:----------------:|:-------------------------:|:--------------------------------------:|
| Direct, lab PGGs with peer/centralized punishment and payoff data (e.g., Suleiman & Samid, Castillo et al., Kanitsar) | exact | exact | exact/mixed |
| Close variants or institutional modifications (e.g., social feedback, redistribution) | close | adjacent to exact (some peer, some institutional) | adjacent to exact (some only behavioral, some efficiency/payoff) |
| Indirect studies (e.g., focus on cooperation rates, punishment as trait, exclusion mechanisms) | close/adjacent | adjacent/weak | adjacent/none |

**Summary of relevance:**
- Several papers are *exactly relevant* (Suleiman & Samid, Castillo et al., Kanitsar): standard PGGs, with enabled/disabled punishment conditions, and efficiency or group payoff as primary outcomes.
- Others are *close* or *adjacent* (e.g., studies using centralized sanctions, redistribution, exogenous matching, feedback in CPR games): valuable for understanding mechanisms but less directly tied to PGG prediction with peer punishment.
- Some are only *weakly* relevant on the payoff dimension, focusing on behavioral outcomes rather than efficiency or group payoffs (Windmann et al., Selterman, Grund et al., Becchetti et al.).
- No papers are fully irrelevant ("none") on all three target dimensions, but some lack direct data for efficiency-related prediction.

# 3) Outcomes Measured In The Literature

Most studies distinguish (or can be interpreted as distinguishing) between tangible, payoff-based outcomes (group efficiency, total earnings, welfare, surplus, coins generated) and non-payoff behavioral outcomes (contribution rate, cooperation frequency, punishment frequency, attitudes).

### Payoff-Related Outcomes
- **Directly Measured Efficiency/Payoff:**  
  - Suleiman & Samid (2021), Castillo et al. (2021), Kanitsar (2021), Nax et al. (2018), Di Guida et al. (2021), Przepiorka & Diekmann (2020)
- **Indirect or Implied Efficiency Gains:**  
  - Becchetti et al. (2018), Selterman (2019) (implied from increased cooperation & likelihood of group success)
- **Absent/Not Measured:**  
  - Windmann et al. (2021), Grund et al. (2020) (focus only on behavioral metrics)

### Non-Payoff Behavioral Outcomes
- Many studies (Windmann et al., Grund et al., Becchetti et al., Selterman) mainly report on cooperation and punishment behaviors, attitudes, or trait measures, with efficiency inferred at best.

**Explicit reporting of efficiency (as group payoff compared to social optimum) is present in about half the papers and missing in the remainder.**

# 4) Main Findings Relevant To Prediction

Synthesizing the findings across the literature, with attention to prediction of average treatment efficiency:

### Empirical Evidence (Efficiency or Payoff Outcomes)
- **Enabling punishment generally increases group efficiency and contributions relative to no-punishment controls in standard PGGs**, but the effect size is modest to moderate and highly variable by group and social context. Effectiveness is highest where groups have more strong reciprocators and fewer norm-keepers; antisocial punishment is rare but norm-keeping (punishing both high and low contributors) reduces efficiency (Suleiman & Samid, 2021).
- **Centralized punishment institutions (manager enforces punishment)** robustly elevate efficiency and contributions; details of manager selection (vote vs. random) don't matter, and varying the punishment cost/effectiveness within typical ranges does not affect the positive impact of enabling punishment in these settings (Castillo et al., 2021).
- **Peer punishment is only efficiency-enhancing in standard PGG structures if the punishment is costless or very cheap**; with higher costs, efficiency gains disappear (Kanitsar, 2021). In sparse or generalized exchange structures, punishment fails to increase efficiency, regardless of cost.
- **Alternative or adjacent mechanisms (redistribution, exclusion, feedback):**
    - Sorting/grouping based on merit (Nax et al., 2018), institutional redistribution (Becchetti et al., 2018), and non-monetary public feedback (Przepiorka & Diekmann, 2020) can all increase efficiency or cooperation, sometimes even without punishment per se.
    - Peer exclusion (Grund et al., 2020), and refusal to cooperate ("soft" punishment) can yield modest, often temporary, efficiency or payoff gains (Di Guida et al., 2021).
    - All-or-nothing or threshold games with punishment show improved group success rates (binary), not always continuous efficiency measures (Selterman, 2019).

### Theory/Mechanism Insights
- **Anticipation of punishment can motivate higher contributions even when actual punishment is rare (Suleiman & Samid, 2021).**
- **Density of the sanctioning network and nature of group structure are critical moderators:** Peer punishment's efficiency gains are specific to dense (standard PGG) networks and do not generalize to all multi-agent cooperation contexts (Kanitsar, 2021).
- **Cost-to-impact ratio for punishment is important,** but only in standard (not sparse) sanctioning networks (Kanitsar, 2021).

### Disagreement/Ambiguity
- Some studies show *heterogeneity in treatment effects*—group composition affects whether the efficiency impact is large, small, or negligible (Suleiman & Samid, 2021; Di Guida et al., 2021).
- Costs and effect sizes are context-dependent: in some centralized settings, cost changes don't moderate the effect; in peer settings, they do.

# 5) Prediction Guidance

Based on the synthesized literature, the following broad guidance is supported for predicting average treatment efficiency from game design dimensions and control efficiency:

- **Enabling peer or centralized punishment in standard (dense) PGGs should be expected to increase group efficiency relative to a control with punishment disabled,** but the magnitude is sensitive to:
  - **Punishment cost:** Only low or zero-cost punishment robustly improves efficiency for peer punishment; higher costs may negate gains.
  - **Game structure:** Effects are robust in standard PGGs but may not generalize to games with sparse or generalized exchange structures.
  - **Group composition and social context:** The prevalence of strong reciprocators enhances punishment's positive effect; norm-keepers can undermine it.
  - **Type of punishment institution:** Centralized punishment works well independently of the manager's selection mechanism; peer punishment is more variable.
  - **Other design factors (e.g., chat, information feedback, all-or-nothing contribution structure) are less strongly implicated by the current paper set.**

- **Control efficiency (the baseline, punishment-off condition) is an important predictor,** but the effect size of enabling punishment is not uniform: anticipate variability by context.
- **Mechanisms akin to punishment (redistribution, group exclusion, public feedback) can sometimes produce similar efficiency effects**; however, prediction should only generalize these results with caution.

**In sum:**  
Prediction models should expect a treatment efficiency boost from enabling punishment under standard PGG parameters, *modulated* by punishment cost/effectiveness, group structure, and possibly group heterogeneity. Where game dimensions or institutional environments depart from standard peer PGGs, especially regarding punishment network density or cost, the direction and magnitude of efficiency change may not follow the peer punishment "default." Control efficiency remains an important but non-exhaustive baseline.

# 6) Design Dimensions Highlighted Across Papers

Based on explicit discussion and empirical coverage in the paper set:

#### Directly Informed Dimensions
- `player_count`: Regularly specified and manipulated (esp. 4, 5, 10, 16)
- `num_rounds`: Commonly reported
- `mpcr`: Almost always specified
- `punishment_cost`: Explicitly manipulated and highly consequential for efficiency
- `all_or_nothing`: Some studies manipulate or fix (continuous vs. discrete contributions)
- `chat`: Sometimes included as an experimental condition
- `punishment_tech`: Sometimes described (peer vs. centralized, cost-to-impact ratio)
  
#### Indirectly Informed/Contextual
- `show_n_rounds`: Sometimes indicated (whether subjects know rounds)
- `show_other_summaries`: Related to information feedback/visibility of actions
- `show_punishment_id`: Salient in papers addressing public vs. private feedback/social sanctions
- `reward_exists`, `reward_cost`, `reward_tech`: Only discussed in the redistribution or feedback contexts
- `reward_cost`, `reward_tech`: Coverage is sparse and limited to adjacent mechanisms

#### Sparse/Missing
- `default_contrib`: Framing not a focus
- `reward_exists`, `reward_cost`, `reward_tech`: Not directly studied as main treatments
- Some potentially relevant design features (e.g., magnitude of punishment or reward, noise/uncertainty in payoffs) are only rarely touched upon.

**Key moderator for efficiency prediction:** `punishment_cost` (cost-to-impact ratio) is repeatedly shown to be crucial—direct evidence links low cost to positive efficiency effects, and high cost to muted or absent effects.

# 7) Important Limitations

**Scope and Generalizability**
- **Most findings are specific to laboratory settings** with standard group sizes and repeated, linear PGGs. Extension to field or large-scale online settings is uncertain.
- **Only a handful of papers report efficiency (payoff) outcomes directly.** Many report only behavioral data, requiring indirect inference about efficiency effects.
- **Peer punishment effectiveness is highly contingent**: findings underscore the mediating role of group composition and social context, but such factors are rarely measured or controlled outside laboratory environments.
- **Sparse coverage of several design dimensions**: Behavioral framing, information feedback, and reward structures are under-studied or only indirectly addressed.
- **Ambiguity in magnitude estimates:** While qualitative effect directions are consistent, precise effect sizes or adjustment formulas for efficiency boost from punishment are not provided.
- **Game structure and institution type matter:** Efficiency effects found for centralized or redistribution mechanisms may not generalize to peer punishment, and vice versa.
- **Non-payoff outcomes:** Where only behavioral outcomes are measured, conclusions about efficiency gain are speculative.

**Conclusion:**  
This paper set provides a strong empirical basis for predicting that enabling peer or centralized punishment in standard PGGs will usually (not always) increase group efficiency above the control, with effect size moderated primarily by punishment cost, group structure, and composition. However, limitations in direct efficiency measurement, design dimension coverage, and generalizability must temper prediction certainty, especially outside standard laboratory PGG settings.
