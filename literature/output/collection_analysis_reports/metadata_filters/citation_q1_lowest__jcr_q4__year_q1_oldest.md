# 1) Evidence Base

The paper set consists of three papers: one empirical laboratory experiment directly focused on public goods game (PGG) institutional design (Fischer & Nicklisch, 2007), and two theoretical papers addressing mechanisms for sustaining cooperation in repeated social dilemmas under punishment or enforcement regimes (Annen, 2011; Jones, 1999). The set is somewhat broad in mechanism coverage—spanning voting, community enforcement, and punishment strategies—but relatively narrow in empirical coverage of punishment effects in PGGs, with explicit laboratory punishment conditions absent. Empirical studies are underrepresented compared to theory; only one paper provides direct behavioral data, and that only for voting rules without explicit punishment. All papers consider standard social dilemma structures, but only one paper is an exact match for standard PGG settings. The remaining two focus on adjacent environments (repeated matching or Prisoner’s Dilemma), offering theoretical arguments about the effect of punishment on cooperation and, indirectly, on efficiency.

# 2) Task Relevance

**pgg_or_variant:**  
- *Fischer & Nicklisch (2007):* exact relevance. Directly studies public good games and reports efficiency outcomes as a function of voting mechanisms.
- *Annen (2011):* close/adjacent relevance. Studies repeated matching games with private monitoring, a structure similar to but not precisely the standard PGG.
- *Jones (1999):* adjacent relevance. Focuses on repeated Prisoners’ Dilemmas, structurally analogous but not identical to PGGs.

**punishment_or_sanctions:**  
- *Fischer & Nicklisch (2007):* adjacent. Explores institutional safeguards (voting) rather than explicit punishment mechanisms.
- *Annen (2011):* exact. Directly theorizes about community enforcement and personal punishment mechanisms.
- *Jones (1999):* exact. Analyzes punishment (via trigger strategies) in repeated dilemmas.

**efficiency_or_related_payoff_outcome:**  
- *Fischer & Nicklisch (2007):* exact. Measures efficiency and profits across conditions.
- *Annen (2011):* exact. Theoretical predictions concern efficiency and group welfare.
- *Jones (1999):* adjacent. Theoretical discussion is in terms of equilibrium support for cooperation rather than measured efficiency, but implications pertain to group payoffs.

# 3) Outcomes Measured In The Literature

- **Payoff-Related Outcomes:**  
   - *Fischer & Nicklisch (2007)*: Directly measures efficiency (group payoff relative to full cooperation).
   - *Annen (2011)*: Theoretical focus on ability of punishment regimes to support efficient cooperation (group welfare).
   - *Jones (1999)*: Theoretical focus on conditions for cooperative equilibria, which if achieved, maximize group payoff/efficiency.

- **Non-Payoff Behavioral Outcomes:**  
   - *Fischer & Nicklisch (2007):* Also measures contribution rates, but these are subordinate to efficiency in the findings.
   - *Annen (2011) & Jones (1999):* Both primarily use behavioral logic/theoretical models to infer potential for high payoff, not reporting specific behavioral rates.

# 4) Main Findings Relevant To Prediction

**Empirical findings:**
- *Voting/safeguards vs. automatic provision:* Institutional safeguards (such as unanimity voting) can increase contributions but may result in lower group efficiency due to higher likelihood of failed provision, not directly due to punishment (Fischer & Nicklisch, 2007).
- *No direct empirical evidence on peer punishment's efficiency impact in PGGs* is present in this set.

**Theoretical findings:**
- *Community enforcement with punishment* can support efficient cooperation in groups, particularly with exogenous (truthful) experience-sharing and in larger groups (Annen, 2011).
- Endogenous (strategic) experience-sharing requires supplemental personal punishment; this reduces community enforcement’s efficacy and increases the threshold for sustaining cooperation.
- *Punishment duration/severity* (trigger strategies) is critical in sustaining cooperation in repeated dilemmas. Longer or more severe punishment makes it easier to support cooperative equilibria—hence, potentially higher efficiency—if the probability of future interaction isn’t too low (Jones, 1999).
- *Short horizons or low continuation probability* (quasifinite games) negate the effectiveness of punishment for sustaining efficient cooperation.
- In all, **punishment mechanisms are generally predicted to increase efficiency, conditional on sufficient future interaction probability and, especially, in larger or well-connected groups**.

