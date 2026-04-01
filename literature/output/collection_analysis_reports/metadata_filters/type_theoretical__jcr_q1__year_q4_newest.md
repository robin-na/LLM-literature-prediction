# 1) Evidence Base

This paper set is extremely broad and almost entirely theoretical (all items are theory or simulation), with no empirical or direct experimental studies. All findings, outcomes, and predictions stem from mathematical models, agent-based simulations, or conceptual analysis of public goods games (PGGs) and a wide array of close or adjacent social dilemma environments. There is substantial coverage of PGGs and variants (e.g., resource games, collective risk dilemmas, trust games, Prisoner’s Dilemmas), with a strong focus on how punishment and/or reward mechanisms affect behavioral and payoff outcomes. The set is rich in mechanism-level detail, mapping outcome changes to changes in game parameters relevant to prediction. However, almost every finding is theoretical, simulation-based, or conceptual, and no real-world or experimental payoff-based outcome data is included. The paper set is large and diverse but is generally narrow in that all studies are social dilemma games or close relatives.

# 2) Task Relevance

**pgg_or_variant:**  
- The literature is highly (mostly exact) relevant: The overwhelming majority of papers directly model PGGs or very close variants (resource games, trust games), with clear mappings to the classic PGG structure and dynamics.
- Some papers are “close” (collective-risk, CPR, group-structured PD, trust games), and a fraction are “adjacent” (dyadic/small-N PD, reputation, norm compliance, etc.).

**punishment_or_sanctions:**  
- Again, relevance is high: Most core papers explicitly analyze punishment or sanctioning mechanisms, often varying the strength, cost, or technology of punishment/reward. The rest are “close” (studying exclusion, reward, or correlated incentive regimes), or “adjacent” (norms, reputation, or other compliance mechanisms).

**efficiency_or_related_payoff_outcome:**  
- About half of the highly relevant studies report average efficiency or directly comparable payoff/welfare/surplus outcomes (label: exact).
- Many papers report “close” payoff proxies (group payoff, welfare, mean payoff, surplus), though some focus only on contribution/cooperation rates (“adjacent”), which are not the target outcome.  
- Several papers in the set study only behavioral outcomes (contribution/cooperation frequency, norm adherence) and thus are “adjacent” or “weak”.

# 3) Outcomes Measured In The Literature

**Payoff-based outcomes:**
- Exact: Average group payoff compared to the group payoff at maximum cooperation (i.e., efficiency), group efficiency directly, welfare, surplus, or total coins/earnings.
- Close: Mean payoff, total surplus, long-run group revenue, resource sustainability (as a proxy for payoff), etc.

**Non-payoff behavioral outcomes:**
- Most papers also (or exclusively) measure:
  - Contribution rate, cooperation rate, prevalence of strategies (cooperate, defect, punish, reward), norm compliance, and stability of cooperation.
  - Frequency of punishment/reward, stability of pro-social institutions, or phase diagrams of strategy prevalence.

**Distinction and caution:**  
- Many findings for “cooperation rate” or “prevalence of punishment” must be interpreted with care: These may correlate with efficiency, but do not always do so, especially when punishment is costly.

# 4) Main Findings Relevant To Prediction

**General direction:**
- The majority of the (exact or close) payoff-based studies show that enabling punishment in PGGs (peer, pool, institutional, or hybrid forms) increases efficiency compared to the control (punishment-disabled), but only under certain parameter regimes:
  - **Positive or large effect**: When punishment is sufficiently cheap and/or effective (high fine-to-cost ratio), when the marginal per-capita return (mpcr) is moderate/high, and when the institution/technology for punishing is efficient or well-aligned with group structure (e.g., structured populations, tax-based or reputation-based centralized punishment). See (Li et al., 2022; Wang et al., 2024 Nature Comm; Wang et al., 2025 Chaos; Gao et al., 2024; Mohlin et al., 2023; Libois, 2022; Sun et al., 2023 IEEE; Nirjhor & Nakamaru, 2023 both papers).
  - **Mixed effect**: If punishment is too costly, too weak, or if the baseline (control) game is already efficient due to other mechanisms (network reciprocity, reward, exclusion, reputation), enabling punishment can have no effect or reduce efficiency (Bühren et al., 2023; Gao et al., 2024; Han et al., 2024; Han, 2022; Han et al., 2024; Liu et al., 2024; Wang et al., 2025 Chaos Solitons & Fractals).
  - **Negative effect**: In some cases, punishment increases cooperation but lowers payoffs/efficiency due to the direct cost of punishment, especially in peer-punishment or noisy environments (Han et al., 2024; Wu et al., 2022; Han, 2022).

**Critical moderators:**
- **Punishment cost and effectiveness**: There are always thresholds—a minimal effectiveness or maximal cost—below/above which punishment is ineffective or welfare-reducing.
- **Synergy/MPCR**: At low MPCR, punishment often fails to raise efficiency; at moderate/high, it can do so decisively, provided costs do not outweigh gains.
- **Player count/network structure**: Larger groups or networks with more connections often require more effective or centralized punishment. Structured networks permit local sanctions to be more effective; well-mixed populations make efficient punishment harder.
- **Reward versus punishment**: Several studies show that reward can sometimes reach similar (or higher) efficiency at lower cost, especially when noise or cost of punishment is high; hybrids (adaptive protocols, threshold responses) can be optimal (Sun et al., 2023 IEEE; Lu et al., 2024; Garrido et al., 2025).
- **Institutional design**: Tax-based or institutional punishment is generally more efficient than peer punishment, especially as player count and group complexity rise.
- **Initial conditions and path dependence**: Bistability is common; enabling punishment can produce high/low-efficiency equilibria depending on initial cooperation and willingness to punish (Liu et al., 2024; Liu et al., 2022; Han et al., 2024).

