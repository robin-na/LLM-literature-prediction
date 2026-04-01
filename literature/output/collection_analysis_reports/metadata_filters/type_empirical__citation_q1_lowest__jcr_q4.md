# 1) Evidence Base

The paper set consists of 26 sources, with a strong predominance of empirical, laboratory-based experiments on public goods games (PGG) and related social dilemma environments. Nearly all relevant studies use experimental designs, often with well-defined game mechanics and clear reporting of group-level outcomes. There are some observational and ethnographic studies, but these are generally only contextually relevant and do not directly address efficiency or punishment in PGGs.

The evidence is primarily empirical, not theoretical. The papers focus heavily on peer punishment and institutional sanctioning, with frequent measurement of payoff-based outcomes, though several studies focus on behavioral outcomes (e.g., contribution rates) without directly reporting efficiency. The literature is relatively broad regarding the institutional detail of punishment and related mechanisms, yet direct coverage of all 14 game design dimensions is uneven—certain dimensions (e.g., player count, MPCR, punishment parameters) are consistently specified, while others (e.g., chat, information conditions, reward mechanisms) appear less systematically.

Overall, the evidence base is well-suited to support empirical prediction of the treatment effect of enabling punishment on efficiency in standard PGGs and some close variants, but is more limited for adjacent or contextually related environments and for games diverging from the canonical PGG structure.

# 2) Task Relevance

**pgg_or_variant relevance**:  
- *Exact*: Multiple studies (e.g., Suleiman & Samid, 2021; Cobo-Reyes et al., 2022; Pancotto et al., 2023) directly use standard repeated PGGs as their environment.
- *Close*: Several others feature coordination games (minimum effort, team investment) or mechanisms (grouping, trust games) that are structurally close but not classic PGGs.
- *Adjacent/Weak/None*: Observational and ethnographic studies are either adjacent or weakly relevant, typically lacking formalized or repeated game structures.

**punishment_or_sanctions relevance**:  
- *Exact*: Many studies manipulate the presence or design of peer punishment or centralized/formal sanctioning.
- *Adjacent*: Studies on exclusion, replacement, or informal social sanctions are classified as adjacent unless costly peer punishment is a central mechanism.
- *None*: Some studies focus exclusively on reward, transparency, or group structure, without introducing punishment.

**efficiency_or_related_payoff_outcome relevance**:
- *Exact*: A significant portion report group efficiency, total/group payoff, or closely related metrics.
- *Adjacent/Close*: Several report contribution rates, norm compliance, or cooperation as proxies and infer efficiency effects; a few provide payoff changes in adjacent game types.
- *None*: Ethnographic and context-only papers (e.g., Sequeira, 2023; Bharti & Malik, 2023) provide no direct payoff data.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:**  
  Many core studies measure and report total group earnings, average individual payoff, group welfare, or efficiency (defined as the ratio of actual payoff to the social optimum). Examples include Suleiman & Samid (2021), Cobo-Reyes et al. (2022), Peng (2022), Nax et al. (2018), Kanitsar (2021), Lec et al. (2023), Calabuig et al. (2024), etc.

- **Non-payoff behavioral outcomes:**  
  Other studies report primarily on contribution rates, frequency of cooperation, punishment frequency, or binary group success (e.g., Pancotto et al., 2023; Selterman, 2019; Grund et al., 2020). These are important for mechanism understanding but do not always translate directly into efficiency measures.

- **Mechanism/process outcomes:**  
  Some studies focus on the prevalence of antisocial punishment, strategies underlying punishment (e.g., norm-keeping vs. strong reciprocators), or decision process effects such as the impact of visibility or justification (Suleiman & Samid, 2021; Herne et al., 2022; Li et al., 2023).

**Distinction:**  
It is crucial to separate payoff-based outcomes (used for efficiency prediction) from behavioral outcomes, as the latter may not always lead to higher efficiency—especially if costly punishment reduces group payoff even as it increases cooperation.

# 4) Main Findings Relevant To Prediction

- **Punishment generally increases efficiency in standard PGGs**  
  Across core PGG studies, enabling peer punishment typically results in a moderate, but variable, increase in group efficiency (Suleiman & Samid, 2021; Cobo-Reyes et al., 2022). The efficiency gains are highly context-dependent, moderated by group composition (strong reciprocators vs. norm-keepers) and by cultural or institutional context.

- **Cost and effectiveness of punishment are critical**  
  When punishment is costless or has a high impact-to-cost ratio, efficiency gains are more likely (Kanitsar, 2021; Lec et al., 2023). When punishment is costly or poorly targeted, efficiency can remain flat or even decline due to the deadweight loss from sanctioning (Herne et al., 2022; Calabuig et al., 2024).

- **Institutional and network features matter**  
  Formal, centralized sanctions outperform informal/peer sanctions in open societies (Cobo-Reyes et al., 2022). The density of the punishment network is a moderator (Kanitsar, 2021). Enabling migration and endogenous group formation can amplify or attenuate the efficiency impact of punishment.

- **Behavioral mechanisms**  
  Efficiency gains from punishment are often driven not by increased deterrence of defectors, but by higher contributions from cooperators who anticipate punishment (Suleiman & Samid, 2021). Significant heterogeneity exists across groups.

