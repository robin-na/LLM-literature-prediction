# 1) Evidence Base

**Mix of Papers:**  
The evidence base is composed entirely of theoretical and computational papers; no empirical or laboratory experiments are included.

**Breadth and Depth:**  
The paper set is broad, encompassing a large number of diverse, mainly theoretical models directly addressing public goods games (PGG) or their close variants with punishment. Many models are high-resolution, specifying detailed payoff and strategy dynamics. However, most examine mechanisms and parameter conditions rather than reporting experimental or real-world effect sizes.

**Empirical Status:**  
All findings are based on mathematical analysis or agent-based simulations; none report new data from human or animal participants.

**Model Focus:**  
Most papers target canonical public goods games, sometimes extending to common-pool resource (CPR) games, voluntary participation, reputation systems, network structure, and “adjacent” games (e.g., iterated Prisoner’s Dilemma, trust games).

**Summary:**  
Theoretical evidence is rich and extensive for the structure and potential effects of punishment in PGG-like environments. The research base is strong on mechanism, prediction formulas, and mapping design dimensions to expected outcomes but lacks empirical calibration.

---

# 2) Task Relevance

**A. pgg_or_variant:**  
Most included papers have `pgg_or_variant` relevance labeled as `exact` for the prediction task: these primarily model standard public goods games with or without punishment. A substantial minority cover adjacent settings (`close`: CPR games, trust games, iterated PD, group-forming, leader-driven, or reputation-based collective action), which are similar but may differ in institutional or ecological structure. Some papers address only loosely related domains.

**B. punishment_or_sanctions:**  
Punishment or sanctions are typically modeled explicitly, with most papers at `exact` relevance—they manipulate the presence, form, cost, and/or magnitude of punishment. Several also consider reward (with reward_*) or hybrid punishment-reward mechanisms, or include indirect/chimeric forms (exclusion, ostracism, reputation loss).

**C. efficiency_or_related_payoff_outcome:**  
About half of the PGG+punishment papers deliver `exact` relevance by modeling efficiency, average group payoff, welfare, or total earnings directly as the dependent variable. The remainder focus mainly on behavioral outcomes like cooperation rate, strategy prevalence, or norm compliance—sometimes drawing inferences about efficiency but not measuring it explicitly.

**Summary Table:**  
| Dimension                    | Exact | Close | Adjacent | Weak | None |
|------------------------------|-------|-------|----------|------|------|
| pgg_or_variant               | High  | Moderate | Significant | Some | Rare |
| punishment_or_sanctions      | High  | Moderate | Significant | Some | Rare |
| efficiency_or_related_payoff | Moderate | Moderate | Significant | Notable | Occasional |

---

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes (Relevance: high for prediction):**
- **Efficiency**: Defined as group total payoff relative to the full-cooperation optimum, is a primary outcome in numerous models (e.g., Levine & Modica, 2016; Hwang & Bowles, 2012; Li et al., 2022; Sun et al., 2023; Dong et al., 2019; Garcia & Traulsen, 2012; Bednar, 2006; Deng et al., 2012; Vasconcelos et al., 2015).
- **Total/average group payoff, welfare, surplus, coins generated**: Alternate terms for efficiency, often the key dependent variable (e.g., Gao et al., 2020; Oya & Ohtsuki, 2017; Wang et al., 2010; Dejong et al., 2008; Wang et al., 2024).
- **Regime classification (efficient/inneficient equilibria, phase diagrams, or fixation probabilities)**: Quantified in some evolutionary models.

**Behavioral (Non-Payoff) Outcomes:**
- **Cooperation/contribution rate**: The most-commonly reported behavioral outcome; often used as a proxy but not identical to efficiency.
- **Punishment frequency, prevalence, or intensity**
- **Strategy frequencies**: Prevalence of punishers, cooperators, defectors, excluders, etc.
- **Norm compliance, ostracism, exclusion/initiation**
- **Structural features**: Clustering, specialization, or role adoption in networks.

