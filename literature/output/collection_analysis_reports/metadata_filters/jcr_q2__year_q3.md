# 1) Evidence Base

The evidence base consists of a mix of **empirical (primarily experimental)** and **theoretical/simulation** studies, with the largest share being laboratory experiments on public goods games (PGGs) and their direct variants, and a significant number of simulation-based theory papers covering evolutionary game theory and institutional modeling. The paper set is **broad in game design coverage** (player count, rounds, institution types, punishment and reward schemes, information structures, heterogeneity, etc.) and includes both canonical linear PGGs and threshold, spatial, or variant games. **Empirical coverage is strongest for standard linear PGGs with peer or centralized punishment, but there is also evidence on institutional choice, network effects, communication, group composition, and cultural/contextual moderators.** The set includes both **papers reporting primary payoff/efficiency outcomes** and a subset reporting **behavioral (contribution, cooperation) outcomes** used as proxies, as well as some adjacent studies with partial relevance to the target outcome of efficiency. **Multiple large-N lab studies directly report both control (no-punishment) and treatment (punishment) average efficiency**, supporting quantitative calibration for prediction tasks. **Theory papers provide analytical mappings between parameters and equilibria**, often complementing empirical findings, especially regarding the cost/effectiveness of punishment, group size, and the structure of the game. **Substantial attention is paid to moderators, boundary conditions, and heterogeneity of punishment effects** in both empirical and theory work.

# 2) Task Relevance

