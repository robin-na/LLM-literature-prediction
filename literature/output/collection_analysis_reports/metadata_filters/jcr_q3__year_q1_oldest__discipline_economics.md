# 1) Evidence Base

The paper set analyzed consists of 40 studies, including both empirical (mostly experimental lab studies) and theoretical works. The empirical studies are heavily weighted toward laboratory public goods games (PGGs), with a focus on how different punishment or sanction mechanisms affect outcomes. The set is moderately broad for the prediction task: while many studies target standard linear PGGs, others cover variants such as common pool resource (CPR) games, partner-switching games, coalition formation, and repeated or networked social dilemmas. Several papers use adjacent social dilemma games (e.g., Prisoner’s Dilemma, trust games) or theoretical models that share key features with PGGs. Both payoff (efficiency, group earnings, welfare) and non-payoff (contribution rate, norm compliance) outcomes are considered, though not all works report treatment efficiency directly. Theoretical papers often provide general mechanism arguments or formal models linking design dimensions to cooperation and efficiency rather than direct empirical estimates.

# 2) Task Relevance

### `pgg_or_variant`
- **exact**: Most studies use standard public goods game structures or voluntary contribution mechanisms, with n=3-6 players, linear returns, and either continuous or all-or-nothing contributions (e.g., Kube & Traxler, 2011; Nikiforakis, 2010; Anderson & Putterman, 2006).
- **close**: Several papers use CPR games, coalition formation, partner switching, repeated trust games, or networked dilemmas, mapping onto social dilemma logic but not exact PGGs (e.g., Akpalu & Martinsson, 2012; Ahn et al., 2008).
- **adjacent/weak**: Some theory/exploratory papers use Prisoner’s Dilemma or trust games, bearing more distant relevance (e.g., Takahashi, 2010; Stahl, 2011; Chassang & Takahashi, 2011).

### `punishment_or_sanctions`
- **exact**: Studies typically manipulate the presence, cost, and structure of peer punishment or institutional sanctions (e.g., Kube & Traxler, 2011; Denant-Boemont et al., 2007). Multiple forms of punishment (peer, legal, ostracism, or switching) are explored.
- **close**: Some works focus on removal/ostracism, coalition entry denial, or implicit sanctions in partner choice scenarios.
- **adjacent/none**: Several papers focus only on communication, reputation, or reward mechanisms, with punishment absent or only discussed for context.

### `efficiency_or_related_payoff_outcome`
- **exact**: Approximately half the empirical studies report direct efficiency or group payoff outcomes as a function of punishment interventions.
- **close**: Several theory papers predict efficiency changes as a function of punishment but lack empirical data.
- **adjacent/weak**: Many studies report only behavioral outcomes (contributions, cooperation) and infer efficiency, or only discuss efficiency conceptually.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (efficiency, welfare, payoff, surplus, total earnings):**
    - Frequently measured in the core empirical studies (e.g., Kube & Traxler, 2011; Nicklisch & Wolff, 2011; Tyran & Feld, 2006; Denant-Boemont et al., 2007).
    - Theoretical models (e.g., Kranz, 2010; Levine & Pesendorfer, 2007) predict efficiency/payoff changes as a function of punishment, compliance share, or identification technology.
- **Non-payoff behavioral outcomes:**
    - Contribution/cooperation rates, norm compliance, punishment frequency, retaliation, ostracism, and trust dominate several studies (e.g., Anderson & Stafford, 2003; Carpenter, 2007; Charness et al., 2011).
    - These outcomes are often strongly (but not perfectly) correlated with payoff measures.

Importantly, only a subset of studies provides direct, quantitative measures of the outcome targeted by the prediction task (efficiency when peer punishment is enabled).

# 4) Main Findings Relevant To Prediction

- **Peer punishment can increase or decrease group efficiency:** 
    - Direct evidence shows peer punishment often increases contributions and, under some designs, efficiency (e.g., Kube & Traxler, 2011; Nicklisch & Wolff, 2011).
    - However, when punishment is very cheap, overused, or enables cycles of counterpunishment, efficiency can be reduced below even the no-punishment baseline due to high enforcement costs (Anderson & Putterman, 2006; Denant-Boemont et al., 2007; Colombier et al., 2011).
- **The effect of punishment depends critically on game design dimensions:**
    - **Punishment cost/tech:** Lower punishment cost leads to more frequent punishment, which can lower efficiency via enforcement costs—even as cooperation rises (Anderson & Putterman, 2006; Kranz, 2010).
    - **Information environment:** The format of feedback (contributions vs. earnings), visibility of others’ actions, and ability to identify punishers all strongly moderate the efficiency effect (Nikiforakis, 2010; Levine & Pesendorfer, 2007).
    - **Possibility of counterpunishment:** Enabling reciprocal or multi-round punishment can sharply decrease efficiency (Denant-Boemont et al., 2007).
    - **Endogeneity of punishment institution:** Voted/self-imposed punishment regimes produce much higher efficiency than externally imposed regimes, even when severity is the same (Tyran & Feld, 2006).
    - **Player count and group formation:** While group size moderates the impact of monitoring/punishment (Carpenter, 2007), in most standard setups (n=3-6) the general effects are robust. In coalition/partner-choice settings, punishment-like exclusion or entry denial can affect efficiency via changes in group size (Ahn et al., 2008).
    - **Other features:** The number of rounds (especially in repeated games), status structure, and communication opportunities also affect the efficiency impact of punishment.
