# 1) Evidence Base

The paper set contains a substantial mix (30 papers), with a predominance of theoretical works and a smaller number of empirical laboratory experiments. The bulk of the evidence is theoretical modeling of public goods games (PGG) and their variants, plus adjacent games and contexts (e.g., mutual aid, division of labor, repeated PD). Most theory papers develop explicit game models and conduct parameter sweeps, with several providing formulas and phase diagrams for efficiency. Experimental studies most often measure cooperation rates or neural/behavioral correlates rather than direct payoffs.

On the targeted question—predicting the effect of enabling peer punishment on efficiency in PGG-like environments using game design features and control game efficiency—the evidence base is fairly broad in coverage of conceptual moderators and design space, but relatively narrow in direct empirical demonstration of treatment efficiency. Relatively few papers provide direct, quantitative, empirical estimates of group efficiency changes due to enabling punishment; most empirical studies focus instead on behavior (contribution rates) rather than payoffs. Nonetheless, there is a strong theoretical foundation directly addressing PGGs with punishment and their impact on efficiency.

# 2) Task Relevance

**pgg_or_variant**:  
- **exact:** The majority of theory papers (e.g., Jiao et al., 2020; Fang et al., 2020; Wang & Lv, 2019; Huang et al., 2018) model exact PGGs, often with peer or institutional punishment mechanisms. Some empirical papers use exact or very close PGGs (e.g., Micheli et al., 2021).  
- **close/adjacent:** Several papers model adjacent games (threshold PGG, division of labor, mutual aid, PD, dictator), often with partial applicability to prediction in PGGs.
- **none:** A handful are not games at all or focus on ethnographic/neurological context.

**punishment_or_sanctions:**  
- **exact:** Multiple theory papers model explicit peer or institutional punishment with variable costs and efficacies (Jiao et al., 2020; Fang et al., 2020; Wang & Lv, 2019; Huang et al., 2018; Nakamaru et al., 2018).
- **close/adjacent:** Some focus on reward, exclusion, or reputation as functional analogues (e.g., information diffusion, bribery, or costless reputation mechanisms), or review punishment-related cultural mechanisms (Raihani & Power, 2021; Smith, 2020).
- **none:** Roughly one third of papers lack any punishment/sanction condition (e.g., studies focusing on baseline cooperation, neural traits, or partner selection).

**efficiency_or_related_payoff_outcome:**  
- **exact:** Several key theory papers directly report group efficiency or mean payoff (Jiao et al., 2020; Fang et al., 2020; Wang & Lv, 2019; Huang et al., 2018).
- **close/adjacent:** Many others infer payoff effects based on cooperative equilibria or report closely related outcomes (group success, welfare, surplus).
- **weak/none:** Many experimental studies do not report efficiency or group payoff as an explicit outcome, focusing on contribution or neural measures instead.

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes:**  
- *Efficiency*, *group payoff*, *mean (or total) earnings*, *welfare*, or *total coins*: The papers with the most precise guidance for prediction clearly report these (Jiao et al., 2020; Fang et al., 2020; Wang & Lv, 2019; Huang et al., 2018; Nakamaru et al., 2018).  
- Some report only *relational* or *equilibrium* payoffs, or the percentage of parameter space over which higher payoff is achieved.
- A few report *expected lifespan* (Kayser & Lampert, 2021) or public-good *achievement* as proxies for efficiency.

**Non-Payoff Behavioral Outcomes:**  
- *Contribution rate*, *cooperation rate*, *frequency of punishment or reward*, *strategy frequencies*, *norm compliance*, or *neural correlates* of prosociality dominate the majority of the experimental studies.
- Many theory papers also track strategy frequency or stability as opposed to explicit group payoff.

**Distinction:**  
- Many papers that only report contribution or punishment rates do *not* report on the net efficiency effect, and thus their behavioral findings must be interpreted with caution for efficiency prediction.

# 4) Main Findings Relevant To Prediction

**Empirical Findings:**
- Laboratory evidence (albeit limited for efficiency) suggests that *introducing punishment increases contribution rates* in PGGs, which typically correlates with higher efficiency unless punishment costs outweigh the gains (Micheli et al., 2021).
- There are *few direct empirical measurements of efficiency change* with punishment enabled. Most empirical work is on behavior rather than payoffs.

**Theoretical Findings (direct PGG with punishment):**
- *Enabling (peer or institutional) punishment increases efficiency* if punishment is not too costly, is effective, and is not easily subverted by bribery or corruption (Jiao et al., 2020; Fang et al., 2020; Wang & Lv, 2019; Huang et al., 2018; Nakamaru et al., 2018).
    - *Probabilistic punishment* (not punishing every time) can be more robust and cost-effective than always-on punishment when costs are high (Jiao et al., 2020).
    - *Shared cost* of punishment (spread across cooperators) permits sustainment of cooperation at lower individual burden (Wang & Lv, 2019).
- *Effectiveness of punishment depends on the size of fine vs. cost*: punishment must hurt defectors enough to alter incentives, but cannot be so costly to punishers that any efficiency gains are erased (Wang & Lv, 2019; Fang et al., 2020).
- *Punishment effectiveness can be undermined* by bribery, high costs, antisocial punishment, or poor alignment of individual and group incentives (Fang et al., 2020, Smith, 2020, Raihani & Power, 2021).

**Mixed/Moderating Findings:**
- *Game design parameters* such as group size, repetition, spatial structure, probability of punishment execution, performance incentives, and monitoring effectiveness are critical moderators of the effect of punishment on efficiency. If these are poorly chosen, punishment may have no effect or even be harmful.
- *Commitment and recognizability* matter: punishment is more likely to raise efficiency when participants can commit or reliably signal intent to punish (Akdeniz & van Veelen, 2021).