**pgg_or_variant**: 
- **Exact relevance** is high—most core papers use linear or threshold public goods games, with detailed experimental controls. Several studies focus on PGG variants (threshold/CPR/exclusion/club goods), and some use close analogs (prisoner's dilemma, gift-exchange, trust games) which offer partial or adjacent relevance.
- Label: **mostly exact or close**, with a minority adjacent.

**punishment_or_sanctions**: 
- **Exact relevance**: Many studies directly manipulate peer or centralized punishment institutions, clearly separating punishment-enabled and baseline games. Several studies explore endogenous choice of punishment, variations in cost-effectiveness, observability, and types (peer, leader, third-party, exclusion, automatic). Some studies discuss reward mechanisms or partner exclusion as adjacent or alternative institutional levers.
- Label: **mostly exact**, with some close or adjacent (e.g., exclusion, taxation as enforcement) mechanisms.

**efficiency_or_related_payoff_outcome**: 
- **Mixed exactness**: A substantial set of studies report **group efficiency as the primary outcome** (group payoff as a ratio to the cooperative optimum), or closely related measures (average group earnings, welfare, surplus, total coins). Other studies report only behavioral outcomes (contribution rates, cooperation frequencies, punishment rates) and do not always specify or analyze efficiency/payoff.
- Label: **exact** for studies explicitly reporting group efficiency/payoff; **adjacent or weak** for behavioral-outcome studies.

**Summary**: The literature provides a strong core of **exactly relevant experimental and theoretical studies** directly matching the prediction task (mapping from PGG game design plus control efficiency to expected treatment efficiency under punishment), complemented by a broad set of adjacent and supporting papers.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes** (most relevant for prediction):
  - **Group efficiency** (group payoff as a ratio to the full-cooperation benchmark) is reported in many high-quality lab studies and theory papers.
  - **Total group payoff, welfare, surplus, or average earnings**—commonly used in the form and directly comparable to efficiency, often presented as mean tokens, relative payoffs, or welfare indices.
  - **Provision/success rates** in threshold games, which can be mapped to efficiency when full provision generates a step-function reward.
  - Some studies additionally decompose payoffs by type (cooperator, punisher, defector) to explore within-group disparities.

- **Non-payoff behavioral outcomes** (important for mechanism, but not prediction target):
  - **Contribution rates, cooperation frequencies, norm compliance, punishment assignment/frequency, partner selection, trust rates.**
  - **Emotional/motivational mediators** such as beliefs, justice sensitivity, punishment/reward motives.
- **Hybrid or adjacent outcomes**:
  - **Exclusion/reintegration, group composition, migration/electoral dynamics**, which impact efficiency indirectly via their effect on behavior and institutional persistence.
- **Explicit absence of payoff/efficiency reporting** in some behavioral/mechanism studies—these are less informative for the prediction target.

**Distinction**: The best calibration for predictive modeling uses studies that **report actual payoffs/efficiency, not just behavioral improvements**.

# 4) Main Findings Relevant To Prediction

## Direction, Magnitude, and Moderation of Punishment Effects

- **Enabling peer or institutional punishment in standard PGGs** (small/medium group size, repeated rounds, no chat, moderate mpcr, typical 1:3 cost-impact ratio):
  - **Robustly increases group efficiency, often dramatically**, relative to the punishment-disabled control (Arechar et al., 2018; Gürerk et al., 2018; Engl et al., 2021; Gürdal et al., 2021; Fatas et al., 2020; Drouvelis et al., 2021 [when efficiency is reported]).
  - The **size of the efficiency gain varies** but in many cases represents a shift from 40-60% of optimum in baseline to 70-90% or higher with punishment, depending on group size, mechanism cost, and antisocial punishment prevalence.

- **Critical moderators of punishment effect on efficiency**:
  - **Punishment cost relative to impact**: Lower cost and higher impact make punishment more effective for efficiency; excessively high cost can offset contribution gains (Glöckner et al., 2018; Ramalingam et al., 2019; Sui et al., 2018).
  - **Heterogeneity in endowment or punishment ability**: When endowments differ, efficiency gains from punishment depend on whether high endowment matches high punishment effectiveness, and whether information is complete (Waichman, 2020; De Geest & Kingsley, 2021; Waichman & Stenzel, 2019).
  - **Information/feedback structure**: Efficiency gains from punishment are much larger when group members can **observe relevant information** (contributions/endowments/identities/rounds), and are **dampened or reversed under incomplete information** (De Geest & Kingsley, 2019; De Geest & Kingsley, 2021; Waichman & Stenzel, 2019).
  - **Network/group structure**: Star and complete networks support efficiency gains from punishment, while circle and line networks may see **no gain or even efficiency loss** due to retaliation or antisocial cycles (Fatas et al., 2020).
  - **Cultural/group composition**: In-group preference and antisocial punishment prevalence are strong moderators—**mixed or antagonistic group composition can eliminate or reverse punishment-driven efficiency gains** (Mantilla et al., 2021; Bruhin et al., 2020; Drouvelis et al., 2021).
  - **Institutional/selection mechanism**: Endogenous choice of punishment (voting, migration) often yields similar or sometimes greater efficiency than exogenous assignment, but is not always a panacea; efficiency is driven mainly by presence, not choice, of effective punishment (Cobo-Reyes et al., 2019; Marcin et al., 2019).
  - **Combination with communication or rewards**: Chat/communication amplifies efficiency gains from punishment (Koch et al., 2021; Morgan et al., 2019). Combined reward and punishment mechanisms can yield higher efficiency than either alone, but the result depends on cost/benefit structure (Gürerk et al., 2018; Dannenberg et al., 2020).
  - **Punishment observability/identity of punisher**: Transparent and observed punishment (including identity) can improve targeting, reduce antisocial punishment, and thus increase efficiency (Glöckner et al., 2018; Kamei, 2018).
  - **Framing, emotional context, and expectations**: Mood induction, prior beliefs, and framing (Give/Take) alter whether punishment leads to efficiency gain or loss (Lee & Min, 2021; Ramalingam et al., 2019; Engel et al., 2021).

- **Boundary conditions and possible negative effects**:
  - **High levels of antisocial punishment** (punishing cooperators) can destroy efficiency gains or even reduce efficiency below baseline (Bruhin et al., 2020; Vollan et al., 2019; Mantilla et al., 2021).
  - **Weak, automatic, or poorly targeted punishment** (e.g., imposed on lowest contributor regardless of context, low magnitude, or without feedback) can be strictly efficiency-reducing (Yang et al., 2020; Glöckner et al., 2018; Waichman & Stenzel, 2019).
  - **Extreme group sizes (too small or too large)** and lack of coordination on punishment can induce over-punishment and efficiency losses (Kamei, 2020).
  - **Behavioral findings** (increased contributions) don't always translate into efficiency unless the cost of punishment is less than the gain from higher contributions.

- **Theory and simulation alignment**: Analytical models are generally consistent with empirical findings: **punishment increases efficiency if sufficiently strong and well-targeted; otherwise, efficiency gains are null or negative** (Zhang et al., 2020; Sui et al., 2018; Yan et al., 2021; Baker & Choi, 2018).

## Control efficiency as baseline predictor
- **Empirical studies consistently show that control (no-punishment) efficiency is a strong—but not sufficient—predictor of treatment (punishment-enabled) efficiency**. The magnitude and direction of the treatment effect is often a function of control efficiency, but is **strongly moderated** by design dimensions and social context (Arechar et al., 2018; Ramalingam et al., 2019; De Geest & Kingsley, 2019).

# 5) Prediction Guidance

## Direct inference for downstream prediction

Given a **control efficiency** value and game **design dimensions**, **treatment efficiency with punishment enabled can generally be predicted to be higher**, often substantially so—**except in the presence of identified negative moderators**:

- **Strong Efficiency Gains Expected**: Standard linear PGGs (group size 3–5, 10–20 rounds, peer/centralized punishment with cost-impact better than or equal to 1:3, no adverse group composition, no strong heterogeneity, observable contributions and identities, no weak/automatic punishment) (Gürerk et al., 2018; Arechar et al., 2018; Engl et al., 2021).
- **Moderate or Conditional Gains**: Heterogeneous groups with observed endowments or when punishment cost is high but not excessive (Waichman, 2020; De Geest & Kingsley, 2021).
- **No or Negative Effect**: High antisocial punishment, incomplete information on contributions/endowments, mixed/antagonistic groups (Bruhin et al., 2020; Mantilla et al., 2021; Vollan et al., 2019; De Geest & Kingsley, 2019), uncoordinated large group punishment (Kamei, 2020), weak or non-salient punishment channels (Yang et al., 2020).
- **Amplified Gains**: When chat or communication is added, or when punishment is combined optimally with rewards or both observed/unobserved channels (Koch et al., 2021; Glöckner et al., 2018; Morgan et al., 2019).
- **Critical boundary conditions** such as the design and cost/impact of punishment, group composition (homogeneity, presence of antisocial punishers), observability, institution selection method, and the presence of chat/communication must be used in prediction.

## Dimension-level prediction:
- When design dimensions match those in **exactly relevant empirical studies with efficiency data**, treatment efficiency should be predicted as:
  - **Substantially higher than control** when punishment cost-effectiveness is moderate/good, and negative moderators are absent.
- When design dimensions match to **theory only or lack direct empirical calibration**, uncertainty/variance in prediction should increase, and negative moderators (information, heterogeneity, group size, antisocial punishment) should be assumed possible unless evidence rules them out.

## **Explicitly: If evidence relates to contribution rates rather than efficiency, only infer efficiency effects to the extent that the cost of punishment does not offset the payoff gain from higher contributions.**

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions** (detailed experimental or theoretical calibration):
- `player_count`, `num_rounds`, `mpcr`, `punishment_cost`, and `punishment_tech` (punishment institution type, cost, and impact)—core in both empirical and theory evidence, with thousands of observed data points over a range of values.
- `chat` (communication)—robust empirical evidence that allowing chat amplifies efficiency gains of punishment (Koch et al., 2021; Morgan et al., 2019).
- `all_or_nothing` (binary vs. continuous contribution)—directly manipulated and analyzed in several studies (Marcin et al., 2019; Ramalingam et al., 2019).
- `show_other_summaries`, `show_n_rounds` (information about others' contributions/payoffs and round number)—shown to be important moderators of punishment's effectiveness (Engl et al., 2021; Waichman & Stenzel, 2019).
- `default_contrib` (framing, opt-in/opt-out)—less commonly manipulated, but some evidence regarding framing and minima (Martinsson et al., 2019).
- `reward_exists`, `reward_cost`, `reward_tech`—numerous studies compare punishment to reward, or hybrid/competition between reward and punishment (Gürerk et al., 2018; Chugunova et al., 2020).
- `punishment_tech` (centralized vs. peer vs. exclusion)—a major source of empirical variation (Engl et al., 2021; Angelovski et al., 2018).
- `show_punishment_id` (punisher/rewarder identity)—directly manipulated as punishment visibility in several studies (Kamei, 2018; Glöckner et al., 2018).
- `show_other_summaries`—feedback and information. When individuals observe others' behavior, targeting is improved and antisocial punishment reduced.

**Indirectly informed or contextually discussed dimensions**:
- `default_contrib` (some framing studies; overall, less frequently manipulated).
- `reward_exists`, `reward_cost`, `reward_tech` (covered more in theory and comparative studies than as core moderators in most PGG-punishment studies).
- **Overlapping, but less commonly experimentally isolated**: Details of the information structure (e.g., summary statistics vs. individual-level info), nature of migration/partner choice.

**Effectively missing or very sparse**:
- Specific interaction of `default_contrib` with punishment effects on efficiency (framing is infrequently studied as a core moderator in experimental PGG-punishment design).
- Details on `reward_cost` and `reward_tech` as standalone moderators, outside of comparative studies.
- Direct analysis of marginal effects of `show_punishment_id` in the full 2x2x... design.
- Systematic variation of multiple dimensions (e.g., granular manipulation of player count >10, combined with varying punishment tech and visibility).

# 7) Important Limitations

- **External validity**: While laboratory experiments allow precise control, generalization to larger groups, natural field settings, or high-stakes environments is uncertain. Some lab-in-the-field and field experiment results suggest moderation or reversal of the lab patterns (Chávez et al., 2021; Vollan et al., 2019).
- **Overfocus on canonical settings**: Strongest evidence is for 3–5 person, repeated, simultaneous move, linear PGGs with canonical punishment ratios; for other environments (large groups, threshold games, one-shot, highly heterogeneous groups) evidence is thinner or more equivocal.
- **Behavioral/psychological outcomes vs. payoff**: Several papers only report on contribution rates or punishment rates, not efficiency, making translation to payoff outcomes indirect.
- **Publication and design bias**: Most studies analyze positive treatment effects; negative results (no effect or negative impact on efficiency) might be underreported, though meta-analytic reviews try to correct for this.
- **Complex moderators**: Multiple design dimensions interact, and only a subset of their interactions are empirically mapped—e.g., simultaneous variation of heterogeneity, communication, and punishment is rare.
- **Effect of antisocial punishment**: Where high, it can erase or reverse expected efficiency gains, but prevalence is variable and depends on context, social norms, and group composition.
- **Theoretical models sometimes abstract away implementation details**: Practical institution-building challenges (adoption, maintenance, participant understanding) are not always captured.
- **Limited direct evidence for very large or dynamic groups, fine-grained reward structures, or sophisticated real-world regulation.**
- **Data on long-run dynamic effects, institution durability, and spillovers between institutions and domains are limited**—some evidence exists, e.g., spillover studies (Engl et al., 2021), but full assessment of sustainability and path dependence is beyond most lab designs.
- **Reward and communication are sometimes confounded with punishment in institutional design**, making it hard to isolate the effect of punishment per se where multiple interventions operate together.

---

**In summary:** The literature is **strongly supportive of predicting higher efficiency in public goods games when punishment is enabled**, but this effect can be overturned by adverse moderators, and the predictive mapping from design plus control efficiency to treatment efficiency is most accurate when all key moderating dimensions are specified and matched to available evidence. **Most game design dimensions relevant to prediction are well-calibrated in the literature, but attention should be paid to information structure, group composition, punishment cost-effectiveness, and institution type, all of which can turn the direction or magnitude of the effect.**
