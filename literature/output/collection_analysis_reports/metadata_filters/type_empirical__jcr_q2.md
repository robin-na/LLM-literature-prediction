# 1) Evidence Base

This paper set contains a large, diverse, and methodologically strong empirical evidence base. The majority of the studies are **empirical/experimental** (lab, lab-in-the-field, and some field experiments). There is little pure theory and only occasional meta-analytic or observational work; the few non-experimental and survey-based studies are easily filtered out.

Sampling is **broad** for the downstream prediction task: most studies are closely centered on standard repeated linear Public Goods Games (PGGs), their networked and institutional variants (e.g., CPRs, threshold games, team production games), and the implementation of institutional features like punishment, reward, sanctions, exclusion, and communication.

The vast majority of the directly relevant papers manipulate the presence/absence of **peer or central punishment** and systematically measure **payoff-based outcomes** (efficiency, earnings, welfare, group profit). Many studies additionally report non-payoff behavioral outcomes (contribution rates, compliance, norms, punishment assigned, etc.).

**Sample coverage of design dimensions is substantial**: key features like player count, rounds, MPCR, punishment cost and effectiveness, communication (chat), network structure, information, and reward presence are all extensively covered, with varying levels of detail across papers.

**However, there are blind spots**: few studies address certain rare combinations (e.g., games with chat + punishment + networked punishment + changing MPCR + reward options). Some game designs—such as dynamic PGGs, one-shot games, or games with extreme heterogeneity or unique cultural settings—are less densely covered. For many adjacent but not exact PGG designs, payoff-based outcomes are missing.

In conclusion, **for lab public goods game-like environments**, the evidence base is both large and directly targeted to the prediction task, uniquely well-positioned to inform quantitative prediction of treatment efficiency, conditional on design features and control efficiency.

---

# 2) Task Relevance

**PGG or Variant (`pgg_or_variant`)**:  
- *Relevance: exact (majority)*  
  Most papers use standard linear/repeated PGGs or close variants such as CPRs, threshold PGGs, or VCMs, with a clear mapping back to canonical PGG structure. Papers using CPR, team production, or network versions are generally at least "close".

**Punishment or Sanctions (`punishment_or_sanctions`)**:  
- *Relevance: exact (majority)*  
  Most key studies manipulate costly punishment as a treatment (peer, centralized, exogenous, or via exclusion/ostracism) or compare it to reward/information/no-sanction conditions. Mechanisms range from standard 1:3 or 1:1 cost-to-impact ratios, fines, probabilistic punishment, voting on punishment, exclusion, ostracism, and more. Some studies test institutional features (votes, majority/consensus, endogenous formation) and cultural variants.
- Studies with only reward, approval/disapproval, or feedback, and not monetary punishment, are `"adjacent"` or `"close"`.

**Efficiency or Related Payoff Outcome (`efficiency_or_related_payoff_outcome`)**:  
- *Relevance: exact to close (majority)*  
  A large subset measure **group efficiency** (payoff relative to the social optimum), total group earnings, group welfare, or surplus directly. Some measure only contributions or norm compliance (coded "adjacent" or "non-payoff"). A minority focus only on behavioral/psychological outcomes with no payoff measurement; these are `"none"` or `"weak"` for our prediction task.

**Summary**:  
There is **excellent, direct coverage** of all three core target-relevance dimensions for the main population of studies.  
Papers with only non-payoff behavioral outcomes, or that analyze games other than PGG/CPR variants, are clearly separable and less relevant to the quantitative prediction of treatment efficiency.

---

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes (Directly relevant):**
- **Efficiency/group efficiency:** Most key studies report group payoff as a fraction of the fully cooperative optimum.
- **Group earnings, net surplus, average participant payoff:** Frequently used if efficiency as a ratio is not available.
- **Welfare, group profit:** Usually equivalent to group efficiency, occasionally net of punishment costs.

**Non-Payoff Behavioral Outcomes (Should not substitute for efficiency):**
- **Contribution/cooperation rates**: Ubiquitously reported as intermediate outcome; important for mechanisms, but not equivalent to efficiency.
- **Punishment assigned/frequency, norm compliance, retaliation, anti-social punishment:** Reported in nearly all punishment experiments; must be distinguished from payoff outcomes.
- **Behavior under social norms, choice of sanctioning institutions, votes:** Useful for mechanistic explanation but only indirectly informative for efficiency.
  
**Adjacent or Weak Payoff Outcomes:**
- **Provision/success rate in threshold games:** Used as a proxy for efficiency in step-level or collective-risk designs.
- **Compliance rates (with rules, minimums):** Intermediate; not equivalent to efficiency unless linked to group payoff.

**Not Measured or Irrelevant:**
- Many studies, especially those marked "adjacent" or "none" for payoff, focus solely on emotions, norm perception, social status, or neural correlates, with no direct mapping to efficiency.

---

# 4) Main Findings Relevant To Prediction

## Empirical Findings

