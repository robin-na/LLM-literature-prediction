# 1) Evidence Base

The available literature set is a **broad and deep collection** of **theoretical models** with targeted application to public goods games (PGGs), closely related social dilemmas, and a range of relevant generalizations (e.g., common pool resources, trust games). All analyzed papers are theoretical; there are no direct experimental or empirical studies in this set. However, many models are built to mirror experimental setups and use explicit parameterizations that correspond to lab PGGs (e.g., group size, punishment cost, marginal per-capita return, etc.). This enables nuanced, parameter-level guidance, albeit with the inherent limitations of theoretical abstraction.

The set includes:
- **Many exact PGG models with explicit peer or institutional punishment**: These systematically examine how punishment affects group payoff or efficiency.
- **Models on strategic variants, spatial structure, heterogeneity, and corruption**: Yielding additional context about the boundary conditions for punishment’s effects.
- **Some adjacent or indirect models**: These discuss mechanisms (e.g., reputation, institution-building) or adjacent outcomes (e.g., cooperation rates) rather than group payoff directly.

Overall, this literature base is **highly comprehensive on theoretical prediction of punishment effects on efficiency in PGGs**, but is **lacking in direct empirical corroboration and coverage of certain real-world features** (e.g., chat/communication, experimental idiosyncrasies).

---

# 2) Task Relevance

**pgg_or_variant**:  
- **Relevance**: `exact` for most key papers (classic/continuous/all-or-nothing PGGs), `close` for common pool resource and joint effort games, `adjacent` for trust, bargaining, and coordination games.
- **Assessment**: The set's core is **highly relevant**—virtually all major mechanisms considered are grounded in PGG analogues. Non-PGG papers inform edge cases or supply mechanistic intuition.

**punishment_or_sanctions**:  
- **Relevance**: Most central papers are `exact` (explicit costly peer/institutional punishment as a treatment variable); several are `adjacent` or `close`, modeling reputation, exclusion, or indirect sanctions without explicit punishment cost.
- **Assessment**: The **core is highly relevant**, enabling strong inferences about peer punishment. Some findings on reward, institution-building, or reputation provide context but require careful translation to payoff-based predictions.

**efficiency_or_related_payoff_outcome**:
- **Relevance**: Many key papers are `exact` (total payoff, group welfare, efficiency defined as in the prediction task), with some only `close` (group achievement, surplus, or theoretical maxima), and others `adjacent` (contribution rates, probability of cooperation).
- **Assessment**: The evidence for **direct payoff-based outcomes is strong**, especially among the exact PGG papers, though several supporting models use behavioral proxies rather than efficiency per se.

---

# 3) Outcomes Measured In The Literature

- **Payoff-based outcomes (`efficiency_or_payoff`)**:  
  - Most relevant theory papers (e.g., Jiao et al. 2020; Eldakar et al. 2007; Oya & Ohtsuki 2017; Bednar 2006; Huang et al. 2018; Milinski & Rockenbach 2012; Okada & Bingham 2008) explicitly model and report the group’s average efficiency, total payoff, or welfare as the primary dependent variable.
  - Variants (e.g., steady-state mean payoff, fraction of maximum achieveable payoff) often align conceptually with the prediction task’s `efficiency` definition.

- **Non-payoff behavioral outcomes**:  
  - Several papers focus on **contribution rates, cooperation frequency, prevalence of altruistic or punishing strategies, or cluster survival** as the main outcomes (e.g., de Jong & Tuyls 2011; Hintze & Adami 2015; de Weerd & Verbrugge 2011; Nakamaru & Dieckmann 2009; Szabó et al. 2013).
  - While often correlated with efficiency, these are **distinct**—the direct impact on group payoffs must be inferred, not assumed.

- **Hybrid or adjacent outcomes**:  
  - Some models analyze the evolution of institutions, rule adoption, or cooperation stability (e.g., Bravo 2011; Safarzynska 2013), which often implies (but does not directly report) efficiency consequences.

---

# 4) Main Findings Relevant To Prediction

**Synthesis of Theory Papers with Direct Payoff Outcomes:**
- **Peer punishment usually increases efficiency relative to no-punishment baseline** *(Jiao et al., 2020; Eldakar et al., 2007; Dercole et al., 2013; Bednar, 2006; Okada & Bingham, 2008; Milinski & Rockenbach, 2012; Huang et al., 2018)*—but only under specific conditions of punishment cost, effectiveness, and game duration.
    - **Conditions favoring efficiency gains:**
        - **Punishment is not too costly** and is **effective at deterring defection**.
        - There is **sufficient time for repeated interaction** (more rounds).
        - **Group size is moderate to small**.
        - **Population structure enables local interactions** (spatial/clustering).
        - **Corruption is controlled**—i.e., enforcers are mostly honest (Huang et al., 2018; Lee et al., 2015, 2017).
        - **No widespread anti-social punishment** (Powers et al., 2012).
        - **Voluntary participation can amplify benefits** (De Silva et al., 2010).
    - **Parameter constraints:**
        - When **punishment cost is too high**, efficiency gains are eroded or reversed (Jiao et al., 2020; Bednar, 2006; Okada & Bingham, 2008; Dercole et al., 2013).
        - If **punishment is weak, non-targeted, or if anti-social punishment is present**, net efficiency can fall (Powers et al., 2012).
        - **One-shot or short games** yield little benefit (Eldakar et al., 2007).

