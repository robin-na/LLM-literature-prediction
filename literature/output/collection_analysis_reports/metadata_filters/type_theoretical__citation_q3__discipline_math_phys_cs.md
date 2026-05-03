# 1) Evidence Base

The evidence base is composed entirely of theoretical modeling and simulation papers; there are no controlled experiments or real-world empirical studies in the supplied set. The scope is broad in terms of the types of public-goods-game-like (PGG-like) environments addressed: standard PGGs (linear, threshold, spatial, voluntary, hierarchical, with or without exclusion, etc.), as well as closely adjacent games (common-pool resources, trust games, snowdrift games, etc.) with similar social dilemma structure. Notably, the literature is predominantly theoretical, with results derived from replicator dynamics, agent-based simulations, and formal game-theoretic analysis. Outcomes are typically modeled over wide parameter sweeps, enabling identification of moderators and demarcation of critical thresholds for cooperation and efficiency. Most findings are qualitative or parametric, with explicit formulas in some theory papers, rather than empirical effect sizes. The set is rich in mechanistic and contextual insights but is limited by the absence of direct empirical data or laboratory experimentation.

# 2) Task Relevance

**pgg_or_variant:**  
- **Exact:** Most papers model standard or variant public goods games directly, many with the same design dimensions as experimental PGGs (e.g., continuous/all-or-nothing contributions, explicit group size, multi-round).
- **Close:** A substantial subset studies adjacent games (common-pool resource dilemmas, trust games, volunteer’s dilemmas, and coordination games) or modifies the standard PGG structure with spatial, hierarchical, or network features.
- **Adjacent/Weak/None:** A minority focus on other games (e.g., prisoner's dilemma, ultimatum games, donation games), providing only tangentially relevant mechanism or context.

**punishment_or_sanctions:**  
- **Exact:** The majority of directly relevant papers explicitly analyze the effect of enabling or disabling punishment (costly, peer, institutional, probabilistic, or tax-based).
- **Close:** Several papers focus on closely related mechanisms (social exclusion, indirect reciprocity, metanorms, partner choice, or hybrid reward/punishment systems).
- **Adjacent/Weak:** Some address only alternative mechanisms (reputation, partner switching, environmental feedback, structural change) rather than economic punishment.
- **None:** A small number do not study punishment at all.

**efficiency_or_related_payoff_outcome:**  
- **Exact:** Many theory papers define and report efficiency as total group payoff relative to the full-cooperation optimum or related measures (aggregate earnings, welfare, mean fitness).
- **Close:** Some report average payoffs or average earnings for each strategy but do not directly translate this into a normalized efficiency ratio.
- **Adjacent:** Numerous studies focus on cooperation rate or behavioral outcomes; some infer efficiency from payoff changes or cooperative stability, but do not report payoff ratios explicitly.
- **Weak/None:** Some papers focus exclusively on behavioral or network outcomes, without any payoff-based analysis.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (direct or close):**  
  - Group efficiency (group total payoff / maximum possible if all cooperate): reported in several theory papers (e.g., Li et al., 2022; Sun et al., 2023; Eldakar et al., 2007; Vasconcelos et al., 2015; Sigmund et al., 2011).
  - Average group payoff, welfare, mean fitness, or surplus: closely related to efficiency (e.g., Noailly et al., 2009; Okada & Bingham, 2008; Kendal et al., 2006; Weibull & Salomonsson, 2006).
  - Explicit mapping between control (no punishment) and treatment (with punishment) efficiency is often given as a function of game parameters.

- **Non-payoff behavioral outcomes (not equivalent):**  
  - Contribution/cooperation rate and frequency of cooperators or punishers: very commonly reported, used as a proxy for the group outcome but not equivalent to efficiency.
  - Stability of cooperative or punishment strategies, phase/state diagrams, prevalence of strategies.
  - Evolutionary stability, critical thresholds for behavior transitions, or phase transitions in population state.
  - Occasionally, static or dynamic features like spatial clustering, network topology effects, or behavioral dynamics are the focus.

- **Absence of payoff outcomes:**  
  - Many studies report only on behavioral or strategic dynamics (e.g., frequency of cooperation) without direct calculation of total payoffs or efficiency, making translation to the prediction task indirect (see e.g., Wu et al., 2017).

# 4) Main Findings Relevant To Prediction

## Empirical Findings  
*(Note: all referred to as "empirical" are actually theoretical or simulation results; no laboratory or field data are present.)*

- **Punishment generally increases group efficiency** relative to the control (no punishment), especially in standard or well-parameterized PGGs, provided the cost of punishment and the effectiveness of the sanction (fine) are favorable (Li et al., 2022; Eldakar et al., 2007; Jiao et al., 2020; Dejong et al., 2008; Gao et al., 2020; Vasconcelos et al., 2015; Sigmund et al., 2011).
- **Critical moderators:** group size (player_count), rounds (num_rounds), MPCR (mpcr), punishment cost (punishment_cost), and punishment technology (punishment_tech/fine) strongly moderate the efficiency effect. High punishment costs, large groups, or short games can diminish or reverse efficiency gains (Eldakar et al., 2007; Oya & Ohtsuki, 2017; Powers et al., 2012; Perry et al., 2018).
- **Population structure (spatial/networked vs. well-mixed):** Punishment is more likely to improve efficiency in spatially structured or networked populations, especially with local (not global) enforcement and when clustering supports cooperator-punisher alliances (Vasconcelos et al., 2015; Noailly et al., 2009; Oya & Ohtsuki, 2017; Wang et al., 2024).
- **Institutional vs. peer punishment:** Institutional (pool) punishment, especially with second-order punishment (punishing non-punishers), can stabilize high efficiency, particularly with voluntary participation. Peer punishment is more cost-burdened and vulnerable to free-riding unless supplemented by additional mechanisms (Sigmund et al., 2011; Dercole et al., 2013).
- **Antisocial punishment and corruption:** If antisocial punishment (defectors punishing cooperators) or institutional corruption is present, efficiency gains may be lost or reversed (Powers et al., 2012; Lee et al., 2015; Lee et al., 2017; Wang et al., 2020). The honesty/transparency of enforcers (punishment_id) is crucial.
- **Effect of reward vs. punishment:** Rewards alone are less robust than punishment at stabilizing high efficiency, but hybrid or adaptive mechanisms can sometimes optimize both cooperation and institutional cost (Sun et al., 2023; Okada et al., 2015; Kendal et al., 2006). The cost-effectiveness of the implemented mechanism is key.
- **Graduated punishment and probabilistic execution:** Adaptive, feedback-based, graduated, or probabilistic punishment mechanisms often produce higher efficiency and lower cost than fixed, deterministic punishment, especially in high-cost environments (Jiao et al., 2020; Iwasa & Lee, 2013; Couto et al., 2020).
- **Critical parameter thresholds:** There are explicit conditions—thresholds for mpcr, punishment cost/fine, or group size—below which punishment fails to improve efficiency (Li et al., 2022; Oya & Ohtsuki, 2017; Deng et al., 2012; Wang et al., 2010; Perry et al., 2018).
- **Benefit function shape:** In non-linear benefit (threshold or sigmoid) games, punishment sometimes adds little to efficiency, as cooperation can already be stable (Archetti & Scheuring, 2013).

## Theory and Mechanism Arguments

- The cost-benefit structure (punishment_cost/punishment_tech vs. MPCR) determines the net effect: when punishment is cost-effective and not overly burdensome, efficiency increases; otherwise, it may fall.
- The broader incentive structure (presence/absence of second-order incentives, meta-incentives) can determine whether punishment works in the long run (Okada et al., 2015).
- The structure of access to information, visibility of rounds, and punishment identity (show_n_rounds, show_punishment_id) further moderate the outcome (Lee et al., 2015).

# 5) Prediction Guidance

- **If punishment is enabled in a standard PGG and the cost-to-impact ratio is moderate or low, group efficiency is expected to increase substantially relative to the no-punishment control, especially if the control efficiency is low (i.e., baseline cooperation is low)** (Li et al., 2022; Eldakar et al., 2007; Wang et al., 2010; Dejong et al., 2008; Gao et al., 2020).
- **The quantitative increase in efficiency can often be estimated from explicit formulas or phase diagrams based on player_count, num_rounds, mpcr, punishment_cost, and punishment_tech** (Li et al., 2022; Jiao et al., 2020; Deng et al., 2012; Dercole et al., 2013).
- **Positive effects on efficiency are diminished if:**
    - Punishment is very costly (punishment_cost high, punishment_tech/fine low)
    - The group size is large and/or population is well-mixed (Oya & Ohtsuki, 2017; Powers et al., 2012)
    - Control efficiency is already near the cooperation maximum (Archetti & Scheuring, 2013)
- **Enabling probabilistic or graduated punishment can out-perform always-on, fixed punishment if constraint by cost** (Jiao et al., 2020; Couto et al., 2020; Iwasa & Lee, 2013).
- **Institutional features:** If the punishment mechanism is subject to corruption, antisocial use, or lacks a supporting incentive structure (e.g., no second-order punishment), enabling punishment may have no effect or can even decrease efficiency (Lee et al., 2015; Powers et al., 2012; Sigmund et al., 2011; Okada et al., 2015).
- **Evidence for prediction is strongest when mapping is direct:** when the input design dimensions match the model’s parameterization, and the reported outcome is efficiency or normalized group payoff.
- **Empirical laboratory or field data are missing; thus, all predictions remain at the level of calibrated theoretical expectation, not empirical effect sizes.**

# 6) Design Dimensions Highlighted Across Papers

| Dimension                  | Informed Status            | Evidence Summary & Prediction Implications                                                           |
|----------------------------|---------------------------|------------------------------------------------------------------------------------------------------|
| player_count               | Direct                    | Heavily modeled; efficiency benefits from punishment are reduced as group size increases              |
| num_rounds                 | Direct                    | More rounds favor punishment’s effectiveness; one-shot games rarely benefit from punishment           |
| chat                       | Effectively missing       | Largely not modeled; a few context mentions, but no systematic study                                 |
| all_or_nothing             | Direct                    | Both continuous and all-or-nothing settings analyzed; rarely a strong moderator unless nonlinearity   |
| default_contrib            | Effectively missing       | Not reported in these theory papers                                                                  |
| mpcr                       | Direct                    | Central moderator; higher MPCR supports cooperation/efficiency and punishment success                 |
| punishment_cost            | Direct                    | Explicitly parameterized; lower costs (relative to fine) increase punishment effectiveness            |
| punishment_tech            | Direct                    | Fine effectiveness modeled; high impact relative to cost is crucial for efficiency gains              |
| reward_exists              | Direct/Indirect           | Reward often modeled alongside punishment; reward alone rarely stabilizes high efficiency             |
| reward_cost                | Indirect/Contextual       | Sometimes modeled; interacts with reward effectiveness in hybrid systems                              |
| reward_tech                | Indirect/Contextual       | As above                                                                                             |
| show_n_rounds              | Contextual/Indirect       | Occasionally mentioned as affecting strategies but not systematically modeled                         |
| show_other_summaries       | Indirect/Contextual       | Sometimes included as reputation/feedback, often boosts effectiveness of punishments                  |
| show_punishment_id         | Indirect/Contextual       | Considered in relation to transparency and honest enforcement (Lee et al., 2015)                      |

- **Most informed:** player_count, num_rounds, mpcr, punishment_cost, punishment_tech, all_or_nothing
- **Partially informed/contextual:** reward_exists, reward_cost/reward_tech, show_other_summaries/show_n_rounds/show_punishment_id
- **Not informed/missing:** chat, default_contrib

# 7) Important Limitations

- **No empirical data:** The literature base lacks empirical laboratory or real-world field experiments to quantify or validate theoretical predictions.
- **Indirect mapping for some dimensions:** Some design features in prediction (such as chat, default contribution, or visibility details) are not directly modeled or only discussed contextually; effects must be inferred or are missing.
- **Behavioral outcomes ≠ efficiency:** Many papers use cooperation or contribution rates as the main outcome, which do not necessarily translate one-to-one to efficiency, especially when punishment is costly; predictions based solely on cooperation rates may overstate efficiency gains.
- **Absence of noise, heterogeneity, or empirical realism:** Theoretical models may assume simplistic updating, perfect rationality, or large/infinite populations, which can mean real-world applications deviate in important ways.
- **Parameter sensitivity and threshold effects:** Many findings are contingent; small changes to punishment cost, effectiveness, population structure, or other parameterizations can dramatically alter the predicted efficiency effect.
- **Negative or null effects possible:** Under some realistic conditions (e.g., costly or corruptible punishment, strong antisocial punishment, ineffective impact), enabling punishment can reduce or have no effect on efficiency (Powers et al., 2012; Isakov & Rand, 2012; Jaffe, 2004; Griffin & Belmonte, 2017).
- **Limited treatment of meta-institutional factors (meta-norms, exclusion, second-order punishment):** While some models include these, not all theoretical treatments address the robustness of punishment mechanisms to free-riding or "punishment of punishers."
- **Potential disconnect with laboratory designs or human behavior:** Because all findings are theoretical, the translation to actual experimental PGG treatments may miss important psychological, social, or institutional moderators not present in models.

---

### **Summary**  
The literature base is strong on theoretical guidance for predicting the effect of enabling punishment on efficiency in PGG-like environments, especially when game design dimensions like group size, number of rounds, MPCR, punishment cost, and punishment technology are known. It is less informative—or altogether silent—on effects related to chat, default contribution frames, or some forms of transparency. While the direction of effect is generally positive, important moderators and potential for negative or null effects are well-documented within the model space. However, the exclusive reliance on theory, the focus on cooperation rates over efficiency in many papers, and the lack of empirical validation or behavioral realism present clear limitations for prediction in applied or experimental settings.
