# 1) Evidence Base

The available literature set consists of four empirical papers, with two lab experiments (Engel & Zhurakhovska, 2017; Chang et al., 2021) and two observational studies (Qirko, 2020; Gao et al., 2024). The scope is relatively broad thematically (touching on lab and field contexts, centralized and third-party punishment, intergenerational dynamics, and general trends in social dilemma research), but narrow in terms of directly addressing the specific prediction task: quantifying the effect of peer or centralized punishment on *efficiency* (payoff relative to the cooperative optimum) in public-goods-game (PGG) or similar experimental environments. There is one paper (Engel & Zhurakhovska, 2017) offering close, primarily empirical evidence for PGGs with punishment, with others providing only adjacent or contextual information.

# 2) Task Relevance

**By Target-Relevance Dimension:**

- **pgg_or_variant:**  
  - *exact:* Only Engel & Zhurakhovska (2017) provides exact-relevance evidence for classical PGGs.  
  - *adjacent:* Qirko (2020), Gao et al. (2024), and Chang et al. (2021) investigate adjacent institutional, field, or resource-extraction settings, or general social dilemma research, which do not directly replicate experimental PGGs but engage with related cooperative dilemmas.
  
- **punishment_or_sanctions:**  
  - *exact:* Engel & Zhurakhovska (2017) and Qirko (2020) report on punishment or enforcement mechanisms, albeit with different implementation (centralized vs. third-party, lab vs. field).  
  - *adjacent:* Gao et al. (2024) reviews the prominence of punishment as a research theme but does not analyze effects or implementations.  
  - *none:* Chang et al. (2021) does not include punishment or sanctions.

- **efficiency_or_related_payoff_outcome:**  
  - *close:* Only Engel & Zhurakhovska (2017) reports payoff/group profit and references an efficiency-relevant baseline (Nash outcome), but does not provide normalized or ratio-based efficiency. Chang et al. (2021) reports payoffs but does not analyze punishment.  
  - *adjacent/none:* Qirko (2020) and Gao et al. (2024) do not directly report on payoff or efficiency; instead, they focus on behavioral outcomes or research trends.

**Summary:**  
For the downstream prediction task—estimating treatment efficiency (group payoff as a ratio of the cooperative optimum) after introducing punishment—most papers in the set provide only indirect or contextual information. Only Engel & Zhurakhovska (2017) is directly informative, and even there, the effect must be inferred from raw payoffs or group profit rather than explicitly computed efficiency.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes:**  
  - Group profit, mean group earnings, and final payoffs are reported in Engel & Zhurakhovska (2017) and (to a degree, but *not* in a punishment context) Chang et al. (2021).
  - None of the papers report efficiency as a normalized ratio to the cooperative optimum, requiring interpretation or inference from available payoff data.
  - Qirko (2020) and Gao et al. (2024) do not report any direct measures of group payoff, welfare, or efficiency.

- **Non-Payoff Behavioral Outcomes:**  
  - Contribution rates, punishment assignments, norm compliance, and other forms of rule-following are the focus of Engel & Zhurakhovska (2017) and Qirko (2020).
  - Chang et al. (2021) examines extraction, restoration behaviors, and intergenerational outcomes, but not sanctions.
  - Gao et al. (2024) discusses the prevalence of cooperation-promoting interventions, but not outcomes quantitatively.

- **Distinction:**  
  - Only Engel & Zhurakhovska (2017) provides both behavioral and payoff-related outcomes in a context directly relevant to PGG with punishment.

# 4) Main Findings Relevant To Prediction

Synthesizing across the papers:

- **Experimental PGGs With Centralized Punishment (Engel & Zhurakhovska, 2017; exact):**  
  There is clear experimental evidence that introducing centralized (authority-imposed) costly punishment in a repeated linear PGG increases both cooperation (behavioral outcome) and group profit (payoff outcome) compared to the Nash baseline (no cooperation, no punishment). The effect is robust to various authority framings, degree of personal stake, and policy announcement. While efficiency (as a ratio) is not directly reported, group profit levels exceed those in the non-punishment baseline, supporting a positive efficiency effect of punishment. The design is well-aligned with lab PGGs: continuous contributions, fixed MPCR, no chat, and known peer actions and punishment.

- **Observational Studies and Field Contexts (Qirko, 2020; adjacent):**  
  In real-world communities, punishment mechanisms exist but are applied inconsistently and contextually. Even where punishment rules are in place, costly enforcement occurs infrequently. There is no direct evidence for an efficiency boost from punishment, and the possibility is raised that external validity of lab results is limited: the *mere presence* of a punishment option does not guarantee its use, nor efficiency improvements.

- **Other Adjacent Literature (Gao et al., 2024; Chang et al., 2021):**  
  These studies confirm that cooperation, sanctions, and payoffs are focal themes in social dilemma research, but they do not synthesize quantitative impacts nor address the effect of punishment on efficiency in controlled or real payoff environments.