**Linkage:**  
Some “behavioral outcome” models provide payoff-based post-processing (e.g., Wang et al., 2010), while others explicitly distinguish between cooperation prevalence and actual monetary/group payoffs. Several warn that increased cooperation via punishment may not always improve efficiency due to high punishment costs or antisocial punishment (Shinada & Yamagishi, 2008; Oya & Ohtsuki, 2017).

**Conclusion:**  
While many models put behavioral outcomes at the forefront, a substantial set delivers explicit efficiency or payoff measures—directly relevant to the downstream prediction task. However, not all behavioral improvements (or declines) translate to efficiency gains.

---

# 4) Main Findings Relevant To Prediction

## Synthesis of Cross-Paper Findings

**A. Punishment Often Raises Efficiency, But Conditional on Moderators**

- **Enabling punishment in standard PGGs generally increases group efficiency** (Levine & Modica, 2016; Eldakar et al., 2007; Dejong et al., 2008; Sigmund et al., 2011; Wang et al., 2024; etc.), but **the size and even the sign of the effect depend on game design details**.

**B. Critical Design Moderators (Backed by Efficiency Analysis)**
- **Group/Player count**: Increases in group size can make it harder for punishment to raise efficiency unless mechanisms for coordination, observability, or leader/institutional punishment are present (Levine & Modica, 2016; Wang et al., 2024; Vasconcelos et al., 2015; POLLOCK, 1988).
- **Number of rounds**: More rounds increase the scope for punishment to sustain cooperation and efficiency; one-shot or very short games see little effect (Eldakar et al., 2007; Bednar, 2006).
- **MPCR (Marginal per-capita return)**: Punishment is more likely to increase efficiency when MPCR is higher; with low MPCR, punishment costs may outweigh gains (Shinada & Yamagishi, 2008; Hwang & Bowles, 2012).
- **Punishment cost and tech (fine-to-fee ratio)**: Net efficiency gain from punishment is greater when the cost to punishers is low and/or fines are high. If punishment is too costly, it can reduce efficiency even as cooperation rises (Shinada & Yamagishi, 2008; Dorrough et al., 2017; Dong et al., 2019; Bednar, 2006).
- **Punishment effectiveness/modality**: Probabilistic, rare-but-severe, or coordinated punishment outperforms always-on, individual, or weak punishment in efficiency impact (Jiao et al., 2020; Deng et al., 2012; Ohdaira, 2022).
- **Institutional vs. peer punishment**: Institutional punishment (when honest and visible) often leads to higher efficiency than decentralized peer punishment (Gavrilets & Shrestha, 2021; Saak, 2012), but can backfire if corruption or antisocial punishment emerges (Lee et al., 2015; Lee et al., 2019).
- **Reward and hybrid mechanisms**: Several papers report that reward-only or combined reward/punishment can outperform punishment-only in maintaining high efficiency, especially when monitoring is noisy or errors are prevalent (Dong et al., 2019; Okada et al., 2020; Han, 2022; Wang et al., 2022).
- **Monitoring, auditing, observability**: Higher quality of monitoring, identity revelation, and effective observability amplify the positive efficiency impact of punishment (Bednar, 2006; García & Traulsen, 2019; Saak, 2012).
- **Communication (chat/gossip)**: Communication enhances norm formation and the effectiveness of punishment in sustaining efficiency (Janssen, 2015; Frey & Burgess, 2023; Molho & Wu, 2021), though not always modeled with direct efficiency outputs.
- **Second-order free rider problem**: Models stress that, without mechanisms to compensate or reward punishers, costly punishment may fail to improve efficiency due to decaying punisher prevalence (Ye et al., 2011; Sigmund et al., 2011).
- **Corruption and antisocial punishment**: If the punishment institution can be corrupted (accept bribes or misapply punishment), or if antisocial punishment is prevalent, enabling punishment can reduce or fail to improve efficiency (Lee et al., 2019; Powers et al., 2012).
- **Heterogeneity of preferences/players**: High levels of unconditional altruism, strong norm-following, or heterogeneity in punishment cost/effectiveness can neutralize or invert the efficiency effects of punishment (Hwang & Bowles, 2012; de Weerd & Verbrugge, 2011).
- **Population/network structure**: Population structure (localized interaction, regular graphs, spatial structure) often makes punishment more potent for efficiency (Sun et al., 2023; Wang et al., 2024; Oya & Ohtsuki, 2017; POLLOCK, 1988).
- **Complementary or substitutive mechanisms**: In some parameter regimes, reputation, exclusion, or sufficiently strong social norms can achieve high efficiency without need for monetary punishment (Benchekroun & Van Long, 2008; Nakamaru & Yokoyama, 2014; Smaldino & Lubell, 2014).

