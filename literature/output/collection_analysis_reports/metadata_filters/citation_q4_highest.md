# 1) Evidence Base

**Composition and Breadth:**  
The literature base comprises a large and diverse set of studies, the majority of which are empirical laboratory experiments with exact public goods game (PGG) structures, and a significant number of theoretical and simulation studies. The majority are experimental lab studies (n > 100), closely mirroring PGG or linear voluntary contribution mechanism (VCM) designs. There are also field experiments, cross-cultural comparisons, and many adjacent/prisoner’s dilemma (PD) or threshold public good variants.

**Empirical vs. Theory:**  
The empirical studies directly measure efficiency or related payoff outcomes in both baseline (no punishment) and punishment-enabled conditions, often manipulating key design dimensions like group size, rounds, MPCR, and punishment cost/tech. Theory papers complement by mapping parameter space, identifying mechanisms or moderators, but with less direct empirical grounding for quantitative effect sizes.

**Coverage for Prediction Task:**  
The evidence base is **broad and rich for the core downstream task**—predicting the effect on efficiency of enabling peer punishment in PGG-like environments, conditional on control efficiency and game design. The strongest and most numerous findings concern linear PGGs with 3-5 players, 6-30 rounds, continuous contributions, and standardized 1:3 or 1:2 punishment cost:impact ratio. Several critical moderators (e.g., antisocial punishment, group heterogeneity, counter-punishment, cultural context) are also covered, though coverage is thinner for very large groups, ecological field contexts, and highly nonstandard PGGs (e.g., optional participation, very high/low MPCR, dynamic/threshold games).

---

# 2) Task Relevance

### PGG or Variant (`pgg_or_variant`):
- **Exact**: The majority of empirical lab studies, both baseline and with punishment, use canonical PGG (VCM) or linear public goods design. Many theory and evolutionary papers model PGGs or threshold generalizations.
- **Close/Adjacent**: Some evidence is from CPR games, threshold public goods, dyadic trust/PD games, and reputation-based allocation games, which are structurally very similar and often included in meta-analyses of punishment effects in public-good contexts.
- **Weak/None**: Where only dictator or ultimatum games, or non-experimental/observational studies are used, task relevance is limited.

### Punishment or Sanctions (`punishment_or_sanctions`):
- **Exact**: Most key experiments manipulate peer punishment as an institution (e.g., Fehr & Gächter, 2000; Sefton et al., 2007; Sutter et al., 2010), directly enabling or disabling costly punishment.
- **Close**: Several studies focus on exclusion/ostracism, reward, reputation, or institutionalized forms of punishment (e.g., centralized/law-based punishment), which function as strong substitutes or complements for peer punishment.
- **Adjacent/Weak**: Some studies focus on related mechanisms (e.g., indirect reciprocity, reputational cues, partner choice) but do not implement literal punishment.

### Efficiency or Related Payoff Outcomes (`efficiency_or_related_payoff_outcome`):
- **Exact**: Many studies measure group efficiency as the main dependent variable—the ratio of actual total payoff to maximum possible (fully cooperative) payoff.
- **Close**: Others report surplus, group earnings, or welfare, which can be mapped to efficiency.
- **Adjacent**: Numerous studies use average contribution, cooperation rate, or punishment frequency as the main outcome, which, while important, are not direct efficiency measures and must be distinguished.
- **Weak**: Several papers only report behavioral motives, emotional responses, or hypothetical behavior rather than actual payoff or efficiency.

**Conclusion:**  
The literature set is of **high direct relevance** for the prediction task of estimating average efficiency with punishment enabled, conditional on control efficiency and design dimensions, especially for canonical PGG lab experimental designs.

---

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes (High direct relevance):**
- **Efficiency/group efficiency**: Ratio of realized group payoff to the optimal (all-cooperate) benchmark is directly measured in most high-impact experiments (e.g., Fehr & Gächter, 2000; Sefton et al., 2007; Sutter et al., 2010; Fehr & Fischbacher, 2002; Grüerk et al., 2006; Markussen et al., 2014).
- **Group/average earnings, welfare, surplus**: Used as close proxies or directly mapped to efficiency, often reported per round or as an aggregate.
- **Total coins generated, average profit**: Sometimes used in simulated or evolutionary models.

