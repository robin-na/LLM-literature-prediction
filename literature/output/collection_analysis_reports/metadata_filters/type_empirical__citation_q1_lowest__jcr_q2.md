# 1) Evidence Base

The paper set comprises 135 empirical studies, almost all experimental, focusing predominantly on standard laboratory public goods games (PGGs) and close variants in resource, market, or trust dilemmas. The majority are narrow, lab-based, and use tightly controlled designs to test hypotheses about peer or institutional punishment, with a notable subset using field or lab-in-the-field methods, meta-analyses, and observational studies for context or external validation. The overall evidence base is broad for PGGs, punishment mechanisms, and behavioral outcomes, and moderately broad for efficiency or payoff-based outcomes, though some studies focus entirely on non-payoff measures (e.g., contribution rates, norm compliance) or psychological mechanisms.

Importantly, a substantial proportion of the literature directly analyzes the efficiency consequences of punishment-enabled treatments compared to controls without punishment, providing high-quality empirical evidence relevant to the downstream prediction task.

# 2) Task Relevance

**Summary of relevance by dimension:**

| Criterion             | High/Exact  | Moderate/Close | Low/Adjacent/Weak/None     |
|-----------------------|-------------|----------------|---------------------------|
| **pgg_or_variant**    | exact/many  | close/subset   | adjacent/minority/none    |
| **punishment_or_sanctions** | exact/many  | close/subset   | adjacent/minority/none    |
| **efficiency_or_related_payoff_outcome** | exact/several | close/many      | adjacent/many/none        |

- **pgg_or_variant**: Task relevance is high. The bulk of the sample consists of experiments using linear PGGs or repeated threshold PGGs with various institutional modifications. A smaller subset works in adjacent territory (e.g., CPR, market/trust games, dictator/ultimatum games).
- **punishment_or_sanctions**: High direct relevance. Many studies systematically manipulate peer punishment, centralized punishment, or formal/informal sanctioning mechanisms. A few focus on adjacent concepts: symbolic rewards, monitoring, exit options, or communication as informal punishment.
- **efficiency_or_related_payoff_outcome**: Good but less comprehensive than for behavioral outcomes; approximately a third of the papers directly report efficiency, group payoff, welfare, or similar. Many additional papers focus on contribution/cooperation (not direct efficiency) or analyze mechanisms rather than reporting aggregate outcomes.

**Overall**, the set is well-suited for informing task predictions in canonical PGGs with punishment, though for some game design dimensions or for causal understanding of mechanisms, the relevance weakens, especially when efficiency rather than contribution behavior is the target.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes:**
- **Direct (exact):** Efficiency (group earnings as a proportion of the cooperative optimum), total group payoff, welfare, surplus, total coins/currency generated. Many primary PGG studies report these outcomes, especially when evaluating enabling punishment.
- **Close:** Some studies report group profit, resource preservation, or market welfare, in designs closely mirroring PGGs.
- **Indirect or contextual:** Many studies do not report efficiency or payoffs, focusing instead on behavioral outcomes.

**Behavioral (non-payoff) outcomes:**
- **Contribution rate, cooperation rate:** Most frequently reported; signify the percentage or amount contributed to the public good.
- **Punishment frequency/amount:** How often or how much players punish, including targeting and motives.
- **Compliance, norm enforcement, partner choice, exclusion/ostracism, information acquisition:** Studied as mechanisms or as indicators of cooperative behavior, but not directly reflecting group welfare.
- **Psychological/attitudinal outcomes:** Fairness preferences, emotional responses, cognitive load effects, and trust.

**Notable distinctions:**
- In a non-trivial subset, punishment increases cooperation but either does not affect or even reduces efficiency due to the costliness of punishment.
- Very few studies measure both contribution and efficiency sufficiently to distinguish between these effects across many game designs.

# 4) Main Findings Relevant To Prediction

