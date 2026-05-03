# 1) Evidence Base

This literature base is dominated by **theoretical modeling papers** with a small minority of empirical laboratory studies. Nearly all the theoretical work focuses on evolutionary models, agent-based simulations, or analytical game-theoretic models of public goods games (PGGs) or their close variants, particularly with explicit punishment, exclusion, or reward mechanisms. The paper set is **narrow in terms of empirical laboratory/field evidence** but **broad in theoretical modeling, parameter space, and evolutionary dynamics** for punishment mechanisms in PGGs.

Many studies are in **idealized, often infinite, populations or highly simplified environments** (e.g., spatial grids, well-mixed populations), with only isolated treatments of richer lab or field conditions (e.g., communication/chat or realistic group structure). Where empirical work is present, it is largely **adjacent (non-punishment) PGG lab experiments** or close variants with mechanisms similar to PGGs (e.g., resource dilemmas, trust games).

The literature is **richer for mechanistic insight and qualitative predictions** about the effects of punishment, but **quantitative empirical evidence linking design parameters to actual efficiency outcomes** is sparse. There is a **strong focus on evolutionary stability, cooperation rates, and the conditions for cooperation to arise or persist**, with less emphasis on directly reporting group efficiency as defined for the prediction task.

# 2) Task Relevance

Relevance of this literature was assessed along three key axes: PGG/variant, punishment/sanctions, and efficiency/payoff outcomes.

| Dimension                    | Prevalence/Strength | Typical Relevance Label      |
|------------------------------|---------------------|-----------------------------|
| pgg_or_variant               | High                | exact or close              |
| punishment_or_sanctions      | High                | exact or close (often exclusion/sanctioning acts as punishment)   |
| efficiency_or_related_payoff | Moderate            | exact, close, or adjacent   |

- **PGG or variant:** Most papers are **exactly on continuous or discrete PGGs** or very close variants (resource renewal dilemmas, trust games, etc.). There are also some studies on prisoner's dilemma, donation games, and multiplayer social dilemmas that are **adjacent** to PGGs. The relevance to the prediction task is therefore mostly exact or close.

- **Punishment or sanctions:** Most studies introduce **explicit peer punishment, pool punishment, or exclusion mechanisms**—the fit here is often **exact**, though some use adjacent forms (exclusion, reputation, partner switching).

- **Efficiency or related payoff outcome:** Only a **minority report efficiency or group payoff as a primary outcome**; many focus mainly on **cooperation/contribution rates, frequency of strategies, or prevalence of cooperation**, which are non-payoff behavioral outcomes. When efficiency/payoff is reported, it is often modeled as average group payoff or welfare and sometimes as the efficiency ratio to full cooperation. Thus, **relevance for efficiency is often close or adjacent**, with fewer cases of exact efficiency data.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (efficiency, group payoff, total earnings/welfare):**
  - **Exact or close efficiency measures** appear in several theoretical papers (e.g., Jiao et al., 2020; Huang et al., 2018; Gao et al., 2020; Liu & Chen, 2020; Wang et al., 2021 [alliance study]; Perry et al., 2018; Glover & Kim, 2021).
  - **Most empirical studies and many theoretical works report only indirectly on efficiency,** via group payoff, average earnings, or total surplus.

- **Non-payoff behavioral outcomes (contribution rate, cooperation rate, punishment frequency):**
  - **Dominant outcome in the paper set.** The majority of studies report on **the steady-state or dynamic levels of cooperation, prevalence of punishers/excluders, or frequency of certain strategies**, e.g., (Wang et al., 2019; Zhang et al., 2021; Quan et al., 2018).
  - Even in theoretical work, efficiency is often inferred from prevalence of cooperative states rather than directly calculated.

- **Mixed/other outcomes:**
  - Some models report both **average payoffs and behavioral frequencies** (e.g., Perry et al., 2018; Gao et al., 2021 [group-structured model]).

**Explicit distinction:** While higher cooperation rates generally **imply** higher efficiency in PGGs, the translation can break down when punishment is costly or mechanisms shift costs/welfare in complex ways (e.g., high punishment fine, low MPCR).

