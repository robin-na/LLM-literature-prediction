# 1) Evidence Base

The literature set consists mainly of theoretical work (4 out of 6 papers) with only one empirical/observational study and one paper synthesizing experimental meta-evidence (Vasconcelos et al., 2022). The primary focus is on theoretical models and conceptual analyses of public goods games (PGGs), their variants, and related social dilemmas, especially concerning mechanisms of punishment and institutional design. The scope for direct prediction of efficiency effects in experimental PGGs with and without punishment is thus relatively narrow. Only **one** paper (Vasconcelos et al., 2022) provides theory alongside meta-synthesized empirical data from PGG experiments; the rest largely extrapolate from adjacent domains or focus on non-payoff behavioral outcomes. Only one paper is a purely observational field study—relevant for organizational cooperation but not game-theoretic efficiency (Holubcik et al., 2023).

# 2) Task Relevance

**pgg_or_variant**:  
- `exact`: Vasconcelos et al. (2022; pure PGGs),  
- `adjacent`: Lim & Capraro (2022; trust game with PGG structure), Wang & Cui (2022; principal-agent social dilemma), Chen et al. (2022; hawk-dove, some Prisoner's Dilemma), Zhu et al. (2023; continuous-action dilemmas),  
- `weak` to `none`: Holubcik et al. (2023) (organizational settings only).

**punishment_or_sanctions**:
- `exact`: Vasconcelos et al. (2022), Lim & Capraro (2022), Wang & Cui (2022; theoretical sanctions),  
- `none`: Chen et al. (2022), Zhu et al. (2023), Holubcik et al. (2023).

**efficiency_or_related_payoff_outcome**:  
- `exact`: Vasconcelos et al. (2022), Lim & Capraro (2022; “mean payoff”),  
- `adjacent`: Wang & Cui (2022) (compliance, self-discipline without group payoff analysis), Zhu et al. (2023), Holubcik et al. (2023),  
- `close`: Chen et al. (2022; time-averaged payoffs in non-PGG games).

**Summary**: Only Vasconcelos et al. (2022) fully fits all three relevance dimensions for the prediction task, with Lim & Capraro (2022) providing close support via trust-game analogs. The remaining papers are limited either by focusing on non-payoff outcomes or by lacking punishment/incentive manipulation.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes** (relevant for efficiency prediction):
- **Efficiency**, **group payoff**, **total earnings** (Vasconcelos et al., 2022; Lim & Capraro, 2022) are analyzed as direct outcomes of punishment in models or meta-analyses.

**Non-payoff behavioral outcomes**:
- **Cooperation rates**, **compliance/self-discipline**, **strategy convergence** (Wang & Cui, 2022; Zhu et al., 2023; Chen et al., 2022).
- Organizational and strategic outcomes, such as **innovation, knowledge sharing, and competitiveness**, (Holubcik et al., 2023)—not payoff-based in the game-theoretic sense.

**Distinction Maintained**:  
Most papers outside of Vasconcelos et al. (2022) and Lim & Capraro (2022) do *not* measure or report group-level payoff/efficiency; their outcomes are behavioral or qualitative.

# 4) Main Findings Relevant To Prediction

- **Punishment Robustly Increases Efficiency in PGGs**: Both the theoretical model and meta-study in Vasconcelos et al. (2022) conclude that enabling peer punishment almost always results in increased group efficiency/payoff *if institutional conditions are suitable*. The key is the alignment of punishment institution scale to the scale of the public good and the decision rule for institution adoption; learning/memory also matter. Poorly aligned or informationally impoverished designs weaken the effect.
- **Synergy with Network Structure and Cost-Effectiveness**: Lim & Capraro (2022) demonstrate—primarily in trust-game-like settings—that punishment and network structure interact: even modest punishment can achieve maximal efficiency when paired with network structure, with diminishing returns (or even negative impact) if punishment is too costly.
- **Punishment Mechanism Details Matter**: Wang & Cui (2022) (in a principal-agent model) find *dynamic* punishment schemes outperform static ones in promoting compliance, plausibly affecting the efficiency impact, although no payoff or efficiency is reported.
- **Parameter Sensitivity**: Both Vasconcelos et al. (2022) and Lim & Capraro (2022) highlight that player count, round number, and MPCR, as well as the cost and targeting of punishment, determine when punishment boosts efficiency versus when it may fail.
- **Lack of Evidence for Some Dimensions**: No direct empirical evidence is available for many design features (opt-in/opt-out framing, chat, showing round number, identity revelation, reward system details), leaving their interactive effects on efficiency under punishment unassessed.

# 5) Prediction Guidance

The literature most supports the following prediction principle:

> **Punishment-enabled designs, when institutional features are appropriately aligned (e.g., collective rule for global goods, adequate learning/information conditions, cost-effective punishment), will predictably yield higher group efficiency relative to punishment-disabled designs (Vasconcelos et al., 2022; Lim & Capraro, 2022). However, the magnitude of this increase depends on details of institutional scale, punishment cost, network structure, and potentially the dynamic targeting of sanctions.**

For *model-based prediction*, use control-game efficiency as a baseline and estimate an increase due to enabling punishment—contingent on:
- Punishment is collective (for global goods) or individual (for local goods)
- Punishment cost is not excessive (so gains from cooperation outweigh costs)
- Players are sufficiently informed (relevant information about actions/outcomes is available)
- Network/interaction structure is not extremely sparse (Lim & Capraro, 2022)
- Potentially, sanctions are dynamic, not static (supported by Wang & Cui, 2022, but without direct efficiency evidence)

Lack of evidence or experimental uncertainty on other design dimensions means their impact should be considered unknown or at best contextually modulating.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- **player_count**, **num_rounds**, **mpcr**, **punishment_cost**, **punishment_tech**: Central in Vasconcelos et al. (2022), Lim & Capraro (2022), and Wang & Cui (2022).
- **show_other_summaries** (information, learning): Explicitly discussed as critical in Vasconcelos et al. (2022).
- **all_or_nothing**: Considered in adjacent models (e.g., Lim & Capraro, 2022; Wang & Cui, 2022), though not always as a primary focus.

**Indirectly or Contextually Discussed:**
- **reward_exists**: Only present in Wang & Cui (2022)—not tied to payoff impact or PGG efficiency.
- **network structure**: Implicit through analysis of player interactions in Lim & Capraro (2022) and Zhu et al. (2023).

**Effectively Missing:**
- **chat**
- **default_contrib**
- **show_n_rounds**
- **show_punishment_id**
- **reward_cost, reward_tech**
- Most elements of interface/feedback design and some institutional details,
- Empirical treatment of **reward-enabled** games.

# 7) Important Limitations

- **Empirical Scope Is Limited**: Only one paper includes meta-analytic confirmation from experimental studies for PGGs with and without punishment; most others are modeled or adjacent domains.
- **Sparse Evidence for Many Design Features**: Little to no evidence on the impact of chat, default contribution framing, reward system details, or salience/information interface variables.
- **Behavioral Versus Payoff Outcomes**: The bulk of the literature (outside Vasconcelos et al., 2022; Lim & Capraro, 2022) reports on cooperation rates or compliance, not efficiency or total payoff—a key distinction for predictive modeling.
- **Adjacent Domains, Not Always PGGs**: Several papers study trust games, principal-agent problems, hawk-dove, or continuous-action dilemmas rather than PGGs, requiring assumptions for transfer to the PGG context.
- **Design Interaction Effects Are Understudied**: Potential interactions between enabling punishment and other features (e.g., communication, information, identity) are untested in this set.
- **No Data on Extreme Parameter Regimes**: Model boundaries and practical limits (e.g., very high or very low MPCR, extreme group sizes) are not experimentally validated and may differ in practice from theoretical predictions.

In sum, this literature set supports the qualitative prediction that well-implemented punishment increases efficiency in PGG-like environments, with some guidance on institutional, cost, and information moderators. However, payoff-based evidence is sparse outside the PGG domain, and many design features relevant to fielded experiments remain evidence-gaps for direct predictive use.
