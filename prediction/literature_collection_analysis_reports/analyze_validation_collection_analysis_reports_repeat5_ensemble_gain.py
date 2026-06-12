from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from analyze_validation_collection_analysis_reports_repeat5 import (
    RUN_SPECS,
    compute_metrics,
    load_learning_treatment_mean,
    load_truth,
    load_variant_metadata,
    _all_paths_exist,
    _baseline_ids,
    _benchmark_ids,
    _collection_ids,
    _full_benchmark_ids,
    _load_source_tables,
    _mean_rows,
)


ROOT = Path(__file__).resolve().parents[2]
RESULTS_DIR = ROOT / "results" / "validation" / "literature_collection_analysis_reports_repeat5_ensemble_gain"
RUN_ROWS_CSV = (
    RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_ensemble_gain_run_rows.csv"
)
ENSEMBLE_ROWS_CSV = (
    RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_ensemble_gain_rows.csv"
)
SUMMARY_BY_METRIC_CSV = (
    RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_ensemble_gain_summary_by_metric.csv"
)
SUMMARY_BY_MODEL_METRIC_CSV = (
    RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_ensemble_gain_summary_by_model_metric.csv"
)
SUMMARY_BY_VARIANT_KIND_METRIC_CSV = (
    RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_ensemble_gain_summary_by_variant_kind_metric.csv"
)
SUMMARY_BY_VARIANT_METRIC_CSV = (
    RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_ensemble_gain_summary_by_variant_metric.csv"
)

METRICS = ["correlation", "rmse", "r2", "directional_accuracy"]
HIGHER_IS_BETTER = {"correlation", "r2", "directional_accuracy"}


def iter_condition_records(
    spec: dict[str, object],
    metadata: dict[str, dict[str, object]],
) -> list[dict[str, object]]:
    baseline_source_df, collection_source_df, benchmark_source_df, full_benchmark_source_df = _load_source_tables(spec)
    out: list[dict[str, object]] = []

    baseline_ids = _baseline_ids(spec)
    if all(row_id in baseline_source_df.index for row_id in baseline_ids):
        out.append(
            {
                "model": str(spec["model"]),
                "mode": str(spec["mode"]),
                "variant_id": "baseline_no_augmentation",
                "variant_kind": "baseline",
                "count": np.nan,
                "description": "No-input baseline with five stochastic repeats.",
                "report_path": "",
                "row_ids": baseline_ids,
                "source_df": baseline_source_df,
            }
        )

    for variant_id, meta in metadata.items():
        if variant_id == spec["benchmark_variant_id"]:
            row_ids = _benchmark_ids(spec)
            source_df = benchmark_source_df
        elif variant_id == spec.get("full_benchmark_variant_id"):
            row_ids = _full_benchmark_ids(spec)
            source_df = full_benchmark_source_df
        else:
            row_ids = _collection_ids(spec, variant_id)
            source_df = collection_source_df

        if not row_ids or any(row_id not in source_df.index for row_id in row_ids):
            continue

        out.append(
            {
                "model": str(spec["model"]),
                "mode": str(spec["mode"]),
                "variant_id": variant_id,
                "variant_kind": str(meta["variant_kind"]),
                "count": meta["count"],
                "description": str(meta["description"]),
                "report_path": str(meta["report_path"]),
                "row_ids": row_ids,
                "source_df": source_df,
            }
        )

    return out


