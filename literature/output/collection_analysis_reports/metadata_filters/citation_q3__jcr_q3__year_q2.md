# 1) Evidence Base

The paper set is moderately broad, encompassing 34 papers, with a significant mix of **empirical experimental studies** (notably lab experiments and some field studies) as well as a sizeable number of **theoretical and simulation-based analyses**. The **majority of high-relevance papers are empirical lab experiments focused directly on public goods games (PGGs) with punishment, reporting both behavioral and payoff outcomes**. The theoretical papers often address complex variants, structured populations, or related games (Prisoner's Dilemma, resource dilemmas, etc.), with several providing explicit welfare or efficiency analyses. There are also empirical and theoretical contributions that are **adjacent**—addressing related games, non-payoff outcomes, or mechanisms indirectly relevant for prediction.

# 2) Task Relevance

### `pgg_or_variant`
- **Exact Relevance**: Several empirical and theoretical papers analyze standard public goods games or their linear variants (e.g., Kuwabara & Yu, 2017; Faillo et al., 2013; Kamijo et al., 2014; Dercole et al., 2013; Archetti & Scheuring, 2013; Oya & Ohtsuki, 2017).
- **Close/Adjacent**: Many theory papers address close variants such as common-pool resource games or multi-player Prisoner's Dilemma (Lee et al., 2015/17; Wilson & Wu, 2017; Zhang et al., 2017; Iwasa & Lee, 2013).

### `punishment_or_sanctions`
- **Exact Relevance**: Many top papers directly manipulate or model punishment enabling/disabling, cost, structure, or legitimacy, with controlled experimental or modeled interventions.
- **Close/Adjacent/Weak**: Some papers only discuss punishment contextually, treat reward mechanisms as alternatives, or focus on non-costly enforcement or information.

### `efficiency_or_related_payoff_outcome`
- **Exact Relevance**: At least 10 papers report or model group efficiency, total payoff, or welfare as the main outcome, and several use incentive-compatible lab designs allowing clean inference about treatment effects on efficiency. A further subset report only contribution rates but in settings where efficiency is a monotonic function of contributions.
- **Adjacent/Weak/None**: Several empirical papers only address cooperation rates, norms, or other behavioral outcomes; a handful do not address efficiency or payoff at all.

**In summary:** The core of the paper set is highly relevant, with multiple studies directly measuring the main prediction endpoint; a substantial perimeter addresses highly related games or behavioral proxies, which must be interpreted carefully when mapping to efficiency outcomes.

# 3) Outcomes Measured In The Literature

### **Payoff-Related Outcomes**
- **Direct Measures**: Efficiency (defined as actual group payoff/maximum possible), group earnings, surplus, welfare, or total coins generated—reported in both experiments and theory (Kuwabara & Yu, 2017; Faillo et al., 2013; Kamijo et al., 2014; Oya & Ohtsuki, 2017; Dercole et al., 2013; Archetti & Scheuring, 2013; Lee et al., 2015/17).
- **Indirect but Strong Proxies**: Average contribution rate (in linear PGGs, this maps directly onto efficiency), sometimes the only reported outcome.
- **Related but Distinct**: Resource collapse/survival, frequency of efficient cooperation, cost/benefit analyses.

### **Non-Payoff Behavioral Outcomes**
- Contribution rate/cooperation rate, frequency or nature of punishment assigned, trust, reputation, norm compliance, social appraisals, willingness to enforce or maintain norms, etc. These appear in both experimental and theory papers (Irwin et al., 2014; Nelissen & Mulder, 2013; Eriksson et al., 2017; Jung et al., 2014).

**Distinction is usually maintained, with frequent reminders in the better studies as to the limitations of inferring payoff/efficiency from behavioral outcomes.**

# 4) Main Findings Relevant To Prediction

### **Empirical and Theoretical Consensus (Under Standard PGG)**
- **Enabling peer punishment in standard PGGs generally increases group efficiency if punishment is costly (Kuwabara & Yu, 2017; Kamijo et al., 2014)**, but only under certain structures.
- **Costless peer punishment can decrease efficiency** due to excessive, antisocial, or retaliatory punishment (Kuwabara & Yu, 2017).
- **Restricting punishment to legitimate (prosocial) use and providing full feedback about contributors robustly increases efficiency** relative to unrestricted punishment or baseline (Faillo et al., 2013).
- **Centralized/designated punishment tends to reduce inefficient, excessive punishment relative to unrestricted peer punishment**; efficiency can be highest with costly, well-structured punishment institutions (Kuwabara & Yu, 2017; Kamijo et al., 2014).
- **The cost and efficiency of punishment (i.e., ratio of penalty to cost) are critical moderators**: high efficiency is achieved only if punishment is strong enough to deter defection, not overly cheap, and not overused (Kamijo et al., 2014; Dercole et al., 2013; Oya & Ohtsuki, 2017).
- **Population structure matters:** Punishment improves efficiency primarily in structured populations or where enforcement is perceived as legitimate; in well-mixed populations, it may not sustain cooperation or efficiency (Oya & Ohtsuki, 2017; Archetti & Scheuring, 2013).

### **Key Moderators Identified**
- **Feedback and information:** Full feedback about group members' actions enhances the beneficial effect of legitimate punishment (Faillo et al., 2013).
- **Legitimacy/Restriction of punishment:** Limiting punishment to higher contributors improves efficiency; unrestricted punishment leads to antisocial punishment and lower efficiency (Faillo et al., 2013).
- **Design of punishment institutions:** Relative (targeted) punishment outperforms absolute (blanket) punishment unless punishments are extremely strong (Kamijo et al., 2014).
- **Institutional honesty/efficacy:** In centralized, delegated, or third-party punishment, honest enforcement is required for efficiency; corrupt institutions destroy efficiency (Lee et al., 2015; Lee et al., 2017).
- **Non-linear benefit functions:** In non-linear (threshold/sigmoid) PGGs, high efficiency may be sustainable even without punishment; punishment has its largest benefit in linear (N-person PD) games (Archetti & Scheuring, 2013).
- **Group size and MPCR:** Larger groups, lower MPCRs, and weak sanctioning make efficiency harder to attain, but institutional structure and targeted punishment can moderate these effects (Dercole et al., 2013).
- **Reward mechanisms:** Carefully calibrated rewards may achieve or surpass efficiency publicized by punishment, but excessive rewards may backfire (Shibayama, 2015).

### **Ambiguities, Conflicts, and Edge Cases**
- Some settings report that **costly punishment does not increase efficiency above control if the baseline cooperation is already high**; strong punishment may have negative reputational side effects or undermine long-term trust (Irwin et al., 2014; Nelissen & Mulder, 2013).
- **In real-world or field settings, punishment and enforcement are less frequent and efficient than in laboratory games**, raising concerns for generalizability (Berger & Hevenstone, 2016).
- **Punishment can sometimes lead to meta-stable states, hysteresis, or bistability, implying that small differences in population, history, or institution yield very different efficiency results** (Hintze & Adami, 2015; Lee et al., 2015/17).

### **Non-Payoff Outcomes**
- Increased contribution or cooperation rates (in lieu of direct efficiency gains) almost always accompany enabled punishment if adequately structured, but overuse or antisocial punishment can offset payoff gains.

# 5) Prediction Guidance

### **Direct Prediction Guidance**
- **If the control (no-punishment) game has low efficiency:** Enabling peer punishment (especially if it is costly, restricted to legitimate targets, and accompanied by full feedback) is highly likely to raise efficiency, possibly near the theoretical maximum, unless the group suffers from antisocial or excessive punishment (Kuwabara & Yu, 2017; Faillo et al., 2013; Kamijo et al., 2014).
- **If punishment is unrestricted, costless, or antisocial:** Efficiency can actually decrease, even below no-punishment control, due to retaliatory or excessive punishment.
- **Cost of punishment (`punishment_cost`) is a key moderator:** Moderate to high costs promote legitimate, targeted punishment and higher efficiency; too low costs promote wasteful punishment and reduce efficiency.
- **Feedback mechanisms:** Enabling feedback that reveals all contributions and actions supports the beneficial effect of punishment.
- **Centralization and legitimacy:** Delegated or institutionally controlled punishment generally increases efficiency if the institution is honest and trusted.
- **Non-linear benefit functions:** If the PGG has non-linear returns, enabling punishment may add little to efficiency due to already stable, high-cooperation equilibria; in standard linear PGGs, punishment is generally necessary for sustaining high efficiency (Archetti & Scheuring, 2013).
- **Population/game structure:** In structured populations or where spatial/network ties exist, punishment can sustain higher efficiency, but in well-mixed settings, its effects are weaker or even negative (Oya & Ohtsuki, 2017).

### **Quantitative Mapping**
- **Direct empirical results (lab):** Reported efficiency increases vary from negligible or negative (costless, unrestricted peer punishment) to substantial (costly, legitimate, full-feedback treatments), depending on the match to empirical parameter regimes.
- **Theoretical models:** Give explicit efficiency/payoff predictions as formulas or equilibrium values; useful as priors or upper/lower bounds for prediction.

### **Limitations on Prediction**
- **Where only behavioral (not payoff) outcomes are available:** Map cooperation/contribution rates to efficiency only where benefits are linear and all contributions are paid out equally; otherwise, treat as qualitative or low-confidence predictors.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- `player_count`: Carefully manipulated in both experiments and models; larger groups often reduce baseline efficiency, but effect of punishment is robust across sizes within tested regimes.
- `num_rounds`: Standard in repeated games; longer repetition can support higher efficiency with punishment, but decay may occur without enforcement.
- `mpcr`: Modeled and measured in most high-relevance papers; interacts with cost of cooperation and effectiveness of punishment.
- `punishment_cost`: Core moderator, directly informed; central to punishment's effect on efficiency.
- `punishment_tech`: Institution type (peer, centralized, relative vs. absolute, legitimate vs. unrestricted)—directly informed.
- `all_or_nothing`: Both all-or-nothing and continuous variants are addressed.
- `chat`: Explicitly manipulated in some lab studies; often not present (communication mostly prohibited).
- `show_other_summaries`: Feedback about peer actions is a critical moderator.
- `show_n_rounds`: Present in some models/papers as a parameter affecting reputation and cooperation strategies.
- `show_punishment_id`: Salient in studies modeling third-party or delegated punishment, enforcer honesty.
- `reward_exists`, `reward_cost`, `reward_tech`: Reward mechanisms considered in a subset of theory papers.
- `default_contrib`: Rarely varied, sometimes noted in behavioral framing studies.
- `punishment_magnitude`: Sometimes parametrized alongside cost, not always distinct from punishment_tech.

**Indirectly/Contextually Informed:**
- Feedback/information structure (partly mapped to `show_other_summaries`, `show_n_rounds`, `show_punishment_id`) is a frequent but sometimes indirectly addressed topic.
- Institution legitimacy and restriction correspond to forbidden/allowed punishment, which maps partially to `punishment_tech`, but is institutionally specific.

**Effectively Missing or Sparse:**
- Detailed manipulation or systematic variation of `default_contrib`, `reward_cost`, `reward_magnitude/tech`, and in-depth analysis of chat/communication effects are rare.
- Some parameters (e.g., chat, default_contrib, reward_cost) are usually held constant, considered minor, or not isolated in primary findings.
- Few studies examine joint interactive effects of more than 3–4 design dimensions at once; most evidence is conditional/univariate/multivariate within experimental constraints.

# 7) Important Limitations

1. **Generalizability:** Most direct evidence comes from standard, laboratory PGGs with fixed (often small) group sizes, limited rounds, restricted communication, and simplified partner matching. Findings may not generalize to large, dynamic, or real-world groups.

2. **Structure of Punishment Institutions:** The detailed specification of punishment (peer vs. central, cost/magnitude, restriction, transparency) substantially alters the outcome; many studies focus on a narrow slice of the possible institutional architectures. Evidence is sparser for decentralized, real-world, or complex institutional settings.

3. **Baseline Efficiency:** The counterfactual (no-punishment) efficiency level is not always reported or systematically varied; results may strongly depend on initial baseline efficiency.

4. **Non-Payoff/Behavioral Outcomes:** Several papers only report contributions/cooperation as proxies, not actual group payoffs; translation to efficiency is valid only in standard (linear) PGGs without benefit nonlinearities or unequal distributions.

5. **Population and Context Effects:** Several findings highlight that **cultural context, real-world settings, and group composition** can dramatically alter rates of enforcement and thus efficiency. Field evidence is limited and sometimes in tension with lab results.

6. **Identifiability and Feedback:** Features like identification of punishers or full feedback are sometimes confounded with other institutional changes; pure estimates of feedback effects are rare.

7. **Nonlinearity, Hysteresis, and Multiple Equilibria:** Some models show multiple, path-dependent equilibria (e.g., bistability, meta-stability), implying that simple mapping from design to efficiency may fail in some parameter regimes.

8. **Missing Dimensions and Multifactor Interactions:** Not all 14 design dimensions are directly manipulated or jointly analyzed; evidence on multi-way interactions is extremely limited.

**Conclusion:** The literature provides moderately strong, directionally consistent evidence for mapping many, but not all, game design features (especially punishment institution structure, cost, group size, MPCR, and information feedback) to expected treatment efficiency in PGG-like environments, given known control efficiency. However, robustness is limited by generalizability, unaddressed design dimensions, and the complexities of mapping institutional nuance to quantitative prediction. Direct application to games highly dissimilar from lab-standard PGGs or with highly atypical parameter values should be undertaken with caution.
