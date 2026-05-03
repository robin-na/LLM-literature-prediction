# 1) Evidence Base

The paper set is very large (101 papers) and overwhelmingly theoretical, with a strong focus on modeling, mechanism, and evolutionary explanation rather than new experimental or empirical evidence. It is relatively broad in scope, ranging from laboratory-standard public goods games (PGGs) with explicit payoff-based outcomes to adjacent or structurally similar games (e.g., trust games, prisoner's dilemma, governance games) and non-payoff measures (e.g., cooperation rates).

Empirical evidence (i.e., new experimental data or payoff results from actual PGG experiments) is mostly lacking; rather, findings are derived from analytical models, simulations, or meta-syntheses of existing studies. A minority of papers include meta-analyses or syntheses of experimental studies (e.g., Vasconcelos et al., 2022; Kraak, 2011), which confer some empirical grounding. The bulk of the literature engages in theoretical exploration of mechanisms, design features, and moderators of punishment’s effect, often spatial or evolutionary game theory based.

As such, the scope is broad for mechanism and design discussions, but narrow in terms of directly comparable, empirical, payoff-based PGG treatments.

---

# 2) Task Relevance

### `pgg_or_variant`
- **Exact relevance**: About 10–15 papers are directly about PGGs or closely matched variants; several others treat close relatives (threshold PGGs, continuous PDs, trust games).
- **Close/Adjacent relevance**: Most others are adjacent, addressing coordination games, multi-actor regulatory games, or evolutionary models with public-goods-like structure.
- **Weak/None**: About a quarter are only contextually related or entirely outside the PGG framework.

### `punishment_or_sanctions`
- **Exact relevance**: Around half the set, including key theory and meta-syntheses, treat punishment/sanctioning directly—both formal (institutions) and informal (peer-to-peer).
- **Close to Adjacent**: Many discuss closely associated mechanisms (reputation-based exclusion, signaling, policing, retaliation, etc.), but not always as directly manipulable game features.
- **None or Weak**: A substantial minority only mention punishment contextually.

### `efficiency_or_related_payoff_outcome`
- **Exact relevance**: Only a small subset (≈10) report or model actual efficiency, group payoff, welfare, or surplus; more deal with close proxies (group success rates, surplus, average earnings).
- **Close**: Many more papers take cooperation rate, compliance, or norm adherence as primary outcomes. Explicit notes in the digests caution these are not efficiency, but related.
- **Weak/None**: Around half the papers do not address payoff-based outcomes directly; some focus exclusively on evolutionary prevalence, behavioral norms, or conceptual discussions.

**Summary:** The set contains several highly relevant theory papers for all three dimensions, but the bulk of empirical or synthetic evidence is indirect, with frequent reliance on adjacent games, mechanisms, or behavioral outcomes. This constrains the granularity and specificity at which predictions of average treatment efficiency can be made.

---

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes (Relevant for Prediction)**  
  - **Efficiency (defined as total group payoff / full cooperation benchmark)**  
    Reported or theoretically analyzed in some key PGG or variant models (e.g., Zhang & Cao, 2020; Vasconcelos et al., 2022; Frey & Rusch, 2012; Liu et al., 2019; Vlerick, 2016; Kraak, 2011; Xu et al., 2014; Zhang & van der Schaar, 2013).
  - **Group Payoff/Total Earnings/Surplus**  
    Reported in a handful of adjacent or exact studies, often as a proxy for efficiency.
  - **Average Earnings/Group Welfare**  
    Modeled in adjacent trust games, CP/PB games, regulatory settings.
- **Non-Payoff (Behavioral) Outcomes**  
  - **Cooperation Rate/Contribution Rate/Compliance**: Most commonly reported, particularly in spatial, evolutionary, or agent-based models (e.g., cooperation density in spatial PGGs).
  - **Prevalence of Honest Reporting, Norm Compliance, Defection Rate**: Frequent in social dilemma, governance, or norm enforcement models.
  - **Strategy Prevalence, Evolutionary Stability, Equilibrium Profiles**: Often primary in evolutionary or conceptual models.
- **Explicit Cautions**  
  Many summaries explicitly distinguish that higher cooperation, compliance, or punishment frequency does **not necessarily equate to higher efficiency** due to costs of punishment or possible overuse, or due to possible presence of covert defection.
- **Combinations and Meta-Outcomes**  
  Some theory papers or reviews attempt to connect behavioral dynamics to expected payoff outcomes.

---

# 4) Main Findings Relevant To Prediction

### Direction and Moderators of Punishment’s Effect on Efficiency
- **Punishment often increases efficiency, but only under certain moderating conditions** (Zhang & Cao, 2020; Vasconcelos et al., 2022; Frey & Rusch, 2012; Rosas, 2008; Kraak, 2011; Vlerick, 2016; Xu et al., 2014).
- **Effectiveness of punishment is conditional on:**
  - **Punishment cost vs. effectiveness (fine-to-fee ratio)**: If punishment is too costly relative to the fine, efficiency gains may be wiped out (Zhang & Cao, 2020; Rosas, 2008; Liu et al., 2019; discussion of variable fine-to-fee in Fehr-Gächter style games).
  - **Time horizon (num_rounds)**: Short games often see efficiency losses due to initial punishment costs; long games or stable group compositions allow punishment to establish cooperation and reduce costs, potentially overtaking control game efficiency (Frey & Rusch, 2012).
  - **Group stability (partner vs. stranger matching)**: Fixed groups favor efficient use of punishment (Frey & Rusch, 2012).
  - **Network structure and population size**: Structured (versus well-mixed) populations often allow punishment to be more effective at lower cost, especially in smaller/local groups (Vasconcelos et al., 2022; Lim & Capraro, 2022; Xu et al., 2014).
  - **Punishment type (peer vs. centralized; exclusion vs. costly monetary/shaming)**: Exclusion and reputation-based punishment can achieve higher, more stable efficiency; peer punishment may be less efficient due to potential retaliation or overuse (Rosas, 2008; Vasconcelos et al., 2022; Kraak, 2011).
  - **Reputation, communication, and information about others’ actions**: Increase the impact of punishment and sometimes reduce need for costly punishment (Kraak, 2011; Vasconcelos et al., 2022; Raihani & Aitken, 2011).
  - **Reward mechanisms**: Rewards can sometimes operate as a substitute or complement; in some parameter regions, rewards are more effective in raising efficiency than punishment in early stages (Raihani & Aitken, 2011; Zhao & Zou, 2025).
  - **Cognitive/psychological modifiers (prospect theory, risk perception, memory)**: Cognitive distortion (risk overweighting) can make punishment more effective at lower cost (prospect theory models).
  - **Design features such as all-or-nothing vs. continuous contributions, default contribution framing, and observability features**: Less specified direct impact, but mechanism arguments suggest that more transparent, opt-out framed, and individualized feedback systems may enhance punishment’s effect.

### Cautions and Failure Modes
- **Punishment can reduce efficiency when:**  
  - **Costs of punishment are high, or punishment is inefficiently targeted** (Frey & Rusch, 2012; Rosas, 2008; simulation studies comparing costly punishment to alternative enforcement mechanisms).
  - **Punishment is indiscriminate, overused, or subject to second-order/retaliatory dynamics** (Rosas, 2008; retaliation models; Goodman, 2022).
  - **Punishment targets non-productive behaviors (e.g., lying rather than defection) or is susceptible to anti-social use** (Rubin, 2022).
  - **Punishment is insufficient to counterbalance defection, is easily bypassed (e.g., via insurance/speculation), or is undermined by attractive “loner” strategies** (Zhang & Cao, 2020).
- **Control efficiency matters:** If control games (no punishment) already achieve high efficiency (due to high MPCR, strong social norms, or effective communication/rewards), enabling punishment may not increase—and can sometimes decrease—efficiency (Kraak, 2011; Vasconcelos et al., 2022).

### Indirect/Adjacent Mechanistic Findings
- **Reputation-based, exclusion, or rating protocols (non-costly "punishment") can sustain high efficiency, sometimes more robustly than costly punishment** (Liu et al., 2019; Xu et al., 2014; linkage/Kandori norm papers).
- **Threshold effects exist:** There can be sharp shifts in efficiency when punishment parameters cross certain thresholds (minimum fine-to-fee ratio to destabilize defection; minimal effectiveness to tip evolutionary dynamics).
- **Combination of punishment and reward, or institutional and peer sanctions, can be more effective than either alone** (Zhao & Zou, 2025; Li & Jiang, 2023).

---

# 5) Prediction Guidance

Given the literature, the following guidance should inform predictions of treatment efficiency from game design dimensions and baseline efficiency:

- **Enabling punishment tends to increase efficiency compared to no-punishment controls**, *especially* when:
  - **Punishment is cost-effective**: The fine-to-fee ratio is high, so defectors pay more than punishers.
  - **The time horizon is long and groups are stable**: Punishment costs decline over time as cooperation stabilizes.
  - **Punishment institutions are appropriately scaled (e.g., local for local goods) and collectively chosen**.
  - **Reputation or communication mechanisms are present**.
  - **The control game has low efficiency (high defection by default).**
- **Magnitude of efficiency gain is strongly moderated by design dimensions:**
  - High punishment *cost* reduces or eliminates efficiency gains.
  - High MPCR or low group size may reduce the *need* for punishment.
  - Peer punishment, if unstructured and poorly targeted, can be wasteful, especially in large/anonymous groups.
  - Exclusion-based or reputation mechanisms can outperform costly peer punishment in enabling high efficiency.
  - Combined punishment and reward designs, when both are moderate, can be synergistic.
- **If control efficiency is already high** (e.g., due to high MPCR, strong social/reputational incentives), predicted efficiency gain from enabling punishment is likely small or zero, and may be negative if punishment is costly or overused.
- **In adjacent game types**, efficiency is most enhanced when conditional strategies and recognition are enabled, mirroring punishment’s role in standard PGGs.
- **Non-payoff evidence (i.e., increases in cooperation rates only)** should *not* lead directly to predicted efficiency gains unless the design ensures that punishment costs do not outweigh increased contributions.

*Explicit note*: Quantitative estimates of the efficiency *magnitude* remain uncertain due to limited direct empirical data; predictions should retain uncertainty and attend to known moderators.

---

# 6) Design Dimensions Highlighted Across Papers

**Dimensions with Direct or Strong Indirect Evidence:**
- `player_count`: Modeled and discussed widely as influencing punishment efficacy (smaller groups often favor higher efficiency with peer punishment; larger groups see diminishing returns or need for institutionalization).
- `num_rounds`: Heavily discussed; longer games favor efficiency gains via reduced long-term punishment costs.
- `mpcr`: Central to models; higher MPCR reduces the need for punishment.
- `punishment_cost` and `punishment_tech`: Well-theorized as major moderators; the fine-to-fee ratio is key.
- `all_or_nothing`: Several models address both all-or-nothing and continuous contributions; some suggest all-or-nothing intensifies sanction effects.
- `reward_exists`, `reward_cost`, `reward_tech`: Frequently included in adjacent models as complementary or substitutive moderators of punishment’s effect.
- `chat`, `show_other_summaries`, `show_n_rounds`, `show_punishment_id`: Discussed in mechanism arguments regarding transparency, learning, stability, and targeting.
- `default_contrib`: Less often directly modeled, but opt-in (keep) vs. opt-out (give) framing is suggested to affect baseline cooperation.

**Sparse or Contextual Evidence:**
- `show_n_rounds` and `show_other_summaries`: Mentioned in a subset of models, mainly as information features, but less often analyzed as primary moderators.
- `show_punishment_id`: Not prominent outside specific mechanism discussions (e.g., reputation-based sanction models).
- `default_contrib`: Sporadically referenced in framing/priming discussions, not routinely modeled.

**Effectively Missing:**
- Interactions among design features beyond 2–3 dimensions (e.g., high-dimensional moderator effects) are rarely explicitly reported.
- Very little direct engagement with the downstream task of predicting *actual numeric efficiency ratios* from design dimension vectors.

---

# 7) Important Limitations

- **Empirical Evidence Gap**: The vast majority of the literature is theoretical or simulation-based, with only sparse direct empirical payoff results in the context most relevant for prediction (multi-person, repeated PGGs with explicit efficiency reporting).
- **Non-payoff outcomes dominate**: Many papers conflate or report only behavioral cooperation, compliance, or norm adherence—outcomes that do not always track efficiency, especially when punishment is costly.
- **Scope and Transferability**: Much evidence comes from models of adjacent games, simplified structures (e.g., two-person games), or abstract evolutionary settings; translation to experimental, parameterized, lab-standard PGGs is not always warranted.
- **Incomplete coverage of design space**: Some design dimensions are well-modeled, others are rarely or never manipulated (e.g., default contribution framing, visibility of punishers, etc.).
- **Cautions about mechanism generalization**: Several papers urge caution in generalizing positive effects of punishment, especially in the presence of possible over-punishment, anti-social punishment, or design-induced artifacts (e.g., variable fine-to-fee ratio confounds).
- **No robust quantitative benchmarks**: There is insufficient directly comparable experimental evidence to support strong, numeric efficiency predictions for treatment arms in untested designs; guidance is therefore mainly qualitative and moderator-based.
- **Ambiguity and Disagreement**: Some models show negative, null, or ambiguous effects of punishment on efficiency, especially under high costs, poor targeting, or in short/intermittent games; meta-syntheses stress the large role of contextual and institutional moderators.
- **Possible publication and modeling biases**: Over-representation of positive findings/mechanisms for punishment in cooperation and efficiency sustenance; adjacent literature critiques over-optimism about generalizability (e.g., reliance on greenbeard-like mechanisms).

---

**In summary:**  
The literature set provides strong mechanistic, theoretical, and contextual support for modeling punishment as a positive moderator of average efficiency in public-goods-game-like environments under specified parameter conditions. However, evidence is largely theoretical, with only limited direct, empirical, payoff-based results that match the level of detail and dimensionality required for robust, quantitative, design-driven prediction of treatment efficiency. Caution, explicit treatment of moderators, and allowance for context-dependence and null/negative effects are warranted.
