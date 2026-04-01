# 1) Evidence Base

The paper set consists predominantly of **empirical, laboratory-based experimental studies** on public goods games (PGGs) and closely related social dilemmas, supplemented by a limited number of **field experiments** and several **theory/simulation papers**. The empirical coverage is extensive for standard PGGs and institutional variations (e.g., leader vs. peer punishment, centralized enforcement, higher-order punishment, third-party punishment), but some studies examine adjacent environments (trust games, CPR games, intergroup conflict) or mechanisms (reward, rent extraction, voluntary agreements, reputational penalties). Several theory papers are included, offering game-theoretic insights into punishment efficacy.

For the **downstream prediction task of treatment efficiency** after enabling punishment (relative to control), this evidence base is **broad in scope** but **varied in directness and depth**. Some papers provide precise, design-level quantitative data on efficiency with and without punishment (**exact or close matches**); others furnish only behavioral proxies for efficiency or utilize adjacent games with transferable mechanisms. There is **substantial empirical variability** in punishment cost/technology, information structure, and enforcement credibility, all of which are well-represented in the database. However, not all 14 game design dimensions are equally emphasized.

# 2) Task Relevance

**A. pgg_or_variant**
- **Exact relevance**: Core lab studies employ standard PGGs (e.g., Jiang & Wang, 2024; Krügel & Maaser, 2025; Nicklisch et al., 2021; Nhim et al., 2023).
- **Close relevance**: Many papers study CPR games, trust games, public bads, or multilevel variants that share primary features with PGGs (e.g., Otten et al., 2024; Kamei et al., 2023; Zong et al., 2025).
- **Adjacent/Weak/None**: Some investigate environments further removed from standard PGGs (e.g., dyadic trust games, bargaining, or naturalistic settings).

**B. punishment_or_sanctions**
- **Exact relevance**: Many studies analyze explicit peer or centralized punishment, varying in cost, technology, and institutional structure (e.g., presence/absence, punishment magnitude, third- vs. fourth-party, competitive punishment institutions).
- **Close relevance**: Some papers conceptualize punishment more broadly, including rent extraction, appropriation, litigation threats, or social pressure as proxies.
- **Adjacent/Weak/None**: A few focus on reward, monitoring, or norm enforcement mechanisms outside of the punishment context.

**C. efficiency_or_related_payoff_outcome**
- **Exact relevance**: A good subset report direct, payoff-based outcomes matching the efficiency definition (ratio of realized group payoff to social optimum), especially for both control and treatment conditions.
- **Close/Adjacent**: Several report aggregate payoffs, welfare, or surplus but not normalized efficiency, or only show related measures in adjacent games. Many studies report behavioral outcomes (contribution rate, compliance) without full calculation of efficiency.
- **Weak/None**: Some papers focus exclusively on non-payoff behavioral outcomes or do not report group-level payoffs at all.

**Summary**: Roughly half the papers are **directly relevant** for PGG/punishment/efficiency; others provide adjacent or partial evidence. Very few provide no relevant insight.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes:**
- **Efficiency**: As defined, "the group's total payoff as a share of the fully cooperative optimum" is measured or calculable in several key empirical papers (e.g., Jiang & Wang, 2024; Krügel & Maaser, 2025; Nicklisch et al., 2021; Nhim et al., 2023; Kamei et al., 2023; Zong et al., 2025).
- **Related outcomes**: Total earnings, group payoff, welfare, surplus, and social welfare are periodically reported, often as primary outcomes. Some theory papers focus exclusively on efficiency-equivalent outcomes.
- **Partial measurement**: Some studies give only partial payoff information or focus on individual, not group, welfare.

**Non-payoff behavioral outcomes:**
- Most papers additionally or exclusively report **contribution rate, cooperation rate, norm compliance**, punishment/reward frequency, and similar variables.
- A number of papers only report these behaviors without directly translating them into efficiency figures, and in such cases, the link to efficiency must be treated carefully and flagged as indirect.

# 4) Main Findings Relevant To Prediction

**Synthesizing the core literature with direct efficiency/payoff measurement in PGGs:**

- **Punishment typically increases efficiency in standard lab PGGs** when: peer or centralized punishment is enabled, monitoring is affordable, and information quality on contributions is good (Jiang & Wang, 2024; Krügel & Maaser, 2025; Nicklisch et al., 2021; Kamei et al., 2023).
- **Magnitude and reliability of the efficiency gain depend on game design:**
  - **Institutional design of punishment:** Efficiency gains are highest when punishment is precise, targeted (not excessive/antisocial), and unnecessary punishment is minimized (Krügel & Maaser, 2025).
  - **Punishment cost and structure:** When punishment is costly and enforcement consumes group resources, efficiency gains may be partially or fully offset by costs (Nhim et al., 2023; Safarzynska, 2020).
  - **Punisher characteristics:** In leader-based punishment, gains depend on leader gender, framing (responsibility vs. authority), and selection method (voting vs. random) (Jiang & Wang, 2024).
  - **Information availability:** Efficient monitoring (even if modestly costly) is critical—if accurate contribution information is inaccessible or too expensive, punishment is less effective or counterproductive (Nicklisch et al., 2021).
  - **Probability/credibility of enforcement:** Gains are realized only when enforcement is credible (Alt et al., 2023). When the probability of punishment is low or enforcement is avoidable, efficiency does not improve or may decline.
  - **Nature of punishment:** Prosocial punishment enhances efficiency, while antisocial or indiscriminate punishment can undermine cooperation or efficiency (Angelsen & Naime, 2024).
  - **Contextual moderators:** Cultural context, prior experience with simpler games, group structure (multilevel vs. single-group), and baseline cooperation levels all affect the magnitude and even presence of efficiency gains (Otten et al., 2024; Praxmarer et al., 2024).

