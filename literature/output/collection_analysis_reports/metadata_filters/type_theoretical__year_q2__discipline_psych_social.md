# 1) Evidence Base

The evidence base consists of 53 papers, all theory or simulation-based (no original empirical or lab/field experimental results), and covers a spectrum from exact public goods game (PGG) studies to adjacent models such as repeated prisoner’s dilemma and resource management games. The set is fairly broad with respect to modeling traditions (evolutionary game theory, economic modeling, agent-based simulations), and includes both direct examinations of punishment in PGGs and more adjacent theoretical frameworks. However, only a minority of studies report group efficiency or related payoff outcomes directly; many focus on cooperation or contribution rates, norm adherence, or structural mechanism arguments.

**Empirical/experimental evidence is lacking**; nearly all results are derived from models, literature reviews, or theoretical synthesis. As a consequence, much of the guidance is conditional, mechanistic, or oriented around equilibrium properties and moderator effects rather than concrete effect sizes or robust empirical generalizations.

# 2) Task Relevance

### By Relevance Label

#### **pgg_or_variant**
- **Exact**: About one-fifth of the papers directly target PGG or very close variants and center on the canonical institutional features, including peer punishment.
- **Close**: Several studies employ models that are structurally similar (e.g., resource sharing, repeated cooperative dilemmas) but are not precise PGG implementations.
- **Adjacent/Weak/None**: A sizable portion employs variants (e.g., repeated PD, signaling games, etc.) or focuses on the evolution of cooperation in settings where punishment is only conceptually related.

#### **punishment_or_sanctions**
- **Exact**: Many papers model or discuss peer punishment as a switchable, parametrized mechanism, directly addressing the dimension relevant to the prediction task.
- **Close/Adjacent**: Numerous studies discuss institutional or reputational sanctions, third-party enforcement, or commitment devices, offering insight that is suggestive but less directly predictive.
- **Weak/None**: A few papers discuss only internalized norms, spatial structures, or reward mechanisms.

#### **efficiency_or_related_payoff_outcome**
- **Exact/Close**: Only a handful of papers report efficiency or directly comparable group payoff measures as the primary outcome (e.g., Boyd et al., 2014; Kroupa, 2014; Kurzban et al., 2015; Asgharpourmasouleh et al., 2017; Farjam et al., 2015; Al-Dhanhani et al., 2014; Nasrallah & Cheaib, 2016).
- **Adjacent**: Many focus on cooperation rates, norm compliance, or provide equilibrium arguments about expected welfare without specific output ratios.
- **Weak/None**: Some make no mention of efficiency, payoffs, or collective welfare.

**Overall:** The set contains a solid core of punishment-in-PGG modeling, but the breadth of adjacent, less directly predictive work, and the lack of experimental/empirical efficiency outcomes, limits the precision of inference for the prediction task.

# 3) Outcomes Measured In The Literature

- **Payoff-based Outcomes** (directly comparable to efficiency):  
    - *Group efficiency* (ratio of actual to maximum payoff) or *total group payoff* (Boyd et al., 2014; Kroupa, 2014; Kurzban et al., 2015; Farjam et al., 2015; Asgharpourmasouleh et al., 2017; Camera & Gioffré, 2014; Nasrallah & Cheaib, 2016; Al-Dhanhani et al., 2014).
    - *Average earnings*, *total coins*, or *welfare* as proxies for efficiency.

- **Non-payoff (behavioral) Outcomes**:
    - Contribution or cooperation rates (e.g., Parks et al., 2013; Strang & Park, 2017; Ogaki & Tanaka, 2017).
    - Rate/frequency of punishment or antisocial punishment, norm compliance, reputation building, social exclusion.
    - Mechanism/process arguments about sustainability, equilibrium, or stability of cooperation.

Many papers derive predictions about efficiency indirectly, relying on the relationship between observed or modeled cooperation and implied group welfare. Only a minority report efficiency as a computed or simulated outcome.

# 4) Main Findings Relevant To Prediction

