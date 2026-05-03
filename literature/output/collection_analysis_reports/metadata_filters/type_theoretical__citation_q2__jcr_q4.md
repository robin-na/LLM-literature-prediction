# 1) Evidence Base

The paper set consists entirely of **theory papers** (7/7), with no new empirical or experimental studies. This base is **narrow** in its direct application for downstream prediction of treatment efficiency: none of the papers provide new quantitative estimates of how efficiency changes when punishment is enabled in public goods game (PGG) treatments. However, several papers develop formal models, evolutionary game theory, or review prior theoretical and empirical work.

The set includes:
- **Three papers** that are *exactly* focused on PGG or variants with explicit consideration of peer or third-party punishment and efficiency outcomes (Carpenter & Matthews, 2010; Zhang & Pei, 2022; Lee & Iwasa, 2014).
- **Four papers** with *adjacent* focus: modeling related social dilemmas (e.g., repeated PD, networked games, or cooperative market settings) or considering punishment strategies outside of standard PGG design (Castro & Toro, 2008; Voelkl, 2015; Forges et al., 2016; Madeo & Mocenni, 2021).

There is a stronger representation of **mechanism arguments and qualitative predictions** than parameterized, empirically-calibrated effect sizes. The base tilts toward abstracts of design principles (e.g., graduated punishment, redistributive penalties, network effects) and boundary conditions for efficiency-enhancing sanctions.

# 2) Task Relevance

Task relevance is assessed along three axes:

- **pgg_or_variant**
  - **exact:** Carpenter & Matthews (2010), Zhang & Pei (2022), Lee & Iwasa (2014)
  - **close/adjacent:** Castro & Toro (2008), Voelkl (2015), Forges et al. (2016), Madeo & Mocenni (2021)

  Several papers model the canonical PGG, but others study closely related settings (e.g., repeated PD, social networks, market-style cooperation).

- **punishment_or_sanctions**
  - **exact:** Carpenter & Matthews (2010), Zhang & Pei (2022), Lee & Iwasa (2014), Voelkl (2015)
  - **adjacent:** Castro & Toro (2008), Forges et al. (2016)
  - **weak:** Madeo & Mocenni (2021) (no explicit punishment)

  The majority of the base discusses models with explicit punishment or sanctions, with a focus on peer or third-party mechanisms. Some only reference punishment in boundary arguments without direct modeling.

- **efficiency_or_related_payoff_outcome**
  - **exact:** Carpenter & Matthews (2010), Lee & Iwasa (2014), Voelkl (2015), Forges et al. (2016), Madeo & Mocenni (2021), Castro & Toro (2008)
  - **close:** Zhang & Pei (2022) (review-based; emphasizes payoff effects but does not report new estimates)
  - The majority of papers focus primarily on **group average payoff, welfare, or surplus** (direct proxies for efficiency), though some mix in cooperation rate or similar behavioral variables.

**Summary:** The literature is **strong in theoretical coverage** of PGG or related games, explicit punishment, and efficiency outcomes, but provides **little direct empirical evidence** for parameterized prediction. Some coverage is indirect or abstract, particularly regarding implementation details or empirical effect magnitudes.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:** Most papers directly analyze **group efficiency** (total or average payoff relative to the cooperative optimum), focusing on the impact of punishment regimes (Carpenter & Matthews, 2010; Lee & Iwasa, 2014; Voelkl, 2015). These outcomes are the most relevant for the prediction task.
    - Examples: average group payoff, efficiency at equilibrium, welfare, surplus.
- **Non-payoff behavioral outcomes:** Multiple papers discuss **cooperation rates, contribution rates, norm compliance**, and the prevalence of free-riding. These are causally and conceptually related to efficiency, but are not payoff measures themselves (made explicit in Zhang & Pei, 2022).
- Some papers (e.g., Zhang & Pei, 2022) explicitly distinguish between cooperation gains (higher contribution rates) and possible costs that may offset or outweigh these gains in terms of *net efficiency* due to the burden of costly punishment or antisocial sanctions.

**Interpretive note:** While gains in cooperation rate commonly co-occur with gains in payoff in theory, costly punishment can create situations where group efficiency does not improve (or can even decline) despite increased cooperation.

# 4) Main Findings Relevant To Prediction

- **Punishment can drive high efficiency, contingent on conditions:** Multiple models (Carpenter & Matthews, 2010; Lee & Iwasa, 2014; Voelkl, 2015) broadly argue that when punishment is sufficiently effective (i.e., the magnitude of penalty for defection exceeds the gain from defecting), enabling punishment can transform PGG-like games from low-efficiency, free-rider-dominated outcomes to equilibria close to the cooperative optimum—**provided the baseline prevalence of free-riders is not too high and punishment is not excessively costly**.
- **Cost of punishment can offset efficiency gains:** Review and theoretical arguments (Zhang & Pei, 2022) caution that **the act of punishing is itself costly**, and in peer punishment systems, the net effect on group payoffs is ambiguous. Punishment can increase cooperation rates but may reduce (rather than increase) overall efficiency if the costs of administering punishment are high, second-order free-riding is severe, or antisocial punishment occurs.
- **Structure of punishment matters:** Models find that **graduated punishment** (where sanctions increase in response to greater harm; Lee & Iwasa, 2014) and **redistributive penalties** (where punishment benefits cooperators; Voelkl, 2015) are more likely to maximize group efficiency than uniform, severe, or arbitrary punishment regimes.
- **Boundary conditions and initial state matter:** The effect of enabling punishment depends upon **initial levels of cooperation/free-riding** (Carpenter & Matthews, 2010). If baseline (control) efficiency is already very low due to pervasive free-riding, the introduction of peer punishment may not be able to rescue the system—punishment needs a sufficient foothold to sustain high-efficiency equilibria.
- **Voluntary participation and self-regulation offer alternatives:** Papers modeling the presence of voluntary participation ("loners"; Castro & Toro, 2008) or endogenous self-regulation (Madeo & Mocenni, 2021) show that high efficiency can sometimes be achieved without formal punishment, especially in repeated games. These results suggest that the effect size of adding punishment may depend on whether alternative mechanisms are available in the design.

