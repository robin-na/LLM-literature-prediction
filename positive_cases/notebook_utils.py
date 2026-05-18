from __future__ import annotations

import json
import re
import shutil
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Callable

import numpy as np
import pandas as pd

from prediction.prediction_metrics import compute_metrics
from positive_cases.agentic_report.column_defs import format_column_definitions
from positive_cases.agentic_report.pipeline import (
    REPORT_METHOD_SPECS,
    canonical_output_dir_name,
)
from positive_cases.agentic_report.prompts import (
    build_final_report_prompt,
    build_report_ensemble_prompt,
    build_report_refinement_prompt,
)


DEFAULT_VALIDATION_CSV = Path("input/pgg_CONFIGmerged_validation.csv")
DEFAULT_REPORTS_ROOT = Path("positive_cases/output")
DEFAULT_RESULTS_DIR = Path("results/notebook_positive_case_prompt_lab")
VARIANT_REGISTRY_PATH = Path("positive_cases/output/report_variant_registry.json")

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
  "reasoning": "brief explanation of how you derived the prediction",
  "prediction": <integer efficiency percent>
}
The value in "prediction" must be an integer with no percent sign."""
)

REPORT_INSTRUCTION = """Below is a prediction-support report discussing how configuration parameters affect punishment treatment effects on efficiency.
Make predictions based faithfully on implications from the report."""

DEFAULT_SYSTEM_PROMPT = SYSTEM_PROMPT_SINGLE_REASONING
DEFAULT_REPORT_INSTRUCTION = REPORT_INSTRUCTION


def find_repo_root(start: Path | None = None) -> Path:
    start_path = (start or Path.cwd()).resolve()
    for candidate in [start_path, *start_path.parents]:
        if (candidate / "positive_cases").exists() and (candidate / "input").exists():
            return candidate
    raise FileNotFoundError(
        "Could not locate repo root. Expected folders 'positive_cases' and 'input'."
    )


def resolve_repo_path(repo_root: Path, path_like: Path | str) -> Path:
    path = Path(path_like)
    return path if path.is_absolute() else repo_root / path


def load_validation_df(
    repo_root: Path | None = None, csv_path: Path | str = DEFAULT_VALIDATION_CSV
) -> pd.DataFrame:
    root = find_repo_root(repo_root)
    path = resolve_repo_path(root, csv_path)
    df = pd.read_csv(path)
    return df.sort_values("CONFIG_configId").reset_index(drop=True)


def question_labels(n_questions: int) -> list[str]:
    return [f"Q{i}" for i in range(1, n_questions + 1)]


def make_validation_ground_truth(
    validation_df: pd.DataFrame,
) -> tuple[pd.Series, pd.Series]:
    labels = question_labels(len(validation_df))
    treatment = pd.Series(
        validation_df["efficiency_p"].to_numpy(dtype=float) * 100.0, index=labels
    )
    control = pd.Series(
        validation_df["efficiency_np"].to_numpy(dtype=float) * 100.0, index=labels
    )
    return treatment, control


def load_report_catalog(
    repo_root: Path | None = None, reports_root: Path | str = DEFAULT_REPORTS_ROOT
) -> dict[str, dict[str, Any]]:
    root = find_repo_root(repo_root)
    reports_base = resolve_repo_path(root, reports_root)

    catalog: dict[str, dict[str, Any]] = {}
    for method in sorted(REPORT_METHOD_SPECS):
        spec = REPORT_METHOD_SPECS[method]
        folder = canonical_output_dir_name(spec["source_mode"], spec["report_style"])
        path = reports_base / folder / "agentic_report.md"
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        catalog[method] = {
            "report_key": method,
            "path": path,
            "text": text,
            "chars": len(text),
            "lines": text.count("\n") + 1,
        }
    return catalog


def report_catalog_dataframe(catalog: dict[str, dict[str, Any]]) -> pd.DataFrame:
    rows = []
    for report_key, payload in catalog.items():
        rows.append(
            {
                "report_key": report_key,
                "chars": payload["chars"],
                "lines": payload["lines"],
                "path": str(payload["path"]),
            }
        )
    if not rows:
        return pd.DataFrame(columns=["report_key", "chars", "lines", "path"])
    return pd.DataFrame(rows).sort_values("report_key").reset_index(drop=True)


def sanitize_variant_name(name: str) -> str:
    sanitized = re.sub(r"[^a-zA-Z0-9_-]+", "_", name.strip()).strip("_").lower()
    if not sanitized:
        raise ValueError("Variant name cannot be empty after sanitization.")
    return sanitized


def variant_registry_path(repo_root: Path | None = None) -> Path:
    root = find_repo_root(repo_root)
    return resolve_repo_path(root, VARIANT_REGISTRY_PATH)


def output_variant_dir(repo_root: Path | None, variant_name: str) -> Path:
    root = find_repo_root(repo_root)
    reports_root = resolve_repo_path(root, DEFAULT_REPORTS_ROOT)
    return reports_root / sanitize_variant_name(variant_name)


def load_source_memos(
    source_mode: str,
    repo_root: Path | None = None,
) -> dict[str, Any]:
    root = find_repo_root(repo_root)
    reports_root = resolve_repo_path(root, DEFAULT_REPORTS_ROOT)
    source_mode = source_mode.lower().strip()
    if source_mode not in {"both", "data_only", "paper_only"}:
        raise ValueError("source_mode must be one of: both, data_only, paper_only")

    base_dir = reports_root / canonical_output_dir_name(source_mode, "freeform")
    analysis_path = base_dir / "analysis_memo.md"
    paper_path = base_dir / "paper_memo.md"

    payload = {
        "source_mode": source_mode,
        "base_dir": base_dir,
        "analysis_memo_path": analysis_path if analysis_path.exists() else None,
        "paper_memo_path": paper_path if paper_path.exists() else None,
        "analysis_memo": "",
        "paper_memo": "",
    }
    if analysis_path.exists():
        payload["analysis_memo"] = analysis_path.read_text(encoding="utf-8")
    if paper_path.exists():
        payload["paper_memo"] = paper_path.read_text(encoding="utf-8")
    return payload


def build_report_generation_prompt(
    *,
    source_mode: str = "both",
    report_style: str = "structured",
    prompt_addendum: str = "",
    repo_root: Path | None = None,
) -> str:
    memos = load_source_memos(source_mode=source_mode, repo_root=repo_root)
    column_defs = format_column_definitions()
    prompt = build_final_report_prompt(
        column_defs=column_defs,
        analysis_memo=memos["analysis_memo"] or "(analysis memo unavailable)",
        paper_memo=memos["paper_memo"] or "(paper memo unavailable)",
        source_mode=source_mode,
        report_style=report_style,
    )
    if prompt_addendum.strip():
        prompt = (
            prompt
            + "\n\nAdditional instructions for this custom variant:\n"
            + prompt_addendum.strip()
        )
    return prompt


def _ensure_built_in_prompt_artifact(
    variant_dir: Path,
    source_mode: str,
    report_style: str,
) -> Path | None:
    analysis_path = variant_dir / "analysis_memo.md"
    paper_path = variant_dir / "paper_memo.md"
    report_path = variant_dir / "agentic_report.md"
    if not report_path.exists():
        return None

    analysis_memo = (
        analysis_path.read_text(encoding="utf-8")
        if analysis_path.exists()
        else "(analysis memo unavailable)"
    )
    paper_memo = (
        paper_path.read_text(encoding="utf-8")
        if paper_path.exists()
        else "(paper memo unavailable)"
    )
    column_defs = format_column_definitions()

    if report_style == "refined":
        stage1_prompt = build_final_report_prompt(
            column_defs=column_defs,
            analysis_memo=analysis_memo,
            paper_memo=paper_memo,
            source_mode=source_mode,
            report_style="freeform",
        )
        stage2_prompt = build_report_refinement_prompt(
            column_defs=column_defs,
            analysis_memo=analysis_memo,
            paper_memo=paper_memo,
            draft_report="<STAGE_1_DRAFT_REPORT>",
            source_mode=source_mode,
        )
        prompt_text = (
            "# Built-in Report Prompt Record\n\n"
            "This built-in variant used a two-stage generation flow.\n\n"
            "## Stage 1 Draft Prompt\n\n```text\n"
            f"{stage1_prompt}\n```\n\n"
            "## Stage 2 Refinement Prompt Template\n\n"
            "The exact original stage-2 prompt depended on the stage-1 draft. "
            "The template below shows the prompt structure with a placeholder.\n\n"
            "```text\n"
            f"{stage2_prompt}\n```\n"
        )
    elif report_style == "ensemble":
        structured_prompt = build_final_report_prompt(
            column_defs=column_defs,
            analysis_memo=analysis_memo,
            paper_memo=paper_memo,
            source_mode=source_mode,
            report_style="structured",
        )
        quantitative_prompt = build_final_report_prompt(
            column_defs=column_defs,
            analysis_memo=analysis_memo,
            paper_memo=paper_memo,
            source_mode=source_mode,
            report_style="quantitative",
        )
        synthesis_prompt = build_report_ensemble_prompt(
            column_defs=column_defs,
            analysis_memo=analysis_memo,
            paper_memo=paper_memo,
            structured_draft="<STRUCTURED_DRAFT>",
            quantitative_draft="<QUANTITATIVE_DRAFT>",
            source_mode=source_mode,
        )
        prompt_text = (
            "# Built-in Report Prompt Record\n\n"
            "This built-in variant used a multi-stage ensemble generation flow.\n\n"
            "## Stage 1 Structured Draft Prompt\n\n```text\n"
            f"{structured_prompt}\n```\n\n"
            "## Stage 1 Quantitative Draft Prompt\n\n```text\n"
            f"{quantitative_prompt}\n```\n\n"
            "## Stage 2 Synthesis Prompt Template\n\n"
            "The exact original stage-2 prompt depended on the intermediate drafts. "
            "The template below shows the synthesis prompt structure with placeholders.\n\n"
            "```text\n"
            f"{synthesis_prompt}\n```\n"
        )
    else:
        prompt = build_final_report_prompt(
            column_defs=column_defs,
            analysis_memo=analysis_memo,
            paper_memo=paper_memo,
            source_mode=source_mode,
            report_style=report_style,
        )
        prompt_text = (
            "# Built-in Report Prompt Record\n\n"
            "```text\n"
            f"{prompt}\n```\n"
        )

    prompt_path = variant_dir / "report_generation_prompt.md"
    prompt_path.write_text(prompt_text, encoding="utf-8")
    return prompt_path


def sync_report_variant_registry(repo_root: Path | None = None) -> dict[str, dict[str, Any]]:
    root = find_repo_root(repo_root)
    reports_root = resolve_repo_path(root, DEFAULT_REPORTS_ROOT)
    registry_path = variant_registry_path(root)

    registry: dict[str, dict[str, Any]] = {}

    for method, spec in sorted(REPORT_METHOD_SPECS.items()):
        folder = canonical_output_dir_name(spec["source_mode"], spec["report_style"])
        variant_dir = reports_root / folder
        report_path = variant_dir / "agentic_report.md"
        prompt_path = _ensure_built_in_prompt_artifact(
            variant_dir=variant_dir,
            source_mode=spec["source_mode"],
            report_style=spec["report_style"],
        )
        registry[method] = {
            "variant_name": method,
            "variant_type": "built_in",
            "source_mode": spec["source_mode"],
            "report_style": spec["report_style"],
            "variant_dir": str(variant_dir.relative_to(root)),
            "report_path": str(report_path.relative_to(root)),
            "analysis_memo_path": str((variant_dir / "analysis_memo.md").relative_to(root))
            if (variant_dir / "analysis_memo.md").exists()
            else None,
            "paper_memo_path": str((variant_dir / "paper_memo.md").relative_to(root))
            if (variant_dir / "paper_memo.md").exists()
            else None,
            "report_prompt_path": str(prompt_path.relative_to(root))
            if prompt_path is not None
            else None,
            "metadata_path": None,
            "exists": report_path.exists(),
        }

    for metadata_path in sorted(reports_root.glob("*/variant_metadata.json")):
        payload = json.loads(metadata_path.read_text(encoding="utf-8"))
        variant_name = sanitize_variant_name(payload["variant_name"])
        registry[variant_name] = {
            "variant_name": variant_name,
            "variant_type": payload.get("variant_type", "custom"),
            "source_mode": payload.get("source_mode"),
            "report_style": payload.get("report_style"),
            "variant_dir": str(metadata_path.parent.relative_to(root)),
            "report_path": payload.get("report_path"),
            "analysis_memo_path": payload.get("analysis_memo_path"),
            "paper_memo_path": payload.get("paper_memo_path"),
            "report_prompt_path": payload.get("report_prompt_path"),
            "metadata_path": str(metadata_path.relative_to(root)),
            "exists": resolve_repo_path(root, payload.get("report_path", "")).exists()
            if payload.get("report_path")
            else False,
        }

    registry_path.parent.mkdir(parents=True, exist_ok=True)
    registry_path.write_text(
        json.dumps(dict(sorted(registry.items())), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return registry


def load_report_variant_registry(
    repo_root: Path | None = None, refresh: bool = False
) -> dict[str, dict[str, Any]]:
    root = find_repo_root(repo_root)
    registry_path = variant_registry_path(root)
    if refresh or not registry_path.exists():
        return sync_report_variant_registry(root)
    return json.loads(registry_path.read_text(encoding="utf-8"))


def report_variant_registry_dataframe(
    registry: dict[str, dict[str, Any]]
) -> pd.DataFrame:
    rows = []
    for _, payload in sorted(registry.items()):
        rows.append(
            {
                "variant_name": payload["variant_name"],
                "variant_type": payload.get("variant_type"),
                "source_mode": payload.get("source_mode"),
                "report_style": payload.get("report_style"),
                "exists": payload.get("exists"),
                "report_path": payload.get("report_path"),
                "report_prompt_path": payload.get("report_prompt_path"),
            }
        )
    return pd.DataFrame(rows)


def load_report_text_from_variant(
    variant_name: str,
    registry: dict[str, dict[str, Any]],
    repo_root: Path | None = None,
) -> str:
    root = find_repo_root(repo_root)
    variant_key = sanitize_variant_name(variant_name)
    if variant_key not in registry:
        raise KeyError(f"Unknown report variant: {variant_name}")
    report_path = resolve_repo_path(root, registry[variant_key]["report_path"])
    return report_path.read_text(encoding="utf-8")


def default_reasoning_task_prompt(row: pd.Series) -> str:
    return build_single_question_prompt(row)


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


def build_single_question_prompt(row: pd.Series) -> str:
    config = make_config(row)
    return f"""Now, predict the efficiency of the game below when punishment is to be enabled.
