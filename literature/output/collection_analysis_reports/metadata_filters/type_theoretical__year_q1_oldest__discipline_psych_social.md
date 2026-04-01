# 1) Evidence Base

The paper set is comprised entirely of theoretical and simulation-based works; none are empirical or report results from laboratory or field experiments. The set is broad in its coverage of concepts related to cooperation, punishment/sanctioning, and group coordination, but only a subset offer direct, detailed modeling of public goods game (PGG) or very close variants. Most papers model payoff-based outcomes, but actual reporting of efficiency (defined as group payoff relative to the social optimum) is less common, with many papers focusing instead on cooperation rates, compliance, or the behavioral mechanisms underlying punishment effects.

Despite this, the literature is rich in arguments, comparative statics, and mathematical derivations exploring how design dimensions (e.g., group size, monitoring, punishment cost/technology) and psychological or institutional moderators influence equilibrium outcomes. The evidence base is much stronger on theoretical sufficiency and mechanism than on empirical effect sizes or quantitative forecasts.

**Summary:**  
- All theory/simulation papers  
- Broad in scope, but with a strong cluster around classic and close PGG/CPR (commons) dilemmas  
- Many payoff-based analyses, but direct reporting of efficiency is sporadic  
- Rich modeling of game parameters and mechanisms, but lacking real-world evidence

# 2) Task Relevance

### pgg_or_variant
- **exact relevance:** Many papers model the standard PGG or n-person social dilemma directly (e.g., Ye et al., 2011; Fehr & Gintis, 2007; Gintis, 2003; Boyd & Richerson, 1992).
- **close relevance:** Many others use related models—repeated Prisoner’s Dilemma, partnership games, common-pool resource (CPR) games, or spatial/structured variants (e.g., Tarui et al., 2008; Noailly et al., 2009).
- **adjacent or weaker:** A subset is adjacent (ultimatum games, trust games, or conflict/contest models), contributing more indirectly.

### punishment_or_sanctions
- **exact relevance:** Most directly analyze peer punishment or sanctioning systems as in experimental PGGs, covering both individual and group-administered punishment (e.g., MACY, 1993; Bednar, 2006).
- **close to adjacent:** Some model punishment-like mechanisms (expulsions, metanorms, reputation, or group-level sanctions).
- **weak/none:** Several focus on mechanisms (e.g., reputation) without explicit costly punishment, offering only indirect support.

### efficiency_or_related_payoff_outcome
- **exact relevance:** Several report efficiency (group payoff relative to optimum), welfare, or closely related measures (Fehr & Gintis, 2007; Bednar, 2006; Tarui et al., 2008).
- **close relevance:** Many infer effects on group payoff or welfare from modeled payoffs or equilibria (e.g., Heller & Sieberg, 2010; Macy, 1993).
- **adjacent/weak:** A large bloc focuses on non-payoff behavioral outcomes (contribution rate, defection, norm enforcement) or on mechanism/process without direct link to efficiency.

# 3) Outcomes Measured In The Literature

### Payoff-related outcomes (directly tied to efficiency)
- **Exact:** Efficiency (ratio of actual/maximum payoff), group payoff, total group earnings, welfare, surplus (e.g., Ye et al., 2011; Bednar, 2006; Tarui et al., 2008; Evans & Thomas, 2001).
- **Close:** Total payoff or average earnings per player, average group welfare, frequency of efficient (cooperative) equilibria, explicit mathematical conditions/formulas for optimality.

### Non-payoff behavioral outcomes
- Contribution rates, fraction of cooperators/punishers, norm compliance, prevalence of punishing behavior, transitions between equilibria, existence of stable/unstable compliance, emotional/motivational responses, strength of reciprocity or group selection.
- These are important for understanding *mechanisms* but are not direct measures of efficiency as required for the prediction task.

### Cross-cutting
- Many papers are careful to note that increased cooperation does not always correspond to increased efficiency: punishment may lead to higher contributions but also destroy resources (e.g., Guala, 2012), making net effects on welfare/efficiency ambiguous or negative in some conditions.

# 4) Main Findings Relevant To Prediction

Synthesizing across relevant papers:

