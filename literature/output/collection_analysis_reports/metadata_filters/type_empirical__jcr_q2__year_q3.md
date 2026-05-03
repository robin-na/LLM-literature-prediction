# 1) Evidence Base

The paper set consists overwhelmingly of empirical laboratory experiments, with some field and framed field studies, and only a few observational or survey-based analyses. Most papers use canonical or closely related repeated linear public goods games (PGGs), often directly manipulating punishment mechanisms (peer, centralized, exogenous, endogenous, delayed, visible, etc.), and measuring outcomes over 10-30 rounds in groups of 3-6 players. The breadth of this evidence base is notable: there is a substantial number of studies (121), many of which report both control (no-punishment) and treatment (punishment-enabled) conditions, with clearly specified game design parameters.

For the target downstream prediction task, the evidence base is strong and directly relevant for the core scenario: repeated linear PGGs, group sizes 3-5, standard MPCR (0.4–0.6), no chat, continuous contributions, punishment cost-to-impact ratios in the 1:3–1:5 range. There is also useful heterogeneity: studies vary institutional features, cultural context, information structure, network topology, composition, and additional mechanisms (reward, endogenous institutions, exclusion, etc.). However, coverage is thinner for more complex or less standard parameter combinations (e.g., large groups, very high or low MPCR, dynamic CPRs, threshold goods, multi-channel punishment, or games with multiple institution types or partner selection).

The majority of findings are empirical and based on observed efficiency or payoff data, but theory-based, mechanism, and qualitative arguments are also present, especially as moderators or explanations for heterogeneity and null/mixed results.

# 2) Task Relevance

**pgg_or_variant**:  
- **Relevance**: **exact**
- The bulk of the literature centers on standard or close-variant PGGs, with well-matched institutional features and design dimensions; deviations (e.g., CPRs, threshold goods, partner choice) are mostly marked as "close" or "adjacent" and are synthesized separately as such.

**punishment_or_sanctions**:  
- **Relevance**: **exact**
- Most experiments manipulate the presence, type, or structure of punishment mechanisms, including classic peer punishment, third-party punishment, centralized punishment, exclusion, and automatic or probabilistic sanctions. Papers frequently compare punishment-enabled to punishment-disabled conditions, making the evidence directly applicable.

**efficiency_or_related_payoff_outcome**:  
- **Relevance**: **exact/close**
- Many papers directly report efficiency (defined as average group payoff relative to the fully cooperative optimum) or closely related measures (total earnings, social welfare, group profit, surplus). Some measure only average contributions or norm compliance, which are not strictly efficiency but can often be interpreted directionally or indirectly.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes**:  
- **Directly measured in a large number of studies:**  
  - Group efficiency (payoff ratio normalized to social optimum), total group earnings, average earnings per round/player, group profit, welfare/surplus, tokens generated.
- **Indirectly measured or inferred in some cases:**  
  - Improvement in payoffs over control, difference-in-differences (treatment vs. no-punishment), or subgroup comparisons (by institution, group type, culture, etc.).

**Non-payoff behavioral outcomes**:  
- **Frequently reported, but distinguished from efficiency:**  
  - Contribution rates, cooperation rates, frequency and magnitude of punishment assigned, antisocial punishment, norm compliance, perceptions of fairness or trust, belief elicitation, norm enforcement behaviors.

**Distinctions maintained in synthesis**:  
- Many studies show increased contributions without efficiency gains (when punishment costs outweigh the gains from greater provision), and others show efficiency gains only in particular institutional or informational contexts.

# 4) Main Findings Relevant To Prediction

Synthesizing across directly relevant empirical studies (and distinguishing payoff from non-payoff findings):

**a. Enabling punishment increases efficiency in most standard PGGs.**
- In canonical repeated linear PGGs with peer or centralized punishment options and moderate MPCR, enabling punishment leads to higher average group net payoffs compared to no-punishment baselines—often substantially so (e.g., Arechar et al., 2018; Gürerk et al., 2018; Engl et al., 2021; Fatas et al., 2020; Angelovski et al., 2018).
- The increase is most robust when punishment is effective (cost:impact ratio high), pro-socially targeted (mainly at defectors), and the frequency of antisocial punishment is low.

