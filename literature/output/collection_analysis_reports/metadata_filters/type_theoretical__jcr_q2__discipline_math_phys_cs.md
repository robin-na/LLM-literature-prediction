# 1) Evidence Base

**Composition:**  
The paper set consists of 226 papers, dominated overwhelmingly by theoretical and simulation-based modeling studies, with very few (effectively no) actual experimental or real-human empirical studies that directly report efficiency changes due to punishment in public goods games (PGGs). Nearly all models are evolutionary or agent-based rather than laboratory behavioral experiments.

**Breadth:**  
The evidence base is **broad in terms of modeled environments, game structures, network types, and a wide range of design parameters**, but is **narrow with respect to direct empirical measurement of efficiency outcomes** in PGGs with and without peer punishment. Nearly all studies use variants of the PGG or closely related social dilemma games (e.g., snowdrift or trust games) and explore both standard and nonstandard punishment mechanisms. Reward, exclusion, institution-building, group structure, and other design dimensions are often considered alongside or as alternatives to punishment.

**Empirics vs. Theory:**  
Almost all findings are based on **theory or simulation** (~100%) rather than controlled laboratory or field experiments. Most studies focus on stationary distributions of strategies, average payoff, or proxy measures for efficiency, with explicit focus on group payoff/efficiency in a minority of cases. Some papers provide analytic or numerical solutions mapping design parameters to cooperation frequency and payoff; others offer phase diagrams or qualitative regime descriptions.

---

# 2) Task Relevance

