from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import pandas as pd

from analyze_validation_reasoning_repeat5 import load_prediction_cube, load_targets
from result_paths import (
    VALIDATION_MODEL_SUITE_COMPREHENSIVE_RESULTS,
    VALIDATION_PAPER_ONLY_41FAMILY_RESULTS as RESULTS,
    VALIDATION_REASONING_REPEAT_SUMMARY_RESULTS,
    ensure_results_dir,
)


ROOT = Path(__file__).resolve().parents[1]
OPENAI_BATCH_OUTPUT = ROOT / "openAI_batch_output"

MODELS = ["GPT-4.1", "GPT-4.1 Mini", "GPT-4.1 Nano"]
PAPER_ONLY_VARIANTS = [
    "paper_only_freeform",
    "paper_only_quantitative",
    "paper_only_structured",
]
VARIANTS = ["baseline", *PAPER_ONLY_VARIANTS]

DIRECT_MODEL_PATHS = {
    "GPT-4.1": OPENAI_BATCH_OUTPUT / "prediction_positive_case_variations_41.jsonl",
    "GPT-4.1 Mini": OPENAI_BATCH_OUTPUT / "prediction_crosswave_variations_41mini.jsonl",
    "GPT-4.1 Nano": OPENAI_BATCH_OUTPUT / "prediction_crosswave_variations_41nano.jsonl",
}

BASELINES = (
    VALIDATION_MODEL_SUITE_COMPREHENSIVE_RESULTS / "validation_model_suite_baselines.csv"
)
AUGMENTATION_ROWS = (
    VALIDATION_MODEL_SUITE_COMPREHENSIVE_RESULTS / "validation_model_suite_augmentation_rows.csv"
)
REPEAT_CONDITIONS = (
    VALIDATION_REASONING_REPEAT_SUMMARY_RESULTS
    / "validation_reasoning_repeat5_condition_comparison.csv"
)

DIRECT_OUTPUT = RESULTS / "validation_paper_only_41family_direct.csv"
EXPLAINED_OUTPUT = RESULTS / "validation_paper_only_41family_explained.csv"
COMBINED_OUTPUT = RESULTS / "validation_paper_only_41family_combined.csv"


def _extract_top_logprobs_and_chosen_logprob(body: dict) -> tuple[list[dict], float | None]:
    if body.get("object") != "chat.completion":
        return [], None
    choices = body.get("choices") or []
    if not choices:
        return [], None
    choice = choices[0]
    logprobs = choice.get("logprobs") or {}
    content = logprobs.get("content") or []
    if not content:
        return [], None
    first = content[0]
    return first.get("top_logprobs") or [], first.get("logprob")


def _parse_direct_custom_id(custom_id: str) -> tuple[str, str] | None:
    if "/Q" not in custom_id:
        return None
    variant, label = custom_id.split("/", 1)
    if not label.startswith("Q"):
        return None
    if variant == "baseline" or variant in PAPER_ONLY_VARIANTS:
        return variant, label
    return None


