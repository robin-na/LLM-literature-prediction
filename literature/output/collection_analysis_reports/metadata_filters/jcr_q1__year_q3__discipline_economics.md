# 1) Evidence Base

The paper set consists of 34 papers, representing a broad and diverse mix of empirical lab and field experiments, as well as theoretical models. Approximately half are empirical lab experiments with standard (or near-standard) public goods games (PGG) or close variants—these contribute the most direct evidence. Several papers are theory-focused, offering mechanism-based arguments and formal models of punishment, efficiency, and cooperation. Some papers are framed field experiments in resource management or trust-game environments, while others are purely observational or adjacent behavioral studies. Although not all papers directly target efficiency outcomes or punishment in PGGs, the set as a whole gives comprehensive coverage of institutional and behavioral moderators of punishment effects across a range of public-goods-like contexts.

# 2) Task Relevance

Each of the three target-relevance axes is populated as follows:

- **pgg_or_variant**
    - **'exact':** Multiple lab experiments directly use standard or near-standard repeated public goods games, including Nicklisch et al. (2021), Ambrus & Greiner (2019), Acemoglu & Wolitzky (2021), and Bühren & Dannenberg (2021).
    - **'close':** Several others use dynamic common-pool resource (CPR) games and trust games (e.g., Wegmann & Musshoff, 2019; Chávez et al., 2018; Hajikhameneh & Rubin, 2019), which approximate the incentives but may differ in extraction/replenishment or matching structure.
    - **'adjacent/weak/none':** A subset are behavioral or theoretical studies in non-PGG settings, such as social preference measurement, status games, or general sanctioning surveys, offering only conceptual or indirect relevance.

- **punishment_or_sanctions**
    - **'exact':** Several core papers manipulate the presence or design of peer punishment mechanisms (Nicklisch et al., 2021; Ambrus & Greiner, 2019) or analyze different punishment institutions and technologies.
    - **'close/adjacent':** Some evaluate reward systems, centralized or third-party punishment (sometimes in non-PGG contexts), or exclusion (Bonroy et al., 2019).
    - **'none':** Some studies entirely omit punishment or sanctions.

- **efficiency_or_related_payoff_outcome**
    - **'exact':** Several experiments and theories report explicit group efficiency or welfare (Nicklisch et al., 2021; Ambrus & Greiner, 2019; Wegmann & Musshoff, 2019; Chávez et al., 2018).
    - **'adjacent':** Others focus on cooperation/contribution rates, trust, or norm compliance—relevant, but not synonymous with efficiency.
    - **'none':** Some measure only willingness to punish or behavioral preferences, with no direct reference to group payoffs or efficiency.

In sum, the evidence base is rich for laboratory studies on PGGs with punishment (and efficiency), but sparser for real-world field environments and for all 14 specific game design dimensions. Many papers that examine behavioral outcomes must be carefully distinguished from those reporting actual group efficiency.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes:**  
    The strongest and most task-relevant evidence comes from papers that directly report on group efficiency, total earnings, welfare, or surplus as the main outcome (e.g., Nicklisch et al., 2021; Ambrus & Greiner, 2019; Wegmann & Musshoff, 2019; Acemoglu & Wolitzky, 2021; Chávez et al., 2018). These enable direct calibration of the effect of punishment on group efficiency.

- **Non-Payoff Behavioral Outcomes:**  
    Many papers focus primarily on contribution rates, cooperation frequency, willingness to punish, or norm compliance. While closely correlated, these do not always translate cleanly to efficiency, especially when costly punishment may reduce net payoffs even as cooperation rises (e.g., Bühren & Dannenberg, 2021; Albrecht et al., 2018; Gallier, 2020).

- **Indirect or Contextual Outcomes:**  
    Theoretical models and adjacent behavioral studies sometimes report on the stability of cooperation, the potential for enforcement, or group trust levels without any efficiency or payoff calculation. These are less useful for direct efficiency prediction.

# 4) Main Findings Relevant To Prediction

