# 1) Evidence Base

The paper set comprises a large, methodologically diverse collection of primarily empirical, experimental studies, overwhelmingly focused on laboratory environments (lab-experiments and some field/lab-in-the-field settings). Theory papers and pure mechanism arguments are rare, with empirical tests of practical interventions dominating. This is a broad and deep evidence base for public goods games (PGGs) and variants, with rich direct experimental evidence on the central prediction problem: the impact of enabling peer (and other forms of) punishment on group efficiency (i.e., total/average group payoff as a share of the cooperative maximum), given detailed game design.

Most studies use canonical linear PGGs but also cover variants: step-level/threshold games, resource dilemmas/CPRs, coordination games, group formation games, and others. There is strong coverage for peer punishment, centralized punishment, exclusion/ostracism, reputation, and institution choice. Many papers report direct efficiency/payoff outcomes in the standard sense (total earnings or normalized surplus). Some emphasize nuanced features such as democratic selection, cultural/group composition, leader/follower dynamics, and information/feedback conditions.

Despite this, significant portions of the literature focus on **behavioral measures** (contribution/cooperation rates, punishment assignments) rather than efficiency. There are also many adjacent studies (trust games, dictator games, principal-agent, or field settings) exploring the psychological or social basis for punishment but not outcomes linked to efficiency. Additionally, although certain dimensions (player count, rounds, MPCR, punishment cost/tech) are well covered, others (reward mechanisms, visibility/identity, communication, default contribution) receive less systematic, direct analysis.

There is also strong cross-validation across labs, countries, and parameterizations, as shown by meta-analyses and multi-lab replications. However, important limitations persist with respect to field generalizability, the interaction of multiple design dimensions, and heterogeneity in outcomes (including contexts featuring low or negative efficiency effects).

---

# 2) Task Relevance

**pgg_or_variant**  
- **Exact** relevance is high: The vast majority of the evidence directly concerns standard PGGs or very close variants (step-level games, resource dilemmas, weakest-link, etc.). The mappings to the prediction context are generally robust and explicit.
- Some **close/adjacent** studies include coordination games, trust games, delegation games, and exclusion-based designs; these are useful for mechanism but weaker for quantitative prediction.
- A minority of studies are **none/weak** relevance (e.g., studies solely of third-party punishment in dictator games), which are not informative for the core prediction task.

**punishment_or_sanctions**  
- **Exact**: Peer punishment, centralized punishment, ostracism/exclusion, and formal/informal sanctions are systematically tested; all core forms of sanctions in PGGs are covered.
- **Close/Adjacent**: Some studies cover reputation, feedback, or social-tie/diffuse punishment (e.g., gossip, signaling). These are behaviorally similar but not equivalent to costly sanctioning.
- **None/Weak**: Many studies on trust, social norms, absence/presence of communication, or reward as the only intervention do not inform punishment effects per se.

**efficiency_or_related_payoff_outcome**  
- **Exact**: Most high-quality, recent experimental papers, as well as key meta-analyses and cross-lab studies, report group earnings/profit, surplus, or efficiency (normalized). These are directly relevant.
- **Adjacent/Weak**: A sizable portion of the literature reports only contribution rates, cooperation frequency, or psychological variables; these must be carefully distinguished as *not direct measures* of efficiency, though sometimes they can be mapped onto expected efficiency if net punishment/reward costs are low or are explicitly reported.
- **None**: Many ethnographic and observational studies, and studies focusing solely on attitudinal or neural outcomes, do not address efficiency.

---

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes:**  
- **Group earnings, total coins, profit**: The primary, correctly matched outcome. E.g., several papers and multi-site replications report increases or decreases in group earnings when punishment is enabled, normalized as a share of maximum social surplus.
- **Efficiency**: Typically defined as actual group payoff divided by maximum possible under full cooperation.
- **Welfare/Surplus**: Sometimes used as synonyms for efficiency.
- **Provision Rate (in step-level games)**: Interpreted as a proxy for efficiency in threshold PGGs.

**Non-payoff behavioral outcomes:**  
- **Contribution/Cooperation rate**: Commonly presented as the fraction of possible contribution given; not equivalent to earnings/efficiency unless punishment/reward costs are negligible or explicitly netted out.
- **Punishment frequency, amount assigned**: Key for mechanism but not themselves efficiency.
- **Compliance, norm adherence**: Psychological and behavioral proxies for cooperation; not equivalent to efficiency.
- **Trust, fairness judgments, moral attitudes, emotional measures**: Relevant for mechanism modeling, not for efficiency prediction.

*Explicit mapping between contribution rate and efficiency is only valid when cost/tech of punishment, reward, or group production is specified, and actual payoff data are provided or can be reconstructed.*

---

# 4) Main Findings Relevant To Prediction