**However, not all punishment mechanisms guarantee efficiency improvements:**
- **If punishment is too costly, institution formation or enforcement consumes more than the surplus generated by increased cooperation**, leading to lower efficiency than the control (Nhim et al., 2023; Safarzynska, 2020; Bar-Gill & Engel, 2018).
- **Decentralized or voluntary-agreement settings with avoidable or evadable punishment**: No improvement in efficiency is seen unless participation/ambition can be enforced (Del Ponte et al., 2025).
- **Behavioral findings** where only contribution rate is reported suggest positive impacts of punishment on cooperation, but these effects do not always translate one-for-one into efficiency improvements if punishment incurs group-level costs or is used antisocially.

# 5) Prediction Guidance

- **For most standard PGGs** (lab, fixed group size, no or limited chat, explicit punishment stage, well-defined MPCR, transparent feedback), the **literature supports a robust, positive average effect** of enabling peer or centralized punishment on group efficiency, relative to the control (punishment disabled). The measured effect is **strongest when punishment cost is low**, information about contributions is reliable and accessible (monitoring is cheap), and punishment is targeted to non-contributors.
- **Prediction should explicitly take into account**:
  - **The control efficiency**: Games with high baseline efficiency may see smaller absolute gains, and, if punishment is costly, the net benefit may be negligible or even negative.
  - **Punishment cost/technology**: Higher costs erode net efficiency gains; prediction models should include the cost-impact ratio as a primary moderator.
  - **Institutional features**: Whether the game uses peer vs. leader/centralized punishment, presence of sequential/third-party punishment, framing of authority, and the odds that punishment can be avoided or misdirected.
  - **Monitoring/information structures**: Games with cheap, accurate monitoring have the largest efficiency gain when punishment is enabled.
  - **Reward mechanisms**: The presence of reward and its cost-effectiveness alter baseline efficiency and may substitute, complement, or crowd out punishment's effect.

- **Where only behavioral/proxy outcomes are reported**, predictions should remain cautious, noting the risk that increased contributions will not produce proportional efficiency gains if punishment is used heavily or cost-ineffectively.
- **In adjacent or less standard games**, transferability is limited—predictions should be correspondingly hedged, and caveats noted regarding differences in player roles, optionality of punishment, and ability to evade or undermine the institution.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions:**
- **player_count, num_rounds**: Most lab studies manipulate or report group size and round number, showing that group size can affect punishment's salience and targeting, while longer games allow greater learning and norm formation.
- **punishment_cost, punishment_tech**: A primary focus in nearly all punishment studies; cost magnitude and implementation details directly shape efficiency outcomes.
- **mpcr**: Explicitly specified in all quantitative studies and shown to moderate both baseline and treatment efficiency (e.g., Cagala et al., 2019).
- **all_or_nothing, chat**: Binary/continuous action structure and communication status are commonly manipulated or detailed, though chat is less frequently observed in punishment studies.
- **show_n_rounds, show_other_summaries, show_punishment_id**: These visibility and information dimensions are periodically addressed, especially in studies on monitoring and social feedback.
- **reward_exists, reward_cost, reward_tech**: Addressed in several papers, although less central than punishment mechanisms.

**Indirectly or contextually discussed dimensions:**
- **default_contrib**: Framing of default decisions is sometimes noted (Del Ponte et al., 2025; Chang et al., 2024).
- **show_punishment_id**: Occasional direct manipulation (Brouwer et al., 2023), but more often only in passing.
- Some dimensions (e.g., magnitude of punishment/reward beyond cost, uncertainty about round number) are implied rather than systematically analyzed.

**Effectively missing:**
- **Several papers do not report or manipulate full information on all dimensions**, particularly regarding feedback structure, punishment identity, or the technical implementation of reward.

# 7) Important Limitations

- **Gaps in payoff-based efficiency reporting**: While many studies are rich in behavioral outcomes, only a subset report the required payoff-based efficiency or allow its direct calculation.
- **Transferability to field or naturalistic environments** is constrained: most strong evidence comes from lab settings with artificial stakes and fixed groupings.
- **Variation in punishment implementation**: Not all punishment mechanisms are equivalent. Peer vs. leader/centralized, costly vs. costless, fixed- vs. variable-impact, and credible vs. avoidable models differ widely in efficiency impact.
- **Limited generalizability to games with optional or evadable punishment**: Where institution adoption or compliance is voluntary, punishment often fails to improve efficiency.
- **Cultural/contextual moderators are often underexplored**: Effects found in one institutional or population context may not generalize.
- **Sparse evidence on some design dimensions**: A sizeable number of the 14 prediction variables are only contextually or indirectly informed, complicating fine-grained or parametric prediction.
- **Ambiguity from conflicting findings**: Some studies document negative or null efficiency effects of punishment (when cost is high or antisocial), while theory predicts positive effects given strong assumptions (e.g., draconian punishment). Ambiguity must be acknowledged in prediction.

---

**In summary:**  
This literature set provides strong, direct evidence that enabling punishment in standard PGGs usually increases efficiency compared to control, **when institution design, punishment cost, monitoring, and enforcement credibility are favorable**. **However, net efficiency gains are not universal and are sensitive to the details of implementation and context.** For prediction, use control efficiency as a partial baseline, adjust upward or downward based on punishment cost, information quality, institution design, and the presence of complementary reward/communication features. Where direct payoff evidence is absent, acknowledge the uncertainty and avoid assuming proportional behavioral-to-efficiency translation.
