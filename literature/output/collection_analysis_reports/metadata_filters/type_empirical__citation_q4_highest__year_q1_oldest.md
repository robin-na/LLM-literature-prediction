# 1) Evidence Base

This is a **large, high-quality, primarily experimental and empirical** literature base, focusing heavily on lab-based public goods games (PGG) and close variants. The core set is dominated by **experimental laboratory studies**, with some high-relevance field experiments and a smaller representation of observational or theoretical work. The coverage is **broad and deep** for classic PGGs with and without **peer punishment**, as well as for environments with close design analogues (e.g., CPR games, contest games, trust games with sanctions). There are numerous **direct efficiency-based outcome reports** as well as clear demarcation between studies that report only behavioral (e.g., contribution rate) or psychological outcomes.

The existing evidence includes **many variations in game design dimensions** (player count, number of rounds, MPCR, monitoring quality, punishment cost/impact, information structure, communication, endogenous institution choice, etc.), allowing for the assessment of a wide range of moderators. A substantial portion of papers also explicitly compare efficiency/payoff outcomes of the same game with and without punishment enabled, and provide **quantitative guidance** for prediction.

# 2) Task Relevance

**pgg_or_variant:**  
- **exact:** Most of the core studies are **exact**-fit public goods games matching the canonical lab PGG format (n=3-5, repeated rounds, VCM structure, with/without punishment).
- **close:** Several studies use close variants (e.g., CPR, ostracism-based or central/pooled punishment, trust games with sanctioning, endogenous group formation).
- **adjacent/weak:** A smaller subset represents adjacent games (dyadic PD, one-shot trust, communication/partner choice, contest games).

**punishment_or_sanctions:**  
- **exact:** Punishment is directly manipulated as a treatment variable in the bulk of studies (peer/monetary punishment, sometimes with reward).
- **close:** Several studies consider ostracism/exclusion or central punishment as close analogs.
- **adjacent:** Some studies focus on non-material or social punishment (shame, disapproval), or reputation systems in place of direct punishment.

**efficiency_or_related_payoff_outcome:**  
- **exact/close:** Many papers report efficiency (group payoff as % of optimum), group earnings, or surplus directly and compare control and punishment-enabled treatment outcomes.
- **adjacent/weak:** A significant minority only report behavioral outcomes (e.g., contribution/cooperation rates, punishment frequency), with explicit notes when these are not efficiency outcomes.
- **none:** A few studies focus solely on psychological or attitudinal variables and are excluded from efficiency-based inferences.

# 3) Outcomes Measured In The Literature

- **Payoff-related (efficiency, group earnings, welfare, surplus):** Directly measured and compared across control and punishment treatments in the majority of empirical PGG studies.
- **Behavioral (contribution rate, punishment rates, compliance, cooperation):** Widely reported, but not always accompanied by efficiency calculations. When only these are available, inferences about efficiency are qualified accordingly.
- **Psychological (trust, anger, norm endorsement, sanction motives):** Reported in some papers; not used to infer efficiency outcomes.

# 4) Main Findings Relevant To Prediction

## Direction and Typical Size of Punishment's Effect on Efficiency

- **Peer punishment in standard repeated PGGs** *typically increases group efficiency (payoff)* relative to the control, but:
    - The net gain is *often much smaller than the increase in contributions*, due to the direct costs of punishment (Fehr & Gächter, 2000; Sefton et al., 2007; Rand et al., 2009).
    - **Typical effect size**: Efficiency increases of 10–40% over control are often reported in canonical designs, particularly once the frequency of punishment declines over time as cooperation is stabilized (Fehr & Gächter, 2000; Fehr et al., 2002; Gintis et al., 2003).
    - In some environments, *punishment increases cooperation but leaves efficiency unchanged or even lowers it*, especially with frequent misapplied ('antisocial') punishment, high punishment cost, or in early rounds (Nikiforakis, 2008; Anderson & Putterman, 2006; Herrmann et al., 2008).
    - **Reward** and communication can, in some cases, match or outperform punishment for efficiency, often without the negative side effects (Rand et al., 2009; Bochet et al., 2006).
  