### a) *Enabling punishment in standard linear PGGs usually—but not always—increases efficiency compared to baseline, assuming punishment is sufficiently costly and well-targeted*   
- Many clean lab PGGs show that costly peer punishment (usual tech: 1 MU cost to reduce 3 MU from target) raises both cooperation and group efficiency. Efficiency gains are robust to variations in player count (typically 4-5), rounds (10–40), and MPCR in the moderate range (0.3–0.5) (e.g., Fehr et al., 2002; Gächter et al., 2017; Gintis et al., 2003; Gordon & Puurtinen, 2021; Sparks et al., 2024).
- The effect size is large in classic, well-designed experiments—with normalized payoff gains of up to 40–50% relative to control.
- However, punishment can fail to increase efficiency, or even reduce it, if:  
  - Punishment is costless or too cheap (leads to excessive/antisocial punishment) (Kuwabara & Yu, 2017; Chen et al., 2025).
  - Peer punishment is used heavily, especially antisocially, leading to deadweight loss (Fatas & Mateu, 2015; Botelho et al., 2022; Vollan et al., 2019).
  - The social context or group composition is adverse (e.g., high frequency of antisocial punishing types; cultural norm-keepers; privileged group settings; unstable punishment power) (Barclay, 2004; Suleiman & Samid, 2021; Dorrough et al., 2017).
  - Institutional design impedes effective targeting (uncertain monitoring, delayed/ambiguous feedback) (Fischer et al., 2016; Waichman & Stenzel, 2019).

### b) *The efficiency effect of punishment is highly sensitive to design dimensions, especially:*
- **Punishment cost/tech:** Punishment must be costly enough to avoid overuse, but cost/impact ratio should be high enough to deter free-riding effectively without excessive net cost (Kuwabara & Yu, 2017; Engelmann & Nikiforakis, 2015; Nikias & Sy, 2021).
- **Punishment institution (peer, centralized, democratic, collective):** Centralized or democratic punishment systems often yield higher or at least similar efficiency with lower punishment costs, compared to unrestricted peer punishment (Nockur et al., 2021; Krügel & Maaser, 2025; Harrell & Simpson, 2016; Benard & Barclay, 2020).
- **Game length (num_rounds):** Short games may see initial efficiency losses due to early high punishment use; longer games allow for learning and efficiency gains as cooperation stabilizes and punishment declines (Sparks et al., 2024; Engelmann & Nikiforakis, 2015).
- **Group size (player_count):** Positive efficiency effects are robust in small–moderate groups (4–12). Effects in large groups are more mixed and can decline due to dilution or coordination problems (Harrell & Wolff, 2023; Wu et al., 2020).
- **Communication (chat):** Enabling communication/feedback often amplifies or substitutes for punishment's positive effect; their interaction can be synergistic (Andrighetto et al., 2016; OSTROM et al., 1992; Cason & Gangadharan, 2016).

### c) *Moderators & boundary conditions:*
- **Feedback/information structure:** Clear, timely feedback linking punishment to behavior is essential for efficiency gains; ambiguous or delayed feedback reduces targeting and effectiveness (Waichman & Stenzel, 2019; Fischer et al., 2016).
- **Reward/co-reward availability:** Peer reward can sometimes yield equal or greater efficiency gains at lower cost (Gürerk et al., 2009; Nockur & Pfattheicher, 2021; Kumakawa, 2013).
- **Transparency/visibility (show_other_summaries, show_punishment_id):** Transparency about endowments, contributions, and identity of punishers can reduce antisocial punishment and increase efficiency (Chen et al., 2023; Hauser et al., 2021).
- **Baseline (control) efficiency:** Where control efficiency is already high, punishment's marginal gain is smaller or negative; in low-efficiency controls, punishment's relative effect is larger (Nair et al., 2018).
- **Social context/group composition:** Cultural norms, local prevalence of reciprocal/norm-keeping types, pre-existing conflict, and group selection mechanisms can flip the sign or size of the effect (Barclay, 2004; Suleiman & Samid, 2021).
- **Production function:** Linear PGGs respond positively to punishment, but in weakest-link, threshold, nonlinear, or alternative-defection games, punishment effects are more variable and sometimes negative (Fatas & Mateu, 2015; Mulder et al., 2006; Cason & Gangadharan, 2016).

### d) *Estimating the effect:*
- With close matching of design dimensions (group size, rounds, MPCR ≈ 0.4, standard peer punishment 1:3), typical effect is a substantial, statistically reliable increase in group efficiency (Gintis et al., 2003; Gächter et al., 2017; Sparks et al., 2024).
- In variants (peer vs. centralized/democratic, with chat, unequal endowments, high antisocial punishment), effect can be neutral or negative unless the mechanism reduces misuse and/or increases coordination/fairness (Nockur et al., 2021; Vollan et al., 2019; Fischer et al., 2016).

---

# 5) Prediction Guidance

### Overall approach:
- **In game designs matching the canonical lab PGG (4–5 players, 10–40 rounds, linear, MPCR ~0.4, no chat, punishment cost 1, impact 3):**  
  Set *treatment efficiency* with punishment **substantially higher** than the measured no-punishment control efficiency—typically a 20–40 percentage point gain relative to full cooperation (Gächter et al., 2017; Gintis et al., 2003; Sparks et al., 2024).
