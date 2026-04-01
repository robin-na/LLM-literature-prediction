# 1) Evidence Base

The paper set comprises a mix of empirical and theoretical studies, with a clear preponderance toward theory-heavy, broad-context literature. Only two papers are strictly empirical, lab-experimental studies directly manipulating punishment availability in standard public goods games (PGG) and measuring efficiency or closely related payoff outcomes (Grechenig et al., 2010; Brick & Visser, 2010). The majority are theoretical or review-based, deriving propositions from evolutionary theory, modeling, or qualitative synthesis (e.g., Rosas, 2008; Kraak, 2011; Frey & Rusch, 2012). The theory-focused works cover a wide array of settings from trust-games and PGGs to general social dilemmas, moral norm enforcement, and animal cooperation. Empirical papers are generally more narrowly focused on core PGG structures, while theory papers often generalize across game forms and punishment mechanisms.

Overall, for the downstream prediction task—forecasting treatment efficiency given control efficiency and design dimensions—the evidence base is relatively broad-conceptual, but only a minority of studies offer direct empirical input under precisely matching conditions.

# 2) Task Relevance

### `pgg_or_variant`
- **exact**: 5 papers explicitly focus on PGGs or variants (Grechenig et al., 2010; Rosas, 2008 [Reciprocity]; Frey & Rusch, 2012; Kraak, 2011; Brick & Visser, 2010).
- **close/adjacent/weak**: The remaining papers are adjacent (trust games, prisoner’s dilemma, general cooperation), supporting similar logic but differing in payoff structure or dynamics.

### `punishment_or_sanctions`
- **exact**: 7 papers directly address peer punishment or sanctions in the PGG context (e.g., Grechenig et al., 2010; Rosas, 2008; Frey & Rusch, 2012; Woodcock & Heath, 2002).
- **close/adjacent**: Some papers emphasize broader sanction concepts, such as exclusion, reputation, or institutional punishment rather than purely peer-based costly punishment (e.g., Sripada, 2005; Brick & Visser, 2010).

### `efficiency_or_related_payoff_outcome`
- **exact**: Only a handful directly report on efficiency or closely related aggregate payoff outcomes (Grechenig et al., 2010; Rosas, 2008; Frey & Rusch, 2012; Kraak, 2011; Bicchieri et al., 2004).
- **adjacent/weak**: Many others report only behavioral outcomes such as cooperation rates, punishment frequency, norm compliance, or theoretical implications for group success without explicitly quantifying efficiency (e.g., Woodcock & Heath, 2002; Dugatkin, 2002).

# 3) Outcomes Measured In The Literature

### Payoff-Related Outcomes
- **Efficiency (group payoff/maximum possible):** Explicitly reported and analyzed in a few core PGG and theory papers (Grechenig et al., 2010; Rosas, 2008; Frey & Rusch, 2012; Kraak, 2011).
- **Group payoff/total earnings/welfare:** Sometimes discussed as surrogates or in the form of "compliance with group target" (Brick & Visser, 2010).
- **Trust-game payoffs:** Bicchieri et al. (2004) report average payoffs as a function of rounds in trust games, not PGG.

### Non-Payoff Behavioral Outcomes
- **Cooperation/contribution rate, compliance:** Frequently assessed, especially when efficiency/payoff is missing (Woodcock & Heath, 2002; Dugatkin, 2002; Brick & Visser, 2010).
- **Punishment frequency/assignment, norm adherence:** Often measured (Grechenig et al., 2010; Rosas, 2008 [Reciprocity]) but less relevant for direct efficiency prediction.

**Notably, there is an overrepresentation of non-payoff behavioral outcomes, with relatively few papers reporting efficiency or welfare as defined for the downstream task.**

# 4) Main Findings Relevant To Prediction

Synthesizing across the most relevant papers:

