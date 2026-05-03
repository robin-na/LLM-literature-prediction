# 1) Evidence Base

This paper set includes 10 papers encompassing both empirical (mainly laboratory experiments) and theoretical studies. The majority of empirical papers employ laboratory experiments, but several theory papers address model-based or game-theoretical frameworks. Coverage is narrow to moderate for the downstream prediction task—only several papers use classic public goods games (PGG) with efficiency or related payoff as a primary outcome in the context of peer punishment. Others use adjacent game types (e.g., dictator or ultimatum games) or focus on non-payoff behavioral outcomes, not group efficiency, or omit punishment entirely. Overall, only a subset of this literature directly informs the prediction of efficiency changes resulting from enabling punishment in PGG-like environments.

# 2) Task Relevance

**pgg_or_variant:**  
- **exact:** Multiple papers use classic PGGs or explicit variants (García & Traulsen, 2012; Fehl et al., 2012; Pan & Houser, 2011; Smaldino & Lubell, 2011).
- **close or adjacent:** Several papers use adjacent social dilemma games (Helbing & Johansson, 2010; Seip et al., 2009; Brüne et al., 2012; Mancini et al., 2011), or non-PGG structures (Panasiti et al., 2011).

**punishment_or_sanctions:**  
- **exact:** Some papers explicitly manipulate or analyze peer punishment in PGGs or analogous setups (García & Traulsen, 2012; Fehl et al., 2012; Seip et al., 2009; Brüne et al., 2012).
- **close/adjacent:** A few examine punishment in non-PGG games or discuss sanctioning as a theoretical mechanism (Helbing & Johansson, 2010; Mancini et al., 2011); others have no punishment element.

**efficiency_or_related_payoff_outcome:**  
- **exact/close:** Direct measurement or modeling of group efficiency or payoff included in García & Traulsen (2012), Fehl et al. (2012), and Brown & Taddei (2007).
- **adjacent/weak:** Most other empirical studies report primarily behavioral (non-payoff) outcomes or use unrelated games.

Thus, direct, strong relevance to all three target dimensions is found in only a subset (principally: García & Traulsen, 2012; Fehl et al., 2012).

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:**  
  - **Efficiency (group payoff relative to fully cooperative baseline):** García & Traulsen (2012; theory), Fehl et al. (2012; experimental but only "close" due to vendetta effects), Brown & Taddei (2007; theory, no punishment).
  - **Total earnings/group payoff/welfare:** Sometimes referenced but often secondary or indirectly measured.

- **Non-payoff behavioral outcomes:**  
  - **Contribution or cooperation rate:** Frequently reported (Fehl et al., 2012; Pan & Houser, 2011).
  - **Punishment frequency and magnitude, norm compliance, emotional drivers (anger, empathy):** Predominant focus in Seip et al. (2009), Brüne et al. (2012), and most adjacent game studies.

Most studies measure behavioral tendencies rather than actual realized group efficiency/payoff, blurring the connection to the prediction target.

# 4) Main Findings Relevant To Prediction

**Empirical findings:**  
- **Punishment can increase cooperation but not necessarily efficiency:**  
  Experimental evidence shows that enabling peer punishment in PGGs often raises cooperation rates, but this can come with costly retaliation cycles (vendettas), eroding or even reducing group efficiency: "the costs of punishment and counter-punishment reduce overall earnings, especially for those involved in vendettas" (Fehl et al., 2012). Dyadic games show fewer vendettas and smaller efficiency losses, indicating the importance of group structure and punishment visibility.

**Theoretical arguments:**  
- **Fragile efficiency gains depend on population dynamics:**  
  Evolutionary models predict that the effect of punishment on efficiency is highly sensitive to the structure of mutations—if players can easily shift strategies, punishment sustains high efficiency; if not, efficiency can collapse (García & Traulsen, 2012).

**Non-payoff findings:**  
- **Emotional and cognitive drivers of punishment:**  
  Anger, not necessarily unfairness perception, is the primary trigger for costly punishment (Seip et al., 2009); cognitive inhibition or low empathy can increase punishment tendency (Brüne et al., 2012).  
  These mechanisms suggest that even if punishment is available, its usage and thus its payoff consequences depend on psychological states.

