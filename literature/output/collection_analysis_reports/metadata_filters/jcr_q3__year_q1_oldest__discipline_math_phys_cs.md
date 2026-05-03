# 1) Evidence Base

The reviewed literature comprises a large set of 60 papers, with a heavy emphasis on **theoretical models**, including mathematical analyses, evolutionary game-theoretic modeling, simulation studies, and some literature reviews. Empirical evidence is sparse and mostly indirect, often referencing laboratory studies from earlier primary sources rather than presenting new experimental results. The focus is overwhelmingly on general mechanisms, evolutionary stability, and design contingencies relevant to cooperation in public-goods-game (PGG) settings and related social dilemmas. The paper set covers a broad span of proximal and more distal models (e.g., indirect reciprocity, threshold games, structured populations), but nearly all findings relevant to the prediction task are **theoretical** rather than empirical.

# 2) Task Relevance

- **pgg_or_variant:** Most highly relevant papers model the canonical PGG or very close variants (e.g., n-player PGG, repeated or spatial PGG, or compulsory participation), providing `exact` or `close` matches. Some papers generalize to public-goods-like games or use adjacent settings such as the n-person Prisoner's Dilemma or iterated cooperation games, with relevance labeled as `adjacent`.
- **punishment_or_sanctions:** Many of the core papers model explicit, costly punishment in group interaction settings, yielding `exact` relevance. Several others discuss punishment in the context of adjacent social dilemmas, indirect or reputation-based sanctions, or group selection, leading to a mix of `close` or `adjacent` relevance. A smaller subset only discuss punishment contextually or model the consequences of mechanisms analogous to punishment (e.g., exclusion, withdrawal), rated `weak`.
- **efficiency_or_related_payoff_outcome:** There is a substantial body of evidence addressing **group efficiency**, **total payoff**, or **welfare**, providing `exact` or `close` measures for many theoretical models. However, empirical reports of efficiency are rare. Several papers measure only behavioral outcomes (like cooperation rates) or the prevalence of strategies, not efficiency directly; these are labeled `adjacent` or `weak`.

In summary, the evidence base is **rich in theory**, with a **narrow-to-moderate focus on exact PGG with explicit punishment and group efficiency**, but:
- Direct empirical data on efficiency changes due to punishment in different game parameterizations is **missing** or only triangulated from simulations.
- Many models address adjacent or conceptual variants, which may or may not generalize quantitatively.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes** (`efficiency`, `total payoff`, `group welfare`, `surplus`, `mean fitness`) are **explicit primary outcomes** in many theoretical models (e.g., Cressman et al., 2012; Eldakar et al., 2007; Gintis, 2000; Gintis et al., 2001). These outcomes relate directly to the downstream prediction task definition.
- **Non-payoff behavioral outcomes** (contribution rate, cooperation prevalence, strategy frequencies, norm compliance, punishment frequency) are ubiquitous, especially in studies focusing on evolutionary dynamics and agent-based simulations. Many papers use as proxy holding that higher sustained cooperation *typically* means higher efficiency but do **not always** confirm this with explicit payoff calculations.
- **Contextual/proxy outcomes:** Some adjacent models (e.g., in indirect reciprocity, reputation games) use payoff outcomes to show theoretical maximas exist, but the mapping to PGG efficiency, especially with explicit costly punishment, is sometimes ambiguous.

The clear distinction is that **most direct evidence for efficiency effects comes from mathematical/theoretical analysis rather than lab or field experiments**.

# 4) Main Findings Relevant To Prediction

## Direction of Punishment's Effect on Efficiency

- **Punishment increases efficiency** relative to no-punishment baseline when:
    - Punishment is not too costly and is effective at deterring defectors (Cressman et al., 2012; Gintis, 2000; Milinski & Rockenbach, 2012).
    - Group size is modest-to-small and the game is repeated for sufficient rounds (Eldakar et al., 2007).
    - Antisocial or retaliatory punishment is minimized or excluded (Rand et al., 2010; Powers et al., 2012).
    - Mechanisms for conformist transmission or reputation/reward complement punishment (Henrich & Boyd, 2001; Milinski & Rockenbach, 2012; Ohtsuki & Iwasa, 2004).

