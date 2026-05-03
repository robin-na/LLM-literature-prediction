# 1) Evidence Base

The paper set consists of both empirical (experimental) and theoretical papers, but the majority are theory/modeling papers rather than direct empirical studies of public goods games (PGGs). Specifically, only one paper (dos Santos et al., 2014) provides direct experimental evidence related to efficiency and punishment in a reputational context, and one (Güney & Newell, 2013) provides experimental evidence focused on the drivers of punishment, but not efficiency outcomes. The remaining six are theoretical models addressing related social dilemmas, exclusion, social pressure, reputation mechanisms, or evolutionary dynamics, with most presenting analytic or agent-based results rather than empirical data.

In terms of breadth, the corpus is relatively broad in conceptual scope—covering reputation, exclusion, social pressure, partner choice, and network information in social dilemmas—but narrow in empirical grounding for the core prediction task: the efficiency impact of peer punishment in PGG or closely matched environments. There is a greater emphasis on indirect reciprocity, partner selection, exclusion, and psychological/social forms of punishment (e.g., social pressure, exclusionary linkage) rather than the classic peer punishment technology of the standard PGG setting.

# 2) Task Relevance

### `pgg_or_variant`
- **Relevance:** Mostly **adjacent**. None of the papers study classic public goods games with all design features directly matching the prediction task. Some use direct or indirect reciprocity games, ultimatum or exclusion mechanisms, or resource management models—structures similar but not identical to the canonical PGG.

### `punishment_or_sanctions`
- **Relevance:** Varies from **exact** (dos Santos et al., 2014; Larson, 2016; Güney & Newell, 2013) in studying costly or peer/psychological punishment, to **adjacent** for models of social pressure or exclusion (Furuzono et al., 2013; Inaba et al., 2016), or **adjacent** in evolutionary models focused on envious/spiteful strategies (Garay et al., 2014). At least half the set considers punishment or sanctions in a form meaningfully comparable to PGG peer punishment.

### `efficiency_or_related_payoff_outcome`
- **Relevance:** Only two papers report **exact** or **close** outcomes (dos Santos et al., 2014; Inaba et al., 2016; Ghachem, 2016; Garay et al., 2014). The rest primarily address behavior (cooperation rates, norm adherence) or focus on payoff proxies (sustainable yield, total fecundity, or equilibrium welfare), which is **adjacent** to but not identical with the formal efficiency definition (ratio of achieved to maximal group payoff in a PGG).

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:** Efficiency (dos Santos et al., 2014; Inaba et al., 2016; Ghachem, 2016; Garay et al., 2014), group payoff, group surplus, total welfare, maximized sustainable yield (Furuzono et al., 2013 as proxy for group payoff).
- **Non-payoff behavioral outcomes:** Cooperation/contribution rates, norm compliance, frequency or type of punishment administered (Güney & Newell, 2013), patterns of exclusion or partner selection (Inaba et al., 2016; Ghachem, 2016), psychological drivers and fairness perceptions (Güney & Newell, 2013), and reputation or tagging effects (dos Santos et al., 2014; Ghachem, 2016).

It is notable that many theoretical models translate their main predictions into expected equilibrium payoffs or group welfare, but these are not experimental measurements and often hinge on auxiliary assumptions.

# 4) Main Findings Relevant To Prediction

- **Punishment and Efficiency:** 
  - Enabling punishment does **not guarantee an efficiency gain**; efficiency effects are contingent on the context, type of punishment, and cognitive/information environment (dos Santos et al., 2014; Syi, 2014).
  - **Cognitive constraints or disturbances undermine the positive efficiency effect** of punishment or reputation mechanisms, and may even reduce efficiency via antisocial punishment (dos Santos et al., 2014).
  - **Limited network knowledge facilitates higher efficiency** by making punishment more effective; high precision about individual positions undermines the power of punishment (Larson, 2016; theory).
  - **Moderate/justified punishment strategies are more effective** for sustaining cooperation; extreme punishment policies (harsh or lenient) reduce overall effectiveness (Syi, 2014; theory).
  - **Combined internal and external sources of social pressure** (psychological/peer punishment) synergistically foster high efficiency; lacking either source attenuates the effect, and the impact declines with increasing group size (Furuzono et al., 2013; theory).
  - **Exclusionary punishment (linkage)** can maintain high efficiency only if perception errors are low; high error rates undermine efficiency, as do high rates of unjustified exclusion (Inaba et al., 2016; theory).
  - **Tagging and partner choice** via institutionally provided information (like reputation scores) can robustly increase efficiency, especially if tag accuracy is high and institutional errors are low (Ghachem, 2016; theory).
  - **Group-level survival incentives make cooperation and efficiency more stable** relative to punitive (spiteful/envious) strategies. Increasing marginal per-capita return or the importance of group welfare increases the likelihood of efficient outcomes (Garay et al., 2014).

- **Non-Payoff-Related Results:**
  - The psychological drivers of punishment (fairness, intentions) do **not make punishment more likely to increase payoff** (Güney & Newell, 2013).
  - The presence of punishment mechanisms can increase both prosocial and antisocial punishment, and the behavioral outcome is not a simple function of game structure (dos Santos et al., 2014).

