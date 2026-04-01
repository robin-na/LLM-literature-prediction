# 1) Evidence Base

The paper set consists entirely of empirical, experimental studies—mainly laboratory experiments, with one field experiment and one scenario-based/other experiment. The empirical focus is somewhat broad in that it covers a range of social dilemma environments: exact public goods games (PGGs), close variants (e.g., common-pool resource games, redistribution games, ultimatum or trust games), and some adjacent settings (e.g., principal-agent, scenario/vignette). Theoretical or purely mechanistic discussions are absent—all results derive from experimental manipulations.

For the downstream prediction task (efficiency impact of enabling peer punishment in PGG-like games), the set provides moderate-to-narrow direct empirical coverage: only a few studies directly report efficiency or group payoff in standard PGGs with and without punishment. Several papers measure only behavioral outcomes (e.g., contribution rates, punishment assigned, sentiment), or focus on centralized or institutional (not peer) punishment. Evidence on peer punishment’s payoff impact in standard PGGs is thus limited but present; broader contextual and behavioral evidence is richer.

# 2) Task Relevance

**pgg_or_variant**
- *exact*: Several papers (e.g., Kocher & Matzat, 2016; Castillo et al., 2021; Campos-Vazquez & Mejia, 2016; Windmann et al., 2021) use standard linear PGG designs or very close variants.
- *close*: Some studies use games with closely related features (e.g., redistribution, common-pool resource, or all-or-nothing framing).
- *adjacent/weak*: A subset address one-shot allocation games, trust/ultimatum games, or scenario-based designs, making their relevance more peripheral.

**punishment_or_sanctions**
- *exact*: Most studies manipulate or enable monetary punishment or sanctions, either in peer or centralized forms.
- *adjacent*: Some focus on reward/redistribution, non-monetary approval/disapproval, or social feedback; these count as adjacent or weak for direct punishment mechanism analysis.
  
**efficiency_or_related_payoff_outcome**
- *exact*: Only a small number report efficiency, group profit, or related payoff metrics *directly* (notably Kocher & Matzat, 2016; Castillo et al., 2021; Abbink et al., 2004; Przepiorka & Diekmann, 2020 (for adjacent settings)).
- *adjacent*: Most papers measure behavioral outcomes like contributions, cooperation, or punishment assigned, but not efficiency.
- *none*: Several studies (e.g., Windmann et al., 2021; Roberts et al., 2013) provide no payoff or efficiency data.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes (group, welfare, surplus, efficiency, total earnings):**
- *Directly measured*: Kocher & Matzat (2016), Castillo et al. (2021), Abbink et al. (2004), Przepiorka & Diekmann (2020).
- *Indirectly implied*: Becchetti et al. (2018) (implication from increased cooperation), others partially discuss group-level outcomes without reporting numerical efficiency.
- *Absent*: The majority report only behavioral indicators.

**Non-payoff behavioral outcomes (contribution rate, cooperation, punishment frequency, etc.):**
- Most studies, especially those on psychological drivers and mechanisms (e.g., Windmann et al., 2021; Leibbrandt & López-Pérez, 2014; Davis & Holt, 1999; Chen, 2012; Güth et al., 2007).

The distinction is crucial: Only a handful directly provide the group efficiency data that the prediction task requires.

# 4) Main Findings Relevant To Prediction

- **Punishment can increase cooperation but often reduces efficiency** in standard laboratory PGGs due to the (usually non-trivial) costs incurred by punishers, which can outweigh gains from higher cooperation (Kocher & Matzat, 2016; Abbink et al., 2004).
- **Centralized punishment** (e.g., a manager or leader) generally increases both cooperation and *efficiency* when compared with no-punishment baselines (Castillo et al., 2021). This contrasts with peer punishment, where efficiency gains are less consistent.
- **Reward mechanisms** and certain forms of redistribution can boost both cooperation and efficiency—sometimes more effectively and at lower net cost than punishment alone (Kocher & Matzat, 2016; Becchetti et al., 2018).
- **The cost and effectiveness (leverage) of punishment** matters: high punishment costs relative to payoff gains typically make overall efficiency fall—even if contribution rates rise (Kocher & Matzat, 2016; Abbink et al., 2004).
- **Peer punishment is often misdirected or used at intermediate rates** that do not optimize payoffs: when punishment is rare or universally anticipated (maximal deterrence), efficiency can approach optimum, but at intermediate levels the group pays both the cost of punishment and the cost of residual defection (Abbink et al., 2004).
- **Context and implementation details matter**: In field or real-world settings, enabling peer punishment may not increase cooperation or efficiency at all (Noussair et al., 2015), suggesting limited generalizability of positive lab results.
- **Behavioral outcomes (not payoff-based) are improved by punishment** in many adjacent settings, but translation to efficiency is either assumed or left untested (Campos-Vazquez & Mejia, 2016; Davis & Holt, 1999; Chen, 2012).

Overall: Peer punishment raises contributions but (in most lab work) does not reliably improve efficiency due to its costs; centralized punishment and reward mechanisms are more reliably efficiency-enhancing.

