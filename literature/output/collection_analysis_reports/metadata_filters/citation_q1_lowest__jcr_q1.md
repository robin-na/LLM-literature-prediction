# 1) Evidence Base

The literature base for predicting the efficiency effect of enabling punishment in public-goods-game-like environments is both broad and deep. The reviewed set includes **a substantial number of high-quality empirical lab experiments, field experiments, and theory/simulation papers**—with many studies directly manipulating or analyzing punishment in classic Public Goods Games (PGGs) or very close institutional variants. Empirical papers often report both behavioral (contribution/cooperation) and payoff-based (efficiency, group earnings) outcomes, while theory and simulation papers enable detailed mapping of parameter regimes, mechanisms, and threshold effects. Meta-analyses, reviews, and comparative institutional studies round out the set, offering high external validity and coverage of edge cases. However, a nontrivial share of the literature—especially in adjacent variants (e.g., Prisoner’s Dilemma, trust games, or asymmetric institutional setups)—examine behavioral/psychological outcomes or mechanism/process arguments without direct measurement of efficiency.

**In summary:** The set is richest and most directly informative for experimental and theoretical studies of repeated, multi-player PGGs with explicit, costly, peer or centralized punishment, making it highly appropriate for the downstream prediction task. There remains, however, heterogeneity in reporting standards, context, outcome focus, and degree of direct applicability to all prediction dimensions.

# 2) Task Relevance

## a) `pgg_or_variant`
- **Relevance:** *exact* (for most of the core empirical/theory papers), *close* (for resource games, climate games, trust games with punishment, or PD-based work), and *adjacent* for studies in related but structurally different games.
- **Coverage:** The overwhelming majority of high-evidence papers explicitly study classic linear or all-or-nothing PGGs or immediately relevant institutional variants (collective-risk, resource games). Only a minority focus mainly on PD, trust, or other games with similar mechanisms but not PGG structure.

## b) `punishment_or_sanctions`
- **Relevance:** *exact* for the central literature—most studies manipulate peer, centralized, or institutional punishment as the main treatment or mechanism of interest. *Close* or *adjacent* relevance occurs where the main intervention is exclusion, reward, or reputation, or where punishment is only contextually discussed.
- **Coverage:** Direct measurement and manipulation of punishment parameters (cost, technology, effectiveness) are common; several studies also include anti-social punishment, third-party punishment, pre-committed/collective punishments, and hybrids with reward.

## c) `efficiency_or_related_payoff_outcome`
- **Relevance:** *exact* for many key empirical and theoretical papers reporting group earnings, welfare, or efficiency explicitly. *Close* when only adjacent measures (e.g., total welfare, group earnings, or surplus in non-PGGs) are reported or when only behavioral outcomes are measured but can be mapped to efficiency. *Adjacent* or *weak* for papers focusing solely on cooperation/contribution rates or psychological mechanisms.
- **Coverage:** Direct measurement of efficiency (group payoff relative to optimum) is common in high-impact studies, but a notable number of papers (especially in adjacent or nonstandard designs) focus on behavioral, normative, or psychological outcomes, requiring cautious mapping to efficiency.

# 3) Outcomes Measured In The Literature

**Payoff-related/efficiency outcomes**:
- *Direct measures:* Group earnings, total payoffs, average player income, efficiency ratios (actual/optimal), surplus, or welfare are frequently reported for both control (no-punishment) and punishment-enabled treatments.
- *Adjacently relevant measures:* Total contributions or public good provision (when cost of punishment is negligible or explicitly controlled) sometimes serve as a proxy for efficiency, but this can overestimate net welfare due to unmeasured costs associated with punishment.

**Non-payoff behavioral outcomes**:
- Contribution/cooperation rates are nearly ubiquitous as a primary outcome.
- Frequencies of punishment events, norm compliance, anti-social/prosocial punishment rates, beliefs, strategy distributions, and psychological variables (trust, status, emotion) are commonly measured, but do not directly index efficiency.
- Some simulation/theory studies infer efficiency via final state stability or cluster analysis—these must be interpreted cautiously.

**Distinction is critical:** Contribution/cooperation rates may rise with punishment, but efficiency can increase, decrease, or remain unchanged depending on the net cost of sanctions and their targeting (prosocial vs antisocial).

# 4) Main Findings Relevant To Prediction

