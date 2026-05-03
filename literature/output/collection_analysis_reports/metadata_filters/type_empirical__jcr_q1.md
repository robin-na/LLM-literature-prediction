# 1) Evidence Base

The evidence base is **broad, diverse, and data-rich**, comprising a large set of mainly laboratory-based experimental studies (with some field or artefactual field experiments and a few observational studies) directly investigating public-goods games (PGGs) and a wide variety of PGG variants and adjacent social dilemmas. The set includes mainly **empirical, experimental studies**—theory-development papers and simulations are rare in this digest and, where present, are always clearly distinguished from empirical findings.

The core of the evidence base is built from dozens of high-quality lab experiments that enable peer punishment (and sometimes reward/exclusion) in repeated, anonymous, and fixed-group PGGs, with efficiency or total group payoff as the primary outcome. Many studies further manipulate key design dimensions such as punishment cost, punishment effectiveness, information quality, group size, round count, communication, leadership, institution selection, and baseline cooperativeness.

There is a **strong focus on payoff-based (efficiency/welfare) outcomes** in many of the exact match studies. Adjacent and weakly related studies focus more narrowly on behavioral or psychological mechanisms (contributions, norm enforcement, emotion, etc.), which serve as valuable context but are less directly relevant.

The breadth of the evidence also ensures variation in cultural context, subject pool (including non-student and non-Western samples), game framing, and institutional detail, but introduces heterogeneity in findings, especially in more complex, noisy, or real-world-inspired designs (CPR, contests, field settings, etc.). Meta-analyses and replications are present, adding robustness checks.

**Summary:** The base is **empirical-heavy, methodologically diverse, and abundant for standard PGGs with punishment**, but heterogeneity is high across settings and many papers limit their direct focus to behavioral or context-adjacent outcomes.

---

# 2) Task Relevance

**Relevance for Downstream Prediction Task**:

- **pgg_or_variant:**
  - **Exact:** Most central studies use canonical linear PGGs, including variations in group size, round structure, cost/benefit parameters, punishment/reward/exclusion mechanisms, and feedback. Many studies directly manipulate or systematically document all 14 of the core game design and prediction dimensions. Numerous high-powered studies meet the exact match criteria, with lab-implemented PGGs explicitly toggling punishment and measuring efficiency.
  - **Close/Adjacent:** Many studies extend to adjacent CPR games, contests, trust games, or use modified PGGs (e.g., binary, threshold, contest, or weak-link/coordination variants), which are adjacent and need care in transferring findings.
  - **Weak/None:** A large set of studies are behavioral, neuro/psychological, or field-based, adjacent but do not adopt the prediction-relevant measures.

- **punishment_or_sanctions:**
  - **Exact:** A large fraction toggle punishment as an experimental variable and implement it using peer or centralized, costly, observable, or anonymous sanctioning. Studies typically vary punishment cost, impact, institution structure, and sometimes scope (who can punish and when).
  - **Close/Adjacent:** Some studies investigate exclusion, reward, reputation-based sanctions, or "punishment-like" interventions (ostracism, expulsion, etc.).
  - **Weak/None:** Some adjacent studies include only symbolic or hypothetical sanctioning, not payoff-relevant punishment.

- **efficiency_or_related_payoff_outcome:**
  - **Exact:** Most exact match PGG studies report efficiency as group earnings relative to social optimum or as a direct efficiency/welfare measure, and many include the actual vs. maximum payoff in both control and treatment arms.
  - **Close:** Some studies provide group payoffs or welfare-related outcomes (not always normalized as efficiency ratios).
  - **Adjacent/Weak:** Many behavioral studies focus exclusively on contribution rates, cooperation frequency, or punishment use, providing only indirect evidence for efficiency.

**Summary:** The literature is **highly relevant** for downstream prediction of efficiency in PGGs with/without punishment, particularly for standard lab designs. **Task relevance is strongest** when both punishment and efficiency (or close proxies) are measured in PGG/VCM games, and **weakest** when the only outcomes are behavioral, attitudinal, or not payoff-based.

---

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes** (**directly relevant to efficiency prediction**):
  - **Exact:** Group efficiency (payoff as a fraction of the max possible), group earnings, welfare/surplus, total coins/profits, net payoffs (after punishment costs), and surplus above/below baseline.
  - **Close proxies:** Group profits in contest/CPR games, share of endowments kept after resource extraction or contest expenditures, public good provision as mean returns to the group.
  - **Not exact:** Many studies report only the **difference in efficiency between control and punishment conditions**, which is the critical quantity for prediction.
- **Non-payoff behavioral outcomes** (**contextual or mechanistic, not directly efficiency**):
  - Contribution/cooperation rate, antisocial/prosocial punishment frequency, norm compliance, trust/trustworthiness, belief updating, institution choice/voting, emotion/attitudinal responses.

