# 1) Evidence Base

The paper set consists primarily of empirical experimental studies (mostly lab-based, with a few field/observational studies) examining social dilemmas, public goods games (PGG), related group cooperation settings, and mechanisms such as punishment, sanctions, voting, contracts, and reputation. The coverage of game design dimensions is moderately broad, with player_count, num_rounds, mpcr, all_or_nothing, punishment_cost, and related dimensions discussed or implemented in several studies. However, direct empirical evidence on treatment efficiency effects from enabling punishment in standard PGGs is sparse, and the treatment of punishment mechanisms and payoff outcomes varies considerably in precision.

The set features a small number of papers offering direct, quantifiable efficiency comparisons in PGGs with and without punishment, while most provide only adjacent or indirect evidence—often focusing on non-payoff behavioral outcomes such as cooperation/contribution rates, punishment frequencies, or mechanism choice. Theoretical arguments and mechanistic insights are present but are outnumbered by empirical findings. Overall, the evidence base is somewhat narrow for the exact downstream task of predicting efficiency changes from punishment in PGGs, although it illustrates a spectrum of design features and contextual variables.

# 2) Task Relevance

**pgg_or_variant:**  
- *Exact:* Several studies use standard linear PGGs or very close variants (Fehr et al., 2010; Fischer & Nicklisch, 2007; English, 2012).
- *Close/Adjacent:* Many others employ social dilemmas structurally similar to PGGs (resource dilemmas, prisoner's dilemma, coalition games, trust games), though not always with the full suite of PGG features.
- *Weak/None:* A few studies analyze non-PGG games (Dictator, Joy-of-Destruction), yielding only weak or contextual relevance.

**punishment_or_sanctions:**  
- *Exact:* Punishment as a costly, explicit action is implemented in several experiments (Fehr et al., 2010; Webb & Foddy, 2004; McEvoy, 2012; Samid & Suleiman, 2008; Klempt, 2012).
- *Close/Adjacent:* Some papers examine indirect sanctions (reputation, third-party monitoring, contracts) or informal/animal analogs, but not always in the standard PGG context.
- *None:* A subset lacks any sanctioning mechanism or relevant manipulation.

**efficiency_or_related_payoff_outcome:**  
- *Exact:* Group efficiency, payoff, or welfare is a primary (measured/compared) outcome in a handful of studies (Fehr et al., 2010; Fischer & Nicklisch, 2007; Webb & Foddy, 2004; Bruttel & Eisenkopf, 2012).
- *Adjacent/Weak:* Most studies focus on behavioral outcomes (contribution/cooperation rates, punishment frequency, etc.) with only inferred or unmeasured implications for efficiency.
- *None:* Some provide no data or only theoretical argument about payoff-based outcomes.

**Summary:** The literature incorporates several papers directly relevant to the prediction task, but substantial portions of the set are only adjacent or provide indirect evidence for the core question: the effect of enabling punishment on group efficiency in PGG-like environments.

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes:**  
- Measured group efficiency or total welfare/payoff in both control and punishment-enabled conditions is available primarily in Fehr et al. (2010), Fischer & Nicklisch (2007), Webb & Foddy (2004), and Bruttel & Eisenkopf (2012).
- In other works (e.g., McEvoy, 2012; Samid & Suleiman, 2008; Loukopoulos et al., 2006) efficiency is not measured directly, and any claims about efficiency stem from inferences based on observed cooperation or behavioral patterns.

**Non-Payoff Behavioral Outcomes:**  
- The majority of studies report changes in contribution rate, cooperation rate, norm compliance, punishment frequency, authority support, or similar processes that are valuable for mechanism understanding, but not synonymous with efficiency.
- Some studies elaborate on the motives for punishment, social context, or neurobiological responses, which offer insight into individual and structural moderators rather than direct efficiency effects (Klempt, 2012; Kodaka et al., 2012).

**Distinction:** Most of the literature emphasizes behavioral responses to punishment, with relatively few studies providing the direct payoff comparison necessary for precise efficiency prediction.

# 4) Main Findings Relevant To Prediction

- **Punishment Often Increases Contribution but Can Lower Efficiency in Short PGGs:**  
  Enabling peer punishment in short-run PGGs (e.g., 10 or fewer rounds) usually raises cooperation/contribution rates but reduces group efficiency due to the costliness of punishment; group payoffs typically drop below the control (Fehr et al., 2010).
- **Positive Efficiency Effects in Longer Games or with Reputation Mechanisms:**  
  In long-horizon games (e.g., 50 rounds) or where reputation/endogenous institution choice is enabled, punishment increases both cooperation and efficiency, ultimately surpassing the control game on payoff (Fehr et al., 2010).
- **Design of Punishment System Moderates Efficiency Impact:**  
  The structure (e.g., targeted vs. shared punishment) affects whether punishment increases resource preservation or group profit—targeted punishment may conserve resources, but shared punishment may yield higher group payoffs (Webb & Foddy, 2004).
- **Cost of Punishment Is Critical:**  
  Excessive or poorly calibrated punishment costs can undermine efficiency even when cooperation rises, as the net loss from punishment exceeds the gains from greater contributions (Samid & Suleiman, 2008).
- **No Universal Effect:**  
  The effect of enabling punishment is context-dependent, with mixed or heterogeneous results across different designs.
- **Indirect or Contextual Moderators:**  
  Social context, expectation management, and feedback mechanisms can have large effects on behavioral outcomes (cooperation), but their translation to efficiency gains depends on the underlying game payoffs (English, 2012; Loukopoulos et al., 2006).
- **Behavioral Outcomes≠Efficiency:**  
  Increased contribution or cooperation does not guarantee higher efficiency in settings where punishment is costly or resources are destroyed in the sanctioning process.

# 5) Prediction Guidance

The literature advises caution in predicting that enabling peer punishment will increase efficiency in public-goods-game-like environments:

- **Short Games (≤10 rounds):**  
  The net effect of punishment is usually to *lower* efficiency compared to control, due to cost of punishment exceeding the benefit from increased cooperation (Fehr et al., 2010). Predicted treatment efficiency should often be lower than observed control efficiency, unless other efficiency-promoting mechanisms are present.
- **Longer Games/With Reputation or Endogenous Choice:**  
  Enabling punishment may yield higher efficiency relative to control, especially if social norms become established and/or the opportunity for repeated interaction allows delayed positive payoff effects to accumulate.
- **High Cost or Excessive Punishment:**  
  Punishment that is too costly or excessively applied can overwhelm benefits, reducing efficiency even if cooperation increases (Samid & Suleiman, 2008).
- **Punishment System Structure Matters:**  
  Mechanisms providing clear, credible, and appropriately targeted punishment improve prospects for efficiency gains (Webb & Foddy, 2004; McEvoy, 2012).
- **Indirect Evidence Only** for cases without direct efficiency data: Where only behavioral outcomes are available, efficiency changes must be inferred, and caution is advised. Not all cooperation gains convert to efficiency gains.

**Design dimensions most influential for prediction (from this literature):**  
- `num_rounds` (game length/time horizon)
- `punishment_cost` and related punishment structure
- `punishment_tech` (implementation and targeting rules)
- Presence of reputation or endogenous institution features (even if not directly coded among the 14 dimensions)
- Baseline (control) efficiency

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**
- `player_count`: Frequent manipulation/observation; moderates group dynamics.
- `num_rounds`: Critical for determining whether punishment can or cannot yield long-run efficiency gains.
- `mpcr`: Often specified, moderates marginal return and thus the incentive structure.
- `all_or_nothing`: Sometimes manipulated, affecting strategic options.
- `punishment_cost`: Central to many studies; directly shapes efficiency tradeoffs.
- `punishment_tech`: Structural features (targeted vs. shared; commitment mechanisms) are a major moderator.
- `show_n_rounds`: Manipulated in some studies and can influence planning behavior.
- `show_other_summaries`: Present in some designs, relevant for expectation management.

**Indirectly Informed / Contextual:**
- `chat`: Included in some studies, generally found to promote cooperation rather than interact directly with punishment.
- `show_punishment_id`: Occasionally noted in observational animal studies (reputation/awareness) and in reputation mechanisms.
- `default_contrib`: Rarely a central focus.
- `reward_exists`, `reward_cost`, `reward_tech`: Seldom enabled in these papers; evidence on rewards is largely missing.

**Effectively Missing:**
- Most studies lack manipulation or focused discussion of the reward dimensions.  
- The detailed implementation of punishment and technological aids (beyond cost and targeting) is often underspecified.
- There is very little evidence on opt-in/opt-out framing (`default_contrib`), and little about interface/feedback manipulations not directly pertaining to game payoffs or efficiency.

# 7) Important Limitations

- **Sparse Direct Efficiency Data for PGGs with Punishment:**  
  Few studies report head-to-head comparisons of group efficiency/payoff in punishment-enabled vs. control PGGs for varied design parameters.
- **Predominantly Behavioral Outcomes:**  
  Many studies infer likely efficiency effects from observed contribution/cooperation rates rather than actually measuring group payoffs—this risks overestimating positive effects where costly punishment is prevalent.
- **Limited Generalizability:**  
  Findings from adjacent or analogous dilemmas (e.g., coalition, resource, or trust games) may not generalize to standard PGGs with different structures, especially if the mechanism for sanctioning, group size, or payoff structure differs.
- **Inadequate Reward Dimension Evidence:**  
  Little to no evidence on how reward mechanisms (and their interaction with punishment) affect efficiency in these settings.
- **Interaction Effects Under-Explored:**  
  Effects of combining multiple design features (e.g., punishment and chat, or visible punishment ID plus reputation) are not systematically explored.
- **Ambiguity and Heterogeneity:**  
  Where multiple studies do address similar settings, disagreement and context dependence are common; efficiency effects of punishment are not universal and depend on design interaction (e.g., time horizon, cost).
- **External Validity and Realism:**  
  The majority of experiments are laboratory-based, using monetary stakes and student populations, limiting direct extrapolation to field or high-stakes environments.

**Conclusion:**  
While the paper set provides a foundational, though incomplete, empirical basis for predicting the effect of enabling peer punishment on group efficiency in public-goods-game-like environments, its limited direct evidence and contextual gaps require predictions to be tailored with significant caution. The most robust moderate predictors, supported by the literature, are the number of rounds (a proxy for time horizon), the actual cost and structure of punishment, and the starting efficiency of the control condition.
