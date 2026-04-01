# 1) Evidence Base

The paper set features a large number (92) of empirical studies, overwhelmingly laboratory experiments using repeated linear public goods games (PGGs) or close variants (e.g., common pool resource games, threshold public goods, team production tasks, and Prisoner's Dilemma games). The majority are within-subject or between-subject lab experiments using real payoffs and manipulate punishment institutions, with a balance between peer, leader/centralized, and third-party punishment mechanisms. There is a wide variety of parameterizations across studies, including variations in group size, number of rounds, MPCR (Marginal Per Capita Return), punishment/reward cost-to-impact ratios, endowment distributions, and information structures.

Empirical (experimental) findings dominate; a few studies provide mechanism or theory arguments, but almost all are empirically grounded. The evidence base is broad in scope for classic PGG and punishment manipulations, but narrows considerably for more complex or less common game dimensions (e.g., chat, default contributions, identity revelation, and certain punishment/reward technologies). Many studies report both contribution and payoff/efficiency outcomes, though some are behavioral only.

# 2) Task Relevance

**pgg_or_variant**  
- **Exact**: The majority of papers use the linear voluntary contributions mechanism (VCM), matching the standard lab PGG, often with 4–5 players, repeated for 8–30 rounds.
- **Close**: Some studies are common-pool-resource games, threshold (step) PGGs, or repeated Prisoner's Dilemma, which are structurally adjacent.
- **Adjacent/Weak/None**: A minority focus purely on trust games, dictator/ultimatum games, or purely observational/survey data.

**punishment_or_sanctions**  
- **Exact**: Most papers directly manipulate whether punishment is enabled, including variations on peer, centralized, third-party, and institutional punishment mechanisms.
- **Close**: Some use closely related incentive structures (e.g., exclusion/ostracism, non-monetary social sanctions, or rewards as a contrast).
- **Adjacent/Weak/None**: A smaller number study communication, group selection, or reputation mechanisms as substitutes or complements to punishment, or only reference punishment peripherally.

**efficiency_or_related_payoff_outcome**  
- **Exact/Close**: Many studies explicitly report group efficiency, net payoff, total earnings, or similar metrics (e.g., average earnings compared to the maximum possible), though some require calculation from reported data.
- **Adjacent**: Numerous studies report only contributions, cooperation rates, or punishment assignment, from which efficiency must be inferred or is only weakly addressed.
- **Weak/None**: A non-trivial minority focus solely on non-payoff outcomes (e.g., behavioral responses, norm compliance) or are not PGGs.

# 3) Outcomes Measured In The Literature

**Payoff-related outcomes (directly relevant):**
- *Efficiency*, group payoff (often as a fraction of the social optimum), average/total earnings, welfare, surplus, and coins generated.
  - Numerous studies offer explicit efficiency comparisons between control (no-punishment) and punishment-enabled conditions.
- Some papers explicitly compare efficiency across treatments varying in institutional structure, punishment severity/cost, network symmetry, or subject population composition.

**Non-payoff behavioral outcomes (context/adjacent):**
- Contribution rates, cooperation rates, punishment use/frequency, anti-social punishment behavior, norm compliance, strategies, and beliefs about others.
  - Many studies report both contribution and payoff outcomes, allowing for correlation analysis, but some are purely behavioral.
- Some studies focus on the psychological and motivational determinants of punishment or cooperation (emotions, social identity, expectations, etc.).

# 4) Main Findings Relevant To Prediction

## a) **Canonical Result**:  
Enabling costly, targeted peer punishment in standard linear PGGs often **increases both contributions and efficiency** compared to a no-punishment baseline; however, **the magnitude and even sign of efficiency effects are contingent**.

## b) **Key Moderators Identified Across Papers:**

- **Punishment Technology & Cost/Impact Ratio:**  
  - Higher punishment effectiveness (e.g., 1:3 or higher cost-to-impact) increases the likelihood that punishment increases net efficiency; low effectiveness (e.g., 1:1) or high punishment costs may erode or reverse efficiency gains (Engel & Kurschilgen, 2013; Gürerk, Lauer et al., 2018; Marcin et al., 2019).
- **Network Structure and Monitoring Symmetry:**  
  - Symmetric, 'complete' punishment opportunities support efficiency gains; asymmetric or incomplete networks, or under-monitored individuals, undermine or reverse the effect (Boosey & Isaac, 2016; Leibbrandt et al., 2015; De Geest et al., 2017).
- **Subject Pool and Antisocial Punishment:**  
  - The prevalence of antisocial punishers (those who punish cooperators) and responsiveness to punishment varies by culture, population, and within-group heterogeneity, directly impacting efficiency (Bruhin et al., 2020; Bortolotti et al., 2015).
- **Information Structure:**  
  - Full disclosure of contributions/punishments, fixed IDs, and transparency help support efficiency via clearer signals and reduced antisocial retaliation (Kamei & Putterman, 2015; Kamei et al., 2017).
- **Endowment Heterogeneity:**  
  - Homogeneous endowments support punishment’s positive role; heterogeneity, especially when endowment info is hidden, can produce normative conflict and undermine efficiency gains (Kingsley, 2016).
- **Role of Communication and Social Learning:**  
  - Access to prior history or structured chat can amplfy the efficiency gains from punishment, sometimes substituting for punishment (Gürerk, 2013; Eisenkopf & Bächtiger, 2013).
- **Scale and Production Function:**  
  - Efficiency gains from punishment are robust in linear/average return PGGs, less so or absent in weakest-link/threshold/step-level games unless punishment is carefully designed and sometimes only with centralized mechanisms (Croson et al., 2015).
- **Third-Party and Centralized Punishment:**  
  - Centralized punishment, properly structured, can achieve similar or better efficiency gains, especially due to reduced antisocial punishment (Engel & Zhurakhovska, 2017; Gürerk, Lauer et al., 2018).

## c) **Effect of Punishment Relative to Control Efficiency:**  
- Generally, **the lower the control (no-punishment) efficiency**, the greater the potential for punishment to yield efficiency gains (Engl et al., 2021). However, high control efficiency may mean limited room for improvement or even efficiency losses due to unnecessary punishment costs (Kocher et al., 2012).

## d) **Non-costly/Social Sanctions:**  
- Costless or non-material punishment (e.g., disapproval points) can improve efficiency, while immaterial feedback mechanisms without clear social consequences usually show no robust efficiency benefit (Dugar, 2013; Peeters & Vorsatz, 2013).

## e) **Punishment Not Always Effective or Positive:**
- Punishment can **reduce efficiency** if:
  - There is high antisocial punishment (Bruhin et al., 2020).
  - Punishment is overused, weakly targeted, or too costly (Leibbrandt et al., 2015; Boosey & Isaac, 2016).
  - Institutional asymmetries/inefficiencies or uncoordinated sanctions exist (De Geest et al., 2017).
  - Punishment technology is flawed (e.g., random, non-individually-targeted) or in production functions with strong complementarities (step-level, weakest-link games) (Fatas et al., 2010; Croson et al., 2015).

# 5) Prediction Guidance

- **Prediction of Treatment Efficiency Should Be Anchored on:**
  - **Control (No-Punishment) Efficiency:** As a baseline, but always in context (e.g., with/without heterogeneity, subject pool, baseline antisocial punishment).
  - **Game Design Dimensions:**
    - **Directly Informed Dimensions**: player_count, num_rounds, mpcr, all_or_nothing, punishment_cost, punishment_tech, reward_exists/reward_cost/reward_tech (when relevant), and to a moderate degree, show_punishment_id (if info about punishment targets is explicit).
      - Strong empirical mapping exists for these: e.g., predicted gains are higher for 4–5 player, 8–30 round, continuous-contribution, peer punishment games with high punishment effectiveness and symmetric networks.
    - **Indirectly/Contextually Informed Dimensions**: chat, default_contrib, show_n_rounds, show_other_summaries, endowment heterogeneity (not a core parameter but highly influential), subject pool, history/social learning.
      - Effects on efficiency are primarily mediated through how they alter contribution expectations, baseline cooperation, or the ability to coordinate sanctions.
    - **Sparse/Effectively Missing**: default_contrib (opt-in/opt-out), chat (except where chat substitutes for punishment), show_Punishment_id (direct evidence is rare except in identity display studies).
- **Statistical Models Should Explicitly Encode the Moderators Above**:  
  - E.g., treatment effect sizes for punishment vary strongly across network symmetry, cost/impact ratio, and subject pool/culture.
  - Predictive confidence should decrease when design dimensions stray from the well-studied symmetrical, peer-punishment linear PGG cases.
  - Efficiency is *not* reliably increased by enabling punishment in all contexts; in environments with high antisocial punishment, heterogeneity, or poorly designed punishment architectures (asymmetric networks, high cost, low impact), the effect may be zero or negative.
- **Reward Mechanisms:** Sometimes outperform punishment in net efficiency and can interact with or substitute for punishment; predictions should account for whether both are enabled and their respective cost/tech (Gürerk, Lauer et al., 2018; Gürerk, Irlenbusch et al., 2009; Dugar, 2013).
- **Exclusion/Ostracism:** Exclusion, if costless or with minimal cost, yields efficiency gains similar to monetary punishment; costly exclusion can offset or reverse gains (Dannenberg et al., 2020).
- **Centralized vs Decentralized Punishment:** Centralized punishment may be less prone to antisocial misuse and yield more consistent efficiency gains, provided the central authority is motivated to uphold group welfare.
- **Non-material/Costless Sanctions:** Only increase efficiency if the platform supports meaningful social signalling (e.g., clear social approval/disapproval with group salience); otherwise, little impact (Dugar, 2013; Peeters & Vorsatz, 2013).

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed:**
- player_count, num_rounds, mpcr, all_or_nothing (binary/continuous contrib), punishment_cost, punishment_tech, reward_exists/cost/tech (in reward studies), and to a useful degree, network structure (though not always codified as a variable).
**Indirectly/Contextually Informed:**
- chat (as communication), show_other_summaries, show_n_rounds, social learning/history features, endowment heterogeneity, subject pool/culture, legal/normative framing.
**Under-Discussed/Sparse:**
- default_contrib (opt-in/opt-out framing is rarely varied in lab PGGs).
- show_punishment_id (explicit identity revelation of punishers/rewarders is rarely experimentally varied; a few studies examine full information vs ego-centric).
- Interaction effects among rarely combined features (e.g., chat with punishment, opt-out framing with antisocial punishment prevalence, etc.)

# 7) Important Limitations

- **Population/Context Specificity:** Many findings are robust for student populations in Western labs; antisocial punishment and unresponsiveness to punishment are far more prevalent in some societies, limiting generalizability.
- **Sparse Evidence on Some Design Dimensions:** Features like opt-in/out framing, explicit identity display (show_punishment_id), and nuanced chat integration lack direct experimental coverage in efficiency-focused studies.
- **Complex Institutional Features:** Many dimensions are studied in isolation—modeling their interactions (e.g., chat *with* punishment, heterogeneity *with* asymmetric monitoring) lacks direct evidence or requires speculative extrapolation.
- **Adjacency of Some Outcomes:** In some studies, efficiency must be inferred from contributions, which may over- or underestimate true welfare change if punishment is frequent and costly or antisocial.
- **Edge Cases (e.g., weak punishment, step-level or weakest-link production, extreme heterogeneity, very large groups):** Fewer studies provide clear guidance; in these regimes, punishment can be neutral or even negative for efficiency.
- **Long-term and External Validity:** Most studies use short time horizons (8–30 rounds), small groups (n=4–5), and relatively artificial environments; real-world durability of effects is less certain.
- **Omitted Variables**: Certain real-world features—e.g., reputational enforcement, endogenous group formation, objective inequalities—are variably represented if at all.
- **Lack of Theory Synthesis:** The mechanisms by which punishment yields efficiency gains are not always directly tested; results sometimes mix contribution rate with efficiency, even though the latter may be degraded by punishment cost or misuse.

---

**Summary**:  
The literature provides strong, multi-contextual, empirical evidence that enabling punishment in linear PGGs frequently increases efficiency relative to no-punishment baselines, *conditional on key design moderators*. The best-informed predictors are structural design features (group size, rounds, MPCR, punishment cost/effectiveness), network structure, and subject pool. However, effects can be null or negative where antisocial punishment is prevalent, enforcement is asymmetric, or punishment costs are high relative to impact. Indirect or missing evidence for certain design dimensions (e.g., chat, default contribution, identity revelation, framing) limits confident extrapolation for games differing substantially from the core lab PGG paradigm. Prediction models should condition strongly on control efficiency and design moderators, and maintain conservative uncertainty away from well-studied parameter regimes.
