from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.append(str(Path(__file__).resolve().parent))
from jsonl_parser import jsonl_to_dataframe  # noqa: E402


def load_ground_truth(
    csv_path: Path,
    question_prefix: str = "Q",
    label_mode: str = "config_id",
) -> tuple[pd.Series, pd.Series]:
    df = pd.read_csv(csv_path)
    cols = ["CONFIG_configId", "treatment_itt_efficiency", "control_itt_efficiency"]
    missing = [c for c in cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in ground truth: {missing}")

    df = df[cols].copy()
    # If duplicates exist for a config id, average them to get the mean outcome.
    df = (
        df.groupby("CONFIG_configId", as_index=False)
        .mean(numeric_only=True)
        .sort_values("CONFIG_configId")
    )

    if label_mode == "config_id":
        df["question"] = df["CONFIG_configId"].astype(int).map(
            lambda x: f"{question_prefix}{x + 1}"
        )
    elif label_mode == "ordinal":
        df = df.reset_index(drop=True)
        df["question"] = [f"{question_prefix}{i}" for i in range(1, len(df) + 1)]
    else:
        raise ValueError("label_mode must be one of: config_id, ordinal")
    df["treatment_scaled"] = df["treatment_itt_efficiency"] * 100
    df["control_scaled"] = df["control_itt_efficiency"] * 100

    treatment = df.set_index("question")["treatment_scaled"]
    control = df.set_index("question")["control_scaled"]
    return treatment, control


def _rmse_np(pred: np.ndarray, truth: np.ndarray) -> float:
    if pred.size == 0:
        return float("nan")
    diff = pred - truth
    return float(np.sqrt(np.mean(diff**2)))


def _corr_np(pred: np.ndarray, truth: np.ndarray) -> float:
    if pred.size < 2:
        return float("nan")
    if np.std(pred) == 0 or np.std(truth) == 0:
        return float("nan")
    return float(np.corrcoef(pred, truth)[0, 1])


def _directional_accuracy_np(
    pred: np.ndarray, truth: np.ndarray, control: np.ndarray
) -> float:
    if pred.size == 0:
        return float("nan")
    true_dir = np.sign(truth - control)
    pred_dir = np.sign(pred - control)
    return float(np.mean(true_dir == pred_dir))


def _metric_with_ci(
    metric_fn,
    pred_arr: np.ndarray,
    truth_arr: np.ndarray,
    control_arr: np.ndarray | None,
    mask: np.ndarray,
    rng: np.random.Generator,
    n_boot: int,
) -> tuple[float, float, float]:
    if mask.sum() == 0:
        return float("nan"), float("nan"), float("nan")

    pred = pred_arr[mask]
    truth = truth_arr[mask]
    if control_arr is None:
        value = metric_fn(pred, truth)
    else:
        control = control_arr[mask]
        value = metric_fn(pred, truth, control)

    if n_boot <= 0:
        return value, float("nan"), float("nan")

    idx = np.flatnonzero(mask)
    boot = np.empty(n_boot, dtype=float)
    for i in range(n_boot):
        sample = rng.choice(idx, size=idx.size, replace=True)
        if control_arr is None:
            boot[i] = metric_fn(pred_arr[sample], truth_arr[sample])
        else:
            boot[i] = metric_fn(
                pred_arr[sample], truth_arr[sample], control_arr[sample]
            )
    finite_boot = boot[np.isfinite(boot)]
    if finite_boot.size == 0:
        return value, float("nan"), float("nan")
    lo, hi = np.nanpercentile(finite_boot, [2.5, 97.5])
    return value, float(lo), float(hi)


def _paired_delta_ci(
    metric_fn,
    pred_arr: np.ndarray,
    base_arr: np.ndarray,
    truth_arr: np.ndarray,
    control_arr: np.ndarray | None,
    mask: np.ndarray,
    rng: np.random.Generator,
    n_boot: int,
) -> tuple[float, float, float]:
    if mask.sum() == 0:
        return float("nan"), float("nan"), float("nan")

    idx = np.flatnonzero(mask)
    if control_arr is None:
        pred_val = metric_fn(pred_arr[idx], truth_arr[idx])
        base_val = metric_fn(base_arr[idx], truth_arr[idx])
    else:
        pred_val = metric_fn(pred_arr[idx], truth_arr[idx], control_arr[idx])
        base_val = metric_fn(base_arr[idx], truth_arr[idx], control_arr[idx])
    delta = float(pred_val - base_val)

    if n_boot <= 0:
        return delta, float("nan"), float("nan")

    boot = np.empty(n_boot, dtype=float)
    for i in range(n_boot):
        sample = rng.choice(idx, size=idx.size, replace=True)
        if control_arr is None:
            m_pred = metric_fn(pred_arr[sample], truth_arr[sample])
            m_base = metric_fn(base_arr[sample], truth_arr[sample])
        else:
            m_pred = metric_fn(
                pred_arr[sample], truth_arr[sample], control_arr[sample]
            )
            m_base = metric_fn(
                base_arr[sample], truth_arr[sample], control_arr[sample]
            )
        boot[i] = m_pred - m_base
    finite_boot = boot[np.isfinite(boot)]
    if finite_boot.size == 0:
        return delta, float("nan"), float("nan")
    lo, hi = np.nanpercentile(finite_boot, [2.5, 97.5])
    return delta, float(lo), float(hi)


def compute_metrics(
    pred_df: pd.DataFrame,
    treatment: pd.Series,
    control: pd.Series,
    rng: np.random.Generator,
    n_boot: int,
) -> pd.DataFrame:
    questions = list(treatment.index)
    pred_df = pred_df.reindex(columns=questions)

    records = []
    for variation, row in pred_df.iterrows():
        pred = pd.to_numeric(row, errors="coerce").reindex(questions)
        truth = treatment.reindex(pred.index)
        ctrl = control.reindex(pred.index)

        pred_arr = pred.to_numpy(dtype=float)
        truth_arr = truth.to_numpy(dtype=float)
        ctrl_arr = ctrl.to_numpy(dtype=float)

        rmse_mask = ~np.isnan(pred_arr) & ~np.isnan(truth_arr)
        corr_mask = rmse_mask.copy()
        dir_mask = rmse_mask & ~np.isnan(ctrl_arr)

        rmse, rmse_lo, rmse_hi = _metric_with_ci(
            _rmse_np, pred_arr, truth_arr, None, rmse_mask, rng, n_boot
        )
        corr, corr_lo, corr_hi = _metric_with_ci(
            _corr_np, pred_arr, truth_arr, None, corr_mask, rng, n_boot
        )
        dir_acc, dir_lo, dir_hi = _metric_with_ci(
            _directional_accuracy_np,
            pred_arr,
            truth_arr,
            ctrl_arr,
            dir_mask,
            rng,
            n_boot,
        )

        records.append(
            {
                "variation": variation,
                "rmse": rmse,
                "rmse_ci_low": rmse_lo,
                "rmse_ci_high": rmse_hi,
                "correlation": corr,
                "correlation_ci_low": corr_lo,
                "correlation_ci_high": corr_hi,
                "directional_accuracy": dir_acc,
                "directional_accuracy_ci_low": dir_lo,
                "directional_accuracy_ci_high": dir_hi,
                "n": int(rmse_mask.sum()),
            }
        )

    return pd.DataFrame.from_records(records).set_index("variation")


def compute_delta_metrics(
    pred_df: pd.DataFrame,
    baseline_row: pd.Series,
    treatment: pd.Series,
    control: pd.Series,
    rng: np.random.Generator,
    n_boot: int,
) -> pd.DataFrame:
    questions = list(treatment.index)
    pred_df = pred_df.reindex(columns=questions)
    baseline = pd.to_numeric(baseline_row, errors="coerce").reindex(questions)

    baseline_arr = baseline.to_numpy(dtype=float)
    truth_arr = treatment.reindex(questions).to_numpy(dtype=float)
    ctrl_arr = control.reindex(questions).to_numpy(dtype=float)

    records = []
    for variation, row in pred_df.iterrows():
        pred = pd.to_numeric(row, errors="coerce").reindex(questions)
        pred_arr = pred.to_numpy(dtype=float)

        rmse_mask = (
            ~np.isnan(pred_arr) & ~np.isnan(baseline_arr) & ~np.isnan(truth_arr)
        )
        corr_mask = rmse_mask.copy()
        dir_mask = rmse_mask & ~np.isnan(ctrl_arr)

        delta_rmse, delta_rmse_lo, delta_rmse_hi = _paired_delta_ci(
            _rmse_np,
            pred_arr,
            baseline_arr,
            truth_arr,
            None,
            rmse_mask,
            rng,
            n_boot,
        )
        delta_corr, delta_corr_lo, delta_corr_hi = _paired_delta_ci(
            _corr_np,
            pred_arr,
            baseline_arr,
            truth_arr,
            None,
            corr_mask,
            rng,
            n_boot,
        )
        delta_dir, delta_dir_lo, delta_dir_hi = _paired_delta_ci(
            _directional_accuracy_np,
            pred_arr,
            baseline_arr,
            truth_arr,
            ctrl_arr,
            dir_mask,
            rng,
            n_boot,
        )

        records.append(
            {
                "variation": variation,
                "delta_rmse": delta_rmse,
                "delta_rmse_ci_low": delta_rmse_lo,
                "delta_rmse_ci_high": delta_rmse_hi,
                "delta_correlation": delta_corr,
                "delta_correlation_ci_low": delta_corr_lo,
                "delta_correlation_ci_high": delta_corr_hi,
                "delta_directional_accuracy": delta_dir,
                "delta_directional_accuracy_ci_low": delta_dir_lo,
                "delta_directional_accuracy_ci_high": delta_dir_hi,
                "n": int(rmse_mask.sum()),
            }
        )

    return pd.DataFrame.from_records(records).set_index("variation")


def process_jsonl(
    jsonl_path: Path,
    results_dir: Path,
    treatment: pd.Series,
    control: pd.Series,
    baseline_row: pd.Series,
    rng: np.random.Generator,
    n_boot: int,
    platform: str,
) -> tuple[Path, Path, Path]:
    pred_df = jsonl_to_dataframe(jsonl_path, platform=platform)

    results_dir.mkdir(parents=True, exist_ok=True)
    pred_csv = results_dir / f"{jsonl_path.stem}.csv"
    pred_df.to_csv(pred_csv, index=True)

    metrics_df = compute_metrics(pred_df, treatment, control, rng, n_boot)
    metrics_csv = results_dir / f"{jsonl_path.stem}_metrics.csv"
    metrics_df.to_csv(metrics_csv, index=True)

    delta_df = compute_delta_metrics(
        pred_df, baseline_row, treatment, control, rng, n_boot
    )
    delta_csv = results_dir / f"{jsonl_path.stem}_metrics_delta.csv"
    delta_df.to_csv(delta_csv, index=True)

    return pred_csv, metrics_csv, delta_csv


def find_prediction_jsonls(input_dir: Path) -> list[Path]:
    if not input_dir.exists():
        return []
    return sorted(
        [p for p in input_dir.iterdir() if p.is_file() and p.name.startswith("prediction") and p.suffix == ".jsonl"]
    )


def _load_baseline(
    input_dir: Path, results_dir: Path, baseline_jsonl: Path | None, platform: str
) -> pd.Series:
    if baseline_jsonl is None:
        baseline_jsonl = input_dir / "prediction_baseline_41.jsonl"
    if baseline_jsonl.exists():
        baseline_df = jsonl_to_dataframe(baseline_jsonl, platform=platform)
    else:
        baseline_csv = results_dir / "prediction_baseline_41.csv"
        if not baseline_csv.exists():
            raise FileNotFoundError(
                "Baseline predictions not found. Expected "
                f"{baseline_jsonl} or {baseline_csv}."
            )
        baseline_df = pd.read_csv(baseline_csv, index_col=0)

    if "baseline" in baseline_df.index:
        return baseline_df.loc["baseline"]
    return baseline_df.iloc[0]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert prediction jsonl files to CSV and compute metrics."
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=Path("openAI_batch_output"),
        help="Directory containing prediction*.jsonl files.",
    )
    parser.add_argument(
        "--results-dir",
        type=Path,
        default=Path("results"),
        help="Directory to write CSV outputs.",
    )
    parser.add_argument(
        "--ground-truth",
        type=Path,
        default=Path("science-data_and_code/data/processed_data/df_paired_val.csv"),
        help="Path to ground-truth CSV.",
    )
    parser.add_argument(
        "--bootstrap-samples",
        type=int,
        default=1000,
        help="Number of bootstrap samples for confidence intervals.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=7,
        help="Random seed for bootstrapping.",
    )
    parser.add_argument(
        "--baseline-jsonl",
        type=Path,
        default=None,
        help="Optional path to baseline prediction jsonl.",
    )
    parser.add_argument(
        "--platform",
        choices=["openai", "claude"],
        default="openai",
        help="Platform-specific jsonl parser.",
    )
    args = parser.parse_args()

    treatment, control = load_ground_truth(args.ground_truth)
    baseline_row = _load_baseline(
        args.input_dir, args.results_dir, args.baseline_jsonl, args.platform
    )
    rng = np.random.default_rng(args.seed)

    jsonl_files = find_prediction_jsonls(args.input_dir)
    if not jsonl_files:
        raise SystemExit(f"No prediction jsonl files found in {args.input_dir}")

    for jsonl_path in jsonl_files:
        pred_csv, metrics_csv, delta_csv = process_jsonl(
            jsonl_path,
            args.results_dir,
            treatment,
            control,
            baseline_row,
            rng,
            args.bootstrap_samples,
            args.platform,
        )
        print(f"Wrote {pred_csv}, {metrics_csv}, {delta_csv}")


if __name__ == "__main__":
    main()
