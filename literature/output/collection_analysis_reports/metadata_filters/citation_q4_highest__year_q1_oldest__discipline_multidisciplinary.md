# 1) Evidence Base

**Composition:**  
The paper set is broad and includes both empirical (laboratory and field experiments, observational studies) and theory/modeling papers. A substantial subset (about 15–20 papers) provide *exact* evidence on standard public goods games (PGGs) with peer punishment and report payoff-based outcomes (efficiency, group payoff). Another meaningful subset addresses *close* variants (e.g., common-pool resource games, indirect reciprocity, networked or dynamic partner games), with a significant number focusing on *adjacent* or related experimental paradigms (trust games, ultimatum, animal cooperation).  
**Scope for Prediction Task:**  
- The literature is collectively rich for standard linear PGGs with and without peer punishment, especially regarding repeated interactions, punishment cost/impact, and the presence of reputation or reward.
- Empirical results are mostly from controlled lab experiments, while some field and naturalistic studies provide context or evidence on cross-societal variability or applied environments.
- Theory papers supply mechanistic insights into how design dimensions moderate the effects of punishment on efficiency, often mapping phase transitions, equilibria, or bistability.
- However, some key design dimensions for fine-grained prediction are only sparsely or contextually discussed (e.g., chat, show_other_summaries, show_punishment_id, default_contrib, reward mechanics).

**Summary:**  
The evidence base is robust for the core prediction task—predicting the change in efficiency when enabling peer punishment in standard repeated PGGs or their closest variants. However, for less canonical designs or when complex moderators (e.g., communication, varying group size, social context) are involved, direct evidence thins and contextual effects become salient.

---

# 2) Task Relevance

**pgg_or_variant:**  
- *Exact:* Many studies focus on standard linear PGGs with N=3–6, repeated rounds, and continuous/all-or-nothing contribution.
- *Close:* Several studies involve CPR games, indirect reciprocity, or multi-dyadic exchange frameworks closely related to PGGs in structure/outcome.
- *Adjacent/Weak:* A number of papers use trust games, dictator/ultimatum games, animal mutualisms, or other settings—valuable for mechanism exploration but less direct for PGG efficiency outcomes.

**punishment_or_sanctions:**  
- *Exact*: Punishment (peer, pool, centralized) is manipulated or modeled directly in many papers.
- *Close/Adjacent*: Some examine related behaviors (ostracism, exclusion, negative reciprocity, network updating, symbolic punishment, or reward as an alternative).
- *Weak/None*: A good subset addresses only baseline or control behavior (no punishment), or treats reward, reputation, or recordkeeping mechanisms exclusively.

**efficiency_or_related_payoff_outcome:**  
- *Exact/Close*: Many core studies measure (or closely infer) group efficiency, total earnings, or surplus; others directly report increases in group payoff as a ratio to the social optimum.
- *Adjacent/Weak*: Several report only contributions, cooperation rates, punishment frequency, or norm compliance, requiring careful interpretation if used as efficiency proxies.

---

# 3) Outcomes Measured In The Literature

**Payoff-based outcomes (directly relevant):**
- Efficiency: Group payoff as a fraction of optimal
- Total earnings/welfare/surplus: Aggregate monetary or resource outcomes, sometimes expressed as a ratio
- Group average payoffs (sometimes called “welfare”)
- Comparative payoff analysis between treatments (with vs. without punishment)

**Non-payoff behavioral outcomes (contextual):**
- Contribution rates/level
- Cooperation/defection frequency
- Frequency, severity, or targeting of punishment
- Norm compliance, fairness-based choices, reputation effects
- Punishment assigned/received, or antisocial punishment frequency

**Distinction:**  
While contribution/cooperation rates are often (but not always) correlated with efficiency, the literature shows they can diverge—e.g., if punishment is used extensively and is costly, group payoff may *not* rise, despite increased contributions.

---

# 4) Main Findings Relevant To Prediction

**Synthesis of Findings:**

