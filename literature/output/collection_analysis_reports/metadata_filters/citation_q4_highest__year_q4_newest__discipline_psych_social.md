### 1) Evidence Base

The paper set includes four papers, all theoretical or review in nature—none are experimental or directly empirical. Only one paper (Hua & Liu, 2024) provides theoretical (model-based) analysis of payoff-based outcomes in public goods games, and focuses on reward rather than punishment. The remaining three (Van Lange & Rand, 2022; Boyd & Richerson, 2022; Gross & Vostroknutov, 2022) are broad, primarily theoretical or literature-synthesizing, and discuss social dilemmas, sanctioning mechanisms, and norm compliance in human cooperation with only adjacent or contextual relevance to payoff-based outcomes or public goods games strictly defined. No paper offers quantitative estimates of efficiency shifts caused by enabling peer punishment. Thus, the evidence base is narrow and indirect for the specific prediction of efficiency changes from peer punishment in public-goods-game-like environments.

---

### 2) Task Relevance

- **PGG or Variant**:  
  - Hua & Liu (2024) is directly (exactly) about PGGs, but only in the context of rewards—not punishment.
  - Van Lange & Rand (2022) are “close”, employing repeated public goods games and social dilemmas as paradigms in their discussion.
  - Boyd & Richerson (2022) and Gross & Vostroknutov (2022) are “adjacent”, discussing collective action and social norms in settings analogous to but not explicitly structured as public goods games.
  
- **Punishment or Sanctions**:  
  - None of the papers provides direct (exact) empirical evidence about peer punishment systems in PGGs.
  - Van Lange & Rand (2022), Boyd & Richerson (2022), and Gross & Vostroknutov (2022) all mention punishment or social sanctions but are only “adjacent” to the specific institutional or peer punishment mechanisms in standard PGGs.
  - Hua & Liu (2024) includes no analysis of punishment.

- **Efficiency or Related Payoff Outcome**:  
  - Only Hua & Liu (2024) addresses efficiency and group payoff explicitly, focusing on how rewards affect these outcomes ("exact" relevance).
  - All other papers focus on cooperation rates, norm adherence, or general group-level outcomes, not payoff or efficiency ("adjacent" at best).

---

### 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes**:  
  - Only Hua & Liu (2024) models and predicts group efficiency and total welfare, and only in the context of rewards.
  - No paper provides empirical or theoretical analysis of payoff or efficiency changes under peer punishment interventions.

- **Non-Payoff Behavioral Outcomes**:  
  - Van Lange & Rand (2022) review findings on contribution/cooperation rates, behaviors under observation, and effects of social mechanisms (reputation, gossip, punishment) on cooperation—but do not measure group payoff or efficiency directly.
  - Boyd & Richerson (2022) discuss scale and mechanisms of cooperation in foraging societies, highlighting how sanctions sustain participation, but without quantifying economic efficiency or payoffs.
  - Gross & Vostroknutov (2022) review norm compliance and its psychological drivers in economic games, focusing on rule-following behavior rather than group payoff or efficiency.

---

### 4) Main Findings Relevant To Prediction

- **Effect of Punishment on Efficiency**:  
  - No paper in the set provides direct evidence or quantitative modeling of the efficiency impact of enabling peer punishment in public goods games.
  - Van Lange & Rand (2022) emphasize that, while punishment can stabilize cooperation, alternative mechanisms such as gossip may achieve similar or greater efficiency due to lower costs, implying that punishment’s benefit may be offset by its direct costs.
  - Boyd & Richerson (2022) argue that large-scale cooperation is often stabilized by sanctions and institutional mechanisms, supporting the general plausibility of punishment as a way to deter free-riding, especially as group size increases. However, they provide no quantified payoff analysis.
  - Hua & Liu (2024) gives conditions under which rewards promote efficiency but does not analyze punishment or any cost incurred through sanctions.
  - Gross & Vostroknutov (2022) focus on internalized norms’ role in sustaining cooperation, suggesting that external punishment may be unnecessary if norms are strong, but again do not link these insights to efficiency outcomes.

