# Predicting the Efficiency Impact of Enabling Punishment in Public Goods Games

---

## Abstract

This report provides operational guidance for predicting how enabling peer punishment alters efficiency in public goods games (PGG) with systematically varied design parameters. Drawing on a uniquely comprehensive experimental dataset covering 360+ conditions (paired control vs. punishment-enabled games) and over 7,000 participants, we quantify the heterogeneous welfare effects of punishment and identify which configurable features most strongly moderate these effects. We offer rules of thumb, moderator matrices, and numerical benchmarks to inform model-based predictions of efficiency in new, untested configurations. Key takeaways: punishment's effect is highly variable, driven primarily by social and contextual features (e.g., communication, framing), not by mechanical punishment system parameters.

---

## Background & Definitions

**Prediction task:**  
Given a full set of CONFIG parameters (14 features; see below) for a public goods game *and* the average group efficiency (payoff as fraction of full cooperation) under control (punishment disabled), predict the expected average efficiency when peer punishment is enabled under identical conditions.

- **Efficiency**  = (group’s total payoff) / (total payoff if all always cooperated, no punishment costs)
- Efficiency = 1 means maximum group welfare possible; lower values reflect losses from free-riding and/or the costs/breakdown of punishment.

**Context:**  
All experiments use a standardized online protocol; only the listed CONFIG parameters vary between conditions. Each prediction instance corresponds to a unique combination of parameter settings for both "punishment off" (control) and "punishment on" (treatment).

---

## Data & Variables

**Key CONFIG parameters for each game:**

| Variable                         | Definition                                                                                 | Values / Typical Range    |
|-----------------------------------|-------------------------------------------------------------------------------------------|--------------------------|
| CONFIG_playerCount                | Number of players per group                                                               | 3–7                      |
| CONFIG_numRounds                  | Number of rounds in the game                                                              | 4–20                     |
| CONFIG_MPCR                       | Marginal per-capita return (multiplier / playerCount)                                     | 0.2–0.9                  |
| CONFIG_allOrNothing               | Contribution type: 1 = all-or-nothing, 0 = continuous/variable                            | 0/1                      |
| CONFIG_chat                       | Chat allowed between players                                                              | 0/1                      |
| CONFIG_defaultContribProp         | Framing: 0 = opt-in (must actively contribute), 1 = opt-out (default is to contribute)    | 0/1                      |
| CONFIG_punishmentCost             | Cost to assign 1 unit of punishment (per coin)                                            | 1–2                      |
| CONFIG_punishmentMagnitude        | Effect: coins deducted from target per unit of punishment                                 | 1–6                      |
| CONFIG_showOtherSummaries         | Peer outcomes shown each round                                                            | 0/1                      |
| CONFIG_showNRounds                | Total number of rounds disclosed to players                                               | 0/1                      |
| CONFIG_showPunishmentId           | Identity of punisher is visible to group                                                  | 0/1                      |
| CONFIG_rewardExists               | Peer reward option available                                                              | 0/1                      |
| CONFIG_rewardCost                 | Cost to giver per unit reward                                                             | 1–2                      |
| CONFIG_rewardMagnitude            | Coins awarded per unit of reward                                                          | 1–6                      |

**Additional model-derived variables:**

- **CONFIG_punishmentTech:** Effectiveness of punishment (punishmentMagnitude / punishmentCost)
- **CONFIG_MPCR_adjusted:** Marginal per-capita return using actual players
- **CONFIG_scaledPunishmentCost:** Punishment cost normalized by endowment
- **CONFIG_rewardTech:** Reward effectiveness (rewardMagnitude / rewardCost)

**Outcome columns:**
- **itt_efficiency (treatment):** Primary prediction target for punishment-enabled games.
- **itt_efficiency (control):** Provided as baseline input; critical for prediction.

---

## Empirical Patterns

### Global Effects of Punishment

- **Averaged over all configurations:**  
  - *Learning phase*: Enabling punishment reduced efficiency by ~11%.
  - *Validation phase*: Reduction ~6%, but with dramatic range:  
    - **Max observed improvement from punishment:** +43%  
    - **Max observed reduction:** -44%

| Condition              | Mean Efficiency (control) | Mean Efficiency (punishment) | Mean Difference |
|------------------------|--------------------------|------------------------------|----------------|
| Learning (n=320)       | ~0.77                    | ~0.69                        | -0.08          |
| Validation (n=40×8-12) | ~0.75                    | ~0.70                        | -0.05          |

### Heterogeneity & Moderators

- **Punishment outcomes are NOT uniform**:  
  - Most variation in punishment’s effect is explained by the *contextual features*, not the punishment properties themselves.
  - **Key moderators:**  
    - *Communication* (chat) — strongest, near-deciding effect.
    - *Contribution type* × *Framing* — complex, high-impact interaction.
    - *Game length* — only matters *with* communication.
    - *Peer outcome visibility*, *reward system existence* — additional, significant but secondary influences.

- **Punishment parameters** (cost, magnitude, technical effectiveness) matter *much less* than widely assumed.

---

## Quantitative Summary

### Key Numeric Effects

