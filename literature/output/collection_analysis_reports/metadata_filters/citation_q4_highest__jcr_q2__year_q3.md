# 1) Evidence Base

The paper set consists of seven papers, including both empirical (2 laboratory experimental studies, 1 review of experiments) and theory/simulation work (4 papers). The empirical studies are tightly focused on public goods games (PGGs) with variable punishment institutions and measure relevant payoff and efficiency outcomes. The theory papers expand the context to networked or spatial environments, feedback-evolving public goods dilemmas, and alternative mechanisms to punishment, though only some directly address payoffs or efficiency. Overall, the paper set is moderately broad with strong representation of laboratory PGGs with punishment and associated efficiency outcomes, supplemented by theoretical models offering adjacent perspectives.

# 2) Task Relevance

**pgg_or_variant:**  
- **exact relevance:** Four papers (Arechar et al., 2018; Dannenberg & Gallier, 2020; Wang et al., 2021; Capraro & Perc, 2018; Dong et al., 2019) focus exactly on PGGs; the others use adjacent social dilemma/game environments (e.g., common-pool resource games).
- **close/adjacent relevance:** Two theory papers (Yan et al., 2021; Szolnoki & Chen, 2018) model games with qualitatively similar but not strictly standard PGG designs (e.g., introducing resource feedbacks or alternative mechanisms).
- **overall:** Strong coverage for standard and networked/variant PGGs.

**punishment_or_sanctions:**  
- **exact relevance:** Arechar et al. (2018), Dannenberg & Gallier (2020), Wang et al. (2021), Yan et al. (2021) center on explicit punishment institutions or mechanisms.
- **close/adjacent relevance:** Capraro & Perc (2018) and Dong et al. (2019) discuss alternative incentive types (reputation, reward) and contextualize punishment, but without direct experimental measurement or implementation.
- **none:** Szolnoki & Chen (2018) do not include any punishment.
- **overall:** Good direct evidence, though some papers address punishment indirectly or not at all.

**efficiency_or_related_payoff_outcome:**  
- **exact relevance:** Arechar et al. (2018), Dannenberg & Gallier (2020), Yan et al. (2021), and Szolnoki & Chen (2018) explicitly model or measure efficiency/payoff.
- **close/adjacent:** Wang et al. (2021), Capraro & Perc (2018), and Dong et al. (2019) primarily report on costs needed for cooperation, reputation, or behavioral changes, but discuss efficiency or surplus contextually.
- **overall:** Strong direct measurement of efficiency in the more empirical papers; theoretical/simulation models link behavioral outcomes to efficiency less explicitly.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (direct):**  
    - *Group efficiency:* Measured directly as average earnings as a share of maximal possible (Arechar et al., 2018; Dannenberg & Gallier, 2020; Yan et al., 2021; Szolnoki & Chen, 2018).
    - *Group payoff, surplus, welfare:* Routine reporting in empirical work; explicit central outcome in Dannenberg & Gallier (2020), and modeled via stationary states in theory papers.
    - *Total costs of incentives/rewards:* Wang et al. (2021) model the net cost to reach/maintain cooperation, adjacent to efficiency if costs are subtracted from payoff.
    - *Resource sustainability:* (Yan et al., 2021) connects institutional punishment to sustainable equilibrium resource levels and thus efficiency.

- **Non-payoff behavioral outcomes (secondary/contextual):**  
    - *Contribution/cooperation rates:* Arechar et al. (2018), Dannenberg & Gallier (2020), Wang et al. (2021), Dong et al. (2019).
    - *Punishment frequency/norm compliance:* Arechar et al. (2018), Dannenberg & Gallier (2020).
    - *Reputation dynamics and conformity:* Dong et al. (2019), Capraro & Perc (2018), Szolnoki & Chen (2018).
    - These are distinguished from efficiency outcomes in most papers.

# 4) Main Findings Relevant To Prediction

- **Enabling peer punishment in repeated standard PGGs:**  
  Increases average contributions and group efficiency substantially. Laboratory and online data agree on a robust positive effect of enabling punishment, raising mean participant payoffs from below to above 80% of the maximal level (Arechar et al., 2018).

- **Punishment effectiveness depends on design:**  
  Effectiveness (in efficiency gains) is maximized when punishment is not too costly, effectively deters free-riding, and is consistently adopted. Very costly or weak punishment yields little or no efficiency gain; incomplete adoption (endogenous/voluntary institutions) dilutes the effect (Dannenberg & Gallier, 2020).

- **Theoretical models echo empirical patterns:**  
  Analytical and simulation studies corroborate that institutional punishment increases efficiency only above certain strength/cost thresholds; otherwise, cooperation and thus efficiency remain low (Yan et al., 2021).
  
- **Initial group state matters for intervention effect:**  
  Reward mechanisms may be more cost-effective than punishment when initial cooperation is low; punishment becomes efficient at higher cooperation rates. Thus, the marginal efficiency impact of enabling punishment partly reflects group composition and history (Wang et al., 2021). (NB: outcome is not always measured in terms of group efficiency, rather as cumulative cost for a behavioral threshold.)

- **Alternative mechanisms (reputation, conformity):**  
  Some models show that institutional or social mechanisms other than punishment (such as reputation or conformity-based imitation) can expand regions of high efficiency (Szolnoki & Chen, 2018; Dong et al., 2019), but these do not speak directly to the effect of punishment per se. They signal that observed efficiency after enabling punishment may also depend on what other mechanisms or channels are present.

