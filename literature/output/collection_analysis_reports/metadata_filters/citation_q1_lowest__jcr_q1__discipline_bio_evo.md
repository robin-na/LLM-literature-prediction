# 1) Evidence Base

This paper set includes 19 items, with a mixture of **empirical experimental studies** (both lab and field) and **theoretical/computational models**. The **empirical studies** often use public goods games (PGGs) or close variants, but several address adjacent games (e.g., CPR, dictator, PD) or use single-player/non-strategic contexts. The **theory papers** typically focus on evolutionary game dynamics, agent-based simulations, or mechanism arguments relating to punishment, norm compliance, and group structure.

The set is **broad in its coverage of social dilemmas and cooperation**, but **narrow in directly addressing the central downstream prediction task**: the effect of enabling peer punishment (versus disabling it) on efficiency or group payoff in multi-round, multi-player PGGs. Only a minority of papers provide exact evidence for all three: PGG/variant + punishment/sanction + efficiency/payoff. Many supply indirect or contextual insights, particularly regarding cooperation, norm-following, or mechanisms underlying punishment, rather than direct payoff outcomes. There is at least one high-relevance theory paper (Powers et al., 2023) and one strong empirical paper with exact relevance (Nhim et al., 2023); the remainder are best seen as providing background, mechanisms, or moderating insights.

---

# 2) Task Relevance

For the three key target-relevance dimensions:

- **PGG or Variant**
  - **Exact**: Several papers (e.g. Powers et al., 2023; Nhim et al., 2023; Odouard et al., 2023) use standard PGGs.
  - **Close**: A few use public bads or CPR games (Del Ponte et al., 2025; Gallier et al., 2018).
  - **Adjacent/None**: Many use PDs, dictator games, or non-group contexts.

- **Punishment or Sanctions**
  - **Exact**: Some papers include explicit punishment or sanctioning mechanisms (Powers et al., 2023; Odouard et al., 2023; Nhim et al., 2023; Del Ponte et al., 2025).
  - **Close/Adjacent**: Others feature destruction or reputational sanctions, or examine intrinsic motivation/sanctions (Wen et al., 2025; Geschwind & Lambsdorff, 2025), or rule-following with/without punishment (Gächter et al., 2025).
  - **None**: Several do not address punishment directly.

- **Efficiency or Related Payoff Outcome**
  - **Exact**: Explicit group efficiency or welfare measured in a few (Powers et al., 2023; Nhim et al., 2023; Del Ponte et al., 2025).
  - **Close/Adjacent**: Some papers infer efficiency via cooperation rates or payoff-related outcomes (Morsky et al., 2024; Graser et al., 2025).
  - **None**: Most emphasize behavioral outcomes (e.g., cooperation, norm compliance) rather than efficiency.

**In summary:** Only a **small subset** is of **exact** relevance to the prediction task; the remaining papers offer background or mechanism context, not direct quantitative evidence about the effect of enabling punishment on efficiency in PGGs.

---

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes** (`efficiency`, `group payoff`, `welfare`, `surplus`, `total earnings`):
    - Reported directly in a handful of studies (Powers et al., 2023—model; Nhim et al., 2023—experiment; Del Ponte et al., 2025—experiment).
    - Several others are adjacent, inferring payoff only from behavioral results or in non-PGG contexts (Morsky et al., 2024; Graser et al., 2025).

- **Non-Payoff Behavioral Outcomes** (`contribution rate`, `cooperation rate`, `punishment frequency`, `norm compliance`, `trust`, `rule-following`, etc.):
    - The overwhelming majority of papers focus on these outcomes, examining:
      - The impact of various mechanisms (punishment, information, social/normative structure) on behavior.
      - Effects of punishment on compliance or cooperation, not efficiency.
    - **Importantly:** Raised cooperation does not always translate to raised efficiency (e.g., if punishment is costly or misapplied).

- **Distinction is maintained** in most papers, and several explicitly note the gap (e.g., Odouard et al., 2023; Wen et al., 2025).

---

# 4) Main Findings Relevant To Prediction

## Cross-paper synthesis

**A) Peers and institutionally arranged punishment generally enable higher efficiency—but only under specific cost and implementation conditions:**
  - **Theory:** Institutional punishment *can* substantially increase efficiency as group size grows, *if* consensus costs and hierarchy/administration are properly managed and punishment is not over- or under-applied (Powers et al., 2023).
  - **Empirical evidence:** Costly punishment mechanisms can raise cooperation but do *not always* improve payoff/efficiency, particularly if the costs of punishment outweigh the benefits (Nhim et al., 2023; Del Ponte et al., 2025).

**B) The cost structure and form of punishment critically moderate its impact:**
  - **High-cost punishment** may undermine efficiency even if it increases cooperation rates (Nhim et al., 2023).
  - **Tax/minimum contribution (costly enforcement by rule)** can be more efficient than peer punishment, as it avoids direct enforcement costs.
  - **Avoidable or voluntary punishment (pledge-based games)** may have *no* efficiency effects if participants avoid penalties by opting out or making weak pledges (Del Ponte et al., 2025).

