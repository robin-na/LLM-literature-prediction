# 1) Evidence Base

This literature set is comprised entirely of **theoretical papers** (no direct empirical or laboratory/field experimental studies), with a strong focus on evolutionary game theory, formal modeling, and simulation results. The set is both **broad in coverage**—addressing many contextual and mechanistic debates about punishment and cooperation—but **narrow for direct prediction**, since almost no papers report direct, outcome-based experimental effect estimates for treatment vs. control efficiency in public goods games (PGGs) with and without punishment. Virtually all findings are derived from analytical models or simulations, and most outcome claims are based on equilibrium states and stability properties, not observed payoffs in controlled treatments.

# 2) Task Relevance

## pgg_or_variant

- **Exact relevance**: The majority of this set directly models canonical or near-canonical PGGs, closely related n-person public goods games, and their typical lab variants, using standard contribution and incentive structures. Most models parameterize design features analogous to the prediction task dimensions.
- **Close to adjacent relevance:** Several papers cover mutualism, repeated prisoner's dilemmas, partner control, indirect reciprocity, or threshold public-good/bystander/volunteer games. These are structurally related but not always identical to lab or online PGG experiments.
- **None**: A minority of papers lack any PGG or direct analog.

## punishment_or_sanctions

- **Exact relevance**: Most models explictly examine punishment (peer or institutional), including cost, targeting, possibility of anti-social punishment, and the conditions for its evolutionary stability.
- **Close relevance**: Many papers also analyze adjacent enforcement concepts—reputation losses, exclusion, partner choice, or withdrawl—treated as punishment-like in effect.
- **None**: Very few papers wholly exclude punishment.

## efficiency_or_related_payoff_outcome

- **Exact relevance**: A substantial subset explicitly addresses group efficiency, total group payoff, welfare, or equivalent measures—sometimes as primary outcomes (e.g., "group efficiency as average payoff/maximum possible").
- **Close/adjacent**: Many others focus on related proxies (e.g., prevalence of cooperation or punishing strategies) and interpret findings as having direct implications for efficiency, though without always giving explicit payoff ratios.
- **Weak/none**: Many models stop at behavioral or norm frequencies (cooperation rate, contribution rate, etc.), and do not calculate aggregate payoffs or efficiency ratios.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes**: 
    - *Explicit/primary:* group efficiency (payoff as % of full cooperation), total group payoff, mean fitness, welfare, or surplus (e.g., Cressman et al., 2012; Eldakar et al., 2007; Powers et al., 2012; Bowles & Gintis, 2004).
    - *Proxy/inferred:* equilibrium levels of cooperation mapped to efficiency under explicit cost/benefit equations (e.g., Gintis, 2000; Rand et al., 2010).
- **Non-payoff behavioral outcomes**:
    - Prevalence/frequency of cooperation, punishment, retaliation.
    - Evolutionary stability of cooperative, punishing, and defecting strategies.
    - Norm compliance, emergence of social learning, reputation status, or conformity dynamics.
    - These are interpreted as predictors or prerequisites for high efficiency, but are not always accompanied by quantitative payoff/effect ratios.

*Many papers conflate these outcome types or interpret greater cooperation as synonymous with higher efficiency, but a subset explicitly warns this is not always so (e.g., Guala, 2012; Jaffe, 2004).*

# 4) Main Findings Relevant To Prediction

## Synthesis Across Papers

### General Effect of Punishment

- **Theory consensus:** Enabling punishment in canonical PGGs *can* increase average group efficiency above the no-punishment baseline by deterring free-riding and sustaining higher cooperation rates (Cressman et al., 2012; Eldakar et al., 2007; Gintis, 2000; Henrich & Boyd, 2001; Bowles & Gintis, 2004; Okada & Bingham, 2008).
- **Conditionality:** The positive efficiency effect is **highly conditional**—it appears *only* when:
    - Punishment cost is not too high, and punishment is effective (high impact per cost) (Gintis, 2000; Okada & Bingham, 2008; Liu & Guo, 2010).
    - Anti-social and retaliatory punishment are rare or disabled (Rand et al., 2010; Powers et al., 2012; Wolff, 2012; Janssen & Bushman, 2008).
    - Game parameters (e.g., group size, MPCR, number of rounds) are favorable (Eldakar et al., 2007; BOYD & RICHERSON 1992).
    - Reputation or coordination mechanisms exist to reduce the frequency or cost of punishment (dos Santos et al., 2011; Milinski & Rockenbach, 2012).
    - The baseline efficiency (without punishment) is not already high (Archetti et al., 2011; Bach et al., 2006).
