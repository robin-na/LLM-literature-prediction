# 1) Evidence Base

The paper set consists of three papers, representing a mix of experimental empirical studies (Sadowski et al., 2015; Schroeder et al., 2014) and one theory paper (Toupo et al., 2014). The evidence base is somewhat narrow for the prediction task, as only one paper (Schroeder et al., 2014) includes explicit punishment manipulation—though not in a strict public-goods game (PGG) context, and without direct measurement of group efficiency. The other empirical paper focuses on communication and leadership in common-pool resource (CPR) dilemmas without punishment, while the theory paper addresses cooperation dynamics in the repeated Prisoner's Dilemma without including punishment or efficiency analysis. Overall, empirical evidence concerning the effect of peer punishment on efficiency in PGG-like environments is limited in this set.

# 2) Task Relevance

**pgg_or_variant**  
- **Sadowski et al. (2015):** `close` – Complex multi-group CPR game (related structure, not canonical PGG).
- **Schroeder et al. (2014):** `adjacent` – Third-party punishment game, not a standard PGG.
- **Toupo et al. (2014):** `adjacent` – Theoretical analysis of repeated Prisoner's Dilemma, not PGG or CPR.

**punishment_or_sanctions**  
- **Sadowski et al. (2015):** `weak` – No punishment or rewards in design; focus is on alternatives to sanctions.
- **Schroeder et al. (2014):** `exact` – Manipulates punishment via third-party punishment; main focus is on the functioning of punishment.
- **Toupo et al. (2014):** `none` – No punishment or rewards included.

**efficiency_or_related_payoff_outcome**  
- **Sadowski et al. (2015):** `exact` – Efficiency and total payoff are primary outcomes.
- **Schroeder et al. (2014):** `adjacent` – Non-payoff behavioral outcomes are primary; payoff is only contextually mentioned.
- **Toupo et al. (2014):** `adjacent` – Focuses on cooperation rates and evolutionary dynamics, not on efficiency or payoff directly.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes:**
- **Sadowski et al. (2015):** Measures group payoff, efficiency, and sustainability of resource extraction—directly aligned with the prediction task’s target outcome.
- **Schroeder et al. (2014):** Mean payoff is measured but not analyzed as a treatment effect; the main focus is on behavioral outcomes.
- **Toupo et al. (2014):** Does not measure payoff or efficiency; the focus is on strategy dynamics and cooperation levels.

**Non-payoff behavioral outcomes:**
- **Sadowski et al. (2015):** Cooperation rates, equitable distribution, leadership behaviors.
- **Schroeder et al. (2014):** Willingness to punish, norm violation, trust, theft rates, expectation of punishment.
- **Toupo et al. (2014):** Cooperation and defection rates, strategy oscillations due to mutation.

# 4) Main Findings Relevant To Prediction

- **Relationship between communication, leadership, and efficiency (Sadowski et al., 2015):** In the absence of punishment, groups can achieve moderate efficiency through open communication and emergent leaders. This suggests that, when chat or robust communication is present, efficiency may already be nontrivial in control, potentially reducing the marginal effect of punishment if it were added.
- **Contextual moderators of punishment (Schroeder et al., 2014):** The willingness to punish norm violations depends on local norms and trust. In environments with high norm violation and low trust, both willingness to punish and the expectation of punishment are reduced, and these factors moderate antisocial behavior. The subjective cost of punishment influences whether individuals are willing to sanction defectors.
- **Ineffectiveness of punishment in some settings (Schroeder et al., 2014):** While expectation of punishment can be manipulated by shifting perceived norms, actual mean payoffs (a proxy for efficiency) are similar across contexts, suggesting that the presence or effectiveness of punishment may be constrained by baseline trust and norm environments rather than by the design feature alone.
- **Theoretical mechanisms for cooperation (Toupo et al., 2014):** Evolutionary dynamics (mutation, strategy diversity) can support sustained cooperation in repeated social dilemmas but are not linked to efficiency or punishment outcomes in this paper set.

