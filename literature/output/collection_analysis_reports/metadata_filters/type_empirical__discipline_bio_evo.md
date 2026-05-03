# 1) Evidence Base

The literature base consists of a large, diverse set (n=132 papers), dominated by empirical laboratory and field experiments, with a minority of theoretical and observational studies. The empirical core is relatively broad with respect to games like the linear Public Goods Game (PGG), its major laboratory variants, and real-world close analogues (common-pool resource games, collective risk dilemmas). There is substantial direct evidence for games that are structurally and payoff-identical to classic lab PGGs, as well as for CPR and threshold games that retain group contribution/extraction dilemmas with variable institutional settings. Most papers explicitly test the effects of enabling punishment or sanctioning options versus control conditions, and a significant subset report on payoff-based outcomes, including total group payoff, efficiency (defined as realized over maximum possible payoff), welfare, or surplus.

The evidence includes several multicountry/cross-cultural studies, a range of punishment institution types (peer, centralized, pool, external), variations in information, player composition, and sanction/reward cost structures. However, a large fraction of studies focus on behavioral mechanisms (contribution rates, norm compliance, punishment frequency) rather than efficiency or total payoff per se; mechanistic/psychological studies are especially common in the "adjacent" literature that includes non-PGG games like Dictator, Trust, and Ultimatum Games.

## Breadth vs. Narrowness

For the downstream task—predicting treatment efficiency from control efficiency and game design dimensions when peer punishment is enabled—the empirical literature provides a strong, but also complex and sometimes fragmented, evidence base. Some game design variables are well covered (e.g., `player_count`, `mpcr`, `punishment_cost`, punishment technology, institution type), while other dimensions (e.g., chat, reward regimes, detailed visibility or framing) are less systematically tested. Evidence for real-world and field variants extends generalizability but also introduces contextual moderators such as baseline trust, local norms, and institution legitimacy.

# 2) Task Relevance

**a) PGG or variant**:  
- Many high-relevance papers use the exact repeated linear PGG (e.g., Gächter et al., 2017; Egas & Riedl, 2008; Fischer et al., 2016; Andrighetto et al., 2016), granting `exact` relevance.  
- Several studies employ close variants (e.g., CPRs: Vollan, 2008; Javaid & Falk, 2015; Xu et al., 2022), yielding `close` relevance.  
- A substantial number are `adjacent` (Ultimatum/DG/Trust games), informative on behavioral mechanisms but less on group efficiency in PGGs.  
- Some papers on natural mutualisms or observational fieldwork score as `weak` or `none`.

**b) Punishment or sanctions**:  
- Numerous studies implement classical peer or centralized costly punishment mechanisms (`exact`), including both lab and field treatments.
- Others investigate modifications (e.g., counter-punishment, pool punishment, ostracism) or only discuss punishment contextually (`close` or `adjacent`).
- Some reward-only or reputational mechanism papers are only `adjacent` or `weak`.

**c) Efficiency or related payoff outcome**:  
- A core subset report directly on efficiency or group payoff (`exact`), often with explicit control and punishment conditions (e.g., Gächter et al., 2017; Sääksvuori et al., 2011; Wegmann & Musshoff, 2019).
- Many others report only behavioral indices—contribution rates, punishment assigned, norm compliance (`adjacent` or `close`).
- Some studies do not report any payoff-based outcome (`none`).

**Summary:**  
- Papers that are `exact-exact-exact` form the strongest, directly relevant base for the downstream efficiency prediction task. However, contextual and institutional moderators, as well as limitations in the reporting of payoff outcomes (including lack of direct comparison between control and treatment efficiency), mean that prediction is best informed by a weighted synthesis across these papers.

# 3) Outcomes Measured In The Literature

