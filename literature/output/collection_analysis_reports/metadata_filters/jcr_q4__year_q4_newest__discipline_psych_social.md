# 1) Evidence Base

This paper set is broad with respect to the social dilemma context but somewhat narrower for the specific prediction task of treatment efficiency in public-goods-game-like (PGG) environments with and without punishment. It includes a mix of empirical (primarily laboratory experiments) and theoretical papers, as well as a few observational and ethnographic studies. The majority of empirical studies use structured, incentivized games—ranging from classic PGGs to adjacent games such as trust, coordination, minimum effort, ultimatum, and real-effort games. Theoretical papers cover a range of formal models (repeated games, evolutionary game theory, prospect theory extensions) relevant to punishment and cooperation. While much of the literature is adjacent or closely related to PGGs, fewer papers provide direct, empirical, payoff-based evidence for the efficiency impacts of (peer) punishment in canonical PGGs.

# 2) Task Relevance

| Dimension                   | Relevance Summary                                                                                                         |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------|
| **PGG or Variant**          | About one-quarter of papers provide *exact* PGG evidence (e.g., Cobo-Reyes et al., 2022; Peng, 2022; Pancotto et al., 2023), others treat adjacent designs (trust, minimum effort, ultimatum), with a few papers highly adjacent (repeated PD, team investment, etc.). Several studies are only contextually relevant or rely on non-game observations.|
| **Punishment or Sanctions** | About half the papers study *exactly* punishment or sanction mechanisms (costly peer/institutional punishment, various techs), while others include adjacent deterrence or do not consider punishment directly (e.g., reward-only, democracy as a meta-institution, or norm transmission without sanctions).                |
| **Efficiency/Payoff Outcome**| Fewer than half directly report efficiency or related payoff outcomes from their experiments; others focus on contributions, cooperation rates (behavioral), or only theorize about payoffs. Some offer only adjacent indicators or infer efficiency changes from behavioral outcomes.                            |

Thus, only a minority of the paper set provides *exact* relevance along all three dimensions. Many findings are *close* or *adjacent*, particularly for PGG structure or efficiency outcomes, while some are of *weak* or *none* relevance.

# 3) Outcomes Measured In The Literature

- **Payoff-based outcomes** (directly consistent with the prediction target—group efficiency, welfare, total payoff, surplus, etc.) are reported in:
    - Direct experimental studies of PGGs with/without punishment (Cobo-Reyes et al., 2022; Peng, 2022).
    - Adjacent games that still provide efficiency or payoff measures linked to cooperative outcomes (Herne et al., 2022; Gueth & Otsubo, 2023; Lec et al., 2023; Pevnitskaya & Ryvkin, 2022; Calabuig et al., 2024; Kamei & Tabero, 2025).
    - Some theoretical models with explicit welfare analysis (Gioffré & Tampieri, 2025; Uchida et al., 2024).
- **Non-payoff behavioral outcomes** (not equivalent to efficiency, but related) include:
    - Contribution rates, cooperation rates, punishment frequency (majority of experiments, e.g., Pancotto et al., 2023).
    - Norm compliance, acceptance and offer behavior in bargaining games.
    - Psychological and social-norm responses to punishment (Dato & Friehe, 2025; Sequeira, 2023; Zhang & Pei, 2022).
- Some studies report administration/structure variables (punishment use, sanctioning choice), but do not connect these directly to efficiency.

There is substantial variability in the unit of measurement, with efficiency sometimes inferred, not directly reported. Several studies require translating contribution or behavioral results into payoff equivalents to apply findings to the prediction task.

# 4) Main Findings Relevant To Prediction