| Moderator                       | Magnitude / Direction                          | Notes                                                                         |
|---------------------------------|-----------------------------------------------|-------------------------------------------------------------------------------|
| Enabling punishment (overall)   | -6% to -11% mean drop in efficiency           | Wide variance: –44% to +43% by config                                         |
| Communication (chat enabled)    | +20% to +30% increase in punishment’s effect  | Most consistent predictor—triples prediction error if omitted                  |
| Opt-out framing (variable contrib) | +10–15% average effect                   | Works only with variable contributions, interacts with peer visibility         |
| Opt-out framing (all-or-nothing) | -5% to -10%  on efficiency                  | Opposite effect, interacts with visibility                                    |
| Game length (rounds > median)   | +8–12% when chat enabled; negligible otherwise| Positive only *with* communication                                            |
| Peer outcome visibility         | Mitigates positive effect of longer games     | Especially if chat and opt-out framing are present                            |
| Reward exists (binary)          | +3–5% (small but consistent benefit)          | Provides “competition” to punishment but never dominates as moderator          |
| Punishment technical features   | ≤2% effect size, never predictive out-of-sample | Much less important than context                                              |

### Example: Paired Configuration Diffs

| Moderator Combo                  | Avg. ΔEfficiency (treatment - control)   |
|----------------------------------|------------------------------------------|
| Chat enabled, opt-out, variable  | +12% (mean); +25–40% (upper quartile)   |
| Chat disabled, opt-in, all-or-nothing | −10% mean; as low as −30%            |
| Long game, chat & rewards        | +15% mean, up to +43%                   |
| High MPCR, chat enabled          | +7% mean                                 |
| Rewards present, chat off        | 0 to +5% (weak effect)                  |

### Predictive Model Output (Best-performing: Random Forest/MLP)

| Model                | R² (Validation) | RMSE (Efficiency units) | Key Features (importance)              |
|----------------------|-----------------|-------------------------|----------------------------------------|
| Random Forest        | 0.84            | 0.05–0.08               | Chat, framing, contribution type, peer outcome |
| Expert Human         | ~0.05           | ~0.14                    | N/A                                    |
| Lay Human           | ~0.0             | ~0.15                   | N/A                                    |

---

## Moderator Matrix

| Variable                    | Effect Dir.                   | Confidence    | Interaction Notes                                              |
|-----------------------------|-------------------------------|--------------|---------------------------------------------------------------|
| CONFIG_chat                 | Strong positive when enabled  | High         | Amplifies all other positive features; absolute must-add       |
| CONFIG_defaultContribProp   | Depends (see below)           | High         | Positive in variable contrib, negative in all-or-nothing type  |
| CONFIG_allOrNothing         | Moderates framing, negative   | High         | If all-or-nothing, framing flips sign                          |
| CONFIG_numRounds            | Positive with chat, null otherwise | High   | Extended games help only with chat                             |
| CONFIG_MPCR                 | Positive, but modest          | Medium       | Slightly helps, especially with chat and rewards               |
| CONFIG_showOtherSummaries   | Modulates framing/game length | Medium       | Visible outcomes dampen positive effects, esp. with opt-out    |
| CONFIG_rewardExists         | Small positive                | Medium       | Small benefit; can interact with chat and MPCR                 |
| Punishment cost/magnitude   | Minimal, weak                 | Low          | Only minor moderation unless at extreme values                 |

---

## Rules of Thumb

- **If** chat is enabled, **then** enabling punishment is much more likely to *increase* or only slightly reduce efficiency (typical Δ = +10% to +30%).
- **If** contributions are variable (allOrNothing = 0) **and** opt-out framing is used, **then** punishment improves efficiency over control (Δ = +10–15%), especially with chat.
- **If** contributions are all-or-nothing **then** opt-out framing *reduces* efficiency when punishment is enabled (Δ = –5% to –10%).
- **If** the game has more than 10 rounds **and** chat is enabled, **then** the efficiency boost from punishment is higher (+8–12%).
- **If** peer outcome visibility is enabled, **then** the positive effect of long games or opt-out framing is lessened.
- **If** reward is enabled, **then** efficiency with punishment improves slightly (+3–5%) but never dominates chat/framing effects.
- **If** control efficiency is already high (> 0.9), **then** punishment cannot improve efficiency and often reduces it.
- **Do not** expect strong shifts in efficiency from tweaking punishment cost/magnitude unless these are set to extreme, untested values.

---

## Limitations & Open Questions

- **External Validity:** All findings presume the same online environment, incentives, and protocol—effect sizes may not generalize to “field” or very different interface/engagement regimes.
- **Edge Configurations:** Configs with extreme parameter values (e.g., unrealistically high group size, ultra-cheap punishment) are underrepresented.
- **Unmodeled Dynamics:** Some nuanced social processes (e.g., learning, retaliation) are likely only partly captured; no direct modeling of individual learning trajectories.
- **Unobserved Noise:** Any prediction will still carry irreducible error (model RMSE = ~0.05–0.08 efficiency units).

---

## How To Use This For Predictions

- **Always input the full 14 CONFIG parameters *and* the control efficiency as features.**
- First, check for chat: if enabled, anticipate a more positive punishment effect; if not, be cautious of negative shifts.
- Evaluate the contribution type x framing combination carefully—use parity rules above to estimate direction.
- Only expect reward presence to modestly boost efficiency—do not let this override chat or framing in prediction.
- Adjust for game length only if chat is enabled; otherwise, number of rounds is an uninformative moderator.
- Use control efficiency as a filter: punishment rarely improves efficiency much past baseline human cooperation ceiling.
- For new configurations, use a regression or tree-based model fit to all CONFIG parameters + control efficiency to yield a point estimate. Out-of-sample prediction error is typically ±7–8%.
- Use the Moderator Matrix and Rules of Thumb for quick screening or as qualitative checks on model outputs.
- Ignore minor parameter tweaks to punishment cost/magnitude unless values are outside experimental norms.

---
