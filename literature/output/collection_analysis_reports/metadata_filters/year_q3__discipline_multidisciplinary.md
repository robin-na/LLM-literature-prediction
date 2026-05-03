# 1) Evidence Base

This paper set is extensive, with a strong balance of empirical (lab/field experiments) and theoretical papers. It includes many direct empirical studies of public goods games (PGGs) and their variants, as well as numerous formal models of cooperation, sanctioning, and efficiency. The coverage is broad not only in terms of treatment types (peer punishment, institutional punishment, reward, exclusion, combinations) but also with respect to game parameterization (group size, rounds, MPCR, punishment cost, etc.). There is a robust core of highly target-relevant studies (i.e., standard linear PGGs with and without punishment, reporting payoff-based efficiency outcomes), but also a substantial tail of studies that focus on adjacent games (PD, SD), reward-only interventions, exclusion/joining mechanisms, or purely behavioral outcomes (contribution rates, norm compliance) rather than efficiencies.

For the downstream prediction task—predicting treatment efficiency in a PGG when peer punishment is enabled from control efficiency and game design dimensions—the empirical base is strong, but with limitations. Many studies report only behavioral outcomes, and among those reporting on efficiency (total/group payoff, surplus), few systematically map effects across the full range of relevant game design dimensions or provide results as a function of baseline (control) efficiency.

# 2) Task Relevance

### `pgg_or_variant`
- **exact**: Large subset of papers study the canonical linear PGG (with or without punishment), or very close variants (e.g., threshold PGG, contest PGG, ROSCA).
- **close/adjacent**: Several papers study adjacent environments (multigenerational PGG, team contest, networked PDG/PGG, dynamic/exclusion-based coordination or common-pool-resource games).
- **weak/none**: Some studies are only tangentially related (e.g., sender-receiver, dictator games, animal or dyadic social dilemma paradigms).

### `punishment_or_sanctions`
- **exact**: Many studies directly manipulate peer punishment institutions, cost/impact ratios, leader vs. peer punishment, or institutional punishment.
- **close/adjacent**: Some focus on reward, exclusion, or combined institutions; or study indirect sanctions/reputation-based enforcement rather than explicit punishment.
- **weak/none**: A subset do not include a punishment condition at all, or focus on correlates of punishment/compensation behavior rather than its presence or effectiveness.

### `efficiency_or_related_payoff_outcome`
- **exact**: The core set of studies reports on efficiency, group payoff, welfare, or total earnings as primary or secondary outcomes.
- **close/adjacent**: Several report on "group achievement" (e.g., rate of success in threshold PGGs), which can be a meaningful proxy for efficiency.
- **weak/none**: Many report only on behavioral outcomes (contributions, cooperation rates, punishment frequency) or distributional measures (inequality); some focus on psychological mediators, perceptions, or neural activations.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (exact/primary):** Efficiency (defined as total group payoff relative to the full-cooperation optimum), group earnings, welfare, surplus, mean income—reported in many empirical and theoretical PGG studies (e.g., Kamijo et al., 2020; Harrell, 2019; Duong & Han, 2021; Hintze et al., 2020; Heine & Strobel, 2020).
- **Payoff-related outcomes (adjacent):** Mean group achievement (e.g., success rate in threshold games), profit in ROSCAs, system-wide expected profit in procurement games.
- **Non-payoff behavioral outcomes (frequent):** Cooperation/contribution rates, number or frequency of punishments/rewards assigned, norm compliance, strategy frequencies, coordination rates, punishment targeting, fairness perceptions, inequality.
- **Other:** Perceptions and attitudes toward punishment, third-party enforcement, reputation effects, emotional/moral mediators.

Explicit caution is needed: high contributions or cooperation rates do not always translate into higher efficiency, as punishment costs can offset gains or even reduce payoffs (Heine & Strobel, 2020; Fehr & Schurtenberger, 2018).

# 4) Main Findings Relevant To Prediction

**Empirical and theoretical studies converge on several key qualitative findings:**

- **Punishment's effect on efficiency is context-dependent:** In many standard PGGs with sufficient MPCR, enabling costly (and sufficiently effective) peer punishment generally increases efficiency (Harrell, 2019; Hintze et al., 2020; Salahshour, 2021; García & Traulsen, 2019). The result is strongest when punishment is well-calibrated (cost is moderate, impact is high, antisocial punishment is minimized).

