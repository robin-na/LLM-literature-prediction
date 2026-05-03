# 1) Evidence Base

The provided literature set is extensive, comprising 130 papers spanning empirical laboratory experiments (primarily), field experiments, theoretical/simulation models, qualitative reviews, and some ethnographic/contextual accounts. There is a strong empirical core focused on public goods games (PGGs) and close variants, many of which specifically target the effects of punishment or sanctioning on cooperation and various outcomes. The majority of PGG-focused studies are laboratory-based and involve monetary or point-based incentives, allowing for measurement of efficiency or closely related payoff variables. There is also representation of non-payoff behavioral outcomes (e.g., contribution rates, punishment behavior), as well as a substantial number of theory/simulation papers that address underlying mechanisms.

The evidence base is relatively **broad, robust, and interdisciplinary** for the core task of predicting how peer punishment affects group efficiency in PGG-like experimental contexts, though much of the literature focuses on behavioral (not payoff) outcomes, and only a subset directly reports efficiency-related measures in both control (no-punishment) and punishment-enabled conditions.

# 2) Task Relevance

**a. pgg_or_variant:**  
- **Exact relevance**: A substantial core of the papers (e.g., Gächter et al., 2017; Gintis et al., 2003; Fehr & Gintis, 2007; Barclay, 2004) address the standard PGG or very close variants (linear/quadratic, maintenance/provision, small to moderate group sizes, repeated rounds).
- **Close/adjacent relevance**: Some studies use adjacent paradigms (CPRs, PDs, dictator/ultimatum/trust games, or market games), many of which preserve the collective action structure but differ in contribution rules or game structure.  
- **Weak/none**: There are some included papers on pure dictator games, one-shot games, or real-world sharing behaviors, but these are less central.

**b. punishment_or_sanctions:**  
- **Exact relevance**: Many papers directly manipulate the presence/absence of peer punishment, with standard lab implementations (e.g., cost 1, inflict 3 units).
- **Close/adjacent**: A significant subset study ostracism/exclusion, reward/compensation, centralized punishment, or symbolic sanctions (gossip, ostracism, feedback systems), which are functionally adjacent but not always structurally identical to peer monetary punishment.
- **Weak/none**: Some reference punishment only as context, or study reputation/reward in the absence of direct sanctions.

**c. efficiency_or_related_payoff_outcome:**  
- **Exact relevance**: Notable primary sources (e.g., Gächter et al., 2017; Gintis et al., 2003; Barclay, 2004; Masclet, 2003; Feinberg et al., 2014; Hamman et al., 2011) report group efficiency or total/group payoffs under both control and punishment.
- **Close**: Several provide welfare, earnings, surplus, or coins generated as a direct outcome.
- **Adjacent/weak**: Many report only behavioral outcomes (contribution, cooperation, punishment frequency) and infer efficiency effects indirectly, or report only individual-level outcomes.

**Summary:**  
The **highest task relevance** is found in papers that (a) use a classic PGG or direct linear variant, (b) experimentally manipulate a peer punishment mechanism (not just central/delegated/ostracism), and (c) report group efficiency, net payoff, or welfare before and after punishment is enabled. This subset offers **exact mapping** to the downstream prediction task.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes**:
- **Efficiency** (group payoff/max possible), total group payoff, welfare, surplus, net group earnings (Gächter et al., 2017; Gintis et al., 2003; Masclet, 2003; Barclay, 2004; Hamman et al., 2011).
- **Individual payoffs** and earnings are sometimes used, but the prediction task targets group-level metrics.
- **Adjunct measures** like coins generated, proportion of rounds at threshold, and surplus are used in some studies.

**Non-payoff behavioral outcomes**:
- **Contribution rate/cooperation**: Dominant in the literature (e.g., Balliet et al., 2013; Hilbig et al., 2012; Kiyonari & Barclay, 2008; Balliet, Mulder, & Van Lange, 2011).
- **Punishment frequency/magnitude**, antisocial punishment occurrences, and norm compliance.
- **Attitudes, trust, norms, reputational consequences**.

