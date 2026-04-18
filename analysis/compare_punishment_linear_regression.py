from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


NR_TOKENS = {"", "nan", "n/r", "not reported", "none"}
PUNISHMENT_DEPENDENT_CONFIGS = [
    "CONFIG_showPunishmentId",
    "CONFIG_punishmentCost",
    "CONFIG_punishmentTech",
]


@dataclass
class TrainedModel:
    model: Pipeline
    numeric_cols: list[str]
    categorical_cols: list[str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Compare linear regressions for treatment efficiency prediction "
            "using (1) paired batch extractions and (2) science learning data."
        )
    )
    parser.add_argument(
        "--batch-table",
        type=Path,
        default=Path("batch_processing/output_xlsx/agentic_extraction_7papers_rawmd.xlsx"),
    )
    parser.add_argument(
        "--learn-csv",
        type=Path,
        default=Path("science-data_and_code/data/processed_data/df_paired_learn.csv"),
    )
    parser.add_argument(
        "--val-csv",
        type=Path,
        default=Path("science-data_and_code/data/processed_data/df_paired_val.csv"),
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("results/punishment_regression_comparison"),
    )
    return parser.parse_args()


def load_table(path: Path, *, sheet_name: str | int | None = None) -> pd.DataFrame:
    if path.suffix.lower() in {".xlsx", ".xls"}:
        return pd.read_excel(path, sheet_name=sheet_name or "extractions")
    return pd.read_csv(path)


def is_config_column(col: str) -> bool:
    return col.startswith("CONFIG_")


def batch_config_columns(df: pd.DataFrame) -> list[str]:
    cols = []
    for col in df.columns:
        if not is_config_column(col):
            continue
        if col.endswith("_reason") or col.endswith("_confidence"):
            continue
        if col == "CONFIG_endowment":
            continue
        cols.append(col)
    return cols


def science_config_columns(df: pd.DataFrame) -> list[str]:
    return [c for c in df.columns if is_config_column(c) and c != "CONFIG_endowment"]


def pick_non_missing_mode(series: pd.Series) -> str | float:
    values = []
    for raw in series:
        if pd.isna(raw):
            continue
        val = str(raw).strip()
        if val.lower() in NR_TOKENS:
            continue
        values.append(val)
    if not values:
        return np.nan
    return pd.Series(values).value_counts().index[0]


def pair_batch_rows(
    batch_df: pd.DataFrame,
    common_cfg: list[str],
) -> tuple[pd.DataFrame, int]:
    work = batch_df.copy()
    work = work[work["METHOD_lab"].astype(str).str.lower() == "true"].copy()
    work["pun_exists"] = pd.to_numeric(work["CONFIG_punishmentExists"], errors="coerce")
    work["efficiency"] = pd.to_numeric(work["DV_efficiency"], errors="coerce")
    work = work[work["pun_exists"].isin([0.0, 1.0])].copy()

    pair_key = [c for c in common_cfg if c not in PUNISHMENT_DEPENDENT_CONFIGS]
    for col in pair_key:
        work[col] = work[col].astype(str).str.strip()

    raw_pairable_groups = 0
    records = []
    for key_vals, group in work.groupby(pair_key, dropna=False):
        has_control = (group["pun_exists"] == 0.0).any()
        has_treatment = (group["pun_exists"] == 1.0).any()
        if not (has_control and has_treatment):
            continue
        raw_pairable_groups += 1

        control = group[(group["pun_exists"] == 0.0)].copy()
        treatment = group[(group["pun_exists"] == 1.0)].copy()
        control = control[(control["efficiency"] >= 0) & (control["efficiency"] <= 1)]
        treatment = treatment[(treatment["efficiency"] >= 0) & (treatment["efficiency"] <= 1)]
        if control.empty or treatment.empty:
            continue

        record: dict[str, object] = {}
        if len(pair_key) == 1:
            record[pair_key[0]] = key_vals
        else:
            record.update(dict(zip(pair_key, key_vals)))
        for col in PUNISHMENT_DEPENDENT_CONFIGS:
            if col in common_cfg:
                record[col] = pick_non_missing_mode(treatment[col])
        record["control_efficiency"] = float(control["efficiency"].mean())
        record["treatment_efficiency"] = float(treatment["efficiency"].mean())
        record["n_control_rows"] = int(len(control))
        record["n_treatment_rows"] = int(len(treatment))
        records.append(record)

    paired = pd.DataFrame(records)
    return paired, raw_pairable_groups


