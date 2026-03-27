# Card Snippet Examples

## Most Relevant (heuristic ranking)

### PGG_MS_202502 (score=35.0)

```text
[Paper] PGG_MS_202502
Type: empirical | empirical=experimental | experimental=lab_experiment
Relevance: pgg_or_variant=exact; punishment_or_sanctions=exact; efficiency_or_related_payoff_outcome=exact
Outcomes: primary=efficiency_or_payoff; overall_effect_on_efficiency_or_payoff=mixed
Informative dimensions:
- all_or_nothing [informative_direct; effect=mixed; basis=manipulated]; notes=Contribution type (variable vs. all-or-nothing) was manipulated. Its effect on punishment's efficiency impact depends on interactions with contribution framing and peer outcome visibility.
- chat [informative_direct; effect=more_positive; basis=manipulated]; notes=Communication (chat) was systematically manipulated (enabled/disabled) and is the single most important predictor of punishment's positive effect on efficiency. When chat is enabled, punishment is much more likely to improve efficiency.
- default_contrib [informative_direct; effect=mixed; basis=manipulated]; notes=Contribution framing (opt-in vs. opt-out) was manipulated. Its effect on punishment's efficiency impact is contingent on contribution type and peer outcome visibility.
- mpcr [informative_direct; effect=more_positive; basis=manipulated]; notes=MPCR (marginal per capita return) was varied (0.06–0.7). Higher MPCR consistently enhances punishment's effect on efficiency, but its predictive importance is small relative to other features.
- num_rounds [informative_direct; effect=mixed; basis=manipulated]; notes=Number of rounds (game length) was systematically varied (1–30 rounds) and is a key moderator. Longer games increase punishment effectiveness only when communication is available; otherwise, the effect is weaker or absent.
- player_count [informative_direct; effect=mixed; basis=manipulated]; notes=Group size (player count) was systematically varied from 2 to 20 and included as a model feature. It was not among the most important predictors of punishment's effect on efficiency, but some heterogeneity is attributable to it.
- punishment_cost [informative_direct; effect=unclear; basis=manipulated]; notes=Punishment cost (peer incentive cost) was varied (1–4 coins per unit). However, punishment cost and impact (technology) had little predictive importance for efficiency outcomes.
- punishment_tech [informative_direct; effect=unclear; basis=manipulated]; notes=Punishment impact per unit cost (punishment technology) was varied (1–4 coins per unit). It had the smallest effect on predictive performance among all features.
- reward_cost [informative_direct; effect=unclear; basis=manipulated]; notes=Reward cost (peer incentive cost) was varied (1–4 coins per unit). Its effect is not highlighted as important for predicting efficiency outcomes.
- reward_exists [informative_direct; effect=more_positive; basis=manipulated]; notes=Reward availability was manipulated (enabled/disabled). The presence of a reward mechanism consistently enhanced punishment's effect on efficiency.
- reward_tech [informative_direct; effect=unclear; basis=manipulated]; notes=Reward impact per unit cost (reward technology) was varied (0.5–1.5 coins per unit). Its effect is not highlighted as important for predicting efficiency outcomes.
- show_n_rounds [informative_direct; effect=unclear; basis=manipulated]; notes=Horizon knowledge (whether players know the total number of rounds) was manipulated. Its effect on punishment's efficiency impact is not highlighted as important.
- show_other_summaries [informative_direct; effect=mixed; basis=manipulated]; notes=Peer outcome visibility (showing others' earnings, punishments, rewards) was manipulated. Its effect on punishment's efficiency impact is contingent and interacts with other features (e.g., it can dampen the positive effect of communication and game length).
- show_punishment_id [informative_direct; effect=unclear; basis=manipulated]; notes=Actor anonymity (whether the identity of punishers/rewarders is revealed) was manipulated. Its effect on efficiency is not highlighted as important for prediction.
Overall summary:
This large-scale integrative experiment systematically varied 14 public goods game parameters across 360 unique conditions to assess the effect of punishment on group efficiency. While punishment consistently increased contributions, its effect on efficiency (group payoff relative to full cooperation) was highly heterogeneous: in some settings, punishment increased efficiency, but in many others, it reduced it, often substantially. The direction and magnitude of punishment's effect on efficiency depended on complex interactions between game design features, with communication, contribution framing, contribution type, game length, peer outcome visibility, and reward availability emerging as key moderators.
Paper findings:
Punishment in public goods games robustly increases contributions but has a highly variable effect on efficiency, ranging from strongly positive to strongly negative depending on the game context. On average, punishment reduced normalized efficiency, but this average masked substantial heterogeneity: in some parameter settings, punishment improved group welfare, while in others it led to large efficiency losses. The most important predictors of punishment's effect on efficiency were the availability of communication (chat), contribution framing (opt-in vs. opt-out), contribution type (variable vs. all-or-nothing), game length (number of rounds), peer outcome visibility, and the presence of a reward mechanism. These features often interacted, such that, for example, longer games only increased punishment effectiveness when communication was available. Predictive models using these parameters and control efficiency outperformed both laypeople and domain experts in forecasting the effect of punishment on efficiency in new settings.
Decision support:
This paper provides direct, high-quality evidence for predicting the effect of punishment on efficiency in public goods games as a function of game design dimensions and control efficiency. It demonstrates that the effect of punishment is not uniform but depends on complex, sometimes non-intuitive interactions among design features. The most predictive dimensions for efficiency outcomes are communication, contribution framing, contribution type, game length, peer outcome visibility, and reward availability. The paper's dataset and predictive models can be used to estimate treatment efficiency in new PGG designs, and the findings caution against assuming that punishment will always improve welfare, even when it increases cooperation. For prediction tasks, the paper supports using machine learning models trained on these dimensions and control efficiency, rather than relying on expert intuition or simple heuristics.
Key claims:
Punishment consistently increases contributions in public goods games, but its effect on efficiency (group payoff) is highly heterogeneous and can be either positive or negative depending on the game context. [support=high] [refs=Results: Heterogeneous effects of punishment across experimental conditions | Figure 2 | Discussion] || On average, punishment reduces normalized efficiency, but this average masks substantial variation: in some settings, punishment increases efficiency, while in others it leads to large efficiency losses. [support=high] [refs=Results: Heterogeneous effects of punishment across experimental conditions | Figure 2B–F] || The most important predictors of punishment's effect on efficiency are communication, contribution framing, contribution type, game length, peer outcome visibility, and reward availability, with many of these features interacting in complex ways. [support=high] [refs=Results: Key PGG design dimensions for predicting punishment effectiveness | Figure 4 | Figure 5] || Predictive models using game design parameters and control efficiency can forecast the effect of punishment on efficiency in new settings more accurately than both domain experts and laypeople. [support=high] [refs=Results: Predicting punishment effectiveness in new experiments | Figure 3] || Punishment technology (cost and impact per unit) is less important for predicting efficiency outcomes than contextual features like communication and contribution framing. [support=medium] [refs=Results: Punishment parameters matter less than expected | Figure 4A]
Important limitations:
The study holds population characteristics constant (primarily online US/UK participants), so findings may not generalize to other populations. | Although 14 design parameters were varied, the design space is not exhaustive; other potentially relevant features (e.g., more nuanced communication types, reputation systems) were not included. | The study focuses on short- to medium-term repeated games (up to 30 rounds); very long-term or one-shot effects may differ. | Interpretation of higher-order interactions is challenging, and the mechanisms underlying some observed effects remain unclear. | The predictive models are trained and validated on the sampled design space; extrapolation to very different or extreme parameter settings may be unreliable.
```