### Game Information ###
{config}

Return JSON with exactly these fields:
- "reasoning": concise rationale grounded in the report and game configuration
- "prediction": integer efficiency percentage only (no % sign)
"""


def default_user_prompt(
    row: pd.Series,
    report_text: str | None = None,
    report_instruction: str = DEFAULT_REPORT_INSTRUCTION,
) -> str:
    task_prompt = default_reasoning_task_prompt(row)
    if not report_text:
        return task_prompt
    return f"""{report_instruction}
----------Report Starts----------

{report_text}

----------Report Ends----------
{task_prompt}"""


def build_prediction_user_prompt(row: pd.Series, scenario: dict[str, Any]) -> str:
    return default_user_prompt(
        row=row,
        report_text=scenario.get("report_text"),
        report_instruction=scenario.get("report_instruction", DEFAULT_REPORT_INSTRUCTION),
    )


def make_scenario(
    name: str,
    report_text: str | None = None,
    system_prompt: str = DEFAULT_SYSTEM_PROMPT,
    report_instruction: str = DEFAULT_REPORT_INSTRUCTION,
    notes: str = "",
) -> dict[str, Any]:
    return {
        "name": name,
        "report_text": report_text,
        "system_prompt": system_prompt,
        "report_instruction": report_instruction,
        "notes": notes,
    }


def scenario_from_report_key(
    report_key: str,
    report_catalog: dict[str, dict[str, Any]],
    *,
    name: str | None = None,
    system_prompt: str = DEFAULT_SYSTEM_PROMPT,
    report_instruction: str = DEFAULT_REPORT_INSTRUCTION,
    notes: str = "",
) -> dict[str, Any]:
    if report_key not in report_catalog:
        raise KeyError(f"Unknown report_key: {report_key}")
    return make_scenario(
        name=name or report_key,
        report_text=report_catalog[report_key]["text"],
        system_prompt=system_prompt,
        report_instruction=report_instruction,
        notes=notes,
    )


def scenario_from_variant_name(
    variant_name: str,
    registry: dict[str, dict[str, Any]],
    *,
    repo_root: Path | None = None,
    system_prompt: str = DEFAULT_SYSTEM_PROMPT,
    report_instruction: str = DEFAULT_REPORT_INSTRUCTION,
    notes: str = "",
) -> dict[str, Any]:
    return make_scenario(
        name=sanitize_variant_name(variant_name),
        report_text=load_report_text_from_variant(variant_name, registry, repo_root),
        system_prompt=system_prompt,
        report_instruction=report_instruction,
        notes=notes,
    )


def preview_scenario_prompt(
    validation_df: pd.DataFrame,
    scenario: dict[str, Any],
    build_user_prompt: Callable[[pd.Series, dict[str, Any]], str],
    question_index: int = 0,
) -> dict[str, str]:
    row = validation_df.iloc[question_index]
    return {
        "system_prompt": scenario["system_prompt"],
        "user_prompt": build_user_prompt(row, scenario),
    }


def make_openai_client(api_key: str | None = None, organization: str | None = None):
    try:
        from openai import OpenAI
    except ImportError as exc:  # pragma: no cover - import guard
        raise ImportError(
            "The 'openai' package is required. Install it with `pip install openai`."
        ) from exc

    kwargs: dict[str, Any] = {}
    if api_key:
        kwargs["api_key"] = api_key
    if organization:
        kwargs["organization"] = organization
    return OpenAI(**kwargs)


def _extract_response_output_text(response) -> str:
    text = getattr(response, "output_text", None)
    if text:
        return text

    parts = []
    for item in getattr(response, "output", []) or []:
        for content in getattr(item, "content", []) or []:
            if getattr(content, "type", None) == "output_text":
                parts.append(getattr(content, "text", ""))
    return "\n".join(parts).strip()


def generate_report_variant(
    *,
    client,
    variant_name: str,
    report_prompt: str,
    source_mode: str = "both",
    report_style: str = "custom",
    model: str = "gpt-4.1",
    overwrite: bool = False,
    repo_root: Path | None = None,
) -> dict[str, Any]:
    root = find_repo_root(repo_root)
    variant_key = sanitize_variant_name(variant_name)
    variant_dir = output_variant_dir(root, variant_key)

    if variant_dir.exists() and not overwrite:
        raise FileExistsError(
            f"Variant directory already exists: {variant_dir}. "
            "Set overwrite=True to replace it."
        )

    memos = load_source_memos(source_mode=source_mode, repo_root=root)
    response = client.responses.create(model=model, input=report_prompt)
    report_text = _extract_response_output_text(response)

    variant_dir.mkdir(parents=True, exist_ok=True)
    report_path = variant_dir / "agentic_report.md"
    prompt_path = variant_dir / "report_generation_prompt.md"
    metadata_path = variant_dir / "variant_metadata.json"

    report_path.write_text(report_text.strip() + "\n", encoding="utf-8")
    prompt_path.write_text(report_prompt.strip() + "\n", encoding="utf-8")

    analysis_target = None
    paper_target = None
    if memos["analysis_memo_path"] is not None:
        analysis_target = variant_dir / "analysis_memo.md"
        shutil.copyfile(memos["analysis_memo_path"], analysis_target)
    if memos["paper_memo_path"] is not None:
        paper_target = variant_dir / "paper_memo.md"
        shutil.copyfile(memos["paper_memo_path"], paper_target)

    metadata = {
        "variant_name": variant_key,
        "variant_type": "custom",
        "source_mode": source_mode,
        "report_style": report_style,
        "model": model,
        "variant_dir": str(variant_dir.relative_to(root)),
        "report_path": str(report_path.relative_to(root)),
        "report_prompt_path": str(prompt_path.relative_to(root)),
        "analysis_memo_path": str(analysis_target.relative_to(root))
        if analysis_target is not None
        else None,
        "paper_memo_path": str(paper_target.relative_to(root))
        if paper_target is not None
        else None,
        "response_id": getattr(response, "id", None),
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }
    metadata_path.write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    registry = sync_report_variant_registry(root)
    return {
        "variant_name": variant_key,
        "report_path": report_path,
        "prompt_path": prompt_path,
        "metadata_path": metadata_path,
        "registry_entry": registry[variant_key],
    }


def _extract_numeric(text: str | None) -> float | None:
    if not text:
        return None
    import re

    matches = re.findall(r"-?\d+(?:\.\d+)?", text.replace(",", " "))
    if not matches:
        return None
    try:
        return float(matches[-1])
    except ValueError:
        return None


def parse_reasoning_output(raw_text: str | None) -> dict[str, Any]:
    if not raw_text:
        return {"prediction": None, "reasoning": None, "parsed_json": None}

    text = raw_text.strip()

    def _from_obj(obj: Any) -> dict[str, Any]:
        if not isinstance(obj, dict):
            return {"prediction": None, "reasoning": None, "parsed_json": obj}
        prediction = obj.get("prediction")
        reasoning = obj.get("reasoning")
        parsed_prediction: float | None = None
        if isinstance(prediction, (int, float)) and not np.isnan(prediction):
            parsed_prediction = float(prediction)
        elif isinstance(prediction, str):
            parsed_prediction = _extract_numeric(prediction)
        return {
            "prediction": parsed_prediction,
            "reasoning": reasoning if isinstance(reasoning, str) else None,
            "parsed_json": obj,
        }

    try:
        return _from_obj(json.loads(text))
    except (json.JSONDecodeError, TypeError):
        pass

    if "```" in text:
        start = text.find("{")
        end = text.rfind("}")
        if start != -1 and end != -1 and end > start:
            try:
                return _from_obj(json.loads(text[start : end + 1]))
            except (json.JSONDecodeError, TypeError):
                pass

    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        try:
            return _from_obj(json.loads(text[start : end + 1]))
        except (json.JSONDecodeError, TypeError):
            pass

    return {"prediction": _extract_numeric(text), "reasoning": None, "parsed_json": None}


def call_reasoning_prediction(
    client,
    *,
    model: str,
    system_prompt: str,
    user_prompt: str,
    temperature: float = 1.0,
    max_tokens: int | None = None,
    max_retries: int = 3,
    retry_sleep_seconds: float = 2.0,
) -> dict[str, Any]:
    last_error: Exception | None = None

    for attempt in range(1, max_retries + 1):
        try:
            request_kwargs = {
                "model": model,
                "temperature": temperature,
                "response_format": {"type": "json_object"},
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
            }
            if max_tokens is not None:
                request_kwargs["max_tokens"] = max_tokens

            response = client.chat.completions.create(**request_kwargs)
            raw_text = response.choices[0].message.content or ""
            parsed = parse_reasoning_output(raw_text)
            return {
                "prediction": parsed["prediction"],
                "reasoning": parsed["reasoning"],
                "raw_text": raw_text,
                "parsed_json": parsed["parsed_json"],
                "response_id": getattr(response, "id", None),
                "error": None,
                "attempt": attempt,
            }
        except Exception as exc:  # pragma: no cover - network/API path
            last_error = exc
            if attempt == max_retries:
                break
            time.sleep(retry_sleep_seconds * attempt)

    return {
        "prediction": None,
        "reasoning": None,
        "raw_text": None,
        "parsed_json": None,
        "response_id": None,
        "error": repr(last_error),
        "attempt": max_retries,
    }


def run_scenarios(
    validation_df: pd.DataFrame,
    scenario_specs: list[dict[str, Any]],
    build_user_prompt: Callable[[pd.Series, dict[str, Any]], str],
    *,
    client,
    model: str = "gpt-4.1",
    temperature: float = 1.0,
    max_tokens: int | None = None,
    pause_seconds: float = 0.0,
    question_limit: int | None = None,
    max_retries: int = 3,
    retry_sleep_seconds: float = 2.0,
    verbose: bool = True,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    df = validation_df.copy()
    if question_limit is not None:
        df = df.head(question_limit).copy()

    questions = question_labels(len(df))
    raw_rows: list[dict[str, Any]] = []

    for scenario in scenario_specs:
        scenario_name = scenario["name"]
        if verbose:
            print(f"Running scenario: {scenario_name}")

        for idx, (_, row) in enumerate(df.iterrows(), start=1):
            question = questions[idx - 1]
            user_prompt = build_user_prompt(row, scenario)
            result = call_reasoning_prediction(
                client,
                model=model,
                system_prompt=scenario["system_prompt"],
                user_prompt=user_prompt,
                temperature=temperature,
                max_tokens=max_tokens,
                max_retries=max_retries,
                retry_sleep_seconds=retry_sleep_seconds,
            )

            raw_rows.append(
                {
                    "variation": scenario_name,
                    "question": question,
                    "config_id": int(row["CONFIG_configId"]),
                    "prediction": result["prediction"],
                    "reasoning": result["reasoning"],
                    "raw_text": result["raw_text"],
                    "response_id": result["response_id"],
                    "error": result["error"],
                    "attempt": result["attempt"],
                    "system_prompt": scenario["system_prompt"],
                    "user_prompt": user_prompt,
                    "report_instruction": scenario.get("report_instruction"),
                    "notes": scenario.get("notes", ""),
                }
            )

            if verbose:
                print(
                    f"  {question}: pred={result['prediction']} error={result['error'] is not None}"
                )
            if pause_seconds > 0:
                time.sleep(pause_seconds)

    raw_df = pd.DataFrame(raw_rows)
    pred_df = (
        raw_df.pivot_table(
            index="variation", columns="question", values="prediction", aggfunc="first"
        )
        .reindex(columns=questions)
        .sort_index()
    )
    return pred_df, raw_df


def evaluate_validation_predictions(
    pred_df: pd.DataFrame,
    validation_df: pd.DataFrame,
    *,
    n_boot: int = 2000,
    seed: int = 0,
) -> pd.DataFrame:
    treatment, control = make_validation_ground_truth(validation_df)
    metrics_df = compute_metrics(
        pred_df, treatment, control, np.random.default_rng(seed), n_boot
    )
    return metrics_df.sort_values(
        by=["correlation", "directional_accuracy", "rmse"],
        ascending=[False, False, True],
    )


def _json_safe(obj: Any) -> Any:
    if isinstance(obj, Path):
        return str(obj)
    if isinstance(obj, (np.integer, np.floating)):
        return obj.item()
    return obj


def save_prompt_lab_run(
    run_name: str,
    scenario_specs: list[dict[str, Any]],
    pred_df: pd.DataFrame,
    metrics_df: pd.DataFrame,
    raw_df: pd.DataFrame,
    *,
    validation_df: pd.DataFrame | None = None,
    build_user_prompt: Callable[[pd.Series, dict[str, Any]], str] | None = None,
    output_dir: Path | str = DEFAULT_RESULTS_DIR,
    repo_root: Path | None = None,
) -> Path:
    root = find_repo_root(repo_root)
    base_dir = resolve_repo_path(root, output_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = base_dir / f"{timestamp}_{run_name}"
    run_dir.mkdir(parents=True, exist_ok=True)

    pred_df.to_csv(run_dir / "predictions.csv")
    metrics_df.to_csv(run_dir / "metrics.csv")
    raw_df.to_csv(run_dir / "raw_predictions.csv", index=False)

    with (run_dir / "scenario_specs.json").open("w", encoding="utf-8") as handle:
        json.dump(scenario_specs, handle, ensure_ascii=False, indent=2, default=_json_safe)

    if validation_df is not None and build_user_prompt is not None and scenario_specs:
        previews = []
        for scenario in scenario_specs:
            payload = preview_scenario_prompt(validation_df, scenario, build_user_prompt)
            previews.append(
                {
                    "variation": scenario["name"],
                    "system_prompt": payload["system_prompt"],
                    "user_prompt_q1": payload["user_prompt"],
                }
            )
        with (run_dir / "prompt_previews.json").open("w", encoding="utf-8") as handle:
            json.dump(previews, handle, ensure_ascii=False, indent=2)

    return run_dir
