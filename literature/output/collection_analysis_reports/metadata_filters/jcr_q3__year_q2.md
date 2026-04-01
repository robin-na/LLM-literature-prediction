# 1) Evidence Base

The paper set comprises a broad mix of **empirical laboratory experiments** (especially on public goods games with and without punishment), **theoretical models** (evolutionary game theory, mechanism design, and network models), and a minority of **field or observational studies**. Overall, the set is **broad and rich** for the prediction task: many studies match the target domain—public goods games (PGG) or close variants—reporting both **payoff-based group outcomes** (efficiency, earnings, total payoff) and **behavioral outcomes** (cooperation rates, punishment frequency).

The set includes:
- Highly controlled lab experiments reporting direct measures of efficiency and earnings in PGGs with and without punishment.
- Theoretical models that explicitly solve for group efficiency as a function of key parameters and mechanisms.
- Studies varying critical design dimensions (e.g., group size, rounds, punishment/reward structure, information feedback, production function shape).
- Some adjacent studies on related social dilemmas, reputation, and common-pool resources, with both payoff and behavioral outcomes; a smaller number of empirical field observations and context-rich case studies.

There is good **coverage** of all major experimental design dimensions relevant for prediction. The empirical-to-theory mix leans empirical for PGGs, while theoretical coverage is especially strong on mechanism design, evolutionary stability, and variants. Some dimensions (e.g., specific combinatorial settings, large-group field trials) are less represented.

# 2) Task Relevance

Assessing the literature set along the three stated dimensions:

### a) `pgg_or_variant`
- **Exact**: The literature very frequently studies standard PGGs and close voluntary contribution mechanisms (VCMs); most experiments and many theory papers match the target well.
- **Close/Adjacent**: There are also studies with common-pool resource games, weakest-link production, trust/investment games, and repeated prisoner's dilemma; these are structurally close, though not strict PGGs.
- **Weak**: Few papers use very indirect analogies or contexts far from PGGs (only a handful).

### b) `punishment_or_sanctions`
- **Exact**: Direct, costly punishment options—peer or centralized—are commonly the focal intervention, with both empirical manipulation and theoretical analysis.
- **Close**: Some studies treat reward, exclusion, or indirect (reputation/social information-based) sanctions or have limitations (e.g., punishment is possible but used only rarely), or study institutional variants (delegated punishment, pool punishment).
- **Adjacent/Weak**: Weak coverage appears for "punishment-like" mechanisms (e.g., exclusion, insurance, voluntary vulnerability); some purely reputational or social norm studies.

### c) `efficiency_or_related_payoff_outcome`
- **Exact**: Many empirical and theory papers report efficiency as the group's total payoff relative to the maximal cooperative benchmark or report directly related earnings, welfare, or surplus.
- **Close**: Some studies use behavioral proxies (contribution rates, norm compliance) and infer payoff/efficiency changes via model structure, often in well-understood games; occasionally, group payoff is derivable from reported contributions.
- **Adjacent/Weak/None**: A subset only reports non-payoff behavioral outcomes or focuses on related but not equivalent outcomes (e.g., trust, participation, reputation, strategy abundance), and a few have only qualitative or mechanistic conclusions.

**Summary:** This collection is **highly relevant and well-matched** on all three axes for the downstream task of predicting efficiency impact of enabling punishment in PGG-like environments.

# 3) Outcomes Measured In The Literature

### Payoff-Related Outcomes (**Directly matching "efficiency"**)
- **Group efficiency**: Most empirical papers and many theoretical models directly report efficiency as actual group payoff divided by the maximum possible cooperative payoff (e.g., Kuwabara & Yu, 2017; Faillo et al., 2013; Fatas & Mateu, 2015; Reuben & Riedl, 2013).
- **Group earnings, welfare, surplus, etc.**: Used interchangeably with efficiency; sometimes group-level, sometimes average per player.
- **Explicit effect sizes for control (punishment off) and treatment (punishment on)**: Many studies allow clear mapping from design dimensions and control efficiency to predicted efficiency with punishment.

