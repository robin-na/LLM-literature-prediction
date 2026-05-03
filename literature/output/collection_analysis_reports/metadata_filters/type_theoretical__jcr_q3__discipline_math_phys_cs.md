# 1) Evidence Base

This evidence base consists entirely of theoretical papers, with no empirical or laboratory experiments represented. The set is very broad in the sense that it covers a wide variety of game-theoretic models, meta-population structures, mechanisms of punishment and reward, variants of public goods and related social dilemma games, and many evolutionary and dynamic analyses. However, for the specific prediction task—estimating efficiency change between control and punishment-enabled public goods games using specific design dimensions—most studies are limited in direct applicability. The literature is dominated by analyses of evolutionary stability, strategy dynamics, and theoretical conditions for cooperation/payoff maximization rather than direct measurements or simulations reporting group efficiency (as a fraction of optimal) for parameterized game designs in repeated PGGs with peer punishment.

Most papers analyze close variants (exact/adjacent) of the public goods game under a variety of mechanisms (institutional punishment, peer punishment, prosocial and antisocial punishment, probabilistic/conditional/exclusionary forms, and reward mechanisms). Although some studies specifically examine the mapping between game design parameters and group efficiency or payoff-based outcomes, many report main results in terms of cooperation rates, prevalence of strategies, or stability/robustness rather than explicit efficiency ratios.

Thus, the evidence base is strong for mechanism and theoretical mapping, moderate for dimension-level moderators, and weak for empirical effect sizes or direct comparative efficiency statistics.

# 2) Task Relevance

**a) pgg_or_variant**  
- **Relevance:** The core set (first ~20 papers) directly addresses public goods games (PGG) or close, structurally similar group-based dilemmas. Most use exact PGGs or standard extensions (with punishment/reward, all-or-nothing or continuous contributions, structured populations, etc.)—label: `exact` or `close`.
- Some papers model closely related n-player social dilemmas, trust games, common-pool resource games, or dyadic donation games—label: `adjacent` or `close`.
- A minority model pure two-player PDs or more abstract evolutionary models—label: `weak` or `none`.

**b) punishment_or_sanctions**  
- **Relevance:** The majority of the most relevant papers include explicit punishment or sanctioning mechanisms—label: `exact`. These mechanisms range from peer and institutional punishment, exclusion, graduated/conditional punishment, to anti-social/reward combinations.
- A substantial minority explore reputation-based or indirect forms of punishment (e.g., exclusion, reputation loss), classified as `close` or `adjacent`.
- Some background/control/adjacent papers only contextualize punishment or mention it as a comparison—label: `weak` or `none`.

**c) efficiency_or_related_payoff_outcome**  
- **Relevance:** Many high-relevance papers analyze efficiency or directly related outcomes (total group payoff, welfare, surplus); others, instead, focus on cooperation rates, strategy prevalence, or evolutionary dynamics—label: `exact` if explicit, `close` if inferred, `adjacent` if only indirectly.
- Numerous studies use cooperation rates as proxies but do not report group efficiency directly—requiring caution to avoid misinterpretation.
- Some papers focus exclusively on behavioral, not payoff, outcomes—label: `none`.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:**  
  - Exact efficiency (group payoff as a fraction of the fully cooperative optimum), total group payoff, aggregate earnings, mean population payoff, welfare, or surplus are primary outcomes in a substantial minority (`exact`).
  - Explicit quantitative relationships between design parameters and efficiency exist in some models, especially those focusing on institutional punishment, the cost/technology of punishment, and structured populations.
  - Some models provide only qualitative or indirect evidence, showing that efficiency increases/decreases under certain conditions (e.g., parameter sweeps, phase diagrams, threshold analysis).
- **Non-payoff behavioral outcomes:**  
  - Prevalence of cooperators/punishers, cooperation/contribution rates, fraction of defectors, evolutionary stability of strategies, probability of reaching full cooperation—all commonly reported, but these are not equivalent to efficiency.
  - Strategy dynamics and equilibria (e.g., coexistence of types, polymorphism, cycles) are analyzed in evolutionary or agent-based models.
  - Some papers focus on mechanism robustness (e.g., stability to mutation/error, impact of retaliation, heterogeneity, network effects).

# 4) Main Findings Relevant To Prediction

