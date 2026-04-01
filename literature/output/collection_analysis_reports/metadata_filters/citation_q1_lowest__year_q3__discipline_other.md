# 1) Evidence Base

This literature set consists of 11 papers: a mix of laboratory experiments (empirical, typically in economics or behavioral science), observational studies (field and case analysis), and a smaller number of theoretical papers. The set covers a variety of environments adjacent to or directly involving social dilemmas, public goods, and collective action. Only a minority of studies focus precisely on classic public-goods games (PGGs) with efficiency or group payoff outcomes as their primary endpoint, and fewer still manipulate peer punishment across the design dimensions relevant to the prediction task. Most studies focus on behavioral outcomes (e.g., cooperation rates), informal sanctioning mechanisms, or abstract theoretical models, often in settings only adjacent or partially corresponding to the prototypical PGG framework.

Overall, the evidence base is **broad in contextual coverage** but **narrow and incomplete for the specific downstream prediction task**: predicting efficiency effects of enabling peer punishment in public goods games parameterized by design dimensions.

# 2) Task Relevance

## a. `pgg_or_variant`
- **exact**: Only two papers (Engel, 2019; De Geest & Kingsley, 2021) use standard or near-standard PGG or CPR game designs.
- **close/adjacent**: Several others employ close variants (linear or threshold social dilemmas, CPR settings, binary contributions), but often with deviations such as one-shot play, community case studies, or non-game interventions.
- **adjacent/weak**: Many are field or theoretical studies with limited direct applicability.

## b. `punishment_or_sanctions`
- **exact**: Several papers implement explicit, game-embedded punishment (e.g., Engel, 2019; De Geest & Kingsley, 2021; Ferguson, 2021; Steimanis et al., 2020; Qirko, 2020).
- **adjacent**: Others focus on informal sanctions, external regulatory norms, or compensation rather than punishment per se (Gomez-Ruiz & Sánchez-Expósito, 2020; Albergaria & Saes, 2018).
- **none**: Some papers do not address punishment at all (Chang et al., 2021).

## c. `efficiency_or_related_payoff_outcome`
- **exact**: Only **one paper** (De Geest & Kingsley, 2021) reports efficiency or group earnings as a formal outcome, comparing with and without punishment.
- **adjacent/close**: Engel (2019) provides descriptive data on total earnings but does not analyze efficiency directly; most others report behavioral measures only (cooperation, contributions).
- **none/weak**: No direct efficiency or group payoff outcome is present in the majority.

**Summary:** The literature provides only patchy coverage of all three relevance axes—particularly for efficiency-related outcomes in the presence of explicit punishment in PGG-type tasks.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (efficiency, group payoff, earnings, welfare, surplus):**
  - **Directly measured:** De Geest & Kingsley (2021) (efficiency), Engel (2019) (group payoff, descriptive only).
  - **Not measured / only discussed:** All other papers.

- **Non-payoff behavioral outcomes (contribution/ cooperation/ punishment frequency/ norm compliance):**
  - **Primary focus**: Most studies, including those by Engel (2019), Gomez-Ruiz & Sánchez-Expósito (2020), Steimanis et al. (2020), Qirko (2020), Albergaria & Saes (2018), Pedroso (2021), focus on cooperation rates, free-riding responses, coordination, punishment events, or norm enforcement.

- **Qualitative or contextual observations:** Oria et al. (2018), Qirko (2020) provide qualitative/contextual insights on rule enforcement, trust, and sanction mechanisms.

**Key point**: The vast majority of outcome data is **not payoff-based**, limiting direct insight into efficiency effects for the prediction task.

# 4) Main Findings Relevant To Prediction

Synthesizing across papers:

### When peer punishment is explicitly enabled in (close to) PGG settings and efficiency or payoff is measured:
- **Punishment's effect on efficiency is heterogeneous**. In De Geest & Kingsley (2021), the effect of enabling punishment depends **crucially on context**:
    - **Equal endowments**: Peer punishment reduces efficiency due to high costs and uncoordinated enforcement.
    - **Unequal endowments**: Punishment can increase efficiency for some (low endowment) and not harm overall average earnings, as norm emergence around fairness improves targeting of punishment.
    - **Implication**: **Endowment heterogeneity/inequality is a key moderator**, influencing whether punishment improves or worsens efficiency.

- **Transparency/feedback features alter impact**. Engel (2019) finds that greater information about both contributions and punishment does **not** improve cooperation or efficiency and may even reduce it. High transparency can backfire, lowering contributions when punishment is observable at the individual level. This suggests **show_other_summaries** and **show_punishment_id** are key dimensions moderating punishment's effect on efficiency.

