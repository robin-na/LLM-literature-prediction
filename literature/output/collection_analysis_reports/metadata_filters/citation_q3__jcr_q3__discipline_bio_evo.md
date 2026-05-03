# 1) Evidence Base

The paper set consists of **48 papers**, with a notable predominance of **theoretical and modeling work**; there is only a small number of **empirical/experimental studies** directly analyzing efficiency or payoff outcomes in PGG-like games with punishment manipulations. Coverage is **relatively broad** for theoretical exploration of punishment mechanisms in public goods and related social dilemmas, but **narrower** for empirical "treatment vs. control" efficiency results in PGGs with peer punishment. Most studies systematically vary key game-design parameters (e.g., punishment cost, group size, MPCR), but **few directly report experimental efficiency outcomes** using lab or field data with treatment-control contrasts. Some adjacent studies discuss mechanisms such as anti-social punishment, corruption, or institutional enforcement, providing indirect insight. Overall, this literature base is **highly informative for parameter-level, mechanistic, and contextual effects**, but more limited for direct, empirical calibration of prediction models.

# 2) Task Relevance

**Assessment on three target-relevance dimensions:**

- **pgg_or_variant:**  
  - **Exact relevance:** The majority of theory papers model standard or closely matched public goods games (PGG), often referencing the classic experimental paradigm or its close extensions (e.g., Jiao et al., 2020; Eldakar et al., 2007; Oya & Ohtsuki, 2017).
  - **Close/adjacent relevance:** Some papers model related dilemmas (e.g., common-pool resources, threshold/tipping models, or iterated Prisoner's Dilemmas) that share features but differ structurally (Lee et al., 2015; Okado & Bingham, 2008).
  
- **punishment_or_sanctions:**  
  - **Exact relevance:** Most relevant theory papers manipulate explicit peer or institutional punishment (costly sanctions applied by group members; e.g., Eldakar et al., Jiao et al., Dercole et al.).
  - **Close/adjacent relevance:** Certain papers instead model delegated (not peer) punishment, anti-social punishment, or punishment by external authorities, or treat punishment as correlated with reputation or indirect reciprocity (Lee et al., 2017; Powers et al., 2012; Raihani & Power, 2021).
  - **Weak/none:** Several control-focused or reciprocity studies do not model punishment at all.
  
- **efficiency_or_related_payoff_outcome:**  
  - **Exact/close relevance:** About half the papers directly report average group efficiency, total payoff, or explicit ratios to the cooperative optimum (Jiao et al., Eldakar et al., Oya & Ohtsuki, Huang et al.).
  - **Adjacent relevance:** Additional studies report strategy frequencies, cooperation rates, or behavioral states as proxies (Dercole et al., Zhang et al., 2017).
  - **Non-payoff/behavioral only:** Many discuss cooperation rates, norm compliance, or punishment behavior without direct efficiency or payoff reporting.
  - **None:** A subset discusses theoretical mechanisms or evolutionary conditions with **no relevant payoff or efficiency measure**.

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes:**
- **Efficiency:** Group payoff as a fraction of the fully cooperative ideal—directly modeled in many PGG theory papers (Jiao et al., 2020; Eldakar et al., 2007; Oya & Ohtsuki, 2017; Huang et al., 2018).
- **Total payoff / welfare / group achievement:** Explicitly modeled as primary outcomes in most PGG theory research (Archetti & Scheuring, Zhang et al., 2013).
- **Equilibrium payoff, mean fitness, population mean payoff:** Used interchangeably with efficiency in some modeling frameworks.
- **Related but less direct:** Some models report transition rates to all-cooperative/all-defector states (proximal to efficiency but not explicit).

**Non-Payoff Behavioral Outcomes:**
- **Contribution rates / cooperation rates:** Very common in both empirical and theoretical models as indicative of cooperative behavior (see Flores et al., 2021; de Weerd & Verbrugge, 2011).
- **Punishment frequency, norm compliance:** Outcomes such as prevalence of punishment, stability of norms, or cluster abundance are widely measured, but only **proximal** to payoff.
- **Evolutionary stability, basin size, or prevalence of certain strategies:** Common in models focused on evolutionary or dynamic stability rather than direct payoffs.
- **Group survival/collapse:** In some resource games, focus is on group survival rates rather than payoff per se.

**Distinction:** Most studies that do **not** directly report efficiency or group payoff either (a) treat it as implied through full cooperation, or (b) provide only behavioral proxies.

# 4) Main Findings Relevant To Prediction

**Synthesis of Cross-Paper Findings:**

- **Peer punishment (when not prohibitively costly or ineffective):**
  - **Generally increases group efficiency** compared to no-punishment treatments in continuous and discrete PGGs, except under certain conditions (Jiao et al., 2020; Eldakar et al., 2007; Dercole et al., 2013; Huang et al., 2018; Archetti & Scheuring, 2013).
  - **Diminishing returns or possible negative effects** if punishment cost is very high, if group size is large, or if anti-social punishment is prevalent (Powers et al., 2012; Oya & Ohtsuki, 2017; Zhang et al., 2013).
- **Key moderators identified:**
  - **Punishment cost and effectiveness:** Positive effects on efficiency only if punishment is cost-effective, with effectiveness (magnitude of fine per unit cost) a critical parameter (Jiao et al., 2020; Okada & Bingham, 2008).
  - **Population/game structure:** In **well-mixed populations**, punishment is less likely to sustain efficiency; in **spatially structured** or repeated games, positive impacts are stronger (Oya & Ohtsuki, 2017; Nakamaru & Dieckmann, 2009).
  - **Anti-social punishment or corruption:** When punishment can be misapplied (punishing cooperators) or open to corruption, effects range from neutral to negative for efficiency (Powers et al., 2012; Lee et al., 2015; Lee et al., 2017).
  - **Group size and round count:** Effectiveness of punishment in boosting efficiency typically **declines with larger groups** or **very short games** (Eldakar et al., 2007; Dercole et al., 2013).
  - **Reward mechanisms and communication:** Limited direct modeling in most papers, but when available (Milinski & Rockenbach, 2012; Jiao et al., 2020), **reward and reputation can further improve efficiency or reduce punishment's cost**.
  - **Probability of execution:** Probabilistic (versus always-on) punishment is sometimes **more efficient when costs are high** (Jiao et al., 2020).
  - **Benefit function (linearity/nonlinearity):** Punishment is more critical for efficiency in **linear PGGs** (Archetti & Scheuring, 2013).
- **Bistability:** _High- vs. low-efficiency equilibria_ may coexist, especially in models with corruptable enforcement or anti-social punishment (Lee et al., 2015, 2017; Oya & Ohtsuki, 2017).

# 5) Prediction Guidance

**Generalizable Guidance from the Literature:**

- **When average efficiency in the control (no punishment) condition is low, enabling peer punishment** (with moderate cost and sufficient effectiveness) should be expected, by theoretical consensus, to **substantially increase average group efficiency**, except in the following contexts:
  - **Punishment is prohibitively costly** or group is very large (diluting individual impact);
  - **Anti-social punishment/corruption is prevalent** and cannot be identified or controlled;
  - **Game is well-mixed and short**, or
  - **Benefit function is concave or step-shaped** (where cooperation can be stable even without punishment).
- **Key design dimensions** that the literature directly supports for prediction:
  - **player_count**, **num_rounds**, **mpcr**, **punishment_cost**, **punishment_tech** (effectiveness), **all_or_nothing**.
- **Indirect or modeled contextually:** **show_punishment_id** (identity transparency), **reward_exists**, **reward_cost**, **probability of punishment execution**.
- **Sparse/weakly addressed:** **chat**, **default_contrib**, **show_n_rounds**, **show_other_summaries**.
- When **control efficiency is already high**, enabling punishment may offer little or no additional improvement and can sometimes reduce efficiency due to incurred costs (Archetti & Scheuring, 2013; Milinski & Rockenbach, 2012).
- The **positive impact of punishment on efficiency** is stronger in small, repeated, spatially structured groups with moderate costs.
- **Downstream prediction should explicitly incorporate**: punishment cost, punishment effectiveness, population/game structure, and anti-social punishment or corruption risks.
- **Mechanistic or evolutionary models** can provide functional forms or explicit equilibrium conditions (e.g., parameter sweeps), which can, in principle, be used to estimate treatment efficiency as a function of control efficiency and design parameters.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- **player_count**: Explicitly modeled in almost all PGG and variant models; shown to moderate punishment effect (smaller groups = greater impact).
- **num_rounds**: Repeated/one-shot structure is a key moderator; longer games support punishment's positive effects (Eldakar et al., 2007).
- **mpcr**: Central in many models, especially the threshold for cooperation/punishment to be effective (Archetti & Scheuring, 2013).
- **punishment_cost**, **punishment_tech**: Core parameters; cost/magnitude ratio consistently highlighted.
- **all_or_nothing**: Several models explore discrete versus continuous choice (Jiao et al., 2020; Oya & Ohtsuki, 2017).
- **reward_exists** (and, less so, **reward_cost**, **reward_tech**): Few models address joint punishment/reward (Milinski & Rockenbach, 2012; Jiao et al., 2020).

**Indirectly or Contextually Discussed:**
- **show_punishment_id**: Transparency of punishment source is analyzed in some corruption and anti-social punishment models (Lee et al., 2015).
- **show_n_rounds**: Modeled in repeated games with known or unknown round number, relevant for direct reciprocity (Leimar, 1997; Kurokawa & Ihara, 2017).
- **show_other_summaries**, **default_contrib**: Touched on rarely, except in experiments concerned with information feedback and framing.

**Effectively Missing or Rarely Addressed:**
- **chat**: Virtually absent from theoretical models; some empirical studies include but do not link systematically to efficiency outcomes.
- **default_contrib**: Framing aspects are not systematically modeled.
- **show_other_summaries**: Only occasionally considered in the context of information structure, and not shown to be a strong moderator.

# 7) Important Limitations

- **Empirical evidence for treatment effect sizes on efficiency is sparse:** Most findings are from theoretical models or simulations, not experimental contrasts of control versus punishment-enabled PGGs.
- **Anti-social punishment, corruption, and enforcement institution integrity are critical but complex moderators; their real-world variability limits prediction certainty** (Powers et al., 2012; Lee et al., 2015, 2017).
- **Design dimensions such as chat, framing, and information feedback** are not systematically explored or linked directly to efficiency in the core literature, weakening the ability to incorporate them in prediction.
- **Efficiency outcomes are often inferred from cooperation rates, stability, or equilibrium prevalence—not always directly measured.** Proxies can overstate impact in settings where efficiency and cooperation diverge.
- **Theory models frequently assume rational or evolutionary selection dynamics that may not fully capture experimental or field behavior**, especially with complex human psychology (Smith, 2020; André & Morin, 2011).
- **Parameter thresholds (e.g., cost-effectiveness of punishment, population structure, and size) can create abrupt changes in efficiency outcomes**, resulting in possible bistability or non-linear impacts not easily captured with simple regression-type prediction from control to treatment.
- **Mixed or negative effects of punishment on efficiency (due to cost, anti-social use, or redundancy in already efficient games) are observed in a subset of models**, indicating that enabling punishment may not always yield gains, especially in contexts prone to misuse or abuse.
- **Dimensions such as reward mechanisms, network structure, and information transparency interact complexly with punishment and are not independently manipulated in much of the literature.**

---

**Overall:**  
The literature base provides strong theoretical and mechanistic support for the claim that **enabling peer punishment in a PGG typically increases efficiency—if punishment is not excessively costly, anti-social, or corrupt, and the environment is not already highly cooperative.** The effect is **moderated by group size, punishment parameters, game structure, and the integrity of enforcement mechanisms**. Prediction using design dimensions plus control efficiency is well supported for cost, effectiveness, repetition, and group size, but less so for "soft" contextual features (chat, framing, reward design, transparency). Caution is warranted in extrapolation, as **empirical quantification is limited, proxies for efficiency are common, and edge cases exist where punishment fails or backfires**.