## a) pgg_or_variant
- **Relevance:** `exact` for the majority of studies—most directly model PGGs (including spatial, voluntary, threshold, multi-level, and continuous versions). However, a substantial subset use close variants (snowdrift, N-person prisoner's dilemma, common pool resource, trust game), sometimes with only structural similarity.  
- **Assessment:** The literature is highly relevant (`exact` to `close`) for mapping findings to public-goods-game-like settings, but for some mechanism papers, only `adjacent` relevance applies.

## b) punishment_or_sanctions
- **Relevance:** `exact` for a large fraction, often explicitly manipulating presence/absence and detailed design of punishment, including peer punishment, institutional punishment, and exclusionary sanctions. Some papers focus primarily on reward, exclusion, or alternative mechanisms, providing only `close` or `adjacent` relevance for punishment.  
- **Assessment:** The set gives **strong coverage of punishment as a mechanism**, with variations in technology (peer, pool, centralized), cost, effectiveness, and implementation rules.

## c) efficiency_or_related_payoff_outcome
- **Relevance:**  
  - **`exact` or `close` (payoff, efficiency, group welfare, surplus):** about half the studies (especially reviewed and heavily cited models) report average group payoff or efficiency (relative to full cooperation), sometimes providing explicit formulas or numerical results.
  - **`adjacent` or `weak` (cooperation rates/other proxies):** Many focus on behavioral outcomes (frequency of cooperation, strategy abundance, defection rate, prevalence of norm enforcement) which are only indirectly related to efficiency, or focus primarily on the conditions for cooperation rather than explicit payoff outcomes.  
  - **Some studies expressly note that increased cooperation does not always result in higher group efficiency** (e.g., when punishment is costly or overused).
- **Assessment:** **Overall relevance is high for mechanism, moderate for quantitative efficiency prediction.** Most findings are theoretical predictions or qualitative mappings, not empirical point estimates of efficiency improvement.

---

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes (Direct):**
- **Efficiency/group payoff/surplus/welfare/total earnings:** Reported directly, with explicit ratios (treatment vs. full cooperation) or as average payoff in a subset of papers (e.g., Powers, 2018; Wu et al., 2014; Sun et al., 2025; Zhuang et al., 2012; Wang et al., 2010; Zhang et al., 2019; Dejong et al., 2008; Sasaki, 2014; Kol’veková et al., 2021; Nasrallah & Cheaib, 2016; Mariano & Correia, 2015).
- **Performance under parameter regimes:** Some theory papers provide parameter-space maps for efficiency, including when enabling punishment.

**Non-Payoff Behavioral Outcomes (Adjacently Measured):**
- **Cooperation/contribution rates:** More common than payoff; many papers report equilibrium frequencies of cooperation, punishment, or defection only.
- **Punishment frequency, norm compliance, exclusion rates, prevalence of strategy types:** Used frequently as proxies, but do not measure group efficiency.
- **Strategy abundance, evolutionary stability, transitions/coexistence:** Focused on the sustainability of strategies rather than total group payoff.

**Explicit Distinctions:**
- Papers regularly note that **higher cooperation does not guarantee higher efficiency** when punishment is expensive or causes resource losses that outweigh cooperative gains (e.g., Quan et al., 2019; Wang et al., 2020).

---

# 4) Main Findings Relevant To Prediction

**Empirical Synthesis:**

1. **Punishment Can Raise Efficiency, But Not Universally**
    - The consensus in theoretical and simulation models is that **enabling punishment usually raises efficiency and/or average group payoff compared to a no-punishment (control) PGG**, especially in environments where the control is inefficient due to defection (Powers, 2018; Wu et al., 2014; Sasaki, 2014; Kol’veková et al., 2021; Nasrallah & Cheaib, 2016; Mariano & Correia, 2015).
    - **Effect size, presence, or even direction depends critically on punishment cost, fine/magnitude, effectiveness, group structure, and norms.** Efficiency may decrease or even fall below control if punishment is overused, too expensive, or poorly targeted (Quan et al., 2019; Wang et al., 2020; Isakov & Rand, 2012).

2. **Parameter Sensitivity and Interactions**
    - **Cost of punishment:** Lower cost per unit (and higher effectiveness per cost) is consistently associated with greater efficiency gains when punishment is enabled (Wu et al., 2014; Zhang et al., 2019; Wang et al., 2010; Sui et al., 2017).
    - **Marginal per capita return (mpcr):** Efficiency gains from punishment are strongest at low mpcr (where the control is most inefficient), and punishment can transform a low-efficiency regime into a high-efficiency one (Wu et al., 2014; Zhuang et al., 2012; Cui et al., 2022). At high mpcr, less additional efficiency is gained, as control efficiency is already high.
    - **Player count and group size:** Larger group sizes can facilitate or undermine the effects of punishment, depending on whether the punishment remains effective and cost-per-punisher remains reasonable (Sui et al., 2017; Sasaki, 2014; Kol’veková et al., 2021).
    - **Population structure (spatial, networked):** Structure matters. **Spatial and small-world networks** often magnify the effect of punishment on efficiency, primarily via network reciprocity and the ability of clusters of punishers/cooperators to resist defectors (Cui et al., 2022; Wu et al., 2014; Chung et al., 2013).
    - **Punishment technology:** Peer punishment is effective but less robust and more vulnerable to second-order free-riders than pool punishment or institutional forms, which, when properly designed, yield higher, more stable efficiency (Sigmund et al., 2011; Sasaki, 2014; Kol’veková et al., 2021).
    - **Institutional design (pool, peer, tax-based):** Institutional or tax-based punishment is often more effective at sustaining cooperation and efficiency than voluntary peer punishment, **if appropriately funded and targeted** (Yao & Chen, 2014; Yang & Yang, 2024).
    - **Combination with reward/exclusion:** Punishment combined with reward or exclusion can be especially effective; in some models, reward alone can outperform punishment on efficiency; in other cases, the optimal is a blend (Zhuang et al., 2012; Sun et al., 2025; Cong et al., 2016; Gao & Liang, 2020).

3. **Nonlinear and Non-Monotonic Effects**
    - The effect of punishment on efficiency is often **non-monotonic**: There is typically a threshold punishment severity/effectiveness below which there is little or no effect, and above which efficiency or cooperation sharply increases. However, **punishment that is too severe or too costly can reduce efficiency** via excessive expenditure or destabilizing cooperation (Quan et al., 2019; Kol’veková et al., 2021; Podobnik et al., 2019).
    - **Parameters such as reputation, second-order punishment, and optional participation** moderate when and how punishment increases efficiency, with voluntary participation and reputation often reinforcing positive efficiency effects.

4. **Context-Dependent Moderators & Boundary Conditions**
    - **Design dimensions such as chat, default contribution, identity disclosure, network topology, information structure, and the presence of other oversight or sanctioning mechanisms** are sometimes modeled but less frequently mapped directly to efficiency outcomes.
    - **High punishment costs or inefficient implementation can cause punishment to backfire** and reduce group payoff below the control (no-punishment) condition (Quan et al., 2019; Isakov & Rand, 2012; Prietula & Conway, 2009).
    - **Control-game efficiency is not always predictive of treatment-game efficiency:** In some cases, enabling punishment moves the system from low to high efficiency; in others, if the control is already efficient (high mpcr, small group, strong baseline cooperation), the marginal gain is small.

---

# 5) Prediction Guidance

- **If the control game (no punishment) is inefficient (low contribution, high defection, low group payoff), enabling punishment is likely to increase group efficiency, often dramatically—**but only if punishment parameters (cost, fine/effectiveness, targeting) are appropriately set (Wu et al., 2014; Sun et al., 2025; Sasaki, 2014; Nasrallah & Cheaib, 2016).
- **The predicted efficiency gain is maximized when punishment cost is low, effectiveness is high, and population/game structure supports identification and targeting of defectors.**
- **If punishment is too costly (relative to the benefit), is misapplied, or is overused, efficiency may stagnate or decrease versus control, despite higher cooperation/contribution rates (Quan et al., 2019; Wang et al., 2020; Isakov & Rand, 2012).**
- **Institutional punishment (tax-funded, shared, pooled) is more robust and typically outperforms pure peer punishment or exclusion-based punishment for sustaining efficiency,** provided the institution is well-designed and is not vulnerable to corruption, insufficient funding, or second-order free-riders (Kol’veková et al., 2021; Yang & Yang, 2024; Yao & Chen, 2014; Sigmund et al., 2011).
- **The effect of punishment is moderated by group size, mpcr, network topology, and the existence of secondary mechanisms (reward, reputation, exclusion).** Factors such as visibility of outcomes (show_other_summaries), presence of chat, or identity disclosure may have effects, but are weakly represented in direct efficiency outcome data.
- **Behavioral outcomes (like cooperation frequency, norm compliance, or punishment rate) should not be used alone as proxies for efficiency.** They must be adjusted for the cost of punishment, the loss to group resources, and the opportunity cost relative to full cooperation.
- **Parameter mapping:** Where a direct empirical or simulated mapping from design dimensions to efficiency exists, these should be used for quantitative prediction; where not available, robust qualitative expectations can be drawn about the direction of effect and likely moderators.

---

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- `player_count` (group size): Frequently varied in models (Kol’veková et al., 2021; Sui et al., 2017; Wu et al., 2014).
- `num_rounds`: Often modeled as infinite or many rounds; occasionally discussed (Powers, 2018; Wang et al., 2010).
- `all_or_nothing`: Both continuous and all-or-nothing models present.
- `mpcr` (marginal per-capita return): A central moderator in almost all studies, with strong evidence about its effect.
- `punishment_cost`, `punishment_tech`: Nearly always manipulated or mapped; key parameter for efficiency outcome.
- `reward_exists`, `reward_cost`, `reward_tech`: Many studies manipulate reward alongside punishment.
- `punishment_exists`: Almost always a manipulated variable.

**Indirectly Informed or Contextually Discussed:**
- `chat`, `default_contrib`: Seldom directly varied, but sometimes appear in discussion of communication or framing effects. Little evidence for direct efficiency effect.
- `show_n_rounds`, `show_other_summaries`, `show_punishment_id`: Rarely manipulated in the payoff studies; some precedent for their behavioral impact, but little on efficiency.
- `show_punishment_id`: Occasionally modeled as a way to increase punishment effectiveness (via reputation, identification), but weak effect on measured efficiency.

**Design Dimensions Effectively Missing:**
- None of the core payoff papers directly examine real-time chat, default contribution framing, or round/historical information disclosure in a way that yields efficiency outcome mappings.

**Other Contextual Moderators in Literature:**
- Population structure (well-mixed vs. spatial or networked)
- Optional/voluntary participation vs. compulsory participation
- Information structure (full vs. partial vs. noisy)
- Mechanism for punishment financing (peer-funded, institution/tax, endogenous, exogenous)

---

# 7) Important Limitations

- **Empirical evidence is almost entirely absent;** predictions are based on theory and simulation, which may not transfer cleanly to human behavioral experiments or real-world settings.
- **Very few papers provide direct parametric mapping from the full set of 14 game design dimensions to efficiency outcomes.** Most focus on a subset (group size, mpcr, punishment cost/effectiveness, and network structure).
- **Punishment is not always beneficial:** Several models demonstrate conditions under which punishment reduces efficiency compared to control (high punishment cost, poor targeting, overuse, ineffective identification, excessive institution cost, or when cooperation is already high in the control).
- **Some design moderators (chat, default contribution, show_other_summaries, show_n_rounds, show_punishment_id) are rarely or never studied in relation to efficiency;** predictions for their effect must be extrapolated with caution.
- **Most outcome measures are behavioral, not efficiency-based.** Caution is needed when inferring efficiency effects from cooperation rates.
- **Ambiguity exists in mechanism and direction of effect in multiple models:** Some studies highlight that increased punishment can destabilize cooperation or lead to inefficiency under some parameterizations (Quan et al., 2019; Isakov & Rand, 2012).
- **No real-world evaluative studies or field data are present,** and so predictions must be understood as pertaining to stylized agent-based or evolutionary game models, not laboratory or societal behavior.

---

**In summary:**  
The reviewed literature strongly supports that **enabling peer punishment in a PGG-like environment will generally—but not always—increase average efficiency versus control, especially when both the cost and the implementation of punishment are well-calibrated to the group's structure and the baseline efficiency is low.** The effect is critically mediated by punishment cost, effectiveness, group/network structure, and interaction with other institutional parameters. **Prediction for specific parameterizations should be based only on those dimensions which the literature directly maps to efficiency outcomes; caution is warranted when extrapolating from behavioral to payoff-based effects or from parameter spaces with little direct evidence.**