def load_direct_logprob_summary() -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for model, path in DIRECT_MODEL_PATHS.items():
        if not path.exists():
            continue
        with path.open() as f:
            for line in f:
                item = json.loads(line)
                custom_id = item.get("custom_id", "")
                parsed = _parse_direct_custom_id(custom_id)
                if parsed is None:
                    continue
                variant, label = parsed
                body = (item.get("response") or {}).get("body") or {}
                top_logprobs, chosen_logprob = _extract_top_logprobs_and_chosen_logprob(body)
                if chosen_logprob is None:
                    continue
                probs = np.array(
                    [math.exp(entry["logprob"]) for entry in top_logprobs],
                    dtype=float,
                )
                captured_mass = float(probs.sum()) if len(probs) else float("nan")
                if len(probs) and captured_mass > 0:
                    renorm = probs / captured_mass
                    trunc_entropy = float(
                        -np.sum(renorm * np.log(np.clip(renorm, 1e-300, None)))
                    )
                    trunc_perplexity = float(math.exp(trunc_entropy))
                    top1_prob = float(probs[0])
                else:
                    trunc_entropy = float("nan")
                    trunc_perplexity = float("nan")
                    top1_prob = float("nan")
                rows.append(
                    {
                        "model": model,
                        "variant": variant,
                        "label": label,
                        "chosen_logprob": float(chosen_logprob),
                        "chosen_perplexity": float(math.exp(-chosen_logprob)),
                        "top1_prob": top1_prob,
                        "captured_mass": captured_mass,
                        "trunc_entropy_nats": trunc_entropy,
                        "trunc_perplexity": trunc_perplexity,
                        "topk": len(top_logprobs),
                    }
                )
    summary = (
        pd.DataFrame(rows)
        .groupby(["model", "variant"], as_index=False)
        .agg(
            n_questions=("label", "size"),
            mean_chosen_logprob=("chosen_logprob", "mean"),
            mean_chosen_perplexity=("chosen_perplexity", "mean"),
            mean_top1_prob=("top1_prob", "mean"),
            mean_captured_mass=("captured_mass", "mean"),
            mean_trunc_entropy_nats=("trunc_entropy_nats", "mean"),
            mean_trunc_perplexity=("trunc_perplexity", "mean"),
            topk=("topk", "median"),
        )
    )
    return summary


def load_direct_performance() -> pd.DataFrame:
    baselines = pd.read_csv(BASELINES)
    baseline_direct = (
        baselines.loc[
            baselines["model"].isin(MODELS) & (baselines["mode"] == "single"),
            ["model", "rmse", "correlation", "r2", "directional_accuracy"],
        ]
        .rename(
            columns={
                "rmse": "baseline_rmse",
                "correlation": "baseline_correlation",
                "r2": "baseline_r2",
                "directional_accuracy": "baseline_directional_accuracy",
            }
        )
        .copy()
    )
    baseline_direct["variant"] = "baseline"
    for metric in ["rmse", "correlation", "r2", "directional_accuracy"]:
        baseline_direct[metric] = baseline_direct[f"baseline_{metric}"]
        baseline_direct[f"delta_{metric}"] = 0.0

    aug_rows = pd.read_csv(AUGMENTATION_ROWS)
    aug_direct = aug_rows.loc[
        aug_rows["model"].isin(MODELS)
        & (aug_rows["mode"] == "single")
        & aug_rows["variant_name"].isin(PAPER_ONLY_VARIANTS),
        [
            "model",
            "variant_name",
            "rmse",
            "correlation",
            "r2",
            "directional_accuracy",
            "baseline_rmse",
            "baseline_correlation",
            "baseline_r2",
            "baseline_directional_accuracy",
            "delta_rmse",
            "delta_correlation",
            "delta_r2",
            "delta_directional_accuracy",
        ],
    ].rename(columns={"variant_name": "variant"})

    return pd.concat([baseline_direct, aug_direct], ignore_index=True, sort=False)


def build_direct_table() -> pd.DataFrame:
    perf = load_direct_performance()
    uncertainty = load_direct_logprob_summary()
    merged = perf.merge(uncertainty, on=["model", "variant"], how="left")

    baseline = (
        merged.loc[
            merged["variant"] == "baseline",
            [
                "model",
                "n_questions",
                "mean_chosen_logprob",
                "mean_chosen_perplexity",
                "mean_top1_prob",
                "mean_captured_mass",
                "mean_trunc_entropy_nats",
                "mean_trunc_perplexity",
                "topk",
            ],
        ]
        .rename(
            columns={
                "mean_chosen_logprob": "baseline_mean_chosen_logprob",
                "mean_chosen_perplexity": "baseline_mean_chosen_perplexity",
                "mean_top1_prob": "baseline_mean_top1_prob",
                "mean_captured_mass": "baseline_mean_captured_mass",
                "mean_trunc_entropy_nats": "baseline_mean_trunc_entropy_nats",
                "mean_trunc_perplexity": "baseline_mean_trunc_perplexity",
                "topk": "baseline_topk",
                "n_questions": "baseline_n_questions",
            }
        )
    )
    merged = merged.merge(baseline, on="model", how="left")
    merged["mode"] = "single"
    merged["mode_label"] = "single w/o explanation"
    merged["uncertainty_metric"] = "mean chosen-token perplexity"
    merged["uncertainty_value"] = merged["mean_chosen_perplexity"]
    merged["baseline_uncertainty_value"] = merged["baseline_mean_chosen_perplexity"]
    merged["delta_uncertainty_value"] = (
        merged["uncertainty_value"] - merged["baseline_uncertainty_value"]
    )
    return merged.sort_values(["model", "variant"]).reset_index(drop=True)


