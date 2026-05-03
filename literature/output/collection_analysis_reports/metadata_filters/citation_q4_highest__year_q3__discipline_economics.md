# 1) Evidence Base

The paper set is a mix of empirical (both experimental and observational) and theoretical work, with three experimental laboratory studies, two large-scale observational/field studies, one theoretical review, and one experimental study with only adjacent relevance. The majority of directly relevant evidence for the prediction task is provided by two empirical lab-experimental studies: Arechar et al. (2018) and the review by Dannenberg & Gallier (2020). Both provide primary, detailed findings on public goods games (PGGs) with and without peer punishment. The other papers offer theoretical background, adjacent evidence in related social dilemma or trust game settings, or are primarily about cultural, psychological, or preference heterogeneity factors, rather than directly about the impact of punishment on group efficiency in PGGs. Overall, while the evidence base is broad in disciplinary perspectives, it is relatively narrow in terms of direct, highly relevant empirical results for predicting efficiency in PGG-like environments with peer punishment enabled versus disabled.

---

# 2) Task Relevance

**pgg_or_variant**
- *exact (2/7)*: Arechar et al. (2018) and Dannenberg & Gallier (2020) provide direct evidence from PGGs or extremely close institutional variants.
- *close/adjacent (2/7)*: Okada (2020) (indirect reciprocity in social dilemmas) and Fonseca & Peters (2018) (trust games with reputation/gossip) are structurally adjacent but not canonical PGGs.
- *none (3/7)*: Enke (2019), Falk et al. (2018), and Sutter et al. (2018) do not use PGGs or structurally similar games.

**punishment_or_sanctions**
- *exact (2/7)*: Arechar et al. (2018) and Dannenberg & Gallier (2020) investigate peer punishment as a treatment.
- *close/adjacent (3/7)*: Okada (2020) (justified punishment in theoretical models), Enke (2019) (societal punishment norms), Fonseca & Peters (2018) (reputation/social sanctions, not direct costly punishment).
- *adjacent/none (2/7)*: Falk et al. (2018) and Sutter et al. (2018) do not manipulate or examine punishment in group settings.

**efficiency_or_related_payoff_outcome**
- *exact (3/7)*: Arechar et al. (2018), Dannenberg & Gallier (2020), and Fonseca & Peters (2018) report efficiency or group payoff outcomes as central dependent variables.
- *adjacent (3/7)*: Okada (2020), Enke (2019), Falk et al. (2018) address efficiency or welfare at a societal or model-abstract level, not measured efficiency in game experiments.
- *none (1/7)*: Sutter et al. (2018) measures individual time preference only.

---

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes**
- *Direct Measures*: Arechar et al. (2018), Dannenberg & Gallier (2020), and Fonseca & Peters (2018) report average efficiency (e.g., earnings as a fraction of maximum possible), group payoff, and total surplus in repeated game settings.
- *Indirect/Abstract*: Okada (2020) and Enke (2019) discuss efficiency or welfare in theoretical or societal terms, not as directly observed experimental variables.

**Non-Payoff Behavioral Outcomes**
- *Contributions*: Arechar et al. (2018) and Dannenberg & Gallier (2020) also report contribution rates and how these support higher payoffs under punishment.
- *Norm Compliance, Punishment Patterns*: Okada (2020) and Enke (2019) focus on norm dynamics and psychological attitudes toward punishment/cooperation.
- *Trust, Trustworthiness*: Fonseca & Peters (2018) measures trust/trustworthiness as mediators for increased efficiency via reputational channels.
- *Preferences*: Falk et al. (2018) and Sutter et al. (2018) report patience, trust, altruism, and reciprocity, but do not examine earnings or efficiency in game-theoretic settings.

---

# 4) Main Findings Relevant To Prediction

- **Peer Punishment Robustly Increases Efficiency in PGGs**: Empirical evidence from Arechar et al. (2018) and Dannenberg & Gallier (2020) shows that, when peer punishment is enabled in standard repeated public goods games, group efficiency increases compared to otherwise identical control games without punishment. Contributions and earnings per participant are sustainably higher, and the gains are seen both in lab and online samples (Arechar et al., 2018).
- **Effect Dependent on Punishment Cost and Effectiveness**: Dannenberg & Gallier (2020) highlight that the efficiency-enhancing effect of punishment institutions is greatest when punishment is effective at eliminating free-riding and not too costly to impose.
- **Institutional Choice and Repeated Interaction**: The effectiveness and popularity of punishment institutions grow with repeated play and institutional learning (Dannenberg & Gallier, 2020).
- **Related Effects in Reputation and Social Sanctions**: Fonseca & Peters (2018) find that even non-costly, reputational sanctions (gossip) also raise efficiency relative to control, but this evidence is from trust games, not PGGs, and operates via trust/trustworthiness rather than direct costly punishment.
- **Cultural and Structural Moderators**: Theoretical and observational papers (Okada, 2020; Enke, 2019) suggest—without experimental confirmation in PGGs—that the effectiveness of punishment may depend on broader cultural or institutional context and the nature of norm systems.

