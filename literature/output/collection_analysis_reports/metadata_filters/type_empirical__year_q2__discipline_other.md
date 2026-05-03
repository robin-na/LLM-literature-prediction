# 1) Evidence Base

The provided paper set consists of six papers, predominantly empirical and experimental (5 out of 6), including both laboratory and field experiments. One paper is observational and qualitative. The set is moderately narrow, with the majority focused on public goods games (PGGs) or close variants and using punishment or sanction mechanisms, though there is some inclusion of adjacent domains such as market externality experiments, the Ultimatum Game, and institutional case studies. Most experiments report behavioral outcomes (e.g., contributions, norm violations) rather than directly reporting efficiency as defined in standard PGGs (group payoff as a ratio to the social optimum). Two lab experiments (Engel & Zhurakhovska, 2017; Eisenberg & Engel, 2014) provide the most specific and closest evidence relating punishment to group payoffs, whereas others inform through mechanisms or analogous findings.

# 2) Task Relevance

**pgg_or_variant:**  
- **Exact:** Four papers use standard linear PGGs or very close analogs (Engel & Zhurakhovska, 2017; Eisenberg & Engel, 2014; Bell et al., 2016; Rommel, 2015).  
- **Adjacent/Weak:** The remaining two (Brevers et al., 2013; Montoya et al., 2015) are adjacent. Brevers et al. analyze costly rejection (punishment) in the Ultimatum Game, and Montoya et al. discuss cooperation mechanisms in institutional and sociobiology analogs, not direct PGGs.

**punishment_or_sanctions:**  
- **Exact:** Four papers are directly about punishment or sanctions within the experimental design (Engel & Zhurakhovska, 2017; Eisenberg & Engel, 2014; Bell et al., 2016; Rommel, 2015).  
- **Adjacent:** Brevers et al. (Ultimatum rejections) and Montoya et al. (punishment/reward in governance theory) only address punishment analogically or as a conceptual factor.

**efficiency_or_related_payoff_outcome:**  
- **Close:** Engel & Zhurakhovska (2017) and Eisenberg & Engel (2014) come closest—they report group payoffs or profit and discuss stability relative to Nash or the baseline, allowing inferences about efficiency. Payoff is not always normalized to the fully cooperative optimum.
- **Adjacent:** Bell et al. (2016) and Rommel (2015) report mainly behavioral outcomes (contribution rates, norm violations) but not direct payoff or efficiency.  
- **None/Weak:** Brevers et al. (2013) and Montoya et al. (2015) do not report efficiency or group payoff.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes:**  
  - **Direct/Close:** Mean group payoff, total profit, or group earnings (Engel & Zhurakhovska, 2017; Eisenberg & Engel, 2014).
  - **Indirect:** None of the papers report efficiency explicitly as a ratio to the social optimum, but it is possible to infer it from group earnings in some.
  - **Absent:** No direct efficiency outcomes in Bell et al. (2016), Rommel (2015), Brevers et al. (2013), or Montoya et al. (2015).

- **Non-Payoff Behavioral Outcomes:**  
  - Contribution rates, punishment rates, conditional cooperation, norm violation frequencies, market entry (as a proxy for externality), rejection of unfair offers, staff stability, and presence of institutional rewards/punishments.
  - Most papers report primarily these behavioral outcomes rather than monetary efficiency.

# 4) Main Findings Relevant To Prediction

- **Punishment increases group payoffs in repeated PGGs:**  
  - Introducing peer or centralized punishment consistently results in higher group payoffs and greater maintenance of cooperation compared to the no-punishment baseline (Engel & Zhurakhovska, 2017; Eisenberg & Engel, 2014).
  - The effect is robust to variations in punishment design (authority characteristics, framing, policy announcement).
  - However, the efficiency gains are strongly moderated by the punishment regime’s severity and probability. When sanctions are weak/rare, cooperation still decays (Eisenberg & Engel, 2014).

- **Behavioral mechanism matters for efficiency effects:**  
  - Actual experience of being punished (not the mere threat) has a stronger impact on sustained payoff and contribution stability (Eisenberg & Engel, 2014).
  - Changes to the power dynamic of punisher (CPun vs. UCPun) affect patterns of conditional cooperation and punishment sensitivity, with ambiguous effects on free-riding rates (Bell et al., 2016).

- **Payoff gains may be reduced by “side effects” of punishment:**  
  - In some setups, the increase in cooperation is offset by higher punishment costs or unintended rise in free riding (Bell et al., 2016), possibly limiting net efficiency gains.

- **Analogous findings:**  
  - In adjacent domains, punishment reduces antisocial or norm-violating behavior (Rommel, 2015; Brevers et al., 2013), but the mapping to standard PGG efficiency is indirect.

