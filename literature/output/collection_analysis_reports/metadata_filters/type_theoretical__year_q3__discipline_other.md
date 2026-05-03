# Evidence Base

The literature set consists exclusively of theoretical papers, with no empirical or experimental studies represented. The selected sources offer a mix of game-theoretic modeling (especially evolutionary dynamics), conceptual analysis, and policy or mechanistic arguments about cooperation, punishment, and efficiency in public-goods-game (PGG) environments or adjacent domains. A handful of papers are focused directly on PGGs and payoff/efficiency outcomes, while the majority provide adjacent or contextual insights (e.g., on norms, networks, or evolutionary arguments about cooperation and punishment). Because empirical intervention or direct experimental calibration is missing, most findings are conditional and model-dependent, and generalizability to empirical or laboratory PGGs is limited. Overall, this set is moderately broad regarding underlying mechanisms but comparatively narrow and indirect in terms of empirical grounding for the downstream prediction task.

# Task Relevance

### PGG or Variant
- **Exact relevance:** 3 papers provide direct models and findings for standard or spatial PGGs, especially regarding efficiency and punishment effects (Zhang & Cao, 2020; Zhu et al., 2020; Liu et al., 2019).
- **Close relevance:** 1 paper addresses threshold/variant PGGs (Pedroso, 2021).
- **Adjacent/Weak:** Remaining papers rely on analogues such as collective action problems, social dilemmas, or abstract cooperation models. These have only contextual or conceptual overlap with standard PGGs.

### Punishment or Sanctions
- **Exact relevance:** 4 papers explicitly model or analyze peer/network or legal punishment as a parameterized mechanism (Zhang & Cao, 2020; Zhu et al., 2020; Baker & Choi, 2018; Steimanis et al., 2020).
- **Close/Adjacent:** Several others discuss punishment as a mechanism for sustaining cooperation but do not model it with editable parameters or for direct efficiency effects.
- **None/Weak:** Some papers only mention punishment in passing or as a conceptual background (e.g., Vlerick, 2020; Heath & Rioux, 2018).

### Efficiency or Related Payoff Outcome
- **Exact relevance:** 3 papers offer direct results about efficiency, group payoff, or surplus in the standard sense (Zhang & Cao, 2020; Liu et al., 2019; Baker & Choi, 2018).
- **Adjacent:** A few papers discuss conditions for stable cooperation or redundancy, with only speculative or indirect references to efficiency (Pedroso, 2021; Liu & Yang, 2018).
- **Weak/None:** Most other papers analyze cooperation rates, strategic frequencies, or discuss evolutionary plausibility and conceptual mechanisms without modeling or measuring efficiency.

# Outcomes Measured In The Literature

- **Payoff-Related Outcomes (Exact):**
  - *Group efficiency*—aggregate group payoff/maximum possible (Zhang & Cao, 2020; Liu et al., 2019; Baker & Choi, 2018).
  - *Average payoff* or welfare (Baker & Choi, 2018), stability of high-payoff regimes.

- **Non-Payoff Behavioral Outcomes:**
  - *Cooperation rate*, frequency of cooperators, prevalence of strategies (Zhu et al., 2020; Steimanis et al., 2020; Liu & Yang, 2018).
  - *Norm compliance* and evolution of cooperation (Vlerick, 2020; Handfield & Thrasher, 2019).
  - Conceptual arguments on the spread/maintenance of prosocial behaviors (de Almeida, 2021; Heath & Rioux, 2018).
  - *Redundancy in cooperation* (Pedroso, 2021).

- **Outcomes Not Reported:** In several papers, neither payoff nor behavioral outcomes are quantitatively modeled.

# Main Findings Relevant To Prediction

