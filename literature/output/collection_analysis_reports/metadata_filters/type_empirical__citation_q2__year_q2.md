# 1) Evidence Base

The evidence base is **empirical and experimental**, composed mainly of laboratory public goods game (PGG) experiments, with several field-experimental and a few observational or theory-adjacent studies. Most papers directly manipulate PGG dimensions, though a significant subset explores related social dilemma or trust-game structures. The set is **broad and deep** for laboratory PGGs, with high coverage of standard design parameters and variations of punishment and institution features. Evidence includes both payoff-based (efficiency, earnings) and behavioral (contribution, punishment use) outcomes, with a strong focus on the direct comparison between PGGs with and without punishment enabled.

# 2) Task Relevance

**pgg_or_variant:**
- **Exact relevance:** The core of the literature features standard linear PGGs and close variants (e.g., threshold games, complementarity games, asymmetric PGGs, and sequential common pool resource games), covering a wide range of typical experimental setups and institutional interventions.
- **Adjacent/close relevance:** A secondary share of studies covers adjacent games (trust, commons dilemmas, team production, insurance pools, procurement, etc.), generally with some PGG-like structure but not always a direct analog.

**punishment_or_sanctions:**
- **Exact relevance:** There is wide and repeated direct manipulation of punishment (peer, centralized, exogenous/deterrence, redistributive, ostracism, expulsion, institutional, and endogenous acquisition of rights), with parameterizations over cost, effectiveness, and targeting.
- **Close/adjacent relevance:** Some studies examine institutional or indirect punishment (e.g., coverage rules, exclusion, milestone penalties), as well as reward, counter-punishment, and mechanisms involving reputational and informational sanctions.

**efficiency_or_related_payoff_outcome:**
- **Exact relevance:** Many studies report group efficiency (earnings as a proportion of possible, surplus, welfare), often contrasting punishment-on and punishment-off treatments with other design dimensions held constant.
- **Close/adjacent/weak relevance:** Several important studies focus on contributions, cooperation rates, punishment frequency, or other non-payoff behaviors, and do not report efficiency directly. Where efficiency is not reported, some inference is possible if the transformation from behavior to efficiency is straightforward, but the evidence is less decisive.

# 3) Outcomes Measured In The Literature

- **Payoff-based outcomes (direct for prediction):** Efficiency (group earnings relative to social optimum), group payoff, surplus, total earnings, welfare, average profit, income distributions.
- **Non-payoff behavioral outcomes (not the same as efficiency):** Contribution/cooperation rates, punishment or reward frequency/use, norm compliance, antisocial or prosocial punishment, emergence of strategies or roles, trust, and behavioral responses to sanctions.
- Several studies explicitly note the distinction and caution against inferring efficiency gains from contribution or norm-enforcement alone, as the costs of punishment can easily offset gains in cooperation.

# 4) Main Findings Relevant To Prediction

**Empirical Findings:**

1. **Punishment increases contributions but often fails to increase efficiency** because punishment costs offset the gains from higher cooperation, especially when antisocial punishment or mis-targeted sanctions occur (Kocher & Matzat, 2016; Fatas & Mateu, 2015; Rockenbach & Wolff, 2016; Dorrough et al., 2017).
2. **Reward, redistribution, or institutionally targeted punishment mechanisms outperform standard costly punishment**—reward often increases both contributions and efficiency, and redistributive punishment (where fines become group rewards) can transform punishment from efficiency-neutral/negative to efficiency-positive (Page et al., 2013; Kocher & Matzat, 2016).
3. **Punishment’s efficiency effect is highly moderated by game design:**
   - **Group size and structure:** Effectiveness declines in large, anonymous groups and can become negative if punishment is illegitimate or perceived as unfair (Zheng & Nie, 2013).
   - **Production function:** Punishment more reliably raises efficiency in complementarity (weakest-link) settings than linear ones, especially when antisocial punishment is common (Fatas & Mateu, 2015).
   - **Punishment rights:** Endogenous acquisition costs for punishment rights can eliminate efficiency gains even when control efficiency is low (Ramalingam et al., 2016).
   - **Centralization & stability:** Stable, equal access to punishment yields higher efficiency than unequal/unstable or monopolized punishment institutions (Dorrough et al., 2017; Fischer et al., 2016; Grieco et al., 2017).
   - **Cost and impact:** Lower-cost, higher-impact (more efficient) punishment or monitoring is more likely to increase efficiency (Kingsley & Brown, 2016; Goeschl & Jarke, 2016).
   - **Noise and information:** Punishment can **reduce efficiency** or become ineffective in noisy environments where mis-punishment is common (Fischer et al., 2016; van Miltenburg et al., 2017).
   - **Institutional legitimacy:** Punishment is more efficient when perceived as legitimate, often linked to transparency, participation, or clear agreements; otherwise, it risks antisocial use and efficiency loss (Zheng & Nie, 2013; Dannenberg, 2016).
   - **Communication:** The presence of chat or communicative mechanisms can neutralize the efficiency loss from punishment or make up for its absence, depending on context (Andrighetto et al., 2016; Brick et al., 2016).
   - **Context & field:** Laboratory findings do not always generalize: in high-baseline-efficiency field contexts, adding punishment can **reduce** efficiency (Javaid et al., 2017).

