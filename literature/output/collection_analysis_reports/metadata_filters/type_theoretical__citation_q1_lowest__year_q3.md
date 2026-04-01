# 1) Evidence Base

**Type and Breadth:**  
The paper set consists entirely of theory and mathematical modeling works; there are no empirical or experimental studies in the digest. The overwhelming majority focus on formal game-theoretic, evolutionary, or simulation models, with a few conceptual or review pieces providing historical or philosophical context. The coverage is broad in the sense of spanning a variety of social dilemma models (public goods games (PGGs) and adjacent environments, including threshold PGGs, volunteer’s dilemmas, trust games, and networked resource-sharing games), but narrow regarding direct empirical validation and direct measurement of efficiency with and without peer punishment.  

**Empirical vs Theory:**  
All papers are theory-based; none present new experimental or field empirical evidence. Simulation-based findings (e.g., agent-based or evolutionary dynamics) are common, but experimental validation is absent. This should be considered a significant limitation for quantitative prediction tasks.

**Directness to Prediction Task:**  
A subset of the papers (notably: Alventosa & Olcina, 2021; Tanimoto, 2018; Gao et al., 2020; Botta et al., 2021; Zhang et al., 2019) directly analyze PGGs with punishment and efficiency outcomes. Many others provide closely related evidence from variants or adjacent paradigms (e.g., spatial or network PGGs, trust games, coalition games), or focus primarily on non-payoff behavioral outcomes (e.g., cooperation rates).

# 2) Task Relevance

**pgg_or_variant:**  
- **Exact:** The set includes multiple papers directly modeling standard linear PGGs or optional PGGs with core design dimensions (Alventosa & Olcina, 2021; Tanimoto, 2018; Gao et al., 2020; Botta et al., 2021; Zhang et al., 2019; Greenwood et al., 2018).
- **Close to Adjacent:** Many works analyze PGG variants (threshold games, spatial/networked PGGs, volunteer’s dilemmas, trust games) — generally sharing basic design similarities but sometimes introducing new mechanisms or different player dynamics (Friehe & Tabbach, 2018; Lancia & Russo, 2019; Mihm & Toth, 2020; Berger & De Silva, 2021).
- **Weak/None:** Several papers discuss only the broad class of social dilemmas (Prisoner’s Dilemma, trust games, or commons problems) or present high-level conceptual arguments.

**punishment_or_sanctions:**  
- **Exact:** Numerous studies implement explicit peer, institutional, or community punishment technologies as modeled treatments or endogenous variables (Alventosa & Olcina, 2021; Tanimoto, 2018; Gao et al., 2020; Botta et al., 2021; Zhang et al., 2019; Eldakar et al., 2018; Greenwood et al., 2018).
- **Close:** Punishment is often analyzed as one incentive alongside reward, or explored in adjacent forms (third-party, institutional, or collective).
- **Adjacent/Weak:** Many papers incorporate only informal sanctions (e.g., blame, exclusion, reputation loss), or treat punishment at the conceptual level without clearly matchable design parameters.

**efficiency_or_related_payoff_outcome:**  
- **Exact:** Several papers directly measure or theorize about group efficiency, total payoff, welfare, or coins generated in explicit contrast to the fully cooperative optimum.
- **Close:** Some papers measure total contributions or welfare proxies, or discuss payoff effects without providing efficiency as a formal outcome.
- **Adjacent/Weak/None:** Many focus only on behavioral outcomes (cooperation rate, contribution rate, fraction of cooperators) and do not provide payoff-based results; some discuss mechanisms that could, by logic, affect efficiency, but do not measure or simulate efficiency directly.

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes (Efficiency, Group Payoff, Welfare):**  
- A minority of papers provide explicit efficiency outcomes (group payoff relative to full cooperation), often as analytic model results or simulation outputs (e.g., Alventosa & Olcina, 2021; Tanimoto, 2018; Gao et al., 2020; Botta et al., 2021; Zhang et al., 2019; Gao & Liang, 2020).
- Some provide closely-related measures (aggregate group earnings, utility, or surplus) or formal conditions under which full efficiency can be achieved (Friehe & Tabbach, 2018; Mihm & Toth, 2020; Berger & De Silva, 2021; Lancia & Russo, 2019; Jindani, 2020).
- In several simulation or evolutionary models, efficiency is inferred from the steady-state group payoff or abundance of cooperators, but not always computed directly or contrasted against a fully cooperative baseline.

**Non-Payoff Behavioral Outcomes:**  
- The majority of models in the set (especially in adjacent or spatial games) focus on the fraction of cooperators, contribution rate, norm compliance rate, or the prevalence of particular strategies.  
- Some models focus on the conditions for the emergence, stability, or collapse of cooperation (e.g., thresholds, phase transitions, or basins of attraction).
- Where punishment is present, punishment frequency, assignment, and type (altruistic, selfish) are often reported but not always linked quantitatively to efficiency.