---

# 5) Prediction Guidance

The literature provides strong, directly transferable evidence that enabling peer punishment in repeated public goods games increases average group efficiency. When predicting treatment efficiency:
- Expect a robust efficiency increase when punishment is enabled, especially when punishment is not too costly and is effective at deterring free-riding (Arechar et al., 2018; Dannenberg & Gallier, 2020).
- If the baseline (control) efficiency is low (i.e., contribution decay or persistent free-riding), the relative gain from enabling punishment is likely to be larger.
- Design features such as player count, number of rounds, MPCR, punishment cost, and the presence/visibility of institutional features (e.g., chat, summaries) are all discussed as influential, with the first three dimensions empirically supported and the others either partially informed or adjacent by analogy.
- Beware that the positive effect can be limited if punishment is too costly or does not eliminate free-riding, and that endogenous adoption of the institution may matter for field or applied predictions (Dannenberg & Gallier, 2020).
- Evidence from adjacent mechanisms (reputation, gossip) in trust games (Fonseca & Peters, 2018) supports the general conclusion that social sanctions increase efficiency, but these effects are not strictly equivalent to direct costly punishment in PGGs.
- Theoretical and cultural context implies potential moderators, but does not provide direct functional forms or effect size estimates for prediction.

---

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- `player_count` (Arechar et al., 2018; Fonseca & Peters, 2018)
- `num_rounds` (Arechar et al., 2018; Fonseca & Peters, 2018)
- `mpcr` (Arechar et al., 2018; Fonseca & Peters, 2018)
- `punishment_cost` (Arechar et al., 2018; Dannenberg & Gallier, 2020; Okada, 2020)
- `punishment_tech` (Dannenberg & Gallier, 2020; Okada, 2020)
- `all_or_nothing` (Arechar et al., 2018; Okada, 2020; Fonseca & Peters, 2018: continuous, not all-or-nothing)
- `chat` (Arechar et al., 2018; Fonseca & Peters, 2018)

**Indirect/Partially Informed:**
- `show_n_rounds` (Fonseca & Peters, 2018, in adjacent games)
- `show_other_summaries` (Adjacent, as peer feedback/reputational info; Fonseca & Peters, 2018)
- `default_contrib` (Not directly addressed, but embedded within design of some studies)
- `punishment_magnitude` (Parameter in Arechar et al., 2018)

**Sparse or Missing:**
- `reward_exists`, `reward_cost`, `reward_tech` (Not directly studied in supplied set)
- `show_punishment_id` (Not specifically manipulated or reported in direct empirical evidence)
- Several papers do not address the design/control/game framing dimensions at all (notably Enke, 2019; Falk et al., 2018; Sutter et al., 2018).

---

# 7) Important Limitations

- **Empirical Coverage is Narrow**: Only two papers (Arechar et al., 2018; Dannenberg & Gallier, 2020) provide directly relevant, parameterized experimental data on punishment versus control efficiency in PGGs. Evidence for other design dimensions or real-world generalizability is limited.
- **Adjacent Evidence May Not Generalize**: Findings from trust games with reputation (Fonseca & Peters, 2018) and indirect reciprocity models (Okada, 2020) may not transfer directly to PGGs, particularly since the mechanism of action (reputational sanctions vs. costly punishment) differs.
- **Non-Payoff Outcomes Are Not Equivalent**: Many papers report increases in trust, cooperation, or norm compliance rather than direct payoff/efficiency metrics. Prediction should not conflate these behavioral changes with actual group efficiency outcomes.
- **Lack of Evidence on Some Design Dimensions**: Several potentially influential design variables, particularly around rewards, group structure, and visibility of sanctions, are not systematically varied or reported in the directly relevant experiments.
- **Potential Moderators Not Explored Experimentally**: Theoretical and cultural context papers highlight possible moderators (e.g., culture, reputation system structure, kinship), but these are not empirically tested within PGGs in this evidence base.
- **Aggregate Benefit of Endogenous Choice is Mixed**: Dannenberg & Gallier (2020) note that while endogenous adoption of punishment institutions can be especially effective, not all groups adopt even beneficial institutions, introducing variability that is difficult to incorporate as a fixed design effect.

**Conclusion:**  
The strongest available guidance is that enabling peer punishment (of the standard, not too costly, not too weak type) in repeated PGGs reliably increases group efficiency relative to disabling it, with player count, rounds, and punishment parameters being informative moderators. However, many design features are underexplored, and broader cultural moderators as well as reward mechanisms remain gaps in the experimental literature reviewed here. Prediction should be anchored in the control efficiency of the no-punishment baseline, with upward adjustment for punishment enabled—moderated by cost and effectiveness—justified by both direct empirical and comprehensive review evidence.
