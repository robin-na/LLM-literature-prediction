# 1) Evidence Base

The paper set comprises 27 studies, nearly all of which are **experimental lab studies** with a small number of field or observational studies. The body of work is empirically focused, with only one or two agent-based or theoretical models blending into the empirical (e.g., Villatoro et al., 2014). The set is **broad** in that it covers a range of environments structurally similar or adjacent to Public Goods Games (PGGs) and includes studies addressing standard linear PGGs, collective-risk games, repeated trust and market settings, and various punishment and reward schemes. However, **papers reporting the efficiency effect of enabling peer punishment in exact PGGs** are in the minority; many studies focus on behavioral outcomes, non-standard or adjacent game forms, or variations on punishment/reward mechanisms.

# 2) Task Relevance

**PGG or Variant**:  
- About 5–6 studies use exact PGGs (Bahbouhi et al., 2024; Peysakhovich & Rand, 2016; Villatoro et al., 2014; Yang & Yang, 2024; Ren & Zheng, 2021).
- Several others use **close** variants (e.g., collective-risk games, repeated PD with group structure, or trust games) or **adjacent** forms (labor markets, allocation games, reputation feedback systems).
- Relevance for the prediction task: **exact** for a subset, **close/adjacent** for the remainder.

**Punishment or Sanctions**:  
- Studies directly manipulating peer punishment in PGGs or very similar dilemmas are present but a minority (Bahbouhi et al., 2024; Villatoro et al., 2014; Jiang et al., 2023; Macleod et al., 2025).
- Others feature *adjacent* punishment (third-party, exogenous, or institutional) or study settings with informal or proxy sanctions (e.g., contract renewal, reputation).
- Several studies lack punishment entirely.
- Only a few studies measure **effects of enabling or manipulating punishment institutions**.

**Efficiency or Related Payoff Outcomes**:  
- Only a small number of papers report **group efficiency** or related payoff/surplus measures as a primary outcome (e.g., Bahbouhi et al., 2024; Macleod et al., 2025; Li & Xiao, 2014; Brown et al., 2004; Jiang et al., 2023).
- Many papers focus on **contribution rate, cooperation, or behavioral outcomes** (**distinct from efficiency**).
- Other studies report **closely related outcomes**: group profit, revenue, or welfare, sometimes as secondary measures.

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes:**  
- **Directly reported:**  
  - Group efficiency, total earnings, surplus, or net profits (Bahbouhi et al., 2024; Macleod et al., 2025; Li & Xiao, 2014; Brown et al., 2004; Fabbri et al., 2019).
  - In several studies, **group success rates, investment levels, and average profit** serve as closely related proxies (Jiang et al., 2023; Shuvo & Kabir, 2024; Hashim et al., 2014).
- **Absent or secondary:**  
  - In many studies, payoff-related outcomes are **not reported** or only tangentially addressed.

**Non-Payoff Behavioral Outcomes:**  
- **Predominant in many papers:**  
  - Cooperation rates, contribution levels, punishment frequency, trust, voting for institutions, etc. (Peysakhovich & Rand, 2016; Villatoro et al., 2014; Falk et al., 2005; Goette et al., 2012).
  - Several studies specifically investigate **motivations for punishment or behavioral mechanisms** rather than efficiency.

# 4) Main Findings Relevant To Prediction

- **Enabling Punishment in Standard PGGs Typically Increases Efficiency:**  
  - Bahbouhi et al. (2024) is the most directly informative: enabling punishment in repeated PGGs increased group efficiency, with the magnitude of the increase moderated by group structure (individuals vs. teams, with unanimity teams seeing greatest gains due to less wasteful/anti-social punishment).
- **Moderation by Institutional Context and Norm Coordination:**  
  - Macleod et al. (2025) finds that punishment *can* increase efficiency (via increased effort, norm compliance) — but only when embedded in a supportive institutional environment (e.g., a formal grievance process). Elsewhere, the direct costs of conflict (punishment) may outweigh cooperative gains, reducing or not affecting efficiency.
- **Punishment Must Be Strong and Credible:**  
  - In collective-risk analogues (Jiang et al., 2023), punishment only meaningfully increases group performance (success at reaching collective targets) when the likelihood and magnitude are sufficiently high; weak or infrequent punishment has little or no effect, especially as group size increases.
- **Antisocial Punishment and Social Competition:**  
  - Antisocial punishment, intergroup competition, or poorly specified norms (Goette et al., 2012; Bahbouhi et al., 2024; Zhang et al., 2020) can undermine efficiency, even when punishment is available; the *form* and *targeting* of punishment matters greatly.
- **Proxy and Adjacent Findings:**  
  - In various **adjacent games** (feedback/reputation, trust, and market games), *punishment-like* mechanisms (e.g., feedback withdrawal, contract renewal/firing) can either enhance or depress efficiency depending on design specifics.
  - In some cases, the *introduction* of mutual retaliation options leads to lower efficiency (Bolton et al., 2018).

# 5) Prediction Guidance

- **Most Direct Guidance Comes from Standard, Well-Specified PGGs with Efficiency Data:**  
  - If the environment is a repeated PGG with peer punishment enabled (individual or team-based decisions), one may expect a **positive effect on efficiency versus control** (no-punishment) games, especially when group coordination mechanisms reduce antisocial or wasteful punishment. If teams use unanimity rules, the efficiency gain is especially strong (Bahbouhi et al., 2024).
