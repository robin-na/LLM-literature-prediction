# 1) Evidence Base

The paper set comprises a robust blend of empirical laboratory and field studies, alongside a substantial number of theoretical and simulation/modeling papers. Empirical work predominantly uses repeated public goods games (PGGs) or close variants, with a smaller subset employing adjacent game structures such as the Prisoner's Dilemma or trust games. Theoretical contributions span evolutionary models, mechanism design, and simulations of reputation, mutation, and spatial structure effects.

With **99 papers** in total, the breadth is strong; however, papers with *direct measurement of efficiency or group payoff in PGGs with punishment enabled vs. disabled* are a subset. Many studies are directly on PGGs (`pgg_or_variant=exact`), utilize punishment or sanctioning institutions (`punishment_or_sanctions=exact`), and report or clearly infer efficiency or payoff-related outcomes (`efficiency_or_related_payoff_outcome=exact/close`). Still, a notable fraction focus on adjacent designs, on behavioral mechanisms (not payoff), or provide only theoretical context.

Empirical findings are well represented for standard lab PGGs with punishment, but empirical coverage thins as one moves to complex and field contexts (e.g., CPR settings, large groups, endogenous institution choice, or highly structured environments). The theoretical literature is broader and covers a rich space of moderators and mechanisms.

# 2) Task Relevance

**pgg_or_variant:**  
- *Exact relevance* dominates: Most leading papers manipulate standard PGG structures, especially for lab studies and many theory papers.  
- *Close/adjacent relevance* is common (especially among works using indirect reciprocity or dyadic games), useful for certain design dimensions, but less so for precise quantitative prediction.  
- A minority are only *contextually relevant* (e.g., trust games, dictator games, or animal studies).

**punishment_or_sanctions:**  
- *Exact* treatment of peer or institutional punishment is frequent, especially in influential experimental and theoretical papers.
- *Close* or *adjacent* treatments cover reputation-based, third-party, or ostracism mechanisms, or where punishment is bundled with reward.
- Some papers only discuss punishment conceptually.

**efficiency_or_related_payoff_outcome:**  
- Several leading PGG lab and theory papers report *efficiency* or total payoff directly.
- Some (including widely cited) report only on *contribution rate*, *norm compliance*, or *behavioral outcomes:* these are not efficiency, though sometimes closely correlated.
- A subset infer efficiency via clear payoff structure; others measure only behavioral change with speculation about efficiency.

Overall, the literature’s *direct* relevance to the prediction task is substantial, but for some moderators and context, we must rely on indirect or adjacent evidence, or interpolate from behavioral results.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes (Directly relevant for prediction):**
- *Efficiency*: Often defined and measured as group payoff divided by the payoff under full cooperation (e.g., Rand et al. 2009; Gürerk et al. 2006; Eriksson & Strimling, 2012).
- *Total group earnings/welfare/surplus/coins generated*: Commonly reported in both empirical and theoretical works (e.g., Fehr & Gächter, 2002; Bodnar & Salathé, 2012).
- *Mean/median individual payoff*: Sometimes used as the main outcome.

**Non-payoff behavioral outcomes (Indirect/adjacent relevance):**
- *Contribution/cooperation rate*: Frequently measured as a key behavioral indicator (e.g., Fehr & Gächter, 2002; Baldassarri & Grossman, 2011).
- *Frequency, intensity, and targeting of punishment*: Detailed in many studies (e.g., Herrmann et al., 2008; Fehl et al., 2012).
- *Norm compliance, anti-social punishment, strategic partner choice*.
- *Emotional or neural correlates of punishment*: Present especially in work on motivation/mechanism.

**Distinction:**  
Many papers find significant increases in *contributions* with punishment but sound a note of caution: *contribution rate rises do not always equate to higher efficiency* due to the direct costs of punishment, retaliation cycles, or anti-social use of sanctions (see, e.g., Rand et al., 2009; Fehl et al., 2012; Herrmann et al., 2008). A subset of papers highlight contexts where punishment reduces efficiency—even with higher cooperation—if punishment costs outweigh cooperative gains (Janssen et al., 2010; Dreber et al., 2008).

# 4) Main Findings Relevant To Prediction

**Empirical and theoretical studies converge on several key points:**

- **Punishment generally increases efficiency in standard repeated PGGs, but the effect is moderated:**  
  - *Direct evidence* (Rand et al., 2009; Gürerk et al., 2006; Fehr & Gächter, 2002) shows that enabling peer punishment typically raises efficiency substantially.  
  - *However*, this is less true if:  
    - Vendettas or retaliation cycles occur (Fehl et al., 2012).
    - Anti-social punishment is common, as in some cultural contexts (Herrmann et al., 2008).
    - The punishment is too weak/expensive to deter defection (Eriksson & Strimling, 2012; Perc, 2012).

