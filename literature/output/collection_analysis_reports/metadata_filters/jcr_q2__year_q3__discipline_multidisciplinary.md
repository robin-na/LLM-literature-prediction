# 1) Evidence Base

The paper set contains two sources: one laboratory experiment in a threshold public goods game (close PGG variant) featuring third-party punishment (Liao et al., 2021), and one theoretical, agent-based model of multi-agent cooperation in poverty alleviation featuring both sanctions and incentives (Zhang et al., 2020). The evidence base is therefore a mix of empirical and theoretical work, but is very limited in size and narrow in directly payoff-related findings pertaining to classic PGG environments. Both papers deal with cooperation and sanctions, but only the experiment provides empirical results relevant to payoff outcomes. The theoretical paper provides only indirect, contextual insights.

# 2) Task Relevance

Relevance is moderate but not complete along all three axes:

- **pgg_or_variant:**  
    - Liao et al. (2021): `close` (threshold PGG with automatic third-party punishment rather than classic peer punishment)  
    - Zhang et al. (2020): `adjacent` (multi-agent cooperation with PGG-like elements but not a canonical PGG)
- **punishment_or_sanctions:**  
    - Liao et al. (2021): `exact` (focused on presence/absence of punishment as a treatment)  
    - Zhang et al. (2020): `adjacent` (punishment modeled as negative returns for non-cooperation, not as explicit player-to-player punishment)
- **efficiency_or_related_payoff_outcome:**  
    - Liao et al. (2021): `adjacent` (primary outcomes are investment/cooperation rates and probability of achieving the public good, not direct total group payoff or efficiency; still interpretable as efficiency-improving in threshold context)
    - Zhang et al. (2020): `adjacent` (analyzes cooperation rates and equilibrium behaviors; does not provide group payoff or efficiency as an explicit outcome)

Neither paper matches perfectly to standard continuous-contribution PGGs with peer punishment and direct efficiency measurement, but the experimental evidence is more relevant and interpretable for the prediction task than the theory paper.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes:**
    - *Liao et al. (2021):* Reports cooperation success rates (proportion of groups achieving the threshold), which can be interpreted as a proxy for efficiency in threshold PGGs, given all-or-nothing payoff structure. Does **not** report direct group payoff or total earnings.
    - *Zhang et al. (2020):* Does not report group payoff or efficiency; focuses on modeling equilibrium cooperation rates.

- **Non-Payoff Behavioral Outcomes:**
    - Both papers focus mainly on cooperation rates, investment rates, or “willingness to cooperate.” These are important for understanding mechanisms but are not direct measures of total group payoff or efficiency.

- **Distinction:**  
    - Neither study provides direct measurements of average efficiency (i.e., realized group payoff as a fraction of the social optimum), but Liao et al. (2021) reports threshold achievement, which in a threshold PGG context maps cleanly to full efficiency in the rounds achieved.

# 4) Main Findings Relevant To Prediction

- **Punishment Effects in PGG-like Environments:**
    - *Liao et al. (2021):* Introducing third-party punishment in a small-group, threshold-based PGG significantly increases group investment rates and the probability of successfully achieving the public good—from 55.57% to 76.85%, under otherwise identical design conditions. Regression analyses confirm this effect is robust to controls. This is strong evidence that a punishment regime of this type (automatic, third-party, impersonal) raises efficiency-like outcomes in such settings.
    - *Zhang et al. (2020):* Qualitative and theoretical support that both punishment (moderate negative returns for noncooperation) and positive incentives encourage cooperation in multi-agent collaborations. The literature points out the need for balance, as excessive punishment is not always better, and a combination of incentives and sanctions is most effective. However, payoff/efficiency outcomes are not demonstrated.

- **Limits and Caveats:**
    - Liao et al. (2021) only implements *automatic* third-party punishment, not peer punishment as is standard in PGG predictions. Results are directly relevant for threshold PGGs with small groups, and may or may not generalize to continuous-contribution PGGs or peer punishment environments.
    - Findings are stronger for behavior than for measured group payoffs/efficiency per se, as neither study reports aggregate welfare or earnings explicitly.

# 5) Prediction Guidance