- **Moderators and Mechanisms**:
  - Observability (showing others' actions or outcomes) is emphasized as important for the effectiveness of sanctions in sustaining cooperation (Van Lange & Rand, 2022).
  - Group size is discussed as crucial for the maintenance of cooperation under collective action frameworks (Boyd & Richerson, 2022).
  - The costs of punishment (punishment_cost) are highlighted as possibly reducing the net efficiency of sanctioning systems, suggesting a trade-off between increased cooperation and resources lost to punishers (Van Lange & Rand, 2022; Boyd & Richerson, 2022).

---

### 5) Prediction Guidance

- The literature reviewed is insufficient for calibrating quantitative predictions of the efficiency effect of enabling peer punishment, given only control game efficiency and specified design dimensions.  
- **Hua & Liu (2024)** offers direct (though only theoretical) guidance for interventions involving *rewards*—for such designs, efficiency as a function of group parameters and reward rules can in principle be predicted following their model.  
- For punishment, the papers only support the qualitative expectation that peer punishment *can* increase cooperation (i.e., increase contributions), but may *not* improve group efficiency if costs of sanctioning outweigh gains in contributed resources (Van Lange & Rand, 2022).
- Mechanism arguments suggest that observability, reputation, and group size moderate the effectiveness of punishment, but there is no empirical or quantitative efficiency data for parameterization.
- For prediction purposes, the best guidance is to treat the presence of punishment as a factor that potentially increases contributions (and thus could increase efficiency in control games with low cooperation), but with an ambiguous or negative effect when punishment is costly and baseline contributions are already high.

---

### 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- For rewards: player_count, all_or_nothing, mpcr, reward_exists, reward_cost, reward_tech (Hua & Liu, 2024).
- Contextual sanction dimensions: player_count, punishment_cost, show_other_summaries, punishment_tech, show_punishment_id (Van Lange & Rand, 2022; Boyd & Richerson, 2022).

**Indirectly/Contextually Discussed:**
- num_rounds, default_contrib, reward_exists, show_n_rounds (Van Lange & Rand, 2022, indirectly when discussing repeated games and cooperation stability).
- Observability-related dimensions (show_other_summaries, show_punishment_id) as modulators of sanction effectiveness (Van Lange & Rand, 2022; Boyd & Richerson, 2022).

**Effectively Missing:**
- punishment_magnitude, reward_magnitude, and most combinatorial aspects of reward and punishment systems.
- chat, default_contrib, and specific implementation details for peer punishment in PGGs are not empirically addressed or discussed in relation to efficiency outcomes.

---

### 7) Important Limitations

- **Lack of Empirical Evidence**: No paper provides direct experimental or observational data on efficiency/payoff outcomes with and without peer punishment in public goods games.
- **Reward versus Punishment Generalization**: Findings for reward-based interventions (Hua & Liu, 2024) cannot be directly extended to punishment-based predictions.
- **Outcome Measures**: Most findings pertain to behavioral outcomes (contribution, cooperation, norm adherence) rather than efficiency or payoff, which is the required criterion for prediction.
- **No Quantitative Estimates**: Mechanistic and theoretical arguments about effectiveness or moderators (e.g., group size, cost of punishment) are not supplemented by parameter values or comparative results between control and punishment-enabled games.
- **Limited Coverage of Design Dimensions**: Several relevant prediction dimensions, especially those unique to punishment implementations, are sparse or unaddressed.
- **Generalizability**: The papers address either broad psychological or anthropological mechanisms or focus on reward, limiting generalizability to experimental PGGs with peer punishment enabled or disabled.

---

**Summary Statement**:  
This literature set offers valuable context about social mechanisms for cooperation and insight into reward-based efficiency enhancement in public goods games. However, it provides only indirect or adjacent support (and no direct empirical findings) for the quantitative prediction of efficiency changes from enabling peer punishment, conditional on game parameters and control efficiency. Its use for prediction tasks should be cautious, qualitative, and limited to contextual or theoretical supplementation.
