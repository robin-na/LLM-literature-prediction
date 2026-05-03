# 1) Evidence Base

This paper set consists of three papers, all of which are theory-based and do not include new empirical or experimental results. The coverage is broad in the sense of considering behavioral mechanisms (social norms, memory, network structure), but narrow and indirect with respect to the downstream prediction task: predicting efficiency in public-goods-game-like (PGG) designs when enabling peer punishment, conditional on design and baseline efficiency. Only one paper (Wang et al., 2023) analytically approaches efficiency-related outcomes, and even then does so in models that are mostly institutional rather than peer-based and focus primarily on structured Prisoner’s Dilemma settings—not canonical PGG. The other two papers are conceptually adjacent: one models cooperation in spatial games with historical memory but no punishment or efficiency analysis (Gou & Li, 2023), and the other reviews norm enforcement and behavioral change from a conceptual/theoretical perspective (Andrighetto & Vriens, 2022).

# 2) Task Relevance

**Relevance by Dimension:**

- **pgg_or_variant:**  
  - *Wang et al. (2023):* `adjacent` (structured Prisoner’s Dilemma, institutional punishment/reward).  
  - *Gou & Li (2023):* `adjacent` (spatial Prisoner’s Dilemma with memory, no punishment).  
  - *Andrighetto & Vriens (2022):* `adjacent` (collective action generally; not specific to PGG).  

- **punishment_or_sanctions:**  
  - *Wang et al. (2023):* `exact` (analyzes institutional punishment and reward mechanisms, though not peer punishment).  
  - *Gou & Li (2023):* `adjacent` (does not include punishment, focuses on history-dependent behavior).  
  - *Andrighetto & Vriens (2022):* `adjacent` (punishment discussed as a norm enforcement mechanism in theory).  

- **efficiency_or_related_payoff_outcome:**  
  - *Wang et al. (2023):* `close` (focus on cumulative cost to achieve high cooperation, which proxies for efficiency but is not a direct measurement).  
  - *Gou & Li (2023):* `adjacent` (outcome is cooperation rate, not payoff or efficiency).  
  - *Andrighetto & Vriens (2022):* `adjacent` (discussion of efficiency is theoretical and contextualized to social norms).  

**Summary:**  
Overall, coverage of punishment/sanctions is most direct in the context of institutional design, not peer-based punishment as found in canonical PGG. Efficiency or payoff as an explicit, measured group-level outcome is largely absent or only proxied by theoretical constructs. No paper provides empirical or experimental efficiency results for PGG with or without punishment.

# 3) Outcomes Measured in the Literature

- **Payoff-related outcomes:**  
  - *Wang et al. (2023):* Theoretical analysis of the cumulative cost required for an institution to sustain high cooperation, which serves as a proxy for intervention efficiency, but not group efficiency as classically defined (i.e., total group payoff relative to the cooperative optimum).
   
- **Non-payoff behavioral outcomes:**  
  - *Gou & Li (2023):* Focuses on cooperation rate, cluster stability, and the effect of memory on cooperation—no consideration of group payoff or efficiency.  
  - *Andrighetto & Vriens (2022):* Emphasizes norm compliance, strength, and change as drivers of collective behavior, sometimes referencing efficiency at a conceptual level but with no measured outcomes.

**Distinction Maintained:**  
Only one paper indirectly relates to payoff/efficiency (Wang et al., 2023). The others restrict their outcome space to behavioral or norm-centric measures.

# 4) Main Findings Relevant to Prediction

- **Punishment and Cooperative Efficiency:**  
  - *Wang et al. (2023)* shows that both punishment and reward (when optimally configured by an institution) can elicit high levels of cooperation in structured populations, with minimal intervention cost—more so when initial cooperation is high. This suggests efficiency can be improved via punishment in certain contexts, although this is modeled for institutional (not peer) punishment in Prisoner’s Dilemma rather than PGG.
  - The results imply efficiency gains are conditional: punishment is more cost-effective (and thus efficient) when groups start with higher cooperation; reward can be preferable when initial cooperation is low.

- **Social Norm Enforcement:**  
  - *Andrighetto & Vriens (2022)* highlights mechanism arguments: punishment as a social norm enforcer can stabilize cooperative behavior but can also entrench inefficient norms or backfire, depending on context (group heterogeneity, cultural “tightness,” etc.). No empirical quantification is offered.

- **Game Properties Affecting Cooperation:**  
  - *Gou & Li (2023)*, while not analyzing punishment, suggests that features like historical memory can stabilize high cooperation rates, which by inference could feed into higher group payoffs—but this effect is not shown for efficiency nor does it address punishment.

