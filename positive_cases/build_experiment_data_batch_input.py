from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd


SYSTEM_PROMPT = """We have conducted multiple public goods game experiments with varying experimental designs, to measure the effect of punishment in cooperative settings under various environments.
Your task is to predict how enabling a punishment mechanism to a specific game changes the ***efficiency*** compared to the same game with punishment disabled.
According to our experiments, whether punishment increases efficiency or not is highly dependent on a lot of dimensions in experiment design, and it is your job to navigate this heterogeneity and make accurate predictions.

***Efficiency*** is the ratio between the game players' behavior and that of a fully-cooperative group (i.e. a group in which all members contribute their full endowment in every round)
In other words, efficiency measures how close a group's total payoff is, compared to that of a group that always cooperated (i.e. always contributes the entire endowment, and benefits maximally from the multiplier).
An efficiency value of 100% means that a group earned the same amount of coins as a hypothetical group that always cooperated.

For example, let's say a game has 5 players playing 10 rounds where 20 coins are given to each player per round and the multiplier for each contributed coin is 3.
In this case, the earning of a hypothetical "always cooperating" group is 5*10*20*3=3000 coins, while the earning of a hypothetical "never cooperating" group is 1000 coins.
Hence, the efficiency is 100% for the always cooperating group and 33% for the never cooperating group.

Your output should strictly be a prediction value with integer only (e.g., 33% should output 33 and nothing else)."""

SYSTEM_PROMPT_REASONING = """We have conducted multiple public goods game experiments with varying experimental designs, to measure the effect of punishment in cooperative settings under various environments.
Your task is to predict how enabling a punishment mechanism to a specific game changes the ***efficiency*** compared to the same game with punishment disabled.
According to our experiments, whether punishment increases efficiency or not is highly dependent on a lot of dimensions in experiment design, and it is your job to navigate this heterogeneity and make accurate predictions.

***Efficiency*** is the ratio between the game players' behavior and that of a fully-cooperative group (i.e. a group in which all members contribute their full endowment in every round)
In other words, efficiency measures how close a group's total payoff is, compared to that of a group that always cooperated (i.e. always contributes the entire endowment, and benefits maximally from the multiplier).
An efficiency value of 100% means that a group earned the same amount of coins as a hypothetical group that always cooperated.

For example, let's say a game has 5 players playing 10 rounds where 20 coins are given to each player per round and the multiplier for each contributed coin is 3.
In this case, the earning of a hypothetical "always cooperating" group is 5*10*20*3=3000 coins, while the earning of a hypothetical "never cooperating" group is 1000 coins.
Hence, the efficiency is 100% for the always cooperating group and 33% for the never cooperating group.

Respond with a JSON object only:
{
  "reasoning": "brief explanation of how you derived the prediction",
  "prediction": <integer efficiency percent>
}
The value in "prediction" must be an integer with no percent sign."""

PROMPT_EXPERIMENT_DATA = """Below is a list of public-goods-game experiments with their configuration values and observed outcomes.
Each experiment includes both:
- efficiency_np: observed efficiency with punishment disabled (control)
- efficiency_p: observed efficiency with punishment enabled (treatment)

Make predictions based on what you can learn from these experiments."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build OpenAI merged batch JSONLs using augmentation from raw experiment data "
            "(validation set and learn set)."
        )
    )
    parser.add_argument(
        "--target-df",
        type=Path,
        default=Path("input/pgg_CONFIGmerged_validation.csv"),
        help="Target df_pgg used to build the 20 prediction instances.",
    )
    parser.add_argument(
        "--augment-validation",
        type=Path,
        default=Path("input/pgg_CONFIGmerged_validation.csv"),
        help="CSV used as in-sample augmentation case.",
    )
    parser.add_argument(
        "--augment-learn",
        type=Path,
        default=Path("input/pgg_CONFIGmerged_learn.csv"),
        help="CSV used as out-of-sample augmentation case.",
    )
    parser.add_argument(
        "--model",
        default="gpt-4.1",
        help="OpenAI model for /v1/chat/completions batch requests.",
    )
    parser.add_argument(
        "--output-nonreasoning",
        type=Path,
        default=Path("openAI_batch_input/prediction_experiment_data_merged_41.jsonl"),
        help="Output JSONL path for non-reasoning prompts.",
    )
    parser.add_argument(
        "--output-reasoning",
        type=Path,
        default=Path(
            "openAI_batch_input/prediction_experiment_data_reasoning_merged_41.jsonl"
        ),
        help="Output JSONL path for reasoning prompts.",
    )
    return parser.parse_args()


def _as_bool(value) -> bool:
    if isinstance(value, bool):
        return value
    if pd.isna(value):
        return False
    if isinstance(value, (int, float)):
        return bool(int(value))
    text = str(value).strip().lower()
    if text in {"true", "1", "yes", "y"}:
        return True
    if text in {"false", "0", "no", "n"}:
        return False
    return bool(text)


def _format_value(value) -> str:
    if pd.isna(value):
        return "NA"
    if isinstance(value, bool):
        return str(value)
    if isinstance(value, (int, float)):
        if isinstance(value, float):
            if float(value).is_integer():
                return str(int(value))
            return f"{value:.6g}"
        return str(value)
    return str(value)


def make_config(row: pd.Series, include_control_line: bool = True) -> str:
    control_line = ""
    if include_control_line:
        control_line = (
            f"***The efficiency of this game with punishment disabled was:*** "
            f"{int(round(100 * row['efficiency_np'], 0))}%\n\n"
        )

    game_structure = f"""
{control_line}[CONFIGURATION]

