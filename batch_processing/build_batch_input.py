import argparse
import csv
import json
from pathlib import Path
import sys

SYSTEM_PROMPT = (
    "You extract structured experimental design details from research papers about "
    "cooperation and punishment. Provide only valid JSON with the specified schema, "
    "using numeric types for numeric values. Use 'N/R' for not reported and 'N/A' for "
    "not applicable."
)

OUTPUT_SCHEMA_DESCRIPTION = """
Return a JSON object with this structure (use actual values from the paper):
{
  "experiments": [
    {
      "data_id": "string",
      "data_id_reason": "string",
      "data_id_confidence": number,
      "indep_var": "string",
      "indep_var_reason": "string",
      "indep_var_confidence": number,
      "METHOD_empirical": boolean,
      "METHOD_empirical_reason": "string",
      "METHOD_empirical_confidence": number,
      "METHOD_experiment": boolean,
      "METHOD_experiment_reason": "string",
      "METHOD_experiment_confidence": number,
      "METHOD_lab": boolean,
      "METHOD_lab_reason": "string",
      "METHOD_lab_confidence": number,
      "METHOD_simulation": boolean,
      "METHOD_simulation_reason": "string",
      "METHOD_simulation_confidence": number,
      "METHOD_analytical": boolean,
      "METHOD_analytical_reason": "string",
      "METHOD_analytical_confidence": number,
      "CONFIG_playerCount": number,
      "CONFIG_playerCount_reason": "string",
      "CONFIG_playerCount_confidence": number,
      "CONFIG_numRounds": number,
      "CONFIG_numRounds_reason": "string",
      "CONFIG_numRounds_confidence": number,
      "CONFIG_allOrNothing": 1 or 0 or "N/A",
      "CONFIG_allOrNothing_reason": "string",
      "CONFIG_allOrNothing_confidence": number,
      "CONFIG_defaultContribProp": number,
      "CONFIG_defaultContribProp_reason": "string",
      "CONFIG_defaultContribProp_confidence": number,
      "CONFIG_MPCR": number,
      "CONFIG_MPCR_reason": "string",
      "CONFIG_MPCR_confidence": number,
      "CONFIG_chat": 1 or 0,
      "CONFIG_chat_reason": "string",
      "CONFIG_chat_confidence": number,
      "CONFIG_showOtherSummaries": 1 or 0,
      "CONFIG_showOtherSummaries_reason": "string",
      "CONFIG_showOtherSummaries_confidence": number,
      "CONFIG_showPunishmentId": 1 or 0,
      "CONFIG_showPunishmentId_reason": "string",
      "CONFIG_showPunishmentId_confidence": number,
      "CONFIG_showRewardId": 1 or 0 or "N/A",
      "CONFIG_showRewardId_reason": "string",
      "CONFIG_showRewardId_confidence": number,
      "CONFIG_showNRounds": 1 or 0,
      "CONFIG_showNRounds_reason": "string",
      "CONFIG_showNRounds_confidence": number,
      "CONFIG_punishmentExists": 1 or 0,
      "CONFIG_punishmentExists_reason": "string",
      "CONFIG_punishmentExists_confidence": number,
      "CONFIG_punishmentCost": number,
      "CONFIG_punishmentCost_reason": "string",
      "CONFIG_punishmentCost_confidence": number,
      "CONFIG_punishmentTech": number or "N/A",
      "CONFIG_punishmentTech_reason": "string",
      "CONFIG_punishmentTech_confidence": number,
      "CONFIG_rewardExists": 1 or 0 or "N/A",
      "CONFIG_rewardExists_reason": "string",
      "CONFIG_rewardExists_confidence": number,
      "CONFIG_rewardCost": number,
      "CONFIG_rewardCost_reason": "string",
      "CONFIG_rewardCost_confidence": number,
      "CONFIG_rewardTech": number or "N/A",
      "CONFIG_rewardTech_reason": "string",
      "CONFIG_rewardTech_confidence": number,
      "CONFIG_endowment": number,
      "CONFIG_endowment_reason": "string",
      "CONFIG_endowment_confidence": number,
      "IVs": ["string", "..."],
      "IVs_reason": "string",
      "IVs_confidence": number,
      "DVs": ["string", "..."],
      "DVs_reason": "string",
      "DVs_confidence": number,
      "DVs_Definitions": {"dv_name": "definition", "...": "..."},
      "DVs_Definitions_reason": "string",
      "DVs_Definitions_confidence": number,
      "DV_efficiencyReported": 1 or 0,
      "DV_efficiencyReported_reason": "string",
      "DV_efficiencyReported_confidence": number,
      "source_data": "Internal" or "External",
      "source_data_reason": "string",
      "source_data_confidence": number,
      "participant_country": "string",
      "participant_country_reason": "string",
      "participant_country_confidence": number,
      "participant_age": "string",
      "participant_age_reason": "string",
      "participant_age_confidence": number,
      "participant_gender": "string",
      "participant_gender_reason": "string",
      "participant_gender_confidence": number,
      "participant_education": "string",
      "participant_education_reason": "string",
      "participant_education_confidence": number,
      "experiment_environment": "Online" | "On site" | "Field experiment" | "Observational" | "No human",
      "experiment_environment_reason": "string",
      "experiment_environment_confidence": number,
      "other_game_info": "string",
      "other_game_info_reason": "string",
      "other_game_info_confidence": number
    }
  ]
}
""".strip()

