from __future__ import annotations

from itertools import combinations
from pathlib import Path

import numpy as np
import pandas as pd

from analyze_validation_collection_analysis_reports_repeat5 import (
    Q_COLS,
    RUN_SPECS,
    _all_paths_exist,
    _baseline_ids,
    _benchmark_ids,
    _load_source_tables,
    compute_metrics,
    load_learning_treatment_mean,
    load_truth,
)


ROOT = Path(__file__).resolve().parents[2]
RESULTS_DIR = ROOT / "results" / "validation" / "literature_collection_analysis_reports_repeat5_model_sampling"
MODEL_ORDER = ["GPT-4.1", "GPT-4.1 Mini", "GPT-4.1 Nano", "GPT-5.1", "GPT-5 Mini", "GPT-5 Nano"]
CONDITION_ORDER = ["baseline", "benchmark"]
METRICS = ["correlation", "rmse", "r2"]


def load_repeat_rows() -> pd.DataFrame:
    treatment, control = load_truth()
    learning_mean = load_learning_treatment_mean()
    rows: list[dict[str, object]] = []

    for spec in RUN_SPECS:
        model = str(spec["model"])
        if model not in MODEL_ORDER or not _all_paths_exist(spec):
            continue

        baseline_df, _, benchmark_df, _ = _load_source_tables(spec)
        for condition, source_df, ids in [
            ("baseline", baseline_df, _baseline_ids(spec)),
            ("benchmark", benchmark_df, _benchmark_ids(spec)),
        ]:
            for repeat_index, row_id in enumerate(ids, start=1):
                pred_row = pd.to_numeric(source_df.loc[row_id], errors="coerce").reindex(Q_COLS)
                metrics = compute_metrics(pred_row, treatment, control, learning_mean)
                row: dict[str, object] = {
                    "model": model,
                    "condition": condition,
                    "repeat": repeat_index,
                    "row_id": row_id,
                    **metrics,
                }
                row.update({q: float(pred_row[q]) for q in Q_COLS})
                rows.append(row)

    out = pd.DataFrame(rows)
    out["model"] = pd.Categorical(out["model"], categories=MODEL_ORDER, ordered=True)
    out["condition"] = pd.Categorical(out["condition"], categories=CONDITION_ORDER, ordered=True)
    return out.sort_values(["condition", "model", "repeat"]).reset_index(drop=True)


def _variance_decomposition(part: pd.DataFrame, metric: str) -> dict[str, float]:
    grand_mean = float(part[metric].mean())
    model_means = part.groupby("model", observed=True)[metric].mean()
    ss_between = sum(int((part["model"] == model).sum()) * float((model_mean - grand_mean) ** 2) for model, model_mean in model_means.items())
    merged = part.merge(model_means.rename("model_mean"), on="model", how="left")
    ss_within = float(((merged[metric] - merged["model_mean"]) ** 2).sum())
    denom = ss_between + ss_within
    eta_model = float(ss_between / denom) if denom > 0 else float("nan")
    return {
        "between_sd_model_means": float(model_means.std(ddof=0)),
        "mean_within_model_sd": float(part.groupby("model", observed=True)[metric].std(ddof=0).mean()),
        "ss_between": float(ss_between),
        "ss_within": float(ss_within),
        "eta_model": eta_model,
    }


