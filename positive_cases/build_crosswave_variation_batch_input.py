from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

from agentic_report.pipeline import REPORT_METHOD_SPECS, canonical_output_dir_name


SYSTEM_PREAMBLE = """We have conducted multiple public goods game experiments with varying experimental designs, to measure the effect of punishment in cooperative settings under various environments.
Your task is to predict how enabling a punishment mechanism to a specific game changes the ***efficiency*** compared to the same game with punishment disabled.
According to our experiments, whether punishment increases efficiency or not is highly dependent on a lot of dimensions in experiment design, and it is your job to navigate this heterogeneity and make accurate predictions.

***Efficiency*** is the ratio between the game players' behavior and that of a fully-cooperative group (i.e. a group in which all members contribute their full endowment in every round)
In other words, efficiency measures how close a group's total payoff is, compared to that of a group that always cooperated (i.e. always contributes the entire endowment, and benefits maximally from the multiplier).
An efficiency value of 100% means that a group earned the same amount of coins as a hypothetical group that always cooperated.

For example, let's say a game has 5 players playing 10 rounds where 20 coins are given to each player per round and the multiplier for each contributed coin is 3.
In this case, the earning of a hypothetical "always cooperating" group is 5*10*20*3=3000 coins, while the earning of a hypothetical "never cooperating" group is 1000 coins.
Hence, the efficiency is 100% for the always cooperating group and 33% for the never cooperating group.
"""

SYSTEM_PROMPT_SINGLE = (
    SYSTEM_PREAMBLE
    + '\nYour output should strictly be a prediction value with integer only (e.g., 33% should output 33 and nothing else).'
)

SYSTEM_PROMPT_SINGLE_REASONING = (
    SYSTEM_PREAMBLE
    + """

Respond with a JSON object only:
{
  "reasoning": "brief explanation of how you derived the prediction",
  "prediction": <integer efficiency percent>
}
The value in "prediction" must be an integer with no percent sign."""
)

REPORT_INSTRUCTION = """Below is a prediction-support report discussing how configuration parameters affect punishment treatment effects on efficiency.
Make predictions based faithfully on implications from the report."""

EXPERIMENT_INSTRUCTION = """Below is a catalog of prior public-goods-game experiments.
Each experiment includes the observed efficiency with punishment disabled and with punishment enabled.
Use these positive-case examples to inform your prediction."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build one merged OpenAI batch JSONL across validation and learning "
            "targets, report/input variations, and elicitation variations."
        )
    )
    parser.add_argument(
        "--validation-df",
        type=Path,
        default=Path("input/pgg_CONFIGmerged_validation.csv"),
        help="Validation-wave target CSV used for Q1..Q20 predictions.",
    )
    parser.add_argument(
        "--learning-df",
        type=Path,
        default=Path("input/df_paired_learn.csv"),
        help="Learning-wave target CSV used for L1..L150 predictions.",
    )
    parser.add_argument(
        "--augment-validation",
        type=Path,
        default=Path("input/pgg_CONFIGmerged_validation.csv"),
        help="Experiment catalog CSV for the validation-wave augmentation source.",
    )
    parser.add_argument(
        "--augment-learn",
        type=Path,
        default=Path("input/pgg_CONFIGmerged_learn.csv"),
        help="Experiment catalog CSV for the learn-wave augmentation source.",
    )
    parser.add_argument(
        "--reports-root",
        type=Path,
        default=Path("positive_cases/output"),
        help="Root directory containing generated report variations.",
    )
    parser.add_argument(
        "--methods",
        nargs="+",
        default=sorted(REPORT_METHOD_SPECS),
        choices=sorted(REPORT_METHOD_SPECS),
        help="Report methods to include.",
    )
    parser.add_argument(
        "--skip-baseline",
        action="store_true",
        help="Exclude baseline no-augmentation conditions.",
    )
    parser.add_argument(
        "--skip-experiment-inputs",
        action="store_true",
        help="Exclude experiment-catalog augmentation conditions.",
    )
    parser.add_argument(
        "--model",
        default="gpt-4.1",
        help="OpenAI chat completions model name.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output JSONL path. If omitted, a model-based default is used.",
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


def _as_binary(value) -> int:
    return 1 if _as_bool(value) else 0


def _pct(value: float) -> int:
    return int(round(100 * float(value), 0))


def _model_tag(model: str) -> str:
    known = {
        "gpt-4.1": "41",
        "gpt-4.1-mini": "41mini",
        "gpt-4.1-nano": "41nano",
        "gpt-4.1-2025-04-14": "41",
        "gpt-4.1-mini-2025-04-14": "41mini",
        "gpt-4.1-nano-2025-04-14": "41nano",
    }
    if model in known:
        return known[model]
    return "".join(ch for ch in model.lower() if ch.isalnum())


def default_output_path(model: str) -> Path:
    return Path(
        f"openAI_batch_input/prediction_crosswave_variations_{_model_tag(model)}.jsonl"
    )


def report_path_for_method(reports_root: Path, method: str) -> Path:
    spec = REPORT_METHOD_SPECS[method]
    folder = canonical_output_dir_name(spec["source_mode"], spec["report_style"])
    return reports_root / folder / "agentic_report.md"


def make_config(row: pd.Series, control_col: str, include_control_line: bool = True) -> str:
    control_line = ""
    if include_control_line:
        control_line = (
            f"***The efficiency of this game with punishment disabled was:*** "
            f"{_pct(row[control_col])}%\n\n"
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


def build_single_prompt(row: pd.Series, control_col: str, include_reasoning: bool) -> str:
    config = make_config(row, control_col=control_col, include_control_line=True)
    if include_reasoning:
        return f"""Now, predict the efficiency of the game below when punishment is to be enabled.