- **Adjacent and non-PGG settings**  
  In trust or coordination games, punishment does not always increase efficiency—sometimes reducing net payoffs due to costly sanctions (Herne et al., 2022; Calabuig et al., 2024). Coordination games, when punishment is effective and group sizes are large, may see increased coordination and thus efficiency (Lec et al., 2023).

- **Lack of direct evidence for some mechanisms**  
  Many contexts (exclusion, binary threshold games, real-effort team tasks) show only adjacent results—important for understanding mechanisms but less directly translatable into quantitative efficiency predictions for standard PGGs.

# 5) Prediction Guidance

The literature provides a strong empirical basis for predicting that enabling peer punishment in standard repeated PGGs will increase efficiency, relative to control conditions without punishment, **but the magnitude is variable and context-dependent**. Key moderators include:

- **Game parameters:**  
  Efficiency gains are larger with low punishment costs and high punishment effectiveness. With high-cost or inefficient punishment, net efficiency gains may vanish or reverse.

- **Baseline group efficiency:**  
  The higher the baseline/control efficiency, the less headroom for further improvement. In high baseline cases, costly punishment may actually reduce net payoff.

- **Group composition and norms:**  
  Prevalence of pro-social ('strong reciprocators') vs. norm-keeping or antisocial punishing types influences both the sustainability and magnitude of efficiency gains.

- **Institutional features:**  
  Centralized/formal punishment is more effective in mobile/open group contexts. Network density (who can punish whom) also matters, especially in non-standard structures.

- **Behavioral context:**  
  Anticipation of punishment can raise contributions and thus efficiency, even if punishment is infrequently applied.

**For downstream prediction:**  
If the target environment closely matches the standard PGG paradigm (player count, rounds, MPCR, etc.), and with punishment parameters matching the empirical literature (especially with moderate cost/effectiveness), prediction should expect a moderate efficiency lift when enabling punishment. Adjustment downward is warranted if punishment is costly, the baseline efficiency is already high, or if the evidence suggests coordination failures (e.g., frequent antisocial punishment).

Where adjacent or context-only studies are the only evidence, predictions about efficiency changes should be highly qualified or considered unsupported by direct empirical evidence.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed:**
- `player_count` (ubiquitously reported, central parameter)
- `num_rounds` (consistently specified, crucial for sustaining effects)
- `mpcr` (central to both control and treatment efficiency)
- `all_or_nothing` (differentiates continuous vs. binary settings)
- `punishment_cost` (key moderator of net efficiency impact)
- `punishment_tech` (cost-to-impact ratio often specified or discussed)
- `reward_exists` (directly manipulated in some studies; evidence is less common for dual punishment-reward settings)
- `chat` (explicitly manipulated in some studies—often, chat is disabled)

**Indirectly/contextually informed:**
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id`  
  These are typically only reported in methods or as part of information structure, not as central treatment factors tied to efficiency outcomes.

- `reward_cost`, `reward_tech`  
  Explored in studies on rewards rather than punishment per se.

**Sparse/missing:**
- `default_contrib`  
  Very rarely specified—framing effects (opt-in vs. opt-out) are mentioned in only a minority of papers.
- `show_punishment_id`  
  Usually fixed as anonymous; the direct effect on efficiency is rarely isolated.
- Some aspects of the information environment (e.g., visibility of mechanisms, payoff transparency) are explored, but not exhaustively across all studies.

# 7) Important Limitations

- **Generalizability to non-standard settings is limited:**  
  While coverage is strong for standard repeated PGGs with common parameterizations, the evidence is thinner for edge cases (e.g., one-shot games, extreme parameter values, non-anonymous punishment, all-or-nothing binary designs).

- **Indirectness in evidence for some dimensions:**  
  Several design features (e.g., contribution framing, full information, role/identity exposure) are not systematically varied, making it harder to model their marginal effect.

- **Payoff vs. behavioral outcomes:**  
  In some studies, increases in cooperation/contribution do not necessarily translate to net efficiency gains due to sanctioning costs (not always reported), especially when punishment is frequent or misapplied.

- **Cultural and group composition moderators:**  
  Substantial group or society-level variation is observed (Suleiman & Samid, 2021), but specific mapping from context variables to predictions is not always possible with available evidence.

- **Adjacency and context evidence are less useful for prediction:**  
  Results from coordination games, trust/bargaining games, and ethnographic/observational studies, while informative for mechanism understanding, provide only qualified or indirect guidance for quantitative treatment effect prediction in PGGs.

- **Lack of direct coverage for combined punishment and reward:**  
  The interaction of punishment and reward mechanisms—and the specifics of their design—remains only partially addressed.

- **Potential publication/selection bias:**  
  The literature may be skewed toward settings that are tractable and show clear effects; contexts where punishment fails or is counterproductive may be underreported.

---

In sum, the literature provides a strong, empirically grounded basis for predicting the direction and likely moderators of punishment’s effect on efficiency in typical repeated PGGs. However, the scope and transferability of detailed, quantitative prediction from some game design dimensions are limited by gaps in direct evidence and coverage. Careful interpretation and transparent uncertainty are warranted, especially for edge-case game designs or for environments unlike those studied in the laboratory tradition.
