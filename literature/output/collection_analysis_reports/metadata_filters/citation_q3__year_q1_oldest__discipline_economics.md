# 1) Evidence Base

The paper set comprises 42 papers, nearly evenly split between empirical (mostly lab and field experiments) and theoretical/modeling studies. There is a moderately broad coverage of public goods games (PGGs), close variants (especially common-pool resource [CPR] and coordination games), and adjacent environments such as trust, ultimatum, and contest games. Empirical studies often use standard PGG or CPR experiments with and without punishment, while theory papers introduce a variety of equilibrium models capturing norms, reputation, group structure, and heterogeneity. 

On the downstream prediction task—predicting the effect of enabling peer punishment on efficiency—this literature set is moderately broad for mechanisms and contexts, but only a subset directly measures and reports relevant payoff-based efficiency outcomes under PGG designs with punishment toggled.

# 2) Task Relevance

**pgg_or_variant:**  
- _Label:_ Most papers are `exact` (classic PGG), `close` (CPR games, step-level/threshold PGGs, group coordination games), or `adjacent` (dyadic PD, trust, contest, ultimatum settings).
- _Assessment:_ There is substantial direct evidence for the standard voluntary contributions PGG and for group contest/resource extraction games; adjacent but less directly relevant evidence comes from PDs, trust, and organizational settings. Some papers (e.g., Zultan, 2012; Stringham, 2011) are not relevant to PGGs.

**punishment_or_sanctions:**  
- _Label:_ Coverage is strong: many papers are `exact` (costly punishment in PGG with peer or centralized mechanisms), some are `close` (expulsion, reputation, nonmonetary sanctions, enforced contributions), and a few are `adjacent` (mechanisms that function as punishment without explicit costly sanctions).
- _Assessment:_ Peer and centralized punishment are both studied, as are sanction intensity/cost, random punishment, expulsion, and nuanced institutional forms.

**efficiency_or_related_payoff_outcome:**  
- _Label:_ Several papers are `exact` (reporting group efficiency or total payoff), others are `close` or `adjacent` (group success rate, welfare, surplus, average earnings), and many more focus only on behavioral outcomes (`non_payoff_behavior`) like contribution rates or cooperation frequency.
- _Assessment:_ Direct measurement of efficiency or welfare as a function of enabling punishment is present but not universal; many studies focus primarily on behavioral, not payoff, outcomes. In some papers, payoff outcomes are inferred or proxied (e.g., step-level provision rates).

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:**  
  - Direct: Group efficiency (relative to full cooperation), total group payoff, surplus, welfare, step-level provision rate, or average coins/earnings (e.g., Gürerk et al., 2009; Fatas et al., 2010; Bracht et al., 2008; Masclet & Pénard, 2012).
  - Indirect: In some papers, efficiency is not directly reported but inferred from contribution/provision or by proxy (e.g., threshold attainment rate, group income).
- **Non-payoff behavioral outcomes:**  
  - Contribution/cooperation rates, punishment frequency, norm compliance, conditional cooperation, and group extraction levels are much more common as primary outcomes (e.g., Kocher et al., 2012; Hayo & Vollan, 2012).
  - Some studies provide detailed process data (e.g., punishments assigned, targeting, timing) but not group payoff.

Distinguishing these is critical as increases in cooperation does not guarantee improvements in efficiency, which can be offset by the costs of punishment.

# 4) Main Findings Relevant To Prediction

**A. Direction and Moderators of Punishment Effects:**
- The effect of enabling punishment on efficiency is **mixed** and highly **context-dependent**.
    - _Positive efficiency effects_ are often observed in games with low baseline efficiency, larger groups, strong or credible punishment, and matching information/monitoring structures (e.g., Noailly et al., 2009; Fatas et al., 2010).
    - _Zero or negative efficiency effects_ emerge when baseline contributions are already high (little margin for improvement), punishment costs are high relative to its effect, or there is significant anti-social punishment or retaliation (e.g., Gürerk et al., 2009; Kocher et al., 2012).
    - Under centralized punishment, efficiency gains are more likely if the mechanism is calibrated (e.g., Guillen et al., 2007).
    - In certain **theoretical models**, punishment can crowd out intrinsic motivation or trust, even reducing efficiency (Orr, 2001; van der Weele, 2012).
    - Baseline/control efficiency is a strong moderator: higher baseline efficiency via norms, communication, or framing reduces the marginal benefit (and sometimes flips the sign) of enabling punishment.

**B. Design Features and Mechanism Details Matter:**
- **Punishment cost and effectiveness:** Efficiency gains depend on whether the punishment is sufficiently strong/deterrent, and whether costs are recycled or lost to the group (Fatas et al., 2010).
- **Form and Targeting of Punishment:** Centralized punishment and local punishment can have different effects; non-targeted or random forms can be wasteful or even harmful.
- **Information feedback:** Observability of actions and who punishes whom affects efficiency; anonymity can affect behavior and retaliation.
- **Voluntary participation:** The combination of voluntary entry and punishment is critical—punishment may boost efficiency under voluntary regimes but not when participation is compulsory (De Silva et al., 2010).
- **Social and motivational context:** Heterogeneity in social background, trust, and preference composition (altruism, reciprocity) crucially moderate the effect (Hwang & Bowles, 2012; Kocher et al., 2012).

**C. Distinction Between Payoff and Behavioral Outcomes:**
- Punishment nearly always increases or sustains higher **contribution rates** or **cooperation**, but this does **not always translate into higher efficiency** due to the direct cost of punishment (Kocher et al., 2012; Gürerk et al., 2009).
- Some reward/positive incentive (even net-positive transfer) mechanisms can outperform punishment on efficiency, especially when costs of punishment are high or majority of group members are highly cooperative anyway.

