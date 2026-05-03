# 1) Evidence Base

This paper set consists exclusively of theoretical contributions, with no empirical or experimental studies (Bowles & Gintis, 2004; Okada, 2020; KRAINES & KRAINES, 1993; Hagen & Hammerstein, 2006). The set covers a range of models addressing mechanisms that support cooperation and (in some cases) efficiency outcomes in social dilemmas, including public-goods-game-like environments, the iterated Prisoner’s Dilemma, and broader theoretical critiques. The literature base is relatively narrow for the purposes of predicting efficiency from design dimensions in actual PGG experiments; it provides mechanism-based arguments and simulated results but lacks direct, controlled, empirical evidence from true PGG studies.

# 2) Task Relevance

**pgg_or_variant:**  
- *Bowles & Gintis (2004)*: `close` – Models public-goods-game-like settings, though not strictly canonical PGGs.  
- *Okada (2020)*: `adjacent` – Focuses on indirect reciprocity and not PGGs, but considers social dilemmas.  
- *KRAINES & KRAINES (1993)*: `adjacent` – Explores iterated Prisoner’s Dilemma, not group-based PGGs.  
- *Hagen & Hammerstein (2006)*: `adjacent` – Critiques methods and interpretations in experimental games broadly, not specifically PGGs.

**punishment_or_sanctions:**  
- *Bowles & Gintis (2004)*: `exact` – Focuses directly on peer punishment.  
- *Okada (2020)*: `close` – Deals with punishment in a reputation/indirect reciprocity context.  
- *KRAINES & KRAINES (1993)*: `adjacent` – Discusses positive/negative payoffs as reinforcement, not explicit peer punishment.  
- *Hagen & Hammerstein (2006)*: `adjacent` – Discuss framing and implicit punishment cues, but not explicit mechanisms.

**efficiency_or_related_payoff_outcome:**  
- *Bowles & Gintis (2004)*: `exact` – Reports group efficiency as core outcome.  
- *Okada (2020)*: `adjacent` – Focuses on cooperation rates and norm stability, not efficiency/payoff.  
- *KRAINES & KRAINES (1993)*: `exact` – Payoff/efficiency in two-player games.  
- *Hagen & Hammerstein (2006)*: `adjacent` – Non-payoff outcomes only.

There is only one paper (Bowles & Gintis, 2004) which is *exactly* relevant on all three axes; the others offer indirect or mechanism insight, but not direct empirical or parameterized results for PGG efficiency with punishment.

# 3) Outcomes Measured In The Literature

- **Payoff-based Outcomes:**  
  - *Bowles & Gintis (2004)*: Group efficiency/average payoffs.  
  - *KRAINES & KRAINES (1993)*: Dyadic payoff tables and efficiency in iterated PD; does not extend to group or PGG settings.

- **Non-payoff Behavioral Outcomes:**  
  - *Okada (2020)*: Cooperation rates, norm stability, reputation dynamics.  
  - *Hagen & Hammerstein (2006)*: Framing effects, social cues, and cognitive processing; outcomes are about interpretation and behavior, not efficiency.

There is a clear distinction: Only Bowles & Gintis (2004) report outcomes that directly correspond to group efficiency as defined in the prediction target. Other papers focus on the mechanisms or behavioral correlates of cooperation (such as norm compliance or reciprocity), not total payoffs.

# 4) Main Findings Relevant To Prediction

Across this literature:

- **Costly peer punishment supports higher group efficiency:**  
  The strongest, most directly relevant finding is from Bowles & Gintis (2004), where agent-based simulations show that enabling peer punishment leads to a stable mix of strong reciprocators and selfish agents, significantly reducing shirking and raising group efficiency compared to settings without punishment. This result is robust across a range of group size, punishment costs, and marginal return parameters.

- **Effect is robust to design dimension variations (theoretically):**  
  In the Bowles & Gintis (2004) model, the positive efficiency effect of punishment holds across multiple values of the design dimensions that map onto player count, punishment cost, and marginal returns (MPCR).

- **Role of punishment structure and norm context:**  
  Okada (2020) provides theoretical arguments (not empirical evidence) that the structure of norms, the transparency of reputation, and rate of implementation errors moderate how effective punishment is at supporting cooperation; however, these insights pertain to indirect reciprocity games, not group PGGs, and are not quantified in terms of group efficiency.

