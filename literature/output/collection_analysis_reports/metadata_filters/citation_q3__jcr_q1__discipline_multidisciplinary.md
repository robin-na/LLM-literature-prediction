# 1) Evidence Base

This paper set is both broad and deep, encompassing 118 papers that include a strong mix of empirical laboratory experiments and formal theoretical models. The set is unusually comprehensive for the target question, particularly for standard linear public goods games (PGG) and close variants. About half the papers are experiments (mostly lab, with a handful of field experiments), and the rest are theoretical/computational models, many of which specify payoff structures and evolutionary dynamics. There is substantial empirical coverage of group-level outcomes (efficiency, group payoff) for PGGs with/without peer punishment, as well as models addressing parameter regimes and mechanism design.

The empirical subset includes canonical PGG-with-punishment studies, long-run repeated designs, and treatments of institutional/peer punishment, while the theoretical literature explores evolutionary stability, network effects, and punishment/reward technologies. Some papers directly report efficiency outcomes per the prediction task, while others focus on closely related payoff outcomes or only on behavioral intermediates.

There is an over-representation of repeated small-group linear PGGs, and less coverage for very large groups, non-standard or threshold PGGs, and games with richer communication/treatment variation. Papers purely adjacent or unrelated to PGGs/punishment/efficiency are included but clearly less central.

# 2) Task Relevance

**pgg_or_variant:**  
- *Exact relevance*: Numerous papers study repeated PGGs (or direct variants) with clear mapping to the prediction task, providing both empirical and theoretical results (e.g., Simpson et al., 2017; Chaudhuri & Paichayontvijit, 2017; Ozono et al., 2020, 2017).  
- *Close relevance*: Some works study step-level, threshold, or snowdrift games, which share sanctioning/cooperation features and payoffs similar to PGGs but require care in direct application (e.g., Jiang et al., 2013; Gao et al., 2015).  
- *Adjacent/weak relevance*: Others use Prisoner’s Dilemma, Ultimatum Game, or generic social dilemma settings, providing mechanistic or indirect insights.  
- *None*: Many papers (about one-fifth) lack direct relevance either because they do not study PGGs or do not include sanctioning/incentives.

**punishment_or_sanctions:**  
- *Exact relevance*: The PGG core is well covered for peer punishment and pool/institutional punishment; several papers rigorously manipulate the presence or design of punishment (e.g., Simpson et al., 2017; Dong et al., 2016).  
- *Close relevance*: Adjacent studies examine exclusion, ostracism, norm-based sanctions, or reward-only interventions.  
- *Adjacently/weak relevance*: Some focus on restorative justice or reputation effects without economic punishment per se.  
- *None*: Many studies lack any sanctioning or incentive manipulation.

**efficiency_or_related_payoff_outcome:**  
- *Exact/close relevance*: A substantial subset report efficiency or total group payoff (as required by the prediction task), though several others focus primarily on contribution rates, cooperation frequency, or punishment rates, which are only indirect proxies.  
- *Adjacent/weak relevance*: Several papers report behavioral outcomes only, or focus on inequality/distribution rather than efficiency.  
- *None*: Many non-central papers lack any payoff analysis.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes**:  
  - *Efficiency* (group payoff vs. social optimum): Measured directly in several empirical and theoretical works (Simpson et al., 2017; Chaudhuri & Paichayontvijit, 2017; Ozono et al., 2020, 2017; Dong et al., 2016; Wang et al., 2024), as well as in many theoretical simulations and evolutionary models (Salahshour, 2021; Hetzer & Sornette, 2013).
  - *Total group earnings/welfare*: Often used when efficiency is not normalized but overall group payoff is provided.
  - *Related outcomes*: Surplus, average profit, collective return.
- **Non-payoff behavioral outcomes**:  
  - *Contribution/cooperation rates*: Nearly ubiquitous as primary outcomes but are not interchangeable with efficiency (Fehl et al., 2012; Molleman et al., 2019).
  - *Punishment frequency/amount*, *punishment coordination*, *retaliation rates*, *support for institutions*, *norm compliance*.
  - *Distributional metrics*: Inequality, wealth distribution.
  - *Psychological/motivational outcomes*: Perceptions, norm salience, emotional reactions (e.g., anger driving punishment; see Seip et al., 2009).
  - *Strategy frequencies/evolutionary stability*: Proportion of strategies at equilibrium in evolutionary simulations.

It is critical to distinguish that increases in cooperation or punishment do not always translate into higher efficiency, especially when costly punishment incurs deadweight losses.

