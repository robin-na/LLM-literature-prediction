# 1) Evidence Base

The paper set is **broad, large, and highly empirical**, with 151 studies—almost all experimental (lab, plus some field) and an overwhelming emphasis on public-goods games (PGGs) or close variants. The **vast majority** of papers are empirical lab experiments that manipulate punishment, with a smaller subset on reward, communication, or informational interventions. A smaller fraction use adjacent paradigms (trust games, CPR games, repeated PDs). The evidence is therefore **rich in direct, comparative, and quantitative data** relevant to the downstream prediction task: forecasting how enabling punishment (given extensive design parameters and control efficiency) impacts group efficiency and payoff-based outcomes. 

A smaller (but nontrivial) portion of the literature is only **contextually or behaviorally relevant** (focusing on contributions/cooperation, norm violations, or punishment use rather than payoffs/efficiency) and is noted for its more limited direct applicability.

# 2) Task Relevance

**Relevance to PGG or Variant (`pgg_or_variant`):**  
- A large proportion of the evidence is **exactly on PGGs** or minimal modifications (e.g., heterogeneous MPCR, networked PGGs, coalition-PGGs, or step-level/backstop variants)—relevance: `exact`.
- Numerous studies cover **closely related environments** (CPR dilemmas, team production, repeated PDs with group structure)—relevance: `close`.
- Some are only **adjacent** (trust games, dictator games, third-party punishment)—relevance: `adjacent` or `weak`.

**Relevance to Punishment or Sanctions (`punishment_or_sanctions`):**
- Most PGG/CPR studies **directly manipulate the presence/structure of punishment**—relevance: `exact`.
- Some papers explore **reward, ostracism, exclusion, or taxation** as alternative sanctions—`close` relevance, but not always identical to peer punishment.
- A moderate subset look at **non-material/indirect sanctions** (gossip, social exclusion, feedback), and a few focus only on **behavioral responses** or attitudes toward punishment rather than institutional presence.

**Relevance to Efficiency or Related Payoff Outcome (`efficiency_or_related_payoff_outcome`):**
- Many core studies report **efficiency, group payoff, or total earnings/surplus**—relevance: `exact`.
- In a number of cases, **contribution/cooperation rates** are the main outcome, and efficiencies must be inferred—relevance: `close` or `adjacent`.
- Some studies do **not report efficiency or payoff-based outcomes** at all, focusing on norm compliance/behavioral outcomes—relevance: `weak` or `none`.

> **Summary:** The evidence base is **highly relevant** to the downstream prediction task, offering strong empirical coverage for PGGs/variants, punishment/sanctions, and (to a slightly lesser extent) direct payoff/efficiency outcomes.

# 3) Outcomes Measured In The Literature

### **Payoff-based Outcomes (Directly Relevant):**
- **Efficiency:** Most central studies report efficiency (group earnings/maximum possible), sometimes as a strict percentage; when not explicit, total group payoff, average earnings, welfare, or surplus are reported.
- **Net Payoff & Welfare:** Many papers provide or allow inference of net payoffs after accounting for punishment/reward costs, crucial for distinguishing increased cooperation from actual increases in group welfare.

### **Non-Payoff Behavioral Outcomes (Indirect):**
- **Contribution/Cooperation Rate:** Frequently reported, but may not map one-to-one to efficiency (due to punishment/reward costs, anti-social punishment, or misaligned incentives).
- **Punishment Assigned/Frequency:** Used to assess mechanism usage (sometimes at the expense of efficiency).
- **Norm Compliance, Trust, Satisfaction, Belief Measures:** Useful for mechanistic understanding, less for direct efficiency prediction.
- **Sanction/Reward Distribution, Retaliation/Counterpunishment:** Occasional focus, relevant for predicting institutional side-effects on efficiency.

> **Distinction:** **Empirical studies often show that higher cooperation does not always translate to higher efficiency**, especially when punishment is costly, anti-social, or misdirected. **Efficiency must not be conflated with contribution rate.**