- **Punishment is less efficient than reward; in combined settings, punishment can reduce efficiency:**  
  - Reward often yields higher payoffs than punishment (Rand et al., 2009).
  - When both are allowed, punishment use is linked to lower efficiency, largely due to cost (Rand et al., 2009).

- **Institutional features and moderators shape the effect of punishment on efficiency:**
  - *Communication*: When allowed, it can substitute for or amplify punishment’s effectiveness (Janssen et al., 2010).
  - *Reputation/Observation*: Punishment works far better if actions are visible or can be tracked (Rockenbach & Milinski, 2006; Sigmund et al., 2010; Hilbe & Traulsen, 2012; Sigmund et al., 2001).
  - *Second-order free-riders*: If not sanctioned, punishment institutions can be unstable, weak, or even reduce efficiency (Perc, 2012).

- **Pool (institutional) vs. Peer punishment:**
  - Pool punishment (pre-committed, institutional) is more stable but often less efficient due to ongoing costs (Sigmund et al., 2010; Bodnar & Salathé, 2012).
  - Peer punishment can be more efficient where reputation or direct observation is feasible, but is less robust in the face of free-riding on punishment.

- **Important boundary conditions:**
  - *Voluntary participation*: Permitting players to opt out dramatically alters the effect and efficiency of punishment; with opt-out, even weak punishment can support full efficiency (Hauert et al., 2007; Sasaki et al., 2012).
  - *Group size*: Larger groups pose challenges, but theory and some field data suggest that with sufficient coordination or scaling, punishment can support high efficiency (Eriksson & Strimling, 2012; Boyd et al., 2010; Mathew & Boyd, 2011).
  - *Mutation/strategy diffusion*: Theoretical results indicate long-run efficiency gains from punishment heavily depend on details of behavioral exploration (García & Traulsen, 2012).

- **Punishment does not always improve efficiency, and may reduce it:**
  - Cases with vendettas/retaliation or high antisocial punishment (Fehl et al., 2012; Herrmann et al., 2008).
  - When punishment is used unproductively, or when costs exceed the added cooperation (Dreber et al., 2008; Janssen et al., 2010; Ohtsuki et al., 2009; Sigmund et al., 2010).

**Conflict/Ambiguity:**
- Some environments show a strong positive net effect, others show zero or negative effect, emphasizing contextual moderators: social/cultural norms, structure of punishment (cost/impact/severity), and the opportunity for reputation or observation.

# 5) Prediction Guidance

**For the downstream prediction task (efficiency with punishment enabled given design and control efficiency):**

- **Control efficiency is a necessary but not sufficient predictor:**  
  - Papers show that punishment tends to have the greatest positive effect where baseline efficiency (without punishment) is low (Gürerk et al., 2006; Eriksson & Strimling, 2012); where control efficiency is already high, additional gains may be limited, and costs of punishment can even reduce efficiency.

- **Specific design dimensions that *directly* moderate the effect (see Section 6 below):**  
  - *Punishment cost, magnitude, tech*: Lower cost and higher impact per unit favor positive efficiency effects, but too high a punishment can destabilize cooperation.
  - *Reputation/observability*: If punishers or actions are seen, positive effects are greatly amplified.
  - *Availability of reward, communication, institution choice*, *voluntary participation*, and *second-order punishment* all act as key moderators.

- **Behavioral outcome increases (contribution/cooperation) often *translate* to efficiency only if punishment usage is modest and well-targeted:**  
  - When punishment is frequent, misdirected, or escalated (vendetta cycles, antisocial punishment), net efficiency gains are low or negative (Fehl et al., 2012; Herrmann et al., 2008).

- **Empirical range of efficiency boost:**  
  - In canonical lab PGGs, enabling punishment increases group efficiency from *low/moderate* to *high*—~10–20% up to ~90–95% of maximum in favorable settings (Fehr & Gächter, 2002; Gürerk et al., 2006; Rockenbach & Milinski, 2006).
  - In less favorable or field/complex contexts, or with antisocial punishment, the efficiency gains may be negligible or negative.

- **Negative or null effects are not rare:**  
  - Dyadic repeated games with punishment (Prisoner’s Dilemma): efficiency gains are minimal/negative because punishment cost cancels cooperative gains (Dreber et al., 2008).
  - Field/CPR settings: punishment can reduce efficiency if not paired with communication or proper institutional features (Janssen et al., 2010).