- **Punishment can fail to increase or even decrease efficiency** when:
    - Anti-social punishment is present or easy (Rand et al., 2010; Powers et al., 2012).
    - Retaliation against punishers is possible and not costly, or punisher anonymity is low (Wolff, 2012; Janssen & Bushman, 2008).
    - Punishment is costly relative to gains from increased cooperation (Weibull & Salomonsson, 2006).

- **Synergy with reward/reputation:** Theoretical analysis suggests combining punishment with reward or reputation mechanisms can achieve **maximal efficiency** (Cressman et al., 2012; Milinski & Rockenbach, 2012; Chalub et al., 2006).

- **Contextual dependence:** Several models demonstrate that punishment's effect is parameter sensitive, particularly with respect to punishment cost, effectiveness, possibility of retaliation, presence of anti-social punishment, player count, number of rounds, and initial group composition.

## Moderators Identified:
- **Punishment Cost & Technology:** Lower cost and higher effectiveness (punishment impact per unit cost) amplify positive efficiency effects (Eldakar et al., 2007; Okada & Bingham, 2008).
- **Group Size (player_count):** Positive effect persists in small groups, deteriorates in large groups, especially when anti-social punishment or retaliation is possible (Henrich & Boyd, 2001; Suzuki & Akiyama, 2007).
- **Number of Rounds (num_rounds):** Longer games enable the stability of punitive/cooperative equilibria (Eldakar et al., 2007), but excessive game length or easy retaliation can undermine efficacy (Wolff, 2012).
- **Reputation/Visibility:** Reputation systems that enable justified punishment without reputational cost support high efficiency (Ohtsuki & Iwasa, 2004/2006).
- **Retaliation / Anonymity:** When punishers are identifiable, or retaliation is cheap, efficiency gains are reduced or reversed (Janssen & Bushman, 2008).

# 5) Prediction Guidance

The literature provides **strong theoretical justification** for predicting that **enabling punishment will increase group efficiency in PGG-like environments**, *conditional on several moderators*:

- **From Design Dimensions:** Strongest positive effects are expected when:
    - **punishment_cost** is moderate to low;
    - **punishment_tech** (effectiveness) is high;
    - **player_count** is small-to-moderate;
    - **num_rounds** is sufficiently high to allow norm establishment but not so long as to enable retaliation cycles;
    - **anti-social punishment** is not possible (not always a modeled dimension, but critical);
    - **punisher anonymity** (show_punishment_id) is maintained if retaliation risk is a concern;
    - **reward_exists** or **reputation mechanisms** are present, increasing the likelihood of full realization of efficiency gains.

- **From Control Efficiency:** When the no-punishment baseline already exhibits high efficiency (e.g., high MPCR), the marginal effect of punishing may be smaller (Takezawa & Price, 2010).

- **Caveats:**
    - If **punishment is very costly**, or if **anti-social or retaliatory punishment is possible and likely**, the efficiency boost can be attenuated, absent, or negative.
    - **Empirical effect sizes and parameter thresholds are not well established.** Most models are qualitative or parametric.
    - **Behavioral outcomes** (cooperation rates, punishment assigned) are **not** reliable proxies for efficiency unless explicitly linked in the model.

- **Net Recommendation for Prediction:** Absent evidence of strong anti-social or retaliatory punishment, **predict a non-negative, likely positive effect of enabling reasonable-cost, effective punishment on group efficiency, with the effect modulated by group size, round number, punishment parameters, and presence/absence of reward/reputation mechanisms** (Cressman et al., 2012; Eldakar et al., 2007; Gintis, 2000; Milinski & Rockenbach, 2012).

# 6) Design Dimensions Highlighted Across Papers

