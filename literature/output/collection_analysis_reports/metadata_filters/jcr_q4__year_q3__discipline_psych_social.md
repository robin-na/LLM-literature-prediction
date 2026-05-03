# 1) Evidence Base

This paper set is relatively broad in coverage, containing 19 papers with a mixture of empirical (mostly laboratory experiments) and theoretical studies. There is a substantial subset of exact and close relevance empirical papers directly measuring efficiency or closely related payoff outcomes in public-goods games (PGGs) with and without punishment enabled. Several theory papers offer mechanistic and equilibrium analyses, often with explicit focus on efficiency implications. However, a minority of papers address adjacent or weakly related game structures (e.g., generalized exchange, common-pool resource, Stag Hunt, Prisoner’s Dilemma, or networked evolutionary games). The theoretical contributions generally discuss mechanisms (e.g., power asymmetry, coalition formation, mechanism design) but sometimes lack direct mapping to standard PGGs. Overall, the evidence base allows for cross-context synthesis, but the strongest support concerns standard linear PGGs with peer or centralized punishment.

# 2) Task Relevance

**pgg_or_variant**:  
- **exact**: Substantial empirical and theoretical evidence comes from standard PGGs (Suleiman & Samid, 2021; Castillo et al., 2021; Botta et al., 2021; Kanitsar, 2021; Windmann et al., 2021).  
- **close**: Some papers use variants such as generalized exchange, threshold or optional PGGs, or related social dilemmas (Eldakar et al., 2018; Bolle, 2021; Di Guida et al., 2021).  
- **adjacent/weak**: Others focus on CPR games, networked dilemmas, or volunteer’s dilemma (Przepiorka & Diekmann, 2020; Madeo & Mocenni, 2021; Friehe & Tabbach, 2018).

**punishment_or_sanctions**:  
- **exact**: Many studies directly manipulate the presence of peer or institutional punishment (Suleiman & Samid, 2021; Castillo et al., 2021; Botta et al., 2021; Kanitsar, 2021).  
- **close/adjacent**: Some examine related mechanisms—exclusion, redistribution, social feedback, voluntary cooperation, or reward (Grund et al., 2020; Becchetti et al., 2018; Przepiorka & Diekmann, 2020).

**efficiency_or_related_payoff_outcome**:  
- **exact/close**: Several exact or close studies report group efficiency or total payoff, the key outcome for prediction (Suleiman & Samid, 2021; Castillo et al., 2021; Botta et al., 2021; Kanitsar, 2021; Nax et al., 2018).  
- **adjacent/weak**: Others report only contribution rates, cooperation rates, or binary success (Selterman, 2019; Windmann et al., 2021; Becchetti et al., 2018).

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes** (efficiency, group earnings, total payoff, welfare) are directly reported in several empirical and theory papers (Suleiman & Samid, 2021; Castillo et al., 2021; Botta et al., 2021; Kanitsar, 2021; Nax et al., 2018; Di Guida et al., 2021; Skarzhinskaya & Tsurikov, 2021; Friehe & Tabbach, 2018).
- **Non-payoff behavioral outcomes** (contribution rate, cooperation rate, punishment frequency) are the focus in some papers, and their relation to payoff outcomes is often discussed but not always quantified (Grund et al., 2020; Becchetti et al., 2018; Windmann et al., 2021; Selterman, 2019).
- Some studies, notably Windmann et al. (2021) and Grund et al. (2020), report only behavioral indicators and not efficiency or payoff.
- Theory and review papers frequently discuss mechanisms or conditions for cooperation, with only some providing analytic results on group welfare or efficiency (Eldakar et al., 2018; Botta et al., 2021; Friehe & Tabbach, 2018; Andersson, 2020).

# 4) Main Findings Relevant To Prediction

**Consensus/Thematic Findings:**
- **Punishment generally increases efficiency**: Multiple experimental and theory papers in standard PGGs find that enabling peer or centralized punishment increases group earnings and efficiency compared to punishment-disabled controls (Suleiman & Samid, 2021; Castillo et al., 2021; Botta et al., 2021; Kanitsar, 2021 [for costless punishment]).
- **Magnitude of efficiency gain varies**: Efficiency improvements with punishment are moderate and highly variable, often depending on group composition (fraction of strong reciprocators), structural context (e.g., dense/sparse sanction networks), and punishment cost (Suleiman & Samid, 2021; Kanitsar, 2021; Eldakar et al., 2018).
- **Effect is context-dependent**: In generalized exchange or sparse sanctioning structures, or when punishment is costly, efficiency gains may vanish (Kanitsar, 2021; Eldakar et al., 2018).
- **Antisocial punishment is rare but efficiency can be reduced by 'norm-keepers'** (those who punish indiscriminately) rather than free riders (Suleiman & Samid, 2021).
- **Institutional design details** such as who enforces punishment (peer vs. manager), punishment effectiveness, and the possibility of exclusion or replacement, can moderate (but sometimes negligibly) the efficiency impact (Castillo et al., 2021; Grund et al., 2020).

**Empirical vs. Theory:**
- **Empirical findings** robustly show positive but variable efficiency effects of enabling punishment, provided design features don’t undermine the mechanism (e.g., high cost, network sparsity).
- **Theory** supports these findings, showing that punishment can stabilize cooperation/efficiency but gains are maximized when punishment is altruistic and power is symmetric; in adverse settings, efficiency gains are limited (Botta et al., 2021; Eldakar et al., 2018; Bolle, 2021; Friehe & Tabbach, 2018).

**Non-payoff findings** (e.g., cooperation rate) often suggest similar directions, but cannot reliably be mapped to efficiency outcomes due to diminishing returns, punishment costs, or strategic play.