- **Punishment costs often limit/offset efficiency gains:** In multiple studies, punishment increases cooperation/contributions but at a cost, such that group efficiency sometimes rises only marginally, or remains unchanged, or can even be reduced compared to no-punishment controls (Heine & Strobel, 2020; Lohse & Waichman, 2020; Gross & De Dreu, 2019; Fehr & Schurtenberger, 2018; Li et al., 2018).

- **When punishment is likely to *decrease* efficiency:**
    - In inefficient PGGs (MPCR < 1), enabling punishment does **not** increase efficiency or group payoffs—sometimes even reduces them due to punishment costs (Kamijo et al., 2020).
    - When peer punishment devolves into antisocial punishment, feuds, or is used against cooperators or for normative disagreements, efficiency can decrease (Fehr & Schurtenberger, 2018; García & Traulsen, 2019; Gross & De Dreu, 2019; Li et al., 2018; Honjo & Kubo, 2020).
    - In "contest" or competitive environments (over-contribution, rent dissipation), punishment can worsen inefficiency (Heine & Strobel, 2020).
    - If alternative individual solutions or exit options are available (self-reliance), enabling punishment may not overcome coordination failures, and can even amplify welfare losses if punishment is misapplied (Gross & De Dreu, 2019).

- **Institution design matters:** Centralized leader punishment, conditional/threshold mechanisms, observability of institutions, and local versus global targeting all moderate the impact of punishment on efficiency (Harrell, 2019; Duong & Han, 2021; García & Traulsen, 2019).

- **Punishment vs. reward:** Institutional or peer reward is often as effective or more robust than punishment in sustaining high efficiency, especially in settings with costly punishment (Kamijo et al., 2020; Ozono et al., 2020; Yang et al., 2018; Góis et al., 2019).

- **Moderators:** Local incentive structure (alignment of individual and group welfare), the presence/absence of antisocial punishment, information structure (reputation, observability), risk and threshold (in collective-risk dilemmas), and social context (norms, corruption, possibility of institutional decay) all crucially shape outcomes (Ozono et al., 2020; Lee et al., 2019; Berger & De Silva, 2021; Fehr & Schurtenberger, 2018).

**Quantitative mapping** across control and treatment conditions is present in only a minority of studies; often, only difference or direction is reported.

# 5) Prediction Guidance

- **General principle:** Punishment tends to increase efficiency *relative to control* when it is *cost-effective* (cost per impact is small), is not heavily antisocial, is well-structured (avoids coordination failures or feuds), and when the PGG is efficient at baseline (MPCR ≥ ~0.5).

- **If control efficiency is low (due to strong free-riding) and punishment is designed well:** Expect moderate-to-large increases in efficiency with peer punishment enabled (Harrell, 2019; Hintze et al., 2020; Salahshour, 2021).

- **If control efficiency is already high:** Marginal efficiency gains from enabling punishment may be small (due to ceiling effects), and punishment costs may partially offset small gains in cooperation.

- **If the PGG is *inefficient* (MPCR < 1):** Punishment will not substantially increase efficiency and may reduce total payoffs (Kamijo et al., 2020; Ozono et al., 2020).

- **Punishment design matters:**
    - *Low cost/high impact* punishment: Stronger positive effect on efficiency (Hintze et al., 2020).
    - *High cost/low impact*: Likely negative or null effect.
    - *Antisocial/uncoordinated punishment, or feuds employed*: Negative or neutral effect on efficiency (Fehr & Schurtenberger, 2018; Li et al., 2018; Gross & De Dreu, 2019).
    - *Centralized punishment (leader/institutional)*: More positive effect than decentralized/peer punishment (Harrell, 2019).

- **Control efficiency as predictor:** A core implication across the literature is that efficiency with punishment enabled will never be lower than control efficiency *minus* aggregate punishment costs (assuming no other shift in game structure), unless additional negative spillovers (such as antisocial punishment or feuding) arise.

- **Interaction with other mechanisms:**
    - Reward and punishment together, or alternative interventions (exclusion, collective choice): May outperform punishment alone for efficiency (Kamijo et al., 2020; Ozono et al., 2020; Góis et al., 2019).
    - Nature of feedback, communication, and observability can amplify or mute punishment's effects (García & Traulsen, 2019; Berger & De Silva, 2021).

- **Design-specific prediction:** For games with standard lab PGG designs (e.g., 3–4 players, 10–20 rounds, linear MPCR 0.3–0.6), introducing peer punishment with a cost:impact ratio of 1:3 or better, no chat, full feedback, and identified sanctioning: expect efficiency to increase versus control by typically 10–25 percentage points, often with diminishing returns at the upper end (Harrell, 2019; Hintze et al., 2020). However, the precise effect will depend on parameterization and pre-existing efficiency.