- **Direction of Punishment Effect:**  
   - In threshold PGGs with small (n=3) groups, no chat, and automatic third-party punishment, enabling punishment is expected to **substantially increase the typical efficiency or likelihood of group success** compared to the control (punishment disabled). This is supported by direct behavioral evidence (Liao et al., 2021).

- **Magnitude:**  
   - The observed effect is from 55.57% to 76.85% “success” rate in public good achievement, which should be interpreted as a Δ-efficiency for these all-or-nothing rounds under these conditions—assuming full payoff in success rounds, zero otherwise.

- **Context Specificity:**  
   - These findings are **most valid** for threshold PGGs with automatic, impersonal third-party punishment, small group size, and no communication.
   - Evidence for classic peer (player-to-player) punishment, for continuous PGGs, or for games with chat/communication is **not directly provided**.

- **Theory Paper Integration:**  
   - Zhang et al. (2020) provides qualitative but not quantitative or directly transferable insights: moderate punishment and reward can improve cooperation, but do not guarantee improved efficiency, and the optimal balance is context-dependent.

- **Dimensions Supported for Prediction:**  
   - Prediction inference is most supported when evaluating designs close to the tested settings (threshold, small group, automatic TPP, no chat, explicit group threshold), and control game efficiency is approximated by the “success rate” baseline.

# 6) Design Dimensions Highlighted Across Papers

- **Directly Informed:**  
    - `player_count` (both papers; small group in Liao, multi-agent model in Zhang)  
    - `num_rounds` (Liao)  
    - `all_or_nothing` (threshold/all-or-nothing in both)
    - `punishment_cost` (both; explicit parameter)
    - `mpcr`/threshold mechanics (Liao)
    - `reward_exists` (Zhang; considered in theory)
    - `chat` (Liao; not allowed)

- **Indirectly Informed:**  
    - `punishment_tech` (Liao uses automatic third-party, not peer)
    - `default_contrib` (not directly manipulated but investment rates tracked)
    - `reward_cost`, `reward_tech` (Zhang discusses incentives generally)

- **Only Contextually Discussed or Missing:**  
    - `show_n_rounds`, `show_other_summaries`, `show_punishment_id` (not manipulated or discussed in detail)
    - `reward_cost`, `reward_tech`, `reward_magnitude` (Zhang; only in theory model, not directly matched to PGG parameters)
    - Communication effects (`chat`) are kept constant (no chat), so interaction with punishment is not explored.

- **Peer Versus Third-Party Punishment:**  
    - The main strongly evidenced intervention is *automatic, impersonal third-party punishment* (Liao). Classic peer-to-peer punishment and its design nuances (e.g., visibility, cost-magnitude tradeoffs) are *not* tested.

# 7) Important Limitations

- **Narrow Empirical Base:**  
    - Only one experiment, with a small sample and a specific implementation of punishment (automatic, third-party) in threshold PGGs; classic peer punishment in standard PGGs is missing.

- **Payoff/Efficiency Outcomes Not Directly Measured:**  
    - Efficiency is inferred (via “success rate”) rather than directly measured as group earnings divided by social optimum as in most PGG studies. This weakens the link to payoff-based prediction.

- **Limited Generalizability to Standard PGGs:**  
    - Both papers are anchored in threshold/all-or-nothing or multi-agent cooperation settings; not designed for canonical continuous-contribution PGGs with peer punishment.

- **Sparse Coverage of Design Dimensions:**  
    - Several prediction-relevant dimensions (e.g., communication, reward cost/tech, payoff display conditions) are not explored systematically.

- **Absent or Incomplete Data on Rival Explanations:**  
    - Potential for negative or null effects of punishment in other contexts (larger groups, other punishment forms, with communication or varying parameters) is not addressed.

- **Retracted Status:**  
    - The primary experimental source (Liao et al., 2021) is marked as retracted, so its reliability is potentially compromised for downstream prediction.

**Conclusion:**  
The evidence base provides relatively strong, if narrow, support that introducing automatic third-party punishment in small threshold PGGs increases efficiency-related outcomes. However, directly relevant experimental evidence for classic peer punishment and direct efficiency measures is absent. Predictions made from this literature are most credible when applied to all-or-nothing, small-group, no-communication designs with automatic third-party punishment, but generalization outside those specifics is poorly supported by the current papers.
