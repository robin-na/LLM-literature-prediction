# 1) Evidence Base

**Mix of Paper Types:**  
The literature set is large (432 papers) and includes both empirical (lab and field experiments) and theoretical contributions. There is a strong emphasis on formal models, evolutionary simulations, and agent-based modeling, complemented by many controlled laboratory and some naturalistic/field studies. The papers span a spectrum from canonical public goods games (PGGs) to close or adjacent dilemmas (common-pool resources, indirect reciprocity, collective-risk, and trust games). Several papers synthesize across studies or provide conceptual reviews.

**Coverage for Prediction Task:**  
Regarding the prediction task—estimating the change in group efficiency (payoff relative to cooperation optimum) when enabling punishment in a PGG-like environment given game design dimensions and control efficiency—the evidence base is:  
- **Broad** on (1) theoretical mechanisms, (2) qualitative effects of punishment, (3) boundary conditions, and (4) moderators such as group size, punishment cost/efficacy, and social structure.
- **Empirical evidence** (measuring efficiency or closely related payoffs) is widespread for standard lab PGGs but sparser for field settings and for non-standard designs.
- **Less coverage** on rare or complex design dimensions (e.g., chat/communication, peer identity revelation, nuanced reputation mechanisms, cultural/psychological moderators) and for hybrid or field-institutional environments.
- Papers closely match standard PGGs with punishment, but evidence becomes more qualitative/indirect as the context moves toward CPR, indirect reciprocity, or reputation-based systems.

# 2) Task Relevance

### a. `pgg_or_variant`  
- **Exact Relevance:** The core of the literature (theory and experiments) is on standard linear PGGs with continuous or binary contributions. Variants (e.g., weakest-link, threshold, CPR) and related games are also represented.
- **Close/Adjacent:** Many theory papers generalize to related social dilemmas or trust/reciprocity games. Some field/complex system papers use resource management games or indirect reciprocity structures, which are close but not identical.
- **Weak/None:** Rare for this set, except in meta-analyses or pure conceptual pieces without a game context.

### b. `punishment_or_sanctions`  
- **Exact Relevance:** Most papers manipulate or model explicit punishment (peer/institutional, costly, pool/peer, or social exclusion) as a treatment variable. Some compare to reward or communication.
- **Close/Adjacent:** A subset study reputational or indirect (e.g., partner switching, gossip, ostracism) or hybrid mechanisms.
- **Weak/None:** A significant tail of papers focus on baseline (control) environments without punishment, useful for modeling control efficiency but not for punishment effect estimation.

### c. `efficiency_or_related_payoff_outcome`  
- **Exact/Close:** Numerous papers directly report group efficiency, average payoffs, welfare/surplus, or explicit earnings ratios (critical for prediction). Several models give parameterized formulas for efficiency with and without punishment under various regimes.
- **Adjacency/Weak:** Many more discuss behavioral proxies (contribution, cooperation, norm compliance) with only indirect or no mapping to efficiency.
- **None:** Some papers focus solely on neural, motivational, or evolutionary trait outcomes without reference to payoffs or efficiency.

# 3) Outcomes Measured In The Literature

**Payoff-based outcomes:**  
- *Directly Reported:* Group efficiency (payoff ratio to optimum), total/group earnings, welfare, proportion of maximum possible group payoff; especially in standard lab PGG and some field/CPR studies and evolutionary models.
- *Closely Related:* Loss avoidance (collective-risk dilemmas), resource sustainability, surplus over baseline, or direct comparison of group welfare under different institutions.
- *Theoretical Models:* Provide explicit efficiency (mean fitness) formulas as a function of game parameters and punishment design.

**Behavioral/non-payoff outcomes:**  
- *Dominant in many papers.* These include cooperation/contribution rates, frequency/type of punishment, norm compliance, retaliation, network topology changes, or evolutionary stability of strategies (not the same as payoff).
- *Contextual moderators* such as psychological measures, emotional responses, belief dynamics, and communication patterns are frequently analyzed as mechanisms or boundary conditions but do not substitute for payoff outcomes.

**Distinction:**  
- Where inferences about efficiency are drawn from behavioral data, papers either **explicitly state** the mapping or caution that contribution ≠ efficiency (e.g., contexts where cost of punishment outweighs gains, or where antisocial punishment is prevalent).

# 4) Main Findings Relevant To Prediction