**Contextual conditions that hinder positive effects:**
- Corruption, antisocial punishment, low monitoring accuracy, or adaptive defector strategies may undermine or reverse benefits (Liu & Chen, 2022; Han et al., 2024; Chiba-Okabe & Plotkin, 2024).
- Excessively strong punishment (high cost or high standard for avoiding punishment) can crowd out voluntary cooperation and reduce welfare (Hernandez et al., 2022).

# 5) Prediction Guidance

## When the literature can directly inform prediction:
- For classic linear PGGs (and very close variants) with standardized or parameterized punishment, prediction should use the explicit threshold and equilibrium results in the literature.
- If control efficiency is low (much less than 1), and game parameters fall in the regime where punishment is not too costly and the fine (or exclusion) is effective, then enabling punishment will usually produce large efficiency gains (near social optimum).
- If control efficiency is already high due to other mechanisms, or if punishment is costly/ineffective, the marginal gain will be small or even negative.
- For adaptive or threshold-based institutions, or environments with feedback, the effect may depend on initial conditions and may feature bistability—both high and low efficiency are possible.
- In structured/heterogeneous networks, local or institutionally supported punishment is more effective up to the point where network complexity (or group size) overwhelms sanctioning capacity.

## When using information from non-payoff outcomes:
- Use with caution. Behavioral evidence on cooperation rates is sometimes, but not always, a good indicator of efficiency, especially in low/no-punishment cost settings.
- If punishment is cheap and increases cooperation, efficiency likely increases. If punishment is costly, it may not—raising cooperation can be offset or outweighed by punishment cost.

## Key moderators and missing dimensions for prediction:
- **Directly well-informed dimensions**:  
  - `player_count`, `num_rounds`, `mpcr`, `all_or_nothing`, `punishment_cost`, `punishment_tech`, `reward_exists` are richly covered with explicit model predictions.
- **Indirect or sparse dimensions**:  
  - `chat`, `default_contrib`, `show_n_rounds`, `show_other_summaries`, `show_punishment_id` are rarely parameterized explicitly.
  - `reward_cost`, `reward_tech` are less commonly varied, but included in some hybrid incentive studies.
- **Effectively missing**:  
  - No evidence based on outcome framing (`default_contrib`) or on communication effects (`chat` as a moderator of punishment efficacy).
  - Little to no information on transparency variables (`show_other_summaries, show_n_rounds, show_punishment_id`), except some mention of observability and learning.
  - No empirical calibration or effect sizes from laboratory/field experiments.

# 6) Design Dimensions Highlighted Across Papers

- **Best informed**:  
  - `player_count`: Multiple analyses link group size to punishment thresholds, network effects, and efficiency gains (Li et al., 2022; Wang et al., 2024; Zefferman, 2023).
  - `num_rounds`: Infinite vs. finite horizon, repeated vs. one-shot structure, and effects on institution/stability (Bühren et al., 2023; Liu et al., 2024).
  - `mpcr`: Universally treated; critical for thresholds, stability, and payoff outcomes.
  - `punishment_cost`, `punishment_tech`: Mapped to phase diagrams and explicit threshold conditions for the effect of punishment.
  - `reward_exists`/`reward_cost`: Explicitly modeled in multiple hybrid-incentive/threshold-incentive papers.
  - `punishment_exists`: Central by design for all included studies.

- **Less directly covered/sparse**:
  - `chat`, `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Only rarely manipulated or modeled.
  - `default_contrib`: Framing effects almost never explicitly included.
  - `reward_tech`: Sometimes covered in hybrid-incentive work, but less rigorously than punishment.

# 7) Important Limitations

- **No empirical or laboratory data**: All results are theoretical or simulated; predictions remain to be validated and parameterized in real settings.
- **Dependence on model assumptions**: Results may be sensitive to simplifying assumptions (e.g., infinite or very large populations, deterministic updating, perfect observability, symmetric costs).
- **Missing direct evidence for some dimensions**: Particularly for communication (`chat`), framing (`default_contrib`), transparency, and information structures.
- **Complexity and ambiguity in mixed or hybrid games**: Bistability, oscillations, and multi-strategy equilibria make point prediction challenging; initial conditions can matter greatly.
- **Potential for non-monotonic and negative effects**: In some parameter ranges, punishment increases cooperation but reduces efficiency due to cost (Han et al., 2024; Hernandez et al., 2022; Wu et al., 2022).
- **Adjacency or coverage gaps in novel or atypical game variants**: Extrapolation to less-standard PGG structures (e.g., opt-in/out, complex institutional features) may be poorly justified.
- **Overrepresentation of positive effects in institutional/centralized settings versus peer punishment**: When peer punishment is considered, negative/welfare-reducing effects are more common at realistic costs.

---

**In summary**:  
The paper set provides rich, theory-based guidance for predicting the effect of enabling punishment on efficiency in PGG-like environments under a wide range of game design dimensions—so long as those dimensions are well-parameterized in typical models (group size, returns, rounds, punishment cost/effectiveness). However, the guidance is almost entirely model-based, with little to no empirical validation. Prediction should be informed by the specific parameter regime and the character of the punishment mechanism, adjusting expectations for game features not well-represented in the models (notably communication, framing, and visibility/transparency). Non-payoff behavioral outcomes, while prevalent, should not be mapped one-to-one to efficiency effects, especially when punishment is costly or creates complex secondary effects. Some ambiguity and model-dependent disagreement persists, particularly regarding the efficiency impact of costly, peer-based punishment versus institutional punishment, and in settings where other mechanisms already achieve high efficiency.
