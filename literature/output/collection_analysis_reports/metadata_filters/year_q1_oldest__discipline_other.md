# 1) Evidence Base

The literature set consists of 16 papers, with a mix of empirical (mostly laboratory experimental) and theory papers. The majority of empirical work most directly relevant to the prediction task comes from a small subset of true public goods game (PGG) experiments with explicit payoff-based outcomes (e.g., Grechenig et al., 2010), alongside several review or theoretical syntheses grounded in prior empirical work (e.g., Frey & Rusch, 2012; Kraak, 2011). Other studies extend models or theorize about social dilemmas, sanctioning, altruism, or cooperation in adjacent domains, including evolutionary, cultural, policy, and real-world analog settings.

The set is not especially broad for the exact prediction task—there are only a handful of studies directly focused on experimental PGGs with efficiency outcomes under variations in the punishment institution. Most other papers provide conceptual, mechanistic, or indirect relevance drawn from theory, evolutionary models, or non-PGG experiments. A few papers are only contextually or weakly relevant, addressing sanctions, information, or group processes without studying their impact on efficiency in a public goods context.

# 2) Task Relevance

**pgg_or_variant:**
- *Exact relevance*: About 5 papers (e.g., Grechenig et al., 2010; Rosas, 2008; Frey & Rusch, 2012; Kraak, 2011) study or theorize about standard or close variants of the public goods game.
- *Close relevance*: Several others analyze games structurally similar to PGGs (trust games, climate games), or discuss evolutionary analogs to public goods dilemmas.
- *Adjacent/weak relevance*: Many papers are adjacent but not direct (e.g., prisoner's dilemma, dictator games, real-world policy, animal cooperation).

**punishment_or_sanctions:**
- *Exact relevance*: About half specifically examine or theorize about peer punishment or sanctions in PGGs or close analogues.
- *Close to adjacent relevance*: Some focus largely on reputation, exclusion, tax-based institutional punishment, or broader sanctioning mechanisms.
- *None/weak relevance*: Several papers do not manipulate or analyze punishment per se.

**efficiency_or_related_payoff_outcome:**
- *Exact relevance*: Only a handful of papers report or analyze efficiency or directly related payoff outcomes in PGGs with/without punishment (e.g., Grechenig et al., 2010; Rosas, 2008).
- *Close/adjacent*: Others discuss cooperation rate, norm compliance, or evolutionary stability of altruism without reporting group payoffs.
- *Weak/none*: Several focus entirely on non-payoff behavioral measures or theoretical arguments about norms, beliefs, or motivation, not efficiency.

# 3) Outcomes Measured In The Literature

- **Payoff-based outcomes** (group efficiency, total payoff, welfare, surplus):
    - Directly measured in a minority of empirical and theory papers (e.g., Grechenig et al., 2010; Kraak, 2011).
    - Some theoretical syntheses extrapolate likely payoff effects from known cooperation rates (Frey & Rusch, 2012).
    - Many relevant theory papers conceptualize efficiency but do not measure it empirically.

- **Non-payoff behavioral outcomes** (contribution rates, compliance, cooperation frequency, norm adherence):
    - Much more common across both empirical and theory papers.
    - Often used as proxies for or mechanistically linked to efficiency, but not always congruent with actual group payoff improvements.
    - Frequently relied upon in adjacent or analogy-driven discussions.

- **Other outcomes**:
    - Perceptions of fairness or legitimacy (in policy papers) and the persistence/robustness of altruism (in evolutionary simulations).
    - Information seeking about norms or others’ actions (in information/decision-making studies).

# 4) Main Findings Relevant To Prediction

- **Punishment’s effect on efficiency is highly *design-contingent***:
    - *Positive efficiency effect*: When peer punishment is enabled in a standard PGG with accurate, visible information about contributions, efficiency (total group payoff relative to the ideal) increases, as observed in both empirical (Grechenig et al., 2010) and theory papers (Rosas, 2008; Frey & Rusch, 2012; Kraak, 2011).
    - *Negative efficiency effect*: When information about contributions is noisy or imperfect, punishment becomes untargeted, antisocial punishment increases, and efficiency drops below the no-punishment baseline (Grechenig et al., 2010).
    - *Time horizon matters*: Efficiency gains from punishment often only manifest in longer games (many rounds), as early rounds are marred by high punishment costs that decline only if cooperation stabilizes (Frey & Rusch, 2012).
    - *Punishment mechanism type matters*: Exclusion-based or reputation-linked punishment can sustain higher and more stable efficiency than direct costly peer punishment, which is prone to over- or under-punishment depending on group composition (Rosas, 2008).
    - *Communication and reputation*: Adding communication (chat) and mechanisms for reputation can increase cooperation and efficiency, either by reducing costly punishment or by making punishment more targeted and socially acceptable (Kraak, 2011; Raihani & Aitken, 2011).
    - *Automatic/institutional sanctions*: Non-peer (tax-based, automatic) punishment can robustly drive compliance and high group payoffs, as in environmental/climate game analogs (Brick & Visser, 2010), sometimes at the cost of crowding out voluntary contributions.

- **Some findings are strictly behavioral—not payoff-based**:
    - Theory and simulation studies show that punishment increases cooperation, norm compliance, or altruism, which may or may not translate into higher efficiency depending on the cost structure (Woodcock & Heath, 2002; Sripada, 2005).
    - In evolutionary and real-world analogs, mechanisms supporting altruism do not always maximize group payoff—punishment may stabilize cooperation but at high cost, or serve other evolutionary purposes not related to group welfare (Nakao & Machery, 2012).

- **Moderators**:
    - *Information accuracy*: Essential for punishment to raise efficiency.
    - *Number of rounds*: Longer repeated games see stronger efficiency gains from punishment.
    - *Group size*: Effects may vary; theory suggests punishment helps sustain cooperation in larger groups but some empirical results focus on small-N.
    - *Punishment cost/effectiveness*: High cost or low effectiveness of punishment can negate or reverse efficiency gains.
    - *Communication/reputation mechanisms*: Enhance positive effects of punishment or, sometimes, substitute for it.

# 5) Prediction Guidance

This literature set supports the following guidance for prediction of treatment efficiency in PGG-like environments with peer punishment:

- **Primary conditional prediction**: The effect of enabling peer punishment on group efficiency is highly sensitive to the design context, especially the accuracy of information about contributions (Grechenig et al., 2010). If monitoring is accurate and transparent, enabling punishment is likely to increase efficiency over the control (no-punishment) baseline, especially in repeated games or with communication.
- **Key moderators** to include in prediction:
    - *Information accuracy (not always a prediction variable—best proxied by `show_other_summaries` or similar)*.
    - *Number of rounds (`num_rounds`)*: Longer games are more likely to see efficiency gains from punishment.
    - *Group structure/player count (`player_count`)*: Theoretical support but limited direct causal evidence in this set.
    - *Punishment cost and effectiveness (`punishment_cost`, `punishment_tech`)*: Lower cost and higher impact per unit support greater efficiency effects.
    - *Communication and reputation mechanisms (`chat`)*: Amplify positive impacts of punishment.
- **Use control efficiency as an anchor**: The higher the baseline efficiency, the more marginal gains (or losses) from punishment depend on whether punishment deters free-riding cost-effectively or simply adds wasteful antisocial sanctions.
- **Caution—context limits**: Where information is noisy, or where punishment is expensive/ineffective, enabling peer punishment is as likely to reduce as to increase efficiency. The presence of exclusion or reputation-based punishment (not always manipulable) may mitigate downsides.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed:**
- `player_count`, `num_rounds`, `chat`, `mpcr`, `punishment_cost`, `punishment_tech`, `all_or_nothing`—Multiple papers, especially empirical and theory PGG papers, link these to efficiency and treatment-punishment effects (Grechenig et al., 2010; Rosas, 2008; Kraak, 2011; Bicchieri et al., 2004; Frey & Rusch, 2012).
- *Number of rounds* is well-theorized as moderating the effect of punishment (Frey & Rusch, 2012; Bicchieri et al., 2004).
- *Communication (`chat`)* and reputation are directly discussed with empirically informed impact (Kraak, 2011; Raihani & Aitken, 2011).

**Indirectly informed:**
- `reward_exists` (reward mechanisms are discussed as complementary in a few theory papers, but less as direct experimental variation).
- `show_other_summaries` and `show_n_rounds`—sometimes referenced under information accuracy or transparency, but not always manipulated as a design variable.
- `all_or_nothing`—discussed in the abstract or in evolutionary models, not as a specific treatment.

**Only contextually discussed or effectively missing:**
- `default_contrib`, `show_punishment_id`, `reward_cost`, `reward_tech`—Rarely mentioned or treated as critical in the prediction-relevant studies.
- *Game-theoretic and cultural context variables* (e.g., group matching, real-world institutional settings, stakeholder involvement) are referenced in some theory and contextual papers but not mapped to the experimental dimensions.

**Important design elements NOT formally addressed:**
- The accuracy and format of feedback (beyond whether others' outcomes are 'shown').
- The exact mapping between specific institutional sanctions and the peer punishment mechanisms most often modelled in laboratory PGGs.

# 7) Important Limitations

- **Few studies directly report efficiency outcomes**: There are only a small number of empirical papers measuring group payoff or welfare under punishment vs. control. Most evidence is indirect or inferred via cooperation rates or theory.
- **Empirical results are *condition-sensitive***: Key results (e.g., punishment increases efficiency) depend strongly on specific contexts—information accuracy, cost structure, available punishment mechanisms—limiting unconditional generalizability.
- **Non-payoff outcomes dominate**: Many papers extrapolate from cooperation rates or norm adherence, which does not always translate to true efficiency improvements—especially when punishment itself is costly or misapplied.
- **Scarcity of manipulation across prediction dimensions**: Many of the 14 dimensions in the design space are not independently varied or analyzed in a factorial way, leaving key gaps for prediction (e.g., there's little direct evidence on `show_punishment_id`, various reward parameters, or default contribution framing).
- **Limited real-world correspondence**: While some theory and policy papers analogize to public goods or sanctions in society/nature, they seldom operationalize these analogies in terms of group efficiency measured as in laboratory PGGs.
- **Potential for ambiguous or conflicting interpretation**: Some theoretical arguments question whether punishment evolved for efficiency or for other evolutionary purposes, cautioning against naïve attribution of positive efficiency effects to enforcement mechanisms (Nakao & Machery, 2012).

# Summary Table: Prediction-Relevant Evidence Across Design Dimensions

| Dimension               | Evidence for Direct Efficiency Effect of Punishment?      |
|-------------------------|----------------------------------------------------------|
| player_count            | Theory papers and some empirical studies—*moderate*      |
| num_rounds              | Strong theoretical & empirical support                   |
| chat                    | Supported as moderator (theory & review)                 |
| all_or_nothing          | Limited, mostly theory                                   |
| default_contrib         | Not addressed                                            |
| mpcr                    | Some theory and empirical support                        |
| punishment_cost         | Widely discussed as moderator                            |
| punishment_tech         | Important per theory, rare as experimental variation     |
| reward_exists           | Indirect/theoretical emphasis, limited direct data       |
| reward_cost             | Not addressed                                            |
| reward_tech             | Not addressed                                            |
| show_n_rounds           | Limited discussion                                       |
| show_other_summaries    | Important empirically (as proxy for information accuracy)|
| show_punishment_id      | Not addressed                                            |

---

## Overall: This literature supports nuanced, conditional prediction that efficiency following the introduction of peer punishment depends sensitively on dimensions such as information accuracy, time horizon, punishment cost/tech, and communication/reputation mechanisms; however, only a subset of these dimensions is directly informed by group efficiency outcome data, and many others are covered only in theory or by analogy. Use caution when generalizing outside empirically studied design spaces.