### 10.1007_s11403-022-00363-8 (score=34.929)

```text
[Paper] 10.1007_s11403-022-00363-8
Type: empirical | empirical=experimental | experimental=lab_experiment
Relevance: pgg_or_variant=exact; punishment_or_sanctions=exact; efficiency_or_related_payoff_outcome=exact
Outcomes: primary=efficiency_or_payoff; overall_effect_on_efficiency_or_payoff=less_positive
Informative dimensions:
- all_or_nothing [informative_direct; effect=N/A; basis=manipulated]; notes=Contribution choices are continuous (0-20 tokens per period).
- chat [informative_direct; effect=N/A; basis=manipulated]; notes=Communication between participants is not allowed.
- mpcr [informative_direct; effect=N/A; basis=manipulated]; notes=Heterogeneous: one member MPCR=0.9, two members MPCR=0.4.
- num_rounds [informative_direct; effect=N/A; basis=manipulated]; notes=Each session consists of 20 periods (10 control, 10 treatment).
- player_count [informative_direct; effect=N/A; basis=manipulated]; notes=All groups have 3 players.
- punishment_cost [informative_direct; effect=N/A; basis=manipulated]; notes=Each punishment point costs 1 token to assigner, reduces target's earnings by 3 tokens.
- punishment_tech [informative_direct; effect=N/A; basis=manipulated]; notes=Punishment effectiveness is 3:1 (each point costs 1, reduces target by 3).
- reward_cost [informative_direct; effect=N/A; basis=manipulated]; notes=Each reward point costs 1 token to assigner, increases target's earnings by 3 tokens.
- reward_exists [informative_direct; effect=N/A; basis=manipulated]; notes=Reward is available in a separate treatment, not in the punishment condition.
- reward_tech [informative_direct; effect=N/A; basis=manipulated]; notes=Reward effectiveness is 3:1 (each point costs 1, increases target by 3).
- show_n_rounds [informative_direct; effect=N/A; basis=manipulated]; notes=Participants know the number of periods (10 per block, 20 total).
- show_other_summaries [informative_direct; effect=N/A; basis=manipulated]; notes=At the end of each period, participants see each group member's contributions and earnings.
- show_punishment_id [informative_direct; effect=N/A; basis=manipulated]; notes=Participants see the total amount of points assigned by the two other group members combined, but not who assigned how much.
Overall summary:
In a lab public goods game with heterogeneous MPCRs (one high-benefit member, two low-benefit members), the introduction of punishment opportunities does not significantly increase group efficiency or average earnings compared to the control (no incentives) condition. In contrast, reward opportunities substantially increase both contributions and efficiency. Punishment is not effective in this heterogeneous setting, and may even be counterproductive due to antisocial punishment by high-benefit members.
Paper findings:
The paper finds that in public goods games with heterogeneous groups (MPCRs 0.9 and 0.4), allowing punishment does not significantly increase group efficiency or average earnings compared to the control (no incentives) condition. Average per-period earnings in the punishment condition (17.007 tokens) are actually lower than in the control (23.860 tokens), and after adjusting for the resource destruction effect of punishment, final earnings in the punishment condition (23.630 tokens) are still not higher than control. In contrast, reward opportunities lead to much higher efficiency and earnings. The lack of effectiveness of punishment is attributed to antisocial punishment by high-benefit members and lack of strategic punishment by low-benefit members. The results are robust across group and individual analyses, and the paper provides direct evidence that punishment does not improve efficiency in this heterogeneous PGG setting.
Decision support:
This paper provides strong evidence that, in public goods games with heterogeneous MPCRs, enabling punishment does not improve efficiency relative to the control (no-punishment) condition. For prediction tasks, if the game design matches this paper (3 players, MPCRs 0.9/0.4, no chat, continuous contributions, punishment cost 1:3, no rewards in punishment condition, 10 rounds, full feedback), the expected efficiency with punishment enabled should be similar to or lower than the control efficiency. The paper also shows that reward is much more effective than punishment in this context. The findings are directly relevant for predicting the effect of punishment on efficiency in heterogeneous PGGs.
Key claims:
Punishment opportunities do not significantly increase group efficiency or average earnings compared to the control (no incentives) condition in heterogeneous public goods games. [support=high] [refs=Section 4.3.2 Reward improves efficiency | Figure 3 Average per-period final earnings | Table 6 Treatment effects: tobit regression results | Conclusion] || Reward opportunities strongly increase both contributions and efficiency, outperforming punishment in heterogeneous groups. [support=high] [refs=Section 4.1.1 Reward versus control | Section 4.1.2 Reward versus punish | Section 4.3.2 Reward improves efficiency | Conclusion] || Punishment is ineffective in heterogeneous groups due to antisocial punishment by high-benefit members and lack of strategic punishment by low-benefit members. [support=high] [refs=Section 4.2 Punishment and reward behavior | Table 4 Punishment/reward depending on contributions and first-stage earnings | Conclusion] || Efficiency (measured as average group earnings, adjusted for welfare construction/destruction) is not improved by punishment relative to control. [support=high] [refs=Section 4.3.2 Reward improves efficiency | Figure 3 Average per-period final earnings]
Important limitations:
The experiment uses a specific form of heterogeneity (one high-benefit, two low-benefit members with fixed MPCRs); results may not generalize to other forms of heterogeneity. | Punishment and reward are implemented in separate treatments; there is no condition with both available simultaneously. | The sample size is moderate (87 in punishment, 81 in reward), and the analysis mixes within- and between-subject comparisons. | Endowments are earned, not windfall, which may affect the relative effectiveness of punishment and reward. | The punishment and reward mechanisms use a 1:3 cost-effectiveness ratio, which may not match all real-world settings. | No communication is allowed; effects may differ with chat or communication.
```

