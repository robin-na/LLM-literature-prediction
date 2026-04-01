# 1) Evidence Base

This paper set provides a moderate-to-broad coverage of public-goods-game-like environments, with an emphasis on both empirical (mainly lab experimental) and theoretical (game-theoretic and simulation) research. Of the 20 papers, several offer **exact empirical tests** of punishment effects on efficiency in public goods games (e.g., Carpenter et al., 2012), while others use **model-based theoretical approaches** to explore long-run or strategic outcomes (e.g., Bowles & Gintis, 2004; Deng et al., 2012). There is a balance between exactly relevant studies and models, closely related dyadic or bargaining games, and more peripheral or adjacent analyses, including papers that focus on behavioral or norm-enforcement mechanisms without reporting efficiency.

Overall, the literature covers a range of designs (e.g., variations in group size, rounds, network structure, punishment/reward mechanics), but the **empirical evidence is strongest for small-group, repeated, lab-environment games**. Theoretical contributions extend these findings to larger and more varied contexts, but there is notable heterogeneity in the modeling assumptions and environments. Direct quantitative head-to-head comparisons of control versus punishment-enabled efficiency, across the 14 prediction dimensions, remain sparse relative to the breadth of procedural variations and contexts explored.

# 2) Task Relevance

**pgg_or_variant:**  
- **exact:** Several papers analyze standard public goods games or their close variants (e.g., Carpenter et al., 2012; Bowles & Gintis, 2004; Fischer & Nicklisch, 2007).
- **close/adjacent:** Some model closely related social dilemmas (n-player Prisoner's Dilemma or resource-sharing with opt-out strategies)—valuable for theoretical generalization but not always directly matching PGG structure (e.g., Castro & Toro, 2008; Kurokawa et al., 2010).
- **weak/none:** A few focus on sequential bargaining, principal-agent reporting, or abstract norm-enforcement, only loosely related to PGGs in strategic structure.

**punishment_or_sanctions:**  
- **exact:** About half the set includes explicit peer punishment or related sanctioning mechanisms (e.g., Carpenter et al., 2012; Bowles & Gintis, 2004; Kendal et al., 2006).
- **adjacent:** Others include punishments conceptually (e.g., as contingent refusal to cooperate) or manipulate related variables like reputation, but do not implement direct costly peer punishment (e.g., Kurokawa et al., 2010; Brosig et al., 2004).
- **none:** Some (e.g., Bourrat et al., 2011) only discuss non-economic norm enforcement or have no punishment treatment.

**efficiency_or_related_payoff_outcome:**  
- **exact:** Several studies (both empirical and theoretical) measure total group payoff, efficiency, welfare, or closely aligned metrics (e.g., Carpenter et al., 2012; Deng et al., 2012).
- **adjacent:** Others, while examining cooperation or norm compliance, do not report direct group payoff or efficiency metrics, making their evidence only indirectly useful (e.g., Davis & Holt, 1999; Güth et al., 2007).
- **none:** A small subset reports only psychological/behavioral measures.

**Summary:**  
The literature **directly addresses the prediction task in several papers** with exact or very close evidence. However, there is a notable contingent (especially among the empirical work) that focuses more on behavioral than payoff outcomes, or on adjacent paradigms, limiting the overall direct guidance available for the prediction task as outlined.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (efficiency, welfare, total group payoff):**
  - **Directly measured** in several empirical and theoretical studies (e.g., Carpenter et al., 2012; Deng et al., 2012; Bowles & Gintis, 2004; Kendal et al., 2006).
  - **Operationalization:** Efficiency is generally defined as the group’s total payoff relative to full-cooperation optimum. Others use ‘welfare’, ‘surplus’, or explicit earning tables.
  - **Observed variation:** Some report that punishment improves efficiency, while others find it neutral or harmful, due to punishment costs offsetting cooperation gains (e.g., Abbink et al., 2004).
- **Non-payoff behavioral outcomes:**
  - **Contribution rate, cooperation rate, frequency of punishment or rewarding, norm compliance, honesty/budget slack** (e.g., Davis & Holt, 1999; Chen, 2012).
  - These outcomes are often used to infer underlying mechanisms but do **not directly translate to payoff-based measures**.
  - Some studies blur these categories by inferring that increased cooperation “should” mean higher efficiency, but do not provide payoff data to confirm.

# 4) Main Findings Relevant To Prediction

- **Punishment can increase efficiency**, but only under specific structural and parametric conditions:
    - **Network structure matters:** In highly connected networks, punishment is more likely to increase efficiency; in sparsely connected or directed networks, punishment costs may overwhelm cooperation gains, reducing efficiency (Carpenter et al., 2012).
    - **Third-party/Metanorm punishment:** Theory papers consistently find that enforcement by third parties or through reward of punishers facilitates high-efficiency equilibria, but only if costs are manageable and initial free-riding is not too widespread (Carpenter & Matthews, 2010; Kendal et al., 2006).
      - **Rare but severe punishment** can be especially efficiency-enhancing, keeping overall costs low (Deng et al., 2012).
    - **Costs of punishment:** High punishment costs often drop efficiency below control, even as norm compliance rises. Some simulation results indicate that punishment reduces group efficiency unless sanctioned behaviors produce additional surplus (Jaffe, 2004; Abbink et al., 2004).
    - **Group size:** Theory indicates that severe, concerted punishment is more effective in larger groups, while in small groups, marginal returns may be lower or costs may erode gains (Deng et al., 2012).
    - **Game parameters held constant:** Some empirical studies control MPCR, group size, rounds, focusing on isolating punishment’s effect, but this restricts external inference across varied parameterizations.
- **Empirical findings are mixed:**
    - Some experiments show **punishment increases efficiency**, others show **neutral or negative effects** when costs mount (Carpenter et al., 2012; Abbink et al., 2004).
    - Several adjacent studies find increased cooperation, not always translating to higher group payoff.

# 5) Prediction Guidance

- **Prediction of treatment efficiency from control efficiency and design:**
    - **Punishment’s effect is contingent:** The effect of enabling peer punishment depends on both baseline efficiency (with punishment off) and design dimensions such as punishment cost, effectiveness (magnitude), and network connectedness.
    - **Control efficiency as a baseline:** If the control game already achieves high efficiency (via communication, reputation, or other mechanisms), enabling punishment might add little or might even reduce efficiency due to costly punitive actions (Abbink et al., 2004).
    - **Network architecture:** Detailed knowledge of the punishment/monitoring network (who can punish whom) is essential. Predictions must account for the possibility of over-punishment or inefficiency in poorly structured networks (Carpenter et al., 2012).
    - **Third-party and metanorm structures:** Prediction models should be sensitive to the presence/strength of third-party punishment and reward for punishers—these can raise the likelihood of high-efficiency outcomes, especially if initial free-riding is not pervasive (Carpenter & Matthews, 2010; Kendal et al., 2006).
    - **Punishment severity and frequency:** Environments with rare but intense (severe) punishment, especially if concerted/shared, can yield more substantial efficiency gains per unit cost, especially in larger groups (Deng et al., 2012).
    - **Cautions:** High punishment frequency at intermediate severity often **reduces efficiency** due to accumulating costs; only at extremes (very high deterrence or rare use) does efficiency approach optimum (Abbink et al., 2004).
    - **Dimension unsupported:** Several behavioral findings (e.g., contribution increases, trustworthiness, budget honesty) are **not directly informative** for payoff/efficiency unless payoff data confirm translation.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions:**
- `player_count`: Multiple theoretical and empirical papers (e.g., Deng et al., 2012; Carpenter et al., 2012).
- `num_rounds`: Repeated games are common, but with limited variation in rounds tested.
- `mpcr`: Explicitly manipulated or modeled in several studies.
- `punishment_cost` and `punishment_tech`: Directly manipulated; identified as important moderators of efficiency (Carpenter et al., 2012; Bowles & Gintis, 2004).
- `network structure` (relates to who can punish whom): Directly shown to be a decisive moderator.
- `all_or_nothing`: Present in models/theory, though less pivotal empirically.
- `reward_exists` and `reward_cost`: Addressed, especially in models comparing reward and punishment (Kendal et al., 2006; Chen, 2012).
- `chat`: Some empirical work addresses communication as a moderator, though findings on its interaction with punishment and efficiency are more indirect (Brosig et al., 2004).
- `show_n_rounds`, `show_other_summaries`: Occasionally manipulated, with some evidence of weak effects.

**Indirectly, contextually, or sparsely informed:**
- `default_contrib`: Framing effects (opt-in/opt-out) rarely directly reported in relation to efficiency or punishment impact.
- `show_punishment_id`: Identity visibility is occasionally manipulated (Abbink et al., 2004), usually affecting more behavioral than efficiency outcomes.
- `reward_tech`, `reward_magnitude`: Sometimes modeled but more rarely tied to efficiency.

**Effectively missing:**
- Several dimensions (especially those about payoff feedback, individual framing, or nuanced cueing) are only contextually addressed or absent from analysis. No comprehensive study jointly manipulates all 14 prediction dimensions.

# 7) Important Limitations

- **Insufficient direct coverage for all dimensions:** Few papers manipulate or report all relevant game design features, limiting ability to estimate cross-dimensional effects or interactions reliably.
- **Mixed empirical findings:** There is **no consensus** on whether punishment reliably increases efficiency: while some settings produce strong positive results, others show punishment’s cost exceeds its cooperation benefits.
- **Over-reliance on theory for large groups or rare punishment:** Many theoretical findings generalize beyond standard lab parameters, but hinge on strong assumptions (e.g., well-mixed populations, stable metanorms, severe/rare concerted actions).
- **Behavioral outcomes ≠ efficiency:** Many studies use increases in contributions or compliance as proxies for efficiency, but empirical results show that costly punishment can actually **reduce** total payoff—such translations are not reliable without direct measurement.
- **Moderators often under-explored:** Critical features—such as exact punishment/reward mechanics, recognition of punishers, multi-round learning, and communication effects—are not systematically varied across payoff-measured experiments.
- **Baseline (control) efficiency matters:** Where control games already achieve high efficiency through other mechanisms, punishment may have diminished or even negative marginal return.
- **Results may not generalize to all PGG designs:** Most payoff evidence comes from small, fixed groups over a set number of rounds; evidence for one-shot, large-group, or field settings is indirect at best.
- **Context sensitivity:** Papers highlight that subtle differences in design, framing, and implementation produce large shifts in the effect of punishment. Direct transfer of parameter effects from these studies to new environments should be done cautiously.

---

**Summary:**  
**This literature set provides a mix of direct empirical, theoretical, and adjacent evidence on the effects of punishment on efficiency in public-goods-game-like environments. The main guidance is that the impact of punishment on efficiency is highly contingent on game design parameters (notably network structure, punishment cost, and baseline efficiency). Mechanistic arguments and synthetic models support the prediction that peer punishment can improve efficiency when its cost is low, is severe but rare, or is reinforced by metanorms, particularly in well-connected settings. However, empirical studies frequently report neutral or negative efficiency effects due to excessive punishment expenditures, especially as network structure and other moderators are changed. Several key prediction dimensions are only partially or indirectly addressed, and researchers should be cautious in extrapolating quantitative prediction rules from this evidence base.**