# 5) Prediction Guidance

**Direct implications for predicting treatment efficiency (enabling peer punishment), given design and control efficiency:**
- In standard linear PGGs with typical punishment protocols (moderate cost/effectiveness), enabling *peer punishment is more likely to decrease efficiency* relative to the control (no punishment), except when punishment is very cheap or universally deterring (Kocher & Matzat, 2016; Abbink et al., 2004).
- **If the control efficiency is already high**, enabling peer punishment is unlikely to create further gains and may reduce efficiency due to unnecessary punishment costs.
- **If centralized punishment is used** (a single ‘manager’ can punish), the effect flips: enabling punishment reliably increases efficiency (Castillo et al., 2021).
- ** Reward mechanisms (and ex post redistribution)** are more promising than punishment for raising efficiency, and their positive effects appear more robust across settings (Kocher & Matzat, 2016; Becchetti et al., 2018).
- **Game details matter**—larger group size (player_count), MPCR, punishment cost, and the ability to communicate (chat) may moderate the size of the effect, but direct efficiency evidence on these moderators is sparse.

Prediction using these papers should:
- Anticipate that enabling peer punishment in most lab-like PGGs decreases efficiency, unless design specifics (e.g., very low punishment costs or high leverage, or rarely used punishment) suggest otherwise.
- Take care when applying these findings to field or contextually different settings, as the effect may disappear or even reverse (Noussair et al., 2015).
- Centralized punishment is a positive outlier—expect efficiency gains when it is present.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions:**  
- `player_count`: Reported and manipulated in nearly all PGGs; evidence does not show strong moderation, but direct, comparative efficiency results by size are limited.
- `num_rounds`: Always specified; some indication that longer games allow for more punishment dynamics, but explicit moderation evidence is minimal.
- `punishment_cost`: Most efficiency-focused papers specify this; critical in determining whether punishment reduces or (exceptionally) enhances efficiency.
- `mpcr`: Always recorded; indirectly suggests higher baseline efficiency at higher MPCR, but not tested as moderator of punishment effect.
- `chat`: Manipulated in some studies; Kocher & Matzat (2016) note that absence/presence does not moderate punishment's efficiency impact.
- `all_or_nothing`: A factor in some (Becchetti et al., 2018); mechanism seems robust to this framing but direct efficiency comparisons are lacking.
- `show_n_rounds`: Specified in Przepiorka & Diekmann (2020); relevant for feedback/punishment expectation, but direct efficiency effect is untested.
   
**Indirectly or partially informed:**
- `punishment_tech`, `punishment_magnitude`: Sometimes specified; efficiency moderation not addressed explicitly.
- `reward_exists`, `reward_cost`, `reward_tech`: Covered where reward/redistribution is compared to punishment (Kocher & Matzat, 2016; Becchetti et al., 2018).
- `show_other_summaries`, `show_punishment_id`: Addressed in public feedback studies (Przepiorka & Diekmann, 2020), but for non-monetary punishment.
- `default_contrib`: Rarely described; opt-in/opt-out framing is not a major focus.
   
**Effectively missing:**  
- Systematic variation or testing of interaction/moderation by most dimensions is rare; most studies manipulate a few dimensions at a time.

# 7) Important Limitations

- **Sparse direct evidence on efficiency:** Only a minority of papers report the exact outcome (efficiency) required for the prediction task; most focus on behavioral responses to punishment/reward.
- **Peer vs. centralized punishment:** Several efficiency findings pertain to *centralized* punishment, which appears more beneficial than peer punishment; care is needed to avoid overgeneralizing these results.
- **Limited dimension-level moderators:** Comprehensive, systematic tests of specific game design dimension effects (especially interactions, e.g., how punishment cost interacts with group size) on efficiency change are lacking.
- **Generalizability:** Laboratory PGG results (where positive behavioral and negative efficiency effects of punishment are strongest) do not always replicate in naturalistic, field, or more complex settings (Noussair et al., 2015).
- **Behavioral vs. payoff confusion:** The literature frequently conflates increased contributions or cooperation rates with improved efficiency; in prediction, only actual payoff/efficiency measures should inform expectations.
- **Reward mechanisms not always available:** Papers showing strongest positive efficiency effects often focus on reward or hybrid mechanisms, which may not apply if the prediction task addresses punishment-only designs.
- **Ambiguity in intermediate punishment use:** Punishment’s efficiency effect is highly sensitive to frequency and targeting; moderate, misdirected, or spiteful punishment can be costly and inefficient, a nuance not always addressed quantitatively.

**In summary:**  
This literature base, while rich in behavioral and mechanistic insight, provides only modest direct empirical evidence for predicting the efficiency effects of enabling *peer* punishment in public-goods-game-like environments as a function of game design dimensions and control efficiency. It suggests that peer punishment usually reduces efficiency, that centralized punishment or reward can increase it, and that most prediction dimensions are only partially or contextually informed by the available studies. Caution is warranted in transferring these conclusions to settings substantially different from the closely studied lab PGGs.
