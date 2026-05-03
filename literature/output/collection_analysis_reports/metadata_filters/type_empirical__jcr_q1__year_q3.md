# 1) Evidence Base

The paper set comprises a large, diverse collection of predominantly **empirical laboratory experiments** (with some field experiments and observational studies) focused on cooperation, punishment, and sanctioning in public-goods-game (PGG) or closely related environments. For the **downstream prediction task**—predicting efficiency change when peer punishment is enabled—this paper set is **broad, methodologically robust, and specifically oriented toward PGGs**, especially within the “exact” and “close” relevance tier. The set includes studies with varying institutional designs (peer, centralized, democratic punishment), cost/impact ratios, observability conditions, information structures, and additional mechanisms like reward, communication, or network structures.

While much of the literature directly reports on **payoff-based outcomes** (efficiency, group payoff, welfare) under various punishment regimes, a significant portion measures only **non-payoff behavioral outcomes** (contribution or cooperation rates, punishment frequency, norm compliance). The theoretical papers are sparse; most mechanism reasoning is embedded in empirical discussion rather than formal modeling. Taken together, the set provides abundant, but sometimes heterogeneous, data on the causal effects of punishment and mediators thereof.

# 2) Task Relevance

**pgg_or_variant**:  
- **Exact relevance** dominates for studies using standard linear PGGs—with varying player counts, rounds, and MPCR—but there is also strong coverage of close variants (CPRs, trust games, networked games, and threshold games).  
- A subset is **adjacent**: e.g. trust games, contest/team games, dyadic games; these are useful as boundary evidence but less directly transferable.

**punishment_or_sanctions**:  
- The set includes exhaustive coverage of **peer punishment** (the main mechanism for the prediction task), with adequate representation of centralized, democratic, and hybrid sanctioning structures.  
- There is also breadth in exogenous enforcement, exclusion, and reward mechanisms. Some studies focus instead on social information, reputation, or alternative forms of enforcement, which are **contextually related**.

**efficiency_or_related_payoff_outcome**:  
- The payoff–efficiency axis is well-covered, with many papers measuring group earnings, profit, welfare, or surplus as a **primary outcome**.  
- However, a notable share (**especially in behavioral or mechanism-focused papers**) reports only on contributions/cooperation or punishment frequency, requiring assumptions for mapping behavior to efficiency, which can be problematic if sanction costs are high or anti-social punishment is frequent.  
- There are also papers reporting “adjacent” or “close” payoff domains or providing only indirect evidence through related constructs (e.g., final wealth, distributional outcomes, group allocation).

**Overall assessment**: The evidence is **highly relevant** to the specific prediction task—especially for classic PGGs, peer punishment, and efficiency outcomes—but some caution is warranted in extrapolating findings where either the outcome is not payoff-based, or the institutional design diverges from the prediction environment.

# 3) Outcomes Measured In The Literature

- **Payoff-based outcomes (“efficiency or related payoff”)**:  
  - Direct: Efficiency (ratio to social optimum), group payoff/welfare, profit, surplus, total earnings, welfare improvements, average coins.  
  - Close proxies: final wealth, surplus, group allocation, average earnings.
  - Some studies specifically report changes in efficiency relative to a control (no-punishment) baseline.

- **Non-payoff behavioral outcomes:**  
  - Contribution rate, cooperation frequency, norm compliance, sanctioning (punishment) frequency, reward frequency, types of punishment (pro-social, anti-social, hypocritical), norm perceptions, and satisfaction/fairness ratings.

- **Boundary or mechanism outcomes:**  
  - Inequality (Gini coefficient), group composition, fairness/norm perception, group composition effects (pro-social punisher fraction), information/monitoring accuracy, leadership and institutional design effects.

- **Distinction maintained:**  
  - Many studies increase contributions with punishment, but if cost of sanctioning is high, **efficiency may decline** (i.e., higher cooperation, but lower group payoff due to costly punishment).
  - Some papers only **infer efficiency** (from contributions) or discuss related mechanisms; these must be interpreted cautiously for payoff prediction.

# 4) Main Findings Relevant To Prediction

**Most informative and consistent findings (empirical):**
- *Peer punishment in standard PGGs*:  
  - Enabling peer punishment **often increases efficiency** (group payoff) relative to control, but this is conditional:
      - **Punishment cost** must not outweigh gains from increased cooperation. If punishment is frequent/costly or misapplied (anti-social, counterpunishment), efficiency can decline despite higher contributions (Burton-Chellew & Guérin, 2021; Nockur et al., 2021; Heine & Strobel, 2020).
      - **High control efficiency** (baseline without punishment) predicts little or negative efficiency gain from punishment (Bühren & Dannenberg, 2021). When control efficiency is already high, punishment often reduces net efficiency due to its cost.
      - **Low control efficiency**: When baseline contributions/payoff are low, enabling punishment (especially severe and well-targeted) can produce substantial **efficiency gains** (Gordon & Puurtinen, 2021; Ertör-Akyazi, 2019).