def summarize_group(df: pd.DataFrame, group_cols: list[str]) -> pd.DataFrame:
    summary_rows: list[dict[str, object]] = []
    for metric in METRICS:
        gain_col = f"ensemble_gain_{metric}"
        if group_cols:
            grouped = df.groupby(group_cols, dropna=False, observed=True)
        else:
            grouped = [((), df)]
        for group_key, part in grouped:
            if not isinstance(group_key, tuple):
                group_key = (group_key,)
            row = {col: value for col, value in zip(group_cols, group_key)}
            gains = pd.to_numeric(part[gain_col], errors="coerce")
            gains = gains[np.isfinite(gains)]
            if gains.empty:
                continue
            row.update(
                {
                    "metric": metric,
                    "n_cells": int(len(gains)),
                    "n_positive": int((gains > 0).sum()),
                    "share_positive": float((gains > 0).mean()),
                    "mean_gain": float(gains.mean()),
                    "median_gain": float(gains.median()),
                    "min_gain": float(gains.min()),
                    "max_gain": float(gains.max()),
                }
            )
            summary_rows.append(row)
    return pd.DataFrame(summary_rows)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    treatment, control = load_truth()
    learning_mean = load_learning_treatment_mean()
    metadata = load_variant_metadata()

    run_rows: list[dict[str, object]] = []
    ensemble_rows: list[dict[str, object]] = []

    for spec in RUN_SPECS:
        if not _all_paths_exist(spec):
            continue

        for record in iter_condition_records(spec, metadata):
            source_df = record["source_df"]
            row_ids = list(record["row_ids"])

            run_metric_rows: list[dict[str, object]] = []
            for run_index, row_id in enumerate(row_ids, start=1):
                pred_row = source_df.loc[row_id]
                metrics = compute_metrics(pred_row, treatment, control, learning_mean)
                run_row = {
                    "model": record["model"],
                    "mode": record["mode"],
                    "variant_id": record["variant_id"],
                    "variant_kind": record["variant_kind"],
                    "count": record["count"],
                    "description": record["description"],
                    "report_path": record["report_path"],
                    "n_runs": len(row_ids),
                    "run_order": run_index,
                    "row_id": row_id,
                    **metrics,
                }
                run_rows.append(run_row)
                run_metric_rows.append(run_row)

            avg_pred = _mean_rows(source_df, row_ids)
            avg_metrics = compute_metrics(avg_pred, treatment, control, learning_mean)
            run_metric_df = pd.DataFrame(run_metric_rows)

            out_row: dict[str, object] = {
                "model": record["model"],
                "mode": record["mode"],
                "variant_id": record["variant_id"],
                "variant_kind": record["variant_kind"],
                "count": record["count"],
                "description": record["description"],
                "report_path": record["report_path"],
                "n_runs": len(row_ids),
            }
            for metric in METRICS:
                single_run_vals = pd.to_numeric(run_metric_df[metric], errors="coerce")
                mean_single_run = float(single_run_vals.mean())
                sd_single_run = float(single_run_vals.std(ddof=1))
                avg_prediction_value = float(avg_metrics[metric])
                if metric in HIGHER_IS_BETTER:
                    gain = avg_prediction_value - mean_single_run
                else:
                    gain = mean_single_run - avg_prediction_value
                out_row[f"mean_single_run_{metric}"] = mean_single_run
                out_row[f"sd_single_run_{metric}"] = sd_single_run
                out_row[f"avg_prediction_{metric}"] = avg_prediction_value
                out_row[f"ensemble_gain_{metric}"] = float(gain)
                out_row[f"ensemble_improved_{metric}"] = bool(gain > 0)
            ensemble_rows.append(out_row)

    run_rows_df = pd.DataFrame(run_rows).sort_values(["model", "variant_id", "run_order"]).reset_index(drop=True)
    ensemble_rows_df = pd.DataFrame(ensemble_rows).sort_values(["model", "variant_kind", "variant_id"]).reset_index(
        drop=True
    )

    summary_by_metric = summarize_group(ensemble_rows_df, [])
    summary_by_model_metric = summarize_group(ensemble_rows_df, ["model"])
    summary_by_variant_kind_metric = summarize_group(ensemble_rows_df, ["variant_kind"])
    summary_by_variant_metric = summarize_group(ensemble_rows_df, ["variant_id"])

    run_rows_df.to_csv(RUN_ROWS_CSV, index=False)
    ensemble_rows_df.to_csv(ENSEMBLE_ROWS_CSV, index=False)
    summary_by_metric.to_csv(SUMMARY_BY_METRIC_CSV, index=False)
    summary_by_model_metric.to_csv(SUMMARY_BY_MODEL_METRIC_CSV, index=False)
    summary_by_variant_kind_metric.to_csv(SUMMARY_BY_VARIANT_KIND_METRIC_CSV, index=False)
    summary_by_variant_metric.to_csv(SUMMARY_BY_VARIANT_METRIC_CSV, index=False)


if __name__ == "__main__":
    main()
