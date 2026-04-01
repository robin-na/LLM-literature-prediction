# 1) Evidence Base

The paper set is composed primarily of empirical experimental studies (laboratory, field, and observational), with a strong focus on lab-based investigations. The literature is relatively broad in terms of methods, participant populations, and game-like settings, but narrows substantially for the downstream prediction task—specifically, forecasting efficiency effects of enabling peer punishment in public-goods-game (PGG) environments based on detailed design features and control efficiency. Only a minority of studies focus on standard PGGs with efficiency (payoff-based) outcomes and include directly relevant experimental manipulations of punishment institutions. Many papers analyze adjacent or related settings (e.g., trust games, prisoner's dilemmas, CPR games, contest games, or animal coordination games), often emphasizing behavioral or psychological outcomes rather than efficiency or group payoff. There is only modest attention to formal theoretical modeling; nearly all insights are empirically grounded.

# 2) Task Relevance

**a. PGG or Variant (`pgg_or_variant`)**  
- **Exact relevance**: Approximately one-fourth of the papers use canonical or near-canonical PGGs (e.g., group contribution settings with continuous or all-or-nothing choice, voluntary contribution mechanisms, and explicit MPCR).
- **Close/Adjacent**: Many papers use CPR games, trust games, contest games, or n-person prisoner's dilemmas—these share key incentive structures but are not strictly PGGs.
- **Weak/None**: Multiple studies use allocation, ultimatum, or animal games with no direct mapping to PGG logic.

**b. Punishment or Sanctions (`punishment_or_sanctions`)**  
- **Exact**: Numerous papers manipulate incentive mechanisms involving explicit punishment stages (peer or centralized, monetary or symbolic, varying cost/impact ratios).
- **Close/Adjacent**: Some use reward-based systems, nonmonetary or reputation/information-based disapproval, or rely on theoretical threats of punishment rather than implemented mechanisms.
- **None**: Several studies do not address punishment or sanctions at all.

**c. Efficiency or Related Payoff Outcome (`efficiency_or_related_payoff_outcome`)**  
- **Exact**: A minority of studies measure (and report) group payoff, welfare, or efficiency as defined by the ratio of realized to maximal cooperative outcomes.
- **Close/Adjacent**: Some report earnings or provision rates (e.g., threshold success in public good provision) that serve as close proxies for efficiency.
- **Weak/None**: Many focus on behavioral outcomes (contribution rates, norm compliance, punishment frequency) without translating these to efficiency or group payoff terms.

**Summary**: Task relevance for prediction of treatment efficiency is limited, as only a subset of studies addresses all three key aspects with the necessary granularity. Where evidence is strongest, it is usually for repeated PGGs with implemented, parametric punishment and clear efficiency/earnings outcomes. Elsewhere, relevance is either partial or limited to plausible analogies.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes** (i.e., efficiency, group payoff, total earnings, welfare) are reported and analyzed in a minority of the most relevant PGG papers—for example, those manipulating punishment cost/benefit ratios or incentive schemes.
- **Behavioral outcomes** (contribution rate, cooperation rate, punishment frequency, retaliation, norm compliance, social judgments, emotional responses) are far more common across the literature. In many cases they are discussed as mechanisms or correlates of efficiency, but are not themselves efficiency metrics.
- A handful of studies use **proxies for efficiency** (e.g., rate of public good provision in threshold games, contest expenditure levels) but do not explicitly calculate efficiency ratios as required for the prediction task.
- Non-payoff outcomes are frequently the primary focus, and some studies report exclusively on attitudinal or psychological measures.

# 4) Main Findings Relevant To Prediction

- **Punishment tends to increase contributions, but does not always improve or can even decrease efficiency:**  
  - In standard repeated PGGs, enabling peer punishment commonly results in higher contributions; however, the costs imposed by punishment (both to the punisher and punished) can offset or exceed the efficiency gain from higher cooperation (Gürerk et al., 2009; Fehl et al., 2012; Kocher et al., 2012).
  - **Vendettas and retaliation cycles** further erode efficiency, especially in repeated games with open punishment and visible identities (Fehl et al., 2012).
  - **Centralized (leader/administered) punishment** sometimes produces better efficiency outcomes, particularly when path-dependence and initial reliance on rewards are considered (Gürerk et al., 2009).
  - **The structure of the punishment mechanism**, including its cost/impact ratio (punishment technology), targeting logic (individual vs. random/blind), and whether punishment costs are recycled, strongly moderates efficiency effects (Fatas et al., 2010; Bracht et al., 2008).
  - **Contextual and group-level moderators**, such as baseline contribution/efficiency in the control, group size, cultural/social background, and the potential for anti-social punishment, can determine whether punishment increases, decreases, or leaves efficiency unchanged (Kocher et al., 2012; Mulder et al., 2006).
  - **Presence of alternative mechanisms (e.g., rewards, communication, commitment, voting):** These can substitute for or outperform punishment in generating efficiency, especially under favorable contextual conditions (Messer & Zarghamee, 2007; Hayo & Vollan, 2012; Bracht et al., 2008).

# 5) Prediction Guidance

- When **control efficiency is high** (i.e., baseline game without punishment already achieves or approaches full efficiency), enabling punishment is unlikely to yield further efficiency gains and may, due to punishment costs, even reduce efficiency (Kocher et al., 2012).
- When **control efficiency is low** (i.e., high levels of free riding and low public good provision), introducing a well-structured punishment mechanism can sometimes increase efficiency, but this effect is sensitive to features such as:
  - The **punishment cost/impact ratio**: Inefficient punishment (high cost, low impact) is detrimental to group payoff.
  - The **potential for vendetta or retaliation cycles**: The risk of efficiency loss from overpunishment or cycles of retaliation must be considered, especially in settings with visible punishers or open-ended peer punishment (Fehl et al., 2012).
  - **Centralization and targeting**: Centralized punishment, or mechanisms that limit irresponsible or anti-social punishment, are more likely to increase efficiency; random or poorly targeted punishment can backfire unless costs are recycled (Gürerk et al., 2009; Fatas et al., 2010).
  - **Social and cultural context**: Group norms, social background, and prevalence of anti-social punishment are powerful moderators but are not encoded in typical game design dimensions.
- **Key design dimensions for prediction**: Evidence is strongest when linking variation in player_count, num_rounds, mpcr, punishment_cost, punishment_tech, all_or_nothing, and chat availability to efficiency changes. Other variables (e.g., default_contrib, reward_exists, communication/voting mechanisms) are experimentally less attended to as primary moderators of punishment effects.
- **Caveats**:
  - Empirical studies show substantial **heterogeneity across settings and participant groups**; quantitative prediction remains challenging without more precise mapping of design dimension values and baseline efficiency levels.
  - Many findings about contribution rates and punishment use do not translate directly to efficiency predictions.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions:**
  - **player_count**: Group size often manipulated and discussed; effects on efficiency via opportunity for punishment, anonymity, and target identification (multiple papers).
  - **num_rounds**: Repetition and time horizon are core (e.g., sustainability of cooperation, escalation of vendettas).
  - **mpcr**: Varies across studies; critical for payoff calculus and moderates both control and treatment efficiency.
  - **punishment_cost, punishment_tech (cost:impact ratio)**: Carefully specified in several experimental designs; central to understanding the net efficiency effect.
  - **all_or_nothing**: Binary versus continuous contribution is commonly a design choice.
  - **chat**: Some studies manipulate communication opportunities; shown to powerfully moderate cooperation (Messer & Zarghamee, 2007; Brosig et al., 2004).
  - **reward_exists, reward_cost, reward_tech**: Effectively covered in studies comparing punishment and reward mechanisms (Gürerk et al., 2009; Bracht et al., 2008).
  - **show_n_rounds**: Sometimes manipulated (Sell & Wilson, 1999).
  - **show_other_summaries**: Less systematically explored, but present in some feedback/monitoring designs.

**Indirectly/contextually discussed:**
  - **default_contrib**: Framing effects on cooperation occasionally explored (Messer & Zarghamee, 2007).
  - **show_punishment_id**: Identity visibility relevant in discussion of vendetta dynamics and social moderation.
  
**Missing or only anecdotally covered:**
  - Fine-tuned manipulations of **show_punishment_id**, **show_other_summaries**, and highly parametrized **reward/punishment technologies**.
  - Multidimensional interactions among dimensions (e.g., punishment plus communication plus all-or-nothing).

# 7) Important Limitations

- **Sparse direct mapping**: Very few papers report both control (no punishment) and treatment (punishment enabled) efficiency for the same PGG design in a way that enables precise out-of-sample prediction using only the 14 specified design features plus control efficiency.
- **Overrepresentation of behavioral proxies**: Many studies rely on contribution rates or other non-payoff metrics, which do not reliably predict net efficiency given punishment costs.
- **Limited generalizability**: Socio-cultural moderators, emotional drivers, and contextual factors (trust, anti-social punishment) are often shown to matter but are not encoded as prediction inputs; quantitative effects may fail to generalize across populations.
- **Retaliation and vendettas**: Not always anticipated in design, but frequently observed empirically, sometimes reversing intuitively expected efficiency gains.
- **Adjacency challenges**: Adjacent games (trust games, n-person PDs, CPRs) may not map cleanly onto standard PGG predictions, especially for fine-grained design variation.
- **Lack of multi-dimensional design space coverage**: The full combinatorial space of the 14 prediction dimensions is not systematically explored.
- **Reward mechanisms and their interplay with punishment**: Sometimes more effective for increasing efficiency, but direct comparison is limited.
- **Long-term, persistence, or history effects**: Some evidence of path-dependence, learning, or post-treatment effects not fully accounted for by initial design features.

---

**In summary:**  
The literature offers qualified support for predicting that enabling peer punishment in PGG-like environments may increase contributions, but its effect on efficiency is highly context-dependent and often negative, particularly when punishment is costly, misapplied, or leads to vendetta cycles. The best predictors are game design features such as group size, MPCR, punishment cost/technology, and baseline efficiency without punishment. Prediction should be cautious and specify that strong efficiency gains occur principally when control efficiency is low, punishment is well-calibrated, and mechanisms for abuse or retaliation are limited. However, quantitative precision in prediction is hampered by the sparseness of directly relevant empirical data and by reliance on partial outcome measures.
