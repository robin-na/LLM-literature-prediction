# 1) Evidence Base

The paper set comprises seven studies spanning empirical laboratory experiments, real-world observational research, agent-based modeling, and formal theory. Four studies are laboratory-based experiments (Li et al., 2018a; Li et al., 2018b; Chen et al., 2019; Powers et al., 2018), one is a real-world/online observational study (Frey, 2019), two are theoretical or agent-based modeling studies (Nhim et al., 2019; Aguilar & Akçay, 2018). The topics cluster around cooperation, punishment, social norms, neural modulation, and evolutionary-cultural dynamics.

For the downstream prediction task—estimating the effect of introducing peer punishment on efficiency in public-goods-like environments—this is a narrow and weakly focused evidence base. Empirical coverage of punishment and associated payoff outcomes is sparse; most studies either lack a punishment mechanism or do not report efficiency or related group payoff results. Model-based and theoretical evidence sometimes include punishment, but generally as a mechanism to sustain cooperation, with only indirect links to payoff or efficiency outcomes.

# 2) Task Relevance

### pgg_or_variant
- **exact:** Four papers use the standard linear PGG or very close analogs (Li et al., 2018a; Li et al., 2018b; Frey, 2019; Powers et al., 2018).
- **close:** Two papers use environments structurally similar to PGGs: one is a common-pool-resource agent-based model (Nhim et al., 2019) and the other a three-player Prisoner's Dilemma with punishment (Chen et al., 2019).
- **adjacent:** One paper (Aguilar & Akçay, 2018) discusses social dilemmas in an evolutionary/altruism context but not in the PGG framework.

### punishment_or_sanctions
- **exact:** One study directly incorporates a punishment mechanism (Chen et al., 2019) and one agent-based model includes peer punishment (Nhim et al., 2019).
- **adjacent/none:** The remaining studies do not include punishment or sanctions in their core design. Some, such as Li et al. (2018a), provide context on cooperation without sanctions.

### efficiency_or_related_payoff_outcome
- **adjacent or weak:** None of the studies report group efficiency or total payoff as a primary or secondary outcome in experimental or empirical contexts where punishment is enabled. Some model-based or theoretical studies discuss socially optimal outcomes or the collapse of cooperation as a proxy for efficiency (Nhim et al., 2019), but without quantitative efficiency data.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (efficiency, group payoff, welfare, surplus):** Essentially absent from empirical studies with punishment; some adjacent, qualitative reference in theory/model work (Nhim et al., 2019).
- **Non-payoff behavioral outcomes (contribution rate, cooperation rate, punishment frequency):** Dominant focus across the set. Most empirical studies measure compliance with cooperative norms, contribution behavior, norm reinforcement, the modulation of punishment behavior (but not payoff), or the evolution of beliefs about cooperation.
- **Psychological/attitudinal outcomes:** Notably, some studies focus on belief updating about cooperation norms or the influence of neural stimulation on such beliefs or behaviors (Li et al., 2018b).
- **No direct measurement:** One theory paper (Aguilar & Akçay, 2018) is agnostic to specific experimental outcomes.

# 4) Main Findings Relevant To Prediction

