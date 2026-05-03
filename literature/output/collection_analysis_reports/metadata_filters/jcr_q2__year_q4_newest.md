# 1) Evidence Base

The paper set is extensive (170 items), interdisciplinary, and covers both empirical (laboratory, field, meta-analytic) and theoretical/computational studies. There is a significant proportion of lab and field experiments focused directly on public goods games (PGGs) and close variants, many of which explicitly compare conditions with and without punishment mechanisms. Key payoff-based outcomes (efficiency or group payoff) are reported in a substantial subset of papers, with other studies emphasizing behavioral outcomes (contribution rates, compliance, norm enforcement, etc.) or modeling evolutionary dynamics and mechanisms.

A significant body of theory supplements the empirical findings, addressing mechanism design, network/topological structure, and evolutionary stability of cooperation with punishment. However, a smaller but notable fraction of the literature is only contextually or adjacently related to the core prediction task (e.g., games with only reward mechanisms, trust/dictator games, or games reporting only behavioral outcomes).

Overall, the evidence base is both **broad and deep for the prediction task**, with many high-signal empirical studies and sophisticated theory, though some design dimensions remain less directly informed.

# 2) Task Relevance

**pgg_or_variant:**
- **Exact relevance**: Many papers directly study standard or canonical public goods games (e.g., linear PGGs, voluntary contribution mechanisms) with typical lab or field parameters.
- **Close relevance**: Several studies are in threshold public goods, CPR games, or “risk” variants, often seen as functional equivalents to PGGs.
- **Adjacent/weak**: Papers on two-player games (PDGs, trust/dictator games, etc.) or multi-agent simulations not framed as PGGs.
- **Coverage**: The set is rich in "exact" studies, with a meaningful subset in "close" CPR/threshold environments, and a large tail of "adjacent" studies.

**punishment_or_sanctions:**
- **Exact relevance**: Punishment, sanctions, or exclusion mechanisms are the explicit experimental manipulation in many papers, and diverse punishment technologies (peer, leader, institutional, ostracism, networked, etc.) are tested.
- **Close/adjacent**: Some papers address only rewards, only threat of punishment, or indirect mechanisms (e.g., reputation, withdrawal, partner choice) as proxies for punishment.
- **Coverage**: Strong for direct punishment variants; some relevant coverage of reward and hybrid mechanisms; many studies examine moderators (e.g., punishment cost, antisocial punishment).

**efficiency_or_related_payoff_outcome:**
- **Exact relevance**: Numerous studies and reviews directly report group efficiency (payoff normalized to maximum cooperation), total group earnings, or welfare as outcomes.
- **Close**: Outcomes such as group achievement in threshold games, resource stocks in CPR games, or average market earnings.
- **Adjacent/weak**: A significant proportion report only behavioral measures (contribution rate, compliance, punishment frequency), not efficiency.
- **Coverage**: Strong, but the behavior-payoff distinction is critical; in some cases reported group payoffs do not fully cover the efficiency spectrum required for prediction.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes**: Many empirical and theoretical studies report efficiency (as defined), total group payoff, average welfare, surplus, and, less frequently, related outcomes like "group achievement" in threshold games. Several provide values for both control and punishment conditions.
- **Non-payoff behavioral outcomes**: A considerable volume of studies report only contributions, cooperation rates, or punishment frequency. These are sometimes strongly correlated with efficiency but do **not** substitute for direct payoff measures.
- **Mixed reporting**: Some studies provide both (e.g., behavior and efficiency). In others, improved cooperation is fully offset by punishment costs, leading to negligible or negative efficiency effects.

# 4) Main Findings Relevant To Prediction

