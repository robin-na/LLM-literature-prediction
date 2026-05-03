# 1) Evidence Base

This paper set is broad and comprises both empirical (experimental lab and field studies) and theoretical contributions, with a strong focus on public goods games (PGG), their close variants, and the effects of punishment/sanctions. Many papers report direct payoff-based outcomes (efficiency, group payoff), while others focus on contributions, cooperation rates, or norm compliance. The evidence base is rich in theory and simulation models, with a substantial but less voluminous set of empirical payoff results. Experimental designs are diverse, spanning standard linear PGGs, spatial and dynamic variants, and closely related social dilemmas.

The literature is strongest and most plentiful on canonical PGG setups and theoretical explorations of punishment. There are multiple high-quality lab experiments reporting efficiency effects, but theoretical works dominate when isolating nuanced game design moderators and mapping results across parameter sweeps.

# 2) Task Relevance

**pgg_or_variant:**  
- **Relevance:** exact/close
- The majority of the literature studies standard PGGs or direct variants (CPRs, N-person PDs, spatial PGGs). A smaller but significant portion of studies are only adjacent, focusing on two-player dilemmas, trust games, or other settings.

**punishment_or_sanctions:**  
- **Relevance:** exact/close
- A large subset of papers focus directly on punishment or sanctioning, with both peer and centralized forms. A further group discusses adjacent mechanisms like reputation, withholding, or expulsion.

**efficiency_or_related_payoff_outcome:**  
- **Relevance:** exact/close for a significant subset; many others are adjacent or report only behavioral outcomes
- Key outcomes of interest (efficiency, total/group payoff, welfare) are reported in a well-represented subset of both empirical and theoretical work. Other studies provide only behavioral or contribution-level outcomes but discuss implications for efficiency.

# 3) Outcomes Measured In The Literature

- **Payoff/Efficiency Outcomes:** Many reviewed papers (especially theoretical) report efficiency explicitly (i.e., group payoff as a fraction of the cooperative optimum). Some empirical studies directly report group earnings, welfare, or efficiency ratios in both control and punishment conditions. Several studies use successful public good provision (step function) or average earnings as a proxy for efficiency.
- **Non-Payoff Behavioral Outcomes:** A substantial fraction of studies focus on cooperation rates, contribution levels, frequency of punishment, norm compliance, and third-party punishment, but do not strictly report payoff or welfare.

**Explicit distinction**: Multiple papers note that increased cooperation/contribution does not always translate into increased efficiency—punishment costs may outweigh the surplus from higher cooperation (e.g., Shinada & Yamagishi, 2008; Fehl et al., 2012).

# 4) Main Findings Relevant To Prediction

## Empirical Findings
- **Punishment often increases contributions, but efficiency gains are conditional**: Enabling punishment reliably increases contribution rates but efficiency gains are not universal; they depend on the relative costs of punishment versus the cooperation it induces (Gürerk et al., 2009; Fehl et al., 2012; Shinada & Yamagishi, 2008).
- **Cost structure is critical**: Punishment is more likely to increase efficiency when the fine-to-fee ratio is high—i.e., punishment is impactful and/or cheap (Wang et al., 2010; Deng et al., 2012; Okada & Bingham, 2008).
- **Potential for efficiency loss**: Several studies show that the costs of punishment (and possible vendettas or anti-social punishment) can result in a net loss of efficiency, especially in larger groups, with high punishment costs, or in environments prone to retaliatory cycles (Fehl et al., 2012; Powers et al., 2012).
- **History and context moderate effects**: Path dependence, group composition (e.g., altruism, trust, cultural norms), and the specific incentive path (reward or punishment first) can strongly mediate long-term efficiency outcomes (Gürerk et al., 2009; Kocher et al., 2012).

## Theoretical Findings
- **Effect of punishment often positive but non-universal**: Theory frequently predicts punishment supports or increases efficiency relative to no-punishment baselines, provided costs aren't prohibitive and monitoring is sufficient (Eldakar et al., 2007; Bednar, 2006; Sigmund et al., 2011). Some models show that punishment without compensation for punishers, or in the presence of second-order free riders, may not enhance or may even decrease efficiency (Ye et al., 2011).
- **Moderator dimensions are key**: Effects depend on parameters such as group size (player_count), number of rounds (num_rounds), MPCR, punishment cost/technology, monitoring accuracy, and whether participation in the public good is voluntary (Sigmund et al., 2011; De Silva et al., 2010).
- **Compensation/reward can change dynamics**: Adding reward or metanorm incentives to support punishers can help punishment raise efficiency (Ye et al., 2011; Kendal et al., 2006).
- **High control efficiency constrains punishment's benefit**: Where baseline efficiency is already high (e.g., due to norms, communication, or framing), punishment often yields little or even negative marginal efficiency gains (van der Weele, 2012; Shinada & Yamagishi, 2008; Kocher et al., 2012).

# 5) Prediction Guidance