def build_repeat_metric_summary(repeat_rows: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for condition, part in repeat_rows.groupby("condition", observed=True):
        for metric in METRICS:
            model_means = part.groupby("model", observed=True)[metric].mean()
            model_sds = part.groupby("model", observed=True)[metric].std(ddof=0)
            decomp = _variance_decomposition(part, metric)
            rows.append(
                {
                    "condition": condition,
                    "metric": metric,
                    **{f"{model}_mean": float(model_means.loc[model]) for model in model_means.index.astype(str)},
                    **{f"{model}_sd": float(model_sds.loc[model]) for model in model_sds.index.astype(str)},
                    **decomp,
                }
            )
    return pd.DataFrame(rows)


def build_question_decomposition(repeat_rows: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    per_question_rows: list[dict[str, object]] = []
    condition_summary_rows: list[dict[str, object]] = []

    for condition, part in repeat_rows.groupby("condition", observed=True):
        between_vars: list[float] = []
        within_vars: list[float] = []
        ratios: list[float] = []
        for question in Q_COLS:
            question_part = part.loc[:, ["model", "repeat", question]].rename(columns={question: "prediction"})
            grand_mean = float(question_part["prediction"].mean())
            model_means = question_part.groupby("model", observed=True)["prediction"].mean()
            ss_between = sum(
                int((question_part["model"] == model).sum()) * float((model_mean - grand_mean) ** 2)
                for model, model_mean in model_means.items()
            )
            merged = question_part.merge(model_means.rename("model_mean"), on="model", how="left")
            ss_within = float(((merged["prediction"] - merged["model_mean"]) ** 2).sum())
            n_obs = int(len(question_part))
            between_var = float(ss_between / n_obs)
            within_var = float(ss_within / n_obs)
            ratio = float(between_var / within_var) if within_var > 0 else float("inf")
            eta_model = float(ss_between / (ss_between + ss_within)) if (ss_between + ss_within) > 0 else float("nan")
            between_vars.append(between_var)
            within_vars.append(within_var)
            ratios.append(ratio)
            per_question_rows.append(
                {
                    "condition": condition,
                    "question": question,
                    "between_model_variance": between_var,
                    "within_model_repeat_variance": within_var,
                    "between_within_ratio": ratio,
                    "eta_model": eta_model,
                }
            )

        condition_summary_rows.append(
            {
                "condition": condition,
                "mean_between_model_variance": float(np.mean(between_vars)),
                "mean_within_model_repeat_variance": float(np.mean(within_vars)),
                "median_between_within_ratio": float(np.median(ratios)),
                "share_questions_between_gt_within": float(np.mean(np.asarray(between_vars) > np.asarray(within_vars))),
                "eta_model_across_questions": float(np.sum(between_vars) / (np.sum(between_vars) + np.sum(within_vars))),
            }
        )

    return pd.DataFrame(per_question_rows), pd.DataFrame(condition_summary_rows)


def build_prediction_correlation_summary(repeat_rows: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    pair_rows: list[dict[str, object]] = []
    condition_rows: list[dict[str, object]] = []

    for condition, part in repeat_rows.groupby("condition", observed=True):
        vectors = {
            (str(record["model"]), int(record["repeat"])): np.asarray([record[q] for q in Q_COLS], dtype=float)
            for record in part.to_dict("records")
        }
        within_corrs: list[float] = []
        between_corrs: list[float] = []
        for left, right in combinations(vectors.keys(), 2):
            corr = float(np.corrcoef(vectors[left], vectors[right])[0, 1])
            pair_type = "within_model" if left[0] == right[0] else "between_model"
            if pair_type == "within_model":
                within_corrs.append(corr)
            else:
                between_corrs.append(corr)
            pair_rows.append(
                {
                    "condition": condition,
                    "left_model": left[0],
                    "left_repeat": left[1],
                    "right_model": right[0],
                    "right_repeat": right[1],
                    "pair_type": pair_type,
                    "prediction_corr": corr,
                }
            )

        model_avg_vectors = {
            model: part.loc[part["model"].astype(str) == model, Q_COLS].mean(axis=0).to_numpy(dtype=float)
            for model in MODEL_ORDER
        }
        model_mean_corrs = [
            float(np.corrcoef(model_avg_vectors[left], model_avg_vectors[right])[0, 1])
            for left, right in combinations(MODEL_ORDER, 2)
        ]
        condition_rows.append(
            {
                "condition": condition,
                "mean_within_model_repeat_prediction_corr": float(np.mean(within_corrs)),
                "mean_between_model_repeat_prediction_corr": float(np.mean(between_corrs)),
                "mean_pairwise_corr_of_model_mean_predictions": float(np.mean(model_mean_corrs)),
            }
        )

    return pd.DataFrame(pair_rows), pd.DataFrame(condition_rows)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    repeat_rows = load_repeat_rows()
    repeat_metric_summary = build_repeat_metric_summary(repeat_rows)
    question_decomposition, question_summary = build_question_decomposition(repeat_rows)
    prediction_corr_pairs, prediction_corr_summary = build_prediction_correlation_summary(repeat_rows)

    repeat_rows.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_model_sampling_repeat_rows.csv",
        index=False,
    )
    repeat_metric_summary.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_model_sampling_repeat_metric_summary.csv",
        index=False,
    )
    question_decomposition.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_model_sampling_question_decomposition.csv",
        index=False,
    )
    question_summary.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_model_sampling_question_summary.csv",
        index=False,
    )
    prediction_corr_pairs.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_model_sampling_prediction_corr_pairs.csv",
        index=False,
    )
    prediction_corr_summary.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_model_sampling_prediction_corr_summary.csv",
        index=False,
    )


if __name__ == "__main__":
    main()