**General patterns:**
- **Enabling punishment typically increases group efficiency when**:
  - *Punishment is targeted at defectors, costly enough to deter but not so costly as to outweigh gains* (Jiang & Wang, 2024; Castillo & Hamman, 2021; Krügel & Maaser, 2025; Nicklisch et al., 2021; Duell et al., 2024).
  - *Punishment is centralized or made more efficient through competition over punishment authority, institutional design, or collective/committed punishment* (Harrell, 2019; Krügel & Maaser, 2025; Duell et al., 2024; Ohdaira, 2025; Powers et al., 2023).
  - *Group structure is homogeneous and monitoring is accurate and affordable* (Molenmaker et al., 2023; Nicklisch et al., 2021; Zefferman, 2023).
- **The efficiency gain from punishment is highly sensitive to design parameters and context**:
  - *High punishment cost or poorly targeted punishment (including antisocial punishment) can erase or reverse efficiency gains* (Molenmaker et al., 2023; Nhim et al., 2023; Chen et al., 2025; Chen et al., 2021; Heine & Strobel, 2020; Milinski & Marotzke, 2022; Ezeigbo, 2017; Nhim et al., 2023).
  - *Reward and hybrid reward-punishment mechanisms often outperform pure punishment in terms of cost-effectiveness* (Makovi et al., 2025; Garrido et al., 2025; Lu et al., 2024; Wang et al., 2024).
  - *Social, demographic, or institutional heterogeneity (e.g., pluralism, open vs closed groups, hierarchy, status) can moderate or even nullify the benefit of punishment* (Molenmaker et al., 2023; Goto & Matsui, 2025; Vincent, 2017; Chen et al., 2025).
- **Enabling punishment does not guarantee improved efficiency**:
  - If the cost of punishment is high relative to the gain in cooperation, group efficiency can decrease (Heine & Strobel, 2020; Milinski & Marotzke, 2022; Nhim et al., 2023).
  - If punishment is voluntary/avoidable or easily subverted (through low ambition pledges, avoidance, or bribery), it may have no effect (Del Ponte et al., 2025; Goto & Matsui, 2025).
- **Baseline cooperativeness and institution history matter**:
  - If baseline (control) efficiency is high, marginal gains from enabling punishment can be small or negative, especially if punishment costs are not offset by additional cooperation.
  - Historical or facilitated group learning, leadership, or communication can determine whether punishment produces persistent efficiency gains (Harrell, 2019; DeCaro et al., 2024; Macleod et al., 2025).

# 5) Prediction Guidance

- **If the game design is a repeated, multi-player, linear or all-or-nothing PGG and the control (no-punishment) efficiency is low to moderate:**
  - *Prediction*: Enabling peer or institutional punishment is likely to increase efficiency, but the magnitude will depend on the cost/benefit ratio of punishment, monitoring accuracy/availability, targeting (prosocial vs antisocial), and group structure/homogeneity (Jiang & Wang, 2024; Castillo & Hamman, 2021; Krügel & Maaser, 2025; Zefferman, 2023; Powers et al., 2023).
  - *Modifiers*: Efficiency gains are larger when punishment is centralized, coordinated, or collective/committed, with reasonably low cost and high targeting selectivity. Efficiency is less improved—or even reduced—when punishment is costly, widely misapplied, antisocial, or subverted by group composition or institution design (Molenmaker et al., 2023; Nhim et al., 2023).
- **If control efficiency is already high:**
  - *Prediction*: The effect of enabling punishment is small or may be negative if punishment creates unnecessary costs (Kroupa, 2014; Nicklisch et al., 2021; Khatun et al., 2025).
- **If the game features collective, pre-committed, or institutionally organized punishment/coordination:**
  - *Prediction*: Larger and more persistent efficiency gains are likely, including in noisy monitoring conditions, when participants opt into commitment (Duell et al., 2024; Krügel & Maaser, 2025; Otten et al., 2024).
- **If the punishment regime is decentralized/peer-based, information is imperfect, or antisocial punishment is common:**
  - *Prediction*: Efficiency gains from punishment are reduced, can be null, or can easily be negative, especially as group size and cost of punishment rise (Molenmaker et al., 2023; Heine & Strobel, 2020; Ozono & Nakama, 2022; Ezeigbo, 2017).
- **In close or adjacent games (resource dilemmas, trust games, contests):**
  - *Prediction*: Similar patterns hold—punishment can increase efficiency only if well targeted, cost-effective, and not voluntarily avoidable. When punishment is profitable for the punisher (rather than costly), it can reduce efficiency and cooperation (Alam & Rai, 2025; Macleod et al., 2025).
- **Institutional context, leadership, communication, and transparency:**
  - Facilitated group learning, leadership with punishment authority, transparent norms, and accurate knowledge about others' endowments/behavior can all boost the efficiency benefit of punishment (Jiang & Wang, 2024; Castillo & Hamman, 2021; Chen et al., 2025; DeCaro et al., 2024).
