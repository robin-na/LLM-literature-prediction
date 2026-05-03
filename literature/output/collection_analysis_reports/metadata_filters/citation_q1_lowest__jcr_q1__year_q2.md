# 1) Evidence Base

The paper set comprises 21 works, with a mix of theoretical and empirical (mostly experimental and some simulation-based) studies. Empirical evidence on standard public goods games (PGGs) with explicit payoff/efficiency outcomes is comparatively sparse; only a minority of papers provide empirical or simulation-based analyses that report efficiency or related group payoff results in games with punishment enabled and disabled. Most papers are theoretical or computational models studying adjacent environments—such as repeated Prisoner’s Dilemma, trust games, or team production settings—rather than canonical multi-player PGGs.

Taken as a whole, this is a moderately broad literature sample for mechanisms and theory, but it is a narrow and incomplete set for the downstream prediction task: predicting average efficiency as a function of game design and control efficiency, specifically in PGGs with peer punishment.

# 2) Task Relevance

**PGG or Variant**
- **exact**: Several papers directly analyze canonical PGGs or extremely close structural variants (Kroupa, 2014; Vincent, 2017; Asgharpourmasouleh et al., 2017; Vermeer et al., 2016).
- **close/adjacent**: Many papers use related social dilemma games (repeated PDs, trust/dyadic games, or common-good settings) whose direct mapping to n-player PGGs is not always trivial (Tang & Ye, 2016; Ezeigbo, 2017; Luo & Zhao, 2013; McBride et al., 2016; Vanderschraaf, 2016; Patrzyk & Takác, 2017).

**Punishment or Sanctions**
- **exact**: A substantial share of papers analyze explicit costly punishment as in PGGs, some with nuanced mechanisms (altruistic, third-party, retaliation, etc.).
- **adjacent or none**: Other studies substitute reward, indirect reciprocity, status, or exclude punishment mechanisms entirely, making their findings contextually relevant rather than directly transferable.

**Efficiency or Related Payoff Outcome**
- **exact**: Only a subset (Kroupa, 2014; Asgharpourmasouleh et al., 2017; Ezeigbo, 2017; Luo & Zhao, 2013; McBride et al., 2016; Vanderschraaf, 2016; Shinya et al., 2016; Harbaugh & To, 2014) report efficiency or group payoff as a primary outcome. A few others report on proximate outcomes like group welfare or total earnings.
- **adjacent**: Several studies focus on cooperation rate, norm compliance, or effort—behavioral outcomes that are related to, but not the same as, efficiency.
- **weak/none**: Many papers, especially those studying strategy dynamics or macro-level phenomena, do not measure or report any efficiency or group payoff outcome.

# 3) Outcomes Measured In The Literature

- **Payoff-related (efficiency, group payoff, total earnings):**
  - Reported as a primary or explicit outcome in only a minority of papers. Outcome definitions and calculational bases often differ: some measure average group payoff, some consider efficiency relative to maximal cooperation, and some use surplus or total coins generated.
  - Even in simulation studies, direct reporting of ‘efficiency’ in the prediction-task sense (as a ratio to full cooperation baseline) is not always present.

- **Non-payoff behavioral outcomes:**
  - Nearly all papers measure or theorize about contribution/cooperation rates, punishment frequency, strategy distributions (cooperator/punisher/defector proportions), norm enforcement actions, or trust.
  - Many theoretical papers center on the evolutionary or strategic stability of cooperation, not on resulting group payoffs/efficiency.

- Several papers are entirely conceptual (e.g., status roles, psychological motives) or focus on norm-psychology, not observing any quantitative outcome.

# 4) Main Findings Relevant To Prediction

Synthesizing only papers with at least close relevance to the prediction task (PGG or close variant, explicit punishment manipulation, and efficiency/payoff outcomes):

- **Punishment alone tends not to improve efficiency in standard, short, anonymous lab PGGs,** where punitive actions have direct costs (Kroupa, 2014; Ezeigbo, 2017). The cost of punishing often outweighs the increase in contributions, reducing group efficiency versus control.
- **Efficiency improvements are possible when additional mechanisms are present,** such as longer time horizons (more rounds), communication or chat, low anonymity (reputation, status, showPunishmentId), or endogenous group formation (Kroupa, 2014; Vincent, 2017; Patrzyk & Takác, 2017). These features can reduce both the necessity and cost of punishment, supporting higher group payoffs.
- **High punishment cost, antisocial punishment, and absence of coordination mechanisms** decrease the efficiency benefits of enabling punishment and may even make treatment groups less efficient than controls (Kroupa, 2014; Ezeigbo, 2017).
- **Structural and motivational complements (e.g., intrinsic desirability for the common good, mating preferences, or coordination on punishment)** can amplify the positive impact of punishment (Asgharpourmasouleh et al., 2017; Tang & Ye, 2016).
- **Network structure and group size** matter: small groups and denser network links can make punishment more effective in raising efficiency (Patrzyk & Takác, 2017; Luo & Zhao, 2013), although these findings are conditional and mostly from non-PGG games.
- **Severity of punishment and how it is administered (proportional, third party, group-wide, or discretionary)** affect both effectiveness and side effects on efficiency (Vanderschraaf, 2016; Koenig & Riley, 2017; Harbaugh & To, 2014; Luo & Zhao, 2013).
- **Balance between punishment and forgiveness/trust**: Harsh punishment in the absence of mechanisms for generosity or leniency can be counterproductive or fail to sustain efficiency, particularly under uncertainty (Shinya et al., 2016).