### 10.1016_j.chieco.2024.102267 (score=34.929)

```text
[Paper] 10.1016_j.chieco.2024.102267
Type: empirical | empirical=experimental | experimental=lab_experiment
Relevance: pgg_or_variant=exact; punishment_or_sanctions=exact; efficiency_or_related_payoff_outcome=exact
Outcomes: primary=efficiency_or_payoff; overall_effect_on_efficiency_or_payoff=more_positive
Informative dimensions:
- all_or_nothing [informative_direct; effect=N/A; basis=manipulated]; notes=Contribution is continuous from 0 to 20 tokens.
- chat [informative_direct; effect=N/A; basis=manipulated]; notes=No communication or chat allowed between players.
- mpcr [informative_direct; effect=N/A; basis=manipulated]; notes=MPCR is 0.6 (public account is multiplied by 0.6 and distributed equally).
- num_rounds [informative_direct; effect=N/A; basis=manipulated]; notes=Each stage consists of 5 rounds.
- player_count [informative_direct; effect=N/A; basis=manipulated]; notes=Groups of 4 (2 men, 2 women) in all sessions.
- punishment_cost [informative_direct; effect=N/A; basis=manipulated]; notes=Punisher pays 1 token per punishment point.
- punishment_tech [informative_direct; effect=N/A; basis=manipulated]; notes=Each punishment point costs the punisher 1 token and reduces the target's earnings by 2 tokens.
- reward_cost [informative_direct; effect=N/A; basis=manipulated]; notes=Leader's bonus is not costly to other players; it is an extra payment if group contributions exceed threshold.
- reward_exists [informative_direct; effect=N/A; basis=manipulated]; notes=Leaders can receive a bonus if group contributions exceed 50 tokens (bonus = (total - 50) * 0.4). No peer reward mechanism for non-leaders.
- reward_tech [informative_direct; effect=N/A; basis=manipulated]; notes=Bonus to leader is (group contribution - 50) * 0.4, only if group contribution > 50.
- show_n_rounds [informative_direct; effect=N/A; basis=manipulated]; notes=Players are told in advance that there are 5 rounds per stage.
- show_other_summaries [informative_direct; effect=N/A; basis=manipulated]; notes=At the end of each round, group members are informed of the total group contribution and their own earnings, but not the contributions of others or who was punished (except for their own punishment).
- show_punishment_id [informative_direct; effect=N/A; basis=manipulated]; notes=Punishment is assigned by the leader, but group members do not know the leader's identity (gender is not revealed), and only the punished member is informed of their own punishment.
Overall summary:
This laboratory experiment uses a standard public good game with a leader who can punish at a cost, and manipulates the framing of the leader's role (authority vs. responsibility) and the method of leader selection (willingness to lead vs. voting). The main finding is that when the leader's role is framed as responsibility and leaders are selected by voting, group efficiency (measured by group income) is significantly higher in female-led groups than in male-led groups or in authority-framed conditions. The effect is driven by higher leader contributions and, to a lesser extent, more targeted punishment. In other conditions, the framing effect is weaker or absent. The study provides direct evidence that punishment-enabled leadership can increase efficiency, especially when combined with responsibility framing and female leaders.
Paper findings:
The experiment finds that introducing a leader with the power to punish increases group contributions and efficiency compared to the no-leader baseline. When the leader's role is framed as responsibility (rather than authority), and especially when the leader is selected by voting, female leaders are more effective at increasing group income and efficiency than male leaders. The responsibility framing increases both leader contributions and the effectiveness of punishment, but the positive effect on efficiency is robustly observed only in the voting stage for female-led groups. In other conditions (authority framing, male leaders, or self-selected leaders), the efficiency gains from punishment are smaller or not significant. The study also shows that leader contributions are a more important driver of efficiency than punishment per se, as punishment can offset its own benefits through costs. Overall, the presence of punishment increases efficiency, but the magnitude depends on leader gender, framing, and selection method.
Decision support:
This paper provides strong evidence that enabling punishment in a public good game increases efficiency, especially when the leader is female, the leadership role is framed as responsibility, and the leader is selected by voting. The game design dimensions most relevant for predicting efficiency gains from punishment are: presence of a leader with punishment power, punishment cost and effectiveness, group size (4), number of rounds (5), and information structure (no chat, summary feedback). The control (no-leader) efficiency is reported, and the treatment (punishment-enabled) efficiency is higher, particularly in the responsibility/voting/female leader condition. For prediction, the paper suggests that punishment is most effective at increasing efficiency when the leader is prosocial (as selected or induced by responsibility framing), and that leader contributions are a key mechanism. The results are directly relevant for predicting efficiency in similar lab PGGs with punishment, especially with comparable group size, round number, and punishment parameters.
Key claims:
Introducing a leader with the power to punish increases group contributions and efficiency compared to the no-leader baseline. [support=high] [refs=Table 2 | Section 3.2.1 | Section 3.3 | Table 9] || Responsibility framing of the leader's role increases efficiency in female-led groups, especially when leaders are selected by voting. [support=high] [refs=Section 3.3 | Table 9 | Result 5 | Conclusion] || Leader contributions are a more important driver of efficiency than punishment per se; punishment can increase contributions but may offset its own benefits through costs. [support=high] [refs=Table 9 | Section 3.3 | Conclusion] || Female leaders are more responsive to responsibility framing than male leaders, leading to higher group efficiency in those conditions. [support=high] [refs=Section 3.2.1 | Section 3.3 | Table 6 | Table 9] || Punishment is necessary to deter low contributions, but its efficiency effect depends on how it is used and by whom. [support=medium] [refs=Section 3.2.2 | Table 8 | Section 3.3]
Important limitations:
The experiment is conducted in a laboratory setting with student participants, which may limit external validity. | Group size, number of rounds, and punishment/reward parameters are fixed and may not generalize to other settings. | Leader identity (including gender) is not revealed to group members, which may affect the generalizability to real-world leadership contexts. | The study focuses on short-term (5-round) repeated games; longer-term dynamics are not explored. | The framing manipulation (authority vs. responsibility) may interact with cultural or institutional factors not present in the lab.
```

