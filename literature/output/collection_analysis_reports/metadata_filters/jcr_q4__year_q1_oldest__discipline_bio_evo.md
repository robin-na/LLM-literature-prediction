# 1) Evidence Base

The paper set consists entirely of theoretical modeling and simulation studies (all N=7), without any empirical or experimental evidence. These models include agent-based simulations, evolutionary game theory, and population biology frameworks. The set is moderately broad in its coverage of public-goods-game-like environments but is narrowly empirical and focused predominantly on long-run equilibrium and evolutionary logic rather than short- or medium-term behavioral dynamics or observed data. Most papers directly address the mechanics of costly punishment, metanorms, or conditional cooperation strategies, with varying degrees of realism in mapping to laboratory or field PGGs. There is substantial diversity in model assumptions and in whether the focus is on explicit punishment mechanisms versus other sanctioning or cooperation-maintenance strategies.

# 2) Task Relevance

- **pgg_or_variant**: The set includes multiple papers with **exact** (Deng et al., 2012; Kurokawa et al., 2010) and **close** (Bowles & Gintis, 2004; Kendal et al., 2006; Castro & Toro, 2008) relevance to PGGs or clear formal equivalents. Two papers are **adjacent** (Jaffe, 2004; Hagen & Hammerstein, 2006), focusing on artificial societies or generalized cooperation games.
- **punishment_or_sanctions**: Four papers are **exactly** on punishment (Deng et al., 2012; Bowles & Gintis, 2004; Kendal et al., 2006; Jaffe, 2004). Kurokawa et al. (2010) and Castro & Toro (2008) are **adjacent**, considering alternative sanctioning or cooperation strategies. Hagen & Hammerstein (2006) is **adjacent** and more concerned with game framing and context than mechanism details.
- **efficiency_or_related_payoff_outcome**: Five studies are **exact** (Deng et al., 2012; Kurokawa et al., 2010; Bowles & Gintis, 2004; Kendal et al., 2006; Jaffe, 2004) in targeting efficiency or explicit group payoff/welfare outcomes. One (Castro & Toro, 2008) is **close**. Hagen & Hammerstein (2006) is **adjacent** but does not present efficiency or payoff analysis.

Overall, the set's main insights for the prediction task derive from theory, not from direct empirical confirmation in laboratory or field settings.

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes**:
- Most of the paper set directly models or simulates aggregate group efficiency, total payoff, or surplus as outcomes (Deng et al., 2012; Kurokawa et al., 2010; Bowles & Gintis, 2004; Kendal et al., 2006; Jaffe, 2004; Castro & Toro, 2008). These outcomes precisely match the intended prediction target: average efficiency as a fraction of the fully cooperative outcome.
- Some studies explicitly examine the evolutionary stability or fixation probability of high-payoff cooperative equilibria (e.g., Kurokawa et al., 2010; Kendal et al., 2006).
- Jaffe (2004) is notable for highlighting scenarios where punishment, while increasing norm adherence, reduces overall efficiency due to its costs.

**Non-Payoff Behavioral Outcomes**:
- Behavioral measures such as norm compliance, contribution rates, and cooperation frequencies are sometimes discussed as intermediate steps or consequences (Jaffe, 2004; Bowles & Gintis, 2004), but efficiency or group payoff remains the primary focus.
- Hagen & Hammerstein (2006) explicitly address only non-payoff outcomes (behavioral responses, cognitive framing), cautioning against overinterpreting game-theoretic models for predicting real-world payoff results.

The set clearly distinguishes efficiency or payoff from non-payoff behaviors, but relies entirely on theoretical logic for payoff predictions.

# 4) Main Findings Relevant To Prediction

- **Positive Effects of Punishment on Efficiency**: Most models (Deng et al., 2012; Bowles & Gintis, 2004; Kendal et al., 2006) find that enabling punishment (of defectors, norm violators, or non-punishers), especially when it is rare, severe, concerted, or reinforced by a metanorm, substantially increases efficiency and average group payoff relative to a no-punishment control. The presence of strong reciprocators or punishing agents can stabilize cooperative, high-efficiency equilibria in a range of group sizes and parameterizations. For example, Bowles & Gintis (2004) and Kendal et al. (2006) observe that the transition from low- to high-efficiency equilibria depends critically on the existence and structure of punishment or reward mechanisms.
- **Parameters Moderating Punishment’s Effect**: The models emphasize that efficiency gains from punishment depend on factors such as group size (larger groups favor concerted/severe and rare punishment: Deng et al., 2012), cost and magnitude of punishment (lower cost and higher severity promote efficiency), presence of metanorms (Kendal et al., 2006), and the specific structure of the punishment (e.g., sharing costs, probabilistic assignment).
- **Conditions Where Punishment Reduces Efficiency**: Jaffe (2004) finds that punishment can reduce aggregate efficiency, despite increasing behavioral cooperation, if the direct costs of punishing are high and there are no synergistic returns from norm compliance. This result stands in partial conflict with the other theoretical models and introduces conditionality into the prediction task.
- **Alternative Mechanisms**: Some models (Kurokawa et al., 2010; Castro & Toro, 2008) find that cooperation and efficiency can arise via contingent cooperation, generosity, or voluntary participation, even without explicit costly punishment, but these findings are only adjacent to the prediction task and do not directly inform the incremental impact of enabling punishment.
- **Framing and Context Sensitivity**: Hagen & Hammerstein (2006) argue for a high sensitivity of all such models to social context, framing, and participants’ cognitive interpretations—factors not formally captured in most models and not in prediction covariates.

