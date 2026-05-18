from __future__ import annotations

from itertools import combinations
from pathlib import Path
import sys

import numpy as np
import pandas as pd


ANALYSIS_ROOT = Path(__file__).resolve().parents[1]
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

from literature_collection_analysis_reports.analyze_validation_collection_analysis_reports_repeat5 import (  # noqa: E402
    Q_COLS,
    RUN_SPECS,
    _all_paths_exist,
    _baseline_ids,
    _benchmark_ids,
    _load_source_tables,
)


ROOT = ANALYSIS_ROOT.parent
RESULTS_DIR = ROOT / "results" / "validation" / "literature_collection_analysis_reports_repeat5_prediction_variance"
MODEL_ORDER = ["GPT-4.1", "GPT-4.1 Mini", "GPT-5.1", "GPT-5 Mini", "GPT-5 Nano"]
CONDITION_ORDER = ["baseline", "benchmark"]


def load_prediction_rows() -> pd.DataFrame:
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
            for repeat_idx, row_id in enumerate(ids, start=1):
                pred = pd.to_numeric(source_df.loc[row_id], errors="coerce").reindex(Q_COLS)
                row: dict[str, object] = {
                    "model": model,
                    "condition": condition,
                    "repeat": repeat_idx,
                    "row_id": row_id,
                }
                row.update({q: float(pred[q]) for q in Q_COLS})
                rows.append(row)

    out = pd.DataFrame(rows)
    out["model"] = pd.Categorical(out["model"], categories=MODEL_ORDER, ordered=True)
    out["condition"] = pd.Categorical(out["condition"], categories=CONDITION_ORDER, ordered=True)
    return out.sort_values(["condition", "model", "repeat"]).reset_index(drop=True)


def build_question_summary(prediction_rows: pd.DataFrame) -> pd.DataFrame:
    out_rows: list[dict[str, object]] = []

    for condition, part in prediction_rows.groupby("condition", observed=True):
        between_vars: list[float] = []
        within_vars: list[float] = []
        ratios: list[float] = []
        question_etas: list[float] = []

        for question in Q_COLS:
            question_part = part.loc[:, ["model", "repeat", question]].rename(columns={question: "prediction"})
            grand_mean = float(question_part["prediction"].mean())
            model_means = question_part.groupby("model", observed=True)["prediction"].mean()

            ss_between = float(
                sum(
                    int((question_part["model"] == model).sum()) * float((model_mean - grand_mean) ** 2)
                    for model, model_mean in model_means.items()
                )
            )
            merged = question_part.merge(model_means.rename("model_mean"), on="model", how="left")
            ss_within = float(((merged["prediction"] - merged["model_mean"]) ** 2).sum())
            n_obs = int(len(question_part))
            between_var = float(ss_between / n_obs)
            within_var = float(ss_within / n_obs)
            eta = float(ss_between / (ss_between + ss_within)) if (ss_between + ss_within) > 0 else float("nan")

            between_vars.append(between_var)
            within_vars.append(within_var)
            ratios.append(float(between_var / within_var) if within_var > 0 else float("inf"))
            question_etas.append(eta)

        out_rows.append(
            {
                "condition": condition,
                "n_models": int(part["model"].nunique()),
                "n_runs": int(len(part)),
                "mean_between_model_variance_per_question": float(np.mean(between_vars)),
                "mean_within_model_repeat_variance_per_question": float(np.mean(within_vars)),
                "median_between_within_ratio": float(np.median(ratios)),
                "share_questions_between_gt_within": float(np.mean(np.asarray(between_vars) > np.asarray(within_vars))),
                "eta_model_across_questions": float(np.sum(between_vars) / (np.sum(between_vars) + np.sum(within_vars))),
                "mean_question_eta_model": float(np.nanmean(question_etas)),
            }
        )

    return pd.DataFrame(out_rows)