# 5) Prediction Guidance

For the downstream prediction task (predicting treatment efficiency under punishment given design and control efficiency):

- **Prediction direction**: Enabling punishment in standard PGG designs (with reasonable cost and peer or institutional implementation) should be predicted to increase efficiency relative to the control, but the magnitude is moderated by details of network structure, punishment cost/effectiveness, and social composition (Suleiman & Samid, 2021; Botta et al., 2021; Castillo et al., 2021; Kanitsar, 2021).
- **Magnitude bounds**: While positive, the efficiency gain is variable and may be minor (or absent) when punishment is costly, when sanction networks are sparse or asymmetric, or when 'norm-keepers' dominate (Suleiman & Samid, 2021; Kanitsar, 2021; Eldakar et al., 2018).
- **Dimension dependence**: Models and experiments show that MPCR, player count, punishment cost, and, in optional-PGGs, loner options or effectiveness thresholds, play critical roles in moderating punishment impact (Botta et al., 2021; Eldakar et al., 2018; Kanitsar, 2021).
- **Control efficiency as reference**: Papers with two-phase designs (with/without punishment) show that treatment efficiency is typically higher than control, with control efficiency setting a realistic lower bound for prediction (Suleiman & Samid, 2021; Castillo et al., 2021).
- **Modifiers to consider**:
  - **If punishment cost is low and applied selectively, efficiency gains are likely larger** (Kanitsar, 2021; Botta et al., 2021).
  - **If the network is non-standard or sanctioning is restricted, treatment gains may be minimal or absent** (Kanitsar, 2021; Bolle, 2021).
  - **Cultural/contextual variability**: Social composition (e.g., fraction of strong reciprocators) modulates outcomes; such variations are difficult to encode from design dimensions alone but are highlighted in Suleiman & Samid (2021).
- **Structural caveats**: These findings are primarily about linear PGGs with clear punishment mechanisms; extrapolation to threshold, networked, or CPR settings should be cautious and evidence-limited.

# 6) Design Dimensions Highlighted Across Papers

- **Directly informed dimensions**:  
  - `player_count`, `num_rounds`, `mpcr`, `all_or_nothing`, `punishment_cost`, `punishment_tech`: Frequently varied and analyzed with respect to efficiency effects (Suleiman & Samid, 2021; Castillo et al., 2021; Kanitsar, 2021; Botta et al., 2021).
  - `punishmentExists` (control/treatment switching): Central to many empirical designs.
- **Indirectly informed/contextually discussed**:
  - `chat`: Sometimes present but rarely directly analyzed for efficiency impact (Nax et al., 2018; Grund et al., 2020).
  - `show_n_rounds`, `show_other_summaries`: Noted in some experiment protocols or social feedback studies (Przepiorka & Diekmann, 2020), but not systematically manipulated to evaluate efficiency change with punishment.
  - `punishment_tech`: Sometimes discussed as peer vs. centralized (Castillo et al., 2021), or action- vs. outcome-based (Friehe & Tabbach, 2018).
- **Minimally or not informed**:
  - `default_contrib`, `reward_exists`, `reward_cost`, `reward_tech`, `show_punishment_id`: Only contextually discussed or included in some protocols, but not the focus for punishment-treatment efficiency effects.
- **Not addressed**: No direct evidence on the impacts of `reward_cost`, `reward_tech`, or `show_punishment_id` on efficiency change with peer punishment.

# 7) Important Limitations

- **Generalizability**: Most robust evidence is for standard linear PGGs; predictions for threshold PGGs, CPR games, or networked dilemmas are only weakly or indirectly supported.
- **Design dimension coverage**: Several prediction dimensions (e.g., `default_contrib`, reward dimensions, visibility of punisher identity) are not independently manipulated or tightly analyzed with respect to efficiency in this set.
- **Efficiency mapping**: Where only contribution rates or cooperation are reported, caution is required in inferring efficiency. Punishment can increase contributions but, due to its costs, may not always improve net efficiency.
- **Heterogeneity and context**: Efficiency effects due to punishment are highly heterogeneous and can be group- or context-specific (e.g., societal norms, 'norm-keepers' frequency), which are not directly codified in the design dimensions.
- **Mechanism specificity**: Peer vs. centralized punishment, action- versus outcome-based punishment, and the presence/absence of loner options or exclusion yield different efficiency impacts, sometimes in opposite directions.
- **Few quantitative mappings**: Papers provide effect directions and qualitative magnitude bounds, but rarely sufficient quantitative data for precise outcome prediction from dimension values.
- **Non-PGG settings**: Several papers focus on adjacent or related environments (CPR, volunteer’s dilemma, social feedback without formal punishment) limiting transferability.
- **Sequential effects**: Some designs rely on phase sequence (control then punishment); path-dependence and learning effects may confound isolate treatment effects.
- **Reporting gaps**: A minority of studies directly report group efficiency; many only infer from other behavioral outcomes, which may misstate true welfare changes.

---

**In summary:**  
The literature strongly supports the prediction that enabling punishment generally increases efficiency in standard PGG environments compared to controls, with the size of this effect moderated by punishment cost, network structure, and, to some degree, group composition. Many key design dimensions are well covered, especially `player_count`, `mpcr`, `punishment_cost`, and the punishment implementation type. However, there is considerable heterogeneity in empirically observed magnitudes, and some prediction dimensions lack direct evidence. Extrapolating to non-standard or weakly related games (such as threshold PGGs or CPRs) should be done cautiously, and predictions should account for identified moderators when possible.