- **Punishment Enables Higher Efficiency, But Not Universally:**
  - *Canonical PGGs*: Enabling costly peer punishment almost always increases group efficiency versus control (no punishment), by raising and sustaining contributions and deterring free riding (Fehr & Gächter, 2002; Gürerk et al., 2006; Rockenbach & Milinski, 2006; Eldakar & Wilson, 2008). In some environments, efficiency can reach 90–95% of the optimum when punishment is available, particularly in repeated games with stable group membership.
  - *Limits/Exceptions*: If punishment is heavily used or not well-targeted, its cost can offset or even exceed contribution gains, leading to neutral or negative efficiency effects. Some societies or contexts show high "antisocial punishment" (punishment of cooperators), which diminishes or even reverses efficiency gains (Herrmann et al., 2008; Rand & Nowak, 2011).

- **Critical Moderators:**
  - **Punishment Cost and Effectiveness:** Lower costs and higher impact-to-cost ratios for punishment yield stronger efficiency improvements (Fehr & Gächter, 2002; Eldakar & Wilson, 2008). Excessive punishment cost or weak impact causes diminished or negative returns.
  - **Reputation & Observation:** Efficiency gains from punishment are much greater when reputational mechanisms are in play—when players can observe or infer others’ actions, punishment is used more efficiently and less destructively (Rockenbach & Milinski, 2006; Sigmund et al., 2010; Hilbe & Traulsen, 2012).
  - **Voluntary/Opt-Out Participation:** Enabling voluntary participation (loner/exit option) amplifies the positive impact of punishment on efficiency by allowing defectors to self-select out or be excluded, thus stabilizing cooperative, high-efficiency equilibria (Sasaki et al., 2012; Hauert et al., 2007; Brandt et al., 2006).
  - **Second-Order Free Riders:** Efficiency improvements from institutional (pool) punishment require that second-order free riders (non-punishing cooperators) are also sanctioned; otherwise, punishment is unsustainable and efficiency gains vanish (Perc, 2012; Sigmund et al., 2010).
  - **Antisocial Punishment:** In contexts or societies where defectors punish cooperators (“antisocial punishment”), efficiency may not rise, and can even fall when punishment is enabled (Herrmann et al., 2008; Rand & Nowak, 2011).

- **Reward vs. Punishment:**  
  - Direct material reward mechanisms can match or even outperform punishment in raising efficiency, as the cost structure is less destructive (Rand et al., 2009).

- **Communication/Chat:**  
  - In some field/lab CPR experiments, communication among participants raises efficiency more reliably than punishment, and when both are present, the marginal effect of punishment may vanish or become negative (Janssen et al., 2010).

- **Group Size, MPCR, and Rounds:**  
  - Smaller groups, higher MPCRs (more effective public good), and longer games generally amplify efficiency gains from punishment, though effects are often robust across a range (Eldakar & Wilson, 2008; Sigmund et al., 2010; Fehr & Gächter, 2002).
  - However, the negative impact of group size on efficient punishment is suggested where information/reputation is blurred in larger groups (Hilbe & Traulsen, 2012).

---

# 5) Prediction Guidance

- **General Expectation**:  
  For standard repeated linear PGGs, enabling peer punishment increases efficiency relative to the no-punishment control game, especially when:
   - Punishment is not prohibitively expensive,
   - The group is not too large,
   - Players can observe others’ actions/reputations, and
   - Antisocial punishment is rare.

- **Quantitative Patterns:**  
  Group efficiency rises sharply upon introduction of punishment in most controlled lab PGGs, sometimes reaching >90% of maximum possible (Gürerk et al., 2006; Fehr & Gächter, 2002). In societies with high antisocial punishment, or where punishment is used inefficiently, gains are muted or absent (Herrmann et al., 2008).

- **Modulation by Design Dimensions:**
  - *Punishment Cost (punishment_cost)*: High punishment cost erodes or reverses gains; effects are optimized at moderate or low costs (Fehr & Gächter, 2002; Eldakar & Wilson, 2008).
  - *Reputation/Observation (show_punishment_id, show_other_summaries)*: Transparency enhances the impact of punishment on efficiency (Rockenbach & Milinski, 2006; Sigmund et al., 2010).
  - *Reward Exists (reward_exists, reward_cost, reward_tech)*: When both punishment and reward are possible, efficiency may be highest when reward is used more than punishment (Rand et al., 2009).
  - *Opt-Out/Voluntary Participation (all_or_nothing, optional entry)*: Substantially amplifies punishment’s efficiency-boosting effect and reduces the required severity of punishment to stabilize cooperation (Hauert et al., 2007; Sasaki et al., 2012).
  - *Communication (chat)*: Communication boosts efficiency independently or more than punishment in CPR-like settings; punishment may not provide additional benefit (Janssen et al., 2010).

