# 1) Evidence Base

The paper set is **broad and heavily empirical**, with the majority of included items being laboratory or field experiments using **(variants of) the standard public goods game (PGG)** framework. Most studies directly compare game designs that enable or disable **peer or institutional punishment** and report **payoff-related outcomes**, primarily **group efficiency, group payoff, total earnings, or social welfare**. A significant minority of papers are theoretical, providing formal models or mechanism arguments, while others focus on adjacent games (CPR, trust, club goods) or on behavioral (non-payoff) outcomes such as contribution rates or norm compliance.

The empirical papers report a **high diversity of environments and design dimensions**, with substantial attention to **punishment institution details (peer vs. centralized, cost and effectiveness, observability, monitoring regime)** and often report both **control (no-punishment)** and **treatment (punishment-enabled)** conditions, allowing for direct effect estimation. A number of field experiments and lab-in-the-field studies add ecological validity. Some studies focus on group heterogeneity, social context (ethnicity, group composition), or communication, while a smaller subset focus on related but not direct PGG variants.

Overall, the evidence base is **strong and directly relevant for the downstream prediction task**, though key limitations include heterogeneity in reporting standards (not all studies report group efficiency explicitly) and gaps in coverage for some game design dimensions.

---

# 2) Task Relevance

- **PGG or Variant**
  - **exact**: The majority of the covered literature—especially the core experimental papers—study standard or near-standard public goods games (Lee & Min, 2021; Angelovski et al., 2018; Mantilla et al., 2021; Waichman, 2020; Fatas et al., 2020, etc.). Some studies involve close variants (CPR, threshold PGGs, or club goods) and are labeled as **close**.
- **Punishment or Sanctions**
  - **exact**: Most empirical papers manipulate the presence, type, or structure of punishment. Both peer and centralized/institutional punishment institutions are studied. Some studies focus on endogenous institution choice. A minority focus on adjacent mechanisms (minimum contribution rules, exclusion, reward, etc.—labeled as **adjacent**), and several specifically study anti-social or misapplied punishment.
- **Efficiency or Related Payoff Outcome**
  - **exact/close**: The main cluster of relevant studies report efficiency, group payoff, social welfare, or closely related outcome measures as primary or secondary outcomes. Other studies only discuss payoff-related outcomes indirectly (e.g., by implication from contribution results) or focus mainly on behavioral metrics (**adjacent** or **weak**).
  
In summary, with respect to the **downstream task of predicting efficiency changes from the design and control efficiency**, the literature is **highly relevant and rich on all three dimensions**, but with some variation in outcome reporting and directness of evidence.

---

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes (Central to Prediction):**
  - **Efficiency** (group payoff as a fraction of the maximum possible): Directly measured in most core PGG punishment papers.
  - **Group payoff / total earnings / welfare / surplus**: Often reported directly and often interchangeable for purposes of normalized efficiency comparisons.
  - **Related earnings (for subgroups: sanctioners, punished, high/low endowment)**: Explored in studies examining heterogeneity or institutional structure.

- **Non-Payoff Behavioral Outcomes (Not Efficiency)**
  - **Contribution rate / cooperation rate:** Widely reported, sometimes as a proxy for efficiency, but **not necessarily correlated** in presence of costly punishment, as increased contributions can come alongside high punishment costs that harm efficiency (Bühren & Dannenberg, 2021; Fatas et al., 2020).
  - **Punishment frequency/allocated punishment**, **antisocial punishment**, **compliance with norms**: Studied as mechanisms or moderators, not as direct payoff outcomes.
  - **Norm emergence, group identification, willingness to sanction**: Inform mechanism understanding but not efficiency.

- **Adjunct Outcomes:**
  - **Inequality** (sometimes studied jointly with efficiency, especially in the context of punishment distribution).

**Explicit distinction is made in the empirical papers between behavioral effects and payoff efficiency; several papers (e.g., Drouvelis et al., 2021; Vollan et al., 2019) show that behavioral changes do not always translate into efficiency gains if punishment is misdirected, antisocial, or excessively costly.**

---

# 4) Main Findings Relevant To Prediction

## Empirical Patterns:
- **Punishment often increases efficiency relative to control, but not always.**
  - In canonical lab PGGs (4–5 players, 10–20 rounds, continuous contributions, no chat), **enabling peer or centralized punishment reliably increases efficiency/group payoff** compared to no-punishment controls, especially when punishment is moderately costly and efficiently targeted (Angelovski et al., 2018; Dutta & Modica, 2021; Cobo-Reyes et al., 2019; Castillo et al., 2021).

