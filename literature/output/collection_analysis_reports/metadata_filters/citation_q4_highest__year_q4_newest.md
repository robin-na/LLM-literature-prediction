# 1) Evidence Base

The supplied literature set is primarily theoretical, with a minority of empirical (notably experimental) studies, and includes several high-level reviews and conceptual papers. Out of 12 papers, only one is an explicit experimental lab study focused on social-dilemma dynamics without sanctions (Bicchieri et al., 2022). The rest are theoretical models, agent-based simulations, or broad conceptual reviews. A substantial fraction of the theory papers use spatially structured population models, which may deviate from standard, well-mixed public goods game (PGG) lab designs.

Most papers focus on the mechanisms promoting cooperation (punishment, rewards, reputation, norms, memory, noise, learning) in collective action problems. However, only a small subset directly reports efficiency or group payoff outcomes in PGGs with or without punishment. The coverage of specific game design dimensions relevant to downstream prediction is heterogeneous: some dimensions (e.g., player count, punishment cost) are modeled in detail in a few theory papers, but several prediction-relevant dimensions (such as chat, default contribution, or information display) are sparsely addressed or entirely absent.

Overall, the base is relatively narrow for the specific prediction task of estimating the impact of peer punishment on efficiency, as there is a stronger focus on conceptual mechanisms, non-payoff behavioral outcomes (like cooperation rates), and adjacent game types (like the prisoner's dilemma or norm compliance tasks).

# 2) Task Relevance

**PGG or Variant**:  
- **exact**: Theory papers by Lee et al. (2022), Lv & Song (2022), Hua & Liu (2024), and Wang et al. (2023) model PGGs or very close structural variants.
- **close–adjacent**: Reviews and historical/sociological analyses (Van Lange & Rand, 2022; Boyd & Richerson, 2022; Traulsen & Glynatsi, 2023; etc.) discuss public goods games or related social dilemmas but often broaden to other collective action or norm-driven contexts.
- **adjacent**: Several studies use structurally similar games (prisoner's dilemma) or generic social dilemma/norm compliance tasks (Gou & Li, 2023; Bicchieri et al., 2022; Wang et al., 2022).

**Punishment or Sanctions**:  
- **exact**: Explicit peer or institutional punishment and its cost/effect is the primary theoretical focus in Lee et al. (2022) and Lv & Song (2022) (though the latter focuses on cooperation rate), as well as Wang et al. (2023) for institutional punishment.
- **adjacent**: Many broader reviews and context papers discuss punishment, sanctions, or indirect analogues (gossip, ostracism, etc.), but few offer direct model or data links to PGG payoff outcomes.
- **none**: Several papers focus on reward only (Hua & Liu, 2024) or have no explicit punishment or sanctions component (Bicchieri et al., 2022; Wang et al., 2022).

**Efficiency or Related Payoff Outcome**:  
- **exact**: Lee et al. (2022) and Hua & Liu (2024) model efficiency and total group payoff as explicit outcomes.
- **close**: Wang et al. (2023) studies cumulative cost to achieve cooperation, which serves as a proxy for institutional efficiency; others discuss payoff in general or adjacent terms.
- **adjacent–none**: Most other studies focus on cooperation rate, norm compliance, punishment rate, or theoretical mechanisms, without direct group efficiency reporting.

**Summary:**  
Only a few theory papers are highly relevant across all three dimensions (pgg=exact, punishment=exact, efficiency=exact or close), especially Lee et al. (2022). Most of the literature provides only adjacent or contextual evidence for the specific task of predicting the effect of punishment on efficiency in public goods games.

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes** (efficiency, group payoff, welfare, total coins, etc.):  
- Directly modeled or reported in Lee et al. (2022), Hua & Liu (2024), and Wang et al. (2023) (institutional cost as a proxy).
- Other papers only mention or contextualize group payoff or efficiency, without quantitative or experimental data.

**Non-Payoff Behavioral Outcomes** (contribution/cooperation rate, punishment frequency, norm compliance, etc.):  
- Focus of Lv & Song (2022), Gou & Li (2023), Bicchieri et al. (2022), and several theoretical reviews.
- Mechanistic or psychological interpretations (norm strength, reputation, memory effects, social proximity) in reviews and context papers.
- Some studies suggest mechanisms by which these behavioral outcomes might translate into payoff changes but do not empirically or mathematically test this link.

**Distinction Maintained:**  
Where efficiency outcomes are not reported, studies often note that findings pertain only to the evolution of cooperation or norm compliance and not to group efficiency or surplus.

# 4) Main Findings Relevant To Prediction

- **Punishment Can Increase Efficiency, But Not Universally:**  
  Lee et al. (2022) theoretically demonstrate that the introduction of peer punishment in a spatial PGG can increase group efficiency, especially when punishment costs are moderate and fines are high. There exists an optimal punishment cost maximizing payoff, and punitive interventions can backfire if implemented with unfavorable parameter values.
  
- **Parameter Sensitivity/Interaction Effects:**  
  The efficiency benefits of punishment are highly sensitive to punishment cost, fine magnitude, tax (where present), player count, and marginal per-capita return (MPCR) (Lee et al., 2022). Theoretical work suggests the importance of tuning these parameters; overly cheap or expensive punishment can reduce overall efficiency.
  
- **Institutional Versus Peer Punishment:**  
  Wang et al. (2023) extend the analysis to institutional punishment, finding that the cost-effectiveness of punishment (relative to reward) depends on initial cooperation level and network structure, with high-cooperation contexts benefiting more from punishment.

- **Behavioral Outcomes Do Not Guarantee Payoff Gains:**  
  Multiple papers (Lv & Song, 2022; reviews) show that punishment increases cooperation rates under many circumstances, but do not always measure group payoff—especially when punishment is costly, leading to higher cooperation but potentially lower efficiency.

- **Alternative Mechanisms (Gossip, Reputation, Social Proximity):**  
  Reviews (Van Lange & Rand, 2022; Bicchieri et al., 2022) highlight that gossip and social proximity can act as low-cost substitutes for punishment. Mechanisms making cooperation observable (showing contributions or punishment identities) also promote cooperation.

- **Structured Populations/Networks Matter:**  
  Most models explore spatial or network-structured games, which have different dynamics from standard, well-mixed lab PGGs, e.g., cluster formation and cyclic dominance can be relevant for predicting the effects of punishment.

- **Reward-Based or Other Interventions:**  
  Reward (rather than punishment) is explicitly addressed in Hua & Liu (2024), showing that well-calibrated rewards can also produce high or even optimal efficiency, but this does not inform punishment effects directly.

# 5) Prediction Guidance

**For prediction of treatment efficiency from design dimensions plus control efficiency:**

- **Direct Predictive Evidence:**  
  Theoretical analyses by Lee et al. (2022) provide phase diagrams mapping out when enabling punishment increases efficiency over the no-punishment (control) baseline. The key is parameterization: efficiency increases are most likely when:
    - Punishment cost is moderate (not too low or too high).
    - The fine imposed is large enough to deter defectors.
    - Structured populations (spatial, networked) may facilitate the positive effect.

  This implies that, *if the control efficiency is moderate and punishment is neither too cheap nor too expensive (relative to MPCR), enabling peer punishment is likely to improve efficiency, up to a point*. Overly expensive punishment, or insufficient fine magnitude, may reduce both payoff and cooperation.

- **Indirect/Mechanistic Insights:**  
  Where direct payoff data is lacking (e.g., behavioral-only studies), an increase in cooperation rate with punishment can be expected, but efficiency gains may be undermined by high punishment costs (see reviews and theory). Observability (e.g., identifying punishers or showing contributions) and mechanisms promoting reputation may further moderate effects.

- **Contextual and Limiting Conditions:**  
  Results may be domain-specific: structured populations, lab versus field settings, institutional versus peer punishment. If other interventions (e.g., rewards, gossip) are present, their potentially greater cost-effectiveness (Van Lange & Rand, 2022) should be considered. However, direct evidence on comparative efficiency is limited.

- **Quantitative Limitations:**  
  Few sources provide estimates or transfer functions for predicting treatment efficiency given design inputs and control efficiency.

# 6) Design Dimensions Highlighted Across Papers

| Dimension                | Directly Informed              | Indirectly/Contextually Discussed         | Missing or Sparse           |
|--------------------------|-------------------------------|-------------------------------------------|----------------------------|
| player_count             | Lee et al. (2022); many       | Most theory/models, contextually          | —                          |
| num_rounds               | Lee et al. (2022), others     | Reviews, most agent-based models          | —                          |
| chat                     | Bicchieri et al. (2022) (no punishment context) | Possibly in reviews                  | Most                       |
| all_or_nothing           | Lee et al. (2022), Hua & Liu (2024) | Several theory models                | —                          |
| default_contrib          | Rare (Bicchieri et al., 2022 context) | Not systematically modeled            | Most                       |
| mpcr (marginal per-capita return) | Lee et al. (2022), Hua & Liu (2024) | Theoretical models                  | —                          |
| punishment_cost          | Lee et al. (2022), Wang et al. (2023), others | Some adjacent models                | —                          |
| punishment_tech (mechanism) | Lee et al. (2022), Wang et al. (2023) (institutional); others discuss in context |                                  | —                          |
| reward_exists/reward_cost/reward_tech | Hua & Liu (2024), Wang et al. (2023) | Theoretical context                 | Sparse for punishment cases|
| show_n_rounds            | Bicchieri et al. (2022)       | Rare reviews/experiments                   | Most                       |
| show_other_summaries     | Van Lange & Rand (2022)       | Norms/reputation in reviews                | Most                       |
| show_punishment_id       | Boyd & Richerson (2022) (contextually); Van Lange & Rand (2022) | Reputation, visibility              | Most                       |

**Most Directly Informed:** player_count, num_rounds, all_or_nothing, mpcr, punishment_cost, punishment_tech.  
**Indirect/Contextual Only:** reward parameters, observability, information sharing (show_xxx dimensions).  
**Sparse or Missing:** chat, default_contrib, explicit reporting of chat or communication, framing, and most information/observability manipulations.

# 7) Important Limitations

- **Limited Empirical Data:**  
  Most papers are theoretical or review-based, with very few reporting experimental or field data connecting design dimensions, control efficiency, and treatment (punishment-enabled) efficiency.

- **Payoff versus Behavioral Measures:**  
  Many findings are based on cooperation rates or norm compliance, not on efficiency or group payoff, limiting their utility for payoff prediction without further assumptions.

- **Contextual Scope:**  
  Many models assume spatial or networked population structure, which may not generalize to well-mixed PGGs commonly used in lab experiments.

- **Missing Design Coverage:**  
  Several important prediction dimensions (such as chat, default contribution, framing, and most observability variables) are not systematically modeled or reported.

- **Comparative Interventions and External Validity:**  
  Studies make alternative mechanisms (gossip, reward) salient, but few provide direct efficiency comparisons or cost-effectiveness analyses between interventions.

- **Absence of Parameterized Predictive Models:**  
  No paper provides an integrated or empirical function mapping all relevant design dimensions plus control efficiency to treatment efficiency in the presence of punishment, leaving a gap for data-driven prediction.

- **Ambiguity in Mechanism-Outcome Link:**  
  Increases in cooperation rates due to punishment do not always translate to increases in efficiency, especially when punishment is costly; this distinction is not always clear in mechanistic papers.

---

In summary, while this literature set provides some strong theoretical insights—particularly about the punishment cost and fine magnitude dimension—empirically grounded, high-resolution guidance for efficiency prediction across full game designs is limited. Where findings exist, they strongly emphasize parameter sensitivity and the importance of context, but prediction must still rely heavily on theoretical conjecture rather than robust empirical calibration.