### 10.1016_j.jebo.2013.08.006 (score=34.929)

```text
[Paper] 10.1016_j.jebo.2013.08.006
Type: empirical | empirical=experimental | experimental=lab_experiment
Relevance: pgg_or_variant=exact; punishment_or_sanctions=exact; efficiency_or_related_payoff_outcome=exact
Outcomes: primary=efficiency_or_payoff; overall_effect_on_efficiency_or_payoff=more_positive
Informative dimensions:
- all_or_nothing [informative_direct; effect=N/A; basis=manipulated]; notes=Contribution is continuous from 0 to 10 experimental dollars.
- chat [informative_direct; effect=N/A; basis=manipulated]; notes=No communication between subjects; decisions made without communication.
- mpcr [informative_direct; effect=N/A; basis=manipulated]; notes=MPCR is 0.4 (group multiplier 1.6, divided by 4 players).
- num_rounds [informative_direct; effect=N/A; basis=manipulated]; notes=Each session has 20 periods (rounds).
- player_count [informative_direct; effect=N/A; basis=manipulated]; notes=All groups have 4 players in both treatments.
- punishment_cost [informative_direct; effect=N/A; basis=manipulated]; notes=Punishment costs 0.25 per unit (punisher pays 0.25 to reduce target's earnings by 1).
- punishment_tech [informative_direct; effect=N/A; basis=manipulated]; notes=Punishment effectiveness is 1 per 0.25 cost (i.e., 1 unit reduction per 0.25 spent).
- reward_cost [informative_direct; effect=N/A; basis=manipulated]; notes=In RP, reward is costless to the rewarder (the cost is paid as part of punishment; reward is a transfer of the fine).
- reward_exists [informative_direct; effect=more_positive; basis=manipulated]; notes=Reward is only available in the redistributive punishment (RP) treatment, where each punishment must be redistributed as a reward to other group members.
- reward_tech [informative_direct; effect=N/A; basis=manipulated]; notes=Reward effectiveness is 1 per 0 cost (each unit of fine is transferred as 1 unit reward to another group member).
- show_n_rounds [informative_direct; effect=N/A; basis=manipulated]; notes=The number of periods (20) is finite and known to participants.
- show_other_summaries [informative_direct; effect=N/A; basis=manipulated]; notes=After each period, subjects see the amounts each other group member contributed (in random order), and their own net change in earnings due to rewards and punishments.
- show_punishment_id [informative_direct; effect=N/A; basis=manipulated]; notes=Subjects do not know which group member punished or rewarded them; only the net effect is shown, and identities are not revealed.
Overall summary:
The paper finds that making punishment redistributive (so that fines are transferred to other group members as rewards) increases both contributions and efficiency in a voluntary contribution mechanism (VCM) public goods game. Even after netting out the direct resource effect of redistribution, efficiency is higher in the redistributive punishment treatment than in standard punishment. Redistributive punishment also reduces perverse punishment (punishment of high contributors) and makes it more profitable to contribute, as the return to contribution becomes positive.
Paper findings:
In a repeated public goods game with four players and 20 rounds, the authors compare standard costly punishment (where fines are burned) to a redistributive punishment treatment (where fines are transferred to other group members as rewards). Both treatments use the same marginal per capita return (MPCR = 0.4), punishment cost (0.25 per unit), and group structure. The redistributive punishment treatment leads to significantly higher average contributions (9.03 vs. 7.09), higher average earnings (15.18 vs. 12.88), and higher efficiency, even after controlling for the resource-conserving effect of redistribution (earnings net of transfers: 14.20 vs. 12.88). The effect on efficiency is marginally statistically significant after netting out transfers. Redistributive punishment also reduces the share of punishment targeted at high contributors and increases the monetary return to contributing (from negative to positive). The study provides direct evidence that the design of the punishment mechanism can moderate the efficiency impact of punishment in public goods games.
Decision support:
This paper provides strong evidence that, in a standard linear public goods game with four players, 20 rounds, no communication, and fixed partners, enabling punishment increases contributions but does not always increase efficiency due to the costliness and mis-targeting of punishment. However, if the punishment mechanism is modified so that fines are redistributed as rewards to other group members (rather than burned), both contributions and efficiency increase, and the return to contributing becomes positive. For prediction tasks, this suggests that the structure of the punishment mechanism (specifically, whether punishment is redistributive or not) is a key moderator of the efficiency effect. The control (punishment-off) efficiency is not directly reported, but the paper references prior work showing that standard punishment does not increase efficiency over the no-punishment baseline, while redistributive punishment does. The findings are directly relevant for predicting treatment efficiency from game design dimensions, especially the nature of the punishment and reward mechanisms.
Key claims:
Making punishment redistributive (so that fines are transferred to other group members) increases both contributions and efficiency in the public goods game, even after netting out the direct resource effect. [support=high] [refs=Abstract | Section 4.2 Earnings | Table 1 | Section 5 Discussion and conclusions] || Redistributive punishment reduces the share of punishment targeted at high contributors (perverse punishment), especially when viewed from the recipient's perspective. [support=high] [refs=Section 4.7 | Table 5 | Result 6] || The return to contributing becomes positive under redistributive punishment, making it more profitable to contribute and reducing successful free-riding. [support=high] [refs=Section 4.8 | Table 6 | Result 7] || Standard costly punishment increases contributions but does not reliably increase efficiency, due to the cost of punishment and mis-targeting. [support=high] [refs=Introduction | Section 4.2 | Section 5] || Punishment is mainly targeted at low contributors, and this targeting is even stronger in the redistributive punishment treatment. [support=high] [refs=Section 4.4 | Table 2 | Result 3]
Important limitations:
The study is limited to a lab setting with undergraduate students and fixed groups of four; generalizability to other populations or group sizes is not tested. | The redistributive punishment mechanism is not commonly observed in real-world collective action settings, so external validity may be limited. | The efficiency benefit of redistributive punishment is only marginally statistically significant after netting out the direct resource effect. | The control (no-punishment) efficiency is not directly measured in this experiment, but inferred from prior work. | The design does not allow for communication or reputation effects, which may be important in real-world settings.
```

