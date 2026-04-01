# 1) Evidence Base

The paper set comprises a large, diverse mix of empirical (including multiple lab experiments) and theoretical (game-theoretic and simulation) research spanning public goods games (PGGs), close variants (e.g., collective-risk games, resource games), related social dilemmas, and adjacent domains (trust games, PDs, repeated partnerships, resource-sharing, etc.). A substantial core of the literature directly studies PGGs with punishment and reports efficiency or closely related payoff outcomes. Many others deal with cooperation or punishment but focus on behavioral outcomes (contribution rates, cooperation frequency, strategy prevalence) rather than payoff-based efficiency.

A strong subset includes repeated/structured lab experiments and detailed theoretical/simulation models that specify or manipulate key game design dimensions (group size, rounds, MPCR, punishment cost/impact, information visibility, etc.), directly informing how punishment affects efficiency. There are also numerous mechanism and boundary-condition studies examining moderators like anti-social punishment, reward, communication/chat, resource dynamics, corruption/bribery, and social/institutional context.

Adjacent and weakly-related papers provide contextual or mechanistic insight (e.g., partner choice, reputation, network adaptation), or study adjacent games and behavioral effects, but do not report efficiency or payoff outcomes under punishment. Overall, the coverage for “classic” repeated PGGs with and without peer punishment is dense and detailed; coverage for efficiency in adjacent and weakly-related cases is much sparser.

---

# 2) Task Relevance

**pgg_or_variant:**
- **exact** relevance: The majority of key theoretical and empirical studies (especially those by Szolnoki, Perc, Chen, Wang, etc.) focus directly on classic or spatial PGGs, including both institutional and peer punishment. Some core empirical lab studies test repeated linear or threshold PGGs (Bahbouhi et al., 2024; Jiang et al., 2023).
- **close** relevance: A set of papers study collective-risk games, repeated trust games, resource games, repeated team production, or complex network settings, which maintain most structural features of PGGs and are used as analogs for prediction.
- **adjacent/weak** relevance: Some literature studies PDs, donor-recipient games, or indirect reciprocity, providing only mechanistic insight or baseline expectations.

**punishment_or_sanctions:**
- **exact**: Many studies directly compare punishment-enabled and punishment-disabled games, with manipulation/parameterization of punishment cost, effectiveness, technology (peer, institutional, exclusion, antisocial), and presence/absence of reward (e.g., Bahbouhi et al., 2024; Szolnoki & Perc, 2013; Perc et al., 2017).
- **close**: Some works focus on exclusion mechanisms, policing/corruption, or punishment as one of several intervention arms (reward, exclusion, partner choice), sometimes in non-PGG games (e.g., Jia & Wang, 2024; Liu & Chen, 2020). 
- **adjacent/weak**: Some focus on ostracism, reputation, or partner leaving (not costly punishment per se), or study punishment's behavioral effects but without efficiency outcomes.

**efficiency_or_related_payoff_outcome:**
- **exact**: A distinct core of papers report group efficiency or average group payoff as a fraction of full cooperation, or explicitly track group-level surplus, welfare, or coins generated (e.g., Bahbouhi et al., 2024; Perc et al., 2017; Wang et al., 2011; Murase & Baek, 2021).
- **close**: Some report average group payoff, group achievement rates (threshold PGGs), or total contributions—proxies for efficiency—although not always normalized to the cooperative optimum.
- **adjacent/weak**: Many track only cooperation/contribution rates, punishment frequencies, or prevalence of strategy types; for these, positive changes are often associated with, but not guaranteed to produce, higher efficiency.

In summary, the literature offers strong direct evidence for exact PGGs with punishment and efficiency outcomes; broader context for related games and mechanisms.

---

# 3) Outcomes Measured In The Literature