**General pattern:**  
- Introducing punishment (peer or institutional) usually increases contributions in PGGs.  
- The impact on efficiency is context-dependent:  
    - **Classic linear PGGs with moderate punishment costs and no or little anti-social punishment:** Enabling punishment often increases efficiency, especially when baseline (control) efficiency is low (Zhang et al., 2024; Jarungrattanapong, 2022; Joseph et al., 2025; Kamei, 2024).
    - **High-cost punishment, or high anti-social punishment, or where punishment is mis-targeted:** Efficiency gains are modest or absent. Sometimes, efficiency is *lower* in the punishment condition due to excessive punishment costs (Botelho et al., 2022; Glöckner et al., 2018; Casari & Tavoni, 2024; Robbett, 2019; Deng et al., 2025).
    - **Punishment technology details matter critically:**  
        - Structures that require group coordination to implement punishment (e.g., Ostracism, democratic or hierarchical leader selection, rule-based centralized punishment): Often yield higher efficiency than fully peer-to-peer, uncoordinated punishment (Benard & Barclay, 2020; Hugh-Jones & Perroni, 2017; Liu et al., 2020; Kamei, 2024).
        - Weak or automatic punishment that is not deterrent can be strictly inefficient or neutral (Yang et al., 2020).
        - Multiple punishment channels (observed and unobserved) can overcome the downside of punishment, improving efficiency (Glöckner et al., 2018).
    - **Antisocial punishment (punishing high contributors) and anti-cooperative retaliation can negate positive effects and sometimes lower efficiency (Kim et al., 2025).**
    - **Cultural and contextual moderators are significant:** Across cultures (Gürdal et al., 2021; Kamei et al., 2025; Davies & Fafchamps, 2021), the payoff effect of punishment can differ—sometimes robust, sometimes context-specific or muted.
    - **Magnitude of punishment:** Strong, well-calibrated punishment increases efficacy. Small or weak punishment may fail to improve, or can worsen, efficiency (Ye et al., 2023; Windrich et al., 2024).
    - **Punishment network and coverage:** Network completeness and coverage of punishment (who can punish whom) is key ("punishment_tech") (Peng & Fan, 2023; Bühren et al., 2025).
    - **Role structure (leader punishment, monitor punishment, centralized 'hired-gun' punishment):** These variants often yield equal or higher efficiency compared to direct peer punishment (Joseph et al., 2025; Zhang et al., 2024; Otto & Bolle, 2016).

**Disagreement and ambiguity:**  
- Some studies and meta-analyses report that, on average, punishment-enabled PGGs do not achieve higher efficiency than controls, especially if punishment is costly, anti-social punishment is present, or if institution choice is endogenous (Botelho et al., 2022; Chugunova et al., 2020; Casari & Tavoni, 2024).
- A substantial number of adjacent studies (especially with field populations or variations in social context) find modulating or null effects of punishment on payoff-related outcomes.

# 5) Prediction Guidance

**What the literature supports for prediction:**
- If the PGG design closely matches standard lab formats (4–5 players, 10–32 rounds, linear MPCR 0.4–0.6, moderate punishment cost and 1:3–1:5 impact, no chat, no rewards), then:
    - Enabling punishment **usually increases efficiency** relative to the control, especially if baseline (control, no-punishment) efficiency is low. The effect is often stronger for formal or leader-administered punishment and when anti-social punishment is limited (Zhang et al., 2024; Joseph et al., 2025; Gürdal et al., 2021; Kamei, 2024).
    - The **magnitude of efficiency improvement is variable** and is influenced by the 14 game design dimensions, especially: punishment_cost, punishment_tech(e.g., who can punish whom), whether punishment is strong relative to the gains from free riding, the presence or absence of anti-social punishment, the presence/structure of communication, group size, and MPCR.
    - Control (no-punishment) efficiency **predicts the ceiling for treatment efficiency**; low baseline efficiency is necessary (but not sufficient) for substantial gains from punishment.
    - **Caveat:** In designs where punishment is poorly targeted, anti-social, too costly, or likely to be applied frequently regardless of behavior, efficiency gains may not materialize, and in some cases, efficiency may decrease compared to control.
    - **Network structure, information/reputation flows, and institutional features** (e.g., endogenously chosen punishment, leader selection process) can strongly moderate the effect direction and magnitude.