- **Efficiency Effects of Punishment (Direct Evidence):**
  - **Punishment can promote maximal efficiency** in PGGs but only if punishment is strong relative to group size and returns (Zhang & Cao, 2020). Strong punishment parameters (large fines relative to cost and group size, high MPCR) can transition the population from cycles of defection to stable full cooperation and maximal group payoff.
  - **Prosocial pool exclusion** (excluders pay to block defectors’ access to returns) is theoretically more robust and effective in sustaining high efficiency than peer punishment, especially in infinite well-mixed populations; antisocial exclusion reduces, but does not eliminate, its efficacy (Liu et al., 2019).
  - **Legal (third-party) punishment** is predicted to be more efficiency-enhancing than reputational sanctions, provided the mechanism is accurate and not prohibitively costly. The efficiency effect is particularly strong when litigation outcomes are public and errors are rare (Baker & Choi, 2018).

- **Cooperation Rates/Behavioral Outcomes (Indirect for Payoff):**
  - Peer punishment more effectively raises cooperation rates (not efficiency) than pool punishment in spatial PGGs, when the ratio of fine to cost is high (Zhu et al., 2020).
  - Conditional neutral punishment and government incentives tend to raise the prevalence of cooperation strategies or the stability of positive cooperation, but efficiency or group payoff are not measured (Steimanis et al., 2020; Liu & Yang, 2018).
  - Larger group size, scale, or heterogeneity can dampen the effectiveness of informal peer punishment mechanisms and may require institutionalized sanctions to sustain cooperation (Jagers et al., 2020).

- **Modulators and Conditionalities:**
  - Effectiveness of punishment is highly parameter-dependent: punishment must not be too weak, too costly, or easily circumvented by alternate strategies (e.g., loners/insurance) (Zhang & Cao, 2020; Pedroso, 2021).
  - Information and environmental "harshness" influence the role and necessity of punishment for cooperative redundancy (Pedroso, 2021).
  - Model assumptions (well-mixed populations, infinite size, deterministic versus stochastic dynamics) significantly alter predictions about efficiency gains from punishment (Liu et al., 2019).

- **Theory-Only Arguments:**
  - Punishment, norm enforcement, and prosocial sanctioning are essential in principle for sustaining large-scale cooperation, but empirical or quantitative support is not provided (Vlerick, 2020; de Almeida, 2021; Handfield & Thrasher, 2019).
  - Theoretical critiques caution that models relying heavily on punishment mechanisms may suffer from structural vulnerabilities (e.g., 'greenbeard' problems) limiting generalizability (Heath & Rioux, 2018).

# Prediction Guidance

- **Strongest Guidance:** Derived from direct PGG theory models (Zhang & Cao, 2020; Liu et al., 2019) and theoretical analysis of sanctions (Baker & Choi, 2018).
    - **Expect positive or maximal efficiency gains from enabling punishment,** if and only if the design features (punishment cost, magnitude, MPCR, group size) favor punishers and the mechanism cannot be easily evaded or undercut by alternative strategies ("insurance"/loners).
    - **Prosocial exclusion** mechanisms may yield even higher and more robust efficiency than peer punishment, if available in the design set.
    - **Effect size and direction** hinges on punishment being effective but not overly costly and on the absence of robust alternative free-riding strategies.
    - **Where outcomes are only at the cooperation rate level,** these can act as proxies for likely positive efficiency effects, but the exact magnitude and reliability are unclear (Zhu et al., 2020; Liu & Yang, 2018).
    - **In large, complex, or anonymous environments,** expect the marginal efficiency returns from peer punishment to decline, unless institutionalization or third-party enforcement is present (Jagers et al., 2020; Baker & Choi, 2018).
    - **If efficiency in the control (no-punishment) condition is already maximal,** punishment may yield little to no additional benefit, and could in principle reduce efficiency if it introduces high costs without additional cooperation.

- **Areas of Ambiguity:**
    - No unified empirical effect size or directionality: magnitude and even sign of prediction is design-dependent and model-dependent.
    - Many results are conditional on specific population assumptions or deterministic evolutionary dynamics.

