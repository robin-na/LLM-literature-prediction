# 1) Evidence Base

The evidence base for this literature analysis consists entirely of theoretical and simulation/modeling papers (no empirical or laboratory experiments). The papers focus overwhelmingly on public goods games (PGGs), their variants, and adjacent N-person social dilemmas, with a secondary set addressing related games such as the Prisoner’s Dilemma or ultimatum game. Within these, a substantial subset model costly peer punishment (and sometimes reward), particularly in spatial or networked environments; others analyze alternative mechanisms or structural moderators of cooperation.  
A narrower set of papers directly address payoff-based outcomes—group efficiency or total payoff—as their primary outcome; a larger portion use cooperation or contribution rates, strategy abundances, or other behavioral measures, often without mapping these to efficiency or group payoff.  
The coverage of game design dimensions relevant to downstream prediction is moderate: most dimensions are directly modeled in at least some papers (player count, group size, rounds, MPCR, punishment cost/effect, etc.), but several (e.g., chat, contribution framing, display variables, identity revelation) are sparsely or not at all addressed.  
In summary: the paper set is broad in mechanisms and contexts for peer punishment in PGG-like games, but is narrow in empirical (experimental) coverage and strongest in theory/simulation, with sparse direct measurement of efficiency or group payoff outcomes.

# 2) Task Relevance

### pgg_or_variant
- **exact**: A core subset (e.g., Zhuang et al., 2012; Wang et al., 2010; Dejong et al., 2008; Sigmund et al., 2011; Perc & Szolnoki, 2012; Xia et al., 2011) model public goods games or direct variants.
- **close/adjacent**: Some analyze closely-related social dilemmas (common pool resources, voluntary PGGs, N-person games with varying contribution, ultimatum/prisoner’s dilemma with parallel punishment/reward logic).
- **none/weak**: Several papers are in adjacent game paradigms or focus on mechanisms not involving explicit PGGs.

### punishment_or_sanctions
- **exact**: Many papers explore peer punishment, pool/institutional punishment, punishment cost and magnitude, and sometimes second-order punishment (punishment of non-punishers).
- **close/adjacent**: Some papers investigate reward only, social control mechanisms distinct from standard costly punishment, or indirect punishment (network restructuring, contribution withdrawal).
- **none**: Papers focusing solely on baseline (no punishment) PGGs or with different mechanisms lack sanctions interventions.

### efficiency_or_related_payoff_outcome
- **exact**: Only a subset (e.g., Zhuang et al., 2012; Wang et al., 2010; Sigmund et al., 2011; Dejong et al., 2008; Szolnoki & Perc, 2012; Noailly et al., 2009) directly model efficiency or group payoff as a primary outcome.
- **close/adjacent**: Many report only on cooperation rates, strategy abundances, or behavioral outcomes, with efficiency as an interpretive or inferred result.
- **none**: Several papers do not report, analyze, or infer efficiency/payoff at all, making them only contextually relevant for the prediction task.

# 3) Outcomes Measured In The Literature

- **Payoff-based outcomes** (`efficiency`, group payoff, welfare, total earnings): Directly measured in a core set of theoretical/simulation papers, often as mean or aggregate payoff relative to the social optimum (e.g., Zhuang et al., 2012; Dejong et al., 2008; Sigmund et al., 2011; Noailly et al., 2009; Szolnoki & Perc, 2012).
- **Behavioral outcomes** (contribution/cooperation rate, strategy frequency, norm compliance, punishment frequency): Predominant in the broader paper set; many papers infer potential efficiency effects from increases in cooperation rather than directly reporting payoffs (e.g., Perc & Szolnoki, 2012; Gao et al., 2012; Wang et al., 2011).
- **Mechanistic arguments**: Some provide only conceptual models or phase diagrams, positing that higher cooperation should increase efficiency (without quantifying it).
- **Limited/No payoff reporting**: Many adjacent or weakly relevant papers do not quantify or discuss efficiency at all.

# 4) Main Findings Relevant To Prediction

Synthesizing across the directly relevant theoretical/simulation literature:

- **Enabling costly punishment mechanisms in PGGs robustly increases group efficiency (mean payoff) compared to the no-punishment baseline, especially when baseline efficiency is low (high defection)** (Wang et al., 2010; Dejong et al., 2008; Zhuang et al., 2012; Sigmund et al., 2011).
- **The magnitude of efficiency increase depends on punishment cost, effectiveness (fine), and game structure (player count, MPCR, rounds, spatial/networked structure)** (Wang et al., 2010; Sigmund et al., 2011; Noailly et al., 2009; Perc & Szolnoki, 2012).
- **Punishment is more effective at increasing efficiency when (a) participation is voluntary, (b) punishment is adaptive or context-sensitive, and (c) spatial or community structure allows punishment and cooperation to cluster** (Perc & Szolnoki, 2012; Xia et al., 2011; Noailly et al., 2009).
- **Reward mechanisms can also increase efficiency, but are typically less effective or more costly compared to punishment for the same parameterization** (Zhuang et al., 2012; Forsyth & Hauert, 2011).
- **If punishment is too costly relative to its impact, or poorly targeted, group efficiency gains may be limited or negative** (Sigmund et al., 2011; Isakov & Rand, 2012).
- **Complexity of punishment mechanism matters: peer punishment is less stable than pool/institutional punishment with second-order sanctions; metanorms can further improve cooperation and, by inference, efficiency** (Sigmund et al., 2011; Prietula & Conway, 2009).
- **Some adjacent literature cautions that in highly asymmetric, coercive, or non-standard PGGs, punishment can sometimes lower efficiency (e.g., by reducing payoffs through excessive punishment)** (Isakov & Rand, 2012), but such effects are not the norm in symmetric PGGs.

