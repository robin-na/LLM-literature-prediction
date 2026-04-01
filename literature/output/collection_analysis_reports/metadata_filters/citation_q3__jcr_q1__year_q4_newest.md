# 1) Evidence Base

This paper set is large (49 items), with a mix of theory papers, simulation/modeling studies, lab and field experiments, and observational/ethnographic works. Roughly half are theory or simulation, focusing on evolutionary/game-theoretic analysis of PGG or closely related environments and mechanisms (punishment, reward, exclusion, reputation). The empirical subset contains mostly laboratory PGG experiments with punishment, along with field/observational studies and meta-analyses. For the downstream efficiency prediction task, the evidence base is theoretically rich for well-specified settings, but empirical coverage of payoff-based group efficiency outcomes is thin—most empirical and some theoretical papers focus on behavioral outcomes (contribution, cooperation, punishment frequency) rather than efficiency or payoff ratios. There is broad, taxonomically relevant coverage of PGG and its classic variants, with some adjacent work from PD, innovation, governance, and real-world norm enforcement contexts.

# 2) Task Relevance

**PGG or Variant:**  
- **exact:** Many theory and meta-analysis papers are framed precisely in standard or spatial PGGs (e.g., Li et al., 2022; Wang et al., 2024; Sun et al., 2023). Several empirical experiments directly use the repeated or one-shot PGG framework.  
- **close/adjacent:** Some studies employ variants (threshold PGG, PD with commitment/exclusion, innovation dilemmas) or real-world analogs (e.g., policy/governance games, ethnographic fieldwork), which are conceptually relevant but less structurally matched.  
- **none/weak:** A small set addresses only conceptual or distant games (norm psychology, real-world punishment), without PGG structure.

**Punishment or Sanctions:**  
- **exact:** Most theory and several empirical papers explicitly analyze punishment mechanisms (peer, pool, institutional, exclusion-based, reputation-modulated, etc.).  
- **close:** Some discuss exclusion, reward, or hybrid schemes (e.g., reward and punishment together).  
- **adjacent/weak:** A few papers focus on reputation, social learning, or norm enforcement without explicit punishment.

**Efficiency or Related Payoff Outcome:**  
- **exact:** Several theory papers directly measure or model group/treatment efficiency (Li et al., 2022; Sun et al., 2023; Wang et al., 2024; Wang & Perc, 2022). Some simulation/modeling work reports average or mean payoff, or social welfare, as primary outcomes.  
- **close:** Many papers report average payoff or cost minimization, which closely tracks efficiency, but do not always normalize to the theoretical maximum.  
- **adjacent:** Several studies focus on non-payoff outcomes (contribution rate, cooperation density), sometimes using payoff for evolutionary dynamics only.  
- **weak/none:** Ethnographic and psychological concept papers often do not measure or report efficiency or group payoff.

Overall, the literature is **strongly relevant** on PGG and punishment, but only **moderately relevant** for efficiency outcomes as required for the downstream prediction task, especially in empirical work.

# 3) Outcomes Measured in the Literature

**Payoff-Related Outcomes:**  
- *Efficiency (normalized group payoff, surplus, welfare):*  
    - Directly reported in several theory/simulation papers for specific PGG configurations (Li et al., 2022; Sun et al., 2023; Wang et al., 2024; Wang & Perc, 2022; Han et al., 2022, 2024; Han et al., 2022b; Köster et al., 2022).  
    - Some simulation models report average payoff or explicit phase diagrams for mean earnings.
- *Total Earnings, Group Payoff, Welfare, Social Welfare, Surplus:*  
    - Sometimes used interchangeably with efficiency, but not always with the precise normalization.
    - Several theory papers focus on minimizing total cost, maximizing group payoff, or maximizing social welfare as proxies for efficiency.

**Non-Payoff Behavioral Outcomes:**  
- *Contribution Rate, Cooperation Rate, Norm Compliance, Punishment Frequency:*  
    - The primary outcome in most empirical PGG experiments.
    - Frequent in meta-analyses and field studies.
    - Many models use these as endpoints for evolutionary stability.
- *Strategy Frequencies, Trust, Trustworthiness, Voting for Punishment:*  
    - Main outcomes in adjacent or broader social dilemma literature.
    - Ethnographic/observational papers typically focus on behavioral or institutional variables.

