# 1) Evidence Base

The literature set is broad and heavily empirical, with a strong focus on experimental laboratory studies and several field or framed field experiments, as well as a few reviews and observational studies. The vast majority are directly focused on public goods games (PGGs) or very close variants, with experimental manipulations of peer punishment and/or sanctions, and with reported outcome measures relevant to group efficiency or payoff. A significant minority address adjacent settings (e.g., common-pool resource games, trust/investment games with punishment, or exclusion-based sanctions), and a smaller set deal with psychological mechanisms or real-world observations related to sanctioning.

Empirical results dominate, with only occasional theoretical or mechanism arguments. A substantial number of studies report direct group payoff, efficiency, or welfare outcomes. The paper set is relatively strong and well-aligned with the downstream prediction task, though it contains some studies where the primary outcomes are behavioral rather than payoff-based.

# 2) Task Relevance

**pgg_or_variant:**  
- **Exact relevance**: Most papers experimentally study standard linear PGG/VCM designs or extremely close variants (e.g., Casari & Luini, 2009; Sefton et al., 2007; Arechar et al., 2018). Several others focus on collection-action, common-pool, or cooperation games with strong structural similarity (Casari & Plott, 2003; Ostrom, 2006).  
- **Close or adjacent**: A subset examine adjacent games (e.g., trust/investment, leader-based reward, exclusion, or social disapproval), which are relevant for understanding mechanisms but are not direct PGGs (Rigdon, 2009; van der Heijden et al., 2009; Charness & Yang, 2014).

**punishment_or_sanctions:**  
- **Exact relevance**: The studies provide comprehensive coverage of peer punishment (punishment_exists, punishment_cost, punishment_tech), including material and social sanctions, exogenous and endogenous rules, and both individual and collective punishment mechanisms. Empirical variation in punishment technology is well-represented.  
- **Close or adjacent:** Some studies focus on exclusion as sanction, ostracism, reputational and social disapproval, or third-party punishment, which are relevant but not always direct peer monetary punishment. These inform the broader class of sanction-based interventions.

**efficiency_or_related_payoff_outcome:**  
- **Exact**: Approximately half the studies report efficiency or group payoff as a main outcome, directly supporting the prediction task (e.g., Sefton et al., 2007; Arechar et al., 2018; Kroll et al., 2007).  
- **Close or adjacent**: Many others report only contribution rates, cooperation frequencies, or non-payoff behaviors, but discuss payoff effects qualitatively. Inferences from these are possible but less precise.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes** (directly useful for prediction):  
- Group efficiency (earnings as a % of social optimum), total group payoff, welfare, surplus, individual earnings.
- Many studies provide clear quantitative comparisons between control (no-punishment) and treatment (punishment-enabled) efficiency.

**Non-payoff behavioral outcomes** (less direct for prediction, but may indicate direction of payoff effects):  
- Contribution rates, cooperation rates.
- Frequency and intensity of punishment, anti-social/perverse punishment occurrence.
- Norm compliance, intention observability, communication acts.
- Emotional or reputational responses (e.g., social disapproval, perceived fairness).

It is critical to distinguish that a higher contribution rate does not always result in higher group efficiency because punishment (even if promoting contributions) itself incurs costs that can offset welfare gains.

# 4) Main Findings Relevant To Prediction

**Synthesis of Empirical Results:**

- **Typical Effect of Enablement:** In standard repeated PGGs with peer punishment, enabling punishment usually leads to:
  - Sustained higher contributions and a clear increase in group efficiency, especially after initial costly punishment phases (Sefton et al., 2007; Arechar et al., 2018; Fehr et al., 2002; Kroll et al., 2007; Noussair & Tucker, 2005).
  - The efficiency gains are robust across laboratory and online environments with similar design dimensions.
  - The cost structure of punishment is crucial: high-impact/low-cost punishment produces larger efficiency gains, while high-cost or anti-social punishment can negate efficiency benefits (Casari & Luini, 2009; Decker et al., 2003).