**Specific dimension-level guidance:**
- For predictions **outside the canonical PGG design** (e.g., CPR games with collective sanctions, market/trust games, field settings with strong norm internalization), the effect direction and size are less reliable and may be positive, zero, or even negative.

**Use caution**: When the only outcomes available are behavioral (contribution, cooperation), the translation to efficiency is not automatic, especially when punishment costs are high or mis-targeted.

# 6) Design Dimensions Highlighted Across Papers

**Dimensions directly and robustly informed:**
- **player_count, num_rounds, mpcr, all_or_nothing:** Directly specified and manipulated in most high-relevance papers.
- **punishment_cost, punishment_tech:** Heavily analyzed and consistently found to be *key moderators* (e.g., cost-to-impact ratio, completeness and coverage of punishment network, who can punish, cost structure).
- **show_n_rounds, show_other_summaries:** Often included in PGG designs, but typically not central.
- **reward_exists, reward_cost, reward_tech:** Less commonly manipulated; when included, rewards are often found to increase efficiency or be more cost-effective than punishment.

**Indirect, variable, or contextually discussed:**
- **chat:** Most studies are no-chat; those with chat or communication typically find it increases cooperation and can substitute for, or complement, punishment. Only a handful examine the interaction directly.
- **default_contrib:** Framing effects are discussed but not usually the main experimental variable.
- **show_punishment_id:** Discussed occasionally; some studies find anonymity or transparency/identification can moderate anti-social punishment or cooperation rates.

**Sparse or effectively missing:**
- **Details of reward mechanisms, punishment/reward interaction:** Infrequent.
- **Specific feedback structures, multiple feedback channels, higher-order punishment:** Addressed only in a minority of studies.
- **Contextual factors (culture, group identity, endogenous institution choice, etc.):** Sometimes discussed, but not systematically mapped across the prediction dimensions.

# 7) Important Limitations

- **Efficiency vs. Contribution:** Many studies report only behavioral outcomes (contribution rates, compliance), which do not map directly onto efficiency—punishment increases cooperation but often at a cost that can outweigh gains in some contexts.
- **Costliness and Targeting of Punishment:** The positive effect of punishment on efficiency is heavily contingent: high-cost, frequent, anti-social, or mis-targeted punishment can reduce or negate efficiency gains.
- **Generality:** Most robust findings are from canonical lab PGGs; transferability to field settings or non-PGG dilemmas is uncertain. Adjacent domains (e.g., CPR, market, or trust games) may not translate cleanly.
- **Missing dimensions:** Some prediction-relevant design features (e.g., identification of punishers, reward-punishment interplay, complex information structures) are only sparsely addressed.
- **Anti-social Punishment and Heterogeneity:** Studies reporting high levels of anti-social punishment or strong group heterogeneity show unstable or reduced efficiency effects, raising questions about prediction in heterogeneous or real-world groups.
- **Measurement of Control Efficiency:** Accurate efficiency prediction requires precise measurement of *control* efficiency (punishment-off condition), which may not be directly comparable across all studies.
- **Cultural and Institutional Moderators:** Results can be highly context-dependent; the same punishment mechanism may have opposite effects across societies or institutional arrangements.
- **Endogenous Institutional Choice:** In studies where groups can choose institutions, punishment is often under-used, and efficiency gains may not materialize; predictions assuming exogenous imposition of punishment may overstate likely effects.
- **Absence of dynamic or long-horizon games:** Most evidence is from finitely repeated or short PGGs; predictions for longer or indefinite horizons are less secure.

---

**In summary**, the literature set provides strong, directly relevant evidence for predicting the effect of enabling peer punishment on efficiency in canonical PGGs, conditional on game design dimensions and measured control efficiency. However, effects are context-sensitive: the design of the punishment institution, its cost and targeting, baseline efficiency, and potential for anti-social punishment all substantially moderate outcomes. Predictions for more complex, variable, or field-realistic environments require care, as external validity and several moderator dimensions remain only patchily informed.