**Non-payoff behavioral outcomes (Must be separately interpreted; do not equate with efficiency):**
- **Contribution rate, cooperation rate**: Widely reported (e.g., as average % of endowment contributed). Correlated with efficiency, but efficiency may be lower even if contributions rise (if punishment is costly).
- **Punishment frequency, punishment assigned, norm compliance**: Often analyzed to explain mechanisms, not as the primary outcome for welfare prediction.
- **Trust, fairness ratings, satisfaction**: Reported in some adjacent/dyadic trust game studies, not as group welfare or efficiency.
- **Emotional responses, reputation/trust judgments**: Inform mechanism but not direct payoff outcomes.

**Key distinction:**  
While **increased contributions often predict increased efficiency**, this is not always true—**punishment costs may offset or reverse the efficiency gains from higher cooperation** (e.g., Nikiforakis 2008; Egas & Riedl 2008; Gächter & Herrmann 2011; Balliet et al., 2011). Prediction must be anchored in payoff-based outcomes, not just behavioral changes.

---

# 4) Main Findings Relevant To Prediction

**A. Baseline Result ("Canonical Lab PGGs"):**
- Enabling costly peer punishment **almost always increases group efficiency** relative to the no-punishment baseline when control efficiency is low (i.e., when cooperation decays under baseline), provided that punishment is reasonably effective (cost-to-impact ratio ≥ 1:2 or better), and conditions such as communication, partner identification, and repeat interaction are stable (Fehr & Gächter, 2000, 2002; Sefton et al., 2007; Sutter et al., 2010; Arechar et al., 2018; Gintis et al., 2003; Andreoni & Gee, 2012).

**B. Critical Moderators Identified in the Literature:**
- **Punishment Cost-Effectiveness**: Efficiency gains are highest when punishment is cheap/effective (cost:impact ≤ 1:3); if punishment is expensive or weak, costs may outweigh cooperative gains (Anderson & Putterman, 2006; Egas & Riedl, 2008).
- **Antisocial/Perverse Punishment**: When punishment is frequently directed at cooperators or arbitrarily, especially in some cultural contexts (Gächter & Herrmann, 2011; Nikiforakis, 2008; Balliet et al., 2011), group efficiency can decrease below control.
- **Monitoring and Information**: With **imperfect/noisy monitoring** of others' behavior, punishment may become mistargeted and reduce efficiency (Ambrus & Greiner, 2012; Grechenig et al., 2010; ABREU et al., 1991; Levine & Pesendorfer, 2007). Accurate feedback supports efficiency gains.
- **Possibility of Counter-Punishment/Feuds**: If the punished can retaliate, or cycles of counter-punishment are permitted, welfare losses can emerge (Nikiforakis & Engelmann, 2011; Denant-Boemont et al., 2007).
- **Feedback Structure ("show_other_summaries")**: Whether feedback is about contributions, earnings, or both can moderate efficiency effects (Nikiforakis, 2010). Showing earnings (not just contributions) can increase punishment or reduce convergence, lowering efficiency.
- **Motivational/Emotional Framing**: Conditions that allow emotional venting (Dickinson & Masclet, 2015) or which manipulate mood (Drouvelis & Grosskopf, 2016) modulate the frequency and efficiency of punishment.
- **Group Heterogeneity & Norm Conflict**: In groups with **strong differences in marginal returns, ethnic/cultural background, or status**, punishment is less likely to increase efficiency (Barclay, 2004; Reuben & Riedl, 2009, 2013; Gächter & Herrmann, 2011).

**C. Institutional Features:**
- **Endogenous Institution Formation** (voting on punishment or reward): Efficiency is higher when groups choose to adopt punishment institutions, especially if selection is by majority (Markussen et al., 2014; Sutter et al., 2010; Tyran & Feld, 2006; Putterman et al., 2011).
- **Centralized vs. Peer Punishment**: Delegated or centralized punishment is sometimes more efficient than pure peer punishment, due to lower cost and better targeting (Gross et al., 2016; Andreoni & Gee, 2012; Kube & Traxler, 2011).
- **Exclusion/Ostracism**: Exclusion as a punishment mechanism can lead to even higher efficiency (Cinyabuguma et al., 2005; Maier-Rigaud et al., 2010; Masclet, 2003).

**D. Communication and Reputation:**
- Enabling **communication** (chat, face-to-face) dramatically increases both contributions and efficiency, often more so than punishment (Bochet et al., 2006); combining chat and punishment yields the highest efficiency.
- **Reputation/reward** mechanisms can also increase efficiency and sometimes outperform punishment in net payoff (Rand et al., 2009; Hilbe et al., 2014; Milinski, 2016).

