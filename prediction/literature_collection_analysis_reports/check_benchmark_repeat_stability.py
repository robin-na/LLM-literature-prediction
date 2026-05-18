from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ANALYSIS_ROOT = Path(__file__).resolve().parents[1]
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

from jsonl_parser import jsonl_to_dataframe  # noqa: E402
from literature_collection_analysis_reports.analyze_validation_collection_analysis_reports_repeat5 import (  # noqa: E402
    Q_COLS,
    RUN_SPECS,
    _baseline_ids,
    _benchmark_ids,
    _load_source_tables,
    compute_metrics,
    load_learning_treatment_mean,
    load_truth,
)


ROOT = ANALYSIS_ROOT.parent
RESULTS_DIR = ROOT / "results" / "validation" / "literature_collection_analysis_reports_repeat5"


def _repeat_label(row_id: str, initial_id: str | None) -> str:
    if initial_id is not None and row_id == initial_id:
        return "initial"
    if "_rep" in row_id:
        return "rep" + row_id.split("_rep")[-1].split("/")[0]
    return row_id


def _mean_rows(df: pd.DataFrame, row_ids: list[str]) -> tuple[pd.Series, pd.DataFrame]:
    rows = [pd.to_numeric(df.loc[row_id], errors="coerce").reindex(Q_COLS) for row_id in row_ids]
    mat = pd.concat(rows, axis=1)
    mat.columns = row_ids
    return mat.mean(axis=1, skipna=True), mat


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    treatment, control = load_truth()
    learning_mean = load_learning_treatment_mean()

    run_rows: list[dict[str, object]] = []
    avg_rows: list[dict[str, object]] = []
    question_sd_rows: list[dict[str, object]] = []
    leave_one_out_rows: list[dict[str, object]] = []

    for spec in RUN_SPECS:
        model = str(spec["model"])
        baseline_source_df, _, benchmark_source_df = _load_source_tables(spec)
        baseline_ids = _baseline_ids(spec)
        benchmark_ids = _benchmark_ids(spec)
        baseline_initial_id = str(spec["baseline_initial_id"]) if "baseline_initial_id" in spec else None
        benchmark_initial_id = str(spec["benchmark_initial_id"]) if "benchmark_initial_id" in spec else None

        for series, source_df, row_ids, initial_id in [
            ("baseline", baseline_source_df, baseline_ids, baseline_initial_id),
            ("benchmark", benchmark_source_df, benchmark_ids, benchmark_initial_id),
        ]:
            for row_id in row_ids:
                pred_row = source_df.loc[row_id]
                metrics = compute_metrics(pred_row, treatment, control, learning_mean)
                run_rows.append(
                    {
                        "model": model,
                        "series": series,
                        "row_id": row_id,
                        "repeat_label": _repeat_label(row_id, initial_id),
                        **metrics,
                        "n_missing": int(pd.to_numeric(pred_row, errors="coerce").reindex(Q_COLS).isna().sum()),
                    }
                )

            avg_pred, mat = _mean_rows(source_df, row_ids)
            avg_rows.append({"model": model, "series": series, **compute_metrics(avg_pred, treatment, control, learning_mean)})

            qsd = mat.std(axis=1, ddof=1)
            for q_label, sd in qsd.items():
                question_sd_rows.append(
                    {
                        "model": model,
                        "series": series,
                        "question": q_label,
                        "prediction_sd": float(sd),
                    }
                )

            for dropped in [None, *row_ids]:
                keep_ids = [row_id for row_id in row_ids if row_id != dropped]
                avg_pred_drop, _ = _mean_rows(source_df, keep_ids)
                metrics = compute_metrics(avg_pred_drop, treatment, control, learning_mean)
                leave_one_out_rows.append(
                    {
                        "model": model,
                        "series": series,
                        "dropped_run": "none" if dropped is None else _repeat_label(dropped, initial_id),
                        **metrics,
                    }
                )

    run_df = pd.DataFrame(run_rows)
    avg_df = pd.DataFrame(avg_rows)
    question_sd_df = pd.DataFrame(question_sd_rows)
    leave_one_out_df = pd.DataFrame(leave_one_out_rows)

    summary_df = (
        run_df.groupby(["model", "series"], dropna=False)
        .agg(
            n_runs=("correlation", "size"),
            corr_mean=("correlation", "mean"),
            corr_sd=("correlation", "std"),
            corr_min=("correlation", "min"),
            corr_max=("correlation", "max"),
            rmse_mean=("rmse", "mean"),
            rmse_sd=("rmse", "std"),
            r2_mean=("r2", "mean"),
            r2_sd=("r2", "std"),
            da_mean=("directional_accuracy", "mean"),
            da_sd=("directional_accuracy", "std"),
            total_missing=("n_missing", "sum"),
        )
        .reset_index()
    )
    summary_df = summary_df.merge(
        avg_df.rename(
            columns={
                "correlation": "avg_prediction_correlation",
                "rmse": "avg_prediction_rmse",
                "r2": "avg_prediction_r2",
                "directional_accuracy": "avg_prediction_directional_accuracy",
            }
        ),
        on=["model", "series"],
        how="left",
    )
    qsd_summary_df = (
        question_sd_df.groupby(["model", "series"], dropna=False)
        .agg(
            mean_question_sd=("prediction_sd", "mean"),
            median_question_sd=("prediction_sd", "median"),
            max_question_sd=("prediction_sd", "max"),
        )
        .reset_index()
    )

    run_df.to_csv(RESULTS_DIR / "benchmark_repeat_run_metrics.csv", index=False)
    avg_df.to_csv(RESULTS_DIR / "benchmark_repeat_avg_prediction_metrics.csv", index=False)
    summary_df.to_csv(RESULTS_DIR / "benchmark_repeat_summary.csv", index=False)
    question_sd_df.to_csv(RESULTS_DIR / "benchmark_repeat_question_sd.csv", index=False)
    qsd_summary_df.to_csv(RESULTS_DIR / "benchmark_repeat_question_sd_summary.csv", index=False)
    leave_one_out_df.to_csv(RESULTS_DIR / "benchmark_repeat_leave_one_out.csv", index=False)

    print(RESULTS_DIR / "benchmark_repeat_run_metrics.csv")
    print(RESULTS_DIR / "benchmark_repeat_avg_prediction_metrics.csv")
    print(RESULTS_DIR / "benchmark_repeat_summary.csv")
    print(RESULTS_DIR / "benchmark_repeat_question_sd.csv")
    print(RESULTS_DIR / "benchmark_repeat_question_sd_summary.csv")
    print(RESULTS_DIR / "benchmark_repeat_leave_one_out.csv")


if __name__ == "__main__":
    main()
