# 1) Evidence Base

The literature set comprises 18 papers with a blend of empirical (lab and field experiments), theoretical, and conceptual contributions. Among empirical studies, only a few (notably Eisenberg & Engel, 2014) directly report group payoff or efficiency outcomes in public goods game (PGG) environments with and without punishment. Several theoretical papers analyze efficiency or payoff in adjacent games or with related mechanisms (e.g., reputation, evolutionary models). Many others provide mechanism arguments, evolutionary context, or discuss norm enforcement and cooperation, but do not empirically measure efficiency or manipulate all design dimensions. Thus, the evidence base is broad conceptually but relatively narrow in terms of direct, quantitative empirical studies that target PGG efficiency as influenced by punishment and game design. Most direct, predictive evidence comes from a small subset of well-designed PGG experiments and formal theoretical models closely tied to efficiency outcomes.

# 2) Task Relevance

### pgg_or_variant
- **exact**: ~2-3 papers, including lab experiments and certain theory models, directly implement PGGs or structurally indistinguishable variants (Eisenberg & Engel, 2014; Bell et al., 2016).
- **close**: Several theory and empirical papers cover threshold public goods, random matching, or networked cooperation closely resembling PGGs (Vasconcelos et al., 2013; Zhang & van der Schaar, 2013; Xu et al., 2014; O'Connor, 2016).
- **adjacent/weak**: Many studies focus on evolutionary/observational analogues, one-shot dyadic games, or non-economic institutional settings (Ultimatum games, markets, policy case studies).

### punishment_or_sanctions
- **exact/close**: Most papers directly analyze punishment or equivalent sanctioning mechanisms (e.g., damages, reputation-based protocols, third-party punishment).
- **adjacent/weak**: Some approach punishment as a broader mechanism for norm enforcement, group selection, or discuss the conceptual/evolutionary plausibility without direct intervention in a game (Sterelny, 2016; Mameli, 2013).

### efficiency_or_related_payoff_outcome
- **exact**: Few directly target group efficiency, group payoff, or surplus as measured in PGGs (Eisenberg & Engel, 2014; Vanderschraaf, 2016; Zhang & van der Schaar, 2013; Xu et al., 2014; O'Connor, 2016).
- **close/adjacent**: Several use behavioral proxies (e.g., group achievement, rate of cooperation, avoidance of catastrophe), which are relevant but not direct measures of efficiency (Vasconcelos et al., 2013; Bell et al., 2016).
- **weak/none**: Many papers focus on norm compliance, punishment frequency, or emotional responses (Clavien & Chapuisat, 2013; Brevers et al., 2013), which are not direct payoff outcomes.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes**: Group efficiency, total group payoff, welfare/surplus, or average total earnings are the main measures directly relevant to prediction (Eisenberg & Engel, 2014; Vanderschraaf, 2016; Zhang & van der Schaar, 2013; Xu et al., 2014; O'Connor, 2016).
- **Non-payoff behavioral outcomes**: Contribution rates, cooperation rates, norm compliance, punishment assigned or frequency, rate of group success (threshold achieved), and willingness to punish or reward are much more common as primary outcomes.
- **Other outcomes**: Evolutionary stability, emotional responses, behavioral adaptation, and norm diffusion appear in theoretical and observational work but do not report payoff/efficiency directly.

# 4) Main Findings Relevant To Prediction

- **Punishment Increases Efficiency — When Appropriately Designed and Enforced**: The strongest empirical evidence (Eisenberg & Engel, 2014) shows that enabling sufficiently severe and/or likely punishment in repeated PGGs raises group efficiency (payoff) by discouraging free-riding and stabilizing cooperation, compared to no-punishment control. Both theoretical and simulation studies in adjacent games (Stag Hunt, asymmetric gift-giving) reinforce this (Vanderschraaf, 2016; Zhang & van der Schaar, 2013; Xu et al., 2014).
- **Quality, Design, and Actual Experience of Punishment Matter**: Not all punishment regimens yield equal gains. Severity, probability, and scope (e.g., punishment based on group rather than individual harm) are key moderators. The realized, experienced threat—rather than just the formal possibility—drives behavioral and efficiency changes (Eisenberg & Engel, 2014).
- **Indirect Evidence: Cooperation and Group Achievement**: Several papers show that punishment increases cooperation or rate of group success (Vasconcelos et al., 2013; Bell et al., 2016), but warn that increased free-riding or misuse of punishment can offset efficiency gains.
- **Adjacent Mechanisms: Reputation and Meta-punishment**: Indirect or reputational punishment protocols often achieve even higher efficiency and stability in repeated or networked contexts (Zhang & van der Schaar, 2013; Xu et al., 2014).
- **Theoretical Mechanisms Support Robust Punishment Effects**: Evolutionary game theory and mechanism arguments support the intuition that punishment (even if costly and sometimes weakly dominated) generally enlarges the basin of attraction for cooperative, high-efficiency outcomes (Vanderschraaf, 2016; O'Connor, 2016), though parameter and context sensitivity is acknowledged.

# 5) Prediction Guidance

- **Empirical weight should be placed on repeated PGG studies with explicit payoff measurement.** Given a no-punishment control efficiency, enabling peer punishment is predicted to increase average efficiency, especially as punishment severity, likelihood, and targeting precision increase (Eisenberg & Engel, 2014).
- **Magnitude of effect is not uniform:** Gains depend on punishment regimen (e.g., treble vs. compensatory, group vs. individual harm), group size, and actual use of punishment. Severe and/or likely sanctions lead to stabilization or increase of group efficiency; weak or rarely applied punishment only slows decay (Eisenberg & Engel, 2014).
- **Control efficiency informs treatment efficiency:** In PGGs with rapid decay of cooperation in control, adding punishment is likely to show a larger relative treatment-control efficiency gap.
- **Design interplay is crucial:** The effect of punishment is moderated by player count, rounds, MPCR, and communication—smaller groups and repeated interactions often see larger positive effects of punishment (Vasconcelos et al., 2013; Sterelny, 2016).
- **Contextual and mechanism-focused papers suggest, but do not quantify, that punishment works best where cooperation is already plausible and monitoring/punisher identity is salient.** Absence of such features may limit or reverse gains.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- `player_count` (multiple papers, both empirical and theory: small groups often benefit more)
- `num_rounds` (varied or repeated games see stronger punishment effects)
- `all_or_nothing` (present in both standard and threshold PGGs, with differences noted)
- `mpcr` (manipulated in several models and experiments)
- `punishment_cost` (varied; severity and costliness play a central role)
- `punishment_tech` (how punishment is implemented: peer, group, central; direct vs. indirect/reputation)
- `chat` (shown as a moderator in at least two papers, especially for cooperation mechanisms)

**Indirectly or Contextually Informed:**
- `show_other_summaries`, `show_n_rounds` (occasionally discussed as transparency and information feedback).
- `show_punishment_id` (some discussion in conceptual papers regarding norm and reputational effects).
- `reward_exists` and related dimensions are discussed only peripherally.

**Effectively Missing:**
- `default_contrib` (framing and default not systematically manipulated or discussed in this set)
- `reward_cost`, `reward_tech` (essentially missing, except for brief observational/contextual mention)

# 7) Important Limitations

- **Limited number of empirical studies reporting direct efficiency outcomes in precisely the target environment.** Most direct evidence comes from a very small set of PGG lab experiments.
- **Many papers focus on non-payoff behavioral outcomes** (cooperation rate, norm compliance), which cannot be equated with efficiency for prediction (see Clavien & Chapuisat, 2013).
- **Design dimensions are sparsely and unevenly covered:** Not all 14 prediction-relevant dimensions are empirically or theoretically addressed.
- **Transferability of adjacent models/theory is imperfect:** While coordination games, reputation environments, and networked sharing provide insight, quantitative generalization to standard PGGs is uncertain.
- **Magnitude and moderators of punishment effects are context-sensitive:** Severity, likelihood, enforcement mechanism, and group structure can reverse or undermine positive impacts.
- **Ambiguity and lack of effect size estimates:** Where behavioral improvements are observed, the actual impact on group efficiency varies and is not always quantified.
- **Missing evidence for some environments:** Large groups, one-shot games, or settings with reward/punishment symmetry are underrepresented.

---

**In summary:**  
The literature base provides strong qualitative support—anchored by a handful of PGG experiments and robust theory—that adding peer punishment typically increases efficiency above the no-punishment baseline, especially with well-designed and experienced punishment mechanisms. However, quantitative prediction across the full spectrum of game design dimensions is impeded by evidence gaps, outcome measurement heterogeneity, and limited direct mapping from adjacent models. Forecasters should weight design features like group size, rounds, MPCR, and punishment parameters, use control efficiency as a base, and expect positive but variable treatment efficiency shifts—all with cautious attention to limits of external validity.
