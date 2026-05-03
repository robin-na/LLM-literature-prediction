# 1) Evidence Base

The paper set consists of five papers, with a mix of empirical (2) and theory (3) studies. The empirical papers use laboratory experiments to study cooperation and payoff outcomes, but only one (Becchetti et al., 2015) is a direct test in a repeated common pool resource/public goods environment. The remaining empirical paper (Liu & Riyanto, 2017) focuses on a coordination (stag hunt) game rather than a classical public goods game. The three theory papers (Spitzer, 2016; Golman, 2016; Beraldo & Sugden, 2016) offer formal models or critical analysis, but do not provide new outcome data. The overall scope of this set is moderately broad in terms of theoretical mechanisms, but narrow and incomplete for direct empirical prediction of punishment effects on efficiency in standard PGGs.

# 2) Task Relevance

**pgg_or_variant**:
- **exact**: Spitzer (2016) – theoretical/critical discussion is directly centered on PGGs.
- **close**: Becchetti et al. (2015) – empirical CPRG, commonly accepted as a close PGG analog.
- **adjacent**: Liu & Riyanto (2017), Golman (2016), Beraldo & Sugden (2016) – work on stag hunt/coordination games or stylized public goods framings.

**punishment_or_sanctions**:
- **exact**: Spitzer (2016), Liu & Riyanto (2017) – both examine punishment mechanisms or their effects.
- **adjacent/none**: Becchetti et al. (2015), Beraldo & Sugden (2016) do **not** involve punishment or sanctions.
- **adjacent**: Golman (2016) discusses punishment as a signaling device, but only theoretically and peripherally.

**efficiency_or_related_payoff_outcome**:
- **exact**: Becchetti et al. (2015), Beraldo & Sugden (2016) – directly report on efficiency, welfare, or payoff.
- **adjacent**: Spitzer (2016), Liu & Riyanto (2017), Golman (2016) – focus mostly on contributions, cooperation, or non-payoff behavior; some suggest implications for efficiency without directly reporting it.

**Summary**: Overall, direct evidence on punishment's effect on efficiency in PGGs is **sparse**: only one theory paper (Spitzer, 2016) combines PGG with punishment, but provides no new data; only one paper (Becchetti et al., 2015) reports on efficiency but does **not** include punishment. Other papers offer indirect mechanisms or evidence from adjacent games. This literature set only partially aligns with the prediction task.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes**: 
    - Efficiency (ratio of realized payoff to max possible), group payoff, total earnings (Becchetti et al., 2015; Beraldo & Sugden, 2016).
    - Liu & Riyanto (2017) infer possible welfare implications from behavioral data, but do not report efficiency or payoffs.
- **Non-payoff behavioral outcomes**:
    - Contribution rate, cooperation rate, norm compliance, conditional cooperation, signaling, punishment/reward actions (Spitzer, 2016; Liu & Riyanto, 2017; Golman, 2016).
    - Most theory papers (and Liu & Riyanto, 2017’s experiment) use behavioral proxies for cooperation or compliance, not efficiency itself.

**Distinction**: Only two papers (Becchetti et al., 2015; Beraldo & Sugden, 2016) provide direct data/theory on efficiency or total payoff; others are limited to behavioral results (contributions, coordination, signaling).

# 4) Main Findings Relevant To Prediction

- **Punishment increases cooperation in adjacent games and with mechanism transparency**: Liu & Riyanto (2017) find that making punishment salient in a stag hunt (centralized punishment) increases mutual cooperation, with implications (but not direct measurement) for group welfare/efficiency. The effect is stronger when the punishment can change game equilibria. No direct efficiency result, and the context is not a standard PGG.
  
- **No evidence for or against punishment’s effect on efficiency in direct PGG experiments**: Spitzer (2016) discusses, theoretically, the sensitivity of punishment effects to the exact mechanism details (cost, strength, institutional choice) and the ambiguity arising from possibility of multiple equilibria. No empirical efficiency data provided.

- **Transparency (without punishment) can *reduce* efficiency**: Becchetti et al. (2015) show that publicly disclosing actions and payoffs decreases efficiency in repeated CPRGs, attributed to increased conformity to (selfish) group behavior.

- **Communication and signaling may modulate punishment use**: Golman (2016) suggests, theoretically, that the opportunity for communication can reduce the need for (costly) punishment by providing an alternative way for participants to signal their intentions. How this translates into group payoff is not addressed empirically.

