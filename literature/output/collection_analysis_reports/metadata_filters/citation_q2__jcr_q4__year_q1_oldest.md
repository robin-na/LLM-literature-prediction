# Evidence Base

The evidence base comprises six papers with a mix of theoretical and empirical (experimental) approaches, but is overall relatively narrow for the specific downstream prediction task. Only one paper (Carpenter & Matthews, 2010) presents a formal theory model that is an *exact fit* to public goods games (PGGs) with explicit consideration of peer and third-party punishment, and reports equilibrium predictions concerning efficiency. The remaining five papers are empirical, using laboratory experiments in adjacent or related game environments—primarily variants of bargaining, trust, or principal-agent games—rather than standard PGGs. Of these, only Abbink et al. (2004) provides direct empirical evidence for punishment’s effect on payoff-based efficiency, though in a bargaining rather than PGG setting. The other empirical studies focus on cooperation, trustworthiness, or honesty as behavioral outcomes, without reporting group efficiency or total payoffs.

# Task Relevance

### PGG or Variant
- **exact**: Only Carpenter & Matthews (2010) directly models a public goods game environment.
- **close**: Castro & Toro (2008) models an N-person repeated social dilemma (Prisoner’s Dilemma), which is structurally related but not a PGG. The other empirical papers (e.g., Abbink et al., Davis & Holt, Chen, Güth et al.) use modified ultimatum, trust, or budget-reporting games, making them **adjacent** to PGGs.

### Punishment or Sanctions
- **exact**: Carpenter & Matthews (2010), Abbink et al. (2004), and all empirical papers except Castro & Toro (2008) directly enable and measure the impact of peer or authority punishment mechanisms.
- **adjacent**: Castro & Toro (2008) discusses punishment hypothetically but does not model or test it.

### Efficiency or Related Payoff Outcome
- **exact**: Carpenter & Matthews (2010), Abbink et al. (2004), and Castro & Toro (2008) explicitly examine efficiency or closely related total payoff outcomes.
- **adjacent/weak**: Davis & Holt (1999), Chen (2012), and Güth et al. (2007) focus on behavioral outcomes (cooperation, slack, trust) and do not report group efficiency or comparable payoff measures; their relevance is thus limited for payoff-based prediction.

# Outcomes Measured In The Literature

- **Payoff-related outcomes** (critical for the prediction task):
    - *Efficiency, average/total group payoff, welfare*: 
      - Carpenter & Matthews (2010) (theory): reports equilibrium efficiency outcomes with and without punishment.
      - Abbink et al. (2004) (empirical): reports group efficiency/payoff with and without punishment in a bargaining setting.
      - Castro & Toro (2008) (theory): reports efficiency in repeated Prisoner’s Dilemmas with and without opt-out, not punishment.

- **Non-payoff behavioral outcomes** (important but insufficient alone for prediction task):
    - *Contribution rate, cooperation rate, punishment frequency, trustworthiness, honesty/slack*:
      - Davis & Holt (1999): cooperation rates with/without punishment.
      - Chen (2012): budgetary slack reduction in response to punishment/reward.
      - Güth et al. (2007): trustworthiness and frequency of punishment in repeated trust games.

# Main Findings Relevant To Prediction

## Synthesis across papers:

- **Evidence for increased efficiency with punishment (in PGGs):**
    - **Strongest in theory:** Carpenter & Matthews (2010) predicts (theoretically) that enabling punishment can sustain high cooperation and push group efficiency close to the social optimum—*if* a sufficient share of punishers exists and the group does not begin in a strongly free-riding/defecting state. Effect diminishes if free-riders dominate at baseline. Costs of punishment play only a minor role *at equilibrium* given low drift/mutation.
    - **Empirically ambiguous:** Abbink et al. (2004) finds that enabling punishment in lab bargaining games actually decreases efficiency, as punishment costs outweigh deterrence/discipline benefits unless punishment use is at the extremes (very low or very high). Thus, punishment is generally payoff-negative in this setting.

- **Evidence that non-PGG settings with punishment change behavior, but not always efficiency:**
    - Davis & Holt (1999), Chen (2012), Güth et al. (2007): Report that punishment/discipline can increase cooperation, trust, or honesty, but do *not* provide evidence on total payoffs or group efficiency. Thus, although punishment may alter behavior, its net effect on group efficiency is unspecified in these studies.

- **The marginal utility of punishment when other mechanisms exist:**
    - Castro & Toro (2008): In social dilemma games where opt-out (“loner”) is available, voluntary participation alone can produce high efficiency—suggesting punishment may be redundant or unnecessary for efficiency gains under such conditions.

