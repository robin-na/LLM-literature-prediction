# 1) Evidence Base

This paper set (n=85) is theoretically rich and centers overwhelmingly on formal models and simulations, with only a small minority of empirical or experimental studies. The set is broad in coverage of punishment and cooperation mechanisms within public goods games (PGGs) and close variants, but it is relatively narrow in empirical evidence directly addressing the efficiency impact of peer punishment. Most papers are theoretical, modeling evolutionary or agent-based dynamics, and many focus on group payoff or efficiency as outcomes, although a substantial number prioritize cooperation rates or other behavioral metrics instead.

The evidence on peer punishment's impact on efficiency comes mainly from theoretical models of standard and threshold PGGs, with some adjacent evidence from games involving exclusion, reputation, network structure, and one-shot or repeated PD-like scenarios. Experimental and empirical studies directly measuring group efficiency with and without punishment in real or simulated PGGs are rare in this set. Many papers provide payoff or efficiency data as secondary outcomes or infer efficiency from modeled payoffs.

# 2) Task Relevance

- **pgg_or_variant**: The majority of the literature is `exact` or `close` in relevance, focusing on PGGs or their close relatives (threshold public goods, spatial or networked PGGs, common-pool resource games with PGG-like incentives). Some works are `adjacent`, using PD, snowdrift, or other multi-agent dilemmas.
- **punishment_or_sanctions**: Coverage for punishment is also `exact` or `close` in roughly half the papers, with varied emphasis on institutional, peer, probabilistic, or exclusion-based punishment. There is significant attention to reward-based incentives and combinations of punishment and reward, which are often closely related but not always identical to peer punishment as defined.
- **efficiency_or_related_payoff_outcome**: The set includes a small but substantive cluster of papers with `exact` or `close` attention to efficiency or total/group payoff, with additional studies reporting payoff as a secondary outcome or using related proxies. However, many papers focus only on contributions, cooperation rates, or punishment behaviors (`adjacent`/`weak`).

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes** (`efficiency`, `group payoff`, `welfare`, `total earnings`): A subset of theory papers (e.g., Li et al., 2022; Sun et al., 2023; Vasconcelos et al., 2015; Wang et al., 2019; Wang & Perc, 2022; Liu & Chen, 2020; Ohdaira, 2017; Glover & Kim, 2021) explicitly model efficiency or mean group payoff, drawing analytic boundaries where punishment and cooperation are sustainable and assessing total or normalized payoffs.
- **Non-payoff behavioral outcomes**: The majority of other papers report on cooperation rate, contribution frequency, prevalence of strategic types (cooperators, defectors, punishers), punishment assignment patterns, or norm compliance. These outcomes, while indicative of cooperation, are not always aligned with efficiency, especially where punishment is costly or overused.
- **Ambiguity**: Some papers infer efficiency from average payoffs or phase diagrams but do not formalize efficiency as the ratio to full cooperation or do not consider punishment costs explicitly, making translation to the prediction task ambiguous.

# 4) Main Findings Relevant To Prediction

**Direction of punishment’s effect on efficiency:**
- *Efficiency gains from punishment*: Several theory papers find that enabling punishment—be it peer or institutional—can sustain higher cooperation and increase average group efficiency, but only within bounded parameter spaces (Li et al., 2022; Vasconcelos et al., 2015; Gao et al., 2020; Wang & Perc, 2022). The effect is most positive when punishment is not too costly or severe, mpcr (marginal per capita return) is moderate/high, and the cost-to-impact ratio is favorable.
- *Conditional effects and moderators*: The efficiency benefit of punishment is contingent on the effectiveness and cost of the mechanism (Sun et al., 2023; Wang et al., 2020; Liu & Chen, 2020; Okada et al., 2015; Glover & Kim, 2021). Spatial structure, reputation, network topology, and the presence of reward or hybrid incentive protocols can shift the direction, size, and sustainability of payoff gains.
  - *Network/Spatial Effects*: In structured populations, local (polycentric) or spatial punishment is often more effective than global/institutional punishment at sustaining efficiency, particularly in small groups and high-risk settings (Vasconcelos et al., 2015; Wang et al., 2020).
  - *Second-order incentives*: Several theory papers emphasize the problem of second-order free-riders and the need for meta-incentives (Okada et al., 2015), where punishment alone does not guarantee high efficiency without supporting systems for sanctioning non-punishers.
- *Negative or non-positive effects*: Some studies (Griffin & Belmonte, 2017; Bolton et al., 2018; Frean & Abraham, 2004) show that punishment can reduce efficiency when it is too costly, non-redistributive, or when its presence leads to self-serving dynamics, strategic retaliation, or collusion. Moreover, the presence of mutual punishment/retaliation options in two-sided dilemmas can reduce efficiency below the control.

