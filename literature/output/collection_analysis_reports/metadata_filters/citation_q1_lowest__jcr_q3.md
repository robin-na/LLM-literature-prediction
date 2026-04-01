# 1) Evidence Base

The evidence base is large (110 papers), methodologically diverse, and covers a broad range of experimental, theoretical, simulation, and conceptual work. There is a strong empirical core of laboratory experiments in standard public goods games (PGG) and close variants, augmented by a deep theoretical literature on social dilemmas, punishment, and efficiency. Many papers are directly relevant—especially experimental studies with explicit punishment treatments and clear payoff-based efficiency outcomes (e.g., Chen, 2022; Sparks et al., 2024; Hou et al., 2019; Lippert & Tremewan, 2021; van Klingeren & Buskens, 2024). Others are only adjacent, dealing with variants (such as CPR games, IPD, or contest settings), mechanism design, or the evolutionary logic of punishment.

Empirical work is strongly represented, especially laboratory studies with monetary stakes, but there is also significant conceptual and theoretical modeling (e.g., Greenwood, 2018; Prétôt et al., 2024). Numerous papers are adjacent—covering related games or hybrid mechanisms—while others are only contextually informative or non-relevant for efficiency prediction.

The literature set offers direct empirical benchmarks, general quantitative mechanisms, and a wide array of moderators that map well onto the 14 design dimensions, though some design aspects remain underexplored in payoff terms. Notably, efficiency outcomes (payoff-based, group welfare) are reported in a substantial number of papers, whereas many others focus on non-payoff behavioral outcomes (contribution, cooperation, punishment frequencies) or on conceptual mechanisms without empirical payoff data.

---

# 2) Task Relevance