- **Behavioral adaptation mechanisms suggest resilience in some repeated games:**  
  KRAINES & KRAINES (1993) show that adaptive learning strategies can maintain high efficiency in repeated dyadic games, but this does not involve peer punishment or group-level dynamics.

- **Framing and contextual cues can alter punishment and cooperation:**  
  Hagen & Hammerstein (2006) argue that contextual and framing factors not captured by standard game dimensions can significantly moderate behavior. However, there is no data or theoretical modeling of their impact on efficiency.

# 5) Prediction Guidance

**Direct evidence** in this set is limited to theoretical models, notably that of Bowles & Gintis (2004), which strongly supports the expectation that introducing peer punishment to a PGG-like environment will raise average efficiency compared to control. The relationship is robust to variations in basic structural parameters (group size, punishment cost, marginal per-capita return).

**However:**
- The evidence is not parameterized in a way that would enable fine-grained prediction across all 14 design dimensions.
- Literature on nuanced design features (e.g., chat, reward mechanisms, information disclosure) is missing, so predictions for games featuring those elements must interpolate or extrapolate cautiously.

**Indirect evidence** (from the other theory papers) suggests:
- The effectiveness of punishment is contingent on norm salience, error rates, and framing—factors not captured in the input dimensions.
- Adaptive strategies or implicit punishment can improve efficiency in two-player games, but generalizing this to group settings is unsupported.

In terms of **operational prediction**:
- If the control game (no punishment) shows low to moderate efficiency, and the only game change is enabling a peer punishment mechanism with non-prohibitive cost, theory predicts (Bowles & Gintis, 2004) a substantial increase in group efficiency.
- There is no direct theoretical or empirical evidence in this set about the *exact magnitude* of the efficiency gain—only that the direction is robust and positive across varied punishment schemes.

# 6) Design Dimensions Highlighted Across Papers

- **Directly informed dimensions:**  
  - `player_count`  
  - `num_rounds`  
  - `mpcr`  
  - `punishment_cost`

  (Bowles & Gintis, 2004) explore the robustness of the punishment effect to these dimensions in simulation.

- **Indirectly informed / contextually discussed:**  
  - `all_or_nothing` (Okada, 2020; KRAINES & KRAINES, 1993; theoretically discussed, not directly in PGG context)  
  - `punishment_tech` (Okada, 2020; only discussed as reputation/public vs. private, not operationalized for PGG)  

- **Effectively missing (no substantive discussion or parameter analysis):**  
  - `chat`  
  - `default_contrib`  
  - `reward_exists`, `reward_cost`, `reward_tech`  
  - `show_n_rounds`, `show_other_summaries`, `show_punishment_id`

  No paper in the set addresses information treatments, communication options, or reward mechanics.

# 7) Important Limitations

- **Absence of empirical or experimental evidence:**  
  All findings are theoretical or simulation-based; there is no observed data on actual player behavior in controlled PGG-with-punishment experiments.

- **Limited coverage of design space:**  
  Only core structural dimensions (player count, rounds, MPCR, punishment cost) are discussed in models. Information treatments, communication, default framing, reward/punishment technology, and visibility features are either omitted or only speculatively addressed.

- **Ambiguity in magnitude and conditionality:**  
  Theoretical predictions capture the directional effect of punishment but lack calibration for magnitude, and do not resolve how effect size varies with subtle variations in design or context.

- **Lack of direct operational mapping:**  
  No paper provides ready-to-use quantitative mappings from the full set of design parameters to efficiency changes under punishment.

- **Potential for contextual and framing moderators:**  
  As noted by Hagen & Hammerstein (2006), unmodeled effects from framing or social context may undermine the reliability of predictions based on structural game features alone.

- **Weak evidence for adjacent mechanisms:**  
  Indirect reciprocity models and adaptive learning mechanisms provide conceptual insight but cannot be confidently mapped to PGG efficiency predictions.

**In summary:**  
Predictions based on this literature should expect that enabling peer punishment in a PGG-like game with otherwise low to moderate control efficiency will increase group efficiency, especially as group size, round count, punishment cost, and MPCR have been theoretically tested for robustness. However, predictions for games involving additional social, informational, or technological features (such as chat, explicit reward systems, or information disclosure treatments) cannot be strongly justified based on this set alone. Empirical calibration and design-dimension coverage are both limited.
