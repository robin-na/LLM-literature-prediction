# 1) Evidence Base

The paper set comprises five sources: two empirical/experimental papers (one direct lab experiment, one review of empirical findings) and three theory or review papers. The empirical content is narrowly focused, with only Grechenig et al. (2010) providing direct experimental evidence related to the prediction task. Kraak (2011) reviews and synthesizes existing empirical findings within a theoretical analysis. The remaining three are purely theoretical or conceptual discussions. The selection is moderately broad in conceptual scope (public goods, trust, cooperation, evolutionary models, institutional context), but direct empirical evidence speaking to efficiency effects of punishment in PGGs is limited. Most papers draw on, reference, or analogize to PGGs, but only Grechenig et al. (2010) and Kraak (2011) report or summarize payoff-based outcomes in actual or modeled PGG environments.
  
# 2) Task Relevance

**pgg_or_variant:**  
- **exact:** Grechenig et al. (2010), Kraak (2011)  
- **close:** Raihani & Aitken (2011)  
- **adjacent:** Bicchieri et al. (2004), Dugatkin (2002)

**punishment_or_sanctions:**  
- **exact:** Grechenig et al. (2010), Kraak (2011)  
- **close:** Raihani & Aitken (2011)  
- **adjacent:** Bicchieri et al. (2004), Dugatkin (2002)

**efficiency_or_related_payoff_outcome:**  
- **exact:** Grechenig et al. (2010), Bicchieri et al. (2004)  
- **close:** Kraak (2011)  
- **adjacent:** Raihani & Aitken (2011), Dugatkin (2002)

**Summary:**  
Task relevance is strongest in Grechenig et al. (2010) and Kraak (2011), which address PGGs, punishment, and efficiency in a directly relevant way. The other papers are closer to mechanism arguments or analogies and do not report experimental findings within public-goods-game environments for efficiency outcomes.

# 3) Outcomes Measured In The Literature

**Payoff-Related Outcomes:**  
- **Directly measured or discussed:**  
    - **Efficiency (group total payoff as a fraction of maximum possible):** Grechenig et al. (2010), Bicchieri et al. (2004)  
    - **Group payoff / welfare:** Kraak (2011) (review/synthesis, not primary data)  
    - **Average payoffs:** Bicchieri et al. (2004) (trust games)  
- **Indirect or theoretical:**  
    - **Welfare or surplus from cooperation:** Theory (Kraak, Bicchieri, Dugatkin)

**Non-Payoff Behavioral Outcomes:**  
- **Cooperation / contribution rate:** All papers refer to this, especially Kraak (2011), Raihani & Aitken (2011), Dugatkin (2002)  
- **Norm compliance, antisocial punishment, targeted punishment:** Grechenig et al. (2010), Kraak (2011)  
- **Mechanistic discussion (reciprocity, trust):** Bicchieri et al. (2004), Dugatkin (2002)

**Distinction:**  
The empirical evidence for prediction is primarily in efficiency and group payoff terms only in a minority of papers. Many findings emphasize non-payoff behavioral metrics, which signal but do not guarantee changes in efficiency.

# 4) Main Findings Relevant To Prediction

- **Punishment can increase efficiency in public goods games if monitoring is accurate.**  
    - Grechenig et al. (2010) find that allowing peer punishment increases efficiency and cooperation only when subjects have accurate information about others’ contributions. When information is noisy, enabling punishment can *reduce* efficiency, as misdirected or antisocial punishment becomes common.
  
- **The benefit of punishment depends on information structure and context.**  
    - Peer-driven punishment, combined with transparency and communication, tends to improve group payoff and efficiency according to Kraak (2011), especially when mechanisms such as reputation-building are enabled and institutional legitimacy is high.
    - Externally imposed or non-peer-driven sanctions can undermine cooperation by harming intrinsic motivation.

- **Positive payoff effects are most robust when punishment supports already-existing cooperation.**  
    - Raihani & Aitken (2011) argue that punishment is most effective at maintaining, rather than initiating, cooperation, while rewards may be more helpful early on.

- **Repeated interactions and opportunity for reciprocation (not explicit punishment) can promote efficiency.**  
    - Bicchieri et al. (2004) show theoretically that longer games with repeated rounds allow for conditional (“punishing”) strategies to stabilize high-efficiency, cooperative outcomes, even without direct material punishment mechanisms.
    - Threshold effects: Efficiency only increases when games are repeated for several rounds; one-shot or low-round games sustain low efficiency.

- **In evolutionary/animal analogs, punishment stabilizes cooperation but outcome quantification is lacking.**  
    - Dugatkin (2002) highlights theoretical support for the stabilizing role of punishment but offers no quantitative efficiency results in PGG settings.

# 5) Prediction Guidance

