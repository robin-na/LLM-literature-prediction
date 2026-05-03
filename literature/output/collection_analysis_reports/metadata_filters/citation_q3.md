# 1) Evidence Base

The provided paper set is exceptionally large and diverse, with 693 entries covering empirical, experimental, theoretical, and simulation-based studies. For the specific task—predicting how enabling peer punishment changes efficiency in public-goods-game (PGG) environments given control efficiency and design dimensions—the core sample is broad and robust. There are numerous lab experiments, field experiments, and theoretical models that directly manipulate and analyze many of the core PGG dimensions. However, relevance to PGGs with explicit efficiency/payoff outcomes is higher in a subset (~dozens) of these studies; many studies focus primarily on contributions or behavior, or only peripherally address efficiency.

The set includes extensive empirical evidence (laboratory, field, cross-cultural), substantial theoretical and simulation work (evolutionary dynamics, analytical models), and insightful reviews and meta-analyses. Some entries strictly adhere to the canonical linear PGG, while others examine variants (e.g., common-pool resource games, trust games, exclusion/ostracism, contest games), and a significant minority are only adjacent or weakly connected. Both direct and indirect evidence on efficiency is available, with some studies reporting direct efficiency ratios and others requiring inference from payoffs or related measures.

# 2) Task Relevance

- **pgg_or_variant**
  - *exact*: Numerous papers (especially in the top of the digest) deal with repeated linear PGGs or closely matched variants (common resource, snowdrift, exclusion, team production).
  - *close*: Many examine threshold games, contest games, or dyadic dilemmas (repeated PD, trust games) with punishment mechanics; these are highly informative when mapped carefully.
  - *adjacent/weak*: A sizable portion investigate one-shot, non-group, or highly modified games—these are less central for direct efficiency prediction.
- **punishment_or_sanctions**
  - *exact*: Many empirical and theoretical papers explicitly test the enabling/disabling of costly peer punishment, institutional punishment, exclusion, and their key parameters (cost, effect, information, role selection).
  - *close*: Several study reward, social sanctions (e.g., costless disapproval), or combined mechanisms; others analyze exit/threat, exclusion, or institutional selection, yielding useful contextual insight.
  - *adjacent/weak*: There is a large adjacent literature concerned entirely with contribution or with reputation/gossip, moral framing, and peer monitoring.
- **efficiency_or_related_payoff_outcome**
  - *exact*: About two dozen experimental studies and a substantial number of theoretical papers directly report group earnings, payoffs, welfare, or ratios to maximum possible payoff under full cooperation.
  - *close*: Many report total contributions (implying, but not equal to, efficiency), or related outcomes such as group profit, surplus, or likelihood of public-good provision (in threshold settings).
  - *adjacent/weak*: A large number focus only on behavioral variables (contribution frequency, punishment assignment, trust, etc.), and some do not report efficiency or closely related payoffs at all.

# 3) Outcomes Measured In The Literature

- **Payoff/Efficiency-based outcomes (suitable for prediction task):**
  - Efficiency ratios (as % of the full cooperation payoff)
  - Group earnings, profits, mean payoffs, surplus, group welfare (sometimes need calculation)
  - Aggregate reductions in resource overuse (for common-pool resource games)
  - Frequency of provision in threshold PGGs (i.e., fraction of rounds/groups reaching provision, where the step function allows mapping to efficiency)
- **Non-payoff, behavioral or psychological outcomes (not equivalent to efficiency):**
  - Contribution rates (mean contribution, cooperation frequency)
  - Punishment rates, frequency, or magnitude assigned
  - Sanctioning/reward assignment, approval/disapproval rates
  - Norm compliance, trust, in/out-group preference, fairness judgments, emotional drivers
  - Group composition, subject heterogeneity, or personality-based correlates
- **Studies reporting only behavioral outcomes must not be treated as reporting on efficiency, though they may indicate directionality under well-understood mappings (e.g., in standard linear PGGs, increased contribution typically maps to increased efficiency unless punishment costs overwhelm gains).**

# 4) Main Findings Relevant To Prediction

