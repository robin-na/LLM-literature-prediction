from __future__ import annotations

from textwrap import dedent


def normalize_text(text: str) -> str:
    return dedent(text).strip()


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


def build_final_report_prompt(
    column_defs: str,
    analysis_memo: str,
    paper_memo: str,
    source_mode: str = "both",
) -> str:
    source_mode = source_mode.lower().strip()
    if source_mode not in {"both", "data_only", "paper_only"}:
        source_mode = "both"

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
