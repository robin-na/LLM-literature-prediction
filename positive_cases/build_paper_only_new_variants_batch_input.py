from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd


DEFAULT_MODELS = [
    "gpt-4.1-2025-04-14",
    "gpt-4.1-mini-2025-04-14",
    "gpt-4.1-nano-2025-04-14",
    "gpt-5.1",
    "gpt-5-mini",
    "gpt-5-nano",
]

MODEL_TAGS = {
    "gpt-4.1": "41",
    "gpt-4.1-mini": "41mini",
    "gpt-4.1-nano": "41nano",
    "gpt-4.1-2025-04-14": "41",
    "gpt-4.1-mini-2025-04-14": "41mini",
    "gpt-4.1-nano-2025-04-14": "41nano",
    "gpt-5.1": "gpt51",
    "gpt-5-mini": "gpt5mini",
    "gpt-5-nano": "gpt5nano",
    "gpt-5.1-mini": "gpt51mini",
    "gpt-5.1-nano": "gpt51nano",
}

DEFAULT_VARIANTS = ["paper_only_narrative", "paper_only_decision"]
N_EXPLANATION_REPEATS = 5

SYSTEM_PREAMBLE = """We have conducted multiple public goods game experiments with varying experimental designs, to measure the effect of punishment in cooperative settings under various environments.
Your task is to predict how enabling a peer punishment mechanism to a specific game changes the efficiency compared to the same game with punishment disabled.
According to our experiments, whether punishment increases efficiency or not is highly dependent on many dimensions of experiment design, and it is your job to navigate this heterogeneity and make accurate predictions.

Efficiency is the ratio between the game players' behavior and that of a fully cooperative group, i.e. a group in which all members contribute their full endowment in every round.
In other words, efficiency measures how close a group's total payoff is compared to that of a group that always contributed the entire endowment and benefited maximally from the multiplier.
An efficiency value of 100 means that a group earned the same amount of coins as a hypothetical group that always cooperated.
"""

SYSTEM_PROMPT_SINGLE = (
    SYSTEM_PREAMBLE
    + "\nReturn only an integer prediction value with no percent sign and no additional text."
)

SYSTEM_PROMPT_SINGLE_EXPLANATION = (
    SYSTEM_PREAMBLE
    + """

Respond with a JSON object only:
{
  "explanation": "how you derived the prediction",
  "prediction": <integer efficiency percent>
}
The value in "prediction" must be an integer with no percent sign.
"""
)

REPORT_INSTRUCTION = """Below is a prediction-support report discussing how configuration parameters affect punishment treatment effects on efficiency.
Make predictions based faithfully on implications from the report."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build model-specific OpenAI batch JSONLs for the paper_only_narrative and "
            "paper_only_decision variants, including single/joint and w/o explanation/with explanation modes. "
            "Explanation-included requests are repeated 5 times per condition."
        )
    )
    parser.add_argument(
        "--df-pgg",
        type=Path,
        default=Path("input/pgg_CONFIGmerged_validation.csv"),
        help="Target validation configurations to predict.",
    )
    parser.add_argument(
        "--variant-registry",
        type=Path,
        default=Path("positive_cases/output/report_variant_registry.json"),
        help="Variant registry JSON.",
    )
    parser.add_argument(
        "--models",
        nargs="+",
        default=DEFAULT_MODELS,
        choices=DEFAULT_MODELS,
        help="Model names to generate batch files for.",
    )
    parser.add_argument(
        "--variants",
        nargs="+",
        default=DEFAULT_VARIANTS,
        choices=DEFAULT_VARIANTS,
        help="Variants to include.",
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


def _model_tag(model: str) -> str:
    return MODEL_TAGS[model]


def _pct(value: float) -> int:
    return int(round(100 * float(value), 0))


def make_config(row: pd.Series) -> str:
    game_structure = f"""
The efficiency of this game with punishment disabled was: {_pct(row['efficiency_np'])}

[CONFIGURATION]

Game Structure
- Number of players: {int(row['CONFIG_playerCount'])}
- Number of rounds: {int(row['CONFIG_numRounds'])}
- Chat enabled: {_as_bool(row['CONFIG_chat'])}
- Contributions are all-or-nothing: {_as_bool(row['CONFIG_allOrNothing'])}
- Contribution is the default (opt-out framing): {_as_bool(row['CONFIG_defaultContribProp'])}

Monetary Stakes
- Marginal per capita return (MPCR): {row['CONFIG_MPCR']}

Peer Incentives
- Punishment cost per unit: {int(row['CONFIG_punishmentCost'])}
- Punishment impact per unit cost: {float(row['CONFIG_punishmentTech'])}
"""

    reward = f"""
- Reward enabled: True
- Reward cost per unit: {int(row['CONFIG_rewardCost'])}
- Reward impact per unit cost: {float(row['CONFIG_rewardTech'])}
"""
    no_reward = "\n- Reward enabled: False\n"

    information_display = f"""

Information Display
- Number of rounds known to players: {_as_bool(row['CONFIG_showNRounds'])}
- Peer outcomes shown: {_as_bool(row['CONFIG_showOtherSummaries'])}
- Punishers/rewarders identified: {_as_bool(row['CONFIG_showPunishmentId'])}
"""

    return (
        game_structure
        + (reward if _as_bool(row["CONFIG_rewardExists"]) else no_reward)
        + information_display
    )


def build_single_prompt(row: pd.Series, include_explanation: bool) -> str:
    config = make_config(row)
    if include_explanation:
        return f"""Predict the efficiency of the game below when punishment is enabled.