*Synthesizing across high-quality, directly relevant papers:*

- **Punishment enables higher contribution, but efficiency gains depend on game structure and punishment design.**
  - In *standard linear PGGs* with costly peer punishment, enabling punishment typically raises contributions but may or may not increase efficiency due to the deduction of punishment costs from group earnings. The sign and size of the net efficiency effect is highly sensitive to:
    - The cost/effectiveness ratio of punishment (punishment tech and cost): High-impact, low-cost punishment is most likely to increase efficiency (Engelmann & Nikiforakis, 2015; Levine & Modica, 2016).
    - The propensity for antisocial punishment (punishing cooperators or retaliation): Where antisocial punishment is common (e.g., in some cultures or with random matching), efficiency gains are reduced or even reversed (Bruhin et al., 2020; Bortolotti et al., 2015).
    - The punishment structure (peer vs. central/democratic): Centralized, democratic, or leader-administered punishment is more likely to improve efficiency, as it curbs both antisocial punishment and excess costs (Harrell & Simpson, 2016; Nockur et al., 2021; Pfattheicher et al., 2018).
    - The information structure: Punishment regimes with full transparency about contributions and punishers' identities lead to more accurate targeting and less antisocial punishment, improving efficiency (Faillo et al., 2013; Kamei & Putterman, 2015).
    - The alignment of local and global incentives: Punishment increases efficiency primarily when group members' interests are aligned with the social optimum (Ozono et al., 2020).
- **Contextual moderators of the efficiency effect:**
  - *Group composition (heterogeneity)*: When endowments or returns are unequal, or when groups are culturally diverse, punishment's effect on efficiency is moderated or neutralized, and can even decrease efficiency due to increased antisocial punishment or misapplication (Kingsley, 2016; Gangadharan et al., 2017; Bortolotti et al., 2015).
  - *Subject pool behavior*: Students often exhibit more responsive and pro-social punishment, with higher resulting efficiency, than broader, more representative samples (Bortolotti et al., 2015).
  - *Baseline/control efficiency*: In designs where control (no-punishment) efficiency is already high, adding punishment tends to yield little improvement or can even reduce efficiency because punishment costs overwhelm minor cooperation gains (Shinada & Yamagishi, 2008; Nair et al., 2018).
  - *Game length (number of rounds)*: Longer games allow the costs of punishment to amortize and can result in efficiency overtaking recommendations/communication treatments in the long run (Chaudhuri & Paichayontvijit, 2017).
- **Variants and exceptional outcomes:**
  - *Costless punishment (non-monetary approval/disapproval)*: Costless disapproval often increases both cooperation and efficiency, as the behavioral effect is achieved without decrementing payoffs (Dugar, 2013).
  - *Punishment via exclusion/ostracism*: Exclusion is often as effective or more effective than token-based costly punishment for raising efficiency, provided the cost to the group is not too high (Dannenberg et al., 2020; Wang & Perc, 2022; Liu & Chen, 2020).
  - *Centralized/third-party punishment*: Central enforcement, especially if honest/corruption-resistant, typically improves efficiency, sometimes more than decentralized peer punishment, particularly in large groups or complex environments (Engel & Zhurakhovska, 2017; Lee et al., 2015).
  - *Environmental/structural moderators*: The presence of network structure (asymmetric monitoring or incomplete punishment networks) can severely reduce or eliminate the efficiency gains from punishment (Boosey & Isaac, 2016; Leibbrandt et al., 2015).

# 5) Prediction Guidance