- **Exceptions/negative cases:** In some institutional or multi-option settings (presence of private solutions, contest environments, high possibility of antisocial punishment), enabling peer punishment can reduce efficiency versus control (Gross & De Dreu, 2019; Heine & Strobel, 2020; Honjo & Kubo, 2020; Tsvetkova et al., 2020).

# 6) Design Dimensions Highlighted Across Papers

**Directly informed:**
- `player_count`, `num_rounds`, `mpcr` (marginal per-capita return): Frequently manipulated and statistically reported.
- `punishment_cost`, `punishment_tech` (fine/cost ratio, central vs. peer): Core focus in both empirical and theoretical studies.
- `reward_exists`, `reward_cost`, `reward_tech`: Reward conditions often included, especially for comparisons.
- `all_or_nothing`, `default_contrib`: Contribution regime and framing, sometimes explicitly discussed.

**Indirectly informed/contextually discussed:**
- `chat` (communication): Sometimes included; effects frequently noted but less systematically explored in efficiency outcomes.
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Feedback and information structure are mentioned as moderators, particularly in theory work on norms and institutional punishment (García & Traulsen, 2019; Berger & De Silva, 2021), but rarely systematically varied in empirical efficiency reporting.
- `punishment_magnitude`, `reward_magnitude`: Often implicit in cost/impact ratios or overall mechanism descriptions but not always separately parameterized.

**Effectively missing:**
- Some studies do not specify or manipulate `default_contrib` (opt-in/opt-out framing), or treat identification/feedback only peripherally. Contextual variables like social norms, institutional trust, and corruption are often treated qualitatively rather than as explicit game dimensions. Studies rarely cross randomize all 14 dimensions exhaustively.

# 7) Important Limitations

- **Confounding between contribution and efficiency effects:** A significant portion of the literature reports only behavioral outcomes (contributions, punishment assigned) without attending to the net efficiency/welfare effect, which can lead to overestimating the benefits of punishment if costs are ignored.

- **Antisocial punishment** is underexplored or not always reported quantitatively, though evidence shows it can seriously undermine efficiency gains, especially where norms or institutional constraints are weak (Fehr & Schurtenberger, 2018; García & Traulsen, 2019).

- **Variability in game parameterization:** Many studies examine only small groups (n = 3–4), 10–20 rounds, and moderate MPCR; results may not generalize to larger groups, more rounds, or extremal MPCR values.

- **Insufficient mapping to full multidimensional design space:** While player count, rounds, MPCR, and punishment cost/impact are well covered in isolation, systematic data across all interacting design variables are rare, limiting fine-grained prediction.

- **Few studies explicitly relate treatment effects to control efficiency:** Predictions often require inferring baseline (control) performance from other sources or from within-study information, but direct mapping of treatment-control efficiency differences as a function of baseline is limited.

- **Neglect of rare population traits and outlier contexts:** Effects of heterogeneous populations (norm disagreement, social value orientation, network structure, cultural setting, etc.) are discussed but rarely tightly linked to efficiency outcomes under punishment.

- **Correlation vs. causation in mechanism studies:** Many theoretical papers model the mechanisms that *could* drive cooperation/efficiency gains, but do not calibrate these models with empirical payoff data, so their quantitative predictive value is limited.

- **Publication and reporting bias:** Studies that find null or negative effects of punishment on efficiency may be underrepresented, and positive effects in behavioral outcomes (contribution) may be over-emphasized compared to payoff-based efficiency.

- **Limited treatment of reward-punishment interaction**: Although reward is often more effective for efficiency, its joint and comparative effects with punishment are not always directly estimated in studies focused on punishment alone.

---

**In summary:** There is strong qualitative and some quantitative support for the prediction that enabling peer punishment in standard, moderately inefficient PGGs will usually improve efficiency over the control, with multiple design-moderated exceptions. The most robust moderators of this effect are MPCR, punishment cost/efficacy, the potential for antisocial punishment, institutional design (central vs. peer, observability, targeting), and the alignment of local and global incentives. The literature directly informs several prediction dimensions but is less systematic in mapping interactions among all relevant design factors or relating efficiency gains to baseline control efficiency. Caution is needed in generalizing to populations or settings not well represented in the laboratory research base.
