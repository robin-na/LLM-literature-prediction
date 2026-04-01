# 1) Evidence Base

This paper set is large (103 papers) and features a strong empirical core. There is a rich set of well-powered laboratory experiments and some field experiments that directly address repeated linear public goods games (PGGs) with and without peer punishment, often reporting efficiency or related payoff-based outcomes. Alongside, there is a substantial body of theory and simulation papers, which frequently focus on cooperation rates or mechanisms, rather than on efficiency in the strict sense. The evidence is broad in terms of paradigm variants (classic PGGs, CPRs, spatial and networked games, exclusion/ostracism, and institutions with varying punishment/reward rules). The literature robustly covers the PGG domain and the effects of peer (and institutional) punishment, especially in canonical lab implementations. Much of the evidence is exactly or closely relevant to the downstream prediction task, particularly for standard PGG/paradigm variants; adjacent paradigms and mechanism analyses expand, but do not dominate, the evidence base.

# 2) Task Relevance

- **pgg_or_variant**: 
  - *Exact relevance*: Many core empirical and theoretical studies use standard or minimally-modified PGGs or voluntary contribution mechanisms, often with repeated rounds, fixed or random groups, and no extraneous framing. Most direct evidence comes from these canonical designs (e.g., Sefton et al., 2007; Fehr et al., 2002; Arechar et al., 2018; Kroll et al., 2007; Casari & Luini, 2009; Noussair & Tucker, 2005; Reuben & Riedl, 2009).
  - *Close/adjacent*: A robust subset broadens to closely related environments (common-pool resource games, threshold games, trust games/principal-agent games, networked and spatial PGGs). Some theoretical/mechanistic papers, or field applications, are "close" or "adjacent" for certain variants.
- **punishment_or_sanctions**:
  - *Exact relevance*: Many papers directly enable or manipulate costly peer punishment, with carefully controlled conditions; some also address institutional, exclusionary, ostracism, or inspection-based sanctions.
  - *Adjacent/indirect*: Several papers focus on reward, reputation, communication, or other pro-cooperation mechanisms but do not always manipulate peer punishment per se; their relevance to the prediction task diminishes accordingly.
- **efficiency_or_related_payoff_outcome**:
  - *Exact relevance*: A substantial number of empirical and some theoretical studies measure group efficiency, total group payoff, welfare, or surplus as the primary treatment outcome.
  - *Close/adjacent*: Some only report group contribution or cooperation rates—recognized as important but non-equivalent proxies; a minor set reports only non-payoff behavioral or attitudinal outcomes.
  - *Weak/none*: Few studies in the set are totally irrelevant; most have at least adjacent relevance.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes**: "Efficiency" (group total payoff relative to maximum possible for full cooperation) is reported or can be directly calculated in many foundational experimental studies (e.g., Sefton et al., 2007; Arechar et al., 2018; Fehr et al., 2002; Kroll et al., 2007; Casari & Luini, 2009; Maier-Rigaud et al., 2010; Kölle, 2015; Casari & Plott, 2003; Ostrom, 2006). Some papers report group earning/welfare/surplus, or related metrics, which bear a close relationship to efficiency as defined in the prediction task.
- **Non-payoff behavioral outcomes**: Contribution rates, cooperation rates, punishment/reward frequency, norm compliance, social preferences, and emotional/psychological measures are reported in many other studies. These often explain mechanisms or motivational underpinnings, and are sometimes used as proxies for efficiency in papers that do not report efficiency directly.
- **Distinction and linkage**: Evidence strongly distinguishes the two classes. Many papers explicitly caution that increased cooperation or contribution does not guarantee increased efficiency due to the direct cost of punishment and potential for anti-social or inefficient use of sanctions (e.g., Casari & Luini, 2009; Decker et al., 2003; Bochet et al., 2006; Tan, 2008).

# 4) Main Findings Relevant To Prediction

## Empirical Evidence (Direct/Exact/Close):