**Disagreement/Ambiguity:** While most models predict positive effects of enabling punishment under theoretically favorable conditions, **the review by Zhang & Pei (2022) highlights empirical cases where costly peer punishment fails to deliver net gains in efficiency, and may sometimes reduce it**.

# 5) Prediction Guidance

- **Qualitative expectation:** Enabling peer punishment in public-goods or PGG-like environments is *predicted by theory* to, in general, increase efficiency under certain conditions:
    - Punishment is strong enough and not prohibitively costly,
    - The control baseline is not dominated by free-riders,
    - The system allows for graduated or context-sensitive sanctions.

- **Be cautious:** In settings where **punishment is expensive relative to its effectiveness**, or where **punishment leads to antisocial use or second-order free-riding**, efficiency may increase only modestly, not at all, or may even decline (Zhang & Pei, 2022).

- **Parameter and context dependence:** Theoretical models suggest that *game design parameters* (such as group size, MPCR, contribution mechanism, and punishment cost/effect) can be strong moderators of the effect of punishment on efficiency. For example:
    - **High MPCR and small group size** favor effectiveness of punishment (Carpenter & Matthews, 2010).
    - **Graduated punishment** more reliably increases efficiency than severe or one-size-fits-all penalties (Lee & Iwasa, 2014).
    - **Redistribution of penalty proceeds** may further enhance efficiency (Voelkl, 2015).

- **Limitation:** The absence of new empirical data in this set means predictions must be qualitative and mechanistic, not quantitative.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions (discussion or modeling in multiple papers):**
- `player_count`: Explicit in Carpenter & Matthews (2010); Voelkl (2015); Castro & Toro (2008); Forges et al. (2016). Theory emphasizes importance of small group size and implications for punishment dynamics.
- `num_rounds`: Modeled/discussed in Carpenter & Matthews (2010); Castro & Toro (2008); Forges et al. (2016). Repetition is noted as a facilitator of cooperation, but not as a moderator of treatment efficiency in the presence of punishment in all models.
- `all_or_nothing`: Modeled in some form in Carpenter & Matthews (2010); Voelkl (2015); Madeo & Mocenni (2021).
- `mpcr`: Modeled directly in Carpenter & Matthews (2010); Castro & Toro (2008). High MPCR generally supports more positive effects of punishment.
- `punishment_cost`, `punishment_tech`: Central in several models (Carpenter & Matthews, 2010; Voelkl, 2015; Lee & Iwasa, 2014).

**Indirectly informed or contextually discussed:**
- `reward_exists`: Mentioned in Voelkl (2015); Zhang & Pei (2022), but not systematically modeled as a treatment dimension.
- `show_n_rounds`, `show_other_summaries`: Contextually discussed (Castro & Toro, 2008), but no strong predictions about their impact on efficiency.

**Rarely or not addressed:**
- `chat`, `default_contrib`, `reward_cost`, `reward_tech`, `show_punishment_id`: **Barely discussed or only referenced in passing**. No direct theoretical or empirical claims about their effect on efficiency or the impact of enabling punishment.

**Summary:** The literature gives the **strongest guidance on punishment-related dimensions** (cost, magnitude, technology), **group/game structure** (player_count, num_rounds, MPCR), and **contribution mechanisms**; **reward, chat, identification, and interface design** are largely unaddressed.

# 7) Important Limitations

- **No new empirical effect sizes:** All insights are from **theoretical or review papers**, not direct experimental evidence; thus, predicted efficiency changes are **not quantitatively specified** and may not generalize outside stylized models.
- **Abstract models dominate:** Where models map closely to canonical PGG (Carpenter & Matthews, 2010), their parameters are specific and may not span the full range of experimental/game-theoretic designs relevant to downstream prediction.
- **Parameter dependence but not full dimensional coverage:** Only some game design parameters receive focused analysis; others (e.g., chat, reward interface, identification, experimental transparency) are **underrepresented or missing**.
- **Ambiguity regarding magnitude and universality of effects:** The **extent and sign of payoff-based effects of punishment are ambiguous** in some reviews, especially regarding costly peer punishment (Zhang & Pei, 2022).
- **No direct test of interaction effects:** There is little discussion of how multiple design dimensions interact (e.g., joint effects of punishment and reward, or of punishment and default framing) to determine treatment efficiency.
- **Assumption-heavy modeling:** Many theoretical papers rest on strong rationality/evolutionary/steady-state assumptions that may not map directly to human behavior in experimental PGGs.

---

**In summary:**  
The literature provides **strong theoretical support** for the claim that enabling (especially effective, graduated) punishment in PGG-like environments usually increases group efficiency, but it highlights crucial caveats: the effect is highly sensitive to punishment cost, baseline cooperation, and implementation details. Due to the absence of new empirical estimates and limited coverage of some design dimensions, **predictions should be cautious and explicitly account for the design parameters available in the theory**. Predictions for game designs that diverge from the theoretical models or rely on unmodeled dimensions are **more speculative**.
