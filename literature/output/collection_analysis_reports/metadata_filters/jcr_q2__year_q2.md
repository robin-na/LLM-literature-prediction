# 1) Evidence Base

The paper set is very broad and contains a large and diverse array of experimental, empirical, and theoretical works. Out of 203 papers, a strong subset are direct laboratory experiments on standard public goods games (PGGs) or very close variants, with manipulations around the presence and form of punishment or sanctions. These empirical studies often report payoff-based outcomes—including group efficiency, average earnings, welfare, or total coins/points generated. Many theory and simulation papers also cover relevant mechanisms and formal conditions for punishment improving efficiency. A substantial minority of the set comprises adjacent games (e.g., Prisoner's Dilemma, common pool resources, helping/trust games) and focuses more on contributions or behavioral outcomes than direct efficiency/payoff data.

For the target prediction task—predicting treatment efficiency (with punishment enabled) given design dimensions and control efficiency (without punishment)—the evidence is strongest in experimental lab-based PGGs, with supporting evidence from theory and adjacent CPR/prisoner’s dilemma studies. There is also a significant subset of papers with high relevance on behavioral outcomes (like contributions, cooperation, or punishment rate) but only indirect or weak relevance for efficiency as defined for the task.

# 2) Task Relevance

## pgg_or_variant
- **exact**: Extensive direct coverage. Many empirical studies use the classic linear public goods game (4 players, repeated rounds, continuous/all-or-nothing contributions, standard MPCR, etc.).
- **close**: Repeated common-pool resource (CPR) games and some trust/goods provision/oligopoly games share crucial features and are often designed to be directly comparable to PGGs.
- **adjacent/weak/none**: Numerous adjacent papers (e.g., evolutionary games, one-shot PDs, trust/ultimatum games) provide theoretical/behavioral mechanistic insights but are less direct for mapping predictions to standard PGG design dimensions.

## punishment_or_sanctions
- **exact**: Strong coverage. Many studies manipulate the presence/absence, cost, and technology of costly peer or institutional punishment, or compare forms (peer vs. centralized/authority, burned vs. redistributed, etc.).
- **close/adjacent**: Many studies examine reward, exclusion, or norm enforcement as alternatives or complements to punishment, or study punishment-like mechanisms in adjacent games.
- **weak/none**: Some focus on non-punitive mechanisms (rewards only, communication, reputation) or punishment in evolutionary/real-world/animal contexts lacking a direct PGG mapping.

## efficiency_or_related_payoff_outcome
- **exact**: About half of the studies measure efficiency or total group payoff as a fraction of the cooperative optimum, often explicitly.
- **close/adjacent**: A significant number report contribution rates, cooperation rates, or punishment frequency, using them as proxies for efficiency. Others report earnings, surplus, or group welfare without scaling to the full cooperative benchmark.
- **weak/none**: Many theoretical or mechanistic papers, or those focused on behavioral traits, do not present efficiency or explicit payoff outcomes.

# 3) Outcomes Measured In The Literature

## Payoff-Related Outcomes (of high relevance for prediction)
- **Efficiency** (group payoff as a ratio of social optimum): Explicitly measured in many experimental studies (e.g., Page et al., 2013; Reif et al., 2017; Wang & Qin, 2015; Gurerk, 2013; Kolle, 2015; Dugar, 2013).
- **Average group payoff/earnings or welfare**: Frequently reported, sometimes used to derive efficiency.
- **Surplus, total coins generated, or total resource level**: Often mapped to efficiency, especially in CPR games.
- **Income inequality, distributional outcomes**: Occasionally examined as secondary effects.

## Non-Payoff Behavioral Outcomes (less directly relevant; proxies for efficiency)
- **Contribution/cooperation rates**: Most studies report mean contributions, often as the primary behavioral outcome.
- **Punishment frequency/targeting**: Extensively measured.
- **Norm compliance/types, trust/ranking, behavioral switching, emotion**: Present in both experimental and field studies.
- **Punishment assigned, reward use, exclusion events**: Proxy for mechanism activity.

Payoff-based outcomes are given primary weight for downstream efficiency prediction. Where only behavioral outcomes are reported, results are interpreted as indirect proxies if justifiable.

# 4) Main Findings Relevant To Prediction

Synthesizing findings across the most directly relevant (exact/close) papers yields several robust empirical and theoretical generalizations, each modulated by interactions with specific design dimensions:

- **Enabling (costly) peer punishment usually increases group efficiency over the control baseline, but not always.** The benefit is clearest when:
  - Punishment cost is not too high, and the punishment technology is effective (e.g., high cost-to-impact ratio) (Wu et al., 2014; Levine & Modica, 2016; Sui et al., 2017).
  - The punishment structure avoids anti-social (misdirected) punishment and is targeted at free-riders (Page et al., 2013; Kingsley, 2016; Bortolotti et al., 2015).
  - Endowment or productivity heterogeneity is limited, or the mechanism can accommodate it (Kolle, 2015; Kingsley, 2016; Robbett, 2016). With strong heterogeneity, punishment can fail to increase efficiency or even decrease it.
  - The structure of the punishment network is complete or symmetric (Leibbrandt et al., 2015; Boosey & Isaac, 2016). Incomplete/patchy networks, or cases with 'untouchables', often yield no improvement or decreased efficiency due to retaliation or under-monitoring.
  - Social learning or history information is available (Gurerk, 2013): efficiency gains from punishment are greater when participants can learn from or are informed about prior outcomes.
  - The design avoids or controls for antisocial punishment (punishing cooperators), which dramatically reduces efficiency gains (Bortolotti et al., 2015; Sylwester et al., 2013).
  - The punishment right is costlessly and widely available (Ramalingam et al., 2016).

- **Punishment sharply increases group contributions, but efficiency gains can be offset or negated by the cost of punishment—especially if:**
  - Punishment is frequent, misdirected, or reciprocal (Kingsley & Brown, 2016; Boosey & Isaac, 2016).
  - There is persistent antisocial punishment (Bortolotti et al., 2015; Sylwester et al., 2013).
  - The subject pool exhibits little prosocial responsiveness to punishment (general population vs. student samples: Bortolotti et al., 2015).

- **Centralized/authoritative or rule-based punishment (e.g., assigned public official/judge, or redistributive punishment) can yield higher efficiency gains compared to decentralized/peer punishment due to reduced retaliation, mis-targeting, and higher legitimacy (Page et al., 2013; Engel & Zhurakhovska, 2017).**

- **The efficacy of punishment is strongly conditional on key design features:**
  - **Network structure and monitoring:** Complete punishment networks enhance efficiency; incomplete networks or limited monitoring can undermine or reverse gains (Leibbrandt et al., 2015; De Geest et al., 2017).
  - **Cost and availability of punishment right:** Even small acquisition costs for the right to punish eliminate efficiency gains (Ramalingam et al., 2016).
  - **Form of punishment:** Redistributive mechanisms (where fines become rewards elsewhere in the group, rather than being burned) are more likely to increase both contributions and efficiency than traditional burning punishment (Page et al., 2013).
  - **Transparency and information feedback:** When punishment is observable (identities/actions), or history is available, targeting and compliance improve (Kamei & Putterman, 2015; Bortolotti et al., 2015), but in the presence of egocentric feedback only, retaliation may increase and efficiency can fall.

- **Baseline efficiency and the presence of strong social information or pre-existing cooperation matter:**
  - In settings with high baseline control efficiency due to strong norms or social information, adding punishment may offer little added benefit or can even reduce efficiency (Javaid et al., 2017).
  - Where social capital is low and baseline efficiency is poor, enabling punishment yields larger proportional gains (Gelcich et al., 2013).

- **Reward mechanisms (positive sanctioning) and exclusion can sometimes substitute for or outperform punishment in raising efficiency, particularly if reward is sufficiently potent/economical (Cong et al., 2016; Drouvelis et al., 2017; Charness & Yang, 2014).**
- **Behavioral outcomes (contribution rate, cooperation) are generally increased by punishment opportunities, but translation into efficiency gains is not automatic and can be masked/offset by punishment costs or mis-targeting.

# 5) Prediction Guidance

### General Guidance:
- **When control efficiency is moderate to low, and group/parameter settings match standard lab PGGs with symmetric, effective, and not too costly punishment, enabling punishment should **substantially increase efficiency** over the control (no-punishment) baseline (Page et al., 2013; Wang & Qin, 2015; Fu et al., 2017; Gurerk, 2013; Qin & Wang, 2013; Grieco et al., 2017).**
- **However, exceptions are notable and should inform cautious predictions:**
  - If **punishment networks are asymmetric, incomplete, or retaliation-prone**, efficiency gains may be zero or negative (Leibbrandt et al., 2015; Boosey & Isaac, 2016).
  - **Endowment or valuation heterogeneity**, especially without transparency, reduces or negates the benefit of punishment (Kolle, 2015; Kingsley, 2016; Robbett, 2016).
  - **If the right to punish is not universally or easily available, or must be purchased (even at low cost), do not predict efficiency gains from enabling punishment** (Ramalingam et al., 2016).
  - **High baseline efficiency** due to pre-existing social norms or strong information feedback (public feedback on extraction/contribution) means punishment may not further raise efficiency and may lower it (Javaid et al., 2017).
  - **Prevalent antisocial punishment or punishment targeted at compliant group members can decrease efficiency or raise variance in outcomes** (Bortolotti et al., 2015).

### Moderation by Design Dimensions:
- **Of all the 14 prediction dimensions, the most heavily and consistently moderating factors are:**
  - `punishment_cost` and `punishment_tech`: Lower costs and higher effectiveness increase the likelihood that enabling punishment boosts efficiency; if cost is high or effectiveness low, the benefit is reduced or vanished (Wu et al., 2014; Levine & Modica, 2016; Sui et al., 2017).
  - `player_count`, `num_rounds`: Larger groups and longer associations increase the need for punishment to sustain efficiency, but also may dilute effectiveness unless punishment is scalable (Levine & Modica, 2016; Sui et al., 2017).
  - `all_or_nothing` vs. continuous: Most lab studies use continuous contributions; evidence for all-or-nothing is limited but mostly aligns with above patterns.
  - `punishment_tech`/network structure: Complete, symmetric, and openly monitored networks yield the best results.
  - `show_other_summaries`/transparency: Improved feedback and visibility of contributions and punishment assignments improves targeting and supports positive efficiency effects.
  - `chat` and `social_learning` enhance the positive impact of punishment (Gurerk, 2013), and can even substitute for punishment when strong enough, but are less systematically studied across all experiments.
  - `reward_exists` and interaction with punishment: Combining well-calibrated (not extreme or unbalanced) reward and punishment can optimize efficiency (Cong et al., 2016).
- **Dimensions less directly supported or only contextually addressed include** `default_contrib`, `show_n_rounds`, `show_punishment_id`, and details such as optional vs. compulsory participation.

### Conditional Guidance:
- **If control efficiency is already high (e.g., due to social feedback, reputation, or culture), enabling punishment may yield little or no additional efficiency, and can introduce coordination problems or reduce welfare** (Javaid et al., 2017; Bortolotti et al., 2015).

# 6) Design Dimensions Highlighted Across Papers

## Dimensions Directly Informed:
- `player_count`, `num_rounds`: Manipulated in nearly all lab PGG studies and almost always reported.
- `mpcr`: Usually specified and manipulated as a core treatment in efficiency analyses.
- `punishment_cost`, `punishment_tech`, and sometimes `punishment_magnitude`: Frequently varied and/or specified as core moderating variables.
- `reward_exists`/`reward_cost`/`reward_tech`: Included in many studies on incentive balance.
- `chat`: Multiple studies explore the interaction between communication and punishment.
- `all_or_nothing` (vs. continuous): Most studies use continuous but all-or-nothing is sometimes tested.
- `show_other_summaries`: Feedback availability is often described and sometimes manipulated.
- `show_punishment_id`: Examined as a moderator of targeting, retaliation, and deterrent effect.

## Dimensions Indirectly or Contextually Discussed:
- `default_contrib`: Sometimes described in experimental protocols but not widely varied.
- `show_n_rounds`: Part of contextual information in some paper descriptions but rarely systematically tested.
- `reward_exists` interaction with punishment is well-developed in theory but less so in lab tests.

## Dimensions Effectively Missing or Sparse:
- `default_contrib`, `show_punishment_id`, fine-grained manipulations of information display (except for summary feedback and history), and the detailed structure of optional vs. compulsory participation.
- Systematic variations in `chat`/communication in combination with punishment are underrepresented.
- Rich manipulation of meta-norms (punishment of non-punishers), and endogenous institution formation have only a few focused studies (Ramalingam et al., 2016; Gurerk, 2013).

# 7) Important Limitations

- **Generalizability beyond lab PGGs:** While lab studies are rich and detailed for standard PGGs, evidence is sparser for field experiments, very large groups, or naturally occurring institutions. Results may not extrapolate to diverse real-world environments or subject pools (notably, "student-only" effects: Bortolotti et al., 2015).
- **Measurement of efficiency:** Many papers use contribution rate or cooperation as the primary outcome, not payout/efficiency. For some, efficiency must be inferred indirectly.
- **Interaction/moderation insufficiently mapped:** Few studies simultaneously manipulate multiple design dimensions (e.g., combination of chat, punishment cost, heterogeneity, and transparency).
- **Incomplete coverage of some dimensions:** As noted, several dimensions (e.g., default contribution, nuanced information treatments, reward–punishment interactions) are rarely independently manipulated.
- **Punishment design details are decisive:** Small changes to who may punish, the cost/benefit structure, or the information feedback can flip the direction of punishment's effect—from large positive to negative or neutral—making prediction sensitive to missing or ambiguous design details.
- **Publication bias and cultural effects:** There is a risk that positive effects of punishment are over-represented, and that culturally dependent patterns (e.g., prevalence of antisocial punishment) are under-explored.
- **Non-lab environments and long-term dynamics:** Evolutionary and field work is supportive but cannot be fully mapped to quantitative lab PGG predictions.
- **Rarely measured: Temporal persistence of efficiency gains post-punishment** (Bruttel & Friehe, 2014).
- **Non-monetary and informal sanctions:** Some evidence suggests these can be powerful in specific environments, but generalizability to monetary efficiency is unclear.

---

**In summary:**  
The literature strongly supports the general pattern that enabling punishment in classic PGGs increases efficiency—*provided* certain structural design details (network completeness, cost/effect ratio, universality of punishment rights, and social learning) are met and that baseline efficiency isn’t already at ceiling. However, important exceptions and moderators demand close attention to game design details when mapping control efficiency to punishment-enabled predictions. Evidence is weakest or most ambiguous when heterogeneity, misdirected or antisocial punishment, incomplete networks, or high baseline cooperation prevail. The design dimensions most robustly supported in the literature are group size, number of rounds, MPCR, punishment cost/technology, punishment network structure, and feedback/information design. Prediction accuracy will decline if these are unknown or under-specified.
