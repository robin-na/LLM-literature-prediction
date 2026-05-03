# 1) Evidence Base

The paper set is broad and predominantly theoretical, consisting of review or formal modeling papers rather than original empirical studies or experimental datasets. Of the 47 papers, almost all are theory or conceptual integration, with a minority providing simulation-based results or referencing external empirical literature. Many papers discuss mechanisms, moderators, and conditions in public-goods-game (PGG) environments or adjacent settings (e.g., repeated Prisoner's Dilemma, common-pool resource dilemmas). Very few papers provide direct, quantitative, empirical evidence on the efficiency effects of enabling punishment within PGGs.

Within the exact PGG and punishment domain, a small subset of papers (e.g., Prétôt et al., 2024; Zhang & Pei, 2022) offers formal payoff-based analysis or direct summaries from empirical/theoretical synthesis. Several adjacent papers (e.g., Gioffré & Tampieri, 2025; Libois, 2022; Melkonyan et al., 2022) model closely related games and report explicit welfare or efficiency implications of punishment mechanisms, but not within standard lab PGGs. Most remaining papers focus on non-payoff behavioral outcomes (contribution rates, norm adherence) or on contextual and mechanism arguments at a high level.

In sum, there is:
- A strong theoretical and mechanism-driven base.
- Scarce direct empirical data on treatment efficiency, with most efficiency-relevant findings in theoretical or adjacent-game contexts.
- Substantial indirect and contextual evidence about how punishment and various design features affect behavior or, more rarely, group payoff.

# 2) Task Relevance

**a) PGG or Variant**  
- Most highly relevant papers model PGGs (or CPR games) directly (`exact` relevance). Several core findings come from these, with a minority focusing on direct public goods settings (Prétôt et al., 2024; Zhang & Pei, 2022).  
- Many other contributions are `close` or `adjacent`, studying repeated Prisoner's Dilemma, club goods, or donation games, which share core dilemmas with PGGs.

**b) Punishment or Sanctions**  
- Around a dozen theoretical contributions focus on, or at least consider, punishment as a core mechanism (`exact` or `close` relevance). Key PGG punishment mechanisms—peer, institutional, probabilistic—are discussed in theory and simulations.  
- Several papers also address adjacent norm enforcement tools (reputation, gossip) but these are less directly informative for peer punishment effects.

**c) Efficiency or Related Payoff Outcome**  
- Direct measurement of efficiency (ratio of achieved to maximal group payoff) or group payoff is limited (`exact` in only a handful of papers).  
- More commonly, outcomes are cooperation rates, behavioral proxies, or theoretical welfare implications (`adjacent` or `close` relevance for payoff).  
- Only a few contributions offer explicit formulas or comparative statics relating punishment design to efficiency (e.g., Prétôt et al., 2024; Libois, 2022).

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes** (group efficiency, total payoff, welfare, surplus):  
  - Papers such as Prétôt et al. (2024), Gioffré & Tampieri (2025), Libois (2022), Han et al. (2022), Melkonyan et al. (2022), and Uchida et al. (2024) directly report or model group efficiency as affected by punishment and other design parameters.
  - Some review papers (Zhang & Pei, 2022) include summary statements about the tradeoff between increased cooperation and reduction in group earnings due to costly punishment.

- **Non-payoff behavioral outcomes** (contribution rate, cooperation rate, norm compliance, punishment frequency):  
  - Most papers (e.g., Lazarus, 2023; Odouard et al., 2023; Otten et al., 2024) emphasize behavioral side effects (cooperation, norm compliance) without direct reference to welfare, efficiency, or payoff-based metrics.
  - Many outcome claims about the efficacy of punishment are thus based on cooperation/contribution rates rather than efficiency in the predictive task sense.

- **Other outcomes**:  
  - A few theoretical papers discuss emergence and stability of norms, cultural adaptation, or psychological correlates (trust, fairness) as outcomes.

# 4) Main Findings Relevant To Prediction

### Synthesis

