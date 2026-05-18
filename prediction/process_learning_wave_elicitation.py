from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(REPO_ROOT / "analysis"))

from jsonl_parser import jsonl_to_dataframe  # noqa: E402
from prediction_metrics import (  # noqa: E402
    _corr_np,
    _directional_accuracy_np,
    _paired_delta_ci,
    _rmse_np,
    compute_delta_metrics,
    compute_metrics,
    load_ground_truth,
)


JSONL_PATH = REPO_ROOT / "openAI_batch_output" / "prediction_learning_wave_elicitation_41.jsonl"
LEARN_GT = REPO_ROOT / "science-data_and_code" / "data" / "processed_data" / "df_paired_learn.csv"
VAL_GT = REPO_ROOT / "science-data_and_code" / "data" / "processed_data" / "df_paired_val.csv"
VAL_PRED = REPO_ROOT / "results" / "prediction_positive_case_variations_41.csv"
VAL_METRICS = REPO_ROOT / "results" / "prediction_positive_case_variations_41_metrics.csv"
RESULTS_DIR = REPO_ROOT / "results"

TARGET_VARIATIONS = [
    "baseline",
    "baseline_reasoning",
    "baseline_joint",
    "baseline_joint_reasoning",
]


def paired_compare(
    pred_df: pd.DataFrame,
    treatment: pd.Series,
    control: pd.Series,
    pred_name: str,
    base_name: str,
    seed: int = 42,
    n_boot: int = 10000,
) -> dict[str, float | str | int]:
    questions = list(treatment.index)
    pred_arr = pd.to_numeric(pred_df.loc[pred_name], errors="coerce").reindex(questions).to_numpy(float)
    base_arr = pd.to_numeric(pred_df.loc[base_name], errors="coerce").reindex(questions).to_numpy(float)
    truth_arr = treatment.reindex(questions).to_numpy(float)
    ctrl_arr = control.reindex(questions).to_numpy(float)

    rmse_mask = ~np.isnan(pred_arr) & ~np.isnan(base_arr) & ~np.isnan(truth_arr)
    corr_mask = rmse_mask.copy()
    dir_mask = rmse_mask & ~np.isnan(ctrl_arr)

    def verdict(lo: float, hi: float, higher_is_better: bool) -> str:
        if higher_is_better:
            if lo > 0:
                return "better"
            if hi < 0:
                return "worse"
            return "uncertain"
        if hi < 0:
            return "better"
        if lo > 0:
            return "worse"
        return "uncertain"

    rng = np.random.default_rng(seed)
    d_rmse = _paired_delta_ci(_rmse_np, pred_arr, base_arr, truth_arr, None, rmse_mask, rng, n_boot)
    rng = np.random.default_rng(seed)
    d_corr = _paired_delta_ci(_corr_np, pred_arr, base_arr, truth_arr, None, corr_mask, rng, n_boot)
    rng = np.random.default_rng(seed)
    d_dir = _paired_delta_ci(
        _directional_accuracy_np,
        pred_arr,
        base_arr,
        truth_arr,
        ctrl_arr,
        dir_mask,
        rng,
        n_boot,
    )

    return {
        "comparison": f"{pred_name}_minus_{base_name}",
        "delta_rmse": d_rmse[0],
        "delta_rmse_ci_low": d_rmse[1],
        "delta_rmse_ci_high": d_rmse[2],
        "rmse_verdict": verdict(d_rmse[1], d_rmse[2], higher_is_better=False),
        "delta_correlation": d_corr[0],
        "delta_correlation_ci_low": d_corr[1],
        "delta_correlation_ci_high": d_corr[2],
        "correlation_verdict": verdict(d_corr[1], d_corr[2], higher_is_better=True),
        "delta_directional_accuracy": d_dir[0],
        "delta_directional_accuracy_ci_low": d_dir[1],
        "delta_directional_accuracy_ci_high": d_dir[2],
        "directional_accuracy_verdict": verdict(d_dir[1], d_dir[2], higher_is_better=True),
        "n": int(rmse_mask.sum()),
    }