# 5) Prediction Guidance

- **Direct prediction using this evidence is limited:** There is only weak empirical evidence for the size or direction of the effect of enabling peer punishment on efficiency in classic PGGs. Most evidence is theoretical or from adjacent settings.
- **Prediction should account for information and error structure:** 
  - When cognitive load, informational disturbance, or high perception error is present, efficiency gains from enabling punishment can be zero or negative (dos Santos et al., 2014; Inaba et al., 2016).
  - In environments with **limited network knowledge** or **strong, multifaceted social pressure**, the efficiency effect of punishment is larger (Larson, 2016; Furuzono et al., 2013).
- **Moderate, justified punishment is likely to help efficiency** more than extreme/harsh or unstructured punishment (Syi, 2014), though this is a theoretical claim.
- **Group size and marginal per-capita return (MPCR) moderate the effect**: Larger groups dilute the force of peer pressure/punishment (Furuzono et al., 2013), and higher MPCR makes group-focused, efficient strategies more stable (Garay et al., 2014).
- The **presence of accurate institutional information/reputation mechanisms** (even if not classic punishment per se) increases the achievable efficiency (Ghachem, 2016).
- **Control group efficiency is an important prior:** Where control (no-punishment) efficiency is already high, the marginal gain from adding punishment might be small, especially if antisocial punishment is likely or if the main driver is stronger group incentives rather than individual-level punishment.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions:**
- `player_count`: Addressed both theoretically and empirically (dos Santos et al., 2014; Inaba et al., 2016; Garay et al., 2014; Furuzono et al., 2013), with findings that larger groups may undermine the per-person force of punishment/social pressure.
- `num_rounds`: Considered in both theory and experiment as a factor for sustaining punishment/cooperation over time (Larson, 2016; dos Santos et al., 2014; Inaba et al., 2016).
- `all_or_nothing`: Present in multiple models; moderate all-or-nothing policies may maintain cooperation, but evidence is indirect (Syi, 2014).
- `mpcr`: Discussed and modeled as a key moderator; higher MPCR strengthens group-level payoffs (Inaba et al., 2016; Garay et al., 2014).
- `punishment_cost`, `punishment_tech`: Directly analyzed in terms of their moderating effects on outcomes in several papers—high costs may reduce punishment use, and different 'technologies' of punishment/exclusion have divergent effects (Larson, 2016; Syi, 2014; Furuzono et al., 2013).

**Indirectly informed/contextual:**
- `chat`: Used as an experimental variable (dos Santos et al., 2014; Larson, 2016), but impact on efficiency is not well quantified.
- `show_n_rounds`, `show_other_summaries`: Considered as part of cognitive and informational environment (Inaba et al., 2016); their role is theorized rather than empirically measured.
- `reward_exists`: Analyzed in the context of evolutionary models (Garay et al., 2014), with indirect effects on the stability of efficient strategies.

**Sparse or not discussed:**
- `default_contrib`: Not empirically addressed.
- `reward_cost`, `reward_tech`, `reward_magnitude`: Only contextually discussed (Garay et al., 2014), not examined in classic PGG terms.
- `show_punishment_id`: Mentioned in relation to information environments (Larson, 2016), but not directly studied for effect on efficiency.
- `punishment_magnitude`: Not specified or analyzed as a separate dimension.

# 7) Important Limitations

- **Empirical evidence on classic PGGs is lacking:** There is only one experimental paper with direct efficiency results relevant to punishment in a PGG-adjacent design (dos Santos et al., 2014). Most findings extrapolate from theory or from variant games where mechanisms or context differ substantially.
- **Punishment design details are underexplored:** Many dimensions critical to real game design—such as punishment magnitude, the structure of punishment costs and rewards, and the visibility/attribution of actions—are not systematically varied or analyzed.
- **Most findings are theoretical and model-dependent:** The models offer significant insight into likely mechanisms and moderators (error rates, information, group size), but real-world parameter variation and unintended behaviors (e.g., antisocial punishment) are not captured.
- **Non-payoff outcomes are often reported over efficiency/payoff:** Several studies emphasize cooperation rates or psychological factors, which do not map directly onto efficiency, limiting their utility for the primary prediction task.
- **Applicability to the downstream prediction task requires caution:** The absence of systematic analysis across all 14 prediction dimensions, and lack of direct experimental measurements of efficiency with/without punishment in canonical PGGs, mean predictions must be highly qualified and conditional.
- **Potential for contradictory effects:** Some models predict positive effects of punishment or institutional information on efficiency, but these are contingent on untested conditions (e.g., low error, strong group incentives). Real environments may fail these assumptions, potentially resulting in inefficacy or even efficiency loss with punishment.

---

**In summary:**  
The evidence base is primarily theoretical and only indirectly addresses the key prediction task. Findings converge on the importance of information structure, error rates, and the interaction of group size and sanction strength, but do not deliver robust empirical effect size estimates for punishment's impact on efficiency in standard public goods games. Use this corpus to guide expectations about moderators and mechanisms—not to generate precise quantitative predictions.