**Distinction**: There are many studies where increased cooperation with punishment is shown, but group efficiency may decrease, especially if punishment is costly or misapplied. **Only a subset quantifies whether the sum total of group earnings increases after accounting for costs of punishment**.

# 4) Main Findings Relevant To Prediction

**Synthesis of Cross-paper Findings on Treatment Efficiency**:

- **Enabling peer punishment generally increases group efficiency in standard lab PGGs** (Gächter et al., 2017; Gintis et al., 2003; Fehr & Gintis, 2007; Masclet, 2003; Barclay, 2004), with the strongest effects in small groups (3-5 players), moderate MPCR (~0.3–0.5), ~10–30 rounds, and when punishment is sufficiently effective (cost/impact ratio 1:3). Gains can be dramatic, routinely restoring group efficiency to near the social optimum in both 'maintenance' and 'provision' frames.

- **Robustness**: The positive effect holds across a range of group identities, incentive levels, and both maintenance/provision framing (Gächter et al., 2017).

- **Moderators and caveats**:
  - **Punishment cost/technology**: If punishment is costly or weak (e.g., cost/impact ratio approaches 1:1, or punishment is uncoordinated/low-probability), group efficiency gains may be neutral or even negative, as resources absorbed by punishment can offset gains from higher cooperation (Guala, 2012; Kurzban et al., 2015; Tenbrunsel & Messick, 1999; Fehr & Schurtenberger, 2018; Gintis et al., 2003). In very long repeated games, efficiency gains are more likely as punishment use tapers off.  
  - **Antisocial punishment** (punishing cooperators) can undermine—and in some contexts, reverse—the efficiency benefits, especially under competitive or low-information conditions (Pleasant & Barclay, 2018; Goette et al., 2012).
  - **Group composition and culture**: Cultural background and ingroup/outgroup status can moderate both willingness to punish and the efficiency effect (Barclay, 2004; Grossman & Baldassarri, 2012; Hilbig et al., 2012).
  - **Communication**: Allowing for communication (chat) enhances or even substitutes for punishment; in fact, the largest efficiency increases are seen when communication and punishment are combined (Ostrom et al., 1992; Mak et al., 2015; Hamman et al., 2011).
  - **Nature of the sanction**: Non-monetary sanctions (ostracism, exclusion, gossip) can sometimes substitute for, or be more efficient than, monetary punishment, especially as they can sustain cooperation at low cost if credible (Feinberg et al., 2014; Masclet, 2003; Kerr et al., 2009).
  - **Centralized vs. peer punishment**: Centralized punishment (by elected or appointed leaders) can yield efficiency gains that are similar or even superior to peer punishment, particularly when legitimacy is high and opportunities for anti-social uses are minimized (Grossman & Baldassarri, 2012; Hamman et al., 2011; Parks et al., 2013).

- **Context-dependence**:
  - In **field experiments and real-world analogues**, punishment is rarely as costly, uncoordinated, or frequent as in lab PGGs; low- or no-cost sanctions (gossip, coordination, institutional punishment) are more prevalent and effective (Guala, 2012; Ostrom et al., 1992; Fehr & Schurtenberger, 2018).
  - The **effect of punishment may be negligible or negative** in short or one-shot games, high-cost/weak punishment, cultures with strong antisocial punishment, or when corruption/bribery is possible (Muthukrishna et al., 2017; Kurzban et al., 2015).

- **Control (no-punishment) efficiency as predictor**: The initial cooperation/efficiency baseline *moderates* the potential gain from punishment—**punishment yields the largest efficiency gains in environments where control efficiency is low due to free-riding**. If baseline cooperation is already high (e.g., due to strong norms or communication), incremental gains from punishment are modest (Fehr & Gintis, 2007; Lubell & Scholz, 2001; Hamman et al., 2011). In environments where control efficiency is high, punishment costs may even reduce net efficiency.

**General Pattern**:  
- **Punishment increases efficiency in standard lab PGGs** (especially with moderate/low baseline efficiency, moderate-to-high MPCR, repeated interaction, effective punishment, no corruption or antisocial punishment, and low-to-moderate group size).
- **Contextual and design factors moderate the effect**; poor implementation, antisocial application, or high cost of punishment can eliminate or reverse efficiency gains.