**Empirical Patterns:**
- **Enabling costly punishment typically increases cooperation rates** across designs (lab and field) (e.g., Zhang et al., 2024; Kamei, 2024).
- **Efficiency outcomes are heterogeneous**: In many standard lab PGGs, adding punishment increases group efficiency/payoff versus control (e.g., Kamei, 2024; Joseph et al., 2025; Jarungrattanapong, 2022; Wang & Huang, 2022; Zhang et al., 2024). However, there are robust findings where adding punishment **does not increase** or even **reduces efficiency** due to punishment costs outweighing the benefits (Botelho et al., 2022; Casari & Tavoni, 2024; Peng, 2022; Deng et al., 2025).
- **Punishment effectiveness depends on costs, targeting, and mechanism**: "Efficient" punishment mechanisms (low cost, high impact, targeted, or institutionalized) can drive efficiency close to optimal (Huang et al., 2024; Sun et al., 2025; Yang & Yang, 2024), while costly, poorly targeted, or antisocial punishment can negate or reverse gains (Botelho et al., 2022; Casari & Tavoni, 2024; Kim et al., 2025; Deng et al., 2025).
- **Punishment network structure matters**: Complete networks of punishers are not always better than incomplete ones; diffusion of responsibility or bystander effects can reduce punishment frequency and efficiency (Peng & Fan, 2023; Pi et al., 2022; Bühren et al., 2025).
- **Reward mechanisms and combined reward/punishment**: Sometimes reward alone is as or more effective than punishment and typically less welfare-reducing; optimal policy often uses minimal punishment and maximal reward (Huang et al., 2024; Yang & Yang, 2024; Sun et al., 2024; Pedrazzini et al., 2025 (review)).
- **Antisocial punishment, retaliation, and second-order punishment**: These phenomena can appear in peer-punishment designs, sometimes reducing or even reversing efficiency gains (Peng, 2022; Deng et al., 2025; Schaefer, 2023; Kim et al., 2025).
- **Heterogeneity in outcomes by context, culture, and game structure**: Cultural norms, player cognitive ability, and the presence of leaders or representatives moderate the effectiveness of punishment (Kim et al., 2025; Kamei et al., 2025). Pool punishment or higher-order punishment may work in some but not all societies.

**Theoretical Patterns:**
- **Thresholds and minimal effective punishment**: Theoretical work provides explicit formulas for the critical punishment needed to drive full cooperation and maximize efficiency (Huang et al., 2024; Yang & Yang, 2024). Above this, further punishment has little benefit and may reduce welfare.
- **Interaction with network/topological structure**: Small-world and structured networks can amplify the effect of punishment on efficiency, often allowing lower punishment to suffice (Cui et al., 2022; Lim & Capraro, 2022; Sun et al., 2025).
- **Dynamic and institutional punishment**: Tax-funded or dynamic/institutionalized mechanisms are often more efficient than voluntary/peer models (Yang & Yang, 2024; Sun et al., 2025; Kamei, 2024).

# 5) Prediction Guidance

- **When the control efficiency is low, and punishment is efficient (low cost/high impact, institutional/pool, or well-targeted), enabling punishment is likely to produce a large, positive effect on group efficiency under standard PGG conditions** (Kamei, 2024; Sun et al., 2025; Huang et al., 2024; Joseph et al., 2025).
- **If punishment is costly, poorly targeted, or antisocial punishment is prevalent (peer-punishment, high cost, opportunity for retaliation), gains in cooperation can be fully offset or overpowered by punishment costs, leading to unchanged or lower efficiency** (Botelho et al., 2022; Casari & Tavoni, 2024). This is particularly common in repeated or binary-action PGGs with high punishment cost or open retaliation channels.
- **The marginal per-capita return (mpcr) moderates gain size**: High mpcr makes cooperation more profitable; punishment is more likely to increase efficiency as defecting is more costly for the group.
- **Network and punishment structure**: Incomplete/targeted punishment networks (as opposed to all-to-all) can sometimes yield higher efficiency (Peng & Fan, 2023; Pi et al., 2022). Institutional settings (leader punishment, monitor, quorum voting) often yield higher efficiency than informal peer-to-peer sanctions.
- **Reward or combined reward-punishment designs may be superior**: If available, optimal policy typically uses maximum possible reward and minimal necessary punishment (Huang et al., 2024).
- **Effect of communication (chat) is typically to further increase cooperation and efficiency, sometimes independent of punishment (Ntuli et al., 2023; Jarungrattanapong, 2022 as no-chat; others with chat show higher baseline efficiency).**
- **Contextual caveats**:
    - In one-shot or short repeated interactions with high baseline cooperation, punishment may make little difference or even reduce efficiency (Botelho et al., 2022; Funk & Mischkowski, 2022).
    - In representation/leader settings, structure and communication strongly moderate efficiency gains (Kim et al., 2025; Zhang et al., 2024).
    - The cultural context and social norms are significant moderators; results from one country/group may not generalize (Kamei et al., 2025; Weber et al., 2023).