- **Note**: Predicting efficiency under rare design features (opaque or ambiguous punishment, uncommon network/heterogeneity structures, unusual group sizes) is riskier due to sparse evidence.

## The implication for predictive modeling:
- Use control efficiency as a baseline but adjust for design moderators, especially those noted above. Incorporate direct evidence where available; for other dimensions, infer cautiously and preserve ambiguity. The absence of direct payoff/efficiency outcomes in some studies means behavioral evidence should only be used to adjust priors, not override direct payoff evidence.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions** (relevant for direct prediction calibration):
- `player_count` and `num_rounds`: Group size and game length are routinely manipulated and reported as moderators (e.g., Zefferman, 2023; Nicklisch et al., 2021).
- `mpcr`: Marginal per capita return is a fundamental parameter in both experimental and theory work; efficiency effects of punishment depend on whether cooperation is individually rational or not.
- `punishment_cost` and `punishment_tech`: Cost to punishers, punishment impact per unit, centralization vs peer punishment, and technological/structural features are critical and well covered.
- `all_or_nothing` and `default_contrib`: Several studies cover binary vs. continuous contribution and the effect of contribution framing.
- `chat`: The role of communication is frequently discussed; communication generally boosts baseline efficiency and can affect the impact of punishment.
- `reward_exists`, `reward_cost`, `reward_tech`: A number of core and adjacent studies investigate reward or hybrid mechanisms and their efficiency effects compared to punishment.
- `show_other_summaries`, `show_n_rounds`: Feedback and information provision are highlighted as moderators of the punishment effect, particularly the precision of feedback (Engel, 2019; Chen et al., 2025).
- `show_punishment_id`: Anonymity of punishment/defectors is a less common focus but is addressed in some central studies.

**Indirectly Informed or Contextually Discussed Dimensions**:
- `show_punishment_id`: Sometimes discussed in the context of anti-social/prosocial punishment and reputation effects.
- `group heterogeneity (not in explicit dimension list)`: Several high-relevance papers highlight the role of group composition, pre-existing norms, or endowment inequality.

**Sparse or Effectively Missing Dimensions**:
- `default_contrib` framing is less systematically explored, aside from specific framing experiments.
- `punishment_tech` is sometimes variably defined; some work uses broad categories (peer, central, rule-based) rather than fine technology details.
- Nonstandard dimensions such as nuanced feedback, variable punishment probabilities, or dynamic environmental feedback are only explored in a handful of theoretical or adjacent-variant papers.

# 7) Important Limitations

- **Efficiency vs behavior:** Many papers report only behavioral outcomes (contribution, cooperation, or rates of punishment) without direct mapping to net group efficiency, especially where punishment is costly or antisocial. Predicting efficiency gains from behavior-only evidence is risky and may overstate net welfare.
- **Contextual generalizability:** Strong evidence is limited to games structurally close to standard repeated PGGs under student-lab or stylized simulation conditions. Generalizing to large real-world groups, highly unequal settings, unfamiliar institutions, or field contexts introduces risk.
- **Parameter space coverage:** Some design dimensions—especially nuanced features of feedback, framing, institutional evolution, or rare variants—are only covered in theory with limited or no empirical calibration.
- **Ambiguity and non-monotonicity:** Some studies show that parameter effects are highly non-monotonic: increasing punishment cost, fine, or institutional complexity can both increase and decrease efficiency depending on other parameters and initial conditions.
- **Nonlinear, context-dependent mechanisms:** The efficiency effect of punishment is conditional on group structure, baseline cooperativeness, history, institution persistence, and anti-social punishment vulnerability. Evidence for strong negative effects (punishment reduces efficiency) is robust where punishment is costly and baseline cooperation is moderate.
- **Edge cases and missing evidence:** Some contexts—such as voluntary participation, pooled punishment, prosocial/antisocial punishment balance, and highly asymmetric reward/punishment—have only sparse empirical coverage. Some predicted effects (e.g., in pluralistic or very large groups) remain ambiguous in direction or magnitude.
- **Translation risk:** Evidence from adjacent games (trust, PD, resource dilemmas) or theoretical simulations needs careful adjustment before applying to real-world or standard lab PGGs due to structural differences.
- **Overreliance on PGG lab paradigms:** Some social contexts (normative enforcement, real-world anti-social punishment, networked or field settings) demonstrate mechanisms not easily reducible to the laboratory PGG paradigm. This limits certainty for predictions requiring ecological validity beyond standard lab games.

---

*This synthesis is based strictly on the evidence and findings provided in the supplied literature set. No outside claims have been introduced.*