INSTRUCTION_TEXT = """
You are given the full text of a paper. Extract every experiment, simulation, or observational
condition described. Each object must be at the treatment/control (condition) level. If a
paper groups multiple conditions under one study, create separate objects for each condition.

STRICT NON-INFERENCE RULE (applies to every field):
Only report a value when the paper explicitly states it or when it is directly and unambiguously
computable from reported numbers. Do NOT infer values from silence, convention, or reasonable
assumption. Specifically:
  - CONFIG fields (design parameters): if a parameter is not explicitly described for this
    condition, use N/A — not 0 or false. Absence of mention ≠ "the feature is absent".
  - DV fields (outcome measures): if a value is not reported and cannot be computed from reported
    numbers, use N/R.
  - The only exception is when the field is inherently binary and one value is logically implied
    by the other (e.g., CONFIG_allOrNothing: if the paper says "continuous contribution choice",
    you may code 1; if it says "all-or-nothing", code 0). Even then, code N/A if neither is stated.

Definitions and rules:
- data_id: the name/description of the condition as the paper describes it (e.g., "Experiment 1 – Control").
- indep_var: the independent variable(s) varied across conditions and the specific value(s) for this row.
- METHOD_empirical: true if the study uses human participants (same meaning as is_human_subject).
- METHOD_experiment: true if it is a controlled experiment; false if observational; false if not empirical.
- METHOD_lab: true if lab experiment; false if field experiment; false if not an experiment.
- METHOD_simulation: true if the study uses a numerical/computer simulation with no human subjects (e.g., agent-based model).
- METHOD_analytical: true if the study is a formal mathematical/closed-form model (e.g., proofs, analytical derivations) with no human subjects.
- CONFIG_allOrNothing: 1 ONLY if the paper explicitly states that players choose a SPECIFIC AMOUNT to contribute (e.g., "between 0 and 20 tokens", "any number from 0 to their endowment"). 0 if the choice is explicitly binary (all-or-nothing, cooperate/defect, two discrete actions). N/A if the paper does not explicitly describe how contributions are structured — do NOT infer 1 from silence or from the fact that it is a PGG paper. WARNING: the field name is counterintuitive — 1 means specific amounts (continuous), not all-or-nothing.
- CONFIG_defaultContribProp: 0 if endowment starts in private account; 1 if starts in public fund; otherwise proportion in public fund. Use N/A if no humans or if not explicitly stated.
- CONFIG_MPCR: marginal per capita return (multiplier divided by group size). Use N/R if not reported.
- CONFIG_playerCount: the number of strategic decision-makers in ONE group/match — not the total number of participants in the study. When teams send a representative, count the number of teams (not individuals per team). When there are third-party punishers or observers, count them as additional players in the group. Prefer the unit that governs the strategic interaction, not the prose headcount.
- CONFIG_chat: 1 if the paper explicitly states that participants can communicate freely (including structured or numeric messages). N/A if communication is not mentioned anywhere in the paper — do NOT code 0 from silence; code 0 only if the paper explicitly states communication was prohibited.
- CONFIG_showOtherSummaries: 1 if the paper explicitly states that participants see individual-level PAYOFFS or EARNINGS of other group members after each round, or explicit punishment/reward activity that reveals relative earnings. 0 if participants only see others' CONTRIBUTIONS (the default in PGGs — contribution visibility alone is NOT enough for 1), their own payoff, or group aggregates. N/A if post-round feedback is not described. KEY: seeing others' contributions ≠ seeing others' payoffs/earnings; only payoff/earnings visibility warrants 1.
- CONFIG_showPunishmentId: 1 if punished players can identify punishers (when punishment exists); 0 only if the paper clearly states punishment is anonymous; N/A if punishment does not exist in this condition OR if the paper does not address whether identities are revealed.
- CONFIG_showRewardId: 1 if reward recipients can identify rewarders; 0 only if the paper clearly states rewarding is anonymous; N/A if there is no reward mechanism in this condition, or if the paper does not address whether identities are visible — do not infer 0 from silence.
- CONFIG_showNRounds: 1 ONLY if the paper explicitly states that the total number of rounds or remaining rounds is displayed to participants. Do NOT infer from rounds being fixed or "common knowledge". N/A if not explicitly stated.
- CONFIG_punishmentExists: 1 only if this specific condition explicitly includes a punishment mechanism. N/A if punishment is not explicitly described for this condition — do NOT infer from other conditions in the paper or from the paper's general design.
- CONFIG_rewardExists: 1 only if the paper clearly describes a reward mechanism for this condition. N/A if rewards are not mentioned or are ambiguous — do NOT default to 0 from silence (silence → N/A, not 0). Code 0 only if the paper explicitly states no reward mechanism exists.
- CONFIG_punishmentCost: coins/tokens spent per unit of punishment assigned. N/A if punishment does not exist in this condition OR if the cost is not explicitly stated numerically.
- CONFIG_punishmentTech: reduction in the TARGET's payoff per coin the PUNISHER spends = punishmentMagnitude / punishmentCost (e.g., punisher spends 1 coin and target loses 3 → 3; punisher spends 2 coins and target loses 3 → 1.5). N/A if punishment does not exist in this condition. N/R if either cost or magnitude is not explicitly stated.
- CONFIG_rewardCost: coins/tokens spent per unit of reward. N/A if reward does not exist in this condition OR if not explicitly stated numerically.
- CONFIG_rewardTech: increase in the RECIPIENT's payoff per coin the REWARDER spends = rewardMagnitude / rewardCost (e.g., rewarder spends 1 coin and recipient gains 3 → 3; rewarder spends 2 coins and recipient gains 3 → 1.5). N/A if reward does not exist in this condition. N/R if either cost or magnitude is not explicitly stated.
- IVs: a JSON array listing the independent variables (experimental factors) that are actually manipulated/varied across conditions in THIS paper, as applicable to THIS specific condition. Use short snake_case names (e.g., "punishment_mechanism", "communication", "group_size" only if varied). Include only factors that differ across conditions — not fixed parameters. Do NOT include outcome measures (those go in DVs). All conditions in a paper share the same set of IVs since the IVs define the paper's design.
- DVs: a JSON array listing the primary dependent variables measured and analyzed in THIS specific condition/treatment — the outcomes the authors are trying to measure and explain for this row. Important distinctions:
  * List BOTH individual-level and group-level contribution measures if the paper reports both (e.g., "individual_contribution" for each player's tokens contributed AND "group_contribution" for the group average or total — these are different DVs).
  * Distinguish punishment assigned/received (points given to or received from others) from punishment expenditure (tokens spent on punishment) — only include whichever the paper actually reports for this condition.
  * Do NOT include independent variables (parameters manipulated across conditions: endowment, group size, MPCR, punishment existence, etc.), nor auxiliary quantities reported only in passing.
  * DVs may differ across conditions: a no-punishment condition should NOT list punishment-related DVs.
  Use short snake_case names. Example: ["individual_contribution", "group_contribution", "efficiency"] for a no-punishment condition; ["individual_contribution", "group_contribution", "punishment_assigned", "punishment_received", "net_earnings"] for a punishment condition.
- DVs_Definitions: a JSON object mapping each DV name from the DVs list for THIS condition to a brief plain-English definition of how that outcome is measured in this paper. Keys must exactly match the entries in DVs for this row. Example: {"individual_contribution": "tokens each player contributes to the public account per round", "group_contribution": "average contribution across all group members as a percentage of maximum possible", "efficiency": "actual group payoff divided by maximum possible cooperative payoff"}.
- DV_efficiencyReported: 1 if the paper reports, computes, or analyzes an efficiency measure (actual group payoff as a fraction of the theoretical maximum cooperative payoff) for ANY condition in the paper. 0 if efficiency is never reported or computed anywhere in the paper. This is a PAPER-LEVEL field — use the same value in every row for a given paper. Do not code 0 for a row just because efficiency is not the focus of that specific condition; if efficiency appears anywhere in the paper, code 1 for all rows.
- source_data: PAPER-LEVEL field (same value for every row). "Internal" if the authors collected the experimental data themselves for this study (lab, online, or field experiment run by these authors). "External" if the data was borrowed from a different experiment or external source (reanalysis of another paper's data, archival data, data collected by other researchers for a different study).
- experiment_environment: one of "Online", "On site", "Field experiment", "Observational", "No human".
- For every field above, provide a corresponding "<field>_reason" and "<field>_confidence".
  - reason: short rationale of how you inferred the value (can be empty if directly stated).
  - confidence: number from 0 to 1 reflecting certainty (1 if unambiguous).
- If a DV value is not explicitly reported but can be computed from reported facts
  (e.g., endowment, contribution amounts, group size, multipliers), calculate it and explain
  the derivation briefly in the reason field.
- If there is heterogeneity within an experiment (e.g., different players have varying endowments),
  record it explicitly in the relevant field(s) rather than choosing one condition or averaging.

Return only valid JSON matching the schema.
""".strip()


