# 1) Evidence Base

The paper set is broad, with 68 items spanning a wide range of theoretical models, simulation studies, and a small number of empirical lab experiments. The majority of papers employ formal evolutionary game theory with a focus on public goods games (PGG) or close variants, while some use adjacent frameworks (e.g., iterated Prisoner's Dilemma, indirect reciprocity, common pool resource dilemmas, or mutualism). Nearly all the papers are theoretical or simulation-based; only a few report empirical or experimental data, and almost none provide large-sample lab evidence with explicit efficiency measures comparing punishment-enabled and punishment-disabled conditions in PGGs. Nonetheless, many models are directly parameterized for PGG institutional detail and report, at minimum, payoff-based outcomes (actual efficiency or group payoff), with many others focusing on behavioral mechanisms.

# 2) Task Relevance

**pgg_or_variant**
- **exact:** Many theory papers explicitly model standard public goods games or minor variants, including player count, MPCR, and repeated rounds (e.g., Cressman et al., 2012; Gintis, 2000; Eldakar et al., 2007).  
- **close/adjacent:** A substantial share analyze Prisoner's Dilemma, indirect reciprocity, threshold games, or group-structured dilemmas closely related to PGGs, but not always with full mapping to PGG institutional parameters.
- **weak/none:** Some are focused on mechanism concepts or psychological underpinnings without concrete game structure relevant to prediction.

**punishment_or_sanctions**
- **exact:** A large fraction of papers engage peer punishment, institutional punishment, or sanctioning as an explicit design dimension, and explore its direct impact (e.g., punishment existence, cost, magnitude, technology).
- **close/adjacent:** Others analyze behaviors analogous to punishment (e.g., withdrawal, reputation damage, exit, withholding cooperation), which may map indirectly onto sanctions in PGGs.
- **weak/none:** Several papers discuss only baseline cooperation, and do not manipulate or model punishment.

**efficiency_or_related_payoff_outcome**
- **exact:** Multiple papers use efficiency, group payoff, mean fitness, or related welfare outcomes as their principal dependent variable (e.g., Cressman et al., 2012; Gintis et al., 2001; Gintis, 2000; Powers et al., 2012).
- **close/adjacent:** Some report on the abundance of strategies, cooperation rates, or norm stability, and use outputs as proxies for group payoff or efficiency (e.g., de Weerd & Verbrugge, 2011).
- **weak/none:** A significant subset measure only behavioral change (e.g., contributions, retaliation behavior, reputations), without payoff or efficiency reporting.

**Summary:** The literature is strong to moderate in direct relevance for the prediction task, with considerable theoretical and simulation coverage of PGGs, punishment, and efficiency, but sparse direct experimental evidence measuring efficiency changes when peer punishment is enabled. The evidence is largely conceptual or model-based, rather than empirical effect-size based for the precise 14-dimension prediction task.

# 3) Outcomes Measured In The Literature

**Payoff-related Outcomes:**
- **Measured Directly:** Many theory papers explicitly report group efficiency, total payoff, mean fitness, or surplus generated under different game designs (e.g., Cressman et al., 2012; Gintis, 2000; Gintis et al., 2001; Powers et al., 2012; Sasaki & Unemi, 2011).
- **Measured Adjacent:** Some models relate prevalence of cooperative/punishing strategies to likely group payoff or infer efficiency based on stable equilibrium analysis.
  
**Non-payoff Behavioral Outcomes:**
- Prevalence or frequency of cooperators/punishers.
- Norm compliance, retaliation, anti-social punishment.
- Contribution rates, punishment frequency, strategies' evolutionary stability.
- Perceptions, reputational impact, willingness to cooperate.

**Distinction:** Although non-payoff outcomes inform mechanism, only efficiency/group payoff measures are valid for direct prediction of treatment efficiency.

# 4) Main Findings Relevant To Prediction

**Synthesis Across Paper Set:**

## Empirical vs. Theoretical Results
- **Empirical evidence is minimal.** Most findings are theory-driven or simulation-based.
- **Where empirical evidence exists (lab),** it supports claims that punishment can sustain or boost cooperation and group payoff, but cost moderation is key.

## Core Mechanisms and Results
1. **Enabling punishment typically increases group efficiency/payoff relative to a control with no punishment**—*if* punishment is not too costly and is effective at reducing defection/destructive behavior (Gintis, 2000; Cressman et al., 2012; Henrich & Boyd, 2001; Gintis et al., 2001; Okada & Bingham, 2008; Okamoto & Matsumura, 2000; Milinski & Rockenbach, 2012).
2. **Effect size and direction depend on:**
   - **Cost and effectiveness of punishment:** High punishment cost can wipe out benefits (Eldakar et al., 2007; Gintis, 2000; Okada & Bingham, 2008).
   - **Group size (player_count):** Larger groups often reduce efficacy of peer punishment (Powers et al., 2012; Eldakar et al., 2007).
   - **Antisocial punishment:** If defectors can punish, efficiency gains evaporate or reverse (Rand et al., 2010; Powers et al., 2012).
   - **Retaliation:** Ability to retaliate strongly reduces positive efficiency effects (Janssen & Bushman, 2008; Wolff, 2012).
   - **Reputation/Information mechanisms:** Efficiency gains are boosted when punishment is visible, justified, and integrated with reputation systems; anonymity or ambiguous sanctions reduce efficacy (Milinski & Rockenbach, 2012; Ohtsuki & Iwasa, 2004, 2006).
   - **Game length (num_rounds):** Punishment costs may outweigh benefits in short games; positive effects accrue over longer horizons (Wolff, 2012; Leimar, 1997).
3. **Combined reward and punishment is maximally effective:** Using both can achieve near-maximal efficiency (Cressman et al., 2012; Milinski & Rockenbach, 2012; Sasaki & Unemi, 2011).
4. **Spatial or group structure can moderate effect:** Structured populations with local interaction may increase (Nakamaru & Dieckmann, 2009) or decrease (Hauert, 2006) the ability of punishment to boost efficiency.

**Dissenting/Conditional Results:**
- **When punishment enables anti-social or spiteful use, efficiency may decrease (Rand et al., 2010; Powers et al., 2012).**
- **If retaliation is easy and punishment is not anonymous, positive effects may not emerge (Janssen & Bushman, 2008).**
- **Mechanisms involving only reputation loss (not costly punishment) can sometimes achieve similar efficiency gains with lower cost (Ohtsuki & Iwasa, 2004, 2006; Chalub et al., 2006).**
- **In some evolutionary settings, punishment is not evolutionarily stable if costs outweigh cooperation gains (Weibull & Salomonsson, 2006; Wolff, 2012).**
- **Efficiency gains are diminished or absent if baseline efficiency (control with no punishment) is already high due to alternative stabilization mechanisms (Foster, 2004; Takezawa & Price, 2010).**

# 5) Prediction Guidance

Given a game design with observed baseline efficiency (no-punishment control), the literature supports the following prediction approach:

- **Predict a higher average efficiency for the same game when peer punishment is enabled, if:**
  - Punishment cost is moderate (not undermining net payoff).
  - Punishment is effective at deterring defection.
  - Anti-social punishment is not permitted or is rare.
  - Retaliation by punished individuals is limited (e.g., by anonymity or non-identifiability of punishers).
  - The game has sufficient rounds for cooperation/punishment dynamics to play out.
  - Group size is not so large as to dilute the effect of punishment.

- **Prediction adjustments by design dimensions:**
  - **player_count:** Efficiency gains from punishment decrease as group size increases (Powers et al., 2012; Eldakar et al., 2007).
  - **num_rounds:** The longer the game, the more likely the net efficiency benefit of punishment (Wolff, 2012; Leimar, 1997).
  - **punishment_cost / punishment_tech:** Lower punishment cost and higher effectiveness enhance efficiency gains (Okada & Bingham, 2008; Gintis, 2000).
  - **reward_exists:** Adding rewards in addition to punishment can push average efficiency higher than punishment alone (Cressman et al., 2012; Milinski & Rockenbach, 2012).
  - **all_or_nothing, mpcr, show_punishment_id:** Design features increasing visibility, directness, and "bite" of punishment typically make efficiency gains more likely, unless sufficiently high cost or social risks intervene (Janssen & Bushman, 2008).

- **If antisocial punishment or easy retaliation is enabled (defectors can punish or punishers can be easily targeted), expect little or even negative effect on efficiency.**

- **If baseline efficiency is already near maximum in control, marginal benefit of punishment is reduced.**

Overall, treating control (no-punishment) efficiency as a reference point, the addition of peer punishment can be expected to increase efficiency, but the size and even direction of the effect depends sharply on the specific moderation conditions highlighted above.

# 6) Design Dimensions Highlighted Across Papers

| Design Dimension         | Coverage in Literature           | Notes                                                               |
|-------------------------|----------------------------------|---------------------------------------------------------------------|
| player_count            | Directly modeled in most theory papers           | Larger groups generally reduce punishment efficacy                  |
| num_rounds              | Directly modeled, especially in repeated game theorizing | More rounds amplify potential benefits of punishment                |
| chat                    | Rarely modeled explicitly        | Mostly absent; communication effects are only contextually addressed |
| all_or_nothing          | Covered in several models        | Modeled in both all-or-nothing and continuous contribution contexts |
| default_contrib         | Not directly discussed           | Missing from most models                                            |
| mpcr                    | Central to payoff calculations   | Low mpcr reduces scope for punishment to boost efficiency           |
| punishment_cost         | Core variable, directly modeled  | Central moderator of punishment's effect                            |
| punishment_tech         | Directly modeled (effectiveness, possibility of antisocial punishment) | Efficacy is key                                                     |
| reward_exists/tech/cost | Discussed in subset (esp. combined w/ punishment) | Reward can boost efficiency, especially in concert with punishment  |
| show_n_rounds           | Occasionally mentioned           | Known game end may moderate behavior but not widely modeled         |
| show_other_summaries    | Addressed in reputation-based models | Information flow critical in indirect reciprocity settings           |
| show_punishment_id      | Modeled in studies of retaliation/visibility     | Anonymity of punishers often a key moderator                        |

**Dimensions with Sparse or No Direct Evidence:**
- **default_contrib**: Not discussed.
- **chat:** Minimal coverage; no direct payoff evidence.
- **reward tech, reward cost:** Modeled in a few papers, secondary focus.
- **show_n_rounds, show_other_summaries, show_punishment_id:** Occasionally modeled as critical moderators, but few papers provide direct quantitative efficiency predictions as a function of these parameters.

# 7) Important Limitations

- **Empirical Evidence Gap:** The vast majority of studies are theoretical or simulation-based; there is very little large-sample, directly observed empirical or experimental data on efficiency outcomes with/without punishment across diverse design settings.
- **Indirectness for Some Dimensions:** Many prediction dimensions are contextually discussed or model-assumed, not empirically tested as causal moderators of efficiency shifts.
- **Limited Multi-dimensional Calibration:** Few models jointly manipulate all 14 design dimensions; predictions are usually offered ceteris paribus and may not hold when parameters interact nonlinearly.
- **Behavioral vs. Payoff Focus:** A substantial share of papers report on cooperation rates, punishment rates, norm stability, or related behaviors—useful for mechanism but not direct substitutes for efficiency/payoff predictions.
- **Ambiguity and Disagreement:** Some models predict that punishment, especially with antisocial forms or retaliation, can reduce efficiency—indicating non-monotonic and context-sensitive effects.
- **Realism of Models:** Theoretical models rely on simplifying assumptions that may not always map straightforwardly onto complex lab or real-world institutions.
- **Absence of Direct Framing/Default Contribution Evidence:** Features such as default contributions, chat, and detailed presentation have little direct evidence on their effect on efficiency following punishment introduction.
- **Scarcity of Empirical Effect Sizes:** There is little direct evidence on the quantitative relationship between control efficiency and treatment (punishment-enabled) efficiency for the full range of game parameterizations. Most predictions are qualitative or based on simulation parameter sweeps, not statistical models grounded in data.

---

**In summary:**  
- The literature strongly supports that enabling peer punishment typically increases efficiency in PGG-like settings, *conditional* on cost, effectiveness, absence of antisocial punishment/retaliation, and other design moderators.
- Many prediction dimensions are directly supported (especially player count, num rounds, mpcr, punishment cost/tech), while others (default contribution framing, chat, some visibility and summary features) have little or no direct evidence.
- Caution is warranted regarding the generalizability and quantitative precision of predictions, due to the theoretical nature and limitations of the existing evidence base.