# 4) Main Findings Relevant To Prediction

**Empirical findings (in PGGs and close variants):**
- Peer and institutional punishment consistently increase average contributions/cooperation compared to control/no-punishment (Simpson et al., 2017; Dong et al., 2016).
- The effect on efficiency is *mixed*: In many PGG studies, costly peer punishment raises contributions but not efficiency, as the cost of punishment offsets gains from higher cooperation (Simpson et al., 2017; Fehl et al., 2012).
- The positive effect of punishment on efficiency is strongest when:  
  - Punishment is cost-effective (cost/impact ratio is favorable, Chaudhuri & Paichayontvijit, 2017).  
  - The public good is locally efficient (Ozono et al., 2020).  
  - The threat of punishment deters free-riding before substantial resources are expended on punishment itself.
- Material punishment enables cycles of retaliation ('vendettas'), driving down efficiency for involved parties (Fehl et al., 2012); moral/non-costly sanctions (approval/disapproval) can improve both cooperation and efficiency (Simpson et al., 2017).
- The effect of punishment depends on group size, number of rounds, matching protocol (fixed vs. random), and baseline control efficiency.
- When cooperation is already high in control, severe punishment can reduce efficiency; when cooperation is low, punishment (especially severe) can substantially improve efficiency (Jiang et al., 2013).
- The design of punishment (conditional, coordinated, probabilistic vs. fixed, cost ratio) and the possibility of targeting defectors are key moderators.

**Theoretical findings:**
- The evolution of efficient cooperation via punishment is more likely when the marginal per capita return (mpcr) is high, punishment is not too cheap or too costly, and antisocial punishment is minimized (Salahshour, 2021; García & Traulsen, 2012).
- Population/network structure (e.g., spatial regular graphs) often conditions whether punishment eliminates defection and maximizes efficiency, with explicit thresholds provided in some models (Wang et al., 2024).
- The structure of the mutation kernel, possibility of anti-social punishment, and observability of institutions are critical for the emergence and sustainability of efficient outcomes (García & Traulsen, 2019).
- Conditional, coordinated, or adaptive punishment can outperform standard fixed-cost models in generating efficiency (Huang et al., 2018; Ohdaira, 2022).
- Pool (institutional) punishment can facilitate higher efficiency when funding/support for the institution is endogenous and properly incentivized (Ozono et al., 2017; Ozono et al., 2016).
- Non-material or costless sanctions (e.g., moral judgments) can simultaneously increase cooperation and efficiency, unlike costly punishment (Simpson et al., 2017).

**Negative findings/contextual limits:**
- When institutions are susceptible to corruption or over-regulation, punishment can reduce group efficiency (Lee et al., 2019; Han et al., 2024).
- The efficiency benefit of punishment is not robust across all contexts and often depends on factors such as cultural setting, observability, institution design, or the opportunity for antisocial punishment to emerge.

# 5) Prediction Guidance

**General prediction pattern:**  
Enabling costly peer punishment in a standard PGG *increases cooperation*, but its impact on *efficiency* (group payoff relative to the cooperative optimum) is context-dependent:

- **If control efficiency is low (cooperation rare), peer punishment is likely to *increase efficiency*, up to or toward the cooperative benchmark, provided punishment is cost-effective and well-targeted.**
- **If control efficiency is already moderate or high, enabling punishment rarely increases efficiency, and may even reduce it due to costs incurred from punishment behaviors and the potential for retaliation/vendettas.**
- **Costless sanctions (e.g., moral judgment, approval/disapproval) can increase both cooperation and efficiency (Simpson et al., 2017).**

**Key moderating design dimensions (from most to least direct evidence):**
- **Punishment cost and effectiveness**: Lower cost or higher impact favors positive efficiency effects (Chaudhuri & Paichayontvijit, 2017; Salahshour, 2021).
- **mpcr (public good efficiency)**: High mpcr strengthens the positive effect of punishment on efficiency (Salahshour, 2021; Ozono et al., 2020).
- **Player count and group size**: The effect of punishment can diminish or change sign in larger groups, with local- vs. global-effect distinctions (Ozono et al., 2020).
- **Number of rounds**: Punishment's efficiency advantage increases with more rounds, as the deterrent effect compounds (Chaudhuri & Paichayontvijit, 2017).
- **Population/network structure**: Structured populations can sustain cooperation and efficiency with punishment, whereas in well-mixed populations, defection remains more persistent (Wang et al., 2024).
- **Form of punishment (peer vs. institutional/pool punishment)**, **conditionality (coordinated punishment thresholds, ability to target defectors)**, and **observability (transparency of punishment application)**.

