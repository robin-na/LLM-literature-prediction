# 1) Evidence Base

The paper set is predominantly empirical and experimental (lab PGGs or close variants), with a substantial theoretical and some observational contributions. The empirical coverage is broad for standard public goods games (PGGs) with and without punishment, with numerous studies reporting efficiency or closely related payoff-based outcomes across diverse game design dimensions. However, several papers (particularly in the 'adjacent' and 'theory' categories) focus on behavioral or strategic mechanisms, cultural and psychological moderators, or adjacent social dilemmas rather than strictly on efficiency in PGGs. Only a subset directly reports quantitative comparisons of efficiency with and without punishment. In summary:
- **Empirical evidence:** Strong, especially for lab-based PGGs. Multiple experimental studies report on efficiency or closely related outcomes under different punishment regimes and game designs.
- **Theoretical work:** Concerns foundations, mechanisms, and extensions of cooperation and punishment in social dilemmas (sometimes with formal predictions about efficiency, but less frequently tailored to specific PGG implementations).
- **Observational/field evidence:** Provides context for real-world cooperation and sanctioning, but does not directly inform the efficiency outcomes in explicit PGG-like environments.
- **Narrow/broad mix:** The core question (predict efficiency given control and design) is moderately-to-well represented for standard PGGs, but evidence is sparser or less direct for design variants (network structure, nonlinearities, cultural contexts, etc.).

# 2) Task Relevance

**pgg_or_variant**
- **Exact:** The majority of experimental and some theory papers are directly about repeated, standard-form PGGs or minimal-variant linear public goods games (e.g., Fischer et al. 2016; Fatas & Mateu 2015; Dorrough et al. 2017; Harrell & Wolff 2023).
- **Close:** Several papers use games with minor modifications (e.g., weakest-link, step-level, or agency extensions), or adjacent social dilemmas (e.g., nonlinear CPR games—Cason & Gangadharan 2016; provider-beneficiary variants—Lierl 2016).
- **Adjacent/Weak:** Some address prisoner's dilemma, third-party punishment, or real-world collective action scenarios.

**punishment_or_sanctions**
- **Exact:** Many studies experimentally manipulate peer punishment (enabled vs. disabled or centralized vs. decentralized) (e.g., Fischer et al. 2016; Andrighetto et al. 2016). Theory papers commonly discuss punishment or sanctioning as the main intervention.
- **Close/Adjacent:** Several discuss reward, informal or reputational sanctions, or alternative institutional mechanisms. Some address punishment only as a behavioral measure, not as a manipulated dimension.
- **None:** A few studies address only communication, group structure, or cooperation without punishment present.

**efficiency_or_related_payoff_outcome**
- **Exact:** Several experimental papers measure group efficiency, total earnings, welfare, or surplus as primary outcomes (e.g., Fischer et al. 2016; Fatas & Mateu 2015; Dorrough et al. 2017; Harrell & Wolff 2023; Lierl 2016; Cason & Gangadharan 2016).
- **Close/Adjacent:** Some report contribution rates, cooperation rates, or frequencies of punishment but infer likely efficiency changes without direct measurement.
- **Weak/None:** Theory and observational papers often discuss mechanisms or context for cooperation, but do not measure efficiency or payoff.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes** (efficiency, group earnings, total payoff, welfare, surplus, total coins):
  - Directly measured in many of the main lab-experimental PGG studies.
  - Sometimes measured only at the round or session finish (not dynamically).
  - Efficiency is tied to total group earnings as a fraction of the maximally cooperative benchmark.
- **Non-payoff behavioral outcomes** (contribution rate, cooperation rate, punishment frequency, norm compliance, retaliation):
  - Very common as primary or secondary outcomes.
  - Used extensively in mechanism-focused or psychology/cultural variant studies.
  - Occasionally used as proxies for efficiency, but do not perfectly align (e.g., increased cooperation can coexist with lower efficiency due to excessive costly punishment).
