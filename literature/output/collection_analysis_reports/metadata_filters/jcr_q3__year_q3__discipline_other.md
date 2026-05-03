# 1) Evidence Base

The provided literature set is composed of five papers with a mix of experimental (lab and field) and theoretical approaches. Three papers report laboratory experiments (Gomez-Ruiz & Sánchez-Expósito, 2020; Zhang et al., 2019; Ferguson, 2021), one is a theory/modeling paper (Liu & Yang, 2018), and one is a quasi-experimental field study (Berger, 2021). The topic focus is broad with respect to the downstream prediction task—punishment-enabled Public Goods Game (PGG) efficiency—since not all papers use formal PGGs or explicit punishment interventions, and only one paper reports group efficiency or related payoffs as a primary outcome. Across the set, empirical work is more common than theory, but empirical findings are mostly limited to behavioral outcomes rather than direct measures of group payoff or efficiency under punishment.

# 2) Task Relevance

**PGG or Variant**:  
- Relevance varies from `exact` (formal PGG) to `close` (public-goods-like dilemmas with relevant design dimensions) and `adjacent` (games or field studies with some social dilemma elements but not full PGG structure). Only Zhang et al. (2019) provides `exact` payoff-related data in a PGG-variant; others are `close` or `adjacent`.  
**Punishment or Sanctions**:  
- Only Ferguson (2021) and Liu & Yang (2018) implement explicit punishment options (`exact`). Others are `adjacent` (team identity, feedback, norm interventions) or have `none` (Zhang et al., 2019). Few papers experimentally compare punishment-on versus punishment-off treatments in a PGG context.  
**Efficiency or Related Payoff Outcome**:  
- Only Zhang et al. (2019) measures average efficiency or group earnings as a primary outcome (`exact`). In other cases, efficiency or total payoff is either not reported or only contextually mentioned (`adjacent` to `weak`). Behavioral cooperation and norm adoption are more frequently measured.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes**:  
  - Direct measures of group payoff, efficiency, or welfare are only reported by Zhang et al. (2019) in a punishment-free, step-level PGG variant. In other studies, such outcomes are either not measured or only informally referenced (e.g., through discussions of stable cooperation potentially implying higher welfare or payoff in Liu & Yang, 2018).
- **Non-Payoff Behavioral Outcomes**:  
  - The dominant outcome type in this set is behavioral: contribution rate, free-riding, norm adoption, punishment or compensation choice behavior.  
  - Examples: Gomez-Ruiz & Sánchez-Expósito (2020) focus on contribution behavior and free-riding responses; Ferguson (2021) reports individual punishment versus compensation choices; Berger (2021) measures the prevalence of a focal sustainable behavior (mug use); Liu & Yang (2018) models cooperation frequency.

# 4) Main Findings Relevant To Prediction

- **Punishment Effects on Efficiency:**  
  - There is little direct evidence on the marginal *effect* of enabling peer punishment on group efficiency in PGG settings. No paper in the set compares PGG efficiency with punishment-on versus punishment-off in a controlled design.
  - Papers with explicit punishment mechanisms (Ferguson, 2021; Liu & Yang, 2018) focus on individual strategy choice or stable cooperation, not actual group efficiency or payoff data. 
  - Behavioral findings suggest that options for compensation may reduce punishment usage (Ferguson, 2021), and that both incentives and punishment need to surpass a threshold to stabilize cooperation (Liu & Yang, 2018). That may *imply* an effect on efficiency, but it is not empirically established.
- **Non-Punitive Mechanisms:**  
  - Social or motivational interventions, such as introducing a consistent contributor (Zhang et al., 2019) or enhancing team identity (Gomez-Ruiz & Sánchez-Expósito, 2020), can boost cooperation and, in one case, group payoff, though only in the absence of punishment.
  - Norm feedback and social tipping (Berger, 2021) influences behavioral adoption rates and shows non-linear, context-dependent effects (possible “boomerang” when baseline behavior is low), but does not report payoff-based outcomes.

# 5) Prediction Guidance