### General Patterns:
- **Enabling peer or central punishment in repeated PGG-like games often increases group efficiency (total payoff relative to the cooperative optimum) compared to control games without punishment**—but only under certain design conditions (Fehr et al., 2002; Sefton et al., 2007; Kamei, 2024; Arechar et al., 2018; Zhang et al., 2024).
- **The efficiency gain from punishment is *not universal***: in a sizeable minority of studies, punishment increases contributions but does *not* increase (and can reduce) group efficiency due to the direct cost of punishing (Botelho et al., 2022; Casari & Luini, 2009; Peng, 2022; Casari & Tavoni, 2024; Vollan et al., 2019).
- **Cost structure and effectiveness of punishment are central** (Gürerk et al., 2018; Dannenberg & Gallier, 2020): punishment must be both not too costly and sufficiently deterrent to yield a net efficiency gain.
- **The *structure* of the punishment institution is critical** (consensus-based, central authority, majority-vote, network structure): institutions that censor anti-social punishment, require consensus, or centralize punishment can substantially improve efficiency compared to baseline peer punishment (Casari & Luini, 2009; Grieco et al., 2017; Kamei & Putterman, 2015; Peng, 2022).
- **Game design dimensions (mainly MPCR, player count, rounds, visibility, and information structure) are strong moderators**.
- **Heterogeneity (in endowment, valuation, productivity, or group composition) often reduces the positive effect of punishment on efficiency, and can cause punishment to backfire or have no effect** (Kingsley, 2016; Kölle, 2015; Waichman, 2020; Mantilla et al., 2021; Reuben & Riedl, 2009).

### Moderators and Interactions:
- **Network structure of punishment (who can punish whom) is a key moderator**: incomplete networks may increase efficiency under certain designs, but in others may reduce it due to diffusion of responsibility or bystander effect (Peng & Fan, 2023; Boosey & Isaac, 2016; Leibbrandt et al., 2015).
- **Antisocial punishment (punishment of cooperators) severely undermines efficiency gains** and is highly variable culturally and across samples (Bruhin et al., 2020; Bortolotti et al., 2015; Mantilla et al., 2021).
- **Punishment is less effective in groups with established high baseline efficiency, strong information/commitment mechanisms, communication, or strong social norms** (Botelho et al., 2022; Javaid & Falk, 2015).
- **Control (no-punishment) efficiency is a strong predictor of treatment efficiency in typical laboratory PGGs when punishment is effective and not too costly—*but not* in settings where punishment effectiveness is undermined by anti-social punishment, population heterogeneity, or costly institution/sanctioning.**

### Time Dynamics:
- **Initial periods after introducing punishment can see lower efficiency (due to sanctioning costs), but efficiency improves over time as cooperation stabilizes and punishment usage declines (learning/threat effects)** (Sefton et al., 2007; Waichman & Stenzel, 2019).
- **Removal of punishment leads to a rapid decay in cooperation and efficiency unless alternate mechanisms are established (legacy/spillover effect is context-dependent)** (JARUNGRATTANAPONG, 2022; Chugunova et al., 2020).

### Key Contrasts:
- **Punishment vs. Reward**: reward-only mechanisms rarely sustain high efficiency in standard PGGs; combined rewards and punishment may further increase efficiency but are less robust in the long run (Sefton et al., 2007; Gürerk et al., 2018; Vyrastekova & van Soest, 2008).
- **Peer vs. Central or Exogenous Punishment**: Both can be effective under proper design; central punishment often yields higher or more stable efficiency by minimizing anti-social punishment, but effectiveness depends on cost, coverage, and information (Angelovski et al., 2018; Engel & Zhurakhovska, 2017).

## Mechanism Arguments and Theory

- **From mechanism/theory arguments**: punishment is thought to increase efficiency only if it is used selectively against free-riders, is not overly costly, is non-retaliatory, and is transparent (Fehr et al., 2002; Ostrom, 2006; Dannenberg et al., 2020).
- **Behavioral regularities** (e.g., targeting, norm compliance, and punishment adaptation over time) inform the expected treatment–control efficiency mapping under specific institutional choices.

---

# 5) Prediction Guidance

