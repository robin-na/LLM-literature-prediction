# 1) Evidence Base

This paper set consists entirely of theoretical work (91 papers; all analytical, simulation, or agent-based models, with no direct experimental or empirical field data). The literature is wide in conceptual scope—covering classic public goods games (PGGs), many variants, and a range of related social dilemma models—but is almost exclusively theoretical, with very limited direct measurement of efficiency as defined for prediction (the ratio of realized group payoff to the full-cooperation benchmark). Most papers analyze or simulate payoff-based outcomes, with a strong focus on underlying mechanisms. There is not a rich supply of experimental effect sizes or direct treatment-versus-control empirical contrasts; instead, the set provides mechanism-based predictions and parametric/qualitative results. Overall, the evidence base provides a broad but theory-driven foundation for the prediction task, with extensive exploration of parameter spaces but relatively less direct, quantitative payoff data from peer punishment interventions in controlled PGGs.

# 2) Task Relevance

**pgg_or_variant:**
- *exact* relevance: Most papers analyze standard PGGs or repeated n-person prisoner’s dilemmas with the same underlying incentive structure. Many others analyze adjacent or structurally similar collective action/resource games (e.g., common-pool resource dilemmas, threshold/linear production variants).
- *close/adjacent*: Numerous papers focus on iterated dyadic dilemmas, common-pool or mutualism models, or games with optional participation, reputation, and other modifications.

**punishment_or_sanctions:**
- *exact*: Many papers model peer or institutional punishment as a formal game dimension, varying cost, severity, or method of implementation.
- *close/adjacent*: Some focus on “soft” forms of punishment (ostracism, gossip, withholding cooperation) or on settings where punishment is part of a broader enforcement environment (including reward, exclusion, corruption, or second-order sanctions).

**efficiency_or_related_payoff_outcome:**
- *exact*: Roughly half of the PGG-focused papers define and report group efficiency or mean fitness/payoff directly.
- *close/adjacent*: Many more report contribution/cooperation rates, norm compliance, or the prevalence of pay-off-maximizing strategies, allowing for indirect inference about efficiency.
- *weak/none*: Behavioral outcome focus (not mapped to payoffs), purely conceptual or biological reviews, or models centered on norm psychology, partner choice, or reputation without direct measurement or calculation of efficiency.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (direct evidence):**
    - Group efficiency: Explicit calculation as a fraction of the full-cooperation payoff is performed in many theory papers (e.g., Dong et al., 2019; Jiao et al., 2020; Eldakar et al., 2007; Oya & Ohtsuki, 2017; Dercole et al., 2013).
    - Total group payoff, welfare, mean fitness, or surplus: Numerous models provide these results analytically or via simulation, frequently as main model outputs.
    - Group-level resource management (in resource game variants): Efficiency analogs based on sustainable yield or resource maintenance.

- **Related but non-payoff (behavioral) outcomes:**
    - Contribution or cooperation rates: Extremely common, often serving as a proxy for efficiency, though not equivalent.
    - Frequency of punishers, defectors, or strategy prevalence.
    - Norm compliance, adoption rate of enforcement, partner selection or exclusion frequencies.
    - Existence and stability of cooperative equilibria (not always mapped to efficiency).

- **Not measured or only contextually discussed:**
    - Empirical effect sizes comparing treatment (punishment-enabled) versus control (punishment-disabled) efficiency in human groups are largely absent.

# 4) Main Findings Relevant To Prediction

- **Punishment tends to increase efficiency when:**
    - Punishment is effective (high impact per unit cost) and not prohibitively costly (Okada & Bingham, 2008; Dercole et al., 2013; Eldakar et al., 2007).
    - The population or group is spatially structured (allowing for clustering of punishers and cooperators) (Oya & Ohtsuki, 2017; Nakamaru & Dieckmann, 2009; POLLOCK, 1988; Roos et al., 2014).
    - The control efficiency (no punishment) is low due to free-riding, and added punishment discourages defection (Baker & Rachlin, 2002; Dercole et al., 2013).
    - Punishment is probabilistic or rare but severe: infrequent, strong punishment can be more cost-efficient and lead to higher efficiency than continuous, mild punishment (Deng et al., 2012; Jiao et al., 2020).
    - There are supporting mechanisms, such as reputation or second-order reward for punishers, aligning individual and group interests (Milinski & Rockenbach, 2012; Podder et al., 2021; Kendal et al., 2006; Okada et al., 2015).

