You are preparing an intermediate literature synthesis for one chunk of a disjoint leaf partition from a larger paper universe.

        The downstream task is: given 14 CONFIG design parameters plus control efficiency, predict treatment efficiency when peer punishment is enabled in a public goods game.

        This leaf partition is defined by:
        - A (exact/close PGG relevance AND exact/close punishment relevance): off
        - B (paper reports payoff-like outcomes): off
        - C (paper is empirical): off

        Use only the leaf evidence digest below. It contains compact paper-level analysis entries for one subset of the broad literature pool.

        What to do:
        - Synthesize across papers in this chunk instead of summarizing them one by one.
        - Track how strong the evidence is inside this leaf, given its relevance, outcome, and study-type profile.
        - Distinguish empirical findings from theory or mechanism arguments.
        - Identify which design dimensions in the 14-parameter task are covered in this chunk and where evidence is sparse.
        - Preserve ambiguity and disagreement when the papers conflict.
        - Do not add outside claims.

        Output Markdown with these sections:
        1) Leaf Coverage
        2) Empirical Patterns
        3) Theory Or Mechanism Signals
        4) Design-Dimension Signals
        5) Predictive Implications For Peer Punishment
        6) Limitations And Gaps

        Make this an intermediate synthesis note that can later be combined with other chunk notes from the same leaf.

        Column definitions:
        - CONFIG_playerCount: Number of players in the game.
- CONFIG_numRounds: Number of rounds in the game.
- CONFIG_MPCR: Marginal per-capita return = multiplier / playerCount.
- CONFIG_allOrNothing: If true, contributions are all-or-nothing rather than continuous amounts.
- CONFIG_chat: Whether chat is enabled between players.
- CONFIG_defaultContribProp: Contribution framing: 0 = opt-in (default keep; must actively give), 1 = opt-out (default contribute; must actively keep).
- CONFIG_punishmentCost: Cost to the punisher per unit of punishment.
- CONFIG_punishmentMagnitude: Coins deducted from a punished player per unit of punishment.
- CONFIG_showOtherSummaries: Whether peer outcomes are shown each round.
- CONFIG_showNRounds: Whether the total number of rounds is shown to players.
- CONFIG_showPunishmentId: Whether the identity of punishers or rewarders is shown.
- CONFIG_rewardExists: Whether rewards are enabled in the game.
- CONFIG_rewardCost: Cost to the rewarder per unit of reward.
- CONFIG_rewardMagnitude: Coins added to a rewarded player per unit of reward.
- CONFIG_punishmentExists: Whether punishment is enabled in the game.

        Leaf metadata:
        - Leaf id: leaf_a0_b0_c0
        - Leaf definition: A=off (exact/close PGG+punishment), B=off (payoff-like outcomes), C=off (empirical)
        - Chunk: 1 of 4
        - Total papers in leaf: 363

        Leaf evidence digest:
        ----------
        # Leaf Evidence Digest: leaf_a0_b0_c0

Leaf definition: A=off (exact/close PGG+punishment), B=off (payoff-like outcomes), C=off (empirical)

Chunk 1 of 4

Total papers in leaf: 363

Papers in this chunk: 99

Each item below is a compact paper-level analysis digest. Use only this digest.

- id: 10.1038_s41598-021-03045-w
  source: Evolution of cooperation and consistent personalities in public goods games | Scientific Reports | 2021
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr, reward_exists, reward_cost
  findings: The paper finds that in two-round public goods games, both reward-based and assortative mechanisms can promote the evolution of cooperation and the emergence of consistent...
  prediction_guidance: This paper does not provide direct evidence for the effect of punishment on efficiency in public goods games. It is highly relevant for understanding how reward and assortment...

