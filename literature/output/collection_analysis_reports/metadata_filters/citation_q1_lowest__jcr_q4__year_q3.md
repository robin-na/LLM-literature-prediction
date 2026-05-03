# 1) Evidence Base

The paper set is moderately broad and consists of 16 papers with a mix of empirical laboratory experiments and theoretical modeling. About half are empirical (primarily lab-based public goods games), providing direct data on key variables, and half are theory papers, offering analytical results and broad conceptual arguments. Several papers focus explicitly on standard public goods games (PGGs), but others extend to variants such as optional-PGG, threshold public good games, generalized exchange, and adjacent dilemmas (e.g., volunteer’s dilemma, repeated prisoner’s dilemma).

Overall, the evidence base is strong on core PGG mechanisms and the efficiency impact of enabling punishment, especially in standard and optional PGG designs. However, some papers contribute only indirectly or contextually, with several discussing adjacent but non-identical game structures or focusing on mechanisms other than explicit costly punishment (e.g., reputation, exclusion, or contracts). There are clear distinctions in the literature between outcome (efficiency/payoff) and behavioral measures (cooperation rate, norm compliance), with most direct empirical evidence favoring efficiency as a key reported metric.

# 2) Task Relevance

- **pgg_or_variant**: Most papers are `exact` matches for standard PGG or design-adjacent variants (e.g., optional PGG, threshold games). A minority focus on adjacent models (generalized exchange, volunteer’s dilemma, prisoners’ dilemma), and a few are contextually relevant, discussing cooperation evolution in more abstract or broader terms.
- **punishment_or_sanctions**: Substantial coverage, with most papers labeled `exact` or `close` due to explicit modeling or experimental enablement of punishment or sanctioning mechanisms. A handful only discuss exclusion, refusal, or reputation, which are adjacent.
- **efficiency_or_related_payoff_outcome**: Coverage ranges from `exact` (clear measurement or modeling of group efficiency, payoff, or welfare) to `adjacent` (reporting mainly on cooperation or contribution without group payoff calculation), with a few having only contextual relevance.

In summary, the set speaks directly to the core prediction target—how enabling punishment alters efficiency in PGG-like settings—especially for standard peer-punishment institutions. However, less is covered about highly parameterized or hybrid game structures, and some adjacent models are included.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes**: 
  - *Directly Measured* — Several empirical studies report group earnings, total payoff, or efficiency (ratio of actual payoff to social optimum) both in control (no punishment) and treatment (punishment enabled) (e.g., Suleiman & Samid, 2021; Kanitsar, 2021).
  - *Theoretically Modeled* — Explicit welfare, social cost minimization, and equilibrium payoff analysis in both peer and centralized punishment settings (Alventosa & Olcina, 2021; Botta et al., 2021; Friehe & Tabbach, 2018).

- **Non-payoff behavioral outcomes**: 
  - Reports on contribution rates, cooperation rates, norm compliance, punishment frequencies, etc., are common, especially in adjacent or theoretical works (e.g., Grund et al., 2020; Selterman, 2019). These are occasionally linked to efficiency, but not always.

- **Ambiguity**: In some works, experimental manipulations affect behavioral measures (cooperation/contribution), with only secondary or indirect inference about welfare or group payoff (e.g., Selterman, 2019). A minority of theory works discuss only mechanism viability or population dynamics (de Almeida, 2021; Hernández, 2021).

# 4) Main Findings Relevant To Prediction

- **Punishment generally increases efficiency**: Enabling peer or institutional punishment in standard PGGs tends to raise group efficiency/payoff above baseline (no punishment) settings (Suleiman & Samid, 2021; Alventosa & Olcina, 2021; Kanitsar, 2021).

- **Magnitude and sign of effect vary**: 
    - The efficiency gain is often *moderate*, not maximal, and highly sensitive to group composition (e.g., prevalence of strong reciprocators vs. norm-keepers) and punishment strategies (Suleiman & Samid, 2021).
    - *Punishment cost* is critical—a high cost to punishers can wipe out efficiency gains, and in some network/game structures (generalized exchange), punishment has no or even negative efficiency impact unless it is costless (Kanitsar, 2021).

- **Theoretical models** reinforce these findings:
    - Punishment effectiveness (magnitude per unit cost) and coverage (fraction punished) are key moderators (Botta et al., 2021; Alventosa & Olcina, 2021).
    - Centralized punishment can, in the best case, transform low-efficiency equilibria to full cooperation when institutional parameters are strong enough, but implementation and enforcement frictions can yield only partial gains (Alventosa & Olcina, 2021).
    - In some adjacent settings (e.g., threshold games, volunteer’s dilemma), outcome-based punishment may be ineffective or counterproductive, while action-based punishment is more robustly efficiency-enhancing (Friehe & Tabbach, 2018; Bolle, 2021).

- **Role of group structure/network**: Dense public-good interaction structures allow punishment effects on efficiency; sparse or circular networks may not (Kanitsar, 2021). Optional participation or loner strategies interact with punishment to permit full cooperation only if punishers reach critical parametric thresholds (Botta et al., 2021).