**pgg_or_variant**:  
- *exact*: There is substantial representation of exact repeated public goods games—many with standard designs matching the prediction task (e.g., player_count, num_rounds, mpcr as in Sparks et al., 2024; Hou et al., 2019; Chen, 2022).
- *close*: A robust set of studies use close variants, including common-pool resource games, binary/all-or-nothing dilemmas, and repeated IPDs (e.g., van Klingeren & Buskens, 2024; Zhosan & Gardner, 2013).
- *adjacent*/*weak*: Several studies are adjacent, focused on mechanism design, partner selection games, mutual-aid, or contest games, generally sharing structure but not strict PGG rules.

**punishment_or_sanctions**:  
- *exact*: Many studies explicitly manipulate costly punishment (e.g., Sparks et al., 2024; Chen, 2022), including third-party and institutionally organized forms (Hou et al., 2019).
- *close*: Some analyze adjacent mechanisms (e.g., review/veto stages, penalty/tax, ostracism, or allocative sanctions), functioning similarly to punishment.
- *adjacent/weak/none*: A minority do not include/assess punishment, only discussing it conceptually or as part of background context.

**efficiency_or_related_payoff_outcome**:  
- *exact*: Several papers provide *direct* efficiency or group payoff outcomes as primary analysis (e.g., Chen, 2022; Sparks et al., 2024; Lippert & Tremewan, 2021; Falvey et al., 2025; van Klingeren & Buskens, 2024).
- *close*: Others report group earnings, welfare, surplus, or payoff proxies closely related to efficiency (e.g., Hou et al., 2019; Zhosan & Gardner, 2013; Faillo et al., 2020).
- *adjacent/weak*: Many studies focus on contribution rates, cooperation behavior, or punishment frequency, which are not payoff-based, though their results may correlate with efficiency.
- *none*: A notable share does not report efficiency or group payoff, focusing on process or behavioral outcomes alone.

---

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (efficiency, group payoff, welfare, surplus):**
    - Directly measured in a significant subset: Several core laboratory experiments and theoretical models place efficiency or average group payoff (as a fraction of full cooperation) as a main outcome (e.g., Chen, 2022; Sparks et al., 2024; Hou et al., 2019; Lippert & Tremewan, 2021; Falvey et al., 2025; van Klingeren & Buskens, 2024).
    - Some report close proxies: e.g., total earnings, tokens earned, group surplus.
    - A few report only related, but not exactly matched, payoff outcomes (sometimes only as a secondary measure).

- **Non-payoff behavioral outcomes (contribution rate, cooperation rate, frequency of punishment):**
    - Widespread in the experimental and modeling literature (e.g., Kingsley & Smith-Walter, 2024; Molenmaker et al., 2019; Wu & Sun, 2022; Guo et al., 2023).
    - Useful for mechanistic inference and as correlates but cannot be directly equated with efficiency.

- **Hybrid or mechanism/process outcomes:**
    - Some studies focus on theoretical or evolutionary stability, social norm prevalence, or process markers like speed to equilibrium or group resilience to shocks.

**Explicit Distinction:**  
Throughout, studies must be careful not to conflate high contribution or cooperation with high efficiency—punishment can increase contributions but destroy efficiency if costs are high, or do the reverse in rare cases (e.g., Chen, 2022 vs. Sparks et al., 2024).

---

# 4) Main Findings Relevant To Prediction

### 1. **Enabling costly peer punishment often—but not always—increases group efficiency relative to no-punishment conditions in standard PGGs.**
- In prototypical settings (e.g., 4 players, repeated rounds, standard MPCR), enabling costly punishment reliably increases long-run group earnings and efficiency (Sparks et al., 2024; Hou et al., 2019). The effect is especially strong in long games and when punishment is salient and effective.

### 2. **The efficiency benefit of punishment is highly context-dependent; significant negative or null effects occur, especially under certain group compositions or design features.**
- In heterogeneous groups, punishment can backfire: efficiency may be unchanged or reduced, particularly due to antisocial punishment, uncoordinated punishment by low-benefit members, or when high-benefit (rich) members punish low-benefit (poor) ones (Chen, 2022). In field experiments with strong intrinsic motivation, punishment may crowd out cooperation and reduce investment/efficiency (Amirova et al., 2022).

### 3. **The cost and technology of punishment are critical moderators.**
- Lower punishment cost (to punisher) and greater punishment effectiveness (higher punishment_tech:coins deducted per cost) raise the probability that punishment will improve efficiency by making deterrence more effective and less wasteful (Nikias & Sy, 2021; Mitzkewitz & Neugebauer, 2020).
- High cost-to-harm ratios, antisocial targeting, or high punishment frequency can destroy efficiency, even with high contributions (Chen, 2022; Greenwood et al., 2018).

### 4. **Empirical results and theory converge on the importance of institutional structure of punishment.**
- Institutionally organized punishment (collective/institutional, group-voted, or centrally funded) is generally more effective at raising efficiency than decentralized pure peer punishment—this is both a theoretical prediction and an empirical regularity (Prétôt et al., 2024; Hou et al., 2019; van Klingeren & Buskens, 2024).
- The presence of second-order free-rider problems (who will punish the non-punishers) limits the effectiveness of peer punishment unless addressed by institutional/collective mechanisms.

### 5. **Presence of reward, or hybrid reward-and-punishment, mechanisms can have distinct and sometimes superior effects.**
- In some settings, reward alone is much less effective than punishment, but hybrid mechanisms (both reward and punishment available) can yield the highest efficiency (Hou et al., 2019; Chen, 2022). However, this is not universal.

### 6. **Information and observability matter:**
- Monitoring structure (who can see what, when) and feedback about contributions/punishment/rounds affect the efficacy of punishment (Mihm & Toth, 2020; Laclau & Tomala, 2017), sometimes making coordination on punishment easier and more efficient.

### 7. **Game design parameters directly moderate the treatment effect:**
- Higher MPCR (synergy) increases baseline efficiency and the marginal benefit of punishment in promoting cooperation (Hou et al., 2019; Falvey et al., 2025).
- Small player counts (smaller groups) tend to allow more effective peer punishment, while large groups make payoff-efficient punishment less likely unless institutionalized (Sugaya & Wolitzky, 2023; Kurokawa, 2023).

### 8. **Control efficiency is a strong predictor; punishment more reliably increases efficiency when baseline efficiency is low.**
- Mechanism/theory and empirical results (Corriveau, 2012; Cooney, 2025; van Klingeren & Buskens, 2024) indicate that when control (no-punishment) efficiency is already near its maximum, further gains from punishment are limited, but when control efficiency is low, punishment (if well-designed and credibly implemented) can produce large efficiency gains.

### 9. **Several important moderator risks are identified:**
- Antisocial or indiscriminate punishment, high punishment cost, or lack of credible threat/coordination can neutralize or reverse the efficiency gains of punishment (Antoci & Zarri, 2015; Amirova et al., 2022; Chen, 2022).
- Motivation crowding, punishment signaling distrust, or malfunctioning institutions can actually reduce intrinsic cooperation and decrease efficiency (Klempt & Pull, 2018; Hakimov & Kajackaite, 2024).

---

# 5) Prediction Guidance

Based on the literature:

- **When control efficiency is known and the punishment enabled condition matches standard lab PGGs (moderate group size, repeated rounds, moderate MPCR, no extreme heterogeneity, efficient punishment), average efficiency is expected to increase upon enabling costly peer punishment.** The increase can be substantial or modest depending on design, but rises over the baseline by deterring defection, especially over longer horizons (Sparks et al., 2024; Hou et al., 2019; Zhosan & Gardner, 2013).

- **If the punishment regime is inefficient (high cost, low effectiveness, ambiguous targeting, presence of antisocial punishment, or in highly heterogeneous groups), enabling punishment may yield no benefit or may reduce efficiency relative to control.** This is most pronounced in settings where intrinsic motivation or nonmaterial norms are strong and where costly punishment crowds out voluntary cooperation (Chen, 2022; Amirova et al., 2022).

- **Institutional features (centralization, collective funding, credible monitoring, and coordinated threat) greatly improve the odds that punishment will actually raise efficiency.** If design dimensions reflect an institutional or hybrid-punishment mechanism, predicted efficiency gain is robust (Prétôt et al., 2024; van Klingeren & Buskens, 2024).

- **Punishment cost and effectiveness must be specifically considered:**
    - Lower punishment_cost and higher punishment_tech (greater impact per cost) increase the likelihood that enabling punishment will improve efficiency (Nikias & Sy, 2021; Mitzkewitz & Neugebauer, 2020).
    - Very high cost or low effectiveness can result in efficiency losses due to resource destruction.

- **Information structure further moderates the effect:**  
    - More transparency about others' choices (show_other_summaries, show_punishment_id) usually enhances the efficacy and efficiency of punishment (Mihm & Toth, 2020; Laclau & Tomala, 2017).
    - Opaque or noisy environments reduce the effectiveness and can lead to inefficiency.

- **If the setting includes strong nonmonetary, costless approval mechanisms, efficiency gains may be achievable without explicit costly punishment (Faillo et al., 2020; Lippert & Tremewan, 2021).**

- **Ambiguity remains in field and heterogeneity-heavy settings—predicted efficiency gain may be attenuated or negative, and contextual factors (intrinsic motivation, crowding out, field partner identity) must be taken into account.**

---

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**
- **player_count:** Commonly varied and mechanistically analyzed; strong evidence on group size as a moderator.
- **num_rounds:** Many repeated-game settings; effects of long vs short games directly tested.
- **mpcr:** Central to both lab and theory work; higher MPCR enhances efficiency and benefit of punishment.
- **punishment_cost & punishment_tech:** Explicitly manipulated in both empirical and theory studies as critical moderators of effectiveness and efficiency gains.
- **reward_exists:** Papers directly compare reward, punishment, and hybrid mechanisms.
- **all_or_nothing, default_contrib:** Present as primary manipulations in many core lab PGG and adjacent games.

**Indirectly Informed:**
- **chat:** Discussed as a parallel or competing mechanism; communication can substitute for (or strongly complement) punishment.
- **show_n_rounds, show_other_summaries, show_punishment_id:** Frequently described; their role in monitoring/transparency is analyzed (Mihm & Toth, 2020).
- **reward_cost, reward_tech:** Many adjacent studies incorporate reward dimensions.

**Contextually Discussed:**
- **punishment_tech (how punishment is implemented)—especially details beyond cost-to-impact ratio, and mode (peer vs. institution)**
- **show_other_summaries, show_punishment_id:** Not always included as primary variable but discussed as mechanisms affecting punishment credibility and targeting.

**Effectively Missing or Weakly Covered:**
- **default_contrib:** Framing of default contribution is sometimes present but rarely a main analytic dimension.
- **Some subtle behavioral presentation/feedback variables (e.g., interface design) are noted but not treated systematically.**

---

# 7) Important Limitations

- **Empirical payoff/efficiency data is limited for some dimensions:** Many papers report contribution behavior, not direct efficiency, especially in field, hybrid, and complex designs.
- **Heterogeneous groups and real-world settings show more variable or even negative effects of punishment on efficiency (Chen, 2022; Amirova et al., 2022), limiting generalizability from standard lab studies.**
- **Antisocial punishment and high-cost punishment can destroy efficiency—even as contributions rise—underscoring the risk of naively assuming any punishment will improve efficiency.**
- **Motivation crowding and signaling effects (Klempt & Pull, 2018; Hakimov & Kajackaite, 2024) show that poorly designed or announced punishment regimes can reduce intrinsic cooperation, with possible negative efficiency effects.**
- **Institutional forms of punishment perform differently than peer punishment: not all papers differentiate clearly between types (peer, institution, third-party, hybrid).**
- **Several key moderators (e.g., group structure, information environment, behavioral heterogeneity, cultural context) are underexplored experimentally in direct efficiency terms, especially outside of student samples.**
- **Some dimensions (e.g., chat, default contribution framing, subtle display features) are underrepresented in payoff-centric analyses, limiting confidence in dimensional extrapolation beyond the tested ranges.**
- **Theoretical models sometimes provide necessary, not empirical, conditions for efficient punishment effects; translation to actual effect sizes in lab or field conditions may be non-trivial.**
- **Not all evidence is symmetric: field or culturally diverse experiments often show weaker or even reversals of standard lab findings, indicating the importance of context for prediction.**

---

*References by example: (Chen, 2022); (Sparks et al., 2024); (Hou et al., 2019); (Lippert & Tremewan, 2021); (Faillo et al., 2020); (van Klingeren & Buskens, 2024); (Greenwood et al., 2018); (Prétôt et al., 2024); (Amirova et al., 2022); (Nikias & Sy, 2021); (Mihm & Toth, 2020); (Klempt & Pull, 2018).*
