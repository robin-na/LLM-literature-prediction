# 1) Evidence Base

The paper set comprises 12 sources spanning both empirical and theoretical studies, with most contributions coming from theory or review papers, and only a minority reporting new empirical (experimental) data. The empirical base is somewhat narrow for the prediction task—just one core study directly tests the treatment effect of peer punishment on efficiency in a public goods game (PGG) with relevant design dimensions (Grechenig et al., 2010). Several theory and modeling papers discuss public goods or closely related social dilemmas with punishment mechanisms, often drawing on evolutionary game theory or conceptual synthesis, but empirical tests of efficiency effects under varied design dimensions are sparse. Many papers focus on mechanisms, moderators, and conceptual frameworks rather than directly reporting efficiency or welfare changes from enabling punishment across PGG variants.

# 2) Task Relevance

**pgg_or_variant:**
- **exact:** Grechenig et al. (2010), Kraak (2011), Zhu et al. (2020), Liu et al. (2019)
- **close:** Vasconcelos et al. (2013), Raihani & Aitken (2011)
- **adjacent:** Bicchieri et al. (2004), Jagers et al. (2020), Dugatkin (2002), Clavien & Chapuisat (2013), Wang et al. (2022), Cushman (2015)

**punishment_or_sanctions:**
- **exact:** Grechenig et al. (2010), Kraak (2011), Zhu et al. (2020), Vasconcelos et al. (2013), Cushman (2015)
- **adjacent:** Liu et al. (2019, via exclusion), Bicchieri et al. (2004, via contingent strategies), Jagers et al. (2020), Dugatkin (2002), Clavien & Chapuisat (2013), Raihani & Aitken (2011)
- **none:** Wang et al. (2022)

**efficiency_or_related_payoff_outcome:**
- **exact:** Grechenig et al. (2010), Liu et al. (2019), Bicchieri et al. (2004)
- **close/adjacent:** Kraak (2011), Vasconcelos et al. (2013), Raihani & Aitken (2011), Cushman (2015), Dugatkin (2002)
- **weak/none:** Clavien & Chapuisat (2013), Wang et al. (2022), Jagers et al. (2020), Zhu et al. (2020)

**Summary:** Only a handful of papers provide direct, exact evidence for the downstream prediction task: experimental PGGs with peer punishment, with efficiency as the outcome. Most other contributions are theoretical, adjacent in domain, or only address behavioral proxies for cooperation.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:** Explicit group efficiency, average payoff, group welfare, or surplus are measured directly in only a few papers (Grechenig et al., 2010; Liu et al., 2019; Bicchieri et al., 2004 (trust game analog)). Several theory papers assert higher payoff or welfare as a consequence of increased cooperation but typically do not present empirical evidence or quantitative model output.
- **Non-payoff behavioral outcomes:** The majority of papers (especially theory/modeling) focus on contribution rates, cooperation frequencies, prevalence of particular strategies, or the likelihood of successful group outcomes (Vasconcelos et al., 2013; Zhu et al., 2020). These are not payoff or efficiency outcomes, though they are closely related.
- **Other outcomes:** Some papers focus on the conditions for norm emergence, stability of cooperation, punishment assignment, second-order punishment, or the effect of institution design on behavior or motivation.

# 4) Main Findings Relevant To Prediction

### Empirical Findings:
- **Peer punishment increases efficiency only under accurate information:** In laboratory PGGs, enabling peer punishment increases efficiency above the control baseline only if information about contributions is accurate. Under noise/uncertainty, frequent and less targeted punishment leads to efficiency losses below control levels (Grechenig et al., 2010).
  
### Theory/Model Findings:
- **Punishment generally supports higher cooperation and, by extension, efficiency:** Many papers argue or model that punishment (when deployed appropriately) stabilizes cooperation and can increase average payoffs (Kraak, 2011; Liu et al., 2019; Bicchieri et al., 2004). However, direct efficiency outcomes are often inferred rather than measured.
- **Effectiveness of punishment is conditional on specific moderators:** Communication, transparency, reputation mechanisms, and institutionalization make punishment more effective and less destructive (Kraak, 2011; Cushman, 2015; Vasconcelos et al., 2013). When punishment is informal or information is noisy, it can reduce efficiency due to retaliation cycles or antisocial punishment (Grechenig et al., 2010; Cushman, 2015).
- **Repeated interaction and conditional strategies enable emergence of efficiency, even without formal punishment:** In repeated trust games, longer interactions allow contingent punishment (strategy-based) that increases efficiency, analogous to repeated PGGs with peer sanctioning (Bicchieri et al., 2004).
- **Alternative sanctions (exclusion) can outperform punishment:** Pool exclusion (costly removal of defectors) can be a more robust mechanism for maintaining high efficiency than punishment alone, especially when institutionalized (Liu et al., 2019).
- **Scale and complexity reduce the effectiveness of informal punishment:** In large groups, diverse populations, or high-complexity settings, informal peer punishment loses effectiveness, and formal, external interventions become more important (Jagers et al., 2020).

