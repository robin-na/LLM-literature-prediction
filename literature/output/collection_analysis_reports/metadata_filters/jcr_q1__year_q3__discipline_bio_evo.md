# 1) Evidence Base

The paper set comprises 37 papers, encompassing a mix of **theoretical modeling**, **lab and field experiments**, **observational studies**, and **conceptual reviews**. The corpus is **broad in coverage** but **heterogeneous** in both empirical grounding and conceptual relevance to the specific prediction task. Several papers deliver **direct empirical (lab and field experimental) evidence** on efficiency and payoff outcomes in public goods games with punishment enabled or disabled (e.g., Wegmann & Musshoff, 2019; Burton-Chellew & Guérin, 2021). Others offer **strong theoretical or simulation-based predictions** regarding punishment’s effects (e.g., Dong et al., 2019; Murase & Baek, 2021). Many papers, however, are **only tangentially related**—focusing on cooperation rates, punishment types, neural mechanisms, or broader socioeconomic and evolutionary contexts, often without direct analysis of group efficiency or PGGs per se.

The empirical papers relevant to the prediction task are **mainly lab experiments in classic linear PGG settings**, plus a few large-scale field or framed field studies in common-pool resource (CPR) games, which are **functionally close but not always exact matches**. Theory papers address a wider variety of game structures, mechanisms, and institutional contexts, typically offering nuanced predictions about when punishment can help or hinder efficiency. There is **variation in how directly the studies map onto actionable prediction** for payoff-based outcomes when game design features and baseline efficiencies are specified.

# 2) Task Relevance

