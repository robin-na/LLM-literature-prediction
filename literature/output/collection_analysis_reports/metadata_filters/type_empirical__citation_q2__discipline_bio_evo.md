# 1) Evidence Base

The paper set comprises **37 studies** and is **empirically oriented**—the overwhelming majority are **laboratory experiments** or **field experiments** with real-world participants; a minor subset are naturalistic or observational studies. A handful of papers rely on model-based agent simulations alongside experimental data. The **breadth** of the evidence for the prediction task is **moderate**:

- About **one-third** feature **standard linear public goods games (PGGs) with or without punishment**; another set employ **close CPR (commons) variants, or threshold/collective-risk/weakest-link games**. Several are only *adjacent* (e.g., trust, ultimatum, or coordination games with punishment features).
- Only a **subset directly measure efficiency, group payoff, or welfare** as their main outcome. Several others focus on cooperation/contribution rates, punishment frequency, norm compliance, or neural/psychological outcomes.
- The **relevance for the downstream prediction task—predicting average efficiency from design dimensions and control efficiency—is thus moderate but limited by outcome reporting and by game/types represented**.

Papers vary in their **institutional contexts** (centralized vs. decentralized punishment, external vs. peer punishment, reward institutions), **group sizes** (mostly 4–5 members), rounds (1 to 30+), and other design characteristics (e.g., presence of communication, type of production function, information feedback).

# 2) Task Relevance

Each paper was assessed on **three key relevance metrics**:

### a) pgg_or_variant
- **Exact relevance**: About ten papers use **standard repeated linear PGGs**.
- **Close relevance**: Several employ **CPR games**, **weakest-link**, or **threshold public goods**, which share core features.
- **Adjacent/weak relevance**: Studies on **trust, dictator, ultimatum, or coordination games**, or on non-human cooperation, typically lack group-based public good provision and are only contextually comparable.

### b) punishment_or_sanctions
- **Exact relevance**: A substantial subset manipulate *punishment (peer, central, third-party, or external)* as a core experimental treatment.
- **Close/adjacent**: Some implement **ostracism (social exclusion)** as a form of sanctioning, or measure indirect signals or aggression.
- **None/weak**: A minority have no punishment component.

### c) efficiency_or_related_payoff_outcome
- **Exact/close relevance**: Fewer than half **report efficiency or total group payoff/welfare** directly.
- **Adjacent/weak**: Many focus on **cooperation rates, norm compliance, or punishment behavior**—not on efficiency as payoff relative to full cooperation.
- **None**: Several do not report any payoff-based group outcome, focusing solely on behavior or neural measures.

# 3) Outcomes Measured In The Literature

### a) Payoff-based Outcomes (Relevant for Prediction)
- **Group efficiency** (payoff as a proportion of full-cooperation benchmark), **average group payoff**, or **welfare** are direct and explicitly measured in:
  - Some standard PGGs with/without punishment (e.g., Fischer et al., 2016; Andrighetto et al., 2016; Fatas & Mateu, 2015; Wegmann & Musshoff, 2019; Javaid & Falk, 2015; Sääksvuori, 2014).
  - Close CPR variants and select collective risk games.
  - **Key for prediction**: Only these studies directly inform how punishment shifts efficiency.

### b) Non-payoff Behavioral Outcomes (Indirect or Contextual Relevance)
- **Contribution or cooperation rates** (most common), **punishment frequency**, **antisocial/prosocial punishment**, **norm compliance**.
- **Neural, psychological, and signaling outcomes**.
- **Important distinction**: Increases in cooperation rate or decreased extraction do **not necessarily map to higher efficiency**, especially if punishment is costly and the cost outweighs the cooperation gains.

### c) Outcomes Not Directly Relevant
- **Neural/brain imaging**, **emotion/mood effects**, **signaling**, and purely descriptive outcome measures.

# 4) Main Findings Relevant To Prediction

Synthesizing the most *directly relevant* empirical findings:

