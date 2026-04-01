# 1) Evidence Base

The paper set is composed entirely of theoretical and computational/modeling studies with no experimental or empirical (lab/field) data. The set is broad in terms of game structures (extending beyond standard PGGs to include various social dilemmas, trust games, and public-goods-like models), but for the core prediction task—public goods games (PGGs) with and without peer punishment and efficiency outcomes—coverage is highly variable. There is a substantial concentration of work with `exact` relevance to the PGG structure and efficient payoff outcomes, but many papers are tangential or only indirectly informative, discussing adjacent games or focusing strictly on behavioral rather than payoff-based outcomes.

There is a strong focus on model-based and analytical mechanism arguments, with some review and synthesis papers drawing on empirical literature, but primary outcome data are typically derived from simulations or equilibrium analysis. This means causal mechanisms are well-theorized and parameter effects can be explored, but empirical variability is harder to assess.

# 2) Task Relevance

**a. PGG or Variant**
- Many papers address standard or direct variants of the public goods game (`exact` relevance), with a sizeable minority examining close analogues (e.g., N-person snowdrift, CPR games; `close` relevance), and others focusing on only adjacent models (e.g., Prisoner’s Dilemma, trust/ultimatum games; `adjacent` or `weak`). Some papers are `none` for PGG but discuss related cooperative dilemmas.

**b. Punishment or Sanctions**
- About half of the evidence base directly models costly peer punishment or institutional sanctions (`exact`), some study social exclusion or monitoring as a close parallel, and others discuss reward, exclusion, or related mechanisms (`adjacent`). Many only discuss punishment contextually, and a significant minority do not address punishment at all.

**c. Efficiency or Related Payoff Outcomes**
- A subset of papers is `exact` in treating efficiency/group payoff/surplus as a primary outcome; many others focus exclusively on behavioral outcomes—contribution/cooperation rates, strategy prevalence, or compliance—without direct efficiency reporting (`adjacent` or `weak` for payoff). Some review and mechanism papers supply links but seldom provide empirical payoff data.

# 3) Outcomes Measured In The Literature

**Payoff-related Outcomes:**
- Group efficiency (ratio of total payoff to full-cooperation payoff), group surplus, total earnings, welfare, and aggregate payoff are modelled and reported in many `exact`-relevance PGG and CPR models (e.g., Levine & Modica, 2016; Hwang & Bowles, 2012; Wang et al., 2010; Noailly et al., 2007, 2009; Sigmund et al., 2011).
- In several adjacent games (e.g., multi-agent trust, repeated PD with punishment), efficiency is similarly defined as average or total payoff relative to an optimal or defect baseline.

**Non-payoff Behavioral Outcomes:**
- The majority of models, especially those focusing on extensions/modifications or spatial/networked designs, report behavioral outcomes: average contribution, cooperation frequency, prevalence of punishers, etc.
- Outcomes like norm compliance, trust rate, and strategy frequencies are common, especially in papers with only indirect or adjacent relevance for payoff-based prediction.

**Distinction:**
- Many behavioral-outcome studies infer higher efficiency from increased cooperation, but this mapping is not always validated—costs of punishment can offset gains, or cycles/norms may not result in better payoffs.

# 4) Main Findings Relevant To Prediction

**Empirical/Theoretical Synthesis:**
- There is near-universal theoretical agreement (supported by robustness across models and parameter sweeps) that **enabling peer punishment in PGGs increases efficiency** relative to the control (no punishment), especially when: group size is moderately large, punishment is effective or salient, and the cost to punishers is not prohibitive (Levine & Modica, 2016; Dejong et al., 2008; Sigmund et al., 2011; Wang et al., 2010; Noailly et al., 2007, 2009).
- **Design Dependency:** The magnitude and sign of the effect **strongly depends on design dimensions**:
    - **Punishment Cost and Effectiveness:** Efficiency gains are maximized when the punishment is sufficiently strong (high fine, low cost). High punishment cost can negate or reverse the benefit, leading to lower efficiency if the punishment burden outweighs efficiency increases from cooperation (Sigmund et al., 2011; Wang et al., 2020; Wang, Liu, & Chen, 2020).
    - **Player Count & Group Size:** Larger groups benefit more from well-designed punishment, since control games tend to collapse; small, face-to-face groups can sustain some efficiency even without punishment (Levine & Modica, 2016; Dejong et al., 2008).
    - **MPCR:** Low MPCR environments (where cooperation is individually irrational) show bigger efficiency gains when punishment is enabled, but only if the sanctions are strong/cost-effective enough.
    - **Voluntary Participation:** Efficiency benefits of punishment are greater when group members can abstain rather than being compelled (Sigmund et al., 2011).
    - **Network/Spatial Structure:** Local or clustered punishment can be more effective than global peer punishment in sustaining efficiency (Noailly et al., 2007; POLLOCK, 1988).
    - **Reward Mechanisms:** When reward mechanisms are included, the impact depends on how they are targeted—rewarding cooperators is more effective at raising payoff than rewarding punishers; combining rewards and punishment without careful design can reduce efficiency (Shen et al., 2022).

- **Moderators and Mechanisms:**
    - **Social Preferences:** If unconditional altruism is high, the **willingness to punish falls**, which reduces the deterrence power of punishment and can actually reduce efficiency in some scenarios (Hwang & Bowles, 2012).
    - **Disguise/Avoidance:** Punishment effectiveness is reduced if defectors can avoid detection/punishment at low cost (Wang, Liu, & Chen, 2020).
    - **Institutional Structure:** Pool or institutional punishment (as opposed to peer) with second-order punishment can further stabilize cooperation and improve efficiency, but at the risk of higher enforcement costs and possible inefficiency if mis-targeted (Sigmund et al., 2011; Sasaki et al., 2016).
    - **Group Heterogeneity and Network Topology:** Efficiency effects can be non-monotonic when group heterogeneity increases or when social monitoring crowds out intrinsic motivation (Orr, 2001; Haag & Lagunoff, 2006).

