# 1) Evidence Base

The paper set comprises **75 studies**, with a strong mix of theoretical and empirical work (laboratory/field experiments and agent-based modeling). The coverage of **public goods games (PGG) and close variants is broad**, including standard linear PGGs, variants (such as common-pool resource games), and adjacent repeated social dilemmas. Both **institutional and peer punishment** are represented, as well as reward, reputation, communication (chat/gossip), and information structure.

**Empirical studies** frequently use laboratory PGGs or field experiments with payoff and/or behavior as outcomes. **Theoretical contributions** dominate in breadth, offering simulation or analytic results with parameter sweeps across key dimensions (e.g., player count, punishment cost, marginal per capita return, and punishment effectiveness). The mix provides **rich, multidimensional evidence**—but detailed, directly comparable experimental payoff-based efficiency results remain limited. Much of the literature focuses on **cooperation/contribution behavior** rather than total group efficiency.

## Breadth for the Prediction Task

- **Relevance to PGGs and their variants:** Broad and deep.
- **Relevance to peer punishment and closely related sanctions:** Strong for both peer and institutional punishment, with many papers analyzing the effect of punishment mechanisms.
- **Relevance to efficiency or related payoff outcomes:** Reasonable, though behavioral measures (e.g., cooperation rate, norm compliance) outnumber direct efficiency/payoff reports.

# 2) Task Relevance

### `pgg_or_variant`  
- **Exact:** The majority directly study PGGs or continuous/discrete PGG variants (Dong et al., 2019; Jiao et al., 2020; Wang & Lv, 2019; etc.).
- **Close:** Several papers analyze threshold PGGs, common-pool resource games, or closely related social dilemmas—these are structurally very similar but may include resource dynamics or opt-out (Wegmann & Musshoff, 2019; Chen & Szolnoki, 2018).
- **Adjacent / Weak:** Some focus on adjacent games (e.g., Prisoner’s Dilemma, Dictator Game, or mutual-aid games) and thus inform baseline cooperation or payoff dynamics but not the effect of punishment in actual PGGs.

### `punishment_or_sanctions`
- **Exact:** Many papers explicitly manipulate or model peer or institutional punishment within PGGs, including cost, magnitude, targeting, and anti-social aspects.
- **Close:** Some study closely related sanctioning systems (e.g., exclusion, policing, exploitation-based sanctions, or opt-out reputational penalties).
- **Adjacent / Weak:** Several address only reputation-based or information-based 'soft sanctions', or discuss punishment in the abstract, outside the context of game implementation.

### `efficiency_or_related_payoff_outcome`
- **Exact:** A strong subset (primarily theory and some field experiments) analyze total group payoff, average efficiency, or social welfare (Dong et al., 2019; Jiao et al., 2020; Wang & Lv, 2019; Wegmann & Musshoff, 2019).
- **Close/Adjacent:** Many empirical studies and reviews report behavioral cooperation, norm compliance, or punishment frequency, which are only indirect proxies for efficiency.
- **Weak/None:** Several papers provide only neural, social, or mechanistic insights, or report individual behavior without mapping to group payoff.

### **Summary**
- The **task relevance is highest** for studies with: (a) direct experimental or theoretical analysis of punishment-enabled PGGs, and (b) efficiency or group payoff as the primary outcome.
- For **downstream prediction of treatment efficiency**, the directly relevant evidence base is concentrated but surrounded by a larger set of contextually or mechanistically relevant work.

# 3) Outcomes Measured In The Literature

**Payoff-based outcomes:**
- **Efficiency:** Ratio of achieved group payoff to full-cooperation optimum; reported in a minority of papers but central in theory work and some field studies.
- **Total (group) payoff, social welfare, surplus, earnings:** Various forms, sometimes as explicit ratios/percentages (e.g., Wegmann & Musshoff, 2019).
- **Resource sustainability or social optimum payoff:** In common-pool resource (CPR) and threshold public goods variants.

**Non-payoff behavioral outcomes:**  
(Important moderators but must not be conflated with efficiency.)
- **Contribution/cooperation rates, frequency of full contribution, norm compliance:** Most common measure, especially in empirical studies.
- **Punishment frequency and intensity, distribution of punishment types.**
- **Normative judgments, social information use, reputation, learning strategies.**
- **Gossip/trust, information transmission, social bonding, neural response, and other behavioral proxies for collective outcomes.**

**Observation:**
- While improvement in cooperation typically suggests higher efficiency, **payoff gains are often offset by punishment costs or antisocial punishment**, so direct efficiency outcomes are not trivially inferred from behavioral data.

# 4) Main Findings Relevant To Prediction

## Synthesis Across Papers

