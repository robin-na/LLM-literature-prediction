# 1) Evidence Base

The paper set is broad and multidisciplinary, containing 62 papers that span empirical (experimental and observational) and theoretical studies. For the task of predicting *treatment* efficiency (with peer punishment enabled) in public-goods-game-like environments, the evidence base includes:

- Several *exactly relevant* lab experiments on repeated public goods games (PGGs) with and without peer punishment, measuring group earnings or efficiency directly (e.g., Lo Iacono et al., 2023; Gordon & Puurtinen, 2021; Gross et al., 2022; Ertör-Akyazi, 2019; Eichenseer, 2023).
- Meta-analyses and meta-regressions (Eichenseer, 2023) that aggregate findings across many experimental studies addressing how design dimensions and interventions affect efficiency.
- Multiple theory papers offering formal models of punishment, efficiency, and moderators (e.g., Boyd et al., 2014; Langlois & Langlois, 2004; Heller & Sieberg, 2010; Libois, 2022).
- Simulation/modeling studies focused on the structure and mechanisms underlying punishment’s efficacy.
- Many *adjacent* or *contextual* papers that address concepts like sanctions, reputation, norm enforcement, ostracism, and informal punishment in similar but not directly matching environments (e.g., CPRe, networked PGG, reward-only conditions).
- Some papers focus strictly on behavioral or psychological outcomes (e.g., willingness to punish, norm compliance) without direct measurement of group payoff or efficiency.

**Empirical papers with direct efficiency outcomes in canonical PGGs are in the minority but provide the strongest evidence for prediction. Contextual and adjacent evidence is rich but must be carefully distinguished from direct payoff evidence.**

# 2) Task Relevance

**pgg_or_variant:**  
- *Exact* relevance: Several papers use repeated, standard linear PGG lab experiments with explicit payoff-based outcomes (Lo Iacono et al., 2023; Gordon & Puurtinen, 2021; Gross et al., 2022; Ertör-Akyazi, 2019; Eichenseer, 2023).
- *Close*: Some studies use threshold PGGs, extraction games, CPRs, or experimentally-framed field environments with high structural similarity.
- *Adjacent/Weak*: Many papers study games not strictly PGGs (ultimatum games, trust/dictator games, CPRe, lending games, coordination or network games).

**punishment_or_sanctions:**  
- *Exact*: Core experimental PGG papers directly manipulate the presence/absence of peer punishment options and measure effects.
- *Close*: Some examine other sanctions (ostracism, monetary penalties, exclusion), leader punishment, endogenous institution selection, or reward as a moderator/alternative.
- *Adjacent*: Reputation, informal social sanctioning, ostracism, and third-party punishment in non-PGG games.
- *Weak/None*: A significant number do not manipulate punishment/sanctions at all.

**efficiency_or_related_payoff_outcome:**  
- *Exact*: Efficiency, group payoff, average profit, earnings, welfare, and surplus are the primary outcomes in a subset of empirical and theoretical core PGG studies (Eichenseer, 2023; Lo Iacono et al., 2023; Gordon & Puurtinen, 2021; Gross et al., 2022; Freytag et al., 2014).
- *Close*: Related payoff outcomes like probability of reaching group targets, earnings net of penalties, or similar wealth/resource flow measures.
- *Adjacent/Weak*: Many focus on contributions, cooperation rates, norm compliance, punishment frequency, intention to punish, trust ratings, or reputational effects—these are behavioral proxies, and not direct measures of efficiency.

**Summary:**  
The literature most directly relevant involves core PGG lab experiments with measurable group efficiency/payoff as a primary outcome, and explicit manipulation of peer punishment. There is a larger contextual base, but only a subset is `exact` or `close` to the downstream prediction task.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes (directly relevant):**
- Group efficiency (fraction of optimal group payoff; Lo Iacono et al., 2023; Gross et al., 2022; Eichenseer, 2023).
- Average/total group profit or earnings.
- Net group surplus/welfare/testing for whether enabling punishment increases cumulative payoffs.
- Probability of meeting group payoff thresholds, in threshold or milestone PGGs.

**Non-payoff outcomes (behavioral or psychological):**
- Contribution or cooperation rates (how much individuals contribute).
- Frequency, targeting, and perceived legitimacy of punishment.
- Norm compliance, retaliation, and antisocial punishment frequency.
- Trust ratings, group cohesion, willingness to sanction or punish, perceived trustworthiness, etc.

**Distinction:**  
While many papers report behavioral outcomes, only a subset provides direct data or theory on efficiency or group payoff. Where findings are based on non-payoff outcomes, these are explicitly indicated as indirect and not sufficient to infer efficiency changes (unless evidence from the same or similar contexts links cooperation rates to efficiency).

# 4) Main Findings Relevant To Prediction

