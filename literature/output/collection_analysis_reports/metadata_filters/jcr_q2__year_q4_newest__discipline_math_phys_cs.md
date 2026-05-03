# 1) Evidence Base

This paper set comprises 57 studies, with a strong mix of **theoretical/simulation** and **empirical (mainly experimental)** research. There are multiple exact-relevance laboratory experiments and a substantial number of simulation-based theoretical studies that target public goods games (PGGs) and their variants. The breadth of public goods game structures, network topologies, and sanction mechanisms is high, making the set broadly representative for PGG-like scenarios featuring peer punishment. There is a concentration of papers reporting explicitly on **efficiency or group payoff** (the primary prediction outcome), but many others focus on **behavioral cooperation outcomes** without reporting efficiency, or analyze adjacent games (e.g., Prisoner’s Dilemma, trust games) or settings (risk-dilemma, resource exchange).

Among the best-resourced dimensions are **punishment mechanism type and cost, network structure, and synergy/marginal return (MPCR)**. Some empirical laboratory studies (e.g., Pi et al., 2022; Wang & Huang, 2022) provide strong direct evidence for the prediction task. However, many theoretical/simulation and conceptual papers analyze mechanisms or behavioral responses without reporting payoff-based outcomes or use game structures that are only adjacent to the canonical PGG.

# 2) Task Relevance