### 10.1016_j.joep.2009.04.004 (score=34.929)

```text
[Paper] 10.1016_j.joep.2009.04.004
Type: empirical | empirical=experimental | experimental=lab_experiment
Relevance: pgg_or_variant=exact; punishment_or_sanctions=exact; efficiency_or_related_payoff_outcome=exact
Outcomes: primary=efficiency_or_payoff; overall_effect_on_efficiency_or_payoff=mixed
Informative dimensions:
- all_or_nothing [informative_direct; effect=N/A; basis=manipulated]; notes=Contribution is continuous: each player chooses how many of 20 tokens to contribute (0-20).
- chat [informative_direct; effect=N/A; basis=manipulated]; notes=Communication between participants was not allowed at any time.
- mpcr [informative_direct; effect=N/A; basis=manipulated]; notes=MPCR is 1.6/6 ≈ 0.267.
- num_rounds [informative_direct; effect=N/A; basis=manipulated]; notes=30 rounds per group, divided into 3 phases of 10 rounds each.
- player_count [informative_direct; effect=N/A; basis=manipulated]; notes=Each group consists of 6 players (1 leader, 5 teammates).
- punishment_cost [informative_direct; effect=N/A; basis=manipulated]; notes=Each punishment token assigned by the leader costs 1 token (opportunity cost: not kept by leader).
- punishment_tech [informative_direct; effect=N/A; basis=manipulated]; notes=Each punishment token reduces the target's payoff by 3 tokens (punishment effectiveness 3:1).
- reward_cost [informative_direct; effect=N/A; basis=manipulated]; notes=Each reward token assigned by the leader costs 1 token (opportunity cost: not kept by leader).
- reward_exists [informative_direct; effect=N/A; basis=manipulated]; notes=Leader can choose to use a reward (positive incentive) scheme.
- reward_tech [informative_direct; effect=N/A; basis=manipulated]; notes=Each reward token increases the target's payoff by 3 tokens (reward effectiveness 3:1).
- show_n_rounds [informative_direct; effect=N/A; basis=manipulated]; notes=All players are informed about the total number of rounds and phases at the start.
- show_other_summaries [informative_direct; effect=N/A; basis=manipulated]; notes=At the end of each round, all players see all individual contributions, payoffs, and received tokens for all group members.
- show_punishment_id [informative_direct; effect=N/A; basis=manipulated]; notes=Players know which group member is the leader and that only the leader can assign tokens, but the display order of teammates is randomized each round to prevent identification of individual teammates across rounds.
Overall summary:
The experiment compares the effects of leader-chosen positive (reward) and negative (punishment) incentive schemes in a repeated public goods game. While punishment increases contributions more than rewards, overall team efficiency (measured as the ratio of actual to maximum possible payoff) is slightly higher under rewards than punishment, though the difference is not statistically significant. Leaders earn more under punishment, but teammates earn more under rewards. The most efficient path in terms of aggregate team payoff is when leaders consistently choose rewards. Switching from rewards to punishment increases contributions, but does not improve overall efficiency or team welfare.
Paper findings:
Leaders overwhelmingly prefer to use rewards initially, but some switch to punishment if free-riding is high. Punishment schemes (NEG) lead to higher contributions than reward schemes (POS), both for leaders and teammates. However, overall payoffs and efficiency are higher under rewards, because the reward mechanism increases total team surplus (each reward token increases team payoff, while each punishment token reduces it). Leaders benefit more from punishment, but teammates benefit more from rewards. The most efficient outcome (in terms of team payoff relative to the maximum possible) is achieved when leaders stick to rewards throughout. Switching from rewards to punishment increases contributions immediately and persistently, but does not increase efficiency. The effectiveness of incentive schemes is path-dependent and history matters. The study provides direct evidence on how the structure and cost/impact of incentives affect efficiency and payoffs in public goods games with centralized leader-administered incentives.
Decision support:
This paper provides high-quality, directly relevant evidence for predicting the effect of enabling punishment in a repeated public goods game with centralized leader-administered incentives. It shows that while punishment increases contributions, it does not increase efficiency or total team payoff compared to rewards; in fact, efficiency is slightly higher with rewards. The marginal per-capita return, punishment/reward cost and effectiveness, and the structure of the incentive mechanism are all specified and can be mapped to prediction dimensions. The results suggest that enabling punishment may increase contributions but not efficiency, and that the net effect on efficiency depends on the cost/impact structure of the punishment mechanism. The findings are most applicable to settings with centralized, leader-chosen incentives, continuous contributions, and full information about contributions and payoffs.
Key claims:
Punishment (NEG) increases contributions more than rewards (POS), both for leaders and teammates. [support=high] [refs=Section 4.1 Overall contributions, payoffs, and efficiency | Fig. 2 | Section 4.2.5 | Section 4.2.6] || Overall team efficiency (actual/maximum payoff) is slightly higher under rewards (POS) than punishment (NEG), but the difference is not statistically significant. [support=high] [refs=Section 4.1 | Fig. 2 | Conclusion] || Leaders earn more under punishment, but teammates earn more under rewards. [support=high] [refs=Section 4.1 | Section 4.3.2 | Fig. 4 | Fig. 5] || The most efficient path in terms of aggregate team payoff is when leaders consistently choose rewards (POS\&POS\&POS). [support=high] [refs=Section 4.3.2 | Fig. 6 | Conclusion] || Switching from rewards to punishment causes an immediate and persistent increase in contributions, but does not increase efficiency. [support=high] [refs=Section 4.2.5 | Section 4.2.6 | Section 4.3.1 | Conclusion] || The effectiveness of incentive schemes is path-dependent; history of incentive use affects future contributions and payoffs. [support=medium] [refs=Section 4.3 | Conclusion]
Important limitations:
The experiment uses a centralized, leader-administered incentive scheme, which may not generalize to decentralized or peer punishment settings. | The cost and effectiveness of punishment and reward are fixed and may not match real-world institutions. | The study uses student subjects in a laboratory environment, which may limit external validity. | No communication is allowed between participants, which may affect cooperation dynamics. | The leader is randomly assigned and not elected, which may affect legitimacy and compliance. | The experiment does not include a pure control condition with no incentives; only reward vs. punishment are compared. | The findings are path-dependent and may not generalize to single-shot or non-repeated settings.
```