- **Critical moderators/conditionalities for efficiency gains:**
    - **Cost-effectiveness of punishment:** Low-cost, high-impact punishment produces the largest efficiency gains; expensive punishment can lower net payoffs (Egas & Riedl, 2008; Anderson & Putterman, 2006; Ambrus & Greiner, 2012).
    - **Targeting/anti-social punishment:** If punishment is misdirected, especially toward cooperators ('antisocial punishment'), efficiency gains vanish or reverse (Herrmann et al., 2008; Gächter & Herrmann, 2011).
    - **Monitoring quality:** Imperfect or noisy monitoring can cause punishment to reduce efficiency overall (Ambrus & Greiner, 2012; Grechenig et al., 2010).
    - **Retaliation/feuding:** If punishment is countered or repeated, costly cycles can erode efficiency (Nikiforakis, 2008; Denant-Boemont et al., 2007).
    - **Game horizon (one-shot vs. repeated):** Efficiency gains are much less likely in one-shot or short games, and more robust in longer/repeated environments.
    - **Cultural/social context:** The net efficiency effect is positive primarily in cultures or groups with low levels of antisocial punishment or spite; it can be negative where antisocial punishment is common (Herrmann et al., 2008; Gächter et al., 2010; Gächter & Herrmann, 2011).
    - **Communication/reputation:** These mechanisms can substitute for, or greatly enhance, the efficiency gains of punishment (Bochet et al., 2006; Rockenbach & Milinski, 2006; Ostrom, 2006).

