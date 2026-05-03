# 1) Evidence Base

The paper set includes a mix of empirical (especially lab experiments) and theoretical studies, spanning direct public goods games (PGG), closely related social dilemmas, and broader conceptual or modeling work. Empirical papers most often use standard or slightly varied laboratory PGGs or adjacent games (repeated PDGs, contest games, dictator games with sanction options). Multiple papers report on punishment and/or reward mechanisms, but only a minority measure efficiency or group payoff directly. Theoretical work covers mechanisms such as commitment, norm evolution, group selection, and strategic tie formation, frequently applied to PGGs but with variable attention to payoff outcomes or explicit punishment treatments.

This literature is relatively broad in exploring social dilemmas, norm compliance, and sanctioning but is narrower regarding the precise prediction task: estimating changes in **efficiency** (as group payoff relative to maximum) when **peer punishment** is enabled in experimentally parameterized PGGs. Only a handful of studies report both pre- and post-punishment efficiency measures in PGGs; others focus on behavioral, neural, or motivational aspects, or on analogues to PGGs.

# 2) Task Relevance

### Public Goods Games or Variant (`pgg_or_variant`)
- **Exact relevance**: Several empirical studies use standard PGGs or explicitly labeled variants—especially those by Pfattheicher et al. (2018), Hou et al. (2019), Molenmaker et al. (2019), and Fraser & Nettle (2020)—and theoretical models often reference or structure their arguments around PGGs (Akdeniz & van Veelen, 2021; Gavrilets, 2021).
- **Close/adjacent relevance**: Numerous papers use adjacent paradigms (repeated PDGs, team production games, contest games, dictator/ultimatum/referee games), framing their findings as generalizable to public goods or cooperation problems.
- **Weak/none**: Few papers model general networks, sender-receiver games, or unrelated social dilemmas without any explicit PGG or collective-action structure.

### Punishment or Sanctions (`punishment_or_sanctions`)
- **Exact relevance**: Many empirical PGG studies manipulate the presence of peer or third-party punishment (Pfattheicher et al., 2018; Hou et al., 2019; Molenmaker et al., 2019). Several theory papers model peer/institutional punishment or sanction as a focal mechanism.
- **Close/adjacent**: Adjacent studies analyze punishment in PDGs, dictator games, contest environments, or the effect of punishment framing.
- **None**: A subset of the literature ignores punishment entirely.

### Efficiency or Related Payoff Outcome (`efficiency_or_related_payoff_outcome`)
- **Exact/close relevance**: Only a few empirical PGG studies report **efficiency** or total group payoff (Pfattheicher et al., 2018; Hou et al., 2019; Szekely et al., 2020 for adjacent designs). Some theory papers explicitly model efficiency or equilibrium welfare.
- **Adjacent/weak**: Most remaining papers emphasize non-payoff behavioral outcomes (contribution rate, punishment frequency) or theoretical plausibility arguments rather than direct group earnings or efficiency.
- **None**: Some works discuss only neural, motivational, or conceptual issues without performance outcomes.

# 3) Outcomes Measured In The Literature

## Payoff-Related Outcomes
- **Direct measurement/reporting:** Efficiency (total group payoff as a fraction of the cooperative maximum) is directly reported in a minority of PGG-with-punishment experiments (notably Pfattheicher et al., 2018; Hou et al., 2019).
- **Closely related outcomes:** Some papers report total group earnings, welfare, or surplus in adjacent social dilemma settings (Szekely et al., 2020; Nikias & Sy, 2021; Raub et al., 2019).
- **Indirect inference:** A number of studies measure behavioral outcomes (contributions, cooperation rate) that are strongly positively correlated with group earnings but are not payoff measures themselves.

## Non-Payoff Behavioral Outcomes
- **Cooperation/contribution rate:** The most common outcome, especially in experimental designs. Used as a proxy for efficiency but not equivalent.
- **Punishment frequency or magnitude:** Often measured (e.g., Molenmaker et al., 2019), but only relevant to prediction if linked to payoffs.
- **Norm compliance/violation:** Salient in theory and behavioral studies as an indicator of social order.
- **Psychological outcomes:** Measures like satisfaction, fairness perception, trust, and neural/neuropsychological states are less relevant to payoff but sometimes reported.

## Notably Absent
- Many papers do not report efficiency, earnings, or total payoff, making translation to the prediction task nontrivial.

