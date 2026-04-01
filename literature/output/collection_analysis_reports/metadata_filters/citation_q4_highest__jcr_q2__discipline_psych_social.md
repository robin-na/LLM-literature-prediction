# 1) Evidence Base

The evidence base comprises a mix of empirical (both laboratory and observational), theoretical, and review papers (24 in total), but is heavily skewed toward studies of laboratory public goods games, with some theory and many adjacent or ethnographic studies. The most relevant and detailed evidence comes from empirical laboratory PGG studies that directly manipulate punishment and measure payoff-based outcomes such as efficiency, group earnings, or welfare (Reuben & Riedl, 2009; Decker et al., 2003; Fehr et al., 2002; Choi & Ahn, 2013). Other papers address adjacent behavioral games, mechanisms (e.g., norm enforcement, social ties), or social/cultural context, but do not always report group payoff or efficiency. The coverage of design dimensions is uneven: some papers offer rich data on game structure and parameters, while many only contextually discuss or do not report relevant prediction features.

Overall, the paper set is moderately narrow for the prediction task: it delivers focused, high-quality laboratory evidence on standard PGGs with punishment, but much sparser or indirect support for less typical designs, cultural settings, or alternate sanction/reward structures.

# 2) Task Relevance

**pgg_or_variant:**  
- **exact**: About four studies provide *exact* relevance by using standard repeated linear PGGs with or without punishment, matching the downstream prediction setting (Reuben & Riedl, 2009; Fehr et al., 2002; Choi & Ahn, 2013; Decker et al., 2003).
- **close/adjacent**: Several others are close (variants, dictator/ultimatum/prisoner’s dilemma) or adjacent (ethnographic studies of cooperation).
- **weak/none**: Remaining studies use different social dilemma paradigms or focus on mechanisms without a direct game-theoretic PGG framework.

**punishment_or_sanctions:**  
- **exact**: Four empirical studies manipulate or enable real costly punishment within a PGG context (see above), and several theoretical/review papers focus specifically on punishment mechanisms.
- **adjacent/weak**: Many other papers discuss punishment in context, or investigate related incentives (e.g., reward, social critique) but do not directly implement peer punishment mechanics.

**efficiency_or_related_payoff_outcome:**  
- **exact/close**: Only four empirical studies report or can be used to estimate group efficiency or closely related payoff outcomes—these are foundational for prediction. Some others (e.g., Choi & Ahn, 2013) do not report efficiency directly but aggregate contribution data can be treated as a strong proxy.
- **adjacent/none**: Most other studies focus on non-payoff behavioral outcomes (contribution rates, fairness, norm compliance) and are only indirectly relevant.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes (directly relevant):**
- *Efficiency*: Reported or calculable in Fehr et al. (2002), Reuben & Riedl (2009), Decker et al. (2003), Choi & Ahn (2013; indirectly via contributions).
- *Group profit/earnings/welfare*: As above, where punishment and costs are included net of contributions and deductions.

**Non-payoff behavioral outcomes (indirect/relevant mostly for mechanism):**
- Contribution or cooperation rates (all “exact” PGG-punishment studies report these, but they are not efficiency per se).
- Punishment assigned, rejection rates, norm compliance, changes in social ties, perceptions of fairness, status attribution, or trust signals.

*Empirical payoff outcomes are comparatively rare; most studies report behavioral responses rather than net group earnings.*

# 4) Main Findings Relevant To Prediction

## Empirical Payoff-based Evidence:

- **Punishment Substantially Increases Efficiency, but with Caveats**:
    - In *homogeneous* standard linear PGGs, adding peer punishment options dramatically increases contributions and efficiency. Efficiency gains often approach or reach ~40% above control (Fehr et al., 2002).
    - These gains persist across both stable (partner) and random (stranger) matching.

- **Punishment Can Backfire or Have Minimal Efficiency Gains**:
    - When the *group is heterogeneous* (privileged PGG, i.e., asymmetric MPCR or unequal returns), punishment's positive effect on efficiency is *much* weaker and often increases inequality (Reuben & Riedl, 2009).
    - *Collective* punishment rules (as opposed to individual) increase contributions, but efficiency does not always rise due to the *added cost* of punishment—emotional, excessively severe, or poorly targeted punishment can reduce or even reverse efficiency gains (Decker et al., 2003).
    - The relationship between punishment availability/severity and efficiency is non-monotonic: more available/cheaper punishment sometimes means more wasteful punishment activity, offsetting cooperation increases.

- **Contributions as a Proxy for Efficiency**:
    - In studies that do not directly report efficiency but where net group contributions increase in the presence of punishment and the cost of punishment is modest, efficiency likely increases (Choi & Ahn, 2013).

## Contextual/Mechanism Evidence:

- *Antisocial punishment* (punishing cooperators) can sometimes reduce—or even eliminate—the efficiency advantage of allowing punishment, and is more prevalent in certain cultures or low-punishment-cost environments (Sylwester et al., 2013).
- The *cost-effectiveness* of punishment is critical; when punishment is expensive relative to the benefit gained from increased cooperation, group efficiency may not improve.
- The mechanics of information (anonymity, display of IDs, chat/communication) and perceptions of legitimacy/trust can moderate punishment’s effectiveness (theory and mechanism reviews).

# 5) Prediction Guidance

**Best-supported quantitative prediction**:
- For standard repeated linear PGGs with homogeneous MPCR, moderate group size (e.g., 3–5 players), and moderate/low punishment cost, enabling peer punishment will *usually* increase efficiency substantially relative to baseline control efficiency, especially as the game progresses. Predicted efficiency gains can be substantial (Fehr et al., 2002; Choi & Ahn, 2013).
- However, this is contingent: if punishment is very costly, poorly targeted (e.g., collective rules), or emotional/antisocial punishment is common, efficiency gains may be small or even negative (Decker et al., 2003; Sylwester et al., 2013).

**Prediction should be adjusted for:**
- **Group composition**: Heterogeneity in MPCR or returns reduces the marginal efficiency gain from punishment dramatically—even when control (no punishment) efficiency is higher (Reuben & Riedl, 2009).
- **Punishment cost and technology**: High punishment cost can erase efficiency advantages; low cost can sometimes boost antisocial punishment and lower welfare.
- **Reward options**: The effect of punishment is distinct from or interacts with reward mechanisms; enabling both may have different payoffs.
- **Information structure**: The identity of punishers/rewarders, rounds information, and summaries can affect the targeting and perceived legitimacy of punishment.
- **Control efficiency**: High baseline efficiency leaves less room for gains from punishment; the relationship is not strictly additive.

**When only non-payoff outcomes are reported:**  
Behavioral increases in cooperation or contribution under treatment with punishment generally imply higher group payoffs, but the magnitude of efficiency gains can only be estimated if punishment costs are known to be low. Without explicit efficiency data, predictions should be made with greater caution.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed:**  
- *player_count*: Empirical studies consistently use small (3–5 players) groups.
- *num_rounds*: Repeat-play dynamics are explored; efficiency gains of punishment are larger in later rounds.
- *mpcr*: Directly manipulated; critical moderator for efficiency effects.
- *punishment_cost*, *punishment_tech*: Both directly manipulated and shown to modulate effect direction and size.
- *all_or_nothing*: Most studies use continuous contributions, but all-or-nothing is reported as a design dimension.
- *chat*: Explicitly controlled (typically no chat) in main studies.
- *reward_exists*: Discussed in papers exploring both punishment and reward.

**Indirectly/contextually discussed:**  
- *show_n_rounds* and *show_other_summaries*: Sometimes reported; potential to moderate information available for targeting punishment.
- *reward_cost*, *reward_tech*: Reward mechanisms present in a minority of studies.
- *show_punishment_id*: Rarely manipulated but recognized as informational variable influencing social dynamics.

**Effectively missing:**  
- *default_contrib*: Framing of default contribution is not explicitly manipulated or reported in relevant studies.
- Several information dimensions (*show_punishment_id*, *show_other_summaries*) are usually held constant or not described in the most directly relevant papers.

# 7) Important Limitations

- **Limited empirical payoff data:** Only a minority of the literature reports group efficiency or net payoff; many studies focus on behavioral/psychological mechanisms without netting out punishment costs.
- **External validity/cultural generalizability:** Most data come from laboratory samples in WEIRD populations; ethnographic and observational results suggest punishment/costs and effects may differ in real-world settings, especially where antisocial punishment is common (Sylwester et al., 2013).
- **Sparse coverage of atypical designs:** Larger groups, longer or uncertain horizons, more complex punishment/reward structures, and communication dimensions are underexplored in relation to payoff.
- **Mechanism ambiguity:** The literature points to many moderators (heterogeneity, information, cultural context) whose effects are not systematically quantified across studies.
- **Non-monotonicity:** More punishment availability/severity can actually decrease efficiency if costs swamp contribution increases, so simple assumptions of positive monotonic effect are not justified.
- **Proxies for efficiency:** In cases where only contributions are reported, efficiency must be inferred and may overstate true efficiency if punishment costs are neglected.

---

**In summary:**  
Robust, empirical laboratory evidence supports that peer punishment can—under certain design conditions (homogeneous groups, moderate costs)—substantially improve efficiency in public goods games. But this positive effect is *not* universal: group heterogeneity, excessively costly or emotional punishment, and cultural patterns of antisocial punishment can sharply limit or even reverse efficiency gains. Accurate prediction requires careful mapping from game design to the context and mechanisms identified in the core experimental papers, adjustment for punishment costs, and caution in generalizing from contribution or cooperation rate increases to efficiency gains.