- **Direct relevance for payoff-based efficiency prediction with peer punishment comes mainly from Grechenig et al. (2010):**
    - If the control game (no-punishment) has high information accuracy about contributions, enabling punishment is likely to increase efficiency.
    - If the design includes noise or uncertainty (e.g. imperfect observation of contributions), enabling punishment is likely to reduce efficiency, potentially below the control baseline.
    - Other design features (player number, rounds, etc.) are less causally isolated in their experiment, limiting evidence on their moderating role.
- **Kraak (2011):** For contexts with communication, reputation, and peer-driven punishment (not top-down), enabling punishment is expected to increase group efficiency after initial adjustment costs.
- **Repeated interaction (Bicchieri et al., 2004):** If the number of rounds is very low (e.g. one-shot), even with conditional punishment strategies, efficiency improvements are unlikely. As number of rounds increases, the environment can support beneficial effects of punishment or reciprocal strategies.
- **Other papers (Raihani & Aitken, Dugatkin):** Suggest that mechanisms increasing information availability, communication, and reward in addition to punishment can enable higher efficiency, especially in early or uncertain cooperation phases, but no direct payoff data are reported.

**Key moderators highlighted for prediction:**
- Accuracy of information/monitoring (most crucial for punishment efficacy).
- Existence of communication, reputation, or transparency mechanisms.
- Number of rounds (support for conditional/punishing strategies emerging).
- The nature of the punishment (peer-driven vs. externally imposed).

# 6) Design Dimensions Highlighted Across Papers

**Directly informed:**
- `player_count` — Empirically held constant in Grechenig et al. (2010); considered important in Kraak (2011) and Bicchieri et al. (2004).
- `num_rounds` — Critical theoretical moderator (Bicchieri et al., 2004); empirically present but not manipulated in Grechenig et al. (2010).
- `mpcr` (Marginal per-capita return) — Included in the design of several papers (Grechenig et al., Kraak, Bicchieri), but specific moderation of punishment efficacy is not empirically isolated.
- `punishment_cost` — Directly included in all PGG/variant empirical and theoretical models.
- `chat` / `communication` — Discussed by Kraak (2011) and Raihani & Aitken (2011) as mechanisms that enhance positive effects of punishment.
- `all_or_nothing` — Included as a feature in the models, but not directly analyzed as a moderator.
- `show_n_rounds` — Included as a procedural feature in Bicchieri et al. (2004), but not central for efficiency prediction.

**Indirectly informed:**
- `show_other_summaries`, `show_punishment_id` — Inferred via discussions of information accuracy and transparency but not separately manipulated.
- `reward_exists`, `reward_cost`, `reward_tech` — Discussed as relevant mechanisms (Raihani & Aitken), but not empirically isolated or linked directly to efficiency.

**Contextually discussed or missing:**
- `default_contrib` — Not directly discussed.
- `punishment_tech`, `punishment_magnitude` — Technology for punishment assumed but details not varied or isolated as moderators.
- Any detailed interface/timing/visibility components beyond presence/absence of information.
  
**Crucially, the most robust, empirically validated moderator emerging from this set is the accuracy and visibility of information about others’ contributions (relates to but not exactly captured by the 14 listed prediction dimensions).**

# 7) Important Limitations

- **Only one paper (Grechenig et al., 2010) provides direct, empirical, and quantitative evidence about the effect of enabling punishment on efficiency in repeated PGGs.**
- **Most other sources provide theoretical or review-based arguments rather than new efficiency data.**
- **No paper experimentally manipulates all 14 prediction dimensions or establishes their separate effects on efficiency.**  
  - Most evidence on `chat`, `reward_exists`, `show_other_summaries`, and visibility of identity is indirect, via mechanism arguments.
- **The identification of accurate information/monitoring as the key moderator (Grechenig et al., 2010) depends on a specific implementation. Its correspondence to design dimensions (`show_other_summaries`, observation technology) is not fully spelled out.**
- **Payoff-based claims are sometimes inferred from increases in cooperation, which does not always translate into higher efficiency (especially if punishment is costly or misapplied, as under noise).**
- **Little evidence is provided about the impact of reward coexistence, punishment magnitude/cost ratio, or default contribution settings on efficiency outcomes.**
- **Generalizability to PGG-like environments with very different numbers of players, round structures, or with complex sanction/reward technologies is untested in this literature set.**
- **Potential negative effects of punishment (e.g., crowding-out of intrinsic motivation, antisocial punishment) are noted in reviews but not directly quantified.**

---

**Summary:**  
The literature most directly supports the importance of accurate contribution information for the efficacy of peer punishment in improving efficiency in public goods games—this is the best-supported moderator for predictions. Other prediction dimensions are only weakly or indirectly covered. There is insufficient empirical evidence within this set to calibrate or extend predictions to novel combinations of player count, rounds, or punishment/reward technologies not explicitly examined. Additional empirical research would be necessary to close these gaps.
