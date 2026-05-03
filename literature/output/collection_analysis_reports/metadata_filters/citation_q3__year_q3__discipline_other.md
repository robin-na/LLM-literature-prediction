# 1) Evidence Base

The paper set consists of four sources: two theoretical papers directly modeling payoff-based outcomes, one theory paper focused on behavioral (non-payoff) outcomes in an adjacent setting, and one empirical (observational) field study measuring norm change rather than payoffs or efficiency. There are no laboratory or field experiments directly manipulating punishment in public goods games (PGG), and empirical evidence on payoff outcomes is limited. The set is moderately broad in considering diverse mechanisms (punishment, incentives, feedback, legal/reputational comparisons), but relatively narrow for the specific prediction task, since only one paper (Zhang & Cao, 2020) provides a formal description linking PGG punishment mechanisms to group efficiency with peer sanctioning enabled.

# 2) Task Relevance

**pgg_or_variant**
- **exact:** Zhang & Cao (2020) (theoretical PGG with punishment, insurance, loners).
- **adjacent:** Baker & Choi (2018) (repeated moral hazard, legal/reputational sanctions); Liu & Yang (2018) (cooperation in innovation networks with free-riding elements); Berger (2021) (sustainable consumption, not a direct game-theoretic public goods setting).

**punishment_or_sanctions**
- **exact:** Zhang & Cao (2020), Baker & Choi (2018), Liu & Yang (2018) (all focus on sanctioning mechanisms).
- **adjacent:** Berger (2021) (normative feedback, no direct punishment).

**efficiency_or_related_payoff_outcome**
- **exact:** Zhang & Cao (2020), Baker & Choi (2018) (focus on group efficiency and welfare as explicit outcomes).
- **adjacent:** Liu & Yang (2018) (cooperation stability; not directly group payoffs).
- **weak:** Berger (2021) (proportion of norm adherence; efficiency not measured).

**Summary:** Only one paper is an *exact* match on all three relevance criteria. Others are either adjacent in mechanism or outcome, with the empirical paper (Berger, 2021) largely focused on norm dynamics rather than efficiency. Empirical evidence directly answering the prediction task is not present.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:** Explicit measurement of group payoff, surplus, welfare, or efficiency is present in the two theory papers (Zhang & Cao, 2020; Baker & Choi, 2018). These works analyze efficiency as a function of sanctioning features.
- **Non-payoff behavioral outcomes:** Liu & Yang (2018) and Berger (2021) measure or discuss behavioral outcomes such as frequency of cooperation or adoption of a sustainable norm. Neither quantifies total payoffs or efficiency relative to optimal group cooperation.
- **Distinction:** The literature is clear that many “cooperation” or “contribution” outcomes do not necessarily translate into higher group efficiency, since costs of punishment and structure of sanctioning can reduce or even reverse payoff gains (Zhang & Cao, 2020; Baker & Choi, 2018).

# 4) Main Findings Relevant To Prediction

- **Punishment Can Enable High Efficiency – But Not Always**: Theoretical modeling (Zhang & Cao, 2020) shows that enabling peer punishment can move a group from low-efficiency equilibria (defection, cycles) to full efficiency if the punishment fine is sufficiently high relative to both the marginal per-capita return and the group size. If the punishment regime is too weak or can be bypassed by other strategy options (insurance, loner), or if the cost of punishment is high, efficiency gains may not materialize.
- **Effectiveness Depends on Design Features**: Specific design parameters—punishment fine (magnitude), cost of punishing, group size, multiplier (mpcr), and the presence of alternate strategies—jointly determine the regime (cooperation, cycles, or defection). Small design changes can shift which equilibrium is stable (Zhang & Cao, 2020).
- **Visibility, Costliness, and Error-Proneness Matter**: Baker & Choi (2018) argue that visible and accurate punishment mechanisms (here, legal sanctions) achieve greater efficiency than more diffuse or uncertain sanctions (reputational), emphasizing the importance of observability and reliability of sanctioning. High costs or low accuracy can undo these efficiency advantages.
- **Indirect Links from Behavioral Change**: Adjacent papers (Liu & Yang, 2018; Berger, 2021) show that interventions such as incentives, punishments, or social feedback can alter cooperation rates or norm adherence, but do *not* directly link these changes to payoff improvement or efficiency.
- **Empirical Confirmation Limited**: There is no direct empirical (experimental or field) evidence in the set quantifying the effect of enabling peer punishment on treatment efficiency versus control.