### Game Information ###
{config}

Return JSON with exactly these fields:
- "reasoning": concise rationale grounded in the provided evidence and the game configuration
- "prediction": integer efficiency percentage only (no % sign)
"""

    return f"""Now, predict the efficiency of the game below when punishment is to be enabled.
### Game Information ###
{config}

You predict that enabling punishment will cause the efficiency percentage to change to (output should be an integer and nothing else):
"""


def build_joint_system_prompt(label_prefix: str, include_reasoning: bool) -> str:
    if include_reasoning:
        return (
            SYSTEM_PREAMBLE
            + f"""

Respond with a JSON object only where each key is a {label_prefix}-id.
Each value must be an object with keys:
- "reasoning": brief explanation
- "prediction": integer efficiency prediction with no percent sign

Example:
{{
  "{label_prefix}1": {{"reasoning": "short explanation", "prediction": 71}},
  "{label_prefix}2": {{"reasoning": "short explanation", "prediction": 64}}
}}"""
        )

    return (
        SYSTEM_PREAMBLE
        + f"""

Respond with a JSON object only where each key is a {label_prefix}-id and each value is an integer efficiency prediction with no percent sign.
Example:
{{
  "{label_prefix}1": 71,
  "{label_prefix}2": 64
}}"""
    )


def build_joint_column_guide(label_prefix: str, dataset_phrase: str) -> str:
    return f"""Each row below is one {dataset_phrase} prediction question.
Column meanings:
- `{label_prefix}`: question id to use in the output JSON.
- `ctrl_eff_pct`: observed efficiency with punishment disabled, in percent.
- `players`: number of players.
- `rounds`: number of rounds.
- `chat`: 1 if chat is enabled, 0 otherwise.
- `aon`: 1 if contribution is all-or-nothing, 0 otherwise.
- `default_contrib`: 1 if contribution is the default (opt-out from contributing), 0 otherwise.
- `mpcr`: marginal per capita return.
- `pun_cost`: punishment cost per unit.
- `pun_tech`: punishment impact per unit cost.
- `rew_on`: 1 if reward is enabled, 0 otherwise.
- `rew_cost`: reward cost per unit.
- `rew_tech`: reward impact per unit cost.
- `rounds_known`: 1 if number of rounds is known to players, 0 otherwise.
- `peer_outcomes`: 1 if peer outcomes are shown, 0 otherwise.
- `punisher_id`: 1 if punishers/rewarders are known, 0 otherwise."""


def build_joint_prompt(
    df: pd.DataFrame,
    control_col: str,
    label_prefix: str,
    dataset_phrase: str,
    include_reasoning: bool,
) -> str:
    table_lines = [
        f"| {label_prefix} | ctrl_eff_pct | players | rounds | chat | aon | default_contrib | mpcr | pun_cost | pun_tech | rew_on | rew_cost | rew_tech | rounds_known | peer_outcomes | punisher_id |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for idx, (_, row) in enumerate(df.iterrows(), start=1):
        table_lines.append(
            "| "
            + " | ".join(
                [
                    f"{label_prefix}{idx}",
                    str(_pct(row[control_col])),
                    str(int(row["CONFIG_playerCount"])),
                    str(int(row["CONFIG_numRounds"])),
                    str(_as_binary(row["CONFIG_chat"])),
                    str(_as_binary(row["CONFIG_allOrNothing"])),
                    str(_as_binary(row["CONFIG_defaultContribProp"])),
                    f"{row['CONFIG_MPCR']}",
                    str(int(row["CONFIG_punishmentCost"])),
                    f"{float(row['CONFIG_punishmentTech'])}",
                    str(_as_binary(row["CONFIG_rewardExists"])),
                    str(int(row["CONFIG_rewardCost"])),
                    f"{float(row['CONFIG_rewardTech'])}",
                    str(_as_binary(row["CONFIG_showNRounds"])),
                    str(_as_binary(row["CONFIG_showOtherSummaries"])),
                    str(_as_binary(row["CONFIG_showPunishmentId"])),
                ]
            )
            + " |"
        )

    output_schema = f"""Output JSON object format:
{{
  "{label_prefix}1": 71,
  "{label_prefix}2": 64
}}"""
    if include_reasoning:
        output_schema = f"""Output JSON object format:
{{
  "{label_prefix}1": {{"reasoning": "short explanation", "prediction": 71}},
  "{label_prefix}2": {{"reasoning": "short explanation", "prediction": 64}}
}}"""

    return "\n\n".join(
        [
            f"Predict the efficiency with punishment enabled for all {len(df)} games below.",
            build_joint_column_guide(label_prefix=label_prefix, dataset_phrase=dataset_phrase),
            "\n".join(table_lines),
            output_schema,
        ]
    )


def wrap_with_report(report_text: str, prompt_text: str) -> str:
    return f"""{REPORT_INSTRUCTION}