# 4) Main Findings Relevant To Prediction

## Empirical Patterns

- **Punishment's Effect on Efficiency is Context-Dependent:**
    - In **standard linear PGGs with peer punishment and moderate/high punishment costs**, enabling punishment typically **increases contributions** but does **not always increase efficiency**. Often, **punishment costs outweigh the gains** from increased cooperation—leading to equal or lower efficiency than control (e.g., Anderson & Putterman 2006; Nikiforakis 2010; Fatas & Mateu 2015).
    - **Efficiency gains appear when:**
        - **Punishment is restricted to 'legitimate' or prosocial forms and anti-social punishment (of cooperators) is minimized** (Faillo et al., 2013; Zheng & Nie, 2013).
        - **Punishment is paired with communication, universal agreements, or high feedback transparency** (Andrighetto et al., 2016; Dannenberg, 2016).
        - **Punishment mechanisms are **costly enough to deter excessive or anti-social use, or made democratic/centralized to mitigate excessive or misdirected punishment** (Kuwabara & Yu, 2017; Pfattheicher et al., 2018).
    - **Antisocial or excessive punishment—when present—can nullify or reverse efficiency gains**, with costs eating into group welfare (Chen, 2022; Fischer et al., 2016; Dorrough et al., 2017).
    - **Centralization or demarcation** (designated punisher, absolute/relative mechanisms) can mitigate anti-social punishment but are not universally efficient—centralized punishment in noisy environments does not always outperform decentralized punishment (Fischer et al., 2016; Kamijo et al., 2014).
    - **Punishment in environments with high intrinsic motivation** (field/real-world, stakes, prosocial orientation) can **crowd out cooperation** and lower efficiency (Amirova et al., 2022).

- **Nonlinearity and Game Structure Matter:**
    - In **nonlinear/CPR settings or where the production function is weakest-link or best-shot, punishment's efficiency impact reverses:**
        - In **weakest-link/threshold games**, punishment is more reliably positive, sharply boosting efficiency (Fatas & Mateu, 2015; Karakostas et al., 2023).
        - In **nonlinear/complex resource games**, punishment can worsen efficiency, as its costs are not offset by enough cooperative gain (Cason & Gangadharan, 2016).
    - **Reward or combined reward/punishment mechanisms generally outperform punishment-only interventions** in efficiency (Chen, J. 2022; Hou et al., 2019; Colombier et al., 2011).

- **Role of Feedback, Visibility, and Communication:**
    - The **format and content of feedback** (showing contributions, earnings, both) **strongly moderate the punishment effect**; certain feedbacks produce more antisocial punishment and lower efficiency (Nikiforakis, 2010).
    - **Enabling communication (chat, messaging, norm expression) robustly increases efficiency**, often more than punishment and sometimes making punishment redundant (Andrighetto et al., 2016; Adams et al., 2022; Zhosan & Gardner, 2013).

- **Group Size, Network Structure, and Legitimacy:**
    - **Punishment effectiveness varies nonmonotonically with group size**; optimal effects can require public identity of punishers (Zheng & Nie, 2013), and excessive monitoring can actually reduce efficiency (Shreedhar et al., 2020).
    - **Legitimacy (via group voting or endogenous institution choice)** markedly increases the efficiency effect of even weak or mild punishment (Tyran & Feld, 2006; van Klingeren & Buskens, 2024; Gatiso & Vollan, 2017).

- **Parameter Sensitivity:**
    - **Punishment cost/effectiveness ratio** is a key moderator: too low a cost leads to over-punishing (lower efficiency), too high reduces its corrective potential (Anderson & Putterman, 2006; Nikiforakis, 2010; Nikias & Sy, 2021).
    - **Noise and monitoring uncertainty** reduce punishment's positive impact on efficiency (Fischer et al., 2016; Gallo et al., 2022).
    - **Institutional details** (anonymity vs public identity, exogenous vs endogenous monitoring, centralized vs peer, opportunity for counterpunishment) are crucial.