- **Payoff-related (Efficiency/Group Payoff):**
  - Many exact PGG and close-variant studies report group efficiency as the ratio of actual group payoff to the maximal cooperative payoff (e.g., Bahbouhi et al., 2024).
  - Others measure average group payoff, system efficiency, total surplus, or “net profit,” sometimes tracked dynamically or at equilibrium/stationary state.
  - Some resource-based games focus on “resource sustainability,” “group achievement rate” (collective targets met), or “fully cooperative” equilibrium as proxies for efficiency.
  - A subset of studies (mostly empirical) report coin generation, total earnings, or observed group profit as laboratory outcomes.

- **Non-payoff Behavioral Outcomes:**
  - The most common secondary outcomes are: mean contribution or cooperation rate, prevalence/fraction of cooperators/defectors, frequency or cost of punishment, and norm compliance.
  - Other behavioral outcomes include: punishment and reward assignment rates, pro-social and anti-social punishment, frequency and type of norm enforcement, reputation, and strategy adoption dynamics.
  - Many studies with strong behavioral focus do not report any efficiency or group payoff data.

- **Distinction Explicit in Studies:**
  - Multiple studies explicitly note that cooperation/contribution rates are not in themselves measures of efficiency, particularly when punishment is costly or anti-social punishment is present (Perc et al., 2017; Szolnoki & Perc, 2017).

---

# 4) Main Findings Relevant To Prediction

## General Pattern:
- **Most studies with exact outcomes find that enabling peer or institutional punishment in PGGs increases efficiency/group payoff relative to control (punishment disabled), provided punishment is not prohibitively costly or inefficiently implemented.** This positive effect on efficiency is more likely when:
  - Punishment cost per fine is low or moderate,
  - Punishment is targeted and not dominated by anti-social motives,
  - The marginal per-capita return (MPCR) is sufficiently high,
  - Groups are small/medium in size,
  - Network/interaction structure supports clustering of cooperators/punishers,
  - Corruption/bribery and revenge cycles are minimal,
  - Mechanisms avoid over-punishment/wasteful conflict.

- **However, several important qualifiers and moderators are consistently identified:**
  - **High punishment costs, poorly tuned parameters, or substantial anti-social punishment can nullify or reverse efficiency gains** (Perc et al., 2017; Goette et al., 2012).
  - **The credibility of punishment matters**—punishment is only efficiency-promoting when it is sufficiently likely and severe (Jiang et al., 2023).
  - In threshold/collective-risk PGGs, punishment greatly increases the probability of group success (meeting the target), especially when punishment risk is high and in smaller groups (Jiang et al., 2023; Vasconcelos et al., 2015).
  - **Empirical lab studies generally find positive, but sometimes modest, efficiency gains from punishment**. Occasionally, punishment costs offset cooperation gains, particularly when anti-social punishment is frequent or institutional context is not supportive (Macleod et al., 2025; Bahbouhi et al., 2024).

## Theoretical Studies (Multiple Sources):
- **Strong, general theoretical support for the proposition that punishment expands the parameter regime in which full cooperation, and thus high efficiency, is stable.** Punishment lowers the critical MPCR needed for stable cooperation (Adami et al., 2016; Dorrough et al., 2017).
- **Resource or ecological context is critical** in resource feedback PGGs: if natural growth is too low or initial abundance is insufficient, even strong punishment fails to prevent resource collapse (Wang et al., 2021; Chen & Szolnoki, 2018).
- **Tax-supported or exclusion-based punishment** often outperforms pure peer punishment in maximizing efficiency and preventing second-order free-riding (Liu & Chen, 2020; Jia & Wang, 2024).
- **Meta-incentives and second-order rewards** may be necessary for long-term efficiency; first-order punishment alone is not always sufficient (Okada et al., 2015).

## Empirical Experimental Findings:
- **Repeated lab PGGs with peer punishment**: Punishment generally increases group efficiency by reducing defections, unless anti-social punishment, miscoordination, or excessive punishment costs erode gains (Bahbouhi et al., 2024; Macleod et al., 2025).
- **Meta-institutional context (norm coordination, formal grievance):** When punishment is framed and coordinated institutionally, efficiency gains are reliable. When "free-form" punishment is allowed, efficiency benefits may be lost due to misapplied or retaliatory punishment (Macleod et al., 2025).

