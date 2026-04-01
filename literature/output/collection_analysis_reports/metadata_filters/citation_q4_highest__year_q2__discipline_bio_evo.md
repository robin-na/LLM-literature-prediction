# 1) Evidence Base

The paper set analyzed is moderately large (44 papers) and diverse, containing a balance of **empirical lab experiments**, **field/field-lab studies**, and **theoretical/simulation-based papers**. About half of the core papers are directly focused on public goods games (PGG) or very close variants; a significant minority study adjacent social dilemmas (helping games, CPR, etc.) or focus primarily on motivational, reputation, or neural mechanisms. There is a strong foundation of **theory papers** providing formal models and mechanism arguments regarding punishment, efficiency, and cooperation, supported by a substantial body of **empirical experimental evidence** from standard and modified PGGs. The **relevance density is highest for standard linear PGGs with peer or institutional punishment, but tails off outside these contexts**. While the set is broad in terms of theory-mechanism coverage, **it is narrower in providing direct, experimental, payoff-based evidence across all design dimensions**.

# 2) Task Relevance

## pgg_or_variant

- **Exact relevance**: The majority of the papers address linear or threshold public goods games directly (e.g., Gächter et al., 2017; Adami et al., 2016; Hilbe et al., 2015). Some analyze closely related CPR or helping game variants.
- **Close/adjacent relevance**: Several papers use CPR, volunteer’s dilemma, or related economic game frameworks. These provide contextually similar, though not always structurally identical, evidence to standard PGGs.
- **Weak/none**: A minority focus on general behavioral motives, neural mechanisms, or games structurally distinct from PGGs.

## punishment_or_sanctions

- **Exact relevance**: Many studies manipulate peer or institutional punishment and sanctions directly (e.g., Gächter et al., 2017; Hauser et al., 2014; Sasaki & Uchida, 2013).
- **Close/adjacent**: Several analyze reward, exclusion, or other forms of social control, with clear mechanism parallels to punishment, but not always direct manipulations.
- **Weak/none**: A few focus primarily on reward or on mechanistic contexts like reputation that only indirectly relate to punishment.

## efficiency_or_related_payoff_outcome

- **Exact/close**: A substantive subset reports group payoff, efficiency, welfare, or closely linked proxies (e.g., "public good provision" correlated with group earnings; Gächter et al., 2017; Adami et al., 2016).
- **Adjacent/weak**: Many others report predominantly behavioral outcomes—contribution rate, cooperation frequency, punishment assigned, norm compliance—inferring payoff effects only by assumption or theoretical link.
- **None**: Some focus on neural, psychological, or reputational outcomes with no payoff or efficiency data.

**Conclusion:** The literature provides solid coverage for standard PGGs with (peer/institutional) punishment and at least "close" outcome relevance for efficiency or group payoff, but is weaker for non-standard designs or where outcome reporting is behavioral only.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes**: These include group efficiency, total earnings, welfare, surplus, and total payoff as a fraction of the social optimum. Papers such as Gächter et al. (2017), Sasaki & Uchida (2013), Adami et al. (2016), and Gelcich et al. (2013) measure these directly and make explicit claims about punishment's effect on efficiency.
- **Non-payoff behavioral outcomes**: Many papers focus on contribution rate, cooperation frequency, frequency of punishment/reward assignment, norm adherence, or neural correlates of punishment behavior (e.g., Szolnoki & Perc, 2013; Buckholtz et al., 2015). These are recognized as related but **distinct from efficiency**—they may *predict* changes in efficiency but do not measure it directly.
- **Mechanistic/motivational variables**: These outcomes, such as perceptions of fairness, reputation, or neural activation, provide context for why individuals punish or cooperate but are not group payoff outcomes.

# 4) Main Findings Relevant To Prediction

## **General Punishment Effects (Empirical and Theoretical Synthesis)**

- **Punishment usually increases efficiency in standard linear PGGs**: Adding a costly punishment stage reliably raises group efficiency from low/moderate (decaying cooperation) to high/nearly optimal levels when anti-social punishment or severe corruption is absent and when punishment costs are within reasonable bounds (Gächter et al., 2017; Adami et al., 2016; Sasaki & Uchida, 2013; Schoenmakers et al., 2014).
- **Antisocial punishment and corruption are critical moderators**: The efficiency gain is neutralized or reversed if anti-social punishment (punishment of cooperators) is prevalent or if institutional punishment mechanisms can be circumvented via bribery or corruption (Hauser et al., 2014; Muthukrishna et al., 2017).
- **Form of punishment matters**: Social exclusion (costly or not) and conditional punishment are sometimes more robust/effective than standard peer punishment, especially in spatial or heterogeneous settings (Sasaki & Uchida, 2013; Szolnoki & Perc, 2013).
- **Effect magnitudes**: When punishment is effective (not undermined by anti-social use or corruption), near-maximal or substantial improvements in efficiency are observed, often restoring group payoff close to social optimum (Gächter et al., 2017; theoretical models).
- **Context dependence**: The magnitude of the efficiency change is moderated by group size, structure (spatial vs. well-mixed), baseline control efficiency, social capital/norms, punishment cost/effectiveness ratio ("tech"), and the possibility of communication or reputation mechanisms.

## **Limits and Boundary Conditions**

- **Punishment effectiveness decreases with group size and high cost**: Efficiency gains are harder to achieve as groups scale up, or if punishment is very costly relative to its deterrence effect (Hilbe et al., 2015; Rand & Nowak, 2013).
- **Information and visibility amplify efficiency gains**: Effective feedback and observability of contributions/punishment history (reputation effects) strengthen punishment’s pro-efficiency impact (dos Santos et al., 2013; Schoenmakers et al., 2014).
- **Baseline efficiency moderates ceiling effect**: If control (no-punishment) efficiency is already high due to other mechanisms (leadership, norms), the additional improvement due to punishment will be smaller (Gelcich et al., 2013; Henrich et al., 2015).
- **Heterogeneous environments** (e.g., variable punishment cost or group composition) can enhance punishment’s effectiveness or moderate overall efficiency outcomes (Przepiorka & Diekmann, 2013; Chen & Perc, 2014).