- **Adjust for key moderators:**
  - **Institutional structure:** Democratic/centralized or well-designed collective institutions magnify efficiency gain; standard peer punishment is effective but less so if antisocial punishment is common.
  - **Punishment cost/tech:** If cost is too low, expect over-punishment and lost efficiency; if too high, punishment is ineffective and effect shrinks. Cost/impact ratios between 1:2 and 1:3 are empirically effective.
  - **Information and feedback:** Efficiency gain only if feedback allows proper targeting of punishment. Delayed or ambiguous information reduces predicted efficiency (Waichman & Stenzel, 2019).
  - **Presence of chat/communication:** If chat is present, expect either a further positive effect (or punishment may become redundant); closely examine whether communication is before or after contribution.
  - **Transparency (showing endowments/IDs):** In unequal groups, making endowments visible is necessary for punishment to increase both efficiency and equality (Hauser et al., 2021; Chen et al., 2023).
  - **Production technology:** In weakest-link, threshold, CPR games, assess carefully: punishment can strongly increase efficiency or have no effect, contingent on local/group structure and ability to direct punishment (Fatas & Mateu, 2015; Aakre et al., 2016; Mulder et al., 2006).
- **Control efficiency as baseline:**  
  Use the measured efficiency in the no-punishment control group as a baseline; expect an increase in most linear PGGs, but magnitude depends on the design and social context as above.
- **Expect neutral or negative effects when:**
  - Peer punishment is costless (excessive punishment use);
  - Group has high antisocial punishment types or 'norm-keepers';
  - Punishment power is unstable or unequal;
  - Control efficiency is already high due to baseline norms or other interventions;
  - Monitoring/feedback is delayed or ambiguous.

---

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions (where predictive mapping is strong):**
- `player_count`, `num_rounds`, `mpcr`, `all_or_nothing` (contribution mode and production structure)
- `punishment_cost`, `punishment_tech` (cost and impact of punishment)
- `reward_exists`, `reward_cost`, `reward_tech` (comparative evidence on reward vs. punishment in some high-quality studies)
- `chat` (presence/absence and timing of communication)
- `show_other_summaries`, `show_punishment_id` (transparency and identifiability)
- `show_n_rounds` (effect of endgame knowledge: minor, but longer games allow efficiency recovery after initial punishment phase)
- `default_contrib` (rarely manipulated, but some evidence of framing effects)

**Less directly or only contextually discussed:**
- `default_contrib`: Only occasional evidence; framing effects sometimes tested.
- `show_punishment_id`: Sometimes, transparency about identity reduces antisocial punishment (Chen et al., 2023).
- Contextual factors (cultural norms, group selection, endogenous institutions, partner choice): Frequently found to moderate, but not systematically coded in all studies.

**Effectively missing:**
- Very few direct tests combining all key dimensions simultaneously; most experiments change only 1–2 dimensions at a time.
- Some combinations (e.g., high player count, high rounds, reward + punishment + chat + transparency) are rare or absent.

---

# 7) Important Limitations

- **Generality to field/non-lab environments:** Most evidence is based on lab PGGs with student samples and artificial stakes. Papers with field evidence sometimes find weaker or null effects (e.g., Noussair et al., 2015).
- **Joint manipulation of multiple dimensions:** The vast majority of studies vary only one key design dimension at a time, making interaction effects underexplored.
- **Heavy reliance on behavioral proxies:** Many older or adjacent studies, and even some recent ones, report only cooperation rates, not efficiency, necessitating caution in inferring surplus effects—especially in settings where punishment costs are high.
- **Boundary conditions for negative/neutral effects:** Badly designed punishment regimes (low cost, high heterogeneity, unstable roles, high antisocial punishment, lack of monitoring, ambiguous information) can reduce efficiency relative to baseline despite increased cooperation.
- **Cultural and group composition moderators:** Strong cross-societal/cultural variation exists. What works in a homogeneous student sample may not transfer to heterogeneous, low-trust, or high-antisocial societies.
- **Incomplete coverage of all prediction dimensions:** Some dimensions (default contribution, interaction of reward and punishment, history of prior interventions, partner choice, entry/exit options) are underexplored relative to their potential impact on efficiency.

---

**In conclusion**, the literature base is highly relevant and directly informative for predicting efficiency in PGGs from design and baseline efficiency, provided care is taken to match on dimensions like punishment cost/tech, institutional structure, communication, and transparency. Several design features systematically moderate the effect. Use control (no-punishment) efficiency as a base, with substantial positive increments expected for enabling well-designed punishment in linear PGGs, but adjust downward or to zero for negative boundary cases identified above. Adoption of more sophisticated or democratic punishment institutions, effective information/feedback, and high transparency can strengthen the efficiency gains further, while designs allowing antisocial or excessive punishment, or lacking proper targeting, can negate or reverse the effect.
