# 1) Evidence Base

The paper set includes 13 studies, mainly recent empirical contributions, with a strong representation of laboratory experiments (especially on public goods games, "PGG") and several field experiments or adjacent studies. The majority are experimental studies with well-documented game parameters. Two papers use hypothetical scenarios or attitudinal measures. There are no pure theory or modeling papers in the set.

The focus is somewhat broad for the prediction task: roughly half the studies directly address PGGs with efficiency or closely related payoff outcomes and peer punishment. Others address adjacent games (common-pool resource games, stag hunt, dictator/helping tasks, allocation games), or outcome measures not centered on efficiency (behavioral outcomes only, such as contribution rates or norm compliance).

Overall, the empirical evidence for direct, quantitative prediction of the efficiency effect of punishment in PGG-like environments is present but not exhaustive. Some key design dimensions are studied in detail in a few papers; however, several dimensions are only referenced contextually or missing.

# 2) Task Relevance

**pgg_or_variant**
- **exact:** Kocher & Matzat (2016); Engelmann & Nikiforakis (2015); Campos-Vazquez & Mejia (2016); Drouvelis et al. (2015); Martinsson et al. (2015)
- **close:** Noussair et al. (2015) (common-pool resource framed field experiment); Becchetti et al. (2015) (CPRG)
- **adjacent/weak:** Remaining papers use adjacent designs or hypothetical scenarios.

**punishment_or_sanctions**
- **exact:** Kocher & Matzat (2016); Engelmann & Nikiforakis (2015); Campos-Vazquez & Mejia (2016); Noussair et al. (2015); Leibbrandt & López-Pérez (2014); Liu & Riyanto (2017); Roberts et al. (2013); Lopez (2017); Gordon & Lea (2016)
- **none/weak:** Several papers do not include punitive institutions (Drouvelis et al., Martinsson et al., Becchetti et al., Manesi et al.)

**efficiency_or_related_payoff_outcome**
- **exact:** Kocher & Matzat (2016); Engelmann & Nikiforakis (2015); Becchetti et al. (2015)
- **adjacent:** Noussair et al. (2015); Liu & Riyanto (2017); Campos-Vazquez & Mejia (2016)
- **none/weak:** Most other studies report only non-payoff behavioral outcomes (contributions, norm compliance, etc.) or attitudinal outcomes.

**Summary:** Only a small subset directly and quantitatively addresses the prediction task: repeated public goods games with and without peer punishment, measuring efficiency or group payoff. Most others are less directly relevant either due to missing punishment, lack of efficiency outcomes, or use of distinct game structures.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (efficiency, group payoff, welfare):**
    - Kocher & Matzat (2016): Explicit group efficiency (payoff ratio to full cooperation)
    - Engelmann & Nikiforakis (2015): Group earnings, efficiency increases/misses depending on punishment structure.
    - Becchetti et al. (2015): Group efficiency and total payoffs in common-pool setting.
- **Behavioral (non-payoff) outcomes:**
    - Most studies focus exclusively on contribution rates, cooperation, punishment frequency, or sentiment (Campos-Vazquez & Mejia, Drouvelis et al., Martinsson et al., Noussair et al., Leibbrandt & López-Pérez, Liu & Riyanto, Roberts et al., Lopez, Gordon & Lea, Manesi et al.).
- **Intermediate/adjacent measures:**
    - Some field studies and non-PGG experiments report related but not equivalent behavioral proxies (e.g., effort, catch, hypothetical sentiment, likability, willingness to pay to punish).

**Separation:** Only a few studies report actual realized group payoffs or efficiency, which are necessary for the downstream prediction task. Most report outcomes (e.g., average contribution) that are not themselves efficiency, although frequently presumed to be closely related.

# 4) Main Findings Relevant To Prediction

**Empirical Synthesis:**

- **Peer punishment often increases cooperation/contributions but does not always increase efficiency.** The main reason is the cost of punishment, which can outweigh the gains from higher cooperation, especially if punishment is overused or feuding occurs (Kocher & Matzat, 2016; Engelmann & Nikiforakis, 2015).
- **The design of the punishment mechanism matters critically for efficiency effects.** "Rich" punishment environments, with multiple punishment stages, fixed IDs, or full information facilitating retaliation or vendettas, can nullify or reverse expected efficiency gains—even if cooperation rises—because punishment costs are large (Engelmann & Nikiforakis, 2015).
- **Reward mechanisms may promote both higher contributions and higher efficiency.** When compared, reward institutions are both preferred and more efficient than punishment or control (Kocher & Matzat, 2016).
- **No or negative effect of punishment in field or non-lab-like conditions.** Field experiments or CPRG variants sometimes find that punishment and reward do not increase cooperation or efficiency, suggesting limited generalizability of classic lab results (Noussair et al., 2015; Becchetti et al., 2015).
- **Transparency/monitoring without punishment can reduce efficiency.** Providing public feedback in the absence of formal sanctions can worsen free riding and undermine group efficiency (Becchetti et al., 2015).
- **Centralized (leader) punishment can increase cooperation.** However, efficiency is unreported; the effect on actual payoff is unknown (Campos-Vazquez & Mejia, 2016).

**Non-payoff and theoretical arguments:**
- Studies on mechanisms, motivations, or sentiment (adjacent environments) underline that punishment is often motivated by inequity aversion or norm enforcement, but such studies do not link these patterns to realized efficiency (Leibbrandt & López-Pérez, Roberts et al., Lopez, Gordon & Lea).
- Structural elements like the publicness of feedback, identity revelation (e.g., show_punishment_id), and presence of retaliation possibilities, can be influential for punishment's effectiveness—but evidence for their effect on efficiency is indirect or absent.