- **Probabilistic (not always-on) punishment** can maximize efficiency—even with high costs, offering more robust efficiency gains than deterministic punishment (Jiao et al., 2020).

- **Spatial structure and heterogeneity**:  
    - Strongly positive effects in spatially structured settings/clusters (Oya & Ohtsuki, 2017; Nakamaru & Dieckmann, 2009).
    - Heterogeneous punishment costs/effectiveness enables more efficient, stable cooperation (de Weerd & Verbrugge, 2011), especially with specialized punishers.
    - In well-mixed populations or without structure, punishment effects can be weak, absent, or negative (Oya & Ohtsuki, 2017).

- **Population/institutional context**:  
    - The presence of corruption, honesty of third-party enforcers, and transparency interventions **critically moderate punishment's effect on efficiency** (Lee et al., 2015, 2017; Huang et al., 2018).
    - **Institutional or graduated punishment** (punishment severity/cost increases with harm/defection) usually improves efficiency, especially with player heterogeneity and monitoring errors (Iwasa & Lee, 2013; Couto et al., 2020).

- **Negative or mixed effects**:  
    - **Anti-social punishment**: When defectors punish cooperators, efficiency can stagnate or fall relative to the no-punishment scenario (Powers et al., 2012).
    - **Insurance against punishment** can undermine efficiency if it is too cheap (Zhang et al., 2013).
    - In compulsory participation, or where monitoring/imposition is imperfect, efficiency falls short of full cooperation (Bednar, 2006; Oya & Ohtsuki, 2017).

- **Adjacent findings**:  
    - Reward alone is generally less effective than punishment at raising efficiency, but **combining punishment and reward/reputation** can yield higher payoffs by reducing punishment need (Milinski & Rockenbach, 2012).
    - Non-linear benefit functions (e.g., threshold PGGs) can achieve high efficiency even without punishment (Archetti & Scheuring, 2013).

---

# 5) Prediction Guidance

- **Enabling peer punishment in an otherwise standard PGG, all else equal, is predicted to increase group efficiency relative to a no-punishment baseline,** provided:
    - **Punishment is not prohibitively costly** and is meaningfully effective at deterring defectors (Jiao et al., 2020; Dercole et al., 2013; Eldakar et al., 2007).
    - **Game is repeated** (multiple rounds): longer games allow punishment to generate deterring reputational effects, increasing the efficiency gap versus control (Eldakar et al., 2007; Milinski & Rockenbach, 2012).
    - **Group size is moderate**: Larger groups dilute punishment’s effectiveness, decrease monitoring, and lower efficiency gains from punishment (Eldakar et al., 2007; Powers et al., 2012).
    - **Population structure or spatial clustering exists**: Clustering strongly magnifies efficiency gains from punishment and enables coexistence of cooperators and punishers (Nakamaru & Dieckmann, 2009; de Weerd & Verbrugge, 2011; Oya & Ohtsuki, 2017).
    - **Monitoring is sufficiently accurate or informative**: Imperfect monitoring or corruption can limit efficiency gains (Bednar, 2006; Huang et al., 2018; Lee et al., 2015, 2017).
    - **Probabilistic punishment** can outperform deterministic punishment in maximizing efficiency when costs are high (Jiao et al., 2020).
    - **Absence of widespread anti-social punishment and insurance loopholes** is important to maintain efficiency gains (Powers et al., 2012; Zhang et al., 2013).

- **Quantitative prediction**: Use the control game’s average efficiency as the base rate. Predict a **strictly higher efficiency in the peer punishment treatment**, with the effect size modulated as follows:
    - **Lower punishment cost / higher punishment magnitude** → greater efficiency gain (Dercole et al., 2013; Okada & Bingham, 2008).
    - **Longer games / more rounds** → larger efficiency increases due to repeated deterrence (Eldakar et al., 2007; Milinski & Rockenbach, 2012).
    - **Larger groups / less spatial structure** → smaller efficiency gain; effects can become negative with large groups and anti-social punishment (Powers et al., 2012).
    - **Imperfect enforcement or corruption** → efficiency rise is attenuated or even reversed if non-cooperating enforcers dominate (Huang et al., 2018; Lee et al., 2015, 2017).

