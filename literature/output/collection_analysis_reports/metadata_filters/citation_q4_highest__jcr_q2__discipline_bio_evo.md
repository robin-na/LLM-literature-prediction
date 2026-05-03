# 1) Evidence Base

The paper set includes 18 sources with a blend of theoretical and empirical work. The majority are theoretical or review papers focused on the evolution and mechanism of cooperation and punishment in public-goods-like environments (e.g., Gardner & West, 2004; Henrich & Henrich, 2006), with a smaller subset providing laboratory or field experimental data (e.g., Gelcich et al., 2013; dos Santos et al., 2013). Empirical studies directly measuring payoff-based or efficiency outcomes in public goods or closely related games are limited. The literature set is broad in terms of addressing cooperation, social dilemmas, and punishment mechanisms, but relatively narrow with respect to direct, quantitative evidence on the impact of enabling peer punishment on efficiency—especially as formalized in average group payoff ratios in canonical PGGs.

# 2) Task Relevance

**pgg_or_variant**:
- *exact*: A minority of papers use or closely match canonical PGGs (e.g., Archetti & Scheuring, 2011; Gelcich et al., 2013).
- *close*: Several others use threshold/two-action PGG variants, common-pool resource (CPR) games, or repeated helping games (e.g., dos Santos et al., 2013; Sasaki & Uchida, 2014).
- *adjacent/weak*: Others are further removed, involving dyadic mutualism (Bshary & Grutter, 2005), general reciprocity, or theoretical frameworks with only conceptual links to PGG (Taylor & Nowak, 2007; Boehm, 1997).

**punishment_or_sanctions**:
- *exact/close*: Papers explicitly analyze punishment as a treatment or mechanism (Gardner & West, 2004; dos Santos et al., 2013; Gelcich et al., 2013), including visibility/reputation effects.
- *adjacent/weak*: Some discuss punishment conceptually (Fletcher & Zwick, 2006) or as one among several partner control mechanisms (Bshary & Grutter, 2005).
- *none*: Several papers focus only on cooperation or rewards and do not include punishment (Archetti & Scheuring, 2011; Sasaki & Uchida, 2014).

**efficiency_or_related_payoff_outcome**:
- *exact*: Rare; direct measures of efficiency (group payoff in ratio form) are reported in only a few papers (Archetti & Scheuring, 2011; Gelcich et al., 2013).
- *close*: Some papers report related outcomes (total group earnings, average payoffs; dos Santos et al., 2013).
- *adjacent/weak*: Many report only behavioral or reputational outcomes (contribution rates, helping/punishing actions, reputation earned).

**Summary**: The literature primarily provides exact or close relevance for the *punishment* and *mechanism* aspects, but only a minority give *exact* outcome relevance (measured efficiency in PGGs with and without punishment). This limits the paper set’s coverage for the specific prediction task.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes**:  
  - Direct group efficiency or normalized total payoff: Rarely reported (Archetti & Scheuring, 2011; Gelcich et al., 2013).
  - Group earnings or welfare (sometimes as absolute or average payoff): Occasionally reported, but often not normalized to cooperation optimum (dos Santos et al., 2013).
  - Some theoretical work models equilibrium group payoff or fitness (Gardner & West, 2004; Sasaki & Uchida, 2014).
- **Non-Payoff Behavioral Outcomes**:
  - Contribution rate, helping behavior, cooperation frequency, norm compliance: Very commonly measured or modeled (Declerck et al., 2013; Raihani & McAuliffe, 2012).
  - Frequency or pattern of assigned punishment or reward.
  - Reputational effects, bystander judgments.
- Most empirical and theoretical discussions of punishment focus on its *effect on cooperation/contribution rates*, with fewer works extending this to explicit group efficiency or surplus quantification.

# 4) Main Findings Relevant To Prediction

- **Punishment Increases Efficiency where Baseline is Low**
  - Experimental CPR/PGG-like settings (Gelcich et al., 2013) show that even weak, probabilistic punishment increases group efficiency—especially in groups with moderate baseline cooperation, strong norms, or social capital.
- **Punishment Reputation Enhances Effect**
  - Where punishment and/or the reputation of punishers are visible, both cooperation rates and group payoffs increase; the effect is robust unless either punishment or its visibility is removed (dos Santos et al., 2013).
- **Moderator Effects**
  - Theoretical work identifies key moderators: group size (smaller groups favor punishment sustaining efficiency), punishment effectiveness (penalty to punished > cost of cooperation), and cost to punisher (Gardner & West, 2004; Henrich & Henrich, 2006).
  - Pre-existing group norms or social capital amplify punishment’s efficiency benefits (Gelcich et al., 2013).
- **Caveats from Theory**
  - Punishment only increases efficiency if it leads to more cooperation robustly and if its cost does not offset group surplus (Gardner & West, 2004). Theory papers disagree on how often this precondition is met in the absence of special structure (Lehmann et al., 2007).
  - If punishment is too costly, or is not reliably linked to increased cooperation, it can fail to increase efficiency—or even reduce it.