- **Baseline/control efficiency is an essential predictor, but the effect of enabling punishment is not a fixed function of baseline efficiency alone; it interacts with:**
  - *Punishment cost/effectiveness*: Use experimental data from close matches in group size, MPCR, and punishment ratio wherever possible. High cost/ineffective punishment often yields net zero or negative efficiency effect (Simpson et al., 2017; Shinada & Yamagishi, 2008).
  - *Punishment structure*: Expect larger efficiency boosts from central, leader, or democratic punishment than peer punishment, particularly in larger or heterogeneous groups (Harrell & Simpson, 2016; Nockur et al., 2021; Pfattheicher et al., 2018).
  - *Antisocial punishment prevalence*: Where antisocial punishment is likely (based on subject pool/cultural parameters), enable a downward adjustment on the expected efficiency effect (Bruhin et al., 2020).
  - *Network/information structure*: Incomplete punishment networks or noisy/missing feedback will often result in muted or negative efficiency gains (Boosey & Isaac, 2016; Leibbrandt et al., 2015).
  - *Endowment and return heterogeneity*: High heterogeneity with no mechanism to reveal type during punishment mapping can void the efficiency effect (Kingsley, 2016).
  - *Game length*: Expect larger treatment–control efficiency deltas in longer games, as initial punishment costs are amortized, unless over-punishment spirals are triggered (Chaudhuri & Paichayontvijit, 2017).
- **Costless and/or non-monetary punishment (e.g., disapproval, social signals) is more likely to increase efficiency than costly, peer-based punishment where costs may outweigh cooperation gains (Dugar, 2013; Peeters & Vorsatz, 2013).**
- **Environments where reward mechanisms are possible and not too costly may yield higher efficiency than punishment-enabled games if reward tech is more efficient or if the environment admits anti-social punishment in peer regimes (Dong et al., 2019; Han, Duong & Perc, 2024).**
- **Key dimension-specific empirical findings to leverage in prediction:**
  - *MPCR*: Higher MPCR (>0.5) environments yield larger efficiency gains from punishment, sometimes up to or above the voluntary contribution level (Chaudhuri & Paichayontvijit, 2017; Levine & Modica, 2016).
  - *Punishment cost/effectiveness (punishment_tech)*: For example, a 1:3 cost-impact ratio is common in lab studies and generally sufficient for seeing moderate efficiency increases, but variations have large effects.
  - *Group size (player_count)*: Increases in group size reduce the effectiveness of peer punishment unless punishment is centralized or network structure is carefully controlled (Levine & Modica, 2016; Powers & Lehmann, 2017).
  - *Chat/communication (chat)*: Chat itself increases efficiency, sometimes surpassing the effect of punishment; if both are present, expect additive or substitutive effects but not always superadditive (Kagel, 2018).
  - *All-or-nothing vs. continuous contributions (all_or_nothing)*: Step-level games (all or nothing) sometimes show larger efficiency gains from punishment (especially central/exclusion mechanisms), but continuous PGGs allow more nuanced response effects.
  - *Show_n_rounds/show_other_summaries/show_punishment_id*: Increased feedback and transparency generally support more effective, less antisocial punishment, leading to larger efficiency improvements (Faillo et al., 2013).
- **When using papers for model training or calibration, prioritize those with explicit reporting of both control and punishment-enabled efficiency, close dimensional mapping, and direct manipulation of relevant design features.** A representative list includes: Simpson et al. (2017), Ozono et al. (2020), Dickinson et al. (2015), Gürerk et al. (2018), Gürerk et al. (2009), Engl et al. (2021), Kuwabara & Yu (2017), Kingsley (2016), Faillo et al. (2013), Leibbrandt et al. (2015), Harrell & Simpson (2016), Nicklisch et al. (2016), Markussen et al. (2016), Chaudhuri & Paichayontvijit (2017).

# 6) Design Dimensions Highlighted Across Papers

**Directly informed (with substantial, multiple-source evidence):**
- *player_count*: Small groups (n=3–5) are the norm in lab experiments; scaling effects investigated in both empirical and theoretical papers.
- *num_rounds*: Both short and long (up to 50) repeated games are represented; long games show punishment paying off via sustained cooperation.
- *mpcr*: MPCR is systematically varied; evidence shows efficiency gains from punishment increase with higher MPCR.
- *punishment_cost* & *punishment_tech* (cost and impact): Explicitly manipulated in many lab experiments and theoretical analyses.
- *punishment_exists*: Directly manipulated in dozens of experiments.
- *all_or_nothing*: Reported in both continuous and step-level (threshold) versions; design differences highlighted in some studies.
- *chat*: Presence/absence of communication well studied; interacts with punishment mechanisms.
- *show_other_summaries*, *show_n_rounds*, *show_punishment_id*: Several experiments manipulate information provision (feedback, identity of punishers, history), with direct implications for both antisocial/inefficient punishment and efficiency gains from punishment.
- *reward_exists*, *reward_cost*, *reward_tech*: Available in some studies (reward vs. punishment, reward cost, reward effectiveness), enabling direct comparison.

