# 1) Evidence Base

The evidence base consists exclusively of theoretical and simulation-based papers (56 total), with **no empirical or experimental studies** directly included. All findings are theoretical derivations, simulations, modeling results, or conceptual discussions. The set is **narrow with respect to empirical data for the specific prediction task** (laboratory public goods game with/without punishment), but **broad in the theoretical mechanisms and game structures** analyzed: it covers exact public goods games (PGG), close variants (volunteer’s dilemma, repeated PD, trust/investment games, common-pool resources, networked games), and adjacent contexts (market, family, signaling, group selection). The models often extend, generalize, or comment on canonical PGG frameworks.

Most papers closely analyze **sanctioning mechanisms** (punishment, peer/centralized, institutional, collective, severity, cost, targeting), and typically treat **payoff-based outcomes** (efficiency, group welfare, total earnings) as primary or central. There is, however, **high diversity in the types of games, punishment implementations, and theoretical frameworks** presented. Behavioral outcomes, such as cooperation/contribution rates, are analyzed primarily as mechanisms or intermediate states toward efficiency.

# 2) Task Relevance

**pgg_or_variant:**  
- **Exact:** ~16/56 papers directly analyze canonical or lab-based PGGs (Alventosa & Olcina, 2021; Huang et al., 2024; Tanimoto, 2018; Botta et al., 2021, etc.).
- **Close:** ~20 papers analyze adjacent or structurally similar games (repeated PD, common-interest, helping, team trust, donation games).
- **Adjacent/none:** ~20 in more distant but conceptually related domains (market games, family, investment games).

**punishment_or_sanctions:**  
- **Exact:** Most of the evidence directly models **punishment (peer or institutional)**, including its design details—cost, magnitude, targeting, timing, effectiveness (Huang et al., 2024; Alventosa & Olcina, 2021; Tanimoto, 2018; etc.).
- **Close/adjacent:** Several explore punishment analogues (reputation loss, exclusion, social pressure), or only mention/simulate punishment in passing.
- **Weak/none:** A small number reference only reward, reputation, or contract mechanisms (no punishment dimension).

**efficiency_or_related_payoff_outcome:**  
- **Exact:** A substantial portion of papers explicitly study **group payoff, efficiency, welfare, or surplus** as the main or only outcome.
- **Close/adjacent:** Some focus on behavioral outcomes (contribution/cooperation rates), and only infer or qualitatively discuss efficiency.
- **Weak/none:** Context-only papers or those discussing norms without payoff analysis.

**Summary:**  
**Direct, theory-based relevance** is **strongest for settings structurally similar to repeated PGGs with explicit punishment**, but **weak for empirical calibration or real-world implementation** due to the lack of lab/field data. Most results on efficiency are derived, not measured.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes**:
- Central to most analyses: group efficiency (payoff as % of full cooperation), total group earnings, welfare/surplus, group or social welfare (Alventosa & Olcina, 2021; Huang et al., 2024; Tanimoto, 2018; Sugaya & Wolitzky, 2023; Botta et al., 2021; much of the adjacent game theory literature).
- Explicit formulas for efficiency under varied incentive systems (punishment cost, magnitude, player count, etc.).
- Some models partition static (immediate) vs. dynamic (long-run/evolutionary) efficiency (Povey, 2014).

**Non-payoff, behavioral outcomes**:
- Contribution, cooperation rate, norm compliance, punishment frequency.
- Mechanism-level studies: frequency of sanctioning, structure of contribution cycles, stability of cooperation.
- Such outcomes are used as proxies for efficiency or as intermediate mechanisms, with **frequent caveats that higher cooperation does not guarantee higher efficiency** (Tanimoto, 2018).

**Distinction:**  
The most prediction-relevant papers explicitly keep **efficiency/welfare** as the main outcome. Where outcomes are only at the behavioral level, that is treated as an **inferential or indirect** indicator for efficiency.

# 4) Main Findings Relevant To Prediction

A synthesis of the most prediction-relevant points:

