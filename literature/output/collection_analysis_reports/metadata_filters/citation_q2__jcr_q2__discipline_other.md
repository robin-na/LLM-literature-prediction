# 1) Evidence Base

The evidence base comprises two theory-oriented papers. There are no empirical or experimental studies in this set. Both papers address multi-agent environments with social dilemma structures, but they differ in their focal mechanisms and outcome measures. The first paper (Lim & Capraro, 2022) uses analytical modeling to examine efficiency effects in a networked trust game, closely related to but not identical with PGG. The second paper (Wang & Cui, 2022) applies evolutionary game theory to a principal-agent setting with sanctioning but reports only behavioral outcomes (compliance/self-discipline), not efficiency or related payoffs. Overall, the paper set is relatively narrow and mostly theoretical, providing indirect but structured guidance for the downstream prediction task.

# 2) Task Relevance

**pgg_or_variant:**  
- Both papers are *adjacent* rather than *exact* with respect to public goods games. Lim & Capraro (2022) analyze a trust game structurally similar to PGG, especially in its treatment of cooperation, network effects, and institutional punishment. Wang & Cui (2022) focuses on a principal-agent dilemma, which maps onto social dilemma frameworks but diverges from canonical PGG settings.

**punishment_or_sanctions:**  
- Both papers are labeled *exact* on this dimension. Punishment mechanisms (institutional in Lim & Capraro; dynamic/static sanctions in Wang & Cui) are a central focus in both analyses.

**efficiency_or_related_payoff_outcome:**  
- The relevance is *exact* in Lim & Capraro (2022), as efficiency (mean payoff relative to optimal) is directly modeled. In Wang & Cui (2022), the relevance is *adjacent*; efficiency is not measured or analyzed, with the focus instead on non-payoff behavioral outcomes (compliance/self-discipline).

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes:**  
  - Only Lim & Capraro (2022) models and measures efficiency and mean group payoff as primary outcomes.

- **Non-Payoff Behavioral Outcomes:**  
  - Wang & Cui (2022) analyzes the proportion of compliant or self-disciplined agents, which reflects norm-following or cooperation rates but does not directly equate to efficiency or welfare.

- **Other Outcomes:**  
  - While both papers discuss the mechanisms and design dimensions that might influence group dynamics, only Lim & Capraro (2022) translates these into group-level payoffs.

# 4) Main Findings Relevant To Prediction

Synthesizing across papers, the most prediction-relevant findings are:

- **Institutional Punishment Increases Efficiency:**  
  - Enabling even modest levels of institutional punishment can lead to full cooperation and maximize efficiency in networked environments if coordinated with structured populations. In these conditions, punishment helps achieve average payoffs close to the theoretical maximum (Lim & Capraro, 2022).

- **Network Structure Moderates Punishment's Effect:**  
  - Efficiency gains from punishment are larger in structured (networked) populations than in well-mixed ones, and the necessary punishment threshold for full efficiency is lower with increased network structure (Lim & Capraro, 2022).

- **Punishment Cost and Overuse:**  
  - Once the critical threshold for inducing cooperation is reached, further increasing the level or intensity of punishment can reduce efficiency due to its costs (Lim & Capraro, 2022).

- **Mechanism Dynamics Matter:**  
  - Dynamic sanctioning (responding to observed behavior) is more effective at promoting compliance than static sanctions, suggesting the sophistication of the punishment mechanism affects behavioral compliance, though payoff effects are not directly reported (Wang & Cui, 2022).

- **Reward–Punishment Asymmetry:**  
  - Increased punishment intensity raises compliance, while stronger rewards can reduce compliance via moral hazard—potentially affecting group welfare, but this is not explicitly measured as efficiency (Wang & Cui, 2022).

# 5) Prediction Guidance

The literature provides the following guidance for predicting average efficiency when enabling peer punishment, conditioned on game dimensions and control-game efficiency:

- **Direct Prediction from Control Efficiency:**  
  - Where efficiency is low in the absence of punishment, enabling punishment likely increases efficiency, particularly in structured (networked) environments and where punishment cost is moderate (Lim & Capraro, 2022).

- **Key Moderators:**  
  - Efficiency gains are largest when:
    - *Network structure* increases local interaction (promoting mutual monitoring).
    - *Punishment cost* is not excessive.
    - *Punishment threshold* is sufficient to deter defection but not so high as to drain resources unnecessarily.
  - Overly costly or excessive punishment can reduce efficiency (Lim & Capraro, 2022).

- **Design Mechanisms:**  
  - More sophisticated (dynamic) sanctioning mechanisms are likely more effective at supporting efficiency than static ones, though this is inferred from behavioral outcomes rather than direct payoff data (Wang & Cui, 2022).

- **Generalizability:**  
  - These inferences are theory-derived and grounded in environments adjacent to, but not exactly matching, the standard PGG.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**  
- `player_count`: Included in both models; affects network structure and dynamics.
- `all_or_nothing`: Both models consider binary participation/effort frameworks.
- `mpcr` (marginal per-capita return): Explicit in Lim & Capraro.
- `punishment_cost`, `punishment_tech`: Both papers engage deeply with cost and mechanism/implementation details.
- `reward_exists`: Explored in Wang & Cui (whether rewards are present as an alternate/parallel institution).

**Indirectly Informed / Contextually Discussed:**  
- `num_rounds`: Only included as context in Wang & Cui; not central.
- `default_contrib`: Not discussed.
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id`, `chat`: Not discussed.
- `reward_cost`, `reward_tech`: Only as part of contrasting treatment in Wang & Cui.

**Missing or Sparse:**  
- Most informational, framing, and communication/messaging variables (`chat`, `show_n_rounds`, `show_other_summaries`, `show_punishment_id`) are not analyzed.
- Effects of stochastic punishment, visibility, or repeated interactions per se are largely absent.

# 7) Important Limitations

- **Theoretical, Not Empirical:**  
  - Both papers are purely theoretical, lacking empirical or experimental validation of predictions.

- **Adjacent to, Not Exact PGG:**  
  - The analytical environments are structurally similar but not identical to the canonical public goods game, limiting the precision of generalization.

- **Payoff Outcomes Underrepresented:**  
  - Only one paper (Lim & Capraro, 2022) models group efficiency directly; the other (Wang & Cui, 2022) offers only compliance/self-discipline rates.

- **Sparse on Key Design Features:**  
  - Critical design variables such as communication (chat), dynamic feedback (display of other’s behavior or identities), and many presentation or framing dimensions are missing.

- **No Evidence for Combined Reward–Punishment Effects on Efficiency:**  
  - The interplay of reward and punishment mechanisms is only partially theorized (behavioral effects only in Wang & Cui).

- **No Model of Peer Versus Institutional Punishment:**  
  - Findings are stronger for institutional punishment; the peer-punishment case commonly used in PGG experiments is not the main focus.

- **No Direct Mapping from Control Efficiency to Treatment Efficiency:**  
  - While theoretical conditions are described, the literature does not provide a formula or meta-analytic mapping from baseline (no-punishment) efficiency to the expected efficiency with punishment under variation in the 14 design dimensions.

---

**In sum:**  
This literature set provides conceptually valuable, general guidance on the efficiency effects of enabling punishment in public-goods-like settings, with strong theoretical support for the core effect and some analytical boundary conditions. However, predictive specificity for empirical PGGs and their many design variants remains limited by the lack of empirical calibration and the gaps regarding certain implementation dimensions and peer-punishment scenarios.