- **Moderators and Exceptions:**
  - **Punishment Institution:** Collective or consensus-based punishment can reduce anti-social (perverse) punishment, increasing net efficiency (Casari & Luini, 2009). Individual open punishment sometimes leads to high costs and negligible or negative net efficiency gains if anti-social punishment is common.
  - **Communication:** Enabling free-form communication alone can match or exceed the efficiency effect of punishment. In such settings, adding punishment confers little additional benefit, as chat already sustains cooperation and high efficiency (Bochet et al., 2006; Oprea et al., 2014).
  - **Group Heterogeneity:** Efficiency gains from punishment are much lower in groups with heterogeneous MPCR or valuations, and may even increase inequality (Reuben & Riedl, 2009; Kölle, 2015; Tan, 2008).
  - **Punishment Revenge/Feuds:** If the punishment mechanism enables retaliatory spirals (feuds), the positive effect on efficiency is reduced or can become negative (Nikiforakis & Engelmann, 2011).
  - **Exclusion/Ostracism:** Similar gains in efficiency can be achieved via ostracism or exclusion, often with lower cost than direct monetary punishment (Maier-Rigaud et al., 2010; Charness & Yang, 2014).
  - **Institutional Design & Technological Parameters:** Efficiency increase is sensitive to punishment impact per cost, group size, MPCR, rounds, observability, and whether punishment identities are shown. High punishment effectiveness and visibility of punishment reputation yield stronger positive effects (Nikiforakis et al., 2010; Rigdon, 2009).

- **Temporal Dynamics:**
  - In most settings, punishment costs outweigh efficiency gains in the early rounds, but as cooperation is stabilized, net efficiency overtakes control in later rounds. The transition point varies by institution and design (Sefton et al., 2007).

# 5) Prediction Guidance

- **Direct Application:** Where available, empirical studies matching the queried game's design dimensions (especially player_count, num_rounds, mpcr, punishment_cost, punishment_tech) should be weighted most. For these cases, the average efficiency in the punishment-enabled game exceeds the control, typically after an initial adaptation phase.
  - **Magnitude:** With typical PGG parameters (4-5 players, MPCR=0.4-0.5, 10-20 rounds, punishment cost:impact 1:3 or higher), expect a substantial (10-40 percentage point) increase in efficiency. Effects may be larger if control game efficiency is low and punishment is highly effective and prosocial.
  - **Conditionality:** Efficiency gains depend critically on the institutional details—anti-social punishment, high punishment costs, or feuding opportunities can substantially dampen or reverse gains; consensus or filtered punishment, high impact per cost, and minimal revenge pathways amplify positive effects.
- **Role of Control Efficiency:** If control efficiency is already high (due to, e.g., communication or strong social norms), the incremental gain from adding punishment may be modest; if very low, the gain is likely more pronounced, but not guaranteed if punishment is expensive or misused.
- **Design Dimensions:** Prediction should attend closely to punishment_cost, punishment_tech, visibility/observability parameters (show_punishment_id), communication (chat), group heterogeneity (mpcr, default_contrib, reward_exists), and institutional form (all_or_nothing, consensus rules). Indirectly discussed dimensions (e.g., show_other_summaries, show_n_rounds) have less empirical backing.
- **Transferability:** While adjacent game studies provide support for the generality of the mechanisms (e.g., trust/investment games, CPR games), quantitative forecasts are most accurate when based on exact or close PGG data. Exclusion/ostracism functions similarly to monetary punishment in terms of efficiency effects, but details on when this comparability holds are sparse.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**
- **player_count, num_rounds, mpcr, all_or_nothing, punishment_cost, punishment_tech:** Extensively manipulated and analyzed in the core empirical studies. The effect of punishment on efficiency is well-documented as a function of group size, length, marginal return, type and cost of punishment.
- **chat (communication):** Frequently studied; its presence often moderates or even outweighs the effect of punishment on efficiency.
- **reward_exists, punishment_exists:** Several papers compare reward, punishment, and combined regimes, finding rewards alone are rarely sufficient; the joint institution yields the highest efficiency only if punishment is part of the mix.
- **show_punishment_id, show_other_summaries:** Some coverage; the visibility of punishment or punisher ID can affect the prevalence and effectiveness of punishment (e.g., possibility of revenge or reputation-based enforcement).
- **default_contrib, show_n_rounds:** Occasionally varied but less often systematically analyzed. Show_n_rounds (known horizon) is standard in most experimental designs.