**a) Punishment’s Efficiency Effects Depend Heavily on Cost, Effectiveness, and Context**
- **Punishment can increase efficiency** *if* the cost is low relative to the fine imposed, and defectors can be selectively and reliably targeted (Wang & Lv, 2019; Huang et al., 2018; Fang et al., 2020).
- **Punishment can reduce efficiency** if it is costly, indiscriminately applied, or if antisocial punishment is common (Burton-Chellew & Guérin, 2021; Fehr & Schurtenberger, 2018).
- **Effect is contingent on population composition** (Greenwood et al., 2018): a sufficient proportion of willing punishers is needed to generate positive efficiency effects.

**b) Efficiency Gains Are Strongest With Institutional Reward, Normative Constraints, or Hybrid Mechanisms**
- **Institutional reward** generally outperforms institutional punishment in terms of efficiency, especially with bounded rationality and error (Dong et al., 2019).
- **Combined systems** of reward and punishment can optimize efficiency at intermediate incentive levels, but punishment alone is rarely robust, particularly in human-error-prone environments.
- **Reputation and information mechanisms** can substitute for or strengthen the effect of punishment, and the *combination* of reputation and punishment is best for sustaining high efficiency (Podder et al., 2021; Fehr & Schurtenberger, 2018).

**c) Contextual Moderators and Limitations**
- **Resource context matters:** In CPR games, ecological/resource renewal rates can *override* the benefits of punishment—strong enforcement cannot prevent collapse if resources recover slowly (Chen & Szolnoki, 2018).
- **Corruption, anti-social punishment, social norms:** Bribery or antisocial punishment undermines efficiency gains from punishment; efficacy improves with corruption control and norm-constraining institutions (Huang et al., 2018; Fehr & Schurtenberger, 2018).
- **Effectiveness depends on monitoring and social structure:** Sanction systems that minimize monitoring cost and increase detection efficacy produce higher efficiency (Nakamaru et al., 2018).

**d) Empirical-Experimental Evidence**
- **Laboratory PGGs** frequently find that punishment increases cooperation but not always efficiency; the costs of punishment often outweigh the cooperative benefit, especially with high punishment frequency and low MPCR (Burton-Chellew & Guérin, 2021).
- **Field experiments** with externally imposed punishment (Wegmann & Musshoff, 2019) show efficiency gains, especially when existing efficiency is below the social optimum.
- **Probabilistic or graduated punishment** can outperform always-on punishment—lower execution rates or adaptive fine sizing can sustain cooperation and efficiency even with high punishment costs (Jiao et al., 2020; Couto et al., 2020).

# 5) Prediction Guidance

**Predicting treatment (punishment-enabled) efficiency given game dimensions and control efficiency:**

- **Positive efficiency effect is most likely:**
    - When **punishment cost is low relative to impact/fine**, and punishment is credible and targeted.
    - When **reward (especially institutional reward)** or hybrid mechanisms are available (strong support: Dong et al., 2019).
    - When **corruption control** or **normative constraints** reduce antisocial punishment (Fehr & Schurtenberger, 2018; Huang et al., 2018).
    - In environments with **moderate to high control efficiency**, limited antisocial punishment, and high MPCR.

- **Negative or null efficiency effect likely:**
    - When **punishment is costly, frequent, antisocial**, or monitoring is ineffective (Burton-Chellew & Guérin, 2021; Fehr & Schurtenberger, 2018; Fang et al., 2020).
    - When **cooperation rates cannot be raised enough by punishment to offset costs**, or **non-punishable defectors are present** (Burton-Chellew & Guérin, 2021).
    - In contexts where **resource renewal is slow** or ecological parameters limit the benefit of cooperation (Chen & Szolnoki, 2018).

- **Conditional/mixed outcomes:**
    - The effect of punishment is **not universal**—it depends on the interaction of design parameters: player count, MPCR, cost/magnitude of punishment, presence of communication or reputation, and institutional control (Wang & Lv, 2019; Greenwood et al., 2018).
    - **Probabilistic/graduated punishment**: Enabling punishment with moderate probability or adaptive fine sizing can maximize efficiency, especially at high per-punishment cost (Jiao et al., 2020; Couto et al., 2020).

- **Empirical patterns:** 
    - Where direct efficiency data is available, **punishment increases group efficiency in CPR and some institutional PGG field studies** (Wegmann & Musshoff, 2019).
    - In many laboratory PGGs, **punishment increases cooperation but is "destructive" for efficiency** (Burton-Chellew & Guérin, 2021).

### Use of Control Efficiency