**a) Payoff-based outcomes (efficiency, group payoff, welfare, surplus):**
- A substantial subset of studies report explicit measures of efficiency (ratio of actual to maximum payoffs) or total group earnings as the primary outcome (e.g., Gächter et al., 2017; O'Gorman et al., 2009; Sääksvuori et al., 2011; Sparks et al., 2024).
- Some studies use payoff measures as secondary outcomes or report aggregate surplus but focus primarily on behavioral variables.
- CPR and close-variant studies typically translate extraction/conservation rates directly into efficiency or welfare figures (e.g., Wegmann & Musshoff, 2019; Vollan, 2008; Javaid & Falk, 2015).

**b) Non-payoff behavioral outcomes:**
- The majority of studies measure and report group average contribution, punishment frequency, cooperation rate, and norm compliance.
- Studies on mechanisms (e.g., neural, psychological, or social drivers) tend to use these as their primary dependent variables.
- In some cases, behavioral outcomes are the only reported results, and efficiency must be inferred indirectly (or is unavailable).

**Note:** For the prediction task, only direct payoff-based outcomes meaningfully inform estimates; contribution rates and compliance are at best indirect proxies.

# 4) Main Findings Relevant To Prediction

**Empirical synthesis:**
- **Punishment often increases cooperation and, in many standard linear PGGs, raises efficiency relative to control, particularly when punishment is effective (low cost/high impact) and antisocial punishment is rare (Gächter et al., 2017; Sparks et al., 2024; O'Gorman et al., 2009).**
    - In these settings, group efficiency moves from moderate/low in the control to near social optimum with punishment enabled, sometimes overcoming the cost of punishment.
- **The efficiency gains from punishment are contingent:**  
    - When antisocial punishment is common, or punishment is used non-strategically (e.g., in some cultures), costs can outweigh gains, leading to reduced or unchanged efficiency (Fatas & Mateu, 2015; Burton-Chellew & Guérin, 2021).
    - In some CPR and threshold games, or field experiments with high existing compliance or strong prosocial norms, the introduction of external punishment can reduce efficiency due to crowding-out, increased coordination problems, or wasted resources (Vollan, 2008; Javaid & Falk, 2015).
- **Institutional form is critical:**  
    - Centralized (single or pool) punishment can reduce perverse punishment but does not always outperform decentralized peer punishment for efficiency; both forms can fail to increase efficiency if information is poor or if punishment costs are high (Fischer et al., 2016; Traulsen et al., 2012).
    - Designated (single) punisher regimes can be more efficient than diffuse ones by preventing redundant punishment (O'Gorman et al., 2009).
- **Design dimensions and moderators stand out as critical:**  
    - Communication strongly amplifies efficiency gains from punishment (Andrighetto et al., 2016).
    - The production function matters: punishment is much more effective at raising efficiency in weakest-link or complementary production functions than in linear ones (Fatas & Mateu, 2015).
    - Intergroup competition or additional institutional complexity may be required for positive efficiency effects in some settings (Sääksvuori et al., 2011).
    - Bribery/corruption opportunities, when enabled, can completely reverse expected punishment effects, decreasing efficiency (Muthukrishna et al., 2017).
    - Cultural background, baseline prosociality, and local norms (e.g., crowding-out under low legitimacy or in high-trust groups) are strong cross-study moderators.
- **In some settings, punishment reliably fails to raise efficiency (or reduces it):**
    - With high punishment costs, low impact, or frequent antisocial punishment (Egas & Riedl, 2008; Burton-Chellew & Guérin, 2021), group payoffs in the punishment condition lag behind control, even if contributions are higher.
    - Likewise, when the control efficiency is already high (e.g., due to social information or strong norms), the addition of punishment may decrease efficiency (Javaid & Falk, 2015).

# 5) Prediction Guidance

Given the above evidence, **the literature provides the following key implications for the downstream prediction task**:

- **Predicted treatment efficiency should not be mechanically assumed to increase with punishment enabled; instead, it is strongly moderated by core design, context, and baseline efficiency.**
    - If control (no-punishment) efficiency is low to moderate, and design parameters match those of linear repeated PGGs with small groups, moderate MPCR, and standard (effective) peer punishment—**treatment efficiency is likely to rise substantially when punishment is enabled** (Gächter et al., 2017; Sparks et al., 2024).
    - If control efficiency is already high (due to existing norms, communication, or public information), enabling punishment may produce little or even negative change in efficiency (Javaid & Falk, 2015; Vollan, 2008).
    - When antisocial punishment is prevalent, or punishment is costly and impact is weak, efficiency gains are neutral or negative—even if contributions rise (Egas & Riedl, 2008; Fatas & Mateu, 2015; Burton-Chellew & Guérin, 2021).
    - The production function/structure and cultural context can lead to reversal of expected effects (Fatas & Mateu, 2015; Muthukrishna et al., 2017).
- **Institutional specification (e.g., peer vs. centralized, voluntary vs. imposed, ability for counter- or second-order punishment) should be modeled as a dimension, since it can moderate or invert efficiency effects.**
    - “Pool” or centralized punishment often increases cooperation but can lead to greater efficiency loss via higher direct costs (Traulsen et al., 2012).
- **Critical design dimensions for prediction (see below) must be included, and missing them undermines prediction accuracy.**
- **Behavioral changes (increased cooperation/contributions) cannot be assumed to directly raise efficiency, as punishment costs may outweigh gains.**

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- `player_count`, `num_rounds`, `mpcr`, `punishment_cost`, `punishment_tech` — Almost all "exact" empirical PGG studies specify and experimentally manipulate these.
- `all_or_nothing` — Some studies identify effects specific to binary/continuous contribution mode (e.g., Traulsen et al., 2012).
- `chat` — A subset of studies document the critical impact of chat/communication (Andrighetto et al., 2016).
- `reward_exists`, `reward_cost`, `reward_tech` — Comparatively fewer, but some field/CPR experiments include and report effect sizes for reward alongside punishment (Wegmann & Musshoff, 2019).
- `default_contrib` — Framing and opt-in/out manipulations are reported in a few cases but less systematically.
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id`—Some variation in information structure is reported (e.g., fixed IDs, summary info, anonymity of sanctions), but these are less consistently analyzed for impact on efficiency.
- **Indirectly Informed**: Some papers discuss these dimensions in the context of mechanism but lack explicit manipulations comparing levels.
- **Contextually Discussed or Missing**: For counter-punishment, bribery, or institutional legitimacy, qualitative or indirect evidence points to these features as critical, but with sparse quantitative effect sizes.

# 7) Important Limitations

- **Not all design dimensions are equally or adequately covered**; for instance, nuanced features like `default_contrib`, `show_punishment_id`, or specific reward mechanisms have rare or inconsistent manipulation.
- **Culture, norms, and institutional details—often not captured by standard design variables—strongly moderate efficiency effects** (Gächter, Herrmann, & Thöni, 2010; Vollan, 2008; Javaid & Falk, 2015), limiting out-of-sample generalizability of purely design-based predictions.
- **Most evidence is lab-based; some field and real-world analogues exist but are context-sensitive, often driven by factors hard to encode as design variables (e.g., trust, resource dependence, legitimacy).**
- **Efficiency improvements from punishment are contingent, not universal; in many classic settings, punishment can reduce efficiency due to cost, errors, or perversity (Egas & Riedl, 2008; Burton-Chellew & Guérin, 2021).**
- **Many studies report contribution rates as outcomes, which are insufficient for the downstream prediction task; proper prediction requires data on group payoff relative to the social optimum.**
- **Some variants (weakest-link games, voluntary games, CPRs with high baseline efficiency) show effects that may be reversed compared to classic linear PGGs.**
- **There is ambiguity and even disagreement: some papers identify positive, some negative, and some null or mixed effects for nominally similar institutional changes, underscoring the importance of specific context and moderators.**
- **Rarely are all 14 design variables manipulated within the same paper—some must be inferred or extrapolated.**
- **Corruption/bribery options and the potential for counter-punishment are only explored in a minority of papers, but when present, can fundamentally change efficiency effects, so gaps in coverage of these features are significant.**

---

**In summary:**  
The literature base provides robust evidence that the effect of enabling punishment in public-goods-game-like environments on efficiency depends heavily on the core game design, the initial level of efficiency, institution type and legitimacy, cultural context, the production function, and the moderation by communication or information. There is no support for the universal prediction that punishment raises efficiency; rather, the relationship is contingent and nonlinear. For prediction, design-informed models should consider these moderators carefully and avoid extrapolating from behavioral increases in cooperation to increases in efficiency without considering punishment costs and context.
