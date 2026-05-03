# 1) Evidence Base

The paper set includes 68 studies, primarily laboratory experiments, with a strong empirical focus on public goods games (PGGs) and their close variants. There is a mix of within-PGG empirical findings and related game paradigms (e.g., collective-risk games, CPR games, and some adjacent PD/Dictator game studies), but a sizable fraction of papers remain directly centered on classic linear PGGs. A minority of papers employ field or artefactual field designs, or meta-analytic methods. Most experimental studies systematically manipulate the presence of punishment or sanctioning institutions and report on both behavioral and payoff outcomes, though some concentrate solely on behavioral measures (e.g., contribution rates, punishment frequency) or neural/psychological mechanisms.

Within the set, the most direct and high-quality evidence comes from multi-lab replications and meta-analyses focusing squarely on the efficiency impact of peer punishment in repeated PGGs with canonical parameters. Several studies systematically explore moderators and design variations (network structure, group size, MPCR, punishment cost, decision rules, etc.), while others isolate specific mechanisms (e.g., antisocial punishment, noise in punishment, information feedback, prior conflict). A substantial number of papers—especially those in adjacent or weak categories—focus on punishment behavior, norm enforcement, and social or neural mechanisms without direct efficiency measurement, which limits the breadth of evidence for the downstream efficiency prediction task.

**Summary:** The evidence base is strong and relatively narrow for classic PGGs with varying punishment regimes, but broader and more diverse once adjacent settings and non-payoff-focused outcome studies are considered.

# 2) Task Relevance

### a) PGG or Variant (`pgg_or_variant`)
- **Exact relevance:** A substantial subset of the evidence base reports from canonical linear PGGs or extremely close variants (e.g., repeated games with or without communication, endogenous and exogenous punishment, variable group size/MPCR). For example, Lo Iacono et al. (2023), Bahbouhi et al. (2024), Salahshour et al. (2022), Pi et al. (2022), Peng (2022), Gross et al. (2022), Wang & Huang (2022), Harrell & Wolff (2023), Eichenseer (2023).
- **Close/adjacent relevance:** Many papers study collective-risk, CPR, or threshold PGGs, which are structurally very similar and generally transferable for prediction (Ntuli et al., 2023; Xu et al., 2022; Grimalda et al., 2022; Jiang et al., 2023).
- **Weaker/none:** The rest focus on PD, DG, one-shot games, or field/observational designs and are less relevant for direct parameterized prediction.

### b) Punishment or Sanctions (`punishment_or_sanctions`)
- **Exact relevance:** Most of the key empirical PGG studies directly manipulate or enable peer punishment or sanctioning (Lo Iacono et al., 2023; Bahbouhi et al., 2024; Wang & Huang, 2022, etc.) with clear reporting on its effects.
- **Close/adjacent:** Some studies use sanctioning variants (e.g., team allocators, sanctioning quotas, competition-induced penalties, or indirect punishment via link removal).
- **Weak/none:** Studies without punishment, or in which punishment is discussed as a context or norm but not manipulated.

### c) Efficiency or Related Payoff Outcome (`efficiency_or_related_payoff_outcome`)
- **Exact/close:** Fewer papers report group efficiency (payoff as a ratio of maximum possible) or comparably measured total earnings/welfare. Many empirical PGG papers include these outcomes (Lo Iacono et al., 2023; Bahbouhi et al., 2024; Salahshour et al., 2022).
- **Adjacent/weak:** Numerous studies focus primarily on contribution rates, cooperation, or punishment frequency, with limited or absent efficiency reporting.
- **None:** Mechanism- or psych-based studies often lack any payoff reporting.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:** A strong subset of the literature reports on group efficiency, total group earnings, net profits, or surplus, directly addressing the core prediction target. These studies often compare treatment (punishment enabled) to control (punishment disabled) within the same parameterized games and provide numeric or at least directional results (e.g., Lo Iacono et al., 2023; Bahbouhi et al., 2024; Wang & Huang, 2022).
- **Close correlates:** In some studies, only welfare, probability of collective success, or resource preservation is measured but can be mapped closely to efficiency (Jiang et al., 2023; Ntuli et al., 2023).
- **Non-payoff behavioral outcomes:** A large number of studies measure only contribution/cooperation rates, frequency or targeting of punishment, norm compliance, emotional/psychological outcomes, or reputational responses. These are acknowledged as relevant behaviors and mechanisms but are not direct measures of efficiency (Espín et al., 2022; Noussair et al., 2024; Bogdan et al., 2023).
- **Mechanism and context outcomes:** Several studies measure institutional legitimacy, group composition, or cognitive/neural mechanisms without any group-level payoff information.

