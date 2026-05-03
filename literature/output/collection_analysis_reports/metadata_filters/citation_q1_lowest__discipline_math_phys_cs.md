# 1) Evidence Base

This is a large, rich, and diverse literature set (231 papers) covering a wide range of experimental, theoretical, and simulation studies on cooperation, punishment, and efficiency in public-goods-game (PGG)-like environments. There is a mix of:
- **Empirical laboratory experiments** with exact PGG designs (e.g., Suleiman & Samid, 2021; Cobo-Reyes et al., 2022; Kanitsar, 2021).
- **Theoretical and computational models** directly addressing PGGs with varied punishment and reward mechanisms (e.g., Wu et al., 2014; Sun et al., 2025; Botta et al., 2021; Gao et al., 2020).
- **Empirical and theoretical work on adjacent games** (e.g., repeated Prisoner’s Dilemma, trust games, threshold collective action games) that analyze punishment and efficiency in closely related settings.
- **A substantial number of studies focusing on cooperation rates, behavioral responses, or other non-payoff outcomes,** rather than direct efficiency or group payoff. 

The set is broad and provides high coverage for standard linear PGGs, PGG variants (spatial, threshold, optional participation, public bads), and institutional contexts (peer vs. centralized punishment, reward schemes, resource games). It covers a range of player counts, MPCRs, punishment costs/technologies, and social/cultural moderators.
- **Exact empirical payoff-based outcome studies are numerous but often limited in parameter variation or lack full mapping to all prediction dimensions.**
- **A significant fraction of the theory papers provide parameterized or qualitative predictions about efficiency but do not always focus on payoff outcomes.**

# 2) Task Relevance

### a. `pgg_or_variant`
- **Exact relevance:** A large core of empirical and theoretical papers directly study standard PGGs or very close variants (e.g., Suleiman & Samid, 2021; Cobo-Reyes et al., 2022; Botta et al., 2021).
- **Close and adjacent:** Many studies are adjacent, analyzing games such as repeated PD, resource dilemmas, trust games, and threshold collective action (e.g., Kanitsar, 2021; Murase, 2025; Friehe & Tabbach, 2018).
- **Weak or missing:** Some papers are not PGGs or use structurally different models; these offer little or no direct relevance.

### b. `punishment_or_sanctions`
- **Exact relevance:** A large number address punishment directly—both peer and institutional, formal and informal, often manipulating presence, cost, and effectiveness.
- **Adjacent/none:** Several only address reward, partner choice, exclusion, or internalized costs as alternatives; others focus on reputation, communication, or structural effects.
- **Note:** Presence of punishment ≠ manipulation or direct comparison to a no-punishment control, so attention to experimental/treatment structure is needed.

### c. `efficiency_or_related_payoff_outcome`
- **Exact relevance:** Many key studies report group earnings, efficiency (total payoff as a fraction of full cooperation), welfare, or closely related surplus.
- **Close:** Some measure net benefit or total wealth with some transformation.
- **Adjacent/weak:** A sizable group reports only cooperation/contribution rates, prevalence of strategies, or behavioral outcomes—these can point to efficiency changes under certain assumptions but are not equivalent.
- **None:** Several papers report neither efficiency nor any payoff-based outcomes.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (Relevant for Prediction):**
    - Average group earnings, efficiency ratios (relative to social optimum), total coins generated, net payoff, welfare, surplus, resource abundance/sustainability.
    - Explicit calculations or phase diagrams showing payoff/efficiency as a function of game parameters.

- **Non-payoff behavioral outcomes (Not Directly Usable for Prediction):**
    - Contribution/cooperation rates, prevalence of punishing/rewarding strategies.
    - Frequency or severity of punishment, anti-social vs. pro-social punishment rates.
    - Group composition dynamics (e.g., stability, prevalence of "norm keepers" or "reciprocators").
    - Strategy transitions in evolutionary or agent-based models.

- **Indirect/proxy outcomes:**
    - Success rate in achieving the public good (sometimes tightly linked to efficiency in threshold games).
    - Persistence or collapse of cooperation as an indicator of maximal or minimal efficiency.

**Important distinction:** Many papers infer that higher cooperation should lead to higher efficiency, but only those measuring actual payoffs, earnings, or efficiency can be used directly for quantitative prediction.

# 4) Main Findings Relevant To Prediction

## a. Direction of Punishment Effects
- **Peer or centralized punishment in PGGs generally increases efficiency** relative to the control game with punishment disabled, as long as:
    - The cost of punishment is not too high relative to its effectiveness (Wu et al., 2014; Botta et al., 2021; Gao et al., 2020; Zhang et al., 2019; Kanitsar, 2021).
    - The population includes a sufficient share of pro-social punishers (“strong reciprocators”), and not too many norm-keepers or anti-social punishers (Suleiman & Samid, 2021).
    - The punishment/institution is designed to efficiently deter defection, either individually or collectively (Ishikawa & Fontanari, 2025; Gao & Liang, 2020; Cooney, 2025; Evans & Thomas, 2001; Nasrallah & Cheaib, 2016).
    - The mechanism is not overridden by high punishment cost, poor targeting, or perverse strategic effects.