**pgg_or_variant:**  
- **Exact**: Approximately 15–20 papers model or experimentally test standard or spatial public goods games directly.
- **Close/Adjacent**: Many others address variants (e.g., collective risk dilemma, voluntary public goods, hierarchical trust games), or adjacent multi-agent dilemmas (Prisoner's Dilemma, donation games).

**punishment_or_sanctions:**  
- **Exact**: A large subset examines peer punishment or institutional punishment as a primary manipulated variable.
- **Close/Adjacent**: Some papers only study reward/incentive, exclusion, or network-based sanctioning; a few analyze punishment in adjacent games/settings, or consider only behavioral forms (e.g., partner switching as “punishment”).

**efficiency_or_related_payoff_outcome:**  
- **Exact/Close**: Roughly ten papers provide direct payoff or efficiency data in the PGG or a direct variant (e.g., Pi et al., 2022; Wang & Huang, 2022; Sun et al., 2025; Cui et al., 2022; Yang & Yang, 2024).
- **Adjacent/Weak**: Many others measure only **behavioral outcomes** (contribution rates, cooperation frequencies) and do not report efficiency or group payoff as a primary outcome, requiring inference or caution for use in efficiency prediction.
- **None**: Some conceptual or bibliometric/context papers do not report any relevant outcomes.

# 3) Outcomes Measured In The Literature

- **Payoff-based outcomes** (directly aligned with "efficiency"):  
  - Group or average payoff (Pi et al., 2022; Wang & Huang, 2022)  
  - Explicit efficiency ratios (Sun et al., 2025)
  - Welfare, surplus, or group earnings (Yang & Yang, 2024)
  - Some theory/simulation papers directly map out efficiency over design parameters (Cui et al., 2022)

- **Behavioral outcomes** (not efficiency):  
  - Contribution rate, cooperation rate, strategy prevalence/clustering, norm compliance  
  - Punishment/reward frequency, sanction assignment  
  - Success in collective-risk tasks or group achievement (Hua & Liu, 2023; Yan et al., 2024)

- **Adjunct/indirect outcomes:**  
  - Stability of cooperation  
  - Oscillations/variability in group performance  
  - Persistence of defectors/punishers

Most relevant to the prediction task are the direct efficiency/payoff outcomes; however, these are less frequently reported than behavioral figures.

# 4) Main Findings Relevant To Prediction

## Effects of Peer Punishment on Efficiency

- **Enabling peer punishment generally increases group efficiency in standard and spatial PGGs**, especially relative to a control where punishment is disabled (Wang & Huang, 2022; Cui et al., 2022; Pi et al., 2022). The effect is robust to various settings, but not universal.
- **Conditionality and structure matter:**  
  - **Network topology**: Efficiency gains are magnified in spatial or small-world networks with the right structure (Cui et al., 2022). Incomplete punishment networks (e.g., circle, pairwise) can outperform complete networks; more potential punishers can reduce effectiveness and efficiency due to bystander effects (Pi et al., 2022).
  - **Synergy factor/MPCR**: Punishment’s positive effect is stronger when the marginal per-capita return is not too low (Sun et al., 2025; Yang & Yang, 2024).
  - **Punishment cost**: The efficiency benefit is maximized when punishment is not too costly; very costly punishment may dampen or even reverse efficiency gains (Sun et al., 2024; Pi et al., 2022).
  - **Redistribution of fines**: If fines from punishment are redistributed to cooperators/punishers, efficiency losses due to costly punishment can be offset, sometimes improving efficiency over no-punishment baselines, especially when punishment is expensive (Sun et al., 2024).

- **Combined punishment-reward mechanisms**:  
  - The combination of peer punishment and reward (institutional or peer) generally leads to **even higher efficiency** than punishment alone, but effects are sensitive to how rewards are allocated (Sun et al., 2025; Yang & Yang, 2024; Shen et al., 2022).

- **Parameter sensitivity and exceptions**:  
  - When punishment is inefficient (high cost, low impact), or implemented poorly (e.g., support rewards to punishers instead of cooperators), efficiency can be reduced or remain no better than control (Shen et al., 2022; Pi et al., 2022).
  - Some models with non-linear or threshold effects show that punishment only helps above certain parameter values (Xiao et al., 2023).
  - Empirical group variability: Some groups in experiments achieve high efficiency with punishment enabled; others less so (Wang & Huang, 2022).

# 5) Prediction Guidance

**Direct prediction should use payoff-relevant findings from exact-relevance PGG studies.**

- **If the control PGG efficiency is low or moderate** (i.e., contribution rates and hence group payoffs are well below fully cooperative levels), **enabling peer punishment will, in most cases, increase average group efficiency** (Wang & Huang, 2022; Pi et al., 2022; Cui et al., 2022).
- **The effect size will depend strongly on:**
  - **Punishment cost and magnitude** (low-cost, high-impact punishment maximizes efficiency gain; very costly punishment may negate gains).
  - **Network structure and punishment technology (punishment_tech)**: Incompletely networked punishment can yield better efficiency than globally enabled punishment due to bystander/bystanding effects (Pi et al., 2022).
  - **MPCR (mpcr)**: Higher MPCR supports more efficient punishment benefits; below certain thresholds, even punishment may not yield high efficiency.
  - **Presence and allocation of rewards** (reward_exists, reward_cost, reward_tech): Reward combined with punishment, especially when reward is directed at cooperators rather than punishers, reliably raises efficiency (Sun et al., 2025; Yang & Yang, 2024; Shen et al., 2022).
  - **Fine redistribution**: If costly punishment is offset by redistributing fines, net efficiency can be improved (Sun et al., 2024).

**Behavioral outcomes (cooperation rates, contribution frequencies) are indicative but should not be treated as efficiency.**  
If quantitative efficiency data are not available for a design, only qualitative directionality can be predicted with confidence.

**Prediction across missing dimensions (e.g., chat, default_contrib, show_punishment_id) should be conservative** due to sparse evidence.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed:**
- `player_count` (group size): Reported and manipulated in most PGG studies.
- `num_rounds`: Present in experimental and theory models; often 10 or more.
- `all_or_nothing`: Explicit in papers distinguishing continuous vs. binary contribution games.
- `mpcr`: Central design variable; closely tied to observed effect sizes.
- `punishment_cost`, `punishment_tech`: Key manipulated dimensions in both lab and simulation studies.
- `reward_exists`, `reward_cost`, `reward_tech`: Informed in several theory/simulation papers with institutional/peer reward.
- `punishment_exists`: All main studies manipulate this.

**Indirectly or contextually informed:**
- `show_other_summaries`, `show_n_rounds`: Occasionally discussed for feedback or information treatments affecting behavior, but rarely linked to efficiency effects.
- `punishment_magnitude` (impact per cost): Sometimes parameterized, but not always distinguished from cost.
- `num_rounds` and `player_count` interaction: Well-studied for dynamics, less so for efficiency as a function of horizon.
- `all_or_nothing`, `default_contrib_prop`: Occasionally present, especially in studies of threshold or binary-contribution games.

**Sparse or missing:**
- `chat`: Rarely present in these studies—real-time or asynchronous communication is almost never permitted or manipulated, so effect is unknown.
- `default_contrib` (framing): Largely unstudied—few if any studies manipulate default framing.
- `show_punishment_id`: Whether punishers are anonymous or public is seldom the focus, except in peer-network structure studies (and even there, not reported for efficiency).
- `reward_magnitude`: Not consistently separated from reward cost or reward type; gaps in precision.
- **Interaction effects among dimensions**: Most studies focus on one or two manipulated parameters, limiting evidence for interaction effects (e.g., how punishment cost interacts with network structure and number of rounds).

# 7) Important Limitations

- **Limited direct empirical (lab-experimental) efficiency data for all possible combinations of design dimensions**; most payoff-based findings are in theory/simulation or limited fixed-lab designs.
- **Sparse coverage for some design dimensions**, especially communication (`chat`), default framing (`default_contrib`), and visibility of punisher identity (`show_punishment_id`), making predictions along these axes speculative.
- **Many studies report only behavioral outcomes** (contribution or cooperation rates), requiring cautious inference when predicting efficiency.
- **Over-representation of spatial and network models in theory/simulation studies**; may overstate network effects compared to real lab PGGs.
- **Institutional vs. peer punishment effects may not fully generalize**; some theoretical results require central funding/tax mechanisms, which differ from peer-based lab designs.
- **Sensitivity to parameter values may produce non-monotonic or threshold effects**; not all studies provide clear parameter boundaries where efficiency increases or decreases.
- **Antisocial punishment and second-order freeriding are often under-studied in terms of efficiency** (except Pi et al., 2022, which documents antisocial punishment but does not fully quantify net efficiency impact).
- **Adjacency of some game structures** (Prisoner’s Dilemma, trust games, risk dilemmas) limits the applicability of those results to standard PGG efficiency predictions.
- **Few studies jointly manipulate or report the full set of prediction dimensions**; interaction effects remain poorly characterized.

---

**In sum:**  
Prediction of treatment (punishment-enabled) efficiency in PGG-like environments should be grounded in direct empirical and simulation-based findings, giving strong weight to core design parameters—player count, number of rounds, MPCR, punishment cost, and punishment network structure—while being cautious or agnostic where evidence is sparse (e.g., chat, default framing, punishment identification). The default expectation, based on the strongest evidence, is that **enabling peer punishment increases group efficiency (relative to control with punishment disabled), provided punishment is not prohibitively costly and the network/channel for punishment is not counterproductively configured**. However, specific design features and high punishment cost can modulate or reverse this effect. Gaps remain for lesser-studied design dimensions and for contexts where only cooperation rates, rather than efficiency, are reported.