- **Punishment and Efficiency:** 
  - Enablement of peer punishment in repeated PGGs can **increase efficiency** above the no-punishment baseline, but only when contextual moderators are favorable (Grechenig et al., 2010; Kraak, 2011; Frey & Rusch, 2012).
  - **Critical moderators for positive efficiency effect:**
    - **Accurate information about others’ contributions:** Punishment increases efficiency when information is precise; it can lower efficiency below control when noise is introduced, due to mistargeted or antisocial punishment (Grechenig et al., 2010).
    - **Longer time horizon (number of rounds):** Negative efficiency effect in short games (once costs are counted), but in long games (20+ rounds) with stable groups, overall efficiency with punishment can surpass the control, as punishment becomes less necessary over time (Frey & Rusch, 2012).
    - **Punishment effectiveness:** When punishment is strong and cost-effective (high impact per unit cost), efficiency gains are more likely (Frey & Rusch, 2012; Rosas, 2008 [Reciprocity]).
    - **Communication and reputation:** Supporting mechanisms for reputation or chat/communication further amplify positive efficiency effects, making peer punishment more targeted and less destructive (Kraak, 2011).
  - **Peer punishment is not always beneficial:** Under uncertainty/noise, short games, or high punishment costs, enabling punishment can make the group worse off due to excessive “wasteful” punishment (Grechenig et al., 2010; Rosas, 2008 [Reciprocity]).

- **Sanction Type and Dynamics:**
  - **Automatic/institutional punishment (tax/fine):** Highly effective at achieving compliance with group targets, but can crowd out voluntary contributions above the threshold, and efficiency not always directly measured in optimal terms (Brick & Visser, 2010).
  - **Exclusion/reputation-based sanctions:** Theoretically, these can be more efficient and stable than costly direct punishment where such mechanisms are allowed (Rosas, 2008 [Reciprocity]; Sripada, 2005), but few empirical papers test these forms directly in PGGs.

- **Non-payoff outcomes:** Across many theoretical papers, the persistence of cooperation via punishment is emphasized, either through evolutionary stability (Woodcock & Heath, 2002; Dugatkin, 2002), norm enforcement (Sripada, 2005), or group selection dynamics (Rosas, 2008 [ML selection]), but these arguments do not robustly translate into payoff-based efficiency without explicit modeling or empirical validation.

# 5) Prediction Guidance

The available literature provides several empirically and theoretically supported guidance points for prediction models of treatment efficiency with peer punishment:

- **Baseline efficiency is necessary but not sufficient:** The observed efficiency of the control (no-punishment) condition sets the reference point, but **the marginal effect of enabling punishment depends critically on other design dimensions** (Grechenig et al., 2010; Frey & Rusch, 2012).
- **Design moderators to prioritize** (ordered by evidence strength from the literature):
  - **Information accuracy** (not a direct input among the 14 dimensions but related to `show_other_summaries`): If players have reliable summaries of contributions, punishment is more effective for efficiency; with uncertainty/noise, it can be destructive (Grechenig et al., 2010).
  - **Number of rounds** (`num_rounds`): Longer games support efficiency gains with punishment, especially with stable group composition (Frey & Rusch, 2012).
  - **Punishment parameters** (`punishment_cost`, `punishment_tech`): Lower costs and higher effectiveness per unit punishment facilitate positive efficiency effects; high costs or weak impact reduce or reverse gains (Rosas, 2008 [Reciprocity]; Frey & Rusch, 2012).
  - **Chat/communication** (`chat`): Presence of communication channels amplifies efficiency gains from punishment by facilitating coordination and reducing mispunishment (Kraak, 2011).
  - **Reputation/transparency** (related to `show_punishment_id`, possibly `reward_tech`, and external to listed dimensions): Reputation or identification mechanisms facilitate targeted punishment and efficiency improvement (Kraak, 2011).
- **Other dimensions (player count, MPCR, all-or-nothing):** Indirectly discussed, with several papers suggesting larger group size and group heterogeneity do not negate punishment’s positive effect but may require strong sanction/reputation mechanisms (Sripada, 2005; Dugatkin, 2002).