# 4) Main Findings Relevant To Prediction

Synthesized from the evidence base:

- **Peer punishment can increase cooperation, but often at a cost.**
  - Standard peer punishment reliably increases contributions in PGGs but also incurs high punishment expenditures—frequently resulting in lower efficiency than the no-punishment baseline, at least in short or moderate length games (Pfattheicher et al., 2018).
  - Third-party punishment (by outside agents) can similarly boost contributions and sometimes group earnings (Hou et al., 2019).

- **Form and design of punishment mechanism matter.**
  - Democratic peer punishment (where punishment is enacted only if agreed by a majority) reduces antisocial/counterproductive punishment, improving efficiency and sometimes surpassing the no-punishment baseline over repeated rounds (Pfattheicher et al., 2018).
  - Lowering the cost of punishment (punishment_cost) increases both cooperation and efficiency, holding other features constant (Nikias & Sy, 2021).
  - The **timing** of punishment opportunity (ex ante/ex post) substantially affects willingness to punish, which can indirectly affect efficiency, but direct linkages to payoff are rarely measured (Molenmaker et al., 2019).

- **Some contexts lead to punishment decreasing efficiency.**
  - Where punishment is costly or antisocial retaliation is common (particularly in settings with disagreement or opportunity for counter-punishment), efficiency may fall below control (Szekely et al., 2020; Barrett, 2020; Raihani & Power, 2021).

- **Moderators identified:**
  - **Number of rounds**: Longer games allow efficiency under peer punishment to "catch up" as antisocial punishment subsides and cooperation becomes self-reinforcing (Pfattheicher et al., 2018).
  - **Size of group**: Some theory suggests punishment is less effective (or more susceptible to breakdown) in large groups without institutional mechanisms (Toelstede, 2020; Smith, 2020).
  - **Information/transparency**: Availability of information about other's actions and history can affect the effectiveness of punishment and the persistence of prosocial/antisocial punishment (Barrett, 2020; Lois & Wessa, 2019).
  - **Framing and motivation crowding**: If punishment is perceived as distrustful or crowding out intrinsic norms, efficiency gains may be muted (Klempt & Pull, 2018; Gold, 2020).

- **Reward co-exists with punishment:**
  - Reward mechanisms, if enabled alongside punishment, sometimes further increase earnings and cooperation, but reward alone is less effective than punishment (Hou et al., 2019).

- **Theoretical models:**
  - Many theory papers propose that availability of credible, targeted punishment can support higher equilibrium efficiency, provided institutional and motivational alignments exist (Forges & Horst, 2018; Raub et al., 2019; Akdeniz & van Veelen, 2021).

# 5) Prediction Guidance

### For predicting efficiency in PGGs from design features—when transitioning from a no-punishment control to punishment-enabled treatment—the literature suggests:

- **Anticipate increased cooperation (behavioral), but ambiguous or negative short-run efficiency.** In baseline lab PGGs, peer punishment increases contributions but often at a net efficiency cost due to high use of costly punishment—unless the mechanism is thoughtfully designed (Pfattheicher et al., 2018).

- **Punishment cost is a crucial moderator.** Lower punishment cost (punishment_cost dimension) generally yields higher efficiency when punishment is enabled, assuming use rates increase but do not provoke escalating counter-punishment (Nikias & Sy, 2021; Barrett, 2020).

- **Structure of the punishment mechanism matters.** Democratic or collectively agreed punishment mechanisms may reduce antisocial punishment and lead to efficiency gains, especially in longer horizons (player_count, num_rounds, punishment_tech: Pfattheicher et al., 2018).

- **Presence of reward mechanisms can strengthen positive effects** but may need to be combined with punishment to matter (Hou et al., 2019).

- **Information features (show_other_summaries, show_punishment_id) can moderate impact** by shaping norm salience, social learning, and perceived fairness (Lois & Wessa, 2019; Barrett, 2020).

- **Effect may differ by round length and group size.** Gains from punishment (in efficiency, not just cooperation) accumulate or only materialize in longer games; effects may be less robust in large groups or with one-shot/short games.

- **Behavioral (non-payoff) findings should be treated with caution for efficiency prediction.** Many studies only track cooperation rates, which do not always translate to higher group payoffs due to the direct cost of punishment.

- **If control (no-punishment) efficiency is already high, enabling punishment may yield negligible or even negative efficiency changes**—particularly when extra cooperation cannot offset punishment costs.