# 4) Main Findings Relevant To Prediction

**Key synthesized findings:**

- **Enabling punishment (peer or institutional) robustly increases efficiency when:**
  - The punishment cost is **low to moderate** relative to its effect (Jiao et al., 2020; Gao et al., 2020; Quan et al., 2018).
  - Defectors **cannot cheaply avoid punishment** (Wang et al., 2020—disguise undermines efficiency gain).
  - Corruption or antisocial punishment is controlled (Huang et al., 2018; Liu & Chen, 2020).
  - The structure/protocol allows **graduated or probabilistic punishment** rather than deterministic or strict forms (Jiao et al., 2020; Couto et al., 2020).

- **Punishment's effect on efficiency is context-dependent and can be negative when:**
  - **Punishment costs are high** and fines are not optimally chosen (Jiao et al., 2020; Perry et al., 2018).
  - **Mutual/bilateral punishment/retaliation is possible**, such as in two-sided social dilemmas, where efficiency may fall (Bolton et al., 2018).
  - **Specialized group structure enables collusion among punishers** (Glover & Kim, 2021).
  - Defectors can **escape identification or punishment is misapplied** (Wang et al., 2020; Perry et al., 2018).

- **Variants and moderators:**
  - **Exclusion-based punishment** (ostracism) can be even more effective than costly peer punishment at boosting efficiency (Liu & Chen, 2020).
  - **Communication or chat** amplifies the effectiveness of punishment but isn't sufficient alone without sanctions (Song et al., 2020).
  - **Graduated punishment** (severity increases with the number of defectors) is more effective than strict fixed punishment (Couto et al., 2020).
  - **Population structure and size, MPCR, and number of rounds** all interact to determine when punishment pays off (Gao et al., 2020).

- **Non-payoff versus payoff evidence:**
  - **Most studies find increased cooperation with punishment**; in many models, this is presumed to imply higher group efficiency, but explicit calculations show otherwise when punishment is very costly.

- **Empirical divergence:** The relatively few lab/field studies (Ren & Zheng, 2021; Bolton et al., 2018) show that effects seen in theory can be muted or reversed by **strategic behavior, retaliation, or persistent low cooperation**. Theory models are generally more optimistic about efficiency gains.

# 5) Prediction Guidance

**How this literature should inform prediction of treatment efficiency (punishment enabled):**

- **If the control game (punishment disabled) has low efficiency** (due to high defection), and punishment is enabled with **optimally moderate cost and fine**, and **defectors cannot easily avoid punishment**, **a substantial efficiency gain is expected** (Jiao et al., 2020; Gao et al., 2020; Quan et al., 2018; Liu & Chen, 2020; Huang et al., 2018).

- **The strength of the efficiency boost is mediated by**:
  - **Punishment cost/effectiveness parameters** (stronger, cheaper punishment amplifies the gain; high-cost/weak punishment can reduce or eliminate the gain).
  - **Game parameters**: higher MPCR (synergy/returns), smaller groups, finite rounds, visible contributions, all generally favor positive punishment effects.
  - **Moderators:** probabilistic punishment, the ability for excluders to operate, and communication/chat all push toward better outcomes.
  - **Network and group structure:** spatial or networked populations can change the prevalence of cooperative clusters but don't always translate directly into higher efficiency (Flores et al., 2021; Quan et al., 2018 [spatial]).

- **Negative or negligible effect scenarios:**
  - **Punishment cost is too high:** Net efficiency can drop below control (Perry et al., 2018; Bolton et al., 2018).
  - **Bilateral retaliation/mutual negative feedback:** Predict reduced or unchanged efficiency relative to control if mutual punishment is possible (Bolton et al., 2018).
  - **High disguise/corruption:** Predict limited/no efficiency improvement if defectors can avoid or undermine sanctions (Wang et al., 2020; Huang et al., 2018—corruption).

- **Effect of other design dimensions** (when not missing in the literature) should be interpreted in the context of the above, but with caution when empirical/theoretical coverage is sparse or when only non-payoff outcomes are reported.