**Findings from Adjacent Contexts:**
- Mechanisms such as reward, exclusion, or information diffusion can functionally substitute for or moderate the effects of punishment, sometimes accelerating cooperation without explicit cost.
- Efficiency gains in related settings are often observed only when indirect costs (e.g., reputation, exclusion) are large enough to change behavior.
- Group size and repeated interaction are often positive moderators of efficiency gains, but only when conditional cooperation or punishment is feasible (Kurokawa, 2019; Shimura & Nakamaru, 2018).

# 5) Prediction Guidance

Based on this literature, the following points guide prediction of treatment efficiency (punishment enabled) given design dimensions and control efficiency:

- **Punishment is not always beneficial:** Net group efficiency increases if (and only if) the cost-to-impact ratio of punishment is moderate to low, punishment is effective at deterring defection, and side effects (e.g., bribery, antisocial punishment) are limited (Jiao et al., 2020; Fang et al., 2020; Wang & Lv, 2019; Huang et al., 2018; Greenwood et al., 2018).
- **Critical dimensions to attend to:**  
    - *Punishment cost* (`punishment_cost`), *punishment magnitude/effectiveness* (`punishment_tech`), and probability/mechanism of execution.
    - *Player count* and *number of rounds*: moderate group sizes, some repetition, and feasible monitoring increase likelihood of positive payoff impact.
    - *Institutional structure*: performance-based incentives or corruption control mechanisms can amplify the positive effect of punishment.
    - *Shared or distributed punishment cost* (punishment cost spread over cooperators) enhances the sustainability of high efficiency.
    - *Type of punishment* (probabilistic, exclusion, graduated): more sophisticated mechanisms often outperform naive, always-on peer punishment.
- **Control efficiency is informative:** If control efficiency is already near maximum (i.e., full cooperation is established without punishment), the marginal gain from adding punishment is limited and could even be negative due to added costs. If control efficiency is low (rampant defection), then well-designed punishment can appreciably improve efficiency—subject to the above moderators.
- **Cautions:** In environments with high punishment cost, ineffective punishment, prevalent antisocial punishment, or bribery/corruption, enabling punishment can *reduce* efficiency due to costs that outweigh any gains from increased cooperation (Fang et al., 2020; Raihani & Power, 2021; Smith, 2020).
- **Empirical calibration is sparse:** Most existing empirical data are on behavioral outcomes, so predicted efficiency gains (or losses) from enabling punishment, even when theoretically robust, should be treated as qualitative rather than quantitative unless strong direct evidence is available.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed:**  
- `player_count`, `num_rounds`, `mpcr`, `all_or_nothing`, `punishment_cost`, `punishment_tech`, `reward_exists` (less often), and, in select models, `punishment_exists` and `reward_cost`.
- Many theory papers sweep these parameters and show how they modulate the net efficiency effect of punishment.
- `shared_cost` designs (cost spread over cooperators) are analyzed in some papers.

**Indirectly informed/Contextually discussed:**  
- `chat`, `default_contrib`, `show_n_rounds`, `show_other_summaries`, `show_punishment_id` receive less direct attention; a few papers consider information disclosure (summaries or punishment/reward visibility), mostly in the context of reputation or monitoring.
- `reward_tech`, `reward_cost` and the simultaneous presence of rewards and punishments are discussed only in a small subset (Jiao et al., 2020).
- Probabilistic vs. deterministic punishment mechanisms and their optimization receive significant theoretical attention (Jiao et al., 2020; Couto et al., 2020).

**Effectively missing:**  
- Most studies do not control for or manipulate `chat` (communication), `default_contrib` (framing), and identity/show features such as `show_punishment_id`. These design features are largely unaddressed or present only contextually.
- Combined or interacting effects of reward and punishment, particularly in empirical settings, are sparse.

# 7) Important Limitations

- **Empirical scarcity for efficiency:** Most empirical studies focus on behavior (contribution/punishment rates) rather than direct measurements of group efficiency, leaving a gap in evidence for the exact outcome targeted in the prediction task.
- **Theory–experiment gap:** The strong, detailed predictions from theory are rarely directly tested with real-world group payoff data. Thus, quantitative use of theory-based formulas is justified primarily as relative/qualitative guidance.
- **Limited diversity in sanction mechanisms:** Most models assume simple, punitive treatments; less is known about complex, multi-level, or real-world institutional arrangements, or about games involving both rewards and punishments.
- **Contextual moderators are underexplored:** Features such as pre-play communication, information visibility, participant beliefs, and social/cultural context are rarely manipulated in tandem with punishment in PGGs.
- **Sparse evidence on negative/side effects:** While antisocial punishment, bribery/corruption, and reputational backlash are discussed as concerns, empirical data on their frequency and impact are minimal.
- **Prediction outside theory parameter space is risky:** Where design features fall outside the parameter ranges (or structures) theorized, prediction is less reliable.
- **Limited evidence for downstream interaction effects:** Few studies model or measure how multiple dimensions interact (e.g., how changing both group size and punishment visibility might jointly affect efficiency).

**Summary:**  
The literature robustly supports qualitative prediction that enabling peer punishment increases efficiency in PGGs under specific, theoretically defined conditions (moderate cost, effective punishment, limited corruption), with effects strongly moderated by several core design dimensions. However, empirical calibration for efficiency (not just behavior change) is sparse, and several prediction-relevant variables are only weakly addressed. Caution and attention to parameter-specific theory are warranted when extrapolating these findings to new game designs.