def build_explained_table() -> pd.DataFrame:
    cond = pd.read_csv(REPEAT_CONDITIONS)
    cond = cond.loc[
        cond["model"].isin(MODELS)
        & cond["mode"].isin(["reasoning", "joint_reasoning"])
        & cond["variant"].isin(VARIANTS)
    ].copy()

    target, _ = load_targets()
    cube = load_prediction_cube(target)
    q_sd_rows: list[dict[str, object]] = []
    for model in MODELS:
        for mode in ["reasoning", "joint_reasoning"]:
            for variant in VARIANTS:
                labels = [
                    label
                    for label in ["initial", "rep1", "rep2", "rep3", "rep4"]
                    if (model, mode, variant, label) in cube
                ]
                if len(labels) < 2:
                    continue
                preds = pd.concat(
                    [cube[(model, mode, variant, label)] for label in labels],
                    axis=1,
                )
                preds.columns = labels
                q_sd = preds.std(axis=1, ddof=1)
                q_sd_rows.append(
                    {
                        "model": model,
                        "mode": mode,
                        "variant": variant,
                        "mean_question_sd": float(q_sd.mean()),
                        "median_question_sd": float(q_sd.median()),
                        "max_question_sd": float(q_sd.max()),
                    }
                )
    q_sd_df = pd.DataFrame(q_sd_rows)
    merged = cond.merge(q_sd_df, on=["model", "mode", "variant"], how="left")

    baseline = (
        merged.loc[merged["variant"] == "baseline"]
        .drop(columns=["variant"])
        .rename(
            columns={
                "mean_prediction_metric_rmse": "baseline_mean_prediction_metric_rmse",
                "mean_prediction_metric_correlation": "baseline_mean_prediction_metric_correlation",
                "mean_prediction_metric_r2": "baseline_mean_prediction_metric_r2",
                "mean_prediction_metric_directional_accuracy": "baseline_mean_prediction_metric_directional_accuracy",
                "mean_question_sd": "baseline_mean_question_sd",
                "median_question_sd": "baseline_median_question_sd",
                "max_question_sd": "baseline_max_question_sd",
            }
        )
    )
    merged = merged.merge(baseline, on=["model", "mode"], how="left")
    merged["delta_mean_prediction_metric_rmse"] = (
        merged["mean_prediction_metric_rmse"]
        - merged["baseline_mean_prediction_metric_rmse"]
    )
    merged["delta_mean_prediction_metric_correlation"] = (
        merged["mean_prediction_metric_correlation"]
        - merged["baseline_mean_prediction_metric_correlation"]
    )
    merged["delta_mean_prediction_metric_r2"] = (
        merged["mean_prediction_metric_r2"]
        - merged["baseline_mean_prediction_metric_r2"]
    )
    merged["delta_mean_prediction_metric_directional_accuracy"] = (
        merged["mean_prediction_metric_directional_accuracy"]
        - merged["baseline_mean_prediction_metric_directional_accuracy"]
    )
    merged["delta_mean_question_sd"] = (
        merged["mean_question_sd"] - merged["baseline_mean_question_sd"]
    )
    merged["mode_label"] = merged["mode"].map(
        {
            "reasoning": "single with explanation",
            "joint_reasoning": "joint with explanation",
        }
    )
    merged["uncertainty_metric"] = "mean question-level SD across 5 runs"
    merged["uncertainty_value"] = merged["mean_question_sd"]
    merged["baseline_uncertainty_value"] = merged["baseline_mean_question_sd"]
    merged["delta_uncertainty_value"] = merged["delta_mean_question_sd"]
    return merged.sort_values(["model", "mode", "variant"]).reset_index(drop=True)