**Distinction and Mapping:**  
- Many papers that report only increased cooperation/contribution rates do *not* report whether this leads to higher efficiency, as the cost of punishment may offset group gains.
- Some theory papers explicitly show that maximizing cooperation via punishment does *not* guarantee higher efficiency (Han et al., 2024).

# 4) Main Findings Relevant to Prediction

### Synthesis of Core Findings:
- **Enabling punishment generally increases cooperation and often—but *not always*—increases efficiency/group payoff compared to no-punishment control.**  
    - *Direct positive efficiency effects* are consistently found in theory and simulation for both peer and institutional punishment if the punishment strength/cost is in the optimal regime (Li et al., 2022; Wang et al., 2024; Sun et al., 2023; Wang & Perc, 2022).
    - *Empirical PGG experiments* almost always confirm increased cooperation under punishment (Zhou et al., 2022; Zhou et al., 2023) but often do not report on efficiency or earnings; where payoff is measured, increases are commonly found when punishment is moderate and effective.

- **The effect of punishment on efficiency is *not monotonic* and depends strongly on game dimensions:**  
    - *Punishment cost and effectiveness* (punishment_cost, punishment_tech):  
        - Too high a cost can erase efficiency gains or make punishment net-negative, especially if defectors are already few or punishment is misapplied (Han et al., 2024; Wu et al., 2022).
        - Critical thresholds for effect: if punishment fines/strengths cross a threshold (relative to cost, mpcr), defectors are suppressed and efficiency is maximized (Wang et al., 2024; Ohdaira, 2022).
    - *Institutional vs. peer punishment:*  
        - Institutional (tax-based, pool, global exclusion) can be more cost-effective or robust, especially in large or structured populations (Li et al., 2022; Wang & Perc, 2022).
        - Peer punishment is more sensitive to cultural/behavioral moderators and retaliation risk.
    - *Game structure (player_count, network structure, all_or_nothing, mpcr):*  
        - Structured populations (spatial/networks) can support higher efficiency with punishment, due to clustering of strategies and local support effects (Wang et al., 2024; Ohdaira, 2022; Quan et al., 2023b).
        - Higher mpcr (synergy factor) generally makes it easier for punishment to improve efficiency, but interacts with other dimensions (Li et al., 2022).
    - *Interaction with reward and combinations:*  
        - Reward can sometimes outperform punishment for efficiency, especially under noisy or uncertain conditions, or when the reward/punishment ratio favors reward (Sun et al., 2023; Han et al., 2024).
        - Adaptive hybrid protocols (switching between reward and punishment) may offer maximal efficiency in structured games.

- **Not all increases in cooperation from punishment translate into higher efficiency:**
    - Several theory papers demonstrate scenarios in which punishment raises cooperation rates but reduces net group efficiency (Han et al., 2024; Wu et al., 2022).
    - Excessive or poorly targeted punishment, and the presence of corruption or antisocial punishment, can make efficiency outcomes worse than no-punishment control.

- **Key boundary/moderator effects:**
    - *Corruption, noise, and legitimacy* moderate the benefits of punishment (Liu & Chen, 2022; Wu et al., 2022; Spadaro et al., 2023).
    - Cultural background affects punishment behavior but is rarely shown to moderate efficiency (Zhou et al., 2023).
    - Voluntary, targeted, or reputation-based punishment is more conducive to efficiency than indiscriminate or compulsory punishment (Han et al., 2022b; Quan et al., 2023a).

# 5) Prediction Guidance

Given the above findings, **the literature supports the following guidance for predicting the efficiency effect of enabling punishment in PGG-like games:**

- **If baseline (control) efficiency is low due to defection** and the punishment mechanism is designed with moderate cost, appropriate strength, and sufficient targeting (as informed by `punishment_cost`, `punishment_tech`, etc.), enabling punishment is likely to increase efficiency, with the magnitude determined by the effectiveness and cost trade-off.  
    - **Use direct model results (Li et al., 2022; Wang et al., 2024)** to estimate whether the punishment parameters cross the necessary threshold for increasing efficiency.

- **If punishment is too costly, poorly targeted, or misapplied**, it may increase cooperation without increasing efficiency, and in some scenarios, group efficiency may fall relative to control (Han et al., 2024; Wu et al., 2022).

