# 1) Evidence Base

The paper set is broad in scope, with 74 papers including theory, simulation, and a smaller subset of experimental or empirical works. For the downstream prediction task—forecasting the efficiency change in a public-goods-game (PGG) or close variant when peer punishment is enabled—most of the directly relevant evidence is found in theory papers and agent-based simulations, with less direct empirical support. The evidence base emphasizes parameterized models (group size, MPCR, punishment cost/effectiveness, threshold, etc.), but there is a notable scarcity of direct empirical effect sizes or field/lab experimental studies that measure efficiency as defined (group payoff relative to full cooperation). Most findings are from stylized models under varying conditions, with outcome measures ranging from cooperation rates to group payoff. Payoff-related results are present but often inferred from behavioral proxies or indirect mechanisms.

# 2) Task Relevance

**pgg_or_variant**  
- **Exact:** Many papers explicitly model or discuss the standard linear or threshold public goods games, or close continuous/all-or-nothing analogs (e.g., Powers, 2018; Sui et al., 2018; Zhang et al., 2019; Wang et al., 2020, 2021; Quan et al., 2018, 2019; Kol'veková et al., 2021).  
- **Close/Adjacent:** Others use closely related social dilemmas (threshold games, common pool resources, networked/social dilemmas), while some rely on adjacent settings such as the prisoner's dilemma, trust game, or traveler's dilemma. These provide partial analogs but must be transferred with caution to standard PGGs.
- **None:** A sizeable subset of papers concerns adjacent games with no explicit PGG structure.

**punishment_or_sanctions**  
- **Exact/Close:** A large number of papers model explicit punishment or sanction mechanisms—peer punishment, institutional punishment, third-party punishment, exclusion, etc.—with calibrated parameters for cost, magnitude, and scope.  
- **Adjacent:** Some model related mechanisms such as ostracism, network rewiring, or partner switching, which serve as functional substitutes for punishment but do not carry explicit payoff costs.
- **None:** Several papers analyze only reward, communication, or reputation mechanisms, and some omit all forms of punishment.

**efficiency_or_related_payoff_outcome**  
- **Exact:** A minority of papers directly report group efficiency, mean or total group payoff, or the fraction of the maximal cooperative payoff (e.g., Powers, 2018; Zhang et al., 2019; Wang et al., 2020; Kol'veková et al., 2021).
- **Close/Adjacent:** More commonly, close proxies such as average payoff, welfare, or group earnings are used. Quite a few report only on contribution or cooperation rates, requiring inferences about efficiency through parameter synthesis.
- **Weak/None:** Many papers only observe behavioral outcomes without relating them to group payoff.

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes (Directly Relevant):**
- Efficiency (ratio of actual group payoff to payoff under full cooperation)
- Mean group payoff
- Total earnings
- Welfare
- Resource abundance or growth rate (for resource games)

**Non-Payoff Behavioral Outcomes:**
- Contribution rate/cooperation rate
- Success rate of public good provision (thresholds met)
- Punishment or reward frequency
- Strategy abundance or adoption rates

**Distinction:**  
Several highly cited findings about the "effectiveness" of punishment in promoting cooperation rely solely on increased contribution or cooperation rates, without accounting for efficiency loss due to punishment expenditures (e.g., Moreno & Gutierrez-Garcia, 2018; Yang & Fu, 2020). Only a subset models or measures net efficiency (punishment cost subtracted from group payoff). A few explicitly warn that punishment-induced cooperation may not always translate into higher efficiency, especially when punishment is costly or misapplied (Quan et al., 2019; Wang et al., 2020).

# 4) Main Findings Relevant To Prediction

**Punishment Tends to Increase Efficiency When:**
- The basic game (control) efficiency is low due to high rates of free-riding, and
- Punishment is sufficiently effective (high penalty relative to cost), not so costly as to negate gains, and preferably endogenous or peer-based (Zhang et al., 2019; Kol'veková et al., 2021; Wang et al., 2020; Gao & Liang, 2020; Sui et al., 2018).
- Population structure, group size, and MPCR interact with punishment: smaller groups and higher MPCRs typically make punishment more effective (Powers, 2018; Sui et al., 2018).

**Punishment Does NOT Always Raise Efficiency:**
- If punishment is weak (low fine or high cost), automatic/non-peer, or non-deterrent, it can be strictly efficiency-reducing (Yang et al., 2020; Nakamura et al., 2019).
- If defectors can avoid/evade punishment cheaply, efficiency gains may disappear (Wang et al., 2020).
- Overuse or misapplication of punishment can suppress group welfare even as cooperation rises (Quan et al., 2019).
- There exist critical thresholds for cost-effectiveness; excess punishment cost or weak intervention can negate gains (Zhang et al., 2019; Yang et al., 2020).

**Contextual and Moderator Effects:**
- Institutional context (rules for punishment deployment—voting, automaticity, shared vs. solo cost) strongly mediates outcomes (Powers, 2018; Kol'veková et al., 2021).
- Social exclusion (ostracism) may substitute for direct monetary punishment but with its own cost/benefit parameters (Sui et al., 2018).
- Reward mechanisms, especially when combined adaptively with punishment, may be more efficient in certain conditions, e.g., low initial cooperation (Wang et al., 2021 Physics Letters A).
- Voluntary participation and the presence of loners alter dynamics, often reducing the need for punishment (Sui et al., 2018).

**Quantitative Synthesis Highlights:**
- Enabling punishment, especially low-cost, endogenous, peer or shared forms, can shift a system from low-efficiency equilibria (all-defection) to high-efficiency equilibria (Kol'veková et al., 2021; Gao & Liang, 2020).
- The effect of enabling punishment is non-monotonic and context-dependent; punishment can sometimes lower efficiency if miscalibrated.

# 5) Prediction Guidance

**Direct Evidence (Most Informative for Prediction):**
- If the control (no-punishment) game has low efficiency, introducing peer punishment of moderate-to-low cost and high effectiveness is likely to increase efficiency. If the control efficiency is already high, the marginal gain from punishment is often smaller or negative due to additional costs (Zhang et al., 2019; Kol'veková et al., 2021).
- Prediction should focus on the parameters: player count, number of rounds, mpcr, all_or_nothing, punishment_cost, punishment_tech, and (where relevant) whether punishment is endogenous/shared, peer or centralized, and if reward exists (Powers, 2018; Sui et al., 2018).
- The magnitude of the efficiency boost from punishment depends most on the improvement in cooperation minus the incurred cost—if punishment cost is too high for the achieved cooperation improvement, efficiency can worsen.
- When peer punishment is enabled in environments close to the model parameterizations above (group size 4+, moderate MPCR, standard punishment cost/fine ratio, static groups), expect a moderate-to-large efficiency increase *if control efficiency is low* and punishment parameters are in the empirically/theoretically identified "effective" regime.
- For institutional or automatic punishment, the evidence is more mixed or even negative; prediction here should be cautious and may even anticipate no efficiency gain (Yang et al., 2020).
- The paper set consistently finds that the benefit of enabling punishment is sensitive to threshold effects—insufficient intensity or excessive cost can render punishment ineffective or counterproductive.

**Indirect/Mechanistic Guidance:**
- Contribution or cooperation rate increases are common after punishment introduction, but these must be discounted for cost to assess efficiency. Mechanistic models (Quan et al., 2019; Wang et al., 2020) provide parameter regions where the transition from low to high efficiency occurs.
- If the design allows for defectors to evade punishment cheaply, expect little or no efficiency gain from enabling punishment (Wang et al., 2020; Quan et al., 2019).
- If partner switching, voluntary participation, or reward is present and already induces high cooperation, the incremental efficiency benefit of punishment is lower.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- `player_count`: Commonly parameterized; small and moderate group sizes are well studied.
- `num_rounds`: Typically finite and small to moderate; present in most models but rarely a strong moderator except via learning/adaptation.
- `mpcr`: Major moderator of both control and treatment efficiency effects; higher MPCR favors both baseline cooperation and punishment effectiveness.
- `punishment_cost`: Carefully parameterized, evidence highlights its central role in moderating effect on efficiency.
- `punishment_tech` (effectiveness/magnitude): Explicitly modeled alongside cost; high effectiveness relative to cost is crucial for positive efficiency effect.
- `all_or_nothing`: Modeled in both all-or-nothing and continuous settings, with consistent results across forms.
- `reward_exists`, `reward_cost`, `reward_tech`: Discussed in some models; reward can substitute or complement punishment with context-dependent effectiveness.

**Indirectly Informed/Contextual Dimensions:**
- `chat`: Seldom modeled directly; when present, often as an exogenous ability to communicate, sometimes leading to higher baseline cooperation/efficiency and reducing punishment’s additional benefits.
- `default_contrib`: Occasionally manipulated via framing; generally, not a primary focus.
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Information display and transparency sometimes appear as moderators in institutional studies, but rarely as systematically varied dimensions.
- `punishment_tech`/structure (peer vs. centralized, voting vs. automatic): Institutional form is a notable moderator of result direction/size but is frequently entangled with other dimensions.

**Effectively Missing Dimensions:**
- Some information/observability dimensions and interface/feedback dimensions (e.g., `show_n_rounds`, `show_punishment_id`, interface design) are generally not systematically manipulated. Evidence about the impact of these on punishment efficacy is scarce or absent.

# 7) Important Limitations

- **Empirical Gaps:** The majority of direct evidence comes from theoretical/simulation studies rather than controlled lab or field experiments that measure group efficiency with and without punishment directly. Experimental reality may diverge from stylized models.
- **Outcome Measurement:** Many studies report only behavioral measures (cooperation rates), not efficiency or total group payoff after subtracting punishment costs. This introduces risk of overestimating the benefit of punishment.
- **Parameter Regime Sensitivity:** Efficiency effects hinge on the fine balance of punishment cost and effectiveness; small parameter shifts can dramatically flip the predicted sign of the effect (positive/negative). Real-world estimates for these parameters are often rough.
- **Centralization vs. Peer Structure:** Evidence on institutional/automatic punishment (as opposed to peer punishment) is sparser and less consistently positive; drawing strong conclusions for all forms of punishment is unwarranted (Yang et al., 2020).
- **Context and Scope:** Many models use homogeneous, well-mixed populations and stylized update/diffusion rules; generalization to heterogeneous, dynamic, or networked real-world groups may be limited.
- **Incomplete Dimensional Coverage:** Some design dimensions relevant to prediction (information display, default contribution framing, etc.) are rarely foregrounded or systematically analyzed, limiting fine-grained predictions along those axes.
- **Interaction with Other Mechanisms:** The predicted effect of punishment can be diluted, amplified, or reversed when combined with partner switching, reward, voluntary participation, or reputation mechanisms, but joint effects are not always covered in depth.

---

**Summary Statement:**  
The literature most directly informs predictions about the effect of peer punishment on efficiency in standard or threshold PGGs, especially when game parameters (player count, MPCR, punishment cost/effectiveness) are known and the control (no-punishment) efficiency is low. Under effective and not overly costly punishment, large efficiency gains are likely. However, there is substantial ambiguity in settings with costly or automatically administered punishment, or when punishment mechanisms are blunt or non-deterrent. Prediction quality is highest when parameter regimes (including punishment design and group structure) match those explored in detail in the theoretical and agent-based evidence. Contextual and information-based design features and empirical effect sizes remain key sources of uncertainty.