# 5) Prediction Guidance

Based on this literature, enabling a well-designed, sufficiently severe, and not-too-costly peer punishment regime in public goods game environments is theoretically predicted to increase group efficiency relative to a no-punishment control, especially for larger groups and if punishment is rare or concerted. The effect is strengthened if reward mechanisms for punishers (metanorms) are present and costs are kept low (Kendal et al., 2006; Bowles & Gintis, 2004; Deng et al., 2012). 
However, predictions should account for conditions where punishment’s costs outweigh efficiency gains, notably in settings where punishing imposes significant resource loss unrewarded by synergistic social returns (Jaffe, 2004).

In practice, using control (no-punishment) efficiency as a baseline, predictions for treatment (punishment-enabled) efficiency should adjust upward—potentially sharply—if the punishment mechanism is severe, rare, and shared in cost, and costs are not prohibitive. The magnitude of the predicted increase should be discounted or possibly reversed if model parameters indicate high implementation cost coupled with a lack of direct returns from norm enforcement. If reward mechanisms for punishers are present, or if group size is large, a stronger positive shift should be predicted. 

Predictions are underpinned solely by theory and simulation, not human-subject experimental data, and may diverge in real-world PGG settings due to framing, cognitive construal, or factors not represented in parameter covariates (Hagen & Hammerstein, 2006).

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed**:
- `player_count`, `num_rounds`, `mpcr`: Modeled in most core theory papers (Deng et al., 2012; Bowles & Gintis, 2004; Kurokawa et al., 2010; Castro & Toro, 2008), with concrete implications for efficiency and punishment effect.
- `punishment_cost`, `punishment_tech`: In-depth analysis of how varying punishment cost and structural details moderate efficiency effects (Deng et al., 2012; Bowles & Gintis, 2004; Jaffe, 2004).
- `reward_exists`, `reward_cost`: Explored by Kendal et al. (2006), especially in the context of metanorms.
- `all_or_nothing`: Discussed in theory for game structure (Deng et al., 2012; Kurokawa et al., 2010).
- `show_n_rounds`: Occasionally modeled in repeated game structures (Kurokawa et al., 2010; Castro & Toro, 2008).

**Indirectly or Contextually Discussed**:
- `show_other_summaries`, `default_contrib`: Some mention in the description of model variants, but not as central moderating variables.
- `punishment_magnitude`: Implicitly embedded in “severity” parameters but often coupled with punishment cost in models.
- `chat`, `show_punishment_id`: Not present in any of the analyzed models.

**Effectively Missing**:
- `chat`, `show_punishment_id`: No discussion; missing from all papers.
- Realistic temporal or social context mechanisms (as flagged by Hagen & Hammerstein, 2006) and explicit experimental design dimensions relevant to laboratory studies.
- No models incorporate behavioral or psychological nuances that might arise from transparency or communication features.

# 7) Important Limitations

- **Theory-Only Base**: No direct human or empirical data; all findings are theoretical or from agent-based simulation, limiting confidence in real-world extrapolation.
- **Sparse Coverage of Some Design Dimensions**: Key game dimensions such as `chat` and `show_punishment_id` are missing from the literature, so their effects on efficiency when enabling punishment are unknown.
- **Conditionality and Disagreement**: While most models predict a positive effect of punishment on efficiency, at least one (Jaffe, 2004) explicitly finds negative efficiency effects from costly punishment absent further social synergy, and the set does not resolve under which empirical circumstances each regime dominates.
- **No Testing of Framing or Social Context Effects**: As flagged by Hagen & Hammerstein (2006), the literature does not model or test the impact of social cues, context, or human construal, thus limiting the predictive utility in varied applications.
- **No Direct Mapping to Control Efficiency**: Although the models can compare regimes, there is little direct quantification of how baseline (no-punishment) efficiency maps onto treatment outcomes after enabling punishment—the translation is conditional on specific modeled equilibria and can be nonlinear.
- **No Validation Against Experimental Data**: None of the predictions about efficiency effects of punishment are empirically validated in public goods games with human or animal subjects.

In summary, this literature set is informative for prediction only under its theoretical assumptions, particularly about punishment structure and costs; it cannot quantify effects where design features fall outside those modeled, and may misestimate real-world effect sizes or directions in the presence of context, communication, or framing effects not parametrized within these models.