**Empirical vs Theory/Mechanism:**  
Most findings are empirical. There is little mechanistic theory discussion (with the possible exception of Qirko's discussion of motives for punishment). Mechanism claims in Engel & Zhurakhovska (2017) are empirical about the capability of authority-based punishment to move groups toward higher payoffs.

**Ambiguities/Disagreement:**  
- The positive efficiency boost from punishment demonstrated in lab PGGs with centralized authority may not generalize to all environments, especially outside the lab or where enforcement is voluntary, as highlighted by Qirko (2020).
- The field/lab gap and real-world implementation nuances (third-party, context-dependent, infrequent punishment) mean that efficiency gains cannot be assumed in all group settings when punishment is introduced.

# 5) Prediction Guidance

**For predictive modeling of treatment efficiency after enabling punishment in a public goods game:**

- **Direct Guidance:**  
  - *In classical lab PGGs, introducing authority-administered (centralized) costly punishment reliably increases group profits above the non-punishment (Nash) baseline, implying increased efficiency* (Engel & Zhurakhovska, 2017). Although efficiency as a ratio is not directly reported, the positive trend is robust across various authority framings and implementation details within the lab setting.

- **Contextual and Limiting Guidance:**  
  - *In field or organically self-governed environments, the enabling of punishment does not ensure deployment or efficacy; actual use (and thus efficiency gains) can be rare, contextual, or absent* (Qirko, 2020).
  - *Efficient outcomes depend on not just the technical availability of punishment but on group norms, context, and willingness to incur the cost of enforcement in practice.*

- **Dimension Inference:**  
  The effect in lab contexts is strengthened if prediction dimensions match those reported in Engel & Zhurakhovska (2017): multiple rounds, no chat, specified player count, linear payoff structure, and visible group outcomes. Absence of these (e.g., in highly contextual field settings, or with unknown punishment structure) means lower reliability of predicted efficiency gain.

- **Non-Payoff Outcomes Caveat:**  
  Where only increases in cooperation, norm compliance, or contribution rates are reported, these cannot be equated with efficiency improvements without direct payoff data.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed in Lab PGGs (Engel & Zhurakhovska, 2017):**
- `player_count` (included)
- `num_rounds` (included)
- `mpcr` (reported as linear, fixed)
- `punishment_cost` (specified)
- `punishment_tech` (authority-enforced, not peer-to-peer)
- `all_or_nothing` (continuous contribution)
- `chat` (not allowed)
- *Information dimensions: full info on others' actions and punishment, most closely matching `show_other_summaries`*
- `reward_exists` (absent)
- Many technical dimensions (e.g., default_contrib, show_punishment_id, reward_cost/magnitude, show_n_rounds) are not discussed in detail

**Indirectly or Contextually Informed (Qirko, 2020; Gao et al., 2024):**
- `punishment_cost` and `punishment_tech` (field implementations, third-party/self-imposed, context-dependent)
- `player_count` and `chat` (group size/context and communication sometimes referenced)
- `show_other_summaries`, `show_punishment_id` (public knowledge of outcomes/enforcement discussed contextually)
- No payoff parameters (e.g., mpcr, all_or_nothing, reward dimensions) specified

**Effectively Missing:**
- `default_contrib`, `reward_cost`, `reward_tech`, `reward_exists`, `reward_magnitude`, and fine details of information structure are largely unaddressed
- Peer punishment (as opposed to centralized) is not directly tested in lab settings with efficiency outcomes
- No paper provides a full mapping of dimension-to-efficiency effect

# 7) Important Limitations

- **Limited Direct Evidence on Efficiency Outcomes:**  
  Only one lab paper (Engel & Zhurakhovska, 2017) provides close (though not exact) evidence for efficiency improvement following the introduction of punishment. Efficiency must be inferred rather than directly reported.

- **Scope Restriction to Centralized (Not Peer) Punishment:**  
  No paper in the set directly analyzes the efficiency effect of peer punishment as implemented in standard PGGs, limiting generalizability for predictions specifically involving peer-based punishment.

- **Field versus Lab and External Validity:**  
  Real-world or field studies (Qirko, 2020) suggest that punishment is often not actively used, and its impact on efficiency is context-governed and unpredictable, raising external validity concerns for lab-based findings.

- **Incomplete Coverage of Design Dimensions:**  
  Among the 14 prediction-relevant design dimensions, only a subset is directly or even indirectly informed by the evidence base. Several dimensions (especially reward-related and some information structure parameters) are missing.

- **Outcome Measurement Gaps:**  
  Many outcomes focus on contributions and compliance rather than efficiency or group payoff, and only one paper links these to observed profit/earnings.

- **No Meta-Analytic or Parameter-Level Synthesis:**  
  The literature set lacks quantitative synthesis of treatment effects, so magnitude and conditionality of punishment's impact on efficiency must be inferred from scattered single-study findings.

- **Missing Peer Punishment and Combined Mechanisms:**  
  Effects of combined mechanisms (e.g., simultaneous punishment and reward, effects of chat or information) on efficiency are not directly addressed.

**In conclusion:**  
The evidence base is sufficient to support cautious predictions about efficiency gains from enabling punishment in lab-based, authority-punished PGG environments—especially when group, game, and information structures closely match those in Engel & Zhurakhovska (2017). However, generalization to peer punishment, broader design dimensions, and field or complex social settings is poorly supported or ambiguous in the current literature set.
