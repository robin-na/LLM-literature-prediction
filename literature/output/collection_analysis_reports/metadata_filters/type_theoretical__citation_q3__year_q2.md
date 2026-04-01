# 1) Evidence Base

The supplied paper set is **large (125 papers)** and is composed **entirely of theoretical studies**; no empirical or experimental evidence is present. Theoretical work covers a broad range of public-goods-game-like (PGG) settings, closely related games, and adjacent domains. However, a **core subset of the papers models PGGs with direct attention to punishment and payoff-based efficiency or group welfare**. Many other papers discuss adjacent or conceptually similar games (e.g., Prisoner's Dilemma, snowdrift games, common-pool resource dilemmas, trust games) or mechanisms (reputation, exclusion), and most of the adjacent papers model *behavioral outcomes* (e.g., cooperation rates) rather than efficiency as defined for the prediction task.

The evidence base is thus **theoretically rich and broad** for understanding mechanisms, moderators, and general directionality of punishment’s effect on cooperation and efficiency, but **lacks empirical estimates and is more robust on theory than on data-driven prediction**. Detailed attention is given to **game design dimensions** and outcomes in several core models, but support is uneven across the full space of prediction-relevant features.

---

# 2) Task Relevance

**Relevance by dimension:**

- **pgg_or_variant**:  
  - **exact**: A substantial subset (Levine & Modica, 2016; Oya & Ohtsuki, 2017; Vasconcelos et al., 2015; Zhang et al., 2013; Dercole et al., 2013; Archetti & Scheuring, 2013; Hetzer & Sornette, 2013; Abdallah et al., 2014; dos Santos & Wedekind, 2015, etc.) model standard PGGs or threshold PGGs.  
  - **close/adjacent**: Many others analyze close variants: snowdrift games, common-pool resources, repeated PD, trust games, or special institutional settings.  
  - The remainder is **adjacent or weak** (models of cooperation, exclusion, networked social dilemmas, etc.)  
- **punishment_or_sanctions**:  
  - **exact/close**: Most of the highly relevant PGG papers model **peer punishment, pool punishment, exclusion as punishment, or third-party sanctions**, generally as a cost to the punisher with an effect on the target.  
  - Many adjacent papers explore **alternative or broader forms of sanctioning (e.g., exclusion, ostracism, meta-incentives, reputation penalties, or collective sanctions)**.  
- **efficiency_or_related_payoff_outcome**:  
  - **exact**: Several key studies (Levine & Modica, 2016; Oya & Ohtsuki, 2017; Vasconcelos et al., 2015; Zhang et al., 2013; Dercole et al., 2013; Archetti & Scheuring, 2013; etc.) report *efficiency* or explicitly define welfare, group payoff, or surplus as their outcome.  
  - **close/adjacent**: Many report **group welfare, average payoff, or expected group fitness**—not always normalized to the “full cooperation” benchmark but strongly related.  
  - A large number report only **cooperation/contribution rates, frequencies of strategies, or prevalence of behavioral types**—these are **not efficiency, but may proxy efficiency under certain parameterizations**.

**Summary:**  
**Task relevance is high for core PGG theoretical models with punishment and efficiency as outcomes.** Evidence becomes more indirect for adjacent models and is weak to none for models that only consider behavioral rates, network structure, or non-punitive mechanisms.

---

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes:**
- **Efficiency** (as a fraction of maximal possible group payoff): Directly analyzed in a significant minority of core theory papers, especially those focused on peer punishment, pool punishment, or institutional sanctions (e.g., Levine & Modica, 2016; Vasconcelos et al., 2015; Dercole et al., 2013; Archetti & Scheuring, 2013; Oya & Ohtsuki, 2017).
- **Group payoff / Total earnings / Welfare / Surplus**: Often used interchangeably with efficiency, though not always explicitly normalized.
- **Explicit analytic formulas**: Some theory papers provide efficiency formulas as a function of design dimensions.

**Non-payoff behavioral outcomes:**
- **Cooperation rate** (fraction of contributors, frequency of cooperation): The most common, but is not always linearly related to efficiency depending on cost/benefit structures and punishment costs.
- **Punishment frequency or magnitude**, **norm compliance**, **prevalence of cooperators, defectors, punishers, or mixed strategies**: Widely reported; important for mechanism analysis but not for direct efficiency prediction.

**Distinction maintained:**  
Many studies **only report behavioral outcomes**, and **explicitly do not analyze efficiency or group payoffs**. Efficiency must *not* be inferred unless explicitly tied to payoff-based measures by the model.

---

# 4) Main Findings Relevant To Prediction

**Synthesized across the most relevant (exact/close) theory papers:**

- **Punishment usually increases efficiency in PGGs**:  
  When introduced and **not prohibitively costly**, peer punishment or institutional punishment generally raises group efficiency, sometimes dramatically (Levine & Modica, 2016; Dercole et al., 2013; Vasconcelos et al., 2015; Archetti & Scheuring, 2013; Powers & Lehmann, 2013).

- **Effect depends critically on punishment cost/effectiveness, group size, and game structure:**  
  - **Costly, ineffective, or highly error-prone punishment may not improve efficiency** (Oya & Ohtsuki, 2017 [well-mixed populations], Okada et al., 2015, Helbing et al., 2014).
  - **Efficiency gains are larger for larger group sizes** *if* punishment is effective and not too costly (Levine & Modica, 2016).
  - If punishment is **too weak, too costly, or leads to over-punishment**, efficiency gains diminish or may be negative, especially considering the cost of antisocial punishment (Thöni, 2014; Helbing et al., 2014).
  - **Mild/shared (non-overpunishing) punishment can suffice to reach high efficiency** (Dercole et al., 2013).
  - **Antisocial punishment** can undermine gains (Thöni, 2014).
  - **Institutional design** (centralized vs. decentralized, exclusion vs. costly deduction, possibility of corruption) modifies effects (Vasconcelos et al., 2015; Abdallah et al., 2014; Lee et al., 2015; Okada et al., 2015).

- **Population structure and mechanism details matter**:  
  - **Well-mixed** settings: punishment less effective or even counterproductive (Oya & Ohtsuki, 2017; Roos et al., 2014).
  - **Spatially structured or networked populations**: punishment more able to sustain high efficiency, especially with local information and recurrent interactions (Levine & Modica, 2016; Roos et al., 2014).
  - **Reputation and exclusion**: alternative or complementary to punishment, sometimes achieving high efficiency without direct punishment.
  - **Production function**: If benefits are nonlinear (threshold, sigmoid, step), *punishment adds little* if cooperation is already stable; if benefits are linear, *punishment is critical* (Archetti & Scheuring, 2013).

- **Risk of negative or null effects under some conditions**:  
  - **Punishment may reduce efficiency if implemented as a non-redistributive tax** (Griffin & Belmonte, 2017), or if punishment costs exceed cooperation benefits.
  - **Corruption of enforcement/monitoring** undermines or reverses efficiency gains from punishment (Abdallah et al., 2014; Lee et al., 2015; Lee, Jusup, & Iwasa, 2017; Okada et al., 2015).

- **Indirect or adjacent evidence** supports/qualifies core findings:  
  - Many models of repeated and threshold games, reputation, or social exclusion show that *punishment-like* interventions or contingent enforcement *can* support or stabilize high efficiency—but results are highly dependent on parameterization and mechanism details.

---

# 5) Prediction Guidance

**How should this literature inform predictions of treatment efficiency (punishment-enabled) given design dimensions and control efficiency?**

- **If the game is a standard PGG with linear benefits, peer or pool punishment, and moderate or low punishment cost/effectiveness barriers, expect a substantial efficiency increase when punishment is enabled**—especially if control efficiency is low and group size is not prohibitively large (Levine & Modica, 2016; Dercole et al., 2013; Powers & Lehmann, 2013; Vasconcelos et al., 2015; Archetti & Scheuring, 2013).
    - *Quantitative estimates can follow the analytic models given in the theory papers, which tie efficiency directly to player_count, mpcr, punishment_cost, and punishment_tech.*  
- **Moderators to account for:**
    - **Punishment cost**: High cost reduces or eliminates efficiency gains. If the cost is very high, enabling punishment may not help or may even hurt, due to the cost burden on punishers.
    - **Punishment effectiveness/technology**: If punishment is weak or indirect, gains diminish.
    - **Group size (player_count)**: Larger groups benefit *if punishment remains effective and not overly costly*, but may suffer if costs scale badly or coordination lapses.
    - **Population structure**: Well-mixed vs. structured (recurrent partners, local neighborhoods) is crucial—punishment is more potent/favorable for efficiency in *structured* populations.
    - **Presence of antisocial punishment** or *corruption*: If present/frequent, efficiency gains are greatly blunted or even reversed.
    - **Production function**: For nonlinear benefit functions (threshold, sigmoid), enabling punishment may have little marginal impact on efficiency *if baseline (control) efficiency is already high*; for linear cases, the predicted gain is much larger.
    - **Audit/monitoring quality**, **reputation/communication**: Higher monitoring improves punishment’s function and thus efficiency; opacity or information asymmetry reduces it.

- **When control efficiency is already high (near full cooperation), expect little marginal effect from punishment.** The largest effects are when baseline efficiency is low (Levine & Modica, 2016; Archetti & Scheuring, 2013).

- **If antisocial punishment, corruption, or misapplied sanctions are expected or structurally possible, predicted gains should be sharply discounted** (Thöni, 2014; Abdallah et al., 2014; Helbing et al., 2014).

- **For prediction in nonstandard cases (networked, threshold, or resource dilemmas), use adjacent models with caution, noting that effect size and even sign can vary with mechanism details.**

- **Predictions are best supported by design-dimension-based formulas offered in analytic models** (see Levine & Modica, 2016; Dercole et al., 2013; Oya & Ohtsuki, 2017; Vasconcelos et al., 2015).

- **If design dimensions are outside the modeled range (e.g., very large N, very high punishment cost, strong nonlinearity, complex network dynamics), acknowledge increased uncertainty and potential for diminished or reversed effects.**

---

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions:**  
The following are directly (and repeatedly) modeled in theory papers with explicit or parametric attention:
- **player_count** - Group size: Strongly modeled regarding scaling of punishment's effect.
- **num_rounds** - Number of rounds: Not always explicit, but critical in repeated games and PGGs vs. one-shot settings.
- **mpcr** - Marginal per-capita return: Core parameter; higher mpcr generally increases potential for cooperation and the efficiency effect of punishment.
- **all_or_nothing** - Binary vs. continuous contribution: Both cases are modeled, with variable effect on punishment's impact.
- **punishment_cost**, **punishment_tech** - Cost and effectiveness of punishment: Core moderators.
- **punishment_exists** - Treatment variable; directly manipulated.
- **reward_exists**, **reward_cost**, **reward_tech**: Some models involve rewards as a counterpoint or complement to punishment (Okada et al., 2015; Gao et al., 2015).
- **show_n_rounds** / **show_other_summaries**: Indirectly via information structure, but less often parameterized directly.
- **show_punishment_id**: Occasionally discussed, especially regarding monitoring and antisocial punishment.

**Indirectly or contextually discussed:**
- **chat**: Communication is mentioned as a moderator in reviews and some models (Janssen, 2015) but not always parameterized.
- **default_contrib**: Occasionally referenced (Krasnow et al., 2015), but not systematically modeled.
- **network structure, mobility, population structure**: Extensively modeled as moderators of punishment efficiency.
- **corruption, error rates, production function shape**: Emergent as moderators/category; sometimes not mapped to a named dimension but crucial for prediction.

**Effectively missing or sparse:**
- **Framing/detailed UI-level variables** (such as default_contrib) are not typically prominent in theory models.
- **Specific experimental features** (e.g., show_punishment_id) are mentioned, but direct mappings to outcomes are rare.

---

# 7) Important Limitations

- **Lack of empirical/experimental data**: All evidence is theoretical or simulation-based, lacking validation or calibration against actual observed group behaviors or payoffs.
- **Behavioral-outcome focus in many models**: Many studies use contribution/cooperation rates rather than explicit efficiency, requiring inference when mapping to payoff-based efficiency.
- **Assumption sensitivity**: Theoretical findings depend critically on model parameters and assumptions regarding cost structures, population structure, and strategy sets. Small changes (nonlinear benefit functions, network structure, error rates, or player knowledge) can flip results.
- **Limited granularity around some design dimensions**: Certain parameters (e.g., chat, information disclosure, framing) are underexplored, making them weakly supported for prediction.
- **Complexity of real-world environments not captured**: Corruption, antisocial punishment, cultural differences, and real audit/monitoring issues are seldom parameterized, and their effects can be large and nonlinear.
- **Adjacent and non-PGG evidence not always transferable**: Close variants (Prisoner's Dilemma, snowdrift, trust games) provide valuable mechanism insight but cannot always be mapped directly to PGG payoff predictions.
- **Ambiguity in presence of mixed/oscillatory equilibria**: Some models predict multiple possible steady states or bistability (Lee et al., 2015; Griffin & Belmonte, 2017), which injects irreducible uncertainty into outcome predictions.
- **Potential for negative or null effects**: Especially when punishment cost is high or when group/institutional structures lead to counterproductive punishment dynamics (Helbing et al., 2014; Oya & Ohtsuki, 2017).

---

**In summary:**  
This theoretical literature supports **directional, mechanism-based predictions** that punishment in PGGs typically increases efficiency when designed well (moderate cost, effective, no corruption, not prone to antisocial use), especially in structured or repeated-group contexts and for linear production functions. However, model parameterization, design specifics, and contextual moderators must be carefully considered, and results are less reliable (and sometimes may invert) when conditions violate core model assumptions or move outside the well-modeled settings. Use analytic models for quantitative prediction where possible, but retain caution about generalizing to out-of-sample or complex environments.