- **Guidance for Prediction Models:**
    - When predicting the efficiency in the punishment-enabled condition, **condition predictions on the control efficiency**, as well as on key design dimensions: player count, rounds, MPCR, punishment cost/magnitude, and presence/absence of exclusion mechanisms.
    - For games with large N, low MPCR, or costly/weak punishment, **expect smaller or nonexistent efficiency gains** from adding punishment.
    - Where only behavioral outcomes are reported, use them as qualitative cues, but be transparent about the uncertainty in mapping to efficiency.

# Design Dimensions Highlighted Across Papers

- **Directly Informed (Parameter-level evidence):**
    - `player_count` (group size): modeled in most PGG theory papers; critical to threshold for punishment effectiveness.
    - `num_rounds`: explicit in most dynamic PGG models.
    - `all_or_nothing`: included in several models impacting strategy space (continuous vs. binary contributions).
    - `mpcr` (marginal per-capita return): featured in all parameterized PGG models as a key modulator.
    - `punishment_cost`, `punishment_tech` (fine structure, peer vs. pool punishment, or institutional/third-party sanctions): directly modeled in 4–5 papers.
    - `reward_exists`: examined in interaction with punishment in at least one model (Liu & Yang, 2018).

- **Indirectly Informed:**
    - `show_other_summaries`, `show_n_rounds`: discussed as information/visibility parameters impacting behavior/cooperation stability (Pedroso, 2021; Baker & Choi, 2018; Jagers et al., 2020).
    - `reward_cost`, `reward_tech`: discussed alongside punishment dimensionality (Liu & Yang, 2018).
    - `default_contrib`: alluded to via framing and information, not a direct model variable.

- **Only Contextually Discussed:**
    - `chat`, `show_punishment_id`: mentioned in passing regarding information/communication effects on cooperation scale (Jagers et al., 2020).
    - `all_or_nothing`: appears as a structural feature, but not as a systematically varied parameter except in a few models.

- **Effectively Missing:**
    - Most papers omit detailed modeling of `chat`, `show_punishment_id`, `default_contrib`, or nuanced reward mechanisms as distinct from punishment.
    - Network structure and spatiality are modeled only in specific spatial PGGs (Zhu et al., 2020; Steimanis et al., 2020), not generalized across all papers.

# Important Limitations

- **No Empirical Evidence:** The entire set is theoretical; no papers provide experimental or observed data for effect calibration, robustness, or generalizability to real-world or laboratory settings.
- **Payoff Outcomes Sparse:** While some models offer explicit predictions about efficiency, many reduce to behavioral outcomes (cooperation rate, prevalence of strategies). The mapping from these to actual efficiency is often indirect and context-dependent.
- **Parameter-Space Gaps:** Key prediction dimensions, such as communication (`chat`), identity revelation (`show_punishment_id`), and nuanced reward structure, are under-explored or absent beyond a conceptual level.
- **Model Dependency:** Findings often rely on specific, sometimes narrow, model assumptions (e.g., infinite well-mixed populations, deterministic updating); departures from these assumptions may yield different predictions.
- **Adjacency Over Exactness:** Many papers are only adjacent or indirectly relevant to standard PGGs, punishment manipulations, or payoff-based outcome prediction.
- **Ambiguity in Effect Sizes:** While theory provides comparative statics and qualitative regimes, the literature does not offer generalizable quantitative estimates for the efficiency effects of punishment.
- **Potential for Disagreement:** There are points of theoretical debate or ambiguity (e.g., greenbeard criticism, sustainability of punishment under anti-social strategies), suggesting prediction models should be cautious and scenario-specific.

---

**Summary Statement:**  
The theoretical literature provides clear *mechanism-based* reasoning for when and why punishment might increase efficiency in public-goods-like environments, but direct, generalizable, and quantitative empirical support for predicting efficiency under a given set of game design dimensions is lacking. The most reliable inference is that punishment can increase efficiency in standard PGGs if its cost and magnitude are well-calibrated relative to group size and returns, but actual outcomes remain highly contingent on specifics of the game architecture and are only weakly supported by non-payoff behavioral results for adjacent settings.
