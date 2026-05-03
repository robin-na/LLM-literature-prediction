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
    compute_metrics,
    load_learning_treatment_mean,
    load_truth,
)


ROOT = ANALYSIS_ROOT.parent
RESULTS_DIR = ROOT / "results" / "validation" / "literature_collection_analysis_reports_repeat5_variance_components"
MODEL_ORDER = ["GPT-4.1", "GPT-4.1 Mini", "GPT-5.1", "GPT-5 Mini", "GPT-5 Nano"]
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
            for repeat_idx, row_id in enumerate(ids, start=1):
                pred = pd.to_numeric(source_df.loc[row_id], errors="coerce").reindex(Q_COLS)
                rows.append(
                    {
                        "model": model,
                        "condition": condition,
                        "repeat": repeat_idx,
                        "row_id": row_id,
                        **compute_metrics(pred, treatment, control, learning_mean),
                    }
                )

    out = pd.DataFrame(rows)
    out["model"] = pd.Categorical(out["model"], categories=MODEL_ORDER, ordered=True)
    out["condition"] = pd.Categorical(out["condition"], categories=CONDITION_ORDER, ordered=True)
    return out.sort_values(["condition", "model", "repeat"]).reset_index(drop=True)


def build_condition_summary(repeat_rows: pd.DataFrame) -> pd.DataFrame:
    out_rows: list[dict[str, object]] = []

    for condition, part in repeat_rows.groupby("condition", observed=True):
        for metric in METRICS:
            values = part[metric].to_numpy(dtype=float)
            grand_mean = float(values.mean())
            model_means = part.groupby("model", observed=True)[metric].mean()

            ss_between = float(
                sum(
                    int((part["model"] == model).sum()) * float((model_mean - grand_mean) ** 2)
                    for model, model_mean in model_means.items()
                )
            )
            merged = part.merge(model_means.rename("model_mean"), on="model", how="left")
            ss_within = float(((merged[metric] - merged["model_mean"]) ** 2).sum())
            eta_model = float(ss_between / (ss_between + ss_within)) if (ss_between + ss_within) > 0 else float("nan")

            same_abs: list[float] = []
            diff_abs: list[float] = []
            same_sq: list[float] = []
            diff_sq: list[float] = []
            records = part.loc[:, ["model", "repeat", metric]].to_dict("records")
            for left, right in combinations(records, 2):
                delta = float(left[metric] - right[metric])
                abs_delta = abs(delta)
                sq_delta = delta**2
                if str(left["model"]) == str(right["model"]):
                    same_abs.append(abs_delta)
                    same_sq.append(sq_delta)
                else:
                    diff_abs.append(abs_delta)
                    diff_sq.append(sq_delta)

            mean_sq_same = float(np.mean(same_sq))
            mean_sq_diff = float(np.mean(diff_sq))
            sigma_repeat_sq = float(mean_sq_same / 2.0)
            sigma_model_sq = float(max((mean_sq_diff - mean_sq_same) / 2.0, 0.0))
            icc_pairwise = (
                float(sigma_model_sq / (sigma_model_sq + sigma_repeat_sq))
                if (sigma_model_sq + sigma_repeat_sq) > 0
                else float("nan")
            )

            out_rows.append(
                {
                    "condition": condition,
                    "metric": metric,
                    "n_models": int(part["model"].nunique()),
                    "n_runs": int(len(part)),
                    "between_sd_model_means": float(model_means.std(ddof=0)),
                    "mean_within_model_sd": float(part.groupby("model", observed=True)[metric].std(ddof=0).mean()),
                    "ss_between": ss_between,
                    "ss_within": ss_within,
                    "eta_model": eta_model,
                    "mean_abs_diff_same_model": float(np.mean(same_abs)),
                    "mean_abs_diff_different_model": float(np.mean(diff_abs)),
                    "mean_sq_diff_same_model": mean_sq_same,
                    "mean_sq_diff_different_model": mean_sq_diff,
                    "sigma_model_sq_pairwise": sigma_model_sq,
                    "sigma_repeat_sq_pairwise": sigma_repeat_sq,
                    "icc_pairwise": icc_pairwise,
                }
            )

    return pd.DataFrame(out_rows)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    repeat_rows = load_repeat_rows()
    condition_summary = build_condition_summary(repeat_rows)

    repeat_rows.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_variance_components_repeat_rows.csv",
        index=False,
    )
    condition_summary.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_variance_components_condition_summary.csv",
        index=False,
    )


if __name__ == "__main__":
    main()