- **Magnitude is highly variable.** The efficiency increase is moderate-to-large in many models and lab experiments, but can be small or negative if:
    - Punishment is automatic, low in severity, or strictly costly (Yang et al., 2020; Calabuig et al., 2024).
    - There is substantial anti-social or norm-keeper punishment (Suleiman & Samid, 2021).
    - The design or context induces punishment among cooperators or is frequently misapplied (Gao & Li, 2023; Kanitsar, 2021; Macleod et al., 2025).
    - The parameter regime makes punishment ineffective (e.g., very high group size or punishment cost; see Kurokawa, 2023).

## b. Moderators and Boundary Conditions
- **Game design parameters affecting the impact:**
    - **Punishment cost and effectiveness:** Lower cost/higher deterrence yields larger efficiency gains (Wu et al., 2014; Sun et al., 2025; Zhang et al., 2019).
    - **MPCR (marginal per capita return):** Effects are strongest in settings where baseline (control) efficiency is low (Wu et al., 2014; Gao et al., 2020), and less pronounced when control efficiency is high (Gao et al., 2025).
    - **Group size:** Larger groups sometimes require institutional or cost-shared mechanisms; costly peer punishment may be less effective (Ishikawa & Fontanari, 2025; Kurokawa, 2023).
    - **Institutional context:** Formal centralization (e.g., tax-funded central punishment) typically yields higher efficiency gains than informal peer punishment, especially in large or open groups (Cobo-Reyes et al., 2022; Yang & Yang, 2024).
    - **Network and group structure:** Dense sanctioning networks (typical PGG) support effectiveness; sparse or circular networks (generalized exchange) do not (Kanitsar, 2021).
    - **Population composition:** High prevalence of strong reciprocators increases the effect; norm-keepers and anti-social punishers can negate gains (Suleiman & Samid, 2021; Greenwood et al., 2018).

- **Control (no-punishment) efficiency as a moderator:**
    - In games with **low control efficiency** (i.e., much less than 1), enabling punishment often raises efficiency substantially.
    - If control efficiency is already high due to other mechanisms (partner choice, strong reciprocity, networked clustering), adding punishment may have little additional effect or can even lower efficiency if costs outweigh benefits (Gao et al., 2025; Cui et al., 2022; Kurokawa, 2023).

- **Nature and design of punishment:**
    - **Peer vs. institutional:** Institutional punishment often produces larger gains (Cobo-Reyes et al., 2022; Yang & Yang, 2024).
    - **Reward mechanisms:** Often, reward (or combined reward-punishment) can match or exceed the efficiency gains from punishment, especially when implemented at the group/institutional level (Sun et al., 2025; Yang & Yang, 2024).

## c. Contextual Effects, Limitations, and Mixed Effects
- **Antisocial punishment, norm-keeping, and misapplied punishment can reduce efficiency or render punishment counterproductive** (Suleiman & Samid, 2021; Kanitsar, 2021; Gao & Li, 2023; Kurokawa, 2023; Macleod et al., 2025).
- **Spatial, network, and reputational structures are important moderators:** Small-world networks facilitate higher efficiency via punishment; network topology and information can either support or hinder punishment’s effectiveness (Cui et al., 2022; Kanitsar, 2021).
- **Control/treatment mapping is non-uniform:** In generalized exchange or games not supporting direct mutual monitoring, punishment is less effective or may even reduce efficiency (Kanitsar, 2021).

# 5) Prediction Guidance

The literature supports the following principles for predicting the average efficiency of a PGG (or close variant) when peer punishment is enabled, given game design parameters and the control (punishment-disabled) efficiency:

1. **Average efficiency with punishment enabled will generally be higher than without, provided:**
    - Punishment cost is reasonable relative to effectiveness;
    - There are enough willing (prosocial) punishers;
    - The institution/mechanism is well targeted (e.g., not flooded with antisocial punishment);
    - The design matches a standard linear or spatial PGG—not an edge case like generalized exchange or weak, automatic punishment (which can make things worse or yield no gain).

2. **The magnitude of the efficiency increase is highly sensitive to:**
    - The ratio of punishment cost to punishment effectiveness (lower costs and higher fines per unit increase effectiveness: Wu et al., 2014; Sun et al., 2025; Zhang et al., 2019);
    - The marginal per capita return (MPCR), with larger gains where MPCR is low and baseline efficiency is poor (Wu et al., 2014; Cui et al., 2022);
    - The population and group structure, including openness, migration, and endogenous group formation (Cobo-Reyes et al., 2022);
    - The presence and strength of alternative cooperation-supporting mechanisms (partner choice, reputation, communication, etc.), which may dampen or override punishment effects (Han & He, 2023; Pancotto et al., 2023);
    - The prevalence of norm-keepers and antisocial punishers;
    - The actual behavioral use of punishment—if punishers do not act (due to consensus thresholds or reversal), gains may be minimal or absent (Gao & Li, 2023).