- **Key caveat:**  
  - Because many studies aggregate over designs with very specific parameters (group size, rounds, cost/impact of punishment, anonymity, ability to communicate), care must be taken in extrapolating to new designs outside the empirically tested set.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed (multiple, direct empirical/theoretical links):**
- `player_count` (group size): Strong empirical and theoretical coverage.  
- `num_rounds` (game repetition): Well-studied; longer/shorter games affect cooperation/punishment dynamics.  
- `mpcr` (marginal per-capita return): Key parameter; strong evidence on its impact in both control and treatment.  
- `punishment_cost`/`punishment_magnitude`/`punishment_tech`: Directly manipulated in many lab experiments and theory papers.  
- `reward_exists`, `reward_cost`, `reward_tech`: Covered, especially in comparison to punishment (several lab studies and modeling papers).  
- `chat` (communication): Some studies explicitly enable/disable communication and show its strong moderating role on efficiency gains from punishment.

**Indirectly informed (meaningful discussion, but less direct evidence):**
- `all_or_nothing` (discrete vs. continuous contribution): Some coverage, but most standard studies use continuous contributions.
- `show_other_summaries` (visibility of others' payoffs): Theoretical and some empirical support (Rockenbach & Milinski, 2006).
- `show_punishment_id` (anonymity/identifiability): Direct manipulation is less frequent, but the importance of (non-)anonymity is repeatedly highlighted in theory.
- `show_n_rounds` (knowledge of game length): Occasional coverage, typically in behavioral framing.

**Contextually discussed or only occasionally mentioned:**
- `default_contrib` (opt-in/opt-out framing): Discussed much less.
- `num_rounds` and `player_count`: Empirical range is constrained—most lab games use small groups and moderate round lengths.

**Sparse or effectively missing:**
- Effects of `default_contrib`, `all_or_nothing` (except in some theory papers), or more granular feedback/summary mechanisms are only weakly covered.
- Realistic field manipulation of `chat`, `show_punishment_id`, or complex feedback structures is rare.

**Other dimensions (not in prediction list but function as critical moderators):**
- *Voluntary participation* (opt-out): Strong theoretical and some empirical support as a powerful moderator (Hauert et al., 2007; Sasaki et al., 2012).
- *Second-order punishment* and institutional stability are key for pool punishment cases.

# 7) Important Limitations

- **Lack of comprehensive coverage for all prediction dimensions:**  
  - Some design parameters (such as anonymity, opt-in/out, complex feedback, and punishment ID) are underexplored. Generalization to these cases may be uncertain.

- **Payoff-behavior distinction:**  
  - Many studies report only on *contribution* or *punishment frequency/severity/targeting*, not efficiency. Where efficiency is not measured, inferences require caution.

- **Context and population effects:**  
  - Field experiments and inter-cultural studies (e.g., Herrmann et al., 2008; Henrich et al., 2006) show that punishment's effect on efficiency is highly context-dependent (e.g., prevalence of antisocial punishment, cultural norms). Lab findings often generalize poorly outside homogeneous or Western samples.

- **Dynamics of punishment usage:**  
  - Costs, vendettas, and misuse of punishment can drive efficiency down, even as cooperation increases. Prediction models should not assume monotonicity between contribution and efficiency.

- **Complex institutional designs underrepresented:**  
  - While theoretical modeling is rich, empirical work is concentrated on standard lab PGGs. Complex, endogenous, or multi-level sanctioning regimes and networked environments are less extensively tested.

- **Adjacency and non-equivalence of some evidence:**  
  - Adjacent evidence (Prisoner's Dilemma, trust games, exclusion/ostracism) is only partly transferable; the underlying social dilemma’s structure and payoff externalities can differ subtly but importantly.

- **Evolutionary and long-run stability results depend on modeling choices:**  
  - Mutation structure, stability of equilibria, and initial condition dependence are highlighted as critical in theory, but less so in lab or field studies.

- **Reporting bias toward positive effects:**  
  - Some influential negative results (e.g., punishment not improving, or reducing, efficiency) are in field/realistic settings, but the overall literature may overrepresent positive findings from tightly controlled lab contexts.

---

**In sum:** The evidence base provides strong, but far from universal, support for the hypothesis that enabling peer punishment in PGG-like environments generally increases efficiency relative to control, especially when initial cooperation is low and design parameters are favorable (low punishment cost, high impact, visible actions, moderate group size). The size, stability, and universality of this effect are, however, *moderated* by numerous institutional, social, behavioral, and structural factors—many of which are directly mapped to design dimensions in standard lab studies but less so in complex, large-group, or unorthodox settings. Many dimensions remain weakly informed or even absent in the literature, and caution is warranted in extrapolating outside well-studied contexts.