def missing_summary(pred_df: pd.DataFrame, expected_questions: list[str]) -> pd.DataFrame:
    records: list[dict[str, object]] = []
    for variation in TARGET_VARIATIONS:
        if variation not in pred_df.index:
            records.append(
                {
                    "variation": variation,
                    "present": False,
                    "n_expected": len(expected_questions),
                    "n_present": 0,
                    "n_missing": len(expected_questions),
                    "missing_labels": ",".join(expected_questions),
                }
            )
            continue
        row = pd.to_numeric(pred_df.loc[variation], errors="coerce").reindex(expected_questions)
        missing = [q for q in expected_questions if pd.isna(row[q])]
        records.append(
            {
                "variation": variation,
                "present": True,
                "n_expected": len(expected_questions),
                "n_present": int(row.notna().sum()),
                "n_missing": len(missing),
                "missing_labels": ",".join(missing),
            }
        )
    return pd.DataFrame.from_records(records)


def dispersion_summary(
    pred_df: pd.DataFrame,
    treatment: pd.Series,
    dataset: str,
) -> pd.DataFrame:
    questions = list(treatment.index)
    truth = treatment.reindex(questions)
    records: list[dict[str, float | str | int]] = []
    for variation in TARGET_VARIATIONS:
        if variation not in pred_df.index:
            continue
        pred = pd.to_numeric(pred_df.loc[variation], errors="coerce").reindex(questions)
        mask = pred.notna() & truth.notna()
        err = pred[mask] - truth[mask]
        abs_err = err.abs()
        sq_err = err**2
        records.append(
            {
                "dataset": dataset,
                "variation": variation,
                "n": int(mask.sum()),
                "residual_std": float(err.std(ddof=1)) if mask.sum() > 1 else float("nan"),
                "absolute_error_mean": float(abs_err.mean()),
                "absolute_error_std": float(abs_err.std(ddof=1)) if mask.sum() > 1 else float("nan"),
                "squared_error_mean": float(sq_err.mean()),
                "squared_error_std": float(sq_err.std(ddof=1)) if mask.sum() > 1 else float("nan"),
            }
        )
    return pd.DataFrame.from_records(records)


