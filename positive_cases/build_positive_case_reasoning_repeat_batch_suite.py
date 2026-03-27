from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd


DEFAULT_MODELS = [
    "gpt-3.5-turbo",
    "gpt-4.1-nano",
    "gpt-4.1-mini",
    "gpt-4o-mini",
    "gpt-4o",
    "o3",
    "o4-mini",
    "gpt-4.1",
    "gpt-5.1",
    "gpt-5-mini",
    "gpt-5-nano",
]

MODEL_TAGS = {
    "gpt-3.5-turbo": "35turbo",
    "gpt-4.1-nano": "41nano",
    "gpt-4.1-mini": "41mini",
    "gpt-4o-mini": "4omini",
    "gpt-4o": "4o",
    "o3": "o3",
    "o4-mini": "o4mini",
    "gpt-4.1": "41",
    "gpt-5.1": "gpt51",
    "gpt-5-mini": "gpt5mini",
    "gpt-5-nano": "gpt5nano",
    "gpt-5.1-mini": "gpt51mini",
    "gpt-5.1-nano": "gpt51nano",
}

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

SYSTEM_PROMPT_SINGLE_REASONING = (
    SYSTEM_PREAMBLE
    + """

Respond with a JSON object only:
{
  "reasoning": "explanation",
  "prediction": <integer efficiency percent>
}
The value in "prediction" must be an integer with no percent sign."""
)

REPORT_INSTRUCTION = """Below is a prediction-support report discussing how configuration parameters affect punishment treatment effects on efficiency.
Make predictions based faithfully on implications from the report."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build model-specific OpenAI batch JSONLs for repeated reasoning runs "
            "over positive-case report variants, covering both single-question "
            "reasoning and joint reasoning."
        )
    )
    parser.add_argument(
        "--df-pgg",
        type=Path,
        default=Path("input/pgg_CONFIGmerged_validation.csv"),
        help="Validation configurations to predict.",
    )
    parser.add_argument(
        "--variant-registry",
        type=Path,
        default=Path("positive_cases/output/report_variant_registry.json"),
        help="Variant registry JSON produced by the positive-case notebook helper.",
    )
    parser.add_argument(
        "--models",
        nargs="+",
        default=DEFAULT_MODELS,
        help="Model names to generate batch files for.",
    )
    parser.add_argument(
        "--variants",
        nargs="+",
        default=None,
        help="Optional explicit list of report variant names.",
    )
    parser.add_argument(
        "--n-repeats",
        type=int,
        default=4,
        help="Number of stochastic repeated calls per condition.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("openAI_batch_input"),
        help="Directory for output JSONL files.",
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


def _is_o_series(model: str) -> bool:
    return model.startswith("o")


def _system_role(model: str) -> str:
    return "developer" if _is_o_series(model) else "system"


def _model_tag(model: str) -> str:
    return MODEL_TAGS.get(model, "".join(ch for ch in model.lower() if ch.isalnum()))


def _pct(value: float) -> int:
    return int(round(100 * float(value), 0))


def make_config(row: pd.Series) -> str:
    game_structure = f"""
***The efficiency of this game with punishment disabled was:*** {_pct(row['efficiency_np'])}%

[CONFIGURATION]

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


def build_single_reasoning_prompt(row: pd.Series) -> str:
    config = make_config(row)
    return f"""Now, predict the efficiency of the game below when punishment is to be enabled.
### Game Information ###
{config}

Return JSON with exactly these fields:
- "reasoning": explanation grounded in the report and game configuration
- "prediction": integer efficiency percentage only (no % sign)
"""


def build_joint_system_prompt() -> str:
    return (
        SYSTEM_PREAMBLE
        + """

Respond with a JSON object only where each key is a Q-id.
Each value must be an object with keys:
- "reasoning": explanation
- "prediction": integer efficiency prediction with no percent sign

Example:
{
  "Q1": {"reasoning": "explanation", "prediction": 71},
  "Q2": {"reasoning": "explanation", "prediction": 64}
}"""
    )


