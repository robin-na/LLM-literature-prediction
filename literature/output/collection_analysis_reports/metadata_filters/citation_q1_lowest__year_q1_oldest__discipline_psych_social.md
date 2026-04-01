# 1) Evidence Base

The paper set includes 16 papers, featuring a mix of empirical (laboratory and field experiments, observational studies) and theoretical papers. The empirical papers employ both standard public goods games (PGG) and close variants, as well as related collective action, trust, and resource dilemma paradigms. Theoretical contributions span mechanism design, repeated games, evolutionary game theory, and networked or spatial social dilemmas.

**Coverage in relation to the prediction task** is broad regarding punishment mechanisms and group cooperation phenomena in social dilemmas, but narrow in terms of direct, quantitative evidence on how peer punishment affects measured efficiency in canonical public goods games. Many papers illuminate adjacent mechanisms or behaviors (e.g., contribution rates, compliance, strategy mix), but fewer report group payoff or efficiency under explicitly varied punishment regimes in standard PGGs.

# 2) Task Relevance

- **`pgg_or_variant`:**  
  - *exact relevance* is limited, with few studies (e.g., English, 2012; Webb & Foddy, 2004) using canonical or near-canonical PGG/VCM designs.  
  - *close relevance* includes resource dilemmas and structured variants.  
  - *adjacent or weaker relevance* covers trust games, spatial and evolutionary simulations, or reputation games that differ substantially from standard PGGs.

- **`punishment_or_sanctions`:**  
  - *exact or close relevance* for punishment appears in a majority of papers (theoretical and empirical), but many focus on authority or institution-driven sanctions, indirect feedback (reputation), or probabilistic/intermittent punishment rather than standard peer punishment.
  - A subset explores absence of punishment (e.g., English, 2012; Rosenbaum et al., 2012), useful for control conditions.

- **`efficiency_or_related_payoff_outcome`:**  
  - Only a few studies report group efficiency or total payoff as defined for prediction (e.g., English, 2012; Corriveau, 2012; Evans & Thomas, 2001), with others focusing on surrogate outcomes (group profit, welfare, resource preservation).
  - Many studies instead report non-payoff behavioral outcomes: contribution rate, cooperation, norm compliance, support for authority, or punishment frequency.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (directly relevant):**
  - *Efficiency* (actual group payoff as a ratio to maximum possible): Reported in a minority of studies (English, 2012; Corriveau, 2012; Evans & Thomas, 2001).
  - *Total group profit/payoff*: Measured or inferred in several theory and empirical studies.
  - *Resource preservation*: Used as a payoff proxy in resource dilemmas (Webb & Foddy, 2004).

- **Non-payoff behavioral outcomes:**
  - *Contribution rates/cooperation*: Most commonly reported (e.g., Loukopoulos et al., 2006; Samid & Suleiman, 2008).
  - *Punishment frequency/assignment*: Behavior tracked as the tendency to sanction.
  - *Norm compliance, authority support, solidarity*: Levels of compliance or support for institutions but not efficiency per se.
  - *Reputation/giving behavior*: Reported in trust/reputation games (Stiff, 2008).

- **Ambiguity/Limitations:**
  - Many studies infer likely efficiency gains from observed behavioral outcomes, but do not provide direct measurement, requiring interpretive caution.

# 4) Main Findings Relevant To Prediction

- **Effect of enabling punishment on efficiency is not uniform:**
  - *Empirical evidence* (Webb & Foddy, 2004): Impact of punishment depends on how sanctions are structured (targeted vs. shared), group heterogeneity, and efficiency definition (resource preservation vs. group profit). Targeted punishment may preserve resources but reduce profit for some.
  - *Theory* highlights non-monotonicity and dependence on multiple conditions. In some models, punishment enables highly efficient cooperation only if it is sufficiently severe (draconian) and credible (Evans & Thomas, 2001; Corriveau, 2012). However, under some circumstances, punishment introduction can cause efficiency to collapse, especially at intermediate monitoring/punishment rates (Whitmeyer, 2004).
  - *Moderation by punishment cost/effectiveness:* Across theory (Heller & Sieberg, 2008; Ziegler, 1997) and empirics (Samid & Suleiman, 2008), punishment boosts efficiency only if costs do not overwhelm coordination benefits; excessive or poorly tuned punishment can reduce total group payoff.
  - *Group size and structure:* Some models (Annen, 2011) support that community enforcement works better with larger groups and require lower discount factors under exogenous, truthful information-sharing.
  - *Repeatedness and expectation management:* In repeated settings with informed and patient players, punishment is more likely to shift groups toward high-efficiency equilibria (Corriveau, 2012; Evans & Thomas, 2001). Manipulating expectations about peer behavior (English, 2012) can sharply alter baseline (control) efficiency, framing context for interpreting punishment effects.
  - *Behavioral spillovers from punishment:* Intermittent or probabilistic punishment increases cooperation in those not directly punished (Loukopoulos et al., 2006), implying potential indirect efficiency gains, though not directly measured in terms of group payoff.
  - *Institutional design and authority:* Authoritative (institutional) sanctioning increases cooperation at moderate cost, but heavy-handedness reduces net gains (Samid & Suleiman, 2008).