# 5) Prediction Guidance

The literature supports the following **principles and cautions for predicting treatment efficiency** (efficiency with peer punishment enabled):

- **In standard lab PGGs**, with typical parameters (4 players, 10–27 rounds, MPCR 0.4–0.5, no chat, continuous contribution, anonymous/no reputation, punishment cost/impact 1:3), **enabling peer punishment is expected to increase group efficiency, often to near-optimal or social optimum levels**, *provided that* the baseline (no-punishment) efficiency is moderate or low (Gächter et al., 2017; Gintis et al., 2003; Masclet, 2003).
- **Control efficiency (no-punishment group efficiency)** is a strong lower-bound predictor: if efficiency is low in control, expect a large increase with well-designed punishment; if control efficiency is high, the marginal benefit may be minimal or negative.
- **Key conditions for positive treatment effect**:
    - *Effective, not overly costly punishment* (cost/impact at least 1:3 or more favorable)
    - *Moderate-to-high number of rounds* (enables punishment to shape behavior and then recede)
    - *No corruption, excessive antisocial punishment, or collusion among punishers*
    - *No ready substitutes for sustaining high cooperation (e.g., chat/communication, reputation, strong intrinsic norms)*
- **Negative or ambiguous effects**:
    - If punishment is highly costly, weak (e.g., cost approximates impact), or easily misapplied, **efficiency gains may be negligible or negative** due to resource destruction (Guala, 2012; Kurzban et al., 2015).
    - **Antisocial punishment** or the possibility of counter-punishment can undermine efficiency benefits, especially in uncoordinated, competitive, or poorly monitored settings.
    - **Very short games, single-shot interactions, or high-trust environments** (where cooperation is already high) may yield little or no efficiency gain from punishment (Balliet et al., 2011; Ostrom et al., 1992).

- **Design dimension moderators**:
    - **Player count**: Effect persists up to moderate group size, but exclusion/ostracism is less effective in large groups (>8, Kerr et al., 2009; Parks et al., 2013).
    - **Number of rounds**: Longer games favor efficiency gains, as initial costs of punishment are amortized and cooperation stabilizes (Fehr & Gintis, 2007; Balliet et al., 2011).
    - **MPCR**: Low MPCRs make cooperation harder to sustain; punishment effectiveness must be greater.
    - **Punishment cost/tech**: Critical; low cost/high impact mechanisms are most effective.
    - **Communication (chat)**: When present, may substitute for or enhance punishment; when absent, punishment effects are more distinct (Mak et al., 2015; Ostrom et al., 1992).
    - **Corruption/bribery mechanisms**: Can reverse punishment's effect (Muthukrishna et al., 2017).
    - **Social context (identifiability, culture)**: Can moderate both cooperation and punishment application.
    - **Reward options**: Frequently, reward is as or more efficient as punishment (Balliet et al., 2011; Rand & Nowak, 2013).
    - **Observability/reputation systems**: Can substitute for punishment in sustaining cooperation (Feinberg et al., 2014; Diekmann et al., 2014).

**Summary for prediction**:
- **When game dimension values match populations in the core empirical literature, and control efficiency is known, treatment efficiency with punishment enabled can be predicted to be substantially higher, unless strong negative moderators (e.g., high cost, uncoordinated/antisocial punishment, high baseline efficiency) are present.**
- **Caution**: If evidence is limited to behavioral outcomes (contribution), efficiency improvement is only inferred, not assured. Only use direct payoff-based results for quantitative predictions; apply qualitative findings where only contributions are measured.

# 6) Design Dimensions Highlighted Across Papers