**General Direction of Punishment on Efficiency:**
- **Positive Effects:**  
  - Theoretical consensus: enabling punishment in standard PGGs **can** increase group efficiency over the no-punishment baseline, **if** punishment is effective (i.e., significant impact per unit cost), costs are not prohibitive, and there are no strong destabilizing factors (Cressman et al., 2012; Eldakar et al., 2007; Gintis, 2000; Henrich & Boyd, 2001; Wang & Lv, 2019; Durrough et al., 2017).
  - Combination of punishment and reward (institutional schemes) are particularly potent, and sufficiently strong punishment alone can maintain full cooperation in standard linear PGGs (Cressman et al., 2012; Jiao et al., 2020).
  - Structured or spatial populations can moderate this effect, sometimes enabling stable coexistence phases with higher efficiency than in well-mixed settings (Oya & Ohtsuki, 2017; Nakamaru & Dieckmann, 2009).

- **Conditional/Null/Negative Effects:**  
  - **Key moderators:** Efficiency gains are greatly attenuated or even reversed when:
    - **Antisocial punishment** (punishment of cooperators) is possible or prevalent—often resulting in reduced or neutral efficiency effects (Rand et al., 2010; Hauser et al., 2014; Powers et al., 2012; Oya & Ohtsuki, 2017; Gao et al., 2015).
    - **Punishment is very costly**, or **punishment cost approaches or exceeds its impact**—then, punishment may not sustain cooperation, and even if contributions rise, net efficiency may not increase (Eldakar et al., 2007; Wolff, 2012; Henrich & Boyd, 2001; Perry et al., 2018).
    - **Retaliation is permitted**—the presence and ease of retaliation can undermine efficiency improvements, especially in larger groups and when punishers are identifiable (Wolff, 2012; Janssen & Bushman, 2008).
    - **Corruption/bribery or institutional failure**—when enforcers are corrupt or monitoring is weak, punishment loses its effectiveness or can even lower efficiency (Lee et al., 2015; Lee et al., 2017; Huang et al., 2018).
    - **Population structure**—in well-mixed populations, punishment may not retain efficiency unless initial conditions or population structure favor punishers (Oya & Ohtsuki, 2017).
    - **Benefit function nonlinearity**—in games with nonlinear (sigmoid, threshold, step) benefits, high efficiency may be achievable without punishment, and introducing punishment adds little benefit (Archetti & Scheuring, 2013).

- **Other Mechanisms:**  
  - The positive effect of punishment can be enhanced by coupling it with **reputation, indirect reciprocity, or institutional visibility** (Milinski & Rockenbach, 2012; Schoenmakers et al., 2014).
  - Conditional and graduated forms of punishment are often more efficient per unit cost and help address second-order free rider problems (Szolnoki & Perc, 2013; Couto et al., 2020; Iwasa & Lee, 2013).

# 5) Prediction Guidance

- **Dimension-informed Prediction:**  
  - Where design parameters are precisely specified (group size, rounds, MPCR, punishment cost/effectiveness, population structure, possibility of anti-social punishment, presence of reward, monitoring/visibility, punisher identification), direct theoretical models provide formulas or phase diagrams to estimate whether punishment will be efficiency-enhancing (e.g. Jiao et al., 2020; Eldakar et al., 2007; Wang & Lv, 2019; Milinski & Rockenbach, 2012, Huang et al., 2018).
  - **If**: punishment is peer-based, with moderate cost, high effect, and anti-social punishment is absent, prediction is that enabling punishment will increase efficiency versus control.
  - **If**: punishment cost is high or efficiency is low in the control, and/or mechanisms allow anti-social punishment or easy retaliation, the predicted efficiency gain is reduced or may even be negative.
  - **If**: corruption or inefficacy in punishment mechanism is possible, efficiency benefits may be lost unless integrity/monitoring are well-designed (Lee et al., 2015; Lee et al., 2017).
  - **If**: the benefit function is nonlinear (not standard linear PGG), the marginal effect of enabling punishment may be weak or negligible (Archetti & Scheuring, 2013).

- **Extrapolating from Non-payoff Outcomes:**  
  - Papers reporting only on cooperation rates or behavioral outcomes must be used with caution. Higher cooperation rates do not guarantee higher efficiency, especially if the cost of punishment is high or punishment is executed excessively.

