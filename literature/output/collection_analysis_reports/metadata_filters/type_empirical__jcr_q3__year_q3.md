# 1) Evidence Base

The paper set is predominantly an **empirical literature base**, with all 38 entries reporting on laboratory experimental studies (primarily lab experiments with human participants). The scope covers a **narrow-to-moderate range** of paradigms: most are linear public goods games (PGG) or close variants, with a subset focusing on adjacent social dilemmas (e.g., common pool resources (CPR), trust games, contests, and third-party punishment games).

A considerable fraction of papers provide **direct empirical evidence** about the effect of **punishment or monetary sanctions** on group efficiency or payoffs in repeated PGGs. Mechanism and theory arguments are present only as supporting explanations or in a few simulation/agent-based treatments, not as primary sources of data. Many papers also report on non-payoff behavioral outcomes (e.g., contribution rates, punishment usage) or focus on adjacent designs (third-party settings, trust games, etc.), providing only indirect or contextual evidence.

The **breadth** relevant to the downstream prediction task is strongest for:
- Standard and modified PGGs with peer, group, or centralized punishment and efficiency outcomes.
- Variations in the design and implementation of punishment and other institutional features (e.g., reward, monitoring, joint decision-making).

However, **gaps remain** in:
- Very large group sizes, real-world field settings, rare design dimensions (e.g., default contribution framing, technological features of punishment/reward), and long-term effects beyond the experimental horizon.

# 2) Task Relevance

**Task Relevance Dimensions:**
- `pgg_or_variant`:
  - **Exact:** ~11 papers use repeated linear PGGs or extremely close variants with minor modifications (e.g., vote-sanctioning, continuous and binary contributions).
  - **Close:** ~7 papers use CPRs, trust games, or repeated PDGs that mimic public-goods dilemmas structurally.
  - **Adjacent/Weak:** Remaining papers cover distant social dilemmas, one-shot games, or use alternative paradigm frames.
- `punishment_or_sanctions`:
  - **Exact:** ~13 papers test peer, group, or centralized costly punishment mechanisms (standard, democratic, or TPP), usually with control conditions.
  - **Close:** Several papers include monetary sanctions, reward, or information-based indirect sanctions (gossip, exclusion, ratings).
  - **Adjacent/Weak:** Some only address punishment via norm or framing, not actual costly sanctions.
- `efficiency_or_related_payoff_outcome`:
  - **Exact/Close:** ~12 directly report efficiency (payoff as % of maximum) or group payoff/welfare/total earnings; a few calculate surplus ratios.
  - **Adjacent/Weak:** Many report only on behavioral correlates (contribution rates, frequency of punishment/ostracism) or provide implied efficiency effects via observational lines.

**Summary:**  
A **core subset** of the literature has exact or close relevance for all three dimensions, particularly for repeated PGGs (or tightly analogous settings) with experimentally varied punishment and direct efficiency outcomes. Other papers are adjacent, offering context but lacking direct evidence for the treatment effect on efficiency.

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes:**
- **Reported Directly:**  
  - **Efficiency:** Calculated as payoff relative to the fully cooperative benchmark (e.g., (Pfattheicher et al., 2018); (Kamei, 2019); (Hou et al., 2019); (Lippert & Tremewan, 2021); (Faillo et al., 2020); (Abbink et al., 2020); (Shreedhar et al., 2020); (Brent et al., 2019); (Mitzkewitz & Neugebauer, 2020); (Szekely et al., 2020); (Fonseca & Peters, 2018); (Fehr & Sutter, 2019)).
  - **Group Payoff/Earnings/Surplus:** Group or mean player earnings analyzed as a function of the punishment intervention in many PGGs.
- **Indirectly or Not Reported:**  
  - Many studies report on contribution rates, cooperation, or punishment assignment without efficiency/payoff measures (e.g., (Fraser & Nettle, 2020); (Molenmaker et al., 2019)).

**Non-Payoff Behavioral Outcomes:**
- **Contribution/Cooperation Rates:**  
  - The most common behavioral measure, used frequently as a proxy for efficiency but analytically distinct.
- **Punishment/Reward Frequency and Magnitude:**  
  - Frequency, severity, and targeting of punishment/reward allocations, analyzed for mechanism insight (but not direct efficiency effect).
- **Norm Compliance, Reputation, Group Satisfaction:**  
  - Examined in some settings with peer approval or norm framing interventions (e.g., (Faillo et al., 2020); (Lois & Wessa, 2019)).

**Distinction Noted:**  
The literature is **clear** in separating efficiency/payoff outcomes from non-payoff behavioral metrics. While behavioral responses may map onto efficiency, the translation is not always one-to-one (e.g., higher punishment use may reduce efficiency if costs outweigh cooperation gains).

# 4) Main Findings Relevant To Prediction

