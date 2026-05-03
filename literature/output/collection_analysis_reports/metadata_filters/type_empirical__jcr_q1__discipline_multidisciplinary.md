# 1) Evidence Base

This paper set is unusually rich, with a very large array of high-quality, recent empirical (mainly lab-experimental) studies examining punishment and payoff-based outcomes in public goods games (PGGs) and closely related environments. The evidence is dominated by empirical, experimental work, with only a handful of observational or theory-based studies. The set is broad and diversified, including not only canonical linear PGG lab studies but also field experiments, studies on variants (e.g., threshold PGGs, contest games), and many works manipulating a wide range of game design features and institutional details. Direct and explicit measurement of group-level efficiency or closely related payoff outcomes is provided in a substantial number of the most central studies, though a significant minority of highly cited studies focus on behavioral measures only (e.g., contributions, norm compliance, punishment rates).

Notably, the literature goes beyond simple presence/absence contrasts for punishment and explores moderators such as punishment cost/effectiveness, identification, noise, institutional structure (peer vs. leader), group composition, centralization, combined reward and punishment regimes, and social/cultural context. While the evidence on most design dimensions is strong for standard four-person, repeated PGGs, coverage for unusual or edge-case design parameters, or for field or large-group settings, is noticeably sparser.

# 2) Task Relevance

### - `pgg_or_variant`
**Exact** relevance dominates: Most key studies implement the standard repeated linear PGG with or without punishment. Several papers cover threshold PGGs, contest games, or close variants (adjacent), but the main empirical base aligns closely with the prediction environment.

### - `punishment_or_sanctions`
**Exact**: The bulk of the central papers manipulate or compare punishment-enabled with no-punishment (control) environments, and most additionally include details about the punishment institution (costs, impact, etc.). Some studies examine combined or alternative sanction regimes (reward, norm signaling, leader vs. peer sanctioning), providing close or adjacent evidence.

### - `efficiency_or_related_payoff_outcome`
**Exact**: A notable fraction directly reports efficiency as the group’s payoff relative to the social optimum, or as net group earnings, welfare, or surplus. Others provide closely related proxies or directly interpretable data (e.g., average group profit, total coins generated, mean final earnings). Some well-known studies, however, focus solely on behavioral variables (contributions, punishment frequency) without explicit efficiency or payoff reporting (adjacent or weak for those).

In summary, direct, high-quality, and well-aligned evidence is available for the downstream prediction task: predicting how peer punishment affects efficiency (group payoff relative to optimum) as a function of game design and control (no punishment) efficiency.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes** (relevance: exact/close for the prediction task):
- **Efficiency**: Ratio of actual group earnings to the maximum possible (full-cooperation) payoff. Directly reported in many central studies (e.g., Fehr & Gächter, 2002; Gächter et al., 2017; Lo Iacono et al., 2023).
- **Group Earnings / Profits / Welfare / Surplus**: Often synonymous with efficiency, used in experiments with varying reporting conventions (e.g., Rand et al., 2009; Gürerk et al., 2006).
- **Total Coins Generated**: Preserves efficiency meaning under certain mappings.

**Non-payoff behavioral outcomes** (not sufficient for task, but often reported):
- **Contribution rate / Cooperation rate**: Most common—typically increase under punishment, but these do not map directly to efficiency if punishment is costly (Simpson et al., 2017; Wu et al., 2016).
- **Punishment frequency/amount, norm compliance, or institutional support**: Useful for mechanism understanding but not equivalent to payoff.
- **Spillovers (e.g., trust in follow-up games), emotion, norm perception**: Contextual/reputational outcomes, not efficiency.

Many studies explicitly note when increased cooperation does not translate to higher efficiency due to punishment costs (e.g., Simpson et al., 2017; Wu et al., 2016; Heine & Strobel, 2020).

# 4) Main Findings Relevant To Prediction

### **General Effect of Enabling Peer Punishment**
- **Positive effects in canonical repeated PGGs**: In basic repeated PGGs with moderate group size, standard cost/impact for punishment, and no extreme costs, enabling peer punishment generally increases efficiency compared to control—sometimes dramatically (Fehr & Gächter, 2002; Gächter et al., 2017; Gürerk et al., 2006; Lo Iacono et al., 2023; Eriksson & Strimling, 2012; Hilbe et al., 2014). The effect is often strongest where baseline cooperation is low.
- **Timing**: Efficiency gains from punishment can be delayed; initial rounds may show lower earnings due to punishment costs, with gains emerging as cooperation stabilizes over time (Chaudhuri & Paichayontvijit, 2017; Fehr & Gächter, 2002).
- **Magnitude varies**: While sometimes efficiency approaches the social optimum (Gürerk et al., 2006), in other settings gains are smaller or absent (Simpson et al., 2017; Wu et al., 2016).

