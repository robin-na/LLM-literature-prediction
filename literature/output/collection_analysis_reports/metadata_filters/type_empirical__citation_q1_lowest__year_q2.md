# 1) Evidence Base

The paper set is dominated by empirical, laboratory-based experimental studies (21 of 22 papers), with one observational study. Among the empirical studies, most involve explicit manipulation of game parameters relevant to public goods (PGG) or adjacent social dilemma/bargaining settings. The coverage of topics is broad in terms of experimental manipulations (punishment, communication, information disclosure, hierarchy, exit), but narrow regarding the specific downstream prediction task: the effect of peer punishment on efficiency in standard PGGs and close variants. Many studies focus on non-payoff behavioral outcomes (e.g., cooperation, punishment assignments, fairness perceptions) rather than on group efficiency or payoff-based metrics. Only a minority of the papers combine (a) exact or close relevance to PGG, (b) experimental manipulation of punishment/sanctions, and (c) direct measurement and reporting of efficiency or payoff outcomes. Thus, while the literature is rich in related findings, only a subset directly inform the quantitative prediction of punishment effects on group efficiency.

---

# 2) Task Relevance

**pgg_or_variant:**
- **Exact relevance**: Several papers (e.g., Hugh-Jones & Perroni, 2017; Otto & Bolle, 2016; Zhosan & Gardner, 2013; Vermeer et al., 2016) use PGGs or very close resource dilemma variants as their core design.
- **Close/Adjacent/Weak/None**: Many others use games adjacent to PGG (ultimatum, coordination, effort tasks, indirect reciprocity, contest/participation, etc.), with a few having weaker or no relevance.

**punishment_or_sanctions:**
- **Exact**: Some studies implement classic peer punishment or sanctioning mechanisms (deduction points, direct fines/penalties, exclusion, expropriation, endogenous audit).
- **Close/Adjacent**: Others employ hierarchical allocation, participation, indirect punishment, disapproval voting, or non-monetary forms (feedback, exit, emotional adjustments), which may serve as functional substitutes or analogs.
- **None**: Several studies do not include any punishment or sanctioning mechanism.

**efficiency_or_related_payoff_outcome:**
- **Exact/Close**: Direct measurement of group efficiency or aggregate payoff is present in some studies (notably Hugh-Jones & Perroni, Zhosan & Gardner, Otto & Bolle, Gaudeul et al., dos Santos et al., Becchetti et al.).
- **Adjacent/Weak/None**: Many other studies focus on non-payoff behavioral outcomes (e.g., compliance, contribution rate, norm enforcement, punishment preference, participation), without directly connecting these to efficiency or group payoffs.

**Summary:** Only a subset of the literature is of exact or close relevance on all three dimensions. There is better coverage for adjacent mechanisms (hierarchy, exit, reputation, information provision), but direct evidence for the core prediction task is limited.

---

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes:**
- **Directly measured efficiency or group payoff**: Some studies report group efficiency (group earnings relative to the fully cooperative benchmark) (e.g., Hugh-Jones & Perroni, Zhosan & Gardner, Otto & Bolle), or closely related aggregates (mean payoff, welfare, surplus).
- **Indirect or proxy outcomes**: Average participant earnings, production, or welfare are occasionally reported, or can be inferred from design, but not always linked directly to efficiency ratios.

**Non-payoff behavioral outcomes:**
- **Common outcomes**: Contribution rate, cooperation rate, compliance (with rules/taxes), frequency and targeting of punishment or sanctions, punishment preferences, effort level, participation/turnout, exclusion rates, and emotional/motivational responses.
- **Note:** Several studies observe that higher compliance or cooperation due to punishment does not necessarily translate to higher efficiency, due to punishment costs or strategic responses (e.g., anti-social or excessive punishment, defensive strategies, or exclusion).

**Distinction maintained:** The digest and this analysis explicitly maintain the distinction between payoff-based outcomes and behavioral rates.

---

# 4) Main Findings Relevant To Prediction

- **Punishment can increase efficiency, but only under specific design conditions:**
    - When punishment is *difficult to coordinate* and thus well-targeted (e.g., minimum group size required for expropriation is high), efficiency increases sharply compared to no-punishment controls. When easy and arbitrary, punishment reduces group efficiency (Hugh-Jones & Perroni, 2017).
    - Sanctioning mechanisms that permit credible threat and are well-structured to target low contributors without being easily misused achieve higher group efficiency.

- **Communication and monitoring:**
    - Communication alone substantially raises efficiency (Zhosan & Gardner, 2013), sometimes more than punishment. Adding sanctions to communication provides further but more modest efficiency gains. However, public feedback/monitoring in the absence of sanctions can *reduce* efficiency (Becchetti et al., 2015).

- **Alternative mechanisms:**
    - Hierarchical allocation (e.g., central allocator/principal selection, not punishment) can *substitute* for peer punishment and achieve even higher efficiency than standard PGG or PGG+punishment (Otto & Bolle, 2016).

- **Exit and exclusion:**
    - Allowing easy exit (as a punishment/substitute) tends to lower group efficiency due to overuse and pessimism, unless it is tightly controlled or costly (Gaudeul et al., 2017).

