# 1) Evidence Base

The literature base comprises a large and diverse set of papers (87 in total), with a substantial mix of **empirical experimental studies** (lab and field), **theoretical modeling**, and a smaller set of **conceptual reviews**. Among the most relevant, approximately 10–15 papers provide **direct empirical or theoretical evidence** about classic public goods games (PGGs) with manipulations of peer punishment and efficiency outcomes. Several additional papers model PGG variants or close analogs (e.g., common-pool resource games, repeated social dilemmas), focusing on adjacent mechanisms or group payoff. Many studies, however, are only contextually or behaviorally related (e.g., focusing on cooperation rates or punishment frequency, not efficiency per se). The paper set is broad in terms of mechanisms and settings, covering not just standard lab PGGs but also field experiments, networked games, and richer institutional variants.

**Strengths:**
- Multiple high-quality empirical lab and field experiments measuring group efficiency under control and punishment conditions.
- Robust theoretical analyses mapping parameter regimes where punishment does or does not improve efficiency.
- Explicit attention to institutional, design, and social moderators (e.g., group size, monitoring noise, exclusion, immunity, group composition).

**Limitations:**
- Some papers use behavioral proxies (contribution, cooperation rate, punishment assigned), with efficiency or payoff only inferred.
- Several adjacent studies analyze other game types or mechanisms (rewards, exclusion, indirect reciprocity, leader selection).
- Contextual and population diversity is discussed, but external validity remains a debated issue in the reviewed set.

# 2) Task Relevance

**Relevance to Prediction Task Dimensions:**

| Dimension                      | Coverage             | Summary                                                                                                                                          |
|--------------------------------|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| `pgg_or_variant`               | Exact/Close          | Strong empirical and theoretical coverage of classic and variant PGGs, with some studies on CPRs, ROSCAs, and donation games as close analogs.    |
| `punishment_or_sanctions`      | Exact/Close          | Many papers manipulate the presence/type/cost/technology of peer punishment or sanctions (including formal and informal, individual/democratic).  |
| `efficiency_or_related_payoff` | Exact/Close/Mixed    | Several studies measure efficiency (ratio to fully cooperative payoff) or total group payoff; others focus on contributions or non-payoff metrics.|

**Relevance Labels:**
- For the **core set** (e.g., Kamijo et al., 2020; Gordon & Puurtinen, 2021; Ertör-Akyazi, 2019; Ambrus & Greiner, 2019; Acemoglu & Wolitzky, 2021; Bühren & Dannenberg, 2021): **exact** relevance on all three criteria.
- For **CPR/ROSCA/auction models**: `pgg_or_variant` = close, `punishment` = exact, `payoff` = exact or close.
- For **network, reputation, or leader-driven models**: most are `adjacent` on PGG, `exact` or `adjacent` on punishment, and usually `adjacent` or `close` on payoff.
- Behavioral/mechanistic papers are mainly `adjacent` or `weak` on payoff.

**Summary**: The evidence base is **highly relevant** to the downstream task for standard public goods games with punishment and efficiency as outcomes; evidence thins for indirect designs, one-shot games, strong context/framing departures, or outcomes focusing heavily on behavior rather than payoffs.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes:**
- **Efficiency**: direct ratio of actual group payoff to the maximum payoff (full cooperation) (e.g., Kamijo et al., 2020; Gordon & Puurtinen, 2021; Ambrus & Greiner, 2019).
- **Total/group payoff**, **average earnings**, **welfare gains**, **profit**: used interchangeably with efficiency in many studies (e.g., Ertör-Akyazi, 2019; Wegmann & Musshoff, 2019; Koike et al., 2018).
- **Net profits**: sometimes specified separately from gross payoffs to emphasize the effect of punishment costs.

**Non-payoff behavioral outcomes:**
- **Contribution or cooperation rates**: nearly universal in all PGG studies, but not equivalent to efficiency if punishment/reward is costly (Lefebvre & Stenger, 2020; Bond, 2019).
- **Punishment frequency/intensity**: how often/to what extent punishment is used (Burton-Chellew & Guérin, 2021; Kamijo et al., 2020).
- **Norm compliance, reputation ratings**, or **exclusion occurrences**: less often directly linked to group payoffs.
- **Procedural/psychological outcomes**: e.g., perceived fairness, satisfaction, willingness to punish (Vollan et al., 2020; Turpie & Letley, 2021).

**Distinguishing note**: Several studies report increased contributions with punishment but show **no or negative effect on efficiency** due to the costs of punishment outweighing cooperation gains (Kamijo et al., 2020; Burton-Chellew & Guérin, 2021).

# 4) Main Findings Relevant To Prediction

**Synthesized findings (empirical and theory):**