### Closely Related Outcomes (**Remappable**)
- **Contribution rate, cooperation rate**: Often matched one-to-one with group payoff in standard linear PGGs, but not always—for example, in nonlinear or threshold games; sometimes used as proxies in theory papers (e.g., conditional on MPCR).
- **Payoffs under complex interventions**: Some studies report proxies (e.g., maximum sustainable yield in resource games) or payoff at equilibrium/stationary distribution.
- **Strategy frequencies**: The fraction of cooperators/punishers/etc. at equilibrium, which can sometimes be mapped to efficiency with model knowledge.

### Non-Payoff Behavioral Outcomes (**Not directly matching efficiency**)
- **Punishment frequency, assigned punishment, norm compliance, trust, participation, reputation, response to social/normative cues**: Frequently measured in adjacent, mechanism-focused, or psychological studies (e.g., Seip et al., 2014; Mieth et al., 2017).
- **Qualitative mechanisms**: Casual or in-depth argumentation about how punishment, information sharing, or legitimacy shapes collective dynamics, without explicit payoff measures.

### Not Measured/Reported
- **Few studies** explicitly omit any efficiency or payoff outcomes, reporting only mechanisms or context.

# 4) Main Findings Relevant To Prediction

**Synthesis of the Literature's Most Useful Insights for Predicting Treatment Efficiency**:

### Empirical Core Findings

- **Enabling peer or centralized costly punishment frequently raises group efficiency versus no-punishment control, sometimes dramatically (20–50 percentage points), especially in standard linear PGGs with moderate MPCR and small to moderate group sizes** (Reuben & Riedl, 2013; Kuwabara & Yu, 2017; Faillo et al., 2013).
- **Punishment is most beneficial when**:
    - **Punishment is costly (not costless):** Costless punishment often leads to excessive, inefficient punishment and efficiency loss.
    - **Punishment is restricted/legitimate** (e.g., only high contributors can punish low contributors; feedback is present): greatly reduces antisocial punishment, increases efficiency (Faillo et al., 2013; Zheng & Nie, 2013).
    - **Information and feedback about group member contributions are fully available.**
    - **Communication is present:** Even limited chat or messaging in combination with punishment leads to higher efficiency; sometimes communication alone yields larger efficiency gains than punishment alone (Andrighetto et al., 2016; Zhosan & Gardner, 2013; Cason & Gangadharan, 2016).
    - **Punishment is not subject to anti-social or competitive dynamics:** Environments with high rates of antisocial punishment or unstable/unequal punishment power can see reduced, neutral, or negative effects on efficiency (Dorrough et al., 2017; Fatas & Mateu, 2015).

- **Punishment increases efficiency LESS or can even reduce efficiency when**:
    - **Antisocial punishment is present or possible:** Substantial antisocial punishment (low contributors punishing high contributors or undeserved punishment) can neutralize or reverse efficiency gains in some groups, often influenced by culture or institution design (Fatas & Mateu, 2015; Hauser et al., 2014).
    - **The punishment institution is poorly designed:** Unrestricted peer punishment, highly unequal or unstable punishment power, or corrupt enforcers yield lower, sometimes negative, efficiency effects (Zheng & Nie, 2013; Dorrough et al., 2017; Lee et al., 2015).
    - **The production technology is nonlinear or complex:** In non-linear or CPR-type settings, punishment alone often fails to raise efficiency (Cason & Gangadharan, 2016).
    - **Punishment cost is high and effectiveness is low:** The net efficiency effect is a non-monotonic function of cost and fine; mild but appropriately targeted punishment is often more efficient (Kamijo et al., 2014; Szolnoki & Perc, 2013).

- **Other moderators include**:
    - **Group size:** Effects of punishment can be stronger in large groups if coordinated or centralized punishment is possible; can also worsen inefficiency if antisocial punishment or noise is high and coordination is lacking (Zheng & Nie, 2013; Hwang, 2017).
    - **Institutional design:** Centralization vs. decentralization, threshold/weakest-link vs. linear production, and feedback all critically moderate efficiency effects.

### Theoretical Core Findings