**b. The efficiency effect of punishment depends critically on game design dimensions and context. The most important empirical moderators include:**
  - **Punishment cost and technology:** Efficiency gains occur when punishing is not too costly (e.g., 1:3 or better cost:impact), when punishment is well-targeted, and especially when multiple punishment channels (e.g., observed plus unobserved) are available (Glöckner et al., 2018).
  - **Group composition and antisocial punishment:** The presence of anti-social punishers, group heterogeneity (especially ethnic or status division), and norm disagreement can strongly reduce or reverse the efficiency effect (Bruhin et al., 2020; Mantilla et al., 2021; Vollan et al., 2019).
  - **Information structure:** Punishment's beneficial effect on efficiency relies on the ability to identify and target true defectors. With incomplete information (e.g., private endowments), punishment can misfire, reducing efficiency (De Geest & Kingsley, 2019, 2021).
  - **Punishment institution selection:** Endogenous (voted) institution adoption sometimes increases efficiency, as it aligns with group preferences and legitimacy, but the effect size is not always larger than exogenous implementation (Marcin et al., 2019; Cobo-Reyes et al., 2019; Dannenberg et al., 2020).
  - **Network structure:** The benefit of punishment for efficiency is realized in certain network topologies (star, complete), but can be negative in others (line, circle), mostly due to retaliation and antisocial punishment dynamics (Fatas et al., 2020).
  - **Emotional or cultural context:** Inducing happiness versus anger, or cross-cultural differences in antisocial punishment, can flip the efficiency effect of punishment from positive to neutral or negative (Lee & Min, 2021; Bruhin et al., 2020).

**c. Enabling punishment does not always increase efficiency:**
- When punishment is misdirected (due to incomplete information), antisocial, group composition is problematic, or the cost is too high, efficiency gains disappear or even reverse (Glöckner et al., 2018; Mantilla et al., 2021; Bruhin et al., 2020; De Geest & Kingsley, 2019).
- In some designs (e.g., threshold games with costly punishment, all-or-nothing contributions), punishment may increase contributions but not net payoffs, especially if the costliness or structure of punishment produces high welfare losses (Vollan et al., 2019; Robbett, 2019).

**d. The magnitude of the efficiency gain is moderated—not just its direction:**
- The size of the improvement is larger when baseline (control) efficiency is low and design/behavioral features favor pro-social, low-cost, well-targeted punishment. Small or negligible if baseline is already high, or when punishment adds little deterrence relative to cost.

# 5) Prediction Guidance

**What does the literature imply for prediction of average efficiency in punishment-enabled PGGs, given design dimensions and control efficiency?**

- **Baseline or control efficiency (no-punishment) is a strong predictor:** Most PGGs with low control efficiency yield larger improvements when punishment is enabled, assuming punishment is effective and pro-socially targeted. In environments where control efficiency is already high, adding punishment delivers smaller and sometimes negligible additional gains (Arechar et al., 2018; Gürdal et al., 2021).
- **Incorporate key design dimensions as moderators:** Design features (see section 6) must be explicitly modeled, as their empirical moderating effects on the punishment-efficiency relationship are substantial and well documented.
    - If **punishment cost is low** and **punishment is pro-social** in a symmetric, homogeneous group with full information, **expect a marked efficiency gain** (often 10–40 percentage points).
    - If **punishment cost is high**, **group is heterogeneous or prone to antisocial punishment**, or **relevant information is hidden**, **expect a weak, null, or negative efficiency effect**.
