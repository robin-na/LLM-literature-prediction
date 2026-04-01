# 1) Evidence Base

The paper set comprises 16 sources spanning both theory and empirical work, with a strong representation from evolutionary and philosophical theory papers and a minority of experimental or observational studies. Among the empirical studies, only a few are direct experimental tests in public goods or close variants; most others provide broader analogies, simulations, or qualitative insights from adjacent domains (e.g., market entry games, collaborative governance). Theoretical work frequently employs modeling and simulation rather than direct observation or experimentation.

The set is **narrow to moderately broad** for the specific downstream prediction task: while it includes several papers exactly or closely aligned with public goods games and punishment (three with exact or near-exact scope on efficiency), much of the evidence is theoretical or focuses on non-payoff outcomes (e.g., cooperation rates, norm adherence) instead of the efficiency outcome central to the prediction task.

# 2) Task Relevance

### Dimension 1: `pgg_or_variant`

- **Relevance**: *exact* in 3 theory papers (Vasconcelos et al., 2022; Rosas, 2008; Frey & Rusch, 2012), *close* or *adjacent* in a handful of others (e.g., Brick & Visser, 2010; O'Connor, 2016; Xu et al., 2014).
- **Assessment**: The evidence base has **moderate directness** regarding public goods or sufficiently close variants, primarily in theory rather than repeated empirical laboratory work.

### Dimension 2: `punishment_or_sanctions`

- **Relevance**: *exact* or *close* in the same key theory papers and some adjacent variants (e.g., rating-based sanctions, third-party exclusion, tax-based sanctions). Most other references are conceptual or discuss punishment as a sustaining/cooperation factor without direct operationalization.
- **Assessment**: The literature **addresses punishment mechanisms directly in PGG or variants** in several theory sources, though empirical coverage is thinner and sometimes focuses on institutional or automatic sanctions (rather than peer punishment).

### Dimension 3: `efficiency_or_related_payoff_outcome`

- **Relevance**: *exact* in three theory papers (Vasconcelos et al., 2022; Rosas, 2008; Frey & Rusch, 2012); most other papers are *adjacent* or *weak*, being more concerned with cooperation rates or qualitative group outcomes rather than group efficiency as a share of maximum possible payoff.
- **Assessment**: **Empirical evidence for how punishment changes group efficiency (payoff ratio) in PGG-like games is sparse and mainly theoretical**. Most empirical and simulation studies either focus on behavioral proxies (contribution/compliance rates, norm adherence) or present qualitative results.

# 3) Outcomes Measured In The Literature

- **Payoff-based Outcomes**: 
  - *Group efficiency* (ratio of actual to maximum possible payoff) is explicitly modelled or discussed in a few theory papers (Vasconcelos et al., 2022; Rosas, 2008; Frey & Rusch, 2012) and some simulation work (Xu et al., 2014; O'Connor, 2016).
  - Some empirical studies (Brick & Visser, 2010; Rommel, 2015) report adjacent metrics like average earnings, compliance rates, or welfare, but do not generally compute or report efficiency in the formal sense.

- **Non-payoff (Behavioral) Outcomes**: 
  - Frequently measured include *contribution rates*, *compliance rates*, *norm adherence*, *punishment frequencies*, *proportion of cooperators or altruists*, and *market entry rates*.
  - Many theory papers focus on evolutionary dynamics—altruist persistence, norm evolution, and stability of cooperation—without connecting these to group payoff or efficiency in a formal sense.

- **Distinction**: Only three theory papers (Vasconcelos et al., 2022; Rosas, 2008; Frey & Rusch, 2012) provide **explicit payoff- or efficiency-based analyses relevant for the downstream prediction task**. The majority of the remainder rely on behavioral or evolutionary proxies.

# 4) Main Findings Relevant To Prediction

1. **Punishment generally increases efficiency under the right conditions, but not always:**
   - **Theory and meta-study synthesis** indicates that punishment, when enabled and properly instituted, *usually* increases both cooperation and efficiency in PGGs, particularly when institutional design matches the social dilemma's scale and when participants have sufficient information and memory (Vasconcelos et al., 2022).
   - **Direct costly punishment** (peer-to-peer) can lead to inefficiency if overused (too many resources wasted on punishment) or underused (defectors go unpunished), with efficiency contingent on group composition and the type of punishment enabled (Rosas, 2008).
   - **Exclusion or institutionalized punishment** (third-party, automatic sanctions) is associated with more stable improvements in efficiency (Rosas, 2008; Brick & Visser, 2010).

2. **Time horizon and group stability moderate punishment effects:**
   - **Short games** (few rounds) or stranger-matching scenarios often see lower or negative efficiency effects from punishment due to unrecovered costs.
   - **Long games** (many rounds), stable partnerships, and effective punishment mechanisms allow efficiency gains by allowing initial punishment to stabilize cooperation, after which punishment expenditures decline (Frey & Rusch, 2012).

3. **Punishment effectiveness and cost parameters are critical:**
   - **Low-cost, high-impact punishment** is more likely to produce net efficiency gains (Frey & Rusch, 2012; Rosas, 2008).
   - If punishment is too costly or insufficiently deterrent, efficiency gains are muted or negative (Frey & Rusch, 2012).

4. **Information, group size, and institution choice matter:**
   - **Learning opportunities** (memory, information, institutional adoption rules) strongly determine whether punishment achieves high efficiency (Vasconcelos et al., 2022).
   - **Group size** acts through scale/matching effects: larger groups may face coordination and information challenges that reduce punishment's efficacy unless supported by institutional design.

5. **Empirical studies with adjacent designs find institutional sanctions (not peer) are highly effective at compliance, with likely efficiency gains, but may crowd out voluntary contributions above the minimum (Brick & Visser, 2010).**

6. **Most other theoretical and empirical studies focus on cooperation, not efficiency or payoff, so their findings are best read as indirect support for the efficiency-enhancing potential of well-designed punishment, but do not supply effect sizes or quantitative predictions.**

# 5) Prediction Guidance

- **When control efficiency is low** (inefficient cooperation), and the game design enables peer or institutional punishment with *effective, affordable punishment technology*, *sufficient rounds*, and either stable groups or adaptive punishment institutions, **treatment efficiency is likely to be much higher with punishment enabled**—potentially approaching full cooperation/maximum payoff in the best cases (Vasconcelos et al., 2022; Frey & Rusch, 2012; Xu et al., 2014).
- **Punishment is less likely to improve or may even harm efficiency** when:
  - The time horizon is short,
  - Punishment cost is high and/or impact is low,
  - Groups are unstable or matching is random (stranger treatments),
  - The environment limits information, learning, or memory (Vasconcelos et al., 2022; Frey & Rusch, 2012).
- **Type of punishment matters**: Peer-to-peer costly punishment is vulnerable to inefficiency through wasted resources, whereas exclusion- or rule-based punishment (taxes/fines, rating systems) can directly enforce compliance and efficiency (Rosas, 2008; Brick & Visser, 2010; Xu et al., 2014).
- **Information structure, transparency, and group scale** (player_count, show_other_summaries, show_n_rounds) should be considered: well-informed agents with sufficient memory and ability to align institutions with the task (e.g., local vs. global goods) are more likely to achieve high efficiency with punishment (Vasconcelos et al., 2022).
- **Evidence for the effects of other design dimensions** (chat, reward mechanisms, contribution framing) is sparse or only addressed indirectly.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- `player_count`: Influences institutional effectiveness, group-local alignment, and punishment robustness (Vasconcelos et al., 2022; Rosas, 2008; Xu et al., 2014).
- `num_rounds`: Longer (more rounds) favor efficiency gains from punishment; shorter, less so (Frey & Rusch, 2012).
- `punishment_cost`, `punishment_tech`: Central predictors of whether punishment is efficient (all three theory papers).
- `mpcr`: Affects returns for cooperation (Vasconcelos et al., 2022).
- `show_other_summaries`, `show_n_rounds`: Information and learning channels impact institutional adoption and efficiency (Vasconcelos et al., 2022; O'Connor, 2016).
- `all_or_nothing`: Modeled but less discussed.
- `reward_exists`, `reward_cost`, `reward_tech`: Tangentially referenced (Montoya et al., 2015).

**Indirectly Informed/Discussed:**
- `chat`: Discussed empirically (Brick & Visser, 2010) as improving contributions but less reliable than sanctions.
- `default_contrib`: Framing alluded to as affecting prosociality, but not extensively analyzed.
- `punishment_magnitude`: Implied where cost/benefit tradeoffs are discussed.
- `show_punishment_id`: Presence affects reputational dynamics in some theory models.

**Effectively Missing:**
- Quantitative analysis or empirical evidence on most dimensions except those above.
- Detailed effects of *reward mechanisms* and their interaction with punishment.

# 7) Important Limitations

- **Empirical evidence on efficiency effects is sparse; theoretical models dominate.** Only a handful of studies (none of them recent large-sample experimental papers) provide group efficiency outcomes for PGGs with and without punishment.
- **Most studies focus on behavioral or evolutionary dynamics (cooperation, norm compliance, altruist prevalence), not formal efficiency or group payoff.** This creates a risk of proxy error if behavioral improvements do not fully translate to payoff gains, especially given costs of punishment.
- **Limited direct coverage of several key game dimensions:** Chat, reward mechanisms, contribution defaults, and visibility/framing are mostly untested or only contextually mentioned.
- **Heterogeneity in punishment mechanisms:** Many studies focus on peer punishment, while empirical effects for institutional or rule-based punishments (tax/fine, ratings, ostracism) may not transfer directly to peer-punishment settings.
- **Ambiguous/mixed findings:** Some models predict punishment may decrease efficiency under certain conditions (high punishment cost, short time horizon, over-punishment scenarios).
- **Adjacent or non-PGG domains supply only indirect support.** Extrapolation from settings like network sharing, market entry, or collaborative governance may overstate generalizability.
- **Quantitative effect sizes are generally absent.** Most claims are directional or theoretical, with little basis for calibrated quantitative prediction. Thus, downstream predictions should maintain conservative uncertainty bounds, especially under unexplored design combinations.

---

**Summary:**  
The literature provides **strong theoretical but limited direct empirical support** for the expectation that enabling effective peer punishment in inefficient public goods games will increase efficiency, with moderating effects for punishment cost, group structure, time horizon, and information. Prediction should be cautious where quantitative calibration is needed, given the proxy reliance and gaps in design coverage.
