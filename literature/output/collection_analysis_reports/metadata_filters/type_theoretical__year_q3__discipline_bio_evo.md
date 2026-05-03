# 1) Evidence Base

The paper set is large (51 theory-focused papers), composed almost entirely of formal theory and simulation modeling; there are no laboratory or field experiments, and only a handful of papers synthesize empirical data. The majority of the work focuses on public-goods games (PGGs) or very close structural variants, with a strong emphasis on modeling punishment, sanctions, or institutional enforcement mechanisms intended to promote cooperation. Most outcomes are payoff-based (efficiency, group payoff, mean welfare), though a substantial minority focus only on cooperation rates, punishment frequency, or strategy persistence. The theoretical coverage of punishment and efficiency in PGG-like environments is broad, directly addressing a wide range of game design parameters, but the absence of controlled experimental studies limits the capacity for quantitative calibration of effect sizes. Nonetheless, the models provide diverse, often explicit, qualitative and sometimes quantitative guidance for predicting efficiency effects when enabling punishment.

# 2) Task Relevance

**pgg_or_variant**:  
- Most papers are of `exact` or `close` relevance—they model standard PGGs, optional PGGs, or very similar collective action and resource-sharing games.
- Some adjacent models (e.g., common-pool resources, mutual-aid games) provide contextually relevant findings for PGG-like dynamics but differ in important structural ways from classic PGGs.

**punishment_or_sanctions**:  
- The central focus is on punishment or sanctions, with most papers targeting `exact` or `close` modeling of peer, institutional, or exclusion-based punishment.
- Several papers explore variants such as reward, reputation, or exclusion, which are adjacent to classic punishment paradigms.

**efficiency_or_related_payoff_outcome**:  
- A strong fraction deliver `exact` guidance on efficiency or total group payoff, the core outcome for prediction.
- Others deliver `close` guidance by addressing group welfare, surplus, or mean fitness, which are tightly linked to efficiency but occasionally confounded with cooperation rates.
- A significant minority measure only non-payoff behavioral outcomes (contribution rates, norm compliance), yielding only `adjacent` or `weak` evidence on efficiency.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes:**
- **Directly measured efficiency:** Many theory papers (e.g., Dong et al., 2019; Jiao et al., 2020; Fang et al., 2020; Wang & Lv, 2019; Murase & Baek, 2021; Huang et al., 2018) model group efficiency or total payoff as the primary outcome, reporting either explicit group payoff ratios or expected mean welfare compared to full cooperation.
- **Indirect or adjacent payoffs:** Some papers measure group achievement, surplus, or mean fitness (e.g., Couto et al., 2020; Bhui et al., 2019; Nakamaru et al., 2018), which strongly correlate with efficiency but may include confounds (e.g., time to achieve, population fitness).
- **Non-payoff behavioral outcomes:** Numerous studies focus only on contribution rates, cooperation stability, punishment use, extinction/maintenance of strategies, or social norm compliance (e.g., Greenwood et al., 2018; Fehr & Schurtenberger, 2018; Gavrilets, 2020). These outcomes are informative about the underlying group dynamics but do not measure efficiency directly.

# 4) Main Findings Relevant To Prediction

**1. Effect of Enabling Punishment on Efficiency is Highly Conditional**
- **Positive effects:** Theoretical models show punishment can stabilize cooperation and increase efficiency, especially if the punishment is not too costly, is highly effective, and targets defectors (e.g., Wang & Lv, 2019; Huang et al., 2018; Couto et al., 2020; Nakamaru et al., 2018; Murase & Baek, 2021).
- **Negative or null effects:** If punishment is costly, prone to anti-social use, or undermined by corruption/bribery, it can reduce efficiency—even if cooperation rates increase (Dong et al., 2019; Fehr & Schurtenberger, 2018; Fang et al., 2020). The costs inflicted by punishment can easily outweigh the gains from increased cooperation.
- **Key moderators:** The impact is strongly moderated by punishment cost, punishment effectiveness (magnitude), group size, possibility of error/mistargeting/antisocial use, and the broader normative or institutional context.

**2. Institutional and Probabilistic Mechanisms Often Outperform Peer Punishment**
- **Reward vs. punishment:** Models often find that institutional reward is more robust than punishment for boosting efficiency, especially under bounded rationality and decision errors (Dong et al., 2019).
- **Graduated/probabilistic punishment:** Moderate, probabilistically executed, or graduated punishment (rather than deterministic or harsh fixed punishment) is optimal for efficiency under many conditions (Jiao et al., 2020; Couto et al., 2020).

**3. The Interaction with Other Mechanisms and Contextual Moderators**
- **Reputation and social norms:** Reputation mechanisms can substitute for or enhance punishment; their presence can turn inefficient punishment treatments into efficient ones (Podder et al., 2021; Fehr & Schurtenberger, 2018).
- **Corruption, bribery, and monitoring effectiveness:** These strongly moderate punishment's impact on efficiency (Fang et al., 2020; Huang et al., 2018).
- **Resource/ecological context:** In common-pool resource games, the effect of punishment on efficiency depends on the underlying growth or renewal rates—punishment cannot 'create' resource if the system is overexploited despite cooperation (Chen & Szolnoki, 2018).
- **Power asymmetries:** Asymmetric power can turn punishment into a coercive tool, reducing or even reversing its positive impact on group efficiency (Phillips, 2018).

