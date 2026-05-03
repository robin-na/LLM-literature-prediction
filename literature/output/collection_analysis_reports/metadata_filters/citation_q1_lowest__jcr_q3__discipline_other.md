# 1) Evidence Base

The paper set consists of 9 studies, featuring a blend of empirical (lab and field experiments) and theory papers:

- **Empirical Studies**: Four are experimental or field-based (Amirova et al.; Herne et al.; Gomez-Ruiz & Sánchez-Expósito; Ferguson; Suzuki & Ishiwata). These address behavioral outcomes, collective investment, or payoff/efficiency, but not all integrate punishment or efficiency as primary variables.
- **Theory Papers**: Five papers are conceptual or theoretical (Wu & Sun; Andrews & Davidson; Suratin et al.; Sthel et al.).
- **Narrowness/Broadness**: The scope is moderately broad regarding mechanisms and settings (public goods, common-pool resources, real-world governance, and even blood/organ donation), but *narrow* for the precise task of predicting efficiency effects of punishment in public-goods-game-like (PGG) environments using explicit game design dimensions. Most studies do not fully align with all three task-relevant aspects (PGG, punishment, efficiency outcome).

# 2) Task Relevance

Assessed on the three key axes:

**a) PGG or Variant**
- Several papers directly use PGG or close analogs (Wu & Sun: exact; Amirova et al.: close; Herne et al.: close; Gomez-Ruiz & Sánchez-Expósito: close).
- Others involve settings adjacent to PGGs (Suzuki & Ishiwata: adjacent with market features; Ferguson: adjacent 3-party context; Sthel et al., Suratin et al., Andrews & Davidson: adjacent or weaker).
- **Label**: *Mix of exact, close, and adjacent relevance; only some are pure PGGs.*

**b) Punishment or Sanctions**
- **Exact**: Wu & Sun, Amirova et al., Ferguson, and Andrews & Davidson directly study or theorize punishment mechanisms in settings close to PGGs.
- **Close/Adjacent**: Suzuki & Ishiwata (taxes as punishment); Suratin et al. (social sanctions discussed conceptually, not implemented); Gomez-Ruiz & Sánchez-Expósito (informal controls only); Herne et al. (no punishment).
- **Label**: *Punishment is a main construct in some studies, adjacent or absent in others; not universal or always empirical.*

**c) Efficiency or Related Payoff Outcome**
- **Exact**: Suzuki & Ishiwata; Herne et al. (but no punishment arm); rest mainly use behavioral proxies (contributions, investments), or only discuss payoff in theory.
- **Close/Adjacent**: Wu & Sun and Amirova et al. use contribution/investment (non-payoff) as proxies for efficiency; Ferguson, Gomez-Ruiz, and others do not report efficiency as the primary outcome.
- **Label**: *Limited exact efficiency outcome studies, more with adjacent or proxy outcomes.*

# 3) Outcomes Measured In The Literature

- **Payoff-Related (Efficiency/Group Payoff)**: 
  - Explicitly reported as efficiency or total payoff in Suzuki & Ishiwata (exact, with a punishment-like treatment) and Herne et al. (exact, but no punishment).
  - Reported as group profit (proxy for efficiency) in Suzuki & Ishiwata.
  - The rest use aggregate contributions or investments as behavioral proxies for efficiency but do not compute efficiency ratios.

- **Non-Payoff Behavioral Outcomes**:
  - Most common. Includes cooperation rate, total/average contributions, collective investment (Amirova et al.), free-riding, and norm compliance.
  - Wu & Sun, Amirova et al., Gomez-Ruiz & Sánchez-Expósito focus on cooperation/investment rates.
  - Ferguson examines individual preference for punishment vs. compensation.

- **Norm Compliance / Informal Mechanisms**:
  - Suratin et al. and Andrews & Davidson address these conceptually, highlighting the importance of social punishment/values, not efficiency per se.

# 4) Main Findings Relevant To Prediction

Synthesizing across the literature, with an explicit focus on empirical payoff-related findings and mechanism arguments:

- **Punishment Generally Increases Cooperation, Often via Behavioral Outcomes**:
  - Multiple theoretical arguments and indicator results (Wu & Sun; Andrews & Davidson; Suratin et al.) suggest that the introduction of punishment mechanisms in PGG-like environments is likely to increase group cooperation or contribution behavior.
  - However, these improvements usually manifest first in *non-payoff behavioral outcomes* (contributions, norm compliance) rather than direct efficiency gains.

- **Efficiency Effects of Punishment Are Context-Dependent and Can Be Negative**:
  - Only a few empirical studies track group payoff or efficiency directly; among those, the effect of punishment is not uniformly positive:
    - **Amirova et al.**: In a field experiment with real-world PGG-like investment, *enabling punishment (penalties) decreased collective investment* relative to baseline due to crowding out intrinsic motivation. This points to a potential *decrease* in efficiency when punishment is enabled, at least in settings prioritizing intrinsic cooperation.
    - **Suzuki & Ishiwata**: In a competitive repeated game, *the introduction of a punishment-like mechanism (carbon tax) increased efficiency (group profit)*, but statistical significance was weak—and only the actual implementation, not mere anticipation, produced effects.
    - **Wu & Sun**: Modeling predicts greater cooperation with monetary compensation for wrongful punishment, but the outcome is measured as contributions, not payoff or efficiency ratios.
  - **No evidence** (empirical or theoretical) that punishment reliably *always* increases efficiency in all PGG settings; mechanisms may depend on context or design specifics.

