# 1) Evidence Base

The current literature set is a mix of **empirical experimental** (lab and field) and **theoretical/game-theoretic** studies, spanning foundational and recent work on cooperation, punishment, and efficiency in public-goods-game-like environments. The spread includes:

- Several **lab experiments** directly using public goods games (PGG) or close variants.
- A large segment of **theoretical and simulation work** on generalized social dilemmas (not always standard PGG).
- Numerous papers reporting on **behavioral outcomes** (contribution rates, punishment behavior) rather than direct efficiency or payoff outcomes.
- A limited subset of studies reporting **direct, quantitative efficiency outcomes under experimentally varied punishment institutions** in actual PGGs.

The set is **broad in mechanism coverage** (including punishment, reward, institution design, reputation, contracts, and spatial/network structure) but **narrower than ideal for the exact task**, as relatively few papers report the downstream effect of enabling peer punishment on efficiency in standard multi-round PGGs parametrized along all 14 design dimensions.

# 2) Task Relevance

_Assessment on three dimensions:_

**a) pgg_or_variant**
- **exact**: A moderate set of empirical and theory papers (e.g., Fehr et al., 2010; Fischer & Nicklisch, 2007; Liu & Guo, 2010) run or model actual PGGs, or games almost mechanically equivalent to PGGs (VCM, resource dilemmas).
- **close**: Many others use close relatives such as repeated Prisoner's Dilemma, resource extraction dilemmas, or networked cooperation—mechanistically similar but not always with the same payoff externalities (e.g., Corriveau, 2012; Janus & Lim, 2009; Webb & Foddy, 2004).
- **adjacent/weak**: Other theoretical or empirical contributions focus on social dilemmas, trust games, or family/organizational analogs, offering conceptual relevance but structural divergence from standard PGG (e.g., Wittman, 2005; Stiff, 2008).

**b) punishment_or_sanctions**
- **exact**: Several empirical studies and models include **explicit costly peer punishment** options in the experimental design (Fehr et al., 2010; Webb & Foddy, 2004).
- **close**: Many theory or simulation papers analyze punishment-like mechanisms, reputation-driven sanctions, or stylized contracts with punishment clauses.
- **adjacent/weak**: A nontrivial share of works mention or discuss punishment abstractly, focus on indirect sanctions, or discuss only the potential for punishment in hypothetical terms (e.g., Stiff, 2008; Nikiforakis, 2010).

**c) efficiency_or_related_payoff_outcome**
- **exact**: A subset of experimental and modeling papers compute or project **group efficiency, welfare, or total payoff** directly (Fehr et al., 2010; Fischer & Nicklisch, 2007; Liu & Guo, 2010).
- **close/adjacent**: Many report **contributions** or **cooperation rates**—behavioral, not directly welfare-based—and infer efficiency effects indirectly, sometimes with strong theorizing but no direct data (e.g., Samid & Suleiman, 2008; Loukopoulos et al., 2006).
- **weak/none**: Several only consider behavioral, neural, or motivational variables; efficiency is not measured or is only conceptual (Cushman, 2011; Kodaka et al., 2012).

# 3) Outcomes Measured In The Literature

**Payoff-related (efficiency, group payoff, welfare):**
- Direct experimental efficiency results in some PGG studies (Fehr et al., 2010; Fischer & Nicklisch, 2007; Webb & Foddy, 2004).
- Theory and simulations measuring expected welfare, system utility, or average fitness in games with sanctioning mechanisms (Janus & Lim, 2009; Liu & Guo, 2010).
- Related, but sometimes less direct, measures: group profit, joint surplus, or population average payoff.

**Non-payoff behavioral outcomes:**
- Most empirical and many theory papers focus on **contribution rates**, **cooperation frequency**, or the **incidence and distribution of punishment** (Loukopoulos et al., 2006; McEvoy, 2012).
- Other proxies: norm compliance, expectation formation, punishment severity, or exclusion rates as indicators of cooperation rather than efficiency.
- Some include **psychological, neural, or motivational measures** (Kodaka et al., 2012; Cushman, 2011).

