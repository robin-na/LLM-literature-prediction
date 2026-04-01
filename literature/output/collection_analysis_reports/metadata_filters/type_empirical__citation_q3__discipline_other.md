# 1) Evidence Base

The paper set consists of five empirical studies, four of which are laboratory experiments and one observational field study. The set is moderately narrow for the prediction task: three papers are direct experimental tests of public goods games (PGGs) with varied punishment mechanisms (Engel & Zhurakhovska, 2017; Eisenberg & Engel, 2014; Bell et al., 2016), while the other two employ adjacent social dilemma paradigms (Ultimatum Game and a field norm intervention) without actual payoff-based efficiency outcomes (Brevers et al., 2013; Berger, 2021). Most findings are empirical, with little pure theory or modeling. Notably, the two Engel-related studies offer the clearest direct, treatment-versus-control lab data on punishment effects in PGGs, while the Bell et al. (2016) paper focuses on behavioral responses without reporting payoff outcomes. Overall, compared to the universe of literature, the evidence base is narrowly but directly focused on laboratory PGGs with punishment, with some behavioral spillovers and context from adjacent paradigms.

# 2) Task Relevance

**pgg_or_variant:**  
- *Exact:* Engel & Zhurakhovska (2017), Eisenberg & Engel (2014), Bell et al. (2016) all study exact PGGs or very close structural variants.
- *Adjacent:* Brevers et al. (2013) uses the Ultimatum Game (dyadic, not group-based), and Berger (2021) covers norm interventions in the field rather than a PGG framework.

**punishment_or_sanctions:**  
- *Exact:* The two Engel papers and Bell et al. (2016) manipulate punishment mechanisms (either centralized or peer).
- *Adjacent:* Brevers et al. (2013) interprets rejection as costly punishment but in a non-PGG setting; Berger (2021) involves no punishment or sanctions, only normative feedback.

**efficiency_or_related_payoff_outcome:**  
- *Close:* Engel & Zhurakhovska (2017) and Eisenberg & Engel (2014) report on group payoffs, profits, or welfare, which are closely related to efficiency, though not always reported as a ratio to the social optimum.
- *Adjacent/Weak:* Bell et al. (2016) does not report efficiency or group payoffs, focusing instead on contributions and behavioral change. Brevers et al. (2013) and Berger (2021) measure only behavioral or norm adoption outcomes, not efficiency or group earnings.

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes:**  
- Engel & Zhurakhovska (2017): *Group profit* (total earnings, not expressly as a fraction of the social optimum; proxies efficiency).
- Eisenberg & Engel (2014): *Group payoff/welfare* over repeated play (again, not always stated as "efficiency").
- Bell et al. (2016): *No payoff outcomes reported*; all findings are based on contributions and behaviors.
- Brevers et al. (2013), Berger (2021): *No payoff outcomes*; measure only behavioral responses (e.g., offer rejection, norm change).

**Non-Payoff Behavioral Outcomes:**  
- Contribution rates, cooperation rates, punishment assignment (Engel & Zhurakhovska, 2017; Bell et al., 2016).
- Sensitivity to unfairness (Brevers et al., 2013).
- Normative feedback and behavioral tipping (Berger, 2021).

# 4) Main Findings Relevant To Prediction

## Empirical Effects of Punishment on Efficiency (Payoffs)
- **Punishment as Efficiency Booster:** Both Engel & Zhurakhovska (2017) and Eisenberg & Engel (2014) find that enabling punishment (whether centralized or peer, provided it is sufficiently potent and likely) in repeated linear PGGs reliably increases group payoffs above the no-punishment baseline. Gains are attributed to stable cooperation rather than a transient or merely theoretical threat.
- **Strength & Implementation Matters:** The efficiency boost depends on the strength (severity and likelihood) of the punishment regime. More severe/class action damages or treble damages, and/or high likelihood of punishment, sustain contributions/efficiency, whereas weak or rare punishment rules may not prevent decay (Eisenberg & Engel, 2014).
- **Mechanism:** The observed effect on group payoffs is explained by actual experience with sanctions—not just their abstract presence. The availability of punishment leads to real behavioral change and payoff improvement.
- **Role of Payoff Type:** Although payoff reporting is usually in group profit or welfare—not always normalized as "efficiency"—the empirical direction (treatment group earns more than control) is clear.
- **Participation & Role Effects:** In Engel & Zhurakhovska (2017), introducing a non-beneficiary authority to administer punishment (centralized) still yields these gains, suggesting the effect is robust across various punishment roles.