- *Institutional and design moderators:*
  - **Centralized or democratically controlled punishment** (vs. purely peer): Tends to be more efficient, primarily because it reduces welfare-destroying, redundant, or anti-social punishment. Efficiency increases most under democratic/centralized structures when the central actor is motivated to enforce cooperation (Harrell, 2019; Castillo & Hamman, 2021; Ambrus & Greiner, 2019; Nockur et al., 2021).
  - **Monitoring/information quality**: Cheap, accurate monitoring dramatically increases punishment's effect on efficiency (Nicklisch et al., 2021). Without good information, punishment can be less effective or counterproductive.
  - **Punishment cost and impact**: A high cost-to-impact ratio dampens efficiency gains and can easily reverse them if the cost is too great or if punishment is excessive or misapplied.

- *Conditional and contextual factors:*
  - **Game structural features:** Alignment between local and global incentives, exclusion of individual solutions (self-reliance options), and the ability to target punishment are critical for whether punishment will improve efficiency (Ozono et al., 2020; Kamijo et al., 2020; Gross & Böhm, 2020).
  - **Information about group composition/cooperativeness**: When groups are highly cooperative without punishment, introducing punishment often lowers efficiency by imposing unnecessary costs (Bühren & Dannenberg, 2021; Nair et al., 2018).
  - **Antisocial punishment/feuds**: High anti-social or reciprocal punishment rates can cause efficiency loss (Gross & De Dreu, 2019; Pleasant & Barclay, 2018).
  - **Behavioral response heterogeneity**: Pro-social vs. anti-social vs. non-punishers within groups create significant variance in effects.

- *Boundary/adjacent domains or mechanisms:*
  - In **CPR or networked environments**, externally imposed or monitored punishment can yield high efficiency gains (Wegmann & Musshoff, 2019; Chávez et al., 2018), but peer-based mechanisms can be less effective or even negative in some contexts, especially if contest or outside options exist (Heine & Strobel, 2020; Gross & De Dreu, 2019).
  - **Exclusion or ostracism** can sometimes outperform direct punishment in raising efficiency.

**Mixed or null findings:**
- When **punishment costs are high, efficacy is low, or use is poorly targeted**, enabling punishment can yield no net efficiency gain or can reduce efficiency (Burton-Chellew & Guérin, 2021; Nockur et al., 2021; Lohse & Waichman, 2020).
- **Reward and punishment together:** Rewards (especially net-positive) consistently outperform punishment for efficiency (Kamijo et al., 2020; Yang et al., 2018; Stoop et al., 2018).
- **Visibility of endowments or outcomes, income transparency, network effects, and social structure** frequently moderate—but do not standardize—the efficiency effects.

# 5) Prediction Guidance

**General implications for predicting treatment efficiency from design dimensions and control efficiency:**

- **Direction and magnitude depend crucially on baseline efficiency:**  
    - If control efficiency is low, punishment is more likely to yield positive efficiency gains (by raising cooperation to profitable levels).
    - If control efficiency is high (cooperation near social optimum), punishment often reduces efficiency (costs exceed marginal gains from small increases in contribution).

- **Key design dimensions directly shaping effect size upon enabling punishment:**
    - *Punishment cost and technology*: Lower cost and higher impact yield greater potential gains, but if both cost and severity are high, risk of net efficiency loss increases.
    - *Institutional structure*: Centralized/democratic punishment institutions (vs. peer punishment) are generally more efficient, as they reduce redundant or anti-social punishment.
    - *Information/monitoring quality (punishment_tech)*: Cheap, precise information boosts efficiency impact of punishment.
    - *Group composition/cooperativeness*: Highly cooperative groups without punishment experience efficiency loss when punishment is added; the reverse is true for low-cooperation groups, especially if participants are aware they need enforcement.
    - *MPCR/all_or_nothing*: Low MPCR or all-or-nothing structures limit capacity for punishment to increase efficiency; sometimes, even high contributions are inefficient.
    - *Player count*: Larger groups dilute effect if monitoring/information is poor; small groups with clear information are most responsive.