**E. Special Contexts Where Punishment Reduces Efficiency:**
- **Low Trust, High Baseline Efficiency**: In settings where control efficiency is already high, adding punishment can lower net earnings (Anderson & Putterman, 2006; Guala, 2012).
- **Antisocial Contexts/Cultures**: In some regions (e.g., parts of Russia, as per Gächter & Herrmann, 2011; Wu et al., 2009), or in contest/war-like PGG variants (Abbink et al., 2010; Gross & De Dreu, 2019), punishment reinforces destructive norms, reducing efficiency.

**F. Time Dynamics:**
- Efficiency gains from punishment are often small or negative in early rounds (when punishment is frequent and costly), but increase in later rounds as cooperation stabilizes and less punishment is needed (Fehr & Gächter, 2000; Sefton et al., 2007; Arechar et al., 2018).

**G. Adjacent Mechanisms:**
- Mechanisms such as partner choice, reputation, communication, and exclusion can substitute for or out-perform punishment in raising efficiency, especially with endogenous group formation (Charness & Yang, 2014; Charness et al., 2011; Page et al., 2005).

---

# 5) Prediction Guidance

- **General rule:**  
  **If the control game with punishment disabled shows low-to-moderate efficiency and is a canonical repeated linear PGG, then enabling a well-designed, peer punishment mechanism (cost:impact at least 1:2) is likely to increase average efficiency, often by 10-40 percentage points.** (Fehr & Gächter, 2000, 2002; Sefton et al., 2007; Arechar et al., 2018; Gintis et al., 2003; Sutter et al., 2010; Andreoni & Gee, 2012; Guala, 2012; Markussen et al., 2014).

- **Magnitude of effect:**  
  The predicted efficiency gain is greatest in:
  - Small groups (3-5)
  - Repeated games with at least 6-10 rounds
  - Games with clear feedback and accurate monitoring
  - Control efficiency < 0.75 (i.e., baseline groups failing to self-sustain cooperation)
  In such settings, predicted efficiency with punishment enabled can approach or even exceed 0.90, especially as punishment use declines over time.

- **Adjustment for cost/effectiveness of punishment:**  
  - If punishment is expensive (cost:impact > 1:3), or weak (impact limited), the treated efficiency may be only moderately higher or even similar to control (Anderson & Putterman, 2006; Egas & Riedl, 2008).
  - If antisocial punishment or counter-punishment is prevalent, efficiency can decline (Nikiforakis, 2008; Gächter & Herrmann, 2011; Wu et al., 2009).
  - If information about others' contributions is noisy or delayed, efficiency gains are reduced or negative (Ambrus & Greiner, 2012; Grechenig et al., 2010; ABREU et al., 1991).

- **Interaction with other mechanisms:**  
  - If communication (chat) is also enabled: expect higher efficiency than punishment alone.
  - If both reward and punishment are enabled: efficiency is generally highest when both present and properly tuned, sometimes higher than either alone, especially with endogenous institution choice (Rand et al., 2009; Sutter et al., 2010; Putterman et al., 2011).
  - If norm-targeting (e.g., exclusion filtered against antisocial punishment; Ertan et al., 2009) or consensus rules are in place, further efficiency gains may occur.

- **Special cases:**  
  - In one-shot, non-repeated, anonymous PGGs, enabling punishment has little or negative effect on efficiency (Gächter & Herrmann, 2011).
  - Where punishment can be countered/avenged/cycled: can reduce or reverse efficiency gains (Nikiforakis & Engelmann, 2011).
  - In environments with strong antisocial punishment, low trust, or poor information, enabling punishment can lower average efficiency compared to control (Gächter & Herrmann, 2011; Wu et al., 2009).

- **Predictive sufficiency of control efficiency and design dimensions:**  
  - Most lab results suggest that, holding control efficiency and core dimensions (player count, rounds, MPCR, cost/tech, feedback structure) fixed, enabling punishment reliably shifts efficiency upward—unless key negative moderators are present (antisocial punishment, noisy monitoring, counter-punishment, severe norm conflict).
  - For non-canonical PGGs (threshold goods, very large groups, field experiments), effect sizes are less predictable: consult studies reporting on similar moderators.