**Effects of group structure and dimensions:**  
- **Capacity/group size constraints can boost cooperator payoffs without punishment:** (Smaldino & Lubell, 2011)
- **Game design (e.g., dyadic vs. n>2; round structure) modulates retaliation, with dyads less prone to destructive vendettas:** (Fehl et al., 2012)

# 5) Prediction Guidance

**When using this literature to predict the effect of enabling peer punishment on treatment efficiency in PGG-like games:**  
- **Do not assume that punishment will increase efficiency** simply because cooperation rises—costs from vendettas and mutual punishment can more than offset gains (Fehl et al., 2012).
- **Model and context details (e.g., group size, mutation dynamics, opportunity for retaliation)** critically determine whether punishment is welfare-improving (García & Traulsen, 2012). Theoretical work suggests that small changes in assumptions (like mutation kernel or group size) can flip the net effect of punishment.
- **If control efficiency is already high, enabling costly punishment may introduce destructive cycles that decrease efficiency.**
- **Behavioral findings indicate punishment will be more prevalent when defection evokes anger or when cognitive inhibition is reduced,** but these do not map cleanly to efficiency.
- **Dimension mapping:** The best-informed dimensions are group size (`player_count`), number of rounds (`num_rounds`), marginal per capita return (`mpcr`), opportunity and cost of punishment (`punishment_cost`), and structural features like `all_or_nothing` and punishment technology.  
- **Absent or weakly informed dimensions include chat, default contribution framing, reward existence, summary visibilities, and most information interventions.**

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**  
- `player_count`, `num_rounds`, `all_or_nothing`, `mpcr`, `punishment_cost`, `punishment_tech`
  - Empirical and theoretical papers often discuss these, linking them to efficiency or retaliation dynamics and mutation-structured cooperation (García & Traulsen, 2012; Fehl et al., 2012).
- **Indirectly Informed:**  
  - `chat` (as social context; Pan & Houser, 2011; Brüne et al., 2012) — but impact on efficiency is speculative.
  - `reward_exists` (Pan & Houser, 2011; only non-punishment rewards studied).
- **Contextually Discussed or Sparse:**  
  - `default_contrib`, `show_n_rounds`, `show_other_summaries`, `show_punishment_id` (sometimes reported in experimental setup, but little analytical leverage).
- **Effectively Missing:**  
  - `reward_cost`, `reward_tech`, and interaction terms involving reward/punishment information or identity visibility are not substantively analyzed vis-a-vis payoff/efficiency.

# 7) Important Limitations

- **Limited direct evidence:** Very few studies actually combine PGG structure, explicit punishment manipulations, and measurement or modeling of efficiency or group payoff. Most studies measuring behavioral or emotional outcomes do not report actual group efficiency, making inferences tenuous for the prediction task.
- **Retaliation and vendetta dynamics may depend strongly on specific game features not varied systematically in this literature:** e.g., whether punishment is anonymous, the number of punishment opportunities per round, or constraints on who can punish.
- **Lack of parameter diversity:** Most studies focus on standard lab PGGs with limited exploration of the full range of the 14 prediction dimensions, especially social information displays, default settings, or reward–punishment interactions.
- **Theoretical ambiguity:** Theory papers reveal that even small modeling changes (mutation kernels, group size) can dramatically alter whether punishment raises or lowers efficiency (García & Traulsen, 2012), indicating a lack of robust, generalizable prediction rules.
- **Behavioral mechanisms do not map directly to payoffs:** The prevalence and psychology of punishment (anger, empathy, cognitive inhibition) are discussed, but without showing how they translate into aggregate efficiency effects.
- **Adjacent and irrelevant studies:** Several papers focus on adjacent games (ultimatum, dictator, deception), absence of punishment, or reward mechanisms only.

**Conclusion:**
This literature set provides some useful evidence—especially regarding the conditions under which punishment can harm or fail to improve efficiency due to retaliation—but overall, its direct utility for reliably predicting treatment efficiency as a function of design dimensions and control efficiency across new PGG designs is limited by the scarcity of studies measuring all relevant outcomes and dimensions in tandem. Careful, context-sensitive interpretation is necessary, and predictions should emphasize uncertainty where generalizability is questionable.