# 5) Prediction Guidance

**How should this literature inform prediction of treatment efficiency from design dimensions and control efficiency?**

- **Default expectation**: Enabling peer punishment in a PGG or close variant will increase average efficiency relative to the same game with punishment disabled, especially if the control game is inefficient due to free-riding.
- **Magnitude of effect**: The efficiency boost is typically larger when:
    - The MPCR is low (high need for intervention)
    - Groups are not too large (dilution of punishment power can occur at high player counts)
    - Punishment cost is modest relative to the fine/impact
    - Punishment is adaptive/context-sensitive as opposed to steady
    - Games are repeated over multiple rounds
    - Voluntary participation is possible
    - Network/spatial structure enables local enforcement and clustering of cooperation/punishment
- **Bounding expectations**: If control efficiency is already high (near-optimal cooperation), punishment effects on efficiency may be minimal or even slightly negative (due to efficiency lost through punishment costs).  
- **Special cases**: Where the game structure is coercive/asymmetric (e.g., king–subject models, Isakov & Rand, 2012), enabling punishment may increase compliance but lower overall efficiency.
- **Parameter sensitivity**: Extreme punishment costs, weak punishment (low fine), or enabling only non-costly social control (e.g., smileys or network breaking without payoff cost) do not map well to the classic positive effect on efficiency seen with costly punishment.
- **Reward mechanisms**: If both reward and punishment are present, reward may yield equal or higher efficiency for the same total intervention cost, but this is secondary to the core prediction task (Zhuang et al., 2012; Forsyth & Hauert, 2011).
- **Limitations**: Magnitude of predicted change is most defensible in parameter regimes closely modeled in the theory papers. Caution is warranted in transferring effects between spatial and well-mixed games, institutional/pool versus peer punishment, or where key implementation details (e.g., identity revelation, information displays) are not specified in the source literature.

# 6) Design Dimensions Highlighted Across Papers

- **Directly informed** (core empirical/theoretical input):
    - `player_count` (all core papers)
    - `num_rounds` (widely modeled; sometimes infinite-horizon or repeated)
    - `all_or_nothing` (common; some continuous versions)
    - `mpcr`/synergy factor (all PGG models)
    - `punishment_cost`, `punishment_tech` (core; models vary cost and effectiveness)
    - `reward_exists`, `reward_cost`, `reward_tech` (studied in comparison or as secondary case)
- **Indirectly informed**:
    - `punishment_exists` (always modeled as binary treatment variable)
    - `show_other_summaries`, `show_n_rounds` (occasionally modeled through information structure, but rarely varied systematically)
    - `show_punishment_id` (not directly addressed; some mention of anonymity, but little formal modeling)
    - `default_contrib` (framing or endowment rarely explicitly modeled)
    - `chat` (very little, but some adjacent papers include social control or communication as a mechanism)
- **Only contextually discussed or missing**:
    - `chat`, `show_punishment_id`, `default_contrib`, and fine details of display variables
    - Information visibility not varied systematically or linked to efficiency outcomes
    - `reward` dimensions are secondary in punishment-focused prediction
- **Dimension impact interpretation**:
    - Evidence is strongest for effects of `punishment_cost`, `mpcr`, `player_count`, `num_rounds`, and spatial/structural variables on the efficiency gain from punishment.
    - Indirect or absent for framing variables, chat/communication, and display/feedback dimensions.
    - Where evidence is based on behavioral rather than payoff outcomes, this is primarily for network structure/media, voluntary participation, and indirect social control (need cautious transfer to efficiency predictions).

# 7) Important Limitations

- **Empirical absence**: All papers are theoretical or simulation-based; no laboratory or field experiments are included. Real-world behavioral noise and complexities may not be captured.
- **Efficiency/outcome reporting**: Many papers use behavioral/cooperation rates as proxies for efficiency, but not all directly translate behavioral shifts into quantified efficiency or payoff outcomes.
- **Parameter transferability**: Results are strongest within the modeled parameter spaces (e.g., certain player counts, MPCR, punishment costs), and transfer to out-of-sample dimensions (such as new chat/communication conditions, alternative information displays, or unfamiliar cost structures) is uncertain.
- **Sparse attention to contextual dimensions**: Treatment of `chat`, `default_contrib`, and display dimensions is minimal or absent, so predictions for these are largely unsupported.
- **Special cases and ambiguities**: Some models (Isakov & Rand, 2012) find that institutional or coercive punishment in asymmetric games can reduce efficiency, and there is disagreement on the effect size where costs of punishment are very high or the design is non-standard.
- **Focus on cooperation mechanisms**: Many adjacent papers provide insights into how cooperation can be sustained, but do not explicitly model or quantify its effect on group efficiency.
- **Over-reliance on simulation**: As all results derive from simulations or theoretical analysis, the magnitude and robustness of the predicted efficiency gains should be interpreted with caution for real-world applications or novel game dimension combinations.

---

**Summary:**  
The literature provides strong theoretical and simulation evidence that enabling peer punishment in public goods games increases average efficiency, especially when the baseline (control) efficiency is low. Core moderating dimensions such as player count, rounds, MPCR, punishment cost, and effectiveness are well-studied and should inform predictive models. Efficiency gains are expected to be higher in moderate-size, repeated games with reasonably effective and not overly costly punishment, and where the social structure supports local enforcement. Prediction in unexplored parameter regimes or regarding dimensions such as communication and display should be cautious, as direct evidence is sparse or absent.