*** Game Structure ***
Number of players: {int(row['CONFIG_playerCount'])}
Number of rounds: {int(row['CONFIG_numRounds'])}
Is chat enabled among players?: {_as_bool(row['CONFIG_chat'])}
Is the contribution "all or nothing" i.e., binary instead of continuous?: {_as_bool(row['CONFIG_allOrNothing'])}
Is contribution the default i.e., does each player's endowment start in the public fund for them to opt-out?: {_as_bool(row['CONFIG_defaultContribProp'])}

*** Monetary Stakes ***
Marginal per capita return (MPCR): {row['CONFIG_MPCR']}

*** Peer Incentives ***
    """

    punishment = f"""
Punishment cost to impose a single unit of punishment: {int(row['CONFIG_punishmentCost'])} coin(s)
Punishment impact (number of coins deducted from the punished player per coin spent punishing): {float(row['CONFIG_punishmentTech'])}
    """

    reward = f"""
Reward cost to grant a single unit of reward: {int(row['CONFIG_rewardCost'])} coin(s)
Reward impact (the coins awarded to a player per coin spent rewarding): {float(row['CONFIG_rewardTech'])}
    """

    information_display = f"""
*** Information Display ***
Is the number of rounds known to players (do they know when the game ends)?: {_as_bool(row['CONFIG_showNRounds'])}
Are peer outcomes shown (do players know how much their peers gained at the end of each round)?: {_as_bool(row['CONFIG_showOtherSummaries'])}"""

    information_punishment = f"""
When a player is punished/rewarded, are the punishers/rewarders known?: {_as_bool(row['CONFIG_showPunishmentId'])}
    """

    no_reward = """
Reward mechanism is not enabled.
    """

    if _as_bool(row["CONFIG_rewardExists"]):
        return game_structure + punishment + reward + information_display + information_punishment
    return game_structure + punishment + no_reward + information_display + information_punishment


def make_predict_prompt(config: str, include_reasoning: bool) -> str:
    if include_reasoning:
        return f"""Now, predict the efficiency of the game below when punishment is to be enabled.
### Game Information ###
{config}

Return JSON with exactly these fields:
- "reasoning": concise rationale grounded in the experiments and game configuration
- "prediction": integer efficiency percentage only (no % sign)
"""

    return f"""Now, predict the efficiency of the game below when punishment is to be enabled.
### Game Information ###
{config}

You predict that enabling punishment will cause the efficiency percentage to change to (output should be an integer and nothing else):
"""


def append_prompt(dataframe: pd.DataFrame, include_reasoning: bool) -> list[str]:
    return [
        make_predict_prompt(
            make_config(row, include_control_line=True), include_reasoning=include_reasoning
        )
        for _, row in dataframe.iterrows()
    ]


def build_experiment_catalog_text(df: pd.DataFrame, source_name: str) -> str:
    _ = source_name
    lines: list[str] = []
    for i, (_, row) in enumerate(df.iterrows(), start=1):
        control_pct = int(round(100 * row["efficiency_np"], 0))
        treatment_pct = int(round(100 * row["efficiency_p"], 0))
        experiment_card = f"""### Exp {i} ###
