# 1) Evidence Base

The paper set consists of 52 papers, featuring a substantial mix of **empirical experimental studies** and **theoretical/modeling papers**. The empirical studies are predominantly laboratory experiments that manipulate punishment, reward, exclusion, or related institutions in variants of public goods games (PGGs), while the theoretical literature explores evolutionary dynamics, stability of cooperative regimes, and how different sanctioning mechanisms affect outcomes. The coverage of **public goods games proper is relatively strong**, and several papers directly study treatment efficiency when punishment is present versus absent, while others explore closely related strategic environments (e.g., prisoner's dilemmas with punishment, liability games, exclusion, leader punishment). **A notable minority of papers only contextually touch on public goods or focus on adjacent games or mechanisms (like gossip, reputation, sorting).** 

Across the set, there is **robust direct empirical and theoretical evidence on the effects of punishment on group-level payoff or efficiency** in PGGs and close variants. However, some papers contribute only indirect evidence via cooperation rates or norm compliance rather than payoff outcomes, and some only narrate potential mechanisms.

# 2) Task Relevance

**Relevance to each dimension:**

- **pgg_or_variant**:  
  - **exact**: The large core of the paper set directly implements or models standard linear PGGs or very close variants (e.g., with binary/all-or-nothing contribution, repeated settings, endogenous/exogenous institutions, pool/peer/third-party punishment), providing *exact* relevance for the prediction task (e.g., Gürerk et al., 2018; Engl et al., 2021; Bruhin et al., 2020; Marcin et al., 2019; Dannenberg et al., 2020).
  - **close/adjacent/weak**: A subset uses adjacent games (prisoner’s dilemma, trust, liability games, etc.) with related group cooperation and punishment mechanisms (Kamei, 2020; Deffains et al., 2019; Gao et al., 2018).
  - **none**: Some papers focus entirely outside the PGG domain.

- **punishment_or_sanctions**:  
  - **exact**: Many papers *directly manipulate or model punishment*, including peer-, pool-, and third-party forms, as well as exclusion, fines, and legal sanctions (Gürerk et al., 2018; Bruhin et al., 2020; Marcin et al., 2019).
  - **close/adjacent/weak**: Others include only adjacent forms (e.g., exclusion as punishment, sanctioning through social disapproval, gossip, or reputation) or discuss punishment as a contextual variable.
  - **none**: Some focus exclusively on rewards or mechanisms not involving sanctions.

- **efficiency_or_related_payoff_outcome**:  
  - **exact/close**: A strong set of papers measures *group efficiency, welfare, or net payoff* under treatment and control (Gürerk et al., 2018; Engl et al., 2021; Bruhin et al., 2020; Marcin et al., 2019; Dannenberg et al., 2020). Some provide only adjacent outcomes, such as average payoff (not normalized by the social optimum).
  - **adjacent/weak**: Several papers report only on cooperation rates, norm compliance, or punishment frequency, requiring indirect inferences to efficiency.
  - **none**: A notable fraction measures only behavioral or individual-level outcomes.

**Conclusion:**  
**The paper set is overall highly relevant** for the target of predicting efficiency outcomes in PGGs or close variants upon enabling punishment, but the depth of relevance varies by paper, with some evidence being more behavioral/mechanistic rather than direct on efficiency.

# 3) Outcomes Measured In The Literature

**Payoff-related (efficiency) outcomes:**
- **Directly measured**: Several high-profile studies report *group efficiency*, *welfare*, or *total group payoff*; in some cases, these are explicitly normalized to the fully cooperative benchmark (Gürerk et al., 2018; Engl et al., 2021; Marcin et al., 2019; Dannenberg et al., 2020; Bruhin et al., 2020).
- **Closely related**: Some papers provide *average payoff*, *earnings*, or *group surplus*, which can generally be interpreted as efficiency if the social optimum is known (Kamei, 2020; Deffains et al., 2019; Gao et al., 2018).
- **Indirectly or not measured**: Many papers focus on *contribution rates*, *cooperation rates*, or *prevalence of cooperative strategies* without computing the net efficiency or accounting for the costs of punishment itself (which is crucial for the prediction task).

**Non-payoff behavioral outcomes:**
- *Contribution rates*, *cooperation frequency*, *punishment frequency*, *norm compliance*, *beliefs*, *expectations*, *reputation dynamics*, *gossip*, *sorting/matching behaviors*.
- *Psychological variables* (e.g., neural markers, personality traits, motivation for norm enforcement).

**Explicit distinction**:  
While high cooperation rates often correlate with high efficiency, this is not guaranteed—*the costliness of punishment can cause high cooperation but lower overall welfare*. Some key studies show that efficiency gains depend critically on the cost-benefit structure of punishment (Dannenberg et al., 2020; Bruhin et al., 2020).

# 4) Main Findings Relevant To Prediction

Synthesizing across the most relevant papers (focusing on PGGs, explicit punishment/sanctions, and efficiency outcomes):

- **Enabling punishment generally increases efficiency in standard PGGs**  
  - When punishment is not too costly and is well-targeted (i.e., focused on defectors), enabling peer or centralized punishment robustly increases total group payoff and efficiency compared to punishment-absent controls (Gürerk et al., 2018; Engl et al., 2021; Marcin et al., 2019).
  - The effect is consistent over repeated rounds, with efficiency often improving or being sustained where it would otherwise decline.

- **The costliness of the punishment mechanism is a critical moderator**  
  - When punishment (e.g., exclusion or fines) is costless or not overly penalizing to punishers or the group, efficiency gains are much stronger and more reliable (Dannenberg et al., 2020).
  - If punishment costs are high (either to punishers or to the group collectively, as with costly exclusion), then enabling punishment may increase cooperation rates but *can reduce net efficiency* (Dannenberg et al., 2020).
  - The punishment cost-to-impact (fine) ratio and overall structure (peer vs centralized) matter for the direction and strength of efficiency effects (Gürerk et al., 2018; Marcin et al., 2019).

- **Group composition and heterogeneity in punishment preferences strongly moderate efficiency effects**  
  - If *antisocial punishers* (those who punish high contributors or otherwise misuse punishment) are present, enabling punishment can *reduce efficiency*, and the prevalence of such types explains much cross-cultural and group-level variance (Bruhin et al., 2020).
  - Efficiency improvements are strongest in groups with few to no antisocial punishers (Bruhin et al., 2020).

- **Implementation method: Endogenous (by vote) vs exogenous (imposed) punishment**  
  - Most studies find that whether punishment is introduced by group vote or imposed externally does not substantially alter efficiency, even though endogenous institutions may lead to more selective or less severe punishment (Marcin et al., 2019; Dannenberg et al., 2020).

- **Punishment is often more effective than rewards at sustaining cooperation/efficiency, though some designs allow for efficiency-increasing reward mechanisms as well (Gürerk et al., 2018).**

- **Theoretical models confirm and clarify key empirical findings**  
  - Models identify precise thresholds for when punishment increases long-run efficiency (relative strength of punishment, cost, presence of potential disguises or avoidance behaviors; Wang et al., 2020; Zhang & Cao, 2020; Quan et al., 2018).

- **Adverse conditions**  
  - The effectiveness of punishment (and thus its efficiency impact) is undermined when: group sizes are large and punishment cannot be coordinated (over-punishment can occur; Kamei, 2020), defectors can cheaply disguise and avoid punishment, or baseline cooperativeness is extremely low and social information cues are negative (Bruhin et al., 2020; Engel et al., 2021).

- **Contextual factors** (chat, information, group size, etc.) can further moderate the effect, but game structure and punishment cost/effectiveness are principal.

# 5) Prediction Guidance

The literature supports the following approach:

- **The baseline efficiency of the control (punishment-off) game is a strong predictor—but** the efficiency gain (or loss) from enabling punishment depends crucially on:
  - **Punishment cost-to-impact ratio** (how effectively does punishment deter relative to its cost?)
  - **Frequency and nature of punishment use** (is it mostly pro-social, or is antisocial/counterproductive punishment frequent?)
  - **Group size and coordination** (smaller or well-coordinated punishing groups avoid over-punishment, large uncoordinated groups risk efficiency loss).
  - **Cultural or group heterogeneity** (prevalence of antisocial punishment types is a key moderator).
  - **Implementation costs or spillovers** (if all must pay for the punishment institution, net efficiency may not rise).
  - **Availability of avoidance or disguise strategies for defectors** (can undermine the positive effects).
- **Direct mapping from game design dimensions is possible when empirical data is available for similar parameterizations** (player count, rounds, continuous/all-or-nothing contribution, MPCR, chat, feedback, etc.).
- **Expected direction:** In a "typical" lab PGG (moderate group size, moderate MPCR, direct peer punishment with reasonable costs and no strong antisocial punishment), enabling punishment increases treatment efficiency above control. If punishment is very costly, poorly targeted, or group structure enables frequent antisocial or over-punishment, efficiency gains are small or negative, and in some conditions treatment efficiency can be *below* control.
- **Crucially, simply knowing control efficiency is not sufficient**—design dimensions, especially **punishment technology and cost structure**, must be factored alongside any available indicators about likely group/punisher types.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed:**  
- **player_count**: Many studies (empirical and theoretical) manipulate or specify group size; evidence indicates group size moderates over-punishment risks (Kamei, 2020) and that core results hold across commonly studied group sizes (Gürerk et al., 2018; Engl et al., 2021; Marcin et al., 2019).
- **num_rounds**: Almost all repeated PGG papers specify and analyze round effects.
- **mpcr**: Marginal per-capita return is universally treated as a core variable; evidence shows efficiency effects of punishment are stronger at higher MPCR.
- **all_or_nothing** & **continuous contribution**: Both variants are studied; main effects of punishment are robust, but some payoff structures (binary vs continuous) can affect the strength of efficiency gains (Marcin et al., 2019).
- **punishment_cost** and **punishment_tech**: Central to nearly all relevant empirical, theoretical, and simulation work.
- **reward_exists/cost/tech**: Occasionally analyzed; some studies directly compare punishment to reward (Gürerk et al., 2018).
- **chat**: Studied in some games; can impact baseline cooperation but less frequently interacts with punishment effectiveness.
- **show_n_rounds**, **show_other_summaries**, **show_punishment_id**: Occasionally specified but generally less systematically varied.

**Indirectly/contextually informed:**  
- **default_contrib**: Rarely reported explicitly; more a framing than a substance manipulation.
- **show_other_summaries/show_punishment_id**: Some studies manipulate visibility of actions/punishment, but effects on efficiency are less systematically explored.

**Sparsely informed or missing:**  
- **Reward details**: While reward is occasionally compared (and sometimes combined with punishment), few studies explore all reward parameters in detail.
- **Feedback, information perturbations, or chat as moderators of *efficiency* (vs. cooperation) effect**: Limited direct evidence.

# 7) Important Limitations

- **Antisocial punishment and cultural heterogeneity remain crucial but under-measured moderators**: While Bruhin et al. (2020) demonstrates that antisocial punishment can reverse the efficiency benefit of punishment, *most empirical studies do not report population heterogeneity or antisocial punishment rates*, limiting quantitative prediction in novel contexts.
- **Scope of design dimensions**: While core dimensions such as group size, rounds, cost and impact of punishment are well-covered, some potentially important moderators (e.g., default contribution settings, chat/reputation mechanisms, visibility of punishment) are less rigorously or systematically manipulated.
- **Lack of direct mapping from behavioral outcomes to payoff**: Many studies report on cooperation or contribution frequency but not on net efficiency, and the cost of punishment is not always netted out, leading to possible overestimation of the benefits of punishment.
- **External validity**: Most studies take place in controlled laboratory environments; behavior—and especially the prevalence of antisocial punishment—might differ in the field or in larger, culturally diverse populations.
- **Interaction with other mechanisms**: The presence of sorting/matching, repeated partner play, rewards, or communication can interact strongly with punishment effects, but are often orthogonal to the main manipulation or not jointly analyzed.
- **Adjacency vs. directness**: Several papers use adjacent games or mechanisms, or model only one aspect (e.g., reputation, exclusion, third-party/law rather than peer PGG punishment); care must be taken not to overgeneralize these results to standard PGGs with peer punishment and efficiency outcomes.
- **Prediction error in certain regimes**: When institutional costs are high, group size is large, antisocial punishers are frequent, or punishment is poorly targeted or error-prone, net efficiency *may not* increase (or may even decrease), but empirical cases mapping these "edge conditions" are relatively scarce.

---

In summary, **the literature base provides strong empirical and theoretical grounding for predicting that enabling punishment in public-goods-game-like environments increases average efficiency, provided punishment is not too costly or antisocially applied, and that group and institutional contexts do not foster over- or misdirected punishment**. Design dimensions such as player count, MPCR, punishment cost/tech, and group composition are best covered by the empirical literature; however, direct predictions should treat cultural and group heterogeneity, institutional costliness, and coordination mechanisms as major sources of uncertainty and error.