**Empirical findings (efficiency/payoff-focused, PGGs with direct comparison):**
- Enabling peer punishment in standard repeated PGGs *typically* raises group efficiency (average payoff), often substantially compared to no-punishment controls—provided some minimal conditions of universality and information exist (Lo Iacono et al., 2023; Gordon & Puurtinen, 2021; Eichenseer, 2023).
- The *magnitude* of efficiency gains depends on context: punishment is more effective with full group accountability, fixed identities, public summary of actions, appropriately balanced punishment cost-to-impact ratios, and absence of unpunishable players (Gordon & Puurtinen, 2021).
- Prior social conflict, identifiability of past conflict roles, or flawed punishment targeting can reduce the efficiency benefit, sometimes eliminating it or causing net efficiency loss via maladaptive punishment (Gross et al., 2022).
- In real-world field or framed experiments, monetary penalty schemes typically yield moderate efficiency increases, less than those achieved via informal communication (Ertör-Akyazi, 2019).
- Meta-analytic evidence demonstrates peer punishment increases efficiency even more than leader or centralized punishment, with rewards having a smaller but positive effect (Eichenseer, 2023). However, rotating punishment/reward roles may undermine efficiency.

**Theoretical and simulation findings:**
- The effect of punishment on efficiency is *highly moderated* by: player count, MPCR (resource scarcity), punishment cost/impact structure, and group social structure (Boyd et al., 2014; Farjam et al., 2015; Heller & Sieberg, 2010; Libois, 2022; Langlois & Langlois, 2004).
    - Small groups, low MPCR, and efficient punishment mechanisms (i.e., high impact/low cost, minimal antisocial use) favor positive efficiency effects.
    - Large groups, high MPCR (abundance), costly or misapplied punishment, and low social cohesion/ability to enforce, can negate efficiency benefits or even make punishment net-negative (Boyd et al., 2014; Farjam et al., 2015; Handfield et al., 2016).
    - Punishment that is self-punishing (mutual, un-targeted, or triggered by noise) can reduce or eliminate efficiency gains (Langlois & Langlois, 2004).
    - Strength and design of sanctioning mechanisms (max enforceable sanction, its relation to incentive to defect) are critical (Libois, 2022).
- Mechanism: punishment increases efficiency only if it promotes accurate targeting of free riders and remains low in overall cost/expenditure. Misapplied or antisocial punishment can sharply reduce efficiency.

**Indirect or adjacent findings:**
- Ostracism and exclusion can function similarly to costly punishment, increasing group efficiency when group membership is dynamic (Sääksvuori, 2014).
- Adding rewards as an alternative or in combination with punishment can also increase efficiency, but the structure (e.g., net-positive rewards; Stoop et al., 2018, Eichenseer, 2023) matters.
- In some environments, communication and framing have equal or stronger effects than punishment on efficiency (Ertör-Akyazi, 2019; Goette & Huffman, 2007).
- Several papers warn that in the presence of antisocial punishment, punishment can actually lower efficiency despite higher cooperation rates (Handfield et al., 2016).
- Some theoretical work cautions that in continuous-choice games or high-noise environments, punishment may have little or even negative effect on efficiency unless augmented by other norms or discretization (Yan et al., 2023; Langlois & Langlois, 2004).

# 5) Prediction Guidance

Given the above literatures:

- **If the design is a canonical repeated PGG (with measured control efficiency), and peer punishment is enabled as in the core experiments:**
    - **Prediction:** Adding peer punishment can be expected to *increase average group efficiency* over the control, with effect sizes ranging from moderate to large, provided that
        - Punishment is universal (no one is immune),
        - Information is full (actions and punishers are visible),
        - The cost/impact ratio is moderate (not excessively costly or ineffective), and
        - Antisocial punishment is rare or absent.
      (Supported by Lo Iacono et al., 2023; Gordon & Puurtinen, 2021; Eichenseer, 2023.)

- **Magnitude of effect:**
    - Meta-analytic results suggest peer punishment increases efficiency by approximately 0.47 (on a scale from 0 to 1) relative to optimal contributions, with leader/centralized punishment at roughly 0.26 (Eichenseer, 2023).
    - The baseline control efficiency is an important moderator: the lower the efficiency in the control, the larger the possible benefit from enabling punishment, so prediction should focus on incremental delta over control.

- **Modifiers:**
    - For *small group sizes* (e.g., n ≤ 12), *low-to-moderate MPCR*, and *reasonable punishment cost/impact ratios*, efficiency gains from punishment are strongly supported.
    - For *large groups*, *high MPCR*, or when *punishment is poorly designed* (e.g., unrestricted, prone to antisocial use), efficiency improvement can disappear or reverse, and even drop below control (Boyd et al., 2014; Farjam et al., 2015; Handfield et al., 2016).

