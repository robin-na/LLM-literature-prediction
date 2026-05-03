# Evidence Base

This paper set comprises 57 studies with a majority being theoretical models and simulations (about two-thirds), and the remainder being experimental or observational (lab, field, or agent-based). The majority of the empirical studies are lab-based, with only a few large-scale or field settings. The set is broad in its coverage of social dilemmas and the evolution of cooperation, but relatively narrow in direct empirical evidence on **efficiency** outcomes—the key target for the prediction task.

The strongest, most directly relevant evidence comes from theoretical modeling of public goods games (PGGs) with punishment, covering peer, pool (institutional), tax-based, exclusion, and hybrid mechanisms. Several simulation and theory papers provide explicit or near-explicit mapping from game design dimensions and control outcomes to efficiency with punishment enabled. However, **empirical studies typically focus on behavioral outcomes (contributions, cooperation, punishment frequency), not on efficiency or group payoff.** Meta-analyses and reviews further emphasize behavioral outcomes rather than efficiency.

Overall, the evidence base is **theory-heavy, with limited direct empirical evidence** on the specific relationship between punishment and efficiency in repeated, multi-player PGGs.

# Task Relevance

**pgg_or_variant**:  
- **exact:** Most theory papers and some empirical papers study either standard PGGs or close variants (spatial, networked, tax-based, group size, and rounds are specified).
- **adjacent/close:** Some papers focus on related dilemmas (Prisoner’s Dilemma, donation games, innovation games), or real-world analogs (pollution, PPP projects, small-scale societies).  
- **none:** A few papers study concepts only tangentially related to PGG (e.g., norm psychology, general review of prosocial behavior).

**punishment_or_sanctions**:  
- **exact:** The majority directly model or experimentally enable punishment as a treatment variable (peer, pool, tax-based, third-party, exclusion, etc.).
- **close/adjacent:** Some include only reward mechanisms or focus on indirect strategies (exclusion, shunning).
- **none:** Several have no punishment or sanction treatment (reputation-only mechanisms).

**efficiency_or_related_payoff_outcome**:  
- **exact:** A subset of theory/simulation papers provides explicit efficiency or normalized group payoff outcomes.
- **close:** Many report average payoff, group welfare, or closely related metrics, which can often be inferred as efficiency.
- **adjacent/weak:** The bulk of empirical studies measure only **behavioral** outcomes (contribution rate, cooperation density), not efficiency or group payoff.

**Synthesis**: For prediction of **treatment efficiency** from design dimensions and control efficiency in PGGs, evidence is strongest from recent theory/simulation work and weakest from experiments (which rarely report efficiency or treatment-control payoff differences).

# Outcomes Measured In The Literature

- **Directly Measured Efficiency/Payoff Outcomes**:  
  - Several theory and simulation papers explicitly compute total group payoff, welfare, efficiency (ratio to full cooperation), or mean group payoffs. These papers often report how efficiency depends on design variables (e.g., MPCR, punishment cost).
- **Related Payoff Outcomes**:  
  - Many works report average payoff per strategy (cooperators, defectors, punishers/excluders), or the difference in payoffs between cooperators and defectors (as a mechanism for the evolution of cooperation).
- **Behavioral Outcomes (NOT efficiency)**:  
  - The overwhelming majority of empirical (especially experimental) studies report **contribution rate, cooperation density, frequency/persistence of punishment, norm compliance, trust, etc.**, rather than efficiency or normalized group payoff metrics.
  - Several meta-analyses and reviews aggregate results on behavioral cooperation, not efficiency.

**Note:** A recurring limitation is that increased cooperation due to punishment does not always translate into higher efficiency, especially when punishment is costly or misapplied.

# Main Findings Relevant To Prediction

## Empirical Findings

- **Punishment increases cooperation**, contribution rates, and norm compliance in both exact PGGs and analog games, across cultures and age groups. This is very robust and well-supported (Zhou et al., 2023; Spadaro et al., 2022; Capraro, 2024; Frey & Burgess, 2023).

- **Effect on efficiency is rarely directly measured in experiments.** When measured in theory/simulation, enabling punishment typically increases efficiency, **but only if punishment is cost-effective, well-targeted, and not excessive** (Li et al., 2022; Wang, C.Q. et al., 2024; Wang, S.X. et al., 2022; Wang, X.J. et al., 2024; Wang, X.F. & Perc, 2022).

- **Exceptions and boundary conditions:**
    - Inefficient or overly costly punishment, or noisy application (mistakenly punishing cooperators), can reduce efficiency below control, even as it increases cooperation (Wu et al., 2022; Han et al., 2024).
    - Reward mechanisms are sometimes *more* efficient than punishment for maintaining cooperation, especially in noisy/institutional contexts (Sun, Z.B. et al., 2023; Han et al., 2024).
    - Cultural and social context modulate both the use of punishment and its normative effects, but empirical payoff differences are rarely quantified (Zhou et al., 2023).
    - Institutional (pool) punishment advantages are more visible in structured or networked populations than in well-mixed ones (Wang, C.Q. et al., 2024).

## Theoretical/Mechanism Arguments

