# Evidence Base

This paper set consists of four studies, mostly theoretical, with one experimental/empirical lab study. The types include:
- One experimental empirical study focused on multi-group common-pool resource games with communication but without punishment (Sadowski et al., 2015).
- Three theory/modeling studies: one on the evolution of shame in response to punishment (Jaffe, 2008), one on multiagent governance with both punishment and reward (Zhang et al., 2020), and one on the dynamics of an N-person chicken game (Szilagyi & Somogyi, 2010).

Overall, the paper set is broad in the types of social dilemma games, but narrow in direct relevance to the downstream prediction task. Only one paper is experimental and only one (Sadowski et al., 2015) includes empirical payoff-based efficiency outcomes, but this paper lacks punishment manipulation. The rest are theory models, with some including punishment or reward mechanisms, but rarely measuring group efficiency or equivalent payoff outcomes directly.

# Task Relevance

**pgg_or_variant:**  
- Only Sadowski et al. (2015) is close to a standard public goods or common-pool resource game (relevance: *close*). The others are *adjacent*: Jaffe (2008) models generic resource-sharing with punishment and shame; Zhang et al. (2020) models multiagent cooperation with specific poverty alleviation context; and Szilagyi & Somogyi (2010) studies an N-person chicken game.
- None is an exact match for the canonical linear PGG.

**punishment_or_sanctions:**  
- Jaffe (2008) focuses exactly on the consequences of social punishment (relevance: *exact*), but not in a PGG context.
- Zhang et al. (2020) is *adjacent*; it includes punishment as negative feedback for non-cooperating agents.
- Sadowski et al. (2015) is *weak*; there is no punishment condition or manipulation, just reference to the absence of punishment.
- Szilagyi & Somogyi (2010) is *none*; punishment is not modeled at all.

**efficiency_or_related_payoff_outcome:**  
- Sadowski et al. (2015) is *exact*; it measures efficiency and group payoffs.
- Szilagyi & Somogyi (2010) is *close*, analyzing aggregate cooperation but not group payoff.
- Jaffe (2008) and Zhang et al. (2020) are *adjacent*; they focus on cooperation rates or behavioral equilibrium, but not efficiency or payoff.

# Outcomes Measured In The Literature

- **Payoff-related outcomes:**  
  Only *Sadowski et al. (2015)* measures group efficiency and total group payoffs, but does NOT include punishment conditions; thus, no evidence on the effect of punishment on efficiency.
- **Non-payoff behavioral outcomes:**  
  All theory papers focus on behavioral or norm-related outcomes—generosity/cooperation rate (Jaffe, 2008), willingness to cooperate (Zhang et al., 2020), and proportion of cooperators (Szilagyi & Somogyi, 2010). These are not direct measures of welfare, surplus, or group efficiency, though they are relevant predictors.

# Main Findings Relevant To Prediction

- **Effect of Punishment/Sanctions:**  
  - Jaffe (2008) finds punishment and shame can sustain higher generosity and stabilize pro-social behaviors, especially if punishment is not costly for the punisher, but this is about evolutionary stability—not group efficiency or payoff.
  - Zhang et al. (2020) finds moderate punishment increases cooperation in a multiagent poverty-relief scenario, but does not report efficiency. Results suggest that a mix of incentives (rewards) and moderate sanctions is better than heavy top-down subsidies.
  - Sadowski et al. (2015) demonstrates that communication and leadership (without punishment) can achieve moderate efficiency, suggesting that punishment is not strictly necessary for cooperation.
- **Payoff Effects:**  
  Direct evidence about punishment's impact on efficiency is absent. Only the mechanism implications are discussed: punishment can promote cooperation (which may increase efficiency), but this link is not quantified or directly tested in these studies.
- **Design Features:**  
  Communication, leadership, and the cost of punishment are highlighted. Communication enables cooperation in the absence of punishment (Sadowski et al., 2015). Low-cost punishment is predicted to be more effective in maintaining high cooperation rates (Jaffe, 2008).

# Prediction Guidance

This literature cannot provide precise, quantitative predictions for the treatment efficiency of a PGG when enabling peer punishment, given control efficiency and design dimensions. Instead:

- It provides indirect, mostly theoretical support for the premise that introducing punishment (especially with low cost) can increase cooperation, which may lead to higher efficiency (Jaffe, 2008; Zhang et al., 2020).
- Empirical evidence from a closely related public goods context (Sadowski et al., 2015) shows that communication alone can achieve moderate efficiency, even without punishment.
- None of the studies allow direct estimation of the change in efficiency when punishment is enabled—only that positive behavioral effects are likely, especially if punishment is inexpensive and where communication or leadership is lacking.
- Extreme caution should be used: the payoff link from increased cooperation to group efficiency is assumed, not established. Effects could be context-dependent and nonmonotonic (Szilagyi & Somogyi, 2010).

# Design Dimensions Highlighted Across Papers

- **Directly Informed:**
  - *player_count* (modeled in several theory papers, tested empirically in Sadowski et al., 2015)
  - *num_rounds* (Sadowski et al., 2015; Szilagyi & Somogyi, 2010)
  - *punishment_cost* (central to Jaffe, 2008; Zhang et al., 2020)
  - *all_or_nothing* (Zhang et al., 2020; Szilagyi & Somogyi, 2010)
  - *chat*/*communication* (Sadowski et al., 2015)

- **Indirectly Informed:**
  - *reward_exists* (Zhang et al., 2020)
  - *show_other_summaries* and *show_n_rounds* (Sadowski et al., 2015, in context of information, but not punishment)

- **Only Contextually Discussed or Missing:**
  - *mpcr*, *default_contrib*, *punishment_tech*, *reward_cost*, *reward_tech*, *show_punishment_id*: These dimensions are not systematically studied or only mentioned in specific setups. No identified studies manipulate technological mechanisms or information display about punishment/reward.
  - No studies describe or analyze all 14 prediction dimensions in a unified way.

# Important Limitations

- There is no direct empirical evidence on the effect of enabling punishment on efficiency in PGGs or very close variants—only indirect or theoretical suggestions.
- The dominant outcomes are behavioral (cooperation/generosity rates), not payoff-based (efficiency, group earnings).
- Most findings relate to evolutionary stability or equilibrium behaviors, not to group welfare or total payoffs.
- The one PGG-variant empirical study (Sadowski et al., 2015) omits punishment and focuses on communication, so it does not inform the impact of punishment activation.
- Theory studies use adjacent settings (generic resource-sharing, multiagent poverty games, N-person chicken), and their dynamics may not transfer straightforwardly to standard PGGs, particularly in quantitative terms.
- Several design dimensions necessary for prediction (e.g., mpcr, information about punishers, reward structure, default contribution) are not addressed.
- Severe risk that predictions based on this set could misestimate or mischaracterize the effect of punishment on efficiency in the target class of games.

---

**In summary:** This paper set provides only indirect, largely theoretical or adjacent evidence for predicting efficiency effects of enabling punishment in PGG-like games. It offers qualitative support that punishment can promote cooperation (and possibly efficiency), especially at low cost or when communication is lacking. However, no paper directly quantifies the efficiency change from enabling punishment, and relevant design dimensions (particularly those related to payoffs and punishment mechanisms) are sparsely covered. Predictions based on this literature should be considered highly uncertain and largely qualitative.