- **Standard PGGs – Peer Punishment:** In canonical repeated linear PGGs with moderate group sizes (3–5 players) and typical MPCR (0.3–0.5), enabling peer punishment nearly always increases average group efficiency in later rounds, relative to the control without punishment—provided that punishment is not prohibitively costly and anti-social punishment is minimal (Sefton et al., 2007; Arechar et al., 2018; Fehr et al., 2002; Noussair & Tucker, 2005; Kroll et al., 2007). The efficiency gain is due to increased, sustained cooperation and a declining punishment rate over time (as threats suffice), such that the cost of punishment becomes small compared to the efficiency gained.
- **Cost and Effectiveness of Punishment:** The cost-impact ratio (punishment_tech) is a critical moderator. Punishment mechanisms where the impact (reduction in target's earnings) is large relative to cost to punisher (e.g., 1:3 or higher) lead to larger efficiency gains; when costs are high relative to impact, gains are smaller and sometimes absent (Tan, 2008; Casari & Luini, 2009; Decker et al., 2003; Dannenberg & Gallier, 2020; Sethi & Somanathan, 2003).
- **Punishment Structure and Institution:** Details matter: Institutions that require consensus or filter out anti-social punishment (e.g., "consensual" punishment rules) lead to greater efficiency gains than those allowing uncoordinated or anti-social punishment (Casari & Luini, 2009; Decker et al., 2003).
- **Communication and Information:** Communication alone (chat/face-to-face) can raise both cooperation and efficiency more effectively. Adding punishment to a communication-enabled game adds little further efficiency (Bochet et al., 2006; Oprea et al., 2014). Where communication is absent, punishment effects are stronger (Sefton et al., 2007).
- **Group Composition/Heterogeneity:** Efficiency gains from punishment are much smaller (or absent) in groups with payoff heterogeneity (differences in valuation/capability/productivity) or privilege structures, especially for valuation heterogeneity (Reuben & Riedl, 2009; Kölle, 2015).
- **Anti-social/Perverse Punishment and Feuds:** When anti-social punishment (punishing cooperators) or feuding is prevalent, efficiency gains disappear or are reversed; behavior and efficiency depend on context (Nikiforakis & Engelmann, 2011; Ones & Putterman, 2007).
- **Other Sanction Mechanisms:** Exclusion/ostracism (Maier-Rigaud et al., 2010; Charness & Yang, 2014), reputation/monitoring, and weak institutional sanctions can increase efficiency, sometimes as effectively as direct costly punishment.

## Theoretical/Simulation Evidence (Close/Indirect):

- **Mechanisms:** Theory confirms and helps explain empirical findings—the benefit of punishment depends on cost/effectiveness, group size, structure (Gardner & West, 2004; Sethi & Somanathan, 2003).
- **Phase transitions/Spatial Models:** In networked/spatial games, punishment expands the parameter range for sustainable cooperation and thus potential efficiency (Perc, 2016; Wang et al., 2021). Adaptive (context-sensitive) punishment or reward is more effective for efficiency than static punishment (Szolnoki & Perc, 2012; Szolnoki & Perc, 2016).
- **Limitations of Mechanisms:** Punishment can fail (or backfire) in the presence of high anti-social punishment, high cost, poor targeting, or second-order free-riding.

# 5) Prediction Guidance

- **Direct prediction of average treatment efficiency from control efficiency and game dimensions is well-informed by the literature in standard repeated linear PGGs (3–5 players, 10–20 rounds, no chat, anonymous punishment, fixed cost-impact punishment, known number of rounds, no reward):**
  - If the control efficiency is low (cooperation decays quickly), enabling punishment is likely to yield a moderate to large increase in efficiency, especially if punishment costs are not too high and anti-social punishment is minimal.
  - Efficiency gains are typically time-dependent: early periods may see lower efficiency due to initial punishment use; in later periods, as cooperation stabilizes and punishment becomes mostly a threat, net efficiency rises above control (Sefton et al., 2007; Arechar et al., 2018; Fehr et al., 2002).
- **Key moderators for prediction:**
  - **punishment_cost / punishment_tech**: Higher impact per cost leads to greater efficiency gains; excessively costly punishment can nullify gains or even reduce efficiency.
  - **player_count**: Smaller groups see stronger effects; as group size increases, effectiveness and efficiency impact of punishment generally declines (Carpenter et al., 2009).
  - **mpcr**: Higher MPCRs (more efficient public good) amplify both the scope for efficiency improvement and the magnitude of efficiency gains from punishment.
  - **num_rounds / show_n_rounds**: Longer games and known number of rounds favor greater cumulative efficiency gains from punishment, as groups have more opportunity to learn/use threats efficiently.
  - **chat**: If chat or open-ended communication is enabled, it is a more effective tool for promoting efficiency than punishment; enabling both punishes and chat does not further increase efficiency beyond chat alone.
  - **Institutional Design**: Mechanism details such as consensus requirements, anti-perverse-punishment filters, visibility of punishment/identity, and presence of audit/inspection or exclusion can dramatically moderate the efficiency effect (Casari & Luini, 2009; Nikiforakis & Engelmann, 2011).
  - **Heterogeneity**: Efficiency gains from punishment decrease or vanish as group heterogeneity in MPCR, payoff structure, or privilege increases (Reuben & Riedl, 2009; Kölle, 2015; Tan, 2008).

# 6) Design Dimensions Highlighted Across Papers

- **Directly informed**: 
  - `player_count`, `num_rounds`, `mpcr`, `punishment_cost`, `punishment_tech`, and to a lesser extent `all_or_nothing`, `show_n_rounds`.
  - Variations in these are well-covered in canonical experiments and form the basis of most robust comparative results.
- **Indirectly informed**: 
  - `chat` (communication), `show_other_summaries` (feedback), and `show_punishment_id`. Communication structure and feedback are often varied but less frequently as primary design variables.
- **Contextually discussed**:
  - `default_contrib` (framing effects), `reward_exists`/`reward_cost`/`reward_tech` (presence and cost of reward mechanisms), with reward typically found less effective than punishment for sustaining efficiency.
- **Effectively missing or under-specified**:
  - Some dimensions, such as `show_other_summaries`, `show_punishment_id`, `reward_cost`, `reward_tech`, and nuances of `default_contrib`, appear rarely and are mostly discussed in behavioral or institutional context rather than as systematically manipulated variables affecting efficiency. Many studies also lack full cross-design matrices, meaning interactions are rarely exhaustively tested.
  - Effects of social or demographic heterogeneity are less directly mapped onto the listed design dimensions.

# 7) Important Limitations

- **External Validity**: While standard PGGs dominate, field contexts and high-heterogeneity groups show greater ambiguity and conditional effects. Results obtained in canonical lab settings may not generalize where culture, group norm strength, or social capital differ markedly (Lopez et al., 2012; Gelcich et al., 2013).
- **Mechanism Complexity**: Efficiency is mediated by a range of second-order effects (anti-social punishment, feuds, group composition, communication), many of which are not readily parameterized in the 14 listed dimensions.
- **Scope of Variation**: Some design dimensions have not been systematically or independently manipulated, or are confounded; institutional details (e.g., consensus vs. unilateral punishment) can reverse the direction of punishment’s effect on efficiency while holding all other parameters constant (Casari & Luini, 2009).
- **Measurement Gaps**: In several influential studies, only cooperation/contribution rates are measured or emphasized—often closely (but imperfectly) correlated with efficiency, but not substitutable for payoff-based measurement needed in prediction.
- **Time Dynamics**: Average (over all rounds) treatment efficiency may mask important dynamic effects—punishment costs can reduce early efficiency, but cooperation is sustained in later periods and cumulative efficiency gains depend on the specific trajectory.
- **Generalizability to Variants**: Findings on exclusion/ostracism, reward, or communication-based rules cannot always be mapped directly onto costly peer punishment; hybrid designs may exhibit non-additive effects. Network/spatial structures and real-world complexity (institutional mixing, excludability, enforcement asymmetries) are only partially modeled.
- **High-level Theoretical Arguments**: Although theory is consistent with and helps interpret empirical findings, many model-based papers report non-payoff or evolutionary outcomes, or assume conditions away (e.g., anti-social punishment), limiting their precise quantitative relevance for payoff prediction.

---

## In summary:

The literature provides a firm empirical basis and moderate theoretical support for prediction of efficiency in PGGs with peer punishment, conditional on the specific design dimensions noted above. Direct, well-measured outcomes are strongest for canonical repeated linear PGGs with moderate group size, moderate MPCR, no chat, and “standard” punishment; under these conditions, enabling punishment reliably increases efficiency provided costs are not excessive and the institution limits anti-social punishment and feuding. Other dimensions are less well parameterized, and prediction outside the controlled space (especially with high heterogeneity, perverse punishment, or complex institutional settings) should be approached with caution, noting that efficiency gains are neither universal nor monotonic and can reverse under pathological punishment dynamics or poor institutional design.