### **Key Moderators and Dimension Effects**
- **Punishment cost/effectiveness**: High punishment costs relative to impact shrink or eliminate efficiency gains (Wu et al., 2016; Simpson et al., 2017).
- **Institutional design**:
    - *Centralized vs. peer*: Centralized or leader punishment usually outperforms peer punishment for efficiency; distribution or uncoordinated peer punishment often leads to waste (Harrell, 2019; Gross et al., 2016).
    - *Second-order punishment*: Including punishment for non-punishers (second-order) can better sustain efficiency (Hilbe et al., 2014; Ozono et al., 2017).
    - *Power centralization*: Voluntary transfer of punishment power can yield higher efficiency (Gross et al., 2016).
    - *Combined reward and punishment*: Combined mechanisms tend to outperform punishment alone for efficiency, and reward can substitute or outperform punishment (Rand et al., 2009; Kamijo et al., 2020; Yang et al., 2018).
    - *Reputation, norm signaling, communication*: Adding norm signals or reputation boosts efficiency gains from punishment (Rockenbach & Milinski, 2006; Andrighetto et al., 2013).
- **Game parameters (player count, rounds, MPCR)**: Efficiency gains from punishment are robust across small group sizes (3-6); long games permit larger cumulative gains (Gürerk et al., 2006; Lo Iacono et al., 2023; Gächter et al., 2017).
- **Punishment noise and antisocial punishment**: When punishment is noisy or antisocial (directed at cooperators), efficiency gains are reduced or reversed (Salahshour et al., 2022; Herrmann et al., 2008).
- **Group structure and heterogeneity**: In uniform/homogeneous groups, punishment increases efficiency. In pluriform/more heterogeneous or diverse groups, punishment can fail or even reduce efficiency due to discrimination or antisocial punishment (Molenmaker et al., 2023; Herrmann et al., 2008; Alexander & Christia, 2011).
- **Contest/competition environments**: In contest-like environments, punishment often leads to over-investment, retaliation, and net reductions in efficiency (Heine & Strobel, 2020; Gross & De Dreu, 2019; Deo et al., 2013).
- **Imperfect monitoring and noise in contributions**: Noisy, imperfect contribution information can induce wasteful or mistaken punishment, reducing efficiency (Salahshour et al., 2022; van Miltenburg et al., 2017).
- **Cultural/social context**: The benefit of punishment for efficiency is not universal, with cultural context and antisocial punishment behaviors shaping effects (Herrmann et al., 2008; Wu et al., 2009).
- **Local vs. global incentives**: When local group welfare does not increase with cooperation, punishment (and reward) becomes less effective for efficiency (Ozono et al., 2020).

### **Boundary and Null Effects**
- In some studies, punishment increases cooperation but not efficiency due to cost offset, or even reduces efficiency (Simpson et al., 2017; Wu et al., 2016; Fehl et al., 2012).
- Especially when punishment cost/impact is low, or when reward or non-material sanctions are available, punishment's marginal efficiency benefit is weak or negative (Rand et al., 2009; Andrighetto et al., 2013; Wu et al., 2016).
- Non-human animal or “adjacent” game structures largely confirm the necessity of punishment for significant, stable cooperation, but don't provide efficiency measurements (various).

# 5) Prediction Guidance

**Summary for predictors:**
- **Control efficiency is a useful but incomplete predictor:** Benchmarking against the efficiency observed in the control (no-punishment) game is best practice, but the predicted effect when peer punishment is enabled depends strongly on *how* punishment is implemented and on key design dimensions.
- **Dimension-specific adjustment is essential:** 
    - *Punishment cost/impact:* Higher punishment effectiveness (stronger fine per cost) predicts greater efficiency gains; high cost/low impact or noisy punishment predicts reduced or even negative effects.
    - *Institutional form:* Peer punishment is generally less efficient than centralized/leader punishment; voluntary power transfers, second-order institutions, or norm-signaling features increase efficiency above standard peer arrangements.
    - *Combined reward/punishment mechanisms and communication:* Prediction should be adjusted upward if communication or norm salience is present alongside punishment, or if reward is available; adjust downward if only punishment is present without these features.
    - *Group structure:* In larger, more diverse, non-anonymous, or pluriform groups, or where identification of group members is suppressed, efficiency gains from punishment are reduced or can become negative.
    - *Noise (in punishment or in feedback):* Prediction should be discounted in environments with noisy punishment technology or contribution feedback—mistakes and antisocial punishment are more common, reducing efficiency.
    - *Cultural/subject pool context:* If enacted in societies or subject pools with high observed antisocial punishment, or where norms do not support prosocial punishment, efficiency gains are not assured.