3. **Prediction is more reliable when the following information is available** (from the design dimensions):
    - Player count, num rounds, MPCR, punishment cost, punishment technology (cost/fine mapping), and whether information is full or partial (Suleiman & Samid, 2021; Wu et al., 2014; Cobo-Reyes et al., 2022; Gao et al., 2020; Ishikawa & Fontanari, 2025).
    - Baseline efficiency in the control game—a stronger baseline reduces headroom for improvement, but does not always prevent gains (e.g., incremental gains for already high-cooperation groups can be small or negative if costs are substantial).

4. **Use caution when:**
    - The game is a near-threshold or all-or-nothing variant (punishment may only help if baseline is just below the contribution threshold);
    - Antisocial punishment is likely, or if societal context suggests many norm-keepers (Suleiman & Samid, 2021);
    - Punishment is weak, automatic, or strictly non-deterrent (Yang et al., 2020).

5. **Prediction should be:**
    - *Quantitatively upward (improved efficiency) in standard PGGs where punishment is plausible and cost-effective*;
    - *Attenuated or even negative where costs are high, punishment is mis-targeted, or in edge-case designs*.

# 6) Design Dimensions Highlighted Across Papers

- **Directly Informed Dimensions:**  
    - `player_count` — Numerous lab and simulation studies directly vary and report player counts.
    - `num_rounds` — Varied across studies, with results on how repetition/finite/infinite horizon affect outcomes (e.g., Jones, 1999).
    - `mpcr` — Very frequently explored; key in calibrating when punishment adds most.
    - `punishment_cost`, `punishment_tech` — Explicit and precisely documented in most empirical/theory studies of punishment effectiveness.
    - `all_or_nothing` (binary vs. continuous) — Both analyzed, but with corresponding differences in cooperative baseline and efficacy.
    - `chat` — Occasionally included; affects cooperation, often boosting baseline and sometimes reducing marginal gain from punishment.
    - `reward_exists`, `reward_cost`, `reward_tech` — Addressed in papers analyzing hybrid or alternative mechanisms to punishment.
    - `show_n_rounds`, `show_other_summaries`, `show_punishment_id` — Some studies vary information disclosure, reporting important moderation of behavioral effects.
- **Indirectly Informed Dimensions:**  
    - `default_contrib` — Less commonly manipulated, but some studies frame via opt-in/opt-out.
    - `show_punishment_id` — Some lab experiments make punisher identification explicit, which is known to change behavioral effects.
- **Sparse or Missing Dimensions:**  
    - Not all design dimensions (especially those relating to interface, defaults, or nuanced information structure) are systematically varied or reported in the majority of empirical studies.
    - Granular breakdowns of group composition (norm-keepers vs. strong reciprocators) are vital but often context- or country-dependent and lacking in many studies.
- **Contextual Coverage:**  
    - Network and spatial structure (e.g., Cui et al., 2022; Wu et al., 2014; Kanitsar, 2021) receive good coverage, but mapping from these to standard PGG predimension space sometimes requires interpretation.
    - Few studies systematically compare all 14 prediction dimensions; rather, most cover subsets in targeted hypothesis analyses.

# 7) Important Limitations

- **Payoff outcome missingness:** A substantial fraction of studies, even when labeled as PGG with punishment, do **not report efficiency or payoff outcomes** but only cooperation rates, limiting direct prediction value.
- **Context dependence:** Many models and experiments flag *strong moderation* by group composition, social norms, network structure, information, and mechanism details—making extrapolation to other parameter regions uncertain.
- **Edge-case designs:** Some “punishment” treatments (e.g., weak, automatic, or anti-social punishment; generalized exchange) have no or negative efficiency effects and must not form naive priors for standard linear PGGs.
- **Treatment implementation:** Not all studies compare control (punishment-off) and treatment (punishment-on) games within the same design or specify all relevant parameters.
- **Empirical coverage gaps:** Despite the large literature, some combinations of design parameters (e.g., large group, non-standard information disclosure, combined reward and punishment, very high/low MPCR, chat) are not fully explored empirically.
- **Mechanism inference vs. direct outcome evidence:** In some cases, efficiency predictions can only be “inferred” from increased cooperation, but this may not hold when punishment costs are substantial or punishment is misapplied.
- **External validity:** Many simulation and theory results presume stylized agent types, evolutionary dynamics, or infinite populations, which may not fully map to lab experiment findings or to real-world institutional interventions.
- **Cultural, social, and demographic moderators are often context-specific** and not always observable or controllable in prediction settings.

**In summary:**  
The literature provides strong evidence and detailed guidance—grounded in both empirical and theoretical studies—that enabling punishment in PGGs typically increases efficiency over the control (punishment-off) baseline, **provided punishment is not too costly, is well targeted at defectors, and pro-social punishers are present**. The effect size is highly sensitive to cost-effectiveness, MPCR, group size, institution/mechanism type, and baseline control efficiency. Predictions should cautiously reflect the information available for the relevant game design dimensions, recognizing that gaps exist where outcomes are non-payoff or context-specific.
