# 1) Evidence Base

The paper set consists entirely of theoretical papers (26/26), with no empirical or laboratory experimental studies. All findings are based on modeling, simulation, conceptual analysis, or theoretical frameworks. This set is broad in its coverage of evolutionary, neuroeconomic, and mechanistic perspectives on cooperation, punishment, and social dilemmas, but narrow in that it provides little to no direct experimental evidence or quantitative effect estimates for public goods games (PGGs) where efficiency is measured as a normalized group payoff. Modeling approaches range from traditional game theory and evolutionary simulation, to gene-culture coevolution and neuroeconomic review. 

# 2) Task Relevance

- **pgg_or_variant**: Theoretical coverage of the PGG or its direct variants is strong in a minority of papers (with several marked `exact`), and broad but indirect in others (`close`, `adjacent`). Most papers focus directly on PGG structure or highly analogous scenarios (e.g., threshold or all-or-nothing PGGs, resource dilemmas).
    - *Label count*: `exact` (8), `close` (8), `adjacent` (8), `none` (2)
- **punishment_or_sanctions**: The majority center punishment (`exact` or `close`), including variants like peer and institutional punishment/sanction, though some papers address only rewards or do not model punishment explicitly.
    - *Label count*: `exact` (13), `close` (2), `adjacent` (8), `weak` (1), `none` (2)
- **efficiency_or_related_payoff_outcome**: Only a minority provide results directly about efficiency (group payoff or welfare), usually within theoretical models; many focus instead on cooperation rates, norm stability, or other behavioral outcomes.
    - *Label count*: `exact` (8), `close` (6), `adjacent` (10), `none` (2)

The literature thus speaks directly to the structure and mechanisms of punishment in PGGs, but very few papers supply efficiency or payoff results directly suited to the prediction task.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes**: Several theoretical models report group efficiency, total payoff, or fitness consequences as their primary outcome (e.g., Eldakar et al., 2013; POLLOCK, 1988; Forsyth & Hauert, 2011; Archetti & Scheuring, 2011; Ubeda & Duéñez-Guzmán, 2011; Sasaki et al., 2016; Sasaki & Uchida, 2014). Even these, however, seldom use the exact normalized efficiency ratio as defined for prediction—many present fitness, equilibrium payoff, or welfare in the context of infinite or very abstract populations.
- **Non-Payoff (Behavioral) Outcomes**: Many more papers focus on model outcomes such as: contribution/cooperation rate, frequency of punisher types, norm stability, strategy fixation, neural or psychological correlates of punishment, and presence/absence of cooperative equilibrium (e.g., Lehmann et al., 2007; Declerck et al., 2013; Henrich & Henrich, 2006; Boehm, 2014). These are informative about mechanisms and moderators, but not group efficiency per se.
- **Mixed or Adjacent Outcomes**: Some studies discuss payoff only as a conceptual extension, while many do not report explicit payoff/efficiency results.

# 4) Main Findings Relevant To Prediction

**Summary of Evidence:**
- **Effect Direction**: Across the theoretical models that address efficiency/payoff in PGGs, enabling peer or institutional punishment generally increases group efficiency relative to control, particularly when punishment is effective and not too costly. (Eldakar et al., 2013; POLLOCK, 1988; Gardner & West, 2004; Ubeda & Duéñez-Guzmán, 2011; Sasaki et al., 2016)
- **Moderators with Strong Theoretical Support**:
    - **Punishment Cost**: The efficiency gain from enabling punishment is greater when the cost for the punisher is low (Eldakar et al., 2013; Gardner & West, 2004; Ubeda & Duéñez-Guzmán, 2011).
    - **Player Count / Group Size**: Smaller groups enable stronger group selection and clearer impact of punishment on efficiency; with larger groups, effect attenuates unless other strong mechanisms (e.g., institution or rewards) are present (Eldakar et al., 2013; Gardner & West, 2004; POLLOCK, 1988; Forsyth & Hauert, 2011 for reward).
    - **Number of Rounds**: More rounds/iterations allow punishment to establish higher efficiency; in single-round or very short games, punishment is less effective (Eldakar et al., 2013; POLLOCK, 1988).
    - **MPCR**: While commonly manipulated, few supply concrete interaction effects—higher MPCR supports baseline cooperation, which may reduce the marginal need for punishment; but its interaction with punishment is model-dependent.
    - **Institutionalization**: Pool/institutional punishment or assessment-linked exclusion are more robust than purely peer-based mechanisms, especially in larger or repeated groups (Sasaki et al., 2016; Forsyth & Hauert, 2011).
    - **Design Complexity (Power Asymmetry, Network Structure, Population Structure)**: Effectiveness of punishment in raising efficiency may require network/population structure or power asymmetries (POLLOCK, 1988; Ubeda & Duéñez-Guzmán, 2011; Lehmann et al., 2007). In unstructured, one-shot, or anonymous environments, punishment less reliably improves efficiency.