# 5) Prediction Guidance

Given the evidence base, prediction of average efficiency upon enabling punishment in a PGG (using control efficiency and game design dimensions) is weakly informed:

- Theoretical insights (*Wang et al., 2023*) suggest that, in games where institutions can tune punishment and reward, efficiency gains from punishment depend on the initial state of cooperation; punishment is efficient in high-cooperation contexts, reward in low-cooperation ones. However, these results are not directly transferable to peer-punishment PGG, as the modeled games and enforcement mechanisms differ.
- *Andrighetto & Vriens (2022)* caution that sanctioning mechanisms can sometimes lead to inefficiency if social norms are misaligned or the group context is adverse.
- No paper empirically quantifies average efficiency improvements resulting from enabling peer punishment under specific game dimensions; no dose–response or comparative analysis is reported.
- For prediction, this literature collectively suggests that the effect of enabling punishment is highly context-dependent—mediated by initial cooperation, sanctioning design, and social norms—but does not provide concrete parameter estimates or quantitative shifts in efficiency based on the game dimensions or observed control efficiency.

# 6) Design Dimensions Highlighted Across Papers

| Dimension                     | Directly Informed                    | Indirectly Informed                  | Contextually Discussed                | Effectively Missing                |
|-------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|------------------------------------|
| player_count                  | Wang et al. (2023); Gou & Li (2023)  | —                                    | —                                     | —                                  |
| num_rounds                    | Gou & Li (2023)                      | —                                    | —                                     | Wang et al. (2023); Andrighetto & Vriens (2022) |
| chat                          | —                                    | —                                    | —                                     | All papers                        |
| all_or_nothing                | Wang et al. (2023); Gou & Li (2023)  | —                                    | —                                     | —                                  |
| default_contrib               | —                                    | —                                    | —                                     | All papers                        |
| mpcr                          | Wang et al. (2023) (by implication)  | —                                    | —                                     | Gou & Li (2023); Andrighetto & Vriens (2022)   |
| punishment_cost               | Wang et al. (2023)                   | —                                    | —                                     | Gou & Li (2023); Andrighetto & Vriens (2022)   |
| punishment_tech               | Wang et al. (2023) (institutional)   | —                                    | —                                     | —                                  |
| reward_exists, reward_cost    | Wang et al. (2023)                   | —                                    | —                                     | —                                  |
| reward_tech                   | Wang et al. (2023)                   | —                                    | —                                     | —                                  |
| show_n_rounds                 | —                                    | —                                    | —                                     | All papers                        |
| show_other_summaries          | —                                    | —                                    | —                                     | All papers                        |
| show_punishment_id            | —                                    | —                                    | —                                     | All papers                        |

**Note:**  
- *Most coverage is theoretical and does not map each dimension to measurable efficiency shifts from punishment.*
- *Peer punishment is not directly analyzed in any paper; Wang et al. (2023) covers institutional punishment.*

# 7) Important Limitations

- **Lack of Empirical Evidence:** None of the reviewed papers provide empirical or experimental data on the effect of enabling (peer) punishment on efficiency in PGG or close variants.
- **Mismatch of Game Structures:** Central results derive from Prisoner’s Dilemma games, not standard PGG, and use institutional (not peer) punishment mechanisms which differ in both psychological and structural effects.
- **Outcome Measure Gap:** Only one study approximates an efficiency-related outcome, and it does so with institutional cost rather than group payoff or actual efficiency ratio.
- **Parameter-Level Gaps:** Most prediction-relevant design dimensions (e.g., chat, default contribution, payoff visibility) are not analyzed or even discussed.
- **Behavioral–Payoff Disconnect:** Two papers focus strictly on behavioral (cooperation/norm) outcomes, not on average group payoffs or efficiency.
- **Ambiguity and Context Dependence:** Theory suggests that punishment effectiveness depends heavily on initial conditions, group context, and potential for negative norm lock-in, but without quantitative guidance, practical prediction is unsupported.
- **Transferability Limits:** Mechanism insights (e.g., norm enforcement, memory effects) are suggestive but may not translate into quantitative shifts in efficiency relevant to the PGG with peer punishment.
- **No Analysis of Peer Punishment Technicalities:** Dimensions like punishment identity revelation, cost-to-magnitude ratio, or reward–punishment interactions in PGG peer settings are not covered.

**Conclusion:**  
This literature set provides conceptual and mechanism-level insights, but is largely ill-equipped to support quantitative or even strong qualitative prediction of the efficiency effects of enabling punishment in public goods games, given the specified game design dimensions and baseline control game efficiency. Direct, parameter-level, empirical evidence is effectively absent.