- If **control efficiency is already low**, adding punishment may not increase efficiency unless punishment is both effective and low-cost (Dong et al., 2019).
- **Efficiency gains are most predictable when control efficiency is moderate and the game design facilitates norm enforcement and minimizes antisocial or mis-targeted punishment.**

# 6) Design Dimensions Highlighted Across Papers

### **Directly Informed**

- **player_count**: Explicitly modeled in most theory work; group size interacts with punishment effectiveness and cooperation stability (Wang & Lv, 2019; Greenwood et al., 2018; Murase & Baek, 2021).
- **num_rounds**: Repetition enables contingent strategies and the emergence of stable cooperation, often increasing the benefit of punishment or norm enforcement (Murase & Baek, 2021; Greenwood et al., 2018).
- **all_or_nothing**: Both continuous and all-or-nothing contribution structures are modeled; cost-benefit analysis applies in both (Wang & Lv, 2019; Fang et al., 2020).
- **mpcr**: A central parameter; higher MPCR generally increases cooperation and the efficiency effect of punishment (Wang & Lv, 2019; Greenwood et al., 2018; Jiao et al., 2020).
- **punishment_cost**, **punishment_tech**: Cost to punisher and punishment effectiveness (magnitude/fine size) frequently manipulated and shown to moderate efficiency effects (Wang & Lv, 2019; Huang et al., 2018; Fang et al., 2020).
- **reward_exists/configuration**: Important moderator in studies that compare reward and punishment (Dong et al., 2019; Jiao et al., 2020).
- **show_other_summaries**: Sometimes used to model information availability and feedback, affecting cooperation/punishment dynamics.

### **Indirectly Informed**

- **chat**: Analyzed indirectly; communication substitutes or enhances punishment (Jolly & Chang, 2021), and in some studies, the effect of enabling chat is distinguished from punishment/reward (Wegmann & Musshoff, 2019).
- **default_contrib**: Framing as opt-in versus opt-out is rarely the focus but may be part of experimental design (Micheli et al., 2021).
- **show_n_rounds**: Rounds information sometimes manipulated; more repetition generally supports stronger punishment/cooperation strategies.
- **show_punishment_id**: Visibility of punisher identity not a primary variable except where anonymity versus transparency is discussed (Fehr & Schurtenberger, 2018; Podder et al., 2021).

### **Contextually Discussed**

- **reward_cost/reward_tech**: Present in some studies focused mainly on reward versus punishment efficiency (Dong et al., 2019).
- **show_other_summaries**, **show_punishment_id**: Mostly discussed as contextual moderators relating to observability, but not systematically manipulated.

### **Effectively Missing**

- **Some dimensions, such as default_contrib or intricacies of technology (technology of implementing punishment or reward), are generally not deeply modeled outside of studies focusing on specific mechanisms.**

# 7) Important Limitations

- **Direct experimental evidence of efficiency changes due to enabling punishment is limited**: Many studies provide only theoretical predictions or measure behavioral cooperation.
- **Distinction between increased cooperation and increased efficiency is critical**: Many studies show cooperation gains, but the cost of punishment or presence of antisocial punishment often reduces or even negates efficiency gains.
- **Context-specific moderators are strong**: Ecological parameters (resource dynamics), social norms, possibility of corruption, and the presence of alternative enforcement mechanisms (e.g., reputation, chat) can override basic game design predictors.
- **Heterogeneity in outcome measures** makes meta-analytic integration challenging; some studies report efficiency as percent of optimal, others as total earnings or social welfare.
- **Parameter interaction effects** are often only theorized, not systematically empirically validated (e.g., how punishment cost interacts with MPCR, or the effect of group size in high cost/low cost punishment regimes).
- **Reward and hybrid incentive systems are understudied relative to punishment**; the evidence suggests reward is more robustly efficiency-enhancing (Dong et al., 2019; Jiao et al., 2020), but predictive models are less developed.
- **Limited coverage for design dimensions such as chat, default contribution framing, visibility of punishment identity, and probabilistic versus deterministic punishment execution** in relation to their impact on efficiency.
- **Non-payoff behavioral outcomes (contribution rate, norm compliance)** vastly outnumber directly comparable efficiency measurements.

---

**In summary:**  
This paper set provides a strong theoretical and moderate empirical foundation for predicting how enabling punishment impacts efficiency in PGG-like environments. The best-supported guidance is: only expect efficiency gains when punishment is low-cost, highly effective, normatively constrained, and not dominated by antisocial or frequent erroneous punishment. When these conditions are not met, null, negative, or highly context-dependent efficiency effects of punishment should be expected—even when behavioral cooperation increases. For robust prediction, integration of multiple design dimensions is essential, and wherever possible, explicit efficiency baselines from closely matched control conditions should be used.