- **Negative or ambiguous findings:** Punishment, especially peer/punishment with frequent errors, may *reduce* group efficiency because of the destruction of resources—unless cost-effectiveness and deterrence are high or punishment rapidly recedes as a threat (Guala, 2012; Jaffe, 2004; Sigmund, 2007).

### Moderators & Mechanism Insights

- **Cost and effectiveness of punishment:** Lower cost and higher impact magnify positive efficiency effects, while high cost or low effectiveness can nullify or reverse gains (Henrich & Boyd, 2001; Gintis, 2000; Okada & Bingham, 2008; Gardner & West, 2004).
- **Group size:** Efficiency gains from punishment diminish as group size increases—punishment becomes harder to coordinate, costs spread thin, and anti-social punishment more easily arises (Eldakar et al., 2007; Powers et al., 2012; Bowles & Gintis, 2004).
- **Anti-social punishment:** Allowing punishment of cooperators by defectors (anti-social punishment) can erase or even reverse the positive efficiency effect of punishment (Rand et al., 2010; Powers et al., 2012).
- **Retaliation:** If punished players can easily identify and retaliate against punishers, punishment loses its deterrent power and does not support higher efficiency (Janssen & Bushman, 2008; Wolff, 2012).
- **Reputation & visibility:** Punishment is more likely to increase efficiency when its use/visibility is reputationally tracked and alters future cooperative opportunities (dos Santos et al., 2011; Brandt et al., 2003).
- **Combined mechanisms:** Combining punishment with rewards, reputation, or group coordination can allow efficiency gains to emerge sooner and be more robust to errors (Cressman et al., 2012; Milinski & Rockenbach, 2012).
- **Population structure:** Spatial or group-structured populations support much more robust efficiency gains from punishment than well-mixed populations—structure supports clusters of cooperators/punishers and inhibits invasion by defectors (Helbing et al., 2010; BOYD & RICHERSON, 1992).
- **Payoff structure:** In nonlinear or threshold PGGs where baseline efficiency is already high due to game structure, the marginal impact of punishment is smaller (Archetti et al., 2011; Bach et al., 2006).
- **Voluntary participation:** Optional participation mechanisms may allow punishment to invade and increase efficiency only under specific payoff and threshold conditions (Mathew & Boyd, 2009).

# 5) Prediction Guidance

**How should this literature inform prediction of treatment efficiency from design dimensions plus control efficiency for PGG-like games with peer punishment enabled?**

- **Efficiency with punishment is generally predicted to exceed baseline efficiency,** but only if:  
    - *Punishment is not too costly relative to its effectiveness;*  
    - *Anti-social and retaliatory punishment are limited;*  
    - *Group size is moderate/small;*  
    - *No strong alternative mechanisms (e.g., very high MPCR, threshold/nonlinear PGG with high baseline efficiency) already sustain cooperation;*  
    - *Reputation, coordination, or group structure supports the effectiveness and targeting of punishment.*

- **Key design moderators to consider in prediction:**
    - **player_count**: Larger groups weaken punishment's impact, may lower or negate efficiency gains due to coordination problems and diffusion of punishment.
    - **num_rounds**: Sufficiently many rounds are required for punishment to impact behavior and for cooperation to be re-established after punishment; very short games see minimal effect.
    - **mpcr**: Higher MPCR makes cooperation easier, so punishment adds less marginal value.
    - **punishment_cost & punishment_tech (effectiveness):** Efficiency gains are only observed when the cost is not prohibitive given the deterrent effect (ratio of fine-to-cost).
    - **anti-social punishment possibility** (not always a coded dimension): If design allows punishment of cooperators, expect no efficiency gain or a negative effect.
    - **retaliation & show_punishment_id:** If punished players can identify (and punish) punishers, efficiency effects are undermined.
    - **reward_exists, reward_cost, reward_tech:** Reward can support initial increases in cooperation, but only combined with punishment does efficiency reliably max out.
    - **all_or_nothing vs. continuous contribution & default_contrib:** Some results depend on whether contributions are binary or continuous and how the framing nudges initial behavior.
    - **chat:** Not often modeled directly; when included or referenced, communication can substitute for or amplify punishment’s effectiveness.
    - **show_n_rounds, show_other_summaries:** Transparency and information flow can increase the effect of punishment, especially via reputation.
    - **spatial or network population structure:** Supports higher and more stable efficiency gains from punishment.

