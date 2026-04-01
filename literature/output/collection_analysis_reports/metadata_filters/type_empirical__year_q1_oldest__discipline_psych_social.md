# 1) Evidence Base

The paper set comprises a large, diverse corpus (122 papers), primarily empirical—dominated by experimental laboratory studies, with some field experiments and observational research for context. The set is **broad in coverage** but **narrower in direct relevance** to the downstream prediction task of estimating treatment (punishment-enabled) efficiency in public-goods-game-like (PGG) environments, given game design dimensions and control (no-punishment) efficiency.

- **Empirical findings** in *standard PGG settings with punishment manipulation* are well-represented, especially for small- to medium-sized groups, repeated games, and standard peer punishment frameworks (e.g., Fehr et al., 2002; Gintis et al., 2003; Barclay, 2004).
- There is a significant body discussing *theoretical mechanisms*, *moral/psychological aspects*, or *behavioral outcomes* (e.g., changes in contribution, cooperation rates), which, while informative, do not report efficiency or payoff directly.
- **Exact evidence** on efficiency responses to punishment for the full diversity of game design configurations (e.g., presence of chat, default contribution framing, identity salience, all reward/punishment tech options) is *incomplete*.
- Papers covering related dilemmas (e.g., resource dilemmas, trust games, dictator/ultimatum games) and non-payoff outcomes are **adjacent or weakly relevant** and mainly provide context rather than direct estimates.

In summary, the empirical base is rich for *standard PGGs with peer punishment*, but less so for edge-case game designs or more recent implementation features. Mechanistic, psychological, and correlated behavioral outcomes are prevalent but must be separated from direct payoff-based findings.

# 2) Task Relevance

Assessed along three axes: `pgg_or_variant`, `punishment_or_sanctions`, `efficiency_or_related_payoff_outcome`:

- **PGG or variant:**  
  - A substantial subset studies *exact PGGs*, and several use close variants (e.g., resource dilemmas, step-level games, n-person PDs, trust games).
  - **Relevance labels:**  
    - *Exact*: Fehr et al. (2002), Gintis et al. (2003), Decker et al. (2003), Barclay (2004), Masclet (2003), Reuben & Riedl (2009), Fatas et al. (2010), etc.  
    - *Close/Adjacent*: Some resource dilemmas, centralized allocation, or step-level threshold PGGs (Ostrom et al., 1992; Webb & Foddy, 2004).
    - *Weak/None*: Dictator, trust, and ultimatum games unless used with group interaction or efficiency reporting.

- **Punishment or sanctions:**  
  - Many papers manipulate the *presence/absence* of *peer punishment* or *sanctioning* mechanisms.
  - Some focus on *reward mechanisms*, *ostracism*, *centralized sanctions,* or *exclusion* as alternatives or complements.
  - **Relevance labels:**  
    - *Exact*: Studies that directly enable/disable costly peer or centralized punishment.
    - *Close*: Exclusion/ostracism mechanisms, collective or institutional sanctions.
    - *Adjacent/Weak*: Feedback, reputation, or approval/disapproval systems with or without material consequences.

- **Efficiency or related payoff outcome:**  
  - Only a subset reports *group efficiency*, total payoff, or welfare as the main, quantitative dependent outcome.
  - Most other studies focus on *contribution/cooperation rate*, norm compliance, or punishment frequency.
  - **Relevance labels:**  
    - *Exact*: Papers reporting group efficiency, surplus, or total earnings (normalized relative to the cooperative maximum).
    - *Close/Adjacent*: "Welfare" or "earnings" discussed, but not systematically or not as the primary outcome.
    - *Weak/None*: Only behavioral outcomes or attitudes reported.

Overall, the core empirical literature *most relevant for predictive modeling* consists of a select subset: lab-experimental PGGs with explicit, parameterized punishment treatments and direct efficiency or surplus measurement. Many others are supportive or informative, particularly for moderators and context, but do not offer direct, parameterized treatment effects.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:**
  - *Efficiency/Surplus/Group Payoff/Total Earnings*:  
    - Some studies (Fehr et al., 2002; Gintis et al., 2003; Reuben & Riedl, 2009; Masclet, 2003; Fatas et al., 2010; Barclay, 2004) report the main prediction target, often as a proportion of the maximum possible cooperative payoff.
    - Immediate and net (post-cost) effects are inconsistently distinguished; some report only total output before punishment/reward costs.
  - *Resource Preservation/Threshold Provision*:  
    - Some step-level or resource dilemma papers report payoff as "provision success" or resources preserved, which is sometimes used as a surrogate for efficiency.

- **Behavioral (non-payoff) outcomes:**  
  - *Contribution rate / cooperation rate* (most common):  
    - Increases with punishment are reliably observed, but translation into efficiency is *not* automatic (punishment costs may outweigh gains).
  - *Punishment frequency/intensity, norm compliance, moral judgments, trust, attitudes:*  
    - Studied extensively as explanatory mechanisms or in contextual analyses.
  - *Punishment assigned, reward frequency, exclusion votes, psychological mediators (anger, trust, fairness):*  
    - Often reported but not directly mapped to group payoff.