def build_joint_column_guide() -> str:
    return """Each row below is one validation prediction question.
Column meanings:
- `Q`: question id to use in the output JSON.
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


def build_joint_reasoning_prompt(df: pd.DataFrame) -> str:
    table_lines = [
        "| Q | ctrl_eff_pct | players | rounds | chat | aon | default_contrib | mpcr | pun_cost | pun_tech | rew_on | rew_cost | rew_tech | rounds_known | peer_outcomes | punisher_id |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for idx, (_, row) in enumerate(df.iterrows(), start=1):
        table_lines.append(
            "| "
            + " | ".join(
                [
                    f"Q{idx}",
                    str(_pct(row["efficiency_np"])),
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

    output_schema = """Output JSON object format:
{
  "Q1": {"reasoning": "explanation", "prediction": 71},
  "Q2": {"reasoning": "explanation", "prediction": 64}
}"""

    return "\n\n".join(
        [
            f"Predict the efficiency with punishment enabled for all {len(df)} games below.",
            build_joint_column_guide(),
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


def load_variant_payloads(
    registry_path: Path, requested_variants: list[str] | None
) -> list[dict]:
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    payloads: list[dict] = []

    if requested_variants is None:
        variant_names = [
            key
            for key, value in registry.items()
            if value.get("variant_type") == "built_in" and value.get("exists")
        ]
    else:
        variant_names = requested_variants

    for variant_name in sorted(variant_names):
        if variant_name not in registry:
            raise KeyError(f"Unknown variant in registry: {variant_name}")
        entry = registry[variant_name]
        if not entry.get("exists"):
            raise FileNotFoundError(
                f"Variant report is marked missing for '{variant_name}': {entry.get('report_path')}"
            )
        payloads.append(
            {
                "variant_name": variant_name,
                "report_path": Path(entry["report_path"]),
            }
        )
    return payloads


def build_openai_request(
    *,
    custom_id: str,
    model: str,
    system_prompt: str,
    user_prompt: str,
    temperature: float | None,
) -> dict:
    body = {
        "model": model,
        "messages": [
            {"role": _system_role(model), "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "response_format": {"type": "json_object"},
    }
    if temperature is not None:
        body["temperature"] = temperature

    return {
        "custom_id": custom_id,
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": body,
    }


def _repeat_suffix(rep_idx: int | None, temperature: float | None) -> str:
    if rep_idx is not None:
        return f"rep{rep_idx}"
    if temperature == 0.0:
        return "temp0"
    raise ValueError("Either rep_idx or temperature==0.0 expected.")


def write_jsonl(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def build_requests(
    *,
    df: pd.DataFrame,
    variant_payloads: list[dict],
    repo_root: Path,
    model: str,
    n_repeats: int,
) -> list[dict]:
    requests: list[dict] = []
    non_o_anchor = not _is_o_series(model)
    run_specs: list[tuple[int | None, float | None]] = [(i, None if _is_o_series(model) else 1.0) for i in range(1, n_repeats + 1)]
    if non_o_anchor:
        run_specs.append((None, 0.0))

    def single_condition_name(variant_name: str, suffix: str) -> str:
        return f"{variant_name}_reasoning_{suffix}"

    def joint_condition_name(variant_name: str, suffix: str) -> str:
        return f"{variant_name}_joint_reasoning_{suffix}"

    for rep_idx, temperature in run_specs:
        suffix = _repeat_suffix(rep_idx, temperature)
        for i, (_, row) in enumerate(df.iterrows(), start=1):
            requests.append(
                build_openai_request(
                    custom_id=f"{single_condition_name('baseline', suffix)}/Q{i}",
                    model=model,
                    system_prompt=SYSTEM_PROMPT_SINGLE_REASONING,
                    user_prompt=build_single_reasoning_prompt(row),
                    temperature=temperature,
                )
            )
        requests.append(
            build_openai_request(
                custom_id=joint_condition_name("baseline", suffix),
                model=model,
                system_prompt=build_joint_system_prompt(),
                user_prompt=build_joint_reasoning_prompt(df),
                temperature=temperature,
            )
        )

    for payload in variant_payloads:
        report_text = (repo_root / payload["report_path"]).read_text(encoding="utf-8")
        variant_name = payload["variant_name"]
        for rep_idx, temperature in run_specs:
            suffix = _repeat_suffix(rep_idx, temperature)
            for i, (_, row) in enumerate(df.iterrows(), start=1):
                requests.append(
                    build_openai_request(
                        custom_id=f"{single_condition_name(variant_name, suffix)}/Q{i}",
                        model=model,
                        system_prompt=SYSTEM_PROMPT_SINGLE_REASONING,
                        user_prompt=wrap_with_report(report_text, build_single_reasoning_prompt(row)),
                        temperature=temperature,
                    )
                )
            requests.append(
                build_openai_request(
                    custom_id=joint_condition_name(variant_name, suffix),
                    model=model,
                    system_prompt=build_joint_system_prompt(),
                    user_prompt=wrap_with_report(report_text, build_joint_reasoning_prompt(df)),
                    temperature=temperature,
                )
            )

    return requests


def main() -> None:
    args = parse_args()
    repo_root = Path.cwd()
    df = pd.read_csv(args.df_pgg).sort_values("CONFIG_configId")
    variant_payloads = load_variant_payloads(args.variant_registry, args.variants)

    for model in args.models:
        requests = build_requests(
            df=df,
            variant_payloads=variant_payloads,
            repo_root=repo_root,
            model=model,
            n_repeats=args.n_repeats,
        )
        output_path = args.output_dir / f"prediction_positive_case_reasoning_repeats_{_model_tag(model)}.jsonl"
        write_jsonl(output_path, requests)
        print(f"Wrote {len(requests)} requests to {output_path}")


if __name__ == "__main__":
    main()