## Theoretical/Mechanism Insights

- **Punishment is most efficient when prosocial, well-targeted, costly enough to avoid excess, and transparent/legitimate.**
- **Efficiency increases depend on the ratio of increased cooperation to punishment cost—a balancing act fouled by excessive, misdirected, or retaliatory punishment.**
- **Crowding out of intrinsic motivation can occur** when punishment is introduced in high-trust or intrinsically cooperative groups, leading to efficiency losses (Amirova et al., 2022).
- **Endogeneity and procedural justice enhance the effect:** punishment regimes chosen or perceived as legitimate/just are more efficiency-enhancing.

# 5) Prediction Guidance

**For forecasting treatment efficiency from design dimensions and control efficiency:**

- **Punishment Effects are Highly Conditional:** Do not assume enabling punishment increases efficiency over control; benchmark first against the structure:  
    - **Linear standard PGGs (small groups, peer punishment, moderate costs, no communication):**  
      - **Positive efficiency effect only if antisocial/excess punishment is constrained (via legitimacy, information, targeting), punishment cost is not too low, and feedback supports norm enforcement.**   
      - **If excessive or anti-social punishment is probable (unrestricted punishment, costless punishment), efficiency may drop below control.**  
    - **Threshold/weakest-link games:**  
      - **Punishment much more likely to yield strong efficiency gains.**
    - **Nonlinear/CPR settings:**  
      - **Punishment often fails to increase, or may reduce, efficiency; communication is a stronger lever.**
    - **Large groups:**  
      - **Legitimacy and monitoring structure are increasingly critical; anonymous or excessive punishment easily backfires.**  
    - **Centralized/Designated Punishments:**  
      - **If institutions are legitimate and allow for targeted, costly sanctions, efficiency is generally higher. Otherwise, centralization alone does not guarantee an effect.**
    - **Endogenous Institution Choice (voting):**  
      - **Enacting punishment by group vote amplifies even weak-signal punishment's effect on efficiency relative to exogenously imposed mild law.**

- **Crucial Moderators:**
    - **Communication**: Presence (chat, messaging) can overshadow or substitute for punishment's effect.
    - **Feedback & Transparency:** The more transparent, fair, and targeted the institutional features (who can punish whom, who sees what), the higher the likelihood of efficiency gains.
    - **Cost/Benefit of Punishment:** High cost tends to reduce overuse; low or costless punishment often reduces efficiency due to over-punishing (Anderson & Putterman, 2006).
    - **Legitimacy and Endogeneity:** Systems perceived as fair/legitimate or chosen by participants are more likely to deliver efficiency gains; imposition/crowding out can reverse expected effects.
    - **Group Heterogeneity:** Results are mixed; some heterogeneous (endowment/beneﬁt) groups see no improvement or lose efficiency due to punishment misuse (Chen, J. 2022 vs. Reuben & Riedl, 2013).

- **If Control (No-Punishment) Efficiency is Low:**
    - **Punishment often improves efficiency, especially when designed to minimize anti-social punishment and maximize legitimacy/feedback.**

- **If Control Efficiency is Already High:**
    - **Punishment may offer little to no incremental efficiency and can reduce efficiency if punishment costs are high and cooperation is already substantial without it.**

- **If Antisocial or Excess Punishment is Possible:**
    - **Expect at best a null effect on efficiency, and potentially negative. Prediction should not assume gains unless design rules out anti-social targeting.**

- **Game Design Dimensions are Critical:**  
    Prediction should not be based on control efficiency alone but must **integrate structural design dimensions constrained by the above findings.**  
    - *E.g.,* Predict efficiency increases **only** if design allows for prosocial-focused, legitimate, and well-monitored punishment, and if the feedback structure encourages normative enforcement rather than vendetta cycles.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions (strong or repeated empirical coverage):**