Other adjacent findings:
- **Punishment preferences often exceed actual material harm/gain** from defection (Koenig & Riley, 2017), suggesting a risk of over-punishment that could hurt efficiency unless mitigated by game design.
- **Effect of punishment can be negative, zero, or positive, and depends on game features more than on the presence of punishment per se** (Kroupa, 2014; McBride et al., 2016).

# 5) Prediction Guidance

The literature supports **several generalizations for prediction:**
- If the control efficiency is high (i.e., baseline cooperation is already strong), then enabling punishment may have **little or even negative effect on efficiency** due to punishment costs (Kroupa, 2014; Ezeigbo, 2017).
- If the control efficiency is low (cooperation is fragile or rare), enabling punishment—especially with **low punishment cost, opportunity for communication/reputation, or other support mechanisms**—is likely to **increase efficiency, potentially dramatically (Asgharpourmasouleh et al., 2017; Luo & Zhao, 2013).**
- **Game design dimensions to adjust predictions upward**: more rounds (numRounds), presence of chat/communication (chat), ability to observe others’ punishments (showPunishmentId), lower punishment cost (punishment_cost), non-anonymous or reputation-enhanced settings. These all facilitate coordinated and effective punishment, reducing misuse and increasing the return on punishment investment (Kroupa, 2014; Vincent, 2017).
- **Design dimensions to adjust predictions downward**: high punishment cost, short games, high anonymity, absence of communication/reputation, or high risk of antisocial punishment. In these cases, punishment can be either ineffective or actively reduce efficiency (Kroupa, 2014; Ezeigbo, 2017).
- **Structural nuances** such as group size and network density interact with these effects, but the direction varies across models.
- Since **few papers report both control and treatment efficiency** for the same game-design cell, quantitative prediction is hazardous; qualitative or directional guidance is more robustly supported.
- Behavioral outcomes such as raised cooperation rates do not always translate into higher efficiency due to the direct cost of punishment (Kroupa, 2014).

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions (with payoff/efficiency evidence):**
- **player_count**: Analyzed in several theoretical and simulation works (e.g., effect of group size on punishment impact; findings mixed and sometimes only in dyads).
- **num_rounds**: Longer games facilitate more efficient punishment (Kroupa, 2014; Shinya et al., 2016).
- **punishment_cost**: Central parameter; lower cost often increases efficiency gains from punishment (Kroupa, 2014; Ezeigbo, 2017; Luo & Zhao, 2013; Vanderschraaf, 2016).
- **punishment_tech** (mechanism/severity): Varies in the literature; proportional or stronger punishment can improve efficiency given proper conditions (Luo & Zhao, 2013; Vanderschraaf, 2016).
- **chat**, **show_punishment_id**, **show_n_rounds**, **show_other_summaries**: Addressed especially in discussions of anonymity, reputation, and coordination (Kroupa, 2014; Vincent, 2017; Patrzyk & Takác, 2017).

**Indirectly or Partially Informed:**
- **mpcr** (marginal per capita return): Occasionally included, mainly when papers use canonical PGG or its analog (Asgharpourmasouleh et al., 2017).
- **all_or_nothing**, **default_contrib**: Sometimes manipulated; all-or-nothing structures make coordination more challenging, but efficiency effects are rarely central in analysis.

**Sparse or Contextually Discussed (little or no efficiency data):**
- **reward_exists**, **reward_cost**, **reward_tech**: Reward mechanisms appear as comparators or complements in a few studies, but are rarely the focus.
- **show_other_summaries**: Mentioned in network or information studies, with little direct efficiency impact analysis.

**Effectively Missing:**
- No paper addresses the joint experimental manipulation of all 14 dimensions with complete efficiency outcome reporting.

# 7) Important Limitations

- **Empirical data on standard PGGs with both control and punishment treatments, reporting efficiency as defined in the prediction task, is rare**—most findings are theoretical, computational, or drawn from adjacent games.
- **Few studies allow strong, quantitative prediction of treatment efficiency given both design dimensions and control efficiency.** Most insights are qualitative (directional).
- **Many outcome measures are non-payoff behavioral proxies** (e.g., cooperation rate), which cannot be assumed to indicate improved efficiency. Several papers explicitly show that raised cooperation does not guarantee higher payoff due to punishment costs (Kroupa, 2014; Ezeigbo, 2017).
- **Heterogeneity in punishment implementation** (self- vs third-party, proportional vs flat, individual vs group-based, availability of antisocial punishment) complicates generalization.
- **Game structural differences across studies (e.g., pairwise vs n-player, spatial vs random-matching, with or without partner choice)** limit the ability to aggregate or statistically pool findings for precise prediction.
- **Experimental and simulation contexts may omit relevant real-world moderators** (communication, real incentives, group norms) or exaggerate certain negative effects of punishment compared to more naturalistic or field environments (Kroupa, 2014).
- **Critical dimensions—such as the interaction of communication, anonymity, and punishment visibility—are insufficiently investigated in relation to efficiency outcomes.**
- **No study in this set offers a comprehensive predictive model or formula** calibrated with empirical data across the full range of design parameters and control efficacies.

**Conclusion:**  
This paper set offers strong qualitative and mechanistic guidance on when and why enabling peer punishment in public-goods-like games may increase or decrease group efficiency, and which design features moderate that effect. The direct, quantitative prediction of treatment efficiency as a function of design and control efficiency is only weakly supported, due to gaps in empirical data, inconsistent outcome measures, and structural heterogeneity across studies. Prediction efforts should therefore use the literature to inform qualitative priors and adjust expectations, especially around the role of punishment cost, communication, and game length, but should avoid strong quantitative claims unsupported by the evidence base.