**Directly/informatively discussed:**
- `player_count` (group size): Explicit parameter in most models (Cressman et al., 2012; Eldakar et al., 2007; Suzuki & Akiyama, 2007).
- `num_rounds`: Key in repeated games models (Eldakar et al., 2007; Wolff, 2012; Leimar, 1997).
- `mpcr`: Central to the payoff structure, often varied in models (Takezawa & Price, 2010; Gintis et al., 2001).
- `punishment_cost` / `punishment_tech`: Cost and effectiveness are universally modeled and highlighted as critical moderators (Okada & Bingham, 2008; Gintis, 2000).
- `all_or_nothing`: Discussed contextually; most models assume continuous or all-or-nothing contributions, with little comparative analysis.
- `reward_exists`, `reward_cost`, `reward_tech`: Some theory and reviews explicitly compare or combine punishment and reward mechanisms (Cressman et al., 2012; Sasaki & Unemi, 2011).
- `show_punishment_id`: Discussed as critical for retaliation and anonymity (Janssen & Bushman, 2008).
- `show_other_summaries`, `show_n_rounds`: Sometimes included as indirect or contextual parameters relevant to norm-tracking and transparency (Gintis et al., 2001).

**Indirectly or contextually discussed:**
- `chat`: Rarely modelled; communication is not a primary focus except as a background variable.
- `default_contrib`: Framing effects, opt-in/opt-out, are not addressed directly.
- `show_punishment_id`: Salient for retaliation risk, but not always a modeled variable.
- `show_n_rounds`, `show_other_summaries`: Affect transparency and strategic reasoning, sometimes included but not central.

**Sparse or missing:**
- None of the papers systematically examine the effect of `chat`, `default_contrib`, or varying `all_or_nothing` structures against standard continuous contributions as a moderator of punishment’s effect on efficiency.
- **No papers provide empirical parameterized mappings** from control efficiency + dimensions to treatment efficiency under punishment.

# 7) Important Limitations

- **Empirical evidence is lacking:** Most predictions are derived from theory/simulation, not experimental data mapping efficiency changes across parameterized game designs.
- **Behavioral outcomes ≠ efficiency:** Many findings rely on cooperation rates or frequencies, not actual realized payoffs, and do not always quantify efficiency effects of punishment independently.
- **Parameter generalizability is uncertain:** Effects of key dimensions—such as cost and technology of punishment, group size, and number of rounds—are often shown directionally (positive/negative) but natural parameter ranges and effect sizes are not deeply quantified.
- **Absence of anti-social punishment as a parameter:** While anti-social punishment is critical, most models do not include it as a configurable variable or design dimension, even though its presence substantially changes expected effects.
- **Retaliation is under-modeled relative to its importance:** Models that do include retaliation find that it can strongly undermine the efficiency benefits of punishment, but how retaliation arises as a function of other design dimensions is not well parameterized.
- **Dimensions such as chat, default_contrib, visibility, and variation in all-or-nothing versus continuous contribution are under-addressed or absent.**
- **Quantitative mapping is missing:** There is no empirically derived or strongly validated formula linking the 14 design dimensions plus control efficiency to treatment efficiency; only qualitative, parameter-contingent predictions are supported.
- **Contextual constraints:** Some papers examine adjacent games, indirect reciprocity, or other social dilemmas, so careful mapping to standard PGGs is required; findings in these domains may not transfer directly.

---

**In summary:**  
The literature provides strong, **parameter-sensitive theoretical justification** for expecting a positive effect of reasonable-cost, effective punishment on group efficiency in public-goods-game-like environments, modulo moderators such as anti-social punishment, group size, retaliation risk, and presence of reward or reputation mechanisms. However, **direct empirical mapping** from game design dimensions and control efficiency to treatment efficiency is missing, and several dimensions are under-explored or absent. Predictions should be made with careful attention to these caveats, preserving the ambiguous or contingent nature of the theoretical results.