- **Behavioral versus payoff outcomes:**  
  In most cases, increases in contribution or cooperation rates translate to higher measured efficiency; however, some literature (notably the theoretical/simulation work) reports on behavioral endpoints only, making payoff implications indirect.

# 5) Prediction Guidance

- **Direct inference:**  
  In repeated PGGs with standard peer punishment (moderate cost, effective impact), enabling punishment is predicted to significantly increase group efficiency relative to the same game without punishment, often restoring efficiency close to (or even above) 80–90% of the social optimum (Arechar et al., 2018; Dannenberg & Gallier, 2020).

- **Dimension sensitivity:**  
  The magnitude of this effect is moderated by parameters such as punishment cost, punishment effectiveness (magnitude and certainty), and the competing institutional or group choice dynamics (Dannenberg & Gallier, 2020; Yan et al., 2021). Prediction from control efficiency should be adjusted downwards if (a) punishment cost is high, (b) punishment efficacy is low, or (c) adoption is partial/voluntary and not universal.

- **Boundary/moderation effects:**  
  In networked or resource-feedback games, high efficiency is achieved only if the punishment mechanism is above a critical effectiveness threshold. Below this threshold, introducing punishment may not increase efficiency at all, and oscillatory or unstable group outcomes may occur (Yan et al., 2021).

- **Contextual/indirect evidence:**  
  Theory suggests that the initial group composition and competing mechanisms (rewards, reputation, learning protocols) can shape whether and how much enabling punishment increases efficiency (Wang et al., 2021; Szolnoki & Chen, 2018). When using only payoff outcomes for prediction, behavioral outcomes should not be substituted except where clear mapping has been demonstrated.

# 6) Design Dimensions Highlighted Across Papers

- **Directly informed (empirical or theory, with explicit manipulation):**  
  - `player_count` (multiple): direct effects measured in varying group sizes (Arechar et al., 2018; Wang et al., 2021; Yan et al., 2021).
  - `num_rounds`: manipulated or modeled in repeated settings.
  - `punishment_cost`, `punishment_tech` (type/mode): separately identified as key moderators of effectiveness/efficiency (Arechar et al., 2018; Dannenberg & Gallier, 2020; Yan et al., 2021).
  - `mpcr` (synergy factor): analyzed in both experiments and theory papers for its role in baseline efficiency and punishment effect.
  - `all_or_nothing`: included as a variant in several models (Wang et al., 2021; Dong et al., 2019; Yan et al., 2021).

- **Indirectly informed/contextually discussed:**  
  - `chat`: used as a feature in one empirical study (Arechar et al., 2018)—impact on efficiency with punishment not isolated.
  - `default_contrib`: framed but not experimentally varied.
  - `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: mostly not isolated.
  - `reward_exists`, `reward_cost`, `reward_tech`: discussed in the context of alternative or combined mechanisms but not central to efficiency outcome prediction given punishment-only treatments.

- **Effectively missing:**  
  Many visualization and interface dimensions (e.g., `show_punishment_id`, `show_other_summaries`) and nuanced behavioral framing features are not systematically studied or reported for their impact on efficiency with punishment in this paper set.

# 7) Important Limitations

- **Scope of mechanism coverage:**  
  Most direct empirical evidence focuses on standard peer punishment or institutional punishment. Richer variants (e.g., endogenous/adopted versus imposed institutions, mixed punishment/reward schemes) are less systematically explored for their unique effect on efficiency.

- **Generalizability beyond lab or model environment:**  
  Experimental results are drawn from standard laboratory or online task settings, generally with fixed and clear rules; actual organizational or field context with ambiguous or changing rules may display different efficiency dynamics after enabling punishment.

- **Dimension-level sparsity:**  
  Not all 14 design dimensions receive direct or systematic attention: especially interface/display features (`show_n_rounds`, `show_punishment_id`, etc.) and reward-related dimensions are underexplored in relation to efficiency with punishment.

- **Behavioral versus payoff outcome confusion:**  
  Several theory papers focus mainly on cooperation frequency, contribution rate, or network reputation rather than direct efficiency or payoff outcomes. This raises the risk of over-interpreting behavioral results as equivalent to efficiency gains without supporting evidence.

- **Parameter interaction effects:**  
  Most studies manipulate one or two dimensions at a time; cross-dimensional moderation (e.g., how `player_count` interacts with `punishment_cost` to affect efficiency lift from punishment) is less exhaustively investigated.

- **Unknowns for minimal/weak punishment:**  
  While the efficiency benefits of strong punishment are clear, predictions for minimal, weak, or costly punishment arrangements are less reliably supported and may be sensitive to small changes in cost/benefit structure (Yan et al., 2021).

- **Network and feedback model external validity:**  
  Simulation results from spatial/networked feedback models (Yan et al., 2021; Szolnoki & Chen, 2018) may differ from lab PGG results due to different updating protocols, feedback delays, or resource dynamics.

---

**Summary**: The literature provides direct and robust laboratory evidence that enabling standard, effective peer punishment boosts group efficiency in repeated public goods games, and this effect is moderated by key design features—especially punishment cost and effectiveness. Theoretical models reinforce that efficiency gains depend on critical parameter thresholds and initial group states. Reward, reputation, and alternative mechanisms are contextually important, but their effects are not directly additive or interchangeable with those of punishment for the prediction target. Several prediction dimensions (notably direct incentives and game structure) are well covered; others are sparsely addressed. Care is needed to distinguish findings on behavioral outcomes from true efficiency improvements for prediction purposes.
