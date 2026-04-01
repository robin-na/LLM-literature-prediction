# 1) Evidence Base

The paper set is composed almost entirely of **theoretical models** (majority), with a minority of **empirical** (including lab and field experiments) and a few review or synthesis works. Many of the theoretical models directly instantiate public goods games (PGGs) or very closely related n-person social dilemma structures—often with explicit, manipulable punishment mechanisms and, less frequently, reward mechanisms. A substantial subset of these models is parameterized to allow variation in core game design dimensions such as group size, rounds, marginal per capita return (mpcr), punishment cost, and punishment effectiveness.

While the base is **broad in the scope of theory covered**, it is notably **narrower with respect to large-sample empirical tests**. Direct experimental papers are relatively rare, and, where present, mostly focus on behavioral mechanisms rather than reporting payoff or efficiency outcomes. Most empirical studies that do exist often measure non-payoff behavioral outcomes (e.g., cooperation rates, punishment frequency) rather than treatment-control efficiency ratios. 

Overall, the evidence base is **well-suited to mapping out parameter dependencies and plausible mechanisms in PGG-like games with punishment**, but it is less suited for directly quantifying or validating empirical efficiency outcomes under varying design dimensions.

# 2) Task Relevance

## `pgg_or_variant`
- **exact**: ~10 papers model or directly reference public goods games with all canonical features (`Eldakar et al., 2007`; `Deng et al., 2012`; `Milinski & Rockenbach, 2012`, etc.).
- **close/adjacent**: Many others use adjacent but not identical frameworks (iterated prisoner's dilemma, mutualisms, resource-exchange, etc.).
- **none**: A few syntheses and reviews are conceptual with no direct model.

## `punishment_or_sanctions`
- **exact**: Most papers explicitly include punishment (peer punishment, costly/anti-social punishment) as a core treatment; several also consider alternative enforcement or reward mechanisms.
- **adjacent/weak**: Some analyze conditional cooperation, retaliation, or partner choice as analogous to punishment but without explicit cost/implementation structure, or focus only on reputation mechanisms.

## `efficiency_or_related_payoff_outcome`
- **exact/close**: About half of the theory papers directly compute or reason about efficiency: the ratio of group payoff under treatment to fully cooperative baseline (e.g., `Eldakar et al., 2007`; `Deng et al., 2012`; `Milinski & Rockenbach, 2012`; `Okada & Bingham, 2008`).
- **adjacent/weak**: Many empirical works (and some theory) report on contributions, cooperation rates, or the prevalence of punishing strategies but do **not** report efficiency or payoff.
- **none**: Very few empirical experiments provide efficiency as a reported outcome.

In sum: There is **high exact relevance for the PGG structure and for punishment as a treatment** in theory, but **less consistent reporting of efficiency or direct payoff measures**, especially in the empirical papers. Most payoff-based support comes from formal or simulation models.

# 3) Outcomes Measured In The Literature

**Payoff-based outcomes** (directly relevant):  
- **Efficiency (group payoff relative to full cooperation):** Explicitly calculated in about half the theory papers, sometimes as mean group welfare, mean fitness, or surplus (`Eldakar et al., 2007`; `Deng et al., 2012`; `Milinski & Rockenbach, 2012`; `Okada & Bingham, 2008`).
- **Group payoff / aggregate wealth / mean fitness:** Used interchangeably with efficiency in several models.

**Non-payoff behavioral outcomes** (often reported, but not directly efficiency):  
- **Cooperation/contribution rate, punishment frequency, prevalence of strategies** (e.g., `de Weerd & Verbrugge, 2011`; `Jaffe, 2004`; `Seip et al., 2009`; `Marlowe et al., 2011`).
- **Norm compliance, retaliation, or anger drivers of punishment** (e.g., `Seip et al., 2009`).
- **Strategy evolution and stability** (how likely agents are to punish, or develop certain behavior profiles).

**Empirical quantification of efficiency** is rare; most lab/field studies focus on **behavioral frequencies** without translating these into group welfare or efficiency ratios.

# 4) Main Findings Relevant To Prediction

## General Direction of Punishment's Effect on Efficiency

- **Punishment often increases efficiency relative to control:** Multiple theoretical models robustly find that, when peer punishment is enabled, efficiency improves over baseline *if* punishment is not prohibitively costly or too infrequently used. Effective (low-cost, severe) punishment mechanisms reliably suppress defection and encourage cooperation, raising group payoffs/efficiency (`Eldakar et al., 2007`; `Deng et al., 2012`; `Milinski & Rockenbach, 2012`; `Okada & Bingham, 2008`).

- **Critical moderating role of punishment cost/effectiveness and group structure:** The efficiency benefit is strongly diminished—or can become negative—if punishment is very costly relative to its deterring impact (`Powers et al., 2012`; `Jaffe, 2004`; `Weibull & Salomonsson, 2006`). Group size, rounds, and game length serve as additional moderators.

- **Possibility of negative or mixed effects:** Several models highlight scenarios where punishment *reduces* efficiency: e.g., anti-social punishment (punishment of cooperators—`Powers et al., 2012`), high cost relative to benefit (`Jaffe, 2004`), or in highly competitive/low-structure environments (`POLLOCK, 1988`; `Weibull & Salomonsson, 2006`).

- **Reward vs. punishment:** Where compared, punishment tends to be more robust in stabilizing high efficiency, but reward (sometimes in metanorm form) can be more effective in low-cooperation populations or under some population structures; reward alone rarely leads to full efficiency (`Forsyth & Hauert, 2011`; `Kendal et al., 2006`).

## Parameter-specific Effects (Design Dimensions)

- **Punishment cost, punishment effect/tech, and cost/effect ratio:** Lower cost and higher severity/efficacy of punishment are consistently associated with greater efficiency gains. Severe, rare, or concerted punishment is especially effective at raising efficiency without excessive cost (`Deng et al., 2012`; `Okada & Bingham, 2008`).

- **Group size (player_count):** Several models show decreasing positive impact (or increasing negative impact) of punishment on efficiency as group size increases, due to dilution of individual incentives and/or increased prevalence of anti-social punishment (`Eldakar et al., 2007`; `Powers et al., 2012`).

- **Number of rounds (num_rounds):** Longer games increase the efficacy of punishment at sustaining high efficiency; one-shot or very short games may not benefit or may even be harmed by punishment (`Eldakar et al., 2007`; `Leimar, 1997`). 

- **MPCR:** High MPCR (i.e., higher return on cooperation) supports higher efficiency *even without punishment*, but amplifies the positive impact of punishment (`Takezawa & Price, 2010`).

- **Reward exists:** Effects are less well-covered, but available evidence suggests reward mechanisms can increase efficiency somewhat, but are less stable than punishment (`Forsyth & Hauert, 2011`).

- **Other dimensions:** Few papers explicitly treat design variables such as chat (communication), all_or_nothing, default_contrib, show_n_rounds, show_other_summaries, or show_punishment_id. Where discussed, these are mostly set to typical experimental defaults.

## Mechanism arguments

- **Partner identification/visibility:** While not always parameterized, some papers note reputation or identification mechanisms (e.g., seeing who punished, or indirect reciprocity) enhance punishment's efficacy at increasing efficiency (`Milinski & Rockenbach, 2012`).

- **Metanorms and combination mechanisms:** Metanorms (rewarding punishers or punishing non-punishers), or combining punishment with reputation/reward, can expand the parameter space for efficient outcomes (`Kendal et al., 2006`; `Rosas, 2010`).

# 5) Prediction Guidance

- **Baseline control efficiency (no punishment):** The literature suggests that the *increment* in efficiency due to enabling punishment will *depend on how high or low control efficiency is*, with the largest relative gains when the baseline (control) is low (i.e., high free-riding).

- **Most influential design dimensions for predicting treatment efficiency:**
    - **Punishment cost and effectiveness:** Lowering cost or raising efficacy of punishment predicts larger efficiency increases.
    - **Player count (group size):** Efficiency gains are most robust in small groups; larger groups see diminished returns or risk anti-social punishment effects.
    - **Number of rounds:** More rounds favor stable, higher efficiency via punishment.
    - **MPCR:** Higher mpcr predicts higher attainable efficiency, regardless of punishment; its inclusion is thus critical for calibrating both control and treatment predictions.
    - **Presence of anti-social punishment or reward:** When explicitly modeled, anti-social punishment reduces or negates the positive impact on efficiency, while reward can sometimes substitute for, or complement, punishment.

- **Game structure and extra features:** In the absence of chat, partner choice, or reputation, theory suggests efficiency gains will depend even more on punishment parameters. When reputation or identification is possible, punishment is more effective and cost is lower per unit efficiency gained.

- **Predictive uncertainty:** Scenarios with very high punishment cost, very large groups, short time horizons (few rounds), or high rates of anti-social punishment can lead to *no gain or even decline* in group efficiency.

- **Empirical limitations:** Most quantitative prediction of treatment efficiency must *rely on theoretical, not empirical, evidence* for mapping from design dimensions to efficiency outcomes.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions** (explicit quantitative or mechanistic analysis in >3 theory papers):
- `player_count`: Strong (numerous theory models; diminishing returns with increased group size, sometimes non-linear).
- `num_rounds`: Strong (longer games = more efficacy from punishment; short = less or none).
- `mpcr`: Strong/moderate (always shaped baseline efficiency; interacts with punishment effects).
- `punishment_cost`, `punishment_tech` (`punishment_magnitude`): Very strong (these are the most frequently parameterized across theory models with explicit impact on efficiency shifts).
- `all_or_nothing`: Moderate (often modeled as a binary contribution, less evidence on continuous vs. all-or-nothing).
- `reward_exists`, `reward_cost`, `reward_tech`: Moderate (some models include, but less coverage than punishment).
- `show_other_summaries`, `show_n_rounds`: Weak (occasionally parameterized, rarely discussed as moderators).
- `show_punishment_id` (`identity`): Weak (some mechanism arguments suggest impact but rarely manipulated).

**Only contextually discussed or sparsely informed:**
- `chat`: Very little explicit analysis.
- `default_contrib`: Not treated as a variable.
- `show_other_summaries`, `show_n_rounds`, `show_punishment_id`: Rarely treated, but occasionally mentioned in relation to information or institutional design.

**Effectively missing:**
- There is almost no direct investigation of the effects of chat, default contribution framing, visibility of punishment or rewards, or fine-grained round-by-round information on downstream efficiency.

# 7) Important Limitations

- **Empirical weakness:** Most evidence is theoretical or simulation-based, with very few empirical studies reporting efficiency or total payoff as an outcome.
- **Efficiency measurement scarcity:** Even in theory, payoff-based outcomes are sometimes inferred or adjacent rather than explicitly computed as efficiency ratios.
- **Parameter sparsity for non-core dimensions:** Several prediction dimensions (e.g., chat, default_contrib, show_punishment_id) are insufficiently or not at all represented; guidance for these is speculative.
- **External validity warnings:** Most models use simplified assumptions (well-mixed populations, no partner selection, pure cost-benefit ratios) that may not capture real-world institutional detail or player cognition.
- **Potential for negative effects (disagreement/ambiguity):** Some models explicitly find conditions where punishment reduces efficiency (e.g., anti-social punishment, high costs, large groups). Not all papers agree that punishment is generally efficiency increasing.
- **Behavioral vs. payoff conflation risk:** Many lab/field studies focus on increased cooperation or punishment frequency and infer efficiency gains without actual payoff measurement; such inferences may not be reliable.
- **Lack of cross-dimensional/interaction exploration:** The joint effect of multiple less-studied design dimensions (e.g., communication plus punishment plus reward plus identification) is mostly unaddressed.

---

**In summary**: The literature set provides a detailed, mostly theoretical mapping of how punishment is expected to alter efficiency (payoff) in public-goods-game-like settings as a function of core game design parameters. Predictive guidance is strongest (and most quantifiable) for dimensions such as group size, rounds, mpcr, punishment cost, and punishment effectiveness. Evidence is mixed or ambiguous in certain parameter regimes (e.g., high cost, large groups, anti-social punishment), and empirical efficiency outcomes are infrequently reported. Many design dimensions relevant for real-world or experimental PGGs remain underrepresented.