def build_pairwise_summary(prediction_rows: pd.DataFrame) -> pd.DataFrame:
    out_rows: list[dict[str, object]] = []

    for condition, part in prediction_rows.groupby("condition", observed=True):
        vectors = {
            (str(record["model"]), int(record["repeat"])): np.asarray([record[q] for q in Q_COLS], dtype=float)
            for record in part.to_dict("records")
        }
        within_corrs: list[float] = []
        between_corrs: list[float] = []
        within_rmses: list[float] = []
        between_rmses: list[float] = []

        for left, right in combinations(vectors.keys(), 2):
            left_vec = vectors[left]
            right_vec = vectors[right]
            corr = float(np.corrcoef(left_vec, right_vec)[0, 1])
            rmse = float(np.sqrt(np.mean((left_vec - right_vec) ** 2)))
            if left[0] == right[0]:
                within_corrs.append(corr)
                within_rmses.append(rmse)
            else:
                between_corrs.append(corr)
                between_rmses.append(rmse)

        model_avg_vectors = {
            model: part.loc[part["model"].astype(str) == model, Q_COLS].mean(axis=0).to_numpy(dtype=float)
            for model in MODEL_ORDER
        }
        model_mean_corrs = [
            float(np.corrcoef(model_avg_vectors[left], model_avg_vectors[right])[0, 1])
            for left, right in combinations(MODEL_ORDER, 2)
        ]
        model_mean_rmses = [
            float(np.sqrt(np.mean((model_avg_vectors[left] - model_avg_vectors[right]) ** 2)))
            for left, right in combinations(MODEL_ORDER, 2)
        ]

        out_rows.append(
            {
                "condition": condition,
                "mean_within_model_repeat_vector_corr": float(np.mean(within_corrs)),
                "mean_between_model_vector_corr": float(np.mean(between_corrs)),
                "mean_pairwise_corr_of_model_mean_predictions": float(np.mean(model_mean_corrs)),
                "mean_within_model_repeat_vector_rmse": float(np.mean(within_rmses)),
                "mean_between_model_vector_rmse": float(np.mean(between_rmses)),
                "mean_pairwise_rmse_of_model_mean_predictions": float(np.mean(model_mean_rmses)),
            }
        )

    return pd.DataFrame(out_rows)


def build_additive_component_summary(prediction_rows: pd.DataFrame) -> pd.DataFrame:
    long_rows = prediction_rows.melt(
        id_vars=["model", "condition", "repeat"],
        value_vars=Q_COLS,
        var_name="question",
        value_name="prediction",
    )
    out_rows: list[dict[str, object]] = []

    for condition, part in long_rows.groupby("condition", observed=True):
        grand_mean = float(part["prediction"].mean())
        question_means = part.groupby("question", observed=True)["prediction"].mean()
        model_means = part.groupby("model", observed=True)["prediction"].mean()
        question_model_means = part.groupby(["question", "model"], observed=True)["prediction"].mean()

        ss_question = float(
            sum(
                int((part["question"] == question).sum()) * float((value - grand_mean) ** 2)
                for question, value in question_means.items()
            )
        )
        ss_model = float(
            sum(
                int((part["model"] == model).sum()) * float((value - grand_mean) ** 2)
                for model, value in model_means.items()
            )
        )

        merged = (
            part.merge(question_means.rename("question_mean"), on="question", how="left")
            .merge(model_means.rename("model_mean"), on="model", how="left")
            .merge(question_model_means.rename("question_model_mean"), on=["question", "model"], how="left")
        )
        interaction = (
            merged["question_model_mean"] - merged["question_mean"] - merged["model_mean"] + grand_mean
        )
        residual = merged["prediction"] - merged["question_model_mean"]

        ss_question_model_interaction = float((interaction**2).sum())
        ss_repeat_within_question_model = float((residual**2).sum())
        ss_total = float(((merged["prediction"] - grand_mean) ** 2).sum())

        out_rows.append(
            {
                "condition": condition,
                "eta_question": float(ss_question / ss_total),
                "eta_model_marginal": float(ss_model / ss_total),
                "eta_question_model_interaction": float(ss_question_model_interaction / ss_total),
                "eta_repeat_within_question_model": float(ss_repeat_within_question_model / ss_total),
            }
        )

    return pd.DataFrame(out_rows)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    prediction_rows = load_prediction_rows()
    question_summary = build_question_summary(prediction_rows)
    pairwise_summary = build_pairwise_summary(prediction_rows)
    additive_component_summary = build_additive_component_summary(prediction_rows)

    prediction_rows.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_prediction_variance_rows.csv",
        index=False,
    )
    question_summary.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_prediction_variance_question_summary.csv",
        index=False,
    )
    pairwise_summary.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_prediction_variance_pairwise_summary.csv",
        index=False,
    )
    additive_component_summary.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_prediction_variance_additive_component_summary.csv",
        index=False,
    )


if __name__ == "__main__":
    main()
