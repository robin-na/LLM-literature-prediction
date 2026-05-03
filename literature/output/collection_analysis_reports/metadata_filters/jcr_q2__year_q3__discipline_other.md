# 1) Evidence Base

The paper set comprises two theory papers with direct or adjacent relevance to punishment effects in public-goods-game (PGG) frameworks, and two empirical papers—one a laboratory experiment in a resource extraction context, the other an observational field study of real-world cooperative groups. The theory papers focus on the direct mechanisms and efficiency impacts of punishment in collective action settings, while the empirical papers provide contextual and behavioral observations, with limited direct measurement of efficiency. Overall, the evidence base skews toward theoretical analysis with explicit comparative statics and clear predictions, while empirical evidence is either adjacent (resource restoration) or lacks payoff-outcome measurement (community field study). The coverage is moderate on PGG and punishment mechanisms, but limited in direct experimental estimation of punishment effects on efficiency within standard PGG designs.

# 2) Task Relevance

- **pgg_or_variant**:  
  - *exact*: One theory paper (Zhang & Cao, 2020) models a standard PGG setup with evolutionary dynamics, punishment, and strategy competition.  
  - *adjacent*: The other theory paper (Baker & Choi, 2018) uses a moral hazard/legal context analogous to collective action, and the two empirical papers study adjacent settings (cooperative communities; resource extraction/restoration games).
- **punishment_or_sanctions**:  
  - *exact*: Both theory papers address punishment/sanctions head-on, analyzing cost, effectiveness, and comparative efficiency.  
  - *exact* (field study): Qirko (2020) documents the presence and contextual use of third-party punishment in communities.  
  - *none*: Chang et al. (2021) does not include or analyze punishment.
- **efficiency_or_related_payoff_outcome**:  
  - *exact*: Zhang & Cao (2020) and Baker & Choi (2018) directly analyze group efficiency or social welfare.  
  - *adjacent/close*: Chang et al. (2021) assesses individual and group payoffs in a restoration task but without punishment.  
  - *none*: Qirko (2020) does not measure efficiency or payoff; focus is on behavioral norms and enforcement.

In summary, the literature set provides strong theoretical and some contextual empirical relevance for punishment and efficiency outcomes in collective action environments, but direct empirical evidence within the precise PGG-with-punishment paradigm is limited.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (efficiency, group payoff, welfare):**  
  - *Zhang & Cao (2020)*: Explicitly models efficiency (group payoff relative to fully cooperative outcome) under different punishment regimes.  
  - *Baker & Choi (2018)*: Models efficiency/comparative welfare implications of legal versus reputational sanctions.  
  - *Chang et al. (2021)*: Reports group/individual payoffs through resource extraction/restoration, but no punishment; only adjacent to PGG with sanctions.
- **Non-payoff behavioral outcomes (contribution rate, norm compliance, punishment behavior):**  
  - *Qirko (2020)*: Primary focus on free-riding acknowledgment, enforcement frequency, and contextual determinants of punishment; no group payoffs measured.
- **Other/unclear outcome types:**  
  - Some papers (e.g., Chang et al., 2021) assess psychological variables (e.g., guilt, anger) associated with restoration choices, not directly predicting efficiency.

**Conclusion:** Only two papers directly target payoff-based outcomes relevant for efficiency prediction; the others provide contextual or behavioral insights, not quantifiable efficiency data.

# 4) Main Findings Relevant To Prediction

- **Theoretical Mechanism (PGG + Punishment):**  
  - Robust, explicit models (Zhang & Cao, 2020) indicate that enabling sufficiently strong punishment (fine size relative to MPCR and group size) can cause a dramatic shift from low- to high-efficiency equilibria, sometimes attaining full cooperation. The regime is sensitive: if punishment is weak or easily circumvented (e.g., via insurance/loner strategies), efficiency gains vanish, and defectors/speculators can dominate.
- **Sanctioning Regime Comparisons:**  
  - Baker & Choi (2018) argue that legal/costly punishment is often more efficient than reputational sanctions, especially when punishment is accurate, visible, and not excessively costly. The presence of error-prone or high-cost enforcement, or highly reliable reputational mechanisms, can reverse efficiency advantages.