- **Punishment may fail to increase efficiency or can even reduce it when:**
    - Punishment is costly relative to its effect, or costs are shared by few individuals (“second-order free rider” problem) (Dong et al., 2019; Powers et al., 2012; Vukov et al., 2013).
    - Population is well-mixed with random matching (no structure), so punishment does not persist and does not sustain cooperation (Oya & Ohtsuki, 2017; Nakamaru & Dieckmann, 2009).
    - Anti-social punishment (punishment of cooperators) is present, causing efficiency to drop (Powers et al., 2012; Podder et al., 2021).
    - Institutions are corrupt or enforcer honesty is low (Lee et al., 2015; Lee et al., 2017; Huang et al., 2018).
    - The punishment mechanism triggers additional maladaptive behaviors, including excessive retaliation (Phillips, 2018; Powers & Lehmann, 2017; Dong et al., 2019).
    - Insurance against punishment is available at a lower cost than the expected fine, subverting deterrence and lowering efficiency (Zhang et al., 2013).
    - The environment is subject to resource scarcity, high variability, or ecological parameters undermining cooperation (Nhim et al., 2019; Safarzynska, 2013).

- **Effect is highly conditional:**
    - The impact of enabling punishment depends, sometimes non-monotonically, on group size (player_count), marginal per-capita return (mpcr), punishment cost, spatial structure, the possibility of cooperation via alternative means (e.g., reputation, partner choice), and institutional design (Deng et al., 2012; Dercole et al., 2013; Dong et al., 2019).
    - Bistability is common (Lee et al., 2015; Lee et al., 2017): both high- and low-efficiency equilibria can exist depending on initial conditions and institutional integrity.

- **Insightful mechanistic results:**
    - Shared (pool) punishment can achieve high efficiency under more realistic cost-sharing conditions (Dercole et al., 2013).
    - Graduated punishment (fine increases with harm or repeated defection) maximizes efficiency in heterogeneous populations (Iwasa & Lee, 2013; Couto et al., 2020).
    - Effectiveness of punishment is enhanced if combined with reputation or transparency (Milinski & Rockenbach, 2012; Lee et al., 2015).

# 5) Prediction Guidance

- **Most relevant design dimensions for predicting the effect of punishment on efficiency:**
    - *player_count*: Small groups favor effective punishment and higher efficiency; large groups dilute effectiveness unless institutions are present.
    - *num_rounds*: More rounds allow punishment’s deterrent effect to accumulate, supporting long-run efficiency gains.
    - *mpcr*: Higher mpcr (greater benefit from cooperation) makes efficiency gains from punishment more likely and larger.
    - *punishment_cost/punishment_tech*: Efficiency benefits require that punishment is not excessively costly relative to its impact.
    - *population structure (implicit in spatial/structured models)*: Punishment is most effective in locally-structured or networked populations.
    - *presence of supporting mechanisms*: Reputation, meta-incentives, transparency, and honesty of enforcers strongly moderate outcomes.

- **When making efficiency predictions using control efficiency and game design:**
    - If control efficiency is already high (close to 1), enabling punishment may not increase efficiency unless the mechanism specifically reduces punishment frequency or cost (e.g., reputation-based “sticks”).
    - If control efficiency is low, adding peer punishment is expected to increase efficiency only if punishment is impactful and affordable, group size is moderate, and there are no overriding negative effects (e.g., anti-social punishment, corruption, insurance loopholes).
    - If the design allows for rare but severe punishment or probabilistic execution, a substantial efficiency improvement is more likely than with constant, always-on punishment.
    - When institutional features reduce the burden or risk of anti-social punishment/corruption (e.g., honest enforcement, identification/transparency), efficiency gains are robust.