Game information:
{config}

Return JSON with exactly these fields:
- "explanation": grounded in the report and game configuration
- "prediction": integer efficiency percentage only (no % sign)
"""

    return f"""Predict the efficiency of the game below when punishment is enabled.

Game information:
{config}

Return only the final integer efficiency percentage with no percent sign.
"""


def build_joint_system_prompt(include_explanation: bool) -> str:
    if include_explanation:
        return (
            SYSTEM_PREAMBLE
            + """

Respond with a JSON object only where each key is a Q-id.
Each value must be an object with keys:
- "explanation"
- "prediction"
"""
        )

    return (
        SYSTEM_PREAMBLE
        + """

Respond with a JSON object only where each key is a Q-id and each value is an integer efficiency prediction with no percent sign.
"""
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
- `default_contrib`: 1 if contribution is the default, 0 otherwise.
- `mpcr`: marginal per capita return.
- `pun_cost`: punishment cost per unit.
- `pun_tech`: punishment impact per unit cost.
- `rew_on`: 1 if reward is enabled, 0 otherwise.
- `rew_cost`: reward cost per unit.
- `rew_tech`: reward impact per unit cost.
- `rounds_known`: 1 if total rounds are shown, 0 otherwise.
- `peer_outcomes`: 1 if peer outcomes are shown, 0 otherwise.
- `punisher_id`: 1 if punishers/rewarders are identified, 0 otherwise."""


def build_joint_prompt(df: pd.DataFrame, include_explanation: bool) -> str:
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

    if include_explanation:
        output_schema = """Output JSON object format:
- each key must be a Q-id
- each value must be an object with keys:
  - "explanation"
  - "prediction"
- each "prediction" value must be an integer efficiency percentage with no percent sign"""
    else:
        output_schema = """Output JSON object format:
- each key must be a Q-id
- each value must be an integer efficiency percentage with no percent sign"""

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
    registry_path: Path, requested_variants: list[str]
) -> list[dict]:
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    payloads: list[dict] = []
    for variant_name in requested_variants:
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
    include_logprobs: bool,
    response_format_json: bool,
    include_explanation: bool,
    seed: int | None = None,
) -> dict:
    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    }
    if seed is not None:
        body["seed"] = int(seed)
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


def write_jsonl(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def build_requests(
    df: pd.DataFrame,
    variant_payloads: list[dict],
    repo_root: Path,
    model: str,
) -> list[dict]:
    requests: list[dict] = []

    for payload in variant_payloads:
        report_text = (repo_root / payload["report_path"]).read_text(encoding="utf-8")
        variant_name = payload["variant_name"]

        for i, (_, row) in enumerate(df.iterrows(), start=1):
            requests.append(
                build_openai_request(
                    custom_id=f"{variant_name}/Q{i}",
                    model=model,
                    system_prompt=SYSTEM_PROMPT_SINGLE,
                    user_prompt=wrap_with_report(
                        report_text,
                        build_single_prompt(row, include_explanation=False),
                    ),
                    include_logprobs=True,
                    response_format_json=False,
                    include_explanation=False,
                )
            )

            for rep_idx in range(1, N_EXPLANATION_REPEATS + 1):
                requests.append(
                    build_openai_request(
                        custom_id=f"{variant_name}_explanation_rep{rep_idx}/Q{i}",
                        model=model,
                        system_prompt=SYSTEM_PROMPT_SINGLE_EXPLANATION,
                        user_prompt=wrap_with_report(
                            report_text,
                            build_single_prompt(row, include_explanation=True),
                        ),
                        include_logprobs=False,
                        response_format_json=True,
                        include_explanation=True,
                    )
                )

        requests.append(
            build_openai_request(
                custom_id=f"{variant_name}_joint",
                model=model,
                system_prompt=build_joint_system_prompt(include_explanation=False),
                user_prompt=wrap_with_report(
                    report_text,
                    build_joint_prompt(df, include_explanation=False),
                ),
                include_logprobs=False,
                response_format_json=True,
                include_explanation=False,
            )
        )

        for rep_idx in range(1, N_EXPLANATION_REPEATS + 1):
            requests.append(
                build_openai_request(
                    custom_id=f"{variant_name}_joint_explanation_rep{rep_idx}",
                    model=model,
                    system_prompt=build_joint_system_prompt(include_explanation=True),
                    user_prompt=wrap_with_report(
                        report_text,
                        build_joint_prompt(df, include_explanation=True),
                    ),
                    include_logprobs=False,
                    response_format_json=True,
                    include_explanation=True,
                )
            )

    return requests


def main() -> None:
    args = parse_args()
    repo_root = Path.cwd()
    df = pd.read_csv(args.df_pgg).sort_values("CONFIG_configId").reset_index(drop=True)
    variant_payloads = load_variant_payloads(args.variant_registry, args.variants)

    for model in args.models:
        requests = build_requests(
            df=df,
            variant_payloads=variant_payloads,
            repo_root=repo_root,
            model=model,
        )
        output_path = (
            args.output_dir
            / f"prediction_positive_case_paper_only_narrative-decision_{_model_tag(model)}.jsonl"
        )
        write_jsonl(output_path, requests)
        print(f"Wrote {len(requests)} requests to {output_path}")


if __name__ == "__main__":
    main()
