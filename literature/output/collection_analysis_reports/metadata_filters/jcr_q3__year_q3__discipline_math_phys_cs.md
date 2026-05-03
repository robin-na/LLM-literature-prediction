# Evidence Base

The analyzed paper set (32 papers) is composed entirely of theoretical (modeling and simulation-based) studies with no empirical (experimental or field) components. The evidence base is broad in covering a wide spectrum of public goods game (PGG) variants and adjacent social dilemmas, but theoretical rather than empirical. Most models explore peer punishment, institutional punishment, or related interventions in PGGs or close analogues; a substantial number also incorporate adjacent social dilemmas (e.g., trust games, prisoner's dilemma) or relevant social structures (hierarchies, networks, spatial populations). Close to half of the papers focus directly on efficiency or related payoff outcomes, while the rest emphasize behavioral outcomes (e.g., cooperation rates) or structure (e.g., network composition).

# Task Relevance

**pgg_or_variant**:  
- **Exact relevance**: About half of the papers model standard or continuous PGGs (Jiao et al., 2020; Fang et al., 2020; Wang & Lv, 2019; Huang et al., 2018; Flores et al., 2021; Greenwood et al., 2018; Chen et al., 2018), making them directly relevant.
- **Close/adjacent relevance**: Several examine threshold public goods, trust games, mutual-aid games, or other n-person social dilemmas (Perry et al., 2018; Couto et al., 2020; Nakamaru et al., 2018; Shimura & Nakamaru, 2018).
- **Weak/none**: A few are only tangentially related (e.g., security games, Bianchi et al., 2020); these provide no or weakly adjacent evidence.

**punishment_or_sanctions**:  
- **Exact relevance**: Many studies directly manipulate or model the presence, cost, and structure of punishment (Jiao et al., 2020; Fang et al., 2020; Wang & Lv, 2019; Huang et al., 2018; Greenwood et al., 2018; Perry et al., 2018).
- **Close/adjacent**: Others consider reward mechanisms, reputation-based redistributions, or informal sanctions, which are adjacent (Du et al., 2018; Wei et al., 2021; Fang & Chen, 2021).
- **Weak/none**: Some model no punishment but may include indirect analogues (e.g., opt-out, partner loss).

**efficiency_or_related_payoff_outcome**:  
- **Exact relevance**: A subset report average group payoff, welfare, mean efficiency in formal terms (Jiao et al., 2020; Wang & Lv, 2019; Huang et al., 2018; Murase & Baek, 2018).
- **Close/adjacent**: Several use group effort, sum of contributions, or average payoff for a subset of strategies as proxies (Flores et al., 2021; Chen et al., 2018; Perry et al., 2018).
- **Weak/none**: Many papers report only contribution rates, cooperation frequencies, or network outcomes without payoff measurement.

# Outcomes Measured In The Literature

- **Payoff-related outcomes (directly measured):**
  - Group efficiency and mean payoff (ratio of group total payoff to the fully cooperative benchmark)
  - Explicit group total earnings or welfare (Jiao et al., 2020; Wang & Lv, 2019; Huang et al., 2018; Perry et al., 2018; Murase & Baek, 2018)
  - Explicit average payoffs to player types or the group

- **Proxies or adjacent payoff outcomes:**
  - Total sum of contributions (often in spatial/networked PGGs)
  - Average payoff to a subset of players (e.g., cooperators only)
  - Group “achievement” often synonymized with public good success

- **Non-payoff behavioral outcomes:**
  - Contribution or cooperation rates
  - Strategy frequencies (e.g., fraction of punishers)
  - Network structure or dynamics (e.g., clustering, rewiring)
  - Norm compliance, reputation scores

**It is important to note** that behavioral outcomes (e.g., cooperation rate) are not equivalent to efficiency, and in several cases, increases in cooperation do not straightforwardly translate to increases in group payoff, especially when punishment is costly.

# Main Findings Relevant To Prediction

- **Enabling punishment typically increases group efficiency and mean payoff** in standard and continuous PGGs, but only when punishment is not excessively costly compared to the fines inflicted and is executed at an optimal probability; indiscriminate or always-on punishment can be detrimental if costs are high (Jiao et al., 2020; Wang & Lv, 2019; Huang et al., 2018).
- **Effectiveness is highly parameter dependent:** The relative cost and magnitude of punishment (punishment_cost & punishment_tech) are key. Effective punishment (high fine per cost or low punishment cost) reliably increases efficiency; high cost or low effect may reduce efficiency even as cooperation increases (Fang et al., 2020; Greenwood et al., 2018; Perry et al., 2018).
- **Network and spatial structure moderate effects:** Spatial structure can allow symbiosis between cooperators and punishers, expanding the viable parameter range for positive efficiency effects (Flores et al., 2021), but sometimes at intermediate or high costs spatial structure reduces efficiency gains compared to well-mixed settings (Wang & Lv, 2019).
- **Thresholds and conditionality:** There is frequently a threshold of punishment effectiveness or prevalence of punishers needed to shift the equilibrium; failing to meet this threshold means punishment does not improve or even reduces efficiency (Greenwood et al., 2018).
- **Institutional and graduated punishment:** Institutional or graduated forms of punishment (fine and/or cost rising with defector count) are generally more effective at achieving high efficiency than strict, fixed-cost punishment, especially in risky or threshold public goods games (Couto et al., 2020).
- **Corruption and second-order problems:** Corruption can undermine the efficiency benefits of punishment regimes; mechanisms for corruption control, or strong performance-based incentives for punishers, mitigate this risk (Fang et al., 2020; Huang et al., 2018).
- **Reward mechanisms:** Reward, when modeled, is often more effective or at least as effective as punishment for increasing both cooperation and group payoff; combinations sometimes perform best, particularly probabilistic implementations (Jiao et al., 2020; Fang & Chen, 2021).

# Prediction Guidance

- **Design dimensions directly relevant for prediction include**: player_count, num_rounds, mpcr, punishment_cost, punishment_tech, and to a lesser extent (when modeled) all_or_nothing, reward_exists, reward_cost, reward_tech, and features of network structure (explicit or implicit in structured populations).
- **Given a well-calibrated control efficiency** (i.e., efficiency with punishment disabled), the introduction of peer punishment should generally be expected to increase treatment efficiency if:
  - Punishment cost is not excessive and fine per unit cost is high;
  - Punishment is either deterministic or, preferably, probabilistic with an optimal execution probability (Jiao et al., 2020);
  - Shared cost and/or institutional design prevent excessive burden on punishers (Wang & Lv, 2019);
  - Corruption is controlled or absent, or punisher incentives are performance-based (Fang et al., 2020; Huang et al., 2018).

- **However**, enabling punishment may not increase (and can reduce) efficiency if:
  - Punishment cost is higher than the inflicted fine (i.e., inefficient punishment);
  - There is widespread corruption or bribery without effective countermeasures;
  - Network or group structure places excessive burden on a few punishers;
  - The fraction of punishers in the population is below a threshold (Greenwood et al., 2018);
  - Indiscriminate or always-on punishment is used at high cost levels;
  - Defectors can undermine or evade punishment (second-order free-rider problem).

- **Quantitative prediction**: The literature provides qualitative and sometimes explicit mathematical relationships between efficiency, group size, punishment cost, and fine, but not empirical calibration. The direction (increase or decrease) can usually be inferred; magnitude likely requires case-specific modeling.

# Design Dimensions Highlighted Across Papers

**Directly Informed:**
- `player_count` (group size): Modeled in nearly all core theory papers; effects often nonlinear.
- `mpcr` (marginal per-capita return): Central to nearly all efficiency analyses.
- `punishment_cost` and `punishment_tech` (fine per cost): Frequently explicit, almost always modeled in relevant papers.
- `reward_exists`, `reward_cost`, `reward_tech`: Directly modeled in a minority (Jiao et al., 2020; Fang & Chen, 2021; Du et al., 2018), mostly in combination with punishment.
- `all_or_nothing`, `num_rounds`: Recurrent, with evidence for their moderating role.
- `show_other_summaries` and `show_n_rounds`: Sometimes modeled (e.g., reputation, listing), but less frequently with direct link to efficiency.

**Indirectly Informed/Contextually Discussed:**
- `chat`, `default_contrib` (contribution framing), `show_punishment_id`: Rarely or never modeled directly; occasionally mentioned in context but without outcome data.
- `punishment_tech` in the sense of "technology" (i.e., efficacy, ability to target, restricting collateral impact) is usually absorbed into cost/fine parameters rather than as a separate entity.
- `show_n_rounds` and `show_other_summaries` are relevant for reputation or information transmission models but not as primary variables in efficiency analyses.

**Missing/Effectively Uninformed:**
- Explicit manipulation of `chat`, `default_contrib`, and `show_punishment_id` is generally absent.
- Empirical calibration (i.e., experimental or field data to relate parameter values to realized payoffs/efficiency) is entirely missing.

# Important Limitations

- **Absence of empirical data:** All evidence is theoretical or simulation-based; there is no direct empirical calibration.
- **Transferability limited:** Some highly parameterized results might not generalize to all environments, especially outside well-mixed or continuous-choice PGGs.
- **Sparse treatment of some dimensions:** Certain prediction features (chat, framing effects, choice disclosure, punishment identification) are not modeled.
- **Behavioral outcomes ≠ payoff outcomes:** Many studies report only cooperation rates or strategy frequencies; while correlated, these are not the same as efficiency—particularly when punishment is extremely costly.
- **Lack of fine-grained comparative statics:** While many models explore multi-dimensional parameter dependencies, most do not provide comprehensive mapping across all design dimensions; cross-dimensional interactions (e.g., chat × punishment) are underexplored.
- **Control efficiency not systematically linked:** Most papers focus on the mechanism with and without punishment per se, not on predicting outcomes from a known control efficiency baseline.
- **Potential optimism bias:** Theoretical models can sometimes assume optimal behavioral or institutional responses, which may not materialize in practice.
- **No evidence on framing, communication, or identity disclosure:** These dimensions, present in many experimental PGGs, lack modeled treatment here, reducing external validity if such features are present in the target prediction environment.

---

**In summary:** The theoretical literature provides clear, multidimensional qualitative (and sometimes explicit quantitative) evidence on when and how punishment increases or decreases average group efficiency in PGGs and close variants. Prediction should rely on punishment cost and effectiveness, group size, efficiency of sanctioning, and the possibility of corruption or second-order free-rider problems. However, some prediction-relevant dimensions (communication, framing, information disclosure) are unmodeled, and the lack of empirical validation is a key limitation. Predictions can be made with caution, mainly for stylized or well-understood environments matching the model assumptions in the literature.