## Effects of Game Design Dimensions:
- **Player Count (Group Size):** Smaller groups are more likely to reach full cooperation and high efficiency with punishment enabled; efficiency gains from punishment decrease as group size increases (Perc et al., 2017; Jiang et al., 2023).
- **Num Rounds:** More repeated interaction facilitates reputational punishment and efficiency gains, especially if future is valued (Evans & Thomas, 2001).
- **Punishment Cost & Effectiveness:** Lower punishment cost per impact increases returns to punishment; if cost is high or impact low, punishment can reduce or fail to improve efficiency.
- **Network Structure:** Local/social structure enables clusters of cooperative punishers and prevents invasion by defectors; well-mixed or scale-free networks may dilute benefits or hinder punishment's effect.
- **Information/Observability:** Less noisy and more informative monitoring improves the efficiency gain from punishment (Abreu et al., 1991; Ohtsuki et al., 2015).
- **Consensus/Decision Rules:** Unanimity or collective punishment requirements can reduce anti-social punishment, improving efficiency (Bahbouhi et al., 2024).
- **Reward Exists:** Reward alone is often less effective than punishment; combined mechanisms may have non-additive effects, sometimes negating each other's benefits if not optimally tuned (Szolnoki & Perc, 2013; Wang et al., 2022).

---

# 5) Prediction Guidance

- **Best-informed prediction is supported in classic PGGs with standard or specified design dimensions:** When predicting treatment (punishment-enabled) efficiency from game design and control efficiency, expect a positive, but not necessarily proportional, increase in efficiency in most settings where punishment is neither extremely costly nor anti-social.
    - The absolute efficiency gain is moderated by control efficiency: Where control efficiency is very low (near full defection), enabled punishment is more likely to produce large relative efficiency gains.
    - For games near the full-cooperation threshold (high control efficiency), punishment may produce only modest additional gains, and at times may even reduce efficiency if punishment costs bite into cooperation gains.
- **In high anti-social punishment, weak institutions, or high-cost regimes:** Efficiency gains from punishment are unlikely, and may become negative.
- **Empirical and simulation results suggest the form:**
    - `treatment_efficiency ≈ control_efficiency + f(game design dims, punishment cost/effectiveness, group size, info structure, baseline cooperation)`, where `f` is typically positive but nonlinear and may be zero or negative if punishment is too costly or misapplied.
- **Design dimensions with greatest predictive weight:** punishment cost/impact, group size, MPCR, reputation/information structure, and presence/absence of collective decision rules are most influential.
- **Contexts where the evidence is weaker or ambiguous:** Highly complex network structures, moderate-to-high anti-social punishment rates, environments with voluntary participation/exit, and scenarios where institutional context is ill-specified.
- **Papers with adjacent-only evidence (e.g., pairwise PDGs, partner choice, reputation-only, reward-only):** These support the general principle that contingent sanctions can increase efficiency if targeted well and not overly costly, but provide little precision for mapping to PGG with peer punishment.

---

# 6) Design Dimensions Highlighted Across Papers