### `pgg_or_variant`
- **Relevance: exact–close (most important papers)**  
  - **Exact**: Approaches using repeated or one-shot standard public goods games (PGGs) with classic parameters (e.g., Burton-Chellew & Guérin, 2021; Dong et al., 2019).
  - **Close**: Studies using linear CPR games or formally analogous structures (e.g., Wegmann & Musshoff, 2019), or exploring optional PGGs and similar dilemmas (e.g., Podder et al., 2021).
  - **Adjacent–weak**: Many theory papers generalize to PGGs but are modeled on more abstract or differing games (Prisoner's Dilemma, dyadic interactions, mutualisms).

### `punishment_or_sanctions`
- **Relevance: exact–adjacent**  
  - **Exact**: Direct manipulation of punishment enabled/disabled in standard PGGs or CPR games (e.g., Burton-Chellew & Guérin, 2021; Wegmann & Musshoff, 2019; Dong et al., 2019; Podder et al., 2021).
  - **Close–adjacent**: Some model punishment in related forms (inspection, entrance fee, reputation-based enforcement, institutional rules). A subset focus on reputational or third-party sanctions, which are relevant but may function differently.
  - **None–weak**: Several papers focus on communication, reward, observability, or other factors without including punishment or sanctions directly.

### `efficiency_or_related_payoff_outcome`
- **Relevance: exact–adjacent**  
  - **Exact**: A handful of key theory and field/experimental papers **directly report efficiency or group payoff with and without punishment** (e.g., Wegmann & Musshoff, 2019; Dong et al., 2019; Murase & Baek, 2021).
  - **Close–adjacent**: More commonly, outcomes reported are cooperation rates, contributions, or theoretical analyses that assert implications for efficiency but often without direct calculation.
  - **None–weak**: Many studies highlight only behavioral, neural, or reputation-based variables, omitting payoff-based group outcomes.

**Summary:**  
- **Direct, strong qualitative and some quantitative evidence** on efficiency change with peer punishment is present, but sparsely distributed among theory and field experimental papers.
- **Many papers are only indirectly informative** due to missing direct efficiency outcomes or diverging from canonical PGG designs.

# 3) Outcomes Measured In The Literature

## **Payoff-Related Outcomes (Efficiency, Group Payoff, Welfare)**
- **Directly measured in only a minority of papers:**  
  - Examples:  
    - **Efficiency increases with punishment:** Wegmann & Musshoff (2019): control 86% vs. punishment 97% (field).
    - **Punishment reduces efficiency:** Dong et al. (2019, theory); Burton-Chellew & Guérin (2021, experimental) — explicit statements that punishment is ‘ultimately destructive’ to group welfare.
    - **Potential for maximal efficiency enforcement:** Murase & Baek (2021, theory) when appropriate contingent strategies (not external peer punishment) are used.
- **Some model aggregate payoffs or welfare, but focus more on mechanism/conditions:** (e.g., Chen & Szolnoki, 2018; Bhui et al., 2019; Hooper et al., 2021)
- **Several studies do not report efficiency or group payoff even if related mechanisms are present**, focusing instead on contributions/cooperation rates.

## **Non-Payoff Behavioral Outcomes**
- **Much more commonly measured:**  
  - Contribution rate, cooperation rate, conditional cooperation, punishment behaviors, anti-social vs. pro-social punishment, coordinated punishment preferences, neural and psychological correlates, use of gossip or reputation systems.
- **Behavioral changes are often interpreted as proxies for efficiency, but this is not always justified** — increases in cooperation can coexist with efficiency losses due to costliness of punishment (Fehr & Schurtenberger, 2018; Burton-Chellew & Guérin, 2021).
- **Many theory and overview papers focus on mechanisms of norm enforcement, reputation, signaling, and their impact on cooperation behavior rather than on group economic outcomes.**

# 4) Main Findings Relevant To Prediction

- **The effect of enabling punishment on efficiency is highly context-dependent and ambiguous.**  
  - **Punishment can increase, decrease, or have no effect on group efficiency** (measured as group payoff relative to full cooperation), depending on game design and context.

- **Destructive/Neutral Effects:**
  - **Punishment often reduces efficiency because its costs outweigh contributions gained**—especially when punishment is frequent, anti-social punishment occurs, and when marginal per capita return (MPCR) is low. In some lab PGGs, overall costs of punishment lead to net welfare loss despite stable or increased cooperation rates (Burton-Chellew & Guérin, 2021; Dong et al., 2019; Podder et al., 2021).
  - **Theoretical results with bounded rationality or error-prone players show group welfare typically declines with punishment, unless costs are very finely calibrated or errors are minimal** (Dong et al., 2019).

- **Positive/Beneficial Effects:**
  - **Externally imposed, well-calibrated punishment (e.g., fines for over-extraction in field CPR games) significantly increases efficiency**, achieving levels near the social optimum (Wegmann & Musshoff, 2019).
  - **When institutional context or reputation mechanisms constrain punishment (e.g., institutional reward, norm constraints, or synergy with reputation), efficiency can increase** (Fehr & Schurtenberger, 2018; Podder et al., 2021; Murase & Baek, 2021).
  - **Positive effects are stronger when resource dynamics are favorable, punishment is effective (high detection/fine/impact), and anti-social punishment is minimized** (Chen & Szolnoki, 2018; Wegmann & Musshoff, 2019).

- **Moderating Game Design Features:**  
  **Key dimensions with evidence for impact on punishment’s efficiency effect:**
  - **Type and cost of punishment (peer vs. institutional, cost-to-impact ratio)**
  - **Reputation mechanisms and observability (synergistic with or substituting for punishment)**
  - **Group size and repeated interaction (fatigue, anonymity, coordination matter)**
  - **Ecological and resource dynamics (e.g., resource renewal, risk of overexploitation in CPR)**
  - **Presence of reward or alternative incentive mechanisms**

- **The relation between increased cooperation/contribution and efficiency is often non-monotonic:** More cooperation via punishment does not guarantee higher group efficiency if punishment costs exceed the value of extra cooperation (Fehr & Schurtenberger, 2018; Burton-Chellew & Guérin, 2021).

# 5) Prediction Guidance

- **Direct prediction of average efficiency with punishment enabled from game design and control efficiency is only well supported for a limited subset of design/configuration space.**  
  - **Where direct field or lab evidence exists, use it as a strong anchor** (e.g., efficiency gains of ~8–11% in field CPR games with externally imposed sanctions; Wegmann & Musshoff, 2019).
  - **In standard lab PGGs, peer punishment frequently does NOT raise average efficiency—and can reduce it—unless design features limit anti-social punishment or reduce punishment costs** (Burton-Chellew & Guérin, 2021; Dong et al., 2019).
  - **If the control (no-punishment) efficiency is already low, enabling peer punishment is more likely to worsen efficiency—unless punishment is institutional, well-targeted, and anti-social punishment is suppressed.**
  - **In games with strong institutional, reputation, or communication mechanisms, efficiency with punishment enabled may rise, but only if the institution/norms prevent counterproductive punishment.**
  - **If game design includes features promoting coordination or reputational targeting (e.g., public punishment identity, powerful gossip channels), efficiency outcomes are highly sensitive to social learning dynamics and player preferences.**
  - **Empirical evidence for effects in large-N, long-run, or highly realistic settings is much more positive if the sanctioning is external, formal, and monitored, rather than peer-based and voluntary.**

- **For configurations not directly tested (i.e., sparse evidence on specific dimensional settings), expectations must rely on theory and analogy to adjacent findings, with high uncertainty.**

# 6) Design Dimensions Highlighted Across Papers

## **Directly informed (repeatedly analyzed with efficiency or payoff outcomes):**
- **player_count:** Explored in most PGG and CPR studies as well as theoretical models (Wegmann & Musshoff, 2019; Podder et al., 2021; Dong et al., 2019; Murase & Baek, 2021).
- **num_rounds:** Standard in repeated PGGs; effects on punishment fatigue, learning, and norm compliance are discussed (Burton-Chellew & Guérin, 2021).
- **all_or_nothing:** Both discrete (binary) and continuous contribution games are analyzed; specific effects on punishment cost-benefit tradeoff discussed (Dong et al., 2019; Molleman et al., 2019).
- **mpcr:** Universally included; central to theoretical and empirical prediction of baseline and punished efficiencies.
- **punishment_cost:** Strongly analyzed both in theory (cost-to-impact ratio a key moderator; Dong et al., 2019; Phillips, 2018; Podder et al., 2021) and empirically.
- **punishment_tech:** Peer vs. institutional or monitoring-based punishment is differentiated with meaningful empirical effects (Wegmann & Musshoff, 2019; Chen & Szolnoki, 2018).
- **reward_exists:** Directly compared with punishment in several papers (Dong et al., 2019; Wegmann & Musshoff, 2019), often found to be more robust in raising efficiency.

## **Indirectly informed/contextually discussed:**
- **chat:** Communication is occasionally included (Jolly & Chang, 2021; Molleman et al., 2019) but effects generally addressed via behavioral outcomes rather than efficiency.
- **show_other_summaries, show_n_rounds, show_punishment_id:** Considered in the design of some studies, especially those exploring observability, reputation, and social learning, but not systematically linked to efficiency outcomes.
- **default_contrib:** Framing (endowment effect, opt-in/opt-out) is rarely tested as a moderator of punishment’s efficiency effect.
- **reward_cost, reward_tech:** Only a minority of studies manipulate or model these variables with respect to efficiency effects.

## **Missing or sparsely covered:**
- **show_punishment_id:** While reputation and observability of punishment are discussed conceptually, their direct impact on efficiency in PGGs is rarely quantified.
- **game-level controls for anti-social punishment, punishment magnitude apart from cost, or explicit social network structure** are seldom analyzed for direct efficiency effects.

# 7) Important Limitations

- **Empirical evidence directly mapping control efficiency and design dimensions to post-punishment efficiency is sparse.** Few studies give both control and punishment-enabled efficiency in the same parameterized design, and where reported, sample sizes are modest (except select field studies).
- **Many studies measure only contribution or cooperation rates, not efficiency**—and the two diverge when punishment is costly.
- **There is significant heterogeneity in game structure, operationalization of punishment (institutional vs. peer, cost structures), and outcome measures across studies**. This hinders meta-analytic or formulaic prediction from the literature.
- **Effects of anti-social punishment, error/noise, and the potential for norm convergence or coordination are often not experimentally controlled or systematically analyzed.**
- **Field and lab domains differ:** Field experiments with monitored institutional punishment consistently find larger, positive efficiency gains versus peer punishment in lab PGGs, which commonly yield neutral or negative welfare outcomes.
- **Few studies systematically test or report effects across the full range of the 14 game dimensions**—interactions and nonlinearities are often theorized but rarely empirically validated.
- **Broad conceptual/theoretical reviews abound, but these provide limited actionable guidance for quantitative efficiency prediction.**
- **Contextual factors including ecological resource dynamics, cultural/cognitive context, and evolved strategy sets** may constrain generalization from lab to field or across populations.

---

## In summary

- **The literature supports both positive and negative effects of punishment on efficiency, with net-negative impacts more common in classic peer-punishment PGGs and net-positive in institutional/externally monitored settings.**
- **Key modulating dimensions:** punishment cost/type, MPCR, group size, anti-social punishment prevalence, reputation mechanisms, and resource/ecological context.
- **Most papers emphasize that increased cooperation in the presence of punishment does NOT guarantee efficiency gains; the costs of administering punishment can and often do overwhelm benefits.**
- **The greatest uncertainty in predicting efficiency change lies in those regions of design space where punishment is neither tightly constrained (institutionalized, refereed) nor so costly as to be rarely used.**
- **Prediction should proceed with explicit modeling of punishment costs and observed control efficiency, with only modest expected efficiency gains—and sometimes losses—when enabling peer punishment in standard PGG configurations.**