**Distinction Maintained:**  
The papers generally maintain clear distinction between payoff-based outcomes (group efficiency, welfare) and behavioral cooperation measures. However, some simulation-based works interpret increased cooperation as a proxy for higher efficiency, which may not be valid when punishment is costly (e.g., Tanimoto, 2018; Matsuzawa & Tanimoto, 2018).

# 4) Main Findings Relevant To Prediction

**Empirical Findings:**  
- **There are no direct empirical findings** (i.e., no new experimental or observed group efficiency outcomes with and without punishment). All conclusions are drawn from theory, modeling, or simulation.

**Theoretical/Simulation Evidence:**  
- *Punishment can increase both cooperation and efficiency*: Core models show that when punishment parameters (low cost, high impact) and willingness to punish are favorable, enabling punishment moves the system towards full-cooperation/manimum-efficiency outcomes (Alventosa & Olcina, 2021; Gao et al., 2020; Botta et al., 2021; Zhang et al., 2019; Gao & Liang, 2020).
- *The effect on efficiency is context-dependent*: The cost of punishment can consume payoffs, meaning that, in many conditions (especially with peer punishment), efficiency may be lower even as cooperation rates rise (Tanimoto, 2018). Only highly effective, low-cost punishment reliably increases efficiency (relative to the control).
- *Mechanism details matter*: Institutional/centralized punishment, collective/consensual punishment, and action-based punishment tend to be more effective in raising efficiency than peer or outcome-based punishment (Alventosa & Olcina, 2021; Friehe & Tabbach, 2018; Gao & Liang, 2020).
- *Game design dimensions as moderators:*  
  - **Player count & group size:** Effects vary; in well-mixed games, higher n makes efficiency harder to sustain (Greenwood et al., 2018), but in some mechanisms, larger groups can stabilize cooperation (Shimura & Nakamaru, 2018, though without punishment).
  - **Punishment cost and effectiveness:** Lower costs and higher punishment magnitudes improve efficiency gains (Tanimoto, 2018; Zhang et al., 2019).
  - **Information/monitoring structure:** More transparent or rich monitoring can either enhance or undermine punishment's effects, due to changes in deterrence and misapplication (Mihm & Toth, 2020; Berger & De Silva, 2021).
  - **Network and spatial structure:** Local punishment and game interaction support high cooperation; globalized structures may lead to fragility (Okada et al., 2021).
  - **Consensus thresholds and social norms:** Collective decision rules (lower consensus required, high preference for incentives) make effective punishment more likely, supporting higher efficiency (Gao et al., 2020; Gao & Liang, 2020).

**Exceptions and Ambiguities:**
- *Punishment can backfire* when costs are high, punishment is misdirected (e.g., antisocial or jealous punishment), or social/organizational structure fosters spite or retaliatory punishment rather than prosocial enforcement (Eldakar et al., 2018; dos Santos & Knoch, 2021; Matsuzawa & Tanimoto, 2018; Berger & De Silva, 2021).
- *Efficiency gains are not guaranteed*: In some models, punishment stabilizes cooperation but does not raise (or can even lower) group efficiency due to sanctioning costs, redundancy, and misapplied punishments (Tanimoto, 2018; Matsuzawa & Tanimoto, 2018; Bear & Rand, 2019).
- *Parameter dependencies*: Many models offer explicit (or computable) thresholds for population composition, punishment frequency, or consensus that must be met before efficiency gains appear (Greenwood et al., 2018; Botta et al., 2021).

# 5) Prediction Guidance

- **Usefulness for Prediction:**  
  The theoretical literature supports the *expectation that enabling punishment will generally increase or maintain efficiency in PGGs relative to the same game without punishment*, when punishment is effective (low cost, high impact), well-targeted (at defectors), and misapplication is rare.
  
- **Degree of Certainty:**  
  Predictions must remain conditional—punishment's effect on efficiency is highly moderated by game design dimensions:
    - **Punishment Cost and Effectiveness:**  
      - *Lower cost and/or higher impact* raise the chances that enabling punishment will improve efficiency (Tanimoto, 2018; Zhang et al., 2019).
      - If punishment is costly with weak impact, *resource drain* may offset gains from higher cooperation (Tanimoto, 2018; Matsuzawa & Tanimoto, 2018).
    - **Type of Punishment:**  
      - *Centralized/institutional and collective punishment* mechanisms more reliably achieve efficiency (Alventosa & Olcina, 2021; Gao & Liang, 2020; Friehe & Tabbach, 2018).
      - *Peer punishment* can be effective only if enough players are willing/able to punish and social structure avoids antisocial punishment (Greenwood et al., 2018).
    - **Player Count and Group Structure:**  
      - In some designs, larger groups undermine effectiveness (Greenwood et al., 2018); others find robustness given repeated interaction or reputation (Jindani, 2020).
    - **Monitoring and Information:**  
      - Monitoring richness can either support (by aiding targeting) or undermine (by blunting the threat or fostering too-easy reputation manipulation) the efficiency effect (Berger & De Silva, 2021; Mihm & Toth, 2020).
    - **Consensus Mechanisms/Social Preferences:**  
      - Outcomes are enhanced if punishment is collectively decided with low consensus thresholds and high willingness to enforce (Gao et al., 2020).