def add_metric_ranks(metrics_df: pd.DataFrame, dataset: str) -> pd.DataFrame:
    subset = metrics_df.loc[metrics_df.index.intersection(TARGET_VARIATIONS)].copy()
    subset["dataset"] = dataset
    subset["rmse_rank"] = subset["rmse"].rank(method="min", ascending=True)
    subset["correlation_rank"] = subset["correlation"].rank(method="min", ascending=False)
    subset["directional_accuracy_rank"] = subset["directional_accuracy"].rank(method="min", ascending=False)
    subset["rank_mean"] = subset[
        ["rmse_rank", "correlation_rank", "directional_accuracy_rank"]
    ].mean(axis=1)
    subset["rmse_ci_width"] = subset["rmse_ci_high"] - subset["rmse_ci_low"]
    subset["correlation_ci_width"] = subset["correlation_ci_high"] - subset["correlation_ci_low"]
    subset["directional_accuracy_ci_width"] = (
        subset["directional_accuracy_ci_high"] - subset["directional_accuracy_ci_low"]
    )
    return subset.reset_index().rename(columns={"index": "variation"})


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    pred_df = jsonl_to_dataframe(JSONL_PATH, platform="openai")
    learn_treatment, learn_control = load_ground_truth(
        LEARN_GT, question_prefix="L", label_mode="ordinal"
    )
    learn_questions = list(learn_treatment.index)
    pred_df = pred_df.reindex(columns=learn_questions)

    pred_csv = RESULTS_DIR / f"{JSONL_PATH.stem}.csv"
    pred_df.to_csv(pred_csv)

    metrics_df = compute_metrics(
        pred_df,
        learn_treatment,
        learn_control,
        rng=np.random.default_rng(42),
        n_boot=10000,
    )
    metrics_csv = RESULTS_DIR / f"{JSONL_PATH.stem}_metrics.csv"
    metrics_df.to_csv(metrics_csv)

    if "baseline" not in pred_df.index:
        raise SystemExit("Expected a 'baseline' row in learning-wave predictions.")

    delta_df = compute_delta_metrics(
        pred_df,
        pred_df.loc["baseline"],
        learn_treatment,
        learn_control,
        rng=np.random.default_rng(42),
        n_boot=10000,
    )
    delta_csv = RESULTS_DIR / f"{JSONL_PATH.stem}_metrics_delta.csv"
    delta_df.to_csv(delta_csv)

    missing_df = missing_summary(pred_df, learn_questions)
    missing_csv = RESULTS_DIR / f"{JSONL_PATH.stem}_missing_summary.csv"
    missing_df.to_csv(missing_csv, index=False)

    pairwise_comparisons = [
        paired_compare(pred_df, learn_treatment, learn_control, "baseline_reasoning", "baseline"),
        paired_compare(pred_df, learn_treatment, learn_control, "baseline_joint", "baseline"),
        paired_compare(pred_df, learn_treatment, learn_control, "baseline_joint_reasoning", "baseline_joint"),
        paired_compare(pred_df, learn_treatment, learn_control, "baseline_joint_reasoning", "baseline_reasoning"),
        paired_compare(pred_df, learn_treatment, learn_control, "baseline_joint_reasoning", "baseline"),
    ]
    pairwise_df = pd.DataFrame.from_records(pairwise_comparisons)
    pairwise_csv = RESULTS_DIR / f"{JSONL_PATH.stem}_elicitation_pairwise.csv"
    pairwise_df.to_csv(pairwise_csv, index=False)

    val_pred_df = pd.read_csv(VAL_PRED, index_col=0)
    val_treatment, val_control = load_ground_truth(VAL_GT, question_prefix="Q")
    val_metrics_df = pd.read_csv(VAL_METRICS, index_col=0)

    compare_df = pd.concat(
        [
            add_metric_ranks(metrics_df, dataset="learning_wave"),
            add_metric_ranks(val_metrics_df, dataset="validation_20"),
        ],
        ignore_index=True,
    )
    compare_csv = RESULTS_DIR / f"{JSONL_PATH.stem}_vs_validation_summary.csv"
    compare_df.to_csv(compare_csv, index=False)

    dispersion_df = pd.concat(
        [
            dispersion_summary(pred_df, learn_treatment, dataset="learning_wave"),
            dispersion_summary(val_pred_df, val_treatment, dataset="validation_20"),
        ],
        ignore_index=True,
    )
    dispersion_csv = RESULTS_DIR / f"{JSONL_PATH.stem}_vs_validation_error_dispersion.csv"
    dispersion_df.to_csv(dispersion_csv, index=False)

    val_pairwise_df = pd.DataFrame.from_records(
        [
            paired_compare(val_pred_df, val_treatment, val_control, "baseline_reasoning", "baseline"),
            paired_compare(val_pred_df, val_treatment, val_control, "baseline_joint", "baseline"),
            paired_compare(val_pred_df, val_treatment, val_control, "baseline_joint_reasoning", "baseline_joint"),
            paired_compare(val_pred_df, val_treatment, val_control, "baseline_joint_reasoning", "baseline_reasoning"),
            paired_compare(val_pred_df, val_treatment, val_control, "baseline_joint_reasoning", "baseline"),
        ]
    )
    val_pairwise_df.insert(0, "dataset", "validation_20")
    pairwise_df.insert(0, "dataset", "learning_wave")
    pairwise_both_df = pd.concat([pairwise_df, val_pairwise_df], ignore_index=True)
    pairwise_both_csv = RESULTS_DIR / f"{JSONL_PATH.stem}_elicitation_pairwise_vs_validation.csv"
    pairwise_both_df.to_csv(pairwise_both_csv, index=False)

    print(f"Wrote {pred_csv}")
    print(f"Wrote {metrics_csv}")
    print(f"Wrote {delta_csv}")
    print(f"Wrote {missing_csv}")
    print(f"Wrote {pairwise_csv}")
    print(f"Wrote {compare_csv}")
    print(f"Wrote {dispersion_csv}")
    print(f"Wrote {pairwise_both_csv}")


if __name__ == "__main__":
    main()
