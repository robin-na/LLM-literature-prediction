# 1) Evidence Base

The paper set comprises six papers, with a mixture of four theoretical works (Deng et al., 2012; Kurokawa et al., 2010; Kendal et al., 2006; Huang, 2007), one agent-based simulation (Jaffe, 2004), and one empirical lab experiment (Brosig et al., 2004). The empirical base is therefore heavily weighted toward theory and simulation, with only one direct experimental study. The set is relatively broad with respect to punishment mechanisms and settings (covering standard PGGs, modified public-goods environments, and adjacent strategic games), but is narrow in direct empirical coverage of the canonical public goods game (PGG) with payoff measurement. Notably, the most process-detailed and payoff-focused comparative results are theoretical or based on simulations. Evidence for treatment efficiency primarily comes from model-based predictions rather than repeated direct observation.

# 2) Task Relevance

Task relevance is assessed along three target-relevance dimensions:

- **pgg_or_variant**:  
  - Three papers are exactly on the PGG or direct variants (Deng et al., 2012; Kurokawa et al., 2010; Kendal et al., 2006).  
  - Three are only adjacent: two extend to related social dilemmas or bargaining environments (Jaffe, 2004; Brosig et al., 2004; Huang, 2007).
- **punishment_or_sanctions**:  
  - Four papers examine punishment or sanctioning with exact relevance (Deng et al., 2012; Kendal et al., 2006; Jaffe, 2004; Brosig et al., 2004; Huang, 2007).  
  - Kurokawa et al. (2010) is adjacent, modeling sanctioning via conditional cooperation rather than explicit costly punishment.
- **efficiency_or_related_payoff_outcome**:  
  - Four papers have exact relevance, reporting or modeling group efficiency, welfare, or total payoff (Deng et al., 2012; Kurokawa et al., 2010; Kendal et al., 2006; Jaffe, 2004), but their outcome meanings and metrics are not always aligned.
  - Two papers (Brosig et al., 2004; Huang, 2007) are adjacent: they focus on non-payoff behavioral outcomes such as cooperation, trust, and norm compliance, which are only proxies for efficiency.

Overall, direct coverage for the prediction task—predicting changes in efficiency following the introduction of punishment in PGG-like games—is moderate but not complete. There is reasonable coverage for PGGs and explicit efficiency outcomes in theoretical papers, but limited empirical/lab evidence and incomplete mapping of all relevant game dimensions.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (efficiency, welfare, aggregate wealth, group earnings, total coins, mean fitness)**:  
  - Four papers (Deng et al., 2012; Kurokawa et al., 2010; Kendal et al., 2006; Jaffe, 2004) explicitly analyze payoff-based outcomes, either theoretically or through simulations. These include group efficiency as the ratio of achieved payoff to full cooperation payoff, aggregate wealth, or “mean fitness.”
- **Non-payoff behavioral outcomes (contribution rate, norm compliance, trust, cooperation rate, punishment frequency)**:  
  - Two papers (Brosig et al., 2004; Huang, 2007) primarily track behavioral response variables but discuss how these might relate to efficiency. For instance, Brosig et al. (2004) analyzes equal splits (not total group payoff), and Huang (2007) models the prevalence of cooperative behavior but not overall payoff.

There is some blending of the outcome types in interpretation, but direct, empirical group-level payoff measurement is rare outside the theoretical models and simulations.

# 4) Main Findings Relevant To Prediction

## Synthesis Across Papers

- **Enabling punishment mechanisms generally increases group efficiency in PGGs or public-goods-like games compared to no-punishment, but this is highly dependent on the structure, cost, and effectiveness of punishment** (Deng et al., 2012; Kendal et al., 2006).
    - **Severe, concerted, and rare punishment** (shared, infrequent, high-magnitude): Maximizes the efficiency gains, especially in large groups with high punishment effectiveness and moderate to low cost (Deng et al., 2012).
    - **Metanorms (rewarding punishers or punishing non-punishers)**: Further boost the likelihood of efficiency gains, especially if costs of punishment/reward are low and initial frequencies of punishers are low (Kendal et al., 2006). Reward-based reinforcement (paying those who punish) is particularly effective.
    - **Generosity/tolerance in sanctioning**: In environments where repeated contingent cooperation (not explicit costly punishment) is used, efficiency is maximized when cooperators are sufficiently tolerant before retaliating; “reactive” generosity supports transitions to high-efficiency states, especially for group size ≥4 (Kurokawa et al., 2010).
    - **Communication**: Strong moderator. Allowing preplay communication (especially face-to-face) increases cooperation and leads to more efficient outcomes than punishment alone; in absence of communication, punishment parameters (cost, effectiveness) are more influential (Brosig et al., 2004).
    - **Punishment cost and structure**: High punishment costs or lack of synergistic group benefits can make efficiency fall below control (punishment-free) conditions, with discipline generating more norm compliance but costing more than gained (Jaffe, 2004).
    - **Effectiveness of punishment, detection, and norm crowding**: Increased institutional effectiveness raises behavioral cooperation but may undermine intrinsic motivation, which might not always translate to net efficiency gains (Huang, 2007).

## Conflict & Ambiguity