- **Punishment and Efficiency:**
    - Enabling peer punishment in repeated linear PGGs **often increases efficiency** relative to control, especially when information is full, group size is moderate, and all can be punished; this effect is robust across symmetric/asymmetric cost structures (Gordon & Puurtinen, 2021; Ambrus & Greiner, 2019; Cui et al., 2019; Hintze et al., 2020; Murase & Baek, 2021).
    - **Costliness moderates the effect**: when punishment is expensive or frequently used, the efficiency gains can be wiped out by the added cost (Kamijo et al., 2020; Burton-Chellew & Guérin, 2021).
    - **Baseline efficiency is a strong moderator**: If control games already achieve high efficiency, adding punishment is likely to **reduce** or leave efficiency unchanged due to unnecessary punishment costs (Bühren & Dannenberg, 2021).
    - In **inefficient public goods** (MPCR < 1), punishment may **not** increase efficiency and can be neutral or negative, whereas rewards can still produce efficiency gains (Kamijo et al., 2020).
    - **Punishment efficacy depends on institutional design**: Democratic punishment (majority vote) reduces misapplication and anti-social punishment, leading to higher efficiency than dictator or individual punishment (Ambrus & Greiner, 2019). Anonymous/enabled immunity for some reduces efficiency.
    - **Framing/implementation** (e.g., penalty vs. purchase of rights; informal vs. formal) changes effectiveness (Ertör-Akyazi, 2019; Koike et al., 2018).
    - **Group composition and knowledge thereof** greatly moderate effects; punishment increases efficiency mostly when there is a need and expectation of free-riding, and reduces it in already cooperative, high-trust groups (Bühren & Dannenberg, 2021; Honjo & Kubo, 2020; Acemoglu & Wolitzky, 2021).

- **Theoretical mechanisms and exceptions:**
    - When punishment is misused for extortion, or when anti-social/hypocritical punishment dominates (i.e., used against cooperators), efficiency can be severely **reduced** (Barron & Guo, 2021; Burton-Chellew & Guérin, 2021).
    - **Unequal or selective punishment** (e.g., immunity or elite-only punishment) increases inequality and can lower overall welfare or efficiency for non-elites (Acemoglu & Wolitzky, 2021; Honjo & Kubo, 2020).
    - In **networked/structured populations**, effectiveness depends on local rules and social/norm enforcement architecture; in some cases leader-driven or cross-community sanctioning is much more effective (Wang et al., 2020; Ringsmuth et al., 2019; Wang & Guo, 2019).
    - In some CPR and ROSCA experiments, **exclusion (by voting) outperforms rule-based or costless punishment** in raising efficiency (Koike et al., 2018).

- **Effect sizes (where reported):**
    - Laboratory and field settings show efficiency improvements with punishment ranging from **non-significant** to as much as **8–15 percentage points**, especially when control efficiency is not already high (Wegmann & Musshoff, 2019; Gordon & Puurtinen, 2021; Ertör-Akyazi, 2019).
    - The addition of reward (especially net-positive rewards) can yield even larger efficiency gains than punishment, and sometimes remains effective even where punishment fails (Kamijo et al., 2020; Stoop et al., 2018; Chen et al., 2019).

# 5) Prediction Guidance

Based on the literature, the following **guidance applies for predicting treatment efficiency from game design variables and control efficiency** in standard/variant public goods games with enabled peer punishment:

- **Baseline efficiency** (control game) is a key reference: 
    - If control efficiency is **already high** (>80%), **adding punishment may reduce efficiency** due to unnecessary costs (Bühren & Dannenberg, 2021).
    - If control efficiency is **moderate to low** (50–75%), and group information/visibility is high, adding punishment **will often increase efficiency** (Gordon & Puurtinen, 2021; Ertör-Akyazi, 2019; Ambrus & Greiner, 2019).
    - If MPCR < 1 and cooperation is unprofitable, **do not expect a positive efficiency effect from punishment** (Kamijo et al., 2020).

- **Game design dimensions** that **increase the effect of punishment on efficiency** (all else equal):
    - **Visibility** of contributions/punishment actions, **identifiability** of free riders (full feedback).
    - **Symmetric applicability** (no immunity), ability for all to punish and be punished.
    - **Democratic sanctioning institutions** as opposed to individual/dictator (Ambrus & Greiner, 2019).
    - **Efficient punishment tech**: higher fine per unit cost (Hintze et al., 2020; Cui et al., 2019).
    - **Absence of communication** or lack of informal means of sustaining cooperation (else effects are smaller).
    - **Absence of framing or design features that erode the legitimacy/acceptability** of punishment (Ertör-Akyazi, 2019).

- **Dimensions that reduce/potentially reverse the effect:**
    - **High punishment cost relative to effect** (Kamijo et al., 2020).
    - **Immunity** or selective application (Acemoglu & Wolitzky, 2021; Burton-Chellew & Guérin, 2021).
    - **Group composition:** High cooperation baseline or known highly cooperative group, punishment adds costs (Bühren & Dannenberg, 2021).
    - **Collective/misapplied sanctions** (e.g., collective punishment or anti-social punishment) can lower both contributions and efficiency (Chapkovski, 2021; Barron & Guo, 2021; Honjo & Kubo, 2020).

