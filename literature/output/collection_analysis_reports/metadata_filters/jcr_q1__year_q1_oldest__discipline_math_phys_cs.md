# 1) Evidence Base

The paper set consists overwhelmingly of **theoretical and simulation-based studies** (theory: ∼26/31), with a smaller number of **empirical laboratory or observational studies** (empirical: ∼5/31). Most papers address **micro-founded social dilemma games**—such as public goods games (PGG), repeated partnerships, or adjacent settings (e.g., resource allocation, partner matching, or ultimatum games)—and focus on the mechanisms underpinning cooperation, punishment, and social structure.

For the **downstream prediction task**—predicting average efficiency when enabling peer punishment in PGG-like environments—**the evidence base is broad in its coverage of mechanism and theory, but relatively sparse in direct empirical estimates of payoff-based treatment effects**. While several papers deliver payoff-related (efficiency) results in exactly matched or closely analogous environments, many others focus primarily on cooperation rates, strategy types, or the emergence of social norms, which must be interpreted with caution for payoff/efficiency prediction.

# 2) Task Relevance

Relevance is assessed across three dimensions, using the labels `exact`, `close`, `adjacent`, `weak`, and `none`:

**a) PGG or Variant**
- Several theory and simulation studies model the public goods game *exactly* (Wang et al., 2011; Helbing et al., 2010; Zhang et al., 2010; Wang et al., 2012; Xiao & Hua, 2012).
- A significant number focus on **close or adjacent games**, such as repeated partnerships, resource allocation, or collective-risk dilemmas (e.g., ABREU et al., 1991; Santos et al., 2012; Brown et al., 2004). Others use prisoner's dilemma, ultimatum, or other social dilemmas (adjacent), which require translation to the PGG context with care.

**b) Punishment or Sanctions**
- Well represented: many papers include explicit punishment or sanctioning mechanisms ranging from **peer punishment in PGG** (exact), to centralized or informal punishment, exclusion, or flexible retaliation (close/adjacent). Several analyze related but distinct "punishment-like" mechanisms such as ostracism, contract termination, or endogenous negative incentives.

**c) Efficiency or Related Payoff Outcome**
- Directly reported **efficiency or total payoff outcomes** are present in a subset of theory and empirical papers (Wang et al., 2011; ABREU et al., 1991; Evans & Thomas, 2001; Cai & Kock, 2009; Nuño et al., 2010; Brown et al., 2004).
- Many others focus on **contribution or cooperation rates**—behavioral, not payoff—and must be treated as *indirect* indicators of efficiency rather than direct outcomes.
- Some studies are **explicitly non-payoff** or only discuss efficiency contextually.

**Summary**: The relevance for the *specific prediction task* is:
- `pgg_or_variant`: *broad coverage* (several exact, many close)
- `punishment_or_sanctions`: *broad coverage* (many exact or close)
- `efficiency_or_related_payoff_outcome`: *mixed*, with fewer *direct* empirical measurement and substantial reliance on theory or indirect outcomes.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes** (directly relevant to efficiency):
- *Group efficiency*: ratio of achieved to maximal cooperative payoff (Wang et al., 2011; Tao et al., 2011; Evans & Thomas, 2001; Cai & Kock, 2009; Nuño et al., 2010).
- *Total/group payoff, welfare, surplus*: often used interchangeably, especially in theoretical models.
- *System utility/wealth*: synonyms in simulation-based resource allocation settings.
- *Average payoff in the presence/absence of punishment*: occasionally directly comparable (e.g., Wang et al., 2011).

**Non-payoff behavioral outcomes** (must not be conflated with efficiency):
- *Contribution or cooperation rate*, *fraction of cooperators*, *mean effort*, *punishment frequency/assignment*, *emergence of strategy types*, and *norm compliance* (measured widely; e.g., Helbing et al., 2010; Shutters, 2012; Falk et al., 2005).
- *Distribution of offers/thresholds* in ultimatum or other games.
- *Reputation*, *social norm adherence*, or *frequency of tag-based interactions*.

**Caution:** Many papers measure *behavioral* rather than *payoff* outcomes—positive shifts in cooperation rates often (but not always) translate to higher efficiency, but not in every model (e.g., miser-slave dynamics; Frean & Abraham, 2004).

# 4) Main Findings Relevant To Prediction