## **Directly Informed Dimensions:**
- **player_count:** Strongly and explicitly modeled; efficiency gains from punishment decrease with rising group size and are most robust in small-to-moderate groups.
- **num_rounds:** More rounds facilitate punishment's efficacy; infinite/repeated models support larger efficiency gains where future punishment is credible.
- **mpcr:** High MPCR favors cooperation and makes punishment more likely to be efficiency-enhancing; punishment often expands the regime of stable cooperation to lower MPCRs.
- **punishment_cost, punishment_tech:** Critical parameters; empirical and theoretical studies explicitly analyze sudden breakdowns in efficiency when punishment is too costly or weak. Variation in punishment effectiveness (peer vs. pool vs. exclusion) is well studied.
- **all_or_nothing:** Design often specified; both binary and continuous contribution games are covered, with some variation in predicted efficiency effects based on contribution granularity.
- **reward_exists:** Directly compared in several studies; reward is often less effective than punishment, but combined effects can be non-additive.
- **show_other_summaries, show_n_rounds, show_punishment_id:** Feedback, information, and monitoring are key moderators. Explicit analysis of imperfect monitoring and information lag in theoretical work (Abreu et al., 1991; Ohtsuki et al., 2015).
- **default_contrib:** Some studies highlight opt-in/opt-out framing/friction, though coverage is not extensive.
- **chat:** A few studies test communication/no-communication; chat can reduce need for punishment, or increase its effectiveness when available.

## **Indirectly or Contextually Informed:**
- **punishment_magnitude (sometimes nested under punishment_tech/cost):** Usually discussed as impact/fine per punished unit.
- **show_other_summaries, show_punishment_id:** Less frequently directly manipulated, but information/feedback mechanisms analyzed.
- **reward_cost, reward_tech:** Some papers on combined reward/punishment or resource allocation, though not all studies model both mechanisms.

## **Effectively Missing/Sparse:**
- **Some design dimensions (such as default_contrib, show_n_rounds, show_punishment_id)** are less systematically reported or manipulated, especially in older and high-level theory papers, and in adjacent studies.
- **Environments with voluntary participation/exit, or more complex multi-level reputation, are less systematically mapped to efficiency effects under punishment.**

---

# 7) Important Limitations

- **Evidence is less decisive in parameter regimes with very high punishment cost, frequent anti-social punishment, or weak institutional support for norm coordination.** In these cases, punishment may have null or negative efficiency effects (e.g., Goette et al., 2012; Perc et al., 2017).
- **Many behavioral studies measure only cooperation/contribution rate, not efficiency:** This can lead to overestimating positive effects of punishment if costly punishment reduces payoff (not captured by behavioral metrics).
- **Sparse empirical data on large, heterogeneous, or dynamic group structures, or on real-world PGG variants with corruption, bribery, voluntary participation, or multidimensional incentives.**
- **Ambiguity in highly complex or mixed settings:** Where multiple incentive mechanisms co-exist (e.g., institutional plus peer punishment, reward plus punishment, or punishment with corruption/bribery/exclusion), the mapping to pure punishment-enabled efficiency is less clear and sometimes parameter-specific.
- **Theory and simulation studies dominate:** Few large-sample or field/lab experiments systematically vary all major design dimensions or report efficiency together with contribution and punishment rates.
- **Some design features missing:** Coverage on chat, default contribution framing, precise information transparency (e.g., show_n_rounds, show_punishment_id) is inconsistent.
- **Adjacent models (PDG, trust games, resource games):** Their outcomes may not generalize to standard PGGs, especially for quantitative efficiency prediction for peer punishment interventions.
- **Effect size quantification is limited:** Most theoretical work provides qualitative (or, in rare cases, functional) predictions, but not empirical effect sizes. Parameter mapping for real-world scenarios may require careful calibration.

---

**In summary:**  
The literature robustly supports the prediction that enabling punishment in standard repeated PGGs increases efficiency relative to control, provided punishment is not too costly nor dominated by anti-social use, and when group size, payoff parameters, and institutional design are favorable. Efficiency gains are strongest when punishment is credible, targeted, and not wasteful, and are moderated by baseline control efficiency and key design dimensions such as group size, punishment cost, monitoring/information, and institutional norm support. The evidence for adjacent environments and in complex, heterogenous, or weakly institutionalized settings is more ambiguous, with both positive and negative efficiency effects observed depending on parameter regimes. Modelers should be cautious extrapolating effects to untested domains and ensure that predictions distinguish between behavioral cooperation rates and true group efficiency.