def parse_args():
    parser = argparse.ArgumentParser(
        description="Build OpenAI batch input JSONL for paper extraction."
    )
    parser.add_argument(
        "--csv-path",
        default="PGG_papers/WoS_251031_eligible.csv",
        help="Path to WoS_251031_eligible.csv",
    )
    parser.add_argument(
        "--markdown-dir",
        required=True,
        help="Directory containing markdown paper files.",
    )
    parser.add_argument(
        "--model",
        default="gpt-5.1",
        help="OpenAI model name for batch requests.",
    )
    parser.add_argument(
        "--custom-ids",
        nargs="*",
        help="Optional list of custom_id values to process. If omitted, process all rows.",
    )
    parser.add_argument(
        "--output",
        default="batch_processing/inputs/batch_input.jsonl",
        help="Output JSONL path.",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=None,
        help=(
            "Sampling temperature. If omitted, the parameter is not sent "
            "(useful for reasoning models that don't support temperature)."
        ),
    )
    return parser.parse_args()


def load_custom_ids(csv_path):
    with open(csv_path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if "custom_id" not in reader.fieldnames:
            raise ValueError("custom_id column missing from CSV")
        return [row["custom_id"].strip() for row in reader if row.get("custom_id")]


def find_markdown_path(markdown_dir, custom_id):
    direct_path = Path(markdown_dir) / custom_id
    if direct_path.exists():
        return direct_path
    matches = list(Path(markdown_dir).rglob(custom_id))
    if matches:
        return matches[0]
    return None


def build_user_prompt(paper_text):
    return "\n\n".join([
        OUTPUT_SCHEMA_DESCRIPTION,
        INSTRUCTION_TEXT,
        "Paper text:\n" + paper_text,
    ])


def main():
    args = parse_args()
    custom_ids = load_custom_ids(args.csv_path)
    selected_ids = custom_ids
    if args.custom_ids:
        selected_ids = [cid for cid in custom_ids if cid in set(args.custom_ids)]

    if not selected_ids:
        raise ValueError("No matching custom_id values found.")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as out_handle:
        for custom_id in selected_ids:
            markdown_path = find_markdown_path(args.markdown_dir, custom_id)
            if not markdown_path:
                print(
                    f"Warning: markdown file not found for {custom_id}",
                    file=sys.stderr,
                )
                continue

            paper_text = markdown_path.read_text(encoding="utf-8")
            user_prompt = build_user_prompt(paper_text)
            request_body = {
                "model": args.model,
                "input": [
                    {
                        "role": "system",
                        "content": [{"type": "input_text", "text": SYSTEM_PROMPT}],
                    },
                    {
                        "role": "user",
                        "content": [{"type": "input_text", "text": user_prompt}],
                    },
                ],
                "text": {"format": {"type": "json_object"}},
            }
            if args.temperature is not None:
                request_body["temperature"] = args.temperature

            record = {
                "custom_id": custom_id,
                "method": "POST",
                "url": "/v1/responses",
                "body": request_body,
            }
            out_handle.write(json.dumps(record, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
