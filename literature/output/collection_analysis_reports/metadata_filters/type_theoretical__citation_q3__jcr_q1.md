# 1) Evidence Base

The evidence base is extremely broad, consisting entirely of theoretical studies (n=199), with no primary empirical or laboratory data. Every paper is either an analytical model, an agent-based simulation, a literature review, or a conceptual/theoretical argument. Nearly all studies are related to social dilemmas, public goods games (PGGs), common-pool resources, or analogous multi-agent environments, but empirical measurement of efficiency in controlled settings is absent.

A substantial portion of the paper set focuses directly on public goods games and efficiency or related payoff-based outcomes, although many studies use adjacent or variant frameworks (e.g., snowdrift games, Prisoner's Dilemmas, or innovation race games). The set covers a wide range of incentive mechanisms: peer and institutional punishment, social exclusion, reward, reputation, and combined or hybrid schemes.

Behavioral outcome measures (e.g., cooperation rate) are frequent, but roughly 30–40% of the highly relevant studies report or analyze efficiency, total group payoff, or welfare as a central outcome. The prediction context (enabling peer punishment and its impact on efficiency) is well represented at the theoretical level, although empirical calibration, direct effect size estimates, and systematic parametric mapping are largely missing.

# 2) Task Relevance

**PGG or Variant:**  
- *Exact:* The core of the evidence base is theoretical models either of standard PGGs or very closely related variants (e.g., threshold PGGs, spatial/networked PGGs, optional participation PGGs). Many papers are limited to adjacent games (e.g., public goods–like resource games, PDGs with group structures).
- *Close or Adjacent:* A smaller but sizable fraction treats closely related social dilemmas (dynamic commons, innovation races, repeated PDGs). Some reviews discuss experimental economics more broadly, while a number focus on norm enforcement, partner choice, and reputation systems in adjacent settings.
- *Weak or None:* A smaller number of papers discuss only context or mechanisms distantly related to PGGs.

**Punishment or Sanctions:**  
- *Exact:* The majority of central papers directly model punishment or sanctions—peer, institutional, centralized/decentralized, exclusion, or sanctioning via reputation mechanisms.
- *Close or Adjacent:* A considerable group uses analogues of punishment (e.g., exclusion, ostracism, reciprocal withholding, shunning).
- *Weak or None:* A subset studies reward only, partner choice, or internal preference evolution without external punishment.

**Efficiency or Related Payoff Outcomes:**  
- *Exact/Close:* Many studies report efficiency explicitly—as mean group payoff, welfare, or payoff ratios compared to the fully cooperative outcome.
- *Adjacent:* A substantial number infer efficiency from average payoff, resource stock, or equilibrium welfare, but main outcomes are often labeled as cooperation rates.
- *Weak/None:* Papers focused on behavioral outcomes (cooperation frequency, compliance), mechanism explanations, or evolutionary/strategy distributions, without linking to group payoff/welfare, are frequent.

# 3) Outcomes Measured in the Literature

**Payoff-related Outcomes (directly informing efficiency):**
- Efficiency (group payoff as a fraction of maximum, or welfare)
- Mean/total group payoff or welfare
- Resource stock relative to optimum (in resource models)
- Probabilities of convergence to efficient/inefficient equilibria (in stochastic models)

**Non-Payoff Behavioral Outcomes (less directly informing efficiency):**
- Contribution rates, cooperation rates, punishment and reward frequencies
- Prevalence of strategies (cooperation, defection, punishment, exclusion, etc.)
- Norm compliance and stability
- Social norm/conformity dynamics
- Evolutionary stability or prevalence of "punishing" strategies

**Importantly:** Many central papers, while discussing payoff functions and sometimes reporting average payoff, present cooperation rates as the main outcome and only infer efficiency. Cross-mapping from behavior to efficiency often requires caution, as high cooperation does not guarantee high efficiency if punishment is costly or misapplied.

# 4) Main Findings Relevant To Prediction

**Synthesis of Empirical Support, Theory, and Mechanism Arguments:**

- **Punishment generally increases efficiency and group welfare in standard PGGs—provided punishment is effective (high impact for low cost) and not undermined by costly side effects, antisocial punishment, or corruption** [(Li et al., 2022); (Salahshour, 2021); (Vasconcelos et al., 2015); (Gao et al., 2020); (Ohdaira, 2022); (Wang et al., 2024)].
    - *Direct theoretical support*: Mathematical models and phase diagrams show clear threshold effects—punishment must cross a cost-effectiveness threshold to meaningfully raise efficiency above control [e.g., (Wang et al., 2024); (Gao et al., 2020)].
    - *Parameters driving positive effects*: High MPCR, moderate/low punishment cost, high punishment impact, small/moderate group size, structured/local networks, observability of punishment, and optimal calibration (not too harsh, not too mild) all enhance the benefit.

- **Contextual and structural moderators can reverse, diminish, or eliminate positive effects:**
    - *Corruption and antisocial punishment*: When institutional punishment can be corrupted, efficiency falls and may cycle between high and low states [(Lee et al., 2019); (Abdallah et al., 2014)]. Antisocial punishment can crowd out prosocial efficacy, especially if punishment is too cheap or not observable as prosocial [(Salahshour, 2021); (García & Traulsen, 2019)].
    - *Second-order free riding*: Without mechanisms to compensate punishers or support institution maintenance, costly punishment may not increase, or may even reduce, efficiency [(Ye et al., 2011); (Okada et al., 2015)].
    - *Mutation structure and learning dynamics*: In evolutionary models, structure of strategy mutation, population updating, and attention to payoff history can cause punishment's effect on efficiency to be highly sensitive or even reversed [(García & Traulsen, 2012)].
    - *Network structure*: Structured (regular, spatial, or networked) populations often enhance punishment's benefit by maintaining clusters of cooperation and punishment; well-mixed populations make efficient enforcement harder [(Wang et al., 2024); (Vasconcelos et al., 2015)].

- **Institutional punishment (e.g., pool or tax-based) can outperform peer punishment on efficiency if corruption is prevented and monitoring is effective** [(Sun et al., 2023); (Dong et al., 2019); (Powers & Lehmann, 2013)]. However, reward-only or hybrid protocols may sometimes achieve higher efficiency, especially in noisy or error-prone environments [(Dong et al., 2019); (Wu et al., 2022); (Han et al., 2024)].

- **Design of punishment matters:** Adaptive, probabilistic, graded, or state-dependent punishment mechanisms generally yield higher efficiency than static or overly severe schemes [(Ohdaira, 2022); (Quan et al., 2023); (Huang et al., 2018); (Huang, F. et al., 2018)].

- **Reward and punishment interact nontrivially:** Rewards often achieve similar or higher efficiency than punishment when errors or retaliation risks are present; mixed mechanisms must be optimally calibrated for cost-effectiveness to avoid waste [(Dong et al., 2019); (Okada et al., 2015); (Han et al., 2021)].

- **Information structure (observability, reputation, knowledge of rounds) is critical:** Punishment is more likely to increase efficiency if outcomes and actions are visible, punishment is reputationally tracked, and roles or intentions are clear [(García & Traulsen, 2019); (Podder et al., 2021); (Bhaskar & Thomas, 2019)].

- **Baseline efficiency (control condition) is a key moderator:** Where baseline efficiency is high (e.g., because of strong norms or high trust), punishment can "crowd out" voluntary cooperation and reduce efficiency; where baseline efficiency is low (i.e., much free-riding), punishment is more likely to yield strong efficiency gains [(van der Weele, 2012)].

# 5) Prediction Guidance

**How to Use This Literature for Prediction:**

- **If control efficiency is low** (free-riding is common), and punishment is enabled with moderate cost-effectiveness, *theoretical models consistently predict a substantial increase in treatment efficiency*—i.e., the average group payoff in the punishment-enabled condition will approach, but usually not reach, full-cooperation levels, with the relative gain being greater for higher MPCRs, modest group size, and effective sanctioning.

- **Marginal efficacy declines with poor punishment parameters:**
    - *If punishment is costly and/or weak (impact/cost ratio is low):* Efficiency gains are minimal or negative.
    - *If anti-social punishment is possible or corruption likely:* Efficiency may fall relative to control, and enabling punishment may worsen payoffs.
    - *If the group is very large, or information is poor:* Peer punishment loses effectiveness unless institutional arrangements (centralized, collective or third-party enforcement) are available.

- **Design dimensions act as strong moderators:**  
    - *player_count*: Smaller groups benefit more from peer punishment; institutional punishment is needed in larger groups for effectiveness.
    - *num_rounds*: Repeated interaction increases the efficacy of punishment via threat of future consequences.
    - *mpcr*: Higher returns to cooperation make punishment more beneficial.
    - *punishment_cost & punishment_tech*: Lower cost and higher impact to defectors is optimal; calibration matters.
    - *chat, reward_exists, show_other_summaries, show_punishment_id*: Observability and reputational feedback enable punishment to have stronger (and more positive) effects.
    - *all_or_nothing, default_contrib*: Less well addressed, but binary contributions or default framing can influence cooperation and, thus, the marginal benefit of punishment.

- **If the system allows adaptive, graded, or reputation-based punishment:**  
  Efficiency is highest, with models suggesting nearly full cooperative efficiency is possible under optimal conditions; fixed or harsh schemes risk over-punishment and lower welfare.

- **If reward or hybrid reward-punishment is available:**  
  Efficiency may be maximized with adaptive, hybrid approaches—pure punishment is not always optimal, especially in noisy or miscoordination-prone environments.

**Empirically, due to the lack of direct laboratory or field estimates in this paper set, these predictions should be interpreted as qualitative or parametric bounds rather than precise effect sizes or ratios.**

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Across Multiple Papers:**
- *player_count*: Group size strongly moderates both punishment effectiveness and efficiency outcomes.
- *num_rounds*: Repeated vs. one-shot structure is almost always explicit in analysis.
- *mpcr*: The marginal return is a key (and often mathematically explicit) moderator.
- *punishment_cost & punishment_tech*: These are typically varied systematically; the ratio of cost to impact is central to most models.
- *reward_exists, reward_cost, reward_tech*: Comparative analyses of punishment and reward appear in many papers.
- *show_punishment_id, show_other_summaries*: Observability is mentioned as a crucial factor in several studies.
- *punishment_exists, reward_exists*: Core to most model manipulations.

**Indirectly or Contextually Addressed:**
- *all_or_nothing*: A number of models use binary vs continuous contributions; less often is the framing dimension (default_contrib) varied.
- *chat*: Communication is often discussed as enhancing cooperation, but less often as an explicit variable in mathematical modeling.
- *default_contrib*: Only rarely directly analyzed.
- *show_n_rounds*: Sometimes referenced in discussions of horizon effects or observability.
- *show_other_summaries*: Often part of the information structure relevant for observability of reputation/punishment, but not always systematically manipulated.

**Effectively Missing or Seldom Treated Specifically:**
- Fine-grained framing dimensions (e.g., default contribution mode), nuanced chat/protocol details, specific feedback modalities, or laboratory artifact effects are rarely incorporated.  
- No empirical parameterization or mapping to specific experimental settings for effect sizes or direct quantitative predictions.

# 7) Important Limitations

- **Lack of empirical measurement:** All included studies are theoretical or simulation-based; there are no direct empirical estimates of efficiency outcomes from actual laboratory or field PGGs with punishment manipulation.
- **Outcome mapping:** Many findings rely on behavioral outcomes (cooperation rate, prevalence) and only infer efficiency or payoff. Costly punishment can, in principle, increase cooperation but reduce or fail to increase group payoff if not calibrated correctly.
- **Transferability from adjacent games:** Several central findings are derived from adjacent frameworks (e.g., repeated PDGs, resource games, innovation races, indirect reciprocity models), requiring caution in direct transfer to standard PGGs.
- **Dependence on model assumptions:** The predicted effect of punishment is often highly dependent on population structure, mutation kernel, learning/reinforcement model, and initial conditions, leading to context-sensitive or non-robust results.
- **Moderator variables not always explicit:** While key design dimensions (group size, MPCR, punishment cost/effectiveness) are often directly analyzed, other potentially important dimensions (chat, framing, feedback, institutional context) are indirect or missing.
- **Ambiguity and divergence in mechanism effects:**  
    - In resource-limited, large, or corruption-prone environments, punishment can reduce efficiency.
    - Reward or adaptive hybrid mechanisms may outperform punishment.
    - Second-order free rider problems, anti-social punishment, and over-regulation risks are highlighted as settings where enabling punishment can backfire.
- **No direct quantitative mapping:** No studies provide empirical calibration or effect size estimates to enable direct prediction of treatment efficiency as a function of control efficiency and design dimensions.

---

**Conclusion:**  
The literature base offers strong and nuanced *theoretical* guidance for predicting the effect of enabling punishment on efficiency in PGG-like environments as a function of game design dimensions. It supports directional and moderator-sensitive prediction, but quantitative precision and empirical calibration are lacking. The absence of empirical or laboratory data, and the need to distinguish behavioral cooperation from actual efficiency improvements, are important constraints; as such, model-based, dimension-conditioned qualitative forecasts are strongly supported, but numerical predictions or universal claims are not warranted based solely on this paper set.
