# 1) Evidence Base

The paper set consists exclusively of theoretical and simulation-based studies, with no empirical or experimental papers. All four papers analyze evolutionary models, strategic dynamics, or agent-based simulations rather than actual behavioral data. With respect to the downstream prediction task, the literature is somewhat specialized—three papers use variants of the public goods game (PGG) explicitly, while one adopts a broader artificial society/resource-sharing model that is PGG-like but not a canonical PGG. The focus is predominantly on efficiency or related group payoff outcomes, not just behavioral measures. The range of punishment mechanisms considered includes classic peer punishment, metanorms (rewarding punishers or punishing non-punishers), forms of generosity or tolerance (generous reciprocity), and structured versus ad-hoc punishment (concerted, severe, rare). The paper set is thus theoretically rich but somewhat narrow empirically, lacking field or lab experimental findings.

# 2) Task Relevance

| Dimension                  | Relevance | Details                                                                  |
|----------------------------|-----------|--------------------------------------------------------------------------|
| `pgg_or_variant`           | exact/close/adjacent | Three papers are exact (modeling n-player PGG or close variants); one is adjacent, using a resource-sharing agent-based simulation. |
| `punishment_or_sanctions`  | exact/adjacent        | All papers analyze punishment; three include explicit punishment or metanorms (exact), one focuses on contingent reciprocity (adjacent). |
| `efficiency_or_related_payoff_outcome` | exact     | All papers focus on group efficiency, total payoff, aggregate wealth, or mean fitness as primary outcomes (not just contribution or cooperation rates). |

- Theoretical focus yields exact or adjacent coverage of the core prediction outcome (group efficiency), with some variation in the operationalization of punishment.
- Only one paper (Jaffe, 2004) is distinctly adjacent for standard PGGs; the rest are exact or very close variants.
- No direct empirical measurement of efficiency effects in experimental or real-world settings.

# 3) Outcomes Measured in the Literature

**Payoff/Efficiency-Related Outcomes (exactly relevant):**
- Total group payoff, aggregate welfare, efficiency ratio, mean fitness, or aggregate wealth (Deng et al., 2012; Kurokawa et al., 2010; Kendal et al., 2006; Jaffe, 2004).

**Non-Payoff Behavioral Outcomes (secondary/adjacent):**
- Rates of cooperation or contribution (mostly for mechanism diagnosis).
- Norm compliance.
- Frequency and targeting of punishment.
- Generosity and retaliation thresholds.

**Distinction Maintained:**
- All four papers report primary results in terms of efficiency or payoff, not merely in behaviors such as cooperation or punishment frequency, though those are sometimes discussed for mechanism elucidation.

# 4) Main Findings Relevant to Prediction

**Positive Effects of Punishment on Efficiency:**
- *Deng et al. (2012):* Predicts that rare, severe, concerted peer punishment can dramatically raise efficiency in PGGs, with effects heightened by larger group sizes and higher punishment severity. Direct quantitative relationships are derived between punishment parameters and efficiency. Standard costly punishment is less efficient than concerted, severe, probabilistic punishment.
- *Kendal et al. (2006):* Shows that either punishment or reward metanorms (rewarding punishers or punishing non-punishers) enable stable, high-efficiency equilibria in PGG-like settings, provided costs are not too high and reward/punishment reinforcement is present. Rewarding punishers is especially robust.
- *Kurokawa et al. (2010):* Generosity in contingent cooperation (tolerating some defection) facilitates the transition to efficient equilibria when cooperation is replacing defection, especially in groups of 4 or more. This effect is adjacent (not explicit peer punishment) but functions similarly as a retaliation/sanction mechanism.

**Ambiguous or Negative Effects of Punishment on Efficiency:**
- *Jaffe (2004):* In agent-based simulations, punishment increases norm compliance and generosity but typically *reduces* aggregate efficiency, unless the punished behaviors yield synergistic societal benefits (i.e., their social impact exceeds punishment costs). Structured societies are somewhat more sensitive to punishment's effect, but the core result holds: in the absence of synergy, punishment generally lowers group wealth.

**Mechanism-level Insights:**
- The efficiency effects of punishment are highly sensitive to *how* punishment is structured:
    - Severity and cost: Severe, shared, and rare punishment is more efficiency-enhancing than frequent, costly, individual punishment (Deng et al.).
    - Metanorms: Supplementary rewards for punishers or punishment of non-punishers sharply raise the chances of reaching efficient equilibria (Kendal et al.).
    - Generosity/tolerance: "All-or-nothing" punishment of defectors is less effective than tolerating one or two defections before sanctioning (Kurokawa et al.).

