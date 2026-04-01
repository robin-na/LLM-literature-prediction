# 1) Evidence Base

This set consists of 9 papers with a strong tilt toward theory (modeling and simulation) and contextual empirical work, and only a minority of papers are direct lab experiments on PGG-like environments with measurable payoff outcomes. Only one study (Liao et al., 2021) is an experimental paper directly testing a punishment intervention in a modified threshold public goods game, while the majority of other papers use either adjacent social dilemma structures (e.g., common pool resource games, N-person chicken games, or evolutive/repeated Prisoner’s Dilemmas) or offer formal theoretical results without empirical payoff data. The breadth covers diverse social dilemmas, but direct evidence on peer punishment’s effect in PGGs is sparse. Some papers address punishment mechanisms without measuring efficiency or only focus on non-payoff behavioral outcomes.

# 2) Task Relevance

- **pgg_or_variant**: Only one paper (Liao et al., 2021) is close to a true PGG, though with a threshold structure; Sadowski et al. (2015) uses a common-pool resource game (“close”), while other papers are adjacent (prisoner’s dilemma, chicken game, multi-agent governance).
  - *Labels*: 1 exact/close, several adjacent/weak, some none.
- **punishment_or_sanctions**: Liao et al. (2021) uses third-party punishment. A few theory and adjacent empirical papers model or discuss punishment (exact or adjacent), but several do not include any punishment concept (none).
  - *Labels*: 1 exact, some adjacent/weak, several none.
- **efficiency_or_related_payoff_outcome**: Most empirical and theory papers focus on cooperation rates, norm compliance, or strategy frequencies—not efficiency or group payoffs. Sadowski et al. (2015) directly measures efficiency in a non-punishment setting; Liao et al. (2021) provides adjacent payoff evidence; others are adjacent or do not measure payoff.
  - *Labels*: 1 exact/adjacent, several adjacent/weak, some none.

**Summary**: Only one study provides near-exact relevance to all three target areas; others give contextual or indirect insights but rarely combine all three dimensions.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes** (relevant for efficiency): 
  - *Direct efficiency/group payoff*: Present in Sadowski et al. (2015) (no punishment, common-pool resource context, measures moderate/sustainable payoffs); Liao et al. (2021) (threshold public goods, improvement in group success/probability/per capita investment with TPP, not always labeled 'efficiency' by the paper but functionally similar).
  - *Absence*: Remaining papers do not report or analyze total payoff, welfare, surplus, or coins generated as primary outcomes.
- **Non-Payoff Behavioral Outcomes**: 
  - Contribution/cooperation rate, norm compliance, frequency of punishment, strategy distributions, agent types, or evolutionary trait frequencies (most theory papers, and e.g., Jaffe (2008), Zhang et al. (2020), Szilagyi & Somogyi (2010), Schroeder et al. (2014)).
- **Ambiguity**:
  - Some theoretical arguments claim links between higher cooperation and possible higher payoffs, but do not measure this; thus, these are not direct efficiency evidence.

# 4) Main Findings Relevant To Prediction

- **Punishment increases cooperation and likely efficiency** in a threshold PGG: Only Liao et al. (2021) tests this directly, showing that third-party punishment *substantially* increases average investment, investment rate, and likelihood of funding the group threshold (interpreted as group success or by inference, higher efficiency). This is in small groups (n=3), with automatic, impersonal punishment, and no communication.
- **Alternative routes to efficiency** (not via punishment): Sadowski et al. (2015) finds moderate/sustainable group payoffs in a context with no punishment but with communication and ethical leadership. This suggests that high group efficiency can sometimes be achieved without punishment, particularly when communication is allowed.
- **Punishment effectiveness is context-dependent**: 
    - Schroeder et al. (2014) finds that punishment is less common and less expected in environments with low trust and more norm violation, and that cost and group norms moderate willingness to punish. However, group payoffs do not differ much across environments.
    - Jaffe (2008), Zhang et al. (2020) (theory) suggest that punishment (especially when less costly) stabilizes cooperation, but focus on behavioral rates and group evolution, not group payoffs; evidence on efficiency is speculative.
- **Other game features may shape outcomes**: Communications, payoff structure (including MPCR and all-or-nothing rules), and the presence of leadership can enable moderate efficiency even without punishment (Sadowski et al., 2015; Szilagyi & Somogyi, 2010). Changes to punishment cost and perceived value also appear important moderators.
- **Absence of evidence on peer punishment**: With the exception of Liao et al., most included punishment mechanisms are either third-party or only modeled as an abstract “cost” in theory, with no corresponding group payoff reporting.

# 5) Prediction Guidance