# 5) Prediction Guidance

To predict treatment efficiency from design dimensions and control efficiency:

- **Leverage direct empirical results:** In lab PGGs, expect peer punishment to increase efficiency **if** information about contributions is accurate and visible (Grechenig et al., 2010). If the design includes noise or uncertainty (e.g., partial/inaccurate contribution summaries), enabling punishment may reduce efficiency below control.
- **Mechanism insights as moderators:**
    - **Presence of communication or reputation mechanisms** (chat, identity revelation, summary visibility) further increases the efficiency advantage of peer punishment (Kraak, 2011).
    - **Punishment is less effective or even destructive** if deployed in large or anonymous groups, with increased opportunity for antisocial punishment or retaliation (Jagers et al., 2020; Cushman, 2015).
- **Interpret evidence cautiously when outcomes are behavioral, not payoff-based:** Many theory/modeling results (e.g., frequency of cooperation) likely translate into higher efficiency, but do not directly quantify group payoff or efficiency effects.
- **Use design dimension cues:** Direct empirical evidence mostly addresses effects when varying information quality, but not across the full space of `player_count`, `mpcr`, `punishment_cost`, etc. Where theory aligns, expect peer punishment to boost efficiency in small, transparent groups, with moderate punishment costs and clear monitoring.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions:**
- **Information accuracy/transparency (contextually via `show_other_summaries`, `show_punishment_id`)**: Grechenig et al. (2010).
- **player_count:** Several papers (Kraak, 2011; Vasconcelos et al., 2013; Liu et al., 2019; Jagers et al., 2020; Bicchieri et al., 2004).
- **num_rounds:** Bicchieri et al. (2004), Kraak (2011), Liu et al. (2019), Wang et al. (2022).
- **chat:** Kraak (2011), Jagers et al. (2020).
- **mpcr:** Grechenig et al. (2010), Kraak (2011), Liu et al. (2019).
- **punishment_cost/punishment_tech:** Grechenig et al. (2010), Zhu et al. (2020), Vasconcelos et al. (2013), Liu et al. (2019).

**Indirectly/contextually discussed:**
- **reward_exists, reward_cost, reward_tech:** Only Raihani & Aitken (2011) discuss rewards alongside punishment, mostly theoretically.
- **show_n_rounds:** Bicchieri et al. (2004), Wang et al. (2022).
- **all_or_nothing:** Some theory papers specify discrete vs. continuous strategies (Kraak, 2011; Vasconcelos et al., 2013).

**Effectively missing for prediction:**
- **default_contrib:** Not directly addressed.
- **punishment magnitude:** Rarely speciﬁed, aside from cost/benefit ratios.
- **show_punishment_id:** Little direct evidence on effects of punisher anonymity or identity.
- **Reward mechanism details (costs/magnitude):** Mostly discussed only at a theoretical level.
- **Simultaneous visibility of other group summaries:** Mentioned only in context.

# 7) Important Limitations

- **Empirical evidence for efficiency effects of punishment in PGGs is thin and highly conditional:** Only one experimental study (Grechenig et al., 2010) directly measures changes in efficiency with treatment and control; others are theory-driven or focus on behavioral proxies.
- **Model-based findings may not generalize to finite experimental settings:** Many modeling papers assume infinite or well-mixed populations, or focus on strategy frequencies rather than actual payoffs (Liu et al., 2019; Bicchieri et al., 2004; Zhu et al., 2020).
- **Many design dimensions are not systematically varied:** There is little empirical or quantitative modeling evidence across variations in `player_count`, `mpcr`, `punishment_cost`, `reward_tech`, `default_contrib`, or the full set of used design parameters.
- **Behavioral and payoff effects are often conflated:** Cooperation and contribution rates are frequently assumed to imply higher efficiency, but this is not always validated by explicit payoff measures (Clavien & Chapuisat, 2013).
- **Lack of quantitative magnitude estimates:** Most theory papers, and even reviews, offer qualitative guidance but not effect size estimates, hampering the calibration of predictions.
- **Scale, anonymity, and complexity often undermine efficiency gains from punishment:** In larger, decentralized, or high-noise groups, punishment can backfire via mistargeting or retaliation, reducing rather than enhancing efficiency (Grechenig et al., 2010; Jagers et al., 2020).

**In conclusion**, for the prediction task, the literature offers limited but actionable guidance: Peer punishment’s efficacy in increasing average efficiency above control depends crucially on information accuracy, communication, and group structure. Predictive models should incorporate these moderating conditions explicitly, and exercise caution when generalizing from cooperation rates to payoff-based efficiency, or when extrapolating findings across untested design dimensions.