- **Costliness and implementation details matter:**
    - Abbink et al. (2004) and Carpenter & Matthews (2010) both note that the *cost of punishment*, its effectiveness per unit, and its visibility are crucial: punishment that is too costly or is used at intermediate/partial rates can decrease efficiency.

- **Behavioral outcomes ≠ efficiency:**
    - Several papers demonstrate increases in prosocial or compliant behavior without corresponding evidence of increased efficiency.

# Prediction Guidance

- **For PGGs or near-variants with parameters similar to Carpenter & Matthews (2010)** (e.g., 4 players, binary contributions, MPCR ~0.75, moderate-to-high punishment effectiveness with manageable cost), enabling punishment is likely to increase efficiency, especially if baseline cooperation is not extremely low (i.e., control efficiency is moderate or high). However, if the initial state is heavily dominated by free-riders, punishment alone may not substantially raise efficiency.
- **For adjacent or structurally distinct environments** (two-player bargaining, trust, or principal-agent games), the introduction of punishment is at best ambiguous and often reduces efficiency due to direct payoff losses from costly punishment.
- **No evidence in this set supports universally positive effects of punishment on efficiency across all design dimensions.**
- **Prediction should be most confident for settings structurally matching the theoretical model in Carpenter & Matthews (2010).** For empirically studied bargaining/trust games, prediction should be more conservative, potentially expecting no efficiency gain or even efficiency loss when enabling punishment.
- **Control efficiency is a crucial moderator:** Punishment helps most when baseline rates are not too low.

# Design Dimensions Highlighted Across Papers

Directly informed:
- **player_count:** Explicitly modeled in theory (Carpenter & Matthews, 2010; Castro & Toro, 2008) and present in all empirical designs.
- **num_rounds:** Directly manipulated/reported in all theory and empirical papers.
- **all_or_nothing:** Binary contribution structure, especially in Carpenter & Matthews (2010) and some empirical games.
- **mpcr:** Marginal per-capita return specified in theoretical models.
- **punishment_cost, punishment_tech:** Varying punishment costs and effectiveness are a focus in both theory and experiments (esp. Carpenter & Matthews, Abbink et al.).
- **chat:** Directly implemented in some experimental games (effect on communication and potential coalition-building).
- **show_n_rounds:** Explicitly modeled or reported in several designs, though not always as a treatment variable.

Indirectly/contextually discussed:
- **default_contrib:** Not directly manipulated but implicitly present in contribution framing.
- **show_other_summaries:** Sometimes present in experimental feedback, but usually not a central variable.
- **show_punishment_id:** Visibility of punishment plays a crucial role in Abbink et al. (2004) but is not systematically varied elsewhere.

Effectively missing/unsupported:
- **reward_exists, reward_cost, reward_tech:** Only tangentially addressed (see Chen, 2012, on combined reward and punishment, but no efficiency data).
  
# Important Limitations

- **Sparse direct empirical evidence for PGG efficiency:** Only one paper provides theory-based equilibrium efficiency predictions in a standard PGG with punishment (Carpenter & Matthews, 2010), and only one (Abbink et al., 2004) reports empirical efficiency with punishment—though not in a PGG proper but in a bargaining game.
- **Strong reliance on theory for main PGG predictions:** Most empirical evidence comes from adjacent games with distinct incentive structures, limiting generalizability.
- **Behavioral evidence ≠ efficiency:** Most lab experiments measure behavioral responses (cooperation, trust, honesty), not direct efficiency or group payoff, constraining their predictive utility for the downstream efficiency-focused task.
- **Parameter dependence:** The effect of punishment is mediated by several design dimensions—group size, punishment cost/effectiveness, baseline cooperation, and contribution structure—limiting the ability to generalize from specific empirical or theoretical treatments.
- **Lack of systematic variation:** Many dimensions (e.g., default contribution, full reward systems) are untested or only contextually mentioned, reducing confidence in prediction under those conditions.
- **Potential for negative efficiency effects:** The literature highlights that, especially when punishment is costly or imperfectly targeted, introducing punishment may lower overall efficiency.

---

**Summary:**  
The evidence base gives the strongest, most granular support for efficiency increases from punishment in PGGs that match specific theoretical model conditions (small group, moderate MPCR, moderate punishment costs). Outside these scenarios, the literature is either ambiguous or suggests possible efficiency losses when punishment merely shifts payoffs through cost rather than raising total surplus. Most experimental studies report behavioral outcomes, not group efficiency. Careful attention to which prediction dimensions are tested—and how closely the relevant papers match the downstream environment—is critical for informed forecast modeling.
