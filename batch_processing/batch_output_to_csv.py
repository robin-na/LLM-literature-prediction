import argparse
import csv
import json
from pathlib import Path
import sys

BASE_FIELDS = [
    "data_id",
    "indep_var",
    "METHOD_empirical",
    "METHOD_experiment",
    "METHOD_lab",
    "METHOD_simulation",
    "METHOD_analytical",
    "CONFIG_playerCount",
    "CONFIG_numRounds",
    "CONFIG_allOrNothing",
    "CONFIG_defaultContribProp",
    "CONFIG_MPCR",
    "CONFIG_chat",
    "CONFIG_showOtherSummaries",
    "CONFIG_showPunishmentId",
    "CONFIG_showRewardId",
    "CONFIG_showNRounds",
    "CONFIG_punishmentExists",
    "CONFIG_punishmentCost",
    "CONFIG_punishmentTech",
    "CONFIG_rewardExists",
    "CONFIG_rewardCost",
    "CONFIG_rewardTech",
    "CONFIG_endowment",
    "DV_contributionRate",
    "DV_contributionAmount",
    "DV_efficiency",
    "DV_groupPayoff",
    "participant_country",
    "participant_age",
    "participant_gender",
    "participant_education",
    "experiment_environment",
    "other_game_info",
]

FIELDNAMES = ["custom_id"]
for field in BASE_FIELDS:
    FIELDNAMES.append(field)
    FIELDNAMES.append(f"{field}_reason")
    FIELDNAMES.append(f"{field}_confidence")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Convert OpenAI batch output JSONL to CSV."
    )
    parser.add_argument("--input-jsonl", required=True, help="Batch output JSONL file.")
    parser.add_argument(
        "--output-csv",
        help=(
            "Output CSV path. If omitted, writes to "
            "batch_processing/output_csv/<input_basename>.csv"
        ),
    )
    return parser.parse_args()


def extract_output_text(response_body):
    output_items = response_body.get("output", [])
    for item in output_items:
        if item.get("type") != "message":
            continue
        for content in item.get("content", []):
            if content.get("type") == "output_text":
                return content.get("text", "")
    return ""


def coerce_row(custom_id, experiment):
    row = {"custom_id": custom_id}
    for field in BASE_FIELDS:
        row[field] = experiment.get(field, "N/R")
        row[f"{field}_reason"] = experiment.get(f"{field}_reason", "")
        row[f"{field}_confidence"] = experiment.get(f"{field}_confidence", 0)
    return row


def main():
    args = parse_args()
    if args.output_csv:
        output_csv = args.output_csv
    else:
        input_path = Path(args.input_jsonl)
        output_dir = Path("batch_processing/output_csv")
        output_dir.mkdir(parents=True, exist_ok=True)
        output_csv = output_dir / f"{input_path.stem}.csv"

    rows = []
    with open(args.input_jsonl, encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                print(f"Warning: invalid JSON on line {line_number}", file=sys.stderr)
                continue

            custom_id = record.get("custom_id", "")
            response = record.get("response", {})
            if response.get("status_code") != 200:
                print(
                    f"Warning: non-200 response for {custom_id} on line {line_number}",
                    file=sys.stderr,
                )
                continue

            body = response.get("body", {})
            output_text = extract_output_text(body)
            if not output_text:
                print(
                    f"Warning: missing output text for {custom_id} on line {line_number}",
                    file=sys.stderr,
                )
                continue

            try:
                parsed = json.loads(output_text)
            except json.JSONDecodeError:
                print(
                    f"Warning: invalid JSON content for {custom_id} on line {line_number}",
                    file=sys.stderr,
                )
                continue

            experiments = parsed.get("experiments", [])
            if not isinstance(experiments, list):
                print(
                    f"Warning: experiments not a list for {custom_id} on line {line_number}",
                    file=sys.stderr,
                )
                continue

            for experiment in experiments:
                if not isinstance(experiment, dict):
                    continue
                rows.append(coerce_row(custom_id, experiment))

    with open(output_csv, "w", newline="", encoding="utf-8") as out_handle:
        writer = csv.DictWriter(out_handle, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