Synthesizing across the literature, the following patterns emerge about punishment's effects on efficiency in public-goods-game-like environments:

- **Punishment often increases efficiency, but only under certain conditions.**  
    When information about contributions is available and the punishment cost is not excessive, peer or democratic punishment can sustain high cooperation and efficiency, often nearing the social optimum (Nicklisch et al., 2021; Ambrus & Greiner, 2019). The efficiency gain from punishment diminishes rapidly if monitoring is expensive, if punishment is poorly targeted (high anti-social punishment), or if the punishment institution is misapplied (Nicklisch et al., 2021; Bühren & Dannenberg, 2021).

- **Institutional details strongly moderate efficacy.**  
    Democratic or majoritarian punishment (Ambrus & Greiner, 2019) reduces anti-social punishment and yields higher efficiency than individual or dictator punishment. The design of the punishment mechanism (who can punish, how, with what cost/impact) directly shapes outcomes (Acemoglu & Wolitzky, 2021).

- **Baseline/control efficiency is a crucial moderator.**  
    Groups with high control efficiency (already highly cooperative) are likely to see efficiency decline when punishment is introduced due to its cost. The positive effect of punishment is largest when control efficiency is low (Bühren & Dannenberg, 2021).

- **Information and monitoring interact with punishment.**  
    If contribution data must be actively (and expensively) acquired, punishment's impact on efficiency is highly sensitive to info cost and accuracy. Cheap, accurate monitoring enables effective punishment; high cost or noisy monitoring undermines efficiency gains (Nicklisch et al., 2021; Ambrus & Greiner, 2019; Bhaskar & Thomas, 2019).

- **Punishment can backfire or be neutral/negative.**  
    In some cases, especially when the majority of a group is already cooperative or punishment is misapplied, efficiency declines after punishment is enabled (due to costs outweighing benefits) (Bühren & Dannenberg, 2021; Safarzynska, 2020).

- **Magnitude and distribution of punishment matter.**  
    Excessive or unevenly applied punishment can reduce welfare, increase inequality, or lead to retaliation/extortion, muting or reversing efficiency gains (Acemoglu & Wolitzky, 2021; Barron & Guo, 2021).

- **Type of social dilemma and alternative mechanisms matter.**  
    Not all results are transferable across game types: for instance, effective punishment in linear PGGs may not yield gains in claim/take games, trust games, or environments with undoing actions or high uncertainty (Stoop et al., 2018; Hajikhameneh & Rubin, 2019).

# 5) Prediction Guidance

From this literature, the most robust prediction rule is:
- **Punishment increases efficiency relative to control primarily when:**
    - **Control efficiency is below the social optimum;**
    - **Punishment is well-targeted (strongly pro-social, limited anti-social punishment);**
    - **Monitoring is cheap and/or information about contributions is public and accurate;**
    - **Punishment costs are not so high as to offset any cooperation gains;**
    - **Punishment is institutionally structured to prevent extortion, misuse, or excessive escalation (e.g., democratic sanctions, public signals, safeguards against anti-social punishment).**

For *quantitative prediction*:
- If control efficiency is low, and design provides cheap, accurate monitoring and moderate punishment cost, enabling punishment should yield a large efficiency gain, approaching the efficient benchmark.
- If control efficiency is already high, or if punishment is costly/misapplied, introducing punishment may lower efficiency.
- Institutions that require group consensus for punishment (democratic or majoritarian) outperform individual punishment in efficiency gains.
- Close game design analogs may allow transfer of empirical effect sizes from laboratory PGGs with similar dimensions.

For prediction tasks using only design dimensions and control efficiency, the best-informed dimensions for predicting punishment-enabled efficiency are: player_count, num_rounds, mpcr, punishment_cost, punishment_tech, and the information environment (monitoring costs and observability). Dimensions like chat, all_or_nothing, and default_contrib have less direct, but sometimes important, effects.

# 6) Design Dimensions Highlighted Across Papers

