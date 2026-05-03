# Evidence Base

The paper set comprises **74 papers** with a mix of empirical (laboratory experiments and observational studies) and theoretical (evolutionary game theory, agent-based models, mechanism design) contributions. The **majority are theoretical or simulation-based analyses** focused on social dilemma games, variants of public goods games (PGGs), or closely related contexts (e.g., repeated Prisoner's Dilemma, trust games, resource dilemmas). There is a solid contingent of **lab experiments on PGGs or close variants**, but also many papers that explore adjacent domains (e.g., helping games, market settings, group selection models). The breadth covers a wide diversity of game forms, punishment (and occasionally reward) mechanisms, and institutional or psychological moderators. However, **papers providing direct experimental data on average efficiency effects of punishment in standard PGGs are a minority**. Most theory and simulation papers consider efficiency and group payoff, while a notable fraction reports only on cooperation rates or other behavioral outcomes.

# Task Relevance

### 1. **PGG or Variant**  
- **Exact:** About a third of the papers use standard PGGs or clear structural variants (e.g., Wu et al., 2014; Kroupa, 2014; Zhosan & Gardner, 2013; Hugh-Jones & Perroni, 2017; Otto & Bolle, 2016; Asgharpourmasouleh et al., 2017).
- **Close/Adjacent:** Many other studies use repeated social dilemmas structurally similar to PGGs—resource dilemmas, repeated help/trust/exclusion games—or spatial/biological implementations of PGG-like incentives.
- **Weak/None:** A substantial number of papers focus on pairwise games, market interactions, or coordination games not directly mappable to PGGs.

### 2. **Punishment or Sanctions**  
- **Exact:** Clear treatments involving explicit costly peer punishment or institutional punishment (Wu et al., 2014; Kroupa, 2014; Hugh-Jones & Perroni, 2017).
- **Close:** Many others discuss punishment in the form of audits, exclusion, voting penalties, psychological/social pressure, or related mechanisms (e.g., endogenous audits, status-based punishment, social pressure).
- **Adjacent/Weak:** Some focus on reward, monitoring, reputation, or non-punishment-based enforcement.

### 3. **Efficiency or Related Payoff Outcome**  
- **Exact:** Several papers explicitly measure and compare efficiency or average group payoff (Wu et al., 2014; Otto & Bolle, 2016; Zhosan & Gardner, 2013; Asgharpourmasouleh et al., 2017; Ezeigbo, 2017).
- **Close:** Others report total earnings, welfare, or surplus, or are theoretical works focusing directly on payoff distributions (Laclau & Tomala, 2017; Olcina & Calabuig, 2015).
- **Adjacent/Weak:** Many papers focus on cooperation rate, punishment frequency, or norm compliance only, which are not equivalent to efficiency.

**In sum**, the literature is **broad on punishment mechanisms and social dilemmas**, moderately broad on PGGs or close variants, and **less comprehensive on direct, experimental efficiency outcomes for peer punishment in PGGs**.

# Outcomes Measured In The Literature

- **Payoff-related Outcomes (efficiency, group payoff, surplus, total earnings):**
  - A clear subset directly measures group efficiency or total payoff (Wu et al., 2014; Otto & Bolle, 2016; Zhosan & Gardner, 2013; Ezeigbo, 2017; Asgharpourmasouleh et al., 2017; Antoci & Zarri, 2015; Olcina & Calabuig, 2015; Camera & Gioffré, 2017).
  - Several theory/simulation studies focus primarily on average payoff as a function of punishment and design parameters.
- **Non-payoff Behavioral Outcomes:**
  - Many papers report only on **contribution rates, cooperation rates, norm compliance, or punishment activity** (Ogaki & Tanaka, 2017; Vincent, 2017; Tang & Ye, 2016; Qu et al., 2016).
  - These are used as **indirect proxies** for efficiency, but their predictive validity for group payoff is often discussed as ambiguous or conditional.

# Main Findings Relevant To Prediction

### 1. **Punishment Increases Efficiency—Conditionally**
- **Empirical and theoretical analyses consistently find that** enabling costly punishment in (spatial or voluntary) PGGs or close variants can increase average group efficiency relative to control, **especially when baseline (control) efficiency is low** (Wu et al., 2014; Zhosan & Gardner, 2013; Asgharpourmasouleh et al., 2017; Olcina & Calabuig, 2015; Vanderschraaf, 2016).
- **However, this positive effect depends strongly** on punishment **being well-targeted, not too costly, and not misapplied** (e.g., antisocial punishment, poor targeting, or low coordination can reduce or reverse efficiency gains) (Kroupa, 2014; Hugh-Jones & Perroni, 2017; Antoci & Zarri, 2015; Ezeigbo, 2017).

### 2. **Design Moderators Are Crucial**
- **Punishment Cost:** Lower cost of punishment increases size and scope of high-efficiency regions (Wu et al., 2014; Olcina & Calabuig, 2015); high-cost punishment can make overall payoffs decrease even as free-riding is reduced (Kroupa, 2014; Ezeigbo, 2017).
- **MPCR (marginal per-capita return):** Punishment is **most beneficial in low-MPCR settings** where baseline efficiency is low (Wu et al., 2014); as MPCR increases, cooperation can sometimes be sustained without punishment.
- **Punishment Technology (“punishment_tech”):** Designs requiring coordinated action for effective punishment (e.g., M>1 for expropriation) are more likely to produce efficiency gains, as punishment becomes credible and less arbitrary (Hugh-Jones & Perroni, 2017; Olcina & Calabuig, 2015).
- **Communication, Reputation, Transparency:** Presence of communication, reputation systems, or some transparency **amplifies the efficiency gains from punishment** or can substitute for some punishment needs (Kroupa, 2014; Zhosan & Gardner, 2013).
- **Information Structure:** Accurate, public information about others’ behaviors facilitates targeted, proportional punishment and higher efficiency (Laclau & Tomala, 2017).
- **Group Size:** Small groups are more likely to realize efficiency improvements via punishment; larger or more anonymous groups diminish the effect (Patrzyk & Takác, 2017; Kroupa, 2014).

### 3. **Punishment Does Not Always Increase Efficiency**
- **Punishment can reduce efficiency when:** 
  - It is expensive,
  - Applied indiscriminately or antisocially (Kroupa, 2014; Ezeigbo, 2017; dos Santos et al., 2014),
  - There is high second-order free riding (Antoci & Zarri, 2015).
- There are notable studies where **contribution rates increase but group payoff does not** (Ogaki & Tanaka, 2017; Hsu, 2013), or where punishment increases costly participation without increasing welfare (Myers, 2016).

### 4. **Complementary or Alternative Mechanisms**
- **Hierarchy and Selection:** Central authority or principal-allocator structures can substitute for punishment and yield even higher efficiency (Otto & Bolle, 2016).
- **Rewards:** Reward mechanisms can either supplement or undermine punishment-based cooperation, depending on structure (Antoci & Zarri, 2015).
- **Reputation and Exclusion:** Reputation-based reward, exclusion, or linkage strategies can achieve high efficiency, especially when punishment is otherwise ineffective or too costly (Camera & Gioffré, 2017; Inaba et al., 2016).

### 5. **Mechanism, Context, and Behavioral Outcomes**
- There is strong **theoretical and indirect evidence that punishment increases cooperation rates, deters free-riding, and can stabilize efficient equilibria**, but these do **not automatically translate to actual increased efficiency unless punishment costs are low and application is targeted**.

# Prediction Guidance

- **Which design dimensions are most informative for efficiency predictions?**
  - **Directly Informed:** `player_count`, `num_rounds`, `mpcr`, `punishment_cost`, `punishment_tech`, `chat` (presence of communication), and to a somewhat lesser extent `show_other_summaries` and aspects of transparency. These are explicitly manipulated in multiple empirical and theory studies with efficiency as an outcome (Wu et al., 2014; Hugh-Jones & Perroni, 2017; Kroupa, 2014; Zhosan & Gardner, 2013; Olcina & Calabuig, 2015).
  - **Indirectly Informed/Contextual:** `all_or_nothing`, `default_contrib`, `show_n_rounds`, `show_punishment_id`, `reward_exists`, `reward_cost`, `reward_tech` are discussed in adjacent or simulation/theory work, but not consistently mapped to empirical efficiency outcomes.
  - **Missing/Sparse:** The literature provides **little direct evidence on the impact of `reward` parameters (when separate from punishment) on efficiency in conjunction with punishment** and on the effect of experimental features like `show_n_rounds` or `show_punishment_id` except as moderators in theory models.

- **How should this literature guide prediction of treatment efficiency from design dimensions and control efficiency?**
  - **If the control (no punishment) game is low-efficiency,** enabling well-targeted, not overly costly punishment (especially in small groups, low MPCR, or with communication) should increase efficiency, potentially substantially (Wu et al., 2014; Asgharpourmasouleh et al., 2017).
  - **In designs with high punishment cost, poor targeting (easy, solo punishment), social anonymity, or large group size,** efficiency gains are lower, can be null, or can even become negative (Kroupa, 2014; Hugh-Jones & Perroni, 2017; Ezeigbo, 2017; Antoci & Zarri, 2015).
  - **Presence of communication, transparency, or reputation mechanisms** can either potentiate or substitute for (and sometimes reduce the need for) punishment, but when paired with punishment, can lead to highest efficiency (Kroupa, 2014; Zhosan & Gardner, 2013).
  - **Antisocial punishment, high levels of second-order free-riding, or unbalanced population structures** can lead to breakdown in efficiency or null/negative effects of punishment interventions (Kroupa, 2014; Antoci & Zarri, 2015; dos Santos et al., 2014). Control efficiency becomes less predictive in these cases.
  - **Control efficiency is a good starting point for prediction,** but the above dimension-level interactions can make the magnitude and even the sign of punishment effects on efficiency contextually dependent.

# Design Dimensions Highlighted Across Papers

- **Directly Informed:** `player_count`, `num_rounds`, `mpcr`, `punishment_cost`, `punishment_tech`, and `chat` are robustly addressed with both empirical and theoretical support and have clear, interpretable effects on efficiency.
- **Indirectly/Non-uniquely Informed:** Design details such as `all_or_nothing`, `default_contrib`, `show_other_summaries`, and `show_n_rounds` are variably present and often only contextually or theoretically discussed.
- **Sparse/Missing:** `reward_exists`, `reward_cost`, `reward_tech`, and aspects like `show_punishment_id` have patchy evidence, mostly in theoretical models or non-PGG games, and their main effects on efficiency in conjunction with punishment are underspecified in empirical papers.

# Important Limitations

- **Payoff vs. Behavioral Outcomes:** **Many studies use cooperation/contribution rate increases as a surrogate for efficiency,** but this relationship is not always reliable; punishment can increase cooperation while reducing total payoff if punishment is costly or misapplied.
- **Heterogeneity of Designs and Metrics:** **Substantial diversity in experimental and model design** (e.g., spatial games, trust games, binary vs. continuous contributions) means that generalizations to all 14 prediction dimensions are limited, and not all findings are equally transferrable to classic PGG structures.
- **Sparse Direct Evidence for Some Dimensions:** Design features such as **reward mechanisms, transparency of punishment, or institutionally-imposed vs. spontaneous peer punishment** are underrepresented in empirical data on efficiency outcomes.
- **Ambiguity in Some Contexts:** Some studies show **mixed or negative effects of punishment on efficiency** (Kroupa, 2014; Ezeigbo, 2017; Antoci & Zarri, 2015), especially under high costs, antisocial punishment, or unclear targeting.
- **Experimental vs. Field/Simulation Contexts:** Most support comes from **simulation or evolutionary models; direct lab evidence for peer punishment effects on payoff-based efficiency, especially for large, diverse groups or field contexts, is less common**.
- **Conditional and Mechanism-dependence:** **Effects of punishment are highly contingent on punishment structure, application, and supplementary mechanisms** such as hierarchy, exclusion, or reward options.

---

### In summary, the literature provides **good coverage and convergent theoretical support for a positive effect of well-targeted, not excessively costly punishment on efficiency in public-goods-game-like environments, especially under low baseline efficiency conditions**. However, the **effect is conditional on multiple game design dimensions, with clear evidence of situations where punishment can fail to increase, or even reduce, efficiency**. Predictive models should, therefore, **incorporate main game design dimensions, especially punishment cost, targeting/technology, and MPCR, and treat behavioral-outcome-only evidence with caution when extrapolating to efficiency**.