### Empirical Context (With/Without Punishment)
- In **public goods games without punishment**, contribution rates and cooperation are generally low, especially in real-world or long-term settings (Frey, 2019); neural or cultural interventions can modulate voluntary cooperation (Li et al., 2018a, 2018b), but improvements in contribution do not directly translate into evidence for efficiency effects of punishment.
- Evidence from the **introduction of punishment** is extremely limited:
    - **Punishment Mechanism Effects:** When punishment is available (in a three-player prisoner's dilemma, not a standard PGG), external manipulation of neural circuits can reduce or increase the frequency of punishment and thereby affect cooperation rates (Chen et al., 2019), but there is no reported effect on group-level payoff or efficiency.
    - **Model-Based Evidence:** Agent-based modeling suggests that punishment sustains high cooperation only if resource abundance, social capital, and punishment strength are sufficient, while inequality or scarcity nullifies or undermines those effects, and system outcomes are either full cooperation or collapse (Nhim et al., 2019). The payoff connection is indirect, inferred through the prevalence of cooperation rather than actual calculated efficiency.

### Theoretical Context
- **Cultural Processes:** Evolutionary models indicate the possibility for cultural selection to sustain altruistic/cooperative traits regardless of underlying genetic selection (Aguilar & Akçay, 2018), implying the domain importance of cultural “institutions” for cooperation in social dilemmas—but this has no direct implication for the marginal effect of punishment on quantifiable efficiency.

### Game Design Dimensions
- Several studies explore contexts with variation in **player count, number of rounds, MPCR, all-or-nothing,** and presence/absence of **summary information** (Li et al., 2018a, 2018b; Frey, 2019), but do not provide treatment comparisons with/without punishment, nor do they measure efficiency outcomes in those contrasts.

# 5) Prediction Guidance

**Due to the lack of direct empirical evidence on group efficiency or total payoff outcomes as affected by peer punishment in public-goods-game-like environments, this literature set can only inform prediction tasks in a very limited and indirect manner.** Key guidance points are:

- Baseline contribution rates (and thus efficiency) in PGGs **without punishment** are low and stable, especially outside lab conditions (Frey, 2019). This is specifically relevant for predicting the control condition.
- The general effect of punishment in adjacent domains (i.e., common-pool models and three-player dilemmas) is to increase cooperation rates under favorable conditions (such as low resource scarcity and low inequality, plus high punishment strength) (Nhim et al., 2019; Chen et al., 2019). However, there is no empirical evidence quantifying the translation of these effects into efficiency gains.
- The risk exists that under high inequality, high scarcity, or other adverse environment dimensions, punishment may lose effectiveness or even fail to sustain cooperation (Nhim et al., 2019).
- Given this, **absolute predictions about efficiency effects of enabling punishment cannot be supported by this set**. At most, one can infer that in some contexts punishment may raise cooperation and, by extension, efficiency, but that these effects are contingent and unquantified in the available data.
- Individual-level or population-level neuropsychological and cultural factors can shift baseline voluntary cooperation but are not shown to directly interact with punishment mechanisms in a payoff-relevant way.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed:**  
- **Player count, number of rounds, MPCR, all-or-nothing, chat, show_n_rounds, show_other_summaries:** Widely reported in designs (Li et al., 2018a,b; Frey, 2019; Powers et al., 2018; Chen et al., 2019).
- **Punishment cost:** Only addressed in model (Nhim et al., 2019) and one lab punishment manipulation (Chen et al., 2019).

**Indirectly informed/contextually discussed:**  
- **Punishment tech, reward exists, reward tech, reward cost:** Only briefly featured in model context (Nhim et al., 2019); not empirically explored.

**Effectively missing:**  
- **Show punishment ID, reward magnitude, punishment magnitude, default_contrib:** No study systematically examines these parameters or their consequences for efficiency with punishment in PGGs.

**Crucially, none of the 14 dimensions are empirically studied with respect to their effect on the marginal efficiency gain from enabling punishment.** All specific findings pertain to cooperation rates or beliefs rather than efficiency metrics.

# 7) Important Limitations

- **No Direct Evidence for Core Prediction Task:** There is an absence of empirical studies manipulating both punishment presence and group efficiency/payoff outcomes in PGGs. The main outcome of interest (change in efficiency with punishment enabled) is not measured directly in any study.
- **Behavioral Outcomes ≠ Payoff Outcomes:** Almost all findings concern behavioral variables (contribution rate, norm compliance, punishment frequency), which are not synonymous with efficiency or group payoff, and caution must be used in inferring payoff outcomes from these metrics.
- **Limited Dimensional Coverage:** While some game design variables are present across the papers, the specific variables most likely to affect the impact of punishment on efficiency (punishment magnitude, visibility, default contribution) are not systematically varied or analyzed for payoff impact.
- **Domain Generality and External Validity:** The agent-based and theoretical studies are structurally similar to PGGs but differ in crucial institutional assumptions (e.g., resource scarcity, land inequality, seasonal harvest), limiting generalizability.
- **Lack of Cross-Condition Comparisons:** No study provides clean within-game contrasts between punishment-enabled and punishment-disabled conditions reporting subsequent changes in payoff or efficiency.
- **Ambiguity around Adverse Contexts:** Model evidence suggests contextual moderators (scarcity, inequality) can undermine punishment’s ability to sustain cooperation, but this is neither empirically tested nor translated into quantitative efficiency changes in PGGs.

---

**In summary:** The literature set provides useful contextual and baseline information about cooperation in PGGs without punishment and theoretical foundations for when punishment may or may not sustain cooperation. However, it is inadequate for quantitatively predicting the marginal effect of punishment on efficiency across game design dimensions. Key payoff- and mechanism-relevant findings are either absent or purely adjacent, with all substantial claims about punishment’s effect on efficiency remaining untested in the empirical set.