#### **Directly informed dimensions:**
- **player_count:** Examined in many lab experiments; group size can moderate both the base rate of cooperation and punishment’s effectiveness (e.g., Bonroy et al., 2019).
- **num_rounds:** Repeated games essential for punishment to support cooperation; most studies feature repeated structure.
- **mpcr:** Strongly identified as a determinant of efficient cooperation and of the marginal benefit from any gains in cooperation.
- **punishment_cost:** Cost to punisher is a key moderator; higher costs reduce net efficiency gains even when cooperation rises.
- **punishment_tech:** The form, severity, and institution (peer, democratic, centralized) of punishment is a critical determinant.
- **all_or_nothing:** Used in both continuous and all-or-nothing settings; some evidence suggests more extreme choices can lead to more misapplied punishment.
- **show_n_rounds:** Examined in a subset of work (Cagala et al., 2019; Nyborg, 2018), usually as part of broader manipulation.

#### **Indirectly or contextually informed:**
- **default_contrib:** Framing effect (opt-in/opt-out) is not separately manipulated in most studies, but some comment on conditional cooperation or default choice architecture.
- **show_other_summaries:** Occasionally examined but more often as context (e.g., Barron & Guo, 2021) than as main manipulation.
- **show_punishment_id:** Publicness of punishers sometimes manipulated, with mixed findings (Nicklisch et al., 2021).

#### **Sparse evidence:**
- **chat:** Occasionally present (Langenbach & Tausch, 2019; Albrecht et al., 2018), but not manipulated systematically with respect to efficiency and punishment.
- **reward_exists, reward_cost, reward_tech:** Present in some design variants (Stoop et al., 2018), but direct punishment and reward comparisons are less common.
- **Information about group composition:** Recognized as an important moderator in recent work (Bühren & Dannenberg, 2021), but usually only present as an exogenous factor.

# 7) Important Limitations

- **Behavioral ≠ Efficiency outcomes:** Many studies conflate gains in cooperation/contribution with gains in efficiency, even though costly punishment can cause net reductions in payoffs. For prediction, only papers with direct efficiency or payoff data should be used for calibration.
- **Partial coverage of design space:** Not all 14 prediction dimensions are systematically tested or reported; dimensions like chat, reward mechanisms, contribution framing, and visibility of punishers are often under-specified.
- **Homogeneous lab samples and settings:** Most empirical results come from lab experiments with student samples, limiting generalizability to heterogeneous field contexts or large groups.
- **Group composition and social context:** Recent evidence (Bühren & Dannenberg, 2021) indicates that group cooperativeness and knowledge thereof are critical for punishment’s effect, but these are rarely observable or exogenous in real applications.
- **Punishment misuse and negative effects:** The literature highlights contexts where punishment reduces efficiency—due to anti-social punishment, overuse, costliness, miscoordination, or extortion (Acemoglu & Wolitzky, 2021; Barron & Guo, 2021)—which may be underrepresented if relying only on average effects.
- **External validity:** CPR and trust-game variants are informative but differ from linear PGGs in resource dynamics, matching, and feedback structure. Transferability of findings must be done with caution.
- **Unmeasured moderators:** Factors such as beliefs about norm prevalence, cultural norms, and real-world economic incentives may alter punishment's effect beyond what design variables capture.
- **Lack of field evidence:** Field or framed-field experiments are less common; most evidence for efficiency impacts comes from controlled lab settings.

---

**Conclusion:** The paper set offers a strong empirical and theoretical foundation for predicting how punishment affects efficiency in public-goods environments, particularly for standard lab PGGs and direct variants. The most actionable guidance for prediction is: carefully calibrate punishment’s expected efficiency effect using baseline control efficiency, punishment cost, information environment, and institutional design—remaining alert to the possibility of negative or null efficiency changes in highly cooperative groups or where punishment is poorly targeted or misused. For seldom-studied dimensions, predictions are more speculative and should be treated with appropriate uncertainty.