Synthesizing across papers with highest task relevance:

**a) Theoretical Models (PGG/Close Variants, Payoff Outcomes)**
- **Enabling peer punishment generally increases efficiency** in PGG or closely related games, particularly when the control (no-punishment) baseline is dominated by defectors or non-cooperation (Wang et al., 2011; Evans & Thomas, 2001; Cai & Kock, 2009; Tao et al., 2011; Nuño et al., 2010).
- **Robustness:** The efficiency gain is often found to be robust across moderate variations in group size, population size, and punishment cost (Wang et al., 2011; Helbing et al., 2010).
- **Parameter Sensitivity:**
    - The **cost and effectiveness** of punishment set a threshold for positive efficiency effects: if punishment is too costly or too weak, gains are limited or absent (Helbing et al., 2010; Cai & Kock, 2009; Nuño et al., 2010).
    - **Spatial structure and social networks** can enhance the efficacy of punishment; in well-mixed populations, effects are weaker or absent unless punishment is very severe (Helbing et al., 2010; Shutters, 2012).
    - **Voluntary participation (entry/exit) and small entry fees** can amplify the effect of punishment in dynamic or anonymous settings (Wang et al., 2011).
    - **Information timing, patience/discounting, and monitoring quality** are critical moderators: punishment only produces high efficiency when players are sufficiently patient and monitoring is informative (ABREU et al., 1991; Evans & Thomas, 2001; Thomadsen & Bhardwaj, 2011).
    - **Retaliation or revenge cycles** can undermine efficiency if punishment is not credibly limited or coordinated (Varga et al., 2010).

**b) Empirical and Simulation-based Studies**
- Direct lab experiments in adjacent, not exact, PGG settings *rarely* report group efficiency or total payoff explicitly. Where efficiency is not measured, results must be interpreted cautiously.
- Behavioral findings show **high rates of targeted punishment by cooperators**, willingness to pay to punish defectors, and norm enforcement (Falk et al., 2005; Goette et al., 2012), but without efficiency measurement, these inform *mechanism* rather than *magnitude* of the efficiency effect.

**c) Mechanism Arguments / Theory**
- **Sufficiently severe/credible punishment guarantees efficiency**—provided it is not too costly or uncoordinated—and mild punishment is often insufficient (Evans & Thomas, 2001; Cai & Kock, 2009).
- **Excessive punishment expenditure**, or antisocial punishment (targeting in-group or out-group members for reasons unrelated to cooperation), can offset or reverse efficiency gains (Nuño et al., 2010; Goette et al., 2012).
- **Indirect/sanctioning mechanisms** (ostracism, contract renewal, adaptive networking) can act as functional substitutes for explicit punishment in raising efficiency (Brown et al., 2004; Zimmermann & Eguíluz, 2005).

# 5) Prediction Guidance

Given the above evidence, the following guidance should inform prediction of treatment (punishment-enabled) efficiency from control efficiency and game design dimensions:

- **Punishment will generally increase treatment efficiency over control**, particularly when baseline (control) efficiency is low due to widespread defection (supported by both theory and simulation—Wang et al., 2011; Evans & Thomas, 2001; Cai & Kock, 2009; Tao et al., 2011).
- **Magnitude of efficiency boost** depends on:
    - *Punishment cost/effectiveness ratio* (high effectiveness at moderate/low cost yields maximal gains; if cost is high or penalties are weak, gains are muted or absent).
    - *Game structure*: Structured populations (networks, spatial clustering) amplify punishment’s effects; well-mixed settings or anonymous populations may require stricter punishment or additional measures (Helbing et al., 2010; Shutters, 2012).
    - *Monitoring/information*: Imperfect or delayed information can *reduce or enhance* efficiency, depending on players' patience and the nature of the monitoring technology (ABREU et al., 1991).
    - *Game duration*: Infinite or sufficiently long games with patient participants support greater efficiency increases from punishment; in finitely repeated games, efficiency gain can erode near endgame (Tao et al., 2011).
    - *Norms and retaliation*: If punishment provokes retaliation cycles or is misapplied (e.g., antisocial punishment in competitive contexts), efficiency gains may be dampened or negative (Goette et al., 2012; Varga et al., 2010).