- **Quantitative prediction of treatment efficiency from design features plus control efficiency is highly feasible for most standard laboratory PGG designs, using this evidence base.**
    - **If the control game is "typical" (low to moderate efficiency, 3-5 players, 10-20 rounds, standard MPCR 0.4–0.5): enabling peer punishment with standard 1:3 cost-to-impact and no communication will increase group efficiency by ~20–40% of the gap to the social optimum.** (Fehr et al., 2002; Arechar et al., 2018; Gürerk et al., 2018)
    - **If the punishment institution is "strong" (costless or nearly so, high impact, or enforced centrally with perfect targeting), expect efficiency gains to approach the social optimum.**
    - **If punishment is weak (costly, low impact, non-targeted, or can be misused for anti-social or retaliatory purposes), efficiency gains are smaller or absent; in the worst case, efficiency can decline due to direct costs and anti-social punishment.** (Botelho et al., 2022; Vollan et al., 2019; Casari & Tavoni, 2024)
    - **Communication (chat or face-to-face), information feedback, and endogenous institution formation are strong positive moderators and can combine synergistically with punishment.** (Ostrom, 2006; Kamei & Putterman, 2015; Engel et al., 2021; Böhm et al., 2020)
    - **Reward mechanisms are rarely a substitute for punishment; their efficiency effect depends heavily on the reward's impact ratio. Combination of reward and punishment sometimes yields the highest efficiency, but only if both are used effectively.** (Sefton et al., 2007; Vyrastekova & van Soest, 2008)
    - **Design dimensions such as punishment network structure, player heterogeneity (endowment, valuation, productivity), group cultural composition, and the possibility for anti-social punishment must be explicitly considered, as they can reduce or reverse the efficiency effect relative to control.**
    - **Time horizon and information about number of rounds matter: known end periods and short games often see weaker efficiency gains from punishment (end-game effect).**
    - **For games with extremely high control efficiency, strong social feedback, or strong alternatives (e.g., binding commitment): expect little or no extra gain from enabling punishment, and possible efficiency loss due to cost of unnecessary punishment.**
    - **If anti-social punishment, feuds, or retaliation are likely (as observed in certain cultures or network structures), predicted treatment efficiency should be reduced even below control efficiency.** (Bruhin et al., 2020; Nikiforakis & Engelmann, 2011)

- **In all cases, prediction must distinguish between increases in contribution/cooperation rates and actual efficiency gains.** Improvements in contribution that are offset by punishment costs may not improve, or may even reduce, average group efficiency.

---

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed (many high-signal studies):**
- **player_count**: Most studies use 3–5 players (with clusters at 4 and 5); effect moderation by group size is empirically documented.
- **num_rounds**: Repeated games (5–30 rounds) dominate; treatment dynamics over time are described in detail.
- **mpcr**: Both high and low MPCRs are tested; effects are non-linear (higher MPCR increases gains from punishment).
- **punishment_cost**, **punishment_tech** (cost-to-impact ratio), **punishment network structure**, **punishment existence**: Varied across papers, universally shown as key moderators.
- **all_or_nothing**: Both binary and continuous designs used; efficiency effects differ (especially in threshold/step-level games).
- **chat (communication)**: Well represented; shown to strongly magnify or, in some contexts, substitute for punishment.
- **show_n_rounds, show_other_summaries, show_punishment_id**: Feedback structure and information presentation are major moderators in several papers.

**Indirectly Informed:**
- **default_contrib**: Framing/opt-in vs. opt-out is less commonly manipulated, but some evidence exists (Martinsson et al., 2019).
- **reward_exists, reward_cost, reward_tech**: A moderate subset address reward and compare it to punishment, but coverage is thinner and less standardized.

**Contextually Discussed or Missing:**
- Designs with **full spectrum of endogenous institutional choice** (voting, endogenous institution formation) are present but less prevalent.
- Highly detailed information/feedback variants, complex dynamic PGGs, and rare population/cultural contexts have fewer studies.

---

# 7) Important Limitations

- **The prediction effect of punishment on efficiency is *not* invariant to setting**: outcomes depend critically on institution design, punishment cost/tech, feedback, group composition, and cultural norms.
- **Contribution rates are not substitutes for efficiency**: many studies report both, but in non-standard designs, a change in contributions can be offset (or outweighed) by punishment costs, anti-social punishment, or retaliation.
- **Some combinations of dimensions (e.g., chat enabled + incomplete punishment networks + endogenous reward + high heterogeneity) are not deeply explored**: thus, out-of-sample prediction in those regions is less secure.
- **Cultural and environmental moderators are variable and not always observable/enumerated in lab settings**; antisocial punishment especially may be underestimated in student or WEIRD population labs.
- **Some specific institutional forms (e.g., non-targeted group punishment, exclusion with high cost, random punishment) can produce perverse efficiency effects even when control efficiency is high.**
- **Many lab studies use baseline student populations and artificial incentives**; external validity to non-lab (e.g., real-world CPRs, field populations) may be limited in some cases.
- **Reward mechanisms and their interaction with punishment are less thoroughly tested than punishment alone.**
- **For adjacent designs (CPRs, trust/investment games, team production, etc.), the mapping to classic PGG efficiency is often indirect and requires mechanistic reasoning or cautious use of proxies.**
- **Most studies assume homogeneous, symmetric groups or random assignment; less is known about efficiency effects in persistent, self-sorted, or highly diverse groups.**

---

**Summary**:  
This paper set provides a robust, high-coverage, and nuanced foundation for quantitative prediction of the efficiency impact of enabling punishment in public-goods-game-like environments. **Direct empirical evidence covers the majority of canonical design dimension combinations**. However, **the sign and size of the efficiency effect are contingent upon punishment cost-effectiveness, institution structure, network design, population composition, and baseline efficiency**. **Careful mapping and explicit consideration of moderators are essential for robust prediction**. Reliable prediction is possible within the main parameter space densely covered by the experiments, but caution is recommended in rare/edge-case combinations or where contextual moderators are poorly measured or absent.
