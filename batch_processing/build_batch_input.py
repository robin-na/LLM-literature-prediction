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
      "experiment_id": "string",
      "experiment_id_reason": "string",
      "experiment_id_confidence": number,
      "is_human_subject": boolean,
      "is_human_subject_reason": "string",
      "is_human_subject_confidence": number,
      "simulation": boolean,
      "simulation_reason": "string",
      "simulation_confidence": number,
      "analytical_model": boolean,
      "analytical_model_reason": "string",
      "analytical_model_confidence": number,
      "CONFIG_playerCount": number,
      "CONFIG_playerCount_reason": "string",
      "CONFIG_playerCount_confidence": number,
      "CONFIG_numRounds": number,
      "CONFIG_numRounds_reason": "string",
      "CONFIG_numRounds_confidence": number,
      "CONFIG_allOrNothing": 1 or 0,
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
      "CONFIG_showRewardId": 1 or 0,
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
      "CONFIG_punishmentTech": number,
      "CONFIG_punishmentTech_reason": "string",
      "CONFIG_punishmentTech_confidence": number,
      "CONFIG_rewardExists": 1 or 0,
      "CONFIG_rewardExists_reason": "string",
      "CONFIG_rewardExists_confidence": number,
      "CONFIG_rewardCost": number,
      "CONFIG_rewardCost_reason": "string",
      "CONFIG_rewardCost_confidence": number,
      "CONFIG_rewardTech": number,
      "CONFIG_rewardTech_reason": "string",
      "CONFIG_rewardTech_confidence": number,
      "CONFIG_endowment": number,
      "CONFIG_endowment_reason": "string",
      "CONFIG_endowment_confidence": number,
      "DV_contributionRate": number,
      "DV_contributionRate_reason": "string",
      "DV_contributionRate_confidence": number,
      "DV_efficiency": number,
      "DV_efficiency_reason": "string",
      "DV_efficiency_confidence": number,
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
You are given the full text of a paper. Extract every experiment or simulation described.
Each experiment becomes one object in the "experiments" array. If the paper reports
multiple conditions (e.g., Control/Treatment), create separate objects for each and
set experiment_id to the label used in the paper (e.g., "Experiment 1", "Control", "Treatment A").

Definitions and rules:
- is_human_subject: true if the experiment/observation uses human participants. false for simulations or analytical models.
- simulation: true if the study uses a numerical/computer simulation with no human subjects (e.g., agent-based model).
- analytical_model: true if the study is a formal mathematical/closed-form model (e.g., proofs, analytical derivations) with no human subjects.
- CONFIG_allOrNothing: 1 if players can contribute any amount; 0 if only all-or-nothing.
- CONFIG_defaultContribProp: 0 if endowment starts in private account; 1 if starts in public fund; otherwise proportion in public fund. Use N/A if no humans.
- CONFIG_MPCR: marginal per capita return (multiplier divided by group size). Use N/R if not reported.
- CONFIG_chat: 1 if communication is allowed; 0 otherwise. Use N/A if no humans.
- CONFIG_showOtherSummaries: 1 if participants see summaries of others' earnings/punishments/rewards; 0 otherwise.
- CONFIG_showPunishmentId / CONFIG_showRewardId: 1 if identities are revealed; 0 otherwise. Use N/A if the mechanism does not exist.
- CONFIG_showNRounds: 1 if total rounds or remaining rounds are displayed; 0 otherwise.
- CONFIG_punishmentExists / CONFIG_rewardExists: 1 or 0.
- CONFIG_punishmentCost / CONFIG_rewardCost: coins spent per unit. Use N/A if disabled.
- CONFIG_punishmentTech / CONFIG_rewardTech: magnitude per coin spent. Use N/A if disabled.
- DV_efficiency: group's total payoff divided by theoretical maximum if all fully contribute without punishing/rewarding. Use N/R if not reported.
- experiment_environment: one of "Online", "On site", "Field experiment", "Observational", "No human".
- For every field above, provide a corresponding "<field>_reason" and "<field>_confidence".
  - reason: short rationale of how you inferred the value (can be empty if directly stated).
  - confidence: number from 0 to 1 reflecting certainty (1 if unambiguous).
- Do not make up information. If a value cannot be inferred from the paper, use "N/R".
- If there is heterogeneity within an experiment (e.g., different players have varying endowments), record it explicitly in the relevant field(s) rather than choosing one condition or averaging.

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