Observed efficiency with punishment disabled (control): {control_pct}%
Observed efficiency with punishment enabled (treatment): {treatment_pct}%

Game information:
{make_config(row, include_control_line=False).strip()}"""
        lines.append(experiment_card)
    return "\n\n".join(lines)


def append_from_text(text: str, messages: list[str], instruction: str) -> list[str]:
    appended_messages: list[str] = []
    for message in messages:
        appended_messages.append(
            f"""{instruction}
----------Experiments Starts----------

{text}

----------Experiments Ends----------
{message}"""
        )
    return appended_messages


def build_requests(
    prompts: list[str],
    source_name: str,
    augmentation_text: str,
    model: str,
    include_reasoning: bool,
) -> list[dict]:
    requests: list[dict] = []
    augmented_prompts = append_from_text(
        text=augmentation_text,
        messages=prompts,
        instruction=PROMPT_EXPERIMENT_DATA,
    )
    for i, prompt in enumerate(augmented_prompts, start=1):
        body = {
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT_REASONING if include_reasoning else SYSTEM_PROMPT,
                },
                {"role": "user", "content": prompt},
            ],
            "temperature": 1.0 if include_reasoning else 0.0,
        }
        if include_reasoning:
            body["response_format"] = {"type": "json_object"}
        else:
            body["logprobs"] = True
            body["top_logprobs"] = 20

        requests.append(
            {
                "custom_id": f"{source_name}/Q{i}",
                "method": "POST",
                "url": "/v1/chat/completions",
                "body": body,
            }
        )
    return requests


def write_jsonl(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def _required_columns() -> set[str]:
    return {
        "efficiency_np",
        "efficiency_p",
        "CONFIG_playerCount",
        "CONFIG_numRounds",
        "CONFIG_chat",
        "CONFIG_allOrNothing",
        "CONFIG_defaultContribProp",
        "CONFIG_MPCR",
        "CONFIG_punishmentCost",
        "CONFIG_punishmentTech",
        "CONFIG_rewardCost",
        "CONFIG_rewardTech",
        "CONFIG_showNRounds",
        "CONFIG_showOtherSummaries",
        "CONFIG_showPunishmentId",
        "CONFIG_rewardExists",
    }


def _validate_columns(df: pd.DataFrame, csv_path: Path) -> None:
    missing = sorted(_required_columns() - set(df.columns))
    if missing:
        raise ValueError(
            f"Missing required columns in {csv_path}: {', '.join(missing)}"
        )


def _load_and_validate(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    _validate_columns(df, path)
    return df


def _stem(path: Path) -> str:
    return path.stem


def main() -> None:
    args = parse_args()

    target_df = _load_and_validate(args.target_df)
    validation_aug_df = _load_and_validate(args.augment_validation)
    learn_aug_df = _load_and_validate(args.augment_learn)

    base_prompts_nonreasoning = append_prompt(target_df, include_reasoning=False)
    base_prompts_reasoning = append_prompt(target_df, include_reasoning=True)

    augment_sources = [
        (_stem(args.augment_validation), validation_aug_df),
        (_stem(args.augment_learn), learn_aug_df),
    ]

    nonreasoning_requests: list[dict] = []
    reasoning_requests: list[dict] = []

    for source_name, source_df in augment_sources:
        augmentation_text = build_experiment_catalog_text(
            df=source_df, source_name=source_name
        )
        nonreasoning_requests.extend(
            build_requests(
                prompts=base_prompts_nonreasoning,
                source_name=source_name,
                augmentation_text=augmentation_text,
                model=args.model,
                include_reasoning=False,
            )
        )
        reasoning_requests.extend(
            build_requests(
                prompts=base_prompts_reasoning,
                source_name=source_name,
                augmentation_text=augmentation_text,
                model=args.model,
                include_reasoning=True,
            )
        )

    write_jsonl(args.output_nonreasoning, nonreasoning_requests)
    write_jsonl(args.output_reasoning, reasoning_requests)

    print(
        f"Wrote {len(nonreasoning_requests)} requests to {args.output_nonreasoning}"
    )
    print(f"Wrote {len(reasoning_requests)} requests to {args.output_reasoning}")


if __name__ == "__main__":
    main()