- **Punishment generally increases efficiency relative to control** (no-punishment baseline), but **only when certain design criteria are met**: punishment must be effective (cost-to-impact ratio high), sufficiently strong, and well-targeted (Huang et al., 2024; Sugaya & Wolitzky, 2023; Evans & Thomas, 2001; Botta et al., 2021).
- **There exist critical punishment thresholds**: Only when punishment severity/likelihood passes a theoretically derived minimum is the full-cooperation (maximal efficiency) equilibrium stable (Huang et al., 2024; Botta et al., 2021). Below this, intermediate or low-efficiency equilibria persist.
- **Punishment effectiveness depends on design dimensions**:
    - **Punishment cost/punisher cost**: If too high, punishment may support cooperation but reduce overall efficiency due to wasted resources (Tanimoto, 2018; Heller & Sieberg, 2008).
    - **Player count and group size**: Larger groups (higher player_count) make coordination on punishment harder—effectiveness and efficiency gains may be harder to achieve, but institutional or community punishment mechanisms can mitigate this (Sugaya & Wolitzky, 2023; Annen, 2011).
    - **Information structure/monitoring**: Efficient outcomes are only sustainable when deviant behavior is observable and attributable (Mihm & Toth, 2020; Laclau & Tomala, 2017; Feinberg & Kets, 2014).
    - **Game duration/rounds**: Longer repeated interaction increases scope for efficiency via punishment, as threat of future sanction supports cooperation (Aramendia, 2006; Evans & Thomas, 2001; Jones, 1999).
    - **Punishment technology**: Centralized/institutional punishment is often more effective at improving efficiency, especially in large or heterogeneous groups (Alventosa & Olcina, 2021; Wang et al., 2023).
- **Reward and punishment**: Joint use of positive (reward) and negative (punishment) incentives can, in theory, achieve maximal efficiency with minimal punishment if reward budgets are exhausted first (Huang et al., 2024).
- **Contextual/structural moderators**: 
    - **Network structure, monitoring, relatedness, prevalence of commitment types**: Can yield bi-stability, non-monotonic, or even negative efficiency effects depending on the environment (Tanimoto, 2018; Dong et al., 2024; Pei, 2024; Povey, 2014).
    - **Implementation frictions and assignment of institutional control**: Poorly aligned or costly institutions may over- or under-implement punishment, causing inefficiency even when punishment is conceptually available (Alventosa & Olcina, 2021).
    - **Targeting of punishment**: Punishment targeted at “bad apples”/defectors is essential for sustaining high efficiency, especially as group size grows (Sugaya & Wolitzky, 2023).

- **Potential for negative or ambiguous effects**:
    - High punishment cost/resource drain can lead to decreased efficiency, even if cooperation rises (Tanimoto, 2018; Povey, 2014).
    - Coordination problems, strategic manipulation, or misalignment of punishment incentives can offset or reverse expected efficiency gains (Spitzer, 2016; Harbaugh & To, 2014).
    - Evolutionary/cultural dynamics: Over long time frames, reliance on punishment can crowd out intrinsic cooperation, reducing dynamic welfare (Povey, 2014).

# 5) Prediction Guidance

**For predicting the average efficiency in a PGG-like game when peer punishment is enabled (treatment), relative to control (no punishment):**

- **Directionality**: Theoretical results predict that, when punishment is (a) effective (high impact per cost), (b) correctly targeted at defectors, and (c) credible/enforceable, **treatment efficiency will increase sharply relative to control efficiency**, often approaching the full cooperation benchmark (Huang et al., 2024; Sugaya & Wolitzky, 2023; Botta et al., 2021).
- **Magnitude**: The predicted efficiency gain **depends on the cost, effectiveness, and coverage of punishment**, as well as baseline control efficiency. Maximal treatment efficiency (≈1) occurs when punishment just crosses the critical “incentive compatibility” threshold needed to prevent defection; above this, further increases in severity/cost are redundant and may waste resources (Huang et al., 2024; Botta et al., 2021).
- **Moderators**:
    - **Punishment cost and magnitude**: If cost is high and/or magnitude is low, efficiency gains are reduced or may even become negative as resources are spent on sanctioning (Tanimoto, 2018; Heller & Sieberg, 2008).
    - **Monitoring and attribution**: Imperfect or limited information (e.g., hiding outcomes, not showing who punished) can undermine the effectiveness of punishment and reduce efficiency gains (Mihm & Toth, 2020; Laclau & Tomala, 2017).
    - **Group size and institution type**: Peer punishment may become less effective/more costly in large groups, while centralized or institutional punishment can sustain high efficiency if well implemented (Alventosa & Olcina, 2021).
    - **Initial control efficiency**: **If control efficiency is already high, efficiency gains from punishment may be limited or unnecessary; if low, potential for large treatment gains exists** (Huang et al., 2024).
    - **Psychological and network factors**: Overweighted punishment probabilities (PT), network structure, and relatedness can lead to variable efficiency outcomes.