**Less directly evidenced—requires mapping from adjacent or non-payoff outcomes:**
- **Chat/communication**: Not widely studied together with punishment-enabled PGGs for direct efficiency outcomes.
- **All-or-nothing vs. continuous contribution**: Both types studied, but direct efficiency comparisons are uncommon.

*Prediction should be based on control (no-punishment) efficiency, game design dimension matches, and punishment cost-effectiveness. If the context includes known high antisocial punishment, high potential for vendettas, or institutional corruption, expect efficiency gains to be muted or negative.*

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions (i.e., varied and shown to moderate efficiency effects):**
- `player_count`: Many studies explicitly vary group size, show shifts in punishment efficacy and efficiency.
- `num_rounds`: Explicitly manipulated, with clear findings that longer games allow punishment to gradually increase efficiency (Chaudhuri & Paichayontvijit, 2017).
- `mpcr`: Parametric variation across studies; higher MPCR yields stronger positive effects from punishment (Salahshour, 2021; Ozono et al., 2020).
- `punishment_cost` and `punishment_tech`: Frequently manipulated (e.g., cost/fine ratios), shown to be critical moderators of efficiency effect (Fehl et al., 2012; Ozono et al., 2017).
- `all_or_nothing`: Both binarized and continuous contribution games are included.
- `reward_exists`, `reward_cost`, `reward_tech`: Less coverage than punishment, but a few studies directly compare or combine these with punishment (Dong et al., 2016).
- `show_punishment_id`: Considered in some theoretical models (García & Traulsen, 2019; Molleman et al., 2019).

**Indirectly informed/contextually discussed dimensions:**
- `chat`: Included in some studies, but not commonly analyzed as a moderator of punishment's efficiency effect.
- `default_contrib`: Mentioned per study design, not often varied for efficiency analysis.
- `show_n_rounds`, `show_other_summaries`: Rarely manipulated in conjunction with punishment as a main moderator.
  
**Effectively missing or only speculatively addressed:**
- Many design dimensions are often reported for completeness, but not varied systematically to enable strong inference about their specific effect on the punishment-efficiency link.
- Some mechanisms (e.g., population mutation structures, network evolution, exclusion, or restorative justice) are discussed in models adjacent to the PGG/punishment context, making transfer to the prediction task more speculative.

# 7) Important Limitations

- **Context dependence of punishment's efficiency effect:**  
  Enabling punishment does not guarantee efficiency gains; the effect size and even the direction depend on baseline control efficiency, punishment cost effectiveness, susceptibility to retaliation, and the specific punishment architecture.
- **Retaliation and anti-social punishment:**  
  Empirical studies identify retaliation/vendetta cycles (Fehl et al., 2012) and antisocial punishment as undermining efficiency, but few studies systematically measure or model their prevalence and impact across broad parameter spaces.
- **Transferability from adjacent designs:**  
  Where outcomes are behavioral rather than payoff-based, or where the game is only a close variant or adjacent to a standard PGG, findings should be applied to the prediction task with caution.
- **Sparse evidence for some design dimensions:**  
  While many core parameters (e.g., player count, rounds, mpcr, punishment cost) are well covered, others (e.g., chat, default contrib, summary feedback, ID disclosure, reward parameters) are rarely examined as efficiency moderators in PGG-plus-punishment settings.
- **Limited real-world scope:**  
  Most empirical studies are small-N, repeated-lab PGGs with modest stakes and low real-world complexity; scaling to large groups, high-stakes, or naturalistic environments should be done carefully.
- **Heterogeneous institutions and cultures:**  
  Several studies highlight the importance of institutional quality (e.g., risk of corruption, observability, ability to coordinate) and cultural moderation, but direct comparative work is limited.
- **Theory-empirics divergence:**  
  Theoretical models often assume perfect rationality, unlimited population size, or idealized dynamics, which may not translate to experimental or field contexts.

**In summary:**  
The literature offers strong support for the *behavioral effect* (punishment increases cooperation), but the *efficiency effect* (punishment increases group payoff) is much more variable and often moderated (or reversed) by punishment cost, baseline cooperation, design specifics, and potential for negative dynamics. *Direct efficiency measurements in well-specified PGGs with and without punishment remain the gold standard for prediction*. Where data exist, predictions should be closely tied to comparable designs, especially regarding baseline efficiency, punishment technology, and duration. The literature warns against assuming monotonic or universal efficiency benefits from enabling punishment in public-goods-game-like environments.
