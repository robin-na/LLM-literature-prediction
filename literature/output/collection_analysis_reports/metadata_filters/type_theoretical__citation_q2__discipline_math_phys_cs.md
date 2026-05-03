# 1) Evidence Base

**Mix and Scope:**  
The provided paper set is extensive, covering 230 theoretical and simulation-based papers (no empirical or experimental reports). Nearly all studies use agent-based modeling, evolutionary game theory, or analytical modeling of public-goods-game-like (PGG) or closely related social dilemma environments. There is a significant focus on payoff-based outcomes, but many papers prioritize behavioral outcomes (e.g., cooperation rates, punishment frequency) over group efficiency or welfare.

**Narrow vs. Broad for Prediction Task:**  
The evidence base is *broad and deep* in theory coverage for variations of the public goods game, the mechanics of punishment and sanctions (both peer and institutional), and evolutionary dynamics. It encompasses a wide range of game structures, sanctioning rules, participation options (voluntary/compulsory), network structures, and sanctioning costs/efficiencies. However, most outcomes reported are theoretical, and the fraction directly matching the prediction task (efficiency/total payoff as a function of design dimensions including punishment on/off) is modest compared to the total set. Empirical human group data are absent; all findings are theoretical/simulated.

# 2) Task Relevance

**a. PGG or Variant:**
- **exact:** The majority of papers model the standard linear/public goods game or close variants (e.g., voluntary participation, spatial PGG, threshold PGG, structured populations).
- **close/adjacent:** A sizable subset analyzes adjacent games (Prisoner's Dilemma, Snowdrift, donation, resource dilemmas), which are closely related but not always structurally identical to PGGs.
- **weak:** Some papers refer to generalized social dilemmas, bargaining, or trust games with only tangential relevance.

**b. Punishment or Sanctions:**
- **exact:** Many papers include explicit peer or institutional punishment mechanisms, with control/treatment designs directly relevant to the prediction task.
- **close:** Papers with exclusion, shunning, or meta-norms (second-order punishment) are included—these are close variants of punishment.
- **adjacent/weak:** Some analyze only reward, anti-social punishment, or environmental feedback, or study punishment analogues (e.g., ostracism, alliance strategies, resource-based penalties).

**c. Efficiency or Related Payoff Outcome:**
- **exact/close:** Only a subset directly measure efficiency (group total payoff relative to max possible under full cooperation), welfare, or group payoff in treatment vs. control.
- **adjacent:** Many report only behavioral outcomes (e.g., cooperation rates, strategy prevalence) or provide indirect indicators (e.g., average payoff per individual, resource levels, but no explicit efficiency ratio).
- **weak/none:** Some do not measure any form of efficiency or payoff, only behavior.

# 3) Outcomes Measured In The Literature

**Payoff/Efficiency-Related Outcomes (directly relevant):**
- **Group efficiency** (ratio of actual group payoff to all-cooperate scenario) is directly modeled in select papers (see e.g., Wang et al., 2019; Kol'veková et al., 2021; Liu et al., 2023; Cui et al., 2019; Zhuang et al., 2012; Powers, 2018; etc.).
- **Total earnings/welfare/mean group payoff** are reported in those same papers, often alongside behavioral outcomes.
- **Proxies** such as system growth rate, resource abundance, or achievement of collective welfare targets are used when explicit efficiency is not quoted.

**Behavioral/Non-Payoff Outcomes (less relevant, often reported instead):**
- **Contribution/cooperation rates**
- **Strategy frequencies (proportion of punishers, cooperators, defectors)**
- **Prevalence or survival of strategies**
- **Punishment frequency/intensity**
- Many studies treat these as primary outcomes and only discuss payoff tangentially or not at all.

**Clear distinction:** Notably, many theoretical studies imply efficiency outcomes based on behavioral dynamics, but do not calculate or report an efficiency metric per se.

# 4) Main Findings Relevant To Prediction

**General findings (from synthesis across directly relevant PGG+punishment+efficiency papers):**
- **Enabling punishment typically increases group efficiency compared to control (punishment-disabled) when:**
    - Punishment is effective (defector loss per unit cost is high),
    - Punishment cost is low/moderate,
    - There are strong monitoring or detection mechanisms (reputation, institutional support, etc.),
    - Social structure supports punishment (e.g., optionally with voluntary participation or entry fees),
    - Participation is voluntary, allowing defectors/non-punishers to self-exclude (Sasaki, 2014; Wang et al., 2015).

- **Magnitude of efficiency gain depends strongly on:**
    - Relative cost/impact of punishment (ratio of fine to cost),
    - Game structure (group size, number of rounds, spatial/network structure, feedback mechanisms, presence of loners),
    - Whether punishment is institutional or peer-driven (institutional can prevent second-order free-riding more robustly).

- **Mixed and parameter-dependent effects:**
    - If punishment is too costly relative to its impact, efficiency gains are nullified or reversed (Liu et al., 2024; Liu et al., 2023; Cui et al., 2019).
    - If anti-social punishment or retaliation is possible and not deterred, punishment can reduce efficiency (Wolff, 2012; Zhang & Pei, 2022; Quan et al., 2019).
    - Excessively strong or weak punishment can either backfire (crowd out cooperators, kill participation) or be ineffectual, with intermediate levels often optimal (Lv et al., 2023; Nuño et al., 2010).

- **Reward versus punishment:**
    - Reward mechanisms often increase efficiency more than punishment when intervention cost is held equal, but are less robust without strong institutional support; combined mechanisms are frequently optimal (Zhuang et al., 2012; Cong et al., 2016; Yao & Chen, 2014).

- **Network and group structure:**
    - Structured populations (spatial, networked) can support cooperation and efficiency at lower punishment thresholds, but in some models, well-mixed populations outperform structured ones at high punishment effectiveness (Wang & Lv, 2019).
    - High network connectivity and more opportunities for sanctioning often make punishment more effective at improving efficiency (Chung et al., 2013; Podobnik et al., 2019).

- **Institutional context, reputation, and monitoring:**
    - Reputation systems and information flow are critical moderators: punishment is only effective at increasing efficiency when actions are observable (De Silva & Sigmund, 2009; Kang et al., 2024).
    - Institutional (tax-based) punishment can avoid free-rider problems and maintain high efficiency more stably than decentralized peer punishment, especially in dynamic or anonymous settings (Yao & Chen, 2014; Wang et al., 2011).

- **Moderators and caveats:**
    - Introduction of bribery, corruption, or meta-punishment significantly complicates the efficiency outcome (Fang et al., 2020; Yamamoto & Okada, 2016).
    - Efficiency effects may be strongly dependent on initial behavioral conditions due to bistability/multiple equilibria (Liu et al., 2024; Nuño et al., 2010).
    - When punishment costs are paid collectively or are endogenous/declining (shared-punishment, endogenous-voting), efficiency improvements are larger and more stable (Kol'veková et al., 2021; Wang & Lv, 2019).

**Adjacent and indirect findings:**
- Many studies that only report cooperation rates or behavioral prevalence nevertheless conclude that enabling punishment increases cooperation, which (in PGGs) usually translates into higher efficiency, unless counteracted by high punishment costs or meta-dynamics.

# 5) Prediction Guidance

- **Direct prediction:**
    - *Baseline effect*: Expect enabling (effective, not overly costly) peer punishment in a PGG-like environment to increase average efficiency compared to the same design with punishment disabled, provided other conditions (such as excessive anti-social punishment, very high cost, or high corruption) are not present.
    - *Magnitude modulation*: The efficiency boost is larger when the control game is inefficient (defection is prevalent), the MPCR is high, group size is moderate or large, punishment cost is low, and punishment impact per unit cost is high. If control efficiency is already high, the marginal efficiency gain may be small or negative due to punishment costs.
    - *Context matters*: The positive effect is undermined or eliminated when punishment is too costly, weak, or when anti-social punishment/retaliation/corruption is prevalent.

- **Dimension-specific insights:**
    - *Player count*: Larger groups generally need less punishment strength to sustain cooperation (Sasaki, 2014); effect of punishment on efficiency more robust as group size increases, though very large groups may not benefit if monitoring/punishment becomes impractical.
    - *MPCR*: Higher MPCR amplifies the effectiveness of punishment; at low MPCR, even strong punishment may not yield high efficiency (Zhuang et al., 2012; Cui et al., 2019).
    - *Punishment cost and tech*: Efficiency improvements require the fine to defectors to be significantly larger than cost to punishers (frequently, fine-to-cost > 1); too high a cost negates or reverses the benefit (Lv et al., 2023; Nuño et al., 2010).
    - *Participation and entry (voluntary, entry fee)*: Optional participation and/or small entry fees can synergize with punishment to produce high efficiency (Wang et al., 2015; Wang et al., 2011).
    - *Reward exists*: The addition of reward can, in some models, further increase efficiency beyond punishment alone, or even substitute for punishment when punishment is not viable (Cong et al., 2016; Yao & Chen, 2014).
    - *Institutional context*: Institutional and tax-based punishment generally outperform peer punishment in sustaining high efficiency (Yao & Chen, 2014).
    - *Retaliation/anti-social punishment*: If retaliation or anti-social forms are prevalent, or unconditionally possible, the predicted efficiency gain may not occur (Wolff, 2012).

- **From non-payoff behavioral outcomes:**
    - If only cooperation rates or strategy frequencies are reported, an increase in cooperation due to punishment usually implies higher efficiency in standard PGGs, unless the cost of punishment is unusually high or other mechanism decouples contribution and group payoff (Zhang & Pei, 2022).

- **Quantitative prediction:**
    - Only a few models provide explicit efficiency formulas or mappings; in other cases, qualitative magnitude should be inferred using the above moderators.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions (explicitly modeled and influential for efficiency prediction):**
- `player_count`: Most models examine effects of group size.
- `num_rounds`: Many evolutionary models correspond to large or infinite rounds; explicit round effects are reported in some threshold games.
- `all_or_nothing`: Frequently modeled; continuous and binary contribution rules are both studied.
- `mpcr`: Always a key moderator; higher MPCR = more potential for efficiency gains from punishment.
- `punishment_cost`, `punishment_tech`: Heavily studied; cost/impact ratio is critical for outcome prediction.
- `punishment_exists`: Directly toggled in almost all models focused on the punishment intervention.
- `reward_exists`, `reward_cost`, `reward_tech`: For models including joint reward-punishment schemes.
- `punishment_tech`: Sometimes termed punishment magnitude.
- `player_count` and social/network structure: Both direct group size and interaction topology are regular moderators.
- `reward_exists`: Where present, often studied in direct comparison to punishment.

**Indirect/contextually discussed or occasionally missing dimensions:**
- `chat`: Rarely modeled directly; some models discuss communication or information/reputation flow (as via `show_other_summaries` or `show_punishment_id`) as proxies.
- `default_contrib`: Only a handful of studies distinguish opt-in/opt-out framing.
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Sometimes referenced in reputation or observability discussions, but rarely parameterized except for explicit reputation-based or information-rich settings.
- `punishment_tech`: In some models, equivalent to fine per unit cost, but usage is uneven.

**Dimensions effectively missing or underdeveloped:**
- `chat`: Direct, real-time free-form chat is essentially absent.
- `default_contrib`: Opt-in vs opt-out framing is almost never manipulated (only implied in a few papers).
- Dimensions capturing UI/feedback (e.g., `show_n_rounds`, etc.) are absent except as high-level information structure.

# 7) Important Limitations

- **Empirical Gap:** The entire evidence base is composed of theory and simulation; absence of laboratory or field experimental data means that real-world behavioral deviations, noise, and unmodeled psychological effects are untested.
- **Outcome Reporting:** Many models report only cooperation rates or strategy frequencies; direct efficiency or group payoff reporting is less common, requiring inference.
- **Heterogeneity of Model Structures:** Model assumptions (e.g., infinite vs. finite population, update rule, spatial vs. well-mixed, voluntary vs. compulsory participation) vary widely and are not always explicitly matched to prediction contexts.
- **Simplifying Mechanisms:** Many models ignore or stylize away empirical details (e.g., bounded rationality, perception errors, non-linear cost structures, mixed-motive institutions, psychological factors).
- **Anti-social punishment and retaliation:** Few models systematically account for these destructive forms, but those that do suggest their presence can undermine positive effects of punishment.
- **Parameter Sensitivity and Bistability:** Many findings are parameter- or initial-condition-dependent; effects of punishment can be multi-modal (i.e., both high and low-efficiency equilibria are possible).
- **Sparse coverage of some dimensions:** UI variables, communication (chat), and detailed cognitive/strategic framing are rarely modeled, limiting transferability to some experimental game designs.
- **Generalizability Beyond Model Structure:** Transfer from infinite/large-population, evolutionary dynamics to small real-life groups and short time horizons should be cautious.

---

**In summary**, this literature set provides strong, primarily theoretical support for the prediction that enabling (cost-effective, well-designed) punishment will, in a wide range of PGG-like settings, increase group efficiency relative to a control with punishment disabled. The effect depends critically on the cost-effectiveness of punishment, the structure of the population, the presence of alternative incentive mechanisms (reward, entry fees), and initial behavioral states. However, due to the modeling focus and lack of direct experimentation, predictions should be framed with attention to the specifics of each design dimension, and with awareness of the possibility of negative or ambiguous effects when moderators such as high punishment cost, anti-social punishment, or corruption are present.
