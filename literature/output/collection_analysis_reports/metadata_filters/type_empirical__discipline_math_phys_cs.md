# 1) Evidence Base

The evidence base consists of 69 empirical papers, virtually all of which are laboratory experiments (mostly with human subjects; some simulation or agent-based studies are present for adjacent environments). The set is broad in the sense that it covers a wide variety of social dilemma games and sanctions/rewards mechanisms, but relatively narrow in terms of the target outcome for prediction (efficiency in PGG-like environments with and without peer punishment). A substantial subset consists of exact or close matches: repeated linear or threshold public goods games with and without institutional or peer punishment, reporting either efficiency (group payoff relative to maximum) or close payoff-based outcomes. Other papers cover adjacent games (e.g., trust, coordination, team investment, PD) or focus on non-payoff outcomes (contribution rates, norm compliance) with limited value for the efficiency prediction task. Some studies are included with no direct manipulation of punishment or payoff, serving only contextual or negative relevance.

# 2) Task Relevance

**PGG or Variant**:  
- *Exact*: Many papers directly use standard repeated PGGs (linear, threshold, or continuous).  
- *Close*: Several examine close variants (e.g., generalized exchange, collective-risk, CPR, team investment games, coordination games with similar group structures).  
- *Adjacent*: Others use trust games, ultimatum games, market or bilateral exchange, or iterated PDs.

**Punishment or Sanctions**:  
- *Exact*: Multiple studies implement peer or institutional punishment in the PGG, often varying punishment cost, magnitude, or structure.  
- *Close*: Some use exclusion, expulsion, centralized/third-party, or automatic punishment, which is often analogous to peer punishment.  
- *Adjacent/Weak*: Many address reward, exclusion, feedback, observability, or social sanctions without monetary fines.

**Efficiency or Related Payoff Outcome**:  
- *Exact/Close*: Approximately a dozen papers report group efficiency, group payoff, or total surplus relative to full cooperation (in relevant PGGs).  
- *Adjacent*: Many report related outcomes (group profit, welfare, net benefit) but not as a ratio to maximum possible; others focus on cooperation or contribution rates only, which must not be conflated with efficiency.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes**:  
  - *Efficiency* (group payoff/maximum): Reported directly in multiple core PGG punishment experiments (e.g., Bahbouhi et al., 2024; Cobo-Reyes et al., 2022; Castillo et al., 2021; Pi et al., 2022; Kanitsar, 2021; Wang & Huang, 2022).  
  - *Total/group earnings, net profit, welfare, surplus*: Sometimes reported as primary outcomes, other times derivable.  
  - *Group success/probability of reaching target*: Used in threshold or collective-risk versions (e.g., Jiang et al., 2023; Liao et al., 2021).

- **Non-Payoff Behavioral Outcomes**:  
  - *Cooperation/contribution rates*: Commonly measured (sometimes the only outcome); often associated with, but not equivalent to, efficiency.
  - *Punishment frequency, norm compliance, strategy updating*: Frequently analyzed as mechanisms or secondary outcomes.

- **Distinction in Reporting**:  
  Payoff-based outcomes are the required ground-truth for predicting changes in efficiency. Several studies report mixed outcomes, and sometimes inferred efficiency effects are drawn from changes in cooperation/contribution (these must be noted as such).

# 4) Main Findings Relevant To Prediction

Synthesizing across the most relevant studies:

**Peer Punishment in Standard PGGs:**
- *Typical Effect*: Enabling peer punishment tends to **increase group efficiency/total payoff** relative to the no-punishment control, but the magnitude and direction are highly conditional (Bahbouhi et al., 2024; Suleiman & Samid, 2021; Wang & Huang, 2022).
- *Moderators*:
  - **Punishment Structure/Technology**: Too much scope for [retaliation, multiple stages, fixed IDs] can nullify efficiency gains or cause feuding that offsets higher contributions (Engelmann & Nikiforakis, 2015; Pi et al., 2022; Villatoro et al., 2014).
  - **Punishment Network**: Incomplete, well-targeted punishment networks (circle/pairwise) often yield higher efficiency than complete, diffuse networks (Pi et al., 2022; Kanitsar, 2021).
  - **Cost and Effectiveness Ratio**: Low or costless punishment is much more efficiency-enhancing; high costs can neutralize or reverse gains (Kanitsar, 2021).
  - **Antisocial/Norm-keeper Punishment**: High rates of antisocial or indiscriminate punishment reduce efficiency benefits (Suleiman & Samid, 2021; Bahbouhi et al., 2024).
  - **Group Decision Rules**: Team/unanimity decision structures can reduce antisocial punishment and improve net efficiency under punishment (Bahbouhi et al., 2024).
  - **Centralized vs. Peer Sanctioning**: Centralized punishment (single manager) nearly always increases efficiency; selection mechanism (vote/rand) is less consequential (Castillo et al., 2021). Formal/centralized sanctions outperform informal under group openness or migration (Cobo-Reyes et al., 2022).
  - **Group Structure/Density**: In sparse networks or generalized exchange, punishment often fails to improve efficiency (Kanitsar, 2021).
  - **Group Size, Openness**: Larger, open groups (migration possible) gain more from punishment. Efficiency gains are fragile when social structure allows for exit or endogenous group formation (Cobo-Reyes et al., 2022; Pi et al., 2022).

**Mixed or Null Effects**:
- Inappropriately structured punishment, weak or automatic punishment, or environments prone to antisocial punishment can **reduce or leave unchanged efficiency** (Engelmann & Nikiforakis, 2015; Yang et al., 2020; Calabuig et al., 2024).
- Efficiency gains from punishment **do not generalize** to adjacent environments (e.g., trust games, binary investment games, etc.), and can even lower efficiency due to direct punishment costs (Herne et al., 2022; Abbink et al., 2004; Calabuig et al., 2024).