- **Mechanisms:** Punishment enforces cooperation by making defection costly; however, its net effect on efficiency depends on whether punishment is used proportionately and without waste (Dercole et al., 2013; Oya & Ohtsuki, 2017).
- **Bistability and institutional trust:** When punishment institutions are susceptible to corruption (as in delegated punishment), efficiency can be high or low depending on initial fractions of honest enforcers or transparency (Lee et al., 2015, 2017).
- **Effectiveness depends on environment:** Structured populations, repeated interactions, and coordinated punishment make efficient cooperation more achievable (Oya & Ohtsuki, 2017; Olcina & Calabuig, 2015; Dercole et al., 2013).
- **Sanction mechanism details matter:** Conditional, graduated, or shared-cost punishments typically incur less cost and are more efficiency enhancing than unconditional or maximum-severity punishment (Szolnoki & Perc, 2013; Wright, 2013).

# 5) Prediction Guidance

Based on the synthesized literature, **downstream prediction of treatment (punishment-enabled) efficiency given game design and control efficiency should follow these principles:**

- **If the game is a standard linear PGG with moderate group size and MPCR, and the punishment stage is costly, restricted to legitimate uses (e.g., pro-social, contribution-based), and not subject to antisocial abuse, enabling punishment will likely yield a **substantial increase in efficiency** over the control (by 10–50 percentage points depending on exact parameters: Reuben & Riedl, 2013; Kuwabara & Yu, 2017).
- **If the punishment mechanism is costless, unrestricted, anti-social punishment is frequent, or punishment power is unequal and unstable, enabling punishment may result in **no efficiency gain or even a reduction in efficiency** due to resource burning and competitive punishment (Dorrough et al., 2017; Fatas & Mateu, 2015; Rockenbach & Wolff, 2016; Hauser et al., 2014).
- **Where both punishment and communication are enabled**, expect a larger effect on efficiency than from punishment alone; conversely, communication may sometimes fully substitute for punishment’s efficiency benefit (Andrighetto et al., 2016; Cason & Gangadharan, 2016).
- **Game structure matters greatly:** In weakest-link or threshold public goods games, introducing punishment dramatically increases efficiency even in contexts (e.g., cultures with anti-social tendencies) where it is less effective in linear PGGs (Fatas & Mateu, 2015).
- **Larger groups**: Efficiency gains from punishment are sustained or enhanced with group size if punishment is coordinated or centralized (Hwang, 2017; Dercole et al., 2013). But, with uncoordinated peer punishment or information noise, large groups can experience increased inefficiency (Zheng & Nie, 2013).
- **Institutional design and information feedback**: The degree of information about contributions, explicitness/legitimacy of sanctioning, and the presence of agreements/norms are important moderators of the treatment effect on efficiency (Faillo et al., 2013; Dannenberg, 2016; Kamijo et al., 2014).

**Thus:**
- **Use control (no-punishment) efficiency as a baseline**, but **adjust for key game dimensions**:
    - Strongly positive adjustment if design matches (legitimate, costly, visible, coordinated, or restricted punishment institutions in small groups with sufficient feedback).
    - Negligible or negative adjustment if costless/unrestricted punishment, high antisocial punishment, power instability, large unstructured groups, or noisy information.
    - Large positive adjustment under complementary production (weakest-link), ambitious group agreement plus punishment, or pool punishment institutions (when visible).
    - For complex, nonlinear, or common-pool resource games, expect little to no gain unless communication or group norm formation is present.

- **Punishment parameters to attend to**: cost to punisher, fine to target (cost:impact ratio), who is empowered to punish (peer/centralized/designated), ability to target, anonymity vs identifiability of punishment/rewarders, feedback structures, group size, and rounds.