- **Boundary Conditions and Limitations**:
    - When punishment costs are high, or punishers can be targeted for counter-punishment, overall efficiency can decrease.
    - Without sufficient structure or linkage (e.g., between punishing and being the recipient of increased cooperation), punishment may fail to increase or may even reduce group efficiency (Gardner et al., 2007; Lehmann et al., 2007).
    - Reward mechanisms alone increase efficiency, but full efficiency generally requires stronger enforcement (Forsyth & Hauert, 2011).

# 5) Prediction Guidance

This literature, though theoretical, provides convergent support for the *direction* of punishment’s effect on efficiency in PGGs: enabling punishment under typical design parameters should increase average group efficiency relative to a no-punishment baseline. However, the magnitude of the effect is highly sensitive to several design dimensions:

- **Directly Informing Dimensions**: Prediction for treatment efficiency should expect larger relative gains from punishment when punishment is cheap (punishment_cost low, punishment_tech effective), groups are small (player_count low), number of rounds is high (num_rounds high), and institutional features that support punishment efficacy are present (punishment_tech includes institutional/pool mechanisms).
- **Indirectly or Weakly Informed Dimensions**: Some dimensions (e.g., mpcr, all_or_nothing, reward_exists, reward_cost, reward_tech, player-specific identity display [showPunishmentId], or chat) are only variably addressed and mostly in supporting roles.
- **Control Efficiency as Input**: While the models inform likely effect direction, none provide a recipe to compute treatment efficiency quantitatively from control efficiency and game parameters; rather, they model mechanism and boundary conditions. Thus, control efficiency remains an important empirically observed anchor, with theory supporting that, ceteris paribus, the addition of effective/cheap punishment should improve treatment efficiency above control, as long as adverse parameter values (e.g., high punishment_cost, very large player_count, lack of group structure) do not apply.

Key caveat: Absence of empirical, parameter-calibrated data means effect size predictions (e.g., how much efficiency improvement for a given change in punishment cost) are uncertain, and the boundary for negative or null effects is predicted only qualitatively.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**
- `player_count` (Eldakar et al., 2013; Forsyth & Hauert, 2011; POLLOCK, 1988; Archetti & Scheuring, 2011)
- `num_rounds` (Eldakar et al., 2013; POLLOCK, 1988; Bshary & Bronstein, 2011)
- `mpcr` (Eldakar et al., 2013; Forsyth & Hauert, 2011; POLLOCK, 1988)
- `punishment_cost` and `punishment_tech` (Eldakar et al., 2013; Gardner & West, 2004; Ubeda & Duéñez-Guzmán, 2011; Lehmann et al., 2007)
- `all_or_nothing` (Archetti & Scheuring, 2011; Forsyth & Hauert, 2011; Sasaki & Uchida, 2014)
- `reward_exists`, `reward_cost`, `reward_tech` (Forsyth & Hauert, 2011; Sasaki & Uchida, 2014)

**Indirectly or Contextually Informed:**
- `show_punishment_id`, `show_other_summaries` (discussed in context: Boehm, 2014; Baker & Rachlin, 2002; Levy, 2022)
- `default_contrib` (very little direct discussion; possible in framing/opt-in/out theory contexts)
- `chat` (Declerck et al., 2013; as influencing cooperation, not specifically efficiency or punishment)

**Effectively Missing:**
- Little or no direct modeling of `show_n_rounds`, `show_punishment_id`, `default_contrib` as design variables in these theoretical models.

# 7) Important Limitations

- **Lack of Empirical Data**: All findings are theoretical; no empirical parameterization or effect-size estimates exist in this set. No data exist on actual treatment versus control efficiency ratios in real PGGs under variant punishment designs.
- **Payoff Outcome Gaps**: Many papers use evolutionary fitness or conceptual group payoff, which do not always map to normalized efficiency as defined for PGGs; sometimes, only behavioral outcomes (e.g., proportion cooperating) are modeled.
- **Sparse Coverage of Some Dimensions**: Several prediction-relevant design dimensions are unmodeled or only tangentially mentioned (e.g., chat, summary visibility, default action framing).
- **Boundary Conditions Unresolved**: Where models diverge (e.g., regarding the need for group/kin structure, or effect under high cost), ambiguity should be maintained—punishment may not increase efficiency in all environments (Gardner et al., 2007; Lehmann et al., 2007).
- **Assumptions Matter**: The models often assume infinite time, repeated play, or ideal enforcement; in practice, real-world variations (e.g., learning, misimplementation) may blunt predicted effects.
- **Reward vs. Punishment**: While some reward-enabled models are included, they may not generalize to prediction of punishment effects, and vice versa.
- **No Calibration for Multi-Dimensional Interactions**: Interaction effects (e.g., between punishment cost and group size, or with reward enabled) are discussed but not quantified for prediction.

---

**In summary:** The theoretical literature robustly supports the qualitative prediction that enabling effective, low-cost punishment will—*under the right conditions*—increase group efficiency in public goods games beyond the no-punishment control. The best-informed design moderators are punishment cost, group size, rounds, and institutionality. However, due to a lack of empirical calibration and coverage gaps for some game features, downstream efficiency predictions based solely on these models should remain cautious and sensitive to game-specific context and unmodeled dimensions.