- **Positive effect on efficiency** is predicted by several models/theoretical treatments (Deng et al., 2012; Kendal et al., 2006) and suggested under contingent cooperation (Kurokawa et al., 2010).
- **Negative or ambiguous effect** is found in agent-based simulations (Jaffe, 2004), where costly punishment reduces net efficiency in absence of additional synergistic benefits from compliance.
- **Behavioral increases in cooperation** do not always equate to efficiency improvements; for instance, more norm compliance may be achieved at a net group cost (Jaffe, 2004; Huang, 2007).

# 5) Prediction Guidance

- **Expect increased efficiency relative to control** when punishment is effective, infrequent but severe, and/or when secondary rewards for punishers are enabled (Deng et al., 2012; Kendal et al., 2006). These mechanisms help overcome free-rider stability, especially in larger groups.
- **Be cautious with costly, frequent, or inefficient punishment**, particularly when punishment expenditures outweigh the gains from increased contributions (Jaffe, 2004). In these cases, efficiency may actually decrease relative to control.
- **Generosity/tolerance in repeated games** can support efficiency gains during the establishment of cooperation, but does not maintain high efficiency without explicit punishment (Kurokawa et al., 2010).
- **Communication should be considered** a critical moderator, especially if enabled, potentially boosting efficiency above what punishment alone achieves (Brosig et al., 2004).
- **When predicting using game design parameters:**  
    - Give extra weight to dimensions that increase the magnitude and coordination of punishment, lower the cost for punishers, increase group size, or add reward (secondary sanctioning) for punishing.
    - Reduce expected efficiency if high punishment costs or lack of direct surplus from norm compliance are present.
    - Treat presence of communication as potentially equally or more important than punishment.
- **If only non-payoff behavioral outcomes are available**, infer that higher cooperation or norm compliance might correspond to higher efficiency, but only cautiously, and primarily when the cost side is well understood.

# 6) Design Dimensions Highlighted Across Papers

- **Directly Informed Dimensions**:  
    - `player_count` (group size): Explicitly modeled in theory/simulation (Deng et al., 2012; Kurokawa et al., 2010; Jaffe, 2004).
    - `num_rounds`: Considered in repeated game models (Kurokawa et al., 2010; Jaffe, 2004).
    - `mpcr` (marginal per-capita return): Modeled in several theories (Deng et al., 2012; Kurokawa et al., 2010; Huang, 2007).
    - `all_or_nothing`: Distinguishes discrete versus continuous choices (Deng et al., 2012; Kurokawa et al., 2010; Jaffe, 2004).
    - `punishment_cost` and `punishment_tech`: Central to almost every theoretical and simulation study.
    - `reward_exists`, `reward_cost`: Explicitly analyzed in models featuring metanorms (Kendal et al., 2006).
    - `chat`/communication: Focus of Brosig et al. (2004).
- **Indirect/Partial Evidence**:  
    - `show_n_rounds`, `show_other_summaries`: Contextual discussion in Kurokawa et al. (2010), adjacent in behavioral papers.
- **Sparse or Missing Evidence**:  
    - `default_contrib`, `show_punishment_id`, `reward_tech`, `reward_magnitude`, and summary/feedback mechanics are not specifically investigated.
    - The joint manipulation of multiple design parameters (e.g., presence/absence of communication *and* reward *and* punishment features) is not systematically covered.
- **Context Only**:  
    - Some dimensions (such as `default_contrib` or feedback/visibility) are only contextually mentioned or implied by the baseline game and are not empirically or theoretically varied.

# 7) Important Limitations

- **Empirical evidence is limited**: The vast majority of results come from theory or simulation; only one paper provides direct lab evidence, and it is not a canonical PGG.
- **Outcome definitions and measurement** are inconsistent: Payoff-based efficiency is modeled differently across papers, and some rely only on behavioral proxies (cooperation rates, norm compliance), not on actual group payoffs.
- **Generalizability of findings**: Several theoretical results make idealized assumptions (well-mixed infinite populations, repeated games with exogenous generosity thresholds, or stylized cost structures) that may not translate directly to experimental or real-world PG games.
- **Effects of communication and reward**: While communication and metanorms are shown to matter, empirical variation across these factors in PGGs is sparse within this set.
- **Design gaps**: Important prediction dimensions such as `reward_tech`, `show_punishment_id`, and certain implementation details are missing or untested.
- **Conflicting results**: Some papers report net efficiency losses upon enabling punishment; others predict or simulate gains—the effect is not uniform and is mediated by parameter regimes (e.g., cost/benefit balance, group size, punishment structure).
- **Ambiguity of behavioral outcomes**: Where only behavioral increases are reported, efficiency impacts are necessarily speculative.
- **Lack of statistical/quantitative predictive models**: Most theory papers offer qualitative or parameter-bound results, but not empirical predictive functions for downstream use.

In sum, the literature base provides a mix of strong theoretical guidance and some conflicting simulation results, with low direct empirical evidence and major gaps in the variation and joint analysis of critical treatment features. For downstream prediction, expect robust positive efficiency effects from well-structured punishment (concerted, severe, reward-reinforced), but allow for negative or null effects with costly, uncoordinated, or frequent punishment, and note the absence of data on several intervention design parameters.