### a) Punishment often *fails* to increase efficiency in standard PGGs (payoff-based).
- **Standard linear PGGs in Western settings:** 
    - Peer or central punishment **does not reliably increase efficiency**; high punishment costs and frequent antisocial/hypocritical punishment can even **reduce group payoff relative to the control** (Fischer et al., 2016; Fatas & Mateu, 2015; Burton-Chellew & Guérin, 2021).
    - **Punishment costs often outweigh cooperation gains, especially when antisocial punishment is frequent.**

### b) Moderators: Information structure, communication, institution type, production function
- **Communication (chat, messaging):** 
    - **Enables substantial efficiency gains** when combined with punishment—neutralizing counter-punishment and supporting norm establishment (Andrighetto et al., 2016).
- **Production technology:**
    - In *weakest-link* (complementary) public goods, **punishment substantially increases efficiency**, even where it does not in a linear PGG (Fatas & Mateu, 2015).
- **Noise/information environment:**
    - Under *intermediate noise*, decentralized peer punishment can reduce efficiency due to excessive punishment; **centralizing punishment or reducing noise mitigates this** (Fischer et al., 2016).
- **Baseline efficiency (control):**
    - **If control efficiency is already high**, external (especially costly/probabilistic) punishment mechanisms can **reduce** group efficiency (Javaid & Falk, 2015).
- **Group composition and culture:**
    - The effect of punishment varies by cultural context and group composition; e.g., some cultures display high antisocial punishment, affecting efficacy (Fatas & Mateu, 2015; Espín et al., 2022).
- **Punishment institution (peer vs. central/external):**
    - Centralization removes perverse punishment but does not necessarily increase efficiency; effectiveness depends more on information and group structure (Fischer et al., 2016).

### c) CPR and close-variant environments:
- **Externally imposed punishment and rewards:** 
    - These *often* raise efficiency significantly when the control is below the social optimum (Wegmann & Musshoff, 2019; Xu et al., 2022).
    - *Magnitude matters*: High fines have larger and more persistent efficiency gains than low fines.
    - **But**: If prior efficiency is high, adding sanctions may worsen outcomes (Javaid & Falk, 2015).

### d) Sanctioning as ostracism
- **Ostracism (social exclusion)**
    - Robustly increases efficiency and payoff in dynamic/migration environments; **ostracism is rarely antisocial and more consistently beneficial than costly punishment** (Sääksvuori, 2014).

### e) Cases where punishment improves efficiency
- **When baseline efficiency is low, punishment is external, targeted, and the cost structure is favorable, efficiency gains are large and reliable** (Wegmann & Musshoff, 2019; Xu et al., 2022; Sääksvuori, 2014).

### f) Non-payoff findings warn about over-interpreting behavioral cooperation
- Many studies observe **increased cooperation rates** with punishment, but highlight that the **costs of administrating punishment often erase or outweigh these gains** in terms of group efficiency (Fischer et al., 2016; Grimalda et al., 2022).

### g) Reward mechanisms
- Where studied, **rewards have similar, sometimes slightly less positive, impacts on efficiency than punishment**, often without the risk of antisocial punishment (Wegmann & Musshoff, 2019).

# 5) Prediction Guidance

**When using this literature to predict average efficiency in PGG-like games with punishment enabled (compared to controls):**

- **Do not assume punishment increases efficiency.**
    - In *standard linear repeated PGGs*, especially with 4–5 players, moderate MPCR, and costly punishment, punishment *frequently fails* to increase efficiency (group payoff relative to optimum) and sometimes reduces it, particularly due to high punishment costs and antisocial punishment.
- **Context and dimension-level moderators are critical:**
    - *Communication*: Enabling chat or messaging (even at punishment/counter-punishment stage) can turn punishment from a net negative to a net positive for efficiency.
    - *Baseline efficiency*: If the control game is already highly efficient (e.g., due to strong social information, existing norms), punishment mechanisms tend to crowd out prosocial behavior or worsen efficiency.
    - *Production function*: Complementary production functions (e.g., weakest-link) are *much* more likely to see efficiency gains from punishment than standard linear PGGs.
    - *Punishment cost/magnitude*: Punishment must be potent, not too frequent/expensive, and structured to avoid antisocial targeting.
    - *Punishment institution*: Centralization can reduce perverse punishment but does not guarantee efficiency gain over decentralized punishment.
    - *Externalities/culture*: Culture, group composition, and history of norms critically moderate efficiency effects.