- **Payoff effects are not always aligned with contributions:** Do not assume that higher contributions under punishment will mechanically translate to higher efficiency—punishment costs can outweigh the gain (Simpson et al., 2017; Wu et al., 2016).

**Quantitative estimate patterns:**
- *Standard repeated, small-group (4-6 players), moderate MPCR, moderate cost/impact peer punishment without communication or leader:* Expect a substantial efficiency increase versus control, sometimes to 80-95% of optimum (Fehr & Gächter, 2002; Gürerk et al., 2006; Lo Iacono et al., 2023; Gächter et al., 2017).
- *Momentum matters:* If control efficiency is very low, and punishment is strong, expect the largest absolute gain. If control efficiency is already high, punishment effect may be smaller, or—if there is overinvestment—punishment can even decrease efficiency due to unnecessary sanctioning (Jiang et al., 2013).
- *With high-cost punishment, antisocial punishment, noisy punishment, or contest structure:* Expect no efficiency gain or an efficiency reduction (Simpson et al., 2017; Fehl et al., 2012; van Miltenburg et al., 2017; Heine & Strobel, 2020).
- *Presence of rewards or norm communication:* Expect higher efficiency than with punishment alone (Rand et al., 2009; Andrighetto et al., 2013).

# 6) Design Dimensions Highlighted Across Papers

**Best informed (directly manipulated/controlled in multiple high-quality studies):**
- `player_count` (group size), `num_rounds` (game length), `mpcr` (marginal per-capita return), `punishment_cost`, `punishment_tech` (cost/impact ratio), `all_or_nothing` (discrete vs. continuous contribution), `chat` (presence/absence), and presence/absence of `reward_exists`.
- Punishment parameters, matching protocol, anonymity, and knowledge of rounds are also well covered.

**Indirectly or contextually discussed:**
- `default_contrib` (contribution framing: opt-in/opt-out)—few studies manipulate this directly.
- `show_n_rounds`, `show_other_summaries`, and `show_punishment_id`—some coverage, but mostly discussed in the context of norm salience, reputation, or feedback (Rockenbach & Milinski, 2006; Milinski et al., 2002; Andrighetto et al., 2013).
- `reward_cost`, `reward_tech`—where combined reward/punishment or reward-only institutions are examined.

**Missing or rarely addressed:**
- Detailed parameterization of `default_contrib`, `show_n_rounds`, and `show_punishment_id` as individual moderators is generally missing or analyzed only as part of broader intervention packages.
- `show_other_summaries` (detailed peer feedback, comparison to group) is sometimes reported but often not the main manipulated dimension.

**Moderators often critical but not always mapped to dimensions:**
- Group composition (homogeneity, identity, leadership), social/cultural background, and cross-cultural factors are critical moderators but are not always tied to an explicit prediction dimension.
- Institutional learning, facilitation, and endogenous vs. exogenous institution choice receive sporadic but important coverage.

# 7) Important Limitations

- **Behavioral-outcome-dominant evidence:** Many studies report only on contribution rates and not directly on efficiency or net payoff, requiring caution when inferring efficiency effects, especially where punishment is costly or antisocial.
- **Heterogeneity and context sensitivity:** The effect of punishment on efficiency is highly sensitive to design details and contextual moderators—cultural background, group structure, and institutional specifics—meaning that control efficiency and high-level design dimensions are sometimes insufficient for precise prediction.
- **Sparse evidence for edge-case or unusual parameterizations:** Designs with very large groups, high punishment cost/inefficiency, high or low MPCR extremes, or combinations of rare features (e.g., reward + punishment + public identification) are less represented.
- **Weak/no coverage for some dimensions:** Some prediction variables (default contribution framing, detailed feedback/visibility controls) are sparsely tested as independent predictors.
- **Potential selection/publication bias:** The literature may over-represent positive or canonical findings, though strong evidence for null and negative effects is present for certain contexts.
- **External validity to field or naturalistic settings:** The bulk of strong evidence is from laboratory settings; direct field evidence is rarer and typically less parameterized.
- **Limited longitudinal or persistence analysis:** Only a handful of studies examine the persistence or decay of efficiency effects after removing punishment or over very long games.
- **Payoff and welfare distribution:** Most studies report mean efficiency or group payoff; effects on inequality or on distribution by participant type (e.g., who bears punishment costs) are less commonly measured.

---

**In summary**, the literature supports robust, dimension-specific prediction of the effect of peer punishment on efficiency in standard PGG environments, but modelers should adjust for key design parameters, control efficiency, and contextual moderators. The prediction task is well-supported for canonical environments, but incomplete or ambiguous for exotic, highly parameterized, or strongly context-dependent settings.
