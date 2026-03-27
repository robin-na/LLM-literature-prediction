# 1) Evidence Base

The paper set analyzed here is extensive (363 papers) but extremely narrow in empirical scope for the precise prediction task: almost all included sources are **theoretical or simulation-based** studies. Very few empirical or laboratory results (with measured human group payoffs or efficiencies) are present, and none are reported in the digest. The vast majority of papers model evolutionary dynamics, behavioral outcomes, and/or cooperation rates rather than reporting **efficiency or related payoff measures** as directly measured quantities.

The coverage of **punishment** mechanisms is broad, including many variants and analogues (exclusion, ostracism, partner switching, apologia/forgiveness, indirect reputation mechanisms, etc.), but **almost all models treat outcomes as cooperation frequency, extinction risk, prevalence of strategies, or behavioral regime**. Formal efficiency—defined as the ratio of achieved group payoff to the maximum possible—appears only rarely and never as the primary outcome.

The base is thus **broad in explored mechanism and context but shallow on empirical, payoff-based outcome data**. For direct downstream prediction—mapping game design dimensions and no-punishment control efficiency to treatment (punishment-enabled) efficiency—this evidence base is highly indirect.

# 2) Task Relevance

### a) `pgg_or_variant`
- **exact:** A modest subset of papers employs public goods games (PGGs) or direct variants.
- **close:** Many papers model games closely related to PGGs (e.g., threshold public goods, N-player donation games, voluntary contribution mechanisms).
- **adjacent:** A large number use dyadic or small-group dilemmas (prisoner’s dilemma, ultimatum, trust, etc.).
- **weak/none:** Some ethnographic, conceptual reviews and theoretical papers are only tangentially related.

### b) `punishment_or_sanctions`
- **exact:** Some papers model (peer or institutional) punishment as in laboratory PGGs.
- **close:** Many include exclusion, network rewiring, social ostracism, or other indirect sanctions.
- **adjacent:** A significant portion covers related mechanisms (exit, withdrawal, information disclosure, reputation).
- **none:** Some focus only on behavioral strategy evolution without sanctions.

### c) `efficiency_or_related_payoff_outcome`
- **exact:** Almost none. Efficiency is rarely reported.
- **close:** Some papers report average payoff, total group payoff, or welfare in comparison to a fully cooperative group, but generally only as supplementary observations.
- **adjacent/weak:** The overwhelming majority report **behavioral outcomes (cooperation rate, strategy frequency)** rather than **payoff-based outcomes**.
- **none:** Many do not address payoff directly at all.

**Overall Relevance:** The evidence set is primarily adjacent for the core prediction task (the effect of punishment on group efficiency in PGG-like settings).

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes** (e.g., total group payoff, average/group efficiency, welfare, surplus): **Rarely** directly measured or reported.
    - A few exceptions exist in simulation studies which occasionally note average payoff as relating to evolutionary fitness or system stability.
    - When present, payoff is typically analyzed in the abstract as theoretical stability or evolutionary fitness, not as a directly reported efficiency ratio as required for prediction.
- **Non-payoff behavioral outcomes** are **ubiquitous**:
    - Prevalence of cooperation or cooperation rate
    - Frequency and stability of strategies (cooperators, defectors, punishers, rewarders)
    - Survival and extinction of strategy types
    - Network structure and formation (cooperator clusters, partner selection)
    - Social norm or reputation dynamics
    - System stability (bistability, cycles, collapse)
- **Other adjacent outcomes:**
    - Prevalence of punishment/reward use
    - Robustness of cooperative equilibrium
    - Effects on fairness, equality, or social trust

**Note:** Most findings about the impact of punishment on “group outcomes” are interpreted from **changes in cooperation rates**, not actual **efficiency/payoff improvements**.

# 4) Main Findings Relevant To Prediction

### Empirical pattern (as gleaned from theory/simulation):

- **Punishment can increase cooperation**—this is robust across models and contexts (spatial, networked, repeated, dynamic, etc.), **especially when punishment is effective, not too costly, and well-targeted at defectors**.
    - Moderate levels of punishment are generally most beneficial; excessive punishment can reduce payoffs or crowd out voluntary cooperation (Hernandez et al., 2022).
    - Punishment is often more effective in **smaller, stable, or denser networks**, where identities are known and retaliation cycles are contained (Roos et al., 2014).
- **Effect on payoff/efficiency is not always positive or monotonic:** 
    - Punishment that is too costly, mis-targeted (e.g., punishing cooperators, anti-social punishment), or applied in large, anonymous, or mobile groups can **reduce group payoffs or efficiency** due to the cost of punishment itself (Rand et al., 2009; Rumble et al., 2022; Vukov et al., 2013).
    - In networked or spatial settings, too much punishment can also fragment the group or escalate retaliation.
- The **effectiveness of punishment depends heavily on game design dimensions**:
    - **Group size (player_count):** Smaller groups often benefit more from punishment; in large groups, individual incentive to punish is weaker (Kritikos & Bolle, 2004; Dubreuil, 2008).
    - **Punishment Cost and Effectiveness (punishment_cost, punishment_tech):** High effectiveness and low cost maximize positive impact; high cost undermines efficiency (Wei et al., 2021; Vukov et al., 2013).
    - **Social structure:** Dense, integrated networks (as opposed to highly mobile or incomplete networks) favor more effective/efficient punishment (Roos et al., 2014; Larson, 2017).
    - **Presence of anti-social punishment:** If anti-social punishment is present, net efficiency gains are much less likely, and efficiency can be reduced (Gao et al., 2015).
    - **Reward mechanisms:** Reward (or combined reward and punishment) can sometimes substitute for or complement punishment, often being less costly for the same outcome, and may produce higher efficiency in some regimes (Du et al., 2018; Zhao et al., 2023).

