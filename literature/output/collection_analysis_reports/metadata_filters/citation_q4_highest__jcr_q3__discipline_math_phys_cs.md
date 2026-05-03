# 1) Evidence Base

The literature set consists exclusively of **theoretical modeling and simulation studies** from mathematical biology and evolutionary game theory. **No empirical or lab experiment papers** are present in this set; all findings are model-based, with some referencing external lab-experimental results for validation. The set is **broad in the range of theoretical mechanisms considered** (peer punishment, institutional sanctions, spatial structure, indirect reciprocity, cultural and network effects), but **narrow with regard to the absence of direct experimental measurement of treatment efficiency in peer-punishment PGGs**. Most papers focus on **asymptotic evolutionary outcomes** (equilibrium strategies, stability conditions, population payoffs) rather than short-run or empirical outcomes under explicit laboratory PGG implementations.

# 2) Task Relevance

### a. `pgg_or_variant`
- **exact**: Many papers model the standard public goods game (PGG) or direct variants (e.g., Cressman et al., 2012; Gintis, 2000; Henrich & Boyd, 2001; Rand et al., 2010; Hauser et al., 2014; Schoenmakers et al., 2014; Szolnoki & Perc, 2013; Gintis et al., 2001).
- **close/adjacent**: Additional papers model indirect reciprocity, repeated prisoner's dilemma, or threshold games with analogous logic to collective action (Ohtsuki & Iwasa, 2004, 2006; Chalub et al., 2006; Gintis, 2003).
- **none**: Some discuss behavioral games (ultimatum, dictator) that only weakly relate to PGG reasoning for the specific prediction task.

### b. `punishment_or_sanctions`
- **exact**: Many papers model explicit costly punishment or institutional sanctions (Cressman et al., 2012; Gintis, 2000; Henrich & Boyd, 2001; Rand et al., 2010; Hauser et al., 2014; Janssen & Bushman, 2008; Szolnoki & Perc, 2013; Gintis et al., 2001; García & Traulsen, 2012).
- **adjacent/close**: Others address norm enforcement via reputation, withdrawal, indirect punishment, or gossip as a sanction-like mechanism (Ohtsuki & Iwasa, 2004, 2006; Chalub et al., 2006; Giardini & Conte, 2012).
- **none/weak**: Some focus purely on reward mechanisms, threshold/coordination effects, or spatial networks without any punishing.

### c. `efficiency_or_related_payoff_outcome`
- **exact**: Most theoretically grounded PGG and sanctioning models provide **explicit payoff/efficiency results**, often as mean group payoff or fraction of maximum potential efficiency (Cressman et al., 2012; Gintis, 2000; Gintis et al., 2001; Ohtsuki & Iwasa, 2004, 2006).
- **close/adjacent**: Several only report **strategy frequencies** (cooperation rate, evolution of punishers) and infer efficiency as a corollary, not a primary measured outcome (Szolnoki & Perc, 2013; García & Traulsen, 2012; Nakamaru & Iwasa, 2006).
- **none/weak**: A minority focus on perceptions, norm stability, or behavioral outcomes rather than realized payoffs.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes (directly informing efficiency):**
  - **Exact**: Mean group efficiency, total payoff, Nash equilibrium welfare, evolutionary fitness (Cressman et al., 2012; Gintis, 2000; Schoenmakers et al., 2014; Henrich & Boyd, 2001; Gintis et al., 2001; Ohtsuki & Iwasa, 2004, 2006; Gintis, 2003).
  - **Close**: Implicit total group payoff or efficiency derived from strategy frequencies when models do not report explicit payoffs.

- **Non-payoff behavioral outcomes:**
  - Frequencies of cooperators, defectors, and punishers.
  - Punishment assignment frequency, anti-social punishment rates, retaliation rates.
  - Reputation and social norm adoption, perceived exploitability, social learning dynamics.

- **Distinction:** Many findings about the **frequency of cooperation or punishment** are used to argue about efficiency, but some papers only infer payoff gains from behavior or via model equilibrium, not explicit measurement.

# 4) Main Findings Relevant To Prediction

### General Effects of Punishment on Efficiency
- **Punishment generally increases efficiency** relative to no-punishment baselines in standard PGGs, **if**:
    - Only pro-social punishment (punishing defectors) is possible.
    - Punishment is effective (high fine relative to cost).
    - Retaliation and anti-social punishment are rare or suppressed (Cressman et al., 2012; Gintis, 2000; Henrich & Boyd, 2001; Schoenmakers et al., 2014; Gintis et al., 2001).
- **Efficiency gains can disappear or reverse** when:
    - **Anti-social punishment** is possible: punishment of cooperators undermines the evolution and stability of cooperation, often returning to defection-like efficiency (Rand et al., 2010; Hauser et al., 2014; García & Traulsen, 2012).
    - **Retaliation against punishers** is possible, especially when identities are visible: cooperation and efficiency gains are suppressed (Janssen & Bushman, 2008).
    - **Punishment is too costly or ineffective**: In such cases, the costs outweigh the benefits, and efficiency can drop (Szolnoki & Perc, 2013; Nakamaru & Iwasa, 2006).