- **Efficiency gains from punishment** are generally larger when:
    - **MPCR is high** (returns to cooperation outweigh cost of punishment).
    - **Punishment is just strong enough to deter defection** but not so costly as to drain group resources.
    - **Institutional or tax-based punishment mechanisms** are available (Li et al., 2022; Sun, Z.B. et al., 2023; Shen et al., 2022).
    - **Adaptive, feedback, or probabilistic punishment mechanisms** are used, increasing efficiency by minimizing punishment waste (Ohdaira, 2022; Wang, X.J. et al., 2024).

- **Efficiency gains are weaker or absent when:**
    - **Punishment cost > marginal social benefit** (Han et al., 2024).
    - There is a **high risk of antisocial punishment or punishment of cooperators** (Shen et al., 2022; Wu et al., 2022).
    - **Reward, communication, or strong reputational mechanisms** substitute for punishment in establishing prosociality, and punishment is redundant (Han, 2022; Pal & Hilbe, 2022).

# Prediction Guidance

- **Prediction of treatment efficiency should heavily weight theoretical results**: Use game design variables (especially MPCR, punishment cost and technology, population structure, and institution type) and control efficiency to estimate the increase (or, rarely, decrease) in efficiency with punishment enabled.
    - **Threshold effects** are common: There is often a punishment cost-to-impact ratio or minimum fine (relative to MPCR and group size) required to see efficiency gains (Li et al., 2022; Wang, C.Q. et al., 2024).
    - In **well-mixed, high-noise, or high-cost** environments, punishment may fail to increase efficiency, or even lower it.
    - **Optimal tuning** of punishment (not maximal!) is essential; over-punishing diminishes efficiency even if cooperation rises.
    - **Institutional support** (tax, pool punishment) can improve the cost-effectiveness and thus the efficiency benefit of punishment.

- **If only non-payoff experimental data are available:** Use these as lower-confidence, indirect indicators, and be cautious—higher cooperation does *not* guarantee higher efficiency, especially if punishment is costly or misapplied.

- **Include context variables**: Structured vs. well-mixed population, reward mechanisms, and communication options all moderate the effectiveness of punishment; predictions should adjust accordingly.

# Design Dimensions Highlighted Across Papers

**Directly informed (explicit evidence for effect on efficiency):**
- `player_count` (group size): Frequently varied in theory; affects thresholds for punishment effectiveness.
- `num_rounds`: Modeled in theory; repeated interactions sustain cooperation more robustly with punishment.
- `mpcr`: Central to nearly all theory work; higher MPCR increases positive impact of punishment on efficiency.
- `punishment_cost`, `punishment_tech`: Directly modeled in most theory studies.
- `reward_exists`, `reward_cost`, `reward_tech`: Addressed in hybrid or comparative incentive models.
- `all_or_nothing`: Varied in several models; rarely in experiments.
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Occasionally modeled or mentioned (e.g., reputation, information structure), but little direct effect evidence.

**Indirectly/contextually discussed:**
- `chat`: Discussed mainly as a facilitator of cooperation, rarely as a moderator of punishment’s marginal effect on efficiency.
- `default_contrib`: Very limited discussion (Capraro, 2024), focus is on framing and behavioral inclination more than efficiency.
- `show_punishment_id`: Mechanistically discussed in theory as affecting reputation, but rarely empirically manipulated.

**Sparse or missing:**
- Many dimensions (`default_contrib`, `show_other_summaries`, specifics of identity display, empirical effects of chat) are absent in direct efficiency analyses.

# Important Limitations

- **Empirical studies rarely report efficiency or group payoff**, focusing on behavioral outcomes instead; direct evidence for efficiency effects is almost entirely theoretical or simulation-based.
- **Parameter coverage is incomplete**: Most studies vary a subset of design dimensions; thus, predictive guidance for unstudied dimension combinations is weaker.
- **Contextual limitations:** Much formal modeling assumes infinite or very large populations, well-mixed or simple networks, and rational/strategy replicator dynamics; behavioral realities (error, antisocial punishment, heterogeneity, cultural norms) are under-represented.
- **Ambiguity in mapping cooperation increases to efficiency gains:** Especially in high-cost, noisy, or misapplied punishment regimes, theory and empirical reviews warn that efficiency can decrease even while cooperation increases.
- **Reward and communication as substitutes:** Some findings suggest that enabling communication, reward, or strong reputation systems can render punishment redundant or even inefficient in promoting efficiency.
- **Special contexts:** Some settings (small-scale societies, real-world governance, innovation dilemmas) show punishment functioning differently from lab PGGs; findings may not generalize to standard, controlled experimental PGG conditions.
- **Sparse coverage of joint effects:** Most studies isolate single variables; few address interactions between multiple design features (e.g., chat + peer punishment + reward).

---

**In conclusion:**  
- *Direct, theoretically rigorous predictions of efficiency effects from enabling punishment in PGGs are available for some design variables (group size, MPCR, punishment cost, mechanism type).*
- *Empirical studies typically confirm that punishment increases cooperation/reactive behavior, but do not confidently quantify efficiency gains or losses.*
- *Predictions should be most confident in settings closely matched to those simulated/theorized in the literature. Out-of-sample predictions (combinations of design dimensions not studied) are less reliable.*
- *High punishment cost, antisocial punishment, and lack of targeting/legitimacy can all reduce or reverse efficiency gains, even as cooperation rises. Optimal, context-sensitive, and institutionalized punishment is most reliably beneficial for efficiency, especially when MPCR is high and reward mechanisms are absent or less efficient.*