# 5) Prediction Guidance

**For quantitative prediction of treatment efficiency (efficiency when peer punishment is enabled, controlling for game design and control efficiency):**

- **Punishment tends to increase contributions but not always efficiency.** Prediction should not assume a positive treatment effect on efficiency; in many standard PGG designs, enabling peer punishment reduces efficiency relative to control (no punishment) because the cost of punishing outweighs the gain in group contributions (Kocher & Matzat, 2016).
- **Punishment structure moderates effect.** Efficiency increases are possible when punishment is constrained to a single, anonymous stage without opportunity for retaliation, especially for longer, repeated games—here, substantial gains relative to control may accrue in later rounds (Engelmann & Nikiforakis, 2015). When punishment is unconstrained, or IDs and histories are fully transparent (facilitating vendettas), gains are lost or reversed.
- **Important dimensions for prediction:**
    - **punishment_cost** and **punishment_tech** are critical: Lower cost, higher impact punishment can support group efficiency only if used sparingly.
    - **show_punishment_id** and **punishment tech (e.g., anonymity, number of stages):** Environments enabling retaliation or non-anonymous punishment are at risk of feuding and thus efficiency losses.
    - **num_rounds:** Efficiency gains from punishment, where present, emerge over time; short games show less effect.
    - **chat:** Evidence is limited, but its absence does not moderate the efficiency effects of punishment (Kocher & Matzat, 2016).
    - **reward_exists, reward_cost/tech:** When present, reward institutions can outperform both punishment and control in efficiency.
- **Field environment caution:** Do not extrapolate lab results naively to field or real-world CPR environments; positive effects of punishment on efficiency are not robust outside tightly controlled standard PGG designs.

**When design or outcome details are sparse, predictions should be cautious and may default to null or negative efficiency effects of punishment, relying heavily on the directness of the game structure to canonical PGGs.**

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**
- **player_count**: Standard (often 4-player) games in core studies (Kocher & Matzat, Engelmann & Nikiforakis, etc.), usually with constant effects.
- **num_rounds**: Varied (e.g., 30-round repeated games), empirically shown to affect efficiency trajectory (Engelmann & Nikiforakis, 2015).
- **mpcr**: Explicitly manipulated/recorded in core efficiency studies.
- **all_or_nothing**: Most studies use continuous contributions, but several examine all-or-nothing designs; however, little direct comparison of its impact on efficiency with punishment.
- **punishment_cost, punishment_tech**: Detailed manipulation/contrast in a few studies, with strong evidence of moderating role.
- **show_punishment_id**: Addressed in studies examining anonymity vs. full ID; directly linked to retaliation/feuding concerns (Engelmann & Nikiforakis, 2015).
- **reward_exists/reward_cost/reward_tech**: Directly manipulated in studies comparing reward to punishment (Kocher & Matzat, 2016).

**Indirectly Informed/Contextual:**
- **chat:** Not manipulated; noted absent in Kocher & Matzat (2016).
- **show_n_rounds, show_other_summaries:** Monitored or referenced, but rarely manipulated to test efficiency outcomes directly.
- **default_contrib:** Framing discussed, but not centrally manipulated for efficiency outcomes with/without punishment.

**Effectively Missing (very rarely or never directly linked to efficiency-punishment effects):**
- **show_punishment_id** in precise quantitative fashion.
- **reward_magnitude** and comparable details, outside of rare comparisons.
- **Contextual variables** like social class, personality, status: explored in relation to behavioral/attitudinal outcomes but not efficiency.
- Some studies report only on behavioral proxies, with little or no reporting on group payoffs/efficiency.

# 7) Important Limitations

- **Sparse direct evidence for the key prediction task.** Only a handful of papers deliver the necessary exact intersection: repeated PGG (or close variant), direct peer punishment manipulation, and explicitly reported efficiency or group payoff outcomes.
- **Many studies conflate behavioral and payoff outcomes.** A rise in contributions from punishment does not necessarily equate to improved efficiency, due to punishment costs; yet several adjacent studies report only on contributions, not efficiency.
- **Generalizability concerns.** Field and CPRG experiments show different patterns for punishment effectiveness and efficiency, cautioning against overgeneralization from lab-based PGGs.
- **Limited exploration of many design dimensions.** Several potentially important factors (e.g., visibility of punishers, information salience, contribution framing, reward magnitude/structure, and the role of repeated/randomly matched partners) are absent or only peripherally addressed.
- **No formal theory/model-based extrapolation.** Mechanism or moderator arguments are frequently speculative or based on behavioral outcomes.
- **Ambiguity in dimension interactions.** Some papers show efficiency gains from punishment if and only if certain restrictive institutional or informational designs are in place; the downstream prediction task is critically sensitive to capturing such interactions, yet current evidence is fragmented.
- **No meta-analytic or comparative quantitative summary is available.** Effect sizes are not aggregated or contextualized across studies; quantitative prediction must rely on the most directly comparable individual studies.

**Bottom line:** The literature synthesizes to strong caution: enabling peer punishment in linear PGGs may decrease group efficiency unless punishment is carefully structured (cost, anonymity, no retaliation), and results are highly sensitive to game design. Only some design dimensions are robustly studied; data on others is missing or too indirect for confident prediction. Behavioral outcomes should not be substituted for efficiency in prediction.