**Contrasts and Ambiguities:**
- Certain models highlight **negative or mixed effects**: High levels of altruism or normatively motivated group members can reduce the efficiency benefit or even make punishment counterproductive; crowding out and strategic complexities can also reverse expected efficiency gains (Hwang & Bowles, 2012; Orr, 2001; Isakov & Rand, 2012).
- Some adjacent models find **punishment can reduce efficiency** if primarily used for coercive or non-cooperative purposes, or if costs are misallocated (Isakov & Rand, 2012). However, these are less central for standard PGGs.

# 5) Prediction Guidance

- **Best-Supported Prediction:** **Enabling peer punishment in standard PGGs will, in most scenarios, increase group efficiency compared to control**, with the exact benefit depending on the initial level of efficiency, group size, MPCR, punishment cost and fine, and the structure of the punishment mechanism.
- The predicted effect is strengthened as **control efficiency falls**—i.e., in games where free riding is dominant in the absence of punishment, the addition of punishment is most likely to move outcomes closer to full efficiency.
- **Game design dimensions** most informative for prediction (see section 6) should be parameterized in the same way as the theoretical models, especially player count, MPCR, punishment cost/effectiveness/tech, and presence/structure of reward or exclusion mechanisms.
- **Moderators to flag:**
    - **Low punishment cost/high punishment fine:** Predict larger efficiency gain.
    - **Larger player count:** Typically increases the size of the effect, especially when control efficiency is low.
    - **Low baseline cooperation/control efficiency:** Punishment effect is more pronounced.
    - **Social preferences:** In highly prosocial or reciprocally motivated groups, punishment may have less impact or could even crowd out efficiency.
    - **Structured networks/voluntary participation:** Can amplify the effect if punishment is local and participants can self-sort.
- **Behavioral-outcome-based studies** should *not* be used to estimate efficiency unless the payoff mapping is clear and punishment costs are included.
- When efficiency is already near-maximal in control, the marginal gain from punishment can be small, zero, or even negative if punishment costs are high.

# 6) Design Dimensions Highlighted Across Papers

**Directly and Explicitly Informed Dimensions:**
- `player_count`: Directly discussed in nearly all exact-relevance papers; size effects and group scaling are explicitly modeled.
- `num_rounds`: Present in repeated/iterated dilemma models and discussed in relation to the stability of cooperation and discounting.
- `all_or_nothing`: Many models use binary (all-or-nothing) versus continuous contribution; effect noted in some models.
- `mpcr`: Marginal per-capita return is a key moderator in all efficiency and threshold analyses.
- `punishment_cost`, `punishment_tech`: Cost, effectiveness, and implementation of punishment are deeply analyzed in quantitative models.
- `reward_exists`, `reward_cost`, `reward_tech`: Less central but addressed directly in several models exploring mixed incentive systems.
- Some include `show_n_rounds`, `show_other_summaries` in context of repeated play and information structure.

**Indirectly Informed or Contextually Discussed:**
- `chat`: Occasionally discussed in contextual analyses or as a communication/enforcement mechanism; impact on efficiency is theorized, not quantitatively estimated for PGGs.
- `default_contrib`: Not usually a focal variable—rarely manipulated, sometimes implicit in initial-state effects.
- `show_punishment_id`: Sometimes addressed in models of reputation or social exclusion, but not always parameterized.

**Effectively Missing or Sparse:**
- Identity/summary disclosure (`show_other_summaries`, `show_punishment_id`) only rarely appears as a modeled variable, with little quantitative guidance for prediction.
- Framing variables (`default_contrib`) and explicit chat manipulation are largely under-examined for their direct impact on efficiency outcomes when punishment is introduced.

# 7) Important Limitations

- **Absence of Experimental Data:** The paper set is strictly theoretical/simulation/modeling; no lab or field experiments are included. This limits confidence about empirical effect sizes and variability due to real-world human behavior and noise.
- **Payoff Mapping in Behavioral Models:** Many findings are based on behavioral outcomes (cooperation/contribution rates) with the efficiency impact inferred but not directly measured; mapping to payoff/efficiency requires caution, especially when punishment costs are significant or when nonlinearity affects group payoff.
- **Limited Coverage for Certain Dimensions:** Some prediction-relevant design dimensions (e.g., information structure, contribution framing, disclosure of identities) are sparsely or not at all covered.
- **Generalizability to Human Subjects:** The models assume rational or boundedly rational agents but do not capture the full spectrum of human social preferences, learning, errors, or cultural effects—especially as related to crowding out, antisocial punishment, or fairness concerns.
- **Empirical Disagreement & Moderation:** While general trends are robust, exceptional cases exist where punishment does not increase efficiency (e.g., high altruism crowds out punishment, costly or error-prone punishment, efficacy undermined by disguise or by social/cognitive factors).
- **Structure Sensitivity:** Spatial, network, or institutional structures (e.g., local, pool punishment, exclusion, or voluntary participation) can sharply moderate the efficiency effect, and many are only theorized under stylized assumptions.

---

**In summary**: The theoretical literature as represented provides strong, mechanism-supported guidance that enabling peer punishment in the standard public goods game setting will typically increase group efficiency relative to control, with the effect size and presence modulated by game design parameters—especially punishment cost/effectiveness, group size, MPCR, and social/institutional structure. However, these predictions are based on model results and carry important caveats regarding real-world generalizability, possible negative side effects, and underexplored design dimensions. Models with only behavioral outcomes cannot reliably inform efficiency prediction unless the payoff structure (including punishment costs) is fully specified.