- Explicit separation is necessary: **improved contributions do not guarantee increased efficiency** if punishment is costly or if negative externalities are present.

# 4) Main Findings Relevant to Prediction

Synthesizing across core and peripheral studies with emphasis on *efficiency* as specified:

- **Peer punishment generally increases contributions and can increase efficiency,** but only when *the gains from increased cooperation significantly exceed the costs of punishment* (Fehr et al., 2002; Gintis et al., 2003; Masclet, 2003; Barclay, 2004).
  - In many *standard repeated PGGs* (typical settings: 3–4 players, 10 rounds, MPCR ~0.4–0.5, no chat, continuous contributions), **punishment-enabled efficiency is markedly higher than control**, often approaching 30–40% increases (Fehr et al., 2002; Gintis et al., 2003).
- **Punishment increases contributions more than rewards,** but **rewards may produce higher net efficiency** due to positive payoff effects (Gürerk et al., 2009).
- **Cost structure matters:**
  - *High punishment costs*: The net efficiency gain can be diminished or negative if excessive punishment is used or misapplied (emotional punishment, spite, or anti-social motives).
  - *Low-moderate punishment costs, high effectiveness*: More likely to yield positive efficiency effects.
  - *Collective/centralized vs. individual punishment*: Centralized or leader-administered punishment can be more or less efficiency-enhancing depending on targeting and consent structures (Gürerk et al., 2009; Reuben & Riedl, 2009; Ostrom et al., 1992).
- **Social context and group composition moderate outcomes:**
  - *Homogeneous groups*: More likely to realize efficiency gains from punishment (Reuben & Riedl, 2009; Barclay, 2004).
  - *Heterogeneity, privilege, or group-based norms/cultural variation*: May reduce or reverse efficiency effects (Barclay, 2004; Reuben & Riedl, 2009).
  - *Cultural or ethnic diversity*: Sometimes increases the efficacy of punishment by altering group dynamics.
- **Design features interact with punishment effectiveness:**
  - *Repeated interactions/partner matching*: Amplifies the positive impact of punishment on efficiency (Balliet et al., 2011; Fehr et al., 2002).
  - *Communication*: Strongly synergistic with punishment; maximizes efficiency gains when combined (Ostrom et al., 1992).
  - *Punishment severity/structure*: Overly severe or untargeted punishment can *reduce* efficiency despite higher cooperation (Decker et al., 2003; Tenbrunsel & Messick, 1999).
- **Alternative mechanisms (ostracism, centralized allocation, reputation transfer):**
  - *Non-monetary punishment (ostracism/exclusion)* can increase efficiency substantially and may avoid direct costs of monetary punishment (Masclet, 2003; Hamman et al., 2011).
  - *Centralized/reputation-based mechanisms* (Hamman et al., 2011; Semmann et al., 2004) may achieve similar or even higher efficiency without punishment per se.
- **Failure cases and negative/ambiguous effects:**
  - When *punishment is used excessively, anti-socially, or mis-targeted*, efficiency can decline (Abbink et al., 2004; Goette et al., 2012).
  - *Step-level (threshold) games or settings with high asynchrony*: Efficiency gains from punishment are less reliable or even negative unless coordinated with communication or institutional choice (Ostrom et al., 1992; Mulder et al., 2006).
  - *Games with alternative defection options*: Punishment may not increase and can sometimes reduce efficiency if players can evade sanctions (Mulder et al., 2006, 2009).
- **Path dependency and persistence:** The history of incentives (e.g., sequence of reward and punishment, removal of sanctions) affects both cooperation rates and efficiency in subsequent periods (Gürerk et al., 2009; Chen et al., 2009).

# 5) Prediction Guidance

The literature supports the following core inferences for prediction:

- **When the control (no-punishment) efficiency is low and the PGG is standard, enabling peer punishment usually increases efficiency—often substantially—but the magnitude depends on game design details.**
  - **Key moderators (from evidence):**  
    - *MPCR*: Higher effectiveness of punishment in moderate-to-high MPCR regimes.
    - *Punishment cost and magnitude*: Need to be balanced for optimal effect; high costs or excessive severity can offset efficiency gains.
    - *Number of players*: Efficiency gains are more robust in small to moderate-sized groups (n=3–5).
    - *Number of rounds*: Gains are larger and more consistently realized in repeated games (≥10 rounds).
    - *Communication and information*: Synergistically amplifies efficiency effects; lack of communication may suppress positive impact.
    - *Cultural/group context*: Heterogeneity (privilege, ethnic divisions, low group identification) may reduce or even reverse efficiency gains.
    - *Punishment structure (centralized vs. decentralized, collective consent rules)* moderates impact on both contributions and efficiency.
