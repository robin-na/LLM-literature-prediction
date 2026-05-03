# 1) Evidence Base

The supplied paper set is **broad** and predominantly **empirical** (lab and field experiments), with a substantial number of **theoretical** contributions. Many papers provide **direct evidence** on standard linear Public Goods Games (PGGs) with and without punishment—core to the downstream prediction task. At the same time, several studies extend to **variant games** (threshold, asymmetric, trust games, CPR, repeated PD), or focus on **adjacent mechanisms** (rewards, exclusion, monitoring, democratic legitimacy).

The **empirical core** offers robust coverage of the canonical PGG with and without peer punishment. Variants and related domains (e.g., trust game, CPR, procurement games) expand the scope but may reduce direct applicability for a model strictly based on PGGs. On outcomes, most studies prioritize **contribution rates or cooperation**; a significant subset explicitly report **group efficiency, welfare, or total earnings**. However, some well-designed behavioral studies and field experiments do not provide efficiency data, limiting their direct value for efficiency prediction.

Some theoretical and review papers provide explicit mechanism insights and cross-study syntheses. Overall, the evidence base is **comprehensive** for standard public goods/punishment lab settings, but patchy (and more adjacent) for field variants or multi-mechanism (reward, expulsion, exclusion) games.

# 2) Task Relevance

**Relevance is assessed on three dimensions:**

- **pgg_or_variant**:  
  - **Exact**: Most empirical lab papers are on exact PGGs (e.g., Kocher & Matzat, Page et al., Reif et al., Wang & Qin, Dannenberg, Zheng & Nie).  
  - **Close/Adjacent**: Some key papers extend to threshold PGGs, CPR, trust games, procurement, insurance, but retain core social dilemma structure (e.g., Bigoni et al., Lévy-Garboua et al., Ahn et al.).  
  - **None/Weak**: Some behavioral or theoretical contributions use allocation games or contextually different dilemmas.

- **punishment_or_sanctions**:  
  - **Exact**: Many studies manipulate peer punishment (enabling/disabling, varying cost/tech, endogenous/exogenous) and compare directly to control. A minority test only adjacent mechanisms (rewards, exclusion) or focus on endogenous sanctions, e.g., coverage, demotion.
  - **Close**: Field and theory papers frequently consider punishment alongside other interventions.
  - **Weak/None**: Several papers omit any form of punishment or only discuss it briefly.

- **efficiency_or_related_payoff_outcome**:  
  - **Exact/Close**: A substantial subset has **group efficiency, total earnings, or welfare** as primary/secondary outcomes, and provide comparative or quantitative results (e.g., Kocher & Matzat, Page et al., Wang & Qin, Zheng & Nie, Grieco et al., Dannenberg, Kingsley & Brown, Buchholz et al.).
  - **Adjacent/Weak**: Many report only **contribution rates** or **cooperation** as proxies, or require inference for efficiency. Some field studies and theoretical models discuss only strategic or norm dynamics.
  - **None**: Several studies lack payoff-based outcomes entirely.

**Summary:**  
The literature set is **highly relevant** for predicting the impact of enabling punishment on efficiency in standard laboratory PGGs, **less so** as the design diverges from canonical PGGs (e.g., into CPR, insurance, or networked trust games).

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes:**  
  - **Directly measured**:  
    - **Efficiency** (group earnings as a fraction of the social optimum)  
    - **Total group earnings/payoff**  
    - **Welfare/surplus/mean income**
  - **Indirect/inferred**:  
    - Some studies allow estimation of efficiency (from contribution, marginal returns, and punishment cost data)
- **Non-Payoff Behavioral Outcomes:**  
  - **Contribution/cooperation rates** (most common primary outcome)
  - **Punishment frequency/targeting**
  - **Norm compliance, effort, harvest ratios, embezzlement, resource extraction**
  - **Punisher/rewarder selection, antisocial punishment**
  - Many studies focus solely on these behaviors, even where payoff implications are strong.

**Distinction:**  
Numerous papers find increased contributions under punishment, yet show no or negative effect on efficiency due to the cost of punishment (e.g., Kocher & Matzat, Dannenberg, Ramalingam et al.). Only a subset unambiguously link punishment to improved efficiency.

# 4) Main Findings Relevant To Prediction

## Empirical Findings