- **Caveats:**
    - The literature shows that punishment mechanisms can be fragile, easily undermined by population mixing, corruption, anti-social punishment, or poor cost structure.
    - Second-order problems (who punishes the non-punishers) are important—if these are not resolved, predicted efficiency gains may fail to materialize.
    - Mechanistic and context-dependent moderators are critical: simple main effects or monotonic predictions are rarely justified.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed (detailed modeling or results):**
- `player_count`: Frequently modeled; effects on punishment efficacy and efficiency are often non-linear.
- `num_rounds`: Key in repeated games; directly modeled in most analytical and simulation work.
- `mpcr`: Central design parameter, with explicit analysis in almost all main theory papers.
- `punishment_cost`, `punishment_tech`: Central variables; extensive parameter sweeps and sensitivity analyses.

**Indirectly informed (occasionally included or discussed, but less central):**
- `all_or_nothing`: Modeled in many, but not all, papers; relevant where binary contribution is assumed.
- `show_punishment_id`, `show_other_summaries`: Sometimes included via “transparency” or reputation mechanisms, but often not focal.
- `reward_exists`, `reward_cost`, `reward_tech`: Covered in several key comparative theory papers (e.g., Dong et al., 2019; Kendal et al., 2006), but less pervasively than punishment.
- `chat`: Seldom modeled directly, but some papers analyze communication or indirect information flow.

**Only contextually discussed or sporadically included:**
- `default_contrib`: Rarely, if ever, manipulated as a design variable.
- `show_n_rounds`: Sometimes modeled as information treatments, but effect on efficiency is rarely the main focus.
- `punishment_magnitude`: Usually incorporated implicitly in punishment “efficacy,” but often not separately from “punishment cost.”
- Other experimental visibility variables (e.g., real-time feedback, identity revelation, etc.) are mentioned occasionally but not treated systematically.

**Effectively missing or unstructured:**
- For most papers, experimental implementation details (e.g., exact framing, interface, communication protocols) are not modeled, and there is little direct evidence or systematic analysis of their effects on efficiency outcomes.

# 7) Important Limitations

- **Theoretical bias**: All findings derive from theoretical models (many evolutionary, some simulation-based); no empirical estimates, effect sizes, or data from experiments or field studies are included in this set.
- **Efficiency sometimes inferred rather than directly calculated**: A sizeable portion of the literature focuses on behavioral or strategic outcomes, requiring inference rather than direct measurement of group efficiency.
- **Assumptions and scope conditions are critical**: Many results depend heavily on parameter choices, model structure (e.g., spatial vs. well-mixed, presence/absence of anti-social punishment), and theoretical assumptions (e.g., infinite vs. finite populations, information structure).
- **Empirical unknowns**: Lack of experimental manipulation and real-world data limits external validity and generalizability; effects seen in idealized models may not hold in realistic or lab settings.
- **Design dimensions not systematically covered**: Some prediction dimensions, especially those related to interface, framing, or experimental procedures, receive little or no theoretical attention, leaving important moderators unaddressed.
- **Positive and negative effects both possible**: Literature reveals that enabling punishment can both help and harm efficiency depending on cost structures, enforcement integrity, and the possible presence of corruption, anti-social punishment, or other countervailing mechanisms.
- **No directly measured treatment-control contrasts**: The majority of insights are mechanistic, focusing on underlying conditions for cooperation rather than on quantitative treatment effect predictions for efficiency in PGGs with versus without punishment.

---

**In sum:**  
The literature strongly supports the expectation that the efficiency impact of enabling punishment in PGG-like environments is highly moderated by core design dimensions (group size, rounds, return structure, punishment cost/tech, population structure, and institutional context). Efficiency gains are most likely when punishment is both effective and not excessively costly, anti-social punishment and corruption are absent, group size is moderate, and supporting mechanisms (e.g., reputation) are present. However, in many plausible parameter regimes and institutional contexts, punishment may yield little to no efficiency gain or may even reduce efficiency. Thus, predictions should always be conditioned on these moderators, and uncertainty should be preserved where the literature shows disagreement or where core moderators are not well specified by the game design.