- **Direct Guidance**: 
  - In threshold PGGs with small groups, no chat, and automatic third-party punishment, enabling punishment *should be expected to increase efficiency or probability of group success* relative to the control (Liao et al., 2021).
- **Contextual Guidance and Cautions**:
  - If the baseline efficiency (with punishment disabled) is already high due to communication or leadership (Sadowski et al., 2015), enabling punishment may have a weaker marginal effect or may be redundant.
  - When trust is low and norm violations are high, punishment is less likely to be assigned/useful; its effect on efficiency may be smaller or inconsistent (Schroeder et al., 2014).
- **Dimension Moderators**:
  - Punishment cost: If punishment is costly to assign, its impact may be weaker; theoretical papers suggest low-cost punishment more strongly stabilizes cooperation (Jaffe, 2008).
  - Reward mechanisms: Some theory suggests that combining incentives and punishments is more effective, but payoff-based evidence is lacking here (Zhang et al., 2020).
- **Indirect and Non-Payoff Evidence**: Where only cooperation rate, not payoff, is measured, increases in cooperation *may* translate to higher efficiency, but this is assumption-dependent and not always corroborated by direct payoff data.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed**:
  - `player_count` (Liao et al., threshold PGG in groups of 3; modeled in several theory papers)
  - `num_rounds` (included in most PGG and adjacent theory papers)
  - `all_or_nothing` (studied in threshold and binary-choice social dilemma models)
  - `punishment_cost` (Liao et al., Jaffe, Zhang et al., Schroeder et al.)
  - `mpcr` (explicit in Liao et al., used in modeling studies)
  - `chat` (explicitly manipulated in Sadowski et al.; absent in Liao et al.)
  - `show_n_rounds`, `show_other_summaries` (Sadowski et al.; summary reporting)
  - `reward_exists` (modeled in Zhang et al.)

**Indirectly Informed or Contextually Discussed**:
  - `punishment_tech` (mechanism detail discussed in Liao et al., Schroeder et al.)
  - `show_punishment_id` (identity cues mentioned only contextually)
  - `default_contrib` (not directly manipulated, sometimes implicit in design/framing)
  - `reward_cost`, `reward_tech` (theory paper discussion only, no empirical estimates)

**Effectively Missing**:
  - Many papers are silent on `default_contrib`, `show_punishment_id`, `reward_cost`, `reward_tech`, and do not distinguish between peer and third-party punishment in ways matching the prediction task.
  - Most dimensions are not systematically varied or cross-factorialized in the experimental literature.

# 7) Important Limitations

- **Sparse direct evidence on payoff/efficiency outcomes**: Only one paper (Liao et al., 2021) provides empirical data on the effect of enabling punishment on outcomes closely related to efficiency in any kind of PGG—and as a threshold game, its generalizability is limited.
- **Limited generalizability and coverage of peer punishment**: Most punishment mechanisms studied are third-party, automatic, or modeled abstractly; direct data on peer punishment (as required by the prediction task) is missing or conflated with third-party punishment.
- **Absent dimension coverage**: Many of the 14 prediction dimensions are under- or un-informed, especially aspects of technological implementation, reward structure, contribution framing, and identity signaling.
- **Context specificity**: Results that punishment increases efficiency are drawn from small, no-communication, threshold games; results from games with communication suggest that efficiency can be high *without* punishment, reducing clarity about general effects.
- **Behavioral–payoff disconnect**: Most evidence is about behavioral outcomes (cooperation rates), not actual group efficiency or total payoff; the translation between the two is not always direct or constant.
- **Retracted article**: The main empirical result (Liao et al., 2021) is from a retracted article, raising concerns about its reliability.
- **Heterogeneity in game types and outcome definitions**: Papers use variants of social dilemmas, but not standard PGG formats; outcome definitions (success rate, cooperation, efficiency) are inconsistent.
- **Absence of negative or null findings**: Literature set lacks studies emphasizing potential downsides or inefficacy of punishment for efficiency, beyond contextual moderating effects.
- **No systematic treatment–control comparisons**: Only one close study directly compares an on/off punishment manipulation; others either do not test this contrast or do not report on equivalent outcomes.

---

**Summary**:  
The literature set offers only limited, mostly indirect evidence to guide prediction of treatment efficiency from design dimensions plus control efficiency when enabling punishment in PGG-like games. One small-group, threshold PGG experiment suggests punishment is efficiency-enhancing under specific conditions, while other studies find that communication or trust can substitute for punishment and that context moderates the effect. For many dimensions and in most standard PGG scenarios, direct evidence is absent or incomplete, and outcome measurement often does not match the prediction target. These limitations should be considered when using this evidence base for prediction or model-building.