**4. Population Structure and Dynamics**
- **Group size and spatial structure:** The benefits of punishment can vary with player_count (group size), often increasing with effectiveness at larger sizes but sometimes being diluted (Wang & Lv, 2019; Huang et al., 2018). Spatial clustering and repeated interactions (num_rounds) can enable even weak punishment to have larger effects.

# 5) Prediction Guidance

- **Direct, robust evidence:** Models explicitly parameterize and analyze the impact of `player_count`, `mpcr`, `punishment_cost`, `punishment_tech`, `reward_exists`, and sometimes `num_rounds`, `all_or_nothing`, and `punishment_exists` on efficiency, supporting direct functional predictions for these dimensions (e.g., Dong et al., 2019; Jiao et al., 2020; Wang & Lv, 2019; Huang et al., 2018).
- **If control efficiency is high:** Enabling punishment is often neutral or can reduce efficiency, since the potential for loss due to wrongly targeted or costly punishment exceeds marginal cooperative gains.
- **If control efficiency is low:** Punishment may improve efficiency, especially with low punishment cost and high punishment impact, but only if design prevents antisocial punishment, corruption, or retaliation.
- **Moderating features critical for accurate prediction:**
    - *Punishment cost and effectiveness*—Low cost, high impact increases the likelihood of efficiency gains.
    - *Presence/role of reward*—Reward may outperform punishment for efficiency.
    - *Normative context*—Norms that prevent antisocial punishment increase the chances of efficiency improving.
    - *Reputation and monitoring*—Integrating peer information and reputational consequences can substitute for or complement punishment.
- **Important caveats:** There is no universal effect—efficiency can decrease or increase depending on interacting dimension values. Predictions should adjust the direction and magnitude of the predicted efficiency shift when enabling punishment according to these moderators.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed (modeled in outcome/parameter space):**
- `player_count`: Almost universal in models—group size is a core game parameter.
- `num_rounds`: Regularly modeled, especially in repeated games.
- `mpcr`: Core parameter in (almost) all PGG models.
- `punishment_cost`, `punishment_tech`: Central in most punishment models.
- `all_or_nothing`: Explicitly modeled in many theoretical papers.
- `reward_exists`: Often included in contrast with punishment.
- `punishment_exists`: Thematic focus throughout.

**Indirectly addressed:**
- `default_contrib`: Sometimes considered via framing effects or opt-in/opt-out mechanisms but rarely a primary model parameter.
- `reward_cost`, `reward_tech`: Addressed in fewer papers, mostly those comparing reward and punishment.
- `show_n_rounds`, `show_other_summaries`: Sometimes addressed in repeated or informational games, but mostly as context rather than outcomes drivers.
- `show_punishment_id`: Addressed in a minority of models (e.g., identity-based or reputation-based punishment), often contextually.

**Contextually mentioned, not modeled:**
- `chat`: Social communication discussed in relation to reputation and norm formation but rarely explicitly modeled as a game dimension.

**Missing or weakly addressed:**
- Some interface and process-level variables (e.g., UI features or detailed chat implementation) are essentially absent.

# 7) Important Limitations

- **Theory biases:** All evidence is theoretical/model-based—robustness to real human behavior, error, and contextual factors is limited, and empirical calibration is unavailable.
- **Non-payoff outcomes:** Many papers use cooperation rate or norm compliance as the primary outcome, which does not always correlate with higher efficiency due to punishment cost or the risk of anti-social punishment.
- **Ambiguity on edge-cases:** While many models agree on mechanisms, there is notable disagreement or model uncertainty in parameters close to threshold effects (e.g., intermediate punishment cost, potential for antisocial punishment).
- **Limited scope for design features:** Not all 14 prediction dimensions are directly tested—most guidance rests on a subsample of core game-theoretic variables (player count, mpcr, punishment parameters) with less about chat, interface, or dynamic feedback cues.
- **Generalizability constraints:** Adjacent models (common-pool resource, mutual-aid, reputation) offer valuable context, but direct applicability to canonical PGG settings may be limited, especially regarding the causal effect of enabling punishment.
- **No empirical calibration:** Quantitative predictions should be interpreted as qualitative directionality or approximate bounds, not as point estimates for real world or experimental effects.

---

**References**  
(Selected from in-text citations for representative grounding, full source listing in evidence section.)  
- Dong et al., 2019  
- Jiao et al., 2020  
- Wang & Lv, 2019  
- Fang et al., 2020  
- Huang et al., 2018  
- Couto et al., 2020  
- Fehr & Schurtenberger, 2018  
- Podder et al., 2021  
- Phillips, 2018