- **Institutional vs. Peer Punishment**:  
  - Institutional (collective, centralized) punishment nearly always increases efficiency if sufficiently funded and credibly enforced (Prétôt et al., 2024; Libois, 2022; Han et al., 2022).  
  - Peer punishment may fail to increase and can even decrease efficiency due to costs (Zhang & Pei, 2022), second-order free-riding, and social retaliation (Levy, 2022; Rumble et al., 2022).

- **Critical Thresholds and Design Moderators**:  
  - Efficiency gains depend on punishment cost, punishment effectiveness, group size, and MPCR. If punishment is too costly or too mild, efficiency increase is unlikely (Prétôt et al., 2024; Gioffré & Tampieri, 2025; Libois, 2022).
  - Many models specify explicit thresholds (e.g., minimum investment in monitoring, minimum effectiveness/fine for punishment).

- **Cost of Punishment and Second-order Dilemmas**:  
  - Even where punishment raises cooperation, the cost paid by punishers can lead to net decreases in group earnings ("costly punishment paradox", Zhang & Pei, 2022; Rumble et al., 2022).
  - Excessively severe or misapplied punishment can crowd out intrinsic cooperation and lower efficiency (Hernandez et al., 2022).

- **Reward vs. Punishment**:  
  - Reward and punishment are both mechanisms for promoting cooperation, but reward generally imposes less cost on group welfare, and is sometimes more “efficient,” especially in noisy environments (Wu et al., 2022).

- **Psychological/Behavioral Moderators**:  
  - The efficacy of punishment for efficiency is moderated by norm psychology (presence of norm internalizers increases indirect efficiency through higher cooperation: Odouard et al., 2023).
  - Prospect-theoretic agents may overreact to even mild punishment, enhancing cooperation and efficiency gains from mild punishments (Uchida et al., 2024).

- **Contextual Moderators**:  
  - Group identity, communication, observability, and audience effects can augment or diminish punishment's positive effects (Lazarus, 2023; Zachník, 2023; Van Lange & Rand, 2022).

- **Ambiguities and Disagreement**:  
  - Some models and reviews caution that peer punishment often fails to deliver efficiency improvements and can worsen outcomes under realistic conditions (Rumble et al., 2022; Milinski, 2022).  
  - There is debate on whether punishment is reliably effective (see contrast between high optimism in some theoretical models and mechanism-based skepticism in others).

# 5) Prediction Guidance

- **Direct implications**:  
  - If institutional (collectively funded) punishment is enabled with sufficient investment, and punishment is credible and not prohibitively costly, efficiency will increase—sometimes up to the fully cooperative level, conditional on other key parameters (Prétôt et al., 2024; Libois, 2022; Gioffré & Tampieri, 2025).
  - In contrast, enabling peer punishment often does NOT reliably increase efficiency and may even decrease it due to direct costs and retaliation/crowding out effects (Zhang & Pei, 2022; Rumble et al., 2022; Hernandez et al., 2022).

- **Dimension sensitivity**:  
  - Efficiency effect sizes are strongly conditional:  
    - **player_count**: Larger groups can make enforcement harder and reduce net gains from punishment (Libois, 2022; Prétôt et al., 2024), though some models show gains are size-invariant with strong enough sanctions (Gioffré & Tampieri, 2025, in repeated PD).
    - **mpcr**: Marginal returns to contribution interact with punishment effectiveness—low MPCR games may need much stronger punishment to yield efficiency gains.
    - **punishment_cost/punishment_tech**: High punishment cost or low effectiveness undermines efficiency gains.
    - **reward_exists/reward_cost/reward_tech**: Presence of rewards can substitute, complement, or in some environments surpass the efficiency benefits of punishment (Wu et al., 2022; Hua & Liu, 2024).

- **Indirect/Contextual guidance**:  
  - Effects of chat, observability, group identity, and audience are generally positive but act primarily through increasing cooperation, not always through increased efficiency if cost of enforcement is nontrivial.

- **Empirical caution**:  
  - Most available evidence for exact PGGs is theoretical or simulation-based. Actual effect sizes are context-dependent, and predictions should carry large uncertainty, especially for peer punishment in finite, small groups.