# 5) Prediction Guidance

**Direct Implications for Predicting Treatment Efficiency:**
- *Enablement of Peer Punishment* in a PGG environment raises expected average efficiency if—conditional on design features—punishment is strong enough (fine, cost), the marginal per-capita return is not too low, and group size is moderate (Zhang & Cao, 2020).
- *Magnitude and Cost Parameters* must be modeled: If punishment is weak, costly, or easily circumvented, predicted efficiency gains shrink or vanish. Empirical control efficiency (pre-punishment) is an important baseline, but structural parameters dictate the marginal impact of punishment (Zhang & Cao, 2020).
- *Visibility and Accuracy* (Baker & Choi, 2018): Prediction should adjust downward if punishment is hidden, unreliable, or perceived as unfair, though this dimension is not empirically measured in this set.
- *Absence of Empirical Estimates*: Quantitative prediction must interpolate from theory; the literature does not offer empirical effect sizes or observed magnitude of efficiency change.

**Limitations:**
- The guidance is theory-driven and assumes conditions (population structure, well-mixed groups, repeated or one-shot games) match the models.
- No empirical data constrains predictions, so uncertainty about the quantitative effect is high.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed (modeled or discussed with payoff outcomes):**
- `player_count` (group size): Theoretical effect on stability of efficient equilibria (Zhang & Cao, 2020; Baker & Choi, 2018).
- `num_rounds`: Modeled in repeated environments and in defining regime (Baker & Choi, 2018; Zhang & Cao, 2020).
- `mpcr` (public goods multiplier): Modeled as critical for determining when punishment benefits outweigh costs (Zhang & Cao, 2020).
- `punishment_cost` and partial `punishment_tech` (fine levels): Central parameters for efficiency outcomes (Zhang & Cao, 2020; Baker & Choi, 2018).
- `all_or_nothing`: Included in theoretical models, impacting mixing and dynamics (Zhang & Cao, 2020).

**Indirectly Informed or Only Contextually Discussed:**
- `reward_exists`: Modeled as complementary incentive (Liu & Yang, 2018).
- `show_n_rounds`, `show_other_summaries`: Discussed as relevant for observability; only contextually tied to efficiency (Baker & Choi, 2018; Berger, 2021).
- `chat` and `show_punishment_id`: Not substantially discussed in relation to efficiency.
- `default_contrib`: Not addressed.
- `reward_cost`, `reward_tech`: Touched upon in incentive modeling (Liu & Yang, 2018) but not with payoff outcomes.

**Sparse or Effectively Missing:**
- `chat`
- `default_contrib`
- `reward_cost`
- `reward_tech`
- `show_punishment_id` (except tangentially in legal sanction discussion)

# 7) Important Limitations

- **Lack of Empirical Evidence:** There are no direct experimental or field-empirical studies in this set reporting observed treatment effects of punishment enablement on efficiency.
- **Limited Scope of Theoretically Modeled Mechanisms:** Theoretical predictions depend on simplifying assumptions (e.g., well-mixed populations, full observability, stable strategies) which may not generalize to all experimental or field settings.
- **Dimension Coverage Gaps:** Several prediction-relevant dimensions (e.g., chat, default contribution framing, identification of punishers, reward mechanics) are unexplored or only contextually referenced, leaving predictions less well-grounded for games that vary these features.
- **Ambiguity For Realistic Settings:** No paper provides quantitative cross-game prediction rules or parameterizations; effects of punishment under ambiguity, heterogeneity, or design complexity are not assessed.
- **Payoff vs. Behavior Distinction:** Some papers report only increased rates of cooperation or norm adherence, not actual efficiency improvement—an effect which may not translate into payoff gains if sanctions are costly or misapplied (as noted in Zhang & Cao, 2020).

**Conclusion:** This paper set provides strong theoretical but limited empirical basis for predicting efficiency changes due to enabling punishment in PGG-like environments. Prediction is best informed by structural modeling of game parameters, but extrapolating to specific experimental designs or settings not matching model assumptions is uncertain. Many design features critical for the downstream task remain underexplored or are absent from the existing literature covered here.
