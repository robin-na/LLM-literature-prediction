# 1) Evidence Base

The paper set consists almost entirely of empirical, experimental laboratory studies, with a minority of framed field experiments. The empirical focus is very strong, with little pure theory but some review/meta-analysis papers and syntheses. Most experiments use variants of the standard linear public goods game (PGG) or closely related social dilemma frameworks, with large experimental literatures testing punishment in many variants. There is a broad sweep across game parameters, punishment mechanisms (peer, centralized, formal, informal, exclusion, etc.), information environments, and cultural/team context.

The papers are highly relevant and relatively comprehensive for the downstream task of predicting efficiency changes resulting from enabling punishment in public-goods-game-like environments across a wide range of design dimensions. Both direct efficiency/payoff outcomes and close proxies (total earnings, welfare, group profit) are frequently measured. This evidence base is notable for both its scale (242 papers) and its depth of direct experimental attention to the target prediction task.

# 2) Task Relevance

### a. PGG or Variant (`pgg_or_variant`)
**Relevance:** `exact`  
The vast majority of papers directly study standard linear PGGs, voluntary contribution mechanisms, common-pool resource games with near-identical structure, and close variants (threshold PGGs, snowdrift, public bads, etc.). Even "close" relevance papers are structured such that their findings are readily mapped to PGG predictions.

### b. Punishment or Sanctions (`punishment_or_sanctions`)
**Relevance:** `exact`  
Almost all experiments involve introducing, varying, or analyzing the effects of punishment or sanctioning mechanisms—including peer punishment, central authorities, ostracism, exogenous fines, pool punishment, exclusion, and other institutions—explicitly as the treatment variable.

### c. Efficiency or Related Payoff Outcome (`efficiency_or_related_payoff_outcome`)
**Relevance:** `exact`  
The majority of papers report group efficiency (payoff as a fraction of theoretical maximum or social optimum), average earnings, surplus, welfare, or similar group-level monetary outcomes as primary measures. Distinction from non-payoff behavioral outcomes is usually clear; contribution rates and punishment frequencies are analyzed separately from payoffs.

# 3) Outcomes Measured In The Literature

## Payoff-Related Outcomes (Directly Used for Prediction)
- **Group efficiency:** Ratio of actual group payoff to the full-cooperation maximum (most common).
- **Group earnings/welfare/surplus:** Total or average monetary payoff per round or over the experiment.
- **Probability of collective success:** In threshold and collective-risk games (e.g., group reaches target).
- **Inequality:** Gini coefficients, group/intra-group earnings disparities.
- **Net payoff after punishment costs:** Sometimes, especially in settings with substantial punishment expenditures.

## Non-Payoff/Behavioral Outcomes (Distinguished)
- **Contribution/cooperation rates:** Not equivalent to efficiency; may increase even as efficiency falls (due to punishment costs).
- **Punishment rates/frequency/intensity:** Used as mechanistic or moderator variables.
- **Norm compliance, targeting/justification of punishment:** Sometimes correlated with efficiency outcomes but not interchangeable.
- **Retaliation/counter-punishment/feuds:** Primarily analyzed as mechanisms for efficiency loss.

# 4) Main Findings Relevant To Prediction

Across hundreds of experimental treatments, the effect of enabling punishment in PGGs on group efficiency is highly **context-dependent and moderated by game design dimensions**. Synthesis of the key findings:

## General Patterns:
- **Punishment almost always increases contributions/cooperation.**  
  However, efficiency increases are **not guaranteed**—direct punishment costs sometimes outweigh cooperation gains.
- **Punishment improves efficiency when:**
  - Punishment is cost-effective (high impact, low cost; e.g., 1:3+ ratio).
  - The game is long enough for punishment use to decline as cooperation stabilizes.
  - Targeting is accurate, anti-social punishment is rare.
  - The punishment institution is well-designed (e.g., centralized, collectively decided, filters out perverse/anti-social uses).
  - Monitoring and information about contributions (and capacities) are accurate and affordable.
  - There are strong/credible mechanisms for punishing only true free riders (not cooperators).
  - Group composition is homogeneous, or heterogeneous but with observable differences (enabling fair norm enforcement).

- **Punishment often reduces or fails to improve efficiency when:**
  - Punishment costs are high or impact is low.
  - There is substantial anti-social punishment, retaliation, or feuding—often due to ambiguity/heterogeneity or social/cultural context.
  - Monitoring information is noisy, incomplete, costly, or ambiguous.
  - Contribution or endowment heterogeneity is present but unobservable.
  - Punishment institutions are decentralized, unfiltered, or have multiple punishment rounds enabling counter-punishment cycles.
  - The threat of punishment is undermined by corruption, bribery, or group favoritism.
  - The baseline efficiency is already high; further improvement is unlikely and costs of residual punishment dominate.
  - The institutional design includes mechanisms that crowd out prosocial norms (e.g., strictly imposed, resented sanctions).