- **Voluntary participation and payoff structure drive cooperation in absence of punishment**: Beraldo & Sugden (2016) model efficiency resulting from voluntary participation and stochastic payoffs, but do not treat sanctioning; thus, no guidance for punishment is offered.

**No direct empirical results** are available for the impact of peer punishment on efficiency in multi-round PGGs for this set.

# 5) Prediction Guidance

Given the literature’s limitations, only **broad qualitative guidance** can be extracted:

- **Model-specific attention**: The effect of peer punishment on efficiency is highly sensitive to game parameters, especially punishment cost, strength, and mechanism design (Spitzer, 2016). Prediction should weigh these parameters carefully for any input game.
- **No empirical payoff effect to calibrate**: The lack of direct PGG-with-punishment efficiency data means empirical estimation must be deferred or borrowed with caution from adjacent paradigms.
- **Information alone is insufficient**: Monitoring or transparency without punishment can reduce efficiency by promoting negative conformity (Becchetti et al., 2015).
- **Potential for efficiency gains with visible, strong punishment**: If the punishment mechanism is strong enough to shift equilibrium and it is made salient, substantial increases in cooperation (and likely efficiency) can be expected, *as in adjacent games* (Liu & Riyanto, 2017), but the transferability of this to standard PGGs is uncertain.
- **Communication may substitute for punishment use**: Enabling chat/communication could reduce reliance on punishment as a cooperative enforcement tool but the net impact on efficiency is ambiguous (Golman, 2016).
- **Control efficiency is not enough**: Because the literature emphasizes sensitivity to mechanism details and equilibrium selection, knowing the control (no-punishment) efficiency is insufficient by itself to predict the impact of enabling punishment.

# 6) Design Dimensions Highlighted Across Papers

- **Directly informed**:
    - `player_count` (N=4 papers; empirical and theory)
    - `num_rounds` (Empirical, theory; Spitzer, Becchetti, Liu)
    - `mpcr` (Spitzer, Becchetti)
    - `punishment_cost` and `punishment_tech/magnitude` (Spitzer, Liu, Golman)
    - `chat` (Spitzer, Liu, Golman)
    - `all_or_nothing` (Becchetti, Liu, Beraldo)
    - `show_n_rounds`, `show_other_summaries` (Becchetti)

- **Indirectly informed**:
    - `reward_exists`, `reward_cost` (Golman, Liu)
    - `default_contrib` (Contextual in Spitzer, not addressed empirically)

- **Contextually discussed**:
    - `show_punishment_id` (Mechanism salience in Liu)
    - `punishment_tech` details in theory work

- **Effectively missing**:
    - Direct empirical results on: `reward_tech`, `reward_magnitude`, `show_punishment_id` (identity visibility), treatment-control differences in efficiency across all manipulations.

**Punishment design details (cost, magnitude, mechanism transparency)** are recognized as potentially critical, but variation is not empirically tied to efficiency in PGGs in this set.

# 7) Important Limitations

- **Absence of direct empirical evidence**: No paper in this set experimentally quantifies the difference in efficiency between control and punishment treatments in a standard multi-round PGG.
- **Lack of cross-condition comparative data**: No within-study comparison of identical PGG design with and without punishment is present.
- **Generalizability from adjacent games is risky**: Key empirical findings on punishment/institutional effects derive from coordination games (Liu & Riyanto, 2017) or theory; transfer to classic PGGs is speculative.
- **Theory papers highlight complexity and context dependence**: Mechanism effects can reverse or vanish depending on fine-grained parameter changes, subject beliefs, and equilibrium multiplicity (Spitzer, 2016; Golman, 2016).
- **Non-payoff behavioral results are not a substitute for efficiency data**: Most papers discuss cooperation rates or signaling, which may not map cleanly onto group welfare or efficiency.
- **Omission of several dimensions**: Several relevant design aspects (reward specifics, identity salience, public feedback in presence of punishment, etc.) lack any direct evidence in this set.
- **No calibration or quantification of effect sizes**: Predictions of efficiency changes remain qualitative due to the lack of appropriate experimental data bridging the design configurations of interest.

---

**Summary**:  
This literature set provides strong caution that the effect of punishment on efficiency in public-goods-game-like environments is highly context-dependent, and it only weakly substantiates any generalizable positive or negative treatment effect. The design dimensions most likely to matter (especially punishment cost and mechanism salience) are discussed, but not tested empirically for their payoff consequences. For prediction purposes, users must acknowledge the significant empirical gap and attend closely to game parameter details, while treating any quantitative efficiency prediction as highly uncertain with this evidence base.
