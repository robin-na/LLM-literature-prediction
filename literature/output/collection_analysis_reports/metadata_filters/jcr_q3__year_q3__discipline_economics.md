# 1) Evidence Base

The paper set is moderately broad, containing 26 papers that span both empirical (predominantly laboratory experiments) and theoretical research. The majority of empirical papers focus on public goods games (PGGs), common pool resource (CPR) dilemmas, trust games, and variants thereof. Several theory papers offer formal models of repeated social dilemmas, emphasizing conditions under which punishment can support high-efficiency outcomes.  

The evidence base skews toward classic or "lab-standard" PGG settings, with considerable direct empirical evidence for linear PGGs and close variants. Central topics include peer and centralized punishment, information structures, network effects, endogenous/exogenous monitoring, and related institutional interventions (e.g., rating/veto/gossip mechanisms, reputation, ostracism, and minimum contribution rules).

A few papers provide only context, background, or adjacent theoretical insights and do not directly address punishment effects on efficiency in public-goods-like environments.

# 2) Task Relevance

## pgg_or_variant

- **exact:** The core of the literature directly examines PGGs or very close variants (e.g., lab PGGs with standard contribution and punishment rules, two-player repeated PDs with public good flavor, CPR games with return functions akin to PGGs). Many experiments and theory papers are anchored in canonical PGG designs.
- **close:** Some evidence comes from trust games, contests, and CPRs. These are structurally similar to PGGs, though not identical, and often model group/social dilemma aspects relevant for public-goods reasoning.
- **adjacent:** A minority of papers discuss sender-receiver games, pure contest games, or evolutionary mechanisms abstracted from direct PGG lab designs.

## punishment_or_sanctions

- **exact:** Many papers study explicit, costly punishment mechanics (peer or centralized sanctions, variable punishment costs, "punishment technology", or fines) matching the prediction task.
- **close:** Several studies investigate adjacent mechanisms—social ratings, reputation, gossip, ostracism, minimum contribution levels, or information-based interventions—which serve as indirect or social forms of punishment/sanctioning. Some theoretical works model "community enforcement" or contagious punishment without assigning material costs as in classic PGGs.
- **adjacent to weak:** A few papers consider only endogenous Nash reversion, signaling, or implicit incentives.

## efficiency_or_related_payoff_outcome

- **exact:** Many papers measure group payoff, efficiency (payoff relative to full cooperation), welfare, or surplus, either as the main outcome or in reported summary statistics.
- **close:** Some report public good provision levels, total earnings, or joint payoffs, which strongly track efficiency but may not be directly normalized to the all-cooperate benchmark.
- **adjacent or weak:** Several papers analyze only contributions, cooperation rates, or behavioral responses, with little or no direct measurement of group efficiency. In such cases, payoff-based inferences rely on theory or qualitative mapping from behavioral to payoff outcomes.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:**  
  - *Direct/primary:* Average group payoff, efficiency (payoff as a share of full cooperation), net/welfare/surplus.
  - *Close substitutes:* Total public good provision (if individually costly), joint earnings, total coins generated, average surplus relative to Nash.
- **Non-payoff behavioral outcomes:**  
  - Contribution rates, cooperation rates, punishment frequency, overbidding, use of ratings, social approval, information signaling, choices of exclusion/ostracism, norm compliance, and trust/trustworthiness.

Several experiments and theories closely distinguish payoff effects from pure behavioral responses. However, some studies emphasize behavioral data (e.g., contribution level or punishment frequency) with efficiency or group payoff as only a secondary or derived measure.

# 4) Main Findings Relevant To Prediction

## Consensus/Robust Findings