- **Control Efficiency Moderates Effect Size:**  
  - When the control game (no punishment) already achieves high efficiency (e.g., due to high MPCR, reputation systems, or small group size), enabling punishment may have a small marginal effect—or, if costs outweigh benefits, even reduce efficiency.
  - When the control efficiency is low, and especially when design parameters make cooperation hard to maintain, punishment is more likely to improve efficiency (if effectively designed).

- **Ambiguity and Disagreement:**  
  - Some mechanistic and evolutionary models yield parameter ranges with multiple stable outcomes; initial conditions or small biases can determine whether full cooperation (high efficiency) or defection (low efficiency) prevails (Lee et al., 2015; Lee et al., 2017; Wolff, 2012; Oya & Ohtsuki, 2017).
  - Disagreement exists in the literature regarding the long-run evolutionary stability of punishment and its cost-benefit balance, especially in the face of anti-social punishment, retaliation, or mutation.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed (specific, recurring, or formally parameterized):**
- `player_count` (group size): Major moderator.
- `num_rounds` (repetition): Major moderator.
- `mpcr` (synergy factor/marginal per-capita return): Direct predictor.
- `punishment_cost` and `punishment_tech` (cost/effectiveness): Central in most theoretical models.
- `all_or_nothing` (discrete vs. continuous contributions): Varies across models, directly parameterized.
- `reward_exists`, `reward_cost`, `reward_tech`: Covered in models exploring reward, combined incentives.
- `show_punishment_id` (punisher anonymity): Direct moderator in retaliation/stability models.
- `show_n_rounds`, `show_other_summaries`: Sometimes parameterized (especially regarding information/monitoring).

**Indirectly informed/contextually discussed:**
- `chat` (communication): Rarely included; usually absent or discussed as a control.
- `default_contrib` (framing): Occasionally mentioned, rarely parameterized.
- `show_other_summaries`: Discussed in reputation/observation contexts.
- `show_n_rounds`: Sometimes included, rarely a major focus.

**Sparse or missing:**
- Detailed interactions among multiple design dimensions (e.g., interaction effects of chat + punishment + group size) are generally not explicitly modeled.
- Effects of default contribution framing, communication/chats, and real-time information flows are typically assumed absent (especially in models focusing on anonymous, one-shot, or strictly structured PGGs).

# 7) Important Limitations

- **Lack of Empirical Calibration:**  
  All evidence is theoretical/simulated, with no empirical effect sizes or validation from laboratory or field data in the reviewed digest.

- **Behavioral vs. Payoff Outcomes:**  
  Many papers focus on strategy dynamics and prevalence of cooperation without translating results to explicit efficiency metrics.

- **Parameter Sensitivity and Context Dependence:**  
  The effect of punishment is highly contingent on cost efficiency, antisocial punishment, retaliation, and population structure, with multiple models showing non-monotonic, mixed, or bistable results for efficiency.

- **Incomplete Coverage of Design Dimensions:**  
  Some game dimensions vital for empirical design—such as communication, dynamic information feedback, and the framing of contributions—are underexplored or absent.

- **Transferability to Laboratory Settings:**  
  Many models assume infinite populations, long evolutionary timescales, or specific update/diffusion rules, which limit precision when mapping to short-term laboratory experiments.

- **Ambiguity for Large Groups and Complex Institutions:**  
  Particularly for larger group sizes or more complex, real-world institutions, the literature is less consistent about whether punishment will reliably yield efficiency gains, especially if corruption, anti-social punishment, or retaliation are possible.

- **Interaction Effects Rarely Modeled:**  
  Few papers explore the joint impact of multiple design features or context-dependent moderators in a way that would enable multivariate prediction using the full set of 14 design dimensions.

---

**In summary:**  
The literature strongly supports the prediction that enabling punishment **can** increase efficiency in public goods games—if designed and implemented carefully, with low punishment cost, high impact, absence of antisocial punishment, and robust institutions. However, numerous studies highlight crucial moderators where the positive effect is weakened, null, or even reversed (especially with antisocial punishment, retaliation, corruption, or high cost). Direct theoretical models provide good qualitative and sometimes quantitative guidance for the main prediction dimensions (group size, rounds, MPCR, cost/effectiveness of punishment), but empirical effect sizes and full mapping for all 14 design dimensions are lacking. Careful attention to the structure and moderators of punishment and to the baseline control efficiency is essential for making accurate predictions informed by this literature set.