## Least Relevant (heuristic ranking)

### 10.20350_digitalCSIC_16534 (score=1.2)

```text
[Paper] 10.20350_digitalCSIC_16534
Type: empirical | empirical=observational | experimental=N/A
Relevance: pgg_or_variant=none; punishment_or_sanctions=none; efficiency_or_related_payoff_outcome=none
Outcomes: primary=non_payoff_behavior; overall_effect_on_efficiency_or_payoff=N/A
Informative dimensions:
- None
Overall summary:
This report provides a comprehensive gender-based analysis of research staff and activities at the Spanish National Research Council (CSIC) as of December 2023. It documents the distribution of men and women across research categories, career progression, access processes, research project leadership, patent inventorship, and training roles. The main focus is on identifying and quantifying gender gaps, glass ceiling effects, and trends in women's participation and advancement in research careers.
Paper findings:
The report finds that while the overall gender distribution at CSIC is balanced, significant disparities remain in permanent and senior research positions, with women underrepresented especially at the Research Professor level (26.9%). The glass ceiling index is 1.42 overall, with higher values in some sub-areas. Positive trends include increases in the percentage of women directors, inventors in patent applications, and supervisors of theses. However, progress in closing the gender gap is slow, and disparities persist in access to higher research categories and leadership roles.
Decision support:
This paper does not provide any evidence or findings relevant to predicting the effect of punishment on efficiency in public goods games or similar environments. It does not discuss game design, cooperation, sanctions, or payoff-based outcomes. Therefore, it should not be used to inform predictions about punishment effects in public-goods-game-like settings.
Key claims:
Women remain underrepresented in permanent and senior research positions at CSIC, with only 26.9% of Research Professors being women. [support=high] [refs=EXECUTIVE SUMMARY | Distribution of research staff by category and sex | Permanent scientific staff by sub-areas] || The glass ceiling index for CSIC scientific staff is 1.42, indicating persistent barriers to women's advancement, with higher values in some disciplines. [support=high] [refs=EXECUTIVE SUMMARY | Glass Ceiling* 2023] || There has been an increase in the percentage of women in leadership and training roles, such as directors, inventors in patent applications, and thesis supervisors. [support=high] [refs=EXECUTIVE SUMMARY | TRANSFER | CHAPTER 4. TRAINING] || Progress toward gender equality in research careers at CSIC is slow, and significant disparities remain, especially in access to higher research categories. [support=high] [refs=EXECUTIVE SUMMARY | CHAPTER 2: ACCESS]
Important limitations:
The report does not address public goods games, punishment, sanctions, or any game-theoretic or experimental economic design. | No efficiency, payoff, or welfare outcomes are reported or analyzed. | All findings are descriptive and observational, focused on gender distribution and career progression in research staff. | No experimental or causal inference relevant to cooperation, punishment, or efficiency is present.
```