- **Ambiguity and limits**: Prediction should **allow for negative or zero effects** of punishment on efficiency (even with increased cooperation) when:
    - The design produces high punishment costs.
    - Monitoring is poor or information is noisy.
    - Institutions are misaligned or over-implemented.
    - Network or population structure undermines targeting.

- **Indirect evidence**: Papers reporting only increased cooperation or norm compliance (not payoff) should be *caveated*: improved behavioral outcomes do not guarantee higher efficiency, especially if achieved via costly punishment (Ogaki & Tanaka, 2017; Teraji, 2016).

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions (frequent, central in theory):**
- `player_count` (group size): Directly modeled as equilibria and punishment incentives scale with size.
- `num_rounds`: Extensive analysis of repeated vs. one-shot games; makes cooperation via punishment feasible.
- `mpcr` (Marginal per-capita return): Modeled as a baseline determinant of payoff incentives, critical for threshold analysis (Huang et al., 2024; Botta et al., 2021).
- `all_or_nothing`: Binary vs. continuous contributions alter equilibrium structure.
- `punishment_cost`, `punishment_tech`, `punishment_magnitude`: Nearly all theory analyses focus on these as key determinants of outcomes.
- `reward_exists`, `reward_cost`, `reward_tech`: Studied in settings with joint incentives (Huang et al., 2024).
- `show_other_summaries`, `show_punishment_id`, `show_n_rounds`: Informational structure, observability, and transparency of punishment and actions are central moderators (Mihm & Toth, 2020; Laclau & Tomala, 2017).

**Indirect/contextual dimensions:**
- `chat`: Explored in adjacent models focusing on communication and signaling but not central to payoff predictions.
- `default_contrib`: Only briefly touched where action framing or minimum contribution is discussed, rarely modeled as a direct prediction moderator.

**Effectively missing:**
- No theory in the set models or analyzes `default_contrib` (opt-in/opt-out framing) as a systematic determinant of efficiency under punishment.
- Some dimensions (e.g., explicit `chat`, reward magnitude/cost interaction in complex lab designs) are referenced rarely and with limited direct connection to predicted efficiency.

# 7) Important Limitations

- **No empirical effect sizes**: All outcomes are theoretical; there are **no data-based quantitative estimates** of treatment-control efficiency differences. Thus, predictions must be founded on **relative changes** and parametric thresholds, not direct effect magnitudes.
- **Wide generality and abstraction**: Many models are highly abstracted or concern close structural analogues (PD, team trust, helping games), which may limit transferability to concrete lab PGGs with complex interfaces and constraints.
- **Limited treatment of heterogeneity and implementation frictions**: While some acknowledge institution misalignment, costly implementation, or imperfect monitoring, few provide operational recipes for adjusting predictions in realistic, imperfectly implemented PGGs.
- **Potential for negative/ambiguous effects often underplayed**: Some models emphasize positive—sometimes maximal—treatment effects, but evidence (Tanimoto, 2018) highlights that increased cooperation does not always mean higher efficiency, especially when punishment is costly or poorly targeted.
- **Behavioral proxies can be misleading**: Where evidence is based on increased cooperation alone, the prediction for efficiency must be **explicitly qualified**—behavioral gains may be offset or more than offset by punishment costs.
- **Game design coverage is partial**: Some design dimensions (default option framing, chat/communication, detailed reward structure) are under-explored; results are best for classic, parameterized PGGs, less so for modern or hybrid lab games.

---

**In summary**: The literature synthesized here is a theoretical, modeling-based foundation for punishing effects in PGG-like environments. Its predictive value is **strongest for classic parametric PGGs** with clear, well-understood mechanisms; **caution is warranted for empirical settings, novel hybrids, or designs outside the analyzed scope**. For the prediction task (treatment efficiency given design and control efficiency), the main directional and qualitative effects are well-mapped, but **quantitative precision and context-specific adjustment require complementary empirical evidence**.