- **Punishment often (but not universally) increases efficiency in standard PGGs:**  
  The dominant result from classic theoretical models is that peer punishment reliably transforms low-efficiency, free-riding equilibria into high-efficiency, cooperative equilibria—*provided* the punishment is effective and not prohibitively costly (Fehr & Gintis, 2007; Gintis, 2003; Macy, 1993; Boyd & Richerson, 1992; BOYD & RICHERSON, 1992; Cai & Kock, 2009).

- **Context and mechanisms moderate the effect:**  
  - **Cost/benefit of punishment matters:** If punishment is too costly or ineffective, it can reduce efficiency or fail to sustain cooperation (Ye et al., 2011; Guala, 2012; Heller & Sieberg, 2008).
  - **Punisher compensation** (e.g., 'sympathy' transfers) can be necessary for positive efficiency effects (Ye et al., 2011).
  - **Antisocial punishment, misapplied punishment, or high error rates** can twist punishment into a negative-sum game—raising costs without enough gain to offset (Guala, 2012; Shinada & Yamagishi, 2008).
  - **Imperfect monitoring:** Efficiency gains are incomplete if monitoring is noisy (Bednar, 2006; ABREU et al., 1991; Nakao, 2009); perfect or highly informative monitoring increases allowable parameter space for cooperation.
  - **Game structure and horizon:** Longer or indefinite repetition (high discount factors, large expected number of rounds) allow punishment’s threat to stabilize efficient equilibria (“grim trigger” stability; Corriveau, 2012; Evans & Thomas, 2001; Jones, 1999).
  - **Group size:** Moderate group sizes—large enough for the public good effect but not so large that monitoring/punishment becomes infeasible—are most conducive to positive efficiency gains (BOYD & RICHERSON, 1992; Dubreuil, 2008); very large groups can dilute the effect (Dubreuil, 2008; Kritikos & Bolle, 2004).
  - **Network structure:** Local punishment and population structure (segmentation, repeat partners) can amplify the effect by making enforcement more credible and avoiding diffusion of responsibility (Noailly et al., 2009; POLLOCK, 1988).

- **Comparative statics:**  
  The *magnitude* of the efficiency gain from enabling punishment is largest:
  - When control efficiency is low (everyone defects in control)
  - When punishment is cheap/effective (high fine-to-fee ratio)
  - When group members can target defectors reliably and avoid antisocial punishment
  - When the MPCR (marginal per-capita return) is high
  - When the punishment mechanism produces few errors or misassignments

- **Ambiguity and mixed effects:**  
  - In some parameter regions (costly punishment, low MPCR, high error), punishment reduces efficiency—even if cooperation rates rise (Guala, 2012; Shinada & Yamagishi, 2008).
  - Multiple stable equilibria are possible: in some simulations, both high and low efficiency can be sustained based on initial conditions (Whitmeyer, 2004).
  - Empirical regularities highlight the need for moderators such as communication, reputation, monitoring, and compensation for punishers.

# 5) Prediction Guidance

**Overall:**  
The theoretical literature provides strong support for a *positive average effect* of enabling peer punishment on efficiency in public-goods-game-like environments—*if* punishment is not too costly, can be targeted effectively, and the environment supports cooperation through repetition or institution-building.

**Key dimension-level guidance:**
- **Control efficiency predicts ceiling:** The magnitude of efficiency gain depends on the gap between current (control) efficiency and the maximum supported by game structure.
- **player_count:** Efficiency gains from punishment decrease in very large groups unless enforcement mechanisms are appropriately institutionalized (Dubreuil, 2008; Kritikos & Bolle, 2004).
- **num_rounds / game horizon:** Longer games or higher discount factors make efficiency gains from punishment more likely and larger (Corriveau, 2012; Evans & Thomas, 2001).
- **mpcr:** Higher MPCR strengthens the effect of punishment by increasing the relative return to cooperation (Shinada & Yamagishi, 2008; BOYD & RICHERSON, 1992).
- **punishment_cost/punishment_tech:** Low or moderate cost and high effectiveness (“fine-to-fee ratio”) are crucial—if punishment is expensive or ineffective, efficiency may fall (Ye et al., 2011; Guala, 2012; Heller & Sieberg, 2008).
- **reward/compensation mechanisms:** The presence of mechanisms to compensate punishers (sympathy, rewards) can make punishment self-sustaining and efficient (Ye et al., 2011).
- **information/monitoring:** High-quality monitoring/feedback is required—imperfect information limits efficiency gains from punishment (Bednar, 2006; Nakao, 2009; ABREU et al., 1991).
- **social structure:** Local punishment, reputation, repeated matchings, and network structure all enhance punishment's effectiveness.
- **Mistargeted/antisocial punishment:** Can erode efficiency gains, and papers highlight the need to limit or mitigate (Brandts & Fatas, 2012).