### 10.1080_0022250x.2019.1704284 (score=0.843)

```text
[Paper] 10.1080_0022250x.2019.1704284
Type: theory | empirical=N/A | experimental=N/A
Relevance: pgg_or_variant=none; punishment_or_sanctions=none; efficiency_or_related_payoff_outcome=none
Outcomes: primary=non_payoff_behavior; overall_effect_on_efficiency_or_payoff=N/A
Informative dimensions:
- num_rounds [informative_direct; effect=N/A; basis=manipulated]; notes=Each simulation runs for 20,000 iterations to reach equilibrium; not structured as discrete rounds of a game, but as asynchronous network updates.
- player_count [informative_direct; effect=N/A; basis=manipulated]; notes=Simulations use n=20 agents as default, with sensitivity analysis for n=50 and n=100. No effect on qualitative results reported.
Overall summary:
This paper develops a stochastic actor-based agent-based model to study how resource heterogeneity and competition for collaboration partners affect the emergence and structure of mutual support expectation networks among professionals. The model simulates multiplex networks of collaboration, trust, and support expectations, manipulating resource distribution and neediness. The main outcomes are network connectivity and segregation, not payoffs or efficiency. No public goods game, punishment, or payoff-based outcomes are present.
Paper findings:
The study finds that competition for high-resource partners in collaboration networks with unequal resource distribution leads to more segregated and slightly less connected mutual support expectation networks. When neediness is negatively correlated with resources, low-resource agents can form dense, segregated support networks among themselves, partially counteracting their marginalization. However, all outcomes are in terms of network structure (connectivity, segregation) and not payoffs, efficiency, or welfare. The model does not include public goods, punishment, or sanctioning mechanisms.
Decision support:
This paper does not inform the prediction of efficiency or payoff outcomes in public-goods-game-like environments with or without punishment. It does not model or report on payoffs, group earnings, or efficiency, nor does it include any form of punishment, sanction, or public goods provision. Its findings on network segregation and support expectations under competition and resource heterogeneity are not transferable to the efficiency effects of punishment in PGGs.
Key claims:
Competition for high-resource partners in a collaboration network with unequal resource distribution generates a support expectation network with lower connectivity and higher segregation compared to a situation with no competition. [support=high] [refs=Section 5 Results | Table 3 | Figure 1 | Propositions 1a and 1b in Section 2] || Heterogeneous neediness negatively correlated with resources can compensate for the exclusion of low-resource agents, leading to denser but more segregated support networks among low-resource agents. [support=high] [refs=Section 5 Results | Table 3 | Figure 1 | Proposition 2 in Section 2] || Resource heterogeneity and competition have a double-edged effect: they can marginalize low-resource agents but also allow for in-group solidarity among them if neediness is high. [support=medium] [refs=Section 6 Discussion and conclusions]
Important limitations:
The model is purely theoretical and not calibrated to empirical data. | No payoff, efficiency, welfare, or group earnings outcomes are modeled or reported. | No public goods, punishment, or sanctioning mechanisms are present. | Findings are about network structure (connectivity, segregation) and not about efficiency or payoffs. | Simulations are limited to small populations (n=20, with some sensitivity analysis). | Generalizability to real-world or larger-scale settings is not established. | No direct relevance to public-goods-game-like environments or the effects of punishment on efficiency.
```

### 10.1103_PhysRevE.101.032305 (score=0.843)

```text
[Paper] 10.1103_PhysRevE.101.032305
Type: theory | empirical=N/A | experimental=N/A
Relevance: pgg_or_variant=none; punishment_or_sanctions=none; efficiency_or_related_payoff_outcome=none
Outcomes: primary=non_payoff_behavior; overall_effect_on_efficiency_or_payoff=N/A
Informative dimensions:
- num_rounds [informative_direct; effect=N/A; basis=manipulated]; notes=Simulations run for 10^4 to 10^6 Monte Carlo steps (MCS), with each MCS corresponding to N updates.
- player_count [informative_direct; effect=N/A; basis=manipulated]; notes=Simulations use system sizes N=500 to 1000; sender-receiver game is pairwise, but population size is specified.
Overall summary:
This paper uses Monte Carlo simulations to study the evolution of honesty and lying in the sender-receiver game across different network topologies (well-mixed, small-world, one-dimensional ring). The main outcomes are the densities of liars and believers, and the prevalence of different strategy profiles, as a function of the type of lie (black, altruistic white, Pareto white, spiteful). The study does not involve public goods games, punishment, or efficiency/payoff outcomes.
Paper findings:
The study finds that network structure has a nontrivial effect on the evolution of honesty and lying in the sender-receiver game. For black lies and altruistic white lies, honesty is more likely to evolve in small-world networks and, to a lesser extent, in the one-dimensional ring, compared to well-mixed populations. For Pareto white lies, lying is more likely to evolve in small-world networks. For spiteful lies, honesty always prevails regardless of network. The outcomes are reported in terms of the densities of liars and believers, not in terms of payoffs or efficiency. The sender-receiver game is fundamentally different from public goods games and does not include punishment or reward mechanisms.
Decision support:
This paper does not provide evidence relevant to predicting the effect of punishment on efficiency in public-goods-game-like environments. It does not study public goods games, does not include punishment or sanctions, and does not report efficiency, welfare, or payoff-based outcomes. Its findings on network structure and the evolution of honesty in the sender-receiver game are not transferable to the prediction task focused on punishment and efficiency in PGGs.
Key claims:
Network structure (e.g., small-world, ring) can promote honesty in the sender-receiver game, especially for black lies and altruistic white lies, compared to well-mixed populations. [support=high] [refs=Abstract | Section III.A | Section IV Discussion | Figures 1-4] || For Pareto white lies, small-world networks can actually favor the evolution of lying compared to well-mixed populations. [support=high] [refs=Abstract | Section III.A | Section IV Discussion | Figure 5] || The sender-receiver game outcomes depend strongly on the type of lie and the specific payoff parameters, and the steady states often do not coincide with Nash equilibria. [support=high] [refs=Section III | Section IV Discussion] || The study does not include punishment or reward mechanisms, but suggests that these could promote honesty, as they do for cooperation in other games. [support=medium] [refs=Section IV Discussion, paragraph on limitations]
Important limitations:
The study does not involve public goods games or any PGG-like environment. | No punishment or sanction mechanisms are present or analyzed. | No efficiency, welfare, group payoff, or related payoff-based outcomes are reported. | Findings are limited to the sender-receiver game and the evolution of honesty/lying on networks. | Results may not generalize to environments with punishment, reward, or different game structures.
```