**Empirical versus theoretical agreement:**
- The theoretical evidence strongly supports the potential for punishment to increase efficiency, but only under carefully specified conditions.
- The limited empirical evidence suggests that, while group coordination and norm-signaling linked to punishment can boost observed cooperation, the translation to actual efficiency gains is often unmeasured or potentially offset by the cost of implementing punishment.

# 5) Prediction Guidance

- **Direct prediction of treatment efficiency from control efficiency and design dimensions** is possible only for settings described by theory papers with explicit payoff/equilibrium formulas (Li et al., 2022; Sun et al., 2023; Vasconcelos et al., 2015; Gao et al., 2020; Wang & Perc, 2022; Okada et al., 2015; Glover & Kim, 2021).
- **For well-mixed, repeated PGGs**, enabling (sufficiently effective and not-too-costly) peer or institutional punishment can, in theory, shift efficiency close to the fully cooperative optimum, but only if mpcr, punishment cost, and group size are favorable, and second-order free-riding is mitigated.
- **In spatial or networked PGGs**, enabling local or polycentric punishment usually increases efficiency more than global/institutional mechanisms, especially for small groups or clusters (Vasconcelos et al., 2015; Wang et al., 2020).
- **Where punishment is costly, easily abused, or retaliatory (mutual punishment/retaliation)**, enabling punishment may reduce or fail to increase efficiency (Griffin & Belmonte, 2017; Bolton et al., 2018; Frean & Abraham, 2004).
- **Behavioral findings on cooperation rates** should not be equated to efficiency; cost of punishment and its impact must be weighed explicitly.
- **Control efficiency**: The effect size of punishment is typically most pronounced when control efficiency is low (defection dominates); as control efficiency rises (due to high mpcr, small group, etc.), the incremental gain from punishment shrinks.
- **Design moderation**: Prediction should condition on game parameters such as player count, mpcr, punishment cost/tech, the presence/absence of chat, visibility, and reputation systems, as these moderate both behavioral and payoff outcomes.

# 6) Design Dimensions Highlighted Across Papers

- **Directly informed**: `player_count`, `num_rounds` (often infinite or large), `mpcr`, `all_or_nothing`, `punishment_cost`, `punishment_tech`, (and in some settings, `reward_exists`, `reward_cost`, `reward_tech`).
- **Indirectly informed**: `chat` (communication), `show_n_rounds`, `show_other_summaries`, `show_punishment_id`—discussed in papers on norm-signaling, communication, and reputation mechanisms.
- **Only contextually discussed**: `default_contrib` (framing), which is rare in this set; `chat` and `show_*` dimensions are discussed mostly in relation to behavioral outcomes or attention to reputation/norms, but rarely for payoff outcomes.
- **Effectively missing**: No consistent theoretical or empirical calibration for `default_contrib`; limited direct mapping for the combined effect of `chat`, `show_n_rounds`, or `show_other_summaries` on efficiency under punishment. Few papers provide explicit consideration of `reward_exists`, `reward_cost`, `reward_tech` dimensions when not paired with punishment.

# 7) Important Limitations

- **Empirical scarcity**: There is a paucity of high-quality experimental or field evidence reporting efficiency as a primary outcome for peer punishment in standard PGGs. Most evidence is theoretical or simulation-based.
- **Behavioral–payoff disconnect**: Many findings on increased cooperation rates or contributions under punishment lack the corresponding efficiency analysis, especially regarding the net cost of punishment; high cooperation does not always mean high efficiency when punishment is costly.
- **Peer vs. institutional punishment ambiguity**: Much of the direct efficiency evidence is for institutional punishment or exclusion; peer punishment, especially as implemented in experimental PGGs, is less rigorously mapped.
- **Parameter sensitivity and generalizability**: The direction and size of efficiency changes are highly sensitive to design dimensions—e.g., punishment cost/effectiveness, group size, mpcr, network structure, and to the presence of meta-incentives or hybrid sanctioning options.
- **Reward mechanisms**: Interactions and tradeoffs between punishment and reward are addressed in theory, but there are few empirical calibrations for their joint/relative effects on efficiency.
- **Conflicting results**: Some papers report that punishment reduces efficiency (especially where it is costly and non-redistributive, or when strategic retaliation/collusion is possible), while more find positive effects conditional on favorable parameter settings.
- **Limited discussion of real-world noise and bounded rationality**: Infinite populations, replicator dynamics, or long-term evolutionary stability are often assumed, sometimes limiting transfer to finite, noisy, or short-horizon experimental settings.

---

**Summary:**  
The literature directly supports the prediction that enabling peer or institutional punishment in PGG-like games can increase group efficiency relative to the control, but this is highly conditional on cost-effectiveness, group structure, and other design dimensions. Theoretical models provide the clearest mapping but require careful parameter alignment and cannot substitute for empirical calibration in all cases. Prediction efforts should give less weight to evidence based only on cooperation rates and more to those with explicit efficiency/payoff analyses. Gaps remain for certain design parameters, and the empirical basis remains thin.