# 5) Prediction Guidance

**For the downstream prediction task — predicting average efficiency of a game with peer punishment enabled, given design dimensions and control efficiency:**

- **Direct Empirical Guidance**: For standard repeated linear PGGs, introducing peer or centralized punishment **usually** increases average efficiency over the no-punishment baseline, but *the effect is highly dependent on design details*:
  - Punishment that is *costly but non-retaliatory, limited in scope, and well-targeted by design* yields clear increases in efficiency.
  - Environments with: **high costs**, *allowance for mutual retaliation*, or frequent **antisocial/norm-keeping punishment** see efficiency gains greatly reduced or even reversed. If the control efficiency is low (due to free-riding), potential for gain is higher, but only if punishment is not itself too costly or misapplied.
  - **Team decision making** (e.g., with unanimity) increases the efficiency benefits of enabling punishment by reducing costly antisocial punishment.
  - **Network structure matters**: Making punishment possible by all to all (complete network) can lower efficiency relative to more structured, limited networks.
  - **Centralized (formal) punishment** yields more robust efficiency gains than peer or informal punishment, especially when groups are open or migration is possible.

- **Indirect/Mechanism Guidance**: Effects inferred from higher contributions or cooperation rates must be cautiously translated to efficiency; if punishment itself is costly and frequent, gains in cooperation may not result in higher net payoffs.

- **Where Evidence Is Limited**:
  - Efficiency effects are **less predictable** in adjacent games (trust games, binary decision, generalized exchange, CPR/threshold). Directly transfer only when structural features align closely with standard PGGs.
  - Key design dimensions often **interact** (e.g., punishment cost × information × network structure).

- **Implications for Using Control Efficiency**: The control efficiency is informative as a baseline, but *the efficiency increase from enabling punishment is moderated by the above factors*; sometimes the effect is small or negative if punishment is frequent and costly.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**  
- `player_count`, `num_rounds`, `mpcr`, `punishment_cost`, `punishment_tech`, `all_or_nothing`, `chat`, `reward_exists` (and sometimes `reward_cost`, `reward_tech`)
  - These are usually explicitly manipulated or reported in the core PGG punishment experiments.
  - **Punishment cost and technology**: Shown as critical moderators for efficiency gains.
  - **Player count/group size**: Larger groups require stronger punishment regimes to maintain efficiency; sometimes reported under migration/open group designs.

**Indirectly Informed:**  
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Occasionally analyzed (e.g., role of information, transparency, feedback, and punishment observability), but evidence is thinner or more contextual.
- `default_contrib`: Sometimes reported (opt-in vs. opt-out framing), but rarely the focus of punishment efficacy.
- `all_or_nothing` vs. continuous contributions: Both represented; some studies show that certain intervention effects (e.g., redistribution) vary by this dimension.

**Sparse/Contextual or Missing:**  
- `reward_exists/cost/tech`: Scattered evidence, mainly as comparison treatments; few direct tests of mixed sanction and reward regimes on efficiency.
- `chat`: Typically disabled in most punishment studies; influence of communication on efficiency under punishment is not well-explored.
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Information/observability effects are covered, but payoff-based evidence on their role in moderating efficiency under punishment is sparse.
- Little direct discussion of `default_contrib` or framing effects in relation to the effect of punishment on efficiency.

# 7) Important Limitations

- **Coverage of Prediction Dimensions**: While core design dimensions (group size, rounds, MPCR, cost/tech of punishment) are well covered, **not all 14 prediction dimensions are equally informed**—especially dimensions relating to information environment, framing, or mixed sanction/reward regimes.
- **Ambiguity in Mixed-Outcome Studies**: Contribution rate increases do not always translate to higher efficiency; some studies rely on behavioral proxies, not direct payoff data.
- **Context and Mechanism Interactions**: Some findings may not transfer when game structure is altered (e.g., generalized exchange, threshold PGGs, binary vs. continuous contributions).
- **Variability and Heterogeneity**: Large variation across societies, groups, and cultures in punishment effects on efficiency; average effects can mask substantial subgroup differences (Suleiman & Samid, 2021).
- **Absence of Some Critical Designs**: Multi-level or hybrid sanction/reward schemes, networked environments, or varied information display — rarely tested in terms of payoff efficiency.
- **Field/Real-World Generalizability**: Field experiments often find **weaker or absent efficiency benefits of peer punishment** relative to laboratory studies (Noussair et al., 2015).
- **Limitation in Reporting**: Many adjacent or contextual papers focus on non-payoff outcomes, limiting their direct utility for the prediction task.
- **Mechanisms Not Fully Separated**: In some studies, increased efficiency is entangled with other changes (e.g., communication, group formation), making it difficult to isolate the effect of peer punishment per se.

---

**Summary**:  
The literature base is strong for standard repeated PGG lab environments and provides a clear empirical foundation for expecting efficiency increases with punishment, conditional on key game design parameters—especially punishment cost/tech, network structure, and moderators of antisocial punishment. Several dimensions central to downstream prediction (e.g., information environment, communication, mixed incentives) are less frequently or only indirectly tested. There is significant empirical ambiguity in generalized/adjacent games and under certain institutional/punishment structures, cautioning against broad generalization beyond the well-studied lab PGGs. The best predictions will leverage direct evidence from studies closely matched to the design in question and use control efficiency as a baseline while applying empirically supported moderators for the effect of enabling punishment.