4. **Nonlinear payoffs, heterogeneity, and complexity often diminish or reverse the classical efficiency advantage of punishment** (Cason & Gangadharan, 2016; Robbett, 2016; Bravo & Squazzoni, 2013).
5. **Ostracism (social exclusion)** and **binding institutional sanctions** can provide strong efficiency improvements in group-formation or migration-based PGGs (Sääksvuori, 2014; Ozono et al., 2016).
6. **Baseline (control) efficiency moderates treatment effect:** Where baseline efficiency is already high due to feedback, norms, or information, enabling punishment may bring little or even negative marginal value (Javaid et al., 2017; Cason & Gangadharan, 2016).
7. **Theory/Mechanism arguments** (less robust than empirical): Punishment supports cooperation through deterrence but is only efficiency-improving when it is well-targeted, not too costly, legitimate, and appropriately moderated by institution and communication (Kingsley & Brown, 2016; Goeschl & Jarke, 2016).

# 5) Prediction Guidance

**For prediction of treatment efficiency (with punishment enabled), given game design and control efficiency:**

- **Do not infer efficiency gain from punishment simply because it increases contributions:** The costliness and targeting of punishment are critical; in many cases, especially standard peer punishment, efficiency is unchanged or even reduced relative to baseline (Kocher & Matzat, 2016; Rockenbach & Wolff, 2016).
- **Punishment’s effect is highly design-contingent:**
  - **Expect efficiency gains** if: punishment is costless or highly effective, well-targeted, redistributive, or institutionally legitimized; when baseline efficiency is moderate/low and group size is small; or mechanisms allow collective coordination with robust monitoring (Page et al., 2013; Ramalingam et al., 2016; Reif et al., 2017).
  - **Expect null or negative effects** if: punishment rights are costly to acquire, antisocial punishment is present, monitoring is noisy or costly, group size is large, institutional power is unstable/unequal, or baseline efficiency is already high (Zheng & Nie, 2013; Dorrough et al., 2017; van Miltenburg et al., 2017; Javaid et al., 2017).
- **If control efficiency is high, the marginal value of punishment is likely to be low or negative** (Javaid et al., 2017; Cason & Gangadharan, 2016).
- **Reward and redistributive punishment almost always beat pure costly punishment for efficiency**, suggesting that the structure of 'punishment' (punishment_tech, reward_exists) is as important as its cost parameter (Page et al., 2013; Kocher & Matzat, 2016; Bravo & Squazzoni, 2013).
- **Game characteristics to emphasize in prediction:**
  - **Group size** (player_count), number of rounds (num_rounds), MPCR (mpcr), punishment cost (punishment_cost), targeting and structure (punishment_tech), chat/communication (chat), and game structure (all_or_nothing, default_contrib).
- **Behavioral findings (e.g., contribution increases, less defecting) cannot substitute for payoff-based efficiency predictions** unless permission is given to infer payoffs from contributions via known transformation (Fatas & Mateu, 2015).

**Rule-of-thumb from the literature:**  
_"Only predict a strong efficiency gain from punishment if the game design ensures that the punishment mechanism is cost-effective, legitimate, and targeted, and where baseline efficiency is not already high due to other mechanisms or context. Otherwise, expect little or even negative marginal efficiency change from enabling standard peer punishment."_

# 6) Design Dimensions Highlighted Across Papers