**Key distinction:** While contribution rates and punishment behavior provide insight into underlying mechanisms, only studies reporting actual group payoffs or welfare inform the payoff prediction task directly.

# 4) Main Findings Relevant To Prediction

Synthesizing across the literature, with a focus on exact and close-relevance studies and explicit efficiency outcomes:

- **Peer punishment typically increases efficiency in canonical repeated PGGs,** especially when the control (no-punishment) efficiency is low or medium and the punishment regime is well-calibrated (Lo Iacono et al., 2023; Bahbouhi et al., 2024; Wang & Huang, 2022; Harrell & Wolff, 2023). The efficiency gain arises from both increased contributions and the deterrence/reduction of free-riding.
    - The magnitude of the efficiency boost can depend strongly on group decision mechanisms (e.g., team unanimity vs. individuals, Bahbouhi et al., 2024) and declines over time if punishment is antisocial or mis-targeted.

- **Punishment effectiveness is highly sensitized to design dimensions:**
    - **Punishment structure/technology:** Noise in punishment (stochastic punishment impact) sharply _reduces_ efficiency, potentially below the control (Salahshour et al., 2022).
    - **Punishment network design:** Allowing all to punish ("complete network") may reduce efficiency compared to restricted, incomplete, or pairwise punishment (Pi et al., 2022).
    - **Punishment cost and severity:** When punishment is expensive or the marginal impact is low, efficiency gains may be neutralized or reversed (Peng, 2022; Grimalda et al., 2022). Costlier or poorly targeted punishment can eat up the surplus from elevated cooperation.
    - **Group size and structure:** Larger groups and denser communication networks amplify the positive effect of punishment (Harrell & Wolff, 2023).
    - **Social context:** Prior conflict or salient social divisions can blunt or reverse the efficiency impact of punishment through mis-targeted or less effective punishment (Gross et al., 2022; Romano et al., 2024).

- **Punishment sometimes improves cooperation but not efficiency:** When punishment is used disproportionately (especially antisocially), its cost can outweigh benefits from higher contributions (Peng, 2022; Grimalda et al., 2022).

- **Variants and close games:**
    - In threshold/collective-risk/CPR settings, credible, well-calibrated punishment (especially if probabilistic risk is high) increases efficiency, especially when the baseline is low (Ntuli et al., 2023; Jiang et al., 2023; Xu et al., 2022). If punishment is too weak or expensive, gains can evaporate.
    - All-can-win competitive sanctions (Riehm et al., 2022) can boost efficiency for most, but sharp penalty structures create risk of severe group losses, offsetting average gains.

- **Meta-analytic evidence:** Peer punishment is consistently more effective than centralized or leader-only punishment, and the presence of both increases over baseline efficiency; reward also helps but less so (Eichenseer, 2023).

- **Signal from behavioral-outcome-only studies:** Numerous studies confirm that high-quality punishment (well-targeted, perceived as legitimate, not antisocial) correlates with higher cooperation and thus efficiency gains when mapped to settings with payoff data (supporting the expectation that design details matter).

# 5) Prediction Guidance

**Direct guidance:**
- The most robust expectation, for _canonical repeated linear PGGs with standard group sizes, moderate MPCR, and deterministic, low-to-moderate-cost punishment_, is:
    - _Enabling peer punishment increases average efficiency (group payoff) compared to the control (no punishment), typically moving efficiency significantly closer to full-cooperation levels._ This is conditional on the control efficiency not already being close to maximum.
    - _Use caution in settings with:_
        - Very costly or weak punishment (expect negligible or negative efficiency effect).
        - Noisy punishment or mis-targeting (possible efficiency drop or even negative effect).
        - Large groups or complex networks: the positive effect is larger if the network allows for sanction diffusion, smaller/lost if monitoring or sanctioning is unreliable.

