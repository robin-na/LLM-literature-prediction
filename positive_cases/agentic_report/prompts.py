from __future__ import annotations

from textwrap import dedent


def normalize_text(text: str) -> str:
    return dedent(text).strip()


VALID_SOURCE_MODES = {"both", "data_only", "paper_only"}
VALID_REPORT_STYLES = {
    "freeform",
    "structured",
    "quantitative",
    "narrative",
    "decision",
    "refined",
    "rules",
    "contrastive",
    "uncertainty",
    "ensemble",
}


def task_context_text() -> str:
    return normalize_text(
        """
        Prediction task context:
        - Each prediction instance provides values for 14 CONFIG parameters plus the average efficiency of the control game (punishment disabled).
        - The goal is to predict the average efficiency of the same game when punishment is enabled.
        - Efficiency is the ratio of the group’s total payoff to the total payoff of a fully cooperative group (everyone contributes fully every round).
        - Thus, efficiency = 1 means full cooperation; lower values indicate less cooperation.
        """
    )


def build_analysis_prompt(column_defs: str) -> str:
    return normalize_text(
        f"""
        You are a research analyst. Your goal is to produce a memo that helps a model predict how enabling punishment changes efficiency in public goods games.

        {task_context_text()}

        Use the attached dataset file `df_analysis_learn.csv` and run statistical analysis with Python. You should compute:
        - Overall mean efficiency with punishment vs without punishment.
        - Treatment effects within paired configurations (paired_config == True), using config-level aggregation.
        - Heterogeneity of treatment effects by key features (MPCR, playerCount, numRounds, chat, allOrNothing, defaultContribProp, showNRounds, showOtherSummaries, showPunishmentId, punishmentCost, punishmentTech, rewardExists, rewardCost, rewardMagnitude).
        - At least two simple predictive models (e.g., linear regression and random forest) to predict treatment effect or treatment efficiency, with top features and direction of effects.
        - Practical heuristics: conditions where punishment likely increases efficiency and where it likely does not.
        - Numerical guidance: quantify expected changes in efficiency for common ranges of key parameters.

        Output a concise Markdown memo with sections:
        1) Data Overview
        2) Global Effect of Punishment
        3) Heterogeneity Findings
        4) Predictive Modeling Signals
        5) Practical Heuristics
        6) Quantitative Summary (include tables with numeric estimates)
        7) Caveats

        Include compact Markdown tables for key aggregates, and at least one model-results table
        (e.g., regression coefficients with standard errors or feature importances with values).

        Column definitions:
        {column_defs}
        """
    )


def build_paper_summary_prompt() -> str:
    return normalize_text(
        f"""
        You are summarizing the published PGG manuscript for the purpose of improving prediction accuracy.
        Use file search to find relevant sections in the attached paper. Focus on experimental design, definitions of efficiency, and key findings on punishment and heterogeneity.
        Do not include any final-answer formatting instructions in your summary.

        {task_context_text()}

        Output a concise Markdown memo with sections:
        1) Design & Data
        2) Efficiency Definition
        3) Main Findings on Punishment
        4) Heterogeneity / Moderators
        5) Notes for Prediction
        """
    )


def build_paper_retrieval_report_prompt(
    column_defs: str,
    report_style: str = "narrative",
) -> str:
    report_style = report_style.lower().strip()
    if report_style not in VALID_REPORT_STYLES:
        report_style = "narrative"

    style_requirements = build_report_style_requirements(report_style)

    return normalize_text(
        f"""
        You are writing a prediction-support report to help estimate how enabling punishment changes efficiency in new public goods games.

        Use file search over the attached paper(s).

        Requirements:
        - Base the report strictly on what the paper(s) support.
        - Do not speculate beyond the retrieved evidence.
        - If a requested quantity, moderator, or rule is not clearly supported by the paper(s), say that explicitly.
        - Explain the key variables and how they map to experimental design.
        - Provide predictive guidance that is useful for forecasting, while remaining faithful to the paper evidence.
        - Output in Markdown with clear section headers.
        - Include numerical estimates and tables only when they are directly supported by the paper evidence.
        - Follow these additional style requirements exactly:
        {style_requirements}

        {task_context_text()}

        Include these sections:
        1) Title
        2) Abstract
        3) Background & Definitions (explicitly restate the prediction task: given CONFIGs plus control efficiency, predict treatment efficiency)
        4) Data & Variables (explicitly define the 14 CONFIG parameters used in prediction, plus CONFIG_punishmentExists because it distinguishes control from treatment)
        5) Empirical Patterns (punishment effects and heterogeneity)
        6) Predictive Guidance
        7) Limitations & Missing Evidence
        8) How To Use This For Predictions (concise bullet list)

        Column definitions:
        {column_defs}
        """
    )