- **Exclusion/ostracism mechanisms:**  
  Repeatedly shown to increase efficiency in PGG-like settings, often more so than costly monetary punishment, especially when actual use is rare but the threat is credible.

- **Rewards versus punishment:**  
  Efficient reward institutions (when cost-effective and well-targeted) can increase efficiency as much or more than punishment, especially when combined or as voluntary, costless approval.

## Moderator and Design Dimension Effects:
- **Institutional design (type of punishment):** Centralized and/or democratically-decided punishment, graduated sanctions, and filtering/censoring of antisocial punishment substantially improve efficiency impact.
- **Punishment technology:** The cost-to-impact ratio is a dominant moderator; high-impact punishment with modest cost is most likely to be efficient.
- **Feedback/information environment:** Full and accurate feedback (and, sometimes, identity transparency) is necessary for positive effects.
- **Game duration:** Longer repeated games allow efficiency losses from initial punishment to be offset by high cooperation and reduced punishment use over time.
- **Group size and structure:** Larger groups, especially with dense networks, benefit more from well-designed punishment; small/sparse groups see weaker effects unless exclusion is allowed.
- **Cultural/contextual moderators:** Societies or groups with a prevalence of antisocial punishment or normative conflict may see no efficiency gain or even losses.
- **Heterogeneity:** Visible and norm-relevant heterogeneity can be managed; invisible or norm-ambiguous heterogeneity tends to destroy efficiency gains from punishment.
- **Communication:** Even minimal communication, or norm signaling (non-binding), often magnifies efficiency effects when combined with punishment.
- **Endogenous institution choice:** Voting/adoption of punishment institutions increases both acceptance and efficiency unless selection is systematically biased.

## Contradictions and Ambiguities:
- **Efficiency effect is highly variable across contexts:**
  - Some papers report large efficiency gains (up to 40% or more over baseline).
  - Others report no improvement or even efficiency loss, especially in the presence of anti-social punishment or poor targeting.
  - Some contradictory findings for similar design dimensions—reflecting sensitivity to details of institution, culture, or group composition.

# 5) Prediction Guidance

The literature **strongly supports a highly conditional predictive mapping** from game design and control efficiency to treatment efficiency with punishment enabled:

- **Control game efficiency is a necessary baseline, but insufficient alone**—the effect of punishment cannot be inferred from control efficiency without taking into account the design dimensions and group context.

- **Directly informed design dimensions for prediction:**
  - `player_count`, `num_rounds`, `mpcr`, `punishment_cost`, `punishment_tech` (e.g., cost-to-impact ratio), `reward_exists`, `reward_cost`, `reward_tech`, `all_or_nothing` (contribution granularity), `show_other_summaries`, `show_n_rounds`, `punishment_tech`, `punishment_exists`, `chat`, `show_punishment_id`, and, in some studies, `default_contrib`.
  - Several studies directly compare efficiency increases for specific parameter combinations (e.g., 4 players, 10 rounds, MPCR=0.4; punishment cost 1, impact 3).

- **Indirectly or contextually informed dimensions:**
  - `default_contrib`, `chat`, `show_punishment_id`.
  - Coordination methods (voting, assignment rules), exclusion options.

- **Effectively missing or under-specified:**
  - Some rare dimensions (e.g., specific forms of communication, less common payoff framing, display options) are less systematically explored or only discussed as context.

- **Quantitative guidance:**
  - Efficiency gains in comparable standard PGGs with peer punishment enabled and an effective cost ratio are typically in the range of 10–40% relative to control, but can be negative if substantial anti-social punishment is present (Fehr & Gächter, 2000; Egas & Riedl, 2008; Herrmann et al., 2008).
  - For **short games (<10 rounds),** efficiency gains are less likely unless punishment is very cost-effective or anti-social punishment is rare.
  - For **longer games (>10–15 rounds),** efficiency gains are more likely as punishment use naturally declines.
  - **Highly effective, centralized, or democratically-filtered punishment** mechanisms have the largest reliably positive effects (Putterman et al., 2011; Ambrus & Greiner, 2019).
  - **Exclusion-based punishment** (ostracism) reliably increases efficiency, especially when costless or rare in actual use (Maier-Rigaud et al., 2010).

- **Correction for special cases:**
  - If information about contributions or endowments is noisy or incomplete, strongly discount or even reverse expected efficiency gains (Grechenig et al., 2010; Nikiforakis et al., 2010).
  - For high baseline efficiency, expect punishment to add little or possibly reduce efficiency (Bühren & Dannenberg, 2021).
  - In environments with known high prevalence of antisocial punishment, expect no efficiency gain or loss (Herrmann et al., 2008).
  - In cases where punishment can be avoided or corruption is possible, efficiency effect may be null or negative.
  - If only weak or non-deterrent punishment is allowed, expect no increase or a decrease in efficiency (Ambrus & Greiner, 2012; Tyran & Feld, 2006).