**Indirectly informed:**
- *default_contrib*: Some studies vary the default contribution framing (opt-in/opt-out, default allocation), showing modest framing effects, but not systematically studied as a moderator of the punishment–efficiency relationship.
- *show_punishment_id*: A few studies test anonymity/transparency in punishment, with evidence that transparency can both improve targeting (pro-social punishment increases efficiency) and increase antisocial punishment (if anonymity undermines restraint).

**Contextually discussed or partially addressed:**
- *group heterogeneity* (not a direct dimension but implied under endowment, productivity, or return type): Multiple papers discuss (and sometimes manipulate) heterogeneity, but this interaction is less systematically linked to prediction dimensions.

**Effectively missing (little or no coverage):**
- *Some specific interaction effects between rare design features (e.g., the presence of multiple simultaneous games, rare parametric edge cases) are missing or only weakly implied.*

# 7) Important Limitations

- **Papers often conflate contribution increases with efficiency gains.** Many studies report increased contributions under punishment but do not directly analyze whether group payoffs, net of punishment costs, actually rise above the control no-punishment condition. Prediction must distinguish these outcomes.
- **Efficiency effect is not universal; substantial negative or null effects** are found where:
  - Antisocial punishment is common or unrestrained.
  - Punishment is costly, poorly targeted, or applies to a heterogeneous group without clear defectors.
  - Control (no punishment) efficiency is already high or the efficiency gain from additional cooperation is small relative to punishment costs.
- **Lab studies overwhelmingly use small, homogeneous, Western student samples,** so cross-cultural and demographic generalization is limited. When more diverse samples are used, effects of punishment can be neutral or negative (Bortolotti et al., 2015).
- **Subject pool heterogeneity and group composition are strong moderators** that are often omitted from prediction models (e.g., attitude toward punishment, propensity for antisocial punishment, cooperativeness).
- **Complex interaction effects** exist: The benefit of punishment is non-additive when combined with communication, reward, or exclusion mechanisms, and models may require higher-order interactions to capture reality accurately.
- **Many adjacent/weak papers report only on behavior (not efficiency),** making it risky to include them in model building or to extrapolate from them for efficiency predictions.
- **Some important design features (e.g., unequal returns, complex peer networks, dynamic reputation systems) are underexplored,** and evidence is sparse or theoretical rather than empirical.
- **The effectiveness of punishment typically declines with group size unless institutionalized, coordinated, or centralized punishment is used.**
- **In dynamic or noisy environments (e.g., noisy information about contributions), punishment can backfire,** reducing efficiency due to mis-targeting and increased retaliation.
- **Rare or bespoke treatment combinations (e.g., probabilistic punishment, multi-level sanctions, second-order free-rider treatments) may lack extensive empirical calibration.**
- **Long-run or field effects (e.g., spillovers to subsequent games, cultural transmission, institution-building) are less well documented with direct efficiency measures.**

---

**In summary:**  
The literature base supports robust, context-sensitive prediction of the efficiency impact of enabling peer/central punishment in PGG-like environments, especially when control efficiency, MPCR, group size, rounds, punishment parameters, and information structure are accounted for. The effect of punishment on efficiency is highly moderated by these dimensions, as well as by subject pool composition and institutional design. Increased contribution is common under punishment but does not always translate to efficiency gains due to punishment costs, antisocial punishment, and poor targeting. Predictions should use directly relevant, efficiency-reporting studies to the extent possible, and ambiguity should be explicitly modeled in uncertain or conflict-laden domains. Adjacent literature focusing solely on contribution or on mechanism should be treated as contextual, not predictive, for efficiency.