----------Report Starts----------

{report_text}

----------Report Ends----------
{prompt_text}"""


def build_experiment_catalog_text(df: pd.DataFrame) -> str:
    lines: list[str] = []
    for i, (_, row) in enumerate(df.iterrows(), start=1):
        experiment_card = f"""### Exp {i} ###
Observed efficiency with punishment disabled (control): {_pct(row['efficiency_np'])}%
Observed efficiency with punishment enabled (treatment): {_pct(row['efficiency_p'])}%

Game information:
{make_config(row, control_col='efficiency_np', include_control_line=False).strip()}"""
        lines.append(experiment_card)
    return "\n\n".join(lines)


def wrap_with_experiments(experiment_text: str, prompt_text: str) -> str:
    return f"""{EXPERIMENT_INSTRUCTION}

{experiment_text}

{prompt_text}"""


def build_openai_request(
    custom_id: str,
    model: str,
    system_prompt: str,
    user_prompt: str,
    include_logprobs: bool,
    response_format_json: bool,
    temperature: float,
) -> dict:
    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": temperature,
    }
    if include_logprobs:
        body["logprobs"] = True
        body["top_logprobs"] = 20
    if response_format_json:
        body["response_format"] = {"type": "json_object"}

    return {
        "custom_id": custom_id,
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": body,
    }


def append_condition_requests(
    requests: list[dict],
    *,
    condition_name: str,
    dataset_name: str,
    df: pd.DataFrame,
    label_prefix: str,
    control_col: str,
    dataset_phrase: str,
    model: str,
    report_text: str | None = None,
    experiment_text: str | None = None,
) -> None:
    for idx, (_, row) in enumerate(df.iterrows(), start=1):
        label = f"{label_prefix}{idx}"

        single_prompt = build_single_prompt(
            row=row, control_col=control_col, include_reasoning=False
        )
        single_reasoning_prompt = build_single_prompt(
            row=row, control_col=control_col, include_reasoning=True
        )

        if report_text is not None:
            single_prompt = wrap_with_report(report_text, single_prompt)
            single_reasoning_prompt = wrap_with_report(report_text, single_reasoning_prompt)
        if experiment_text is not None:
            single_prompt = wrap_with_experiments(experiment_text, single_prompt)
            single_reasoning_prompt = wrap_with_experiments(
                experiment_text, single_reasoning_prompt
            )

        requests.append(
            build_openai_request(
                custom_id=f"{condition_name}/{label}",
                model=model,
                system_prompt=SYSTEM_PROMPT_SINGLE,
                user_prompt=single_prompt,
                include_logprobs=True,
                response_format_json=False,
                temperature=0.0,
            )
        )
        requests.append(
            build_openai_request(
                custom_id=f"{condition_name}_reasoning/{label}",
                model=model,
                system_prompt=SYSTEM_PROMPT_SINGLE_REASONING,
                user_prompt=single_reasoning_prompt,
                include_logprobs=False,
                response_format_json=True,
                temperature=1.0,
            )
        )

    joint_prompt = build_joint_prompt(
        df=df,
        control_col=control_col,
        label_prefix=label_prefix,
        dataset_phrase=dataset_phrase,
        include_reasoning=False,
    )
    joint_reasoning_prompt = build_joint_prompt(
        df=df,
        control_col=control_col,
        label_prefix=label_prefix,
        dataset_phrase=dataset_phrase,
        include_reasoning=True,
    )

    if report_text is not None:
        joint_prompt = wrap_with_report(report_text, joint_prompt)
        joint_reasoning_prompt = wrap_with_report(report_text, joint_reasoning_prompt)
    if experiment_text is not None:
        joint_prompt = wrap_with_experiments(experiment_text, joint_prompt)
        joint_reasoning_prompt = wrap_with_experiments(experiment_text, joint_reasoning_prompt)

    requests.append(
        build_openai_request(
            custom_id=f"{dataset_name}/{condition_name}_joint",
            model=model,
            system_prompt=build_joint_system_prompt(
                label_prefix=label_prefix, include_reasoning=False
            ),
            user_prompt=joint_prompt,
            include_logprobs=False,
            response_format_json=True,
            temperature=0.0,
        )
    )
    requests.append(
        build_openai_request(
            custom_id=f"{dataset_name}/{condition_name}_joint_reasoning",
            model=model,
            system_prompt=build_joint_system_prompt(
                label_prefix=label_prefix, include_reasoning=True
            ),
            user_prompt=joint_reasoning_prompt,
            include_logprobs=False,
            response_format_json=True,
            temperature=1.0,
        )
    )


def write_jsonl(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def main() -> None:
    args = parse_args()

    validation_df = pd.read_csv(args.validation_df)
    learning_df = (
        pd.read_csv(args.learning_df).sort_values("CONFIG_configId").reset_index(drop=True)
    )
    validation_aug_df = pd.read_csv(args.augment_validation)
    learn_aug_df = pd.read_csv(args.augment_learn)

    report_texts: dict[str, str] = {}
    for method in args.methods:
        report_path = report_path_for_method(args.reports_root, method)
        if not report_path.exists():
            raise FileNotFoundError(f"Missing report for method '{method}': {report_path}")
        report_texts[method] = report_path.read_text(encoding="utf-8")

    experiment_inputs = {
        args.augment_validation.stem: build_experiment_catalog_text(validation_aug_df),
        args.augment_learn.stem: build_experiment_catalog_text(learn_aug_df),
    }

    requests: list[dict] = []

    datasets = [
        {
            "dataset_name": "validation",
            "df": validation_df,
            "label_prefix": "Q",
            "control_col": "efficiency_np",
            "dataset_phrase": "validation-wave",
        },
        {
            "dataset_name": "learning",
            "df": learning_df,
            "label_prefix": "L",
            "control_col": "control_itt_efficiency",
            "dataset_phrase": "learning-wave",
        },
    ]

    for dataset in datasets:
        if not args.skip_baseline:
            append_condition_requests(
                requests,
                condition_name="baseline",
                dataset_name=dataset["dataset_name"],
                df=dataset["df"],
                label_prefix=dataset["label_prefix"],
                control_col=dataset["control_col"],
                dataset_phrase=dataset["dataset_phrase"],
                model=args.model,
            )

        for method in args.methods:
            append_condition_requests(
                requests,
                condition_name=method,
                dataset_name=dataset["dataset_name"],
                df=dataset["df"],
                label_prefix=dataset["label_prefix"],
                control_col=dataset["control_col"],
                dataset_phrase=dataset["dataset_phrase"],
                model=args.model,
                report_text=report_texts[method],
            )

        if not args.skip_experiment_inputs:
            for source_name, experiment_text in experiment_inputs.items():
                append_condition_requests(
                    requests,
                    condition_name=source_name,
                    dataset_name=dataset["dataset_name"],
                    df=dataset["df"],
                    label_prefix=dataset["label_prefix"],
                    control_col=dataset["control_col"],
                    dataset_phrase=dataset["dataset_phrase"],
                    model=args.model,
                    experiment_text=experiment_text,
                )

    output_path = args.output or default_output_path(args.model)
    write_jsonl(output_path, requests)
    print(f"Wrote {len(requests)} requests to {output_path}")


if __name__ == "__main__":
    main()