- **Control Game Efficiency Use:**  
  The efficiency of the control game (without punishment) provides a strong baseline, but punishment can produce a non-linear jump in efficiency, sometimes regardless of low baseline efficiency, especially when punishment is well-designed and appropriately targeted. However, in contexts prone to antisocial punishment, the control’s efficiency may already reflect population-level tendencies that diminish the marginal returns from enabling punishment.

- **Caveats:**  
  Where antisocial punishment, high punishment cost, a lack of transparency/reputation, or second-order free riders are prevalent, enabling punishment **may not** increase efficiency, and could worsen outcomes (Herrmann et al., 2008; Rand & Nowak, 2011; Perc, 2012).

---

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions (frequent strong evidence):**
- `player_count` (group size): Many papers discuss or manipulate this.
- `num_rounds`: Varies across studies; effects for repeated vs. single-shot well-covered.
- `mpcr`: Marginal per-capita return a standard parameter.
- `punishment_cost`: Key moderator; often reported and varied.
- `punishment_tech` (who can punish, peer vs. pool vs. centralized): Modeled/experimented in several papers.
- `all_or_nothing`: Some papers use all-or-nothing contributions; both types represented.
- `reward_exists`: Crossover between reward/punishment often analyzed directly.

**Indirectly Informed or Contextually Discussed:**
- `chat` (communication): Discussed as a moderator (especially in CPR/field settings), sometimes manipulated.
- `show_other_summaries`, `show_punishment_id`: Discussed in terms of transparency, reputation, or observation, but less systematically manipulated.
- `punishment_magnitude`: Occasionally specified alongside cost, but less often independently varied.

**Sparse or Missing Evidence:**
- `default_contrib` (opt-in/opt-out framing): Little direct manipulation or reporting.
- `reward_cost`, `reward_tech`, `reward_magnitude`: Some evidence but far less systematic than for punishment.
- `show_n_rounds`: Sometimes controlled, but not typically varied as a treatment.
- Nuanced interface/UX factors (e.g., prominence of punishment option, user feedback) are almost never a focus.

---

# 7) Important Limitations

- **External Validity & Context Dependence:**  
  Most lab-based results apply best to standard, anonymous, repeated PGGs in WEIRD (Western, educated, industrialized, rich, democratic) populations. Real-world, cross-cultural, or complex group contexts (field/observational studies) show marked variability—most notably due to antisocial punishment (Herrmann et al., 2008), social norms, or group integration (Alexander & Christia, 2011).
  
- **Non-linearity and Contingency:**  
  The impact of enabling punishment is often non-linear and highly contingent on multiple design and contextual factors (punishment cost, group size, likelihood of antisocial punishment, transparency, communication, voluntary participation). Simple linear extrapolation from control efficiency is unreliable in the presence of strong moderators.

- **Payoff vs. Behavior:**  
  Many studies infer efficiency gains from behavioral increases in cooperation or contributions, but extensive evidence shows that high punishment-use, or poorly targeted punishment, can erode these gains, or even reduce overall efficiency.

- **Design Dimension Coverage:**  
  Certain prediction dimensions are underexplored or manipulated only in narrow contexts (default contribution framing, detailed reward parameters, interface visibility, nuanced information exposure).

- **Second-order Effects and Stability:**  
  Sustainability of efficiency gains often depends on second-order free rider suppression, which is rarely manipulated directly in lab PGGs but is central in theory papers. Models show abrupt transitions between low- and high-efficiency states, raising questions about stability and sensitivity to initial conditions.

- **Treatment Control Matching:**  
  Some studies do not always align baseline and treatment games on all dimensions except the punishment variable, complicating strict causal attribution.

---

**Overall**, the literature provides strong guidance for predicting that enabling peer punishment in repeated, standard PGGs with appropriate design features increases efficiency over control games, often substantially. However, the realized effect is highly sensitive to game parameterization and social context, with several critical moderators (cost/impact, reputation, communication, voluntary participation, group size, antisocial punishment, population norms) shaping the magnitude and even the direction of the effect. Direct evidence is richest for canonical PGGs varied by punishment cost, group size, and repetition; predictions for outlier environments, novel mechanisms, or complex field scenarios are necessarily more speculative.
