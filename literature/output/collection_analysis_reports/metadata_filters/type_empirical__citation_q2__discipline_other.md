# 1) Evidence Base

The collected evidence comprises seven papers spanning both experimental and observational methodologies. Among these:

- **Experimental Empirical Papers (3):**  
  - Two lab experiments investigate close variants of public goods games (PGGs), focusing on cooperation mechanisms but varying in punishment inclusion (Brick & Visser, 2010; Zhang et al., 2019; Xiao & Bicchieri, 2012).
  - One field experiment focuses on third-party punishment in a market externality context (Rommel, 2015).

- **Observational Empirical Papers (4):**  
  - Three analyze real-world cooperation or policy dilemmas, with discussions of punishment or reward mostly at a conceptual or structural level, not via controlled experiments or direct measurement (Montoya et al., 2015; Johansson et al., 2003; Holubcik et al., 2023).
  - One paper analyzes how design choices and information affect allocation decisions in a dictator game, but without punishment (Xiao & Bicchieri, 2012).

**Breadth:** Overall, the set is broad in thematic scope (cooperation, sanctions, social dilemmas, organizational strategy), but narrow with respect to direct, empirical evidence about the impact of peer punishment on efficiency in classical PGG or close laboratory variants. Most evidence is either adjacent, indirect, or does not focus primarily on group payoff or efficiency.

# 2) Task Relevance

**PGG or Variant:**  
- Most papers are *close* or *adjacent* in modeling collective action, but only a subset use PGG or step-level PGG directly (Zhang et al., 2019; Brick & Visser, 2010). Some investigate related scenarios (markets with negative externalities, real institutional dilemmas).

**Punishment or Sanctions:**  
- Only **one** lab experiment directly implements sanctions/punishment, but as institutional/automatic (not peer) punishment (Brick & Visser, 2010).
- One field experiment directly examines costly (peer/third-party) punishment, but not in a PGG (Rommel, 2015).
- Several discuss punishment/reward conceptually or structurally, but without experimental manipulation (Montoya et al., 2015; Johansson et al., 2003).

**Efficiency or Related Payoff Outcome:**  
- Only **one** paper measures group efficiency or earnings explicitly (Zhang et al., 2019), but *without* punishment.
- One infers increased compliance with targets (and suggests improved group welfare) under sanctions but falls short of quantifying efficiency as a ratio (Brick & Visser, 2010).
- Others do not track efficiency or payoff outcomes.

**Summary:**  
- Core task relevance is limited: *exact* matches on all three axes (PGG, punishment, and efficiency) are missing. The closest evidence comes from variants or with partial overlap on these dimensions.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes:**  
  - *Directly measured efficiency:* Only Zhang et al. (2019) explicitly provides group efficiency; however, this is *without* punishment mechanisms.
  - *Inferred/adjacent payoffs:* Brick & Visser (2010) report compliance rates, which can be mapped to efficiency, but do not formally compute the payoff ratio.
  - *Other references:* Some studies mention "earnings," "economic surplus," or "competitiveness" (Zhang et al., Holubcik et al.), but these are either not in a controlled public goods setting or are not measured as a fraction of maximum group payoff.

- **Non-Payoff Behavioral Outcomes:**  
  - Norm compliance, cooperation choices, frequency of sanctions, market entry (Rommel, 2015; Brick & Visser, 2010), information-seeking about norms (Xiao & Bicchieri, 2012).
  - Surveyed attitudes toward sanctions, motivation for cooperation, and policy acceptability (Montoya et al., Johansson et al.).

**Distinction:** While several studies establish behavioral effects (norm compliance, contribution, sanctioning rates), these are distinct from directly measured efficiency.

# 4) Main Findings Relevant To Prediction

- **Punishment and Efficiency:**
  - *Sanction-based mechanisms (automatic/tax)* yield near-universal compliance with group targets in a step-level public good, far surpassing the efficacy of voluntary cooperation or communication alone (Brick & Visser, 2010). While efficiency is not directly measured, the high compliance implies strong gains in group payoff—though excess contributions above the target can be crowded out.
  - *Peer/third-party punishment* in market-like settings strongly deters norm violation (harmful market entry), showing high willingness to pay for punishment and substantial behavioral shifts (Rommel, 2015). *Efficiency* is not computed, so payoff-based predictive value is indirect.

- **Mechanisms Without Punishment:**
  - *Consistent contributors* boost group efficiency and earnings, demonstrating that motivational or role-model interventions can drive high efficiency absent punitive mechanisms (Zhang et al., 2019).

- **Qualitative/Theoretical Support:**
  - Observational and theory-informed papers reinforce that sanction and reward systems help sustain cooperation, especially in large-scale or institutional settings, but do not provide empirical evidence specific to efficiency impacts in game-like scenarios (Montoya et al., 2015; Johansson et al., 2003).

- **Behavioral Outcomes Dominating:**
  - Across punishment-related contexts (except Zhang et al., 2019), most reported effects are on compliance, cooperation, entry rates, or norm adherence, not directly on group efficiency or total payoff.