- **Control Efficiency Baseline:**  
  Where the control PGG (no-punishment) already achieves high efficiency, *the marginal effect of punishment is often reduced*, and in some cases, introducing punishment may not justify its cost unless targeting is highly accurate and sanctioning rare but sufficient.

- **Translating to Prediction Input:**  
  - If design dimensions indicate strong, targeted, low-cost punishment and adequate monitoring, predict a meaningful *increase in average efficiency* in the punishment-enabled variant (relative to control efficiency).
  - If punishment is costly, misdirected, or subject to antisocial dynamics, predict a *smaller increase* or possibly *no change or a decrease* in efficiency—even if cooperation rates rise.
  - For ambiguous or partial implementations (weak or fractionally effective punishment, high player count with no network clustering, limited monitoring, or high consensus thresholds for sanction), predict *minimal effect* or *potential for negative side effects*.

- **Limitations of Quantification:**  
  The literature frequently gives only qualitative or relative effect sizes. Where analytic thresholds are provided, these depend on specific parameterizations that may not map simply onto any particular game design (Greenwood et al., 2018; Botta et al., 2021).

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**
- **player_count:** Incorporated in almost every relevant model (exact or close) and shown to moderate cooperation/effectiveness of punishment, though directionality varies.
- **num_rounds:** Modeled in repeated or evolutionary games, impacting stability and effectiveness of punishment.
- **mpcr:** Core to PGG models and a central moderator in all efficiency findings.
- **punishment_cost / punishment_tech:** Explicitly modeled in works focusing on punishment (cost/effectiveness tradeoff is central to almost all predictions).
- **all_or_nothing:** Most models state whether contributions are discrete or continuous; some findings depend on binary (volunteer’s dilemma/all-or-nothing) vs. graded contribution structure.
- **reward_exists, reward_cost, reward_tech:** Explored as possible alternatives or complements to punishment in several models (e.g., Gao & Liang, 2020; Chen & Chen, 2020).
- **show_other_summaries, show_punishment_id:** Discussed as information/monitoring variables in several models (Mihm & Toth, 2020; Berger & De Silva, 2021).

**Indirectly Informed or Contextually Discussed:**
- **chat:** Rarely present; only a small number of models (and those only adjacent) consider chat or communication.
- **default_contrib:** Little direct attention; some models with opt-in/out framing, but relevance is generally low.
- **show_n_rounds:** Sometimes affect patience (discount factor) in repeated games but not central.
- **show_punishment_id:** Typically proxied through monitoring and public observability, but not always an explicit design variable.

**Effectively Missing or Sparse:**
- **reward_magnitude:** Rarely parameterized explicitly.
- **Detailed mechanisms for fractional punishment or targeted identity-based punishment:** Only a few models (Botta et al., 2021; dos Santos & Knoch, 2021) simulate these mechanisms.
- **In-depth analysis of communication, framing, and social-norm compliance as design-levered variables:** Limited in the context of punishment’s direct impact on efficiency.

# 7) Important Limitations

- **Absence of empirical validation:** All findings are theoretical/analytical or from simulations; there is no tested empirical/experimental evidence relating design dimensions to observed efficiency changes.
- **Ambiguity in context dependence:** Many models reveal that identical punishment mechanisms can have variable effects on efficiency depending on group structure, monitoring/information, consensus rules, and the prevalence of cooperative/punishing types. Generalizability is thus limited.
- **Limited quantification of magnitude:** Most models report qualitative or relative directionality; only a subset provides analytic thresholds (and still only for stylized parameter choice).
- **Sparse coverage of some design dimensions (e.g., communication, framing, identity disclosure):** These are rarely modeled in a way directly mappable to prediction inputs.
- **Behavioral vs. payoff outcome conflation risk:** There is a risk in some literature (and for modelers using these findings) of inferring efficiency changes from observed cooperation or contribution-rate increases, which may be invalid if punishment is sufficiently costly or misapplied.
- **Adjacency rather than exact match:** Many findings are from adjacent game structures (threshold PGGs, spatial dilemmas, trust games) or rely on adjacent (not exact) operationalizations of punishment, which may limit translation to standard PGG prediction tasks.
- **Lack of field or heterogeneous-population validation:** Simulations rarely account for the diversity in willingness to punish, norms, or endogenous evolution of punishment strategies found in real-world or experimental groups.

---

**In summary:**  
The theoretical literature set robustly supports a *conditional* expectation that enabling peer or institutional punishment in PGG-like environments increases group efficiency *compared to no-punishment controls*, *when* punishment is sufficiently targeted, cost-effective, and well-monitored. The evidence is strong for identifying moderators and threshold effects across key dimensions—but these thresholds, tradeoffs, and magnitudes remain only qualitatively established, and only a subset of game design features are consistently and directly mapped in these models. Any quantitative prediction should preserve acknowledged context-dependence and parameter sensitivity, and avoid assuming gains where design dimensions indicate costly, poorly targeted, or easily misapplied punishment regimes.