**When using this literature to inform predictions:**
- Expect significant efficiency gains from enabling punishment when punishment is effective, affordable, and the baseline is low.
- Be cautious predicting positive effects when punishment is costly, monitoring is poor, or antisocial punishment is likely.
- Fine-tune predictions based on game design parameters, with attention to cost/effectiveness and feedback/monitoring design; control efficiency is a strong anchor point.

# 6) Design Dimensions Highlighted Across Papers

## **Directly Informed:**
- `player_count`: Frequently modeled; group size effects feature prominently.
- `num_rounds`: Repetition/horizon is fundamental in sustaining cooperation through punishment.
- `mpcr`: Systematically analyzed as it impacts incentives to cooperate/defect.
- `punishment_cost` / `punishment_tech`: Core parameters—findings are often conditional on these.
- `reward_exists` / `reward_cost`: Addressed as moderators (especially compensation for punishers).
- `all_or_nothing`: Modeled in some, particularly in binary/reciprocity analyses.
- `show_n_rounds`, `show_other_summaries`: Studied in monitoring/information papers.

## **Indirectly Informed:**
- `chat`: Discussed as enhancing cooperation and possibly moderating punishment's effect; less systematically modeled.
- `default_contrib`: Addressed in passing as framing may influence baseline cooperation but not core to theoretical models.
- `reward_tech`: Sometimes modeled in environments with combined reward/punishment schemes.

## **Only Contextually Discussed:**
- `show_punishment_id`: Raised in discussions of antisocial punishment, but rarely modeled explicitly.
- `show_n_rounds`, `show_other_summaries`: Quality/timing of information addressed, but often subsumed under imperfect monitoring.

## **Effectively Missing:**
- Details of experimental interface design (e.g., specific summary statistics, feedback screens) are generally absent.
- Nuanced reward structures (e.g., continuous vs discrete) and subtle framing effects are largely omitted or only discussed in mechanism terms.

# 7) Important Limitations

- **No direct empirical evidence:** All findings are theoretical or simulation-based; no laboratory or field data for calibration or out-of-sample validation.
- **Efficiency often inferred, not measured:** Many papers extrapolate from contributions or compliance to efficiency, which can be misleading when punishment is costly.
- **Potential for overgeneralization:** Models tend to focus on the necessary conditions for sustainability but may not address magnitude or noise in real groups.
- **Parameter sensitivity and boundary effects:** Positive efficiency effects from punishment depend critically on cost/effectiveness, group size, error rates, and compensation; broad results often collapse under small deviations from ideal configurations.
- **Neglect of antisocial punishment and error-prone environments:** Some papers explicitly highlight, but others neglect, scenarios where punishment backfires (antisocial, misapplied, excessive).
- **Ambiguity in multiple equilibria:** Several models exhibit multiple stable equilibria; realized outcomes may depend on initial conditions, group histories, or rare stochastic shocks.
- **Sparse treatment of some design dimensions:** Communication, punishment identity visibility, and reward schemes are modeled in only a few cases; interaction effects are not fully explored.

---

**In summary:**  
The theoretical literature provides strong mechanism-based support for the hypothesis that enabling peer punishment in public-goods-game-like environments generally increases efficiency—conditional on punishment not being prohibitively costly, monitoring being effective, and the group not being too large or fragmented. The net efficiency impact depends on the interplay of cost/effectiveness of punishment, quality of monitoring, and compensation mechanisms. Direct dimension-specific predictions are best informed for group size, game length, MPCR, and punishment parameters. However, the absence of direct empirical validation and the sometimes fragile dependence of results on key parameters warrant caution and sensitivity analysis in downstream prediction tasks.