- **Non-payoff outcomes (contribution, norm compliance) often but not always track efficiency:** 
    - Sometimes increased cooperation via punishment is more than offset by costly punishment itself, so efficiency does not rise (Colombier et al., 2011).
- **Contextual limits:** In some environments (CPRs, “all-or-nothing” games, or where masquerading is cheap), punishment may not yield efficiency gains.

# 5) Prediction Guidance

- **Direct prediction of treatment efficiency (with peer punishment enabled) is most reliable when:**
    - The game is a linear PGG with n=3-6, no chat, continuous contributions, and standard feedback, and punishment is peer-to-peer with moderate (not too low) cost (Kube & Traxler, 2011; Nicklisch & Wolff, 2011; Kranz, 2010).
    - Information about others’ actions is clear, and punishment is anonymous, one-shot, or single-stage.
    - Control efficiency is known: the incremental effect of punishment should be modeled as depending jointly on control efficiency and key design moderators (punishment cost, MPCR, feedback, group voting, etc.).
- **Expect sharply reduced (or even negative) efficiency gains from punishment if:**
    - Punishment cost is very low and/or its use is unconstrained.
    - Multi-stage or counter-punishment is possible, or information about punishers is provided in a way that facilitates retaliation.
    - The feedback environment shows both contributions and earnings, increasing noise and norm conflict (Nikiforakis, 2010).
    - The sanction institution is exogenous, weak, or imposed over group objections (Tyran & Feld, 2006).
- **Empirical adjustment for reward mechanisms:** If both punishment and reward are enabled, welfare effects may be more positive under reward than punishment (Colombier et al., 2011), and the cost-effectiveness of each should be considered.
- **Generalization to adjacent cases (network/partner selection, CPRs, repeated PDs):** The direction of punishment’s effect on efficiency is preserved only if (1) punishment is credible and targeted, (2) the ability to identify defectors is high, and (3) group structure enables monitoring. Otherwise, efficiency gains may not occur.

# 6) Design Dimensions Highlighted Across Papers

The literature provides **direct or strong indirect evidence** for the following prediction dimensions:

- **player_count:** Directly manipulated and reported in nearly all empirical studies.
- **num_rounds:** Reported with attention to its moderating role (short vs. long, finite vs. indefinite).
- **mpcr:** A key analytic focus in both theory and empirics.
- **punishment_cost / punishment_tech:** Explicitly manipulated and analyzed for efficiency effects.
- **show_other_summaries:** Feedback form (conclusions about contributions/earnings/identities) is a major moderator, well covered (Nikiforakis, 2010; Levine & Pesendorfer, 2007).
- **all_or_nothing / default_contrib:** Sometimes discussed, but not always as primary analytic features.
- **chat:** Occasionally used as a manipulation or controlled for, but less central.
- **reward_exists / reward_cost / reward_tech:** Coverage is sparser; when discussed, direct efficiency comparisons with punishment are made (Colombier et al., 2011).
- **show_n_rounds / show_punishment_id:** Discussed selectively, but highlighted as important for endogenous punishment credibility, retaliation, etc.
- **punishment_magnitude:** Sometimes specified (Nicklisch & Wolff, 2011); in other cases, assumed or inferred.
- **Other contextual moderators:** Status, voluntary participation, group formation rules, identification technology—these are highlighted as critical elsewhere but are not always formal prediction dimensions.

Some dimensions (especially reward/communication details, identification mechanisms, specifics of feedback content) are only contextually or sporadically covered.

# 7) Important Limitations

- **Direct measurement of efficiency is limited to a subset** of empirical studies. Many studies require inference from contribution rates, which may overstate or understate net efficiency effects when punishment is costly.
- **Coverage of certain design dimensions is uneven:** Critical moderators such as the clarity of identification (show_punishment_id), feedback format, or group voting are only studied intensively in a minority of works.
- **Reward mechanisms and communication (chat)** are less frequently analyzed in tandem with punishment, reducing certainty in predictions about their combined effects.
- **Generality beyond linear PGGs is limited:** While adjacent games support broader mechanism arguments, direct evidence for non-PGG environments or with more complex institutions (CPR, networks) is sparse.
- **Parameter non-monotonicity:** The effect of punishment is not always monotonic in cost or magnitude; sometimes, “more punishment” or “cheaper punishment” reduces efficiency due to overuse or retaliation.
- **Ambiguity in ambiguous and conflicting settings:** Some findings (e.g., multi-stage/counterpunishment) conflict with standard theory and with each other, and context (e.g., information structure, population heterogeneity) can reverse average effects.
- **Absence of field data and real-world heterogeneity:** Nearly all evidence comes from lab settings with small, homogeneous, often student populations.

---

**Summary:**  
The literature base provides strong, direct empirical and theoretical support for the prediction of treatment efficiency in standard lab PGGs with peer punishment, with clear evidence on the importance of several design dimensions (player count, rounds, punishment parameters, feedback). However, coverage of more complex or varied institutional details, external reward, communication or identity mechanisms, and indirect, ambiguous, or non-standard settings is weaker, and efficiency is not always directly measured. Prediction accuracy will be highest when applied to environments closely matching the standard experimental paradigms and where key design moderators align with those most studied in the literature.