### Efficiency Effects of Punishment in PGG(-like) Games
- **General pattern:**  
  Punishment increases cooperation/contribution rates, but its efficiency effect is highly contingent. **Efficiency (group payoff as fraction of maximum) can increase, decrease, or remain unchanged** depending on structural features:

    - **Positive Effects:**
        - In *small groups*, with *low punishment cost*, and/or *long repeated interactions*, punishment more reliably increases efficiency, especially when communication or reputation is present (Boyd et al., 2014; Kroupa, 2014; Parks et al., 2013; Asgharpourmasouleh et al., 2017; Camera & Gioffré, 2014).
        - Punishment-based *reputation* mechanisms are effective (dos Santos & Wedekind, 2015), especially in large groups or with errors in monitoring.
        - *Third-party monitoring* and *centralized punishment* outperform decentralized, peer punishment in maximizing efficiency (Camera & Gioffré, 2014; Simpson & Willer, 2015).

    - **Negative or Mixed Effects:**
        - In standard short, anonymous lab designs, punishment can **decrease efficiency** because the cost of administering/receiving punishment outweighs gains from increased cooperation (Kroupa, 2014; Kurzban et al., 2015; Handfield et al., 2016).
        - Efficiency loss is more likely if there is *antisocial punishment* (punishing cooperators), high punishment cost, or opportunity for retaliation (Kurzban et al., 2015; Sylwester et al., 2013; Thöni, 2014; Handfield et al., 2016).
        - The effect of punishment on efficiency can depend on the *MPCR* (Farjam et al., 2015)—it may only raise efficiency in games with low MPCR (scarcity), and not when resources are abundant.

    - **Design Moderators:**  
        - *Communication* and *reputation* mechanisms mitigate costs of punishment and support efficiency gains (Kroupa, 2014; Parks et al., 2013).  
        - *Reward* mechanisms are generally more efficient than punishment if enabled (Rand & Nowak, 2013).  
        - *Punishment structure*: Unrestricted or anti-social punishment reduces efficiency; targeted, second-order, or status-differentiated punishment can support higher efficiency (Thöni, 2014; Toriumi et al., 2016; Vincent, 2017; Antoci & Zarri, 2015).

### Theoretical and Mechanism Arguments (not empirical):
- Punishment is effective when a *minority of punishers* can deter defection (Boyd et al., 2014).
- *Network structure*, *monitoring breadth*, and *information transmission* influence how efficiently peer punishment sustains cooperation (Camera & Gioffré, 2014; Larson, 2017).
- The *relative efficiency* of peer punishment versus centralized punishment or other structural mechanisms is context-dependent (Simpson & Willer, 2015; Parks et al., 2013).

# 5) Prediction Guidance

**How this literature should inform prediction:**

- **Directionality:** 
    - The effect of punishment on efficiency is *not uniformly positive*. It is highly moderated by the features of the game and the baseline level of cooperation/efficiency in the control condition.
    - **If control efficiency is already high (near-maximal cooperation), punishment may not further increase and may even decrease efficiency due to added costs.**
    - **If control efficiency is low, enabling punishment tends to increase efficiency, especially in favorable environments (low cost, repeated, small groups, communication allowed).**

- **Key design dimensions to consider:**
    - **player_count**: Large groups reduce the effectiveness of peer punishment for efficiency (Boyd et al., 2014; Parks et al., 2013).
    - **num_rounds**: More repetitions favor the efficiency-raising effect of punishment (Kroupa, 2014; Kurzban et al., 2015).
    - **chat (communication)**, **show_other_summaries**: Facilitates coordination and reduces inefficient punishment, supporting greater efficiency gains (Kroupa, 2014; Parks et al., 2013).
    - **mpcr**: When returns to cooperation are low (scarcity), punishment is more likely to improve efficiency; when returns are high, its value declines or reverses (Farjam et al., 2015).
    - **punishment_cost**: Low-cost punishment is more efficiency-enhancing; high-cost punishment likely reduces or eliminates gains (Kurzban et al., 2015; Kroupa, 2014; Sylwester et al., 2013).
    - **punishment_tech**: The structure of punishment (targeted, restricted vs. open, potentially antisocial) critically moderates efficiency impact.

- **Other moderators:**
    - Cultural and social context, presence of antisocial punishment, status structures, and opportunity for verbal or reputational coordination all shape whether punishment becomes a group benefit or a net cost (Sylwester et al., 2013; Vincent, 2017; Thöni, 2014).