**Distinction:** Many studies do **not** measure (or only indirectly speak to) efficiency as “group payoff relative to full cooperation”—the core prediction task.

# 4) Main Findings Relevant To Prediction

**Synthesized across the most relevant literature:**

- **Costly Peer Punishment in Standard PGGs:**
  - In canonical short-horizon (10 rounds or fewer) lab PGGs, enabling peer punishment increases cooperation but typically **reduces efficiency** due to the social cost of punishment—payoffs fall relative to control (Fehr et al., 2010). In long-horizon games (e.g., 50 rounds) or with effective reputation/choice mechanisms, efficiency can be higher with punishment.

- **Design Sensitivity of Punishment Effects:**
  - Efficiency effects from enabling punishment in PGGs are **not uniform**; they depend strongly on **number of rounds (CONFIG_numRounds)**, **the ratio of punishment cost to benefit (CONFIG_punishmentCost/CONFIG_mpcr)**, and the **presence of reputation/endogenous institution choice** (Fehr et al., 2010; Liu & Guo, 2010).

- **Structure of Punishment:**
  - Sanctioning systems' design (targeted vs. shared, voluntary vs. committed, credible vs. non-credible) shapes whether efficiency increases or decreases. For example, targeted sanctions may better preserve resources, but shared punishment yields higher group profit (Webb & Foddy, 2004).

- **Theoretical Models:**
  - Theoretical and simulation models overwhelmingly show that **sufficiently strong, credible, and not excessively costly punishment can stabilize high cooperation—thus, higher efficiency—especially in infinitely repeated or long-term games** (Corriveau, 2012; Janus & Lim, 2009; Aramendia, 2006; Evans & Thomas, 2001). But these results require patient players and observable actions.

- **Cost Thresholds:**
  - If punishment is too costly relative to the potential cooperative benefit, it may not improve, or may even lower, efficiency (Liu & Guo, 2010; Heller & Sieberg, 2008).

- **Ineffective or Non-credible Punishment:**
  - Voluntary or non-committed punishment, or coercion that's too costly, is often ineffective for efficiency improvement (McEvoy, 2012; Samid & Suleiman, 2008).

- **Behavioral Spillovers and Context:**
  - Some evidence suggests **intermittent punishment can increase cooperation** even without universally targeting all defectors, but the efficiency effect is likely positive only if the cost is not prohibitive (Loukopoulos et al., 2006).

- **Multi-dimensional Moderators:**
  - Moderators include **group size (player_count)**, reputation, transparency of punishment (show_punishment_id), and information sharing (show_other_summaries), but most are supported by theory or by non-payoff behavioral outcomes more than by direct efficiency data.

# 5) Prediction Guidance

**How should these findings inform the prediction of efficiency with punishment enabled, given game design and control game efficiency?**

- **Efficiency impact is non-uniform and design-sensitive.**
  - In *short, standard PGGs* (few rounds), peer punishment likely **reduces efficiency** relative to control (often due to costly punishment “overshoot”) (Fehr et al., 2010).
  - In *longer games* or with additional institution/reputation mechanisms, peer punishment can **increase efficiency**, sustaining both high cooperation and higher net payoffs (Fehr et al., 2010; Corriveau, 2012).

- **Key prediction moderators:**
  - **num_rounds:** More rounds make punishment more likely to increase efficiency.
  - **punishment_cost vs. group benefit:** Low-to-moderate cost, highly effective punishment is beneficial; too costly and it backfires (Fehr et al., 2010; Liu & Guo, 2010).
  - **punishment_tech:** Mechanisms enabling credible, committed, or “draconian” punishment support efficient outcomes (Evans & Thomas, 2001).
  - **endogenous choice/reputation:** If the design includes endogenous institution choice or reputation, treatment efficiency is more likely to rise (Fehr et al., 2010).

