from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.append(str(Path(__file__).resolve().parent))
from jsonl_parser import jsonl_to_dataframe  # noqa: E402


def load_ground_truth(csv_path: Path) -> tuple[pd.Series, pd.Series]:
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

    df["question"] = df["CONFIG_configId"].astype(int).map(lambda x: f"Q{x + 1}")
    df["treatment_scaled"] = df["treatment_itt_efficiency"] * 100
    df["control_scaled"] = df["control_itt_efficiency"] * 100

    treatment = df.set_index("question")["treatment_scaled"]
    control = df.set_index("question")["control_scaled"]
    return treatment, control


def _rmse(pred: pd.Series, truth: pd.Series) -> float:
    mask = pred.notna() & truth.notna()
    if mask.sum() == 0:
        return float("nan")
    diff = pred[mask] - truth[mask]
    return float(np.sqrt(np.mean(diff**2)))


def _corr(pred: pd.Series, truth: pd.Series) -> float:
    mask = pred.notna() & truth.notna()
    if mask.sum() < 2:
        return float("nan")
    return float(pred[mask].corr(truth[mask]))


def _directional_accuracy(
    pred: pd.Series, truth: pd.Series, control: pd.Series
) -> float:
    mask = pred.notna() & truth.notna() & control.notna()
    if mask.sum() == 0:
        return float("nan")
    true_dir = np.sign(truth[mask] - control[mask])
    pred_dir = np.sign(pred[mask] - control[mask])
    return float((true_dir == pred_dir).mean())


def compute_metrics(
    pred_df: pd.DataFrame, treatment: pd.Series, control: pd.Series
) -> pd.DataFrame:
    questions = list(treatment.index)
    pred_df = pred_df.reindex(columns=questions)

    records = []
    for variation, row in pred_df.iterrows():
        pred = pd.to_numeric(row, errors="coerce")
        truth = treatment.reindex(pred.index)
        ctrl = control.reindex(pred.index)

        records.append(
            {
                "variation": variation,
                "rmse": _rmse(pred, truth),
                "correlation": _corr(pred, truth),
                "directional_accuracy": _directional_accuracy(pred, truth, ctrl),
                "n": int((pred.notna() & truth.notna()).sum()),
            }
        )

    return pd.DataFrame.from_records(records).set_index("variation")


def process_jsonl(
    jsonl_path: Path,
    results_dir: Path,
    treatment: pd.Series,
    control: pd.Series,
) -> tuple[Path, Path]:
    pred_df = jsonl_to_dataframe(jsonl_path)

    results_dir.mkdir(parents=True, exist_ok=True)
    pred_csv = results_dir / f"{jsonl_path.stem}.csv"
    pred_df.to_csv(pred_csv, index=True)

    metrics_df = compute_metrics(pred_df, treatment, control)
    metrics_csv = results_dir / f"{jsonl_path.stem}_metrics.csv"
    metrics_df.to_csv(metrics_csv, index=True)

    return pred_csv, metrics_csv


def find_prediction_jsonls(input_dir: Path) -> list[Path]:
    if not input_dir.exists():
        return []
    return sorted(
        [p for p in input_dir.iterdir() if p.is_file() and p.name.startswith("prediction") and p.suffix == ".jsonl"]
    )


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
    args = parser.parse_args()

    treatment, control = load_ground_truth(args.ground_truth)

    jsonl_files = find_prediction_jsonls(args.input_dir)
    if not jsonl_files:
        raise SystemExit(f"No prediction jsonl files found in {args.input_dir}")

    for jsonl_path in jsonl_files:
        pred_csv, metrics_csv = process_jsonl(
            jsonl_path, args.results_dir, treatment, control
        )
        print(f"Wrote {pred_csv} and {metrics_csv}")


if __name__ == "__main__":
    main()
