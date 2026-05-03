# 1) Evidence Base

The paper set comprises three studies: two empirical and one theoretical. The empirical studies include a laboratory experiment with human participants in a punishment context (Kodaka et al., 2012) and a field-based observational study examining punishment and response behaviors in animals (Bshary & Bshary, 2012). The theoretical paper uses agent-based simulation of N-person games with nonlinear payoffs but does not incorporate explicit sanctions or report efficiency outcomes (Szilagyi & Somogyi, 2010). 

Overall, the coverage is narrow for the downstream prediction task: none of the papers provide experimental or quantitative comparisons of group efficiency or payoff with and without peer punishment in a public-goods-game (PGG) context. Instead, the set focuses primarily on behavioral responses and the mechanisms or contexts shaping punishment, with only indirect or adjacent discussions of efficiency or payoff outcomes.

# 2) Task Relevance

- **pgg_or_variant**: All three papers are only *adjacent* to PGGs. Kodaka et al. (2012) uses a cooperation context with punishment but does not specify a standard PGG. Bshary & Bshary (2012) studies a naturalistic foraging game with public-good analogies rather than a laboratory PGG. The theoretical simulation (Szilagyi & Somogyi, 2010) examines N-person games with externalities but does not model a classic PGG structure.

- **punishment_or_sanctions**: Kodaka et al. (2012) has *exact* relevance (direct punishment manipulation), Bshary & Bshary (2012) is *close* (punishment by victims in a public-good-like scenario), and Szilagyi & Somogyi (2010) is only *adjacent* (no explicit punishment).

- **efficiency_or_related_payoff_outcome**: All three score *weak* to *adjacent* at best. None report efficiency, group payoff, or welfare outcomes as their primary result; all focus on non-payoff outcomes such as punishment behavior, cooperation rates, or individual foraging choices.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes**: Direct measurements of group efficiency, total earnings, welfare, or surplus are absent across the set. Bshary & Bshary (2012) and Szilagyi & Somogyi (2010) occasionally discuss payoff structures or payoffs in adjacent terms, but do not report group-level efficiency.

- **Non-payoff behavioral outcomes**: All papers focus primarily on behavioral outcomes:
   - Kodaka et al. (2012) examines how the level of group cooperation modulates the intensity of punishment assigned to non-cooperators.
   - Bshary & Bshary (2012) studies individual behavioral adaptation (e.g., switching victims) after punishment.
   - Szilagyi & Somogyi (2010) analyzes equilibrium rates of cooperation under varying payoff functions and agent update rules.
   
  These outcomes include punishment frequency, cooperation rates, and strategy adaptation, but they are not substitutes for actual group efficiency data.

# 4) Main Findings Relevant To Prediction

- **Punishment is context-dependent**: Kodaka et al. (2012) empirically demonstrates that the severity of punishment dealt to non-cooperators is higher in highly cooperative groups, reflecting both behavior and brain activation. However, there is no evidence about how this shifts group efficiency.

- **Behavioral heterogeneity and public good creation**: Bshary & Bshary (2012) shows that not all punishment in a public-good-like setting leads to increased group benefit. The effect of punishment depends critically on whether punished individuals adapt in ways that benefit the group—specifically, whether they switch behaviors in response to punishment. There is a suggestion that only certain behavior patterns after punishment contribute to higher group payoff, but this is a mechanistic inference, not a direct efficiency measurement.

- **Game structure, payoff shape, and cooperation**: Szilagyi & Somogyi (2010) identifies that the shape of the payoff function, as well as other aspects of game structure such as neighborhood and agent behavior rules, have strong effects on equilibrium cooperation rates, but these are not mapped to efficiency outcomes and are examined without explicit use of punishment.

- **No empirical quantification of efficiency or payoff gains from punishment**: Across all three papers, there is an absence of direct empirical or simulated evidence for the change in group efficiency when peer punishment is enabled compared to a punishment-absent control condition.

# 5) Prediction Guidance

Given the lack of direct efficiency measurements, this literature set provides only indirect and highly qualified guidance for predicting treatment efficiency:

- **Context sensitivity**: The effect of punishment on group cooperation—and potentially on efficiency—appears sensitive to the broader social context (e.g., existing cooperation levels) (Kodaka et al., 2012). Modeling or prediction efforts should consider interaction effects between punishment mechanisms and baseline cooperation.

- **Behavioral rules matter**: Individual variability in response to punishment (e.g., propensity to cooperate, switch partners, or defect) could mediate or even reverse the expected efficiency gains from enabling punishment (Bshary & Bshary, 2012). Predictive models should not assume uniform or always-beneficial punishment effects.

- **Theoretical ambiguity**: Nonlinear payoffs and local interactions introduce unpredictability in cooperation levels that could influence efficiency outcomes, but the link between such behaviors and actual group payoff under punishment is not addressed (Szilagyi & Somogyi, 2010).

**Bottom line**: This set does not support numerical or precise prediction of the change in average efficiency due to the introduction of peer punishment in PGG-like environments. It mainly suggests factors and contextual moderators that should be included in richer modeling or in setting priors on prediction models.

# 6) Design Dimensions Highlighted Across Papers

- **Directly informed**:
   - `player_count`, `num_rounds`, `punishment_tech`, `punishment_cost`, `all_or_nothing`, `show_n_rounds`, `show_punishment_id`: These dimensions are either directly manipulated or described in the context of the experiments (Kodaka et al., 2012; Bshary & Bshary, 2012; Szilagyi & Somogyi, 2010).
- **Indirectly informed or contextually discussed**:
   - `chat` (Kodaka et al., 2012, included as a contextual factor), `punishment_cost` and `punishment_tech` (mainly as background in Bshary & Bshary, 2012).
   - `all_or_nothing` (binary decisions in Szilagyi & Somogyi, 2010).
- **Effectively missing or not covered**:
   - `default_contrib`, `mpcr`, `reward_exists`, `reward_cost`, `reward_tech`, `show_other_summaries`, `show_punishment_id` (other than context; no direct manipulation or measurement), and especially the mapping between these and payoff or efficiency outcomes.

Crucially, none of the 14 dimensions are systematically mapped to changes in efficiency, and several (including marginal per-capita return, reward features, and payoff feedback mechanisms) are not analyzed for their impact on treatment efficiency.

# 7) Important Limitations

- **Lack of direct outcome data**: No study quantifies or compares average efficiency or related payoff outcomes with and without punishment in a PGG-like context.

- **Limited focus on standard PGGs**: All three papers are at best adjacent in design, with either naturalistic analogues or abstracted N-person games that lack key features needed for direct mapping to the target prediction task.

- **Non-payoff focus**: The exclusive emphasis on behavioral or neural outcomes (e.g., punishment assigned, cooperation rate) rather than group payoff or efficiency means that findings may not transfer directly to efficiency predictions.

- **Design dimension sparseness**: Coverage is sparse or absent for several key game design variables relevant for prediction—especially marginal per-capita return, default contribution framing, feedback mechanisms, and reward dimensions.

- **Theoretical ambiguity**: Theoretical and empirical work highlight factors that can unpredictably moderate cooperation and, by extension, efficiency, but offer little guidance for quantification or systematic effect size estimation.

**Summary**: This literature set provides mechanistic and contextual insights about punishment and cooperation, but lacks direct evidence on efficiency outcomes and comprehensive coverage of relevant design dimensions for downstream predictive modeling of efficiency effects when enabling peer punishment in public-goods-game-like settings.
