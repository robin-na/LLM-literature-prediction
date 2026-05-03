# 1) Evidence Base

The reviewed paper set consists primarily of empirical, laboratory experimental studies (the majority), with one observational bibliometric study. Among the 12 papers, 5 use exact or close variants of the public goods game (PGG) and include explicit punishment mechanisms; the remainder examine adjacent game forms (e.g., Prisoner's Dilemma or threshold public good games), or focus on structural determinants like network adaptation or reputation-based partner selection, often without explicit or costly peer punishment. Only a subset directly measures group efficiency or closely related payoff outcomes, with most others focused on behavioral cooperation or contribution rates. The set leans toward narrow, detailed laboratory studies rather than broad meta-analytic synthesis, and provides mixed experimental findings about the effect of punishment on outcomes relevant to the prediction task.

# 2) Task Relevance

**pgg_or_variant:**  
- *Exact relevance* is found in a minority of the set (e.g., Pi et al., 2022; Wang & Huang, 2022; Yang et al., 2020; Sun et al., 2020), each utilizing a standard or canonical PGG.
- *Close or adjacent relevance* arises in threshold public goods or dynamic network settings (e.g., Liao et al., 2021 [retracted], Weng et al., 2021, Zhang et al., 2024).
- Papers on Prisoner's Dilemma games, reputation systems, or general cooperation trends are only *adjacent* or *weak*ly relevant (e.g., Pan et al., 2018; Zhang et al., 2024; Powers et al., 2018; Gao et al., 2025).

**punishment_or_sanctions:**  
- *Exact relevance*: Several studies directly manipulate costly punishment (peer or third-party), sometimes in multiple forms (Pi et al., 2022; Wang & Huang, 2022; Yang et al., 2020).
- *Close/adjacent relevance*: Reputation-based or structural “punishment” (disconnecting, exclusion, network adaptation) are sometimes interpreted as punishment but are technically distinct (Pan et al., 2018; Sun et al., 2020).
- Studies entirely lacking punishment are classified as *none* on this dimension.

**efficiency_or_related_payoff_outcome:**  
- *Exact or close relevance*: Pi et al. (2022) and Wang & Huang (2022) report group efficiency or group payoff as a primary outcome.
- *Adjacent*: Outcomes reported as success rate at achieving a group threshold or other proxies, rather than efficiency ratios (Liao et al., 2021). Other studies focus on behavioral or reputation outcomes, not efficiency.
- *None/weak*: Most studies do not report efficiency or total group payoff per se.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes**: Measured directly in Pi et al. (2022) (efficiency, group payoff), Wang & Huang (2022) (group payoff, efficiency as group payoff relative to maximum), and to some extent Liao et al. (2021) (success rate of group achieving the public good; proxy for efficiency in threshold games).  
- **Non-payoff behavioral outcomes**: The majority of other studies measure average/aggregate contribution, cooperation rate, frequency of successful provision, punishment/reward assignment rates, or partner selection behavior. These are important for understanding mechanisms driving efficiency, but are not direct measures of payoff or welfare.
- **No outcome reporting on efficiency or payoff**: Many adjacent studies (network adaptation, reputation, personality effects) only discuss cooperation frequency, not efficiency.

# 4) Main Findings Relevant To Prediction

- **Peer punishment typically increases efficiency—but not always.** In repeated linear PGGs with peer punishment, enabling costly punishment increases contributions and group payoffs/efficiency compared to the no-punishment baseline (Wang & Huang, 2022), echoing canonical results from the PGG literature.
- **Punishment network structure matters.** Pi et al. (2022) demonstrate that efficiency is highest not when everyone can punish everyone (complete network), but in certain incomplete punishment networks (circle and pairwise). More potential punishers can reduce punishment severity (a bystander effect) and thus lower efficiency.
- **Weak, automatic punishment can reduce efficiency.** When punishment is weak, automatic, and centralized (non-peer), as in Yang et al. (2020), it does not increase group contribution or efficiency; indeed, it may come at a net efficiency cost.
- **Third-party automatic punishment in threshold games can strongly increase provision rates.** Liao et al. (2021) [retracted] finds that third-party punishment increases the success rate of achieving the group threshold, a behavioral proxy for efficiency, in small groups.
- **Timing of punishment observability less crucial than its possibility.** Wang & Huang (2022) report that whether punishments are immediately observable or delayed does not moderate the positive effect of punishment on efficiency in PGGs.
- **Heterogeneity in effect magnitude and group-level outcomes.** Both strictly positive group-level efficiency effects and a degree of between-group variability are noted (Wang & Huang, 2022).
- **Non-costly or reputational “punishments” promote cooperation but evidence for efficiency is indirect.** Adaptive partner selection or network breakup (Sun et al., 2020; Pan et al., 2018; Zhang et al., 2024) increase observed cooperation rates, but do not directly report payoff-based efficiency benefits.
- **Effect of punishment is contingent on institutional and game design details.** Weak, automatic, and/or non-peer punishments are less reliably effective at raising efficiency than peer punishment with sufficient cost and impact.

# 5) Prediction Guidance

**For treatment efficiency prediction tasks in PGG-like settings:**
- **Enable peer punishment, expect increased efficiency on average, but magnitude depends on punishment structure.** In standard, repeated PGGs with peer punishment (i.e., non-automatic, targeted, costly), efficiency reliably increases relative to the no-punishment control—this holds across a range of effect sizes and group heterogeneity (Wang & Huang, 2022; Pi et al., 2022).
- **Consider punishment network structure.** Adding more potential punishers does not always enhance efficiency—limited, structured peer punishment networks can outperform complete networks (Pi et al., 2022). Prediction models should use the `punishment_tech` dimension carefully, beyond just binary encoding of punishment enabled.
- **Automatic or weak punishment does not improve, and may reduce, efficiency.** If the punishment is (a) weak in magnitude, (b) automatic (imposed by rule, not by peers), and/or (c) centralized, efficiency gains should not be predicted; there may be efficiency loss (Yang et al., 2020).
- **Threshold games, third-party punishment.** For small-n threshold PGGs, automatic third-party punishment can substantially improve group success rates (Liao et al., 2021 [retracted]), suggesting a strong efficiency boost for those settings.
- **Effect of observability is minor.** Group efficiency gains from punishment appear to be robust to whether punishments are visible during play or only revealed at the end (Wang & Huang, 2022).
- **Cautions for adjacent designs.** Partner-selection, dynamic linking, and reputation-based exclusions act as cooperation-enhancing mechanisms, but their effect on true efficiency is less well documented in this set and should not be directly conflated with payoff-based outcomes.
- **Control game efficiency is contextually informative but not always reported** (Pi et al., 2022); use with care, and prefer studies that report both control and treatment efficiency in matching contexts.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed**:
- `player_count`, `num_rounds`, `mpcr`, `all_or_nothing`, `punishment_cost`, `punishment_tech` are directly manipulated and discussed in Pi et al. (2022), Wang & Huang (2022), and other experiments.  
- `chat` (communication between players) is sometimes enabled or disabled and tested as a moderator (Wang & Huang, 2022).
  
**Indirectly informed/contextually discussed**:
- `show_other_summaries` and `show_n_rounds` are described as background in several studies (Sun et al., 2020; Ando et al., 2025; Weng et al., 2021).
- `reward_exists` and `reward_cost` appear mainly in adjacent or non-focal studies (Li et al., 2024).
- `default_contrib` (contribution framing) is only occasionally mentioned as a detail of participant instruction.
- `show_punishment_id` is not systematically tested for its effect; anonymity of punishment is described, but evidence is sparse.
- `punishment_magnitude` is included in the cost-magnitude ratio but not systematically varied.

**Effectively missing or weakly covered**:
- Effects of revealing the number of rounds (`show_n_rounds`), detailed forms of outcome summarization (`show_other_summaries`), and the explicit display of the punishment or reward identity (`show_punishment_id`) have minimal or no direct evidence.
- Systematic exploration of simultaneous punishment and reward treatments (`reward_exists` etc.) is essentially missing.
- There is little explicit evidence regarding the interaction of multiple dimension settings.

# 7) Important Limitations

- **Sparse reporting of direct efficiency outcomes.** Only a subset of the papers measures or reports the group efficiency ratio directly; most highlight behavioral cooperation or contribution without payoff context.
- **Heterogeneous game forms and punishment regimes.** Studies mix standard linear PGGs, threshold games, networked games, and other social dilemmas, sometimes with non-peer or automatic punishment; findings may not generalize across all game forms.
- **Limited exploration of full design dimension space.** Not all 14 prediction dimensions are empirically tested, and some (e.g., punishment/reward identity visibility or reward costs) are effectively missing.
- **Lack of systematic comparison of punishment cost, magnitude, and design tradeoffs.** Evidence for how efficiency effects scale with changes in punishment cost or structure is limited to a few design points per study.
- **Unclear generalizability to large groups and different network structures.** Most lab experiments use small groups (n=3-4, occasionally larger), and the scalability of findings to larger PGGs is uncertain.
- **Few direct comparisons between peer and other punishment forms.** Automatic (centralized) vs. peer punishment effects are rarely tested head-to-head in matching designs.
- **Ambiguity due to conflicting findings.** The efficiency impact of punishment is not uniformly positive; the network structure or weak/automatic punishment can reverse the sign of the effect or make it negligible (Pi et al., 2022; Yang et al., 2020).
- **Retracted and adjacent evidence.** Liao et al. (2021) is retracted, and its findings should be treated with caution. Several other papers offer only adjacent evidence, especially regarding efficiency.
- **Absence of meta-analytic or large-sample synthesis.** The evidence is based on individual experiments, not systematic quantitative review or aggregation.

---

## In summary:
The evidence base provides robust support for the positive effect of enabling peer punishment on group efficiency in standard repeated PGGs—but only under certain design conditions, especially where punishment is peer-administered and sufficiently severe. The structure of the punishment mechanism, group size, and MPCR are all well-documented moderators. However, the literature is limited by the infrequent and inconsistent reporting of efficiency outcomes, weak coverage of several prediction dimensions, and only partial generalizability across the full range of PGG-like designs. Models built on this literature should account for these nuances and limit extrapolation to settings that are directly empirically supported.