- **Punishment increases contributions but not always efficiency:**  
  - *Many studies* find that while peer punishment reliably increases contribution rates, the cost of administering punishment can fully offset (or exceed) contribution gains, resulting in unchanged or lower efficiency versus no-punishment controls (Kocher & Matzat, Dannenberg, Rockenbach & Wolff, Ramalingam et al., Zheng & Nie).
  - Efficiency **improves** only when punishment is **well targeted, not misused (no antisocial/retaliatory punishment), and/or is cost-effective** (Grieco et al., Wang & Qin—especially for exogenous/cash punishment).

- **Institutional details are decisive:**  
  - The **cost and technology of punishment** (punishment_cost, punishment_tech), **punisher selection/identity** (show_punishment_id), **group size** (player_count), and **legitimacy/consensus** (chat, endogenous/democratic institution formation, agreements) are key moderators.
  - *Redistributive* punishment (burned fines redistributed as rewards) can actually increase efficiency in contrast with standard (burned) fines (Page et al.).
  - **Effectiveness of enforcement** (centralized vs. decentralized, targeted vs. random, endogenous access to punishment) also critically shapes outcomes (Ramalingam et al., Grieco et al., Kingsley & Brown, Zheng & Nie).

- **Contextual moderators:**  
  - **Group size effects**: In some settings, punishment increases efficiency in small groups but decreases or fails in larger groups unless designed for legitimacy and transparency (Zheng & Nie, Hwang).
  - **Communication (chat)**: Robustly increases efficiency and may diminish the need for punishment (Rockenbach & Wolff, Noussair & van Soest). Its presence tends to improve outcomes even in the absence of explicit sanctions.
  - **Agreement/Norm consensus**: Punishment is most efficiency-enhancing when a clear, ambitious group norm or agreement exists (Dannenberg). Without shared expectations, punishment more often raises costs without securing large payoff gains.

- **Negative or null effects:**
  - **Imperfect/limited punishment**: Weak or ambiguous punishment (e.g., when costly to acquire punishment rights, low monitoring, low legitimacy) can fail to increase, or even lower, efficiency (Ramalingam et al., Kingsley & Brown, Robbett).
  - **Antisocial/counter-punishment**: When punishment is misused—punishing cooperators or in response to punishment—efficiency can be reduced (de Melo & Piaggio, Romaniuc et al.).
  - In **heterogeneous groups** or field contexts, punishment effects are often **weaker or inconsistent** (Robbett; field papers).

## Theoretical/Mechanism Arguments

- **Enforcement cost and efficiency**: Most formal models agree that punishment can, in theory, sustain high efficiency if it is **credible, coordinated, and not prohibitively costly** (Hwang; Buchholz et al.; Chassang & Zehnder; Yu et al.).
- **Network, monitoring, and legitimacy**: Social structures—who can observe whom, network connectivity, and legitimacy of punishment—are decisive for whether punishment will actually be used and yield efficiency (Balmaceda & Escobar; Buchholz et al.; Forges et al.).
- **Dynamic and evolutionary stability**: Models show that repeated interactions, possibility of retaliation, and evolutionary dynamics all affect whether punishment leads to sustained efficiency or wasted costs (Ochea, Fujiwara-Greve et al., Yu et al.).

# 5) Prediction Guidance

The literature indicates **no universal answer**: Enabling peer punishment in public-goods-like games increases contributions **almost always**, but its effect on **average efficiency** (group earnings as a fraction of social optimum) depends on design details highlighted below.

**For prediction:**

- **If control efficiency is low and punishment is**:
  - **Cheap and effective** (high punishment magnitude/cost ratio)
  - **Easily available** (punishment rights universal or no/low acquisition cost)
  - **Well targeted, legitimate, and coordinated** (identity shown, transparent, group consensus)
  - **Without substantial antisocial punishment**
  
  **Then:** Enabling punishment **likely increases efficiency**, possibly substantially above the control (Wang & Qin, Page et al., Reif et al., Grieco et al., Hwang, Buchholz et al.).

- **If punishment is**:
  - **Costly or hard to acquire** (even a small cost suppresses use)
  - **Inefficiently used, with antisocial or retaliatory punishment common**
  - **Implemented in a large, heterogeneous, or poorly coordinated group**
  - **Legitimacy is low, no clear agreement/norm exists**
  
  **Then:** Enabling punishment will **not increase efficiency** and may lower it compared to control (Kocher & Matzat, Rockenbach & Wolff, Ramalingam et al., Lowen & Schmitt, Robbett). Cases where efficiency with punishment falls below control are mostly associated with high punishment cost, mis-targeted punishment (especially in large groups), or settings lacking robust norms.

- **Important caveat:** *Even when punishment increases efficiency, the improvement is never to the full cooperative optimum unless punishment is both highly effective and barely used in the equilibrium* (i.e., the threat suffices, actual punishment is rare, and cooperation is robust).