- **In cases with endogenous institution adoption (voting):** Efficiency gains may be larger when institution selection is endogenous, but the difference is modest and not uniformly observed.
- **Special structural cases:** In threshold (all-or-nothing) games or those with costly exclusion, efficiency gains may be present if exclusion is costless, but disappear or reverse if exclusion or punishment is costly to all (Dannenberg et al., 2020).
- **Do not use non-payoff behavioral measures as proxies for efficiency unless justified:** Many studies show increased contributions with no net efficiency gain (due to punishment costs offsetting benefits). Only use payoff or efficiency outcomes for prediction calibration.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed by evidence (i.e., systematically varied with clear outcome data):**
- **player_count (group size):** Effects are directly estimated in PGGs with 3–5, and some up to 10, with robustness shown; network topology and large group heterogeneity further explored in specialized studies (Fatas et al., 2020; Kamei, 2020).
- **num_rounds:** Most experiments use 10–30 rounds, and evidence shows that efficiency effects of punishment are robust over repeated interactions; dynamics matter for decay or increase in contributions/efficiency.
- **mpcr (marginal per-capita return):** A key moderator; efficiency gains from punishment are stronger at moderate MPCR (0.4–0.6); less data on very low/high MPCR.
- **all_or_nothing (contribution structure):** Some evidence (e.g., Marcin et al., 2019) from binary/all-or-nothing designs, showing similar directions but sometimes smaller/more volatile treatment effects.
- **punishment_cost, punishment_tech:** Empirically rich; varies cost:impact ratios, centralization/decentralization, visibility, immediacy, and mechanisms—strong evidence for their moderating roles.
- **chat (communication):** Strongly supported; chat amplifies efficiency, can substitute or complement punishment (Koch et al., 2021; Arechar et al., 2018).
- **show_other_summaries, show_n_rounds:** Commonly manipulated; full information conditions favor efficient punishment; lack thereof can lead to mis-targeting and inefficiency (De Geest & Kingsley, 2019, 2021).

**Indirectly or contextually discussed, with partial or inferred evidence:**
- **default_contrib (contribution framing):** Not a central variable in most analyses, but some evidence that framing (give vs. take) moderates contribution and sometimes efficiency effects (Ramalingam et al., 2019).
- **reward_exists, reward_cost, reward_tech:** Some studies contrast reward and punishment, showing that rewards can also increase efficiency, sometimes more than punishment if designed to be payoff-increasing (Gürerk et al., 2018).
- **show_punishment_id:** Discussed in the context of punishment visibility and social image but less systematically manipulated.

**Effectively missing or rarely tested:**
- **num_rounds** outside the typical lab range, large or dynamic group sizes, structural variations (e.g., variable network topologies, dynamic CPRs), and highly asymmetric endowment or MPCR settings.

# 7) Important Limitations

- **Limited coverage outside standard lab PGGs:** Most evidence is for small groups, moderate MPCR, and repeated play. Predictions for large groups, one-shot, or highly dynamic settings require caution.
- **Sparse direct data on certain design dimensions:** Some prediction dimensions (e.g., show_punishment_id, reward_tech, or very low default_contrib) are seldom manipulated independently, so conclusions for these are indirect.
- **Context dependence and interaction effects:** Multiple empirical moderators (culture, group composition, information, network) can sharply change the punishment-efficiency relationship, sometimes overwhelming the main effect.
- **Anti-social punishment as a key risk:** Environments with high rates of anti-social punishment frequently see neutral or negative efficiency effects, and group/cultural composition is not always easily observable or predictable ex ante.
- **Behavioral measures ≠ payoff outcomes:** Several studies report only or mainly contributions or norm compliance, which do not correspond 1:1 to efficiency, especially when punishment costs are high.
- **Results may not extrapolate to field or real-world settings:** Field or observational studies suggest real-life punishment is less commonly used and sometimes less effective than in lab settings; application outside the lab requires caution (Qirko, 2020; Vollan et al., 2019).

---

**In summary:**  
The literature set provides a strong empirical foundation for predicting efficiency in repeated PGGs when peer punishment is enabled versus disabled, conditional on control efficiency and key design dimensions. Most design parameters—group size, rounds, MPCR, punishment cost/tech, communication, and information—are directly and robustly evidenced as moderators. The consensus is that, under standard conditions, enabling punishment increases efficiency, but this effect is highly contingent on cost-effectiveness, norm targeting, group composition, and information structure. For reliable prediction, models should explicitly account for these dimensions and moderators, and avoid extrapolation to under-evidenced regimes or non-laboratory settings without further validation.