- **Control Efficiency as Baseline:**  
  - Studies detailing both control (no punishment) and treatment (punishment enabled) allow mapping. However, the magnitude of efficiency gain is **moderated by group structure, punishment technology (cost/magnitude), and the likelihood of antisocial punishment**.
- **Key Moderators for Prediction:**
  - **Group Size:** Larger groups make punishment less effective unless the punishment risk is high (Jiang et al., 2023).
  - **Punishment Cost/Effectiveness:** More effective (i.e., higher magnitude relative to cost) and more focused punishment supports greater deterrence and efficiency.
  - **Punishment Structure/Decision Rule:** Unanimity and group coordination reduce destructive punishment, increasing net efficiency.
  - **Norm Structure and Clarity:** Well-defined and salient norms, along with institutionalized coordination or grievance channels, enhance the efficiency of punishment (Macleod et al., 2025; Bahbouhi et al., 2024).
  - **Baseline (Control) Efficiency:** If baseline efficiency is already high, punishment may yield smaller marginal gains or even net loss due to its cost (several studies).

- **Caveats:**
  - **Prediction is weaker if evidence comes only from behavioral cooperation rates** rather than total payoff.
  - **Antisocial or misapplied punishment can reduce group efficiency** (Goette et al., 2012); group composition or competition increases this risk.
  - **Adjacent or proxy outcomes (trust, compliance, revenue) suggest similar moderating principles**: effectiveness and design are key.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions (with empirical payoff data in at least one relevant study):**
- `player_count` (group size): directly manipulated or measured in several studies with efficiency outcomes, especially PGGs and variants.
- `num_rounds`: repeated vs. one-shot (or number of rounds) is commonly reported, including its effect on norm formation and punishment efficacy.
- `mpcr`: Marginal per capita return is often specified and sometimes varied.
- `punishment_cost` & `punishment_tech` (structure, magnitude): these are manipulated in experimental studies and are shown to be key moderators of punishment's efficiency effect.
- `all_or_nothing`: all papers specify, some directly manipulate this dimension.
- `team_decision_rule` (contextually: individuals vs. teams/unanimity, per Bahbouhi et al., 2024).

**Indirectly Informed/Contextually Discussed:**
- `chat`: presence or absence is reported; rarely a focal manipulation for efficiency.
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: occasionally reported for transparency but rarely as primary experimental variables.
- `default_contrib`: only directly present in a minority of studies.
- `reward_exists`, `reward_cost`, `reward_tech`: occasionally present (e.g. Li & Xiao, 2014; Fabbri et al., 2019) but not the focus except in field-specific studies.

**Effectively Missing:**
- Some dimensions (`reward_magnitude`, `show_punishment_id`) are rarely present or manipulated in efficiency-focused studies.
- The *joint effect* of multiple dimensions (e.g., chat by group size, or punishment tech by all-or-nothing) is only rarely explored empirically with efficiency payoffs.

# 7) Important Limitations

- **Exact Relevance to Downstream Prediction Task is Limited:**  
  - Only a few studies provide **both** standard PGG structure **and** payoff-based efficiency measures for both control and punishment-enabled treatments.
  - Many studies use **behavioral outcomes as proxies** for efficiency; direct mapping to payoff is not always justified.
  - **Adjacent and proxy environments** (e.g., trust games, repeated PD, market settings) differ structurally from standard PGGs in important ways, limiting transferability.
- **Subset of Design Dimensions Are Well-Informed:**  
  - Several design dimensions (e.g., information visibility, group composition, chat) are typically reported but not systematically varied.
- **Ambiguity in Moderator Effects:**  
  - Some studies suggest **conflicting impacts of punishment** depending on social context (e.g., intergroup competition can switch punishment from prosocial to antisocial, thus reducing efficiency).
  - The **role of institutional context is paramount**: formal procedures (grievances, codes of conduct) or well-specified group decision rules can convert punishment from destructive to efficiency-enhancing.
- **Data on Baseline/Control Efficiency is Scarce:**  
  - Few studies report both control and treatment (punishment enabled) efficiency under multiple parameterizations.
- **Contribution Rate ≠ Efficiency:**  
  - Many studies focus on cooperation/contribution or punitive behavior, not on the net group payoff; translating behavioral gains to efficiency gains is not trivial, especially if punishment is costly or misapplied.
- **Potential Overestimation of Positive Punishment Effects:**  
  - Several studies show the positive impact of punishment on cooperation *without* always a clear net payoff gain; may overstate likely efficiency improvements in poorly designed or weakly coordinated real-world environments.

**In summary:**  
- The literature provides a **solid qualitative foundation** for predicting when punishment will (and will not) increase efficiency in public-goods-game-like settings, primarily under repeated, well-coordinated structures with clear norms. Predictive guidance is strongest for variation in group structure, punishment cost/effectiveness, and norm coordination. However, **quantitative predictions** should be made **cautiously** due to sparse coverage of the full design space and limited direct evidence on efficiency outcomes for many combinations of game dimensions. 

---

**References**  
Bahbouhi, J. E., et al. (2024); Peysakhovich & Rand (2016); Villatoro et al. (2014); Yang & Yang (2024); Ren & Zheng (2021); Jiang et al. (2023); Macleod et al. (2025); Goette et al. (2012); Zhang et al. (2020); Bolton et al. (2018); Brown et al. (2004); Li & Xiao (2014); Fabbri et al. (2019); others in evidence digest.