- **Critical dimensions for modelers:**  
  - **Control efficiency is a strong baseline moderator**: If control game already yields high efficiency, little or no gain is expected from enabling punishment, and losses due to cost are possible.
  - *Effect sizes can often be interpreted in reference to directly reported group earnings/efficiency in the relevant empirical papers* (e.g., Zheng & Nie provides efficiency figures by treatment and group size).
  - **No strong evidence** is found for persistent post-treatment efficiency gains from temporary punishment regimes (Bruttel & Friehe).

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions** (empirical/theoretical findings consistently report and analyze impact):

- **player_count**: Effects of group size are extensively analyzed; larger groups pose coordination challenges, may moderate punishment’s benefits (Zheng & Nie, Hwang).
- **num_rounds**: More rounds allow for learning and retaliation/coordination (Wang & Qin, Grieco et al., Page et al.).
- **mpcr**: Key driver of underlying incentives; higher MPCR can substitute for punishment or interact with it (Bruttel & Friehe, Page et al.).
- **punishment_cost, punishment_tech (magnitude/effectiveness)**: *Most critical* for positive efficiency effects (Kocher & Matzat, Page et al., Ramalingam et al.).
- **all_or_nothing**: Continuous vs. discrete contribution interacts with targeting and impact of punishment (varied across studies).
- **show_punishment_id**: Transparency/legitimacy/targeting moderates effect (Zheng & Nie, Khadjavi et al., Grieco et al.).
- **reward_exists, reward_cost, reward_tech**: Compared or combined with punishment in several studies (Kocher & Matzat, Page et al., Greiff).

**Indirectly/contextually discussed dimensions**:

- **chat**: Communication’s effect on coordination and efficiency is robust, often interacts with punishment (Rockenbach & Wolff, Noussair & van Soest).
- **default_contrib**: Status quo/contribution framing influences baseline cooperation; evidence less direct regarding interaction with punishment (Messer et al.).
- **show_n_rounds, show_other_summaries**: Information treatments are relevant but less systematically tested for their impact on punishment efficiency dividends.

**Effectively missing or only contextually touched**:  
- **default_contrib, show_other_summaries, show_n_rounds** (when not core to the design or reporting) are infrequently linked to efficiency outcomes in punishment treatments.
- Cross-dimensional interactions (e.g., punishment with threshold PGG, combinations of reward and punishment) are less systematically explored for direct efficiency prediction.

# 7) Important Limitations

- **Payoff–behavior confusion:** The most common outcome reported is contribution rate, not efficiency. Relying on contribution alone risks conflating increased cooperation with improved group welfare. Where efficiency is unreported, inference is possible but potentially misleading if punishment costs are high.

- **Context specificity:** Most decisive findings come from **standard linear lab PGGs with small groups, explicit punishment, and no communication**. Generalization to field settings, heterogeneous groups, or real-world context is risky. Field experiments and non-lab studies sometimes show weaker, null, or reversed effects (Noussair et al., Robbett, de Melo & Piaggio).

- **Punishment institution and legitimacy:** Effects are highly sensitive to nuances (e.g., endogenous vs. exogenous punishment rights, anonymous vs. public punishment, existence of clear norms). These subtleties may not be fully captured by the 14 design dimensions.

- **Sparse or indirect data on some dimensions:** Not all 14 prediction dimensions are equally represented (e.g., show_other_summaries, default_contrib, chat). Information treatments, framing, and monitoring costs are sometimes discussed but rarely varied experimentally with direct efficiency measurement.

- **Interaction effects:** Design features interact (e.g., punishment with chat or agreement). These combinatorial effects are not modular and are not empirically mapped in all combinations. Post-treatment or removal effects (hysteresis/crowding out) are little studied (Romaniuc et al., Bruttel & Friehe).

- **Non-universal effect direction:** There is **no universal direction of punishment's impact on efficiency**, despite consistently positive effects on contribution. Predictive models based on these literatures must condition on key moderators.

---

**References (by example):**  
Kocher & Matzat, 2016; Page et al., 2013; Reif et al., 2017; Wang & Qin, 2015; Ramalingam et al., 2016; Zheng & Nie, 2013; Grieco et al., 2017; Dannenberg, 2016; Lowen & Schmitt, 2013; Rockenbach & Wolff, 2016; Kingsley & Brown, 2016; Hwang, 2017; Robbett, 2016; Bruttel & Friehe, 2014; Romaniuc et al., 2016.