- **Control efficiency as a baseline:**
  - Where **control game efficiency is already high**, punishment may add little or even reduce efficiency by introducing relatively unnecessary costs.
  - Where **control efficiency is low**, well-designed punishment mechanisms (not too costly, credible, effective) are more likely to raise efficiency.

- **Design feature gaps:**
  - Some dimensions (e.g., chat, showNRounds, defaultContrib) are rarely addressed; guidance for their role in moderating treatment efficiency is weak or absent.

- **Contextual uncertainties:**
  - Many studies rely on theoretical rather than empirical efficiency, or interpret cooperative behavior as a proxy, so actual effect sizes are difficult to forecast. Ambiguity exists, especially in "borderline" conditions (e.g., moderate-length games, or moderate-cost punishment).

# 6) Design Dimensions Highlighted Across Papers

**Directly informed by the literature (i.e., supported by empirical or theoretical models with efficiency outcomes):**
- **player_count:** Group size considered in most models and experiments.
- **num_rounds:** Strongly supported as a moderator of punishment's efficiency effect (Fehr et al., 2010; Corriveau, 2012).
- **all_or_nothing:** Present in several theoretical models and experiments.
- **mpcr:** Central to payoff scaling and the benefit/cost ratio.
- **punishment_cost:** The costliness threshold is a critical moderator.
- **punishment_tech:** Varied forms of punishment (targeted, collective, public, private, mechanism rules) receive attention.

**Indirectly informed or contextually discussed:**
- **show_other_summaries, show_n_rounds, show_punishment_id:** These aspects arise in information-transmission and observability models, but empirical payoff data by these specific manipulations are sparse.
- **reward_exists, reward_cost, reward_tech:** Several models/theories compare reward to punishment or examine their interaction, but direct efficiency data in PGGs is rarer.
- **chat:** Occasional presence, but rarely isolated as a moderator of efficiency under punishment.

**Effectively missing or very weakly represented:**
- **default_contrib:** Opt-in/opt-out framing is almost never explored with efficiency as the dependent variable.
- **showNRounds & chat (as explicit moderators):** Scant attention to their marginal effect on efficiency with punishment enabled.

# 7) Important Limitations

- **Few papers report direct, quantitative efficiency outcomes for PGGs with peer punishment enabled and control-comparable baselines.** Most provide theory or behavioral proxies.
- **Empirical evidence is concentrated in a handful of studies, especially Fehr et al. (2010);** many other findings are conditioned on PGG-variants or adjacent games.
- **Parameter coverage is incomplete—many design features are not systematically varied or reported** (e.g., chat, framing, visibility dimensions).
- **Efficiency effects are sometimes inferred from behavioral or theoretical indicators rather than direct measurement,** and the mapping from cooperation/contribution to efficiency is not always transparent or monotonic.
- **Ambiguity and disagreement persist:** Even among empirical PGG studies, the effect of punishment varies by time horizon and institution structure; amongst theory papers, results often hinge on repeated, infinite-horizon play and strong rationality assumptions.
- **External validity is limited:** Many design choices (e.g., endogenous institution choice, complex punish/reward mechanisms) are not standard in all PGGs. Extrapolation across settings is nontrivial.
- **Behavioral outcomes (e.g., contribution rates, cooperation) cannot be assumed equivalent to efficiency,** especially when punishment is costly.

---

**Summary:**  
A rich body of theory and some empirical studies suggest that enabling peer punishment can, under some conditions, increase efficiency in PGG-like environments—but this is highly conditional on game duration, punishment cost and design, and initial efficiency levels. In short, punishment is not a universal fix: it can both help or hurt efficiency, and prediction must attend to detailed game design dimensions, particularly **num_rounds, punishment_cost, punishment_tech, and mpcr**. For other dimensions, guidance from the literature is weak, absent, or only behavioral. Overall, while the literature provides valuable qualitative and some quantitative clues for prediction, substantial gaps and contingencies remain.