- **Rewards as an Alternative**
  - In threshold public goods settings, introducing reward may be a more effective or feasible route to high efficiency than punishment, but direct comparisons are limited (Sasaki & Uchida, 2014).

# 5) Prediction Guidance

The literature (weighted toward theory and a handful of experiments) supports a qualitative expectation that enabling peer punishment will increase group efficiency compared to control (punishment disabled) in typical public-goods-game-like environments:
  - The effect is **strongest when baseline efficiency is low to moderate**, group norms favor cooperation, and punishment is both visible and effective (penalizes defectors more than the costs it imposes on the punisher).
  - **Design features** that increase the effectiveness of punishment (higher punishment magnitude relative to cost, visibility, and links to reputation) are important moderators, but only a couple of papers directly test these.
  - **Quantitative extrapolation** is hampered by a lack of multiple-arm PGG experiments reporting both control and punishment-enabled efficiency on a comparable scale.
  - When using game design variables and control-game efficiency to predict treatment efficiency, the best supported dimensions are player count, number of rounds, mpcr, punishment cost, and punishment reputation/visibility. Even so, the uncertainty is substantial due to the limited number of directly comparable empirical studies.
  - For **outlier cases** (e.g., already-high efficiency, very high punishment costs, anonymous or one-shot games), the effect of enabling punishment may be attenuated or ambiguous.
  - There is some evidence (though mostly theoretical) that in the absence of supporting social structure/visibility, or with poor punishment incentives, enabling punishment may not increase, or could even reduce, efficiency.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed**:
- `player_count`, `num_rounds`, `mpcr`: Consistently modeled or measured (Archetti & Scheuring, 2011; Gelcich et al., 2013; Gardner & West, 2004; dos Santos et al., 2013).
- `punishment_cost`, `punishment_tech` (method, effectiveness): Discussed in theory and some experiments (Gardner & West, 2004; Gelcich et al., 2013; dos Santos et al., 2013).
- `show_punishment_id`/visibility: Reputation and visibility shown to strongly moderate effects in a few studies (dos Santos et al., 2013); otherwise more often theorized.
- `reward_exists`, `reward_cost`: Explored theoretically relative to punishment in some work (Sasaki & Uchida, 2014).

**Indirectly or Contextually Informed**:
- `all_or_nothing`, `default_contrib`: Commonly specified but not used as predictors of efficiency change (Archetti & Scheuring, 2011; Gelcich et al., 2013).
- `chat`: Sometimes included, with indirect links to norms or enforcement potential (Gelcich et al., 2013; Declerck et al., 2013).
- `show_n_rounds`, `show_other_summaries`: Occasionally specified but rarely analyzed as moderators of the punishment effect.

**Effectively Missing/Sparse**:
- Detailed parametric mapping for `punishment_magnitude`, `reward_magnitude`: Not systematically reported.
- Comparative manipulation of `reward_exists` versus `punishment_exists` in fully controlled settings.
- Few papers systematically explore or manipulate design variables in tandem; most focus on one or two dimensions at a time.

# 7) Important Limitations

- **Scarcity of Direct Experimental Evidence**: Only a handful of empirical studies explicitly report efficiency or normalized group payoff in both punishment-disabled and punishment-enabled treatments.
- **Dominance of Theory**: The majority of findings are theoretical or mechanistic, providing qualitative direction and identifying moderators, but not empirically parameterized predictive models.
- **Non-payoff Outcomes Predominate**: Many works measure behavioral change (cooperation rate, punishing activity) rather than efficiency, making it hazardous to impute efficiency impacts from behavioral proxies.
- **Variation in Game Structure**: Many included studies use variants that differ from standard PGGs in key ways (e.g., helping games, CPR scenarios, reputation-based games), complicating direct transfer of findings.
- **Contextual Moderators Under-Explored**: Important boundary conditions (e.g., social capital, preexisting norms, reputation mechanisms) are identified but not systematically tested across the range of design parameters.
- **Design Variable Coverage is Patchy**: No single source or set of syntheses systematically varies all key game parameters, limiting the predictive specificity for arbitrary design settings.
- **Ambiguity and Contradiction**: Some theory papers (e.g., Lehmann et al., 2007) note that without special structure or direct benefits, costly punishment may not increase efficiency, highlighting that the beneficial effect of punishment is not universal.

**Summary**:  
The literature base provides strong qualitative reason to expect that enabling peer punishment can increase efficiency under common PGG-like conditions, especially if baseline efficiency is not already high, punishment is visible and effective, and supportive norms exist. However, for quantitative prediction as a function of design variables and control efficiency, empirical evidence is thin and focused on a limited space of parameter settings. Uncertainty and the risk of overgeneralizing from non-payoff measures are both substantial. This literature is best used to set priors about the positive direction of the effect and to alert forecasters to key moderators, not for precise efficiency prediction.