- **For CPR-like designs** (with natural resource extraction, external enforcement, low starting efficiency), punishment often gives clear efficiency gains.
- **Efficiency predictions** should use **control efficiency and the above moderators to set expectations**:
    - **If control efficiency is low, punishment is external, and high fines are used**, expect substantial gains in efficiency.
    - **If control efficiency is high or the punishment mechanism is peer-based in standard PGGs**, *do not expect efficiency improvements* and consider possible efficiency loss.
    - **Presence of communication increases the effectiveness of punishment on efficiency**.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- `player_count` and `num_rounds`: Well covered; most studies use 4–5 players and 10–30 rounds.
- `punishment_cost`, `punishment_tech`: Extensively manipulated—core to main findings.
- `chat`: Strong coverage for its presence/absence as a moderator of punishment efficacy.
- `all_or_nothing`: Reported (binary or continuous contributions), outcomes differ by structure.
- `mpcr`: Often specified; moderator of cooperation efficacy/predicted efficiency.
- `show_n_rounds`, `show_other_summaries`: Sometimes explicitly reported and analyzed (as in Sääksvuori, 2014).
- `reward_exists`/`reward_cost`/`reward_tech`: Included in select studies that test reward as an alternative or parallel to punishment.

**Indirectly Informed/Contextual:**
- `default_contrib`: Contribution framing is occasionally reported but not routinely manipulated as a treatment.
- `show_punishment_id`: Identities of punishers sometimes revealed, but rarely isolated as main treatment.
- `punishment_magnitude`: Usually coupled with punishment cost; often not separately varied.
- Other *institutional structure* variables (authority, monitoring, group feedback) are relevant but mapped only in some papers.

**Sparse or Missing:**
- *Several papers do not systematically report or manipulate design dimensions such as default contributions, visibility of punishers/rewarders, or reward magnitude*.
- **Few studies explicitly vary more than a handful of the 14 dimensions at once**, limiting granularity of prediction mapping.

# 7) Important Limitations

- **Limited reporting of directly relevant outcomes**: Many otherwise well-designed PGG/punishment studies do *not* report or analyze group efficiency/total payoff; instead, they focus on behavioral rates.
- **Sparse coverage of multi-dimensional interactions**: Most experiments alter *one or two* key design features at a time, limiting generalizability across the 14-dimension design space.
- **Cultural and ecological diversity**: Western lab samples dominate the "standard" PGG studies; external validity to other cultures, large groups, or longer games is limited.
- **Mechanism ambiguity**: Some conflicting or ambiguous results, particularly depending on baseline efficiency and the nature of antisocial punishment.
- **Adjacent games**: A significant fraction of adjacent or weak studies (trust games, dictator games, animal cooperation) offer only context, not direct guidance for prediction.
- **Reward mechanisms and hybrid institutions**: While a few studies address rewards, most focus squarely on punishment; highly coupled reward/punishment or dynamic institutions are underrepresented.
- **Rare attention to specific details**: Details such as punishment/reward visibility, exact identity disclosure, and contribution framing are inconsistently discussed or missing.
- **Outcome conflation**: Some studies report "group success" or "cooperation increases" where the mechanism is ambiguous or where efficiency gains are undermined by the cost of punishment.
- **Information structure complexity**: The importance of information structure (noise, identity, group feedback) is highlighted but not universally studied or standardized across papers.

---

**In summary**:  
The literature provides a nuanced, empirically grounded—but incomplete—basis for predicting the effect of enabling punishment on efficiency in public goods-like environments. The best-informed predictions are for standard linear repeated PGGs with 4–5 players: in these, punishment is often neutral or even detrimental to efficiency unless counteracted by communication or specific institutional design features. For CPR and non-linear games, external punishment can be highly effective if starting efficiency is low. The absence of efficiency reporting and multidimensional design coverage limits precision in predictions outside these well-studied designs.