- **For prediction models**: The best efficiency predictions are achieved by referencing control efficiency, then adjusting the expected effect based on punishment parameters (cost, tech), mpcr, player count, network structure, and known moderators (chat, reward).

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions** (with multiple empirical/theoretical studies tying these to punishment efficiency impacts):
- `player_count` — widely manipulated and reported; group size can moderate both cooperation and the effect of punishment.
- `num_rounds` — effects on sustainability of cooperation and end-game behavior are noted; long games allow dynamic response to punishment.
- `mpcr` — critical moderator; higher mpcr generally means greater room for efficiency gains from punishment.
- `punishment_cost`, `punishment_tech` — major focus; cost/effect ratio is a primary driver of efficiency outcomes. Institutional vs. peer punishment and particulars of "who can punish whom" are often specified.
- `chat` — communication status frequently reported; enables higher baseline efficiency and can shift the effect of punishment.
- `reward_exists`, `reward_cost`, `reward_tech` — included in several studies examining reward, or joint reward/punishment mechanisms.
- `all_or_nothing` — binary vs. continuous contribution is common; binary sometimes associated with less robust gains from punishment, but evidence is mixed.
- `show_n_rounds`, `show_other_summaries` — round structure and information sharing/feedback are sometimes manipulated.
- `default_contrib` — only occasionally specified.
- `show_punishment_id` — rarely varied, but included in a few studies on transparency or identity.

**Indirectly/Contextually Discussed:**
- Game framing/heterogeneity, cognitive ability, or cultural context — important moderators, but not always specified as design dimensions.
- Network structure (complete vs. incomplete punishment connections), not parameterized as a standard dimension but shown to be crucial.
- Endogenous institution choice and voting — addressed in some experimental designs (Botelho et al., 2022).

**Effectively Missing/Sparse:**
- Some dimensions such as `show_punishment_id` are rarely manipulated except in targeted transparency studies.
- Effects of defaults (`default_contrib`), nuanced summary visibility (`show_other_summaries`), and identity mechanisms are limited to a few papers.

# 7) Important Limitations

- **Efficiency is not always reported**: Despite many studies on cooperation and punishment, a substantial subset report only behavioral (not payoff) measures, which can misstate actual efficiency impacts. Caution is required in inferring payoff effects from improved cooperation alone.
- **Parameter generalization risk**: The clearest results are for standard lab PGGs with small groups, moderate punishment costs, and no communication. Generalizing outside this regime (large groups, real-world settings, repeated overtime, severe heterogeneity, cultural differences) carries substantial uncertainty.
- **Antisocial punishment and retaliation effects**: Some designs see antisocial punishment, retaliation, or other inefficiencies that neutralize or reverse the efficiency gains from increased cooperation (Botelho et al., 2022; Casari & Tavoni, 2024; Deng et al., 2025); these are not easy to model without specific behavioral parameters.
- **Reward, communication, and voting not always manipulated**: The full interplay between punishment, reward, and communication/feedback is addressed in limited empirical studies. Models that ignore concurrent mechanisms may mispredict efficiency impact.
- **Complex/interacting moderators**: Cultural differences, cognitive ability, institution design, and group structure can strongly moderate outcomes but are not always parameterized in prediction-ready form.
- **Mechanism studies vs. quantitative prediction**: Some of the most nuanced mechanism analyses come from theory papers that provide clear insights on thresholds, stability, and formulae, but lack empirical validation or quantitative effect sizes for downstream models.
- **Long-term/dynamic or field outcomes**: Most experimental studies are short and lack ecological validity for sustained, real-world public goods challenges.

---

**Summary**:  
This literature base robustly supports the use of game design dimensions plus control efficiency for predicting punishment-enabled efficiency in standard laboratory PGGs and close derivatives. Punishment often increases efficiency when it is efficient (low cost, high impact, institutionally implemented), but can reduce or nullify efficiency—even as cooperation rises—when poorly targeted, antisocial, or costly. Predictive models should condition on the specific game design (especially punishment cost/tech, mpcr, network structure), anticipate important moderators, and not overweight contribution-rate results unless payoff implications are clearly established. Where evidence relies on non-payoff outcomes, this should be clearly flagged. Ambiguities and countervailing results (especially regarding punishment cost, antisocial punishment, and network structure) should remain explicit in any downstream use.