# 5) Prediction Guidance

- **Enabling peer punishment in a standard PGG** can be expected, on average, to increase efficiency relative to a control where punishment is disabled. The magnitude of the effect depends strongly on:
    - **Punishment parameters**: Cost to punishers, magnitude of punishment, and overall effectiveness.
    - **Group composition and social context**: More strong reciprocators and fewer norm-keepers (who punish both high and low contributors) lead to greater efficiency gains (Suleiman & Samid, 2021).
    - **Network/game structure**: Gains predominantly arise in dense, symmetric structures. In sparser (generalized exchange) networks or threshold games with high punishment costs or collective punishment, gains are much smaller or may be absent (Kanitsar, 2021; Bolle, 2021).

- **Indirect and conditional effects**:
    - Where the punishment is too costly, or power is asymmetrically distributed (selfish punishers dominate), only partial efficiency gains may result, or even losses relative to the control (Eldakar et al., 2018).
    - For games with optional participation, full efficiency is reached only if punishment is sufficiently frequent/effective (Botta et al., 2021).

- **Control efficiency baseline**:
    - The effect of enabling punishment generally builds on the control game's average efficiency. If control efficiency is already high (due to existing mechanisms—e.g., meritocracy, communication), the marginal gain from adding punishment may be small or zero (Nax et al., 2018).
    - In setting with low baseline efficiency (no other incentives), the introduction of punishment is more likely to result in large efficiency gains.

- **Parameter regime cautions**:
    - For highly costly punishment regimes (relative to group size/MPCR), the marginal efficiency gain may be close to zero or even negative due to resource wastage.
    - Design dimensions surrounding punishment cost, effectiveness, and social observability (punishment_id, other_summaries) are crucial but only partially covered in this literature set.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions**:
- `player_count`: Most core empirical and theoretical studies specify and examine this.
- `num_rounds`: Treatments are generally multi-round (dynamics covered).
- `mpcr`: Marginal per-capita return universally recognized as a moderator.
- `all_or_nothing`: Binary vs. continuous contribution is frequently systematized.
- `punishment_cost`: Explicitly addressed—central to almost all efficiency findings.
- `punishment_tech` (effectiveness, magnitude): Covered theoretically and occasionally empirically.
  
**Indirectly or Contextually Informed**:
- `chat`: Sometimes mentioned, but rarely a focus; communication is less central except in a few experimental setups.
- `reward_exists`, `reward_cost`, `reward_tech`: A couple of theory papers discuss reward as an alternative or supplement (Skarzhinskaya & Tsurikov, 2021; Friehe & Tabbach, 2018), but most studies isolate punishment-only cases.
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Occasionally described as part of the interface but not systematically analyzed for effect on efficiency.

**Effectively Missing or Only Contextually Discussed**:
- `default_contrib`: Framing of endowment/contribution (opt-in vs. opt-out) is not systematically varied in this set.
- `show_punishment_id`, `show_other_summaries`: Only minimal or secondary attention.
  
# 7) Important Limitations

- **Context dependence**: Many efficiency results depend on group composition (behavioral types), power asymmetry, and cultural/societal context, which are not parameterized or controlled in standard predictive tasks.
- **Design parameter sparsity**: Not all 14 game design dimensions are equally covered; evidence is strong for player count, rounds, MPCR, and punishment cost, but weak or patchy for others such as chat, framing, information displays, and reward dimensions.
- **Adjacency and generalizability**: Some results come from adjacent games (volunteer’s dilemma, prisoners’ dilemma, threshold games) or from unusual implementations of sanctioning (e.g., exclusion, refusal to cooperate, centralized punishment), requiring care in generalizing to standard PGGs with peer punishment.
- **Cost-effectiveness of punishment**: Several papers (Kanitsar, 2021; Eldakar et al., 2018) caution that punishment increases group earnings only if costs are not excessive; otherwise, resources may be dissipated with little or no welfare gain.
- **Variance and heterogeneity**: Enabling punishment tends to *increase variance* in group outcomes—some groups reach near-optimal efficiency, while others remain inefficient depending on internal dynamics (Di Guida et al., 2021; Suleiman & Samid, 2021).
- **Lack of high-dimensional empirical tests**: Interactions between multiple dimensions (e.g., how chat and punishment jointly affect efficiency) are under-explored; studies typically vary one or two parameters at a time.
- **Predominance of lab settings and simplified environments**: External validity for field or naturally occurring environments may be limited.
- **No direct treatment of information design**: Variables such as punishment observability and payoff transparency are only occasionally described and not experimentally manipulated.

---

**In summary:** The literature strongly supports the claim that enabling (peer or institutional) punishment in public-goods-game-like environments generally increases efficiency relative to disabling punishment, all else equal. The magnitude of this effect, and conditions under which it will occur, depend critically on the cost and effectiveness of punishment, network/game structure, baseline efficiency, and the behavioral composition of groups. Only a subset of game design dimensions are directly informed in this literature set, and several important moderators (information design, framing, reward systems, communication) remain underexplored for direct payoff effects.