**D. Theory and Model Outcomes:**
- Theoretical work provides explicit equilibrium conditions for when punishment can support high efficiency (Tarui et al., 2008; Noailly et al., 2009) and identifies network structure, type composition, and monitoring as critical moderators (Haag & Lagunoff, 2006; Saak, 2012).
- However, details such as learning, stochastic play, and out-of-equilibrium dynamics are typically abstracted.

# 5) Prediction Guidance

**How Should This Literature Inform Prediction?**

- **Baseline efficiency is key:**  
  The control efficiency (with punishment disabled) is a strong predictor of the potential marginal benefit from enabling punishment. If control efficiency is high (e.g., due to communication, norms, or framing), punishment often offers **little or no gain**, and may reduce efficiency due to punishment costs (Gürerk et al., 2009; Kocher et al., 2012; van der Weele, 2012).

- **Game design dimensions matter:**  
  Dimensions such as `player_count`, `num_rounds`, `mpcr`, `punishment_cost`, and whether punishment is centralized or peer-based (`punishment_tech`) all have documented moderating impacts. For example:
    - Larger groups may initially benefit more from punishment, but overly large groups may dilute incentives and reduce sustainability (Tarui et al., 2008; Noailly et al., 2009).
    - High punishment cost can negate payoff gains from increased cooperation (Fatas et al., 2010; Kocher et al., 2012).
    - Centralized punishment often yields more predictable or positive efficiency effects than peer punishment, but can be costly to administer (Gürerk et al., 2009; Guillen et al., 2007).

- **Punishment does not uniformly increase efficiency:**  
  Predict a positive effect only when baseline efficiency is low and punishment is both effective and not too costly. Predict negligible or negative effects when baseline efficiency is high, punishment is weak (not deterrent), costs are high, or anti-social punishment is rife.

- **The effect is path-dependent and context-sensitive:**  
  History of behavior, path dependence, and the opportunity for communication or social learning affect outcomes (Gürerk et al., 2009; van der Weele, 2012).

- **Unmeasured factors can intervene:**  
  Social/motivational heterogeneity is often both crucial and unobserved in experimental designs. Prediction should account for possible unmeasured moderators.

# 6) Design Dimensions Highlighted Across Papers

Among the 14 prediction dimensions:

**Directly Informed:**  
- `player_count`, `num_rounds`, `mpcr`, `punishment_cost`, `punishment_tech` are included in many experimental designs and/or model parameters, with clear empirical or theoretical sensitivity to their values.
- `all_or_nothing` (binary vs. continuous contribution) is mapped in most models and experiments.
- `chat` (communication) is repeatedly identified as a major moderator of cooperation and efficiency.
- `reward_exists`, `reward_cost`, `reward_tech` are addressed where positive incentives are compared to punishment.
  
**Indirectly Informed:**  
- `show_other_summaries`, `show_n_rounds`, `show_punishment_id` are sometimes present in experiment methods, showing that information structure and transparency can matter, though not always isolated.
- `default_contrib` (framing) is discussed in papers examining framing effects on control efficiency.
- `punishment_magnitude` (effect of punishment delivered)—sometimes discussed via the impact ratio or punishment technology.

**Only Contextually Discussed or Sparse:**  
- Some dimensions, like `show_punishment_id` (whether the identity of punishers is revealed), are only mentioned in passing or flagged as possibly influential but not systematically varied or reported.
- The mapping from `show_other_summaries` to behavioral effects is more assumed than directly tested.
  
**Missing:**  
- Few papers empirically manipulate or systematically report on the effects of `show_punishment_id`, `default_contrib`, or detailed reward/punishment implementation subtleties on efficiency.
- Outright missing are systematic, multi-dimensional studies where the 14-dimensional space is covered factorially.

# 7) Important Limitations

- **Behavioral vs. payoff measurement:**  
  Many studies prioritize behavioral outcomes (contribution, cooperation) over direct efficiency or group payoff, which means inference to outcomes relevant for prediction is sometimes indirect.

- **External validity / generalizability:**  
  Some findings depend on specific experimental or cultural contexts. For example, social background, motivation composition, and cultural norms can moderate the effect, but are not captured in standard prediction dimensions (Kocher et al., 2012; van der Weele, 2012).
  
- **Punishment implementation details matter:**  
  Effects differ under peer vs. centralized punishment, anonymous vs. identified punishment, and with different cost-to-impact ratios, but not every study measures these aspects distinctly.

- **Design variables are not orthogonally manipulated:**  
  There is a lack of studies systematically and independently varying all design features, so estimates of interaction effects and general functional form are sparse.

- **Theoretical results may not capture experimental nuances and vice versa:**  
  Theory often presumes rational, patient, homogeneous agents and equilibrium play, while experiments reveal heterogeneity, learning, and irrationality.

- **Absence of robust quantitative effect sizes:**  
  For many combinations of design dimensions (especially rarely tested modes), only qualitative or theoretical guidance is available rather than parameterized prediction rules.

- **Limited direct empirical evidence on some dimensions:**  
  Some important information variables (`show_punishment_id`, `show_other_summaries`) and the details of reward impact are rarely independently tested for their effect on efficiency.

---

**Summary:**  
The literature directly supports that the effect of enabling punishment in PGG-like environments on efficiency is **context-dependent** and moderated by both design parameters (player count, rounds, MPCR, punishment cost/technology) and the initial level of group efficiency absent punishment. The evidence is strongest for settings with low control efficiency and effective punishment; weakest or most ambiguous where control is already efficient, punishment is costly/ineffective, or social context inhibits payoff improvements. Most, but not all, prediction dimensions are at least partially informed, but limitations in design coverage and focus on non-payoff outcomes temper forecasts in under-studied corners of the design space.