- **Variants and institutional mechanisms:**
    - **Centralized/delegated punishment** and *ostracism/exclusion* can achieve higher efficiency at lower cost, especially when peer punishment is costly or misapplied (Andreoni & Gee, 2012; O'Gorman et al., 2009; Maier-Rigaud et al., 2010).
    - **Endogenous institution choice** (group voting for rules) tends to amplify efficiency, sometimes more than the imposition of punishment by fiat (Sutter et al., 2010; Tyran & Feld, 2006).
    - **Privilege/heterogeneity in group returns** weakens the efficiency benefit of punishment, increasing inequality and sometimes causing counterproductive targeting (Reuben & Riedl, 2009; Nikiforakis et al., 2012).

# 5) Prediction Guidance

The literature supports an overall model where the **efficiency of a PGG with peer punishment enabled** is typically **higher than the control game efficiency (without punishment)**, *holding design dimensions constant*, but with crucial caveats:

- **Magnitude and robustness**: The expected efficiency boost under "standard lab" conditions (small homogeneous groups, clear monitoring, partner or stranger matching, moderate punishment cost and effectiveness) ranges from ~10% up to 40% above control, *especially in later rounds* as punishment becomes rare and free riding is suppressed. In the very first rounds, punishment costs may initially outweigh efficiency gains; predictions should take round structure into consideration.

- **Key dimension-level moderators** (for which strong, direct evidence is available):
    - **Punishment cost and effectiveness (`punishment_cost`, `punishment_tech`)**: Net efficiency gains are maximized with low punishment cost and high impact per unit; cheap but misapplied punishment can destroy surplus (Anderson & Putterman, 2006; Egas & Riedl, 2008).
    - **Noise/imperfect monitoring**: Efficiency gains from punishment **vanish or reverse** with moderate/high noise (Ambrus & Greiner, 2012; Grechenig et al., 2010).
    - **Feedback/information (`show_other_summaries`)**: Feedback type (showing contributions vs. earnings) dramatically changes outcomes—contribution feedback supports higher efficiency, while earnings feedback can decrease efficiency (Nikiforakis, 2010).
    - **Anti-social/counter punishment (`show_punishment_id`, structure of institution)**: The opportunity for counter-punishment, or absence of anti-social punishment controls, strongly moderates efficiency effects (Nikiforakis, 2008; Denant-Boemont et al., 2007; Casari & Luini, 2009).
    - **Communication (`chat`)**, **reputation**: Presence yields marked efficiency improvements even relative to punishment alone (Bochet et al., 2006; Rockenbach & Milinski, 2006).

- **Indirect, contextual, or missing evidence**: Several design dimensions are mainly informed by adjacent or limited evidence. For these, inferences must be made with caution, especially when relying on non-efficiency outcomes.

- **Special cases—negative or null effects**:  
    - **High prevalence of antisocial or misdirected punishment**: Punishment can, and does, reduce efficiency compared to the control (Herrmann et al., 2008; Gächter & Herrmann, 2011; Nikiforakis, 2008; Egas & Riedl, 2008).
    - **Noisy monitoring, high likelihood of error/counter-punishment**: Efficiency losses can be severe (Ambrus & Greiner, 2012; Denant-Boemont et al., 2007).
    - **Adjacency to PGGs**: In some adjacent games (Lab PD, contest games), punishment raises contributions but *may not* increase or may decrease efficiency (Wu et al., 2009; Dreber et al., 2008; Abbink et al., 2010).

- **Use of prior efficiency (control game) for prediction**: The *efficiency improvement resulting from enabling punishment* is **not a fixed function of control-game efficiency**; the moderator dimensions listed above often *change the slope and even the sign* of the treatment effect.

- **Game design interactions:** Combinations, such as punishment + communication or punishment + reputation, are **superadditive** in producing high and stable efficiency (Ostrom, 2006; Rockenbach & Milinski, 2006).

# 6) Design Dimensions Highlighted Across Papers

**Directly informed (strong, explicit evidence supporting predictions as a function of the dimension):**
- `player_count`
- `num_rounds`
- `mpcr`
- `punishment_cost` and `punishment_tech`
- `chat` (communication)
- `all_or_nothing` (binary vs. continuous contribution)
- `reward_exists`
- `show_other_summaries` (feedback format)
- `show_punishment_id` (blame/identifiability for punishment/anti-social punishment)
- `punishment_tech` (who can punish, consensus requirements, institution structure)
- `reward_cost`, `reward_tech` (less common, but included in direct comparisons)

**Indirectly informed or strongly context-dependent:**
- `default_contrib` (framing, opt-in vs. opt-out): Not much experimental variation in the core papers; mainly background or not systematically tested.
- `show_n_rounds`: Some indirect evidence relates to known vs. unknown horizon effects, but not unambiguously as a strong moderator separate from other design factors.

**Contextually mentioned or sparsely informed:**
- `show_other_summaries`: Beyond feedback specifics, general summary of others' outcomes is often standard but not always varied as a treatment. Nikiforakis (2010) is a key study for this dimension.
- Group heterogeneity (privilege, MPCR asymmetry): Well covered only in select studies (Reuben & Riedl, 2009; Nikiforakis et al., 2012).
- Effects of chat and communication are robustly documented for classic, open-ended channels, but less so for minimal/non-verbal or structured chat.
- Some dimensions (e.g., opt-in vs. opt-out framing, round number display) are underexplored as moderators for efficiency effects.

# 7) Important Limitations

- **Generalizability to Field/Real-World Settings:** Nearly all high-relevance payoff-based evidence comes from highly controlled laboratory environments with cash incentives, clear monitoring, and simple group structures. Real-world inefficiencies and institutional constraints may not be reflected (Lopez et al., 2012; Vollan, 2008).
- **Cultural and Social Context:** There are significant, **documented cultural and social group differences** in the effect of punishment on efficiency (Herrmann et al., 2008; Gächter et al., 2010). Predictions based on lab results from one culture may not transfer to others.
- **Measurement Timing:** Some studies report that efficiency is only higher after the initial rounds, with early punishment costs dominating at first (Sefton et al., 2007; Fehr & Gächter, 2000). Prediction must consider average vs. round-by-round efficiency.
- **Nonlinear effects and threshold behaviors:** Efficiency responses to small changes in punishment parameters can be nonlinear and threshold-dependent (Ambrus & Greiner, 2012).
- **Missing interactions:** Not all possible interactions among game design dimensions are experimentally mapped; some extrapolation may be needed.
- **Sparse evidence for some dimensions:** Clearly, not all 14 prediction dimensions have robust, direct, systematic variation in the current literature, especially for framing, explicit defaults, and some information structures.
- **Payoff-Behavior Disconnect:** Elevated contribution rates can mask unchanged or worsened efficiency due to high punishment costs (Egas & Riedl, 2008; Nikiforakis, 2008).

---

**In sum:** The literature provides **robust, directly relevant, empirical evidence** for predicting how enabling peer punishment will change efficiency in PGG-like environments, *conditional* on careful matching of game design dimensions and context. The effect is **positive in standard lab PGGs** but is **highly moderated** by punishment institution details, monitoring quality, group heterogeneity, cultural context, and feedback structures. *Direct estimation of treatment efficiency from control efficiency is best done with explicit modeling of these moderators,* using the detailed parameterizations and findings from the cited studies.