def build_final_report_prompt(
    column_defs: str,
    analysis_memo: str,
    paper_memo: str,
    source_mode: str = "both",
    report_style: str = "freeform",
) -> str:
    source_mode = source_mode.lower().strip()
    report_style = report_style.lower().strip()
    if source_mode not in VALID_SOURCE_MODES:
        source_mode = "both"
    if report_style not in VALID_REPORT_STYLES:
        report_style = "freeform"

    if source_mode == "data_only":
        source_note = (
            "Source mode: data_only. Use ONLY the analysis memo derived from the CSV. "
            "Do not introduce evidence or claims from the paper."
        )
    elif source_mode == "paper_only":
        source_note = (
            "Source mode: paper_only. Use ONLY the paper memo. "
            "Do not introduce evidence or claims from the data analysis. "
            "If the paper lacks needed numbers, state the gaps explicitly."
        )
    else:
        source_note = "Source mode: both. Use both the analysis memo and the paper memo."

    memo_blocks = []
    if source_mode in {"both", "data_only"}:
        memo_blocks.append(
            normalize_text(
                f"""
                Analysis memo:
                ---
                {analysis_memo}
                ---
                """
            )
        )
    if source_mode in {"both", "paper_only"}:
        memo_blocks.append(
            normalize_text(
                f"""
                Paper memo:
                ---
                {paper_memo}
                ---
                """
            )
        )

    memos_text = "\n\n".join(memo_blocks)

    style_requirements = build_report_style_requirements(report_style)

    return normalize_text(
        f"""
        You are writing a prediction-support paper to help a model estimate how enabling punishment changes efficiency in new public goods games.

        Requirements:
        - Use the available memos as primary evidence (depending on the selected source mode).
        - {source_note}
        - Explain the key variables and how they map to experimental design.
        - Provide actionable predictive guidance, not just a summary.
        - Keep the report grounded in the data and the published paper.
        - Output in Markdown with clear section headers.
        - Target length: 800 to 1400 words.
        - Do NOT include any final-answer formatting or \"Final Answer\" template.
        - Assume the protocol and online environment are consistent across studies; differences are driven by the CONFIG parameters.
        - Include concrete numerical estimates and tables drawn from the available evidence.
        - Report style: {report_style}
        - Follow these additional style requirements exactly:
        {style_requirements}

        {task_context_text()}

        Include these sections:
        1) Title
        2) Abstract
        3) Background & Definitions (explicitly restate the prediction task: given 14 CONFIGs plus control efficiency, predict treatment efficiency)
        4) Data & Variables (explicitly list and define these 14 CONFIG parameters: CONFIG_playerCount, CONFIG_numRounds, CONFIG_MPCR, CONFIG_allOrNothing, CONFIG_chat, CONFIG_defaultContribProp with 0/1 coding, CONFIG_punishmentCost, CONFIG_punishmentMagnitude, CONFIG_showOtherSummaries, CONFIG_showNRounds, CONFIG_showPunishmentId, CONFIG_rewardExists, CONFIG_rewardCost, CONFIG_rewardMagnitude)
        5) Empirical Patterns (punishment effects and heterogeneity)
        6) Quantitative Summary (tables with numeric effects and model outputs)
        7) Predictive Guidance (rules of thumb and feature interactions with numeric ranges)
        8) Limitations & Open Questions
        9) How To Use This For Predictions (concise bullet list)

        Column definitions:
        {column_defs}

        {memos_text}
        """
    )