**C. Negative or Mixed Effects of Punishment on Efficiency**
- Punishment sometimes increases cooperation but reduces efficiency due to high cost or retaliation (Shinada & Yamagishi, 2008; Han et al., 2024).
- Institutional punishment without taxpayer compensation for punishers can fail or reduce efficiency (Ye et al., 2011).
- Corrupt enforcement undermines the efficiency benefit of punishment (Lee et al., 2015; Lee et al., 2019).
- Excessive or poorly targeted punishment (e.g., in the presence of misidentification, error, or antisocial punishment) can lead to lower group surplus (van der Weele, 2012; Powers et al., 2012; Thöni, 2014).

**D. Dependence on Baseline (Control) Efficiency**
- If the control (no-punishment) efficiency is already high due to social preferences, reputational concerns, or other incentives, enabling punishment may yield no additive benefit—or could even crowd out pre-existing motives and reduce efficiency (Hwang & Bowles, 2012; Orr, 2001; van der Weele, 2012).

**E. Mechanistic and Quantitative Links**
- Several models provide explicit formulas or parameter thresholds for treatment-group efficiency as a function of game design dimensions and control efficiency (Levine & Modica, 2016; Li et al., 2022; Sun et al., 2023; Zhang et al., 2020). Some supply phase diagrams showing regions of positive, neutral, or negative punishment effects.

---

# 5) Prediction Guidance

**Overall Guidance:**

- **Punishment generally increases efficiency in public goods games, provided it is not prohibitively costly and is sufficiently effective at deterring defection.** However, the effect size—and even the sign—depends critically on game design dimensions and baseline (control game) efficiency.

**Dimension-Specific Instructions:**
- **Player count**: Positive efficiency impact more likely for smaller groups unless institutional punishment (with honest, observable enforcement) or strong network structure is present; in large groups, unless institutions solve the second-order free rider or coordination problem, punishment’s effect is diluted.
- **Num rounds**: More rounds increase the scope for efficiency gains from punishment, especially in repeated settings.
- **Punishment cost/punishment tech**: The fine-to-fee or impact-to-cost ratio is a key moderator. Efficiency gains require that the punitive cost is not so high as to offset increased cooperation. Models allow for explicit calculation using these parameters.
- **MPCR**: Low MPCR environments are more brittle to punishment; high MPCR makes efficient outcomes more likely with punishment.
- **Reward exists**: If effective reward exists as an alternative to punishment, reward may sometimes be equally or more efficient; the effect depends on whether the reward and punishment are optimally tuned and whether monitoring is reliable.
- **Chat (communication)**: Where present, expect higher norm compliance and increased effectiveness of any punishment mechanism, indirectly improving efficiency.
- **Show_n_rounds/Show_other_summaries/Show_punishment_id**: Transparency and observability increase the deterrence power of punishment, thus amplifying its positive effect on efficiency.
- **All or nothing, default contrib**: Contribution granularity and framing can affect baseline (control) efficiency but are less often a primary moderator for punishment's marginal effect.
- **Reward cost, reward tech, reward magnitude**: When combined with punishment, these serve as secondary moderators; high reward effectiveness can substitute for punishment under some conditions or make hybrids optimal.
- **Punishment tech**: Mode and accuracy of punishment (peer, institution, probabilistic, adaptive, etc.) is a core moderator; effective, well-targeted, and observable punishment is most likely to yield strong efficiency gains.

**Use of Control Efficiency:**
- **Conditional Effect**: If the control game is already efficient due to strong social preferences, reputation, or direct reciprocity, incremental benefit of punishment may be limited or negative; if control efficiency is low, the introduction of punishment is more likely to yield substantial efficiency gains.