**C) Behavioral outcomes do not always map onto efficiency:**
  - Many studies find rising cooperation or rule-following under punishment (Gallier et al., 2018; Odouard et al., 2023), but these may not lead to higher group payoffs when enforcement is costly.

**D) Moderators and context:**
  - **Group size, MPCR (marginal per-capita return), and punishment cost** are widely identified as moderators of punishment effectiveness (Powers et al., 2023; Nhim et al., 2023).
  - **Norm internalization** can catalyze higher cooperation, but is only indirectly linked to efficiency (Odouard et al., 2023).
  - **Punishment implementation details** (direct/indirect, voluntary/automatic) affect whether efficiency benefits are realized (Wen et al., 2025; Del Ponte et al., 2025).

**E) Context-specific findings:**
  - Rewards, chat, and alternative social information structures can also influence cooperation and efficiency, but few papers in the set speak directly to their interplay with punishment.

---

# 5) Prediction Guidance

**For downstream prediction of treatment efficiency when enabling peer punishment:**

- **Do not assume enabling punishment always increases group efficiency.** The evidence shows:
    - If punishment is **costly** and the cost is substantial, it can **increase cooperation without raising—or even reducing—efficiency** (Nhim et al., 2023).
    - **Efficiency gains from punishment are realized only when punishment cost is low relative to the gains from cooperation**, and institutional design is optimal (Powers et al., 2023).
    - **In decentralized, voluntary, or easily-avoided punishment systems, efficiency may remain unchanged** (Del Ponte et al., 2025).

- **Use control efficiency as an anchor:** If the control (no punishment) efficiency is high, enabling punishment may not yield gains and may even reduce efficiency if costs or misapplications rise. If control efficiency is low, and the punishment mechanism is well-designed (low cost, not easily avoided, optimally administered), then a positive effect on efficiency is more plausible.

- **Consider design dimensions critically:** Especially group size, MPCR, punishment cost, and the details of enforcement/punishment implementation.

- **Be cautious extrapolating from non-payoff behavioral outcomes**, as higher cooperation does not guarantee higher efficiency.

---

# 6) Design Dimensions Highlighted Across Papers

**Directly informed:**
  - `player_count` (Powers et al., 2023; Nhim et al., 2023; Odouard et al., 2023; Del Ponte et al., 2025; several others)
  - `num_rounds` (Nhim et al., 2023; Odouard et al., 2023; Del Ponte et al., 2025)
  - `mpcr` (Powers et al., 2023; Nhim et al., 2023; Odouard et al., 2023; Graser et al., 2025; others)
  - `punishment_cost` (Powers et al., 2023; Nhim et al., 2023; Odouard et al., 2023)
  - `punishment_tech` (design of enforcement; Powers et al., 2023; Odouard et al., 2023; Wen et al., 2025)
  - `all_or_nothing` (binary/continuous contributions; several)
  - `chat` (Nhim et al., 2023; Del Ponte et al., 2025)
  - `default_contrib` (Del Ponte et al., 2025)
  - `show_n_rounds` (Burton-Chellew et al., 2021)

**Indirectly or contextually discussed:**
  - `show_other_summaries` (Odouard et al., 2023; Morsky et al., 2024; Burton-Chellew et al., 2021)
  - `show_punishment_id` (not directly, but listed in some game descriptions)

**Sparse or missing:**
  - `reward_exists`, `reward_cost`, `reward_tech` (few papers consider rewards alongside punishment)
  - Precise distinctions in punishment implementation (peer vs. institutional, voluntary vs. automatic punishment) are occasionally captured.

---

# 7) Important Limitations

- **Few papers provide direct empirical evidence on efficiency effects of enabling peer punishment in PGGs.** Most studies are either simulation/theoretical, focus on non-payoff outcomes, or examine adjacent game structures.

- **Payoff-related outcomes are often missing or only adjacent.** Many findings about cooperation, compliance, or norm-following may not translate directly into efficiency predictions.

- **Mechanism and context specificity:** The effectiveness of punishment depends crucially on cost structures, implementation (institutional vs. peer, voluntary vs. automatic), the ability for participants to opt out or avoid punishment, and the presence or absence of supporting institutions/hierarchy.

- **Several design dimensions are not systematically varied or reported,** including reward mechanisms and details of social information. Reported outcomes may not fully capture the effects of features like chat, observability, or default contribution.

- **Game variants and non-PGG evidence:** Much insight is drawn from adjacent games (CPR, PD, trust games, dictator games), which may not fully generalize to PGG contexts.

- **The mapping from higher behavioral cooperation to higher efficiency is not always reliable** due to potentially high enforcement costs or punishment misapplication.

- **Finally, predictions based on simulation/theory should be cautiously extrapolated** to empirical settings, especially for institutional design recommendations.

---

**In summary**, this literature base provides *tentative, context-sensitive* guidance: peer and institutional punishment *can* raise efficiency in PGGs, especially with well-designed, low-cost institutions and in larger groups, but may not do so when costs are high, institutions are poorly incentivized, or punishment is avoidable. Several key design dimensions (especially cost and group size) are directly relevant, but the translation from increased cooperation to increased efficiency is not guaranteed and is sensitive to the details of punishment implementation.