- **Punishment tends to increase efficiency:** In standard lab PGGs (4-player, 10–20 rounds, continuous contribution), enabling peer punishment robustly boosts efficiency (group payoff as a % of maximum), often dramatically and persistently (Kamei, 2019; Dutta et al., 2021; Lippert & Tremewan, 2021; Mitzkewitz & Neugebauer, 2020).
- **Effect magnitude is context-dependent:** The efficiency gain from punishment is strongly moderated by punishment cost and effectiveness (tech), monitoring structure (who sees what and who can punish whom), and group size/matching protocol.
- **Centralized vs. Peer Punishment:** Both can increase efficiency, but centralized mechanisms can be undermined by illegitimacy, unequal political power, or corruption (Chang et al., 2018; Abbink et al., 2020).
- **Too much punishment can reduce efficiency:** When monitoring and punishment are too "perfect" or dense, high punishment expenditures can consume group resources and lower net efficiency, even if appropriation rates are steady (Shreedhar et al., 2020).
- **Non-monetary and social/electronic sanctions:** Low- or zero-cost rating (social approval), gossip, and reputation/bystander exclusion can substitute for costly punishment, increasing efficiency if implementation is suitable and costless (Faillo et al., 2020; Fehr & Sutter, 2019; Fonseca & Peters, 2018); even imperfect reputation mechanisms help.

## Points of Disagreement/Ambiguity

- **Monitoring regime:** Endogenous (voluntary, group-chosen) monitoring can undermine the punishment institution and thus reduce efficiency compared to exogenous (imposed) monitoring (DeAngelo & Gee, 2020).
- **Communication & matching:** Pre-play chat and partner matching enhance the efficiency effect of punishment but can, in some contexts, substitute for formal punishment altogether (Kamei, 2019; Bigoni et al., 2019).
- **Long-run vs. short-run:** Some models/theories predict that efficiency gains from punishment only manifest after repeated rounds and learning (Dutta et al., 2021; Mitzkewitz & Neugebauer, 2020).
- **Fragility under noise/disagreement:** Ineffective or mis-targeted punishment, social disagreements, or monitoring errors can destabilize cooperation and reduce efficiency benefits (Barrett, 2020; Mihm & Toth, 2020).

# 5) Prediction Guidance

- **Direct prediction:** In canonical laboratory PGGs (e.g., 2–4 players, 10–20 rounds, continuous contribution, moderate MPCR, moderate punishment cost/effectiveness), enabling peer punishment is very likely to raise efficiency substantially compared to control (no punishment)—possibly approaching full cooperation under favorable conditions (Kamei, 2019; Dutta et al., 2021; Lippert & Tremewan, 2021).
- **Moderators:**  
  - *Punishment cost/tech:* Lower cost and higher effectiveness (punishment_tech) result in larger efficiency effects; if costs are too high, punishment is underused; if too low, excessive punishment expenditure can be wasteful.
  - *Monitoring structure:* Dense/perfect monitoring can increase punishment costs and lower net efficiency, even if cooperation is stabilized. Sparser networks or incomplete monitoring often lead to less waste and higher efficiency (Shreedhar et al., 2020).
  - *Information:* Visibility of others' actions/punishers ("show_other_summaries", "show_punishment_id") helps sustain cooperation and punishment's deterrent role (Mihm & Toth, 2020; Jindani, 2020).
  - *Player count & matching:* Smaller, fixed groups (partner matching) facilitate the emergence and sustainment of high-efficiency equilibria (Kamei, 2019).
  - *Chat/communication:* Enables norm agreement and mutual monitoring, sometimes making explicit costly punishment less necessary (Kamei, 2019; Bigoni et al., 2019).
- **Contextual caveats:**  
  - Centralized punishment is vulnerable to corruption/illegitimacy, possibly reducing efficiency gains (Abbink et al., 2020; Chang et al., 2018).
  - Endogenous institution formation (voluntary monitoring) can either support or undermine punishment's efficiency effect depending on collective buy-in (DeAngelo & Gee, 2020).