- **Indirect or contextually relevant dimensions:**
    - *Chat/communication*: Can substitute for punishment—where communication is possible, baseline efficiency may be high, diminishing the marginal gain from punishment.
    - *Reward exists*: The presence of reward (without punishment) can raise efficiency more than punishment.
    - *Visibility, feedback, and show_punishment_id*: Increased information often increases the effectiveness of punishment, but excessive transparency can backfire by fostering perceptions of unfairness or increasing norm confusion, sometimes suppressing cooperation (Engel, 2019).
    - *Income/endowment transparency*: Revealing information about others’ resources affects whom is punished/rewarded, with implications for efficiency and equality.

- **Cautions:**
    - Non-payoff behavioral outcome findings should never be mapped 1:1 into efficiency predictions. In particular, high contribution rates with high punishment costs do not guarantee higher group payoffs.
    - The effect of punishment is **not monotonic** in any single dimension (e.g., cost, severity, or information). Interaction effects abound.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed (frequently manipulated or measured and directly drawn on for predictive implications):**
- `player_count`: Many studies (3–5 players, sometimes much larger); effect varies with group size, especially via monitoring and dilution of responsibility.
- `num_rounds`: Widely tested (single to 30+ rounds); repeated interaction generally strengthens punishment efficacy.
- `mpcr`: Varied systematically; effect of enabling punishment depends heavily on returns to cooperation.
- `punishment_cost`, `punishment_tech`: Extensively manipulated; central for calibration.
- `all_or_nothing`: Both binary and continuous contribution frames employed; often affects baseline cooperativeness and thus marginal gain from punishment.
- `chat`: Communication/observation included or off in many studies; effects on baseline efficiency provide guidance for expected marginal impact from punishment.
- `show_other_summaries`, `show_punishment_id`, `show_n_rounds`: Information structure/feedback dimensions; several studies manipulate and discuss their effect on norm clarity, detection, and punishment’s efficacy.
- `reward_exists`: Papers distinguishing reward vs. punishment provide clear differential outcome predictions.

**Indirectly or contextually discussed:**
- `default_contrib`: Limited direct manipulation; mostly context, with some findings on framing (but effect is small relative to material incentives).
- `reward_cost`, `reward_tech`: When reward is present; less often compared head-to-head with punishment.
- `show_punishment_id`: Affects transparency and, in some cases, the social cost-benefit calculation for punishing; limited but notable evidence.
- `num_rounds`, as a moderator of institution effectiveness (especially for leadership or “legacy” effects).

**Effectively missing or rarely tested:**
- Co-detailed interaction terms across all these variables are rare (especially more than 3–4 at once).
- The design dimensions are generally **well-covered in the “exact” and “close” paper set**. However, some more exotic or field-environmental features (very large groups, highly fluid groups, endogenous institution selection) are less frequently tested.

# 7) Important Limitations

- **Non-payoff outcome bias**: A sizable literature measures only contributions, not efficiency. Where punishment is costly or misapplied, contributions and efficiency can diverge sharply.
- **Selection on lab convenience**: Most experiments involve small to medium groups of students from WEIRD populations; external validity and generalizability to real-world or high-powered field settings can be limited, especially under endogenous group formation, social ties, and longer-term interactions.
- **Context-specific mechanisms**: Some robust effects (e.g., net-positive efficiency gain from punishment) are contingent on very specific design details—e.g., monitoring, MPCR, institutional framing—so generalization requires careful attention.
- **Ambiguity/disagreement**: Findings on centralization vs. peer punishment; differential effect of punishment under high vs. low control efficiency; and antisocial punishment prevalence yield **real empirical ambiguity**. The expected sign and size of punishment’s effect is therefore sometimes indeterminate from design dimensions alone.
- **Limited joint coverage of all prediction dimensions**: Though all core dimensions are well-represented, few studies simultaneously cross all 14; thus, multivariate predictions may be extrapolations beyond exact-testing environments.
- **Lack of pure mechanism papers**: Most theoretical arguments are embedded in data-driven discussion; formal models are underrepresented.
- **Adjacent and weak-relevance papers**: A significant portion of the latter part of the digest concerns settings too different (dyads, trust games, dictator games, PGGs with no punishment, real-world observational data) to provide strong transfer value, except as qualitative context.

---

**In summary:**  
This literature base is rich, methodologically sound (mainly empirical with direct measurement of efficiency or closely related payoffs in many studies), and highly relevant for predicting the effect of enabling punishment on group efficiency in public goods game-like environments. The evidence supports nuanced, conditional predictions based on game design (especially baseline efficiency, punishment cost and targeting, and institutional structure). The most robust guiding principle is that the efficiency effect of punishment depends strongly on baseline group cooperativeness: punishment is most beneficial when baseline efficiency is low and least or even negative when it is high. Laboratory findings are robust for canonical PGGs, but ambiguity, divergence in findings, and external validity concerns must temper overconfident prediction.
