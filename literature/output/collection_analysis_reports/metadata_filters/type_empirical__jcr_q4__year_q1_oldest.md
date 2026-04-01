# 1) Evidence Base

The paper set comprises 8 empirical, experimental lab studies, with a focus on economic games involving cooperation, punishment, and institutional design. The majority are tightly controlled experiments, primarily studying payoff and behavioral outcomes within various game-theoretic environments. Only one paper (Carpenter et al., 2012) directly investigates standard public goods games (PGG) with punishment and reports on group efficiency. Several papers examine adjacent environments (e.g., sequential bargaining, principal-agent, trust games), some with explicit punishment options. Others address institutional mechanisms (e.g., voting, surveillance cues) or focus on behavioral proxies such as cooperation and norm compliance. This results in a moderately narrow evidence base with only partial direct coverage of the target prediction task: the impact of enabling peer punishment on efficiency in PGG-like environments.

# 2) Task Relevance

Assessment across core relevance dimensions:

- **pgg_or_variant:**  
  - `exact`: 2 papers (Carpenter et al., 2012; Fischer & Nicklisch, 2007)
  - `adjacent`: 5 papers (e.g., bargaining, trust, budget reporting)
  - `none`: 1 paper (Bourrat et al., 2011)

- **punishment_or_sanctions:**  
  - `exact`: 6 papers (explicit punishment mechanisms available)
  - `adjacent`: 2 papers (institutional design or surveillance cues only; no explicit punishment)

- **efficiency_or_related_payoff_outcome:**  
  - `exact`: 2 papers (Carpenter et al., 2012; Fischer & Nicklisch, 2007)
  - `adjacent`: 4 papers (Abbink et al., 2004; Brosig et al., 2004; Chen, 2012; Güth et al., 2007—behavioral proxies only)
  - `none`: 2 papers (Davis & Holt, 1999; Bourrat et al., 2011, only non-payoff outcomes)

As a whole, the literature set offers limited direct coverage of PGGs with peer punishment and efficiency outcomes. Only Carpenter et al. (2012) provides empirical, direct, and high-relevance evidence matching all the prediction task requirements. Other papers offer theoretical or behavioral insights with weaker or adjacent relevance for payoff-based PGG analysis.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes** (directly measuring efficiency, group payoff, or total earnings):
- Measured explicitly in:  
  - Carpenter et al. (2012): Efficiency (payoff), by network structure.
  - Fischer & Nicklisch (2007): Efficiency (payoff), by voting mechanism.
  - Abbink et al. (2004): Efficiency (payoff) in bargaining with punishment.

**Non-payoff behavioral outcomes** (contribution rates, cooperation, punishment frequencies, norm compliance, slack reduction, etc.):
- Measured in the majority of adjacent papers:  
  - Davis & Holt (1999): Cooperation rates.
  - Brosig et al. (2004): Prevalence of equal splits (proxy for efficiency).
  - Chen (2012): Budgetary slack (honesty).
  - Güth et al. (2007): Trustworthiness, propensities to punish.
  - Bourrat et al. (2011): Moral condemnation (no economic behavior).

Few papers report both payoff and behavioral outcomes; most adjacent-literature findings pertain only to behavior, not group payoff or efficiency directly.

# 4) Main Findings Relevant To Prediction

- **Direct PGG+Punishment+Efficiency Evidence:**  
  Carpenter et al. (2012) shows that the impact of peer punishment on efficiency in PGGs is highly dependent on the monitoring/punishment network structure:
    - In *complete* or *well-connected* networks, punishment can increase contributions and efficiency—if punishment costs remain low.
    - In *directed* or *disconnected* networks, punishment is less targeted, more frequent, and often reduces efficiency due to high punishment expenditures.
    - Merely enabling punishment does **not** guarantee higher efficiency; network architecture fundamentally moderates the outcome.

- **Adjacent Environments (bargaining, trust, reporting games):**
    - Abbink et al. (2004): In repeated bargaining with visible punishment, efficiency is **lower** in punishment-enabled treatments due to increased costly punishment, except at extremely low or high rejection rates.
    - Brosig et al. (2004): Communication (especially face-to-face) dramatically increases efficient outcomes (equal splits), overriding the impact of punishment mechanisms.
    - Chen (2012): Punishment (especially when combined with rewards) reduces dishonest behavior (budget slack), but no group payoff reported.
    - Güth et al. (2007): Punishment sustains trustworthiness, but efficiency or payoff consequences are not analyzed.
    - Fischer & Nicklisch (2007): Changing institutional mechanism (voting rule) affects efficiency, but these are not punishment mechanisms per se.

