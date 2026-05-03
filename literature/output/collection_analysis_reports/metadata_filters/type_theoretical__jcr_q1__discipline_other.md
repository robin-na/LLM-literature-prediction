# 1) Evidence Base

The literature base is broad in conceptual scope but theory-oriented and largely simulation/modeling-based; empirical and experimental results are referenced mainly via meta-surveys or as motivating evidence rather than in new data. Of the 41 papers, most are theoretical, focused on public goods games (PGGs), variants, or adjacent dilemmas, and very few report original or meta-analytic outcomes on group efficiency or payoff following the introduction of punishment. Several papers deliver robust, parameterized models closely matching PGG constructs (e.g., Vasconcelos et al., 2022; Frey & Rusch, 2012; Liu et al., 2019), and a minority provide summary syntheses or mechanism-based arguments grounded by experimental patterns (Kraak, 2011). The paper set includes both exact matches and indirectly relevant models (e.g., exclusion or reputation-based punishment, coordination games, trust games, networked sharing, etc.), with varying proximity to the prediction task. Overall, this literature base is moderately comprehensive regarding theoretical possibilities for punishment effects, but is relatively thin on direct empirical, design-dimension-crossed evidence for changes in efficiency when peer punishment is enabled.

# 2) Task Relevance

**PGG or variant (`pgg_or_variant`):**  
- Relevance is **exact** in several key papers explicitly analyzing standard or spatial public goods games (e.g., Vasconcelos et al., 2022; Rosas, 2008; Frey & Rusch, 2012; Kraak, 2011; Liu et al., 2019).  
- Many papers are **adjacent** (prisoner's dilemma, trust games, threshold games, networked cooperation), providing analogous insight but with different payoff and informational structures.  
- A subset focus on broader collective action dilemmas (**close**) or coordination games (e.g., Vanderschraaf, 2016).

**Punishment or sanctions (`punishment_or_sanctions`):**  
- Most theory work is **exact** or **close** for inclusion of punishment, modeling both peer and institutional punishment constructs.  
- Some articles focus on alternative or adjacent sanctioning forms (exclusion, reputation, rewards), with **adjacent** or **close** relevance.  
- Several papers are critique-oriented or discuss punishment mechanisms contextually, rather than through explicit modeling (**adjacent** or **weak**).

**Efficiency or related payoff outcome (`efficiency_or_related_payoff_outcome`):**  
- Only a minority measure efficiency or payoff directly (**exact** match: Vasconcelos et al., 2022; Liu et al., 2019; Frey & Rusch, 2012; Zhang & van der Schaar, 2013; Xu et al., 2014; Bicchieri et al., 2004; O'Connor, 2016; Li & Jiang, 2023).  
- Several others (**close**/**adjacent**) infer efficiency from behavioral or success proxies (group success, rate of collective achievement) or from modeled welfare metrics (Quan et al., 2023; Vasconcelos et al., 2013).  
- Many model or discuss only cooperation rates, strategy frequency, norm compliance, or similar **non-payoff behavioral outcomes**, providing **adjacent** or **weak** relevance for efficiency prediction.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes**:  
    - Efficiency (group payoff normalized to full cooperation): Directly measured or simulated in a small subset (Vasconcelos et al., 2022; Liu et al., 2019; Frey & Rusch, 2012; Zhang & van der Schaar, 2013; Xu et al., 2014; O'Connor, 2016; Li & Jiang, 2023).
    - Group/average payoff, welfare, surplus, social welfare: Used as proxies for efficiency, e.g., average fitness in evolutionary models.
    - Total earnings or coins: Sometimes reported or discussed in support of group-level outcomes.

- **Non-payoff behavioral outcomes**:  
    - Contribution/cooperation rate, frequency of cooperation or defectors.
    - Punishment frequency and target selection.
    - Norm compliance, exclusion rates, detection of cheaters.
    - Group achievement in threshold games (e.g., avoiding catastrophe).

The distinction is explicit in some sources (e.g., Quan et al., 2023, Zhu et al., 2020: cooperation, not efficiency), and several caution that increased cooperation can mask stable or declining efficiency due to over-punishment or strategic mimicking (Goodman, 2023).

# 4) Main Findings Relevant To Prediction

- **Enabling punishment usually increases efficiency, but only under key conditions.**  
  - When punishment is **well-calibrated** and institutionalized at the right scale (local for local goods, collective for global goods), efficiency increases (Vasconcelos et al., 2022).  
  - Direct costly punishment may reduce or even harm efficiency if punishment is frequent, overused, or mis-targeted (Rosas, 2008; Frey & Rusch, 2012).  
  - **Time horizon** is critical: Short games (few rounds) often show initial efficiency losses from punishment (due to incurred costs), but in longer and stable-group games, declining need for punishment means efficiency can surpass the no-punishment baseline (Frey & Rusch, 2012).

- **Type and technology of punishment matter.**  
  - **Exclusion-based and reputation-based** sanctions confer higher, more stable efficiency than direct costly punishment, especially when defectors are reliably detected and cannot exploit the system (Rosas, 2008; Liu et al., 2019; Quan et al., 2023; Zhang & van der Schaar, 2013).
  - **Peer punishment** is more effective than pool punishment for driving cooperation in spatial contexts (Zhu et al., 2020), though outcomes are reported as cooperation rates.

- **Group and information structure modulate punishment's impact.**
  - **Stable, smaller groups** with communication, transparency, and longer memory/information produce stronger positive effects of punishment on efficiency (Vasconcelos et al., 2022; Kraak, 2011; Frey & Rusch, 2012).
  - **Learning environments** with clear feedback and information sharing facilitate institution adoption and efficiency improvements.
  - **Reputation, communication, and reward** mechanisms, when combined with punishment, amplify efficiency improvements over punishment alone (Kraak, 2011; Raihani & Aitken, 2011).

- **Evidence from adjacent models is broadly supportive but less specific for quantitative prediction.**
  - Trust, coordination, and networked sharing models consistently find that repeated play, effective conditional strategies, and well-calibrated sanctions shift populations toward more efficient, cooperative states (Bicchieri et al., 2004; Vanderschraaf, 2016; Xu et al., 2014).
  - Several highlight that excessively high punishment costs or weak detection mechanisms can blunt or reverse the efficiency benefits (Quan et al., 2023; Frey & Rusch, 2012).

- **Over-punishment, undetectable defection, and antisocial punishment can undermine efficiency.**  
  - Models where punishment is not well-targeted (over-punishment when most are cooperating; undetectable/covert defection) suggest apparent behavioral cooperation may not map to increased efficiency (Goodman, 2023), and that design features exposing or constraining these behaviors affect efficiency impacts.

# 5) Prediction Guidance

- **Main guidance**:  
  - **If the control (no-punishment) game is inefficient and the design allows repeated interactions, stable groups, and effective, reasonably low-cost punishment, enabling peer punishment will likely increase average group efficiency.**
  - The magnitude of improvement depends on: match between punishment scale and public good, clarity and cost-effectiveness of the punishment technology, group/stage length, and the availability of communication and learning.

- **Moderators for prediction**:  
  - **Game length/number of rounds (num_rounds)**: Short games may see reduced or no efficiency gains due to upfront punishment costs; long games allow for stabilization and efficiency improvement.
  - **Player count (player_count)**: Smaller, stable groups are more likely to benefit efficiently from punishment; large, fluid groups require institutionalization and/or formal third-party mechanisms.
  - **Punishment tech and cost (punishment_tech, punishment_cost)**: Exclusion or reputation-based systems typically yield higher efficiency than costly, direct punishment; fine/cost ratio is critical.
  - **Information/feedback (show_other_summaries, show_punishment_id)**: Visibility of contribution and punishment history supports effective targeting, learning, and efficiency.
  - **Communication and reward (chat, reward_exists, reward_cost, reward_tech)**: Communication and complementary rewards further enhance efficiency impacts.
  - **Alignment of institution and good**: Punishment institutions matched to problem scale are more effective (Vasconcelos et al., 2022).

- **Caution**:  
  - If the design permits undetectable defection, high antisocial punishment, or poorly calibrated punishment costs, predicted efficiency gains may be attenuated or negated.
  - Control efficiency that is already high may see limited or negative changes from adding punishment, especially if punishment is overused or unnecessary (Rosas, 2008).

- **Where only cooperation rate is reported**: Recognize that increases in cooperation do not always imply increased efficiency, especially if punishment is excessively or inefficiently deployed.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions:**  
- **player_count, num_rounds, mpcr, punishment_cost, punishment_tech, show_other_summaries**: Explicitly modeled and/or parameterized in several theory/exact PGG papers (Vasconcelos et al., 2022; Rosas, 2008; Frey & Rusch, 2012; Quan et al., 2023; Liu et al., 2019; Zhang & van der Schaar, 2013; Xu et al., 2014).
- **chat, all_or_nothing**: Discussed or manipulated in some models (Kraak, 2011; Quan et al., 2023; Vasconcelos et al., 2013; Bicchieri et al., 2004).
- **reward_exists, reward_cost, reward_tech**: Less frequently manipulated, but their joint presence (with punishment) is identified as amplifying efficiency (Kraak, 2011; Raihani & Aitken, 2011; Li & Jiang, 2023).

**Indirectly informed/contextually discussed:**  
- **default_contrib**: Rarely isolated, but choice architecture (opt-in/opt-out) implied in models of default behavior.
- **show_n_rounds, show_punishment_id**: Occasionally modeled or discussed to illustrate information/environmental conditions (Goodman, 2023; Mameli, 2013).

**Effectively missing from parameterized analysis:**  
- **Some visibility and framing parameters** (default_contrib, show_n_rounds, show_punishment_id), and certainly **fine-grained reward dimensions** are sparsely addressed, typically only contextually rather than through systematic variation.

# 7) Important Limitations

- **Empirical data scarcity on direct efficiency outcomes:**  
  - Few papers report real or simulated efficiency or group payoff values for both punishment-enabled and control games, reducing capacity for quantitative extrapolation to new designs.

- **Heavy reliance on theory and simulation:**  
  - Many conclusions are model-based, with outcomes depending on specific assumptions about update rules, parameter space, or population structure.
  - Translation from infinite or idealized populations to finite/human lab groups is uncertain, and model-dependent results may not generalize across experimental institutional details.

- **Outcome conflation risk:**  
  - Many sources report only cooperation rate or norm compliance, not efficiency/payoff; prediction must carefully distinguish these to avoid misattribution.

- **Moderators not always independently manipulable:**  
  - Many design dimensions are correlated in published work (e.g., long-duration games often have small, stable groups); interaction effects may be underidentified.

- **Sparse attention to framing, information, and visibility dimensions:**  
  - Framing, default contribution, and rounds/identity visibility are minimally addressed as direct moderators, though inferred to matter through mechanism arguments.

- **Adjacent games and mechanisms:**  
  - A substantial share of cited theoretical or adjacent-game work (e.g., PD, trust/reward/bystander mechanisms) may not map quantitatively onto PGG efficiency effects, especially regarding peer punishment.

- **Conflicting results and contextual dependencies:**  
  - Some models predict negative, null, or ambiguous effects for punishment (over-punishment, ineffectiveness in the presence of covert defectors, costs exceeding benefits), underscoring context sensitivity and the need to incorporate detailed design and context when predicting efficiency changes.

**In sum**, the literature strongly supports the idea that enabling effective, well-designed peer punishment mechanisms increases group efficiency in public goods games, but this effect is highly contingent on punishment cost/effectiveness, group and game structure, time horizon, and information environment. Prediction should rely on these contextual moderators, emphasize outcome distinctions, and recognize uncertainty due to theory-heavy evidence and limited empirical/parameterized data.
