# 1) Evidence Base

The paper set includes six works, all of which are theoretical modeling studies with no new empirical or experimental data. Four papers (Shen et al., 2022; Xiao et al., 2023; Sun et al., 2023; Wang et al., 2022) examine variants of Public Goods Games (PGGs) and closely related social dilemmas, while the remaining two (Frey & Burgess, 2023; Chen et al., 2022) analyze adjacent domains using analogous game-theoretic frameworks (e.g., climate negotiations, pedestrian yielding, construction enterprise innovation). 

Overall, the literature set is broad in its exploration of punishment mechanisms, covering a range of game designs, enforcement institutions, and behavioral norms. However, it is notably narrow with respect to prediction of efficiency or group payoff outcomes: only one paper (Shen et al., 2022) directly models efficiency as a primary outcome, while others report on behavioral or compliance metrics that are only indirectly related to efficiency.

# 2) Task Relevance

**pgg_or_variant:**  
- Three papers are an *exact* match, modeling the canonical PGG or straightforward extensions (Shen et al., 2022; Xiao et al., 2023; Frey & Burgess, 2023).
- The rest are *adjacent*, analyzing trust games, driver compliance, and innovation partnerships, each with analogous cooperative dilemmas (Sun et al., 2023; Chen et al., 2022; Wang et al., 2022).

**punishment_or_sanctions:**  
- All papers have *exact* relevance, as they model or review punishment (and often reward) institutions for promoting compliance or cooperation.

**efficiency_or_related_payoff_outcome:**  
- Only one paper (Shen et al., 2022) is an *exact* match, modeling efficiency (group payoff relative to the cooperative optimum).
- Three papers are *adjacent*: they report behavioral outcomes (e.g., cooperation, compliance) and discuss institutional effects, sometimes referencing welfare or efficiency interpretively but without direct reporting (Frey & Burgess, 2023; Chen et al., 2022; Wang et al., 2022; Sun et al., 2023; Xiao et al., 2023).
- No papers are purely *close*, as none present empirical or experimental efficiency data from classic PGGs.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes (efficiency, group payoff, welfare, surplus):**
- **Directly modeled/reporting:** Only Shen et al. (2022) provides theoretical results on group efficiency and explicit conditions under which punishment and reward affect payoff.
- **Other sources:** Frey & Burgess (2023) and a few adjacent papers reference "welfare" or "group outcomes" but do not operationalize or quantify these as efficiency; any statements about efficiency are mechanism arguments or qualitative summaries.

**Non-payoff behavioral outcomes (cooperation rate, compliance, punishment frequency, trust):**
- The vast majority of the literature (five papers) focuses on cooperation rates, compliance stability, the adoption of cooperative strategies, trust, and punishment activity, with little to no mapping from these behaviors to actual payoffs or efficiency.
- These behavioral measures are relevant for understanding potential pathways to increased group efficiency, but their quantitative relationship to actual efficiency is unspecified or assumed, not demonstrated.

# 4) Main Findings Relevant To Prediction

Synthesizing across the papers, the following main findings pertain to the efficiency effects of peer punishment in public-goods-game-like environments:

- **Efficiency gains from punishment are possible, but design-sensitive:** Only one paper (Shen et al., 2022) models efficiency explicitly and finds that the effect of enabling punishment depends critically on how reward and punishment are implemented. Tax-based rewards given to cooperators (rather than punishers) increase both cooperation and efficiency; poorly designed rewards (supporting punishers) can actually reduce efficiency below baseline levels.

- **Punishment effectiveness is threshold-dependent and nonlinear:** Several papers indicate that punishment increases cooperation rates only above certain intensity or threshold levels (Xiao et al., 2023; Sun et al., 2023). However, the efficiency consequences of this are not directly measured—higher cooperation does not always translate to higher efficiency if costly punishment consumes resources.

- **Punishment often increases cooperation, with ambiguous efficiency effects:** Most adjacent and theory-based papers agree that punishment (often combined with reward or monitoring) robustly increases cooperation, trust, or compliance (Xiao et al., 2023; Sun et al., 2023; Chen et al., 2022; Wang et al., 2022). Only Frey & Burgess (2023) addresses the efficiency consequences explicitly, arguing that long-term welfare may rise despite potential short-term efficiency losses due to punishment costs.

- **Importance of parameterization:** Dimensions such as punishment cost, intensity, technology, player count, and the structure of reward/monitoring are repeatedly highlighted as key moderators. Theory papers emphasize threshold effects, competitive dynamics between cooperators/punishers, and the critical role of institutional design parameters in determining both behavioral and efficiency outcomes.