**Direct Prediction**:  
- The literature set provides little direct empirical support for predicting how enabling peer punishment changes efficiency in public-goods-game-like environments.  
- The only paper with payoff-based outcomes (Zhang et al., 2019) reports effects of *non-punitive* interventions—increases in efficiency due to a role model, not punishment.  
- Where punishment is present, outcomes are generally behavioral or theoretical (Ferguson, 2021; Liu & Yang, 2018), without efficiency metrics or side-by-side control comparisons.

**Indirect or Contextual Guidance**:  
- Findings suggest the *potential* for punishment to shift group behavior toward more cooperation or discourage free-riding *if* parameters like punishment cost and available compensation are appropriately set (Liu & Yang, 2018; Ferguson, 2021).
- Compensation options may crowd out punitive responses, potentially affecting efficiency if punishment is key to deterring free-riding.
- Non-punitive mechanisms (role models, team identity) can meaningfully increase efficiency in the absence of punishment (Zhang et al., 2019) and may set the baseline.
- Feedback and norm signaling can impact the likelihood of norm-adoption but show variable directionality depending on initial conditions (Berger, 2021).

# 6) Design Dimensions Highlighted Across Papers

- **Directly Informed Dimensions**:
  - `player_count`, `num_rounds`, `chat`, `all_or_nothing`, `mpcr`, `show_n_rounds`: All are explicitly varied or reported in at least two experimental papers (Gomez-Ruiz & Sánchez-Expósito, 2020; Zhang et al., 2019; Ferguson, 2021).
  - `punishment_cost`, `punishment_tech`: Directly manipulated in Ferguson (2021) and modeled in Liu & Yang (2018).
  - `reward_exists`: Modeled in Liu & Yang (2018), though reward size/cost details are limited.
  - `show_other_summaries`: Central to the feedback intervention in Berger (2021).
- **Indirect/Only Contextually Discussed**:
  - `default_contrib`: Some evidence from framing and intervention context, but not systematically varied.
  - `show_punishment_id`, `reward_cost`, `reward_tech`/`reward_magnitude`: Not directly manipulated in experiments; at best background or possibly implied.
- **Effectively Missing**:
  - For several dimensions (notably `reward_cost`, `reward_tech`, detailed punishment magnitude), little to no empirical evidence is provided on efficiency or payoff outcomes relative to those settings. Similarly, cross-dimensional interactions (e.g., how `chat` or `player_count` may moderate punishment’s efficiency effects) are not explored.

# 7) Important Limitations

- **Lack of Direct Efficiency Data**:  
  There are no experiments in this set that compare efficiency (payoff) in “punishment-off” (control) versus “punishment-on” (treatment) versions of the same PGG design. Most findings on punishment relate to behavioral outcomes, not group payoff or aggregate efficiency.
- **Punishment Effects are Indirect or Modeled**:  
  Where punishment is analyzed, it is often in non-PGG or non-repeated settings (Ferguson, 2021), or as part of a theoretical model (Liu & Yang, 2018) without direct efficiency outcome data.
- **Contextual (Not Mechanistic) Focus**:  
  Several papers (Gomez-Ruiz & Sánchez-Expósito, 2020; Berger, 2021) address mechanisms for sustaining cooperation that are not tied to formal punishment or payoff outcomes and may not generalize to punishment-enabled designs.
- **Sparse Design Dimension Coverage**:  
  While basic game parameters are represented, other dimensions critical for prediction (e.g., information structure around punishment, cost/magnitude of punitive and reward actions) are underexplored with respect to efficiency or payoff-based effects.
- **Ambiguity and Absence of Comparative Data**:  
  No clear disambiguation is available regarding under what conditions peer punishment increases, decreases, or leaves unchanged the efficiency of group play in PGGs—especially as compared to baseline control efficiency.

**Conclusion:**  
The literature set is limited in its ability to inform direct predictions about punishment’s effect on efficiency in PGGs as a function of design dimensions and control efficiency. Most evidence is indirect, either focusing on behavioral outcomes, non-punitive mechanisms, or theoretical thresholds rather than quantifying payoff-based treatment effects in the relevant experimental settings.