**Synthesis of Main Empirical Findings:**

- **Peer Punishment Increases Contribution But May Reduce Efficiency In Standard Form:**
  - In classic PGGs, **enabling standard peer punishment nearly always increases contribution rates**, but **total efficiency often falls** due to costly punishment expenditures, unless punishment is well-targeted and limited in scope (e.g., (Pfattheicher et al., 2018); (Shreedhar et al., 2020)).
  - The *net* effect of punishment on **efficiency** is highly sensitive to the **cost-to-impact ratio**, the targeting/structure of punishment, and the possibility of antisocial (misdirected) punishment.

- **Punishment Institutional Design Matters:**
  - **Democratic peer punishment** (punishment applied only with majority support) or **centralized/group punishment** tends to reduce wasteful or antisocial punishment and can lead to **higher or neutral efficiency relative to no-punishment**, especially as the game progresses or when the mechanism is well-designed ((Pfattheicher et al., 2018); (Kamei, 2019); (DeAngelo & Gee, 2020)).
  - **Endogenous monitoring regimes** (where players can opt in to monitoring and punishment) may fail due to free rider problems, nullifying efficiency gains ((DeAngelo & Gee, 2020)).

- **Cost and Effectiveness of Punishment Are Crucial Moderators:**
  - **Lower punishment cost** increases the use of punishment, cooperation, and thus efficiency (within certain designs) ((Nikias & Sy, 2021)).
  - **Higher punishment effectiveness** (impact per unit cost) increases efficiency *if* correctly targeted but does not always solve the problem of antisocial punishment or overuse ((Mitzkewitz & Neugebauer, 2020); (Dorrough et al., 2021)).

- **Third-Party and Centralized Sanctions:**
  - **Third-party punishment** and especially its combination with rewards robustly increase both cooperation and group payoffs compared to baseline/no-sanction conditions ((Hou et al., 2019); (Chang et al., 2018)). **Reward alone** is generally less effective than punishment, and the combination is optimal.
  - **Centralized sanctions (taxation/fines)**, if properly structured, increase efficiency, sometimes more reliably than peer punishment, and with lower risk of costly antisocial effects ((Brent et al., 2019); (Abbink et al., 2020)).

- **Indirect Social Sanctions Increase Efficiency:**
  - Mechanisms such as **gossip**, **peer approval/rating**, or **ostracism voting** (when costless or very low cost) can increase efficiency comparably to monetary punishment, provided information is accurate and the cost to sanction is minimal ((Faillo et al., 2020); (Fehr & Sutter, 2019); (Fonseca & Peters, 2018); (Ramalingam et al., 2019)).
  - Small costs to approval/rating or unreliable indirect sanctions (noisy gossip) largely neutralize their positive effects.

- **Matching Protocol, Communication, and Group Size:**
  - **Fixed partner matching and communication (chat)** can increase both efficiency and cooperation, and interact with the effect of punishment ((Kamei, 2019); (Bigoni et al., 2019)).
  - Group size effects are reported but less consistently—very small (2-4 player) groups are most studied.

- **Design-Specific Variations:**
  - In **CPR games**, tighter monitoring structures and centralization increase efficiency, while imperfect networks (i.e., not everyone can punish everyone) reduce costly punishment and can raise efficiency ((Shreedhar et al., 2020)).
  - In “corrupt punishment” settings (e.g., bribes), the efficiency gains from punishment are reduced or even negated (Abbink et al., 2020).

**Points of Ambiguity and Disagreement:**
- Some studies find that **efficiency can be lower with punishment**, especially with high punishment costs or misdirected (antisocial) punishment ((Pfattheicher et al., 2018); (Shreedhar et al., 2020); (Szekely et al., 2020)).
- The **long-term/late-stage impact** of punishment (and especially of democratic or centralized institutions) may be substantially better than short-run effects, but evidence for this is experimental or simulation-based.
- The translation from *increased cooperation* to *increased efficiency* is **not always direct**.

# 5) Prediction Guidance

**How the Literature Should Inform Prediction:**

- **Baseline Control Efficiency is Key:**  
  Prediction of treatment (punishment-enabled) efficiency requires factoring the control (no-punishment) efficiency, as punishment’s effect is generally additive or multiplicative on this baseline, and the literature repeatedly uses this comparative structure.

- **Punishment Effect Moderated by Design Dimensions:**  
  - For **standard peer punishment** (few players, moderate rounds, continuous contribution, MPCR 0.4–0.8, punishment cost:impact ratio 1:3):
    - *Expect contribution rates to rise but efficiency increases only if punishment is targeted and not overused. Costly antisocial punishment may make net efficiency lower than control, especially in short games.*
  - For **democratic/majority or centralized punishment**:
    - *Predict higher efficiency than standard peer punishment, sometimes surpassing control over longer games.*
  - For designs with **low punishment cost, high effectiveness, and reliable monitoring**, expect the largest efficiency gains.
  - If **reward exists alongside punishment**, the effect can be complementary, with the highest efficiency in combined treatment arms ((Hou et al., 2019)).
  - Where **monitoring is endogenous** (opt-in), efficiency gains may not materialize unless freeriding on monitoring is solved.