**Key distinction:** Many studies **explicitly separate** (and sometimes contrast) the effect of punishment on cooperation/contribution **versus** its effect on group efficiency/welfare, often finding that costs of punishment erode potential welfare gains. Studies focusing only on contribution rate must be flagged as offering only indirect evidence for efficiency.

---

# 4) Main Findings Relevant To Prediction

**Synthesized Cross-Paper Findings**:

**a. Punishment Effect Often Increases Efficiency, But Not Always**
- The **majority of standard lab PGGs** find that enabling (peer or centralized) punishment increases group efficiency/payoff relative to no-punishment controls, especially when control efficiency is low (due to declining contributions). The typical efficiency gain is 10–40% of the full-cooperation benchmark, but this depends crucially on the cost-effectiveness and targeting of punishment [(Fehr & Gächter, 2000); (Gürerk et al., 2006); (Sutter et al., 2010); (Dickinson et al., 2015); (Gintis et al., 2003)].

**b. Welfare Gain Often Less Than Behavioral Gain**
- **Contribution rates** routinely rise far more (to near full-cooperation) than do average payoffs/efficiency, because costly punishment drains resources. In some designs, net efficiency rises little or not at all, even if contributions increase [(Simpson et al., 2017); (Wu et al., 2016); (Egas & Riedl, 2008)].