- **Contextual Enforcement, Empirical Setting:**  
  - Qirko (2020) finds that even when punishment mechanisms are available in real-world cooperative groups, actual enforcement is infrequent and highly context-dependent. This suggests enabling punishment is not always sufficient for efficiency gains if not implemented or utilized.
- **Absence of Punishment:**  
  - Chang et al. (2021) shows resource overexploitation in the absence of punishment, but cannot answer whether a punishment regime would improve efficiency.

# 5) Prediction Guidance

- **Direct Application:**  
  Theoretical papers offer explicit comparative statics: Enabling peer punishment should be predicted to increase efficiency—potentially up to full cooperation—if punishment is strong relative to the benefit and group size, and if circumvention channels (insurance, loner exit) are closed or unappealing (Zhang & Cao, 2020). If punishment is weak or circumvented, enabling it should not be expected to increase efficiency.
- **Mechanism Sensitivity:**  
  Predictions should be conditional on punishment cost, magnitude, and accuracy. High punishment cost or low punishment efficacy may yield little or negative effect. Contexts where punishment is not used, despite being available, may see no efficiency gain.
- **Empirical Uncertainty:**  
  Absent direct empirical evidence for standard PGG experiments with punishment modulation, predictions should draw on theory but retain uncertainty about implementation fidelity, contextual moderators, and external validity (as per Qirko, 2020).
- **Default Prediction:**  
  If control game efficiency is low and game design allows for effective and not-too-costly punishment, theory suggests a substantial increase in treatment efficiency is plausible when enabling punishment. This is attenuated if group size is large, punishment is expensive or ineffective, or opportunities for circumvention exist.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed (by theory or empirical evidence on payoff/efficiency):**
- `player_count`, `num_rounds`, `all_or_nothing`, `mpcr`, `punishment_cost`, `punishment_tech` (Zhang & Cao, 2020; Baker & Choi, 2018)
- `show_n_rounds` (Baker & Choi, 2018; Chang et al., 2021)

**Indirectly, contextually, or non-payoff informed:**
- `chat`, `show_other_summaries`, `show_punishment_id` (Behavioral implementation details in Qirko, 2020; Chang et al., 2021—not linked to payoff outcomes)
- `reward_exists`, `reward_cost`, `reward_tech`, `default_contrib`: Mentioned in dimensions list but not substantively analyzed in the set.

**Effectively missing (not informed or only in adjacent settings):**
- Design dimensions relating to rewards (`reward_exists`, `reward_cost`, `reward_tech`), and interface/framing features (`default_contrib`, `show_other_summaries`, `chat`) are generally not empirically or theoretically connected to efficiency effects of punishment in these papers.

# 7) Important Limitations

- **Empirical Gaps:**  
  There is a lack of direct experimental measurement of efficiency changes due to enabling/disabling punishment in canonical PGG settings (no classic lab experiments included).
- **Real-world Context vs. Lab Results:**  
  Field/observational evidence (Qirko, 2020) shows that punishment mechanisms may not be utilized in practice, limiting external validity of theoretical predictions.
- **Mechanism Generality:**  
  Some theoretical results are developed for large, well-mixed populations or legal enforcement regimes (Baker & Choi, 2018), so their quantitative predictions may not port cleanly to small-group PGG lab settings.
- **Unmodeled Design Dimensions:**  
  Several game design variables critical for prediction (e.g., chat, reward options, summary visibility, default contribution framing) are not covered in efficiency-relevant findings.
- **Qualitative Over Quantitative:**  
  Most guidance from the theory papers is comparative/static or directional, not calibrated to produce quantitative estimates of effect size (change in efficiency).
- **Circumvention and Non-Payoff Considerations:**  
  Theory highlights mechanisms (insurance/loner options, litigation error) that can moderate or negate punishment’s efficiency effects, yet their empirical frequency and impact in practical PGG designs remain sparse in this set.

---
**References**  
- Zhang, J. L., & Cao, M. (2020)  
- Baker, S., & Choi, A. H. (2018)  
- Qirko, H. (2020)  
- Chang, C. C. et al. (2021)
