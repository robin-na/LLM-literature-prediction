# 1) Evidence Base

This paper set is broad, containing 66 sources with a primary focus on empirical laboratory experiments and a minority of observational, field, and theoretical studies. The majority of the most relevant and actionable evidence for the downstream efficiency prediction task comes from laboratory experiments using public goods games (PGGs) or close variants. Most studies are experimental, with clear manipulations of punishment, player count, rounds, and related game parameters. The evidence coverage for the task is robust for standard linear PGGs and some close variants. Adjacent and contextual studies (e.g., dictator games, trust games, real-world collective action) broaden the perspective but provide little direct value for quantitative efficiency prediction.

Empirically, there is a preponderance of studies that directly measure or infer efficiency and group payoff, but there are also many which only examine behavioral proxies (e.g., contributions, cooperation rates, punishment frequency) or non-payoff outcomes (e.g., trust, norm compliance). Theoretical or observational work is largely peripheral to the core prediction task.

# 2) Task Relevance

**pgg_or_variant**:  
- **exact relevance**: Many studies employ standard linear PGGs or close structural variants (e.g., weakest-link, nonlinear CPR games).  
- **close relevance**: Some studies use step-level, agency, or dynamic resource games with strong similarity to PGGs.  
- **adjacent/weak relevance**: Others use dyadic dilemmas, trust/dictator/ultimatum games, or field/real-world analogs, mostly for theoretical or contextual framing.

**punishment_or_sanctions**:  
- **exact relevance**: Multiple studies explicitly manipulate the presence of punishment (on/off), or compare costly vs. costless punishment, centralization vs. peer punishment, punishment vs. reward, and third-party vs. peer punishment. Design dimensions are often experimentally controlled.  
- **close/adjacent relevance**: Others examine forms of sanctioning (rewards, exclusion, informal enforcement), or the psychological and cultural moderators of punishment behavior, though not always in the context of PGGs.

**efficiency_or_related_payoff_outcome**:  
- **exact/close relevance**: About a third of studies report direct measures of efficiency or total group earnings.  
- **adjacent/weak/none**: Many focus solely on contribution rates, cooperation frequencies, or punishment behaviors. A minority report only psychological outcomes or contextual attitudes.

**Summary**:  
The highest prediction utility comes from experimental studies with (a) standard or closely related PGGs, (b) explicit manipulation of punishment, and (c) measurement of group efficiency or payoff.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes**: Efficiency (group earnings relative to optimum), total coins/profit/earnings, welfare, surplus, group payoff. *These are the key outcomes for the downstream prediction task.*
- **Non-payoff behavioral outcomes**: Contribution rate, cooperation rate, frequency and magnitude of punishment/reward, norm compliance, participation/turnout, retaliation, trust, psychological variables (e.g., satisfaction, fairness, anger).
- *Distinction*: Several studies measure both, but many only report behavioral metrics. When inferring efficiency from behavioral results, mapping is sometimes straightforward (e.g., in linear PGGs where contributions map directly to payoffs), but not always reliable—especially in nonlinear, agency, or step-level games.

# 4) Main Findings Relevant To Prediction

**Synthesized Empirical Findings (Payoff Effects):**
- **Punishment as an efficiency enhancer**:  
  - Costly, well-calibrated punishment often increases efficiency or group earnings in repeated linear PGGs, especially over longer games and when antisocial punishment is rare or contained [(Sparks et al., 2024); (Harrell & Wolff, 2023); (Kuwabara & Yu, 2017); (Hou et al., 2019)].
  - Communication between players and structured/democratic punishment can mitigate inefficiencies by reducing excessive punishment, improving targeted (prosocial) punishment, and raising long-run efficiency [(Andrighetto et al., 2016); (Pfattheicher et al., 2018)].
  - Effectiveness is highly sensitive to the production function: punishment robustly increases efficiency in weakest-link/complementary games, but not necessarily in linear PGGs with prevalent antisocial punishment [(Fatas & Mateu, 2015)].

- **Punishment as an efficiency reducer or neutral**:  
  - Costless peer punishment can lower efficiency due to excessive or antisocial use [(Kuwabara & Yu, 2017); (Fatas & Mateu, 2015)].
  - Centralization of punishment does not necessarily increase efficiency unless combined with information control or legitimacy signals [(Fischer et al., 2016); (Dorrough et al., 2017)].
  - In games with unstable, unequal punishment power or poorly designed punishment structures, enabling punishment can reduce group efficiency through resource waste and competition for power [(Dorrough et al., 2017); (Lierl, 2016)].
  - Effects may be context-specific in nonlinear common pool resource settings: punishment often does not improve efficiency over control; communication is a stronger driver [(Cason & Gangadharan, 2016)].

- **Critical moderators**:
  - *Punishment cost*: Increasing punishment cost can increase efficiency by limiting punitive excess, but if cost is too high, deterrence is weak; if too low, retaliation and overuse reduce efficiency [(Kuwabara & Yu, 2017); (Nikias & Sy, 2021)].
  - *Punishment structure*: Democratic or centralized punishment (especially with legitimacy) is more effective than unregulated, peer-to-peer punishment at improving efficiency [(Pfattheicher et al., 2018); (Kuwabara & Yu, 2017)].
  - *Communication*: Chat and communication features can substitute for or enhance punishment's efficiency gains [(Andrighetto et al., 2016); (Cason & Gangadharan, 2016); (Harrell & Wolff, 2023)].
  - *Group size*: Efficiency gains from punishment are larger in large, densely connected groups; in small groups, information alone can suffice [(Harrell & Wolff, 2023)].