# 5) Prediction Guidance

Given the available evidence, direct prediction of efficiency changes due to enabling peer punishment in PGG-like games is only weakly supported:

- **Control (no-punishment) efficiency is context-sensitive.** Communication and leadership can sustain moderate efficiency without punishment (Sadowski et al., 2015), so marginal effects of punishment may be smaller in such settings.
- **Marginal impact of punishment is moderated by trust and local norms.** In environments with low trust and high norm violation, both the propensity to punish and its effectiveness in shifting behavior are reduced (Schroeder et al., 2014). Thus, enabling punishment may not always lead to substantial efficiency gains, even when the infrastructure exists.
- **Punishment cost is a moderator.** Higher subjective or objective punishment costs reduce willingness to punish; thus, expected efficiency gains from enabling punishment should be discounted when punishment is expensive.
- **Payoff effects of punishment are not empirically established in this set.** Where punishment is studied, group payoff does not clearly improve relative to control, especially in settings where norm violation is high (Schroeder et al., 2014).
- **Prediction for efficiency should incorporate control efficiency, presence of communication, punishment cost, and environmental trust and norms,** but the expected effect of punishment enablement is highly uncertain given the evidence provided.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed:**
- **player_count, num_rounds**: Discussed in all empirical studies; inform basic game structure.
- **chat (communication):** Sadowski et al. (2015) discusses its central role in efficiency outcomes, but only in non-punishment games.
- **all_or_nothing:** Present in design details; experimental games use either continuous or all-or-nothing contribution structures.
- **punishment_cost:** Directly manipulated by Schroeder et al. (2014).
- **show_n_rounds:** Addressed in both empirical papers.
- **show_other_summaries:** Only Sadowski et al. (2015).

**Indirect/contextual evidence:**
- **punishment_tech:** Manipulated in Schroeder et al. (2014) (3PP game); informs who can punish.
- **mpcr:** Present only as a design parameter, not as a focus of analysis.
- **default_contrib:** Only contextually referenced in one design (framing).

**Sparse/Effectively missing:**
- **punishment_magnitude, show_punishment_id:** Not explicitly addressed.
- **reward_exists, reward_cost, reward_tech:** Not manipulated or discussed.
- **show_other_summaries, show_punishment_id:** Only one (Sadowski et al., 2015) mentions summary information; identity visibility is not studied.

# 7) Important Limitations

- **Lack of direct empirical evidence for effect of punishment on efficiency:** Only one paper examines punishment (`Schroeder et al., 2014`), and even there, group payoff (efficiency) is not a central outcome or analyzed in relation to punishment enablement.
- **Absence of standard PGGs:** None of the papers employ canonical PGG designs; closest are CPR and third-party punishment games. Theory paper is further removed (Prisoner’s Dilemma).
- **Sparse evidence over many prediction dimensions:** Crucial dimensions such as punishment magnitude, reward mechanics, and player awareness of punishers are largely missing.
- **Behavioral outcomes predominate:** Even when punishment is manipulated, measured effects emphasize norm compliance, trust, and expectations rather than payoffs or efficiency.
- **Potential for contextual moderators:** Communication and leadership, as well as norms and trust, are shown to be important for efficiency and punishment—but the generalizability of these moderators to other environments or parameter values is not established.
- **Ambiguity about marginal effects:** Where both communication and punishment are considered (across papers, not within), there is uncertainty about whether enabling punishment adds to efficiency gains or is redundant when communication/leadership is strong.
- **Limited external validity:** The unique social contexts and experimental manipulations in these studies may not generalize to all PGG-like designs.

**In summary:** The paper set offers only indirect and contextually limited guidance for predicting the effect of peer punishment enablement on efficiency in PGG-like settings across diverse game designs. Empirical coverage of the joint effect of punishment and key design dimensions on group efficiency is notably sparse.