- **Control efficiency as a predictor**:  
  - If control efficiency is already high (near cooperative maximum), the marginal effect of adding punishment may be negligible or negative due to added enforcement costs (in line with threshold logic in Prétôt et al., 2024).  
  - If control efficiency is low (heavy free-riding), the potential for punishment to increase efficiency is correspondingly greater (conditional on design and parameter thresholds).

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**  
- `player_count` (Prétôt et al., 2024; Libois, 2022; Gioffré & Tampieri, 2025): Models and reviews discuss group size as a key moderator.
- `num_rounds` (Zhang & Pei, 2022; Gioffré & Tampieri, 2025): Repetition is important for equilibrium enforcement.
- `mpcr` (Prétôt et al., 2024; Libois, 2022; Uchida et al., 2024): Critical for defining the game's cooperation incentives.
- `punishment_cost`, `punishment_tech` (Prétôt et al., 2024; Uchida et al., 2024; Libois, 2022): Central to nearly all formalizations of punishment effectiveness.
- `reward_exists`, `reward_cost`, `reward_tech` (Wu et al., 2022; Hua & Liu, 2024): Directly modeled for reward-punishment tradeoff.

**Indirect/Moderately Informed Dimensions:**  
- `all_or_nothing`, `default_contrib`: Some models discuss the relevance of discrete vs. continuous contributions (`all_or_nothing`, Yan et al., 2023), or implication of contribution framing, but this is generally indirect.
- `chat`, `show_other_summaries`, `show_n_rounds`, `show_punishment_id`: Discussed as auxiliary moderators (Lazarus, 2023; Van Lange & Rand, 2022), but effects typically described in behavioral rather than payoff outcomes.

**Contextually Discussed or Missing:**  
- `default_contrib`, `show_punishment_id`: Often mentioned in settings discussing peer vs. centralized punishment or signaling but lack direct modeling or outcome data.
- Several dimensions (e.g., `show_n_rounds`, `show_other_summaries`) are included in the game descriptions but not directly tied to efficiency outcomes in most theory models.

# 7) Important Limitations

- **Empirical Scarcity:** There is a lack of direct experimental findings on efficiency outcomes for punishment-enabled vs. control PGGs within this paper set; most evidence is theoretical or simulation-based.
- **Overweighting of Theory:** The main guidance comes from theoretical models which assume rationality, perfect information, or infinite populations; these conditions may not hold in real lab or field PGGs.
- **Behavioral vs. Payoff Outcomes:** Most studies report on behavioral change (e.g., cooperation rate), making it necessary to infer, but not directly observe, changes in efficiency. This introduces uncertainty.
- **Specificity to Peer Punishment:** The strongest evidence for efficiency gains generally applies to institutional or collective punishment, not to classic peer punishment as typically implemented in lab experiments.
- **Parameter Interactions and Thresholds:** Many findings emphasize threshold effects and context dependence—efficiency gains from punishment are not guaranteed and depend on precise parameter calibrations (punishment cost, magnitude, group size).
- **Ambiguity and Disagreement:** Some models and reviews argue that punishment often fails or backfires in practice (especially peer punishment), while others model high efficiency under idealized design—this disagreement limits strong prediction outside well-specified parameter ranges.
- **Design Dimension Coverage:** While the core dimensions (group size, repetition, incentives, punishment design) are frequently addressed, others are mentioned only in passing or not at all, reducing guidance for games with more complex information or communication features.
- **Limited reward-punishment interaction modeling:** Although several reviews note the importance of combined reward and punishment, only a few models systematically explore their joint effect on efficiency.

---

**Summary:**  
The literature base is strong for theoretical mechanisms and qualitative expectations concerning punishment's effect on efficiency in PGG-like environments. Direct, quantitative, empirical evidence is sparse and often focused on adjacent designs or models. The best-supported predictions are that enabling institutional (not peer) punishment under the right cost-effectiveness regime increases efficiency, especially where baseline efficiency is low. For peer punishment in small, repeated games, the literature is divided—sometimes showing efficiency gains, but often emphasizing cost, retaliation, and second-order free-riding that erode those gains. Predictive models should accordingly make use of control efficiency, core incentive parameters, and punishment characteristics, but remain cautious about predictions in settings where evidence is indirect or ambiguous, or where key dimensions are not modeled directly.
