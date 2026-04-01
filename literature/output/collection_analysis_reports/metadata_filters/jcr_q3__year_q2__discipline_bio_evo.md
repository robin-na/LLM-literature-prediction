# 1) Evidence Base

The supplied paper set is broad in both method and conceptual scope, covering 41 papers including laboratory experiments, agent-based and analytic theory, and simulation studies. Empirical coverage is strong for classic repeated public goods games and some close variants; most empirical studies are lab-based with detailed manipulation of core design parameters. Large portions of the set are theoretical or model-based, including extensive analyses of population structure, punishment modalities (peer vs. centralized), social norms, corruption, information structure, and dynamic/environmental contingencies. Most theoretical papers are tightly focused on evolutionary mechanisms, strategic stability, or institution design, with strong attention to critical moderators (e.g., anti-social punishment, information noise, or cost structures).

The set is rich for the prediction task: direct coverage (exact or close) for PGG and its structural variants, detailed examination of punishment and sanctions (institutional, peer, and counter-punishment), and frequent—though not always primary—attention to payoff-based outcomes, especially group efficiency as defined by the prediction task. Several studies, both empirical and theoretical, report effects of enabling punishment under conditions closely matching classic PGG parameters and manipulations.

However, the literature also includes many adjacent or supporting studies that focus primarily on behavioral outcomes (cooperation rates, norm compliance, etc.) or closely related games (prisoner's dilemma, common-pool resource games), providing indirect evidence or mechanistic insight rather than direct payoff results.

# 2) Task Relevance

**pgg_or_variant:**  
- **exact:** Most papers focus on the PGG or direct extensions (e.g., weakest-link or voluntary PGGs).  
- **close/adjacent:** Some model common-pool resources, n-player prisoners’ dilemmas, or structured spatial dilemmas, which share critical features but may differ in outcome mapping.  
- **none:** A minority focus on fundamentally different tasks or allocation games.

**punishment_or_sanctions:**  
- **exact:** Many works (empirical and theoretical) directly manipulate or model peer punishment, institutional (pool) punishment, or variations (counter-punishment, graduated punishment).
- **close/adjacent:** Several studies use punishment-like mechanisms (exclusion, reputation-based sanctions, social pressure) mapping closely to sanctions in PGG contexts.
- **none:** Some works entirely exclude punishment mechanisms (e.g., focus only on reciprocity, reward, or voluntary withdrawal).

**efficiency_or_related_payoff_outcome:**  
- **exact:** Empirical PGG studies report efficiency (group payoff as a fraction of the cooperative maximum) or close equivalents.
- **close:** Some theoretical/simulation studies focus on total group payoff or stationary average welfare.
- **adjacent/weak:** Many theory papers focus mainly on cooperation rates or strategy abundances, inferring efficiency only indirectly.
- **none:** A subset measure only behavioral or psychological responses, with no link to group payoff.

**Summary:**  
Relevance for the downstream prediction task is high for PGG and punishment; coverage is moderately strong for efficiency/payoff outcomes, though in a significant portion of the literature, efficiency is inferred via cooperation or strategy prevalence, not always reported as primary outcome.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (direct):**
  - Group efficiency (total payoff relative to fully cooperative optimum) [frequent in PGG empirical studies and some theory].
  - Group total earnings, welfare, or surplus.
  - Explicit modeling of group welfare, average payoff, or evolutionary fitness proxies.

- **Payoff-related outcomes (indirect):**
  - Fraction of cooperators (when mapping is direct to payoff, e.g., in linear PGGs).
  - Resource sustainability or average stock (in common-pool resource models as stand-ins for group efficiency).

- **Non-payoff behavioral outcomes:**
  - Average contribution/cooperation rate.
  - Punishment frequency, anti/social punishment rates.
  - Norm compliance, strategy frequencies, pattern dynamics.
  - Psychological, cognitive, or neural correlates.

**Distinction:**  
Empirical lab studies often report both contribution and payoff/efficiency, while theory/simulation results frequently focus on behavioral-strategy outcomes, requiring inference for payoff-based prediction. Many adjacent papers provide mechanism insights without explicit efficiency reporting.

# 4) Main Findings Relevant To Prediction

**General pattern:**
- **Punishment can, but need not, increase efficiency relative to the no-punishment control.** The effect is highly context dependent:
  - **Information environment:** Punishment is only effective at boosting efficiency when information about contributions or identities is sufficiently rich and accurate. Noise or lack of transparency can dampen or reverse the effect (Fischer et al., 2016; Larson, 2016).
  - **Production function:** Payoff structure matters. In linear PGGs, antisocial punishment and cultural factors often negate efficiency gains (Fatas & Mateu, 2015; Hauser et al., 2014). In complementarity-based (weakest-link) games or non-linear benefit structures, punishment can dramatically increase efficiency (Fatas & Mateu, 2015; Archetti & Scheuring, 2013).
  - **Punishment design:** Centralized (institutional/pool) punishment is often more robust or effective at increasing efficiency than decentralized peer punishment, especially where antisocial punishment is prevalent (Gao et al., 2015; Fischer et al., 2016; Dercole et al., 2013; Schoenmakers et al., 2014).
  - **Anti-social punishment:** Allows at least as much efficiency loss as gain; only pro-social punishment consistently increases efficiency (Hauser et al., 2014; Fatas & Mateu, 2015).
  - **Communication:** Enabling communication or normative messaging reliably enhances efficiency in punishment environments, neutralizing negative effects of counter-punishment (Andrighetto et al., 2016).
  - **Institutional quality:** The honesty, effectiveness, and transparency of enforcers or institutions strongly moderate the efficiency impact of punishment (Lee et al., 2015; Lee et al., 2017).
  - **Group structure & size:** Spatial/structured populations, smaller group sizes, or community-based enforcement often enhance positive punishment effects (Oya & Ohtsuki, 2017). Large and well-mixed groups, or weak group associations, often see diminished or null effects.
  - **Cost-to-fine ratio:** Efficiency gains from punishment fall if it is too costly or if fine-to-cost ratio is low (Szolnoki & Perc, 2013; Dercole et al., 2013).

**Findings by design feature:**
- **Peer punishment (enabled):**
  - Typical effect is small or null increase in efficiency, sometimes even reduced efficiency due to retaliation or antisocial punishment unless paired with strong institutional rules or communication (Fischer et al., 2016; Fatas & Mateu, 2015).
- **Centralized/institutional punishment:**
  - More consistently yields higher efficiency, especially when institutions are transparent and honest (Schoenmakers et al., 2014; Lee et al., 2017).
- **Communication:**
  - Strong moderator; when chat/messaging is enabled, negative punishment effects are consistently muted or reversed (Andrighetto et al., 2016).
- **Counter-punishment:**
  - Only detrimental to efficiency when chat is not enabled; can be mitigated or eliminated with communication (Andrighetto et al., 2016).
- **Production function (all_or_nothing, weakest-link):**
  - Where the PGG reward function is complementary or nonlinear, punishment boosts efficiency more robustly (Fatas & Mateu, 2015; Archetti & Scheuring, 2013).
- **Population structure:**
  - Structured or spatially clustered populations see more positive efficiency effects, while well-mixed populations typically do not benefit from punishment (Oya & Ohtsuki, 2017; Kaiping et al., 2016).

# 5) Prediction Guidance

- **Base prediction on control (no-punishment) efficiency plus key design moderators:**
  - **Punishment will increase efficiency only when:**
    - Pro-social (not anti-social) punishment is the norm, or antisocial punishment is institutionally deterred (Hauser et al., 2014).
    - Information about defections/contributions is sufficiently accurate and visible (Fischer et al., 2016; Larson, 2016).
    - The punishment institution is honest, transparent, and not corrupt (Lee et al., 2015, 2017).
    - Chat or communication is allowed, especially in settings with counter-punishment (Andrighetto et al., 2016).
    - Group size is moderate; effect declines in large, well-mixed groups (Hilbe et al., 2015; Oya & Ohtsuki, 2017).

- **Do NOT expect efficiency gains from enabling punishment when:**
  - Anti-social punishment is common or undeterred (Hauser et al., 2014; Fatas & Mateu, 2015).
  - Information is severely noisy or incomplete.
  - Institution is subject to corruption and players can't identify honest punishers (Lee et al., 2015, 2017).
  - Costs of punishment are high relative to its deterrent effect.
  - Control (no-punishment) efficiency is already high due to other mechanisms (e.g., reciprocity, specific benefit function).

- **Magnitude of the effect:**
  - The incremental gain in efficiency from enabling peer punishment is unreliable; some contexts see no gain or even a loss. In contrast, moving from no-punishment to transparent, centralized punishment can yield a substantial increase—but only under institutional integrity.
  - Communication and production function (linear vs. nonlinear) can swing the efficiency effect from negative/neutral to strongly positive.

# 6) Design Dimensions Highlighted Across Papers

**Directly informed dimensions:**
- `player_count` (frequently manipulated; impact on efficiency robustly described).
- `num_rounds` (empirical studies specific; theory papers analyze repeated play).
- `chat` (critical moderator of punishment effect on efficiency).
- `all_or_nothing` (binary vs. continuous; effects on payoff evaluated, especially in weakest-link/complementarity variants).
- `mpcr` (widely captured as key driver of the benefits of cooperation and punishment effectiveness).
- `punishment_cost`, `punishment_tech` (core to nearly all punishment studies; differentiated between peer/centralized, cost/fine ratio, conditional vs. unconditional).
- `show_other_summaries`, `show_n_rounds`, `show_punishment_id` (variously tested as part of information structure/institutional transparency).

**Indirectly or variably informed:**
- `default_contrib` (opt-in/opt-out framing occasionally noted, not systematically manipulated).
- `reward_exists`, `reward_cost`, `reward_tech` (a few studies test or discuss reward mechanisms, but core findings focused on punishment).
- `punishment_magnitude` (sometimes subsumed under technology/cost or fine; not always separated as a unique dimension).

**Contextually/discursively discussed or sparse:**
- `reward_magnitude` (rarely a primary focus).
- Combined/interactive settings (e.g., both punishment and reward enabled) are not as systematically explored for direct payoff effects as peer punishment alone.

# 7) Important Limitations

- **Ambiguous effect directions:** Some studies (especially lab experiments in linear PGGs) find no efficiency gain—or even a loss—when punishment is enabled, due to antisocial punishment or escalation (Fatas & Mateu, 2015; Fischer et al., 2016).
- **Heavily context-moderated outcomes:** The effect of punishment on efficiency is highly sensitive to information structure, punishment design, and social norms/culture. Generalization to novel contexts is risky if these variables are not measured.
- **Payoff vs. behavioral conflation:** Many theory and simulation papers focus on cooperation rates rather than efficiency, meaning inference for the prediction task often requires assuming that increases in cooperation translate to payoff in the specific game structure, which may not always hold (notably in nonlinear or threshold payoff functions).
- **Rare direct estimates for all dimensions:** Some design dimensions essential for prediction (e.g., default_contrib, specific visibility manipulations) are not systematically varied in ways that would allow precise parameterization.
- **Institution quality and honesty often assumed:** Some theory results predicting strong positive effects of punishment presume perfect or visible enforcement, rarely achieved in empirical settings.
- **Culture and sample limitations:** Many empirical results come from relatively narrow samples or cultures with known differences in antisocial punishment rates; variation in baseline efficiency and punishment response is likely.
- **External mechanisms (e.g., reward, communication):** Efficiency effects attributed to punishment may, in practice, require co-enabling of communication, reputation, or reward mechanisms to be positive.
- **Short-run vs. long-run:** Many theoretical findings concern evolutionary stability or long-run dynamics, while experimental results are mostly short-run; translation between the two may be imperfect.
- **No direct experimental manipulation for some parameter combinations:** Few, if any, studies exhaustively manipulate all 14 prediction dimensions in laboratory settings, meaning some interactions (e.g., between visibility, chat, default framing, and cost structure) remain untested empirically.

---

**In summary:**  
The literature provides solid, multi-method evidence for predicting the incremental effect of enabling punishment on efficiency in public-goods-game-like environments, but the direction and magnitude of this effect are highly sensitive to specific design choices—especially information visibility, communication, punishment institution design, production function, and the baseline rate of anti-social punishment. Prediction should not assume a uniform positive effect of punishment; instead, design features and control efficiency as well as the broader social context must inform any estimate. Many critical design dimensions are directly studied, though some (reward, default framing, complex institution design) are less fully covered in terms of their impact on efficiency relative to punishment.