- **Control efficiency is a strong predictor of achievable efficiency with punishment enabled, but the *increment* is not monotonic:**  
  - *Very low control efficiency* settings allow for the largest positive swings.
  - *Relatively high control efficiency* (e.g., due to strong intrinsic cooperation, communication, or alternative mechanisms) may see *little or no gain* from adding punishment, and sometimes negative returns if punishment is used unwisely.
- **Do not assume that increased cooperation or contribution rates under punishment will automatically yield proportionate efficiency gains.**  
  - Check whether the punishment cost structure and use rates plausibly overwhelm the group payoff improvements from increased cooperation in similar game parameters.
- **Where both peer punishment and peer reward are available, reward mechanisms sometimes produce higher efficiency/performance, even if punishment elicits more immediate norm compliance.**
- **In step-level/threshold-tied collective action, two-choice or simple settings, or when "bad" defection options exist, punishment's effect on efficiency becomes less reliable and highly context-sensitive.**

# 6) Design Dimensions Highlighted Across Papers

A mapping of prediction dimensions and degree of direct/indirect evidence:

| Dimension               | Informed Directly | Informed Indirectly | Contextual Only / Missing      |
|-------------------------|------------------|---------------------|------------------------------|
| `player_count`          | Yes              | -                   | -                            |
| `num_rounds`            | Yes              | -                   | -                            |
| `chat`                  | Yes (sometimes)  | -                   | Often missing in detail      |
| `all_or_nothing`        | Yes              | -                   | -                            |
| `default_contrib`       | Rare             | Sometimes (adjacent)| Often missing/subsumed       |
| `mpcr`                  | Yes              | -                   | -                            |
| `punishment_cost`       | Yes              | -                   | -                            |
| `punishment_tech`       | Yes (standard, ostracism)| Yes (collective, centralized)| Less so for non-monetary/nonstandard types |
| `reward_exists`         | Yes, but less common| Yes               | -                            |
| `reward_cost`           | Sometimes        | -                   | Often missing                |
| `reward_tech`           | Sometimes (peer, leader)| Indirect cases | Sparse for advanced or real-world reward tech|
| `show_n_rounds`         | Sometimes explicit| Contextual         | Many papers silent           |
| `show_other_summaries`  | Occasional       | Frequent context    | Often not a main manipulation|
| `show_punishment_id`    | Seldom           | Yes, for centralized/leader| Sparse in peer punishment studies          |

More specifically:
- **Direct evidence is strong** for: `player_count`, `num_rounds`, `mpcr`, `all_or_nothing`, `punishment_cost`, and basic `punishment_tech`.
- **Indirect or incomplete** for: `chat`, `default_contrib`, `show_punishment_id`, and advanced/structural features of reward/punishment (`punishment_tech`, `reward_tech`).
- **Contextual/missing** for: identity features (`show_punishment_id`), default contribution settings/framing, technological subtleties, or real-world institutional variants.

# 7) Important Limitations

- **Not all game configurations are covered:** Most direct empirical results come from *standard, small-group repeated games* with specific parameterizations. For more complex or recent designs (e.g., with chat, opt-in/opt-out framing, dynamically changing MPCR, technologically advanced punishment/reward systems, or large groups), *direct transferability is uncertain*.
- **Payoff outcomes and behavioral outcomes are often conflated or unreported:** Many studies use *contribution rate* as the main outcome; efficiency must sometimes be inferred, not directly measured—so translation to exact predictions can be error-prone if cost structures are not explicit.
- **Moderators and context effects are often underreported or not systematically varied:** For example, *cultural, ethnic, group identification*, or *social norm strength*—which have been shown to shift both the use and effects of punishment—are usually not fully explored within any single design or set of parameter values.
- **Existing studies rarely map multi-dimensional design spaces exhaustively:** Interactions among dimensions (e.g., MPCR × punishment cost × group size × communication) are often not factorially crossed, limiting quantitative predictive power for out-of-sample combinations.
- **Behavioral spillovers and longer-term consequences are unclear:** Several findings show that effects of punishment may *backfire* or dissipate if removed (e.g., Chen et al., 2009; Mulder et al., 2006), and path dependence exists; current literature only partially addresses these dynamic effects.
- **High baseline (control) efficiency or effectiveness of alternative mechanisms (reputation, communication, endogenous delegation) can saturate efficiency, limiting additional gains from punishment.**
- **Edge-case or nonstandard punishment mechanisms (exclusion, ostracism, blind punishment) are less well documented in terms of efficiency impact.**
- **Publication bias and reporting practices may overstate positive punishment effects due to nonreporting of null or negative findings.**

---

**Conclusion:**  
The literature gives robust, empirically grounded guidance for *standard PGGs with peer punishment enabled*, particularly when control efficiency is low and design parameters match the canonical lab settings. Punishment is *not* universally efficiency-enhancing: its effects are often *contingent*, sometimes *negative*, and tightly bound to cost structure, targeting, group composition, and social/institutional context. *Precise prediction* is best supported for standard, small-group, repeated PGGs with explicit, parameterized punishment; more complex or novel environments require extrapolation and caution, as evidence grows thinner or more ambiguous.
