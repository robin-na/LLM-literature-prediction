## 1) Design & Data

- The study employed an "integrative experiment" with 14 systematically varied design parameters, producing 360 unique experimental conditions (147,618 decisions from 7,100 participants). This space covers a diverse range of PGG scenarios.
- Each condition involved a paired design: one game with punishment enabled (treatment), one with punishment disabled (control), sharing identical parameters otherwise.
- Data was collected in two waves: Wave 1 ("learning") used a Sobol sequence to fill the parameter space with 320 conditions (1 trial per condition), Wave 2 ("validation") consisted of 40 new conditions each with 8–12 trials for precise evaluation. Experiments were run in a controlled online environment with consistent protocols and interfaces.
- The 14 parameters (CONFIG) include group size, game length, contribution type (variable/all-or-nothing), contribution framing (opt-in/opt-out), MPCR, communication, peer outcome visibility, actor anonymity, horizon knowledge, and design elements governing punishment and reward mechanisms, among others.

## 2) Efficiency Definition

- “Efficiency” is defined as the ratio:  
  **Efficiency = (Group’s total earnings) / (Earnings of a fully cooperative group of the same config)**
- Thus, efficiency = 1 indicates all members contributed fully every round and did not incur extra costs from punishment; lower values reflect less cooperation and/or losses due to costly punishment.
- This measure was used for the core prediction task (regular “efficiency” vs. “normalized efficiency” which rescales for cross-game comparisons), and is especially intuitive for direct treatment-control (punishment on/off) comparisons within the same config.

## 3) Main Findings on Punishment

- On average, punishment increased contributions (from 73/74% to 80/82% of endowment), but its effect on efficiency (welfare) was much more heterogeneous and context-dependent.
- In aggregate, punishment **often reduced efficiency**: e.g., average normalized efficiency dropped from 0.71 to 0.63 in learning experiments and from 0.72 to 0.68 in validation. But this average masked substantial *heterogeneity*:
   - In specific settings, punishment reduced normalized efficiency by up to 44%; in others, it increased it by as much as 43%.
- **Key finding:** The effect of punishment on welfare is highly context-sensitive and can swing dramatically based on other parameters, not reliably positive or negative overall.

## 4) Heterogeneity / Moderators

- **Communication availability** was by far the most important moderator: enabling chat led to a large positive impact on punishment effectiveness (shuffling this feature increased prediction error by 60%, ~3x higher than the next most important).
- Other consistent or contingent moderators:
  - **Contribution framing** (opt-in vs. opt-out): The effect of opt-out framing for punishment depends on contribution type and peer outcome visibility.
     - Opt-out increased punishment effectiveness with variable contributions but reduced it in all-or-nothing settings, with peer outcome visibility further modulating these effects.
  - **Game length** increases punishment impact only when communication is available; the effect is weaker if peer outcomes are visible.
  - Availability of **reward mechanisms** consistently enhanced the effect of punishment, though predicted variance was mostly captured by communication and framing.
  - MPCR has a small but reliably positive impact.
  - **Punishment technology** (size/cost ratio) surprisingly had the **least impact** on predicting punishment effectiveness compared to contextual moderators.
- Statistical tests revealed strong and robust heterogeneity across configs, driven by design parameter differences, not method differences or sample noise.

## 5) Notes for Prediction

- Each prediction instance should use values for all 14 CONFIG parameters plus the **control game efficiency** to predict the efficiency with punishment enabled. Control efficiency is highly informative and was included as a feature in the best models.
- The validated Elastic Net (E-Net) model performed best (out-of-sample R² = 0.53), substantially outperforming both expert and lay human forecasters, whose predictions were barely better than the mean baseline.
- Coordinate moderator effects: communication, contribution framing/type, game length, and peer outcome visibility are key drivers, with interactions and boundary conditions.
- Ignore punishment technology for predicting welfare; focus modeling/attention on interaction between context variables.
- The heterogeneity and sensitivity of punishment’s effectiveness reinforce the need for *high-fidelity, config-aware* prediction rather than reliance on grand averages or canonical findings.
- The dataset is designed for prediction, not for hypothesis-testing of individual effects in isolation; patterns discovered should be validated with out-of-sample configurations and may generalize more robustly than meta-analytic averages.