- **Mapping from control to treatment:**
  - If the control game is inefficient and punishment is well-designed, expect a large positive shift.
  - If the control game is already efficient, no shift or a small negative shift.
  - Consider key design moderators as multiplicative or threshold effects: e.g., add efficiency only if cost-to-impact ratio exceeds a critical threshold, or if group composition is homogeneous and information accurate.

# 6) Design Dimensions Highlighted Across Papers

## Well-Informed Dimensions (many papers with direct payoff evidence):
- **`player_count`** (varies from 2 to 16+; efficiency results often differ across group sizes).
- **`num_rounds`** (short vs. long games; long games allow for delayed efficiency recovery).
- **`mpcr`** (marginal per-capita return is a central parameter; qualitative breakpoints at MPCR=1/n or MPCR<1/n).
- **`punishment_cost`** and **`punishment_tech`** (cost-to-impact ratio is a key predictor of efficiency effect).
- **`punishment_exists`** (binary indicator: almost all studies compare with/without punishment).
- **`reward_exists`**, **`reward_cost`**, **`reward_tech`** (when present; papers often directly compare reward to punishment; reward sometimes outperforms punishment for efficiency).
- **`all_or_nothing`** (continuous vs. binary contributions; some effect on punishment targeting and outcomes).
- **`show_other_summaries`**, **`show_n_rounds`** (feedback on group outcomes and time horizon; relevant for expectations and end-game effects).
- **`chat`/`communication`** (when present, strongly enhances efficiency unless paired with negative group dynamics).
- **`show_punishment_id`** (transparency often moderates anti-social punishment and efficiency).
- **`default_contrib`** (rarely highlighted, sometimes discussed re: nudge effects and default behavior).

## Indirectly or Contextually Discussed:
- **Type/structure of punishment network** (peer, centralized, exclusion, pool, ostracism, etc.; often only coarsely parameterized).
- **Norm clarity and group composition** (less formalized in variable definitions, but repeatedly isolated as moderators).
- **Institution selection mechanisms (voting, endogenous choice)** (sometimes discussed under 'institutional choice' or 'endogenous selection').
- **Cost and probability of monitoring/acquisition of punishment rights**.

## Sparse or Effectively Missing:
- **Direct mapping for complex, hybrid, or rare features (e.g., hybrid reward/punishment, extremely asymmetric games, complicated feedback/history mechanisms).**
- **Meta-parameters about participant characteristics beyond group composition (e.g., cognitive ability, cultural background) are only contextually discussed.**

# 7) Important Limitations

- **Heterogeneity in results:**  
  Efficiency effects of punishment are highly variable across studies with similar design dimensions, reflecting strong moderation by unobserved factors (culture, group composition, anti-social punishment prevalence).
- **Anti-social punishment and norm conflict:**  
  In environments with high rates of anti-social punishment or ambiguous group composition, enabling punishment can decrease efficiency or have no effect—these parameters are difficult to anticipate solely from game design.
- **Punishment design details:**  
  Small differences in punishment institution (e.g., individual vs. democratic, centralized vs. peer, targeting criteria, cost/impact structure, information design) can qualitatively reverse predictions; these are sometimes not fully mapped in predictor variables.
- **Short-term vs. long-term dynamics:**  
  In short games, or early in repeated games, punishment often decreases efficiency; positive effects typically require repeated play for high-cost punishment to recede.
- **Generalizability to population/culture:**  
  Laboratory results may not generalize to field or diverse population contexts, especially when anti-social punishment or cultural differences strongly affect behavior (Herrmann et al., 2008; Suleiman & Samid, 2021).
- **Mapping to field or complex CPR environments:**  
  Closest evidence is for lab PGGs; field and more complex CPR variants show larger variance in outcomes and greater influence of external factors (social identity, resource dynamics, trust).
- **Feedback and monitoring assumptions:**  
  Many positive efficiency effects depend upon full, accurate feedback and effective monitoring—settings lacking this often see reduced or reversed effects.
- **Reward vs. punishment and hybrid institutions:**  
  Studies show reward institutions may outperform punishment for efficiency, but the presence/absence and parametrization of reward is not always standardized in the prediction dimensions.
- **Endogeneity and learning effects:**  
  Institutions chosen via voting or with social learning/history information enhance efficiency, but not all prediction dimensions capture these mechanisms.
- **Ambiguous or imprecisely parameterized dimensions:**  
  Some design details crucial for efficiency prediction (e.g., norm-targeting, anti-social punishment filters, monitoring structure) may not be fully specified in standard predictor variables.

---

**In summary:**  
The experimental literature provides a rich, directly applicable evidence base for predicting how enabling punishment alters efficiency in public-goods-game-like settings, with most design dimensions well represented. However, the payoff effect of punishment is highly contingent and sensitive to several interacting design elements and contextual moderators—particularly punishment cost-effectiveness, institution type, information structure, group composition/homogeneity, and the prevalence of anti-social punishment or norm ambiguity. Efficient prediction requires not just control efficiency and major game parameters, but also attention to these contextual/structural moderators and the possibility of conflicting results in equivalent-seeming games.