- **Caveats and exceptions:**
    - If *any player is immune* from punishment, a significant drop in efficiency is likely due to exploitation by the immune player.
    - If the social context includes recent conflict with identifiable roles, efficiency gains from punishment may be muted or lost unless roles are anonymized (Gross et al., 2022).
    - Game structure (threshold vs. linear, continuous vs. discrete choices) and the presence of framing/communication can alter or override effects.

- **When core design dimensions differ from canonical lab settings (e.g., networked/CPR, informal institutions, non-PGG):**
    - Prediction should be attenuated: efficiency effect of peer punishment is less certain and may be context-specific or even negative, especially if the sanction system is costly, misapplied, or does not overcome existing norms or payoff structures.

- **Use control efficiency as baseline:**
    - Predict treatment efficiency as baseline control efficiency plus an expected delta (based on meta-analytic or experiment-specific findings), adjusting for design dimensions indicated above.
    - Caution is advised if control efficiency is already high due to other mechanisms (e.g., communication); the incremental gain from punishment may be minimal or zero.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions:**  
- **player_count:** Strongly examined; effect of group size is a central moderator (Lo Iacono et al., 2023; Eichenseer, 2023; Boyd et al., 2014; Libois, 2022).
- **num_rounds:** Most studies use repeated games; number of rounds is generally fixed, but not much cross-study variance.
- **mpcr:** Frequently manipulated; known moderator of whether punishment helps or harms efficiency (Farjam et al., 2015; Ertör-Akyazi, 2019).
- **punishment_cost / punishment_tech:** Directly addressed as moderators; cost/benefit ratio, structure (peer, centralized, ostracism, leader), and technological implementation are key (Eichenseer, 2023; Boyd et al., 2014; Heller & Sieberg, 2010).
- **all_or_nothing:** Usually continuous, but some all-or-nothing/game-variant studies inform this dimension.
- **chat:** Empirically tested as a strong moderator; communication often produces efficiency gains larger than punishment (Ertör-Akyazi, 2019; Goette & Huffman, 2007).
- **reward_exists:** Directly analyzed in leader/peer reward and combined treatments (Eichenseer, 2023; Stoop et al., 2018).

**Indirect or contextually discussed dimensions:**  
- **default_contrib:** Referenced in framing, but not a primary focus.
- **show_other_summaries, show_n_rounds, show_punishment_id:** Addressed where visibility and information structure moderate punishment targeting and effect.
- **reward_cost, reward_tech:** Somewhat discussed in studies on joint reward and punishment treatments.

**Effectively missing or very sparsely covered:**  
- **punishment_magnitude:** Usually coupled to cost as a ratio, but less often independently varied.
- **show_punishment_id:** Rarely manipulated directly; discussed as part of information/visibility.
- **reward_magnitude:** Seldom quantified; not central in core findings.

# 7) Important Limitations

- **Scope:** Only a subset of papers provide directly relevant, quantitative evidence with all necessary design dimensions measured and varied; much of the literature is adjacent, conceptual, or focused on behavioral proxies.
- **Generalizability:** Most strong findings come from highly controlled lab experiments with fixed parameters; generalizing to different group sizes, MPCRs, networks, contexts, or real-world settings carries substantial risk.
- **Moderators sometimes unmeasured:** Many possible moderators (e.g., control efficiency, antisocial punishment, social network effects, ostracism, immunity, communication, framing) are not systematically manipulated or only explored in one or two papers.
- **Ambiguity about causality/mechanisms:** While an overall trend for efficiency gains from peer punishment exists, the *mechanisms* (deterrence, targeting accuracy, reputation, retaliation, information, etc.) are not always isolated.
- **Behavioral-proxy confusion:** A considerable portion of the literature relies on contribution rates or norm compliance as outcomes, which do not always map cleanly to efficiency, especially when punishment costs are high or misapplied.
- **Boundary conditions:** Efficiency gains appear strongest in conditions with clear free rider problems and baseline low efficiency; in high-control-efficiency games (due to communication, social norms, strong institutional context), the marginal improvement from punishment may be small or nil, and punishment may even reduce welfare via cost overrun or antisocial use.
- **Heterogeneity in punishment design:** Not all "punishment" is equal. Design details—such as universality, permanence, visibility, cost, magnitude, possibility of antisocial punishment, or redress—critically condition whether enabling punishment aids or hinders efficiency.
- **Limited variance on some dimensions:** Central parameters (player count, MPCR, punishment cost) are often held constant within any given study, limiting inference about cross-dimensional interactions.

**In sum:** The literature set provides solid evidence that enabling peer punishment in canonical repeated PGGs generally increases group efficiency, but the effect is quantitatively and qualitatively moderated by multiple design dimensions and baseline efficiency. For prediction tasks, strongest guidance should be drawn from meta-analytic findings and direct experimental evidence, with contextual and theoretical insights shaping interpretation of design-specific cases. Substantial caution is warranted when extrapolating to novel designs, large groups, high-resource environments, or real-world field settings.