Ambiguity and disagreement exist regarding universal benefit: Some findings show positive efficiency effects or conditional improvements, but others warn of possible efficiency collapse or offsetting costs.

# 5) Prediction Guidance

- **When is punishment likely to raise efficiency?**
  - When punishment is credible, observable, and not prohibitively costly (Evans & Thomas, 2001; Heller & Sieberg, 2008).
  - In repeat-interaction or networked-group settings with sufficient player patience and transparent peer monitoring (Corriveau, 2012; Annen, 2011).
  - When the baseline (control) efficiency is low and opportunity for expectation management exists, punishment may have larger marginal effects, but if baseline efficiency is high, added punishment may yield limited or even negative returns (English, 2012 plus theory).
  - Punishment system details (targeted/shared, cost, severity, feedback design) are critical moderators—generic “punishment enabled” vs. “disabled” treatments conflate heterogeneous mechanisms (Webb & Foddy, 2004).

- **When might enabling punishment not improve efficiency (or harm it)?**
  - If punishment costs are high relative to gains from increased coordination, or if punishment induces counterproductive cycles of retaliation or escalates destructive behavior (Samid & Suleiman, 2008; Whitmeyer, 2004).
  - If initial cooperation is already high, or expectations are managed by other means (English, 2012), punishment may yield little further benefit.
  - In one-shot games or those with low player patience, punishment mechanisms are less likely to alter equilibrium outcomes.

- **How should predictors use the literature?**
  - Use design dimensions—most strongly, *punishment cost*, *player count*, *repeatedness* (num_rounds), *punishment mechanism* (tech), and details of information/feedback—to assess likelihood and magnitude of efficiency gains from enabling punishment.
  - Interpret control efficiency (no-punishment) as a key input, as high baseline groups may respond differently than low baseline groups (English, 2012).
  - Avoid assuming monotonic or average-sized gains; rather, consider non-linearity, conditionality, and possible negative impacts.

# 6) Design Dimensions Highlighted Across Papers

- **Directly informed:**
  - `player_count` (**direct**): Group size is experimentally or theoretically manipulated/considered in a majority of papers.
  - `num_rounds` (**direct/close**): Repeatedness and horizon (especially infinite vs. finite) are strong moderators.
  - `punishment_cost`, `punishment_tech` (**direct**): Cost and structure of punishment are central to several findings.
  - `mpcr` (**direct/indirect**): Marginal per-capita return manipulated in some designs.
  - `all_or_nothing` (**direct/indirect**): Discrete/continuous choice affects cooperation dynamics.

- **Indirectly or contextually discussed:**
  - `show_other_summaries`, `show_n_rounds`, `show_punishment_id`: Feedback and transparency sometimes addressed in mechanism-oriented studies (Annen, 2011; Evans & Thomas, 2001).
  - `chat`: Occasionally manipulated (English, 2012; Loukopoulos et al., 2006) but not closely analyzed as a moderator of punishment efficacy.
  - `default_contrib`: Framing effects (opt-in/opt-out) are seldom the focus.
  - `reward_exists`, `reward_cost`, `reward_tech`: Rewards are rarely present; focus is on punishment or sanctions.
  - `punishment_exists`: Central, but mostly as a binary treatment.

- **Effectively missing or absent:**
  - Structured manipulations of reward technology, default contribution framing, or feedback/ID transparency are sparse.
  - Simultaneous variation of multiple dimensions (e.g., joint manipulation of cost, magnitude, tech, ID visibility) is rarely present, limiting interaction effect insights.

# 7) Important Limitations

- **Limited direct measurement of efficiency:**  
  Most studies measure cooperation rates or qualitative compliance rather than group payoff or efficiency as defined in the prediction task, forcing reliance on inference for many findings.

- **Variation in game types and definitions:**  
  Not all studies use canonical PGGs; many employ close variants, resource dilemmas, trust/dyadic games, or spatial/network simulations, which may differ in critical details from the prediction context.

- **Ambiguous or conditional findings:**  
  Literature stresses context sensitivity: punishment’s effect on efficiency depends on design details, group structure, repeatedness, and even initial conditions. In some cases, punishment lowers efficiency.

- **Sparse information for some design dimensions:**  
  Key moderators such as visibility of punishment/reward, detailed feedback mechanics, and reward co-existence are insufficiently addressed, limiting predictive power for designs manipulating these dimensions.

- **Theory heavy on mechanism, light on quantitative prediction:**  
  Theoretical models motivate possibilities and critical thresholds but seldom quantify expected efficiency changes for specific parameter values or predict magnitudes as required in the prediction task.

- **Empirical generalizability:**  
  Field and lab studies may differ systematically, and context effects (culture, expectations, prior experience) can influence baseline efficiency and the effect of punishment, limiting simple extrapolation.

**In summary:**  
While the literature offers substantial theoretical and some empirical support for the idea that enabling peer punishment increases efficiency in public-goods-like environments—conditional on punishment being effective, not overly costly, and incorporated into repeated, transparent interactions—findings are nuanced, context-dependent, and do not yield easy or uniform predictions. Direct, parameterized, efficiency-based results for standard PGGs remain limited, so prediction should rely on careful matching of design dimensions and recognition of the qualitative, sometimes non-monotonic, dependency of punishment effects.