- **Cognitive context and misuse:**
    - High cognitive load or excessive, antisocial punishment reduces or nullifies expected efficiency gains from punishment, even in well-designed games (dos Santos et al., 2014).
    - Punishment may increase compliance/participation without raising (or even reducing) efficiency, depending on how costs and benefits are distributed (Hsu, 2013; Myers, 2016).
    - Information structure and salience of mechanisms (e.g., whether punishment is public, whether punishment/reward can credibly shift the equilibrium) are moderating factors (Liu & Riyanto, 2017; D'Exelle & Riedl, 2013).

- **Summary of ambiguity:** The effect of enabling punishment is not uniformly positive; it depends on punishment technology, group size, communication, information flows, possibility of misuse, and context. In some designs, punishment reduces efficiency compared to control.

---

# 5) Prediction Guidance

For downstream prediction of treatment (punishment-enabled) efficiency based on design and control efficiency:

- **Punishment improves efficiency when...**
    - The punishment mechanism is *hard to coordinate*, so it is used selectively and credibly targets defectors.
    - Communication is also enabled, supporting norm consensus, and monitoring supports effective targeting of punishment.
    - Control game efficiency is low due to free-riding, and punishment can address this without excessive cost.
    - Social distance is low, and punishment is salient to those punished.

- **Punishment harms or does not improve efficiency when...**
    - Punishment is *too easy* to use, leading to arbitrary, antisocial, or excessive application.
    - Cognitive constraints, ambiguity, or history enable antisocial punishment or reduce effective targeting.
    - The cost of punishment is high and not offset by gains from increased cooperation.
    - Other mechanisms (e.g., hierarchy, communication alone) can achieve similar or higher efficiency without punishment.
    - Control game efficiency is already high (little free-riding to address), limiting the marginal benefit of punishment.

- **Prediction interpretation:** When predicting treatment efficiency:
    - Use control efficiency as a baseline, but adjust for punitive design dimensions, especially punishment technology (coordination requirement, targeting ease), punishment cost, and interaction with communication or monitoring.
    - Do not expect uniformly positive (additive) effects of punishment; anticipate context dependence and possible efficiency losses when mechanisms are poorly designed.

---

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions:**
- **player_count**: Almost all studies report and sometimes manipulate group size; some findings suggest effect moderation by group size, but only few directly link size to punishment effects on efficiency.
- **num_rounds**: Most studies use repeated games; findings indicate that number of rounds can matter for learning, targeting, and ratcheting effects.
- **mpcr**: Regularly reported; acknowledged as crucial in determining the baseline social dilemma severity and potential for cooperation, but few papers directly test its interaction with punishment.
- **punishment_cost** and **punishment_tech**: Central to several studies, especially Hugh-Jones & Perroni (group expropriation technology), Zhosan & Gardner (monetary sanctions), D'Exelle & Riedl (voting rules), dos Santos et al. (cognitive/misuse context).
- **chat**/**communication**: Varied in several experiments (Zhosan & Gardner, Vermeer et al., Gaudeul et al.).
- **all_or_nothing**, **default_contrib**: Manipulated in some studies, but rarely a focus of punishment efficiency analysis.
- **show_n_rounds**, **show_other_summaries**: Sometimes varied/toyed with to alter information structures and transparency.
- **reward_exists**, **reward_cost**, **reward_tech**: Covered in studies comparing punishment and reward effects (Liu & Riyanto; Koenig & Riley), but not always combined with payoff measurement.
- **show_punishment_id**: Studied in the context of anonymity vs. publicity (Koenig & Riley).

**Indirectly addressed or contextually discussed:**
- **Heterogeneity** and identity cues are sometimes considered as moderators but not standard dimensions.
- **Contextual factors** (social distance, cognitive load, environment) receive mention as sources of inefficiency or effectiveness.

**Missing or sparsely informed dimensions:**
- The interaction effects among all 14 dimensions are rarely systematically investigated.
- Some dimensions (e.g., default_contrib, reward_tech/reward_cost, show_punishment_id) are only contextually discussed, if at all, and not mapped to efficiency outcomes.

---

# 7) Important Limitations

- **Limited direct evidence:** Only a minority of studies provide all the elements (exact PGG, explicit punishment, direct efficiency or group payoff measures) necessary for high-confidence quantitative predictions across the full design space.
- **Sparse coverage of interaction effects:** Few papers systematically vary multiple design parameters (e.g., punishment tech and cost and communication) to allow assessment of interaction effects.
- **Heterogeneous outcome focus:** Many studies prioritize behavioral outcomes over efficiency, making it necessary to infer payoff implications that are not always straightforward.
- **Context dependence and ambiguity:** Findings emphasize the context dependence of punishment's effect; mechanisms that help in one setting can harm in another (e.g., if punishment is arbitrary, misused, or poorly designed).
- **Adjacent game types:** A substantial portion of the literature examines adjacent or analogous games (ultimatum, coordination, indirect reciprocity), which may not generalize quantitatively to classic PGG outcomes.
- **Absence of designs with all 14 dimensions represented:** No single study comprehensively spans all the predictor dimensions, and some dimensions are only marginally, if at all, addressed.
- **No strong theoretical models for efficiency prediction:** The paper set lacks robust theory papers offering generalizable efficiency predictions from design dimensions and control efficiency.
- **Measurement differences:** Efficiency is sometimes operationalized differently across studies, limiting direct comparability.
- **External validity:** Most evidence is from lab settings with small groups and short time horizons, potentially limiting the generalizability to field or long-run settings.

---

**Conclusion:**  
The literature set provides strong but context-dependent evidence that peer punishment can improve efficiency in public-goods-game-like settings, but only when punishment is well-targeted, not easily misused, and game design supports effective norm enforcement. Serious risks of efficiency loss arise when punishment mechanisms invite arbitrary, costly, or antisocial punishment, or when other design features (e.g., communication, hierarchy) can substitute for peer sanctions. Prediction models should pay special attention to the technology and cost parameters of punishment, the presence of communication, cognitive and informational frictions, and base-level control efficiency. However, ambiguity, heterogeneity of outcome focus, and partial or adjacent evidence leave important gaps for high-precision predictions.