- **Efficiency effect of punishment is highly context- and design-dependent.**
  - **Social/ethnic heterogeneity**: In-group favoritism and ethnic diversity reduce or reverse the efficiency gain from punishment because deterrence suffers (Mantilla et al., 2021; Drouvelis et al., 2021).
  - **Information structure**: Punishment boosts efficiency when group members can observe and target free riders (complete info on contributions/endowments); with incomplete info, efficiency gains disappear or reverse (De Geest & Kingsley, 2021, 2019).
  - **Punishment institution**: Democratic or centralized punishment regimes outperform individual or dictator mechanisms in terms of efficiency, mostly by minimizing antisocial punishment (Ambrus & Greiner, 2019; Castillo et al., 2021).
  - **Network structure**: Hierarchical or complete networks favor efficient punishment, while line/circle structures foster antisocial punishment and lower efficiency (Fatas et al., 2020).
  - **Group composition/cooperativeness**: In high-cooperation groups (control already near-optimal efficiency), enabling punishment **reduces efficiency** due to its cost; in low-cooperation contexts, punishment can strongly boost efficiency (Bühren & Dannenberg, 2021).
  - **Endogenous institution choice**: Allowing groups to vote on punishment/monitoring regimes increases both efficiency and compliance compared to exogenous imposition (Cobo-Reyes et al., 2019).
  - **Feedback and observability**: Efficient punishment depends on clear linkages between observed contributions and the experience of being punished (Waichman & Stenzel, 2019).
  - **Emotional/contextual factors**: Emotional induction (anger vs. happiness) moderates the effect; with happiness induction, punishment can reduce efficiency (Lee & Min, 2021).

- **Punishment can also harm efficiency:**
  - **Antisocial and retaliatory punishment**: Peer punishment is often subject to misuse (punishing high cooperators or retaliation cycles), eroding or eliminating efficiency gains (Vollan et al., 2019; Fatas et al., 2020; Drouvelis et al., 2021).
  - **High punishment costs**: If the cost of punishment is high, efficiency gains disappear or reverse, even if contributions increase (Bühren & Dannenberg, 2021).
  - **Defective institution design**: Pool punishment with poorly structured incentives can be seen as indirect free riding and reduces efficiency compared to fixed payment regimes (Angelovski et al., 2018). "Whistleblowing" as group-level punishment can be destructively inefficient (Makowsky & Wang, 2018).
  - **Imperfect monitoring/endogenous monitoring collapse**: When monitoring is endogenous and costly (requiring consensus/group contribution), peer punishment is robust, but group monitoring may collapse—punishment then doesn't improve efficiency (DeAngelo & Gee, 2020).
  - **Certain threshold public goods and extraction games**: In threshold/CPR settings, internal peer punishment can increase compliance but reduce efficiency due to costly punishment and antisocial cycles (Vollan et al., 2019; De Geest & Stranlund, 2019).

## Theoretical Insights:
- **Punishment's effect on efficiency is non-monotonic:** Too much coercion or highly unequal application leads to efficiency loss or high inequality (Acemoglu & Wolitzky, 2021; Barron & Guo, 2021).
- **Critical moderators include:**
  - **Structure of who can punish and be punished**
  - **Visibility and reputation effects**
  - **Speed and flexibility of institutional responses**
  - **Support/incentivization for punishers (Brandt & Svendsen, 2019)**

## Control Efficiency as a Moderator:
- **Baseline (control) efficiency predicts possible returns from punishment:** When the control condition already achieves near-optimal efficiency, punishment introduces unnecessary cost and reduces efficiency. When control efficiency is low, properly designed punishment can yield large relative gains (Bühren & Dannenberg, 2021).

---

# 5) Prediction Guidance

## Quantitative Implications:
- **If control (no-punishment) efficiency is low to moderate and design matches canonical PGG parameters (4–5 players, 10–20 rounds, anonymous, observable, moderate MPCR and punishment cost), prediction should be a strong efficiency gain from enabling punishment** (Dutta & Modica, 2021; Angelovski et al., 2018; Ambrus & Greiner, 2019).
- **If control efficiency is already high, expect punishment to reduce efficiency** due to unnecessary cost (Bühren & Dannenberg, 2021).
- **Institutional and group context should be integrated into the prediction**:
  - **Ethnic or social heterogeneity, opportunity for antisocial punishment, ambiguous norm identification, or unobservable differences** (in endowment or ability) sharply reduce or negate positive efficiency effects (Mantilla et al., 2021; De Geest & Kingsley, 2021).
  - **Democratic, peer-verified, or centralized institutions that minimize antisocial punishment and ensure punishment accuracy** predict higher efficiency boosts than individual or dictator regimes (Ambrus & Greiner, 2019).