# 6) Design Dimensions Highlighted Across Papers

**Dimensions with direct or strong indirect coverage:**

- **player_count**: Explored in most theoretical models; larger groups make cooperation harder and can dull punishment's marginal effect (Gao et al., 2020; Huang et al., 2018).
- **num_rounds**: Present in model parameterizations, but infinite horizon is common in theory; some coverage of finite repeated settings.
- **mpcr (marginal per-capita return)**: A central moderator; higher mpcr increases the effectiveness of punishment in improving efficiency (many sources).
- **punishment_cost** and **punishment_tech** (fine, cost, mechanism): Directly parameterized and explored in nearly all core papers (Jiao et al., 2020; Gao et al., 2020).
- **reward_exists, reward_cost** (in reward papers): Comparatively less, but some papers discuss the interplay of reward and punishment (Jiao et al., 2020; Zhang et al., 2021; Wang et al., 2021).

**Dimensions only contextually discussed or sparse:**

- **chat**: Only mentioned as a moderator in a few theory reviews and empirical papers; not often parametrically varied or directly modeled (Song et al., 2020).
- **all_or_nothing**: Sometimes specified in model parameters (binary vs. continuous), but less frequently the main focus of analysis.
- **default_contrib**: Framing not a primary focus in most theoretical literature.
- **show_n_rounds, show_other_summaries, show_punishment_id**: Rarely varied or parametrically analyzed as endogenous design choices.
- **reward_tech, reward_cost**: Only in papers where dual incentive mechanisms are studied; less coverage than punishment parameters.
- **punishment_tech (type: probabilistic, exclusion, institutional, peer)**: Well covered; the role of mechanism is central in theory models.

**Dimensions effectively missing:**

- Mechanistic context or design variations specific to **information displays, summary statistics, identity revelation**, or **detailed chat protocols** are infrequently addressed or formally linked to outcomes.

# 7) Important Limitations

- **Heavy reliance on theoretical models:** Most findings are derived from model assumptions that may not map straightforwardly onto human laboratory or field behavior.
- **Sparse direct empirical validation:** Very limited laboratory or field evidence for quantitative efficiency changes under different punishment regimes. Most "efficiency" results are model predictions, not measured group outcomes.
- **Dominance of behavioral (not payoff-based) outcomes:** The translation from increased cooperation/contribution to net group efficiency is assumed but not always validated—punishment may raise cooperation but lower efficiency if costs are too high.
- **Simplifying assumptions:** Infinite populations, evolutionary updating, spatial structure, discrete strategies—all may not match real-world or experimental designs.
- **Heterogeneous mechanisms/confounds:** Some papers include exclusion, reputation, or role asymmetry as "punishment," which may differ greatly in cost/effect from standard peer punishment.
- **Missing design dimensions:** Key moderators such as **chat, communication, social visibility, default settings,** and **reward framing** are typically not systematically varied or linked to efficiency for punishment treatment.
- **Limits to generalization:** Most models assume homogeneous agents and static parameters, rarely examining the effect of variability in personality, belief updating, or dynamic feedback.
- **Conflicting or ambiguous findings:** Some papers show punishment will hurt efficiency under high cost or allow collusion, while others predict strong positive effects if implementation is optimized.

---

**Summary:**  
This literature set offers **strong theoretical evidence for positive effects of well-designed punishment on treatment efficiency in PGGs**, but **empirical support and parametric mapping to the full range of design dimensions is limited**. The best-supported prediction is that **enabling peer punishment will increase efficiency relative to control when punishment is not too costly and mechanisms for defector evasion are absent**. The net effect depends critically on **punishment cost, effectiveness, mechanism, group size, and MPCR**, with **probabilistic or graduated forms generally outperforming strict, always-on punishment**. Empirical studies and complex mechanisms (e.g., mutual bilateral retaliation, corruption, collusion) can negate or reverse expected gains. **Direct mapping of most design dimensions to efficiency is incomplete; caution and careful extrapolation are warranted.**
