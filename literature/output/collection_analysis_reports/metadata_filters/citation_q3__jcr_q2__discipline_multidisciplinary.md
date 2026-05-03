# 1) Evidence Base

The paper set consists of two sources: one experimental/empirical paper (Schroeder et al., 2014) and one theory/modeling paper (Toupo et al., 2014). The empirical study uses a lab experiment with a third-party punishment (3PP) game variant but does not employ the standard public goods game (PGG) or directly measure efficiency. The theory paper develops a formal model of evolutionary dynamics in the repeated Prisoner's Dilemma, focusing on cooperation and defection cycles driven by mutation, but does not involve punishment or measure efficiency. Overall, the evidence base is quite narrow and indirect for the task of predicting the efficiency impact of enabling punishment in standard PGG-like games.

# 2) Task Relevance

**pgg_or_variant:**  
- Both papers are **adjacent** rather than exact. Schroeder et al. (2014) uses a third-party punishment game with some overlapping dimensions but it is not a standard PGG. Toupo et al. (2014) analyzes repeated Prisoner's Dilemma, which shares features with PGGs but differs in structure.

**punishment_or_sanctions:**  
- Schroeder et al. (2014): **exact** (examines third-party punishment directly).
- Toupo et al. (2014): **none** (does not discuss punishment or sanctions).

**efficiency_or_related_payoff_outcome:**  
- Schroeder et al. (2014): **adjacent** (mean payoffs mentioned but not analyzed systematically; primary outcomes are behavioral).
- Toupo et al. (2014): **adjacent** (focus on behavioral dynamics, not efficiency or payoffs).

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:**  
  - Schroeder et al. (2014) briefly notes mean payoffs are similar across treatment neighborhoods but does not analyze group efficiency or systematically report on total payoffs.
  - Toupo et al. (2014) does not measure payoffs or efficiency; focuses on strategy frequencies and stability.

- **Non-payoff behavioral outcomes:**  
  - Schroeder et al. (2014) centers on norm compliance, theft rates, expectation of punishment, and willingness to punish, influenced by local trust and perceived norms.
  - Toupo et al. (2014) models the long-term oscillatory dynamics between cooperation and defection at the strategy population level.

# 4) Main Findings Relevant To Prediction

- **Direct empirical findings:**  
  - There is no direct empirical evidence on the impact of enabling peer punishment on group efficiency in a PGG.  
  - In 3PP games, willingness to punish is influenced by environmental trust and local norms (Schroeder et al., 2014). When trust is low and norm violations are perceived as frequent, punishment is both less likely and less expected. Manipulating the perceived social norm increases expectation of punishment, but resulting changes in efficiency or payoffs are not systematically analyzed.

- **Mechanisms and moderators:**  
  - Cost of punishment and trust are identified as moderators for the use and expectation of punishment decisions (Schroeder et al., 2014).
  - Strategic diversity and mutation rates affect the persistence of cooperation in repeated social dilemmas, but not under punishment (Toupo et al., 2014).

- **Payoff outcomes ambiguity:**  
  - While mean payoffs are reported as similar across neighborhoods in Schroeder et al. (2014), this is not related to the enabling/disabling of punishment mechanics, nor is efficiency explicitly analyzed as a function of game parameters.

# 5) Prediction Guidance

Given the evidence, **predictions about treatment efficiency when enabling peer punishment should be made with caution**:

- Empirical results indicate that the effectiveness of punishment (and thus any boost to efficiency) may depend on contextual factors such as baseline trust and perceived local norms. If players expect cheating to go unpunished because of low trust or weak norm compliance, adding punishment options may do little to improve efficiency (Schroeder et al., 2014).

- The subjective and objective cost of punishment can moderate willingness to use it, which in turn affects any possible influence on efficiency. Lower punishment costs are likely to increase use, but the net effect on group payoff is not empirically established.

- There is no direct evidence on how average efficiency changes as a function of design dimensions or baseline control efficiency. Mechanisms and moderators identified (trust, norms, punishment cost) may be relevant covariates but should be used as indirect signals only.

- Theory (Toupo et al., 2014) suggests varied cooperation levels can be sustained through mechanisms other than punishment (e.g., mutation, strategic diversity), providing context but not predictive leverage for punishment’s impact.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed** (explicitly manipulated or analyzed):  
- **player_count** (Schroeder et al., 2014; 3 players),  
- **num_rounds** (both papers),  
- **all_or_nothing** (both papers; binary action choice, not continuous),  
- **punishment_cost** (Schroeder et al., 2014; subjective cost focus),  
- **punishment_tech** (Schroeder et al., 2014; 3PP mechanism),  
- **show_n_rounds** (Schroeder et al., 2014).

**Indirectly/contextually discussed:**  
- **trust** and **local norms** (Schroeder et al., 2014; not a prediction dimension but highly influential),  
- **mutation/strategy diversity** (Toupo et al., 2014; adjacent to mechanism, not a listed design dimension).

**Sparse or missing:**  
- **mpcr**, **chat**, **default_contrib**, **reward_exists**, **reward_cost**, **reward_tech**, **show_other_summaries**, **show_punishment_id**: Not analyzed in either paper.  
- **Efficiency** (as a function of these dimensions) is not systematically reported.

# 7) Important Limitations

- **Lack of exact context:** Neither paper uses a standard PGG with efficiency as a primary outcome, limiting direct applicability.

- **Empirical coverage is superficial for prediction:** Critical dimensions for the downstream prediction (e.g., baseline/control efficiency, range of punishment regimes, group size, MPCR variation) are not systematically varied or analyzed for their effect on efficiency.

- **Payoff outcomes are secondary or unreported:** Both studies focus on non-payoff behavioral outcomes (norm compliance, expectation of punishment, strategy dynamics) rather than group efficiency or total payoffs.

- **No controlled comparison of punishment-enabled vs. punishment-disabled:** The core prediction—how enabling punishment changes average efficiency compared to control—is not empirically addressed.

- **Theory paper lacks punishment analysis:** Toupo et al. (2014) offers only contextual theoretical mechanisms for sustained cooperation, unrelated to punishment.

- **Ambiguity about generalizability:** Effects observed regarding norms, trust, and punishment may not generalize to all PGG-like environments or the parameter spaces relevant for prediction.

**In summary:**  
This literature set provides only **indirect, partial, and contextually limited guidance** for predicting the efficiency impact of enabling punishment in PGG-like games. The main empirical signal is that punishment effectiveness is moderated by trust, perceived norms, and punishment cost, but there is no direct empirical or theoretical basis for quantitative prediction of efficiency outcomes as a function of experimental design parameters.