**Indirectly Informed/Contextually Discussed:**
- **punishment_tech (effectiveness of punishment), reward_cost/reward_tech:** Discussed as moderators but not always systematically varied.
- **show_other_summaries:** Sometimes included as information feedback; the effect on efficiency in the presence of punishment is more often taken as a given.
- **default_contrib:** Rarely a treatment variable.

**Effectively Missing:**
- Several dimensions are not systematically reported across studies, including default_contrib and, in a systematic way, show_n_rounds, though most experiments make the round horizon known.
- Discussion of player matching protocols, endowment variance, and finer-grained reward mechanics is less common.

# 7) Important Limitations

- **Scope of Empirical Evidence:** Not all payoff-related outcomes are present for every design dimension, and the majority of evidence is from laboratory settings with standard N (4-5) and round counts (10-20). There is less evidence for large groups, extremely high/low MPCR, or rare design permutations.
- **Absence of Nonlinear/Complex Designs:** Most studies use linear PGGs; non-linear returns, variable group sizes, and field variants are less represented.
- **Ambiguity in Heterogeneous or Field Contexts:** Evidence is sparser and more ambiguous for games with strong player heterogeneity (e.g., unequal MPCR or capabilities) or in naturalistic, field contexts, where efficiency gains from punishment may be attenuated or mixed.
- **Behavioral vs. Payoff Outcomes:** Some highly cited findings (e.g., strong increases in contribution rate) only imply, but do not guarantee, increases in efficiency. Across the set, efficiency can be reduced by high punishment costs or prevalence of anti-social (perverse) punishment.
- **Moderating Role of Feud/Revenge:** The design dimensions enabling identity revelation and repeated retaliation can flip the sign of the effect; many laboratory games artificially block these pathways.
- **Combined Institutions and Social Mechanisms:** Communication, social disapproval, exclusion, or reputation mechanisms can enhance or even supplant the role of material punishment—and sometimes do so at lower cost.
- **Measurement and Reporting Variation:** Some studies estimate efficiency only indirectly (from contribution rates), limiting precision in quantitative prediction.
- **Underreporting of Rare Design Components:** Some prediction-relevant dimensions (e.g., default contribution framing, detailed info feedback) are underreported or rarely isolated as treatment variables.

---

## **Summary Table: Design Dimension Coverage**

| Dimension                | Evidence Strength      | Example Key Sources                         |
|--------------------------|-----------------------|---------------------------------------------|
| player_count             | Direct/Informed       | Sefton et al., 2007; Fehr et al., 2002     |
| num_rounds               | Direct                | Arechar et al., 2018; Bochet et al., 2006  |
| chat                     | Direct context/mod.   | Bochet et al., 2006; Oprea et al., 2014    |
| all_or_nothing           | Direct/Partial        | Kroll et al., 2007; Kölle, 2015            |
| default_contrib          | Sparse                | Few/no direct tests                        |
| mpcr                     | Direct/Moderator      | Fehr et al., 2002; Casari & Plott, 2003    |
| punishment_cost          | Direct/Key Moderator  | Casari & Luini, 2009; Nikiforakis et al., 2010 |
| punishment_tech          | Direct/Key Moderator  | Rigdon, 2009; Nikiforakis et al., 2010     |
| reward_exists            | Direct/Compared       | Sefton et al., 2007; Choi & Ahn, 2013      |
| reward_cost/tech         | Indirectly            | Sefton et al., 2007; sparse                |
| show_n_rounds            | Contextually          | Most studies fixed, not manipulated         |
| show_other_summaries     | Indirect/Sparse       | Some included (feedback), minor attention   |
| show_punishment_id       | Partial/Critical      | Nikiforakis & Engelmann, 2011              |

---

**In conclusion**, this literature set provides robust empirical support for predicting that, in public-goods-game-like settings, enabling peer punishment generally increases efficiency above control, but the effect is strongly conditional on institutional design, effectiveness and cost of punishment, the prevalence of anti-social punishment or revenge, and the presence of alternative cooperation-enhancing mechanisms (especially communication). Direct studies of variants closely matching the 14 design dimensions should be prioritized in prediction, while caution is warranted in generalizing from adjacent settings or behavioral-only outcome studies.