- **Ambiguity/Caveats:**
  - Compulsory sanctioning may crowd out voluntary above-target contributions, with this effect varying by player type (Brick & Visser, 2010).
  - Peer punishment is effective at deterring violation, but the effect on overall surplus depends on costs of punishment and on how “deterrence” is balanced by the loss from punishers' cost outlays.

# 5) Prediction Guidance

Given this evidence:

- **General Expectation:**  
  The literature suggests that introducing *sanctions* (including punishment) nearly universally increases compliance with contribution targets in PGG-like settings, and implies substantial improvements in group welfare and efficiency *relative to voluntary/cooperation-only baselines* (Brick & Visser, 2010). However, this is best established for *institutional* (automated) sanctions, with less direct evidence for *peer* punishment.

- **Quantitative Prediction:**  
  Precise quantitative predictions of efficiency change are *not* supported by this literature, given the rarity of direct efficiency measurement in the punishment condition.

- **Control Efficiency as Baseline:**  
  Where control efficiency (no punishment) is low and voluntary cooperation insufficient, enabling sanctions is likely to yield dramatic efficiency gains, approaching target compliance levels (Brick & Visser, 2010). In settings with high baseline efficiency, the marginal gain may be less pronounced, and possible crowd-out of voluntary excess contributions may occur.

- **Role of Game Design Dimensions:**  
  The effect of punishment appears robust to heterogeneity of player type (capital/labor distinction), and communication supports but does not supplant the effect of sanctions (Brick & Visser, 2010). Motivational interventions (role models) can also yield meaningful increases in efficiency even *without* punishment (Zhang et al., 2019).

- **Peer vs. Institutional Sanctions:**  
  The direct transferability of findings from institutional to peer punishment is uncertain; peer punishment can be costly and may introduce efficiency losses if punishment is excessive or misdirected (Rommel, 2015; theory by analogy). No direct group efficiency measurements with peer punishment are supplied.

- **Summary Prediction Guidance:**  
  The set supports the *qualitative* prediction that efficiency will rise when peer punishment is enabled (especially from a low-control-efficiency baseline), but does not enable detailed, dimension-specific or quantitative prediction.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed (manipulated or directly analyzed):**
- `player_count` (several experiments)
- `num_rounds` (experiments)
- `chat` (communication allowed or manipulated)
- `all_or_nothing` (step-level or continuous contribution forms)
- `mpcr` (public good multiplier per player, at least in lab experiments)
- `punishment_cost` (explicit in punishment studies)
- `punishment_tech` (type of punishment: institutional/automatic or third-party/peer)
- `reward_exists` (presence/absence)
- `show_n_rounds` (information availability)
- `show_other_summaries` (feedback information)

**Indirectly or contextually discussed:**
- `reward_cost`, `reward_tech`, `default_contrib` (framing or treatment in some studies, but not directly measured in terms of efficiency or punishment effect)
- `show_punishment_id` (not manipulated, but identity/observability sometimes relevant in discussions)

**Effectively missing:**
- No study directly manipulates `default_contrib`, `reward_cost`, `reward_tech`, `show_punishment_id` with reported effects on efficiency when punishment is enabled.
- Peer punishment is implemented only in a market/trader context (Rommel, 2015), not in a classic PGG.

# 7) Important Limitations

- **Lack of Direct Efficiency Evidence:**  
  The central gap is an absence of direct experimental measurement of *group efficiency* (payoff ratio) under both *control* (no punishment) and *peer punishment* in a PGG design with full measurement of relevant dimensions. Most findings are inferred from compliance rates or adjacent outcomes.

- **Focus on Institutional, Not Peer, Punishment:**  
  The strongest evidence for positive effects of punishment derives from *institutional/automatic* sanctions, not *peer* punishment—the target of the prediction task.

- **Limited Quantitative Comparisons:**  
  No papers in the set supply before/after (control/treatment) efficiency data suitable for direct modeling or prediction; most control conditions involve alternative interventions (communication, role models) rather than a no-punishment baseline.

- **Sparse Coverage of Prediction Dimensions:**  
  While some design dimensions are manipulated (e.g., player count, rounds, communication), others critical to nuanced prediction (punishment/reward framing, identification, default contribution) are missing or only contextually referenced.

- **Predominance of Non-Payoff Outcomes:**  
  Several studies focus on behavioral indicators of cooperation or norm compliance, not on the actual welfare gains or total payoff impacts; translation between these requires caution.

- **Contextual/Structural Differences:**  
  Adjacent studies differ in underlying game structure (market externalities, public policy coordination) or observational focus, limiting direct transferability.

- **Theoretical/Normative Papers Lack Experimental Validation:**  
  Observational results and theory provide suggestive but non-causal support for sanctions boosting cooperation; they lack empirical evidence on efficiency.

**In conclusion**, while the literature provides contextual and indirect support for the predictive relationship that enabling punishment increases efficiency in public-goods-game-like environments (especially when baseline efficiency is low), it falls short of enabling detailed, design-dimension-specific, or quantitative prediction for peer punishment based on control efficiency and game parameters.