- **If the control (no-punishment) efficiency is high:** The absolute efficiency gain from enabling punishment may be smaller (ceiling effect), and the cost of unnecessary punishment (anti-social punishment) could slightly reduce net outcomes (Lippert & Tremewan, 2021).

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**
- `player_count`: Explicit group size effects in most experiments and models; two-player and four-player cases receive the most focus (Kamei, 2019; Dutta et al., 2021).
- `num_rounds`: Lab games typically report explicit effects for 10–20 rounds; repeated interaction critical for learning/persistence of efficiency gains (Dutta et al., 2021; Lippert & Tremewan, 2021).
- `mpcr`: Variations in marginal per-capita return are often controlled and analyzed.
- `punishment_cost`, `punishment_tech` (magnitude): Key moderators of punishment's effectiveness and efficiency impact (Dutta et al., 2021; Mitzkewitz & Neugebauer, 2020; Shreedhar et al., 2020).
- `chat`: Some direct evidence on the effect of communication in facilitating efficiency (Kamei, 2019; Bigoni et al., 2019).
- `all_or_nothing`: Occasionally manipulated (continuous vs. binary choice); evidence mostly from continuous settings.
- `show_n_rounds`: Recognized as important for end-game effects and learning (Lippert & Tremewan, 2021).
- `show_other_summaries`, `show_punishment_id`: Addressed in network and monitoring theory (Mihm & Toth, 2020; Jindani, 2020).

**Indirectly Informed:**
- `reward_exists`, `reward_cost`, `reward_tech`: Scarcely directly addressed; a few papers (Faillo et al., 2020; Mitzkewitz & Neugebauer, 2020) mention non-monetary rewards or the absence of reward in their designs.
- `default_contrib`: Framing (opt-in vs opt-out) sometimes contextually noted but not systematically manipulated across studies.

**Contextually Discussed or Effectively Missing:**
- `show_punishment_id`: Touched on via "identifiability" or "who can punish whom" in network/monitoring settings, but little directly empirical work on the salience of punishment identity.
- Details of "all_or_nothing" contributions, incentive salience, and fine-grained display settings are typically not systematically explored.
- Modern or field-relevant implementations of punishment and reward (e.g., mobile/online interfaces) are rarely addressed.

# 7) Important Limitations

- **Generalizability to field and scaled settings:** Most evidence comes from small groups (2–4 players), lab settings, and simple, stylized games; larger groups, field settings, or digital platforms may not reproduce these effects.
- **Limited coverage of several design dimensions:** Little empirical variation or systematic testing of `reward_exists`, `reward_cost`, `reward_tech`, `default_contrib`, or display features (`show_punishment_id`, detailed outcome summaries).
- **Ambiguity in non-standard environments:** CPR games, trust games, and contests, while instructive, are structurally different from standard PGGs and have their own dynamics; transfer to classic PGG may be incomplete.
- **Normative and contextual moderators not always explicit:** Factors such as social norms, group history, wealth distribution, and moral disagreement, which may moderate punishment effects, are not systematically explored.
- **Prominence of theory over empirical detail in some mechanisms:** Several highly optimistic theoretical models (e.g., community enforcement) depend on strong assumptions (perfect patience, random matching, impeccable monitoring) that may not always be reflected in real environments.
- **Predictions in designs with high control efficiency:** When the baseline (no-punishment) efficiency is already high, the marginal impact of punishment is less clear—some evidence suggests possible cost-overrun from unnecessary or anti-social punishment.
- **Endogeneity of institution and monitoring structure:** The fate of punishment institutions under voluntary, endogenous formation is tenuous and may not match imposed treatments, creating real-world uncertainty for predictions (DeAngelo & Gee, 2020).

---

**In sum**:  
This literature base offers strong, predominantly supportive, and relatively direct evidence that enabling peer punishment generally increases efficiency in lab-standard PGGs, often substantially, but the effect size and direction are sharply moderated by group size, cost/effectiveness of punishment, monitoring structure, communication, and baseline efficiency. There is especially strong evidence on `player_count`, `num_rounds`, `mpcr`, `punishment_cost`, and the importance of monitoring/visibility, but several other design features are sparsely covered. The prediction of treatment efficiency from design dimensions plus control efficiency can be reasonably well-informed for canonical lab PGGs, but inference is weaker for less-standard or real-world contexts.