- **Quantitative effect estimation is not supported:**  
  No studies provide precise formulas or effect sizes mapping design dimensions and control efficiency to treatment efficiency, but several provide boundary conditions or qualitative rules.

- **Behavioral outcomes and efficiency:**   
  Higher cooperation does not guarantee higher efficiency if punishment is costly or misapplied. Prediction should not assume monotonic translation from cooperation gains to efficiency gains.

# 6) Design Dimensions Highlighted Across Papers

### Most directly informed dimensions (reported or robustly discussed):
- **player_count**: Explicitly modeled and shown to moderate punishment’s effect in many studies (Boyd et al., 2014; Parks et al., 2013).
- **num_rounds**: Strong focus, especially regarding the sustainability and payoff consequences over repeated interactions (Kroupa, 2014; Kurzban et al., 2015).
- **chat**: Frequently noted as a moderator of punishment efficiency, especially with respect to coordination and anti-social punishment.
- **mpcr**: Modeled and shown to moderate efficiency gains (Farjam et al., 2015; Parks et al., 2013).
- **punishment_cost**: Consistently highlighted as central for both cooperation and efficiency consequences (Kurzban et al., 2015; Kroupa, 2014; Farjam et al., 2015).
- **punishment_tech**: Discussed where second-order punishment, antisocial punishment, or mechanism design is modeled (Toriumi et al., 2016; Thöni, 2014).

### Indirectly or contextually informed:
- **all_or_nothing**, **default_contrib**, **reward_exists**, **reward_cost**, **reward_tech**: Sometimes present as background features or as limited comparative conditions but not systematically analyzed for efficiency consequences.
- **show_n_rounds**, **show_other_summaries**, **show_punishment_id**: Occasionally discussed regarding transparency/moderation of punishment (Camera & Gioffré, 2014), but not consistently mapped to efficiency outcomes.

### Sparse, missing, or only contextually mentioned:
- **default_contrib**: Rare or not analyzed.
- **reward_exists, reward_cost, reward_tech**: Addressed in a few comparisons (rewards vs. punishment—Rand & Nowak, 2013), not systematically.
- **show_n_rounds, show_punishment_id**: Rarely analyzed with respect to efficiency impact of punishment.
- **show_other_summaries**: Sometimes mentioned as a transparency mechanism but not directly tied to efficiency findings.

# 7) Important Limitations

- **Lack of experimental/empirical payoff or efficiency data**: There is little direct measurement of efficiency outcomes under well-controlled experimental variation of the full set of design dimensions. Most evidence is theoretical or from simulations rather than observed behavior.

- **Frequent reliance on behavioral proxies**: Many results infer possible efficiency effects from cooperation or norm compliance, which do not always map monotonically to payoff outcomes, especially when punishment is costly or misapplied.

- **Sparse evidence for certain design dimensions**: Several predictors in the downstream task (e.g., default contribution, detailed reward mechanics, display variables) are little analyzed and thus prediction must interpolate or extrapolate.

- **Qualitative rather than quantitative guidance**: Except for specific boundary conditions or contingent equilibrium arguments, precise effect sizes for the impact of punishment (relative to control efficiency and design features) are largely missing.

- **Ambiguity and heterogeneity among models**: Some studies find positive efficiency effects (typically under low baseline cooperation/favorable conditions), while others find negative or null effects (especially where punishment is costly, antisocial, or insufficiently targeted).

- **Potential cultural/contextual generalizability issues**: Some mechanism arguments depend on social context, anti-social punishment rates, or endogenous hierarchy emergence, which may not transfer across settings.

---

**In summary:**  
The literature offers **conditional and mechanism-oriented guidance**:  
**Punishment can increase efficiency, but only under specific design-dependent circumstances**—notably, small groups, low cost, many rounds, and the presence of communication or reputation systems.  
**Where control efficiency is already high, or punishment is costly/misapplied, efficiency gains are unlikely and negative effects possible.**  
**Design features such as antisocial punishment, lack of communication, or poor mechanism design undermine punishment’s efficiency benefit.**  
**The evidence is strongest and most directly informative for dimensions including group size, punishment cost, repetition, and communication, while indirect or sparse for display/framing variables and detailed reward mechanisms.**
