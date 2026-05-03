# 1) Evidence Base

The paper set comprises 29 papers, with a mix of **empirical lab experiments** (mainstream in PGG and social dilemma research) and **theoretical/simulation modeling** (including agent-based and game-theoretic analyses). About half the papers are direct empirical studies of public goods or closely analogous games, while others build general theory, model variants (e.g., procurement games, ROSCAs), or focus on related social dilemmas (e.g., common pool resource games, repeated Prisoner's Dilemmas).

The set is **broad in its coverage of cooperation mechanisms and institutional devices** (including reward, exclusion, reputation, mobility, and memory), yet the **number of papers reporting both punishment-enabled and punishment-disabled efficiency (or closely related payoff outcomes) within public goods games is limited**. Many empirical studies focus on behavioral variables (like contribution rates), and theoretical work often emphasizes cooperation maintenance, stability conditions, or the influence of norm structures, with efficiency as a more occasional outcome.

There is **substantial heterogeneity in game design features** across the papers, and not all 14 prediction dimensions are systematically varied in the literature. Some dimensions (e.g., punishment cost, mpcr/player_count) are well covered, while others (e.g., reward parameters, chat, contribution framing, information displays) are sparse.

# 2) Task Relevance

**PGG or Variant**:  
- **exact**: Roughly half the papers are standard linear PGGs or extremely close (e.g., Kamijo et al., 2020; Lefebvre & Stenger, 2020; Chapkovski, 2021; Bond, 2019; Hintze et al., 2020; etc.).  
- **close**: Some model PGG-like environments (ROSCAs, procurement with penalties, common resource games).  
- **adjacent/weak**: Several papers address Prisoner's Dilemma, collective choice in commons, or other group dilemmas, not standard PGGs.

**Punishment or Sanctions**:  
- **exact**: Many papers include peer punishment or institutional sanctions as a treatment (Kamijo et al., 2020; Hintze et al., 2020; Lefebvre & Stenger, 2020; Chapkovski, 2021; Bond, 2019).  
- **close/adjacent**: Some model exclusion, institutional costs, or penalty contracts (e.g., Koike et al., 2018; Qian et al., 2018; Salahshour, 2021 [institutional cost not labeled as peer punishment]).  
- **weak/none**: Many focus on reward, reputation, or partner choice mechanisms without punishment.

**Efficiency or Related Payoff Outcome**:  
- **exact**: Only a minority report efficiency/group payoff as the primary outcome (Kamijo et al., 2020; Hintze et al., 2020; Koike et al., 2018; Nockur et al., 2020; Honjo & Kubo, 2020; Qian et al., 2018).  
- **close/adjacent**: Many focus on cooperation/contribution rates, which may—but need not—correlate with efficiency, particularly when punishment is costly.  
- **weak/none**: Several report only behavioral/social outcomes or model variant games.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes**:  
  - *Efficiency* (ratio of realized to maximum group payoff): Occasionally reported directly, more often implied via group payoff or average earnings.
  - *Group payoff / welfare / surplus / total coins*: Sometimes reported or can be inferred.
  - *Profit or mean group profit*: For ROCSA/procurement variants or common-pool games.

- **Non-payoff behavioral outcomes**:  
  - *Contribution rate/cooperation rate*: Most frequently reported in empirical PGGs.
  - *Punishment/reward frequency*: Common in punishment and reward mechanism experiments.
  - *Norm compliance, strategy adoption, behavioral type evolution*: Salient in theoretical models.
  - *Psychological outcomes*: Satisfaction, fairness perception, guilt, trait preferences.

**Importantly, many papers that demonstrate an increase in cooperation/contribution rate do NOT report efficiency or payoff changes, and when punishment is costly, these measures can diverge.**

# 4) Main Findings Relevant To Prediction

- **Empirical PGGs with peer punishment** agree that:
    - *Punishment often increases contributions and sometimes cooperation rates* (Lefebvre & Stenger, 2020; Bond, 2019).
    - *The effect on efficiency (group payoff) is conditional*: When punishment is costly, the **efficiency benefit can be minimal, null, or even negative**, as increased contributions are offset by punishment costs (Kamijo et al., 2020; Chapkovski, 2021).
    - *Reward mechanisms* (where available) **more reliably increase efficiency** than punishment alone, especially in inefficient PGGs (MPCR < 1) (Kamijo et al., 2020).

- **Theory and simulation work** highlights key moderators:
    - *The efficiency of the punishment mechanism itself* (fine-to-cost ratio, i.e., punishment_magnitude/punishment_cost) is critical: Efficient punishment yields positive efficiency effects, but high cost reduces or negates this benefit (Hintze et al., 2020; Qian et al., 2018; Honjo & Kubo, 2020).
    - *Game structure* (player count, MPCR) interacts with punishment effectiveness (Hintze et al., 2020; Salahshour, 2021).
    - *Competitive social preferences*: In environments dominated by competitive players, punishment can reduce efficiency by fueling retaliation or persistent defection (Honjo & Kubo, 2020).
    - *Informational context*: Mechanisms for observing others' actions and payoffs can produce high efficiency even in the absence of punishment (Johnson & Smirnov, 2018; Podder et al., 2021).

- **Variants and adjacent mechanisms** (exclusion, institutional cost, etc.) show that:
    - *Peer exclusion via voting* is more effective than rule-based forfeiture punishments at increasing both cooperation and efficiency in ROSCA-type games (Koike et al., 2018).
    - *Collective sanctions* (sanctioning the whole group for one member’s defect) may reduce both contribution and earnings relative to individual peer punishment (Chapkovski, 2021).

# 5) Prediction Guidance

Based on this literature:

- **In PGGs with baseline (control) efficiency known, enabling peer punishment is likely to**:
    - **Increase contribution rates** (behavioral cooperation), but this does **not necessarily increase efficiency or group payoff**, particularly if *punishment is costly*.
    - **Efficiency gains** from punishment **depend on the punishment cost-to-impact ratio**: *Low-cost, high-impact punishment* is most likely to yield efficiency increases (Hintze et al., 2020; Bond, 2019); *high-cost punishment* can erase efficiency gains (Kamijo et al., 2020).
    - **Baseline game profitability matters**: In *inefficient PGGs* (MPCR < 1), even successful punishment-mediated cooperation may **not yield efficiency gains**—and may even decrease efficiency compared to the control (Kamijo et al., 2020).
    - **Exclusion, voting, or reward mechanisms** (when available) may outperform punishment in raising efficiency (Koike et al., 2018; Kamijo et al., 2020).
    - **Contextual moderators** (e.g., competitive vs. prosocial orientation) may result in neutral or negative punishment effects on efficiency (Honjo & Kubo, 2020).
- **Therefore, prediction models should pay particular attention to:**
    - *MPCR* (game profitability).
    - *Punishment cost and magnitude* (mechanics of punishment).
    - *Whether the environment also supports reward/exclusion* (since these moderate or dominate punishment effects).
    - *Observed control efficiency and group composition* (since baseline rates set the upper/lower bound for improvement).
- **Direct use of non-payoff behavioral outcomes (contribution/cooperation rates) as proxies for efficiency is unsafe**, especially when punishment expenditures are significant.

# 6) Design Dimensions Highlighted Across Papers

**Directly and empirically informed:**
- `player_count`  
- `num_rounds`  
- `mpcr`  
- `punishment_cost`  
- `punishment_tech` (including fine-to-cost ratio, mechanism specifics)  
- `all_or_nothing`  

**Indirectly or contextually informed:**
- `reward_exists`, `reward_cost`, `reward_tech` (only in a minority of papers, but when studied, large effect on efficiency).
- `chat` (rarely varied systematically, but included in some lab designs).
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id` (appear as manipulation checks or context for information, seldom as primary moderators).

**Sparse or effectively missing:**
- `default_contrib` (contribution framing; mostly absent as a variable).
- `show_other_summaries` and `show_punishment_id` (not highlighted as key independent variables).
- Interaction effects among the full set of 14 design dimensions (most papers only vary a subset).

# 7) Important Limitations

- **Few papers directly report the treatment efficiency outcomes required for the downstream prediction task**; most report behavioral or adjacent outcomes, necessitating caution in inference.
- **The effect of punishment costliness is inconsistently operationalized**, and not all studies specify the fine-to-cost ratio—a moderator with strong theoretical and empirical support.
- **Reward and exclusion treatments are not universally available** for comparison and are sometimes confounded with punishment, making the unique effect of punishment hard to isolate.
- **Game design dimensions are often correlated in the targets studied**; for instance, studies using continuous versus all-or-nothing contributions often differ on other features as well.
- **Social and psychological moderators** (player orientation, fairness perceptions) are rarely measured alongside payoff/economic outcomes, limiting insight into when punishment backfires or fails to help efficiency.
- **Adjacent designs (e.g., auction/procurement, ROSCA) provide suggestive but not directly transferable evidence** to standard PGGs.
- **Potential publication bias for positive effects of punishment on cooperation/efficiency** (null/negative findings are rarer).
- **Generalizability to out-of-sample design combinations is not demonstrated**, as experimental manipulations typically vary a small subset of possible design features.

---

**In short: The literature provides strong conceptual support and moderate empirical support for modeling punishment-enabled efficiency as influenced by MPCR, punishment cost, and group size, but the precise quantitative effect is highly context dependent. Behavioral increases in cooperation/contribution after enabling punishment are robust, but efficiency gains are unreliable and often small unless punishment is designed to be highly efficient, or unless the game is already sufficiently cooperative and profitable in baseline. Prediction models should explicitly account for punishment cost and base rates, and be conservative in extrapolating from behavioral outcomes to efficiency.**