- **Ambiguity and exceptions**: In environments with potential for meta-norm breakdown (e.g., frequent antisocial punishment, lack of punishment legitimacy, unstable role assignment), predictions are highly uncertain or may even go against standard intuition.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- `player_count` (group size): Heavily addressed; effect of punishment on efficiency is often moderated by group size and player matching structure.
- `num_rounds`: Standard variation; longer repeated games often sustain higher cooperation and more stable efficiency under punishment, but fatigue and declining cooperation are possible.
- `chat`: Communication effects are robustly tested. Presence of chat or messaging strongly moderates punishment’s effect on efficiency.
- `mpcr`: Extensively varied in both empirical and theory papers. Critical for baseline efficiency and for the magnitude of punishment effect.
- `punishment_cost`, `punishment_tech` (e.g., peer vs centralized, cost per unit, effectiveness per unit): Almost always specified and systematically manipulated in many studies.
- `show_other_summaries`, `show_n_rounds`, `show_punishment_id`: Information feedback and transparency are frequently manipulated and found pivotal in moderating the efficiency effect.
- `reward_exists`, `reward_cost`, `reward_tech`: Less frequently manipulated, but dimension is present; some experiments directly contrast reward and punishment or examine hybrid institutions.
- `all_or_nothing`, `default_contrib`: Production function variants (all-or-nothing, weakest-link) and framing/manipulation of contribution defaults are explored, but not as systematically as other factors.

**Indirectly Informed Dimensions:**
- `show_punishment_id`: The role of identifiability in punishment effectiveness is addressed, most clearly in studies on legitimacy and reputation, but sometimes only discussed or in context, not directly manipulated in PGGs.
- `reward_cost`, `reward_tech`: Often contextual, more prominent in theory or hybrid studies.

**Sparse or Missing:**
- Multi-dimensional institutional complexity (e.g., simultaneous reward and punishment, or rapid changes in institution over time): much less direct evidence; only some theory papers model these.
- Edge-case settings: e.g., extremely large groups in field conditions, pure observational or naturally-occurring games beyond lab/agent-based models (these are infrequent).

# 7) Important Limitations

- **Heterogeneity of experimental and institutional detail**: Game design features and payoff structures often interact in untested or underexplored ways. Cross-study generalization is thus subject to institutional dependency and confounding between dimensions.
- **Antisocial and competitive punishment is still poorly predictable:** While its impact is acknowledged, there are limited predictive tools for when antisocial punishment will dominate versus be minimal, except for coarse cultural or institutional correlates.
- **Complex real-world environments**: Lab results may overestimate the positive efficiency effects of punishment compared to field, networked, or naturally heterogeneous populations (Berger & Hevenstone, 2016).
- **Sparse coverage of non-linear or ecological environments:** Most strong evidence is from linear or simple additive PGGs; prediction in nonlinear CPRs or highly dynamic environments is less certain (Cason & Gangadharan, 2016; Lee et al., 2017).
- **Reward, exclusion, and hybrid institutions:** Although included in some papers, these are less systematically explored, limiting prediction accuracy where punishment is embedded in richer institutional contexts.
- **Temporal and evolutionary dynamics:** Many models focus on equilibrium or long-term outcomes, but "static" empirical effects may not hold in longer-run evolutionary or repeated play with turnover, learning, or changing group composition.
- **Substantial sensitivity to 'soft' moderators**: Legitimacy, perceived fairness, information structure, and group culture can cause high variance in outcomes even with similar technical parameters.
- **Behavioral outcome mapping:** In some studies, efficiency must be inferred from contribution rates, strategy frequencies, or experimental parameters, which is valid in standard linear PGGs but less reliable in nonlinear or complex settings.

---

## *References (APA-style):*
(Dorrough et al., 2017; Kuwabara & Yu, 2017; Faillo et al., 2013; Andrighetto et al., 2016; Fatas & Mateu, 2015; Fischer et al., 2016; Zheng & Nie, 2013; Dannenberg, 2016; Kamijo et al., 2014; Reuben & Riedl, 2013; Rockenbach & Wolff, 2016; Hauser et al., 2014; Hwang, 2017; Kamijo et al., 2014; Zhosan & Gardner, 2013; Cason & Gangadharan, 2016; Lee et al., 2015; Lee et al., 2017; Oya & Ohtsuki, 2017; Dercole et al., 2013; Szolnoki & Perc, 2013; Wright, 2013.) [This list is illustrative; cite supplied digest lines for specific claims.]