## Non-Payoff Behavioral Mechanisms
- **Conditional Cooperation:** Bell et al. (2016) show that adding punishment options changes behavioral dynamics (responsiveness, sensitivity to others' contributions), but the increased cooperation may be offset by increased free riding. The net effect on efficiency is ambiguous since non-payoff outcomes are measured.
- **Norm Feedback:** Berger (2021) highlights the effects of normative feedback on behavioral tipping, with no direct payoff or PGG context.

# 5) Prediction Guidance

This literature set indicates with reasonable confidence that, in repeated linear PGG designs with similar configurations (group size, MPCR, number of rounds, and punishment available), enabling peer or centralized punishment is expected to increase average efficiency (or group payoff) above the no-punishment baseline, provided that punishment is sufficiently severe and likely to be implemented (Engel & Zhurakhovska, 2017; Eisenberg & Engel, 2014).

In other words, **all else equal (including control game efficiency), the presence and strength of punishment is associated with increases in group efficiency**. However, the magnitude of the effect depends on specifics of punishment design (cost, magnitude, who can punish, probability, and experience with sanctions) and group/environmental context. Only the Engel and Eisenberg & Engel papers deliver clear payoff outcomes—the other sources reinforce behavioral mechanisms.

For **prediction models**, the strongest inferences are where game dimensions match the lab designs studied: no chat, repeated rounds, specified MPCR, moderate group size, linear returns, punishment enabled with non-trivial cost and effect, and no competing reward mechanism. If punishment rules are weak or infrequently triggered, efficiency may not improve and could even decline (by cost of punishment alone).

**Dimensions not reported or only weakly discussed (e.g., chat, information feedback, reward systems)** may modulate the observed effect, but the evidence does not allow direct quantitative mapping without extrapolation.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions (empirical evidence of effect on efficiency or payoff):**
- `player_count`
- `num_rounds`
- `mpcr`
- `all_or_nothing`
- `punishment_cost`
- `punishment_tech` (centralized vs. peer, severity, etc.)

**Indirectly or Contextually Informed:**
- `show_other_summaries` (feedback on others’ actions is present in main studies but not experimentally varied)
- `show_n_rounds`
- `default_contrib` (framing not systematically varied, but not default in main studies)
- `reward_exists`, `reward_cost`, `reward_tech` (absent; not manipulated or discussed)

**Sparse or Missing Evidence:**
- `chat` (explicitly absent in key studies; effect unknown)
- `show_punishment_id` (anonymity or visibility of punishers is not systematically explored)
- `reward_exists`, `reward_cost`, `reward_tech` (no evidence)
- Behavioral dimensions (sensitivity to unfairness, norm tipping) discussed contextually, not payoff/efficiency-based and only peripheral to prediction.

# 7) Important Limitations

- **Measurement of Efficiency:** Few papers report efficiency as a ratio to the social optimum; most use total group payoffs. This requires the predictor to infer efficiency from raw earnings.
- **Non-Payoff Focus in Several Papers:** One-third of the papers do not provide payoff-based outcomes, limiting the ability to ground predictions on those dimensions (Bell et al., 2016; Brevers et al., 2013; Berger, 2021).
- **No Variation or Discussion of Many Design Dimensions:** Key moderators such as chat, reward mechanisms, punishment/reward identity visibility, and feedback about others' actions are either fixed or not discussed. This restricts generalizability and precision of prediction across all design possibilities.
- **Sparse Evidence on All-Or-Nothing vs. Continuous Contributions:** While the main papers use linear PGGs, it is unclear if results generalize to threshold or discrete-action games.
- **Consistency of Findings:** The main finding—punishment increases group payoffs and efficiency—is consistent, but ambiguous results from behavioral-only studies (e.g., increased free riding via punishment capability) caution against overgeneralization.
- **Limited Field/Contextual Evidence:** Most evidence is lab-based, and interventions outside the lab (e.g., Berger, 2021) do not translate directly to efficiency predictions or PGGs with punishment.
- **Generalizability beyond LAB PGGs:** Findings may not transfer to more complex or naturalistic settings (e.g., larger groups, longer/unknown duration, or games with communication/changing population).

---

In summary: This literature set is strong in supporting the prediction that (in repeated, linear, lab-based PGGs) introducing punishment will typically increase efficiency or group payoff, provided the punishment regime is consequential. The direct evidence is limited to a subset of the 14 design dimensions, particularly those concerning group structure and punishment specifics. Predictions for settings differing from these lab configurations or involving additional dimensions (e.g., communication, rewards) are less supported and should be made with caution.