def prep_science_df(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["control_efficiency"] = pd.to_numeric(out["control_itt_efficiency"], errors="coerce")
    out["treatment_efficiency"] = pd.to_numeric(
        out["treatment_itt_efficiency"], errors="coerce"
    )
    out = out.dropna(subset=["control_efficiency", "treatment_efficiency"])
    out = out[
        (out["control_efficiency"] >= 0)
        & (out["control_efficiency"] <= 1)
        & (out["treatment_efficiency"] >= 0)
        & (out["treatment_efficiency"] <= 1)
    ].copy()
    return out


def split_feature_types(
    df: pd.DataFrame, feature_cols: list[str], numeric_threshold: float = 0.95
) -> tuple[pd.DataFrame, list[str], list[str]]:
    x = df[feature_cols].copy()
    numeric_cols: list[str] = []
    categorical_cols: list[str] = []
    for col in feature_cols:
        numeric = pd.to_numeric(x[col], errors="coerce")
        if numeric.notna().mean() >= numeric_threshold:
            x[col] = numeric
            numeric_cols.append(col)
        else:
            x[col] = x[col].astype(str)
            categorical_cols.append(col)
    return x, numeric_cols, categorical_cols


def train_linear_model(df: pd.DataFrame, feature_cols: list[str]) -> TrainedModel:
    x, numeric_cols, categorical_cols = split_feature_types(df, feature_cols)
    y = df["treatment_efficiency"].to_numpy()

    transformers = []
    if numeric_cols:
        transformers.append(
            (
                "num",
                Pipeline([("imputer", SimpleImputer(strategy="median"))]),
                numeric_cols,
            )
        )
    if categorical_cols:
        transformers.append(
            (
                "cat",
                Pipeline(
                    [
                        ("imputer", SimpleImputer(strategy="most_frequent")),
                        ("onehot", OneHotEncoder(handle_unknown="ignore")),
                    ]
                ),
                categorical_cols,
            )
        )

    model = Pipeline(
        [("preprocess", ColumnTransformer(transformers=transformers)), ("lr", LinearRegression())]
    )
    model.fit(x, y)
    return TrainedModel(model=model, numeric_cols=numeric_cols, categorical_cols=categorical_cols)


def model_predict(
    trained: TrainedModel, df: pd.DataFrame, feature_cols: list[str]
) -> np.ndarray:
    x = df[feature_cols].copy()
    for col in trained.numeric_cols:
        x[col] = pd.to_numeric(x[col], errors="coerce")
    for col in trained.categorical_cols:
        x[col] = x[col].astype(str)
    return trained.model.predict(x)


def evaluate_predictions(
    y_true: np.ndarray, y_pred: np.ndarray, control_efficiency: np.ndarray
) -> dict[str, float]:
    rmse = float(np.sqrt(mean_squared_error(y_true, y_pred)))
    if np.std(y_pred) > 0 and np.std(y_true) > 0:
        corr = float(np.corrcoef(y_true, y_pred)[0, 1])
    else:
        corr = float("nan")
    directional = float(
        np.mean(np.sign(y_pred - control_efficiency) == np.sign(y_true - control_efficiency))
    )
    sse_model = float(np.sum((y_true - y_pred) ** 2))
    sse_baseline = float(np.sum((y_true - control_efficiency) ** 2))
    if sse_baseline > 0:
        r2_vs_control = float(1 - (sse_model / sse_baseline))
    else:
        r2_vs_control = float("nan")
    baseline_rmse = float(np.sqrt(mean_squared_error(y_true, control_efficiency)))
    return {
        "rmse": rmse,
        "corr": corr,
        "directional_accuracy": directional,
        "r2_vs_control_baseline": r2_vs_control,
        "baseline_rmse_control": baseline_rmse,
    }


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    batch_df = load_table(args.batch_table, sheet_name="extractions")
    learn_df = pd.read_csv(args.learn_csv)
    val_df = pd.read_csv(args.val_csv)

    batch_cfg = batch_config_columns(batch_df)
    learn_cfg = science_config_columns(learn_df)
    val_cfg = science_config_columns(val_df)
    common_cfg = sorted(set(batch_cfg) & set(learn_cfg) & set(val_cfg))
    feature_cols = common_cfg + ["control_efficiency"]

    paired_batch, raw_pairable_groups = pair_batch_rows(batch_df, common_cfg)
    paired_batch = paired_batch.dropna(subset=["control_efficiency", "treatment_efficiency"]).copy()
    paired_batch = paired_batch[
        (paired_batch["control_efficiency"] >= 0)
        & (paired_batch["control_efficiency"] <= 1)
        & (paired_batch["treatment_efficiency"] >= 0)
        & (paired_batch["treatment_efficiency"] <= 1)
    ].copy()

    learn_prepped = prep_science_df(learn_df)
    val_prepped = prep_science_df(val_df)

    model_from_batch = train_linear_model(paired_batch, feature_cols)
    model_from_learn = train_linear_model(learn_prepped, feature_cols)

    y_val = val_prepped["treatment_efficiency"].to_numpy()
    control_val = val_prepped["control_efficiency"].to_numpy()

    pred_batch = model_predict(model_from_batch, val_prepped, feature_cols)
    pred_learn = model_predict(model_from_learn, val_prepped, feature_cols)

    metrics_batch = evaluate_predictions(y_val, pred_batch, control_val)
    metrics_learn = evaluate_predictions(y_val, pred_learn, control_val)

    metrics_df = pd.DataFrame(
        [
            {"model": "batch_output_51_paired", **metrics_batch},
            {"model": "science_df_paired_learn", **metrics_learn},
        ]
    )
    metrics_csv = args.output_dir / "model_comparison_metrics.csv"
    metrics_df.to_csv(metrics_csv, index=False)

    val_preds = val_prepped[["CONFIG_configId", "control_efficiency", "treatment_efficiency"]].copy()
    val_preds["pred_from_batch_model"] = pred_batch
    val_preds["pred_from_science_learn_model"] = pred_learn
    val_preds.to_csv(args.output_dir / "validation_predictions.csv", index=False)
    paired_batch.to_csv(args.output_dir / "batch_output_51_paired_dataset.csv", index=False)

    summary = {
        "raw_pairable_groups_in_batch_lab_data": raw_pairable_groups,
        "paired_groups_after_efficiency_filter": int(len(paired_batch)),
        "learn_rows_after_efficiency_filter": int(len(learn_prepped)),
        "validation_rows_after_efficiency_filter": int(len(val_prepped)),
        "feature_columns_used": feature_cols,
        "metrics_csv": str(metrics_csv),
    }
    (args.output_dir / "run_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print("Feature columns used:")
    for col in feature_cols:
        print(f"  - {col}")
    print()
    print("Sample sizes:")
    print(f"  - Raw pairable groups in batch lab data: {raw_pairable_groups}")
    print(f"  - Batch paired groups after DV filter: {len(paired_batch)}")
    print(f"  - Learn rows after filter: {len(learn_prepped)}")
    print(f"  - Validation rows after filter: {len(val_prepped)}")
    print()
    print("Validation metrics:")
    print(metrics_df.to_string(index=False))
    print()
    print(f"Wrote outputs to: {args.output_dir}")


if __name__ == "__main__":
    main()