### Mechanistic Moderators: Game Design Dimensions
- **Group (player) size**: Complexity of sustaining high efficiency increases in larger groups without strong institutions or low-cost punishment (Gintis, 2000; Suzuki & Akiyama, 2007; Hilbe et al., 2015).
- **Punishment cost and technology**: Greater effectiveness (high impact per cost) and lower cost-to-fine ratios strongly predict the success of punishment in raising efficiency (Gintis, 2000; Schoenmakers et al., 2014; Gintis et al., 2001).
- **Anonymity/visibility of punishment**: Visibility of the punisher can facilitate retaliation and lower the impact of punishment on efficiency; anonymity can help maintain efficiency gains (Janssen & Bushman, 2008).
- **Presence of reward**: Some models suggest combining reward with punishment maximizes efficiency, but the primary focus relevant to prediction is on punishment alone (Cressman et al., 2012).
- **Social learning / norm transmission**: Payoff-biased and conformist learning can stabilize punishment and cooperation, producing higher payoffs in the long run (Henrich & Boyd, 2001; Gintis et al., 2001).
- **Spatial structure/networking**: Structure can both help and hurt depending on update rules and local groupings (Szolnoki & Perc, 2013; Nakamaru & Iwasa, 2006).
- **Retaliation and information**: Ability of punished individuals to identify and retaliate against punishers, as well as information about punishment, critically influences whether efficiency gains persist (Janssen & Bushman, 2008; Giardini & Conte, 2012).

# 5) Prediction Guidance

- **If pro-social peer punishment is enabled, with limited anti-social punishment and low retaliation risk**, **predict increased efficiency** compared to the control (no punishment), especially if punishment is not excessively costly and is consistently applied.
    - The relationship between design parameters and efficiency gains is governed by the **cost-to-fine ratio**, group size, and presence/absence of information that enables retaliation (Gintis, 2000; Henrich & Boyd, 2001).
    - **Knowledge of control group efficiency** is crucial: if baseline efficiency is already high (due to reward, commitment, or small group size), the marginal gain from punishment may be limited (Cressman et al., 2012).
- **If anti-social punishment or high retaliation risk exists, or punishment is very costly**, **do not count on efficiency gains** from enabling punishment; efficiency may remain unchanged or decrease (Rand et al., 2010; Hauser et al., 2014; Janssen & Bushman, 2008).
- **Effect size is context-dependent and not precisely quantified**, but the direction of effect is robust to model extensions when the above moderators are controlled.
- **Absence of empirical data**: All findings are from theory; real-world and short-run behavioral deviations are untested in this set.

# 6) Design Dimensions Highlighted Across Papers

**Directly Informed Dimensions:**
- `player_count`: Clear effects in most models (group size a key moderator).
- `num_rounds`: Modeled in repeated/iterated variants.
- `mpcr`: Fundamental parameter in payoff and evolutionary models.
- `punishment_cost`: Central to outcomes.
- `punishment_tech`: Effectiveness and design of punishment mechanism.
- `show_punishment_id`: Discussed as identity visibility/retaliation in some models.
- `reward_exists`, `reward_cost`, `reward_tech`: Direct evidence limited; some studies address reward with qualitative crossover to punishment.

**Indirectly/Contextually Informed:**
- `all_or_nothing`: Some models use binary vs. continuous contribution.
- `show_n_rounds`: Occasional attention in repeated/finite iterations.
- `show_other_summaries`: Modeled as observability of outcomes/or reputation.
- `chat`: Rarely modeled explicitly but sometimes present in broader social information effects.
- `default_contrib`: Opt-in/opt-out framing is not directly analyzed; context-dependent.
- `show_punishment_id`: Implicitly discussed as punisher visibility in retaliation.

**Effectively Missing:**
- **No empirical parameter estimates or lab data** for any design dimension.
- **No explicit treatment of chat/communication** effects except in contextual discussion.
- **No reporting of effect sizes or predicted efficiencies for specific dimensional combinations**.

# 7) Important Limitations

- **No empirical or experimental measurement of efficiency outcomes**: All conclusions are theoretical, with no real-world or laboratory PGG data on punishment-enabled vs. control efficiency.
- **Lack of direct modeling for chat/communication, opt-in/out framing, and specific observability features**: Most models abstract away from these dimensions or do not specify how they interact with punishment and efficiency.
- **Heavy focus on evolutionary stability/long-run equilibrium**: Short-term treatment effects, learning dynamics, and noise in small-group laboratory games may diverge.
- **Key moderators (anti-social punishment, retaliation, information structure) are sometimes modeled as binary switches**; real-world environments may exhibit intermediate forms.
- **Effect size ambiguity**: Magnitude of efficiency changes is not precisely quantified; only direction and moderators are clear.
- **Reward and combination incentive regimes are insufficiently addressed for the specific punishment prediction task**.
- **Boundary conditions and domain generality**: Some findings (e.g., from indirect reciprocity) may not transfer to canonical peer punishment PGGs, especially when reputation, exclusion, or other mechanisms are primary.
- **Absence of parameterized prediction functions**: No functional forms for predicting treatment efficiency from 14-dimensional game descriptors plus control efficiency are given.

---

**In summary:**  
This theory-driven evidence base demonstrates robust model support for the prediction that enabling peer punishment increases efficiency in PGG-like environments, if anti-social punishment and retaliation are suppressed, and if punishment is not prohibitively costly. The game design dimension evidence is strongest on player count, mpcr, punishment cost, and punishment implementation, but lacks empirical quantification for parameter combinations. Predictions should explicitly note the boundary conditions under which theoretical efficiency gains from punishment will (or will not) arise, and recognize the absence of lab data connecting these models to realized short-run group efficiency.