- **Use control efficiency (baseline) contextually:** If the control game already achieves high efficiency (e.g., via high MPCR or nonlinear thresholds), the predicted efficiency increase from enabling punishment is likely to be smaller.

- **Magnitude and direction of effect:** The literature is predominately qualitative/theoretical. When punishment is costly, anti-social punishment is possible, or coordination is lacking, punishment can *reduce* efficiency—even if it increases cooperation rates (Guala, 2012; Jaffe, 2004).

- **Do *not* infer more than mechanism allows:** In the absence of direct empirical estimates, predictions are scenario-sensitive. For models not including behavioral noise, framing effects, or anti-social punishment, effects may be overstated compared to real-world settings.

# 6) Design Dimensions Highlighted Across Papers

- **Directly Informed Dimensions**:
    - `player_count` (group size): Parameterized and analyzed in many papers.
    - `num_rounds` (game length): Modeled as the number of repeated interactions.
    - `mpcr`: Central moderator in most models.
    - `punishment_cost`, `punishment_tech` (cost/effectiveness): Explicit focus throughout.
    - `all_or_nothing` (binary/continuous contributions): Differentiated in several models.
    - `reward_exists`, `reward_cost`, `reward_tech`: Analyzed in models with both "stick and carrot".
    - `show_n_rounds`, `show_other_summaries`: Information and visibility are often modeled.

- **Indirectly Informed/Contextually Referenced**:
    - `chat`: Sometimes discussed (rarely directly modeled).
    - `default_contrib`: Framing effects referenced, but rarely parameterized.
    - `show_punishment_id`: Considered in retaliation/visibility models.

- **Missing or Sparse**:
    - Very few, if any, models explicitly manipulate or report on: `chat`, `default_contrib`, or nuanced UI features.
    - No direct modeling of platform effects (e.g., lab vs. online) or cultural context.

- **Crucial but often only contextually addressed**:
    - Possibility of anti-social punishment, retaliation, and institutionally enabled reputation/coordination mechanisms.

# 7) Important Limitations

- **Absence of empirical effect estimates**: All conclusions about efficiency changes from punishment are theoretical or based on simulation—no controlled experimental effect sizes or real-world field estimates are provided in this set.
- **Over-reliance on equilibrium/long-run dynamics**: Predictions may not match short-run or single-treatment lab experiments.
- **Limited attention to behavioral noise, framing, and context**: Issues such as cultural variance, learning, and experimental demand characteristics are largely ignored.
- **Many models assume ideal targeting, no anti-social punishment, and no errors**: This likely overstates efficiency gains, as laboratory and field data often show substantial resource wastage due to mis-targeted or retaliatory punishment.
- **Anti-social punishment and retaliation are rarely modeled, but are known from empirical work to be vital moderators**: The few papers addressing these factors show that their presence can fully reverse expected efficiency outcomes.
- **Qualitative guidance predominates; quantitative guidance is weak:** Most models indicate the *direction* and *conditionality* of effects, not their magnitude.
- **Indirect linkage of non-payoff and payoff outcomes:** Many findings on cooperation or norm enforcement are used as proxies for efficiency, but may not predict total group payoff when accounting for the costliness and self-reinforcing nature of sanctioning.
- **Sparse coverage of some design dimensions:** Chat, framing, visibility of punishment, and user interface/channel features are rarely manipulated and only sometimes discussed.

---

**In summary:**  
This paper set provides **strong theoretical, mechanism-based support** for the conditional prediction that enabling appropriately designed punishment in PGG-like environments increases group efficiency, but only when costs, retaliation, anti-social punishment, and group size are favorable. Most of the 14 prediction dimensions are at least indirectly addressed, with player count, punishment cost/effectiveness, group structure, and reputation information highlighted as critical moderators. However, the literature is **missing empirical outcome data and fine-grained, quantitative dimension-level effect estimates**, and warnings about anti-social punishment, retaliation, and high cost directly challenge the generalizability of positive predictions. Use this base for **mechanistic directional prediction and scenario mapping, not for precise quantitative efficiency forecasting**.
