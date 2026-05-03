# 1) Evidence Base

The paper set reviewed comprises 28 articles, predominantly theoretical models with some simulation-based results, and a minority of empirical (experimental) studies. Most papers focus on evolutionary game theory or mechanism design, with a narrow emphasis on cooperation, punishment, and efficiency in repeated social dilemma settings. Direct empirical evidence on public goods games (PGGs) with and without punishment is limited; most evidence is theoretical or drawn from adjacent game types (e.g., spatial PD, stag hunt). Several papers address design dimensions (e.g., punishment cost, group size, MPCR), but coverage of the full set of 14 prediction dimensions is uneven. Overall, the literature is conceptually rich but empirically sparse for the specific downstream prediction task.

# 2) Task Relevance

**PGG or Variant**:  
- *exact*: A small subset of papers directly model the PGG or voluntary PGG (e.g., Wu et al., Zhang et al.), providing the most relevant, directly transferable findings.
- *close*: Some papers use resource sharing or coordination games that bear strong structural similarity to PGGs (e.g., Becchetti et al., Liu & Riyanto, Mariano & Correia).
- *adjacent/weak*: Most of the remaining works use pairwise social dilemmas (Prisoner’s Dilemma, Snowdrift, Master–Worker), spatial/layered games, or discuss general cooperation theory—valuable for mechanism insight but not direct predictors.

**Punishment or Sanctions**:
- *exact*: About half the theoretical models explicitly feature punishment (as implemented in PGGs or similar games), and some study both its cost and mode of delivery.
- *close/adjacent*: A minority analyze functionally similar mechanisms (exclusion, stress, internalized costs) or focus on reward, information, or monitoring rather than punishment per se.
- *none/weak*: Several do not include punishment or sanctions; these are irrelevant for the treatment–control efficiency contrast needed for prediction.

**Efficiency or Related Payoff Outcome**:
- *exact*: About six papers provide direct analysis of group efficiency or average payoff, with or without punishment (e.g., Wu et al., Luo & Zhao, Mariano & Correia, Zhang et al.).
- *adjacent/weak*: The majority report only cooperation/contribution rates or discuss efficiency mechanistically without data or models to support quantitative inference.
- *none*: Roughly a third report purely behavioral dynamics (e.g., frequency of cooperators, network structure impact) with no efficiency or total payoff outcomes.

*Summary*: The most relevant evidence for the prediction task comes from a narrow subset of theory papers modeling PGGs with explicit punishment and group efficiency as a primary outcome. Empirical evidence is lacking; most literature is indirect.

# 3) Outcomes Measured In The Literature

- **Payoff-based Outcomes (Relevant to Efficiency):**
    - *Direct*: Average group payoff/efficiency (Wu et al., Luo & Zhao, McBride et al., Zhang et al., Mariano & Correia, Nasrallah & Cheaib, Inaba et al., Garay et al., Ghachem, Becchetti et al.)
    - *Indirect/Implied*: Analyses where higher cooperation rates logically increase total group welfare, though not explicitly measured.
- **Non-payoff (Behavioral) Outcomes:**
    - Frequency or rate of cooperative choices, norm compliance, punishment behavior, and strategy convergence (very common across the set).
    - Network effects, information transmission, or cluster size effects on emergent cooperation (numerous theoretical studies).
    - Mechanistic or conceptual analyses of reciprocity, retaliation, peer identification, or emotional mechanisms.
    - Note: Many studies with non-payoff outcomes explicitly do *not* provide information about efficiency, and this distinction is clear in the reviewed digests.

# 4) Main Findings Relevant To Prediction

- **Enabling punishment in PGGs or their closest analogs** generally increases average group efficiency, particularly when punishment is not excessively costly and is effectively targeted (Wu et al., Luo & Zhao, Mariano & Correia, Nasrallah & Cheaib). Full cooperation (and thus maximum efficiency) is more likely when:
    - Punishment cost is low (Wu et al.; Luo & Zhao).
    - Punishment is universal and not subject to elite exemption or partial coverage (Nasrallah & Cheaib).
    - MPCR is low or temptation to defect is high—punishment has its greatest impact in low baseline efficiency environments (Wu et al.).
    - Social or network structure limits precise targeting of low-connected players, thereby sustaining cooperation (Larson).
- **The effect of punishment is highly sensitive to parameterization**:
    - Overly severe or frequent punishment, high punishment cost, or excessive risk of retaliation/retaliatory cost can undermine efficiency or nullify gains (McBride et al.).
    - In some adjacent models, the presence of “informants”—those who both defect and punish—is critical for punishment to improve efficiency (McBride et al.).
    - Internalized costs for defection (moral emotions, stress) or exclusion mechanisms can substitute for external punishment in supporting efficiency, provided the cost is sufficiently high (Zhang et al.; Inaba et al.).
- **Information conditions moderate punishment’s effect**: When network knowledge or feedback is limited or imperfect, punishment is more robust in maintaining high efficiency (Larson; Inaba et al.; Ghachem).
- **Public monitoring alone may negatively impact efficiency** if punishment is not available, as individuals match average (low-cooperation) behavior (Becchetti et al.).
- **Reward mechanisms can be complementary or substitutive** to punishment, but their independent impact on payoffs/efficiency is underexplored in this set.
- **Substantial ambiguities and disagreement** remain in adjacent (non-PGG) literature regarding the impact of strategy complexity, memory, error, and group size.

