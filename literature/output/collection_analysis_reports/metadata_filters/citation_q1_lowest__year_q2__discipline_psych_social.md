# 1) Evidence Base

The paper set is broad in its theoretical coverage—spanning lab experiments, agent-based simulations, and formal economic models—but relatively narrow in terms of direct empirical studies focused on efficiency effects of peer punishment in classic public goods games (PGGs). Of the 25 papers, the majority are theory-oriented or report empirical results from close or adjacent game types (e.g., resource allocation, Prisoner's Dilemma, contest games). Only a few (notably Kroupa, 2014; Asgharpourmasouleh et al., 2017; Antoci & Zarri, 2015; Nasrallah & Cheaib, 2016) directly address the primary outcome of interest—group efficiency or analogous payoff-based outcomes—when comparing baseline conditions to punishment-enabled treatments. Many papers address non-payoff behavioral outcomes such as cooperation rates, norm compliance, and punishment frequency or motivation. A significant subset provides mechanistic or psychological insights but lacks direct quantitative payoff data.

# 2) Task Relevance

**pgg_or_variant:**  
- **exact relevance:** A minority of papers directly study PGGs or standard variants (e.g., Kroupa, 2014; Ogaki & Tanaka, 2017; Vincent, 2017).
- **close/adjacent relevance:** Several studies use agent-based models or games structurally similar to PGGs (e.g., Asgharpourmasouleh et al., 2017; Antoci & Zarri, 2015; Nasrallah & Cheaib, 2016), or examine resource allocation or Prisoner’s Dilemma games with punishment mechanics.
- **weak/none:** Many other papers are either not based on PGGs or use only weak analogues.

**punishment_or_sanctions:**  
- **exact/close relevance:** About half explicitly introduce or theorize peer punishment or decentralized sanctions as a treatment or mechanism.
- **adjacent:** Some report on adjacent forms, such as exit or exclusion (Gaudeul et al., 2017), or subjective evaluation as indirect punishment (Gillenkirch & Kreienbaum, 2017).
- **none:** Several studies focus only on transparency, monitoring, or third-party surveillance, with no actual punishment (e.g., Becchetti et al., 2015; Sääksvuori & Ramalingam, 2015).

**efficiency_or_related_payoff_outcome:**  
- **exact:** Only a few papers use efficiency, total earnings, welfare, or surplus as primary reported outcomes (notably Kroupa, 2014; Nasrallah & Cheaib, 2016; Asgharpourmasouleh et al., 2017; Antoci & Zarri, 2015).
- **adjacent/close:** Most others focus on cooperation rates or norm compliance (behavioral), citing efficiency only as an interpretive or secondary outcome.
- **none:** A substantial portion provide no evidence on payoffs or efficiency.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (relevant for prediction):**  
  - **Directly measured:** Group efficiency (group payoff divided by maximum possible), total earnings, welfare, total coins.
  - **Papers:** Kroupa (2014); Asgharpourmasouleh et al. (2017); Nasrallah & Cheaib (2016); Antoci & Zarri (2015); marginally in Gaudeul et al. (2017) and Becchetti et al. (2015) (but without punishment).
- **Non-payoff, behavioral outcomes (not direct substitutes):**  
  - **Common metrics:** Contribution rate, cooperation rate, punishment frequency or intensity, norm compliance, participation rate.
  - **Papers:** Most theory and many lab experiment papers (e.g., Ogaki & Tanaka, 2017; Vincent, 2017; Tang & Ye, 2016; Teraji, 2016; Gillenkirch & Kreienbaum, 2017; D'Exelle & Riedl, 2013).
- **Distinction:** Where only behavioral outcomes are measured, their relationship to efficiency is often asserted but rarely quantified.

# 4) Main Findings Relevant To Prediction

- **Punishment does not universally increase efficiency:**  
  - In standard lab PGGs with costly punishment, efficiency often decreases due to the cost of sanctioning outweighing the increase in cooperation (Kroupa, 2014; Antoci & Zarri, 2015).  
  - In richer game environments (more rounds, communication, reputation), the cost of punishment drops, cooperation stabilizes, and efficiency increases—sometimes surpassing the no-punishment baseline (Kroupa, 2014; Vincent, 2017).
- **Conditionality and moderators:**  
  - Efficiency increases with punishment primarily when baseline cooperation is low and when mechanisms (communication, reputation, endogenous group formation) dampen unnecessary or antisocial punishment (Kroupa, 2014).
  - If anti-social punishment or second-order free riding is strong and not mitigated, the efficiency gains from punishment are eroded or become negative (Antoci & Zarri, 2015).
  - Agent-based models show large positive shifts in efficiency when both punishment is enabled and agents have strong intrinsic motivation for the common good (Asgharpourmasouleh et al., 2017).
- **Indirect and adjacent evidence:**  
  - Many models and experimental studies show increased cooperation with punishment, but do not observe or report direct efficiency metrics.
  - In adjacent game types (Prisoner’s Dilemma, resource allocation with sanctions), efficiency is highly sensitive to group size, information structure, and the alignment of the punishment mechanism (Nasrallah & Cheaib, 2016; D'Exelle & Riedl, 2013; Patrzyk & Takác, 2017).
  - The presence of rewards or alternative sanctioning mechanisms sometimes undermines the efficiency benefits of punishment if not carefully structured (Antoci & Zarri, 2015).

# 5) Prediction Guidance

The literature supports several clear, evidence-based recommendations for predicting average group efficiency when peer punishment is enabled in PGG-like environments:

- **Baseline control efficiency is informative:**  
  - If the no-punishment baseline is already highly efficient (cooperation is stable), enabling punishment is less likely to further increase efficiency and may even reduce it if punishment costs are significant.
  - If baseline efficiency is low (frequent defection), enabling punishment is more likely to yield gains in efficiency, provided that negative side effects (e.g., antisocial punishment) are limited (Asgharpourmasouleh et al., 2017; Nasrallah & Cheaib, 2016).
- **Prediction must account for game design moderators:**
  - **Rounds:** More rounds increase the scope for punishment to be efficiency-enhancing, as strategic cooperation and learning reduce the need for costly punishment over time (Kroupa, 2014).
  - **Communication and reputation:** Their presence strongly moderates the effect of punishment; predictions should be adjusted upward for designs that include these features (Kroupa, 2014; Vincent, 2017).
  - **Punishment cost and effectiveness:** High punishment cost reduces efficiency impact; more efficient punishment (greater deterrence per unit cost) yields greater efficiency benefits (Kroupa, 2014; Nasrallah & Cheaib, 2016).
  - **Antisocial punishment and second-order free riding:** Efficiency will be lower if designs enable or fail to prevent these behaviors (Antoci & Zarri, 2015).
- **Quantitative prediction:** The evidence is strongest for the qualitative direction and moderating factors, not for precise numeric prediction—few papers report effect sizes or magnitude of efficiency change due to punishment.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions:**
- `player_count`, `num_rounds`, `all_or_nothing`, `mpcr`, `punishment_cost`: Frequently analyzed both empirically and theoretically (Kroupa, 2014; Asgharpourmasouleh et al., 2017; Antoci & Zarri, 2015; Nasrallah & Cheaib, 2016; Tang & Ye, 2016).
- `punishment_tech`: Discussed in terms of mechanism design or deterrence effectiveness (Antoci & Zarri, 2015; Nasrallah & Cheaib, 2016).
- `chat` (communication): Treated as a key moderator of efficiency with punishment (Kroupa, 2014; Vincent, 2017).
- `show_other_summaries`, `show_n_rounds`: Touched upon regarding information disclosure and strategy (Becchetti et al., 2015; D’Exelle & Riedl, 2013).

**Indirectly/contextually discussed:**
- `default_contrib`: Some mention of framing but not directly analyzed (Vermeer et al., 2016).
- `show_punishment_id`: Reputation effects discussed in theory/simulation (Kroupa, 2014; Vincent, 2017; Patrzyk & Takác, 2017).
- `reward_exists`, `reward_cost`, `reward_tech`: The effect of enabling both punishment and rewards is investigated theoretically (Antoci & Zarri, 2015), but sparse empirical evidence.

**Effectively missing or rarely considered:**
- Interaction effects among dimensions (e.g., joint presence of chat and reward).
- Parameter sensitivity (e.g., non-linear interaction of `mpcr` and `punishment_cost`).
- Precise implementation/fidelity of real-world punishment compared to lab analogues.

# 7) Important Limitations

- **Scarcity of direct empirical studies:** Very few studies report both control and punishment-enabled efficiency within the same experimental design, limiting direct generalizability for prediction.
- **Heavy reliance on indirect proxies:** Many findings are based on cooperation rates or norm compliance, not direct payoff outcomes, which can mislead if the cost of punishment is neglected.
- **Heterogeneity and ambiguity in mechanisms:** Effects of punishment are highly context-dependent; antisocial punishment, second-order free-riding, and design specifics (communication, group size, information structure) can reverse the qualitative effect.
- **Lack of quantitative predictive models:** There is little empirical data supporting parameterized predictions (i.e., how much efficiency increases, given baseline and design parameters)—most guidance is directional with conditional qualifiers.
- **Sparse evidence on less common design dimensions:** Variables like `default_contrib`, detailed feedback structures, and the joint operation of rewards and punishments are insufficiently studied.
- **External validity issues:** Real-world moderation from social capital, reputation, and endogenous group composition is primarily discussed in theory, with rare field validation.
- **Ambiguity in adjacent/variant games:** Evidence from games adjacent to PGGs (Prisoner’s Dilemma, CPRGs) may not transfer cleanly.

---

**Summary:**  
The literature provides robust qualitative support for the idea that the efficiency effect of enabling punishment in PGGs is highly contingent on game design—especially number of rounds, communication, reputation, and the cost/effectiveness of punishment. Baseline control efficiency is a critical moderator. However, the evidence for precise, dimension-specific numerical prediction is limited, and effects can be negative if design induces antisocial punishment or high sanctioning cost. Many studied outcomes are behavioral (cooperation rate) rather than direct efficiency. Overall, the best-supported prediction is: **Enabling punishment in PGG-like games tends to increase efficiency when baseline efficiency is low and game design includes features (longer rounds, communication, reputation) that suppress costly or antisocial punishment; otherwise, the efficiency effect may be weak or negative.** Careful attention to the interaction of design dimensions is warranted, and predictions should remain cautious where empirical payoff evidence is sparse.