- Many papers explicitly note when efficiency and payoff are not measured.

# 4) Main Findings Relevant To Prediction

## Empirical Findings

- **Punishment's effect on efficiency is highly context-dependent:**
  - **Standard linear PGG:** Peer punishment does not uniformly increase efficiency. In some cultures or parameter regimes (e.g., high antisocial punishment), efficiency can stagnate or decrease due to wasteful punishment costs (Fatas & Mateu 2015; Fischer et al. 2016).
  - **Weakest-link/complementary production:** Punishment can raise both contributions and group efficiency dramatically, implying interaction between game structure and punishment effect (Fatas & Mateu 2015).
  - **Large and/or densely connected groups:** Punishment is more likely to achieve efficiency gains, especially where information is readily available (Harrell & Wolff 2023; Camera & Gioffré 2014).
  - **Information environment:** Noise in feedback undermines efficiency gains from punishment. Centralized sanctions can reduce perverse/antisocial punishment but may not yield higher efficiency except under specific noise regimes (Fischer et al. 2016).
  - **Stability and equality in punishment power:** Instability or inequality in who can punish reduces the efficiency benefit and can even make punishment detrimental (Dorrough et al. 2017).
  - **Communication:** Mandatory chat or normative/accountability messages substantially augment punishment's positive impact on efficiency; in their absence, punishment may be less beneficial or even net-negative (Andrighetto et al. 2016; Cason & Gangadharan 2016).
  - **Nonlinear/CPR games:** Peer punishment often fails to raise, or can even reduce, efficiency relative to baseline because of complexity or misuse (Cason & Gangadharan 2016).
  - **Sanctioning structure:** Who can punish whom matters. Limiting punishment to only certain relationships (e.g., only among beneficiaries) can increase efficiency, while broader networks may dilute or reverse this effect (Lierl 2016).

## Theory and Mechanism Arguments