- **Reward mechanisms** (if present) can outcompete or complement punishment in producing high efficiency, especially with positive return-to-reward cost ratios.

- **When evidence on a dimension is based on non-payoff outcomes** (e.g., only contribution rate), beware of inferring efficiency improvements if punishment is costly.

- **Prediction models** should thus take into account the interaction between baseline efficiency, group structure, information, punishment institution/cost/tech, and framing. Where design info is sparse, predictions should be conservative.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions** (frequent, quantitative, or nuanced evidence):
- `player_count`: All relevant studies specify group size (commonly 3-5).
- `num_rounds`: Repeated games are standard in experimental/theoretical work.
- `mpcr`: Central to nearly all analyses; effects are often mapped as a function of MPCR.
- `punishment_cost`, `punishment_tech`: Both cost and efficacy of punishment are experimentally manipulated and theoretically modeled.
- `punishment_exists`: Central treatment variable.
- `chat`: Manipulated in several studies (with/without), shown to strongly moderate efficiency (Ertör-Akyazi, 2019).
- `all_or_nothing`: Binary vs. continuous contributions are reported and often analyzed.

**Indirectly Informed Dimensions** (modeled/discussed, but with less direct evidence):
- `show_other_summaries`, `show_n_rounds`, `show_punishment_id`: Discussed in terms of feedback, accountability, and reputation, but not always manipulated independently.
- `punishment_tech`: Institutional design (individual vs. majority/democratic punishment) (Ambrus & Greiner, 2019).

**Contextually Discussed/Sparse Evidence**:
- `default_contrib`: Only occasionally referenced; not systematically varied.
- `reward_exists`, `reward_cost`, `reward_tech`: Well covered in studies of rewards but less so in studies strictly isolating punishment.
- Many studies note the possibility of endogenous selection into institutions but rarely experimentally manipulate default contribution.

**Effectively Missing**:
- No direct/multiple studies systematically manipulate `default_contrib`, and only a few manipulate public display of rounds/feedback (`show_n_rounds`, `show_other_summaries`) as primary variables.
- Details about heterogeneity in `show_punishment_id` and its effect on efficiency are sparse.

# 7) Important Limitations

- **Context and Framing Effects**: Several papers (and reviews) warn that external validity and context (cultural, population-specific, real vs. experimental stakes) strongly moderate behavioral and efficiency effects. Parallelism between game and real-world is not guaranteed (Naar, 2020).
- **Heterogeneity and Group Composition**: Many efficiency effects are contingent on the baseline cooperativeness of the group and the knowledge thereof—variables that may not be observable in advance in prediction contexts (Bühren & Dannenberg, 2021).
- **Punishment Misuse**: Efficiency gains depend on normatively appropriate application; anti-social, hypocritical, or extortionate use of punishment can reduce or reverse efficiency effects in some contexts (Barron & Guo, 2021; Burton-Chellew & Guérin, 2021).
- **Limited Direct Efficiency Measurement**: Despite the overall strong empirical base, many studies report only contribution rates or behavioral outcomes, requiring imputed effects or caution when mapping to payoff-based prediction.
- **Institutional Design Factors**: Fine-grained aspects such as punishment selection mechanisms, public vs. anonymous punishment, and cross-community sanctioning are not systematically manipulated across studies, so prediction across under-represented designs is more speculative.
- **Interaction Effects Underexplored**: Few studies probe higher-order interactions (e.g., punishment × chat × baseline efficiency × visibility), which limits the precision of cross-design predictions.
- **Sparse Evidence on Some Dimensions**: `default_contrib`, more complex feedback systems, detailed punishment/reward parameter interactions, and identification of sanction initiators are notably less studied.
- **Adjacency/Limited Transfer**: Some adjacent models (CPR, ROSCA, networked PD) provide suggestive but not directly translatable findings. Effects in small, one-shot, or highly asymmetric games may not generalize.

---

**Summary**:  
The literature base provides strong, multi-faceted evidence that peer punishment **often (but not always) increases efficiency** in repeated, transparent public goods environments, with the effect highly contingent on baseline cooperativeness, cost-effectiveness of sanctions, information availability, institutional design, and group composition. Prediction models should **incorporate these moderators** and avoid “one-size-fits-all” assumptions about punishment effects. When baseline efficiency is high or punishment is costly/misaligned, enabling punishment can reduce efficiency relative to control. Robust prediction of efficiency gains should draw wherever possible on **empirical estimates from similar game structures and control efficiencies**, and be cautious in out-of-sample or structurally novel settings.