- **Control efficiency is informative**: When the no-punishment efficiency is already high (due to, e.g., partner choice, ostracism, or reputation effects), the marginal efficiency gain from enabling punishment may be small or even negative (Frean & Abraham, 2004).

**Absent or ambiguous context**: Precise quantitative estimates of the treatment-control difference in efficiency are not available from this paper set, particularly for real-world-scale or large-group lab games. Most direct evidence is theoretical or simulation-based.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- `player_count` (group size): Multiple studies test robustness across group size (Wang et al., 2011; Helbing et al., 2010; Cai & Kock, 2009), generally finding that moderate group size does not undermine punishment’s positive effect, though larger groups may dilute peer monitoring/punishment (Helbing et al., 2010).
- `num_rounds`: Game length matters; infinitely or sufficiently long games support stronger efficiency gains from punishment (ABREU et al., 1991; Tao et al., 2011), while finite rounds (and endgame effects) can curtail this.
- `mpcr`: Synergy factor or marginal return is a critical moderator of both baseline and treatment efficiency (Helbing et al., 2010; Cai & Kock, 2009).
- `punishment_cost` & `punishment_tech`: Effectiveness and cost of punishment shape the threshold and stability of efficiency (Helbing et al., 2010; Cai & Kock, 2009; Nuño et al., 2010).
- `reward_exists`: Some studies examine combinations or tradeoffs between reward and punishment (Wang et al., 2011; Varga et al., 2010).

**Indirectly Informed Dimensions:**
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Information release, transparency, and monitoring technology are critical in repeated games but are not always explicitly modeled as separate experimental dimensions (ABREU et al., 1991; Evans & Thomas, 2001).
- `all_or_nothing`, `default_contrib`: Studied in some models, showing that binary or continuous contribution frames can moderate strategic complexity but do not fundamentally change the direction of punishment effects.
- `chat`: Communication is infrequently studied but may moderate coordination and norm emergence (Shutters, 2012).
- `reward_cost`, `reward_tech`, `reward_magnitude`: Examined primarily as points of contrast with punishment or as robustness checks (Wang et al., 2011).

**Contextually Discussed or Missing:**
- Many subtle aspects—such as the specific user interface for judgments, presentation of previous rounds’ actions, or cognitive limitations (e.g., `forgetfulness` in Thomadsen & Bhardwaj, 2011)—are discussed conceptually but not as systematic dimensions.
- `show_punishment_id`: Studied mainly in mechanism or theory form, not as lab manipulations.

# 7) Important Limitations

- **Empirical coverage of direct efficiency outcomes is limited**: Most findings are theoretical or simulation-based; empirical lab evidence for the average group efficiency impact of enabling peer punishment is sparse.
- **Parametric/structural gaps**: The paper set does not jointly vary all prediction dimensions, so interactions (e.g., between group size and punishment cost, or between monitoring and social structure) are incompletely mapped.
- **Reliance on behavioral proxies**: A large fraction of studies measure cooperation/contribution rates or punishment targeting and must be translated with caution when predicting efficiency.
- **Ambiguity in punishment implementation**: Some models abstract away from real-world implementation details (e.g., how punishment is allocated, social vs. centralized punishment, or whether retaliation is possible) and so do not always translate cleanly to applied environments.
- **Scope for antisocial or inefficient punishment**: Several studies indicate that, depending on social context (e.g., intergroup competition or partner identity), punishment may be misdirected, reducing—not increasing—efficiency (Goette et al., 2012).
- **Structural differences in adjacent models**: Findings from repeated partnership, resource allocation, or ultimatum games may not fully generalize to standard PGG settings.
- **Absence of contextual moderators**: Factors such as voluntary participation, mobility, tag-based recognition, and information delays—occasionally shown to be crucial moderators—are only addressed in isolated studies.
- **Lack of granular empirical calibration**: Theoretical and simulation models often show qualitative robustness, but quantitative calibration to lab or field data is not available.

---

**Conclusion**: This literature set strongly supports the *qualitative* expectation that enabling (peer) punishment will usually increase average efficiency in public-goods-game-like environments, relative to a no-punishment control, especially when punishment is sufficiently credible and coordinated, and baseline cooperation is low. However, the effect is *parameter-dependent*, and the lack of direct empirical estimates for all interactions among design dimensions means that careful attention to contextual moderators, theoretical thresholds, and known failure cases is warranted when translating these findings to new prediction tasks.