- **Directly and repeatedly informed:**  
  - `player_count` (group size): Efficiency effects of punishment are strongest and most often positive in small groups; large groups dilute effect, introduce problems of legitimacy and mis-targeting (Zheng & Nie, 2013; Andrighetto et al., 2016).
  - `num_rounds`: Repeated interactions allow learning and adaptation in punishment use; short-run and long-run effects can diverge (Wang & Qin, 2015; Reif et al., 2017; Kocher & Matzat, 2016).
  - `chat` (communication): Strong moderator; enables coordination, can substitute for or amplify institutional effects (Andrighetto et al., 2016; Dannenberg, 2016).
  - `mpcr`: Higher MPCR can amplify both the benefits and the risk of negative punishment effects, depending on the targeting (Bruttel & Friehe, 2014; Fatas & Mateu, 2015).
  - `punishment_cost` and `punishment_tech`: Central moderators; lower cost and higher impact (cost-effectiveness) greatly favor efficiency impacts from punishment (Kingsley & Brown, 2016; Ramalingam et al., 2016).
  - `all_or_nothing`: Findings are robust across continuous and all-or-nothing (binary) contribution games, but some papers show structure-specific effects—e.g., threshold/weakest-link games support punishment better (Fatas & Mateu, 2015).
  - `show_other_summaries`, `show_n_rounds`: Information feedback is crucial for targeted punishment and institutional legitimacy (Dorrough et al., 2017; Khadjavi et al., 2017).
  - `reward_exists`: Reward mechanisms consistently outperform punishment for efficiency, or at least avoid punishment’s cost drag (Kocher & Matzat, 2016; Bravo & Squazzoni, 2013; Page et al., 2013).
  - `punishment_tech`: Variants such as centralization, quota, redistributive vs. burned punishment, collective vs. individual, endogenous acquisition of rights—all repeatedly tested as critical moderators.

- **Indirectly or sparsely informed:**  
  - `default_contrib`: Some evidence from experimental framing, but much less frequent and less central.
  - `show_punishment_id`: Occasionally addressed (Zheng & Nie, 2013; Khadjavi et al., 2017).
  - `reward_cost`, `reward_tech`: Related evidence (Kocher & Matzat, 2016; Bravo & Squazzoni, 2013), but less thoroughly varied for direct efficiency effects.
- **Effectively missing or only contextually discussed:**  
  - Some design dimensions that combine elements under unusual institutional arrangements (e.g., highly endogenous or field-specific institutions, or complex reputation/coalition structures) are not systematically varied in the efficiency-focused PGG studies.

# 7) Important Limitations

- **Ambiguity/disagreement:**  
  - There is clear empirical disagreement on when enabling punishment increases, decreases, or leaves efficiency unchanged, and this is context- and design-dependent (compare Kocher & Matzat, 2016 vs. Reif et al., 2017; Dorrough et al., 2017 vs. Grieco et al., 2017).
- **Field vs. lab and generalizability:**  
  - Laboratory findings (particularly efficiency improvements from punishment) do not always generalize to field settings or real-world CAS/CPR problems. In some high-baseline-efficiency field scenarios, punishment can reduce efficiency (Javaid et al., 2017).
- **Non-payoff behavioral outcomes:**  
  - Many high-profile studies focus exclusively on contributions or norm compliance without reporting efficiency or group payoff, limiting their predictive value for the specific task (e.g., Kubena et al., 2014).
- **Parameter confounds:**  
  - In many cases, the relative effect of punishment is an interaction of several experimental parameters (group size, punishment cost, transparency, institution type, communication), making dimension-level predictions challenging without comprehensive parameter fit.
- **Sparse direct evidence for uncommon settings:**  
  - Certain combinations of game dimensions (e.g., very large groups, highly endogenous punishment rights, heavy noise, complex payoff functions) are under-studied.
- **Outcome definition and measurement:**  
  - Not all papers use strict efficiency as defined (payoff relative to full cooperation), even among those reporting "efficiency" results; check for compatible definitions.
- **Potential selection bias:**  
  - Some published studies may overrepresent settings with highly visible or controversial results (e.g., strong efficiency gains/losses from punishment), and null results may be underreported.
- **Limited ability to impute efficiency from behavioral outcomes:**  
  - Where only contribution, punishment frequency, or non-payoff outcomes are given, care must be taken not to infer efficiency effects without direct evidence or transparent mapping between behavior and payoffs.

---

**In summary:**  
The literature provides a strong, empirically grounded foundation for predicting changes in group efficiency due to enabling punishment in PGG-like environments, with nuanced and sometimes conflicting results. The effect depends critically on design details (especially group size, punishment structure and cost, institution legitimacy, and the baseline efficiency level) and prediction must be sensitive to these moderators. Using control efficiency and the specific configuration of design dimensions is essential, while generalizing from behavioral to payoff outcomes is risky unless supported by direct evidence.
