# 1) Evidence Base

The evidence base consists of two papers, both of which are theoretical modeling studies without direct empirical or experimental data. The papers are broad in their consideration of public-goods-like environments and the effects of punishment or sanctions, providing a formal analytical framework rather than measured effect sizes or empirical generalization. Both papers examine social dilemma scenarios related to public goods or common-pool resources with a focus on how punishment affects group efficiency/welfare, but they differ in model specifics and context. There is no direct experimental comparison of efficiency outcomes in controlled and punishment-enabled games, but both provide qualitative and formal theoretical predictions highly relevant to the prediction task.

# 2) Task Relevance

- **pgg_or_variant**:  
  - *Lee & Iwasa (2014)*: `close` – The model is closely related to PGG or common-pool resource games but not an exact PGG instantiation.
  - *Voelkl (2015)*: `adjacent` – The core scenario involves a marketing cooperative with continuous contributions; the structure is related but not a standard PGG.
- **punishment_or_sanctions**:  
  - Both: `exact` – Both papers explicitly analyze punishment/sanctions mechanisms.
- **efficiency_or_related_payoff_outcome**:  
  - Both: `exact` – Both papers focus on efficiency or total group payoff as their primary outcome.

In summary, the literature's direct relevance is strongest for the punishment and efficiency dimensions in PGG-like environments, though the game structures modeled are variants and not canonical PGGs.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:**  
  Both papers measure or theorize about efficiency, group payoff, welfare, or total group earnings—outcomes directly aligned with the task definition of efficiency. These outcomes are not mediated by behavioral variables like cooperation rate, but instead quantify aggregate returns relative to an ideal fully cooperative benchmark.

- **Non-payoff behavioral outcomes:**  
  While strategies for cooperation or defection and the stability of cooperation are discussed in both models, these are only relevant as mechanisms leading to payoff outcomes. Neither paper focuses primarily on direct measurements such as contribution rates, norm compliance, or punishment frequency.

# 4) Main Findings Relevant To Prediction

Synthesizing across the two theoretical papers:

- **Enabling punishment in public-goods-like settings is predicted to increase efficiency relative to no-punishment baselines, provided that punishment is sufficiently strong or graduated, and not excessively severe** (Lee & Iwasa, 2014; Voelkl, 2015).
    - *Lee & Iwasa (2014)* specifically shows that graduated (proportional) sanctions, which scale with the degree or impact of uncooperative behavior, maximize efficiency, especially under realistic conditions (evaluation errors, heterogeneous player sensitivities).
    - *Voelkl (2015)* finds that when punishment is strong enough to fully offset the private gains from uncooperative behavior (defection), cooperation becomes stable and group welfare is maximized. Additionally, redistributing penalties among cooperative members further strengthens this effect.

- **Mechanisms:**  
  Both papers argue that punishment, when correctly calibrated, creates strong incentives to cooperate, indirectly leading to stabilizing cooperation and maximizing efficiency. However, over-severe punishment or punishment mechanisms insensitive to harm may not be optimal, especially in realistic social settings.

- **Parameters and granularity:**  
  The findings are qualitative and do not provide empirical effect-size estimates, nor do they resolve how game design parameters (e.g., number of players, MPCR) condition the magnitude of punishment effects. Instead, they provide explicit (theoretical) conditions under which efficiency improvements are expected.

# 5) Prediction Guidance

Given the theoretical findings:

- **Enabling peer punishment in a PGG-like social dilemma is expected to increase average efficiency relative to a control condition without punishment, conditional on the punishment being strong enough to outweigh the private payoff from defection.**
- **Graduated (proportional) punishment is especially likely to improve efficiency in realistic environments with heterogeneity and evaluation errors, whereas excessively harsh or poorly targeted punishment may not achieve this.**
- **Redistribution of punishment proceeds among cooperators (if present in the game design) could further boost efficiency gains.**
- As the predictions are derived from theoretical rather than empirical studies, this guidance is qualitative: the direction (+) of efficiency change with punishment enabled is well-supported, especially in environments sufficiently similar to those modeled.

However, the models do not provide direct mapping from specific prediction dimensions (e.g., player count, MPCR, number of rounds) to quantitative treatment effects for efficiency. Thus, prediction should be anchored in the control game's efficiency and adjusted upward for the presence (and strength/design) of effective punishment.

# 6) Design Dimensions Highlighted Across Papers

- **Directly informed dimensions:**  
  - `punishment_tech` (both): Central focus; effects of graduated vs. severe/non-graduated punishment are explicit (Lee & Iwasa, 2014).
  - `punishment_cost` (Voelkl, 2015): Modeled as necessary for stable cooperation.
  - `reward_exists` (Voelkl, 2015): Redistribution of penalties (akin to reward) is modeled.
  - `player_count`, `all_or_nothing` (Voelkl, 2015): Present in the model but results do not directly differentiate across different values.
- **Indirectly/contextually discussed:**  
  - Aspects of contribution granularity (`all_or_nothing`), behavioral heterogeneity, and implementation error are mentioned as context but not indexed to concrete design variations.
- **Effectively missing/no coverage:**  
  - `num_rounds`, `chat`, `default_contrib`, `mpcr`, `reward_cost`, `reward_tech`, `show_n_rounds`, `show_other_summaries`, `show_punishment_id`, and most implementation-level details are not addressed or modeled parametrically.

Overall, the papers provide strong theoretical support specifically for the `punishment_tech` dimension (e.g., graduated vs. severe punishment) and for conditions under which punishment is effective in improving efficiency.

# 7) Important Limitations

- **Lack of empirical data:**  
  All findings are theoretical—no experimental or observational validation is provided for effect sizes or for the robustness of the models to real-world contingencies.
- **Papers model PGG-like but not canonical PGG settings:**  
  While highly relevant, neither paper models the full complexity of actual experimental public goods games, possibly limiting the generalizability of precise predictions.
- **Sparse mapping of design dimensions:**  
  Only a subset of the 14 prediction dimensions are directly discussed. Key variables such as player count, MPCR, and round number—often important in empirical settings—lack specific coverage or are embedded only contextually.
- **No quantitative parametric predictions:**  
  The literature provides strong claims on the directionality of punishment effects on efficiency but cannot provide quantitative estimates of efficiency change given specific game parameters.
- **Potential ambiguity in real-world implementation:**  
  The optimality of punishment depends on calibration (graduated vs. severe) and on accurate targeting of sanctions, with real-world behavioral and informational frictions potentially muting the modeled effects.

In summary, while the literature strongly supports the qualitative prediction that enabling well-calibrated peer punishment increases efficiency in PGG-like dilemmas, it lacks empirical grounding and fine-grained parameterization relevant for precise, context-specific efficiency forecasts.