- **Communication (chat)** and **matching protocol** (partner vs. stranger) further moderate the efficiency impact: these can either reinforce or, if absent, limit the gains from punishment.

- **Indirect sanctions** (approval, gossip, ostracism) can substitute for costly punishment if costless, but lose efficacy even with small sanctioning costs.

- **Structural and social context** (e.g., group size, minimum provision rules, team identity, group vs individual punishment targeting) also modulate the effect. The evidence is strongest for small groups, symmetric payoffs, and standard lab settings.

**Practical Recommendation:**  
*Predictions should be sensitive to the exact configuration of game design dimensions, especially with respect to the cost and scope of punishment, centralization, opportunity for antisocial use, reward availability, communication, and control game efficiency.*

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- `player_count` and `num_rounds`: Nearly all relevant studies report and vary these; findings are strongest for 2–4 players and 6–20 rounds.
- `mpcr`: Regularly varied or specified; impacts both baseline efficiency and punishment's incentive effect.
- `punishment_cost` and `punishment_tech` (impact): Directly manipulated in ~8 studies, with explicit findings on how lower cost or higher effectiveness raises efficiency when punishment is enabled.
- `punishment_exists` and type (standard vs. democratic vs. centralized): Central to most relevant studies; the difference in form is critical.
- `reward_exists`, `reward_cost`, `reward_tech`: Examined in several studies, often in combination with punishment, showing reward alone is weak but adds value in combination.
- `chat`: Directly manipulated in ~4 studies; enables higher cooperation and sometimes moderates the effect of punishment.
- `all_or_nothing`: Both binary and continuous contribution games are studied, though more work is in continuous versions.
- `show_n_rounds`, `show_other_summaries`: Present in some protocols; evidence suggests minor direct effect, but full transparency about others’ actions enables indirect sanctioning.
- `matching protocol` (partner vs. stranger): Coded in at least two studies, showing strong partner effects in small groups.

**Indirectly Informed or Contextual Dimensions:**
- `default_contrib`: Rarely manipulated; evidence is only contextual or missing.
- `show_punishment_id`: Occasionally reported (punisher/rewarder anonymity); indirect evidence of effects on punishment usage.
- `reward_cost`/`reward_tech`: Studied in intersection with punishment, but less emphasis individually.

**Missing/Sparse:**
- Long-run field settings, higher player counts (above 6), strong manipulations of default choices (default_contrib), very complex or multi-dimensional feedback arrangements.

# 7) Important Limitations

- **External Validity/Generalizability:**  
  The literature is based almost exclusively on short- to medium-length lab experiments with 2–6 players, short time horizons, and artificial settings; extrapolation to high player counts, field settings, or complex organizational structures is limited.

- **Breadth of Design Dimensions:**  
  Several design dimensions (e.g., default contribution framing, technology features of punishment/reward, punishment/reward identity revelation) are underexplored or only present contextually.

- **Payoff vs. Behavioral Outcomes:**  
  Some studies only report behaviors, not efficiency; mapping behavioral changes to efficiency relies on assumptions that may not hold in all cases.

- **Time Horizon Effects:**  
  Many findings suggest that the efficiency effects of punishment (especially democratic or centralized forms) improve with longer games, but most experimental horizons are short.

- **Antisocial/Costly Punishment:**  
  The prevalence and impact of antisocial punishment is context-dependent, and its long-term consequences on group dynamics and efficiency remain ambiguous.

- **Interplay of Mechanisms:**  
  The interaction between punishment and other mechanisms (reward, communication, peer approval, ostracism) is sometimes addressed but not comprehensively mapped; joint effect estimation is scarce.

- **Heterogeneity in Punishment Targeting:**  
  Effects can differ for centralized vs. decentralized, peer vs. group vs. third-party, and honest vs. corrupt punishment, with limited data for each variant within identical design frameworks.

- **Data on Control Efficiency:**  
  In a few studies, control (no-punishment) efficiency is not directly reported, making it difficult to precisely estimate the counterfactual.

---

*In sum, the literature provides robust empirical guidance for predicting the effect of enabling punishment on efficiency in repeated public-goods-game-like environments, especially for standard lab designs with well-specified parameters. Prediction is best supported when key design dimensions (player count, rounds, MPCR, punishment cost/tech, monitoring structure, reward) plus control efficiency are known. Outcomes are clearest for small groups and short horizons; the greatest limitations are external validity, underexplored design dimensions, and gaps in long-run and field evidence.*