**Conditionality:**
- Positive efficiency effects are contingent—strongest for certain mechanisms (concerted, severe, or metanorm-reinforced punishment), moderate or negative when punishment is simply costly and frequent.
- Population structure and initial frequencies matter; transition from inefficient to efficient states is influenced by both.

# 5) Prediction Guidance

The theoretical literature compiled here implies that enabling punishment in PGGs or close variants is *not uniformly* efficiency-enhancing. The direction and magnitude of the effect depend critically on:
- The *structure* of the punishment mechanism (severity, cost, frequency, shared versus individual)
- Availability of *metanorm reinforcement* (rewards for punishers or punishments for non-punishers)
- The *group size* (player count) and *cost/benefit* structure (mpcr, punishment cost)

For standard peer punishment (costly, individually administered), the prediction is *ambiguous*—it may promote cooperation but at an efficiency cost, unless some synergy or metanorm is present. Mechanism modifications (rare, severe, concerted punishment or metanorms) robustly produce high efficiency.

Therefore, when predicting *treatment efficiency* given game design and control efficiency:
- If punishment is enabled as *concerted, severe, and rare*: predict a substantial (sometimes dramatic) increase in efficiency over control, especially in larger groups (Deng et al., 2012).
- If punishment is abetted by *rewards for punishers* or *punishment of non-punishers*: predict efficient equilibria are more reachable and stable, even from low-cooperation starting points (Kendal et al., 2006).
- For *standard peer punishment with cost and no metanorms*: prediction is more uncertain—the effect may be neutral or even negative relative to control efficiency (Jaffe, 2004).
- The benefit of punishment is *not automatic*—mechanism details and context (e.g., whether cooperative behaviors create enough surplus to offset punishment costs) are decisive.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**  
- `player_count` (Deng et al., 2012; Kurokawa et al., 2010; Jaffe, 2004): Strong theoretical results on group size effects—larger groups benefit most from concerted or generous sanctioning.
- `num_rounds` (Kurokawa et al., 2010; Jaffe, 2004): Modeled as relevant to iterative sanctioning/reciprocity.
- `all_or_nothing` (Deng et al., 2012; Kurokawa et al., 2010): Explicit attention to binary versus graded contributions.
- `mpcr` (Deng et al., 2012; Kurokawa et al., 2010): Strong consideration of how marginal per capita return governs efficient equilibria.
- `punishment_cost` (All except Kurokawa et al., whose focus is adjacent): Key moderating variable for efficiency tradeoff.
- `punishment_tech` (All except Kendal et al.): Varieties of punishment method/mechanism are central in predictions.
- `reward_exists`, `reward_cost` (Kendal et al., 2006): Explored in metanorm context.

**Indirectly/Weakly Informed:**  
- `show_n_rounds` (Kurokawa et al., 2010; role in theoretical models of repeated games but not empirically varied)
- `reward_tech` (implied in Kendal et al., 2006 but not operationalized with design detail)
- `default_contrib`, `show_other_summaries`, `show_punishment_id`, `punishment_magnitude`, `reward_magnitude`, `chat`: Not discussed or only implied as background; no specific mechanism analysis or experimental data provided on these dimensions.

# 7) Important Limitations

- **No Empirical Evidence:** All studies are theoretical/simulation-based; findings await real-world or lab confirmation and may omit practical implementation challenges.
- **Limited Punishment Mechanisms:** Structured but not exhaustive treatment of peer punishment; "reward" and hybrid mechanisms only appear in one paper in detail.
- **Sparse Reporting on Many Prediction Dimensions:** Most prediction dimensions (e.g., information visibility, chat, contribution framing, punishment/reward magnitude) are barely referenced or missing.
- **Ambiguity in Mechanism Translation:** The relevance of agent-based and evolutionary cultural models to one-shot or short-term experimental settings is uncertain.
- **Context Dependency:** Efficiency outcomes depend on specific cost/benefit configurations and initial population states—broad predictions may not generalize without careful mapping to design specifics.
- **Potential Overstatement of Effects:** Some findings report circumstances where cooperation is evolutionarily stable assuming population mixing, explicit probabilistic adoption, and model-specific rationality, which may diverge from human subjects’ behavior.
- **Negative/Neutral Results Exist:** Not all mechanisms of punishment are efficiency-enhancing—papers explicitly show that some forms of punishment may lower total payoffs.

**In summary:** The literature gives theoretically grounded, mechanism-sensitive guidance on when and how enabling punishment shifts efficiency in PGG-like settings, but should be applied with caution to practical predictions due to structural, empirical, and design-information gaps.