# 5) Prediction Guidance

**Strength of Guidance:**  
- The literature provides **strong empirical evidence that enabling (peer or centralized) punishment in repeated linear PGGs generally increases group efficiency**, i.e., the average group payoff rises relative to the no-punishment baseline (Engel & Zhurakhovska, 2017; Eisenberg & Engel, 2014).
- **Key moderators include:** 
  - Punishment severity and likelihood (stronger/likelier punishment yields higher gains in efficiency)
  - Realization (punishment must be actually used, not just available)
  - Game repetition and information structure (feedback, repeated rounds, observability)

**Quantitative Prediction:**  
- The effect size of efficiency improvement is design-dependent: severe, likely, and centralized punishment mechanisms produce greater and more sustained efficiency gains; weak or infrequently used sanctions yield only modest or temporary improvements.
- When punishment is “just enough” to stabilize cooperation, efficiency rises but potentially falls short of the social optimum if punishment is costly or applied excessively.

**Control Efficiency as Predictor:**  
- In environments where control group efficiency is very low (rapid decay of cooperation/payoff), introducing punishment typically produces a large relative increase in efficiency, but the absolute post-treatment efficiency depends on the severity, cost, and effectiveness of the sanction regime.

**Caveats:**  
- In games or treatments where punishment produces counterproductive side effects (e.g., increased free riding or costly over-punishment), efficiency gains may be moderated or offset (Bell et al., 2016).

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**  
- `player_count` and `num_rounds`: All experimental papers specify these; most are small-N lab setups (2–6 players, 1 to ~20 rounds).
- `mpcr` (Marginal per-capita return): Explicitly specified and manipulated in several papers (Engel & Zhurakhovska, 2017; Eisenberg & Engel, 2014; Bell et al., 2016).
- `punishment_cost`: Varied or manipulated directly in most punishment papers (all but Brevers et al., Montoya et al.).
- `all_or_nothing`: Most studies use continuous contributions; some note all-or-nothing conditions.
- `chat`: Absence of chat is specified.
- `punishment_tech` and `punishment_magnitude`: At least partly considered via different punishment regimes (compensatory/treble damages; conditional/unconditional punishment).

**Indirectly Informed/Partially Addressed:**  
- `show_other_summaries`, `show_n_rounds`, `show_punishment_id`: Sometimes mentioned (e.g., information feedback and transparency in Engel & Zhurakhovska, 2017), but not systematically varied.
- `reward_exists`, `reward_cost`, `reward_tech`: Only Montoya et al. (2015) explicitly discusses rewards, and then only as a qualitative mechanism, not an experimentally manipulated design dimension.
- `default_contrib`: Not directly reported or manipulated.

**Missing or Contextual Only:**  
- Very limited discussion or absence of manipulations for `reward_cost`, `reward_tech`, `reward_magnitude`, and `default_contrib`.
- No systematic evidence on the effect of enabling mutual rewards alongside punishment.

# 7) Important Limitations

- **Lack of direct efficiency reporting:** Most papers report group payoffs, but few express results as efficiency relative to the full-cooperation maximum, requiring inference or cautious extrapolation for prediction tasks.
- **Behavioral vs. payoff measures:** Many findings are about contribution/cooperation rates or norm violations—these often, but not always, correlate with group efficiency, especially when punishment is costly.
- **Limited generalizability of some findings:** Some treatments are highly specialized (centralized punishment, legal framing, one-shot games, or market entry with externalities), which may not generalize cleanly to standard peer-punishment PGGs.
- **Sparse coverage across all prediction dimensions:** Only a subset of the 14 dimensions is directly addressed; others (especially reward-related and informational transparency variables) are either unmanipulated or missing.
- **No quantification of moderator effects:** The influence of `player_count`, `num_rounds`, `mpcr`, and punishment parameters is shown to matter, but quantitative relationships (i.e., how much efficiency rises with increasing punishment severity or player number) are not provided.
- **Ambiguous findings regarding punishment side effects:** At least one study finds a rise in free riding with punishment, suggesting unpredictable side effects on efficiency under certain configurations (Bell et al., 2016).
- **Adjacent domain evidence is suggestive, not definitive:** Ultimatum Game and institutional/case study findings are conceptually relevant but provide no direct basis for efficiency prediction.

---

**In summary:**  
Prediction models using this literature should rely most strongly on repeated linear PGG lab findings: enabling punishment (especially when severe/likely/centralized) increases group payoffs and efficiency over baseline, but the magnitude depends on specific parameterization, actual implementation, and the structure of feedback and information. Some prediction dimensions (reward, framing, transparency) are weakly or not at all informed. Where only non-payoff or adjacent evidence exists, caution is warranted in generalizing findings to efficiency outcomes.
