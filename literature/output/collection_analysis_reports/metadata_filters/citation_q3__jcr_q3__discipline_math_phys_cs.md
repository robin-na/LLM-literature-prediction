# Evidence Base

The paper set consists of **48 papers**, predominantly **theoretical modeling** studies, with sparse empirical or experimental evidence directly addressing the downstream prediction task. The focus is extremely **broad in terms of theory coverage**—including diverse models of public goods games (PGG), social dilemmas, resource games, and mutualism—but is **narrow in empirical scope**, as almost all papers lack direct laboratory or field-based payoff outcome measurements. The breadth of theoretical models allows for comprehensive coverage of many game **design dimensions** relevant to the prediction task. Direct measures of **efficiency** or group payoff are reported or explicitly modeled in a substantial minority of papers, while many more model or report on closely related behavioral measures (e.g., cooperation rates, prevalence of punishment, strategy proportions).

# Task Relevance

### 1. **pgg_or_variant**
- **Exact Relevance**: Most papers are models of the standard public goods game or direct variants (e.g., threshold PGG, spatial PGG).
- **Close or Adjacent**: A subset extends or generalizes to adjacent social dilemmas (e.g., n-player prisoner's dilemma, common-pool resource games, mutualism models).
- **None/Weak**: Only a few are not directly PGG-linked.

### 2. **punishment_or_sanctions**
- **Exact Relevance**: Many papers directly enable, manipulate, or model **peer punishment** or institutionally-mediated punishment.
- **Close or Adjacent**: Some focus solely on indirect punitive effects (e.g., conditional reciprocity, withholding), or discuss reward systems without explicit punishments.
- **Weak/None**: Several do not address punishment at all.

### 3. **efficiency_or_related_payoff_outcome**
- **Exact/Close**: Approx. half of the papers model or predict **efficiency** (defined as group payoff relative to full cooperation), or other explicit payoff/welfare measures.
- **Adjacent**: Several report **behavioral** proxies for efficiency (such as cooperation rates, strategy proportions).
- **Weak/None**: Some never report payoff or efficiency outcomes, focusing instead on behavior patterns, network structures, or evolutionary trajectories.

### **Summary**
- **Strongest task relevance** lies in theoretical papers explicitly modeling PGG with the option to enable/disable peer punishment and reporting equilibrium or aggregate payoff outcomes.
- **Empirical gaps**: Laboratory or field experimental evidence of control vs. punishment efficiency is missing.

# Outcomes Measured In The Literature

### **Payoff-Based Outcomes (`efficiency_or_payoff`)**
- **Exact**: Model-predicted group payoff, total welfare, or explicitly calculated efficiency ratios with/without punishment (e.g., Jiao et al., 2020; Eldakar et al., 2007; Archetti & Scheuring, 2013; Huang et al., 2018).
- **Close/Adjacent**: Analytical results on population mean fitness, average welfare, or conditions for reaching full-cooperation payoffs.
- **Indirect or Absent**: Many models use strategy frequencies, cooperation rates, or punishment prevalence as proxies; these require behavioral-payoff mapping.

### **Non-Payoff Behavioral Outcomes**
- **Common**: Prevalence of cooperation, frequency of punishment assignment, norm compliance, strategy evolution, cluster formation, avoidance mechanisms.
- **Distinction Maintained**: Most papers do not equate behavioral outcomes with efficiency, but do infer that increased cooperation is *usually* associated with higher payoff, with notable caveats.
- **Reporting Gaps**: Many studies clarify their outcomes are not group payoffs or efficiency per se.

# Main Findings Relevant To Prediction

### **Enabling peer punishment in PGGs generally leads to:**
- **Increase in efficiency (group payoff) compared to no-punishment control**, provided:
  - **Punishment is not too costly** (Eldakar et al., 2007; Dercole et al., 2013; Okada & Bingham, 2008).
  - **Punishment is effective** (high fine-to-cost ratio, Archetti & Scheuring, 2013; Okada & Bingham, 2008).
  - **Population structure is favorable** (spatial/local interactions rather than well-mixed, Oya & Ohtsuki, 2017; Nakamaru & Dieckmann, 2009).
  - **Punishment is pro-social (targeting defectors) and not anti-social** (Powers et al., 2012).
  - **Enforcement is honest and/or transparent** (Lee et al., 2015; Lee et al., 2017).

### **Caveats and Moderators:**
- **High punishment cost** or low punishment effectiveness can negate or reverse efficiency gains (Oya & Ohtsuki, 2017; Powers et al., 2012; Perry et al., 2018).
- **Presence of anti-social punishment** (punishing cooperators) or corruption can reduce or eliminate efficiency gain (Powers et al., 2012; Huang et al., 2018; Lee et al., 2015).
- **Group size effect**: Smaller groups typically exhibit stronger positive efficiency effects from punishment; larger groups risk diluted impact or increased coordination problems (Eldakar et al., 2007; Dercole et al., 2013; Archetti & Scheuring, 2013).
- **Number of rounds**: Multi-round/repeated games allow for efficiency improvement through punishment; one-shot games see reduced or no effect (Eldakar et al., 2007; Milinski & Rockenbach, 2012).
- **Probabilistic or graduated punishment** can optimize efficiency at high punishment costs (Jiao et al., 2020; Couto et al., 2020; Iwasa & Lee, 2013).
- **Benefit function shape**: Nonlinear (threshold/sigmoid) benefit functions can sometimes sustain efficiency without punishment; only linear benefit PGGs necessitate punishment for maximal efficiency (Archetti & Scheuring, 2013).
- **Reward mechanisms**: The effect of combining punishment with reward or reputation mechanisms is context-dependent but can yield higher efficiency than punishment alone (Milinski & Rockenbach, 2012; Fang & Chen, 2021).

### **Disagreement & Ambiguity:**
- Some models predict **neutral or negative efficiency effects** when punishment is poorly targeted, anti-social, or group conditions are unfavorable (Oya & Ohtsuki, 2017; Powers et al., 2012; Weibull & Salomonsson, 2006; Perry et al., 2018).
- Some models show **bistable outcomes** (either high or low efficiency depending on initial conditions or corruption rates) (Lee et al., 2015; Lee et al., 2017).

# Prediction Guidance

- **Punishment-enabled treatment efficiency** will, in standard PGG structures, **typically exceed control (no-punishment) efficiency**, but the magnitude and even direction of effect depend on specific game design dimensions and initial scenarios.
- For **prediction given control efficiency** and design dimensions:
  - **Low-cost, highly effective punishment**: Large expected increase in efficiency.
  - **High punishment cost or low effectiveness**: Small or negative effect; consider the risk of efficiency loss due to cost of punishment exceeding cooperation gains.
  - **Structured (spatial/local) interactions**: Punishment effects on efficiency are stronger than in well-mixed groups.
  - **Large groups or one-shot games**: Expect weaker or possibly no efficiency improvement.
  - **Antisocial punishment or opportunity for corruption**: Expect little or negative efficiency effect; model outcomes can be bistable.
  - **Graduated or probabilistic punishment**: Allows for cost-effective efficiency improvement in non-ideal parameter regimes.
  - **Nonlinear benefit functions**: In threshold or sigmoid benefit settings, enabling punishment may add little to efficiency already achieved by group dynamics.

- **If game includes rewards, communication, or reputation mechanisms**: Efficiency under punishment may be higher, especially if rewards are well targeted and/or reputation is visible.

# Design Dimensions Highlighted Across Papers

| Design Dimension           | Directly Informed                 | Indirect or Contextual | Sparse/Absent           |
|---------------------------|-----------------------------------|------------------------|------------------------|
| player_count              | Strong (almost all models)        |                        |                        |
| num_rounds                | Strong                            |                        |                        |
| mpcr                      | Strong                            |                        |                        |
| all_or_nothing            | Strong                            |                        |                        |
| punishment_cost           | Strong                            |                        |                        |
| punishment_tech           | Strong (effectiveness, fine)      |                        |                        |
| reward_exists/reward_cost/reward_tech | Moderate            | Often contextual        | Sometimes absent       |
| show_other_summaries      | Weak/Contextual                   | Some models            | Often absent           |
| show_n_rounds             | Occasionally direct                | More often contextual  | Mostly absent          |
| show_punishment_id        | Rare direct, some contextual      | More in resource/corruption models | Usually absent |
| chat                      | Rarely discussed, rarely direct   |                        | Present in few models  |
| default_contrib           | Only contextually (framing)       |                        | Generally absent       |

- **Most directly-informative for efficiency predictions under punishment**: `player_count`, `num_rounds`, `mpcr`, `all_or_nothing`, `punishment_cost`, `punishment_tech`.
- **Reward dimensions** (reward exists, cost, tech): Moderate coverage; effects on efficiency only modeled in some.
- **Feedback/visibility variables** (`show_other_summaries`, `show_punishment_id`, `show_n_rounds`, `chat`, `default_contrib`): Occasionally touched upon, but generally not systematically modeled in efficiency-outcome frameworks.

# Important Limitations

- **Empirical Evidence Gap**: The evidence base is heavily theoretical; few, if any, direct laboratory/field measurements of efficiency under experimental enabling/disabling of punishment.
- **Payoff-Behavior Mapping**: Many findings are inferred from cooperative behavior or strategy distributions, not from explicit group payoffs or efficiency.
- **Parameter Range Uncertainty**: Effects may change sign (from positive to negative) depending on unmodeled or outside-of-range design parameters, especially punishment cost, anti-social punishment, and corruption.
- **Population Structure Dependency**: Results may not generalize across spatially structured vs. well-mixed groups.
- **Ambiguity in Multidimensional Interactions**: Combinatorial interactions between dimensions (e.g., large groups with high punishment cost and communication) are rarely explored in depth.
- **No Coverage on Some Dimensions**: Information or framing effects (`chat`, `default_contrib`), full visibility or anonymity settings, and the practical implementation of institutions (feedback, identities) are underexplored.
- **Correlational/Mechanistic Reasoning Prevalent**: Causal (experimental) tests of the effect of enabling punishment on group efficiency are missing; most evidence is mechanistic or simulated.
- **Complex Real-World Institutional Details**: Settings with complex, evolving institutions or mixed incentive structures are only cursorily explored in some models and not systematically parameterized.
- **Reward Mechanism Interaction**: Combined effects of punishment and reward, and their optimal calibration, only explored in a few models.
- **Results May Be Non-Monotonic or Discontinuous**: Thresholds, phase transitions, and bistability often occur—so small parameter changes may produce outsized effects not well captured by simple linear predictions.
- **Qualitative Rather Than Quantitative Guidance in Some Cases**: Many models supply the *direction* or *qualitative logic* of effects, but not easily extractable quantitative effects for plug-in prediction models.

---

**In sum:** The theoretical literature provides moderately robust, mechanistically rich—but not empirically calibrated—evidence to predict that enabling peer punishment in public-goods games usually improves treatment efficiency relative to control. This inference is conditional on key design dimensions, especially punishment cost and effectiveness, group size, repetition, and institutional/parameter moderators (such as anti-social punishment/corruption and benefit function shape). However, important empirical gaps and parameter uncertainties mean that predictions should be made cautiously and with appropriate acknowledgment of context and limitations.