**Adjustment by dimension:**
- **Group structure/design:** Adjust expected efficiency change based on group size, network density, punishment technology (completeness, pairwise, majority-voting), and decision process (teams with unanimity > individuals).
- **Contextual variables:** Social context, prior conflict, and role-identifiability can limit punishment's effectiveness.
- **MPCR and baseline efficiency:** The efficiency lift from punishment is generally larger when baseline (no punishment) efficiency is low.

**Insufficient evidence for certain contexts:**
- Where outcome measures are limited to non-payoff or mechanism/behavioral measures, do not directly adjust predicted efficiency, but use the findings to inform which moderators have strong conditional effects (e.g., anti-social punishment, legitimacy of enforcement, group equity, network uncertainty, instruction clarity).

**Meta-analytic estimate:** For classic linear PGGs (6-12 players, 10-30 rounds, standard MPCR), enabling peer punishment increases efficiency (relative to no-punishment control) by 0.26–0.47 (proportional scale), depending on whether punishment is centralized or peer-enabled (Eichenseer, 2023).

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions:**
- **player_count, num_rounds:** Regularly varied or well-specified; effects on efficiency are empirically estimated (Lo Iacono et al., 2023; Harrell & Wolff, 2023).
- **chat:** Explicitly included in some experiments, shown to moderate cooperation but not always interacting strongly with punishment (Bahbouhi et al., 2024; Ntuli et al., 2023).
- **all_or_nothing, mpcr:** Routinely manipulated; MPCR shown to strongly moderate the potential for punishment to increase efficiency.
- **punishment_cost, punishment_tech:** Frequently manipulated; effects on efficiency are central (Peng, 2022; Salahshour et al., 2022; Pi et al., 2022).
- **reward_exists:** Informative where studied; peer reward increases efficiency, but less than punishment, and both combined show additive effects (Eichenseer, 2023).

**Indirectly informed/contextually discussed:**
- **default_contrib, show_n_rounds, show_other_summaries, show_punishment_id:** Occasionally discussed or controlled, but impact on punishment’s efficiency effect is subtler; included as control variables or background.
- **punishment_magnitude, reward_cost, reward_tech, reward_magnitude:** When manipulated, show significant effects but are less commonly the focus.

**Effectively missing:**
- Several less canonical settings (e.g., explicit manipulation of default contribution, identity visibility in punishment, explicit impact of round display) are less frequently or systematically explored in the included papers, with quantitative efficiency results.

# 7) Important Limitations

- **Measurement limitations:** Many studies reporting on punishment and cooperation do not report efficiency or payout-based outcomes, limiting their direct predictive value.
- **Generalizability:** Strongest results are for repeated, linear PGGs with adult student participants; transfer to threshold, CPR, one-shot, or field contexts requires caution.
- **Moderator gaps:** Manipulations of certain prediction dimensions (e.g., reward technology, punishment visibility, default frames) are under-represented; thus, their moderating effects on efficiency are less certain.
- **Ambiguity in punishment magnitude/cost tradeoffs:** Papers disagree (or find non-monotonicity) on whether increasing punishment power always increases efficiency; excessive or antisocial punishment can negate or reverse efficiency gains.
- **Cultural/contextual factors:** Effects can vary by culture, explicitness of instructions, and prior social history (e.g., previous conflict, social identity), creating contextual moderation not easily captured by core design variables alone.
- **Reporting bias:** Efficiency gains are more likely to be published where positive (publication bias), while null or negative effects (e.g., from costly or mis-targeted punishment) may be under-represented.
- **Mapping from behavior to efficiency:** In some 'close' or 'adjacent' papers, only surrogates for efficiency (e.g., cooperation rate, resource preservation) are measured, and mapping to the efficiency ratio may rely on inferences not directly warranted by the data.

---

**In sum:**  
The strongest, most actionable empirical generalization is that enabling peer punishment increases efficiency in standard repeated PGGs, but that _the sign and size of the effect depend heavily on punishment cost, technical features, targeting, group structure, noise, and context_. For accurate prediction, align closely to canonical game structures and control for cost and punishment technology dimensions, treating results from behavioral-only or adjacent studies as secondary, indirect evidence.