In practice, **predictive models should adjust the expected efficiency uplift from enabling punishment upward in long, stable, transparent, communicative, and low-noise environments, and downward—or anticipate negative effects—when these conditions are absent.**

# 6) Design Dimensions Highlighted Across Papers

**Directly informed (feature supported by direct findings relevant to efficiency):**
- `player_count`: Group size manipulated or discussed in several papers, especially regarding scaling of punishment/cooperation (Grechenig et al., 2010; Kraak, 2011; Sripada, 2005).
- `num_rounds`: Strongly emphasized as a moderator of efficiency effect (Frey & Rusch, 2012; Bicchieri et al., 2004).
- `mpcr`: Manipulated in empirical/theory models; higher values typically support cooperation (Grechenig et al., 2010; Kraak, 2011).
- `punishment_cost`, `punishment_tech`: Strong support that cost and technology moderate efficiency impact (Grechenig et al., 2010; Rosas, 2008; Frey & Rusch, 2012).
- `chat`: Highlighted as a cooperation/efficiency amplifier (Kraak, 2011).
- `all_or_nothing`: Studied as a variant, with mostly indirect evidence (Grechenig et al., 2010; Kraak, 2011).
- `reward_exists`: Discussed as a complementary/alternative cooperation-enforcement mechanism (Raihani & Aitken, 2011).

**Indirectly informed or contextually discussed:**
- `show_other_summaries`, `show_punishment_id`: Linked theoretically to information/reputation effects, with only indirect empirical evidence (Kraak, 2011; Grechenig et al., 2010—in context of information accuracy but not direct manipulation of summary visibility).
- `reward_cost`, `reward_tech`: Discussed as comparisons (Raihani & Aitken, 2011), but few direct efficiency results.
- `default_contrib`, `show_n_rounds`: Touched on in theory models (Bicchieri et al., 2004) and design context, but no strong empirical test.

**Effectively missing (limited or no data on efficiency impact):**
- `reward_cost`, `reward_tech` (direct manipulation for efficiency not present).
- `default_contrib` (contribution frame rarely discussed with respect to payoff).
- `show_n_rounds` (mainly theoretical discussion).
- Any dimension relating to specific identity tracking or complex reputation tech beyond communicative context.

# 7) Important Limitations

- **Limited direct empirical evidence**: Only a small number of studies (notably Grechenig et al., 2010; Brick & Visser, 2010) offer direct, quantitative efficiency outcomes for PGGs with and without punishment.
- **Non-payoff emphasis in much of the literature**: Many theory and review papers focus on cooperation rates or evolutionary persistence rather than directly measurable efficiency or payoffs.
- **Factors Exogenous to Core Dimension List**: Some empirically critical moderators (especially information/noise, group stability/matching protocol, reputation mechanisms) are not neatly mapped by the 14 dimensions, creating ambiguity in prediction when such features are present or absent in the target environment.
- **Diverse punishment mechanism types**: Literature mixes direct costly punishment, exclusion, tax/fine, and reputation sanctions. Efficiency impacts can differ; this heterogeneity is not always explicitly delineated.
- **Population and context differences**: Lab PGGs, evolutionary models, and field analogues (e.g., fisheries, climate games) may yield different effects due to population composition, social context, and framing.
- **Ambiguity regarding negative effects**: Under certain conditions (noise, mispunishment, high cost, short run), enabling punishment can reduce efficiency—a caution that should be explicitly carried in prediction models (Grechenig et al., 2010).
- **Missing detail on reward structures**: The interaction of reward and punishment features is discussed theoretically, but payoff data on alternative or complementary reward mechanisms are sparse.

In conclusion, **while the literature supports a conditional efficiency-enhancing role for peer punishment in PGGs, downstream efficiency prediction should be strongly moderated by information accuracy, time horizon, punishment parameters, and the presence of communication and reputation mechanisms.** Blind assumption of positive effects from enabling punishment is not justified across all design spaces.
