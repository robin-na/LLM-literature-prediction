# 1) Evidence Base

This paper set is extensive and moderately diverse, containing 164 papers with a mix of empirical laboratory experiments, field experiments, observational studies, and theoretical/modeling papers. A significant portion of the studies are lab-based, tightly controlled public goods game (PGG) experiments, but there is also substantial coverage of adjacent social dilemmas, including Prisoner's Dilemma, trust, dictator, exclusion, and commons dilemmas.

The literature base is strongest for standard multi-player public goods games, with both empirical and theoretical research giving directly relevant evidence for efficiency and payoff-based outcomes. There are also numerous papers on closely related dilemmas (e.g., repeated dyadic interactions, pool punishment, exclusion, and networked/coordinated environments) and a substantive body of theory papers modeling the efficiency impact of various institutional and behavioral interventions.

Overall, the evidence base is broad and contains many high-relevance, directly empirical studies—especially focused on repeated, fixed-group linear PGGs with and without punishment. Some important dimensions (e.g., peer vs. pool punishment, reward vs. punishment, impacts of communication, reputation, and anti-social punishment) are addressed via both experiments and modeling, while others (such as the effects of chat, opt-in framing, or alternative social structures) are more sparsely represented. Theoretical coverage of complex moderators is strong, but empirical multi-factor manipulations are relatively rare. The base includes research from diverse societies but has a majority of studies conducted in Western lab settings.

# 2) Task Relevance