**Theoretical/Mechanism Arguments and Behavioral Outcomes:**
- Trust, expectations, social context, and legitimacy are important, but their effects transmit through cooperation/contribution rates, not directly through payoffs [(English, 2012); (Irwin et al., 2014)].
- Non-payoff outcomes (e.g., contribution rates) generally point same-direction as efficiency in standard linear PGGs, but the mapping is not always reliable in step-level, nonlinear, or agency games [(Lierl, 2016); (Cason & Gangadharan, 2016)].

# 5) Prediction Guidance

- **When control (no-punishment) efficiency is low, and the game is a standard, repeated linear PGG with moderate punishment cost/tech, enabling peer punishment usually increases efficiency, probably more so as the game length increases and with communication features.**
  - *Empirical basis*: [(Sparks et al., 2024); (Harrell & Wolff, 2023); (Hou et al., 2019)]
- **If punishment is costless or very cheap, especially in peer settings, efficiency may decrease due to over-punishment and retaliation.**
  - *Empirical basis*: [(Kuwabara & Yu, 2017); (Fatas & Mateu, 2015)]
- **Punishment's effect is weaker or can be neutral/negative if:**  
    - Game structure is nonlinear or agency-based [(Cason & Gangadharan, 2016); (Lierl, 2016)]
    - Antisocial punishment is prevalent (e.g., some cultural settings, linear VCMs) [(Fatas & Mateu, 2015)]
    - Inequality or instability in punishment power triggers competitive punishment [(Dorrough et al., 2017)]
- **Game design dimensions most predictive:**  
    - *player_count*: Larger groups with dense networks amplify positive effects of punishment.
    - *num_rounds*: Efficiency gains from punishment grow over time; short games may show no gain or losses.
    - *chat*: Communication largely enhances, sometimes supersedes, punishment efficiency gains.
    - *mpcr*: Lower MPCRs (harder dilemmas) generally see greater absolute efficiency gains from punishment.
    - *punishment_cost* and *punishment_tech*: Must be moderate; too high reduces deterrence, too low increases waste.
    - *reward_exists/cost/tech*: Rewards alone are weaker than punishment; combined punishment/reward can be optimal in some settings [(Hou et al., 2019)].
    - *punishment institution*: Democratic, designated, or centralized punishment (with legitimacy) is more efficient than unregulated peer punishment.

- **For close variants (weakest-link, dynamic CPRs):**  
    - The interaction between production technology and punishment is critical; the sign and magnitude of the efficiency effect can reverse [(Fatas & Mateu, 2015); (van Klingeren & Buskens, 2024)].

- **If only non-payoff outcomes are reported, caution is warranted:** For standard PGGs, increased cooperation rates typically correspond to efficiency increases, but this may not hold in step-level, agency, or contest games.

# 6) Design Dimensions Highlighted Across Papers

**Direct empirical evidence:**
- *player_count*, *num_rounds*, *mpcr*, *punishment_cost*, *punishment_tech*: common and well-instrumented.
- *chat*: Manipulated in multiple high-relevance papers.
- *all_or_nothing*, *default_contrib*, *show_other_summaries*: Present in some, but less often systematically varied.

**Moderately covered or indirectly discussed:**
- *reward_exists*, *reward_cost*, *reward_tech*: A few studies test reward vs. punishment, but direct prediction evidence is sparse.
- *show_n_rounds*, *show_punishment_id*: Occasionally manipulated, less frequently analyzed for efficiency impact.

**Effectively missing or only contextually discussed:**
- *default_contrib*: Virtually never the main focus.
- *show_punishment_id*: Only in a handful of adjacent studies, with rare analysis of efficiency effects.

# 7) Important Limitations

- **Payoff coverage**: A significant proportion of studies report only behavioral (not efficiency) outcomes. While mapping from cooperation rate to payoff is valid in standard linear PGGs, it may not hold in nonlinear, agency, step-level, or contest variants.
- **Game design generalizability**: Robust conclusions about punishment's effect on efficiency apply best to standard, repeated, linear PGGs. Findings frequently diverge in nonlinear CPR games or weakest-link/minimum-contribution games.
- **Cultural and contextual moderators**: Some cultures exhibit high antisocial punishment, leading to lower or negative efficiency effects; these are not always identified in advance.
- **Horizon effects**: Efficiency gains from punishment often require many rounds to materialize; short games may see no gain or even net welfare loss due to punishment costs.
- **Mechanism variability**: Positive effects of punishment depend on appropriate calibration of punishment cost, legitimacy, institutional structure, and communication opportunities.
- **Sparse coverage of certain design features**: Dimensions like *default_contrib*, *show_punishment_id*, and granular information feedback are understudied in terms of efficiency impacts.
- **Control game as baseline**: Accurate prediction relies on knowing baseline (no punishment) efficiency, which may itself be shaped by many contextual and cultural factors not always captured in the literature.

**Conclusion**:  
While this literature set provides rich, direct evidence connecting game design features and control efficiency to efficiency under punishment in PGGs, predictions must be carefully conditioned on exact design parameters and contextual moderators. The literature does **not** support universal claims that enabling punishment always increases efficiency; effects are contingent, especially on punishment cost/structure, communication, game structure, and group size. For efficiency prediction, only results with direct payoff measurement and clearly-specified design dimensions should be considered high-confidence.
