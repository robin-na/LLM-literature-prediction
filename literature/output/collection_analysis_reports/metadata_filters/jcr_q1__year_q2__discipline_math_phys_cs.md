# 1) Evidence Base

The paper set is broad in its coverage of theoretical models, with a large proportion (the majority) of items being theory or simulation-based studies without direct empirical/experimental data. A moderate subset of experimental (lab-based) studies is present, though these tend to focus on behavioral outcomes (e.g., contribution rates, norm compliance) more often than on payoff-based efficiency. The theoretical coverage of public goods games and their variants is extensive and rich, with many models parametrizing core game design dimensions such as player count, rounds, MPCR (marginal per-capita return), and especially punishment cost and technology.

Empirical evidence directly addressing peer punishment's effect on group efficiency in PGGs is sparse. Most theoretical models report efficiency or closely related payoff outcomes, and these models serve as the dominant evidence base for downstream prediction on how enabling punishment alters efficiency, given game design and baseline (control) efficiency.

# 2) Task Relevance

**pgg_or_variant:**  
- **Exact relevance**: Numerous papers focus directly on public goods games (PGG), including standard and threshold PGGs. Most theoretical and some simulation studies are designed around PGG (e.g., Perc et al., 2017; Szolnoki & Perc, 2013; Vasconcelos et al., 2015; Adami et al., 2016).
- **Close/adjacent relevance**: Some studies examine closely related environments (e.g., multi-player prisoner's dilemma, snowdrift games, trust games, or adversarial games), providing mechanism insights (e.g., Luo & Zhao, 2013; Ohdaira, 2017).

**punishment_or_sanctions:**  
- **Exact relevance**: Many papers explicitly manipulate punishment, including peer punishment, pool punishment, exclusion, and meta-incentive frameworks (e.g., Perc et al., 2017; Szolnoki & Perc, 2017; Adami et al., 2016; Wang et al., 2015).
- **Close/adjacent relevance**: Several examine reward mechanisms, observer sanctions, or punishment analogues (e.g., exclusion as a type of sanction; Al-Dhanhani et al., 2014) or comparative/conditional punishment complexities (Okada et al., 2015).
- **Non-relevant**: A subset does not include punishment, focusing instead on norms, reputation, or social mechanisms without explicit cost-imposing sanctions (marked as none or adjacent).

**efficiency_or_related_payoff_outcome:**  
- **Exact/close relevance**: A robust core of theoretical papers reports group efficiency or total payoff as primary or secondary outcomes (e.g., Vasconcelos et al., 2015; Adami et al., 2016; Wang et al., 2015).  
- **Adjacent/weak relevance**: Many works report only behavioral outcomes (contributions, cooperation), making inference about efficiency possible only when costs/rewards are simple and transparent.  
- **Empirical experimental studies**: Those with efficiency outcomes are rare—experimental work reports behavioral outcomes more frequently (e.g., Peysakhovich & Rand, 2016; Villatoro et al., 2014).

# 3) Outcomes Measured In The Literature

- **Payoff-related (Effciency/Total Earnings/Group Welfare/Surplus):**  
  - Theoretical PGG papers predominantly report group efficiency as defined (ratio of total payoff to maximal cooperative payoff), group earnings, or welfare, especially in relation to the core design dimensions and manipulation of punishment (Perc et al., 2017; Szolnoki & Perc, 2013; Adami et al., 2016; Vasconcelos et al., 2015; Wang et al., 2015).
  - Some adjacent domain theory papers on PDG, SDG, trust games, or adversarial public-goods-like setups also provide direct group efficiency or total payoff analyses (Ohdaira, 2017; Luo & Zhao, 2013; McBride et al., 2016; Griffin & Belmonte, 2017).

- **Non-payoff (Behavioral: Contribution/Cooperation/Punishment Rates, Norms):**  
  - The majority of empirical lab studies and some theoretical papers report primarily on cooperation rates, fraction of cooperators, or punishment behavior (Szolnoki & Chen, 2017; Villatoro et al., 2014; Villatoro et al., 2014; Zhang et al., 2016). These are proximate but not equivalent to efficiency.
  - Some studies focus on normative, reputational, or information-based behavioral effects (e.g., Schram & Charness, 2015; Ohtsuki et al., 2015).

# 4) Main Findings Relevant To Prediction

- **Overall Direction of Punishment’s Effect:**  
  - **Theory and simulation models** consistently find that enabling (peer) punishment generally increases efficiency, *conditional* on punishment’s cost-effectiveness, group size, MPCR, and the absence of strong antisocial punishment (Szolnoki & Perc, 2013; Perc et al., 2017; Adami et al., 2016).
  - **Punishment cost**: When punishment costs are low relative to their effect, efficiency gains are more likely. High-cost punishment, antisocial punishment, or poorly tuned systems can *reduce* efficiency (Perc et al., 2017; Griffin & Belmonte, 2017).
  - **Reward versus Punishment:** Reward mechanisms alone do not generally outperform punishment in improving efficiency; combining them offers little additional gain except under very low-cost regimes (Szolnoki & Perc, 2013).
  - **Spatial/Networked Structure:** Effects can depend on spatial structure—clustering of cooperators and punishers strengthens efficiency gains, especially when synergy factor (MPCR) is low (Perc et al., 2017; Szolnoki & Perc, 2017).
  - **Exclusion & Meta-incentive Mechanisms:** Exclusion-based punishment is effective especially in small groups or with effective exclusion (Li et al., 2015). Meta-incentives (rewards for rewarding, etc.) are critical in sustaining efficiency in complex incentive situations (Okada et al., 2015).
  - **Empirical Studies:** Direct lab evidence for efficiency impact is rare—laboratory experiments more often document increased cooperation/contribution rates with punishment, but leave overall group earnings (i.e., efficiency) ambiguous, or unreported.

- **Conditional Effects and Parameter Sensitivity:**  
  - **Effectiveness threshold:** There is often a critical punishment cost/effectiveness (and MPCR) region: punishment’s efficiency benefit is largest near the transition from defection to cooperation (Adami et al., 2016).
  - **Group Size (player_count):** Smaller groups often benefit more from punishment; large groups may dilute the effect unless punishment is pooled or centralized (Vasconcelos et al., 2015).
  - **Institutional Structure:** Polycentric/local punishment outperforms centralized/global punishment in sustaining high efficiency (Vasconcelos et al., 2015; Pacheco et al., 2014).
  - **Antisocial Punishment:** In well-mixed populations, antisocial punishment can undercut efficiency, but certain second-order dynamics can neutralize this in structured games (Szolnoki & Perc, 2017).
  - **Punishment Technology:** Adaptive, probabilistic, or proportional punishment mechanisms can outperform simple deterministic punishment, especially in reducing unnecessary costs and improving net efficiency (Ohdaira, 2017; Luo & Zhao, 2013).

- **Non-payoff Outcome Evidence:**  
  - Widespread increases in contribution/cooperation with punishment are documented, but do not always translate into net group efficiency gains due to punishment’s cost “burden” (evidence from both theory and experiment; see Villatoro et al., 2014; Peysakhovich & Rand, 2016).

# 5) Prediction Guidance

- **Direct Implications for Prediction:**
  - *When punishment is enabled and cost-effectiveness is favorable*, efficiency is generally increased compared to no-punishment control (Perc et al., 2017; Szolnoki & Perc, 2013; Adami et al., 2016; Vasconcelos et al., 2015; Wang et al., 2015).
  - *Parameters to consider in prediction:*
    - **Punishment cost (CONFIG_punishmentCost):** Gains are lost if cost is too high relative to impact.
    - **Synergy/MPCR (CONFIG_mpcr):** Effects of punishment are more pronounced near the MPCR threshold for cooperation.
    - **Group size (CONFIG_playerCount):** Small groups, or locally enforced punishment, favor efficiency gains.
    - **Spatial/network structure:** If available, cluster-based interactions enable more stable efficiency improvement.
    - **Reward mechanisms (CONFIG_rewardExists):** Adding reward rarely improves upon punishment alone unless costs are minimal for both.
    - **Antisocial punishment risk:** If present and unchecked, can disrupt efficiency unless second-order free-riding or structured play suppresses it.

- **Use of Control Efficiency:**
  - Predictions should be *anchored to the baseline efficiency* (no-punishment condition), adjusting expected efficiency upward when punishment is predicted to be effective (see phase diagrams and payoff equations in Perc et al., 2017; Adami et al., 2016).
  - Where anti-social punishment or high punishment cost is probable, adjustment may be null or even negative.

- **Interpretation Caveats:**
  - **If model design is out-of-sample** (e.g., non-standard punishment mechanisms or exotic spatial structures), theoretical results may not generalize quantitatively.
  - **Where only non-payoff outcomes are reported** (as in many empirical studies), efficiency cannot be directly inferred, and predictions should be qualified accordingly.

# 6) Design Dimensions Highlighted Across Papers

- **Directly Informed Dimensions:**
  - **player_count:** Extensively analyzed in theory papers; smaller groups often experience larger efficiency boosts with punishment (Szolnoki & Perc, 2013; Vasconcelos et al., 2015).
  - **mpcr:** Widely covered; closely tied to phase transitions in efficiency (Perc et al., 2017; Adami et al., 2016).
  - **punishment_cost / punishment_tech:** Central in almost all relevant works; quantified phase diagrams indicate the precise role of cost and implementation (Szolnoki & Perc, 2013; Adami et al., 2016; Wang et al., 2015).
  - **reward_exists / reward_cost / reward_tech:** Sometimes discussed for completeness or as comparators, but less central than punishment (Szolnoki & Perc, 2013; Okada et al., 2015).
  - **num_rounds, all_or_nothing:** Often specified in models, but interactions with punishment effects are less systematically explored.

- **Indirectly or Contextually Informed:**
  - **Spatial/network interaction structures, clustering parameters:** Heavily featured in theory; less so in experiments.
  - **show_other_summaries, show_n_rounds:** Information transparency or feedback occasionally addressed via analogues (e.g., public observability in Ohtsuki et al., 2015; Chen et al., 2017).
  - **chat, default_contrib, show_punishment_id:** Rarely analyzed directly.

- **Effectively Missing or Sparse:**
  - **chat, default_contrib, show_punishment_id:** Almost never operationalized or discussed in terms of their impact on efficiency effect of punishment.
  - **Complex meta-institutional features:** (e.g., meta-incentives beyond first-order punishment), are present in only a few theoretical papers (Okada et al., 2015), but not empirically instantiated.

# 7) Important Limitations

- **Empirical Scarcity:** Direct experimental/empirical data on efficiency outcomes with/without peer punishment in PGGs is scarce. Most experimental results pertain to cooperation rates, not efficiency, making direct quantitative calibration difficult.

- **Generalization Limits:** The majority of the evidence is theoretical, relying on stylized network and evolutionary models which may not capture all real-game complexities (e.g., real human behavior, institutional context, unforeseen anti-social strategies).

- **Parameter Sensitivity:** Many key findings are conditional—punishment improves efficiency only within certain cost/effectiveness ranges, group sizes, or MPCR values. Important interactions among dimensions (e.g., how punishment cost interacts with MPCR or group structure) may not be fully mapped for all relevant combinations.

- **Missing Dimensions:** Several prediction-relevant dimensions such as chat, information disclosure, default contribution framing, and identity observability are rarely or never analyzed for their moderation of punishment’s payoff effect. Thus, predictions regarding their effect on the efficiency gain of punishment must be speculative.

- **Behavioral Versus Payoff Focus:** Much of the experimental literature—and a sizable minority of theoretical work—reports on cooperation or contribution rate alone, not efficiency. Drawing conclusions about efficiency from these papers can be misleading, since group efficiency can decrease if costly punishment is excessive or misdirected, even as cooperation rises.

- **Ambiguity and Disagreement:** There are contexts (e.g., with costly non-redistributive punishment, antisocial punishment, or unstable coordination equilibria) where enabling punishment may reduce or fail to improve efficiency (Perc et al., 2017; Griffin & Belmonte, 2017; Okada et al., 2015). Disagreement is more pronounced in non-standard, adjacent game types, or under certain dynamic/evolutionary updating rules.

---

**In summary**, this literature set provides strong, theory-driven guidance for predicting the impact of enabling punishment on efficiency in PGG-like games, particularly as a function of core design parameters like group size, MPCR, and punishment cost/tech. Direct empirical evidence on efficiency is lacking, and several design dimensions are underexplored; care is needed when extending the findings to new settings or to dimensions not systematically studied in this literature.