### 10.1016_j.jebo.2003.09.017 (score=0.736)

```text
[Paper] 10.1016_j.jebo.2003.09.017
Type: theory | empirical=N/A | experimental=N/A
Relevance: pgg_or_variant=none; punishment_or_sanctions=none; efficiency_or_related_payoff_outcome=none
Outcomes: primary=non_payoff_behavior; overall_effect_on_efficiency_or_payoff=N/A
Informative dimensions:
- player_count [contextual; effect=N/A; basis=discussion_only]; notes=Simulations use large populations (e.g., 10,000 agents), but the model is not a game and does not analyze player count as a variable affecting efficiency or payoff.
Overall summary:
This is a theoretical and simulation-based paper modeling the emergence and stability of social groups through homophilous imitation, without any explicit payoffs, rewards, or punishments. The models show that stable group structures and polarization can arise from imitation alone, especially when individuals are more likely to imitate those similar to themselves and when there is a tendency to revert to group norms. No public goods game, punishment, or efficiency/welfare outcomes are studied.
Paper findings:
The paper demonstrates that stable social groups and polarization can emerge in agent-based models where individuals imitate others who are similar to themselves (homophily), even in the absence of any explicit payoffs, rewards, or punishments. The stability of group structures depends on the rate of introspective (idiosyncratic) changes and the strength of homophilous imitation. The models are not payoff-based and do not include any public goods, cooperation, or sanctioning mechanisms.
Decision support:
This paper does not inform the prediction of efficiency or payoff outcomes in public-goods-game-like environments with or without punishment. It does not model or analyze any payoff, efficiency, or sanctioning mechanism, and thus provides no direct or indirect evidence for the effect of punishment on efficiency or related outcomes. Its findings are not transferable to the prediction task as defined.
Key claims:
Stable social groups and polarization can arise from homophilous imitation alone, without the need for explicit payoffs, rewards, or punishments. [support=high] [refs=Abstract | Section 2: Models of imitation | Section 3: Analytical results | Section 4: Conclusions] || The stability of group structures depends on the rate of introspective changes and the strength of imitation toward group norms. [support=high] [refs=Section 2: Models of imitation | Section 3: Analytical results | Figures 3, 5] || The model does not require xenophobia (active opposition to out-groups) for polarization to occur. [support=medium] [refs=Section 4: Conclusions]
Important limitations:
The model does not include any payoff, efficiency, or welfare outcomes; all results are about group structure and opinion dynamics. | No public goods game, cooperation, or sanctioning mechanisms are modeled. | Findings are not transferable to efficiency or payoff prediction tasks in PGG-like environments. | All results are theoretical or simulation-based; no empirical or experimental data.
```

### 10.1111_1467-923x.12939 (score=0.5)

```text
[Paper] 10.1111_1467-923x.12939
Type: theory | empirical=N/A | experimental=N/A
Relevance: pgg_or_variant=none; punishment_or_sanctions=none; efficiency_or_related_payoff_outcome=none
Outcomes: primary=N/R; overall_effect_on_efficiency_or_payoff=N/A
Informative dimensions:
- None
Overall summary:
This paper is a theoretical and historical analysis of the challenges and lessons of forming progressive political alliances, with a focus on the UK and international cases. It does not involve public goods games, punishment, or efficiency-related outcomes in the sense relevant to experimental economics or game theory.
Paper findings:
The paper reviews historical attempts at progressive political cooperation, identifying recurring challenges and lessons for contemporary efforts. It discusses the importance of inclusivity, flexibility, and shared purpose in alliances, and warns against dominance by any single member or rigidity in structure. The analysis is qualitative and historical, not empirical or experimental.
Decision support:
This paper does not provide evidence relevant to predicting the effect of punishment on efficiency in public goods games or similar environments. It does not discuss game design dimensions, control or treatment efficiency, or any related experimental outcomes. It should not be used to inform predictions in the specified downstream task.
Key claims:
Progressive political alliances are difficult to sustain due to ideological, geographical, and social divisions, but are necessary to overcome fragmentation and achieve electoral success. [support=high] [refs=Lessons from progressive history | Between concert and context | Finding the centre(-left) of gravity] || Successful alliances require inclusivity, flexibility, and avoidance of dominance by any single member. [support=high] [refs=Lessons from progressive history | To close, it is worth considering the key risks, or dangers, about which the history of progressive cooperation can act as a salutary warning for British progressives today.] || Historical examples show that alliances often form reactively in response to external threats, especially from the far right. [support=high] [refs=From negative resistance to a positive programme]
Important limitations:
The paper is entirely theoretical and historical, with no empirical, experimental, or quantitative analysis. | It does not discuss public goods games, punishment, efficiency, or any related game-theoretic or experimental concepts. | No outcomes relevant to the prediction of efficiency or payoff in public goods game environments are reported or discussed.
```