**c. Moderators of the Punishment-Efficiency Relationship:**
- **Group composition:** Punishment is more effective at raising efficiency in randomly composed and low baseline-cooperativeness groups than in highly cooperative or homogenous groups [(Barclay, 2004); (Bühren & Dannenberg, 2021)].
- **Institution design:** Leader/centralized punishment, democratic punishment, or targeted regimes (punishment only for low contributors) boost efficiency compared to diffuse, peer punishment [(O'Gorman et al., 2009); (Nockur et al., 2021); (Ambrus & Greiner, 2019); (Krügel & Maaser, 2025)].
- **Information and monitoring:** When information about others' actions is incomplete or noisy, punishment becomes misdirected and can lower efficiency [(Grechenig et al., 2010); (Ambrus & Greiner, 2012); (Salahshour et al., 2022)].
- **Punishment cost/effectiveness ratio:** High cost–low effectiveness ratios (e.g., 1:1) lead to little or negative effect on efficiency. Low cost–high effectiveness ratios (e.g., 1:3+) are required for efficiency gains [(Fehr & Gächter, 2000); (Egas & Riedl, 2008)].
- **Game structure:** In settings with all-or-nothing contributions, pool punishment, intergroup contest, or contest-framed PGGs, punishment can reduce efficiency or lead to wasteful overcontribution [(Dekel et al., 2017); (Heine & Strobel, 2020); (Abbink et al., 2010)].
- **Social/psychological context:** Antisocial punishment or counter-punishment (punishing cooperators or retaliating) is especially common in some cultural settings or when monitoring is noisy, and reduces or erases efficiency gains [(Herrmann et al., 2008); (Gächter & Herrmann, 2011)].

**d. Communication, Reputation, or Reward Can Substitute or Outperform**
- Many studies show that **non-punitive mechanisms** (communication, reputation, endogenous rewards) can yield higher or more sustainable efficiency than punishment [(Rand et al., 2009); (Bochet & Putterman, 2009); (Yang et al., 2018)].
- In settings where both punishment and reward are available, reward is often more efficient due to the lower direct cost [(Sutter et al., 2010); (Rand et al., 2009)].

**e. Endogenous Institutional Choice Further Boosts Efficiency**
- Giving groups the option to vote for/against punishment institutions increases both acceptance and realized efficiency, especially if the institution selected is strong and well-targeted [(Markussen et al., 2016); (Putterman et al., 2011); (Lo Iacono et al., 2023)].

**f. Negative or Null Effects in Challenging Contexts**
- Efficiency is **not reliably increased—and may be reduced—** when:
    - Punishment is mostly antisocial or retaliatory.
    - The control game efficiency is already high.
    - Game structure contains intergroup contests, harm to a minority, absence of communication, or opportunities for strategic exploitation [(Dekel et al., 2017); (Fehr & Rockenbach, 2003); (Gross & De Dreu, 2019); (Goto & Matsui, 2025)].
    - Punishment is implemented with high noise, high monitoring cost, or inability to target free riders [(Grechenig et al., 2010); (Nicklisch et al., 2016)].
    - Institutional context is high-trust and top-down (crowding out) or subject buy-in is low [(Vollan, 2008); (Gatiso et al., 2015)].

---

# 5) Prediction Guidance

**How should this literature inform downstream prediction of efficiency with punishment enabled, given game design and control efficiency?**

- **Baseline:** If the control (no-punishment) efficiency is *low* (declining contributions, typical in standard repeated linear PGGs), the average efficiency with peer punishment enabled **should be predicted to be higher** (typical gain: +10–40%, depending on context and parameterization). **This effect is strongest under:**
    - Deterministic, accurate feedback on contributions
    - Peer punishment with 1:3 or higher cost-impact ratios
    - Small to moderate group size (4–6)
    - Moderate number of rounds (6–30)
    - No chat, anonymity, no reward
    - Continuous contributions

- **Marginal Effect Moderators:**
    - **Information quality:** If information about others' behavior is noisy or costly, efficiency improvements may be negligible or negative.
    - **Punishment tech/cost:** High-cost or low-effectiveness punishment can negate or reverse efficiency gains.
    - **Punishment structure:** Democratic or leader punishment and targeted punishment are more efficiency-enhancing than diffuse, peer-only systems.
    - **Cultural context:** In high-antisocial-punishment or low-trust cultures, or under certain field settings, punishment may not improve efficiency and can reduce it.
    - **Group composition:** If the group is already highly cooperative, or if group heterogeneity leads to feuding or anti-normativity, punishment may not increase efficiency and may even reduce it.
    - **Communication or rewards co-enabled:** If chat or costless rewards are available, the marginal effect of punishment may be reduced or even negative relative to those interventions.

- **Ceiling effects:** If control efficiency is already high (e.g., due to communication, high baseline cooperation, or reward mechanisms), enabling punishment is less likely to yield further efficiency gains and may reduce efficiency due to punishment costs.

- **Narrow vs. broad generalization:** The most reliable quantitative predictions come from close parameter matches (group size, rounds, MPCR, punishment regime/cost, information) to the literature. When design dimensions differ (e.g., all-or-nothing vs. continuous, contest or collective-risk games, institution selection, endowment inequality), uncertainty increases, and adjacent/weak evidence should not be over-interpreted.

---

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions (with rich quantitative evidence):**
  - `player_count`
  - `num_rounds`
  - `mpcr`
  - `punishment_cost`
  - `punishment_tech` (punishment effectiveness/leverage)
  - `all_or_nothing` (binary vs. continuous contribution)
  - `show_n_rounds` (known/unknown horizon)

**Indirectly or contextually informed dimensions (occasionally reported, less often varied):**
  - `chat` (communication enabled/disabled)
  - `show_other_summaries` (feedback/monitoring technology)
  - `show_punishment_id` (anonymity of punishment)
  - `reward_exists`, `reward_cost`, `reward_tech` (when reward/feedback systems are included)

**Rarely discussed, sparse evidence:**
  - `default_contrib` (contribution framing)
  - `punishment_enabled` (as a variable is widely toggled, but the institutional design and method of enabling is less often the focus)
  - `institutional choice` (endogenous selection, voting)

**Missing or under-explored dimensions:**
  - Intergroup competition/contest structure in standard linear PGGs
  - High heterogeneity in returns, endowments, or network structure directly (though a few studies address these)

**Summary:** The literature is best at informing predictions about the effect of enabling peer punishment under known, standard game design specifications. **Critical moderators** with strong literature coverage: group size, rounds, MPCR, punishment cost and effectiveness, information structure; **moderate coverage**: chat, feedback, reward mechanisms; **sparse**: default framing, subtle feedback or institutional features.

---

# 7) Important Limitations

**a. Outcome Interpretation:**
  - Behavioral outcomes (contributions/cooperation) are often more positive than efficiency outcomes, due to the cost of punishment draining resources.

**b. Context Sensitivity:**
  - Negative or null effects in field, contest, all-or-nothing, or complex real-world settings—especially with antisocial punishment, cultural heterogeneity, or low information quality.
  - Success of punishment in raising efficiency is not universal and is strongly context dependent.

**c. Design Generalizability:**
  - The strongest predictive power is for canonical linear, repeated PGGs with punishment stages. In designs with structural deviations (contest, threshold, asymmetry, network/CPR variants, field/real-world contexts), findings transfer only with caution.
  - Some design dimensions relevant to modern or applied settings (institutional evolution, endogenously chosen punishment, hierarchical institutions, multiplex monitoring) are under-explored or absent.

**d. Reporting Biases:**
  - Some papers only report relative efficiency; absolute treatment efficiency, especially as a percent of the social optimum, is not always available.
  - Efficiency is sometimes reported only for final rounds or as pooled averages, masking round-to-round or trend effects.

**e. Missing Cases:**
  - Few studies systematically document the absence or null effect of punishment, or the boundary conditions under which punishment no longer increases efficiency (e.g., rapid decay due to anti-social punishment, breakdown at high group size or high monitoring noise).

**f. Over-emphasis on Laboratory Contexts:**
  - Field and real-world operationalizations are much less common, and where present, treatment effects are often mixed or weaker than in lab settings.

**Summary:** While the literature provides **excellent support for prediction in standard repeated PGGs with punishment**, caution must be exercised when extending to structurally or contextually different environments, when relying on non-payoff outcome data, or when the control game efficiency is already high due to other mechanisms. Ambiguity remains in edge cases, and disagreement exists about the efficiency effect of punishment in complex or noisy institutional settings.