- **Antisocial punishment and norm conflict reduce or reverse gains** (Raihani & Power, 2021); expect especially ambiguous efficiency effects under disagreement or in cultures with high antisocial punishment.

# 6) Design Dimensions Highlighted Across Papers

## Directly informed (experimental evidence in PGG or close analogs, with at least adjacent payoff outcomes)
- **player_count**: Many studies use 2-4 players; some theory addresses size effects; transferability to large N is less substantiated.
- **num_rounds**: Heavily represented; longer games see efficiency gains materialize (Pfattheicher et al., 2018).
- **mpcr**: Common treatment variable; effect on baseline efficiency and incentive to cooperate well studied.
- **punishment_cost**: Directly manipulated and shown to moderate both use of punishment and efficiency (Nikias & Sy, 2021).
- **punishment_tech** (cost-to-impact ratio): Primarily in lab studies (Pfattheicher et al., 2018; Hou et al., 2019).
- **all_or_nothing**: Some studies use continuous, some binary contributions; most findings suggest similar directional effects.
- **chat**: Direct evidence that lack of communication holds in many lab settings; effect of enabling chat is less central.

## Indirectly informed (mostly behavioral outcomes or conceptual discussion)
- **reward_exists**, **reward_cost**, **reward_tech**: Evidence primarily from Hou et al. (2019): reward alone does little, but combined with punishment can increase efficiency.
- **default_contrib**: Framing effects on default contribution are rarely singled out; relevant mostly in theoretical framing papers.
- **show_n_rounds**, **show_other_summaries**: Information treatments and feedback are common, with behavioral effects, but rarely linked systematically to efficiency outcomes.
- **show_punishment_id**: Identity visibility is discussed as a possible moderator of punishment dynamics, especially regarding antisocial punishment, but the payoff connection is typically speculative.

## Only contextually discussed or effectively missing
- **Most studies do not systematically vary or report the effect of** `default_contrib`, `chat`, `show_punishment_id`, or the full range of information/feedback dimensions for payoff outcomes.
- **Reward dimensions** are generally addressed only alongside or subordinate to punishment (one or two papers).
- **Design features like institution formation, commitment devices, or complex endogenous structures** are noted in theory/results but not parameterized prediction-relevant evidence.

# 7) Important Limitations

- **Sparse direct efficiency measurement:** Only a few studies report the key outcome—change in group efficiency due to enabling punishment, holding other factors constant. Most others focus on behavioral proxies (contributions, punishment rates), which do not straightforwardly translate to payoffs due to the costs of punishment and possible crowding out.
- **Limited variation in design dimensions:** Most experiments use standard or limited parameter sets (e.g., 4-player, 6-10 round, continuous PGGs with fixed punishment impact/cost) and laboratory settings. Extrapolation to other scaling, complex institutional features, or field settings remains speculative.
- **Overrepresentation of specific outcome windows:** Efficiency effects of punishment are often examined in short or moderate-length experiments; findings suggest that positive effects may emerge only in longer runs, so the literature may underestimate positive long-run efficiency from punishment.
- **Behavioral vs. payoff distinction:** Frequent confusion or conflation between behavioral change (higher cooperation) and efficiency improvement; some papers highlight that these do not always align when punishment is costly.
- **Weak attention to social, cultural, and psychological context:** While some papers theorize about effects of trust, disagreement, or crowding out, direct empirical payoff evidence under those moderators is limited.
- **Indirect treatment of several design dimensions:** Many of the 14 predictor dimensions are not systematically manipulated or reported for their separate effects on efficiency, limiting the ability to finely calibrate predictions.
- **Heterogeneity in game structure and external validity:** The inclusion of adjacent designs (team games, PDGs, contest games) introduces conceptual breadth but may reduce confidence in the direct transferability of quantitative findings to benchmark PGGs.

---

**In summary:**  
The strongest actionable evidence for prediction comes from PGG experiments directly measuring group efficiency before and after enabling punishment or reward, and from theory modeling equilibrium efficiency as a function of punishment cost and design. The evidence base underscores that peer punishment tends to increase cooperation, but efficiency gains depend critically on punishment costs, game duration, and mechanism design. Prediction of efficiency changes should use direct efficiency findings where available, be cautious in extrapolating from increased cooperation alone, pay special attention to punishment cost and design features, and adjust for limitations in context, duration, and coverage of design dimension space in the literature.