**Boundary Conditions:**
- If corruption, antisocial punishment, or misapplied sanctions are likely or cannot be prevented, enabling punishment may not improve—and may reduce—treatment efficiency.
- In games allowing for non-punitive exclusion (ostracism) instead of costly punishment, efficiency gains from enabling exclusion may exceed those from punishment.

---

# 6) Design Dimensions Highlighted Across Papers

**Dimensions with Direct, Strong Theoretical/Modeling Support:**
- `player_count`
- `num_rounds`
- `mpcr`
- `punishment_cost`
- `punishment_tech` (effectiveness, mode, coordination)
- `reward_exists` (and interactions with punishment)
- `show_n_rounds`
- `show_other_summaries`
- Population/network structure (though not always parameterized as a standard dimension)

**Dimensions with Indirect, Partial, or Contextual Evidence:**
- `all_or_nothing`, `default_contrib`: Affected control efficiency; moderate effect on marginal value of punishment.
- `reward_cost`, `reward_tech`, `reward_magnitude`: Mostly via studies on reward vs. punishment hybrids or alternatives—relevant when both options are considered.
- `chat`: Mechanistically influential but less often directly quantified for payoff outcomes.

**Dimensions Rarely/Missing/Sparingly Discussed:**
- `show_punishment_id`: Occasionally mentioned, mainly in context of observability or reputation effects, but not as a primary moderator of efficiency.
- Enforcement transparency, corruption potential (`reward`/`punishment` administered by honest vs. corrupt agents): Discussed in some models (Lee et al., 2015, 2019), but not always as a standard design variable.

---

# 7) Important Limitations

- **Empirical Calibration Is Lacking:** The entire paper set is theoretical. There are no empirical data or experimental effect sizes to validate the size of efficiency changes found in models.
- **Generality vs. Specificity:** High generalizability and mechanistic explanation, but low context sensitivity—real-world variation in behavioral noise, institutional stability, social preferences are not empirically tested in this set.
- **Payoff Conversion Assumptions:** Many models infer efficiency from increased cooperation without always accounting for the net costs of punishment; some that do (Shinada & Yamagishi, 2008; Han et al., 2024) find that increased cooperation does not always translate to increased efficiency.
- **Population Structure Effects:** Numerous findings may not generalize from well-mixed to structured populations or vice versa (networked vs. random-matching settings), and the mapping from structural features to standard game design dimensions may not be 1:1.
- **Behavioral Outcomes Misapplied:** A large fraction of the broader literature reports only behavioral outcomes (cooperation, norm compliance) rather than efficiency; incorrect translation of these findings may lead to overestimation of punishment’s positive impact on efficiency.
- **Edge Cases (Corruption, Anti-Social Punishment, Strong Social Preferences):** Models show that in the presence of antisocial punishment, corrupt institutional enforcement, or highly altruistic subject pools, punishment can reduce efficiency or fail to improve it.
- **Parameter Mapping:** For some dimensions (especially nuanced punishment/reward technology, exclusion, or identity-revelation), model treatments vary and mapping to real-world interventions or experimental parameterizations is approximate.
- **No Direct Evidence on Some Dimensions:** Some design dimensions (e.g., `chat`, `all_or_nothing`, `default_contrib`, `show_punishment_id`) are not systematically varied or are only contextually discussed, limiting exact prediction.

---

**In sum:**
- The paper set gives strong, multi-model theoretical evidence that punishment in PGGs will usually—but not always—improve efficiency, depending on key design parameters (group size, rounds, MPCR, punishment cost/effectiveness, presence of reward, observability, monitoring, and institutional integrity).
- Several robust boundary conditions are identified: high cost punishment, corrupt or antisocial enforcers, or contexts with high baseline efficiency can nullify or reverse the efficiency gain from punishment.
- All guidance for effect size, thresholds, or direction is rooted in theoretical/computational results, not validated by direct experimental or empirical findings. Extensive caution is warranted in generalizing model outcomes to lab experiments or field interventions.