**Empirical patterns:**
- **Enabling punishment often increases efficiency** in standard lab PGGs at moderate group sizes, punishment costs, and rounds, but key *exceptions* are robust:
    - *High punishment frequency/cost* can cause net efficiency loss, even if cooperation rises (Egas & Riedl, 2008; Burton-Chellew & Guérin, 2021).
    - *Antisocial punishment* (punishing cooperators or in-group bias) can reduce or reverse efficiency gains (Fatas & Mateu, 2015; Rand et al., 2010; Hauser et al., 2014; Herrmann et al., 2008, cited).
    - *Retaliation* or opportunities for counter-punishment can nullify the efficiency benefit of punishment or drive negative efficiency (Janssen & Bushman, 2008; Wolff, 2012).
    - *Communication* (chat, gossip, reputation signals) can substitute for punishment and in some cases yield equal or higher efficiency with lower cost (Andrighetto et al., 2016; Milinski, 2016).
    - *Social exclusion/ostracism* is often more efficient than costly punishment, especially in structured or mobile populations (Sasaki & Uchida, 2013; Sääksvuori, 2014).
    - *Intergroup competition* increases efficiency from punishment compared to isolated groups, often dramatically (Sääksvuori et al., 2011).

**Theory and modeling:**
- **Effect of punishment is highly parameter-dependent**:  
    - *Punishment cost/effectiveness threshold*: Efficiency gains require punishment to be effective (high penalty per cost) and not too frequent or costly (Bowles & Gintis, 2004; Gintis, 2000).
    - *Group size*: Smaller groups generally favor efficiency gains; larger group size can undermine punishment effectiveness without institutional coordination (O'Gorman et al., 2009; Eldakar et al., 2013; Powers & Lehmann, 2017).
    - *Population structure*: Spatial clustering and limited dispersal support more positive punishment effects on efficiency (Helbing et al., 2010; Adami et al., 2016).
    - *Type of punishment*: Institutional (pool) punishment, when honest and non-corrupt, can stably enforce cooperation and high efficiency, but is sensitive to cost-sharing, corruption, and effectiveness (Ishikawa & Fontanari, 2025; Lee et al., 2015, 2017; Dong et al., 2019).
    - *Reward vs. punishment*: Rewards tend to be at least as effective and often more efficient, due to less resource destruction and reduced risk of antisocial use (Dong et al., 2019; Rand & Nowak, 2013).
    - *Synergy with information*: Reputation, partner choice, or public visibility strongly amplify punishment's efficiency effect (dos Santos et al., 2011; dos Santos et al., 2013).

**Moderators and negative cases:**
- **Punishment can reduce efficiency**:  
    - When baseline efficiency (without punishment) is already high due to norms or strong social information, adding punishment frequently *decreases* efficiency by introducing unnecessary or misapplied sanctions (Javaid & Falk, 2015; Vollan, 2008).
    - In settings with complex or corrupt institutions, crowding-out effects, or cultural resistance to imposed rules, punishment can backfire or be neutral (Vollan, 2008; Castillo et al., 2011; Muthukrishna et al., 2017).
    - Voluntary/avoidable punishment (e.g., opt-in pledge systems) does not increase efficiency unless participation and ambition are enforced (Del Ponte et al., 2025).

# 5) Prediction Guidance

**General guidance:**
- **Expect punishment to increase efficiency** *if*:  
    - Control efficiency is substantially below optimum.
    - Punishment cost is not excessive relative to its impact.
    - Antisocial punishment and retaliation are rare or structually prevented.
    - There are no alternative efficiency-boosting mechanisms (e.g., strong communication/norms, reputation, high baseline prosociality).
    - Institution is honest/non-corrupt and well-targeted.
    - Game is repeated/sufficiently long to let punishment take behavioral effect but not so long as to introduce complex retaliation/spite cycles.

- **Expect little or negative effect** *if*:  
    - Control efficiency is already high (norms, information, local authority).
    - Punishment is costly, frequently used, or poorly targeted.
    - Antisocial punishment, crowding-out, or retaliation risk is high.
    - Punishment can be avoided or is not supported by participant buy-in.

**Dimension-specific rules (supported dimensions):**
- **Player count (\`player_count\`)**:  
    - Smaller groups: punishment more likely to improve efficiency (O'Gorman et al., 2009; Bowles & Gintis, 2004).
    - Larger groups: harsher institutions or centralized punishment required; effectiveness can fall off (Ishikawa & Fontanari, 2025).

- **Number of rounds (\`num_rounds\`)**:  
    - More rounds favor long-term discipline and efficiency gains if costs of punishment drop as behavior stabilizes (Sparks et al., 2024).
    - Single/short rounds: punishment rarely yields net efficiency gain.

- **MPCR (\`mpcr\`)**:  
    - Lower mpcr (social dilemma more severe): punishment needed for efficiency gain; as mpcr approaches 1, control likely already efficient, so marginal benefit of punishment declines (Takezawa & Price, 2010).

- **Punishment cost/impact (\`punishment_cost, punishment_tech\`)**:  
    - Positive effect on efficiency only if penalty/impact to the punished is sufficiently high relative to cost to punisher (Sasaki & Uchida, 2013; Eldakar et al., 2007).
    - Too high a cost or weak impact: punishment reduces net group payoff.

- **Reward settings (\`reward_exists, reward_cost, reward_tech\`)**:  
    - If both reward and punishment are enabled, or reward alone, rewards are generally more efficient and less risky for group welfare (Dong et al., 2019).

- **Chat/communication (\`chat\`)**:  
    - Enabling communication can substitute for or amplify punishment's effect on efficiency, sometimes making punishment redundant (Andrighetto et al., 2016; Milinski, 2016).

- **Informational dimensions (\`show_n_rounds, show_other_summaries, show_punishment_id\`)**:  
    - Revealing punishment identity or outcomes can support norm stabilization but also risks retaliation, which can nullify efficiency benefits (Janssen & Bushman, 2008).

**Qualitative adjustment:**  
- *For very high or low control efficiency, the effect size of punishment is smaller or negative, unless design changes are aligned with known moderators (e.g., switching from peer to institutional punishment, adding norms/social capital).*

# 6) Design Dimensions Highlighted Across Papers

**Directly informed:**
- `player_count`, `num_rounds`, `mpcr`, `all_or_nothing`, `punishment_cost`, `punishment_tech`, and to a lesser extent `show_other_summaries` (especially in studies discussing reputation/summary feedback).
- `reward_exists`, `reward_cost`, `reward_tech` are treated in several comparative and hybrid studies.
- `chat` is robustly analyzed in empirical studies of communication effects.

**Indirectly informed:**
- `show_punishment_id` and `show_n_rounds`—occasionally addressed, mainly in the context of information structure, observability, or the threat of punishment.
- `default_contrib` (framing of contribution, opt-in vs opt-out) is less commonly reported but is occasionally manipulated or discussed as a moderator.

**Contextual/missing:**
- Nuanced or compound dimensions (e.g., form of norm feedback, cultural background, multi-level institutions) are rarely parameterized in models; when present, their impact is often described narratively.
- Some dimensions (e.g., punish/reward institution design, optional participation) are addressed only in a few theory or field studies.

# 7) Important Limitations

- **Heterogeneity across studies**: Substantial variation in efficiency effects depending on subject pools (cross-cultural variation, social capital, trust), even under matched game dimensions. Results from lab settings may not extrapolate to real-world field or CPR contexts.
- **Ambiguity in definitions:** Not all papers report efficiency as defined for prediction (ratio of actual/group payoff to social optimum); attention must be paid to outcome mapping.
- **Sparse direct measures:** Some behavioral/outcome effects (e.g., increased contributions) are commonly reported, but only a subset of studies confirm these translate cleanly to improved efficiency, especially when punishment is frequent or costly.
- **Complex boundary conditions:** Parameter sweeps and theoretical models show strong non-linearities and bistability; small parameter changes (e.g., in group size or punishment cost) can flip the effect of punishment from strongly positive to negative.
- **Cultural/contextual moderators:** Many empirical and field studies highlight the importance of local norms, self-determination, group voting, and participant buy-in for the success of punitive institutions. These are not always captured by the 14 design dimensions used in prediction.
- **Indirect applicability for adjacent/complex environments:** Many theory papers study close-adjacent games (CPR, indirect reciprocity, partner choice, threshold goods, etc.), which may not map directly to laboratory PGGs.

---

**In summary:**  
The literature base provides strong—but heavily parameter-dependent—support that enabling punishment in group social dilemmas often increases efficiency, *conditional on* moderate group size, repeated interaction, moderate punishment cost/efficacy, and the absence of pervasive antisocial punishment and retaliation. Game design dimensions most directly support accurate prediction for standard PGGs with measured efficiency, but less so for complex field or institutionalized environments except where explicit efficiency or welfare outcomes are reported. Ambiguity and counterexamples are frequent, especially in high-trust groups, strong norm or communication settings, or when punishment is costly or poorly targeted.