# 5) Prediction Guidance

- The literature suggests that **peer punishment, if enabled in a repeated public-goods-game-like environment, has the potential to improve group efficiency over baseline (control) efficiency**, however:
    - *The magnitude of this improvement is conditional:*  
        - **Group size** matters—the effect is predicted to be more positive in larger groups (Annen, 2011).
        - **Game horizon/continuation probability**—if it is short/low, punishment is predicted to have no effect due to lack of deterrence (Jones, 1999).
        - **Quality of experience/reporting mechanisms**—exogenous/truthful experience-sharing enhances punishment’s positive effect; endogenous/strategic sharing requires penalties that may dilute welfare gains (Annen, 2011).
        - *Voting institutional safeguards* (not punishment) may also increase contributions with possible reduction in efficiency—hinting that mechanism design effects can go in different directions depending on their coordination properties (Fischer & Nicklisch, 2007).
- Because explicit empirical evidence on peer punishment's quantitative effect on PGG efficiency is missing, **predictions from this set should emphasize theoretical considerations and highlight conditionality on group size, time horizon, and information sharing structures**.
- Control game efficiency remains an important baseline. Where control games are already efficient (due to institutional safeguards or intrinsic cooperation), the marginal effect of enabling punishment may be attenuated or ambiguous.

# 6) Design Dimensions Highlighted Across Papers

- **Directly informed dimensions:**
    - **player_count**: All papers discuss group size consequences, theoretically or empirically.
    - **num_rounds**: Covered in empirical and theoretical treatments; links to game horizon and cooperation sustainability.
    - **all_or_nothing**: Present in all papers; relates to contribution structure.
    - **mpcr**: Included in empirical design and theory; directly affects incentives.
    - **show_other_summaries**: Mentioned in two papers as relevant to information availability.
    - **show_n_rounds**: Present in empirical study (affecting player expectations).
- **Indirect/contextual coverage:**  
    - **punishment_cost**: Implicit in theoretical discussions of punishment, but not parameterized or experimentally varied.
    - **punishment_tech**: Discussed as "community enforcement" or "trigger strategies," not in fine-grained implementation terms.
    - **default_contrib**: Not covered.
    - **chat**, **show_punishment_id**, **reward_exists**, **reward_cost**, **reward_tech**: Only contextually covered or missing.
- **Effectively missing for prediction:**  
    - Dimensions relating to chat, explicit reward mechanisms/costs, punishment/reward technology specifics, and default contribution framing are not empirically addressed.

# 7) Important Limitations

- **Lack of direct empirical evidence for peer punishment in PGGs.** The key downstream prediction—how enabling peer punishment affects efficiency given control efficiency and design parameters—is addressed primarily by theory and only in adjacent environments.
- **Theories do not provide quantitative predictions.** Existing theory offers only logical or equilibrium conditions for efficiency changes, not numerical estimates or parameterized effect sizes.
- **Relevant design dimensions are incompletely covered.** Information on several design dimensions central to prediction (punishment cost, reward design, chat, visibility of punishment, contribution framing) is sparse or missing.
- **Population and matching structures differ from prediction setting.** Some findings rest on repeated matching rather than fixed groups, or on indirect monitoring; translation to standard PGG may not be exact.
- **Mechanism heterogeneity.** Institutional safeguards (voting) and peer punishment may interact, but this set studies these separately; no papers examine combined or hybrid effects.
- **Reporting bias toward positive mechanism effects.** Theoretical results emphasize possibilities for supporting high efficiency; real-world behavioral deviations and failures may be underrepresented.
- **Ambiguity in mapping theory to practice.** While theoretical results justify when punishment can improve efficiency, empirical generalizability is uncertain—especially where strategic reporting or retaliation complicates equilibrium predictions.

**In summary:**  
This literature set provides partial, mostly theoretical guidance for predicting the efficiency impact of enabling peer punishment in public-good-game-like environments. The implications are clearer for large groups, longer games, and transparent information structures, but empirical quantification for the baseline prediction task remains limited.
