## 1) Design & Data

- The study used an integrative experiment varying 14 design parameters across 360 experimental conditions (147,618 decisions from 7,100 participants): 320 “learning” conditions (one trial each for maximum breadth), and 40 “validation” conditions (8–12 replications for precision) in two data collection waves. Each condition had a punishment-enabled (“treatment”) game and a punishment-disabled (“control”) game, identical except for the punishment feature.
- Parameters included group size, game length, contribution type (variable or all-or-nothing), framing (opt-in/out), marginal per capita return (MPCR), communication, peer outcome visibility, actor anonymity, horizon knowledge, punishment/reward availability, costs/technology for punishment/reward, etc.
- Experiments were run with consistent protocols, interfaces, and recruitment to minimize hidden confounds.
- Prediction models were trained on the learning data using PGG parameters and the control condition efficiency to predict treatment (punishment-enabled) efficiency, then tested on validation conditions; comparison was made to the performance of human forecasters (experts and laypeople).

## 2) Efficiency Definition

- **Efficiency** is defined as the ratio of the group’s total payoff to the total payoff under full cooperation (every player contributes their entire endowment every round).  
- Efficiency = 1 implies full cooperation/welfare; lower values reflect inefficiency, either due to non-cooperation or costs of punishment.
- The prediction task uses *regular* efficiency (net earnings scaled by the full cooperation baseline), not normalized efficiency (which is used for some cross-configuration comparisons in the paper).

## 3) Main Findings on Punishment

- **Punishment did not universally improve efficiency:** On average, punishment increased contributions, but did *not* consistently increase overall group efficiency. The average effect of punishment was slightly negative: a decrease in normalized efficiency by 6–11% on average, but with significant variability depending on the parameters—effects ranged from a 43% improvement to a 44% reduction in efficiency across different conditions.
- Notably, punishment technology (the magnitude/cost ratio) mattered less than expected for prediction accuracy; context (communication, framing, interactions) was far more important.
- Predictive models (especially elastic net with interactions) outperformed all human forecasters, with model R² = 0.53 on held-out data compared to near-zero for experts/laypeople.

## 4) Heterogeneity / Moderators

- Strong and systematic heterogeneity in punishment effects was observed. Some configurations saw large efficiency gains, others saw large losses.
- **Most influential moderators (by importance for prediction):**
  - Communication (most important; increased prediction error by 60% when shuffled; always increased punishment’s effectiveness).
  - Contribution framing (opt-in vs. opt-out; 2nd most important; opt-out improved efficiency only with *variable* contribution, but *reduced* it with all-or-nothing).
  - Game length (long games enhanced punishment’s effectiveness only if communication was allowed, especially when peer outcomes were not visible).
  - Peer outcome visibility (moderated framing and game length effects).
  - Availability of rewards (always helped, but less influential than the above).
  - MPCR (higher values slightly increased effectiveness, but effect was small).
- Many parameter effects were contingent on the settings of others—e.g., effect of framing depended on contribution type and outcome visibility.

## 5) Notes for Prediction

- Accurate prediction requires accounting for interactions among parameters, especially the context in which punishment operates rather than mechanistic punishment details.
- Including the efficiency of the control (no-punishment) game as an input boosts predictive accuracy.
- Communication, contribution framing, contribution type, game length, and outcome visibility are especially critical moderators; their interactions should be carefully modeled for highest prediction gain.
- Single-factor generalizations (e.g., “punishment works” or “fails”) are not reliable—the effects are highly context-dependent.
- Human predictions fail to capture the complexity of these interactions—mechanistic models trained on broad parameter sweeps generalize better to new scenarios.