- **Structured/networked populations (as specified by `player_count`, spatial/network config, etc.)** support higher efficiency gains under punishment due to clustering and localized enforcement (Wang et al., 2024; Ohdaira, 2022).

- **If reward or hybrid incentives are available (`reward_exists`),** adaptive protocols may yield higher efficiency than punishment alone, especially in contexts with noise or uncertain monitoring.

- **Critical design dimensions for prediction:**  
    - Prediction is best supported when detailed values for `player_count`, `num_rounds`, `mpcr`, `punishment_cost`, `punishment_tech`, and population structure are given, as these are directly linked to model conditions for positive efficiency effects.
    - For treatments with exclusion or commitment, the timing of punishment and availability of voluntary opt-out (`all_or_nothing`, `show_n_rounds`) are important (Han et al., 2022b; Liu et al., 2022).

- **Ambiguity/heterogeneity:**  
    - If the control game already has high efficiency (e.g., due to high mpcr or strong reward/communication), punishment may have little or even negative net effect.
    - Evidence is thinnest on the disruptive effects of antisocial punishment, punishment legitimacy, or dynamic group composition on efficiency—as such moderators are more often discussed than explicitly modeled or measured.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed for prediction:**
- `player_count`, `num_rounds`, `mpcr`, `all_or_nothing`, `punishment_cost`, `punishment_tech`, `reward_exists`, `reward_cost`, `reward_tech`
    - Multiple theory papers provide payoff phase diagrams and explicit threshold conditions as a function of these dimensions (Li et al., 2022; Wang et al., 2024; Sun et al., 2023).
- Population structure (networked vs. well-mixed) is deeply addressed in simulation and theory, implicating `player_count` and spatial configuration.

**Indirectly informed/contextually discussed:**
- `chat`, `show_n_rounds`, `show_other_summaries`, `show_punishment_id`
    - Communication, round information, observability, and identity dynamics are mentioned as moderators, especially in empirical/meta-analytic work (Spadaro et al., 2022), but are rarely directly modeled for efficiency outcomes.
- `default_contrib`
    - Occasionally discussed in framing or cognitive studies (Capraro, 2024).

**Sparse or effectively missing:**
- Detailed empirical results linking punishment to *treatment efficiency* across full range of dimensions (i.e., few lab or field experiments actually report group payoff/efficiency in all conditions).
- The combined manipulation of reward and punishment parameters is less often reported as directly additive (many papers choose one mechanism).
- Dynamic group composition, endowment or productivity heterogeneity (Wang et al., 2023), and real-world institutional variation are more descriptive/contextual than formalized.

# 7) Important Limitations

- **Limited empirical payoff data:**  
    - Few experiments report both control and treatment efficiency; most measure only behavioral outcomes. Generalizing from cooperation rates to efficiency requires strong and sometimes invalid assumptions about punishment cost structures.
- **Non-monotonicity and boundary conditions:**  
    - Many models identify regions where punishment *decreases* efficiency. The literature emphasizes careful parameterization—simple heuristics (e.g., "punishment always helps") are contradicted by multiple theory papers.
- **Transfer from theory to real-world/empirical context is not always valid:**  
    - Models frequently assume infinite populations, infinite rounds, deterministic updating, or other simplifications not met in lab/field designs.
- **Reward vs. punishment:**  
    - Several papers show that reward (or hybrid/adaptive mechanisms) can outperform punishment for efficiency, yet these findings are not always replicated in matched empirical studies.
- **Moderators under-studied:**  
    - Effects of antisocial punishment, cultural norms, communication, group composition, and legitimacy are discussed or modeled in highly stylized ways but rarely tested for efficiency in empirical studies.
- **Design dimension coverage is uneven:**  
    - While key game-theoretic parameters are amply modeled, many experimental design choices (e.g., information, chat, institutional identity) are understudied with respect to efficiency impact.
- **Adjacent and non-PGG contexts:**  
    - Several "payoff" findings are from adjacent games (PD, commitment/innovation) or real-world settings, limiting direct transfer to canonical PGG structure.

**In summary:**  
The literature set directly supports prediction of efficiency effects from punishment in public goods games for key design parameters, primarily through theory/simulation, with spotty empirical confirmation. Efficient prediction should use formal models for the relevant region of parameter space; simple extrapolation from behavioral outcomes or from theory papers outside the parameter regime is not supported. Ambiguities remain, especially regarding real-world moderators and extreme parameterizations.