def build_report_style_requirements(report_style: str) -> str:
    report_style = report_style.lower().strip()
    if report_style == "structured":
        return normalize_text(
            """
            - Prefer compact sections, bullets, and tables over long narrative paragraphs.
            - Explicitly include a "Moderator Matrix" table with each key variable, likely effect direction, confidence, and interaction notes.
            - Explicitly include a "Rules of Thumb" section formatted as if-then statements.
            - Keep prose concise and operational.
            """
        )
    if report_style == "quantitative":
        return normalize_text(
            """
            - Prioritize numeric evidence over narrative explanation.
            - Put tables first whenever possible.
            - Include at least three quantitative tables: overall effects, moderator effects, and prediction guidance ranges.
            - Minimize qualitative wording unless it clarifies how to use the numbers.
            """
        )
    if report_style == "narrative":
        return normalize_text(
            """
            - Keep the report narrative-driven and readable, with prose as the default form.
            - Use tables only when they clarify the paper evidence.
            """
        )
    if report_style == "decision":
        return normalize_text(
            """
            - Keep the report compact, operational, and prediction-oriented.
            - Include a "Moderator Matrix" table with each key variable, likely direction, confidence, and evidence note.
            - Include a "Decision Rules" section written as if-then statements.
            - Every rule must clearly distinguish strongly supported guidance from weak or missing evidence.
            - Do not invent numeric thresholds or conditional ranges unless they are clearly supported by the paper.
            """
        )
    if report_style == "refined":
        return normalize_text(
            """
            - Produce a clean final report only.
            - The report should read like a corrected and tightened version of an earlier draft.
            - Eliminate unsupported claims, vague wording, and claims that are not grounded in the supplied memos.
            - Be explicit about uncertainty when evidence is mixed or weak.
            """
        )
    if report_style == "rules":
        return normalize_text(
            """
            - Make the report operational and rule-first rather than essay-first.
            - Include a ranked predictor list, then a rules section built from if-then statements.
            - Each rule should include direction of effect and an approximate numeric range when available.
            - Keep narrative explanation minimal and subordinate to actionable guidance.
            """
        )
    if report_style == "contrastive":
        return normalize_text(
            """
            - Explicitly separate where the paper memo and analysis memo agree, partially agree, or disagree.
            - Include an "Agreement / Disagreement Matrix" table.
            - Reconcile conflicts and explain which evidence should dominate prediction when they diverge.
            - The final predictive guidance should clearly indicate whether it is supported by paper, data, or both.
            """
        )
    if report_style == "uncertainty":
        return normalize_text(
            """
            - For every major predictive claim, include an explicit confidence label such as high, medium, or low.
            - Distinguish stable effects from interaction-heavy or weakly supported effects.
            - Include a section titled "High-Confidence Rules" and another titled "Low-Confidence / Unstable Regions".
            - Preserve actionable guidance, but make uncertainty visible everywhere it matters.
            """
        )
    if report_style == "ensemble":
        return normalize_text(
            """
            - Produce a final integrated report that combines strengths of multiple drafting styles.
            - The final result should be compact, operational, quantitatively grounded, and internally consistent.
            - Favor content that survives across multiple candidate draft forms over content that appears only once.
            """
        )
    return normalize_text(
        """
        - Write a balanced narrative synthesis with clear headings, concrete numbers, and actionable guidance.
        - Use prose as the default form, with tables where helpful.
        """
    )


def build_report_refinement_prompt(
    column_defs: str,
    analysis_memo: str,
    paper_memo: str,
    draft_report: str,
    source_mode: str = "both",
) -> str:
    source_mode = source_mode.lower().strip()
    if source_mode not in VALID_SOURCE_MODES:
        source_mode = "both"

    report_prompt = build_final_report_prompt(
        column_defs=column_defs,
        analysis_memo=analysis_memo,
        paper_memo=paper_memo,
        source_mode=source_mode,
        report_style="refined",
    )

    return normalize_text(
        f"""
        You are revising a draft prediction-support report.

        Your job:
        - Audit the draft for unsupported claims, leakage across source constraints, vague statements, and weak quantitative grounding.
        - Rewrite the report so it is tighter, better supported, and more useful for prediction.
        - Preserve useful content from the draft only when it is supported by the memos.
        - Output only the improved final report in Markdown.

        Draft report:
        ---
        {draft_report}
        ---

        Use these report requirements for the rewrite:
        {report_prompt}

        Column definitions:
        {column_defs}
        """
    )


def build_report_ensemble_prompt(
    column_defs: str,
    analysis_memo: str,
    paper_memo: str,
    structured_draft: str,
    quantitative_draft: str,
    source_mode: str = "both",
) -> str:
    source_mode = source_mode.lower().strip()
    if source_mode not in VALID_SOURCE_MODES:
        source_mode = "both"

    report_prompt = build_final_report_prompt(
        column_defs=column_defs,
        analysis_memo=analysis_memo,
        paper_memo=paper_memo,
        source_mode=source_mode,
        report_style="ensemble",
    )

    return normalize_text(
        f"""
        You are synthesizing a final prediction-support report from two candidate drafts.

        Your job:
        - Merge the strongest parts of both drafts into one final report.
        - Prefer claims that are numerically grounded, operational for prediction, and consistent with the supplied memos.
        - Remove redundancy, unsupported claims, and stylistic clutter.
        - Output only the final report in Markdown.

        Structured draft:
        ---
        {structured_draft}
        ---

        Quantitative draft:
        ---
        {quantitative_draft}
        ---

        Final report requirements:
        {report_prompt}

        Column definitions:
        {column_defs}
        """
    )