- **Punishment cost and technology (cost-to-impact ratio)**: Within tested ranges, moderate punishment cost (e.g., 1:3 cost-impact) is effective, but high cost can make efficiency gains elusive.
- **Communication/chat**: Presence of chat or communication mechanisms often improves efficiency independently or synergistically with punishment (Koch et al., 2021; Kamei, 2019).

## Prediction Formula Guidance:
> **Predicted efficiency with punishment enabled = Control efficiency + (delta contingent on: design parameters, baseline efficiency, institution structure, group composition, observability, punishment cost/tech, possibility of antisocial punishment, and info clarity).**
>
> The delta (efficiency gain or loss) is *positive* and large when canonical lab PGG design is used with clear info and efficient institutions; *zero or negative* when group is highly cooperative already, antisocial punishment is present, info/punishment targeting is noisy, or group is highly heterogeneous or divided.

## Uncertainty:
- The net effect of punishment on efficiency is **ambiguous in some design regimes** (heterogeneous endowments, high ethnic diversity, high punishment cost, destructive or group-level punishment). **Prediction should reflect increased uncertainty (e.g., wider confidence intervals) under those dimensions.**

---

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**
- `player_count`: Almost all studies specify and often examine effects across different sizes.
- `num_rounds`: Standardized in most studies; repeated play is a core design feature.
- `mpcr` (Marginal per capita return): Frequently manipulated and reported.
- `punishment_cost`, `punishment_tech` (cost-impact ratio): Core to efficiency effect; frequently manipulated.
- `chat`: Examined in multiple studies as a moderator.
- `all_or_nothing` (discrete vs. continuous): Both types present; implications discussed.
- `punishment_exists`: Central dimension; main driver for treatment comparisons.
- `reward_exists`, `reward_cost`, `reward_tech`: Covered in several comparison studies, though less central than punishment.
- `show_other_summaries`, `show_n_rounds`: Sometimes manipulated and often reported, especially in relation to observability and feedback mechanisms.
- `show_punishment_id`: Occasionally discussed, mostly in relation to visibility and targeting.

**Indirectly Informed/Contextually Discussed:**
- `default_contrib` (framing, opt-in/opt-out): Not systematically varied, but mentioned occasionally.
- **Group composition (not a listed dimension but present in many findings)**: Effects of social, ethnic, or productivity heterogeneity are substantial moderators.

**Effectively Missing or Sparse:**
- Extremely large groups (beyond 10), continuous or highly dynamic membership.
- Multi-level punishment/reward structures (beyond the typical peer or centralized punishment).

---

# 7) Important Limitations

- **Heterogeneity in outcome measurement:** Not all studies report efficiency in a directly comparable way; sometimes only contributions or net payoffs are given.
- **Ambiguity in complex institutional/field environments:** Effects in large, highly heterogeneous, or real-world field settings are less well-represented, and the direction/magnitude of punishment's efficiency effect is more ambiguous or may even reverse.
- **Punishment mechanisms covered may not represent all forms of real-world punishment:** Most evidence is for monetary, explicit, and round-based punishment; social, reputational, or exclusion punishments are less systematically studied.
- **Behavioral mechanisms vs. outcome measures:** Many studies focus on behavioral mechanisms (cooperation, norm compliance) whose relationship to efficiency is non-trivial when costly punishment or antisocial punishment is present.
- **Unmeasured moderators:** Emotional state, comprehension, belief structures, and information timing are important and sometimes highlighted (e.g., Lee & Min, 2021; Waichman & Stenzel, 2019) but not always measured or controlled.
- **Sparse coverage of some dimensions:** While many key predictors are directly informed, less is known about, for example, the impact of default contribution framing, multi-stage or field-like dynamics, or compound incentives.
- **Potential for publication bias:** Positive punishment effects may be over-represented; null or negative findings are present but possibly under-sampled.

---

**Summary:**  
The literature strongly supports the predictive value of punishment institutions for group efficiency in public-goods-game-like environments but highlights the fundamental importance of design details: **Efficiency gains from enabling punishment are large only in canonical environments with effective targeting and institutions. In heterogeneous, uncoordinated, or high-control-efficiency settings—or where punishment is prone to misuse—punishment can have no effect or even reduce efficiency. Careful attention to both the 14 specified design dimensions and control efficiency is required for accurate prediction.**