**Synthesis—PGG and Adjacent Laboratory Results:**
- In *canonical PGGs*, enabling **formal, centralized punishment** is robustly associated with higher group efficiency, especially when group membership is open (migration possible), as formal mechanisms outperform informal peer punishment in promoting average payoffs (Cobo-Reyes et al., 2022). In closed groups with high baseline cooperation, informal punishment can also sustain efficiency, but its effectiveness is fragile (susceptible to turnover).
- **Peer punishment** in PGGs and adjacent games (trust, minimum effort, team investment) increases cooperation rates and sometimes increases group efficiency, but its *net effect on efficiency* is highly contingent:
    - Where the *cost of punishment is high* and baseline efficiency is already moderate/high, enabling punishment may not improve, and can even reduce, efficiency due to second-order costs and antisocial punishment (Herne et al., 2022; Calabuig et al., 2024; Zhang & Pei, 2022).
    - Where the *cost of punishment is moderate to low*, and/or the baseline efficiency is low (due to high free-riding), enabling punishment can increase efficiency substantially, particularly as coordination improves over rounds (Lec et al., 2023; Gioffré & Tampieri, 2025; Uchida et al., 2024).
- **Reward mechanisms** (especially majority-vote) can increase efficiency even more robustly than peer reward, particularly in heterogeneous groups (Peng, 2022). In some cases, reward alone is less effective than punishment (Zhang & Pei, 2022; Pevnitskaya & Ryvkin, 2022).
- **Adjacency/Borderline Evidence** suggests:
    - The structure, effectiveness, and visibility of punishment (who can punish, whether identities are shown, whether punishment is pre-announced or coordinated) critically affect its impact on efficiency (Li et al., 2023; Gueth & Otsubo, 2023; Calabuig et al., 2024).
    - Punishment coupled with democratic decision-making or paired with reward may yield higher efficiency, but only if punishments are strong enough to deter and not offset by excessive cost (Kamei & Tabero, 2025; Pevnitskaya & Ryvkin, 2022).
- **Theoretical work** underlines that punishment is most efficiency-enhancing when:
    - The marginal per-capita return (MPCR) and fine/cost ratios fall within certain critical ranges for effective deterrence (Gioffré & Tampieri, 2025; Uchida et al., 2024).
    - Cognitive/psychological biases (e.g., probability weighting) amplify the perceived risk of punishment, making even moderate punishment effective in practice (Uchida et al., 2024).
- **Mechanism caveats**: Many empirical studies show increased cooperation but not increased efficiency, as the cost of administering punishment offsets the gain from greater cooperation (Herne et al., 2022; Calabuig et al., 2024; Zhang & Pei, 2022).

# 5) Prediction Guidance

The literature supports the following practical guidance for predicting efficiency outcomes when punishment is enabled, conditional on control efficiency and design dimensions:

- **Efficiency changes are highly context-dependent**:
    - *When control (no-punishment) efficiency is low* (typically due to pronounced free-riding), enabling punishment is more likely to result in a large positive efficiency gain—especially if punishment is formal/centralized or supported by high fine/cost ratios, and group structure is stable (Cobo-Reyes et al., 2022; Lec et al., 2023; Uchida et al., 2024).
    - *When control efficiency is moderate/high*, the marginal efficiency gain from punishment is typically small or even negative, unless punishment is nearly costless or extremely effective at raising cooperation at low administrative cost (Herne et al., 2022; Calabuig et al., 2024).