def build_combined_table(direct: pd.DataFrame, explained: pd.DataFrame) -> pd.DataFrame:
    direct_part = direct[
        [
            "model",
            "mode",
            "mode_label",
            "variant",
            "rmse",
            "correlation",
            "r2",
            "directional_accuracy",
            "baseline_rmse",
            "baseline_correlation",
            "baseline_r2",
            "baseline_directional_accuracy",
            "delta_rmse",
            "delta_correlation",
            "delta_r2",
            "delta_directional_accuracy",
            "uncertainty_metric",
            "uncertainty_value",
            "baseline_uncertainty_value",
            "delta_uncertainty_value",
        ]
    ].copy()

    explained_part = explained[
        [
            "model",
            "mode",
            "mode_label",
            "variant",
            "mean_prediction_metric_rmse",
            "mean_prediction_metric_correlation",
            "mean_prediction_metric_r2",
            "mean_prediction_metric_directional_accuracy",
            "baseline_mean_prediction_metric_rmse",
            "baseline_mean_prediction_metric_correlation",
            "baseline_mean_prediction_metric_r2",
            "baseline_mean_prediction_metric_directional_accuracy",
            "delta_mean_prediction_metric_rmse",
            "delta_mean_prediction_metric_correlation",
            "delta_mean_prediction_metric_r2",
            "delta_mean_prediction_metric_directional_accuracy",
            "uncertainty_metric",
            "uncertainty_value",
            "baseline_uncertainty_value",
            "delta_uncertainty_value",
        ]
    ].rename(
        columns={
            "mean_prediction_metric_rmse": "rmse",
            "mean_prediction_metric_correlation": "correlation",
            "mean_prediction_metric_r2": "r2",
            "mean_prediction_metric_directional_accuracy": "directional_accuracy",
            "baseline_mean_prediction_metric_rmse": "baseline_rmse",
            "baseline_mean_prediction_metric_correlation": "baseline_correlation",
            "baseline_mean_prediction_metric_r2": "baseline_r2",
            "baseline_mean_prediction_metric_directional_accuracy": "baseline_directional_accuracy",
            "delta_mean_prediction_metric_rmse": "delta_rmse",
            "delta_mean_prediction_metric_correlation": "delta_correlation",
            "delta_mean_prediction_metric_r2": "delta_r2",
            "delta_mean_prediction_metric_directional_accuracy": "delta_directional_accuracy",
        }
    )

    combined = pd.concat([direct_part, explained_part], ignore_index=True, sort=False)
    mode_order = {
        "single": 0,
        "reasoning": 1,
        "joint_reasoning": 2,
    }
    variant_order = {name: idx for idx, name in enumerate(VARIANTS)}
    combined["_mode_order"] = combined["mode"].map(mode_order)
    combined["_variant_order"] = combined["variant"].map(variant_order)
    combined = combined.sort_values(
        ["model", "_mode_order", "_variant_order"]
    ).drop(columns=["_mode_order", "_variant_order"])
    return combined.reset_index(drop=True)


def main() -> None:
    ensure_results_dir(RESULTS)
    direct = build_direct_table()
    explained = build_explained_table()
    combined = build_combined_table(direct, explained)

    direct.to_csv(DIRECT_OUTPUT, index=False)
    explained.to_csv(EXPLAINED_OUTPUT, index=False)
    combined.to_csv(COMBINED_OUTPUT, index=False)

    print(DIRECT_OUTPUT)
    print(EXPLAINED_OUTPUT)
    print(COMBINED_OUTPUT)


if __name__ == "__main__":
    main()