- id: 10.1098_rsif.2024.0827
  source: Indirect reciprocity in the public goods game with collective reputations | Journal Of The Royal Society Interface | 2025
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr, show_other_summaries
  findings: The paper finds that in public goods games with collective reputation and indirect reciprocity, all of the leading-eight social norm strategies can sustain cooperation in...
  prediction_guidance: This paper provides indirect evidence for the prediction task by showing that, in public goods games with indirect reciprocity and collective reputation (but without explicit...

- id: 10.1016_j.amc.2018.10.068
  source: Cleverly handling the donation information can promote cooperation in public goods game | Applied Mathematics And Computation | 2019
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=more_positive
  dimensions: player_count, num_rounds, all_or_nothing, mpcr, show_other_summaries
  findings: Publishing the donation list partially (i.e., only for those who contribute above a threshold) increases total contributions to the public good compared to publishing all or...
  prediction_guidance: This paper provides evidence that indirect social sanctions (via partial publication of contribution information and gossip) can increase total group contributions in a...

- id: 10.1371_journal.pone.0023019
  source: An Institutional Mechanism for Assortment in an Ecology of Games | Plos One | 2011
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, mpcr
  findings: The paper finds that capacity constraints (limits on the number of players per game) are a simple and effective institutional mechanism for promoting positive assortment of...
  prediction_guidance: This paper does not provide direct evidence for the effect of punishment on efficiency in public goods games, as it does not model punishment or sanctions. However, it is...

- id: 10.1016_j.physa.2010.04.018
  source: Diversity of contribution promotes cooperation in public goods games | Physica A-Statistical Mechanics And Its Applications | 2010
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, mpcr
  findings: The study finds that allowing cooperators to preferentially contribute more to groups with higher cooperation levels (high-quality groups) significantly promotes the evolution...
  prediction_guidance: This paper is relevant for understanding how endogenous contribution patterns (where cooperators can direct more resources to cooperative groups) affect cooperation and the...

- id: 10.1016_j.jtbi.2011.03.017
  source: The joker effect: Cooperation driven by destructive agents | Journal Of Theoretical Biology | 2011
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, all_or_nothing, mpcr
  findings: The paper finds that introducing destructive agents ('jokers') into a public goods game leads to robust cycles in which cooperation periodically surges. The mechanism is that...
  prediction_guidance: This paper is not directly informative for predicting the effect of punishment on efficiency in public goods games, as it does not study punishment or sanctions per se....

- id: 10.1038_srep01521
  source: Evolution of collective action in adaptive social structures | Scientific Reports | 2013
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, mpcr
  findings: The paper finds that when individuals can adapt their social ties—specifically, break links with defectors more quickly than with cooperators—cooperation can be sustained at...
  prediction_guidance: This paper is useful for understanding how endogenous partner selection and adaptive network structure can promote cooperation in PGGs, which may indirectly inform predictions...

- id: 10.1016_j.physa.2006.11.047
  source: Smiling contributions:: Social control in a public goods game with network decline | Physica A-Statistical Mechanics And Its Applications | 2007
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, chat, all_or_nothing, mpcr, punishment_cost, reward_exists
  findings: The paper develops a theoretical framework for public goods games with endogenous network change and social control mechanisms. It predicts that clustered networks reduce...
  prediction_guidance: This paper provides theoretical insights into how network structure and non-costly social control (smileys) might affect contribution behavior in public goods games. However,...

- id: 10.1140_epjb_e2020-100618-x
  source: Promoting cooperation by reputation-based payoff transfer mechanism in public goods game | European Physical Journal B | 2020
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr, punishment_tech, reward_exists
  findings: The reputation-based payoff transfer mechanism, which redistributes payoffs from low- to high-reputation players, can significantly increase the fraction of cooperators in a...
  prediction_guidance: This paper provides indirect evidence that mechanisms combining endogenous punishment and reward based on reputation can increase cooperation rates in public goods games,...

- id: 10.1007_s42001-019-00049-5
  source: A belief in rewards accelerates cooperation on consumer-generated media | Journal Of Computational Social Science | 2020
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr, reward_exists, reward_cost
  findings: The study finds that in a public goods game with only rewards and meta-rewards (no punishment), cooperation can be sustained if players can observe and respond to the...
  prediction_guidance: This paper does not provide direct evidence for the effect of punishment on efficiency in public goods games. It is relevant for understanding the role of reward and...

- id: 10.1209_0295-5075_92_38003
  source: Reward and cooperation in the spatial public goods game | Epl | 2010
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr, reward_exists, reward_cost
  findings: The study finds that introducing costly reward in a spatial public goods game can promote cooperation, particularly when the synergy factor (MPCR) is low. However, the effect...
  prediction_guidance: This paper provides indirect evidence about the effect of reward (not punishment) on cooperation in spatial public goods games. It does not report efficiency or payoff...

- id: 10.1140_epjb_e2018-90052-6
  source: The impact of neutral reward on cooperation in public good game | European Physical Journal B | 2018
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr, reward_exists, reward_cost
  findings: The study finds that introducing a neutral reward mechanism, where the majority strategy in a group is rewarded by the minority, promotes the evolution of cooperation in a...
  prediction_guidance: This paper provides indirect evidence that reward mechanisms (even when not perfectly targeted) can promote cooperation in spatial public goods games. However, because the...

- id: 10.1038_srep23006
  source: Evolution of conditional cooperation under multilevel selection | Scientific Reports | 2016
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, chat, all_or_nothing, mpcr, show_n_rounds
  findings: The paper demonstrates that in public goods games with continuous contribution and multilevel selection, the presence of conditional strategies (modeled as piecewise linear...
  prediction_guidance: This paper provides strong evidence that conditional cooperation strategies can sustain high contribution levels in public goods games under multilevel selection, even without...

- id: 10.1016_j.jebo.2020.01.010
  source: Children's heterogeneity in cooperation and parental background: An experimental study | Journal Of Economic Behavior & Organization | 2020
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr, reward_exists, reward_cost
  findings: The study finds that allocating taxes and rewards based on memory reputation generally increases the cooperation rate in spatial public goods games, especially in environments...
  prediction_guidance: This paper does not provide direct evidence for predicting the effect of punishment on efficiency in public goods games, as it does not include punishment or efficiency...

- id: 10.1109_tcss.2024.3386501
  source: Evolutionary Dynamics of Preguidance Strategies in Population Games | Ieee Transactions On Computational Social Systems | 2024
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr, show_n_rounds
  findings: The paper introduces and analyzes two forms of preemptive guidance strategies (peer and pool guidance) in a one-shot public goods game with a pregame negotiation phase. Both...
  prediction_guidance: This paper provides theoretical and simulation evidence that preemptive guidance strategies can reduce free riding and increase the prevalence of guidance strategies in PGGs,...

- id: 10.3389_fphy.2020.00058
  source: Public Goods Games on Coevolving Social Network Models | Frontiers In Physics | 2020
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr, show_n_rounds
  findings: The study finds that allowing agents to rewire their social connections when unsatisfied (i.e., when their payoff is less than their contribution) leads to higher average...
  prediction_guidance: This paper provides indirect evidence that enabling a form of costless partner switching (exit) can increase average contributions in networked public goods games, which may be...

- id: 10.1103_PhysRevE.95.052316
  source: Alliance formation with exclusion in the spatial public goods game | Physical Review E | 2017
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, mpcr, punishment_cost, punishment_tech
  findings: The paper finds that in spatial public goods games, the introduction of an excluder strategy (which monitors and excludes defectors at a cost) can lead to the elimination of...
  prediction_guidance: This paper provides indirect support for the idea that exclusion-based sanctions (a form of punishment) can be highly effective in structured populations, especially when...

- id: 10.1098_rspa.2022.0290
  source: Indirect exclusion can promote cooperation in repeated group interactions | Proceedings Of The Royal Society A-Mathematical Physical And Engineering Sciences | 2022
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, mpcr, show_n_rounds, show_other_summaries
  findings: The paper finds that indirect exclusion—where a game organizer probabilistically selects cooperators for future participation—can promote the stable coexistence of cooperators...
  prediction_guidance: This paper provides theoretical evidence that indirect exclusion mechanisms can increase the equilibrium level of cooperation in repeated public goods games, especially as the...

- id: 10.1088_2632-072X_ad0208
  source: Evolution of cooperation driven by sampling reward | Journal Of Physics-Complexity | 2023
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, mpcr, reward_exists, reward_cost, reward_tech
  findings: The paper finds that the sampling reward mechanism can effectively increase the average cooperation level in both PGG and CRD models. Higher reward thresholds and higher reward...
  prediction_guidance: This paper provides theoretical evidence that reward mechanisms (specifically, sampling reward) can increase cooperation rates in PGG-like environments, with effects moderated...

- id: 10.1038_s41598-023-43918-w
  source: Co-evolution of conditional cooperation and social norm | Scientific Reports | 2023
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr, show_other_summaries
  findings: The model finds that high initial cooperation and low contribution costs favor the emergence and stability of high cooperation and moderate norm sensitivity. When contribution...
  prediction_guidance: This paper provides indirect, mechanistic insight into how internalized norm enforcement (psychic costs) and conditional cooperation can sustain cooperation in repeated PGGs,...

- id: 10.1016_j.jtbi.2018.04.024
  source: Disseminators or silencers: The effect of information diffusion intensity on cooperation in public goods game | Journal Of Theoretical Biology | 2018
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr, show_other_summaries
  findings: The paper finds that the presence and type of information dissemination strongly affect the speed at which full cooperation is achieved in a spatial public goods game with...
  prediction_guidance: This paper does not provide direct evidence for predicting the effect of punishment on efficiency in public goods games, as it does not include a punishment or sanctioning...

- id: 10.1016_j.jtbi.2014.01.037
  source: Rewarding evolutionary fitness with links between populations promotes cooperation | Journal Of Theoretical Biology | 2014
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, mpcr, reward_exists, reward_tech
  findings: The paper finds that rewarding players whose utility exceeds a threshold by granting them external links to another population can significantly promote cooperation in both...
  prediction_guidance: This paper does not provide direct evidence for predicting the effect of punishment on efficiency in public goods games. It models a reward mechanism (external links for...

- id: 10.1016_j.chaos.2016.10.003
  source: An improved public goods game model with reputation effect on the spatial lattices | Chaos Solitons & Fractals | 2016
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr, show_n_rounds
  findings: The study finds that embedding a reputation effect into the utility function of agents in a spatial PGG model leads to a substantial increase in the stationary fraction of...
  prediction_guidance: This paper provides indirect evidence that reputation mechanisms can promote cooperation in spatial PGGs, but does not address punishment, sanctions, or efficiency outcomes....

- id: 10.1016_j.amc.2020.125835
  source: The emergence and implementation of pool exclusion in spatial public goods game with heterogeneous ability-to-pay | Applied Mathematics And Computation | 2021
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, mpcr, punishment_cost, punishment_tech
  findings: The study finds that introducing pool exclusion, where excluders pay a cost to exclude defectors from the public good, can significantly increase the level of cooperation in a...
  prediction_guidance: This paper provides indirect support for the idea that exclusionary sanctions (pool exclusion) can increase cooperation in spatial public goods games, especially under certain...

- id: 10.1016_j.amc.2017.04.017
  source: Publishing the donation list incompletely promotes the emergence of cooperation in public goods game | Applied Mathematics And Computation | 2017
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr, show_other_summaries
  findings: Publishing the donation list incompletely (only for those who contribute above a threshold) leads to higher total contributions and more equal contributions among players in a...
  prediction_guidance: This paper provides indirect evidence that social information mechanisms (such as partial publication of contribution lists) can increase cooperation in public goods games, but...

- id: 10.1103_PhysRevE.88.042128
  source: Effects of adaptive dynamical linking in networked games | Physical Review E | 2013
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr
  findings: The study finds that adaptive dynamical linking—where agents lengthen or shorten social ties based on whether their partners cooperate or defect—can dramatically increase the...
  prediction_guidance: This paper does not provide direct evidence for the prediction task of how punishment affects efficiency in public goods games. It is relevant as a demonstration that network...

- id: 10.1063_5.0235953
  source: Dynamic incentives and environmental feedback in public goods games: Promoting cooperation through critical thresholds | Chaos | 2025
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr
  findings: The study finds that introducing dynamic, group-level environmental feedback (bonuses or penalties based on collective contribution thresholds) in a spatial public goods game...
  prediction_guidance: This paper does not provide direct evidence for predicting the effect of punishment on efficiency in public goods games, as it does not include a punishment mechanism. Instead,...

- id: 10.1016_j.physleta.2019.126165
  source: The evolution of cooperation within the multigame environment based on the Particle Swarm Optimization algorithm | Physics Letters A | 2020
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr
  findings: The study finds that increasing the threshold required to initiate a public goods game (i.e., requiring more cooperators for the game to proceed) leads to higher stable levels...
  prediction_guidance: This paper provides indirect evidence that mechanisms which increase the cost of defection (here, via reputation loss) or require a threshold of cooperation to initiate public...

- id: 10.1016_j.physleta.2019.01.021
  source: Cooperation in the spatial public goods game with the second-order reputation evaluation | Physics Letters A | 2019
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr
  findings: The introduction of a second-order reputation evaluation mechanism in a spatial public goods game leads to a significant increase in the frequency of cooperators, especially as...
  prediction_guidance: This paper does not provide direct evidence for predicting the effect of punishment on efficiency in public goods games, as it does not include a punishment mechanism or report...

- id: 10.1016_j.physa.2012.12.022
  source: Emergence of cooperation in spatial public goods game with conditional participation | Physica A-Statistical Mechanics And Its Applications | 2013
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr
  findings: The study finds that introducing conditional participation (interpreted as a form of punishment) in a spatial public goods game can promote cooperation, but only within an...
  prediction_guidance: This paper is of limited direct use for predicting the effect of enabling standard punishment on efficiency in public goods games, as it does not study standard punishment...

- id: 10.1016_j.physa.2009.11.010
  source: Cooperation and charity in spatial public goods game under different strategy update rules | Physica A-Statistical Mechanics And Its Applications | 2010
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr
  findings: The study finds that charity (modeled as payoff transfer from egalitarians to the lowest-payoff neighbor) does not enhance cooperation under random selection update rules, but...
  prediction_guidance: This paper is not directly informative for predicting the effect of punishment on efficiency in public goods games, as it does not include punishment or report efficiency or...

- id: 10.1016_j.chaos.2025.116298
  source: The impact of memory reputation-induced tax and reward allocation on spatial public goods games | Chaos Solitons & Fractals | 2025
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr
  findings: The study finds that introducing a reputation-driven mechanism for adjusting local synergy factors in a spatial public goods game can significantly promote cooperation. The...
  prediction_guidance: This paper is not directly informative for predicting the effect of explicit punishment on efficiency in public goods games, as it does not include a punishment mechanism....

- id: 10.1016_j.amc.2020.125250
  source: The interplay of behaviors and attitudes in public goods game considering environmental investment | Applied Mathematics And Computation | 2020
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr
  findings: The introduction of an alliance strategy, where players pay an aid fee to help exploited allies, leads to a dramatic increase in the prevalence of cooperative behavior (C + A)...
  prediction_guidance: This paper provides indirect evidence that mechanisms analogous to mutual aid or alliance (distinct from punishment) can promote cooperation and increase the prevalence of...

- id: 10.1007_s13235-022-00485-5
  source: Complexity of Behavioural Strategies and Cooperation in the Optional Public Goods Game | Dynamic Games And Applications | 2023
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, all_or_nothing, mpcr, show_other_summaries
  findings: The study finds that in the OPGG, increasing the complexity of behavioral strategies (i.e., the ability to condition actions on more finely-grained reputational information)...
  prediction_guidance: This paper does not provide direct evidence for predicting the effect of punishment on efficiency in public goods games, as it does not include punishment or report efficiency...

- id: 10.3938_jkps.72.480
  source: Evolutionary Public Goods Game on Evolving Random Networks | Journal Of The Korean Physical Society | 2018
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, all_or_nothing, mpcr
  findings: The study finds that allowing informed cooperators to rewire their network connections at a cost can substantially increase the prevalence of cooperation in public goods games...
  prediction_guidance: This paper is not directly informative for predicting the effect of punishment on efficiency in public goods games, as it does not implement or analyze punishment or...

- id: 10.1103_PhysRevE.80.026121
  source: Partner selections in public goods games with constant group size | Physical Review E | 2009
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, mpcr
  findings: The study finds that, in public goods games with constant group size on networks, increasing group size generally promotes higher cooperation rates, especially when individuals...
  prediction_guidance: This paper does not provide direct evidence for predicting the effect of enabling explicit punishment on efficiency in public goods games. It is relevant for understanding how...

- id: 10.1017_ehs.2021.30
  source: False beliefs can bootstrap cooperative communities through social norms | Evolutionary Human Sciences | 2021
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: all_or_nothing, show_other_summaries
  findings: The paper finds that inaccurate, overly optimistic beliefs about the level of cooperation can bootstrap and sustain high cooperation in communities governed by conditional...
  prediction_guidance: This paper provides theoretical insight into how belief management and social norm dynamics can affect cooperation rates in public-goods-game-like environments, especially in...

- id: 10.1016_j.physa.2019.121767
  source: Compulsory persistent cooperation in continuous public goods games | Physica A-Statistical Mechanics And Its Applications | 2019
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: all_or_nothing, mpcr
  findings: The paper finds that persistent cooperation mechanisms in continuous public goods games can substantially increase the average cooperation level, especially when agents...
  prediction_guidance: This paper does not provide direct evidence for predicting the effect of punishment on efficiency in public goods games, as it does not include punishment or sanctions as a...

- id: 10.1063_1.3621719
  source: Cascading failures and the emergence of cooperation in evolutionary-game based models of social and economical networks | Chaos | 2011
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr
  findings: The study finds that in evolutionary games on networks (including PGG), introducing a survival threshold (death/bankruptcy) leads to catastrophic cascades when defection is...
  prediction_guidance: This paper does not provide direct evidence for predicting the effect of punishment on efficiency in public goods games. It does not manipulate or analyze punishment, nor does...

- id: 10.1007_s13235-025-00619-5
  source: Public Goods Games in Disease Evolution and Spread | Dynamic Games And Applications | 2025
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=exact | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, all_or_nothing, mpcr
  findings: The paper synthesizes theoretical and modeling work on PGGs in disease and cancer, highlighting how cooperation can be sustained or undermined depending on game parameters,...
  prediction_guidance: This paper provides conceptual background on how PGGs are used to model cooperation in health-related contexts and discusses mechanisms (including sanctions and incentives)...

- id: 10.1038_nature02978
  source: Indirect reciprocity can stabilize cooperation without the second-order free rider problem | Nature | 2004
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=close | punishment=adjacent | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr, punishment_cost, punishment_tech
  findings: The paper finds that linking collective action (public goods contribution) to indirect reciprocity (mutual aid based on reputation) can stabilize cooperation through exclusion...
  prediction_guidance: This paper provides theoretical support for the idea that indirect punishment via exclusion (rather than direct costly punishment) can stabilize cooperation in public goods...

- id: 10.1016_j.chaos.2023.113318
  source: Evolutionary games with environmental feedbacks under an external incentive mechanism | Chaos Solitons & Fractals | 2023
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=close | punishment=adjacent | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=mixed
  dimensions: player_count, num_rounds, all_or_nothing, mpcr, reward_exists, reward_cost
  findings: The paper finds that external incentives (subsidies/carbon credits) can promote cooperation and improve environmental quality in a spatial public goods game with environmental...
  prediction_guidance: This paper provides indirect but informative evidence for predicting the effect of external incentives (akin to rewards) on cooperation and group welfare in spatial public...

- id: 10.1103_PhysRevE.91.062802
  source: Evolutionary dynamics for persistent cooperation in structured populations | Physical Review E | 2015
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=close | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr, punishment_cost, punishment_tech
  findings: The study finds that persistent cooperators can invade and dominate structured populations (lattices) under more relaxed conditions than in well-mixed populations. The presence...
  prediction_guidance: This paper provides indirect evidence that mechanisms analogous to costly punishment (here, persistent cooperation) can suppress defection and promote cooperation in structured...

- id: 10.1038_s41598-019-44725-y
  source: Benefits of asynchronous exclusion for the evolution of cooperation in stochastic evolutionary optional public goods games | Scientific Reports | 2019
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=close | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, mpcr, punishment_cost, punishment_tech
  findings: The paper finds that asynchronous exclusion (where excluders act sequentially and avoid redundant costs) is more effective at promoting cooperation than synchronous exclusion...
  prediction_guidance: This paper provides indirect evidence about the effectiveness of exclusion (a sanctioning mechanism) in promoting cooperation in optional public goods games. While it does not...

- id: 10.1016_j.physa.2018.08.070
  source: The effect of link rewiring on a coevolutionary common pool resource game | Physica A-Statistical Mechanics And Its Applications | 2018
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=close | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, punishment_cost, punishment_tech
  findings: The study finds that allowing cooperators to rewire their links away from defectors (link rewiring) in a CPR game can prevent the collapse of cooperation and resource...
  prediction_guidance: This paper does not provide direct evidence for the effect of costly punishment on efficiency in public goods or CPR games. Instead, it analyzes a costless ostracism/reputation...

- id: 10.1093_bjps_axz022
  source: Blind Cooperation: The Evolution of Redundancy via Ignorance | British Journal For The Philosophy Of Science | 2021
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=close | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, all_or_nothing, mpcr, show_other_summaries
  findings: The paper finds that redundancy in group cooperation can evolve without targeted punishment or coercion if individuals are ignorant of others' strategies and/or face harsh...
  prediction_guidance: This paper provides theoretical context for how information availability and environmental harshness affect cooperation and redundancy in threshold public goods games. It...

- id: 10.1016_j.chaos.2016.08.015
  source: How the expanded crowd-funding mechanism of some southern rural areas in China affects cooperative behaviors in threshold public goods game | Chaos Solitons & Fractals | 2016
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=close | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: all_or_nothing, mpcr, show_other_summaries
  findings: The study finds that both publishing the list of cooperators and the presence of lobbyists can significantly increase the number of cooperators in a threshold public goods...
  prediction_guidance: This paper provides indirect evidence about how social recognition (publishing the list) and persuasive agents (lobbyists) can increase cooperation rates in threshold public...

- id: 10.1209_0295-5075_107_60005
  source: Climate collective risk dilemma with feedback of real-time temperatures | Epl | 2014
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=close | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, mpcr
  findings: The model demonstrates that coupling real-time environmental feedback (temperature) to payoffs in a threshold public goods game can promote and stabilize cooperation. When the...
  prediction_guidance: This paper is only indirectly relevant to predicting the effect of punishment on efficiency in public goods games. The 'punishment' mechanism is environmental (temperature rise...

- id: 10.1103_PhysRevE.86.036101
  source: Risk-driven migration and the collective-risk social dilemma | Physical Review E | 2012
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=close | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, mpcr
  findings: The study shows that risk-driven migration, where players move in response to the risk of collective failure, can substantially increase the fraction of cooperators in a...
  prediction_guidance: This paper is relevant for understanding how migration and risk of collective loss affect cooperation in public-goods-like environments, but it does not directly address the...

- id: 10.1016_j.jtbi.2005.10.024
  source: Spatial effects in social dilemmas | Journal Of Theoretical Biology | 2006
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=close | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, mpcr
  findings: The paper finds that spatial structure can both promote and inhibit cooperation in social dilemmas, depending on the type of game (prisoner's dilemma, snowdrift, by-product...
  prediction_guidance: This paper does not provide direct evidence for predicting the effect of punishment on efficiency in public goods games. However, it is informative about how spatial structure,...

- id: 10.1007_s10584-016-1838-3
  source: Cooperation studies of catastrophe avoidance: implications for climate negotiations | Climatic Change | 2017
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=close | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: chat
  findings: The paper finds that cooperation in collective-risk social dilemma games is strongly affected by perceived risk, inequality, uncertainty about thresholds, intergenerational...
  prediction_guidance: This paper provides indirect, contextual evidence about the importance of enforcement (punishment) mechanisms for sustaining cooperation in public-goods-like threshold games,...

- id: 10.1016_0303-2647(96)01604-8
  source: Evolutionary strategies of stochastic learning automata in the prisoner's dilemma | Biosystems | 1996
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=close | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, chat, all_or_nothing, punishment_cost, reward_exists
  findings: The paper argues that cooperation in resource dilemmas (including public goods and commons dilemmas) is shaped by individual value orientation (pro-social vs egoistic),...
  prediction_guidance: This paper provides conceptual background on the psychological mechanisms that may moderate the effect of punishment, reward, and uncertainty on cooperation in...

- id: 10.1016_j.amc.2022.127578
  source: Unfairness promotes the evolution of cooperation | Applied Mathematics And Computation | 2023
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=close | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, all_or_nothing, mpcr, punishment_cost, punishment_tech
  findings: The study finds that allowing individuals to reject unfair resource allocations (interpreted as a form of punishment) leads to higher levels of cooperation, especially when...
  prediction_guidance: This paper provides indirect evidence that the ability to reject unfair offers (a form of costly punishment) can promote cooperation in public-goods-like games, especially when...

- id: 10.1007_978-3-319-29354-7_9
  source:  |  | 
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=close | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, mpcr, punishment_cost, punishment_tech
  findings: The paper finds that cognitive mechanisms such as intention recognition, commitment, apology, and forgiveness can reinforce the emergence and stability of cooperation in...
  prediction_guidance: This paper provides theoretical and simulation-based insights into how various cognitive and social mechanisms (commitment, apology, forgiveness, restriction of benefits) can...

- id: 10.1146_annurev-psych-020821-110044
  source: Human Cooperation and the Crises of Climate Change, COVID-19, and Misinformation | Annual Review Of Psychology | 2022
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=close | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, punishment_cost, show_other_summaries
  findings: The review synthesizes evidence that mechanisms such as reputation, reciprocity, and social preferences (including egalitarianism and parochialism) are central to sustaining...
  prediction_guidance: This review is useful for understanding the mechanisms by which punishment, reputation, and observability can promote cooperation in public goods games and related social...

- id: 10.1016_j.jtbi.2010.02.035
  source: Group selection: The quest for social preferences | Journal Of Theoretical Biology | 2010
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=close | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, mpcr
  findings: The paper finds that group selection can, under certain conditions, support the evolution of cooperation and altruism in public-goods-like and Prisoner's Dilemma games. Three...
  prediction_guidance: This paper provides theoretical context for how group structure, migration, and mechanisms like conformity or signalling can affect the evolution of cooperation in...

- id: 10.1111_eva.12303
  source: Principles of cooperation across systems: from human sharing to multicellularity and cancer | Evolutionary Applications | 2016
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=close | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count
  findings: The paper identifies three general principles that facilitate cooperation: (1) the ability to 'Walk Away' from uncooperative partners, (2) need-based resource transfers, and...
  prediction_guidance: This paper provides conceptual and theoretical background on mechanisms that support cooperation, such as partner choice (Walk Away) and cheater suppression, which are relevant...

- id: 10.1007_s10955-012-0679-3
  source: A Simple Model of Stability in Critical Mass Dynamics | Journal Of Statistical Physics | 2013
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=close | punishment=adjacent | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count
  findings: The paper finds that weakly self-reinforcing collective action systems (where incentives to participate peak before full participation, allowing for free riders) are more...
  prediction_guidance: This paper provides theoretical insight into the trade-off between maximizing participation (and thus, potentially, efficiency) and ensuring long-term stability in collective...

- id: 10.1016_j.chaos.2024.115250
  source: The influence of the heterogeneities of social institutions and individuals' tendency to establish social institutions on cooperation | Chaos Solitons & Fractals | 2024
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=more_positive
  dimensions: player_count, num_rounds, mpcr, punishment_cost, punishment_tech, reward_exists
  findings: The study finds that introducing heterogeneous social institutions (pool punishment, anti-social punishment, and social security/reward) in a spatial prisoner's dilemma...
  prediction_guidance: This paper provides theoretical and simulation-based evidence that the design of punishment and reward institutions—including their cost, effectiveness, and resource allocation...

- id: 10.1007_s11229-022-03743-6
  source: When it pays to punish in the evolution of honesty and cooperation | Synthese | 2022
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=mixed
  dimensions: player_count, num_rounds, all_or_nothing, mpcr, punishment_cost, punishment_tech
  findings: The paper uses evolutionary game theory and simulations to analyze how different forms of costly punishment (punishing lying vs. punishing defection) affect the evolution of...
  prediction_guidance: This paper provides important cautionary evidence for predicting the effect of punishment on efficiency in games with multi-stage cooperation (e.g., signaling plus donation)....

- id: 10.1140_epjb_s10051-021-00212-w
  source: Reputational preference-based payoff punishment promotes cooperation in spatial social dilemmas | European Physical Journal B | 2021
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=more_positive
  dimensions: player_count, num_rounds, all_or_nothing, punishment_cost, punishment_tech, show_n_rounds
  findings: The paper finds that introducing a reputational preference-based payoff punishment mechanism in spatial social dilemmas (PDG and SDG) significantly increases the fraction of...
  prediction_guidance: This paper provides strong theoretical/simulation evidence that introducing a costly, reputation-based punishment mechanism in spatial social dilemmas increases cooperation...

- id: 10.1098_rspb.2016.0488
  source: Coevolution between positive reciprocity, punishment, and partner switching in repeated interactions | Proceedings Of The Royal Society B-Biological Sciences | 2016
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr, punishment_cost, punishment_tech
  findings: The study finds that in repeated Prisoner's Dilemma games, the evolutionary success of punishment, positive reciprocity, and partner switching depends on the number of rounds,...
  prediction_guidance: This paper provides indirect but informative evidence for predicting the effect of punishment on efficiency in repeated Prisoner's Dilemma-like environments. It suggests that...

- id: 10.1016_j.physleta.2020.126723
  source: Cooperation under institutional incentives with perfect and imperfect observation | Physics Letters A | 2020
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=more_positive
  dimensions: player_count, all_or_nothing, punishment_cost, punishment_tech, reward_exists, reward_cost
  findings: Institutional punishment (and reward), funded by a tax on positive payoffs, can promote the evolutionary emergence of cooperation in a well-mixed prisoner's dilemma. The...
  prediction_guidance: This paper provides theoretical evidence that institutional punishment (with costs funded by a tax on payoffs) can increase the evolutionary success of cooperation, especially...

- id: 10.1016_j.jtbi.2008.09.015
  source: Direct reciprocity with costly punishment: Generous tit-for-tat prevails | Journal Of Theoretical Biology | 2009
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, punishment_cost, punishment_tech, show_n_rounds
  findings: The paper shows that in repeated Prisoner's Dilemma games with costly punishment, the addition of a punishment option does not increase cooperation or group payoffs in...
  prediction_guidance: For the prediction task, this paper suggests that enabling costly punishment in a repeated two-player PD-like environment does not increase efficiency or group payoff,...

- id: 10.1177_00375497231171138
  source: Integrated analysis of employee cooperation and conflict behaviors in the context of digital technology | Simulation-Transactions Of The Society For Modeling And Simulation International | 2023
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=more_positive
  dimensions: player_count, num_rounds, all_or_nothing, punishment_cost, punishment_tech, show_n_rounds
  findings: The paper finds that the presence and magnitude of punishment (penalty for conflict) is a key determinant of stable cooperation in a group setting modeled as an evolutionary...
  prediction_guidance: This paper provides strong theoretical and simulation-based evidence that increasing the penalty for non-cooperation (punishment) above a critical threshold (half the cost of...

- id: 10.18564_jasss.3336
  source: Cooperation Via Intimidation: An Emergent System of Mutual Threats can Maintain Social Order | Jasss-The Journal Of Artificial Societies And Social Simulation | 2017
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=more_positive
  dimensions: player_count, all_or_nothing, punishment_cost, punishment_tech, show_other_summaries, show_punishment_id
  findings: The study finds that in agent-based models of repeated Prisoner's Dilemma with post-game fighting (punishment), aggressive strategies (harassers) become evolutionarily stable...
  prediction_guidance: This paper provides indirect but informative evidence that enabling punishment in repeated PD-like environments can increase cooperation rates (and thus efficiency) compared to...

- id: 10.1177_1059712316653451
  source: A synergy of costly punishment and commitment in cooperation dilemmas | Adaptive Behavior | 2016
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, punishment_cost, punishment_tech, show_n_rounds
  findings: The paper finds that a strategy combining prior commitment and costly punishment (CPP) can achieve higher frequencies of cooperation than either mechanism alone, across a wide...
  prediction_guidance: This paper provides theoretical evidence that combining commitment and punishment mechanisms can outperform either alone in promoting cooperation, especially when commitment is...

- id: 10.1016_j.knosys.2017.05.016
  source: Evolutionary dynamics of strategies for threshold snowdrift games on complex networks | Knowledge-Based Systems | 2017
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr, punishment_cost, punishment_tech
  findings: The paper finds that introducing punishment in threshold snowdrift games increases the evolutionary advantage of cooperation over defection, especially when punishment cost is...
  prediction_guidance: This paper provides indirect evidence that punishment can increase cooperation rates in threshold public-goods-like games, especially when punishment is effective and not too...

- id: 10.1016_j.jtbi.2014.07.021
  source: Selfish punishment with avoiding mechanism can alleviate both first-order and second-order social dilemma | Journal Of Theoretical Biology | 2014
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, punishment_cost, punishment_tech, show_punishment_id
  findings: The study finds that introducing selfish punishment with an avoiding mechanism into a spatial prisoner's dilemma game can alleviate both first-order and second-order social...
  prediction_guidance: This paper provides indirect support for the idea that punishment (especially when including mechanisms for selfish punishment and avoidance) can promote cooperation and reduce...

- id: 10.1098_rspb.2013.2661
  source: High strength-of-ties and low mobility enable the evolution of third-party punishment | Proceedings Of The Royal Society B-Biological Sciences | 2014
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=more_positive
  dimensions: all_or_nothing, punishment_cost, punishment_tech, show_other_summaries, show_punishment_id
  findings: The paper finds that responsible third-party punishment (3PP) can evolve and sustain cooperation in structured populations when social-structural constraints are high (i.e.,...
  prediction_guidance: This paper provides strong theoretical evidence that the effectiveness of punishment in promoting cooperation and increasing pay-off (and thus efficiency) depends critically on...

- id: 10.1209_0295-5075_121_48005
  source: Evolutionary prisoner's dilemma games on the network with punishment and opportunistic partner switching | Epl | 2018
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=more_positive
  dimensions: player_count, num_rounds, all_or_nothing, punishment_cost, punishment_tech
  findings: The study finds that both punishment and partner switching (opportunistic rewiring of social ties) can support the evolution of cooperation in a networked prisoner's dilemma....
  prediction_guidance: This paper provides indirect but informative evidence for the prediction task. While it does not report group efficiency or total welfare directly, it shows that both...

- id: 10.1007_s11432-023-4170-3
  source: Exit options sustain altruistic punishment and decrease the second-order free-riders, but it is not a panacea | Science China-Information Sciences | 2025
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=unclear
  dimensions: player_count, num_rounds, all_or_nothing, punishment_cost, punishment_tech
  findings: The paper finds that adding an exit option to a prisoner's dilemma with altruistic punishment changes the evolutionary dynamics. In well-mixed populations, exiters replace...
  prediction_guidance: This paper provides indirect evidence about how the presence and incentive level of an exit option (voluntary participation) can affect the evolutionary stability of punishment...

- id: 10.1037_pspa0000301
  source: The Importance of Being Unearnest: Opportunists and the Making of Culture | Journal Of Personality And Social Psychology | 2022
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=less_positive
  dimensions: player_count, num_rounds, show_n_rounds, show_other_summaries
  findings: The paper finds that (1) more severe punishment for noncooperation reduces the amount of voluntary cooperation in a population, both in agent-based simulations and in a human...
  prediction_guidance: This paper provides strong evidence that, in environments structurally similar to public goods games with punishment, increasing the severity of punishment or raising the bar...

- id: 10.3389_fphy.2018.00156
  source: Rare Third-Party Punishment Promotes Cooperation in Risk-Averse Social Learning Dynamics | Frontiers In Physics | 2019
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=more_positive
  dimensions: player_count, all_or_nothing, punishment_cost, punishment_tech
  findings: The paper finds that risk-averse individuals in evolutionary social dilemma games can achieve stable, high levels of cooperation with only rare third-party punishment. Both...
  prediction_guidance: This paper provides strong theoretical support that, in two-player social dilemma games with third-party punishment, enabling punishment (even rarely) can substantially...

- id: 10.1016_j.chaos.2018.03.029
  source: Sanctions triggered by jealousy help promote the cooperation in spatial prisoner's dilemma games | Chaos Solitons & Fractals | 2018
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=unclear
  dimensions: player_count, all_or_nothing, punishment_cost, punishment_tech
  findings: The study finds that jealousy-motivated sanctions (where agents punish neighbors with higher payoffs, regardless of strategy) can promote cooperation in spatial prisoner's...
  prediction_guidance: This paper provides indirect evidence for the effect of punishment on efficiency in public-goods-like environments, but the model is a spatial prisoner's dilemma, not a public...

- id: 10.1016_j.jtbi.2015.09.009
  source: Promote or hinder? The role of punishment in the emergence of cooperation | Journal Of Theoretical Biology | 2015
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, punishment_cost, punishment_tech
  findings: The paper finds that the effectiveness of punishment in promoting cooperation depends critically on the pattern of punishment and the presence of anti-social punishment....
  prediction_guidance: This paper provides indirect but informative theoretical evidence about how punishment design (centralized vs decentralized, presence of anti-social punishment) can affect the...

- id: 10.1016_j.physleta.2014.11.035
  source: Emergence of parochial altruism in well-mixed populations | Physics Letters A | 2015
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, punishment_cost, punishment_tech
  findings: The paper finds that parochial altruism (in-group cooperation, out-group punishment) is favored by selection under certain parameter regimes, especially when the benefit of...
  prediction_guidance: This paper provides indirect support for predicting the effect of punishment on efficiency in public-goods-like environments, by showing that punishment (when effective and not...

- id: 10.1038_373209a0
  source: PUNISHMENT IN ANIMAL SOCIETIES | Nature | 1995
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: punishment_cost, punishment_tech
  findings: Theoretical models show that punishment can be stable and effective in animal societies, especially when dominants can punish subordinates at low cost and with high impact....
  prediction_guidance: This paper provides conceptual and theoretical support for the idea that punishment can enforce cooperation and deter selfishness, which is relevant to predicting the effects...

- id: 10.1155_2022_7259257
  source: Beyond Reciprocity: Forgiveness, Generosity, and Punishment in Continuing Dyadic Interactions | Journal Of Theoretical Social Psychology | 2022
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=close
  outcomes: primary=non_payoff_behavior | overall_effect=less_positive
  dimensions: player_count, punishment_cost
  findings: The paper synthesizes evidence from simulation and behavioral studies of dyadic repeated games (mainly Prisoner's Dilemma and its continuous variants) to argue that punishment,...
  prediction_guidance: This paper provides strong theoretical and literature-based evidence that, in dyadic repeated games (especially noisy or continuous-choice environments), enabling punishment is...

- id: 10.1016_j.physa.2022.128165
  source: Reward and Punishment Mechanism with weighting enhances cooperation in evolutionary games | Physica A-Statistical Mechanics And Its Applications | 2022
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, punishment_cost, punishment_tech, reward_exists
  findings: The study finds that the introduction of a reward and punishment mechanism with weighting (RPMW) increases the frequency of cooperation in evolutionary games (PDG, SDG, SHG),...
  prediction_guidance: This paper provides indirect evidence that punishment (and reward) mechanisms can increase cooperation rates in social dilemma games, and that the effect is stronger with...

- id: 10.1016_j.amc.2025.129309
  source: Effects of an update mechanism based on combinatorial memory and high-reputation learning objects on the evolution of | Applied Mathematics And Computation | 2025
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, punishment_cost, punishment_tech, reward_exists
  findings: The introduction of a social monitoring mechanism (SMM) that rewards judges based on the observed cooperation rate among participants leads to higher levels of cooperation and...
  prediction_guidance: This paper provides indirect evidence that mechanisms which reward third-party punishers based on group cooperation rates can increase cooperation and reduce corruption in...

- id: 10.1098_rspb.2018.1508
  source: The emergence and selection of reputation systems that drive cooperative behaviour | Proceedings Of The Royal Society B-Biological Sciences | 2018
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr, punishment_cost, punishment_tech
  findings: The paper finds that in a population of initially non-cooperative individuals, a reputation system based on punishment is likely to emerge first and drive the initial evolution...
  prediction_guidance: This paper provides indirect support for the idea that punishment-based reputation systems can help establish cooperation in repeated social dilemmas, especially when...

- id: 10.1016_j.jtbi.2005.01.006
  source: Altruism may arise from individual selection | Journal Of Theoretical Biology | 2005
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, chat, all_or_nothing, punishment_cost, punishment_tech
  findings: The paper finds that strong reciprocity (altruistic punishment) can arise and persist in agent-based evolutionary models of the Ultimatum Game under individual selection,...
  prediction_guidance: This paper provides theoretical support for the possibility that punishment (in the form of rejection of unfair offers) can evolve and persist under individual selection in...

- id: 10.3389_fpubh.2022.881330
  source: Supervision for the Public Health Services for Older Adults Under the Background of Government Purchasing: An Evolutionary Game Analysis Framework | Frontiers In Public Health | 2022
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, punishment_cost, punishment_tech, reward_exists
  findings: The paper finds that in a principal-agent setting with information asymmetry, static punishment or reward mechanisms are insufficient to ensure full compliance...
  prediction_guidance: This paper provides theoretical support for the idea that the effectiveness of punishment in promoting cooperation (or self-discipline) depends on the design of the sanctioning...

- id: 10.1086_690066
  source: Networks and Interethnic Cooperation | Journal Of Politics | 2017
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, punishment_cost, punishment_tech, show_n_rounds
  findings: The paper finds that the ability of groups to enforce cooperation through peer punishment depends critically on the structure of their internal communication networks....
  prediction_guidance: This paper provides theoretical guidance on how network structure moderates the effectiveness of peer punishment in sustaining cooperation in repeated social dilemmas. For...

- id: 10.1073_pnas.1704032114
  source: Evolution of flexibility and rigidity in retaliatory punishment | Proceedings Of The National Academy Of Sciences Of The United States Of America | 2017
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, punishment_cost, punishment_tech, show_n_rounds
  findings: The paper finds that when punishment is costly, flexible (learning-based) victims are less likely to learn to punish, making them more vulnerable in repeated interactions. This...
  prediction_guidance: This paper provides theoretical and simulation-based evidence about the evolution of punishment strategies in repeated dyadic games, focusing on the interplay between learning...

- id: 10.1017_s0043887117000181
  source: WHY THE WEST BECAME WILD Informal Governance with Incomplete Networks | World Politics | 2017
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, punishment_cost, punishment_tech, show_n_rounds
  findings: The paper finds that the ability of peer punishment to sustain cooperation depends critically on the social network structure and the reach of gossip. Incomplete networks with...
  prediction_guidance: This paper provides theoretical insight into how network structure and information transmission affect the limits of peer punishment in sustaining cooperation. It is relevant...

- id: 10.1016_j.physa.2019.123410
  source: Evolutionary traveler's dilemma game based on particle swarm optimization | Physica A-Statistical Mechanics And Its Applications | 2020
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, punishment_cost, punishment_tech, reward_exists
  findings: The paper finds that using a PSO-based learning mechanism in the traveler's dilemma game leads to higher levels of cooperation (higher average claims) compared to traditional...
  prediction_guidance: This paper provides indirect evidence about how learning mechanisms and the structure of reward/punishment in a traveler's dilemma game (an adjacent but not exact variant of...

- id: 10.1016_j.chaos.2022.112432
  source: Impacts of special cooperation strategy with reward and punishment mechanism on cooperation evolution | Chaos Solitons & Fractals | 2022
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, punishment_cost, punishment_tech, reward_exists
  findings: The paper finds that introducing special cooperators who can both reward and punish leads to a variety of stable states, including coexistence of all three strategies or pairs...
  prediction_guidance: This paper provides indirect, mechanistic evidence that punishment (especially when combined with reward) can promote the prevalence of cooperative strategies in spatial...

- id: 10.1016_j.amc.2024.128864
  source: Suppressing defection by increasing temptation: The impact of smart cooperators on a social dilemma situation | Applied Mathematics And Computation | 2024
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, punishment_cost, punishment_tech, reward_exists
  findings: The study finds that adding a 'smart cooperator' strategy (who both punishes defectors and rewards cooperators, at a cost) to a spatial prisoner's dilemma model leads to cyclic...
  prediction_guidance: This paper provides indirect, mechanistic insight into how punishment and reward mechanisms interact in a spatial social dilemma with multiple strategies, but does not provide...

- id: 10.1016_j.amc.2022.127612
  source: How punishing evil and promoting good promotes cooperation in social dilemma | Applied Mathematics And Computation | 2023
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, punishment_cost, punishment_tech, reward_exists
  findings: The paper finds that the introduction of a 'punishing evil and promoting good' strategy can promote the survival of cooperation in social dilemmas. Increasing punishment...
  prediction_guidance: This paper provides theoretical evidence that both punishment and reward mechanisms can promote cooperation in social dilemma settings, and that their effects are...

- id: 10.1007_s10668-024-05335-5
  source: Dynamic strategies for collaborative governance of rural environments: a simulation study on the most effective mechanisms | Environment Development And Sustainability | 2024
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, punishment_cost, punishment_tech, reward_exists
  findings: The paper finds that under a static reward and punishment mechanism (SRPM), the system does not reach a stable equilibrium; strategies of all parties fluctuate periodically....
  prediction_guidance: This paper provides indirect support for the prediction task by showing that dynamic, behavior-dependent punishment mechanisms (analogous to more flexible or responsive...

- id: 10.1371_journal.pone.0124513
  source: Can Centralized Sanctioning Promote Trust in Social Dilemmas? A Two-Level Trust Game with Incomplete Information | Plos One | 2015
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, punishment_cost, punishment_tech, show_n_rounds
  findings: The paper finds that introducing a centralized sanctioning authority into a repeated trust game with incomplete information can increase trust and reciprocity, especially when...
  prediction_guidance: This paper provides theoretical support for the idea that adding a centralized punishment mechanism to a trust-based social dilemma can increase trust and cooperation,...

- id: 10.1371_journal.pone.0085531
  source: Recidivism and Rehabilitation of Criminal Offenders: A Carrot and Stick Evolutionary Game | Plos One | 2014
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, punishment_cost, punishment_tech, reward_exists, reward_cost
  findings: The model demonstrates that neither punishment alone nor rehabilitation alone is optimal for reducing crime and recidivism. Instead, the best outcomes (highest ratio of...
  prediction_guidance: This paper provides indirect, adjacent evidence for the prediction task. It supports the idea that the effect of punishment on group-level outcomes (here, the ratio of reformed...

- id: 10.1140_epjb_s10051-021-00185-w
  source: Evolutionary dynamics of trust in the N-player trust game with individual reward and punishment | European Physical Journal B | 2021
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, mpcr, punishment_cost, punishment_tech, reward_exists, reward_cost
  findings: The introduction of individual reward and punishment in the N-player trust game can promote the stable coexistence of investors and trustworthy trustees, which is interpreted...
  prediction_guidance: This paper provides indirect theoretical support for the idea that introducing punishment (and especially reward) mechanisms can promote cooperation-like behavior in...

- id: 10.1109_access.2021.3084342
  source: Research on the Evolution Path and Influence Factors of Core Enterprise Oriented Entrepreneurship Ecosystem Under the Government Regulation | Ieee Access | 2021
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, all_or_nothing, punishment_cost, punishment_tech, reward_exists, reward_cost
  findings: The paper finds that the presence and magnitude of punishment (by core enterprises to start-ups, and by government to both) increases the likelihood and speed of positive...
  prediction_guidance: This paper provides indirect, theoretical support for the idea that punishment mechanisms (and their cost/benefit structure) can promote positive, cooperative, or pro-social...

- id: 10.1063_5.0232207
  source: Third party interventions promote cooperation on the interdependent networks: A perspective based on prospect theory | Chaos | 2024
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, punishment_cost, punishment_tech, reward_exists
  findings: The introduction of third-party intervention (punishment and/or reward) in a networked PD/SD game increases the fraction of cooperators in both the intervention and dispute...
  prediction_guidance: This paper provides strong evidence that third-party punishment and reward mechanisms can increase cooperation rates in networked social dilemmas, and that the effect is...

- id: 10.1016_j.evolhumbehav.2004.08.001
  source: False friends are worse than bitter enemies: Altruistic punishment of in-group members | Evolution And Human Behavior | 2004
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, mpcr, punishment_cost, punishment_tech
  findings: The bidirectional supervision mechanism, where players can check and avoid corrupt umpires, is effective at suppressing both corruption and defection in a spatial donation game...
  prediction_guidance: This paper provides indirect support for the prediction task by showing that the design of punishment, bribe, tax, and checking cost parameters can strongly affect the...

- id: 10.1016_j.amc.2015.01.040
  source: Group-separations based on the repeated prisoners' dilemma games | Applied Mathematics And Computation | 2015
  type: theory | empirical=N/A | experimental=N/A
  relevance: pgg=adjacent | punishment=exact | payoff=adjacent
  outcomes: primary=non_payoff_behavior | overall_effect=N/A
  dimensions: player_count, num_rounds, all_or_nothing, punishment_cost, punishment_tech, show_n_rounds
  findings: The paper provides a theoretical framework for understanding how the ability to sustain cooperation via punishment (trigger strategies) in repeated pairwise prisoners' dilemma...
  prediction_guidance: This paper is of limited direct use for predicting the effect of punishment on efficiency in public goods games or their variants, as it does not analyze efficiency or payoff...


        ----------