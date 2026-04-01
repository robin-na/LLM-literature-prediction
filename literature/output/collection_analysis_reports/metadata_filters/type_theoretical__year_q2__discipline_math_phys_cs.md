# 1) Evidence Base

The literature set comprises **166 papers**, nearly all theoretical in nature, with almost no direct empirical or laboratory studies. Theoretical approaches include analytic modeling and simulation of public goods games (PGGs) and a broad range of social dilemma games, with some studies focused on related paradigms (prisoner's dilemma, resource management, auction games, multi-population games, etc.). The set is **broad with respect to conceptual mechanisms**—addressing punishment, reward, exclusion, institutional design, and other sanctioning or signaling mechanisms—but most studies **do not deliver empirical effect sizes or real-world validation**.

With respect to the **core prediction task**—estimating the effect of enabling punishment on efficiency in PGG-like settings, conditioned on game design dimensions and control efficiency—this evidence base is **strong in theoretical mechanisms** and rich in parameter explorations, but **lacks direct empirical calibration and real-world external validity**.

# 2) Task Relevance

**pgg_or_variant:**  
- The **majority** of studies are labeled `exact` or `close` for the public goods game or a direct variant (e.g., voluntary PGG, spatial PGG, threshold PGG).
- A significant minority use only **adjacent** models (e.g., n-person snowdrift, prisoner's dilemma, common-pool resource games), meaning not all findings are fully transferable.

**punishment_or_sanctions:**  
- Many studies are `exact` in modeling peer or institutional punishment (with explicit cost and impact), but a notable number are only `close` (e.g., ostracism, exclusion, reputation-loss as punishment), and some discuss **adjacent mechanisms** (e.g., commitment, indirect punishment, group exclusion).
- A few report on **reward** or alternative mechanisms without punishment, or on settings where punishment is only contextually discussed.

**efficiency_or_related_payoff_outcome:**  
- A **subset** of studies are `exact` on efficiency or total/group payoff outcome (i.e., ratio of achieved payoff to cooperative optimum).
- However, in a large number of papers, the primary outcomes are **behavioral**—contribution rates, cooperation frequencies, or strategy abundances. These are only **proximal or indirect evidence** for efficiency unless explicit mapping is provided.

# 3) Outcomes Measured In The Literature

- **Payoff-related outcomes**: About 30-40% of PGG or close-variant studies report some measure of efficiency, average group payoff, or welfare. These include analytical formulas, phase diagrams, or numeric ratios.
- **Non-payoff outcomes**: Many report only **cooperation rates, frequency of defectors/punishers, or prevalence of certain strategies**; these are routinely linked to efficiency, but are not the same and may be misleading where punishment is costly or behavioral changes don't translate into welfare gains (or losses).
- **Behavioral/structural outcomes**: Prevalence of antisocial punishment, mutation rates, network clustering, stability of cooperation, etc., are qualitatively discussed and often tied to mechanism analysis but not to explicit efficiency ratios.

**Explicit clarity**: Papers that tie contribution/cooperation rates to group payoff under given cost/benefit parameters support stronger inferences. Purely behavioral studies require caution and cannot substitute for direct efficiency evidence.

# 4) Main Findings Relevant To Prediction

**Empirical findings**: None—**all evidence is theoretical** (analytic or simulation-based). This limits learning about real-world parameterizations and effect size variability.

**Synthesis of core findings:**
- **Punishment can increase efficiency** in PGGs relative to the no-punishment control, especially when **punishment is not too costly**, the **effect on defectors is strong**, and **antisocial punishment is absent or suppressed** [(Wu et al., 2014); (Perc et al., 2017); (Szolnoki & Perc, 2013)].
- **Spatial structure** (local networks, clustering) substantially **enhances the effectiveness of punishment** for efficiency [(Szolnoki & Perc, 2017); (Oya & Ohtsuki, 2017)], but in **well-mixed populations**, punishment may be neutral or even detrimental [(Oya & Ohtsuki, 2017)].
- **High punishment cost, ineffective punishment, or substantial antisocial punishment** (punishment of cooperators) can **eliminate or even reverse efficiency gains**. In some models, the net group payoff is lower with punishment due to wasted effort [(Perc et al., 2017); (Hauser et al., 2014)].
- **Optimal punishment is intermediate**: Too weak, and defection persists; too strong, and costs undermine group efficiency [(Szolnoki & Perc, 2013); (Sui et al., 2017); (Ohdaira, 2017)].
- **Synergy factor (mpcr)**: Punishment is especially impactful at **low-to-intermediate mpcr** (settings where baseline efficiency is low); in high-mpcr (where cooperation is already likely), punishment adds little [(Wu et al., 2014); (Adami et al., 2016)].
- **Reward versus punishment**: Reward mechanisms can sometimes outperform punishment for efficiency, especially when rewards can be tax-based or pooled [(Yao & Chen, 2014); (Cong et al., 2016)]. The **presence of both** does not always add further efficiency unless carefully balanced.
- **Institutional Design**: **Decentralized/local or peer punishment** often yields higher efficiency than global/central punishment, especially in small groups or networked populations [(Vasconcelos et al., 2015); (Pacheco et al., 2014)].
- **Mechanism fragility**: **Corruption, mistaken identification, ineffective monitoring, and lack of second-order incentives** (punishing non-punishers or failing to reward rewarders) can cause the efficiency benefit of punishment to evaporate [(Lee et al., 2015); (Okada et al., 2015); (Lee et al., 2017)].

**Where studies report only behavioral outcomes:**  
Many studies find strong increases in cooperation or reductions in defection with punishment, but **do not account for the costs** incurred by punishers—which often means actual efficiency gains are smaller, or even negative, compared to the no-punishment control [(Vukov et al., 2013); (Chen et al., 2014)].

# 5) Prediction Guidance

**What is well supported:**
- If the **control game efficiency is low**, and game design settings are in the region where punishment is **not too costly** (low `punishment_cost`, high `punishment_magnitude`), **enabling punishment is likely to increase efficiency**—sometimes dramatically, especially in **spatial, locally structured, or voluntary participation games** [(Wu et al., 2014); (Szolnoki & Perc, 2013); (Vasconcelos et al., 2015)].
- The **magnitude of the efficiency gain** is highly **context-dependent** on design parameters:
    - **Player count**: Larger groups can dilute both cooperation and punishment effectiveness; some studies show positive effects with increasing group size **only when punishment effectiveness scales** accordingly [(Sui et al., 2017); (Vasconcelos et al., 2015)].
    - **Number of rounds and memory**: Sufficient rounds (and not too much memory) support enforcement, but excessive memory or rounds can cement inefficient equilibria [(Wu et al., 2014)].
    - **Cost and tech of punishment**: Only **moderate or low-cost, high-impact punishment** (favorable `punishment_cost`/`punishment_magnitude` ratio) is reliably positive for efficiency. If punishment is too expensive or ineffective, it can waste resources [(Szolnoki & Perc, 2013); (Adami et al., 2016)].

- In environments with **possible antisocial punishment** or **corrupt enforcers** (or where identification of punishers is poor), **do not expect efficiency gains**—and sometimes expect losses, especially if antisocial punishment is common [(Hauser et al., 2014); (Lee et al., 2015); (Thöni, 2014)].
- If **reward or reputation mechanisms** are present and strong, **punishment may add little** to efficiency, or can in some cases be counterproductive unless well balanced [(Cong et al., 2016); (Yao & Chen, 2014)].
- **Presence of voluntary participation** (as opposed to compulsory), local information, or spatial structure can **foster highly efficient cooperative equilibria with punishment**, sometimes with low cost [(Sasaki, 2014); (Szolnoki & Perc, 2013)].

**What is less supported or ambiguous:**
- The expected efficiency effect of punishment in **well-mixed, large, anonymous groups with high `punishment_cost` or high risk of antisocial punishment** is uncertain and may be negative [(Oya & Ohtsuki, 2017); (Hauser et al., 2014)].
- The literature is ambiguous on the **interaction between chat, communication, and punishment**; empirical and direct theoretical work on the role of chat (`chat` dimension) is essentially missing.

**Quantitative prediction**:  
Some studies provide **analytic or simulation formulas** (e.g., (Adami et al., 2016); (Wang et al., 2015)), but the mapping to empirical effect sizes is untested. Nonetheless, these formulas can be used for **relative predictions** (e.g., "efficiency increases with decreasing `punishment_cost`", or "punishment effectiveness threshold must be exceeded to realize gains").

# 6) Design Dimensions Highlighted Across Papers

**Directly informed (i.e., explicitly modeled and results mapped across):**
- `player_count`, `num_rounds`, `mpcr` (synergy factor), `punishment_cost`, and `punishment_tech` (**cost/effect formulas, tech of punishment—peer vs. institution—are central to most models**)
- `all_or_nothing` (continuous vs. discrete contributions), in many models
- `reward_exists`, `reward_cost`, `reward_tech` in studies contrasting punishment with reward [(Cong et al., 2016); (Yao & Chen, 2014)]

**Indirectly informed (studied but not always with efficiency outcomes):**
- `show_other_summaries`, `show_n_rounds`—sometimes discussed as elements of information availability, but rarely tied directly to efficiency in punishment-enabled games
- `show_punishment_id`—discussed only in certain contexts (e.g., **identification of corrupt enforcers**, (Lee et al., 2015)), but generally **absent as a systematically varied parameter**
- `default_contrib`—framing effects only contextually mentioned; rarely modeled for efficiency
- `chat`—almost entirely **missing** or contextually referenced rather than analyzed
- **Interaction between `reward_exists` and punishment** is analyzed in a few papers, with some suggesting **complementarity only at low cost**, but more often **punishment alone is sufficient** [(Szolnoki & Perc, 2013); (Cong et al., 2016)].

**Effectively missing or unavailable:**
- **No systematic results** on the effect of `chat`, information cascade features, or player anonymity on the punishment–efficiency relationship.
- **Sparse evidence** for complex reward technologies and their interaction with punishment (**reward_tech**).
- Details on **framing**, such as **`default_contrib`**, are contextual or missing from formal analysis.

# 7) Important Limitations

- **Lack of empirical evidence**: All findings are theoretical or simulation-based. There are **no laboratory or field experiments establishing causal effect sizes or calibrating prediction errors**.
- **Payoff-based versus behavioral outcomes**: Many studies **do not account for the cost of punishment** when reporting cooperation rates as a proxy for efficiency. Where only behavioral effects are reported, **increases in cooperation can come with net losses in efficiency** if punishment is costly.
- **Model assumptions**: Many models **presume homogeneous agents, static networks, or well-mixed populations**, which may not generalize to experimental or real-world environments.
- **Edge cases and exceptions**: Positive effects of punishment may **not generalize to all environments**; settings with **corruption, antisocial punishment, high cost, or low punishment efficacy** can yield **neutral or negative effects**.
- **Sparse coverage of design dimensions**: Several game features (e.g., chat, contribution framing, visibility, identity, and summary statistics) are **not systematically studied** for their moderating effects on efficiency.
- **No characterization of effect size variability**: Without empirical data, the range, variance, or expected noise in efficiency outcomes under punishment-enabled treatments is **unknown**.
- **Contextual and institutional moderators**: The effect of punishment can be **highly sensitive to institution-specific details** (peer versus centralized, voluntary versus compulsory, informational transparency), and these contextual features are not always parameterized nor clearly mapped to experimental design choices.

---

**In summary:**  
- Theoretical models converge that, under favorable design conditions (low punishment cost, high impact, local interaction, no antisocial punishment, proper incentive balance), **enabling punishment increases efficiency compared to control.**
- Significant **moderation by game dimensions** is demonstrated, including group size, cost/effect of punishment, spatial structure, and institutional mechanism.
- However, **in the absence of well-calibrated empirical data** and with frequent reliance on non-payoff outcomes, **predictions should be cautious, context-specific, and attuned to exceptions**. The literature offers **rich mechanistic logic and parameter dependencies**, but **does not support precise empirical prediction** for novel experimental designs.