- **Critical design dimensions** to attend to in prediction include: group size (*player_count*), rounds (*num_rounds*), MPCR, punishment cost and fine (*punishment_cost*, *punishment_tech*), group openness, and information structure (punishment visibility).
- **Peer punishment** often induces higher cooperation but does not guarantee efficiency gains, due to costs and risk of antisocial punishment; formal/institutional punishment is less fragile but can also be expensive (Zhang & Pei, 2022).
- **Interaction with reward**: If rewards are present or possible, their effect on efficiency may dominate or supplement punishment, depending on mechanism details (Peng, 2022; Pevnitskaya & Ryvkin, 2022).
- **Do not impute from non-payoff behavioral outcomes**: While higher cooperation and contribution rates usually align with higher efficiency, these are not interchangeable; direct evidence of group payoff is necessary for strong prediction.
- **Theoretical guidance** justifies expecting monotonic increases in efficiency only when punishment is credible, not too costly, and deterrence is salient given the population and game structure (Gioffré & Tampieri, 2025; Uchida et al., 2024).

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- *player_count* (most lab studies and all models specify group size)
- *num_rounds* (present in all repeated/iterated games)
- *mpcr* (explicit in most PGGs and theoretical models)
- *punishment_cost* and *punishment_tech* (specified in most lab studies)
- *all_or_nothing* (binary vs. continuous decision: covered in several experiments)
- *reward_exists* (reward mechanisms directly studied in some papers, e.g., Peng, 2022)
- *reward_tech* and *reward_cost* (where reward is the focus)

**Indirectly Informed/Contextually Discussed Dimensions:**
- *chat* (communication present or absent is recorded and sometimes manipulated, but less frequently the focus of analysis)
- *show_n_rounds*, *show_other_summaries*, and *show_punishment_id* (sometimes present, but their specific effect on efficiency is not deeply analyzed)
- *default_contrib* (framing of contributions is mentioned, but rarely as the main variable)
- *punishment_exists* (inclusion vs. exclusion of punishment—central to most analyses)

**Missing or Very Weakly Addressed Dimensions:**
- *show_punishment_id* (identity notification is only specifically manipulated or discussed in a minority of adjacent papers)
- *default_contrib* (opt-in vs. opt-out framing has little quantitative analysis)
- *reward_magnitude* (rarely specified in detail)
- *show_n_rounds*, *show_other_summaries* (usually kept constant or default; their design-level effect on efficiency is underexplored)

# 7) Important Limitations

- **Sparse direct evidence for canonical PGGs**: Only a few studies explore efficiency effects of peer punishment in true PGGs with full reporting of design dimensions and efficiency comparisons; many findings come from games with adjacent structure.
- **Limited variation across all prediction dimensions**: Many dimensions (default_contrib, chat, summary visibility, etc.) are not systematically manipulated or studied for their impact on the punishment-efficiency link.
- **Behavioral outcomes vs. payoff**: Many experimental and review papers highlight increased cooperation rather than net efficiency, leaving open whether higher contributions always translate to efficiency gains after deducting punishment/reward costs.
- **Context-specific and often fragile findings**: Results depend on key moderators (e.g., group openness, sanction visibility, cost/fine ratios, presence of migration or endogenous group formation) and may not transfer to different population sizes, matchings, or environments.
- **Peer versus institutional punishment**: Papers often conflate peer punishment with institutional sanctioning, or only compare the two in narrow parameters, limiting generalizability.
- **Ambiguous or mixed results in adjacent games**: Efficiency improvements from punishment in trust, ultimatum, or minimum effort games do not always extrapolate directly to PGG settings.
- **Overreliance on theoretical mechanisms**: Several papers provide theoretical support but lack empirical verification, especially about human psychological factors or real-world applicability.
- **Sparse evidence on several dimensions**: Framing (default_contrib), communication/chat, and information structure features (punisher identity, round visibility) are rarely the primary focus, leaving their effects ambiguous.
- **Ethnographic and observational evidence not readily translatable**: Qualitative studies or those in real-world settings rarely provide payoff or efficiency data or focus on formal punishment, limiting their prediction utility.

---

**Summary**:  
The literature provides moderate guidance for predicting efficiency changes when enabling punishment in PGG-like environments, with robust qualitative understanding of moderators and the roles of design dimensions such as cost/benefit ratios, group structure, and mechanism details. However, strong quantitative prediction—especially across all design dimensions—is limited by a lack of studies jointly varying these factors and directly reporting both control and treatment efficiency. Prediction should be cautious and conditional on the specifics of game design, the cost and type of punishment, and the level of cooperation achieved in control settings.