# 5) Prediction Guidance

## Direct implications for the downstream prediction task:

- **If control (no punishment) efficiency is low and standard peer punishment (with no major corruption/anti-social use) is enabled, predict a large increase in treatment efficiency—often to near social optimum—especially in group sizes ≤5, with moderate punishment costs, and sufficient rounds for effects to manifest** (Gächter et al., 2017; Adami et al., 2016).
- **If anti-social punishment or bribery (corruption) is possible, predict little or no efficiency gain—and possibly a reduction relative to control**, even with standard punishment parameters (Hauser et al., 2014; Muthukrishna et al., 2017).
- **If the punishment design is highly inefficient (high cost:impact ratio), or if group size is large, the efficiency increase will be smaller, possibly negligible** (Rand & Nowak, 2013; Hilbe et al., 2015).
- **If social capital, pre-existing cooperative norms, or reputational/observability mechanisms are strong, efficiency gains from introducing punishment may be smaller ("ceiling" effect) or more persistent** (Gelcich et al., 2013; dos Santos et al., 2013).
- **Detailed mapping of punishment technology (cost, impact, visibility), possibility of reward, available information, and group structure is needed for calibrated predictions**; effects are quantitatively sensitive to these design features (Sasaki & Uchida, 2013; Schoenmakers et al., 2014; Szolnoki & Perc, 2013).

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**  
- `player_count`: Addressed in most empirical/theoretical PGG papers; group size effects discussed for efficiency, baseline cooperation, and punishment efficacy.
- `num_rounds`: Explicit in lab studies and models; key for observing cooperation decay/regeneration.
- `mpcr`: Treated as “multiplier,” “enhancement factor,” or “synergy parameter”; critical in all theory and most experimental papers.
- `punishment_cost`, `punishment_tech`: Core in mechanism papers; cost-to-impact (fee:fine) and form (peer/institutional/exclusion/conditional) heavily modeled and manipulated.
- `punishment_exists`: The main treatment variable in almost all directly relevant studies.

**Individually or Indirectly Discussed:**
- `all_or_nothing`: Some designs use binary (all or nothing) vs. continuous contributions; effect on punishment efficacy is discussed but not always isolated.
- `chat`: Manipulated in a subset; communication tends to boost baseline cooperation and interacts with punishment, but not universally modeled.
- `default_contrib`: Rarely directly manipulated; a few papers mention framing effects or opt-in/opt-out default consequences.
- `reward_exists`, `reward_cost`, `reward_tech`: Addressed primarily in papers comparing reward and punishment or studying anti-social rewarding; not as systematically covered as punishment.
- `show_other_summaries`, `show_punishment_id`, `show_n_rounds`: Feedback and visibility mechanics are highlighted in some studies as key moderators but not always isolated or experimentally varied.

**Effectively Missing or Contextual:**
- Some features like `default_contrib`, `show_punishment_id`, `show_n_rounds` are mostly contextually discussed or inferred, not systematically studied.
- Most “contextual” dimensions are discussed as potential moderators, but cross-paper empirical synthesis is rarely possible.

# 7) Important Limitations

- **Outcome restriction**: Several “relevant” papers rely on behavioral proxies (contribution/punishment rates) rather than direct efficiency or payoff outcomes. This means efficiency predictions often involve some inference or assumption rather than reporting a measured outcome.
- **Boundary conditions for anti-social punishment and corruption**: The strong efficiency gains reported for punishment assume that punishment is used pro-socially. Where anti-social punishment or corruption arises, empirically validated efficiency predictions are either negative or highly variable, but the boundary conditions for these behaviors are not always clearly mapped to the game design dimensions.
- **Limited design dimension coverage**: Not every prediction dimension is systematically isolated or manipulated. Some factors (like information structure, default contribution framing, or visibility of punishment) are highlighted as important in select papers but are not universally or orthogonally tested.
- **Extrapolation for large player counts or complex institutions**: Most experimental and simulation studies use small groups (n ≤ 5). Predictions for large groups or complex institutional arrangements rest mainly on theory/simulation, which may not fully capture real-world dynamics.
- **Interaction with baseline efficiency**: Depending on the presence of strong existing social capital, leadership structures, or reputational mechanisms, the effect size of adding punishment is likely reduced, but there is limited quantitative guidance for these interaction effects.
- **External validity**: Field evidence (e.g., Gelcich et al., 2013) indicates that effectiveness of punishment can depend on group cultural norms and pre-existing cooperative structures, challenging laboratory generalization.
- **Quantitative effect size calibration**: While the direction of punishment's effect on efficiency is generally clear under standard, well-behaved conditions, **precise quantitative predictions for new parameter settings require caution**, especially when important moderators (antisocial punishment, corruption, group heterogeneity) are present.

---

**Summary**  
*This literature set gives strong, mostly positive support for the expectation that enabling peer punishment in public-goods-game-like environments substantially increases efficiency, but only when antisocial misuse or corruption are ruled out. The predictive value is highest for standard linear PGGs with small-moderate group size, moderate punishment cost/effectiveness, and no rewards or major confounds. There is limited coverage of some design dimension interactions, and caution is warranted when extending predictions beyond empirically tested regions, designs with efficiency already near ceiling, or environments likely to foster antisocial punishment or corruption.*