- **Communication (Chat) Can Also Raise Efficiency**:
  - **Herne et al.**: Communication (structured or unstructured) robustly increases group efficiency, with or without explicit punishment mechanisms.

- **Type of Punishment and Social Mechanisms Matter**:
  - Several theory papers (Suratin et al., Wu & Sun, Ferguson) stress that the effectiveness and payoff impact of punishment depend on whether it is financial vs. social, whether compensation for wrongful punishment is present, and the broader institutional/identity context.

# 5) Prediction Guidance

Given the above findings:

- **Empirical Basis for Prediction**:
  - There is *limited direct evidence* to quantitatively predict the effect of enabling peer punishment on group efficiency in generic PGGs; only one adjacent study (Suzuki & Ishiwata) reports a direct efficiency improvement, while another (Amirova et al.) reports a strong efficiency *decrease* in a real-world context.
  - Most other studies show that punishment can raise cooperation or contributions, but efficiency (payoff to the group) may not increase, especially if punishment is costly or demotivating or crowding out intrinsic motivation.

- **Role of Control Game Efficiency and Design Dimensions**:
  - When baseline efficiency is already high due to communication or informal mechanisms (Herne et al., Gomez-Ruiz & Sánchez-Expósito), the marginal effect of punishment could be small or negative.
  - Prediction should consider context: in field/real-world settings where intrinsic motivation is high, or communication is possible, punishment may lower efficiency (Amirova et al.); in market-like, competitive games with clear, salient penalties/taxes, efficiency may increase (Suzuki & Ishiwata).

- **Design Dimension Moderators**:
  - The literature suggests the *effect of punishment on efficiency* is moderated by:
    - Communication (chat) increases baseline efficiency, potentially reducing need for punishment.
    - Type of punishment (social vs. financial) and compensation features.
    - Game structure (number of rounds, player count, mechanism for punishment/reward).
    - Player identities, informal mechanisms (team identity, stewardship, guilt aversion), and cultural context.

- **Quantitative Uncertainty**:
  - There is not enough direct, quantitative evidence to specify the magnitude—or even the sign—of efficiency change with punishment across all PGG-like games. Prediction must preserve outcome ambiguity and acknowledge setting-specific effects.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed**:
- `player_count`, `num_rounds`, and (sometimes) `mpcr`, appear in almost all empirical designs (Wu & Sun; Amirova et al.; Herne et al.; Suzuki & Ishiwata).
- `chat`/communication is a major moderator, routinely measured and manipulated (Amirova et al.; Herne et al.; Gomez-Ruiz & Sánchez-Expósito).
- `all_or_nothing` and `punishment_cost`/`punishment_tech` are present in several studies (Wu & Sun; Ferguson; Suzuki & Ishiwata).
- `reward_exists` is mentioned (Suratin et al.), but less frequently tested.

**Indirectly/Contextually Discussed**:
- `default_contrib` (framing), `show_n_rounds`, `show_other_summaries`, and `show_punishment_id` are less commonly core variables but included in some experimental settings (Herne et al., Suzuki & Ishiwata).

**Effectively Missing**:
- Most papers do not directly study `reward_cost`, `reward_tech`, or the effects of revealing punisher identity, nor the impact of alternative framing/defaults for contribution.
- The effect of parametric variations in game dimensions (e.g., systematically varying punishment cost or magnitude) is inconsistently addressed.

# 7) Important Limitations

- **Sparse Direct Evidence**: Only two studies provide direct, empirical evidence of punishment effects on group efficiency, and even these are contextually specific (market tax in lab; penalties in field, with opposite sign results).
- **Reliance on Proxy Outcomes**: Most studies measure behavioral outcomes (cooperation, contribution, norm compliance), not payoff-based efficiency, thus limiting direct relevance for payoff predictions.
- **Contextual Specificity**: Field experiments (Amirova et al.) and market simulations (Suzuki & Ishiwata) may not generalize to standard PGGs with pure peer punishment.
- **Theoretical Emphasis**: Many arguments are mechanism- or theory-heavy (Suratin et al.; Andrews & Davidson), lacking empirical calibration for prediction.
- **Missing Dimension Coverage**: Several important design variables are under- or unrepresented, particularly regarding reward systems, framing, and interface.
- **Potential Conflicts/Ambiguities**: The direction and magnitude of efficiency change with punishment are ambiguous; findings may conflict across lab vs. field, market vs. cooperation contexts.
- **No Unified Parametric Synthesis**: The literature does not provide continuous quantitative relationships between design dimensions and efficiency change when punishment is enabled; results are qualitative or categorical.

---

In summary, while the literature confirms that punishment changes behavior in public goods and related games, it does not provide strong, generalizable quantitative evidence—especially using group efficiency/payoff as the primary outcome—suitable for direct prediction using the full catalog of design dimensions. Most findings are contextually specific, reliant on behavioral proxies, and moderated by communication, motivation, and the institutional environment. Careful, context-aware interpretation and conservative prediction are warranted.
