from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd


DEFAULT_MODELS = [
    "o3",
    "o4-mini",
    "gpt-3.5-turbo",
    "gpt-4o-mini",
    "gpt-4o",
    "gpt-5.1",
]

MODEL_TAGS = {
    "o3": "o3",
    "o4-mini": "o4mini",
    "gpt-3.5-turbo": "35turbo",
    "gpt-4o-mini": "4omini",
    "gpt-4o": "4o",
    "gpt-5.1": "gpt51",
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build model-specific OpenAI batch JSONLs for validation positive-case "
            "report variants, single-question only, with direct and reasoning "
            "requests combined into one file per model."
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
        help=(
            "Optional explicit list of report variant names. If omitted, all built-in "
            "registered variants are included."
        ),
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("openAI_batch_input"),
        help="Directory for output JSONL files.",
    )
    parser.add_argument(
        "--direct-only",
        action="store_true",
        help="Write only the non-reasoning integer-output requests.",
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


def _is_o_series(model: str) -> bool:
    return model.startswith("o")


def _system_role(model: str) -> str:
    # Official chat-completions docs note that with o1 models and newer,
    # developer messages replace the previous system messages.
    return "developer" if _is_o_series(model) else "system"


def _model_tag(model: str) -> str:
    return MODEL_TAGS.get(model, "".join(ch for ch in model.lower() if ch.isalnum()))


def _top_logprobs_limit(model: str) -> int:
    return 5 if model == "gpt-5.1" else 20


def make_config(row: pd.Series) -> str:
    game_structure = f"""
***The efficiency of this game with punishment disabled was:*** {int(round(100 * row['efficiency_np'], 0))}%

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


def build_single_question_prompt(row: pd.Series, include_reasoning: bool) -> str:
    config = make_config(row)
    if include_reasoning:
        return f"""Now, predict the efficiency of the game below when punishment is to be enabled.
### Game Information ###
{config}

Return JSON with exactly these fields:
- "reasoning": concise rationale grounded in the report and game configuration
- "prediction": integer efficiency percentage only (no % sign)
"""

    return f"""Now, predict the efficiency of the game below when punishment is to be enabled.
### Game Information ###
{config}

You predict that enabling punishment will cause the efficiency percentage to change to (output should be an integer and nothing else):
"""


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
    include_logprobs: bool,
    response_format_json: bool,
    include_reasoning: bool,
) -> dict:
    body = {
        "model": model,
        "messages": [
            {"role": _system_role(model), "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    }

    # Chat Completions docs explicitly note parameter support differs for newer
    # reasoning models and that `max_tokens` is incompatible with o-series models.
    # We omit temperature for o-series conservatively; no official doc we found
    # explicitly requires it for these models.
    if not _is_o_series(model):
        body["temperature"] = 1.0 if include_reasoning else 0.0

    if include_logprobs:
        body["logprobs"] = True
        body["top_logprobs"] = _top_logprobs_limit(model)
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
    include_reasoning: bool,
) -> list[dict]:
    requests: list[dict] = []
    system_prompt = (
        SYSTEM_PROMPT_SINGLE_REASONING if include_reasoning else SYSTEM_PROMPT_SINGLE
    )

    for i, (_, row) in enumerate(df.iterrows(), start=1):
        requests.append(
            build_openai_request(
                custom_id=f"{'baseline_reasoning' if include_reasoning else 'baseline'}/Q{i}",
                model=model,
                system_prompt=system_prompt,
                user_prompt=build_single_question_prompt(
                    row, include_reasoning=include_reasoning
                ),
                include_logprobs=not include_reasoning,
                response_format_json=include_reasoning,
                include_reasoning=include_reasoning,
            )
        )

    for payload in variant_payloads:
        report_text = (repo_root / payload["report_path"]).read_text(encoding="utf-8")
        variant_name = payload["variant_name"]
        variant_id = f"{variant_name}_reasoning" if include_reasoning else variant_name

        for i, (_, row) in enumerate(df.iterrows(), start=1):
            requests.append(
                build_openai_request(
                    custom_id=f"{variant_id}/Q{i}",
                    model=model,
                    system_prompt=system_prompt,
                    user_prompt=wrap_with_report(
                        report_text,
                        build_single_question_prompt(
                            row, include_reasoning=include_reasoning
                        ),
                    ),
                    include_logprobs=not include_reasoning,
                    response_format_json=include_reasoning,
                    include_reasoning=include_reasoning,
                )
            )

    return requests


def main() -> None:
    args = parse_args()
    repo_root = Path.cwd()
    df = pd.read_csv(args.df_pgg)
    variant_payloads = load_variant_payloads(args.variant_registry, args.variants)

    for model in args.models:
        model_tag = _model_tag(model)
        merged_requests = build_requests(
            df=df,
            variant_payloads=variant_payloads,
            repo_root=repo_root,
            model=model,
            include_reasoning=False,
        )
        if not args.direct_only:
            merged_requests += build_requests(
                df=df,
                variant_payloads=variant_payloads,
                repo_root=repo_root,
                model=model,
                include_reasoning=True,
            )

        output_path = (
            args.output_dir / f"prediction_positive_case_variants_single_{model_tag}.jsonl"
        )

        write_jsonl(output_path, merged_requests)
        print(f"Wrote {len(merged_requests)} requests to {output_path}")


if __name__ == "__main__":
    main()