- **Punishment potential vs. cost:** Theoretical models highlight that punishment only improves efficiency if costs are not excessive, monitoring is accurate, and punishment targets defectors rather than cooperators (Barrett 2020; Nakao 2009; Camera & Gioffré 2014).
- **Commitment and norm agreement:** The ability to commit to punishment (as a credible threat) and group agreement on what norm to enforce increase the effectiveness of punishment for efficiency (Akdeniz & van Veelen 2021; Brandts & Fatas 2012).
- **Reputation, repeated interaction, and monitoring breadth:** These can substitute for formal punishment; broader monitoring (more information about others' actions) makes punishment more effective (Camera & Gioffré 2014; Raub et al. 2019).

## Behavioral Outcomes

- **Antisocial punishment and counter-punishment:** In some populations, punishment is used against cooperators (antisocial), eroding or even reversing efficiency gains (Fatas & Mateu 2015; Fischer et al. 2016).
- **Punishment under threat of retaliation/counter-punishment**: May not raise efficiency, depending on institution and culture (Andrighetto et al. 2016).

# 5) Prediction Guidance

Based on the evidence:
- **Punishment enabled does not reliably increase efficiency** compared to control unless:
  - The game is structured so that punishment is inexpensive, well-targeted, and not vulnerable to antisocial misuse.
  - The information environment ensures that punishment can be credibly and accurately applied to defectors.
  - The power to punish is equally and stably distributed, without status-based competition.
  - Communication is allowed, or monitoring structures are strong.
  - The production function is complementary (e.g., weakest-link), as opposed to standard linear aggregation.
  - The group is large/densely connected (with some caveats around network structure).
- **If these moderators are not met, punishment may have no or even negative impact on efficiency** (due to waste, retaliation, or diffusion of enforcement).
- **Control efficiency alone is not a sufficient predictor**: Knowledge of baseline efficiency is useful, but the marginal effect of punishment is highly conditional on the design dimensions above.
- **When communication is enabled**, much of the potential efficiency loss from counter-punishment is mitigated (Andrighetto et al. 2016).
- **In nonlinear or more complex social dilemmas,** punishment may underperform, and communication will likely outperform punishment in delivering efficiency (Cason & Gangadharan 2016).

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions:**
- `player_count`: Extensively varied and analyzed (most evidence for groups of 4–6; larger groups studied in Harrell & Wolff 2023).
- `num_rounds`: Manipulated across studies; important for assessing repeated interaction effects.
- `chat`: Explicitly manipulated in several experiments; clear effects on efficiency in combination with punishment (Andrighetto et al. 2016; Cason & Gangadharan 2016).
- `all_or_nothing`: Studied in several contexts (e.g., threshold and weakest-link PGGs), which have distinct efficiency dynamics.
- `mpcr`: Frequently specified; critical for baseline efficiency and incentive calculations.
- `punishment_cost`/`punishment_tech` (`punishment_magnitude`): Commonly fixed or varied; shown as critical for whether punishment increases or decreases efficiency.
- `punishment_exists`: Central manipulation in almost all experiments.

**Indirectly or contextually informed dimensions:**
- `default_contrib`: Framing of contribution rarely explicitly manipulated as a main treatment.
- `reward_exists`, `reward_cost`, `reward_tech`: Some discussion of reward as alternative to punishment, but direct empirical efficiency effects are sparse.
- `show_n_rounds`, `show_other_summaries`: Sometimes discussed as part of the information environment, but rarely as main treatments; reporting level may affect punishment's targeting and perceived fairness.
- `show_punishment_id`: Only occasionally manipulated; important for reputation effects, less often for efficiency outcomes.

**Missing or only contextually discussed:**
- Design details such as specific parameterizations of default behavior, all design permutations, and fine-grained aspects of feedback/monitoring are not systematically varied across the entire literature set.

# 7) Important Limitations

- **Efficiency outcome not always measured:** Many behavioral studies do not directly report efficiency, focusing instead on cooperation rates or normative compliance.
- **Design heterogeneity:** Experimental manipulations frequently confound multiple dimensions (e.g., varying both punishment and communication), making it challenging to infer isolated effects.
- **Generalizability across structures:** Most robust efficiency results are for standard linear PGGs with small groups; findings are less certain for threshold, nonlinear, or real-world collective action settings.
- **Cultural and population effects:** Cultural context (e.g., prevalence of antisocial punishment) can completely reverse the efficiency impact of punishment, but is rarely well controlled.
- **Short horizon vs. long-run dynamics:** Some laboratory timeframes (10–30 rounds) may be insufficient to observe long-term equilibrium effects, especially if efficiency gains from punishment only manifest across many rounds (Szekely et al. 2020).
- **Outcome measure divergence:** Payoff-based and behavioral outcomes can diverge (e.g., higher cooperation but lower efficiency if punishment is misapplied).
- **Sparse coverage of night design dimensions:** Not all 14 prediction dimensions are systematically addressed; design-context interactions are not fully explored for reward, information presentation, or group feedback.
- **Limited field/real-world transfer:** Laboratory designs may not capture the richer set of sanctioning and reinforcement mechanisms present in field and anthropological settings.
- **Control efficiency is not determinative:** Baseline (no-punishment) efficiency varies widely for reasons orthogonal to punishment, and is not in itself reliable to predict the marginal effect of enabling punishment.

---

**Summary:**  
Prediction of efficiency with punishment enabled is best supported when game design dimensions—especially punishment cost, targeting, institution, information environment, group size/structure, and communication—are well specified and fall within the parameter regime directly studied in the experiments reporting efficiency outcomes. In standard PGGs, punishment may or may not raise efficiency depending on these moderators; in games with complementary production, stable and well-targeted punishment is much more likely to increase efficiency. Control efficiency is a useful but not sufficient predictor for treatment efficiency. Key contextual moderators include the potential for antisocial or misdirected punishment, stability/equality of punishment power, network structure, and presence/quality of communication.