# 5) Prediction Guidance

The main actionable insights for downstream prediction are:
- In environments matching the PGG with peer punishment, if the control (no punishment) efficiency is low (e.g., low MPCR), enabling punishment is likely to produce a substantial efficiency increase, especially if punishment is not overly costly (Wu et al.; Luo & Zhao).
- The positive effect of punishment is strong when:
    - Punishment cost is moderate or low.
    - All or most players are subject to punishment (no exempt subgroups).
    - There is either moderately limited information about others’ choices/networks or universal observability of bad acts, but not highly noisy or high-error information (Larson; Inaba et al.; Ghachem).
- If design features make punishment highly costly or prone to post-punishment retaliation, the expected effect on efficiency is reduced and may be negative (McBride et al.).
- When some form of internal sanction or exclusion operates, similar efficiency benefits as with external punishment are likely, provided observability is reliable and error is not excessive (Zhang et al.; Inaba et al.).
- For design dimensions where evidence is indirect (e.g., chat, all-or-nothing framing, default contribution, or identity revelation), caution is warranted; the literature suggests potential moderation but offers no direct efficiency findings.
- Empirical calibration (i.e., predicting treatment efficiency from control efficiency plus design dimensions) is only partially supported; most findings are qualitative or theoretical, not empirical regressions or effect size estimates.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**
- `player_count`: Extensively modeled, with findings that increased group size can both raise or lower the threshold for punishment to improve efficiency, depending on game parameters (Wu et al.; Zhang et al.; Luo & Zhao; McBride et al.).
- `num_rounds`: Modeled in theory work; longer games generally strengthen the effect of punishment on sustaining cooperation (Wu et al.; Qu et al.; Huang & Inohara).
- `mpcr`: Central in many theoretical models (Wu et al.; Zhang et al.; Inaba et al.), with low MPCR especially benefiting from added punishment.
- `punishment_cost`: Universally modeled in theory work; lower cost enhances the positive efficiency effect but must remain non-trivial to deter exploitation (Wu et al.; Mariano & Correia; Luo & Zhao).
- `punishment_tech` (technology/effectiveness): Discussed in varying levels of detail (McBride et al.; Mariano & Correia; Nasrallah & Cheaib; Larson).

**Indirectly Informed:**
- `all_or_nothing`: Common game structure in models, but effects on efficiency generally inferred via mechanism not direct comparison.
- `show_n_rounds`, `show_other_summaries`: Some coverage in PGG-like games or adjacent settings; effects are more behavioral than payoff-based.
- `reward_exists`, `reward_cost`, `reward_tech`: Addressed as alternatives or complements to punishment (Mariano & Correia; Christoforou et al.; Garay et al.); efficiency impact unclear due to lack of direct data.

**Contextually Discussed:**
- `chat`: A few papers mention communication or gossip structures (Larson; Golman), usually as moderators of punishment behavior rather than as direct inputs to efficiency.
- `default_contrib`: Little explicit discussion; framing of endowment/contribution rarely isolated as a variable.
- `show_punishment_id`: Identity revelation is sometimes discussed (Larson, McBride et al.) but efficiency outcomes are rarely modeled as a function of this variable.

**Effectively Missing:**
- Direct empirical evidence or parameterized models informing the incremental efficiency gain attributable to: `chat`, `default_contrib`, `show_punishment_id`, or interaction effects among multiple design features.

# 7) Important Limitations

- **Empirical basis is weak**: Most evidence is theoretical, with few direct experimental or field measurements of efficiency changes when punishment is enabled in PGGs with controlled design variation.
- **Over-reliance on behavioral proxies**: Many papers substitute cooperation rates or punishment frequency for explicit group efficiency, which can misrepresent payoff-based results, especially when punishment is costly.
- **Parameter and context sensitivity**: Predicted efficiency impacts of punishment depend critically on cost structures, social network information (precision or error), and strategy availability, none of which are measured consistently or empirically across the paper set.
- **Sparse coverage of key design features**: Most design dimensions beyond group size, rounds, and punishment cost or effectiveness are only thinly supported.
- **Generality from adjacent settings is uncertain**: Extrapolating findings from spatial PDGs, resource sharing, or exclusion games to PGGs with peer punishment is not always justified, especially where payoff structures differ.
- **Missing treatment–control mapping**: The literature rarely provides direct comparisons between the same game design with and without punishment, making quantitative prediction (from control efficiency to treatment efficiency) imprecise.

**Summary:** While the literature provides clear direction that enabling peer punishment in PGG-like settings *can* increase group efficiency—particularly under low baseline efficiency and moderate punishment cost—this is mainly a theoretical result, with high context and parameter sensitivity, limited empirical calibration, and numerous holes in coverage for specific design dimension effects. Predictions of treatment efficiency from control efficiency using these sources should be made cautiously and recognize substantial uncertainty, particularly outside the core punishment/cost/MPCR settings.
