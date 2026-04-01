# 1) Evidence Base

The evidence base consists of two recent empirical lab experiments: one focusing on costly punishment dynamics influenced by emotional state in ultimatum and third-party punishment games (Gummerum et al., 2022), and one examining efficiency outcomes in an intergroup centipede game with emotional communication (Nunney et al., 2022). Both papers use controlled lab experiments, yielding direct behavioral data. The set is narrow for the downstream prediction task, as neither study produces efficiency outcomes in public goods games (PGGs) with formal peer punishment, nor do they manipulate all key design dimensions relevant to that context.

# 2) Task Relevance

- **pgg_or_variant**:  
  - **Gummerum et al. (2022)**: Adjacent. Uses ultimatum and third-party punishment games. These feature costly punishment over fairness norms but do not capture the simultaneous, multi-party cooperation and free-rider dynamics central to PGGs.
  - **Nunney et al. (2022)**: Adjacent. Uses a repeated intergroup centipede game. This is a sequential social dilemma with group payoffs and a costly punishment component, with some overlap but not identity with the PGG structure.

- **punishment_or_sanctions**:  
  - **Gummerum et al. (2022)**: Exact. Costly punishment is the primary focus, though not in a PGG setting.
  - **Nunney et al. (2022)**: Adjacent. Studies both costly punishment and alternative norm enforcement (social emotion expressions), but punishment is not implemented as a peer-sanctioning stage typical of PGGs.

- **efficiency_or_related_payoff_outcome**:  
  - **Gummerum et al. (2022)**: Adjacent. Only behavioral outcomes (punishment rates, severity); does not report efficiency, total group payoff, or welfare.
  - **Nunney et al. (2022)**: Exact. Reports efficiency (group payoffs/tickets won) as primary outcomes.

**Summary**: The paper set provides adjacent but not direct evidence for efficiency outcomes resulting from peer punishment in PGGs. Emotional and communicative moderators are emphasized, but the specific PGG context with formal punishment is missing.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes**:
  - **Nunney et al. (2022)**: Directly measures group payoffs and efficiency levels (tickets won).
- **Non-payoff behavioral outcomes**:
  - **Gummerum et al. (2022)**: Measures punishment enactment rates, severity, and their emotional/developmental correlates; does not address total group payoff, efficiency, or surplus.
  - **Nunney et al. (2022)**: Also tracks cooperation rates, costly punishment actions, and communication content (emotional expressions), distinguishing these from efficiency.

**Distinction**: Only one study uses payoff-based outcomes as the main dependent variable, and neither does so in a PGG.

# 4) Main Findings Relevant To Prediction

- **Punishment and Emotion**:  
  Gummerum et al. (2022) show that incidental anger increases costly punishment of unfair actions in both second- and third-party settings (with developmental moderation). However, there is no measured effect on group efficiency or payoff and no PGG context. This suggests higher punishment frequency/severity under some conditions, but without clear implications for efficiency.

- **Communication, Emotion, and Group Efficiency**:  
  Nunney et al. (2022) demonstrate that group expressions of shame or guilt following uncooperative behavior lead to higher subsequent group efficiency (payoff) in repeated games, while pride expressions result in greater punishment and lower efficiency. These effects hold even without formal peer punishment, suggesting that communication and emotion are potent moderators of behavioral responses to norm violations, affecting eventual payoffs.

- **Punishment Mechanisms**:  
  Neither study manipulates or isolates the causal efficiency effect of enabling or disabling peer punishment in a standard PGG framework.

- **Game Structure**:  
  Both studies use multi-round, multi-player social dilemmas but not classical PGGs; only Nunney et al. (2022) analyzes efficiency.

# 5) Prediction Guidance

Given the evidence, direct quantitative prediction of efficiency uplift (or drop) from enabling peer punishment in a PGG, conditional on control efficiency and design dimensions, is not possible. However, some qualitative guidance can be inferred:

- The motivation for costly punishment is sensitive to emotional states (anger), self-relevance, and developmental stages—but changes in punishment propensity do not always translate to changes in aggregate payoffs or efficiency unless linked to cooperation dynamics (Gummerum et al., 2022).
- Communication channels (chat, emotion expressions) can meaningfully alter efficiency outcomes in repeated social dilemmas, sometimes substituting for or modulating the need for formal punishment (Nunney et al., 2022).
- In settings that allow communication, non-punitive responses (guilt/shame) may raise efficiency, while pride or escalation in punishment may reduce it. However, these effects are demonstrated outside a classic PGG with formal peer sanctioning.

Thus, when designing or predicting efficiency in a PGG-like game with punishment enabled:
- Expect the influence of emotional or expressive factors—especially if chat channels or visible emotion cues are present.
- Direct efficiency gains from enabling punishment are not confirmed by these studies; effects are context-dependent, with communication potentially substituting for punishment’s normative function.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed**:
- `player_count`: Both studies vary or specify player group size.
- `num_rounds`: Both use multi-round designs.
- `punishment_cost`: Both manipulate or specify cost characteristics for punishment in their respective games.
- `punishment_tech`: Mechanisms for enabling punishment are central.
- `chat`: Nunney et al. (2022) include communication/emotion expression; Gummerum et al. (2022) does not, but their findings are relevant to communication environments.
- `show_n_rounds`: Mentioned in Nunney et al. (2022).

**Indirectly or Contextually Discussed**:
- `all_or_nothing`: Gummerum et al. (2022) incorporates a binary (“accept or reject”) dynamic, which may be analogous.
- `show_other_summaries`: Implicit in reporting group outcomes or available information, but not experimentally varied.
- `show_punishment_id`: Not discussed or manipulated.

**Effectively Missing**:
- `default_contrib`, `mpcr`, `reward_exists`, `reward_cost`, `reward_tech`, `show_other_summaries`, `show_punishment_id`: These critical dimensions for PGG outcome prediction are not addressed in the studies.

# 7) Important Limitations

- No study directly implements or isolates the peer punishment effect on efficiency in a standard PGG. Both use adjacent paradigms, limiting internal validity for predicting efficiency in PGGs.
- Only one study (Nunney et al., 2022) measures efficiency, and it does so in a sequential social dilemma with unique communicative and emotional features, not through punishment enablement per se.
- The effect of punishment on behavioral outcomes does not necessarily translate to effects on total group payoff or efficiency (Gummerum et al., 2022).
- Key prediction-relevant design dimensions (MPCR, default contribution framing, explicit reward mechanisms, visibility settings) are not systematically manipulated or even addressed.
- Emotional and communicative moderators, while seemingly influential on both punishment and efficiency, may operate differently in formal PGGs versus the settings studied.
- Results may not extrapolate to standard PGG environments, especially where communication, group identity, and emotional expression are restricted or absent.

**Summary**: The literature set is narrow and only adjacent or partial for the prediction task. It highlights mechanisms by which emotion and communication impact punishment and efficiency-related outcomes, but does not provide a direct empirical basis for predicting the payoff impact of enabling peer punishment in PGGs as a function of detailed game design dimensions.