- **Special caveats**:
    - **All-or-nothing vs. continuous games**: Punishment effectiveness varies; in all-or-nothing, outcomes are often more polarized (Oya & Ohtsuki, 2017).
    - **Nonlinear benefit functions**: If the PGG is non-linear (threshold/sigmoid), punishment’s marginal benefit may be minimal (Archetti & Scheuring, 2013).
    - **Voluntary participation amplifies payoff gains from punishment**, while compulsory participation can eliminate the positive effect (De Silva et al., 2010).

**Dimension-to-prediction mapping**: For practical prediction, the literature supports using the 14 design dimensions, especially `player_count`, `num_rounds`, `mpcr`, `punishment_cost`, `punishment_tech`, `reward_exists`, and aspects of monitoring (`show_other_summaries`, `show_punishment_id`). Dimensions like `chat`, `default_contrib`, and some visibility/framing aspects are less directly addressed in this evidence set.

---

# 6) Design Dimensions Highlighted Across Papers

- **Directly informed** (explicit/quantitative parameterization and effect evidence):  
    - `player_count`: Many models vary group size, showing diminishing efficiency boosts with increasing group size (Eldakar et al., 2007; Dercole et al., 2013; Powers et al., 2012).
    - `num_rounds`: Longer repeated interactions increase the return to punishment and efficiency gains (Eldakar et al., 2007; Milinski & Rockenbach, 2012).
    - `mpcr`: Central moderator of baseline control efficiency and the sustainability of cooperation with or without punishment (Takezawa & Price, 2010; Dercole et al., 2013).
    - `punishment_cost`: A key moderator; as it increases, efficiency gains shrink and can turn negative (Jiao et al., 2020; Okada & Bingham, 2008; Bednar, 2006).
    - `punishment_tech` (effectiveness of punishment): Higher effectiveness per unit cost yields larger efficiency gains (Okada & Bingham, 2008; Dercole et al., 2013).
    - `reward_exists`: Some theory combines punishment and reward, finding the combination can be synergistic (Milinski & Rockenbach, 2012).
    - `all_or_nothing`: Both continuous and all-or-nothing games are directly modeled.

- **Indirectly informed** (discussed in models or theory but not always in payoff terms):  
    - `show_other_summaries`, `show_n_rounds`: Imperfect/perfect monitoring and information visibility influence equilibrium compliance and efficiency gaps to the cooperation optimum (Bednar, 2006).
    - `show_punishment_id`: Enforcer identification and transparency affect corruption dynamics (Lee et al., 2015).
    - `reward_cost`, `reward_tech`: Less central, but modeled in dual incentive mechanisms (Jiao et al., 2020).
    - `default_contrib`: Framing effects are not systematically modeled, only contextually referenced.

- **Only contextually discussed or effectively missing**:  
    - `chat`: Communication is described as important in reviews (Ehmke & Shogren, 2009), but not incorporated into formal payoff models.
    - `show_other_summaries`, `show_punishment_id`: Usually implicit in monitoring structure, less frequently parameterized as decision variables.
    - Any aspect pertaining to **lab framing, interface, or experimental demand characteristics**.

---

# 7) Important Limitations

- **No direct empirical or experimental findings**: All papers are theoretical or simulation-based, limiting external validity and the ability to calibrate predictions to actual observed efficiency increases.
- **Behavioral outcomes ≠ payoff**: Several supporting models use frequency of cooperation, punishment, or norm adherence as proxies for efficiency; this introduces uncertainty in translating results to actual payoff effects.
- **Limited treatment of some design dimensions**: Features such as communication (`chat`), contribution framing (`default_contrib`), and some visibility controls (`show_punishment_id`, `show_other_summaries`) are underrepresented in quantitative models.
- **Corruption, anti-social punishment, and practical implementation challenges**: While theoretically addressed, real-world rates and context dependence (e.g., cultural variation in anti-social punishment or corruption) are not captured empirically.
- **Boundary conditions are critical**: In some model regimes (high punishment cost, large group size, one-shot games, anti-social punishment or corruption), punishment does **not** improve efficiency and can make it worse. Prediction in these domains is more uncertain.
- **Population and information structure often idealized**: Real-world environments may not achieve the spatial structures, heterogeneity, or monitoring technology assumed in many models.
- **Extrapolation to laboratory or field settings requires caution**, as theoretical models (particularly those with fixed-strategy agents, perfect rationality, or infinite rounds) may overstate or understate the effect size.
- **Prediction outside of classic PGG structure** (e.g., threshold public goods, trust games, common-pool resource dilemmas) is less reliably grounded in this evidence set.

---

In summary, this literature set provides **strong theoretical guidance** for predicting the effect of peer punishment on group efficiency in public goods games as a function of core game design parameters. Positive effects are typical under favorable conditions, but exceptions and complex moderation abound—especially as punishment costs, group size, institutional quality, or population structure vary. Quantitative prediction should weight control (no-punishment) efficiency most heavily, adjust for key design dimensions as highlighted above, and account for strong context-dependent moderators (cost, corruption, anti-social punishment, structure). Empirical validation is a key limitation and opportunity.