- **Punishment's marginal effect is conditional, not universal**: When predicting treatment efficiency (punishment enabled) from control efficiency and game design dimensions, do not assume a monotonic positive effect. Consider:
  - **Low control efficiency / High defection**: Punishment is more likely to yield substantial efficiency gains, provided punishment is not prohibitively costly and monitoring is effective (Sigmund et al., 2011; Wang et al., 2010; Bednar, 2006).
  - **High control efficiency / High baseline cooperation**: Little to no efficiency gain, and with high punishment costs or anti-social punishment, efficiency may decrease (Kocher et al., 2012; van der Weele, 2012).
  - **Game parameter dependency**: The magnitude and sign of punishment's effect depend on several moderators (see next section), and theory provides functional forms for some moderators (Eldakar et al., 2007; Hwang & Bowles, 2012).
- **Behavioral outcomes ≠ efficiency**: Increases in contributions/cooperation do not always translate to efficiency gains; the cost of punishment can negate the value of increased cooperation (Fehl et al., 2012; Shinada & Yamagishi, 2008).
- **Mapping to design dimensions**: Use available prior results to match on game design features—punishment cost/tech, MPCR, group size—to weight the likely effect of punishment on efficiency for a given prediction case. Extrapolation outside tested parameter regions or when design elements are missing is higher risk and should be flagged.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- **player_count:** Extensively analyzed as a moderator (Eldakar et al., 2007; Deng et al., 2012; Bednar, 2006; Kocher et al., 2012).
- **num_rounds:** Important for sustaining efficiency effects; longer games support behavioral adaptation (Eldakar et al., 2007; Bednar, 2006).
- **mpcr:** Frequently discussed; higher MPCR generally increases the efficiency gain achievable by punishment (Shinada & Yamagishi, 2008; Sigmund et al., 2011).
- **punishment_cost/punishment_tech:** Central in almost all relevant studies for calibrating punishment impact and net efficiency effect (Wang et al., 2010; Okada & Bingham, 2008).
- **reward_exists/reward_cost/reward_tech:** Addressed in fewer studies, but noted as critical moderators when present (Gürerk et al., 2009; Kendal et al., 2006).
- **all_or_nothing:** Covered, especially in studies using discrete or binary contribution models (Deng et al., 2012; Bednar, 2006).
- **show_n_rounds, show_other_summaries:** Sometimes present and acknowledged as part of monitoring/feedback design (Bednar, 2006; Kurokawa et al., 2010).
  
**Indirectly or Occasionally Discussed:**
- **chat:** Mentioned as a possible cooperation-boosting factor that may reduce or moderate the added value of punishment (Kocher et al., 2012; Gürerk et al., 2009).
- **default_contrib:** Experimental manipulation in some studies, but less directly linked to punishment effects (Messer & Zarghamee, 2007).
- **show_punishment_id:** Referenced as an information/identification variable in some adjacent studies, especially in anti-social punishment scenarios.
- **punishment_tech:** Varies in meaning, but often includes fine-to-fee ratio or presence of peer vs. centralized systems (Powers et al., 2012; Gürerk et al., 2009).

**Sparse or Effectively Missing:**
- **Reward stage dynamics, default_contrib, show_punishment_id, chat (beyond noting its presence), and nuanced framing effects** are less systematically analyzed relative to punishment and main structural game parameters.

# 7) Important Limitations

- **Gaps in empirical directness:** The abundance of theory papers means mechanistic conclusions are often robust, but precise empirical effect sizes for how punishment affects efficiency under given design dimensions are limited—especially for combinations of less common features (e.g., chat + punishment + default framing).
- **Transfer from behavioral to efficiency outcomes:** Many studies report behavioral improvements (contributions/cooperation), but not efficiency or group payoff, requiring caution in transferring conclusions.
- **Contextual/individual difference effects:** Social norms, trust, social background, and participant motivations (e.g., role of anger, altruism, or crowding out of intrinsic motivation) moderate punishment effectiveness but are often unobserved or not parameterized in model predictions.
- **Potential for negative or neutral effects:** The literature emphasizes that punishment can backfire—via excessive cost, vendettas, anti-social punishment, or disruption of intrinsic motivation—yet these pathologies are not always directly observable from design parameters alone.
- **Sparse coverage of some design features:** As noted, evidence is less systematic for how punishment interacts with dimensions like information feedback (show_punishment_id), non-linear payoff structures, or the presence of parallel reward mechanisms.
- **Most payoff-based evidence is for peer or symmetric punishment in standard linear PGGs:** Caution is advised in extrapolating to asymmetric, centralized, or more institutionally structured games.

---

**Summary:**  
This literature base robustly supports the claim that enabling punishment in PGG-like environments will often—but not always—increase efficiency relative to no-punishment controls, particularly when control efficiency is low and punishment is well-targeted, not too costly, and accompanied by effective monitoring. However, efficiency gains are contingent rather than universal, with strong dependence on game structural dimensions, context, and behavioral path-dependence. Prediction models should weight these moderators heavily and avoid assuming monotonic efficiency gains from enabling punishment without checking the fit to known evidence. Where key design dimensions are not informed, predictions should note uncertainty.
