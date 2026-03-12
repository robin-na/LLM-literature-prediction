## 1) Design & Data

- The study utilizes an integrative, high-throughput experimental approach. It systematically varied 14 design parameters across 360 unique conditions in public goods games (PGGs), yielding over 147,000 decisions from 7,100 participants. Parameters included group size (2-20), game length (1-30 rounds), contribution type (variable vs. all-or-nothing), contribution framing (opt-in vs. opt-out), MPCR, communication, peer outcome visibility, anonymity, knowledge of horizon, punishment and reward mechanisms (on/off), peer incentive cost, punishment/reward technology, and more.
- Each experiment consisted of a matched pair: one control (punishment disabled) and one treatment (punishment enabled), sharing all other configuration values.
- The design consisted of two data waves: Wave 1 (learning/space-filling, single trial per 320 conditions) and Wave 2 (validation/higher precision, 8-12 trials across 40 conditions).
- All experiments were run on a unified platform with identical protocols to minimize confounds.
- Predictive models (elastic net, random forest, XGBoost, MLP, OLS) were evaluated using out-of-sample performance (R², RMSE) on held-out validation settings, with comparison to human forecasters (experts and laypeople).

## 2) Efficiency Definition

- **Efficiency** is defined as the ratio of the group’s total payoff to the maximum possible payoff (i.e., if everyone contributed fully every round and no coins were lost to punishment/reward costs). 
- Mathematically:  
  \[
  \text{Efficiency} = \frac{\text{Total group earnings}}{\text{Earnings under full cooperation}}
  \]
  Values near 1 indicate full cooperation; lower values reflect less cooperation or higher punishment/reward losses.
- For comparison across games with different structure, a "normalized efficiency" metric is sometimes used, which adjusts for differences in minimum and maximum possible outcomes for each setup.

## 3) Main Findings on Punishment

- **Punishment consistently increased contributions** (e.g., from 73% to 80% average endowment contributed), but did not reliably increase efficiency: average efficiency actually **declined when punishment was enabled** due to the costs associated with punishing, though effects are highly heterogeneous.
- The effect of punishment on efficiency ranged from **+43% to -44%** depending on other game parameters.
- Prediction models (especially elastic net with interaction terms) **outperformed human experts at predicting when punishment would be beneficial vs. detrimental**.
- The **most important factor for benefit from punishment was the availability of communication**, which had a much larger impact than any other feature. When communication was enabled, punishment was much more likely to improve efficiency.
- Other consistently positive moderators: reward availability and higher MPCR (marginal per capita return).
- **Complex interactions:** for example, opt-out contribution framing increases punishment’s effectiveness only for variable contributions, but can decrease it for all-or-nothing contributions, particularly when peer outcomes are visible. Game length increases effectiveness of punishment primarily when communication is allowed.

## 4) Heterogeneity / Moderators

- Heterogeneity was substantial and robust: punishment effects on efficiency were sometimes dramatically positive or negative within the same participant pool and protocol, depending only on configuration.
- **Key moderators and interactions:**
  - **Communication:** Dominant predictor, amplifies punishment’s effectiveness.
  - **Contribution Framing (opt-in/opt-out):** Second most important, with effects contingent on type of contribution (variable vs all-or-nothing) and outcome visibility.
  - **Game Length:** Important, but only increases punishment effectiveness with communication; effect dampened by peer outcome visibility.
  - **Outcome Visibility:** Modulates framing and game-length effects, and can either attenuate or amplify punishment’s impact depending on the situation.
  - **Reward mechanisms:** The presence of rewards boosts likelihood that punishment is welfare enhancing.
  - **Punishment technology (severity vs. cost):** Surprisingly little predictive power in aggregate models, implying context and interaction matter more than the raw punishment ratio.
- Between-game heterogeneity was largely attributable to configuration, not random noise.

## 5) Notes for Prediction

- Use the 14 CONFIG parameters and control game efficiency as model input.
- Prioritize communication, contribution framing, and interaction terms in feature engineering or model interpretation.
- Consider conditional effects: e.g., communication amplifies punishment effectiveness in long games; opt-out framing can help or harm depending on contribution type/outcome visibility.
- Simple main effects or averages mask substantial variation; interpretable interaction terms are key.
- Human intuition (even expert) is poor at integrating these factors; data-driven modeling is more reliable.
- Results and insights are strongest within the design space tested; external validity should be treated cautiously.