- `player_count`  
- `num_rounds`
- `mpcr`  
- `punishment_cost`  
- `punishment_tech`  
- `chat`  
- `reward_exists` / `reward_cost` / `reward_tech` (sometimes)
- `all_or_nothing`  
- `show_other_summaries` / `show_n_rounds`  
- `show_punishment_id` (identity/reputation channels are frequently manipulated)
- `punishment_exists` (primary treatment variable)
- `default_contrib` (sometimes in framing manipulations)

**Indirect or Contextually Discussed Dimensions:**
- `reward_tech`, `reward_cost`—often as comparison, less as main focus.
- `default_contrib`, in the context of opt-in/opt-out frames.
- `show_n_rounds`, `show_other_summaries`—sometimes manipulated, more often as control settings.
- `show_punishment_id`—key in anonymous vs. public punishment treatments.

**Effectively Missing or Weakly Treated:**
- Precise fine-grained manipulations of `default_contrib` are rare.
- Combined, endogenous multi-dimensional manipulations (simultaneous full variation in >5 dimensions) are rare; most studies vary 1–3 at a time.
- Some interaction terms (e.g., `reward_exists` × `punishment_exists` × `chat`) are less represented.

**Implications:**  
**Strongest predictive confidence is for design dimensions targeted in multiple studies** (punishment cost, monitoring, feedback types, group size, rounds, MPCR, legitimation, chat, punishment/reward simultaneity, information structure). **Prediction for edge cases or underexplored design regions must account for uncertainty.**

# 7) Important Limitations

- **Potential Gaps in Parametric Coverage:** Not every combination of the 14 design dimensions is represented empirically, and for some (e.g., very large/small groups, extremely high/low mpcr, or idiosyncratic feedback arrangements) only contextual evidence is available.
- **Heavy Skew Toward Laboratory Contexts:** Field, online, and naturally occurring public-goods dilemmas are underrepresented; results from the field (e.g., Amirova et al., 2022) suggest institutional interventions may backfire or crowd out intrinsic motivation—difficult to extrapolate from lab to field.
- **Payoff vs. Behavior Confounds:** Many papers report only behavioral proxies (contribution rates, punishment assigned), requiring inferential leaps to group efficiency, and at times these diverge (e.g., increased cooperation but lower net efficiency due to punishment costs).
- **Ambiguity/Disagreement in Some Parameter Regions:** Clear empirical conflict in the effect of punishment in heterogeneous groups (Chen, J. 2022 vs. Reuben & Riedl, 2013), with strong contextual modulation (production technology, legitimacy, feedback).
- **Institutional Detail Sensitivity:** Small changes in punishment targeting, cost, legitimacy, or feedback structure result in sharply different efficiency outcomes.
- **Absence of Non-Lab/Social Norm and Informal Sanctioning Mechanisms:** Some contextually important factors (role models, gossip, endogenous agreements, framing effects) are less systematically mapped to efficiency outcomes.
- **Limited Evidence on Multi-intervention Synergy:** Interactions between punishment and other mechanisms (chat, reward, reputation, endogenous institution formation) are well documented in some dyads but sparse across the full combinatorial space.
- **Lack of Longitudinal Evidence on Durability:** Some studies show long-term convergence of efficiency with punishment (Sparks et al., 2024); others document only transitory effects or short-run adverse outcomes.

---

**In summary:**  
The literature synthesizes to a nuanced account: **Punishment in PGGs can increase, decrease, or leave unchanged group efficiency depending heavily on the details of game design, the institutional structure of punishment, cost/impact ratio, feedback system, legitimacy, and the initial level of group cooperation.** Predictive models must carefully attend to these moderators. Control efficiency alone is insufficient without integrating key design dimensions, and prediction is most certain within well-represented, empirically grounded parameter regions.