**pgg_or_variant:**  
- The coverage is *exact* for standard PGGs and their direct variants (multi-player, repeated rounds, continuous or all-or-nothing contributions, linear payoff structure).  
- Many papers are *close* (e.g., commons dilemmas, threshold/collective-risk PGGs, networked games, institutional variants, or evolutionary models directly mapped to PGGs).  
- A minority are *adjacent* or *weak* (Prisoner's Dilemma, Dictator, or Trust Games, or field studies about norm enforcement).

**punishment_or_sanctions:**  
- The majority of relevant papers are *exact*—they manipulate the presence of peer or institutional punishment.  
- Many also consider both *punishment and reward* (costly incentives) or compare *peer* to *pool* punishment, including second-order punishment.  
- Some evidence is *close* (punishment as exclusion, social ostracism, or indirect/reputation-based mechanisms) or *adjacent* (partner choice, indirect sanctions).  
- A few studies cover only *weak* or *none* (settings with no punishment manipulated), serving as baseline references.

**efficiency_or_related_payoff_outcome:**  
- There is *exact* coverage in key experimental and theoretical studies that directly measure group efficiency, welfare, surplus, or net earnings versus the cooperative optimum.
- Several important studies report only *close* outcomes (average contribution as a proxy for efficiency, or group success rate in threshold games).
- Some are *adjacent* (analyzing only behavioral outcomes such as cooperation rate or punishment frequency), providing only indirect information.
- A segment of the paper set is *none*, lacking payoff or efficiency outcomes altogether.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes:** Directly measured group efficiency, total payoff/profit, welfare, group surplus, mean group earnings, or the fraction of the social optimum achieved. These are most relevant for the prediction task.
- **Proxy outcomes:** Average contribution, provision or maintenance of the public good, group success rate in threshold games, or share of cooperative groups. Proxies are often used where direct efficiency reporting is absent but can usually be mapped reliably in standard PGGs.
- **Non-payoff behavioral outcomes:** Individual or group contribution rates, cooperation/defection rates, punishment/reward frequency, norm compliance, conditional cooperation, ostracism, exclusion, partner selection, or emotional/psychological responses.  
  - While informative for mechanisms, these are not equivalent to efficiency and cannot always be reliably mapped to group payoffs, especially when punishment is costly or when anti-social punishment occurs.

# 4) Main Findings Relevant To Prediction

**Empirical and theoretical synthesis shows:**

- **Punishment reliably increases efficiency in standard, repeated PGGs with moderate group size, moderate-to-high MPCR, and peer punishment—provided anti-social punishment is rare and the punishment cost is not prohibitive** (Fehr & Gächter, 2002; Gürerk et al., 2006; Gächter et al., 2017; Gross et al., 2016; Hilbe et al., 2014; Rockenbach & Milinski, 2006).
- **Reward (positive incentives) is often as effective or more efficient than punishment**; combining reward and punishment can produce the highest efficiency (Rand et al., 2009; Chen et al., 2015; Fang et al., 2019).
- **Punishment is costly; if used frequently, the costs can offset gains from increased cooperation, so efficiency does not always rise—even when contribution rates do** (Wu et al., 2016; Lohse & Waichman, 2020; Dreber et al., 2008).
- **When norm signaling, communication (chat), or reputation mechanisms are present, the efficiency gains due to punishment are much larger and punishment is used less frequently** (Rockenbach & Milinski, 2006; Andrighetto et al., 2013).
- **Anti-social punishment, corruption, and counter-punishment can completely nullify or even reverse efficiency gains from punishment**; their prevalence depends on cultural, game, and institutional context (Herrmann et al., 2008; Rand & Nowak, 2011; Muthukrishna et al., 2017).
- **Threshold effects are observed: at low punishment cost, or high enough punishment impact, transformative efficiency gains can occur (often discontinuously)**—but beyond certain costs, additional punishment has little effect or is even detrimental (Perc, 2012; Sasaki et al., 2012).
- **Punishment can enforce destructive or inefficient norms, leading to a decrease in efficiency if the underlying social or economic structure makes cooperation net-destructive (MPCR<1/n)** (Abbink et al., 2017).
- **Communication alone, or in combination with punishment, can produce efficiency gains as large or larger than punishment alone** (Andrighetto et al., 2013; Janssen et al., 2010).

# 5) Prediction Guidance

## General Principles

- **Baseline control efficiency is an important predictor:** Where control (no-punishment) efficiency is already high—e.g., due to high MPCR, reward, repeated interaction, or strong reputation—adding punishment yields little or no additional efficiency.
- **Expect a strong positive effect of enabling peer punishment on efficiency relative to control in:**
  - Standard repeated-PGGs with MPCR ≥ 1/n, moderate group size (4–6), moderate punishment cost (1:3 or similar cost:impact), and no endemic anti-social punishment.
- **Magnitude of efficiency gain is highly sensitive to game design:**
  - **Punishment cost/impact ratio:** Lower punishment cost and higher impact per cost → larger efficiency gains (subject to ceiling effects); high cost can nullify gains.
  - **Presence of reward:** If both are available, effect of punishment is dampened or reversed (Rand et al., 2009).
  - **Reputation, feedback, communication:** Strongly moderate the efficiency impact—transparent feedback or chat magnifies positive effect of punishment (Rockenbach & Milinski, 2006; Andrighetto et al., 2013).
  - **Institutional context:** Voluntary participation, centralization of punishment, institution choice, and legitimacy of authority amplify or suppress the effect (Gross et al., 2016; Hilbe et al., 2014; Baldassarri & Grossman, 2011).
- **Anti-social punishment, second-order free riders, and corruption:**  
  - If anti-social punishment or second-order free riding is possible and not suppressed (by design or norms), effect of punishment on efficiency can be null or negative (Herrmann et al., 2008; Perc, 2012).
  - If corruption/bribery (e.g., leader diverts punishment) is possible, punishment can reduce efficiency (Muthukrishna et al., 2017).

## Parameter Mapping

- **Directly useable design dimensions for prediction:**  
  - *player_count, num_rounds, mpcr, punishment_cost, punishment_tech, reward_exists, reward_cost, chat, show_other_summaries, show_n_rounds, show_punishment_id, default_contrib, all_or_nothing* (varied across exact-match studies).
- **For new games fitting the canonical repeated PGG design, expect efficiency to increase on enabling punishment, with estimates proportional to empirical benchmarks (~60–95% of optimum with punishment vs. 30–60% without, exact figures from Fehr & Gächter, 2002; Gürerk et al., 2006; Gächter et al., 2017).**
- **Contextual modifiers:** Reduce expected efficiency gain if punishment is high-cost, impact:cost is low, reward is present, chat/reputation is absent, anti-social punishment is likely (e.g., non-Western contexts or no mechanism to suppress anti-social punishment).

## Caveats

- **Do not infer efficiency gains from increased contributions alone—cases exist where punishment increases contribution rates but net payoffs do not rise, due to punishment cost or destructive enforcement** (Wu et al., 2016; Janssen et al., 2010; Abbink et al., 2017).
- **Empirical studies with negative or null efficiency effect of punishment are disproportionately associated with:**
  - High punishment cost/low impact.
  - Anti-social punishment/misaligned social norms.
  - Non-PGG settings (dyadic/Prisoner's Dilemma).
  - Environments allowing corruption, bribery, or destructive enforcement.
- **Effect of punishment on efficiency is likely non-monotonic in both punishment cost and impact; beyond certain thresholds, additional increases don't yield benefit and may cause harm** (Perc, 2012).

# 6) Design Dimensions Highlighted Across Papers

The following prediction dimensions are **best informed** by the evidence base (often directly manipulated or measured):

- `player_count`: Group size (typically 4–6, but some studies vary this).
- `num_rounds`: Repeated vs. one-shot games, with moderate- to high-n rounds driving more robust punishment effects.
- `mpcr`: Substantial variation; key moderator; directly linked to efficiency and observed as a critical threshold in several studies.
- `punishment_cost` & `punishment_tech`: Commonly manipulated; fee-to-fine ratio and allowable punishment intensity are critical moderators.
- `reward_exists`, `reward_cost`, `reward_tech`: Often manipulated in comparison to, or combination with, punishment.
- `chat`, `show_other_summaries`, `show_punishment_id`: Covered, especially regarding their effect on reputation, feedback, and norm salience.
- `all_or_nothing` & `default_contrib`: Present in many standard PGG designs.
- `show_n_rounds`: Varied; not always central, but sometimes a moderator of horizon effects.

**Indirectly informed or contextually discussed:**
- `punishment_tech`: Details beyond fee-to-fine ratio (e.g., targeting, visibility, scope).
- `show_other_summaries`, `show_punishment_id`: More contextually noted as part of reputation and transparency mechanisms.
- `centralization` or delegation of punishment (institutional vs. peer): Covered in a subset.

**Sparse or missing:**
- Detailed manipulation or reporting of `default_contrib` (opt-in/not) and its impact on efficiency under punishment.
- Games with `reward_exists` as the only intervention—most evidence is for punishment alone or joint reward-punishment.
- Fine-grained effects or interactive treatment of dimension combinations (e.g., chat × punishment × reward).

# 7) Important Limitations

- **Heterogeneity in Experimental Contexts:**  
  - Most lab experiments feature Western, student populations in artificial, well-understood environments; field/lab comparisons show context (especially anti-social punishment, legitimacy of authority, and baseline norms) can dramatically alter effects.
- **Limited Generalizability to Complex and Real-world Settings:**  
  - More complex social dilemmas (e.g., real resource management, optional participation, multigenerational thresholds, corruption/bribery, diverse participant pools) may yield different outcomes.
- **Variable Reporting:**  
  - Many studies report contribution rates or behavioral phenomena, not group efficiency/payoff, requiring careful mapping or exclusion.
- **Design Dimension Gaps:**  
  - Some relevant prediction dimensions (detailed communication protocols, opt-in framing, hybrid institutions, degree of anonymity, and punishment visibility) are thinly covered or unreported.
- **Non-monotonic and Discontinuous Effects:**  
  - Efficiency gains may jump (phase transitions) or collapse at parameter thresholds (e.g., insufficient punishment impact, excessive cost, existence of second-order free riders, or corruptible institutions), not captured by linear models.
- **Antisocial Punishment and Norm Enforcement of Inefficient Equilibria:**  
  - In some contexts, punishment stabilizes inefficient or destructive norms (Abbink et al., 2017), so increases in contribution can *reduce* efficiency.
- **Reward is Often a More Effective or Efficient Mechanism:**  
  - Many studies indicate that enabling only punishment misses out on the larger, more efficient gains available from reward or hybrid incentives.

---

**In summary:**  
The literature base provides strong, direct, and nuanced guidance for predicting the effect of enabling peer punishment on PGG efficiency, especially in canonical lab settings with known game dimensions. Many design moderators are well quantified; others require more caution. There is substantial qualification to the general "punishment increases efficiency" result, with several documented exceptions and reversals depending on cost structure, the presence of anti-social punishment, social/institutional norms, and design features such as chat, reward, or corruption. Control efficiency is a useful, but not sufficient, input for prediction: design features and context must also be accounted for, and behavioral outcomes must not be conflated with payoff.