### Conflict/Ambiguity:
- Some models suggest that enabling punishment has no effect or even a **negative effect on efficiency**—especially in repeated dyadic games or when retaliatory cycles occur (Rand et al., 2009; Rumble et al., 2022).
- The relation between increased cooperation and efficiency is sometimes **not straightforward**: efficiency gains can be wiped out or reversed by high punishment costs, or crowding out of intrinsic motivation (Gao et al., 2015; Hernandez et al., 2022).

### Key Moderators explicitly stated:
- Punishment cost and punishment-to-impact ratio
- Group size and structure
- Social/partner selection mechanisms (exit, rewiring, exclusion as alternatives)
- Observability, information flow (show_punishment_id, show_other_summaries, chat)
- Asymmetry in power or information

# 5) Prediction Guidance

Given the evidence (almost all derived from **simulations and theory**, not empirical payoff data):

- **Enabling punishment** in PGG-like environments generally:
    - **Increases cooperation rates** under a wide parameter range;
    - Is **likely to increase group efficiency** (i.e., group payoff as a % of cooperative optimum), **but only if**:
        - Punishment is not too costly;
        - Punishment is well-targeted at defectors;
        - Anti-social punishment is minimal or absent;
        - The group is small or networked in a way that supports observability and repeated interaction.
- **If the baseline (control) efficiency is already close to full cooperation** (i.e., without punishment, group nearly achieves maximum payoff), **adding punishment may yield little or no efficiency gain**, and costs may even reduce efficiency (due to wasteful punishment expenditure or crowding out of intrinsic incentives).
- **If control efficiency is low (persistent defection or free-riding dominates), introducing peer punishment is more likely to increase efficiency**—again, as long as punishment is not overly costly or mis-targeted.
- **Optimal punishment parameters (cost, impact) are typically moderate:** Too low and punishment is ineffective; too high and the costs outweigh cooperation gains.
- **Social context and implementation matter:** Effective punishment often requires observability, reputation, communication about actions, and, in larger groups, may need to be institutional (not peer) to be efficient.
- **Combined reward and punishment mechanisms can be more effective than either alone**, especially when well-calibrated (Zhao et al., 2023; Zhang et al., 2022).

However, **in the absence of empirical, payoff-based outcome data linking game design parameters and control efficiency to actual post-punishment efficiency**, these relationships must be treated as **mechanistic expectations, not quantitative predictions**.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions:**
- `player_count`: Moderately discussed (group size effects, crowding, group structure).
- `punishment_cost`, `punishment_tech`: Heavily analyzed (cost/benefit tradeoff, effectiveness, threshold for positive impact).
- `reward_exists`: Frequently modeled in combined reward/punishment regimes.
- `show_other_summaries`, `show_punishment_id`: Commonly noted as important for observability, reputation, or effectiveness of punishment/reward.
- `all_or_nothing`: Modeled in many adjacent games (binary contribution or action selection).

**Indirectly/contextually informed:**
- `num_rounds`: Usually included as part of repeated game structure (but effect on payoff/efficiency is not always isolated).
- `chat`: Communication modeled in some settings; generally support improved cooperation and possibly amplify punishment effectiveness.
- `mpcr`: Often parameterized as the benefit-to-cost ratio or public goods multiplier; its interaction with punishment is recognized but links to efficiency not reported explicitly.
- `reward_cost`, `reward_tech`, `reward_tech`: Discussed in dual-mechanism models.

**Sparse or missing:**
- `default_contrib`: Very rarely discussed.
- `show_n_rounds`: Occasionally described, but not analyzed for outcome effects.
- `show_punishment_id`: Named as a potentially relevant moderator for punishment effectiveness, but not systematically analyzed.
- `show_other_summaries`: Included in some reputation and information flow models, but rarely connected to efficiency.

**Missing for payoff-based prediction:**
- None of the 14 dimensions are specifically mapped—via empirical data—to efficiency increase or decrease under punishment treatments; all evidence is indirect or theoretical.

# 7) Important Limitations

- **Absence of empirical, payoff-based outcome data:** Almost no papers provide actual efficiency values for control vs. punishment treatments in experimental or field settings.
- **Behavioral outcomes dominate:** Nearly all claims about efficiency are inferred from increases in cooperation rate, not direct payoff improvements. High cooperation rates do not always guarantee efficiency gains, especially when punishment is costly.
- **Heterogeneity and boundary conditions are underexplored:** The effect of design dimensions (e.g., varying player_count, MPCR, punishment_cost) on efficiency is discussed mostly in qualitative or theoretical terms, not estimated with data.
- **Anti-social punishment, retaliation, and crowding-out are often discussed, but their quantitative impact on efficiency is speculative.**
- **Limited generalizability:** Most models are specific to particular types of social dilemmas, populations, or network structures; their transferability to laboratory or real-world PGGs is not tested in this set.
- **Contradictory/conflicting findings:** Some theoretical models predict positive, others negative, and some mixed effects of punishment on efficiency, depending on the detailed assumptions (network, cost structure, presence of anti-social punishment, etc.).
- **Sparse coverage of certain dimensions:** For key moderators like `default_contrib`, `show_n_rounds`, and `show_punishment_id`, little to no predictive evidence is available.

**Conclusion:** This literature set provides **strong mechanistic and qualitative support** for the conditions under which punishment is likely to influence cooperation and possibly efficiency, with highlights on the key role of cost-effectiveness, targeting, group size, and social structure. However, it is **not sufficient for quantitative prediction** of treatment efficiency from specified design dimensions plus control efficiency, due to an almost total lack of empirical or directly measured payoff-based outcome data. All predictions derived from this set should be treated as **theoretical priors or qualitative expectations** rather than data-driven forecasts.