---

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- **player_count**: Strong empirical coverage, but most studies use small groups (3-5); efficiency effects are well-characterized for these sizes, with declining reliability for larger groups (>10).
- **num_rounds**: Well-covered, with longer repeated games (>6-10 rounds) showing a larger positive efficiency effect from punishment.
- **mpcr** (marginal per-capita return): Many studies vary MPCR; higher MPCR increases the marginal effectiveness of punishment on efficiency.
- **punishment_cost, punishment_tech**: Frequently and systematically manipulated; cost-to-impact ratio is a critical moderator.
- **show_other_summaries, show_n_rounds**: Several studies manipulate information feedback, demonstrating its impact on punishment targeting and efficiency (Nikiforakis, 2010; Ambrus & Greiner, 2012).
- **all_or_nothing, default_contrib**: Less systematically varied, but both continuous and all-or-nothing designs are represented.
- **reward_exists, reward_cost, reward_tech**: Well-covered in studies comparing reward vs. punishment effects.
- **chat**: Multiple studies manipulate chat/communication and find strong effects on efficiency.

**Indirectly Informed or Only Contextually Discussed:**
- **show_punishment_id**: Some studies test anonymity vs. identifiability of punishers, but results on efficiency are less systematic.
- **punishment existence/absence (treatment/control)**: The core manipulated feature throughout the paper set.

**Effectively Missing or Weakly Covered:**
- **Very large group sizes (>10)**
- **Dynamic/endogenous group formation (except in a handful of studies)**
- **Field context with environmental uncertainty, resource feedback, or high social complexity**
- **Highly nonstandard PGGs (e.g., optional participation, dynamic thresholds, CPRs with ecological feedback)**
- **Time horizon uncertainty and sophisticated strategic uncertainty (rarely the focal manipulation)**

---

# 7) Important Limitations

**1. Laboratory Context and Population:**  
The overwhelming majority of strong evidence comes from lab experiments with undergraduates in Western contexts; generalizability to field, ecological, or highly heterogeneous real-world collective action is imperfect.

**2. Cultural and Social Context Effects:**  
Cross-cultural studies (Gächter & Herrmann, 2011; Wu et al., 2009; Reuben & Riedl, 2009) show large differences in punishment targeting, trust, and efficiency effects—**design dimensions alone are not sufficient for prediction when cultural context is a major moderator.**

**3. Antisocial Punishment and Norm Conflict:**  
In settings with strong antisocial punishment or norm heterogeneity (due to culture, group composition, or ambiguous rules), enabling punishment can reduce, not raise, efficiency—control efficiency is not a sufficient predictor.

**4. Monitoring and Information Structure:**  
If feedback is delayed, noisy, or error-prone, the efficiency benefit of punishment is sharply reduced and may be negative (Ambrus & Greiner, 2012; Grechenig et al., 2010).

**5. Crowding-out, Retaliation, and Counter-punishment:**  
Punishment can undermine intrinsic motivation (Guala, 2012), and opportunities for retaliation or feuds can cause welfare loss (Nikiforakis & Engelmann, 2011; Balliet et al., 2011).

**6. Limited Range of Punishment Parameters:**  
Most studies use standard 1:3 or 1:2 cost:impact ratios; effects for much higher or lower ratios are less certain. Very expensive or weak punishment may not increase efficiency (Anderson & Putterman, 2006).

**7. SSRN and Pre-published/Unpublished Results:**  
Some theoretical claims, especially regarding complex ecological or demographic moderators, are supported in principle but lack robust direct empirical testing.

**8. Overlap Between Behavioral and Payoff Outcomes:**  
Many papers report only cooperation/contribution rates rather than efficiency; effects on efficiency can diverge from effects on contribution (costly punishment outweighing gains).

**9. Dynamic and Threshold/Nonlinear PGGs:**  
Evidence is sparser for games with threshold, nonlinear, or dynamic resource components (but see some CPR, threshold, and contest literature).

---

**In summary:**  
Laboratory and theoretical evidence robustly supports a **substantial positive effect of enabling peer punishment on efficiency** in canonical repeated PGGs, provided that monitoring is accurate, antisocial punishment is rare, and punishment is reasonably effective and not costly. Control efficiency, combined with design dimensions such as group size, rounds, MPCR, punishment cost/tech, and information structure, is usually sufficient for strong prediction—**unless** there is strong norm conflict, high antisocial punishment, cultural mismatch, weak monitoring, or confounding institutional features (e.g., counter-punishment, retaliation, or poorly targeted punishment). Adjust predictions downward or even to zero/negative when such moderators are present, as empirically shown in studies on Russia, contest/war games, and noisy/anonymous or norm-diverse contexts. Design dimensions are well mapped in the literature, except for rare or highly specialized variants.