**Strongly/directly informed dimensions** (frequently manipulated, moderated, or reported):
- `player_count`: Strongly covered; effects in small-medium groups are most known.
- `num_rounds`: Directly manipulated; longer games generally produce better efficiency improvements with punishment.
- `mpcr`: Standard moderator; lower MPCRs are harder environments, but punishment can still be effective.
- `punishment_cost` and `punishment_tech` (`punishmentMagnitude`/cost ratio): Central; efficiency effects are strongly dependent on these.
- `chat`: Often manipulated; communication frequently raises efficiency vs. control and interacts with punishment effects.
- `all_or_nothing`: Most studies use continuous contribution, but some manipulate binary vs. continuous structure.
- `reward_exists` (and cost/tech): Studied in parallel to punishment or as a combined treatment in several works.
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Sometimes present, but typically not the primary focus; reputation/identifiability is a frequent secondary manipulation.
- `default_contrib`: Contribution framing is less commonly manipulated; most lab studies default to opt-in (default keep).
- `show_punishment_id`: Peer punishment is often anonymous unless reputation is manipulated; not consistently specified.

**Sparse/missing dimensions**:
- Precise implementation of `default_contrib`, `show_n_rounds`, `show_punishment_id` is often unreported or only contextually specified.
- `all_or_nothing` is less often the primary manipulated variable, though some theory treats binary/step-level contribution.
- Multi-level reward structures and complex sanction/reward techs are infrequent.

# 7) Important Limitations

- **Payoff vs. behavioral outcomes**: Many studies report only cooperation/contribution, not group efficiency after punishment costs, making direct efficiency prediction difficult for those designs.
- **Generalizability**: The vast majority of high-quality evidence is from lab PGGs with small, homogeneous, WEIRD (Western, Educated, Industrialized, Rich, Democratic) samples; field evidence may not generalize due to different sanction mechanisms and contextual moderators.
- **Complex environments**: Real-world collective action and field experiments suggest that **costly, peer-based punishment is less prevalent and effective than coordination-based, reputational, or centralized sanctions** (Guala, 2012; Ostrom et al., 1992). Lab findings may overstate real-world efficiency gains.
- **Antisocial/counter-punishment**: Efficiency gains can be wiped out or reversed in settings with anti-norm/sanctioning, competitive contexts, or culture-specific tendencies toward antisocial punishment.
- **Sparse coverage of design space**: Some combinations of design dimensions (e.g., very high or low MPCR, very large group sizes, extreme punishment cost/impact ratios, presence of multiple simultaneous institutional features) are underexplored.
- **Missing or inconsistent reporting of critical dimensions**, especially for information/reputation, framing, and identifiability.
- **Non-linear or threshold games**: Most evidence is from linear PGGs; nonlinear production or threshold games may behave differently.

---

# Summary Table: Dimension-Level Evidence

| Dimension                | Directly/Strongly Informed         | Indirectly/Contextually Informed   | Sparse/Missing         |
|--------------------------|------------------------------------|------------------------------------|-----------------------|
| player_count             | Yes (small/moderate, 3–8)          | High/large sizes less covered      |                       |
| num_rounds               | Yes (6–27+)                        | One-shot/short games less covered  |                       |
| chat                     | Yes (communication/no-comm manip.) | Often interacts with punishment    |                       |
| all_or_nothing           | Partially (continuous > binary)    | Binary covered in some theory      |                       |
| default_contrib          | Rarely manipulated or reported     |                                    | Yes                   |
| mpcr                     | Yes (0.3–0.5)                      | Extreme values less covered        |                       |
| punishment_cost/tech     | Central focus, strong evidence     | Some ambiguity re: implementation  |                       |
| reward_exists/tech       | Often in parallel, but secondary   |                                    |                       |
| show_n_rounds            | Sometimes reported                  | Rarely a direct treatment          | Yes                   |
| show_other_summaries     | Sometimes (for reputation/monitor) |                                    | Yes                   |
| show_punishment_id       | Occasionally (for reputation)      | Commonly anonymous                | Yes                   |

---

## In summary:

The literature provides **strong empirical and theoretical support** for the prediction that, under standard lab PGG conditions and well-designed peer punishment mechanisms, enabling punishment will increase group efficiency relative to control (no-punishment) games, especially when baseline efficiency is low. The **effect is highly sensitive to punishment cost and technology, game repetition, group size, communication, and social context**. Many design dimension effects are represented directly in the evidence base, but some (e.g., large groups, detailed framing) are underexplored. **A careful, design-sensitive approach is required for prediction, especially for efficiency—not merely cooperation rates.** Important moderators and limitations must be explicitly considered when making any predictions based on these findings.