# 5) Prediction Guidance

**For predicting treatment efficiency (average efficiency with punishment enabled, given design and control efficiency):**

- The only directly informing result (Shen et al., 2022) shows that the payoff impact of punishment depends on its cost, the rule for allocating rewards, and the efficiency of the control game. Enabling punishment does not uniformly increase efficiency—poorly designed systems (e.g., rewards to punishers) may undermine both cooperation and group payoff relative to control.

- In the absence of other direct efficiency modeling, behavioral findings (cooperation, compliance, trust) can only provide *indirect* support. Theory papers repeatedly find that punishment, especially above a threshold intensity, increases cooperation rates—but the net effect on efficiency depends on the balance between increased cooperation and punishment costs.

- For parameter settings where control efficiency is low and punishment costs are moderate (and especially when rewards are structured to encourage cooperators, not punishers), enabling punishment is likely to increase efficiency according to Shen et al. (2022). If punishment is costly, misdirected, or paired with counterproductive rewards, efficiency may fall flat or even decrease.

- No empirical or experimental data are reported in this set, so all predictions must be considered theory-driven and conditional on model assumptions. Mechanistic arguments (from Frey & Burgess, 2023; Chen et al., 2022; Wang et al., 2022) support the link between punishment and increased cooperation/compliance as a pathway to efficiency improvement, but provide no direct effect sizes or guarantees.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed (modeled or linked to outcomes):**
- **player_count** (4 papers): (Shen et al., 2022; Xiao et al., 2023; Sun et al., 2023; Wang et al., 2022)
- **mpcr** (4 papers): (Shen et al., 2022; Xiao et al., 2023; Sun et al., 2023)
- **punishment_cost, punishment_tech** (all but Frey & Burgess, 2023): Modeled as key variables for punishment’s effectiveness and overall outcome.
- **reward_exists, reward_cost** (Shen et al., 2022; Chen et al., 2022): Modeled alongside punishment to assess their joint and interactive efficiency effects.
- **all_or_nothing** (3 papers): (Xiao et al., 2023; Sun et al., 2023; Wang et al., 2022) – as game structure.
  
**Indirectly informed:**
- **chat** (Frey & Burgess, 2023): Discussed as a moderator of negotiation/trust in climate games.
  
**Only discussed contextually or referenced briefly:**
- **default_contrib**, **show_n_rounds**, **show_other_summaries**, **show_punishment_id**, **reward_tech**, **reward_magnitude**, **punishment_magnitude**: Not substantively analyzed in any paper.

**Effectively missing:**
- No paper directly models or empirically manipulates show_n_rounds, show_other_summaries, show_punishment_id, or the specific implementation details of contribution framing, chat, or summary presentation. Their effects on efficiency with punishment are unaddressed or only contextually raised.

# 7) Important Limitations

- **Scarcity of direct efficiency evidence:** Only one paper (Shen et al., 2022) models efficiency or group payoff quantitatively—the rest provide only behavioral or procedural arguments, limiting precision for prediction.

- **No new empirical or experimental data:** All findings are theoretical-model-based or literature syntheses; the lack of empirical input limits generalizability and external validity.

- **Behavioral–payoff gap:** While behavioral outcomes (cooperation, compliance, trust) are repeatedly shown to rise with certain punishment regimes, their translation into actual efficiency—especially when punishment is costly—remains mostly an assumption, not a demonstrated fact.

- **Limited coverage of design dimension space:** Several potentially important design variables for downstream prediction are not addressed, including chat, contribution framing, visibility of rounds, and reward/punishment institutional details, reducing the ability to extrapolate to a wide range of game designs.

- **Contextual and institutional specificity:** Some models are tightly tied to analogs (e.g., climate negotiations, driver behavior, innovation partnerships), whose mapping to public goods games may not be exact, further limiting the transferability of their findings to the specific prediction task.

- **Potential for divergence in predictions:** Theoretical models sometimes yield contradictory implications depending on institutional details (e.g., when supporting punishers vs. cooperators with rewards)—such ambiguity must be carried forward in prediction and cannot be resolved with the available evidence.

---

**Summary:**  
The literature base is robust in its attention to the mechanics and conditions under which punishment might promote cooperation and (potentially) efficiency in PGG-like environments, but nearly all evidence is theoretical and/or behavioral. Only limited and institutionally sensitive guidance can be given for predicting treatment efficiency, and the impacts of several design features remain unmodeled or unknown. For formal prediction tasks, direct reliance must be placed on theoretical results (notably, Shen et al., 2022), and ambiguity about the translation from cooperation to efficiency must be explicitly maintained.