### When outcomes are behavioral rather than payoff-based:
- **Punishment mechanisms (including conditional or neutral) reliably increase cooperation or reduce free-riding** (Steimanis et al., 2020; Engel, 2019), but this does **not automatically lead to higher efficiency** (costly punishment may offset gains).
- **Informal mechanisms (e.g., team identity, trust)** can sustain high cooperation (Gomez-Ruiz & Sánchez-Expósito, 2020), suggesting that baseline cooperation levels may moderate the marginal effect of adding punishment.
- **Practical/real-world settings** (Qirko, 2020; Oria et al., 2018) report infrequent and situational use of actual punishment, emphasizing that mere presence of a punishment mechanism does not guarantee improved efficiency.

### Theory and mechanism arguments:
- Theoretical work (Pedroso, 2021; de Almeida, 2021) emphasize the role of information structure and macro-level norm enforcement but offer no quantitative guidance on efficiency or its moderators in punishment-enabled settings.

# 5) Prediction Guidance

- **The best empirically grounded prediction is conditional**:
    - If the PGG or CPR environment involves **equal endowments** and punishment is costly/ poorly coordinated, enabling punishment may **reduce efficiency** (De Geest & Kingsley, 2021).
    - If there is **endowment heterogeneity** or a salient fairness norm, peer punishment is more likely to **increase or at least not reduce efficiency**, via more effective targeting and coordination (De Geest & Kingsley, 2021).

- **Transparency/Feedback** (e.g., showing individual contributions and punishment decisions) can undermine the positive effects of punishment, reducing both cooperation and efficiency (Engel, 2019). Thus, **show_other_summaries** and **show_punishment_id** should be treated as potentially negative moderators of the punishment effect.

- **Game design dimensions that matter based on this literature**: player_count (group size), num_rounds (coordination over time), MPCR, punishment_cost, punishment_tech, endowment distribution (not always parameterized), and feedback/transparency variables.

- **Baseline cooperation matters**: If the control (no-punishment) game produces high efficiency, enabling punishment is less likely to add value and may incur unnecessary costs (Engel, 2019).

- **Behavioral trends (not direct efficiency-based)**: Increases in cooperation or norm compliance with punishment are frequent, but these need not translate into higher efficiency unless the net cost of punishment is low relative to the gain in contributions.

- **Absent or poorly covered prediction dimensions**: Effects of chat, reward mechanisms, contribution framing (default_contrib), and all-or-nothing versus continuous contributions are **not empirically addressed in relation to efficiency changes with punishment** in this literature.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed (by empirical efficiency or closely related payoff outcomes):**
  - `player_count` (group size): Varied and sometimes analyzed (De Geest & Kingsley, Engel).
  - `num_rounds`: Present in most lab experiments, sometimes noted as relevant for sustaining coordination.
  - `all_or_nothing`: Used in some experiments and theory papers as a binary contribution structure.
  - `mpcr`: Explicitly manipulated in several PGG and CPR experiments.
  - `punishment_cost`, `punishment_tech`: Key in lab experiments; `punishment_cost` shown to mediate efficiency effects.
  - Endowment distribution (contextual rather than parameterized): Central in De Geest & Kingsley (2021).

**Indirectly informed (by behavioral outcomes or field evidence):**
  - `show_other_summaries`, `show_punishment_id` (feedback/transparency): Highlighted in Engel (2019) as important moderators via effects on cooperation, not directly on efficiency.
  - `chat`, `reward_exists`, `reward_cost`, `reward_tech`: Mentioned but **not empirically linked to efficiency effects of punishment**.

**Only contextually discussed or missing:**
  - `default_contrib`: Not analyzed.
  - `reward_exists`, `reward_cost`, `reward_tech`: Virtually untouched for efficiency prediction in the context of punishment.
  - `show_n_rounds`: Sometimes present as a framing device, but not analyzed for impact on punishment's effect on efficiency.

# 7) Important Limitations

- **Scarcity of direct evidence**: Only one study (De Geest & Kingsley, 2021) provides a direct, empirical test of punishment's effect on efficiency, and only in a CPR context with two endowment structures.
- **Predominance of behavioral outcomes**: Most papers report changes in cooperation or punishment frequency, not efficiency or group payoff, limiting quantitative prediction of efficiency under treatment.
- **Narrow coverage of parameter space**: Key prediction dimensions such as reward systems, chat, contribution framing, and feedback are not systematically manipulated in relation to efficiency outcomes.
- **Generalizability issues**: Real-world/observational papers emphasize context dependence and infrequent use of sanctions, suggesting that lab results may overstate efficiency gains from enabling punishment in field settings.
- **Uncertain external validity**: Field findings suggest that the effects of punishment depend heavily on group identity, trust, and context, factors not easily captured by game parameterization alone.
- **Ambiguity in efficiency-behavior linkage**: Behavioral increases in cooperation or compliance due to punishment do not guarantee efficiency improvements, especially if punishment is costly or misdirected.

**In sum: the evidence base provides only modest and context-contingent predictive power for the downstream task of estimating efficiency changes when enabling peer punishment in PGG-like games. Key moderators are endowment distribution and transparency; many design parameters lack direct empirical support for their predictive influence on efficiency.**