- **Critical Moderators Identified:**  
  - The *structure* and *connectedness* of punishment options.
  - The *cost* of punishment (punisher’s cost) and how visible/usable the punishment option is.
  - The *presence of communication* which can substitute or amplify punishment effects.
  - Institutional context (voting rules in Fischer & Nicklisch, 2007).

- Across studies, **little evidence** supports an unconditional “punishment increases efficiency” prediction—context, especially network and cost, is vital.

# 5) Prediction Guidance

- **Strongest evidence:**  
  Any prediction of punishment-enabled efficiency in PGG-like environments should condition on **network structure**. Only in fully connected or highly integrated networks with relatively low punishment expenditures does enabling punishment tend to increase efficiency (Carpenter et al., 2012).

- **High cost or fragmented monitoring networks** can cause punishment interventions to **decrease** efficiency, even when contributions rise, due to the costliness and frequency of punitive actions (Carpenter et al., 2012; Abbink et al., 2004).

- **Communication presence** can shift outcomes toward high efficiency independently or synergistically with punishment (Brosig et al., 2004).

- **Institutional specifics** (e.g., whether punishment is visible, severity/costs, availability of rewards alongside punishment) must be considered for robust prediction; proxy findings in adjacent environments imply risk in assuming punishment will reliably increase efficiency.

- Using **control (no-punishment) efficiency** as a predictor is useful, but must be combined with the above moderators for valid estimates.

- **Mechanism intuition**: The downstream effect of peer punishment depends as much on how targeted and costly it is, and on the group’s ability to coordinate on fair punishment, as on its mere availability.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed:**
- `player_count` (reported in most studies, key in network effects)
- `num_rounds` (varied, mostly short- to medium-length)
- `all_or_nothing` (several discrete-contribution or binary-choice settings)
- `chat` / `communication` (Brosig et al., 2004; others address its absence/presence as a major moderator)
- `mpcr` (Carpenter et al., 2012; Fischer & Nicklisch, 2007)
- `punishment_cost` (explicit focus in several studies)
- `punishment_tech` (network architecture: who can punish whom)

**Indirectly or contextually informed:**
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id` (revealed but not systematically varied)
- `reward_exists`, `reward_cost`, `reward_tech` (addressed in Chen, 2012, and occasionally combined with punishment, but rarely as an isolated dimension)

**Effectively missing:**
- `default_contrib` (framing: opt-in/opt-out not addressed)
- `reward_magnitude`, `punishment_magnitude` (not systematically varied or directly analyzed in relation to efficiency)
- `show_punishment_id` (identity sometimes visible, but effect not quantified for efficiency)

Network structure of punishment is the most systematically explored design dimension with high direct relevance for efficiency predictions.

# 7) Important Limitations

- **Sparse direct PGG+punishment+efficiency evidence:** Only one paper (Carpenter et al., 2012) empirically and directly matches all three core relevance dimensions for prediction.
- **Adjacent designs dominate**: Many studies involve bargaining, trust, or reporting games, which may limit generalizability to multi-player PGGs.
- **Behavioral ≠ Payoff outcomes:** Most adjacent studies only report cooperation rates, norm compliance, or honesty, not group payoff or efficiency.
- **Key dimensions unaddressed:** Several design dimensions used in the prediction model (e.g., default contribution framing, reward magnitude, full range of visibility treatments) lack experimental coverage in this set.
- **No studies combine full variation across all relevant design factors:** Interactions between, for example, network architecture, punishment cost, and communication are not all empirically mapped.
- **Limited treatment of rewards:** Most focus is on punishment; games with both peer rewards and punishments are rare.
- **Ambiguity in effect directionality:** In several studies (Abbink et al., 2004; Brosig et al., 2004), punishment can reduce efficiency or its effect is reversed by other moderators.

**Conclusion:**  
While some robust empirical principles emerge—especially highlighting the importance of network structure, connectedness, and punishment cost—there is a notable lack of broad, systematic evidence covering the full set of prediction-relevant design features. This makes strong, generalizable predictions from this literature set difficult, and suggests caution in extrapolating findings outside the specific parameterizations and contexts directly studied.
